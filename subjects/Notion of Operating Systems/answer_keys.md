# Notion of Operating Systems: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 28e0b389209c

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/72631__Semester I.zip :: Final-Exam/Bachelor of Science (Information Technology) - 45618/Notion Of Operating Systems/ANS_Final-Exam_Notion Of Operating Systems(NHNOS103)_Semester I_2025-2026.pdf`
- Printed on paper: max marks: 60; exam date: 11 Oct 2025
- Text: text (12 pages)

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: Bachelor of Science (Information Technology)
Year: I/Semester I (Exam Year: 2025-2026)
Subject: Notion of Operating Systems/Notion Of Operating
Systems
Time: 11:30 am - 01:30 pm (02:00
Date: 11 Oct 2025
Hrs.)
Max Marks: 60
FINAL EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 12 pages
2. All questions are compulsory.
3. All questions carry equal marks
4. Answer to each new question to be started on a fresh page.
5. Figures on the right-hand side indicate full marks.
6. Draw neat labelled diagram wherever necessary
7. Use of Calculator is not allowed
1.   Answer the following questions:(Attempt Any 4 Questions)   20
a.   5
When a process blocks, it does so because logically it cannot continue, typically because it is
waiting for input that is not yet available. It is also possible for a process that is conceptually
ready and able to run to be stopped because the operating system has decided to allocate the
CPU to another process for a while.
Page 1 of 12
--- page 2 ---
These two conditions are completely different. In the first case, the suspension is inherent in
the problem (you cannot process the user’s command line until it has been typed). In the
second case, it is a technicality of the system (not enough CPUs to give each process its own
private processor).
In Fig. we see a state diagram showing the three states a process may be in:
1. Running (actually using the CPU at that instant).
2. Ready (runnable; temporarily stopped to let another process run).
3. Blocked (unable to run until some external event happens).
Logically, the first two states are similar. In both cases the process is willing to run, only in the
second one, there is temporarily no CPU available for it. The third state is fundamentally
different from the first two in that the process cannot run, even if the CPU is idle and has
nothing else to do.
b. Every PC contains a motherboard, which contains the CPU, slots for memory chips, and   5
sockets for PCIe (or other) plug-in cards. On the motherboard a small amount of flash holds a
program called the system firmware, which we commonly still refer to as the BIOS (Basic
Input Output System).
Booting using the original BIOS was slow, architecture-dependent, and limited to smaller
SSDs and disks (up to 2 TB). After we press the power button, the motherboard waits for the
signal that the power supply has stabilized. When the CPU starts executing, it fetches code
from a hard-coded physical address (known as the reset vector) that is mapped to the flash
memory. Next, it is time to move to the next stage of the booting process.
In systems using the old-style BIOS, this was all very straightforward. The BIOS would
determine the boot device by trying a list of devices stored in the CMOS memory. The user can
change this list by entering a BIOS configuration program just after booting. The first sector
from the boot device is read into memory and executed. This sector, known as the MBR
(Master Boot Record), contains a program that normally examines the partition table at the end
of the boot sector to determine which partition is active.
A partition is a distinct region on the storage device that may for instance contain its own file
systems. Then a secondary boot loader is read in from that partition. This loader reads in the
operating system from the active partition and starts it. The operating system then queries the
BIOS to get the configuration information. For each device, it checks to see if it has the device
driver. If not, it asks the user to install it, for instance by downloading it from the Internet.
Page 2 of 12
--- page 3 ---
Once it has all the device drivers, the operating system loads them into the kernel. Then it
initializes its tables, creates whatever background processes are needed, and starts up a login
program or GUI.
c.   5
Mutual exclusion, is a way of making sure that if one process is using a shared variable or file,
the other processes will be excluded from doing the same thing. That part of the program
where the shared memory is accessed is called the critical region or critical section. If we could
arrange matters such that no two processes were ever in their critical regions at the same time,
we could avoid races.
In an abstract sense, the behavior that we want is shown in Fig. Here process A enters its
critical region at time T1. A little later, at time T2 process B attempts to enter its critical region
but fails because another process is already in its critical region and we allow only one at a
time. Consequently, B is temporarily suspended until time T3 when A leaves its critical region,
allowing B to enter immediately. Eventually B leaves (at T4) and we are back to the original
situation with no processes in their critical regions.
d. Personal Computer Operating Systems   5
Modern computers support multiprogramming, often with dozens of programs started up at
boot time, and multiprocessor architectures. Their job is to provide good support to a single
user. They are widely used for word processing, spreadsheets, games, and Internet access.
Common examples are Windows 11, macOS, Linux, and FreeBSD.
Smartphone and Handheld Computer Operating Systems
Page 3 of 12
--- page 4 ---
Continuing on down to smaller and smaller systems, we come to tablets smartphones and other
handheld computers. A handheld computer,originally known as a PDA (Personal Digital
Assistant), is a small computer that can be held in your hand during operation. Smartphones
and tablets are the best known examples.
This market is currently dominated by Google’s Android and Apple’s iOS. Most of these
devices boast multicore CPUs, GPS, cameras and other sensors, copious amounts of memory,
and sophisticated operating systems. Moreover, all of them have more third-party applications
(apps) than you can shake a (USB) stick at. Google has over 3 million Android apps in the Play
Store and Apple has over 2 million in the App Store.
5
Process   Arrival   Burst Completion   Turn around   Waiting
e. id   Time   Time   time   time   Time
P1   3   6   17   14   8
P2   1   1   4   3   2
P3   0   3   3   3   0
P4   2   7   11   9   2
Gantt Chart
0   3   4   11   17
P3   P2   P4   P1
Average Turn
around time   7.25
Average waiting
time   3
5
Process   Arrival   Burst Completion   Turn around   Waiting
f. id   Time   Time   time   time   Time
P5   1   4   11   10   6
P6   0   4   8   8   4
P7   2   2   6   4   2
Page 4 of 12
--- page 5 ---
P8   3   1   9   6   5
Gantt Chart
0   2   4   6   8   9   11
P6   P5   P7   P6   P8   P5
Average Turn
around time   7
Average waiting
time   4.25
2.   Answer the following questions:(Attempt Any 4 Questions)   20
a. Many operating systems support two-part file names, with the two parts separated by a period,   5
as in prog.c. The part following the period is called the file extension and usually indicates
something about the file. In MS-DOS, for example, file names were 1–8 characters, plus an
optional extension of 1–3 characters.
Any 6 file extensions
b.   5
Page 5 of 12
--- page 6 ---
The Ostrich Algorithm is a strategy used in operating systems to deliberately ignore potential
deadlocks or other rare issues, assuming that they occur infrequently and are not worth the cost
of prevention or detection.
The term is metaphorical—just like an ostrich is (mythically) believed to bury its head in the
sand to avoid danger, the system chooses to "ignore" certain problems rather than handling
them proactively.
Why Use the Ostrich Algorithm?
•   Deadlock prevention and detection mechanisms often require significant overhead in
terms of CPU time, memory, or complexity.
•   If deadlocks are rare in a particular system, it may be more efficient to let them happen
occasionally and handle them manually or via reboot.
Assumptions Behind the Algorithm:
•   Deadlocks are very rare.
•   System restarts or administrator intervention can resolve issues when they arise.
•   Cost of prevention > Cost of occasional failure.
c. On any computer, programs reference a set of memory addresses. When a program executes an   5
instruction like MOV REG,1000
it does so to copy the contents of memory address 1000 to REG (assuming the first operand
represents the destination and the second the source). Addresses can be generated using
indexing, base registers, and various other ways.
These program-generated addresses are called virtual addresses and form the virtual address
space. On computers without virtual memory, the virtual address is put directly onto the
memory bus and causes the physical memory word with the same address to be read or written.
When virtual memory is used, the virtual addresses do not go directly to the memory bus.
Instead, they go to an MMU (Memory Management Unit) that maps the virtual addresses
onto the physical memory addresses, as illustrated in Fig.
Page 6 of 12
--- page 7 ---
d. Deadlock Recovery-Detection and recovery. Let them occur, detect them, and take action.   5
Various ways of recovering from deadlock.
Recovery through Preemption In some cases, it may be possible to temporarily take a
resource away from its current owner and give it to another process. In many cases, manual
intervention may be required, especially in batch-processing operating systems running on
mainframes. For example, to take a laser printer away from its owner, the operator can collect
all the sheets already printed and put them in a pile. Then the process can be suspended
(marked as not runnable). At this point, the printer can be assigned to another process. When
that process finishes, the pile of printed sheets can be put back in the printer’s output tray and
the original process restarted.
Recovery through Rollback
If the system designers and machine operators know that deadlocks are likely, they can
arrange to have processes checkpointed periodically. Checkpointing a process means that its
state is written to a file so that it can be restarted later. The checkpoint contains not only the
memory image, but also the resource state, in other words, which resources are currently
assigned to the process. To be most effective, new checkpoints should not overwrite old ones
but should be written to new files, so as the process executes, a whole sequence accumulates.
When a deadlock is detected, it is easy to see which resources are needed. To do the recovery, a
process that owns a needed resource is rolled back to a point in time before it acquired that
resource by starting at one of its earlier checkpoints. All the work done since the checkpoint is
lost (e.g., output printed since the checkpoint must be discarded, since it will be printed again).
Recovery through Killing Processes
Page 7 of 12
--- page 8 ---
The crudest but simplest way to break a deadlock is to kill one or more processes. One
possibility is to kill a process in the cycle. With a little luck, the other processes will be able to
continue. If this does not help, it can be repeated until the cycle is broken.
Alternatively, a process not in the cycle can be chosen as the victim in order to release its
resources. In this approach, the process to be killed is carefully chosen because it is holding
resources that some process in the cycle needs. For example, one process might hold a printer
and want a plotter, with another process holding a plotter and wanting a printer. These two are
then deadlocked. A third process may hold another identical printer and another identical
plotter and be happily running. Killing the third process will release these resources and break
the deadlock involving the first two.
Where possible, it is best to kill a process that can be rerun from the beginning with no ill
effects. For example, a compilation can always be rerun because all it does is read a source file
and produce an object file. If it is killed partway through, the first run has no influence on the
second run.
On the other hand, a process that updates a database cannot always be run a second time safely.
If the process adds 1 to some field of a table in the database, running it once, killing it, and then
running it again will add 2 to the field, which is incorrect.
e. i.   0   5
ii.   26000
iii.   34875
0 falls in 0K to 4K. This is mapped to 28K to 32K. Hence physical address is 28672
26000 falls in 24K to 28K.
26000-24576 = 1424
This is mapped to 16K to 20K
Hence physical address is 16384+1424=17808
34875 falls in 32K to 36K.
34875-32768=2107
This is mapped to 20K to 24K
Hence physical address is 20480+2107=22587
f.   5
Page 8 of 12
--- page 9 ---
i) RAG edges
Assignment (held):
Printer→P1, Scanner→P2, TapeDrive→P3, Camera→P4, Microphone→P5
Request (waiting):
P1→Scanner, P2→TapeDrive, P3→Camera, P4→Microphone, P5→Printer, P6→TapeDrive
ii) Deadlock? Yes—there is a cycle.
iii) Deadlock cycle (processes & resources):
P1→Scanner→P2→TapeDrive→P3→Camera→P4→Microphone→P5→Printer→P1
Involved: P1, P2, P3, P4, P5 and Printer, Scanner, TapeDrive, Camera, Microphone.
P6 is waiting for TapeDrive (held within the cycle) → blocked but not in the cycle.
3.   Answer the following questions:(Attempt Any 4 Questions)   20
a. A hard link is an extra name for an existing file that points to the same inode.   5
All hard links, including the original name, are equal—there is no concept of an “original” file.
The file’s data blocks remain until the last hard link is removed.
Example:
Suppose you have a file fun in the playground directory:
cd playground
ln fun fun-hard
This creates fun-hard as a hard link to fun.
Now:
ls -li
Sample output:
12353538 -rw-r--r-- 2 me me 1650 Mar 10 12:33 fun
12353538 -rw-r--r-- 2 me me 1650 Mar 10 12:33 fun-hard
Same inode number (12353538) confirms both names reference the same data.
The link count 2 shows there are now two directory entries (the original fun and fun-hard)
pointing to that inode.
Page 9 of 12
--- page 10 ---
If you delete fun, fun-hard still provides full access to the data.
b. i) pwd – Print Working Directory   5
Displays the full absolute path of the current working directory.
Example:
pwd
Output:
/home/student/projects
ii) wc – Word/Line/Character Count
Counts the number of lines, words, and characters in a file.
Example:
wc notes.txt
Output:
10 45 320 notes.txt
(10 lines, 45 words, 320 characters)
Options:
wc -l → lines only
wc -w → words only
wc -c → bytes/characters
iii) kill – Terminate a Process
Sends a signal to a process to stop it.
Example:
kill 1234
Terminates the process with PID 1234.
c.   5
Page 10 of 12
--- page 11 ---
d. To change the mode (permissions) of a file or directory, the chmod command is used. Only the   5
file’s owner or the superuser can change the mode of a file or directory. chmod supports two
distinct ways of specifying mode changes: octal number representation, or symbolic
representation.
[me@linuxbox ~]$ > foo.txt
[me@linuxbox ~]$ ls -l foo.txt
-rw-rw-r-- 1 me me 0 2016-03-06 14:52 foo.txt
[me@linuxbox ~]$ chmod 600 foo.txt
[me@linuxbox ~]$ ls -l foo.txt
-rw------- 1 me me 0 2016-03-06 14:52 foo.txt
e.   i.   cat ls-output.txt   5
ii.   cat movie.mpeg.001 movie.mpeg.002 > movie.mpeg
iii.   cat
Type any text and press Ctrl+D to end.
Everything typed is echoed back
Page 11 of 12
--- page 12 ---
iv.   cat > lazy_dog.txt
The quick brown fox jumped over the lazy dog.
[Ctrl+D]
v.   cat < lazy_dog.txt
Reads the file through standard input and prints it.
f. cd office   5
i-create staff.txt with one line, Ctrl+D to finish
cat > staff.txt
ii-ls
iii-mkdir records
iv-cp staff.txt records/
v-ls records
Page 12 of 12
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper aea5e787b214

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/72631__Semester I.zip :: Re-Exam/Bachelor of Science (Information Technology) - 45618/Notion Of Operating Systems/ANS_Re-Exam_Notion Of Operating Systems(NHNOS103)_Semester I_2025-2026.pdf`
- Printed on paper: max marks: 60; exam date: 20 Jan 2026
- Text: text (11 pages)

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: B.Sc. (IT)
Year: I/Semester I (Exam Year: 2025-2026)
Subject: Notion of Operating Systems/Notion Of Operating
Systems
Time: 11:00 am - 01:00 pm (02:00
Date: 20 Jan 2026
Hrs.)
Max Marks: 60
RE EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 11 pages
2. All questions are compulsory.
3. All questions carry equal marks
4. Answer to each new question to be started on a fresh page.
5. Figures on the right-hand side indicate full marks.
6. Draw neat labelled diagram wherever necessary
7. Use of Calculator is not allowed
1.   Answer the following questions:(Attempt Any 4 Questions)   20
a. Word processors usually display the document being created on the screen formatted exactly as   5
it will appear on the printed page. Suppose that the user is writing a book. Now consider what
happens when the user suddenly deletes one sentence from page 1 of an 800-page book.
After checking the changed page for correctness, she now wants to make another change on
page 600 and types in a command telling the word processor to go to that page (possibly by
searching for a phrase occurring
only there). The word processor is now forced to reformat the entire book up to page 600 on
the spot because it does not know what the first line of page 600 will be until it has processed
all the previous pages
Page 1 of 11
--- page 2 ---
Suppose that the word processor is written as a two threaded program. One thread interacts
with the user and the other handles reformatting in the background. As soon as the sentence is
deleted from page 1, the interactive thread tells the reformatting thread to reformat the whole
book.
Meanwhile, the interactive thread continues to listen to the keyboard and mouse and responds
to simple commands like scrolling page 1 while the other thread is computing madly in the
background. With a little luck, the reformatting will be completed before the user asks to see
page 600, so it can be displayed instantly
Lets add 1 more thread. Many word processors have a feature of automatically saving the
entire file to disk every few minutes to protect
the user against losing a day’s work in the event of a program crash, system crash, or power
failure. The third thread can handle the disk backups without interfering with the other two.
b. RAM   5
Main memory is usually called RAM (Random Access Memory).It is volatile in nature and its
looses its contents when the power is switched off
ROM
ROM (Read Only Memory) is programmed at the factory and cannot be changed afterward. It
is fast and inexpensive. On some computers, the bootstrap loader used to start the computer is
contained in ROM. Unlike RAM, nonvolatile memory does not lose its contents when the
power is switched off
EEPROM
Page 2 of 11
--- page 3 ---
EEPROM (Electrically Erasable PROM) is also nonvolatile, but in contrast to ROM can be
erased and rewritten. However, writing it takes orders of magnitude more time than writing
RAM, so it is used in the same way ROM is, except that it is now possible to correct bugs in
programs by rewriting them in the field.
Flash Memory
Flash memory is also commonly used as the storage medium in portable electronic devices
such as smartphones and in SSDs to serve as a faster alternative to hard disks. Flash memory is
intermediate in speed between RAM and disk. Boot strapping code may also be stored in Flash
memory, which is similarly nonvolatile, but in contrast to ROM can be erased and rewritten
c. Nearly all processes alternate bursts of computing with (disk or network) I/O Requests. I/O in   5
this sense is when a process enters the blocked state waiting for an external device to complete
its work. some processes, such as the one in Fig. (a), spend most of their time computing, while
other processes, such as the one shown in Fig. (b), spend most of their time waiting for I/O.
The former are called compute-bound or CPU-bound; the latter are called I/O bound.
Compute-bound processes typically have long CPU bursts and thus infrequent I/O waits,
whereas I/O-bound processes have short CPU bursts and thus frequent I/O waits.
Note that the key factor is the length of the CPU burst, not the length of the I/O burst. I/O-
bound processes are I/O bound because they do not compute much between I/O requests, not
because they have especially long I/O requests. It takes the same time to issue the hardware
request to read a disk block no matter how much or how little time it takes to process the data
after they arrive
d. Real-time systems are characterized by having time as a key parameter. For example, in   5
industrial process-control systems, real-time computers have to collect data about the
production process and use it to control machines in the factory. Often there are hard deadlines
that must be met. For example, if a car is moving down an assembly line, certain actions must
take place at certain instants of time.
Page 3 of 11
--- page 4 ---
If the action absolutely must occur at a certain moment (or within a certain range), we have a
hard real-time system. Many of these are found in industrial process control, avionics, military,
and similar application areas. These systems must provide absolute guarantees that a certain
action will occur by a certain time.
A soft real-time system is one where missing an occasional deadline, while not desirable, is
acceptable and does not cause any permanent damage. Digital audio or multimedia systems fall
in this category. Smartphones are also soft realtime systems.
Since meeting deadlines is crucial in (hard) real-time systems, sometimes the operating system
is simply a library linked in with the application programs, with everything tightly coupled and
no protection between parts of the system. An example of this type of real-time system is eCos.
5
Process   Arrival   Burst Completion   Turn around   Waiting
e. id   Time   Time   time   time   Time
P1   2   5   19   17   12
P2   0   8   8   8   0
P3   3   2   10   7   5
P4   1   4   14   13   9
Gantt Chart
0   8   10   14   19
P2   P3   P4   P1
Average Turn
around time   11.25
Average waiting
time   6.5
5
Process   Arrival   Burst Completion   Turn around   Waiting
f. id   Time   Time   time   time   Time
P5   3   2   10   7   5
P6   0   4   8   8   4
Page 4 of 11
--- page 5 ---
P7   2   2   6   4   2
P8   1   3   11   10   7
Gantt Chart
0   2   4   6   8   10   11
P6   P8   P7   P6   P5   P8
Average Turn
around time   7.25
Average waiting
time   4.5
2.   Answer the following questions:(Attempt Any 4 Questions)   20
a. Files can be structured in any of several ways. Three common possibilities are depicted in Fig.   5
The file in Fig. (a) is an unstructured sequence of bytes.In effect, the operating system does not
know or care what is in the file. All it sees are bytes
In fig b, a file is a sequence of fixed-length records, each with some internal structure. Central
to the idea of a file being a sequence of records is the idea that the read operation returns one
record and the write operation overwrites or appends one record.
Page 5 of 11
--- page 6 ---
The third kind of file structure is shown in Fig. (c). In this organization, a file consists of a tree
of records, not necessarily all the same length, each containing a key field in a fixed position in
the record. The tree is sorted on the key field, to allow rapid searching for a particular key. The
basic operation here is not to get the ‘‘next’’ record, although that is also possible, but to get the
record with a specific key
b. ·   Use an array state to track if each philosopher is thinking, hungry, or eating.   5
·   A philosopher can eat only if neither neighbor is eating.
·   For philosopher i, neighbors are LEFT (i-1) and RIGHT (i+1).
Advantages:
·   Deadlock-free.
·   No starvation.
·   Allows maximum parallelism, letting multiple philosophers eat at the same time when
possible.
c.   5
d. Four strategies are used for dealing with deadlocks.   5
1. Deadlock Ignorance-Just ignore the problem. Maybe if you ignore it, it will ignore you.
2. Deadlock Recovery-Detection and recovery. Let them occur, detect them, and take action.
Page 6 of 11
--- page 7 ---
3. Deadlock Avoidance- Dynamic avoidance by careful resource allocation.
4. Deadlock Prevention-Prevention, by structurally negating one of the four conditions.
Deadlock Prevention
Restrain the ways request can be made
¢ Mutual Exclusion – not required for sharable resources (e.g., read-only files); must hold for
non-sharable resources
¢ Hold and Wait – must guarantee that whenever a process requests a resource, it does not
hold any other resources
Ƙ Require process to request and be allocated all its resources before it begins execution, or
allow process to request resources only when the process has none allocated to it.
Ƙ Low resource utilization; starvation possible
¢ No Preemption –
Ƙ If a process that is holding some resources requests another resource that cannot be
immediately allocated to it, then all resources currently being held are released
Ƙ Preempted resources are added to the list of resources for which the process is waiting
Ƙ Process will be restarted only when it can regain its old resources, as well as the new ones
that it is requesting
¢ Circular Wait – impose a total ordering of all resource types, and require that each process
requests resources in an increasing order of enumeration
e. i.   0   5
0 falls in 0K to 4K. This is mapped to 20K to 24K. Hence physical address is 20480
ii.   30000
30000 falls in 28K to 32K.
30000-28,672 = 1328
This is mapped to 24K to 28K
Hence physical address is 24576+1328 = 25904
iii.   25325
25325 falls in 24K to 38K.
25325-24576=749
This is mapped to 12K to 16K
Hence physical address is 12288+749= 13037
f.   5
Page 7 of 11
--- page 8 ---
i) RAG edges
Assignment:
3DPrinter→P1, LaserCutter→P2, Plotter→P3, BluRayWriter→P4, USBDrive→P5
Request:
P1→LaserCutter, P2→Plotter, P3→BluRayWriter, P4→USBDrive, P5→3DPrinter,
P6→Plotter
ii) Deadlock? Yes.
iii) Deadlock cycle:
P1→LaserCutter→P2→Plotter→P3→BluRayWriter→P4→USBDrive→P5→3DPrinter→P1
Involved: P1–P5 and 3DPrinter, LaserCutter, Plotter, BluRayWriter, USBDrive.
P6 waits for Plotter → blocked but not in the cycle.
3.   Answer the following questions:(Attempt Any 4 Questions)   20
a. Step 1: Create the hard links   5
cd playground
ln fun fun-hard
ln fun dir1/fun-hard
ln fun dir2/fun-hard
These commands create three hard links:
playground/fun-hard
playground/dir1/fun-hard
playground/dir2/fun-hard
Step 2: Verify
ls -li fun fun-hard dir1/fun-hard dir2/fun-hard
Example output:
12353538 -rw-r--r-- 4 me me 1650 Mar 10 12:33 fun
12353538 -rw-r--r-- 4 me me 1650 Mar 10 12:33 fun-hard
12353538 -rw-r--r-- 4 me me 1650 Mar 10 12:33 dir1/fun-hard
12353538 -rw-r--r-- 4 me me 1650 Mar 10 12:33 dir2/fun-hard
·   Inode number 12353538 is the same for all four names (original + three links).
Page 8 of 11
--- page 9 ---
·   The link count (4) confirms that these four directory entries all point to the same data
blocks.
Thus, even if you delete fun, the file’s data remains accessible through any of the hard links.
b. Absolute Pathname   5
An absolute pathname gives the complete path to a file or directory starting from the root
directory /.
It always begins with / and uniquely identifies a location no matter where you are in the
filesystem.
Example:
/home/student/projects/report.txt
This path starts at the root /, then goes through home, student, projects, and finally the file
report.txt.
Using cd with an absolute path
If we are anywhere in the system and run:
cd /home/student/projects
we will always end up in /home/student/projects, because the path is absolute.
We can confirm our location with:
pwd
which will display:
/home/student/projects
Relative Pathname
A relative pathname describes a location in relation to the current working directory.
It never begins with /; it starts with a directory name or with special symbols:
. – the current directory
.. – the parent directory (one level up)
If the current directory is /home/student, the relative path to the same report.txt file could
simply be:
projects/report.txt
because we are already inside /home/student.
Using cd with a relative path
Suppose we are in /home/student:
cd projects
This moves us to /home/student/projects without writing the full path.
We can also go up one level and then into another directory:
cd ../downloads
Here .. means “parent directory,” so we move to /home/downloads.
Page 9 of 11
--- page 10 ---
we can even include . to explicitly reference the current directory:
cd ./projects
which is effectively the same as cd projects.
c.   5
d.   5
Examples
[me@linuxbox ~]$ echo $((2 + 2))
4
[me@linuxbox ~]$ echo $(($((5**2)) * 3))
75
e.   i.   cat playlist.txt   5
ii.   cat clip.001 clip.002 clip.003 > clip_full.mkv
iii.   cat
(Type text, finish with Ctrl+D.)
Everything typed is echoed back
Page 10 of 11
--- page 11 ---
iv.   cat > favorites.txt
My favorite songs go here.
[Ctrl+D]
v.   cat < favorites.txt
f.   i.   ls a*   5
ii.   ls b*.txt
iii.   ls data???
iv.   ls [abc]*
v.   ls [[:upper:]]*
Page 11 of 11
````
