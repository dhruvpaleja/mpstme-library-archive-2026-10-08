# Introduction to Operating Systems: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper b97da29d074c

- Departments: Computer Engineering
- Programmes: DIPLOMA IN COMPUTER ENGINEERING - 7073
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN COMPUTER ENGINEERING - 7073/Introduction to Operating Systems/ANS_Introduction to Operating Systems(701CO0C022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (18 pages), mean OCR confidence 39.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Introduction to Operating Systems
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. •   Question No. 1 is compulsory.
3. •   Out of remaining questions, attempt any 4 questions.
4. •   In all 5 questions to be attempted.
5. •   All questions carry equal marks.
6. •   Answer to each new question to be started on a fresh page.
7. •   Figures in brackets on the right hand side indicate full marks.
8. •   Assume Suitable data if necessary.
9.
Q1
Answer briefly:   [20]
a.   “A system is in an unsafe state but not deadlocked.” Explain this with
clear example.
Ans:
1. Introduction (1 Mark)
A deadlock occurs when processes are permanently blocked.
An unsafe state means the system may lead to deadlock in the future,
but is not currently deadlocked.
CO3   ;
2. Explanation (2 Marks)
SO- ; BL-
4   ● In an unsafe state, no guaranteed safe sequence exists.
● However, processes are still executing and not all are blocked.
● Deadlock has not yet occurred, but the system is at risk.
Key Point:
All deadlocks are unsafe states, but not all unsafe states are
deadlocks.
3. Example (1.5 Marks)
Consider:
********** 1 **********
--- page 2 ---
● Total resources = 2
● Processes: P1 and P2
● Available = 0
● Both processes need 1 more resource
If both request simultaneously → system cannot satisfy → deadlock
possible
But currently, they are still running → unsafe but not deadlocked
4. Conclusion (0.5 Mark)
An unsafe state indicates risk of deadlock, but the system is still
operational until all processes are blocked.
b.   Explain the role of medium term scheduler.
Answer:
Introduction (1 Mark)
The medium-term scheduler is responsible for temporarily removing
processes from main memory and later reintroducing them for
execution.
CO2   ;   This process is called swapping.
SO- ; BL-
2   Role / Functions (3 Marks)
onclusion (1 Mark)
The medium-term scheduler plays a key role in memory management
and process control, ensuring efficient use of system resources through
swapping.
c.   Discuss types of IPC models.
Answer:
CO3   ;
Answer: Types of IPC Models
SO- ; BL-
1. Introduction (1 Mark)
2
Interprocess Communication (IPC) allows processes to communicate
and share data with each other for coordination and synchronization.
2. Types of IPC Models (3 Marks)
********** 2 **********
--- page 3 ---
1. Shared Memory Model
● Processes share a common memory space
● Communication is done by reading/writing shared data
Features:
● Fast communication
● Requires synchronization (e.g., semaphores)
2. Message Passing Model
● Processes communicate by sending and receiving messages
● No shared memory required
Features:
● Easier to implement
● Suitable for distributed systems
3. Conclusion (1 Mark)
Both IPC models are important:
● Shared memory is faster
● Message passing is simpler and safer
CO4   ; d.   “A real-time embedded system must ensure predictable memory
SO- ; BL-   allocation with minimal overhead.” Assess whether static partitioning
5   or dynamic partitioning is more suitable for this system. Justify your
choice by evaluating trade-offs in fragmentation, flexibility, and
predictability.
Ans:
1. Introduction (1 Mark)
In memory management, static partitioning uses fixed-size memory
blocks, while dynamic partitioning allocates memory based on process
requirements at runtime.
2. Evaluation (3 Marks)
Predictability
● Static Partitioning ✔ → Fixed allocation, predictable
behavior (important for real-time systems)
● Dynamic → Allocation varies, less predictable
Overhead
********** 3 **********
--- page 4 ---
● Static ✔ → Minimal overhead (no complex allocation
algorithms)
● Dynamic → Higher overhead due to allocation/deallocation
Fragmentation & Flexibility
● Static → Internal fragmentation, less flexible
● Dynamic ✔ → Better utilization, more flexible but
causes external fragmentation
3. Conclusion (1 Mark)
Static partitioning is more suitable for real-time embedded systems
because it provides predictable performance and low overhead,
which are critical, even though it may cause some memory wastage.
Q2   a.   20
CO2   ;   Draw a neat labeled diagram of a Process Control Block (PCB).
SO- ; BL-   Explain each component of the PCB and discuss how it is used during
3   process execution.
Ans:
CO4   ; b.
SO- ; BL-
1. Introduction (2 Marks)
3
A Process Control Block (PCB) is a data structure used by the
operating system to store all information about a process.
It is essential for process management and context switching.
2. Neat Labeled Diagram (2 Marks)
Components of PCB (4 Marks)
Role During Process Execution (1.5 Marks)
Conclusion (0.5 Mark)
PCB acts as the backbone of process management, enabling efficient
multitasking and resource handling.
Explain internal fragmentation and external fragmentation using
suitable examples.
Why is external fragmentation a serious problem in memory allocation?
Answer:
********** 4 **********
--- page 5 ---
1. Introduction (2 Marks)
Fragmentation occurs when memory is not utilized efficiently during
allocation and deallocation of processes.
It leads to wastage of memory and reduced system performance.
2. Internal Fragmentation (3 Marks)
Definition:
Occurs when allocated memory is larger than required, leaving
unused space inside the allocated block.
Example:
● Fixed partition: 4 MB
● Process size: 3 MB
● Unused: 1 MB (cannot be used by others)
Key Point:
Wastage occurs inside allocated memory.
3. External Fragmentation (3 Marks)
Definition:
Occurs when free memory is available but not contiguous, so it cannot
satisfy a process request.
Example:
● Free spaces: 2 MB + 1 MB + 1 MB
● Process needs: 3 MB
● Total free = 4 MB but not contiguous → cannot allocate
Key Point:
Wastage occurs outside allocated memory.
4. Why External Fragmentation is Serious (1.5 Marks)
● Prevents allocation despite sufficient total memory
● Leads to inefficient memory utilization
● Requires compaction (costly and time-consuming)
● Affects system performance
5. Conclusion (0.5 Mark)
Internal fragmentation wastes space within blocks, while external
fragmentation disrupts allocation.
External fragmentation is more serious as it prevents effective use of
available memory.
********** 5 **********
--- page 6 ---
a.   Define turnaround time, waiting time, and response time.
Explain their importance in evaluating scheduling algorithms.
Answer:
b.   1. Introduction (2 Marks)
To evaluate the performance of CPU scheduling algorithms, certain
metrics are used.
The most important among them are Turnaround Time, Waiting
Time, and Response Time.
2. Definitions (4 Marks)
Q3   Turnaround Time (TAT)
CO2   ;
● Total time taken from process submission to completion
SO- ; BL-   ● Formula:
3   TAT = Completion Time – Arrival Time
CO3   ;   Waiting Time (WT)
20
SO- ; BL-   ● Total time a process spends waiting in the ready queue
2   ● Formula:
WT = Turnaround Time – Burst Time
Response Time (RT)
● Time from submission of process to its first response (first
CPU allocation)
● Formula:
RT = First Start Time – Arrival Time
3. Importance in Scheduling (3 Marks)
● Turnaround Time
Measures overall system efficiency
→ Lower TAT = faster completion
● Waiting Time
Indicates delay experienced by processes
→ Lower WT = better performance
● Response Time
Important for interactive systems
→ Faster response improves user experience
4. Conclusion (1 Mark)
********** 6 **********
--- page 7 ---
These metrics help in comparing scheduling algorithms and selecting
the best one based on system requirements like efficiency, fairness,
and responsiveness.
Explain the Producer–Consumer problem.
Write a solution using semaphores and explain how synchronization is
achieved.
Answer:
1. Introduction (2 Marks)
The Producer–Consumer problem is a classical synchronization
problem where:
● Producer generates data and places it in a buffer
● Consumer consumes data from the buffer
Both share a common buffer, requiring proper synchronization to
avoid errors.
2. Problem Description (2 Marks)
● Buffer has limited size
● Producer should not add data when buffer is full
● Consumer should not remove data when buffer is empty
● Requires mutual exclusion while accessing buffer
3. Semaphore Solution (4 Marks)
Let:
● mutex = 1 → for mutual exclusion
● empty = n → number of empty slots
● full = 0 → number of filled slots
Producer Code:
wait(empty)
wait(mutex)
********** 7 **********
--- page 8 ---
add item to buffer
signal(mutex)
signal(full)
Consumer Code:
wait(full)
wait(mutex)
remove item from buffer
signal(mutex)
signal(empty)
4. How Synchronization is Achieved (1.5 Marks)
● mutex ensures only one process accesses buffer (mutual
exclusion)
● empty prevents overflow (producer waits if buffer full)
● full prevents underflow (consumer waits if buffer empty)
5. Conclusion (0.5 Mark)
Semaphores ensure safe and coordinated execution of producer and
consumer, avoiding race conditions and ensuring correct data sharing.
********** 8 **********
--- page 9 ---
a.   Consider the following processes in the system:
Questions:
Apply Round Robin scheduling with:
Q4
CO2   ;   ● Time Quantum = 2
SO- ; BL-   ● Time Quantum = 4
3
Draw Gantt charts for both cases.
Calculate:
● Average Waiting Time
● Average Turnaround Time
Critically analyze the effect of time quantum on performance.
Answer:
20
Round Robin Scheduling
Given Data (1 Mark)
b.
Case 1: Time Quantum = 2
2. Gantt Chart (2 Marks)
Average TAT = (26+13+27+21)/4 = 21.75
CO1   ;   Average WT = (16+8+19+15)/4 = 14.5
SO- ; BL-
5
Case 2: Time Quantum = 4
Gantt Chart (2 Marks)
Average TAT = 24
Average WT = 16.75
Analysis (2 Marks)
● Smaller Time Quantum (2):
Better response time
More context switching (overhead)
Lower waiting time
********** 9 **********
--- page 10 ---
● Larger Time Quantum (4):
Fewer context switches
Higher waiting time
Less responsiveness
Conclusion (1 Mark)
Smaller time quantum improves responsiveness but increases overhead.
Larger quantum reduces overhead but behaves like FCFS.
Optimal quantum balances both.
Evaluate how OS services and system calls support process execution
and management.
Answer:
1. Introduction (2 Marks)
An Operating System (OS) provides various services to manage
processes and system resources.
System calls act as an interface between user programs and the OS,
enabling process execution and control.
2. OS Services for Process Management (3 Marks)
● Process Creation & Termination
OS creates and deletes processes as required
● CPU Scheduling
Allocates CPU to processes efficiently
● Memory Management
Allocates and deallocates memory to processes
● I/O Operations
Handles input/output requests of processes
● Protection & Security
Ensures controlled access to resources
3. System Calls and Their Role (3 Marks)
System calls allow user programs to request OS services:
4. Evaluation (1.5 Marks)
● OS services provide the functionality needed for process
execution
● System calls act as the interface to access these services
********** 10 **********
--- page 11 ---
● Together, they ensure efficient, secure, and coordinated
execution of processes
5. Conclusion (0.5 Mark)
OS services and system calls are essential for process management,
enabling smooth execution, resource allocation, and system stability.
Q5
a.   A system has 3 frames. Reference string:
CO4   ;
4, 2, 3, 2, 1, 4, 2, 3, 1, 2
SO- ; BL-
3
Questions::
1. Apply following algorithm:
○ OPTIMAL PAGE REPLACEMENT
○ FIFO
2. Show all steps clearly.
3. Compare:
○ Number of page faults
Answer:
CO5   ;   1. Given Data (1 Mark)
SO- ; BL- b.   20
● Frames = 3
4   ● Reference String:
4, 2, 3, 2, 1, 4, 2, 3, 1, 2
2. FIFO Algorithm (4 Marks)
Frame Table:
Page Faults:
FIFO = 7 faults
3. OPTIMAL Algorithm (4 Marks)
Frame Table:
Page Faults:
********** 11 **********
--- page 12 ---
OPT = 6 faults
4. Comparison (1 Mark)
FIFO → 7 faults
OPT → 6 faults
OPT gives minimum page faults
5. Conclusion (1 Mark)
Optimal algorithm performs best because it replaces the page that will
not be used for the longest time in future, though it is not practical to
implement.
What is a directory?
Explain different types of directory structures (single-level, two-level,
tree structure).
Answer:
1. Introduction (2 Marks)
A directory is a data structure used by the operating system to organize
and store information about files.
It maintains file names, locations, and attributes, helping users
efficiently manage files.
2. Functions of Directory (1 Mark)
● File organization
● Naming and grouping of files
● Easy access and retrieval
● File protection and sharing
3. Types of Directory Structures (5 Marks)
1. Single-Level Directory
● All files are stored in one directory
● No subdirectories
●
Advantages:
********** 12 **********
--- page 13 ---
● Simple to implement
Disadvantages:
● File name conflicts
● Poor organization
2. Two-Level Directory
● Separate directory for each user
● Master directory + user directories
Advantages:
● Avoids name conflicts
● Better organization
Disadvantages:
● Limited flexibility
● Difficult file sharing
3. Tree Structure Directory
● Hierarchical structure (root → subdirectories → files)
● Most commonly used
Advantages:
● Efficient organization
● Supports grouping and easy search
● Flexible and scalable
Disadvantages:
● More complex to manage
4. Conclusion (2 Marks)
Directory structures improve file organization and management.
Among them, the tree structure is most widely used due to its
flexibility, scalability, and efficiency.
Q6   a.
CO5   ;   A disk has 0–199 tracks. Initial head position is 100.
SO- ; BL-   Request queue:
2   20
55, 58, 60, 70, 18, 90, 150, 160
Questions:
********** 13 **********
--- page 14 ---
1. Apply:
○ SCAN (initial direction towards higher tracks)
○ C-SCAN
2. Show the sequence of head movement.
3. Calculate total seek distance for each algorithm.
Answer:
CO3   ;
1. Given Data (1 Mark)
SO- ; BL-
b.   ● Disk tracks: 0–199
4
●   Initial head position: 100
● Direction: towards higher tracks
● Request queue:
55, 58, 60, 70, 18, 90, 150, 160
Sorted queue:
18, 55, 58, 60, 70, 90, 150, 160
2. SCAN Algorithm (Elevator) (4 Marks)
Movement (towards higher first):
100 → 150 → 160 → 199 → 90 → 70 → 60 → 58 → 55 → 18
Step-wise Head Movement:
Total Seek = 50+10+39+109+20+10+2+3+37 = 280
3. C-SCAN Algorithm (4 Marks)
Movement (only one direction):
100 → 150 → 160 → 199 → 0 → 18 → 55 → 58 → 60 → 70 → 90
Total Seek = 50+10+39+199+18+37+3+2+10+20 = 388
4. Comparison (1 Mark)
● SCAN = 280
● C-SCAN = 388
SCAN gives lower seek time
5. Conclusion (1 Mark)
● SCAN is more efficient in terms of total head movement
********** 14 **********
--- page 15 ---
● C-SCAN provides better fairness (uniform waiting time)
Explain the implications of unsafe states and how Banker’s Algorithm
helps prevent deadlocks.
Answer:
1. Introduction (2 Marks)
A system state in resource allocation can be safe or unsafe.
A safe state guarantees that all processes can complete execution,
while an unsafe state may lead to deadlock.
2. Unsafe State (Concept & Implications) (3 Marks)
● Definition:
An unsafe state is one where no safe sequence exists.
● Implications:
○ May lead to deadlock in future
○ System cannot guarantee completion of all processes
○ Resource allocation becomes risky
○ Reduced system reliability
Key Point:
Unsafe state ≠ Deadlock, but it can result in deadlock.
3. Banker’s Algorithm (Deadlock Avoidance) (3 Marks)
● A deadlock avoidance algorithm
● Grants resource requests only if the system remains in a safe
state
Working Steps:
1. Check if request ≤ available resources
2. Pretend allocation (temporary allocation)
3. Check for safe sequence
4. Grant request only if system remains safe
4. How Banker’s Algorithm Prevents Deadlock (1.5 Marks)
● Avoids entering unsafe states
● Ensures at least one safe execution sequence exists
● Allocates resources cautiously
5. Conclusion (0.5 Mark)
********** 15 **********
--- page 16 ---
Unsafe states pose a risk of deadlock, and Banker’s Algorithm helps
prevent it by maintaining the system in a safe state through careful
resource allocation.
Q7 CO3 ;   a.   Explain the Readers–Writers problem.
SO- ; BL-   Discuss a solution using semaphores and explain how it ensures
4   synchronization between multiple readers and writers.
Answer:
1. Introduction (2 Marks)
CO5   ; b.
SO- ; BL-   The Readers–Writers problem is a classical synchronization problem
3   where:
● Readers only read shared data
● Writers modify shared data
The goal is to allow multiple readers simultaneously but ensure
exclusive access for writers.
2. Problem Description (2 Marks)
● Multiple readers can access data at the same time
● Writers require exclusive access
● No reader should read while a writer is writing
● Requires synchronization to avoid inconsistency   20
3. Semaphore Solution (4 Marks)
Let:
● mutex = 1 → protects read count
● wrt = 1 → controls writer access
● read_count = 0
Reader Code:
Writer Code:
4. How Synchronization is Achieved (1.5 Marks)
● Multiple readers can access simultaneously
● First reader blocks writers (wrt)
● Writers get exclusive access
● Mutex ensures safe update of read_count
5. Conclusion (0.5 Mark)
********** 16 **********
--- page 17 ---
Semaphores ensure proper coordination between readers and
writers, preventing conflicts and maintaining data consistency.
Explain the structure of a disk (tracks, sectors, cylinders).
How does disk organization affect performance?
Ans:
1. Introduction (2 Marks)
A disk is a secondary storage device used to store data permanently.
Data on a disk is organized into tracks, sectors, and cylinders, which
helps in efficient storage and retrieval.
2. Structure of Disk diagram(5 Marks)
Circular paths on the disk surface
Data is stored along these concentric circles
Each track is divided into smaller parts called sectors
Smallest unit of data storage
● set of corresponding tracks across all disk platters
● Same track number on each platter forms a cylinder
3. Impact on Performance (2 Marks)
● Seek Time
Time taken to move head across tracks (major factor)
● Rotational Latency
Time taken for sector to rotate under head
● Data Locality
Storing data in same cylinder reduces movement → faster
access
● Disk Scheduling
Algorithms (SCAN, SSTF) use this structure to optimize
performance
4. Conclusion (1 Mark)
Disk organization plays a crucial role in performance.
Efficient arrangement of data reduces access time and improves overall
system efficiency.
********** 17 **********
--- page 18 ---
FR ICR 7] QA HH
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper ede06847b4e8

- Departments: Computer Science
- Programmes: DIPLOMA IN COMPUTER SCIENCE AND ENGINEE
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN COMPUTER SCIENCE AND ENGINEE_04f07abf/Introduction to Operating Systems/ANS_Introduction to Operating Systems(701CO0C022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (18 pages), mean OCR confidence 39.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Introduction to Operating Systems
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. •   Question No. 1 is compulsory.
3. •   Out of remaining questions, attempt any 4 questions.
4. •   In all 5 questions to be attempted.
5. •   All questions carry equal marks.
6. •   Answer to each new question to be started on a fresh page.
7. •   Figures in brackets on the right hand side indicate full marks.
8. •   Assume Suitable data if necessary.
9.
Q1
Answer briefly:   [20]
a.   “A system is in an unsafe state but not deadlocked.” Explain this with
clear example.
Ans:
1. Introduction (1 Mark)
A deadlock occurs when processes are permanently blocked.
An unsafe state means the system may lead to deadlock in the future,
but is not currently deadlocked.
CO3   ;
2. Explanation (2 Marks)
SO- ; BL-
4   ● In an unsafe state, no guaranteed safe sequence exists.
● However, processes are still executing and not all are blocked.
● Deadlock has not yet occurred, but the system is at risk.
Key Point:
All deadlocks are unsafe states, but not all unsafe states are
deadlocks.
3. Example (1.5 Marks)
Consider:
********** 1 **********
--- page 2 ---
● Total resources = 2
● Processes: P1 and P2
● Available = 0
● Both processes need 1 more resource
If both request simultaneously → system cannot satisfy → deadlock
possible
But currently, they are still running → unsafe but not deadlocked
4. Conclusion (0.5 Mark)
An unsafe state indicates risk of deadlock, but the system is still
operational until all processes are blocked.
b.   Explain the role of medium term scheduler.
Answer:
Introduction (1 Mark)
The medium-term scheduler is responsible for temporarily removing
processes from main memory and later reintroducing them for
execution.
CO2   ;   This process is called swapping.
SO- ; BL-
2   Role / Functions (3 Marks)
onclusion (1 Mark)
The medium-term scheduler plays a key role in memory management
and process control, ensuring efficient use of system resources through
swapping.
c.   Discuss types of IPC models.
Answer:
CO3   ;
Answer: Types of IPC Models
SO- ; BL-
1. Introduction (1 Mark)
2
Interprocess Communication (IPC) allows processes to communicate
and share data with each other for coordination and synchronization.
2. Types of IPC Models (3 Marks)
********** 2 **********
--- page 3 ---
1. Shared Memory Model
● Processes share a common memory space
● Communication is done by reading/writing shared data
Features:
● Fast communication
● Requires synchronization (e.g., semaphores)
2. Message Passing Model
● Processes communicate by sending and receiving messages
● No shared memory required
Features:
● Easier to implement
● Suitable for distributed systems
3. Conclusion (1 Mark)
Both IPC models are important:
● Shared memory is faster
● Message passing is simpler and safer
CO4   ; d.   “A real-time embedded system must ensure predictable memory
SO- ; BL-   allocation with minimal overhead.” Assess whether static partitioning
5   or dynamic partitioning is more suitable for this system. Justify your
choice by evaluating trade-offs in fragmentation, flexibility, and
predictability.
Ans:
1. Introduction (1 Mark)
In memory management, static partitioning uses fixed-size memory
blocks, while dynamic partitioning allocates memory based on process
requirements at runtime.
2. Evaluation (3 Marks)
Predictability
● Static Partitioning ✔ → Fixed allocation, predictable
behavior (important for real-time systems)
● Dynamic → Allocation varies, less predictable
Overhead
********** 3 **********
--- page 4 ---
● Static ✔ → Minimal overhead (no complex allocation
algorithms)
● Dynamic → Higher overhead due to allocation/deallocation
Fragmentation & Flexibility
● Static → Internal fragmentation, less flexible
● Dynamic ✔ → Better utilization, more flexible but
causes external fragmentation
3. Conclusion (1 Mark)
Static partitioning is more suitable for real-time embedded systems
because it provides predictable performance and low overhead,
which are critical, even though it may cause some memory wastage.
Q2   a.   20
CO2   ;   Draw a neat labeled diagram of a Process Control Block (PCB).
SO- ; BL-   Explain each component of the PCB and discuss how it is used during
3   process execution.
Ans:
CO4   ; b.
SO- ; BL-
1. Introduction (2 Marks)
3
A Process Control Block (PCB) is a data structure used by the
operating system to store all information about a process.
It is essential for process management and context switching.
2. Neat Labeled Diagram (2 Marks)
Components of PCB (4 Marks)
Role During Process Execution (1.5 Marks)
Conclusion (0.5 Mark)
PCB acts as the backbone of process management, enabling efficient
multitasking and resource handling.
Explain internal fragmentation and external fragmentation using
suitable examples.
Why is external fragmentation a serious problem in memory allocation?
Answer:
********** 4 **********
--- page 5 ---
1. Introduction (2 Marks)
Fragmentation occurs when memory is not utilized efficiently during
allocation and deallocation of processes.
It leads to wastage of memory and reduced system performance.
2. Internal Fragmentation (3 Marks)
Definition:
Occurs when allocated memory is larger than required, leaving
unused space inside the allocated block.
Example:
● Fixed partition: 4 MB
● Process size: 3 MB
● Unused: 1 MB (cannot be used by others)
Key Point:
Wastage occurs inside allocated memory.
3. External Fragmentation (3 Marks)
Definition:
Occurs when free memory is available but not contiguous, so it cannot
satisfy a process request.
Example:
● Free spaces: 2 MB + 1 MB + 1 MB
● Process needs: 3 MB
● Total free = 4 MB but not contiguous → cannot allocate
Key Point:
Wastage occurs outside allocated memory.
4. Why External Fragmentation is Serious (1.5 Marks)
● Prevents allocation despite sufficient total memory
● Leads to inefficient memory utilization
● Requires compaction (costly and time-consuming)
● Affects system performance
5. Conclusion (0.5 Mark)
Internal fragmentation wastes space within blocks, while external
fragmentation disrupts allocation.
External fragmentation is more serious as it prevents effective use of
available memory.
********** 5 **********
--- page 6 ---
a.   Define turnaround time, waiting time, and response time.
Explain their importance in evaluating scheduling algorithms.
Answer:
b.   1. Introduction (2 Marks)
To evaluate the performance of CPU scheduling algorithms, certain
metrics are used.
The most important among them are Turnaround Time, Waiting
Time, and Response Time.
2. Definitions (4 Marks)
Q3   Turnaround Time (TAT)
CO2   ;
● Total time taken from process submission to completion
SO- ; BL-   ● Formula:
3   TAT = Completion Time – Arrival Time
CO3   ;   Waiting Time (WT)
20
SO- ; BL-   ● Total time a process spends waiting in the ready queue
2   ● Formula:
WT = Turnaround Time – Burst Time
Response Time (RT)
● Time from submission of process to its first response (first
CPU allocation)
● Formula:
RT = First Start Time – Arrival Time
3. Importance in Scheduling (3 Marks)
● Turnaround Time
Measures overall system efficiency
→ Lower TAT = faster completion
● Waiting Time
Indicates delay experienced by processes
→ Lower WT = better performance
● Response Time
Important for interactive systems
→ Faster response improves user experience
4. Conclusion (1 Mark)
********** 6 **********
--- page 7 ---
These metrics help in comparing scheduling algorithms and selecting
the best one based on system requirements like efficiency, fairness,
and responsiveness.
Explain the Producer–Consumer problem.
Write a solution using semaphores and explain how synchronization is
achieved.
Answer:
1. Introduction (2 Marks)
The Producer–Consumer problem is a classical synchronization
problem where:
● Producer generates data and places it in a buffer
● Consumer consumes data from the buffer
Both share a common buffer, requiring proper synchronization to
avoid errors.
2. Problem Description (2 Marks)
● Buffer has limited size
● Producer should not add data when buffer is full
● Consumer should not remove data when buffer is empty
● Requires mutual exclusion while accessing buffer
3. Semaphore Solution (4 Marks)
Let:
● mutex = 1 → for mutual exclusion
● empty = n → number of empty slots
● full = 0 → number of filled slots
Producer Code:
wait(empty)
wait(mutex)
********** 7 **********
--- page 8 ---
add item to buffer
signal(mutex)
signal(full)
Consumer Code:
wait(full)
wait(mutex)
remove item from buffer
signal(mutex)
signal(empty)
4. How Synchronization is Achieved (1.5 Marks)
● mutex ensures only one process accesses buffer (mutual
exclusion)
● empty prevents overflow (producer waits if buffer full)
● full prevents underflow (consumer waits if buffer empty)
5. Conclusion (0.5 Mark)
Semaphores ensure safe and coordinated execution of producer and
consumer, avoiding race conditions and ensuring correct data sharing.
********** 8 **********
--- page 9 ---
a.   Consider the following processes in the system:
Questions:
Apply Round Robin scheduling with:
Q4
CO2   ;   ● Time Quantum = 2
SO- ; BL-   ● Time Quantum = 4
3
Draw Gantt charts for both cases.
Calculate:
● Average Waiting Time
● Average Turnaround Time
Critically analyze the effect of time quantum on performance.
Answer:
20
Round Robin Scheduling
Given Data (1 Mark)
b.
Case 1: Time Quantum = 2
2. Gantt Chart (2 Marks)
Average TAT = (26+13+27+21)/4 = 21.75
CO1   ;   Average WT = (16+8+19+15)/4 = 14.5
SO- ; BL-
5
Case 2: Time Quantum = 4
Gantt Chart (2 Marks)
Average TAT = 24
Average WT = 16.75
Analysis (2 Marks)
● Smaller Time Quantum (2):
Better response time
More context switching (overhead)
Lower waiting time
********** 9 **********
--- page 10 ---
● Larger Time Quantum (4):
Fewer context switches
Higher waiting time
Less responsiveness
Conclusion (1 Mark)
Smaller time quantum improves responsiveness but increases overhead.
Larger quantum reduces overhead but behaves like FCFS.
Optimal quantum balances both.
Evaluate how OS services and system calls support process execution
and management.
Answer:
1. Introduction (2 Marks)
An Operating System (OS) provides various services to manage
processes and system resources.
System calls act as an interface between user programs and the OS,
enabling process execution and control.
2. OS Services for Process Management (3 Marks)
● Process Creation & Termination
OS creates and deletes processes as required
● CPU Scheduling
Allocates CPU to processes efficiently
● Memory Management
Allocates and deallocates memory to processes
● I/O Operations
Handles input/output requests of processes
● Protection & Security
Ensures controlled access to resources
3. System Calls and Their Role (3 Marks)
System calls allow user programs to request OS services:
4. Evaluation (1.5 Marks)
● OS services provide the functionality needed for process
execution
● System calls act as the interface to access these services
********** 10 **********
--- page 11 ---
● Together, they ensure efficient, secure, and coordinated
execution of processes
5. Conclusion (0.5 Mark)
OS services and system calls are essential for process management,
enabling smooth execution, resource allocation, and system stability.
Q5
a.   A system has 3 frames. Reference string:
CO4   ;
4, 2, 3, 2, 1, 4, 2, 3, 1, 2
SO- ; BL-
3
Questions::
1. Apply following algorithm:
○ OPTIMAL PAGE REPLACEMENT
○ FIFO
2. Show all steps clearly.
3. Compare:
○ Number of page faults
Answer:
CO5   ;   1. Given Data (1 Mark)
SO- ; BL- b.   20
● Frames = 3
4   ● Reference String:
4, 2, 3, 2, 1, 4, 2, 3, 1, 2
2. FIFO Algorithm (4 Marks)
Frame Table:
Page Faults:
FIFO = 7 faults
3. OPTIMAL Algorithm (4 Marks)
Frame Table:
Page Faults:
********** 11 **********
--- page 12 ---
OPT = 6 faults
4. Comparison (1 Mark)
FIFO → 7 faults
OPT → 6 faults
OPT gives minimum page faults
5. Conclusion (1 Mark)
Optimal algorithm performs best because it replaces the page that will
not be used for the longest time in future, though it is not practical to
implement.
What is a directory?
Explain different types of directory structures (single-level, two-level,
tree structure).
Answer:
1. Introduction (2 Marks)
A directory is a data structure used by the operating system to organize
and store information about files.
It maintains file names, locations, and attributes, helping users
efficiently manage files.
2. Functions of Directory (1 Mark)
● File organization
● Naming and grouping of files
● Easy access and retrieval
● File protection and sharing
3. Types of Directory Structures (5 Marks)
1. Single-Level Directory
● All files are stored in one directory
● No subdirectories
●
Advantages:
********** 12 **********
--- page 13 ---
● Simple to implement
Disadvantages:
● File name conflicts
● Poor organization
2. Two-Level Directory
● Separate directory for each user
● Master directory + user directories
Advantages:
● Avoids name conflicts
● Better organization
Disadvantages:
● Limited flexibility
● Difficult file sharing
3. Tree Structure Directory
● Hierarchical structure (root → subdirectories → files)
● Most commonly used
Advantages:
● Efficient organization
● Supports grouping and easy search
● Flexible and scalable
Disadvantages:
● More complex to manage
4. Conclusion (2 Marks)
Directory structures improve file organization and management.
Among them, the tree structure is most widely used due to its
flexibility, scalability, and efficiency.
Q6   a.
CO5   ;   A disk has 0–199 tracks. Initial head position is 100.
SO- ; BL-   Request queue:
2   20
55, 58, 60, 70, 18, 90, 150, 160
Questions:
********** 13 **********
--- page 14 ---
1. Apply:
○ SCAN (initial direction towards higher tracks)
○ C-SCAN
2. Show the sequence of head movement.
3. Calculate total seek distance for each algorithm.
Answer:
CO3   ;
1. Given Data (1 Mark)
SO- ; BL-
b.   ● Disk tracks: 0–199
4
●   Initial head position: 100
● Direction: towards higher tracks
● Request queue:
55, 58, 60, 70, 18, 90, 150, 160
Sorted queue:
18, 55, 58, 60, 70, 90, 150, 160
2. SCAN Algorithm (Elevator) (4 Marks)
Movement (towards higher first):
100 → 150 → 160 → 199 → 90 → 70 → 60 → 58 → 55 → 18
Step-wise Head Movement:
Total Seek = 50+10+39+109+20+10+2+3+37 = 280
3. C-SCAN Algorithm (4 Marks)
Movement (only one direction):
100 → 150 → 160 → 199 → 0 → 18 → 55 → 58 → 60 → 70 → 90
Total Seek = 50+10+39+199+18+37+3+2+10+20 = 388
4. Comparison (1 Mark)
● SCAN = 280
● C-SCAN = 388
SCAN gives lower seek time
5. Conclusion (1 Mark)
● SCAN is more efficient in terms of total head movement
********** 14 **********
--- page 15 ---
● C-SCAN provides better fairness (uniform waiting time)
Explain the implications of unsafe states and how Banker’s Algorithm
helps prevent deadlocks.
Answer:
1. Introduction (2 Marks)
A system state in resource allocation can be safe or unsafe.
A safe state guarantees that all processes can complete execution,
while an unsafe state may lead to deadlock.
2. Unsafe State (Concept & Implications) (3 Marks)
● Definition:
An unsafe state is one where no safe sequence exists.
● Implications:
○ May lead to deadlock in future
○ System cannot guarantee completion of all processes
○ Resource allocation becomes risky
○ Reduced system reliability
Key Point:
Unsafe state ≠ Deadlock, but it can result in deadlock.
3. Banker’s Algorithm (Deadlock Avoidance) (3 Marks)
● A deadlock avoidance algorithm
● Grants resource requests only if the system remains in a safe
state
Working Steps:
1. Check if request ≤ available resources
2. Pretend allocation (temporary allocation)
3. Check for safe sequence
4. Grant request only if system remains safe
4. How Banker’s Algorithm Prevents Deadlock (1.5 Marks)
● Avoids entering unsafe states
● Ensures at least one safe execution sequence exists
● Allocates resources cautiously
5. Conclusion (0.5 Mark)
********** 15 **********
--- page 16 ---
Unsafe states pose a risk of deadlock, and Banker’s Algorithm helps
prevent it by maintaining the system in a safe state through careful
resource allocation.
Q7 CO3 ;   a.   Explain the Readers–Writers problem.
SO- ; BL-   Discuss a solution using semaphores and explain how it ensures
4   synchronization between multiple readers and writers.
Answer:
1. Introduction (2 Marks)
CO5   ; b.
SO- ; BL-   The Readers–Writers problem is a classical synchronization problem
3   where:
● Readers only read shared data
● Writers modify shared data
The goal is to allow multiple readers simultaneously but ensure
exclusive access for writers.
2. Problem Description (2 Marks)
● Multiple readers can access data at the same time
● Writers require exclusive access
● No reader should read while a writer is writing
● Requires synchronization to avoid inconsistency   20
3. Semaphore Solution (4 Marks)
Let:
● mutex = 1 → protects read count
● wrt = 1 → controls writer access
● read_count = 0
Reader Code:
Writer Code:
4. How Synchronization is Achieved (1.5 Marks)
● Multiple readers can access simultaneously
● First reader blocks writers (wrt)
● Writers get exclusive access
● Mutex ensures safe update of read_count
5. Conclusion (0.5 Mark)
********** 16 **********
--- page 17 ---
Semaphores ensure proper coordination between readers and
writers, preventing conflicts and maintaining data consistency.
Explain the structure of a disk (tracks, sectors, cylinders).
How does disk organization affect performance?
Ans:
1. Introduction (2 Marks)
A disk is a secondary storage device used to store data permanently.
Data on a disk is organized into tracks, sectors, and cylinders, which
helps in efficient storage and retrieval.
2. Structure of Disk diagram(5 Marks)
Circular paths on the disk surface
Data is stored along these concentric circles
Each track is divided into smaller parts called sectors
Smallest unit of data storage
● set of corresponding tracks across all disk platters
● Same track number on each platter forms a cylinder
3. Impact on Performance (2 Marks)
● Seek Time
Time taken to move head across tracks (major factor)
● Rotational Latency
Time taken for sector to rotate under head
● Data Locality
Storing data in same cylinder reduces movement → faster
access
● Disk Scheduling
Algorithms (SCAN, SSTF) use this structure to optimize
performance
4. Conclusion (1 Mark)
Disk organization plays a crucial role in performance.
Efficient arrangement of data reduces access time and improves overall
system efficiency.
********** 17 **********
--- page 18 ---
FR ICR 7] QA HH
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 3ad113a0e5da

- Departments: Information Technology
- Programmes: DIPLOMA IN INFORMATION TECHNOLOGY - 7075
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN INFORMATION TECHNOLOGY - 7075/Introduction to Operating Systems/ANS_Introduction to Operating Systems(701CO0C022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (18 pages), mean OCR confidence 39.1

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Introduction to Operating Systems
Date: 13 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. •   Question No. 1 is compulsory.
3. •   Out of remaining questions, attempt any 4 questions.
4. •   In all 5 questions to be attempted.
5. •   All questions carry equal marks.
6. •   Answer to each new question to be started on a fresh page.
7. •   Figures in brackets on the right hand side indicate full marks.
8. •   Assume Suitable data if necessary.
9.
Q1
Answer briefly:   [20]
a.   “A system is in an unsafe state but not deadlocked.” Explain this with
clear example.
Ans:
1. Introduction (1 Mark)
A deadlock occurs when processes are permanently blocked.
An unsafe state means the system may lead to deadlock in the future,
but is not currently deadlocked.
CO3   ;
2. Explanation (2 Marks)
SO- ; BL-
4   ● In an unsafe state, no guaranteed safe sequence exists.
● However, processes are still executing and not all are blocked.
● Deadlock has not yet occurred, but the system is at risk.
Key Point:
All deadlocks are unsafe states, but not all unsafe states are
deadlocks.
3. Example (1.5 Marks)
Consider:
********** 1 **********
--- page 2 ---
● Total resources = 2
● Processes: P1 and P2
● Available = 0
● Both processes need 1 more resource
If both request simultaneously → system cannot satisfy → deadlock
possible
But currently, they are still running → unsafe but not deadlocked
4. Conclusion (0.5 Mark)
An unsafe state indicates risk of deadlock, but the system is still
operational until all processes are blocked.
b.   Explain the role of medium term scheduler.
Answer:
Introduction (1 Mark)
The medium-term scheduler is responsible for temporarily removing
processes from main memory and later reintroducing them for
execution.
CO2   ;   This process is called swapping.
SO- ; BL-
2   Role / Functions (3 Marks)
onclusion (1 Mark)
The medium-term scheduler plays a key role in memory management
and process control, ensuring efficient use of system resources through
swapping.
c.   Discuss types of IPC models.
Answer:
CO3   ;
Answer: Types of IPC Models
SO- ; BL-
1. Introduction (1 Mark)
2
Interprocess Communication (IPC) allows processes to communicate
and share data with each other for coordination and synchronization.
2. Types of IPC Models (3 Marks)
********** 2 **********
--- page 3 ---
1. Shared Memory Model
● Processes share a common memory space
● Communication is done by reading/writing shared data
Features:
● Fast communication
● Requires synchronization (e.g., semaphores)
2. Message Passing Model
● Processes communicate by sending and receiving messages
● No shared memory required
Features:
● Easier to implement
● Suitable for distributed systems
3. Conclusion (1 Mark)
Both IPC models are important:
● Shared memory is faster
● Message passing is simpler and safer
CO4   ; d.   “A real-time embedded system must ensure predictable memory
SO- ; BL-   allocation with minimal overhead.” Assess whether static partitioning
5   or dynamic partitioning is more suitable for this system. Justify your
choice by evaluating trade-offs in fragmentation, flexibility, and
predictability.
Ans:
1. Introduction (1 Mark)
In memory management, static partitioning uses fixed-size memory
blocks, while dynamic partitioning allocates memory based on process
requirements at runtime.
2. Evaluation (3 Marks)
Predictability
● Static Partitioning ✔ → Fixed allocation, predictable
behavior (important for real-time systems)
● Dynamic → Allocation varies, less predictable
Overhead
********** 3 **********
--- page 4 ---
● Static ✔ → Minimal overhead (no complex allocation
algorithms)
● Dynamic → Higher overhead due to allocation/deallocation
Fragmentation & Flexibility
● Static → Internal fragmentation, less flexible
● Dynamic ✔ → Better utilization, more flexible but
causes external fragmentation
3. Conclusion (1 Mark)
Static partitioning is more suitable for real-time embedded systems
because it provides predictable performance and low overhead,
which are critical, even though it may cause some memory wastage.
Q2   a.   20
CO2   ;   Draw a neat labeled diagram of a Process Control Block (PCB).
SO- ; BL-   Explain each component of the PCB and discuss how it is used during
3   process execution.
Ans:
CO4   ; b.
SO- ; BL-
1. Introduction (2 Marks)
3
A Process Control Block (PCB) is a data structure used by the
operating system to store all information about a process.
It is essential for process management and context switching.
2. Neat Labeled Diagram (2 Marks)
Components of PCB (4 Marks)
Role During Process Execution (1.5 Marks)
Conclusion (0.5 Mark)
PCB acts as the backbone of process management, enabling efficient
multitasking and resource handling.
Explain internal fragmentation and external fragmentation using
suitable examples.
Why is external fragmentation a serious problem in memory allocation?
Answer:
********** 4 **********
--- page 5 ---
1. Introduction (2 Marks)
Fragmentation occurs when memory is not utilized efficiently during
allocation and deallocation of processes.
It leads to wastage of memory and reduced system performance.
2. Internal Fragmentation (3 Marks)
Definition:
Occurs when allocated memory is larger than required, leaving
unused space inside the allocated block.
Example:
● Fixed partition: 4 MB
● Process size: 3 MB
● Unused: 1 MB (cannot be used by others)
Key Point:
Wastage occurs inside allocated memory.
3. External Fragmentation (3 Marks)
Definition:
Occurs when free memory is available but not contiguous, so it cannot
satisfy a process request.
Example:
● Free spaces: 2 MB + 1 MB + 1 MB
● Process needs: 3 MB
● Total free = 4 MB but not contiguous → cannot allocate
Key Point:
Wastage occurs outside allocated memory.
4. Why External Fragmentation is Serious (1.5 Marks)
● Prevents allocation despite sufficient total memory
● Leads to inefficient memory utilization
● Requires compaction (costly and time-consuming)
● Affects system performance
5. Conclusion (0.5 Mark)
Internal fragmentation wastes space within blocks, while external
fragmentation disrupts allocation.
External fragmentation is more serious as it prevents effective use of
available memory.
********** 5 **********
--- page 6 ---
a.   Define turnaround time, waiting time, and response time.
Explain their importance in evaluating scheduling algorithms.
Answer:
b.   1. Introduction (2 Marks)
To evaluate the performance of CPU scheduling algorithms, certain
metrics are used.
The most important among them are Turnaround Time, Waiting
Time, and Response Time.
2. Definitions (4 Marks)
Q3   Turnaround Time (TAT)
CO2   ;
● Total time taken from process submission to completion
SO- ; BL-   ● Formula:
3   TAT = Completion Time – Arrival Time
CO3   ;   Waiting Time (WT)
20
SO- ; BL-   ● Total time a process spends waiting in the ready queue
2   ● Formula:
WT = Turnaround Time – Burst Time
Response Time (RT)
● Time from submission of process to its first response (first
CPU allocation)
● Formula:
RT = First Start Time – Arrival Time
3. Importance in Scheduling (3 Marks)
● Turnaround Time
Measures overall system efficiency
→ Lower TAT = faster completion
● Waiting Time
Indicates delay experienced by processes
→ Lower WT = better performance
● Response Time
Important for interactive systems
→ Faster response improves user experience
4. Conclusion (1 Mark)
********** 6 **********
--- page 7 ---
These metrics help in comparing scheduling algorithms and selecting
the best one based on system requirements like efficiency, fairness,
and responsiveness.
Explain the Producer–Consumer problem.
Write a solution using semaphores and explain how synchronization is
achieved.
Answer:
1. Introduction (2 Marks)
The Producer–Consumer problem is a classical synchronization
problem where:
● Producer generates data and places it in a buffer
● Consumer consumes data from the buffer
Both share a common buffer, requiring proper synchronization to
avoid errors.
2. Problem Description (2 Marks)
● Buffer has limited size
● Producer should not add data when buffer is full
● Consumer should not remove data when buffer is empty
● Requires mutual exclusion while accessing buffer
3. Semaphore Solution (4 Marks)
Let:
● mutex = 1 → for mutual exclusion
● empty = n → number of empty slots
● full = 0 → number of filled slots
Producer Code:
wait(empty)
wait(mutex)
********** 7 **********
--- page 8 ---
add item to buffer
signal(mutex)
signal(full)
Consumer Code:
wait(full)
wait(mutex)
remove item from buffer
signal(mutex)
signal(empty)
4. How Synchronization is Achieved (1.5 Marks)
● mutex ensures only one process accesses buffer (mutual
exclusion)
● empty prevents overflow (producer waits if buffer full)
● full prevents underflow (consumer waits if buffer empty)
5. Conclusion (0.5 Mark)
Semaphores ensure safe and coordinated execution of producer and
consumer, avoiding race conditions and ensuring correct data sharing.
********** 8 **********
--- page 9 ---
a.   Consider the following processes in the system:
Questions:
Apply Round Robin scheduling with:
Q4
CO2   ;   ● Time Quantum = 2
SO- ; BL-   ● Time Quantum = 4
3
Draw Gantt charts for both cases.
Calculate:
● Average Waiting Time
● Average Turnaround Time
Critically analyze the effect of time quantum on performance.
Answer:
20
Round Robin Scheduling
Given Data (1 Mark)
b.
Case 1: Time Quantum = 2
2. Gantt Chart (2 Marks)
Average TAT = (26+13+27+21)/4 = 21.75
CO1   ;   Average WT = (16+8+19+15)/4 = 14.5
SO- ; BL-
5
Case 2: Time Quantum = 4
Gantt Chart (2 Marks)
Average TAT = 24
Average WT = 16.75
Analysis (2 Marks)
● Smaller Time Quantum (2):
Better response time
More context switching (overhead)
Lower waiting time
********** 9 **********
--- page 10 ---
● Larger Time Quantum (4):
Fewer context switches
Higher waiting time
Less responsiveness
Conclusion (1 Mark)
Smaller time quantum improves responsiveness but increases overhead.
Larger quantum reduces overhead but behaves like FCFS.
Optimal quantum balances both.
Evaluate how OS services and system calls support process execution
and management.
Answer:
1. Introduction (2 Marks)
An Operating System (OS) provides various services to manage
processes and system resources.
System calls act as an interface between user programs and the OS,
enabling process execution and control.
2. OS Services for Process Management (3 Marks)
● Process Creation & Termination
OS creates and deletes processes as required
● CPU Scheduling
Allocates CPU to processes efficiently
● Memory Management
Allocates and deallocates memory to processes
● I/O Operations
Handles input/output requests of processes
● Protection & Security
Ensures controlled access to resources
3. System Calls and Their Role (3 Marks)
System calls allow user programs to request OS services:
4. Evaluation (1.5 Marks)
● OS services provide the functionality needed for process
execution
● System calls act as the interface to access these services
********** 10 **********
--- page 11 ---
● Together, they ensure efficient, secure, and coordinated
execution of processes
5. Conclusion (0.5 Mark)
OS services and system calls are essential for process management,
enabling smooth execution, resource allocation, and system stability.
Q5
a.   A system has 3 frames. Reference string:
CO4   ;
4, 2, 3, 2, 1, 4, 2, 3, 1, 2
SO- ; BL-
3
Questions::
1. Apply following algorithm:
○ OPTIMAL PAGE REPLACEMENT
○ FIFO
2. Show all steps clearly.
3. Compare:
○ Number of page faults
Answer:
CO5   ;   1. Given Data (1 Mark)
SO- ; BL- b.   20
● Frames = 3
4   ● Reference String:
4, 2, 3, 2, 1, 4, 2, 3, 1, 2
2. FIFO Algorithm (4 Marks)
Frame Table:
Page Faults:
FIFO = 7 faults
3. OPTIMAL Algorithm (4 Marks)
Frame Table:
Page Faults:
********** 11 **********
--- page 12 ---
OPT = 6 faults
4. Comparison (1 Mark)
FIFO → 7 faults
OPT → 6 faults
OPT gives minimum page faults
5. Conclusion (1 Mark)
Optimal algorithm performs best because it replaces the page that will
not be used for the longest time in future, though it is not practical to
implement.
What is a directory?
Explain different types of directory structures (single-level, two-level,
tree structure).
Answer:
1. Introduction (2 Marks)
A directory is a data structure used by the operating system to organize
and store information about files.
It maintains file names, locations, and attributes, helping users
efficiently manage files.
2. Functions of Directory (1 Mark)
● File organization
● Naming and grouping of files
● Easy access and retrieval
● File protection and sharing
3. Types of Directory Structures (5 Marks)
1. Single-Level Directory
● All files are stored in one directory
● No subdirectories
●
Advantages:
********** 12 **********
--- page 13 ---
● Simple to implement
Disadvantages:
● File name conflicts
● Poor organization
2. Two-Level Directory
● Separate directory for each user
● Master directory + user directories
Advantages:
● Avoids name conflicts
● Better organization
Disadvantages:
● Limited flexibility
● Difficult file sharing
3. Tree Structure Directory
● Hierarchical structure (root → subdirectories → files)
● Most commonly used
Advantages:
● Efficient organization
● Supports grouping and easy search
● Flexible and scalable
Disadvantages:
● More complex to manage
4. Conclusion (2 Marks)
Directory structures improve file organization and management.
Among them, the tree structure is most widely used due to its
flexibility, scalability, and efficiency.
Q6   a.
CO5   ;   A disk has 0–199 tracks. Initial head position is 100.
SO- ; BL-   Request queue:
2   20
55, 58, 60, 70, 18, 90, 150, 160
Questions:
********** 13 **********
--- page 14 ---
1. Apply:
○ SCAN (initial direction towards higher tracks)
○ C-SCAN
2. Show the sequence of head movement.
3. Calculate total seek distance for each algorithm.
Answer:
CO3   ;
1. Given Data (1 Mark)
SO- ; BL-
b.   ● Disk tracks: 0–199
4
●   Initial head position: 100
● Direction: towards higher tracks
● Request queue:
55, 58, 60, 70, 18, 90, 150, 160
Sorted queue:
18, 55, 58, 60, 70, 90, 150, 160
2. SCAN Algorithm (Elevator) (4 Marks)
Movement (towards higher first):
100 → 150 → 160 → 199 → 90 → 70 → 60 → 58 → 55 → 18
Step-wise Head Movement:
Total Seek = 50+10+39+109+20+10+2+3+37 = 280
3. C-SCAN Algorithm (4 Marks)
Movement (only one direction):
100 → 150 → 160 → 199 → 0 → 18 → 55 → 58 → 60 → 70 → 90
Total Seek = 50+10+39+199+18+37+3+2+10+20 = 388
4. Comparison (1 Mark)
● SCAN = 280
● C-SCAN = 388
SCAN gives lower seek time
5. Conclusion (1 Mark)
● SCAN is more efficient in terms of total head movement
********** 14 **********
--- page 15 ---
● C-SCAN provides better fairness (uniform waiting time)
Explain the implications of unsafe states and how Banker’s Algorithm
helps prevent deadlocks.
Answer:
1. Introduction (2 Marks)
A system state in resource allocation can be safe or unsafe.
A safe state guarantees that all processes can complete execution,
while an unsafe state may lead to deadlock.
2. Unsafe State (Concept & Implications) (3 Marks)
● Definition:
An unsafe state is one where no safe sequence exists.
● Implications:
○ May lead to deadlock in future
○ System cannot guarantee completion of all processes
○ Resource allocation becomes risky
○ Reduced system reliability
Key Point:
Unsafe state ≠ Deadlock, but it can result in deadlock.
3. Banker’s Algorithm (Deadlock Avoidance) (3 Marks)
● A deadlock avoidance algorithm
● Grants resource requests only if the system remains in a safe
state
Working Steps:
1. Check if request ≤ available resources
2. Pretend allocation (temporary allocation)
3. Check for safe sequence
4. Grant request only if system remains safe
4. How Banker’s Algorithm Prevents Deadlock (1.5 Marks)
● Avoids entering unsafe states
● Ensures at least one safe execution sequence exists
● Allocates resources cautiously
5. Conclusion (0.5 Mark)
********** 15 **********
--- page 16 ---
Unsafe states pose a risk of deadlock, and Banker’s Algorithm helps
prevent it by maintaining the system in a safe state through careful
resource allocation.
Q7 CO3 ;   a.   Explain the Readers–Writers problem.
SO- ; BL-   Discuss a solution using semaphores and explain how it ensures
4   synchronization between multiple readers and writers.
Answer:
1. Introduction (2 Marks)
CO5   ; b.
SO- ; BL-   The Readers–Writers problem is a classical synchronization problem
3   where:
● Readers only read shared data
● Writers modify shared data
The goal is to allow multiple readers simultaneously but ensure
exclusive access for writers.
2. Problem Description (2 Marks)
● Multiple readers can access data at the same time
● Writers require exclusive access
● No reader should read while a writer is writing
● Requires synchronization to avoid inconsistency   20
3. Semaphore Solution (4 Marks)
Let:
● mutex = 1 → protects read count
● wrt = 1 → controls writer access
● read_count = 0
Reader Code:
Writer Code:
4. How Synchronization is Achieved (1.5 Marks)
● Multiple readers can access simultaneously
● First reader blocks writers (wrt)
● Writers get exclusive access
● Mutex ensures safe update of read_count
5. Conclusion (0.5 Mark)
********** 16 **********
--- page 17 ---
Semaphores ensure proper coordination between readers and
writers, preventing conflicts and maintaining data consistency.
Explain the structure of a disk (tracks, sectors, cylinders).
How does disk organization affect performance?
Ans:
1. Introduction (2 Marks)
A disk is a secondary storage device used to store data permanently.
Data on a disk is organized into tracks, sectors, and cylinders, which
helps in efficient storage and retrieval.
2. Structure of Disk diagram(5 Marks)
Circular paths on the disk surface
Data is stored along these concentric circles
Each track is divided into smaller parts called sectors
Smallest unit of data storage
● set of corresponding tracks across all disk platters
● Same track number on each platter forms a cylinder
3. Impact on Performance (2 Marks)
● Seek Time
Time taken to move head across tracks (major factor)
● Rotational Latency
Time taken for sector to rotate under head
● Data Locality
Storing data in same cylinder reduces movement → faster
access
● Disk Scheduling
Algorithms (SCAN, SSTF) use this structure to optimize
performance
4. Conclusion (1 Mark)
Disk organization plays a crucial role in performance.
Efficient arrangement of data reduces access time and improves overall
system efficiency.
********** 17 **********
--- page 18 ---
FR ICR 7] QA HH
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper dfa5d04cb27f

- Departments: Computer Science
- Programmes: DIPLOMA IN COMPUTER SCIENCE AND ENGINEE
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/DIPLOMA IN COMPUTER SCIENCE AND ENGINEE_04f07abf/Introduction to Operating Systems/ANS_Introduction to Operating Systems(701CO0C022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: mixed (16 pages), mean OCR confidence 78.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Introduction to Operating Systems
Date: 09 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. •   Question No. 1 is compulsory.
3. •   Out of remaining questions, attempt any 4 questions.
4. •   In all 5 questions to be attempted.
5. •   All questions carry equal marks.
6. •   Answer to each new question to be started on a fresh page.
7. •   Figures in brackets on the right hand side indicate full marks.
8. •   Assume Suitable data if necessary.
9.
Q1
Answer briefly:   [20]
a.   Compare deadlock avoidance and deadlock detection approaches in
terms of:
● Runtime overhead
● System knowledge requirements
● Practical applicability in modern operating systems
Conclude which approach is more feasible for large-scale systems and
justify your answer.
Answer:
CO3   ;   1. Introduction (1 Mark)
SO- ; BL-4
Deadlock handling in operating systems can be done using deadlock
avoidance and deadlock detection.
2. Comparison (3 Marks)
Conclusion (1 Mark)
Deadlock detection and recovery is more feasible for large-scale
systems because it is flexible, requires less prior information, and has
lower runtime overhead.
********** 1 **********
--- page 2 ---
b.   Explain the need of long term scheduler.
Ans:
1. Introduction (1 Mark)
The long-term scheduler (also called job scheduler) selects processes
from the job pool (secondary storage) and loads them into main
memory for execution.
2. Need / Functions (3 Marks)
● Controls Degree of Multiprogramming
It decides how many processes are admitted into the system,
thus controlling CPU utilization.
CO2   ;   ● Balances System Load
SO- ; BL-2   Prevents system overload by limiting the number of active
processes.
● Maintains Process Mix
Selects a proper mix of CPU-bound and I/O-bound processes
to improve system performance.
● Efficient Resource Utilization
Ensures memory and CPU resources are used effectively by
selecting appropriate processes.
3. Conclusion (1 Mark)
The long-term scheduler is essential for maintaining system stability,
performance, and efficient resource utilization by controlling which
processes enter the ready queue.
c.   Discuss the need of process synchronization.
Answer:
1. Introduction (1 Mark)
CO3 ;   Process synchronization is required when multiple processes execute
SO- ; BL-2   concurrently and share common resources. It ensures correct and
coordinated execution.
2. Need / Importance (3 Marks)
● Prevents Race Conditions
Without synchronization, multiple processes may access shared
data simultaneously, leading to incorrect results.
********** 2 **********
--- page 3 ---
● Ensures Data Consistency
Maintains accuracy of shared data by controlling access through
proper mechanisms.
● Maintains Mutual Exclusion
Ensures that only one process enters the critical section at a
time.
● Avoids Inconsistency & Errors
Prevents unpredictable system behavior due to concurrent
execution.
3. Conclusion (1 Mark)
Process synchronization is essential for safe, reliable, and correct
execution of concurrent processes in an operating system.
CO4   ; d.   Discuss whether paging truly removes all types of fragmentation and
SO- ; BL-5   justify your answer with appropriate reasoning.
Ans:
1. Introduction (1 Mark)
Paging is a non-contiguous memory allocation technique that divides
memory into fixed-size pages and frames, helping in efficient memory
utilization.
2. Analysis (3 Marks)
● Eliminates External Fragmentation
Paging removes the problem of external fragmentation because
memory is allocated in fixed-size frames, so contiguous
allocation is not required.
● Still Causes Internal Fragmentation
Paging cannot fully utilize the last frame if the process size is
not an exact multiple of page size, leading to unused space
within a frame.
● Example Insight
If page size = 4 KB and process size = 10 KB → 3 pages (12
KB allocated), resulting in 2 KB unused space → internal
fragmentation.
3. Conclusion (1 Mark)
Paging does not eliminate all fragmentation. It removes external
fragmentation but still suffers from internal fragmentation, though
typically less severe.
********** 3 **********
--- page 4 ---
Q2   a.   With the help of a neat diagram, explain the process state model of an   20
CO2   ;   operating system. Discuss each state and analyze the conditions under
SO- ; BL-3   which transitions occur between states.
Answer:
CO4   ; b.
SO- ; BL-3
1. Introduction (2 Marks)
A process state model describes the different states a process goes
through during its lifecycle in an operating system.
It helps in managing process execution, scheduling, and resource
allocation efficiently.
2. Neat Diagram (2 Marks)
3. Explanation of States (3 Marks)
● New
Process is being created.
● Ready
Process is waiting in the ready queue for CPU allocation.
● Running
Process is currently executing on the CPU.
● Waiting (Blocked)
Process is waiting for an event (e.g., I/O completion).
● Terminated
Process has completed execution.
State Transitions (2 Marks)
Analysis / Importance (1 Mark)
Proper management of process states ensures efficient CPU utilization,
multitasking, and system stability.
Explain memory allocation in operating systems.
Describe First Fit, Best Fit, and Worst Fit algorithms with suitable
examples.
Answer:
. Introduction (2 Marks)
Memory allocation is the process by which an operating system
assigns main memory to processes for execution.
********** 4 **********
--- page 5 ---
2. Memory Allocation Strategies (1 Mark)
3. Explanation of Algorithms (4 Marks)
First Fit
● Allocates the first available hole that is large enough.
● Faster as it searches from the beginning.
Example:
Blocks: 100, 500, 200, 300
Process: 212 → allocated to 500
Best Fit
● Allocates the smallest hole that fits the process.
● Searches entire memory.
Example:
Blocks: 100, 500, 200, 300
Process: 212 → allocated to 300
Worst Fit
● Allocates the largest available hole.
● Leaves large remaining free space.
Example:
Blocks: 100, 500, 200, 300
Process: 212 → allocated to 500
a.   Explain different types of threads (user-level and kernel-level threads).
Mention their advantages.
Answer:
Q3
1. Introduction (2 Marks)
CO2   ;
SO- ; BL-3   A thread is the smallest unit of execution within a process.
Threads allow multiple tasks to run concurrently within the same   20
CO3   ;
process, improving performance and responsiveness.
SO- ; BL-2
2. Types of Threads (1 Mark)
There are two main types:
● User-Level Threads (ULT)
b.   ● Kernel-Level Threads (KLT)
********** 5 **********
--- page 6 ---
3. User-Level Threads (3 Marks)
Definition:
Threads managed at the user level by a thread library; the kernel is not
aware of them.
Features:
● Managed in user space
● Faster creation and switching
● No kernel involvement
Advantages:
● Fast context switching
● Low overhead
● Portable across operating systems
4. Kernel-Level Threads (3 Marks)
Definition:
Threads managed directly by the operating system kernel.
Features:
● Kernel is aware of threads
● Each thread scheduled independently
Advantages:
● Better CPU utilization (true parallelism)
● Blocking of one thread does not block others
● Suitable for multiprocessor systems
5. Conclusion (1 Mark)
Both thread types improve system performance.
User-level threads are faster, while kernel-level threads provide better
concurrency and reliability.
What is a semaphore?
Explain its types (binary and counting semaphores) and describe how
they are used in process synchronization with suitable examples.
Answer: 1. Introduction (2 Marks)
********** 6 **********
--- page 7 ---
A semaphore is a synchronization tool used in operating systems to
control access to shared resources by multiple processes.
It helps in preventing race conditions and ensures mutual exclusion.
2. Basic Operations (1 Mark)
Semaphore works using two atomic operations:
● wait() (P operation) → decreases value
● signal() (V operation) → increases value
3. Types of Semaphores (4 Marks)
Binary Semaphore (Mutex)
● Value is either 0 or 1
● Used for mutual exclusion
Example:
Only one process can enter the critical section at a time.
If one process is using the resource, others must wait.
Counting Semaphore
● Value can be greater than 1
● Used when multiple instances of a resource are available
Example:
If 3 printers are available, semaphore value = 3
Up to 3 processes can use printers simultaneously.
4. Use in Process Synchronization (2 Marks)
● Ensures only one process enters critical section (binary
semaphore)
● Controls access to multiple resources (counting semaphore)
● Helps avoid race conditions and inconsistencies
Example (Producer–Consumer):
● empty semaphore → tracks empty buffer slots
● full semaphore → tracks filled slots
● mutex → ensures mutual exclusion
5. Conclusion (1 Mark)
Semaphores are essential for safe and efficient synchronization in
concurrent systems, ensuring proper coordination among processes.
********** 7 **********
--- page 8 ---
Q4   a.   Consider the following process details in system:
CO2   ;
SO- ; BL-3
(Lower number = higher priority)
Questions:
1. Draw Gantt charts for:
○ FCFS
○ SJF (Non-preemptive)
2. Calculate for each algorithm:
○ Waiting Time of each process and average waiting time.
○ Turnaround Time of each process and average
Turnaround
○ Compare all algorithms and identify:
○ Which gives minimum average waiting time   20
○ Which is most suitable for time-sharing systems
Answer:
FCFS Scheduling (3 Marks)
CO1   ; b.   Gantt Chart:
SO- ; BL-5
Average WT = (0+7+10+18+22)/5 = 11.4
********** 8 **********
--- page 9 ---
SJF (Non-Preemptive) (3 Marks)
Average WT = (0+4+9+11+17)/5 = 8.2
Average TAT = 13.8
Compare Monolithic, Layered, and Microkernel architectures.
Evaluate their advantages and limitations, and justify which architecture
is most suitable for modern operating systems.
Answer:
Introduction (2 Marks)
Operating systems are designed using different architectures such as
Monolithic, Layered, and Microkernel.
Each architecture defines how system components interact and impacts
performance, security, and maintainability.
Comparison (4 Marks)
Advantages & Limitations (3 Marks)
Evaluation & Justification (1 Mark)
********** 9 **********
--- page 10 ---
Modern operating systems prefer hybrid approaches (based on
microkernel concepts) because they provide a balance between
performance and security.
Conclusion (1 Mark)
No single architecture is perfect.
However, microkernel-based or hybrid architectures are most
suitable for modern systems due to their modularity, security, and
scalability
Q5   A system uses 4 frames and the following reference string:
CO4 ;   a.
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
SO- ; BL-3
Questions:
1. Apply following algorithms:
○ FIFO
○ LRU
2. Draw the frame table for each algorithm.
3. Count:
○ Page faults
○ Page hits
4. Analyze:
○ Which algorithm gives minimum faults?
Answer:
b.   Given Data (1 Mark)   20
CO5   ;
● Frames = 4
SO- ; BL-4   ● Reference String:
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
2. FIFO Algorithm (4 Marks)
Frame Table:
Page Faults & Hits:
● Page Faults = 10
● Page Hits = 2
LRU Algorithm (4 Marks)
********** 10 **********
--- page 11 ---
Frame Table:
Page Faults & Hits:
● Page Faults = 8
● Page Hits = 4
Analysis (1 Mark)
● LRU gives fewer faults (8) than FIFO (10)
● LRU uses recent usage → better performance
Conclusion (1 Mark)
LRU is better than FIFO as it minimizes page faults by replacing least
recently used pages, making it more efficient in most cases.
Explain I/O management in an operating system.
Discuss I/O buffering and its types, and explain the need for buffering
Answer:
Introduction (2 Marks)
I/O management in an operating system handles communication
between the CPU and I/O devices (keyboard, disk, printer, etc.).
It ensures efficient, safe, and coordinated data transfer between devices
and memory.
Functions of I/O Management (2 Marks)
I/O Buffering (Definition) (1 Mark)
4. Types of Buffering (3 Marks)
Single Buffering
● One buffer is used
● CPU waits while data is transferred
● Simple but less efficient
Double Buffering
● Two buffers used alternately
● One buffer is filled while the other is processed
● Improves performance
Circular (Multiple) Buffering
********** 11 **********
--- page 12 ---
● Multiple buffers used in a circular queue
● Continuous data flow
● Best for high-speed I/O systems
5. Need for Buffering (1 Mark)
● Handles speed mismatch between CPU and I/O devices
● Reduces CPU waiting time
● Improves throughput and efficiency
● Supports asynchronous data transfer
6. Conclusion (1 Mark)
I/O management with buffering improves system performance,
efficiency, and resource utilization, making it essential in modern
operating systems.
Q6   a.   .A disk has 200 tracks (0–199). The disk head is initially at track 50.
CO5   ;   The request queue is:
SO- ; BL-2
82, 170, 43, 140, 24, 16, 190
Questions:
1. Apply the following algorithms:
○ FCFS
○ SSTF
2. For each algorithm:
○ Show the order of servicing requests
○ Calculate the total head movement
3. Compare the results and identify which algorithm gives
minimum seek time.
20
Answer:
1. Given Data (1 Mark)
CO3   ;
b.   ● Disk tracks: 0–199
SO- ; BL-4
●   Initial head position: 50
● Request Queue:
82, 170, 43, 140, 24, 16, 190
2. FCFS Algorithm diagram (4 Marks)
Order of Execution:
50 → 82 → 170 → 43 → 140 → 24 → 16 → 190
********** 12 **********
--- page 13 ---
Head Movement Calculation
Total Head Movement = 32 + 88 + 127 + 97 + 116 + 8 + 174 = 642
STF Algorithm (4 Marks)
Step-by-Step Selection (Nearest First):
50 → 43 → 24 → 16 → 82 → 140 → 170 → 190
Head Movement Calculation:
Total Head Movement = 7 + 19 + 8 + 66 + 58 + 30 + 20 = 208
Comparison & Analysis (1 Mark)
● FCFS Total Movement = 642
● SSTF Total Movement = 208
SSTF gives minimum seek time because it always selects the nearest
request.
Conclusion (1 Mark)
SSTF is more efficient than FCFS in reducing head movement and
seek time.
However, SSTF may cause starvation for distant requests.
Explain the concepts of deadlock, its necessary conditions, and
handling techniques.
Critically evaluate how design choices in deadlock handling affect:
● System throughput
● Resource utilization
● Fairness
Q7   a.
CO3   ;   Explain the concept of concurrency in operating systems.
Differentiate between:
SO- ; BL-4
● Mutual exclusion and synchronization   20
● Binary semaphore and counting semaphore
Ans:
********** 13 **********
--- page 14 ---
CO5   ; b.   1. Introduction (2 Marks)
SO- ; BL-3
A deadlock is a situation in which a set of processes are blocked
because each process is waiting for a resource held by another process.
It results in indefinite waiting and system inefficiency.
2. Necessary Conditions of Deadlock (2 Marks)
Deadlock occurs when all four conditions hold simultaneously:
1. Mutual Exclusion – Resources cannot be shared
2. Hold and Wait – Process holds resources while waiting for
others
3. No Preemption – Resources cannot be forcibly taken
4. Circular Wait – Circular chain of processes waiting
Deadlock Handling Techniques (3 Marks)
Critical Evaluation (2 Marks)
System Throughput
● Prevention ↓ throughput (strict rules)
● Avoidance moderate
● Detection ↑ throughput (more flexibility)
Resource Utilization
● Prevention → poor utilization
● Avoidance → better but cautious
● Detection → high utilization
Fairness
● Prevention → fair but restrictive
● Avoidance → balanced
● Detection → may cause starvation (unfair)
Conclusion (1 Mark)
Deadlock handling involves trade-offs.
Detection and recovery is often preferred in modern systems due to
better performance and flexibility, despite some fairness issues.
Explain SCAN and C-SCAN disk scheduling algorithms.
How are they different from FCFS?
Answer:
********** 14 **********
--- page 15 ---
Introduction (2 Marks)
Disk scheduling algorithms determine the order in which disk I/O
requests are serviced.
SCAN and C-SCAN are advanced algorithms designed to reduce seek
time compared to simple methods like FCFS.
2. SCAN Algorithm (2 Marks)
● Also called Elevator Algorithm
● Disk head moves in one direction servicing requests, then
reverses direction
Working:
Head moves from one end to the other, servicing all requests in its
path.
Advantages:
● Better performance than FCFS
● Reduces total head movement
Disadvantage:
● Requests at ends may wait longer
3. C-SCAN Algorithm (2 Marks)
● Circular version of SCAN
● Head moves in one direction only
● After reaching end, jumps to the beginning without servicing
requests on return
Working:
Services requests in one direction → jumps back → continues
Advantages:
● Provides uniform waiting time
● Avoids starvation at ends
Disadvantage:
● Slightly more head movement due to jump
Difference between SCAN, C-SCAN and FCFS (3 Marks)
Conclusion (1 Mark)
SCAN and C-SCAN significantly improve disk performance over
FCFS.
********** 15 **********
--- page 16 ---
Among them, C-SCAN is preferred for systems requiring uniform
response time and fairness.

FRR ICR 7 6 AC OH
````
