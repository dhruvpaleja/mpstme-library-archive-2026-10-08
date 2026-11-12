# Microprocessor Systems and Interfacing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 2b2a292ac7c0

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_Mechatronics_7004/Microprocessor Systems and Interfacing/ANS_Microprocessor Systems and Interfacing(702MH0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Microprocessor Systems and Interfacing
Date: 08 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO1, SO1,   a. Describe the Von Neumann architecture and state any two limitations of using a   5
BL2   common memory for program and data.
The Von Neumann architecture is a stored-program computer architecture in
which both program instructions and data are stored in the same main memory, and
the CPU fetches both through the same communication path. It mainly consists of
a CPU, memory unit, input unit, and output unit, where the CPU includes the
Control Unit, ALU, and registers.
********** 1 **********
--- page 2 ---
In this architecture, the Control Unit fetches an instruction from memory, decodes
it, and the ALU performs the required arithmetic or logical operation. Since
instructions and data share the same memory and bus, the system follows the fetch-
execute cycle in a sequential manner.
Any two limitations of using common memory for program and data are:
•   It creates the Von Neumann bottleneck, because instructions and data
cannot be accessed simultaneously over the same bus.
• The CPU often must wait for memory transfers, which reduces overall
processing speed and throughput.research.ibm+2
CO2, SO1,   b.   Differentiate RISC and CISC architectures with any four suitable points.   5
BL2
Point   RISC   CISC
Instruction Uses a small and simple   Uses a large and complex
set   instruction set.   instruction set.
Instructions are usually fixed   Instructions are usually variable
Instruction
in length, which makes   in length, which makes
length
decoding easier.   decoding more complex.
Most instructions are designed Many instructions require
Execution
to execute in a single clock   multiple clock cycles for
time
cycle.   execution.
Can support memory-to-
Follows a load/store approach,
Memory   memory or register-to-memory
so arithmetic operations are
operation   operations within instructions.
mainly register to register.
stanford+1
Hardware is simpler and   Hardware is more complex and
Hardware
pipelining is easier to   pipelining is comparatively
design
implement.   harder.
Program size is generally   Program size is generally
Code size   larger because more simple   smaller because one complex
instructions are needed.   instruction can do more work.
CO3, SO1,   c.   Explain the PUSH and POP instructions of 8086 with one example each.   5
BL2
PUSH and POP can be explained as stack instructions used to store and retrieve 16-
bit data in the 8086 stack memory. The stack works with the stack segment and
stack pointer, and each PUSH or POP operation changes SP by 2 bytes because
8086 handles a word at a time in these instructions.
********** 2 **********
--- page 3 ---
PUSH instruction
The PUSH instruction stores a 16-bit register or memory content at the top of the
stack. During PUSH, the stack pointer is first decremented by 2, and then the word
is written at the memory location addressed by SS:SP.
Example:
MOV AX, 1234H
PUSH AX
In this example, the content of AX, that is 1234H, is pushed onto the stack, and SP
is reduced by 2.
POP instruction
The POP instruction removes the top 16-bit data from the stack and transfers it to
a register or memory location. During POP, the word from memory location SS:SP
is copied to the destination, and then SP is incremented by 2.
Example:
POP DX
If 1234H was previously on the top of the stack, after executing POP DX, the value
1234H is copied into DX and SP increases by 2.
CO2, SO1,   d. Explain the functions of the Program Counter (PC) and Data Pointer (DPTR) in the   5
BL2   8051 microcontroller, with one application of each.
In the 8051, the Program Counter (PC) is a 16-bit register that holds the address
of the next instruction to be fetched from program memory, while the Data Pointer
(DPTR) is a 16-bit register used to hold an address for data access, especially for
external data memory or table look-up operations. Both are essential because PC
controls program execution flow, whereas DPTR helps the microcontroller access
data beyond the normal 8-bit register range.
Program Counter
The Program Counter is a 16-bit register that always points to the next instruction
to be executed in program memory. After each instruction is fetched or executed,
the PC is automatically incremented, and after reset it starts from address 0000H.
The PC can also be changed by branch or jump instructions so that the program can
continue from another location in code memory.
Application: The PC is used during normal sequential program execution, for
example when the 8051 runs a control program step by step from ROM starting at
0000H.
********** 3 **********
--- page 4 ---
Data Pointer
The Data Pointer, or DPTR, is the only user-accessible 16-bit register in the 8051,
and it is formed by two 8-bit registers called DPH and DPL. Its main function is to
store a 16-bit address that points to data, commonly in external data memory or in
program memory during table access operations. DPTR is widely used with
instructions such as MOVX for external data memory access and MOVC for
reading constant data from code memory tables.
Application: DPTR is used in table look-up or LCD/message display programs,
where it points to a string or data table stored in memory and the 8051 reads bytes
one by one.
Q2   a. Compare Microprocessor architecture and Microcontroller architecture in [10]
CO1, SO1,   detail. Explain their memory organization, bus structure, speed, cost, flexibility,
BL2   and applications.
Microprocessor architecture Microcontroller architecture
Parameter   Microprocessor   Microcontroller
Mainly CPU on chip;
CPU, memory, and peripherals
Architecture memory and peripherals are
are integrated on a single chip.
usually external.
Uses external RAM, ROM,   Uses on-chip program memory
Memory   cache, and storage, so   and data memory, so memory
organization   system design is more   organization is compact and
expandable.   fixed.
Relies more on external   Internal buses connect CPU,
Bus   address, data, and control   memory, and peripherals within
structure   buses to connect memory   the same chip, reducing external
and I/O devices.   bus requirements.
Generally higher and   Usually lower than
Speed
suitable for complex   microprocessors, commonly
********** 4 **********
--- page 5 ---
processing, often operating   used for real-time control tasks
from MHz to GHz ranges.   in kHz to MHz ranges.
Overall system cost is
Lower cost because most
higher because external
Cost   required components are already
memory and interface
available on one chip.
components are needed.
Highly flexible, since   Less flexible, because the
Flexibility   memory and peripherals can   internal resources are fixed once
be expanded as required.   the chip is manufactured.
Higher power consumption
Lower power consumption and
Power   due to external components
often supports power-saving
consumption and higher processing
modes.
capability.
Used in embedded systems such
Used in personal computers,   as washing machines, traffic
Applications   laptops, servers, and high-   controllers, medical devices,
performance systems.   robotics, and automotive
control.
CO2, SO1,   b. Draw the pin configuration of the 8051 microcontroller and explain the functions
BL2   of Port 0, ALE & RST.   [10]
********** 5 **********
--- page 6 ---
Port 0
Port 0 consists of pins P0.0 to P0.7 and is located on pins 32 to 39. It is a
bidirectional I/O port, but unlike the other ports, it does not have internal pull-up
resistors, so external pull-ups are required when it is used as a normal I/O port.
Port 0 also has an alternate function as a multiplexed low-order address and data
bus, written as AD0 to AD7, during external memory interfacing. In such cases, the
same pins first carry the lower address byte and later carry data, which helps reduce
the total number of pins required in the 8051.
ALE
ALE stands for Address Latch Enable, and it is available at pin 30 of the 8051. Its
main function is to de-multiplex the address and data signals available on Port 0
when external memory is interfaced.
When the lower byte of the address appears on Port 0, ALE gives a high pulse to
latch that address into an external latch such as 74LS373 or 74HC573. After
********** 6 **********
--- page 7 ---
latching, Port 0 can then be used for data transfer, so ALE helps separate address
and data from the same port lines.
RST
RST is the reset pin of the 8051 and is located at pin 9. A high pulse applied to this
pin resets the microcontroller and brings it to its initial state.
On reset, the program execution starts from address 0000H, and the internal
registers are initialized to their default conditions. Thus, the RST pin is used during
power-on initialization and whenever the system needs to restart proper program
execution.
Q3   a. Design an 8086-microprocessor code to multiply two 8-bit numbers stored in
CO3, SO1,   memory and store the 16-bit result in memory; draw the flowchart and write the
BL5   program with proper comments.
1. Proper flowchart.   4
2. Code with proper comments for each step.   5
3. Role of DX register during operation.   1
CO2, SO1,   b. Explain the features of the Pentium processor in detail. Discuss its dual integer [10]
BL2   pipelines, split instruction and data caches, wider data bus, and improved
instruction throughput.
The Pentium processor introduced major architectural improvements over earlier
x86 processors by increasing parallel execution, improving memory access, and
raising data transfer bandwidth. Its important features include dual integer
pipelines, separate instruction and data caches, a 64-bit external data bus, and
mechanisms that improve instruction throughput.
Features
The Pentium is a CISC-based processor that also uses RISC-like internal
improvements for faster execution of common instructions. It supports superscalar
processing, improved pipelining, on-chip cache organization, floating-point
support, branch prediction, and better bus performance.
Important features of the Pentium processor are:
• Dual integer pipelines called U-pipeline and V-pipeline.
•   Separate 8 KB instruction cache and 8 KB data cache.
•   64-bit external data bus and 32-bit address bus.
•   Integrated and pipelined Floating-Point Unit.
• Branch prediction logic and prefetch buffers to reduce stalls.
********** 7 **********
--- page 8 ---
•   Better instruction throughput due to parallel execution and reduced cache
contention.
Dual pipelines
One of the most important features of the Pentium processor is its dual integer
pipelines, named U and V. These pipelines allow two instructions to be fetched,
decoded, and executed simultaneously if the instructions are pairable and
independent.
The U-pipeline is the main pipeline and can execute all integer instructions,
whereas the V-pipeline is meant mainly for simpler instructions. Because of this
arrangement, the Pentium can execute up to two integer instructions in one clock
cycle under suitable conditions, which significantly improves performance.
Split caches
The Pentium uses split L1 caches, with one 8 KB cache for instructions and another
8 KB cache for data. Both caches are two-way set associative, and this separation
allows instruction fetch and data access to occur simultaneously without competing
for a single cache resource.
This is an improvement over earlier unified-cache designs, where the processor
could suffer delays if code fetch and data access were requested at the same time.
By separating the code and data caches, the Pentium reduces pipeline stalls and
increases instruction flow efficiency.
Wider bus and throughput
The Pentium has a 64-bit external data bus, which is wider than the 32-bit external
data bus used in earlier 486 processors. This wider bus increases the amount of data
transferred in one bus cycle and improves memory bandwidth.
Because of the dual pipelines, split caches, prefetching, and wider data bus, the
Pentium achieves improved instruction throughput. It can keep the pipelines
supplied with instructions more effectively, reduce waiting time for memory, and
execute more instructions per unit time than earlier processors.
Q4   a. Explain block diagram of all the pins of 8237 DMA controller and its working [10]
CO4, SO1,   sequence of how it helps in faster data transfer between peripheral and memory.
BL2
********** 8 **********
--- page 9 ---
The 8237 is a programmable DMA controller used to transfer data directly between
an I/O device and memory without continuous CPU involvement, which makes
data transfer faster than programmed I/O.
The 8237 is a 40-pin IC with four DMA channels, and it contains internal address
and word-count registers for each channel to control DMA transfers. It operates in
slave mode while being programmed by the CPU and in master mode while
performing DMA transfer.
Pin functions
The DREQ0-DREQ3 pins are DMA request inputs from peripherals, and each one
corresponds to one DMA channel. The DACK0-DACK3 pins are DMA
acknowledge outputs that inform the selected peripheral that its request has been
accepted.
The HRQ pin is a hold request output sent by the 8237 to the CPU when the
controller needs control of the system bus for DMA transfer. The HLDA pin is the
hold acknowledge input from the CPU, indicating that the processor has released
the buses to the DMA controller.
The A0-A3 pins are used during programming to select internal registers, and
during DMA mode they output the lower address bits. The A4-A7 pins output
higher lower-byte address bits during DMA operation, while the upper address byte
is latched externally using control signals.
The DB0-DB7 pins form the bidirectional data bus used for programming the 8237
and for transferring the high-order address byte during DMA with external latching.
********** 9 **********
--- page 10 ---
The AEN signal enables the DMA address path and disables the normal CPU
buffers so the DMA controller can use the bus safely. The ADSTB signal is used to
latch the address from the data bus into an external latch during DMA operation.
The MEMR and MEMW signals control memory read and memory write
operations, while IOR and IOW control I/O read and I/O write operations during
transfer. The READY input allows wait states for slow memory or peripherals,
the CLK pin provides timing, and RESET initializes the controller and clears its
internal state. The CS, IOR, and IOW interface signals are also used when the CPU
programs the controller in slave mode.
Working sequence
First, the CPU programs the selected DMA channel by loading the starting memory
address, the word count, and the transfer mode into the 8237 registers. The word
count determines how many bytes are to be transferred, and the current address
register is automatically updated after each byte transfer.
When a peripheral is ready, it activates one of the DREQ lines to request DMA
service. The 8237 then checks priority, selects the active channel, and
sends HRQ to the CPU to request bus control.
After completing its current bus cycle, the CPU responds with HLDA, releasing the
system buses to the DMA controller. The 8237 now becomes bus master,
activates AEN, outputs the address, and acknowledges the peripheral using the
corresponding DACK line.
If the transfer is from I/O to memory, the controller activates IOR and MEMW so
data is read from the peripheral and written into memory. If the transfer is from
memory to I/O, it activates MEMR and IOW so data is read from memory and
written to the peripheral.
After each byte transfer, the current address register is incremented or decremented
as programmed, and the word count register is updated automatically. When the
programmed byte count is completed, the controller generates terminal count or
end-of-process indication and releases the bus by deactivating HRQ.
Why transfer is faster
DMA is faster because the actual data movement occurs directly between memory
and the peripheral, so the CPU does not waste time executing repeated read and
write instructions for every byte. This reduces CPU overhead, improves throughput,
and is especially useful for high-speed devices and block transfers.
********** 10 **********
--- page 11 ---
CO2, SO1,   b. Explain the internal RAM organization of the 8051 microcontrollers, including   [10]
BL2   register banks, bit-addressable area, and general-purpose RAM.
The internal RAM of the 8051 is organized into 128 bytes from address 00H to
7FH, and this space is divided into three main parts: register banks, bit-addressable
RAM, and general-purpose RAM. This organization makes the 8051 efficient for
fast register access, single-bit control operations, and temporary data storage.
The first 32 bytes from 00H to 1FH are reserved for four register banks, the next
16 bytes from 20H to 2FH form the bit-addressable area, and the remaining 80 bytes
from 30H to 7FH are used as general-purpose RAM.
Register banks
The 8051 has four register banks, and each bank contains eight 8-bit registers
named R0 to R7. Their address ranges are Bank 0: 00H-07H, Bank 1: 08H-0FH,
Bank 2: 10H-17H, and Bank 3: 18H-1FH.
Only one register bank is active at a time, and the active bank is selected by the
RS1 and RS0 bits of the Program Status Word register. By default, after reset, Bank
********** 11 **********
--- page 12 ---
0 is selected, so R0-R7 correspond to addresses 00H-07H unless the program
changes the bank selection.
Bit-addressable area
The RAM locations from 20H to 2FH form a 16-byte bit-addressable area. Since
each byte has 8 bits, this region provides 128 directly addressable bits, which is
very useful for flags, status bits, and control signals.
Individual bits in this area can be accessed by bit-level instructions such as SETB
and CLR without affecting the other bits in the same byte. This makes the 8051
especially suitable for embedded control applications where single-bit decisions are
common.
General-purpose RAM
The addresses from 30H to 7FH form the general-purpose RAM area, giving a total
of 80 bytes. This area is used to store temporary data, variables, intermediate
results, and sometimes the stack if the programmer relocates it there.
Unlike the bit-addressable region, this section is mainly used for normal byte-level
read and write operations. Because it is on-chip RAM, access is fast and convenient
for data manipulation during program execution.
Q5   a.   Construct and explain the logic for interfacing a common anode seven-segment   [10]
CO5, SO1,   display with any port of 8051 microcontroller. Also form a look up table to
BL2   display a number 0 to 9 on the seven-segment display.
********** 12 **********
--- page 13 ---
To interface a common anode seven-segment display with the 8051, the common
anode pin is connected to +5 V and the segment pins 𝑎 to 𝑔 are connected to any
8051 port pins through current-limiting resistors, so a logic 0 at a port pin turns a
segment ON and a logic 1 turns it OFF. For a 10-mark answer, you should show
the interfacing logic, explain the negative-logic operation, add a flowchart, and
provide the lookup table for digits 0 to 9.
In this circuit, each segment line is connected to one port pin through a resistor to
limit LED current. Because the display is common anode, all anodes are tied to +5
V, and the 8051 must provide a LOW signal to the required segment cathode in
order to glow that segment. Thus, the circuit works with negative logic, where 0
means ON and 1 means OFF.
Working
To display a decimal digit, the microcontroller sends a bit pattern to the selected
port so that only the required segments are driven LOW. For example, to display 0,
segments 𝑎, 𝑏, 𝑐, 𝑑, 𝑒, 𝑓 must glow and segment 𝑔 must remain OFF, so the
corresponding common-anode code is the complement of the usual common-
cathode pattern.
The program stores all segment patterns for digits 0 to 9 in a lookup table.
Whenever a number is to be displayed, the microcontroller reads the corresponding
code from the table and writes it to the output port.
Lookup table
The standard common-cathode codes for 0 to 9 are 3FH, 06H, 5BH, 4FH, 66H,
6DH, 7DH, 07H, 7FH, and 6FH. For a common anode display, the required codes
are the bitwise complements of these values, giving C0H, F9H, A4H, B0H, 99H,
92H, 82H, F8H, 80H, and 90H respectively.
Digit   Segments ON   Common anode hex code
0   a, b, c, d, e, f   C0H
1   b, c   F9H
2   a, b, d, e, g   A4H
3   a, b, c, d, g   B0H
4   b, c, f, g   99H
5   a, c, d, f, g   92H
6   a, c, d, e, f, g   82H
********** 13 **********
--- page 14 ---
7   a, b, c   F8H
8   a, b, c, d, e, f, g   80H
9   a, b, c, d, f, g   90H
CO3, SO1,   b. Explain in detail the following addressing modes of the 8086 microprocessors. For [10]
BL2   each addressing mode, give the definition, working principle, syntax, and suitable
examples.
(i)   Register addressing
(ii)   Register indirect addressing
(iii)   Indexed addressing.
(i) Register addressing
Definition: In register addressing mode, the operand is present in one of the 8086
registers named in the instruction. Both source and destination operands may be
registers in this mode.
Working principle: The CPU does not access memory for the operand data, because
the required data is already available inside the register specified by the instruction.
This makes register addressing one of the most compact and fastest addressing
forms in 8086.
Syntax: The general form is OPCODE destination_register, source_register.
Registers may be 8-bit or 16-bit general-purpose registers, except IP is not normally
used in this mode.
Examples:
MOV AX, BX copies the contents of BX into AX.
ADD AL, CL adds the contents of CL to AL.
(ii) Register indirect addressing
Definition: In register indirect addressing mode, the instruction specifies a register
that contains the offset address of the operand in memory. In 8086, registers
commonly used for this purpose are BX, BP, SI, and DI.
Working principle: The processor first reads the content of the specified register
and treats it as the effective address of the memory operand. It then accesses the
data from that memory location rather than taking the operand directly from the
register itself. By default, [BX], [SI], and [DI] use the DS segment, while [BP] uses
the SS segment.
********** 14 **********
--- page 15 ---
Syntax: The general form is OPCODE register, [BX], OPCODE register, [BP],
OPCODE register, [SI], or OPCODE register, [DI]. Brackets indicate that the
register content is used as a memory address.
Examples:
MOV AX, [BX] transfers a word from the memory location whose offset is stored
in BX into AX.
MOV DL, [SI] transfers a byte from the memory location pointed to by SI into DL.
(iii) Indexed addressing
Definition: In indexed addressing mode, the offset address of the operand is
obtained using one of the index registers, SI or DI. Some descriptions present it as
a special case of indirect addressing using index registers.
Working principle: The processor forms the effective address from the contents of
SI or DI, and in many cases a displacement may also be added to that index value.
Thus, indexed addressing is very useful for accessing elements of arrays, strings,
and tables stored in memory. For SI and DI, the default segment is generally DS,
though string operations use DS for SI and ES for DI in their standard forms.
Syntax: The common forms are OPCODE register, [SI], OPCODE register, [DI],
OPCODE register, [SI + displacement], and OPCODE register, [DI +
displacement]. Here the displacement may be 8-bit or 16-bit.
Examples:
MOV AX, [SI] moves the data from the memory location pointed to by SI into AX.
MOV AX, [DI+10H] accesses the memory location obtained by adding 10H to DI
and then loads that data into AX.
Q6   a. Explain the following,   [10]
CO3, SO1,   1. ADDC A, Rn,
BL2   2. DEC Rn,
3. INC DPTR,
4. DIV AB
5. SWAP A.
Instructions of the 8051 microcontrollers in detail. For each instruction, describe its
operation, syntax, effect on flags
1) ADDC A, Rn   2*5
********** 15 **********
--- page 16 ---
Definition: This is an add-with-carry instruction used in multi-byte addition. It adds
three values: accumulator content, register content, and the current carry flag.
Working: The operation is 𝐴←𝐴+ 𝑅𝑛+ 𝐶𝑌. The result is stored back in A.
Syntax: ADDC A, R
Flags: Carry, auxiliary carry, and overflow are affected by the addition result.
Example:
MOV A, #3AH
MOV R1, #25H
SETB C
ADDC A, R1
After execution, A = 60H.
2) DEC Rn
Definition: This instruction decreases the content of the selected register by 1. It is
commonly used in loop counters.
Working: The operation is 𝑅𝑛←𝑅𝑛−1. If the register contains 00H, it
underflows to FFH.
Syntax: DEC R
Flags: No flags are affected.
Example:
MOV R3, #22H
DEC R3
After execution, R3 = 21H.
3) INC DPTR
Definition: This instruction increments the 16-bit Data Pointer register by 1. DPTR
is the only user-accessible 16-bit register in the 8051 that can be incremented
directly by this instruction.
Working: The operation is 𝐷𝑃𝑇𝑅←𝐷𝑃𝑇𝑅+ 1. It is useful in table access and
external memory access.
Syntax: INC DPTR
Flags: No flags are affected.
Example:
MOV DPTR, #2050H
INC DPTR
After execution, DPTR = 2051H.
4) DIV AB
********** 16 **********
--- page 17 ---
Definition: This instruction divides the unsigned byte in accumulator A by the
unsigned byte in register B. It is used for arithmetic division operations in 8051
programs.uok+2
Working: The quotient is stored in A and the remainder is stored in B. If B = 00H,
the result is undefined, CY is cleared, and OV is set.
Syntax: DIV AB
Flags: CY is always cleared; OV is set only in divide-by-zero condition, otherwise
OV is cleared.
Example:
If A = FBH and B = 12H, then after DIV AB, A = 0DH and B = 11H because 251 =
13 × 18 + 17
5) SWAP A
Definition: This instruction swaps the upper 4 bits and lower 4 bits of the
accumulator. It is useful in BCD and hexadecimal digit manipulation.
Working: The high nibble of A becomes the low nibble and the low nibble
becomes the high nibble.
Syntax: SWAP A
Flags: No flags are affected.
Example:
If A = 3CH, then after SWAP A, A = C3H.
CO2, SO1,   b. Draw and explain the Bus Unit of the Pentium processor. Describe the functions of [10]
BL2   address drivers, data bus transceivers, bus control logic, write buffers.
********** 17 **********
--- page 18 ---
The Bus Unit of the Pentium processor provides the interface between the CPU and
external memory or I/O devices, and it is responsible for sending addresses,
transferring data, controlling bus cycles, buffering writes, handling bus ownership,
and checking parity for reliable communication. It is an important reason the
Pentium achieved higher external transfer performance, because it works with a 32-
bit address bus and a 64-bit data bus and supports both standard and burst transfers.
Address drivers
The address drivers and receivers place the address generated by the processor onto
the local address bus, typically using lines A31 to A3 along with byte enable signals
BE7 to BE0. Their function is to specify the exact external memory location or I/O
location involved in the current bus cycle.
During read or write operations, these drivers ensure that the correct address
reaches the external subsystem so that the targeted memory block or I/O device can
respond properly. Thus, address drivers are responsible for accurate addressing in
external communication.
Data bus transceivers
The data bus transceivers manage bidirectional data transfer between the Pentium
and external memory or I/O devices. Since the Pentium has a 64-bit data bus, these
transceivers allow a larger amount of data to move in one transfer compared with
older 32-bit designs.
When the processor performs a read cycle, the transceivers bring data from the bus
into the processor. During a write cycle, they place processor data onto the external
bus for memory or I/O devices.
Bus control logic
The bus control logic decides the type and timing of each bus cycle and generates
the required control signals for memory and I/O communication. It controls
whether the processor performs a standard bus cycle for I/O or non-cacheable
memory access, or a burst bus cycle for cache line fills and write-backs.
This logic improves performance because burst transfers allow several data items
to be transferred in sequence with lower overhead than separate single transfers.
Therefore, bus control logic is central to fast external communication in the
Pentium.
Write buffers
********** 18 **********
--- page 19 ---
The Pentium Bus Unit contains two 64-bit write buffers, one associated with each
execution pipeline. These write buffers temporarily store data that must be written
to memory, especially when a cache miss occurs or when the external bus is busy.
Because of these buffers, the execution pipelines do not always need to wait for the
write operation to complete on the external bus. This reduces pipeline stalls and
allows the processor to continue executing instructions while memory writes are
completed in the background.
Q7   a. Design an 8086 assembly language program to find the largest number from the [20]
CO3,   following data set and store the result in memory: 16H, 4AH, 2CH, 71H, 09H, 3EH,
SO1,   55H.
BL5   1. Draw a proper flowchart.   7
Add screenshots of the following performed in TASM software in a word file and
attach the printout in the paper.
8
a. Screenshot of the code with proper comments for each step
1
b. Number of counters required, and value loaded into each counter.
2
c. Data segment before and after sorting with memory address.
2
d. Output of Flag registers when number is smaller and when number greater.
********** 19 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 2b017f27ba76

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_Mechatronics_7004/Microprocessor Systems and Interfacing/ANS_Microprocessor Systems and Interfacing(702MH0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Microprocessor Systems and Interfacing
Date: 04 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO1, a. Explain in detail the differences between 8-bit and 16-bit microprocessor architectures.   5
SO1,
BL2
Feature   8-bit microprocessor   16-bit microprocessor
Word length   Processes 8 bits at a time.   Processes 16 bits at a time.
Typically performs 8-bit   Performs 16-bit arithmetic and
ALU size
arithmetic and logic in one step.   logic in one step.
16-bit wide in processors like
Usually 8-bit wide, so one
Data bus   8086, so one transfer can carry 2
transfer carries 1 byte.
bytes.
16-bit registers such as AX, BX,
Mostly 8-bit registers, with
Registers   CX, DX, plus 8-bit halves like
fewer large internal operands.
AH/AL.
Larger address space; 8086 uses
Address   Usually smaller address space in
20 address lines and can access 1
capability   typical 8-bit families.
MB.
Simpler instructions and less   Richer addressing modes and
Instruction
powerful addressing in many   stronger support for memory and
handling
classic designs.   I/O access.
Faster and more efficient for
Slower for large arithmetic and
Performance   larger data and program
data processing.
execution.
********** 1 **********
--- page 2 ---
CO2, b. Explain the role of BIU and EU in the 8086 microprocessors.   5
SO1,
BL2
In the 8086, the Bus Interface Unit (BIU) handles all communication with memory and
I/O devices, while the Execution Unit (EU) decodes and executes the instructions. Both
work simultaneously, which allows instruction fetching and execution to overlap and
improves performance through pipelining.
BIU role
The BIU is responsible for fetching instructions from memory, reading data from memory
and I/O ports, and writing data back to memory and I/O ports. It also generates the 20-bit
physical address needed by the 8086 to access memory.
The BIU contains the segment registers CS, DS, SS, and ES, along with the instruction
pointer and a dedicated adder for address generation. It also has a 6-byte instruction queue
that stores prefetched instructions, so the processor does not have to wait every time the
next instruction is needed.
EU role
The EU takes the instructions already fetched by the BIU, decodes them, and executes
them. It performs arithmetic, logic, comparison, and decision-making operations using the
16-bit ALU.
The EU contains the general-purpose registers AX, BX, CX, and DX, along with pointer
and index registers such as SP, BP, SI, and DI. It also updates the flag register after
execution, which helps in branching and control operations.
How they work together
The BIU and EU operate asynchronously in the 8086 architectures. While the EU is
executing the current instruction, the BIU can fetch upcoming instructions and place them
in the instruction queue.
This overlapping action is called pipelining, and it improves system speed and bus
utilization. In simple words, BIU brings the instructions and data, and EU does the actual
processing.
CO3,   c. Explain the ADD, SUB, and INC instructions of the 8086 microprocessors in detail. For   5
SO1,   each instruction, describe its operation, syntax, effect on flags
BL2
ADD instruction
The ADD instruction adds the source operand to the destination operand and stores the
result in the destination. It can be used with register, memory, and immediate operands of
the same size, and it also supports byte and word forms such as ADD AL, data8 and ADD
AX, data16.
Syntax includes forms such as ADD reg, reg, ADD reg, mem, ADD mem, reg, ADD reg,
data, ADD mem, data, ADD AL, data8, and ADD AX, data16. In simple form, the
operation is Destination = Destination + Source.
Example: ADD AX, BX means AX is replaced by AX + BX. Similarly, ADD AL,
05H adds 05H to AL and stores the result back in AL
SUB instruction
The SUB instruction subtracts the source operand from the destination operand and stores
the result in the destination. It also supports register, memory, and immediate forms,
including byte and word operations such as SUB AL, data8 and SUB AX, data16.
Syntax includes SUB reg, reg, SUB reg, mem, SUB mem, reg, SUB reg, data, SUB mem,
data, SUB AL, data8, and SUB AX, data16. Its basic operation is Destination =
Destination - Source.
Example: SUB AX, BX means AX is replaced by AX - BX. Another example is SUB AL,
02H, which subtracts 02H from AL and stores the result in AL.
********** 2 **********
--- page 3 ---
INC instruction
The INC instruction adds 1 to the destination operand. It can be used on an 8-bit register,
a 16-bit register, or a memory location.
Syntax includes INC reg8, INC reg16, and INC mem. Its operation is simply Destination
= Destination + 1.
Example: INC AX increases AX by 1, and INC BL increases BL by 1. If AX contains
1000H, after INC AX it becomes 1001H.
CO2, d. Explain in detail the functions of the Accumulator (A), B register, and in the 8051   5
SO1,   microcontrollers.
BL2
In the 8051, the Accumulator (A) is the main working register for arithmetic, logic, and
data transfer operations, while the B register mainly assists the accumulator during
multiplication and division and can otherwise be used as a temporary register. These two
8-bit registers are part of the CPU core and are central to most data-processing instructions
in the 8051.
Accumulator (A)
The Accumulator, also called ACC or register A, is an 8-bit multipurpose register. It holds
operands and results of ALU operations, so most arithmetic and logical instructions use A
directly.
Its main functions are:
• Holding one operand and the result during arithmetic operations such as addition
and subtraction.
• Taking part in logical operations like AND, OR, XOR, complement, rotate, and
swap.
• Acting as the primary register for data transfer between internal locations and, in
some cases, external memory.
•   Affecting status flags such as carry, overflow, auxiliary carry, and parity after
operations.
For example, in an instruction like ADD A, R1, the value in register R1 is added to the
Accumulator, and the result is stored back in A. This shows why the accumulator is called
the main working register of the 8051.
B register
The B register is also an 8-bit register, but it is more specialized than the accumulator. Its
most important role is to work together with the Accumulator during multiplication and
division operations.
Its main functions are:
•   In MUL AB, A and B are multiplied; the result is stored across both registers, with
A and B together holding the final product.
•   In DIV AB, A is divided by B; the quotient is stored in A and the remainder is
stored in B.
•   Serving as a scratch-pad or temporary storage register in other instructions when it
is not being used for multiply or divide operations.
• Supporting bitwise or temporary data handling when required in a program.
So, unlike A, the B register is not the default register for ordinary arithmetic and logic. It
becomes especially important only in instructions where the 8051 explicitly uses the pair
AB.
Difference between A and B
The accumulator is the primary data-processing register of the 8051, while the B register
is mainly a support register. Almost all arithmetic and logic instructions revolve around A,
but B is mainly reserved for multiply/divide and temporary storage.
********** 3 **********
--- page 4 ---
Q2   a. Compare Harvard architecture and Von Neumann architecture in detail. Explain their [10]
CO1,   memory organization, bus structure, speed, cost, flexibility, and applications, and justify
SO1,   which architecture is more suitable for embedded systems.
BL2
Aspect   Von Neumann   Harvard
Memory   One memory for both   Separate memory for instructions and
organization   instructions and data.   data.
Bus structure   Single shared bus.   Separate instruction and data buses.
Slower, due to shared-bus
Speed   Faster, due to simultaneous access.
contention.
Lower, because the design   Higher, because hardware is more
Cost
is simpler.   complex.
Higher, because memory is   Lower, because memory is fixed and
Flexibility
unified.   separate.
General-purpose computers, Embedded systems, DSPs,
Typical uses   desktops, laptops, and   communication systems, and real-
servers.   time controllers.
Explain all the above points in details.
CO2, b. Explain in brief with proper block diagram the internal architecture of 8086
SO1,   microprocessor.   [10]
BL2
Q3   a. Design an 8086-microprocessor code to convert the following number in data segment to
CO3,   it corresponding ASCII codes: 91H, store the result back in data segment.
SO1,   1. Draw a proper flowchart.   4
BL5   2. Write the code with proper comments for each step.   4
********** 4 **********
--- page 5 ---
3. State the role of flag register during operation.   2
CO2, b. Describe the need for cache architecture in the evolution of the Pentium processor. Explain [10]
SO1,   the memory bottleneck in early x86 systems and discuss the role of external cache, on-chip
BL2   cache, split caches, superscalar execution, and branch prediction in improving
performance.
The need for cache architecture in the evolution of the Pentium processor came from a
growing speed gap between the CPU and main memory: processors were getting faster,
but external memory access remained relatively slow, so the CPU often had to wait for
instructions and data. Cache reduced that waiting time by keeping frequently used
instructions and data in much faster storage close to or inside the processor.
Early bottleneck
Early x86 systems largely followed a Von Neumann style of operation in which instruction
fetch and data transfer compete for memory access, creating a shared-path bottleneck. In
such systems, the processor may need one phase to read the instruction and another to read
or write data, which limits throughput and leaves execution units underused.
As CPU clock rates increased, this memory bottleneck became a serious performance
problem because main memory could not supply instructions and data fast enough. This is
why cache memory became essential in later processor evolution.
Cache evolution
The first improvement was external cache, placed outside the CPU but closer and faster
than main memory. It acted as an intermediate layer, so frequently used code and data
could be served more quickly than from RAM, reducing average memory access time.
The next major step was on-chip cache, where cache memory was integrated directly on
the processor die. This made access even faster than external cache because signal travel
distance and interface delay were reduced.
Later designs also used split caches, meaning separate instruction cache and data cache.
This follows the advantage of Harvard-style separation, allowing the processor to fetch
instructions and access data in parallel rather than forcing them to compete for the same
path.
Pentium improvements
The Pentium improved performance not only with cache but also with superscalar
execution. Superscalar architecture allows more than one instruction to be executed in a
single clock cycle by using multiple execution units, which increases throughput when
enough instructions are ready.
However, superscalar execution only helps if the processor is fed with instructions and
data quickly enough, so cache architecture became a necessary support system for it.
Without fast cache, the extra execution units would spend time idle waiting for memory.
Another major improvement was branch prediction, which helps the processor guess the
likely path of branch instructions before the branch is fully resolved. This reduces pipeline
stalls and prevents frequent waiting during instruction flow, especially in pipelined and
superscalar processors.
Why cache mattered
The combined effect of external cache, on-chip cache, split instruction/data caches,
superscalar execution, and branch prediction was to keep the Pentium pipeline busy and
reduce wasted cycles. Cache reduced memory latency, split caches allowed simultaneous
instruction and data access, superscalar design increased parallel execution, and branch
prediction reduced control hazards.
In simple terms, Pentium performance improved because the processor was no longer
forced to wait so often for memory. Cache architecture was therefore a central part of
Pentium evolution, not just an extra feature, because it solved the main memory-speed
bottleneck that limited early x86 systems.
********** 5 **********
--- page 6 ---
Q4   a. Explain DMA data transfer using microprocessor with neat block diagram of 8237 DMA [10]
CO4,   controller and its working sequence.
SO1,
BL2
DMA data transfer is a method in which a DMA controller transfers data directly between
an I/O device and memory without the CPU moving each byte or word itself. This
improves speed and reduces CPU overhead because the microprocessor only gives control
of the buses and then resumes other work after the transfer is finished.
DMA concept
In a normal programmed transfer, the CPU reads data from an I/O device and then writes
it to memory, so the processor is busy for every transfer. In DMA, the DMA controller
takes temporary control of the address, data, and control buses and performs the transfer
directly between memory and the peripheral.
In systems using an 8086, the DMA controller requests the system bus through
HOLD/HLDA type handshaking so that the CPU can release bus control. Once the transfer
block is complete, the DMA controller returns control to the microprocessor.
Working sequence
The working sequence of DMA transfer using the 8237 is as follows.
1. An I/O device sends a DMA request on one of the DREQ lines to the DMA
controller.
2. The DMA controller sends HRQ or hold request to the CPU, asking for control of
the system buses.
3. The CPU responds with HLDA and releases the address, data, and control buses.
4. The DMA   controller acknowledges the requesting device using   the
appropriate DACK signal.
5. The DMA controller places the memory address on the address bus and generates
the necessary control signals such as memory read, memory write, I/O read, or I/O
write depending on the transfer direction.
6. Data is transferred directly between the I/O device and memory.
7. After each transfer, the address register is updated and the word count register is
decremented.
8. When the count reaches terminal count, the DMA transfer ends, the controller
releases the bus, and the CPU regains control.
********** 6 **********
--- page 7 ---
CO2, b. List the features of 8051 microcontroller also explain the timing and control unit of 8051   [10]
SO1,   microcontroller.
BL2
8051 features
The main features of the 8051 microcontroller are listed below.
•   8-bit CPU.
• 4 KB on-chip program memory.
• 128 bytes on-chip data memory.
•   Capability to address up to 64 KB external program memory and 64 KB external
data memory.
• 32 bidirectional I/O lines arranged as four 8-bit ports P0 to P3.
• Two 16-bit timer/counters.
•   Full-duplex serial transmitter/receiver.
• Four register banks.
•   8-bit program status word and stack pointer.
•   Interrupt structure with two priority levels.
• On-chip oscillator and clock circuits.
• Support for binary and decimal arithmetic.
• Power-saving mode.
These features make the 8051 useful for control-oriented applications where low cost,
moderate speed, and built-in peripherals are important.
Timing and control
The timing and control unit of the 8051 mainly works with the on-chip oscillator and clock
circuit. The oscillator generates clock pulses that synchronize all internal operations of the
microcontroller, and a quartz crystal is commonly used for this purpose.
The material states that the 8051 typically operates with oscillator frequencies from 1 MHz
to 16 MHz. These clock pulses drive the internal sequencing of fetch, decode, execute,
timer operation, serial communication, and interrupt handling.
Main functions
The control unit manages instruction execution by fetching instructions from program
memory, decoding them, and sending control signals to the ALU, registers, memory, and
I/O blocks in the correct order. It also controls data movement between internal RAM,
ROM, special function registers, timers, serial port, and external interfaces.
It supports external memory interfacing through signals such as ALE and PSEN. ALE is
used to demultiplex Port 0 address/data lines, while PSEN acts as the read strobe for
external program memory.
Machine cycle role
The timing unit defines machine-cycle behavior, which is important for timers and
counters. In the 8051, one machine cycle equals 12 oscillator periods, and timers increment
once per machine cycle when operating as timers, so the counting rate is one-twelfth of the
oscillator frequency.
For counter operation, external pulses are sampled in relation to machine-cycle timing, so
the timing unit also determines when external events are recognized. This precise
sequencing is what allows the 8051 to generate delays, count events, support serial baud-
rate generation, and respond to interrupts in a controlled manner.
Q5   a. Construct and explain the logic for interfacing a 4×3 matrix keyboard with 8051 [10]
CO5,   microcontroller. Also write an 8051-assembly language program to detect the pressed key.
SO1,
BL2
********** 7 **********
--- page 8 ---
A 4×3 matrix keyboard is interfaced to the 8051 by connecting its rows and columns to
port pins and then using a row-by-row scanning method to detect which key is pressed.
The microcontroller drives one row at a time and reads the column lines; when a key is
pressed, the active row gets electrically connected to one column, allowing the pressed key
to be identified from the row-column combination.
Interfacing logic
A 4×3 matrix keyboard has 4 rows and 3 columns, so only 7 I/O lines are required instead
of 12 separate lines. Since 8051 ports are bidirectional and can be used as input or output,
one practical arrangement is to connect the 4 row lines to four lower port pins and the 3
column lines to three upper port pins of the same port, commonly Port 1.
One suitable connection is:
• Row lines 𝑅1, 𝑅2, 𝑅3, 𝑅4 to P1.0, P1.1, P1.2, P1.3.
• Column lines 𝐶1, 𝐶2, 𝐶3 to P1.4, P1.5, P1.6.
Detection method
The scanning logic works in this sequence.
•   Initialize the port so row and column lines are in inactive state.
• Drive Row 1 low and keep the other rows high, then read the column lines.
•   If no column is active, drive Row 2 low and repeat.
• Continue similarly for Row 3 and Row 4.
• When a column is detected, combine the row number and column number to
determine the pressed key.
With proper diagram and code
CO3, b. Explain in detail the following addressing modes of the 8086 microprocessors. For each [10]
SO1,   addressing mode, give the definition, working principle, syntax, and suitable examples.
BL2   i.   Immediate Addressing
ii.   Direct Addressing
iii. Base Indexed Addressing
In the 8086, an addressing mode tells the processor how to locate the operand used by an
instruction, whether the operand is part of the instruction itself, stored at a fixed memory
location, or obtained by combining base and index registers. The three modes you asked
about are widely used because they cover constants, direct memory access, and array or
table access.
Immediate addressing
Definition: In immediate addressing, the actual operand value is given directly in the
instruction itself. The data may be 8-bit or 16-bit depending on the instruction.
Working principle: When the instruction is decoded, the processor reads the constant
value from the instruction bytes and uses it directly as the source operand. Since the
operand is already present in the instruction, no extra memory lookup is needed for the
data value itself.
Syntax:
• MOV reg, data
• ADD reg, data
• Example forms: MOV DL, 08H, MOV AX, 0A9FH
Examples:
• MOV DL, 08H loads the immediate 8-bit value 08H into register DL.
• MOV AX, 0A9FH loads the immediate 16-bit value 0A9FH into AX.
• ADD AX, 1234H adds the constant 1234H directly to AX.
This mode is very useful for initializing registers, loading constants, and performing
arithmetic with fixed values.
Direct addressing
********** 8 **********
--- page 9 ---
Definition: In direct addressing, the effective address of the memory location containing
the operand is written directly in the instruction. So the instruction directly specifies
where the operand is stored in memory.
Working principle: The processor takes the 16-bit offset given in the instruction as the
effective address. The physical address is then formed by combining the default segment
base with that offset, usually using DS for data access.
Syntax:
• MOV reg, [address]
• MOV [address], reg
• Example form: MOV BX, [1354H]
Examples:
• MOV BX, [1354H] copies the contents of memory location at offset 1354H into
BX.
• MOV AL, [2000H] copies the byte stored at offset 2000H into AL.
• MOV [2500H], AX stores AX into the memory location whose offset is 2500H.
This mode is suitable when the memory location of the operand is fixed and known in
advance.
Base indexed addressing
Definition: In base indexed addressing, the effective address is obtained by adding the
contents of one base register and one index register, and it may also include a
displacement. The base register is usually BX or BP, while the index register is SI or DI.
Working principle: The processor computes the effective address as the sum of base
register + index register + optional displacement. If BX is used as the base register, DS
is usually the default segment, while if BP is used, SS is used as the default segment.
Syntax:
• MOV reg, [BX + SI]
• MOV reg, [BX + DI]
• MOV reg, [BP + SI]
• MOV reg, [BP + DI]
• With displacement: MOV reg, [BX + SI + disp]
Examples:
• MOV DX, [BX + SI + 0AH] uses BX as base, SI as index, and 0AH as
displacement to form the effective address.
• The effective address in this example is EA = BX + SI + 000AH.
• The physical address is then obtained by adding this effective address to the
segment base, normally DS when BX is used.
This mode is very useful for arrays, tables, records, and matrix-type data structures
because one register can point to the start of the structure and the other can select an
element within it.
Q6   a. Explain the following,   [10]
CO3,   1. ADD A,direct
SO1,   2. ANL A,Rn
BL2   3. XRL A,#data
4. RRC A
5. MOVX A,@Ri
Instructions of the 8051 microcontrollers in detail. For each instruction, describe its
operation, syntax, effect on flags
In the 8086, addressing modes specify how an instruction finds its operand. For the three
modes you asked about, immediate addressing gives the data directly in the instruction,
direct addressing gives the memory offset directly in the instruction, and base indexed
********** 9 **********
--- page 10 ---
addressing forms the effective address by adding a base register, an index register, and
optionally a displacement.
Immediate addressing
Definition: In immediate addressing mode, the actual data itself is included as part of the
instruction. The operand is therefore a constant value, not a memory location.
Working principle: When the instruction is decoded, the CPU takes the immediate 8-bit
or 16-bit value from the instruction and loads or uses it directly. No separate memory
address calculation is needed for the source operand because the data is already present in
the instruction.
Syntax: Common forms are MOV reg, data, MOV mem, data, ADD AL, data8, and ADD
AX, data16.
Examples
• MOV DL, 08H stores the immediate 8-bit value 08H into DL.
• MOV AX, 0A9FH stores the immediate 16-bit value 0A9FH into AX.
• ADD AL, 25H adds immediate data 25H to AL.
Direct addressing
Definition: In direct addressing mode, the effective address of the memory operand is
written explicitly in the instruction. The instruction directly specifies the offset of the
operand in memory.
Working principle: The CPU takes the 16-bit displacement given in the instruction as the
effective address. For normal data access, the physical address is formed by adding this
offset to the base address from the data segment, so Physical Address = (DS × 10𝐻) +
EA.
Syntax: The common form is MOV reg, [address] or MOV [address], reg.
Examples:
• MOV BX, [1354H] copies the word stored at offset 1354H into BX.
• MOV BL, [0400H] copies the byte stored at offset 0400H into BL.
Here the square brackets mean “contents of memory at this address,” not the address value
itself. This mode is called direct because the displacement from the segment base is directly
specified in the instruction.
Base indexed
Definition: In base indexed addressing mode, the effective address is obtained by adding
a base register, an index register, and usually a displacement. The base register is BX or
BP, and the index register is SI or DI.
Working principle: The CPU computes the effective address as
𝐸𝐴= (Base Register) + (Index Register) + Displacement
If BX is used as base, the default segment is DS, and if BP is used as base, the default
segment is SS. After finding the effective address, the physical address is obtained by
adding it to the corresponding segment base.
Syntax: Typical forms are:
• MOV reg, [BX + SI]
• MOV reg, [BX + DI + disp]
• MOV reg, [BP + SI + disp]
• MOV reg, [BP + DI + disp]
Example:
• MOV DX, [BX + SI + 0AH] uses BX as base, SI as index, and 0AH as
displacement.
CO2, b. Explain the branch prediction logic, superscalar and super-pipelined architecture and [10]
SO1,   Instruction Prefetching and Decoding of the Pentium processor with its significance.
BL2
********** 10 **********
--- page 11 ---
The Pentium improved performance by combining branch prediction, superscalar
execution, super-pipelining, and instruction prefetch/decode so that the processor could
keep more instructions flowing to the execution units with fewer stalls. These features
were significant because they increased instruction throughput, reduced waiting caused by
memory and branches, and made better use of the processor’s parallel hardware.
Branch prediction
Branch prediction logic is used to guess the outcome of branch instructions before the
actual branch condition is fully resolved. This helps the Pentium continue fetching and
preparing the most likely next instructions instead of stopping the pipeline at every
conditional jump.
Its significance is that it reduces pipeline stalls and wasted clock cycles. Since branch
instructions can break the normal sequential flow of execution, prediction helps maintain
continuous instruction flow and improves overall processor efficiency.
Superscalar design
The Pentium introduced superscalar architecture, which allows more than one
instruction to be executed in a single clock cycle. This is done by using multiple execution
paths or pipelines so that independent instructions can be processed in parallel.
Its significance is higher throughput. Instead of completing only one instruction per cycle
in the ideal case, the processor can complete multiple instructions when dependencies and
resource conflicts do not block parallel execution.
Super-pipelining
Super-pipelined architecture means the instruction processing path is divided into more,
shorter stages so that each stage does less work per clock cycle. This allows the processor
to operate at a higher clock frequency and overlap more instruction activities at the same
time.
Its significance is improved speed because several instructions can be in different stages
of execution simultaneously. In practice, this increases instruction throughput, but it also
makes penalties from branch misprediction more important, which is why branch
prediction becomes essential.
Prefetch and decoding
The Pentium uses an instruction queue to store prefetched instructions before execution.
The material states that this queue is a FIFO buffer and that the Pentium uses a 32-byte
instruction queue, larger than much older processors such as the 8086.
Instruction prefetching means the processor fetches instructions from memory in advance
so the execution units do not have to wait every time a new instruction is needed. Decoding
then interprets the opcode and determines how the instruction should be sent to the
available execution pipelines.
Its significance is threefold:
•   It reduces memory latency by keeping instructions ready near the execution stage.
•   It supports parallel execution in the Pentium’s multiple pipelines.
•   It works with branch prediction to reduce disruption from control-transfer
instructions.
Combined impact
These mechanisms are most effective when they work together. Prefetching keeps
instructions available, decoding prepares them for execution, superscalar architecture
allows multiple instructions to run in parallel, super-pipelining overlaps more stages of
work, and branch prediction prevents frequent breaks in the flow.
As a result, the Pentium can use its hardware more efficiently and achieve much better
performance than earlier processors that executed instructions more sequentially. This is
why these architectural features are considered core reasons for the Pentium’s speed
improvement.
********** 11 **********
--- page 12 ---
Q7   a. Design an 8086-microprocessor code to sort following numbers in ascending order:   [20]
CO3,   Numbers: 3FH, 1DH, 5AH, 2EH, 7BH, 19H, 4CH
SO1,   1. Draw a proper flowchart.   7
BL5   Add screenshots of the following performed in TASM software in a word file and attach
the printout in the paper.
a. Screenshot of the code with proper comments for each step   8
b. Number of counters required, and value loaded into each counter.   1
c. Data segment before and after sorting with memory address.   2
d. Output of Flag registers when number is smaller and when number greater.   2
1. Draw a proper flowchart.
One possible solution with proper screen shots
********** 12 **********
````
