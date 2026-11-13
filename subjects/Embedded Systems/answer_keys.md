# Embedded Systems: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 0f14d3d032ec

- Departments: Information Technology
- Programmes: BTech IT 7001, Integrated IT 7037, MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_IT_7001/Embedded Systems/ANS_Embedded Systems(702IT0C015)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 26 Nov 2025
- Text: mixed (12 pages), mean OCR confidence 91.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester IX/Semester V(Exam Year: 2025-2026)
Subject: Embedded Systems
Date: 26 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume suitable data if neccessary
Q1   Answer briefly:   [20]
CO-1;   a.   List and briefly describe the constraints under which embedded systems typically operate.   [5]
SO-2 ;   Constraint   Description
BL-1   1. Performance   The system must meet specific timing requirements
Constraint   (real-time deadlines, response time) and throughput
goals.
2. Power   Embedded systems often run on batteries or limited
Constraint   power; energy efficiency is critical (low-power
processors, sleep modes).
3. Memory   Limited RAM/ROM availability requires compact
Constraint   code and optimized memory usage.
4. Cost   System cost must remain low; impacts choice of
Constraint   components, packaging, and production volume.
5. Size / Space   Physical footprint of hardware should be minimal—
Constraint   important in portable and wearable systems.
6. Reliability and   The system must operate reliably under environmental
Safety Constraint   and electrical stress; crucial for automotive, medical,
and industrial systems.
7. Real-Time   Many embedded systems must guarantee deterministic
Constraint   behavior within strict timing deadlines.
CO-1;   b.   Explain the layered architecture of an embedded system with a neat diagram.   [5]
SO-2 ;   Layers:
BL-1
1. Hardware Layer:
o   Includes processor, memory, I/O ports, timers, sensors, and actuators.
o   Performs basic hardware functions.
2. System Software Layer:
o   Contains device drivers and RTOS.
o Manages hardware resources and controls task execution.
o Middleware Layer:
1.   Provides libraries or communication protocols.
2. Helps applications use hardware easily.
3.   Application Software Layer:
o   Includes user programs that perform control or data-processing functions.
o   Example: motor speed control, sensor monitoring.
o   User Interface Layer (optional):
1.   Provides display or keypad for user interaction.
********** 1 **********
--- page 2 ---
CO-1;   c.   Differentiate between Hard Real-Time Operating Systems (RTOS) and Soft Real-Time Operating   [5]
SO-2 ;   Systems with respect to task deadlines, scheduling behavior, and system response. Support your
BL-2   answer with suitable examples from embedded applications.
Feature   Hard Real-Time Operating   Soft Real-Time Operating System
System (RTOS)   (RTOS)
Task Deadlines   Deadlines are strict — missing   Deadlines are flexible — occasional
a deadline can cause system   delays are acceptable.
failure.
Scheduling   Uses deterministic scheduling   Uses priority-based or round-robin
Behavior   like Rate Monotonic (RMS) or   scheduling, not all tasks are
Earliest Deadline First (EDF)   guaranteed to meet deadlines.
to ensure all tasks meet
deadlines.
System Response   Predictable and must respond   Variable response time; performance
within a fixed time bound.   degrades gracefully under load.
Reliability   Very high — used in safety-   Moderate — used where delay affects
Requirement   critical systems.   quality, not safety.
Examples   Airbag controller, pacemaker,   Multimedia player, smart thermostat,
industrial robotic arm.   mobile OS task scheduling.
CO-2;   d.   Explain the major challenges in embedded system design related to power dissipation, flexibility,   [5]
SO-2   ;   and reliability. Support your answer with suitable examples from real-time embedded applications.
BL-3
Embedded systems face several key design challenges that affect their performance and
lifetime:
Challenge   Explanation   Example
1. Power   Embedded systems often run on   Example: Wearable fitness tracker
Dissipation   battery power or limited energy   or wireless sensor node.
sources. Designers must reduce
power consumption using low-
power processors, sleep modes,
and efficient algorithms.
2. Flexibility   Systems should be adaptable to   Example: IoT controller with
design changes, feature updates, or   firmware update capability.
different applications without full
redesign. Hardware–software
partitioning and reconfigurable
devices (like FPGA) help achieve
flexibility.
3. Reliability   Systems must work continuously   Example: Automotive ECU or
and correctly under varying   medical monitoring device.
conditions such as temperature,
noise, and voltage changes. Fault-
tolerant hardware and error-
checking software improve
reliability.
********** 2 **********
--- page 3 ---
Q2   A   Classify embedded systems based on functionality and performance requirements. Explain each   [10]
CO-1;   category — stand-alone, real-time (hard and soft), networked information appliances, and mobile
SO-2;   devices — with one suitable example for each.
BL-3;
Embedded systems are classified based on their functionality and performance requirements into the
following categories:
1️. Stand-alone Embedded Systems
•   Operate independently without connecting to other systems.
•   Take input from sensors or switches and control hardware outputs directly.
•   Generally designed for a specific function.
Example: Washing machine controller, microwave oven.
2. Real-Time Embedded Systems
•   Must produce correct output within a fixed time limit (deadline).
•   Timing is critical; missing a deadline can affect performance or safety.
a) Hard Real-Time Systems
•   Missing a deadline leads to system failure.
Example: Airbag control unit, pacemaker.
b) Soft Real-Time Systems
•   Occasional deadline misses are acceptable, though performance degrades.
Example: Multimedia player, smart home lighting control.
3. Networked Embedded Systems
•   Connected to a communication network (wired or wireless).
• Can send or receive data for monitoring or control.
Example: Smart meter connected to the IoT network, industrial automation system.
4.   Mobile Embedded Systems
•   Small, portable, and battery-powered systems.
•   Designed for high performance with low power consumption.
Example: Smartphone, digital camera.
Q2   B   Explain the factors that influence the selection of a microcontroller (MCU) for an embedded   [10]
CO-2;   system design.
SO-2;   The selection of a microcontroller depends on several hardware and application-related factors
BL-4;   that affect system performance and cost.
•   Performance Requirements:
The MCU should meet the speed, response time, and computation needs of the system.
High-speed MCUs are used for real-time and signal-processing tasks.
• Memory Requirements:
Adequate RAM, ROM, and Flash memory are needed for code, data, and buffers.
Complex applications or RTOS-based designs need more memory.
• Power Consumption:
Important for battery-powered systems. Low-power MCUs with sleep modes and clock
scaling are preferred for portable or IoT devices.
•   Input/Output Capabilities:
The number and type of ports (GPIO, ADC, DAC, UART, SPI, I2C) determine
hardware interfacing options with sensors and peripherals.
********** 3 **********
--- page 4 ---
•   Cost and Availability:
The MCU should be cost-effective and easily available. Vendor support and supply
reliability are also key.
•   Packaging and Size:
The MCU must fit the mechanical design and available space, especially for compact
embedded products.
•   Development Tools:
Good support for IDEs, compilers, debuggers, and simulators helps in faster
development and easier testing.
•   Special On-chip Features:
Built-in peripherals such as timers, PWM, communication modules, and watchdog
timers improve integration and reduce external components.
Q3   A   Analyze   the   hardware   architecture   of   an   embedded   system.   [10]
CO-1;   Explain how the different building blocks work together to ensure the system’s functionality and
SO-2;   reliability. Support your answer with a neat labeled diagram.
BL-4;   The hardware architecture of an embedded system consists of several interconnected building
blocks that perform sensing, processing, control, and communication tasks.
•   1. Processor (Microcontroller or Microprocessor):
The main control unit that executes instructions, performs computations, and manages
all system operations.
Example: ARM Cortex-M, 8051, AVR.
•   2. Memory Unit:
Stores program code and data.
o ROM/Flash: For permanent program storage.
o RAM: For temporary data and stack operations.
o EEPROM: For retaining user data or configurations.
•   3. Input/Output Interfaces:
Connect the processor with external devices such as sensors, actuators, and user
interfaces.
Includes serial interfaces like UART, SPI, I²C, USB, and GPIO ports.
•   4. Sensors and Actuators:
o Sensors detect physical parameters (temperature, light, pressure).
o Actuators convert electrical signals into mechanical actions (motors, relays).
•   5. Power Supply Circuit:
Provides regulated voltage and current to all components.
Includes converters and battery management for energy efficiency.
•   6. Clock and Timing Circuit:
Generates precise timing signals for the processor and peripherals.
Ensures synchronization and predictable execution.
•   7. Watchdog Timer:
Monitors system operation and resets the processor if it hangs or fails to respond.
Improves system reliability and fault recovery.
•   8. Communication Interface:
Enables data exchange with other systems or networks (e.g., Ethernet, CAN, Zigbee,
Bluetooth).
Q3   B   Develop a UML-based model for an embedded application smart home temperature controller.
CO-3;   Identify the key classes, states, and interactions, and justify how the UML model helps achieve
SO-2;   design clarity and modularity.
[10]
BL-5;
********** 4 **********
--- page 5 ---
Why UML helps (Justification)
•   Clarity: separates structure (classes) and behavior (states, interactions)
•   Modularity: independent components enable reuse and testing
•   Traceability: requirements map to classes & states; easy impact analysis
•   Collaboration: common language for HW/SW teams; supports code generation &
documentation
•   Extensibility: easy to add modes/devices via new classes and states
Q4   A   Explain the working of Round Robin Scheduling and Preemptive Fixed Priority Scheduling used [10]
CO-1;   in   real-time   operating   systems.
SO-2;   Discuss how each algorithm handles task execution, prioritization, and response time in a real-
BL-4;   time environment. Support your answer with suitable timing diagrams and examples.
********** 5 **********

[Text in pictures on this page, read by OCR]
Sensor State Diagram Sequence Diagram

readTemp() ( Idle ») ,
calibrate() User Display | |Controller) | Sensor
T
' f
1 i
1 f

timer/clock ! setTemp!
ji
Comparing! 1 ‘update | H
Deciding

Heater Cooler id isetspoint | '
bei et heater/cooler cmd odaren
Actuating ‘em temp !

PowerManager | SystemClock optional ne
sleep() [tick Maintaining | showSta '
i} 1 ' 1

SystemClock optional |__neck();

1
tick() Fault / Recovery i 1 !

Sequence Diagram

Round-robin scheduling
Same as SCHED_FIFO but with timeslices

Among tasks of equal priority:
+ Rotate through all tasks
+ Each task gets a fixed time slice

+ Only a higher priority SCHED_FIFO or SCHED_RR task can preempt a SCHED_FIFO Time
+ Tasks of equal priority preempt each other after timeslice expiration
--- page 6 ---
Q4   B   Evaluate different codesign methodologies (traditional vs. modern integrated approaches) in terms [10 ]
CO-2;   of   flexibility,   verification   efficiency,   and   risk   of   late-stage   failures.
SO-2;   Provide justified recommendations for selecting an appropriate methodology in large-scale
BL-5;   embedded project.
Evaluate: Traditional (Sequential) vs Modern Integrated Codesign
•   Flexibility
o   Traditional: Low. HW fixed early; late HW changes are costly; SW adapts
around HW limits.
o   Integrated: High. Concurrent HW/SW partitioning; executable specs; easy
design-space exploration; IP reuse and re-targeting.
•   Verification Efficiency
o   Traditional: Late, siloed verification; HW verified first, SW later; interface
bugs discovered at integration time; limited co-simulation.
o   Integrated: Early and continuous verification; HW/SW co-sim, virtual
prototypes; unified testbenches; requirements traceability; fewer re-spins.
•   Risk of Late-Stage Failures
o   Traditional: High. Interface mismatches, unmet performance/power targets
discovered late; schedule slips.
o   Integrated: Low–Moderate. Early visibility of timing, throughput, latency, and
power; continuous integration reduces surprise defects.
Key Practices in Modern Integrated Approach (as per “Typical/Conventional vs Ideal
Codesign Environment”)
• Common, executable system specification shared by HW and SW
•   Unified languages and shared design databases; re-usable IP blocks
•   Early HW/SW partitioning with rapid iteration; model-based design
•   Co-simulation, FPGA prototyping, and formal checks throughout
•   Toolchain cross-fertilization: synthesis tools, shared verification assets
Recommendations for Large-Scale Embedded Projects
•   Prefer a modern integrated codesign methodology with:
▪   Executable specs and model-based design for early behavior validation
▪ HW/SW co-design flow with co-simulation and virtual prototypes
▪   Unified repositories (shared DB), version control, and CI pipelines
▪   Requirements traceability from use-cases → models → RTL/firmware → tests
▪   Early FPGA prototyping for performance/power validation before tape-out
▪   IP reuse strategy and standardized interfaces to cut cycle time
•   Use the traditional sequential approach only when:
▪   Scope is small, requirements are stable, and HW IP is pre-frozen
▪   Time-to-first-demo is critical and risks are low
•   Governance checklist to minimize late failures:
▪   Define measurable targets (latency, throughput, power) in the spec
▪   Enforce interface contracts and auto-generated stubs from the model
▪   Gate reviews tied to co-sim results and coverage metrics
▪   Plan risk-burn-down via early prototypes and incremental integration
********** 6 **********
--- page 7 ---
Q5   A   Propose an optimized embedded software development strategy that balances power efficiency,   [10]
CO-3;   real-time performance, and maintainability. Justify how the use of high-level programming
SO-2;   languages (C/C++) and source-code engineering tools can enhance productivity and system
BL-6;   reliability.
Strategy — Power Efficiency
•   Use interrupt-driven design; avoid busy-wait loops; batch I/O to reduce wakeups
•   Enable MCU low-power modes, DVFS, peripheral gating; adopt tickless RTOS where
applicable
•   Offload with DMA and smart peripherals (timers, PWM, ADC with FIFO) to let CPU
sleep
•   Minimize memory traffic (cache-friendly data, fixed-point where suitable); compress or
table-lookups for constants
•   Schedule energy-aware: group high-power tasks, defer non-critical work
Strategy — Real-Time Performance
•   Choose a small RTOS with fixed-priority preemption; assign priorities from
rate/deadline analysis
• Bound latency: short ISRs, defer work to tasks; use lock-free/FIFO queues where
possible
•   Control priority inversion (inheritance/ceiling); keep critical sections minimal
•   Measure WCET and jitter; size stacks; use tracing to verify deadlines (context-switch,
run-time, IRQ latency)
•   Partition time-critical paths from housekeeping; use double-buffering for I/O
Strategy — Maintainability
•   Layered architecture: App → Services/Middleware → HAL/Drivers → BSP
•   Pure C APIs for drivers/HAL; encapsulate hardware in modules; configuration via
tables, not #ifdef sprawl
•   Finite-state machines for control logic; publish-subscribe/event queues for decoupling
•   Coding standards (MISRA-C/C++), self-documenting names, Doxygen headers
•   Regression safety nets: unit tests (on host), HIL tests (on target), Traceability from
requirements → tests
Build/Release Workflow
•   Single source of truth build (CMake or Make); reproducible versions; per-commit
version stamp
•   Git + code review; CI on host (compile, unit tests, static analysis); nightly target builds
and HIL smoke tests
•   Feature flags and safe rollback; crash logs and watchdog-guarded recovery
Why C/C++ (Productivity + Reliability)
•   Direct control of memory, timing, and peripherals with zero-cost abstractions (C++) for
clarity without overhead
•   Vast ecosystem: compilers, debuggers, profilers, RTOS ports, and device libraries
•   Strong type system (C++) reduces defects; RAII for deterministic resource release in
drivers/services
•   Templates and constexpr enable compile-time checks/config without run-time cost
Why Source-Code Engineering Tools
•   Static analysis catches null/overflow/UB early
•   Sanitizers on host fuzzing for parsers/protocols; cyclomatic complexity gates
********** 7 **********
--- page 8 ---
•   Unit test frameworks with mocks for drivers; coverage tracking
•   Trace/profiling to verify deadlines and locate hotspots
•   Formatters (clang-format) and linters keep codebase uniform; Doxygen auto-docs
support onboarding
• Lower energy per function (sleep more, offload more), bounded latency with verified
deadlines, and a modular codebase that scales safely across features and hardware
variants.
Q5   B   Explain the cross-platform development process used in embedded systems, highlighting the   [10]
CO-1;   interrelationship between the Host system and the Target system. Describe each stage of
SO-2;   development and support your answer with a neat labeled diagram.
BL-4;
The cross-platform development process in embedded systems involves designing and testing
software on a Host System (usually a PC) and then running it on a Target System (the actual
embedded hardware).
This approach helps in faster development, testing, and debugging before deploying on the real
device.
1.   Interrelationship between Host and Target Systems
•   Host System:
o The developer’s workstation used to write, compile, simulate, and debug
embedded code.
o   Contains development tools like compilers, assemblers, linkers, and debuggers.
•   Target System:
o The embedded hardware platform where the final executable runs.
o   Includes microcontroller, memory, peripherals, and real-time interfaces.
•   The Host and Target communicate through a serial port, JTAG, or Ethernet for code
download and debugging.
2. Stages of Cross-Platform Development
•   a) Code Development (on Host):
Developers write code in C or C++ using an IDE or text editor.
•   b) Cross-Compilation:
The code is compiled using a cross-compiler, which generates executable code for the
Target’s processor (e.g., ARM GCC for ARM MCU).
•   c) Linking and Building:
Object files are linked with libraries to create the final binary (e.g., .hex or .bin
file).
•   d) Downloading to Target:
The binary is transferred to the Target via serial, JTAG, or USB using tools like Flash
programmers.
•   e) Testing and Debugging:
The developer debugs on the Host using tools that communicate with the Target through
emulators or in-circuit debuggers.
•   f) Integration and Validation:
The final application is validated under real operating conditions to ensure correct
timing, performance, and reliability.
Q6   A   Explain the roles of User Mode and Supervisory (Kernel) Mode in an embedded operating system.   [10]
CO-1;   Discuss how mode switching ensures system security, predictability, and performance in real-time
SO-2;   environments.
BL-4;
********** 8 **********
--- page 9 ---
User Mode (Unprivileged Mode)
• Runs application-level code such as user tasks and processes.
• Has limited access to system resources — cannot directly access hardware or critical
memory regions.
•   Interacts with hardware only through system calls to the kernel.
•   Protects system integrity by isolating faults caused by user programs.
•   Example: Temperature monitoring task, display update function.
Supervisory / Kernel Mode (Privileged Mode)
•   Executes critical system operations like task scheduling, interrupt handling, and
memory management.
• Has full access to CPU registers, I/O devices, and memory.
• Manages context switching, interrupt service routines (ISRs), and device drivers.
•   Example: RTOS kernel executing the scheduler or handling an interrupt.
Mode Switching Process
•   The CPU switches between User Mode and Kernel Mode through system calls or
interrupts.
•   System Call: User task requests kernel service (e.g., read sensor data → kernel executes
driver function).
•   Interrupt: Hardware signal triggers kernel mode to handle time-critical events.
•   After service completion, control returns to User Mode.
Benefits of Mode Switching
•   Security:
o   Prevents user tasks from corrupting kernel data or hardware registers.
o   Protects memory and I/O spaces through privilege separation.
•   Predictability:
o   Kernel handles interrupts and real-time scheduling deterministically.
o   Ensures consistent response times for time-critical events.
•   Performance:
o Only essential operations run in Kernel Mode; others run in User Mode to
reduce overhead.
o   Context switching is optimized to maintain real-time deadlines.
Q6   B   Implement the following Boolean functions using a PLA:   [10]
CO-2;   F1(A,B,C)=Σ(0,1,2,4)
SO-2;   F2(A,B,C)=Σ(0,5,6,7)
BL-6;
1. Obtain minimized SOP expressions for F1 and F2 (use K-maps or equivalent) and
identify shared product terms. (3M)
2. Specify the PLA specification table (input polarities, product terms, output mapping).
(2M)
3. Draw the PLA programming matrix/connection diagram, indicating which AND and OR
fuses are intact/blown. (3M)
4. State the minimum number of product terms required and justify your choice. (2M)
********** 9 **********
--- page 10 ---
Q7   A   Explain the process of hardware–software partitioning in embedded system codesign. Discuss how   [10]
CO-2;   partitioning decisions affect performance, cost, and development time, and illustrate your answer
SO-2;   with a suitable example.
BL-5;
1️. Definition
•   Hardware–Software Partitioning is the process of dividing system functionality
between hardware (custom logic, processors, FPGA, ASIC) and software (programs
running on a processor).
•   The goal is to achieve an optimal balance between performance, cost, and
development time.
2️. Process of Partitioning (from your slides)
•   a) System Specification:
Define the complete system behavior and requirements (performance, cost, power,
reliability).
•   b) Task Identification:
Break the design into smaller functions or modules (e.g., signal processing,
communication, control).
•   c) Partition Analysis:
Evaluate each function — decide whether it should be implemented in hardware or
software based on speed, area, and flexibility.
•   d) Design Space Exploration:
Simulate different HW/SW combinations to find the best trade-off.
•   e) Integration and Verification:
Combine both hardware and software components and verify through co-simulation or
emulation.
3️. Factors Influencing Partitioning Decisions
********** 10 **********

[Text in pictures on this page, read by OCR]
A

BC B

oo 01 1 10

1 1 0 1

1 0 0 0

Cc
P= A’B! + AIC’ + BIC’
Fy =(AB+ AC + BC)'

A

BC B
00 01 i110

1 0 0 0

0 1 1 1

c
F,= AB + AC+ A'BIC!
F,=(A'C+A'B+ BIC)’
--- page 11 ---
•   Performance:
o Hardware gives faster execution and deterministic timing.
o   Software offers flexibility but slower execution.
o Example: Time-critical DSP tasks → Hardware; Control logic → Software.
•   Cost:
o Hardware (FPGA, ASIC) increases unit cost.
o   Software implementation reduces cost through reusability and easier updates.
•   Development Time:
o Hardware design takes longer due to synthesis and testing.
o   Software can be developed and modified quickly.
o A hybrid approach ensures faster prototyping and reliable results.
4️. Example (from your slides)
Digital Camera System:
• Image capture and compression → Implemented in hardware for real-time speed.
•   User interface, storage control, and communication → Implemented in software for
flexibility.
•   Result: High-speed image processing with user-friendly adaptability.
Q7   B   Compare CPLD and FPGA in terms of their architecture, configurability, and application areas.   [10]
CO-3;   Explain how these differences influence their selection and performance in embedded system
SO-2;   design.
BL-6;
1️. CPLD (Complex Programmable Logic Device)
•   Consists of a limited number of logic blocks (macrocells) connected through a
predictable, fixed interconnect structure.
•   Non-volatile configuration memory — retains logic even after power-off.
•   Configuration is done using AND–OR arrays similar to PLAs.
•   Offers deterministic timing due to fixed routing paths.
• Lower density and speed, suitable for simpler control and interface logic.
Architecture Summary:
•   Block-based, hierarchical (function blocks + global interconnect).
•   Non-volatile configuration (EEPROM/Flash).
2️. FPGA (Field Programmable Gate Array)
•   Contains thousands of Configurable Logic Blocks (CLBs) interconnected via a
flexible routing matrix.
•   Uses volatile configuration memory (SRAM-based) — requires reloading at power-
up.
•   Supports parallelism and high-speed operations.
•   Highly suitable for signal processing, computation, and complex control.
Architecture Summary:
•   Array of logic blocks with lookup tables (LUTs), flip-flops, and routing channels.
•   Volatile configuration; programmable through bitstreams.
********** 11 **********
--- page 12 ---
Feature cPLD FPGA

Architecture Fewer macrocells with fixed interconnects Thousands of CLBs with reconfigurable
routing

Configuration Memory Non-volatile (EEPROM/Flash) Volatile (SRAM, needs reloading)

Timing Behavior Deterministic, predictable Non-deterministic, depends on routing

Logic Density Low to medium Very high

Speed Moderate High (supports parallelism)

Power Consumption Lower Higher

Reconfiguration Limited Flexible and dynamic

Typical Use Glue logic, address decoding, interface DSP, image processing, communication
control systems

FRR ICR] DA KH
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper eb393a1caf02

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_IT_7001/Embedded Systems/ANS_Embedded Systems(702IT0C015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Embedded Systems
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume suitable data if neccessary
Q   Answer briefly:   [20
1
]
a. Define an embedded system. Discuss how factors such as memory limitation, power consumption, and real-   [5]
time deadlines affect its design.
Sol:
• Embedded System Definition:
An embedded system is a special-purpose computer built to perform a dedicated function within a larger
system.
It combines hardware and software to operate in real-time under given constraints.
Example: Washing machine controller, pacemaker, or automotive ECU.
• Memory Limitation:
Embedded systems often have limited RAM and ROM.
Software must be optimized to use minimal memory.
Efficient algorithms and data handling are needed to fit within hardware limits.
• Power Consumption:
Many embedded systems run on batteries or low-power sources.
Designers use low-power processors, sleep modes, and efficient clock management to reduce energy use.
Power optimization increases battery life and reliability.
•   Real-Time Deadlines:
Systems must respond within a defined time limit.
Real-time scheduling and interrupt handling ensure deterministic responses.
Missing deadlines can cause functional failure in critical applications.
********** 1 **********
--- page 2 ---
b   Differentiate between CISC and RISC processor architectures based on their instruction set, register usage,   [5]
.   and design philosophy. Support your answer with suitable examples.
c. Explain the different task states in a real-time operating system and describe how a task transitions between   [5]
these states during execution.
• A task is the basic building block of software in an RTOS and is usually a subroutine.
•   The RTOS starts a task by specifying its corresponding subroutine, priority, stack etc.
•   The task can have 3 states :-
1. Running – The task code is currently being executed by the microprocessor. Except in multi-
processor systems, only one task is in running state.
2. Ready – The task is waiting to execute but another task is currently running.
3. Blocked – The task cannot run even if the microprocessor is free. It might be waiting for an
external event or a response. e.g. a push-button task stays blocked until the button is pushed.
•   Most RTOSs have other states like suspended, waiting, dormant etc. but these are just sub-divisions
of one of the three states above.
********** 2 **********

[Text in pictures on this page, read by OCR]
Feature CISC (Complex Instruction Set Computer) RISC (Reduced Instruction Set Computer)

Instruction Set Large set of complex instructions; each can Small set of simple instructions; each performs
perform multiple operations. one basic operation.

Instruction Length Variable length; some instructions take Fixed length; most instructions execute in one
many cycles to execute. clock cycle.

Register Usage Fewer general-purpose registers; heavy Many general-purpose registers; minimizes
dependence on memory. memory access.

Design Philosophy Hardware complexity; microcoded control Simplified hardware; hardwired control; focus
unit; focus on reducing code size. on speed and pipelining.

Performance Slower execution; more cycles per Faster execution; efficient instruction pipeline.
instruction.

Examples Intel x86, Motorola 68000. ARM, MIPS, PowerPC.
--- page 3 ---
d   Describe the role of device drivers in embedded systems.   [5]
.   Explain how architecture-specific and generic drivers differ in managing hardware components.
•   Device Driver Definition: A device driver is a specialized software component that acts as an
interface between the operating system (or application software) and hardware devices in an
embedded system. It allows software to access hardware functions without needing to know the low-
level hardware details.
•   Role of Device Drivers in Embedded Systems:
• Enable communication between software and hardware components.
• Abstract hardware complexity, allowing application code to be hardware-independent.
• Handle low-level operations such as reading/writing registers and managing interrupts.
• Support initialization, configuration, data transfer, and power management of peripherals.
• Improve system modularity and portability by separating hardware control from application logic.
• Example: UART driver for serial communication, SPI driver for sensors, GPIO driver for LEDs.
•   Architecture-Specific Drivers:
• Written for a particular processor or microcontroller architecture (e.g., ARM Cortex-M, AVR).
• Directly manipulate hardware registers, memory-mapped I/O, and interrupt lines.
• Provide optimal performance because they are tightly coupled to the hardware.
• Depend on processor-specific addressing, instruction sets, and peripheral structures.
• Example: STM32 UART driver using vendor HAL library or ARM CMSIS-based peripheral driver.
•   Generic Drivers:
• Platform-independent and designed to work across multiple architectures with minor modifications.
• Use standardized APIs or abstraction layers provided by the OS (e.g., POSIX, Linux kernel
interfaces).
• Focus on portability and reusability rather than raw performance.
• Typically rely on underlying architecture-specific layers for direct hardware access.
• Example: Generic USB or network driver framework in Linux that supports multiple hardware
platforms.
Q A   •   Classify embedded systems based on microcontroller performance as small-scale, medium-scale, and   [10
sophisticated systems. Explain each category with features, microcontroller type, and one real-world
2   ]
application example showing where it is used.
Embedded systems are classified based on microcontroller performance and application complexity into three
types: small-scale, medium-scale, and sophisticated embedded systems.
•   Small-Scale Embedded Systems:
• Use low-end 8-bit or 16-bit microcontrollers.
• Designed for simple and dedicated operations with limited memory and peripherals.
• Programs are written in C or assembly and stored in on-chip ROM or Flash.
• Operate with low power and minimal hardware complexity.
• Typically do not use an operating system and rely on simple looping or interrupt-based logic.
• Microcontroller Examples: 8051, PIC16F877A, AT89C51.
• Application Example: Digital thermometer, automatic streetlight, or simple home appliance
controller.
•   Medium-Scale Embedded Systems:
• Use 16-bit or 32-bit microcontrollers or microprocessors.
• Perform moderately complex tasks and often support multitasking.
• May use a real-time operating system (RTOS) for scheduling and resource management.
• Include more memory and advanced peripherals like ADCs, UARTs, and communication ports.
• Suitable for applications requiring both performance and flexibility.
• Microcontroller Examples: ARM Cortex-M series, AVR32, MSP430.
• Application Example: Smart washing machine, industrial process controller, portable medical
devices.
•   Sophisticated Embedded Systems:
• Use high-performance 32-bit or 64-bit processors or SoCs.
• Capable of executing multiple complex tasks simultaneously.
• Run full-fledged embedded operating systems such as Linux, Android, or QNX.
• Include features like Ethernet, USB, Wi-Fi, and graphics interfaces.
********** 3 **********
--- page 4 ---
• Require high memory, storage, and advanced hardware-software integration.
• Processor Examples: ARM Cortex-A series, Intel Atom, Raspberry Pi SoC.
• Application Example: Automotive ECU, smart surveillance camera, or drone control system.
Q B   Explain the role of Digital Signal Processing (DSP) in embedded systems. Analyze how the integration of DSP   [10
2   techniques enhances the performance, precision, and functionality of real-time embedded applications. Support   ]
your answer with suitable examples.
Digital Signal Processing (DSP) is used in embedded systems to process real-world analog signals that have
been converted into digital form. It involves mathematical operations such as filtering, transformation, and
compression to extract useful information or modify signals for specific purposes.
❖ Role of DSP in Embedded Systems:
• Enhances system capability to handle audio, video, sensor, and communication signals in real time.
• Performs operations like filtering, modulation, spectral analysis, and signal compression.
• Used in applications requiring fast, repetitive, and high-precision mathematical processing.
• Executes complex algorithms (like FFT, FIR, IIR) directly on embedded hardware.
• Reduces noise, improves data accuracy, and ensures reliable real-time output.
• DSP chips or integrated DSP cores are often embedded alongside microcontrollers for efficiency.
❖ Integration of DSP Techniques – Performance Enhancement:
• Performance: Dedicated DSP cores execute multiply–accumulate (MAC) operations efficiently,
offering faster response in real-time systems such as speech and image processing.
• Precision: Fixed-point or floating-point arithmetic enables accurate signal computation with
minimal quantization error.
• Functionality: Enables complex processing like adaptive filtering, predictive control, and sensor
fusion within embedded environments.
• Efficiency: Parallel pipelines and specialized instruction sets in DSPs reduce processing latency.
• Optimization: Hardware-level DSP integration minimizes CPU load and improves throughput.
❖ Examples of DSP in Embedded Applications:
• Audio Processing: Noise suppression, echo cancellation, equalization in Bluetooth headsets or
hearing aids.
• Image and Video Processing: Edge detection, image enhancement, and object tracking in smart
cameras.
• Communication Systems: Modulation/demodulation, error correction, and signal decoding in
mobile or IoT networks.
• Industrial Control: Vibration and condition monitoring using real-time signal analysis for
predictive maintenance.
• Biomedical Devices: ECG and EEG filtering and feature extraction for patient monitoring systems.
❖ Analysis Summary:
Integration of DSP techniques in embedded systems improves computational speed, signal accuracy,
and functional intelligence. It enables real-time systems to achieve deterministic performance,
making them more efficient, responsive, and adaptable to complex signal-driven environments.
Q   •   Explain how the Real-Time Operating System (RTOS) and Application Software together constitute the   [10
software architecture of an embedded system. Describe how their interaction supports task scheduling,
3 A   ]
context switching, and ensures system reliability.
•
•   The software architecture of an embedded system is typically layered, consisting of the Application
Software, RTOS kernel, hardware abstraction layer, and device drivers. The RTOS and Application
Software together form the main functional core that enables real-time operation and reliability.
•   Role of RTOS in Software Architecture:
• Acts as the control center that manages processor time, memory, and resources among multiple tasks.
• Provides essential services such as task scheduling, inter-task communication, synchronization, and
interrupt handling.
• Ensures deterministic response by allowing high-priority tasks to pre-empt lower ones.
• Facilitates modular software design by separating time-critical kernel functions from application logic.
********** 4 **********
--- page 5 ---
•   Role of Application Software:
• Consists of user-defined tasks and functions designed to fulfill system-specific requirements.
• Runs on top of the RTOS, using its APIs for communication, timing, and resource access.
• Each task represents a functional unit, such as sensor reading, motor control, or display update.
• Application software depends on the RTOS for timing accuracy and task coordination.
•   Interaction between RTOS and Application Software:
• The RTOS schedules and manages tasks created by the application.
• Each task transitions through states such as ready, running, waiting, or suspended under RTOS control.
• System calls and APIs connect the application layer to the kernel for services like semaphores, message
queues, and timers.
• Interrupts are handled by the RTOS, which triggers the corresponding application task or ISR.
• Context switching performed by the RTOS saves and restores CPU states to switch between tasks
without losing data or state.
•   Support for Task Scheduling and Context Switching:
• RTOS uses priority-based or round-robin scheduling to allocate CPU time efficiently.
• Context switching ensures smooth transfer between tasks, maintaining system responsiveness.
• The kernel manages stack and register storage during task switching to avoid data corruption.
•   Ensuring System Reliability:
• Fault isolation prevents one malfunctioning task from affecting others.
• Watchdog timers and health monitoring tasks enhance fault recovery.
• Synchronization mechanisms (mutexes, semaphores) prevent race conditions and resource conflicts.
• Deterministic execution ensures timely completion of safety-critical operations.
•   The RTOS provides time management, multitasking, and resource control, while the Application
Software implements system functionality. Their coordinated interaction ensures predictable timing,
modularity, and reliability in real-time embedded systems.
Q B Develop a UML-based model for an embedded application automatic door lock system. Identify the key   [10
3   classes, states, and interactions, and justify how the UML model helps achieve design clarity and modularity.   ]
How UML helps design clarity and modularity (Justification):
• Separation of concerns: classes isolate authentication, actuation, sensing, UI, and timing, simplifying
reasoning and testing
• Traceable behavior: state diagram maps policy (timeouts, retries, tamper) to explicit states/transitions,
reducing ambiguity
• Reusable components: AuthModule, LockActuator, DoorSensor can be reused across other access-control
products
• Change-friendly: adding a new credential (e.g., NFC) or mode (visitor access) only extends interface
classes and state transitions, leaving core logic intact
********** 5 **********
--- page 6 ---
• HW/SW codesign alignment: clear interfaces between controller and drivers (LockActuator, DoorSensor)
support HAL/RTOS layering from your slides
• Verification readiness: scenarios from the sequence diagram become test cases (normal open/close, invalid
PINs, lockout, tamper)
Example mapping to RTOS tasks (optional alignment):
• Tasks: InputTask (keypad/RFID), ControlTask (state machine), ActuatorTask (lock), UITask
(display/buzzer), LoggerTask, Watchdog/TimerTask
• RTOS services: message queues for events, timers for auto-relock, mutex for shared log
Q A Explain Real-Time Scheduling in embedded systems and its role in executing periodic tasks within deadlines.
4   Discuss the working of Earliest Deadline First (EDF) and Round Robin scheduling algorithms with suitable
timing diagrams.
[10
]
Q B   Evaluate how cross-fertilization between hardware and software design—using synthesis tools, unified [10
4   languages, and shared databases—improves the efficiency of embedded system development. Also state the key   ]
requirements of an ideal codesign environment that enable such integration.
********** 6 **********

[Text in pictures on this page, read by OCR]
EDF Scheduling

Earliest Deadline First (EDF) scheduling
* Simple, yet effective

+ Whichever task has next deadline gets to run

Deadline: 5 Deadline: 8 [Tsk | Deadline: 12
Exec time: 4 Exec time: 3 Exec time: 2

+ Theory exists to analyze such systems

Time ° ts ts

te

Round Robin Scheduling

Round-robin scheduling
‘Same as SCHED_FIFO but with timeslices

Among tasks of equal priority:
* Rotate through all tasks
+ Each task gets a fixed time slice

* Only a higher priority SCHED_FIFO or SCHED_BR task can preempt a SCHED_FIFO Time
+ Tasks of equal priority each other after ti
--- page 7 ---
Cross-fertilization in embedded system design refers to the close collaboration and overlap between
hardware and software development activities to achieve faster, more efficient, and optimized system design.
How cross-fertilization improves design efficiency:
• Concurrent Development: Hardware and software can be designed, simulated, and verified in parallel
rather than sequentially, reducing overall design time.
• Use of Unified Languages: High-level specification languages (like SystemC, VHDL-AMS, Verilog-AMS,
UML) describe both hardware and software behavior, improving communication and reducing design
ambiguity.
• Synthesis Tools Integration: Automated synthesis tools convert high-level system descriptions into
hardware (RTL) and software (C/C++/firmware) components, ensuring consistency and faster
implementation.
• Shared Databases: Unified design repositories maintain common specifications, timing data, interface
definitions, and test vectors accessible by both hardware and software teams, ensuring design traceability and
version control.
• Improved Verification and Validation: Co-simulation environments verify hardware and software
behavior together, identifying integration issues early and minimizing late-stage rework.
• Design Reuse and Scalability: Standardized interfaces and reusable IP blocks simplify porting designs
across platforms and reduce future development costs.
• Optimized Performance: Partitioning and iterative refinement between hardware and software enable the
most efficient use of resources such as speed, area, and power.
Key Requirements of an Ideal Codesign Environment:
• Unified Specification Model: A single executable specification for both hardware and software to ensure
consistency and shared understanding.
• Common Design Database: Central repository for design data, IP libraries, timing constraints, and
documentation accessible to all design tools.
• Integrated Synthesis and Simulation Tools: Tools that allow automatic synthesis, co-simulation, and
performance evaluation of hardware and software components.
• Seamless Hardware–Software Partitioning: Capability to explore multiple design alternatives, move
functions between hardware and software, and assess trade-offs dynamically.
• Standardized Communication Interfaces: Support for common protocols (e.g., AMBA, SPI, I2C) and
reusable interface models for interoperability.
• Support for Reuse and Scalability: Modular design and IP reuse support across projects and platforms.
• Automatic Verification Support: Built-in testbench generation, co-simulation, and debugging features for
early integration testing.
• Cross-Team Collaboration Tools: Shared dashboards and documentation tools enabling real-time
coordination between hardware and software engineers.
Cross-fertilization between hardware and software through synthesis tools, unified modeling languages, and
shared databases transforms the design flow into an integrated, concurrent process. It minimizes development
time, enhances design accuracy, and leads to better performance and reliability. An ideal codesign
********** 7 **********
--- page 8 ---
environment supports this integration with unified specifications, tool interoperability, and strong verification
support.
Q A Evaluate how system calls enable communication between application programs and the operating system in   [10
5   embedded environments. Discuss how improper system call management can affect system performance and   ]
reliability.
System calls are special functions provided by the operating system that allow application programs to
request specific services from the kernel.
In embedded systems, they serve as a controlled interface between user-level applications and system-level
resources such as hardware devices, memory, and peripherals.
Role of System Calls in Embedded Environments:
• Provide a secure and standardized way for applications to access OS resources without directly manipulating
hardware.
• Enable essential operations such as process management, task scheduling, file access, communication, and
interrupt handling.
• Support real-time constraints by allowing applications to request deterministic services (e.g., task delay,
event wait, semaphore control).
• Ensure isolation between user tasks and kernel operations, preventing user code from corrupting system
data.
• Simplify application development by abstracting low-level details and exposing clear APIs.
• Examples of system calls in embedded RTOS: osDelay(), osSemaphoreWait(), osMessageQueuePut(),
read(), write().
How System Calls Enable Communication:
• When an application invokes a system call, it triggers a software interrupt (SWI) or trap instruction that
transfers control to the kernel in supervisory mode.
• The kernel executes the requested service (e.g., allocate memory, read sensor data, start a timer).
• Once completed, control returns to the application in user mode with the result or status code.
• This mechanism ensures safe, controlled communication between user applications and system-level
services.
Impact of Improper System Call Management:
• Increased Latency: Excessive or poorly timed system calls can cause frequent context switches, increasing
task response time and violating real-time deadlines.
• Resource Contention: Uncontrolled access to shared resources (files, devices, or buffers) through system
calls can lead to race conditions and deadlocks.
• Kernel Overhead: Repeated calls to non-critical services burden the CPU, lowering system throughput.
• Security Risks: Mismanaged calls may allow unauthorized access to protected memory or device registers.
• Memory Leaks: Failing to release OS-allocated resources after system calls (e.g., semaphores, queues)
degrades performance over time.
• Reduced Reliability: Unchecked return values or improper error handling can cause unpredictable behavior
or system crashes in safety-critical applications.
Good System Call Practices in Embedded Systems:
• Use minimal and optimized system calls in real-time tasks to reduce kernel transition overhead.
• Validate all parameters before invoking system calls to prevent illegal access or null references.
• Group related system calls logically to minimize switching and improve performance.
********** 8 **********
--- page 9 ---
• Implement proper error handling, timeout mechanisms, and watchdog monitoring for robust operation.
• Profile and optimize system call usage during real-time testing to ensure predictable behavior.
Evaluation Summary:
System calls form the vital communication bridge between applications and the OS kernel in embedded
systems, ensuring safe and structured access to hardware and services. Proper management of system calls
maintains determinism, performance, and security, whereas poor management can lead to latency,
instability, and reliability failures in real-time embedded environments.
Q B   Explain the sequence of steps involved in creating an executable image for an embedded system. Discuss how [10
5   the compiler, assembler, linker, and locator collectively transform source code into a target-specific binary   ]
image. Support your answer with a labeled diagram showing the relationship between host and target systems.
In embedded systems, the software development process involves generating a target-specific executable
image on a host computer, which is later downloaded to the target hardware for execution.
The toolchain used includes the compiler, assembler, linker, and locator, which work together to produce
the final binary.
Step 1: Source Code Creation (on Host System)
• Developers write high-level source code in C or C++ using an IDE or text editor.
• Code includes application logic, hardware drivers, and RTOS functions.
• Example: main.c, sensor.c, motor.c.
Step 2: Compilation
• The compiler translates high-level C/C++ code into assembly language instructions specific to the target
processor architecture.
• Performs optimizations, syntax checking, and generates intermediate files (.asm or .obj).
• Example: ARM GCC or Keil compiler generates ARM assembly code.
Step 3: Assembly
• The assembler converts the assembly instructions into machine code (object files with .o or .obj
extensions).
• Produces symbol tables and relocatable object code.
• Each source file becomes one object file, ready for linking.
Step 4: Linking
• The linker combines multiple object files into a single executable file.
• Resolves external symbols, function calls, and global variables used across different modules.
• Links with standard libraries (e.g., math, RTOS kernel, device drivers).
• Produces a partially complete executable known as an absolute object file (.elf or .axf).
Step 5: Location and Image Generation
• The locator (also called the linker-locator) assigns physical memory addresses to the program segments
(code, data, stack, heap).
• Generates the final binary/hex image that matches the target’s memory map.
• Output formats include .bin, .hex, or .srec, ready for download to Flash or ROM.
Step 6: Downloading to Target System
• The final image is transferred from the host system to the target hardware via interfaces such as JTAG,
********** 9 **********
--- page 10 ---
UART, or USB.
• A bootloader or programmer writes the image into the target’s memory for execution.
Step 7: Execution and Debugging
• Once loaded, the target processor executes the image.
• Debuggers (GDB, Keil μVision) on the host allow step-by-step verification, breakpoints, and memory
inspection.
Q A Explain the concept of priority inversion in real-time embedded systems. Describe how it affects task scheduling [10
6   and system performance, and discuss suitable techniques used to minimize or prevent this problem.   ]
• Priority inversion occurs when a high-priority task is indirectly blocked by a low-priority task because
the low-priority task holds a shared resource that the high-priority task needs. Meanwhile, medium-priority
tasks may preempt the low-priority one, causing the high-priority task to wait longer.
• Example:
• Task T1 – High Priority (needs shared resource)
• Task T2 – Low Priority (holding that resource)
• Task T3 – Medium Priority (independent but preempts T2)
Here, T3 delays T2, which in turn delays T1, creating an inversion of priorities.
• Effects on Task Scheduling and System Performance:
• Causes high-priority tasks to miss deadlines, breaking real-time constraints.
• Reduces system predictability and determinism.
• Increases response latency and context-switching overhead.
• May cause task starvation when medium-priority tasks keep preempting the lower one.
• Degrades system reliability and performance in safety-critical systems like automotive ECUs or robotic
control.
• Techniques to Minimize or Prevent Priority Inversion:
• Priority Inheritance Protocol (PIP):
The low-priority task holding the resource temporarily inherits the priority of the highest-priority task waiting
for it, preventing medium-priority preemption.
• Priority Ceiling Protocol (PCP):
Each shared resource is assigned a ceiling priority equal to the highest task priority that can access it. A task
can only lock a resource if its priority is higher than the current ceiling, preventing deadlocks and bounding
blocking time.
• Immediate Ceiling Protocol (ICPP):
When a task locks a resource, it immediately executes at the ceiling priority until it releases the resource,
ensuring no other task can preempt it.
• Non-blocking Design Approaches:
Use lock-free algorithms, message queues, or event-driven designs to minimize resource sharing.
• Watchdog Monitoring:
Detects and logs priority inversion cases during execution for system tuning.
• Practical Example:
In an automotive braking ECU, a low-priority diagnostic task holding a bus resource can delay a high-priority
braking control task. Applying priority inheritance allows the diagnostic task to complete quickly, restoring
real-time responsiveness.
• Summary:
Priority inversion disrupts real-time scheduling by allowing lower-priority tasks to block critical ones.
Techniques such as priority inheritance and priority ceiling protocols ensure bounded blocking time,
improved predictability, and higher reliability in real-time embedded systems.
********** 10 **********
--- page 11 ---
Q B Implement the following Boolean functions using a suitable PAL.   [10
6   Let inputs be x,y,z(both true and complemented forms available).   ]
A(x,y,z)=Σ (1,2,4,6)
B(x,y,z)=Σ(0,1,6,7)
C(x,y,z)=Σ(2,6)
Tasks (show working):
i.   Obtain minimized SOP for A,B,C, (K-maps or equivalent) and identify shared product terms across
the four outputs. (3M)
ii.   Prepare the PAL specification table: list product terms, their input literals, and map them to outputs
A,B,C. (2M)
iii.   Draw the PAL programming matrix/connection diagram (AND/OR planes), clearly indicating
intact/blown fuses (or marked connections). (3M)
iv.   State the minimum number of product terms your design uses and justify how sharing was achieved.
(2M)
********** 11 **********
--- page 12 ---
Q   Describe the Hardware–Software Codesign flow from system specification to integration and testing. Explain [10
7 A how concurrent and integrated development of hardware and software improves design quality and reduces   ]
iteration effort.
Hardware–Software Codesign is an integrated design methodology in which hardware and software
components are developed concurrently from a unified system specification. It aims to achieve optimal
performance, cost, and time efficiency for embedded systems.
Codesign Flow — Step-by-Step Process:
• 1. System Specification:
The design begins with defining overall system requirements — functionality, timing, power, cost, and
performance goals.
A unified, high-level executable specification (using UML, SystemC, or MATLAB models) describes both
hardware and software behavior.
• 2. System Partitioning:
The system functions are divided between hardware (to improve performance or meet timing constraints) and
software (for flexibility and cost efficiency).
Design space exploration evaluates different partition alternatives to achieve optimal trade-offs.
• 3. Hardware Design:
Hardware blocks identified from partitioning are implemented using HDL (VHDL/Verilog/SystemVerilog).
Synthesis tools generate gate-level circuits and optimize area, speed, and power.
Hardware prototypes (FPGA or simulation) validate timing and functionality.
• 4. Software Design:
Software components (RTOS, drivers, application logic) are developed in parallel using C/C++ or assembly.
Tasks are implemented, tested, and profiled on virtual platforms or simulators before real hardware is ready.
• 5. Co-Simulation and Verification:
Hardware and software modules are simulated together using co-simulation tools (e.g., ModelSim, QEMU, or
SystemC).
This stage detects interface mismatches, synchronization issues, and timing violations early.
• 6. Integration:
Hardware (FPGA/ASIC) and software (firmware, drivers, RTOS) are integrated on the target platform.
Communication interfaces, buses, and interrupts are validated for correct operation.
The integration ensures the system meets functional and timing specifications.
• 7. Testing and Validation:
The integrated system undergoes hardware-in-the-loop (HIL) testing and performance validation.
Functional, timing, and stress tests confirm that the design meets reliability and real-time constraints.
Verified models are used for regression and future reuse.
Concurrent and Integrated Development Benefits:
• Reduced Development Time: Parallel hardware and software development shortens the overall project
timeline.
• Early Error Detection: Co-simulation identifies integration and interface issues before hardware
fabrication.
• Improved Design Quality: Shared specifications and synchronized models ensure functional consistency
and reduce human errors.
• Better Resource Optimization: Partitioning enables balancing of performance (hardware) and flexibility
(software).
• Lower Iteration Effort: Unified modeling reduces redesign cycles caused by late discovery of cross-
********** 12 **********
--- page 13 ---
domain issues.
• Enhanced Collaboration: Cross-functional teams (hardware, firmware, and application engineers) work on
shared design databases.
Q B Compare FPGA, ASIC, and PSOC technologies with respect to their architecture, design flexibility,   [10
7   performance, and cost. Explain how these factors influence the choice of implementation for various embedded   ]
system applications.
********** 13 **********

[Text in pictures on this page, read by OCR]
Feature FPGA ASIC PSOC

Architecture Configurable logic blocks and Fully customized gate- MCU core + programmable
routing matrix level design analog/digital blocks
Design Flexibility High (reconfigurable) None (fixed post- Moderate (reconfigurable mixed-sic
fabrication)
Performance Medium to high Very high Moderate
Power Consumption Moderate to high Very low Low
Development Time Short (ready-to-program) Long (requires Short to moderate

fabrication)

Cost per Unit High for low-volume, low for Very low for large Moderate
prototypes volume, high NRE
Typical Use Prototyping, DSP, Communication Mass-market high-speed Low-power, mixed-signal embeddec

applications systems
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 4b18497ca3a2

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_IT_7041/Embedded Systems/ANS_Embedded Systems(702IT0C015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Embedded Systems
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume suitable data if neccessary
Q   Answer briefly:   [20
1
]
a. Define an embedded system. Discuss how factors such as memory limitation, power consumption, and real-   [5]
time deadlines affect its design.
Sol:
• Embedded System Definition:
An embedded system is a special-purpose computer built to perform a dedicated function within a larger
system.
It combines hardware and software to operate in real-time under given constraints.
Example: Washing machine controller, pacemaker, or automotive ECU.
• Memory Limitation:
Embedded systems often have limited RAM and ROM.
Software must be optimized to use minimal memory.
Efficient algorithms and data handling are needed to fit within hardware limits.
• Power Consumption:
Many embedded systems run on batteries or low-power sources.
Designers use low-power processors, sleep modes, and efficient clock management to reduce energy use.
Power optimization increases battery life and reliability.
•   Real-Time Deadlines:
Systems must respond within a defined time limit.
Real-time scheduling and interrupt handling ensure deterministic responses.
Missing deadlines can cause functional failure in critical applications.
********** 1 **********
--- page 2 ---
b   Differentiate between CISC and RISC processor architectures based on their instruction set, register usage,   [5]
.   and design philosophy. Support your answer with suitable examples.
c. Explain the different task states in a real-time operating system and describe how a task transitions between   [5]
these states during execution.
• A task is the basic building block of software in an RTOS and is usually a subroutine.
•   The RTOS starts a task by specifying its corresponding subroutine, priority, stack etc.
•   The task can have 3 states :-
1. Running – The task code is currently being executed by the microprocessor. Except in multi-
processor systems, only one task is in running state.
2. Ready – The task is waiting to execute but another task is currently running.
3. Blocked – The task cannot run even if the microprocessor is free. It might be waiting for an
external event or a response. e.g. a push-button task stays blocked until the button is pushed.
•   Most RTOSs have other states like suspended, waiting, dormant etc. but these are just sub-divisions
of one of the three states above.
********** 2 **********

[Text in pictures on this page, read by OCR]
Feature CISC (Complex Instruction Set Computer) RISC (Reduced Instruction Set Computer)

Instruction Set Large set of complex instructions; each can Small set of simple instructions; each performs
perform multiple operations. one basic operation.

Instruction Length Variable length; some instructions take Fixed length; most instructions execute in one
many cycles to execute. clock cycle.

Register Usage Fewer general-purpose registers; heavy Many general-purpose registers; minimizes
dependence on memory. memory access.

Design Philosophy Hardware complexity; microcoded control Simplified hardware; hardwired control; focus
unit; focus on reducing code size. on speed and pipelining.

Performance Slower execution; more cycles per Faster execution; efficient instruction pipeline.
instruction.

Examples Intel x86, Motorola 68000. ARM, MIPS, PowerPC.
--- page 3 ---
d   Describe the role of device drivers in embedded systems.   [5]
.   Explain how architecture-specific and generic drivers differ in managing hardware components.
•   Device Driver Definition: A device driver is a specialized software component that acts as an
interface between the operating system (or application software) and hardware devices in an
embedded system. It allows software to access hardware functions without needing to know the low-
level hardware details.
•   Role of Device Drivers in Embedded Systems:
• Enable communication between software and hardware components.
• Abstract hardware complexity, allowing application code to be hardware-independent.
• Handle low-level operations such as reading/writing registers and managing interrupts.
• Support initialization, configuration, data transfer, and power management of peripherals.
• Improve system modularity and portability by separating hardware control from application logic.
• Example: UART driver for serial communication, SPI driver for sensors, GPIO driver for LEDs.
•   Architecture-Specific Drivers:
• Written for a particular processor or microcontroller architecture (e.g., ARM Cortex-M, AVR).
• Directly manipulate hardware registers, memory-mapped I/O, and interrupt lines.
• Provide optimal performance because they are tightly coupled to the hardware.
• Depend on processor-specific addressing, instruction sets, and peripheral structures.
• Example: STM32 UART driver using vendor HAL library or ARM CMSIS-based peripheral driver.
•   Generic Drivers:
• Platform-independent and designed to work across multiple architectures with minor modifications.
• Use standardized APIs or abstraction layers provided by the OS (e.g., POSIX, Linux kernel
interfaces).
• Focus on portability and reusability rather than raw performance.
• Typically rely on underlying architecture-specific layers for direct hardware access.
• Example: Generic USB or network driver framework in Linux that supports multiple hardware
platforms.
Q A   •   Classify embedded systems based on microcontroller performance as small-scale, medium-scale, and   [10
sophisticated systems. Explain each category with features, microcontroller type, and one real-world
2   ]
application example showing where it is used.
Embedded systems are classified based on microcontroller performance and application complexity into three
types: small-scale, medium-scale, and sophisticated embedded systems.
•   Small-Scale Embedded Systems:
• Use low-end 8-bit or 16-bit microcontrollers.
• Designed for simple and dedicated operations with limited memory and peripherals.
• Programs are written in C or assembly and stored in on-chip ROM or Flash.
• Operate with low power and minimal hardware complexity.
• Typically do not use an operating system and rely on simple looping or interrupt-based logic.
• Microcontroller Examples: 8051, PIC16F877A, AT89C51.
• Application Example: Digital thermometer, automatic streetlight, or simple home appliance
controller.
•   Medium-Scale Embedded Systems:
• Use 16-bit or 32-bit microcontrollers or microprocessors.
• Perform moderately complex tasks and often support multitasking.
• May use a real-time operating system (RTOS) for scheduling and resource management.
• Include more memory and advanced peripherals like ADCs, UARTs, and communication ports.
• Suitable for applications requiring both performance and flexibility.
• Microcontroller Examples: ARM Cortex-M series, AVR32, MSP430.
• Application Example: Smart washing machine, industrial process controller, portable medical
devices.
•   Sophisticated Embedded Systems:
• Use high-performance 32-bit or 64-bit processors or SoCs.
• Capable of executing multiple complex tasks simultaneously.
• Run full-fledged embedded operating systems such as Linux, Android, or QNX.
• Include features like Ethernet, USB, Wi-Fi, and graphics interfaces.
********** 3 **********
--- page 4 ---
• Require high memory, storage, and advanced hardware-software integration.
• Processor Examples: ARM Cortex-A series, Intel Atom, Raspberry Pi SoC.
• Application Example: Automotive ECU, smart surveillance camera, or drone control system.
Q B   Explain the role of Digital Signal Processing (DSP) in embedded systems. Analyze how the integration of DSP   [10
2   techniques enhances the performance, precision, and functionality of real-time embedded applications. Support   ]
your answer with suitable examples.
Digital Signal Processing (DSP) is used in embedded systems to process real-world analog signals that have
been converted into digital form. It involves mathematical operations such as filtering, transformation, and
compression to extract useful information or modify signals for specific purposes.
❖ Role of DSP in Embedded Systems:
• Enhances system capability to handle audio, video, sensor, and communication signals in real time.
• Performs operations like filtering, modulation, spectral analysis, and signal compression.
• Used in applications requiring fast, repetitive, and high-precision mathematical processing.
• Executes complex algorithms (like FFT, FIR, IIR) directly on embedded hardware.
• Reduces noise, improves data accuracy, and ensures reliable real-time output.
• DSP chips or integrated DSP cores are often embedded alongside microcontrollers for efficiency.
❖ Integration of DSP Techniques – Performance Enhancement:
• Performance: Dedicated DSP cores execute multiply–accumulate (MAC) operations efficiently,
offering faster response in real-time systems such as speech and image processing.
• Precision: Fixed-point or floating-point arithmetic enables accurate signal computation with
minimal quantization error.
• Functionality: Enables complex processing like adaptive filtering, predictive control, and sensor
fusion within embedded environments.
• Efficiency: Parallel pipelines and specialized instruction sets in DSPs reduce processing latency.
• Optimization: Hardware-level DSP integration minimizes CPU load and improves throughput.
❖ Examples of DSP in Embedded Applications:
• Audio Processing: Noise suppression, echo cancellation, equalization in Bluetooth headsets or
hearing aids.
• Image and Video Processing: Edge detection, image enhancement, and object tracking in smart
cameras.
• Communication Systems: Modulation/demodulation, error correction, and signal decoding in
mobile or IoT networks.
• Industrial Control: Vibration and condition monitoring using real-time signal analysis for
predictive maintenance.
• Biomedical Devices: ECG and EEG filtering and feature extraction for patient monitoring systems.
❖ Analysis Summary:
Integration of DSP techniques in embedded systems improves computational speed, signal accuracy,
and functional intelligence. It enables real-time systems to achieve deterministic performance,
making them more efficient, responsive, and adaptable to complex signal-driven environments.
Q   •   Explain how the Real-Time Operating System (RTOS) and Application Software together constitute the   [10
software architecture of an embedded system. Describe how their interaction supports task scheduling,
3 A   ]
context switching, and ensures system reliability.
•
•   The software architecture of an embedded system is typically layered, consisting of the Application
Software, RTOS kernel, hardware abstraction layer, and device drivers. The RTOS and Application
Software together form the main functional core that enables real-time operation and reliability.
•   Role of RTOS in Software Architecture:
• Acts as the control center that manages processor time, memory, and resources among multiple tasks.
• Provides essential services such as task scheduling, inter-task communication, synchronization, and
interrupt handling.
• Ensures deterministic response by allowing high-priority tasks to pre-empt lower ones.
• Facilitates modular software design by separating time-critical kernel functions from application logic.
********** 4 **********
--- page 5 ---
•   Role of Application Software:
• Consists of user-defined tasks and functions designed to fulfill system-specific requirements.
• Runs on top of the RTOS, using its APIs for communication, timing, and resource access.
• Each task represents a functional unit, such as sensor reading, motor control, or display update.
• Application software depends on the RTOS for timing accuracy and task coordination.
•   Interaction between RTOS and Application Software:
• The RTOS schedules and manages tasks created by the application.
• Each task transitions through states such as ready, running, waiting, or suspended under RTOS control.
• System calls and APIs connect the application layer to the kernel for services like semaphores, message
queues, and timers.
• Interrupts are handled by the RTOS, which triggers the corresponding application task or ISR.
• Context switching performed by the RTOS saves and restores CPU states to switch between tasks
without losing data or state.
•   Support for Task Scheduling and Context Switching:
• RTOS uses priority-based or round-robin scheduling to allocate CPU time efficiently.
• Context switching ensures smooth transfer between tasks, maintaining system responsiveness.
• The kernel manages stack and register storage during task switching to avoid data corruption.
•   Ensuring System Reliability:
• Fault isolation prevents one malfunctioning task from affecting others.
• Watchdog timers and health monitoring tasks enhance fault recovery.
• Synchronization mechanisms (mutexes, semaphores) prevent race conditions and resource conflicts.
• Deterministic execution ensures timely completion of safety-critical operations.
•   The RTOS provides time management, multitasking, and resource control, while the Application
Software implements system functionality. Their coordinated interaction ensures predictable timing,
modularity, and reliability in real-time embedded systems.
Q B Develop a UML-based model for an embedded application automatic door lock system. Identify the key   [10
3   classes, states, and interactions, and justify how the UML model helps achieve design clarity and modularity.   ]
How UML helps design clarity and modularity (Justification):
• Separation of concerns: classes isolate authentication, actuation, sensing, UI, and timing, simplifying
reasoning and testing
• Traceable behavior: state diagram maps policy (timeouts, retries, tamper) to explicit states/transitions,
reducing ambiguity
• Reusable components: AuthModule, LockActuator, DoorSensor can be reused across other access-control
products
• Change-friendly: adding a new credential (e.g., NFC) or mode (visitor access) only extends interface
classes and state transitions, leaving core logic intact
********** 5 **********
--- page 6 ---
• HW/SW codesign alignment: clear interfaces between controller and drivers (LockActuator, DoorSensor)
support HAL/RTOS layering from your slides
• Verification readiness: scenarios from the sequence diagram become test cases (normal open/close, invalid
PINs, lockout, tamper)
Example mapping to RTOS tasks (optional alignment):
• Tasks: InputTask (keypad/RFID), ControlTask (state machine), ActuatorTask (lock), UITask
(display/buzzer), LoggerTask, Watchdog/TimerTask
• RTOS services: message queues for events, timers for auto-relock, mutex for shared log
Q A Explain Real-Time Scheduling in embedded systems and its role in executing periodic tasks within deadlines.
4   Discuss the working of Earliest Deadline First (EDF) and Round Robin scheduling algorithms with suitable
timing diagrams.
[10
]
Q B   Evaluate how cross-fertilization between hardware and software design—using synthesis tools, unified [10
4   languages, and shared databases—improves the efficiency of embedded system development. Also state the key   ]
requirements of an ideal codesign environment that enable such integration.
********** 6 **********

[Text in pictures on this page, read by OCR]
EDF Scheduling

Earliest Deadline First (EDF) scheduling
* Simple, yet effective

+ Whichever task has next deadline gets to run

Deadline: 5 Deadline: 8 [Tsk | Deadline: 12
Exec time: 4 Exec time: 3 Exec time: 2

+ Theory exists to analyze such systems

Time ° ts ts

te

Round Robin Scheduling

Round-robin scheduling
‘Same as SCHED_FIFO but with timeslices

Among tasks of equal priority:
* Rotate through all tasks
+ Each task gets a fixed time slice

* Only a higher priority SCHED_FIFO or SCHED_BR task can preempt a SCHED_FIFO Time
+ Tasks of equal priority each other after ti
--- page 7 ---
Cross-fertilization in embedded system design refers to the close collaboration and overlap between
hardware and software development activities to achieve faster, more efficient, and optimized system design.
How cross-fertilization improves design efficiency:
• Concurrent Development: Hardware and software can be designed, simulated, and verified in parallel
rather than sequentially, reducing overall design time.
• Use of Unified Languages: High-level specification languages (like SystemC, VHDL-AMS, Verilog-AMS,
UML) describe both hardware and software behavior, improving communication and reducing design
ambiguity.
• Synthesis Tools Integration: Automated synthesis tools convert high-level system descriptions into
hardware (RTL) and software (C/C++/firmware) components, ensuring consistency and faster
implementation.
• Shared Databases: Unified design repositories maintain common specifications, timing data, interface
definitions, and test vectors accessible by both hardware and software teams, ensuring design traceability and
version control.
• Improved Verification and Validation: Co-simulation environments verify hardware and software
behavior together, identifying integration issues early and minimizing late-stage rework.
• Design Reuse and Scalability: Standardized interfaces and reusable IP blocks simplify porting designs
across platforms and reduce future development costs.
• Optimized Performance: Partitioning and iterative refinement between hardware and software enable the
most efficient use of resources such as speed, area, and power.
Key Requirements of an Ideal Codesign Environment:
• Unified Specification Model: A single executable specification for both hardware and software to ensure
consistency and shared understanding.
• Common Design Database: Central repository for design data, IP libraries, timing constraints, and
documentation accessible to all design tools.
• Integrated Synthesis and Simulation Tools: Tools that allow automatic synthesis, co-simulation, and
performance evaluation of hardware and software components.
• Seamless Hardware–Software Partitioning: Capability to explore multiple design alternatives, move
functions between hardware and software, and assess trade-offs dynamically.
• Standardized Communication Interfaces: Support for common protocols (e.g., AMBA, SPI, I2C) and
reusable interface models for interoperability.
• Support for Reuse and Scalability: Modular design and IP reuse support across projects and platforms.
• Automatic Verification Support: Built-in testbench generation, co-simulation, and debugging features for
early integration testing.
• Cross-Team Collaboration Tools: Shared dashboards and documentation tools enabling real-time
coordination between hardware and software engineers.
Cross-fertilization between hardware and software through synthesis tools, unified modeling languages, and
shared databases transforms the design flow into an integrated, concurrent process. It minimizes development
time, enhances design accuracy, and leads to better performance and reliability. An ideal codesign
********** 7 **********
--- page 8 ---
environment supports this integration with unified specifications, tool interoperability, and strong verification
support.
Q A Evaluate how system calls enable communication between application programs and the operating system in   [10
5   embedded environments. Discuss how improper system call management can affect system performance and   ]
reliability.
System calls are special functions provided by the operating system that allow application programs to
request specific services from the kernel.
In embedded systems, they serve as a controlled interface between user-level applications and system-level
resources such as hardware devices, memory, and peripherals.
Role of System Calls in Embedded Environments:
• Provide a secure and standardized way for applications to access OS resources without directly manipulating
hardware.
• Enable essential operations such as process management, task scheduling, file access, communication, and
interrupt handling.
• Support real-time constraints by allowing applications to request deterministic services (e.g., task delay,
event wait, semaphore control).
• Ensure isolation between user tasks and kernel operations, preventing user code from corrupting system
data.
• Simplify application development by abstracting low-level details and exposing clear APIs.
• Examples of system calls in embedded RTOS: osDelay(), osSemaphoreWait(), osMessageQueuePut(),
read(), write().
How System Calls Enable Communication:
• When an application invokes a system call, it triggers a software interrupt (SWI) or trap instruction that
transfers control to the kernel in supervisory mode.
• The kernel executes the requested service (e.g., allocate memory, read sensor data, start a timer).
• Once completed, control returns to the application in user mode with the result or status code.
• This mechanism ensures safe, controlled communication between user applications and system-level
services.
Impact of Improper System Call Management:
• Increased Latency: Excessive or poorly timed system calls can cause frequent context switches, increasing
task response time and violating real-time deadlines.
• Resource Contention: Uncontrolled access to shared resources (files, devices, or buffers) through system
calls can lead to race conditions and deadlocks.
• Kernel Overhead: Repeated calls to non-critical services burden the CPU, lowering system throughput.
• Security Risks: Mismanaged calls may allow unauthorized access to protected memory or device registers.
• Memory Leaks: Failing to release OS-allocated resources after system calls (e.g., semaphores, queues)
degrades performance over time.
• Reduced Reliability: Unchecked return values or improper error handling can cause unpredictable behavior
or system crashes in safety-critical applications.
Good System Call Practices in Embedded Systems:
• Use minimal and optimized system calls in real-time tasks to reduce kernel transition overhead.
• Validate all parameters before invoking system calls to prevent illegal access or null references.
• Group related system calls logically to minimize switching and improve performance.
********** 8 **********
--- page 9 ---
• Implement proper error handling, timeout mechanisms, and watchdog monitoring for robust operation.
• Profile and optimize system call usage during real-time testing to ensure predictable behavior.
Evaluation Summary:
System calls form the vital communication bridge between applications and the OS kernel in embedded
systems, ensuring safe and structured access to hardware and services. Proper management of system calls
maintains determinism, performance, and security, whereas poor management can lead to latency,
instability, and reliability failures in real-time embedded environments.
Q B   Explain the sequence of steps involved in creating an executable image for an embedded system. Discuss how [10
5   the compiler, assembler, linker, and locator collectively transform source code into a target-specific binary   ]
image. Support your answer with a labeled diagram showing the relationship between host and target systems.
In embedded systems, the software development process involves generating a target-specific executable
image on a host computer, which is later downloaded to the target hardware for execution.
The toolchain used includes the compiler, assembler, linker, and locator, which work together to produce
the final binary.
Step 1: Source Code Creation (on Host System)
• Developers write high-level source code in C or C++ using an IDE or text editor.
• Code includes application logic, hardware drivers, and RTOS functions.
• Example: main.c, sensor.c, motor.c.
Step 2: Compilation
• The compiler translates high-level C/C++ code into assembly language instructions specific to the target
processor architecture.
• Performs optimizations, syntax checking, and generates intermediate files (.asm or .obj).
• Example: ARM GCC or Keil compiler generates ARM assembly code.
Step 3: Assembly
• The assembler converts the assembly instructions into machine code (object files with .o or .obj
extensions).
• Produces symbol tables and relocatable object code.
• Each source file becomes one object file, ready for linking.
Step 4: Linking
• The linker combines multiple object files into a single executable file.
• Resolves external symbols, function calls, and global variables used across different modules.
• Links with standard libraries (e.g., math, RTOS kernel, device drivers).
• Produces a partially complete executable known as an absolute object file (.elf or .axf).
Step 5: Location and Image Generation
• The locator (also called the linker-locator) assigns physical memory addresses to the program segments
(code, data, stack, heap).
• Generates the final binary/hex image that matches the target’s memory map.
• Output formats include .bin, .hex, or .srec, ready for download to Flash or ROM.
Step 6: Downloading to Target System
• The final image is transferred from the host system to the target hardware via interfaces such as JTAG,
********** 9 **********
--- page 10 ---
UART, or USB.
• A bootloader or programmer writes the image into the target’s memory for execution.
Step 7: Execution and Debugging
• Once loaded, the target processor executes the image.
• Debuggers (GDB, Keil μVision) on the host allow step-by-step verification, breakpoints, and memory
inspection.
Q A Explain the concept of priority inversion in real-time embedded systems. Describe how it affects task scheduling [10
6   and system performance, and discuss suitable techniques used to minimize or prevent this problem.   ]
• Priority inversion occurs when a high-priority task is indirectly blocked by a low-priority task because
the low-priority task holds a shared resource that the high-priority task needs. Meanwhile, medium-priority
tasks may preempt the low-priority one, causing the high-priority task to wait longer.
• Example:
• Task T1 – High Priority (needs shared resource)
• Task T2 – Low Priority (holding that resource)
• Task T3 – Medium Priority (independent but preempts T2)
Here, T3 delays T2, which in turn delays T1, creating an inversion of priorities.
• Effects on Task Scheduling and System Performance:
• Causes high-priority tasks to miss deadlines, breaking real-time constraints.
• Reduces system predictability and determinism.
• Increases response latency and context-switching overhead.
• May cause task starvation when medium-priority tasks keep preempting the lower one.
• Degrades system reliability and performance in safety-critical systems like automotive ECUs or robotic
control.
• Techniques to Minimize or Prevent Priority Inversion:
• Priority Inheritance Protocol (PIP):
The low-priority task holding the resource temporarily inherits the priority of the highest-priority task waiting
for it, preventing medium-priority preemption.
• Priority Ceiling Protocol (PCP):
Each shared resource is assigned a ceiling priority equal to the highest task priority that can access it. A task
can only lock a resource if its priority is higher than the current ceiling, preventing deadlocks and bounding
blocking time.
• Immediate Ceiling Protocol (ICPP):
When a task locks a resource, it immediately executes at the ceiling priority until it releases the resource,
ensuring no other task can preempt it.
• Non-blocking Design Approaches:
Use lock-free algorithms, message queues, or event-driven designs to minimize resource sharing.
• Watchdog Monitoring:
Detects and logs priority inversion cases during execution for system tuning.
• Practical Example:
In an automotive braking ECU, a low-priority diagnostic task holding a bus resource can delay a high-priority
braking control task. Applying priority inheritance allows the diagnostic task to complete quickly, restoring
real-time responsiveness.
• Summary:
Priority inversion disrupts real-time scheduling by allowing lower-priority tasks to block critical ones.
Techniques such as priority inheritance and priority ceiling protocols ensure bounded blocking time,
improved predictability, and higher reliability in real-time embedded systems.
********** 10 **********
--- page 11 ---
Q B Implement the following Boolean functions using a suitable PAL.   [10
6   Let inputs be x,y,z(both true and complemented forms available).   ]
A(x,y,z)=Σ (1,2,4,6)
B(x,y,z)=Σ(0,1,6,7)
C(x,y,z)=Σ(2,6)
Tasks (show working):
i.   Obtain minimized SOP for A,B,C, (K-maps or equivalent) and identify shared product terms across
the four outputs. (3M)
ii.   Prepare the PAL specification table: list product terms, their input literals, and map them to outputs
A,B,C. (2M)
iii.   Draw the PAL programming matrix/connection diagram (AND/OR planes), clearly indicating
intact/blown fuses (or marked connections). (3M)
iv.   State the minimum number of product terms your design uses and justify how sharing was achieved.
(2M)
********** 11 **********
--- page 12 ---
Q   Describe the Hardware–Software Codesign flow from system specification to integration and testing. Explain [10
7 A how concurrent and integrated development of hardware and software improves design quality and reduces   ]
iteration effort.
Hardware–Software Codesign is an integrated design methodology in which hardware and software
components are developed concurrently from a unified system specification. It aims to achieve optimal
performance, cost, and time efficiency for embedded systems.
Codesign Flow — Step-by-Step Process:
• 1. System Specification:
The design begins with defining overall system requirements — functionality, timing, power, cost, and
performance goals.
A unified, high-level executable specification (using UML, SystemC, or MATLAB models) describes both
hardware and software behavior.
• 2. System Partitioning:
The system functions are divided between hardware (to improve performance or meet timing constraints) and
software (for flexibility and cost efficiency).
Design space exploration evaluates different partition alternatives to achieve optimal trade-offs.
• 3. Hardware Design:
Hardware blocks identified from partitioning are implemented using HDL (VHDL/Verilog/SystemVerilog).
Synthesis tools generate gate-level circuits and optimize area, speed, and power.
Hardware prototypes (FPGA or simulation) validate timing and functionality.
• 4. Software Design:
Software components (RTOS, drivers, application logic) are developed in parallel using C/C++ or assembly.
Tasks are implemented, tested, and profiled on virtual platforms or simulators before real hardware is ready.
• 5. Co-Simulation and Verification:
Hardware and software modules are simulated together using co-simulation tools (e.g., ModelSim, QEMU, or
SystemC).
This stage detects interface mismatches, synchronization issues, and timing violations early.
• 6. Integration:
Hardware (FPGA/ASIC) and software (firmware, drivers, RTOS) are integrated on the target platform.
Communication interfaces, buses, and interrupts are validated for correct operation.
The integration ensures the system meets functional and timing specifications.
• 7. Testing and Validation:
The integrated system undergoes hardware-in-the-loop (HIL) testing and performance validation.
Functional, timing, and stress tests confirm that the design meets reliability and real-time constraints.
Verified models are used for regression and future reuse.
Concurrent and Integrated Development Benefits:
• Reduced Development Time: Parallel hardware and software development shortens the overall project
timeline.
• Early Error Detection: Co-simulation identifies integration and interface issues before hardware
fabrication.
• Improved Design Quality: Shared specifications and synchronized models ensure functional consistency
and reduce human errors.
• Better Resource Optimization: Partitioning enables balancing of performance (hardware) and flexibility
(software).
• Lower Iteration Effort: Unified modeling reduces redesign cycles caused by late discovery of cross-
********** 12 **********
--- page 13 ---
domain issues.
• Enhanced Collaboration: Cross-functional teams (hardware, firmware, and application engineers) work on
shared design databases.
Q B Compare FPGA, ASIC, and PSOC technologies with respect to their architecture, design flexibility,   [10
7   performance, and cost. Explain how these factors influence the choice of implementation for various embedded   ]
system applications.
********** 13 **********

[Text in pictures on this page, read by OCR]
Feature FPGA ASIC PSOC

Architecture Configurable logic blocks and Fully customized gate- MCU core + programmable
routing matrix level design analog/digital blocks
Design Flexibility High (reconfigurable) None (fixed post- Moderate (reconfigurable mixed-sic
fabrication)
Performance Medium to high Very high Moderate
Power Consumption Moderate to high Very low Low
Development Time Short (ready-to-program) Long (requires Short to moderate

fabrication)

Cost per Unit High for low-volume, low for Very low for large Moderate
prototypes volume, high NRE
Typical Use Prototyping, DSP, Communication Mass-market high-speed Low-power, mixed-signal embeddec

applications systems
````

## 2025-26 · Re-Exam · Sem 9 · Answer key · paper 564f1fa53218

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_09/Re-Exam/Integrated_IT_7037/Embedded Systems/ANS_Embedded Systems(702IT0C015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Embedded Systems
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume suitable data if neccessary
Q   Answer briefly:   [20
1
]
a. Define an embedded system. Discuss how factors such as memory limitation, power consumption, and real-   [5]
time deadlines affect its design.
Sol:
• Embedded System Definition:
An embedded system is a special-purpose computer built to perform a dedicated function within a larger
system.
It combines hardware and software to operate in real-time under given constraints.
Example: Washing machine controller, pacemaker, or automotive ECU.
• Memory Limitation:
Embedded systems often have limited RAM and ROM.
Software must be optimized to use minimal memory.
Efficient algorithms and data handling are needed to fit within hardware limits.
• Power Consumption:
Many embedded systems run on batteries or low-power sources.
Designers use low-power processors, sleep modes, and efficient clock management to reduce energy use.
Power optimization increases battery life and reliability.
•   Real-Time Deadlines:
Systems must respond within a defined time limit.
Real-time scheduling and interrupt handling ensure deterministic responses.
Missing deadlines can cause functional failure in critical applications.
********** 1 **********
--- page 2 ---
b   Differentiate between CISC and RISC processor architectures based on their instruction set, register usage,   [5]
.   and design philosophy. Support your answer with suitable examples.
c. Explain the different task states in a real-time operating system and describe how a task transitions between   [5]
these states during execution.
• A task is the basic building block of software in an RTOS and is usually a subroutine.
•   The RTOS starts a task by specifying its corresponding subroutine, priority, stack etc.
•   The task can have 3 states :-
1. Running – The task code is currently being executed by the microprocessor. Except in multi-
processor systems, only one task is in running state.
2. Ready – The task is waiting to execute but another task is currently running.
3. Blocked – The task cannot run even if the microprocessor is free. It might be waiting for an
external event or a response. e.g. a push-button task stays blocked until the button is pushed.
•   Most RTOSs have other states like suspended, waiting, dormant etc. but these are just sub-divisions
of one of the three states above.
********** 2 **********

[Text in pictures on this page, read by OCR]
Feature CISC (Complex Instruction Set Computer) RISC (Reduced Instruction Set Computer)

Instruction Set Large set of complex instructions; each can Small set of simple instructions; each performs
perform multiple operations. one basic operation.

Instruction Length Variable length; some instructions take Fixed length; most instructions execute in one
many cycles to execute. clock cycle.

Register Usage Fewer general-purpose registers; heavy Many general-purpose registers; minimizes
dependence on memory. memory access.

Design Philosophy Hardware complexity; microcoded control Simplified hardware; hardwired control; focus
unit; focus on reducing code size. on speed and pipelining.

Performance Slower execution; more cycles per Faster execution; efficient instruction pipeline.
instruction.

Examples Intel x86, Motorola 68000. ARM, MIPS, PowerPC.
--- page 3 ---
d   Describe the role of device drivers in embedded systems.   [5]
.   Explain how architecture-specific and generic drivers differ in managing hardware components.
•   Device Driver Definition: A device driver is a specialized software component that acts as an
interface between the operating system (or application software) and hardware devices in an
embedded system. It allows software to access hardware functions without needing to know the low-
level hardware details.
•   Role of Device Drivers in Embedded Systems:
• Enable communication between software and hardware components.
• Abstract hardware complexity, allowing application code to be hardware-independent.
• Handle low-level operations such as reading/writing registers and managing interrupts.
• Support initialization, configuration, data transfer, and power management of peripherals.
• Improve system modularity and portability by separating hardware control from application logic.
• Example: UART driver for serial communication, SPI driver for sensors, GPIO driver for LEDs.
•   Architecture-Specific Drivers:
• Written for a particular processor or microcontroller architecture (e.g., ARM Cortex-M, AVR).
• Directly manipulate hardware registers, memory-mapped I/O, and interrupt lines.
• Provide optimal performance because they are tightly coupled to the hardware.
• Depend on processor-specific addressing, instruction sets, and peripheral structures.
• Example: STM32 UART driver using vendor HAL library or ARM CMSIS-based peripheral driver.
•   Generic Drivers:
• Platform-independent and designed to work across multiple architectures with minor modifications.
• Use standardized APIs or abstraction layers provided by the OS (e.g., POSIX, Linux kernel
interfaces).
• Focus on portability and reusability rather than raw performance.
• Typically rely on underlying architecture-specific layers for direct hardware access.
• Example: Generic USB or network driver framework in Linux that supports multiple hardware
platforms.
Q A   •   Classify embedded systems based on microcontroller performance as small-scale, medium-scale, and   [10
sophisticated systems. Explain each category with features, microcontroller type, and one real-world
2   ]
application example showing where it is used.
Embedded systems are classified based on microcontroller performance and application complexity into three
types: small-scale, medium-scale, and sophisticated embedded systems.
•   Small-Scale Embedded Systems:
• Use low-end 8-bit or 16-bit microcontrollers.
• Designed for simple and dedicated operations with limited memory and peripherals.
• Programs are written in C or assembly and stored in on-chip ROM or Flash.
• Operate with low power and minimal hardware complexity.
• Typically do not use an operating system and rely on simple looping or interrupt-based logic.
• Microcontroller Examples: 8051, PIC16F877A, AT89C51.
• Application Example: Digital thermometer, automatic streetlight, or simple home appliance
controller.
•   Medium-Scale Embedded Systems:
• Use 16-bit or 32-bit microcontrollers or microprocessors.
• Perform moderately complex tasks and often support multitasking.
• May use a real-time operating system (RTOS) for scheduling and resource management.
• Include more memory and advanced peripherals like ADCs, UARTs, and communication ports.
• Suitable for applications requiring both performance and flexibility.
• Microcontroller Examples: ARM Cortex-M series, AVR32, MSP430.
• Application Example: Smart washing machine, industrial process controller, portable medical
devices.
•   Sophisticated Embedded Systems:
• Use high-performance 32-bit or 64-bit processors or SoCs.
• Capable of executing multiple complex tasks simultaneously.
• Run full-fledged embedded operating systems such as Linux, Android, or QNX.
• Include features like Ethernet, USB, Wi-Fi, and graphics interfaces.
********** 3 **********
--- page 4 ---
• Require high memory, storage, and advanced hardware-software integration.
• Processor Examples: ARM Cortex-A series, Intel Atom, Raspberry Pi SoC.
• Application Example: Automotive ECU, smart surveillance camera, or drone control system.
Q B   Explain the role of Digital Signal Processing (DSP) in embedded systems. Analyze how the integration of DSP   [10
2   techniques enhances the performance, precision, and functionality of real-time embedded applications. Support   ]
your answer with suitable examples.
Digital Signal Processing (DSP) is used in embedded systems to process real-world analog signals that have
been converted into digital form. It involves mathematical operations such as filtering, transformation, and
compression to extract useful information or modify signals for specific purposes.
❖ Role of DSP in Embedded Systems:
• Enhances system capability to handle audio, video, sensor, and communication signals in real time.
• Performs operations like filtering, modulation, spectral analysis, and signal compression.
• Used in applications requiring fast, repetitive, and high-precision mathematical processing.
• Executes complex algorithms (like FFT, FIR, IIR) directly on embedded hardware.
• Reduces noise, improves data accuracy, and ensures reliable real-time output.
• DSP chips or integrated DSP cores are often embedded alongside microcontrollers for efficiency.
❖ Integration of DSP Techniques – Performance Enhancement:
• Performance: Dedicated DSP cores execute multiply–accumulate (MAC) operations efficiently,
offering faster response in real-time systems such as speech and image processing.
• Precision: Fixed-point or floating-point arithmetic enables accurate signal computation with
minimal quantization error.
• Functionality: Enables complex processing like adaptive filtering, predictive control, and sensor
fusion within embedded environments.
• Efficiency: Parallel pipelines and specialized instruction sets in DSPs reduce processing latency.
• Optimization: Hardware-level DSP integration minimizes CPU load and improves throughput.
❖ Examples of DSP in Embedded Applications:
• Audio Processing: Noise suppression, echo cancellation, equalization in Bluetooth headsets or
hearing aids.
• Image and Video Processing: Edge detection, image enhancement, and object tracking in smart
cameras.
• Communication Systems: Modulation/demodulation, error correction, and signal decoding in
mobile or IoT networks.
• Industrial Control: Vibration and condition monitoring using real-time signal analysis for
predictive maintenance.
• Biomedical Devices: ECG and EEG filtering and feature extraction for patient monitoring systems.
❖ Analysis Summary:
Integration of DSP techniques in embedded systems improves computational speed, signal accuracy,
and functional intelligence. It enables real-time systems to achieve deterministic performance,
making them more efficient, responsive, and adaptable to complex signal-driven environments.
Q   •   Explain how the Real-Time Operating System (RTOS) and Application Software together constitute the   [10
software architecture of an embedded system. Describe how their interaction supports task scheduling,
3 A   ]
context switching, and ensures system reliability.
•
•   The software architecture of an embedded system is typically layered, consisting of the Application
Software, RTOS kernel, hardware abstraction layer, and device drivers. The RTOS and Application
Software together form the main functional core that enables real-time operation and reliability.
•   Role of RTOS in Software Architecture:
• Acts as the control center that manages processor time, memory, and resources among multiple tasks.
• Provides essential services such as task scheduling, inter-task communication, synchronization, and
interrupt handling.
• Ensures deterministic response by allowing high-priority tasks to pre-empt lower ones.
• Facilitates modular software design by separating time-critical kernel functions from application logic.
********** 4 **********
--- page 5 ---
•   Role of Application Software:
• Consists of user-defined tasks and functions designed to fulfill system-specific requirements.
• Runs on top of the RTOS, using its APIs for communication, timing, and resource access.
• Each task represents a functional unit, such as sensor reading, motor control, or display update.
• Application software depends on the RTOS for timing accuracy and task coordination.
•   Interaction between RTOS and Application Software:
• The RTOS schedules and manages tasks created by the application.
• Each task transitions through states such as ready, running, waiting, or suspended under RTOS control.
• System calls and APIs connect the application layer to the kernel for services like semaphores, message
queues, and timers.
• Interrupts are handled by the RTOS, which triggers the corresponding application task or ISR.
• Context switching performed by the RTOS saves and restores CPU states to switch between tasks
without losing data or state.
•   Support for Task Scheduling and Context Switching:
• RTOS uses priority-based or round-robin scheduling to allocate CPU time efficiently.
• Context switching ensures smooth transfer between tasks, maintaining system responsiveness.
• The kernel manages stack and register storage during task switching to avoid data corruption.
•   Ensuring System Reliability:
• Fault isolation prevents one malfunctioning task from affecting others.
• Watchdog timers and health monitoring tasks enhance fault recovery.
• Synchronization mechanisms (mutexes, semaphores) prevent race conditions and resource conflicts.
• Deterministic execution ensures timely completion of safety-critical operations.
•   The RTOS provides time management, multitasking, and resource control, while the Application
Software implements system functionality. Their coordinated interaction ensures predictable timing,
modularity, and reliability in real-time embedded systems.
Q B Develop a UML-based model for an embedded application automatic door lock system. Identify the key   [10
3   classes, states, and interactions, and justify how the UML model helps achieve design clarity and modularity.   ]
How UML helps design clarity and modularity (Justification):
• Separation of concerns: classes isolate authentication, actuation, sensing, UI, and timing, simplifying
reasoning and testing
• Traceable behavior: state diagram maps policy (timeouts, retries, tamper) to explicit states/transitions,
reducing ambiguity
• Reusable components: AuthModule, LockActuator, DoorSensor can be reused across other access-control
products
• Change-friendly: adding a new credential (e.g., NFC) or mode (visitor access) only extends interface
classes and state transitions, leaving core logic intact
********** 5 **********
--- page 6 ---
• HW/SW codesign alignment: clear interfaces between controller and drivers (LockActuator, DoorSensor)
support HAL/RTOS layering from your slides
• Verification readiness: scenarios from the sequence diagram become test cases (normal open/close, invalid
PINs, lockout, tamper)
Example mapping to RTOS tasks (optional alignment):
• Tasks: InputTask (keypad/RFID), ControlTask (state machine), ActuatorTask (lock), UITask
(display/buzzer), LoggerTask, Watchdog/TimerTask
• RTOS services: message queues for events, timers for auto-relock, mutex for shared log
Q A Explain Real-Time Scheduling in embedded systems and its role in executing periodic tasks within deadlines.
4   Discuss the working of Earliest Deadline First (EDF) and Round Robin scheduling algorithms with suitable
timing diagrams.
[10
]
Q B   Evaluate how cross-fertilization between hardware and software design—using synthesis tools, unified [10
4   languages, and shared databases—improves the efficiency of embedded system development. Also state the key   ]
requirements of an ideal codesign environment that enable such integration.
********** 6 **********

[Text in pictures on this page, read by OCR]
EDF Scheduling

Earliest Deadline First (EDF) scheduling
* Simple, yet effective

+ Whichever task has next deadline gets to run

Deadline: 5 Deadline: 8 [Tsk | Deadline: 12
Exec time: 4 Exec time: 3 Exec time: 2

+ Theory exists to analyze such systems

Time ° ts ts

te

Round Robin Scheduling

Round-robin scheduling
‘Same as SCHED_FIFO but with timeslices

Among tasks of equal priority:
* Rotate through all tasks
+ Each task gets a fixed time slice

* Only a higher priority SCHED_FIFO or SCHED_BR task can preempt a SCHED_FIFO Time
+ Tasks of equal priority each other after ti
--- page 7 ---
Cross-fertilization in embedded system design refers to the close collaboration and overlap between
hardware and software development activities to achieve faster, more efficient, and optimized system design.
How cross-fertilization improves design efficiency:
• Concurrent Development: Hardware and software can be designed, simulated, and verified in parallel
rather than sequentially, reducing overall design time.
• Use of Unified Languages: High-level specification languages (like SystemC, VHDL-AMS, Verilog-AMS,
UML) describe both hardware and software behavior, improving communication and reducing design
ambiguity.
• Synthesis Tools Integration: Automated synthesis tools convert high-level system descriptions into
hardware (RTL) and software (C/C++/firmware) components, ensuring consistency and faster
implementation.
• Shared Databases: Unified design repositories maintain common specifications, timing data, interface
definitions, and test vectors accessible by both hardware and software teams, ensuring design traceability and
version control.
• Improved Verification and Validation: Co-simulation environments verify hardware and software
behavior together, identifying integration issues early and minimizing late-stage rework.
• Design Reuse and Scalability: Standardized interfaces and reusable IP blocks simplify porting designs
across platforms and reduce future development costs.
• Optimized Performance: Partitioning and iterative refinement between hardware and software enable the
most efficient use of resources such as speed, area, and power.
Key Requirements of an Ideal Codesign Environment:
• Unified Specification Model: A single executable specification for both hardware and software to ensure
consistency and shared understanding.
• Common Design Database: Central repository for design data, IP libraries, timing constraints, and
documentation accessible to all design tools.
• Integrated Synthesis and Simulation Tools: Tools that allow automatic synthesis, co-simulation, and
performance evaluation of hardware and software components.
• Seamless Hardware–Software Partitioning: Capability to explore multiple design alternatives, move
functions between hardware and software, and assess trade-offs dynamically.
• Standardized Communication Interfaces: Support for common protocols (e.g., AMBA, SPI, I2C) and
reusable interface models for interoperability.
• Support for Reuse and Scalability: Modular design and IP reuse support across projects and platforms.
• Automatic Verification Support: Built-in testbench generation, co-simulation, and debugging features for
early integration testing.
• Cross-Team Collaboration Tools: Shared dashboards and documentation tools enabling real-time
coordination between hardware and software engineers.
Cross-fertilization between hardware and software through synthesis tools, unified modeling languages, and
shared databases transforms the design flow into an integrated, concurrent process. It minimizes development
time, enhances design accuracy, and leads to better performance and reliability. An ideal codesign
********** 7 **********
--- page 8 ---
environment supports this integration with unified specifications, tool interoperability, and strong verification
support.
Q A Evaluate how system calls enable communication between application programs and the operating system in   [10
5   embedded environments. Discuss how improper system call management can affect system performance and   ]
reliability.
System calls are special functions provided by the operating system that allow application programs to
request specific services from the kernel.
In embedded systems, they serve as a controlled interface between user-level applications and system-level
resources such as hardware devices, memory, and peripherals.
Role of System Calls in Embedded Environments:
• Provide a secure and standardized way for applications to access OS resources without directly manipulating
hardware.
• Enable essential operations such as process management, task scheduling, file access, communication, and
interrupt handling.
• Support real-time constraints by allowing applications to request deterministic services (e.g., task delay,
event wait, semaphore control).
• Ensure isolation between user tasks and kernel operations, preventing user code from corrupting system
data.
• Simplify application development by abstracting low-level details and exposing clear APIs.
• Examples of system calls in embedded RTOS: osDelay(), osSemaphoreWait(), osMessageQueuePut(),
read(), write().
How System Calls Enable Communication:
• When an application invokes a system call, it triggers a software interrupt (SWI) or trap instruction that
transfers control to the kernel in supervisory mode.
• The kernel executes the requested service (e.g., allocate memory, read sensor data, start a timer).
• Once completed, control returns to the application in user mode with the result or status code.
• This mechanism ensures safe, controlled communication between user applications and system-level
services.
Impact of Improper System Call Management:
• Increased Latency: Excessive or poorly timed system calls can cause frequent context switches, increasing
task response time and violating real-time deadlines.
• Resource Contention: Uncontrolled access to shared resources (files, devices, or buffers) through system
calls can lead to race conditions and deadlocks.
• Kernel Overhead: Repeated calls to non-critical services burden the CPU, lowering system throughput.
• Security Risks: Mismanaged calls may allow unauthorized access to protected memory or device registers.
• Memory Leaks: Failing to release OS-allocated resources after system calls (e.g., semaphores, queues)
degrades performance over time.
• Reduced Reliability: Unchecked return values or improper error handling can cause unpredictable behavior
or system crashes in safety-critical applications.
Good System Call Practices in Embedded Systems:
• Use minimal and optimized system calls in real-time tasks to reduce kernel transition overhead.
• Validate all parameters before invoking system calls to prevent illegal access or null references.
• Group related system calls logically to minimize switching and improve performance.
********** 8 **********
--- page 9 ---
• Implement proper error handling, timeout mechanisms, and watchdog monitoring for robust operation.
• Profile and optimize system call usage during real-time testing to ensure predictable behavior.
Evaluation Summary:
System calls form the vital communication bridge between applications and the OS kernel in embedded
systems, ensuring safe and structured access to hardware and services. Proper management of system calls
maintains determinism, performance, and security, whereas poor management can lead to latency,
instability, and reliability failures in real-time embedded environments.
Q B   Explain the sequence of steps involved in creating an executable image for an embedded system. Discuss how [10
5   the compiler, assembler, linker, and locator collectively transform source code into a target-specific binary   ]
image. Support your answer with a labeled diagram showing the relationship between host and target systems.
In embedded systems, the software development process involves generating a target-specific executable
image on a host computer, which is later downloaded to the target hardware for execution.
The toolchain used includes the compiler, assembler, linker, and locator, which work together to produce
the final binary.
Step 1: Source Code Creation (on Host System)
• Developers write high-level source code in C or C++ using an IDE or text editor.
• Code includes application logic, hardware drivers, and RTOS functions.
• Example: main.c, sensor.c, motor.c.
Step 2: Compilation
• The compiler translates high-level C/C++ code into assembly language instructions specific to the target
processor architecture.
• Performs optimizations, syntax checking, and generates intermediate files (.asm or .obj).
• Example: ARM GCC or Keil compiler generates ARM assembly code.
Step 3: Assembly
• The assembler converts the assembly instructions into machine code (object files with .o or .obj
extensions).
• Produces symbol tables and relocatable object code.
• Each source file becomes one object file, ready for linking.
Step 4: Linking
• The linker combines multiple object files into a single executable file.
• Resolves external symbols, function calls, and global variables used across different modules.
• Links with standard libraries (e.g., math, RTOS kernel, device drivers).
• Produces a partially complete executable known as an absolute object file (.elf or .axf).
Step 5: Location and Image Generation
• The locator (also called the linker-locator) assigns physical memory addresses to the program segments
(code, data, stack, heap).
• Generates the final binary/hex image that matches the target’s memory map.
• Output formats include .bin, .hex, or .srec, ready for download to Flash or ROM.
Step 6: Downloading to Target System
• The final image is transferred from the host system to the target hardware via interfaces such as JTAG,
********** 9 **********
--- page 10 ---
UART, or USB.
• A bootloader or programmer writes the image into the target’s memory for execution.
Step 7: Execution and Debugging
• Once loaded, the target processor executes the image.
• Debuggers (GDB, Keil μVision) on the host allow step-by-step verification, breakpoints, and memory
inspection.
Q A Explain the concept of priority inversion in real-time embedded systems. Describe how it affects task scheduling [10
6   and system performance, and discuss suitable techniques used to minimize or prevent this problem.   ]
• Priority inversion occurs when a high-priority task is indirectly blocked by a low-priority task because
the low-priority task holds a shared resource that the high-priority task needs. Meanwhile, medium-priority
tasks may preempt the low-priority one, causing the high-priority task to wait longer.
• Example:
• Task T1 – High Priority (needs shared resource)
• Task T2 – Low Priority (holding that resource)
• Task T3 – Medium Priority (independent but preempts T2)
Here, T3 delays T2, which in turn delays T1, creating an inversion of priorities.
• Effects on Task Scheduling and System Performance:
• Causes high-priority tasks to miss deadlines, breaking real-time constraints.
• Reduces system predictability and determinism.
• Increases response latency and context-switching overhead.
• May cause task starvation when medium-priority tasks keep preempting the lower one.
• Degrades system reliability and performance in safety-critical systems like automotive ECUs or robotic
control.
• Techniques to Minimize or Prevent Priority Inversion:
• Priority Inheritance Protocol (PIP):
The low-priority task holding the resource temporarily inherits the priority of the highest-priority task waiting
for it, preventing medium-priority preemption.
• Priority Ceiling Protocol (PCP):
Each shared resource is assigned a ceiling priority equal to the highest task priority that can access it. A task
can only lock a resource if its priority is higher than the current ceiling, preventing deadlocks and bounding
blocking time.
• Immediate Ceiling Protocol (ICPP):
When a task locks a resource, it immediately executes at the ceiling priority until it releases the resource,
ensuring no other task can preempt it.
• Non-blocking Design Approaches:
Use lock-free algorithms, message queues, or event-driven designs to minimize resource sharing.
• Watchdog Monitoring:
Detects and logs priority inversion cases during execution for system tuning.
• Practical Example:
In an automotive braking ECU, a low-priority diagnostic task holding a bus resource can delay a high-priority
braking control task. Applying priority inheritance allows the diagnostic task to complete quickly, restoring
real-time responsiveness.
• Summary:
Priority inversion disrupts real-time scheduling by allowing lower-priority tasks to block critical ones.
Techniques such as priority inheritance and priority ceiling protocols ensure bounded blocking time,
improved predictability, and higher reliability in real-time embedded systems.
********** 10 **********
--- page 11 ---
Q B Implement the following Boolean functions using a suitable PAL.   [10
6   Let inputs be x,y,z(both true and complemented forms available).   ]
A(x,y,z)=Σ (1,2,4,6)
B(x,y,z)=Σ(0,1,6,7)
C(x,y,z)=Σ(2,6)
Tasks (show working):
i.   Obtain minimized SOP for A,B,C, (K-maps or equivalent) and identify shared product terms across
the four outputs. (3M)
ii.   Prepare the PAL specification table: list product terms, their input literals, and map them to outputs
A,B,C. (2M)
iii.   Draw the PAL programming matrix/connection diagram (AND/OR planes), clearly indicating
intact/blown fuses (or marked connections). (3M)
iv.   State the minimum number of product terms your design uses and justify how sharing was achieved.
(2M)
********** 11 **********
--- page 12 ---
Q   Describe the Hardware–Software Codesign flow from system specification to integration and testing. Explain [10
7 A how concurrent and integrated development of hardware and software improves design quality and reduces   ]
iteration effort.
Hardware–Software Codesign is an integrated design methodology in which hardware and software
components are developed concurrently from a unified system specification. It aims to achieve optimal
performance, cost, and time efficiency for embedded systems.
Codesign Flow — Step-by-Step Process:
• 1. System Specification:
The design begins with defining overall system requirements — functionality, timing, power, cost, and
performance goals.
A unified, high-level executable specification (using UML, SystemC, or MATLAB models) describes both
hardware and software behavior.
• 2. System Partitioning:
The system functions are divided between hardware (to improve performance or meet timing constraints) and
software (for flexibility and cost efficiency).
Design space exploration evaluates different partition alternatives to achieve optimal trade-offs.
• 3. Hardware Design:
Hardware blocks identified from partitioning are implemented using HDL (VHDL/Verilog/SystemVerilog).
Synthesis tools generate gate-level circuits and optimize area, speed, and power.
Hardware prototypes (FPGA or simulation) validate timing and functionality.
• 4. Software Design:
Software components (RTOS, drivers, application logic) are developed in parallel using C/C++ or assembly.
Tasks are implemented, tested, and profiled on virtual platforms or simulators before real hardware is ready.
• 5. Co-Simulation and Verification:
Hardware and software modules are simulated together using co-simulation tools (e.g., ModelSim, QEMU, or
SystemC).
This stage detects interface mismatches, synchronization issues, and timing violations early.
• 6. Integration:
Hardware (FPGA/ASIC) and software (firmware, drivers, RTOS) are integrated on the target platform.
Communication interfaces, buses, and interrupts are validated for correct operation.
The integration ensures the system meets functional and timing specifications.
• 7. Testing and Validation:
The integrated system undergoes hardware-in-the-loop (HIL) testing and performance validation.
Functional, timing, and stress tests confirm that the design meets reliability and real-time constraints.
Verified models are used for regression and future reuse.
Concurrent and Integrated Development Benefits:
• Reduced Development Time: Parallel hardware and software development shortens the overall project
timeline.
• Early Error Detection: Co-simulation identifies integration and interface issues before hardware
fabrication.
• Improved Design Quality: Shared specifications and synchronized models ensure functional consistency
and reduce human errors.
• Better Resource Optimization: Partitioning enables balancing of performance (hardware) and flexibility
(software).
• Lower Iteration Effort: Unified modeling reduces redesign cycles caused by late discovery of cross-
********** 12 **********
--- page 13 ---
domain issues.
• Enhanced Collaboration: Cross-functional teams (hardware, firmware, and application engineers) work on
shared design databases.
Q B Compare FPGA, ASIC, and PSOC technologies with respect to their architecture, design flexibility,   [10
7   performance, and cost. Explain how these factors influence the choice of implementation for various embedded   ]
system applications.
********** 13 **********

[Text in pictures on this page, read by OCR]
Feature FPGA ASIC PSOC

Architecture Configurable logic blocks and Fully customized gate- MCU core + programmable
routing matrix level design analog/digital blocks
Design Flexibility High (reconfigurable) None (fixed post- Moderate (reconfigurable mixed-sic
fabrication)
Performance Medium to high Very high Moderate
Power Consumption Moderate to high Very low Low
Development Time Short (ready-to-program) Long (requires Short to moderate

fabrication)

Cost per Unit High for low-volume, low for Very low for large Moderate
prototypes volume, high NRE
Typical Use Prototyping, DSP, Communication Mass-market high-speed Low-power, mixed-signal embeddec

applications systems
````
