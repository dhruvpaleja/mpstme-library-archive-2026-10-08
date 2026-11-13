# Computer Organization and Architecture: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 57a15e7488f3

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_AIML_7053/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & ML)/B. Tech (CSBS)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 08 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions..
6. Assume Suitable data if necessary.
Q.n   Question   Marks
o.
1
CO1 a How does Computer Organization differ from Computer Architecture? Give   5
,   examples to justify your answer
BT3   Answer:
Difference between Computer Organization and Computer Architecture: 4
Marks
Computer   Computer
Aspect
Organization   Architecture
Refers to the
operational units
Refers to the
and their
structure and
interconnections
behavior of the
that realize the
Definition   computer as seen by
architectural
the programmer. It
specifications. It
deals with what the
deals with how a
computer does.
computer system
works.
Focuses on the   Focuses on the
implementation   functional design
details such as   and instruction set
Focus
control signals, data   (ISA), addressing
paths, memory   modes, data formats,
access methods, etc.   etc.
Hardware
System design
components and
decisions that affect
their
Concerned With   performance,
interconnection—like
functionality, and
ALU, control unit,
cost.
registers, and buses.
********** 1 **********
--- page 2 ---
Viewed from the   Viewed from the
Viewpoint   hardware designer’s   programmer’s
perspective.   perspective.
- The type of
- How addition is   instructions available
Example
implemented in ALU.   in the instruction set
(RISC or CISC).
Example to Justify: 1 Marks
•   In the Intel Core i7 processor, the architecture defines it as a 64-bit
CISC processor with specific instruction sets and registers.
• The organization describes how these instructions are executed—
such as the use of pipelines, cache memory, and bus systems to
improve performance.
CO3 b Write short notes on Assembler Directives. How do they differ from   5
,   processor instructions?
BT2   Answer:
Assembler Directives are commands or instructions given to the assembler
(not to the processor) to control the assembly process. They provide
information about how the program should be translated into machine code
but do not generate any machine instructions themselves.
They help in defining data, reserving memory space, setting program start
addresses, and controlling code organization. 1 Marks
Example(any 3) with explanation: 3 marks
DB: Define Byte
DW: Define Word
ENDP, PROC, EQU,
Processor
Aspect   Assembler Directives
Instructions
Guide the assembler   Perform actual
Purpose   during program   operations during
translation.   program execution.
Handled by the
Executed by the CPU
Executed by   assembler (at
(at run time).
assembly time).
No, they do not   Yes, they generate
Generates Machine
generate machine   corresponding
Code?
code.   machine instructions.
1 Marks
CO4   c Describe the SIMD and MISD computer architectures. Support your answer   5
,   with neat diagrams.
BT2
1.SIMD (Single Instruction Multiple Data Stream) 2.5 Marks
********** 2 **********
--- page 3 ---
A SIMD system is a multiprocessor machine, capable of executing the same
instruction on all the CPUs but operating on the different data stream.
2.MISD (Multiple Instruction Single Data stream) 2.5 Marks
An MISD computing is a multiprocessor machine capable of executing
different instructions on process
single elements but all of them operating on the same data set.
CO4 d Write a note on Direct Memory Access (DMA) and its advantage over   5
,   programmed I/O.
BT2   Answer:
Direct Memory Access (DMA) is a data transfer technique that allows
peripheral devices (like disks, network cards, or sound cards) to transfer data
directly to or from the main memory without continuous involvement of the
CPU.
A special hardware component called the DMA Controller (DMAC) manages
this transfer, allowing the CPU to perform other tasks simultaneously. 3
Marks
Advantages of DMA over Programmed I/O: 2 Marks
********** 3 **********
--- page 4 ---
1. CPU is free after initializing the DMA transfer.
2. Faster because data is transferred directly between memory and
device.
3. High efficiency as CPU and I/O operations overlap.
4. Data moves directly between memory and I/O device.
Q2   a Discuss the bus hierarchy in computer systems. How do different types of   10
CO1   buses (processor-memory bus, I/O bus, backplane bus) differ in their roles?
,
BT2   Answer:
• The traditional bus architecture is reasonably efficient but begins to
break down as higher and higher performance is seen in the I/O devices.
•   In response to these growing demands, a common approach taken by
industry is to build a high speed bus that is closely integrated with the
rest of the system, requiring only a bridge between the processor’s bus
and the high speed bus
•   This arrangement is sometimes known as a mezzanine architecture.
• There is a local bus that connects the processor to a cache controller ,
which is in turn connected to a system bus that supports main memory.
• The cache controller is integrated into a bridge , or buffering device, that
connects to the high speed bus.
• This bus supports connections to high speed LANs, video and graphics
workstation controllers, SCSI and Fire Wire.
• Lower speed devices are still supported off an expansion bus, with an
interface buffering traffic between the expansion bus and the high speed bus.
• The advantage of this arrangement is that the high speed bus brings high
demand devices into closer integration with the processor and at the same
time is independent of the processor.
********** 4 **********
--- page 5 ---
CO2 b A computer system with Direct Mapping, has a main memory of size 4 GB and 10
,   a cache of size 1 MB. The block size is 4 KB.
BT3   1. Calculate the number of bits required for the physical address.
2. Find the number of blocks in main memory.
3. Determine the number of lines in cache.
4. How many tag bits are required?
Answer:
• Main memory = 4 GB = 4×2304 \times 2^{30}4×230 bytes.
• Cache = 1 MB = 2202^{20}220 bytes.
•   Block size = 4 KB = 2122^{12}212 bytes.
• Mapping = Direct mapping.
1) Number of bits required for the physical address 2.5Marks
2) Number of blocks in main memory 2.5Marks
Number of main-memory blocks = (main memory bytes) / (block size bytes).
3.) Number of lines in cache 2.5Marks
4) Number of tag bits required (direct-mapped) 2.5Marks
********** 5 **********
--- page 6 ---
Q3   a Describe in detail the various phases of the Basic Instruction Cycle. Explain   10
CO1   each phase with the help of a neat and labeled diagram.
,   Answer:
BT2   Diagram: 4 Marks
Explanation of all phases: 6 Marks
1.Instruction fetch
It is the process in which we bring the instruction from memory to the CPU.
When the CPU wants to execute the first Instruction I1 of the program, it
fetches an instruction from memory to the CPU.
For example, in the above figure, when the CPU wants to execute the first
instruction, it must have a program counter having a value of 200.
Instruction decode
********** 6 **********
--- page 7 ---
When instruction is copied to the instruction register from memory to CPU, it
contains the instruction's opcode, which is decoded by CPU. When the CPU
decodes the instruction's opcode and gets to know what operation to
perform, this process is called Instruction Decode.
3. Effective Address Calculation
Every instruction has two parts, one is the opcode, another is operand
information. Opcode has already been decoded by CPU, and now CPU
decodes the operand information from where it obtained the effective
address.
4. Operand Fetch
To execute the program, operands are needed, stored in somewhere memory
in the form of data, and that are fetched by CPU from memory; the process is
called operand fetch. For example, a, b is the data stored somewhere in the
memory. It is fetched by CPU from memory.
5. Execution
When the operation is performed on data, and the result is generated to the
Accumulator. This process is called execution. For example, the operation is
performed on data a, b, and generated to Accumulator.
6. Write back result
Finally, after the result is generated in Accumulator, it is copied to
destination c. the result is written back or copied back to the destination in
memory.
CO2 b Perform multiplication of (−6) × (2) using Booth’s algorithm. Show all steps of   10
,   the calculation.
BT3   Correct initial values in A Q and Q-1 (2marks)
Four correct step of calculation (2marks for each step)
Q4   a What is Content Addressable Memory. Describe the operation of Content   10
CO2   Addressable Memory (CAM) with the help of a diagram.
,
BT2   Answer: explanation 3Marks
• A memory unit accessed by content of data rather than address is
also known as content addressable memory(CAM).
• The content is accessed parallel on the basis of data rather than
specific address or location
• A search can be done entire word or specific field within a word.
•   It is more expensive because each cell consist the storage capacity
and logic circuits for matching its content.
•   Example: Neural network for pattern search, Google
********** 7 **********
--- page 8 ---
diagram 3marks
•   Searching word contained by argument register (A) with n-bits ,1-bit
for word
• A is matched with AM then it is placed in match register as 1
otherwise it is denoted with 0.
•   Content is searched based on portion then store in key register
indicating by 1 other bits represented by 0
•   Complete word need to search the k will content all 1’s otherwise
specific position contains 1.
•   Reading is performed in sequential; writing is performed in empty
cells.
Explanation of dia with example: 4 marks
CO2 b Explain the working of the Intel 8087 Math Coprocessor with block diagram.   10
,   What are its major functionalities?
BT2
• The Intel 8087 was first math co-processor suited for operations of
16 bit.
•   It was built to be paired with the Intel 8086 Microprocessor.
•   Its main purpose was to decrease time required by the applications
to give output (that require high floating point computations).
With introduction of co-processor along with the main processor, it
was noticed that performance of the applications improved from 20%
to 500%.
********** 8 **********
--- page 9 ---
Diagram: 3 marks
Control Unit
•   data buffer
•   shared operand queue
•   control, and status word register
•   addressing and bus tracking unit
• and exception pointer.
Numerical Execution Unit
•   register stack
•   microcode control unit
• programmable shifter
•   arithmetic module
•   temporary registers
•   shared operand queue
exponent module
5 marks for explanation.
Major Functionalities of 8087 2marks
1. Floating-Point Arithmetic Operations:
o   Addition, subtraction, multiplication, division.
2. Transcendental Functions:
o Square root, exponentiation, logarithm, sine, cosine, tangent.
3. Data Conversion:
o Conversion between integer and floating-point formats.
Q5   a Explain in detail the basic elements of cache memory design. Discuss the   10
CO2   function and importance of each element.
,   2 marks for explanation of each (any 5)
BT2
There are a few basic design elements that serve to classify and differentiate
cache architectures. They are :
1.Cache Addresses: Physical Cache and Logica cache
2.Cache Size: The total amount of data the cache can store, usually measured
in kilobytes (KB) or megabytes (MB).
3.Mapping Function:
The mapping function determines how blocks from main memory are
placed into cache lines.
********** 9 **********
--- page 10 ---
Types of Mapping:
1. Direct Mapping:
Each block of main memory maps to exactly one cache line.
o Simple and fast but prone to conflicts.
2. Fully Associative Mapping:
Any block can be placed anywhere in the cache.
o   Flexible but requires complex hardware.
3. Set-Associative Mapping:
Compromise between the two; cache is divided into sets, and each
block maps to a specific set.
o Balances speed and flexibility.
4.Replacement Algorithm: When the cache is full and new data needs to be
loaded, the replacement algorithm decides which cache line to evict.
Common Replacement Policies:
1. Least Recently Used (LRU): Replaces the block that hasn’t been used
for the longest time.
2. First-In First-Out (FIFO): Replaces the oldest block in the cache.
3. Random Replacement: Randomly selects a block to replace.
5.Write Policy:
Determines how updates to data in the cache are written to the main
memory.
Types of Write Policies:
1. Write-Through:
Data is written simultaneously to both cache and main memory.
o Simpler and ensures consistency but slower.
2. Write-Back:
Data is written only to the cache initially and to main memory later
when replaced.
o Faster but requires a dirty bit to track modified data.
6.Line Size: The amount of data transferred between main memory and cache
during one operation, typically a few bytes to several words.
7.Number of caches:
L1 Cache: Smallest and fastest (closest to CPU).
L2 Cache: Larger, slightly slower.
L3 Cache: Shared among cores, larger but slower than L2.
CO2 b Explain the different techniques used to represent signed integer numbers — 10
,   Sign-Magnitude Representation, 1’s Complement, and 2’s Complement.
BT3   Discuss each method in detail and state the drawbacks/advantage of each.
Answer:
• To represent negative numbers various techniques are because
computer does not have provision to represent negative sign.
•   Technique to represent signed integer numbers :
•   Sign-magnitude representation
•   1's complement
•   2's complement
Sign-magnitude representation: 3 marks
********** 10 **********
--- page 11 ---
•   In case of unsigned 8-bit binary numbers the decimal range is 0 to
255.
•   For sign-magnitude 8-bit numbers the largest magnitude is reduced
from 255 to 127 because we need to represent both positive and
negative numbers.
• Maximum positive number 0 1 1 1 1 1 1 1 = +127
• Maximum negative number 1 1 1 1 1 1 1 1 =- 127
•   Drawbacks of sign-magnitude representation
•   For addition and subtraction, it is necessary to consider signs
of both the numbers and their relative magnitudes in order to
carry out the required arithmetic operation.
•   There are two representations of zeros :
•   +010= 0000 0000
•   -010 = 1000 0000
• Due to the two representations of zero, it is more difficult to
test for zero operation frequently performed by the computer.
1's Complement Representation: 2 Marks
•   In the 1's complement representation, negative numbers are
obtained by complementing each bit of the corresponding positive
number.
•   Thus, the representation for -4 is obtained by complementing each bit
in the vector 0100 to yield 1011.
• The operation of obtaining the 1's complement of a number is
equivalent to subtraction that numbers from 2n-1 that is from 1111 in
case of 4-bit no.
Two's Complement Representation:
5 Marks with example and advantage
• The two's complement number is obtained by subtracting
corresponding positive number from 2n.
•   Hence, the 2's complement number is obtained by adding 1 to the 1's
complement number.
********** 11 **********
--- page 12 ---
•   Advantages of 2's complement representation
• From Table 2.1 we can note that there are distinct + 0 and -0
representations in both the sign-magnitude and 1's
complement systems, but the 2's-complement system has
only a + 0 representation.
•   For 4-bit numbers, the value -8 is representable only in the 2's
complement system and not in other systems.
•   It is more efficient for logic circuit implementation, and one
often used in computers, for addition and subtraction
operations.
Q6   a Discuss the different types of addressing modes in 8086 with examples. Why   10
CO3   are multiple addressing modes required?
,   Answer: any 4 addressing mode with example (each carry 2.5 Marks)
BT2   The 8086 microprocessor uses various addressing modes to specify how the
operand (data) for an instruction is obtained.
An addressing mode defines the way in which the operand is selected during
instruction execution.
1. Immediate Addressing Mode
2. Register Addressing Mode
3. Direct Addressing Mode
4. Register Indirect Addressing Mode
CO4 b What is Direct Memory Access (DMA)? Explain its operation and different   10
,   transfer modes (Burst, Cycle Stealing, Interleaved).
BT2
Answer: 2 marks for what is DMA
Direct Memory Access (DMA) is a technique that allows I/O devices to
transfer data directly to or from main memory without continuous
involvement of the CPU.
In normal (programmed) I/O, the CPU manages every data transfer, which
slows down system performance.
When large blocks of data are transferred (e.g., from disk, network, or ADC),
the CPU becomes a bottleneck if it has to manage every byte.
DMA improves performance by allowing direct data movement between
peripherals and memory.
Operation of DMA (2marks)
Modes: 6 marks
(a) Burst Mode (Block Transfer Mode)
********** 12 **********
--- page 13 ---
Operation:
• The DMA controller transfers the entire block of data in one
continuous burst.
• The CPU is disabled (bus is occupied) until the entire block transfer
completes.
Characteristics:
•   Fastest transfer mode.
• CPU is inactive during transfer (no bus access).
(b) Cycle Stealing Mode
Operation:
• DMA controller transfers one word (or byte) per request.
•   After each transfer, the CPU regains control of the bus for its own
operation.
• DMA “steals” bus cycles from the CPU intermittently.
Characteristics:
• CPU and DMA alternate in using the bus.
• CPU performance slightly reduced, but not completely halted.
(c) Transparent (Interleaved) Mode
Operation:
• DMA transfers occur only when the CPU is not using the system bus.
• Data transfer happens during CPU idle cycles (instruction fetch or
memory wait states).
Characteristics:
•   Fully transparent to the CPU — CPU performance remains unaffected.
•   Requires hardware support for detecting bus idle cycles.
Q7   a Q6. Explain the organization and working of a Hardwired Control Unit with a   10
CO4   neat block diagram.
,
BT2   Explanation 6 marks diagram 4 marks
Answer:
• The Hardwired Control organization involves the control logic to be
implemented with gates, flip-flops, decoders, and other digital
circuits.
The control hardware can be viewed as a state machine that changes from
one state to another in every clock cycle, depending on the contents of the
instruction register, the condition codes, and the external inputs.
• The outputs of the state machine are the control signals. The sequence of
the operation carried out by this machine is determined by the wiring of the
logic elements and hence named “hardwired”.
• Fixed logic circuits that correspond directly to the Boolean expressions are
used to generate the control signals.
• Hardwired control is faster than micro-programmed control.
• A controller that uses this approach can operate at high speed.
• RISC architecture is based on the hardwired control unit
********** 13 **********
--- page 14 ---
The block diagram of the computer is shown in above Figure
It consists of
1.Two memory units:
✓ Main memory -for storing instructions and data, and
✓ Control memory -for storing the microprogram.
2.Six Registers:
•   Processor unit register:
✓ AC(accumulator),
✓ PC(Program Counter),
✓ AR(Address Register),
✓ DR(Data Register)
********** 14 **********
--- page 15 ---
✓ Control unit register: CAR (Control Address Register),
✓ SBR(Subroutine Register)
3.Multiplexers:
• The transfer of information among the registers in the processor is
done through multiplexers rather than a common bus.
4.ALU: The arithmetic, logic, and shift unit performs micro operations with
data from AC and DR and places the result in AC. UNIT -III Unit 4 –
Microprogrammed Control DR can receive information from AC, PC, or
memory.
5. AR can receive information from PC or DR.
PC can receive information only from AR.
6. Input data written to memory come from DR, and data read from memory
can go only to DR.
CO1 b   i. Describe the functions of a computer system with respect to Data   5
,   Processing, Storage, Movement, and Control.
BT2
Answer: explanation of each
CO3   A computer system is an electronic device that performs a variety of
,   operations on data to produce meaningful results.
BT2   Its main functions can be classified into four major categories:
• Data Processing
• Data Storage
• Data Movement
•   Control
(i) Data Processing Function 2marks
The primary function of a computer is to process data — converting raw input
into meaningful information.
• Data processing involves performing operations such as arithmetic
(addition, subtraction, etc.), logical (comparison, decision-making),
and data manipulation (sorting, merging, classifying).
• The Central Processing Unit (CPU) performs these operations using
its Arithmetic Logic Unit (ALU) and Control Unit (CU).
Example:
•   Calculating employee salaries from attendance and rate of pay
(ii) Data Storage Function 1marks
A computer must be able to store data and instructions temporarily or
permanently for processing and future use.
•   Storage is divided into two main types:
1. Primary Storage (Main Memory):
.
2. Secondary Storage:
(iii) Data Movement Function 1marks
Data must be moved from one location to another — either within the
computer or between the computer and external devices.
•   Internal Data Movement: Between components inside the system,
such as from memory to CPU or vice versa.
•   External Data Movement: Between the computer and external
peripherals (e.g., keyboard, monitor, printer, network).
********** 15 **********
--- page 16 ---
(iv) Control Function 1marks
The control function coordinates all activities of the computer system to
ensure correct and orderly operation.
ii. Explain why the Program Counter (PC) is essential for instruction
execution. How does it affect program length?
Answer:
3 marks
The Program Counter (PC) is a special-purpose CPU register that holds the
address of the next instruction to be fetched from memory.
Essential Functions:
1. Instruction Sequencing:
o Ensures the CPU fetches instructions in the correct order.
o   After fetching an instruction, the PC is automatically   5
incremented to point to the next instruction (unless a branch
or jump occurs).
2. Control Flow Management:
o During jumps, branches, or subroutine calls, the PC is
updated to the target instruction address.
o Allows the program to change execution sequence
dynamically.
3. Synchronization with Memory:
o Coordinates instruction fetching between CPU and memory.
o Without PC, CPU would not know which instruction to execute
next.
Effect on Program Length   2marks
1. Address Size Determines Program Length:
o The number of bits in the PC determines the maximum
addressable memory space.
o Example:
▪   16-bit PC → 2¹⁶ = 65,536 memory locations
********** 16 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper f8ac9b84d276

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CSBS_7036/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & ML)/B. Tech (CSBS)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 08 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions..
6. Assume Suitable data if necessary.
Q.n   Question   Marks
o.
1
CO1 a How does Computer Organization differ from Computer Architecture? Give   5
,   examples to justify your answer
BT3   Answer:
Difference between Computer Organization and Computer Architecture: 4
Marks
Computer   Computer
Aspect
Organization   Architecture
Refers to the
operational units
Refers to the
and their
structure and
interconnections
behavior of the
that realize the
Definition   computer as seen by
architectural
the programmer. It
specifications. It
deals with what the
deals with how a
computer does.
computer system
works.
Focuses on the   Focuses on the
implementation   functional design
details such as   and instruction set
Focus
control signals, data   (ISA), addressing
paths, memory   modes, data formats,
access methods, etc.   etc.
Hardware
System design
components and
decisions that affect
their
Concerned With   performance,
interconnection—like
functionality, and
ALU, control unit,
cost.
registers, and buses.
********** 1 **********
--- page 2 ---
Viewed from the   Viewed from the
Viewpoint   hardware designer’s   programmer’s
perspective.   perspective.
- The type of
- How addition is   instructions available
Example
implemented in ALU.   in the instruction set
(RISC or CISC).
Example to Justify: 1 Marks
•   In the Intel Core i7 processor, the architecture defines it as a 64-bit
CISC processor with specific instruction sets and registers.
• The organization describes how these instructions are executed—
such as the use of pipelines, cache memory, and bus systems to
improve performance.
CO3 b Write short notes on Assembler Directives. How do they differ from   5
,   processor instructions?
BT2   Answer:
Assembler Directives are commands or instructions given to the assembler
(not to the processor) to control the assembly process. They provide
information about how the program should be translated into machine code
but do not generate any machine instructions themselves.
They help in defining data, reserving memory space, setting program start
addresses, and controlling code organization. 1 Marks
Example(any 3) with explanation: 3 marks
DB: Define Byte
DW: Define Word
ENDP, PROC, EQU,
Processor
Aspect   Assembler Directives
Instructions
Guide the assembler   Perform actual
Purpose   during program   operations during
translation.   program execution.
Handled by the
Executed by the CPU
Executed by   assembler (at
(at run time).
assembly time).
No, they do not   Yes, they generate
Generates Machine
generate machine   corresponding
Code?
code.   machine instructions.
1 Marks
CO4   c Describe the SIMD and MISD computer architectures. Support your answer   5
,   with neat diagrams.
BT2
1.SIMD (Single Instruction Multiple Data Stream) 2.5 Marks
********** 2 **********
--- page 3 ---
A SIMD system is a multiprocessor machine, capable of executing the same
instruction on all the CPUs but operating on the different data stream.
2.MISD (Multiple Instruction Single Data stream) 2.5 Marks
An MISD computing is a multiprocessor machine capable of executing
different instructions on process
single elements but all of them operating on the same data set.
CO4 d Write a note on Direct Memory Access (DMA) and its advantage over   5
,   programmed I/O.
BT2   Answer:
Direct Memory Access (DMA) is a data transfer technique that allows
peripheral devices (like disks, network cards, or sound cards) to transfer data
directly to or from the main memory without continuous involvement of the
CPU.
A special hardware component called the DMA Controller (DMAC) manages
this transfer, allowing the CPU to perform other tasks simultaneously. 3
Marks
Advantages of DMA over Programmed I/O: 2 Marks
********** 3 **********
--- page 4 ---
1. CPU is free after initializing the DMA transfer.
2. Faster because data is transferred directly between memory and
device.
3. High efficiency as CPU and I/O operations overlap.
4. Data moves directly between memory and I/O device.
Q2   a Discuss the bus hierarchy in computer systems. How do different types of   10
CO1   buses (processor-memory bus, I/O bus, backplane bus) differ in their roles?
,
BT2   Answer:
• The traditional bus architecture is reasonably efficient but begins to
break down as higher and higher performance is seen in the I/O devices.
•   In response to these growing demands, a common approach taken by
industry is to build a high speed bus that is closely integrated with the
rest of the system, requiring only a bridge between the processor’s bus
and the high speed bus
•   This arrangement is sometimes known as a mezzanine architecture.
• There is a local bus that connects the processor to a cache controller ,
which is in turn connected to a system bus that supports main memory.
• The cache controller is integrated into a bridge , or buffering device, that
connects to the high speed bus.
• This bus supports connections to high speed LANs, video and graphics
workstation controllers, SCSI and Fire Wire.
• Lower speed devices are still supported off an expansion bus, with an
interface buffering traffic between the expansion bus and the high speed bus.
• The advantage of this arrangement is that the high speed bus brings high
demand devices into closer integration with the processor and at the same
time is independent of the processor.
********** 4 **********
--- page 5 ---
CO2 b A computer system with Direct Mapping, has a main memory of size 4 GB and 10
,   a cache of size 1 MB. The block size is 4 KB.
BT3   1. Calculate the number of bits required for the physical address.
2. Find the number of blocks in main memory.
3. Determine the number of lines in cache.
4. How many tag bits are required?
Answer:
• Main memory = 4 GB = 4×2304 \times 2^{30}4×230 bytes.
• Cache = 1 MB = 2202^{20}220 bytes.
•   Block size = 4 KB = 2122^{12}212 bytes.
• Mapping = Direct mapping.
1) Number of bits required for the physical address 2.5Marks
2) Number of blocks in main memory 2.5Marks
Number of main-memory blocks = (main memory bytes) / (block size bytes).
3.) Number of lines in cache 2.5Marks
4) Number of tag bits required (direct-mapped) 2.5Marks
********** 5 **********
--- page 6 ---
Q3   a Describe in detail the various phases of the Basic Instruction Cycle. Explain   10
CO1   each phase with the help of a neat and labeled diagram.
,   Answer:
BT2   Diagram: 4 Marks
Explanation of all phases: 6 Marks
1.Instruction fetch
It is the process in which we bring the instruction from memory to the CPU.
When the CPU wants to execute the first Instruction I1 of the program, it
fetches an instruction from memory to the CPU.
For example, in the above figure, when the CPU wants to execute the first
instruction, it must have a program counter having a value of 200.
Instruction decode
********** 6 **********
--- page 7 ---
When instruction is copied to the instruction register from memory to CPU, it
contains the instruction's opcode, which is decoded by CPU. When the CPU
decodes the instruction's opcode and gets to know what operation to
perform, this process is called Instruction Decode.
3. Effective Address Calculation
Every instruction has two parts, one is the opcode, another is operand
information. Opcode has already been decoded by CPU, and now CPU
decodes the operand information from where it obtained the effective
address.
4. Operand Fetch
To execute the program, operands are needed, stored in somewhere memory
in the form of data, and that are fetched by CPU from memory; the process is
called operand fetch. For example, a, b is the data stored somewhere in the
memory. It is fetched by CPU from memory.
5. Execution
When the operation is performed on data, and the result is generated to the
Accumulator. This process is called execution. For example, the operation is
performed on data a, b, and generated to Accumulator.
6. Write back result
Finally, after the result is generated in Accumulator, it is copied to
destination c. the result is written back or copied back to the destination in
memory.
CO2 b Perform multiplication of (−6) × (2) using Booth’s algorithm. Show all steps of   10
,   the calculation.
BT3   Correct initial values in A Q and Q-1 (2marks)
Four correct step of calculation (2marks for each step)
Q4   a What is Content Addressable Memory. Describe the operation of Content   10
CO2   Addressable Memory (CAM) with the help of a diagram.
,
BT2   Answer: explanation 3Marks
• A memory unit accessed by content of data rather than address is
also known as content addressable memory(CAM).
• The content is accessed parallel on the basis of data rather than
specific address or location
• A search can be done entire word or specific field within a word.
•   It is more expensive because each cell consist the storage capacity
and logic circuits for matching its content.
•   Example: Neural network for pattern search, Google
********** 7 **********
--- page 8 ---
diagram 3marks
•   Searching word contained by argument register (A) with n-bits ,1-bit
for word
• A is matched with AM then it is placed in match register as 1
otherwise it is denoted with 0.
•   Content is searched based on portion then store in key register
indicating by 1 other bits represented by 0
•   Complete word need to search the k will content all 1’s otherwise
specific position contains 1.
•   Reading is performed in sequential; writing is performed in empty
cells.
Explanation of dia with example: 4 marks
CO2 b Explain the working of the Intel 8087 Math Coprocessor with block diagram.   10
,   What are its major functionalities?
BT2
• The Intel 8087 was first math co-processor suited for operations of
16 bit.
•   It was built to be paired with the Intel 8086 Microprocessor.
•   Its main purpose was to decrease time required by the applications
to give output (that require high floating point computations).
With introduction of co-processor along with the main processor, it
was noticed that performance of the applications improved from 20%
to 500%.
********** 8 **********
--- page 9 ---
Diagram: 3 marks
Control Unit
•   data buffer
•   shared operand queue
•   control, and status word register
•   addressing and bus tracking unit
• and exception pointer.
Numerical Execution Unit
•   register stack
•   microcode control unit
• programmable shifter
•   arithmetic module
•   temporary registers
•   shared operand queue
exponent module
5 marks for explanation.
Major Functionalities of 8087 2marks
1. Floating-Point Arithmetic Operations:
o   Addition, subtraction, multiplication, division.
2. Transcendental Functions:
o Square root, exponentiation, logarithm, sine, cosine, tangent.
3. Data Conversion:
o Conversion between integer and floating-point formats.
Q5   a Explain in detail the basic elements of cache memory design. Discuss the   10
CO2   function and importance of each element.
,   2 marks for explanation of each (any 5)
BT2
There are a few basic design elements that serve to classify and differentiate
cache architectures. They are :
1.Cache Addresses: Physical Cache and Logica cache
2.Cache Size: The total amount of data the cache can store, usually measured
in kilobytes (KB) or megabytes (MB).
3.Mapping Function:
The mapping function determines how blocks from main memory are
placed into cache lines.
********** 9 **********
--- page 10 ---
Types of Mapping:
1. Direct Mapping:
Each block of main memory maps to exactly one cache line.
o Simple and fast but prone to conflicts.
2. Fully Associative Mapping:
Any block can be placed anywhere in the cache.
o   Flexible but requires complex hardware.
3. Set-Associative Mapping:
Compromise between the two; cache is divided into sets, and each
block maps to a specific set.
o Balances speed and flexibility.
4.Replacement Algorithm: When the cache is full and new data needs to be
loaded, the replacement algorithm decides which cache line to evict.
Common Replacement Policies:
1. Least Recently Used (LRU): Replaces the block that hasn’t been used
for the longest time.
2. First-In First-Out (FIFO): Replaces the oldest block in the cache.
3. Random Replacement: Randomly selects a block to replace.
5.Write Policy:
Determines how updates to data in the cache are written to the main
memory.
Types of Write Policies:
1. Write-Through:
Data is written simultaneously to both cache and main memory.
o Simpler and ensures consistency but slower.
2. Write-Back:
Data is written only to the cache initially and to main memory later
when replaced.
o Faster but requires a dirty bit to track modified data.
6.Line Size: The amount of data transferred between main memory and cache
during one operation, typically a few bytes to several words.
7.Number of caches:
L1 Cache: Smallest and fastest (closest to CPU).
L2 Cache: Larger, slightly slower.
L3 Cache: Shared among cores, larger but slower than L2.
CO2 b Explain the different techniques used to represent signed integer numbers — 10
,   Sign-Magnitude Representation, 1’s Complement, and 2’s Complement.
BT3   Discuss each method in detail and state the drawbacks/advantage of each.
Answer:
• To represent negative numbers various techniques are because
computer does not have provision to represent negative sign.
•   Technique to represent signed integer numbers :
•   Sign-magnitude representation
•   1's complement
•   2's complement
Sign-magnitude representation: 3 marks
********** 10 **********
--- page 11 ---
•   In case of unsigned 8-bit binary numbers the decimal range is 0 to
255.
•   For sign-magnitude 8-bit numbers the largest magnitude is reduced
from 255 to 127 because we need to represent both positive and
negative numbers.
• Maximum positive number 0 1 1 1 1 1 1 1 = +127
• Maximum negative number 1 1 1 1 1 1 1 1 =- 127
•   Drawbacks of sign-magnitude representation
•   For addition and subtraction, it is necessary to consider signs
of both the numbers and their relative magnitudes in order to
carry out the required arithmetic operation.
•   There are two representations of zeros :
•   +010= 0000 0000
•   -010 = 1000 0000
• Due to the two representations of zero, it is more difficult to
test for zero operation frequently performed by the computer.
1's Complement Representation: 2 Marks
•   In the 1's complement representation, negative numbers are
obtained by complementing each bit of the corresponding positive
number.
•   Thus, the representation for -4 is obtained by complementing each bit
in the vector 0100 to yield 1011.
• The operation of obtaining the 1's complement of a number is
equivalent to subtraction that numbers from 2n-1 that is from 1111 in
case of 4-bit no.
Two's Complement Representation:
5 Marks with example and advantage
• The two's complement number is obtained by subtracting
corresponding positive number from 2n.
•   Hence, the 2's complement number is obtained by adding 1 to the 1's
complement number.
********** 11 **********
--- page 12 ---
•   Advantages of 2's complement representation
• From Table 2.1 we can note that there are distinct + 0 and -0
representations in both the sign-magnitude and 1's
complement systems, but the 2's-complement system has
only a + 0 representation.
•   For 4-bit numbers, the value -8 is representable only in the 2's
complement system and not in other systems.
•   It is more efficient for logic circuit implementation, and one
often used in computers, for addition and subtraction
operations.
Q6   a Discuss the different types of addressing modes in 8086 with examples. Why   10
CO3   are multiple addressing modes required?
,   Answer: any 4 addressing mode with example (each carry 2.5 Marks)
BT2   The 8086 microprocessor uses various addressing modes to specify how the
operand (data) for an instruction is obtained.
An addressing mode defines the way in which the operand is selected during
instruction execution.
1. Immediate Addressing Mode
2. Register Addressing Mode
3. Direct Addressing Mode
4. Register Indirect Addressing Mode
CO4 b What is Direct Memory Access (DMA)? Explain its operation and different   10
,   transfer modes (Burst, Cycle Stealing, Interleaved).
BT2
Answer: 2 marks for what is DMA
Direct Memory Access (DMA) is a technique that allows I/O devices to
transfer data directly to or from main memory without continuous
involvement of the CPU.
In normal (programmed) I/O, the CPU manages every data transfer, which
slows down system performance.
When large blocks of data are transferred (e.g., from disk, network, or ADC),
the CPU becomes a bottleneck if it has to manage every byte.
DMA improves performance by allowing direct data movement between
peripherals and memory.
Operation of DMA (2marks)
Modes: 6 marks
(a) Burst Mode (Block Transfer Mode)
********** 12 **********
--- page 13 ---
Operation:
• The DMA controller transfers the entire block of data in one
continuous burst.
• The CPU is disabled (bus is occupied) until the entire block transfer
completes.
Characteristics:
•   Fastest transfer mode.
• CPU is inactive during transfer (no bus access).
(b) Cycle Stealing Mode
Operation:
• DMA controller transfers one word (or byte) per request.
•   After each transfer, the CPU regains control of the bus for its own
operation.
• DMA “steals” bus cycles from the CPU intermittently.
Characteristics:
• CPU and DMA alternate in using the bus.
• CPU performance slightly reduced, but not completely halted.
(c) Transparent (Interleaved) Mode
Operation:
• DMA transfers occur only when the CPU is not using the system bus.
• Data transfer happens during CPU idle cycles (instruction fetch or
memory wait states).
Characteristics:
•   Fully transparent to the CPU — CPU performance remains unaffected.
•   Requires hardware support for detecting bus idle cycles.
Q7   a Q6. Explain the organization and working of a Hardwired Control Unit with a   10
CO4   neat block diagram.
,
BT2   Explanation 6 marks diagram 4 marks
Answer:
• The Hardwired Control organization involves the control logic to be
implemented with gates, flip-flops, decoders, and other digital
circuits.
The control hardware can be viewed as a state machine that changes from
one state to another in every clock cycle, depending on the contents of the
instruction register, the condition codes, and the external inputs.
• The outputs of the state machine are the control signals. The sequence of
the operation carried out by this machine is determined by the wiring of the
logic elements and hence named “hardwired”.
• Fixed logic circuits that correspond directly to the Boolean expressions are
used to generate the control signals.
• Hardwired control is faster than micro-programmed control.
• A controller that uses this approach can operate at high speed.
• RISC architecture is based on the hardwired control unit
********** 13 **********
--- page 14 ---
The block diagram of the computer is shown in above Figure
It consists of
1.Two memory units:
✓ Main memory -for storing instructions and data, and
✓ Control memory -for storing the microprogram.
2.Six Registers:
•   Processor unit register:
✓ AC(accumulator),
✓ PC(Program Counter),
✓ AR(Address Register),
✓ DR(Data Register)
********** 14 **********
--- page 15 ---
✓ Control unit register: CAR (Control Address Register),
✓ SBR(Subroutine Register)
3.Multiplexers:
• The transfer of information among the registers in the processor is
done through multiplexers rather than a common bus.
4.ALU: The arithmetic, logic, and shift unit performs micro operations with
data from AC and DR and places the result in AC. UNIT -III Unit 4 –
Microprogrammed Control DR can receive information from AC, PC, or
memory.
5. AR can receive information from PC or DR.
PC can receive information only from AR.
6. Input data written to memory come from DR, and data read from memory
can go only to DR.
CO1 b   i. Describe the functions of a computer system with respect to Data   5
,   Processing, Storage, Movement, and Control.
BT2
Answer: explanation of each
CO3   A computer system is an electronic device that performs a variety of
,   operations on data to produce meaningful results.
BT2   Its main functions can be classified into four major categories:
• Data Processing
• Data Storage
• Data Movement
•   Control
(i) Data Processing Function 2marks
The primary function of a computer is to process data — converting raw input
into meaningful information.
• Data processing involves performing operations such as arithmetic
(addition, subtraction, etc.), logical (comparison, decision-making),
and data manipulation (sorting, merging, classifying).
• The Central Processing Unit (CPU) performs these operations using
its Arithmetic Logic Unit (ALU) and Control Unit (CU).
Example:
•   Calculating employee salaries from attendance and rate of pay
(ii) Data Storage Function 1marks
A computer must be able to store data and instructions temporarily or
permanently for processing and future use.
•   Storage is divided into two main types:
1. Primary Storage (Main Memory):
.
2. Secondary Storage:
(iii) Data Movement Function 1marks
Data must be moved from one location to another — either within the
computer or between the computer and external devices.
•   Internal Data Movement: Between components inside the system,
such as from memory to CPU or vice versa.
•   External Data Movement: Between the computer and external
peripherals (e.g., keyboard, monitor, printer, network).
********** 15 **********
--- page 16 ---
(iv) Control Function 1marks
The control function coordinates all activities of the computer system to
ensure correct and orderly operation.
ii. Explain why the Program Counter (PC) is essential for instruction
execution. How does it affect program length?
Answer:
3 marks
The Program Counter (PC) is a special-purpose CPU register that holds the
address of the next instruction to be fetched from memory.
Essential Functions:
1. Instruction Sequencing:
o Ensures the CPU fetches instructions in the correct order.
o   After fetching an instruction, the PC is automatically   5
incremented to point to the next instruction (unless a branch
or jump occurs).
2. Control Flow Management:
o During jumps, branches, or subroutine calls, the PC is
updated to the target instruction address.
o Allows the program to change execution sequence
dynamically.
3. Synchronization with Memory:
o Coordinates instruction fetching between CPU and memory.
o Without PC, CPU would not know which instruction to execute
next.
Effect on Program Length   2marks
1. Address Size Determines Program Length:
o The number of bits in the PC determines the maximum
addressable memory space.
o Example:
▪   16-bit PC → 2¹⁶ = 65,536 memory locations
********** 16 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 2a2cb2896a7e

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_Computer_7002/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B.
Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 04 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. Assume Suitable data if necessary
Q.no   Questions   Mark
.   s
Q1
CO1, a Analyze the functional view of a computer and explain how different operations   5
BT2   (input, processing, output, storage) are coordinated during program execution.
Ans: 1 marks for each
There are four main functions of a computer:
• Data processing : Data may take a wide variety of forms and the range of
processing requirements is broad
• Data storage :
✓ Short-term
✓ Long-term
• Data movement:
✓ Input-output (I/O) - when data are received from or delivered to a
device (peripheral) that is directly connected to the computer
✓ Data communications – when data are moved over longer distances, to
or from a remote device
• Control
A control unit manages the computer’s resources and coordinates the
performance of its functional parts in response to instructions
During execution: 1 marks
• Control unit fetches instructions
• Decodes them
• Executes using ALU
•   Stores results in memory or sends to output
CO3, b What are the different types of registers in a CPU?   5
BT2   Ans:
1.25m for each type
********** 1 **********
--- page 2 ---
1. Accumulator : used to hold an operand and result of an ALU operation
2. General Purpose registers to hold data
3. Segment / Index / pointer registers to hold memory address
4. Status / Flag registers to indicate status of ALU operation ( Sign, Zero, Carry,
parity etc.)
CO4, c Define following:   5
BT2   a. Micro-operation
b. Micro-instruction
c. Micro-program
d. Micro-code
e. Control word
Ans:
Each 1 marks
Ans.
a. Micro-operation
A micro-operation is a basic operation performed on data stored in registers
within the CPU.
b. Micro-instruction
A micro-instruction is a binary control instruction that specifies one or more
micro-operations to be executed at a given time.
c. Micro-program
A micro-program is a sequence of micro-instructions stored in control memory
that implements a machine-level instruction.
d. Micro-code
Micro-code refers to the set of micro-instructions used to implement the
instruction set of a processor.
e. Control Word
A control word is a binary pattern of control signals that specifies the operations to be
performed in a single clock cycle.
CO4, d Explain superscalar architecture and its working principle.   5
BT4
Marks Bifurcation
Definition: 2 Marks
Working Principle: 3 Marks
Answer-
Superscalar architecture is a processor design that allows execution of multiple
instructions in a single clock cycle.
It works by using multiple pipelines and execution units. The processor fetches,
decodes, and dispatches multiple instructions simultaneously. Techniques like
instruction-level parallelism and out-of-order execution help improve
performance.
********** 2 **********
--- page 3 ---
This results in higher throughput and better CPU utilization.
Q2   a Describe, what is system bus arbitration? Explain the method of centralized bus   10
CO1,   arbitration in brief with diagram.
BT2
Ans: [1 marks defination]
bus arbitration : is who can use the Bus a specific time or More than one
module controlling the bus
• Bus Arbitration refers to the process by which the current bus master
accesses and then leaves the control of the bus and passes it to the another
bus requesting processor unit
• The controller that has access to a bus at an instance is known as Bus master
Method of centralized bus arbitration: 3 marks for each
(i)   Daisy Chaining method –
✓ It is a centralized bus arbitration method.
✓ It is a simple and cheaper method where all the bus masters use the same
line for making bus requests.
✓ The bus grant signal serially propagates through each master until it
encounters the first one that is requesting access to the bus.
✓ This master blocks the propagation of the bus grant signal, therefore any
other requesting module will not receive the grant signal and hence cannot
access the bus.
During any bus cycle, the bus master may be any device – the processor or any
DMA controller unit, connected to the bus.
ii)Polling or Rotating Priority method
✓ In this, the controller is used to generate the address for the master(unique
priority), the number of address lines required depends on the number of
masters connected in the system.
✓ the priorities are dynamically changed to give every device an opportunity
to access the bus.
✓ The controller generates a sequence of master addresses.
✓ When the requesting master recognizes its address, it activates the busy line
and begins to use the bus.
********** 3 **********
--- page 4 ---
(iii) Fixed priority or Independent Request method
✓ In this, each master has a separate pair of bus request and bus grant lines
and each pair has a priority assigned to it.
The built-in priority decoder within the controller selects the highest priority
request   and   asserts   the   corresponding   bus   grant   signal.
CO2, b Consider a computer system with the following cache specifications:   10
BT3   • Cache size = 256 KB
• Block size = 64 bytes
• Mapping technique = Direct mapping
• Main memory size = 4 MB
Assume that the system uses byte-addressable memory. Divide the main memory
address into Tag, Index, and Block Offset fields, clearly specifying the number of
bits in each.
Ans:
2.5 marks for each Step:
********** 4 **********
--- page 5 ---
Final division of the 22-bit main memory address:
Field   Number of Bits
Tag   4 bits
Index   12 bits
Block Offset 6 bits
Q3   a Explain hardware interrupts and software interrupts in detail. Compare the   10
CO1,   interrupt-driven I/O method with the polling method and justify why interrupts are
BT2   more efficient.
Ans:
1. Hardware Interrupts 2 marks
Definition:
Hardware interrupts are signals sent to the CPU by external hardware devices to
indicate they need immediate attention.
• Triggered by external events (e.g., keyboard input, mouse click, I/O device
ready).
• Asynchronous to the CPU’s current operations.
Software Interrupts 2 marks
Definition:
Software interrupts are generated by programs or the CPU itself to request OS
services or handle exceptional conditions.
• Triggered by executing specific instructions (e.g., INT in x86 assembly).
• Synchronous with program execution.
• Used for system calls, debugging, or handling errors like divide-by-zero.
Comparison: 4 Marks
********** 5 **********
--- page 6 ---
Why Interrupts Are More Efficient : 2 marks
1. Eliminate   Wasteful   Waiting:
Interrupts free the CPU from continuous checking, allowing it to execute
other instructions until the device needs attention.
2. Better   CPU   Utilization:
CPU resources are used more effectively for useful work rather than polling.
CO2, b Compare the IEEE 754 single precision and double precision formats. Show the   10
BT3   representations side by side and state two practical scenarios where double
precision is preferred over single precision.
Ans: 8 marks for Difference
1. Bit-Level Representation (Side-by-Side)
Component   Single Precision (32-bit) Double Precision (64-bit)
Sign bit   1 bit   1 bit
Exponent   8 bits   11 bits
Mantissa (Fraction) 23 bits   52 bits
Total Size   32 bits   64 bits
2. Format Structure
Single Precision (32-bit)
| S | Exponent (8 bits) | Fraction (23 bits) |
Double Precision (64-bit)
| S | Exponent (11 bits) | Fraction (52 bits) |
3. Key Differences
Feature   Single Precision   Double Precision
Precision   ~6–7 decimal digits ~15–16 decimal digits
Range   Smaller   Much larger
Memory usage   4 bytes   8 bytes
Computational speed Faster   Slightly slower
********** 6 **********
--- page 7 ---
Rounding error   Higher   Lower
When Double Precision is Preferred (Any Two Scenarios) : 2 marks
1. Scientific and Engineering Calculations
Used in simulations such as:
• Weather forecasting
•   Fluid dynamics
•   Structural engineering analysis
Reason: These applications require high numerical accuracy and small rounding
errors can significantly affect results.
2. Financial and Statistical Computations
Used in:
• Risk analysis models
•   Large-scale financial forecasting
• Machine learning statistical computations
Q4   a Explain the concept of Content Addressable Memory (CAM). Describe its working   10
CO2,   principle with a neat diagram.
BT2   And:
Explain the concept of Content Addressable Memory (CAM) 2 marks
• A memory unit accessed by content of data rather than address is also known
as content addressable memory(CAM).
• The content is accessed parallel on the basis of data rather than specific
address or location
• A search can be done entire word or specific field within a word.
•   It is more expensive because each cell consist the storage capacity and logic
circuits for matching its content.
• Example: Neural network for pattern search, Google
working principle:
********** 7 **********
--- page 8 ---
diagram=3 marks
•   Searching word contained by argument register (A) with n-bits ,1-bit for
word
• A is matched with AM then it is placed in match register as 1 otherwise it is
denoted with 0.
• Content is searched based on portion then store in key register indicating
by 1 other bits represented by 0
• Complete word need to search the k will content all 1’s otherwise specific
position contains 1.
• Reading is performed in sequential; writing is performed in empty cells.
[Explanation 5 marks]
CO2, b Explain the design and working of a 4-bit parallel adder–subtractor with a neat   10
BT2   diagram. Illustrate how the circuit performs both addition and subtraction using
control logic. Also state the advantages and disadvantages of the parallel adder–
subtractor.
Ans:
[Diagram with explanation 6 marks ]
********** 8 **********
--- page 9 ---
• Advantages of parallel Adder/Subtractor [2 marks]
1. The parallel adder/subtractor performs the addition operation faster as
compared to serial adder/subtractor.
2. Time required for addition does not depend on the number of bits.
3. The output is in parallel form i.e all the bits are added/subtracted at the same
time.
4. It is less costly.
• Disadvantages of parallel Adder/Subtractor [2 marks]
1. Each adder has to wait for the carry to come from the previous adder in the
chain.
2. The propagation delay( delay associated with the travelling of carry bit) is
found to increase with the increase in the number of bits to be added.
Q5   a Explain the concept of the Translation Lookaside Buffer (TLB) and its working   10
CO2,   mechanism. Discuss why a TLB is required in modern computer systems. Illustrate
BT 2   your answer with a suitable diagram.
Ans:
(a)The Translation Lookaside Buffer (TLB) is a high-speed hardware
cache situated inside or near the Memory Management Unit (MMU). It
stores the most recently used mappings between Virtual Page Numbers
(VPNs) and Physical Frame Numbers (PFNs), reducing the need for
frequent page table lookups.
• Acts as a quick reference for recent virtual-to-physical address
translations.
•   Significantly speeds up memory access by minimizing main memory
lookups.
• Enhances overall CPU performance and efficiency in address translation.
********** 9 **********
--- page 10 ---
[diagram 4 Marks]
Reasons to use TLB : [explanation 6 marks]
When the CPU generates a virtual address, it must be translated into a physical
address to access data in main memory. The naive approach stores the entire page
table in main memory. Therefore, for every memory access, the following two
memory accesses are required:
1. Access the page table in main memory to get the frame number.
2. Access the actual data in the main memory frame.
3. This leads to a performance problem, as every memory access now
requires two memory accesses, causing a significant slowdown. 3M
CO2, b Apply Booth’s Algorithm to multiply 7 × 3 using 4-bit representation and show all   10
BT3   intermediate steps. Also, draw and explain the hardware structure of Booth’s
multiplier.
Ans: 5 marks for Solution
Step A B (Q) Q-1   Operation
INIT 0000 0011 0   Initial values
1   1001 0011 0 A ← A − M (10)
1   1100 1001 1   Arithmetic right shift
2   1100 1001 1 No operation (11)
2   1110 0100 1   Arithmetic right shift
3   0101 0100 1 A ← A + M (01)
3   0010 1010 0   Arithmetic right shift
4   0010 1010 0 No operation (00)
4   0001 0101 0   Arithmetic right shift
********** 10 **********
--- page 11 ---
2 marks= diagram
• The Booth's algorithm can be implemented as shown in the Fig. 2.19.
• The circuit is similar to circuit for positive number multiplication.
•   It consists of n-bit adder, shift, add subtract control logic and four registers,
A, B, Q and Q -1.
• As shown in the Fig. 2.19 multiplier and multiplicand are loaded into
register Q and register B, respectively, and register A and (2-1 are initially
set to 0.
3 marks explanation
Q6   a Explain the architecture of the 8086 microprocessors with a neat and labeled   10
CO3,   diagram. Describe the functions of its major components in detail.
BT2
Diagram of architecture: 4m
Explanation of Execution unit: 3m
Explanation of Bus Interface unit: 3m
The internal architecture of Intel 8086 is divided into 2 units: The Bus Interface Unit
(BIU), and The Execution Unit (EU).
********** 11 **********
--- page 12 ---
1. The Bus Interface Unit (BIU):It provides the interface of 8086 to external memory and
I/O devices via the System Bus. It performs various machine cycles such as memory read,
I/O   read,   etc.   to   transfer   data between memory and   I/O   devices.
BIU performs the following functions are as follows:
●   It generates the 20-bit physical address for memory access.
●   It fetches instructions from the memory.
●   It transfers data to and from the memory and I/O.
● Supports pipelining
BIU mainly contains the 4 Segment registers, the Instruction Pointer, a pre-fetch queue,
and an Address Generation Circuit.
Instruction Pointer (IP):
●   It is a 16-bit register. It holds offset of the next instructions in the Code
Segment.
●   IP is incremented after every instruction byte is fetched.
Code Segment register: (16 Bit register): CS holds the base address for the Code
Segment. All programs are stored in the Code Segment and accessed via the IP.
Data Segment register: (16 Bit register): DS holds the base address for the Data
Segment.
Stack Segment register: (16 Bit register): SS holds the base address for the Stack
Segment.
Extra Segment register: (16 Bit register): ES holds the base address for the Extra
Segment.
Address Generation Circuit:
● The BIU has a Physical Address Generation Circuit.
●   It generates the 20-bit physical address using Segment and Offset addresses
using the formula:
●   In Bus Interface Unit (BIU) the circuit shown by the Σ symbol is responsible for
the calculation unit which is used to calculate the physical address of an
instruction in memory.
Pre-fetch Queue:
●   It is a 6-byte queue (FIFO).
● Fetching the next instruction (by BIU from CS) while executing the current
instruction is called pipelining.
● Gets flushed whenever a branch instruction occurs.
● The pre-Fetch queue is of 6-Bytes only because the maximum size of instruction
that can have in 8086 is 6 bytes. Hence to cover up all operands and data fields
of maximum size instruction in 8086 Microprocessor there is a Pre-Fetch queue
is 6 Bytes.
2. The Execution Unit (EU):
The main components of the EU are General purpose registers, the ALU, Special purpose
registers, the Instruction Register and Instruction Decoder, and the Flag/Status Register.
Fetches instructions from the Queue in BIU, decodes, and executes arithmetic and logic
operations using the ALU. Sends control signals for internal data transfer operations
within the microprocessor (Control Unit). Sends request signals to the BIU to access the
external module.
8086 has four 16-bit general purpose registers AX, BX, CX, and DX which store
intermediate values during execution. Each of these has two 8-bit parts (higher and
lower).
********** 12 **********
--- page 13 ---
Special purpose registers (16-bit): Special purpose registers are called Offset registers
also. Which points to specific memory locations under each segment.
● Stack Pointer: Points to Stack top.
● Base Pointer: BP can hold the offset addresses of any location in the stack
segment.
● Source Index: It holds an offset address in Data Segment during string
operations.
● Destination Index: It holds offset addresses in Extra Segment during string
operations.
Instruction Register and Instruction Decoder: The EU fetches an opcode from the
queue into the instruction register. The instruction decoder decodes it and sends the
information to the control circuit for execution.
Flag/Status register (16 bits): It has 9 flags that help change or recognize the state of
the microprocessor.
Control unit : The Control Unit in the 8086 microprocessor is a component that
manages the overall operation of the microprocessor. The control unit is responsible for
controlling the flow of instructions through the microprocessor and coordinating the
activities of the other components, including the Decode Unit, Execution Unit, and
Prefetch Unit.
CO4, b Differentiate between Memory-Mapped I/O and I/O-Mapped I/O. Explain their   10
BT2   working principal.
Ans: difference 6 marks
Working 4 makrs
1. Memory-Mapped I/O – Working Principle
In Memory-Mapped I/O, I/O devices are treated as part of the main memory. Each
I/O device is assigned a unique memory address within the normal memory address
space.
Working:
• The CPU generates a memory address on the address bus.
• This address may refer to either:
o A memory location, or
o An I/O device register
• The control unit does not differentiate between memory and I/O initially.
********** 13 **********
--- page 14 ---
• The address decoder identifies whether the address belongs to RAM or an
I/O device.
•   If it is an I/O address:
o The corresponding device responds just like memory would.
• CPU uses normal instructions like:
o LOAD, STORE, MOV
2. I/O-Mapped I/O (Isolated I/O) – Working Principle
In I/O-Mapped I/O, I/O devices have a separate address space distinct from
memory.
Working:
• The CPU uses special I/O instructions like IN and OUT (8086
architecture).
• When an I/O instruction is executed:
o The CPU places the I/O port address on the address bus.
o   It activates I/O control signals (IOR or IOW).
• The memory system ignores this operation because memory and I/O are
separated.
• Only the selected I/O device responds to the I/O control signal.
• Data is transferred between CPU and I/O device via accumulator/registers.
Q7   a Explain the organization and operation of an I/O Processor with a suitable diagram.   10
CO4,   Ans:
BT2
2 marks what is IOP
2 marks diagram
6 marks explanation
Input / Output Processor [2 marks]
•An input-output processor (IOP) is a processor with direct memory access
capability.
•In this, the computer system is divided into a memory unit and number of
processors.
•Each IOP controls and manage the input-output tasks.
•The IOP is similar to CPU except that it handles only the details of I/O processing.
•The IOP can fetch and execute its own instructions.
•These IOP instructions are designed to manage I/O transfers only.
BelowisablockdiagramofacomputeralongwithvariousI/OProcessors.
•Thememoryunitoccupiesthecentralpositionandcancommunicatewitheachprocessor
.
•TheCPUprocessesthedatarequiredforsolvingthecomputationaltasks.
•TheIOPprovidesapathfortransferofdatabetweenperipheralsandmemory.
********** 14 **********
--- page 15 ---
•TheCPUassignsthetaskofinitiatingtheI/Oprogram.
•TheIOPoperatesindependentfromCPUandtransferdatabetweenperipheralsandmem
ory.
The communication between the IOP and the devices is similar to the program
control method of transfer.
•And the communication with the memory is similar to the direct memory access
method.
•In large scale computers, each processor is independent of other processors and
any processor can initiate the operation.
•The CPU can act as master and the IOP act as slave processor.
•The CPU assigns the task of initiating operations but it is the IOP, who executes
the instructions, and not the CPU.
•CPU instructions provide operations to start an I/O transfer.
•The IOP asks for CPU through interrupt.
•Instructions that are read from memory by an IOP are also called commands to
distinguish them from instructions that are read by CPU.
•Commands are prepared by programmers and are stored in memory.
•Command words make the program for IOP.
•CPU informs the IOP where to find the commands in memory.
CO1, b   i.   Identify the different methods of specifying operands in an instruction.   5
BT3   Illustrate any 2 methods with an example.
Ans:
Enlist the method 1 marks
Explaination of each method 2 marks   5
The different methods used to specify operands in an instruction are called Addressing
Modes.
Common methods (Addressing Modes):
1. Immediate Addressing Mode
2. Direct Addressing Mode
3. Indirect Addressing Mode
4. Register Addressing Mode
5. Register Indirect Addressing Mode
********** 15 **********
--- page 16 ---
6. Indexed Addressing Mode
7. Base (Displacement) Addressing Mode
8. Relative Addressing Mode
Immediate Addressing Mode
In this mode, the operand (data) is specified directly in the instruction itself.
Working Principle:
• The CPU does not need to access memory for the operand.
• The value is immediately available in the instruction.
Example:
MOV AL, 05H
Direct Addressing Mode
In this mode, the address of the operand is directly given in the instruction.
Working Principle:
• The instruction contains the memory address.
• CPU goes to that memory location to fetch the operand.
Example:
MOV AL, [2000H]
CO1,   ii.   Distinguish between computer organization and architecture.
BT2
Each difference 1 marks
********** 16 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 213991748cba

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CyberSecurity_7010/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B.
Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 04 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. Assume Suitable data if necessary
Q.no   Questions   Mark
.   s
Q1
CO1, a Analyze the functional view of a computer and explain how different operations   5
BT2   (input, processing, output, storage) are coordinated during program execution.
Ans: 1 marks for each
There are four main functions of a computer:
• Data processing : Data may take a wide variety of forms and the range of
processing requirements is broad
• Data storage :
✓ Short-term
✓ Long-term
• Data movement:
✓ Input-output (I/O) - when data are received from or delivered to a
device (peripheral) that is directly connected to the computer
✓ Data communications – when data are moved over longer distances, to
or from a remote device
• Control
A control unit manages the computer’s resources and coordinates the
performance of its functional parts in response to instructions
During execution: 1 marks
• Control unit fetches instructions
• Decodes them
• Executes using ALU
•   Stores results in memory or sends to output
CO3, b What are the different types of registers in a CPU?   5
BT2   Ans:
1.25m for each type
********** 1 **********
--- page 2 ---
1. Accumulator : used to hold an operand and result of an ALU operation
2. General Purpose registers to hold data
3. Segment / Index / pointer registers to hold memory address
4. Status / Flag registers to indicate status of ALU operation ( Sign, Zero, Carry,
parity etc.)
CO4, c Define following:   5
BT2   a. Micro-operation
b. Micro-instruction
c. Micro-program
d. Micro-code
e. Control word
Ans:
Each 1 marks
Ans.
a. Micro-operation
A micro-operation is a basic operation performed on data stored in registers
within the CPU.
b. Micro-instruction
A micro-instruction is a binary control instruction that specifies one or more
micro-operations to be executed at a given time.
c. Micro-program
A micro-program is a sequence of micro-instructions stored in control memory
that implements a machine-level instruction.
d. Micro-code
Micro-code refers to the set of micro-instructions used to implement the
instruction set of a processor.
e. Control Word
A control word is a binary pattern of control signals that specifies the operations to be
performed in a single clock cycle.
CO4, d Explain superscalar architecture and its working principle.   5
BT4
Marks Bifurcation
Definition: 2 Marks
Working Principle: 3 Marks
Answer-
Superscalar architecture is a processor design that allows execution of multiple
instructions in a single clock cycle.
It works by using multiple pipelines and execution units. The processor fetches,
decodes, and dispatches multiple instructions simultaneously. Techniques like
instruction-level parallelism and out-of-order execution help improve
performance.
********** 2 **********
--- page 3 ---
This results in higher throughput and better CPU utilization.
Q2   a Describe, what is system bus arbitration? Explain the method of centralized bus   10
CO1,   arbitration in brief with diagram.
BT2
Ans: [1 marks defination]
bus arbitration : is who can use the Bus a specific time or More than one
module controlling the bus
• Bus Arbitration refers to the process by which the current bus master
accesses and then leaves the control of the bus and passes it to the another
bus requesting processor unit
• The controller that has access to a bus at an instance is known as Bus master
Method of centralized bus arbitration: 3 marks for each
(i)   Daisy Chaining method –
✓ It is a centralized bus arbitration method.
✓ It is a simple and cheaper method where all the bus masters use the same
line for making bus requests.
✓ The bus grant signal serially propagates through each master until it
encounters the first one that is requesting access to the bus.
✓ This master blocks the propagation of the bus grant signal, therefore any
other requesting module will not receive the grant signal and hence cannot
access the bus.
During any bus cycle, the bus master may be any device – the processor or any
DMA controller unit, connected to the bus.
ii)Polling or Rotating Priority method
✓ In this, the controller is used to generate the address for the master(unique
priority), the number of address lines required depends on the number of
masters connected in the system.
✓ the priorities are dynamically changed to give every device an opportunity
to access the bus.
✓ The controller generates a sequence of master addresses.
✓ When the requesting master recognizes its address, it activates the busy line
and begins to use the bus.
********** 3 **********
--- page 4 ---
(iii) Fixed priority or Independent Request method
✓ In this, each master has a separate pair of bus request and bus grant lines
and each pair has a priority assigned to it.
The built-in priority decoder within the controller selects the highest priority
request   and   asserts   the   corresponding   bus   grant   signal.
CO2, b Consider a computer system with the following cache specifications:   10
BT3   • Cache size = 256 KB
• Block size = 64 bytes
• Mapping technique = Direct mapping
• Main memory size = 4 MB
Assume that the system uses byte-addressable memory. Divide the main memory
address into Tag, Index, and Block Offset fields, clearly specifying the number of
bits in each.
Ans:
2.5 marks for each Step:
********** 4 **********
--- page 5 ---
Final division of the 22-bit main memory address:
Field   Number of Bits
Tag   4 bits
Index   12 bits
Block Offset 6 bits
Q3   a Explain hardware interrupts and software interrupts in detail. Compare the   10
CO1,   interrupt-driven I/O method with the polling method and justify why interrupts are
BT2   more efficient.
Ans:
1. Hardware Interrupts 2 marks
Definition:
Hardware interrupts are signals sent to the CPU by external hardware devices to
indicate they need immediate attention.
• Triggered by external events (e.g., keyboard input, mouse click, I/O device
ready).
• Asynchronous to the CPU’s current operations.
Software Interrupts 2 marks
Definition:
Software interrupts are generated by programs or the CPU itself to request OS
services or handle exceptional conditions.
• Triggered by executing specific instructions (e.g., INT in x86 assembly).
• Synchronous with program execution.
• Used for system calls, debugging, or handling errors like divide-by-zero.
Comparison: 4 Marks
********** 5 **********
--- page 6 ---
Why Interrupts Are More Efficient : 2 marks
1. Eliminate   Wasteful   Waiting:
Interrupts free the CPU from continuous checking, allowing it to execute
other instructions until the device needs attention.
2. Better   CPU   Utilization:
CPU resources are used more effectively for useful work rather than polling.
CO2, b Compare the IEEE 754 single precision and double precision formats. Show the   10
BT3   representations side by side and state two practical scenarios where double
precision is preferred over single precision.
Ans: 8 marks for Difference
1. Bit-Level Representation (Side-by-Side)
Component   Single Precision (32-bit) Double Precision (64-bit)
Sign bit   1 bit   1 bit
Exponent   8 bits   11 bits
Mantissa (Fraction) 23 bits   52 bits
Total Size   32 bits   64 bits
2. Format Structure
Single Precision (32-bit)
| S | Exponent (8 bits) | Fraction (23 bits) |
Double Precision (64-bit)
| S | Exponent (11 bits) | Fraction (52 bits) |
3. Key Differences
Feature   Single Precision   Double Precision
Precision   ~6–7 decimal digits ~15–16 decimal digits
Range   Smaller   Much larger
Memory usage   4 bytes   8 bytes
Computational speed Faster   Slightly slower
********** 6 **********
--- page 7 ---
Rounding error   Higher   Lower
When Double Precision is Preferred (Any Two Scenarios) : 2 marks
1. Scientific and Engineering Calculations
Used in simulations such as:
• Weather forecasting
•   Fluid dynamics
•   Structural engineering analysis
Reason: These applications require high numerical accuracy and small rounding
errors can significantly affect results.
2. Financial and Statistical Computations
Used in:
• Risk analysis models
•   Large-scale financial forecasting
• Machine learning statistical computations
Q4   a Explain the concept of Content Addressable Memory (CAM). Describe its working   10
CO2,   principle with a neat diagram.
BT2   And:
Explain the concept of Content Addressable Memory (CAM) 2 marks
• A memory unit accessed by content of data rather than address is also known
as content addressable memory(CAM).
• The content is accessed parallel on the basis of data rather than specific
address or location
• A search can be done entire word or specific field within a word.
•   It is more expensive because each cell consist the storage capacity and logic
circuits for matching its content.
• Example: Neural network for pattern search, Google
working principle:
********** 7 **********
--- page 8 ---
diagram=3 marks
•   Searching word contained by argument register (A) with n-bits ,1-bit for
word
• A is matched with AM then it is placed in match register as 1 otherwise it is
denoted with 0.
• Content is searched based on portion then store in key register indicating
by 1 other bits represented by 0
• Complete word need to search the k will content all 1’s otherwise specific
position contains 1.
• Reading is performed in sequential; writing is performed in empty cells.
[Explanation 5 marks]
CO2, b Explain the design and working of a 4-bit parallel adder–subtractor with a neat   10
BT2   diagram. Illustrate how the circuit performs both addition and subtraction using
control logic. Also state the advantages and disadvantages of the parallel adder–
subtractor.
Ans:
[Diagram with explanation 6 marks ]
********** 8 **********
--- page 9 ---
• Advantages of parallel Adder/Subtractor [2 marks]
1. The parallel adder/subtractor performs the addition operation faster as
compared to serial adder/subtractor.
2. Time required for addition does not depend on the number of bits.
3. The output is in parallel form i.e all the bits are added/subtracted at the same
time.
4. It is less costly.
• Disadvantages of parallel Adder/Subtractor [2 marks]
1. Each adder has to wait for the carry to come from the previous adder in the
chain.
2. The propagation delay( delay associated with the travelling of carry bit) is
found to increase with the increase in the number of bits to be added.
Q5   a Explain the concept of the Translation Lookaside Buffer (TLB) and its working   10
CO2,   mechanism. Discuss why a TLB is required in modern computer systems. Illustrate
BT 2   your answer with a suitable diagram.
Ans:
(a)The Translation Lookaside Buffer (TLB) is a high-speed hardware
cache situated inside or near the Memory Management Unit (MMU). It
stores the most recently used mappings between Virtual Page Numbers
(VPNs) and Physical Frame Numbers (PFNs), reducing the need for
frequent page table lookups.
• Acts as a quick reference for recent virtual-to-physical address
translations.
•   Significantly speeds up memory access by minimizing main memory
lookups.
• Enhances overall CPU performance and efficiency in address translation.
********** 9 **********
--- page 10 ---
[diagram 4 Marks]
Reasons to use TLB : [explanation 6 marks]
When the CPU generates a virtual address, it must be translated into a physical
address to access data in main memory. The naive approach stores the entire page
table in main memory. Therefore, for every memory access, the following two
memory accesses are required:
1. Access the page table in main memory to get the frame number.
2. Access the actual data in the main memory frame.
3. This leads to a performance problem, as every memory access now
requires two memory accesses, causing a significant slowdown. 3M
CO2, b Apply Booth’s Algorithm to multiply 7 × 3 using 4-bit representation and show all   10
BT3   intermediate steps. Also, draw and explain the hardware structure of Booth’s
multiplier.
Ans: 5 marks for Solution
Step A B (Q) Q-1   Operation
INIT 0000 0011 0   Initial values
1   1001 0011 0 A ← A − M (10)
1   1100 1001 1   Arithmetic right shift
2   1100 1001 1 No operation (11)
2   1110 0100 1   Arithmetic right shift
3   0101 0100 1 A ← A + M (01)
3   0010 1010 0   Arithmetic right shift
4   0010 1010 0 No operation (00)
4   0001 0101 0   Arithmetic right shift
********** 10 **********
--- page 11 ---
2 marks= diagram
• The Booth's algorithm can be implemented as shown in the Fig. 2.19.
• The circuit is similar to circuit for positive number multiplication.
•   It consists of n-bit adder, shift, add subtract control logic and four registers,
A, B, Q and Q -1.
• As shown in the Fig. 2.19 multiplier and multiplicand are loaded into
register Q and register B, respectively, and register A and (2-1 are initially
set to 0.
3 marks explanation
Q6   a Explain the architecture of the 8086 microprocessors with a neat and labeled   10
CO3,   diagram. Describe the functions of its major components in detail.
BT2
Diagram of architecture: 4m
Explanation of Execution unit: 3m
Explanation of Bus Interface unit: 3m
The internal architecture of Intel 8086 is divided into 2 units: The Bus Interface Unit
(BIU), and The Execution Unit (EU).
********** 11 **********
--- page 12 ---
1. The Bus Interface Unit (BIU):It provides the interface of 8086 to external memory and
I/O devices via the System Bus. It performs various machine cycles such as memory read,
I/O   read,   etc.   to   transfer   data between memory and   I/O   devices.
BIU performs the following functions are as follows:
●   It generates the 20-bit physical address for memory access.
●   It fetches instructions from the memory.
●   It transfers data to and from the memory and I/O.
● Supports pipelining
BIU mainly contains the 4 Segment registers, the Instruction Pointer, a pre-fetch queue,
and an Address Generation Circuit.
Instruction Pointer (IP):
●   It is a 16-bit register. It holds offset of the next instructions in the Code
Segment.
●   IP is incremented after every instruction byte is fetched.
Code Segment register: (16 Bit register): CS holds the base address for the Code
Segment. All programs are stored in the Code Segment and accessed via the IP.
Data Segment register: (16 Bit register): DS holds the base address for the Data
Segment.
Stack Segment register: (16 Bit register): SS holds the base address for the Stack
Segment.
Extra Segment register: (16 Bit register): ES holds the base address for the Extra
Segment.
Address Generation Circuit:
● The BIU has a Physical Address Generation Circuit.
●   It generates the 20-bit physical address using Segment and Offset addresses
using the formula:
●   In Bus Interface Unit (BIU) the circuit shown by the Σ symbol is responsible for
the calculation unit which is used to calculate the physical address of an
instruction in memory.
Pre-fetch Queue:
●   It is a 6-byte queue (FIFO).
● Fetching the next instruction (by BIU from CS) while executing the current
instruction is called pipelining.
● Gets flushed whenever a branch instruction occurs.
● The pre-Fetch queue is of 6-Bytes only because the maximum size of instruction
that can have in 8086 is 6 bytes. Hence to cover up all operands and data fields
of maximum size instruction in 8086 Microprocessor there is a Pre-Fetch queue
is 6 Bytes.
2. The Execution Unit (EU):
The main components of the EU are General purpose registers, the ALU, Special purpose
registers, the Instruction Register and Instruction Decoder, and the Flag/Status Register.
Fetches instructions from the Queue in BIU, decodes, and executes arithmetic and logic
operations using the ALU. Sends control signals for internal data transfer operations
within the microprocessor (Control Unit). Sends request signals to the BIU to access the
external module.
8086 has four 16-bit general purpose registers AX, BX, CX, and DX which store
intermediate values during execution. Each of these has two 8-bit parts (higher and
lower).
********** 12 **********
--- page 13 ---
Special purpose registers (16-bit): Special purpose registers are called Offset registers
also. Which points to specific memory locations under each segment.
● Stack Pointer: Points to Stack top.
● Base Pointer: BP can hold the offset addresses of any location in the stack
segment.
● Source Index: It holds an offset address in Data Segment during string
operations.
● Destination Index: It holds offset addresses in Extra Segment during string
operations.
Instruction Register and Instruction Decoder: The EU fetches an opcode from the
queue into the instruction register. The instruction decoder decodes it and sends the
information to the control circuit for execution.
Flag/Status register (16 bits): It has 9 flags that help change or recognize the state of
the microprocessor.
Control unit : The Control Unit in the 8086 microprocessor is a component that
manages the overall operation of the microprocessor. The control unit is responsible for
controlling the flow of instructions through the microprocessor and coordinating the
activities of the other components, including the Decode Unit, Execution Unit, and
Prefetch Unit.
CO4, b Differentiate between Memory-Mapped I/O and I/O-Mapped I/O. Explain their   10
BT2   working principal.
Ans: difference 6 marks
Working 4 makrs
1. Memory-Mapped I/O – Working Principle
In Memory-Mapped I/O, I/O devices are treated as part of the main memory. Each
I/O device is assigned a unique memory address within the normal memory address
space.
Working:
• The CPU generates a memory address on the address bus.
• This address may refer to either:
o A memory location, or
o An I/O device register
• The control unit does not differentiate between memory and I/O initially.
********** 13 **********
--- page 14 ---
• The address decoder identifies whether the address belongs to RAM or an
I/O device.
•   If it is an I/O address:
o The corresponding device responds just like memory would.
• CPU uses normal instructions like:
o LOAD, STORE, MOV
2. I/O-Mapped I/O (Isolated I/O) – Working Principle
In I/O-Mapped I/O, I/O devices have a separate address space distinct from
memory.
Working:
• The CPU uses special I/O instructions like IN and OUT (8086
architecture).
• When an I/O instruction is executed:
o The CPU places the I/O port address on the address bus.
o   It activates I/O control signals (IOR or IOW).
• The memory system ignores this operation because memory and I/O are
separated.
• Only the selected I/O device responds to the I/O control signal.
• Data is transferred between CPU and I/O device via accumulator/registers.
Q7   a Explain the organization and operation of an I/O Processor with a suitable diagram.   10
CO4,   Ans:
BT2
2 marks what is IOP
2 marks diagram
6 marks explanation
Input / Output Processor [2 marks]
•An input-output processor (IOP) is a processor with direct memory access
capability.
•In this, the computer system is divided into a memory unit and number of
processors.
•Each IOP controls and manage the input-output tasks.
•The IOP is similar to CPU except that it handles only the details of I/O processing.
•The IOP can fetch and execute its own instructions.
•These IOP instructions are designed to manage I/O transfers only.
BelowisablockdiagramofacomputeralongwithvariousI/OProcessors.
•Thememoryunitoccupiesthecentralpositionandcancommunicatewitheachprocessor
.
•TheCPUprocessesthedatarequiredforsolvingthecomputationaltasks.
•TheIOPprovidesapathfortransferofdatabetweenperipheralsandmemory.
********** 14 **********
--- page 15 ---
•TheCPUassignsthetaskofinitiatingtheI/Oprogram.
•TheIOPoperatesindependentfromCPUandtransferdatabetweenperipheralsandmem
ory.
The communication between the IOP and the devices is similar to the program
control method of transfer.
•And the communication with the memory is similar to the direct memory access
method.
•In large scale computers, each processor is independent of other processors and
any processor can initiate the operation.
•The CPU can act as master and the IOP act as slave processor.
•The CPU assigns the task of initiating operations but it is the IOP, who executes
the instructions, and not the CPU.
•CPU instructions provide operations to start an I/O transfer.
•The IOP asks for CPU through interrupt.
•Instructions that are read from memory by an IOP are also called commands to
distinguish them from instructions that are read by CPU.
•Commands are prepared by programmers and are stored in memory.
•Command words make the program for IOP.
•CPU informs the IOP where to find the commands in memory.
CO1, b   i.   Identify the different methods of specifying operands in an instruction.   5
BT3   Illustrate any 2 methods with an example.
Ans:
Enlist the method 1 marks
Explaination of each method 2 marks   5
The different methods used to specify operands in an instruction are called Addressing
Modes.
Common methods (Addressing Modes):
1. Immediate Addressing Mode
2. Direct Addressing Mode
3. Indirect Addressing Mode
4. Register Addressing Mode
5. Register Indirect Addressing Mode
********** 15 **********
--- page 16 ---
6. Indexed Addressing Mode
7. Base (Displacement) Addressing Mode
8. Relative Addressing Mode
Immediate Addressing Mode
In this mode, the operand (data) is specified directly in the instruction itself.
Working Principle:
• The CPU does not need to access memory for the operand.
• The value is immediately available in the instruction.
Example:
MOV AL, 05H
Direct Addressing Mode
In this mode, the address of the operand is directly given in the instruction.
Working Principle:
• The instruction contains the memory address.
• CPU goes to that memory location to fetch the operand.
Example:
MOV AL, [2000H]
CO1,   ii.   Distinguish between computer organization and architecture.
BT2
Each difference 1 marks
********** 16 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 1189e7c5869a

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_IT_7001/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B.
Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 04 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. Assume Suitable data if necessary
Q.no   Questions   Mark
.   s
Q1
CO1, a Analyze the functional view of a computer and explain how different operations   5
BT2   (input, processing, output, storage) are coordinated during program execution.
Ans: 1 marks for each
There are four main functions of a computer:
• Data processing : Data may take a wide variety of forms and the range of
processing requirements is broad
• Data storage :
✓ Short-term
✓ Long-term
• Data movement:
✓ Input-output (I/O) - when data are received from or delivered to a
device (peripheral) that is directly connected to the computer
✓ Data communications – when data are moved over longer distances, to
or from a remote device
• Control
A control unit manages the computer’s resources and coordinates the
performance of its functional parts in response to instructions
During execution: 1 marks
• Control unit fetches instructions
• Decodes them
• Executes using ALU
•   Stores results in memory or sends to output
CO3, b What are the different types of registers in a CPU?   5
BT2   Ans:
1.25m for each type
********** 1 **********
--- page 2 ---
1. Accumulator : used to hold an operand and result of an ALU operation
2. General Purpose registers to hold data
3. Segment / Index / pointer registers to hold memory address
4. Status / Flag registers to indicate status of ALU operation ( Sign, Zero, Carry,
parity etc.)
CO4, c Define following:   5
BT2   a. Micro-operation
b. Micro-instruction
c. Micro-program
d. Micro-code
e. Control word
Ans:
Each 1 marks
Ans.
a. Micro-operation
A micro-operation is a basic operation performed on data stored in registers
within the CPU.
b. Micro-instruction
A micro-instruction is a binary control instruction that specifies one or more
micro-operations to be executed at a given time.
c. Micro-program
A micro-program is a sequence of micro-instructions stored in control memory
that implements a machine-level instruction.
d. Micro-code
Micro-code refers to the set of micro-instructions used to implement the
instruction set of a processor.
e. Control Word
A control word is a binary pattern of control signals that specifies the operations to be
performed in a single clock cycle.
CO4, d Explain superscalar architecture and its working principle.   5
BT4
Marks Bifurcation
Definition: 2 Marks
Working Principle: 3 Marks
Answer-
Superscalar architecture is a processor design that allows execution of multiple
instructions in a single clock cycle.
It works by using multiple pipelines and execution units. The processor fetches,
decodes, and dispatches multiple instructions simultaneously. Techniques like
instruction-level parallelism and out-of-order execution help improve
performance.
********** 2 **********
--- page 3 ---
This results in higher throughput and better CPU utilization.
Q2   a Describe, what is system bus arbitration? Explain the method of centralized bus   10
CO1,   arbitration in brief with diagram.
BT2
Ans: [1 marks defination]
bus arbitration : is who can use the Bus a specific time or More than one
module controlling the bus
• Bus Arbitration refers to the process by which the current bus master
accesses and then leaves the control of the bus and passes it to the another
bus requesting processor unit
• The controller that has access to a bus at an instance is known as Bus master
Method of centralized bus arbitration: 3 marks for each
(i)   Daisy Chaining method –
✓ It is a centralized bus arbitration method.
✓ It is a simple and cheaper method where all the bus masters use the same
line for making bus requests.
✓ The bus grant signal serially propagates through each master until it
encounters the first one that is requesting access to the bus.
✓ This master blocks the propagation of the bus grant signal, therefore any
other requesting module will not receive the grant signal and hence cannot
access the bus.
During any bus cycle, the bus master may be any device – the processor or any
DMA controller unit, connected to the bus.
ii)Polling or Rotating Priority method
✓ In this, the controller is used to generate the address for the master(unique
priority), the number of address lines required depends on the number of
masters connected in the system.
✓ the priorities are dynamically changed to give every device an opportunity
to access the bus.
✓ The controller generates a sequence of master addresses.
✓ When the requesting master recognizes its address, it activates the busy line
and begins to use the bus.
********** 3 **********
--- page 4 ---
(iii) Fixed priority or Independent Request method
✓ In this, each master has a separate pair of bus request and bus grant lines
and each pair has a priority assigned to it.
The built-in priority decoder within the controller selects the highest priority
request   and   asserts   the   corresponding   bus   grant   signal.
CO2, b Consider a computer system with the following cache specifications:   10
BT3   • Cache size = 256 KB
• Block size = 64 bytes
• Mapping technique = Direct mapping
• Main memory size = 4 MB
Assume that the system uses byte-addressable memory. Divide the main memory
address into Tag, Index, and Block Offset fields, clearly specifying the number of
bits in each.
Ans:
2.5 marks for each Step:
********** 4 **********
--- page 5 ---
Final division of the 22-bit main memory address:
Field   Number of Bits
Tag   4 bits
Index   12 bits
Block Offset 6 bits
Q3   a Explain hardware interrupts and software interrupts in detail. Compare the   10
CO1,   interrupt-driven I/O method with the polling method and justify why interrupts are
BT2   more efficient.
Ans:
1. Hardware Interrupts 2 marks
Definition:
Hardware interrupts are signals sent to the CPU by external hardware devices to
indicate they need immediate attention.
• Triggered by external events (e.g., keyboard input, mouse click, I/O device
ready).
• Asynchronous to the CPU’s current operations.
Software Interrupts 2 marks
Definition:
Software interrupts are generated by programs or the CPU itself to request OS
services or handle exceptional conditions.
• Triggered by executing specific instructions (e.g., INT in x86 assembly).
• Synchronous with program execution.
• Used for system calls, debugging, or handling errors like divide-by-zero.
Comparison: 4 Marks
********** 5 **********
--- page 6 ---
Why Interrupts Are More Efficient : 2 marks
1. Eliminate   Wasteful   Waiting:
Interrupts free the CPU from continuous checking, allowing it to execute
other instructions until the device needs attention.
2. Better   CPU   Utilization:
CPU resources are used more effectively for useful work rather than polling.
CO2, b Compare the IEEE 754 single precision and double precision formats. Show the   10
BT3   representations side by side and state two practical scenarios where double
precision is preferred over single precision.
Ans: 8 marks for Difference
1. Bit-Level Representation (Side-by-Side)
Component   Single Precision (32-bit) Double Precision (64-bit)
Sign bit   1 bit   1 bit
Exponent   8 bits   11 bits
Mantissa (Fraction) 23 bits   52 bits
Total Size   32 bits   64 bits
2. Format Structure
Single Precision (32-bit)
| S | Exponent (8 bits) | Fraction (23 bits) |
Double Precision (64-bit)
| S | Exponent (11 bits) | Fraction (52 bits) |
3. Key Differences
Feature   Single Precision   Double Precision
Precision   ~6–7 decimal digits ~15–16 decimal digits
Range   Smaller   Much larger
Memory usage   4 bytes   8 bytes
Computational speed Faster   Slightly slower
********** 6 **********
--- page 7 ---
Rounding error   Higher   Lower
When Double Precision is Preferred (Any Two Scenarios) : 2 marks
1. Scientific and Engineering Calculations
Used in simulations such as:
• Weather forecasting
•   Fluid dynamics
•   Structural engineering analysis
Reason: These applications require high numerical accuracy and small rounding
errors can significantly affect results.
2. Financial and Statistical Computations
Used in:
• Risk analysis models
•   Large-scale financial forecasting
• Machine learning statistical computations
Q4   a Explain the concept of Content Addressable Memory (CAM). Describe its working   10
CO2,   principle with a neat diagram.
BT2   And:
Explain the concept of Content Addressable Memory (CAM) 2 marks
• A memory unit accessed by content of data rather than address is also known
as content addressable memory(CAM).
• The content is accessed parallel on the basis of data rather than specific
address or location
• A search can be done entire word or specific field within a word.
•   It is more expensive because each cell consist the storage capacity and logic
circuits for matching its content.
• Example: Neural network for pattern search, Google
working principle:
********** 7 **********
--- page 8 ---
diagram=3 marks
•   Searching word contained by argument register (A) with n-bits ,1-bit for
word
• A is matched with AM then it is placed in match register as 1 otherwise it is
denoted with 0.
• Content is searched based on portion then store in key register indicating
by 1 other bits represented by 0
• Complete word need to search the k will content all 1’s otherwise specific
position contains 1.
• Reading is performed in sequential; writing is performed in empty cells.
[Explanation 5 marks]
CO2, b Explain the design and working of a 4-bit parallel adder–subtractor with a neat   10
BT2   diagram. Illustrate how the circuit performs both addition and subtraction using
control logic. Also state the advantages and disadvantages of the parallel adder–
subtractor.
Ans:
[Diagram with explanation 6 marks ]
********** 8 **********
--- page 9 ---
• Advantages of parallel Adder/Subtractor [2 marks]
1. The parallel adder/subtractor performs the addition operation faster as
compared to serial adder/subtractor.
2. Time required for addition does not depend on the number of bits.
3. The output is in parallel form i.e all the bits are added/subtracted at the same
time.
4. It is less costly.
• Disadvantages of parallel Adder/Subtractor [2 marks]
1. Each adder has to wait for the carry to come from the previous adder in the
chain.
2. The propagation delay( delay associated with the travelling of carry bit) is
found to increase with the increase in the number of bits to be added.
Q5   a Explain the concept of the Translation Lookaside Buffer (TLB) and its working   10
CO2,   mechanism. Discuss why a TLB is required in modern computer systems. Illustrate
BT 2   your answer with a suitable diagram.
Ans:
(a)The Translation Lookaside Buffer (TLB) is a high-speed hardware
cache situated inside or near the Memory Management Unit (MMU). It
stores the most recently used mappings between Virtual Page Numbers
(VPNs) and Physical Frame Numbers (PFNs), reducing the need for
frequent page table lookups.
• Acts as a quick reference for recent virtual-to-physical address
translations.
•   Significantly speeds up memory access by minimizing main memory
lookups.
• Enhances overall CPU performance and efficiency in address translation.
********** 9 **********
--- page 10 ---
[diagram 4 Marks]
Reasons to use TLB : [explanation 6 marks]
When the CPU generates a virtual address, it must be translated into a physical
address to access data in main memory. The naive approach stores the entire page
table in main memory. Therefore, for every memory access, the following two
memory accesses are required:
1. Access the page table in main memory to get the frame number.
2. Access the actual data in the main memory frame.
3. This leads to a performance problem, as every memory access now
requires two memory accesses, causing a significant slowdown. 3M
CO2, b Apply Booth’s Algorithm to multiply 7 × 3 using 4-bit representation and show all   10
BT3   intermediate steps. Also, draw and explain the hardware structure of Booth’s
multiplier.
Ans: 5 marks for Solution
Step A B (Q) Q-1   Operation
INIT 0000 0011 0   Initial values
1   1001 0011 0 A ← A − M (10)
1   1100 1001 1   Arithmetic right shift
2   1100 1001 1 No operation (11)
2   1110 0100 1   Arithmetic right shift
3   0101 0100 1 A ← A + M (01)
3   0010 1010 0   Arithmetic right shift
4   0010 1010 0 No operation (00)
4   0001 0101 0   Arithmetic right shift
********** 10 **********
--- page 11 ---
2 marks= diagram
• The Booth's algorithm can be implemented as shown in the Fig. 2.19.
• The circuit is similar to circuit for positive number multiplication.
•   It consists of n-bit adder, shift, add subtract control logic and four registers,
A, B, Q and Q -1.
• As shown in the Fig. 2.19 multiplier and multiplicand are loaded into
register Q and register B, respectively, and register A and (2-1 are initially
set to 0.
3 marks explanation
Q6   a Explain the architecture of the 8086 microprocessors with a neat and labeled   10
CO3,   diagram. Describe the functions of its major components in detail.
BT2
Diagram of architecture: 4m
Explanation of Execution unit: 3m
Explanation of Bus Interface unit: 3m
The internal architecture of Intel 8086 is divided into 2 units: The Bus Interface Unit
(BIU), and The Execution Unit (EU).
********** 11 **********
--- page 12 ---
1. The Bus Interface Unit (BIU):It provides the interface of 8086 to external memory and
I/O devices via the System Bus. It performs various machine cycles such as memory read,
I/O   read,   etc.   to   transfer   data between memory and   I/O   devices.
BIU performs the following functions are as follows:
●   It generates the 20-bit physical address for memory access.
●   It fetches instructions from the memory.
●   It transfers data to and from the memory and I/O.
● Supports pipelining
BIU mainly contains the 4 Segment registers, the Instruction Pointer, a pre-fetch queue,
and an Address Generation Circuit.
Instruction Pointer (IP):
●   It is a 16-bit register. It holds offset of the next instructions in the Code
Segment.
●   IP is incremented after every instruction byte is fetched.
Code Segment register: (16 Bit register): CS holds the base address for the Code
Segment. All programs are stored in the Code Segment and accessed via the IP.
Data Segment register: (16 Bit register): DS holds the base address for the Data
Segment.
Stack Segment register: (16 Bit register): SS holds the base address for the Stack
Segment.
Extra Segment register: (16 Bit register): ES holds the base address for the Extra
Segment.
Address Generation Circuit:
● The BIU has a Physical Address Generation Circuit.
●   It generates the 20-bit physical address using Segment and Offset addresses
using the formula:
●   In Bus Interface Unit (BIU) the circuit shown by the Σ symbol is responsible for
the calculation unit which is used to calculate the physical address of an
instruction in memory.
Pre-fetch Queue:
●   It is a 6-byte queue (FIFO).
● Fetching the next instruction (by BIU from CS) while executing the current
instruction is called pipelining.
● Gets flushed whenever a branch instruction occurs.
● The pre-Fetch queue is of 6-Bytes only because the maximum size of instruction
that can have in 8086 is 6 bytes. Hence to cover up all operands and data fields
of maximum size instruction in 8086 Microprocessor there is a Pre-Fetch queue
is 6 Bytes.
2. The Execution Unit (EU):
The main components of the EU are General purpose registers, the ALU, Special purpose
registers, the Instruction Register and Instruction Decoder, and the Flag/Status Register.
Fetches instructions from the Queue in BIU, decodes, and executes arithmetic and logic
operations using the ALU. Sends control signals for internal data transfer operations
within the microprocessor (Control Unit). Sends request signals to the BIU to access the
external module.
8086 has four 16-bit general purpose registers AX, BX, CX, and DX which store
intermediate values during execution. Each of these has two 8-bit parts (higher and
lower).
********** 12 **********
--- page 13 ---
Special purpose registers (16-bit): Special purpose registers are called Offset registers
also. Which points to specific memory locations under each segment.
● Stack Pointer: Points to Stack top.
● Base Pointer: BP can hold the offset addresses of any location in the stack
segment.
● Source Index: It holds an offset address in Data Segment during string
operations.
● Destination Index: It holds offset addresses in Extra Segment during string
operations.
Instruction Register and Instruction Decoder: The EU fetches an opcode from the
queue into the instruction register. The instruction decoder decodes it and sends the
information to the control circuit for execution.
Flag/Status register (16 bits): It has 9 flags that help change or recognize the state of
the microprocessor.
Control unit : The Control Unit in the 8086 microprocessor is a component that
manages the overall operation of the microprocessor. The control unit is responsible for
controlling the flow of instructions through the microprocessor and coordinating the
activities of the other components, including the Decode Unit, Execution Unit, and
Prefetch Unit.
CO4, b Differentiate between Memory-Mapped I/O and I/O-Mapped I/O. Explain their   10
BT2   working principal.
Ans: difference 6 marks
Working 4 makrs
1. Memory-Mapped I/O – Working Principle
In Memory-Mapped I/O, I/O devices are treated as part of the main memory. Each
I/O device is assigned a unique memory address within the normal memory address
space.
Working:
• The CPU generates a memory address on the address bus.
• This address may refer to either:
o A memory location, or
o An I/O device register
• The control unit does not differentiate between memory and I/O initially.
********** 13 **********
--- page 14 ---
• The address decoder identifies whether the address belongs to RAM or an
I/O device.
•   If it is an I/O address:
o The corresponding device responds just like memory would.
• CPU uses normal instructions like:
o LOAD, STORE, MOV
2. I/O-Mapped I/O (Isolated I/O) – Working Principle
In I/O-Mapped I/O, I/O devices have a separate address space distinct from
memory.
Working:
• The CPU uses special I/O instructions like IN and OUT (8086
architecture).
• When an I/O instruction is executed:
o The CPU places the I/O port address on the address bus.
o   It activates I/O control signals (IOR or IOW).
• The memory system ignores this operation because memory and I/O are
separated.
• Only the selected I/O device responds to the I/O control signal.
• Data is transferred between CPU and I/O device via accumulator/registers.
Q7   a Explain the organization and operation of an I/O Processor with a suitable diagram.   10
CO4,   Ans:
BT2
2 marks what is IOP
2 marks diagram
6 marks explanation
Input / Output Processor [2 marks]
•An input-output processor (IOP) is a processor with direct memory access
capability.
•In this, the computer system is divided into a memory unit and number of
processors.
•Each IOP controls and manage the input-output tasks.
•The IOP is similar to CPU except that it handles only the details of I/O processing.
•The IOP can fetch and execute its own instructions.
•These IOP instructions are designed to manage I/O transfers only.
BelowisablockdiagramofacomputeralongwithvariousI/OProcessors.
•Thememoryunitoccupiesthecentralpositionandcancommunicatewitheachprocessor
.
•TheCPUprocessesthedatarequiredforsolvingthecomputationaltasks.
•TheIOPprovidesapathfortransferofdatabetweenperipheralsandmemory.
********** 14 **********
--- page 15 ---
•TheCPUassignsthetaskofinitiatingtheI/Oprogram.
•TheIOPoperatesindependentfromCPUandtransferdatabetweenperipheralsandmem
ory.
The communication between the IOP and the devices is similar to the program
control method of transfer.
•And the communication with the memory is similar to the direct memory access
method.
•In large scale computers, each processor is independent of other processors and
any processor can initiate the operation.
•The CPU can act as master and the IOP act as slave processor.
•The CPU assigns the task of initiating operations but it is the IOP, who executes
the instructions, and not the CPU.
•CPU instructions provide operations to start an I/O transfer.
•The IOP asks for CPU through interrupt.
•Instructions that are read from memory by an IOP are also called commands to
distinguish them from instructions that are read by CPU.
•Commands are prepared by programmers and are stored in memory.
•Command words make the program for IOP.
•CPU informs the IOP where to find the commands in memory.
CO1, b   i.   Identify the different methods of specifying operands in an instruction.   5
BT3   Illustrate any 2 methods with an example.
Ans:
Enlist the method 1 marks
Explaination of each method 2 marks   5
The different methods used to specify operands in an instruction are called Addressing
Modes.
Common methods (Addressing Modes):
1. Immediate Addressing Mode
2. Direct Addressing Mode
3. Indirect Addressing Mode
4. Register Addressing Mode
5. Register Indirect Addressing Mode
********** 15 **********
--- page 16 ---
6. Indexed Addressing Mode
7. Base (Displacement) Addressing Mode
8. Relative Addressing Mode
Immediate Addressing Mode
In this mode, the operand (data) is specified directly in the instruction itself.
Working Principle:
• The CPU does not need to access memory for the operand.
• The value is immediately available in the instruction.
Example:
MOV AL, 05H
Direct Addressing Mode
In this mode, the address of the operand is directly given in the instruction.
Working Principle:
• The instruction contains the memory address.
• CPU goes to that memory location to fetch the operand.
Example:
MOV AL, [2000H]
CO1,   ii.   Distinguish between computer organization and architecture.
BT2
Each difference 1 marks
********** 16 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper e312eb58b337

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_Computer_7047/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B.
Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 04 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. Assume Suitable data if necessary
Q.no   Questions   Mark
.   s
Q1
CO1, a Analyze the functional view of a computer and explain how different operations   5
BT2   (input, processing, output, storage) are coordinated during program execution.
Ans: 1 marks for each
There are four main functions of a computer:
• Data processing : Data may take a wide variety of forms and the range of
processing requirements is broad
• Data storage :
✓ Short-term
✓ Long-term
• Data movement:
✓ Input-output (I/O) - when data are received from or delivered to a
device (peripheral) that is directly connected to the computer
✓ Data communications – when data are moved over longer distances, to
or from a remote device
• Control
A control unit manages the computer’s resources and coordinates the
performance of its functional parts in response to instructions
During execution: 1 marks
• Control unit fetches instructions
• Decodes them
• Executes using ALU
•   Stores results in memory or sends to output
CO3, b What are the different types of registers in a CPU?   5
BT2   Ans:
1.25m for each type
********** 1 **********
--- page 2 ---
1. Accumulator : used to hold an operand and result of an ALU operation
2. General Purpose registers to hold data
3. Segment / Index / pointer registers to hold memory address
4. Status / Flag registers to indicate status of ALU operation ( Sign, Zero, Carry,
parity etc.)
CO4, c Define following:   5
BT2   a. Micro-operation
b. Micro-instruction
c. Micro-program
d. Micro-code
e. Control word
Ans:
Each 1 marks
Ans.
a. Micro-operation
A micro-operation is a basic operation performed on data stored in registers
within the CPU.
b. Micro-instruction
A micro-instruction is a binary control instruction that specifies one or more
micro-operations to be executed at a given time.
c. Micro-program
A micro-program is a sequence of micro-instructions stored in control memory
that implements a machine-level instruction.
d. Micro-code
Micro-code refers to the set of micro-instructions used to implement the
instruction set of a processor.
e. Control Word
A control word is a binary pattern of control signals that specifies the operations to be
performed in a single clock cycle.
CO4, d Explain superscalar architecture and its working principle.   5
BT4
Marks Bifurcation
Definition: 2 Marks
Working Principle: 3 Marks
Answer-
Superscalar architecture is a processor design that allows execution of multiple
instructions in a single clock cycle.
It works by using multiple pipelines and execution units. The processor fetches,
decodes, and dispatches multiple instructions simultaneously. Techniques like
instruction-level parallelism and out-of-order execution help improve
performance.
********** 2 **********
--- page 3 ---
This results in higher throughput and better CPU utilization.
Q2   a Describe, what is system bus arbitration? Explain the method of centralized bus   10
CO1,   arbitration in brief with diagram.
BT2
Ans: [1 marks defination]
bus arbitration : is who can use the Bus a specific time or More than one
module controlling the bus
• Bus Arbitration refers to the process by which the current bus master
accesses and then leaves the control of the bus and passes it to the another
bus requesting processor unit
• The controller that has access to a bus at an instance is known as Bus master
Method of centralized bus arbitration: 3 marks for each
(i)   Daisy Chaining method –
✓ It is a centralized bus arbitration method.
✓ It is a simple and cheaper method where all the bus masters use the same
line for making bus requests.
✓ The bus grant signal serially propagates through each master until it
encounters the first one that is requesting access to the bus.
✓ This master blocks the propagation of the bus grant signal, therefore any
other requesting module will not receive the grant signal and hence cannot
access the bus.
During any bus cycle, the bus master may be any device – the processor or any
DMA controller unit, connected to the bus.
ii)Polling or Rotating Priority method
✓ In this, the controller is used to generate the address for the master(unique
priority), the number of address lines required depends on the number of
masters connected in the system.
✓ the priorities are dynamically changed to give every device an opportunity
to access the bus.
✓ The controller generates a sequence of master addresses.
✓ When the requesting master recognizes its address, it activates the busy line
and begins to use the bus.
********** 3 **********
--- page 4 ---
(iii) Fixed priority or Independent Request method
✓ In this, each master has a separate pair of bus request and bus grant lines
and each pair has a priority assigned to it.
The built-in priority decoder within the controller selects the highest priority
request   and   asserts   the   corresponding   bus   grant   signal.
CO2, b Consider a computer system with the following cache specifications:   10
BT3   • Cache size = 256 KB
• Block size = 64 bytes
• Mapping technique = Direct mapping
• Main memory size = 4 MB
Assume that the system uses byte-addressable memory. Divide the main memory
address into Tag, Index, and Block Offset fields, clearly specifying the number of
bits in each.
Ans:
2.5 marks for each Step:
********** 4 **********
--- page 5 ---
Final division of the 22-bit main memory address:
Field   Number of Bits
Tag   4 bits
Index   12 bits
Block Offset 6 bits
Q3   a Explain hardware interrupts and software interrupts in detail. Compare the   10
CO1,   interrupt-driven I/O method with the polling method and justify why interrupts are
BT2   more efficient.
Ans:
1. Hardware Interrupts 2 marks
Definition:
Hardware interrupts are signals sent to the CPU by external hardware devices to
indicate they need immediate attention.
• Triggered by external events (e.g., keyboard input, mouse click, I/O device
ready).
• Asynchronous to the CPU’s current operations.
Software Interrupts 2 marks
Definition:
Software interrupts are generated by programs or the CPU itself to request OS
services or handle exceptional conditions.
• Triggered by executing specific instructions (e.g., INT in x86 assembly).
• Synchronous with program execution.
• Used for system calls, debugging, or handling errors like divide-by-zero.
Comparison: 4 Marks
********** 5 **********
--- page 6 ---
Why Interrupts Are More Efficient : 2 marks
1. Eliminate   Wasteful   Waiting:
Interrupts free the CPU from continuous checking, allowing it to execute
other instructions until the device needs attention.
2. Better   CPU   Utilization:
CPU resources are used more effectively for useful work rather than polling.
CO2, b Compare the IEEE 754 single precision and double precision formats. Show the   10
BT3   representations side by side and state two practical scenarios where double
precision is preferred over single precision.
Ans: 8 marks for Difference
1. Bit-Level Representation (Side-by-Side)
Component   Single Precision (32-bit) Double Precision (64-bit)
Sign bit   1 bit   1 bit
Exponent   8 bits   11 bits
Mantissa (Fraction) 23 bits   52 bits
Total Size   32 bits   64 bits
2. Format Structure
Single Precision (32-bit)
| S | Exponent (8 bits) | Fraction (23 bits) |
Double Precision (64-bit)
| S | Exponent (11 bits) | Fraction (52 bits) |
3. Key Differences
Feature   Single Precision   Double Precision
Precision   ~6–7 decimal digits ~15–16 decimal digits
Range   Smaller   Much larger
Memory usage   4 bytes   8 bytes
Computational speed Faster   Slightly slower
********** 6 **********
--- page 7 ---
Rounding error   Higher   Lower
When Double Precision is Preferred (Any Two Scenarios) : 2 marks
1. Scientific and Engineering Calculations
Used in simulations such as:
• Weather forecasting
•   Fluid dynamics
•   Structural engineering analysis
Reason: These applications require high numerical accuracy and small rounding
errors can significantly affect results.
2. Financial and Statistical Computations
Used in:
• Risk analysis models
•   Large-scale financial forecasting
• Machine learning statistical computations
Q4   a Explain the concept of Content Addressable Memory (CAM). Describe its working   10
CO2,   principle with a neat diagram.
BT2   And:
Explain the concept of Content Addressable Memory (CAM) 2 marks
• A memory unit accessed by content of data rather than address is also known
as content addressable memory(CAM).
• The content is accessed parallel on the basis of data rather than specific
address or location
• A search can be done entire word or specific field within a word.
•   It is more expensive because each cell consist the storage capacity and logic
circuits for matching its content.
• Example: Neural network for pattern search, Google
working principle:
********** 7 **********
--- page 8 ---
diagram=3 marks
•   Searching word contained by argument register (A) with n-bits ,1-bit for
word
• A is matched with AM then it is placed in match register as 1 otherwise it is
denoted with 0.
• Content is searched based on portion then store in key register indicating
by 1 other bits represented by 0
• Complete word need to search the k will content all 1’s otherwise specific
position contains 1.
• Reading is performed in sequential; writing is performed in empty cells.
[Explanation 5 marks]
CO2, b Explain the design and working of a 4-bit parallel adder–subtractor with a neat   10
BT2   diagram. Illustrate how the circuit performs both addition and subtraction using
control logic. Also state the advantages and disadvantages of the parallel adder–
subtractor.
Ans:
[Diagram with explanation 6 marks ]
********** 8 **********
--- page 9 ---
• Advantages of parallel Adder/Subtractor [2 marks]
1. The parallel adder/subtractor performs the addition operation faster as
compared to serial adder/subtractor.
2. Time required for addition does not depend on the number of bits.
3. The output is in parallel form i.e all the bits are added/subtracted at the same
time.
4. It is less costly.
• Disadvantages of parallel Adder/Subtractor [2 marks]
1. Each adder has to wait for the carry to come from the previous adder in the
chain.
2. The propagation delay( delay associated with the travelling of carry bit) is
found to increase with the increase in the number of bits to be added.
Q5   a Explain the concept of the Translation Lookaside Buffer (TLB) and its working   10
CO2,   mechanism. Discuss why a TLB is required in modern computer systems. Illustrate
BT 2   your answer with a suitable diagram.
Ans:
(a)The Translation Lookaside Buffer (TLB) is a high-speed hardware
cache situated inside or near the Memory Management Unit (MMU). It
stores the most recently used mappings between Virtual Page Numbers
(VPNs) and Physical Frame Numbers (PFNs), reducing the need for
frequent page table lookups.
• Acts as a quick reference for recent virtual-to-physical address
translations.
•   Significantly speeds up memory access by minimizing main memory
lookups.
• Enhances overall CPU performance and efficiency in address translation.
********** 9 **********
--- page 10 ---
[diagram 4 Marks]
Reasons to use TLB : [explanation 6 marks]
When the CPU generates a virtual address, it must be translated into a physical
address to access data in main memory. The naive approach stores the entire page
table in main memory. Therefore, for every memory access, the following two
memory accesses are required:
1. Access the page table in main memory to get the frame number.
2. Access the actual data in the main memory frame.
3. This leads to a performance problem, as every memory access now
requires two memory accesses, causing a significant slowdown. 3M
CO2, b Apply Booth’s Algorithm to multiply 7 × 3 using 4-bit representation and show all   10
BT3   intermediate steps. Also, draw and explain the hardware structure of Booth’s
multiplier.
Ans: 5 marks for Solution
Step A B (Q) Q-1   Operation
INIT 0000 0011 0   Initial values
1   1001 0011 0 A ← A − M (10)
1   1100 1001 1   Arithmetic right shift
2   1100 1001 1 No operation (11)
2   1110 0100 1   Arithmetic right shift
3   0101 0100 1 A ← A + M (01)
3   0010 1010 0   Arithmetic right shift
4   0010 1010 0 No operation (00)
4   0001 0101 0   Arithmetic right shift
********** 10 **********
--- page 11 ---
2 marks= diagram
• The Booth's algorithm can be implemented as shown in the Fig. 2.19.
• The circuit is similar to circuit for positive number multiplication.
•   It consists of n-bit adder, shift, add subtract control logic and four registers,
A, B, Q and Q -1.
• As shown in the Fig. 2.19 multiplier and multiplicand are loaded into
register Q and register B, respectively, and register A and (2-1 are initially
set to 0.
3 marks explanation
Q6   a Explain the architecture of the 8086 microprocessors with a neat and labeled   10
CO3,   diagram. Describe the functions of its major components in detail.
BT2
Diagram of architecture: 4m
Explanation of Execution unit: 3m
Explanation of Bus Interface unit: 3m
The internal architecture of Intel 8086 is divided into 2 units: The Bus Interface Unit
(BIU), and The Execution Unit (EU).
********** 11 **********
--- page 12 ---
1. The Bus Interface Unit (BIU):It provides the interface of 8086 to external memory and
I/O devices via the System Bus. It performs various machine cycles such as memory read,
I/O   read,   etc.   to   transfer   data between memory and   I/O   devices.
BIU performs the following functions are as follows:
●   It generates the 20-bit physical address for memory access.
●   It fetches instructions from the memory.
●   It transfers data to and from the memory and I/O.
● Supports pipelining
BIU mainly contains the 4 Segment registers, the Instruction Pointer, a pre-fetch queue,
and an Address Generation Circuit.
Instruction Pointer (IP):
●   It is a 16-bit register. It holds offset of the next instructions in the Code
Segment.
●   IP is incremented after every instruction byte is fetched.
Code Segment register: (16 Bit register): CS holds the base address for the Code
Segment. All programs are stored in the Code Segment and accessed via the IP.
Data Segment register: (16 Bit register): DS holds the base address for the Data
Segment.
Stack Segment register: (16 Bit register): SS holds the base address for the Stack
Segment.
Extra Segment register: (16 Bit register): ES holds the base address for the Extra
Segment.
Address Generation Circuit:
● The BIU has a Physical Address Generation Circuit.
●   It generates the 20-bit physical address using Segment and Offset addresses
using the formula:
●   In Bus Interface Unit (BIU) the circuit shown by the Σ symbol is responsible for
the calculation unit which is used to calculate the physical address of an
instruction in memory.
Pre-fetch Queue:
●   It is a 6-byte queue (FIFO).
● Fetching the next instruction (by BIU from CS) while executing the current
instruction is called pipelining.
● Gets flushed whenever a branch instruction occurs.
● The pre-Fetch queue is of 6-Bytes only because the maximum size of instruction
that can have in 8086 is 6 bytes. Hence to cover up all operands and data fields
of maximum size instruction in 8086 Microprocessor there is a Pre-Fetch queue
is 6 Bytes.
2. The Execution Unit (EU):
The main components of the EU are General purpose registers, the ALU, Special purpose
registers, the Instruction Register and Instruction Decoder, and the Flag/Status Register.
Fetches instructions from the Queue in BIU, decodes, and executes arithmetic and logic
operations using the ALU. Sends control signals for internal data transfer operations
within the microprocessor (Control Unit). Sends request signals to the BIU to access the
external module.
8086 has four 16-bit general purpose registers AX, BX, CX, and DX which store
intermediate values during execution. Each of these has two 8-bit parts (higher and
lower).
********** 12 **********
--- page 13 ---
Special purpose registers (16-bit): Special purpose registers are called Offset registers
also. Which points to specific memory locations under each segment.
● Stack Pointer: Points to Stack top.
● Base Pointer: BP can hold the offset addresses of any location in the stack
segment.
● Source Index: It holds an offset address in Data Segment during string
operations.
● Destination Index: It holds offset addresses in Extra Segment during string
operations.
Instruction Register and Instruction Decoder: The EU fetches an opcode from the
queue into the instruction register. The instruction decoder decodes it and sends the
information to the control circuit for execution.
Flag/Status register (16 bits): It has 9 flags that help change or recognize the state of
the microprocessor.
Control unit : The Control Unit in the 8086 microprocessor is a component that
manages the overall operation of the microprocessor. The control unit is responsible for
controlling the flow of instructions through the microprocessor and coordinating the
activities of the other components, including the Decode Unit, Execution Unit, and
Prefetch Unit.
CO4, b Differentiate between Memory-Mapped I/O and I/O-Mapped I/O. Explain their   10
BT2   working principal.
Ans: difference 6 marks
Working 4 makrs
1. Memory-Mapped I/O – Working Principle
In Memory-Mapped I/O, I/O devices are treated as part of the main memory. Each
I/O device is assigned a unique memory address within the normal memory address
space.
Working:
• The CPU generates a memory address on the address bus.
• This address may refer to either:
o A memory location, or
o An I/O device register
• The control unit does not differentiate between memory and I/O initially.
********** 13 **********
--- page 14 ---
• The address decoder identifies whether the address belongs to RAM or an
I/O device.
•   If it is an I/O address:
o The corresponding device responds just like memory would.
• CPU uses normal instructions like:
o LOAD, STORE, MOV
2. I/O-Mapped I/O (Isolated I/O) – Working Principle
In I/O-Mapped I/O, I/O devices have a separate address space distinct from
memory.
Working:
• The CPU uses special I/O instructions like IN and OUT (8086
architecture).
• When an I/O instruction is executed:
o The CPU places the I/O port address on the address bus.
o   It activates I/O control signals (IOR or IOW).
• The memory system ignores this operation because memory and I/O are
separated.
• Only the selected I/O device responds to the I/O control signal.
• Data is transferred between CPU and I/O device via accumulator/registers.
Q7   a Explain the organization and operation of an I/O Processor with a suitable diagram.   10
CO4,   Ans:
BT2
2 marks what is IOP
2 marks diagram
6 marks explanation
Input / Output Processor [2 marks]
•An input-output processor (IOP) is a processor with direct memory access
capability.
•In this, the computer system is divided into a memory unit and number of
processors.
•Each IOP controls and manage the input-output tasks.
•The IOP is similar to CPU except that it handles only the details of I/O processing.
•The IOP can fetch and execute its own instructions.
•These IOP instructions are designed to manage I/O transfers only.
BelowisablockdiagramofacomputeralongwithvariousI/OProcessors.
•Thememoryunitoccupiesthecentralpositionandcancommunicatewitheachprocessor
.
•TheCPUprocessesthedatarequiredforsolvingthecomputationaltasks.
•TheIOPprovidesapathfortransferofdatabetweenperipheralsandmemory.
********** 14 **********
--- page 15 ---
•TheCPUassignsthetaskofinitiatingtheI/Oprogram.
•TheIOPoperatesindependentfromCPUandtransferdatabetweenperipheralsandmem
ory.
The communication between the IOP and the devices is similar to the program
control method of transfer.
•And the communication with the memory is similar to the direct memory access
method.
•In large scale computers, each processor is independent of other processors and
any processor can initiate the operation.
•The CPU can act as master and the IOP act as slave processor.
•The CPU assigns the task of initiating operations but it is the IOP, who executes
the instructions, and not the CPU.
•CPU instructions provide operations to start an I/O transfer.
•The IOP asks for CPU through interrupt.
•Instructions that are read from memory by an IOP are also called commands to
distinguish them from instructions that are read by CPU.
•Commands are prepared by programmers and are stored in memory.
•Command words make the program for IOP.
•CPU informs the IOP where to find the commands in memory.
CO1, b   i.   Identify the different methods of specifying operands in an instruction.   5
BT3   Illustrate any 2 methods with an example.
Ans:
Enlist the method 1 marks
Explaination of each method 2 marks   5
The different methods used to specify operands in an instruction are called Addressing
Modes.
Common methods (Addressing Modes):
1. Immediate Addressing Mode
2. Direct Addressing Mode
3. Indirect Addressing Mode
4. Register Addressing Mode
5. Register Indirect Addressing Mode
********** 15 **********
--- page 16 ---
6. Indexed Addressing Mode
7. Base (Displacement) Addressing Mode
8. Relative Addressing Mode
Immediate Addressing Mode
In this mode, the operand (data) is specified directly in the instruction itself.
Working Principle:
• The CPU does not need to access memory for the operand.
• The value is immediately available in the instruction.
Example:
MOV AL, 05H
Direct Addressing Mode
In this mode, the address of the operand is directly given in the instruction.
Working Principle:
• The instruction contains the memory address.
• CPU goes to that memory location to fetch the operand.
Example:
MOV AL, [2000H]
CO1,   ii.   Distinguish between computer organization and architecture.
BT2
Each difference 1 marks
********** 16 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 8bc25c896919

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_IT_7041/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B.
Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 04 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. Assume Suitable data if necessary
Q.no   Questions   Mark
.   s
Q1
CO1, a Analyze the functional view of a computer and explain how different operations   5
BT2   (input, processing, output, storage) are coordinated during program execution.
Ans: 1 marks for each
There are four main functions of a computer:
• Data processing : Data may take a wide variety of forms and the range of
processing requirements is broad
• Data storage :
✓ Short-term
✓ Long-term
• Data movement:
✓ Input-output (I/O) - when data are received from or delivered to a
device (peripheral) that is directly connected to the computer
✓ Data communications – when data are moved over longer distances, to
or from a remote device
• Control
A control unit manages the computer’s resources and coordinates the
performance of its functional parts in response to instructions
During execution: 1 marks
• Control unit fetches instructions
• Decodes them
• Executes using ALU
•   Stores results in memory or sends to output
CO3, b What are the different types of registers in a CPU?   5
BT2   Ans:
1.25m for each type
********** 1 **********
--- page 2 ---
1. Accumulator : used to hold an operand and result of an ALU operation
2. General Purpose registers to hold data
3. Segment / Index / pointer registers to hold memory address
4. Status / Flag registers to indicate status of ALU operation ( Sign, Zero, Carry,
parity etc.)
CO4, c Define following:   5
BT2   a. Micro-operation
b. Micro-instruction
c. Micro-program
d. Micro-code
e. Control word
Ans:
Each 1 marks
Ans.
a. Micro-operation
A micro-operation is a basic operation performed on data stored in registers
within the CPU.
b. Micro-instruction
A micro-instruction is a binary control instruction that specifies one or more
micro-operations to be executed at a given time.
c. Micro-program
A micro-program is a sequence of micro-instructions stored in control memory
that implements a machine-level instruction.
d. Micro-code
Micro-code refers to the set of micro-instructions used to implement the
instruction set of a processor.
e. Control Word
A control word is a binary pattern of control signals that specifies the operations to be
performed in a single clock cycle.
CO4, d Explain superscalar architecture and its working principle.   5
BT4
Marks Bifurcation
Definition: 2 Marks
Working Principle: 3 Marks
Answer-
Superscalar architecture is a processor design that allows execution of multiple
instructions in a single clock cycle.
It works by using multiple pipelines and execution units. The processor fetches,
decodes, and dispatches multiple instructions simultaneously. Techniques like
instruction-level parallelism and out-of-order execution help improve
performance.
********** 2 **********
--- page 3 ---
This results in higher throughput and better CPU utilization.
Q2   a Describe, what is system bus arbitration? Explain the method of centralized bus   10
CO1,   arbitration in brief with diagram.
BT2
Ans: [1 marks defination]
bus arbitration : is who can use the Bus a specific time or More than one
module controlling the bus
• Bus Arbitration refers to the process by which the current bus master
accesses and then leaves the control of the bus and passes it to the another
bus requesting processor unit
• The controller that has access to a bus at an instance is known as Bus master
Method of centralized bus arbitration: 3 marks for each
(i)   Daisy Chaining method –
✓ It is a centralized bus arbitration method.
✓ It is a simple and cheaper method where all the bus masters use the same
line for making bus requests.
✓ The bus grant signal serially propagates through each master until it
encounters the first one that is requesting access to the bus.
✓ This master blocks the propagation of the bus grant signal, therefore any
other requesting module will not receive the grant signal and hence cannot
access the bus.
During any bus cycle, the bus master may be any device – the processor or any
DMA controller unit, connected to the bus.
ii)Polling or Rotating Priority method
✓ In this, the controller is used to generate the address for the master(unique
priority), the number of address lines required depends on the number of
masters connected in the system.
✓ the priorities are dynamically changed to give every device an opportunity
to access the bus.
✓ The controller generates a sequence of master addresses.
✓ When the requesting master recognizes its address, it activates the busy line
and begins to use the bus.
********** 3 **********
--- page 4 ---
(iii) Fixed priority or Independent Request method
✓ In this, each master has a separate pair of bus request and bus grant lines
and each pair has a priority assigned to it.
The built-in priority decoder within the controller selects the highest priority
request   and   asserts   the   corresponding   bus   grant   signal.
CO2, b Consider a computer system with the following cache specifications:   10
BT3   • Cache size = 256 KB
• Block size = 64 bytes
• Mapping technique = Direct mapping
• Main memory size = 4 MB
Assume that the system uses byte-addressable memory. Divide the main memory
address into Tag, Index, and Block Offset fields, clearly specifying the number of
bits in each.
Ans:
2.5 marks for each Step:
********** 4 **********
--- page 5 ---
Final division of the 22-bit main memory address:
Field   Number of Bits
Tag   4 bits
Index   12 bits
Block Offset 6 bits
Q3   a Explain hardware interrupts and software interrupts in detail. Compare the   10
CO1,   interrupt-driven I/O method with the polling method and justify why interrupts are
BT2   more efficient.
Ans:
1. Hardware Interrupts 2 marks
Definition:
Hardware interrupts are signals sent to the CPU by external hardware devices to
indicate they need immediate attention.
• Triggered by external events (e.g., keyboard input, mouse click, I/O device
ready).
• Asynchronous to the CPU’s current operations.
Software Interrupts 2 marks
Definition:
Software interrupts are generated by programs or the CPU itself to request OS
services or handle exceptional conditions.
• Triggered by executing specific instructions (e.g., INT in x86 assembly).
• Synchronous with program execution.
• Used for system calls, debugging, or handling errors like divide-by-zero.
Comparison: 4 Marks
********** 5 **********
--- page 6 ---
Why Interrupts Are More Efficient : 2 marks
1. Eliminate   Wasteful   Waiting:
Interrupts free the CPU from continuous checking, allowing it to execute
other instructions until the device needs attention.
2. Better   CPU   Utilization:
CPU resources are used more effectively for useful work rather than polling.
CO2, b Compare the IEEE 754 single precision and double precision formats. Show the   10
BT3   representations side by side and state two practical scenarios where double
precision is preferred over single precision.
Ans: 8 marks for Difference
1. Bit-Level Representation (Side-by-Side)
Component   Single Precision (32-bit) Double Precision (64-bit)
Sign bit   1 bit   1 bit
Exponent   8 bits   11 bits
Mantissa (Fraction) 23 bits   52 bits
Total Size   32 bits   64 bits
2. Format Structure
Single Precision (32-bit)
| S | Exponent (8 bits) | Fraction (23 bits) |
Double Precision (64-bit)
| S | Exponent (11 bits) | Fraction (52 bits) |
3. Key Differences
Feature   Single Precision   Double Precision
Precision   ~6–7 decimal digits ~15–16 decimal digits
Range   Smaller   Much larger
Memory usage   4 bytes   8 bytes
Computational speed Faster   Slightly slower
********** 6 **********
--- page 7 ---
Rounding error   Higher   Lower
When Double Precision is Preferred (Any Two Scenarios) : 2 marks
1. Scientific and Engineering Calculations
Used in simulations such as:
• Weather forecasting
•   Fluid dynamics
•   Structural engineering analysis
Reason: These applications require high numerical accuracy and small rounding
errors can significantly affect results.
2. Financial and Statistical Computations
Used in:
• Risk analysis models
•   Large-scale financial forecasting
• Machine learning statistical computations
Q4   a Explain the concept of Content Addressable Memory (CAM). Describe its working   10
CO2,   principle with a neat diagram.
BT2   And:
Explain the concept of Content Addressable Memory (CAM) 2 marks
• A memory unit accessed by content of data rather than address is also known
as content addressable memory(CAM).
• The content is accessed parallel on the basis of data rather than specific
address or location
• A search can be done entire word or specific field within a word.
•   It is more expensive because each cell consist the storage capacity and logic
circuits for matching its content.
• Example: Neural network for pattern search, Google
working principle:
********** 7 **********
--- page 8 ---
diagram=3 marks
•   Searching word contained by argument register (A) with n-bits ,1-bit for
word
• A is matched with AM then it is placed in match register as 1 otherwise it is
denoted with 0.
• Content is searched based on portion then store in key register indicating
by 1 other bits represented by 0
• Complete word need to search the k will content all 1’s otherwise specific
position contains 1.
• Reading is performed in sequential; writing is performed in empty cells.
[Explanation 5 marks]
CO2, b Explain the design and working of a 4-bit parallel adder–subtractor with a neat   10
BT2   diagram. Illustrate how the circuit performs both addition and subtraction using
control logic. Also state the advantages and disadvantages of the parallel adder–
subtractor.
Ans:
[Diagram with explanation 6 marks ]
********** 8 **********
--- page 9 ---
• Advantages of parallel Adder/Subtractor [2 marks]
1. The parallel adder/subtractor performs the addition operation faster as
compared to serial adder/subtractor.
2. Time required for addition does not depend on the number of bits.
3. The output is in parallel form i.e all the bits are added/subtracted at the same
time.
4. It is less costly.
• Disadvantages of parallel Adder/Subtractor [2 marks]
1. Each adder has to wait for the carry to come from the previous adder in the
chain.
2. The propagation delay( delay associated with the travelling of carry bit) is
found to increase with the increase in the number of bits to be added.
Q5   a Explain the concept of the Translation Lookaside Buffer (TLB) and its working   10
CO2,   mechanism. Discuss why a TLB is required in modern computer systems. Illustrate
BT 2   your answer with a suitable diagram.
Ans:
(a)The Translation Lookaside Buffer (TLB) is a high-speed hardware
cache situated inside or near the Memory Management Unit (MMU). It
stores the most recently used mappings between Virtual Page Numbers
(VPNs) and Physical Frame Numbers (PFNs), reducing the need for
frequent page table lookups.
• Acts as a quick reference for recent virtual-to-physical address
translations.
•   Significantly speeds up memory access by minimizing main memory
lookups.
• Enhances overall CPU performance and efficiency in address translation.
********** 9 **********
--- page 10 ---
[diagram 4 Marks]
Reasons to use TLB : [explanation 6 marks]
When the CPU generates a virtual address, it must be translated into a physical
address to access data in main memory. The naive approach stores the entire page
table in main memory. Therefore, for every memory access, the following two
memory accesses are required:
1. Access the page table in main memory to get the frame number.
2. Access the actual data in the main memory frame.
3. This leads to a performance problem, as every memory access now
requires two memory accesses, causing a significant slowdown. 3M
CO2, b Apply Booth’s Algorithm to multiply 7 × 3 using 4-bit representation and show all   10
BT3   intermediate steps. Also, draw and explain the hardware structure of Booth’s
multiplier.
Ans: 5 marks for Solution
Step A B (Q) Q-1   Operation
INIT 0000 0011 0   Initial values
1   1001 0011 0 A ← A − M (10)
1   1100 1001 1   Arithmetic right shift
2   1100 1001 1 No operation (11)
2   1110 0100 1   Arithmetic right shift
3   0101 0100 1 A ← A + M (01)
3   0010 1010 0   Arithmetic right shift
4   0010 1010 0 No operation (00)
4   0001 0101 0   Arithmetic right shift
********** 10 **********
--- page 11 ---
2 marks= diagram
• The Booth's algorithm can be implemented as shown in the Fig. 2.19.
• The circuit is similar to circuit for positive number multiplication.
•   It consists of n-bit adder, shift, add subtract control logic and four registers,
A, B, Q and Q -1.
• As shown in the Fig. 2.19 multiplier and multiplicand are loaded into
register Q and register B, respectively, and register A and (2-1 are initially
set to 0.
3 marks explanation
Q6   a Explain the architecture of the 8086 microprocessors with a neat and labeled   10
CO3,   diagram. Describe the functions of its major components in detail.
BT2
Diagram of architecture: 4m
Explanation of Execution unit: 3m
Explanation of Bus Interface unit: 3m
The internal architecture of Intel 8086 is divided into 2 units: The Bus Interface Unit
(BIU), and The Execution Unit (EU).
********** 11 **********
--- page 12 ---
1. The Bus Interface Unit (BIU):It provides the interface of 8086 to external memory and
I/O devices via the System Bus. It performs various machine cycles such as memory read,
I/O   read,   etc.   to   transfer   data between memory and   I/O   devices.
BIU performs the following functions are as follows:
●   It generates the 20-bit physical address for memory access.
●   It fetches instructions from the memory.
●   It transfers data to and from the memory and I/O.
● Supports pipelining
BIU mainly contains the 4 Segment registers, the Instruction Pointer, a pre-fetch queue,
and an Address Generation Circuit.
Instruction Pointer (IP):
●   It is a 16-bit register. It holds offset of the next instructions in the Code
Segment.
●   IP is incremented after every instruction byte is fetched.
Code Segment register: (16 Bit register): CS holds the base address for the Code
Segment. All programs are stored in the Code Segment and accessed via the IP.
Data Segment register: (16 Bit register): DS holds the base address for the Data
Segment.
Stack Segment register: (16 Bit register): SS holds the base address for the Stack
Segment.
Extra Segment register: (16 Bit register): ES holds the base address for the Extra
Segment.
Address Generation Circuit:
● The BIU has a Physical Address Generation Circuit.
●   It generates the 20-bit physical address using Segment and Offset addresses
using the formula:
●   In Bus Interface Unit (BIU) the circuit shown by the Σ symbol is responsible for
the calculation unit which is used to calculate the physical address of an
instruction in memory.
Pre-fetch Queue:
●   It is a 6-byte queue (FIFO).
● Fetching the next instruction (by BIU from CS) while executing the current
instruction is called pipelining.
● Gets flushed whenever a branch instruction occurs.
● The pre-Fetch queue is of 6-Bytes only because the maximum size of instruction
that can have in 8086 is 6 bytes. Hence to cover up all operands and data fields
of maximum size instruction in 8086 Microprocessor there is a Pre-Fetch queue
is 6 Bytes.
2. The Execution Unit (EU):
The main components of the EU are General purpose registers, the ALU, Special purpose
registers, the Instruction Register and Instruction Decoder, and the Flag/Status Register.
Fetches instructions from the Queue in BIU, decodes, and executes arithmetic and logic
operations using the ALU. Sends control signals for internal data transfer operations
within the microprocessor (Control Unit). Sends request signals to the BIU to access the
external module.
8086 has four 16-bit general purpose registers AX, BX, CX, and DX which store
intermediate values during execution. Each of these has two 8-bit parts (higher and
lower).
********** 12 **********
--- page 13 ---
Special purpose registers (16-bit): Special purpose registers are called Offset registers
also. Which points to specific memory locations under each segment.
● Stack Pointer: Points to Stack top.
● Base Pointer: BP can hold the offset addresses of any location in the stack
segment.
● Source Index: It holds an offset address in Data Segment during string
operations.
● Destination Index: It holds offset addresses in Extra Segment during string
operations.
Instruction Register and Instruction Decoder: The EU fetches an opcode from the
queue into the instruction register. The instruction decoder decodes it and sends the
information to the control circuit for execution.
Flag/Status register (16 bits): It has 9 flags that help change or recognize the state of
the microprocessor.
Control unit : The Control Unit in the 8086 microprocessor is a component that
manages the overall operation of the microprocessor. The control unit is responsible for
controlling the flow of instructions through the microprocessor and coordinating the
activities of the other components, including the Decode Unit, Execution Unit, and
Prefetch Unit.
CO4, b Differentiate between Memory-Mapped I/O and I/O-Mapped I/O. Explain their   10
BT2   working principal.
Ans: difference 6 marks
Working 4 makrs
1. Memory-Mapped I/O – Working Principle
In Memory-Mapped I/O, I/O devices are treated as part of the main memory. Each
I/O device is assigned a unique memory address within the normal memory address
space.
Working:
• The CPU generates a memory address on the address bus.
• This address may refer to either:
o A memory location, or
o An I/O device register
• The control unit does not differentiate between memory and I/O initially.
********** 13 **********
--- page 14 ---
• The address decoder identifies whether the address belongs to RAM or an
I/O device.
•   If it is an I/O address:
o The corresponding device responds just like memory would.
• CPU uses normal instructions like:
o LOAD, STORE, MOV
2. I/O-Mapped I/O (Isolated I/O) – Working Principle
In I/O-Mapped I/O, I/O devices have a separate address space distinct from
memory.
Working:
• The CPU uses special I/O instructions like IN and OUT (8086
architecture).
• When an I/O instruction is executed:
o The CPU places the I/O port address on the address bus.
o   It activates I/O control signals (IOR or IOW).
• The memory system ignores this operation because memory and I/O are
separated.
• Only the selected I/O device responds to the I/O control signal.
• Data is transferred between CPU and I/O device via accumulator/registers.
Q7   a Explain the organization and operation of an I/O Processor with a suitable diagram.   10
CO4,   Ans:
BT2
2 marks what is IOP
2 marks diagram
6 marks explanation
Input / Output Processor [2 marks]
•An input-output processor (IOP) is a processor with direct memory access
capability.
•In this, the computer system is divided into a memory unit and number of
processors.
•Each IOP controls and manage the input-output tasks.
•The IOP is similar to CPU except that it handles only the details of I/O processing.
•The IOP can fetch and execute its own instructions.
•These IOP instructions are designed to manage I/O transfers only.
BelowisablockdiagramofacomputeralongwithvariousI/OProcessors.
•Thememoryunitoccupiesthecentralpositionandcancommunicatewitheachprocessor
.
•TheCPUprocessesthedatarequiredforsolvingthecomputationaltasks.
•TheIOPprovidesapathfortransferofdatabetweenperipheralsandmemory.
********** 14 **********
--- page 15 ---
•TheCPUassignsthetaskofinitiatingtheI/Oprogram.
•TheIOPoperatesindependentfromCPUandtransferdatabetweenperipheralsandmem
ory.
The communication between the IOP and the devices is similar to the program
control method of transfer.
•And the communication with the memory is similar to the direct memory access
method.
•In large scale computers, each processor is independent of other processors and
any processor can initiate the operation.
•The CPU can act as master and the IOP act as slave processor.
•The CPU assigns the task of initiating operations but it is the IOP, who executes
the instructions, and not the CPU.
•CPU instructions provide operations to start an I/O transfer.
•The IOP asks for CPU through interrupt.
•Instructions that are read from memory by an IOP are also called commands to
distinguish them from instructions that are read by CPU.
•Commands are prepared by programmers and are stored in memory.
•Command words make the program for IOP.
•CPU informs the IOP where to find the commands in memory.
CO1, b   i.   Identify the different methods of specifying operands in an instruction.   5
BT3   Illustrate any 2 methods with an example.
Ans:
Enlist the method 1 marks
Explaination of each method 2 marks   5
The different methods used to specify operands in an instruction are called Addressing
Modes.
Common methods (Addressing Modes):
1. Immediate Addressing Mode
2. Direct Addressing Mode
3. Indirect Addressing Mode
4. Register Addressing Mode
5. Register Indirect Addressing Mode
********** 15 **********
--- page 16 ---
6. Indexed Addressing Mode
7. Base (Displacement) Addressing Mode
8. Relative Addressing Mode
Immediate Addressing Mode
In this mode, the operand (data) is specified directly in the instruction itself.
Working Principle:
• The CPU does not need to access memory for the operand.
• The value is immediately available in the instruction.
Example:
MOV AL, 05H
Direct Addressing Mode
In this mode, the address of the operand is directly given in the instruction.
Working Principle:
• The instruction contains the memory address.
• CPU goes to that memory location to fetch the operand.
Example:
MOV AL, [2000H]
CO1,   ii.   Distinguish between computer organization and architecture.
BT2
Each difference 1 marks
********** 16 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 14d8ed7f117f

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_Computer_7032/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B.
Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 04 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. Assume Suitable data if necessary
Q.no   Questions   Mark
.   s
Q1
CO1, a Analyze the functional view of a computer and explain how different operations   5
BT2   (input, processing, output, storage) are coordinated during program execution.
Ans: 1 marks for each
There are four main functions of a computer:
• Data processing : Data may take a wide variety of forms and the range of
processing requirements is broad
• Data storage :
✓ Short-term
✓ Long-term
• Data movement:
✓ Input-output (I/O) - when data are received from or delivered to a
device (peripheral) that is directly connected to the computer
✓ Data communications – when data are moved over longer distances, to
or from a remote device
• Control
A control unit manages the computer’s resources and coordinates the
performance of its functional parts in response to instructions
During execution: 1 marks
• Control unit fetches instructions
• Decodes them
• Executes using ALU
•   Stores results in memory or sends to output
CO3, b What are the different types of registers in a CPU?   5
BT2   Ans:
1.25m for each type
********** 1 **********
--- page 2 ---
1. Accumulator : used to hold an operand and result of an ALU operation
2. General Purpose registers to hold data
3. Segment / Index / pointer registers to hold memory address
4. Status / Flag registers to indicate status of ALU operation ( Sign, Zero, Carry,
parity etc.)
CO4, c Define following:   5
BT2   a. Micro-operation
b. Micro-instruction
c. Micro-program
d. Micro-code
e. Control word
Ans:
Each 1 marks
Ans.
a. Micro-operation
A micro-operation is a basic operation performed on data stored in registers
within the CPU.
b. Micro-instruction
A micro-instruction is a binary control instruction that specifies one or more
micro-operations to be executed at a given time.
c. Micro-program
A micro-program is a sequence of micro-instructions stored in control memory
that implements a machine-level instruction.
d. Micro-code
Micro-code refers to the set of micro-instructions used to implement the
instruction set of a processor.
e. Control Word
A control word is a binary pattern of control signals that specifies the operations to be
performed in a single clock cycle.
CO4, d Explain superscalar architecture and its working principle.   5
BT4
Marks Bifurcation
Definition: 2 Marks
Working Principle: 3 Marks
Answer-
Superscalar architecture is a processor design that allows execution of multiple
instructions in a single clock cycle.
It works by using multiple pipelines and execution units. The processor fetches,
decodes, and dispatches multiple instructions simultaneously. Techniques like
instruction-level parallelism and out-of-order execution help improve
performance.
********** 2 **********
--- page 3 ---
This results in higher throughput and better CPU utilization.
Q2   a Describe, what is system bus arbitration? Explain the method of centralized bus   10
CO1,   arbitration in brief with diagram.
BT2
Ans: [1 marks defination]
bus arbitration : is who can use the Bus a specific time or More than one
module controlling the bus
• Bus Arbitration refers to the process by which the current bus master
accesses and then leaves the control of the bus and passes it to the another
bus requesting processor unit
• The controller that has access to a bus at an instance is known as Bus master
Method of centralized bus arbitration: 3 marks for each
(i)   Daisy Chaining method –
✓ It is a centralized bus arbitration method.
✓ It is a simple and cheaper method where all the bus masters use the same
line for making bus requests.
✓ The bus grant signal serially propagates through each master until it
encounters the first one that is requesting access to the bus.
✓ This master blocks the propagation of the bus grant signal, therefore any
other requesting module will not receive the grant signal and hence cannot
access the bus.
During any bus cycle, the bus master may be any device – the processor or any
DMA controller unit, connected to the bus.
ii)Polling or Rotating Priority method
✓ In this, the controller is used to generate the address for the master(unique
priority), the number of address lines required depends on the number of
masters connected in the system.
✓ the priorities are dynamically changed to give every device an opportunity
to access the bus.
✓ The controller generates a sequence of master addresses.
✓ When the requesting master recognizes its address, it activates the busy line
and begins to use the bus.
********** 3 **********
--- page 4 ---
(iii) Fixed priority or Independent Request method
✓ In this, each master has a separate pair of bus request and bus grant lines
and each pair has a priority assigned to it.
The built-in priority decoder within the controller selects the highest priority
request   and   asserts   the   corresponding   bus   grant   signal.
CO2, b Consider a computer system with the following cache specifications:   10
BT3   • Cache size = 256 KB
• Block size = 64 bytes
• Mapping technique = Direct mapping
• Main memory size = 4 MB
Assume that the system uses byte-addressable memory. Divide the main memory
address into Tag, Index, and Block Offset fields, clearly specifying the number of
bits in each.
Ans:
2.5 marks for each Step:
********** 4 **********
--- page 5 ---
Final division of the 22-bit main memory address:
Field   Number of Bits
Tag   4 bits
Index   12 bits
Block Offset 6 bits
Q3   a Explain hardware interrupts and software interrupts in detail. Compare the   10
CO1,   interrupt-driven I/O method with the polling method and justify why interrupts are
BT2   more efficient.
Ans:
1. Hardware Interrupts 2 marks
Definition:
Hardware interrupts are signals sent to the CPU by external hardware devices to
indicate they need immediate attention.
• Triggered by external events (e.g., keyboard input, mouse click, I/O device
ready).
• Asynchronous to the CPU’s current operations.
Software Interrupts 2 marks
Definition:
Software interrupts are generated by programs or the CPU itself to request OS
services or handle exceptional conditions.
• Triggered by executing specific instructions (e.g., INT in x86 assembly).
• Synchronous with program execution.
• Used for system calls, debugging, or handling errors like divide-by-zero.
Comparison: 4 Marks
********** 5 **********
--- page 6 ---
Why Interrupts Are More Efficient : 2 marks
1. Eliminate   Wasteful   Waiting:
Interrupts free the CPU from continuous checking, allowing it to execute
other instructions until the device needs attention.
2. Better   CPU   Utilization:
CPU resources are used more effectively for useful work rather than polling.
CO2, b Compare the IEEE 754 single precision and double precision formats. Show the   10
BT3   representations side by side and state two practical scenarios where double
precision is preferred over single precision.
Ans: 8 marks for Difference
1. Bit-Level Representation (Side-by-Side)
Component   Single Precision (32-bit) Double Precision (64-bit)
Sign bit   1 bit   1 bit
Exponent   8 bits   11 bits
Mantissa (Fraction) 23 bits   52 bits
Total Size   32 bits   64 bits
2. Format Structure
Single Precision (32-bit)
| S | Exponent (8 bits) | Fraction (23 bits) |
Double Precision (64-bit)
| S | Exponent (11 bits) | Fraction (52 bits) |
3. Key Differences
Feature   Single Precision   Double Precision
Precision   ~6–7 decimal digits ~15–16 decimal digits
Range   Smaller   Much larger
Memory usage   4 bytes   8 bytes
Computational speed Faster   Slightly slower
********** 6 **********
--- page 7 ---
Rounding error   Higher   Lower
When Double Precision is Preferred (Any Two Scenarios) : 2 marks
1. Scientific and Engineering Calculations
Used in simulations such as:
• Weather forecasting
•   Fluid dynamics
•   Structural engineering analysis
Reason: These applications require high numerical accuracy and small rounding
errors can significantly affect results.
2. Financial and Statistical Computations
Used in:
• Risk analysis models
•   Large-scale financial forecasting
• Machine learning statistical computations
Q4   a Explain the concept of Content Addressable Memory (CAM). Describe its working   10
CO2,   principle with a neat diagram.
BT2   And:
Explain the concept of Content Addressable Memory (CAM) 2 marks
• A memory unit accessed by content of data rather than address is also known
as content addressable memory(CAM).
• The content is accessed parallel on the basis of data rather than specific
address or location
• A search can be done entire word or specific field within a word.
•   It is more expensive because each cell consist the storage capacity and logic
circuits for matching its content.
• Example: Neural network for pattern search, Google
working principle:
********** 7 **********
--- page 8 ---
diagram=3 marks
•   Searching word contained by argument register (A) with n-bits ,1-bit for
word
• A is matched with AM then it is placed in match register as 1 otherwise it is
denoted with 0.
• Content is searched based on portion then store in key register indicating
by 1 other bits represented by 0
• Complete word need to search the k will content all 1’s otherwise specific
position contains 1.
• Reading is performed in sequential; writing is performed in empty cells.
[Explanation 5 marks]
CO2, b Explain the design and working of a 4-bit parallel adder–subtractor with a neat   10
BT2   diagram. Illustrate how the circuit performs both addition and subtraction using
control logic. Also state the advantages and disadvantages of the parallel adder–
subtractor.
Ans:
[Diagram with explanation 6 marks ]
********** 8 **********
--- page 9 ---
• Advantages of parallel Adder/Subtractor [2 marks]
1. The parallel adder/subtractor performs the addition operation faster as
compared to serial adder/subtractor.
2. Time required for addition does not depend on the number of bits.
3. The output is in parallel form i.e all the bits are added/subtracted at the same
time.
4. It is less costly.
• Disadvantages of parallel Adder/Subtractor [2 marks]
1. Each adder has to wait for the carry to come from the previous adder in the
chain.
2. The propagation delay( delay associated with the travelling of carry bit) is
found to increase with the increase in the number of bits to be added.
Q5   a Explain the concept of the Translation Lookaside Buffer (TLB) and its working   10
CO2,   mechanism. Discuss why a TLB is required in modern computer systems. Illustrate
BT 2   your answer with a suitable diagram.
Ans:
(a)The Translation Lookaside Buffer (TLB) is a high-speed hardware
cache situated inside or near the Memory Management Unit (MMU). It
stores the most recently used mappings between Virtual Page Numbers
(VPNs) and Physical Frame Numbers (PFNs), reducing the need for
frequent page table lookups.
• Acts as a quick reference for recent virtual-to-physical address
translations.
•   Significantly speeds up memory access by minimizing main memory
lookups.
• Enhances overall CPU performance and efficiency in address translation.
********** 9 **********
--- page 10 ---
[diagram 4 Marks]
Reasons to use TLB : [explanation 6 marks]
When the CPU generates a virtual address, it must be translated into a physical
address to access data in main memory. The naive approach stores the entire page
table in main memory. Therefore, for every memory access, the following two
memory accesses are required:
1. Access the page table in main memory to get the frame number.
2. Access the actual data in the main memory frame.
3. This leads to a performance problem, as every memory access now
requires two memory accesses, causing a significant slowdown. 3M
CO2, b Apply Booth’s Algorithm to multiply 7 × 3 using 4-bit representation and show all   10
BT3   intermediate steps. Also, draw and explain the hardware structure of Booth’s
multiplier.
Ans: 5 marks for Solution
Step A B (Q) Q-1   Operation
INIT 0000 0011 0   Initial values
1   1001 0011 0 A ← A − M (10)
1   1100 1001 1   Arithmetic right shift
2   1100 1001 1 No operation (11)
2   1110 0100 1   Arithmetic right shift
3   0101 0100 1 A ← A + M (01)
3   0010 1010 0   Arithmetic right shift
4   0010 1010 0 No operation (00)
4   0001 0101 0   Arithmetic right shift
********** 10 **********
--- page 11 ---
2 marks= diagram
• The Booth's algorithm can be implemented as shown in the Fig. 2.19.
• The circuit is similar to circuit for positive number multiplication.
•   It consists of n-bit adder, shift, add subtract control logic and four registers,
A, B, Q and Q -1.
• As shown in the Fig. 2.19 multiplier and multiplicand are loaded into
register Q and register B, respectively, and register A and (2-1 are initially
set to 0.
3 marks explanation
Q6   a Explain the architecture of the 8086 microprocessors with a neat and labeled   10
CO3,   diagram. Describe the functions of its major components in detail.
BT2
Diagram of architecture: 4m
Explanation of Execution unit: 3m
Explanation of Bus Interface unit: 3m
The internal architecture of Intel 8086 is divided into 2 units: The Bus Interface Unit
(BIU), and The Execution Unit (EU).
********** 11 **********
--- page 12 ---
1. The Bus Interface Unit (BIU):It provides the interface of 8086 to external memory and
I/O devices via the System Bus. It performs various machine cycles such as memory read,
I/O   read,   etc.   to   transfer   data between memory and   I/O   devices.
BIU performs the following functions are as follows:
●   It generates the 20-bit physical address for memory access.
●   It fetches instructions from the memory.
●   It transfers data to and from the memory and I/O.
● Supports pipelining
BIU mainly contains the 4 Segment registers, the Instruction Pointer, a pre-fetch queue,
and an Address Generation Circuit.
Instruction Pointer (IP):
●   It is a 16-bit register. It holds offset of the next instructions in the Code
Segment.
●   IP is incremented after every instruction byte is fetched.
Code Segment register: (16 Bit register): CS holds the base address for the Code
Segment. All programs are stored in the Code Segment and accessed via the IP.
Data Segment register: (16 Bit register): DS holds the base address for the Data
Segment.
Stack Segment register: (16 Bit register): SS holds the base address for the Stack
Segment.
Extra Segment register: (16 Bit register): ES holds the base address for the Extra
Segment.
Address Generation Circuit:
● The BIU has a Physical Address Generation Circuit.
●   It generates the 20-bit physical address using Segment and Offset addresses
using the formula:
●   In Bus Interface Unit (BIU) the circuit shown by the Σ symbol is responsible for
the calculation unit which is used to calculate the physical address of an
instruction in memory.
Pre-fetch Queue:
●   It is a 6-byte queue (FIFO).
● Fetching the next instruction (by BIU from CS) while executing the current
instruction is called pipelining.
● Gets flushed whenever a branch instruction occurs.
● The pre-Fetch queue is of 6-Bytes only because the maximum size of instruction
that can have in 8086 is 6 bytes. Hence to cover up all operands and data fields
of maximum size instruction in 8086 Microprocessor there is a Pre-Fetch queue
is 6 Bytes.
2. The Execution Unit (EU):
The main components of the EU are General purpose registers, the ALU, Special purpose
registers, the Instruction Register and Instruction Decoder, and the Flag/Status Register.
Fetches instructions from the Queue in BIU, decodes, and executes arithmetic and logic
operations using the ALU. Sends control signals for internal data transfer operations
within the microprocessor (Control Unit). Sends request signals to the BIU to access the
external module.
8086 has four 16-bit general purpose registers AX, BX, CX, and DX which store
intermediate values during execution. Each of these has two 8-bit parts (higher and
lower).
********** 12 **********
--- page 13 ---
Special purpose registers (16-bit): Special purpose registers are called Offset registers
also. Which points to specific memory locations under each segment.
● Stack Pointer: Points to Stack top.
● Base Pointer: BP can hold the offset addresses of any location in the stack
segment.
● Source Index: It holds an offset address in Data Segment during string
operations.
● Destination Index: It holds offset addresses in Extra Segment during string
operations.
Instruction Register and Instruction Decoder: The EU fetches an opcode from the
queue into the instruction register. The instruction decoder decodes it and sends the
information to the control circuit for execution.
Flag/Status register (16 bits): It has 9 flags that help change or recognize the state of
the microprocessor.
Control unit : The Control Unit in the 8086 microprocessor is a component that
manages the overall operation of the microprocessor. The control unit is responsible for
controlling the flow of instructions through the microprocessor and coordinating the
activities of the other components, including the Decode Unit, Execution Unit, and
Prefetch Unit.
CO4, b Differentiate between Memory-Mapped I/O and I/O-Mapped I/O. Explain their   10
BT2   working principal.
Ans: difference 6 marks
Working 4 makrs
1. Memory-Mapped I/O – Working Principle
In Memory-Mapped I/O, I/O devices are treated as part of the main memory. Each
I/O device is assigned a unique memory address within the normal memory address
space.
Working:
• The CPU generates a memory address on the address bus.
• This address may refer to either:
o A memory location, or
o An I/O device register
• The control unit does not differentiate between memory and I/O initially.
********** 13 **********
--- page 14 ---
• The address decoder identifies whether the address belongs to RAM or an
I/O device.
•   If it is an I/O address:
o The corresponding device responds just like memory would.
• CPU uses normal instructions like:
o LOAD, STORE, MOV
2. I/O-Mapped I/O (Isolated I/O) – Working Principle
In I/O-Mapped I/O, I/O devices have a separate address space distinct from
memory.
Working:
• The CPU uses special I/O instructions like IN and OUT (8086
architecture).
• When an I/O instruction is executed:
o The CPU places the I/O port address on the address bus.
o   It activates I/O control signals (IOR or IOW).
• The memory system ignores this operation because memory and I/O are
separated.
• Only the selected I/O device responds to the I/O control signal.
• Data is transferred between CPU and I/O device via accumulator/registers.
Q7   a Explain the organization and operation of an I/O Processor with a suitable diagram.   10
CO4,   Ans:
BT2
2 marks what is IOP
2 marks diagram
6 marks explanation
Input / Output Processor [2 marks]
•An input-output processor (IOP) is a processor with direct memory access
capability.
•In this, the computer system is divided into a memory unit and number of
processors.
•Each IOP controls and manage the input-output tasks.
•The IOP is similar to CPU except that it handles only the details of I/O processing.
•The IOP can fetch and execute its own instructions.
•These IOP instructions are designed to manage I/O transfers only.
BelowisablockdiagramofacomputeralongwithvariousI/OProcessors.
•Thememoryunitoccupiesthecentralpositionandcancommunicatewitheachprocessor
.
•TheCPUprocessesthedatarequiredforsolvingthecomputationaltasks.
•TheIOPprovidesapathfortransferofdatabetweenperipheralsandmemory.
********** 14 **********
--- page 15 ---
•TheCPUassignsthetaskofinitiatingtheI/Oprogram.
•TheIOPoperatesindependentfromCPUandtransferdatabetweenperipheralsandmem
ory.
The communication between the IOP and the devices is similar to the program
control method of transfer.
•And the communication with the memory is similar to the direct memory access
method.
•In large scale computers, each processor is independent of other processors and
any processor can initiate the operation.
•The CPU can act as master and the IOP act as slave processor.
•The CPU assigns the task of initiating operations but it is the IOP, who executes
the instructions, and not the CPU.
•CPU instructions provide operations to start an I/O transfer.
•The IOP asks for CPU through interrupt.
•Instructions that are read from memory by an IOP are also called commands to
distinguish them from instructions that are read by CPU.
•Commands are prepared by programmers and are stored in memory.
•Command words make the program for IOP.
•CPU informs the IOP where to find the commands in memory.
CO1, b   i.   Identify the different methods of specifying operands in an instruction.   5
BT3   Illustrate any 2 methods with an example.
Ans:
Enlist the method 1 marks
Explaination of each method 2 marks   5
The different methods used to specify operands in an instruction are called Addressing
Modes.
Common methods (Addressing Modes):
1. Immediate Addressing Mode
2. Direct Addressing Mode
3. Indirect Addressing Mode
4. Register Addressing Mode
5. Register Indirect Addressing Mode
********** 15 **********
--- page 16 ---
6. Indexed Addressing Mode
7. Base (Displacement) Addressing Mode
8. Relative Addressing Mode
Immediate Addressing Mode
In this mode, the operand (data) is specified directly in the instruction itself.
Working Principle:
• The CPU does not need to access memory for the operand.
• The value is immediately available in the instruction.
Example:
MOV AL, 05H
Direct Addressing Mode
In this mode, the address of the operand is directly given in the instruction.
Working Principle:
• The instruction contains the memory address.
• CPU goes to that memory location to fetch the operand.
Example:
MOV AL, [2000H]
CO1,   ii.   Distinguish between computer organization and architecture.
BT2
Each difference 1 marks
********** 16 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper e06b373ead47

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_IT_7037/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B.
Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 04 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. Assume Suitable data if necessary
Q.no   Questions   Mark
.   s
Q1
CO1, a Analyze the functional view of a computer and explain how different operations   5
BT2   (input, processing, output, storage) are coordinated during program execution.
Ans: 1 marks for each
There are four main functions of a computer:
• Data processing : Data may take a wide variety of forms and the range of
processing requirements is broad
• Data storage :
✓ Short-term
✓ Long-term
• Data movement:
✓ Input-output (I/O) - when data are received from or delivered to a
device (peripheral) that is directly connected to the computer
✓ Data communications – when data are moved over longer distances, to
or from a remote device
• Control
A control unit manages the computer’s resources and coordinates the
performance of its functional parts in response to instructions
During execution: 1 marks
• Control unit fetches instructions
• Decodes them
• Executes using ALU
•   Stores results in memory or sends to output
CO3, b What are the different types of registers in a CPU?   5
BT2   Ans:
1.25m for each type
********** 1 **********
--- page 2 ---
1. Accumulator : used to hold an operand and result of an ALU operation
2. General Purpose registers to hold data
3. Segment / Index / pointer registers to hold memory address
4. Status / Flag registers to indicate status of ALU operation ( Sign, Zero, Carry,
parity etc.)
CO4, c Define following:   5
BT2   a. Micro-operation
b. Micro-instruction
c. Micro-program
d. Micro-code
e. Control word
Ans:
Each 1 marks
Ans.
a. Micro-operation
A micro-operation is a basic operation performed on data stored in registers
within the CPU.
b. Micro-instruction
A micro-instruction is a binary control instruction that specifies one or more
micro-operations to be executed at a given time.
c. Micro-program
A micro-program is a sequence of micro-instructions stored in control memory
that implements a machine-level instruction.
d. Micro-code
Micro-code refers to the set of micro-instructions used to implement the
instruction set of a processor.
e. Control Word
A control word is a binary pattern of control signals that specifies the operations to be
performed in a single clock cycle.
CO4, d Explain superscalar architecture and its working principle.   5
BT4
Marks Bifurcation
Definition: 2 Marks
Working Principle: 3 Marks
Answer-
Superscalar architecture is a processor design that allows execution of multiple
instructions in a single clock cycle.
It works by using multiple pipelines and execution units. The processor fetches,
decodes, and dispatches multiple instructions simultaneously. Techniques like
instruction-level parallelism and out-of-order execution help improve
performance.
********** 2 **********
--- page 3 ---
This results in higher throughput and better CPU utilization.
Q2   a Describe, what is system bus arbitration? Explain the method of centralized bus   10
CO1,   arbitration in brief with diagram.
BT2
Ans: [1 marks defination]
bus arbitration : is who can use the Bus a specific time or More than one
module controlling the bus
• Bus Arbitration refers to the process by which the current bus master
accesses and then leaves the control of the bus and passes it to the another
bus requesting processor unit
• The controller that has access to a bus at an instance is known as Bus master
Method of centralized bus arbitration: 3 marks for each
(i)   Daisy Chaining method –
✓ It is a centralized bus arbitration method.
✓ It is a simple and cheaper method where all the bus masters use the same
line for making bus requests.
✓ The bus grant signal serially propagates through each master until it
encounters the first one that is requesting access to the bus.
✓ This master blocks the propagation of the bus grant signal, therefore any
other requesting module will not receive the grant signal and hence cannot
access the bus.
During any bus cycle, the bus master may be any device – the processor or any
DMA controller unit, connected to the bus.
ii)Polling or Rotating Priority method
✓ In this, the controller is used to generate the address for the master(unique
priority), the number of address lines required depends on the number of
masters connected in the system.
✓ the priorities are dynamically changed to give every device an opportunity
to access the bus.
✓ The controller generates a sequence of master addresses.
✓ When the requesting master recognizes its address, it activates the busy line
and begins to use the bus.
********** 3 **********
--- page 4 ---
(iii) Fixed priority or Independent Request method
✓ In this, each master has a separate pair of bus request and bus grant lines
and each pair has a priority assigned to it.
The built-in priority decoder within the controller selects the highest priority
request   and   asserts   the   corresponding   bus   grant   signal.
CO2, b Consider a computer system with the following cache specifications:   10
BT3   • Cache size = 256 KB
• Block size = 64 bytes
• Mapping technique = Direct mapping
• Main memory size = 4 MB
Assume that the system uses byte-addressable memory. Divide the main memory
address into Tag, Index, and Block Offset fields, clearly specifying the number of
bits in each.
Ans:
2.5 marks for each Step:
********** 4 **********
--- page 5 ---
Final division of the 22-bit main memory address:
Field   Number of Bits
Tag   4 bits
Index   12 bits
Block Offset 6 bits
Q3   a Explain hardware interrupts and software interrupts in detail. Compare the   10
CO1,   interrupt-driven I/O method with the polling method and justify why interrupts are
BT2   more efficient.
Ans:
1. Hardware Interrupts 2 marks
Definition:
Hardware interrupts are signals sent to the CPU by external hardware devices to
indicate they need immediate attention.
• Triggered by external events (e.g., keyboard input, mouse click, I/O device
ready).
• Asynchronous to the CPU’s current operations.
Software Interrupts 2 marks
Definition:
Software interrupts are generated by programs or the CPU itself to request OS
services or handle exceptional conditions.
• Triggered by executing specific instructions (e.g., INT in x86 assembly).
• Synchronous with program execution.
• Used for system calls, debugging, or handling errors like divide-by-zero.
Comparison: 4 Marks
********** 5 **********
--- page 6 ---
Why Interrupts Are More Efficient : 2 marks
1. Eliminate   Wasteful   Waiting:
Interrupts free the CPU from continuous checking, allowing it to execute
other instructions until the device needs attention.
2. Better   CPU   Utilization:
CPU resources are used more effectively for useful work rather than polling.
CO2, b Compare the IEEE 754 single precision and double precision formats. Show the   10
BT3   representations side by side and state two practical scenarios where double
precision is preferred over single precision.
Ans: 8 marks for Difference
1. Bit-Level Representation (Side-by-Side)
Component   Single Precision (32-bit) Double Precision (64-bit)
Sign bit   1 bit   1 bit
Exponent   8 bits   11 bits
Mantissa (Fraction) 23 bits   52 bits
Total Size   32 bits   64 bits
2. Format Structure
Single Precision (32-bit)
| S | Exponent (8 bits) | Fraction (23 bits) |
Double Precision (64-bit)
| S | Exponent (11 bits) | Fraction (52 bits) |
3. Key Differences
Feature   Single Precision   Double Precision
Precision   ~6–7 decimal digits ~15–16 decimal digits
Range   Smaller   Much larger
Memory usage   4 bytes   8 bytes
Computational speed Faster   Slightly slower
********** 6 **********
--- page 7 ---
Rounding error   Higher   Lower
When Double Precision is Preferred (Any Two Scenarios) : 2 marks
1. Scientific and Engineering Calculations
Used in simulations such as:
• Weather forecasting
•   Fluid dynamics
•   Structural engineering analysis
Reason: These applications require high numerical accuracy and small rounding
errors can significantly affect results.
2. Financial and Statistical Computations
Used in:
• Risk analysis models
•   Large-scale financial forecasting
• Machine learning statistical computations
Q4   a Explain the concept of Content Addressable Memory (CAM). Describe its working   10
CO2,   principle with a neat diagram.
BT2   And:
Explain the concept of Content Addressable Memory (CAM) 2 marks
• A memory unit accessed by content of data rather than address is also known
as content addressable memory(CAM).
• The content is accessed parallel on the basis of data rather than specific
address or location
• A search can be done entire word or specific field within a word.
•   It is more expensive because each cell consist the storage capacity and logic
circuits for matching its content.
• Example: Neural network for pattern search, Google
working principle:
********** 7 **********
--- page 8 ---
diagram=3 marks
•   Searching word contained by argument register (A) with n-bits ,1-bit for
word
• A is matched with AM then it is placed in match register as 1 otherwise it is
denoted with 0.
• Content is searched based on portion then store in key register indicating
by 1 other bits represented by 0
• Complete word need to search the k will content all 1’s otherwise specific
position contains 1.
• Reading is performed in sequential; writing is performed in empty cells.
[Explanation 5 marks]
CO2, b Explain the design and working of a 4-bit parallel adder–subtractor with a neat   10
BT2   diagram. Illustrate how the circuit performs both addition and subtraction using
control logic. Also state the advantages and disadvantages of the parallel adder–
subtractor.
Ans:
[Diagram with explanation 6 marks ]
********** 8 **********
--- page 9 ---
• Advantages of parallel Adder/Subtractor [2 marks]
1. The parallel adder/subtractor performs the addition operation faster as
compared to serial adder/subtractor.
2. Time required for addition does not depend on the number of bits.
3. The output is in parallel form i.e all the bits are added/subtracted at the same
time.
4. It is less costly.
• Disadvantages of parallel Adder/Subtractor [2 marks]
1. Each adder has to wait for the carry to come from the previous adder in the
chain.
2. The propagation delay( delay associated with the travelling of carry bit) is
found to increase with the increase in the number of bits to be added.
Q5   a Explain the concept of the Translation Lookaside Buffer (TLB) and its working   10
CO2,   mechanism. Discuss why a TLB is required in modern computer systems. Illustrate
BT 2   your answer with a suitable diagram.
Ans:
(a)The Translation Lookaside Buffer (TLB) is a high-speed hardware
cache situated inside or near the Memory Management Unit (MMU). It
stores the most recently used mappings between Virtual Page Numbers
(VPNs) and Physical Frame Numbers (PFNs), reducing the need for
frequent page table lookups.
• Acts as a quick reference for recent virtual-to-physical address
translations.
•   Significantly speeds up memory access by minimizing main memory
lookups.
• Enhances overall CPU performance and efficiency in address translation.
********** 9 **********
--- page 10 ---
[diagram 4 Marks]
Reasons to use TLB : [explanation 6 marks]
When the CPU generates a virtual address, it must be translated into a physical
address to access data in main memory. The naive approach stores the entire page
table in main memory. Therefore, for every memory access, the following two
memory accesses are required:
1. Access the page table in main memory to get the frame number.
2. Access the actual data in the main memory frame.
3. This leads to a performance problem, as every memory access now
requires two memory accesses, causing a significant slowdown. 3M
CO2, b Apply Booth’s Algorithm to multiply 7 × 3 using 4-bit representation and show all   10
BT3   intermediate steps. Also, draw and explain the hardware structure of Booth’s
multiplier.
Ans: 5 marks for Solution
Step A B (Q) Q-1   Operation
INIT 0000 0011 0   Initial values
1   1001 0011 0 A ← A − M (10)
1   1100 1001 1   Arithmetic right shift
2   1100 1001 1 No operation (11)
2   1110 0100 1   Arithmetic right shift
3   0101 0100 1 A ← A + M (01)
3   0010 1010 0   Arithmetic right shift
4   0010 1010 0 No operation (00)
4   0001 0101 0   Arithmetic right shift
********** 10 **********
--- page 11 ---
2 marks= diagram
• The Booth's algorithm can be implemented as shown in the Fig. 2.19.
• The circuit is similar to circuit for positive number multiplication.
•   It consists of n-bit adder, shift, add subtract control logic and four registers,
A, B, Q and Q -1.
• As shown in the Fig. 2.19 multiplier and multiplicand are loaded into
register Q and register B, respectively, and register A and (2-1 are initially
set to 0.
3 marks explanation
Q6   a Explain the architecture of the 8086 microprocessors with a neat and labeled   10
CO3,   diagram. Describe the functions of its major components in detail.
BT2
Diagram of architecture: 4m
Explanation of Execution unit: 3m
Explanation of Bus Interface unit: 3m
The internal architecture of Intel 8086 is divided into 2 units: The Bus Interface Unit
(BIU), and The Execution Unit (EU).
********** 11 **********
--- page 12 ---
1. The Bus Interface Unit (BIU):It provides the interface of 8086 to external memory and
I/O devices via the System Bus. It performs various machine cycles such as memory read,
I/O   read,   etc.   to   transfer   data between memory and   I/O   devices.
BIU performs the following functions are as follows:
●   It generates the 20-bit physical address for memory access.
●   It fetches instructions from the memory.
●   It transfers data to and from the memory and I/O.
● Supports pipelining
BIU mainly contains the 4 Segment registers, the Instruction Pointer, a pre-fetch queue,
and an Address Generation Circuit.
Instruction Pointer (IP):
●   It is a 16-bit register. It holds offset of the next instructions in the Code
Segment.
●   IP is incremented after every instruction byte is fetched.
Code Segment register: (16 Bit register): CS holds the base address for the Code
Segment. All programs are stored in the Code Segment and accessed via the IP.
Data Segment register: (16 Bit register): DS holds the base address for the Data
Segment.
Stack Segment register: (16 Bit register): SS holds the base address for the Stack
Segment.
Extra Segment register: (16 Bit register): ES holds the base address for the Extra
Segment.
Address Generation Circuit:
● The BIU has a Physical Address Generation Circuit.
●   It generates the 20-bit physical address using Segment and Offset addresses
using the formula:
●   In Bus Interface Unit (BIU) the circuit shown by the Σ symbol is responsible for
the calculation unit which is used to calculate the physical address of an
instruction in memory.
Pre-fetch Queue:
●   It is a 6-byte queue (FIFO).
● Fetching the next instruction (by BIU from CS) while executing the current
instruction is called pipelining.
● Gets flushed whenever a branch instruction occurs.
● The pre-Fetch queue is of 6-Bytes only because the maximum size of instruction
that can have in 8086 is 6 bytes. Hence to cover up all operands and data fields
of maximum size instruction in 8086 Microprocessor there is a Pre-Fetch queue
is 6 Bytes.
2. The Execution Unit (EU):
The main components of the EU are General purpose registers, the ALU, Special purpose
registers, the Instruction Register and Instruction Decoder, and the Flag/Status Register.
Fetches instructions from the Queue in BIU, decodes, and executes arithmetic and logic
operations using the ALU. Sends control signals for internal data transfer operations
within the microprocessor (Control Unit). Sends request signals to the BIU to access the
external module.
8086 has four 16-bit general purpose registers AX, BX, CX, and DX which store
intermediate values during execution. Each of these has two 8-bit parts (higher and
lower).
********** 12 **********
--- page 13 ---
Special purpose registers (16-bit): Special purpose registers are called Offset registers
also. Which points to specific memory locations under each segment.
● Stack Pointer: Points to Stack top.
● Base Pointer: BP can hold the offset addresses of any location in the stack
segment.
● Source Index: It holds an offset address in Data Segment during string
operations.
● Destination Index: It holds offset addresses in Extra Segment during string
operations.
Instruction Register and Instruction Decoder: The EU fetches an opcode from the
queue into the instruction register. The instruction decoder decodes it and sends the
information to the control circuit for execution.
Flag/Status register (16 bits): It has 9 flags that help change or recognize the state of
the microprocessor.
Control unit : The Control Unit in the 8086 microprocessor is a component that
manages the overall operation of the microprocessor. The control unit is responsible for
controlling the flow of instructions through the microprocessor and coordinating the
activities of the other components, including the Decode Unit, Execution Unit, and
Prefetch Unit.
CO4, b Differentiate between Memory-Mapped I/O and I/O-Mapped I/O. Explain their   10
BT2   working principal.
Ans: difference 6 marks
Working 4 makrs
1. Memory-Mapped I/O – Working Principle
In Memory-Mapped I/O, I/O devices are treated as part of the main memory. Each
I/O device is assigned a unique memory address within the normal memory address
space.
Working:
• The CPU generates a memory address on the address bus.
• This address may refer to either:
o A memory location, or
o An I/O device register
• The control unit does not differentiate between memory and I/O initially.
********** 13 **********
--- page 14 ---
• The address decoder identifies whether the address belongs to RAM or an
I/O device.
•   If it is an I/O address:
o The corresponding device responds just like memory would.
• CPU uses normal instructions like:
o LOAD, STORE, MOV
2. I/O-Mapped I/O (Isolated I/O) – Working Principle
In I/O-Mapped I/O, I/O devices have a separate address space distinct from
memory.
Working:
• The CPU uses special I/O instructions like IN and OUT (8086
architecture).
• When an I/O instruction is executed:
o The CPU places the I/O port address on the address bus.
o   It activates I/O control signals (IOR or IOW).
• The memory system ignores this operation because memory and I/O are
separated.
• Only the selected I/O device responds to the I/O control signal.
• Data is transferred between CPU and I/O device via accumulator/registers.
Q7   a Explain the organization and operation of an I/O Processor with a suitable diagram.   10
CO4,   Ans:
BT2
2 marks what is IOP
2 marks diagram
6 marks explanation
Input / Output Processor [2 marks]
•An input-output processor (IOP) is a processor with direct memory access
capability.
•In this, the computer system is divided into a memory unit and number of
processors.
•Each IOP controls and manage the input-output tasks.
•The IOP is similar to CPU except that it handles only the details of I/O processing.
•The IOP can fetch and execute its own instructions.
•These IOP instructions are designed to manage I/O transfers only.
BelowisablockdiagramofacomputeralongwithvariousI/OProcessors.
•Thememoryunitoccupiesthecentralpositionandcancommunicatewitheachprocessor
.
•TheCPUprocessesthedatarequiredforsolvingthecomputationaltasks.
•TheIOPprovidesapathfortransferofdatabetweenperipheralsandmemory.
********** 14 **********
--- page 15 ---
•TheCPUassignsthetaskofinitiatingtheI/Oprogram.
•TheIOPoperatesindependentfromCPUandtransferdatabetweenperipheralsandmem
ory.
The communication between the IOP and the devices is similar to the program
control method of transfer.
•And the communication with the memory is similar to the direct memory access
method.
•In large scale computers, each processor is independent of other processors and
any processor can initiate the operation.
•The CPU can act as master and the IOP act as slave processor.
•The CPU assigns the task of initiating operations but it is the IOP, who executes
the instructions, and not the CPU.
•CPU instructions provide operations to start an I/O transfer.
•The IOP asks for CPU through interrupt.
•Instructions that are read from memory by an IOP are also called commands to
distinguish them from instructions that are read by CPU.
•Commands are prepared by programmers and are stored in memory.
•Command words make the program for IOP.
•CPU informs the IOP where to find the commands in memory.
CO1, b   i.   Identify the different methods of specifying operands in an instruction.   5
BT3   Illustrate any 2 methods with an example.
Ans:
Enlist the method 1 marks
Explaination of each method 2 marks   5
The different methods used to specify operands in an instruction are called Addressing
Modes.
Common methods (Addressing Modes):
1. Immediate Addressing Mode
2. Direct Addressing Mode
3. Indirect Addressing Mode
4. Register Addressing Mode
5. Register Indirect Addressing Mode
********** 15 **********
--- page 16 ---
6. Indexed Addressing Mode
7. Base (Displacement) Addressing Mode
8. Relative Addressing Mode
Immediate Addressing Mode
In this mode, the operand (data) is specified directly in the instruction itself.
Working Principle:
• The CPU does not need to access memory for the operand.
• The value is immediately available in the instruction.
Example:
MOV AL, 05H
Direct Addressing Mode
In this mode, the address of the operand is directly given in the instruction.
Working Principle:
• The instruction contains the memory address.
• CPU goes to that memory location to fetch the operand.
Example:
MOV AL, [2000H]
CO1,   ii.   Distinguish between computer organization and architecture.
BT2
Each difference 1 marks
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 5512010777d4

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_AIML_7053/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & ML)/B. Tech (CSBS)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 09 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions..
6. Assume Suitable data if necessary.
Q.n   Question   Mark
o.   s
1
CO1 a Explain the role of Registers in CPU operation. Mention any four types of registers and their 5
,   functions.
BT3
Answer:
Registers are small, high-speed storage locations inside the Central Processing Unit (CPU).
They are used to store data, instructions, addresses, and intermediate results temporarily
during program execution.
Role of Registers in CPU Operation: 1 marks
Registers play a crucial role in every step of instruction execution. Their main roles include:
1. Holding Instructions and Data:
2. Storing Addresses:
3. Temporary Storage for Arithmetic/Logic Operations:
4. Instruction Control and Sequencing:
(i) Program Counter (PC) 1 mark for explanation of each
•   Function:
Holds the address of the next instruction to be fetched from memory for
execution.
After fetching an instruction, the PC is automatically incremented to point to the
next one.
(ii) Instruction Register (IR)
•   Function:
Stores the current instruction that has been fetched from memory and is being
decoded and executed.
•   Process:
o CPU fetches the instruction from memory using the address in the PC.
(iii) Memory Address Register (MAR)
********** 1 **********
--- page 2 ---
•   Function:
Holds the address in memory where data or instructions are to be fetched from or
written to.
(iv) Memory Data Register (MDR) (also called Memory Buffer Register – MBR)
•   Function:
Temporarily holds the data being transferred to or from memory.
CO3 b Compare RISC and CISC in terms of instruction set simplicity and pipeline performance.   5
,   Answer:
BT2
CO4   c What is a Superscalar Processor? How does it differ from a traditional scalar processor?   5
,   Answer: 2 marks
BT2   A Superscalar Processor is a type of CPU architecture that can execute more than one
instruction per clock cycle by using multiple execution units (such as ALUs, FPUs, etc.).
It can fetch, decode, and execute several instructions simultaneously, thereby improving
instruction throughput.
Difference between Scalar and Superscalar Processors 3 marks
CO4 d Distinguish between memory-mapped I/O and I/O-mapped I/O.   5
,
BT2
********** 2 **********
--- page 3 ---
Q2   a What is bus Arbitration. Explain in detail the various bus arbitration techniques..   10
CO1   Answer: 1 marks
,   ✓ who can use the Bus a specific time or More than one module controlling the bus
BT2   ✓ Bus Arbitration refers to the process by which the current bus master accesses and
then leaves the control of the bus and passes it to the another bus requesting
processor unit
✓ The controller that has access to a bus at an instance is known as Bus master
Methods of BUS Arbitration –There are three bus arbitration methods: (3marks for each)
✓ Daisy Chaining method –
✓   It is a centralized bus arbitration method.
✓   It is a simple and cheaper method where all the bus masters use the same line for
making bus requests.
✓ The bus grant signal serially propagates through each master until it encounters the
first one that is requesting access to the bus.
✓ This master blocks the propagation of the bus grant signal, therefore any other
requesting module will not receive the grant signal and hence cannot access the
bus.
(ii)Polling or Rotating Priority method
✓ In this, the controller is used to generate the address for the master(unique
priority), the number of address lines required depends on the number of masters
connected in the system.
✓ the priorities are dynamically changed to give every device an opportunity to access
the bus.
✓ The controller generates a sequence of master addresses.
********** 3 **********
--- page 4 ---
(iii) Fixed priority or Independent Request method
✓ In this, each master has a separate pair of bus request and bus grant lines and each
pair has a priority assigned to it.
✓ The built-in priority decoder within the controller selects the highest priority
request and asserts the corresponding bus grant signal.
CO2 b Set-Associative Mapping   10
,   A computer system with Set-Associative Mapping, has a main memory of 2 GB and a cache
BT3   of size 512 KB. The block size is 256 B and the cache uses 4-way set associative mapping.
1. Calculate the number of blocks in main memory.
2. Calculate the number of lines in cache.
3. How many sets are present in the cache?
4. Determine the number of tag bits.
Answer:
Main memory size = 2 GB = 2×230=2312 \times 2^{30} = 2^{31}2×230=231 bytes
Cache size = 512 KB = 512×210=219512 \times 2^{10} = 2^{19}512×210=219 bytes
Block size = 256 B = 282^828 bytes
Cache mapping = 4-way set associative
********** 4 **********
--- page 5 ---
Q3   a Describe the various elements involved in Bus Design in computer architecture. Explain   10
CO1   each element in detail.
,
Answer: Detail explanation of any 4(2.5 marks for each).
•   Bus Types:
• Method of Arbitration
•   Timing
•   Bus width
•   Data Transfer Type
•   Block Data Transfer
********** 5 **********
--- page 6 ---
CO2 b Convert the decimal number −25.25 into IEEE 754 single precision (32-bit) and double   10
,   precision floating point representation. Show all steps.
BT3   Answer:
2 marks for each step
Step 1: Determine the sign bit
• The number is negative, so:
Sing=1
Step 2: Convert the magnitude to binary
We ignore the sign and convert 25.25 to binary.
********** 6 **********
--- page 7 ---
IEEE 754 Single Precision: 1 10000011 10010100000000000000000
IEEE 754 Double Precision: 1 10000000011 100101000000000000000000000000000000000
0000000000000
Q4   a Explain in detail the different cache address mapping techniques with neat diagrams.   10
CO2
,   Answer: 1 marks for list
BT2   Cache memory is a small, fast memory located close to the CPU to reduce the average
memory access time.
When a CPU accesses memory, it checks the cache first. The mapping technique
determines how main memory blocks are placed in cache lines.
The main cache mapping techniques are:
(3marks for each: explanation with diagram/ example)
1. Direct Mapping
2. Associative Mapping
3. Set-Associative Mapping
CO2 b With neat block diagram, explain the design and working of a 4-bit serial adder. Show how   10
,   two 4-bit binary numbers can be added using shift registers and a full adder.
BT2
Answer: explanation with diagram and example 10 Marks
A 4-bit serial adder is a digital circuit used to add two 4-bit binary numbers bit by bit in a
serial manner.
********** 7 **********
--- page 8 ---
Q5   a Discuss the various parameters and characteristics that influence the design and   10
CO2   performance of memory systems in computers.
,
BT2   Answer: explanation of any 5(2 marks for each)
1.Location: The computer memory is placed in three different locations:
a. CPU: It is in the form of CPU registers and its internal cache memory
(16K bytes in case of Pentium)
b. Internal: It is in the main memory of the system which CPU can   access directly
c. External : It is in the form of secondary storage devices such as
magnetic disk, tapes, etc. The CPU accesses this memory with the help of I/O controllers
2. Capacity: It is expressed using two terms: Word size and number of words.
a. Word size:-It is expressed in bytes (8- it).The common word sizes are 8,16 and 32bits.
********** 8 **********
--- page 9 ---
b. Number of word:-This term specifies the number of words available in the particular
memory device. e.g. If memory capacity is 4K X 8 , then its word size is 8 and number of
words are 4K=4096.
3. Unit of Transfer: It is the maximum number of bits that can be read or written into the
memory at a time
In case of main memory, most of the times it is equal to word size
In case of external memory, unit of transfer is not limited to word size, it is often larger
than a word and it is referred to as blocks
4. Access Method: There are two different method generally used for memory access a
Sequential access: Here, memory is organized into units of data, called records . If current
record is 1 then in order to read record N, it is necessary to read physical records 1 through
N -1. A tape drive is an example of sequential access memory
Random access: Here, each addressable location in memory has an unique address It is
possible to access any memory location at random
Others are direct access and Associate access.
5. Performance: The performance of the memory system is determined using three
parameters
I. Access time: In case of random access memory, it is the time taken by memory to
complete read/ write operation from the instant that an address
is sent to the memory.
On the other hand, for non-random access memory, access time is the time it takes to
position the read /write mechanism at the desired location
II. Memory cycle time: This term is used only with random access memory and it is defined
as access time plus additional time required before a second access can commence
III. Transfer rate It is defined as the rate at which data can be transferred into or out of a
memory unit
6.Physical Type: Two most common physical types used today are semi conductor memory
and magnetic surface memory.
Physical characteristics:-
a. Volatile/Non-volatile: If memory can hold data even if power is turned off, it is called as
non volatile memory; otherwise it is called as volatile memory.
b. Erasable/Nonerasable: The memories in which data is once programmed cannot be
erased are called as non erasable memories. On the other hand, if data in the memory is
erasable then memory is called as erasable memory.
CO2 b Explain the Modified Booth’s Algorithm for multiplication of signed binary numbers.   10
,   Illustrate your explanation with a suitable example.
BT3
Answer:
Booth’s Algorithm is a technique for multiplying signed binary numbers efficiently.
It handles both positive and negative numbers using two’s complement representation.
Algorithm: 4 marks
Example: 6 marks
Q6   a With a neat diagram, explain the CPU register organization and elaborate on the function   10
CO3   of Accumulator, PC, Status Register, and Stack Pointer.
,   Answer: diagram 2 marks, function of each 8 marks
BT2
********** 9 **********
--- page 10 ---
i) Accumulator (ACC)
•   Purpose: Holds operands and results of arithmetic and logic operations.
• Works closely with the ALU.
ii) Program Counter (PC)
•   Purpose: Stores the address of the next instruction to be fetched from memory.
•   Automatically increments after each fetch unless a branch or jump instruction
occurs.
iii) Status Register (SR) / Flag Register
•   Purpose: Holds status flags set by ALU operations.
• Common flags include:
o Zero (Z): Result is zero
o Carry (C): Carry out occurred
o Sign (S): Result is negative
iv) Stack Pointer (SP)
•   Purpose: Points to the top of the stack in memory.
•   Stack is used for:
o   Storing return addresses during subroutine calls
o Temporary storage of data and registers
CO4 b Describe the architecture and operation of a Microprogrammed Control Unit with the help   10
,   of a block diagram.
BT2   Answer:
•   In computer central processing units, micro-operations (also known as micro-ops)
are the functional or atomic, operations of a processor.
•   These are low level instructions used in some designs to implement complex
machine instructions, also known as macro instruction.
********** 10 **********
--- page 11 ---
Diagram: 3 marks
Explanation: 7 marks
Q7   a Compare Programmed I/O, Interrupt-driven I/O, and DMA techniques in terms of CPU   10
CO4   involvement and efficiency.
,
BT2   Answer: each comparison 2 marks
DMA (Direct Memory
Feature   Programmed I/O   Interrupt-driven I/O
Access)
CPU executes other   CPU initiates DMA
CPU continuously
CPU   instructions; device   transfer; DMA controller
polls the I/O device
Involvement   interrupts CPU when handles data transfer
until it’s ready.
ready.   directly.
Low; CPU is busy   Higher; CPU does   Very high; CPU is free
Efficiency   waiting and cannot   useful work while   during transfer, only
perform other tasks.   waiting for I/O.   interrupted at start/end.
Fastest; data moves
Slow; dependent on
Faster than programmed directly between memory
Speed   CPU polling
I/O; less CPU idle time. and I/O without CPU
frequency.
intervention.
Hardware   Simple; no extra   Moderate; requires   Complex; requires DMA
Complexity   hardware required.   interrupt controller.   controller.
Medium-speed devices High-speed devices (e.g.,
Simple, low-speed
Best Use   where CPU can do other disk, graphics, network)
devices.
work.   with large data transfers.
Moderate; CPU   Low; CPU only sets up
CPU   High; constantly
responds only when   DMA and continues other
Overhead   checks device status.
interrupted.   tasks.
CO1 b   i.   Define Cache memory. Why is it organized in multiple levels (L1, L2, L3)?   5
,   Answer:
BT2   Define: 2 marks
CO3   Cache memory is a small, high-speed memory placed between the CPU and main memory.
,   •   It stores frequently used instructions and data to reduce the average memory
BT2   access time.
********** 11 **********
--- page 12 ---
•   Acts as a buffer between slow main memory and fast CPU.
Modern CPUs use multi-level cache to balance speed, size, and cost: (purpose of each level
3 marks)
ii.   Explain the Pipelined Processor Architecture with a
Answer: explanation 3 marks, diagram-2 marks
•   Usually pipeline processor consists of a sequence of m data-processing circuits,
called elements, stages or segments.
•   These stages collectively perform a single operation on a stream of data operands   5
passing through them.
• The processing is done part by part in each stage, but the final result is obtained
only after an operand set has passed through the entire pipeline.
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 69c79323e495

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CSBS_7036/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)/B. Tech (AI & ML)/B. Tech (CSBS)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 09 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions..
6. Assume Suitable data if necessary.
Q.n   Question   Mark
o.   s
1
CO1 a Explain the role of Registers in CPU operation. Mention any four types of registers and their 5
,   functions.
BT3
Answer:
Registers are small, high-speed storage locations inside the Central Processing Unit (CPU).
They are used to store data, instructions, addresses, and intermediate results temporarily
during program execution.
Role of Registers in CPU Operation: 1 marks
Registers play a crucial role in every step of instruction execution. Their main roles include:
1. Holding Instructions and Data:
2. Storing Addresses:
3. Temporary Storage for Arithmetic/Logic Operations:
4. Instruction Control and Sequencing:
(i) Program Counter (PC) 1 mark for explanation of each
•   Function:
Holds the address of the next instruction to be fetched from memory for
execution.
After fetching an instruction, the PC is automatically incremented to point to the
next one.
(ii) Instruction Register (IR)
•   Function:
Stores the current instruction that has been fetched from memory and is being
decoded and executed.
•   Process:
o CPU fetches the instruction from memory using the address in the PC.
(iii) Memory Address Register (MAR)
********** 1 **********
--- page 2 ---
•   Function:
Holds the address in memory where data or instructions are to be fetched from or
written to.
(iv) Memory Data Register (MDR) (also called Memory Buffer Register – MBR)
•   Function:
Temporarily holds the data being transferred to or from memory.
CO3 b Compare RISC and CISC in terms of instruction set simplicity and pipeline performance.   5
,   Answer:
BT2
CO4   c What is a Superscalar Processor? How does it differ from a traditional scalar processor?   5
,   Answer: 2 marks
BT2   A Superscalar Processor is a type of CPU architecture that can execute more than one
instruction per clock cycle by using multiple execution units (such as ALUs, FPUs, etc.).
It can fetch, decode, and execute several instructions simultaneously, thereby improving
instruction throughput.
Difference between Scalar and Superscalar Processors 3 marks
CO4 d Distinguish between memory-mapped I/O and I/O-mapped I/O.   5
,
BT2
********** 2 **********
--- page 3 ---
Q2   a What is bus Arbitration. Explain in detail the various bus arbitration techniques..   10
CO1   Answer: 1 marks
,   ✓ who can use the Bus a specific time or More than one module controlling the bus
BT2   ✓ Bus Arbitration refers to the process by which the current bus master accesses and
then leaves the control of the bus and passes it to the another bus requesting
processor unit
✓ The controller that has access to a bus at an instance is known as Bus master
Methods of BUS Arbitration –There are three bus arbitration methods: (3marks for each)
✓ Daisy Chaining method –
✓   It is a centralized bus arbitration method.
✓   It is a simple and cheaper method where all the bus masters use the same line for
making bus requests.
✓ The bus grant signal serially propagates through each master until it encounters the
first one that is requesting access to the bus.
✓ This master blocks the propagation of the bus grant signal, therefore any other
requesting module will not receive the grant signal and hence cannot access the
bus.
(ii)Polling or Rotating Priority method
✓ In this, the controller is used to generate the address for the master(unique
priority), the number of address lines required depends on the number of masters
connected in the system.
✓ the priorities are dynamically changed to give every device an opportunity to access
the bus.
✓ The controller generates a sequence of master addresses.
********** 3 **********
--- page 4 ---
(iii) Fixed priority or Independent Request method
✓ In this, each master has a separate pair of bus request and bus grant lines and each
pair has a priority assigned to it.
✓ The built-in priority decoder within the controller selects the highest priority
request and asserts the corresponding bus grant signal.
CO2 b Set-Associative Mapping   10
,   A computer system with Set-Associative Mapping, has a main memory of 2 GB and a cache
BT3   of size 512 KB. The block size is 256 B and the cache uses 4-way set associative mapping.
1. Calculate the number of blocks in main memory.
2. Calculate the number of lines in cache.
3. How many sets are present in the cache?
4. Determine the number of tag bits.
Answer:
Main memory size = 2 GB = 2×230=2312 \times 2^{30} = 2^{31}2×230=231 bytes
Cache size = 512 KB = 512×210=219512 \times 2^{10} = 2^{19}512×210=219 bytes
Block size = 256 B = 282^828 bytes
Cache mapping = 4-way set associative
********** 4 **********
--- page 5 ---
Q3   a Describe the various elements involved in Bus Design in computer architecture. Explain   10
CO1   each element in detail.
,
Answer: Detail explanation of any 4(2.5 marks for each).
•   Bus Types:
• Method of Arbitration
•   Timing
•   Bus width
•   Data Transfer Type
•   Block Data Transfer
********** 5 **********
--- page 6 ---
CO2 b Convert the decimal number −25.25 into IEEE 754 single precision (32-bit) and double   10
,   precision floating point representation. Show all steps.
BT3   Answer:
2 marks for each step
Step 1: Determine the sign bit
• The number is negative, so:
Sing=1
Step 2: Convert the magnitude to binary
We ignore the sign and convert 25.25 to binary.
********** 6 **********
--- page 7 ---
IEEE 754 Single Precision: 1 10000011 10010100000000000000000
IEEE 754 Double Precision: 1 10000000011 100101000000000000000000000000000000000
0000000000000
Q4   a Explain in detail the different cache address mapping techniques with neat diagrams.   10
CO2
,   Answer: 1 marks for list
BT2   Cache memory is a small, fast memory located close to the CPU to reduce the average
memory access time.
When a CPU accesses memory, it checks the cache first. The mapping technique
determines how main memory blocks are placed in cache lines.
The main cache mapping techniques are:
(3marks for each: explanation with diagram/ example)
1. Direct Mapping
2. Associative Mapping
3. Set-Associative Mapping
CO2 b With neat block diagram, explain the design and working of a 4-bit serial adder. Show how   10
,   two 4-bit binary numbers can be added using shift registers and a full adder.
BT2
Answer: explanation with diagram and example 10 Marks
A 4-bit serial adder is a digital circuit used to add two 4-bit binary numbers bit by bit in a
serial manner.
********** 7 **********
--- page 8 ---
Q5   a Discuss the various parameters and characteristics that influence the design and   10
CO2   performance of memory systems in computers.
,
BT2   Answer: explanation of any 5(2 marks for each)
1.Location: The computer memory is placed in three different locations:
a. CPU: It is in the form of CPU registers and its internal cache memory
(16K bytes in case of Pentium)
b. Internal: It is in the main memory of the system which CPU can   access directly
c. External : It is in the form of secondary storage devices such as
magnetic disk, tapes, etc. The CPU accesses this memory with the help of I/O controllers
2. Capacity: It is expressed using two terms: Word size and number of words.
a. Word size:-It is expressed in bytes (8- it).The common word sizes are 8,16 and 32bits.
********** 8 **********
--- page 9 ---
b. Number of word:-This term specifies the number of words available in the particular
memory device. e.g. If memory capacity is 4K X 8 , then its word size is 8 and number of
words are 4K=4096.
3. Unit of Transfer: It is the maximum number of bits that can be read or written into the
memory at a time
In case of main memory, most of the times it is equal to word size
In case of external memory, unit of transfer is not limited to word size, it is often larger
than a word and it is referred to as blocks
4. Access Method: There are two different method generally used for memory access a
Sequential access: Here, memory is organized into units of data, called records . If current
record is 1 then in order to read record N, it is necessary to read physical records 1 through
N -1. A tape drive is an example of sequential access memory
Random access: Here, each addressable location in memory has an unique address It is
possible to access any memory location at random
Others are direct access and Associate access.
5. Performance: The performance of the memory system is determined using three
parameters
I. Access time: In case of random access memory, it is the time taken by memory to
complete read/ write operation from the instant that an address
is sent to the memory.
On the other hand, for non-random access memory, access time is the time it takes to
position the read /write mechanism at the desired location
II. Memory cycle time: This term is used only with random access memory and it is defined
as access time plus additional time required before a second access can commence
III. Transfer rate It is defined as the rate at which data can be transferred into or out of a
memory unit
6.Physical Type: Two most common physical types used today are semi conductor memory
and magnetic surface memory.
Physical characteristics:-
a. Volatile/Non-volatile: If memory can hold data even if power is turned off, it is called as
non volatile memory; otherwise it is called as volatile memory.
b. Erasable/Nonerasable: The memories in which data is once programmed cannot be
erased are called as non erasable memories. On the other hand, if data in the memory is
erasable then memory is called as erasable memory.
CO2 b Explain the Modified Booth’s Algorithm for multiplication of signed binary numbers.   10
,   Illustrate your explanation with a suitable example.
BT3
Answer:
Booth’s Algorithm is a technique for multiplying signed binary numbers efficiently.
It handles both positive and negative numbers using two’s complement representation.
Algorithm: 4 marks
Example: 6 marks
Q6   a With a neat diagram, explain the CPU register organization and elaborate on the function   10
CO3   of Accumulator, PC, Status Register, and Stack Pointer.
,   Answer: diagram 2 marks, function of each 8 marks
BT2
********** 9 **********
--- page 10 ---
i) Accumulator (ACC)
•   Purpose: Holds operands and results of arithmetic and logic operations.
• Works closely with the ALU.
ii) Program Counter (PC)
•   Purpose: Stores the address of the next instruction to be fetched from memory.
•   Automatically increments after each fetch unless a branch or jump instruction
occurs.
iii) Status Register (SR) / Flag Register
•   Purpose: Holds status flags set by ALU operations.
• Common flags include:
o Zero (Z): Result is zero
o Carry (C): Carry out occurred
o Sign (S): Result is negative
iv) Stack Pointer (SP)
•   Purpose: Points to the top of the stack in memory.
•   Stack is used for:
o   Storing return addresses during subroutine calls
o Temporary storage of data and registers
CO4 b Describe the architecture and operation of a Microprogrammed Control Unit with the help   10
,   of a block diagram.
BT2   Answer:
•   In computer central processing units, micro-operations (also known as micro-ops)
are the functional or atomic, operations of a processor.
•   These are low level instructions used in some designs to implement complex
machine instructions, also known as macro instruction.
********** 10 **********
--- page 11 ---
Diagram: 3 marks
Explanation: 7 marks
Q7   a Compare Programmed I/O, Interrupt-driven I/O, and DMA techniques in terms of CPU   10
CO4   involvement and efficiency.
,
BT2   Answer: each comparison 2 marks
DMA (Direct Memory
Feature   Programmed I/O   Interrupt-driven I/O
Access)
CPU executes other   CPU initiates DMA
CPU continuously
CPU   instructions; device   transfer; DMA controller
polls the I/O device
Involvement   interrupts CPU when handles data transfer
until it’s ready.
ready.   directly.
Low; CPU is busy   Higher; CPU does   Very high; CPU is free
Efficiency   waiting and cannot   useful work while   during transfer, only
perform other tasks.   waiting for I/O.   interrupted at start/end.
Fastest; data moves
Slow; dependent on
Faster than programmed directly between memory
Speed   CPU polling
I/O; less CPU idle time. and I/O without CPU
frequency.
intervention.
Hardware   Simple; no extra   Moderate; requires   Complex; requires DMA
Complexity   hardware required.   interrupt controller.   controller.
Medium-speed devices High-speed devices (e.g.,
Simple, low-speed
Best Use   where CPU can do other disk, graphics, network)
devices.
work.   with large data transfers.
Moderate; CPU   Low; CPU only sets up
CPU   High; constantly
responds only when   DMA and continues other
Overhead   checks device status.
interrupted.   tasks.
CO1 b   i.   Define Cache memory. Why is it organized in multiple levels (L1, L2, L3)?   5
,   Answer:
BT2   Define: 2 marks
CO3   Cache memory is a small, high-speed memory placed between the CPU and main memory.
,   •   It stores frequently used instructions and data to reduce the average memory
BT2   access time.
********** 11 **********
--- page 12 ---
•   Acts as a buffer between slow main memory and fast CPU.
Modern CPUs use multi-level cache to balance speed, size, and cost: (purpose of each level
3 marks)
ii.   Explain the Pipelined Processor Architecture with a
Answer: explanation 3 marks, diagram-2 marks
•   Usually pipeline processor consists of a sequence of m data-processing circuits,
called elements, stages or segments.
•   These stages collectively perform a single operation on a stream of data operands   5
passing through them.
• The processing is done part by part in each stage, but the final result is obtained
only after an operand set has passed through the entire pipeline.
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 7fa71088df5f

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_Computer_7002/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Text: none (FileDataError: Failed to open stream)

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper e998b7b85019

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_IT_7001/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B.
Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 30 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. Assume Suitable data if necessary
Q.no   Questions   Mark
.   s
Q1
CO1, a Explain the general organization of a computer system and describe the interaction   5
BT2   between its major components
Ans:
[Diagram :2 Marks]
Major Components of a Computer System [2 marks]
1. Input Unit
Accepts data and instructions from the user
Converts them into machine-readable form
Example: Keyboard, mouse
2. Memory Unit
Stores data, instructions, and intermediate results
Types:
Primary memory (RAM, ROM)
Secondary memory (hard disk, SSD)
3. Central Processing Unit (CPU)
********** 1 **********
--- page 2 ---
• Arithmetic Logic Unit (ALU)
Performs arithmetic operations (addition, subtraction, etc.)
Performs logical operations (AND, OR, NOT)
• Control Unit (CU)
Controls and coordinates all operations
Fetches, decodes, and executes instructions
• Registers
High-speed storage inside CPU
Stores temporary data and instructions
4. Output Unit
Converts processed data into human-readable form
Example: Monitor, printer
Interaction Between Components [1marks]
CO3, b What is an instruction format? Illustrate an instruction format with examples.   5
BT2   Ans:
Definition 2marks
Diagram with explanation with Example 3marks
Def: The instruction format defines the layout and structure of the program instruction
that can be decoded by the CPU and then perform the desired operation on the data.
CO4, c Discuss any 5 applications of GPU.   5
BT2   Ans:
Each 1 marks
Ans.
A GPU (Graphics Processing Unit) is a specialized processor designed to handle
parallel processing, making it useful in many high-performance applications
beyond graphics.
1. Graphics Rendering
GPUs are mainly used for rendering images, videos, and animations in
computers, games, and multimedia applications.
👉 Example: 3D games, video editing, animation movies.
2. Machine Learning and AI
GPUs accelerate deep learning and neural network training due to their ability
to process large data in parallel.
👉 Example: Image recognition, speech processing, chatbots.
********** 2 **********
--- page 3 ---
3. Scientific Computing
Used in simulations and complex calculations in fields like physics, chemistry, and
engineering.
👉 Example: Weather forecasting, molecular modeling.
4. Data Processing and Big Data
GPUs help in fast processing of large datasets using parallel computing.
👉 Example: Data analytics, real-time data processing.
5. Cryptocurrency Mining
GPUs are widely used for solving complex mathematical problems required in
cryptocurrency mining.
👉 Example: Bitcoin, Ethereum mining.
CO4, d A system executes the same instruction on multiple data elements simultaneously.   5
BT4   Identify the appropriate Flynn’s classification and justify your answer with a
practical example.
Ans:
Marks Bifurcation
Identification: 2 Marks
Explanation with Example: 3 Marks
Answer-
The given system represents SIMD (Single Instruction Multiple Data) architecture.
In SIMD, a single instruction is executed simultaneously on multiple data
elements. This is useful when the same operation needs to be repeated on large
datasets. The system uses multiple processing units that perform identical
operations in parallel.
Example: Image processing where the same filter is applied to all pixels, or GPU
operations in graphics rendering.
Q2   a Sketch the diagram to elaborate interrupt handling process. Write the advantages   10
CO1,   and disadvantages of interrupt.
BT2   Ans:
********** 3 **********
--- page 4 ---
Diagram = 2 marks
Explanation= 4 marks
Advantages = 2 marks
Disadvantages= 2 marks
Steps Involved (Explanation):
1. Interrupt Request
o I/O device sends an interrupt signal to CPU
2. Interrupt Acknowledgment
o CPU completes current instruction
o Acknowledges the interrupt
3. Context Saving
o CPU saves the current state (PC, registers)
4. ISR Execution
o Control transfers to Interrupt Service Routine (ISR)
o Required service is performed
5. Context Restoration
o Saved state is restored
6. Resume Execution
o CPU continues execution of main program
Advantages:
•   Efficient use of CPU time.
•   Facilitates real-time processing.
•   Reduces polling overhead.
Disadvantages:
• Adds complexity to system design.
•   Frequent interrupts can reduce overall performance.
CO2, b Consider a computer system with the following cache specifications:   10
BT3   • Cache size = 32 KB
• Block size = 128 bytes
• Mapping technique = Fully Associative
• Main memory size = 1 MB
Assume byte-addressable memory.
Divide the main memory address into Tag and Block Offset fields and specify the
number of bits in each. Also, calculate the number of cache blocks.
Ans: [2.5 marks for each step\
Step 1: Calculate Address Size
Main memory = 2^20 bytes
Address bits = 20 bits
Step 2: Block Offset Bits
Block size = 2^7 bytes
Block offset = 7 bits
Step 3: Tag Bits
In fully associative mapping:
********** 4 **********
--- page 5 ---
• No index field
• Address = Tag + Block Offset
Tag bits=20−7=13 bits
Step 4: Number of Cache Blocks
Address Format
Tag (13 bits)   Block Offset (7 bits)
Q3   a Name the various phases involved in execution of an instruction and explain   10
CO1,   opcode fetch decode cycle in detail.
BT2   Ans:
Fetch instruction from memory.   [2 marks]
Decode the instruction.
Read the effective address from memory.
Execute the instruction.
Fetch Cycle:   [4 marks]
• The address of the next instruction to execute is in the Program Counter (PC) at
the beginning of the fetch cycle.
• The address in the program counter is transferred to the Memory Address
Register(MAR), as this is the only register that is connected to the system bus
address lines.The address in MAR is put on the address bus, now a Read order is
provided by the control unit on the control bus, and the result appears on the data
bus and is then copied into the memory buffer register.
• The program counter is incremented by one, to get ready for the next instruction.
These two acts can be carried out concurrently to save time.
• The content of the MBR is moved to the instruction register (IR). The instruction
fetch cycle consists of four micro-operations:
Decode instruction Cycle: [4 marks]
• The next move is to fetch source operands once an instruction is fetched.
•   Indirect addressing (it can be obtained by any addressing mode, here it is done
by indirect addressing) is obtained by Source Operand.
• The instruction address field is passed to the MAR. This is used to fetch the
operand 's address.
• The address field of the IR is updated from the MBR
• The IR is now in the state. Now IR is ready for the execute cycle
CO2, b Explain the IEEE 754 single precision floating-point format. Convert the decimal   10
BT3   number –47.375 to IEEE 754 single precision format. Show all steps.
Ans: [Each Step 2 marks]
Step 1 — Sign bit
Number is negative → Sign bit = 1
Step 2 — Convert 47.375 to binary
47 = 101111
0.375 × 2 = 0.75 → 0
********** 5 **********
--- page 6 ---
0.75 × 2 = 1.50 → 1
0.50 × 2 = 1.00 → 1
0.375 = 0.011
47.375 = 101111.011
Step 3 — Normalize
101111.011 = 1.01111011 × 25
Step 4 — Biased exponent (bias = 127)
5 + 127 = 132 = 10000100
Step 5 — Mantissa (drop leading 1, pad to 23 bits)
01111011000000000000000
Final 32-bit representation:
Sign   Exponent (8)   Mantissa (23)
(1)
1   10000100   01111011000000000000000
Q4   a Explain all the components of memory hierarchy with a neat diagram. Highlight   10
CO2,   its important parameters.
BT2
Ans:
Memory Hierarchy Design
1. Registers
Registers are small, high-speed memory units located in the CPU. They are used to
store the most frequently used data and instructions. Registers have the fastest
access time and the smallest storage capacity, typically ranging from 16 to 64 bits.
2. Cache Memory
Cache memory is a small, fast memory unit located close to the CPU. It stores
frequently used data and instructions that have been recently accessed from the
main memory. Cache memory is designed to minimize the time it takes to access
data by providing the CPU with quick access to frequently used data
3. Main Memory
Main memory, also known as RAM (Random Access Memory), is the primary
memory of a computer system. It has a larger storage capacity than cache memory,
but it is slower. Main memory is used to store data and instructions that are
currently in use by the CPU.
Types of Main Memory
Static RAM: Static RAM stores the binary information in flip flops and
information remains valid until power is supplied. Static RAM has a faster access
time and is used in implementing cache memory.
Dynamic RAM: It stores the binary information as a charge on the capacitor. It
requires refreshing circuitry to maintain the charge on the capacitors after a few
milliseconds. It contains more memory cells per unit area as compared to SRAM.
4. Secondary Storage
Secondary storage, such as hard disk drives (HDD) and solid-state drives (SSD) ,
is a non-volatile memory unit that has a larger storage capacity than main memory.
It is used to store data and instructions that are not currently in use by the CPU.
Secondary storage has the slowest access time and is typically the least expensive
type of memory in the memory hierarchy.
5. Magnetic Disk
Magnetic Disks are simply circular plates that are fabricated with either a metal or
a plastic or a magnetized material. The Magnetic disks work at a high speed inside
the computer and these are frequently used.
6. Magnetic Tape
********** 6 **********
--- page 7 ---
Magnetic Tape is simply a magnetic recording device that is covered with a plastic
film. Magnetic Tape is generally used for the backup of data. In the case of a
magnetic tape, the access time for a computer is a little slower and therefore, it
requires some amount of time for accessing the strip. 5 Marks
1 Marks
Characteristics/ parameters of Memory Hierarchy
Capacity: It is the global volume of information the memory can store. As we
move from top to bottom in the Hierarchy, the capacity increases.
Access Time: It is the time interval between the read/write request and the
availability of the data. As we move from top to bottom in the Hierarchy, the
access time increases.
Performance: The Memory Hierarch design ensures that frequently accessed data
is stored in faster memory to improve system performance.
Cost Per Bit: As we move from bottom to top in the Hierarchy, the cost per bit
increases i.e. Internal Memory is costlier than External Memory. 4Marks
CO2, b Describe the internal architecture of the 8087 NDP. Explain how it enhances the   10
BT2   performance of the 8086 system in handling arithmetic operations.
Ans:
The 8087 NDP is a coprocessor designed to work with the 8086/8088
microprocessor to perform high-speed arithmetic and floating-point operations.
********** 7 **********
--- page 8 ---
Diagram =3marks
1. Control Unit   [Explanation 5 marks]
• Coordinates operations
• Synchronizes with 8086
2. Instruction Decoder
• Decodes ESC (escape) instructions from 8086
•   Identifies instructions meant for 8087
3. Floating Point Unit (FPU)
• Performs:
o Addition, subtraction
o Multiplication, division
o Square root, trigonometric functions
4. Register Stack (8 × 80-bit)
• Organized as stack (ST0–ST7)
•   Stores intermediate results
• High precision (80-bit format)
5. Data Bus Interface
• Communicates with memory and CPU
• Fetches operands and stores results
Performance Enhancement: [2marks]
Parallel Processing
• 8086 and 8087 operate simultaneously
• Improves throughput
✔ Faster Arithmetic Operations
********** 8 **********
--- page 9 ---
• Hardware-based floating-point operations
• Much faster than software implementation
✔ High Precision
•   80-bit internal registers
• Accurate scientific calculations
✔ Reduced CPU Load
• Complex calculations handled by 8087
• CPU free for other tasks
Q5   a Identify and explain any five characteristics of memory. Further, analyze how   10
CO2,   these characteristics affect the performance and design of a computer system.
BT 3
2 marks for each (any 5)
CO2, b Sketch the flowchart of Booth's Multiplication Algorithm and use Booth's   10
BT3   algorithm to multiply –6 and 5.
********** 9 **********
--- page 10 ---
Ans: Algo=4Marks
Solve=6marks
Q6   a Define RISC and CISC processors. Differentiate between them with suitable   10
CO3,   points.
BT2
********** 10 **********
--- page 11 ---
Ans:
RISC Definition 1m
CISC Definition 1m
Comparison 1m per point
RISC (Reduced Instruction Set Computer): a CPU architecture with a small, simple, and
regular set of instructions designed to execute quickly and be efficiently pipelined.
CISC (Complex Instruction Set Computer): a CPU architecture with a large set of
variable-length instructions that can perform complex tasks in fewer program
instructions but often require more complex decoding and multiple cycles.
CO4, b Describe the hardwired control unit with a neat block diagram. Explain its working   10
BT2   and discuss its main characteristics.
Ans:
Marks distribution: Describing hardwired control unit 5 marks
Block diagram with explanation 5 marks
• The control hardware can be viewed as a state machine that changes from one
state to another in every clock cycle, depending on the contents of the instruction
register, the condition codes, and the external inputs.
• The outputs of the state machine are the control signals. The sequence of the
operation carried out by this machine is determined by the wiring of the logic
elements and hence named “hardwired”.
•   Fixed logic circuits that correspond directly to the Boolean expressions are used
to generate the control signals. • Hardwired control is faster than micro-
programmed control.
• A controller that uses this approach can operate at high speed.
• RISC architecture is based on the hardwired control unit
Characteristics:
• A Hard wired Control consists of two decoders, a sequence counter, and a
number of logic gates
• An instruction fetched from the memory unit is placed in the instruction
register (IR)
• The component of an instruction register includes I bit, the operation code, and
bits 0 through 11
• The operation code in bits 12 through 14 are coded with a 3 x 8 decoder
• The outputs of the decoder are designated by the symbols D 0 through D 7
********** 11 **********
--- page 12 ---
• The operation code at bit 15 is transferred to a flip flop designated by the
symbol I
• The operation codes from Bits 0 through 11 are applied to the control logic
gates
• The Sequence counter (SC) can count in binary from 0 through 15
Q7   a With the help of a neat diagram, explain the DMA controller and its operation.   10
CO4,   Compare DMA with interrupt-driven I/O.
BT2
Ans: [Diagram 2 marks]
Steps: [Explanation 4 marks]
1. Initialization
o CPU provides starting address, data size, and direction to DMA
2. DMA Request
o I/O device sends request (DRQ)
3. Bus Request
o DMA requests control of system bus from CPU
4. Bus Grant
o CPU grants bus and suspends its operation
5. Data Transfer
o DMA transfers data directly:
▪ Memory ↔ I/O device
6. Completion
********** 12 **********
--- page 13 ---
o DMA interrupts CPU after transfer completion
Comparison: 4Marks
CO1, b   i.   Explain the functions of the Bus Interface Unit (BIU) and the Execution   5
BT2   Unit (EU) in the 8086 microprocessors during instruction fetching and
execution. Why is the processor divided into these two units?
Ans:
Functions of BIU (Bus Interface Unit)   [2marks]
CO1,   • Fetches instructions from memory
BT2   • Handles address generation using segment registers   5
• Maintains instruction queue (6 bytes) for prefetching
•   Transfers data between CPU, memory, and I/O
Functions of EU (Execution Unit)   [2marks]
• Decodes and executes instructions
• Performs arithmetic and logical operations (ALU)
• Uses registers for computation
• Takes instructions from the instruction queue
During Instruction Execution
• BIU fetches instructions and stores them in queue
• EU takes instructions from queue and executes them
• Both units work simultaneously
Why Division into BIU and EU?   [1 marks]
✔ Enables pipelining (parallelism)
✔ Improves execution speed
✔ Reduces CPU idle time
✔ Increases overall efficiency
ii.   Explain the stored program concept and its significance in modern
computer systems.
Ans: [Explanation: 3marks]
The stored program concept is a fundamental idea in computer architecture
introduced by John von Neumann. It means that a computer’s instructions
(program) and data are stored together in the same memory.
Explanation
In this concept:
• A program is stored in the computer’s memory just like data.
********** 13 **********
--- page 14 ---
• The CPU fetches instructions one by one from memory, decodes them, and
executes them.
• This is known as the fetch–decode–execute cycle.
Earlier machines required manual rewiring to change programs, but with this
concept, programs can be changed simply by loading new instructions into
memory.
Significance in Modern Computer Systems [2 marks]
1. Flexibility
Computers can perform different tasks by loading different programs
without changing hardware.
2. Ease of Programming
Programmers can write, modify, and store programs easily in memory.
3. Foundation of Modern Architecture
It forms the basis of the Von Neumann Architecture, used in most
computers today.
4. Efficient Execution
Automatic execution of instructions improves speed and efficiency.
5. Supports Advanced Features
Enables multitasking, operating systems, and complex applications.
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 66a0f9885ee2

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_Computer_7047/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B.
Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 30 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. Assume Suitable data if necessary
Q.no   Questions   Mark
.   s
Q1
CO1, a Explain the general organization of a computer system and describe the interaction   5
BT2   between its major components
Ans:
[Diagram :2 Marks]
Major Components of a Computer System [2 marks]
1. Input Unit
Accepts data and instructions from the user
Converts them into machine-readable form
Example: Keyboard, mouse
2. Memory Unit
Stores data, instructions, and intermediate results
Types:
Primary memory (RAM, ROM)
Secondary memory (hard disk, SSD)
3. Central Processing Unit (CPU)
********** 1 **********
--- page 2 ---
• Arithmetic Logic Unit (ALU)
Performs arithmetic operations (addition, subtraction, etc.)
Performs logical operations (AND, OR, NOT)
• Control Unit (CU)
Controls and coordinates all operations
Fetches, decodes, and executes instructions
• Registers
High-speed storage inside CPU
Stores temporary data and instructions
4. Output Unit
Converts processed data into human-readable form
Example: Monitor, printer
Interaction Between Components [1marks]
CO3, b What is an instruction format? Illustrate an instruction format with examples.   5
BT2   Ans:
Definition 2marks
Diagram with explanation with Example 3marks
Def: The instruction format defines the layout and structure of the program instruction
that can be decoded by the CPU and then perform the desired operation on the data.
CO4, c Discuss any 5 applications of GPU.   5
BT2   Ans:
Each 1 marks
Ans.
A GPU (Graphics Processing Unit) is a specialized processor designed to handle
parallel processing, making it useful in many high-performance applications
beyond graphics.
1. Graphics Rendering
GPUs are mainly used for rendering images, videos, and animations in
computers, games, and multimedia applications.
👉 Example: 3D games, video editing, animation movies.
2. Machine Learning and AI
GPUs accelerate deep learning and neural network training due to their ability
to process large data in parallel.
👉 Example: Image recognition, speech processing, chatbots.
********** 2 **********
--- page 3 ---
3. Scientific Computing
Used in simulations and complex calculations in fields like physics, chemistry, and
engineering.
👉 Example: Weather forecasting, molecular modeling.
4. Data Processing and Big Data
GPUs help in fast processing of large datasets using parallel computing.
👉 Example: Data analytics, real-time data processing.
5. Cryptocurrency Mining
GPUs are widely used for solving complex mathematical problems required in
cryptocurrency mining.
👉 Example: Bitcoin, Ethereum mining.
CO4, d A system executes the same instruction on multiple data elements simultaneously.   5
BT4   Identify the appropriate Flynn’s classification and justify your answer with a
practical example.
Ans:
Marks Bifurcation
Identification: 2 Marks
Explanation with Example: 3 Marks
Answer-
The given system represents SIMD (Single Instruction Multiple Data) architecture.
In SIMD, a single instruction is executed simultaneously on multiple data
elements. This is useful when the same operation needs to be repeated on large
datasets. The system uses multiple processing units that perform identical
operations in parallel.
Example: Image processing where the same filter is applied to all pixels, or GPU
operations in graphics rendering.
Q2   a Sketch the diagram to elaborate interrupt handling process. Write the advantages   10
CO1,   and disadvantages of interrupt.
BT2   Ans:
********** 3 **********
--- page 4 ---
Diagram = 2 marks
Explanation= 4 marks
Advantages = 2 marks
Disadvantages= 2 marks
Steps Involved (Explanation):
1. Interrupt Request
o I/O device sends an interrupt signal to CPU
2. Interrupt Acknowledgment
o CPU completes current instruction
o Acknowledges the interrupt
3. Context Saving
o CPU saves the current state (PC, registers)
4. ISR Execution
o Control transfers to Interrupt Service Routine (ISR)
o Required service is performed
5. Context Restoration
o Saved state is restored
6. Resume Execution
o CPU continues execution of main program
Advantages:
•   Efficient use of CPU time.
•   Facilitates real-time processing.
•   Reduces polling overhead.
Disadvantages:
• Adds complexity to system design.
•   Frequent interrupts can reduce overall performance.
CO2, b Consider a computer system with the following cache specifications:   10
BT3   • Cache size = 32 KB
• Block size = 128 bytes
• Mapping technique = Fully Associative
• Main memory size = 1 MB
Assume byte-addressable memory.
Divide the main memory address into Tag and Block Offset fields and specify the
number of bits in each. Also, calculate the number of cache blocks.
Ans: [2.5 marks for each step\
Step 1: Calculate Address Size
Main memory = 2^20 bytes
Address bits = 20 bits
Step 2: Block Offset Bits
Block size = 2^7 bytes
Block offset = 7 bits
Step 3: Tag Bits
In fully associative mapping:
********** 4 **********
--- page 5 ---
• No index field
• Address = Tag + Block Offset
Tag bits=20−7=13 bits
Step 4: Number of Cache Blocks
Address Format
Tag (13 bits)   Block Offset (7 bits)
Q3   a Name the various phases involved in execution of an instruction and explain   10
CO1,   opcode fetch decode cycle in detail.
BT2   Ans:
Fetch instruction from memory.   [2 marks]
Decode the instruction.
Read the effective address from memory.
Execute the instruction.
Fetch Cycle:   [4 marks]
• The address of the next instruction to execute is in the Program Counter (PC) at
the beginning of the fetch cycle.
• The address in the program counter is transferred to the Memory Address
Register(MAR), as this is the only register that is connected to the system bus
address lines.The address in MAR is put on the address bus, now a Read order is
provided by the control unit on the control bus, and the result appears on the data
bus and is then copied into the memory buffer register.
• The program counter is incremented by one, to get ready for the next instruction.
These two acts can be carried out concurrently to save time.
• The content of the MBR is moved to the instruction register (IR). The instruction
fetch cycle consists of four micro-operations:
Decode instruction Cycle: [4 marks]
• The next move is to fetch source operands once an instruction is fetched.
•   Indirect addressing (it can be obtained by any addressing mode, here it is done
by indirect addressing) is obtained by Source Operand.
• The instruction address field is passed to the MAR. This is used to fetch the
operand 's address.
• The address field of the IR is updated from the MBR
• The IR is now in the state. Now IR is ready for the execute cycle
CO2, b Explain the IEEE 754 single precision floating-point format. Convert the decimal   10
BT3   number –47.375 to IEEE 754 single precision format. Show all steps.
Ans: [Each Step 2 marks]
Step 1 — Sign bit
Number is negative → Sign bit = 1
Step 2 — Convert 47.375 to binary
47 = 101111
0.375 × 2 = 0.75 → 0
********** 5 **********
--- page 6 ---
0.75 × 2 = 1.50 → 1
0.50 × 2 = 1.00 → 1
0.375 = 0.011
47.375 = 101111.011
Step 3 — Normalize
101111.011 = 1.01111011 × 25
Step 4 — Biased exponent (bias = 127)
5 + 127 = 132 = 10000100
Step 5 — Mantissa (drop leading 1, pad to 23 bits)
01111011000000000000000
Final 32-bit representation:
Sign   Exponent (8)   Mantissa (23)
(1)
1   10000100   01111011000000000000000
Q4   a Explain all the components of memory hierarchy with a neat diagram. Highlight   10
CO2,   its important parameters.
BT2
Ans:
Memory Hierarchy Design
1. Registers
Registers are small, high-speed memory units located in the CPU. They are used to
store the most frequently used data and instructions. Registers have the fastest
access time and the smallest storage capacity, typically ranging from 16 to 64 bits.
2. Cache Memory
Cache memory is a small, fast memory unit located close to the CPU. It stores
frequently used data and instructions that have been recently accessed from the
main memory. Cache memory is designed to minimize the time it takes to access
data by providing the CPU with quick access to frequently used data
3. Main Memory
Main memory, also known as RAM (Random Access Memory), is the primary
memory of a computer system. It has a larger storage capacity than cache memory,
but it is slower. Main memory is used to store data and instructions that are
currently in use by the CPU.
Types of Main Memory
Static RAM: Static RAM stores the binary information in flip flops and
information remains valid until power is supplied. Static RAM has a faster access
time and is used in implementing cache memory.
Dynamic RAM: It stores the binary information as a charge on the capacitor. It
requires refreshing circuitry to maintain the charge on the capacitors after a few
milliseconds. It contains more memory cells per unit area as compared to SRAM.
4. Secondary Storage
Secondary storage, such as hard disk drives (HDD) and solid-state drives (SSD) ,
is a non-volatile memory unit that has a larger storage capacity than main memory.
It is used to store data and instructions that are not currently in use by the CPU.
Secondary storage has the slowest access time and is typically the least expensive
type of memory in the memory hierarchy.
5. Magnetic Disk
Magnetic Disks are simply circular plates that are fabricated with either a metal or
a plastic or a magnetized material. The Magnetic disks work at a high speed inside
the computer and these are frequently used.
6. Magnetic Tape
********** 6 **********
--- page 7 ---
Magnetic Tape is simply a magnetic recording device that is covered with a plastic
film. Magnetic Tape is generally used for the backup of data. In the case of a
magnetic tape, the access time for a computer is a little slower and therefore, it
requires some amount of time for accessing the strip. 5 Marks
1 Marks
Characteristics/ parameters of Memory Hierarchy
Capacity: It is the global volume of information the memory can store. As we
move from top to bottom in the Hierarchy, the capacity increases.
Access Time: It is the time interval between the read/write request and the
availability of the data. As we move from top to bottom in the Hierarchy, the
access time increases.
Performance: The Memory Hierarch design ensures that frequently accessed data
is stored in faster memory to improve system performance.
Cost Per Bit: As we move from bottom to top in the Hierarchy, the cost per bit
increases i.e. Internal Memory is costlier than External Memory. 4Marks
CO2, b Describe the internal architecture of the 8087 NDP. Explain how it enhances the   10
BT2   performance of the 8086 system in handling arithmetic operations.
Ans:
The 8087 NDP is a coprocessor designed to work with the 8086/8088
microprocessor to perform high-speed arithmetic and floating-point operations.
********** 7 **********
--- page 8 ---
Diagram =3marks
1. Control Unit   [Explanation 5 marks]
• Coordinates operations
• Synchronizes with 8086
2. Instruction Decoder
• Decodes ESC (escape) instructions from 8086
•   Identifies instructions meant for 8087
3. Floating Point Unit (FPU)
• Performs:
o Addition, subtraction
o Multiplication, division
o Square root, trigonometric functions
4. Register Stack (8 × 80-bit)
• Organized as stack (ST0–ST7)
•   Stores intermediate results
• High precision (80-bit format)
5. Data Bus Interface
• Communicates with memory and CPU
• Fetches operands and stores results
Performance Enhancement: [2marks]
Parallel Processing
• 8086 and 8087 operate simultaneously
• Improves throughput
✔ Faster Arithmetic Operations
********** 8 **********
--- page 9 ---
• Hardware-based floating-point operations
• Much faster than software implementation
✔ High Precision
•   80-bit internal registers
• Accurate scientific calculations
✔ Reduced CPU Load
• Complex calculations handled by 8087
• CPU free for other tasks
Q5   a Identify and explain any five characteristics of memory. Further, analyze how   10
CO2,   these characteristics affect the performance and design of a computer system.
BT 3
2 marks for each (any 5)
CO2, b Sketch the flowchart of Booth's Multiplication Algorithm and use Booth's   10
BT3   algorithm to multiply –6 and 5.
********** 9 **********
--- page 10 ---
Ans: Algo=4Marks
Solve=6marks
Q6   a Define RISC and CISC processors. Differentiate between them with suitable   10
CO3,   points.
BT2
********** 10 **********
--- page 11 ---
Ans:
RISC Definition 1m
CISC Definition 1m
Comparison 1m per point
RISC (Reduced Instruction Set Computer): a CPU architecture with a small, simple, and
regular set of instructions designed to execute quickly and be efficiently pipelined.
CISC (Complex Instruction Set Computer): a CPU architecture with a large set of
variable-length instructions that can perform complex tasks in fewer program
instructions but often require more complex decoding and multiple cycles.
CO4, b Describe the hardwired control unit with a neat block diagram. Explain its working   10
BT2   and discuss its main characteristics.
Ans:
Marks distribution: Describing hardwired control unit 5 marks
Block diagram with explanation 5 marks
• The control hardware can be viewed as a state machine that changes from one
state to another in every clock cycle, depending on the contents of the instruction
register, the condition codes, and the external inputs.
• The outputs of the state machine are the control signals. The sequence of the
operation carried out by this machine is determined by the wiring of the logic
elements and hence named “hardwired”.
•   Fixed logic circuits that correspond directly to the Boolean expressions are used
to generate the control signals. • Hardwired control is faster than micro-
programmed control.
• A controller that uses this approach can operate at high speed.
• RISC architecture is based on the hardwired control unit
Characteristics:
• A Hard wired Control consists of two decoders, a sequence counter, and a
number of logic gates
• An instruction fetched from the memory unit is placed in the instruction
register (IR)
• The component of an instruction register includes I bit, the operation code, and
bits 0 through 11
• The operation code in bits 12 through 14 are coded with a 3 x 8 decoder
• The outputs of the decoder are designated by the symbols D 0 through D 7
********** 11 **********
--- page 12 ---
• The operation code at bit 15 is transferred to a flip flop designated by the
symbol I
• The operation codes from Bits 0 through 11 are applied to the control logic
gates
• The Sequence counter (SC) can count in binary from 0 through 15
Q7   a With the help of a neat diagram, explain the DMA controller and its operation.   10
CO4,   Compare DMA with interrupt-driven I/O.
BT2
Ans: [Diagram 2 marks]
Steps: [Explanation 4 marks]
1. Initialization
o CPU provides starting address, data size, and direction to DMA
2. DMA Request
o I/O device sends request (DRQ)
3. Bus Request
o DMA requests control of system bus from CPU
4. Bus Grant
o CPU grants bus and suspends its operation
5. Data Transfer
o DMA transfers data directly:
▪ Memory ↔ I/O device
6. Completion
********** 12 **********
--- page 13 ---
o DMA interrupts CPU after transfer completion
Comparison: 4Marks
CO1, b   i.   Explain the functions of the Bus Interface Unit (BIU) and the Execution   5
BT2   Unit (EU) in the 8086 microprocessors during instruction fetching and
execution. Why is the processor divided into these two units?
Ans:
Functions of BIU (Bus Interface Unit)   [2marks]
CO1,   • Fetches instructions from memory
BT2   • Handles address generation using segment registers   5
• Maintains instruction queue (6 bytes) for prefetching
•   Transfers data between CPU, memory, and I/O
Functions of EU (Execution Unit)   [2marks]
• Decodes and executes instructions
• Performs arithmetic and logical operations (ALU)
• Uses registers for computation
• Takes instructions from the instruction queue
During Instruction Execution
• BIU fetches instructions and stores them in queue
• EU takes instructions from queue and executes them
• Both units work simultaneously
Why Division into BIU and EU?   [1 marks]
✔ Enables pipelining (parallelism)
✔ Improves execution speed
✔ Reduces CPU idle time
✔ Increases overall efficiency
ii.   Explain the stored program concept and its significance in modern
computer systems.
Ans: [Explanation: 3marks]
The stored program concept is a fundamental idea in computer architecture
introduced by John von Neumann. It means that a computer’s instructions
(program) and data are stored together in the same memory.
Explanation
In this concept:
• A program is stored in the computer’s memory just like data.
********** 13 **********
--- page 14 ---
• The CPU fetches instructions one by one from memory, decodes them, and
executes them.
• This is known as the fetch–decode–execute cycle.
Earlier machines required manual rewiring to change programs, but with this
concept, programs can be changed simply by loading new instructions into
memory.
Significance in Modern Computer Systems [2 marks]
1. Flexibility
Computers can perform different tasks by loading different programs
without changing hardware.
2. Ease of Programming
Programmers can write, modify, and store programs easily in memory.
3. Foundation of Modern Architecture
It forms the basis of the Von Neumann Architecture, used in most
computers today.
4. Efficient Execution
Automatic execution of instructions improves speed and efficiency.
5. Supports Advanced Features
Enables multitasking, operating systems, and complex applications.
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper ed98036061c2

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_IT_7041/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C059)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B.
Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 30 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. Assume Suitable data if necessary
Q.no   Questions   Mark
.   s
Q1
CO1, a Explain the general organization of a computer system and describe the interaction   5
BT2   between its major components
Ans:
[Diagram :2 Marks]
Major Components of a Computer System [2 marks]
1. Input Unit
Accepts data and instructions from the user
Converts them into machine-readable form
Example: Keyboard, mouse
2. Memory Unit
Stores data, instructions, and intermediate results
Types:
Primary memory (RAM, ROM)
Secondary memory (hard disk, SSD)
3. Central Processing Unit (CPU)
********** 1 **********
--- page 2 ---
• Arithmetic Logic Unit (ALU)
Performs arithmetic operations (addition, subtraction, etc.)
Performs logical operations (AND, OR, NOT)
• Control Unit (CU)
Controls and coordinates all operations
Fetches, decodes, and executes instructions
• Registers
High-speed storage inside CPU
Stores temporary data and instructions
4. Output Unit
Converts processed data into human-readable form
Example: Monitor, printer
Interaction Between Components [1marks]
CO3, b What is an instruction format? Illustrate an instruction format with examples.   5
BT2   Ans:
Definition 2marks
Diagram with explanation with Example 3marks
Def: The instruction format defines the layout and structure of the program instruction
that can be decoded by the CPU and then perform the desired operation on the data.
CO4, c Discuss any 5 applications of GPU.   5
BT2   Ans:
Each 1 marks
Ans.
A GPU (Graphics Processing Unit) is a specialized processor designed to handle
parallel processing, making it useful in many high-performance applications
beyond graphics.
1. Graphics Rendering
GPUs are mainly used for rendering images, videos, and animations in
computers, games, and multimedia applications.
👉 Example: 3D games, video editing, animation movies.
2. Machine Learning and AI
GPUs accelerate deep learning and neural network training due to their ability
to process large data in parallel.
👉 Example: Image recognition, speech processing, chatbots.
********** 2 **********
--- page 3 ---
3. Scientific Computing
Used in simulations and complex calculations in fields like physics, chemistry, and
engineering.
👉 Example: Weather forecasting, molecular modeling.
4. Data Processing and Big Data
GPUs help in fast processing of large datasets using parallel computing.
👉 Example: Data analytics, real-time data processing.
5. Cryptocurrency Mining
GPUs are widely used for solving complex mathematical problems required in
cryptocurrency mining.
👉 Example: Bitcoin, Ethereum mining.
CO4, d A system executes the same instruction on multiple data elements simultaneously.   5
BT4   Identify the appropriate Flynn’s classification and justify your answer with a
practical example.
Ans:
Marks Bifurcation
Identification: 2 Marks
Explanation with Example: 3 Marks
Answer-
The given system represents SIMD (Single Instruction Multiple Data) architecture.
In SIMD, a single instruction is executed simultaneously on multiple data
elements. This is useful when the same operation needs to be repeated on large
datasets. The system uses multiple processing units that perform identical
operations in parallel.
Example: Image processing where the same filter is applied to all pixels, or GPU
operations in graphics rendering.
Q2   a Sketch the diagram to elaborate interrupt handling process. Write the advantages   10
CO1,   and disadvantages of interrupt.
BT2   Ans:
********** 3 **********
--- page 4 ---
Diagram = 2 marks
Explanation= 4 marks
Advantages = 2 marks
Disadvantages= 2 marks
Steps Involved (Explanation):
1. Interrupt Request
o I/O device sends an interrupt signal to CPU
2. Interrupt Acknowledgment
o CPU completes current instruction
o Acknowledges the interrupt
3. Context Saving
o CPU saves the current state (PC, registers)
4. ISR Execution
o Control transfers to Interrupt Service Routine (ISR)
o Required service is performed
5. Context Restoration
o Saved state is restored
6. Resume Execution
o CPU continues execution of main program
Advantages:
•   Efficient use of CPU time.
•   Facilitates real-time processing.
•   Reduces polling overhead.
Disadvantages:
• Adds complexity to system design.
•   Frequent interrupts can reduce overall performance.
CO2, b Consider a computer system with the following cache specifications:   10
BT3   • Cache size = 32 KB
• Block size = 128 bytes
• Mapping technique = Fully Associative
• Main memory size = 1 MB
Assume byte-addressable memory.
Divide the main memory address into Tag and Block Offset fields and specify the
number of bits in each. Also, calculate the number of cache blocks.
Ans: [2.5 marks for each step\
Step 1: Calculate Address Size
Main memory = 2^20 bytes
Address bits = 20 bits
Step 2: Block Offset Bits
Block size = 2^7 bytes
Block offset = 7 bits
Step 3: Tag Bits
In fully associative mapping:
********** 4 **********
--- page 5 ---
• No index field
• Address = Tag + Block Offset
Tag bits=20−7=13 bits
Step 4: Number of Cache Blocks
Address Format
Tag (13 bits)   Block Offset (7 bits)
Q3   a Name the various phases involved in execution of an instruction and explain   10
CO1,   opcode fetch decode cycle in detail.
BT2   Ans:
Fetch instruction from memory.   [2 marks]
Decode the instruction.
Read the effective address from memory.
Execute the instruction.
Fetch Cycle:   [4 marks]
• The address of the next instruction to execute is in the Program Counter (PC) at
the beginning of the fetch cycle.
• The address in the program counter is transferred to the Memory Address
Register(MAR), as this is the only register that is connected to the system bus
address lines.The address in MAR is put on the address bus, now a Read order is
provided by the control unit on the control bus, and the result appears on the data
bus and is then copied into the memory buffer register.
• The program counter is incremented by one, to get ready for the next instruction.
These two acts can be carried out concurrently to save time.
• The content of the MBR is moved to the instruction register (IR). The instruction
fetch cycle consists of four micro-operations:
Decode instruction Cycle: [4 marks]
• The next move is to fetch source operands once an instruction is fetched.
•   Indirect addressing (it can be obtained by any addressing mode, here it is done
by indirect addressing) is obtained by Source Operand.
• The instruction address field is passed to the MAR. This is used to fetch the
operand 's address.
• The address field of the IR is updated from the MBR
• The IR is now in the state. Now IR is ready for the execute cycle
CO2, b Explain the IEEE 754 single precision floating-point format. Convert the decimal   10
BT3   number –47.375 to IEEE 754 single precision format. Show all steps.
Ans: [Each Step 2 marks]
Step 1 — Sign bit
Number is negative → Sign bit = 1
Step 2 — Convert 47.375 to binary
47 = 101111
0.375 × 2 = 0.75 → 0
********** 5 **********
--- page 6 ---
0.75 × 2 = 1.50 → 1
0.50 × 2 = 1.00 → 1
0.375 = 0.011
47.375 = 101111.011
Step 3 — Normalize
101111.011 = 1.01111011 × 25
Step 4 — Biased exponent (bias = 127)
5 + 127 = 132 = 10000100
Step 5 — Mantissa (drop leading 1, pad to 23 bits)
01111011000000000000000
Final 32-bit representation:
Sign   Exponent (8)   Mantissa (23)
(1)
1   10000100   01111011000000000000000
Q4   a Explain all the components of memory hierarchy with a neat diagram. Highlight   10
CO2,   its important parameters.
BT2
Ans:
Memory Hierarchy Design
1. Registers
Registers are small, high-speed memory units located in the CPU. They are used to
store the most frequently used data and instructions. Registers have the fastest
access time and the smallest storage capacity, typically ranging from 16 to 64 bits.
2. Cache Memory
Cache memory is a small, fast memory unit located close to the CPU. It stores
frequently used data and instructions that have been recently accessed from the
main memory. Cache memory is designed to minimize the time it takes to access
data by providing the CPU with quick access to frequently used data
3. Main Memory
Main memory, also known as RAM (Random Access Memory), is the primary
memory of a computer system. It has a larger storage capacity than cache memory,
but it is slower. Main memory is used to store data and instructions that are
currently in use by the CPU.
Types of Main Memory
Static RAM: Static RAM stores the binary information in flip flops and
information remains valid until power is supplied. Static RAM has a faster access
time and is used in implementing cache memory.
Dynamic RAM: It stores the binary information as a charge on the capacitor. It
requires refreshing circuitry to maintain the charge on the capacitors after a few
milliseconds. It contains more memory cells per unit area as compared to SRAM.
4. Secondary Storage
Secondary storage, such as hard disk drives (HDD) and solid-state drives (SSD) ,
is a non-volatile memory unit that has a larger storage capacity than main memory.
It is used to store data and instructions that are not currently in use by the CPU.
Secondary storage has the slowest access time and is typically the least expensive
type of memory in the memory hierarchy.
5. Magnetic Disk
Magnetic Disks are simply circular plates that are fabricated with either a metal or
a plastic or a magnetized material. The Magnetic disks work at a high speed inside
the computer and these are frequently used.
6. Magnetic Tape
********** 6 **********
--- page 7 ---
Magnetic Tape is simply a magnetic recording device that is covered with a plastic
film. Magnetic Tape is generally used for the backup of data. In the case of a
magnetic tape, the access time for a computer is a little slower and therefore, it
requires some amount of time for accessing the strip. 5 Marks
1 Marks
Characteristics/ parameters of Memory Hierarchy
Capacity: It is the global volume of information the memory can store. As we
move from top to bottom in the Hierarchy, the capacity increases.
Access Time: It is the time interval between the read/write request and the
availability of the data. As we move from top to bottom in the Hierarchy, the
access time increases.
Performance: The Memory Hierarch design ensures that frequently accessed data
is stored in faster memory to improve system performance.
Cost Per Bit: As we move from bottom to top in the Hierarchy, the cost per bit
increases i.e. Internal Memory is costlier than External Memory. 4Marks
CO2, b Describe the internal architecture of the 8087 NDP. Explain how it enhances the   10
BT2   performance of the 8086 system in handling arithmetic operations.
Ans:
The 8087 NDP is a coprocessor designed to work with the 8086/8088
microprocessor to perform high-speed arithmetic and floating-point operations.
********** 7 **********
--- page 8 ---
Diagram =3marks
1. Control Unit   [Explanation 5 marks]
• Coordinates operations
• Synchronizes with 8086
2. Instruction Decoder
• Decodes ESC (escape) instructions from 8086
•   Identifies instructions meant for 8087
3. Floating Point Unit (FPU)
• Performs:
o Addition, subtraction
o Multiplication, division
o Square root, trigonometric functions
4. Register Stack (8 × 80-bit)
• Organized as stack (ST0–ST7)
•   Stores intermediate results
• High precision (80-bit format)
5. Data Bus Interface
• Communicates with memory and CPU
• Fetches operands and stores results
Performance Enhancement: [2marks]
Parallel Processing
• 8086 and 8087 operate simultaneously
• Improves throughput
✔ Faster Arithmetic Operations
********** 8 **********
--- page 9 ---
• Hardware-based floating-point operations
• Much faster than software implementation
✔ High Precision
•   80-bit internal registers
• Accurate scientific calculations
✔ Reduced CPU Load
• Complex calculations handled by 8087
• CPU free for other tasks
Q5   a Identify and explain any five characteristics of memory. Further, analyze how   10
CO2,   these characteristics affect the performance and design of a computer system.
BT 3
2 marks for each (any 5)
CO2, b Sketch the flowchart of Booth's Multiplication Algorithm and use Booth's   10
BT3   algorithm to multiply –6 and 5.
********** 9 **********
--- page 10 ---
Ans: Algo=4Marks
Solve=6marks
Q6   a Define RISC and CISC processors. Differentiate between them with suitable   10
CO3,   points.
BT2
********** 10 **********
--- page 11 ---
Ans:
RISC Definition 1m
CISC Definition 1m
Comparison 1m per point
RISC (Reduced Instruction Set Computer): a CPU architecture with a small, simple, and
regular set of instructions designed to execute quickly and be efficiently pipelined.
CISC (Complex Instruction Set Computer): a CPU architecture with a large set of
variable-length instructions that can perform complex tasks in fewer program
instructions but often require more complex decoding and multiple cycles.
CO4, b Describe the hardwired control unit with a neat block diagram. Explain its working   10
BT2   and discuss its main characteristics.
Ans:
Marks distribution: Describing hardwired control unit 5 marks
Block diagram with explanation 5 marks
• The control hardware can be viewed as a state machine that changes from one
state to another in every clock cycle, depending on the contents of the instruction
register, the condition codes, and the external inputs.
• The outputs of the state machine are the control signals. The sequence of the
operation carried out by this machine is determined by the wiring of the logic
elements and hence named “hardwired”.
•   Fixed logic circuits that correspond directly to the Boolean expressions are used
to generate the control signals. • Hardwired control is faster than micro-
programmed control.
• A controller that uses this approach can operate at high speed.
• RISC architecture is based on the hardwired control unit
Characteristics:
• A Hard wired Control consists of two decoders, a sequence counter, and a
number of logic gates
• An instruction fetched from the memory unit is placed in the instruction
register (IR)
• The component of an instruction register includes I bit, the operation code, and
bits 0 through 11
• The operation code in bits 12 through 14 are coded with a 3 x 8 decoder
• The outputs of the decoder are designated by the symbols D 0 through D 7
********** 11 **********
--- page 12 ---
• The operation code at bit 15 is transferred to a flip flop designated by the
symbol I
• The operation codes from Bits 0 through 11 are applied to the control logic
gates
• The Sequence counter (SC) can count in binary from 0 through 15
Q7   a With the help of a neat diagram, explain the DMA controller and its operation.   10
CO4,   Compare DMA with interrupt-driven I/O.
BT2
Ans: [Diagram 2 marks]
Steps: [Explanation 4 marks]
1. Initialization
o CPU provides starting address, data size, and direction to DMA
2. DMA Request
o I/O device sends request (DRQ)
3. Bus Request
o DMA requests control of system bus from CPU
4. Bus Grant
o CPU grants bus and suspends its operation
5. Data Transfer
o DMA transfers data directly:
▪ Memory ↔ I/O device
6. Completion
********** 12 **********
--- page 13 ---
o DMA interrupts CPU after transfer completion
Comparison: 4Marks
CO1, b   i.   Explain the functions of the Bus Interface Unit (BIU) and the Execution   5
BT2   Unit (EU) in the 8086 microprocessors during instruction fetching and
execution. Why is the processor divided into these two units?
Ans:
Functions of BIU (Bus Interface Unit)   [2marks]
CO1,   • Fetches instructions from memory
BT2   • Handles address generation using segment registers   5
• Maintains instruction queue (6 bytes) for prefetching
•   Transfers data between CPU, memory, and I/O
Functions of EU (Execution Unit)   [2marks]
• Decodes and executes instructions
• Performs arithmetic and logical operations (ALU)
• Uses registers for computation
• Takes instructions from the instruction queue
During Instruction Execution
• BIU fetches instructions and stores them in queue
• EU takes instructions from queue and executes them
• Both units work simultaneously
Why Division into BIU and EU?   [1 marks]
✔ Enables pipelining (parallelism)
✔ Improves execution speed
✔ Reduces CPU idle time
✔ Increases overall efficiency
ii.   Explain the stored program concept and its significance in modern
computer systems.
Ans: [Explanation: 3marks]
The stored program concept is a fundamental idea in computer architecture
introduced by John von Neumann. It means that a computer’s instructions
(program) and data are stored together in the same memory.
Explanation
In this concept:
• A program is stored in the computer’s memory just like data.
********** 13 **********
--- page 14 ---
• The CPU fetches instructions one by one from memory, decodes them, and
executes them.
• This is known as the fetch–decode–execute cycle.
Earlier machines required manual rewiring to change programs, but with this
concept, programs can be changed simply by loading new instructions into
memory.
Significance in Modern Computer Systems [2 marks]
1. Flexibility
Computers can perform different tasks by loading different programs
without changing hardware.
2. Ease of Programming
Programmers can write, modify, and store programs easily in memory.
3. Foundation of Modern Architecture
It forms the basis of the Von Neumann Architecture, used in most
computers today.
4. Efficient Execution
Automatic execution of instructions improves speed and efficiency.
5. Supports Advanced Features
Enables multitasking, operating systems, and complex applications.
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper ae70d2945bf8

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/Integrated_Computer_7032/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B.
Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 30 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. Assume Suitable data if necessary
Q.no   Questions   Mark
.   s
Q1
CO1, a Explain the general organization of a computer system and describe the interaction   5
BT2   between its major components
Ans:
[Diagram :2 Marks]
Major Components of a Computer System [2 marks]
1. Input Unit
Accepts data and instructions from the user
Converts them into machine-readable form
Example: Keyboard, mouse
2. Memory Unit
Stores data, instructions, and intermediate results
Types:
Primary memory (RAM, ROM)
Secondary memory (hard disk, SSD)
3. Central Processing Unit (CPU)
********** 1 **********
--- page 2 ---
• Arithmetic Logic Unit (ALU)
Performs arithmetic operations (addition, subtraction, etc.)
Performs logical operations (AND, OR, NOT)
• Control Unit (CU)
Controls and coordinates all operations
Fetches, decodes, and executes instructions
• Registers
High-speed storage inside CPU
Stores temporary data and instructions
4. Output Unit
Converts processed data into human-readable form
Example: Monitor, printer
Interaction Between Components [1marks]
CO3, b What is an instruction format? Illustrate an instruction format with examples.   5
BT2   Ans:
Definition 2marks
Diagram with explanation with Example 3marks
Def: The instruction format defines the layout and structure of the program instruction
that can be decoded by the CPU and then perform the desired operation on the data.
CO4, c Discuss any 5 applications of GPU.   5
BT2   Ans:
Each 1 marks
Ans.
A GPU (Graphics Processing Unit) is a specialized processor designed to handle
parallel processing, making it useful in many high-performance applications
beyond graphics.
1. Graphics Rendering
GPUs are mainly used for rendering images, videos, and animations in
computers, games, and multimedia applications.
👉 Example: 3D games, video editing, animation movies.
2. Machine Learning and AI
GPUs accelerate deep learning and neural network training due to their ability
to process large data in parallel.
👉 Example: Image recognition, speech processing, chatbots.
********** 2 **********
--- page 3 ---
3. Scientific Computing
Used in simulations and complex calculations in fields like physics, chemistry, and
engineering.
👉 Example: Weather forecasting, molecular modeling.
4. Data Processing and Big Data
GPUs help in fast processing of large datasets using parallel computing.
👉 Example: Data analytics, real-time data processing.
5. Cryptocurrency Mining
GPUs are widely used for solving complex mathematical problems required in
cryptocurrency mining.
👉 Example: Bitcoin, Ethereum mining.
CO4, d A system executes the same instruction on multiple data elements simultaneously.   5
BT4   Identify the appropriate Flynn’s classification and justify your answer with a
practical example.
Ans:
Marks Bifurcation
Identification: 2 Marks
Explanation with Example: 3 Marks
Answer-
The given system represents SIMD (Single Instruction Multiple Data) architecture.
In SIMD, a single instruction is executed simultaneously on multiple data
elements. This is useful when the same operation needs to be repeated on large
datasets. The system uses multiple processing units that perform identical
operations in parallel.
Example: Image processing where the same filter is applied to all pixels, or GPU
operations in graphics rendering.
Q2   a Sketch the diagram to elaborate interrupt handling process. Write the advantages   10
CO1,   and disadvantages of interrupt.
BT2   Ans:
********** 3 **********
--- page 4 ---
Diagram = 2 marks
Explanation= 4 marks
Advantages = 2 marks
Disadvantages= 2 marks
Steps Involved (Explanation):
1. Interrupt Request
o I/O device sends an interrupt signal to CPU
2. Interrupt Acknowledgment
o CPU completes current instruction
o Acknowledges the interrupt
3. Context Saving
o CPU saves the current state (PC, registers)
4. ISR Execution
o Control transfers to Interrupt Service Routine (ISR)
o Required service is performed
5. Context Restoration
o Saved state is restored
6. Resume Execution
o CPU continues execution of main program
Advantages:
•   Efficient use of CPU time.
•   Facilitates real-time processing.
•   Reduces polling overhead.
Disadvantages:
• Adds complexity to system design.
•   Frequent interrupts can reduce overall performance.
CO2, b Consider a computer system with the following cache specifications:   10
BT3   • Cache size = 32 KB
• Block size = 128 bytes
• Mapping technique = Fully Associative
• Main memory size = 1 MB
Assume byte-addressable memory.
Divide the main memory address into Tag and Block Offset fields and specify the
number of bits in each. Also, calculate the number of cache blocks.
Ans: [2.5 marks for each step\
Step 1: Calculate Address Size
Main memory = 2^20 bytes
Address bits = 20 bits
Step 2: Block Offset Bits
Block size = 2^7 bytes
Block offset = 7 bits
Step 3: Tag Bits
In fully associative mapping:
********** 4 **********
--- page 5 ---
• No index field
• Address = Tag + Block Offset
Tag bits=20−7=13 bits
Step 4: Number of Cache Blocks
Address Format
Tag (13 bits)   Block Offset (7 bits)
Q3   a Name the various phases involved in execution of an instruction and explain   10
CO1,   opcode fetch decode cycle in detail.
BT2   Ans:
Fetch instruction from memory.   [2 marks]
Decode the instruction.
Read the effective address from memory.
Execute the instruction.
Fetch Cycle:   [4 marks]
• The address of the next instruction to execute is in the Program Counter (PC) at
the beginning of the fetch cycle.
• The address in the program counter is transferred to the Memory Address
Register(MAR), as this is the only register that is connected to the system bus
address lines.The address in MAR is put on the address bus, now a Read order is
provided by the control unit on the control bus, and the result appears on the data
bus and is then copied into the memory buffer register.
• The program counter is incremented by one, to get ready for the next instruction.
These two acts can be carried out concurrently to save time.
• The content of the MBR is moved to the instruction register (IR). The instruction
fetch cycle consists of four micro-operations:
Decode instruction Cycle: [4 marks]
• The next move is to fetch source operands once an instruction is fetched.
•   Indirect addressing (it can be obtained by any addressing mode, here it is done
by indirect addressing) is obtained by Source Operand.
• The instruction address field is passed to the MAR. This is used to fetch the
operand 's address.
• The address field of the IR is updated from the MBR
• The IR is now in the state. Now IR is ready for the execute cycle
CO2, b Explain the IEEE 754 single precision floating-point format. Convert the decimal   10
BT3   number –47.375 to IEEE 754 single precision format. Show all steps.
Ans: [Each Step 2 marks]
Step 1 — Sign bit
Number is negative → Sign bit = 1
Step 2 — Convert 47.375 to binary
47 = 101111
0.375 × 2 = 0.75 → 0
********** 5 **********
--- page 6 ---
0.75 × 2 = 1.50 → 1
0.50 × 2 = 1.00 → 1
0.375 = 0.011
47.375 = 101111.011
Step 3 — Normalize
101111.011 = 1.01111011 × 25
Step 4 — Biased exponent (bias = 127)
5 + 127 = 132 = 10000100
Step 5 — Mantissa (drop leading 1, pad to 23 bits)
01111011000000000000000
Final 32-bit representation:
Sign   Exponent (8)   Mantissa (23)
(1)
1   10000100   01111011000000000000000
Q4   a Explain all the components of memory hierarchy with a neat diagram. Highlight   10
CO2,   its important parameters.
BT2
Ans:
Memory Hierarchy Design
1. Registers
Registers are small, high-speed memory units located in the CPU. They are used to
store the most frequently used data and instructions. Registers have the fastest
access time and the smallest storage capacity, typically ranging from 16 to 64 bits.
2. Cache Memory
Cache memory is a small, fast memory unit located close to the CPU. It stores
frequently used data and instructions that have been recently accessed from the
main memory. Cache memory is designed to minimize the time it takes to access
data by providing the CPU with quick access to frequently used data
3. Main Memory
Main memory, also known as RAM (Random Access Memory), is the primary
memory of a computer system. It has a larger storage capacity than cache memory,
but it is slower. Main memory is used to store data and instructions that are
currently in use by the CPU.
Types of Main Memory
Static RAM: Static RAM stores the binary information in flip flops and
information remains valid until power is supplied. Static RAM has a faster access
time and is used in implementing cache memory.
Dynamic RAM: It stores the binary information as a charge on the capacitor. It
requires refreshing circuitry to maintain the charge on the capacitors after a few
milliseconds. It contains more memory cells per unit area as compared to SRAM.
4. Secondary Storage
Secondary storage, such as hard disk drives (HDD) and solid-state drives (SSD) ,
is a non-volatile memory unit that has a larger storage capacity than main memory.
It is used to store data and instructions that are not currently in use by the CPU.
Secondary storage has the slowest access time and is typically the least expensive
type of memory in the memory hierarchy.
5. Magnetic Disk
Magnetic Disks are simply circular plates that are fabricated with either a metal or
a plastic or a magnetized material. The Magnetic disks work at a high speed inside
the computer and these are frequently used.
6. Magnetic Tape
********** 6 **********
--- page 7 ---
Magnetic Tape is simply a magnetic recording device that is covered with a plastic
film. Magnetic Tape is generally used for the backup of data. In the case of a
magnetic tape, the access time for a computer is a little slower and therefore, it
requires some amount of time for accessing the strip. 5 Marks
1 Marks
Characteristics/ parameters of Memory Hierarchy
Capacity: It is the global volume of information the memory can store. As we
move from top to bottom in the Hierarchy, the capacity increases.
Access Time: It is the time interval between the read/write request and the
availability of the data. As we move from top to bottom in the Hierarchy, the
access time increases.
Performance: The Memory Hierarch design ensures that frequently accessed data
is stored in faster memory to improve system performance.
Cost Per Bit: As we move from bottom to top in the Hierarchy, the cost per bit
increases i.e. Internal Memory is costlier than External Memory. 4Marks
CO2, b Describe the internal architecture of the 8087 NDP. Explain how it enhances the   10
BT2   performance of the 8086 system in handling arithmetic operations.
Ans:
The 8087 NDP is a coprocessor designed to work with the 8086/8088
microprocessor to perform high-speed arithmetic and floating-point operations.
********** 7 **********
--- page 8 ---
Diagram =3marks
1. Control Unit   [Explanation 5 marks]
• Coordinates operations
• Synchronizes with 8086
2. Instruction Decoder
• Decodes ESC (escape) instructions from 8086
•   Identifies instructions meant for 8087
3. Floating Point Unit (FPU)
• Performs:
o Addition, subtraction
o Multiplication, division
o Square root, trigonometric functions
4. Register Stack (8 × 80-bit)
• Organized as stack (ST0–ST7)
•   Stores intermediate results
• High precision (80-bit format)
5. Data Bus Interface
• Communicates with memory and CPU
• Fetches operands and stores results
Performance Enhancement: [2marks]
Parallel Processing
• 8086 and 8087 operate simultaneously
• Improves throughput
✔ Faster Arithmetic Operations
********** 8 **********
--- page 9 ---
• Hardware-based floating-point operations
• Much faster than software implementation
✔ High Precision
•   80-bit internal registers
• Accurate scientific calculations
✔ Reduced CPU Load
• Complex calculations handled by 8087
• CPU free for other tasks
Q5   a Identify and explain any five characteristics of memory. Further, analyze how   10
CO2,   these characteristics affect the performance and design of a computer system.
BT 3
2 marks for each (any 5)
CO2, b Sketch the flowchart of Booth's Multiplication Algorithm and use Booth's   10
BT3   algorithm to multiply –6 and 5.
********** 9 **********
--- page 10 ---
Ans: Algo=4Marks
Solve=6marks
Q6   a Define RISC and CISC processors. Differentiate between them with suitable   10
CO3,   points.
BT2
********** 10 **********
--- page 11 ---
Ans:
RISC Definition 1m
CISC Definition 1m
Comparison 1m per point
RISC (Reduced Instruction Set Computer): a CPU architecture with a small, simple, and
regular set of instructions designed to execute quickly and be efficiently pipelined.
CISC (Complex Instruction Set Computer): a CPU architecture with a large set of
variable-length instructions that can perform complex tasks in fewer program
instructions but often require more complex decoding and multiple cycles.
CO4, b Describe the hardwired control unit with a neat block diagram. Explain its working   10
BT2   and discuss its main characteristics.
Ans:
Marks distribution: Describing hardwired control unit 5 marks
Block diagram with explanation 5 marks
• The control hardware can be viewed as a state machine that changes from one
state to another in every clock cycle, depending on the contents of the instruction
register, the condition codes, and the external inputs.
• The outputs of the state machine are the control signals. The sequence of the
operation carried out by this machine is determined by the wiring of the logic
elements and hence named “hardwired”.
•   Fixed logic circuits that correspond directly to the Boolean expressions are used
to generate the control signals. • Hardwired control is faster than micro-
programmed control.
• A controller that uses this approach can operate at high speed.
• RISC architecture is based on the hardwired control unit
Characteristics:
• A Hard wired Control consists of two decoders, a sequence counter, and a
number of logic gates
• An instruction fetched from the memory unit is placed in the instruction
register (IR)
• The component of an instruction register includes I bit, the operation code, and
bits 0 through 11
• The operation code in bits 12 through 14 are coded with a 3 x 8 decoder
• The outputs of the decoder are designated by the symbols D 0 through D 7
********** 11 **********
--- page 12 ---
• The operation code at bit 15 is transferred to a flip flop designated by the
symbol I
• The operation codes from Bits 0 through 11 are applied to the control logic
gates
• The Sequence counter (SC) can count in binary from 0 through 15
Q7   a With the help of a neat diagram, explain the DMA controller and its operation.   10
CO4,   Compare DMA with interrupt-driven I/O.
BT2
Ans: [Diagram 2 marks]
Steps: [Explanation 4 marks]
1. Initialization
o CPU provides starting address, data size, and direction to DMA
2. DMA Request
o I/O device sends request (DRQ)
3. Bus Request
o DMA requests control of system bus from CPU
4. Bus Grant
o CPU grants bus and suspends its operation
5. Data Transfer
o DMA transfers data directly:
▪ Memory ↔ I/O device
6. Completion
********** 12 **********
--- page 13 ---
o DMA interrupts CPU after transfer completion
Comparison: 4Marks
CO1, b   i.   Explain the functions of the Bus Interface Unit (BIU) and the Execution   5
BT2   Unit (EU) in the 8086 microprocessors during instruction fetching and
execution. Why is the processor divided into these two units?
Ans:
Functions of BIU (Bus Interface Unit)   [2marks]
CO1,   • Fetches instructions from memory
BT2   • Handles address generation using segment registers   5
• Maintains instruction queue (6 bytes) for prefetching
•   Transfers data between CPU, memory, and I/O
Functions of EU (Execution Unit)   [2marks]
• Decodes and executes instructions
• Performs arithmetic and logical operations (ALU)
• Uses registers for computation
• Takes instructions from the instruction queue
During Instruction Execution
• BIU fetches instructions and stores them in queue
• EU takes instructions from queue and executes them
• Both units work simultaneously
Why Division into BIU and EU?   [1 marks]
✔ Enables pipelining (parallelism)
✔ Improves execution speed
✔ Reduces CPU idle time
✔ Increases overall efficiency
ii.   Explain the stored program concept and its significance in modern
computer systems.
Ans: [Explanation: 3marks]
The stored program concept is a fundamental idea in computer architecture
introduced by John von Neumann. It means that a computer’s instructions
(program) and data are stored together in the same memory.
Explanation
In this concept:
• A program is stored in the computer’s memory just like data.
********** 13 **********
--- page 14 ---
• The CPU fetches instructions one by one from memory, decodes them, and
executes them.
• This is known as the fetch–decode–execute cycle.
Earlier machines required manual rewiring to change programs, but with this
concept, programs can be changed simply by loading new instructions into
memory.
Significance in Modern Computer Systems [2 marks]
1. Flexibility
Computers can perform different tasks by loading different programs
without changing hardware.
2. Ease of Programming
Programmers can write, modify, and store programs easily in memory.
3. Foundation of Modern Architecture
It forms the basis of the Von Neumann Architecture, used in most
computers today.
4. Efficient Execution
Automatic execution of instructions improves speed and efficiency.
5. Supports Advanced Features
Enables multitasking, operating systems, and complex applications.
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper 78c5eeb27c4f

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/Integrated_IT_7037/Computer Organization and Architecture/ANS_Computer Organization and Architecture(702CO0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - CS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B.
Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / IV/Sem 4 Re-exam/Sem 8 Re-exam/Semester IV(Exam Year: 2025-2026)
Subject: Computer Organization and Architecture
Date: 30 Jun 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. Assume Suitable data if necessary
Q.no   Questions   Mark
.   s
Q1
CO1, a Explain the general organization of a computer system and describe the interaction   5
BT2   between its major components
Ans:
[Diagram :2 Marks]
Major Components of a Computer System [2 marks]
1. Input Unit
Accepts data and instructions from the user
Converts them into machine-readable form
Example: Keyboard, mouse
2. Memory Unit
Stores data, instructions, and intermediate results
Types:
Primary memory (RAM, ROM)
Secondary memory (hard disk, SSD)
3. Central Processing Unit (CPU)
********** 1 **********
--- page 2 ---
• Arithmetic Logic Unit (ALU)
Performs arithmetic operations (addition, subtraction, etc.)
Performs logical operations (AND, OR, NOT)
• Control Unit (CU)
Controls and coordinates all operations
Fetches, decodes, and executes instructions
• Registers
High-speed storage inside CPU
Stores temporary data and instructions
4. Output Unit
Converts processed data into human-readable form
Example: Monitor, printer
Interaction Between Components [1marks]
CO3, b What is an instruction format? Illustrate an instruction format with examples.   5
BT2   Ans:
Definition 2marks
Diagram with explanation with Example 3marks
Def: The instruction format defines the layout and structure of the program instruction
that can be decoded by the CPU and then perform the desired operation on the data.
CO4, c Discuss any 5 applications of GPU.   5
BT2   Ans:
Each 1 marks
Ans.
A GPU (Graphics Processing Unit) is a specialized processor designed to handle
parallel processing, making it useful in many high-performance applications
beyond graphics.
1. Graphics Rendering
GPUs are mainly used for rendering images, videos, and animations in
computers, games, and multimedia applications.
👉 Example: 3D games, video editing, animation movies.
2. Machine Learning and AI
GPUs accelerate deep learning and neural network training due to their ability
to process large data in parallel.
👉 Example: Image recognition, speech processing, chatbots.
********** 2 **********
--- page 3 ---
3. Scientific Computing
Used in simulations and complex calculations in fields like physics, chemistry, and
engineering.
👉 Example: Weather forecasting, molecular modeling.
4. Data Processing and Big Data
GPUs help in fast processing of large datasets using parallel computing.
👉 Example: Data analytics, real-time data processing.
5. Cryptocurrency Mining
GPUs are widely used for solving complex mathematical problems required in
cryptocurrency mining.
👉 Example: Bitcoin, Ethereum mining.
CO4, d A system executes the same instruction on multiple data elements simultaneously.   5
BT4   Identify the appropriate Flynn’s classification and justify your answer with a
practical example.
Ans:
Marks Bifurcation
Identification: 2 Marks
Explanation with Example: 3 Marks
Answer-
The given system represents SIMD (Single Instruction Multiple Data) architecture.
In SIMD, a single instruction is executed simultaneously on multiple data
elements. This is useful when the same operation needs to be repeated on large
datasets. The system uses multiple processing units that perform identical
operations in parallel.
Example: Image processing where the same filter is applied to all pixels, or GPU
operations in graphics rendering.
Q2   a Sketch the diagram to elaborate interrupt handling process. Write the advantages   10
CO1,   and disadvantages of interrupt.
BT2   Ans:
********** 3 **********
--- page 4 ---
Diagram = 2 marks
Explanation= 4 marks
Advantages = 2 marks
Disadvantages= 2 marks
Steps Involved (Explanation):
1. Interrupt Request
o I/O device sends an interrupt signal to CPU
2. Interrupt Acknowledgment
o CPU completes current instruction
o Acknowledges the interrupt
3. Context Saving
o CPU saves the current state (PC, registers)
4. ISR Execution
o Control transfers to Interrupt Service Routine (ISR)
o Required service is performed
5. Context Restoration
o Saved state is restored
6. Resume Execution
o CPU continues execution of main program
Advantages:
•   Efficient use of CPU time.
•   Facilitates real-time processing.
•   Reduces polling overhead.
Disadvantages:
• Adds complexity to system design.
•   Frequent interrupts can reduce overall performance.
CO2, b Consider a computer system with the following cache specifications:   10
BT3   • Cache size = 32 KB
• Block size = 128 bytes
• Mapping technique = Fully Associative
• Main memory size = 1 MB
Assume byte-addressable memory.
Divide the main memory address into Tag and Block Offset fields and specify the
number of bits in each. Also, calculate the number of cache blocks.
Ans: [2.5 marks for each step\
Step 1: Calculate Address Size
Main memory = 2^20 bytes
Address bits = 20 bits
Step 2: Block Offset Bits
Block size = 2^7 bytes
Block offset = 7 bits
Step 3: Tag Bits
In fully associative mapping:
********** 4 **********
--- page 5 ---
• No index field
• Address = Tag + Block Offset
Tag bits=20−7=13 bits
Step 4: Number of Cache Blocks
Address Format
Tag (13 bits)   Block Offset (7 bits)
Q3   a Name the various phases involved in execution of an instruction and explain   10
CO1,   opcode fetch decode cycle in detail.
BT2   Ans:
Fetch instruction from memory.   [2 marks]
Decode the instruction.
Read the effective address from memory.
Execute the instruction.
Fetch Cycle:   [4 marks]
• The address of the next instruction to execute is in the Program Counter (PC) at
the beginning of the fetch cycle.
• The address in the program counter is transferred to the Memory Address
Register(MAR), as this is the only register that is connected to the system bus
address lines.The address in MAR is put on the address bus, now a Read order is
provided by the control unit on the control bus, and the result appears on the data
bus and is then copied into the memory buffer register.
• The program counter is incremented by one, to get ready for the next instruction.
These two acts can be carried out concurrently to save time.
• The content of the MBR is moved to the instruction register (IR). The instruction
fetch cycle consists of four micro-operations:
Decode instruction Cycle: [4 marks]
• The next move is to fetch source operands once an instruction is fetched.
•   Indirect addressing (it can be obtained by any addressing mode, here it is done
by indirect addressing) is obtained by Source Operand.
• The instruction address field is passed to the MAR. This is used to fetch the
operand 's address.
• The address field of the IR is updated from the MBR
• The IR is now in the state. Now IR is ready for the execute cycle
CO2, b Explain the IEEE 754 single precision floating-point format. Convert the decimal   10
BT3   number –47.375 to IEEE 754 single precision format. Show all steps.
Ans: [Each Step 2 marks]
Step 1 — Sign bit
Number is negative → Sign bit = 1
Step 2 — Convert 47.375 to binary
47 = 101111
0.375 × 2 = 0.75 → 0
********** 5 **********
--- page 6 ---
0.75 × 2 = 1.50 → 1
0.50 × 2 = 1.00 → 1
0.375 = 0.011
47.375 = 101111.011
Step 3 — Normalize
101111.011 = 1.01111011 × 25
Step 4 — Biased exponent (bias = 127)
5 + 127 = 132 = 10000100
Step 5 — Mantissa (drop leading 1, pad to 23 bits)
01111011000000000000000
Final 32-bit representation:
Sign   Exponent (8)   Mantissa (23)
(1)
1   10000100   01111011000000000000000
Q4   a Explain all the components of memory hierarchy with a neat diagram. Highlight   10
CO2,   its important parameters.
BT2
Ans:
Memory Hierarchy Design
1. Registers
Registers are small, high-speed memory units located in the CPU. They are used to
store the most frequently used data and instructions. Registers have the fastest
access time and the smallest storage capacity, typically ranging from 16 to 64 bits.
2. Cache Memory
Cache memory is a small, fast memory unit located close to the CPU. It stores
frequently used data and instructions that have been recently accessed from the
main memory. Cache memory is designed to minimize the time it takes to access
data by providing the CPU with quick access to frequently used data
3. Main Memory
Main memory, also known as RAM (Random Access Memory), is the primary
memory of a computer system. It has a larger storage capacity than cache memory,
but it is slower. Main memory is used to store data and instructions that are
currently in use by the CPU.
Types of Main Memory
Static RAM: Static RAM stores the binary information in flip flops and
information remains valid until power is supplied. Static RAM has a faster access
time and is used in implementing cache memory.
Dynamic RAM: It stores the binary information as a charge on the capacitor. It
requires refreshing circuitry to maintain the charge on the capacitors after a few
milliseconds. It contains more memory cells per unit area as compared to SRAM.
4. Secondary Storage
Secondary storage, such as hard disk drives (HDD) and solid-state drives (SSD) ,
is a non-volatile memory unit that has a larger storage capacity than main memory.
It is used to store data and instructions that are not currently in use by the CPU.
Secondary storage has the slowest access time and is typically the least expensive
type of memory in the memory hierarchy.
5. Magnetic Disk
Magnetic Disks are simply circular plates that are fabricated with either a metal or
a plastic or a magnetized material. The Magnetic disks work at a high speed inside
the computer and these are frequently used.
6. Magnetic Tape
********** 6 **********
--- page 7 ---
Magnetic Tape is simply a magnetic recording device that is covered with a plastic
film. Magnetic Tape is generally used for the backup of data. In the case of a
magnetic tape, the access time for a computer is a little slower and therefore, it
requires some amount of time for accessing the strip. 5 Marks
1 Marks
Characteristics/ parameters of Memory Hierarchy
Capacity: It is the global volume of information the memory can store. As we
move from top to bottom in the Hierarchy, the capacity increases.
Access Time: It is the time interval between the read/write request and the
availability of the data. As we move from top to bottom in the Hierarchy, the
access time increases.
Performance: The Memory Hierarch design ensures that frequently accessed data
is stored in faster memory to improve system performance.
Cost Per Bit: As we move from bottom to top in the Hierarchy, the cost per bit
increases i.e. Internal Memory is costlier than External Memory. 4Marks
CO2, b Describe the internal architecture of the 8087 NDP. Explain how it enhances the   10
BT2   performance of the 8086 system in handling arithmetic operations.
Ans:
The 8087 NDP is a coprocessor designed to work with the 8086/8088
microprocessor to perform high-speed arithmetic and floating-point operations.
********** 7 **********
--- page 8 ---
Diagram =3marks
1. Control Unit   [Explanation 5 marks]
• Coordinates operations
• Synchronizes with 8086
2. Instruction Decoder
• Decodes ESC (escape) instructions from 8086
•   Identifies instructions meant for 8087
3. Floating Point Unit (FPU)
• Performs:
o Addition, subtraction
o Multiplication, division
o Square root, trigonometric functions
4. Register Stack (8 × 80-bit)
• Organized as stack (ST0–ST7)
•   Stores intermediate results
• High precision (80-bit format)
5. Data Bus Interface
• Communicates with memory and CPU
• Fetches operands and stores results
Performance Enhancement: [2marks]
Parallel Processing
• 8086 and 8087 operate simultaneously
• Improves throughput
✔ Faster Arithmetic Operations
********** 8 **********
--- page 9 ---
• Hardware-based floating-point operations
• Much faster than software implementation
✔ High Precision
•   80-bit internal registers
• Accurate scientific calculations
✔ Reduced CPU Load
• Complex calculations handled by 8087
• CPU free for other tasks
Q5   a Identify and explain any five characteristics of memory. Further, analyze how   10
CO2,   these characteristics affect the performance and design of a computer system.
BT 3
2 marks for each (any 5)
CO2, b Sketch the flowchart of Booth's Multiplication Algorithm and use Booth's   10
BT3   algorithm to multiply –6 and 5.
********** 9 **********
--- page 10 ---
Ans: Algo=4Marks
Solve=6marks
Q6   a Define RISC and CISC processors. Differentiate between them with suitable   10
CO3,   points.
BT2
********** 10 **********
--- page 11 ---
Ans:
RISC Definition 1m
CISC Definition 1m
Comparison 1m per point
RISC (Reduced Instruction Set Computer): a CPU architecture with a small, simple, and
regular set of instructions designed to execute quickly and be efficiently pipelined.
CISC (Complex Instruction Set Computer): a CPU architecture with a large set of
variable-length instructions that can perform complex tasks in fewer program
instructions but often require more complex decoding and multiple cycles.
CO4, b Describe the hardwired control unit with a neat block diagram. Explain its working   10
BT2   and discuss its main characteristics.
Ans:
Marks distribution: Describing hardwired control unit 5 marks
Block diagram with explanation 5 marks
• The control hardware can be viewed as a state machine that changes from one
state to another in every clock cycle, depending on the contents of the instruction
register, the condition codes, and the external inputs.
• The outputs of the state machine are the control signals. The sequence of the
operation carried out by this machine is determined by the wiring of the logic
elements and hence named “hardwired”.
•   Fixed logic circuits that correspond directly to the Boolean expressions are used
to generate the control signals. • Hardwired control is faster than micro-
programmed control.
• A controller that uses this approach can operate at high speed.
• RISC architecture is based on the hardwired control unit
Characteristics:
• A Hard wired Control consists of two decoders, a sequence counter, and a
number of logic gates
• An instruction fetched from the memory unit is placed in the instruction
register (IR)
• The component of an instruction register includes I bit, the operation code, and
bits 0 through 11
• The operation code in bits 12 through 14 are coded with a 3 x 8 decoder
• The outputs of the decoder are designated by the symbols D 0 through D 7
********** 11 **********
--- page 12 ---
• The operation code at bit 15 is transferred to a flip flop designated by the
symbol I
• The operation codes from Bits 0 through 11 are applied to the control logic
gates
• The Sequence counter (SC) can count in binary from 0 through 15
Q7   a With the help of a neat diagram, explain the DMA controller and its operation.   10
CO4,   Compare DMA with interrupt-driven I/O.
BT2
Ans: [Diagram 2 marks]
Steps: [Explanation 4 marks]
1. Initialization
o CPU provides starting address, data size, and direction to DMA
2. DMA Request
o I/O device sends request (DRQ)
3. Bus Request
o DMA requests control of system bus from CPU
4. Bus Grant
o CPU grants bus and suspends its operation
5. Data Transfer
o DMA transfers data directly:
▪ Memory ↔ I/O device
6. Completion
********** 12 **********
--- page 13 ---
o DMA interrupts CPU after transfer completion
Comparison: 4Marks
CO1, b   i.   Explain the functions of the Bus Interface Unit (BIU) and the Execution   5
BT2   Unit (EU) in the 8086 microprocessors during instruction fetching and
execution. Why is the processor divided into these two units?
Ans:
Functions of BIU (Bus Interface Unit)   [2marks]
CO1,   • Fetches instructions from memory
BT2   • Handles address generation using segment registers   5
• Maintains instruction queue (6 bytes) for prefetching
•   Transfers data between CPU, memory, and I/O
Functions of EU (Execution Unit)   [2marks]
• Decodes and executes instructions
• Performs arithmetic and logical operations (ALU)
• Uses registers for computation
• Takes instructions from the instruction queue
During Instruction Execution
• BIU fetches instructions and stores them in queue
• EU takes instructions from queue and executes them
• Both units work simultaneously
Why Division into BIU and EU?   [1 marks]
✔ Enables pipelining (parallelism)
✔ Improves execution speed
✔ Reduces CPU idle time
✔ Increases overall efficiency
ii.   Explain the stored program concept and its significance in modern
computer systems.
Ans: [Explanation: 3marks]
The stored program concept is a fundamental idea in computer architecture
introduced by John von Neumann. It means that a computer’s instructions
(program) and data are stored together in the same memory.
Explanation
In this concept:
• A program is stored in the computer’s memory just like data.
********** 13 **********
--- page 14 ---
• The CPU fetches instructions one by one from memory, decodes them, and
executes them.
• This is known as the fetch–decode–execute cycle.
Earlier machines required manual rewiring to change programs, but with this
concept, programs can be changed simply by loading new instructions into
memory.
Significance in Modern Computer Systems [2 marks]
1. Flexibility
Computers can perform different tasks by loading different programs
without changing hardware.
2. Ease of Programming
Programmers can write, modify, and store programs easily in memory.
3. Foundation of Modern Architecture
It forms the basis of the Von Neumann Architecture, used in most
computers today.
4. Efficient Execution
Automatic execution of instructions improves speed and efficiency.
5. Supports Advanced Features
Enables multitasking, operating systems, and complex applications.
********** 14 **********
````
