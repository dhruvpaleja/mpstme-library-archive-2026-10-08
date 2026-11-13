# Operating Systems: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper f30513de6164

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2024/Sem_05/Final-Exam/BTech_Computer_7002/Operating Systems/ANS_Operating Systems(702CO1C002)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: mixed (22 pages), mean OCR confidence 39.8
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MBA Tech (AI)/MBA Tech (Comp)
Year: II / III / V/Semester III/Semester IX/Semester V(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 28 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1 A What do you mean by Dual mode Operation in OS? Explain with suitable 5
diagram?
Definition (2 mark)
Explanation (2 marks)
Diagram (1 Mark)
Dual Mode Operation is a feature of modern operating systems that allows the
CPU to operate in two distinct modes — User Mode and Kernel (Supervisor)
Mode — to ensure system security and stability. It prevents user programs
from directly accessing critical system resources.
• User Mode:
o Used to execute user applications.
o Access to hardware and system resources is restricted.
o System calls are used to request OS services.
• Kernel Mode:
o Used by the operating system to execute privileged instructions.
o Has unrestricted access to hardware and system memory.
o Switching from user mode to kernel mode occurs through
interrupts or system calls.
The mode bit in the CPU (usually 0 = kernel, 1 = user) determines the current
operating   mode.
********** 1 **********

[Text in pictures on this page, read by OCR]
user process

user mode
user process executing | calls system call | | return from system call (mode bit = 1)
\
st Z
t ra
trap return
Kemal mode bit = 0 mode bit = 1

\ kernel mode
execute system call (mode bit = 0)
--- page 2 ---
When an interrupt or system call occurs, the mode bit switches to kernel mode;
when control returns to the user process, it switches back to user mode.
Advantages / Purpose
•   Protects OS and hardware from faulty or malicious user programs.
• Maintains system stability and security.
• Ensures controlled access to resources through system calls only.
B A student writes the following Producer-Consumer code:   5
semaphore full = 0, empty = N, mutex = 1;
Producer() {
while (true) {
produce_item(x);
wait(full);
wait(mutex);
insert(x);
signal(mutex);
signal(empty);
}
}
Consumer() {
while (true) {
wait(empty);
wait(mutex);
remove(x);
signal(mutex);
signal(full);
consume_item(x);
}
}
Identify the mistakes in semaphore usage and correct the code.
Explanation: 1 mark
Corrected code : 4 marks
Semaphore wait/signal on full and empty are reversed in Producer and
Consumer:
• The Producer should wait on empty (wait for empty slot) before
inserting an item, then signal full (indicate one more full slot).
• The Consumer should wait on full (wait for an item) before removing,
then signal empty (indicate one more empty slot).
.
semaphore full = 0, empty = N, mutex = 1;
Producer() {
while (true) {
produce_item(x);
wait(empty);   // wait for an empty slot
wait(mutex);
********** 2 **********
--- page 3 ---
insert(x);
signal(mutex);
signal(full);   // signal that a new item is available
}
}
Consumer() {
while (true) {
wait(full);   // wait for an available item
wait(mutex);
remove(x);
signal(mutex);
signal(empty);   // signal that a slot is now free
consume_item(x);
}
}
C What is deadlock prevention? Discuss any two strategies used for preventing
deadlocks in an operating system.
Deadlock Prevention 1 Mark
Strategy 2 Mark each (4 Marks)
Deadlock prevention is a proactive method of ensuring that the system is
designed in such a way that at least one of the necessary conditions for
deadlock can never occur.
The four necessary conditions for deadlock are:
1. Mutual Exclusion
2. Hold and Wait
3. No Preemption
4. Circular Wait
Deadlock prevention works by denying or controlling these conditions.
Invalidate one of the four necessary conditions for deadlock:
▪ Mutual Exclusion – not required for sharable resources (e.g., read-only
files); must hold for non-sharable resources
▪ Hold and Wait – must guarantee that whenever a process requests a
resource, it does not hold any other resources
• Require process to request and be allocated all its resources
before it begins execution, or allow process to request resources
only when the process has none allocated to it.
• Low resource utilization; starvation possible
▪ No Preemption:
•   If a process that is holding some resources requests another
resource that cannot be immediately allocated to it, then all
resources currently being held are released
• Preempted resources are added to the list of resources for which
the process is waiting
•   Process will be restarted only when it can regain its old
resources, as well as the new ones that it is requesting
▪ Circular Wait:
********** 3 **********
--- page 4 ---
• Impose a total ordering of all resource types, and require that
each process requests resources in an increasing order of
enumeration
D Compare blocking, non-blocking, and asynchronous I/O operations by
explaining how each works in practice, and provide examples to illustrate the
differences.
Each operation 1 Mark (3 Marks)
Example 2 Marks
Blocking I/O: Process suspended until I/O completed; easy to use and
understand; sufficient for simple sequential operations
Nonblocking I/O: Returns immediately with available data; implemented via
multi-threading; useful for user interfaces and buffered I/O; uses select() to
check data availability
Asynchronous I/O: Process continues execution while I/O executes; difficult
to use but efficient; I/O subsystem signals process upon completion
Examples: Blocking for simple file reads, nonblocking for network servers
handling multiple connections, asynchronous for high-performance database
operations
2 A Explain the Dining Philosophers problem and critically analyze the reasons 10
why semaphore-based implementations may result in deadlock or starvation.
Propose and justify a monitor-based solution that addresses these issues.
Description: 2 marks
Why semaphore solution Fail: 2 marks
Monitor solution: 6 marks
Description:
● 5 philosophers’ sit at a round table with a bowl of rice in the middle.
● They spend their lives alternating thinking and eating.
● They do not interact with their neighbors.
● Occasionally try to pick up 2 chopsticks (one at a time) to eat from bowl
.
● Need both to eat, then release both when done
Why semaphore solution Fail:
● Although this solution guarantees that no two neighbors are eating
simultaneously, it nevertheless must be rejected because it could create
a deadlock.
● Suppose that all five philosophers become hungry at the same time and
each grab their left chopstick. All the elements of chopstick will now
be equal to 0. When each philosopher tries to grab their right chopstick,
they will be delayed forever
Monitor solution:
monitor DiningPhilosophers
{
enum ( THINKING, HUNGRY, EATING)
state [5] ;
condition self [5];
void pickup (int i) {
state[i] = HUNGRY;
********** 4 **********
--- page 5 ---
test(i);
if (state[i] != EATING)
self[i].wait;
}
void putdown (int i) {
state[i] = THINKING;
// test left and right neighbors
test((i + 4) % 5);
test((i + 1) % 5);
}
void test (int i) {
if ((state[(i + 4) % 5] != EATING) &&
(state[i] == HUNGRY) &&
(state[(i + 1) % 5] != EATING) ) {
state[i] = EATING ;
self[i].signal () ;
}
}
initialization_code() {
for (int i = 0; i < 5; i++)
state[i] = THINKING;
}
}
B Consider the following processes with their arrival times, burst times, and 10
priorities.
Process   Arrival Time   Burst Time   Priority
P1   0   10   2
P2   1   4   1
P3   3   7   3
P4   4   6   2
P5   6   5   0
i. Considering pre-emptive priority scheduling algorithm (lower priority
numbers indicate higher priority), calculate the average turnaround
time and average waiting time for the given batch of processes.
ii. Considering round-robin scheduling algorithm (with time quantum =
4), calculate the average turnaround time and average waiting time for
the given batch of processes.
********** 5 **********
--- page 6 ---
(GC = 2 marks, Avg. TAT = 1.5 marks, Avg. WT = 1.5 marks)
(GC = 2 marks, Avg. TAT = 1.5 marks, Avg. WT = 1.5 marks)
3 A Consider the following snapshot of a system running 5 processes:
Process Allocation   Max   Available
A   B   C A   B   C A   B   C
P1   0   1   0   7   5   3   3   3   2
P2   2   0   0   3   2   2
P3   3   0   2   9   0   2
P4   2   1   1   2   2   2
P5   0   0   2   4   3   3
********** 6 **********
--- page 7 ---
Answer the following: -
i. How many resources of type A, B, C are there?
ii.   Calculate the need matrix?
iii.   Determine if the system is safe or not.
iv.   What will happen if the resource request (1, 0, 0) for process P1 arrive,
can the system accept this request immediately?
Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks
Safe Sequence 3 Marks
Additional Request 3 Marks
Total Resources = Available + Allocation
A B C
10 5 7
Need Matrix = Max – Allocation
Process Need Matrix
A   B
C
P1   7   4   3
P2   1   2   2
P3   6   0   0
P4   0   1   1
P5   4   3   1
Finding out system is safe or not. And if safe then the sequence of process
execution.
Check if Need matrix <= Available
Process P2 need ca be full filled
New Available = Available – Need [P2]
A B C
2 1 0
After P2 complete, Available = New Available + Max[P2]
A B C
5 3 2
Next Process P4 need ca be full filled
New Available = Available – Need [P4]
A B C
5 2 1
After P4 complete, Available = New Available + Max[P4]
A B C
7 4 3
Next Process P5 need ca be full filled
New Available = Available – Need [P5]
********** 7 **********
--- page 8 ---
A B C
3 1 2
After P5 complete, Available = New Available + Max[P5]
A B C
7 4 5
Next Process P1 need ca be full filled
New Available = Available – Need [P1]
A B C
0 0 2
After P1 complete, Available = New Available + Max[P1]
A B C
7 5 5
Next Process P3 need ca be full filled
New Available = Available – Need [P3]
A B C
1 5 5
After P3 complete, Available = New Available + Max[P3]
A B C
10 5 7
If Available == Total Resources.
Then the system is in safe state and one of the sequences of the process
execution will be
P2 -> P4 -> P5 -> P1 -> P3
Showing the request of P1 (1,0,0) is acceptable or not.
In the provided available recourses that is
A B C
3 3 2
If we grant P1 (1,0,0) then new available will be
A B C
2 3 2
With these available resources still, we can proceed with the safe sequences of
the all the process. That’s why we can grant P1 request immediately.
B Explain the concept of paging and its purpose in memory management. With 10
the help of a neat diagram, describe how paging hardware translates a logical
address into a physical address. How the Translation Lookaside Buffer (TLB)
can enhances the performance of paging.
Marks Distribution:
Explanation of paging and need – 4 Marks
Paging hardware representation – 4 Marks
Role of TLB in paging – 2 Marks
Definition:
Paging is a memory management technique in which the logical (virtual)
memory of a process is divided into fixed-size blocks called pages, and the
physical memory (RAM) is divided into blocks of the same size called frames.
********** 8 **********
--- page 9 ---
When a program is executed, its pages are loaded into available frames in main
memory, not necessarily in a contiguous manner.
Need for Paging:
1. Eliminates External Fragmentation:
Since pages and frames are of fixed size, there are no variable-sized
memory holes.
2. Efficient Memory Utilization:
Allows non-contiguous memory allocation — unused gaps between
processes are minimized.
3. Simplifies Memory Management:
The operating system can manage memory using page tables rather than
complex variable partitions.
4. Supports Virtual Memory:
Enables programs larger than physical memory to execute by loading
only required pages.
Role of Translation Lookaside Buffer (2 Marks)
• Every memory access in a paging system requires two memory
references:
o One to access the page table (to find the frame number).
o Another to access the actual data in memory.
• This doubles the access time.
To solve this, a Translation Lookaside Buffer (TLB) is used.
TLB:
• A special high-speed cache that stores recently used page table entries
(page–frame mappings).
• When a logical address is generated:
o   If the page number is found in the TLB (TLB hit), the frame
number is retrieved instantly.
o   If not found (TLB miss), the page table is accessed and the
TLB is updated.
4 A Operating systems provide an environment for execution of programs and,
offers services to programs and users. Justify the statement by explaining the
operating system services with suitable diagram?
Justification (3 Marks)
********** 9 **********

[Text in pictures on this page, read by OCR]
frame e

logical address physical address 0x000
frame f
cpu slp | a |
p — Oxfff
f frame g

physical memory

page table
--- page 10 ---
Operating System Services any five (5 Marks)
Diagram (2 Marks)
An Operating System (OS) serves as an essential layer between the hardware
and the user/programs, ensuring efficient, reliable, and convenient execution
of   applications.
It provides an execution environment where multiple programs can run
concurrently, share resources, and interact with hardware safely.
The OS not only controls hardware but also delivers services that simplify
program   execution   and   enhance   user   productivity.
Thus, it can be viewed as both a resource manager and a service provider.
Justification
Without the operating system, users would have to directly manage complex
hardware operations such as memory allocation, device communication, or
process   synchronization.
The OS abstracts these complexities by offering well-defined services such as
program execution, file management, and interprocess communication.
By providing these services:
• The OS ensures convenience — users can run programs without
handling hardware details.
•   It ensures efficiency — resources like CPU, memory, and I/O are
allocated optimally.
•   It ensures security and reliability — through error handling and
protection mechanisms.
Hence, the OS creates a controlled, stable, and user-friendly environment for
both users and system programs.
Operating System Services (5 Marks)
1. Program   Execution:
Loads, runs, and terminates programs. Manages process scheduling and
transitions.
2. I/O   Operations:
Provides a uniform interface for input/output devices, abstracting
hardware details.
3. File   System   Manipulation:
Manages file creation, deletion, access control, and organization in
secondary storage.
4. Inter-process   Communication   (IPC):
Enables process coordination and data exchange through shared
memory or message passing.
5. Error   Detection   and   Handling:
Monitors the system to detect and respond to hardware or software
errors gracefully.
6. Resource   Allocation:
Dynamically allocates CPU time, memory, and I/O to competing
processes fairly.
********** 10 **********
--- page 11 ---
7. Accounting:
Tracks system and resource usage for performance monitoring and
optimization.
8. Protection   and   Security:
Ensures data privacy and system integrity through controlled access and
authentication.
The OS provides a well-defined execution environment by hiding hardware
complexity, managing concurrent activities, ensuring safe resource sharing,
and delivering reliable services.
Therefore, the statement is justified: “Operating Systems provide an
environment for execution of programs and services to both programs and
users.”
B A disk queue has requests on cylinders 2069, 1212, 2296, 2800, 544, 1618,
356, 1523. The disk head is currently positioned at cylinder 2150. The disk has
cylinders numbered from 0 to 4999.
Calculate the total head movement (in cylinders) required to service all
requests using the following disk scheduling algorithms:
1. FCFS (First-Come-First-Served)
2. SCAN (Elevator Algorithm), assuming the head is initially moving
towards the highest cylinder (4999).
3. C-SCAN (Circular SCAN), assuming the head is initially moving
towards the highest cylinder (4999).
Compare the performance of the three algorithms based on their total head
movement and discuss one major factor of comparison.
Each algorithm 3 marks (9 marks)
Comparison 1 mark
********** 11 **********

[Text in pictures on this page, read by OCR]
user and other system programs

GUI touch screen | command line

user interfaces

system calls

program vO file a resource
communication

. A a accounting
execution operations systems allocation

protection
and
security

error
detection
services

operating system

hardware
--- page 12 ---
Performance Comparison: SCAN has the lowest head movement (7492
cylinders), making it the most efficient algorithm for this specific batch of
********** 12 **********

[Text in pictures on this page, read by OCR]
Performance Comparison

ALGORITHM TOTAL MOVEMENT CHARACTERISTICS
FCFS 8,285 Simple, fair, but high seek time
SCAN 7,492 Fair, predictable, moderate performance

C-SCAN 9,917 More uniform wait time, higher movement
--- page 13 ---
requests and head position. FCFS performs better than C-SCAN, but SCAN is
the most efficient of the three.
Major Factor of Comparison: Uniformity of Wait Time
The major factor distinguishing SCAN and C-SCAN is the Uniformity of Wait
Time.
• SCAN: Causes a non-uniform wait time. Requests that are waiting just
behind the reversing head (e.g., at cylinder 4900 after the head has just
left it going towards 0) will have to wait for the entire sweep to the
other end (0) and back, leading to a much longer latency than requests
near the ends.
• C-SCAN: Provides a more uniform wait time. By always servicing
requests in only one direction and immediately jumping back to the
start, C-SCAN ensures that a new request waits, at most, for the time it
takes the head to complete one full circular sweep, regardless of its
position on the disk. This predictability is highly valuable in high-
performance or heavy-load systems.
5 A Describe the concept of Message Passing by explaining its fundamental
primitives and addressing methods. Support your explanation with a neat
diagram of the general message format.
Message passing: 2 marks
Primitives: 3 marks
Addressing: 2 marks
Message format: 3 marks
Message Passing:
● When processes interact with one another, two fundamental
requirements must be satisfied: synchronization and communication.
● Processes need to be synchronized to enforce mutual exclusion;
cooperating processes may need to exchange information.
● One approach to providing both of these functions is message passing.
● Message passing has the further advantage that it lends itself to
implementation in distributed systems as well as in shared-memory
multiprocessor and uniprocessor systems.
Primitives:
● We need to specify what happens to a process after it issues a send or
receive primitive.
● When a send primitive is executed in a process, there are two
possibilities: Either the sending process is blocked until the message is
received, or it is not.
● Similarly, when a process issues a receive primitive, there are two
possibilities:
1. If a message has previously been sent, the message is received and execution
continues.
2. If there is no waiting message, then either (a) the process is blocked until a
message arrives, or (b) the process continues to execute, abandoning the
attempt to receive.
● Thus, both the sender and receiver can be blocking or nonblocking.
● Three combinations are common, although any particular system will
usually have only one or two combinations implemented:
********** 13 **********
--- page 14 ---
1. Blocking send, blocking receive: Both the sender and receiver are blocked
until the message is delivered; this is sometimes referred to as a rendezvous.
This combination allows for tight synchronization between processes.
2. Nonblocking send, blocking receive: Although the sender may continue on,
the receiver is blocked until the requested message arrives. This is probably
the most useful combination. It allows a process to send one or more messages
to a variety of destinations as quickly as possible. A process that must receive
a message before it can do useful work needs to be blocked until such a
message arrives. An example is a server process that exists to provide a service
or resource to other processes.
3. Nonblocking send, nonblocking receive: Neither party is required to wait.
Addressing:
● The various schemes for specifying processes in send and receive
primitives fall into two categories: direct addressing and indirect
addressing.
● With direct addressing, the send primitive includes a specific identifier
of the destination process.
● The receive primitive can be handled in one of two ways. One
possibility is to require that the process explicitly designate a sending
process. Thus, the process must know ahead of time from which process
a message is expected.
● The other general approach is indirect addressing. In this case,
messages are not sent directly from sender to receiver, but rather are
sent to a shared data structure consisting of queues that can temporarily
hold messages.
● Such queues are generally referred to as mailboxes. Thus, for two
processes to communicate, one process sends a message to the
appropriate mailbox, and the other process picks up the messages from
the mailbox.
B Analyze how hardware address protection mechanisms, such as base and limit
registers, prevent illegal memory access. Illustrate your answer with an
example of process isolation. Consider six memory partitions of size 350 KB,
700 KB, 580 KB, 450 KB, and 300 KB in the same order. Considering
contiguous memory allocation, show how the first-fit, best-fit and worst-fit
algorithms will place the processes of 360 KB, 600 KB, 425 KB, and 250 KB
(in order).
********** 14 **********

[Text in pictures on this page, read by OCR]
Message Type
Destination ID
Header Source ID
Message Length
Control Information

Body 1 Message Contents

Figure 5.19 General Message Format
--- page 15 ---
Marks Distribution:
Address protection mechanism 2 marks
Process isolation 2 marks
First Fit – 2 marks
Best Fit – 2 marks
Worst Fit – 2 marks
Hardware address protection is a mechanism in an operating system that
ensures each process accesses only its allocated memory space. This protection
is achieved through special hardware registers — primarily the base register
and limit register — which define the valid address range for each process.
Base Register: Holds the starting physical address of the process’s memory
space.
Limit Register: Specifies the size or maximum offset of the process’s
addressable memory range.
When a process generates an address (logical address), the hardware adds the
base value to it to get the physical address.
Before accessing memory, the hardware checks whether the logical address is
less than the limit. If it exceeds, the access is blocked, and a trap or exception
is raised.
If 0 ≤ Logical Address < Limit ⇒ Access Allowed
Else ⇒ Trap (Illegal Access)
Process Isolation Example
Consider two processes — P1 and P2.
P1 has Base = 1000 and Limit = 500, so it can access physical addresses 1000–
1499.
P2 has Base = 2000 and Limit = 400, so it can access addresses 2000–2399.
If P1 tries to access memory location 1800, the hardware check will detect it
is beyond its limit (1499), triggering a trap — thereby preventing illegal access
to P2’s memory region.
********** 15 **********
--- page 16 ---
FOI 7 6 FC Cr
--- page 17 ---
6 A   I.   Illustrate and describe, using a suitable diagram, how a process 10
transitions through various states during its execution.
II.   Identify and explain the conditions under which each state transition
takes place.
III.   Apply your understanding of process scheduling to explain two
scenarios in which a process may transition from the Running state to
the Ready state before completing its CPU burst.
I.   4 marks
II.   3 Marks
III.   3 Marks
Solution: i. State Transition diagram - (4 marks)
i. Transitions occurrence: (3 marks)
• New→Ready: admitted by long-term scheduler.
• Ready→Running: selected by CPU scheduler.
• Running→Waiting: I/O request, page fault, lock wait.
********** 17 **********
--- page 18 ---
• Waiting→Ready: I/O completes, event/interrupt occurs.
• Running→Ready: preempted by higher priority or time slice expiry.
• Running→Terminated: process exit/abort.
ii. As stated in the Lifecycle diagram, a process may move from the
Running state to the Ready state before completing its CPU burst due
to pre-emption (I/O or event wait) or priority-based scheduling events
(interrupts). - (3 marks)
B A system uses 4 frames for storing process pages in main memory. Assume
that all the page frames are initially empty. Consider the page reference string
given below:
2,3,4,5,3,2,6,7,3,2,3,4,8,7,4,3,2,3,4,7
I.   Simulate the page replacement using the FIFO algorithm.
II.   Simulate the page replacement using the LRU algorithm.
III.   Simulate the page replacement using the Optimal algorithm.
IV.   For each algorithm, calculate the total number of page faults.
V.   Based on your results, which algorithm performs best and why?
Marks Distribution:
2 marks each on every point of questions i.e. 5 * 2 = 10 marks
a)
b)
********** 18 **********

[Text in pictures on this page, read by OCR]
2 3
7 2
| 3
FOF
3 4
6 4
7 7
3 3
2 2
F

Total Page Fault:

F

14

F

F
--- page 19 ---
c)
d) Total number of page faults:
FIFO:14, LRU:10, optimal: 8
e) Based on your results, which algorithm performs best and why?
Optimal minimizes page faults by always replacing the page that will not be
used for the longest time in the future. It uses future knowledge, making it
theoretical but ideal for benchmarking. LRU is better than FIFO because it
uses past usage patterns (replacing least recently used), while FIFO doesn’t
consider usage, just arrival order.
7 A What is resource allocation graph? Consider the following snapshot of a
system having 2 resources (R1 having 1 instance and R2 having 2 instances)
and running 3 processes.
Process   Allocation   Request
R1   R2 R1   R2
P1   1   0 0   1
********** 19 **********

[Text in pictures on this page, read by OCR]
LRU

2 3 4
2 2 2
3 3
4
F F F
3 4 8
2 2 2
3 3 3
6 4 4
7 7 8
F F

Total Page Fault: 10

2 3
2 [2
_| 3
FOF
_3| 4
2 [2
—3| [3
_4 4
7 7

Total Page Fault:
--- page 20 ---
P2   0   1 1   0
P3   0   1 0   0
Draw the resource allocation graph. Find if there is a deadlock or not? If there
is no deadlock then what will be the sequence of the process to get executed?
RAG description 3 marks
Draw RAG 4 marks
Safe Sequence 3 marks
i) What is resource allocation graph? [3 Marks]
 A useful tool in characterizing the allocation of resources to processes
is the resource allocation graph.
 The resource allocation graph is a directed graph that depicts a state of
the system of resources and processes, with each process and each
resource represented by a node.
 A graph edge directed from a process to a resource indicates a resource
that has been requested by the process but not yet granted.
 Within a resource node, a dot is shown for each instance of that
resource.
 Examples of resource types that may have multiple instances are I/O
devices that are allocated by a resource management module in the OS.
 A graph edge directed from a reusable resource node dot to a process
indicates a request that has been granted; that is, the process has been
assigned one unit of that resource.
ii) Draw a resource allocation graph of the following table? [4 Marks]
********** 20 **********
--- page 21 ---
iii) Find if there is a deadlock or not? If there is no deadlock then what will be
the sequence of the process to get executed?   [3 Marks]
There is no deadlock in the resource allocation graph.
The sequence of process to execute in safe sequence is
P3 -> P1 ->P2
B Define a PCB. How can it help in enabling multi-tasking?   5
Definition 1 Mark
Explanation 4 marks
Solution: A Process Control Block (PCB) is a data structure maintained by
the Operating System that contains all the essential information about a
process.   (1 mark)
Multitasking means executing multiple processes seemingly at the same time
by rapidly switching the CPU between them.
Here’s how PCB makes that possible:
1. Context Saving:
a. When a running process is interrupted (e.g., due to time slice
expiry or I/O request),
the OS saves its current CPU state (registers, PC, etc.) into its
PCB.
2. Context Restoration:
a. When the process is scheduled again, the OS restores the saved
state from its PCB.
The process resumes exactly where it left off.
3. Accurate Process Switching:
a. The PCB ensures that switching between processes (context
switching) does not corrupt data or execution flow.
4. Tracking Multiple Processes:
********** 21 **********
--- page 22 ---
a. Each process has its own PCB, so the OS can easily track,
suspend, resume, or terminate any process at any time.
(4 marks)
C Summarize the main file attributes managed by a file system and explain the 5
common operations that can be performed on a file.
Key Attributes 2.5 marks
File Operations 2.5 marks
Key File attributes:
File attributes are pieces of information maintained by the file system about a
file and are typically kept in the directory structure on the disk.
Name: This is the only file information kept in human-readable form.
Identifier: This is a unique tag (a number) that identifies the file within the
file system.
Type: This is needed for systems that support different types of files.
Location: This is a pointer that indicates the file's location on the storage
device.
Size: This records the current size of the file.
Protection: This controls who can perform operations such as reading,
writing, and executing the file.
Time, Date, and User Identification: This data is maintained for protection,
security, and monitoring file usage.
Major File Operations:
The operating system provides several major operations that can be
performed on files:
Create: This operation creates a new file.
Write: This operation writes data to the file starting at the current write
pointer location.
Read: This operation reads data from the file starting at the current read
pointer location.
Delete: This operation deletes the file.
Open (Fj): This operation involves searching the directory structure on disk
for the entry Fj and moving the content of that entry into memory.
Close (Fi): This operation moves the content of file entry Fi from memory
back to the directory structure on the disk.
Reposition (Seek): This operation moves the read/write pointer within the
file.
Truncate: This operation zeros the file length and keeps the attributes, but
discards the file's contents.
********** 22 **********
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper cf0a2c29db19

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Operating Systems/ANS_Operating Systems(703CO1C002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: mixed (9 pages), mean OCR confidence 89.7

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester I(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 08 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compuslory
3. Out of the remaining question, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Answer each new question to be started on a fresh page
7. Figures in brackets on the right-hand side indicate full marks
8. Assume suitable data if necessary
Q1
Answer briefly:
a.   Describe the importance of the Process Block and explain its contents.
Ans
1. Importance of the Process Block
The Process Block represents the core functional unit of a system. It is
where the main operations or transformations on input data occur.
Essentially, it defines how inputs are processed to produce
meaningful outputs.
Key Reasons for Its Importance:
CO-
2;SO-   • Central Functionality: It performs the actual computation or   5
1,6;BL-2   logic that defines the system’s purpose.
• Data Transformation: Converts raw input data into useful
information through calculations, filtering, decision-making, or
control actions.
• System Understanding: In a block diagram, the process block
helps visualize the flow of operations, making system design and
analysis easier.
• Modularity: It allows complex systems to be broken into
smaller, manageable units, each handling a specific process.
• Debugging and Optimization: Understanding the process block
helps in identifying performance bottlenecks or logical errors.
********** 1 **********
--- page 2 ---
2. Contents of a Process Block
b.   Differentiate Concurrent vs Co-operative processes.
Ans
CO-
2;SO-   5
1;BL-4
c.   Discuss internal and external fragmentation in memory management.
Ans
CO-
3;SO-   5
1,6;BL-2
CO-   d.
4;SO-   Explain three different categories of DMA configurations.   5
1,6;BL-2
Q2   A set of processes that must be scheduled on a single CPU. All the
CO-   a.   times are given in milliseconds.   5+5
Process Name   Arrival Time   Execution Time
2;SO-   1   0   6
1;BL-3   2   3   2
3   5   4
CO-   4   7   6
3;SO-   5   10   3
Apply SRT and SJF. Calculate the average turnaround time and average
1,6;BL-2   waiting time.
********** 2 **********

[Text in pictures on this page, read by OCR]
Component Description |

Input Variables / Signals Data or signals entering the block from sensors, user input, or preceding block

Processing Logic / Algorithm The core set of instructions, mathematical computations, or decision rules that
manipulate the input.

Parameters / Constants Fixed values or coefficients used in the computations (e.g., filter coefficients,
learning rates).

Control Signals Signals that determine how the processing occurs (e.g., mode selection, timin,
control).
Output Variables / Signals The processed data or results generated and sent to the next block.

Memory or Storage (if applicable) Temporary or permanent data storage used during processing (e.g., buffers,

Feature Internal Fragmentation External Fragmentation

Location of Wastage Inside allocated memory block Between allocated blocks
Cause Fixed-size allocation Variable-size allocation
Occurs In Paging, partitioned systems Contiguous memory allocation
Visibility Hidden (within a process block) Visible (as free holes)
Possible Solution Reduce block size or use variable partitions Compaction or paging

Example 3.2 KB process in 4 KB block > 0.8 KB Free memory scattered across RA
--- page 3 ---
b.
Explain the need for the replacement of algorithms.
1+9
Three frames have been allocated to a process. Reference string is
1,3,1,2,4,5,6,3,2,5,4,3,2. Calculate the hit and miss ratio for all three
algorithms. (FIFO, LRU, OPT). Give an analysis on these methods.
a.   Explain the purpose of disk-scheduling policies.   2+8
Ans
Q3
CO-
3;SO-
1;BL-3
CO-
Consider the following disk request sequence for a disk with 300 tracks:
1;SO-
76, 124, 17, 269, 201, 29, 137. Head pointer starting at 76. Apply
1,6;BL-2
FCFS, SSTF, C-SCAN, and LOOK Disk Scheduling Algorithms. If one
adjacent track movement takes 0.3ms, what is the total time taken for
the whole request for individual methods? Compare their Efficiency.
(Assume initially the head movement for C-SCAN:-outwards and
LOOK:-inwards)
Explain the Layered vs Monolithic architecture. List two advantages
and disadvantages of each. (Include diagrams)
********** 3 **********

[Text in pictures on this page, read by OCR]
Reason Explanation 6

1. Limited Physical Memory The total size of all running processes often exceeds the size of physical RAM.
Replacement is required to free space for new pages.

2. Page Fault Handling When a required page is not in memory (page fault), the OS must decide which
existing page to remove — replacement algorithms guide this choice.

3. Efficient Memory Utilization Helps in keeping the most useful or frequently used pages in memory, improving
system performance.

4, Minimizing Page Faults Agood algorithm reduces the number of page faults, thus minimizing the time
spent in disk I/O (which is much slower than RAM access).

5. Maintaining Process Continuity Ensures that a process can continue its execution smoothly by loading required
pages and replacing less useful ones.

6. System Stability and Efficient replacement ensures balanced resource use, better CPU utilization, an
Throughput higher system throughput.

1. Minimize Seek Time The seek time is the time taken by the disk arm to move to the desired
track. Scheduling helps in arranging requests to minimize this head

movement.
2. Reduce Rotational Latency and Access By smartly ordering requests, the policy reduces the average time spent
Time waiting for the disk to rotate to the right position.
3. Improve Throughput More I/O operations can be completed per unit time if the disk arm

moves efficiently.

4. Ensure Fairness Every I/O request should get a fair chance to be serviced; no request
should starve (wait indefinitely).

5. Optimize System Performance Reducing disk access time improves overall system speed, especially in
\/O-intensive applications.

6. Prioritize Critical Requests Some algorithms can handle high-priority requests faster (e.g., real-time
systems).
--- page 4 ---
b.   5+5
a.   Demonstrate how the semaphore is helping to solve the Readers’
10
Writers Problem.
We must ensure:
1. No two writers write at the same time.
2. No reader reads while a writer is writing.
3. Multiple readers can read together (if no writer is active).
Semaphores are used for process synchronization and mutual
exclusion.
They prevent race conditions and ensure the above rules are satisfied.
We typically use:
• mutex → Protects the reader count variable.
• rw_mutex → Controls access to the shared resource (file/data).
• read_count → Tracks the number of active readers.
Q4
CO-
semaphore mutex = 1;   // For protecting read_count
2;SO-
semaphore rw_mutex = 1;   // For controlling access to shared data
1,6;BL-3
int read_count = 0;   // Number of readers currently reading
CO-
// Entry Section
2;SO-
wait(mutex);   // Lock read_count update
1,6;BL-2
read_count = read_count + 1;
if (read_count == 1)
wait(rw_mutex);   // First reader locks the resource
signal(mutex);   // Release mutex
// Critical Section (Reading)
... (read the data) ...
// Exit Section
wait(mutex);
read_count = read_count - 1;
if (read_count == 0)
signal(rw_mutex);   // Last reader unlocks the resource
signal(mutex);
// Entry Section
wait(rw_mutex);   // Only one writer (or no readers)
// Critical Section (Writing)
... (write to the data) ...
********** 4 **********
--- page 5 ---
// Exit Section
signal(rw_mutex);
Explain the necessary conditions for deadlock, and different ways of
preventing the deadlock in an executable system.
Ans
4+6
b.
Discuss three File allocation methods in detail.   10
a.
Q5.
CO-
4;SO-
1;BL-2
CO-
2;SO-
1,6;BL-2
4+6
********** 5 **********

[Text in pictures on this page, read by OCR]
. Multiple Readers Allowed:
All readers can enter the critical section concurrently once the first reader acquires the lock.

. Writers Get Exclusive Access:

rw_mutex ensures that if a writer is writing, no readers or other writers can enter.

. No Race Condition:

The mutex semaphore prevents concurrent modification of read_count .

A deadlock occurs only if all the following four conditions hold simultaneously (Coffman conditions):

Condition Description Example

1. Mutual Exclusion At least one resource must be held in a non-shareable Printer can be used by only one
mode. Only one process can use the resource at a time. process at a time.

2. Hold and Wait Aprocess holding at least one resource is waiting to Process P11 holds R1 and waits for R2.

acquire additional resources held by others.

3. No Preemption Resources cannot be forcibly taken away; they must be OS cannot take a printer away from a
released voluntarily by the process. process in use.

4. Circular Wait Aclosed chain of processes exists such that each P1—R1— P2-—R2-P1 (cycle
process holds at least one resource needed by the next formed).

process in the chain.

Method Description Example OS Usage

©) Contiguous Allocation Stores each file in one continuous block of Early systems, CD-ROMs
memory on disk

B Linked Allocation Each file is a linked list of disk blocks FAT file systems

© Indexed Allocation Uses an index block that stores all pointers to UNIX, NTFS
the file's data blocks

Feature Contiguous Linked Indexed Oo

Access Type Random/Sequential Sequential Random/Sequential
Fragmentation External None None

Space Overhead None Pointer per block Index block

File Growth Difficult Easy Easy

Access Speed Fast (for sequential) Slow (pointer traversal) Moderate
Implementation Complexity Simple Moderate High

{© Conclusion:
* Contiguous allocation — Best for simple, static files (e.g., CD-ROMs).
+ Linked allocation — Suitable for files with sequential access (e.g., logs).
+ Indexed allocation — Preferred in modern syst ,) + (e.g., UNIX, NTFS) for efficient random access and
flexibility.
--- page 6 ---
Explain the lightweight property of the thread and its types. Discuss the
b.   Multithreading models.
Explain the concepts “Cloud Operating System” and “Distributed   5+5
Operating System”.
Q6
a.
CO-
4;SO-
1,6;BL-2
CO-
2;SO-
1,6;BL-2
********** 6 **********

[Text in pictures on this page, read by OCR]
A thread is the smallest unit of CPU execution within a process.

Each thread represents an independent path of execution that shares the same:
¢ Code section
e Data section

e Files and resources of the parent process
But each thread has its own:

e Program counter (PC)
e Stack

e Registers

Feature Process Thread

Resource Allocation Requires separate memory, PCB, file Shares memory and resources with paren’
descriptors, etc. process
Inter-process communication (IPC) is Inter-thread communication is easy (share
complex memory)

Creation Time Slow (OS must allocate separate Fast (shares resources)
resources)

Context Switching Heavy Light and quick

Overhead High Low

Concept Key Idea

Thread Smallest CPU execution unit within a process

Lightweight Property Threads are faster to create, manage, and switch because they share
process resources

Thread Types User-Level, Kernel-Level, Hybrid

Multithreading Models Many-to-One, One-to-One, Many-to-Many

Feature Cloud Operating System Distributed Operating System c

Scope Manages cloud infrastructure (virtualized Manages a group of networked physical
data centers) computers

Resource Management Virtualized resources (VMs, containers) Physical resources (CPUs, disks, memory

Architecture Centralized or hierarchical (via cloud Decentralized (peer-to-peer coordination)
controllers)

Access Over the Internet via APIs/web Via network, but acts as a unified local

system
Goal Deliver on-demand cloud services Provide transparency and resource sharin,
Examples OpenStack, AWS, Azure, CloudStack Amoeba, Mach, MOSIX, LOCUS

User Perspective “Service platform” (virtual < \ 3s) “Single system image” (logical access)
--- page 7 ---
Explain Deadlock in “Diner's Philosopher’s Problem with all 3 cases
and their solutions.
10
b.
Q7   10
CO-   a.
2;SO-
1,6;BL-1   Define the term “Critical Section”. Explain the implementation of
Peterson’s solution in process synchronization.
CO-
3;SO-
1,6;BL-2
********** 7 **********

[Text in pictures on this page, read by OCR]
¢ Three Cases of the Dining Philosophers Problem

() Case 1: Deadlock
¢ All philosophers pick up the left fork first.
e Each philosopher is waiting for the right fork, which is held by their neighbor.

e Outcome: Circular wait — deadlock.

Solution:
e Introduce resource hierarchy:
« Number the forks from 1 to 5.
« Philosophers pick lower-numbered fork first, then higher-numbered.
e One philosopher (e.g., last one) picks in reverse order.
¢ This breaks circular wait, preventing deadlock.

© Case 2: Starvation
« Even without deadlock, some philosophers may never get both forks.
« Occurs if others continuously pick forks first.
« Outcome: A philosopher may wait indefinitely — starvation.
Solution:
e Use semaphores or mutexes with fairness:
« Each philosopher waits in queue if forks unavailable.
« Prevents a philosopher from being indefinitely blocked.
e Example: Monitor solution using a state array ( THINKING , HUNGRY, EATING ) and condition

variables.

(©) Case 3: No Deadlock / No Starvation

e Philosophers alternate picking forks carefully.
e Use a semaphore for each fork:
e Aphilosopher can pick both forks only if both are available.
e Or limit maximum philosophers at table:
e lIfn=5, allow at most 4 philosophers to try eating at once.
e Prevents circular wait — no deadlock.

{. This is considered the safe solution.
--- page 8 ---
int turn;
bool flag[2] = {false, false};
flag[0] = true;   // P0 wants to enter critical section
turn = 1;   // Give priority to P1
while (flag[1] && turn == 1)
;   // Busy wait
// Critical Section
... (access shared resource) ...
flag[0] = false;   // Exit critical section
flag[1] = true;   // P1 wants to enter critical section
turn = 0;   // Give priority to P0
while (flag[0] && turn == 0)
;   // Busy wait
b.   10
// Critical Section
... (access shared resource) ...
flag[1] = false;   // Exit critical section
Discuss the paging model in memory management. Explain Paging
hardware with the TLB mechanism. List the merits and demerits of the
Paging model.
********** 8 **********

[Text in pictures on this page, read by OCR]
¢ Properties of Critical Section

Any solution for critical sections must satisfy three requirements:

Property Description
Mutual Exclusion Only one process can be in the critical section at a time.
Progress If no process is in the critical section and some want to enter, one of them must

be allowed to enter.

Bounded Waiting / Fairness Every process waiting to enter the critical section will eventually be allowed in (no
starvation).

¢ Paging Hardware

The CPU uses paging hardware to translate logical addresses into physical addresses efficiently.

Components:
1. Page Table Base Register (PTBR):
Holds the starting address of the page table in memory.
2. Page Table:
Maps page numbers to frame numbers.
3. Memory Management Unit (MMU):
« Performs the actual address translation.
« Input: Logical address (p, d)
+ Output: Physical address (f, d)

¢ Address Translation Process

1. CPU generates a logical address (p, d) . NY
2. MMU uses page number (p) to index the page table.
--- page 9 ---
¢ Translation Lookaside Buffer (TLB)
¢ LB is a special fast cache in MMU that stores recent page number — frame number mappings.
How it works:

1. CPU generates logical address (p, d) .
2. MMU checks TLB first:
¢ TLB hit: Frame number f found — directly access memory.
¢ TLB miss: Access page table in memory — update TLB.
3. Combines frame number with offset to access physical memory.

TLB Hit Ratio affects performance:

¢ High hit ratio + faster memory access.
« Low hit ratio + more page table lookups.

Merits Explanation

Eliminates External Fragmentation Pages can be mapped anywhere in physical memory.
Simplifies Memory Allocation Fixed-size pages and frames make allocation easy.
Efficient Use of Memory Only required pages need to be loaded into memory.
Supports Virtual Memory Paging works well with demand paging for large processes.

¢ Demerits of Paging

Demerits Explanation

Internal Fragmentation Last page may not completely fill a frame.

Page Table Overhead Each process requires its own page table + memory consumption.

Slower Memory Access Extra memory access needed for page table lookup (mitigated by TLB).
; ov

Complexity Requires 1...dware support for MMU and TLB.

FIC QF OH ar
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 5ee21ef853f2

- Departments: AI and Data Science, Artificial Intelligence, Computer Engineering, Data Science
- Programmes: BTech AI 7012, BTech AIDS 7056, BTech CSE DS 7057, MBATech AI 7051, MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_AIDS_7056/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf` (+4 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: ocr (22 pages), mean OCR confidence 86.6
- 12 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS

SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MBA Tech (AD/MBA Tech (Comp)
Year: II / III / V/Semester I1/Semester IX/Semester V(Exam Year: 2025-2026)

Subject: Operating Systems
Date: 28 Nov 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)

Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)

Instructions:
1. This question paper contains 22 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. | is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. Inall 5 questions to be attempted.
7. Assume Suitable data if necessary.

1|A | What do you mean by Dual mode Operation in OS? Explain with suitable 5

diagram?
Definition (2 mark)
Explanation (2 marks)
Diagram (1 Mark)

Dual Mode Operation is a feature of modern operating systems that allows the
CPU to operate in two distinct modes — User Mode and Kernel (Supervisor)
Mode — to ensure system security and stability. It prevents user programs

from directly accessing critical system resources.

e User Mode:
o Used to execute user applications.
o Access to hardware and system resources is restricted.

o System calls are used to request OS services.

e Kernel Mode:
o Used by the operating syst
o Has unrestricted access to
o Switching from user mo
interrupts or system calls.

em to execute privileged instructions.
hardware and system memory.
de to kernel mode occurs through

ser process
user mode
user process executing calls system call return from system call (mode bit = 1)
ah. J
— + 7
kernel EP Se res ;
| / kernel mode
(mode bit = 0)

| execute system call

ernel, 1 = user) determines the current

The mode bit in the CPU (usually 0=k
mode.

operating

RAKE KERR 7 Te RE EE
--- page 2 ---
When an interrupt or system call occurs

when control returns to the use:
Advantages / Purpose

¢ Protects OS and hardware from

¢ Maintains system stability and
¢ Ensures controlled access to re.

, the mode bit switches to kernel mode;

t process, it switches back to user mode.

faulty or malicious user programs.
security.

sources through system calls only.

B | A student writes the following Produc

semaphore full = 0, empty = N, mutex

Producer() {
while (true) {
produce_item(x);
wait(full);
wait(mutex);
insert(x);
signal(mutex);

>

signal(empty);
}
}

Consumer() {
while (true) {
wait(empty);
wait(mutex);
remove(x);
signal(mutex);
signal(full);
consume_item(x);

}

Identify the mistakes in semap)

er-Consumer code:

=1;

hore usage and correct the code.

Explanation: 1 mark
Corrected code : 4 marks

Consumer:

* The Producer should wait on em
inserting an item, then signal full (i

© The Consumer should wali

pty (wait for empty slot) before
indicate one more full slot).

ton full (wait for an item) before removing,

then signal empty (indicate one more empty slot).

semaphore full = 0, empty = N, mutex = |;

Producer() {
while (true) {
produce_item(x);
wait(empty);
Wwait(mutex);

// wait for an empty slot

REREEK EEE 2 FFRRERE EE
--- page 3 ---
insert(x);
signal(mutex);
signal(full); _// signal that a new item is available
}
}

Consumer() {

while (true) {
wait(full); // wait for an available item
wait(mutex);
remove(x);
signal(mutex);
signal(empty); _// signal that a slot is now free
consume_item(x);

}

C | What is deadlock prevention? Discuss any two strategies used for preventing
deadlocks in an operating system.

Deadlock Prevention 1 Mark
Strategy 2 Mark each (4 Marks)

Deadlock prevention is a proactive method of ensuring that the system is
designed in such a way that at least one of the necessary conditions for

deadlock can never occur.

The four necessary conditions for deadlock are:

1. Mutual Exclusion
2. Hold and Wait

3. No Preemption
4, Circular Wait

Deadlock prevention works by denying or controlling these conditions.

Invalidate one of the four necessary conditions for deadlock:
= Mutual Exclusion — not required for sharable resources (e.g., read-only

files); must hold for non-sharable resources
= Hold and Wait — must guarantee that whenever a process requests a
resource, it does not hold any other resources
* Require process to request and be allocated all its resources
before it begins execution, or allow process to request resources
only when the process has none allocated to it.
+ Low resource utilization; starvation possible

« No Preemption:
at is holding some resources requests another

* Ifa process thi
resource that cannot be immediately allocated to it, then all

resources currently being held are released
« Preempted resources are ‘added to the list of resources for which

the process is waiting
* Process will be restarted only when it can regain its old

resources, as well as the new ones that it is requesting
= Circular Wait:

--- page 4 ---
Impose a total ordering of all resource types, and require that

each process requests resources in an increasing order of
enumeration

D | Compare blocking, non-blocking,

explaining how each works in practic:
differences,

and asynchronous I/O operations by
, and provide examples to illustrate the

Each operation 1 Mark (3 Marks)
Example 2 Marks

Blocking I/O: Process suspended until I/O completed; easy to use and
understand; sufficient for simple sequential operations

Nonblocking I/O: Returns immediately with available data; implemented via
multi-threading; useful for user interfaces and buffered 1/0; uses select() to
check data availability

Asynchronous I/O: Process continues execution while I/O executes; difficult

to use but efficient; I/O subsystem signals process upon completion

Examples: Blocking for simple file reads, nonblocking for network servers
handling multiple connectio

ms, asynchronous for high-performance database
operations

2|A | Explain the Dining Philosophers problem and critically analyze the reasons

why semaphore-based implementations may result in deadlock or starvation.

Propose and justify a monitor-based solution that addresses these issues.

10

Description: 2 marks

Why semaphore solution Fail: 2 marks
Monitor solution: 6 marks

Description:

5 philosophers’ sit at a round table with a bowl of rice in the middle,
They spend their lives alternating thinking and eating.
They do not interact with their neighbors.

Occasionally try to pick up 2 chopsticks (one at a time) to eat from bowl

© Need both to eat, then release both when done

Why semaphore solution Fail:
e Although this solution
simultaneously,

a deadlock.

Suppose that all five philosophers become hungry at the same time and
each grab their left chopstick. All the elements of chopstick will now
be equal to 0. When each philosopher tries to grab their right chopstick,
they will be delayed forever

guarantees that no two neighbors are eating
it nevertheless must be rejected because it could create

Monitor solution:
monitor DiningPhilosophers
{

enum ( THINKING, HUNGRY, EATING)
state [5] ;

condition self [5];
void pickup (int i) {
state[i] = HUNGRY;

HREREKEK KK Q ReeKKA KEES
--- page 5 ---
test(i);
if (state[i] != EATING)
self[i].wait;

}

void putdown (int i) {
state[i] = THINKING;
// test left and right neighbors
test((i + 4) % 5);
test((i + 1) % 5);

void test (int i) {
if ((state[(i + 4) % 5] != EATING) &&
(state[i] == HUNGRY) &&
(state[(i + 1) % 5] != EATING) ) {
state[i] = EATING ;
self[i].signal () ;
}

}
sii iciiek SET ;
ae = THINKING; Dining Philasopher p 7 kali ag
} [st Cot RX / i

Diana Philosophen. putdo nC)’

B | Consider the following processes with their an‘val times, burst times, and | 10 | ~
priorities.

Process Arrival Time BurstTime Priority

Pl 0 10 2
P2 1 4 1
P3 3 U 3
P4 4 6 2
P5 6 3) 0

Considering pre-emptive priority scheduling algorithm (lower priority
numbers indicate higher priority), calculate the average turnaround
time and average waiting time for the given batch of processes.

ii. Considering round-robin scheduling algorithm (with time quantum =
4), calculate the average turnaround time and average waiting time for

the given batch of processes.

i

KKK KKREK 5 oe KE KE
--- page 6 ---
5 att

(GC =2 marks, Avg. TAT = 1.5 marks, Avg. WT = 1.5 marks)

(GC =2 marks, Avg. TAT = 1.5 marks, Avg. WT = 1.5 marks)

3 | A | Consider the following snapshot of a system running 5 processes:

Process | Allocation Max Available
A B CIA B CiA B

Pl 0 il 0 7) 5 3/3 3

P2 2 0 0 3 2 2

P3 3 0 2 9 0 y

P4 2 1 1 2 2 2

P5 0 0 2 4 3 3

RRKKEKAR KK 6 HKRKKERKEK
--- page 7 ---
Answer the following: -
i. How many resources of type A, B, C are there?
ii. Calculate the need matrix?
iii. Determine if the system is safe or not.
iv. What will happen if the resource request (1, 0, 0) for process P1 arrive,

can the system accept this request immediately?

Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks

Safe Sequence 4 Marks

Additional Request 3 Marks

Total Resources = Available + Allocation

ABC
105 7

Need Matrix = Max — Allocation

Process Need Matrix

A B
Cc
Pl 7 4 3
| P2 [1 2 2]
P3 6 0 0
[ P4 [0 1 1]
P5 4 3 1

Finding out system is safe or not. And if safe then the sequence of process

execution.
Check if Need matrix <= Available

Process P2 need ca be full filled

New Available = Available ~ Need [P2]

ABC

2 1 «0

After P2 complete, Available = New Available + Max[P2]
ABC

Sh wok 2

Next Process P4 need ca be full filled

New Available = Available — Need [P4]

ABC

Sy 2) ih

After P4 complete, Available = New Available + Max[P4]
ABC

7 4 3

Next Process P5 need ca be full filled
New Available = Available — Need [P5]

KEKE ERERE 7 HHKKREKKEKE
--- page 8 ---
ABC
3 ey
After P5 complete, Available = New Available + Max[P5]
ABC
7 4 °5

Next Process P1 need ca be full filled

New Available = Available — Need [P1]

ABC

0 20572

After P1 complete, Available = New Available + Max[P1]
ABC

7 5 5

Next Process P3 need ca be full filled

New Available = Available — Need [P3]

ABC

1l- S235

After P3 complete, Available = New Available + Max[P3]
ABC

10 5 7

If Available == Total Resources.

Then the system is in safe state and one of the sequences of the process
execution will be

P2 -> P4 -> P5 -> Pl -> P3

Showing the request of P1 (1,0,0) is acceptable or not.
In the provided available recourses that is

ABC

3 3 2

If we grant P1 (1,0,0) then new available will be
ABC

2535 2

With these available resources still, we can proceed with the safe sequences of
the all the process. That’s why we can grant P1 request immediately.

Explain the concept of paging and its purpose in memory management. With
the help of a neat diagram, describe how paging hardware translates a logical

address into a physical address. How the Translation Lookaside Buffer (TLB)
can enhances the performance of paging.

10

Marks Distribution:

Explanation of paging and need — 4 Marks
Paging hardware representation — 4 Marks
Role of TLB in paging — 2 Marks

Definition:

Paging is a memory management technique in which the logical (virtual)
memory of a process is divided into fixed-size blocks called pages, and the
physical memory (RAM) is divided into blocks of the same size called frames.

KKKKKEEERE 8 REEKRERKERE
--- page 9 ---
When a program is executed, its pages are loaded into available frames in main
memory, not necessarily in a contiguous manner.

Need for Paging:

1. Eliminates External Fragmentation:
Since pages and frames are of fixed size, there are no variable-sized
memory holes.

2. Efficient Memory Utilization:

Allows non-contiguous memory allocation — unuse'
processes are minimized.

3. Simplifies Memory Management:
The operating system can manage me
complex variable partitions.

4. Supports Virtual Memory:
Enables programs larger th

only required pages.

d gaps between
mory using page tables rather than

an physical memory to execute by loading

frame @
logical address 0x000
cpu als = frame f
| p => Oxfttt
— t t frame g
ae physical memory

page table
Role of Translation Lookaside Buffer (2 Marks)
« Every memory access in a paging system requires two memory

references:
o One to access the page table (to find the frame number).

o Another to access the actual data in memory.
e This doubles the access time.
To solve this, a Translation Lookaside Buffer (TLB) is used.

TLB:
e A special high-speed cache that stores recently used page table entries
(page—frame mappings).
« When a logical address is generated:
o Ifthe page number is found in the TLB (TLB hit), the frame
number is retrieved instantly.
o Ifnot found (TLB miss), the page table is accessed and the

TLB is updated.

4| A | Operating systems provide an environment for execution of programs and,
offers services to programs and users. Justify the statement by explaining the
operating system services with suitable diagram?

Justification (3 Marks)

HEEKKKREKE Q AK ERE REE
--- page 10 ---
Operating System Services any five (5 Marks)
Diagram (2 Marks)

An Operating System (OS) serves as an essential layer between the hardware
and the user/programs

» ensuring efficient, reliable, and convenient execution
of

applications.
ere multiple programs can run
ith hardware safely.

It provides an execution environment wh
concurrently, share resources, and interact w

The OS not only controls hardware but also deli
program execution and enhance

Thus, it can be viewed as both a resource manager and

vers services that simplify
user productivity.
a service provider.

Justification

Without the operating system, users would have to directly manage complex

hardware operations such as memory allocation, device communication, or
process synchronization.
The OS abstracts these complexities by offering well-defined services such as
program execution, file management, and interprocess communication,

By providing these services:

¢ The OS ensures convenie
handling hardware details.

e It ensures efficienc
allocated optimally.

¢ It ensures security and reliabili
protection mechanisms.

nce —— users can run programs without

Y — resources like CPU, memory, and I/O are

‘y — through error handling and

Hence, the OS creates a controlled, stable, and user-friendly environment for
both users and system programs.

Operating System Services (5 Marks)

1. Program Execution:
Loads, runs, and terminates programs. Manages process scheduling and
transitions.

2. VO

Operations:
Provides a uniform interface for input/output devices, abstracting
hardware details.

3. File System
Manages file creation, deletion,
secondary storage,

4. Inter-process
Enables process coordinatio
memory or message passing.

5. Error Detection

and Handling:
Monitors the system to detect and respond to hardware or software
€frors gracefully.

6. Resource

Dynamically allocates CPU time,
processes fairly.

Manipulation:
access control, and organization in

Communication (IPC):
n and data exchange through shared

Allocation:
memory, and I/O to competing

--- page 11 ---
7. Accounting:
Tracks system and re:
optimization.

source usage for performance monitoring and

8. Protection and Security:
Ensures data privacy and system integrity through controlled access and
authentication.

user and other system programs a
| Gul touch screen | command fine
i
user interfaces
L
system calls
7 ie OR Shh. Ae | eens ieee
execution \| operations Ed systems conmeunication {| allocation accounting }
=e 5
Ca j protection
| detection | | dans
services
operating system

; hardware

The OS provides a well-defined execution
complexity, managing concurrent activities,
and delivering reliable services.

Therefore, the statement is justified:
environment for execution of programs and

nvironment by hiding hardware
ensuring safe resource sharing,

“Operating Systems provide an
services to both programs and

users.”
nders 2069, 1212, 2296, 2800, 544, 1618,

A disk queue has requests on cyli
356, 1523. The disk head is currently positioned at cylinder 2150. The disk has

cylinders numbered from 0 to 4999.
Calculate the total head movement (in cylinders
requests using the following disk scheduling algorithms:
1. FCFS (First-Come-First-Served)
2. SCAN (Elevator Algorithm), assuming the h
towards the highest cylinder (4999).

3. C-SCAN (Circular SCAN), assuming the head is initially moving
towards the highest cylinder (4999).
Compare the performance of the three algorithm:
movement and discuss one major factor of comparison.

) required to service all

ead is initially moving

s based on their total head

Each algorithm 3 marks (9 marks)
Comparison 1 mark

--- page 12 ---
ae
gee
b ha
68
f
Mt +
é
Performance Comparison
ALGORITHM TOTAL MOVEMENT ‘CHARACTERISTICS
FCFS 8,285 Simple. fa'r, but hign seek time
SCAN 7,492 Fait, ptedictabve. moderate performance
C-SCAN, 9.917

More uniform wait tire higher movement

Performance Comparison: SCAN has the lowest head movement (7492

cylinders), making it the most efficient algorithm for this specific batch of

KEKE KEE 12 FRREKERERE
--- page 13 ---
requests and head position. FCFS performs better than C-SCAN, but SCAN is

the most efficient of the three.
Major Factor of Comparison: Uniformity of Wait Time
The major factor distinguishing SCAN and C-SCAN is the Uniformity of Wait

Time.
« SCAN: Causes a non-uniform wait ti
behind the reversing head (e.g., at cylinder 4900 after the head has just

left it going towards 0) will have to wait for the entire sweep to the
other end (0) and back, leading to a much longer latency than requests

near the ends.

» C-SCAN: Provides a more uniform wait t
requests in only one direction and immediatel,
start, C-SCAN ensures that a new request waits, at most, for the time it
takes the head to complete one full circular sweep, regardless of its
position on the disk. This predictability is highly valuable in high-

performance or heavy-load systems.

me. Requests that are waiting just

ime. By always servicing
y jumping back to the

5|A

Describe the concept of Message Passing by explaining its fundamental
primitives and addressing methods. Support your explanation with a neat

diagram of the general message format.

Message passing: 2 marks
Primitives: 3 marks
Addressing: 2 marks
Message format: 3 marks

Message Passing:

e@ When processes interact with one another, two fundamental

requirements must be satisfied: synchronization and communication.

e Processes need to be synchronized to enforce mutual exclusion;
cooperating processes may need to exchange information.

@ One approach to providing both of these functions is message passing.

e Message passing has the further advantage that it lends itself to
implementation in distributed systems as well as in shared-memory

multiprocessor and uniprocessor systems.

Primitives:

e We need to specify what happens to a process after it issues a send or
receive primitive.

e@ When a send primiti
possibilities: Either the
received, or it is not.

e Similarly, when a process issues a rece
possibilities:

1. Ifa message has previous
continues.
n either (a) the process is blocked until a

9. If there is no waiting message, the
message arrives, or (b) the process continues to execute, abandoning the

attempt to receive.
e Thus, both the sender and receiver can be blocking or nonblocking.

e Three combinations are common, although any particular system will
usually have only one or two combinations implemented:

ve is executed in a process, there are two
sending process is blocked until the message is

ive primitive, there are two

ly been sent, the message is received and execution

HEREKEEERE 13 KEKE EEK
--- page 14 ---
1. Blocking send, blocking receive: B.
until the message is delivered; thi
This combination allows for tight
2. Nonblocking send, blocking re:
the receiver is blocked until the
the most useful combination. It al
to a variety of destinations as qui
a message before it can do use
message arrives. An example is a
or resource to other processes.

3. Nonblocking send, nonblocking receive: Neither party is required to wait.

oth the sender and receiver are blocked
s is sometimes referred to as a rendezvous.
synchronization between processes.

ceive: Although the sender may continue on,
requested message arrives. This is probably
lows a process to send one or more messages
ckly as possible. A process that must receive
ful work needs to be blocked until such a
Server process that exists to provide a service

Addressing:

¢ The various schemes for sp

primitives fall into two cat
addressing.

© With direct addressing, the send primitive includes a specific identifier
of the destination process.

e The receive primitive can be
possibility is to require that the
process. Thus, the process must
a message is expected.

ecifying processes in send and receive
egories: direct addressing and indirect

handled in one of two ways. One
process explicitly designate a sending
know ahead of time from which process

¢ The other general approach is indirect addressing. In this case,
messages are not sent directly from sender to receiver, but rather are
sent to a shared data structure consisting of queues that can temporarily
hold messages.

e Such queues are generally referred to as mailboxes. Thus, for two
Processes to communicate, one Process sends a message to the
appropriate mailbox, and the other Process picks up the messages from
the mailbox.

Destination ID
Header Source ID
Control Information
Body | Message Contents

protection mechanisms, such as base and limit
registers, prevent illegal memory access. Illustrate your answer with an
example of process isolation. Consider six memory partitions of size 350 KB,
700 KB, 580 KB, 450 KB, and 300 KB in the same order. Considering

contiguous memory allocation, show how the first-fit, best-fit and worst-fit

algorithms will place the Processes of 360 KB, 600 KB, 425 KB, and 250 KB
(in order),

KEKE RK EK 14 RRKKAKEA ARE
--- page 15 ---
Marks Distribution:

Address protection mechanism 2 marks
Process isolation 2 marks

First Fit — 2 marks

Best Fit — 2 marks

Worst Fit — 2 marks

Hardware address protection is a mechanism in an operating system that
ensures each process accesses only its allocated memory space. This protection
is achieved through special hardware registers — primarily the base register
and limit register — which define the valid address range for each process.

Base Register: Holds the starting physical address of the process’s memory
space.

Limit Register: Specifies the size or maximum offset of the process’s
addressable memory range.

When a process generates an address (logical address), the hardware adds the

base value to it to get the physical address.

Before accessing memory, the hardware checks whether the logical address is
less than the limit. If it exceeds, the access is blocked, and a trap or exception

is raised.
base base + limit

ES yes
<

no

CPU address

trap to operating system
illegal addressing error memory

If 0 < Logical Address < Limit > Access Allowed
Else > Trap (Illegal Access)

Process Isolation Example
Consider two processes — P1 and P2.

P1 has Base = 1000 and Limit = 500, so it can access physical addresses 1000-
1499.

P2 has Base = 2000 and Limit = 400, so it can access addresses 2000-2399.

If Pl tries to access memory location 1800, the hardware check will detect it
is beyond its limit (1499), triggering a trap — thereby preventing illegal access
to P2’s memory region.

--- page 16 ---
REKEKE KEKE 16 KAKKKEEKER
--- page 17 ---
10

6!A| I. _ Illustrate and describe, using a suitable diagram, how a process
transitions through various states during its execution.
Il. Identify and explain the conditions under which each state transition

takes place.
Ul. Apply your understanding of process scheduling to explain two

scenarios in which a process may transition from the Running state to
the Ready state before completing its CPU burst.

I. 4 marks
I. 3 Marks
Iii. 3 Marks

Solution: i. State Transition diagram - (4 marks)

admitted

interrupt

1/0 or event wait

i. Transitions occurrence: (3 marks)

e New—Ready: admitted by long-term scheduler.

« Ready—Running: selected by CPU scheduler.

e Running— Waiting: I/O request, page fault, lock wait.

HERRERA 7 FRR EEE EE
--- page 18 ---
Waiting—Ready: I/O completes, event/interrupt occurs.
Running—Ready: preempted by higher priority or time slice expiry.
¢ Running—Terminated: process exit/abort.

tii. As stated in the Lifecycle diagram, a process may move from the
Running state to the Ready state before completing its CPU burst due
to pre-emption (I/O or event wait) or priority.

-based scheduling events
(interrupts). - (3 marks)

B | A system uses 4 frames for storin:
that all the page frames are initial]
given below:

2,3,4,5,3,2,6,7,3,2,3,4,8,7,4,3,2,3,4,7

§ process pages in main memory. Assume
y empty. Consider the page reference string

I. Simulate the page replacement using the FIFO algorithm.
I. Simulate the page replacement using the LRU algorithm.
Il. Simulate the page replacement using the Optimal algorithm.
IV. For each algorithm, calculate the total number of page faults.
V.

Based on your results, which algorithm performs best and why?

Marks Distribution:

2 marks each on every point of questions i.e. 5 * 2 = 10 marks
a)

FIFO
2 3 4 5 3 2 6 7 3 2
2 2 2 2 2b 3 (2 G 6 6 6
3 3 3 3 3 ee 7 ete (P| 7
4 4 4 4 4 4 3 3
[5] 5 5 5 5 5 2
3 4 8 z 4 3 2 3 4 7
6 4] [4] [a4 44 [al [2 BP a Ee
7 7 8 8 8} | 8 8 ei}
3 3 3 7 7 7 7 7 7 7
2 2 2 2 2 3 3 3 3 3
Total Page Fault: 14
b)

REREKKRERE ig RRERERE RAK
--- page 19 ---
LRU

2 3 4 5 3 2 6 7 3 2
2 102) 22) 32) 4) of tt 2 OR
of al {a} lal of 3] 3] 213) 3] 3] 0} 3} 11 8
ola (4 24 34 ole +e 36 36
ot sl tsi zal 3[_4] of 7] 17 27

3 4 8 7 4 3 2 3 4 7
| 2] 22] 3) of 7] 317 7 3{_ 7) 47] 57] oL7
g~al tlval 2{al 3[_3l 4[_s| ofl 1[3] OL 3] | 3) 4 3

4-7 yt] ofa 1 Cal 2Lal aL] ola] Lad 2 i

F F F F

Total Page Fault: 10

¢)
Optimal
2 3 4 5 3 2 6 7 3 2
2 2 4 C2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4
5 8 5 6 7 7 7
3 4 8 7 4 3 2 3 4 7
2 2 8 8 8 8 2 2 2 2
3) 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
_7 u 7 7 7 7 7 7 7 7
F F

Total Page Fault: 8

d) Total number of page faults:
FIFO:14, LRU:10, optimal: 8

e) Based on your results, which algorithm performs best and why?

Optimal minimizes page faults by always replacing the page that will not be

used for the longest time in the future. It uses future knowledge, making it
theoretical but ideal for benchmarking. LRU is better than FIFO because it
uses past usage patterns (replacing least recently used), while FIFO doesn’t

consider usage, just arrival order.

7A | What is resource allocation graph? Consider the following snapshot of a

system having 2 resources (RI having 1 instance and R2 having 2 instances)

and running 3 processes.

Process Allocation Request
RI R2 Ril R2
{Pi [1 0 [0 i |

HK KKKEKEKE 1O RK KE EEK
--- page 20 ---
P2 0 lei 0
[P3 [0 ela Oe]
Draw the resource allocation graph. Find if there is a deadlock or not? If there

is no deadlock then what will be the sequence of the process to get executed?

RAG description 3 marks
Draw RAG 4 marks

Safe Sequence 3 marks

i) What is resource allocation graph? [3 Marks]

© A useful tool in characterizing the allocation of resources to processes

is the resource allocation graph.

The resource allocation graph is a directed graph that depicts a state of

the system of resources and processes, with each process and each

resource represented by a node.

A graph edge directed from a process to a resource indicates a resource

that has been requested by the process but not yet granted.
Within a resource node, a dot is shown for each instance of that
resource.

Examples of resource types that may have multiple instances are VO

devices that are allocated by a resource management module in the Os.
A graph edge directed from a reusable resource node dot to a process

indicates a request that has been granted; that is, the process has been
assigned one unit of that resource.

Requests

. [ 7 |

‘ } Held b:

oe & ao? &

ie pa Py j
{a) Resource is requested (b) Resource is held

ii) Draw a resource allocation graph of the following table? [4 Marks]

--- page 21 ---
if there is a deadlock or not? If there is no deadlock then what will be
[3 Marks]

iii) Find
the sequence of the process to get executed?
There is no deadlock in the resource allocation graph.

The sequence of process to execute in safe sequence is

P3 -> Pl ->P2
Define a PCB. How can it help in enabling multi-tasking?
Definition 1 Mark

Explanation 4 marks

) is a data structure maintained by
al information about a

(1 mark)

Solution: A Process Control Block (PCB
the Operating System that contains all the essenti

process.

Multitasking means executing multiple processes seemingly at the same time

by rapidly switching the CPU between them.
Here’s how PCB makes that possible:

1. Context Saving:
a. When a running process is interrupted (e.g., due to time slice

expiry or I/O request),
the OS saves its current CPU state
PCB.
2. Context Restoration:
a. When the process is scheduled again,
state from its PCB.
The process resumes exactly where it left off.
3. Accurate Process Switching:
a. The PCB ensures that switching
switching) does not corrupt data or execution flow.

4. Tracking Multiple Processes:

(registers, PC, etc.) into its

the OS restores the saved

between processes (context

--- page 22 ---
a. Each process has its own PCB, so the OS can easily track,
suspend, resume, or terminate any process at any time.

(4 marks)

C | Summarize the main file attributes managed by a fi

le system and explain the | 5
common operations that can be performed on a file.

Key Attributes 2.5 marks
File Operations 2.5 marks

Key File attributes:

File attributes are pieces of information maintained by the file system about a
file and are typically kept in the directory structure on the disk.

Name: This is the onl
Identifier: This is au
file system.

Type: This is needed for s
Location: This is a
device.

Size: This records the current size of the file.

Protection: This controls who can perform operations such as reading,
writing, and executing the file.

Time, Date, and User Identification: Thi
security, and monitoring file usage.

y file information kept in human-readable form.
nique tag (a number) that identifies the file within the

ystems that support different types of files.

pointer that indicates the file's location on the storage

s data is maintained for protection,

Major File Operations:

The operating system
performed on files:

Create: This operation creates a new file.
Write: This operation writes data to
pointer location.

Read: This operation reads data from the fi
pointer location.

Delete: This operation deletes the file.
Open (Fj): This Operation involves searc
for the entry Fj and moving the content of that entry into memory.

Close (Fi): This operation moves the content of file entry Fi from memory
back to the directory structure on the disk.

Reposition (Seek): This Operation moves the read/write pointer within the
file.

Provides several major operations that can be

the file starting at the current write

le starting at the current read

hing the directory structure on disk

Truncate: This operation zeros the file length and keeps the attributes, but
discards the file's contents.

EREKEREEKK 22 RREEEKERHRE
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 5e1d7605a5b5

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_AIML_7053/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: mixed (22 pages), mean OCR confidence 39.8
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MBA Tech (AI)/MBA Tech (Comp)
Year: II / III / V/Semester III/Semester IX/Semester V(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 28 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 22 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1 A What do you mean by Dual mode Operation in OS? Explain with suitable 5
diagram?
Definition (2 mark)
Explanation (2 marks)
Diagram (1 Mark)
Dual Mode Operation is a feature of modern operating systems that allows the
CPU to operate in two distinct modes — User Mode and Kernel (Supervisor)
Mode — to ensure system security and stability. It prevents user programs
from directly accessing critical system resources.
• User Mode:
o Used to execute user applications.
o Access to hardware and system resources is restricted.
o System calls are used to request OS services.
• Kernel Mode:
o Used by the operating system to execute privileged instructions.
o Has unrestricted access to hardware and system memory.
o Switching from user mode to kernel mode occurs through
interrupts or system calls.
The mode bit in the CPU (usually 0 = kernel, 1 = user) determines the current
operating   mode.
********** 1 **********

[Text in pictures on this page, read by OCR]
user process

user mode
user process executing | calls system call | | return from system call (mode bit = 1)
\
st Z
t ra
trap return
Kemal mode bit = 0 mode bit = 1

\ kernel mode
execute system call (mode bit = 0)
--- page 2 ---
When an interrupt or system call occurs, the mode bit switches to kernel mode;
when control returns to the user process, it switches back to user mode.
Advantages / Purpose
•   Protects OS and hardware from faulty or malicious user programs.
• Maintains system stability and security.
• Ensures controlled access to resources through system calls only.
B A student writes the following Producer-Consumer code:   5
semaphore full = 0, empty = N, mutex = 1;
Producer() {
while (true) {
produce_item(x);
wait(full);
wait(mutex);
insert(x);
signal(mutex);
signal(empty);
}
}
Consumer() {
while (true) {
wait(empty);
wait(mutex);
remove(x);
signal(mutex);
signal(full);
consume_item(x);
}
}
Identify the mistakes in semaphore usage and correct the code.
Explanation: 1 mark
Corrected code : 4 marks
Semaphore wait/signal on full and empty are reversed in Producer and
Consumer:
• The Producer should wait on empty (wait for empty slot) before
inserting an item, then signal full (indicate one more full slot).
• The Consumer should wait on full (wait for an item) before removing,
then signal empty (indicate one more empty slot).
.
semaphore full = 0, empty = N, mutex = 1;
Producer() {
while (true) {
produce_item(x);
wait(empty);   // wait for an empty slot
wait(mutex);
********** 2 **********
--- page 3 ---
insert(x);
signal(mutex);
signal(full);   // signal that a new item is available
}
}
Consumer() {
while (true) {
wait(full);   // wait for an available item
wait(mutex);
remove(x);
signal(mutex);
signal(empty);   // signal that a slot is now free
consume_item(x);
}
}
C What is deadlock prevention? Discuss any two strategies used for preventing
deadlocks in an operating system.
Deadlock Prevention 1 Mark
Strategy 2 Mark each (4 Marks)
Deadlock prevention is a proactive method of ensuring that the system is
designed in such a way that at least one of the necessary conditions for
deadlock can never occur.
The four necessary conditions for deadlock are:
1. Mutual Exclusion
2. Hold and Wait
3. No Preemption
4. Circular Wait
Deadlock prevention works by denying or controlling these conditions.
Invalidate one of the four necessary conditions for deadlock:
▪ Mutual Exclusion – not required for sharable resources (e.g., read-only
files); must hold for non-sharable resources
▪ Hold and Wait – must guarantee that whenever a process requests a
resource, it does not hold any other resources
• Require process to request and be allocated all its resources
before it begins execution, or allow process to request resources
only when the process has none allocated to it.
• Low resource utilization; starvation possible
▪ No Preemption:
•   If a process that is holding some resources requests another
resource that cannot be immediately allocated to it, then all
resources currently being held are released
• Preempted resources are added to the list of resources for which
the process is waiting
•   Process will be restarted only when it can regain its old
resources, as well as the new ones that it is requesting
▪ Circular Wait:
********** 3 **********
--- page 4 ---
• Impose a total ordering of all resource types, and require that
each process requests resources in an increasing order of
enumeration
D Compare blocking, non-blocking, and asynchronous I/O operations by
explaining how each works in practice, and provide examples to illustrate the
differences.
Each operation 1 Mark (3 Marks)
Example 2 Marks
Blocking I/O: Process suspended until I/O completed; easy to use and
understand; sufficient for simple sequential operations
Nonblocking I/O: Returns immediately with available data; implemented via
multi-threading; useful for user interfaces and buffered I/O; uses select() to
check data availability
Asynchronous I/O: Process continues execution while I/O executes; difficult
to use but efficient; I/O subsystem signals process upon completion
Examples: Blocking for simple file reads, nonblocking for network servers
handling multiple connections, asynchronous for high-performance database
operations
2 A Explain the Dining Philosophers problem and critically analyze the reasons 10
why semaphore-based implementations may result in deadlock or starvation.
Propose and justify a monitor-based solution that addresses these issues.
Description: 2 marks
Why semaphore solution Fail: 2 marks
Monitor solution: 6 marks
Description:
● 5 philosophers’ sit at a round table with a bowl of rice in the middle.
● They spend their lives alternating thinking and eating.
● They do not interact with their neighbors.
● Occasionally try to pick up 2 chopsticks (one at a time) to eat from bowl
.
● Need both to eat, then release both when done
Why semaphore solution Fail:
● Although this solution guarantees that no two neighbors are eating
simultaneously, it nevertheless must be rejected because it could create
a deadlock.
● Suppose that all five philosophers become hungry at the same time and
each grab their left chopstick. All the elements of chopstick will now
be equal to 0. When each philosopher tries to grab their right chopstick,
they will be delayed forever
Monitor solution:
monitor DiningPhilosophers
{
enum ( THINKING, HUNGRY, EATING)
state [5] ;
condition self [5];
void pickup (int i) {
state[i] = HUNGRY;
********** 4 **********
--- page 5 ---
test(i);
if (state[i] != EATING)
self[i].wait;
}
void putdown (int i) {
state[i] = THINKING;
// test left and right neighbors
test((i + 4) % 5);
test((i + 1) % 5);
}
void test (int i) {
if ((state[(i + 4) % 5] != EATING) &&
(state[i] == HUNGRY) &&
(state[(i + 1) % 5] != EATING) ) {
state[i] = EATING ;
self[i].signal () ;
}
}
initialization_code() {
for (int i = 0; i < 5; i++)
state[i] = THINKING;
}
}
B Consider the following processes with their arrival times, burst times, and 10
priorities.
Process   Arrival Time   Burst Time   Priority
P1   0   10   2
P2   1   4   1
P3   3   7   3
P4   4   6   2
P5   6   5   0
i. Considering pre-emptive priority scheduling algorithm (lower priority
numbers indicate higher priority), calculate the average turnaround
time and average waiting time for the given batch of processes.
ii. Considering round-robin scheduling algorithm (with time quantum =
4), calculate the average turnaround time and average waiting time for
the given batch of processes.
********** 5 **********
--- page 6 ---
(GC = 2 marks, Avg. TAT = 1.5 marks, Avg. WT = 1.5 marks)
(GC = 2 marks, Avg. TAT = 1.5 marks, Avg. WT = 1.5 marks)
3 A Consider the following snapshot of a system running 5 processes:
Process Allocation   Max   Available
A   B   C A   B   C A   B   C
P1   0   1   0   7   5   3   3   3   2
P2   2   0   0   3   2   2
P3   3   0   2   9   0   2
P4   2   1   1   2   2   2
P5   0   0   2   4   3   3
********** 6 **********
--- page 7 ---
Answer the following: -
i. How many resources of type A, B, C are there?
ii.   Calculate the need matrix?
iii.   Determine if the system is safe or not.
iv.   What will happen if the resource request (1, 0, 0) for process P1 arrive,
can the system accept this request immediately?
Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks
Safe Sequence 3 Marks
Additional Request 3 Marks
Total Resources = Available + Allocation
A B C
10 5 7
Need Matrix = Max – Allocation
Process Need Matrix
A   B
C
P1   7   4   3
P2   1   2   2
P3   6   0   0
P4   0   1   1
P5   4   3   1
Finding out system is safe or not. And if safe then the sequence of process
execution.
Check if Need matrix <= Available
Process P2 need ca be full filled
New Available = Available – Need [P2]
A B C
2 1 0
After P2 complete, Available = New Available + Max[P2]
A B C
5 3 2
Next Process P4 need ca be full filled
New Available = Available – Need [P4]
A B C
5 2 1
After P4 complete, Available = New Available + Max[P4]
A B C
7 4 3
Next Process P5 need ca be full filled
New Available = Available – Need [P5]
********** 7 **********
--- page 8 ---
A B C
3 1 2
After P5 complete, Available = New Available + Max[P5]
A B C
7 4 5
Next Process P1 need ca be full filled
New Available = Available – Need [P1]
A B C
0 0 2
After P1 complete, Available = New Available + Max[P1]
A B C
7 5 5
Next Process P3 need ca be full filled
New Available = Available – Need [P3]
A B C
1 5 5
After P3 complete, Available = New Available + Max[P3]
A B C
10 5 7
If Available == Total Resources.
Then the system is in safe state and one of the sequences of the process
execution will be
P2 -> P4 -> P5 -> P1 -> P3
Showing the request of P1 (1,0,0) is acceptable or not.
In the provided available recourses that is
A B C
3 3 2
If we grant P1 (1,0,0) then new available will be
A B C
2 3 2
With these available resources still, we can proceed with the safe sequences of
the all the process. That’s why we can grant P1 request immediately.
B Explain the concept of paging and its purpose in memory management. With 10
the help of a neat diagram, describe how paging hardware translates a logical
address into a physical address. How the Translation Lookaside Buffer (TLB)
can enhances the performance of paging.
Marks Distribution:
Explanation of paging and need – 4 Marks
Paging hardware representation – 4 Marks
Role of TLB in paging – 2 Marks
Definition:
Paging is a memory management technique in which the logical (virtual)
memory of a process is divided into fixed-size blocks called pages, and the
physical memory (RAM) is divided into blocks of the same size called frames.
********** 8 **********
--- page 9 ---
When a program is executed, its pages are loaded into available frames in main
memory, not necessarily in a contiguous manner.
Need for Paging:
1. Eliminates External Fragmentation:
Since pages and frames are of fixed size, there are no variable-sized
memory holes.
2. Efficient Memory Utilization:
Allows non-contiguous memory allocation — unused gaps between
processes are minimized.
3. Simplifies Memory Management:
The operating system can manage memory using page tables rather than
complex variable partitions.
4. Supports Virtual Memory:
Enables programs larger than physical memory to execute by loading
only required pages.
Role of Translation Lookaside Buffer (2 Marks)
• Every memory access in a paging system requires two memory
references:
o One to access the page table (to find the frame number).
o Another to access the actual data in memory.
• This doubles the access time.
To solve this, a Translation Lookaside Buffer (TLB) is used.
TLB:
• A special high-speed cache that stores recently used page table entries
(page–frame mappings).
• When a logical address is generated:
o   If the page number is found in the TLB (TLB hit), the frame
number is retrieved instantly.
o   If not found (TLB miss), the page table is accessed and the
TLB is updated.
4 A Operating systems provide an environment for execution of programs and,
offers services to programs and users. Justify the statement by explaining the
operating system services with suitable diagram?
Justification (3 Marks)
********** 9 **********

[Text in pictures on this page, read by OCR]
frame e

logical address physical address 0x000
frame f
cpu slp | a |
p — Oxfff
f frame g

physical memory

page table
--- page 10 ---
Operating System Services any five (5 Marks)
Diagram (2 Marks)
An Operating System (OS) serves as an essential layer between the hardware
and the user/programs, ensuring efficient, reliable, and convenient execution
of   applications.
It provides an execution environment where multiple programs can run
concurrently, share resources, and interact with hardware safely.
The OS not only controls hardware but also delivers services that simplify
program   execution   and   enhance   user   productivity.
Thus, it can be viewed as both a resource manager and a service provider.
Justification
Without the operating system, users would have to directly manage complex
hardware operations such as memory allocation, device communication, or
process   synchronization.
The OS abstracts these complexities by offering well-defined services such as
program execution, file management, and interprocess communication.
By providing these services:
• The OS ensures convenience — users can run programs without
handling hardware details.
•   It ensures efficiency — resources like CPU, memory, and I/O are
allocated optimally.
•   It ensures security and reliability — through error handling and
protection mechanisms.
Hence, the OS creates a controlled, stable, and user-friendly environment for
both users and system programs.
Operating System Services (5 Marks)
1. Program   Execution:
Loads, runs, and terminates programs. Manages process scheduling and
transitions.
2. I/O   Operations:
Provides a uniform interface for input/output devices, abstracting
hardware details.
3. File   System   Manipulation:
Manages file creation, deletion, access control, and organization in
secondary storage.
4. Inter-process   Communication   (IPC):
Enables process coordination and data exchange through shared
memory or message passing.
5. Error   Detection   and   Handling:
Monitors the system to detect and respond to hardware or software
errors gracefully.
6. Resource   Allocation:
Dynamically allocates CPU time, memory, and I/O to competing
processes fairly.
********** 10 **********
--- page 11 ---
7. Accounting:
Tracks system and resource usage for performance monitoring and
optimization.
8. Protection   and   Security:
Ensures data privacy and system integrity through controlled access and
authentication.
The OS provides a well-defined execution environment by hiding hardware
complexity, managing concurrent activities, ensuring safe resource sharing,
and delivering reliable services.
Therefore, the statement is justified: “Operating Systems provide an
environment for execution of programs and services to both programs and
users.”
B A disk queue has requests on cylinders 2069, 1212, 2296, 2800, 544, 1618,
356, 1523. The disk head is currently positioned at cylinder 2150. The disk has
cylinders numbered from 0 to 4999.
Calculate the total head movement (in cylinders) required to service all
requests using the following disk scheduling algorithms:
1. FCFS (First-Come-First-Served)
2. SCAN (Elevator Algorithm), assuming the head is initially moving
towards the highest cylinder (4999).
3. C-SCAN (Circular SCAN), assuming the head is initially moving
towards the highest cylinder (4999).
Compare the performance of the three algorithms based on their total head
movement and discuss one major factor of comparison.
Each algorithm 3 marks (9 marks)
Comparison 1 mark
********** 11 **********

[Text in pictures on this page, read by OCR]
user and other system programs

GUI touch screen | command line

user interfaces

system calls

program vO file a resource
communication

. A a accounting
execution operations systems allocation

protection
and
security

error
detection
services

operating system

hardware
--- page 12 ---
Performance Comparison: SCAN has the lowest head movement (7492
cylinders), making it the most efficient algorithm for this specific batch of
********** 12 **********

[Text in pictures on this page, read by OCR]
Performance Comparison

ALGORITHM TOTAL MOVEMENT CHARACTERISTICS
FCFS 8,285 Simple, fair, but high seek time
SCAN 7,492 Fair, predictable, moderate performance

C-SCAN 9,917 More uniform wait time, higher movement
--- page 13 ---
requests and head position. FCFS performs better than C-SCAN, but SCAN is
the most efficient of the three.
Major Factor of Comparison: Uniformity of Wait Time
The major factor distinguishing SCAN and C-SCAN is the Uniformity of Wait
Time.
• SCAN: Causes a non-uniform wait time. Requests that are waiting just
behind the reversing head (e.g., at cylinder 4900 after the head has just
left it going towards 0) will have to wait for the entire sweep to the
other end (0) and back, leading to a much longer latency than requests
near the ends.
• C-SCAN: Provides a more uniform wait time. By always servicing
requests in only one direction and immediately jumping back to the
start, C-SCAN ensures that a new request waits, at most, for the time it
takes the head to complete one full circular sweep, regardless of its
position on the disk. This predictability is highly valuable in high-
performance or heavy-load systems.
5 A Describe the concept of Message Passing by explaining its fundamental
primitives and addressing methods. Support your explanation with a neat
diagram of the general message format.
Message passing: 2 marks
Primitives: 3 marks
Addressing: 2 marks
Message format: 3 marks
Message Passing:
● When processes interact with one another, two fundamental
requirements must be satisfied: synchronization and communication.
● Processes need to be synchronized to enforce mutual exclusion;
cooperating processes may need to exchange information.
● One approach to providing both of these functions is message passing.
● Message passing has the further advantage that it lends itself to
implementation in distributed systems as well as in shared-memory
multiprocessor and uniprocessor systems.
Primitives:
● We need to specify what happens to a process after it issues a send or
receive primitive.
● When a send primitive is executed in a process, there are two
possibilities: Either the sending process is blocked until the message is
received, or it is not.
● Similarly, when a process issues a receive primitive, there are two
possibilities:
1. If a message has previously been sent, the message is received and execution
continues.
2. If there is no waiting message, then either (a) the process is blocked until a
message arrives, or (b) the process continues to execute, abandoning the
attempt to receive.
● Thus, both the sender and receiver can be blocking or nonblocking.
● Three combinations are common, although any particular system will
usually have only one or two combinations implemented:
********** 13 **********
--- page 14 ---
1. Blocking send, blocking receive: Both the sender and receiver are blocked
until the message is delivered; this is sometimes referred to as a rendezvous.
This combination allows for tight synchronization between processes.
2. Nonblocking send, blocking receive: Although the sender may continue on,
the receiver is blocked until the requested message arrives. This is probably
the most useful combination. It allows a process to send one or more messages
to a variety of destinations as quickly as possible. A process that must receive
a message before it can do useful work needs to be blocked until such a
message arrives. An example is a server process that exists to provide a service
or resource to other processes.
3. Nonblocking send, nonblocking receive: Neither party is required to wait.
Addressing:
● The various schemes for specifying processes in send and receive
primitives fall into two categories: direct addressing and indirect
addressing.
● With direct addressing, the send primitive includes a specific identifier
of the destination process.
● The receive primitive can be handled in one of two ways. One
possibility is to require that the process explicitly designate a sending
process. Thus, the process must know ahead of time from which process
a message is expected.
● The other general approach is indirect addressing. In this case,
messages are not sent directly from sender to receiver, but rather are
sent to a shared data structure consisting of queues that can temporarily
hold messages.
● Such queues are generally referred to as mailboxes. Thus, for two
processes to communicate, one process sends a message to the
appropriate mailbox, and the other process picks up the messages from
the mailbox.
B Analyze how hardware address protection mechanisms, such as base and limit
registers, prevent illegal memory access. Illustrate your answer with an
example of process isolation. Consider six memory partitions of size 350 KB,
700 KB, 580 KB, 450 KB, and 300 KB in the same order. Considering
contiguous memory allocation, show how the first-fit, best-fit and worst-fit
algorithms will place the processes of 360 KB, 600 KB, 425 KB, and 250 KB
(in order).
********** 14 **********

[Text in pictures on this page, read by OCR]
Message Type
Destination ID
Header Source ID
Message Length
Control Information

Body 1 Message Contents

Figure 5.19 General Message Format
--- page 15 ---
Marks Distribution:
Address protection mechanism 2 marks
Process isolation 2 marks
First Fit – 2 marks
Best Fit – 2 marks
Worst Fit – 2 marks
Hardware address protection is a mechanism in an operating system that
ensures each process accesses only its allocated memory space. This protection
is achieved through special hardware registers — primarily the base register
and limit register — which define the valid address range for each process.
Base Register: Holds the starting physical address of the process’s memory
space.
Limit Register: Specifies the size or maximum offset of the process’s
addressable memory range.
When a process generates an address (logical address), the hardware adds the
base value to it to get the physical address.
Before accessing memory, the hardware checks whether the logical address is
less than the limit. If it exceeds, the access is blocked, and a trap or exception
is raised.
If 0 ≤ Logical Address < Limit ⇒ Access Allowed
Else ⇒ Trap (Illegal Access)
Process Isolation Example
Consider two processes — P1 and P2.
P1 has Base = 1000 and Limit = 500, so it can access physical addresses 1000–
1499.
P2 has Base = 2000 and Limit = 400, so it can access addresses 2000–2399.
If P1 tries to access memory location 1800, the hardware check will detect it
is beyond its limit (1499), triggering a trap — thereby preventing illegal access
to P2’s memory region.
********** 15 **********
--- page 16 ---
FOI 7 6 FC Cr
--- page 17 ---
6 A   I.   Illustrate and describe, using a suitable diagram, how a process 10
transitions through various states during its execution.
II.   Identify and explain the conditions under which each state transition
takes place.
III.   Apply your understanding of process scheduling to explain two
scenarios in which a process may transition from the Running state to
the Ready state before completing its CPU burst.
I.   4 marks
II.   3 Marks
III.   3 Marks
Solution: i. State Transition diagram - (4 marks)
i. Transitions occurrence: (3 marks)
• New→Ready: admitted by long-term scheduler.
• Ready→Running: selected by CPU scheduler.
• Running→Waiting: I/O request, page fault, lock wait.
********** 17 **********
--- page 18 ---
• Waiting→Ready: I/O completes, event/interrupt occurs.
• Running→Ready: preempted by higher priority or time slice expiry.
• Running→Terminated: process exit/abort.
ii. As stated in the Lifecycle diagram, a process may move from the
Running state to the Ready state before completing its CPU burst due
to pre-emption (I/O or event wait) or priority-based scheduling events
(interrupts). - (3 marks)
B A system uses 4 frames for storing process pages in main memory. Assume
that all the page frames are initially empty. Consider the page reference string
given below:
2,3,4,5,3,2,6,7,3,2,3,4,8,7,4,3,2,3,4,7
I.   Simulate the page replacement using the FIFO algorithm.
II.   Simulate the page replacement using the LRU algorithm.
III.   Simulate the page replacement using the Optimal algorithm.
IV.   For each algorithm, calculate the total number of page faults.
V.   Based on your results, which algorithm performs best and why?
Marks Distribution:
2 marks each on every point of questions i.e. 5 * 2 = 10 marks
a)
b)
********** 18 **********

[Text in pictures on this page, read by OCR]
2 3
7 2
| 3
FOF
3 4
6 4
7 7
3 3
2 2
F

Total Page Fault:

F

14

F

F
--- page 19 ---
c)
d) Total number of page faults:
FIFO:14, LRU:10, optimal: 8
e) Based on your results, which algorithm performs best and why?
Optimal minimizes page faults by always replacing the page that will not be
used for the longest time in the future. It uses future knowledge, making it
theoretical but ideal for benchmarking. LRU is better than FIFO because it
uses past usage patterns (replacing least recently used), while FIFO doesn’t
consider usage, just arrival order.
7 A What is resource allocation graph? Consider the following snapshot of a
system having 2 resources (R1 having 1 instance and R2 having 2 instances)
and running 3 processes.
Process   Allocation   Request
R1   R2 R1   R2
P1   1   0 0   1
********** 19 **********

[Text in pictures on this page, read by OCR]
LRU

2 3 4
2 2 2
3 3
4
F F F
3 4 8
2 2 2
3 3 3
6 4 4
7 7 8
F F

Total Page Fault: 10

2 3
2 [2
_| 3
FOF
_3| 4
2 [2
—3| [3
_4 4
7 7

Total Page Fault:
--- page 20 ---
P2   0   1 1   0
P3   0   1 0   0
Draw the resource allocation graph. Find if there is a deadlock or not? If there
is no deadlock then what will be the sequence of the process to get executed?
RAG description 3 marks
Draw RAG 4 marks
Safe Sequence 3 marks
i) What is resource allocation graph? [3 Marks]
 A useful tool in characterizing the allocation of resources to processes
is the resource allocation graph.
 The resource allocation graph is a directed graph that depicts a state of
the system of resources and processes, with each process and each
resource represented by a node.
 A graph edge directed from a process to a resource indicates a resource
that has been requested by the process but not yet granted.
 Within a resource node, a dot is shown for each instance of that
resource.
 Examples of resource types that may have multiple instances are I/O
devices that are allocated by a resource management module in the OS.
 A graph edge directed from a reusable resource node dot to a process
indicates a request that has been granted; that is, the process has been
assigned one unit of that resource.
ii) Draw a resource allocation graph of the following table? [4 Marks]
********** 20 **********
--- page 21 ---
iii) Find if there is a deadlock or not? If there is no deadlock then what will be
the sequence of the process to get executed?   [3 Marks]
There is no deadlock in the resource allocation graph.
The sequence of process to execute in safe sequence is
P3 -> P1 ->P2
B Define a PCB. How can it help in enabling multi-tasking?   5
Definition 1 Mark
Explanation 4 marks
Solution: A Process Control Block (PCB) is a data structure maintained by
the Operating System that contains all the essential information about a
process.   (1 mark)
Multitasking means executing multiple processes seemingly at the same time
by rapidly switching the CPU between them.
Here’s how PCB makes that possible:
1. Context Saving:
a. When a running process is interrupted (e.g., due to time slice
expiry or I/O request),
the OS saves its current CPU state (registers, PC, etc.) into its
PCB.
2. Context Restoration:
a. When the process is scheduled again, the OS restores the saved
state from its PCB.
The process resumes exactly where it left off.
3. Accurate Process Switching:
a. The PCB ensures that switching between processes (context
switching) does not corrupt data or execution flow.
4. Tracking Multiple Processes:
********** 21 **********
--- page 22 ---
a. Each process has its own PCB, so the OS can easily track,
suspend, resume, or terminate any process at any time.
(4 marks)
C Summarize the main file attributes managed by a file system and explain the 5
common operations that can be performed on a file.
Key Attributes 2.5 marks
File Operations 2.5 marks
Key File attributes:
File attributes are pieces of information maintained by the file system about a
file and are typically kept in the directory structure on the disk.
Name: This is the only file information kept in human-readable form.
Identifier: This is a unique tag (a number) that identifies the file within the
file system.
Type: This is needed for systems that support different types of files.
Location: This is a pointer that indicates the file's location on the storage
device.
Size: This records the current size of the file.
Protection: This controls who can perform operations such as reading,
writing, and executing the file.
Time, Date, and User Identification: This data is maintained for protection,
security, and monitoring file usage.
Major File Operations:
The operating system provides several major operations that can be
performed on files:
Create: This operation creates a new file.
Write: This operation writes data to the file starting at the current write
pointer location.
Read: This operation reads data from the file starting at the current read
pointer location.
Delete: This operation deletes the file.
Open (Fj): This operation involves searching the directory structure on disk
for the entry Fj and moving the content of that entry into memory.
Close (Fi): This operation moves the content of file entry Fi from memory
back to the directory structure on the disk.
Reposition (Seek): This operation moves the read/write pointer within the
file.
Truncate: This operation zeros the file length and keeps the attributes, but
discards the file's contents.
********** 22 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 2ef5f34cd14b

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CSE_DS_7011/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 25 Nov 2025
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 25 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 1 ;   a.   Compare User Mode and Kernel Mode operations. Explain how 5
SO-1 ;
switching between them affects system efficiency.
BL-4
Ans:
(3 marks for compare any 3 points and 2 marks for system efficiency)
Aspect   User Mode   Kernel Mode
Limited access — cannot   Full access to
Access to
directly access hardware or hardware and all
Resources
kernel data.   system resources.
Executes privileged
instructions such as
Execution   Runs non-privileged
I/O operations,
Privileges   instructions only.
memory
management, etc.
Used by the
Used to run user
operating system to
Purpose   applications (e.g., text
manage hardware
editors, browsers).
and system tasks.
Safer — errors in user   Risky — any fault
Security   programs do not crash the   can crash the
entire system.   system.
Requires switching to
Mode   Switches back to
Kernel Mode for system
Switching   User Mode after
calls or I/O requests.
********** 1 **********
--- page 2 ---
completing the
service.
Effect on System Efficiency:
• Every time a user program requests a system service (like file
access or I/O), the CPU switches from User Mode to Kernel
Mode and back.
• This mode switching involves saving and restoring CPU states,
which causes overhead and reduces efficiency if it happens too
frequently.
•   Efficient system design aims to minimize mode switching to
maintain performance while still ensuring security and stability.
CO- 2 ;   b.   For the given below resource allocation graph. Analyze is there a 5
SO-2 ;
deadlock or not using allocation and request matrix. Justify your answer.
BL-5
Ans:
(3 marks)
To determine the state of the system we will write it in the form of an
allocation and request matrix.
R1 R2 R3 R1 R2 R3
P1
0   1   0   1   0   0
P2 1   0   0   0   0   1
P3 0   0   1   0   1   0
********** 2 **********
--- page 3 ---
P4 0   0   1   0   0   0
Algorithm to check deadlock (2 marks)
First, find the currently available instances of each resource.
Check for each process which can be executed using the allocated +
available resource.
Add the allocated resource of the executable process to the available
resources and terminate it.
Repeat the 2nd and 3rd steps until the execution of each process.
If at any step, none of the processes can be executed then there is a
deadlock in the system.
Using the above algorithm, we will get that there is no deadlock in the
above-given example, and their sequence of execution can be P4 → P2
→ P1 → P3.
CO- 3;   c.   Explain the Two level and Tree structured directory structures used in a 5
SO- 1;
file management system, with their advantages and disadvantages.
BL- 2
Ans:
a. Two-Level Directory (2.5 marks)
Advantages:
• Solves name conflict problem.
• Each user can manage their own files independently.
Disadvantages:
• No support for grouping related files within user directory.
b. Hierarchical (Tree) Directory (2.5 marks)
********** 3 **********

[Text in pictures on this page, read by OCR]
master file
directory user 1 | user 2| user 3| user 4

a

ae at a | test a | data a | test x |data| a

“Tiiliiii itt
--- page 4 ---
Advantages:
• Organizes files logically in groups.
• Easy to manage large number of files.
• Avoids name conflicts.
Disadvantages:
• More complex to implement.
CO- 4 ;   d.   Compare iOS and Android operating system software   5
SO-1 ;
(Correct 8 points 5 marks)
BL-4
Feature   iOS (Apple)   Android (Google)
Google (Open Source
Developer / Company   Apple Inc.
under AOSP)
Works on multiple
Works only on Apple
Device Compatibility   brands (Samsung,
devices (iPhone, iPad)
OnePlus, Xiaomi, etc.)
Highly customizable
Simple, uniform, and
User Interface (UI)   with widgets,
consistent
launchers, and themes
Google Play Store
Apple App Store
App Store   (more apps, but less
(strict app review)
strict control)
Very limited (Apple   Highly customizable
Customization   controls system   (users can modify
design)   almost everything)
********** 4 **********
--- page 5 ---
Varies by
Regular and
manufacturer and
Software Updates   simultaneous for all
model (updates may
Apple devices
be delayed)
Secure but more
Very secure and
Security   vulnerable due to
closed system
open-source nature
Voice Assistant   Siri   Google Assistant
Uses AirDrop   Uses Bluetooth, Wi-Fi
File Sharing   (between Apple   Direct, and apps like
devices only)   SHAREit
Default Browser   Safari   Google Chrome
Q2   a.   Assume the following processes arrive for execution at the time   [10]
CO-2;   indicated and the length of CPU burst time given in msec.
SO-2;
Process No.   Burst time   Arrival time   Priority
BL-5
P1   0   4   2
P2   1   2   4
P3   2   3   6
P4   3   5   10
P5   4   1   8
P6   5   4   12
P7   6   6   9
Note: Higher number is having higher priority
a. Draw Gantt chart for SRTF and Preemptive Priority scheduling.
b. Calculate average waiting time and average turnaround time.
Ans: SRTF (5 marks)
0 2 3 6 9 13 18 26
|Idle|P2|P3|P4|P5|P6|P7|
********** 5 **********
--- page 6 ---
Arriv
Process   Burst Completion TAT = C-A WT = TAT-B
al
P1   4   0   4   0   0
P2   2   1   3   1   0
P3   3   2   6   3   1
P4   5   3   9   4   1
P5   1   4   13   12   8
P6   4   5   18   14   9
P7   6   6   26   20   14
Average TAT = (0+1+3+4+12+14+20)/7 = 54/7 ≈ 7.71
Average WT = (0+0+1+1+8+9+14)/7 = 33/7 ≈ 4.71
. Preemptive Priority (5 marks)
0-1: Idle
1-4: P5
4-11: P6
11-14: P4
14-20: P7
20-23: P5
23-25: P3
25-26: P2
Arriv
Process   Burst Completion TAT = C-A WT = TAT-B
al
P1   4   0   4   0   0
P2   2   1   26   24   23
P3   3   2   25   22   20
P4   5   3   14   9   6
P5   1   4   23   22   18
P6   4   5   11   7   2
P7   6   6   20   14   8
Average TAT = (0+24+22+9+22+7+14)/7 = 98/7 ≈ 14
Average WT = (0+23+20+6+18+2+8)/7 = 77/7 ≈ 11
Q2   b.   Explain the concept of demand paging with reference to virtual   [10]
CO-3;   memory, including the role of valid and invalid bits with a neat labelled
SO-2;
diagram.
BL- 2
Ans: Virtual Memory (2 marks)
Definition:
Virtual memory is a memory management technique that gives an
application the illusion of having a large, contiguous main memory,
********** 6 **********
--- page 7 ---
even though the physical memory (RAM) may be smaller. It allows
programs to execute partially in main memory and partially on
secondary storage (like a disk).
Demand Paging (2 marks)
Definition:
Demand paging is a lazy loading technique where pages are loaded into
memory only when they are needed, rather than loading the entire
process at once.
Working: (4 marks)
Each page in the page table has a valid/invalid bit:
Valid bit = 1: Page is in main memory (physical memory).
Invalid bit = 0: Page is not in main memory (may be on disk or not part
of process).
When a process tries to access a page:
The system checks the valid/invalid bit.
If valid, the page is accessed normally.
If invalid, a page fault occurs. The OS loads the required page from disk
into memory and updates the page table.
Advantages of Demand Paging:
Reduces memory requirement.
Improves system throughput by avoiding loading unused pages.
Diagram (2 marks)
********** 7 **********

[Text in pictures on this page, read by OCR]
2

valid—invalid
bit 3

ane
of 4 |v 4A
af fi 5
2| 6 |v
3 i 6) Cc
4 i Fr
5) 9 |v
6) fi 8)
e i 9] F
page table 10

1

12

13

14

15

physical memory
--- page 8 ---
Q3   a.   Consider the following disk queue with requests for I/O to block on   [10]
CO- 3;   cylinders:
SO-6;
55, 58, 39, 18, 80, 160, 158, 38, 184
BL-5
Assume that a disk has 200 tracks from 0 to 199.Consider that the head
starts from location 100
Find the total head movement of the cylinder for the following
i.   SSTF
ii.   SCAN (towards higher side of track)
iii.   C-SCAN (towards higher side of track)
iv.   LOOK (towards higher side of track)
v.   C-LOOK (towards higher side of track)
Ans:
i.   SSTF (2 marks)
Seek time = 248
ii.   SCAN (towards higher side of track) (2 marks)
Seek time= 280
iii.   C-SCAN (towards higher side of track) (2 marks)
Seek time = 384
iv.   LOOK (towards higher side of track) (2 marks)
Seek time = 250
v.   C-LOOK (towards higher side of track) (2 marks)
Seek time = 322
Q3   b.   Explain the different types of operating system kernels and illustrate   [10]
CO- 1;   them with diagrams.
SO-1;   Ans: Diagram (4 marks)
BL-2   Explain (2 marks each)
Q4   a   Discuss the issues in Peterson’s solution for critical section problem and [10]
CO-2;   how they are addressed. Also, design a pseudocode to explain the
SO-2;
concept of a binary semaphore.
BL-6
Ans: Peterson’s Solution: (5 marks)
********** 8 **********

[Text in pictures on this page, read by OCR]
Monolithic Kemel Microkemel “Hybrid kemel"
based Operating System based Operating System based Operating System

Operating system
--- page 9 ---
A classic software-based solution to achieve mutual exclusion for two
processes.
Uses two variables:
flag[i] → indicates if process i wants to enter the critical section
turn → indicates whose turn it is
flag[0] = true;
turn = 1;
while (flag[1] == true && turn == 1)
; // wait
// Critical Section
flag[0] = false;
Problems:
Limited to Two Processes:
Works only for two processes. Cannot directly extend to multiple
processes.
Busy Waiting:
Uses busy waiting, wasting CPU cycles while waiting.
Not Practical on Modern Multiprocessors:
Relies on atomic read/write assumptions which may not hold due to
compiler optimization or hardware caching
Binary Semaphore (5 marks)
Definition:
A binary semaphore is a synchronization tool that can have only two
values: 0 and 1.
Used to control access to a single shared resource.
1 → resource available
0 → resource unavailable
wait(s):
while s == 0:
; // busy wait
s = 0
signal(s):
s = 1
Q4   b   Explain the various types of Memory Partitioning techniques used in [10]
Operating Systems. Support your explanation with suitable examples.
********** 9 **********
--- page 10 ---
CO-3;   Ans:
SO-6;
Types of Memory Partitioning
BL-2
1. Fixed Partitioning (Static Partitioning)(5 marks)
In this method, memory is divided into fixed-size partitions at the time
of system initialization. Each partition can hold only one process at a
time.
If a process is smaller than the partition, the remaining space is wasted
— this is called internal fragmentation. If the process is larger than the
partition, it cannot be loaded.
Example:
Suppose 1 GB of memory is divided into four partitions of 256 MB each.
If a process of 150 MB is loaded, 106 MB remains unused in that
partition.
2. Dynamic Partitioning (Variable Partitioning) (5marks)
In this method, partitions are created dynamically according to the size
of each process.
There is no fixed size for partitions; memory is allocated exactly as much
as required.
It reduces internal fragmentation but may cause external fragmentation,
as free spaces appear between allocated blocks over time.
Example:
If a process requires 200 MB, exactly 200 MB is allocated from the free
memory.
When it finishes, that 200 MB space becomes available for another
process.
Q5   a.   Consider the following snapshot of the system in which there are five   [10]
CO-2;   process and three resources A, B, C and D
SO-2;
BL-5
Allocation   Max   Available
A B C D A B C D A B C D
P0   0   0   1   2   0   0   1   2   1   5   2   0
P1   1   0   0   0   1   7   5   0
P2   1   3   5   4   2   3   5   6
P3   0   6   3   2   0   6   5   2
P4   0   0   1   4   0   6   5   6
********** 10 **********
--- page 11 ---
Answer the following question using Banker’s Algorithm
i.   Calculate Need Matrix?
ii.   Is, the system in safe state? If Yes, give safe sequence.
iii.   If the request from P1 arrives for (0, 4, 2, 1); can the request
be granted immediately?
Ans:
1. Need Matrix (2 mrks)
Pro
ces A B C D
s
P0 0   0   0   0
P1 0   7   5   0
P2 1   0   0   2
P3 0   0   2   0
P4 0   6   4   2
2. All processes can finish → System is in safe state (4 marks)
Safe sequence: P0, P2, P3, P4, P1
3. Request from P1 (0,4,2,1) granted? No, exceeds declared Need.
(4 marks)
Q5   b.   Define Operating System? Explain different services provided by   [10]
CO-1;   Operating System.
SO-1;
Ans: Operating system 2 marks
BL-2
Service diagram – 3 marks
Explain service- 5 marks
Q6   a.   Define Page fault? Calculate total number of page fault, page hit for the   [10]
CO-3;   following string using LRU, FIFO and optimal page replacement policy.
SO-6;
Consider the page frame size is 3.
BL-5
********** 11 **********
--- page 12 ---
6, 7, 8, 9, 6, 7, 1, 6, 7, 8, 9, 1, 7, 9, 6
Ans: Define page fault- 2 marks
LRU (3 marks)
PF=12, PH-3
FIFO (2 marks)
PF=11, PH=4
Optimal (3 marks)
PF=8, PH=7
Q6   b.   What is a process? Explain the process state diagram and the role of the   [10]
CO-2;   process control block (PCB).
SO-2;
Ans: Define process- 2marks
BL-2
Process diagram- 2 marks, explain- 2 marks
PCB- 1marks diagram and 3 marks explain
Q7   a.   Explain the Chained allocation method of file storage with a neat   [10]
CO-3;   diagram. Discuss its advantages, disadvantages, and possible ways to
SO-2;
overcome the disadvantages.
BL-2
Ans: Diagram (2 marks)
********** 12 **********
--- page 13 ---
Explain (4 marks)
•   Allocation on basis of individual block
• Each block contains a pointer to the next block in the chain
• Only single entry in the file allocation table
– Starting block and length of file
• No external fragmentation
•   Best for sequential files
Advantages (1 marks)
1. No external fragmentation
2. Dynamic file size
3. Efficient sequential access
Disadvantages (1 marks)
1. Access time for random access is slow
2. Pointer overhead
3. Reliability problem
How to Overcome Disadvantages (2 marks)
1. Use an index block (Indexed Chaining)
2. Combine with other allocation methods
Q7   b.   What is the Reader-Writer Problem? Design pseudocode to solve it   [10]
CO-2;   using semaphores.
SO-2;
Ans: Reader-Writer Problem (2 marks)
BL-6
The Reader-Writer Problem is a classic synchronization problem in
operating systems. It deals with concurrent access to a shared resource
(like a database) by multiple processes:
• Readers: Processes that only read the data and do not modify it.
•   Writers: Processes that write or modify the data.
********** 13 **********
--- page 14 ---
Pseudocode
Reader Process (4 marks)
Reader() {
wait(mutex)   // Entry section
read_count = read_count + 1
if read_count == 1 then
wait(rw_mutex)   // First reader locks writers
signal(mutex)   // Exit section
// Critical section (Reading)
read_data()
wait(mutex)   // Entry section
read_count = read_count - 1
if read_count == 0 then
signal(rw_mutex)   // Last reader unlocks writers
signal(mutex)   // Exit section
}
Writer Process (4 marks)
Writer() {
wait(rw_mutex)   // Entry section (exclusive access)
// Critical section (Writing)
write_data()
signal(rw_mutex)   // Exit section
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper c3c4d5aef193

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CSBS_7036/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (23 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech
(IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 11 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain the layered structure of an Operating System with suitable
explanation.
Layered Structure of an Operating System
The layered structure of an Operating System is a design approach
where the OS is divided into multiple layers, each performing specific
functions.
Each layer uses services of the lower layer and provides services to the
layer above.
Typical Layers:
CO-1 ;
SO-2 ;   1. Hardware – Physical components like CPU, memory, I/O devices   5
BL-2   2. Kernel – Manages processes, memory, and devices
3. System Call Interface – Connects user programs with kernel
4. System Programs – Utilities like compilers and editors
5. User Interface – CLI/GUI for user interaction
Advantages:
• Easy to design and debug
•   Better modularity and security
********** 1 **********
--- page 2 ---
Disadvantages:
•   Performance overhead due to multiple layers
b.   Define a process and describe its different states with a diagram.
Definition of a Process
A process is a program in execution. It is an active entity that includes
not only the program code but also its current activity, such as the
program counter, CPU registers, stack, and data.
Different States of a Process
CO-2 ;
SO- 2;   5
BL-2
A process passes through the following states during its lifecycle:
1. New (Created)
o The process is being created.
o Resources are allocated, but execution has not yet started.
2. Ready
o The process is ready to run and waiting for CPU
allocation.
o   It resides in the ready queue.
3. Running
o The process is currently executing on the CPU.
o Only one process can be in this state per CPU at a time.
4. Waiting (Blocked)
o The process is waiting for some event to occur (e.g., I/O
completion).
o   It cannot proceed until the event is completed.
5. Terminated (Exit)
o The process has finished execution.
o The OS deallocates its resources.
********** 2 **********
--- page 3 ---
State Transitions (Brief)
• New → Ready (admitted by OS)
• Ready → Running (CPU scheduler selects)
• Running → Waiting (I/O request)
• Waiting → Ready (I/O completion)
• Running → Terminated (execution finished)
c.   What is a race condition? Explain its impact with an example.
Race Condition (5 Marks Answer)
A race condition occurs when two or more processes/threads access
and modify shared data simultaneously, and the final result depends
on the order of execution.
Impact
• Produces incorrect or inconsistent results
CO-3 ;   • May cause data corruption
SO- 2;   • Leads to unpredictable system behavior
5
BL-2
and BL-3
Example
Consider a shared variable count = 5.
Two processes P1 and P2 increment it at the same time.
• Both read count = 5
• Both increment to 6
• Both write back 6
👉 Final value becomes 6 instead of 7 → incorrect result
d.   Define deadlock and briefly explain its necessary conditions.
Here is a crisp 5-mark answer (exam-ready) 👇
Deadlock
Definition:
A deadlock is a situation in an operating system where a set of
processes are blocked indefinitely, each waiting for a resource held by
CO- 3;   another process.
SO- 2;   5
BL-2   Necessary Conditions for Deadlock
(All four must occur simultaneously)
1. Mutual Exclusion
o At least one resource is non-shareable (only one process
can use it at a time)
2. Hold and Wait
o A process holding at least one resource is waiting for
additional resources
********** 3 **********
--- page 4 ---
3. No Preemption
o Resources cannot be forcibly taken; they must be
released voluntarily
4. Circular Wait
o A circular chain of processes exists where each process is
waiting for a resource held by the next process
a. Explain the Producer–Consumer (Bounded Buffer) problem. Write a
semaphore-based solution and explain synchronization. (10 Marks)
Producer–Consumer (Bounded Buffer) Problem
b.   The Producer–Consumer problem is a synchronization problem
where a producer process generates data and places it in a fixed-size
buffer, while a consumer process removes data from the buffer. Since
the buffer is bounded, the producer must wait if the buffer is full, and
the consumer must wait if the buffer is empty.
Semaphore-Based Solution
Let:
• mutex = 1 (ensures mutual exclusion)
• empty = N (number of empty slots in buffer)
• full = 0 (number of filled slots)
Q2
CO-2;
SO-2;   Producer   [20]
BL-3   do {
and BL-4   wait(empty);
wait(mutex);
// insert item into buffer
signal(mutex);
signal(full);
} while(true);
Consumer
do {
wait(full);
wait(mutex);
// remove item from buffer
signal(mutex);
signal(empty);
} while(true);
********** 4 **********
--- page 5 ---
Synchronization Explanation
• mutex ensures only one process accesses the buffer at a time
(mutual exclusion).
• empty prevents the producer from adding data when the buffer
is full.
• full prevents the consumer from removing data when the
buffer is empty.
• wait() and signal() operations coordinate execution and
avoid race conditions.
Conclusion
The semaphore-based solution ensures proper synchronization between
producer and consumer, preventing buffer overflow, underflow, and
race conditions.
Consider the following processes:
Process Arrival Time Burst Time
P1   0   6
P2   1   4
P3   2   5
P4   3   3
i) Apply Shortest Remaining Time First (Preemptive) scheduling. Draw
the Gantt Chart and calculate Average Waiting Time and Average
Turnaround Time. (4 Marks)
ii) Apply Shortest Job First (Non-Preemptive) scheduling. Draw the
Gantt Chart and calculate Average Waiting Time and Average
Turnaround Time. (4 Marks)
iii) Compare both algorithms based on Average Waiting Time and
Turnaround Time. (2 Marks)
Given Processes
Pro
AT BT
cess
P1 0   6
P2 1   4
P3 2   5
P4 3   3
## i) SRTF (Preemptive)
Gantt Chart:
0–1 P1 | 1–5 P2 | 5–8 P4 | 8–13 P3 | 13–18 P1
********** 5 **********
--- page 6 ---
Completion Time (CT):
Pro
CT
cess
P1 18
P2 5
P3 13
P4 8
Turnaround Time (TAT = CT – AT)
Pro
TAT
cess
P1 18
P2 4
P3 11
P4 5
Waiting Time (WT = TAT – BT)
Pro
WT
cess
P1 12
P2 0
P3 6
P4 2
Average Times:
• Avg WT = (12 + 0 + 6 + 2) / 4 = 5
• Avg TAT = (18 + 4 + 11 + 5) / 4 = 9.5
## ii) SJF (Non-Preemptive)
Gantt Chart:
0–6 P1 | 6–9 P4 | 9–13 P2 | 13–18 P3
Completion Time (CT):
Pro
CT
cess
P1 6
P2 13
P3 18
P4 9
********** 6 **********
--- page 7 ---
Turnaround Time (TAT):
Pro
TAT
cess
P1 6
P2 12
P3 16
P4 6
Waiting Time (WT):
Pro
WT
cess
P1 0
P2 8
P3 11
P4 3
Average Times:
• Avg WT = (0 + 8 + 11 + 3) / 4 = 5.5
• Avg TAT = (6 + 12 + 16 + 6) / 4 = 10
## iii) Comparison
• SRTF gives lower Average Waiting Time (5 < 5.5)
• SRTF gives lower Average Turnaround Time (9.5 < 10)
• Hence, SRTF performs better than SJF (Non-Preemptive) for
this set.
a.   Discuss the Readers–Writer problem. Explain its semaphore-based
solution and describe how synchronization is achieved when multiple
readers and a single writer access shared data. (10 Marks)
Readers–Writers Problem
The Readers–Writers problem is a classic synchronization problem
Q3   where:
CO-2;   b.   • Multiple readers can read shared data simultaneously   [20]
SO-2;   • A writer must have exclusive access to the shared data
BL-3 and
BL-4   👉 The challenge is to ensure:
• No reader reads while a writer is writing
• No writer writes while readers are reading
Semaphore-Based Solution
********** 7 **********
--- page 8 ---
Shared Variables:
• mutex = 1 → protects read count
• rw_mutex = 1 → controls access to shared resource
• read_count = 0 → number of active readers
Reader Process
do {
wait(mutex);
read_count++;
if (read_count == 1)
wait(rw_mutex);   // first reader blocks writers
signal(mutex);
// Reading is performed
wait(mutex);
read_count--;
if (read_count == 0)
signal(rw_mutex); // last reader releases writer
signal(mutex);
} while(true);
Writer Process
do {
wait(rw_mutex);
// Writing is performed
signal(rw_mutex);
} while(true);
How Synchronization is Achieved
• Multiple Readers Allowed:
Readers can access the data simultaneously since they do not
modify it
• Writer Gets Exclusive Access:
rw_mutex ensures only one writer can access the resource and
blocks readers during writing
• Reader Priority (in this version):
First reader locks the resource; last reader releases it
• Mutual Exclusion:
Writers are mutually exclusive with both readers and other
writers
Conclusion
The semaphore-based solution ensures correct synchronization by
allowing concurrent reading while maintaining exclusive writing,
thus preventing race conditions and ensuring data consistency.
********** 8 **********
--- page 9 ---
Given the following processes (all arriving at time 0 ms)
Process   Burst Time (ms)
P1   6
P2   8
P3   3
P4   5
a) Apply Round Robin Scheduling (Time Quantum = 2 ms). Draw the
Gantt Chart and compute Average Waiting Time and Average Turnaround
Time. (4 Marks)
b) Apply First Come First Serve (FCFS) scheduling. Draw the Gantt Chart
and compute Average Waiting Time and Average Turnaround Time. (4
Marks)
c) Compare both algorithms based on the results obtained. (2 Marks)
Given Processes (All AT = 0)
Bur
Pro   st
cess Tim
e
P1 6
P2 8
P3 3
P4 5
## a) Round Robin (Time Quantum = 2 ms)
Gantt Chart:
0–2 P1 | 2–4 P2 | 4–6 P3 | 6–8 P4 |
8–10 P1 | 10–12 P2 | 12–13 P3 | 13–15 P4 |
15–17 P1 | 17–19 P2 | 19–20 P4 | 20–22 P2
Completion Time (CT):
Pro
CT
cess
P1 17
P2 22
P3 13
P4 20
********** 9 **********
--- page 10 ---
Turnaround Time (TAT = CT – AT)
Pro
TAT
cess
P1 17
P2 22
P3 13
P4 20
Waiting Time (WT = TAT – BT)
Pro
WT
cess
P1 11
P2 14
P3 10
P4 15
Average Times:
• Avg WT = (11 + 14 + 10 + 15) / 4 = 12.5
• Avg TAT = (17 + 22 + 13 + 20) / 4 = 18
## b) FCFS Scheduling
Gantt Chart:
0–6 P1 | 6–14 P2 | 14–17 P3 | 17–22 P4
Completion Time (CT):
Pro
CT
cess
P1 6
P2 14
P3 17
P4 22
Turnaround Time (TAT):
Pro
TAT
cess
P1 6
P2 14
P3 17
P4 22
Waiting Time (WT):
********** 10 **********
--- page 11 ---
Pro
WT
cess
P1 0
P2 6
P3 14
P4 17
Average Times:
• Avg WT = (0 + 6 + 14 + 17) / 4 = 9.25
• Avg TAT = (6 + 14 + 17 + 22) / 4 = 14.75
## c) Comparison
• FCFS has lower Average Waiting Time (9.25 < 12.5)
• FCFS has lower Average Turnaround Time (14.75 < 18)
• Round Robin provides better response time but higher
waiting time
a.   Explain deadlock and its four necessary conditions. Discuss techniques
to handle deadlock including prevention, avoidance, detection, and
recovery. (10 Marks)
Deadlock
Definition
A deadlock is a situation in an operating system where a group of
b.   processes are blocked indefinitely, each waiting for a resource held by
another process in the group.
Q4   Necessary Conditions for Deadlock
(All four must occur simultaneously)
CO-2 and
CO-3;
1. Mutual Exclusion   [20]
SO-2;
o At least one resource is non-shareable, i.e., only one
BL-3
process can use it at a time.
and BL-4   2. Hold and Wait
o A process holding one or more resources is waiting for
additional resources.
3. No Preemption
o Resources cannot be forcibly taken; they must be
released voluntarily.
4. Circular Wait
o A set of processes forms a circular chain, where each
process is waiting for a resource held by the next.
Techniques to Handle Deadlock
********** 11 **********
--- page 12 ---
1. Deadlock Prevention
• Ensures that at least one of the necessary conditions is
eliminated.
• Methods:
o Remove mutual exclusion (if possible)
o Avoid hold and wait (request all resources at once)
o Allow preemption of resources
o Break circular wait (impose ordering of resources)
2. Deadlock Avoidance
• System checks resource allocation dynamically to avoid unsafe
states.
• Uses algorithms like Banker’s Algorithm.
•   Allocates resources only if the system remains in a safe state.
3. Deadlock Detection
• Allows deadlock to occur and then detects it.
• Techniques:
o Resource Allocation Graph (for single instance)
o Detection algorithms (for multiple instances)
4. Deadlock Recovery
• Once detected, system takes action:
o Terminate processes (all or one by one)
o Resource preemption (take resources and reassign)
o Rollback processes to a safe state
Consider the page reference string: (10 Marks)
3, 1, 2, 0, 3, 1, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 4, 3, 2, 1
i) Calculate the number of page faults using:
• FIFO
• LRU
• OPTIMAL
(Assume 3 frames)
ii) Identify the best algorithm and justify your answer.
Given:
********** 12 **********
--- page 13 ---
Page Reference String:
3, 1, 2, 0, 3, 1, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 4, 3, 2, 1
Number of Frames = 3
i) Page Fault Calculation
1. FIFO (First-In First-Out)
• Replace the oldest page first.
Page Faults = 15
2. LRU (Least Recently Used)
• Replace the page that has not been used for the longest time.
Page Faults = 12
3. OPTIMAL
• Replace the page that will not be used for the longest time in
future.
Page Faults = 9
ii) Best Algorithm
👉 OPTIMAL is the best algorithm
Justification:
•   It gives the minimum number of page faults (9).
•   It uses future knowledge, so it is theoretically optimal.
• However, it is not practical in real systems because future
references are unknown.
•   In practice, LRU is preferred as it approximates OPTIMAL.
Final Answer Summary
Algorithm   Page Faults
FIFO   15
LRU   12
OPTIMAL   9 ✅
********** 13 **********
--- page 14 ---
a.   Explain the Paging memory management technique.
Describe how paging eliminates the problem of external fragmentation
and explain the address translation mechanism with a neat diagram.
(10M)
Paging Memory Management Technique
Definition
b.
Paging is a memory management technique in which:
• Logical memory is divided into fixed-size pages
•   Physical memory is divided into fixed-size frames
• Pages are mapped to frames using a page table
Working of Paging
• A logical address is divided into:
o Page Number (p) → used to index the page table
o Offset (d) → specifies location within the page
Q5   • The page table maps page → frame
•   Physical address = Frame Number + Offset
CO-2 and
CO3; SO-
[20]
2;   Elimination of External Fragmentation
BL-3
and BL-4   •   In paging, memory is allocated in fixed-size blocks
• Any free frame can be assigned to any page
• Hence, no need for contiguous memory allocation
👉 Therefore:
• External fragmentation is eliminated
• Only internal fragmentation may occur (unused space within a
frame)
Address Translation Mechanism
Steps:
1. CPU generates a logical address (p, d)
2. Page number (p) is used to index the page table
3. Corresponding frame number (f) is obtained
4. Physical address is formed as (f, d)
Diagram (Conceptual)
Logical Address
┌──────────────┐
********** 14 **********
--- page 15 ---
│ Page | Offset│
└──────────────┘
↓
Page Table
(maps Page → Frame)
↓
┌──────────────┐
│Frame | Offset│
└──────────────┘
= Physical Address
↓
Physical Memory
Advantages
✔ Eliminates external fragmentation
✔ Efficient memory utilization
✔ Easy allocation of memory
Disadvantages
✖ May cause internal fragmentation
✖ Requires additional memory for page table
✖ Extra overhead in address translation
Conclusion
Paging provides an efficient way to manage memory by dividing it into
fixed-size units, eliminating external fragmentation and enabling
flexible memory allocation.
Consider the following snapshot of a system:
Process Allocation Max (A B   Available (A B
(A B C)   C)   C)
P0   0 1 0   7 5 3   3 3 2
P1   2 0 0   3 2 2   —
P2   3 0 2   9 0 2   —
P3   2 1 1   2 2 2   —
P4   0 0 2   4 3 3   —
Answer the following using Banker’s Algorithm:
1. Find the Need Matrix
2. Determine whether the system is in a safe state. If yes, write the
safe sequence
3.   If a request from process P1 (1, 0, 2) arrives, can it be granted
immediately? Justify
1. Need Matrix (Need = Max – Allocation)
********** 15 **********
--- page 16 ---
Allo
cati Max Nee
Pro
on (A B d (A
cess
(A B C) B C)
C)
0 1 7 5 7 4
P0
0   3   3
2 0 3 2 1 2
P1
0   2   2
3 0 9 0 6 0
P2
2   2   0
2 1 2 2 0 1
P3
1   2   1
0 0 4 3 4 3
P4
2   3   1
2. Safe State Check
Available = (3, 3, 2)
Step-wise:
• P1 → Need (1,2,2) ≤ (3,3,2) ✔ → New Available = (5,3,2)
• P3 → Need (0,1,1) ≤ (5,3,2) ✔ → New Available = (7,4,3)
• P4 → Need (4,3,1) ≤ (7,4,3) ✔ → New Available = (7,4,5)
• P0 → Need (7,4,3) ≤ (7,4,5) ✔ → New Available = (7,5,5)
• P2 → Need (6,0,0) ≤ (7,5,5) ✔
Safe Sequence:
P1 → P3 → P4 → P0 → P2
👉 System is in a SAFE state
3. Request by P1 = (1, 0, 2)
Check 1: Request ≤ Need
(1,0,2) ≤ (1,2,2) ✔
Check 2: Request ≤ Available
(1,0,2) ≤ (3,3,2) ✔
New Available after allocation:
(3,3,2) – (1,0,2) = (2,3,0)
Check Safe State Again:
• P1 → Need becomes (0,2,0) ≤ (2,3,0) ✔ → Available = (5,3,0)
• P3 → (0,1,1) ✖ (fails due to C=1 > 0)
• P2 → (6,0,0) ✖
• P4 → (4,3,1) ✖
********** 16 **********
--- page 17 ---
• P0 → (7,4,3) ✖
👉 No further process can proceed
Final Answer:
•
a.   Explain the concept of File Management in an Operating System.
Discuss different file organization methods and explain how files are
stored and accessed in secondary storage.
File Management in an Operating System
Concept
File Management is a component of the operating system responsible
for creating, storing, organizing, accessing, and protecting files on
secondary storage devices such as disks.
A file is a collection of related data stored on secondary storage and
b.   identified by a unique name.
Functions of File Management
•   File creation and deletion
•   File reading and writing
•   Directory management
• Access control and protection
Q6   • Storage allocation and space management
CO-3;
SO-2;   [20]
BL-2   File Organization Methods
1. Sequential Organization
and BL-4
• Data is stored in a linear sequence
• Access is done one record after another
Advantages:
• Simple and efficient for batch processing
Disadvantages:
• Slow for random access
2. Direct (Random) Organization
• Data is accessed using direct address or index
• Any record can be accessed directly
Advantages:
********** 17 **********
--- page 18 ---
•   Fast access
Disadvantages:
• Requires more complex implementation
3. Indexed Organization
• Uses an index table to locate records
• Combines features of sequential and direct access
Advantages:
•   Efficient searching
• Supports both sequential and random access
Disadvantages:
• Extra storage needed for index
File Storage in Secondary Storage
Files are stored on disks using different allocation methods:
1. Contiguous Allocation
•   File occupies continuous blocks
•   Fast access
2. Linked Allocation
•   File blocks are scattered but linked together
• No external fragmentation
3. Indexed Allocation
• Uses an index block containing addresses of all file blocks
•   Efficient and flexible
File Access Methods
• Sequential Access → Read/write in order
• Direct Access → Jump to any block directly
• Indexed Access → Use index to locate data
********** 18 **********
--- page 19 ---
Consider the following disk request queue (0–199):
95, 180, 34, 119, 11, 123, 62, 64
Initial head position = 50
Tasks:
1. Apply FCFS and SSTF disk scheduling algorithms
2. Show the order of execution
3. Calculate the total head movement
4. Identify which algorithm performs better and justify.
Given:
Request Queue: 95, 180, 34, 119, 11, 123, 62, 64
Initial Head Position = 50
## 1. FCFS (First Come First Serve)
Order of Execution:
50 → 95 → 180 → 34 → 119 → 11 → 123 → 62 → 64
Head Movements:
Dist
Mo
anc
ve
e
50
→ 45
95
95
→ 85
180
180
→ 146
34
34
→ 85
119
119
→ 108
11
11
→ 112
123
123
→ 61
62
********** 19 **********
--- page 20 ---
62
→ 2
64
Total Head Movement:
45 + 85 + 146 + 85 + 108 + 112 + 61 + 2 = 644
## 2. SSTF (Shortest Seek Time First)
Order of Execution:
50 → 62 → 64 → 34 → 11 → 95 → 119 → 123 → 180
Head Movements:
Move   Distance
50 → 62   12
62 → 64   2
64 → 34   30
34 → 11   23
11 → 95   84
95 → 119 24
119 → 123 4
123 → 180 57
Total Head Movement:
12 + 2 + 30 + 23 + 84 + 24 + 4 + 57 = 236
## 3. Comparison
• FCFS Total Movement = 644
• SSTF Total Movement = 236
Final Answer:
👉 SSTF performs better because it minimizes total head movement,
leading to faster disk access compared to FCFS.
Select any 4:
Q7   1. Explain any two Operating System services with suitable
CO-   examples.
1,CO2   Operating System Services
and CO3;   [20]
1. Process Management
SO-2;
The OS manages the creation, scheduling, and termination of processes.
BL-2
It allocates CPU time to processes and ensures smooth execution.
and BL-3   Example:
When multiple applications (e.g., browser, text editor) are running, the
OS schedules them using CPU scheduling algorithms.
********** 20 **********
--- page 21 ---
2. File Management
The OS handles file operations such as creation, deletion, reading,
writing, and organization of files in directories.
Example:
Creating a file, saving it, renaming it, or deleting it using the file
system.
2. What is a Process Control Block (PCB)? Explain its
components.
Process Control Block (PCB)
Definition:
A Process Control Block (PCB) is a data structure used by the
operating system to store all information about a process. It is created
when a process is initiated and deleted when the process terminates.
Components of PCB
1. Process ID (PID)
o Unique identifier assigned to each process
2. Process State
o Current state of the process (New, Ready, Running,
Waiting, Terminated)
3. Program Counter
o Address of the next instruction to be executed
4. CPU Registers
o Stores values of CPU registers (accumulator, index
registers, etc.) during context switching
5. CPU Scheduling Information
o Includes priority, scheduling queue pointers, etc.
6. Memory Management Information
o Information about memory allocation such as base/limit
registers or page tables
7. I/O Status Information
o List of I/O devices allocated and open files
8. Accounting Information
o CPU usage, execution time, process limits
3. What is a deadlock? Explain the concept of a Wait-For Graph.
Deadlock
Definition:
A deadlock is a situation in which a group of processes are blocked
indefinitely, each waiting for a resource held by another process in the
group.
Wait-For Graph (WFG)
********** 21 **********
--- page 22 ---
Concept:
A Wait-For Graph is a directed graph used to detect deadlocks in a
system with single-instance resources.
• Nodes represent processes
• A directed edge Pi → Pj indicates that process Pi is waiting for
a resource held by Pj
Working:
• Convert the Resource Allocation Graph (RAG) into a Wait-
For Graph by removing resource nodes
•   If the graph contains a cycle, then a deadlock exists
•   If there is no cycle, the system is deadlock-free
Example:
If:
• P1 is waiting for P2
• P2 is waiting for P3
• P3 is waiting for P1
Then a cycle is formed:
P1 → P2 → P3 → P1 → Deadlock exists
4. Define seek time and rotational latency in disk systems.
Seek Time and Rotational Latency
Seek Time
Seek time is the time required for the disk arm (read/write head) to
move from its current position to the desired track where the data is
stored.
Rotational Latency
Rotational latency is the time taken for the disk to rotate so that the
required sector aligns under the read/write head.
5. What is a directory? Explain different directory operations in an
operating system.
Directory in an Operating System
Definition:
A directory is a special file that stores information about files and
subdirectories, helping in organizing and managing files in a
hierarchical structure.
Directory Operations
1. Create Directory
o Creates a new directory in the file system
********** 22 **********
--- page 23 ---
2. Delete Directory
o Removes an existing directory (usually only if it is
empty)
3. Open Directory
o Allows access to the directory for reading its contents
4. Close Directory
o Closes the directory after operations are completed
5. Search Directory
o Searches for a file or subdirectory within the directory
6. List Directory Contents
o Displays all files and subdirectories present
7. Rename Directory/File
o Changes the name of a directory or file
8. Traverse Directory
o Allows navigation through the directory structure
********** 23 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 22a932b6366c

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CyberSecurity_7010/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (23 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech
(IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 11 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain the layered structure of an Operating System with suitable
explanation.
Layered Structure of an Operating System
The layered structure of an Operating System is a design approach
where the OS is divided into multiple layers, each performing specific
functions.
Each layer uses services of the lower layer and provides services to the
layer above.
Typical Layers:
CO-1 ;
SO-2 ;   1. Hardware – Physical components like CPU, memory, I/O devices   5
BL-2   2. Kernel – Manages processes, memory, and devices
3. System Call Interface – Connects user programs with kernel
4. System Programs – Utilities like compilers and editors
5. User Interface – CLI/GUI for user interaction
Advantages:
• Easy to design and debug
•   Better modularity and security
********** 1 **********
--- page 2 ---
Disadvantages:
•   Performance overhead due to multiple layers
b.   Define a process and describe its different states with a diagram.
Definition of a Process
A process is a program in execution. It is an active entity that includes
not only the program code but also its current activity, such as the
program counter, CPU registers, stack, and data.
Different States of a Process
CO-2 ;
SO- 2;   5
BL-2
A process passes through the following states during its lifecycle:
1. New (Created)
o The process is being created.
o Resources are allocated, but execution has not yet started.
2. Ready
o The process is ready to run and waiting for CPU
allocation.
o   It resides in the ready queue.
3. Running
o The process is currently executing on the CPU.
o Only one process can be in this state per CPU at a time.
4. Waiting (Blocked)
o The process is waiting for some event to occur (e.g., I/O
completion).
o   It cannot proceed until the event is completed.
5. Terminated (Exit)
o The process has finished execution.
o The OS deallocates its resources.
********** 2 **********
--- page 3 ---
State Transitions (Brief)
• New → Ready (admitted by OS)
• Ready → Running (CPU scheduler selects)
• Running → Waiting (I/O request)
• Waiting → Ready (I/O completion)
• Running → Terminated (execution finished)
c.   What is a race condition? Explain its impact with an example.
Race Condition (5 Marks Answer)
A race condition occurs when two or more processes/threads access
and modify shared data simultaneously, and the final result depends
on the order of execution.
Impact
• Produces incorrect or inconsistent results
CO-3 ;   • May cause data corruption
SO- 2;   • Leads to unpredictable system behavior
5
BL-2
and BL-3
Example
Consider a shared variable count = 5.
Two processes P1 and P2 increment it at the same time.
• Both read count = 5
• Both increment to 6
• Both write back 6
👉 Final value becomes 6 instead of 7 → incorrect result
d.   Define deadlock and briefly explain its necessary conditions.
Here is a crisp 5-mark answer (exam-ready) 👇
Deadlock
Definition:
A deadlock is a situation in an operating system where a set of
processes are blocked indefinitely, each waiting for a resource held by
CO- 3;   another process.
SO- 2;   5
BL-2   Necessary Conditions for Deadlock
(All four must occur simultaneously)
1. Mutual Exclusion
o At least one resource is non-shareable (only one process
can use it at a time)
2. Hold and Wait
o A process holding at least one resource is waiting for
additional resources
********** 3 **********
--- page 4 ---
3. No Preemption
o Resources cannot be forcibly taken; they must be
released voluntarily
4. Circular Wait
o A circular chain of processes exists where each process is
waiting for a resource held by the next process
a. Explain the Producer–Consumer (Bounded Buffer) problem. Write a
semaphore-based solution and explain synchronization. (10 Marks)
Producer–Consumer (Bounded Buffer) Problem
b.   The Producer–Consumer problem is a synchronization problem
where a producer process generates data and places it in a fixed-size
buffer, while a consumer process removes data from the buffer. Since
the buffer is bounded, the producer must wait if the buffer is full, and
the consumer must wait if the buffer is empty.
Semaphore-Based Solution
Let:
• mutex = 1 (ensures mutual exclusion)
• empty = N (number of empty slots in buffer)
• full = 0 (number of filled slots)
Q2
CO-2;
SO-2;   Producer   [20]
BL-3   do {
and BL-4   wait(empty);
wait(mutex);
// insert item into buffer
signal(mutex);
signal(full);
} while(true);
Consumer
do {
wait(full);
wait(mutex);
// remove item from buffer
signal(mutex);
signal(empty);
} while(true);
********** 4 **********
--- page 5 ---
Synchronization Explanation
• mutex ensures only one process accesses the buffer at a time
(mutual exclusion).
• empty prevents the producer from adding data when the buffer
is full.
• full prevents the consumer from removing data when the
buffer is empty.
• wait() and signal() operations coordinate execution and
avoid race conditions.
Conclusion
The semaphore-based solution ensures proper synchronization between
producer and consumer, preventing buffer overflow, underflow, and
race conditions.
Consider the following processes:
Process Arrival Time Burst Time
P1   0   6
P2   1   4
P3   2   5
P4   3   3
i) Apply Shortest Remaining Time First (Preemptive) scheduling. Draw
the Gantt Chart and calculate Average Waiting Time and Average
Turnaround Time. (4 Marks)
ii) Apply Shortest Job First (Non-Preemptive) scheduling. Draw the
Gantt Chart and calculate Average Waiting Time and Average
Turnaround Time. (4 Marks)
iii) Compare both algorithms based on Average Waiting Time and
Turnaround Time. (2 Marks)
Given Processes
Pro
AT BT
cess
P1 0   6
P2 1   4
P3 2   5
P4 3   3
## i) SRTF (Preemptive)
Gantt Chart:
0–1 P1 | 1–5 P2 | 5–8 P4 | 8–13 P3 | 13–18 P1
********** 5 **********
--- page 6 ---
Completion Time (CT):
Pro
CT
cess
P1 18
P2 5
P3 13
P4 8
Turnaround Time (TAT = CT – AT)
Pro
TAT
cess
P1 18
P2 4
P3 11
P4 5
Waiting Time (WT = TAT – BT)
Pro
WT
cess
P1 12
P2 0
P3 6
P4 2
Average Times:
• Avg WT = (12 + 0 + 6 + 2) / 4 = 5
• Avg TAT = (18 + 4 + 11 + 5) / 4 = 9.5
## ii) SJF (Non-Preemptive)
Gantt Chart:
0–6 P1 | 6–9 P4 | 9–13 P2 | 13–18 P3
Completion Time (CT):
Pro
CT
cess
P1 6
P2 13
P3 18
P4 9
********** 6 **********
--- page 7 ---
Turnaround Time (TAT):
Pro
TAT
cess
P1 6
P2 12
P3 16
P4 6
Waiting Time (WT):
Pro
WT
cess
P1 0
P2 8
P3 11
P4 3
Average Times:
• Avg WT = (0 + 8 + 11 + 3) / 4 = 5.5
• Avg TAT = (6 + 12 + 16 + 6) / 4 = 10
## iii) Comparison
• SRTF gives lower Average Waiting Time (5 < 5.5)
• SRTF gives lower Average Turnaround Time (9.5 < 10)
• Hence, SRTF performs better than SJF (Non-Preemptive) for
this set.
a.   Discuss the Readers–Writer problem. Explain its semaphore-based
solution and describe how synchronization is achieved when multiple
readers and a single writer access shared data. (10 Marks)
Readers–Writers Problem
The Readers–Writers problem is a classic synchronization problem
Q3   where:
CO-2;   b.   • Multiple readers can read shared data simultaneously   [20]
SO-2;   • A writer must have exclusive access to the shared data
BL-3 and
BL-4   👉 The challenge is to ensure:
• No reader reads while a writer is writing
• No writer writes while readers are reading
Semaphore-Based Solution
********** 7 **********
--- page 8 ---
Shared Variables:
• mutex = 1 → protects read count
• rw_mutex = 1 → controls access to shared resource
• read_count = 0 → number of active readers
Reader Process
do {
wait(mutex);
read_count++;
if (read_count == 1)
wait(rw_mutex);   // first reader blocks writers
signal(mutex);
// Reading is performed
wait(mutex);
read_count--;
if (read_count == 0)
signal(rw_mutex); // last reader releases writer
signal(mutex);
} while(true);
Writer Process
do {
wait(rw_mutex);
// Writing is performed
signal(rw_mutex);
} while(true);
How Synchronization is Achieved
• Multiple Readers Allowed:
Readers can access the data simultaneously since they do not
modify it
• Writer Gets Exclusive Access:
rw_mutex ensures only one writer can access the resource and
blocks readers during writing
• Reader Priority (in this version):
First reader locks the resource; last reader releases it
• Mutual Exclusion:
Writers are mutually exclusive with both readers and other
writers
Conclusion
The semaphore-based solution ensures correct synchronization by
allowing concurrent reading while maintaining exclusive writing,
thus preventing race conditions and ensuring data consistency.
********** 8 **********
--- page 9 ---
Given the following processes (all arriving at time 0 ms)
Process   Burst Time (ms)
P1   6
P2   8
P3   3
P4   5
a) Apply Round Robin Scheduling (Time Quantum = 2 ms). Draw the
Gantt Chart and compute Average Waiting Time and Average Turnaround
Time. (4 Marks)
b) Apply First Come First Serve (FCFS) scheduling. Draw the Gantt Chart
and compute Average Waiting Time and Average Turnaround Time. (4
Marks)
c) Compare both algorithms based on the results obtained. (2 Marks)
Given Processes (All AT = 0)
Bur
Pro   st
cess Tim
e
P1 6
P2 8
P3 3
P4 5
## a) Round Robin (Time Quantum = 2 ms)
Gantt Chart:
0–2 P1 | 2–4 P2 | 4–6 P3 | 6–8 P4 |
8–10 P1 | 10–12 P2 | 12–13 P3 | 13–15 P4 |
15–17 P1 | 17–19 P2 | 19–20 P4 | 20–22 P2
Completion Time (CT):
Pro
CT
cess
P1 17
P2 22
P3 13
P4 20
********** 9 **********
--- page 10 ---
Turnaround Time (TAT = CT – AT)
Pro
TAT
cess
P1 17
P2 22
P3 13
P4 20
Waiting Time (WT = TAT – BT)
Pro
WT
cess
P1 11
P2 14
P3 10
P4 15
Average Times:
• Avg WT = (11 + 14 + 10 + 15) / 4 = 12.5
• Avg TAT = (17 + 22 + 13 + 20) / 4 = 18
## b) FCFS Scheduling
Gantt Chart:
0–6 P1 | 6–14 P2 | 14–17 P3 | 17–22 P4
Completion Time (CT):
Pro
CT
cess
P1 6
P2 14
P3 17
P4 22
Turnaround Time (TAT):
Pro
TAT
cess
P1 6
P2 14
P3 17
P4 22
Waiting Time (WT):
********** 10 **********
--- page 11 ---
Pro
WT
cess
P1 0
P2 6
P3 14
P4 17
Average Times:
• Avg WT = (0 + 6 + 14 + 17) / 4 = 9.25
• Avg TAT = (6 + 14 + 17 + 22) / 4 = 14.75
## c) Comparison
• FCFS has lower Average Waiting Time (9.25 < 12.5)
• FCFS has lower Average Turnaround Time (14.75 < 18)
• Round Robin provides better response time but higher
waiting time
a.   Explain deadlock and its four necessary conditions. Discuss techniques
to handle deadlock including prevention, avoidance, detection, and
recovery. (10 Marks)
Deadlock
Definition
A deadlock is a situation in an operating system where a group of
b.   processes are blocked indefinitely, each waiting for a resource held by
another process in the group.
Q4   Necessary Conditions for Deadlock
(All four must occur simultaneously)
CO-2 and
CO-3;
1. Mutual Exclusion   [20]
SO-2;
o At least one resource is non-shareable, i.e., only one
BL-3
process can use it at a time.
and BL-4   2. Hold and Wait
o A process holding one or more resources is waiting for
additional resources.
3. No Preemption
o Resources cannot be forcibly taken; they must be
released voluntarily.
4. Circular Wait
o A set of processes forms a circular chain, where each
process is waiting for a resource held by the next.
Techniques to Handle Deadlock
********** 11 **********
--- page 12 ---
1. Deadlock Prevention
• Ensures that at least one of the necessary conditions is
eliminated.
• Methods:
o Remove mutual exclusion (if possible)
o Avoid hold and wait (request all resources at once)
o Allow preemption of resources
o Break circular wait (impose ordering of resources)
2. Deadlock Avoidance
• System checks resource allocation dynamically to avoid unsafe
states.
• Uses algorithms like Banker’s Algorithm.
•   Allocates resources only if the system remains in a safe state.
3. Deadlock Detection
• Allows deadlock to occur and then detects it.
• Techniques:
o Resource Allocation Graph (for single instance)
o Detection algorithms (for multiple instances)
4. Deadlock Recovery
• Once detected, system takes action:
o Terminate processes (all or one by one)
o Resource preemption (take resources and reassign)
o Rollback processes to a safe state
Consider the page reference string: (10 Marks)
3, 1, 2, 0, 3, 1, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 4, 3, 2, 1
i) Calculate the number of page faults using:
• FIFO
• LRU
• OPTIMAL
(Assume 3 frames)
ii) Identify the best algorithm and justify your answer.
Given:
********** 12 **********
--- page 13 ---
Page Reference String:
3, 1, 2, 0, 3, 1, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 4, 3, 2, 1
Number of Frames = 3
i) Page Fault Calculation
1. FIFO (First-In First-Out)
• Replace the oldest page first.
Page Faults = 15
2. LRU (Least Recently Used)
• Replace the page that has not been used for the longest time.
Page Faults = 12
3. OPTIMAL
• Replace the page that will not be used for the longest time in
future.
Page Faults = 9
ii) Best Algorithm
👉 OPTIMAL is the best algorithm
Justification:
•   It gives the minimum number of page faults (9).
•   It uses future knowledge, so it is theoretically optimal.
• However, it is not practical in real systems because future
references are unknown.
•   In practice, LRU is preferred as it approximates OPTIMAL.
Final Answer Summary
Algorithm   Page Faults
FIFO   15
LRU   12
OPTIMAL   9 ✅
********** 13 **********
--- page 14 ---
a.   Explain the Paging memory management technique.
Describe how paging eliminates the problem of external fragmentation
and explain the address translation mechanism with a neat diagram.
(10M)
Paging Memory Management Technique
Definition
b.
Paging is a memory management technique in which:
• Logical memory is divided into fixed-size pages
•   Physical memory is divided into fixed-size frames
• Pages are mapped to frames using a page table
Working of Paging
• A logical address is divided into:
o Page Number (p) → used to index the page table
o Offset (d) → specifies location within the page
Q5   • The page table maps page → frame
•   Physical address = Frame Number + Offset
CO-2 and
CO3; SO-
[20]
2;   Elimination of External Fragmentation
BL-3
and BL-4   •   In paging, memory is allocated in fixed-size blocks
• Any free frame can be assigned to any page
• Hence, no need for contiguous memory allocation
👉 Therefore:
• External fragmentation is eliminated
• Only internal fragmentation may occur (unused space within a
frame)
Address Translation Mechanism
Steps:
1. CPU generates a logical address (p, d)
2. Page number (p) is used to index the page table
3. Corresponding frame number (f) is obtained
4. Physical address is formed as (f, d)
Diagram (Conceptual)
Logical Address
┌──────────────┐
********** 14 **********
--- page 15 ---
│ Page | Offset│
└──────────────┘
↓
Page Table
(maps Page → Frame)
↓
┌──────────────┐
│Frame | Offset│
└──────────────┘
= Physical Address
↓
Physical Memory
Advantages
✔ Eliminates external fragmentation
✔ Efficient memory utilization
✔ Easy allocation of memory
Disadvantages
✖ May cause internal fragmentation
✖ Requires additional memory for page table
✖ Extra overhead in address translation
Conclusion
Paging provides an efficient way to manage memory by dividing it into
fixed-size units, eliminating external fragmentation and enabling
flexible memory allocation.
Consider the following snapshot of a system:
Process Allocation Max (A B   Available (A B
(A B C)   C)   C)
P0   0 1 0   7 5 3   3 3 2
P1   2 0 0   3 2 2   —
P2   3 0 2   9 0 2   —
P3   2 1 1   2 2 2   —
P4   0 0 2   4 3 3   —
Answer the following using Banker’s Algorithm:
1. Find the Need Matrix
2. Determine whether the system is in a safe state. If yes, write the
safe sequence
3.   If a request from process P1 (1, 0, 2) arrives, can it be granted
immediately? Justify
1. Need Matrix (Need = Max – Allocation)
********** 15 **********
--- page 16 ---
Allo
cati Max Nee
Pro
on (A B d (A
cess
(A B C) B C)
C)
0 1 7 5 7 4
P0
0   3   3
2 0 3 2 1 2
P1
0   2   2
3 0 9 0 6 0
P2
2   2   0
2 1 2 2 0 1
P3
1   2   1
0 0 4 3 4 3
P4
2   3   1
2. Safe State Check
Available = (3, 3, 2)
Step-wise:
• P1 → Need (1,2,2) ≤ (3,3,2) ✔ → New Available = (5,3,2)
• P3 → Need (0,1,1) ≤ (5,3,2) ✔ → New Available = (7,4,3)
• P4 → Need (4,3,1) ≤ (7,4,3) ✔ → New Available = (7,4,5)
• P0 → Need (7,4,3) ≤ (7,4,5) ✔ → New Available = (7,5,5)
• P2 → Need (6,0,0) ≤ (7,5,5) ✔
Safe Sequence:
P1 → P3 → P4 → P0 → P2
👉 System is in a SAFE state
3. Request by P1 = (1, 0, 2)
Check 1: Request ≤ Need
(1,0,2) ≤ (1,2,2) ✔
Check 2: Request ≤ Available
(1,0,2) ≤ (3,3,2) ✔
New Available after allocation:
(3,3,2) – (1,0,2) = (2,3,0)
Check Safe State Again:
• P1 → Need becomes (0,2,0) ≤ (2,3,0) ✔ → Available = (5,3,0)
• P3 → (0,1,1) ✖ (fails due to C=1 > 0)
• P2 → (6,0,0) ✖
• P4 → (4,3,1) ✖
********** 16 **********
--- page 17 ---
• P0 → (7,4,3) ✖
👉 No further process can proceed
Final Answer:
•
a.   Explain the concept of File Management in an Operating System.
Discuss different file organization methods and explain how files are
stored and accessed in secondary storage.
File Management in an Operating System
Concept
File Management is a component of the operating system responsible
for creating, storing, organizing, accessing, and protecting files on
secondary storage devices such as disks.
A file is a collection of related data stored on secondary storage and
b.   identified by a unique name.
Functions of File Management
•   File creation and deletion
•   File reading and writing
•   Directory management
• Access control and protection
Q6   • Storage allocation and space management
CO-3;
SO-2;   [20]
BL-2   File Organization Methods
1. Sequential Organization
and BL-4
• Data is stored in a linear sequence
• Access is done one record after another
Advantages:
• Simple and efficient for batch processing
Disadvantages:
• Slow for random access
2. Direct (Random) Organization
• Data is accessed using direct address or index
• Any record can be accessed directly
Advantages:
********** 17 **********
--- page 18 ---
•   Fast access
Disadvantages:
• Requires more complex implementation
3. Indexed Organization
• Uses an index table to locate records
• Combines features of sequential and direct access
Advantages:
•   Efficient searching
• Supports both sequential and random access
Disadvantages:
• Extra storage needed for index
File Storage in Secondary Storage
Files are stored on disks using different allocation methods:
1. Contiguous Allocation
•   File occupies continuous blocks
•   Fast access
2. Linked Allocation
•   File blocks are scattered but linked together
• No external fragmentation
3. Indexed Allocation
• Uses an index block containing addresses of all file blocks
•   Efficient and flexible
File Access Methods
• Sequential Access → Read/write in order
• Direct Access → Jump to any block directly
• Indexed Access → Use index to locate data
********** 18 **********
--- page 19 ---
Consider the following disk request queue (0–199):
95, 180, 34, 119, 11, 123, 62, 64
Initial head position = 50
Tasks:
1. Apply FCFS and SSTF disk scheduling algorithms
2. Show the order of execution
3. Calculate the total head movement
4. Identify which algorithm performs better and justify.
Given:
Request Queue: 95, 180, 34, 119, 11, 123, 62, 64
Initial Head Position = 50
## 1. FCFS (First Come First Serve)
Order of Execution:
50 → 95 → 180 → 34 → 119 → 11 → 123 → 62 → 64
Head Movements:
Dist
Mo
anc
ve
e
50
→ 45
95
95
→ 85
180
180
→ 146
34
34
→ 85
119
119
→ 108
11
11
→ 112
123
123
→ 61
62
********** 19 **********
--- page 20 ---
62
→ 2
64
Total Head Movement:
45 + 85 + 146 + 85 + 108 + 112 + 61 + 2 = 644
## 2. SSTF (Shortest Seek Time First)
Order of Execution:
50 → 62 → 64 → 34 → 11 → 95 → 119 → 123 → 180
Head Movements:
Move   Distance
50 → 62   12
62 → 64   2
64 → 34   30
34 → 11   23
11 → 95   84
95 → 119 24
119 → 123 4
123 → 180 57
Total Head Movement:
12 + 2 + 30 + 23 + 84 + 24 + 4 + 57 = 236
## 3. Comparison
• FCFS Total Movement = 644
• SSTF Total Movement = 236
Final Answer:
👉 SSTF performs better because it minimizes total head movement,
leading to faster disk access compared to FCFS.
Select any 4:
Q7   1. Explain any two Operating System services with suitable
CO-   examples.
1,CO2   Operating System Services
and CO3;   [20]
1. Process Management
SO-2;
The OS manages the creation, scheduling, and termination of processes.
BL-2
It allocates CPU time to processes and ensures smooth execution.
and BL-3   Example:
When multiple applications (e.g., browser, text editor) are running, the
OS schedules them using CPU scheduling algorithms.
********** 20 **********
--- page 21 ---
2. File Management
The OS handles file operations such as creation, deletion, reading,
writing, and organization of files in directories.
Example:
Creating a file, saving it, renaming it, or deleting it using the file
system.
2. What is a Process Control Block (PCB)? Explain its
components.
Process Control Block (PCB)
Definition:
A Process Control Block (PCB) is a data structure used by the
operating system to store all information about a process. It is created
when a process is initiated and deleted when the process terminates.
Components of PCB
1. Process ID (PID)
o Unique identifier assigned to each process
2. Process State
o Current state of the process (New, Ready, Running,
Waiting, Terminated)
3. Program Counter
o Address of the next instruction to be executed
4. CPU Registers
o Stores values of CPU registers (accumulator, index
registers, etc.) during context switching
5. CPU Scheduling Information
o Includes priority, scheduling queue pointers, etc.
6. Memory Management Information
o Information about memory allocation such as base/limit
registers or page tables
7. I/O Status Information
o List of I/O devices allocated and open files
8. Accounting Information
o CPU usage, execution time, process limits
3. What is a deadlock? Explain the concept of a Wait-For Graph.
Deadlock
Definition:
A deadlock is a situation in which a group of processes are blocked
indefinitely, each waiting for a resource held by another process in the
group.
Wait-For Graph (WFG)
********** 21 **********
--- page 22 ---
Concept:
A Wait-For Graph is a directed graph used to detect deadlocks in a
system with single-instance resources.
• Nodes represent processes
• A directed edge Pi → Pj indicates that process Pi is waiting for
a resource held by Pj
Working:
• Convert the Resource Allocation Graph (RAG) into a Wait-
For Graph by removing resource nodes
•   If the graph contains a cycle, then a deadlock exists
•   If there is no cycle, the system is deadlock-free
Example:
If:
• P1 is waiting for P2
• P2 is waiting for P3
• P3 is waiting for P1
Then a cycle is formed:
P1 → P2 → P3 → P1 → Deadlock exists
4. Define seek time and rotational latency in disk systems.
Seek Time and Rotational Latency
Seek Time
Seek time is the time required for the disk arm (read/write head) to
move from its current position to the desired track where the data is
stored.
Rotational Latency
Rotational latency is the time taken for the disk to rotate so that the
required sector aligns under the read/write head.
5. What is a directory? Explain different directory operations in an
operating system.
Directory in an Operating System
Definition:
A directory is a special file that stores information about files and
subdirectories, helping in organizing and managing files in a
hierarchical structure.
Directory Operations
1. Create Directory
o Creates a new directory in the file system
********** 22 **********
--- page 23 ---
2. Delete Directory
o Removes an existing directory (usually only if it is
empty)
3. Open Directory
o Allows access to the directory for reading its contents
4. Close Directory
o Closes the directory after operations are completed
5. Search Directory
o Searches for a file or subdirectory within the directory
6. List Directory Contents
o Displays all files and subdirectories present
7. Rename Directory/File
o Changes the name of a directory or file
8. Traverse Directory
o Allows navigation through the directory structure
********** 23 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 7b55faccca09

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_IT_7001/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (23 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech
(IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 11 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain the layered structure of an Operating System with suitable
explanation.
Layered Structure of an Operating System
The layered structure of an Operating System is a design approach
where the OS is divided into multiple layers, each performing specific
functions.
Each layer uses services of the lower layer and provides services to the
layer above.
Typical Layers:
CO-1 ;
SO-2 ;   1. Hardware – Physical components like CPU, memory, I/O devices   5
BL-2   2. Kernel – Manages processes, memory, and devices
3. System Call Interface – Connects user programs with kernel
4. System Programs – Utilities like compilers and editors
5. User Interface – CLI/GUI for user interaction
Advantages:
• Easy to design and debug
•   Better modularity and security
********** 1 **********
--- page 2 ---
Disadvantages:
•   Performance overhead due to multiple layers
b.   Define a process and describe its different states with a diagram.
Definition of a Process
A process is a program in execution. It is an active entity that includes
not only the program code but also its current activity, such as the
program counter, CPU registers, stack, and data.
Different States of a Process
CO-2 ;
SO- 2;   5
BL-2
A process passes through the following states during its lifecycle:
1. New (Created)
o The process is being created.
o Resources are allocated, but execution has not yet started.
2. Ready
o The process is ready to run and waiting for CPU
allocation.
o   It resides in the ready queue.
3. Running
o The process is currently executing on the CPU.
o Only one process can be in this state per CPU at a time.
4. Waiting (Blocked)
o The process is waiting for some event to occur (e.g., I/O
completion).
o   It cannot proceed until the event is completed.
5. Terminated (Exit)
o The process has finished execution.
o The OS deallocates its resources.
********** 2 **********
--- page 3 ---
State Transitions (Brief)
• New → Ready (admitted by OS)
• Ready → Running (CPU scheduler selects)
• Running → Waiting (I/O request)
• Waiting → Ready (I/O completion)
• Running → Terminated (execution finished)
c.   What is a race condition? Explain its impact with an example.
Race Condition (5 Marks Answer)
A race condition occurs when two or more processes/threads access
and modify shared data simultaneously, and the final result depends
on the order of execution.
Impact
• Produces incorrect or inconsistent results
CO-3 ;   • May cause data corruption
SO- 2;   • Leads to unpredictable system behavior
5
BL-2
and BL-3
Example
Consider a shared variable count = 5.
Two processes P1 and P2 increment it at the same time.
• Both read count = 5
• Both increment to 6
• Both write back 6
👉 Final value becomes 6 instead of 7 → incorrect result
d.   Define deadlock and briefly explain its necessary conditions.
Here is a crisp 5-mark answer (exam-ready) 👇
Deadlock
Definition:
A deadlock is a situation in an operating system where a set of
processes are blocked indefinitely, each waiting for a resource held by
CO- 3;   another process.
SO- 2;   5
BL-2   Necessary Conditions for Deadlock
(All four must occur simultaneously)
1. Mutual Exclusion
o At least one resource is non-shareable (only one process
can use it at a time)
2. Hold and Wait
o A process holding at least one resource is waiting for
additional resources
********** 3 **********
--- page 4 ---
3. No Preemption
o Resources cannot be forcibly taken; they must be
released voluntarily
4. Circular Wait
o A circular chain of processes exists where each process is
waiting for a resource held by the next process
a. Explain the Producer–Consumer (Bounded Buffer) problem. Write a
semaphore-based solution and explain synchronization. (10 Marks)
Producer–Consumer (Bounded Buffer) Problem
b.   The Producer–Consumer problem is a synchronization problem
where a producer process generates data and places it in a fixed-size
buffer, while a consumer process removes data from the buffer. Since
the buffer is bounded, the producer must wait if the buffer is full, and
the consumer must wait if the buffer is empty.
Semaphore-Based Solution
Let:
• mutex = 1 (ensures mutual exclusion)
• empty = N (number of empty slots in buffer)
• full = 0 (number of filled slots)
Q2
CO-2;
SO-2;   Producer   [20]
BL-3   do {
and BL-4   wait(empty);
wait(mutex);
// insert item into buffer
signal(mutex);
signal(full);
} while(true);
Consumer
do {
wait(full);
wait(mutex);
// remove item from buffer
signal(mutex);
signal(empty);
} while(true);
********** 4 **********
--- page 5 ---
Synchronization Explanation
• mutex ensures only one process accesses the buffer at a time
(mutual exclusion).
• empty prevents the producer from adding data when the buffer
is full.
• full prevents the consumer from removing data when the
buffer is empty.
• wait() and signal() operations coordinate execution and
avoid race conditions.
Conclusion
The semaphore-based solution ensures proper synchronization between
producer and consumer, preventing buffer overflow, underflow, and
race conditions.
Consider the following processes:
Process Arrival Time Burst Time
P1   0   6
P2   1   4
P3   2   5
P4   3   3
i) Apply Shortest Remaining Time First (Preemptive) scheduling. Draw
the Gantt Chart and calculate Average Waiting Time and Average
Turnaround Time. (4 Marks)
ii) Apply Shortest Job First (Non-Preemptive) scheduling. Draw the
Gantt Chart and calculate Average Waiting Time and Average
Turnaround Time. (4 Marks)
iii) Compare both algorithms based on Average Waiting Time and
Turnaround Time. (2 Marks)
Given Processes
Pro
AT BT
cess
P1 0   6
P2 1   4
P3 2   5
P4 3   3
## i) SRTF (Preemptive)
Gantt Chart:
0–1 P1 | 1–5 P2 | 5–8 P4 | 8–13 P3 | 13–18 P1
********** 5 **********
--- page 6 ---
Completion Time (CT):
Pro
CT
cess
P1 18
P2 5
P3 13
P4 8
Turnaround Time (TAT = CT – AT)
Pro
TAT
cess
P1 18
P2 4
P3 11
P4 5
Waiting Time (WT = TAT – BT)
Pro
WT
cess
P1 12
P2 0
P3 6
P4 2
Average Times:
• Avg WT = (12 + 0 + 6 + 2) / 4 = 5
• Avg TAT = (18 + 4 + 11 + 5) / 4 = 9.5
## ii) SJF (Non-Preemptive)
Gantt Chart:
0–6 P1 | 6–9 P4 | 9–13 P2 | 13–18 P3
Completion Time (CT):
Pro
CT
cess
P1 6
P2 13
P3 18
P4 9
********** 6 **********
--- page 7 ---
Turnaround Time (TAT):
Pro
TAT
cess
P1 6
P2 12
P3 16
P4 6
Waiting Time (WT):
Pro
WT
cess
P1 0
P2 8
P3 11
P4 3
Average Times:
• Avg WT = (0 + 8 + 11 + 3) / 4 = 5.5
• Avg TAT = (6 + 12 + 16 + 6) / 4 = 10
## iii) Comparison
• SRTF gives lower Average Waiting Time (5 < 5.5)
• SRTF gives lower Average Turnaround Time (9.5 < 10)
• Hence, SRTF performs better than SJF (Non-Preemptive) for
this set.
a.   Discuss the Readers–Writer problem. Explain its semaphore-based
solution and describe how synchronization is achieved when multiple
readers and a single writer access shared data. (10 Marks)
Readers–Writers Problem
The Readers–Writers problem is a classic synchronization problem
Q3   where:
CO-2;   b.   • Multiple readers can read shared data simultaneously   [20]
SO-2;   • A writer must have exclusive access to the shared data
BL-3 and
BL-4   👉 The challenge is to ensure:
• No reader reads while a writer is writing
• No writer writes while readers are reading
Semaphore-Based Solution
********** 7 **********
--- page 8 ---
Shared Variables:
• mutex = 1 → protects read count
• rw_mutex = 1 → controls access to shared resource
• read_count = 0 → number of active readers
Reader Process
do {
wait(mutex);
read_count++;
if (read_count == 1)
wait(rw_mutex);   // first reader blocks writers
signal(mutex);
// Reading is performed
wait(mutex);
read_count--;
if (read_count == 0)
signal(rw_mutex); // last reader releases writer
signal(mutex);
} while(true);
Writer Process
do {
wait(rw_mutex);
// Writing is performed
signal(rw_mutex);
} while(true);
How Synchronization is Achieved
• Multiple Readers Allowed:
Readers can access the data simultaneously since they do not
modify it
• Writer Gets Exclusive Access:
rw_mutex ensures only one writer can access the resource and
blocks readers during writing
• Reader Priority (in this version):
First reader locks the resource; last reader releases it
• Mutual Exclusion:
Writers are mutually exclusive with both readers and other
writers
Conclusion
The semaphore-based solution ensures correct synchronization by
allowing concurrent reading while maintaining exclusive writing,
thus preventing race conditions and ensuring data consistency.
********** 8 **********
--- page 9 ---
Given the following processes (all arriving at time 0 ms)
Process   Burst Time (ms)
P1   6
P2   8
P3   3
P4   5
a) Apply Round Robin Scheduling (Time Quantum = 2 ms). Draw the
Gantt Chart and compute Average Waiting Time and Average Turnaround
Time. (4 Marks)
b) Apply First Come First Serve (FCFS) scheduling. Draw the Gantt Chart
and compute Average Waiting Time and Average Turnaround Time. (4
Marks)
c) Compare both algorithms based on the results obtained. (2 Marks)
Given Processes (All AT = 0)
Bur
Pro   st
cess Tim
e
P1 6
P2 8
P3 3
P4 5
## a) Round Robin (Time Quantum = 2 ms)
Gantt Chart:
0–2 P1 | 2–4 P2 | 4–6 P3 | 6–8 P4 |
8–10 P1 | 10–12 P2 | 12–13 P3 | 13–15 P4 |
15–17 P1 | 17–19 P2 | 19–20 P4 | 20–22 P2
Completion Time (CT):
Pro
CT
cess
P1 17
P2 22
P3 13
P4 20
********** 9 **********
--- page 10 ---
Turnaround Time (TAT = CT – AT)
Pro
TAT
cess
P1 17
P2 22
P3 13
P4 20
Waiting Time (WT = TAT – BT)
Pro
WT
cess
P1 11
P2 14
P3 10
P4 15
Average Times:
• Avg WT = (11 + 14 + 10 + 15) / 4 = 12.5
• Avg TAT = (17 + 22 + 13 + 20) / 4 = 18
## b) FCFS Scheduling
Gantt Chart:
0–6 P1 | 6–14 P2 | 14–17 P3 | 17–22 P4
Completion Time (CT):
Pro
CT
cess
P1 6
P2 14
P3 17
P4 22
Turnaround Time (TAT):
Pro
TAT
cess
P1 6
P2 14
P3 17
P4 22
Waiting Time (WT):
********** 10 **********
--- page 11 ---
Pro
WT
cess
P1 0
P2 6
P3 14
P4 17
Average Times:
• Avg WT = (0 + 6 + 14 + 17) / 4 = 9.25
• Avg TAT = (6 + 14 + 17 + 22) / 4 = 14.75
## c) Comparison
• FCFS has lower Average Waiting Time (9.25 < 12.5)
• FCFS has lower Average Turnaround Time (14.75 < 18)
• Round Robin provides better response time but higher
waiting time
a.   Explain deadlock and its four necessary conditions. Discuss techniques
to handle deadlock including prevention, avoidance, detection, and
recovery. (10 Marks)
Deadlock
Definition
A deadlock is a situation in an operating system where a group of
b.   processes are blocked indefinitely, each waiting for a resource held by
another process in the group.
Q4   Necessary Conditions for Deadlock
(All four must occur simultaneously)
CO-2 and
CO-3;
1. Mutual Exclusion   [20]
SO-2;
o At least one resource is non-shareable, i.e., only one
BL-3
process can use it at a time.
and BL-4   2. Hold and Wait
o A process holding one or more resources is waiting for
additional resources.
3. No Preemption
o Resources cannot be forcibly taken; they must be
released voluntarily.
4. Circular Wait
o A set of processes forms a circular chain, where each
process is waiting for a resource held by the next.
Techniques to Handle Deadlock
********** 11 **********
--- page 12 ---
1. Deadlock Prevention
• Ensures that at least one of the necessary conditions is
eliminated.
• Methods:
o Remove mutual exclusion (if possible)
o Avoid hold and wait (request all resources at once)
o Allow preemption of resources
o Break circular wait (impose ordering of resources)
2. Deadlock Avoidance
• System checks resource allocation dynamically to avoid unsafe
states.
• Uses algorithms like Banker’s Algorithm.
•   Allocates resources only if the system remains in a safe state.
3. Deadlock Detection
• Allows deadlock to occur and then detects it.
• Techniques:
o Resource Allocation Graph (for single instance)
o Detection algorithms (for multiple instances)
4. Deadlock Recovery
• Once detected, system takes action:
o Terminate processes (all or one by one)
o Resource preemption (take resources and reassign)
o Rollback processes to a safe state
Consider the page reference string: (10 Marks)
3, 1, 2, 0, 3, 1, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 4, 3, 2, 1
i) Calculate the number of page faults using:
• FIFO
• LRU
• OPTIMAL
(Assume 3 frames)
ii) Identify the best algorithm and justify your answer.
Given:
********** 12 **********
--- page 13 ---
Page Reference String:
3, 1, 2, 0, 3, 1, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 4, 3, 2, 1
Number of Frames = 3
i) Page Fault Calculation
1. FIFO (First-In First-Out)
• Replace the oldest page first.
Page Faults = 15
2. LRU (Least Recently Used)
• Replace the page that has not been used for the longest time.
Page Faults = 12
3. OPTIMAL
• Replace the page that will not be used for the longest time in
future.
Page Faults = 9
ii) Best Algorithm
👉 OPTIMAL is the best algorithm
Justification:
•   It gives the minimum number of page faults (9).
•   It uses future knowledge, so it is theoretically optimal.
• However, it is not practical in real systems because future
references are unknown.
•   In practice, LRU is preferred as it approximates OPTIMAL.
Final Answer Summary
Algorithm   Page Faults
FIFO   15
LRU   12
OPTIMAL   9 ✅
********** 13 **********
--- page 14 ---
a.   Explain the Paging memory management technique.
Describe how paging eliminates the problem of external fragmentation
and explain the address translation mechanism with a neat diagram.
(10M)
Paging Memory Management Technique
Definition
b.
Paging is a memory management technique in which:
• Logical memory is divided into fixed-size pages
•   Physical memory is divided into fixed-size frames
• Pages are mapped to frames using a page table
Working of Paging
• A logical address is divided into:
o Page Number (p) → used to index the page table
o Offset (d) → specifies location within the page
Q5   • The page table maps page → frame
•   Physical address = Frame Number + Offset
CO-2 and
CO3; SO-
[20]
2;   Elimination of External Fragmentation
BL-3
and BL-4   •   In paging, memory is allocated in fixed-size blocks
• Any free frame can be assigned to any page
• Hence, no need for contiguous memory allocation
👉 Therefore:
• External fragmentation is eliminated
• Only internal fragmentation may occur (unused space within a
frame)
Address Translation Mechanism
Steps:
1. CPU generates a logical address (p, d)
2. Page number (p) is used to index the page table
3. Corresponding frame number (f) is obtained
4. Physical address is formed as (f, d)
Diagram (Conceptual)
Logical Address
┌──────────────┐
********** 14 **********
--- page 15 ---
│ Page | Offset│
└──────────────┘
↓
Page Table
(maps Page → Frame)
↓
┌──────────────┐
│Frame | Offset│
└──────────────┘
= Physical Address
↓
Physical Memory
Advantages
✔ Eliminates external fragmentation
✔ Efficient memory utilization
✔ Easy allocation of memory
Disadvantages
✖ May cause internal fragmentation
✖ Requires additional memory for page table
✖ Extra overhead in address translation
Conclusion
Paging provides an efficient way to manage memory by dividing it into
fixed-size units, eliminating external fragmentation and enabling
flexible memory allocation.
Consider the following snapshot of a system:
Process Allocation Max (A B   Available (A B
(A B C)   C)   C)
P0   0 1 0   7 5 3   3 3 2
P1   2 0 0   3 2 2   —
P2   3 0 2   9 0 2   —
P3   2 1 1   2 2 2   —
P4   0 0 2   4 3 3   —
Answer the following using Banker’s Algorithm:
1. Find the Need Matrix
2. Determine whether the system is in a safe state. If yes, write the
safe sequence
3.   If a request from process P1 (1, 0, 2) arrives, can it be granted
immediately? Justify
1. Need Matrix (Need = Max – Allocation)
********** 15 **********
--- page 16 ---
Allo
cati Max Nee
Pro
on (A B d (A
cess
(A B C) B C)
C)
0 1 7 5 7 4
P0
0   3   3
2 0 3 2 1 2
P1
0   2   2
3 0 9 0 6 0
P2
2   2   0
2 1 2 2 0 1
P3
1   2   1
0 0 4 3 4 3
P4
2   3   1
2. Safe State Check
Available = (3, 3, 2)
Step-wise:
• P1 → Need (1,2,2) ≤ (3,3,2) ✔ → New Available = (5,3,2)
• P3 → Need (0,1,1) ≤ (5,3,2) ✔ → New Available = (7,4,3)
• P4 → Need (4,3,1) ≤ (7,4,3) ✔ → New Available = (7,4,5)
• P0 → Need (7,4,3) ≤ (7,4,5) ✔ → New Available = (7,5,5)
• P2 → Need (6,0,0) ≤ (7,5,5) ✔
Safe Sequence:
P1 → P3 → P4 → P0 → P2
👉 System is in a SAFE state
3. Request by P1 = (1, 0, 2)
Check 1: Request ≤ Need
(1,0,2) ≤ (1,2,2) ✔
Check 2: Request ≤ Available
(1,0,2) ≤ (3,3,2) ✔
New Available after allocation:
(3,3,2) – (1,0,2) = (2,3,0)
Check Safe State Again:
• P1 → Need becomes (0,2,0) ≤ (2,3,0) ✔ → Available = (5,3,0)
• P3 → (0,1,1) ✖ (fails due to C=1 > 0)
• P2 → (6,0,0) ✖
• P4 → (4,3,1) ✖
********** 16 **********
--- page 17 ---
• P0 → (7,4,3) ✖
👉 No further process can proceed
Final Answer:
•
a.   Explain the concept of File Management in an Operating System.
Discuss different file organization methods and explain how files are
stored and accessed in secondary storage.
File Management in an Operating System
Concept
File Management is a component of the operating system responsible
for creating, storing, organizing, accessing, and protecting files on
secondary storage devices such as disks.
A file is a collection of related data stored on secondary storage and
b.   identified by a unique name.
Functions of File Management
•   File creation and deletion
•   File reading and writing
•   Directory management
• Access control and protection
Q6   • Storage allocation and space management
CO-3;
SO-2;   [20]
BL-2   File Organization Methods
1. Sequential Organization
and BL-4
• Data is stored in a linear sequence
• Access is done one record after another
Advantages:
• Simple and efficient for batch processing
Disadvantages:
• Slow for random access
2. Direct (Random) Organization
• Data is accessed using direct address or index
• Any record can be accessed directly
Advantages:
********** 17 **********
--- page 18 ---
•   Fast access
Disadvantages:
• Requires more complex implementation
3. Indexed Organization
• Uses an index table to locate records
• Combines features of sequential and direct access
Advantages:
•   Efficient searching
• Supports both sequential and random access
Disadvantages:
• Extra storage needed for index
File Storage in Secondary Storage
Files are stored on disks using different allocation methods:
1. Contiguous Allocation
•   File occupies continuous blocks
•   Fast access
2. Linked Allocation
•   File blocks are scattered but linked together
• No external fragmentation
3. Indexed Allocation
• Uses an index block containing addresses of all file blocks
•   Efficient and flexible
File Access Methods
• Sequential Access → Read/write in order
• Direct Access → Jump to any block directly
• Indexed Access → Use index to locate data
********** 18 **********
--- page 19 ---
Consider the following disk request queue (0–199):
95, 180, 34, 119, 11, 123, 62, 64
Initial head position = 50
Tasks:
1. Apply FCFS and SSTF disk scheduling algorithms
2. Show the order of execution
3. Calculate the total head movement
4. Identify which algorithm performs better and justify.
Given:
Request Queue: 95, 180, 34, 119, 11, 123, 62, 64
Initial Head Position = 50
## 1. FCFS (First Come First Serve)
Order of Execution:
50 → 95 → 180 → 34 → 119 → 11 → 123 → 62 → 64
Head Movements:
Dist
Mo
anc
ve
e
50
→ 45
95
95
→ 85
180
180
→ 146
34
34
→ 85
119
119
→ 108
11
11
→ 112
123
123
→ 61
62
********** 19 **********
--- page 20 ---
62
→ 2
64
Total Head Movement:
45 + 85 + 146 + 85 + 108 + 112 + 61 + 2 = 644
## 2. SSTF (Shortest Seek Time First)
Order of Execution:
50 → 62 → 64 → 34 → 11 → 95 → 119 → 123 → 180
Head Movements:
Move   Distance
50 → 62   12
62 → 64   2
64 → 34   30
34 → 11   23
11 → 95   84
95 → 119 24
119 → 123 4
123 → 180 57
Total Head Movement:
12 + 2 + 30 + 23 + 84 + 24 + 4 + 57 = 236
## 3. Comparison
• FCFS Total Movement = 644
• SSTF Total Movement = 236
Final Answer:
👉 SSTF performs better because it minimizes total head movement,
leading to faster disk access compared to FCFS.
Select any 4:
Q7   1. Explain any two Operating System services with suitable
CO-   examples.
1,CO2   Operating System Services
and CO3;   [20]
1. Process Management
SO-2;
The OS manages the creation, scheduling, and termination of processes.
BL-2
It allocates CPU time to processes and ensures smooth execution.
and BL-3   Example:
When multiple applications (e.g., browser, text editor) are running, the
OS schedules them using CPU scheduling algorithms.
********** 20 **********
--- page 21 ---
2. File Management
The OS handles file operations such as creation, deletion, reading,
writing, and organization of files in directories.
Example:
Creating a file, saving it, renaming it, or deleting it using the file
system.
2. What is a Process Control Block (PCB)? Explain its
components.
Process Control Block (PCB)
Definition:
A Process Control Block (PCB) is a data structure used by the
operating system to store all information about a process. It is created
when a process is initiated and deleted when the process terminates.
Components of PCB
1. Process ID (PID)
o Unique identifier assigned to each process
2. Process State
o Current state of the process (New, Ready, Running,
Waiting, Terminated)
3. Program Counter
o Address of the next instruction to be executed
4. CPU Registers
o Stores values of CPU registers (accumulator, index
registers, etc.) during context switching
5. CPU Scheduling Information
o Includes priority, scheduling queue pointers, etc.
6. Memory Management Information
o Information about memory allocation such as base/limit
registers or page tables
7. I/O Status Information
o List of I/O devices allocated and open files
8. Accounting Information
o CPU usage, execution time, process limits
3. What is a deadlock? Explain the concept of a Wait-For Graph.
Deadlock
Definition:
A deadlock is a situation in which a group of processes are blocked
indefinitely, each waiting for a resource held by another process in the
group.
Wait-For Graph (WFG)
********** 21 **********
--- page 22 ---
Concept:
A Wait-For Graph is a directed graph used to detect deadlocks in a
system with single-instance resources.
• Nodes represent processes
• A directed edge Pi → Pj indicates that process Pi is waiting for
a resource held by Pj
Working:
• Convert the Resource Allocation Graph (RAG) into a Wait-
For Graph by removing resource nodes
•   If the graph contains a cycle, then a deadlock exists
•   If there is no cycle, the system is deadlock-free
Example:
If:
• P1 is waiting for P2
• P2 is waiting for P3
• P3 is waiting for P1
Then a cycle is formed:
P1 → P2 → P3 → P1 → Deadlock exists
4. Define seek time and rotational latency in disk systems.
Seek Time and Rotational Latency
Seek Time
Seek time is the time required for the disk arm (read/write head) to
move from its current position to the desired track where the data is
stored.
Rotational Latency
Rotational latency is the time taken for the disk to rotate so that the
required sector aligns under the read/write head.
5. What is a directory? Explain different directory operations in an
operating system.
Directory in an Operating System
Definition:
A directory is a special file that stores information about files and
subdirectories, helping in organizing and managing files in a
hierarchical structure.
Directory Operations
1. Create Directory
o Creates a new directory in the file system
********** 22 **********
--- page 23 ---
2. Delete Directory
o Removes an existing directory (usually only if it is
empty)
3. Open Directory
o Allows access to the directory for reading its contents
4. Close Directory
o Closes the directory after operations are completed
5. Search Directory
o Searches for a file or subdirectory within the directory
6. List Directory Contents
o Displays all files and subdirectories present
7. Rename Directory/File
o Changes the name of a directory or file
8. Traverse Directory
o Allows navigation through the directory structure
********** 23 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper b57df48a4c45

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/MBATech_IT_7041/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (23 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech
(IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 11 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain the layered structure of an Operating System with suitable
explanation.
Layered Structure of an Operating System
The layered structure of an Operating System is a design approach
where the OS is divided into multiple layers, each performing specific
functions.
Each layer uses services of the lower layer and provides services to the
layer above.
Typical Layers:
CO-1 ;
SO-2 ;   1. Hardware – Physical components like CPU, memory, I/O devices   5
BL-2   2. Kernel – Manages processes, memory, and devices
3. System Call Interface – Connects user programs with kernel
4. System Programs – Utilities like compilers and editors
5. User Interface – CLI/GUI for user interaction
Advantages:
• Easy to design and debug
•   Better modularity and security
********** 1 **********
--- page 2 ---
Disadvantages:
•   Performance overhead due to multiple layers
b.   Define a process and describe its different states with a diagram.
Definition of a Process
A process is a program in execution. It is an active entity that includes
not only the program code but also its current activity, such as the
program counter, CPU registers, stack, and data.
Different States of a Process
CO-2 ;
SO- 2;   5
BL-2
A process passes through the following states during its lifecycle:
1. New (Created)
o The process is being created.
o Resources are allocated, but execution has not yet started.
2. Ready
o The process is ready to run and waiting for CPU
allocation.
o   It resides in the ready queue.
3. Running
o The process is currently executing on the CPU.
o Only one process can be in this state per CPU at a time.
4. Waiting (Blocked)
o The process is waiting for some event to occur (e.g., I/O
completion).
o   It cannot proceed until the event is completed.
5. Terminated (Exit)
o The process has finished execution.
o The OS deallocates its resources.
********** 2 **********
--- page 3 ---
State Transitions (Brief)
• New → Ready (admitted by OS)
• Ready → Running (CPU scheduler selects)
• Running → Waiting (I/O request)
• Waiting → Ready (I/O completion)
• Running → Terminated (execution finished)
c.   What is a race condition? Explain its impact with an example.
Race Condition (5 Marks Answer)
A race condition occurs when two or more processes/threads access
and modify shared data simultaneously, and the final result depends
on the order of execution.
Impact
• Produces incorrect or inconsistent results
CO-3 ;   • May cause data corruption
SO- 2;   • Leads to unpredictable system behavior
5
BL-2
and BL-3
Example
Consider a shared variable count = 5.
Two processes P1 and P2 increment it at the same time.
• Both read count = 5
• Both increment to 6
• Both write back 6
👉 Final value becomes 6 instead of 7 → incorrect result
d.   Define deadlock and briefly explain its necessary conditions.
Here is a crisp 5-mark answer (exam-ready) 👇
Deadlock
Definition:
A deadlock is a situation in an operating system where a set of
processes are blocked indefinitely, each waiting for a resource held by
CO- 3;   another process.
SO- 2;   5
BL-2   Necessary Conditions for Deadlock
(All four must occur simultaneously)
1. Mutual Exclusion
o At least one resource is non-shareable (only one process
can use it at a time)
2. Hold and Wait
o A process holding at least one resource is waiting for
additional resources
********** 3 **********
--- page 4 ---
3. No Preemption
o Resources cannot be forcibly taken; they must be
released voluntarily
4. Circular Wait
o A circular chain of processes exists where each process is
waiting for a resource held by the next process
a. Explain the Producer–Consumer (Bounded Buffer) problem. Write a
semaphore-based solution and explain synchronization. (10 Marks)
Producer–Consumer (Bounded Buffer) Problem
b.   The Producer–Consumer problem is a synchronization problem
where a producer process generates data and places it in a fixed-size
buffer, while a consumer process removes data from the buffer. Since
the buffer is bounded, the producer must wait if the buffer is full, and
the consumer must wait if the buffer is empty.
Semaphore-Based Solution
Let:
• mutex = 1 (ensures mutual exclusion)
• empty = N (number of empty slots in buffer)
• full = 0 (number of filled slots)
Q2
CO-2;
SO-2;   Producer   [20]
BL-3   do {
and BL-4   wait(empty);
wait(mutex);
// insert item into buffer
signal(mutex);
signal(full);
} while(true);
Consumer
do {
wait(full);
wait(mutex);
// remove item from buffer
signal(mutex);
signal(empty);
} while(true);
********** 4 **********
--- page 5 ---
Synchronization Explanation
• mutex ensures only one process accesses the buffer at a time
(mutual exclusion).
• empty prevents the producer from adding data when the buffer
is full.
• full prevents the consumer from removing data when the
buffer is empty.
• wait() and signal() operations coordinate execution and
avoid race conditions.
Conclusion
The semaphore-based solution ensures proper synchronization between
producer and consumer, preventing buffer overflow, underflow, and
race conditions.
Consider the following processes:
Process Arrival Time Burst Time
P1   0   6
P2   1   4
P3   2   5
P4   3   3
i) Apply Shortest Remaining Time First (Preemptive) scheduling. Draw
the Gantt Chart and calculate Average Waiting Time and Average
Turnaround Time. (4 Marks)
ii) Apply Shortest Job First (Non-Preemptive) scheduling. Draw the
Gantt Chart and calculate Average Waiting Time and Average
Turnaround Time. (4 Marks)
iii) Compare both algorithms based on Average Waiting Time and
Turnaround Time. (2 Marks)
Given Processes
Pro
AT BT
cess
P1 0   6
P2 1   4
P3 2   5
P4 3   3
## i) SRTF (Preemptive)
Gantt Chart:
0–1 P1 | 1–5 P2 | 5–8 P4 | 8–13 P3 | 13–18 P1
********** 5 **********
--- page 6 ---
Completion Time (CT):
Pro
CT
cess
P1 18
P2 5
P3 13
P4 8
Turnaround Time (TAT = CT – AT)
Pro
TAT
cess
P1 18
P2 4
P3 11
P4 5
Waiting Time (WT = TAT – BT)
Pro
WT
cess
P1 12
P2 0
P3 6
P4 2
Average Times:
• Avg WT = (12 + 0 + 6 + 2) / 4 = 5
• Avg TAT = (18 + 4 + 11 + 5) / 4 = 9.5
## ii) SJF (Non-Preemptive)
Gantt Chart:
0–6 P1 | 6–9 P4 | 9–13 P2 | 13–18 P3
Completion Time (CT):
Pro
CT
cess
P1 6
P2 13
P3 18
P4 9
********** 6 **********
--- page 7 ---
Turnaround Time (TAT):
Pro
TAT
cess
P1 6
P2 12
P3 16
P4 6
Waiting Time (WT):
Pro
WT
cess
P1 0
P2 8
P3 11
P4 3
Average Times:
• Avg WT = (0 + 8 + 11 + 3) / 4 = 5.5
• Avg TAT = (6 + 12 + 16 + 6) / 4 = 10
## iii) Comparison
• SRTF gives lower Average Waiting Time (5 < 5.5)
• SRTF gives lower Average Turnaround Time (9.5 < 10)
• Hence, SRTF performs better than SJF (Non-Preemptive) for
this set.
a.   Discuss the Readers–Writer problem. Explain its semaphore-based
solution and describe how synchronization is achieved when multiple
readers and a single writer access shared data. (10 Marks)
Readers–Writers Problem
The Readers–Writers problem is a classic synchronization problem
Q3   where:
CO-2;   b.   • Multiple readers can read shared data simultaneously   [20]
SO-2;   • A writer must have exclusive access to the shared data
BL-3 and
BL-4   👉 The challenge is to ensure:
• No reader reads while a writer is writing
• No writer writes while readers are reading
Semaphore-Based Solution
********** 7 **********
--- page 8 ---
Shared Variables:
• mutex = 1 → protects read count
• rw_mutex = 1 → controls access to shared resource
• read_count = 0 → number of active readers
Reader Process
do {
wait(mutex);
read_count++;
if (read_count == 1)
wait(rw_mutex);   // first reader blocks writers
signal(mutex);
// Reading is performed
wait(mutex);
read_count--;
if (read_count == 0)
signal(rw_mutex); // last reader releases writer
signal(mutex);
} while(true);
Writer Process
do {
wait(rw_mutex);
// Writing is performed
signal(rw_mutex);
} while(true);
How Synchronization is Achieved
• Multiple Readers Allowed:
Readers can access the data simultaneously since they do not
modify it
• Writer Gets Exclusive Access:
rw_mutex ensures only one writer can access the resource and
blocks readers during writing
• Reader Priority (in this version):
First reader locks the resource; last reader releases it
• Mutual Exclusion:
Writers are mutually exclusive with both readers and other
writers
Conclusion
The semaphore-based solution ensures correct synchronization by
allowing concurrent reading while maintaining exclusive writing,
thus preventing race conditions and ensuring data consistency.
********** 8 **********
--- page 9 ---
Given the following processes (all arriving at time 0 ms)
Process   Burst Time (ms)
P1   6
P2   8
P3   3
P4   5
a) Apply Round Robin Scheduling (Time Quantum = 2 ms). Draw the
Gantt Chart and compute Average Waiting Time and Average Turnaround
Time. (4 Marks)
b) Apply First Come First Serve (FCFS) scheduling. Draw the Gantt Chart
and compute Average Waiting Time and Average Turnaround Time. (4
Marks)
c) Compare both algorithms based on the results obtained. (2 Marks)
Given Processes (All AT = 0)
Bur
Pro   st
cess Tim
e
P1 6
P2 8
P3 3
P4 5
## a) Round Robin (Time Quantum = 2 ms)
Gantt Chart:
0–2 P1 | 2–4 P2 | 4–6 P3 | 6–8 P4 |
8–10 P1 | 10–12 P2 | 12–13 P3 | 13–15 P4 |
15–17 P1 | 17–19 P2 | 19–20 P4 | 20–22 P2
Completion Time (CT):
Pro
CT
cess
P1 17
P2 22
P3 13
P4 20
********** 9 **********
--- page 10 ---
Turnaround Time (TAT = CT – AT)
Pro
TAT
cess
P1 17
P2 22
P3 13
P4 20
Waiting Time (WT = TAT – BT)
Pro
WT
cess
P1 11
P2 14
P3 10
P4 15
Average Times:
• Avg WT = (11 + 14 + 10 + 15) / 4 = 12.5
• Avg TAT = (17 + 22 + 13 + 20) / 4 = 18
## b) FCFS Scheduling
Gantt Chart:
0–6 P1 | 6–14 P2 | 14–17 P3 | 17–22 P4
Completion Time (CT):
Pro
CT
cess
P1 6
P2 14
P3 17
P4 22
Turnaround Time (TAT):
Pro
TAT
cess
P1 6
P2 14
P3 17
P4 22
Waiting Time (WT):
********** 10 **********
--- page 11 ---
Pro
WT
cess
P1 0
P2 6
P3 14
P4 17
Average Times:
• Avg WT = (0 + 6 + 14 + 17) / 4 = 9.25
• Avg TAT = (6 + 14 + 17 + 22) / 4 = 14.75
## c) Comparison
• FCFS has lower Average Waiting Time (9.25 < 12.5)
• FCFS has lower Average Turnaround Time (14.75 < 18)
• Round Robin provides better response time but higher
waiting time
a.   Explain deadlock and its four necessary conditions. Discuss techniques
to handle deadlock including prevention, avoidance, detection, and
recovery. (10 Marks)
Deadlock
Definition
A deadlock is a situation in an operating system where a group of
b.   processes are blocked indefinitely, each waiting for a resource held by
another process in the group.
Q4   Necessary Conditions for Deadlock
(All four must occur simultaneously)
CO-2 and
CO-3;
1. Mutual Exclusion   [20]
SO-2;
o At least one resource is non-shareable, i.e., only one
BL-3
process can use it at a time.
and BL-4   2. Hold and Wait
o A process holding one or more resources is waiting for
additional resources.
3. No Preemption
o Resources cannot be forcibly taken; they must be
released voluntarily.
4. Circular Wait
o A set of processes forms a circular chain, where each
process is waiting for a resource held by the next.
Techniques to Handle Deadlock
********** 11 **********
--- page 12 ---
1. Deadlock Prevention
• Ensures that at least one of the necessary conditions is
eliminated.
• Methods:
o Remove mutual exclusion (if possible)
o Avoid hold and wait (request all resources at once)
o Allow preemption of resources
o Break circular wait (impose ordering of resources)
2. Deadlock Avoidance
• System checks resource allocation dynamically to avoid unsafe
states.
• Uses algorithms like Banker’s Algorithm.
•   Allocates resources only if the system remains in a safe state.
3. Deadlock Detection
• Allows deadlock to occur and then detects it.
• Techniques:
o Resource Allocation Graph (for single instance)
o Detection algorithms (for multiple instances)
4. Deadlock Recovery
• Once detected, system takes action:
o Terminate processes (all or one by one)
o Resource preemption (take resources and reassign)
o Rollback processes to a safe state
Consider the page reference string: (10 Marks)
3, 1, 2, 0, 3, 1, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 4, 3, 2, 1
i) Calculate the number of page faults using:
• FIFO
• LRU
• OPTIMAL
(Assume 3 frames)
ii) Identify the best algorithm and justify your answer.
Given:
********** 12 **********
--- page 13 ---
Page Reference String:
3, 1, 2, 0, 3, 1, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 4, 3, 2, 1
Number of Frames = 3
i) Page Fault Calculation
1. FIFO (First-In First-Out)
• Replace the oldest page first.
Page Faults = 15
2. LRU (Least Recently Used)
• Replace the page that has not been used for the longest time.
Page Faults = 12
3. OPTIMAL
• Replace the page that will not be used for the longest time in
future.
Page Faults = 9
ii) Best Algorithm
👉 OPTIMAL is the best algorithm
Justification:
•   It gives the minimum number of page faults (9).
•   It uses future knowledge, so it is theoretically optimal.
• However, it is not practical in real systems because future
references are unknown.
•   In practice, LRU is preferred as it approximates OPTIMAL.
Final Answer Summary
Algorithm   Page Faults
FIFO   15
LRU   12
OPTIMAL   9 ✅
********** 13 **********
--- page 14 ---
a.   Explain the Paging memory management technique.
Describe how paging eliminates the problem of external fragmentation
and explain the address translation mechanism with a neat diagram.
(10M)
Paging Memory Management Technique
Definition
b.
Paging is a memory management technique in which:
• Logical memory is divided into fixed-size pages
•   Physical memory is divided into fixed-size frames
• Pages are mapped to frames using a page table
Working of Paging
• A logical address is divided into:
o Page Number (p) → used to index the page table
o Offset (d) → specifies location within the page
Q5   • The page table maps page → frame
•   Physical address = Frame Number + Offset
CO-2 and
CO3; SO-
[20]
2;   Elimination of External Fragmentation
BL-3
and BL-4   •   In paging, memory is allocated in fixed-size blocks
• Any free frame can be assigned to any page
• Hence, no need for contiguous memory allocation
👉 Therefore:
• External fragmentation is eliminated
• Only internal fragmentation may occur (unused space within a
frame)
Address Translation Mechanism
Steps:
1. CPU generates a logical address (p, d)
2. Page number (p) is used to index the page table
3. Corresponding frame number (f) is obtained
4. Physical address is formed as (f, d)
Diagram (Conceptual)
Logical Address
┌──────────────┐
********** 14 **********
--- page 15 ---
│ Page | Offset│
└──────────────┘
↓
Page Table
(maps Page → Frame)
↓
┌──────────────┐
│Frame | Offset│
└──────────────┘
= Physical Address
↓
Physical Memory
Advantages
✔ Eliminates external fragmentation
✔ Efficient memory utilization
✔ Easy allocation of memory
Disadvantages
✖ May cause internal fragmentation
✖ Requires additional memory for page table
✖ Extra overhead in address translation
Conclusion
Paging provides an efficient way to manage memory by dividing it into
fixed-size units, eliminating external fragmentation and enabling
flexible memory allocation.
Consider the following snapshot of a system:
Process Allocation Max (A B   Available (A B
(A B C)   C)   C)
P0   0 1 0   7 5 3   3 3 2
P1   2 0 0   3 2 2   —
P2   3 0 2   9 0 2   —
P3   2 1 1   2 2 2   —
P4   0 0 2   4 3 3   —
Answer the following using Banker’s Algorithm:
1. Find the Need Matrix
2. Determine whether the system is in a safe state. If yes, write the
safe sequence
3.   If a request from process P1 (1, 0, 2) arrives, can it be granted
immediately? Justify
1. Need Matrix (Need = Max – Allocation)
********** 15 **********
--- page 16 ---
Allo
cati Max Nee
Pro
on (A B d (A
cess
(A B C) B C)
C)
0 1 7 5 7 4
P0
0   3   3
2 0 3 2 1 2
P1
0   2   2
3 0 9 0 6 0
P2
2   2   0
2 1 2 2 0 1
P3
1   2   1
0 0 4 3 4 3
P4
2   3   1
2. Safe State Check
Available = (3, 3, 2)
Step-wise:
• P1 → Need (1,2,2) ≤ (3,3,2) ✔ → New Available = (5,3,2)
• P3 → Need (0,1,1) ≤ (5,3,2) ✔ → New Available = (7,4,3)
• P4 → Need (4,3,1) ≤ (7,4,3) ✔ → New Available = (7,4,5)
• P0 → Need (7,4,3) ≤ (7,4,5) ✔ → New Available = (7,5,5)
• P2 → Need (6,0,0) ≤ (7,5,5) ✔
Safe Sequence:
P1 → P3 → P4 → P0 → P2
👉 System is in a SAFE state
3. Request by P1 = (1, 0, 2)
Check 1: Request ≤ Need
(1,0,2) ≤ (1,2,2) ✔
Check 2: Request ≤ Available
(1,0,2) ≤ (3,3,2) ✔
New Available after allocation:
(3,3,2) – (1,0,2) = (2,3,0)
Check Safe State Again:
• P1 → Need becomes (0,2,0) ≤ (2,3,0) ✔ → Available = (5,3,0)
• P3 → (0,1,1) ✖ (fails due to C=1 > 0)
• P2 → (6,0,0) ✖
• P4 → (4,3,1) ✖
********** 16 **********
--- page 17 ---
• P0 → (7,4,3) ✖
👉 No further process can proceed
Final Answer:
•
a.   Explain the concept of File Management in an Operating System.
Discuss different file organization methods and explain how files are
stored and accessed in secondary storage.
File Management in an Operating System
Concept
File Management is a component of the operating system responsible
for creating, storing, organizing, accessing, and protecting files on
secondary storage devices such as disks.
A file is a collection of related data stored on secondary storage and
b.   identified by a unique name.
Functions of File Management
•   File creation and deletion
•   File reading and writing
•   Directory management
• Access control and protection
Q6   • Storage allocation and space management
CO-3;
SO-2;   [20]
BL-2   File Organization Methods
1. Sequential Organization
and BL-4
• Data is stored in a linear sequence
• Access is done one record after another
Advantages:
• Simple and efficient for batch processing
Disadvantages:
• Slow for random access
2. Direct (Random) Organization
• Data is accessed using direct address or index
• Any record can be accessed directly
Advantages:
********** 17 **********
--- page 18 ---
•   Fast access
Disadvantages:
• Requires more complex implementation
3. Indexed Organization
• Uses an index table to locate records
• Combines features of sequential and direct access
Advantages:
•   Efficient searching
• Supports both sequential and random access
Disadvantages:
• Extra storage needed for index
File Storage in Secondary Storage
Files are stored on disks using different allocation methods:
1. Contiguous Allocation
•   File occupies continuous blocks
•   Fast access
2. Linked Allocation
•   File blocks are scattered but linked together
• No external fragmentation
3. Indexed Allocation
• Uses an index block containing addresses of all file blocks
•   Efficient and flexible
File Access Methods
• Sequential Access → Read/write in order
• Direct Access → Jump to any block directly
• Indexed Access → Use index to locate data
********** 18 **********
--- page 19 ---
Consider the following disk request queue (0–199):
95, 180, 34, 119, 11, 123, 62, 64
Initial head position = 50
Tasks:
1. Apply FCFS and SSTF disk scheduling algorithms
2. Show the order of execution
3. Calculate the total head movement
4. Identify which algorithm performs better and justify.
Given:
Request Queue: 95, 180, 34, 119, 11, 123, 62, 64
Initial Head Position = 50
## 1. FCFS (First Come First Serve)
Order of Execution:
50 → 95 → 180 → 34 → 119 → 11 → 123 → 62 → 64
Head Movements:
Dist
Mo
anc
ve
e
50
→ 45
95
95
→ 85
180
180
→ 146
34
34
→ 85
119
119
→ 108
11
11
→ 112
123
123
→ 61
62
********** 19 **********
--- page 20 ---
62
→ 2
64
Total Head Movement:
45 + 85 + 146 + 85 + 108 + 112 + 61 + 2 = 644
## 2. SSTF (Shortest Seek Time First)
Order of Execution:
50 → 62 → 64 → 34 → 11 → 95 → 119 → 123 → 180
Head Movements:
Move   Distance
50 → 62   12
62 → 64   2
64 → 34   30
34 → 11   23
11 → 95   84
95 → 119 24
119 → 123 4
123 → 180 57
Total Head Movement:
12 + 2 + 30 + 23 + 84 + 24 + 4 + 57 = 236
## 3. Comparison
• FCFS Total Movement = 644
• SSTF Total Movement = 236
Final Answer:
👉 SSTF performs better because it minimizes total head movement,
leading to faster disk access compared to FCFS.
Select any 4:
Q7   1. Explain any two Operating System services with suitable
CO-   examples.
1,CO2   Operating System Services
and CO3;   [20]
1. Process Management
SO-2;
The OS manages the creation, scheduling, and termination of processes.
BL-2
It allocates CPU time to processes and ensures smooth execution.
and BL-3   Example:
When multiple applications (e.g., browser, text editor) are running, the
OS schedules them using CPU scheduling algorithms.
********** 20 **********
--- page 21 ---
2. File Management
The OS handles file operations such as creation, deletion, reading,
writing, and organization of files in directories.
Example:
Creating a file, saving it, renaming it, or deleting it using the file
system.
2. What is a Process Control Block (PCB)? Explain its
components.
Process Control Block (PCB)
Definition:
A Process Control Block (PCB) is a data structure used by the
operating system to store all information about a process. It is created
when a process is initiated and deleted when the process terminates.
Components of PCB
1. Process ID (PID)
o Unique identifier assigned to each process
2. Process State
o Current state of the process (New, Ready, Running,
Waiting, Terminated)
3. Program Counter
o Address of the next instruction to be executed
4. CPU Registers
o Stores values of CPU registers (accumulator, index
registers, etc.) during context switching
5. CPU Scheduling Information
o Includes priority, scheduling queue pointers, etc.
6. Memory Management Information
o Information about memory allocation such as base/limit
registers or page tables
7. I/O Status Information
o List of I/O devices allocated and open files
8. Accounting Information
o CPU usage, execution time, process limits
3. What is a deadlock? Explain the concept of a Wait-For Graph.
Deadlock
Definition:
A deadlock is a situation in which a group of processes are blocked
indefinitely, each waiting for a resource held by another process in the
group.
Wait-For Graph (WFG)
********** 21 **********
--- page 22 ---
Concept:
A Wait-For Graph is a directed graph used to detect deadlocks in a
system with single-instance resources.
• Nodes represent processes
• A directed edge Pi → Pj indicates that process Pi is waiting for
a resource held by Pj
Working:
• Convert the Resource Allocation Graph (RAG) into a Wait-
For Graph by removing resource nodes
•   If the graph contains a cycle, then a deadlock exists
•   If there is no cycle, the system is deadlock-free
Example:
If:
• P1 is waiting for P2
• P2 is waiting for P3
• P3 is waiting for P1
Then a cycle is formed:
P1 → P2 → P3 → P1 → Deadlock exists
4. Define seek time and rotational latency in disk systems.
Seek Time and Rotational Latency
Seek Time
Seek time is the time required for the disk arm (read/write head) to
move from its current position to the desired track where the data is
stored.
Rotational Latency
Rotational latency is the time taken for the disk to rotate so that the
required sector aligns under the read/write head.
5. What is a directory? Explain different directory operations in an
operating system.
Directory in an Operating System
Definition:
A directory is a special file that stores information about files and
subdirectories, helping in organizing and managing files in a
hierarchical structure.
Directory Operations
1. Create Directory
o Creates a new directory in the file system
********** 22 **********
--- page 23 ---
2. Delete Directory
o Removes an existing directory (usually only if it is
empty)
3. Open Directory
o Allows access to the directory for reading its contents
4. Close Directory
o Closes the directory after operations are completed
5. Search Directory
o Searches for a file or subdirectory within the directory
6. List Directory Contents
o Displays all files and subdirectories present
7. Rename Directory/File
o Changes the name of a directory or file
8. Traverse Directory
o Allows navigation through the directory structure
********** 23 **********
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper a856e239cc98

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_Computer_7002/Operating Systems/ANS_Operating Systems(702CO1C002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: ocr (22 pages), mean OCR confidence 86.3
- 7 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS

SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

/B. Tech (AI & ML)/B. Tech (COMP). Tech
CE)/MBA Tech (Al)/MBA Tech (Comp)
IX/Semester V(Exam Year: 2025-2026)

Programme: B. Tech (AJ)/B. Tech (AI & DS).
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (
Year: I/ Ill / V/Semester IIl/Semester

Subject: Operating Systems
Date: 28 Nov 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)

Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)

Instructions:
1, This question paper contains 22 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. | is compulsory.
5. Out of remaining questions, attempt any
6. Inall 5 questions to be attempted.
7. Assume Suitable data if necessary.

4 questions.

11 A | What do you mean by Dual mode Operation in OS? Explain with suitable 5
diagram?

Definition (2 mark)
Explanation (2 marks)

Diagram (1 Mark)

ature of modern operating systems that allows the
ct modes — User Mode and Kernel (Supervisor)

ity and stability. It prevents user programs

Dual Mode Operation is a fe
CPU to operate in two distin
Mode — to ensure system securi
from directly accessing critical system resources.

e User Mode:
o Used to execute user applications.
Access to hardware and system resources is re!
o System calls are used to request OS services.
e Kernel Mode:
o Used by the operating sys
o Has unrestricted access to
o Switching from user mo
interrupts or system calls.

ser process
user mode
user process executing — calls system cail return from system call (mode bit = 1)
. Z
." Zz

ap retum
kernel mode bit « it =
bit=0 mode bit = 1 rial e

| (mode bit = 0)

The mode bit in the CPU (usually 0 = kernel, 1 = user) determines the current
mode. hat

operating

° stricted.

tem to execute privileged instructions.

hardware and system memory.
de to kernel mode occurs through

food 7 kaa ROR aR
--- page 2 ---
When an interrupt or system call occurs
when control returns to the use

Advantages / Purpose

, the mode bit switches to kernel mode;
T process, it switches back to user mode.

¢ Protects OS and hardware from faulty or malicious user programs.
¢ Maintains system stability and security.

¢ Ensures controlled access to resources through system calls only.

B | A student writes the following Producer-Consumer code: 5

semaphore full = 0, empty = N, mutex = 1;

Producer() {
while (true) {
produce_item(x);
wait(full);
wait(mutex);
insert(x);
signal(mutex);
signal(empty);
}

}

Consumer() {
while (true) {
wait(empty);
wait(mutex);
remove(x);
signal(mutex);
signal(full);
consume_item(x);

}

Identify the mistakes in semaphore usage and correct the code.

Explanation: 1 mark
Corrected code : 4 marks

Semaphore wait/si
Consumer:

° The Producer should wait on emp’
inserting an item, then signal full (i

ignal on full and empty are reversed in Producer and

ty (wait for empty slot) before
indicate one more full slot),

¢ The Consumer should wait on full (wait for an item) before removing,
then signal empty (indicate one more empty slot).

semaphore full = 0, empty = N, mutex = 1;

Producer() {
while (true) {
produce_item(x);
wait(empty);

// wait for an empty slot
wait(mutex);

Ae a ke a 2 FERRER REE
--- page 3 ---
insert(x);
signal(mutex);
signal(full), —_// signal that a new item is available
}
}

Consumer() {

while (true) {
wait(full); // wait for an available item
wait(mutex);
remove(x);
signal(mutex);
signal(empty); _// signal that a slot is now free
consume_item(x);

}

What is deadlock prevention? Discuss any two strategies used for preventing
deadlocks in an operating system.

Deadlock Prevention 1 Mark
Strategy 2 Mark each (4 Marks)

tion is a proactive method of ensuring that the system is

Deadlock preven
designed in such a way that at least one of the necessary conditions for

deadlock can never occur.

The four necessary conditions for deadlock are:

1. Mutual Exclusion
2. Hold and Wait

3. No Preemption
4, Circular Wait

Deadlock prevention works by denying or controlling these conditions.

Invalidate one of the four necessary conditions for deadlock:
= Mutual Exclusion — not required for sharable resources (e.g., read-only

files); must hold for non-sharable resources
« Hold and Wait — must guarantee that whenever a process req

resource, it does not hold any other resources
* Require process to request and be allocated all its resources

before it begins execution, or allow process to request resources
only when the process has none allocated to it.
+ Low resource utilization; starvation possible

= No Preemption:

+ If a process that is holding some resources requests another
resource that cannot be immediately allocated to it, then all
resources currently being held are released

* Preempted resources are added to the list of resources for which
the process is waiting

* Process will be restarted only when it can regain its old
resources, as well as the new ones that it is requesting

» Circular Wait:

uests a

SRA QR ERE
--- page 4 ---
Impose a total ordering of all resource types, and require that

each process requests resources in an increasing order of
enumeration

S|

D | Compare blocking, non-blocking,

explaining how each works in practic:
differences.

and asynchronous I/O operations by
€, and provide examples to illustrate the

Each operation 1 Mark (3 Marks)
Example 2 Marks

Blocking I/O: Process suspended until I/O completed; easy to use and
understand; sufficient for simple sequential operations
Nonblocking I/O: Returns immediately with available data: implemented via

multi-threading; useful for user interfaces and buffered I/O; uses select() to
check data availability

Asynchronous I/O: Process continues ex

to use but efficient; I/O subs

Examples: Blocking for si

handling multiple connecti
__| Operations

ecution while I/O executes; difficult
ystem signals process upon completion

mple file reads, nonblocking for network servers
ons, asynchronous for high-performance database

2/A | Explain the Dining Philosophers problem and critically analyze the reasons
why semaphore-based implementations may result in deadlock or starvation.
Propose and justify a monitor-based solution that addresses these issues,

10

Description: 2 marks

Why semaphore solution Fail: 2 marks
Monitor solution: 6 marks

Description:

¢ 5 philosophers’ sit at a round table with a bowl of rice in the middle.
e They spend their lives alternating thinking and eating.
¢ They do not interact with their neighbors.

@ Occasionally try to pick up 2 chopsticks (one at a time) to eat from bowl

¢ Need both to eat, then release both when done

Why semaphore solution Fail:
e Although this solution
simultaneously,

a deadlock.

Suppose that all five philosophers become hungry at the same time and
each grab their left chopstick. All the elements of chopstick will now

be equal to 0. When each philosopher tries to grab their right chopstick,
they will be delayed forever

guarantees that no two neighbors are eating
it nevertheless must be rejected because it could create

Monitor solution:
monitor DiningPhilosophers
{

enum ( THINKING, HUNGRY, EATING)
state [5] ;

condition self [5];
void pickup (int i) {
state[i] = HUNGRY;

FE EO RR OR ek Q FREE EHR
--- page 5 ---
test(i);
if (state[i] != EATING)
self[i].wait;

}

void putdown (int i) {
state[i] = THINKING;
// test left and right neighbors
test((i + 4) % 5);
test((i + 1) % 5);

void test (int i) {
if ((state[(i + 4) % 5] != EATING) &&
(state[i] == HUNGRY) &&
(state[(i + 1) % 5] != EATING) ) {
state[i] = EATING ;
self[i].signal () ;
}

}
re ee :
for (int i= 05 <5; i++) Ln vooati on of op enation =
— = THINKING; Dining Philassphes pic kupcily-
} [i Cok 8 / :

Dini na Philosophen _ putdospnt )) °

B | Consider the following processes with their arval times, burst tintes, and | 10 | ~

priorities.
Process Arrival Time BurstTime _ Priority
Pl 0 10 2
P2 1 4 1
P3 3 7 3
P4 4 6 2
P5 6 5 0

Considering pre-emptive priority scheduling algorithm (lower priority
numbers indicate higher priority), calculate the average turnaround
time and average waiting time for the given batch of processes.

ii. Considering round-robin scheduling algorithm (with time quantum =
4), calculate the average turnaround time and average waiting time for

the given batch of processes.

i.

se ea RE OD oe
--- page 6 ---
(GC =2 marks, Avg. TAT = 1.5 marks, Avg. WT = 1.5 marks)

(GC = 2 marks, Avg. TAT = 1.5 marks, Avg. WT = 1.5 marks)

3 | A | Consider the following snapshot of a system running 5 processes:

Process | Allocation Max Available
A B (COMIN B CIA B

Pl 0 il 0 a7, 5 3 13 3

P2 2 0 0 3 2 2)

P3 3 0 2 9 0 2

P4 2 1 1 2 2 2

PS 0 ORNS) 4 3 3

RRR EK EKA G FRR KERR ER
--- page 7 ---
Answer the following: -
i. How many resources of type A, B, C are there?
ii. Calculate the need matrix?
iii. Determine if the system is safe or not.
iv. What will happen if the resource request (1, 0, 0) for process P1 arrive,

can the system accept this request immediately?

Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks

Safe Sequence 4 Marks

Additional Request 3 Marks

Total Resources = Available + Allocation

ABC
10 5 7

Need Matrix = Max — Allocation

Process Need Matrix

A B

Cc
Pl 7 4 3
| P2 [1 2 2 |
P3 6 0 0
[ P4 [0 1 1|
PS 4 3 1

Finding out system is safe or not. And if safe then the sequence of process

execution.
Check if Need matrix <= Available

Process P2 need ca be full filled

New Available = Available — Need [P2]

ABC

2 1 0

After P2 complete, Available = New Available + Max[P2]
ABC

Shak 2.

Next Process P4 need ca be full filled

New Available = Available — Need [P4]

ABC

§ 2 1

After P4 complete, Available = New Available + Max[P4]
ABC

7 4 3

Next Process P5 need ca be full filled
New Available = Available — Need [P5]

--- page 8 ---
ABC
3 a
After P5 complete, Available = New Available + Max[P5]
ABC
2

Next Process P1 need ca be full filled

New Available = Available — Need [P1]

ABC

0 0 2

After P1 complete, Available = New Available + Max[P1]
ABC

7 Wt #5

Next Process P3 need ca be full filled

New Available = Available — Need [P3]

ABC

1_ 5235

After P3 complete, Available = New Available + Max[P3]
ABC

10 5 7

If Available == Total Resources.

Then the system is in safe state and one of the sequences of the process
execution will be

P2 -> P4 -> P5 -> Pl -> P3

Showing the request of P1 (1,0,0) is acceptable or not.
In the provided available recourses that is

ABC

3 3 2

If we grant P1 (1,0,0) then new available will be
ABC

2 3 2

With these available resources still, we can proceed with the safe sequences of
the all the process. That’s why we can grant PJ request immediately.

Explain the concept of paging and its purpose in memory management. With
the help of a neat diagram, describe how paging hardware translates a logical
address into a physical address. How the Translation Lookaside Buffer (TLB)
can enhances the performance of paging.

10

Marks Distribution:

Explanation of paging and need — 4 Marks
Paging hardware representation — 4 Marks
Role of TLB in paging — 2 Marks

Definition:

Paging is a memory management technique in which the logical (virtual)
memory of a process is divided into fixed-size blocks called pages, and the
physical memory (RAM) is divided into blocks of the same size called frames.

RK EH QB RRERERA RAK
--- page 9 ---
iF When a program is executed, its pages are loaded into available frames in main
memory, not necessarily in a contiguous manner.
Need for Paging:
1. Eliminates External Fragmentation:
Since pages and frames are of fixed size, there ar
memory holes.
2. Efficient Memory Utilization:
Allows non-contiguous memory allocation
processes are minimized.
3. Simplifies Memory Management:
The operating system can manage memory using pag
complex variable partitions.
4. Supports Virtual Memory:
Enables programs larger than physical memory to exec’

only required pages.

e no variable-sized

— unused gaps between

e tables rather than

ute by loading

frame @

logical address physical address 0x000
d

nm =m

cpu pla jt|4 fares
| p >= Oxtfft

—/ ft frame

—— 9

physical memory

page table
Role of Translation Lookaside Buffer (2 Marks)
e Every memory access in a paging system requires two memory

references:
o One to access the page table (to find the frame number).

o Another to access the actual data in memory.

e This doubles the access time.
To solve this, a Translation Lookaside Buffer (TLB) is used.

TLB:

A special high-speed cache that stores recently used page table entries

(page—frame mappings).
« When a logical address is generated:
o Ifthe page number is found in the TLB (TLB hit), the frame

number is retrieved instantly.
o Ifnot found (TLB miss), the page table is accessed and the

TLB is updated.

4 | A | Operating systems provide an environment for execution of programs and,
offers services to programs and users. Justify the statement by explaining the

operating system services with suitable diagram?

Justification (3 Marks)

dea Qa te
--- page 10 ---
Operating System Services any five (5 Marks)
Diagram (2 Marks)

An Operating System (OS) serves as an essential layer between the hardware
and the user/

programs, ensuring efficient, reliable, and convenient execution
of

applications.
It provides an execution environment wh

ere multiple programs can run
concurrently, share resources, and interact with hardware safely.

The OS not only controls hardware but also deli
program execution and enhance
Thus, it can be viewed as both a resource manager and

vers Services that simplify
user productivity.
a service provider.

Justification

Without the operating system, use!
hardware operations such as me
process

The OS abstracts these complexities by offering well-defined
program execution, fi

ts would have to directly manage complex
mory allocation, device communication, or
synchronization.

services such as
le management, and interprocess communication.

By providing these services:

¢ The OS ensures convenie:

handling hardware details.
e It ensures efficienc
allocated optimally.
It ensures security and reliability —
protection mechanisms,

nce — users can run programs without

Y — resources like CPU, memory, and I/O are

through error handling and

Hence, the OS creates a controlled, stable, and user.

-friendly environment for
both users and system programs.

Operating System Services (5 Marks)

1. Program Execution:
Loads, runs, and terminates programs. Manages process scheduling and
transitions.

2. VO

Operations:

Provides a uniform interface for input/output devices, abstracting

hardware details.

3. File System Manipulation:
Manages file creation, deletion, access control, and organization in
secondary storage,

4. Inter-process
Enables process coordinatio
memory or message passing.
5. Error Detection and

Monitors the system to detect and respoi
errors gracefully.
6. Resource

Dynamically allocates CPU time,
processes fairly.

Communication (IPC):
n and data exchange through shared

Handling:
md to hardware or software

Allocation:
memory, and I/O to competing

FRRE RK RE KE 10 FEHR HK RHE
--- page 11 ---
7. Accounting:
Tracks system and resource usage for performance monitoring and
optimization.

8. Protection
Ensures data privacy and system integrity thro

and Security:
ugh controlled access and

authentication.
ee _ =
‘user and other system programs 5
— |
| Gul | touch screen command line |
|
user interfaces
Lethe
| system calls
—. ce ee ee eee
|| execution \| operations systems communication || allocation accounting
Wee EES ee
error | pratection
detection | and
services bres
operating system pee Be eee Bl
hardware

defined execution environment by hiding hardware

The OS provides a well-
uring safe resource sharing,

complexity, managing concurrent activities, ens
and delivering reliable services.

Therefore, the statement is justified:
environment for execution of programs and servic

“Operating Systems provide an
es to both programs and

users.”
A disk queue has requests on cylinders 2069, 1212, 2296, 2800, 544, 1618,
inder 2150. The disk has

356, 1523. The disk head is currently positioned at cyl

cylinders numbered from 0 to 4999.
Calculate the total head movement (in cylinders) required to service all

requests using the following disk scheduling algorithms:
1. FCFS (First-Come-First-Served)
2. SCAN (Elevator Algorithm), assuming the hea
towards the highest cylinder (4999).
3. C-SCAN (Circular SCAN), assuming

towards the highest cylinder (4999).
Compare the performance of the three algorithms based on their total head

movement and discuss one major factor of comparison.

d is initially moving

the head is initially moving

Each algorithm 3 marks (9 marks)
Comparison 1 mark

--- page 12 ---
a
Performance Comparison
ALGORITHM TOTAL MOVEMENT ‘CHARACTERISTICS
FCFS 8,285 Simele. fa'r, but hign seek time
SCAN 7,492 Fair, predictabie. moderate performance
SCAN 9,917

More uniform wait tire higher movement

Performance Comparison: SCAN has the lowest head movement (7492

cylinders), making it the most efficient algorithm for this specific batch of

ER ER 12 PRK EK
--- page 13 ---
requests and head position. FCES performs better than C-SCAN, but SCAN is

the most efficient of the three.
Major Factor of Comparison: Uniformity of Wait Time
The major factor distinguishing SCAN and C-SCAN is the Uniformity of Wait

Time.

e SCAN: Causes a non-uniform wait time. Requests that are waiting just
behind the reversing head (e.g., at cylinder 4900 after the head has just
left it going towards 0) will have to wait for the entire sweep to the
other end (0) and back, leading to a much longer latency than requests

near the ends.
» C-SCAN: Provides a more uniform wait time. By always servicing
ing back to the

requests in only one direction and immediately jump
start, C-SCAN ensures that a new request waits, at most, for the time it
takes the head to complete one full circular sweep, regardless of its
position on the disk. This predictability is highly valuable in high-

performance or heavy-load systems.

S|A

ing by explaining its fundamental

Describe the concept of Message Pass
port your explanation with a neat

primitives and addressing methods. Sup
diagram of the general message format.

Message passing: 2 marks
Primitives: 3 marks
Addressing: 2 marks
Message format: 3 marks

Message Passing:
@ When processes interact with one another, two fundamental

requirements must be satisfied: synchronization and communication.
e Processes need to be synchronized to enforce mutual exclusion;

cooperating processes may need to exchange information.
@ One approach to providing both of these functions is message passing.

e Message passing has the further advantage that it lends itself to

implementation in distributed systems as well as in shared-memory
multiprocessor and uniprocessor systems.

Primitives:

e We need to specify what happens to a
receive primitive.

e@ When a send primitive is exec
possibilities: Either the sending process is
received, or it is not.

e Similarly, when a process
possibilities:

1, Ifa message has previously been sent, the messag

continues.
> If there is no waiting message, then either (a) the process is blocked until a
message arrives, or (b) the process continues to execute, abandoning the

attempt to receive.
e Thus, both the sender and receiver can be blocking or nonblocking.

e Three combinations are common, although any particular system will
usually have only one or two combinations implemented:

process after it issues a send or

uted in a process, there are two
blocked until the message is

issues a receive primitive, there are two

e is received and execution

RRR REE 7 QZ eR
--- page 14 ---
1. Blocking send, blocking receive: Both the sender and receiver are blocked
until the message is delivered; this is sometimes referred to as a rendezvous.

This combination allows for tight synchronization between processes.

2. Nonblocking send, blocking receive: Although the sender may continue on,

the receiver is blocked until the requested message arrives. This is probably
the most useful combination. It allows a process to send one or more messages

to a variety of destinations as quickly as possible. A process that must receive
a message before it can do useful work needs to be blocked until such a
message arrives. An example is a server process that exists to provide a service
or resource to other processes.

3. Nonblocking send, nonblocking receive: Neither party is required to wait.

Addressing:

@ The various schemes for specifying processes in send and receive

Primitives fall into two categories: direct addressing and indirect
addressing.
© With direct addressing, the send primitive includes a specific identifier
of the destination process.
© The receive primitive can be
possibility is to require that the
process. Thus, the process must
a message is expected.
The other general approach is indirect ad
Messages are not sent directly from sender to
sent to a shared data structur.
hold messages.
Such queues are generally referred to as
Processes to communicate, one
appropriate mailbox,
the mailbox.

handled in one of two ways. One
process explicitly designate a sending
know ahead of time from which process

dressing. In this case,
receiver, but rather are
€ consisting of queues that can temporarily

mailboxes. Thus, for two
process sends a message to the
and the other process picks up the messages from

Destination ID
Header
Message Length
Control Information
Body A Message Contents

Figure 5.19 General Message Format

B | Analyze how hardware address protection mechanisms, such as base and limit

registers, prevent illegal memory access. Illustrate your answer with an

example of process isolation. Consider six memory partitions of size 350 KB,
700 KB, 580 KB, 450 KB, and 300 KB in the same order. Considering
contiguous memory allocation, show how the first-fit, best-fit and worst-fit

algorithms will place the Processes of 360 KB, 600 KB, 425 KB, and 250 KB
(in order).

RR RK Ke 14 FRR RRR RE
--- page 15 ---
Marks Distribution:

Address protection mechanism 2 marks
Process isolation 2 marks

First Fit — 2 marks

Best Fit — 2 marks

Worst Fit — 2 marks

Hardware address protection is a mechanism in an operating system that
ensures each process accesses only its allocated memory space. This protection
is achieved through special hardware registers — primarily the base register
and limit register — which define the valid address range for each process.

Base Register: Holds the starting physical address of the process’s memory
space.

Limit Register: Specifies the size or maximum offset of the process’s
addressable memory range.

When a process generates an address (logical address), the hardware adds the
base value to it to get the physical address.

Before accessing memory, the hardware checks whether the logical address is
less than the limit. If it exceeds, the access is blocked, and a trap or exception

is raised.
base base + limit
id eS eS
cpu address G E> -— y
no no |

trap to operating system
illegal addressing error memory

If 0 < Logical Address < Limit > Access Allowed
Else > Trap (Illegal Access)

Process Isolation Example
Consider two processes — P1 and P2.

P1 has Base = 1000 and Limit = 500, so it can access physical addresses 1000—

1499.
P2 has Base = 2000 and Limit = 400, so it can access addresses 2000-2399.

If P1 tries to access memory location 1800, the hardware check will detect it
is beyond its limit (1499), triggering a trap — thereby preventing illegal access
to P2’s memory region.

eR KEKE TS KKK ERE KE
--- page 16 ---
REE RK 16 FERRER RRS
--- page 17 ---
6\|A| I.   Lilustrate and describe, using a suitable diagram, how a process 10
transitions through various states during its execution.
Il. Identify and explain the conditions under which each state transition

takes place.
Ill. Apply your understanding of process scheduling to explain two

scenarios in which a process may transition from the Running state to
the Ready state before completing its CPU burst.

I. 4 marks
I. 3 Marks
I. 3 Marks

Solution: i. State Transition diagram - (4 marks)
admitted interrupt

1/0 or event wait

i. Transitions occurrence: (3 marks)

e New—Ready: admitted by long-term scheduler.

e Ready—»Running: selected by CPU scheduler.

e Running— Waiting: I/O request, page fault, lock wait.

HH AOR AOR AIR 7 OR EE
--- page 18 ---
Waiting—Ready: I/O completes, event/interrupt occurs.
Running—Ready: preempted by higher priority or time slice expiry.
¢ Running—Terminated: Process exit/abort.

lii. As stated in the Lifecycle diagram, a process may move from the
Running state to the Ready state before completing its CPU burst due

to pre-emption (I/O or event wait) or priority-based scheduling events
(interrupts). - (3 marks)

B | A system uses 4 frames for storin
that all the page frames are initial]
given below:

2,3,4,5,3,2,6,7,3,2,3,4,8,7,4,3,2,3,4,7

8 process pages in main memory. Assume
ly empty. Consider the page reference string

I. Simulate the page replacement using the FIFO algorithm.
I. Simulate the page replacement using the LRU algorithm.
Ul. Simulate the page replacement using the Optimal algorithm.
IV. For each algorithm, calculate the total number of page faults.
V.

Based on your results, which algorithm performs best and why?

Marks Distribution:

2 marks each on every point of questions i.e. 5 * 2 = 10 marks
a)

FIFO
2 3 4 5 3 2 6 i 3 2
2 2 2 ieee (a2 [6] 6 6| | ¢|
| 3 3 3} [3 3 7 7 7
4 4) | 4 4 4 4 3 3
Ls} Ls [5s 5 5 5 2
3 4 8 7 4 3 2 3 7

4
AF oOo eA RAGE
J
3 fa tal Cy La 7 3
2 2 Lz [a [a 3 3 3 3
F F F F F
Total Page Fault: 14
b)

TR OR Oe 1G FRRKEK REE
--- page 19 ---
LRU

q

q
4

3

2 3 4 5 3 2 6 7 3 2
a} 12) ofa) 32) 42] of 2]! 2] 2, 2 82) oO 2
o| 3] ¢ (3 al of sl 1 (al 213] 313] ol 3] 11 3
o| 4 14 24) 34 ele [4 36 3/5
ax.) a] t{_5| 2{_5} 315] of 7 117 217
3 4 8 7 4 3 2 3 4 7
2} 22) 34 of 4 ' [7 7 3{- 7) 47] S27] 07
a} 1{_al 2{_3| 3-3] 4[-a| of a] i a] oO 8 | 3 2 8
6] o| 4) 1 | 4! 4} Oo] 4) 1\_4) 214) 3 0 \
4a olcal vCal ae} Sel ol 2] | 2, 3B 3L®
F F F F
Total Page Fault: 10
¢)
Optimal
2 3 4 5 3 2 6 7 3 2
Tah aml ae afc 2. [e 2 2 2 2 2
_| Ls Ls Ls 3} | 3} | 8 3 3 3
—| FI 4 4 al [al 4 4 4 4
oa |_4| a) [sl Ls 7 7 7
3 4 8 Ze seks dl eehise 2 3 4 7
4 | 8 3 8 2} {2 L2 2
Ta) 3 3 3 3 3 3 3 3 3
al (4 4 a4) C4 La L4 4 4 4
7 7 7 7 7 7 7 7 7 7
F F

Total Page Fault: 8

d) Total number of page faults:
FIFO:14, LRU:10, optimal: 8

e) Based on your results, which algorithm performs best and why?

Optimal minimizes page faults by always replacing the page that will not be
e. It uses future knowledge, making it

used for the longest time in the futur
theoretical but ideal for benchmarking. LRU is better than FIFO because it

uses past usage patterns (replacing least recently used), while FIFO doesn’t
consider usage, just arrival order.

T\A

What is resource allocation graph? Consider the following snapshot of a

system having 2 resources (RI having 1 instance and R2 having 2 instances)

and running 3 processes.

Process Allocation Request
RI R2_ Rl R2
{Pi [4 0 [0 i |

4

RARER RK 1 RRR ORE
--- page 20 ---
P2 0 est 0
[P3 [0 i [0 0 |
Draw the resource allocation graph. Find if there is a deadloc

k or not? If there
is no deadlock then what will be the sequence of the process to get executed?

RAG description 3 marks
Draw RAG 4 marks

Safe Sequence 3 marks

i) What is resource allocation graph? [3 Marks]

° A useful tool in characterizing the allocation of resources to processes

is the resource allocation graph.

The resource allocation graph is a directed graph that depicts a state of

the system of resources and processes, with each process and each

resource represented by a node.

A graph edge directed from a process to a resource indicates a resource

that has been requested by the process but not yet granted.

Within a resource node, a dot is shown for each instance of that
resource.

Examples of resource types that may have multiple instances are Vo
devices that are allocated by a resource management module in the OS.
A graph edge directed from a reusable resource node dot to a process

indicates a request that has been granted; that is, the process has been
assigned one unit of that resource.

. > |
Requests \ Hel

Pt _ @ Rk a ees

wy — | |

moe AC) oe 4
{a) Resource is requesied (b) Resource is held

a ii) Draw a resource allocation graph of the following table? [4 Marks]

--- page 21 ---
iii) Find if there is a deadlock or not
the sequence of the process to get executed?
There is no deadlock in the resource allocation graph.

2 If there is no deadlock then what will be
[3 Marks]

The sequence of process to execute in safe sequence is

P3 -> Pl ->P2

B | Define a PCB. How can it help in enabling multi-tasking?

Definition 1 Mark
Explanation 4 marks

A Process Control Block (PCB) is a data structure maintained by
contains all the essential information about a

(1 mark)

Solution:
the Operating System that

process.

Multitasking means executing multiple processes seemingly at the same time
by rapidly switching the CPU between them.

Here’s how PCB makes that possible:

1. Context Saving:
a. When a running process is interrupte:

expiry or I/O request),
the OS saves its current CPU state (registers, PC, etc.) into its
PCB.

2. Context Restoration:
a. When the process is scheduled again, the OS restore

state from its PCB.
The process resumes exactly where it left off.

3. Accurate Process Switching:
a. The PCB ensures that switching between processes (context

switching) does not corrupt data or execution flow.
4. Tracking Multiple Processes:

d (e.g., due to time slice

s the saved

ae OR ER 21 RRR KA EERE
--- page 22 ---
a. Each process has its own PCB, so the OS can easily track,
suspend, resume, or terminate any process at any time.

(4 marks)

C | Summarize the main file attributes managed by a file system and explain the | 5
common operations that can be performed on a file.

Key Attributes 2.5 marks
File Operations 2.5 marks

Key File attributes:
File attributes are

pieces of information maintained by the file system about a
file and are typica

ly kept in the directory structure on the disk.
Name: This is the only file information kept in human-readable form.
Identifier: This is a unique tag (a number) that identifies the file within the
file system.

Type: This is needed for sy:
Location: This is a pointer
device.

Size: This records the current size of the file.
Protection: This controls who can
writing, and executing the file,
Time, Date, and User Identification: Thi
security, and monitoring file usage.

stems that support different types of files.
that indicates the file's location on the storage

perform operations such as reading,

s data is maintained for protection,

Major File Operations:

The operating system
performed on files:

Create: This operation creates a new file.

Write: This operation writes data to the file starting at the current write
pointer location.

Read: This operation reads data
pointer location.

Delete: This operation deletes the file.
Open (Fj): This operation involves searc
for the entry Fj and moving the content of that entry into memory.

Close (Fi): This operation moves the content of file entry Fi from memory
back to the directory structure on the disk.

Reposition (Seek): This operation moves the read/write pointer within the
file.

Provides several major operations that can be

from the file Starting at the current read

hing the directory structure on disk

Truncate: This operation zeros the file length and keeps the attributes, but
discards the file's contents.

KERR EER 22 FFEEEK ERR
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper ea4157d5b0d2

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/Integrated_IT_7037/Operating Systems/ANS_Operating Systems(702CO1C002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (23 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech
(IT)
Year: II / IV/Semester IV/Semester VIII(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 11 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain the layered structure of an Operating System with suitable
explanation.
Layered Structure of an Operating System
The layered structure of an Operating System is a design approach
where the OS is divided into multiple layers, each performing specific
functions.
Each layer uses services of the lower layer and provides services to the
layer above.
Typical Layers:
CO-1 ;
SO-2 ;   1. Hardware – Physical components like CPU, memory, I/O devices   5
BL-2   2. Kernel – Manages processes, memory, and devices
3. System Call Interface – Connects user programs with kernel
4. System Programs – Utilities like compilers and editors
5. User Interface – CLI/GUI for user interaction
Advantages:
• Easy to design and debug
•   Better modularity and security
********** 1 **********
--- page 2 ---
Disadvantages:
•   Performance overhead due to multiple layers
b.   Define a process and describe its different states with a diagram.
Definition of a Process
A process is a program in execution. It is an active entity that includes
not only the program code but also its current activity, such as the
program counter, CPU registers, stack, and data.
Different States of a Process
CO-2 ;
SO- 2;   5
BL-2
A process passes through the following states during its lifecycle:
1. New (Created)
o The process is being created.
o Resources are allocated, but execution has not yet started.
2. Ready
o The process is ready to run and waiting for CPU
allocation.
o   It resides in the ready queue.
3. Running
o The process is currently executing on the CPU.
o Only one process can be in this state per CPU at a time.
4. Waiting (Blocked)
o The process is waiting for some event to occur (e.g., I/O
completion).
o   It cannot proceed until the event is completed.
5. Terminated (Exit)
o The process has finished execution.
o The OS deallocates its resources.
********** 2 **********
--- page 3 ---
State Transitions (Brief)
• New → Ready (admitted by OS)
• Ready → Running (CPU scheduler selects)
• Running → Waiting (I/O request)
• Waiting → Ready (I/O completion)
• Running → Terminated (execution finished)
c.   What is a race condition? Explain its impact with an example.
Race Condition (5 Marks Answer)
A race condition occurs when two or more processes/threads access
and modify shared data simultaneously, and the final result depends
on the order of execution.
Impact
• Produces incorrect or inconsistent results
CO-3 ;   • May cause data corruption
SO- 2;   • Leads to unpredictable system behavior
5
BL-2
and BL-3
Example
Consider a shared variable count = 5.
Two processes P1 and P2 increment it at the same time.
• Both read count = 5
• Both increment to 6
• Both write back 6
👉 Final value becomes 6 instead of 7 → incorrect result
d.   Define deadlock and briefly explain its necessary conditions.
Here is a crisp 5-mark answer (exam-ready) 👇
Deadlock
Definition:
A deadlock is a situation in an operating system where a set of
processes are blocked indefinitely, each waiting for a resource held by
CO- 3;   another process.
SO- 2;   5
BL-2   Necessary Conditions for Deadlock
(All four must occur simultaneously)
1. Mutual Exclusion
o At least one resource is non-shareable (only one process
can use it at a time)
2. Hold and Wait
o A process holding at least one resource is waiting for
additional resources
********** 3 **********
--- page 4 ---
3. No Preemption
o Resources cannot be forcibly taken; they must be
released voluntarily
4. Circular Wait
o A circular chain of processes exists where each process is
waiting for a resource held by the next process
a. Explain the Producer–Consumer (Bounded Buffer) problem. Write a
semaphore-based solution and explain synchronization. (10 Marks)
Producer–Consumer (Bounded Buffer) Problem
b.   The Producer–Consumer problem is a synchronization problem
where a producer process generates data and places it in a fixed-size
buffer, while a consumer process removes data from the buffer. Since
the buffer is bounded, the producer must wait if the buffer is full, and
the consumer must wait if the buffer is empty.
Semaphore-Based Solution
Let:
• mutex = 1 (ensures mutual exclusion)
• empty = N (number of empty slots in buffer)
• full = 0 (number of filled slots)
Q2
CO-2;
SO-2;   Producer   [20]
BL-3   do {
and BL-4   wait(empty);
wait(mutex);
// insert item into buffer
signal(mutex);
signal(full);
} while(true);
Consumer
do {
wait(full);
wait(mutex);
// remove item from buffer
signal(mutex);
signal(empty);
} while(true);
********** 4 **********
--- page 5 ---
Synchronization Explanation
• mutex ensures only one process accesses the buffer at a time
(mutual exclusion).
• empty prevents the producer from adding data when the buffer
is full.
• full prevents the consumer from removing data when the
buffer is empty.
• wait() and signal() operations coordinate execution and
avoid race conditions.
Conclusion
The semaphore-based solution ensures proper synchronization between
producer and consumer, preventing buffer overflow, underflow, and
race conditions.
Consider the following processes:
Process Arrival Time Burst Time
P1   0   6
P2   1   4
P3   2   5
P4   3   3
i) Apply Shortest Remaining Time First (Preemptive) scheduling. Draw
the Gantt Chart and calculate Average Waiting Time and Average
Turnaround Time. (4 Marks)
ii) Apply Shortest Job First (Non-Preemptive) scheduling. Draw the
Gantt Chart and calculate Average Waiting Time and Average
Turnaround Time. (4 Marks)
iii) Compare both algorithms based on Average Waiting Time and
Turnaround Time. (2 Marks)
Given Processes
Pro
AT BT
cess
P1 0   6
P2 1   4
P3 2   5
P4 3   3
## i) SRTF (Preemptive)
Gantt Chart:
0–1 P1 | 1–5 P2 | 5–8 P4 | 8–13 P3 | 13–18 P1
********** 5 **********
--- page 6 ---
Completion Time (CT):
Pro
CT
cess
P1 18
P2 5
P3 13
P4 8
Turnaround Time (TAT = CT – AT)
Pro
TAT
cess
P1 18
P2 4
P3 11
P4 5
Waiting Time (WT = TAT – BT)
Pro
WT
cess
P1 12
P2 0
P3 6
P4 2
Average Times:
• Avg WT = (12 + 0 + 6 + 2) / 4 = 5
• Avg TAT = (18 + 4 + 11 + 5) / 4 = 9.5
## ii) SJF (Non-Preemptive)
Gantt Chart:
0–6 P1 | 6–9 P4 | 9–13 P2 | 13–18 P3
Completion Time (CT):
Pro
CT
cess
P1 6
P2 13
P3 18
P4 9
********** 6 **********
--- page 7 ---
Turnaround Time (TAT):
Pro
TAT
cess
P1 6
P2 12
P3 16
P4 6
Waiting Time (WT):
Pro
WT
cess
P1 0
P2 8
P3 11
P4 3
Average Times:
• Avg WT = (0 + 8 + 11 + 3) / 4 = 5.5
• Avg TAT = (6 + 12 + 16 + 6) / 4 = 10
## iii) Comparison
• SRTF gives lower Average Waiting Time (5 < 5.5)
• SRTF gives lower Average Turnaround Time (9.5 < 10)
• Hence, SRTF performs better than SJF (Non-Preemptive) for
this set.
a.   Discuss the Readers–Writer problem. Explain its semaphore-based
solution and describe how synchronization is achieved when multiple
readers and a single writer access shared data. (10 Marks)
Readers–Writers Problem
The Readers–Writers problem is a classic synchronization problem
Q3   where:
CO-2;   b.   • Multiple readers can read shared data simultaneously   [20]
SO-2;   • A writer must have exclusive access to the shared data
BL-3 and
BL-4   👉 The challenge is to ensure:
• No reader reads while a writer is writing
• No writer writes while readers are reading
Semaphore-Based Solution
********** 7 **********
--- page 8 ---
Shared Variables:
• mutex = 1 → protects read count
• rw_mutex = 1 → controls access to shared resource
• read_count = 0 → number of active readers
Reader Process
do {
wait(mutex);
read_count++;
if (read_count == 1)
wait(rw_mutex);   // first reader blocks writers
signal(mutex);
// Reading is performed
wait(mutex);
read_count--;
if (read_count == 0)
signal(rw_mutex); // last reader releases writer
signal(mutex);
} while(true);
Writer Process
do {
wait(rw_mutex);
// Writing is performed
signal(rw_mutex);
} while(true);
How Synchronization is Achieved
• Multiple Readers Allowed:
Readers can access the data simultaneously since they do not
modify it
• Writer Gets Exclusive Access:
rw_mutex ensures only one writer can access the resource and
blocks readers during writing
• Reader Priority (in this version):
First reader locks the resource; last reader releases it
• Mutual Exclusion:
Writers are mutually exclusive with both readers and other
writers
Conclusion
The semaphore-based solution ensures correct synchronization by
allowing concurrent reading while maintaining exclusive writing,
thus preventing race conditions and ensuring data consistency.
********** 8 **********
--- page 9 ---
Given the following processes (all arriving at time 0 ms)
Process   Burst Time (ms)
P1   6
P2   8
P3   3
P4   5
a) Apply Round Robin Scheduling (Time Quantum = 2 ms). Draw the
Gantt Chart and compute Average Waiting Time and Average Turnaround
Time. (4 Marks)
b) Apply First Come First Serve (FCFS) scheduling. Draw the Gantt Chart
and compute Average Waiting Time and Average Turnaround Time. (4
Marks)
c) Compare both algorithms based on the results obtained. (2 Marks)
Given Processes (All AT = 0)
Bur
Pro   st
cess Tim
e
P1 6
P2 8
P3 3
P4 5
## a) Round Robin (Time Quantum = 2 ms)
Gantt Chart:
0–2 P1 | 2–4 P2 | 4–6 P3 | 6–8 P4 |
8–10 P1 | 10–12 P2 | 12–13 P3 | 13–15 P4 |
15–17 P1 | 17–19 P2 | 19–20 P4 | 20–22 P2
Completion Time (CT):
Pro
CT
cess
P1 17
P2 22
P3 13
P4 20
********** 9 **********
--- page 10 ---
Turnaround Time (TAT = CT – AT)
Pro
TAT
cess
P1 17
P2 22
P3 13
P4 20
Waiting Time (WT = TAT – BT)
Pro
WT
cess
P1 11
P2 14
P3 10
P4 15
Average Times:
• Avg WT = (11 + 14 + 10 + 15) / 4 = 12.5
• Avg TAT = (17 + 22 + 13 + 20) / 4 = 18
## b) FCFS Scheduling
Gantt Chart:
0–6 P1 | 6–14 P2 | 14–17 P3 | 17–22 P4
Completion Time (CT):
Pro
CT
cess
P1 6
P2 14
P3 17
P4 22
Turnaround Time (TAT):
Pro
TAT
cess
P1 6
P2 14
P3 17
P4 22
Waiting Time (WT):
********** 10 **********
--- page 11 ---
Pro
WT
cess
P1 0
P2 6
P3 14
P4 17
Average Times:
• Avg WT = (0 + 6 + 14 + 17) / 4 = 9.25
• Avg TAT = (6 + 14 + 17 + 22) / 4 = 14.75
## c) Comparison
• FCFS has lower Average Waiting Time (9.25 < 12.5)
• FCFS has lower Average Turnaround Time (14.75 < 18)
• Round Robin provides better response time but higher
waiting time
a.   Explain deadlock and its four necessary conditions. Discuss techniques
to handle deadlock including prevention, avoidance, detection, and
recovery. (10 Marks)
Deadlock
Definition
A deadlock is a situation in an operating system where a group of
b.   processes are blocked indefinitely, each waiting for a resource held by
another process in the group.
Q4   Necessary Conditions for Deadlock
(All four must occur simultaneously)
CO-2 and
CO-3;
1. Mutual Exclusion   [20]
SO-2;
o At least one resource is non-shareable, i.e., only one
BL-3
process can use it at a time.
and BL-4   2. Hold and Wait
o A process holding one or more resources is waiting for
additional resources.
3. No Preemption
o Resources cannot be forcibly taken; they must be
released voluntarily.
4. Circular Wait
o A set of processes forms a circular chain, where each
process is waiting for a resource held by the next.
Techniques to Handle Deadlock
********** 11 **********
--- page 12 ---
1. Deadlock Prevention
• Ensures that at least one of the necessary conditions is
eliminated.
• Methods:
o Remove mutual exclusion (if possible)
o Avoid hold and wait (request all resources at once)
o Allow preemption of resources
o Break circular wait (impose ordering of resources)
2. Deadlock Avoidance
• System checks resource allocation dynamically to avoid unsafe
states.
• Uses algorithms like Banker’s Algorithm.
•   Allocates resources only if the system remains in a safe state.
3. Deadlock Detection
• Allows deadlock to occur and then detects it.
• Techniques:
o Resource Allocation Graph (for single instance)
o Detection algorithms (for multiple instances)
4. Deadlock Recovery
• Once detected, system takes action:
o Terminate processes (all or one by one)
o Resource preemption (take resources and reassign)
o Rollback processes to a safe state
Consider the page reference string: (10 Marks)
3, 1, 2, 0, 3, 1, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 4, 3, 2, 1
i) Calculate the number of page faults using:
• FIFO
• LRU
• OPTIMAL
(Assume 3 frames)
ii) Identify the best algorithm and justify your answer.
Given:
********** 12 **********
--- page 13 ---
Page Reference String:
3, 1, 2, 0, 3, 1, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 4, 3, 2, 1
Number of Frames = 3
i) Page Fault Calculation
1. FIFO (First-In First-Out)
• Replace the oldest page first.
Page Faults = 15
2. LRU (Least Recently Used)
• Replace the page that has not been used for the longest time.
Page Faults = 12
3. OPTIMAL
• Replace the page that will not be used for the longest time in
future.
Page Faults = 9
ii) Best Algorithm
👉 OPTIMAL is the best algorithm
Justification:
•   It gives the minimum number of page faults (9).
•   It uses future knowledge, so it is theoretically optimal.
• However, it is not practical in real systems because future
references are unknown.
•   In practice, LRU is preferred as it approximates OPTIMAL.
Final Answer Summary
Algorithm   Page Faults
FIFO   15
LRU   12
OPTIMAL   9 ✅
********** 13 **********
--- page 14 ---
a.   Explain the Paging memory management technique.
Describe how paging eliminates the problem of external fragmentation
and explain the address translation mechanism with a neat diagram.
(10M)
Paging Memory Management Technique
Definition
b.
Paging is a memory management technique in which:
• Logical memory is divided into fixed-size pages
•   Physical memory is divided into fixed-size frames
• Pages are mapped to frames using a page table
Working of Paging
• A logical address is divided into:
o Page Number (p) → used to index the page table
o Offset (d) → specifies location within the page
Q5   • The page table maps page → frame
•   Physical address = Frame Number + Offset
CO-2 and
CO3; SO-
[20]
2;   Elimination of External Fragmentation
BL-3
and BL-4   •   In paging, memory is allocated in fixed-size blocks
• Any free frame can be assigned to any page
• Hence, no need for contiguous memory allocation
👉 Therefore:
• External fragmentation is eliminated
• Only internal fragmentation may occur (unused space within a
frame)
Address Translation Mechanism
Steps:
1. CPU generates a logical address (p, d)
2. Page number (p) is used to index the page table
3. Corresponding frame number (f) is obtained
4. Physical address is formed as (f, d)
Diagram (Conceptual)
Logical Address
┌──────────────┐
********** 14 **********
--- page 15 ---
│ Page | Offset│
└──────────────┘
↓
Page Table
(maps Page → Frame)
↓
┌──────────────┐
│Frame | Offset│
└──────────────┘
= Physical Address
↓
Physical Memory
Advantages
✔ Eliminates external fragmentation
✔ Efficient memory utilization
✔ Easy allocation of memory
Disadvantages
✖ May cause internal fragmentation
✖ Requires additional memory for page table
✖ Extra overhead in address translation
Conclusion
Paging provides an efficient way to manage memory by dividing it into
fixed-size units, eliminating external fragmentation and enabling
flexible memory allocation.
Consider the following snapshot of a system:
Process Allocation Max (A B   Available (A B
(A B C)   C)   C)
P0   0 1 0   7 5 3   3 3 2
P1   2 0 0   3 2 2   —
P2   3 0 2   9 0 2   —
P3   2 1 1   2 2 2   —
P4   0 0 2   4 3 3   —
Answer the following using Banker’s Algorithm:
1. Find the Need Matrix
2. Determine whether the system is in a safe state. If yes, write the
safe sequence
3.   If a request from process P1 (1, 0, 2) arrives, can it be granted
immediately? Justify
1. Need Matrix (Need = Max – Allocation)
********** 15 **********
--- page 16 ---
Allo
cati Max Nee
Pro
on (A B d (A
cess
(A B C) B C)
C)
0 1 7 5 7 4
P0
0   3   3
2 0 3 2 1 2
P1
0   2   2
3 0 9 0 6 0
P2
2   2   0
2 1 2 2 0 1
P3
1   2   1
0 0 4 3 4 3
P4
2   3   1
2. Safe State Check
Available = (3, 3, 2)
Step-wise:
• P1 → Need (1,2,2) ≤ (3,3,2) ✔ → New Available = (5,3,2)
• P3 → Need (0,1,1) ≤ (5,3,2) ✔ → New Available = (7,4,3)
• P4 → Need (4,3,1) ≤ (7,4,3) ✔ → New Available = (7,4,5)
• P0 → Need (7,4,3) ≤ (7,4,5) ✔ → New Available = (7,5,5)
• P2 → Need (6,0,0) ≤ (7,5,5) ✔
Safe Sequence:
P1 → P3 → P4 → P0 → P2
👉 System is in a SAFE state
3. Request by P1 = (1, 0, 2)
Check 1: Request ≤ Need
(1,0,2) ≤ (1,2,2) ✔
Check 2: Request ≤ Available
(1,0,2) ≤ (3,3,2) ✔
New Available after allocation:
(3,3,2) – (1,0,2) = (2,3,0)
Check Safe State Again:
• P1 → Need becomes (0,2,0) ≤ (2,3,0) ✔ → Available = (5,3,0)
• P3 → (0,1,1) ✖ (fails due to C=1 > 0)
• P2 → (6,0,0) ✖
• P4 → (4,3,1) ✖
********** 16 **********
--- page 17 ---
• P0 → (7,4,3) ✖
👉 No further process can proceed
Final Answer:
•
a.   Explain the concept of File Management in an Operating System.
Discuss different file organization methods and explain how files are
stored and accessed in secondary storage.
File Management in an Operating System
Concept
File Management is a component of the operating system responsible
for creating, storing, organizing, accessing, and protecting files on
secondary storage devices such as disks.
A file is a collection of related data stored on secondary storage and
b.   identified by a unique name.
Functions of File Management
•   File creation and deletion
•   File reading and writing
•   Directory management
• Access control and protection
Q6   • Storage allocation and space management
CO-3;
SO-2;   [20]
BL-2   File Organization Methods
1. Sequential Organization
and BL-4
• Data is stored in a linear sequence
• Access is done one record after another
Advantages:
• Simple and efficient for batch processing
Disadvantages:
• Slow for random access
2. Direct (Random) Organization
• Data is accessed using direct address or index
• Any record can be accessed directly
Advantages:
********** 17 **********
--- page 18 ---
•   Fast access
Disadvantages:
• Requires more complex implementation
3. Indexed Organization
• Uses an index table to locate records
• Combines features of sequential and direct access
Advantages:
•   Efficient searching
• Supports both sequential and random access
Disadvantages:
• Extra storage needed for index
File Storage in Secondary Storage
Files are stored on disks using different allocation methods:
1. Contiguous Allocation
•   File occupies continuous blocks
•   Fast access
2. Linked Allocation
•   File blocks are scattered but linked together
• No external fragmentation
3. Indexed Allocation
• Uses an index block containing addresses of all file blocks
•   Efficient and flexible
File Access Methods
• Sequential Access → Read/write in order
• Direct Access → Jump to any block directly
• Indexed Access → Use index to locate data
********** 18 **********
--- page 19 ---
Consider the following disk request queue (0–199):
95, 180, 34, 119, 11, 123, 62, 64
Initial head position = 50
Tasks:
1. Apply FCFS and SSTF disk scheduling algorithms
2. Show the order of execution
3. Calculate the total head movement
4. Identify which algorithm performs better and justify.
Given:
Request Queue: 95, 180, 34, 119, 11, 123, 62, 64
Initial Head Position = 50
## 1. FCFS (First Come First Serve)
Order of Execution:
50 → 95 → 180 → 34 → 119 → 11 → 123 → 62 → 64
Head Movements:
Dist
Mo
anc
ve
e
50
→ 45
95
95
→ 85
180
180
→ 146
34
34
→ 85
119
119
→ 108
11
11
→ 112
123
123
→ 61
62
********** 19 **********
--- page 20 ---
62
→ 2
64
Total Head Movement:
45 + 85 + 146 + 85 + 108 + 112 + 61 + 2 = 644
## 2. SSTF (Shortest Seek Time First)
Order of Execution:
50 → 62 → 64 → 34 → 11 → 95 → 119 → 123 → 180
Head Movements:
Move   Distance
50 → 62   12
62 → 64   2
64 → 34   30
34 → 11   23
11 → 95   84
95 → 119 24
119 → 123 4
123 → 180 57
Total Head Movement:
12 + 2 + 30 + 23 + 84 + 24 + 4 + 57 = 236
## 3. Comparison
• FCFS Total Movement = 644
• SSTF Total Movement = 236
Final Answer:
👉 SSTF performs better because it minimizes total head movement,
leading to faster disk access compared to FCFS.
Select any 4:
Q7   1. Explain any two Operating System services with suitable
CO-   examples.
1,CO2   Operating System Services
and CO3;   [20]
1. Process Management
SO-2;
The OS manages the creation, scheduling, and termination of processes.
BL-2
It allocates CPU time to processes and ensures smooth execution.
and BL-3   Example:
When multiple applications (e.g., browser, text editor) are running, the
OS schedules them using CPU scheduling algorithms.
********** 20 **********
--- page 21 ---
2. File Management
The OS handles file operations such as creation, deletion, reading,
writing, and organization of files in directories.
Example:
Creating a file, saving it, renaming it, or deleting it using the file
system.
2. What is a Process Control Block (PCB)? Explain its
components.
Process Control Block (PCB)
Definition:
A Process Control Block (PCB) is a data structure used by the
operating system to store all information about a process. It is created
when a process is initiated and deleted when the process terminates.
Components of PCB
1. Process ID (PID)
o Unique identifier assigned to each process
2. Process State
o Current state of the process (New, Ready, Running,
Waiting, Terminated)
3. Program Counter
o Address of the next instruction to be executed
4. CPU Registers
o Stores values of CPU registers (accumulator, index
registers, etc.) during context switching
5. CPU Scheduling Information
o Includes priority, scheduling queue pointers, etc.
6. Memory Management Information
o Information about memory allocation such as base/limit
registers or page tables
7. I/O Status Information
o List of I/O devices allocated and open files
8. Accounting Information
o CPU usage, execution time, process limits
3. What is a deadlock? Explain the concept of a Wait-For Graph.
Deadlock
Definition:
A deadlock is a situation in which a group of processes are blocked
indefinitely, each waiting for a resource held by another process in the
group.
Wait-For Graph (WFG)
********** 21 **********
--- page 22 ---
Concept:
A Wait-For Graph is a directed graph used to detect deadlocks in a
system with single-instance resources.
• Nodes represent processes
• A directed edge Pi → Pj indicates that process Pi is waiting for
a resource held by Pj
Working:
• Convert the Resource Allocation Graph (RAG) into a Wait-
For Graph by removing resource nodes
•   If the graph contains a cycle, then a deadlock exists
•   If there is no cycle, the system is deadlock-free
Example:
If:
• P1 is waiting for P2
• P2 is waiting for P3
• P3 is waiting for P1
Then a cycle is formed:
P1 → P2 → P3 → P1 → Deadlock exists
4. Define seek time and rotational latency in disk systems.
Seek Time and Rotational Latency
Seek Time
Seek time is the time required for the disk arm (read/write head) to
move from its current position to the desired track where the data is
stored.
Rotational Latency
Rotational latency is the time taken for the disk to rotate so that the
required sector aligns under the read/write head.
5. What is a directory? Explain different directory operations in an
operating system.
Directory in an Operating System
Definition:
A directory is a special file that stores information about files and
subdirectories, helping in organizing and managing files in a
hierarchical structure.
Directory Operations
1. Create Directory
o Creates a new directory in the file system
********** 22 **********
--- page 23 ---
2. Delete Directory
o Removes an existing directory (usually only if it is
empty)
3. Open Directory
o Allows access to the directory for reading its contents
4. Close Directory
o Closes the directory after operations are completed
5. Search Directory
o Searches for a file or subdirectory within the directory
6. List Directory Contents
o Displays all files and subdirectories present
7. Rename Directory/File
o Changes the name of a directory or file
8. Traverse Directory
o Allows navigation through the directory structure
********** 23 **********
````

## 2025-26 · Final-Exam · Sem 9 · Answer key · paper 11eda5b6240d

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_09/Final-Exam/Integrated_Computer_7032/Operating Systems/ANS_Operating Systems(702CO1C002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: ocr (22 pages), mean OCR confidence 86.6
- 12 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS

SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MBA Tech (AD/MBA Tech (Comp)
Year: II / III / V/Semester I1/Semester IX/Semester V(Exam Year: 2025-2026)

Subject: Operating Systems
Date: 28 Nov 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)

Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)

Instructions:
1. This question paper contains 22 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. | is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. Inall 5 questions to be attempted.
7. Assume Suitable data if necessary.

1|A | What do you mean by Dual mode Operation in OS? Explain with suitable 5

diagram?
Definition (2 mark)
Explanation (2 marks)
Diagram (1 Mark)

Dual Mode Operation is a feature of modern operating systems that allows the
CPU to operate in two distinct modes — User Mode and Kernel (Supervisor)
Mode — to ensure system security and stability. It prevents user programs

from directly accessing critical system resources.

e User Mode:
o Used to execute user applications.
o Access to hardware and system resources is restricted.

o System calls are used to request OS services.

e Kernel Mode:
o Used by the operating syst
o Has unrestricted access to
o Switching from user mo
interrupts or system calls.

em to execute privileged instructions.
hardware and system memory.
de to kernel mode occurs through

ser process
user mode
user process executing calls system call return from system call (mode bit = 1)
ah. J
— + 7
kernel EP Se res ;
| / kernel mode
(mode bit = 0)

| execute system call

ernel, 1 = user) determines the current

The mode bit in the CPU (usually 0=k
mode.

operating

RAKE KERR 7 Te RE EE
--- page 2 ---
When an interrupt or system call occurs

when control returns to the use:
Advantages / Purpose

¢ Protects OS and hardware from

¢ Maintains system stability and
¢ Ensures controlled access to re.

, the mode bit switches to kernel mode;

t process, it switches back to user mode.

faulty or malicious user programs.
security.

sources through system calls only.

B | A student writes the following Produc

semaphore full = 0, empty = N, mutex

Producer() {
while (true) {
produce_item(x);
wait(full);
wait(mutex);
insert(x);
signal(mutex);

>

signal(empty);
}
}

Consumer() {
while (true) {
wait(empty);
wait(mutex);
remove(x);
signal(mutex);
signal(full);
consume_item(x);

}

Identify the mistakes in semap)

er-Consumer code:

=1;

hore usage and correct the code.

Explanation: 1 mark
Corrected code : 4 marks

Consumer:

* The Producer should wait on em
inserting an item, then signal full (i

© The Consumer should wali

pty (wait for empty slot) before
indicate one more full slot).

ton full (wait for an item) before removing,

then signal empty (indicate one more empty slot).

semaphore full = 0, empty = N, mutex = |;

Producer() {
while (true) {
produce_item(x);
wait(empty);
Wwait(mutex);

// wait for an empty slot

REREEK EEE 2 FFRRERE EE
--- page 3 ---
insert(x);
signal(mutex);
signal(full); _// signal that a new item is available
}
}

Consumer() {

while (true) {
wait(full); // wait for an available item
wait(mutex);
remove(x);
signal(mutex);
signal(empty); _// signal that a slot is now free
consume_item(x);

}

C | What is deadlock prevention? Discuss any two strategies used for preventing
deadlocks in an operating system.

Deadlock Prevention 1 Mark
Strategy 2 Mark each (4 Marks)

Deadlock prevention is a proactive method of ensuring that the system is
designed in such a way that at least one of the necessary conditions for

deadlock can never occur.

The four necessary conditions for deadlock are:

1. Mutual Exclusion
2. Hold and Wait

3. No Preemption
4, Circular Wait

Deadlock prevention works by denying or controlling these conditions.

Invalidate one of the four necessary conditions for deadlock:
= Mutual Exclusion — not required for sharable resources (e.g., read-only

files); must hold for non-sharable resources
= Hold and Wait — must guarantee that whenever a process requests a
resource, it does not hold any other resources
* Require process to request and be allocated all its resources
before it begins execution, or allow process to request resources
only when the process has none allocated to it.
+ Low resource utilization; starvation possible

« No Preemption:
at is holding some resources requests another

* Ifa process thi
resource that cannot be immediately allocated to it, then all

resources currently being held are released
« Preempted resources are ‘added to the list of resources for which

the process is waiting
* Process will be restarted only when it can regain its old

resources, as well as the new ones that it is requesting
= Circular Wait:

--- page 4 ---
Impose a total ordering of all resource types, and require that

each process requests resources in an increasing order of
enumeration

D | Compare blocking, non-blocking,

explaining how each works in practic:
differences,

and asynchronous I/O operations by
, and provide examples to illustrate the

Each operation 1 Mark (3 Marks)
Example 2 Marks

Blocking I/O: Process suspended until I/O completed; easy to use and
understand; sufficient for simple sequential operations

Nonblocking I/O: Returns immediately with available data; implemented via
multi-threading; useful for user interfaces and buffered 1/0; uses select() to
check data availability

Asynchronous I/O: Process continues execution while I/O executes; difficult

to use but efficient; I/O subsystem signals process upon completion

Examples: Blocking for simple file reads, nonblocking for network servers
handling multiple connectio

ms, asynchronous for high-performance database
operations

2|A | Explain the Dining Philosophers problem and critically analyze the reasons

why semaphore-based implementations may result in deadlock or starvation.

Propose and justify a monitor-based solution that addresses these issues.

10

Description: 2 marks

Why semaphore solution Fail: 2 marks
Monitor solution: 6 marks

Description:

5 philosophers’ sit at a round table with a bowl of rice in the middle,
They spend their lives alternating thinking and eating.
They do not interact with their neighbors.

Occasionally try to pick up 2 chopsticks (one at a time) to eat from bowl

© Need both to eat, then release both when done

Why semaphore solution Fail:
e Although this solution
simultaneously,

a deadlock.

Suppose that all five philosophers become hungry at the same time and
each grab their left chopstick. All the elements of chopstick will now
be equal to 0. When each philosopher tries to grab their right chopstick,
they will be delayed forever

guarantees that no two neighbors are eating
it nevertheless must be rejected because it could create

Monitor solution:
monitor DiningPhilosophers
{

enum ( THINKING, HUNGRY, EATING)
state [5] ;

condition self [5];
void pickup (int i) {
state[i] = HUNGRY;

HREREKEK KK Q ReeKKA KEES
--- page 5 ---
test(i);
if (state[i] != EATING)
self[i].wait;

}

void putdown (int i) {
state[i] = THINKING;
// test left and right neighbors
test((i + 4) % 5);
test((i + 1) % 5);

void test (int i) {
if ((state[(i + 4) % 5] != EATING) &&
(state[i] == HUNGRY) &&
(state[(i + 1) % 5] != EATING) ) {
state[i] = EATING ;
self[i].signal () ;
}

}
sii iciiek SET ;
ae = THINKING; Dining Philasopher p 7 kali ag
} [st Cot RX / i

Diana Philosophen. putdo nC)’

B | Consider the following processes with their an‘val times, burst times, and | 10 | ~
priorities.

Process Arrival Time BurstTime Priority

Pl 0 10 2
P2 1 4 1
P3 3 U 3
P4 4 6 2
P5 6 3) 0

Considering pre-emptive priority scheduling algorithm (lower priority
numbers indicate higher priority), calculate the average turnaround
time and average waiting time for the given batch of processes.

ii. Considering round-robin scheduling algorithm (with time quantum =
4), calculate the average turnaround time and average waiting time for

the given batch of processes.

i

KKK KKREK 5 oe KE KE
--- page 6 ---
5 att

(GC =2 marks, Avg. TAT = 1.5 marks, Avg. WT = 1.5 marks)

(GC =2 marks, Avg. TAT = 1.5 marks, Avg. WT = 1.5 marks)

3 | A | Consider the following snapshot of a system running 5 processes:

Process | Allocation Max Available
A B CIA B CiA B

Pl 0 il 0 7) 5 3/3 3

P2 2 0 0 3 2 2

P3 3 0 2 9 0 y

P4 2 1 1 2 2 2

P5 0 0 2 4 3 3

RRKKEKAR KK 6 HKRKKERKEK
--- page 7 ---
Answer the following: -
i. How many resources of type A, B, C are there?
ii. Calculate the need matrix?
iii. Determine if the system is safe or not.
iv. What will happen if the resource request (1, 0, 0) for process P1 arrive,

can the system accept this request immediately?

Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks

Safe Sequence 3 Marks

Additional Request 3 Marks

Total Resources = Available + Allocation

ABC
105 7

Need Matrix = Max — Allocation

Process Need Matrix

A B
Cc
Pl 7 4 3
| P2 [1 2 2]
P3 6 0 0
[ P4 [0 1 1]
P5 4 3 1

Finding out system is safe or not. And if safe then the sequence of process

execution.
Check if Need matrix <= Available

Process P2 need ca be full filled

New Available = Available ~ Need [P2]

ABC

2 1 «0

After P2 complete, Available = New Available + Max[P2]
ABC

Sh wok 2

Next Process P4 need ca be full filled

New Available = Available — Need [P4]

ABC

Sy 2) ih

After P4 complete, Available = New Available + Max[P4]
ABC

7 4 3

Next Process P5 need ca be full filled
New Available = Available — Need [P5]

KEKE ERERE 7 HHKKREKKEKE
--- page 8 ---
ABC
3 ey
After P5 complete, Available = New Available + Max[P5]
ABC
7 4 °5

Next Process P1 need ca be full filled

New Available = Available — Need [P1]

ABC

0 20572

After P1 complete, Available = New Available + Max[P1]
ABC

7 5 5

Next Process P3 need ca be full filled

New Available = Available — Need [P3]

ABC

1l- S235

After P3 complete, Available = New Available + Max[P3]
ABC

10 5 7

If Available == Total Resources.

Then the system is in safe state and one of the sequences of the process
execution will be

P2 -> P4 -> P5 -> Pl -> P3

Showing the request of P1 (1,0,0) is acceptable or not.
In the provided available recourses that is

ABC

3 3 2

If we grant P1 (1,0,0) then new available will be
ABC

2535 2

With these available resources still, we can proceed with the safe sequences of
the all the process. That’s why we can grant P1 request immediately.

Explain the concept of paging and its purpose in memory management. With
the help of a neat diagram, describe how paging hardware translates a logical

address into a physical address. How the Translation Lookaside Buffer (TLB)
can enhances the performance of paging.

10

Marks Distribution:

Explanation of paging and need — 4 Marks
Paging hardware representation — 4 Marks
Role of TLB in paging — 2 Marks

Definition:

Paging is a memory management technique in which the logical (virtual)
memory of a process is divided into fixed-size blocks called pages, and the
physical memory (RAM) is divided into blocks of the same size called frames.

KKKKKEEERE 8 REEKRERKERE
--- page 9 ---
When a program is executed, its pages are loaded into available frames in main
memory, not necessarily in a contiguous manner.

Need for Paging:

1. Eliminates External Fragmentation:
Since pages and frames are of fixed size, there are no variable-sized
memory holes.

2. Efficient Memory Utilization:

Allows non-contiguous memory allocation — unuse'
processes are minimized.

3. Simplifies Memory Management:
The operating system can manage me
complex variable partitions.

4. Supports Virtual Memory:
Enables programs larger th

only required pages.

d gaps between
mory using page tables rather than

an physical memory to execute by loading

frame @
logical address 0x000
cpu als = frame f
| p => Oxfttt
— t t frame g
ae physical memory

page table
Role of Translation Lookaside Buffer (2 Marks)
« Every memory access in a paging system requires two memory

references:
o One to access the page table (to find the frame number).

o Another to access the actual data in memory.
e This doubles the access time.
To solve this, a Translation Lookaside Buffer (TLB) is used.

TLB:
e A special high-speed cache that stores recently used page table entries
(page—frame mappings).
« When a logical address is generated:
o Ifthe page number is found in the TLB (TLB hit), the frame
number is retrieved instantly.
o Ifnot found (TLB miss), the page table is accessed and the

TLB is updated.

4| A | Operating systems provide an environment for execution of programs and,
offers services to programs and users. Justify the statement by explaining the
operating system services with suitable diagram?

Justification (3 Marks)

HEEKKKREKE Q AK ERE REE
--- page 10 ---
Operating System Services any five (5 Marks)
Diagram (2 Marks)

An Operating System (OS) serves as an essential layer between the hardware
and the user/programs

» ensuring efficient, reliable, and convenient execution
of

applications.
ere multiple programs can run
ith hardware safely.

It provides an execution environment wh
concurrently, share resources, and interact w

The OS not only controls hardware but also deli
program execution and enhance

Thus, it can be viewed as both a resource manager and

vers services that simplify
user productivity.
a service provider.

Justification

Without the operating system, users would have to directly manage complex

hardware operations such as memory allocation, device communication, or
process synchronization.
The OS abstracts these complexities by offering well-defined services such as
program execution, file management, and interprocess communication,

By providing these services:

¢ The OS ensures convenie
handling hardware details.

e It ensures efficienc
allocated optimally.

¢ It ensures security and reliabili
protection mechanisms.

nce —— users can run programs without

Y — resources like CPU, memory, and I/O are

‘y — through error handling and

Hence, the OS creates a controlled, stable, and user-friendly environment for
both users and system programs.

Operating System Services (5 Marks)

1. Program Execution:
Loads, runs, and terminates programs. Manages process scheduling and
transitions.

2. VO

Operations:
Provides a uniform interface for input/output devices, abstracting
hardware details.

3. File System
Manages file creation, deletion,
secondary storage,

4. Inter-process
Enables process coordinatio
memory or message passing.

5. Error Detection

and Handling:
Monitors the system to detect and respond to hardware or software
€frors gracefully.

6. Resource

Dynamically allocates CPU time,
processes fairly.

Manipulation:
access control, and organization in

Communication (IPC):
n and data exchange through shared

Allocation:
memory, and I/O to competing

--- page 11 ---
7. Accounting:
Tracks system and re:
optimization.

source usage for performance monitoring and

8. Protection and Security:
Ensures data privacy and system integrity through controlled access and
authentication.

user and other system programs a
| Gul touch screen | command fine
i
user interfaces
L
system calls
7 ie OR Shh. Ae | eens ieee
execution \| operations Ed systems conmeunication {| allocation accounting }
=e 5
Ca j protection
| detection | | dans
services
operating system

; hardware

The OS provides a well-defined execution
complexity, managing concurrent activities,
and delivering reliable services.

Therefore, the statement is justified:
environment for execution of programs and

nvironment by hiding hardware
ensuring safe resource sharing,

“Operating Systems provide an
services to both programs and

users.”
nders 2069, 1212, 2296, 2800, 544, 1618,

A disk queue has requests on cyli
356, 1523. The disk head is currently positioned at cylinder 2150. The disk has

cylinders numbered from 0 to 4999.
Calculate the total head movement (in cylinders
requests using the following disk scheduling algorithms:
1. FCFS (First-Come-First-Served)
2. SCAN (Elevator Algorithm), assuming the h
towards the highest cylinder (4999).

3. C-SCAN (Circular SCAN), assuming the head is initially moving
towards the highest cylinder (4999).
Compare the performance of the three algorithm:
movement and discuss one major factor of comparison.

) required to service all

ead is initially moving

s based on their total head

Each algorithm 3 marks (9 marks)
Comparison 1 mark

--- page 12 ---
ae
gee
b ha
68
f
Mt +
é
Performance Comparison
ALGORITHM TOTAL MOVEMENT ‘CHARACTERISTICS
FCFS 8,285 Simple. fa'r, but hign seek time
SCAN 7,492 Fait, ptedictabve. moderate performance
C-SCAN, 9.917

More uniform wait tire higher movement

Performance Comparison: SCAN has the lowest head movement (7492

cylinders), making it the most efficient algorithm for this specific batch of

KEKE KEE 12 FRREKERERE
--- page 13 ---
requests and head position. FCFS performs better than C-SCAN, but SCAN is

the most efficient of the three.
Major Factor of Comparison: Uniformity of Wait Time
The major factor distinguishing SCAN and C-SCAN is the Uniformity of Wait

Time.
« SCAN: Causes a non-uniform wait ti
behind the reversing head (e.g., at cylinder 4900 after the head has just

left it going towards 0) will have to wait for the entire sweep to the
other end (0) and back, leading to a much longer latency than requests

near the ends.

» C-SCAN: Provides a more uniform wait t
requests in only one direction and immediatel,
start, C-SCAN ensures that a new request waits, at most, for the time it
takes the head to complete one full circular sweep, regardless of its
position on the disk. This predictability is highly valuable in high-

performance or heavy-load systems.

me. Requests that are waiting just

ime. By always servicing
y jumping back to the

5|A

Describe the concept of Message Passing by explaining its fundamental
primitives and addressing methods. Support your explanation with a neat

diagram of the general message format.

Message passing: 2 marks
Primitives: 3 marks
Addressing: 2 marks
Message format: 3 marks

Message Passing:

e@ When processes interact with one another, two fundamental

requirements must be satisfied: synchronization and communication.

e Processes need to be synchronized to enforce mutual exclusion;
cooperating processes may need to exchange information.

@ One approach to providing both of these functions is message passing.

e Message passing has the further advantage that it lends itself to
implementation in distributed systems as well as in shared-memory

multiprocessor and uniprocessor systems.

Primitives:

e We need to specify what happens to a process after it issues a send or
receive primitive.

e@ When a send primiti
possibilities: Either the
received, or it is not.

e Similarly, when a process issues a rece
possibilities:

1. Ifa message has previous
continues.
n either (a) the process is blocked until a

9. If there is no waiting message, the
message arrives, or (b) the process continues to execute, abandoning the

attempt to receive.
e Thus, both the sender and receiver can be blocking or nonblocking.

e Three combinations are common, although any particular system will
usually have only one or two combinations implemented:

ve is executed in a process, there are two
sending process is blocked until the message is

ive primitive, there are two

ly been sent, the message is received and execution

HEREKEEERE 13 KEKE EEK
--- page 14 ---
1. Blocking send, blocking receive: B.
until the message is delivered; thi
This combination allows for tight
2. Nonblocking send, blocking re:
the receiver is blocked until the
the most useful combination. It al
to a variety of destinations as qui
a message before it can do use
message arrives. An example is a
or resource to other processes.

3. Nonblocking send, nonblocking receive: Neither party is required to wait.

oth the sender and receiver are blocked
s is sometimes referred to as a rendezvous.
synchronization between processes.

ceive: Although the sender may continue on,
requested message arrives. This is probably
lows a process to send one or more messages
ckly as possible. A process that must receive
ful work needs to be blocked until such a
Server process that exists to provide a service

Addressing:

¢ The various schemes for sp

primitives fall into two cat
addressing.

© With direct addressing, the send primitive includes a specific identifier
of the destination process.

e The receive primitive can be
possibility is to require that the
process. Thus, the process must
a message is expected.

ecifying processes in send and receive
egories: direct addressing and indirect

handled in one of two ways. One
process explicitly designate a sending
know ahead of time from which process

¢ The other general approach is indirect addressing. In this case,
messages are not sent directly from sender to receiver, but rather are
sent to a shared data structure consisting of queues that can temporarily
hold messages.

e Such queues are generally referred to as mailboxes. Thus, for two
Processes to communicate, one Process sends a message to the
appropriate mailbox, and the other Process picks up the messages from
the mailbox.

Destination ID
Header Source ID
Control Information
Body | Message Contents

protection mechanisms, such as base and limit
registers, prevent illegal memory access. Illustrate your answer with an
example of process isolation. Consider six memory partitions of size 350 KB,
700 KB, 580 KB, 450 KB, and 300 KB in the same order. Considering

contiguous memory allocation, show how the first-fit, best-fit and worst-fit

algorithms will place the Processes of 360 KB, 600 KB, 425 KB, and 250 KB
(in order),

KEKE RK EK 14 RRKKAKEA ARE
--- page 15 ---
Marks Distribution:

Address protection mechanism 2 marks
Process isolation 2 marks

First Fit — 2 marks

Best Fit — 2 marks

Worst Fit — 2 marks

Hardware address protection is a mechanism in an operating system that
ensures each process accesses only its allocated memory space. This protection
is achieved through special hardware registers — primarily the base register
and limit register — which define the valid address range for each process.

Base Register: Holds the starting physical address of the process’s memory
space.

Limit Register: Specifies the size or maximum offset of the process’s
addressable memory range.

When a process generates an address (logical address), the hardware adds the

base value to it to get the physical address.

Before accessing memory, the hardware checks whether the logical address is
less than the limit. If it exceeds, the access is blocked, and a trap or exception

is raised.
base base + limit

ES yes
<

no

CPU address

trap to operating system
illegal addressing error memory

If 0 < Logical Address < Limit > Access Allowed
Else > Trap (Illegal Access)

Process Isolation Example
Consider two processes — P1 and P2.

P1 has Base = 1000 and Limit = 500, so it can access physical addresses 1000-
1499.

P2 has Base = 2000 and Limit = 400, so it can access addresses 2000-2399.

If Pl tries to access memory location 1800, the hardware check will detect it
is beyond its limit (1499), triggering a trap — thereby preventing illegal access
to P2’s memory region.

--- page 16 ---
REKEKE KEKE 16 KAKKKEEKER
--- page 17 ---
10

6!A| I. _ Illustrate and describe, using a suitable diagram, how a process
transitions through various states during its execution.
Il. Identify and explain the conditions under which each state transition

takes place.
Ul. Apply your understanding of process scheduling to explain two

scenarios in which a process may transition from the Running state to
the Ready state before completing its CPU burst.

I. 4 marks
I. 3 Marks
Iii. 3 Marks

Solution: i. State Transition diagram - (4 marks)

admitted

interrupt

1/0 or event wait

i. Transitions occurrence: (3 marks)

e New—Ready: admitted by long-term scheduler.

« Ready—Running: selected by CPU scheduler.

e Running— Waiting: I/O request, page fault, lock wait.

HERRERA 7 FRR EEE EE
--- page 18 ---
Waiting—Ready: I/O completes, event/interrupt occurs.
Running—Ready: preempted by higher priority or time slice expiry.
¢ Running—Terminated: process exit/abort.

tii. As stated in the Lifecycle diagram, a process may move from the
Running state to the Ready state before completing its CPU burst due
to pre-emption (I/O or event wait) or priority.

-based scheduling events
(interrupts). - (3 marks)

B | A system uses 4 frames for storin:
that all the page frames are initial]
given below:

2,3,4,5,3,2,6,7,3,2,3,4,8,7,4,3,2,3,4,7

§ process pages in main memory. Assume
y empty. Consider the page reference string

I. Simulate the page replacement using the FIFO algorithm.
I. Simulate the page replacement using the LRU algorithm.
Il. Simulate the page replacement using the Optimal algorithm.
IV. For each algorithm, calculate the total number of page faults.
V.

Based on your results, which algorithm performs best and why?

Marks Distribution:

2 marks each on every point of questions i.e. 5 * 2 = 10 marks
a)

FIFO
2 3 4 5 3 2 6 7 3 2
2 2 2 2 2b 3 (2 G 6 6 6
3 3 3 3 3 ee 7 ete (P| 7
4 4 4 4 4 4 3 3
[5] 5 5 5 5 5 2
3 4 8 z 4 3 2 3 4 7
6 4] [4] [a4 44 [al [2 BP a Ee
7 7 8 8 8} | 8 8 ei}
3 3 3 7 7 7 7 7 7 7
2 2 2 2 2 3 3 3 3 3
Total Page Fault: 14
b)

REREKKRERE ig RRERERE RAK
--- page 19 ---
LRU

2 3 4 5 3 2 6 7 3 2
2 102) 22) 32) 4) of tt 2 OR
of al {a} lal of 3] 3] 213) 3] 3] 0} 3} 11 8
ola (4 24 34 ole +e 36 36
ot sl tsi zal 3[_4] of 7] 17 27

3 4 8 7 4 3 2 3 4 7
| 2] 22] 3) of 7] 317 7 3{_ 7) 47] 57] oL7
g~al tlval 2{al 3[_3l 4[_s| ofl 1[3] OL 3] | 3) 4 3

4-7 yt] ofa 1 Cal 2Lal aL] ola] Lad 2 i

F F F F

Total Page Fault: 10

¢)
Optimal
2 3 4 5 3 2 6 7 3 2
2 2 4 C2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4
5 8 5 6 7 7 7
3 4 8 7 4 3 2 3 4 7
2 2 8 8 8 8 2 2 2 2
3) 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
_7 u 7 7 7 7 7 7 7 7
F F

Total Page Fault: 8

d) Total number of page faults:
FIFO:14, LRU:10, optimal: 8

e) Based on your results, which algorithm performs best and why?

Optimal minimizes page faults by always replacing the page that will not be

used for the longest time in the future. It uses future knowledge, making it
theoretical but ideal for benchmarking. LRU is better than FIFO because it
uses past usage patterns (replacing least recently used), while FIFO doesn’t

consider usage, just arrival order.

7A | What is resource allocation graph? Consider the following snapshot of a

system having 2 resources (RI having 1 instance and R2 having 2 instances)

and running 3 processes.

Process Allocation Request
RI R2 Ril R2
{Pi [1 0 [0 i |

HK KKKEKEKE 1O RK KE EEK
--- page 20 ---
P2 0 lei 0
[P3 [0 ela Oe]
Draw the resource allocation graph. Find if there is a deadlock or not? If there

is no deadlock then what will be the sequence of the process to get executed?

RAG description 3 marks
Draw RAG 4 marks

Safe Sequence 3 marks

i) What is resource allocation graph? [3 Marks]

© A useful tool in characterizing the allocation of resources to processes

is the resource allocation graph.

The resource allocation graph is a directed graph that depicts a state of

the system of resources and processes, with each process and each

resource represented by a node.

A graph edge directed from a process to a resource indicates a resource

that has been requested by the process but not yet granted.
Within a resource node, a dot is shown for each instance of that
resource.

Examples of resource types that may have multiple instances are VO

devices that are allocated by a resource management module in the Os.
A graph edge directed from a reusable resource node dot to a process

indicates a request that has been granted; that is, the process has been
assigned one unit of that resource.

Requests

. [ 7 |

‘ } Held b:

oe & ao? &

ie pa Py j
{a) Resource is requested (b) Resource is held

ii) Draw a resource allocation graph of the following table? [4 Marks]

--- page 21 ---
if there is a deadlock or not? If there is no deadlock then what will be
[3 Marks]

iii) Find
the sequence of the process to get executed?
There is no deadlock in the resource allocation graph.

The sequence of process to execute in safe sequence is

P3 -> Pl ->P2
Define a PCB. How can it help in enabling multi-tasking?
Definition 1 Mark

Explanation 4 marks

) is a data structure maintained by
al information about a

(1 mark)

Solution: A Process Control Block (PCB
the Operating System that contains all the essenti

process.

Multitasking means executing multiple processes seemingly at the same time

by rapidly switching the CPU between them.
Here’s how PCB makes that possible:

1. Context Saving:
a. When a running process is interrupted (e.g., due to time slice

expiry or I/O request),
the OS saves its current CPU state
PCB.
2. Context Restoration:
a. When the process is scheduled again,
state from its PCB.
The process resumes exactly where it left off.
3. Accurate Process Switching:
a. The PCB ensures that switching
switching) does not corrupt data or execution flow.

4. Tracking Multiple Processes:

(registers, PC, etc.) into its

the OS restores the saved

between processes (context

--- page 22 ---
a. Each process has its own PCB, so the OS can easily track,
suspend, resume, or terminate any process at any time.

(4 marks)

C | Summarize the main file attributes managed by a fi

le system and explain the | 5
common operations that can be performed on a file.

Key Attributes 2.5 marks
File Operations 2.5 marks

Key File attributes:

File attributes are pieces of information maintained by the file system about a
file and are typically kept in the directory structure on the disk.

Name: This is the onl
Identifier: This is au
file system.

Type: This is needed for s
Location: This is a
device.

Size: This records the current size of the file.

Protection: This controls who can perform operations such as reading,
writing, and executing the file.

Time, Date, and User Identification: Thi
security, and monitoring file usage.

y file information kept in human-readable form.
nique tag (a number) that identifies the file within the

ystems that support different types of files.

pointer that indicates the file's location on the storage

s data is maintained for protection,

Major File Operations:

The operating system
performed on files:

Create: This operation creates a new file.
Write: This operation writes data to
pointer location.

Read: This operation reads data from the fi
pointer location.

Delete: This operation deletes the file.
Open (Fj): This Operation involves searc
for the entry Fj and moving the content of that entry into memory.

Close (Fi): This operation moves the content of file entry Fi from memory
back to the directory structure on the disk.

Reposition (Seek): This Operation moves the read/write pointer within the
file.

Provides several major operations that can be

the file starting at the current write

le starting at the current read

hing the directory structure on disk

Truncate: This operation zeros the file length and keeps the attributes, but
discards the file's contents.

EREKEREEKK 22 RREEEKERHRE
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 0ce22de69961

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Operating Systems/ANS_Operating Systems(703CO1C002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Feb 2026
- Text: mixed (10 pages), mean OCR confidence 85.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 09 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compuslory
3. Out of the remaining question, attempt any 4 questions
4. In all 5 questions to be attempted
5. All questions carry equal marks
6. Answer each new question to be started on a fresh page
7. Figures in brackets on the right-hand side indicate full marks
8. Assume suitable data if necessary
Q1
Answer briefly:
a.   Describe the architecture of Thread. Differentiate User and Kernel
Threads.
Ans
CO-
2;SO-   5
1,6;BL-2
CO-   b.   Demonstrate the requirements to ensure concurrency in process
2;SO-   5
management.
1;BL-3
********** 1 **********

[Text in pictures on this page, read by OCR]
A thread is the smallest unit of CPU execution within a process.
Each thread represents an independent path of execution but shares the same resources (code, data, files)
of its parent process.

Thread Architecture Components

Each thread typically contains:
41. Thread ID (TID): Unique identifier for the thread.
2. Program Counter (PC): Indicates the next instruction to execute.
3. Register Set: Holds the current working variables and intermediate results.
4. Stack: Stores local variables, function calls, and return addresses.
5. Thread Control Block (TCB):
Similar to a Process Control Block (PCB) but for threads. It holds:

¢ Thread ID

¢ State (Ready, Running, Blocked)

¢ Stack pointer

« Priority

« Scheduling information

« Pointers to other threads of the same process
--- page 2 ---
c.   Discuss the concept of Monitors to ensure synchronization. (Include
diagram)
CO-
2;SO-   5
1,6;BL-2
d.   Explain the Buffering techniques and their types, and limitations.
CO-
4;SO-   5
1,6;BL-2
********** 2 **********

[Text in pictures on this page, read by OCR]
1, Mutual Exclusion Ensures that when one process is accessing a critical section (shared resource), Prevents race conditions —e.g., two

no other process can access it simultaneously. processes writing to the same file at
the same time.
2. Progress If no process is executing in its critical section and one or more processes wish to Guarantees fairness and avoids
enter, the selection of the next process to enter the critical section cannot be unnecessary delays.

postponed indefinitely.

3. Bounded Waiting Ensures that there is a limit on the number of times other processes can enter Prevents starvation (a process
their critical sections after a process has requested to enter its own. waiting forever).
4, Synchronization Mechanism to coordinate the execution order of processes that depend on each Example: A consumer must wait until
other's results. the producer has produced data
(Producer-Consumer problem).
5. Deadlock Freedom The system must avoid or prevent situations where two or more processes are Example: Process A waiting for B's
waiting indefinitely for each other to release resources. resource, while B waits for A's
resource.
6. Non-Preemption Once a process has acquired » ~~source (especially in a critical section), it should Ensures data integrity and prevents

not be forcibly taken away unt, Y eleases it voluntarily. Inconsistent states.

A Monitor is a high-level synchronization construct used to control access to shared resources in
concurrent programming.

It combines mutual exclusion and condition synchronization in an easier and safer way than
semaphores.

In simpler terms,

A monitor acts as a guarded room that only one process or thread can enter at a time to access
shared data.

2. Structure of a Monitor
A Monitor consists of:
1. Shared data variables (resources to be protected).
2. Procedures (functions) that operate on the shared data.
3. Synchronization mechanisms (e.g., condition variables) to control process waiting and signaling.
Only one process can execute any monitor procedure at a time — ensuring mutual exclusion

automatically.

Buffering is a technique used in operating systems and data communication to temporarily store data in a
memory area called a buffer while it is being transferred between two devices or processes that operate at

different speeds.

Purpose of Buffering
+ To match the speed difference between producer and consumer.
« To increase system efficiency and throughput.
« To smooth out data flow during input/output (I/O) operations.

Example:
When data is read from a disk (slow device) and written to memory (fast device), a buffer temporarily stores

data blocks so that the CPU can continue working without waiting for the disk.

2. How Buffering Works
« The producer (data sender) places data in the buffer.
+ The consumer (data receiver) retrieves data from the buffer.

* The buffer allows both to work asynchronously. improving concurrency.
--- page 3 ---
For the given table, which of the following scheduling algorithms
a.   (SRTF, RR(2), Pre-emptive priority scheduling with one as high
priority) will work best in the case of average waiting time and average
Q2   turnaround time? Require a Gantt chart and full steps.   10
CO-
2;SO-
1;BL-3
CO-   b.
3;SO-   Explain the requirements of memory management.
1,6;BL-3   Ans
Relocation, Sharing, Security, Physical and Logical Organisation   2+8
RAM with 5 frames and the reference string 3,8,2,7,9,2,6,1,8,9,2,6,2,1,3
for FIFO, OPT, and LRU to see which option is appropriate in the case
of the number of page faults. Show the complete working.
a.   2+8
Explain the disk performance parameters.
Q3
CO-
3;SO-
1;BL-3
CO-
1;SO-
1,6;BL-2   For a disk with 100 tracks, the initial position is at 50, and the pending
requests are 45, 25, 85, 11, 53, 66, 82, 28, 71. How much more does
SSTF traverse the distance compared to SCAN, CLOOK? (Assume for
SCAN and CLOOK, initially head moves outwards/larger cylinder) If
one adjacent track movement takes 0.2ms, what is the total time taken
for all requests for individual methods?
Explain the Microkernel vs Monolithic architecture. List two
advantages and two disadvantages of each. (Include diagrams)
********** 3 **********

[Text in pictures on this page, read by OCR]
1. Seek Time (Ts) The time taken by the disk arm to move the read/write Shorter seek time — Faster access.
head to the track containing the desired data.

2. Rotational Latency (Tr) The time taken for the desired sector of the disk to Depends on disk rotation speed (RPM).
rotate under the read/write head after the head
Teaches the correct track.

3. Transfer Time (Tt) The time required to actually transfer data between the Larger transfer rate — Better
disk surface and main memory once the head is in throughput.
position.

4. Access Time (Ta) Total time to access data from the disk. It is the sum of Formula: Ta = T's + Tr + Tt

seek time, rotational latency, and transfer time.

5, Disk Response Time Time from the moment a request is issued until data Affected by system load and request
(Tresp) transfer is complete. It includes access time plus scheduling.
command and queuing delays.

6. Disk Throughput The amount of data transferred per unit time. It Higher throughput — Better overall
(Bandwidth) measures how much useful data the disk can deliver. performance.
7. Disk Utilization The percentage of time the | is busy performing /0 High utilization indicates efficient use

operations. but may increase latency.
--- page 4 ---
b.
5+5
a.   10
Q4
CO-
2;SO-
1,6;BL-2   Identify the problem associated with the Bounded Buffer and suggest a
CO-   solution by using a suitable semaphore.
2;SO-
1,6;BL-1
********** 4 **********

[Text in pictures on this page, read by OCR]
2. Monolithic Kernel Architecture

Concept

In a Monolithic Kernel,

All basic OS services — such as process management, memory management, file systems, and device
drivers — run in kernel space as a single large process.

Everything runs in supervisor mode, sharing the same address space.

Characteristics
e Single large kernel running in privileged mode.
« All OS modules can communicate directly.
« Device drivers are part of the kernel.

Advantages
1. High Performance:
Direct communication between components — no message-passing overhead.
2. Easier Access to Resources:

All services run in the same address space, enabling faster execution.

Disadvantages
1. Poor Reliability:
A bug in one module (e.g., device driver) can crash the entire system.
2. Difficult Maintenance:

Updating or debugging is complex since all mods are tightly coupled.

3. Microkernel Architecture

Concept

A Microkernel contains only the minimal essential services in kernel space — such as:

« Inter-Process Communication (IPC)
+ Basic scheduling
+ Low-level memory management

All other services (file system, device drivers, network, etc.) run in user space as separate server
processes.

The idea: Keep the kernel small and move everything else to user space.
--- page 5 ---
produce(item) {
wait(empty);   // wait for at least one empty slot
wait(mutex);   // enter critical section
buffer[rear] = item;
rear = (rear + 1) % N;
count = count + 1;
signal(mutex);   // leave critical section
signal(full);   // indicate one more filled slot
}
consume() {
wait(full);   // wait for at least one filled slot
wait(mutex);   // enter critical section
item = buffer[front];
front = (front + 1) % N;
count = count - 1;
signal(mutex);   // leave critical section
signal(empty);   // indicate one more empty slot
return item;
}
********** 5 **********

[Text in pictures on this page, read by OCR]
Problem & solution for the Bounded Buffer (Producer-Consumer)
using semaphores

1) The problem
In the classic Bounded Buffer (producer—consumer) problem:
« Aproducer places items into a fixed-size buffer.
« Aconsumer removes items from that buffer.
Main issues if left unsynchronized:
1. Race condition on shared buffer data structures (head/tail/indexes, count, array) — simultaneous
access corrupts data.
2. Buffer overflow (producer writes when buffer is full).
3. Buffer underflow (consumer reads when buffer is empty).
4. Potential deadlock or starvation if synchronization is incorrect.
We need to enforce:
* Mutual exclusion for buffer access.
* Proper synchronization so producers wait if buffer is full and consumers wait if buffer is empty.

2) Semaphores used (standard solution)
Use three semaphores:
1. mutex — binary semaphore (or mutex) for mutual exclusion when accessing/modifying the buffe
¢ Initialized to 2.
2. empty — counting semaphore representing number of empty slots in the buffer.
¢ Initialized to n (buffer capacity).
3. full — counting semaphore representing number of filled slots in the buffer.
« Initialized to o.

Semantics:
¢ wait(s) / p(s) decrements s (blocks if s == 0).
¢ signal(s) / v(s) increments s (wakes a waiting process if any).
--- page 6 ---
b.   Define the terms Circular wait, Race condition, starvation, RAG, and   10
WFG.
Q5.   3+7
CO-   a.   Discuss the critical objectives for file organization. Explain the types of
4;SO-   file organization methods.
1;BL-2
********** 6 **********

[Text in pictures on this page, read by OCR]
1. Circular Wait

Definition:

Circular wait is one of the necessary conditions for a deadlock to occur.

It happens when a set of processes are waiting for resources in such a way that each process is holding
one resource and waiting for another resource held by the next process in the chain — forming a
circular chain.

3. Starvation

Definition:

Starvation (or Indefinite Blocking) occurs when a process waits indefinitely to acquire a resource
because other processes continuously get preference.

Example:

In a scheduling system with priorities, if higher-priority processes keep arriving, a lower-priority process may

never get CPU time.

Prevented by:

« Using aging: Gradually increasing the priority of waiting processes.

4. RAG (Resource Allocation Graph)

Definition:

A Resource Allocation Graph (RAG) is a directed graph used to represent resource allocation and

process requests in a system.

Components:
« Processes (P1, P2, ...) — represented as circles
« Resources (R14, R2, ...) — represented as rectangles
« Request edge (Pi — Rj): Process Pi requests resource Rj

« Assignment edge (Rj — Pi): Resource Rj is assigned to process Pi

5. WFG (Wait-For Graph)

Definition:
A Wait-For Graph (WFG) is a simplified version of the Resource Allocation Graph, used to represent
which process is waiting for which other process directly.

Construction:

¢ Derived from a RAG by removing resource nodes.
¢ If Process P1 is waiting for a resource held by Process P2, then:
--- page 7 ---
CO-
2;SO-
1,6;BL-2
3+7
b.
Explain the Process Scheduler and its various types in detail.
Q6   5+5
CO-
4;SO-   a.
Explain the concepts “Real-time Operating System” and “Distributed
1,6;BL-2
Operating System”.
CO-
2;SO-
1,6;BL-4
********** 7 **********

[Text in pictures on this page, read by OCR]
Objective Explanation

1, Fast Access Data should be easily and quickly retrievable when needed.

2. Efficient Storage Utilization Disk space should be used optimally, minimizing wastage and fragmentation.
3. Easy Update and Maintenance Insertion, deletion, and modification operations should be simple and efficient.
4, Security and Data Integrity Data should be protected from unauthorized access and corruption.

5. Flexibility The organization method should adapt to different types of processing

requirements (e.g., sequential, random access).

6. Minimum Redundancy Avoid storing duplicate data to reduce inconsistency and save space.
7. Reliability and Recovery Data should be recoverable in case of system failure or crash.
8. Support for Multiple Users The file system should allow concurrent access without conflicts.

ib

Method Access Type Speed Use Case Main Limitation

Sequential Sequential Slow for random Payroll, batch processing Inefficient for update:
Direct (Hashed) Random Fast Real-time lookup Hash collisions
Indexed Sequential Sequential + Random Moderate Database systems Extra index maintene

Clustered Sequential + Random Fast (for related data) Database joins Complex structure

3. Objectives of Process Scheduling

Objective Description

1. Fairness Every process should get a fair share of CPU time.

2. Efficiency Keep the CPU as busy as possible (maximize CPU utilization).
3. Response Time Minimize the time taken to start responding to user input.

4. Turnaround Time Reduce the total time taken to complete each process.

5. Throughput Maximize the number of processes completed per unit time.

6. Waiting Time Minimize the time a process spends waiting in the ready queue.

7. Priority Handling Ensure high-priority tasks are executed first.
--- page 8 ---
10
b.
Discuss Banker’s Algorithm. What is the content of the Need Matrix for
the arrangement of resources below? Is the system in a safe state? If the
request from P1 arrives for (0, 4, 2, 1), Can the request be granted
immediately? What is the process termination sequence order?
Availability of Resources (A:1 B:5 C:2 D:0)
5+5
a.   Illustrate the working of Mutex Locks and Semaphores. Explain
Semaphore types.
Q7
CO-
2;SO-
1,6;BL-3
CO-
3;SO-
1,6;BL-2
********** 8 **********

[Text in pictures on this page, read by OCR]
Feature Real-Time OS (RTOS) Distributed OS (DOS)

Primary Goal Ensure timely task completion Manage multiple computers as a single
system

Time Constraint Strict deadlines (hard/soft real-time) Not necessarily time-critical

Task Management Priority-based scheduling Coordination across nodes

Transparency N/A High (location, replication, access,
concurrency)

Reliability Requirement Very high, especially for hard real-time High fault tolerance across nodes

Example Applications Airbags, pacemakers, industrial Cloud systems, distributed databases,

controllers cluster computing

1. Mutex Locks

Definition:

A Mutex (Mutual Exclusion) Lock is a binary mechanism used to ensure that only one process or
thread can access a critical section at a time.

¢ Binary: 0 (locked) or 1 (unlocked)

e Ensures mutual exclusion to prevent race conditions.

Working of Mutex Lock
1. Acquire / Lock:
Aprocess checks the mutex.
e If mutex = 1 (unlocked) — process locks it ( mutex = @ ) and enters critical section.
¢ If mutex = @ (locked) — process waits until it becomes unlocked.
2. Critical Section:
Only the process holding the mutex executes the critical section safely.
3. Release / Unlock:
After completing, the process sets mutex = 1, ey ving another waiting process to acquire it.
--- page 9 ---
Explain Demand Paging with the help of virtual memory.
Interpret the steps to handle the page fault that occurs while memory
b.   referencing.
5+5
********** 9 **********

[Text in pictures on this page, read by OCR]
2. Semaphores

Definition:

A Semaphore is an integer variable used for process synchronization and mutual exclusion.

It is used to control access to shared resources by multiple processes in a concurrent system.

Key Operations:
41. wait() / P() / down():
» Decreases semaphore value by 1.
° If the result < 0 — the process is blocked.
2. signal() / V()/ up():
« Increases semaphore value by 1.
« If<0-— wakes up a waiting process.

Type Description Use Case

Binary Semaphore Can take values 0 or 1; behaves like a Mutual exclusion in critical section.
mutex.

Counting Semaphore Can take any non-negative integer value; Managing access to multiple identical
represents number of available resources, e.g., 5 printers shared among

resources. processes.

1. Introduction to Virtual Memory

Virtual Memory (VM):
A technique that allows execution of processes larger than the available physical memory by using
secondary storage (disk) to extend memory.

Key Idea:

« Programs use a virtual address space, which is mapped to physical memory frames.

* Only the needed pages are loaded into RAM, the rest stay on disk.

2. Demand Paging

Definition:
Demand Paging is a memory management scheme in which pages are loaded into memory only when
they are needed (i.e., when a process tries to access them).

» Pages are not loaded in advance.

+ Reduces I/O overhead and memory usage.

e Lazy loading: “Bring a page on demand.” an

Term Meaning

Page Fixed-size block of virtual memory (e.g., 4 KB)
Frame Fixed-size block of physical memory (same size as page)
Page Table Maps virtual page numbers to frame numbers

Page Fault Occurs when a process tries to access a page not in memory
--- page 10 ---
When a page fault occurs, the OS must fetch the required page trom disk into memory. Ihe steps are as
follows:
1. Detect Page Fault
« CPU generates a page fault interrupt because the referenced page is not in physical memory.
2. Suspend Process
« Current process is suspended; CPU is freed for other tasks.
3. Check Validity
« Verify if the memory access is legal:
If illegal — terminate process (segmentation fault).
¢ lIflegal — proceed.
4. Find a Free Frame
¢ Search for an empty frame in physical memory.
« Ifo free frame — use page replacement algorithm (e.g., LRU, FIFO).
5. Read Page from Disk
« Copy the required page from backing store (disk) to the allocated frame in RAM.
6. Update Page Table
« Mark the page as present in memory.
« Update the frame number in the page table.
7. Restart the Instruction Ny
« The CPU re-executes the instruction that caused the page fault.

FRR ICR 7 OI HOH
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 0700f0abf2e7

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_AIDS_7056/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 70.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MASTER OF BUSINESS ADMINISTRATION
IN TECHNOLOGY MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA
Tech (Comp)
Year: II / III / V/Sem 3 Re-exam/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1 A What are the various components of an Operating System? Briefly explain 5
with the help of a diagram.
Explanation of components (any four) 1 mark each (4 Marks)
Diagram   1 mark
The main components of an operating system are:
1. Process Management
o Handles creation, scheduling, and termination of processes.
o Ensures fair CPU allocation among processes.
2. Memory Management
o Manages primary memory allocation and deallocation.
o Keeps track of memory usage and optimizes performance.
3. File Management
o Organizes, stores, retrieves, and manages data in files.
o Maintains directories and provides file access control.
4. Device Management
o Controls and coordinates input/output devices via device
drivers.
o Ensures efficient and conflict-free resource usage.
5. Security and Protection
o Protects data and system resources from unauthorized
access.
o Implements authentication, authorization, and encryption
mechanisms.
********** 1 **********
--- page 2 ---
B Analyze the code for Process Pi and Pj and state whether it satisfies the 5
three requirements for the solution to the critical section problem or not.
Justify your answer.
For process Pi:
do {
flag[i] = true;
turn = j;
while (flag[j] && turn == j);
// Critical Section
flag[i] = false;
// Remainder Section
} while (true);
For process Pj:
do {
flag[j] = true;
turn = i;
while (flag[i] && turn == i);
// Critical Section
flag[j] = false;
// Remainder Section
} while (true);
Final verdict: 2 marks
Justification each condition: 1 Mark (3 marks)
Yes, it satifies all the three conditions of mutual exclusion.
A. Mutual exclusion is preserved
Pi enters CS only if:
either flag[j] = false or turn = i
B. Progress requirement is satisfied: If a process wants to enter the
critical section, it waits only if the other process is inside or waiting
to enter, and it is the other process’s turn.
If the other process is not interested (flag[j] == false), then the first
process proceeds immediately without waiting.
Also, the turn variable guarantees that the processes alternate access
if both want to enter, so no process can block the other indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
user and other system programs

GUI touch screen | command line

user interfaces

system calls

program vO file a resource
communication

. A a accounting
execution operations systems allocation

protection
and
security

error
detection
services

operating system

hardware
--- page 3 ---
C. Bounded-waiting requirement is met: The turn variable acts as a fair
"token" passed between the two processes, ensuring that after one
process finishes, the other will eventually get the turn.
C Describe the process of deadlock recovery after detection. What are the
common methods used? Explain any two.
Deadlock Recovery 1 mark
Methods 4 marks
Process of Deadlock Recovery (1 Marks)
Once a deadlock is detected (usually using the resource allocation graph or
Banker’s algorithm), the OS performs the following steps:
1. Identify deadlocked processes and resources.
2. Select a recovery method — terminate processes, preempt
resources, or roll back processes.
3. Recover the system by releasing held resources and restarting
affected processes.
4. Resume normal operation.
Common Methods of Deadlock Recovery
The two main categories are:
1. Process Termination — killing one or more processes involved in
the deadlock.
2. Resource Preemption — temporarily taking resources away from
processes.
Other less common methods:
• Process Rollback (restore to a safe checkpoint).
• Manual Intervention (in simple or embedded systems).
(i) Process Termination (2 Marks)
• Concept:
Abort one or more processes involved in the deadlock until the cycle
is broken.
• Approaches:
1. Abort all deadlocked processes.
▪ Simple but costly; results in loss of work.
2. Abort processes one at a time until the deadlock cycle is
resolved.
•   Selection   Criteria:
When choosing which process to terminate, the OS considers:
1. Process priority and importance.
2. Amount of CPU time consumed.
3. Number and type of resources held.
4. Whether the process can be restarted easily.
• Advantages:
1. Straightforward and guaranteed recovery.
• Disadvantages:
1. May lead to loss of significant computation progress.
2. System performance temporarily degrades.
(ii) Resource Preemption (2 Marks)
• Concept:
Temporarily take away (preempt) resources from some processes
and give them to others to break the deadlock.
********** 3 **********
--- page 4 ---
• Steps Involved:
1. Select a victim process – the one whose resource preemption
has the least cost.
2. Save its state (checkpoint) – so it can be restarted later.
3. Reassign its resources to other waiting processes.
•   Challenges:
1. Rollback: The victim process must be rolled back to a safe
state.
2. Starvation: A process may be repeatedly chosen as a victim;
hence, the OS must keep track of how often each process is
preempted.
• Advantages:
1. Allows partial progress of other processes.
• Disadvantages:
1. Complex to implement and may lead to instability if done
repeatedly.
D Describe the concept of I/O management in an operating system and apply
your knowledge to identify key factors that can enhance I/O performance.
I/O Management 2 Marks
Factors 3 Marks (at least 3)
I/O management is a major component of operating system design that
handles the interaction between the computer system and I/O devices.
Key Components:
•   Ports, Buses, Controllers: Connect various devices to the system
• Device Drivers: Encapsulate device-specific details and present
uniform device-access interface to I/O subsystem
• I/O Hardware: Manages incredible variety of devices (storage,
transmission, human-interface)
I/O Methods:
•   Polling: CPU repeatedly checks device status (inefficient for slow
devices)
•   Interrupts: Device signals CPU when ready (efficient, used for
time-sensitive operations)
• DMA (Direct Memory Access): Transfers data directly between
device and memory without CPU involvement
I/O Operations:
• Blocking I/O: Process suspended until I/O completed
• Nonblocking I/O: Returns immediately with available data
• Asynchronous I/O: Process continues while I/O executes
Factors for Improving I/O Performance
1. Reduce Context Switches
• Minimize switching between processes during I/O operations
2. Reduce Data Copying
• Minimize copying data between kernel and user space
3. Reduce Interrupts
• Use large transfers instead of multiple small ones
• Employ smart controllers
• Use polling when appropriate
4. Use DMA (Direct Memory Access)
• Allow devices to transfer data directly to/from memory
********** 4 **********
--- page 5 ---
• Frees CPU from data transfer burden
5. Use Smarter Hardware Devices
•   Intelligent controllers with built-in processing capabilities
6. Balance System Resources
• Balance CPU, memory, bus, and I/O performance for highest
throughput
7. Move User-mode Processes to Kernel Threads
• Reduces overhead for frequently used I/O operations
8. Implement Efficient Buffering and Caching
• Buffer data to handle speed/size mismatches
• Cache frequently accessed data on faster devices
2 A Examine the synchronization problem in operating systems, identifying the
challenges it creates. Analyse how counting semaphores provide a
structured solution and resolve these issues in the Readers–Writers
problem.
Explain Synchronization Problem in Detail [4 marks]
Readers-Writers Problem [6 marks]
The Synchronization Problem arises in a multi-process or multi-threaded
environment when multiple processes concurrently access and manipulate
shared data. The core issue is that the final result of the execution depends
on the specific order in which instructions are interleaved, leading to
unpredictable and inconsistent results. This is known as a race condition.
Causes and Consequences:
1. Race Condition: Occurs when several processes access and modify
the same shared data concurrently, and the outcome of the execution
depends on the order of access.
2. Data Inconsistency: The primary consequence is that the shared data
may end up in a corrupted or inconsistent state.
Example (The Critical Section Problem): A simple counter shared by two
threads, one incrementing and the other decrementing. The operations
(Read → Modify → Write) are not atomic. If the operations are interrupted
and interleaved, the final count can be incorrect (e.g., instead of
100→101→100, it might become 100→101→101).
Requirements for a Correct Solution:
1. Mutual Exclusion: Only one process can be executing in its critical
section at any time.
2. Progress: If no process is executing in its critical section and some
processes wish to enter, then only those processes not in their
remainder sections can participate in deciding which will enter next,
and this selection cannot be postponed indefinitely.
3. Bounded Waiting: There must be a limit on the number of times
other processes are allowed to enter their critical sections after a
process has made a request to enter its critical section and before
that request is granted.
B. Counting Semaphore for Readers-Writers Problem [6 marks]
The Readers-Writers Problem is a classic synchronization problem where
multiple processes try to access a shared database.
● Readers only read the data and can do so concurrently.
● Writers modify the data and must have exclusive access (no other
reader or writer allowed).
********** 5 **********
--- page 6 ---
A Counting Semaphore (and a Binary/Mutex semaphore) can be used to
manage this access
Writer Process Logic: The writer needs exclusive access. It only needs to
wait on the general lock (wrt).
do {
wait(wrt);
// Writing is performed
signal(wrt);
} while (TRUE);
Reader Process Logic: Readers need to coordinate using readcount and
the wrt lock.
do {
wait(mutex);   // 1. Lock the readcount variable
readcount++;
if (readcount == 1) {   // 2. First reader locks out the writer
wait(wrt);
}
signal(mutex);   // 3. Unlock the readcount variable
// Reading is performed
wait(mutex);   // 4. Lock the readcount variable
readcount--;
if (readcount == 0) {   // 5. Last reader signals the writer
signal(wrt);
}
signal(mutex);   // 6. Unlock the readcount variable
} while (TRUE);
B Consider the following set of processes, each with varying arrival times
and burst times.
Process   Arrival Time   Burst Time
P1   0   7
P2   2   4
P3   4   1
P4   5   4
P5   6   3
i. Using the SRTF scheduling algorithm, determine the average
waiting time and average response time.
ii. Using the Round-Robin scheduling algorithm with time quantum =
3, determine the average waiting time and average response time.
********** 6 **********
--- page 7 ---
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
3 A Consider the following snapshot of a system running 5 processes:
Pro- Allocation   Max   Available
cess A   B   C   D A   B   C D A B   C D
P0   0   0   1   2 0   0   1   2 1   5   2   0
P1   1   0   0   0 1   7   5   0
P2   1   3   5   4 2   3   5   6
P3   0   6   3   2 0   6   5   2
********** 7 **********
--- page 8 ---
P4   0   0   1   4 0   6   5   6
Answer the following: -
i. How many resources of type A, B, C, D are there?
ii.   Calculate the need matrix?
iii.   Determine if the system is safe or not.
iv.   What will happen if the resource request (0, 4, 2,0) for process P1
arrive, can the system accept this request immediately?
Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks
Safe Sequence 3 Marks
Additional Request 3 Marks
The total number of resources of each type is calculated as:
Total = Allocation (sum) + Available
• A = 2 + 1 = 3
• B = 9 + 5 = 14
• C = 10 + 2 = 12
• D = 12 + 0 = 12
Thus, total system resources = (3, 14, 12, 12).
vi) Need Matrix
Process   A   B   C   D
P0   0   0   0   0
P1   0   7   5   0
P2   1   0   0   2
P3   0   0   2   0
P4   0   6   4   2
vii) Safe State Check
Starting with Available = (1, 5, 2, 0):
• P0 runs → Work = (1, 5, 3, 2)
• P3 runs → Work = (1, 11, 6, 4)
• P2 runs → Work = (2, 14, 11, 8)
• P4 runs → Work = (2, 14, 12, 12)
• P1 runs → Work = (3, 14, 12, 12)
Safe sequence = <P0, P3, P2, P4, P1>. Therefore, the system is SAFE.
viii) Resource Request (0, 4, 2, 0) by P1
********** 8 **********
--- page 9 ---
• Request (0, 4, 2, 0) ≤ Need(P1) = (0, 7, 5, 0) ✔
• Request (0, 4, 2, 0) ≤ Available (1, 5, 2, 0) ✔
After tentative allocation: Available = (1, 1, 0, 0).
Safety test sequence:
• P0 → Work = (1, 1, 1, 2)
• P2 → Work = (2, 4, 6, 6)
• P3 → Work = (2, 10, 9, 8)
• P4 → Work = (2, 10, 10, 12)
• P1 → completes.
Safe sequence = <P0, P2, P3, P4, P1>. Hence, the request CAN be
granted immediately.
B Describe the concept and working of a Translation Lookaside Buffer (TLB) 10
in a paging system. Explain how address translation is carried out with and
without TLB.
Definition and Need of TLB (2 Marks)
address translation without TLB (4 Marks)
address translation with TLB (4 Marks)
• A Translation Lookaside Buffer (TLB) is a special high-speed cache
that stores recent translations of virtual page numbers (VPNs) to
physical frame numbers (PFNs).
•   In a paging system, every memory access requires a page table lookup
to translate the virtual address into a physical address.
• This lookup takes extra time (additional memory access), which slows
down the system.
• The TLB reduces this delay by caching frequently used page table
entries — providing fast access to address translations.
Address translation is carried out with TLB.
********** 9 **********

[Text in pictures on this page, read by OCR]
frame e

logical address physical address 0x000
frame f
cpu slp | a |
p — Oxfff
f frame g

physical memory

page table
--- page 10 ---
Address translation is carried without TLB.
4 A Provide a comparative analysis of the Monolithic and Layered architectures 10
of Operating Systems. Include appropriate diagrams to support your
explanation.
Monolithic Architecture (3 Marks)
Layered Architecture (3 Marks)
Comparative Analysis (4 Marks)
Operating System architecture defines the structure and organization of the
OS components and their interaction with each other and hardware.
Two commonly used architectures are Monolithic and Layered
architectures.
Monolithic Architecture (3 Marks)
Explanation:
•   In a monolithic system, the entire operating system is working in a
single kernel space.
•   All system components such as   file management, process
scheduling, memory management, and device drivers are integrated
into one large block of code that runs in supervisor mode.
•   It provides high performance because there are no inter-layer
overheads, but poor modularity and difficult debugging.
Diagram:
********** 10 **********

[Text in pictures on this page, read by OCR]
logical

address
CPU +> pid

page frame

number number

E TLB hit physical

BI address
Lt | 4d }—

TLB

TLB miss

a physical
memory

page table
--- page 11 ---
Advantages:
• High execution speed (no layer overhead).
•   Efficient direct access to hardware.
Disadvantages:
•   Difficult to maintain and debug.
• Poor security and modularity—failure in one module may crash the
entire system.
Examples:
MS-DOS, UNIX (early versions), Linux (partially monolithic).
Layered Architecture (3 Marks)
Explanation:
•   In layered architecture, the OS is divided into multiple layers, each
built upon the lower one.
• Each layer performs specific functions and interacts only with its
adjacent layers.
• The bottom layer deals with hardware, while the top layer provides
user interfaces.
Diagram:
********** 11 **********

[Text in pictures on this page, read by OCR]
applications

glibc standard c library

system-call interface
file CPU
systems scheduler
networks memory
(TCP/IP) manager
block character
devices devices

device drivers

hardware
--- page 12 ---
Advantages:
•   Better modularity and maintainability.
•   Easier to test and debug individual layers.
• Higher security and reliability due to restricted communication.
Disadvantages:
• Slower execution due to layer-to-layer communication overhead.
•   Difficult to design and define proper boundaries between layers.
Examples:
THE Operating System, Windows NT, OS/2.
Comparative Analysis (4 Marks)
Feature   Monolithic OS   Layered OS
Structure   Single large kernel Multiple   layers   with   clear
interfaces
Performance   High   (no Slightly slower (due to layering)
overhead)
Modularity   Poor   Excellent
Maintainability Difficult   Easier to maintain and modify
Security   Low   (shared High   (restricted   inter-layer
kernel)   access)
Examples   MS-DOS, UNIX   Windows NT, THE OS
Conclusion:
Monolithic architecture emphasizes performance, whereas layered
architecture   emphasizes   modularity,   reliability,   and   security.
Modern operating systems often adopt a hybrid approach, combining the
speed of monolithic design with the structure of layered models.
B A disk queue with requests on cylinders 85, 170, 45, 130, 25, 115, 72, 58 10
needs to be serviced. The disk head is initially at cylinder 60, and the disk
has cylinders numbered 0-199. Calculate the total head movement for:
1. FCFS
2. SSTF
3. SCAN (assuming initial direction towards cylinder 199)
4. C-SCAN (assuming initial direction towards cylinder 199)
Compare the performance of each algorithm and determine which suits best
for this scenario.
********** 12 **********

[Text in pictures on this page, read by OCR]
application file device user
program system driver mode

messages: messages

CPU
scheduling

memory
managment

kernel
mode

interprocess
communication

microkernel

hardware
--- page 13 ---
Each Algorithm 2 Marks
Comparison 2 Marks

RK KKK RK KK 13 2h KKK RK Kk KK
--- page 14 ---
Best Algorithm for This Scenario:
SSTF provides the best performance with only 180 cylinders of movement,
making it ideal for this scenario where minimizing seek time is the priority
and the request queue is relatively small, reducing starvation risk.
5 A Describe the concept of monitors in process synchronization with internal 10
structure and functioning. Explain how monitors manage process
coordination using condition variables and synchronization primitives.
Concept of Monitors (2 Marks)
Internal Structure of a Monitor (4 Marks)
Functioning and Coordination (4 Marks)
In concurrent programming, monitors are high-level synchronization
constructs that provide a convenient and safe mechanism for process
coordination.
They encapsulate shared data, the procedures that operate on that data, and
the synchronization between concurrent processes — all within a single
module.
Monitors eliminate many of the errors possible when using low-level
primitives such as semaphores.
A monitor is a software module with:
• Shared data variables.
• A set of procedures (only one process can execute inside the
monitor at a time).
• Condition variables for process synchronization.
It ensures mutual exclusion automatically — no two processes can execute
monitor procedures simultaneously.
********** 14 **********

[Text in pictures on this page, read by OCR]
Performance Comparison

Algorithm Total Movement Characteristics

FCFS 572 Simple, fair, but high seek time

SSTF 188 Minimal movement, risk of starvation
SCAN 313 Fair, predictable, moderate performance

C-SCAN 396 More uniform wait time, higher movement
--- page 15 ---
Internal Structure of a Monitor (4 Marks)
Components:
1. Shared Data: Variables accessible only through monitor procedures.
2. Procedures: Define operations that can be performed on shared data.
3. Initialization Code: Sets up initial values for data and conditions.
4. Condition Variables: Used for process synchronization (e.g., x, y).
Pseudocode syntax of a monitor:
monitor monitor-name
{
// shared variable declarations
function P1 (…) { …. }
function P2 (…) { …. }
function Pn (…) {……}
initialization code (…) { … }
}
Diagram of Monitor Structure (1 Mark)
+-----------------------------------+
Functioning and Coordination (4 Marks)
Condition Variables and Synchronization:
• Condition variables allow a process to wait for a certain condition
to become true.
• Two basic operations are used:
o wait(c) → Process is suspended until another process signals
condition c.
o signal(c) → Wakes up one waiting process on condition c.
• Mutual exclusion: Achieved automatically; only one process
executes within the monitor.
•   Synchronization: Managed through wait and signal on condition
variables.
• No busy waiting: Blocked processes are placed in a waiting queue
inside the monitor.
Advantages of Monitors
********** 15 **********
--- page 16 ---
• Provides structured and safer synchronization compared to
semaphores.
•   Eliminates errors like deadlocks and race conditions caused by
improper semaphore use.
• Promotes modularity and clarity in concurrent program design.
B Explain how fragmentation affects memory management in operating 10
systems and illustrate the different types of fragmentation with suitable
example. A system has five memory partitions of sizes 110 KB, 480 KB,
210   KB,   350   KB,   and   140   KB   respectively.
A sequence of processes arrives for allocation in the following order: P1 =
100 KB, P2 = 200 KB, P3 = 300 KB, P4 = 140 KB, and P5 = 50 KB.
Considering Contiguous memory allocation, show the final process-to-
partition allocations using First-Fit, Best-Fit, and Worst-Fit memory
allocation strategies.
Marks Distribution:
Fragmentation 2 Marks
Types 2 marks
First Fit – 2 marks
Best Fit – 2 marks
Worst Fit – 2 marks
Fragmentation is a memory management problem that occurs when free memory
space is broken into small, non-contiguous blocks over time. It reduces the
system’s ability to allocate large continuous memory blocks to new processes,
even if total free memory is sufficient.
Fragmentation affects memory utilization and system performance, leading to
inefficient use of available RAM.
Types of Fragmentation
(a) Internal Fragmentation
Definition: Occurs when a fixed-sized memory block allocated to a process is
larger than the process’s actual memory requirement.
Cause: Fixed partitioning or paging schemes with block sizes larger than needed.
Effect: Wasted space inside the allocated partition.
Example:
Suppose a system allocates 4 KB blocks, and a process needs only 3.6 KB.
→ Unused memory = 0.4 KB per process
This 0.4 KB inside the allocated block is internally fragmented.
External Fragmentation
Definition: Occurs when total free memory exists but is scattered in non-
contiguous blocks, preventing allocation of large processes.
Cause: Dynamic memory allocation where processes are loaded and removed
frequently.
Effect: Wasted space outside allocated partitions.
Example:
Assume memory = 100 MB total. Free blocks: 20 MB + 15 MB + 10 MB (non-
contiguous).
********** 16 **********
--- page 17 ---
A process requesting 40 MB cannot be allocated, though 45 MB is free in total.
6 A   I.   Apply your understanding of process scheduling to compare Long- 10
term and Short-term schedulers in terms of their purpose, execution
frequency, speed, alternate names, and where process selection
occurs (main or secondary memory).
II.   Apply the concepts of process scheduling to justify why time-
sharing systems rely more on Short-term scheduler, while batch-
processing systems depend more on Long-term scheduler.
I.   5 Marks (One mark for each criteria)
II.   5 Marks
Solution:
i. Following are the differences between a LTS and STS:- (5 marks)
********** 17 **********
--- page 18 ---
Aspect   Long-Term Scheduler   Short-Term Scheduler
Frequency   Runs less frequently.   Runs very frequently.
Speed   Slower, as it involves   Faster, as it focuses
more complex decision-   solely on CPU allocation.
making and memory
checks.
Process   Selects processes from the   Selects processes from
selection   job pool (secondary   the ready queue (main
location   memory).   memory).
Alternate   Job Scheduler   CPU Scheduler
Name
Purpose   Balances I/O-bound and   Maximizes CPU
CPU-bound processes.   utilization and minimizes
process waiting times.
ii. Time-sharing: Many interactive users → responsiveness is critical.
The short-term scheduler (CPU scheduler) decides which process
runs next very frequently (milliseconds). Long-term scheduler is
less relevant because new jobs are admitted immediately.
Batch system: Jobs are large and submitted in bulk. The long-term
scheduler regulates how many jobs enter memory, controlling
degree of multiprogramming. If too many are admitted, system
thrashes; if too few, CPU underutilizes.
(5 marks)
B A system has 3 frames for storing process pages in main memory. Assume
that all the page frames are initially empty. Consider the page reference
string given below:
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Compute the number of page faults and show frame contents step-by-step
for:
(a) FIFO,
(b) LRU,
(c) Optimal.
Also state which algorithm gave the fewest faults.
Marks Distribution:
(FIFO: 3 marks, LRU: 3 marks, Optimal: 3 marks)
Also state which algorithm gave the fewest faults and why.(1 marks)
********** 18 **********
--- page 19 ---
Reference string length = 12. Frames = 3.
(a) FIFO (First-In, First-Out)
Frames after
Step   Ref   Fault?
step (f1,f2,f3)
1   1   1, - , -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
4   4   4, 2, 3 (1 out) Y
5   1   4, 1, 3 (2 out) Y
6   2   4, 1, 2 (3 out) Y
7   5   5, 1, 2 (4 out) Y
8   1   5, 1, 2   N
9   2   5, 1, 2   N
10   3   5, 3, 2 (1 out) Y
11   4   5, 3, 4 (2 out) Y
12   5   5, 3, 4   N
Total page faults (FIFO): 9.
(b) LRU (Least Recently Used)
LRU replaces the page that has not been used for the longest time.
Step   Ref   Frames after step Fault? Comment
1   1   1, -, -   Y   load 1
2   2   1, 2, -   Y   load 2
3   3   1, 2, 3   Y   load 3
4, 2, 3 (1 was
4   4   Y
LRU)
4, 1, 3 (2 LRU
5   1   Y
replaced)
4, 1, 2 (3 LRU
6   2   Y
replaced)
********** 19 **********
--- page 20 ---
5, 1, 2 (4 LRU
7   5   Y
replaced)
8   1   5, 1, 2   N
9   2   5, 1, 2   N
3, 1, 2 (5 LRU
10   3   Y
replaced)
3, 4, 2 (1 LRU
11   4   Y
replaced)
3, 4, 5 (2 LRU
12   5   Y
replaced)
Total page faults (LRU): 10.
(c) Optimal (Belady’s optimal algorithm) — replace the page that will not
be used for the longest time in the future.
Frames after
Step   Ref   Fault?
step
1   1   1, -, -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
1, 2, 4 (3
replaced; will be
4   4   used later   Y
sooner than 1 or
2?)*
5   1   1, 2, 4   N
6   2   1, 2, 4   N
1, 2, 5 (4
replaced: 4 next
used at step 11;
7   5   Y
1 and 2 are
needed earlier at
steps 8 and 9)
8   1   1, 2, 5   N
9   2   1, 2, 5   N
3, 2, 5 (1
replaced; 1 next
10   3   Y
used later than 2
or 5)
********** 20 **********
--- page 21 ---
3, 4, 5 (2
11   4   Y
replaced)
12   5   3, 4, 5   N
Total page faults (Optimal): 7.
Optimal gives the fewest faults (7) because it uses future knowledge. For
real systems we cannot implement Optimal, but it is used as a baseline. In
this case FIFO (9) beats LRU (10) — showing that LRU is usually good
but not always strictly better than FIFO, and that algorithms’ effectiveness
depends on the reference string.
7 A Analyze the Resource Allocation Graph
i)   Write resource allocated and requested table
ii)   Find if there is a deadlock or not? If there is no deadlock then
what will be the sequence of the process to get executed?
iii)   What will happen if one instance of resource R3 is removed
from the system.
I.   4 marks
II.   4 Marks
III.   2 Marks
i)
********** 21 **********
--- page 22 ---
II) System is in Safe State. Safe Sequence: P2, P0, P1, P3
III) There will be a deadlock in the system.
B Explain user level and kernel level threads. Which one are more light 5
weight and independent?
User and Kernel Thread 3 marks
Explanation 2 marks
Solution: User-level threads are managed entirely by a user-level thread
library without direct involvement from the operating system's kernel.
The kernel is unaware of their existence and treats the entire process
containing these threads as a single unit of execution.
(1.5 marks)
Kernel-level threads are managed directly by the operating system's
kernel. The kernel is aware of each individual kernel thread and handles
their creation, scheduling, and management.   (1.5 marks)
User-level threads are managed by a user-level thread library, making
them more lightweight as they don't require kernel intervention and offer
faster context switching, but are less independent as a blocking thread can
block the entire process. Kernel-level threads are managed by the
operating system, are more independent because they can take advantage
of multiple CPUs and are not tied to a single process's blocking state but
are more heavyweight due to the overhead of kernel mode transitions and
are slower to create and switch.
(2 marks)
C   Differentiate between sequential access and direct access methods for files. 5
Provide examples of applications where each access method would be
preferred.
Difference 4 marks
Example 1 marks
Sequential Access In sequential access, data in a file is processed in
order, one record or byte after the next. The operations typically used are
read next and write next. Repositioning within the file usually requires a
Reset (rewind) operation to go back to the beginning.
********** 22 **********
--- page 23 ---
Direct Access Direct access views a file as a numbered sequence of fixed-
length logical records. This method allows for immediate, random access
to any part of the file. Operations include explicitly reading or writing
record number (read n, write n), and moving the file pointer directly to
record (position to n).
Application Preference:
Sequential Access Preference This method is preferred for applications
where files must be processed entirely from beginning to end. Examples
include simple text files, log files (where records are appended
chronologically), and source code files read by a compiler.
Direct Access Preference Direct access is preferred for applications that
require quick, random retrieval and update of specific records. A prime
example is an Indexed/Relative File system, commonly used in databases
or any system (like a customer database or airline reservation system)
where a record must be accessed by its index or relative block number.
********** 23 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 2d871971f099

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_AIML_7053/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 70.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MBA Tech (AI)/MBA Tech (Comp)
Year: II / III / V/Sem 3 Re-exam/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1 A What are the various components of an Operating System? Briefly explain 5
with the help of a diagram.
Explanation of components (any four) 1 mark each (4 Marks)
Diagram   1 mark
The main components of an operating system are:
1. Process Management
o Handles creation, scheduling, and termination of processes.
o Ensures fair CPU allocation among processes.
2. Memory Management
o Manages primary memory allocation and deallocation.
o Keeps track of memory usage and optimizes performance.
3. File Management
o Organizes, stores, retrieves, and manages data in files.
o Maintains directories and provides file access control.
4. Device Management
o Controls and coordinates input/output devices via device
drivers.
o Ensures efficient and conflict-free resource usage.
5. Security and Protection
o Protects data and system resources from unauthorized
access.
o Implements authentication, authorization, and encryption
mechanisms.
********** 1 **********
--- page 2 ---
B Analyze the code for Process Pi and Pj and state whether it satisfies the 5
three requirements for the solution to the critical section problem or not.
Justify your answer.
For process Pi:
do {
flag[i] = true;
turn = j;
while (flag[j] && turn == j);
// Critical Section
flag[i] = false;
// Remainder Section
} while (true);
For process Pj:
do {
flag[j] = true;
turn = i;
while (flag[i] && turn == i);
// Critical Section
flag[j] = false;
// Remainder Section
} while (true);
Final verdict: 2 marks
Justification each condition: 1 Mark (3 marks)
Yes, it satifies all the three conditions of mutual exclusion.
A. Mutual exclusion is preserved
Pi enters CS only if:
either flag[j] = false or turn = i
B. Progress requirement is satisfied: If a process wants to enter the
critical section, it waits only if the other process is inside or waiting
to enter, and it is the other process’s turn.
If the other process is not interested (flag[j] == false), then the first
process proceeds immediately without waiting.
Also, the turn variable guarantees that the processes alternate access
if both want to enter, so no process can block the other indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
user and other system programs

GUI touch screen | command line

user interfaces

system calls

program vO file a resource
communication

. A a accounting
execution operations systems allocation

protection
and
security

error
detection
services

operating system

hardware
--- page 3 ---
C. Bounded-waiting requirement is met: The turn variable acts as a fair
"token" passed between the two processes, ensuring that after one
process finishes, the other will eventually get the turn.
C Describe the process of deadlock recovery after detection. What are the
common methods used? Explain any two.
Deadlock Recovery 1 mark
Methods 4 marks
Process of Deadlock Recovery (1 Marks)
Once a deadlock is detected (usually using the resource allocation graph or
Banker’s algorithm), the OS performs the following steps:
1. Identify deadlocked processes and resources.
2. Select a recovery method — terminate processes, preempt
resources, or roll back processes.
3. Recover the system by releasing held resources and restarting
affected processes.
4. Resume normal operation.
Common Methods of Deadlock Recovery
The two main categories are:
1. Process Termination — killing one or more processes involved in
the deadlock.
2. Resource Preemption — temporarily taking resources away from
processes.
Other less common methods:
• Process Rollback (restore to a safe checkpoint).
• Manual Intervention (in simple or embedded systems).
(i) Process Termination (2 Marks)
• Concept:
Abort one or more processes involved in the deadlock until the cycle
is broken.
• Approaches:
1. Abort all deadlocked processes.
▪ Simple but costly; results in loss of work.
2. Abort processes one at a time until the deadlock cycle is
resolved.
•   Selection   Criteria:
When choosing which process to terminate, the OS considers:
1. Process priority and importance.
2. Amount of CPU time consumed.
3. Number and type of resources held.
4. Whether the process can be restarted easily.
• Advantages:
1. Straightforward and guaranteed recovery.
• Disadvantages:
1. May lead to loss of significant computation progress.
2. System performance temporarily degrades.
(ii) Resource Preemption (2 Marks)
• Concept:
Temporarily take away (preempt) resources from some processes
and give them to others to break the deadlock.
********** 3 **********
--- page 4 ---
• Steps Involved:
1. Select a victim process – the one whose resource preemption
has the least cost.
2. Save its state (checkpoint) – so it can be restarted later.
3. Reassign its resources to other waiting processes.
•   Challenges:
1. Rollback: The victim process must be rolled back to a safe
state.
2. Starvation: A process may be repeatedly chosen as a victim;
hence, the OS must keep track of how often each process is
preempted.
• Advantages:
1. Allows partial progress of other processes.
• Disadvantages:
1. Complex to implement and may lead to instability if done
repeatedly.
D Describe the concept of I/O management in an operating system and apply
your knowledge to identify key factors that can enhance I/O performance.
I/O Management 2 Marks
Factors 3 Marks (at least 3)
I/O management is a major component of operating system design that
handles the interaction between the computer system and I/O devices.
Key Components:
•   Ports, Buses, Controllers: Connect various devices to the system
• Device Drivers: Encapsulate device-specific details and present
uniform device-access interface to I/O subsystem
• I/O Hardware: Manages incredible variety of devices (storage,
transmission, human-interface)
I/O Methods:
•   Polling: CPU repeatedly checks device status (inefficient for slow
devices)
•   Interrupts: Device signals CPU when ready (efficient, used for
time-sensitive operations)
• DMA (Direct Memory Access): Transfers data directly between
device and memory without CPU involvement
I/O Operations:
• Blocking I/O: Process suspended until I/O completed
• Nonblocking I/O: Returns immediately with available data
• Asynchronous I/O: Process continues while I/O executes
Factors for Improving I/O Performance
1. Reduce Context Switches
• Minimize switching between processes during I/O operations
2. Reduce Data Copying
• Minimize copying data between kernel and user space
3. Reduce Interrupts
• Use large transfers instead of multiple small ones
• Employ smart controllers
• Use polling when appropriate
4. Use DMA (Direct Memory Access)
• Allow devices to transfer data directly to/from memory
********** 4 **********
--- page 5 ---
• Frees CPU from data transfer burden
5. Use Smarter Hardware Devices
•   Intelligent controllers with built-in processing capabilities
6. Balance System Resources
• Balance CPU, memory, bus, and I/O performance for highest
throughput
7. Move User-mode Processes to Kernel Threads
• Reduces overhead for frequently used I/O operations
8. Implement Efficient Buffering and Caching
• Buffer data to handle speed/size mismatches
• Cache frequently accessed data on faster devices
2 A Examine the synchronization problem in operating systems, identifying the
challenges it creates. Analyse how counting semaphores provide a
structured solution and resolve these issues in the Readers–Writers
problem.
Explain Synchronization Problem in Detail [4 marks]
Readers-Writers Problem [6 marks]
The Synchronization Problem arises in a multi-process or multi-threaded
environment when multiple processes concurrently access and manipulate
shared data. The core issue is that the final result of the execution depends
on the specific order in which instructions are interleaved, leading to
unpredictable and inconsistent results. This is known as a race condition.
Causes and Consequences:
1. Race Condition: Occurs when several processes access and modify
the same shared data concurrently, and the outcome of the execution
depends on the order of access.
2. Data Inconsistency: The primary consequence is that the shared data
may end up in a corrupted or inconsistent state.
Example (The Critical Section Problem): A simple counter shared by two
threads, one incrementing and the other decrementing. The operations
(Read → Modify → Write) are not atomic. If the operations are interrupted
and interleaved, the final count can be incorrect (e.g., instead of
100→101→100, it might become 100→101→101).
Requirements for a Correct Solution:
1. Mutual Exclusion: Only one process can be executing in its critical
section at any time.
2. Progress: If no process is executing in its critical section and some
processes wish to enter, then only those processes not in their
remainder sections can participate in deciding which will enter next,
and this selection cannot be postponed indefinitely.
3. Bounded Waiting: There must be a limit on the number of times
other processes are allowed to enter their critical sections after a
process has made a request to enter its critical section and before
that request is granted.
B. Counting Semaphore for Readers-Writers Problem [6 marks]
The Readers-Writers Problem is a classic synchronization problem where
multiple processes try to access a shared database.
● Readers only read the data and can do so concurrently.
● Writers modify the data and must have exclusive access (no other
reader or writer allowed).
********** 5 **********
--- page 6 ---
A Counting Semaphore (and a Binary/Mutex semaphore) can be used to
manage this access
Writer Process Logic: The writer needs exclusive access. It only needs to
wait on the general lock (wrt).
do {
wait(wrt);
// Writing is performed
signal(wrt);
} while (TRUE);
Reader Process Logic: Readers need to coordinate using readcount and
the wrt lock.
do {
wait(mutex);   // 1. Lock the readcount variable
readcount++;
if (readcount == 1) {   // 2. First reader locks out the writer
wait(wrt);
}
signal(mutex);   // 3. Unlock the readcount variable
// Reading is performed
wait(mutex);   // 4. Lock the readcount variable
readcount--;
if (readcount == 0) {   // 5. Last reader signals the writer
signal(wrt);
}
signal(mutex);   // 6. Unlock the readcount variable
} while (TRUE);
B Consider the following set of processes, each with varying arrival times
and burst times.
Process   Arrival Time   Burst Time
P1   0   7
P2   2   4
P3   4   1
P4   5   4
P5   6   3
i. Using the SRTF scheduling algorithm, determine the average
waiting time and average response time.
ii. Using the Round-Robin scheduling algorithm with time quantum =
3, determine the average waiting time and average response time.
********** 6 **********
--- page 7 ---
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
3 A Consider the following snapshot of a system running 5 processes:
Pro- Allocation   Max   Available
cess A   B   C   D A   B   C D A B   C D
P0   0   0   1   2 0   0   1   2 1   5   2   0
P1   1   0   0   0 1   7   5   0
P2   1   3   5   4 2   3   5   6
P3   0   6   3   2 0   6   5   2
********** 7 **********
--- page 8 ---
P4   0   0   1   4 0   6   5   6
Answer the following: -
i. How many resources of type A, B, C, D are there?
ii.   Calculate the need matrix?
iii.   Determine if the system is safe or not.
iv.   What will happen if the resource request (0, 4, 2,0) for process P1
arrive, can the system accept this request immediately?
Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks
Safe Sequence 3 Marks
Additional Request 3 Marks
The total number of resources of each type is calculated as:
Total = Allocation (sum) + Available
• A = 2 + 1 = 3
• B = 9 + 5 = 14
• C = 10 + 2 = 12
• D = 12 + 0 = 12
Thus, total system resources = (3, 14, 12, 12).
vi) Need Matrix
Process   A   B   C   D
P0   0   0   0   0
P1   0   7   5   0
P2   1   0   0   2
P3   0   0   2   0
P4   0   6   4   2
vii) Safe State Check
Starting with Available = (1, 5, 2, 0):
• P0 runs → Work = (1, 5, 3, 2)
• P3 runs → Work = (1, 11, 6, 4)
• P2 runs → Work = (2, 14, 11, 8)
• P4 runs → Work = (2, 14, 12, 12)
• P1 runs → Work = (3, 14, 12, 12)
Safe sequence = <P0, P3, P2, P4, P1>. Therefore, the system is SAFE.
viii) Resource Request (0, 4, 2, 0) by P1
********** 8 **********
--- page 9 ---
• Request (0, 4, 2, 0) ≤ Need(P1) = (0, 7, 5, 0) ✔
• Request (0, 4, 2, 0) ≤ Available (1, 5, 2, 0) ✔
After tentative allocation: Available = (1, 1, 0, 0).
Safety test sequence:
• P0 → Work = (1, 1, 1, 2)
• P2 → Work = (2, 4, 6, 6)
• P3 → Work = (2, 10, 9, 8)
• P4 → Work = (2, 10, 10, 12)
• P1 → completes.
Safe sequence = <P0, P2, P3, P4, P1>. Hence, the request CAN be
granted immediately.
B Describe the concept and working of a Translation Lookaside Buffer (TLB) 10
in a paging system. Explain how address translation is carried out with and
without TLB.
Definition and Need of TLB (2 Marks)
address translation without TLB (4 Marks)
address translation with TLB (4 Marks)
• A Translation Lookaside Buffer (TLB) is a special high-speed cache
that stores recent translations of virtual page numbers (VPNs) to
physical frame numbers (PFNs).
•   In a paging system, every memory access requires a page table lookup
to translate the virtual address into a physical address.
• This lookup takes extra time (additional memory access), which slows
down the system.
• The TLB reduces this delay by caching frequently used page table
entries — providing fast access to address translations.
Address translation is carried out with TLB.
********** 9 **********

[Text in pictures on this page, read by OCR]
frame e

logical address physical address 0x000
frame f
cpu slp | a |
p — Oxfff
f frame g

physical memory

page table
--- page 10 ---
Address translation is carried without TLB.
4 A Provide a comparative analysis of the Monolithic and Layered architectures 10
of Operating Systems. Include appropriate diagrams to support your
explanation.
Monolithic Architecture (3 Marks)
Layered Architecture (3 Marks)
Comparative Analysis (4 Marks)
Operating System architecture defines the structure and organization of the
OS components and their interaction with each other and hardware.
Two commonly used architectures are Monolithic and Layered
architectures.
Monolithic Architecture (3 Marks)
Explanation:
•   In a monolithic system, the entire operating system is working in a
single kernel space.
•   All system components such as   file management, process
scheduling, memory management, and device drivers are integrated
into one large block of code that runs in supervisor mode.
•   It provides high performance because there are no inter-layer
overheads, but poor modularity and difficult debugging.
Diagram:
********** 10 **********

[Text in pictures on this page, read by OCR]
logical

address
CPU +> pid

page frame

number number

E TLB hit physical

BI address
Lt | 4d }—

TLB

TLB miss

a physical
memory

page table
--- page 11 ---
Advantages:
• High execution speed (no layer overhead).
•   Efficient direct access to hardware.
Disadvantages:
•   Difficult to maintain and debug.
• Poor security and modularity—failure in one module may crash the
entire system.
Examples:
MS-DOS, UNIX (early versions), Linux (partially monolithic).
Layered Architecture (3 Marks)
Explanation:
•   In layered architecture, the OS is divided into multiple layers, each
built upon the lower one.
• Each layer performs specific functions and interacts only with its
adjacent layers.
• The bottom layer deals with hardware, while the top layer provides
user interfaces.
Diagram:
********** 11 **********

[Text in pictures on this page, read by OCR]
applications

glibc standard c library

system-call interface
file CPU
systems scheduler
networks memory
(TCP/IP) manager
block character
devices devices

device drivers

hardware
--- page 12 ---
Advantages:
•   Better modularity and maintainability.
•   Easier to test and debug individual layers.
• Higher security and reliability due to restricted communication.
Disadvantages:
• Slower execution due to layer-to-layer communication overhead.
•   Difficult to design and define proper boundaries between layers.
Examples:
THE Operating System, Windows NT, OS/2.
Comparative Analysis (4 Marks)
Feature   Monolithic OS   Layered OS
Structure   Single large kernel Multiple   layers   with   clear
interfaces
Performance   High   (no Slightly slower (due to layering)
overhead)
Modularity   Poor   Excellent
Maintainability Difficult   Easier to maintain and modify
Security   Low   (shared High   (restricted   inter-layer
kernel)   access)
Examples   MS-DOS, UNIX   Windows NT, THE OS
Conclusion:
Monolithic architecture emphasizes performance, whereas layered
architecture   emphasizes   modularity,   reliability,   and   security.
Modern operating systems often adopt a hybrid approach, combining the
speed of monolithic design with the structure of layered models.
B A disk queue with requests on cylinders 85, 170, 45, 130, 25, 115, 72, 58 10
needs to be serviced. The disk head is initially at cylinder 60, and the disk
has cylinders numbered 0-199. Calculate the total head movement for:
1. FCFS
2. SSTF
3. SCAN (assuming initial direction towards cylinder 199)
4. C-SCAN (assuming initial direction towards cylinder 199)
Compare the performance of each algorithm and determine which suits best
for this scenario.
********** 12 **********

[Text in pictures on this page, read by OCR]
application file device user
program system driver mode

messages: messages

CPU
scheduling

memory
managment

kernel
mode

interprocess
communication

microkernel

hardware
--- page 13 ---
Each Algorithm 2 Marks
Comparison 2 Marks

RK KKK RK KK 13 2h KKK RK Kk KK
--- page 14 ---
Best Algorithm for This Scenario:
SSTF provides the best performance with only 180 cylinders of movement,
making it ideal for this scenario where minimizing seek time is the priority
and the request queue is relatively small, reducing starvation risk.
5 A Describe the concept of monitors in process synchronization with internal 10
structure and functioning. Explain how monitors manage process
coordination using condition variables and synchronization primitives.
Concept of Monitors (2 Marks)
Internal Structure of a Monitor (4 Marks)
Functioning and Coordination (4 Marks)
In concurrent programming, monitors are high-level synchronization
constructs that provide a convenient and safe mechanism for process
coordination.
They encapsulate shared data, the procedures that operate on that data, and
the synchronization between concurrent processes — all within a single
module.
Monitors eliminate many of the errors possible when using low-level
primitives such as semaphores.
A monitor is a software module with:
• Shared data variables.
• A set of procedures (only one process can execute inside the
monitor at a time).
• Condition variables for process synchronization.
It ensures mutual exclusion automatically — no two processes can execute
monitor procedures simultaneously.
********** 14 **********

[Text in pictures on this page, read by OCR]
Performance Comparison

Algorithm Total Movement Characteristics

FCFS 572 Simple, fair, but high seek time

SSTF 188 Minimal movement, risk of starvation
SCAN 313 Fair, predictable, moderate performance

C-SCAN 396 More uniform wait time, higher movement
--- page 15 ---
Internal Structure of a Monitor (4 Marks)
Components:
1. Shared Data: Variables accessible only through monitor procedures.
2. Procedures: Define operations that can be performed on shared data.
3. Initialization Code: Sets up initial values for data and conditions.
4. Condition Variables: Used for process synchronization (e.g., x, y).
Pseudocode syntax of a monitor:
monitor monitor-name
{
// shared variable declarations
function P1 (…) { …. }
function P2 (…) { …. }
function Pn (…) {……}
initialization code (…) { … }
}
Diagram of Monitor Structure (1 Mark)
+-----------------------------------+
Functioning and Coordination (4 Marks)
Condition Variables and Synchronization:
• Condition variables allow a process to wait for a certain condition
to become true.
• Two basic operations are used:
o wait(c) → Process is suspended until another process signals
condition c.
o signal(c) → Wakes up one waiting process on condition c.
• Mutual exclusion: Achieved automatically; only one process
executes within the monitor.
•   Synchronization: Managed through wait and signal on condition
variables.
• No busy waiting: Blocked processes are placed in a waiting queue
inside the monitor.
Advantages of Monitors
********** 15 **********
--- page 16 ---
• Provides structured and safer synchronization compared to
semaphores.
•   Eliminates errors like deadlocks and race conditions caused by
improper semaphore use.
• Promotes modularity and clarity in concurrent program design.
B Explain how fragmentation affects memory management in operating 10
systems and illustrate the different types of fragmentation with suitable
example. A system has five memory partitions of sizes 110 KB, 480 KB,
210   KB,   350   KB,   and   140   KB   respectively.
A sequence of processes arrives for allocation in the following order: P1 =
100 KB, P2 = 200 KB, P3 = 300 KB, P4 = 140 KB, and P5 = 50 KB.
Considering Contiguous memory allocation, show the final process-to-
partition allocations using First-Fit, Best-Fit, and Worst-Fit memory
allocation strategies.
Marks Distribution:
Fragmentation 2 Marks
Types 2 marks
First Fit – 2 marks
Best Fit – 2 marks
Worst Fit – 2 marks
Fragmentation is a memory management problem that occurs when free memory
space is broken into small, non-contiguous blocks over time. It reduces the
system’s ability to allocate large continuous memory blocks to new processes,
even if total free memory is sufficient.
Fragmentation affects memory utilization and system performance, leading to
inefficient use of available RAM.
Types of Fragmentation
(a) Internal Fragmentation
Definition: Occurs when a fixed-sized memory block allocated to a process is
larger than the process’s actual memory requirement.
Cause: Fixed partitioning or paging schemes with block sizes larger than needed.
Effect: Wasted space inside the allocated partition.
Example:
Suppose a system allocates 4 KB blocks, and a process needs only 3.6 KB.
→ Unused memory = 0.4 KB per process
This 0.4 KB inside the allocated block is internally fragmented.
External Fragmentation
Definition: Occurs when total free memory exists but is scattered in non-
contiguous blocks, preventing allocation of large processes.
Cause: Dynamic memory allocation where processes are loaded and removed
frequently.
Effect: Wasted space outside allocated partitions.
Example:
Assume memory = 100 MB total. Free blocks: 20 MB + 15 MB + 10 MB (non-
contiguous).
********** 16 **********
--- page 17 ---
A process requesting 40 MB cannot be allocated, though 45 MB is free in total.
6 A   I.   Apply your understanding of process scheduling to compare Long- 10
term and Short-term schedulers in terms of their purpose, execution
frequency, speed, alternate names, and where process selection
occurs (main or secondary memory).
II.   Apply the concepts of process scheduling to justify why time-
sharing systems rely more on Short-term scheduler, while batch-
processing systems depend more on Long-term scheduler.
I.   5 Marks (One mark for each criteria)
II.   5 Marks
Solution:
i. Following are the differences between a LTS and STS:- (5 marks)
********** 17 **********
--- page 18 ---
Aspect   Long-Term Scheduler   Short-Term Scheduler
Frequency   Runs less frequently.   Runs very frequently.
Speed   Slower, as it involves   Faster, as it focuses
more complex decision-   solely on CPU allocation.
making and memory
checks.
Process   Selects processes from the   Selects processes from
selection   job pool (secondary   the ready queue (main
location   memory).   memory).
Alternate   Job Scheduler   CPU Scheduler
Name
Purpose   Balances I/O-bound and   Maximizes CPU
CPU-bound processes.   utilization and minimizes
process waiting times.
ii. Time-sharing: Many interactive users → responsiveness is critical.
The short-term scheduler (CPU scheduler) decides which process
runs next very frequently (milliseconds). Long-term scheduler is
less relevant because new jobs are admitted immediately.
Batch system: Jobs are large and submitted in bulk. The long-term
scheduler regulates how many jobs enter memory, controlling
degree of multiprogramming. If too many are admitted, system
thrashes; if too few, CPU underutilizes.
(5 marks)
B A system has 3 frames for storing process pages in main memory. Assume
that all the page frames are initially empty. Consider the page reference
string given below:
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Compute the number of page faults and show frame contents step-by-step
for:
(a) FIFO,
(b) LRU,
(c) Optimal.
Also state which algorithm gave the fewest faults.
Marks Distribution:
(FIFO: 3 marks, LRU: 3 marks, Optimal: 3 marks)
Also state which algorithm gave the fewest faults and why.(1 marks)
********** 18 **********
--- page 19 ---
Reference string length = 12. Frames = 3.
(a) FIFO (First-In, First-Out)
Frames after
Step   Ref   Fault?
step (f1,f2,f3)
1   1   1, - , -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
4   4   4, 2, 3 (1 out) Y
5   1   4, 1, 3 (2 out) Y
6   2   4, 1, 2 (3 out) Y
7   5   5, 1, 2 (4 out) Y
8   1   5, 1, 2   N
9   2   5, 1, 2   N
10   3   5, 3, 2 (1 out) Y
11   4   5, 3, 4 (2 out) Y
12   5   5, 3, 4   N
Total page faults (FIFO): 9.
(b) LRU (Least Recently Used)
LRU replaces the page that has not been used for the longest time.
Step   Ref   Frames after step Fault? Comment
1   1   1, -, -   Y   load 1
2   2   1, 2, -   Y   load 2
3   3   1, 2, 3   Y   load 3
4, 2, 3 (1 was
4   4   Y
LRU)
4, 1, 3 (2 LRU
5   1   Y
replaced)
4, 1, 2 (3 LRU
6   2   Y
replaced)
********** 19 **********
--- page 20 ---
5, 1, 2 (4 LRU
7   5   Y
replaced)
8   1   5, 1, 2   N
9   2   5, 1, 2   N
3, 1, 2 (5 LRU
10   3   Y
replaced)
3, 4, 2 (1 LRU
11   4   Y
replaced)
3, 4, 5 (2 LRU
12   5   Y
replaced)
Total page faults (LRU): 10.
(c) Optimal (Belady’s optimal algorithm) — replace the page that will not
be used for the longest time in the future.
Frames after
Step   Ref   Fault?
step
1   1   1, -, -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
1, 2, 4 (3
replaced; will be
4   4   used later   Y
sooner than 1 or
2?)*
5   1   1, 2, 4   N
6   2   1, 2, 4   N
1, 2, 5 (4
replaced: 4 next
used at step 11;
7   5   Y
1 and 2 are
needed earlier at
steps 8 and 9)
8   1   1, 2, 5   N
9   2   1, 2, 5   N
3, 2, 5 (1
replaced; 1 next
10   3   Y
used later than 2
or 5)
********** 20 **********
--- page 21 ---
3, 4, 5 (2
11   4   Y
replaced)
12   5   3, 4, 5   N
Total page faults (Optimal): 7.
Optimal gives the fewest faults (7) because it uses future knowledge. For
real systems we cannot implement Optimal, but it is used as a baseline. In
this case FIFO (9) beats LRU (10) — showing that LRU is usually good
but not always strictly better than FIFO, and that algorithms’ effectiveness
depends on the reference string.
7 A Analyze the Resource Allocation Graph
i)   Write resource allocated and requested table
ii)   Find if there is a deadlock or not? If there is no deadlock then
what will be the sequence of the process to get executed?
iii)   What will happen if one instance of resource R3 is removed
from the system.
I.   4 marks
II.   4 Marks
III.   2 Marks
i)
********** 21 **********
--- page 22 ---
II) System is in Safe State. Safe Sequence: P2, P0, P1, P3
III) There will be a deadlock in the system.
B Explain user level and kernel level threads. Which one are more light 5
weight and independent?
User and Kernel Thread 3 marks
Explanation 2 marks
Solution: User-level threads are managed entirely by a user-level thread
library without direct involvement from the operating system's kernel.
The kernel is unaware of their existence and treats the entire process
containing these threads as a single unit of execution.
(1.5 marks)
Kernel-level threads are managed directly by the operating system's
kernel. The kernel is aware of each individual kernel thread and handles
their creation, scheduling, and management.   (1.5 marks)
User-level threads are managed by a user-level thread library, making
them more lightweight as they don't require kernel intervention and offer
faster context switching, but are less independent as a blocking thread can
block the entire process. Kernel-level threads are managed by the
operating system, are more independent because they can take advantage
of multiple CPUs and are not tied to a single process's blocking state but
are more heavyweight due to the overhead of kernel mode transitions and
are slower to create and switch.
(2 marks)
C   Differentiate between sequential access and direct access methods for files. 5
Provide examples of applications where each access method would be
preferred.
Difference 4 marks
Example 1 marks
Sequential Access In sequential access, data in a file is processed in
order, one record or byte after the next. The operations typically used are
read next and write next. Repositioning within the file usually requires a
Reset (rewind) operation to go back to the beginning.
********** 22 **********
--- page 23 ---
Direct Access Direct access views a file as a numbered sequence of fixed-
length logical records. This method allows for immediate, random access
to any part of the file. Operations include explicitly reading or writing
record number (read n, write n), and moving the file pointer directly to
record (position to n).
Application Preference:
Sequential Access Preference This method is preferred for applications
where files must be processed entirely from beginning to end. Examples
include simple text files, log files (where records are appended
chronologically), and source code files read by a compiler.
Direct Access Preference Direct access is preferred for applications that
require quick, random retrieval and update of specific records. A prime
example is an Indexed/Relative File system, commonly used in databases
or any system (like a customer database or airline reservation system)
where a record must be accessed by its index or relative block number.
********** 23 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 0fea659c99e5

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_AI_7012/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 70.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MASTER OF BUSINESS ADMINISTRATION
IN TECHNOLOGY MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA
Tech (Comp)
Year: II / III / V/Sem 3 Re-exam/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1 A What are the various components of an Operating System? Briefly explain 5
with the help of a diagram.
Explanation of components (any four) 1 mark each (4 Marks)
Diagram   1 mark
The main components of an operating system are:
1. Process Management
o Handles creation, scheduling, and termination of processes.
o Ensures fair CPU allocation among processes.
2. Memory Management
o Manages primary memory allocation and deallocation.
o Keeps track of memory usage and optimizes performance.
3. File Management
o Organizes, stores, retrieves, and manages data in files.
o Maintains directories and provides file access control.
4. Device Management
o Controls and coordinates input/output devices via device
drivers.
o Ensures efficient and conflict-free resource usage.
5. Security and Protection
o Protects data and system resources from unauthorized
access.
o Implements authentication, authorization, and encryption
mechanisms.
********** 1 **********
--- page 2 ---
B Analyze the code for Process Pi and Pj and state whether it satisfies the 5
three requirements for the solution to the critical section problem or not.
Justify your answer.
For process Pi:
do {
flag[i] = true;
turn = j;
while (flag[j] && turn == j);
// Critical Section
flag[i] = false;
// Remainder Section
} while (true);
For process Pj:
do {
flag[j] = true;
turn = i;
while (flag[i] && turn == i);
// Critical Section
flag[j] = false;
// Remainder Section
} while (true);
Final verdict: 2 marks
Justification each condition: 1 Mark (3 marks)
Yes, it satifies all the three conditions of mutual exclusion.
A. Mutual exclusion is preserved
Pi enters CS only if:
either flag[j] = false or turn = i
B. Progress requirement is satisfied: If a process wants to enter the
critical section, it waits only if the other process is inside or waiting
to enter, and it is the other process’s turn.
If the other process is not interested (flag[j] == false), then the first
process proceeds immediately without waiting.
Also, the turn variable guarantees that the processes alternate access
if both want to enter, so no process can block the other indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
user and other system programs

GUI touch screen | command line

user interfaces

system calls

program vO file a resource
communication

. A a accounting
execution operations systems allocation

protection
and
security

error
detection
services

operating system

hardware
--- page 3 ---
C. Bounded-waiting requirement is met: The turn variable acts as a fair
"token" passed between the two processes, ensuring that after one
process finishes, the other will eventually get the turn.
C Describe the process of deadlock recovery after detection. What are the
common methods used? Explain any two.
Deadlock Recovery 1 mark
Methods 4 marks
Process of Deadlock Recovery (1 Marks)
Once a deadlock is detected (usually using the resource allocation graph or
Banker’s algorithm), the OS performs the following steps:
1. Identify deadlocked processes and resources.
2. Select a recovery method — terminate processes, preempt
resources, or roll back processes.
3. Recover the system by releasing held resources and restarting
affected processes.
4. Resume normal operation.
Common Methods of Deadlock Recovery
The two main categories are:
1. Process Termination — killing one or more processes involved in
the deadlock.
2. Resource Preemption — temporarily taking resources away from
processes.
Other less common methods:
• Process Rollback (restore to a safe checkpoint).
• Manual Intervention (in simple or embedded systems).
(i) Process Termination (2 Marks)
• Concept:
Abort one or more processes involved in the deadlock until the cycle
is broken.
• Approaches:
1. Abort all deadlocked processes.
▪ Simple but costly; results in loss of work.
2. Abort processes one at a time until the deadlock cycle is
resolved.
•   Selection   Criteria:
When choosing which process to terminate, the OS considers:
1. Process priority and importance.
2. Amount of CPU time consumed.
3. Number and type of resources held.
4. Whether the process can be restarted easily.
• Advantages:
1. Straightforward and guaranteed recovery.
• Disadvantages:
1. May lead to loss of significant computation progress.
2. System performance temporarily degrades.
(ii) Resource Preemption (2 Marks)
• Concept:
Temporarily take away (preempt) resources from some processes
and give them to others to break the deadlock.
********** 3 **********
--- page 4 ---
• Steps Involved:
1. Select a victim process – the one whose resource preemption
has the least cost.
2. Save its state (checkpoint) – so it can be restarted later.
3. Reassign its resources to other waiting processes.
•   Challenges:
1. Rollback: The victim process must be rolled back to a safe
state.
2. Starvation: A process may be repeatedly chosen as a victim;
hence, the OS must keep track of how often each process is
preempted.
• Advantages:
1. Allows partial progress of other processes.
• Disadvantages:
1. Complex to implement and may lead to instability if done
repeatedly.
D Describe the concept of I/O management in an operating system and apply
your knowledge to identify key factors that can enhance I/O performance.
I/O Management 2 Marks
Factors 3 Marks (at least 3)
I/O management is a major component of operating system design that
handles the interaction between the computer system and I/O devices.
Key Components:
•   Ports, Buses, Controllers: Connect various devices to the system
• Device Drivers: Encapsulate device-specific details and present
uniform device-access interface to I/O subsystem
• I/O Hardware: Manages incredible variety of devices (storage,
transmission, human-interface)
I/O Methods:
•   Polling: CPU repeatedly checks device status (inefficient for slow
devices)
•   Interrupts: Device signals CPU when ready (efficient, used for
time-sensitive operations)
• DMA (Direct Memory Access): Transfers data directly between
device and memory without CPU involvement
I/O Operations:
• Blocking I/O: Process suspended until I/O completed
• Nonblocking I/O: Returns immediately with available data
• Asynchronous I/O: Process continues while I/O executes
Factors for Improving I/O Performance
1. Reduce Context Switches
• Minimize switching between processes during I/O operations
2. Reduce Data Copying
• Minimize copying data between kernel and user space
3. Reduce Interrupts
• Use large transfers instead of multiple small ones
• Employ smart controllers
• Use polling when appropriate
4. Use DMA (Direct Memory Access)
• Allow devices to transfer data directly to/from memory
********** 4 **********
--- page 5 ---
• Frees CPU from data transfer burden
5. Use Smarter Hardware Devices
•   Intelligent controllers with built-in processing capabilities
6. Balance System Resources
• Balance CPU, memory, bus, and I/O performance for highest
throughput
7. Move User-mode Processes to Kernel Threads
• Reduces overhead for frequently used I/O operations
8. Implement Efficient Buffering and Caching
• Buffer data to handle speed/size mismatches
• Cache frequently accessed data on faster devices
2 A Examine the synchronization problem in operating systems, identifying the
challenges it creates. Analyse how counting semaphores provide a
structured solution and resolve these issues in the Readers–Writers
problem.
Explain Synchronization Problem in Detail [4 marks]
Readers-Writers Problem [6 marks]
The Synchronization Problem arises in a multi-process or multi-threaded
environment when multiple processes concurrently access and manipulate
shared data. The core issue is that the final result of the execution depends
on the specific order in which instructions are interleaved, leading to
unpredictable and inconsistent results. This is known as a race condition.
Causes and Consequences:
1. Race Condition: Occurs when several processes access and modify
the same shared data concurrently, and the outcome of the execution
depends on the order of access.
2. Data Inconsistency: The primary consequence is that the shared data
may end up in a corrupted or inconsistent state.
Example (The Critical Section Problem): A simple counter shared by two
threads, one incrementing and the other decrementing. The operations
(Read → Modify → Write) are not atomic. If the operations are interrupted
and interleaved, the final count can be incorrect (e.g., instead of
100→101→100, it might become 100→101→101).
Requirements for a Correct Solution:
1. Mutual Exclusion: Only one process can be executing in its critical
section at any time.
2. Progress: If no process is executing in its critical section and some
processes wish to enter, then only those processes not in their
remainder sections can participate in deciding which will enter next,
and this selection cannot be postponed indefinitely.
3. Bounded Waiting: There must be a limit on the number of times
other processes are allowed to enter their critical sections after a
process has made a request to enter its critical section and before
that request is granted.
B. Counting Semaphore for Readers-Writers Problem [6 marks]
The Readers-Writers Problem is a classic synchronization problem where
multiple processes try to access a shared database.
● Readers only read the data and can do so concurrently.
● Writers modify the data and must have exclusive access (no other
reader or writer allowed).
********** 5 **********
--- page 6 ---
A Counting Semaphore (and a Binary/Mutex semaphore) can be used to
manage this access
Writer Process Logic: The writer needs exclusive access. It only needs to
wait on the general lock (wrt).
do {
wait(wrt);
// Writing is performed
signal(wrt);
} while (TRUE);
Reader Process Logic: Readers need to coordinate using readcount and
the wrt lock.
do {
wait(mutex);   // 1. Lock the readcount variable
readcount++;
if (readcount == 1) {   // 2. First reader locks out the writer
wait(wrt);
}
signal(mutex);   // 3. Unlock the readcount variable
// Reading is performed
wait(mutex);   // 4. Lock the readcount variable
readcount--;
if (readcount == 0) {   // 5. Last reader signals the writer
signal(wrt);
}
signal(mutex);   // 6. Unlock the readcount variable
} while (TRUE);
B Consider the following set of processes, each with varying arrival times
and burst times.
Process   Arrival Time   Burst Time
P1   0   7
P2   2   4
P3   4   1
P4   5   4
P5   6   3
i. Using the SRTF scheduling algorithm, determine the average
waiting time and average response time.
ii. Using the Round-Robin scheduling algorithm with time quantum =
3, determine the average waiting time and average response time.
********** 6 **********
--- page 7 ---
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
3 A Consider the following snapshot of a system running 5 processes:
Pro- Allocation   Max   Available
cess A   B   C   D A   B   C D A B   C D
P0   0   0   1   2 0   0   1   2 1   5   2   0
P1   1   0   0   0 1   7   5   0
P2   1   3   5   4 2   3   5   6
P3   0   6   3   2 0   6   5   2
********** 7 **********
--- page 8 ---
P4   0   0   1   4 0   6   5   6
Answer the following: -
i. How many resources of type A, B, C, D are there?
ii.   Calculate the need matrix?
iii.   Determine if the system is safe or not.
iv.   What will happen if the resource request (0, 4, 2,0) for process P1
arrive, can the system accept this request immediately?
Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks
Safe Sequence 3 Marks
Additional Request 3 Marks
The total number of resources of each type is calculated as:
Total = Allocation (sum) + Available
• A = 2 + 1 = 3
• B = 9 + 5 = 14
• C = 10 + 2 = 12
• D = 12 + 0 = 12
Thus, total system resources = (3, 14, 12, 12).
vi) Need Matrix
Process   A   B   C   D
P0   0   0   0   0
P1   0   7   5   0
P2   1   0   0   2
P3   0   0   2   0
P4   0   6   4   2
vii) Safe State Check
Starting with Available = (1, 5, 2, 0):
• P0 runs → Work = (1, 5, 3, 2)
• P3 runs → Work = (1, 11, 6, 4)
• P2 runs → Work = (2, 14, 11, 8)
• P4 runs → Work = (2, 14, 12, 12)
• P1 runs → Work = (3, 14, 12, 12)
Safe sequence = <P0, P3, P2, P4, P1>. Therefore, the system is SAFE.
viii) Resource Request (0, 4, 2, 0) by P1
********** 8 **********
--- page 9 ---
• Request (0, 4, 2, 0) ≤ Need(P1) = (0, 7, 5, 0) ✔
• Request (0, 4, 2, 0) ≤ Available (1, 5, 2, 0) ✔
After tentative allocation: Available = (1, 1, 0, 0).
Safety test sequence:
• P0 → Work = (1, 1, 1, 2)
• P2 → Work = (2, 4, 6, 6)
• P3 → Work = (2, 10, 9, 8)
• P4 → Work = (2, 10, 10, 12)
• P1 → completes.
Safe sequence = <P0, P2, P3, P4, P1>. Hence, the request CAN be
granted immediately.
B Describe the concept and working of a Translation Lookaside Buffer (TLB) 10
in a paging system. Explain how address translation is carried out with and
without TLB.
Definition and Need of TLB (2 Marks)
address translation without TLB (4 Marks)
address translation with TLB (4 Marks)
• A Translation Lookaside Buffer (TLB) is a special high-speed cache
that stores recent translations of virtual page numbers (VPNs) to
physical frame numbers (PFNs).
•   In a paging system, every memory access requires a page table lookup
to translate the virtual address into a physical address.
• This lookup takes extra time (additional memory access), which slows
down the system.
• The TLB reduces this delay by caching frequently used page table
entries — providing fast access to address translations.
Address translation is carried out with TLB.
********** 9 **********

[Text in pictures on this page, read by OCR]
frame e

logical address physical address 0x000
frame f
cpu slp | a |
p — Oxfff
f frame g

physical memory

page table
--- page 10 ---
Address translation is carried without TLB.
4 A Provide a comparative analysis of the Monolithic and Layered architectures 10
of Operating Systems. Include appropriate diagrams to support your
explanation.
Monolithic Architecture (3 Marks)
Layered Architecture (3 Marks)
Comparative Analysis (4 Marks)
Operating System architecture defines the structure and organization of the
OS components and their interaction with each other and hardware.
Two commonly used architectures are Monolithic and Layered
architectures.
Monolithic Architecture (3 Marks)
Explanation:
•   In a monolithic system, the entire operating system is working in a
single kernel space.
•   All system components such as   file management, process
scheduling, memory management, and device drivers are integrated
into one large block of code that runs in supervisor mode.
•   It provides high performance because there are no inter-layer
overheads, but poor modularity and difficult debugging.
Diagram:
********** 10 **********

[Text in pictures on this page, read by OCR]
logical

address
CPU +> pid

page frame

number number

E TLB hit physical

BI address
Lt | 4d }—

TLB

TLB miss

a physical
memory

page table
--- page 11 ---
Advantages:
• High execution speed (no layer overhead).
•   Efficient direct access to hardware.
Disadvantages:
•   Difficult to maintain and debug.
• Poor security and modularity—failure in one module may crash the
entire system.
Examples:
MS-DOS, UNIX (early versions), Linux (partially monolithic).
Layered Architecture (3 Marks)
Explanation:
•   In layered architecture, the OS is divided into multiple layers, each
built upon the lower one.
• Each layer performs specific functions and interacts only with its
adjacent layers.
• The bottom layer deals with hardware, while the top layer provides
user interfaces.
Diagram:
********** 11 **********

[Text in pictures on this page, read by OCR]
applications

glibc standard c library

system-call interface
file CPU
systems scheduler
networks memory
(TCP/IP) manager
block character
devices devices

device drivers

hardware
--- page 12 ---
Advantages:
•   Better modularity and maintainability.
•   Easier to test and debug individual layers.
• Higher security and reliability due to restricted communication.
Disadvantages:
• Slower execution due to layer-to-layer communication overhead.
•   Difficult to design and define proper boundaries between layers.
Examples:
THE Operating System, Windows NT, OS/2.
Comparative Analysis (4 Marks)
Feature   Monolithic OS   Layered OS
Structure   Single large kernel Multiple   layers   with   clear
interfaces
Performance   High   (no Slightly slower (due to layering)
overhead)
Modularity   Poor   Excellent
Maintainability Difficult   Easier to maintain and modify
Security   Low   (shared High   (restricted   inter-layer
kernel)   access)
Examples   MS-DOS, UNIX   Windows NT, THE OS
Conclusion:
Monolithic architecture emphasizes performance, whereas layered
architecture   emphasizes   modularity,   reliability,   and   security.
Modern operating systems often adopt a hybrid approach, combining the
speed of monolithic design with the structure of layered models.
B A disk queue with requests on cylinders 85, 170, 45, 130, 25, 115, 72, 58 10
needs to be serviced. The disk head is initially at cylinder 60, and the disk
has cylinders numbered 0-199. Calculate the total head movement for:
1. FCFS
2. SSTF
3. SCAN (assuming initial direction towards cylinder 199)
4. C-SCAN (assuming initial direction towards cylinder 199)
Compare the performance of each algorithm and determine which suits best
for this scenario.
********** 12 **********

[Text in pictures on this page, read by OCR]
application file device user
program system driver mode

messages: messages

CPU
scheduling

memory
managment

kernel
mode

interprocess
communication

microkernel

hardware
--- page 13 ---
Each Algorithm 2 Marks
Comparison 2 Marks

RK KKK RK KK 13 2h KKK RK Kk KK
--- page 14 ---
Best Algorithm for This Scenario:
SSTF provides the best performance with only 180 cylinders of movement,
making it ideal for this scenario where minimizing seek time is the priority
and the request queue is relatively small, reducing starvation risk.
5 A Describe the concept of monitors in process synchronization with internal 10
structure and functioning. Explain how monitors manage process
coordination using condition variables and synchronization primitives.
Concept of Monitors (2 Marks)
Internal Structure of a Monitor (4 Marks)
Functioning and Coordination (4 Marks)
In concurrent programming, monitors are high-level synchronization
constructs that provide a convenient and safe mechanism for process
coordination.
They encapsulate shared data, the procedures that operate on that data, and
the synchronization between concurrent processes — all within a single
module.
Monitors eliminate many of the errors possible when using low-level
primitives such as semaphores.
A monitor is a software module with:
• Shared data variables.
• A set of procedures (only one process can execute inside the
monitor at a time).
• Condition variables for process synchronization.
It ensures mutual exclusion automatically — no two processes can execute
monitor procedures simultaneously.
********** 14 **********

[Text in pictures on this page, read by OCR]
Performance Comparison

Algorithm Total Movement Characteristics

FCFS 572 Simple, fair, but high seek time

SSTF 188 Minimal movement, risk of starvation
SCAN 313 Fair, predictable, moderate performance

C-SCAN 396 More uniform wait time, higher movement
--- page 15 ---
Internal Structure of a Monitor (4 Marks)
Components:
1. Shared Data: Variables accessible only through monitor procedures.
2. Procedures: Define operations that can be performed on shared data.
3. Initialization Code: Sets up initial values for data and conditions.
4. Condition Variables: Used for process synchronization (e.g., x, y).
Pseudocode syntax of a monitor:
monitor monitor-name
{
// shared variable declarations
function P1 (…) { …. }
function P2 (…) { …. }
function Pn (…) {……}
initialization code (…) { … }
}
Diagram of Monitor Structure (1 Mark)
+-----------------------------------+
Functioning and Coordination (4 Marks)
Condition Variables and Synchronization:
• Condition variables allow a process to wait for a certain condition
to become true.
• Two basic operations are used:
o wait(c) → Process is suspended until another process signals
condition c.
o signal(c) → Wakes up one waiting process on condition c.
• Mutual exclusion: Achieved automatically; only one process
executes within the monitor.
•   Synchronization: Managed through wait and signal on condition
variables.
• No busy waiting: Blocked processes are placed in a waiting queue
inside the monitor.
Advantages of Monitors
********** 15 **********
--- page 16 ---
• Provides structured and safer synchronization compared to
semaphores.
•   Eliminates errors like deadlocks and race conditions caused by
improper semaphore use.
• Promotes modularity and clarity in concurrent program design.
B Explain how fragmentation affects memory management in operating 10
systems and illustrate the different types of fragmentation with suitable
example. A system has five memory partitions of sizes 110 KB, 480 KB,
210   KB,   350   KB,   and   140   KB   respectively.
A sequence of processes arrives for allocation in the following order: P1 =
100 KB, P2 = 200 KB, P3 = 300 KB, P4 = 140 KB, and P5 = 50 KB.
Considering Contiguous memory allocation, show the final process-to-
partition allocations using First-Fit, Best-Fit, and Worst-Fit memory
allocation strategies.
Marks Distribution:
Fragmentation 2 Marks
Types 2 marks
First Fit – 2 marks
Best Fit – 2 marks
Worst Fit – 2 marks
Fragmentation is a memory management problem that occurs when free memory
space is broken into small, non-contiguous blocks over time. It reduces the
system’s ability to allocate large continuous memory blocks to new processes,
even if total free memory is sufficient.
Fragmentation affects memory utilization and system performance, leading to
inefficient use of available RAM.
Types of Fragmentation
(a) Internal Fragmentation
Definition: Occurs when a fixed-sized memory block allocated to a process is
larger than the process’s actual memory requirement.
Cause: Fixed partitioning or paging schemes with block sizes larger than needed.
Effect: Wasted space inside the allocated partition.
Example:
Suppose a system allocates 4 KB blocks, and a process needs only 3.6 KB.
→ Unused memory = 0.4 KB per process
This 0.4 KB inside the allocated block is internally fragmented.
External Fragmentation
Definition: Occurs when total free memory exists but is scattered in non-
contiguous blocks, preventing allocation of large processes.
Cause: Dynamic memory allocation where processes are loaded and removed
frequently.
Effect: Wasted space outside allocated partitions.
Example:
Assume memory = 100 MB total. Free blocks: 20 MB + 15 MB + 10 MB (non-
contiguous).
********** 16 **********
--- page 17 ---
A process requesting 40 MB cannot be allocated, though 45 MB is free in total.
6 A   I.   Apply your understanding of process scheduling to compare Long- 10
term and Short-term schedulers in terms of their purpose, execution
frequency, speed, alternate names, and where process selection
occurs (main or secondary memory).
II.   Apply the concepts of process scheduling to justify why time-
sharing systems rely more on Short-term scheduler, while batch-
processing systems depend more on Long-term scheduler.
I.   5 Marks (One mark for each criteria)
II.   5 Marks
Solution:
i. Following are the differences between a LTS and STS:- (5 marks)
********** 17 **********
--- page 18 ---
Aspect   Long-Term Scheduler   Short-Term Scheduler
Frequency   Runs less frequently.   Runs very frequently.
Speed   Slower, as it involves   Faster, as it focuses
more complex decision-   solely on CPU allocation.
making and memory
checks.
Process   Selects processes from the   Selects processes from
selection   job pool (secondary   the ready queue (main
location   memory).   memory).
Alternate   Job Scheduler   CPU Scheduler
Name
Purpose   Balances I/O-bound and   Maximizes CPU
CPU-bound processes.   utilization and minimizes
process waiting times.
ii. Time-sharing: Many interactive users → responsiveness is critical.
The short-term scheduler (CPU scheduler) decides which process
runs next very frequently (milliseconds). Long-term scheduler is
less relevant because new jobs are admitted immediately.
Batch system: Jobs are large and submitted in bulk. The long-term
scheduler regulates how many jobs enter memory, controlling
degree of multiprogramming. If too many are admitted, system
thrashes; if too few, CPU underutilizes.
(5 marks)
B A system has 3 frames for storing process pages in main memory. Assume
that all the page frames are initially empty. Consider the page reference
string given below:
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Compute the number of page faults and show frame contents step-by-step
for:
(a) FIFO,
(b) LRU,
(c) Optimal.
Also state which algorithm gave the fewest faults.
Marks Distribution:
(FIFO: 3 marks, LRU: 3 marks, Optimal: 3 marks)
Also state which algorithm gave the fewest faults and why.(1 marks)
********** 18 **********
--- page 19 ---
Reference string length = 12. Frames = 3.
(a) FIFO (First-In, First-Out)
Frames after
Step   Ref   Fault?
step (f1,f2,f3)
1   1   1, - , -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
4   4   4, 2, 3 (1 out) Y
5   1   4, 1, 3 (2 out) Y
6   2   4, 1, 2 (3 out) Y
7   5   5, 1, 2 (4 out) Y
8   1   5, 1, 2   N
9   2   5, 1, 2   N
10   3   5, 3, 2 (1 out) Y
11   4   5, 3, 4 (2 out) Y
12   5   5, 3, 4   N
Total page faults (FIFO): 9.
(b) LRU (Least Recently Used)
LRU replaces the page that has not been used for the longest time.
Step   Ref   Frames after step Fault? Comment
1   1   1, -, -   Y   load 1
2   2   1, 2, -   Y   load 2
3   3   1, 2, 3   Y   load 3
4, 2, 3 (1 was
4   4   Y
LRU)
4, 1, 3 (2 LRU
5   1   Y
replaced)
4, 1, 2 (3 LRU
6   2   Y
replaced)
********** 19 **********
--- page 20 ---
5, 1, 2 (4 LRU
7   5   Y
replaced)
8   1   5, 1, 2   N
9   2   5, 1, 2   N
3, 1, 2 (5 LRU
10   3   Y
replaced)
3, 4, 2 (1 LRU
11   4   Y
replaced)
3, 4, 5 (2 LRU
12   5   Y
replaced)
Total page faults (LRU): 10.
(c) Optimal (Belady’s optimal algorithm) — replace the page that will not
be used for the longest time in the future.
Frames after
Step   Ref   Fault?
step
1   1   1, -, -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
1, 2, 4 (3
replaced; will be
4   4   used later   Y
sooner than 1 or
2?)*
5   1   1, 2, 4   N
6   2   1, 2, 4   N
1, 2, 5 (4
replaced: 4 next
used at step 11;
7   5   Y
1 and 2 are
needed earlier at
steps 8 and 9)
8   1   1, 2, 5   N
9   2   1, 2, 5   N
3, 2, 5 (1
replaced; 1 next
10   3   Y
used later than 2
or 5)
********** 20 **********
--- page 21 ---
3, 4, 5 (2
11   4   Y
replaced)
12   5   3, 4, 5   N
Total page faults (Optimal): 7.
Optimal gives the fewest faults (7) because it uses future knowledge. For
real systems we cannot implement Optimal, but it is used as a baseline. In
this case FIFO (9) beats LRU (10) — showing that LRU is usually good
but not always strictly better than FIFO, and that algorithms’ effectiveness
depends on the reference string.
7 A Analyze the Resource Allocation Graph
i)   Write resource allocated and requested table
ii)   Find if there is a deadlock or not? If there is no deadlock then
what will be the sequence of the process to get executed?
iii)   What will happen if one instance of resource R3 is removed
from the system.
I.   4 marks
II.   4 Marks
III.   2 Marks
i)
********** 21 **********
--- page 22 ---
II) System is in Safe State. Safe Sequence: P2, P0, P1, P3
III) There will be a deadlock in the system.
B Explain user level and kernel level threads. Which one are more light 5
weight and independent?
User and Kernel Thread 3 marks
Explanation 2 marks
Solution: User-level threads are managed entirely by a user-level thread
library without direct involvement from the operating system's kernel.
The kernel is unaware of their existence and treats the entire process
containing these threads as a single unit of execution.
(1.5 marks)
Kernel-level threads are managed directly by the operating system's
kernel. The kernel is aware of each individual kernel thread and handles
their creation, scheduling, and management.   (1.5 marks)
User-level threads are managed by a user-level thread library, making
them more lightweight as they don't require kernel intervention and offer
faster context switching, but are less independent as a blocking thread can
block the entire process. Kernel-level threads are managed by the
operating system, are more independent because they can take advantage
of multiple CPUs and are not tied to a single process's blocking state but
are more heavyweight due to the overhead of kernel mode transitions and
are slower to create and switch.
(2 marks)
C   Differentiate between sequential access and direct access methods for files. 5
Provide examples of applications where each access method would be
preferred.
Difference 4 marks
Example 1 marks
Sequential Access In sequential access, data in a file is processed in
order, one record or byte after the next. The operations typically used are
read next and write next. Repositioning within the file usually requires a
Reset (rewind) operation to go back to the beginning.
********** 22 **********
--- page 23 ---
Direct Access Direct access views a file as a numbered sequence of fixed-
length logical records. This method allows for immediate, random access
to any part of the file. Operations include explicitly reading or writing
record number (read n, write n), and moving the file pointer directly to
record (position to n).
Application Preference:
Sequential Access Preference This method is preferred for applications
where files must be processed entirely from beginning to end. Examples
include simple text files, log files (where records are appended
chronologically), and source code files read by a compiler.
Direct Access Preference Direct access is preferred for applications that
require quick, random retrieval and update of specific records. A prime
example is an Indexed/Relative File system, commonly used in databases
or any system (like a customer database or airline reservation system)
where a record must be accessed by its index or relative block number.
********** 23 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper f73e79faafbb

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CSE_DS_7011/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 1;   a.   Compare Monolithic kernel and Microkernel architectures.   5
SO-1;
Ans: Any 5 correct points than 5 marks 1 marks each
BL-4
Feature   Monolithic Kernel   Microkernel
A kernel architecture
A kernel architecture
where the entire OS
where only essential
(device drivers, file
Definition   services run in kernel
system, memory
space; other services run
management, etc.) runs
in user space
in kernel space
Large, includes all OS   Small, minimal core
Size
services   services only
Device drivers, file   Only essential services
system, memory   like IPC (Inter-Process
Services in
management, process   Communication), basic
Kernel
management all run in   scheduling, minimal
kernel   memory management
Highly modular; services
Poor modularity; all
Modularity   can run independently in
code tightly coupled
user space
Less reliable; bug in   More reliable; bugs in
Reliability
one module can crash   user-space services do not
& Stability
the whole system   crash the kernel
********** 1 **********
--- page 2 ---
Slightly slower, due to
Performanc Faster, as everything
context switching and
e   runs in kernel mode
IPC overhead
Requires message passing
Communic Function calls within
between user-space
ation   kernel
services and kernel
Easier to maintain and
Ease of   Difficult to maintain
extend; services can be
Maintenanc due to tightly coupled
updated without touching
e   code
the kernel
Examples UNIX, Linux, MS-DOS MINIX, Mach, QNX, L4
CO- 2;   b.   Consider the methods used by processes P1 and P2 for accessing their 5
SO-2;
critical sections whenever needed, as given below. The initial values of
BL-5
shared Boolean variables S1 and S2 are randomly assigned.
P1   P2
while (S1 == S2);   while (S1! = S2);
Critical Section
Critical Section
S2 = !S1
S1 = S2
Which one of the following statements describes the properties achieved?
Justify
i.   Mutual exclusion but not progress
ii.   Progress but not mutual exclusion
iii.   Neither mutual exclusion nor progress
iv.   Both mutual exclusion and progress
Ans: Option I Mutual exclusion but not progress (5 marks)
CO- 3;   c.   Explain the different file access methods used in operating systems, with 5
SO- 1;
suitable examples for each.
BL- 2
Ans:
Sequential Access (1.5 marks)
Definition:
• Data in the file is accessed in a linear order, from the beginning
to the end.
• One must read all preceding data to reach a specific point.
Example:
• Reading a text file or log file line by line.
********** 2 **********
--- page 3 ---
Direct (Random) Access (1.5 marks)
Definition:
• Allows immediate access to any record in the file without reading
preceding data.
• Each record has a unique address or offset.
Example:
• Database files, where specific records are retrieved quickly.
• Disk-based applications like banking systems.
Indexed Access (1.5 marks)
Definition:
• Uses an index to locate data in the file.
• Index contains pointers to data blocks in the file.
• Useful for large files where direct access to records is needed
without scanning sequentially.
Example:
•   Library management systems using ISBN index.
•   File systems that use B-trees or hash-based indexing.
CO- 4;   d.   Compare LINUX and UNIX operating system software.   5
SO-1;
Any 5 correct than 5 marks
BL-4
Feature   UNIX   LINUX
Developed in 1969 at
Developed in 1991 by
AT&T Bell Labs by
Origin   Linus Torvalds as a free
Ken Thompson and
alternative to UNIX
Dennis Ritchie
Open source, freely
Source   Mostly proprietary
available for modification
Code   (closed source)
and distribution
Expensive, requires
Cost   Free or low-cost
licensing
Runs on a wide range:
Originally designed for
PCs, servers,
Platform   mainframes,
smartphones, embedded
minicomputers
systems
Traditionally command- Both CLI and GUI
User   line interface (CLI),   available; GUI (e.g.,
Interface   GUI available via add- GNOME, KDE) is built-in
ons   on most distributions
********** 3 **********
--- page 4 ---
Very stable and secure,
Highly secure; security
widely used in
Security   depends on distribution
enterprise and critical
and configuration
systems
Performs well on both
Performanc Excellent performance
high-end and low-end
e   on high-end systems
systems
Supports UFS, ZFS and Supports ext3, ext4, XFS,
File System
others   Btrfs, and more
Multitaskin
g &   Yes, robust support   Yes, robust support
Multiuser
Developed collaboratively
Developme Developed by AT&T
by open-source
nt Model   and commercial vendors
community
Updates managed by   Updates are frequent,
Updates
vendor, less frequent   managed by distributions
Example   Ubuntu, Red Hat, Fedora,
AIX, HP-UX, Solaris
Variants   Debian
Q2   a.   Assume the following processes arrive for execution at the time   [10]
CO-2;   indicated and the length of CPU burst time given in msec.
SO-2;
BL-6
a. Draw Gantt chart for FCFS and Round Robin scheduling
(TQ=3msec).
b. Calculate average waiting time and average turnaround time.
Q2   b.   Explain the concept of paging in memory management. Describe the   [10]
CO-3;   roles of the page table, page frame, and page fault, and discuss how the
SO-2;
Translation Lookaside Buffer (TLB) improves performance, with the
BL-2
help of a neat labelled diagram.
Ans:
Concept of Paging in Memory Management (1 marks)
Paging is a memory management scheme that eliminates external
fragmentation and allows non-contiguous allocation of physical
memory.
Key idea:
• The logical memory of a process is divided into fixed-size
blocks called pages.
********** 4 **********

[Text in pictures on this page, read by OCR]
Process Id Arrival time Burst time

Pl 5 5
P2 4 6
P3 3 7
P4 1 9
PS 2 2

P6 6 3
--- page 5 ---
• The physical memory is divided into fixed-size blocks called
frames.
• Pages are mapped to frames in physical memory, which may be
non-contiguous.
Advantages of Paging:
1. Eliminates external fragmentation.
2. Allows efficient memory utilization.
3. Supports virtual memory and demand paging.
Logical Address Structure in Paging:
• A logical address is divided into:
o Page Number (p): Identifies the page in logical memory
o Page Offset (d): Offset within the page
Logical Address = (𝑝, 𝑑)
3. Page Frame (1 marks)
Definition:
• A page frame is a fixed-size block of physical memory.
Role of Page Frame:
1. Stores a page from logical memory.
2. Physical memory is divided into frames of the same size as
pages.
3. Allows non-contiguous allocation of memory.
4. Page Fault (1 marks)
Definition:
• A page fault occurs when a process tries to access a page that is
not currently in physical memory.
Role / Handling of Page Fault:
1. OS suspends the process and finds a free frame in memory.
2. The required page is loaded from secondary storage (like disk)
into the free frame.
3. Page table is updated to reflect the new frame number.
4. Process resumes execution from where it was interrupted.
2. Page Table (1 marks)
Definition:
********** 5 **********
--- page 6 ---
• A page table is a data structure used by the OS to map logical
pages to physical frames.
Role of Page Table:
1. Stores the frame number for each page.
2. Used by the Memory Management Unit (MMU) to translate
logical addresses to physical addresses.
3. Helps implement virtual memory by keeping track of pages in
memory and pages on disk.
Translation Lookaside Buffer (TLB) (6 marks- 3marks diagram, 3
marks explain)
Q3   a.   Compare LOOK and SCAN disk scheduling algorithm. Consider the   [10]
CO-3;   following disk queue with requests for I/O to block on cylinders:
SO-6;
45, 81, 185, 33, 175, 99, 150, 77
BL-5
Consider that the head starts from location 58. Assume a disk with 200
tracks (0 to 199.Find the total head movement of the cylinder for the
following
i.   C-SCAN (head starts moving in the right direction)
ii.   FCFS disk scheduling algorithm
iii.   SSTF disk scheduling algorithm
Ans:
Compare LOOK and SCAN disk scheduling algorithm (4 marks)
Feature SCAN (Elevator Algorithm)   LOOK Algorithm
The disk arm moves from one The disk arm moves only
Definition end of the disk to the other,   as far as the last request in
servicing requests along the   each direction before
********** 6 **********

[Text in pictures on this page, read by OCR]
logical
address

CPU Dp

page frame

number number

TLB hit

physical
address

f [dq - 4

TLB

, {
TLB miss

—— physical
memory

page table
--- page 7 ---
way. When it reaches the end, reversing — it does not go
it reverses direction and   to the physical end of the
continues.   disk.
Goes all the way to the last
Goes only as far as needed
Movemen cylinder (0 or max) even if
(to the last request in the
t   there are no pending requests
current direction).
there.
Slightly less efficient (extra More efficient because it
Efficiency
movement to end of disk).   avoids unnecessary travel.
Direction Reverses only at disk ends (0 Reverses at last request in
Reversal   or max track).   the direction.
Performan Slightly higher average seek Lower average seek time
ce   time due to end travel.   due to optimized path.
Fair — all requests are
Fairness   Fair and more efficient.
eventually serviced.
Example Legacy systems where head Modern systems —
Use   moves across fixed range.   improved SCAN variant.
i.   C-SCAN (head starts moving in the right direction) (2 marks)
Order of service:
58 → 77 → 81 → 99 → 150 → 175 → 185 → (jump to 0) →
33 → 45
Total head movement = 19 + 4 + 18 + 51 + 25 + 10 + 14 +
199 + 33 + 12 = 385 tracks
ii.   FCFS disk scheduling algorithm (2 marks)
Process requests in the order they arrive:
58 → 45 → 81 → 185 → 33 → 175 → 99 → 150 → 77
Total head movement = 13 + 36 + 104 + 152 + 142 + 76 + 51
+ 73 = 647 tracks
iii.   SSTF disk scheduling algorithm (2 marks)
58 → 45 → 33 → 77 → 81 → 99 → 150 → 175 → 185
Total head movement = 13 + 12 + 44 + 4 + 18 + 51 + 25 +
10 = 177 tracks
Q3   b.   What is a system call? Explain its working with a neat diagram and   [10]
CO-1;   describe the different types of system calls used in operating systems.
SO-1;
Ans: System Call (3 marks)
BL-2
•   Interface between OS and User programs (processes)
• Used to request service from the kernel through API
********** 7 **********
--- page 8 ---
• At the very least, we need to separate modes of operation:
user mode and kernel mode. At system boot time, the
hardware starts in kernel mode. The operating system is
then loaded and starts user applications in user mode.
• Whenever a trap or interrupt occurs, the hardware
switches from user mode to kernel mode. Thus, whenever
the operating system gains control of the computer, it is
in kernel mode.
•   Control is switched back to the operating system via an
interrupt, a trap, or a system call. System calls provide
the means for a user program to ask the operating system
to perform tasks reserved for the operating system on the
user program’s behalf. When a system call is executed, it
is treated by the hardware as a software interrupt. Control
passes through the interrupt vector to a service routine in
the operating system, and the mode bit is set to kernel
mode.
Working (5 marks)
Types of System Calls (2 marks)
1. Process Control
2. File Management
3. Device Management
4. Information Management
5. Communication
Q4   a   Define semaphore and explain the need for a mutex. Design pseudocode [10]
CO-2;   to illustrate the Producer-Consumer problem using semaphores.
SO-2;
********** 8 **********

[Text in pictures on this page, read by OCR]
user application

open ()
user
mode
—_ system call interface
kernel
mode
Li»): open ()
a Implementation
i —>—» ofopen()

e system call
: :
--- page 9 ---
BL-6   Ans
What is a Semaphore? (2 marks)
A semaphore is a synchronization primitive used in operating systems
to control access to shared resources by multiple processes and to avoid
race conditions.
Types of Semaphores:
1. Binary Semaphore:
o Takes only values 0 or 1.
o Used for mutual exclusion (mutex).
2. Counting Semaphore:
o Can take non-negative integer values.
o Used to count available resources.
Basic Operations:
•   wait() / P() / down(): Decrement the semaphore. If the value
becomes negative, the process is blocked.
•   signal() / V() / up(): Increment the semaphore. If a process is
waiting, it is woken up.
2. Need for a Mutex (2 marks)
Mutex (Mutual Exclusion Object):
• Ensures that only one process/thread enters the critical section at
a time.
• Prevents race conditions, which occur when multiple processes
access shared data simultaneously.
Example:
If two threads try to update a shared counter without mutex, the final
value may be incorrect due to concurrent updates.
3. Producer-Consumer Problem Using Semaphores (3 marks)
Problem Statement:
• Producer: Produces data and puts it into a buffer.
• Consumer: Consumes data from the buffer.
•   Constraint:
o Buffer has a finite size.
o Producer must wait if buffer is full.
o Consumer must wait if buffer is empty.
Semaphores Used:
********** 9 **********
--- page 10 ---
Semaphore Purpose
empty   Counts number of empty slots in buffer
full   Counts number of full slots in buffer
Ensures mutual exclusion while accessing
mutex
buffer
Initialization:
mutex = 1   // binary semaphore
empty = n   // size of buffer
full = 0
Pseudocode (3marks)
Producer Process:
while (true) {
produce_item(item);   // create an item
wait(empty);   // check for empty slot
wait(mutex);   // enter critical section
insert_item(item);   // add item to buffer
signal(mutex);   // leave critical section
signal(full);   // increment count of full slots
}
Consumer Process:
while (true) {
wait(full);   // check if buffer has item
wait(mutex);   // enter critical section
remove_item(item);   // remove item from buffer
signal(mutex);   // leave critical section
signal(empty);   // increment count of empty slots
consume_item(item);   // consume the item
}
********** 10 **********
--- page 11 ---
Q4   b   Explain the concept of segmentation in memory management with the   [10]
CO-3;   help of a neat diagram and suitable example.
SO-6;
Ans: Segmentation (3 marks)
BL-2
• A program can be subdivided into segments
– Segments may vary in length
– There is a maximum segment length
• Addressing consist of two parts
– a segment number and
– an offset
• Segmentation is similar to dynamic partitioning
Diagram (3 marks) and explain (4 marks)
Q5   a.   Write the Bankers algorithm. Consider the following snapshot of the   [10]
CO-2;   system in which there are five process and four resources A, B, C and D
SO-2;
Max   Allocation   Available
BL-6
A B   C D A B   C D   A   B   C D
P0 6   0   1   2   4   0   0   1   3   2   1   1
P1 1   7   5   0   1   1   0   0
P2 2   3   5   6   1   2   5   4
P3 1   6   5   3   0   6   3   3
P4 1   6   5   6   0   2   1   2
Answer the following question using Banker’s Algorithm
i.   Calculate Need Matrix?
ii.   Is, the system in safe state? If Yes, give safe sequence.
Ans:
Bankers Algorithm (4 marks)
********** 11 **********
--- page 12 ---
•   Available: Vector of length m. If available [j] = k, there are k
instances of resource type Rj available
• Max: n x m matrix. If Max [i,j] = k, then process Pi may request
at most k instances of resource type Rj
•   Allocation: n x m matrix. If Allocation[i,j] = k then Pi is
currently allocated k instances of Rj
• Need: n x m matrix. If Need[i,j] = k, then Pi may need k more
instances of Rj to complete its task
Need [i,j] = Max[i,j] – Allocation [i,j]
Let Work and Finish be vectors of length m and n, respectively.
Initialize:
Work = Available
Finish [i] = false for i = 0, 1, …, n- 1
2.   Find an i such that both:
(a) Finish [i] = false
(b) Needi  Work
If no such i exists, go to step 4
3. Work = Work + Allocationi
Finish[i] = true
go to step 2
4.   If Finish [i] == true for all i, then the system is in a safe state
Requesti = request vector for process Pi. If Requesti [j] = k then process
Pi wants k instances of resource type Rj
1.   If Requesti  Needi go to step 2. Otherwise, raise error
condition, since process has exceeded its maximum claim
2.   If Requesti  Available, go to step 3. Otherwise Pi must wait,
since resources are not available
3.   Pretend to allocate requested resources to Pi by modifying the
state as follows:
Available = Available – Requesti;
Allocationi = Allocationi + Requesti;
Needi = Needi – Requesti;
l   If safe  the resources are allocated to Pi
l   If unsafe  Pi must wait, and the old resource-
allocation state is restored
********** 12 **********
--- page 13 ---
Need Matrix(2 marks)
Proces A B C
s   D
P0   2 0 1 1
P1   0 6 5 0
P2   1 1 0 2
P3   1 0 2 0
P4   1 4 4 4
Result (4 marks)
• System is in a safe state
• Safe Sequence:
P0 → P2 → P1 → P3 → P4
Q5   b.   Explain Monolithic and Layered Structure of OS in detail with neat [10]
CO-1;   diagram.
SO-1;   Ans:
BL-2
Monolithic structure (5 marks)
• Big Mess
• No structure
•   Collection of procedures
• No information hiding
• Working :
• User mode program calls a system service
•   Processor traps the call and switches the calling thread to
kernel mode
• On completion of system service, the thread switches back
to user mode.
********** 13 **********
--- page 14 ---
• One service procedure for each system call
•   Utility procedures do things that are needed by several service
procedures like fetching user data.
Layered Structure (5 marks)
• OS organized as hierarchy of layers
•   First layered OS – ‘THE’ system
There are 6 layers in Layered OS
Q6   a.   Calculate total number of page fault, page hit for the following string   [10]
CO-3;   using LRU, FIFO and optimal page replacement policy. Consider the
SO-6;
page frame size is 3. Give advantages and disadvantages of each
BL-5
algorithm
2,0,3,0,4,2,3,0,3,2,7,2,0,7,5,0,7,5,7,0
Ans:FIFO(2marks)
FIFO Page Faults = 12
FIFO Hits = 8
LRU (2marks)
LRU Page Faults = 9
LRU Hits = 11
Optimal (2 marks)
Optimal Page Faults = 9
Optimal Hits = 11
Advantages and Disadvantages (4 marks)
********** 14 **********

[Text in pictures on this page, read by OCR]
Layers
User Programs.

Layer 5
uyers VO Butter
Process Management
Layers
- Memory Management
CPU Scheduling
Layer 1
Hardware

LAYERED OPERATING SYSTEM
--- page 15 ---
Algori
Advantages   Disadvantages
thm
Can cause Belady’s anomaly
Simple and easy to
FIFO   (more frames will have more
implement
faults)
Better performance than
Needs hardware support or
LRU FIFO; considers recent
counters; more complex
usage
Requires future knowledge
Optim Lowest possible page
of reference string; not
al   faults
practical
Q6   b.   What is a Thread? Explain the benefits of using threads. Describe   [10]
CO-2;   different multithreading models with neat diagrams, and discuss their
SO-2;
advantages and disadvantages.
BL-2
Ans:
Thread (2 marks)
 Threads run within application
 Before threads different processes were created to perform
different tasks.
 Now, multiple threads are created within a same process to
handle different tasks.
 This is called as multithreading.
Benefit (2 marks)
 Responsiveness – Multithreading an interactive application may
allow a program to continue running even if part of it is blocked
or is performing a lengthy operation, thereby increasing
responsiveness to the user. This quality is especially useful in
designing user interfaces.
 Resource Sharing – threads share resources of process to which
they belong by default. It is easier than shared memory or
message passing. The benefit of sharing code and data is that it
allows an application to have several different threads of activity
within the same address space.
 Economy – Allocating memory and resources for process
creation is costly. Because threads share the resources of the
process to which they belong, it is more economical to create
and context-switch threads.
********** 15 **********
--- page 16 ---
 Scalability – The benefits of multithreading can be even greater
in a multiprocessor architecture, where threads may be running
in parallel on different processing cores.
Multithreading Models(6 marks)
 Three common ways of establishing such a relationship
 Many-to-Many
 Many-to-One
 One-to-One
Q7   a.   Explain the Indexed allocation method of file storage with a neat   [10]
CO-3;   diagram. Discuss its advantages and disadvantages.
SO-2;
Ans:
BL-2
(2 marks)
Definition:
Indexed allocation is a file allocation method in which each file has its
own index block. The index block contains pointers to all the blocks of
the file. This method overcomes the limitations of contiguous and
linked allocation.
Diagram ( 2marks)
Explain (2 marks)
Advantages of Indexed Allocation(2 marks)
Direct access:
No external fragmentation:
Flexible file size:
Disadvantages of Indexed Allocation(2 marks)
********** 16 **********
--- page 17 ---
Index block overhead:
Maximum file size limitation:
Extra memory access:
Must read the index block first before accessing data blocks.
Q7   b.   Explain the issues in the two-process solution using the flag variable.   [10]
CO-2;   Discuss how these issues can be resolved and design pseudocode to
SO-2;
implement the solution for process synchronization
BL-6
Ans: (2 marks)
Suppose we have two processes, P0 and P1. Each process has a critical
section that must not be executed simultaneously. The flag variable
solution tries to control access:
flag[0] = true; // P0 wants to enter critical section
flag[1] = true; // P1 wants to enter critical section
Each process sets its own flag[i] before entering the critical section and
checks the other process's flag:
while(flag[j]) {
// wait
}
2. Issues in the Flag Variable Approach (2 marks)
The main problem occurs when both processes try to enter the critical
section simultaneously:
Suppose both P0 and P1 set flag[0] = true and flag[1] = true at the same
time.
Both will see that the other’s flag is true.
Both processes keep waiting forever.
This situation is called deadlock.
To solve this, we use Peterson’s Algorithm, which introduces (2 marks)
1. A flag array indicating intent to enter the critical section.
2. A turn variable to decide whose turn it is if both want to enter.
Pseudocode for Peterson’s Algorithm (4 marks)
Shared variables:
flag[2] = {false, false} // intention to enter critical section
turn = 0   // whose turn is it
********** 17 **********
--- page 18 ---
Process P0:
while (true) {
// Entry section
flag[0] = true
turn = 1
while (flag[1] == true && turn == 1) {
// busy wait
}
// Critical section
// ... perform critical operation ...
// Exit section
flag[0] = false
// Remainder section
// ... non-critical operations ...
}
Process P1:
while (true) {
// Entry section
flag[1] = true
turn = 0
while (flag[0] == true && turn == 0) {
// busy wait
}
// Critical section
// ... perform critical operation ...
// Exit section
flag[1] = false
// Remainder section
// ... non-critical operations ...
}
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 18c37dde1732

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MBATech_AI_7051/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 70.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MASTER OF BUSINESS ADMINISTRATION
IN TECHNOLOGY MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA
Tech (Comp)
Year: II / III / V/Sem 3 Re-exam/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1 A What are the various components of an Operating System? Briefly explain 5
with the help of a diagram.
Explanation of components (any four) 1 mark each (4 Marks)
Diagram   1 mark
The main components of an operating system are:
1. Process Management
o Handles creation, scheduling, and termination of processes.
o Ensures fair CPU allocation among processes.
2. Memory Management
o Manages primary memory allocation and deallocation.
o Keeps track of memory usage and optimizes performance.
3. File Management
o Organizes, stores, retrieves, and manages data in files.
o Maintains directories and provides file access control.
4. Device Management
o Controls and coordinates input/output devices via device
drivers.
o Ensures efficient and conflict-free resource usage.
5. Security and Protection
o Protects data and system resources from unauthorized
access.
o Implements authentication, authorization, and encryption
mechanisms.
********** 1 **********
--- page 2 ---
B Analyze the code for Process Pi and Pj and state whether it satisfies the 5
three requirements for the solution to the critical section problem or not.
Justify your answer.
For process Pi:
do {
flag[i] = true;
turn = j;
while (flag[j] && turn == j);
// Critical Section
flag[i] = false;
// Remainder Section
} while (true);
For process Pj:
do {
flag[j] = true;
turn = i;
while (flag[i] && turn == i);
// Critical Section
flag[j] = false;
// Remainder Section
} while (true);
Final verdict: 2 marks
Justification each condition: 1 Mark (3 marks)
Yes, it satifies all the three conditions of mutual exclusion.
A. Mutual exclusion is preserved
Pi enters CS only if:
either flag[j] = false or turn = i
B. Progress requirement is satisfied: If a process wants to enter the
critical section, it waits only if the other process is inside or waiting
to enter, and it is the other process’s turn.
If the other process is not interested (flag[j] == false), then the first
process proceeds immediately without waiting.
Also, the turn variable guarantees that the processes alternate access
if both want to enter, so no process can block the other indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
user and other system programs

GUI touch screen | command line

user interfaces

system calls

program vO file a resource
communication

. A a accounting
execution operations systems allocation

protection
and
security

error
detection
services

operating system

hardware
--- page 3 ---
C. Bounded-waiting requirement is met: The turn variable acts as a fair
"token" passed between the two processes, ensuring that after one
process finishes, the other will eventually get the turn.
C Describe the process of deadlock recovery after detection. What are the
common methods used? Explain any two.
Deadlock Recovery 1 mark
Methods 4 marks
Process of Deadlock Recovery (1 Marks)
Once a deadlock is detected (usually using the resource allocation graph or
Banker’s algorithm), the OS performs the following steps:
1. Identify deadlocked processes and resources.
2. Select a recovery method — terminate processes, preempt
resources, or roll back processes.
3. Recover the system by releasing held resources and restarting
affected processes.
4. Resume normal operation.
Common Methods of Deadlock Recovery
The two main categories are:
1. Process Termination — killing one or more processes involved in
the deadlock.
2. Resource Preemption — temporarily taking resources away from
processes.
Other less common methods:
• Process Rollback (restore to a safe checkpoint).
• Manual Intervention (in simple or embedded systems).
(i) Process Termination (2 Marks)
• Concept:
Abort one or more processes involved in the deadlock until the cycle
is broken.
• Approaches:
1. Abort all deadlocked processes.
▪ Simple but costly; results in loss of work.
2. Abort processes one at a time until the deadlock cycle is
resolved.
•   Selection   Criteria:
When choosing which process to terminate, the OS considers:
1. Process priority and importance.
2. Amount of CPU time consumed.
3. Number and type of resources held.
4. Whether the process can be restarted easily.
• Advantages:
1. Straightforward and guaranteed recovery.
• Disadvantages:
1. May lead to loss of significant computation progress.
2. System performance temporarily degrades.
(ii) Resource Preemption (2 Marks)
• Concept:
Temporarily take away (preempt) resources from some processes
and give them to others to break the deadlock.
********** 3 **********
--- page 4 ---
• Steps Involved:
1. Select a victim process – the one whose resource preemption
has the least cost.
2. Save its state (checkpoint) – so it can be restarted later.
3. Reassign its resources to other waiting processes.
•   Challenges:
1. Rollback: The victim process must be rolled back to a safe
state.
2. Starvation: A process may be repeatedly chosen as a victim;
hence, the OS must keep track of how often each process is
preempted.
• Advantages:
1. Allows partial progress of other processes.
• Disadvantages:
1. Complex to implement and may lead to instability if done
repeatedly.
D Describe the concept of I/O management in an operating system and apply
your knowledge to identify key factors that can enhance I/O performance.
I/O Management 2 Marks
Factors 3 Marks (at least 3)
I/O management is a major component of operating system design that
handles the interaction between the computer system and I/O devices.
Key Components:
•   Ports, Buses, Controllers: Connect various devices to the system
• Device Drivers: Encapsulate device-specific details and present
uniform device-access interface to I/O subsystem
• I/O Hardware: Manages incredible variety of devices (storage,
transmission, human-interface)
I/O Methods:
•   Polling: CPU repeatedly checks device status (inefficient for slow
devices)
•   Interrupts: Device signals CPU when ready (efficient, used for
time-sensitive operations)
• DMA (Direct Memory Access): Transfers data directly between
device and memory without CPU involvement
I/O Operations:
• Blocking I/O: Process suspended until I/O completed
• Nonblocking I/O: Returns immediately with available data
• Asynchronous I/O: Process continues while I/O executes
Factors for Improving I/O Performance
1. Reduce Context Switches
• Minimize switching between processes during I/O operations
2. Reduce Data Copying
• Minimize copying data between kernel and user space
3. Reduce Interrupts
• Use large transfers instead of multiple small ones
• Employ smart controllers
• Use polling when appropriate
4. Use DMA (Direct Memory Access)
• Allow devices to transfer data directly to/from memory
********** 4 **********
--- page 5 ---
• Frees CPU from data transfer burden
5. Use Smarter Hardware Devices
•   Intelligent controllers with built-in processing capabilities
6. Balance System Resources
• Balance CPU, memory, bus, and I/O performance for highest
throughput
7. Move User-mode Processes to Kernel Threads
• Reduces overhead for frequently used I/O operations
8. Implement Efficient Buffering and Caching
• Buffer data to handle speed/size mismatches
• Cache frequently accessed data on faster devices
2 A Examine the synchronization problem in operating systems, identifying the
challenges it creates. Analyse how counting semaphores provide a
structured solution and resolve these issues in the Readers–Writers
problem.
Explain Synchronization Problem in Detail [4 marks]
Readers-Writers Problem [6 marks]
The Synchronization Problem arises in a multi-process or multi-threaded
environment when multiple processes concurrently access and manipulate
shared data. The core issue is that the final result of the execution depends
on the specific order in which instructions are interleaved, leading to
unpredictable and inconsistent results. This is known as a race condition.
Causes and Consequences:
1. Race Condition: Occurs when several processes access and modify
the same shared data concurrently, and the outcome of the execution
depends on the order of access.
2. Data Inconsistency: The primary consequence is that the shared data
may end up in a corrupted or inconsistent state.
Example (The Critical Section Problem): A simple counter shared by two
threads, one incrementing and the other decrementing. The operations
(Read → Modify → Write) are not atomic. If the operations are interrupted
and interleaved, the final count can be incorrect (e.g., instead of
100→101→100, it might become 100→101→101).
Requirements for a Correct Solution:
1. Mutual Exclusion: Only one process can be executing in its critical
section at any time.
2. Progress: If no process is executing in its critical section and some
processes wish to enter, then only those processes not in their
remainder sections can participate in deciding which will enter next,
and this selection cannot be postponed indefinitely.
3. Bounded Waiting: There must be a limit on the number of times
other processes are allowed to enter their critical sections after a
process has made a request to enter its critical section and before
that request is granted.
B. Counting Semaphore for Readers-Writers Problem [6 marks]
The Readers-Writers Problem is a classic synchronization problem where
multiple processes try to access a shared database.
● Readers only read the data and can do so concurrently.
● Writers modify the data and must have exclusive access (no other
reader or writer allowed).
********** 5 **********
--- page 6 ---
A Counting Semaphore (and a Binary/Mutex semaphore) can be used to
manage this access
Writer Process Logic: The writer needs exclusive access. It only needs to
wait on the general lock (wrt).
do {
wait(wrt);
// Writing is performed
signal(wrt);
} while (TRUE);
Reader Process Logic: Readers need to coordinate using readcount and
the wrt lock.
do {
wait(mutex);   // 1. Lock the readcount variable
readcount++;
if (readcount == 1) {   // 2. First reader locks out the writer
wait(wrt);
}
signal(mutex);   // 3. Unlock the readcount variable
// Reading is performed
wait(mutex);   // 4. Lock the readcount variable
readcount--;
if (readcount == 0) {   // 5. Last reader signals the writer
signal(wrt);
}
signal(mutex);   // 6. Unlock the readcount variable
} while (TRUE);
B Consider the following set of processes, each with varying arrival times
and burst times.
Process   Arrival Time   Burst Time
P1   0   7
P2   2   4
P3   4   1
P4   5   4
P5   6   3
i. Using the SRTF scheduling algorithm, determine the average
waiting time and average response time.
ii. Using the Round-Robin scheduling algorithm with time quantum =
3, determine the average waiting time and average response time.
********** 6 **********
--- page 7 ---
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
3 A Consider the following snapshot of a system running 5 processes:
Pro- Allocation   Max   Available
cess A   B   C   D A   B   C D A B   C D
P0   0   0   1   2 0   0   1   2 1   5   2   0
P1   1   0   0   0 1   7   5   0
P2   1   3   5   4 2   3   5   6
P3   0   6   3   2 0   6   5   2
********** 7 **********
--- page 8 ---
P4   0   0   1   4 0   6   5   6
Answer the following: -
i. How many resources of type A, B, C, D are there?
ii.   Calculate the need matrix?
iii.   Determine if the system is safe or not.
iv.   What will happen if the resource request (0, 4, 2,0) for process P1
arrive, can the system accept this request immediately?
Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks
Safe Sequence 3 Marks
Additional Request 3 Marks
The total number of resources of each type is calculated as:
Total = Allocation (sum) + Available
• A = 2 + 1 = 3
• B = 9 + 5 = 14
• C = 10 + 2 = 12
• D = 12 + 0 = 12
Thus, total system resources = (3, 14, 12, 12).
vi) Need Matrix
Process   A   B   C   D
P0   0   0   0   0
P1   0   7   5   0
P2   1   0   0   2
P3   0   0   2   0
P4   0   6   4   2
vii) Safe State Check
Starting with Available = (1, 5, 2, 0):
• P0 runs → Work = (1, 5, 3, 2)
• P3 runs → Work = (1, 11, 6, 4)
• P2 runs → Work = (2, 14, 11, 8)
• P4 runs → Work = (2, 14, 12, 12)
• P1 runs → Work = (3, 14, 12, 12)
Safe sequence = <P0, P3, P2, P4, P1>. Therefore, the system is SAFE.
viii) Resource Request (0, 4, 2, 0) by P1
********** 8 **********
--- page 9 ---
• Request (0, 4, 2, 0) ≤ Need(P1) = (0, 7, 5, 0) ✔
• Request (0, 4, 2, 0) ≤ Available (1, 5, 2, 0) ✔
After tentative allocation: Available = (1, 1, 0, 0).
Safety test sequence:
• P0 → Work = (1, 1, 1, 2)
• P2 → Work = (2, 4, 6, 6)
• P3 → Work = (2, 10, 9, 8)
• P4 → Work = (2, 10, 10, 12)
• P1 → completes.
Safe sequence = <P0, P2, P3, P4, P1>. Hence, the request CAN be
granted immediately.
B Describe the concept and working of a Translation Lookaside Buffer (TLB) 10
in a paging system. Explain how address translation is carried out with and
without TLB.
Definition and Need of TLB (2 Marks)
address translation without TLB (4 Marks)
address translation with TLB (4 Marks)
• A Translation Lookaside Buffer (TLB) is a special high-speed cache
that stores recent translations of virtual page numbers (VPNs) to
physical frame numbers (PFNs).
•   In a paging system, every memory access requires a page table lookup
to translate the virtual address into a physical address.
• This lookup takes extra time (additional memory access), which slows
down the system.
• The TLB reduces this delay by caching frequently used page table
entries — providing fast access to address translations.
Address translation is carried out with TLB.
********** 9 **********

[Text in pictures on this page, read by OCR]
frame e

logical address physical address 0x000
frame f
cpu slp | a |
p — Oxfff
f frame g

physical memory

page table
--- page 10 ---
Address translation is carried without TLB.
4 A Provide a comparative analysis of the Monolithic and Layered architectures 10
of Operating Systems. Include appropriate diagrams to support your
explanation.
Monolithic Architecture (3 Marks)
Layered Architecture (3 Marks)
Comparative Analysis (4 Marks)
Operating System architecture defines the structure and organization of the
OS components and their interaction with each other and hardware.
Two commonly used architectures are Monolithic and Layered
architectures.
Monolithic Architecture (3 Marks)
Explanation:
•   In a monolithic system, the entire operating system is working in a
single kernel space.
•   All system components such as   file management, process
scheduling, memory management, and device drivers are integrated
into one large block of code that runs in supervisor mode.
•   It provides high performance because there are no inter-layer
overheads, but poor modularity and difficult debugging.
Diagram:
********** 10 **********

[Text in pictures on this page, read by OCR]
logical

address
CPU +> pid

page frame

number number

E TLB hit physical

BI address
Lt | 4d }—

TLB

TLB miss

a physical
memory

page table
--- page 11 ---
Advantages:
• High execution speed (no layer overhead).
•   Efficient direct access to hardware.
Disadvantages:
•   Difficult to maintain and debug.
• Poor security and modularity—failure in one module may crash the
entire system.
Examples:
MS-DOS, UNIX (early versions), Linux (partially monolithic).
Layered Architecture (3 Marks)
Explanation:
•   In layered architecture, the OS is divided into multiple layers, each
built upon the lower one.
• Each layer performs specific functions and interacts only with its
adjacent layers.
• The bottom layer deals with hardware, while the top layer provides
user interfaces.
Diagram:
********** 11 **********

[Text in pictures on this page, read by OCR]
applications

glibc standard c library

system-call interface
file CPU
systems scheduler
networks memory
(TCP/IP) manager
block character
devices devices

device drivers

hardware
--- page 12 ---
Advantages:
•   Better modularity and maintainability.
•   Easier to test and debug individual layers.
• Higher security and reliability due to restricted communication.
Disadvantages:
• Slower execution due to layer-to-layer communication overhead.
•   Difficult to design and define proper boundaries between layers.
Examples:
THE Operating System, Windows NT, OS/2.
Comparative Analysis (4 Marks)
Feature   Monolithic OS   Layered OS
Structure   Single large kernel Multiple   layers   with   clear
interfaces
Performance   High   (no Slightly slower (due to layering)
overhead)
Modularity   Poor   Excellent
Maintainability Difficult   Easier to maintain and modify
Security   Low   (shared High   (restricted   inter-layer
kernel)   access)
Examples   MS-DOS, UNIX   Windows NT, THE OS
Conclusion:
Monolithic architecture emphasizes performance, whereas layered
architecture   emphasizes   modularity,   reliability,   and   security.
Modern operating systems often adopt a hybrid approach, combining the
speed of monolithic design with the structure of layered models.
B A disk queue with requests on cylinders 85, 170, 45, 130, 25, 115, 72, 58 10
needs to be serviced. The disk head is initially at cylinder 60, and the disk
has cylinders numbered 0-199. Calculate the total head movement for:
1. FCFS
2. SSTF
3. SCAN (assuming initial direction towards cylinder 199)
4. C-SCAN (assuming initial direction towards cylinder 199)
Compare the performance of each algorithm and determine which suits best
for this scenario.
********** 12 **********

[Text in pictures on this page, read by OCR]
application file device user
program system driver mode

messages: messages

CPU
scheduling

memory
managment

kernel
mode

interprocess
communication

microkernel

hardware
--- page 13 ---
Each Algorithm 2 Marks
Comparison 2 Marks

RK KKK RK KK 13 2h KKK RK Kk KK
--- page 14 ---
Best Algorithm for This Scenario:
SSTF provides the best performance with only 180 cylinders of movement,
making it ideal for this scenario where minimizing seek time is the priority
and the request queue is relatively small, reducing starvation risk.
5 A Describe the concept of monitors in process synchronization with internal 10
structure and functioning. Explain how monitors manage process
coordination using condition variables and synchronization primitives.
Concept of Monitors (2 Marks)
Internal Structure of a Monitor (4 Marks)
Functioning and Coordination (4 Marks)
In concurrent programming, monitors are high-level synchronization
constructs that provide a convenient and safe mechanism for process
coordination.
They encapsulate shared data, the procedures that operate on that data, and
the synchronization between concurrent processes — all within a single
module.
Monitors eliminate many of the errors possible when using low-level
primitives such as semaphores.
A monitor is a software module with:
• Shared data variables.
• A set of procedures (only one process can execute inside the
monitor at a time).
• Condition variables for process synchronization.
It ensures mutual exclusion automatically — no two processes can execute
monitor procedures simultaneously.
********** 14 **********

[Text in pictures on this page, read by OCR]
Performance Comparison

Algorithm Total Movement Characteristics

FCFS 572 Simple, fair, but high seek time

SSTF 188 Minimal movement, risk of starvation
SCAN 313 Fair, predictable, moderate performance

C-SCAN 396 More uniform wait time, higher movement
--- page 15 ---
Internal Structure of a Monitor (4 Marks)
Components:
1. Shared Data: Variables accessible only through monitor procedures.
2. Procedures: Define operations that can be performed on shared data.
3. Initialization Code: Sets up initial values for data and conditions.
4. Condition Variables: Used for process synchronization (e.g., x, y).
Pseudocode syntax of a monitor:
monitor monitor-name
{
// shared variable declarations
function P1 (…) { …. }
function P2 (…) { …. }
function Pn (…) {……}
initialization code (…) { … }
}
Diagram of Monitor Structure (1 Mark)
+-----------------------------------+
Functioning and Coordination (4 Marks)
Condition Variables and Synchronization:
• Condition variables allow a process to wait for a certain condition
to become true.
• Two basic operations are used:
o wait(c) → Process is suspended until another process signals
condition c.
o signal(c) → Wakes up one waiting process on condition c.
• Mutual exclusion: Achieved automatically; only one process
executes within the monitor.
•   Synchronization: Managed through wait and signal on condition
variables.
• No busy waiting: Blocked processes are placed in a waiting queue
inside the monitor.
Advantages of Monitors
********** 15 **********
--- page 16 ---
• Provides structured and safer synchronization compared to
semaphores.
•   Eliminates errors like deadlocks and race conditions caused by
improper semaphore use.
• Promotes modularity and clarity in concurrent program design.
B Explain how fragmentation affects memory management in operating 10
systems and illustrate the different types of fragmentation with suitable
example. A system has five memory partitions of sizes 110 KB, 480 KB,
210   KB,   350   KB,   and   140   KB   respectively.
A sequence of processes arrives for allocation in the following order: P1 =
100 KB, P2 = 200 KB, P3 = 300 KB, P4 = 140 KB, and P5 = 50 KB.
Considering Contiguous memory allocation, show the final process-to-
partition allocations using First-Fit, Best-Fit, and Worst-Fit memory
allocation strategies.
Marks Distribution:
Fragmentation 2 Marks
Types 2 marks
First Fit – 2 marks
Best Fit – 2 marks
Worst Fit – 2 marks
Fragmentation is a memory management problem that occurs when free memory
space is broken into small, non-contiguous blocks over time. It reduces the
system’s ability to allocate large continuous memory blocks to new processes,
even if total free memory is sufficient.
Fragmentation affects memory utilization and system performance, leading to
inefficient use of available RAM.
Types of Fragmentation
(a) Internal Fragmentation
Definition: Occurs when a fixed-sized memory block allocated to a process is
larger than the process’s actual memory requirement.
Cause: Fixed partitioning or paging schemes with block sizes larger than needed.
Effect: Wasted space inside the allocated partition.
Example:
Suppose a system allocates 4 KB blocks, and a process needs only 3.6 KB.
→ Unused memory = 0.4 KB per process
This 0.4 KB inside the allocated block is internally fragmented.
External Fragmentation
Definition: Occurs when total free memory exists but is scattered in non-
contiguous blocks, preventing allocation of large processes.
Cause: Dynamic memory allocation where processes are loaded and removed
frequently.
Effect: Wasted space outside allocated partitions.
Example:
Assume memory = 100 MB total. Free blocks: 20 MB + 15 MB + 10 MB (non-
contiguous).
********** 16 **********
--- page 17 ---
A process requesting 40 MB cannot be allocated, though 45 MB is free in total.
6 A   I.   Apply your understanding of process scheduling to compare Long- 10
term and Short-term schedulers in terms of their purpose, execution
frequency, speed, alternate names, and where process selection
occurs (main or secondary memory).
II.   Apply the concepts of process scheduling to justify why time-
sharing systems rely more on Short-term scheduler, while batch-
processing systems depend more on Long-term scheduler.
I.   5 Marks (One mark for each criteria)
II.   5 Marks
Solution:
i. Following are the differences between a LTS and STS:- (5 marks)
********** 17 **********
--- page 18 ---
Aspect   Long-Term Scheduler   Short-Term Scheduler
Frequency   Runs less frequently.   Runs very frequently.
Speed   Slower, as it involves   Faster, as it focuses
more complex decision-   solely on CPU allocation.
making and memory
checks.
Process   Selects processes from the   Selects processes from
selection   job pool (secondary   the ready queue (main
location   memory).   memory).
Alternate   Job Scheduler   CPU Scheduler
Name
Purpose   Balances I/O-bound and   Maximizes CPU
CPU-bound processes.   utilization and minimizes
process waiting times.
ii. Time-sharing: Many interactive users → responsiveness is critical.
The short-term scheduler (CPU scheduler) decides which process
runs next very frequently (milliseconds). Long-term scheduler is
less relevant because new jobs are admitted immediately.
Batch system: Jobs are large and submitted in bulk. The long-term
scheduler regulates how many jobs enter memory, controlling
degree of multiprogramming. If too many are admitted, system
thrashes; if too few, CPU underutilizes.
(5 marks)
B A system has 3 frames for storing process pages in main memory. Assume
that all the page frames are initially empty. Consider the page reference
string given below:
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Compute the number of page faults and show frame contents step-by-step
for:
(a) FIFO,
(b) LRU,
(c) Optimal.
Also state which algorithm gave the fewest faults.
Marks Distribution:
(FIFO: 3 marks, LRU: 3 marks, Optimal: 3 marks)
Also state which algorithm gave the fewest faults and why.(1 marks)
********** 18 **********
--- page 19 ---
Reference string length = 12. Frames = 3.
(a) FIFO (First-In, First-Out)
Frames after
Step   Ref   Fault?
step (f1,f2,f3)
1   1   1, - , -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
4   4   4, 2, 3 (1 out) Y
5   1   4, 1, 3 (2 out) Y
6   2   4, 1, 2 (3 out) Y
7   5   5, 1, 2 (4 out) Y
8   1   5, 1, 2   N
9   2   5, 1, 2   N
10   3   5, 3, 2 (1 out) Y
11   4   5, 3, 4 (2 out) Y
12   5   5, 3, 4   N
Total page faults (FIFO): 9.
(b) LRU (Least Recently Used)
LRU replaces the page that has not been used for the longest time.
Step   Ref   Frames after step Fault? Comment
1   1   1, -, -   Y   load 1
2   2   1, 2, -   Y   load 2
3   3   1, 2, 3   Y   load 3
4, 2, 3 (1 was
4   4   Y
LRU)
4, 1, 3 (2 LRU
5   1   Y
replaced)
4, 1, 2 (3 LRU
6   2   Y
replaced)
********** 19 **********
--- page 20 ---
5, 1, 2 (4 LRU
7   5   Y
replaced)
8   1   5, 1, 2   N
9   2   5, 1, 2   N
3, 1, 2 (5 LRU
10   3   Y
replaced)
3, 4, 2 (1 LRU
11   4   Y
replaced)
3, 4, 5 (2 LRU
12   5   Y
replaced)
Total page faults (LRU): 10.
(c) Optimal (Belady’s optimal algorithm) — replace the page that will not
be used for the longest time in the future.
Frames after
Step   Ref   Fault?
step
1   1   1, -, -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
1, 2, 4 (3
replaced; will be
4   4   used later   Y
sooner than 1 or
2?)*
5   1   1, 2, 4   N
6   2   1, 2, 4   N
1, 2, 5 (4
replaced: 4 next
used at step 11;
7   5   Y
1 and 2 are
needed earlier at
steps 8 and 9)
8   1   1, 2, 5   N
9   2   1, 2, 5   N
3, 2, 5 (1
replaced; 1 next
10   3   Y
used later than 2
or 5)
********** 20 **********
--- page 21 ---
3, 4, 5 (2
11   4   Y
replaced)
12   5   3, 4, 5   N
Total page faults (Optimal): 7.
Optimal gives the fewest faults (7) because it uses future knowledge. For
real systems we cannot implement Optimal, but it is used as a baseline. In
this case FIFO (9) beats LRU (10) — showing that LRU is usually good
but not always strictly better than FIFO, and that algorithms’ effectiveness
depends on the reference string.
7 A Analyze the Resource Allocation Graph
i)   Write resource allocated and requested table
ii)   Find if there is a deadlock or not? If there is no deadlock then
what will be the sequence of the process to get executed?
iii)   What will happen if one instance of resource R3 is removed
from the system.
I.   4 marks
II.   4 Marks
III.   2 Marks
i)
********** 21 **********
--- page 22 ---
II) System is in Safe State. Safe Sequence: P2, P0, P1, P3
III) There will be a deadlock in the system.
B Explain user level and kernel level threads. Which one are more light 5
weight and independent?
User and Kernel Thread 3 marks
Explanation 2 marks
Solution: User-level threads are managed entirely by a user-level thread
library without direct involvement from the operating system's kernel.
The kernel is unaware of their existence and treats the entire process
containing these threads as a single unit of execution.
(1.5 marks)
Kernel-level threads are managed directly by the operating system's
kernel. The kernel is aware of each individual kernel thread and handles
their creation, scheduling, and management.   (1.5 marks)
User-level threads are managed by a user-level thread library, making
them more lightweight as they don't require kernel intervention and offer
faster context switching, but are less independent as a blocking thread can
block the entire process. Kernel-level threads are managed by the
operating system, are more independent because they can take advantage
of multiple CPUs and are not tied to a single process's blocking state but
are more heavyweight due to the overhead of kernel mode transitions and
are slower to create and switch.
(2 marks)
C   Differentiate between sequential access and direct access methods for files. 5
Provide examples of applications where each access method would be
preferred.
Difference 4 marks
Example 1 marks
Sequential Access In sequential access, data in a file is processed in
order, one record or byte after the next. The operations typically used are
read next and write next. Repositioning within the file usually requires a
Reset (rewind) operation to go back to the beginning.
********** 22 **********
--- page 23 ---
Direct Access Direct access views a file as a numbered sequence of fixed-
length logical records. This method allows for immediate, random access
to any part of the file. Operations include explicitly reading or writing
record number (read n, write n), and moving the file pointer directly to
record (position to n).
Application Preference:
Sequential Access Preference This method is preferred for applications
where files must be processed entirely from beginning to end. Examples
include simple text files, log files (where records are appended
chronologically), and source code files read by a compiler.
Direct Access Preference Direct access is preferred for applications that
require quick, random retrieval and update of specific records. A prime
example is an Indexed/Relative File system, commonly used in databases
or any system (like a customer database or airline reservation system)
where a record must be accessed by its index or relative block number.
********** 23 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper b77aeadefccc

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CSBS_7036/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 Jul 2026
- Text: mixed (34 pages), mean OCR confidence 74.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech
(IT)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 14 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 34 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   1. Define Operating System & Objectives
An Operating System (OS) is system software that acts as an interface
between the user and the computer hardware. It manages hardware
resources and provides services for application programs, ensuring
efficient and convenient system operation.
Objectives of a modern Operating System:
CO- 1;   1. Convenience: Makes the computer system easy to use.
SO-2 ;
2. Efficiency: Ensures optimal use of hardware resources like CPU,
BL-2
memory, and I/O devices.
3. Ability to Evolve: Allows the system to be updated with new
features and improvements.
4. Resource Management: Efficiently allocates and manages
system resources among processes.
b.   2. Process Control Block (PCB) and its Components
A Process Control Block (PCB) is a data structure used by the operating
CO-2 ;
SO-2 ;   system to store all relevant information about a process. It is essential for
BL-2   process management and context switching.
Components of PCB:
********** 1 **********
--- page 2 ---
• Process ID (PID): Unique identifier assigned to each process.
• Process State: Indicates whether the process is new, ready,
running, waiting, or terminated.
• Program Counter: Stores the address of the next instruction to
be executed.
• CPU Registers: Holds the values of CPU registers for the
process.
• Memory Management Information: Includes details like page
tables, base and limit registers.
• I/O Status Information: Contains information about I/O devices
allocated to the process.
• Accounting Information: Tracks CPU usage, execution time,
and other statistics.
c.   3. Conditions for Critical Section Problem
To ensure correct and fair access to shared resources, a solution to the
CO-3 ;   critical section problem must satisfy the following conditions:
SO-2 ;   1. Mutual Exclusion: Only one process can execute in the critical
BL-2
and BL-3   section at any given time.
2. Progress: If no process is in the critical section, the selection of
the next process cannot be postponed indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
Process ID

Process state

Process priority

Accounting information

Program counter

CPU registers

PCB pointers

List of open files

Process I/O status information
--- page 3 ---
3. Bounded Waiting: There must be a limit on how many times
other processes can enter the critical section before a waiting
process gets its turn
d.   Necessary Conditions for Deadlock
Deadlock can occur only if all the following four conditions hold
simultaneously:
1. Mutual Exclusion: At least one resource must be held in a non-
shareable mode.
2. Hold and Wait: A process holding at least one resource is waiting
CO-3 ;
SO-2 ;   to acquire additional resources.
BL-2   3. No Preemption: Resources cannot be forcibly taken from a
process; they must be released voluntarily.
4. Circular Wait: A circular chain of processes exists where each
process is waiting for a resource held by another process in the
chain.
a. SRTF (Preemptive SJF)
Gantt Chart
0 1 5 7 11 16
| P2 | P3 | P0 | P1 | P2 |
Completion Time (CT)
• P2 = 16
• P3 = 5
Q2   • P1 = 11
CO-2;   • P0 = 7
[20]
SO-2;   Turnaround Time (TAT = CT – AT)
BL-3
and BL-4   • P2 = 16 – 0 = 16
• P3 = 5 – 1 = 4
• P1 = 11 – 2 = 9
• P0 = 7 – 3 = 4
Waiting Time (WT = TAT – BT)
• P2 = 16 – 6 = 10
• P3 = 4 – 4 = 0
• P1 = 9 – 4 = 5
********** 3 **********
--- page 4 ---
• P0 = 4 – 2 = 2
Average Times
• Average Waiting Time = (10 + 0 + 5 + 2) / 4 = 4.25
• Average Turnaround Time = (16 + 4 + 9 + 4) / 4 = 8.25
ii) Non-Preemptive SJF
Gantt Chart
0 6 8 12 16
| P2 | P0 | P3 | P1 |
Completion Time (CT)
• P2 = 6
• P0 = 8
• P3 = 12
• P1 = 16
Turnaround Time (TAT)
• P2 = 6 – 0 = 6
• P0 = 8 – 3 = 5
• P3 = 12 – 1 = 11
• P1 = 16 – 2 = 14
Waiting Time (WT)
• P2 = 6 – 6 = 0
• P0 = 5 – 2 = 3
• P3 = 11 – 4 = 7
• P1 = 14 – 4 = 10
Average Times
• Average Waiting Time = (0 + 3 + 7 + 10) / 4 = 5
• Average Turnaround Time = (6 + 5 + 11 + 14) / 4 = 9
iii) Comparison (2 Marks)
• SRTF (Preemptive SJF) gives better performance with:
o Lower Average Waiting Time (4.25 < 5)
o Lower Average Turnaround Time (8.25 < 9)
• This is because shorter processes get CPU earlier due to
preemption.
• However, SRTF is more complex and may cause frequent
context switching.
********** 4 **********
--- page 5 ---
(i) What is a Semaphore? Explain its Types (3 Marks)
A semaphore is a synchronization tool used in operating systems to
control access to shared resources by multiple processes or threads.
It is essentially an integer variable that is accessed only through two
atomic operations: wait() and signal().
Types of Semaphores:
Binary Semaphore (Mutex)
Takes only two values: 0 or 1
Used for mutual exclusion (only one process can access the critical
section at a time)
Example:
A printer shared by multiple processes
If semaphore = 1 → resource is free
If semaphore = 0 → resource is busy
Counting Semaphore
Can take non-negative integer values (0, 1, 2, …)
Used when multiple instances of a resource are available
Example:
A system with 3 identical printers → semaphore initialized to 3
Each process decreases count when using a printer and increases
after releasing
(ii) Semaphore Implementation Using Busy Waiting (4 Marks)
In busy waiting, a process continuously checks (loops) until the
semaphore becomes available.
Operations:
wait(S) {
while (S <= 0);   // busy waiting (spin lock)
S--;
}
signal(S) {
********** 5 **********
--- page 6 ---
S++;
}
Explanation:
•   wait(S):
o Checks if S > 0
o   If not, it keeps checking repeatedly (CPU is busy)
o When S > 0, it decrements S and enters the critical
section
•   signal(S):
o Increments the semaphore value
o Indicates that the resource is released
Drawback:
• CPU cycles are wasted while waiting
•   Inefficient for long waiting periods
(iii) Semaphore Without Busy Waiting (4 Marks)
To avoid wasting CPU time, semaphores can be implemented using
blocking (sleep) and wakeup mechanisms.
Operations:
wait(S) {
S--;
if (S < 0) {
add process to queue;
block();   // process goes to sleep
}
}
signal(S) {
S++;
if (S <= 0) {
remove process from queue;
wakeup(process);
}
}
Explanation:
wait(S):
********** 6 **********
--- page 7 ---
If resource not available → process is blocked
It is placed in a waiting queue
signal(S):
Wakes up one waiting process from the queue
Advantages:
No CPU wastage (no spinning)
Better CPU utilization
Efficient for systems with many processes
i   Readers–Writers Problem
The Readers–Writers problem is a classic synchronization problem in
operating systems that deals with managing access to a shared
resource (like a file or database).
• Readers → only read the data (do not modify)
• Writers → modify the data
Key Requirement:
• Multiple readers can access the resource simultaneously
• Only one writer can access the resource exclusively
• No reader should read while a writer is writing
Q3
Types of Readers–Writers Problems
CO-2;
1. Reader Priority → Readers are not blocked unless a writer is   [20]
SO-2;
BL-3 and   already writing
BL-4
2. Writer Priority → Writers get priority (avoid starvation)
3. Fair Solution → No starvation for either
(Below is the standard Reader-Priority solution using semaphores)
Semaphore-Based Solution
Initialization:
semaphore mutex = 1;   // protects readCount
semaphore wrt = 1;   // controls access to shared resource
int readCount = 0;   // number of active readers
Reader Process
********** 7 **********
--- page 8 ---
wait(mutex);
readCount++;
if (readCount == 1)
wait(wrt);   // first reader blocks writers
signal(mutex);
// Reading is performed
wait(mutex);
readCount--;
if (readCount == 0)
signal(wrt); // last reader releases writer
signal(mutex);
Writer Process
wait(wrt);
// Writing is performed
signal(wrt);
How the Solution Works
1. Handling Multiple Readers
• The variable readCount keeps track of active readers
•   First reader locks the resource using wait(wrt)
• Subsequent readers:
o Do NOT block
o Can read simultaneously
• Hence, multiple readers are allowed concurrently
2. Handling Single Writer
• Writer uses wait(wrt)
•   If:
o Any reader is active OR
********** 8 **********
--- page 9 ---
o Another writer is active
→ writer must wait
• Ensures only one writer at a time
3. Mutual Exclusion Logic
• mutex protects updates to readCount
• wrt ensures:
o No writer enters when readers are present
o No readers enter when a writer is active
Key Advantages
•   Efficient for read-heavy systems
• Allows maximum concurrency for readers
Limitation
•   Writers may suffer from starvation
(continuous arrival of readers may delay writers indefinitely)
Conclusion
• The semaphore-based solution ensures:
o Concurrent access for readers
o Exclusive access for writers
• Achieves synchronization using:
o mutex → protects shared variable
o wrt → controls resource access.
Here is the descriptive answer (without bullets, exam-ready format):
a) Round Robin Scheduling (Time Quantum = 3 ms)
All processes arrive at time 0 ms, so scheduling starts in the order P1,
P2, P3, and P4.
Gantt Chart
0 3 6 9 12 14 17 18 21 23 24
********** 9 **********
--- page 10 ---
| P1 | P2 | P3 | P4 | P1 | P2 | P3 | P4 | P2 | P4 |
Completion Times
P3 completes at 18 ms, P1 at 14 ms, P2 at 23 ms, and P4 at 24 ms.
Turnaround Time (TAT = CT – AT)
Since all arrival times are 0:
P1 = 14, P2 = 23, P3 = 18, P4 = 24
Waiting Time (WT = TAT – BT)
P1 = 14 – 5 = 9
P2 = 23 – 7 = 16
P3 = 18 – 4 = 14
P4 = 24 – 6 = 18
Average Values
Average Waiting Time = (9 + 16 + 14 + 18) / 4 = 14.25 ms
Average Turnaround Time = (14 + 23 + 18 + 24) / 4 = 19.75 ms
b) First Come First Serve (FCFS)
Since all processes arrive at the same time, execution follows the order
P1, P2, P3, P4.
Gantt Chart
0 5 12 16 22
| P1 | P2 | P3 | P4 |
Completion Times
P1 = 5, P2 = 12, P3 = 16, P4 = 22
Turnaround Time
P1 = 5, P2 = 12, P3 = 16, P4 = 22
Waiting Time
P1 = 0
P2 = 5
P3 = 12
P4 = 16
Average Values
Average Waiting Time = (0 + 5 + 12 + 16) / 4 = 8.25 ms
Average Turnaround Time = (5 + 12 + 16 + 22) / 4 = 13.75 ms
c) Comparison of Round Robin and FCFS
********** 10 **********
--- page 11 ---
From the results, it is observed that FCFS provides lower average
waiting time and turnaround time compared to Round Robin in this
case. This is because all processes arrive at the same time and shorter
processes are not delayed by time slicing.
Round Robin, on the other hand, ensures fairness by giving equal CPU
time to each process, but it increases waiting time due to frequent
context switching. Therefore, FCFS performs better for this specific
scenario, while Round Robin is more suitable for time-sharing systems
where responsiveness is important.
If you want, I can also give this in step-wise solving format (for
students to follow easily in exams) or convert it into a Word
document.
Deadlock is a situation in an operating system where a set of processes
are permanently blocked because each process is waiting for a resource
that is held by another process in the same set. As a result, none of the
processes can proceed, and the system gets stuck in a circular waiting
state. A common real-life analogy is two people each holding one
resource and waiting for the other to release theirs—neither moves
forward.
For a deadlock to occur, four necessary conditions must hold
Q4   simultaneously. The first is mutual exclusion, meaning at least one
CO-2;   resource must be non-shareable; only one process can use it at a time.
SO-2;   [20]
BL-3   The second is hold and wait, where a process holding at least one
and BL-4   resource is waiting to acquire additional resources held by other
processes. The third is no preemption, which implies that resources
cannot be forcibly taken away from a process; they must be released
voluntarily. The fourth is circular wait, where a circular chain of
processes exists such that each process is waiting for a resource held by
the next process in the cycle. If any one of these conditions is
prevented, deadlock cannot occur.
Operating systems use different techniques to handle deadlock, broadly
classified as prevention, detection, and recovery.
********** 11 **********
--- page 12 ---
In deadlock prevention, the system is designed in such a way that at
least one of the four necessary conditions is never allowed to occur. For
example, mutual exclusion can be reduced by making resources
sharable where possible, though this is not always practical. The hold-
and-wait condition can be avoided by requiring processes to request all
needed resources at once before execution begins, or by forcing them to
release currently held resources before requesting new ones. The no-
preemption condition can be handled by allowing the system to take
resources away from a process if it requests additional ones and cannot
be satisfied immediately. Circular wait can be prevented by imposing a
strict ordering on resource types and requiring processes to request
resources in that order. While prevention guarantees that deadlocks
never occur, it often leads to poor resource utilization and reduced
system efficiency.
In deadlock detection, the system allows deadlocks to occur but
periodically checks whether they have happened. This is typically done
using structures like a resource allocation graph or matrix-based
algorithms. If the system has only single instances of resources, a cycle
in the graph indicates deadlock. For multiple instances, more complex
detection algorithms similar to the Banker’s algorithm are used.
Detection is suitable for systems where deadlocks are rare, as it avoids
the overhead of strict prevention but requires additional computation to
monitor system state.
Once a deadlock is detected, the system must apply recovery
techniques to break the deadlock. One approach is process
termination, where one or more processes involved in the deadlock are
aborted. This can be done either by terminating all deadlocked
processes or by selecting processes one by one until the cycle is broken.
Another approach is resource preemption, where resources are taken
away from certain processes and given to others until the deadlock is
resolved. This requires careful handling to avoid inconsistencies, and
processes may need to be rolled back to a safe state before execution
resumes.
In summary, deadlock is a critical issue in resource management where
processes block each other indefinitely. The four necessary conditions
********** 12 **********
--- page 13 ---
define its occurrence, and operating systems handle it either by
preventing it altogether, detecting it after occurrence, or recovering
from it. Each approach involves trade-offs between system
performance, complexity, and resource utilization.
Here is the exam-style solution with proper columns (3 frames):
FIFO Page Replacement
Re Frame Frame Frame Page
f   1   2   3   Fault
5   5   -   -   Yes
0   5   0   -   Yes
1   5   0   1   Yes
0   5   0   1   No
2   2   0   1   Yes
3   2   3   1   Yes
0   2   3   0   Yes
2   2   3   0   No
4   4   3   0   Yes
3   4   3   0   No
3   4   3   0   No
2   4   2   0   Yes
0   4   2   0   No
2   4   2   0   No
1   1   2   0   Yes
2   1   2   0   No
7   1   7   0   Yes
0   1   7   0   No
1   1   7   0   No
1   1   7   0   No
********** 13 **********
--- page 14 ---
0   1   7   0   No
Total Page Faults (FIFO) = 15
LRU Page Replacement
Re Frame Frame Frame Page
f   1   2   3   Fault
5   5   -   -   Yes
0   5   0   -   Yes
1   5   0   1   Yes
0   5   0   1   No
2   2   0   1   Yes
3   2   3   1   Yes
0   2   3   0   Yes
2   2   3   0   No
4   4   3   0   Yes
3   4   3   0   No
3   4   3   0   No
2   4   3   2   Yes
0   0   3   2   Yes
2   0   3   2   No
1   0   1   2   Yes
2   0   1   2   No
7   7   1   2   Yes
0   7   0   2   Yes
1   7   0   1   Yes
1   7   0   1   No
0   7   0   1   No
Total Page Faults (LRU) = 12
Optimal Page Replacement
********** 14 **********
--- page 15 ---
Re Frame Frame Frame Page
f   1   2   3   Fault
5   5   -   -   Yes
0   5   0   -   Yes
1   5   0   1   Yes
0   5   0   1   No
2   2   0   1   Yes
3   2   0   3   Yes
0   2   0   3   No
2   2   0   3   No
4   2   4   3   Yes
3   2   4   3   No
3   2   4   3   No
2   2   4   3   No
0   2   0   3   Yes
2   2   0   3   No
1   2   0   1   Yes
2   2   0   1   No
7   2   0   7   Yes
0   2   0   7   No
1   1   0   7   Yes
1   1   0   7   No
0   1   0   7   No
Total Page Faults (Optimal) = 9
Final Conclusion
Optimal algorithm gives the minimum page faults, followed by LRU
and then FIFO. Therefore, Optimal is the best, while LRU is the best
practical approach.
********** 15 **********
--- page 16 ---
Here is the proper step-by-step exam solution (Banker’s Algorithm):
Step 1: Given Data
Allocation Matrix
P0 → (1 0 2 1)
P1 → (0 1 1 0)
P2 → (1 2 0 1)
P3 → (0 0 1 2)
Max Matrix
P0 → (3 2 2 2)
P1 → (1 3 3 1)
P2 → (2 4 1 2)
P3 → (1 2 2 3)
Available = (2 1 0 1)
i) Need Matrix Calculation
Q5
Need = Max – Allocation
CO-2;
P0 → (3−1, 2−0, 2−2, 2−1) = (2 2 0 1)
SO-2;   [20]
BL-3   P1 → (1−0, 3−1, 3−1, 1−0) = (1 2 2 1)
and BL-4   P2 → (2−1, 4−2, 1−0, 2−1) = (1 2 1 1)
P3 → (1−0, 2−0, 2−1, 3−2) = (1 2 1 1)
ii) Check Safe State
Initial Available = (2 1 0 1)
Now compare Need ≤ Available:
P0 → (2 2 0 1) ✗ (B not satisfied)
P1 → (1 2 2 1) ✗
P2 → (1 2 1 1) ✗
P3 → (1 2 1 1) ✗
No process can proceed since no Need is ≤ Available.
Conclusion
The system is NOT in a safe state because no process can execute first.
Hence, no safe sequence exists.
********** 16 **********
--- page 17 ---
iii) Request from P3 = (0 1 0 1)
Step 1: Check Request ≤ Need
P3 Need = (1 2 1 1)
Request = (0 1 0 1) → satisfies condition ✓
Step 2: Check Request ≤ Available
Available = (2 1 0 1)
Request = (0 1 0 1) → satisfies condition ✓
Step 3: Allocate Temporarily
New Available = (2 1 0 1) − (0 1 0 1) = (2 0 0 0)
New Allocation of P3 = (0 1 1 3)
New Need of P3 = (1 1 1 0)
Step 4: Check Safe State Again
Available = (2 0 0 0)
P0 → (2 2 0 1) ✗
P1 → (1 2 2 1) ✗
P2 → (1 2 1 1) ✗
P3 → (1 1 1 0) ✗
Again, no process can proceed.
Final Conclusion
The system is not in a safe state initially, and even after granting the
request, it remains unsafe. Therefore, the request cannot be granted
immediately.
********** 17 **********
--- page 18 ---
How Segmentation Overcomes Limitations of Paging
Paging divides memory into fixed-size blocks (pages/frames), which
simplifies allocation but introduces some limitations. Segmentation
addresses these issues as follows:
•   In paging, programs are divided into fixed-size pages without
considering the logical structure of a program. This makes it
difficult for programmers to relate memory to program
components. Segmentation, on the other hand, divides memory
based on logical units such as functions, arrays, stacks, and
modules, making it more meaningful and programmer-friendly.
• Paging suffers from internal fragmentation because memory is
allocated in fixed sizes, leading to unused space within a page.
********** 18 **********

[Text in pictures on this page, read by OCR]
os

Offset
< Limit

CPU Segment | Offset
Number

Logical Address

| | 1500 so

Base Limit
1800 a
|o] 1500 200
1 1800 100
= 2000
2] 2000 | 150 + 82
3| 2400 100
Segment Table 2400 $3
Main Memory

Segmentation

Paging

Logical Physical
Address Address
| 10000..00
cpu |—>| Plid t Il d | Physical

Memory

11111..11

"{

L_, f

Page table
--- page 19 ---
Segmentation eliminates internal fragmentation since segments
are of variable size, matching the actual size of program
components.
• Paging does not support logical protection and sharing
effectively at a high level. Segmentation enables protection and
sharing at segment level, allowing different processes to share
specific segments like libraries while keeping others private.
•   In paging, debugging and maintenance become difficult because
memory is not organized logically. Segmentation improves this
by maintaining a clear mapping between logical program
structure and memory layout.
However, segmentation may introduce external fragmentation, which
paging avoids—so both techniques have trade-offs.
Here is the proper exam solution with step-by-step calculation:
Given:
Request Queue: 98, 183, 37, 122, 14, 124, 65, 67
Initial Head Position = 53
i) FCFS (First Come First Serve)
In FCFS, requests are served in the order they arrive.
Sequence:
Q6
53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67
CO-3;
SO-2;   Head Movements:   [20]
BL-2
Movemen Distanc
and BL-4
t   e
53 → 98 45
98 → 183 85
183 → 37 146
37 → 122 85
122 → 14 108
14 → 124 110
124 → 65 59
********** 19 **********
--- page 20 ---
65 → 67 2
Total Head Movement:
45 + 85 + 146 + 85 + 108 + 110 + 59 + 2 = 640 tracks
ii) SSTF (Shortest Seek Time First)
In SSTF, the closest request to the current head position is serviced
first.
Step-wise Selection:
From 53 → nearest is 65
From 65 → nearest is 67
From 67 → nearest is 37
From 37 → nearest is 14
From 14 → nearest is 98
From 98 → nearest is 122
From 122 → nearest is 124
From 124 → nearest is 183
Sequence:
53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183
Head Movements:
Movemen Distanc
t   e
53 → 65 12
65 → 67 2
67 → 37 30
37 → 14 23
14 → 98 84
98 → 122 24
122 →
2
124
124 →
59
183
Total Head Movement:
12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = 236 tracks
********** 20 **********
--- page 21 ---
Final Answer
FCFS total head movement = 640 tracks
SSTF total head movement = 236 tracks
Conclusion
SSTF performs better than FCFS because it minimizes the seek time by
selecting the nearest request, resulting in significantly lower head
movement.
File Management in Operating System
********** 21 **********
--- page 22 ---
Concept of File Management
File management is a fundamental function of an operating system that
deals with the creation, organization, storage, retrieval, and
protection of files on secondary storage devices such as disks.
A file is a collection of related data stored on a storage device and
treated as a single unit by the OS. The operating system provides an
abstraction so users do not need to know how data is physically stored.
The OS is responsible for:
• Creating and deleting files
• Reading and writing data
• Managing directories (folders)
•   Controlling access permissions (security)
•   Allocating disk space efficiently
• Maintaining file metadata (size, type, location, timestamps)
Thus, file management ensures efficient, reliable, and secure data
storage and access.
File Organization Methods
File organization refers to how records within a file are arranged for
storage and retrieval.
1. Sequential File Organization
********** 22 **********

[Text in pictures on this page, read by OCR]
Comparison of File Designs

Sequential Direct-Access Indexed-Sequential
Types of Access batch online batch or online
Data Organization sequentially no particular sequentially and by
by key value order index
Flexibility in low high very high
Handling Inquiries
Availability of no yes yes
Up-to-Date Data
Speed of Retrieval slow very fast fast
Activity high low high
Volatility low high high
Examples payroll airline customer ordering
processing reservations and billing
and billing and banking

operations transactions
--- page 23 ---
• Data is stored in order (record by record)
• Access is done sequentially from beginning to end
•   Suitable for applications like logs or reports
Advantage: Simple and efficient for large batch processing
Limitation: Slow for random access
2. Direct (Random) File Organization
• Records are accessed directly using an address or key
• No need to read previous records
Advantage: Fast access to any record
Limitation: Requires calculation of address (hashing or indexing)
3. Indexed File Organization
• Uses an index table that stores keys and their corresponding
addresses
• Combines benefits of sequential and direct access
Advantage: Efficient searching and retrieval
Limitation: Extra storage required for index
File Storage Methods (Allocation Techniques)
File storage refers to how files are physically placed on disk blocks.
1. Contiguous Allocation
•   File occupies continuous blocks on disk
Advantages:
•   Fast access (both sequential and direct)
• Simple implementation
Disadvantages:
•   External fragmentation
•   Difficult to expand file size
2. Linked Allocation
•   File is stored as a linked list of blocks scattered across disk
• Each block points to the next
Advantages:
• No external fragmentation
********** 23 **********
--- page 24 ---
• Easy file growth
Disadvantages:
• Slow random access
•   Pointer overhead
3. Indexed Allocation
• A separate index block contains addresses of all file blocks
Advantages:
• Supports direct access
• No external fragmentation
Disadvantages:
• Extra space for index block
• Overhead for small files
How Files Are Stored and Accessed
Files are stored on disk as a collection of blocks. The OS maintains
metadata (via structures like file control blocks or inodes) that store:
•   File name, size, permissions
• Location of blocks on disk
When a user accesses a file:
1. The OS searches the directory structure to locate the file
2. Retrieves metadata (block addresses)
3. Uses the allocation method (contiguous/linked/indexed)
4. Reads or writes data from/to disk
Access methods include:
• Sequential access → read/write in order
• Direct access → jump to specific location
• Indexed access → use index for faster retrieval
Conclusion
File management in an OS ensures structured storage, efficient retrieval,
and secure handling of data. Different file organization and allocation
methods are used depending on system requirements, balancing
performance, flexibility, and storage efficiency.
********** 24 **********
--- page 25 ---
Select any 4 only.
1. Explain any two Operating System Services.
Operating System Services (Any Two)
1. Program Execution
Program execution is a core service of an operating system that
enables users to run application programs. The OS loads the
program from secondary storage into main memory, creates a
process, and begins execution. It allocates required resources
such as CPU time, memory, and I/O devices, and manages the
entire lifecycle of the program—from initiation to termination. It
also handles abnormal termination in case of errors, ensuring
smooth and controlled execution.
2. I/O Operations
Q7
The operating system provides a standardized interface for input
CO-
and output operations. Instead of interacting directly with
1,CO2
and CO-   hardware devices like keyboards, disks, or printers, users and   [20]
3; SO-2;
applications communicate through the OS. The OS manages
BL-2
device drivers, buffering, caching, and scheduling of I/O
and BL-3
requests to improve efficiency. It also detects and handles errors,
ensuring reliable communication between software and
hardware.
2. Define single-threaded and multi-threaded processes.
Single-Threaded and Multi-Threaded Processes
A process is a program in execution, and it may contain one or
more threads, which are the basic units of CPU execution.
Single-Threaded Process
A single-threaded process contains only one thread of
execution. This means the process performs one task at a time,
following a single sequence of instructions. If the thread is
blocked (for example, waiting for I/O), the entire process is also
blocked.
********** 25 **********
--- page 26 ---
Example: A simple calculator program that performs one
operation at a time.
Multi-Threaded Process
A multi-threaded process contains multiple threads within the
same process, all sharing the same memory space and resources.
These threads can execute concurrently, allowing the process to
perform multiple tasks simultaneously.
Example: A web browser where one thread handles user
interaction, another loads web pages, and another manages
background tasks.
Key Difference
Single-threaded → one task at a time, simpler but slower
Multi-threaded → multiple tasks concurrently, more efficient but
complex to manage.
3. What are the symbols used in a Resource Allocation Graph
(RAG)? Explain with a small example.
Symbols used in Resource Allocation Graph (RAG)
A Resource Allocation Graph (RAG) is a directed graph used to
represent the allocation of resources to processes and to detect
deadlocks in a system.
The main symbols used in a RAG are as follows:
A process is represented by a circle (○). Each circle denotes a process
such as P1, P2, etc.
A resource type is represented by a rectangle (□). If a resource has
multiple instances, it is shown by multiple dots inside the rectangle.
A request edge is represented by a directed arrow from a process to a
resource (P → R). This indicates that the process is requesting that
resource.
An assignment edge is represented by a directed arrow from a
resource to a process (R → P). This indicates that the resource has
been allocated to that process.
Small Example
********** 26 **********
--- page 27 ---
Consider two processes P1 and P2, and two resources R1 and R2.
Process P1 is holding resource R1 and requesting resource R2. At the
same time, process P2 is holding resource R2 and requesting resource
R1.
********** 27 **********
--- page 28 ---
This situation can be represented using a Resource Allocation Graph
where there is an assignment edge from R1 to P1 and from R2 to P2,
and request edges from P1 to R2 and from P2 to R1.
Such a graph forms a cycle, which indicates the possibility of a
deadlock when each resource has a single instance.
4. Explain the working of Peterson’s Solution using shared
variables (flag and turn).
Peterson’s Solution is a classical software-based solution to the
critical section problem for two processes. It ensures mutual
exclusion, progress, and bounded waiting using two shared
variables:
•   flag[2] → indicates if a process wants to enter the critical section
•   turn → indicates whose turn it is to enter
🔹 Shared Variables
boolean flag[2];   // initially flag[0] = flag[1] = false
int turn;
🔹 Structure for Process Pi (i = 0 or 1)
do {
flag[i] = true;   // Process Pi wants to enter
turn = j;   // Give chance to other process
while (flag[j] && turn == j);   // Wait if Pj wants to enter and
it's Pj's turn
// Critical Section
flag[i] = false;   // Exit section
// Remainder Section
} while (true);
(where j = 1 - i)
********** 28 **********
--- page 29 ---
🔹 Working Explanation
Consider two processes P0 and P1:
1. Desire to Enter Critical Section
o When a process (say P0) wants to enter, it sets:
▪   flag[0] = true
o This indicates interest in entering the critical section.
2. Turn Assignment
o P0 sets turn = 1 (gives priority to P1).
o This ensures fairness if both processes request
simultaneously.
3. Condition Checking (Busy Waiting)
o P0 checks:
o while (flag[1] && turn == 1);
o This means:
▪   If P1 also wants to enter (flag[1] = true)
▪ AND it is P1’s turn → P0 waits
4. Entering Critical Section
o   If the condition becomes false:
▪   Either P1 is not interested (flag[1] = false)
▪ OR it is not P1’s turn
→ P0 enters the critical section
5. Exiting Critical Section
o After execution, P0 sets:
▪   flag[0] = false
o This allows P1 to enter
🔹 Key Properties Achieved
• Mutual Exclusion
Only one process can enter the critical section at a time.
• Progress
If no process is in the critical section, one of the waiting
processes will be allowed to enter.
• Bounded Waiting
Each process gets a fair chance (due to turn variable).
********** 29 **********
--- page 30 ---
🔹 Example Scenario
• Both P0 and P1 set their flag = true at the same time
• Suppose turn = 1
→ P0 waits, P1 enters
•   After P1 exits, it sets flag[1] = false
→ Now P0 can enter
5. Explain the concept of a page fault and write the steps involved
in handling a page fault?
Page Fault – Concept
A page fault occurs in a paging-based memory management
system when a process tries to access a page that is not
currently present in main memory (RAM) but is available on
secondary storage (disk).
• Each process has a page table with a valid/invalid bit
•   If the bit is invalid, it indicates the page is not in memory
→ This triggers a page fault trap to the operating system
Working of Page Fault (Conceptual View)
********** 30 **********
--- page 31 ---
Steps Involved in Handling a Page Fault
1. Page Access Attempt
o CPU generates a logical address
o Page table is checked for validity
2. Page Fault Detection
o   If the valid bit = 0 (invalid)
→ Hardware triggers a page fault interrupt (trap) to OS
3. Check Validity of Reference
o OS verifies whether the reference is:
▪ Legal (valid page but not in memory) →
proceed
▪   Illegal (invalid access) → terminate process
********** 31 **********

[Text in pictures on this page, read by OCR]
page is on
backing store

operating
system ®
reference
@ trap
load M 4 li
restart | page table
instruction
free frame
reset page bring in
table missing page
physical

memory
--- page 32 ---
4. Locate the Required Page on Disk
o OS finds the required page in secondary storage
(backing store)
5. Find a Free Frame
o   If a free frame is available → use it
o Otherwise → apply a page replacement algorithm (e.g.,
FIFO, LRU)
6. Swap Out (if required)
o   If the selected frame contains a modified page
→ write it back to disk
7. Load Required Page into Memory
o Read the required page from disk into the selected frame
8. Update Page Table
o Set valid bit = 1
o Update frame number for the page
9. Restart the Instruction
o The interrupted instruction is restarted
o This time, execution proceeds successfully
5.Define a file in an operating system. Explain the different types of
files.
Definition of a File in Operating System
A file is a collection of related information stored on secondary
storage (such as a disk), identified by a name, and treated as a
single unit by the operating system.
•   It can store data, programs, or any form of information
•   Files provide a way to store, retrieve, and manage data
permanently
• Each file has attributes such as name, type, size, location, and
permissions
Conceptual View of File System
********** 32 **********
--- page 33 ---
directory directory

file file file

Structures of Directory in Operating System
Two Level ale Root
Master Directory (ESI

Directory J T 3
User fiw file File MMgrm File | File
Directory faivtag Entry Entry Meaney Entry Entry
Files

rhe ats

Ul Suz U3 Files

D3 D4" D5 wm

Directory Single Level Directory

Directory ye methods,txt) os.docx 2.mp4_JTP.txt
Files

D9 DIO
Files
@stop
root | spell bin programs|
stat | mail | dist find | count| hex |reorder e mail
prog | copy | prt exp reorder| list find hex | count

ooo Lf

list obj | spell all last | first

666666

FR ICR QQ I OH
--- page 34 ---
Different Types of Files
Operating systems classify files based on their structure and
purpose:
1. Regular Files (Ordinary Files)
• Contain user data such as text, images, programs, etc.
• Can be text files or binary files
• Examples: .txt, .doc, .exe, .jpg
2. Directory Files
•   Store information about files and subdirectories
• Help in organizing files in a hierarchical structure
• Example: folders in Windows/Linux
3. Special Files (Device Files)
• Represent hardware devices
• Used for input/output operations
• Two types:
o Character Special Files → data handled as a stream
(keyboard, mouse)
o Block Special Files → data handled in blocks (hard disk)
4. FIFO (Named Pipe) Files
• Used for inter-process communication (IPC)
• Data flows in a first-in, first-out manner
5. Symbolic Link Files
• Act as a pointer/reference to another file
• Do not contain actual data, only the path of the original file
********** 34 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 1b478c5e9ac1

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CyberSecurity_7010/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 Jul 2026
- Text: mixed (34 pages), mean OCR confidence 74.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech
(IT)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 14 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 34 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   1. Define Operating System & Objectives
An Operating System (OS) is system software that acts as an interface
between the user and the computer hardware. It manages hardware
resources and provides services for application programs, ensuring
efficient and convenient system operation.
Objectives of a modern Operating System:
CO- 1;   1. Convenience: Makes the computer system easy to use.
SO-2 ;
2. Efficiency: Ensures optimal use of hardware resources like CPU,
BL-2
memory, and I/O devices.
3. Ability to Evolve: Allows the system to be updated with new
features and improvements.
4. Resource Management: Efficiently allocates and manages
system resources among processes.
b.   2. Process Control Block (PCB) and its Components
A Process Control Block (PCB) is a data structure used by the operating
CO-2 ;
SO-2 ;   system to store all relevant information about a process. It is essential for
BL-2   process management and context switching.
Components of PCB:
********** 1 **********
--- page 2 ---
• Process ID (PID): Unique identifier assigned to each process.
• Process State: Indicates whether the process is new, ready,
running, waiting, or terminated.
• Program Counter: Stores the address of the next instruction to
be executed.
• CPU Registers: Holds the values of CPU registers for the
process.
• Memory Management Information: Includes details like page
tables, base and limit registers.
• I/O Status Information: Contains information about I/O devices
allocated to the process.
• Accounting Information: Tracks CPU usage, execution time,
and other statistics.
c.   3. Conditions for Critical Section Problem
To ensure correct and fair access to shared resources, a solution to the
CO-3 ;   critical section problem must satisfy the following conditions:
SO-2 ;   1. Mutual Exclusion: Only one process can execute in the critical
BL-2
and BL-3   section at any given time.
2. Progress: If no process is in the critical section, the selection of
the next process cannot be postponed indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
Process ID

Process state

Process priority

Accounting information

Program counter

CPU registers

PCB pointers

List of open files

Process I/O status information
--- page 3 ---
3. Bounded Waiting: There must be a limit on how many times
other processes can enter the critical section before a waiting
process gets its turn
d.   Necessary Conditions for Deadlock
Deadlock can occur only if all the following four conditions hold
simultaneously:
1. Mutual Exclusion: At least one resource must be held in a non-
shareable mode.
2. Hold and Wait: A process holding at least one resource is waiting
CO-3 ;
SO-2 ;   to acquire additional resources.
BL-2   3. No Preemption: Resources cannot be forcibly taken from a
process; they must be released voluntarily.
4. Circular Wait: A circular chain of processes exists where each
process is waiting for a resource held by another process in the
chain.
a. SRTF (Preemptive SJF)
Gantt Chart
0 1 5 7 11 16
| P2 | P3 | P0 | P1 | P2 |
Completion Time (CT)
• P2 = 16
• P3 = 5
Q2   • P1 = 11
CO-2;   • P0 = 7
[20]
SO-2;   Turnaround Time (TAT = CT – AT)
BL-3
and BL-4   • P2 = 16 – 0 = 16
• P3 = 5 – 1 = 4
• P1 = 11 – 2 = 9
• P0 = 7 – 3 = 4
Waiting Time (WT = TAT – BT)
• P2 = 16 – 6 = 10
• P3 = 4 – 4 = 0
• P1 = 9 – 4 = 5
********** 3 **********
--- page 4 ---
• P0 = 4 – 2 = 2
Average Times
• Average Waiting Time = (10 + 0 + 5 + 2) / 4 = 4.25
• Average Turnaround Time = (16 + 4 + 9 + 4) / 4 = 8.25
ii) Non-Preemptive SJF
Gantt Chart
0 6 8 12 16
| P2 | P0 | P3 | P1 |
Completion Time (CT)
• P2 = 6
• P0 = 8
• P3 = 12
• P1 = 16
Turnaround Time (TAT)
• P2 = 6 – 0 = 6
• P0 = 8 – 3 = 5
• P3 = 12 – 1 = 11
• P1 = 16 – 2 = 14
Waiting Time (WT)
• P2 = 6 – 6 = 0
• P0 = 5 – 2 = 3
• P3 = 11 – 4 = 7
• P1 = 14 – 4 = 10
Average Times
• Average Waiting Time = (0 + 3 + 7 + 10) / 4 = 5
• Average Turnaround Time = (6 + 5 + 11 + 14) / 4 = 9
iii) Comparison (2 Marks)
• SRTF (Preemptive SJF) gives better performance with:
o Lower Average Waiting Time (4.25 < 5)
o Lower Average Turnaround Time (8.25 < 9)
• This is because shorter processes get CPU earlier due to
preemption.
• However, SRTF is more complex and may cause frequent
context switching.
********** 4 **********
--- page 5 ---
(i) What is a Semaphore? Explain its Types (3 Marks)
A semaphore is a synchronization tool used in operating systems to
control access to shared resources by multiple processes or threads.
It is essentially an integer variable that is accessed only through two
atomic operations: wait() and signal().
Types of Semaphores:
Binary Semaphore (Mutex)
Takes only two values: 0 or 1
Used for mutual exclusion (only one process can access the critical
section at a time)
Example:
A printer shared by multiple processes
If semaphore = 1 → resource is free
If semaphore = 0 → resource is busy
Counting Semaphore
Can take non-negative integer values (0, 1, 2, …)
Used when multiple instances of a resource are available
Example:
A system with 3 identical printers → semaphore initialized to 3
Each process decreases count when using a printer and increases
after releasing
(ii) Semaphore Implementation Using Busy Waiting (4 Marks)
In busy waiting, a process continuously checks (loops) until the
semaphore becomes available.
Operations:
wait(S) {
while (S <= 0);   // busy waiting (spin lock)
S--;
}
signal(S) {
********** 5 **********
--- page 6 ---
S++;
}
Explanation:
•   wait(S):
o Checks if S > 0
o   If not, it keeps checking repeatedly (CPU is busy)
o When S > 0, it decrements S and enters the critical
section
•   signal(S):
o Increments the semaphore value
o Indicates that the resource is released
Drawback:
• CPU cycles are wasted while waiting
•   Inefficient for long waiting periods
(iii) Semaphore Without Busy Waiting (4 Marks)
To avoid wasting CPU time, semaphores can be implemented using
blocking (sleep) and wakeup mechanisms.
Operations:
wait(S) {
S--;
if (S < 0) {
add process to queue;
block();   // process goes to sleep
}
}
signal(S) {
S++;
if (S <= 0) {
remove process from queue;
wakeup(process);
}
}
Explanation:
wait(S):
********** 6 **********
--- page 7 ---
If resource not available → process is blocked
It is placed in a waiting queue
signal(S):
Wakes up one waiting process from the queue
Advantages:
No CPU wastage (no spinning)
Better CPU utilization
Efficient for systems with many processes
i   Readers–Writers Problem
The Readers–Writers problem is a classic synchronization problem in
operating systems that deals with managing access to a shared
resource (like a file or database).
• Readers → only read the data (do not modify)
• Writers → modify the data
Key Requirement:
• Multiple readers can access the resource simultaneously
• Only one writer can access the resource exclusively
• No reader should read while a writer is writing
Q3
Types of Readers–Writers Problems
CO-2;
1. Reader Priority → Readers are not blocked unless a writer is   [20]
SO-2;
BL-3 and   already writing
BL-4
2. Writer Priority → Writers get priority (avoid starvation)
3. Fair Solution → No starvation for either
(Below is the standard Reader-Priority solution using semaphores)
Semaphore-Based Solution
Initialization:
semaphore mutex = 1;   // protects readCount
semaphore wrt = 1;   // controls access to shared resource
int readCount = 0;   // number of active readers
Reader Process
********** 7 **********
--- page 8 ---
wait(mutex);
readCount++;
if (readCount == 1)
wait(wrt);   // first reader blocks writers
signal(mutex);
// Reading is performed
wait(mutex);
readCount--;
if (readCount == 0)
signal(wrt); // last reader releases writer
signal(mutex);
Writer Process
wait(wrt);
// Writing is performed
signal(wrt);
How the Solution Works
1. Handling Multiple Readers
• The variable readCount keeps track of active readers
•   First reader locks the resource using wait(wrt)
• Subsequent readers:
o Do NOT block
o Can read simultaneously
• Hence, multiple readers are allowed concurrently
2. Handling Single Writer
• Writer uses wait(wrt)
•   If:
o Any reader is active OR
********** 8 **********
--- page 9 ---
o Another writer is active
→ writer must wait
• Ensures only one writer at a time
3. Mutual Exclusion Logic
• mutex protects updates to readCount
• wrt ensures:
o No writer enters when readers are present
o No readers enter when a writer is active
Key Advantages
•   Efficient for read-heavy systems
• Allows maximum concurrency for readers
Limitation
•   Writers may suffer from starvation
(continuous arrival of readers may delay writers indefinitely)
Conclusion
• The semaphore-based solution ensures:
o Concurrent access for readers
o Exclusive access for writers
• Achieves synchronization using:
o mutex → protects shared variable
o wrt → controls resource access.
Here is the descriptive answer (without bullets, exam-ready format):
a) Round Robin Scheduling (Time Quantum = 3 ms)
All processes arrive at time 0 ms, so scheduling starts in the order P1,
P2, P3, and P4.
Gantt Chart
0 3 6 9 12 14 17 18 21 23 24
********** 9 **********
--- page 10 ---
| P1 | P2 | P3 | P4 | P1 | P2 | P3 | P4 | P2 | P4 |
Completion Times
P3 completes at 18 ms, P1 at 14 ms, P2 at 23 ms, and P4 at 24 ms.
Turnaround Time (TAT = CT – AT)
Since all arrival times are 0:
P1 = 14, P2 = 23, P3 = 18, P4 = 24
Waiting Time (WT = TAT – BT)
P1 = 14 – 5 = 9
P2 = 23 – 7 = 16
P3 = 18 – 4 = 14
P4 = 24 – 6 = 18
Average Values
Average Waiting Time = (9 + 16 + 14 + 18) / 4 = 14.25 ms
Average Turnaround Time = (14 + 23 + 18 + 24) / 4 = 19.75 ms
b) First Come First Serve (FCFS)
Since all processes arrive at the same time, execution follows the order
P1, P2, P3, P4.
Gantt Chart
0 5 12 16 22
| P1 | P2 | P3 | P4 |
Completion Times
P1 = 5, P2 = 12, P3 = 16, P4 = 22
Turnaround Time
P1 = 5, P2 = 12, P3 = 16, P4 = 22
Waiting Time
P1 = 0
P2 = 5
P3 = 12
P4 = 16
Average Values
Average Waiting Time = (0 + 5 + 12 + 16) / 4 = 8.25 ms
Average Turnaround Time = (5 + 12 + 16 + 22) / 4 = 13.75 ms
c) Comparison of Round Robin and FCFS
********** 10 **********
--- page 11 ---
From the results, it is observed that FCFS provides lower average
waiting time and turnaround time compared to Round Robin in this
case. This is because all processes arrive at the same time and shorter
processes are not delayed by time slicing.
Round Robin, on the other hand, ensures fairness by giving equal CPU
time to each process, but it increases waiting time due to frequent
context switching. Therefore, FCFS performs better for this specific
scenario, while Round Robin is more suitable for time-sharing systems
where responsiveness is important.
If you want, I can also give this in step-wise solving format (for
students to follow easily in exams) or convert it into a Word
document.
Deadlock is a situation in an operating system where a set of processes
are permanently blocked because each process is waiting for a resource
that is held by another process in the same set. As a result, none of the
processes can proceed, and the system gets stuck in a circular waiting
state. A common real-life analogy is two people each holding one
resource and waiting for the other to release theirs—neither moves
forward.
For a deadlock to occur, four necessary conditions must hold
Q4   simultaneously. The first is mutual exclusion, meaning at least one
CO-2;   resource must be non-shareable; only one process can use it at a time.
SO-2;   [20]
BL-3   The second is hold and wait, where a process holding at least one
and BL-4   resource is waiting to acquire additional resources held by other
processes. The third is no preemption, which implies that resources
cannot be forcibly taken away from a process; they must be released
voluntarily. The fourth is circular wait, where a circular chain of
processes exists such that each process is waiting for a resource held by
the next process in the cycle. If any one of these conditions is
prevented, deadlock cannot occur.
Operating systems use different techniques to handle deadlock, broadly
classified as prevention, detection, and recovery.
********** 11 **********
--- page 12 ---
In deadlock prevention, the system is designed in such a way that at
least one of the four necessary conditions is never allowed to occur. For
example, mutual exclusion can be reduced by making resources
sharable where possible, though this is not always practical. The hold-
and-wait condition can be avoided by requiring processes to request all
needed resources at once before execution begins, or by forcing them to
release currently held resources before requesting new ones. The no-
preemption condition can be handled by allowing the system to take
resources away from a process if it requests additional ones and cannot
be satisfied immediately. Circular wait can be prevented by imposing a
strict ordering on resource types and requiring processes to request
resources in that order. While prevention guarantees that deadlocks
never occur, it often leads to poor resource utilization and reduced
system efficiency.
In deadlock detection, the system allows deadlocks to occur but
periodically checks whether they have happened. This is typically done
using structures like a resource allocation graph or matrix-based
algorithms. If the system has only single instances of resources, a cycle
in the graph indicates deadlock. For multiple instances, more complex
detection algorithms similar to the Banker’s algorithm are used.
Detection is suitable for systems where deadlocks are rare, as it avoids
the overhead of strict prevention but requires additional computation to
monitor system state.
Once a deadlock is detected, the system must apply recovery
techniques to break the deadlock. One approach is process
termination, where one or more processes involved in the deadlock are
aborted. This can be done either by terminating all deadlocked
processes or by selecting processes one by one until the cycle is broken.
Another approach is resource preemption, where resources are taken
away from certain processes and given to others until the deadlock is
resolved. This requires careful handling to avoid inconsistencies, and
processes may need to be rolled back to a safe state before execution
resumes.
In summary, deadlock is a critical issue in resource management where
processes block each other indefinitely. The four necessary conditions
********** 12 **********
--- page 13 ---
define its occurrence, and operating systems handle it either by
preventing it altogether, detecting it after occurrence, or recovering
from it. Each approach involves trade-offs between system
performance, complexity, and resource utilization.
Here is the exam-style solution with proper columns (3 frames):
FIFO Page Replacement
Re Frame Frame Frame Page
f   1   2   3   Fault
5   5   -   -   Yes
0   5   0   -   Yes
1   5   0   1   Yes
0   5   0   1   No
2   2   0   1   Yes
3   2   3   1   Yes
0   2   3   0   Yes
2   2   3   0   No
4   4   3   0   Yes
3   4   3   0   No
3   4   3   0   No
2   4   2   0   Yes
0   4   2   0   No
2   4   2   0   No
1   1   2   0   Yes
2   1   2   0   No
7   1   7   0   Yes
0   1   7   0   No
1   1   7   0   No
1   1   7   0   No
********** 13 **********
--- page 14 ---
0   1   7   0   No
Total Page Faults (FIFO) = 15
LRU Page Replacement
Re Frame Frame Frame Page
f   1   2   3   Fault
5   5   -   -   Yes
0   5   0   -   Yes
1   5   0   1   Yes
0   5   0   1   No
2   2   0   1   Yes
3   2   3   1   Yes
0   2   3   0   Yes
2   2   3   0   No
4   4   3   0   Yes
3   4   3   0   No
3   4   3   0   No
2   4   3   2   Yes
0   0   3   2   Yes
2   0   3   2   No
1   0   1   2   Yes
2   0   1   2   No
7   7   1   2   Yes
0   7   0   2   Yes
1   7   0   1   Yes
1   7   0   1   No
0   7   0   1   No
Total Page Faults (LRU) = 12
Optimal Page Replacement
********** 14 **********
--- page 15 ---
Re Frame Frame Frame Page
f   1   2   3   Fault
5   5   -   -   Yes
0   5   0   -   Yes
1   5   0   1   Yes
0   5   0   1   No
2   2   0   1   Yes
3   2   0   3   Yes
0   2   0   3   No
2   2   0   3   No
4   2   4   3   Yes
3   2   4   3   No
3   2   4   3   No
2   2   4   3   No
0   2   0   3   Yes
2   2   0   3   No
1   2   0   1   Yes
2   2   0   1   No
7   2   0   7   Yes
0   2   0   7   No
1   1   0   7   Yes
1   1   0   7   No
0   1   0   7   No
Total Page Faults (Optimal) = 9
Final Conclusion
Optimal algorithm gives the minimum page faults, followed by LRU
and then FIFO. Therefore, Optimal is the best, while LRU is the best
practical approach.
********** 15 **********
--- page 16 ---
Here is the proper step-by-step exam solution (Banker’s Algorithm):
Step 1: Given Data
Allocation Matrix
P0 → (1 0 2 1)
P1 → (0 1 1 0)
P2 → (1 2 0 1)
P3 → (0 0 1 2)
Max Matrix
P0 → (3 2 2 2)
P1 → (1 3 3 1)
P2 → (2 4 1 2)
P3 → (1 2 2 3)
Available = (2 1 0 1)
i) Need Matrix Calculation
Q5
Need = Max – Allocation
CO-2;
P0 → (3−1, 2−0, 2−2, 2−1) = (2 2 0 1)
SO-2;   [20]
BL-3   P1 → (1−0, 3−1, 3−1, 1−0) = (1 2 2 1)
and BL-4   P2 → (2−1, 4−2, 1−0, 2−1) = (1 2 1 1)
P3 → (1−0, 2−0, 2−1, 3−2) = (1 2 1 1)
ii) Check Safe State
Initial Available = (2 1 0 1)
Now compare Need ≤ Available:
P0 → (2 2 0 1) ✗ (B not satisfied)
P1 → (1 2 2 1) ✗
P2 → (1 2 1 1) ✗
P3 → (1 2 1 1) ✗
No process can proceed since no Need is ≤ Available.
Conclusion
The system is NOT in a safe state because no process can execute first.
Hence, no safe sequence exists.
********** 16 **********
--- page 17 ---
iii) Request from P3 = (0 1 0 1)
Step 1: Check Request ≤ Need
P3 Need = (1 2 1 1)
Request = (0 1 0 1) → satisfies condition ✓
Step 2: Check Request ≤ Available
Available = (2 1 0 1)
Request = (0 1 0 1) → satisfies condition ✓
Step 3: Allocate Temporarily
New Available = (2 1 0 1) − (0 1 0 1) = (2 0 0 0)
New Allocation of P3 = (0 1 1 3)
New Need of P3 = (1 1 1 0)
Step 4: Check Safe State Again
Available = (2 0 0 0)
P0 → (2 2 0 1) ✗
P1 → (1 2 2 1) ✗
P2 → (1 2 1 1) ✗
P3 → (1 1 1 0) ✗
Again, no process can proceed.
Final Conclusion
The system is not in a safe state initially, and even after granting the
request, it remains unsafe. Therefore, the request cannot be granted
immediately.
********** 17 **********
--- page 18 ---
How Segmentation Overcomes Limitations of Paging
Paging divides memory into fixed-size blocks (pages/frames), which
simplifies allocation but introduces some limitations. Segmentation
addresses these issues as follows:
•   In paging, programs are divided into fixed-size pages without
considering the logical structure of a program. This makes it
difficult for programmers to relate memory to program
components. Segmentation, on the other hand, divides memory
based on logical units such as functions, arrays, stacks, and
modules, making it more meaningful and programmer-friendly.
• Paging suffers from internal fragmentation because memory is
allocated in fixed sizes, leading to unused space within a page.
********** 18 **********

[Text in pictures on this page, read by OCR]
os

Offset
< Limit

CPU Segment | Offset
Number

Logical Address

| | 1500 so

Base Limit
1800 a
|o] 1500 200
1 1800 100
= 2000
2] 2000 | 150 + 82
3| 2400 100
Segment Table 2400 $3
Main Memory

Segmentation

Paging

Logical Physical
Address Address
| 10000..00
cpu |—>| Plid t Il d | Physical

Memory

11111..11

"{

L_, f

Page table
--- page 19 ---
Segmentation eliminates internal fragmentation since segments
are of variable size, matching the actual size of program
components.
• Paging does not support logical protection and sharing
effectively at a high level. Segmentation enables protection and
sharing at segment level, allowing different processes to share
specific segments like libraries while keeping others private.
•   In paging, debugging and maintenance become difficult because
memory is not organized logically. Segmentation improves this
by maintaining a clear mapping between logical program
structure and memory layout.
However, segmentation may introduce external fragmentation, which
paging avoids—so both techniques have trade-offs.
Here is the proper exam solution with step-by-step calculation:
Given:
Request Queue: 98, 183, 37, 122, 14, 124, 65, 67
Initial Head Position = 53
i) FCFS (First Come First Serve)
In FCFS, requests are served in the order they arrive.
Sequence:
Q6
53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67
CO-3;
SO-2;   Head Movements:   [20]
BL-2
Movemen Distanc
and BL-4
t   e
53 → 98 45
98 → 183 85
183 → 37 146
37 → 122 85
122 → 14 108
14 → 124 110
124 → 65 59
********** 19 **********
--- page 20 ---
65 → 67 2
Total Head Movement:
45 + 85 + 146 + 85 + 108 + 110 + 59 + 2 = 640 tracks
ii) SSTF (Shortest Seek Time First)
In SSTF, the closest request to the current head position is serviced
first.
Step-wise Selection:
From 53 → nearest is 65
From 65 → nearest is 67
From 67 → nearest is 37
From 37 → nearest is 14
From 14 → nearest is 98
From 98 → nearest is 122
From 122 → nearest is 124
From 124 → nearest is 183
Sequence:
53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183
Head Movements:
Movemen Distanc
t   e
53 → 65 12
65 → 67 2
67 → 37 30
37 → 14 23
14 → 98 84
98 → 122 24
122 →
2
124
124 →
59
183
Total Head Movement:
12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = 236 tracks
********** 20 **********
--- page 21 ---
Final Answer
FCFS total head movement = 640 tracks
SSTF total head movement = 236 tracks
Conclusion
SSTF performs better than FCFS because it minimizes the seek time by
selecting the nearest request, resulting in significantly lower head
movement.
File Management in Operating System
********** 21 **********
--- page 22 ---
Concept of File Management
File management is a fundamental function of an operating system that
deals with the creation, organization, storage, retrieval, and
protection of files on secondary storage devices such as disks.
A file is a collection of related data stored on a storage device and
treated as a single unit by the OS. The operating system provides an
abstraction so users do not need to know how data is physically stored.
The OS is responsible for:
• Creating and deleting files
• Reading and writing data
• Managing directories (folders)
•   Controlling access permissions (security)
•   Allocating disk space efficiently
• Maintaining file metadata (size, type, location, timestamps)
Thus, file management ensures efficient, reliable, and secure data
storage and access.
File Organization Methods
File organization refers to how records within a file are arranged for
storage and retrieval.
1. Sequential File Organization
********** 22 **********

[Text in pictures on this page, read by OCR]
Comparison of File Designs

Sequential Direct-Access Indexed-Sequential
Types of Access batch online batch or online
Data Organization sequentially no particular sequentially and by
by key value order index
Flexibility in low high very high
Handling Inquiries
Availability of no yes yes
Up-to-Date Data
Speed of Retrieval slow very fast fast
Activity high low high
Volatility low high high
Examples payroll airline customer ordering
processing reservations and billing
and billing and banking

operations transactions
--- page 23 ---
• Data is stored in order (record by record)
• Access is done sequentially from beginning to end
•   Suitable for applications like logs or reports
Advantage: Simple and efficient for large batch processing
Limitation: Slow for random access
2. Direct (Random) File Organization
• Records are accessed directly using an address or key
• No need to read previous records
Advantage: Fast access to any record
Limitation: Requires calculation of address (hashing or indexing)
3. Indexed File Organization
• Uses an index table that stores keys and their corresponding
addresses
• Combines benefits of sequential and direct access
Advantage: Efficient searching and retrieval
Limitation: Extra storage required for index
File Storage Methods (Allocation Techniques)
File storage refers to how files are physically placed on disk blocks.
1. Contiguous Allocation
•   File occupies continuous blocks on disk
Advantages:
•   Fast access (both sequential and direct)
• Simple implementation
Disadvantages:
•   External fragmentation
•   Difficult to expand file size
2. Linked Allocation
•   File is stored as a linked list of blocks scattered across disk
• Each block points to the next
Advantages:
• No external fragmentation
********** 23 **********
--- page 24 ---
• Easy file growth
Disadvantages:
• Slow random access
•   Pointer overhead
3. Indexed Allocation
• A separate index block contains addresses of all file blocks
Advantages:
• Supports direct access
• No external fragmentation
Disadvantages:
• Extra space for index block
• Overhead for small files
How Files Are Stored and Accessed
Files are stored on disk as a collection of blocks. The OS maintains
metadata (via structures like file control blocks or inodes) that store:
•   File name, size, permissions
• Location of blocks on disk
When a user accesses a file:
1. The OS searches the directory structure to locate the file
2. Retrieves metadata (block addresses)
3. Uses the allocation method (contiguous/linked/indexed)
4. Reads or writes data from/to disk
Access methods include:
• Sequential access → read/write in order
• Direct access → jump to specific location
• Indexed access → use index for faster retrieval
Conclusion
File management in an OS ensures structured storage, efficient retrieval,
and secure handling of data. Different file organization and allocation
methods are used depending on system requirements, balancing
performance, flexibility, and storage efficiency.
********** 24 **********
--- page 25 ---
Select any 4 only.
1. Explain any two Operating System Services.
Operating System Services (Any Two)
1. Program Execution
Program execution is a core service of an operating system that
enables users to run application programs. The OS loads the
program from secondary storage into main memory, creates a
process, and begins execution. It allocates required resources
such as CPU time, memory, and I/O devices, and manages the
entire lifecycle of the program—from initiation to termination. It
also handles abnormal termination in case of errors, ensuring
smooth and controlled execution.
2. I/O Operations
Q7
The operating system provides a standardized interface for input
CO-
and output operations. Instead of interacting directly with
1,CO2
and CO-   hardware devices like keyboards, disks, or printers, users and   [20]
3; SO-2;
applications communicate through the OS. The OS manages
BL-2
device drivers, buffering, caching, and scheduling of I/O
and BL-3
requests to improve efficiency. It also detects and handles errors,
ensuring reliable communication between software and
hardware.
2. Define single-threaded and multi-threaded processes.
Single-Threaded and Multi-Threaded Processes
A process is a program in execution, and it may contain one or
more threads, which are the basic units of CPU execution.
Single-Threaded Process
A single-threaded process contains only one thread of
execution. This means the process performs one task at a time,
following a single sequence of instructions. If the thread is
blocked (for example, waiting for I/O), the entire process is also
blocked.
********** 25 **********
--- page 26 ---
Example: A simple calculator program that performs one
operation at a time.
Multi-Threaded Process
A multi-threaded process contains multiple threads within the
same process, all sharing the same memory space and resources.
These threads can execute concurrently, allowing the process to
perform multiple tasks simultaneously.
Example: A web browser where one thread handles user
interaction, another loads web pages, and another manages
background tasks.
Key Difference
Single-threaded → one task at a time, simpler but slower
Multi-threaded → multiple tasks concurrently, more efficient but
complex to manage.
3. What are the symbols used in a Resource Allocation Graph
(RAG)? Explain with a small example.
Symbols used in Resource Allocation Graph (RAG)
A Resource Allocation Graph (RAG) is a directed graph used to
represent the allocation of resources to processes and to detect
deadlocks in a system.
The main symbols used in a RAG are as follows:
A process is represented by a circle (○). Each circle denotes a process
such as P1, P2, etc.
A resource type is represented by a rectangle (□). If a resource has
multiple instances, it is shown by multiple dots inside the rectangle.
A request edge is represented by a directed arrow from a process to a
resource (P → R). This indicates that the process is requesting that
resource.
An assignment edge is represented by a directed arrow from a
resource to a process (R → P). This indicates that the resource has
been allocated to that process.
Small Example
********** 26 **********
--- page 27 ---
Consider two processes P1 and P2, and two resources R1 and R2.
Process P1 is holding resource R1 and requesting resource R2. At the
same time, process P2 is holding resource R2 and requesting resource
R1.
********** 27 **********
--- page 28 ---
This situation can be represented using a Resource Allocation Graph
where there is an assignment edge from R1 to P1 and from R2 to P2,
and request edges from P1 to R2 and from P2 to R1.
Such a graph forms a cycle, which indicates the possibility of a
deadlock when each resource has a single instance.
4. Explain the working of Peterson’s Solution using shared
variables (flag and turn).
Peterson’s Solution is a classical software-based solution to the
critical section problem for two processes. It ensures mutual
exclusion, progress, and bounded waiting using two shared
variables:
•   flag[2] → indicates if a process wants to enter the critical section
•   turn → indicates whose turn it is to enter
🔹 Shared Variables
boolean flag[2];   // initially flag[0] = flag[1] = false
int turn;
🔹 Structure for Process Pi (i = 0 or 1)
do {
flag[i] = true;   // Process Pi wants to enter
turn = j;   // Give chance to other process
while (flag[j] && turn == j);   // Wait if Pj wants to enter and
it's Pj's turn
// Critical Section
flag[i] = false;   // Exit section
// Remainder Section
} while (true);
(where j = 1 - i)
********** 28 **********
--- page 29 ---
🔹 Working Explanation
Consider two processes P0 and P1:
1. Desire to Enter Critical Section
o When a process (say P0) wants to enter, it sets:
▪   flag[0] = true
o This indicates interest in entering the critical section.
2. Turn Assignment
o P0 sets turn = 1 (gives priority to P1).
o This ensures fairness if both processes request
simultaneously.
3. Condition Checking (Busy Waiting)
o P0 checks:
o while (flag[1] && turn == 1);
o This means:
▪   If P1 also wants to enter (flag[1] = true)
▪ AND it is P1’s turn → P0 waits
4. Entering Critical Section
o   If the condition becomes false:
▪   Either P1 is not interested (flag[1] = false)
▪ OR it is not P1’s turn
→ P0 enters the critical section
5. Exiting Critical Section
o After execution, P0 sets:
▪   flag[0] = false
o This allows P1 to enter
🔹 Key Properties Achieved
• Mutual Exclusion
Only one process can enter the critical section at a time.
• Progress
If no process is in the critical section, one of the waiting
processes will be allowed to enter.
• Bounded Waiting
Each process gets a fair chance (due to turn variable).
********** 29 **********
--- page 30 ---
🔹 Example Scenario
• Both P0 and P1 set their flag = true at the same time
• Suppose turn = 1
→ P0 waits, P1 enters
•   After P1 exits, it sets flag[1] = false
→ Now P0 can enter
5. Explain the concept of a page fault and write the steps involved
in handling a page fault?
Page Fault – Concept
A page fault occurs in a paging-based memory management
system when a process tries to access a page that is not
currently present in main memory (RAM) but is available on
secondary storage (disk).
• Each process has a page table with a valid/invalid bit
•   If the bit is invalid, it indicates the page is not in memory
→ This triggers a page fault trap to the operating system
Working of Page Fault (Conceptual View)
********** 30 **********
--- page 31 ---
Steps Involved in Handling a Page Fault
1. Page Access Attempt
o CPU generates a logical address
o Page table is checked for validity
2. Page Fault Detection
o   If the valid bit = 0 (invalid)
→ Hardware triggers a page fault interrupt (trap) to OS
3. Check Validity of Reference
o OS verifies whether the reference is:
▪ Legal (valid page but not in memory) →
proceed
▪   Illegal (invalid access) → terminate process
********** 31 **********

[Text in pictures on this page, read by OCR]
page is on
backing store

operating
system ®
reference
@ trap
load M 4 li
restart | page table
instruction
free frame
reset page bring in
table missing page
physical

memory
--- page 32 ---
4. Locate the Required Page on Disk
o OS finds the required page in secondary storage
(backing store)
5. Find a Free Frame
o   If a free frame is available → use it
o Otherwise → apply a page replacement algorithm (e.g.,
FIFO, LRU)
6. Swap Out (if required)
o   If the selected frame contains a modified page
→ write it back to disk
7. Load Required Page into Memory
o Read the required page from disk into the selected frame
8. Update Page Table
o Set valid bit = 1
o Update frame number for the page
9. Restart the Instruction
o The interrupted instruction is restarted
o This time, execution proceeds successfully
5.Define a file in an operating system. Explain the different types of
files.
Definition of a File in Operating System
A file is a collection of related information stored on secondary
storage (such as a disk), identified by a name, and treated as a
single unit by the operating system.
•   It can store data, programs, or any form of information
•   Files provide a way to store, retrieve, and manage data
permanently
• Each file has attributes such as name, type, size, location, and
permissions
Conceptual View of File System
********** 32 **********
--- page 33 ---
directory directory

file file file

Structures of Directory in Operating System
Two Level ale Root
Master Directory (ESI

Directory J T 3
User fiw file File MMgrm File | File
Directory faivtag Entry Entry Meaney Entry Entry
Files

rhe ats

Ul Suz U3 Files

D3 D4" D5 wm

Directory Single Level Directory

Directory ye methods,txt) os.docx 2.mp4_JTP.txt
Files

D9 DIO
Files
@stop
root | spell bin programs|
stat | mail | dist find | count| hex |reorder e mail
prog | copy | prt exp reorder| list find hex | count

ooo Lf

list obj | spell all last | first

666666

FR ICR QQ I OH
--- page 34 ---
Different Types of Files
Operating systems classify files based on their structure and
purpose:
1. Regular Files (Ordinary Files)
• Contain user data such as text, images, programs, etc.
• Can be text files or binary files
• Examples: .txt, .doc, .exe, .jpg
2. Directory Files
•   Store information about files and subdirectories
• Help in organizing files in a hierarchical structure
• Example: folders in Windows/Linux
3. Special Files (Device Files)
• Represent hardware devices
• Used for input/output operations
• Two types:
o Character Special Files → data handled as a stream
(keyboard, mouse)
o Block Special Files → data handled in blocks (hard disk)
4. FIFO (Named Pipe) Files
• Used for inter-process communication (IPC)
• Data flows in a first-in, first-out manner
5. Symbolic Link Files
• Act as a pointer/reference to another file
• Do not contain actual data, only the path of the original file
********** 34 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 2a44d4f4d39f

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_IT_7001/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 Jul 2026
- Text: mixed (34 pages), mean OCR confidence 74.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech
(IT)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 14 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 34 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   1. Define Operating System & Objectives
An Operating System (OS) is system software that acts as an interface
between the user and the computer hardware. It manages hardware
resources and provides services for application programs, ensuring
efficient and convenient system operation.
Objectives of a modern Operating System:
CO- 1;   1. Convenience: Makes the computer system easy to use.
SO-2 ;
2. Efficiency: Ensures optimal use of hardware resources like CPU,
BL-2
memory, and I/O devices.
3. Ability to Evolve: Allows the system to be updated with new
features and improvements.
4. Resource Management: Efficiently allocates and manages
system resources among processes.
b.   2. Process Control Block (PCB) and its Components
A Process Control Block (PCB) is a data structure used by the operating
CO-2 ;
SO-2 ;   system to store all relevant information about a process. It is essential for
BL-2   process management and context switching.
Components of PCB:
********** 1 **********
--- page 2 ---
• Process ID (PID): Unique identifier assigned to each process.
• Process State: Indicates whether the process is new, ready,
running, waiting, or terminated.
• Program Counter: Stores the address of the next instruction to
be executed.
• CPU Registers: Holds the values of CPU registers for the
process.
• Memory Management Information: Includes details like page
tables, base and limit registers.
• I/O Status Information: Contains information about I/O devices
allocated to the process.
• Accounting Information: Tracks CPU usage, execution time,
and other statistics.
c.   3. Conditions for Critical Section Problem
To ensure correct and fair access to shared resources, a solution to the
CO-3 ;   critical section problem must satisfy the following conditions:
SO-2 ;   1. Mutual Exclusion: Only one process can execute in the critical
BL-2
and BL-3   section at any given time.
2. Progress: If no process is in the critical section, the selection of
the next process cannot be postponed indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
Process ID

Process state

Process priority

Accounting information

Program counter

CPU registers

PCB pointers

List of open files

Process I/O status information
--- page 3 ---
3. Bounded Waiting: There must be a limit on how many times
other processes can enter the critical section before a waiting
process gets its turn
d.   Necessary Conditions for Deadlock
Deadlock can occur only if all the following four conditions hold
simultaneously:
1. Mutual Exclusion: At least one resource must be held in a non-
shareable mode.
2. Hold and Wait: A process holding at least one resource is waiting
CO-3 ;
SO-2 ;   to acquire additional resources.
BL-2   3. No Preemption: Resources cannot be forcibly taken from a
process; they must be released voluntarily.
4. Circular Wait: A circular chain of processes exists where each
process is waiting for a resource held by another process in the
chain.
a. SRTF (Preemptive SJF)
Gantt Chart
0 1 5 7 11 16
| P2 | P3 | P0 | P1 | P2 |
Completion Time (CT)
• P2 = 16
• P3 = 5
Q2   • P1 = 11
CO-2;   • P0 = 7
[20]
SO-2;   Turnaround Time (TAT = CT – AT)
BL-3
and BL-4   • P2 = 16 – 0 = 16
• P3 = 5 – 1 = 4
• P1 = 11 – 2 = 9
• P0 = 7 – 3 = 4
Waiting Time (WT = TAT – BT)
• P2 = 16 – 6 = 10
• P3 = 4 – 4 = 0
• P1 = 9 – 4 = 5
********** 3 **********
--- page 4 ---
• P0 = 4 – 2 = 2
Average Times
• Average Waiting Time = (10 + 0 + 5 + 2) / 4 = 4.25
• Average Turnaround Time = (16 + 4 + 9 + 4) / 4 = 8.25
ii) Non-Preemptive SJF
Gantt Chart
0 6 8 12 16
| P2 | P0 | P3 | P1 |
Completion Time (CT)
• P2 = 6
• P0 = 8
• P3 = 12
• P1 = 16
Turnaround Time (TAT)
• P2 = 6 – 0 = 6
• P0 = 8 – 3 = 5
• P3 = 12 – 1 = 11
• P1 = 16 – 2 = 14
Waiting Time (WT)
• P2 = 6 – 6 = 0
• P0 = 5 – 2 = 3
• P3 = 11 – 4 = 7
• P1 = 14 – 4 = 10
Average Times
• Average Waiting Time = (0 + 3 + 7 + 10) / 4 = 5
• Average Turnaround Time = (6 + 5 + 11 + 14) / 4 = 9
iii) Comparison (2 Marks)
• SRTF (Preemptive SJF) gives better performance with:
o Lower Average Waiting Time (4.25 < 5)
o Lower Average Turnaround Time (8.25 < 9)
• This is because shorter processes get CPU earlier due to
preemption.
• However, SRTF is more complex and may cause frequent
context switching.
********** 4 **********
--- page 5 ---
(i) What is a Semaphore? Explain its Types (3 Marks)
A semaphore is a synchronization tool used in operating systems to
control access to shared resources by multiple processes or threads.
It is essentially an integer variable that is accessed only through two
atomic operations: wait() and signal().
Types of Semaphores:
Binary Semaphore (Mutex)
Takes only two values: 0 or 1
Used for mutual exclusion (only one process can access the critical
section at a time)
Example:
A printer shared by multiple processes
If semaphore = 1 → resource is free
If semaphore = 0 → resource is busy
Counting Semaphore
Can take non-negative integer values (0, 1, 2, …)
Used when multiple instances of a resource are available
Example:
A system with 3 identical printers → semaphore initialized to 3
Each process decreases count when using a printer and increases
after releasing
(ii) Semaphore Implementation Using Busy Waiting (4 Marks)
In busy waiting, a process continuously checks (loops) until the
semaphore becomes available.
Operations:
wait(S) {
while (S <= 0);   // busy waiting (spin lock)
S--;
}
signal(S) {
********** 5 **********
--- page 6 ---
S++;
}
Explanation:
•   wait(S):
o Checks if S > 0
o   If not, it keeps checking repeatedly (CPU is busy)
o When S > 0, it decrements S and enters the critical
section
•   signal(S):
o Increments the semaphore value
o Indicates that the resource is released
Drawback:
• CPU cycles are wasted while waiting
•   Inefficient for long waiting periods
(iii) Semaphore Without Busy Waiting (4 Marks)
To avoid wasting CPU time, semaphores can be implemented using
blocking (sleep) and wakeup mechanisms.
Operations:
wait(S) {
S--;
if (S < 0) {
add process to queue;
block();   // process goes to sleep
}
}
signal(S) {
S++;
if (S <= 0) {
remove process from queue;
wakeup(process);
}
}
Explanation:
wait(S):
********** 6 **********
--- page 7 ---
If resource not available → process is blocked
It is placed in a waiting queue
signal(S):
Wakes up one waiting process from the queue
Advantages:
No CPU wastage (no spinning)
Better CPU utilization
Efficient for systems with many processes
i   Readers–Writers Problem
The Readers–Writers problem is a classic synchronization problem in
operating systems that deals with managing access to a shared
resource (like a file or database).
• Readers → only read the data (do not modify)
• Writers → modify the data
Key Requirement:
• Multiple readers can access the resource simultaneously
• Only one writer can access the resource exclusively
• No reader should read while a writer is writing
Q3
Types of Readers–Writers Problems
CO-2;
1. Reader Priority → Readers are not blocked unless a writer is   [20]
SO-2;
BL-3 and   already writing
BL-4
2. Writer Priority → Writers get priority (avoid starvation)
3. Fair Solution → No starvation for either
(Below is the standard Reader-Priority solution using semaphores)
Semaphore-Based Solution
Initialization:
semaphore mutex = 1;   // protects readCount
semaphore wrt = 1;   // controls access to shared resource
int readCount = 0;   // number of active readers
Reader Process
********** 7 **********
--- page 8 ---
wait(mutex);
readCount++;
if (readCount == 1)
wait(wrt);   // first reader blocks writers
signal(mutex);
// Reading is performed
wait(mutex);
readCount--;
if (readCount == 0)
signal(wrt); // last reader releases writer
signal(mutex);
Writer Process
wait(wrt);
// Writing is performed
signal(wrt);
How the Solution Works
1. Handling Multiple Readers
• The variable readCount keeps track of active readers
•   First reader locks the resource using wait(wrt)
• Subsequent readers:
o Do NOT block
o Can read simultaneously
• Hence, multiple readers are allowed concurrently
2. Handling Single Writer
• Writer uses wait(wrt)
•   If:
o Any reader is active OR
********** 8 **********
--- page 9 ---
o Another writer is active
→ writer must wait
• Ensures only one writer at a time
3. Mutual Exclusion Logic
• mutex protects updates to readCount
• wrt ensures:
o No writer enters when readers are present
o No readers enter when a writer is active
Key Advantages
•   Efficient for read-heavy systems
• Allows maximum concurrency for readers
Limitation
•   Writers may suffer from starvation
(continuous arrival of readers may delay writers indefinitely)
Conclusion
• The semaphore-based solution ensures:
o Concurrent access for readers
o Exclusive access for writers
• Achieves synchronization using:
o mutex → protects shared variable
o wrt → controls resource access.
Here is the descriptive answer (without bullets, exam-ready format):
a) Round Robin Scheduling (Time Quantum = 3 ms)
All processes arrive at time 0 ms, so scheduling starts in the order P1,
P2, P3, and P4.
Gantt Chart
0 3 6 9 12 14 17 18 21 23 24
********** 9 **********
--- page 10 ---
| P1 | P2 | P3 | P4 | P1 | P2 | P3 | P4 | P2 | P4 |
Completion Times
P3 completes at 18 ms, P1 at 14 ms, P2 at 23 ms, and P4 at 24 ms.
Turnaround Time (TAT = CT – AT)
Since all arrival times are 0:
P1 = 14, P2 = 23, P3 = 18, P4 = 24
Waiting Time (WT = TAT – BT)
P1 = 14 – 5 = 9
P2 = 23 – 7 = 16
P3 = 18 – 4 = 14
P4 = 24 – 6 = 18
Average Values
Average Waiting Time = (9 + 16 + 14 + 18) / 4 = 14.25 ms
Average Turnaround Time = (14 + 23 + 18 + 24) / 4 = 19.75 ms
b) First Come First Serve (FCFS)
Since all processes arrive at the same time, execution follows the order
P1, P2, P3, P4.
Gantt Chart
0 5 12 16 22
| P1 | P2 | P3 | P4 |
Completion Times
P1 = 5, P2 = 12, P3 = 16, P4 = 22
Turnaround Time
P1 = 5, P2 = 12, P3 = 16, P4 = 22
Waiting Time
P1 = 0
P2 = 5
P3 = 12
P4 = 16
Average Values
Average Waiting Time = (0 + 5 + 12 + 16) / 4 = 8.25 ms
Average Turnaround Time = (5 + 12 + 16 + 22) / 4 = 13.75 ms
c) Comparison of Round Robin and FCFS
********** 10 **********
--- page 11 ---
From the results, it is observed that FCFS provides lower average
waiting time and turnaround time compared to Round Robin in this
case. This is because all processes arrive at the same time and shorter
processes are not delayed by time slicing.
Round Robin, on the other hand, ensures fairness by giving equal CPU
time to each process, but it increases waiting time due to frequent
context switching. Therefore, FCFS performs better for this specific
scenario, while Round Robin is more suitable for time-sharing systems
where responsiveness is important.
If you want, I can also give this in step-wise solving format (for
students to follow easily in exams) or convert it into a Word
document.
Deadlock is a situation in an operating system where a set of processes
are permanently blocked because each process is waiting for a resource
that is held by another process in the same set. As a result, none of the
processes can proceed, and the system gets stuck in a circular waiting
state. A common real-life analogy is two people each holding one
resource and waiting for the other to release theirs—neither moves
forward.
For a deadlock to occur, four necessary conditions must hold
Q4   simultaneously. The first is mutual exclusion, meaning at least one
CO-2;   resource must be non-shareable; only one process can use it at a time.
SO-2;   [20]
BL-3   The second is hold and wait, where a process holding at least one
and BL-4   resource is waiting to acquire additional resources held by other
processes. The third is no preemption, which implies that resources
cannot be forcibly taken away from a process; they must be released
voluntarily. The fourth is circular wait, where a circular chain of
processes exists such that each process is waiting for a resource held by
the next process in the cycle. If any one of these conditions is
prevented, deadlock cannot occur.
Operating systems use different techniques to handle deadlock, broadly
classified as prevention, detection, and recovery.
********** 11 **********
--- page 12 ---
In deadlock prevention, the system is designed in such a way that at
least one of the four necessary conditions is never allowed to occur. For
example, mutual exclusion can be reduced by making resources
sharable where possible, though this is not always practical. The hold-
and-wait condition can be avoided by requiring processes to request all
needed resources at once before execution begins, or by forcing them to
release currently held resources before requesting new ones. The no-
preemption condition can be handled by allowing the system to take
resources away from a process if it requests additional ones and cannot
be satisfied immediately. Circular wait can be prevented by imposing a
strict ordering on resource types and requiring processes to request
resources in that order. While prevention guarantees that deadlocks
never occur, it often leads to poor resource utilization and reduced
system efficiency.
In deadlock detection, the system allows deadlocks to occur but
periodically checks whether they have happened. This is typically done
using structures like a resource allocation graph or matrix-based
algorithms. If the system has only single instances of resources, a cycle
in the graph indicates deadlock. For multiple instances, more complex
detection algorithms similar to the Banker’s algorithm are used.
Detection is suitable for systems where deadlocks are rare, as it avoids
the overhead of strict prevention but requires additional computation to
monitor system state.
Once a deadlock is detected, the system must apply recovery
techniques to break the deadlock. One approach is process
termination, where one or more processes involved in the deadlock are
aborted. This can be done either by terminating all deadlocked
processes or by selecting processes one by one until the cycle is broken.
Another approach is resource preemption, where resources are taken
away from certain processes and given to others until the deadlock is
resolved. This requires careful handling to avoid inconsistencies, and
processes may need to be rolled back to a safe state before execution
resumes.
In summary, deadlock is a critical issue in resource management where
processes block each other indefinitely. The four necessary conditions
********** 12 **********
--- page 13 ---
define its occurrence, and operating systems handle it either by
preventing it altogether, detecting it after occurrence, or recovering
from it. Each approach involves trade-offs between system
performance, complexity, and resource utilization.
Here is the exam-style solution with proper columns (3 frames):
FIFO Page Replacement
Re Frame Frame Frame Page
f   1   2   3   Fault
5   5   -   -   Yes
0   5   0   -   Yes
1   5   0   1   Yes
0   5   0   1   No
2   2   0   1   Yes
3   2   3   1   Yes
0   2   3   0   Yes
2   2   3   0   No
4   4   3   0   Yes
3   4   3   0   No
3   4   3   0   No
2   4   2   0   Yes
0   4   2   0   No
2   4   2   0   No
1   1   2   0   Yes
2   1   2   0   No
7   1   7   0   Yes
0   1   7   0   No
1   1   7   0   No
1   1   7   0   No
********** 13 **********
--- page 14 ---
0   1   7   0   No
Total Page Faults (FIFO) = 15
LRU Page Replacement
Re Frame Frame Frame Page
f   1   2   3   Fault
5   5   -   -   Yes
0   5   0   -   Yes
1   5   0   1   Yes
0   5   0   1   No
2   2   0   1   Yes
3   2   3   1   Yes
0   2   3   0   Yes
2   2   3   0   No
4   4   3   0   Yes
3   4   3   0   No
3   4   3   0   No
2   4   3   2   Yes
0   0   3   2   Yes
2   0   3   2   No
1   0   1   2   Yes
2   0   1   2   No
7   7   1   2   Yes
0   7   0   2   Yes
1   7   0   1   Yes
1   7   0   1   No
0   7   0   1   No
Total Page Faults (LRU) = 12
Optimal Page Replacement
********** 14 **********
--- page 15 ---
Re Frame Frame Frame Page
f   1   2   3   Fault
5   5   -   -   Yes
0   5   0   -   Yes
1   5   0   1   Yes
0   5   0   1   No
2   2   0   1   Yes
3   2   0   3   Yes
0   2   0   3   No
2   2   0   3   No
4   2   4   3   Yes
3   2   4   3   No
3   2   4   3   No
2   2   4   3   No
0   2   0   3   Yes
2   2   0   3   No
1   2   0   1   Yes
2   2   0   1   No
7   2   0   7   Yes
0   2   0   7   No
1   1   0   7   Yes
1   1   0   7   No
0   1   0   7   No
Total Page Faults (Optimal) = 9
Final Conclusion
Optimal algorithm gives the minimum page faults, followed by LRU
and then FIFO. Therefore, Optimal is the best, while LRU is the best
practical approach.
********** 15 **********
--- page 16 ---
Here is the proper step-by-step exam solution (Banker’s Algorithm):
Step 1: Given Data
Allocation Matrix
P0 → (1 0 2 1)
P1 → (0 1 1 0)
P2 → (1 2 0 1)
P3 → (0 0 1 2)
Max Matrix
P0 → (3 2 2 2)
P1 → (1 3 3 1)
P2 → (2 4 1 2)
P3 → (1 2 2 3)
Available = (2 1 0 1)
i) Need Matrix Calculation
Q5
Need = Max – Allocation
CO-2;
P0 → (3−1, 2−0, 2−2, 2−1) = (2 2 0 1)
SO-2;   [20]
BL-3   P1 → (1−0, 3−1, 3−1, 1−0) = (1 2 2 1)
and BL-4   P2 → (2−1, 4−2, 1−0, 2−1) = (1 2 1 1)
P3 → (1−0, 2−0, 2−1, 3−2) = (1 2 1 1)
ii) Check Safe State
Initial Available = (2 1 0 1)
Now compare Need ≤ Available:
P0 → (2 2 0 1) ✗ (B not satisfied)
P1 → (1 2 2 1) ✗
P2 → (1 2 1 1) ✗
P3 → (1 2 1 1) ✗
No process can proceed since no Need is ≤ Available.
Conclusion
The system is NOT in a safe state because no process can execute first.
Hence, no safe sequence exists.
********** 16 **********
--- page 17 ---
iii) Request from P3 = (0 1 0 1)
Step 1: Check Request ≤ Need
P3 Need = (1 2 1 1)
Request = (0 1 0 1) → satisfies condition ✓
Step 2: Check Request ≤ Available
Available = (2 1 0 1)
Request = (0 1 0 1) → satisfies condition ✓
Step 3: Allocate Temporarily
New Available = (2 1 0 1) − (0 1 0 1) = (2 0 0 0)
New Allocation of P3 = (0 1 1 3)
New Need of P3 = (1 1 1 0)
Step 4: Check Safe State Again
Available = (2 0 0 0)
P0 → (2 2 0 1) ✗
P1 → (1 2 2 1) ✗
P2 → (1 2 1 1) ✗
P3 → (1 1 1 0) ✗
Again, no process can proceed.
Final Conclusion
The system is not in a safe state initially, and even after granting the
request, it remains unsafe. Therefore, the request cannot be granted
immediately.
********** 17 **********
--- page 18 ---
How Segmentation Overcomes Limitations of Paging
Paging divides memory into fixed-size blocks (pages/frames), which
simplifies allocation but introduces some limitations. Segmentation
addresses these issues as follows:
•   In paging, programs are divided into fixed-size pages without
considering the logical structure of a program. This makes it
difficult for programmers to relate memory to program
components. Segmentation, on the other hand, divides memory
based on logical units such as functions, arrays, stacks, and
modules, making it more meaningful and programmer-friendly.
• Paging suffers from internal fragmentation because memory is
allocated in fixed sizes, leading to unused space within a page.
********** 18 **********

[Text in pictures on this page, read by OCR]
os

Offset
< Limit

CPU Segment | Offset
Number

Logical Address

| | 1500 so

Base Limit
1800 a
|o] 1500 200
1 1800 100
= 2000
2] 2000 | 150 + 82
3| 2400 100
Segment Table 2400 $3
Main Memory

Segmentation

Paging

Logical Physical
Address Address
| 10000..00
cpu |—>| Plid t Il d | Physical

Memory

11111..11

"{

L_, f

Page table
--- page 19 ---
Segmentation eliminates internal fragmentation since segments
are of variable size, matching the actual size of program
components.
• Paging does not support logical protection and sharing
effectively at a high level. Segmentation enables protection and
sharing at segment level, allowing different processes to share
specific segments like libraries while keeping others private.
•   In paging, debugging and maintenance become difficult because
memory is not organized logically. Segmentation improves this
by maintaining a clear mapping between logical program
structure and memory layout.
However, segmentation may introduce external fragmentation, which
paging avoids—so both techniques have trade-offs.
Here is the proper exam solution with step-by-step calculation:
Given:
Request Queue: 98, 183, 37, 122, 14, 124, 65, 67
Initial Head Position = 53
i) FCFS (First Come First Serve)
In FCFS, requests are served in the order they arrive.
Sequence:
Q6
53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67
CO-3;
SO-2;   Head Movements:   [20]
BL-2
Movemen Distanc
and BL-4
t   e
53 → 98 45
98 → 183 85
183 → 37 146
37 → 122 85
122 → 14 108
14 → 124 110
124 → 65 59
********** 19 **********
--- page 20 ---
65 → 67 2
Total Head Movement:
45 + 85 + 146 + 85 + 108 + 110 + 59 + 2 = 640 tracks
ii) SSTF (Shortest Seek Time First)
In SSTF, the closest request to the current head position is serviced
first.
Step-wise Selection:
From 53 → nearest is 65
From 65 → nearest is 67
From 67 → nearest is 37
From 37 → nearest is 14
From 14 → nearest is 98
From 98 → nearest is 122
From 122 → nearest is 124
From 124 → nearest is 183
Sequence:
53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183
Head Movements:
Movemen Distanc
t   e
53 → 65 12
65 → 67 2
67 → 37 30
37 → 14 23
14 → 98 84
98 → 122 24
122 →
2
124
124 →
59
183
Total Head Movement:
12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = 236 tracks
********** 20 **********
--- page 21 ---
Final Answer
FCFS total head movement = 640 tracks
SSTF total head movement = 236 tracks
Conclusion
SSTF performs better than FCFS because it minimizes the seek time by
selecting the nearest request, resulting in significantly lower head
movement.
File Management in Operating System
********** 21 **********
--- page 22 ---
Concept of File Management
File management is a fundamental function of an operating system that
deals with the creation, organization, storage, retrieval, and
protection of files on secondary storage devices such as disks.
A file is a collection of related data stored on a storage device and
treated as a single unit by the OS. The operating system provides an
abstraction so users do not need to know how data is physically stored.
The OS is responsible for:
• Creating and deleting files
• Reading and writing data
• Managing directories (folders)
•   Controlling access permissions (security)
•   Allocating disk space efficiently
• Maintaining file metadata (size, type, location, timestamps)
Thus, file management ensures efficient, reliable, and secure data
storage and access.
File Organization Methods
File organization refers to how records within a file are arranged for
storage and retrieval.
1. Sequential File Organization
********** 22 **********

[Text in pictures on this page, read by OCR]
Comparison of File Designs

Sequential Direct-Access Indexed-Sequential
Types of Access batch online batch or online
Data Organization sequentially no particular sequentially and by
by key value order index
Flexibility in low high very high
Handling Inquiries
Availability of no yes yes
Up-to-Date Data
Speed of Retrieval slow very fast fast
Activity high low high
Volatility low high high
Examples payroll airline customer ordering
processing reservations and billing
and billing and banking

operations transactions
--- page 23 ---
• Data is stored in order (record by record)
• Access is done sequentially from beginning to end
•   Suitable for applications like logs or reports
Advantage: Simple and efficient for large batch processing
Limitation: Slow for random access
2. Direct (Random) File Organization
• Records are accessed directly using an address or key
• No need to read previous records
Advantage: Fast access to any record
Limitation: Requires calculation of address (hashing or indexing)
3. Indexed File Organization
• Uses an index table that stores keys and their corresponding
addresses
• Combines benefits of sequential and direct access
Advantage: Efficient searching and retrieval
Limitation: Extra storage required for index
File Storage Methods (Allocation Techniques)
File storage refers to how files are physically placed on disk blocks.
1. Contiguous Allocation
•   File occupies continuous blocks on disk
Advantages:
•   Fast access (both sequential and direct)
• Simple implementation
Disadvantages:
•   External fragmentation
•   Difficult to expand file size
2. Linked Allocation
•   File is stored as a linked list of blocks scattered across disk
• Each block points to the next
Advantages:
• No external fragmentation
********** 23 **********
--- page 24 ---
• Easy file growth
Disadvantages:
• Slow random access
•   Pointer overhead
3. Indexed Allocation
• A separate index block contains addresses of all file blocks
Advantages:
• Supports direct access
• No external fragmentation
Disadvantages:
• Extra space for index block
• Overhead for small files
How Files Are Stored and Accessed
Files are stored on disk as a collection of blocks. The OS maintains
metadata (via structures like file control blocks or inodes) that store:
•   File name, size, permissions
• Location of blocks on disk
When a user accesses a file:
1. The OS searches the directory structure to locate the file
2. Retrieves metadata (block addresses)
3. Uses the allocation method (contiguous/linked/indexed)
4. Reads or writes data from/to disk
Access methods include:
• Sequential access → read/write in order
• Direct access → jump to specific location
• Indexed access → use index for faster retrieval
Conclusion
File management in an OS ensures structured storage, efficient retrieval,
and secure handling of data. Different file organization and allocation
methods are used depending on system requirements, balancing
performance, flexibility, and storage efficiency.
********** 24 **********
--- page 25 ---
Select any 4 only.
1. Explain any two Operating System Services.
Operating System Services (Any Two)
1. Program Execution
Program execution is a core service of an operating system that
enables users to run application programs. The OS loads the
program from secondary storage into main memory, creates a
process, and begins execution. It allocates required resources
such as CPU time, memory, and I/O devices, and manages the
entire lifecycle of the program—from initiation to termination. It
also handles abnormal termination in case of errors, ensuring
smooth and controlled execution.
2. I/O Operations
Q7
The operating system provides a standardized interface for input
CO-
and output operations. Instead of interacting directly with
1,CO2
and CO-   hardware devices like keyboards, disks, or printers, users and   [20]
3; SO-2;
applications communicate through the OS. The OS manages
BL-2
device drivers, buffering, caching, and scheduling of I/O
and BL-3
requests to improve efficiency. It also detects and handles errors,
ensuring reliable communication between software and
hardware.
2. Define single-threaded and multi-threaded processes.
Single-Threaded and Multi-Threaded Processes
A process is a program in execution, and it may contain one or
more threads, which are the basic units of CPU execution.
Single-Threaded Process
A single-threaded process contains only one thread of
execution. This means the process performs one task at a time,
following a single sequence of instructions. If the thread is
blocked (for example, waiting for I/O), the entire process is also
blocked.
********** 25 **********
--- page 26 ---
Example: A simple calculator program that performs one
operation at a time.
Multi-Threaded Process
A multi-threaded process contains multiple threads within the
same process, all sharing the same memory space and resources.
These threads can execute concurrently, allowing the process to
perform multiple tasks simultaneously.
Example: A web browser where one thread handles user
interaction, another loads web pages, and another manages
background tasks.
Key Difference
Single-threaded → one task at a time, simpler but slower
Multi-threaded → multiple tasks concurrently, more efficient but
complex to manage.
3. What are the symbols used in a Resource Allocation Graph
(RAG)? Explain with a small example.
Symbols used in Resource Allocation Graph (RAG)
A Resource Allocation Graph (RAG) is a directed graph used to
represent the allocation of resources to processes and to detect
deadlocks in a system.
The main symbols used in a RAG are as follows:
A process is represented by a circle (○). Each circle denotes a process
such as P1, P2, etc.
A resource type is represented by a rectangle (□). If a resource has
multiple instances, it is shown by multiple dots inside the rectangle.
A request edge is represented by a directed arrow from a process to a
resource (P → R). This indicates that the process is requesting that
resource.
An assignment edge is represented by a directed arrow from a
resource to a process (R → P). This indicates that the resource has
been allocated to that process.
Small Example
********** 26 **********
--- page 27 ---
Consider two processes P1 and P2, and two resources R1 and R2.
Process P1 is holding resource R1 and requesting resource R2. At the
same time, process P2 is holding resource R2 and requesting resource
R1.
********** 27 **********
--- page 28 ---
This situation can be represented using a Resource Allocation Graph
where there is an assignment edge from R1 to P1 and from R2 to P2,
and request edges from P1 to R2 and from P2 to R1.
Such a graph forms a cycle, which indicates the possibility of a
deadlock when each resource has a single instance.
4. Explain the working of Peterson’s Solution using shared
variables (flag and turn).
Peterson’s Solution is a classical software-based solution to the
critical section problem for two processes. It ensures mutual
exclusion, progress, and bounded waiting using two shared
variables:
•   flag[2] → indicates if a process wants to enter the critical section
•   turn → indicates whose turn it is to enter
🔹 Shared Variables
boolean flag[2];   // initially flag[0] = flag[1] = false
int turn;
🔹 Structure for Process Pi (i = 0 or 1)
do {
flag[i] = true;   // Process Pi wants to enter
turn = j;   // Give chance to other process
while (flag[j] && turn == j);   // Wait if Pj wants to enter and
it's Pj's turn
// Critical Section
flag[i] = false;   // Exit section
// Remainder Section
} while (true);
(where j = 1 - i)
********** 28 **********
--- page 29 ---
🔹 Working Explanation
Consider two processes P0 and P1:
1. Desire to Enter Critical Section
o When a process (say P0) wants to enter, it sets:
▪   flag[0] = true
o This indicates interest in entering the critical section.
2. Turn Assignment
o P0 sets turn = 1 (gives priority to P1).
o This ensures fairness if both processes request
simultaneously.
3. Condition Checking (Busy Waiting)
o P0 checks:
o while (flag[1] && turn == 1);
o This means:
▪   If P1 also wants to enter (flag[1] = true)
▪ AND it is P1’s turn → P0 waits
4. Entering Critical Section
o   If the condition becomes false:
▪   Either P1 is not interested (flag[1] = false)
▪ OR it is not P1’s turn
→ P0 enters the critical section
5. Exiting Critical Section
o After execution, P0 sets:
▪   flag[0] = false
o This allows P1 to enter
🔹 Key Properties Achieved
• Mutual Exclusion
Only one process can enter the critical section at a time.
• Progress
If no process is in the critical section, one of the waiting
processes will be allowed to enter.
• Bounded Waiting
Each process gets a fair chance (due to turn variable).
********** 29 **********
--- page 30 ---
🔹 Example Scenario
• Both P0 and P1 set their flag = true at the same time
• Suppose turn = 1
→ P0 waits, P1 enters
•   After P1 exits, it sets flag[1] = false
→ Now P0 can enter
5. Explain the concept of a page fault and write the steps involved
in handling a page fault?
Page Fault – Concept
A page fault occurs in a paging-based memory management
system when a process tries to access a page that is not
currently present in main memory (RAM) but is available on
secondary storage (disk).
• Each process has a page table with a valid/invalid bit
•   If the bit is invalid, it indicates the page is not in memory
→ This triggers a page fault trap to the operating system
Working of Page Fault (Conceptual View)
********** 30 **********
--- page 31 ---
Steps Involved in Handling a Page Fault
1. Page Access Attempt
o CPU generates a logical address
o Page table is checked for validity
2. Page Fault Detection
o   If the valid bit = 0 (invalid)
→ Hardware triggers a page fault interrupt (trap) to OS
3. Check Validity of Reference
o OS verifies whether the reference is:
▪ Legal (valid page but not in memory) →
proceed
▪   Illegal (invalid access) → terminate process
********** 31 **********

[Text in pictures on this page, read by OCR]
page is on
backing store

operating
system ®
reference
@ trap
load M 4 li
restart | page table
instruction
free frame
reset page bring in
table missing page
physical

memory
--- page 32 ---
4. Locate the Required Page on Disk
o OS finds the required page in secondary storage
(backing store)
5. Find a Free Frame
o   If a free frame is available → use it
o Otherwise → apply a page replacement algorithm (e.g.,
FIFO, LRU)
6. Swap Out (if required)
o   If the selected frame contains a modified page
→ write it back to disk
7. Load Required Page into Memory
o Read the required page from disk into the selected frame
8. Update Page Table
o Set valid bit = 1
o Update frame number for the page
9. Restart the Instruction
o The interrupted instruction is restarted
o This time, execution proceeds successfully
5.Define a file in an operating system. Explain the different types of
files.
Definition of a File in Operating System
A file is a collection of related information stored on secondary
storage (such as a disk), identified by a name, and treated as a
single unit by the operating system.
•   It can store data, programs, or any form of information
•   Files provide a way to store, retrieve, and manage data
permanently
• Each file has attributes such as name, type, size, location, and
permissions
Conceptual View of File System
********** 32 **********
--- page 33 ---
directory directory

file file file

Structures of Directory in Operating System
Two Level ale Root
Master Directory (ESI

Directory J T 3
User fiw file File MMgrm File | File
Directory faivtag Entry Entry Meaney Entry Entry
Files

rhe ats

Ul Suz U3 Files

D3 D4" D5 wm

Directory Single Level Directory

Directory ye methods,txt) os.docx 2.mp4_JTP.txt
Files

D9 DIO
Files
@stop
root | spell bin programs|
stat | mail | dist find | count| hex |reorder e mail
prog | copy | prt exp reorder| list find hex | count

ooo Lf

list obj | spell all last | first

666666

FR ICR QQ I OH
--- page 34 ---
Different Types of Files
Operating systems classify files based on their structure and
purpose:
1. Regular Files (Ordinary Files)
• Contain user data such as text, images, programs, etc.
• Can be text files or binary files
• Examples: .txt, .doc, .exe, .jpg
2. Directory Files
•   Store information about files and subdirectories
• Help in organizing files in a hierarchical structure
• Example: folders in Windows/Linux
3. Special Files (Device Files)
• Represent hardware devices
• Used for input/output operations
• Two types:
o Character Special Files → data handled as a stream
(keyboard, mouse)
o Block Special Files → data handled in blocks (hard disk)
4. FIFO (Named Pipe) Files
• Used for inter-process communication (IPC)
• Data flows in a first-in, first-out manner
5. Symbolic Link Files
• Act as a pointer/reference to another file
• Do not contain actual data, only the path of the original file
********** 34 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper db9ab6dbd450

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_IT_7041/Operating Systems/ANS_Operating Systems(702CO0C056)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 Jul 2026
- Text: mixed (34 pages), mean OCR confidence 74.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSBS)/B. Tech (CSE - CS)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech
(IT)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 14 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 34 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   1. Define Operating System & Objectives
An Operating System (OS) is system software that acts as an interface
between the user and the computer hardware. It manages hardware
resources and provides services for application programs, ensuring
efficient and convenient system operation.
Objectives of a modern Operating System:
CO- 1;   1. Convenience: Makes the computer system easy to use.
SO-2 ;
2. Efficiency: Ensures optimal use of hardware resources like CPU,
BL-2
memory, and I/O devices.
3. Ability to Evolve: Allows the system to be updated with new
features and improvements.
4. Resource Management: Efficiently allocates and manages
system resources among processes.
b.   2. Process Control Block (PCB) and its Components
A Process Control Block (PCB) is a data structure used by the operating
CO-2 ;
SO-2 ;   system to store all relevant information about a process. It is essential for
BL-2   process management and context switching.
Components of PCB:
********** 1 **********
--- page 2 ---
• Process ID (PID): Unique identifier assigned to each process.
• Process State: Indicates whether the process is new, ready,
running, waiting, or terminated.
• Program Counter: Stores the address of the next instruction to
be executed.
• CPU Registers: Holds the values of CPU registers for the
process.
• Memory Management Information: Includes details like page
tables, base and limit registers.
• I/O Status Information: Contains information about I/O devices
allocated to the process.
• Accounting Information: Tracks CPU usage, execution time,
and other statistics.
c.   3. Conditions for Critical Section Problem
To ensure correct and fair access to shared resources, a solution to the
CO-3 ;   critical section problem must satisfy the following conditions:
SO-2 ;   1. Mutual Exclusion: Only one process can execute in the critical
BL-2
and BL-3   section at any given time.
2. Progress: If no process is in the critical section, the selection of
the next process cannot be postponed indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
Process ID

Process state

Process priority

Accounting information

Program counter

CPU registers

PCB pointers

List of open files

Process I/O status information
--- page 3 ---
3. Bounded Waiting: There must be a limit on how many times
other processes can enter the critical section before a waiting
process gets its turn
d.   Necessary Conditions for Deadlock
Deadlock can occur only if all the following four conditions hold
simultaneously:
1. Mutual Exclusion: At least one resource must be held in a non-
shareable mode.
2. Hold and Wait: A process holding at least one resource is waiting
CO-3 ;
SO-2 ;   to acquire additional resources.
BL-2   3. No Preemption: Resources cannot be forcibly taken from a
process; they must be released voluntarily.
4. Circular Wait: A circular chain of processes exists where each
process is waiting for a resource held by another process in the
chain.
a. SRTF (Preemptive SJF)
Gantt Chart
0 1 5 7 11 16
| P2 | P3 | P0 | P1 | P2 |
Completion Time (CT)
• P2 = 16
• P3 = 5
Q2   • P1 = 11
CO-2;   • P0 = 7
[20]
SO-2;   Turnaround Time (TAT = CT – AT)
BL-3
and BL-4   • P2 = 16 – 0 = 16
• P3 = 5 – 1 = 4
• P1 = 11 – 2 = 9
• P0 = 7 – 3 = 4
Waiting Time (WT = TAT – BT)
• P2 = 16 – 6 = 10
• P3 = 4 – 4 = 0
• P1 = 9 – 4 = 5
********** 3 **********
--- page 4 ---
• P0 = 4 – 2 = 2
Average Times
• Average Waiting Time = (10 + 0 + 5 + 2) / 4 = 4.25
• Average Turnaround Time = (16 + 4 + 9 + 4) / 4 = 8.25
ii) Non-Preemptive SJF
Gantt Chart
0 6 8 12 16
| P2 | P0 | P3 | P1 |
Completion Time (CT)
• P2 = 6
• P0 = 8
• P3 = 12
• P1 = 16
Turnaround Time (TAT)
• P2 = 6 – 0 = 6
• P0 = 8 – 3 = 5
• P3 = 12 – 1 = 11
• P1 = 16 – 2 = 14
Waiting Time (WT)
• P2 = 6 – 6 = 0
• P0 = 5 – 2 = 3
• P3 = 11 – 4 = 7
• P1 = 14 – 4 = 10
Average Times
• Average Waiting Time = (0 + 3 + 7 + 10) / 4 = 5
• Average Turnaround Time = (6 + 5 + 11 + 14) / 4 = 9
iii) Comparison (2 Marks)
• SRTF (Preemptive SJF) gives better performance with:
o Lower Average Waiting Time (4.25 < 5)
o Lower Average Turnaround Time (8.25 < 9)
• This is because shorter processes get CPU earlier due to
preemption.
• However, SRTF is more complex and may cause frequent
context switching.
********** 4 **********
--- page 5 ---
(i) What is a Semaphore? Explain its Types (3 Marks)
A semaphore is a synchronization tool used in operating systems to
control access to shared resources by multiple processes or threads.
It is essentially an integer variable that is accessed only through two
atomic operations: wait() and signal().
Types of Semaphores:
Binary Semaphore (Mutex)
Takes only two values: 0 or 1
Used for mutual exclusion (only one process can access the critical
section at a time)
Example:
A printer shared by multiple processes
If semaphore = 1 → resource is free
If semaphore = 0 → resource is busy
Counting Semaphore
Can take non-negative integer values (0, 1, 2, …)
Used when multiple instances of a resource are available
Example:
A system with 3 identical printers → semaphore initialized to 3
Each process decreases count when using a printer and increases
after releasing
(ii) Semaphore Implementation Using Busy Waiting (4 Marks)
In busy waiting, a process continuously checks (loops) until the
semaphore becomes available.
Operations:
wait(S) {
while (S <= 0);   // busy waiting (spin lock)
S--;
}
signal(S) {
********** 5 **********
--- page 6 ---
S++;
}
Explanation:
•   wait(S):
o Checks if S > 0
o   If not, it keeps checking repeatedly (CPU is busy)
o When S > 0, it decrements S and enters the critical
section
•   signal(S):
o Increments the semaphore value
o Indicates that the resource is released
Drawback:
• CPU cycles are wasted while waiting
•   Inefficient for long waiting periods
(iii) Semaphore Without Busy Waiting (4 Marks)
To avoid wasting CPU time, semaphores can be implemented using
blocking (sleep) and wakeup mechanisms.
Operations:
wait(S) {
S--;
if (S < 0) {
add process to queue;
block();   // process goes to sleep
}
}
signal(S) {
S++;
if (S <= 0) {
remove process from queue;
wakeup(process);
}
}
Explanation:
wait(S):
********** 6 **********
--- page 7 ---
If resource not available → process is blocked
It is placed in a waiting queue
signal(S):
Wakes up one waiting process from the queue
Advantages:
No CPU wastage (no spinning)
Better CPU utilization
Efficient for systems with many processes
i   Readers–Writers Problem
The Readers–Writers problem is a classic synchronization problem in
operating systems that deals with managing access to a shared
resource (like a file or database).
• Readers → only read the data (do not modify)
• Writers → modify the data
Key Requirement:
• Multiple readers can access the resource simultaneously
• Only one writer can access the resource exclusively
• No reader should read while a writer is writing
Q3
Types of Readers–Writers Problems
CO-2;
1. Reader Priority → Readers are not blocked unless a writer is   [20]
SO-2;
BL-3 and   already writing
BL-4
2. Writer Priority → Writers get priority (avoid starvation)
3. Fair Solution → No starvation for either
(Below is the standard Reader-Priority solution using semaphores)
Semaphore-Based Solution
Initialization:
semaphore mutex = 1;   // protects readCount
semaphore wrt = 1;   // controls access to shared resource
int readCount = 0;   // number of active readers
Reader Process
********** 7 **********
--- page 8 ---
wait(mutex);
readCount++;
if (readCount == 1)
wait(wrt);   // first reader blocks writers
signal(mutex);
// Reading is performed
wait(mutex);
readCount--;
if (readCount == 0)
signal(wrt); // last reader releases writer
signal(mutex);
Writer Process
wait(wrt);
// Writing is performed
signal(wrt);
How the Solution Works
1. Handling Multiple Readers
• The variable readCount keeps track of active readers
•   First reader locks the resource using wait(wrt)
• Subsequent readers:
o Do NOT block
o Can read simultaneously
• Hence, multiple readers are allowed concurrently
2. Handling Single Writer
• Writer uses wait(wrt)
•   If:
o Any reader is active OR
********** 8 **********
--- page 9 ---
o Another writer is active
→ writer must wait
• Ensures only one writer at a time
3. Mutual Exclusion Logic
• mutex protects updates to readCount
• wrt ensures:
o No writer enters when readers are present
o No readers enter when a writer is active
Key Advantages
•   Efficient for read-heavy systems
• Allows maximum concurrency for readers
Limitation
•   Writers may suffer from starvation
(continuous arrival of readers may delay writers indefinitely)
Conclusion
• The semaphore-based solution ensures:
o Concurrent access for readers
o Exclusive access for writers
• Achieves synchronization using:
o mutex → protects shared variable
o wrt → controls resource access.
Here is the descriptive answer (without bullets, exam-ready format):
a) Round Robin Scheduling (Time Quantum = 3 ms)
All processes arrive at time 0 ms, so scheduling starts in the order P1,
P2, P3, and P4.
Gantt Chart
0 3 6 9 12 14 17 18 21 23 24
********** 9 **********
--- page 10 ---
| P1 | P2 | P3 | P4 | P1 | P2 | P3 | P4 | P2 | P4 |
Completion Times
P3 completes at 18 ms, P1 at 14 ms, P2 at 23 ms, and P4 at 24 ms.
Turnaround Time (TAT = CT – AT)
Since all arrival times are 0:
P1 = 14, P2 = 23, P3 = 18, P4 = 24
Waiting Time (WT = TAT – BT)
P1 = 14 – 5 = 9
P2 = 23 – 7 = 16
P3 = 18 – 4 = 14
P4 = 24 – 6 = 18
Average Values
Average Waiting Time = (9 + 16 + 14 + 18) / 4 = 14.25 ms
Average Turnaround Time = (14 + 23 + 18 + 24) / 4 = 19.75 ms
b) First Come First Serve (FCFS)
Since all processes arrive at the same time, execution follows the order
P1, P2, P3, P4.
Gantt Chart
0 5 12 16 22
| P1 | P2 | P3 | P4 |
Completion Times
P1 = 5, P2 = 12, P3 = 16, P4 = 22
Turnaround Time
P1 = 5, P2 = 12, P3 = 16, P4 = 22
Waiting Time
P1 = 0
P2 = 5
P3 = 12
P4 = 16
Average Values
Average Waiting Time = (0 + 5 + 12 + 16) / 4 = 8.25 ms
Average Turnaround Time = (5 + 12 + 16 + 22) / 4 = 13.75 ms
c) Comparison of Round Robin and FCFS
********** 10 **********
--- page 11 ---
From the results, it is observed that FCFS provides lower average
waiting time and turnaround time compared to Round Robin in this
case. This is because all processes arrive at the same time and shorter
processes are not delayed by time slicing.
Round Robin, on the other hand, ensures fairness by giving equal CPU
time to each process, but it increases waiting time due to frequent
context switching. Therefore, FCFS performs better for this specific
scenario, while Round Robin is more suitable for time-sharing systems
where responsiveness is important.
If you want, I can also give this in step-wise solving format (for
students to follow easily in exams) or convert it into a Word
document.
Deadlock is a situation in an operating system where a set of processes
are permanently blocked because each process is waiting for a resource
that is held by another process in the same set. As a result, none of the
processes can proceed, and the system gets stuck in a circular waiting
state. A common real-life analogy is two people each holding one
resource and waiting for the other to release theirs—neither moves
forward.
For a deadlock to occur, four necessary conditions must hold
Q4   simultaneously. The first is mutual exclusion, meaning at least one
CO-2;   resource must be non-shareable; only one process can use it at a time.
SO-2;   [20]
BL-3   The second is hold and wait, where a process holding at least one
and BL-4   resource is waiting to acquire additional resources held by other
processes. The third is no preemption, which implies that resources
cannot be forcibly taken away from a process; they must be released
voluntarily. The fourth is circular wait, where a circular chain of
processes exists such that each process is waiting for a resource held by
the next process in the cycle. If any one of these conditions is
prevented, deadlock cannot occur.
Operating systems use different techniques to handle deadlock, broadly
classified as prevention, detection, and recovery.
********** 11 **********
--- page 12 ---
In deadlock prevention, the system is designed in such a way that at
least one of the four necessary conditions is never allowed to occur. For
example, mutual exclusion can be reduced by making resources
sharable where possible, though this is not always practical. The hold-
and-wait condition can be avoided by requiring processes to request all
needed resources at once before execution begins, or by forcing them to
release currently held resources before requesting new ones. The no-
preemption condition can be handled by allowing the system to take
resources away from a process if it requests additional ones and cannot
be satisfied immediately. Circular wait can be prevented by imposing a
strict ordering on resource types and requiring processes to request
resources in that order. While prevention guarantees that deadlocks
never occur, it often leads to poor resource utilization and reduced
system efficiency.
In deadlock detection, the system allows deadlocks to occur but
periodically checks whether they have happened. This is typically done
using structures like a resource allocation graph or matrix-based
algorithms. If the system has only single instances of resources, a cycle
in the graph indicates deadlock. For multiple instances, more complex
detection algorithms similar to the Banker’s algorithm are used.
Detection is suitable for systems where deadlocks are rare, as it avoids
the overhead of strict prevention but requires additional computation to
monitor system state.
Once a deadlock is detected, the system must apply recovery
techniques to break the deadlock. One approach is process
termination, where one or more processes involved in the deadlock are
aborted. This can be done either by terminating all deadlocked
processes or by selecting processes one by one until the cycle is broken.
Another approach is resource preemption, where resources are taken
away from certain processes and given to others until the deadlock is
resolved. This requires careful handling to avoid inconsistencies, and
processes may need to be rolled back to a safe state before execution
resumes.
In summary, deadlock is a critical issue in resource management where
processes block each other indefinitely. The four necessary conditions
********** 12 **********
--- page 13 ---
define its occurrence, and operating systems handle it either by
preventing it altogether, detecting it after occurrence, or recovering
from it. Each approach involves trade-offs between system
performance, complexity, and resource utilization.
Here is the exam-style solution with proper columns (3 frames):
FIFO Page Replacement
Re Frame Frame Frame Page
f   1   2   3   Fault
5   5   -   -   Yes
0   5   0   -   Yes
1   5   0   1   Yes
0   5   0   1   No
2   2   0   1   Yes
3   2   3   1   Yes
0   2   3   0   Yes
2   2   3   0   No
4   4   3   0   Yes
3   4   3   0   No
3   4   3   0   No
2   4   2   0   Yes
0   4   2   0   No
2   4   2   0   No
1   1   2   0   Yes
2   1   2   0   No
7   1   7   0   Yes
0   1   7   0   No
1   1   7   0   No
1   1   7   0   No
********** 13 **********
--- page 14 ---
0   1   7   0   No
Total Page Faults (FIFO) = 15
LRU Page Replacement
Re Frame Frame Frame Page
f   1   2   3   Fault
5   5   -   -   Yes
0   5   0   -   Yes
1   5   0   1   Yes
0   5   0   1   No
2   2   0   1   Yes
3   2   3   1   Yes
0   2   3   0   Yes
2   2   3   0   No
4   4   3   0   Yes
3   4   3   0   No
3   4   3   0   No
2   4   3   2   Yes
0   0   3   2   Yes
2   0   3   2   No
1   0   1   2   Yes
2   0   1   2   No
7   7   1   2   Yes
0   7   0   2   Yes
1   7   0   1   Yes
1   7   0   1   No
0   7   0   1   No
Total Page Faults (LRU) = 12
Optimal Page Replacement
********** 14 **********
--- page 15 ---
Re Frame Frame Frame Page
f   1   2   3   Fault
5   5   -   -   Yes
0   5   0   -   Yes
1   5   0   1   Yes
0   5   0   1   No
2   2   0   1   Yes
3   2   0   3   Yes
0   2   0   3   No
2   2   0   3   No
4   2   4   3   Yes
3   2   4   3   No
3   2   4   3   No
2   2   4   3   No
0   2   0   3   Yes
2   2   0   3   No
1   2   0   1   Yes
2   2   0   1   No
7   2   0   7   Yes
0   2   0   7   No
1   1   0   7   Yes
1   1   0   7   No
0   1   0   7   No
Total Page Faults (Optimal) = 9
Final Conclusion
Optimal algorithm gives the minimum page faults, followed by LRU
and then FIFO. Therefore, Optimal is the best, while LRU is the best
practical approach.
********** 15 **********
--- page 16 ---
Here is the proper step-by-step exam solution (Banker’s Algorithm):
Step 1: Given Data
Allocation Matrix
P0 → (1 0 2 1)
P1 → (0 1 1 0)
P2 → (1 2 0 1)
P3 → (0 0 1 2)
Max Matrix
P0 → (3 2 2 2)
P1 → (1 3 3 1)
P2 → (2 4 1 2)
P3 → (1 2 2 3)
Available = (2 1 0 1)
i) Need Matrix Calculation
Q5
Need = Max – Allocation
CO-2;
P0 → (3−1, 2−0, 2−2, 2−1) = (2 2 0 1)
SO-2;   [20]
BL-3   P1 → (1−0, 3−1, 3−1, 1−0) = (1 2 2 1)
and BL-4   P2 → (2−1, 4−2, 1−0, 2−1) = (1 2 1 1)
P3 → (1−0, 2−0, 2−1, 3−2) = (1 2 1 1)
ii) Check Safe State
Initial Available = (2 1 0 1)
Now compare Need ≤ Available:
P0 → (2 2 0 1) ✗ (B not satisfied)
P1 → (1 2 2 1) ✗
P2 → (1 2 1 1) ✗
P3 → (1 2 1 1) ✗
No process can proceed since no Need is ≤ Available.
Conclusion
The system is NOT in a safe state because no process can execute first.
Hence, no safe sequence exists.
********** 16 **********
--- page 17 ---
iii) Request from P3 = (0 1 0 1)
Step 1: Check Request ≤ Need
P3 Need = (1 2 1 1)
Request = (0 1 0 1) → satisfies condition ✓
Step 2: Check Request ≤ Available
Available = (2 1 0 1)
Request = (0 1 0 1) → satisfies condition ✓
Step 3: Allocate Temporarily
New Available = (2 1 0 1) − (0 1 0 1) = (2 0 0 0)
New Allocation of P3 = (0 1 1 3)
New Need of P3 = (1 1 1 0)
Step 4: Check Safe State Again
Available = (2 0 0 0)
P0 → (2 2 0 1) ✗
P1 → (1 2 2 1) ✗
P2 → (1 2 1 1) ✗
P3 → (1 1 1 0) ✗
Again, no process can proceed.
Final Conclusion
The system is not in a safe state initially, and even after granting the
request, it remains unsafe. Therefore, the request cannot be granted
immediately.
********** 17 **********
--- page 18 ---
How Segmentation Overcomes Limitations of Paging
Paging divides memory into fixed-size blocks (pages/frames), which
simplifies allocation but introduces some limitations. Segmentation
addresses these issues as follows:
•   In paging, programs are divided into fixed-size pages without
considering the logical structure of a program. This makes it
difficult for programmers to relate memory to program
components. Segmentation, on the other hand, divides memory
based on logical units such as functions, arrays, stacks, and
modules, making it more meaningful and programmer-friendly.
• Paging suffers from internal fragmentation because memory is
allocated in fixed sizes, leading to unused space within a page.
********** 18 **********

[Text in pictures on this page, read by OCR]
os

Offset
< Limit

CPU Segment | Offset
Number

Logical Address

| | 1500 so

Base Limit
1800 a
|o] 1500 200
1 1800 100
= 2000
2] 2000 | 150 + 82
3| 2400 100
Segment Table 2400 $3
Main Memory

Segmentation

Paging

Logical Physical
Address Address
| 10000..00
cpu |—>| Plid t Il d | Physical

Memory

11111..11

"{

L_, f

Page table
--- page 19 ---
Segmentation eliminates internal fragmentation since segments
are of variable size, matching the actual size of program
components.
• Paging does not support logical protection and sharing
effectively at a high level. Segmentation enables protection and
sharing at segment level, allowing different processes to share
specific segments like libraries while keeping others private.
•   In paging, debugging and maintenance become difficult because
memory is not organized logically. Segmentation improves this
by maintaining a clear mapping between logical program
structure and memory layout.
However, segmentation may introduce external fragmentation, which
paging avoids—so both techniques have trade-offs.
Here is the proper exam solution with step-by-step calculation:
Given:
Request Queue: 98, 183, 37, 122, 14, 124, 65, 67
Initial Head Position = 53
i) FCFS (First Come First Serve)
In FCFS, requests are served in the order they arrive.
Sequence:
Q6
53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67
CO-3;
SO-2;   Head Movements:   [20]
BL-2
Movemen Distanc
and BL-4
t   e
53 → 98 45
98 → 183 85
183 → 37 146
37 → 122 85
122 → 14 108
14 → 124 110
124 → 65 59
********** 19 **********
--- page 20 ---
65 → 67 2
Total Head Movement:
45 + 85 + 146 + 85 + 108 + 110 + 59 + 2 = 640 tracks
ii) SSTF (Shortest Seek Time First)
In SSTF, the closest request to the current head position is serviced
first.
Step-wise Selection:
From 53 → nearest is 65
From 65 → nearest is 67
From 67 → nearest is 37
From 37 → nearest is 14
From 14 → nearest is 98
From 98 → nearest is 122
From 122 → nearest is 124
From 124 → nearest is 183
Sequence:
53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183
Head Movements:
Movemen Distanc
t   e
53 → 65 12
65 → 67 2
67 → 37 30
37 → 14 23
14 → 98 84
98 → 122 24
122 →
2
124
124 →
59
183
Total Head Movement:
12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 = 236 tracks
********** 20 **********
--- page 21 ---
Final Answer
FCFS total head movement = 640 tracks
SSTF total head movement = 236 tracks
Conclusion
SSTF performs better than FCFS because it minimizes the seek time by
selecting the nearest request, resulting in significantly lower head
movement.
File Management in Operating System
********** 21 **********
--- page 22 ---
Concept of File Management
File management is a fundamental function of an operating system that
deals with the creation, organization, storage, retrieval, and
protection of files on secondary storage devices such as disks.
A file is a collection of related data stored on a storage device and
treated as a single unit by the OS. The operating system provides an
abstraction so users do not need to know how data is physically stored.
The OS is responsible for:
• Creating and deleting files
• Reading and writing data
• Managing directories (folders)
•   Controlling access permissions (security)
•   Allocating disk space efficiently
• Maintaining file metadata (size, type, location, timestamps)
Thus, file management ensures efficient, reliable, and secure data
storage and access.
File Organization Methods
File organization refers to how records within a file are arranged for
storage and retrieval.
1. Sequential File Organization
********** 22 **********

[Text in pictures on this page, read by OCR]
Comparison of File Designs

Sequential Direct-Access Indexed-Sequential
Types of Access batch online batch or online
Data Organization sequentially no particular sequentially and by
by key value order index
Flexibility in low high very high
Handling Inquiries
Availability of no yes yes
Up-to-Date Data
Speed of Retrieval slow very fast fast
Activity high low high
Volatility low high high
Examples payroll airline customer ordering
processing reservations and billing
and billing and banking

operations transactions
--- page 23 ---
• Data is stored in order (record by record)
• Access is done sequentially from beginning to end
•   Suitable for applications like logs or reports
Advantage: Simple and efficient for large batch processing
Limitation: Slow for random access
2. Direct (Random) File Organization
• Records are accessed directly using an address or key
• No need to read previous records
Advantage: Fast access to any record
Limitation: Requires calculation of address (hashing or indexing)
3. Indexed File Organization
• Uses an index table that stores keys and their corresponding
addresses
• Combines benefits of sequential and direct access
Advantage: Efficient searching and retrieval
Limitation: Extra storage required for index
File Storage Methods (Allocation Techniques)
File storage refers to how files are physically placed on disk blocks.
1. Contiguous Allocation
•   File occupies continuous blocks on disk
Advantages:
•   Fast access (both sequential and direct)
• Simple implementation
Disadvantages:
•   External fragmentation
•   Difficult to expand file size
2. Linked Allocation
•   File is stored as a linked list of blocks scattered across disk
• Each block points to the next
Advantages:
• No external fragmentation
********** 23 **********
--- page 24 ---
• Easy file growth
Disadvantages:
• Slow random access
•   Pointer overhead
3. Indexed Allocation
• A separate index block contains addresses of all file blocks
Advantages:
• Supports direct access
• No external fragmentation
Disadvantages:
• Extra space for index block
• Overhead for small files
How Files Are Stored and Accessed
Files are stored on disk as a collection of blocks. The OS maintains
metadata (via structures like file control blocks or inodes) that store:
•   File name, size, permissions
• Location of blocks on disk
When a user accesses a file:
1. The OS searches the directory structure to locate the file
2. Retrieves metadata (block addresses)
3. Uses the allocation method (contiguous/linked/indexed)
4. Reads or writes data from/to disk
Access methods include:
• Sequential access → read/write in order
• Direct access → jump to specific location
• Indexed access → use index for faster retrieval
Conclusion
File management in an OS ensures structured storage, efficient retrieval,
and secure handling of data. Different file organization and allocation
methods are used depending on system requirements, balancing
performance, flexibility, and storage efficiency.
********** 24 **********
--- page 25 ---
Select any 4 only.
1. Explain any two Operating System Services.
Operating System Services (Any Two)
1. Program Execution
Program execution is a core service of an operating system that
enables users to run application programs. The OS loads the
program from secondary storage into main memory, creates a
process, and begins execution. It allocates required resources
such as CPU time, memory, and I/O devices, and manages the
entire lifecycle of the program—from initiation to termination. It
also handles abnormal termination in case of errors, ensuring
smooth and controlled execution.
2. I/O Operations
Q7
The operating system provides a standardized interface for input
CO-
and output operations. Instead of interacting directly with
1,CO2
and CO-   hardware devices like keyboards, disks, or printers, users and   [20]
3; SO-2;
applications communicate through the OS. The OS manages
BL-2
device drivers, buffering, caching, and scheduling of I/O
and BL-3
requests to improve efficiency. It also detects and handles errors,
ensuring reliable communication between software and
hardware.
2. Define single-threaded and multi-threaded processes.
Single-Threaded and Multi-Threaded Processes
A process is a program in execution, and it may contain one or
more threads, which are the basic units of CPU execution.
Single-Threaded Process
A single-threaded process contains only one thread of
execution. This means the process performs one task at a time,
following a single sequence of instructions. If the thread is
blocked (for example, waiting for I/O), the entire process is also
blocked.
********** 25 **********
--- page 26 ---
Example: A simple calculator program that performs one
operation at a time.
Multi-Threaded Process
A multi-threaded process contains multiple threads within the
same process, all sharing the same memory space and resources.
These threads can execute concurrently, allowing the process to
perform multiple tasks simultaneously.
Example: A web browser where one thread handles user
interaction, another loads web pages, and another manages
background tasks.
Key Difference
Single-threaded → one task at a time, simpler but slower
Multi-threaded → multiple tasks concurrently, more efficient but
complex to manage.
3. What are the symbols used in a Resource Allocation Graph
(RAG)? Explain with a small example.
Symbols used in Resource Allocation Graph (RAG)
A Resource Allocation Graph (RAG) is a directed graph used to
represent the allocation of resources to processes and to detect
deadlocks in a system.
The main symbols used in a RAG are as follows:
A process is represented by a circle (○). Each circle denotes a process
such as P1, P2, etc.
A resource type is represented by a rectangle (□). If a resource has
multiple instances, it is shown by multiple dots inside the rectangle.
A request edge is represented by a directed arrow from a process to a
resource (P → R). This indicates that the process is requesting that
resource.
An assignment edge is represented by a directed arrow from a
resource to a process (R → P). This indicates that the resource has
been allocated to that process.
Small Example
********** 26 **********
--- page 27 ---
Consider two processes P1 and P2, and two resources R1 and R2.
Process P1 is holding resource R1 and requesting resource R2. At the
same time, process P2 is holding resource R2 and requesting resource
R1.
********** 27 **********
--- page 28 ---
This situation can be represented using a Resource Allocation Graph
where there is an assignment edge from R1 to P1 and from R2 to P2,
and request edges from P1 to R2 and from P2 to R1.
Such a graph forms a cycle, which indicates the possibility of a
deadlock when each resource has a single instance.
4. Explain the working of Peterson’s Solution using shared
variables (flag and turn).
Peterson’s Solution is a classical software-based solution to the
critical section problem for two processes. It ensures mutual
exclusion, progress, and bounded waiting using two shared
variables:
•   flag[2] → indicates if a process wants to enter the critical section
•   turn → indicates whose turn it is to enter
🔹 Shared Variables
boolean flag[2];   // initially flag[0] = flag[1] = false
int turn;
🔹 Structure for Process Pi (i = 0 or 1)
do {
flag[i] = true;   // Process Pi wants to enter
turn = j;   // Give chance to other process
while (flag[j] && turn == j);   // Wait if Pj wants to enter and
it's Pj's turn
// Critical Section
flag[i] = false;   // Exit section
// Remainder Section
} while (true);
(where j = 1 - i)
********** 28 **********
--- page 29 ---
🔹 Working Explanation
Consider two processes P0 and P1:
1. Desire to Enter Critical Section
o When a process (say P0) wants to enter, it sets:
▪   flag[0] = true
o This indicates interest in entering the critical section.
2. Turn Assignment
o P0 sets turn = 1 (gives priority to P1).
o This ensures fairness if both processes request
simultaneously.
3. Condition Checking (Busy Waiting)
o P0 checks:
o while (flag[1] && turn == 1);
o This means:
▪   If P1 also wants to enter (flag[1] = true)
▪ AND it is P1’s turn → P0 waits
4. Entering Critical Section
o   If the condition becomes false:
▪   Either P1 is not interested (flag[1] = false)
▪ OR it is not P1’s turn
→ P0 enters the critical section
5. Exiting Critical Section
o After execution, P0 sets:
▪   flag[0] = false
o This allows P1 to enter
🔹 Key Properties Achieved
• Mutual Exclusion
Only one process can enter the critical section at a time.
• Progress
If no process is in the critical section, one of the waiting
processes will be allowed to enter.
• Bounded Waiting
Each process gets a fair chance (due to turn variable).
********** 29 **********
--- page 30 ---
🔹 Example Scenario
• Both P0 and P1 set their flag = true at the same time
• Suppose turn = 1
→ P0 waits, P1 enters
•   After P1 exits, it sets flag[1] = false
→ Now P0 can enter
5. Explain the concept of a page fault and write the steps involved
in handling a page fault?
Page Fault – Concept
A page fault occurs in a paging-based memory management
system when a process tries to access a page that is not
currently present in main memory (RAM) but is available on
secondary storage (disk).
• Each process has a page table with a valid/invalid bit
•   If the bit is invalid, it indicates the page is not in memory
→ This triggers a page fault trap to the operating system
Working of Page Fault (Conceptual View)
********** 30 **********
--- page 31 ---
Steps Involved in Handling a Page Fault
1. Page Access Attempt
o CPU generates a logical address
o Page table is checked for validity
2. Page Fault Detection
o   If the valid bit = 0 (invalid)
→ Hardware triggers a page fault interrupt (trap) to OS
3. Check Validity of Reference
o OS verifies whether the reference is:
▪ Legal (valid page but not in memory) →
proceed
▪   Illegal (invalid access) → terminate process
********** 31 **********

[Text in pictures on this page, read by OCR]
page is on
backing store

operating
system ®
reference
@ trap
load M 4 li
restart | page table
instruction
free frame
reset page bring in
table missing page
physical

memory
--- page 32 ---
4. Locate the Required Page on Disk
o OS finds the required page in secondary storage
(backing store)
5. Find a Free Frame
o   If a free frame is available → use it
o Otherwise → apply a page replacement algorithm (e.g.,
FIFO, LRU)
6. Swap Out (if required)
o   If the selected frame contains a modified page
→ write it back to disk
7. Load Required Page into Memory
o Read the required page from disk into the selected frame
8. Update Page Table
o Set valid bit = 1
o Update frame number for the page
9. Restart the Instruction
o The interrupted instruction is restarted
o This time, execution proceeds successfully
5.Define a file in an operating system. Explain the different types of
files.
Definition of a File in Operating System
A file is a collection of related information stored on secondary
storage (such as a disk), identified by a name, and treated as a
single unit by the operating system.
•   It can store data, programs, or any form of information
•   Files provide a way to store, retrieve, and manage data
permanently
• Each file has attributes such as name, type, size, location, and
permissions
Conceptual View of File System
********** 32 **********
--- page 33 ---
directory directory

file file file

Structures of Directory in Operating System
Two Level ale Root
Master Directory (ESI

Directory J T 3
User fiw file File MMgrm File | File
Directory faivtag Entry Entry Meaney Entry Entry
Files

rhe ats

Ul Suz U3 Files

D3 D4" D5 wm

Directory Single Level Directory

Directory ye methods,txt) os.docx 2.mp4_JTP.txt
Files

D9 DIO
Files
@stop
root | spell bin programs|
stat | mail | dist find | count| hex |reorder e mail
prog | copy | prt exp reorder| list find hex | count

ooo Lf

list obj | spell all last | first

666666

FR ICR QQ I OH
--- page 34 ---
Different Types of Files
Operating systems classify files based on their structure and
purpose:
1. Regular Files (Ordinary Files)
• Contain user data such as text, images, programs, etc.
• Can be text files or binary files
• Examples: .txt, .doc, .exe, .jpg
2. Directory Files
•   Store information about files and subdirectories
• Help in organizing files in a hierarchical structure
• Example: folders in Windows/Linux
3. Special Files (Device Files)
• Represent hardware devices
• Used for input/output operations
• Two types:
o Character Special Files → data handled as a stream
(keyboard, mouse)
o Block Special Files → data handled in blocks (hard disk)
4. FIFO (Named Pipe) Files
• Used for inter-process communication (IPC)
• Data flows in a first-in, first-out manner
5. Symbolic Link Files
• Act as a pointer/reference to another file
• Do not contain actual data, only the path of the original file
********** 34 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper d26ad17a2400

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CSE_DS_7057/Operating Systems/ANS_Operating Systems(702CO1C002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 70.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MASTER OF BUSINESS ADMINISTRATION
IN TECHNOLOGY MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA
Tech (Comp)
Year: II / III / V/Sem 3 Re-exam/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1 A What are the various components of an Operating System? Briefly explain 5
with the help of a diagram.
Explanation of components (any four) 1 mark each (4 Marks)
Diagram   1 mark
The main components of an operating system are:
1. Process Management
o Handles creation, scheduling, and termination of processes.
o Ensures fair CPU allocation among processes.
2. Memory Management
o Manages primary memory allocation and deallocation.
o Keeps track of memory usage and optimizes performance.
3. File Management
o Organizes, stores, retrieves, and manages data in files.
o Maintains directories and provides file access control.
4. Device Management
o Controls and coordinates input/output devices via device
drivers.
o Ensures efficient and conflict-free resource usage.
5. Security and Protection
o Protects data and system resources from unauthorized
access.
o Implements authentication, authorization, and encryption
mechanisms.
********** 1 **********
--- page 2 ---
B Analyze the code for Process Pi and Pj and state whether it satisfies the 5
three requirements for the solution to the critical section problem or not.
Justify your answer.
For process Pi:
do {
flag[i] = true;
turn = j;
while (flag[j] && turn == j);
// Critical Section
flag[i] = false;
// Remainder Section
} while (true);
For process Pj:
do {
flag[j] = true;
turn = i;
while (flag[i] && turn == i);
// Critical Section
flag[j] = false;
// Remainder Section
} while (true);
Final verdict: 2 marks
Justification each condition: 1 Mark (3 marks)
Yes, it satifies all the three conditions of mutual exclusion.
A. Mutual exclusion is preserved
Pi enters CS only if:
either flag[j] = false or turn = i
B. Progress requirement is satisfied: If a process wants to enter the
critical section, it waits only if the other process is inside or waiting
to enter, and it is the other process’s turn.
If the other process is not interested (flag[j] == false), then the first
process proceeds immediately without waiting.
Also, the turn variable guarantees that the processes alternate access
if both want to enter, so no process can block the other indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
user and other system programs

GUI touch screen | command line

user interfaces

system calls

program vO file a resource
communication

. A a accounting
execution operations systems allocation

protection
and
security

error
detection
services

operating system

hardware
--- page 3 ---
C. Bounded-waiting requirement is met: The turn variable acts as a fair
"token" passed between the two processes, ensuring that after one
process finishes, the other will eventually get the turn.
C Describe the process of deadlock recovery after detection. What are the
common methods used? Explain any two.
Deadlock Recovery 1 mark
Methods 4 marks
Process of Deadlock Recovery (1 Marks)
Once a deadlock is detected (usually using the resource allocation graph or
Banker’s algorithm), the OS performs the following steps:
1. Identify deadlocked processes and resources.
2. Select a recovery method — terminate processes, preempt
resources, or roll back processes.
3. Recover the system by releasing held resources and restarting
affected processes.
4. Resume normal operation.
Common Methods of Deadlock Recovery
The two main categories are:
1. Process Termination — killing one or more processes involved in
the deadlock.
2. Resource Preemption — temporarily taking resources away from
processes.
Other less common methods:
• Process Rollback (restore to a safe checkpoint).
• Manual Intervention (in simple or embedded systems).
(i) Process Termination (2 Marks)
• Concept:
Abort one or more processes involved in the deadlock until the cycle
is broken.
• Approaches:
1. Abort all deadlocked processes.
▪ Simple but costly; results in loss of work.
2. Abort processes one at a time until the deadlock cycle is
resolved.
•   Selection   Criteria:
When choosing which process to terminate, the OS considers:
1. Process priority and importance.
2. Amount of CPU time consumed.
3. Number and type of resources held.
4. Whether the process can be restarted easily.
• Advantages:
1. Straightforward and guaranteed recovery.
• Disadvantages:
1. May lead to loss of significant computation progress.
2. System performance temporarily degrades.
(ii) Resource Preemption (2 Marks)
• Concept:
Temporarily take away (preempt) resources from some processes
and give them to others to break the deadlock.
********** 3 **********
--- page 4 ---
• Steps Involved:
1. Select a victim process – the one whose resource preemption
has the least cost.
2. Save its state (checkpoint) – so it can be restarted later.
3. Reassign its resources to other waiting processes.
•   Challenges:
1. Rollback: The victim process must be rolled back to a safe
state.
2. Starvation: A process may be repeatedly chosen as a victim;
hence, the OS must keep track of how often each process is
preempted.
• Advantages:
1. Allows partial progress of other processes.
• Disadvantages:
1. Complex to implement and may lead to instability if done
repeatedly.
D Describe the concept of I/O management in an operating system and apply
your knowledge to identify key factors that can enhance I/O performance.
I/O Management 2 Marks
Factors 3 Marks (at least 3)
I/O management is a major component of operating system design that
handles the interaction between the computer system and I/O devices.
Key Components:
•   Ports, Buses, Controllers: Connect various devices to the system
• Device Drivers: Encapsulate device-specific details and present
uniform device-access interface to I/O subsystem
• I/O Hardware: Manages incredible variety of devices (storage,
transmission, human-interface)
I/O Methods:
•   Polling: CPU repeatedly checks device status (inefficient for slow
devices)
•   Interrupts: Device signals CPU when ready (efficient, used for
time-sensitive operations)
• DMA (Direct Memory Access): Transfers data directly between
device and memory without CPU involvement
I/O Operations:
• Blocking I/O: Process suspended until I/O completed
• Nonblocking I/O: Returns immediately with available data
• Asynchronous I/O: Process continues while I/O executes
Factors for Improving I/O Performance
1. Reduce Context Switches
• Minimize switching between processes during I/O operations
2. Reduce Data Copying
• Minimize copying data between kernel and user space
3. Reduce Interrupts
• Use large transfers instead of multiple small ones
• Employ smart controllers
• Use polling when appropriate
4. Use DMA (Direct Memory Access)
• Allow devices to transfer data directly to/from memory
********** 4 **********
--- page 5 ---
• Frees CPU from data transfer burden
5. Use Smarter Hardware Devices
•   Intelligent controllers with built-in processing capabilities
6. Balance System Resources
• Balance CPU, memory, bus, and I/O performance for highest
throughput
7. Move User-mode Processes to Kernel Threads
• Reduces overhead for frequently used I/O operations
8. Implement Efficient Buffering and Caching
• Buffer data to handle speed/size mismatches
• Cache frequently accessed data on faster devices
2 A Examine the synchronization problem in operating systems, identifying the
challenges it creates. Analyse how counting semaphores provide a
structured solution and resolve these issues in the Readers–Writers
problem.
Explain Synchronization Problem in Detail [4 marks]
Readers-Writers Problem [6 marks]
The Synchronization Problem arises in a multi-process or multi-threaded
environment when multiple processes concurrently access and manipulate
shared data. The core issue is that the final result of the execution depends
on the specific order in which instructions are interleaved, leading to
unpredictable and inconsistent results. This is known as a race condition.
Causes and Consequences:
1. Race Condition: Occurs when several processes access and modify
the same shared data concurrently, and the outcome of the execution
depends on the order of access.
2. Data Inconsistency: The primary consequence is that the shared data
may end up in a corrupted or inconsistent state.
Example (The Critical Section Problem): A simple counter shared by two
threads, one incrementing and the other decrementing. The operations
(Read → Modify → Write) are not atomic. If the operations are interrupted
and interleaved, the final count can be incorrect (e.g., instead of
100→101→100, it might become 100→101→101).
Requirements for a Correct Solution:
1. Mutual Exclusion: Only one process can be executing in its critical
section at any time.
2. Progress: If no process is executing in its critical section and some
processes wish to enter, then only those processes not in their
remainder sections can participate in deciding which will enter next,
and this selection cannot be postponed indefinitely.
3. Bounded Waiting: There must be a limit on the number of times
other processes are allowed to enter their critical sections after a
process has made a request to enter its critical section and before
that request is granted.
B. Counting Semaphore for Readers-Writers Problem [6 marks]
The Readers-Writers Problem is a classic synchronization problem where
multiple processes try to access a shared database.
● Readers only read the data and can do so concurrently.
● Writers modify the data and must have exclusive access (no other
reader or writer allowed).
********** 5 **********
--- page 6 ---
A Counting Semaphore (and a Binary/Mutex semaphore) can be used to
manage this access
Writer Process Logic: The writer needs exclusive access. It only needs to
wait on the general lock (wrt).
do {
wait(wrt);
// Writing is performed
signal(wrt);
} while (TRUE);
Reader Process Logic: Readers need to coordinate using readcount and
the wrt lock.
do {
wait(mutex);   // 1. Lock the readcount variable
readcount++;
if (readcount == 1) {   // 2. First reader locks out the writer
wait(wrt);
}
signal(mutex);   // 3. Unlock the readcount variable
// Reading is performed
wait(mutex);   // 4. Lock the readcount variable
readcount--;
if (readcount == 0) {   // 5. Last reader signals the writer
signal(wrt);
}
signal(mutex);   // 6. Unlock the readcount variable
} while (TRUE);
B Consider the following set of processes, each with varying arrival times
and burst times.
Process   Arrival Time   Burst Time
P1   0   7
P2   2   4
P3   4   1
P4   5   4
P5   6   3
i. Using the SRTF scheduling algorithm, determine the average
waiting time and average response time.
ii. Using the Round-Robin scheduling algorithm with time quantum =
3, determine the average waiting time and average response time.
********** 6 **********
--- page 7 ---
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
3 A Consider the following snapshot of a system running 5 processes:
Pro- Allocation   Max   Available
cess A   B   C   D A   B   C D A B   C D
P0   0   0   1   2 0   0   1   2 1   5   2   0
P1   1   0   0   0 1   7   5   0
P2   1   3   5   4 2   3   5   6
P3   0   6   3   2 0   6   5   2
********** 7 **********
--- page 8 ---
P4   0   0   1   4 0   6   5   6
Answer the following: -
i. How many resources of type A, B, C, D are there?
ii.   Calculate the need matrix?
iii.   Determine if the system is safe or not.
iv.   What will happen if the resource request (0, 4, 2,0) for process P1
arrive, can the system accept this request immediately?
Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks
Safe Sequence 3 Marks
Additional Request 3 Marks
The total number of resources of each type is calculated as:
Total = Allocation (sum) + Available
• A = 2 + 1 = 3
• B = 9 + 5 = 14
• C = 10 + 2 = 12
• D = 12 + 0 = 12
Thus, total system resources = (3, 14, 12, 12).
vi) Need Matrix
Process   A   B   C   D
P0   0   0   0   0
P1   0   7   5   0
P2   1   0   0   2
P3   0   0   2   0
P4   0   6   4   2
vii) Safe State Check
Starting with Available = (1, 5, 2, 0):
• P0 runs → Work = (1, 5, 3, 2)
• P3 runs → Work = (1, 11, 6, 4)
• P2 runs → Work = (2, 14, 11, 8)
• P4 runs → Work = (2, 14, 12, 12)
• P1 runs → Work = (3, 14, 12, 12)
Safe sequence = <P0, P3, P2, P4, P1>. Therefore, the system is SAFE.
viii) Resource Request (0, 4, 2, 0) by P1
********** 8 **********
--- page 9 ---
• Request (0, 4, 2, 0) ≤ Need(P1) = (0, 7, 5, 0) ✔
• Request (0, 4, 2, 0) ≤ Available (1, 5, 2, 0) ✔
After tentative allocation: Available = (1, 1, 0, 0).
Safety test sequence:
• P0 → Work = (1, 1, 1, 2)
• P2 → Work = (2, 4, 6, 6)
• P3 → Work = (2, 10, 9, 8)
• P4 → Work = (2, 10, 10, 12)
• P1 → completes.
Safe sequence = <P0, P2, P3, P4, P1>. Hence, the request CAN be
granted immediately.
B Describe the concept and working of a Translation Lookaside Buffer (TLB) 10
in a paging system. Explain how address translation is carried out with and
without TLB.
Definition and Need of TLB (2 Marks)
address translation without TLB (4 Marks)
address translation with TLB (4 Marks)
• A Translation Lookaside Buffer (TLB) is a special high-speed cache
that stores recent translations of virtual page numbers (VPNs) to
physical frame numbers (PFNs).
•   In a paging system, every memory access requires a page table lookup
to translate the virtual address into a physical address.
• This lookup takes extra time (additional memory access), which slows
down the system.
• The TLB reduces this delay by caching frequently used page table
entries — providing fast access to address translations.
Address translation is carried out with TLB.
********** 9 **********

[Text in pictures on this page, read by OCR]
frame e

logical address physical address 0x000
frame f
cpu slp | a |
p — Oxfff
f frame g

physical memory

page table
--- page 10 ---
Address translation is carried without TLB.
4 A Provide a comparative analysis of the Monolithic and Layered architectures 10
of Operating Systems. Include appropriate diagrams to support your
explanation.
Monolithic Architecture (3 Marks)
Layered Architecture (3 Marks)
Comparative Analysis (4 Marks)
Operating System architecture defines the structure and organization of the
OS components and their interaction with each other and hardware.
Two commonly used architectures are Monolithic and Layered
architectures.
Monolithic Architecture (3 Marks)
Explanation:
•   In a monolithic system, the entire operating system is working in a
single kernel space.
•   All system components such as   file management, process
scheduling, memory management, and device drivers are integrated
into one large block of code that runs in supervisor mode.
•   It provides high performance because there are no inter-layer
overheads, but poor modularity and difficult debugging.
Diagram:
********** 10 **********

[Text in pictures on this page, read by OCR]
logical

address
CPU +> pid

page frame

number number

E TLB hit physical

BI address
Lt | 4d }—

TLB

TLB miss

a physical
memory

page table
--- page 11 ---
Advantages:
• High execution speed (no layer overhead).
•   Efficient direct access to hardware.
Disadvantages:
•   Difficult to maintain and debug.
• Poor security and modularity—failure in one module may crash the
entire system.
Examples:
MS-DOS, UNIX (early versions), Linux (partially monolithic).
Layered Architecture (3 Marks)
Explanation:
•   In layered architecture, the OS is divided into multiple layers, each
built upon the lower one.
• Each layer performs specific functions and interacts only with its
adjacent layers.
• The bottom layer deals with hardware, while the top layer provides
user interfaces.
Diagram:
********** 11 **********

[Text in pictures on this page, read by OCR]
applications

glibc standard c library

system-call interface
file CPU
systems scheduler
networks memory
(TCP/IP) manager
block character
devices devices

device drivers

hardware
--- page 12 ---
Advantages:
•   Better modularity and maintainability.
•   Easier to test and debug individual layers.
• Higher security and reliability due to restricted communication.
Disadvantages:
• Slower execution due to layer-to-layer communication overhead.
•   Difficult to design and define proper boundaries between layers.
Examples:
THE Operating System, Windows NT, OS/2.
Comparative Analysis (4 Marks)
Feature   Monolithic OS   Layered OS
Structure   Single large kernel Multiple   layers   with   clear
interfaces
Performance   High   (no Slightly slower (due to layering)
overhead)
Modularity   Poor   Excellent
Maintainability Difficult   Easier to maintain and modify
Security   Low   (shared High   (restricted   inter-layer
kernel)   access)
Examples   MS-DOS, UNIX   Windows NT, THE OS
Conclusion:
Monolithic architecture emphasizes performance, whereas layered
architecture   emphasizes   modularity,   reliability,   and   security.
Modern operating systems often adopt a hybrid approach, combining the
speed of monolithic design with the structure of layered models.
B A disk queue with requests on cylinders 85, 170, 45, 130, 25, 115, 72, 58 10
needs to be serviced. The disk head is initially at cylinder 60, and the disk
has cylinders numbered 0-199. Calculate the total head movement for:
1. FCFS
2. SSTF
3. SCAN (assuming initial direction towards cylinder 199)
4. C-SCAN (assuming initial direction towards cylinder 199)
Compare the performance of each algorithm and determine which suits best
for this scenario.
********** 12 **********

[Text in pictures on this page, read by OCR]
application file device user
program system driver mode

messages: messages

CPU
scheduling

memory
managment

kernel
mode

interprocess
communication

microkernel

hardware
--- page 13 ---
Each Algorithm 2 Marks
Comparison 2 Marks

RK KKK RK KK 13 2h KKK RK Kk KK
--- page 14 ---
Best Algorithm for This Scenario:
SSTF provides the best performance with only 180 cylinders of movement,
making it ideal for this scenario where minimizing seek time is the priority
and the request queue is relatively small, reducing starvation risk.
5 A Describe the concept of monitors in process synchronization with internal 10
structure and functioning. Explain how monitors manage process
coordination using condition variables and synchronization primitives.
Concept of Monitors (2 Marks)
Internal Structure of a Monitor (4 Marks)
Functioning and Coordination (4 Marks)
In concurrent programming, monitors are high-level synchronization
constructs that provide a convenient and safe mechanism for process
coordination.
They encapsulate shared data, the procedures that operate on that data, and
the synchronization between concurrent processes — all within a single
module.
Monitors eliminate many of the errors possible when using low-level
primitives such as semaphores.
A monitor is a software module with:
• Shared data variables.
• A set of procedures (only one process can execute inside the
monitor at a time).
• Condition variables for process synchronization.
It ensures mutual exclusion automatically — no two processes can execute
monitor procedures simultaneously.
********** 14 **********

[Text in pictures on this page, read by OCR]
Performance Comparison

Algorithm Total Movement Characteristics

FCFS 572 Simple, fair, but high seek time

SSTF 188 Minimal movement, risk of starvation
SCAN 313 Fair, predictable, moderate performance

C-SCAN 396 More uniform wait time, higher movement
--- page 15 ---
Internal Structure of a Monitor (4 Marks)
Components:
1. Shared Data: Variables accessible only through monitor procedures.
2. Procedures: Define operations that can be performed on shared data.
3. Initialization Code: Sets up initial values for data and conditions.
4. Condition Variables: Used for process synchronization (e.g., x, y).
Pseudocode syntax of a monitor:
monitor monitor-name
{
// shared variable declarations
function P1 (…) { …. }
function P2 (…) { …. }
function Pn (…) {……}
initialization code (…) { … }
}
Diagram of Monitor Structure (1 Mark)
+-----------------------------------+
Functioning and Coordination (4 Marks)
Condition Variables and Synchronization:
• Condition variables allow a process to wait for a certain condition
to become true.
• Two basic operations are used:
o wait(c) → Process is suspended until another process signals
condition c.
o signal(c) → Wakes up one waiting process on condition c.
• Mutual exclusion: Achieved automatically; only one process
executes within the monitor.
•   Synchronization: Managed through wait and signal on condition
variables.
• No busy waiting: Blocked processes are placed in a waiting queue
inside the monitor.
Advantages of Monitors
********** 15 **********
--- page 16 ---
• Provides structured and safer synchronization compared to
semaphores.
•   Eliminates errors like deadlocks and race conditions caused by
improper semaphore use.
• Promotes modularity and clarity in concurrent program design.
B Explain how fragmentation affects memory management in operating 10
systems and illustrate the different types of fragmentation with suitable
example. A system has five memory partitions of sizes 110 KB, 480 KB,
210   KB,   350   KB,   and   140   KB   respectively.
A sequence of processes arrives for allocation in the following order: P1 =
100 KB, P2 = 200 KB, P3 = 300 KB, P4 = 140 KB, and P5 = 50 KB.
Considering Contiguous memory allocation, show the final process-to-
partition allocations using First-Fit, Best-Fit, and Worst-Fit memory
allocation strategies.
Marks Distribution:
Fragmentation 2 Marks
Types 2 marks
First Fit – 2 marks
Best Fit – 2 marks
Worst Fit – 2 marks
Fragmentation is a memory management problem that occurs when free memory
space is broken into small, non-contiguous blocks over time. It reduces the
system’s ability to allocate large continuous memory blocks to new processes,
even if total free memory is sufficient.
Fragmentation affects memory utilization and system performance, leading to
inefficient use of available RAM.
Types of Fragmentation
(a) Internal Fragmentation
Definition: Occurs when a fixed-sized memory block allocated to a process is
larger than the process’s actual memory requirement.
Cause: Fixed partitioning or paging schemes with block sizes larger than needed.
Effect: Wasted space inside the allocated partition.
Example:
Suppose a system allocates 4 KB blocks, and a process needs only 3.6 KB.
→ Unused memory = 0.4 KB per process
This 0.4 KB inside the allocated block is internally fragmented.
External Fragmentation
Definition: Occurs when total free memory exists but is scattered in non-
contiguous blocks, preventing allocation of large processes.
Cause: Dynamic memory allocation where processes are loaded and removed
frequently.
Effect: Wasted space outside allocated partitions.
Example:
Assume memory = 100 MB total. Free blocks: 20 MB + 15 MB + 10 MB (non-
contiguous).
********** 16 **********
--- page 17 ---
A process requesting 40 MB cannot be allocated, though 45 MB is free in total.
6 A   I.   Apply your understanding of process scheduling to compare Long- 10
term and Short-term schedulers in terms of their purpose, execution
frequency, speed, alternate names, and where process selection
occurs (main or secondary memory).
II.   Apply the concepts of process scheduling to justify why time-
sharing systems rely more on Short-term scheduler, while batch-
processing systems depend more on Long-term scheduler.
I.   5 Marks (One mark for each criteria)
II.   5 Marks
Solution:
i. Following are the differences between a LTS and STS:- (5 marks)
********** 17 **********
--- page 18 ---
Aspect   Long-Term Scheduler   Short-Term Scheduler
Frequency   Runs less frequently.   Runs very frequently.
Speed   Slower, as it involves   Faster, as it focuses
more complex decision-   solely on CPU allocation.
making and memory
checks.
Process   Selects processes from the   Selects processes from
selection   job pool (secondary   the ready queue (main
location   memory).   memory).
Alternate   Job Scheduler   CPU Scheduler
Name
Purpose   Balances I/O-bound and   Maximizes CPU
CPU-bound processes.   utilization and minimizes
process waiting times.
ii. Time-sharing: Many interactive users → responsiveness is critical.
The short-term scheduler (CPU scheduler) decides which process
runs next very frequently (milliseconds). Long-term scheduler is
less relevant because new jobs are admitted immediately.
Batch system: Jobs are large and submitted in bulk. The long-term
scheduler regulates how many jobs enter memory, controlling
degree of multiprogramming. If too many are admitted, system
thrashes; if too few, CPU underutilizes.
(5 marks)
B A system has 3 frames for storing process pages in main memory. Assume
that all the page frames are initially empty. Consider the page reference
string given below:
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Compute the number of page faults and show frame contents step-by-step
for:
(a) FIFO,
(b) LRU,
(c) Optimal.
Also state which algorithm gave the fewest faults.
Marks Distribution:
(FIFO: 3 marks, LRU: 3 marks, Optimal: 3 marks)
Also state which algorithm gave the fewest faults and why.(1 marks)
********** 18 **********
--- page 19 ---
Reference string length = 12. Frames = 3.
(a) FIFO (First-In, First-Out)
Frames after
Step   Ref   Fault?
step (f1,f2,f3)
1   1   1, - , -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
4   4   4, 2, 3 (1 out) Y
5   1   4, 1, 3 (2 out) Y
6   2   4, 1, 2 (3 out) Y
7   5   5, 1, 2 (4 out) Y
8   1   5, 1, 2   N
9   2   5, 1, 2   N
10   3   5, 3, 2 (1 out) Y
11   4   5, 3, 4 (2 out) Y
12   5   5, 3, 4   N
Total page faults (FIFO): 9.
(b) LRU (Least Recently Used)
LRU replaces the page that has not been used for the longest time.
Step   Ref   Frames after step Fault? Comment
1   1   1, -, -   Y   load 1
2   2   1, 2, -   Y   load 2
3   3   1, 2, 3   Y   load 3
4, 2, 3 (1 was
4   4   Y
LRU)
4, 1, 3 (2 LRU
5   1   Y
replaced)
4, 1, 2 (3 LRU
6   2   Y
replaced)
********** 19 **********
--- page 20 ---
5, 1, 2 (4 LRU
7   5   Y
replaced)
8   1   5, 1, 2   N
9   2   5, 1, 2   N
3, 1, 2 (5 LRU
10   3   Y
replaced)
3, 4, 2 (1 LRU
11   4   Y
replaced)
3, 4, 5 (2 LRU
12   5   Y
replaced)
Total page faults (LRU): 10.
(c) Optimal (Belady’s optimal algorithm) — replace the page that will not
be used for the longest time in the future.
Frames after
Step   Ref   Fault?
step
1   1   1, -, -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
1, 2, 4 (3
replaced; will be
4   4   used later   Y
sooner than 1 or
2?)*
5   1   1, 2, 4   N
6   2   1, 2, 4   N
1, 2, 5 (4
replaced: 4 next
used at step 11;
7   5   Y
1 and 2 are
needed earlier at
steps 8 and 9)
8   1   1, 2, 5   N
9   2   1, 2, 5   N
3, 2, 5 (1
replaced; 1 next
10   3   Y
used later than 2
or 5)
********** 20 **********
--- page 21 ---
3, 4, 5 (2
11   4   Y
replaced)
12   5   3, 4, 5   N
Total page faults (Optimal): 7.
Optimal gives the fewest faults (7) because it uses future knowledge. For
real systems we cannot implement Optimal, but it is used as a baseline. In
this case FIFO (9) beats LRU (10) — showing that LRU is usually good
but not always strictly better than FIFO, and that algorithms’ effectiveness
depends on the reference string.
7 A Analyze the Resource Allocation Graph
i)   Write resource allocated and requested table
ii)   Find if there is a deadlock or not? If there is no deadlock then
what will be the sequence of the process to get executed?
iii)   What will happen if one instance of resource R3 is removed
from the system.
I.   4 marks
II.   4 Marks
III.   2 Marks
i)
********** 21 **********
--- page 22 ---
II) System is in Safe State. Safe Sequence: P2, P0, P1, P3
III) There will be a deadlock in the system.
B Explain user level and kernel level threads. Which one are more light 5
weight and independent?
User and Kernel Thread 3 marks
Explanation 2 marks
Solution: User-level threads are managed entirely by a user-level thread
library without direct involvement from the operating system's kernel.
The kernel is unaware of their existence and treats the entire process
containing these threads as a single unit of execution.
(1.5 marks)
Kernel-level threads are managed directly by the operating system's
kernel. The kernel is aware of each individual kernel thread and handles
their creation, scheduling, and management.   (1.5 marks)
User-level threads are managed by a user-level thread library, making
them more lightweight as they don't require kernel intervention and offer
faster context switching, but are less independent as a blocking thread can
block the entire process. Kernel-level threads are managed by the
operating system, are more independent because they can take advantage
of multiple CPUs and are not tied to a single process's blocking state but
are more heavyweight due to the overhead of kernel mode transitions and
are slower to create and switch.
(2 marks)
C   Differentiate between sequential access and direct access methods for files. 5
Provide examples of applications where each access method would be
preferred.
Difference 4 marks
Example 1 marks
Sequential Access In sequential access, data in a file is processed in
order, one record or byte after the next. The operations typically used are
read next and write next. Repositioning within the file usually requires a
Reset (rewind) operation to go back to the beginning.
********** 22 **********
--- page 23 ---
Direct Access Direct access views a file as a numbered sequence of fixed-
length logical records. This method allows for immediate, random access
to any part of the file. Operations include explicitly reading or writing
record number (read n, write n), and moving the file pointer directly to
record (position to n).
Application Preference:
Sequential Access Preference This method is preferred for applications
where files must be processed entirely from beginning to end. Examples
include simple text files, log files (where records are appended
chronologically), and source code files read by a compiler.
Direct Access Preference Direct access is preferred for applications that
require quick, random retrieval and update of specific records. A prime
example is an Indexed/Relative File system, commonly used in databases
or any system (like a customer database or airline reservation system)
where a record must be accessed by its index or relative block number.
********** 23 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 71fb2a817037

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CS_7055/Operating Systems/ANS_Operating Systems(702CO1C002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 70.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MASTER OF BUSINESS ADMINISTRATION
IN TECHNOLOGY MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA
Tech (Comp)
Year: II / III / V/Sem 3 Re-exam/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1 A What are the various components of an Operating System? Briefly explain 5
with the help of a diagram.
Explanation of components (any four) 1 mark each (4 Marks)
Diagram   1 mark
The main components of an operating system are:
1. Process Management
o Handles creation, scheduling, and termination of processes.
o Ensures fair CPU allocation among processes.
2. Memory Management
o Manages primary memory allocation and deallocation.
o Keeps track of memory usage and optimizes performance.
3. File Management
o Organizes, stores, retrieves, and manages data in files.
o Maintains directories and provides file access control.
4. Device Management
o Controls and coordinates input/output devices via device
drivers.
o Ensures efficient and conflict-free resource usage.
5. Security and Protection
o Protects data and system resources from unauthorized
access.
o Implements authentication, authorization, and encryption
mechanisms.
********** 1 **********
--- page 2 ---
B Analyze the code for Process Pi and Pj and state whether it satisfies the 5
three requirements for the solution to the critical section problem or not.
Justify your answer.
For process Pi:
do {
flag[i] = true;
turn = j;
while (flag[j] && turn == j);
// Critical Section
flag[i] = false;
// Remainder Section
} while (true);
For process Pj:
do {
flag[j] = true;
turn = i;
while (flag[i] && turn == i);
// Critical Section
flag[j] = false;
// Remainder Section
} while (true);
Final verdict: 2 marks
Justification each condition: 1 Mark (3 marks)
Yes, it satifies all the three conditions of mutual exclusion.
A. Mutual exclusion is preserved
Pi enters CS only if:
either flag[j] = false or turn = i
B. Progress requirement is satisfied: If a process wants to enter the
critical section, it waits only if the other process is inside or waiting
to enter, and it is the other process’s turn.
If the other process is not interested (flag[j] == false), then the first
process proceeds immediately without waiting.
Also, the turn variable guarantees that the processes alternate access
if both want to enter, so no process can block the other indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
user and other system programs

GUI touch screen | command line

user interfaces

system calls

program vO file a resource
communication

. A a accounting
execution operations systems allocation

protection
and
security

error
detection
services

operating system

hardware
--- page 3 ---
C. Bounded-waiting requirement is met: The turn variable acts as a fair
"token" passed between the two processes, ensuring that after one
process finishes, the other will eventually get the turn.
C Describe the process of deadlock recovery after detection. What are the
common methods used? Explain any two.
Deadlock Recovery 1 mark
Methods 4 marks
Process of Deadlock Recovery (1 Marks)
Once a deadlock is detected (usually using the resource allocation graph or
Banker’s algorithm), the OS performs the following steps:
1. Identify deadlocked processes and resources.
2. Select a recovery method — terminate processes, preempt
resources, or roll back processes.
3. Recover the system by releasing held resources and restarting
affected processes.
4. Resume normal operation.
Common Methods of Deadlock Recovery
The two main categories are:
1. Process Termination — killing one or more processes involved in
the deadlock.
2. Resource Preemption — temporarily taking resources away from
processes.
Other less common methods:
• Process Rollback (restore to a safe checkpoint).
• Manual Intervention (in simple or embedded systems).
(i) Process Termination (2 Marks)
• Concept:
Abort one or more processes involved in the deadlock until the cycle
is broken.
• Approaches:
1. Abort all deadlocked processes.
▪ Simple but costly; results in loss of work.
2. Abort processes one at a time until the deadlock cycle is
resolved.
•   Selection   Criteria:
When choosing which process to terminate, the OS considers:
1. Process priority and importance.
2. Amount of CPU time consumed.
3. Number and type of resources held.
4. Whether the process can be restarted easily.
• Advantages:
1. Straightforward and guaranteed recovery.
• Disadvantages:
1. May lead to loss of significant computation progress.
2. System performance temporarily degrades.
(ii) Resource Preemption (2 Marks)
• Concept:
Temporarily take away (preempt) resources from some processes
and give them to others to break the deadlock.
********** 3 **********
--- page 4 ---
• Steps Involved:
1. Select a victim process – the one whose resource preemption
has the least cost.
2. Save its state (checkpoint) – so it can be restarted later.
3. Reassign its resources to other waiting processes.
•   Challenges:
1. Rollback: The victim process must be rolled back to a safe
state.
2. Starvation: A process may be repeatedly chosen as a victim;
hence, the OS must keep track of how often each process is
preempted.
• Advantages:
1. Allows partial progress of other processes.
• Disadvantages:
1. Complex to implement and may lead to instability if done
repeatedly.
D Describe the concept of I/O management in an operating system and apply
your knowledge to identify key factors that can enhance I/O performance.
I/O Management 2 Marks
Factors 3 Marks (at least 3)
I/O management is a major component of operating system design that
handles the interaction between the computer system and I/O devices.
Key Components:
•   Ports, Buses, Controllers: Connect various devices to the system
• Device Drivers: Encapsulate device-specific details and present
uniform device-access interface to I/O subsystem
• I/O Hardware: Manages incredible variety of devices (storage,
transmission, human-interface)
I/O Methods:
•   Polling: CPU repeatedly checks device status (inefficient for slow
devices)
•   Interrupts: Device signals CPU when ready (efficient, used for
time-sensitive operations)
• DMA (Direct Memory Access): Transfers data directly between
device and memory without CPU involvement
I/O Operations:
• Blocking I/O: Process suspended until I/O completed
• Nonblocking I/O: Returns immediately with available data
• Asynchronous I/O: Process continues while I/O executes
Factors for Improving I/O Performance
1. Reduce Context Switches
• Minimize switching between processes during I/O operations
2. Reduce Data Copying
• Minimize copying data between kernel and user space
3. Reduce Interrupts
• Use large transfers instead of multiple small ones
• Employ smart controllers
• Use polling when appropriate
4. Use DMA (Direct Memory Access)
• Allow devices to transfer data directly to/from memory
********** 4 **********
--- page 5 ---
• Frees CPU from data transfer burden
5. Use Smarter Hardware Devices
•   Intelligent controllers with built-in processing capabilities
6. Balance System Resources
• Balance CPU, memory, bus, and I/O performance for highest
throughput
7. Move User-mode Processes to Kernel Threads
• Reduces overhead for frequently used I/O operations
8. Implement Efficient Buffering and Caching
• Buffer data to handle speed/size mismatches
• Cache frequently accessed data on faster devices
2 A Examine the synchronization problem in operating systems, identifying the
challenges it creates. Analyse how counting semaphores provide a
structured solution and resolve these issues in the Readers–Writers
problem.
Explain Synchronization Problem in Detail [4 marks]
Readers-Writers Problem [6 marks]
The Synchronization Problem arises in a multi-process or multi-threaded
environment when multiple processes concurrently access and manipulate
shared data. The core issue is that the final result of the execution depends
on the specific order in which instructions are interleaved, leading to
unpredictable and inconsistent results. This is known as a race condition.
Causes and Consequences:
1. Race Condition: Occurs when several processes access and modify
the same shared data concurrently, and the outcome of the execution
depends on the order of access.
2. Data Inconsistency: The primary consequence is that the shared data
may end up in a corrupted or inconsistent state.
Example (The Critical Section Problem): A simple counter shared by two
threads, one incrementing and the other decrementing. The operations
(Read → Modify → Write) are not atomic. If the operations are interrupted
and interleaved, the final count can be incorrect (e.g., instead of
100→101→100, it might become 100→101→101).
Requirements for a Correct Solution:
1. Mutual Exclusion: Only one process can be executing in its critical
section at any time.
2. Progress: If no process is executing in its critical section and some
processes wish to enter, then only those processes not in their
remainder sections can participate in deciding which will enter next,
and this selection cannot be postponed indefinitely.
3. Bounded Waiting: There must be a limit on the number of times
other processes are allowed to enter their critical sections after a
process has made a request to enter its critical section and before
that request is granted.
B. Counting Semaphore for Readers-Writers Problem [6 marks]
The Readers-Writers Problem is a classic synchronization problem where
multiple processes try to access a shared database.
● Readers only read the data and can do so concurrently.
● Writers modify the data and must have exclusive access (no other
reader or writer allowed).
********** 5 **********
--- page 6 ---
A Counting Semaphore (and a Binary/Mutex semaphore) can be used to
manage this access
Writer Process Logic: The writer needs exclusive access. It only needs to
wait on the general lock (wrt).
do {
wait(wrt);
// Writing is performed
signal(wrt);
} while (TRUE);
Reader Process Logic: Readers need to coordinate using readcount and
the wrt lock.
do {
wait(mutex);   // 1. Lock the readcount variable
readcount++;
if (readcount == 1) {   // 2. First reader locks out the writer
wait(wrt);
}
signal(mutex);   // 3. Unlock the readcount variable
// Reading is performed
wait(mutex);   // 4. Lock the readcount variable
readcount--;
if (readcount == 0) {   // 5. Last reader signals the writer
signal(wrt);
}
signal(mutex);   // 6. Unlock the readcount variable
} while (TRUE);
B Consider the following set of processes, each with varying arrival times
and burst times.
Process   Arrival Time   Burst Time
P1   0   7
P2   2   4
P3   4   1
P4   5   4
P5   6   3
i. Using the SRTF scheduling algorithm, determine the average
waiting time and average response time.
ii. Using the Round-Robin scheduling algorithm with time quantum =
3, determine the average waiting time and average response time.
********** 6 **********
--- page 7 ---
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
3 A Consider the following snapshot of a system running 5 processes:
Pro- Allocation   Max   Available
cess A   B   C   D A   B   C D A B   C D
P0   0   0   1   2 0   0   1   2 1   5   2   0
P1   1   0   0   0 1   7   5   0
P2   1   3   5   4 2   3   5   6
P3   0   6   3   2 0   6   5   2
********** 7 **********
--- page 8 ---
P4   0   0   1   4 0   6   5   6
Answer the following: -
i. How many resources of type A, B, C, D are there?
ii.   Calculate the need matrix?
iii.   Determine if the system is safe or not.
iv.   What will happen if the resource request (0, 4, 2,0) for process P1
arrive, can the system accept this request immediately?
Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks
Safe Sequence 3 Marks
Additional Request 3 Marks
The total number of resources of each type is calculated as:
Total = Allocation (sum) + Available
• A = 2 + 1 = 3
• B = 9 + 5 = 14
• C = 10 + 2 = 12
• D = 12 + 0 = 12
Thus, total system resources = (3, 14, 12, 12).
vi) Need Matrix
Process   A   B   C   D
P0   0   0   0   0
P1   0   7   5   0
P2   1   0   0   2
P3   0   0   2   0
P4   0   6   4   2
vii) Safe State Check
Starting with Available = (1, 5, 2, 0):
• P0 runs → Work = (1, 5, 3, 2)
• P3 runs → Work = (1, 11, 6, 4)
• P2 runs → Work = (2, 14, 11, 8)
• P4 runs → Work = (2, 14, 12, 12)
• P1 runs → Work = (3, 14, 12, 12)
Safe sequence = <P0, P3, P2, P4, P1>. Therefore, the system is SAFE.
viii) Resource Request (0, 4, 2, 0) by P1
********** 8 **********
--- page 9 ---
• Request (0, 4, 2, 0) ≤ Need(P1) = (0, 7, 5, 0) ✔
• Request (0, 4, 2, 0) ≤ Available (1, 5, 2, 0) ✔
After tentative allocation: Available = (1, 1, 0, 0).
Safety test sequence:
• P0 → Work = (1, 1, 1, 2)
• P2 → Work = (2, 4, 6, 6)
• P3 → Work = (2, 10, 9, 8)
• P4 → Work = (2, 10, 10, 12)
• P1 → completes.
Safe sequence = <P0, P2, P3, P4, P1>. Hence, the request CAN be
granted immediately.
B Describe the concept and working of a Translation Lookaside Buffer (TLB) 10
in a paging system. Explain how address translation is carried out with and
without TLB.
Definition and Need of TLB (2 Marks)
address translation without TLB (4 Marks)
address translation with TLB (4 Marks)
• A Translation Lookaside Buffer (TLB) is a special high-speed cache
that stores recent translations of virtual page numbers (VPNs) to
physical frame numbers (PFNs).
•   In a paging system, every memory access requires a page table lookup
to translate the virtual address into a physical address.
• This lookup takes extra time (additional memory access), which slows
down the system.
• The TLB reduces this delay by caching frequently used page table
entries — providing fast access to address translations.
Address translation is carried out with TLB.
********** 9 **********

[Text in pictures on this page, read by OCR]
frame e

logical address physical address 0x000
frame f
cpu slp | a |
p — Oxfff
f frame g

physical memory

page table
--- page 10 ---
Address translation is carried without TLB.
4 A Provide a comparative analysis of the Monolithic and Layered architectures 10
of Operating Systems. Include appropriate diagrams to support your
explanation.
Monolithic Architecture (3 Marks)
Layered Architecture (3 Marks)
Comparative Analysis (4 Marks)
Operating System architecture defines the structure and organization of the
OS components and their interaction with each other and hardware.
Two commonly used architectures are Monolithic and Layered
architectures.
Monolithic Architecture (3 Marks)
Explanation:
•   In a monolithic system, the entire operating system is working in a
single kernel space.
•   All system components such as   file management, process
scheduling, memory management, and device drivers are integrated
into one large block of code that runs in supervisor mode.
•   It provides high performance because there are no inter-layer
overheads, but poor modularity and difficult debugging.
Diagram:
********** 10 **********

[Text in pictures on this page, read by OCR]
logical

address
CPU +> pid

page frame

number number

E TLB hit physical

BI address
Lt | 4d }—

TLB

TLB miss

a physical
memory

page table
--- page 11 ---
Advantages:
• High execution speed (no layer overhead).
•   Efficient direct access to hardware.
Disadvantages:
•   Difficult to maintain and debug.
• Poor security and modularity—failure in one module may crash the
entire system.
Examples:
MS-DOS, UNIX (early versions), Linux (partially monolithic).
Layered Architecture (3 Marks)
Explanation:
•   In layered architecture, the OS is divided into multiple layers, each
built upon the lower one.
• Each layer performs specific functions and interacts only with its
adjacent layers.
• The bottom layer deals with hardware, while the top layer provides
user interfaces.
Diagram:
********** 11 **********

[Text in pictures on this page, read by OCR]
applications

glibc standard c library

system-call interface
file CPU
systems scheduler
networks memory
(TCP/IP) manager
block character
devices devices

device drivers

hardware
--- page 12 ---
Advantages:
•   Better modularity and maintainability.
•   Easier to test and debug individual layers.
• Higher security and reliability due to restricted communication.
Disadvantages:
• Slower execution due to layer-to-layer communication overhead.
•   Difficult to design and define proper boundaries between layers.
Examples:
THE Operating System, Windows NT, OS/2.
Comparative Analysis (4 Marks)
Feature   Monolithic OS   Layered OS
Structure   Single large kernel Multiple   layers   with   clear
interfaces
Performance   High   (no Slightly slower (due to layering)
overhead)
Modularity   Poor   Excellent
Maintainability Difficult   Easier to maintain and modify
Security   Low   (shared High   (restricted   inter-layer
kernel)   access)
Examples   MS-DOS, UNIX   Windows NT, THE OS
Conclusion:
Monolithic architecture emphasizes performance, whereas layered
architecture   emphasizes   modularity,   reliability,   and   security.
Modern operating systems often adopt a hybrid approach, combining the
speed of monolithic design with the structure of layered models.
B A disk queue with requests on cylinders 85, 170, 45, 130, 25, 115, 72, 58 10
needs to be serviced. The disk head is initially at cylinder 60, and the disk
has cylinders numbered 0-199. Calculate the total head movement for:
1. FCFS
2. SSTF
3. SCAN (assuming initial direction towards cylinder 199)
4. C-SCAN (assuming initial direction towards cylinder 199)
Compare the performance of each algorithm and determine which suits best
for this scenario.
********** 12 **********

[Text in pictures on this page, read by OCR]
application file device user
program system driver mode

messages: messages

CPU
scheduling

memory
managment

kernel
mode

interprocess
communication

microkernel

hardware
--- page 13 ---
Each Algorithm 2 Marks
Comparison 2 Marks

RK KKK RK KK 13 2h KKK RK Kk KK
--- page 14 ---
Best Algorithm for This Scenario:
SSTF provides the best performance with only 180 cylinders of movement,
making it ideal for this scenario where minimizing seek time is the priority
and the request queue is relatively small, reducing starvation risk.
5 A Describe the concept of monitors in process synchronization with internal 10
structure and functioning. Explain how monitors manage process
coordination using condition variables and synchronization primitives.
Concept of Monitors (2 Marks)
Internal Structure of a Monitor (4 Marks)
Functioning and Coordination (4 Marks)
In concurrent programming, monitors are high-level synchronization
constructs that provide a convenient and safe mechanism for process
coordination.
They encapsulate shared data, the procedures that operate on that data, and
the synchronization between concurrent processes — all within a single
module.
Monitors eliminate many of the errors possible when using low-level
primitives such as semaphores.
A monitor is a software module with:
• Shared data variables.
• A set of procedures (only one process can execute inside the
monitor at a time).
• Condition variables for process synchronization.
It ensures mutual exclusion automatically — no two processes can execute
monitor procedures simultaneously.
********** 14 **********

[Text in pictures on this page, read by OCR]
Performance Comparison

Algorithm Total Movement Characteristics

FCFS 572 Simple, fair, but high seek time

SSTF 188 Minimal movement, risk of starvation
SCAN 313 Fair, predictable, moderate performance

C-SCAN 396 More uniform wait time, higher movement
--- page 15 ---
Internal Structure of a Monitor (4 Marks)
Components:
1. Shared Data: Variables accessible only through monitor procedures.
2. Procedures: Define operations that can be performed on shared data.
3. Initialization Code: Sets up initial values for data and conditions.
4. Condition Variables: Used for process synchronization (e.g., x, y).
Pseudocode syntax of a monitor:
monitor monitor-name
{
// shared variable declarations
function P1 (…) { …. }
function P2 (…) { …. }
function Pn (…) {……}
initialization code (…) { … }
}
Diagram of Monitor Structure (1 Mark)
+-----------------------------------+
Functioning and Coordination (4 Marks)
Condition Variables and Synchronization:
• Condition variables allow a process to wait for a certain condition
to become true.
• Two basic operations are used:
o wait(c) → Process is suspended until another process signals
condition c.
o signal(c) → Wakes up one waiting process on condition c.
• Mutual exclusion: Achieved automatically; only one process
executes within the monitor.
•   Synchronization: Managed through wait and signal on condition
variables.
• No busy waiting: Blocked processes are placed in a waiting queue
inside the monitor.
Advantages of Monitors
********** 15 **********
--- page 16 ---
• Provides structured and safer synchronization compared to
semaphores.
•   Eliminates errors like deadlocks and race conditions caused by
improper semaphore use.
• Promotes modularity and clarity in concurrent program design.
B Explain how fragmentation affects memory management in operating 10
systems and illustrate the different types of fragmentation with suitable
example. A system has five memory partitions of sizes 110 KB, 480 KB,
210   KB,   350   KB,   and   140   KB   respectively.
A sequence of processes arrives for allocation in the following order: P1 =
100 KB, P2 = 200 KB, P3 = 300 KB, P4 = 140 KB, and P5 = 50 KB.
Considering Contiguous memory allocation, show the final process-to-
partition allocations using First-Fit, Best-Fit, and Worst-Fit memory
allocation strategies.
Marks Distribution:
Fragmentation 2 Marks
Types 2 marks
First Fit – 2 marks
Best Fit – 2 marks
Worst Fit – 2 marks
Fragmentation is a memory management problem that occurs when free memory
space is broken into small, non-contiguous blocks over time. It reduces the
system’s ability to allocate large continuous memory blocks to new processes,
even if total free memory is sufficient.
Fragmentation affects memory utilization and system performance, leading to
inefficient use of available RAM.
Types of Fragmentation
(a) Internal Fragmentation
Definition: Occurs when a fixed-sized memory block allocated to a process is
larger than the process’s actual memory requirement.
Cause: Fixed partitioning or paging schemes with block sizes larger than needed.
Effect: Wasted space inside the allocated partition.
Example:
Suppose a system allocates 4 KB blocks, and a process needs only 3.6 KB.
→ Unused memory = 0.4 KB per process
This 0.4 KB inside the allocated block is internally fragmented.
External Fragmentation
Definition: Occurs when total free memory exists but is scattered in non-
contiguous blocks, preventing allocation of large processes.
Cause: Dynamic memory allocation where processes are loaded and removed
frequently.
Effect: Wasted space outside allocated partitions.
Example:
Assume memory = 100 MB total. Free blocks: 20 MB + 15 MB + 10 MB (non-
contiguous).
********** 16 **********
--- page 17 ---
A process requesting 40 MB cannot be allocated, though 45 MB is free in total.
6 A   I.   Apply your understanding of process scheduling to compare Long- 10
term and Short-term schedulers in terms of their purpose, execution
frequency, speed, alternate names, and where process selection
occurs (main or secondary memory).
II.   Apply the concepts of process scheduling to justify why time-
sharing systems rely more on Short-term scheduler, while batch-
processing systems depend more on Long-term scheduler.
I.   5 Marks (One mark for each criteria)
II.   5 Marks
Solution:
i. Following are the differences between a LTS and STS:- (5 marks)
********** 17 **********
--- page 18 ---
Aspect   Long-Term Scheduler   Short-Term Scheduler
Frequency   Runs less frequently.   Runs very frequently.
Speed   Slower, as it involves   Faster, as it focuses
more complex decision-   solely on CPU allocation.
making and memory
checks.
Process   Selects processes from the   Selects processes from
selection   job pool (secondary   the ready queue (main
location   memory).   memory).
Alternate   Job Scheduler   CPU Scheduler
Name
Purpose   Balances I/O-bound and   Maximizes CPU
CPU-bound processes.   utilization and minimizes
process waiting times.
ii. Time-sharing: Many interactive users → responsiveness is critical.
The short-term scheduler (CPU scheduler) decides which process
runs next very frequently (milliseconds). Long-term scheduler is
less relevant because new jobs are admitted immediately.
Batch system: Jobs are large and submitted in bulk. The long-term
scheduler regulates how many jobs enter memory, controlling
degree of multiprogramming. If too many are admitted, system
thrashes; if too few, CPU underutilizes.
(5 marks)
B A system has 3 frames for storing process pages in main memory. Assume
that all the page frames are initially empty. Consider the page reference
string given below:
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Compute the number of page faults and show frame contents step-by-step
for:
(a) FIFO,
(b) LRU,
(c) Optimal.
Also state which algorithm gave the fewest faults.
Marks Distribution:
(FIFO: 3 marks, LRU: 3 marks, Optimal: 3 marks)
Also state which algorithm gave the fewest faults and why.(1 marks)
********** 18 **********
--- page 19 ---
Reference string length = 12. Frames = 3.
(a) FIFO (First-In, First-Out)
Frames after
Step   Ref   Fault?
step (f1,f2,f3)
1   1   1, - , -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
4   4   4, 2, 3 (1 out) Y
5   1   4, 1, 3 (2 out) Y
6   2   4, 1, 2 (3 out) Y
7   5   5, 1, 2 (4 out) Y
8   1   5, 1, 2   N
9   2   5, 1, 2   N
10   3   5, 3, 2 (1 out) Y
11   4   5, 3, 4 (2 out) Y
12   5   5, 3, 4   N
Total page faults (FIFO): 9.
(b) LRU (Least Recently Used)
LRU replaces the page that has not been used for the longest time.
Step   Ref   Frames after step Fault? Comment
1   1   1, -, -   Y   load 1
2   2   1, 2, -   Y   load 2
3   3   1, 2, 3   Y   load 3
4, 2, 3 (1 was
4   4   Y
LRU)
4, 1, 3 (2 LRU
5   1   Y
replaced)
4, 1, 2 (3 LRU
6   2   Y
replaced)
********** 19 **********
--- page 20 ---
5, 1, 2 (4 LRU
7   5   Y
replaced)
8   1   5, 1, 2   N
9   2   5, 1, 2   N
3, 1, 2 (5 LRU
10   3   Y
replaced)
3, 4, 2 (1 LRU
11   4   Y
replaced)
3, 4, 5 (2 LRU
12   5   Y
replaced)
Total page faults (LRU): 10.
(c) Optimal (Belady’s optimal algorithm) — replace the page that will not
be used for the longest time in the future.
Frames after
Step   Ref   Fault?
step
1   1   1, -, -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
1, 2, 4 (3
replaced; will be
4   4   used later   Y
sooner than 1 or
2?)*
5   1   1, 2, 4   N
6   2   1, 2, 4   N
1, 2, 5 (4
replaced: 4 next
used at step 11;
7   5   Y
1 and 2 are
needed earlier at
steps 8 and 9)
8   1   1, 2, 5   N
9   2   1, 2, 5   N
3, 2, 5 (1
replaced; 1 next
10   3   Y
used later than 2
or 5)
********** 20 **********
--- page 21 ---
3, 4, 5 (2
11   4   Y
replaced)
12   5   3, 4, 5   N
Total page faults (Optimal): 7.
Optimal gives the fewest faults (7) because it uses future knowledge. For
real systems we cannot implement Optimal, but it is used as a baseline. In
this case FIFO (9) beats LRU (10) — showing that LRU is usually good
but not always strictly better than FIFO, and that algorithms’ effectiveness
depends on the reference string.
7 A Analyze the Resource Allocation Graph
i)   Write resource allocated and requested table
ii)   Find if there is a deadlock or not? If there is no deadlock then
what will be the sequence of the process to get executed?
iii)   What will happen if one instance of resource R3 is removed
from the system.
I.   4 marks
II.   4 Marks
III.   2 Marks
i)
********** 21 **********
--- page 22 ---
II) System is in Safe State. Safe Sequence: P2, P0, P1, P3
III) There will be a deadlock in the system.
B Explain user level and kernel level threads. Which one are more light 5
weight and independent?
User and Kernel Thread 3 marks
Explanation 2 marks
Solution: User-level threads are managed entirely by a user-level thread
library without direct involvement from the operating system's kernel.
The kernel is unaware of their existence and treats the entire process
containing these threads as a single unit of execution.
(1.5 marks)
Kernel-level threads are managed directly by the operating system's
kernel. The kernel is aware of each individual kernel thread and handles
their creation, scheduling, and management.   (1.5 marks)
User-level threads are managed by a user-level thread library, making
them more lightweight as they don't require kernel intervention and offer
faster context switching, but are less independent as a blocking thread can
block the entire process. Kernel-level threads are managed by the
operating system, are more independent because they can take advantage
of multiple CPUs and are not tied to a single process's blocking state but
are more heavyweight due to the overhead of kernel mode transitions and
are slower to create and switch.
(2 marks)
C   Differentiate between sequential access and direct access methods for files. 5
Provide examples of applications where each access method would be
preferred.
Difference 4 marks
Example 1 marks
Sequential Access In sequential access, data in a file is processed in
order, one record or byte after the next. The operations typically used are
read next and write next. Repositioning within the file usually requires a
Reset (rewind) operation to go back to the beginning.
********** 22 **********
--- page 23 ---
Direct Access Direct access views a file as a numbered sequence of fixed-
length logical records. This method allows for immediate, random access
to any part of the file. Operations include explicitly reading or writing
record number (read n, write n), and moving the file pointer directly to
record (position to n).
Application Preference:
Sequential Access Preference This method is preferred for applications
where files must be processed entirely from beginning to end. Examples
include simple text files, log files (where records are appended
chronologically), and source code files read by a compiler.
Direct Access Preference Direct access is preferred for applications that
require quick, random retrieval and update of specific records. A prime
example is an Indexed/Relative File system, commonly used in databases
or any system (like a customer database or airline reservation system)
where a record must be accessed by its index or relative block number.
********** 23 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 80a313e0989b

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_Computer_7002/Operating Systems/ANS_Operating Systems(702CO1C002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 70.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MASTER OF BUSINESS ADMINISTRATION
IN TECHNOLOGY MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA
Tech (Comp)
Year: II / III / V/Sem 3 Re-exam/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1 A What are the various components of an Operating System? Briefly explain 5
with the help of a diagram.
Explanation of components (any four) 1 mark each (4 Marks)
Diagram   1 mark
The main components of an operating system are:
1. Process Management
o Handles creation, scheduling, and termination of processes.
o Ensures fair CPU allocation among processes.
2. Memory Management
o Manages primary memory allocation and deallocation.
o Keeps track of memory usage and optimizes performance.
3. File Management
o Organizes, stores, retrieves, and manages data in files.
o Maintains directories and provides file access control.
4. Device Management
o Controls and coordinates input/output devices via device
drivers.
o Ensures efficient and conflict-free resource usage.
5. Security and Protection
o Protects data and system resources from unauthorized
access.
o Implements authentication, authorization, and encryption
mechanisms.
********** 1 **********
--- page 2 ---
B Analyze the code for Process Pi and Pj and state whether it satisfies the 5
three requirements for the solution to the critical section problem or not.
Justify your answer.
For process Pi:
do {
flag[i] = true;
turn = j;
while (flag[j] && turn == j);
// Critical Section
flag[i] = false;
// Remainder Section
} while (true);
For process Pj:
do {
flag[j] = true;
turn = i;
while (flag[i] && turn == i);
// Critical Section
flag[j] = false;
// Remainder Section
} while (true);
Final verdict: 2 marks
Justification each condition: 1 Mark (3 marks)
Yes, it satifies all the three conditions of mutual exclusion.
A. Mutual exclusion is preserved
Pi enters CS only if:
either flag[j] = false or turn = i
B. Progress requirement is satisfied: If a process wants to enter the
critical section, it waits only if the other process is inside or waiting
to enter, and it is the other process’s turn.
If the other process is not interested (flag[j] == false), then the first
process proceeds immediately without waiting.
Also, the turn variable guarantees that the processes alternate access
if both want to enter, so no process can block the other indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
user and other system programs

GUI touch screen | command line

user interfaces

system calls

program vO file a resource
communication

. A a accounting
execution operations systems allocation

protection
and
security

error
detection
services

operating system

hardware
--- page 3 ---
C. Bounded-waiting requirement is met: The turn variable acts as a fair
"token" passed between the two processes, ensuring that after one
process finishes, the other will eventually get the turn.
C Describe the process of deadlock recovery after detection. What are the
common methods used? Explain any two.
Deadlock Recovery 1 mark
Methods 4 marks
Process of Deadlock Recovery (1 Marks)
Once a deadlock is detected (usually using the resource allocation graph or
Banker’s algorithm), the OS performs the following steps:
1. Identify deadlocked processes and resources.
2. Select a recovery method — terminate processes, preempt
resources, or roll back processes.
3. Recover the system by releasing held resources and restarting
affected processes.
4. Resume normal operation.
Common Methods of Deadlock Recovery
The two main categories are:
1. Process Termination — killing one or more processes involved in
the deadlock.
2. Resource Preemption — temporarily taking resources away from
processes.
Other less common methods:
• Process Rollback (restore to a safe checkpoint).
• Manual Intervention (in simple or embedded systems).
(i) Process Termination (2 Marks)
• Concept:
Abort one or more processes involved in the deadlock until the cycle
is broken.
• Approaches:
1. Abort all deadlocked processes.
▪ Simple but costly; results in loss of work.
2. Abort processes one at a time until the deadlock cycle is
resolved.
•   Selection   Criteria:
When choosing which process to terminate, the OS considers:
1. Process priority and importance.
2. Amount of CPU time consumed.
3. Number and type of resources held.
4. Whether the process can be restarted easily.
• Advantages:
1. Straightforward and guaranteed recovery.
• Disadvantages:
1. May lead to loss of significant computation progress.
2. System performance temporarily degrades.
(ii) Resource Preemption (2 Marks)
• Concept:
Temporarily take away (preempt) resources from some processes
and give them to others to break the deadlock.
********** 3 **********
--- page 4 ---
• Steps Involved:
1. Select a victim process – the one whose resource preemption
has the least cost.
2. Save its state (checkpoint) – so it can be restarted later.
3. Reassign its resources to other waiting processes.
•   Challenges:
1. Rollback: The victim process must be rolled back to a safe
state.
2. Starvation: A process may be repeatedly chosen as a victim;
hence, the OS must keep track of how often each process is
preempted.
• Advantages:
1. Allows partial progress of other processes.
• Disadvantages:
1. Complex to implement and may lead to instability if done
repeatedly.
D Describe the concept of I/O management in an operating system and apply
your knowledge to identify key factors that can enhance I/O performance.
I/O Management 2 Marks
Factors 3 Marks (at least 3)
I/O management is a major component of operating system design that
handles the interaction between the computer system and I/O devices.
Key Components:
•   Ports, Buses, Controllers: Connect various devices to the system
• Device Drivers: Encapsulate device-specific details and present
uniform device-access interface to I/O subsystem
• I/O Hardware: Manages incredible variety of devices (storage,
transmission, human-interface)
I/O Methods:
•   Polling: CPU repeatedly checks device status (inefficient for slow
devices)
•   Interrupts: Device signals CPU when ready (efficient, used for
time-sensitive operations)
• DMA (Direct Memory Access): Transfers data directly between
device and memory without CPU involvement
I/O Operations:
• Blocking I/O: Process suspended until I/O completed
• Nonblocking I/O: Returns immediately with available data
• Asynchronous I/O: Process continues while I/O executes
Factors for Improving I/O Performance
1. Reduce Context Switches
• Minimize switching between processes during I/O operations
2. Reduce Data Copying
• Minimize copying data between kernel and user space
3. Reduce Interrupts
• Use large transfers instead of multiple small ones
• Employ smart controllers
• Use polling when appropriate
4. Use DMA (Direct Memory Access)
• Allow devices to transfer data directly to/from memory
********** 4 **********
--- page 5 ---
• Frees CPU from data transfer burden
5. Use Smarter Hardware Devices
•   Intelligent controllers with built-in processing capabilities
6. Balance System Resources
• Balance CPU, memory, bus, and I/O performance for highest
throughput
7. Move User-mode Processes to Kernel Threads
• Reduces overhead for frequently used I/O operations
8. Implement Efficient Buffering and Caching
• Buffer data to handle speed/size mismatches
• Cache frequently accessed data on faster devices
2 A Examine the synchronization problem in operating systems, identifying the
challenges it creates. Analyse how counting semaphores provide a
structured solution and resolve these issues in the Readers–Writers
problem.
Explain Synchronization Problem in Detail [4 marks]
Readers-Writers Problem [6 marks]
The Synchronization Problem arises in a multi-process or multi-threaded
environment when multiple processes concurrently access and manipulate
shared data. The core issue is that the final result of the execution depends
on the specific order in which instructions are interleaved, leading to
unpredictable and inconsistent results. This is known as a race condition.
Causes and Consequences:
1. Race Condition: Occurs when several processes access and modify
the same shared data concurrently, and the outcome of the execution
depends on the order of access.
2. Data Inconsistency: The primary consequence is that the shared data
may end up in a corrupted or inconsistent state.
Example (The Critical Section Problem): A simple counter shared by two
threads, one incrementing and the other decrementing. The operations
(Read → Modify → Write) are not atomic. If the operations are interrupted
and interleaved, the final count can be incorrect (e.g., instead of
100→101→100, it might become 100→101→101).
Requirements for a Correct Solution:
1. Mutual Exclusion: Only one process can be executing in its critical
section at any time.
2. Progress: If no process is executing in its critical section and some
processes wish to enter, then only those processes not in their
remainder sections can participate in deciding which will enter next,
and this selection cannot be postponed indefinitely.
3. Bounded Waiting: There must be a limit on the number of times
other processes are allowed to enter their critical sections after a
process has made a request to enter its critical section and before
that request is granted.
B. Counting Semaphore for Readers-Writers Problem [6 marks]
The Readers-Writers Problem is a classic synchronization problem where
multiple processes try to access a shared database.
● Readers only read the data and can do so concurrently.
● Writers modify the data and must have exclusive access (no other
reader or writer allowed).
********** 5 **********
--- page 6 ---
A Counting Semaphore (and a Binary/Mutex semaphore) can be used to
manage this access
Writer Process Logic: The writer needs exclusive access. It only needs to
wait on the general lock (wrt).
do {
wait(wrt);
// Writing is performed
signal(wrt);
} while (TRUE);
Reader Process Logic: Readers need to coordinate using readcount and
the wrt lock.
do {
wait(mutex);   // 1. Lock the readcount variable
readcount++;
if (readcount == 1) {   // 2. First reader locks out the writer
wait(wrt);
}
signal(mutex);   // 3. Unlock the readcount variable
// Reading is performed
wait(mutex);   // 4. Lock the readcount variable
readcount--;
if (readcount == 0) {   // 5. Last reader signals the writer
signal(wrt);
}
signal(mutex);   // 6. Unlock the readcount variable
} while (TRUE);
B Consider the following set of processes, each with varying arrival times
and burst times.
Process   Arrival Time   Burst Time
P1   0   7
P2   2   4
P3   4   1
P4   5   4
P5   6   3
i. Using the SRTF scheduling algorithm, determine the average
waiting time and average response time.
ii. Using the Round-Robin scheduling algorithm with time quantum =
3, determine the average waiting time and average response time.
********** 6 **********
--- page 7 ---
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
3 A Consider the following snapshot of a system running 5 processes:
Pro- Allocation   Max   Available
cess A   B   C   D A   B   C D A B   C D
P0   0   0   1   2 0   0   1   2 1   5   2   0
P1   1   0   0   0 1   7   5   0
P2   1   3   5   4 2   3   5   6
P3   0   6   3   2 0   6   5   2
********** 7 **********
--- page 8 ---
P4   0   0   1   4 0   6   5   6
Answer the following: -
i. How many resources of type A, B, C, D are there?
ii.   Calculate the need matrix?
iii.   Determine if the system is safe or not.
iv.   What will happen if the resource request (0, 4, 2,0) for process P1
arrive, can the system accept this request immediately?
Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks
Safe Sequence 3 Marks
Additional Request 3 Marks
The total number of resources of each type is calculated as:
Total = Allocation (sum) + Available
• A = 2 + 1 = 3
• B = 9 + 5 = 14
• C = 10 + 2 = 12
• D = 12 + 0 = 12
Thus, total system resources = (3, 14, 12, 12).
vi) Need Matrix
Process   A   B   C   D
P0   0   0   0   0
P1   0   7   5   0
P2   1   0   0   2
P3   0   0   2   0
P4   0   6   4   2
vii) Safe State Check
Starting with Available = (1, 5, 2, 0):
• P0 runs → Work = (1, 5, 3, 2)
• P3 runs → Work = (1, 11, 6, 4)
• P2 runs → Work = (2, 14, 11, 8)
• P4 runs → Work = (2, 14, 12, 12)
• P1 runs → Work = (3, 14, 12, 12)
Safe sequence = <P0, P3, P2, P4, P1>. Therefore, the system is SAFE.
viii) Resource Request (0, 4, 2, 0) by P1
********** 8 **********
--- page 9 ---
• Request (0, 4, 2, 0) ≤ Need(P1) = (0, 7, 5, 0) ✔
• Request (0, 4, 2, 0) ≤ Available (1, 5, 2, 0) ✔
After tentative allocation: Available = (1, 1, 0, 0).
Safety test sequence:
• P0 → Work = (1, 1, 1, 2)
• P2 → Work = (2, 4, 6, 6)
• P3 → Work = (2, 10, 9, 8)
• P4 → Work = (2, 10, 10, 12)
• P1 → completes.
Safe sequence = <P0, P2, P3, P4, P1>. Hence, the request CAN be
granted immediately.
B Describe the concept and working of a Translation Lookaside Buffer (TLB) 10
in a paging system. Explain how address translation is carried out with and
without TLB.
Definition and Need of TLB (2 Marks)
address translation without TLB (4 Marks)
address translation with TLB (4 Marks)
• A Translation Lookaside Buffer (TLB) is a special high-speed cache
that stores recent translations of virtual page numbers (VPNs) to
physical frame numbers (PFNs).
•   In a paging system, every memory access requires a page table lookup
to translate the virtual address into a physical address.
• This lookup takes extra time (additional memory access), which slows
down the system.
• The TLB reduces this delay by caching frequently used page table
entries — providing fast access to address translations.
Address translation is carried out with TLB.
********** 9 **********

[Text in pictures on this page, read by OCR]
frame e

logical address physical address 0x000
frame f
cpu slp | a |
p — Oxfff
f frame g

physical memory

page table
--- page 10 ---
Address translation is carried without TLB.
4 A Provide a comparative analysis of the Monolithic and Layered architectures 10
of Operating Systems. Include appropriate diagrams to support your
explanation.
Monolithic Architecture (3 Marks)
Layered Architecture (3 Marks)
Comparative Analysis (4 Marks)
Operating System architecture defines the structure and organization of the
OS components and their interaction with each other and hardware.
Two commonly used architectures are Monolithic and Layered
architectures.
Monolithic Architecture (3 Marks)
Explanation:
•   In a monolithic system, the entire operating system is working in a
single kernel space.
•   All system components such as   file management, process
scheduling, memory management, and device drivers are integrated
into one large block of code that runs in supervisor mode.
•   It provides high performance because there are no inter-layer
overheads, but poor modularity and difficult debugging.
Diagram:
********** 10 **********

[Text in pictures on this page, read by OCR]
logical

address
CPU +> pid

page frame

number number

E TLB hit physical

BI address
Lt | 4d }—

TLB

TLB miss

a physical
memory

page table
--- page 11 ---
Advantages:
• High execution speed (no layer overhead).
•   Efficient direct access to hardware.
Disadvantages:
•   Difficult to maintain and debug.
• Poor security and modularity—failure in one module may crash the
entire system.
Examples:
MS-DOS, UNIX (early versions), Linux (partially monolithic).
Layered Architecture (3 Marks)
Explanation:
•   In layered architecture, the OS is divided into multiple layers, each
built upon the lower one.
• Each layer performs specific functions and interacts only with its
adjacent layers.
• The bottom layer deals with hardware, while the top layer provides
user interfaces.
Diagram:
********** 11 **********

[Text in pictures on this page, read by OCR]
applications

glibc standard c library

system-call interface
file CPU
systems scheduler
networks memory
(TCP/IP) manager
block character
devices devices

device drivers

hardware
--- page 12 ---
Advantages:
•   Better modularity and maintainability.
•   Easier to test and debug individual layers.
• Higher security and reliability due to restricted communication.
Disadvantages:
• Slower execution due to layer-to-layer communication overhead.
•   Difficult to design and define proper boundaries between layers.
Examples:
THE Operating System, Windows NT, OS/2.
Comparative Analysis (4 Marks)
Feature   Monolithic OS   Layered OS
Structure   Single large kernel Multiple   layers   with   clear
interfaces
Performance   High   (no Slightly slower (due to layering)
overhead)
Modularity   Poor   Excellent
Maintainability Difficult   Easier to maintain and modify
Security   Low   (shared High   (restricted   inter-layer
kernel)   access)
Examples   MS-DOS, UNIX   Windows NT, THE OS
Conclusion:
Monolithic architecture emphasizes performance, whereas layered
architecture   emphasizes   modularity,   reliability,   and   security.
Modern operating systems often adopt a hybrid approach, combining the
speed of monolithic design with the structure of layered models.
B A disk queue with requests on cylinders 85, 170, 45, 130, 25, 115, 72, 58 10
needs to be serviced. The disk head is initially at cylinder 60, and the disk
has cylinders numbered 0-199. Calculate the total head movement for:
1. FCFS
2. SSTF
3. SCAN (assuming initial direction towards cylinder 199)
4. C-SCAN (assuming initial direction towards cylinder 199)
Compare the performance of each algorithm and determine which suits best
for this scenario.
********** 12 **********

[Text in pictures on this page, read by OCR]
application file device user
program system driver mode

messages: messages

CPU
scheduling

memory
managment

kernel
mode

interprocess
communication

microkernel

hardware
--- page 13 ---
Each Algorithm 2 Marks
Comparison 2 Marks

RK KKK RK KK 13 2h KKK RK Kk KK
--- page 14 ---
Best Algorithm for This Scenario:
SSTF provides the best performance with only 180 cylinders of movement,
making it ideal for this scenario where minimizing seek time is the priority
and the request queue is relatively small, reducing starvation risk.
5 A Describe the concept of monitors in process synchronization with internal 10
structure and functioning. Explain how monitors manage process
coordination using condition variables and synchronization primitives.
Concept of Monitors (2 Marks)
Internal Structure of a Monitor (4 Marks)
Functioning and Coordination (4 Marks)
In concurrent programming, monitors are high-level synchronization
constructs that provide a convenient and safe mechanism for process
coordination.
They encapsulate shared data, the procedures that operate on that data, and
the synchronization between concurrent processes — all within a single
module.
Monitors eliminate many of the errors possible when using low-level
primitives such as semaphores.
A monitor is a software module with:
• Shared data variables.
• A set of procedures (only one process can execute inside the
monitor at a time).
• Condition variables for process synchronization.
It ensures mutual exclusion automatically — no two processes can execute
monitor procedures simultaneously.
********** 14 **********

[Text in pictures on this page, read by OCR]
Performance Comparison

Algorithm Total Movement Characteristics

FCFS 572 Simple, fair, but high seek time

SSTF 188 Minimal movement, risk of starvation
SCAN 313 Fair, predictable, moderate performance

C-SCAN 396 More uniform wait time, higher movement
--- page 15 ---
Internal Structure of a Monitor (4 Marks)
Components:
1. Shared Data: Variables accessible only through monitor procedures.
2. Procedures: Define operations that can be performed on shared data.
3. Initialization Code: Sets up initial values for data and conditions.
4. Condition Variables: Used for process synchronization (e.g., x, y).
Pseudocode syntax of a monitor:
monitor monitor-name
{
// shared variable declarations
function P1 (…) { …. }
function P2 (…) { …. }
function Pn (…) {……}
initialization code (…) { … }
}
Diagram of Monitor Structure (1 Mark)
+-----------------------------------+
Functioning and Coordination (4 Marks)
Condition Variables and Synchronization:
• Condition variables allow a process to wait for a certain condition
to become true.
• Two basic operations are used:
o wait(c) → Process is suspended until another process signals
condition c.
o signal(c) → Wakes up one waiting process on condition c.
• Mutual exclusion: Achieved automatically; only one process
executes within the monitor.
•   Synchronization: Managed through wait and signal on condition
variables.
• No busy waiting: Blocked processes are placed in a waiting queue
inside the monitor.
Advantages of Monitors
********** 15 **********
--- page 16 ---
• Provides structured and safer synchronization compared to
semaphores.
•   Eliminates errors like deadlocks and race conditions caused by
improper semaphore use.
• Promotes modularity and clarity in concurrent program design.
B Explain how fragmentation affects memory management in operating 10
systems and illustrate the different types of fragmentation with suitable
example. A system has five memory partitions of sizes 110 KB, 480 KB,
210   KB,   350   KB,   and   140   KB   respectively.
A sequence of processes arrives for allocation in the following order: P1 =
100 KB, P2 = 200 KB, P3 = 300 KB, P4 = 140 KB, and P5 = 50 KB.
Considering Contiguous memory allocation, show the final process-to-
partition allocations using First-Fit, Best-Fit, and Worst-Fit memory
allocation strategies.
Marks Distribution:
Fragmentation 2 Marks
Types 2 marks
First Fit – 2 marks
Best Fit – 2 marks
Worst Fit – 2 marks
Fragmentation is a memory management problem that occurs when free memory
space is broken into small, non-contiguous blocks over time. It reduces the
system’s ability to allocate large continuous memory blocks to new processes,
even if total free memory is sufficient.
Fragmentation affects memory utilization and system performance, leading to
inefficient use of available RAM.
Types of Fragmentation
(a) Internal Fragmentation
Definition: Occurs when a fixed-sized memory block allocated to a process is
larger than the process’s actual memory requirement.
Cause: Fixed partitioning or paging schemes with block sizes larger than needed.
Effect: Wasted space inside the allocated partition.
Example:
Suppose a system allocates 4 KB blocks, and a process needs only 3.6 KB.
→ Unused memory = 0.4 KB per process
This 0.4 KB inside the allocated block is internally fragmented.
External Fragmentation
Definition: Occurs when total free memory exists but is scattered in non-
contiguous blocks, preventing allocation of large processes.
Cause: Dynamic memory allocation where processes are loaded and removed
frequently.
Effect: Wasted space outside allocated partitions.
Example:
Assume memory = 100 MB total. Free blocks: 20 MB + 15 MB + 10 MB (non-
contiguous).
********** 16 **********
--- page 17 ---
A process requesting 40 MB cannot be allocated, though 45 MB is free in total.
6 A   I.   Apply your understanding of process scheduling to compare Long- 10
term and Short-term schedulers in terms of their purpose, execution
frequency, speed, alternate names, and where process selection
occurs (main or secondary memory).
II.   Apply the concepts of process scheduling to justify why time-
sharing systems rely more on Short-term scheduler, while batch-
processing systems depend more on Long-term scheduler.
I.   5 Marks (One mark for each criteria)
II.   5 Marks
Solution:
i. Following are the differences between a LTS and STS:- (5 marks)
********** 17 **********
--- page 18 ---
Aspect   Long-Term Scheduler   Short-Term Scheduler
Frequency   Runs less frequently.   Runs very frequently.
Speed   Slower, as it involves   Faster, as it focuses
more complex decision-   solely on CPU allocation.
making and memory
checks.
Process   Selects processes from the   Selects processes from
selection   job pool (secondary   the ready queue (main
location   memory).   memory).
Alternate   Job Scheduler   CPU Scheduler
Name
Purpose   Balances I/O-bound and   Maximizes CPU
CPU-bound processes.   utilization and minimizes
process waiting times.
ii. Time-sharing: Many interactive users → responsiveness is critical.
The short-term scheduler (CPU scheduler) decides which process
runs next very frequently (milliseconds). Long-term scheduler is
less relevant because new jobs are admitted immediately.
Batch system: Jobs are large and submitted in bulk. The long-term
scheduler regulates how many jobs enter memory, controlling
degree of multiprogramming. If too many are admitted, system
thrashes; if too few, CPU underutilizes.
(5 marks)
B A system has 3 frames for storing process pages in main memory. Assume
that all the page frames are initially empty. Consider the page reference
string given below:
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Compute the number of page faults and show frame contents step-by-step
for:
(a) FIFO,
(b) LRU,
(c) Optimal.
Also state which algorithm gave the fewest faults.
Marks Distribution:
(FIFO: 3 marks, LRU: 3 marks, Optimal: 3 marks)
Also state which algorithm gave the fewest faults and why.(1 marks)
********** 18 **********
--- page 19 ---
Reference string length = 12. Frames = 3.
(a) FIFO (First-In, First-Out)
Frames after
Step   Ref   Fault?
step (f1,f2,f3)
1   1   1, - , -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
4   4   4, 2, 3 (1 out) Y
5   1   4, 1, 3 (2 out) Y
6   2   4, 1, 2 (3 out) Y
7   5   5, 1, 2 (4 out) Y
8   1   5, 1, 2   N
9   2   5, 1, 2   N
10   3   5, 3, 2 (1 out) Y
11   4   5, 3, 4 (2 out) Y
12   5   5, 3, 4   N
Total page faults (FIFO): 9.
(b) LRU (Least Recently Used)
LRU replaces the page that has not been used for the longest time.
Step   Ref   Frames after step Fault? Comment
1   1   1, -, -   Y   load 1
2   2   1, 2, -   Y   load 2
3   3   1, 2, 3   Y   load 3
4, 2, 3 (1 was
4   4   Y
LRU)
4, 1, 3 (2 LRU
5   1   Y
replaced)
4, 1, 2 (3 LRU
6   2   Y
replaced)
********** 19 **********
--- page 20 ---
5, 1, 2 (4 LRU
7   5   Y
replaced)
8   1   5, 1, 2   N
9   2   5, 1, 2   N
3, 1, 2 (5 LRU
10   3   Y
replaced)
3, 4, 2 (1 LRU
11   4   Y
replaced)
3, 4, 5 (2 LRU
12   5   Y
replaced)
Total page faults (LRU): 10.
(c) Optimal (Belady’s optimal algorithm) — replace the page that will not
be used for the longest time in the future.
Frames after
Step   Ref   Fault?
step
1   1   1, -, -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
1, 2, 4 (3
replaced; will be
4   4   used later   Y
sooner than 1 or
2?)*
5   1   1, 2, 4   N
6   2   1, 2, 4   N
1, 2, 5 (4
replaced: 4 next
used at step 11;
7   5   Y
1 and 2 are
needed earlier at
steps 8 and 9)
8   1   1, 2, 5   N
9   2   1, 2, 5   N
3, 2, 5 (1
replaced; 1 next
10   3   Y
used later than 2
or 5)
********** 20 **********
--- page 21 ---
3, 4, 5 (2
11   4   Y
replaced)
12   5   3, 4, 5   N
Total page faults (Optimal): 7.
Optimal gives the fewest faults (7) because it uses future knowledge. For
real systems we cannot implement Optimal, but it is used as a baseline. In
this case FIFO (9) beats LRU (10) — showing that LRU is usually good
but not always strictly better than FIFO, and that algorithms’ effectiveness
depends on the reference string.
7 A Analyze the Resource Allocation Graph
i)   Write resource allocated and requested table
ii)   Find if there is a deadlock or not? If there is no deadlock then
what will be the sequence of the process to get executed?
iii)   What will happen if one instance of resource R3 is removed
from the system.
I.   4 marks
II.   4 Marks
III.   2 Marks
i)
********** 21 **********
--- page 22 ---
II) System is in Safe State. Safe Sequence: P2, P0, P1, P3
III) There will be a deadlock in the system.
B Explain user level and kernel level threads. Which one are more light 5
weight and independent?
User and Kernel Thread 3 marks
Explanation 2 marks
Solution: User-level threads are managed entirely by a user-level thread
library without direct involvement from the operating system's kernel.
The kernel is unaware of their existence and treats the entire process
containing these threads as a single unit of execution.
(1.5 marks)
Kernel-level threads are managed directly by the operating system's
kernel. The kernel is aware of each individual kernel thread and handles
their creation, scheduling, and management.   (1.5 marks)
User-level threads are managed by a user-level thread library, making
them more lightweight as they don't require kernel intervention and offer
faster context switching, but are less independent as a blocking thread can
block the entire process. Kernel-level threads are managed by the
operating system, are more independent because they can take advantage
of multiple CPUs and are not tied to a single process's blocking state but
are more heavyweight due to the overhead of kernel mode transitions and
are slower to create and switch.
(2 marks)
C   Differentiate between sequential access and direct access methods for files. 5
Provide examples of applications where each access method would be
preferred.
Difference 4 marks
Example 1 marks
Sequential Access In sequential access, data in a file is processed in
order, one record or byte after the next. The operations typically used are
read next and write next. Repositioning within the file usually requires a
Reset (rewind) operation to go back to the beginning.
********** 22 **********
--- page 23 ---
Direct Access Direct access views a file as a numbered sequence of fixed-
length logical records. This method allows for immediate, random access
to any part of the file. Operations include explicitly reading or writing
record number (read n, write n), and moving the file pointer directly to
record (position to n).
Application Preference:
Sequential Access Preference This method is preferred for applications
where files must be processed entirely from beginning to end. Examples
include simple text files, log files (where records are appended
chronologically), and source code files read by a compiler.
Direct Access Preference Direct access is preferred for applications that
require quick, random retrieval and update of specific records. A prime
example is an Indexed/Relative File system, commonly used in databases
or any system (like a customer database or airline reservation system)
where a record must be accessed by its index or relative block number.
********** 23 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 5a0088561df9

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_Computer_7047/Operating Systems/ANS_Operating Systems(702CO1C002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 70.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MASTER OF BUSINESS ADMINISTRATION
IN TECHNOLOGY MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA
Tech (Comp)
Year: II / III / V/Sem 3 Re-exam/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1 A What are the various components of an Operating System? Briefly explain 5
with the help of a diagram.
Explanation of components (any four) 1 mark each (4 Marks)
Diagram   1 mark
The main components of an operating system are:
1. Process Management
o Handles creation, scheduling, and termination of processes.
o Ensures fair CPU allocation among processes.
2. Memory Management
o Manages primary memory allocation and deallocation.
o Keeps track of memory usage and optimizes performance.
3. File Management
o Organizes, stores, retrieves, and manages data in files.
o Maintains directories and provides file access control.
4. Device Management
o Controls and coordinates input/output devices via device
drivers.
o Ensures efficient and conflict-free resource usage.
5. Security and Protection
o Protects data and system resources from unauthorized
access.
o Implements authentication, authorization, and encryption
mechanisms.
********** 1 **********
--- page 2 ---
B Analyze the code for Process Pi and Pj and state whether it satisfies the 5
three requirements for the solution to the critical section problem or not.
Justify your answer.
For process Pi:
do {
flag[i] = true;
turn = j;
while (flag[j] && turn == j);
// Critical Section
flag[i] = false;
// Remainder Section
} while (true);
For process Pj:
do {
flag[j] = true;
turn = i;
while (flag[i] && turn == i);
// Critical Section
flag[j] = false;
// Remainder Section
} while (true);
Final verdict: 2 marks
Justification each condition: 1 Mark (3 marks)
Yes, it satifies all the three conditions of mutual exclusion.
A. Mutual exclusion is preserved
Pi enters CS only if:
either flag[j] = false or turn = i
B. Progress requirement is satisfied: If a process wants to enter the
critical section, it waits only if the other process is inside or waiting
to enter, and it is the other process’s turn.
If the other process is not interested (flag[j] == false), then the first
process proceeds immediately without waiting.
Also, the turn variable guarantees that the processes alternate access
if both want to enter, so no process can block the other indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
user and other system programs

GUI touch screen | command line

user interfaces

system calls

program vO file a resource
communication

. A a accounting
execution operations systems allocation

protection
and
security

error
detection
services

operating system

hardware
--- page 3 ---
C. Bounded-waiting requirement is met: The turn variable acts as a fair
"token" passed between the two processes, ensuring that after one
process finishes, the other will eventually get the turn.
C Describe the process of deadlock recovery after detection. What are the
common methods used? Explain any two.
Deadlock Recovery 1 mark
Methods 4 marks
Process of Deadlock Recovery (1 Marks)
Once a deadlock is detected (usually using the resource allocation graph or
Banker’s algorithm), the OS performs the following steps:
1. Identify deadlocked processes and resources.
2. Select a recovery method — terminate processes, preempt
resources, or roll back processes.
3. Recover the system by releasing held resources and restarting
affected processes.
4. Resume normal operation.
Common Methods of Deadlock Recovery
The two main categories are:
1. Process Termination — killing one or more processes involved in
the deadlock.
2. Resource Preemption — temporarily taking resources away from
processes.
Other less common methods:
• Process Rollback (restore to a safe checkpoint).
• Manual Intervention (in simple or embedded systems).
(i) Process Termination (2 Marks)
• Concept:
Abort one or more processes involved in the deadlock until the cycle
is broken.
• Approaches:
1. Abort all deadlocked processes.
▪ Simple but costly; results in loss of work.
2. Abort processes one at a time until the deadlock cycle is
resolved.
•   Selection   Criteria:
When choosing which process to terminate, the OS considers:
1. Process priority and importance.
2. Amount of CPU time consumed.
3. Number and type of resources held.
4. Whether the process can be restarted easily.
• Advantages:
1. Straightforward and guaranteed recovery.
• Disadvantages:
1. May lead to loss of significant computation progress.
2. System performance temporarily degrades.
(ii) Resource Preemption (2 Marks)
• Concept:
Temporarily take away (preempt) resources from some processes
and give them to others to break the deadlock.
********** 3 **********
--- page 4 ---
• Steps Involved:
1. Select a victim process – the one whose resource preemption
has the least cost.
2. Save its state (checkpoint) – so it can be restarted later.
3. Reassign its resources to other waiting processes.
•   Challenges:
1. Rollback: The victim process must be rolled back to a safe
state.
2. Starvation: A process may be repeatedly chosen as a victim;
hence, the OS must keep track of how often each process is
preempted.
• Advantages:
1. Allows partial progress of other processes.
• Disadvantages:
1. Complex to implement and may lead to instability if done
repeatedly.
D Describe the concept of I/O management in an operating system and apply
your knowledge to identify key factors that can enhance I/O performance.
I/O Management 2 Marks
Factors 3 Marks (at least 3)
I/O management is a major component of operating system design that
handles the interaction between the computer system and I/O devices.
Key Components:
•   Ports, Buses, Controllers: Connect various devices to the system
• Device Drivers: Encapsulate device-specific details and present
uniform device-access interface to I/O subsystem
• I/O Hardware: Manages incredible variety of devices (storage,
transmission, human-interface)
I/O Methods:
•   Polling: CPU repeatedly checks device status (inefficient for slow
devices)
•   Interrupts: Device signals CPU when ready (efficient, used for
time-sensitive operations)
• DMA (Direct Memory Access): Transfers data directly between
device and memory without CPU involvement
I/O Operations:
• Blocking I/O: Process suspended until I/O completed
• Nonblocking I/O: Returns immediately with available data
• Asynchronous I/O: Process continues while I/O executes
Factors for Improving I/O Performance
1. Reduce Context Switches
• Minimize switching between processes during I/O operations
2. Reduce Data Copying
• Minimize copying data between kernel and user space
3. Reduce Interrupts
• Use large transfers instead of multiple small ones
• Employ smart controllers
• Use polling when appropriate
4. Use DMA (Direct Memory Access)
• Allow devices to transfer data directly to/from memory
********** 4 **********
--- page 5 ---
• Frees CPU from data transfer burden
5. Use Smarter Hardware Devices
•   Intelligent controllers with built-in processing capabilities
6. Balance System Resources
• Balance CPU, memory, bus, and I/O performance for highest
throughput
7. Move User-mode Processes to Kernel Threads
• Reduces overhead for frequently used I/O operations
8. Implement Efficient Buffering and Caching
• Buffer data to handle speed/size mismatches
• Cache frequently accessed data on faster devices
2 A Examine the synchronization problem in operating systems, identifying the
challenges it creates. Analyse how counting semaphores provide a
structured solution and resolve these issues in the Readers–Writers
problem.
Explain Synchronization Problem in Detail [4 marks]
Readers-Writers Problem [6 marks]
The Synchronization Problem arises in a multi-process or multi-threaded
environment when multiple processes concurrently access and manipulate
shared data. The core issue is that the final result of the execution depends
on the specific order in which instructions are interleaved, leading to
unpredictable and inconsistent results. This is known as a race condition.
Causes and Consequences:
1. Race Condition: Occurs when several processes access and modify
the same shared data concurrently, and the outcome of the execution
depends on the order of access.
2. Data Inconsistency: The primary consequence is that the shared data
may end up in a corrupted or inconsistent state.
Example (The Critical Section Problem): A simple counter shared by two
threads, one incrementing and the other decrementing. The operations
(Read → Modify → Write) are not atomic. If the operations are interrupted
and interleaved, the final count can be incorrect (e.g., instead of
100→101→100, it might become 100→101→101).
Requirements for a Correct Solution:
1. Mutual Exclusion: Only one process can be executing in its critical
section at any time.
2. Progress: If no process is executing in its critical section and some
processes wish to enter, then only those processes not in their
remainder sections can participate in deciding which will enter next,
and this selection cannot be postponed indefinitely.
3. Bounded Waiting: There must be a limit on the number of times
other processes are allowed to enter their critical sections after a
process has made a request to enter its critical section and before
that request is granted.
B. Counting Semaphore for Readers-Writers Problem [6 marks]
The Readers-Writers Problem is a classic synchronization problem where
multiple processes try to access a shared database.
● Readers only read the data and can do so concurrently.
● Writers modify the data and must have exclusive access (no other
reader or writer allowed).
********** 5 **********
--- page 6 ---
A Counting Semaphore (and a Binary/Mutex semaphore) can be used to
manage this access
Writer Process Logic: The writer needs exclusive access. It only needs to
wait on the general lock (wrt).
do {
wait(wrt);
// Writing is performed
signal(wrt);
} while (TRUE);
Reader Process Logic: Readers need to coordinate using readcount and
the wrt lock.
do {
wait(mutex);   // 1. Lock the readcount variable
readcount++;
if (readcount == 1) {   // 2. First reader locks out the writer
wait(wrt);
}
signal(mutex);   // 3. Unlock the readcount variable
// Reading is performed
wait(mutex);   // 4. Lock the readcount variable
readcount--;
if (readcount == 0) {   // 5. Last reader signals the writer
signal(wrt);
}
signal(mutex);   // 6. Unlock the readcount variable
} while (TRUE);
B Consider the following set of processes, each with varying arrival times
and burst times.
Process   Arrival Time   Burst Time
P1   0   7
P2   2   4
P3   4   1
P4   5   4
P5   6   3
i. Using the SRTF scheduling algorithm, determine the average
waiting time and average response time.
ii. Using the Round-Robin scheduling algorithm with time quantum =
3, determine the average waiting time and average response time.
********** 6 **********
--- page 7 ---
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
3 A Consider the following snapshot of a system running 5 processes:
Pro- Allocation   Max   Available
cess A   B   C   D A   B   C D A B   C D
P0   0   0   1   2 0   0   1   2 1   5   2   0
P1   1   0   0   0 1   7   5   0
P2   1   3   5   4 2   3   5   6
P3   0   6   3   2 0   6   5   2
********** 7 **********
--- page 8 ---
P4   0   0   1   4 0   6   5   6
Answer the following: -
i. How many resources of type A, B, C, D are there?
ii.   Calculate the need matrix?
iii.   Determine if the system is safe or not.
iv.   What will happen if the resource request (0, 4, 2,0) for process P1
arrive, can the system accept this request immediately?
Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks
Safe Sequence 3 Marks
Additional Request 3 Marks
The total number of resources of each type is calculated as:
Total = Allocation (sum) + Available
• A = 2 + 1 = 3
• B = 9 + 5 = 14
• C = 10 + 2 = 12
• D = 12 + 0 = 12
Thus, total system resources = (3, 14, 12, 12).
vi) Need Matrix
Process   A   B   C   D
P0   0   0   0   0
P1   0   7   5   0
P2   1   0   0   2
P3   0   0   2   0
P4   0   6   4   2
vii) Safe State Check
Starting with Available = (1, 5, 2, 0):
• P0 runs → Work = (1, 5, 3, 2)
• P3 runs → Work = (1, 11, 6, 4)
• P2 runs → Work = (2, 14, 11, 8)
• P4 runs → Work = (2, 14, 12, 12)
• P1 runs → Work = (3, 14, 12, 12)
Safe sequence = <P0, P3, P2, P4, P1>. Therefore, the system is SAFE.
viii) Resource Request (0, 4, 2, 0) by P1
********** 8 **********
--- page 9 ---
• Request (0, 4, 2, 0) ≤ Need(P1) = (0, 7, 5, 0) ✔
• Request (0, 4, 2, 0) ≤ Available (1, 5, 2, 0) ✔
After tentative allocation: Available = (1, 1, 0, 0).
Safety test sequence:
• P0 → Work = (1, 1, 1, 2)
• P2 → Work = (2, 4, 6, 6)
• P3 → Work = (2, 10, 9, 8)
• P4 → Work = (2, 10, 10, 12)
• P1 → completes.
Safe sequence = <P0, P2, P3, P4, P1>. Hence, the request CAN be
granted immediately.
B Describe the concept and working of a Translation Lookaside Buffer (TLB) 10
in a paging system. Explain how address translation is carried out with and
without TLB.
Definition and Need of TLB (2 Marks)
address translation without TLB (4 Marks)
address translation with TLB (4 Marks)
• A Translation Lookaside Buffer (TLB) is a special high-speed cache
that stores recent translations of virtual page numbers (VPNs) to
physical frame numbers (PFNs).
•   In a paging system, every memory access requires a page table lookup
to translate the virtual address into a physical address.
• This lookup takes extra time (additional memory access), which slows
down the system.
• The TLB reduces this delay by caching frequently used page table
entries — providing fast access to address translations.
Address translation is carried out with TLB.
********** 9 **********

[Text in pictures on this page, read by OCR]
frame e

logical address physical address 0x000
frame f
cpu slp | a |
p — Oxfff
f frame g

physical memory

page table
--- page 10 ---
Address translation is carried without TLB.
4 A Provide a comparative analysis of the Monolithic and Layered architectures 10
of Operating Systems. Include appropriate diagrams to support your
explanation.
Monolithic Architecture (3 Marks)
Layered Architecture (3 Marks)
Comparative Analysis (4 Marks)
Operating System architecture defines the structure and organization of the
OS components and their interaction with each other and hardware.
Two commonly used architectures are Monolithic and Layered
architectures.
Monolithic Architecture (3 Marks)
Explanation:
•   In a monolithic system, the entire operating system is working in a
single kernel space.
•   All system components such as   file management, process
scheduling, memory management, and device drivers are integrated
into one large block of code that runs in supervisor mode.
•   It provides high performance because there are no inter-layer
overheads, but poor modularity and difficult debugging.
Diagram:
********** 10 **********

[Text in pictures on this page, read by OCR]
logical

address
CPU +> pid

page frame

number number

E TLB hit physical

BI address
Lt | 4d }—

TLB

TLB miss

a physical
memory

page table
--- page 11 ---
Advantages:
• High execution speed (no layer overhead).
•   Efficient direct access to hardware.
Disadvantages:
•   Difficult to maintain and debug.
• Poor security and modularity—failure in one module may crash the
entire system.
Examples:
MS-DOS, UNIX (early versions), Linux (partially monolithic).
Layered Architecture (3 Marks)
Explanation:
•   In layered architecture, the OS is divided into multiple layers, each
built upon the lower one.
• Each layer performs specific functions and interacts only with its
adjacent layers.
• The bottom layer deals with hardware, while the top layer provides
user interfaces.
Diagram:
********** 11 **********

[Text in pictures on this page, read by OCR]
applications

glibc standard c library

system-call interface
file CPU
systems scheduler
networks memory
(TCP/IP) manager
block character
devices devices

device drivers

hardware
--- page 12 ---
Advantages:
•   Better modularity and maintainability.
•   Easier to test and debug individual layers.
• Higher security and reliability due to restricted communication.
Disadvantages:
• Slower execution due to layer-to-layer communication overhead.
•   Difficult to design and define proper boundaries between layers.
Examples:
THE Operating System, Windows NT, OS/2.
Comparative Analysis (4 Marks)
Feature   Monolithic OS   Layered OS
Structure   Single large kernel Multiple   layers   with   clear
interfaces
Performance   High   (no Slightly slower (due to layering)
overhead)
Modularity   Poor   Excellent
Maintainability Difficult   Easier to maintain and modify
Security   Low   (shared High   (restricted   inter-layer
kernel)   access)
Examples   MS-DOS, UNIX   Windows NT, THE OS
Conclusion:
Monolithic architecture emphasizes performance, whereas layered
architecture   emphasizes   modularity,   reliability,   and   security.
Modern operating systems often adopt a hybrid approach, combining the
speed of monolithic design with the structure of layered models.
B A disk queue with requests on cylinders 85, 170, 45, 130, 25, 115, 72, 58 10
needs to be serviced. The disk head is initially at cylinder 60, and the disk
has cylinders numbered 0-199. Calculate the total head movement for:
1. FCFS
2. SSTF
3. SCAN (assuming initial direction towards cylinder 199)
4. C-SCAN (assuming initial direction towards cylinder 199)
Compare the performance of each algorithm and determine which suits best
for this scenario.
********** 12 **********

[Text in pictures on this page, read by OCR]
application file device user
program system driver mode

messages: messages

CPU
scheduling

memory
managment

kernel
mode

interprocess
communication

microkernel

hardware
--- page 13 ---
Each Algorithm 2 Marks
Comparison 2 Marks

RK KKK RK KK 13 2h KKK RK Kk KK
--- page 14 ---
Best Algorithm for This Scenario:
SSTF provides the best performance with only 180 cylinders of movement,
making it ideal for this scenario where minimizing seek time is the priority
and the request queue is relatively small, reducing starvation risk.
5 A Describe the concept of monitors in process synchronization with internal 10
structure and functioning. Explain how monitors manage process
coordination using condition variables and synchronization primitives.
Concept of Monitors (2 Marks)
Internal Structure of a Monitor (4 Marks)
Functioning and Coordination (4 Marks)
In concurrent programming, monitors are high-level synchronization
constructs that provide a convenient and safe mechanism for process
coordination.
They encapsulate shared data, the procedures that operate on that data, and
the synchronization between concurrent processes — all within a single
module.
Monitors eliminate many of the errors possible when using low-level
primitives such as semaphores.
A monitor is a software module with:
• Shared data variables.
• A set of procedures (only one process can execute inside the
monitor at a time).
• Condition variables for process synchronization.
It ensures mutual exclusion automatically — no two processes can execute
monitor procedures simultaneously.
********** 14 **********

[Text in pictures on this page, read by OCR]
Performance Comparison

Algorithm Total Movement Characteristics

FCFS 572 Simple, fair, but high seek time

SSTF 188 Minimal movement, risk of starvation
SCAN 313 Fair, predictable, moderate performance

C-SCAN 396 More uniform wait time, higher movement
--- page 15 ---
Internal Structure of a Monitor (4 Marks)
Components:
1. Shared Data: Variables accessible only through monitor procedures.
2. Procedures: Define operations that can be performed on shared data.
3. Initialization Code: Sets up initial values for data and conditions.
4. Condition Variables: Used for process synchronization (e.g., x, y).
Pseudocode syntax of a monitor:
monitor monitor-name
{
// shared variable declarations
function P1 (…) { …. }
function P2 (…) { …. }
function Pn (…) {……}
initialization code (…) { … }
}
Diagram of Monitor Structure (1 Mark)
+-----------------------------------+
Functioning and Coordination (4 Marks)
Condition Variables and Synchronization:
• Condition variables allow a process to wait for a certain condition
to become true.
• Two basic operations are used:
o wait(c) → Process is suspended until another process signals
condition c.
o signal(c) → Wakes up one waiting process on condition c.
• Mutual exclusion: Achieved automatically; only one process
executes within the monitor.
•   Synchronization: Managed through wait and signal on condition
variables.
• No busy waiting: Blocked processes are placed in a waiting queue
inside the monitor.
Advantages of Monitors
********** 15 **********
--- page 16 ---
• Provides structured and safer synchronization compared to
semaphores.
•   Eliminates errors like deadlocks and race conditions caused by
improper semaphore use.
• Promotes modularity and clarity in concurrent program design.
B Explain how fragmentation affects memory management in operating 10
systems and illustrate the different types of fragmentation with suitable
example. A system has five memory partitions of sizes 110 KB, 480 KB,
210   KB,   350   KB,   and   140   KB   respectively.
A sequence of processes arrives for allocation in the following order: P1 =
100 KB, P2 = 200 KB, P3 = 300 KB, P4 = 140 KB, and P5 = 50 KB.
Considering Contiguous memory allocation, show the final process-to-
partition allocations using First-Fit, Best-Fit, and Worst-Fit memory
allocation strategies.
Marks Distribution:
Fragmentation 2 Marks
Types 2 marks
First Fit – 2 marks
Best Fit – 2 marks
Worst Fit – 2 marks
Fragmentation is a memory management problem that occurs when free memory
space is broken into small, non-contiguous blocks over time. It reduces the
system’s ability to allocate large continuous memory blocks to new processes,
even if total free memory is sufficient.
Fragmentation affects memory utilization and system performance, leading to
inefficient use of available RAM.
Types of Fragmentation
(a) Internal Fragmentation
Definition: Occurs when a fixed-sized memory block allocated to a process is
larger than the process’s actual memory requirement.
Cause: Fixed partitioning or paging schemes with block sizes larger than needed.
Effect: Wasted space inside the allocated partition.
Example:
Suppose a system allocates 4 KB blocks, and a process needs only 3.6 KB.
→ Unused memory = 0.4 KB per process
This 0.4 KB inside the allocated block is internally fragmented.
External Fragmentation
Definition: Occurs when total free memory exists but is scattered in non-
contiguous blocks, preventing allocation of large processes.
Cause: Dynamic memory allocation where processes are loaded and removed
frequently.
Effect: Wasted space outside allocated partitions.
Example:
Assume memory = 100 MB total. Free blocks: 20 MB + 15 MB + 10 MB (non-
contiguous).
********** 16 **********
--- page 17 ---
A process requesting 40 MB cannot be allocated, though 45 MB is free in total.
6 A   I.   Apply your understanding of process scheduling to compare Long- 10
term and Short-term schedulers in terms of their purpose, execution
frequency, speed, alternate names, and where process selection
occurs (main or secondary memory).
II.   Apply the concepts of process scheduling to justify why time-
sharing systems rely more on Short-term scheduler, while batch-
processing systems depend more on Long-term scheduler.
I.   5 Marks (One mark for each criteria)
II.   5 Marks
Solution:
i. Following are the differences between a LTS and STS:- (5 marks)
********** 17 **********
--- page 18 ---
Aspect   Long-Term Scheduler   Short-Term Scheduler
Frequency   Runs less frequently.   Runs very frequently.
Speed   Slower, as it involves   Faster, as it focuses
more complex decision-   solely on CPU allocation.
making and memory
checks.
Process   Selects processes from the   Selects processes from
selection   job pool (secondary   the ready queue (main
location   memory).   memory).
Alternate   Job Scheduler   CPU Scheduler
Name
Purpose   Balances I/O-bound and   Maximizes CPU
CPU-bound processes.   utilization and minimizes
process waiting times.
ii. Time-sharing: Many interactive users → responsiveness is critical.
The short-term scheduler (CPU scheduler) decides which process
runs next very frequently (milliseconds). Long-term scheduler is
less relevant because new jobs are admitted immediately.
Batch system: Jobs are large and submitted in bulk. The long-term
scheduler regulates how many jobs enter memory, controlling
degree of multiprogramming. If too many are admitted, system
thrashes; if too few, CPU underutilizes.
(5 marks)
B A system has 3 frames for storing process pages in main memory. Assume
that all the page frames are initially empty. Consider the page reference
string given below:
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Compute the number of page faults and show frame contents step-by-step
for:
(a) FIFO,
(b) LRU,
(c) Optimal.
Also state which algorithm gave the fewest faults.
Marks Distribution:
(FIFO: 3 marks, LRU: 3 marks, Optimal: 3 marks)
Also state which algorithm gave the fewest faults and why.(1 marks)
********** 18 **********
--- page 19 ---
Reference string length = 12. Frames = 3.
(a) FIFO (First-In, First-Out)
Frames after
Step   Ref   Fault?
step (f1,f2,f3)
1   1   1, - , -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
4   4   4, 2, 3 (1 out) Y
5   1   4, 1, 3 (2 out) Y
6   2   4, 1, 2 (3 out) Y
7   5   5, 1, 2 (4 out) Y
8   1   5, 1, 2   N
9   2   5, 1, 2   N
10   3   5, 3, 2 (1 out) Y
11   4   5, 3, 4 (2 out) Y
12   5   5, 3, 4   N
Total page faults (FIFO): 9.
(b) LRU (Least Recently Used)
LRU replaces the page that has not been used for the longest time.
Step   Ref   Frames after step Fault? Comment
1   1   1, -, -   Y   load 1
2   2   1, 2, -   Y   load 2
3   3   1, 2, 3   Y   load 3
4, 2, 3 (1 was
4   4   Y
LRU)
4, 1, 3 (2 LRU
5   1   Y
replaced)
4, 1, 2 (3 LRU
6   2   Y
replaced)
********** 19 **********
--- page 20 ---
5, 1, 2 (4 LRU
7   5   Y
replaced)
8   1   5, 1, 2   N
9   2   5, 1, 2   N
3, 1, 2 (5 LRU
10   3   Y
replaced)
3, 4, 2 (1 LRU
11   4   Y
replaced)
3, 4, 5 (2 LRU
12   5   Y
replaced)
Total page faults (LRU): 10.
(c) Optimal (Belady’s optimal algorithm) — replace the page that will not
be used for the longest time in the future.
Frames after
Step   Ref   Fault?
step
1   1   1, -, -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
1, 2, 4 (3
replaced; will be
4   4   used later   Y
sooner than 1 or
2?)*
5   1   1, 2, 4   N
6   2   1, 2, 4   N
1, 2, 5 (4
replaced: 4 next
used at step 11;
7   5   Y
1 and 2 are
needed earlier at
steps 8 and 9)
8   1   1, 2, 5   N
9   2   1, 2, 5   N
3, 2, 5 (1
replaced; 1 next
10   3   Y
used later than 2
or 5)
********** 20 **********
--- page 21 ---
3, 4, 5 (2
11   4   Y
replaced)
12   5   3, 4, 5   N
Total page faults (Optimal): 7.
Optimal gives the fewest faults (7) because it uses future knowledge. For
real systems we cannot implement Optimal, but it is used as a baseline. In
this case FIFO (9) beats LRU (10) — showing that LRU is usually good
but not always strictly better than FIFO, and that algorithms’ effectiveness
depends on the reference string.
7 A Analyze the Resource Allocation Graph
i)   Write resource allocated and requested table
ii)   Find if there is a deadlock or not? If there is no deadlock then
what will be the sequence of the process to get executed?
iii)   What will happen if one instance of resource R3 is removed
from the system.
I.   4 marks
II.   4 Marks
III.   2 Marks
i)
********** 21 **********
--- page 22 ---
II) System is in Safe State. Safe Sequence: P2, P0, P1, P3
III) There will be a deadlock in the system.
B Explain user level and kernel level threads. Which one are more light 5
weight and independent?
User and Kernel Thread 3 marks
Explanation 2 marks
Solution: User-level threads are managed entirely by a user-level thread
library without direct involvement from the operating system's kernel.
The kernel is unaware of their existence and treats the entire process
containing these threads as a single unit of execution.
(1.5 marks)
Kernel-level threads are managed directly by the operating system's
kernel. The kernel is aware of each individual kernel thread and handles
their creation, scheduling, and management.   (1.5 marks)
User-level threads are managed by a user-level thread library, making
them more lightweight as they don't require kernel intervention and offer
faster context switching, but are less independent as a blocking thread can
block the entire process. Kernel-level threads are managed by the
operating system, are more independent because they can take advantage
of multiple CPUs and are not tied to a single process's blocking state but
are more heavyweight due to the overhead of kernel mode transitions and
are slower to create and switch.
(2 marks)
C   Differentiate between sequential access and direct access methods for files. 5
Provide examples of applications where each access method would be
preferred.
Difference 4 marks
Example 1 marks
Sequential Access In sequential access, data in a file is processed in
order, one record or byte after the next. The operations typically used are
read next and write next. Repositioning within the file usually requires a
Reset (rewind) operation to go back to the beginning.
********** 22 **********
--- page 23 ---
Direct Access Direct access views a file as a numbered sequence of fixed-
length logical records. This method allows for immediate, random access
to any part of the file. Operations include explicitly reading or writing
record number (read n, write n), and moving the file pointer directly to
record (position to n).
Application Preference:
Sequential Access Preference This method is preferred for applications
where files must be processed entirely from beginning to end. Examples
include simple text files, log files (where records are appended
chronologically), and source code files read by a compiler.
Direct Access Preference Direct access is preferred for applications that
require quick, random retrieval and update of specific records. A prime
example is an Indexed/Relative File system, commonly used in databases
or any system (like a customer database or airline reservation system)
where a record must be accessed by its index or relative block number.
********** 23 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 9a8373796214

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_Computer_7047/Operating Systems/ANS_Operating Systems(702CO1C002)_2025-2026_9a83737962.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Mar 2026
- Text: mixed (16 pages), mean OCR confidence 40.0
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MBA Tech (AI)/MBA Tech (Comp)
Year: III/Sem V Spl Exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 10 Mar 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:
Explain the concept of Layered Structure vs. Monolithic Structure of an Operating
System. Compare their advantages and disadvantages with suitable examples.
[Monolithic: 1.5 | Layered: 1.5 | Comparison Table: 2]
Monolithic Structure:
• The entire OS runs as a single program in kernel mode.
• All OS services (file system, memory, I/O, scheduling) are combined into one large
block.
• Example: Early UNIX, MS-DOS.
• Advantages: Fast execution due to direct function calls; simple design.
• Disadvantages: Difficult to maintain and debug; a bug in any module can crash the
CO   whole OS.
-1;   Layered Structure:
SO   • The OS is divided into a hierarchy of layers, each built on the layer below it.
a
-1;   • Layer 0 = hardware; the topmost layer = user interface.   [5]
.
BL   • Each layer uses services only from the layer immediately below it.
-   • Example: THE OS (Dijkstra), modern Windows (partially).
1,2   • Advantages: Easier debugging, testing, and modification layer by layer.
• Disadvantages: Performance overhead due to multiple layer traversals; difficult to
define strict layer boundaries.
Monolithic   Layered
Single large kernel   Divided into layers
Fast (direct calls)   Slower (layer calls)
Hard to debug   Easier to debug
Less modular   Highly modular
CO b Consider the following Peterson's solution code for process Pi:
[5]
-2;   .   flag[i] = true; turn = j;
********** 1 **********
--- page 2 ---
SO   while (flag[j] && turn == j);
-2;   /* critical section */
BL   flag[i] = false;
-   /* remainder section */
3,4   Analyze whether this algorithm satisfies the three requirements for a critical section
solution. Justify your answer for each property.
[Mutual Exclusion: 1.5 | Progress: 1.5 | Bounded Waiting: 1.5 | Conclusion: 0.5 ]
The algorithm for Pi is:
flag[i] = true; turn = j;
while (flag[j] && turn == j); /* entry section */
/* critical section */
flag[i] = false; /* exit section */
1. Mutual Exclusion: ✓ SATISFIED
• Both processes can only be in the CS simultaneously if flag[i]=flag[j]=true AND
(turn==i AND turn==j), which is impossible since turn is a single variable.
• Conclusion: Only one process can be in the CS at a time.
2. Progress: ✓ SATISFIED
• If Pi wants to enter and Pj does not (flag[j]=false), the while condition is false and Pi
enters immediately.
• No process outside the CS blocks others indefinitely.
3. Bounded Waiting: ✓ SATISFIED
• Once Pi sets turn=j and Pj enters the CS, when Pj exits it sets flag[j]=false.
• Pi's while loop then exits; Pi enters the CS next.
• Pi waits at most one CS entry by Pj — bounded by 1.
Conclusion:
This is a valid Peterson's Solution for two processes. All three requirements are
satisfied.
Differentiate between Deadlock Prevention and Deadlock Avoidance. Explain the
concept of a Safe State and unsafe state.
[Prevention vs Avoidance: 2 | Safe State: 1.5 | Unsafe State: 1.5]
Deadlock Prevention   Deadlock Avoidance
Eliminates at least one of the Allows conditions but decides
4 necessary conditions   dynamically whether to grant
resources
More restrictive — lower   Less restrictive — better utilization
CO
-3;   resource utilization
SO   c   Applied at design time   Applied at runtime
-1;   [5]
.
BL   No need for advance   Requires Max need info from each
-   resource info   process
1,2
Example: Imposing resource Example: Banker's Algorithm
ordering
Safe State:
• A system is in a SAFE state if there exists at least one safe sequence of processes
such that each process can be allocated its maximum resources using the remaining
available + resources held by already-completed processes.
• Example: Available=3, Processes need [1,2,4]. Safe sequence: P0 → P1 → P2.
Unsafe State:
********** 2 **********
--- page 3 ---
• A system is in an UNSAFE state if NO safe sequence exists.
• An unsafe state does not guarantee deadlock, but it makes deadlock possible.
• Deadlock avoidance ensures the system never enters an unsafe state.
Explain the concept of I/O Buffering in operating systems.
[Definition: 1 | Single Buffering: 1 | Double Buffering: 1.5 | Circular Buffering:
1.5]
Definition:
I/O Buffering is a technique in which a region of physical memory (buffer) is used to
temporarily hold data while it is being transferred between two processes or between a
process and an I/O device. It bridges the speed mismatch between fast CPUs and slow
I/O devices.
1. Single Buffering:
• One buffer between the process and the device.
• The OS transfers data into the single buffer; process reads from it while next block is
CO
fetched.
-3;
• Advantage: Simple implementation; reduces process waiting time.
SO
d   • Disadvantage: Process must wait if buffer is full/empty; device is idle during data
-1;   [5]
.   consumption.
BL
2. Double Buffering:
-
• Two buffers used alternately.
1,2
• While process consumes data from Buffer-1, the device fills Buffer-2. They then
swap.
• Advantage: Producer and consumer operate concurrently — better overlap of CPU
and I/O.
• Disadvantage: Still may cause wait if both operations are heavily unbalanced in
speed.
3. Circular Buffering:
• Multiple buffers arranged in a circular queue (ring buffer).
• Producer writes to the next empty buffer; consumer reads from the next full buffer.
• Advantage: Continuous overlap of I/O and processing; handles bursts effectively.
• Disadvantage: More complex to implement; requires synchronization (semaphores).
i.   Define the concept of a monitor as a high-level synchronization construct
used in concurrent programming. Clearly describe its structure and
operational semantics. Further, compare monitors with semaphores,
highlighting key differences in abstraction level, safety, encapsulation of
shared data, and ease of use.
ii.   Develop a monitor-based solution to the Bounded Buffer (Producer–
Q2
Consumer) problem for a buffer of size N. Present the complete
a
CO   pseudocode, including shared data structures, condition variables, and the
-2;   implementations of the produce() and consume() procedures.
[10
SO
-2;   [Monitor concept & difference from semaphore: 4 | Pseudocode with   ]
BL   explanation: 4 | Trace: 2]
-   What is a Monitor?
3,4   • A Monitor is a high-level synchronization construct that encapsulates shared data,
procedures, and synchronization primitives within a single module.
• Only one process can be active inside a monitor at a time — mutual exclusion is
automatic.
• Uses condition variables for signaling: x.wait() and x.signal().
Monitor vs. Semaphores:
Monitor   Semaphore
********** 3 **********
--- page 4 ---
Mutual exclusion is automatic Must be done manually via
wait/signal
Uses condition variables   Uses integer counters
Less prone to programmer   Prone to misuse (deadlock,
error   starvation)
Structured, modular   Unstructured
Monitor-based Bounded Buffer (size N):
monitor BoundedBuffer {
int buffer[N];
int count = 0, in = 0, out = 0;
condition notFull, notEmpty;
void insert(int item) {
if (count == N) notFull.wait(); // wait if full
buffer[in] = item;
in = (in + 1) % N;
count++;
notEmpty.signal();   // signal consumer
}
int remove() {
if (count == 0) notEmpty.wait(); // wait if empty
int item = buffer[out];
out = (out + 1) % N;
count--;
notFull.signal();   // signal producer
return item;
}
}
Trace (N=2, buffer initially empty):
• Producer calls insert(x): count=0 < N → buffer[0]=x, count=1, signals notEmpty.
• Consumer calls remove(): count=1 > 0 → item=buffer[0], count=0, signals notFull.
• Producer and consumer operate safely with no race conditions since monitor
guarantees mutual exclusion.
Consider the following set of processes with their arrival times, burst times, and
priorities:
Process Arrival Time   Burst Time   Priority
P1   0   6   2
Q2   P2   2   4   4
b   P3   4   8   3
CO   P4   5   2   1
-2;   P5   6   5   2
[10
SO   (Note: Higher priority number = Higher priority)
]
-6;   I. Apply Shortest Remaining Time First (SRTF / Preemptive SJF). Draw the Gantt
BL   chart. Calculate Average Waiting Time and Average Turnaround Time.
-   II. Apply Preemptive Priority Scheduling. Draw the Gantt chart. Calculate Average
5,6   Waiting Time and Average Turnaround Time.
III. Compare both algorithms. Which performs better on Avg. Turnaround Time?
Justify.
[Gantt Chart SRTF: 2.5 | Avg WT & TAT SRTF: 2.5 | Gantt Chart Priority: 2.5 |
Avg WT & TAT Priority: 2.5]
********** 4 **********
--- page 5 ---
Processes: P1(AT=0,BT=6,Pri=2), P2(AT=2,BT=4,Pri=4), P3(AT=4,BT=8,Pri=3),
P4(AT=5,BT=2,Pri=1), P5(AT=6,BT=5,Pri=2)
Higher priority number = Higher priority.
Part I: SRTF (Preemptive SJF)
At each point, run the process with shortest remaining burst time:
• t=0: Only P1 (RT=6). Run P1.
• t=2: P2 arrives (RT=4 < P1 RT=4). Tie → continue P1. Run P1.
• t=2: P1 RT=4, P2 RT=4. Run P1 (arrived first). t=2→4, P1 RT=2.
• t=4: P3 arrives (RT=8). P1 RT=2 < P2 RT=4 < P3 RT=8. Run P1.
• t=5: P4 arrives (RT=2). P1 RT=1 < P4 RT=2. Run P1.
• t=6: P1 completes (CT=6). P5 arrives (RT=5). Ready: P2(4), P3(8), P4(2), P5(5).
Run P4.
• t=7: P4 completes (CT=7). Run P2 (RT=4).
• t=11: P2 completes (CT=11). Run P5 (RT=5).
• t=16: P5 completes (CT=16). Run P3 (RT=8).
• t=24: P3 completes (CT=24).
Gantt Chart: [P1|0-6][P4|6-7][P2|7-11][P5|11-16][P3|16-24]
Process   AT   BT   CT   TAT   WT
P1   0   6   6   6   0
P2   2   4   11   9   5
P3   4   8   24   20   12
P4   5   2   7   2   0
P5   6   5   16   10   5
Avg TAT = (6+9+20+2+10)/5 = 47/5 = 9.4
Avg WT = (0+5+12+0+5)/5 = 22/5 = 4.4
Part II: Preemptive Priority (Higher number = Higher priority)
• t=0: P1 (Pri=2) arrives. Run P1.
• t=2: P2 (Pri=4) arrives. 4>2 → Preempt P1. Run P2.
• t=4: P2 RT=2, P3 (Pri=3) arrives. 4>3 → Continue P2.
• t=5: P2 RT=1, P4 (Pri=1) arrives. P2 still highest. Continue P2.
• t=6: P2 completes (CT=6). P5 (Pri=2) arrives. Ready: P1(Pri=2,RT=4),
P3(Pri=3,RT=8), P4(Pri=1,RT=2), P5(Pri=2,RT=5). Run P3.
• t=14: P3 completes (CT=14). Run P1 or P5 (Pri=2 tie, P1 arrived first). Run P1.
• t=18: P1 completes (CT=18). Run P5.
• t=23: P5 completes (CT=23). Run P4.
• t=25: P4 completes (CT=25).
Gantt Chart: [P1|0-2][P2|2-6][P3|6-14][P1|14-18][P5|18-23][P4|23-25]
Process   AT   BT   CT   TAT   WT
P1   0   6   18   18   12
P2   2   4   6   4   0
P3   4   8   14   10   2
P4   5   2   25   20   18
P5   6   5   23   17   12
Avg TAT = (18+4+10+20+17)/5 = 69/5 = 13.8
Avg WT = (12+0+2+18+12)/5 = 44/5 = 8.8
Comparison:
********** 5 **********
--- page 6 ---
• SRTF performs better: Avg TAT = 9.4 vs 13.8 for Priority; Avg WT = 4.4 vs 8.8.
• SRTF minimizes burst-based waiting; Priority favors high-priority processes causing
starvation of P4.
Consider the following system snapshot with 4 processes and 3 resource types (X, Y,
Z). Total resources: X=10, Y=5, Z=7.
Process   Allocation(X,Y,Z)   Max(X,Y,Z)
P0   0 1 0   7 5 3
P1   2 0 0   3 2 2
P2   3 0 2   9 0 2
P3   2 1 1   2 2 2
Using Banker's Algorithm:
I. Calculate the Available resource vector.
II. Compute the Need matrix.
III. Determine whether the system is in a safe state. If yes, find ALL possible safe
sequences.
[Available vector: 2 | Need matrix: 2 | Safe sequence(s): 4 | P0 request: 2]
I. Available = Total – Allocated = (10-7, 5-2, 7-3) = (3, 3, 4)
II. Need Matrix = Max – Allocation:
Process   Need X   Need Y   Need Z
Q3
a   P0   7   4   3
CO
P1   1   2   2
-2;
[10
SO   P2   6   0   0   ]
-1;
BL   P3   0   1   1
-   III. Safety Check (Available = 3,3,4):
5,6   • P1: Need(1,2,2) ≤ Avail(3,3,4) ✓ → Run P1. Avail = 3+2,3+0,4+0 = 5,3,4.
• P3: Need(0,1,1) ≤ Avail(5,3,4) ✓ → Run P3. Avail = 5+2,3+1,4+1 = 7,4,5.
• P0: Need(7,4,3) ≤ Avail(7,4,5) ✓ → Run P0. Avail = 7+0,4+1,5+0 = 7,5,5.
• P2: Need(6,0,0) ≤ Avail(7,5,5) ✓ → Run P2. Avail = 7+3,5+0,5+2 = 10,5,7.
✓ System is in SAFE STATE.
Safe Sequence: P1 → P3 → P0 → P2
Additional Request: P0 requests (0,1,0):
• Check: Request(0,1,0) ≤ Need P0(7,4,3) ✓
• Check: Request(0,1,0) ≤ Available(3,3,4) ✓
• Tentatively grant: Avail = (3,2,4). Run safety check again:
o P1: Need(1,2,2) ≤ (3,2,4) ✓ → Avail = (5,2,4)
o P3: Need(0,1,1) ≤ (5,2,4) ✓ → Avail = (7,3,5)
o P0: Need(7,3,3) ≤ (7,3,5) ✓ → Avail = (7,4,5)
o P2: Need(6,0,0) ≤ (7,4,5) ✓ → Avail = (10,4,7)
✓ Safe Sequence still exists: P1→P3→P0→P2. Request GRANTED.
Q3   Compare paging and segmentation in memory management with respect to internal
b   and external fragmentation. Briefly explain how paging results in internal
CO   fragmentation while segmentation may lead to external fragmentation.
-3;
[10
SO   [Paging explanation + diagram: 3 | Segmentation explanation + diagram: 3 |
]
-1;   Comparison table: 2 | Example: 2]
BL   Paging:
-   • Logical memory is divided into fixed-size pages; physical memory into same-size
1,2   frames.
********** 6 **********
--- page 7 ---
• OS maintains a page table: maps page number → frame number.
• Logical Address = (Page number p, Offset d). Physical Address = Frame(p) ×
frame_size + d.
• Eliminates external fragmentation but may have internal fragmentation (last page
partially filled).
Segmentation:
• Logical memory is divided into variable-sized segments corresponding to logical
units (code, stack, heap).
• OS maintains a segment table: maps segment number → base address + limit.
• Logical Address = (Segment number s, Offset d). If d < limit[s] → Physical =
base[s] + d. Else trap.
• No internal fragmentation, but suffers from external fragmentation over time.
Comparison:
Parameter   Paging   Segmentation
Unit Size   Fixed (pages)   Variable (segments)
Internal   Yes (last page) No
Fragmentation
External   No   Yes
Fragmentation
Programmer   Transparent   Visible (logical)
Visibility
Address Structure   Page no. +   Segment no. + offset
offset
Protection   At page level   At segment level (more
natural)
********** 7 **********

[Text in pictures on this page, read by OCR]
-————> 5

r— limit [base

Segment Table

CPU =| Ss

Logical
Address

offse\ yes
fee

no

Invalid Address Physical memory
--- page 8 ---
Modern Use   Preferred   Combined (x86 segmented
(simpler)   paging)
Explain the concept of system calls in an operating system and describe their role in
enabling interaction between user programs and the operating system. Further, discuss
the different types of system calls and provide at least two examples for each
category. Support your answer with a system call flow diagram.
[Definition: 2 | Types with examples (4 types × 1.5): 6 | System call flow diagram:
2]
What is a System Call?
A system call is the programmatic interface through which a user-level program
requests services from the OS kernel. When a system call is invoked, the CPU
switches from user mode to kernel mode (via a trap/interrupt), executes the requested
service, then returns.
Types of System Calls with Examples:
Q4   • 1. Process Control: Create, terminate, load, and execute processes.
a   o Examples: fork() – creates a child process; exit() – terminates a process; wait() –
CO   waits for child.
-1;   • 2. File Management: Create, open, read, write, and delete files.
[10
SO   o Examples: open('/file.txt', O_RDONLY) – opens a file; read(fd, buf, n) – reads n
]
-3;   bytes; write(), close().
BL   • 3. Device Management: Request and release I/O devices; read/write devices.
-   o Examples: ioctl() – device-specific control; read(device) / write(device).
3,4   • 4. Information Maintenance: Get/set system time, process attributes, system data.
o Examples: getpid() – get process ID; time() – get system time; alarm().
• 5. Communication: Inter-process communication via pipes, sockets, or messages.
o Examples: pipe() – creates a pipe; socket(), send(), recv() – for network IPC;
shmget() – shared memory.
System Call Execution Flow:
• 1. User program calls library function (e.g., printf → write).
• 2. Library places system call number in CPU register and executes TRAP/INT
instruction.
• 3. CPU switches to kernel mode (mode bit = 0); jumps to system call handler in
kernel.
• 4. Kernel identifies the call number, executes the corresponding kernel routine.
• 5. Result placed in register; CPU switches back to user mode (mode bit = 1);
resumes user program.
A disk queue has pending requests for the following cylinders: 176, 79, 34, 60, 92, 11,
41, 114. The disk head is currently positioned at cylinder 50, moving towards the
lower cylinders. The disk has cylinders numbered 0 to 199.
Q4   Calculate the total head movement (in cylinders) for:
b   I. SCAN (Elevator Algorithm) – moving towards lower cylinders first.
CO   II. SSTF
-3;   III. FCFS
[10
SO   Draw the head movement sequence for each algorithm. Compare their performance
]
-6;   and state which algorithm is best suited for a real-time database server. Justify your
BL   answer.
-   [Each algorithm with sequence + movement: 3 × 3 = 9 | Comparison &
5,6   recommendation: 1]
Requests: 176, 79, 34, 60, 92, 11, 41, 114   | Head at: 50   | Moving: towards lower
cylinders   | Disk: 0–199
Sorted requests: 11, 34, 41, 60, 79, 92, 114, 176
********** 8 **********
--- page 9 ---
I. SCAN (Elevator, moving towards 0 first):
Sequence: 50 → 41 → 34 → 11 → 0 → 60 → 79 → 92 → 114 → 176
• 50→41: 9 | 41→34: 7 | 34→11: 23 | 11→0: 11 | 0→60: 60 | 60→79: 19 | 79→92: 13
| 92→114: 22 | 114→176: 62
Total SCAN = 9+7+23+11+60+19+13+22+62 = 226 cylinders
II. SSTF (Shortest Seek Time First):
Always pick the closest request to current head position:
• 50 → 60(10) → 41(19) → 34(7) → 11(23) → 79(68) → 92(13) → 114(22) →
176(62)
Total SSTF = 10+19+7+23+68+13+22+62 = 224 cylinders
III. FCFS (First Come First Served):
Order: 176, 79, 34, 60, 92, 11, 41, 114
• 50→176: 126 | 176→79: 97 | 79→34: 45 | 34→60: 26 | 60→92: 32 | 92→11: 81 |
11→41: 30 | 41→114: 73
Total FCFS = 126+97+45+26+32+81+30+73 = 510 cylinders
Comparison:
Algorithm Total   Characteristic
Movement
SCAN   226   Fair, predictable
SSTF   224   Near-optimal but may
starve
FCFS   510   Simple but inefficient
• Best for a real-time database server: SCAN — provides predictable, fair service with
low average seek time, preventing starvation unlike SSTF.
Define a race condition and explain the critical section problem in concurrent systems.
Discuss how the compare-and-swap (CAS) atomic instruction can be used to address
the critical section problem. Provide a detailed explanation of the working
mechanism, including the logic of the atomic operation and how it ensures mutual
exclusion.
[Race Condition: 2 | Critical Section Problem + 3 requirements: 4 | Compare and
swap solution: 4]
Race Condition:
Q5
A race condition occurs when the outcome of a program depends on the relative order
a
of execution of concurrent processes or threads accessing shared data. The final result
CO
becomes unpredictable because multiple processes read and write shared data without
-2;
synchronization.   [10
SO
• Example: Two processes both read counter=5, each increment to 6, and both write 6   ]
-3;
— but expected result is 7. The race leads to lost update.
BL
-
Critical Section Problem:
3,4
A critical section is a segment of code in which a process accesses shared resources
(variables, files, etc.). The Critical Section Problem is to design a protocol ensuring
that when one process is executing in its critical section, no other process can execute
in its critical section.
Structure of a process with CS:
do {
/* Entry Section */
/* Critical Section */
********** 9 **********
--- page 10 ---
/* Exit Section */
/* Remainder Section */
} while (true);
Three Requirements for a Valid Solution:
• 1. Mutual Exclusion: Only one process can be in the CS at a time.
• 2. Progress: If no process is in the CS and some wish to enter, selection cannot be
postponed indefinitely.
• 3. Bounded Waiting: There is a bound on the number of times other processes can
enter before a waiting process is allowed in.
The compare-and-swap (CAS) instruction is a hardware-supported atomic operation
used to achieve synchronization. It compares the contents of a memory location with a
given value and updates it only if the comparison is successful. Since the operation is
atomic, no other process can interrupt it during execution.
CAS operation:
boolean compare_and_swap(int *value, int expected, int new_value)
{
if (*value == expected) {
*value = new_value;
return true;
}
else
return false;
}
Using CAS for critical section control:
do {
while (!compare_and_swap(&lock, 0, 1))
;   // busy waiting
/* Critical Section */
lock = 0;
/* Remainder Section */
} while (true);
Explanation:
•   Initially, lock = 0, indicating that the critical section is free.
• A process attempting entry executes compare_and_swap(&lock, 0, 1).
•   If the lock value is 0, it is atomically changed to 1, granting access to the
critical section.
• Other processes fail the comparison and continue waiting.
•   After execution, the process releases the lock by setting it back to 0.
Thus, CAS guarantees mutual exclusion through atomic execution, ensures progress
because any free lock can be acquired immediately, and supports bounded waiting
under fair scheduling, thereby providing an effective solution to the critical section
problem.
i.   How base and limit registers provide memory protection in an OS.
Q5   ii.   Consider the following memory partitions (in order): 100 KB, 500 KB, 200
b   [10
KB, 300 KB, 600 KB. Processes to be allocated (in order): 212 KB, 417
CO   ]
-3;   KB, 112 KB, 426 KB. Apply First-Fit, Best-Fit, and Worst-Fit allocation
algorithms. For each:
********** 10 **********
--- page 11 ---
SO   a. Show which partition each process is placed in.
-6;   b. Calculate the internal fragmentation for each allocation.
BL   c. Identify which processes (if any) cannot be allocated.
-
[Base/Limit explanation: 2 | First-Fit: 2.5 | Best-Fit: 2.5 | Worst-Fit: 2.5 |
5,6
Summary: 0.5]
Base and Limit Registers:
• Base Register: Holds starting physical address of process memory.
• Limit Register: Holds the size (range) of the process's addressable memory.
• For every memory access, hardware checks: if (address >= base && address <
base+limit) → Allow, else → Trap to OS.
• Example: P1 base=2000, limit=500 → can access 2000–2499. If P1 accesses 2600
→ illegal → trap.
Partitions: 100 KB, 500 KB, 200 KB, 300 KB, 600 KB
Processes (in order): 212 KB, 417 KB, 112 KB, 426 KB
First-Fit (allocate to first partition that fits):
• 212 KB → 500 KB partition (first fit). Remaining: 288 KB. IF = 288 KB.
• 417 KB → 600 KB partition. Remaining: 183 KB. IF = 183 KB.
• 112 KB → 100 KB partition? No (100 < 112). Try 288 KB remaining in 500 KB
slot. If tracking as separate: 288 KB fits. IF = 176 KB.
• 426 KB → No remaining partition fits (183 KB left in 600 KB, 300 KB, 200 KB all
< 426 KB). CANNOT ALLOCATE.
Process   Size   Partition   Allocated   IF
212 KB   212   500 KB   Yes   288 KB
417 KB   417   600 KB   Yes   183 KB
112 KB   112   200 KB   Yes   88 KB
426 KB   426   None   No   —
Best-Fit (allocate to smallest partition that fits):
Process   Size   Best Partition   Allocated   IF
212 KB   212   300 KB   Yes   88 KB
417 KB   417   500 KB   Yes   83 KB
112 KB   112   200 KB   Yes   88 KB
426 KB   426   600 KB   Yes   174 KB
Total IF (Best-Fit) = 88+83+88+174 = 433 KB
Worst-Fit (allocate to largest partition that fits):
Process   Size   Worst Partition   Allocated   IF
212 KB   212   600 KB   Yes   388 KB
417 KB   417   500 KB   Yes   83 KB
112 KB   112   388 KB rem.   Yes   276 KB
426 KB   426   None fits   No   —
********** 11 **********
--- page 12 ---
Best-Fit allocates all 4 processes — recommended for minimizing wasted
memory.
Define the term process in the context of an operating system and describe & show the
various process states along with their transitions. Provide a detailed explanation of
the different types of schedulers in an operating system, outlining their roles and
functions in process management.
[Process definition: 1 | State diagram + 5 states: 4 | State transitions: 2 |
Schedulers (3 types): 3]
Process and Process State Transitions:
A process is a program in execution. It has a state that changes during its lifetime. The
OS maintains a Process Control Block (PCB) for each process.
Five-State Process Model:
• 1. New: Process is being created (PCB allocated, resources not yet assigned).
• 2. Ready: Process is in memory, waiting to be assigned to the CPU.
• 3. Running: Process is currently being executed by the CPU.
• 4. Waiting (Blocked): Process is waiting for an I/O event or resource to become
available.
• 5. Terminated: Process has finished execution; OS reclaims resources.
State Transitions:
• New → Ready: Admitted by the long-term scheduler (process loaded into memory).
• Ready → Running: CPU scheduler dispatches the process.
Q6   • Running → Waiting: Process requests I/O or waits for an event (page fault, lock).
a   • Waiting → Ready: I/O completes or event occurs; process moved back to ready
CO   queue.
-2;   • Running → Ready: Preempted by higher-priority process or time quantum expires.
SO   • Running → Terminated: Process completes or is killed.   [10
]
-2;
BL
-
3,4
Types of Schedulers:
• 1. Long-Term Scheduler (Job Scheduler):
o Controls the degree of multiprogramming — decides which processes to admit into
the ready queue from the job pool.
o Runs infrequently (seconds to minutes). Balances CPU-bound and I/O-bound
processes.
o Found in batch systems; often absent in time-sharing/interactive OS.
• 2. Short-Term Scheduler (CPU Scheduler):
o Selects which ready process gets the CPU next. Runs frequently (milliseconds).
o Must be very fast — a slow scheduler wastes CPU cycles.
o Implements scheduling algorithms: FCFS, SJF, Priority, Round Robin, etc.
• 3. Medium-Term Scheduler (Swapper):
o Temporarily removes processes from memory and swaps them to disk (swapping
out) to reduce the degree of multiprogramming.
o Re-introduces processes (swapping in) when memory becomes available.
o Helps maintain a mix of CPU-bound and I/O-bound processes.
Q6   A system uses 3 frames for page storage (initially all empty). Consider the page   [10
b   reference string:   ]
********** 12 **********
--- page 13 ---
CO   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1
-3;   I. Simulate FIFO page replacement. Show the frame state at each step and count
SO   page faults.
-6;   II. Simulate LRU page replacement. Show the frame state at each step and count page
BL   faults.
-   III. Simulate Optimal page replacement. Show the frame state at each step and count
5,6   page faults.
IV. Now repeat FIFO with 4 frames. Compare with 3-frame FIFO result.
V. Does Belady's Anomaly occur in this case? Which algorithm(s) are immune to
Belady's Anomaly and why?
[FIFO 3-frame: 2 | LRU 3-frame: 2 | Optimal 3-frame: 2 | FIFO 4-frame: 2 |
Belady's discussion: 2]
Reference String: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
I. FIFO (3 frames) — Replace the oldest loaded page:
7   0   1   2   0   3   0   4   2   3   0   3   2   1   2   0   1   7   0
7   0   1   2   2   3   3   4   4   3   0   0   0   1   1   0   0   7   7
0   1   1   0   0   0   4   2   2   2   3   2   1   2   2   1   1   0
1   2   0   3   0   4   2   3   0   3   2   1   2   0   1   7   0
F F F F   F F F   F F   F F   F F F F
FIFO Page Faults (3 frames) = 15
II. LRU (3 frames) — Replace least recently used page:
• 7→F | 0→F | 1→F | 2→F(evict 7) | 0→hit | 3→F(evict 1) | 0→hit | 4→F(evict 2) |
2→F(evict 3) | 3→F(evict 0) | 0→F(evict 4) | 3→hit | 2→hit | 1→F(evict 0) | 2→hit |
0→F(evict 3) | 1→hit | 7→F(evict 2) | 0→hit | 1→hit
LRU Page Faults (3 frames) = 12
III. Optimal (3 frames) — Replace page not used for longest future time:
• 7→F | 0→F | 1→F | 2→F(evict 7, used farthest) | 0→hit | 3→F(evict 1, not used
soon) | 0→hit | 4→F(evict 3) | 2→hit | 3→F(evict 4) | 0→hit | 3→hit | 2→hit |
1→F(evict 3) | 2→hit | 0→hit | 1→hit | 7→F(evict 1) | 0→hit | 1→F(evict 7)
Optimal Page Faults (3 frames) = 9
IV. FIFO with 4 frames:
• 7→F | 0→F | 1→F | 2→F | 0→hit | 3→F(evict 7) | 0→hit | 4→F(evict 0) | 2→hit |
3→hit | 0→F(evict 1) | 3→hit | 2→hit | 1→F(evict 2) | 2→F(evict 3) | 0→hit | 1→hit |
7→F(evict 4) | 0→hit | 1→hit
FIFO Page Faults (4 frames) = 10
V. Belady's Anomaly:
• 3-frame FIFO = 15 faults; 4-frame FIFO = 10 faults → More frames = fewer faults
here. No anomaly in this case.
• Belady's Anomaly: For FIFO, increasing the number of frames can sometimes
INCREASE page faults. Classic example: reference string 1,2,3,4,1,2,5,1,2,3,4,5 gives
9 faults for 3 frames but 10 for 4 frames.
• Immune algorithms: LRU and Optimal are stack algorithms — they never exhibit
Belady's Anomaly. For any stack algorithm, increasing frames always reduces or
maintains page faults.
Q7   Define a Resource Allocation Graph (RAG) and explain how it is used to detect
a   deadlocks.
CO   Consider a system with 3 processes (P1, P2, P3) and   [10
-2;   3 resources (R1: 1 instance, R2: 2 instances, R3: 1 instance):   ]
SO   - P1 holds R1, requests R2
-1;   - P2 holds R2 (one instance), requests R3
********** 13 **********
--- page 14 ---
BL   - P3 holds R3, requests R2
-   - P2 also holds R2 (second instance)
5,6   I. Draw the complete Resource Allocation Graph.
II. Detect if deadlock exists. Justify using cycle detection.
III. If deadlock exists, which process should be terminated first to resolve it with
minimum cost? If not, state the execution order.
IV. How would the RAG change if R2 had 3 instances instead of 2? Would deadlock
still occur?
[RAG definition + edge types: 2 | Draw RAG: 3 | Deadlock detection &
justification: 3 | What-if R2=3: 2]
What is a Resource Allocation Graph?
A RAG is a directed graph used by the OS to represent the state of resource
allocation. It has two types of nodes:
• Process nodes (circles): P1, P2, P3.
• Resource nodes (rectangles with dots for instances): R1, R2, R3.
Two types of edges:
• Request edge (Pi → Rj): Process Pi is waiting for an instance of Rj.
• Assignment edge (Rj → Pi): An instance of Rj is held by Pi.
Given System:
• R1: 1 instance | R2: 2 instances | R3: 1 instance
• P1: holds R1, requests R2
• P2: holds R2 (1 instance) AND R2 (2nd instance), requests R3
• P3: holds R3, requests R2
RAG Edges:
• Assignment: R1 → P1, R2 → P2 (inst 1), R2 → P2 (inst 2), R3 → P3
• Request: P1 → R2, P2 → R3, P3 → R2
Deadlock Detection:
Check for cycle:
• P1 → R2 → P2 (P2 holds both instances of R2, none available) → R3 → P3 → R2
→ P2...
• Cycle detected: P1 → R2 → P2 → R3 → P3 → R2 → P2 (circular wait).
• Since R2 has only 2 instances and both are held by P2, neither P1 nor P3 can
proceed.
DEADLOCK EXISTS. Processes P1, P2, P3 are all deadlocked.
Resolution — Process Termination:
• Terminate P2: P2 releases R2 (both instances) and R3.
• After termination: R2 available (2), R3 available (1). P1 gets R2 (executes, releases
R1). P3 gets R2 (executes). Deadlock resolved.
What-if: R2 has 3 instances?
• P2 holds 2 instances of R2. Remaining = 1 instance of R2 available.
• P1 requests R2 → granted (gets the 1 remaining). P1 executes, releases R1 and R2.
• Now R2 available = 3. P3 can get R2 and proceed.
• No circular wait possible. DEADLOCK WOULD NOT OCCUR with R2 = 3
instances.
Differentiate between preemptive and non-preemptive CPU scheduling techniques by
Q7
highlighting their key characteristics and operational differences.   [5]
b
********** 14 **********
--- page 15 ---
CO   [Preemptive vs Non-Preemptive: 5
-   I. Preemptive vs Non-Preemptive Scheduling:
2,3   Preemptive   Non-Preemptive
;
SO   CPU can be taken from a   CPU is held until process terminates
-1;   running process   or blocks
BL
-   Better responsiveness for   Simple to implement
1,2   interactive systems
Requires context save/restore No mid-execution interruption
on each preemption
Risk of race conditions on   No preemption-related
shared data   synchronization issues
Examples: Round Robin,   Examples: FCFS, Non-Preemptive
Preemptive Priority, SRTF   SJF, Non-Preemptive Priority
Best for: Time-sharing, real-   Best for: Batch processing systems
time OS
Explain the various file allocation methods used in operating systems, supported with
appropriate examples.
File Allocation Methods (3 types): 5
File Allocation Methods:
• 1. Contiguous Allocation:
o Each file occupies a set of contiguous blocks on disk.
o Directory entry stores starting block and length.
Q7   o Advantages: Simple; supports sequential and direct access; fast read.
C   o Disadvantages: External fragmentation; file size must be known at creation; difficult
CO   to extend.
-   o Example: A file of 5 blocks starting at block 10 uses blocks 10,11,12,13,14.
2,3
;   • 2. Linked Allocation:   [5]
SO   o File is a linked list of disk blocks scattered anywhere on disk.
-1;   o Each block contains a pointer to the next block. Directory stores first and last block.
BL   o Advantages: No external fragmentation; files can grow dynamically.
-   o Disadvantages: No direct access (must traverse from start); pointer overhead;
1,2   reliability issues if pointer is lost.
o Variant: FAT (File Allocation Table) — pointers stored in a table in memory, not in
blocks.
3. Indexed Allocation:
o Each file has an index block containing all pointers to its data blocks.
o Directory stores the address of the index block.
o Advantages: Supports direct access; no external fragmentation; files can grow.
o Disadvantages: Index block overhead; for large files, multi-level index needed.
o Example: UNIX inode structure — uses direct, single-indirect, double-indirect,
triple-indirect pointers.
********** 15 **********
--- page 16 ---
FRR ICR 7 6 AC OH
````

## 2025-26 · Re-Exam · Sem 9 · Answer key · paper e304ad59d8e2

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_09/Re-Exam/Integrated_Computer_7032/Operating Systems/ANS_Operating Systems(702CO1C002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: mixed (23 pages), mean OCR confidence 70.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. TECH (CSE - DS)/B. Tech Intg. (CE)/MASTER OF BUSINESS ADMINISTRATION
IN TECHNOLOGY MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA
Tech (Comp)
Year: II / III / V/Sem 3 Re-exam/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Operating Systems
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1 A What are the various components of an Operating System? Briefly explain 5
with the help of a diagram.
Explanation of components (any four) 1 mark each (4 Marks)
Diagram   1 mark
The main components of an operating system are:
1. Process Management
o Handles creation, scheduling, and termination of processes.
o Ensures fair CPU allocation among processes.
2. Memory Management
o Manages primary memory allocation and deallocation.
o Keeps track of memory usage and optimizes performance.
3. File Management
o Organizes, stores, retrieves, and manages data in files.
o Maintains directories and provides file access control.
4. Device Management
o Controls and coordinates input/output devices via device
drivers.
o Ensures efficient and conflict-free resource usage.
5. Security and Protection
o Protects data and system resources from unauthorized
access.
o Implements authentication, authorization, and encryption
mechanisms.
********** 1 **********
--- page 2 ---
B Analyze the code for Process Pi and Pj and state whether it satisfies the 5
three requirements for the solution to the critical section problem or not.
Justify your answer.
For process Pi:
do {
flag[i] = true;
turn = j;
while (flag[j] && turn == j);
// Critical Section
flag[i] = false;
// Remainder Section
} while (true);
For process Pj:
do {
flag[j] = true;
turn = i;
while (flag[i] && turn == i);
// Critical Section
flag[j] = false;
// Remainder Section
} while (true);
Final verdict: 2 marks
Justification each condition: 1 Mark (3 marks)
Yes, it satifies all the three conditions of mutual exclusion.
A. Mutual exclusion is preserved
Pi enters CS only if:
either flag[j] = false or turn = i
B. Progress requirement is satisfied: If a process wants to enter the
critical section, it waits only if the other process is inside or waiting
to enter, and it is the other process’s turn.
If the other process is not interested (flag[j] == false), then the first
process proceeds immediately without waiting.
Also, the turn variable guarantees that the processes alternate access
if both want to enter, so no process can block the other indefinitely.
********** 2 **********

[Text in pictures on this page, read by OCR]
user and other system programs

GUI touch screen | command line

user interfaces

system calls

program vO file a resource
communication

. A a accounting
execution operations systems allocation

protection
and
security

error
detection
services

operating system

hardware
--- page 3 ---
C. Bounded-waiting requirement is met: The turn variable acts as a fair
"token" passed between the two processes, ensuring that after one
process finishes, the other will eventually get the turn.
C Describe the process of deadlock recovery after detection. What are the
common methods used? Explain any two.
Deadlock Recovery 1 mark
Methods 4 marks
Process of Deadlock Recovery (1 Marks)
Once a deadlock is detected (usually using the resource allocation graph or
Banker’s algorithm), the OS performs the following steps:
1. Identify deadlocked processes and resources.
2. Select a recovery method — terminate processes, preempt
resources, or roll back processes.
3. Recover the system by releasing held resources and restarting
affected processes.
4. Resume normal operation.
Common Methods of Deadlock Recovery
The two main categories are:
1. Process Termination — killing one or more processes involved in
the deadlock.
2. Resource Preemption — temporarily taking resources away from
processes.
Other less common methods:
• Process Rollback (restore to a safe checkpoint).
• Manual Intervention (in simple or embedded systems).
(i) Process Termination (2 Marks)
• Concept:
Abort one or more processes involved in the deadlock until the cycle
is broken.
• Approaches:
1. Abort all deadlocked processes.
▪ Simple but costly; results in loss of work.
2. Abort processes one at a time until the deadlock cycle is
resolved.
•   Selection   Criteria:
When choosing which process to terminate, the OS considers:
1. Process priority and importance.
2. Amount of CPU time consumed.
3. Number and type of resources held.
4. Whether the process can be restarted easily.
• Advantages:
1. Straightforward and guaranteed recovery.
• Disadvantages:
1. May lead to loss of significant computation progress.
2. System performance temporarily degrades.
(ii) Resource Preemption (2 Marks)
• Concept:
Temporarily take away (preempt) resources from some processes
and give them to others to break the deadlock.
********** 3 **********
--- page 4 ---
• Steps Involved:
1. Select a victim process – the one whose resource preemption
has the least cost.
2. Save its state (checkpoint) – so it can be restarted later.
3. Reassign its resources to other waiting processes.
•   Challenges:
1. Rollback: The victim process must be rolled back to a safe
state.
2. Starvation: A process may be repeatedly chosen as a victim;
hence, the OS must keep track of how often each process is
preempted.
• Advantages:
1. Allows partial progress of other processes.
• Disadvantages:
1. Complex to implement and may lead to instability if done
repeatedly.
D Describe the concept of I/O management in an operating system and apply
your knowledge to identify key factors that can enhance I/O performance.
I/O Management 2 Marks
Factors 3 Marks (at least 3)
I/O management is a major component of operating system design that
handles the interaction between the computer system and I/O devices.
Key Components:
•   Ports, Buses, Controllers: Connect various devices to the system
• Device Drivers: Encapsulate device-specific details and present
uniform device-access interface to I/O subsystem
• I/O Hardware: Manages incredible variety of devices (storage,
transmission, human-interface)
I/O Methods:
•   Polling: CPU repeatedly checks device status (inefficient for slow
devices)
•   Interrupts: Device signals CPU when ready (efficient, used for
time-sensitive operations)
• DMA (Direct Memory Access): Transfers data directly between
device and memory without CPU involvement
I/O Operations:
• Blocking I/O: Process suspended until I/O completed
• Nonblocking I/O: Returns immediately with available data
• Asynchronous I/O: Process continues while I/O executes
Factors for Improving I/O Performance
1. Reduce Context Switches
• Minimize switching between processes during I/O operations
2. Reduce Data Copying
• Minimize copying data between kernel and user space
3. Reduce Interrupts
• Use large transfers instead of multiple small ones
• Employ smart controllers
• Use polling when appropriate
4. Use DMA (Direct Memory Access)
• Allow devices to transfer data directly to/from memory
********** 4 **********
--- page 5 ---
• Frees CPU from data transfer burden
5. Use Smarter Hardware Devices
•   Intelligent controllers with built-in processing capabilities
6. Balance System Resources
• Balance CPU, memory, bus, and I/O performance for highest
throughput
7. Move User-mode Processes to Kernel Threads
• Reduces overhead for frequently used I/O operations
8. Implement Efficient Buffering and Caching
• Buffer data to handle speed/size mismatches
• Cache frequently accessed data on faster devices
2 A Examine the synchronization problem in operating systems, identifying the
challenges it creates. Analyse how counting semaphores provide a
structured solution and resolve these issues in the Readers–Writers
problem.
Explain Synchronization Problem in Detail [4 marks]
Readers-Writers Problem [6 marks]
The Synchronization Problem arises in a multi-process or multi-threaded
environment when multiple processes concurrently access and manipulate
shared data. The core issue is that the final result of the execution depends
on the specific order in which instructions are interleaved, leading to
unpredictable and inconsistent results. This is known as a race condition.
Causes and Consequences:
1. Race Condition: Occurs when several processes access and modify
the same shared data concurrently, and the outcome of the execution
depends on the order of access.
2. Data Inconsistency: The primary consequence is that the shared data
may end up in a corrupted or inconsistent state.
Example (The Critical Section Problem): A simple counter shared by two
threads, one incrementing and the other decrementing. The operations
(Read → Modify → Write) are not atomic. If the operations are interrupted
and interleaved, the final count can be incorrect (e.g., instead of
100→101→100, it might become 100→101→101).
Requirements for a Correct Solution:
1. Mutual Exclusion: Only one process can be executing in its critical
section at any time.
2. Progress: If no process is executing in its critical section and some
processes wish to enter, then only those processes not in their
remainder sections can participate in deciding which will enter next,
and this selection cannot be postponed indefinitely.
3. Bounded Waiting: There must be a limit on the number of times
other processes are allowed to enter their critical sections after a
process has made a request to enter its critical section and before
that request is granted.
B. Counting Semaphore for Readers-Writers Problem [6 marks]
The Readers-Writers Problem is a classic synchronization problem where
multiple processes try to access a shared database.
● Readers only read the data and can do so concurrently.
● Writers modify the data and must have exclusive access (no other
reader or writer allowed).
********** 5 **********
--- page 6 ---
A Counting Semaphore (and a Binary/Mutex semaphore) can be used to
manage this access
Writer Process Logic: The writer needs exclusive access. It only needs to
wait on the general lock (wrt).
do {
wait(wrt);
// Writing is performed
signal(wrt);
} while (TRUE);
Reader Process Logic: Readers need to coordinate using readcount and
the wrt lock.
do {
wait(mutex);   // 1. Lock the readcount variable
readcount++;
if (readcount == 1) {   // 2. First reader locks out the writer
wait(wrt);
}
signal(mutex);   // 3. Unlock the readcount variable
// Reading is performed
wait(mutex);   // 4. Lock the readcount variable
readcount--;
if (readcount == 0) {   // 5. Last reader signals the writer
signal(wrt);
}
signal(mutex);   // 6. Unlock the readcount variable
} while (TRUE);
B Consider the following set of processes, each with varying arrival times
and burst times.
Process   Arrival Time   Burst Time
P1   0   7
P2   2   4
P3   4   1
P4   5   4
P5   6   3
i. Using the SRTF scheduling algorithm, determine the average
waiting time and average response time.
ii. Using the Round-Robin scheduling algorithm with time quantum =
3, determine the average waiting time and average response time.
********** 6 **********
--- page 7 ---
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
(GC = 2 marks, Avg. WT = 1.5 marks, Avg. RT = 1.5 marks)
3 A Consider the following snapshot of a system running 5 processes:
Pro- Allocation   Max   Available
cess A   B   C   D A   B   C D A B   C D
P0   0   0   1   2 0   0   1   2 1   5   2   0
P1   1   0   0   0 1   7   5   0
P2   1   3   5   4 2   3   5   6
P3   0   6   3   2 0   6   5   2
********** 7 **********
--- page 8 ---
P4   0   0   1   4 0   6   5   6
Answer the following: -
i. How many resources of type A, B, C, D are there?
ii.   Calculate the need matrix?
iii.   Determine if the system is safe or not.
iv.   What will happen if the resource request (0, 4, 2,0) for process P1
arrive, can the system accept this request immediately?
Calculation of total resources 1.5 Marks
Finding the need matrix 1.5 Marks
Safe Sequence 3 Marks
Additional Request 3 Marks
The total number of resources of each type is calculated as:
Total = Allocation (sum) + Available
• A = 2 + 1 = 3
• B = 9 + 5 = 14
• C = 10 + 2 = 12
• D = 12 + 0 = 12
Thus, total system resources = (3, 14, 12, 12).
vi) Need Matrix
Process   A   B   C   D
P0   0   0   0   0
P1   0   7   5   0
P2   1   0   0   2
P3   0   0   2   0
P4   0   6   4   2
vii) Safe State Check
Starting with Available = (1, 5, 2, 0):
• P0 runs → Work = (1, 5, 3, 2)
• P3 runs → Work = (1, 11, 6, 4)
• P2 runs → Work = (2, 14, 11, 8)
• P4 runs → Work = (2, 14, 12, 12)
• P1 runs → Work = (3, 14, 12, 12)
Safe sequence = <P0, P3, P2, P4, P1>. Therefore, the system is SAFE.
viii) Resource Request (0, 4, 2, 0) by P1
********** 8 **********
--- page 9 ---
• Request (0, 4, 2, 0) ≤ Need(P1) = (0, 7, 5, 0) ✔
• Request (0, 4, 2, 0) ≤ Available (1, 5, 2, 0) ✔
After tentative allocation: Available = (1, 1, 0, 0).
Safety test sequence:
• P0 → Work = (1, 1, 1, 2)
• P2 → Work = (2, 4, 6, 6)
• P3 → Work = (2, 10, 9, 8)
• P4 → Work = (2, 10, 10, 12)
• P1 → completes.
Safe sequence = <P0, P2, P3, P4, P1>. Hence, the request CAN be
granted immediately.
B Describe the concept and working of a Translation Lookaside Buffer (TLB) 10
in a paging system. Explain how address translation is carried out with and
without TLB.
Definition and Need of TLB (2 Marks)
address translation without TLB (4 Marks)
address translation with TLB (4 Marks)
• A Translation Lookaside Buffer (TLB) is a special high-speed cache
that stores recent translations of virtual page numbers (VPNs) to
physical frame numbers (PFNs).
•   In a paging system, every memory access requires a page table lookup
to translate the virtual address into a physical address.
• This lookup takes extra time (additional memory access), which slows
down the system.
• The TLB reduces this delay by caching frequently used page table
entries — providing fast access to address translations.
Address translation is carried out with TLB.
********** 9 **********

[Text in pictures on this page, read by OCR]
frame e

logical address physical address 0x000
frame f
cpu slp | a |
p — Oxfff
f frame g

physical memory

page table
--- page 10 ---
Address translation is carried without TLB.
4 A Provide a comparative analysis of the Monolithic and Layered architectures 10
of Operating Systems. Include appropriate diagrams to support your
explanation.
Monolithic Architecture (3 Marks)
Layered Architecture (3 Marks)
Comparative Analysis (4 Marks)
Operating System architecture defines the structure and organization of the
OS components and their interaction with each other and hardware.
Two commonly used architectures are Monolithic and Layered
architectures.
Monolithic Architecture (3 Marks)
Explanation:
•   In a monolithic system, the entire operating system is working in a
single kernel space.
•   All system components such as   file management, process
scheduling, memory management, and device drivers are integrated
into one large block of code that runs in supervisor mode.
•   It provides high performance because there are no inter-layer
overheads, but poor modularity and difficult debugging.
Diagram:
********** 10 **********

[Text in pictures on this page, read by OCR]
logical

address
CPU +> pid

page frame

number number

E TLB hit physical

BI address
Lt | 4d }—

TLB

TLB miss

a physical
memory

page table
--- page 11 ---
Advantages:
• High execution speed (no layer overhead).
•   Efficient direct access to hardware.
Disadvantages:
•   Difficult to maintain and debug.
• Poor security and modularity—failure in one module may crash the
entire system.
Examples:
MS-DOS, UNIX (early versions), Linux (partially monolithic).
Layered Architecture (3 Marks)
Explanation:
•   In layered architecture, the OS is divided into multiple layers, each
built upon the lower one.
• Each layer performs specific functions and interacts only with its
adjacent layers.
• The bottom layer deals with hardware, while the top layer provides
user interfaces.
Diagram:
********** 11 **********

[Text in pictures on this page, read by OCR]
applications

glibc standard c library

system-call interface
file CPU
systems scheduler
networks memory
(TCP/IP) manager
block character
devices devices

device drivers

hardware
--- page 12 ---
Advantages:
•   Better modularity and maintainability.
•   Easier to test and debug individual layers.
• Higher security and reliability due to restricted communication.
Disadvantages:
• Slower execution due to layer-to-layer communication overhead.
•   Difficult to design and define proper boundaries between layers.
Examples:
THE Operating System, Windows NT, OS/2.
Comparative Analysis (4 Marks)
Feature   Monolithic OS   Layered OS
Structure   Single large kernel Multiple   layers   with   clear
interfaces
Performance   High   (no Slightly slower (due to layering)
overhead)
Modularity   Poor   Excellent
Maintainability Difficult   Easier to maintain and modify
Security   Low   (shared High   (restricted   inter-layer
kernel)   access)
Examples   MS-DOS, UNIX   Windows NT, THE OS
Conclusion:
Monolithic architecture emphasizes performance, whereas layered
architecture   emphasizes   modularity,   reliability,   and   security.
Modern operating systems often adopt a hybrid approach, combining the
speed of monolithic design with the structure of layered models.
B A disk queue with requests on cylinders 85, 170, 45, 130, 25, 115, 72, 58 10
needs to be serviced. The disk head is initially at cylinder 60, and the disk
has cylinders numbered 0-199. Calculate the total head movement for:
1. FCFS
2. SSTF
3. SCAN (assuming initial direction towards cylinder 199)
4. C-SCAN (assuming initial direction towards cylinder 199)
Compare the performance of each algorithm and determine which suits best
for this scenario.
********** 12 **********

[Text in pictures on this page, read by OCR]
application file device user
program system driver mode

messages: messages

CPU
scheduling

memory
managment

kernel
mode

interprocess
communication

microkernel

hardware
--- page 13 ---
Each Algorithm 2 Marks
Comparison 2 Marks

RK KKK RK KK 13 2h KKK RK Kk KK
--- page 14 ---
Best Algorithm for This Scenario:
SSTF provides the best performance with only 180 cylinders of movement,
making it ideal for this scenario where minimizing seek time is the priority
and the request queue is relatively small, reducing starvation risk.
5 A Describe the concept of monitors in process synchronization with internal 10
structure and functioning. Explain how monitors manage process
coordination using condition variables and synchronization primitives.
Concept of Monitors (2 Marks)
Internal Structure of a Monitor (4 Marks)
Functioning and Coordination (4 Marks)
In concurrent programming, monitors are high-level synchronization
constructs that provide a convenient and safe mechanism for process
coordination.
They encapsulate shared data, the procedures that operate on that data, and
the synchronization between concurrent processes — all within a single
module.
Monitors eliminate many of the errors possible when using low-level
primitives such as semaphores.
A monitor is a software module with:
• Shared data variables.
• A set of procedures (only one process can execute inside the
monitor at a time).
• Condition variables for process synchronization.
It ensures mutual exclusion automatically — no two processes can execute
monitor procedures simultaneously.
********** 14 **********

[Text in pictures on this page, read by OCR]
Performance Comparison

Algorithm Total Movement Characteristics

FCFS 572 Simple, fair, but high seek time

SSTF 188 Minimal movement, risk of starvation
SCAN 313 Fair, predictable, moderate performance

C-SCAN 396 More uniform wait time, higher movement
--- page 15 ---
Internal Structure of a Monitor (4 Marks)
Components:
1. Shared Data: Variables accessible only through monitor procedures.
2. Procedures: Define operations that can be performed on shared data.
3. Initialization Code: Sets up initial values for data and conditions.
4. Condition Variables: Used for process synchronization (e.g., x, y).
Pseudocode syntax of a monitor:
monitor monitor-name
{
// shared variable declarations
function P1 (…) { …. }
function P2 (…) { …. }
function Pn (…) {……}
initialization code (…) { … }
}
Diagram of Monitor Structure (1 Mark)
+-----------------------------------+
Functioning and Coordination (4 Marks)
Condition Variables and Synchronization:
• Condition variables allow a process to wait for a certain condition
to become true.
• Two basic operations are used:
o wait(c) → Process is suspended until another process signals
condition c.
o signal(c) → Wakes up one waiting process on condition c.
• Mutual exclusion: Achieved automatically; only one process
executes within the monitor.
•   Synchronization: Managed through wait and signal on condition
variables.
• No busy waiting: Blocked processes are placed in a waiting queue
inside the monitor.
Advantages of Monitors
********** 15 **********
--- page 16 ---
• Provides structured and safer synchronization compared to
semaphores.
•   Eliminates errors like deadlocks and race conditions caused by
improper semaphore use.
• Promotes modularity and clarity in concurrent program design.
B Explain how fragmentation affects memory management in operating 10
systems and illustrate the different types of fragmentation with suitable
example. A system has five memory partitions of sizes 110 KB, 480 KB,
210   KB,   350   KB,   and   140   KB   respectively.
A sequence of processes arrives for allocation in the following order: P1 =
100 KB, P2 = 200 KB, P3 = 300 KB, P4 = 140 KB, and P5 = 50 KB.
Considering Contiguous memory allocation, show the final process-to-
partition allocations using First-Fit, Best-Fit, and Worst-Fit memory
allocation strategies.
Marks Distribution:
Fragmentation 2 Marks
Types 2 marks
First Fit – 2 marks
Best Fit – 2 marks
Worst Fit – 2 marks
Fragmentation is a memory management problem that occurs when free memory
space is broken into small, non-contiguous blocks over time. It reduces the
system’s ability to allocate large continuous memory blocks to new processes,
even if total free memory is sufficient.
Fragmentation affects memory utilization and system performance, leading to
inefficient use of available RAM.
Types of Fragmentation
(a) Internal Fragmentation
Definition: Occurs when a fixed-sized memory block allocated to a process is
larger than the process’s actual memory requirement.
Cause: Fixed partitioning or paging schemes with block sizes larger than needed.
Effect: Wasted space inside the allocated partition.
Example:
Suppose a system allocates 4 KB blocks, and a process needs only 3.6 KB.
→ Unused memory = 0.4 KB per process
This 0.4 KB inside the allocated block is internally fragmented.
External Fragmentation
Definition: Occurs when total free memory exists but is scattered in non-
contiguous blocks, preventing allocation of large processes.
Cause: Dynamic memory allocation where processes are loaded and removed
frequently.
Effect: Wasted space outside allocated partitions.
Example:
Assume memory = 100 MB total. Free blocks: 20 MB + 15 MB + 10 MB (non-
contiguous).
********** 16 **********
--- page 17 ---
A process requesting 40 MB cannot be allocated, though 45 MB is free in total.
6 A   I.   Apply your understanding of process scheduling to compare Long- 10
term and Short-term schedulers in terms of their purpose, execution
frequency, speed, alternate names, and where process selection
occurs (main or secondary memory).
II.   Apply the concepts of process scheduling to justify why time-
sharing systems rely more on Short-term scheduler, while batch-
processing systems depend more on Long-term scheduler.
I.   5 Marks (One mark for each criteria)
II.   5 Marks
Solution:
i. Following are the differences between a LTS and STS:- (5 marks)
********** 17 **********
--- page 18 ---
Aspect   Long-Term Scheduler   Short-Term Scheduler
Frequency   Runs less frequently.   Runs very frequently.
Speed   Slower, as it involves   Faster, as it focuses
more complex decision-   solely on CPU allocation.
making and memory
checks.
Process   Selects processes from the   Selects processes from
selection   job pool (secondary   the ready queue (main
location   memory).   memory).
Alternate   Job Scheduler   CPU Scheduler
Name
Purpose   Balances I/O-bound and   Maximizes CPU
CPU-bound processes.   utilization and minimizes
process waiting times.
ii. Time-sharing: Many interactive users → responsiveness is critical.
The short-term scheduler (CPU scheduler) decides which process
runs next very frequently (milliseconds). Long-term scheduler is
less relevant because new jobs are admitted immediately.
Batch system: Jobs are large and submitted in bulk. The long-term
scheduler regulates how many jobs enter memory, controlling
degree of multiprogramming. If too many are admitted, system
thrashes; if too few, CPU underutilizes.
(5 marks)
B A system has 3 frames for storing process pages in main memory. Assume
that all the page frames are initially empty. Consider the page reference
string given below:
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Compute the number of page faults and show frame contents step-by-step
for:
(a) FIFO,
(b) LRU,
(c) Optimal.
Also state which algorithm gave the fewest faults.
Marks Distribution:
(FIFO: 3 marks, LRU: 3 marks, Optimal: 3 marks)
Also state which algorithm gave the fewest faults and why.(1 marks)
********** 18 **********
--- page 19 ---
Reference string length = 12. Frames = 3.
(a) FIFO (First-In, First-Out)
Frames after
Step   Ref   Fault?
step (f1,f2,f3)
1   1   1, - , -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
4   4   4, 2, 3 (1 out) Y
5   1   4, 1, 3 (2 out) Y
6   2   4, 1, 2 (3 out) Y
7   5   5, 1, 2 (4 out) Y
8   1   5, 1, 2   N
9   2   5, 1, 2   N
10   3   5, 3, 2 (1 out) Y
11   4   5, 3, 4 (2 out) Y
12   5   5, 3, 4   N
Total page faults (FIFO): 9.
(b) LRU (Least Recently Used)
LRU replaces the page that has not been used for the longest time.
Step   Ref   Frames after step Fault? Comment
1   1   1, -, -   Y   load 1
2   2   1, 2, -   Y   load 2
3   3   1, 2, 3   Y   load 3
4, 2, 3 (1 was
4   4   Y
LRU)
4, 1, 3 (2 LRU
5   1   Y
replaced)
4, 1, 2 (3 LRU
6   2   Y
replaced)
********** 19 **********
--- page 20 ---
5, 1, 2 (4 LRU
7   5   Y
replaced)
8   1   5, 1, 2   N
9   2   5, 1, 2   N
3, 1, 2 (5 LRU
10   3   Y
replaced)
3, 4, 2 (1 LRU
11   4   Y
replaced)
3, 4, 5 (2 LRU
12   5   Y
replaced)
Total page faults (LRU): 10.
(c) Optimal (Belady’s optimal algorithm) — replace the page that will not
be used for the longest time in the future.
Frames after
Step   Ref   Fault?
step
1   1   1, -, -   Y
2   2   1, 2, -   Y
3   3   1, 2, 3   Y
1, 2, 4 (3
replaced; will be
4   4   used later   Y
sooner than 1 or
2?)*
5   1   1, 2, 4   N
6   2   1, 2, 4   N
1, 2, 5 (4
replaced: 4 next
used at step 11;
7   5   Y
1 and 2 are
needed earlier at
steps 8 and 9)
8   1   1, 2, 5   N
9   2   1, 2, 5   N
3, 2, 5 (1
replaced; 1 next
10   3   Y
used later than 2
or 5)
********** 20 **********
--- page 21 ---
3, 4, 5 (2
11   4   Y
replaced)
12   5   3, 4, 5   N
Total page faults (Optimal): 7.
Optimal gives the fewest faults (7) because it uses future knowledge. For
real systems we cannot implement Optimal, but it is used as a baseline. In
this case FIFO (9) beats LRU (10) — showing that LRU is usually good
but not always strictly better than FIFO, and that algorithms’ effectiveness
depends on the reference string.
7 A Analyze the Resource Allocation Graph
i)   Write resource allocated and requested table
ii)   Find if there is a deadlock or not? If there is no deadlock then
what will be the sequence of the process to get executed?
iii)   What will happen if one instance of resource R3 is removed
from the system.
I.   4 marks
II.   4 Marks
III.   2 Marks
i)
********** 21 **********
--- page 22 ---
II) System is in Safe State. Safe Sequence: P2, P0, P1, P3
III) There will be a deadlock in the system.
B Explain user level and kernel level threads. Which one are more light 5
weight and independent?
User and Kernel Thread 3 marks
Explanation 2 marks
Solution: User-level threads are managed entirely by a user-level thread
library without direct involvement from the operating system's kernel.
The kernel is unaware of their existence and treats the entire process
containing these threads as a single unit of execution.
(1.5 marks)
Kernel-level threads are managed directly by the operating system's
kernel. The kernel is aware of each individual kernel thread and handles
their creation, scheduling, and management.   (1.5 marks)
User-level threads are managed by a user-level thread library, making
them more lightweight as they don't require kernel intervention and offer
faster context switching, but are less independent as a blocking thread can
block the entire process. Kernel-level threads are managed by the
operating system, are more independent because they can take advantage
of multiple CPUs and are not tied to a single process's blocking state but
are more heavyweight due to the overhead of kernel mode transitions and
are slower to create and switch.
(2 marks)
C   Differentiate between sequential access and direct access methods for files. 5
Provide examples of applications where each access method would be
preferred.
Difference 4 marks
Example 1 marks
Sequential Access In sequential access, data in a file is processed in
order, one record or byte after the next. The operations typically used are
read next and write next. Repositioning within the file usually requires a
Reset (rewind) operation to go back to the beginning.
********** 22 **********
--- page 23 ---
Direct Access Direct access views a file as a numbered sequence of fixed-
length logical records. This method allows for immediate, random access
to any part of the file. Operations include explicitly reading or writing
record number (read n, write n), and moving the file pointer directly to
record (position to n).
Application Preference:
Sequential Access Preference This method is preferred for applications
where files must be processed entirely from beginning to end. Examples
include simple text files, log files (where records are appended
chronologically), and source code files read by a compiler.
Direct Access Preference Direct access is preferred for applications that
require quick, random retrieval and update of specific records. A prime
example is an Indexed/Relative File system, commonly used in databases
or any system (like a customer database or airline reservation system)
where a record must be accessed by its index or relative block number.
********** 23 **********
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper bf76353a16c3

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Operating Systems/ANS_Operating Systems(703CO1C002)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Dec 2024
- Text: text (8 pages)
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester I(Exam Year: 2024-2025)
Subject: Operating Systems
Date: 06 Dec 2024   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 8 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any four questions.
4. In all five question to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page
7. Figure in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q.1   a   [05]
Discuss the concept of Threads in brief with its advantages.
Ans:
 a smallest dispatchable unit of CPU utilization that forms the basis of
multithreaded computer systems
advantages:
 Takes less time to create a new thread than a process
 Less time to terminate a thread than a process
 Less time to switch between two threads within the same process
 Since threads within the same process share memory and files, they
can communicate with each other without invoking the kernel
b
What is Deadlock? Discuss the type of resources involved in the occurrence of   [05]
the deadlock.
Ans:
• Permanent blocking of a set of processes that either compete for
system resources or communicate with each other, no efficient
solution.
•   Involve conflicting needs for resources by two or more processes
Resources :
Reusable Resources
Consumable Resources
c   Discuss the requirements of Memory management as relocation and   [05]
protection.
********** 1 **********
--- page 2 ---
Ans:
Requirements: Relocation
 The programmer does not know where the program will be placed in
memory when it is executed,
◦   it may be swapped to disk and return to main memory at a
different location (relocated)
 Memory references must be translated to the actual physical memory
address
Protection:
 Processes should not be able to reference memory locations in another
process without permission
 Impossible to check absolute addresses at compile time
 Must be checked at run time
d   Explain the categories of I/O devises used by the OS to complete the users
task.
Ans:
a. Human readable
b. Machine readable
c. Communications
Q.2   a   Consider the following set of processes, with the length of the CPU-burst time
given in milliseconds and arrival time.   (10)
Process   Burst Time   Arrival time
P1   8   0
P2   4   2
P3   2   3
P4   1   3
P5   5   5
Draw Gantt charts and find the average waiting and turnaround time
illustrating the execution of these processes using preemptive SJF scheduling
algorithm
Ans:
Step-by-step implementation of the algorithm [3M]
Gantt chart: [3M]
Accurate Waiting time [2M]
Accurate turnaround time [2M]
b
What is race condition? Explain the working principle of monitors to achieve   (10)
mutual exclusion.
Ans:
 A race condition occurs when
◦   Multiple processes or threads read and write data items
◦   They do so in a way where the final result depends on the
order of execution of the processes.
◦ The output depends on who finishes the race last.
Monitors:
********** 2 **********
--- page 3 ---
 The monitor is a programming-language construct that provides
equivalent functionality to that of semaphores and that is easier to
control.
Q.3   a
Discuss in detail, various design objectives and services of operating systems.   (10)
Ans:
 Convenience
   Efficiency
   Ability to evolve
Services
 Program development
◦   Editors, compilers, linker, loader and debuggers
 Program execution
 Access to I/O devices
 Controlled access to files
 Access to other plug and play devices
   Security to users programs and applications
   Error detection and response
◦   internal and external hardware errors
 memory error
 device failure
◦   software errors
 arithmetic overflow
 access forbidden memory locations
 Accounting
◦   collect statistics
◦   monitor performance
********** 3 **********

[Text in pictures on this page, read by OCR]
'

queue of
entering
processes
monitor waiting area Entrance
{Ce
MONITOR

local data

ewait(el)

condition variables

5 Procedure 1

Procedure k

urgent queue

csignal ae
a initialization code

alo
Exit
--- page 4 ---
b   Explain deadlock detection algorithm with the help of suitable example.   (10)
Ans: algorithm [5M]
1. Let Work and Finish be vectors of length m and n, respectively Initialize:
(a) Work = Available
(b)   For i = 1,2, …, n, if Allocationi  0, then
Finish[i] = false;otherwise, Finish[i] = true
2.   Find an index i such that both:
(a)   Finish[i] == false
(a) Requesti  Work
If no such i exists, go to step 4
3.   Work = Work + Allocationi
Finish[i] = true
go to step 2
4.   If Finish[i] == false, for some i, 1  i  n, then the system is in deadlock
state. Moreover, if Finish[i] == false, then Pi is deadlocked
Example [5M]
Q.4 a   Explain the significance of page replacement algorithm. Calculate the page
faults occur for FIFO page replacement algorithms for the given reference   (10)
strings.
Number of available Frames : 3
Reference String : 5 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 5 0 1
Ans:
Significance [4M]
Finding page faults with accurate table – [6M]
b   What is producer / consumer problem? Provide the solution with the help of   (10)
semaphore.
Ans: Producer/Consumer Problem: [2M]
 General Situation:
********** 4 **********

[Text in pictures on this page, read by OCR]
mple of Detection Algorithm

& processes P, through P,; three resource types A
(7 instances), B (2 instances), and C (6 instances)

+ Snapshot at time Tp:
AllocationRequestAvailable

ABC ABC ABC
P, 010 000 000
P,; 200 202
P, 303 000
P3211 100
P,002 002

. uence <P, P2, P3, P;,P.>-wilHresult-in-Finishfi
P for all i
--- page 5 ---
◦ One or more producers are generating data and placing these in
a buffer
◦ A single consumer is taking items out of the buffer one at time
◦   Only one producer or consumer may access the buffer at any
one time
 The Problem:
◦   Ensure that the Producer can’t add data into full buffer and
consumer can’t remove data from empty buffer
Producer   Consumer
while (true) {   while (true) {
/* produce item v */   while (in <= out)
b[in] = v;   /*do nothing */;
in++;   w = b[out];
}   out++;
/* consume item w */
}
Solution: [8M]
Q.5 a   Explain Shortest Service Time First, SCAN and C-SCAN disk scheduling
algorithms with suitable example.   (10)
Ans: sequence: 55, 58, 39, 18, 90, 160, 150, 38, 184.
********** 5 **********

[Text in pictures on this page, read by OCR]
/* program producerconsumer */
ant n;

binary_semaphore s = 1, delay = 0
void producer( )
{
while (true) {
produce();
semWaitB(s);
append( );
n++;7
af (m==1) semSignalB(delay);
semSignalB(s);
+
}
void consumer()
{
aint m; /* a local variable */
semWaitB(delay);
while (true) {
semWaitB(s);
semSignalB(s);
consume ();
af (m==0) semWaitB(delay);
+

void main()

n= 0;
parbegin (producer, consumer) ;
--- page 6 ---
b   Explain various elements of directory and its tree structure.   (10)
Ans: basic elements [6M]
Basic information
Address information
Access Control Information
Usage Information
Tree structure
Q.6 a   What do you mean by segmentation in memory management? Explain
translation of logical address in to physical address in segmentation.   (10)
Ans: segmentation [3M]
 A program can be subdivided into segments
◦ Segments may vary in length
◦   There is a maximum segment length
 Addressing consist of two parts
◦   a segment number and
◦ an offset
 Segmentation is similar to dynamic partitioning
Address Translation: explanation with diagram [7M]
********** 6 **********

[Text in pictures on this page, read by OCR]
Master Directory

Subirectory Subirectory Subirectory
Subirectory Subirectory File
File File File

Figure 12.4 Tree-Structured Directory
--- page 7 ---
b   Explain Dining – Philosopher problem with an example.   (10)
Ans:: explanation [5M]
Dining Philosophers Problem States that there are 5 Philosophers who are
engaged in two activities Thinking and Eating. Meals are taken communally in a
table with five plates and five forks in a cyclic manner as shown in the figure.
Constraints and Condition for the problem :
1. Every Philosopher needs two forks in order to eat.
2. Every Philosopher may pick up the forks on the left or right but only one fork
at once.
3. Philosophers only eat when they had two forks. We have to design such a
protocol i.e. pre and post protocol which ensures that a philosopher only eats
if he or she had two forks.
4. Each fork is either clean or dirty.
Solution[5M]
Correctness properties it needs to satisfy are :
1. Mutual Exclusion Principle –
No two Philosophers can have the two forks simultaneously.
2. Free from Deadlock –
Each philosopher can get the chance to eat in a certain finite time.
3. Free from Starvation –When few Philosophers are waiting then one gets a
chance to eat in a while.
4. No strict Alternation.
5. Proper utilization of time.
Q.7   Write short note on the following
a   Round Robin Scheduling algorithm   (10)
Ans:
********** 7 **********

[Text in pictures on this page, read by OCR]
16-bit logical address

4-bit segment # 12-bit offset

[o[olo[1]oJo[1[o[1[1 [1 [2 [o[ololo}
SY

Length Base |
0 [001011101110[000001000000000:
1 [011110011110/0010000000100000}————_>

Process segment table


16-bit physical address
(b) Segmentation

Figure 7.12 Examples of Logical-to-Physical Address Translation
--- page 8 ---
b   Mutual Exclusion with message passing   (10)
Ans:
 The actual function of message passing is normally provided in the form
of a pair of primitives:
send (destination, message)
receive (source, message)
Synchronization
Blocking send, Blocking receive
Non-blocking Send
Addressing
Direct Addressing
Indirect addressing
********** 8 **********

[Text in pictures on this page, read by OCR]
4, Round Robin (RR)

» Each process gets a small unit of CPU time (time
quantum), usually 10-100 milliseconds. After this
time has elapsed, the process is preempted and
added to the end of the ready queue.

« If there are n processes in the ready queue and
the time quantum is q, then each process gets
I/n of the CPU time in chunks of at most g time
units at once. No process waits more than (n-
I)q time units.

« Performance

q large => FIFO

q small => q must be large with respect to context
switch, otherwise overhead is too high

Example of RR with Time Quantum = 4
Process Burst Time

P, 24
P, 3
P; 3

* The Gantt chart is:

[i feelejejr|r le |e
0 4 7 10 14 18 22 26 3

* Typically, higher average turnaround than SJF,
but better response

/* program mutualexclusion */
const int n = /* number of processes */;
void P(int i)
{
message msg;
while (true) {
receive (box, msg);
/* critical section ap
send (box, msg);
/* remainder */;

}
void main()
{

create mailbox (box);

send (box, null);

parbegin (P(1), P(2), . . «, P(M)):
}

Figure 5.20 Mutual Exclusion Using Messages
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper aa115ff0b5e2

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Operating Systems/ANS_Operating Systems(703CO1C002)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 25 Feb 2025
- Text: mixed (8 pages), mean OCR confidence 75.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 1 Re-exam(Exam Year: 2024-2025)
Subject: Operating Systems
Date: 25 Feb 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 8 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any four questions.
4. In all five question to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page
7. Figure in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q.1   a.
What do you mean by the context of a process? Explain in brief.   [05]
Ans:
It is basically the state of a processor during the execution of current
instruction
content of CPU registers
Program counter
PSW etc.
b.
How to you recover from the deadlock situation? Explain in brief.   [05]
Ans: Process Termination
•   Abort all deadlocked processes
•   Abort one process at a time until the deadlock cycle is eliminated
•   order should we choose to abort
–   Priority of the process
– How long process has computed, and how much longer to
completion
– Resources the process has used
– Resources process needs to complete
– How many processes will need to be terminated
–   Is process interactive or batch?
Resource Preemption
•   Selecting a victim – minimize cost
•   Rollback – return to some safe state, restart process for that state
********** 1 **********
--- page 2 ---
c.   Discuss the requirements of Memory management as logical and physical   [05]
organization of the space.
Ans: Logical Organization
 Memory is organized linearly (usually)
 Programs are written in modules
◦ Modules can be written and compiled independently
   Different degrees of protection given to modules (read-only, execute-
only)
 Share modules among processes
 Segmentation helps here
Physical organization
 Cannot leave the programmer with the responsibility to manage
memory
 Memory available for a program plus its data may be insufficient
◦   Overlaying (Overlapping) allows various modules to be
assigned the same region of memory but is time consuming to
program
 Programmer does not know how much space will be available
d.   Explain the area of differences for the I/O devices.   [05]
Ans:
A. Data Rate
B. Application
C. Complexity of Control
D. Unit of Transfer
E. Data Representation
F. Error Conditions
Q.2 a
Solve the following problem for preemptive Priority scheduling. Calculate   [10]
average waiting time and average turnaround time. Also draw the Gantt
chart.
Consider low number as higher priority
Processes   Arrival time   Burst time   Priority
P1   0   8   2
P2   4   8   0
P3   7   10   1
Ans:
Step-by-step implementation of the algorithm [3M]
Gantt chart: [3M]
Accurate Waiting time [2M]
Accurate turnaround time [2M]
b
********** 2 **********
--- page 3 ---
What is semaphore? Discussed how it is useful to achieve mutual exclusion
with an example.
Ans:
 Semaphore:
◦ An integer value used for signalling among processes.
 Only three operations may be performed on a semaphore, all of which
are atomic:
◦   initialize,
◦ Decrement (semWait)
◦   increment (semSignal)
Implemented with an example. [8M]
Q.3 a
Differentiate between Layered and Monolithic structure of Operating Systems   [10]
with suitable diagram.
Ans:
Layered Architecture
********** 3 **********

[Text in pictures on this page, read by OCR]
Critical
region

| Normal

execution

Queue for Value of
“TT [0] 1 Blocked on

semaphore lock semaphore lock A B Cc |
! semaphore

1 lock

Note that normal
execution can
proceed in parallel
but that critical
regions are serialized.

Figure 5.7 Processes Accessing Shared Data Protected by a Semaphore

Monolithic Kernel System
Unprivileged
Mode

Privileged

File Network Mode
Systems Subsystem

Memory Process Drivers
Management Management

Monolithic Kernel
--- page 4 ---
Layer 6
User Programs
roo Layer 5

Layer 4 W/o Buffer

Process Management Layers
Layer 2 Memory Management
CPU Scheduling

Layer
Hardware

FIC 7) IC HOH
--- page 5 ---
b Consider following data for deadlock avoidance algorithm (Banker’s) and determine whether   (10
the state is safe or not. Give the safe sequence if it is safe.   )
R1   R2   R3   R1   R2   R3
P1   3   2   2   P1 1   0   0
P2   6   1   3   P2   6   1   2   R1   R2   R3
P3   3   1   4   P3   2   1   1   9   3   6
P4   4   2   2   P4   0   0   2
Claim Matrix (C)   Allocation Matrix (A)   Resource Vector (R)
Ans:
Solving step-by-step for safe state – [8M]
Depicting safe sequence – [2M]
Q.   a Explain the significance of page replacement algorithm. Calculate the page faults occur for
4   LRU page replacement algorithms for the given reference strings.   [10
Number of available Frames : 3   ]
Reference String : 5 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 5 0 1
Ans:
Significance [4M]
Finding page faults with accurate table – [6M]
b What is Inter-process Communication? Explain Reader’s / Writer’s problem with suitable   (10
example   )
Ans: IPC [2M]
Reader’s / Writer’s problem [8M]
 A data area is shared among many processes
◦ Some processes only read the data area, some only write to the area
 Conditions to satisfy:
◦   Multiple readers may read the file at once.
◦   Only one writer at a time may write
◦   If a writer is writing to the file, no reader may read it.
********** 5 **********

[Text in pictures on this page, read by OCR]
Pl
P2
P3
P4

Rl R2 R3 Rl R2 R3
0 t) 0 Pl tt) 0 0 Pl
0 0 0 P2 tt) 0 0 P2
0 t) 0 P3 0 0 0 P3
4 2 2 P4 0 0 2 P4

Claim matrix C Allocation matrix A
Rl R2 R3 Rl R2 R3

Po [ 3 [ 6 | Lo | 3 T 4 |

Resource vector R Available vector V

(d) P3 runs to completion

Rl R2 Rj
0 0 0
0 0 0
0 0 0
4 2 0
C-A
--- page 6 ---
Q.   a
5   Discuss I/O buffering and its types with the limitations.   (10
)
Ans:
Stream-Oriented single Buffering
Block oriented single buffering
Double Buffer
Circular Buffer
Limitation : enough demand eventually all buffers become full and their advantage is lost
b Explain any four methods of file organization used by an operating system.   (10
)
Ans:
◦   Pile
◦   Sequential file
◦   Indexed sequential file
◦   Indexed file
Q.   a What do you mean by paging in memory management? Explain translation of logical address
6   in to physical address in paging.   (10
)
Ans: paging - [3M]
********** 6 **********

[Text in pictures on this page, read by OCR]
/* program readersandwriters */
int readcount;
semaphore x = 1, wsem = 1;
void reader()
{
while (true) {
semWait (x);
readcount++;
if (readcount == 1) semWait (wsem);
semSignal (x);
READUNIT( ) ;
semWait (x);
readcount--;

if (readcount == 0) semSignal (wsem);
semSignal (x);
}
}
void writer()
{
while (true) {
semWait (wsem);
WRITEUNIT( );
semSignal (wsem);
}
}

void main()

{

readcount = 0;
parbegin (reader, writer);
--- page 7 ---
   Partition memory into small equal fixed-size chunks and divide each process into the
same size chunks
 The chunks of a process are called pages
 The chunks of memory are called frames
Address Translation: explanation with diagram [7M]
b Explain Dining – Philosopher problem with an example.   (10
)
Ans:: explanation [5M]
Dining Philosophers Problem States that there are 5 Philosophers who are engaged in two
activities Thinking and Eating. Meals are taken communally in a table with five plates and five
forks in a cyclic manner as shown in the figure.
Constraints and Condition for the problem :
1. Every Philosopher needs two forks in order to eat.
2. Every Philosopher may pick up the forks on the left or right but only one fork at once.
3. Philosophers only eat when they had two forks. We have to design such a protocol i.e. pre
and post protocol which ensures that a philosopher only eats if he or she had two forks.
4. Each fork is either clean or dirty.
Solution[5M]
Correctness properties it needs to satisfy are :
1. Mutual Exclusion Principle –
No two Philosophers can have the two forks simultaneously.
2. Free from Deadlock –
Each philosopher can get the chance to eat in a certain finite time.
3. Free from Starvation –When few Philosophers are waiting then one gets a chance to eat in a
while.
4. No strict Alternation.
5. Proper utilization of time.
Q.   Write short note on the following   (20
7   a. Process Control Block   )
Ans: Explanation on at least 5 attributes in detail [2M for each]
Process identification
Processor State Information
User-Visible Registers
Control and Status Register
Stack Pointers
Process Control Information
********** 7 **********

[Text in pictures on this page, read by OCR]
16-bit logical address
6-bit page # 10-bit offset
lojofofololajoj1{1[1Jo}1{1]1[1Jo]
nn A et
l

0[000101
1[000110
2[011001

Process
page table

FT @ [V+
[ofofo[1]1jojo[1[1]1Joj1]1]1]1]o}

16-bit physical address
(a) Paging
--- page 8 ---
b. Mutual exclusion with the hardware support
Ans:
Disabling Interrupts [3M]
Test and Set instruction [4M]
Swap instruction[3M]
********** 8 **********
````
