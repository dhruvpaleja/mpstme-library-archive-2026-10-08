# Fundamentals of Operating Systems: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 149b19dbdfb9

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/Integrated_IT_7037/Fundamentals of Operating Systems/ANS_Fundamentals of Operating Systems(701IT0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (29 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Fundamentals of Operating Systems
Date: 11 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 29 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain the functions of an Operating System.
The OS manages the life cycle of processes.
Key Activities:
• Creation and termination of processes
• CPU scheduling (deciding execution order)
• Process synchronization (avoiding race conditions)
•   Inter-process communication
👉 Deep Insight:
CO-1 ;   The OS must maintain fairness + efficiency, ensuring no process
SO-2 ;   monopolizes CPU.
BL-2   👉 Example:
While running Chrome + VS Code + Zoom → OS schedules CPU
among them.
2. Memory Management
The OS manages main memory (RAM) allocation.
Responsibilities:
• Tracks memory usage
•   Allocates/deallocates memory
• Prevents memory overlap
********** 1 **********
--- page 2 ---
Advanced Concepts:
• Paging → divides memory into pages
• Segmentation → logical division
•   Virtual Memory → illusion of large memory
👉 Insight:
Memory management ensures isolation + protection, preventing one
process from corrupting another.
3. File System Management
The OS organizes data into files and directories.
Functions:
•   File creation, deletion
• Read/write operations
•   Directory structure maintenance
• Access control
👉 Example:
Saving a file → OS maps logical file to physical disk blocks.
4. I/O and Device Management
The OS manages hardware devices.
Mechanisms:
• Device drivers
• Buffering → temporary storage
• Caching → faster access
• Spooling → queueing
👉 Insight:
CPU is much faster than devices → OS bridges this speed gap.
5. Secondary Storage Management
• Manages disk allocation
• Free space management
• Disk scheduling
6. Security and Protection
•   Authentication (login systems)
•   Authorization (permissions)
• Data protection
👉 Example:
File permission system in Linux (rwx)
7. Deadlock Handling
OS may:
********** 2 **********
--- page 3 ---
• Prevent deadlock
• Avoid deadlock
• Detect and recover
8. User Interface
• CLI (Linux terminal)
• GUI (Windows interface)
b.   Describe the different types of threads in an operating system.
A thread is the smallest unit of CPU execution within a process.
Why Threads?
•   Faster execution
•   Better resource sharing
• Improved responsiveness
1. User-Level Threads (ULT)
Characteristics:
• Managed by user libraries
• OS is unaware
CO-2 ;
SO- 2;   Advantages:
BL-2
•   Fast creation and switching
• No kernel involvement
Limitations:
• Blocking system call blocks entire process
• No parallelism on multi-core
👉 Example: Java user threads
2. Kernel-Level Threads (KLT)
Characteristics:
• Managed by OS kernel
Advantages:
• True parallel execution
********** 3 **********
--- page 4 ---
•   Better scheduling
Disadvantages:
• Higher overhead
👉 Example: Windows threads
3. Hybrid Thread Model
Concept:
• Many user threads mapped to multiple kernel threads
Advantages:
• Combines efficiency + parallelism
👉 Example: Solaris
c.   What is a deadlock? Explain its necessary conditions.
What is Deadlock?
A deadlock is a situation where a set of processes are permanently
blocked, each waiting for a resource held by another process.
Graph-Based Understanding
Deadlock can be represented using a Resource Allocation Graph
(RAG).
👉 Cycle in graph ⇒ Deadlock (for single instance resources)
Four Necessary Conditions (Coffman Conditions)
CO-3 ;   1. Mutual Exclusion
SO-2 ;
BL-3   • Resource cannot be shared
👉 Example: Printer
2. Hold and Wait
• Process holds one resource and waits for another
3. No Preemption
• Resource cannot be taken forcibly
********** 4 **********
--- page 5 ---
4. Circular Wait
•   Circular chain exists
👉 Example:
P1 → P2 → P3 → P1
🔥 Key Insight
Deadlock occurs only when all four conditions hold simultaneously
d.   Describe the process states with a suitable diagram.
A process moves through different states during execution.
Process State Diagram
New → Ready → Running → Waiting → Ready → Terminated
Detailed Explanation
1. New
• Process is being created
2. Ready
• Process waiting for CPU
CO-2 ;   3. Running
SO- 2;
BL-2   • Process currently executing
4. Waiting (Blocked)
• Waiting for I/O or event
5. Terminated
• Process execution completed
Transitions
• Ready → Running → CPU allocated
• Running → Waiting → I/O request
• Waiting → Ready → I/O complete
********** 5 **********
--- page 6 ---
a.   Explain the concept of Process Control Block (PCB) and describe its
components.
Definition of PCB
A Process Control Block (PCB) is a data structure maintained by
the operating system that contains all the information required to
b.   manage and execute a process.
It acts as a record for each process and is stored in the kernel space.
2. Purpose of PCB
• To store the current state of a process
• To enable process management and scheduling
• To support context switching
• To keep track of resources used by the process
3. Role in Context Switching
When the CPU switches from one process to another:
1. The current process state is saved in its PCB
2. The next process state is loaded from its PCB
Q2   Thus, PCB allows the OS to resume a process exactly from where it
stopped.
CO-2;
[20]
SO-2;   4. Components of PCB (Detailed)
BL-
2,BL3
1. Process Identification Information
• Process ID (PID)
•   Parent Process ID
Used to uniquely identify a process in the system
2. Process State
• New
• Ready
• Running
• Waiting
• Terminated
Indicates the current status of the process
3. Program Counter (PC)
•   Stores the address of the next instruction to be executed
Ensures correct execution after interruption
********** 6 **********
--- page 7 ---
4. CPU Registers
• General-purpose registers
• Stack pointer
•   Instruction register
Stores execution context of the process
5. CPU Scheduling Information
• Process priority
• Scheduling queue pointers
• Time slice
Used by CPU scheduler to select processes
6. Memory Management Information
• Base and limit registers
• Page table or segment table
Helps in memory allocation and protection
7. I/O Status Information
•   List of open files
• Devices allocated
• Pending I/O operations
8. Accounting Information
• CPU usage time
• Execution time limits
• Job number
Used for system monitoring and billing
5. PCB Structure Representation
+------------------------+
| Process ID   |
| Process State   |
| Program Counter   |
| CPU Registers   |
| Scheduling Info   |
| Memory Info   |
| I/O Status   |
| Accounting Info   |
+------------------------+
********** 7 **********
--- page 8 ---
Describe different multithreading models used in operating systems
with suitable examples.
b) Multithreading Models (10 Marks)
1. Definition of Thread
A thread is the smallest unit of execution within a process.
Threads share the same memory and resources but have their own
execution context.
2. Need for Multithreading
• Improves system performance
• Enables concurrent execution
•   Increases responsiveness
•   Efficient resource utilization
3. Multithreading Models
These models define how user-level threads are mapped to kernel-
level threads.
✅ 1. Many-to-One Model
Concept
• Multiple user threads are mapped to a single kernel thread
Working
• Thread management is done at user level
• OS is not aware of multiple threads
Advantages
•   Fast thread creation and switching
• No kernel involvement
Disadvantages
•   If one thread blocks, entire process blocks
• No parallel execution on multi-core systems
Example
• Early Java threading model
********** 8 **********
--- page 9 ---
✅ 2. One-to-One Model
Concept
• Each user thread is mapped to a separate kernel thread
Working
• OS schedules each thread independently
Advantages
• True parallelism
• Blocking of one thread does not affect others
Disadvantages
• High overhead due to kernel involvement
• Limited number of threads
Example
• Windows OS
• Linux (modern systems)
✅ 3. Many-to-Many Model
Concept
• Many user threads are mapped to many kernel threads
Working
• OS dynamically maps user threads to kernel threads
Advantages
• Combines benefits of both models
• Supports parallel execution
• Avoids blocking problem
********** 9 **********
--- page 10 ---
Disadvantages
• Complex implementation
Example
•   Solaris
4. Comparison of Multithreading Models
Many-to-   One-to-   Many-to-
Feature
One   One   Many
Parallelism No   Yes   Yes
Overhead   Low   High   Moderate
Blocking
Yes   No   No
Issue
Complexity   Simple   Moderate Complex
5. Summary
• PCB is essential for managing process execution and enabling
context switching
•   Multithreading improves performance and concurrency
•   Different models provide trade-offs between efficiency and
complexity
a.   Explain the concept of semaphores and describe their types with
examples.
a) Semaphores – Concept, Types, and Examples (10
Marks)
Q3
1. Introduction to Synchronization
CO-3;   In a multiprogramming system, multiple processes execute concurrently
[20]
SO-2;   and may share resources such as memory, files, or variables.
BL-3 and   This can lead to race conditions if proper synchronization is not
BL-4   maintained.
To avoid such issues, synchronization mechanisms like semaphores are
used.
2. Definition of Semaphore
A semaphore is a synchronization primitive used to control access to
shared resources by multiple processes in a concurrent system.
It is a non-negative integer variable that is accessed only through two
atomic operations:
********** 10 **********
--- page 11 ---
•   wait() (P operation)
•   signal() (V operation)
3. Semaphore Operations
wait(S):
• Decrements the semaphore value
•   If S ≤ 0 → process waits (blocked or busy waits)
wait(S):
while(S <= 0);   // busy waiting
S = S - 1;
signal(S):
• Increments the semaphore value
• Wakes up a waiting process
signal(S):
S = S + 1;
4. Types of Semaphores
1. Binary Semaphore (Mutex)
• Value can be 0 or 1
• Used for mutual exclusion
Working:
• S = 1 → resource available
• S = 0 → resource in use
Example:
wait(S);
Critical Section
signal(S);
Ensures only one process enters critical section at a time.
2. Counting Semaphore
• Value can be greater than 1
• Used when multiple instances of a resource are available
Example:
If 3 printers are available:
•   Initialize S = 3
• Each process uses wait(S) before using printer
5. Example of Semaphore Usage (Producer–Consumer Concept)
********** 11 **********
--- page 12 ---
• Producer produces items
• Consumer consumes items
• Semaphores ensure:
o No overflow
o No underflow
6. Advantages of Semaphores
• Prevent race conditions
• Provide synchronization
• Ensure mutual exclusion
7. Disadvantages
• Busy waiting wastes CPU time
•   Difficult to debug
• Improper use may lead to deadlock
Explain the Dining Philosophers problem and discuss a suitable
solution to avoid deadlock.
Dining Philosophers Problem (10 Marks)
1. Problem Description
b.
The Dining Philosophers problem is a classical synchronization
problem that demonstrates issues like deadlock and starvation.
2. Scenario
• 5 philosophers sit around a circular table
• 5 forks are placed between them
• Each philosopher needs two forks (left and right) to eat
• Philosophers alternate between:
o Thinking
o Eating
3. Problem
If all philosophers pick up one fork at the same time:
• Each philosopher holds one fork
• Each waits for the other fork
• No one can proceed
👉 This leads to deadlock
4. Representation
********** 12 **********
--- page 13 ---
P1   P2   P3   P4   P5
|   |   |   |   |
F1   F2   F3   F4   F5
5. Deadlock Condition in This Problem
All four deadlock conditions are satisfied:
• Mutual exclusion → forks cannot be shared
• Hold and wait → each philosopher holds one fork
• No preemption → cannot take fork forcibly
•   Circular wait → circular dependency exists
6. Solutions to Avoid Deadlock
1. Limiting Number of Philosophers
• Allow only 4 philosophers to sit at a time
• At least one philosopher can always eat
2. Resource Ordering
• Number the forks
• Each philosopher picks forks in increasing order
👉 Breaks circular wait
3. Using Semaphores (Classic Solution)
Initialize:
• Forks → binary semaphores
• Global semaphore S = 4
wait(S); // limit philosophers
wait(fork[i]);
wait(fork[(i+1)%5]);
// Eating
signal(fork[i]);
signal(fork[(i+1)%5]);
signal(S);
4. Monitor-Based Solution (Conceptual)
• Use condition variables
• Allow eating only if neighbors are not eating
7. Starvation Issue
Even if deadlock is avoided, some philosophers may never get chance
to eat.
********** 13 **********
--- page 14 ---
Solution:
•   Fair scheduling
• Queue-based access
8. Key Understanding
• Problem models real-world resource allocation
• Used in designing:
o Database locks
o OS scheduling systems
✅ FINAL SUMMARY
Concept   Key Idea
Controls access to shared
Semaphore
resources
Binary Semaphore Mutual exclusion
Counting
Multiple resources
Semaphore
Dining Philosophers Deadlock scenario
Solution   Break deadlock conditions
a.   Consider the following set of processes:
Proces   Arrival   Burst
s   Time   Time
P1   0   10
P2   1   5
Q4
P3   2   8
CO-2;   P4   3   6
SO-2;   [20]
BL-3   Apply Round Robin Scheduling (Preemptive, Time Quantum = 3
ms) and:
and BL-4   i) Draw the Gantt Chart (4 Marks)
ii) Calculate Completion Time (CT), Turnaround Time (TAT), and
Waiting Time (WT) for each process (4 Marks)
iii) Compute Average Waiting Time and Average Turnaround Time
(2 Marks)
b.
Consider the following set of processes:
********** 14 **********
--- page 15 ---
Proces   Arrival   Burst   Priorit
s   Time   Time   y
P1   0   10   3
P2   1   5   1
P3   2   8   4
P4   3   6   2
(Lower number indicates higher priority)
Apply Priority Scheduling (Non-Preemptive) and:
i) Draw the Gantt Chart (4 Marks)
ii) Calculate Completion Time (CT), Turnaround Time (TAT), and
Waiting Time (WT) (4 Marks)
iii) Compute Average Waiting Time and Average Turnaround Time
(2 Marks)
Q4 a) Round Robin Scheduling (tq = 3 ms) – (10
Marks)
Given:
Proces   Arrival Time   Burst Time
s   (AT)   (BT)
P1   0   10
P2   1   5
P3   2   8
P4   3   6
Step 1: Execution Order (Round Robin Logic)
Time quantum = 3 ms
Processes are executed in FIFO order of ready queue
Execution Timeline
• 0–3: P1 → remaining = 7
• 3–6: P2 → remaining = 2
• 6–9: P3 → remaining = 5
• 9–12: P4 → remaining = 3
• 12–15: P1 → remaining = 4
• 15–17: P2 → completes
• 17–20: P3 → remaining = 2
• 20–23: P4 → completes
• 23–26: P1 → remaining = 1
• 26–28: P3 → completes
• 28–29: P1 → completes
i) Gantt Chart (4 Marks)
********** 15 **********
--- page 16 ---
0–3 P1 | 3–6 P2 | 6–9 P3 | 9–12 P4 | 12–15 P1 | 15–17 P2
|
17–20 P3 | 20–23 P4 | 23–26 P1 | 26–28 P3 | 28–29 P1
ii) Completion Time (CT), Turnaround Time (TAT), Waiting Time
(WT) (4 Marks)
Completion Time (CT)
Proces C
s   T
2
P1
9
1
P2
7
2
P3
8
2
P4
3
Turnaround Time (TAT = CT – AT)
Proces
TAT
s
29 – 0 =
P1
29
17 – 1 =
P2
16
28 – 2 =
P3
26
23 – 3 =
P4
20
Waiting Time (WT = TAT – BT)
Proces
WT
s
29 – 10 =
P1
19
P2   16 – 5 = 11
P3   26 – 8 = 18
P4   20 – 6 = 14
iii) Averages (2 Marks)
• Average WT = (19 + 11 + 18 + 14) / 4 = 62 / 4 = 15.5 ms
• Average TAT = (29 + 16 + 26 + 20) / 4 = 91 / 4 = 22.75 ms
********** 16 **********
--- page 17 ---
🔷 Q4 b) Priority Scheduling (Non-Preemptive) –
(10 Marks)
Given:
Proces A B Priorit
s   T T   y
P1   0 10 3
P2   1 5 1
P3   2 8 4
P4   3 6 2
👉 Lower number = higher priority
Step 1: Scheduling Logic
• Non-preemptive → once started, process runs fully
•   Select highest priority among available processes
Execution Timeline
• t=0–10: P1 (only process available at start)
• At t=10 → choose highest priority among P2, P3, P4
→ P2 (priority 1)
• t=10–15: P2
• Next highest priority → P4 (priority 2)
• t=15–21: P4
•   Last → P3
• t=21–29: P3
i) Gantt Chart (4 Marks)
0–10 P1 | 10–15 P2 | 15–21 P4 | 21–29 P3
ii) CT, TAT, WT (4 Marks)
Completion Time
Proces C
s   T
1
P1
0
1
P2
5
2
P3
9
2
P4
1
********** 17 **********
--- page 18 ---
Turnaround Time (TAT = CT – AT)
Proces
TAT
s
10 – 0 =
P1
10
15 – 1 =
P2
14
29 – 2 =
P3
27
21 – 3 =
P4
18
Waiting Time (WT = TAT – BT)
Proces
WT
s
10 – 10 =
P1
0
P2   14 – 5 = 9
27 – 8 =
P3
19
18 – 6 =
P4
12
iii) Averages (2 Marks)
• Average WT = (0 + 9 + 19 + 12) / 4 = 40 / 4 = 10 ms
• Average TAT = (10 + 14 + 27 + 18) / 4 = 69 / 4 = 17.25 ms
✅ FINAL OBSERVATION (FOR ANSWER QUALITY)
• Round Robin ensures fairness but increases waiting time
•   Priority scheduling reduces waiting for high-priority processes
but may cause starvation
a.   Consider a system with the following Resource Allocation Graph
Q5   (RAG):
CO-4 and   •   Processes: P1, P2, P3
CO3; SO-   • Resources (single instance): R1, R2, R3   [20]
2;
BL-3   Edges:
and BL-4
• P1 → R1
• R1 → P2
********** 18 **********
--- page 19 ---
• P2 → R2
• R2 → P3
• P3 → R3
• R3 → P1
Answer the following:
i) Draw the Resource Allocation Graph (RAG). (3 Marks)
ii) Determine whether a deadlock exists. Justify your answer using
cycle detection. (3 Marks)
iii) Explain the necessary conditions for deadlock. (4 Marks)
i) Resource Allocation Graph (RAG)
b.
Representation of given system:
• Processes: P1, P2, P3 (circles)
• Resources: R1, R2, R3 (rectangles, single instance)
Edges:
• P1 → R1 (request)
• R1 → P2 (allocated)
• P2 → R2 (request)
• R2 → P3 (allocated)
• P3 → R3 (request)
• R3 → P1 (allocated)
Graph Structure (text form):
P1 → R1 → P2 → R2 → P3 → R3 → P1
********** 19 **********
--- page 20 ---
This forms a closed loop (cycle).
ii) Deadlock Detection using Cycle
Yes, deadlock exists.
Justification:
• There is a cycle in the RAG:
P1 → R1 → P2 → R2 → P3 → R3 → P1
• Since each resource has a single instance, the presence of a
cycle is both necessary and sufficient condition for deadlock.
Therefore, all processes P1, P2, P3 are deadlocked, each waiting
for a resource held by another process in the cycle.
iii) Necessary Conditions for Deadlock (Coffman Conditions)
A deadlock occurs only if all four conditions hold simultaneously:
1. Mutual Exclusion
At least one resource must be held in a non-shareable mode.
(e.g., R1, R2, R3 are single-instance resources)
2. Hold and Wait
A process holding at least one resource is waiting for additional
resources.
(e.g., P1 holds R3 indirectly and waits for R1)
3. No Preemption
Resources cannot be forcibly taken; they must be released
voluntarily.
4. Circular Wait
A circular chain of processes exists where each process is
waiting for a resource held by the next process.
(P1 → P2 → P3 → P1)
In this problem, all four conditions are satisfied, hence deadlock
occurs.
If you want, I can convert this into a perfect 10-mark synoptic answer
table (faculty audit format) or diagram-only printable version for
exam solution.
********** 20 **********
--- page 21 ---
Given memory partitions of sizes 100 KB, 500 KB, 200 KB, 300 KB,
and 600 KB (in order), and processes of sizes 212 KB, 417 KB, 112
KB, and 426 KB:
Answer the following:
i) Allocate memory using First Fit, Best Fit, and Worst Fit methods.
(6 Marks)
ii) Show the final memory allocation for each method clearly. (2
Marks)
iii) Compare the methods based on memory utilization and
fragmentation. (2 Marks).
Memory Management – Partitioning Numerical (10
Marks)
Given:
Memory Blocks (in order):
100 KB, 500 KB, 200 KB, 300 KB, 600 KB
Processes:
P1 = 212 KB
P2 = 417 KB
P3 = 112 KB
P4 = 426 KB
🔷 i) Allocation using Different Methods (6 Marks)
✅ 1. First Fit
👉 Allocate the first available block that is large enough
Stepwise Allocation
• P1 (212 KB) → first suitable = 500 KB → remaining = 288 KB
• P2 (417 KB) → next suitable = 600 KB → remaining = 183 KB
• P3 (112 KB) → first suitable = 288 KB → remaining = 176 KB
• P4 (426 KB) → no suitable block available
Final Allocation (First Fit)
Block   Status
100 KB   Not used
500 KB →   288 → P3 → 176
P1   left
200 KB   Not used
300 KB   Not used
********** 21 **********
--- page 22 ---
600 KB →
183 left
P2
👉 P4 not allocated
✅ 2. Best Fit
👉 Allocate the smallest block that fits
Stepwise Allocation
• P1 (212 KB) → best fit = 300 KB → remaining = 88 KB
• P2 (417 KB) → best fit = 500 KB → remaining = 83 KB
• P3 (112 KB) → best fit = 200 KB → remaining = 88 KB
• P4 (426 KB) → best fit = 600 KB → remaining = 174 KB
Final Allocation (Best Fit)
Block   Status
Not
100 KB
used
500 KB →
83 left
P2
200 KB →
88 left
P3
300 KB →
88 left
P1
600 KB →
174 left
P4
👉 All processes allocated successfully
✅ 3. Worst Fit
👉 Allocate the largest available block
Stepwise Allocation
• P1 (212 KB) → largest = 600 KB → remaining = 388 KB
• P2 (417 KB) → largest = 500 KB → remaining = 83 KB
• P3 (112 KB) → largest = 388 KB → remaining = 276 KB
• P4 (426 KB) → no suitable block
Final Allocation (Worst Fit)
Block   Status
Not
100 KB
used
500 KB → P2   83 left
********** 22 **********
--- page 23 ---
Not
200 KB
used
Not
300 KB
used
600 KB → P1 →
276 left
P3
👉 P4 not allocated
🔷 ii) Final Allocation Summary (2 Marks)
Processes   Unallocate
Method
Allocated   d
First Fit P1, P2, P3   P4
Best Fit P1, P2, P3, P4   None
Worst
P1, P2, P3   P4
Fit
🔷 iii) Comparison (2 Marks)
Memory   Fragmentatio
Method   Observation
Utilization   n
First Fit Moderate   Moderate   Fast but leaves gaps
Efficient, all
Best Fit High   Low
allocated
Worst
Low   High   Large space wasted
Fit
✅ Final Conclusion (Write in Exam)
• Best Fit gives best memory utilization as all processes are
allocated
•   First Fit is faster but less efficient
• Worst Fit leads to higher fragmentation and poor utilization
a.
a) A disk system has the following parameters:
Q6   • Spindle speed = 7200 RPM
CO-2 and   • Average seek time = 5 ms
CO4; SO-   •   Transfer rate = 1 Gb/sec
2;   •   Controller overhead = 0.1 ms   [20]
BL-3   • Block size = 4 KB
and BL-2   Answer the following:
i) Calculate the average rotational latency (2 Marks)
ii) Calculate the average access time (seek time + latency) (2 Marks)
********** 23 **********
--- page 24 ---
iii) Calculate the transfer time for the given block (3 Marks)
iv) Compute the total average I/O time (3 Marks)
Disk Performance Calculation
Given Data:
b.
Spindle Speed (N) = 7200 RPM
Average Seek Time = 5 ms
Transfer Rate = 1 Gb/sec = 10^9 bits/sec
Controller Overhead = 0.1 ms
Block Size = 4 KB = 4 × 1024 × 8 = 32768 bits
i) Average Rotational Latency (2 Marks)
Formula:
Latency = (1/2) × (60 / RPM)
Calculation:
= (1/2) × (60 / 7200)
= (1/2) × 0.00833
= 0.00417 sec
Convert to milliseconds:
= 0.00417 × 1000 = 4.17 ms
Answer: Average Rotational Latency = 4.17 ms
ii) Average Access Time (2 Marks)
Formula:
Access Time = Seek Time + Rotational Latency
Calculation:
= 5 + 4.17 = 9.17 ms
Answer: Average Access Time = 9.17 ms
iii) Transfer Time (3 Marks)
Formula:
Transfer Time = Block Size / Transfer Rate
Calculation:
= 32768 / 10^9
= 3.2768 × 10^-5 sec
Convert to milliseconds:
= 0.0327 ms ≈ 0.03 ms
Answer: Transfer Time ≈ 0.03 ms
iv) Total Average I/O Time (3 Marks)
Formula:
I/O Time = Access Time + Transfer Time + Overhead
Calculation:
= 9.17 + 0.03 + 0.1 = 9.30 ms
Answer: Total Average I/O Time = 9.30 ms
Describe the file system concept in an operating system. Explain
various file attributes and operations, along with different access
methods.
1. Definition of File System
A file system is a method used by the operating system to store,
organize, manage, and retrieve data on storage devices.
It provides a logical abstraction of physical storage.
********** 24 **********
--- page 25 ---
2. File Attributes
Each file has metadata describing its properties:
• Name – Identifier of file
• Type – Text, binary, executable
•   Size – File length
• Location – Storage address
• Permissions – Read, write, execute
• Time stamps – Creation/modification
3. File Operations
Operating system provides various operations:
• Create – Create a new file
• Open – Access file
• Read – Retrieve data
• Write – Store data
• Close – Release file
• Delete – Remove file
4. File Access Methods
1. Sequential Access
• Data accessed in order
• Simple but slow
👉 Example: Reading a log file
2. Direct (Random) Access
• Access any record directly
•   Faster than sequential
👉 Example: Database access
3. Indexed Access
• Uses index to locate data
•   Efficient for large files
👉 Example: Library system
5. Importance of File System
• Organizes data efficiently
• Enables fast retrieval
• Provides security and protection
• Supports multi-user access
********** 25 **********
--- page 26 ---
✅ FINAL SUMMARY
Part   Result
4.17
Latency
ms
9.17
Access Time
ms
Transfer   0.03
Time   ms
Total I/O   9.30
Time   ms
Select any four .
a) Evolution of OS.
b) IPC types.
c) File Access control.
d) Explain any four Linux operating system commands.
e) Internal fragmentation and External Fragmentation.
a) Evolution of Operating Systems
Q7   Operating Systems have evolved over time to improve efficiency, user
CO-   interaction, and resource utilization.
1,CO-
2,CO-   1. Batch Operating System (1950s–1960s)
[20]
3,CO-4;
SO-2;   • Jobs were collected and executed in batches
BL-2   • No user interaction during execution
• High turnaround time
and BL-3
👉 Example: Early IBM systems
2. Multiprogramming Systems
• Multiple jobs loaded into memory simultaneously
• CPU switches between jobs
• Improves CPU utilization
3. Time-Sharing Systems
•   Interactive systems
• Multiple users share CPU using time slices
• Provides quick response
********** 26 **********
--- page 27 ---
👉 Example: UNIX
4. Distributed Systems
• Multiple computers connected via network
• Resource sharing and load balancing
5. Modern Operating Systems
• Cloud computing
•   Virtualization
• Mobile operating systems
👉 Example: Windows, Linux, Android
🔷 b) IPC (Inter-Process Communication) Types
IPC allows processes to communicate and share data.
1. Shared Memory
• Processes share a common memory space
•   Fast communication
• Requires synchronization
2. Message Passing
• Processes exchange messages via OS
• No shared memory
•   Safer but slower
3. Pipes
•   Unidirectional communication
• Used between related processes
4. Sockets
• Communication over networks
• Used in client-server systems
5. Signals
• Used for process notifications
• Example: interrupt signal
🔷 c) File Access Control
********** 27 **********
--- page 28 ---
File access control ensures security and controlled access to files.
1. Permission-Based Control
• Read (r)
• Write (w)
• Execute (x)
Applied to:
• Owner
• Group
• Others
2. Access Control List (ACL)
•   Specifies permissions for multiple users
•   Fine-grained control
3. User Identification
• Each file has owner and group
• OS verifies user identity
4. Protection Goals
•   Confidentiality
•   Integrity
•   Availability
🔷 d) Linux Operating System
Linux is an open-source, multi-user, multitasking operating system.
Features:
• Open-source (free to use and modify)
• Supports CLI and GUI
• Highly secure
•   Portable across platforms
• Supports multitasking and multi-user environment
Advantages:
• High stability
• Customization flexibility
• Strong security
********** 28 **********
--- page 29 ---
Common Uses:
•   Servers
• Embedded systems
• Development environments
🔷 e) Internal and External Fragmentation
1. Internal Fragmentation
Occurs when allocated memory block is larger than required, leaving
unused space inside.
👉 Example:
Process needs 90 KB but allocated 100 KB → 10 KB wasted
2. External Fragmentation
Occurs when free memory is scattered in small blocks, preventing
allocation of large process.
👉 Example:
Total free memory = 300 KB but in small pieces → cannot allocate 200
KB
Comparison
Internal   External
Feature
Fragmentation   Fragmentation
Locatio   Outside between
Inside allocated block
n   blocks
Cause   Fixed partitioning   Variable partitioning
Solutio
Better allocation   Compaction
n
✅ FINAL SUMMARY
Topic   Key Idea
OS developed from batch to modern
Evolution
systems
IPC   Enables process communication
File Control   Provides secure access
Linux   Open-source OS
Fragmentatio
Memory wastage problem
n
********** 29 **********
````

## 2024-25 · Final-Exam · Sem 6 · Answer key · paper 720e262e9de4

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2024/Sem_06/Final-Exam/Integrated_IT_7037/Fundamentals of Operating Systems/ANS_Fundamentals of Operating Systems(701IT0C008)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2025
- Text: text (8 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Semester VI(Exam Year: 2024-2025)
Subject: Fundamentals of Operating Systems
Date: 07 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions
6. In all ___5_ questions to be attempted.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1 ;   a.   Illustrate the role of an Operating System by discussing how its basic services [5]
SO-2 ; BL-   function in a computer system.
3   a. Role of an Operating System:
• Manages hardware resources such as CPU, memory, and I/O devices.
• Provides a user interface for interaction (CLI or GUI).
• Handles process management including creation, scheduling, and
termination.
• Manages files and directories with file systems.
• Ensures system security and access control.
CO-1 ;   b.   Differentiate between Process and Thread with suitable examples.   [5]
SO-2 ; BL-   b. Difference between Process and Thread:
2   • A process is an independent program in execution with its own memory
space.
• A thread is a lightweight subprocess sharing the same memory space of the
process.
• Threads are faster to create and manage than processes.
• Processes communicate through inter-process communication (IPC),
threads share data easily.
• Example: Chrome browser (Process), each tab (Thread).
CO-2 ;   c.   Apply the concept of Semaphore by solving a synchronization problem with an [5]
SO-2 ; BL-   appropriate example.
3   Semaphore synchronization example:
********** 1 **********
--- page 2 ---
• Semaphore is a synchronization tool to control access to a shared resource.
• Two types: Binary Semaphore (0/1) and Counting Semaphore (non-negative
integer).
• Example: Producer-Consumer problem.
• Producer increments semaphore when producing an item.
• Consumer decrements semaphore when consuming an item to avoid race
conditions.
CO-4;   d.   Illustrate how various CPU scheduling criteria affect the performance of a [5]
SO-2 ; BL-
computer system by providing practical examples.
2
CPU scheduling criteria and system performance:
• CPU utilization – Maximize CPU usage (e.g., RR algorithm).
• Throughput – Number of processes completed per time unit.
• Turnaround time – Total time from submission to completion.
• Waiting time – Time spent waiting in the ready queue.
• Response time – Time from submission to first response (critical for
interactive systems).
Q2   Q2   Consider the set of 6 processes whose arrival time and burst time are given [10]
CO-2;   A   below-
SO-2; BL-3
Process   Arrival Time   Burst Time
𝑃1   0   4
𝑃2   1   5
𝑃3   2   2
𝑃4   3   1
𝑃5   4   6
If   the CPU   𝑃6   6   3   scheduling
policy is Round Robin with time quantum = 2, calculate the average waiting
time and average turnaround time. Also draw Gantt chart.
• Apply Round Robin scheduling with Time Quantum = 2.
• Track the process queue based on arrival time.
• Execute each process for max 2 units or till completion.
• Maintain Gantt chart to visualize execution order.
• Calculate Completion Time (CT) for each process.
• Calculate Turnaround Time (TAT) = CT - Arrival Time.
• Calculate Waiting Time (WT) = TAT - Burst Time.
• Compute average Waiting Time = 7.33
• Compute average Turnaround Time. = 10.83
• Gantt chart and calculation will show fairness but increased context
switches.
• Detailed calculations are illustrated below.
CO-1;   Q2   Explain the significance of user mode and kernel mode in the operating system [10]
SO-2; BL-3   B   architecture, and analyze how context switching between these modes
influences system performance.
********** 2 **********
--- page 3 ---
• User mode is a restricted mode where user applications execute.
• Kernel mode is a privileged mode where OS code runs.
User Mode and Kernel Mode in Operating System Architecture
1. Introduction
Modern operating systems operate in two distinct modes: User Mode and
Kernel Mode. These modes are essential for ensuring system security,
stability, and controlled access to hardware resources.
2. User Mode
•   Definition: A restricted mode in which applications and user-level
programs execute.
•   Features:
o Limited access to system resources.
o No direct access to hardware.
o   If a program crashes, it does not affect the entire system.
• Examples: Running word processors, web browsers, games, etc.
3. Kernel Mode
•   Definition: A privileged mode where the operating system's core
components operate.
•   Features:
o   Full access to hardware and system resources.
o Can execute any CPU instruction.
o Handles process management, memory management, device
control, etc.
• Examples: System calls execution, interrupt handling, memory
allocation.
4. Context Switching Between User Mode and Kernel Mode
Context Switching is the process where the CPU switches from executing in
user mode to kernel mode (or vice versa).
How it Occurs:
• When a user application requests a service via system calls.
•   During interrupts or exceptions.
•   For performing I/O operations.
Q3   A   Assume that there are three resources, A, B, and C. There are 4 processes P0 [10]
CO-4;   to P3. At T0 we have the following snapshot of the system:
SO-2; BL-2   Allocation   MAX   Available
A   B   C   A   B   C   A   B   C
P0   1   0   1   2   1   1   2   1   1
P1   2   1   2   5   4   4
P2   3   0   0   3   1   1
P3   1   0   1   1   1   1
Is the system in a safe state? Why or why not?
********** 3 **********
--- page 4 ---
Q3   B   Using the Interrupt-Driven I/O cycle diagram, demonstrate step-by-step what [10]
CO-2;   happens when a device signals the CPU with an interrupt request. Provide a
SO-2; BL-2   practical scenario to illustrate this process.
A   Demonstrate how Fixed and Dynamic Memory Partitioning techniques
Q4   manage memory allocation by providing suitable examples.
• Fixed Partitioning: Divides memory into fixed-sized partitions.
CO-2;   • Example: 1GB RAM split into four 256MB partitions.   [10]
SO-2; BL-2   • Simple to implement; each process gets one partition.
• Leads to internal fragmentation if process size < partition size.
• Easy process allocation and deallocation.
• Dynamic Partitioning: Allocates memory based on process size.
• No fixed partition size, reducing internal fragmentation.
• Suffering from external fragmentation.
********** 4 **********

[Text in pictures on this page, read by OCR]
sume that there are three resources, A.B, and C_ There sre 4 processes Po to Py. At To
we have the following snapshot of the system:
Allocation Max — | Available |] 1 Create the need mari.
‘Need
A |e fe fals]eclalale a Tele
Pi 3 2
> 3 Ts
esto fe ts ffi aot
—+> = Ps o [ilo

Ps 1 o 1 1 fi jy

2. Is the system in a safe state? Why or why nor?
In order to check this, we should mm the safety alzorithm = Let*s create the work vector
and finish marix:

Work vector Finish ‘Needs (1,1,0) is less than work, so let's go
matrix ahead and update work and fimish:
2 False Work vector Finish
1 False Deane.
7 False 3 Py | True
False 1 BP, | False
2 P, | False
PB: | False

‘Weeds (0.1.0) is less than work, we
can update work and finish:

Finish matrix Work vector | Finish matix
J Po Tre 7 PB True
1 Pi | False 1 BR, | False
2 Py Tre 3 P, True
PB False Py True

‘We now need to go back to Pi. Need: (3.3.2) is not less than work, so we camnot continue.
Thus, the system is not in a safe state.

7

CPU

1/O controller

[—} device driver initiates VO Pm

initiates /O

CPU executing checks for
interrupts between instructions
1

¥

CPU receiving interrupt, 4

transfers control to
interrupt handler

input ready, output
complete, or error
generates interrupt signal

[5
interrupt handler

processes data,
returns from interrupt

|e
CPU resumes

— processing of
interrupted task
--- page 5 ---
• Requires compaction to reduce external fragmentation.
• More flexible, suitable for varying process sizes.
Q4   B   Briefly explain the following network commands with examples:   [10]
CO-2;   a) ping command
b) traceroute command
SO-2; BL-2
c) ifconfig command
d) netstat command
e) nslookup command
• ping: Tests network connectivity to a host by sending ICMP echo requests
(e.g., ping google.com).
> ping google.com
• traceroute: Displays the route packets take to reach a host, showing each
hop (e.g., traceroute google.com).
> traceroute google.com
• ifconfig: Displays or configures network interfaces in Unix/Linux systems
(e.g., ifconfig eth0).
>
• netstat: Shows network connections, routing tables, and interface statistics
(e.g., netstat -a).
> netstat -tuln
Explanation: Shows all active TCP/UDP listening ports along with numeric
addresses.
• nslookup: Queries DNS to obtain domain name or IP address mapping (e.g.,
nslookup google.com).
> nslookup google.com
Q5   A   Consider the set of 6 processes whose arrival time and burst time are given [10]
CO-3;   below-
SO-2; BL-   Process   Arrival   Burst   Priority
Time   Time
4
𝑃0   0   10   5
𝑃1   1   6   4
𝑃2   3   2   2
𝑃3   5   4   0
If   the CPU   scheduling
policy is Priority scheduling (Preemptive), calculate the average waiting time
and average turnaround time. Also draw Gantt chart. Consider the lower
number as highest priority.
Process   Arrival   Burst   Priority   Completion   Turn   Waiting
Time   Time   time   around   time
time
𝑃0   0   10   5   22   22   12
𝑃1   1   6   4   13   12   6
𝑃2   3   2   2   5   2   0
𝑃3   5   4   0   9   4   0
Total   40   18
Average values   10   4.5
********** 5 **********
--- page 6 ---
GANTT CHART
P0   P1   P2   P3   P1   P0
0 ---------1   1----------3   3----------5   5----------9   9--------13   13-------22
• Turnaround Time (TAT) = CT - Arrival Time.
• Waiting Time (WT) = TAT - Burst Time.
• Compute average Waiting Time and average Turnaround Time.
• Detailed Gantt chart and calculations to be manually worked out.
• Preemptive nature improves response time but increases overhead.
Q5   B   Apply your understanding of Single-Level Directory, Two-Level Directory, Tree- [10]
CO-2;   Structured Directory, and Acyclic-Graph Directory to explain their advantages
and disadvantages in terms of file searching, naming, and grouping. Provide
SO-2; BL-3
suitable examples for each structure.
• Single-Level Directory:
- One directory for all files.
- Easy to implement but naming conflicts.
- No grouping capability.
• Two-Level Directory:
- Separate directory for each user.
- Prevents name conflicts.
- Limited grouping capability.
• Tree-Structured Directory:
- Hierarchical structure like tree.
- Allows better organization & grouping.
- Complex but scalable.
• Acyclic-Graph Directory:
- Allows shared files via links.
- Eliminates redundancy.
- Needs careful management to avoid cycles.
• Example: Linux file system uses Tree-Structured.
Q6   A   Analyze the classic Reader-Writer problem in operating systems. Examine the [10]
CO-4;   synchronization challenges involved and propose a suitable solution to handle
concurrent access by multiple readers and writers. Explain how your solution
SO-2; BL-4
addresses potential issues like starvation or deadlock.
• Multiple readers can read simultaneously, writers require exclusive access.
• Challenge: Synchronizing readers and writers without conflict.
• Solution: Semaphores or mutex locks used.
• Readers acquire read lock; writers acquire both read and write locks.
• Prevents writer starvation by priority to writers.
• Can also apply writer preference or reader preference solutions.
• Deadlock avoided by proper lock release order.
• Example: Database access by readers (queries) and writers (updates).
• Critical to ensure data consistency.
• Well-designed synchronization ensures fairness and efficiency.
Q6   B   Compare and contrast the design principles of Linux and Windows OS.   [10]
********** 6 **********
--- page 7 ---
CO-3;   • Linux is open-source; Windows is proprietary.
SO-2; BL-3   • Linux has monolithic kernel; Windows uses hybrid kernel.
• Linux follows POSIX standard; Windows uses Windows API.
• Linux offers better customization; Windows is user-friendly.
• Security: Linux has strong user permissions; Windows has built-in firewall &
Defender.
• File System: Linux supports ext4, Windows supports NTFS.
• Linux preferred for servers; Windows dominates desktop market.
• Command-line usage prominent in Linux; GUI dominates Windows.
• Software availability is broader for Windows.
• Linux encourages community-driven development; Windows relies on
Microsoft.
Q7   A   Explain the Process Control Block (PCB) and apply your understanding to   [10]
CO-4;   describe how the operating system uses PCB to manage processes during
context switching. Provide a suitable example to support your explanation.
SO-2; BL-
3
Q7   B   Explain the basic file protection mechanisms used in modern operating   [10]
CO-4;   systems. Describe the purpose of access control lists (ACLs), user/group
permissions, and file encryption.
SO-2; BL-3   Modern operating systems implement various file protection mechanisms to ensure the security and
integrity of files. The primary purpose is to prevent unauthorized access, modification, or deletion of
files. The most commonly used mechanisms are:
1. Access Control Lists (ACLs)
•   Definition: ACLs are lists associated with each file or directory that specify which users or
system processes have permission to access or manipulate the file.
•   Components: Each entry in an ACL includes a user or group and their allowed permissions
(read, write, execute, etc.).
•   Purpose:
o   Allows fine-grained control over file access.
o   Enables assigning different permissions to different users or groups.
o   Provides flexibility beyond simple user/group permission schemes.
•   Example: In Linux, extended ACLs can allow a specific user to have write access to a file, while
others have only read access.
2. User/Group Permissions
•   Definition: This is a traditional UNIX-based permission model where each file is assigned to a
specific user (owner) and group.
•   Permissions Categories:
o   User (Owner): The person who created the file.
o   Group: A set of users who share the same permissions.
********** 7 **********

[Text in pictures on this page, read by OCR]
Process Control Block (PCB)

Information associated with each process(also called
task control block)

= Process state — running, waiting, etc.

= Program counter — location of instruction to next process state
execute process number

= CPU registers — contents of all process -centric program counter
registers

= CPU scheduling information - priorities, scheduling registers

queue pointers
= Memory-management information — memory
allocated to the process

memory limits
list of open files

= Accounting information — CPU used, clock time eee
elapsed since start, time limits

= I/O status information — I/O devices allocated to
process, list of open files

Sy
XS

Operating System Concepts — 10 Edition 314 ‘Silberschatz, Galvin and Gagne ©2018
--- page 8 ---
o   Others: All other users.
•   Permission Types:
o   Read (r): Permission to view the contents of the file.
o   Write (w): Permission to modify or delete the file.
o   Execute (x): Permission to run the file as a program.
•   Purpose:
o   Provides a basic level of file access control.
o   Ensures only authorized users can access or modify files.
•   Example: File permissions like rwxr-xr-- define specific rights for owner, group, and others.
3. File Encryption
•   Definition: Encryption converts the file content into an unreadable format using a
cryptographic algorithm, making it accessible only to those who have the decryption key.
•   Types:
o   Symmetric Encryption: Same key is used for both encryption and decryption.
o   Asymmetric Encryption: Public key encrypts the file, private key decrypts it.
•   Purpose:
o   Protects the confidentiality of file data.
o   Prevents unauthorized access even if file permissions are bypassed or the file is
stolen.
o   Commonly used for sensitive files like personal data, financial records, etc.
•   Example: Operating systems like Windows offer features such as BitLocker for file/system
encryption.
********** 8 **********
````

## 2024-25 · Re-Exam · Sem 6 · Answer key · paper e99adb25d467

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/Integrated_IT_7037/Fundamentals of Operating Systems/ANS_Fundamentals of Operating Systems(701IT0C008)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2025
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Sem 6 Re-exam(Exam Year: 2024-2025)
Subject: Fundamentals of Operating Systems
Date: 09 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions
6. In all ___5_ questions to be attempted.
7. Answer to each new question to be started on a fresh page.
8. Figures in brackets on the right hand side indicate full marks.
9. Assume Suitable data if necessary.
Q1 Answer briefly:   [20]
Q1   Explain the basic components of a Computer System Structure. Describe the role   [5]
of each component and how they interact to perform system operations.
A.   • Hardware: Includes CPU, memory, storage, and I/O devices; performs
actual data processing.
• Operating System (OS): Manages hardware resources, processes,
memory, and provides user interface.
• System Programs: Utilities and tools like compilers and file managers that
support system functioning.
•   Application Programs: Software used by users to perform specific tasks
(e.g., browsers, word processors).
•   Users: End-users who interact with the system through application
programs.
•   Interaction: Users → Application Programs → OS → Hardware →
Output shown to users.
Q1   Define Interprocess Communication. Explain any two IPC mechanisms.   [5]
Interprocess Communication (IPC)
B.
•   Definition: IPC is the process by which multiple processes communicate
and exchange data with each other in an operating system.
•   Purpose: Enables coordination, data sharing, and synchronization
between processes.
Two IPC Mechanisms:
1. Shared Memory:
o A memory region is shared between processes.
o Processes read/write data directly to this shared space.
o   Faster communication but requires synchronization (e.g.,
semaphores).
2. Message Passing:
********** 1 **********
--- page 2 ---
o Processes exchange messages via the OS (using send/receive
operations).
o No shared memory; suitable for distributed systems.
o Ensures better process isolation and security.
Q1   Apply your knowledge of process synchronization to explain the Critical Section   [5]
Problem. Describe its significance and provide an example where solving the
C.
critical section problem is essential.
Critical Section Problem
•   Definition: The Critical Section Problem arises when multiple processes
access and modify shared resources (like variables or files) concurrently.
It is crucial to ensure that only one process accesses the critical section
(shared resource) at a time to avoid data inconsistency.
Significance:
•   Prevents race conditions (unpredictable results due to concurrent
access).
•   Ensures data integrity and consistency.
•   Maintains process synchronization and avoids deadlocks or starvation.
Conditions for Solution (3 Conditions):
1. Mutual Exclusion: Only one process can be in the critical section at a
time.
2. Progress: If no process is in the critical section, selection of next process
cannot be postponed indefinitely.
3. Bounded Waiting: A process must get a chance to enter the critical
section after a limited number of turns.
Example:
Banking System:
• Two processes updating the same customer’s account balance.
•   Without synchronization, simultaneous updates may result in incorrect
balance.
•   Solving the critical section problem ensures correct, consistent account
updates.
********** 2 **********
--- page 3 ---
Q1 Given memory partitions of 100K, 500K, 200K, 300K, and 600K (in order), how   [5]
would each of the First-fit, Best-fit, and Worst-fit algorithms place processes of
D.
212K, 417K, 112K, and 426K (in order)? Which algorithm makes the most
efficient use of memory?
First-Fit:
• 212K is put in 500K partition.
• 417K is put in 600K partition.
• 112K is put in 288K partition (new partition 288K = 500K - 212K).
• 426K must wait.
▪   Best-Fit:
• 212K is put in 300K partition.
• 417K is put in 500K partition.
• 112K is put in 200K partition.
• 426K is put in 600K partition.
▪   Worst-Fit:
• 212K is put in 600K partition.
• 417K is put in 500K partition.
• 112K is put in 388K partition.
• 426K must wait.
▪   In this example, Best-Fit turns out to be the best.
Q2   Consider the set of 5 processes whose arrival time and burst time are given   [10]
below
A
Process   Arrival time   Burst time
P1   3   1
P2   1   4
P3   4   2
P4   0   6
P5   2   3
If the CPU scheduling policy is SJF non-preemptive and is SJF preemptive,
calculate the average waiting time and average turnaround time for both cases.
Also conclude which one is having minimum average waiting time among two
algorithms.
SJF
| P4 | P1 | P3 | P5 | P2 |
0   6   7   9   12 16
SRTF:
Proc AT   BT   CT   TAT (TAT WT = TAT - BT)
ess   = CT - AT)
P1   3   1   4   4 - 3 = 1   1 - 1 = 0
P2   1   4   12   12 - 1 = 11   11 - 4 = 7
P3   4   2   8   8 - 4 = 4   4 - 2 = 2
P4   0   6   16   16 - 0 = 16   16 - 6 = 10
P5   2   3   6   6 - 2 = 4   4 - 3 = 1
********** 3 **********
--- page 4 ---
Final Averages:
• Average Waiting Time (AWT) = (0 + 7 + 2 + 10 + 1) / 5 = 4.0
• Average Turnaround Time (ATAT) = (1 + 11 + 4 + 16 + 4) / 5 = 7.2
Scheduling Algorithm   Avg Waiting   Avg Turnaround
Time   Time
SJF Non-Preemptive   4.8   8.0
SJF Preemptive   4.0   7.2
(corrected)
Q2 Apply your understanding of virtual memory to explain the role of a Page Table in [10]
address translation. Illustrate with an example how a logical address is converted
B   to a physical address using a Page Table.
Q3   Apply your knowledge of synchronization to describe the Dining Philosophers [10]
A   Problem. Suggest a method to prevent deadlock and illustrate how it solves the
problem.
•   Philosophers spend their lives alternating thinking and eating
•   Don’t interact with their neighbors, occasionally try to pick up 2 chopsticks
(one at a time) to eat from bowl
o Need both to eat, then release both when done
•   In the case of 5 philosophers
o Shared data
▪ Bowl of rice (data set)
▪ Semaphore chopstick [5] initialized to 1
• The structure of Philosopher i:
do {
wait (chopstick[i] );
wait (chopStick[ (i + 1) % 5] );
// eat
signal (chopstick[i] );
signal (chopstick[ (i + 1) % 5] );
// think
} while (TRUE);
********** 4 **********
--- page 5 ---
Q3   Explain the concept of Direct Memory Access (DMA) in operating systems. How [10]
B   does DMA differ from traditional I/O techniques like programmed I/O and
interrupt-driven I/O?
Q4   Consider a system with four resource types (A,B,C, D) and five processes. The [10]
A   maximum demand matrix and allocation matrix are given as follows:
Allocation   Max. Demand   Available
Process   A B C D A B C D   A   B C   D
P0   0   1   1   0   0   2   1   0   1   5   2   0
P1   1   2   3   1   1   6   5   2
P2   1   3   6   5   2   3   6   6
P3   0   6   3   2   0   6   5   2
P4   0   0   1   4   0   6   5   6
a) Apply Banker’s algorithm considering resources A, B, C, and D to
determine whether the system is in safe state or not.
b) If the system is in safe state, provide a safe sequence. If not, explain why
the system is not safe.
********** 5 **********

[Text in pictures on this page, read by OCR]
Data
count

Data lines Data
register

Address
Address lines register
Request to DMA
Acknowledge from DMA Control
Interrupt logic
logic
Read

Write

a 4 —————
1. Create the need matrix (max-allocation)

Need(i) = Max(i) — Allocated(i) Need Matrix = Max Matrix
(0) (0.2.1.0) - (0.1.1.0) = (0,1.0,0) — Allocation Matrix

1) = (0.4.2.1) AlB|c [Dp

5) = (1.00.1) Po |O}i1/0|0

(0652)- - (0,6,3.2) = (0,0.2,0) Pilol/4/2 {1

(i=4) (0.6.5.6) - (0.0.1.4) = (0.6.4.2) P2 1 0 0 1

Ex. Process Pl has max of (1,6,5,2) and allocated by (1.2.3.1) P; | o | 0 }| 2] 0

Need(p1) = max(p1)- allocated(p1) = (1,6,5,2) — (1,2.3,1) =(0,4,2,1) Ps 0 6|4 2
--- page 6 ---
Safety Sequence
P0,P3,P4,P1,P2
Q4   Briefly explain the following process management commands and system calls [10]
B   with examples:
a) ps command - >ps aux
>ps aux | grep firefox
b) top command --- >top # Displays running processes dynamically, press q to quit.
c) kill command -- > 1. pidof firefox (PID will be learnt) then kill -9 PID will
forcrefull kill the PID
d) strace commands - Traces system calls and signals of a process. Useful for
debugging or monitoring. > strace ls
e) fork() system call
#include <stdio.h>
#include <unistd.h>
********** 6 **********

[Text in pictures on this page, read by OCR]
needo (0,1,0,0) <= work(1,!
Finish matrix PO will release the allocated Work vector

PO will be 7 resources(0,1,1,0) 1 [6 [3 [0
executed because eu one Work = Work
need(P0) <= Work | P False (1,5,2,0)+Allocated(P0)
PO will be True Pr False (0,1,1,0) = 1,6,3,0
P3 False
Ps False

Need) (0,4,2,1) <= work(1,6,3,0) Condition Is False _P1 will Not be executed
Need? (1,0,0,1) <= work(1,6,3,0) Condition Is False_P2 will Not be executed
Need3 (0,0,2,0) <= work(1,6,3,0) P3 will be executed

P3 will be Finish matrix P3 will release the allocated Work vector
executed because , resources (0,6,3,2) 1 ]12]6 [2
need(P3) <= Work [Post | Trme | t= Work
P3 will be True Pl False (1,6,3,0)+Allocated(P3)
P2 False ( 0,6,3,2) = 1.12.62
P3-2 True
Ps False
Needy (0,6,4,.2) <= work(1,12,6,2) P4 will be executed
P4 will be Finish matrix P4 will release the allocated Work vector
executed because D resources (0,0,1.4) 1 | 12 | 7 [6
need(P4) <= Work | P02 | True Work = Work
P4 will be True Pl False )
P? False
P3-2 True
Py-3 True
4.2.1) <= work(1,12,7,6)_P1 will be executed
Finish matrix P1 will release the allocated Work vector
Pl will be , j resources (1.2.3.1) 2 [14] 10 [7
executed because | a | oie Work = Work
need(P1)<=Work [Pi | True (1,12,7,6) + Allocated(P1)
P1 will be True P) False (1,2,3,1) = 2,14,10,7
|P3-2 | True

Pa-3 True

Need) (1,0,0,1) <= work(2,14,10,7) P2 will be executed

P2 will be Finish matrix P2 will release the allocated Work vector

nt | Po-1 | True resources 88>) 3 [17 J 16 [12
P2willbe True   |PI4 | True (2,14,10,7) + Allocated(P1)

|P2-5 | True (1,3,6,5) = 3,17,16,12

P3-2 True

Py-3 True

The system is in a safe state and the processes will be executed in the following order:
PO.P3.P4.P1.P2
--- page 7 ---
int main() {
printf("PID: %d\n", getpid());
return 0;
}
A) Consider the set of 6 processes whose arrival time and burst time are given [10]
below-If the CPU scheduling policy is Round Robin with time quantum = 2,
Q5
calculate the average waiting time and average turnaround time.
A   Process ID   Arrival time   Burst time/CPU execution time
P1   0   4
P2   1   5
P3   2   1
P4   3   1
P5   4   5
P6   6   2
Gantt chart
| P1 | P2 | P3 | P4 | P1 | P5 | P6 | P2 | P5 | P2 | P5 |
0 2 4 5 6   8 10 12 14 16 17 18
Q5   B) Explain how I/O buffering is used to improve the efficiency of process   [10]
B   execution. Apply your knowledge to describe a real-life situation where buffering
minimizes process waiting time during data transfer.
********** 7 **********

[Text in pictures on this page, read by OCR]
Process Arrival Burst Completion TAT = CT- AT WT = TAT - BT

PI 0 4 8 8-0=8 8-4=4
P2 1 5 7 17-1=16 16-5=11
P3 2 1 5 5-223 3-122
P4 3 1 6 6-3=3 3-122
PS 4 5 18 18-4=14 14-5=9

P6 6 2 12 12-6=6 6-2=4
--- page 8 ---
Q6   In designing a concurrent solution to the reader-writer problem, evaluate   [10]
A   different synchronization strategies such as read-write locks, semaphores,
ensuring fair access to shared resources by readers and writers in a multi-
threaded environment.
Data set
Semaphore rw_mutex initialized to 1
Semaphore mutex initialized to 1
Integer read_count initialized to 0
The structure of a writer process
do {
wait(rw_mutex);
...
/* writing is performed */
...
signal(rw_mutex);
} while (true);
The structure of a reader process
do {
wait(mutex);
read_count++;
if (read_count == 1)
wait(rw_mutex);
signal(mutex);
...
/* reading is performed */
...
wait(mutex);
read count--;
if (read_count == 0)
signal(rw_mutex);
signal(mutex);
} while (true);
********** 8 **********

[Text in pictures on this page, read by OCR]
\/O Buffering

* Why buffering is required?
— When a user process wants to read blocks of data from a disk, process
waits for the transfer

— It waits either by

* Busy waiting

* Process suspension on an interrupt
— The problems with this approach

* Program waits for slow I/O

* Virtual locations should stay in the main memory during the
course of block transfer

* Risk of single-process deadlock
* Process is blocked during transfer and may not be swapped out

The above inefficiencies can be resolved if input transfers in advance of
requests are being made and output transfers are performed some time after
the request is made. This technique is known asbuffering.
--- page 9 ---
Q6 Compare the performance of Windows and Linux operating systems based on   [10]
B   their performance issues. Highlight key factors affecting their efficiency.
Q7   Explain multithreaded models and differentiate between user-level and kernel-   [10]
A   level threads.
********** 9 **********

[Text in pictures on this page, read by OCR]
Factor Windows Linux

Boot Time Slower boot time due to heavier GUI and Faster boot time due to lightweight
services architecture

Resource Usage Consumes more system resources (heavy GUI Efficient use of CPU and RAM

(RAM/CPU) and background services) (lightweight)

System Updates Frequent and automatic updates may slow Updates are user-controlled and
system efficient

Process Management GUI-based, user-friendly but may lag under CLI and GUI tools available; highly
heavy load efficient under load

File System Uses NTFS; slower on large files or multiple Uses ext4, XFS; faster file operations

Performance file access and indexing

Customization & Limited customization; performance tuning Highly customizable for

Optimization restricted performance optimization

Multitasking Efficiency Good, but performance may degrade with Excellent multitasking; better load
multiple processes handling

Security Impact on Heavy antivirus software can affect speed Built-in security tools with minimal

Performance performance impact

Driver & Hardware Better support for proprietary hardware and _Limited support for some

Support drivers proprietary drivers

System Crash Recovery More prone to freeze/crash under load More stable under high workloads

Multithreading is the ability of a CPU or a single process to manage multiple threads (smaller units of a

process) for concurrent execution. This improves performance and resource utilization.

There are three primary multithreaded models:

Model Description

1. Many-to- Many user threads are mapped to a single kernel thread. Thread management is done by the

One user-level thread library. Efficient but lacks concurrency on multi-core systems.

2. One-to- Each user thread maps to a kernel thread. Offers better concurrency but can be resource-intensive
One due to more kernel involvement.

3.Many-to- Many user threads are mapped to a smaller or equal number of kernel threads. Allows multiple

Many threads to run in parallel while maintaining efficiency.
--- page 10 ---
Q7   Analyze various file access methods with in operating systems. (Unit 6)   [10]
B
•   Sequential access is best for reading files from start to end.
•   Direct access allows quick, random reads/writes.
• Indexed access is ideal when both search speed and ordered access are
important.
********** 10 **********

[Text in pictures on this page, read by OCR]
Difference Between User-Level and Kernel-Level Threads

Aspect User-Level Threads Kernel-Level Threads
Management Managed by user-space libraries Managed by the operating system kernel

Visibility to OS Invisible to the OS; the kernel is unaware Fully visible and controlled by the OS

Context Fast (no need for kernel mode switch) Slower (involves kernel mode switch)

Switching

Concurrency Limited; one thread at atime per process _—_True parallelism is possible on multi-core
systems

Blocking If one thread blocks, all threads in the One blocking thread doesn't affect others

process block
Portability More portable across platforms Less portable due to kernel dependencies

Examples Java green threads, early pthreads Modern pthreads, Windows threads, Linux

kernel threads

Access

Method Access Pattern Speed Use Case Efficiency
Sequential Record-by-record Slow for large Log files, media High for full scan
jumps playback
Direct Any location Fast Databases, disks High for random
directly access

Indexed Index + data block — Medium Large databases Efficient for searches
````
