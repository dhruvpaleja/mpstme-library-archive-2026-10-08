# Information Security: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 400a160a109b

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSBS_7036/Information Security/ANS_Information Security(702CO0C036)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: mixed (54 pages), mean OCR confidence 94.3
- 5 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Information Security
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 54 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of the remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1
SO-   a.   Explain the different security goals with example.   [5]
BL-2
Example for each and explanation.
Ans.
CO-2   Explain the terminologies with example with respect to a program security.
SO-   1. Error
b.   2. Fault   [5]
BL-2   3. Failure
4. Flaw
********** 1 **********

[Text in pictures on this page, read by OCR]
_ Security Goals

> Confidentiality > Authentication
¢ Assuring that the communicating
entity is the one that it claims to be

> Access Control

* Only intended users should be able
to access the contents of a message

» Integrity ° Who can access what resources and|
« A message should be preserved as it under what conditions
travels from one point to another > Non- Repudiation
> Availability A Protection against denial by one of
the entities involved in al
» It ensures that the resources are Garment

available to the authorized entities
at all time
--- page 2 ---
Ans.
CO-3   Explain the following terminologies.
SO-   1. Identity
2. Files and Objects
c.   [5]
3. Users
BL-2   4. Groups and Roles
Ans.
********** 2 **********

[Text in pictures on this page, read by OCR]
Sidebar 3-1 The Terminology of (Lack of) Quality

Thanks to Admiral Grace Murray Hopper, we casually call a software problem a
“bug.” [KID98] But that term can mean different things depending on context: a
mistake in interpreting a requirement, a syntax error in a piece of code, or the
(as-yet-unknown) cause of a system crash. The Institute of Electronics and
Electrical Engineers (IEEE) suggests using a standard terminology (in IEEE
Standard 729) for describing bugs in our software products [IEE83].

When a human makes a mistake, called an error, in performing some
software activity, the error may lead to a fault, or an incorrect step, command,
process, or data definition in a computer program, design, or documentation. For
example, a designer may misunderstand a requirement and create a design that
does not match the actual intent of the requirements analyst and the user. This
design fault is an encoding of the error, and it can lead to other faults, such as
incorrect code and an incorrect description in a user manual. Thus, a single error
can generate many faults, and a fault can reside in any development or
maintenance product.

A failure is a departure from the system’s required behavior. It can be
discovered before or after system delivery, during testing, or during operation
and maintenance. Since the requirements documents can contain faults, a failure
indicates that the system is not performing as required, even though it may be
performing as specified.

Thus, a fault is an inside view of the system, as seen by the eyes of the
developers, whereas a failure is an outside view: a problem that the user sees.
Every failure has at least one fault as its root cause. But not every fault
corresponds to a failure; for example, if faulty code is never executed or a
particular state is never entered, the fault will never cause the code to fail.

Although software engineers usually pay careful attention to the distinction
between faults and failures, security engineers rarely do. Instead, security
engineers use flaw to describe both faults and failures. In this book, we use the
security terminology; we try to provide enough context so that you can
understand whether we mean fault or failure.

15.1. What Is Identity?

Identity is simply a computer’s representation of an entity.

Definition 15-1. A principal is a unique entity. An identity specifies a
principal.

Authentication binds a principal to a representation of identity internal
to the computer. Each system has its own way of expressing this representation,
--- page 3 ---
but all decisions of access and resource allocation assume that the binding is
correct.

Identities are used for several purposes. The two main ones are for
accountability and for access control. Accountability requires an identity that
tracks principals across actions and changes of other identities, so that the
principal taking any action can be unambiguously identified. Access control
requires an identity that the access control mechanisms can use to determine if
a specific access (or type of access) should be allowed.

Accountability is tied to logging and auditing. It requires an unambiguous
identification of the principal involved. On many systems, this is not possible.
Instead, the logged identity maps to a user account, to a group, or to a role.

Most systems base access rights on the identity of the principal executing
the process. That is, all processes executed by user bishop have some set of rights.
All processes executed by user holly have a set of rights that may differ from those
that bishop’s processes have. However, a process may have fewer rights than the
principal executing it, and in fact there are substantial reasons to reduce privileges.
Chapter 16, “Access Control Mechanisms,” discusses this topic in more depth.

15.2 Files and Objects

The identity of a file or other entity (here called an “object”) depends on the
system that contains the object.

Local systems identify objects by assigning names. The name may be
intended for human use (such as a file name), for process use (such as a file
descriptor or handle), or for kernel use (such as a file allocation table entry). Each
name may have different semantics.

EXAMPLE: The UNIX operating system offers four different types of file names.
The device number and inode uniquely identify a file. The inode contains file
attribute information such as access control permissions and ownership informa-
tion, and identifies the specific disk blocks that contain the file’s data. Processes
read files using a file descriptor that abstracts the inode into a representation that
the process can read from, write to, and so forth. Once created, the file descriptor
cannot be rebound to a different file. Processes (and users) can also use file names
that identify files by describing their positions in the file hierarchy. UNIX file
names may be absolute path names that describe the locations of files with respect
to the root of the UNIX file hierarchy, or relative path names that describe the
locations of files with respect to the directory in which the current process is
executing.

The semantics of the names differ in important ways. Most critically, when
a process or user operates on a file, the kernel maps the file name to an inode using

FC QI a iar
--- page 4 ---
an iterative procedure. It obtains the inode of the first directory in the path,! opens
it, and within that directory locates the inode number of the next component in
the path. This continues until the file’s inode number is found. Two references to
the same file name will reference different file objects when the file is deleted after
the first reference and a new file, with the same name as the deleted file, is created.
This can create problems with programs (see Section 31.5.3.3, “Race Conditions
in File Accesses”).

However, when a file descriptor is created, it refers to a specific object.
Regardless of how the file is manipulated, the inode that the file descriptor refers
to remains present until the file descriptor is closed, which breaks the association
between the descriptor and the inode.

If the object resides on a different system, the name must encode the
location of the object.

EXAMPLE: A uniform resource locator (URL) identifies an object by its location
and the protocol needed to access it. The object with the URL Attp://
abccorp.comlpub/README specifies that the named object can be accessed by
using the HTTP protocol to request the object /pub/README from the host
abccorp.com. The URL does not say that the object is located on that host. Indeed,
the host may construct the object to respond to the request, or it may forward the
request to another host, or it may be invalid.

One file may have multiple names. The semantics of the system determine
the effects of each name. For example, some systems define “deleting a file” to
mean removing the given file name. The file object itself will not be deleted until
all its names (or all names meeting certain conditions) have been deleted. Section
30.3.1.3, “File Deletion,” discusses this issue further.

15.3. Users

In general, a user is an identity tied to a single entity. Specific systems may add
additional constraints. Systems represent user identity in a number of different
ways. Indeed, the same system may use different representations of identity in
different contexts.

'If the path is an absolute path name, the first directory in the path is the root directory, which has a
well-known inode number (typically 0, 1, or 2). If the path is a relative path name, the first directory
has the same inode number as the directory in which the process executes.

FIC 7) IC HOH
--- page 5 ---
EXAMPLE: Versions of the UNIX operating system usually represent user iden-
tity as an integer between 0 and some large integer (usually 65,535). This integer
is called the user identification number, or UID. Principals (called users) may also
be assigned /ogin names. Each login name corresponds to a single UID (although
one UID may have many different login names).

When the kernel deals with user identity, it uses the UID; for example, the
superuser is any user whose UID is 0 regardless of that user’s name. However,
when a user logs in, she provides her identity as her login name. Similarly, all
logging uses the login name rather than the numeric UID.

The same principal may have many different identities. Typically each
identity serves a particular function.

EXAMPLE: Versions of the UNIX operating system provide several types of user
identities [1294]. Because a user is a subject, and a process executes on behalf of
a user, the various identities are associated with processes. The real UID is the
user identity at initial login, but it can be changed. The effective UID is the user
identity used for access control. For example, if only UID 22 can read a particular
file, and a process’s real UID is 22 and its effective UID is 35, the user will not be
able to read the file. If the process’s real UID were 35 and its effective UID were
22, access would be granted.

A special class of programs, called setuid programs [747], create processes
with the effective UID being that of the owner of the program rather than that of
the user executing the program. The resulting process has the access rights of the
owner of the program rather than those of the user executing the program.

In an effort to limit the need for special privileges, UNIX systems provide
a saved UID. Whenever the effective UID changes, the saved UID is set to the
value of the effective UID before the change. The user can switch among the real,
effective, and saved UIDs. This allows the process to be given root privileges, use
them for a limited time (effective UID of 0), drop them (saved UID of 0, nonzero
effective UID), and reacquire them later.

Traditionally, the real UID was used to track the original UID of the
process. However, the superuser can change it. To provide an unalterable means
of recording the original real UID of the process, many UNIX systems provide
an audit or login UID. This UID is assigned at login and cannot be changed.?

Where disambiguation of two users with the same identification is required,
additional information is needed. On a network, for example, the host name or
domain name may be attached to the identity.

EXAMPLE: Kerberos key distribution centers (see Section 11.2.2) can interop-
erate. Each one forms the basis of a “realm” (essentially a domain controlled
by the Kerberos key distribution center). Kerberos users are then identified
by both name and realm. For example “anne@realm1.com” refers to the user

FIC DI EH ar
--- page 6 ---
15.4 Groups and Roles

An “entity” may be a set of individual entities referred to by a single identifier.
The members of the set must be distinguishable, but the set may have an identity
separate from any of its elements.

Principals often need to share access to files. Most systems allow principals
to be grouped into sets called, logically enough, groups. Groups are essentially a
shorthand tool for assigning rights to a set of principals simultaneously.

Two implementations of groups provide different abilities and therefore are
based on different models. The first simply uses a group as an alias for a set of
principals. Principals are assigned to groups, and they stay in those groups for
the lifetimes of their sessions. The second model allows principals to change from
one group to another. After each change, the rights belonging to the principal as
a member of the previous group are discarded and the rights of the new group are
added. The difference lies in the representations of identity. In the former model,
the identity assigned to a principal remains static; it is the principal identity and
the set of identities of each group that the principal is a part of. This identity does
not change throughout the lifetime of the session. In the latter model, the identity
of the principal is the identity of the user and the set of identities of each group of
which the principal is currently a member. It is dynamic, and should the principal
change from one group to another, the identity of that principal also changes.
In practice, one discusses “user identity” and “group identity.”

EXAMPLE: UNIX users are assigned membership to a group when they log
in [1294]. Each process has two identities, a “user identification” and a “group
identification.” On older UNIX systems, each principal can be in only one group
ata time. The command newgrp(1) changes this identity. The principal can change
to any group of which he is a member. On other UNIX systems, each principal
can be in several groups at a time. On login, the user is placed into all groups of
which he is a member.

Membership in a group is often based on some set of attributes, for example
membership in an organization, a particular medical condition, or access to
particular sets of equipment or data. A commonly used attribute is a person’s job
because the job requirements dictate the rights that someone needs to do the job.

More precisely, a role is a type of group that ties membership to function.
When a principal assumes a role, the principal is given certain rights that belong to
that role. When the principal leaves the role, those rights are removed. The rights
given are consistent with the functionality that the principal needs to perform the
tasks expected of members of the role.

COo-3

SO- d. | Define digital forensics and its types. [5]

BL-2

FIC 6 I HF
--- page 7 ---
Ans.

Introduction to Digital Forensic

Forensic science is a well-established science that plays a
critical role in criminal justice systems.

Forensic science is often referred to as forensics.

Digital forensics is also referred to as digital forensic science, a
branch of computer forensic science that includes the
restoration and inspection of material detected in digital
devices, often in relation to a cybercrime.

Digital Forensic is a series of steps to uncover and analyze
electronic data through scientific method. The major goal of the
process is to duplicate original data and preserve original
evidence then performing the series of the investigation by
collecting, identifying and validating the digital information for
the purpose of reconstructing past events.

Need of Digital Forensic

The meaning of the word “forensics” is “to bring to the
court”.

It is necessary for network administrator and security staff
of networked organizations to practice computer forensics
and should have knowledge of laws, because rate of cyber
crimes is increasing greatly.

the major goal of computer forensics is to recognize,
gather, protect and examine data in such a way that
protects the integrity of the collected evidence to use it
efficiently and effectively in a case.

FIC 7 IC OHH
--- page 8 ---
Types of Digital Forensic

Computer Forensics — the identification, preservation, collection, analysis and
reporting on evidence found on computers, laptops, and storage media in support
of investigations and legal proceedings.

Network Forensics — the monitoring, capture, storing, and analysis of network
activities or events in order to discover the source of security attacks, intrusions
or other problem incidents, that is, worms, virus, or malware attacks, abnormal
network traffic and security breaches.

Mobile Devices Forensics — the recovery of electronic evidence from mobile
phones, smartphones, SIM cards, PDAs, GPS devices, tablets, and game
consoles. Mobile device forensics involves the recovery of digital evidence or
data from mobile devices.

Digital Image Forensics — the extraction and analysis of digitally acquired
photographic images to validate their authenticity by recovering the metadata of
the image file to ascertain its history

Digital Video/Audio Forensics — the collection, analysis, and evaluation of sound
and video recordings. The science is the establishment of authenticity as to
whether a recording is original and whether it has been tampered with,either
maliciously or accidentally.

Memory forensics — the recovery of evidence from the RAM of a running
computer, also called live acquisition.

Qz [20]
CO-2

SO- a. Discuss buffer overflow attack in depth. [10]
BL-2

Implications of Overwriting Memory

Let us more closely examine the problem of overwriting memory. Be sure to recognize
that the potential overflow causes a serious problem only in some instances. The
problem’s occurrence depends on what is adjacent to the array sample. For example,
suppose each of the ten elements of the array sample is filled with the letter A and the
erroneous reference uses the letter B, as follows:

Click here to view code image
Ans. for (i=0; i<=9; i++)
sample[i] = ‘A’;
sample[10] = ‘B’

All program and data elements are in memory during execution, sharing space with the
operating system, other code, and resident routines. So four cases must be considered in
deciding where the ‘B’ goes, as shown in Figure 3-4. If the extra character overflows into
the user’s data space, it simply overwrites an existing variable value (or it may be written
into an as-yet unused location), perhaps affecting the program’s result but affecting no
other program or data.

FIC QF EH 1
--- page 9 ---
User's Data
OO

— RGEBOOEROOo

(a) Affects user's data

User's Data User's Program Code

Memory Jafalafafala}afafa}a |

(b) Affects user's code

User's Data System Data

Line BGGEODOEEBD

(c) Affects system data

User's Data System Program Code

— RGEEBOEROoo

(d) Affects system code
FIGURE 3-4 One-Character Overflow

In the second case, the ‘B’ goes into the user’s program area. If it overlays an already
executed instruction (which will not be executed again), the user should perceive no
effect. If it overlays an instruction that is not yet executed, the machine will try to execute
an instruction with operation code 0x42, the internal code for the character ‘B’. If there is
no instruction with operation code 0x42, the system will halt on an illegal instruction
exception. Otherwise, the machine will use subsequent bytes as if they were the rest of the
instruction, with success or failure depending on the meaning of the contents. Again, only
the user is likely to experience an effect.

The most interesting cases (from a security perspective) occur when the system owns
the space immediately after the array that overflows. Spilling over into system data or
code areas produces results similar to those for the user’s space: computing with a faulty
value or trying to execute an operation.

Program procedures use both local data, data used strictly within one procedure, and
shared or common or global data, which are shared between two or more procedures.
Memory organization can be complicated, but we simplify the layout as in Figure 3-5. In
that picture, local data are stored adjacent to the code of a procedure. Thus, as you can see,
a data overflow either falls strictly within a data space or it spills over into an adjacent
code area. The data end up on top of one of

+ another piece of your data
* an instruction of yours

FIC QF OH ar
--- page 10 ---
+ data or code belonging to another program
+ data or code belonging to the operating system

We consider each of these cases separately.

User |’s
code &
Proc M
data of
Proc M data
User 2’s Proc A
code &
data Proc A data
Operating Proc B
system’s Proc B data
code &
data

FIGURE 3-5 Memory of Different Procedures for Different Users
Affecting Your Own Data

Modifying your own data, especially with an unintended value, will obviously affect
your computing. Perhaps a loop will repeat too many or too few times, a sum will be
compromised, or a date will become garbled. You can imagine these possibilities for
yourself. The error may be so egregious that you will easily recognize something is
wrong, but a more subtle failure may escape your notice, perhaps forever.

From a security standpoint, few system controls protect you from this kind of error: You
own your data space and anything you want to store there is your business. Some, but not
all, programming languages generate checking code for things like arrays to ensure that
you store elements only within the space allocated. For this reason, the defensive
programming technique (discussed later in this chapter) recommends that you always
check to ensure that array elements and strings are within their boundaries. As Sidebar 3-3
demonstrates, sometimes such an error lies dormant for a long time.

FRR ICR 7 OI HOH
--- page 11 ---
specialized communications processors called IMPs. Each interface message
processor (IMP) controlled an individual subnetwork, much like today’s routers;
the IMPs connected to other IMPs through dedicated communications lines. For
reliability, each IMP had at least two distinct paths to each other IMP. The IMP
connections were added to a table dynamically as communication between two
IMPs was required by network traffic.

In 1988, one subnetwork added a connection to a 348th IMP. The table for
IMP connections had been hard-coded in 1969 to only 347 entries, which
seemed wildly excessive at the time, and in the intervening years people had
forgotten that table size if, indeed, it had ever been publicized. (In 1967, 347
IMPs was far more than the designers ever envisioned the network would have.)
Software handling the IMP’s table detected this overflow but handled it by
causing the IMP to reboot; upon rebooting, the IMP’s table was cleared and
would be repopulated as it discovered other reachable subnetworks. Apparently
the authors of that software assumed such a table overflow would be a sporadic
mistake from another cause, so clearing and rebooting would rid the table of the
faulty data. Because the fault was due to a real situation, in 1989 the refreshed
IMP ran for a while until its table refilled and then it failed and rebooted again.

It took some time to determine the source and remedy of this flaw, because
twenty years had passed between coding and failing; everybody associated with
the original design or implementation had moved on to other projects.

As this example shows, buffer overflows—like other program faults—can
remain unexploited and undetected for some time, but they are still present.

Affecting an Instruction of Yours

Again, the failure of one of your instructions affects you, and systems give wide latitude
to what you can do to yourself. If you store a string that does not represent a valid or
permitted instruction, your program may generate a fault and halt, returning control to the
operating system. However, the system will try to execute a string that accidentally does
represent a valid instruction, with effects depending on the actual value. Again, depending
on the nature of the error, this faulty instruction may have no effect (if it is not in the path
of execution or in a section that has already been executed), a null effect (if it happens not
to affect code or data, such as an instruction to move the contents of register 1 to itself), or
an unnoticed or readily noticed effect.

Destroying your own code or data is unpleasant, but at least you can say the harm was
your own fault. Unless, of course, it wasn’t your fault. One early flaw in Microsoft’s
Outlook involved the simple date field: A date is a few bytes long to represent a day,
month, year, and time in GMT (Greenwich Mean Time) format. In a former version of
Outlook, a message with a date of more than 1000 bytes exceeded the buffer space for
message headers and ran into reserved space. Simply downloading such a message from a
mail server would cause your system to crash, and each time you tried to restart, Outlook
would try to reload the same message and crash again. In this case, you suffered harm
from a buffer overflow involving only your memory area.

One program can accidentally modify code or data of another procedure that will not be

FRI ICR 7 FI OH
--- page 12 ---
CO-3   What do you mean by operating system security. Explain the following.
SO-   b.   1. separation   [10]
2. memory protection
BL-1   3. access control
Ans.
********** 12 **********

[Text in pictures on this page, read by OCR]
executed until much later, so the delayed impact can be almost as difficult to diagnose as if
the attack came from an unrelated, independent user. The most significant impact of a
buffer overflow occurs when the excess data affect the operating system’s code or data.

Modification of code and data for one user or another is significant, but it is not a major
computer security issue. However, as we show in the next section, buffer overflows
perpetrated on the operating system can have serious consequences.

Affecting the Operating System or a Critical Application

The same basic scenarios occur for operating system code or data as for users, although
again there are important variations. Exploring these differences also leads us to consider
motive, and so we shift from thinking of what are essentially accidents to intentional
malicious acts by an attacker.

Because the mix of programs changes continually on a computing system, there is little
opportunity to affect any one particular use. We now consider the case in which an
attacker who has already overtaken an ordinary user now wants to overtake the operating
system. Such an attack can let the attacker plant permanent code that is reactivated each
time a machine is restarted, for example. Or the attack may expose data, for example,
passwords or cryptographic keys that the operating system is entrusted to safeguard. So
now let us consider the impact a (compromised) user can have on the operating system.

Users’ code and data are placed essentially at random: wherever there is free memory of
an appropriate size. Only by tracing through system memory allocation tables can you
learn where your program and data appear in memory. However, certain portions of the
operating system are placed at particular fixed locations, and other data are located at
places that can easily be determined during execution. Fixed or easily determined location
distinguishes operating system routines, especially the most critical ones, from a user’s
code and data.

Asecond distinction between ordinary users and the operating system is that a user runs
without operating system privileges. The operating system invokes a user’s program as if
it were a subprocedure, and the operating system receives control back when the user’s
program exits. If the user can alter what the operating system does when it regains control,
the user can force the operating system to execute code the user wants to run, but with
elevated privileges (those of the operating system). Being able to modify operating system
code or data allows the user (that is, an attacker acting as the user) to obtain effective
privileged status.

Privilege escalation, executing attack code with higher system
permissions, is a bonus for the attacker.

The call and return sequence operates under a well-defined protocol using a data
structure called the stack. Aleph One (Elias Levy) describes how to use buffer overflows
to overwrite the call stack [ALE96]. In the next section we show how a programmer can
use an overflow to compromise a computer’s operation.

13.1 Introduction

In this chapter, we’ll look at some of the security issues related to operating
systems (OSs). OSs are large and complex pieces of software. Recall that in
Chapter 12 we argued that there are almost certain to be security flaws in
any large and complex computer program. But here we are concerned with
the security protection provided by the OS, not with the very real threat of
bad OS software. That is, we are concerned with the role of the OS as the
security enforcer. This is a large topic that ties into many other aspects of
security and we'll just barely scratch the surface.

First, we'll describe the primary security-related functions of any modern
operating system. Then we’ll discuss the notion of a trusted OS, and we’ll
conclude with a look at Microsoft’s fairly recent effort to develop a trusted
operating system, which goes by the catchy name of the Next Generation
Secure Computing Base, or better yet, NGSCB.
--- page 13 ---
13.2 OS Security Functions

An OS must deal with potential security issues whether they arise accidentally
or as part of a malicious attack. Modern OSs are designed for multi-user
environments and multi-tasking operations. Consequently, an OS must, at a
minimum, deal with separation, memory protection, and access control. We
briefly discuss each of these three topics below.

13.2.1 Separation

Arguably the most fundamental security issue for a modern OS is that of
separation. That is, the OS must keep users and processes separate from
each other.

There are several ways that separation can be enforced [235], including
the following:

e Physical separation — Users are restricted to separate devices. This
provides a strong form of separation, but it is often impractical.

e Temporal separation — Processes are separated in time. This eliminates
many problems that arise due to concurrency and simplifies the job of
the OS. However, there is a loss of efficiency.

e Logical separation — For example, each process might be allocated its
own “sandbox.” A process is free to do almost anything within its
sandbox, but it can do almost nothing outside of its sandbox.

e Cryptographic separation — Crypto can be used to make information
unintelligible to an outsider.

Of course, various combinations of these methods can be used.

13.2.2 Memory Protection

Another fundamental issue an OS must deal with is memory protection. This
includes protection for the memory that the OS itself uses as well as the
memory of user processes. A fence, or fence address, is one option for memory
protection. A fence is a particular address that users and their processes
cannot cross—only the OS can operate on one side of the fence, and users are
restricted to the other side.

A fence could be static, in which case there is a fixed fence address. How-
ever, this places a strict limit on the size of the OS, which is a major drawback
(or benefit, depending on your perspective). Alternatively, a dynamic fence
can be used, which can be implemented using a fence register to specify the
current fence address.

FIR ICR 7] QI HO
--- page 14 ---
In addition to a fence, base and bounds registers can be used. These
registers contain the lower and upper address limits of a particular user (or
process) space. The base and bounds register approach implicitly assumes
that the user (or process) space is contiguous in memory.

The OS must determine what protection to apply to a specific memory
location. In some cases it might be sufficient to apply the same protection
to all of a user’s (or process’s) memory. At the other extreme, tagging spec-
ifies the protection for each individual address. While this is as fine-grained
protection as possible, it introduces significant overhead. The overhead can
be reduced by tagging sections of the address space instead of each individ-
ual address. In any case, another drawback to tagging is compatibility, since
tagging schemes are not in common use.

The most common methods of memory protection are segmentation and
paging. While these are not as flexible as tagging, they’re much more efficient.
We briefly discuss each of these next.

Segmentation, as illustrated in Figure 13.1, divides the memory into log-
ical units, such as individual procedures or the data in one array. Then
appropriate access control can be enforced on each segments. A benefit of
segmentation is that any segment can be placed in any memory location—
provided the location is large enough to hold it. Of course, the OS must
keep track of the locations of all segments, which is accomplished using
<segment ,offset> pairs, where the cleverly named segment specifies the
segment, and the offset is the starting address of the specified segment.

memory

Figure 13.1: Segmentation

Other benefits of segmentation include the fact that segments can be
moved to different locations in memory and they can also be moved in and out
of memory. With segmentation, all address references must go through the
OS, so the OS can, in this respect, achieve complete mediation. Depending

FRR IC 7 I OH
--- page 15 ---
Q3   [20]
CO-3   Describe the following principles of secure design with example.
SO-   a.   1. Principle of Least Privilege   [10]
2. Principle of Least Authority
BL-2   3. Principle of Fail-Safe Defaults
********** 15 **********

[Text in pictures on this page, read by OCR]
on the access control applied to particular segments, users can share access
to some segments or users can be restricted to specific segments.

One serious drawback to segmentation is that the segments are of variable
sizes. As a result, before the OS tries to reference any element of a given
segment it must know the size of the segment so that it can be sure that
the requested address is within the segment. But some segments—such as
those that include dynamic memory allocation—can grow during execution.
Consequently, the OS must keep track of dynamic segment sizes. And due
the variability of segment sizes, memory fragmentation is a potential problem.
Finally, when memory is compacted to make better use of the available space,
the segmentation tables change. In short, segmentation is complex and places
a significant burden on the OS.

Paging is like segmentation, except that all segments are of a fixed size,
as illustrated in Figure 13.2. With paging, access to a particular page uses a
pair of the form <page, offset>. The advantages of paging over segmentation
include no fragmentation, improved efficiency, and the fact that there are no
variable sizes to worry about. The disadvantages are that there is, in general,
no logical unity to pages, which makes it more difficult to determine the
proper access control to apply to a given page.

memory

Page 1
program fee
Page 0 ee eee

Page 1 |_fovee _|

Page 2 Poge.0

Page 3

Page 4 ne
Page 3

Figure 13.2: Paging

13.2.3. Access Control

OSs are the ultimate enforcers of access control. This is one reason why the
OS is such an attractive target for attack—a successful attack on the OS
can effectively nullify any protection built in at a higher level. We discussed
access control in Chapter 8 and we’ll briefly return to the subject in the next
section when we discuss the concept of a trusted OS.
--- page 16 ---
Ans.

14.2 Principles of Secure Design

The principles of secure design discussed in this section express common-sense
applications of simplicity and restriction in terms of computing. We will discuss
detailed applications of these principles throughout the remainder of Part V and
in Part VIII, “Practicum.” However, this chapter mentions specific examples.

14.2.1. Principle of Least Privilege
This principle restricts how privileges are granted.

Definition 14-1. The principle of least privilege states that a subject should
be given only those privileges that it needs in order to complete its task.

If a subject does not need an access right, the subject should not have that
right. Furthermore, the function of the subject (as opposed to its identity) should
control the assignment of rights. If a specific action requires that a subject’s access
rights be augmented, those extra rights should be relinquished immediately on
completion of the action. This is the analogue of the “need to know” rule: if the
subject does not need access to an object to perform its task, it should not have
the right to access that object. More precisely, if a subject needs to append to an
object, but not to alter the information already contained in the object, it should
be given append rights and not write rights.

In practice, most systems do not have the granularity of privileges and
permissions required to apply this principle precisely. The designers of security
mechanisms then apply this principle as best they can. In such systems, the
consequences of security problems are often more severe than the consequences
for systems that adhere to this principle.

EXAMPLE: The UNIX operating system does not apply access controls to the
user root. That user can terminate any process and read, write, or delete any file.
Thus, users who create backups can also delete files. The administrator account
on Windows has the same powers.

FRR ICR 7 6 AC OH
--- page 17 ---
This principle requires that processes should be confined to as small a
protection domain as possible.

EXAMPLE: A mail server accepts mail from the Internet and copies the messages
into a spool directory; a local server will complete delivery. The mail server needs
the rights to access the appropriate network port, to create files in the spool
directory, and to alter those files (so it can copy the message into the file, rewrite the
delivery address if needed, and add the appropriate “Received” lines). It should
surrender the right to access the file as soon as it has finished writing the file
into the spool directory, because it does not need to access that file again. The
server should not be able to access any user’s files, or any files other than its own
configuration files.

14.2.1.1 Principle of Least Authority

Closely related to the principle of least privilege is the principle of least author-
ity [1349]. The two are often treated as meaning the same. However, some authors
make a distinction between “permission” and “authority.” They treat permission
as determining what actions a process can take on objects directly, and authority
as determining that effects a process may have on an object, either directly (as
with permission) or indirectly through its interactions with other processes or
subsystems.

Miller and Shapiro [1349] give a good example from the Take-Grant
Protection Model. In that model, the rights would represent actions that subjects
could take over objects, and so represent permissions. But the de facto rules of
that model, which govern information transfer, show how information can flow
from a subject to an object that is not directly connected to the subject. Hence the
subject does not have permission to write information into the object, but it does
have permission to pass the information to a second subject, and that subject can
write the information into the object.!

Definition 14-2. The principle of least authority states that a subject should
be given only the authority that it needs in order to complete its task.

If one reads the principle of least privilege as speaking to permissions, then

this principle is somewhat different. But if it speaks to authority, the two are the
same.

14.2.2 Principle of Fail-Safe Defaults

This principle restricts how privileges are initialized when a subject or object is
created.

FRR ICR] AC OH
--- page 18 ---
CO-3
Describe the working of IDS. Describe basic principle of IDS and desirable
SO-   b.   [10]
requirements for an IDS system.
BL-2
Ans.
********** 18 **********

[Text in pictures on this page, read by OCR]
Definition 14-3. The principle of fail-safe defaults states that, unless a
subject is given explicit access to an object, it should be denied access to
that object.

This principle requires that the default access to an object is none. Whenever
access, privileges, or some security-related attribute is not explicitly granted, it
should be denied. Moreover, if the subject is unable to complete its action or task,
it should undo those changes it made to the security state of the system before it
terminates. This way, even if the program fails, the system is still safe.

EXAMPLE: If the mail server is unable to create a file in the spool directory,
it should close the network connection, issue an error message, and stop. It
should not try to store the message elsewhere or to expand its privileges to
save the message in another location, because an attacker could use that ability
to overwrite other files or fill up other disks (a denial of service attack). The
protections on the mail spool directory itself should allow create and write access
only to the mail server and read and delete access only to the local server. No other
user should have access to the directory.

In practice, most systems will allow an administrator access to the mail
spool directory. By the principle of least privilege, that administrator should be
able to access only the subjects and objects involved in mail queueing and delivery.
As we have seen, this constraint minimizes the threats if that administrator’s
account is compromised. The mail system can be damaged or destroyed, but
nothing else can be.

Because many users do not change default access control permissions, this
rule applies to the default settings for both the system and for users.

8.2 INTRUSION DE ON

The following terms are relevant to our discussion:

security intrusion: Unauthorized act of bypassing the security mechanisms of a
system.

intrusion detection: A hardware or software function that gathers and analyzes
information from various areas within a computer or a network to identify possible
security intrusions.

An IDS comprises three logical components:

° Sensors: Sensors are responsible for collecting data. The input for a sensor may
be any part of a system that could contain evidence of an intrusion. Types of
input to a sensor includes network packets, log files, and system call traces.
Sensors collect and forward this information to the analyzer.

e Analyzers: Analyzers receive input from one or more sensors or from other ana-
lyzers. The analyzer is responsible for determining if an intrusion has occurred.
The output of this component is an indication that an intrusion has occurred.
The output may include evidence supporting the conclusion that an intrusion
occurred. The analyzer may provide guidance about what actions to take as a
result of the intrusion. The sensor inputs may also be stored for future analysis
and review in a storage or database component.
--- page 19 ---
¢ User interface: The user interface to an IDS enables a user to view output from
the system or control the behavior of the system. In some systems, the user
interface may equate to a manager, director, or console component.

An IDS may use a single sensor and analyzer, such as a classic HIDS on a host
or NIDS in a firewall device. More sophisticated IDSs can use multiple sensors, across
a range of host and network devices, sending information to a centralized analyzer
and user interface in a distributed architecture.

IDSs are often classified based on the source and type of data analyzed, as:

¢ Host-based IDS (HIDS): Monitors the characteristics of a single host and the
events occurring within that host, such as process identifiers and the system calls
they make, for evidence of suspicious activity.

¢ Network-based IDS (NIDS): Monitors network traffic for particular network
segments or devices and analyzes network, transport, and application protocols
to identify suspicious activity.

¢ Distributed or hybrid IDS: Combines information from a number of sensors,
often both host and network-based, in a central analyzer that is able to better
identify and respond to intrusion activity.

Basic Principles

Authentication facilities, access control facilities, and firewalls all play a role in coun-
tering intrusions. Another line of defense is intrusion detection, and this has been
the focus of much research in recent years. This interest is motivated by a number of
considerations, including the following:

1. If an intrusion is detected quickly enough, the intruder can be identified and
ejected from the system before any damage is done or any data are compro-
mised. Even if the detection is not sufficiently timely to preempt the intruder,
the sooner that the intrusion is detected, the less the amount of damage and
the more quickly that recovery can be achieved.

2. An effective IDS can serve as a deterrent, thus acting to prevent intrusions.

3. Intrusion detection enables the collection of information about intrusion tech-
niques that can be used to strengthen intrusion prevention measures.

Intrusion detection is based on the assumption that the behavior of the intruder
differs from that of a legitimate user in ways that can be quantified. Of course, we
cannot expect that there will be a crisp, exact distinction between an attack by an
intruder and the normal use of resources by an authorized user. Rather, we must
expect that there will be some overlap.

Figure 8.1 suggests, in abstract terms, the nature of the task confronting the
designer of an IDS. Although the typical behavior of an intruder differs from the typi-
cal behavior of an authorized user, there is an overlap in these behaviors. Thus, a loose
interpretation of intruder behavior, which will catch more intruders, will also lead to
a number of false positives, or false alarms, where authorized users are identified as
intruders. On the other hand, an attempt to limit false positives by a tight interpreta-
tion of intruder behavior will lead to an increase in false negatives, or intruders not

FRR ICR 7 QI OR
--- page 20 ---
Q4   [20]
CO-3
SO-   a.   List the different types of filtering services. Discuss firewall and its types in detail.   [10]
BL-2
********** 20 **********

[Text in pictures on this page, read by OCR]
Probability Profile of
density function authorized user
Profile of behavior

intruder behavior

Overlap in observed
or expected behavior

Average behavior Average behavior Measurable behavior
of intruder _of authorized user parameter

Figure 8.1 Profiles of Behavior of Intruders and Authorized Users

identified as intruders. Thus, there is an element of compromise and art in the practice
of intrusion detection. Ideally, you want an IDS to have a high detection rate, that is,
the ratio of detected to total attacks, while minimizing the false alarm rate, the ratio
of incorrectly classified to total normal usage [LAZA05].

In an important early study of intrusion [ANDE80], Anderson postulated that
one could, with reasonable confidence, distinguish between an outside attacker and a
legitimate user. Patterns of legitimate user behavior can be established by observing
past history, and significant deviation from such patterns can be detected. Anderson
suggests the task of detecting an inside attacker (a legitimate user acting in an unau-
thorized fashion) is more difficult, in that the distinction between abnormal and
normal behavior may be small. Anderson concluded that such violations would be
undetectable solely through the search for anomalous behavior. However, insider
behavior might nevertheless be detectable by intelligent definition of the class of
conditions that suggest unauthorized use. These observations, which were made in
1980, remain true today.

Requirements
[BALA9§] lists the following as desirable for an IDS. It must:

e Run continually with minimal human supervision.

¢ Be fault tolerant in the sense that it must be able to recover from system crashes
and reinitializations.

¢ Resist subversion. The IDS must be able to monitor itself and detect if it has
been modified by an attacker.

¢ Impose a minimal overhead on the system where it is running.

¢ Be able to be configured according to the security policies of the system that
is being monitored.

© Be able to adapt to changes in system and user behavior over time.
¢ Be able to scale to monitor a large number of hosts.

¢ Provide graceful degradation of service in the sense that if some components
of the IDS stop working for any reason, the rest of them should be affected as
little as possible.

¢ Allow dynamic reconfiguration; that is, the ability to reconfigure the IDS with-
out having to restart it.
--- page 21 ---
Filtering Services

» Filtering services play a crucial role in enhancing network security by
controlling and monitoring the flow of data within a network.
» Various filtering services are employed to protect against cyber threats,

manage network resources, and enforce policies.

Types of Filtering services

» Firewall — Examines the content and make the decision based on the traffic.

» Intrusion Prevention System — Monitor network and/or system activities for
malicious exploits or security policy violations and take action to block or prevent
those activities.

» Antivirus and Antimalware Filters — Scan files and network traffic for known
patterns or signatures of malicious software and prevent them from entering the
network.

» Web Content Filtering — Control and restrict access to certain websites or content
categories based on predefined policies. This helps prevent users from accessing
malicious or inappropriate content.

Types of Filtering services
Ans. P 9

» Email Filtering — Scan email content and attachments for malicious code, phishing
attempts, or spam. Email filtering helps prevent the delivery of malicious content
through email.

» DNS Filtering — Block access to malicious websites by filtering DNS requests. DNS
filtering can prevent users from accessing known malicious domains or websites.

» Application Layer Filtering — Control or block specific applications or services at
the application layer. This can include filtering instant messaging, peer-to-peer file

sharing, or other applications that may pose security risks.

Types of Filtering services

» Virtual Private Network Filtering - Manage and control access to VPN
connections to ensure secure and authorized remote access to the network.

» Data Loss Prevention — Monitor and control the transfer of sensitive data within
the network to prevent unauthorized access or data leakage.

» Packet Filtering — Examines packets of data and makes decisions to allow or block
the transmission based on predefined rules.

» Behavioral Analysis — Analyze the behavior of network traffic and detect

anomalies or patterns indicative of potential security threats.

FI ICR D7 FAC HOH
--- page 22 ---
Firewalls

> A firewall is a type of cybersecurity tool that is used to filter traffic on a
network. Firewalls can be used to separate network nodes from external
traffic sources, internal traffic sources, or even specific applications.
Firewalls can be software, hardware, or cloud-based, with each type of

firewall having its own unique pros and cons.

» The primary goal of a firewall is to block malicious traffic requests and data

packets while allowing legitimate traffic through.

Firewall types - Packet Filtering

» As the most “basic” and oldest type of firewall architecture, packet-filtering firewalls basically
create a checkpoint at a traffic router or switch. The firewall performs a simple check of the data
packets coming through the router—inspecting information such as the destination and
origination IP address, packet type, port number, and other surface-level information without
opening up the packet to inspect its contents.

» Ifthe information packet doesn’t pass the inspection, it is dropped.

» The good thing about these firewalls is that they aren’t very resource-intensive. This means they
don’t have a huge impact on system performance and are relatively simple. However, they’re also

relatively easy to bypass compared to firewalls with more robust inspection capabilities.

Firewall types - Circuit Level Gateways

» As another simplistic firewall type that is meant to quickly and easily approve or deny traffic
without consuming significant computing resources, circuit-level gateways work by verifying the
transmission control protocol (TCP) handshake. This TCP handshake check is designed to make

sure that the session the packet is from is legitimate.

» While extremely resource-efficient, these firewalls do not check the packet itself. So, if a packet
held malware, but had the right TCP handshake, it would pass right through. This is why circuit-

level gateways are not enough to protect your business by themselves.

Firewall types - Stateful Inspection

» These firewalls combine both packet inspection technology and TCP handshake
verification to create a level of protection greater than either of the previous two

architectures could provide alone.

» However, these firewalls do put more of a strain on computing resources as well. This

may slow down the transfer of legitimate packets compared to the other solutions

FIR ICR DAC HH
--- page 23 ---
Firewall types - Proxy

» Proxy firewalls operate at the application layer to filter incoming traffic between your network and
the traffic source—hence, the name “application-level gateway.” These firewalls are delivered via a
cloud-based solution or another proxy device. Rather than letting traffic connect directly, the proxy
firewall first establishes a connection to the source of the traffic and inspects the incoming data
packet.

» This check is similar to the stateful inspection firewall in that it looks at both the packet and at the
TCP handshake protocol. However, proxy firewalls may also perform deep-layer packet inspections,
checking the actual contents of the information packet to verify that it contains no malware.

> Once the check is complete, and the packet is approved to connect to the destination, the proxy
sends it off. This creates an extra layer of separation between the “client” (the system where the
packet originated) and the individual devices on your network—obscuring them to create additional
anonymity and protection for your network.

> If there’s one drawback to proxy firewalls, it’s that they can create significant slowdown because of
the extra steps in the data packet transferal process.

Firewall types - Next Generation

» Many of the most recently-released firewall products are being touted as “next-generation”

architectures. However, there is not as much consensus on what makes a firewall truly next-gen.

» Some common features of next-generation firewall architectures include deep-packet inspection
(checking the actual contents of the data packet), TCP handshake checks, and surface-level packet
inspection. Next-generation firewalls may include other technologies as well, such as intrusion

prevention systems (IPSs) that work to automatically stop attacks against your network.

> The issue is that there is no one definition of a next-generation firewall, so it’s important to verify

what specific capabilities such firewalls have before investing in one.

Firewall types - Software

» Software firewalls include any type of firewall that is installed on a local device rather
than a separate piece of hardware (or a cloud server). The big benefit of a software
firewall is that it's highly useful for creating defense in depth by isolating individual

network endpoints from one another.

» However, maintaining individual software firewalls on different devices can be difficult
and time-consuming. Furthermore, not every device on a network may be compatible
with a single software firewall, which may mean having to use several different

software firewalls to cover every asset.

FIR ICR 2 I OH
--- page 24 ---
Explanation for each in detail with example.
CO-2
SO-   b.   Write short note on incomplete mediation.   [10]
BL-2
Ans.
********** 24 **********

[Text in pictures on this page, read by OCR]
Firewall types - Hardware

» Hardware firewalls use a physical appliance that acts in a manner similar to a traffic router to
intercept data packets and traffic requests before they're connected to the network's servers.
Physical appliance-based firewalls like this excel at perimeter security by making sure malicious
traffic from outside the network is intercepted before the company's network endpoints are exposed

to risk.

> The major weakness of a hardware-based firewall, however, is that it is often easy for insider
attacks to bypass them. Also, the actual capabilities of a hardware firewall may vary depending on
the manufacturer—some may have a more limited capacity to handle simultaneous connections

than others.

Firewall types - Cloud

» Whenever a cloud solution is used to deliver a firewall, it can be called a cloud firewall,
or firewall-as-a-service (FaaS). Cloud firewalls are considered synonymous with proxy
firewalls by many, since a cloud server is often used in a proxy firewall setup (though

the proxy doesn't necessarily have to be on the cloud, it frequently is).

» The big benefit of having cloud-based firewalls is that they are very easy to scale with
your organization. As your needs grow, you can add additional capacity to the cloud
server to filter larger traffic loads. Cloud firewalls, like hardware firewalls, excel at

perimeter security.

Incomplete Mediation

Mediation means checking: the process of intervening to confirm an actor’s
authorization before it takes an intended action. In the last chapter we discussed the steps
and actors in the authentication process: the access control triple that describes what
subject can perform what operation on what object. Verifying that the subject is authorized
to perform the operation on an object is called mediation. Incomplete mediation is a
security problem that has been with us for decades: Forgetting to ask “Who goes there?”
before allowing the knight across the castle drawbridge is just asking for trouble. In the
same way, attackers exploit incomplete mediation to cause security problems.

Definition

Consider the following URL. In addition to a web address, it contains two parameters,
--- page 25 ---
so you can think of it as input to a program:
Click} . ici

http://www. somesite.com/subpage/user input .asp?
parmi=(808)555-12124parm2=2015Jan17
As a security professional trying to find and fix problems before they occur, you might
examine the various parts of the URL to determine what they mean and how they might be
exploited. For instance, the parameters parm1 and parm2 look like a telephone number
and a date, respectively. Probably the client’s (user’s) web browser enters those two values
in their specified format for easy processing on the server’s side.

But what would happen if parm2 were submitted as 1800Jan01? Or 1800Feb30? Or
2048Min32? Or 1Aardvark2Many? Something in the program or the system with which it
communicates would likely fail. As with other kinds of programming errors, one
possibility is that the system would fail catastrophically, with a routine’s failing on a data
type error as it tried to handle a month named “Min” or even a year (like 1800) that was
out of expected range. Another possibility is that the receiving program would continue to
execute but would generate a very wrong result. (For example, imagine the amount of
interest due today on a billing error with a start date of 1 Jan 1800.) Then again, the
processing server might have a default condition, deciding to treat 1Aardvark2Many as 21
July 1951. The possibilities are endless.

A programmer typically dismisses considering bad input, asking why anyone would
enter such numbers. Everybody knows there is no 30th of February and, for certain
applications, a date in the 1800s is ridiculous. True. But ridiculousness does not alter
human behavior. A person can type 1800 if fingers slip or the typist is momentarily
distracted, or the number might have been corrupted during transmission. Worse, just
because something is senseless, stupid, or wrong doesn’t prevent people from doing it.
And if a malicious person does it accidentally and finds a security weakness, other people
may well hear of it. Security scoundrels maintain a robust exchange of findings. Thus,
programmers should not assume data will be proper; instead, programs should validate
that all data values are reasonable before using them.

Users make errors from ignorance, misunderstanding, distraction; user
errors should not cause program failures.

Validate All Input

One way to address potential problems is to try to anticipate them. For instance, the
programmer in the examples above may have written code to check for correctness on the
client’s side (that is, the user’s browser). The client program can search for and screen out
errors. Or, to prevent the use of nonsense data, the program can restrict choices to valid
ones only. For example, the program supplying the parameters might have solicited them
by using a drop-down box or choice list from which only the twelve conventional months
could have been selected. Similarly, the year could have been tested to ensure a reasonable
value (for example, between 2000 and 2050, according to the application) and date
numbers would have to be appropriate for the months in which they occur (no 30th of
February, for example). Using such verification, the programmer may have felt well

FI ICR AC KH
--- page 26 ---
insulated from the possible problems a careless or malicious user could cause.
Guard Against Users’ Fingers

However, the application is still vulnerable. By packing the result into the return URL,
the programmer left these data fields in a place where the user can access (and modify)
them. In particular, the user can edit the URL line, change any parameter values, and send
the revised line. On the server side, the server has no way to tell if the response line came
from the client’s browser or as a result of the user’s editing the URL directly. We say in
this case that the data values are not completely mediated: The sensitive data (namely, the
parameter values) are in an exposed, uncontrolled condition.

Unchecked data values represent a serious potential vulnerability. To demonstrate this
flaw’s security implications, we use a real example; only the name of the vendor has been
changed to protect the guilty. Things, Inc., was a very large, international vendor of
consumer products, called Objects. The company was ready to sell its Objects through a
web site, using what appeared to be a standard e-commerce application. The management
at Things decided to let some of its in-house developers produce a web site with which its
customers could order Objects directly from the web.

To accompany the web site, Things developed a complete price list of its Objects,
including pictures, descriptions, and drop-down menus for size, shape, color, scent, and
any other properties. For example, a customer on the web could choose to buy 20 of part
number 555A Objects. If the price of one such part were $10, the web server would
correctly compute the price of the 20 parts to be $200. Then the customer could decide
whether to have the Objects shipped by boat, by ground transportation, or sent
electronically. If the customer were to choose boat delivery, the customer’s web browser
would complete a form with parameters like these:

Click here to view code image
http://www. things. com/order .asp?cust ID=101&part=555A
&qy=20&price=10&ship=boat&shipcost=5atotal=205
So far, so good; everything in the parameter passing looks correct. But this procedure
leaves the parameter statement open for malicious tampering. Things should not need to
pass the price of the items back to itself as an input parameter. Things presumably knows
how much its Objects cost, and they are unlikely to change dramatically since the time the
price was quoted a few screens earlier.

There is no reason to leave sensitive data under control of an untrusted
user.

A malicious attacker may decide to exploit this peculiarity by supplying instead the
following URL, where the price has been reduced from $205 to $25:
Click} . ici

http://www. things .com/order .asp?cust ID=101par t=555A
&qy=20&price=1&ship=boat&shipcost=Satotal=25

Surprise! It worked. The attacker could have ordered Objects from Things in any
quantity at any price. And yes, this code was running on the web site for a while before

FI ICR 2 6 FAH KK
--- page 27 ---
the problem was detected.

From a security perspective, the most serious concern about this flaw was the length of
time that it could have run undetected. Had the whole world suddenly made a rush to
Things’ web site and bought Objects at a fraction of their actual price, Things probably
would have noticed. But Things is large enough that it would never have detected a few
customers a day choosing prices that were similar to (but smaller than) the real price, say,
30 percent off. The e-commerce division would have shown a slightly smaller profit than
other divisions, but the difference probably would not have been enough to raise anyone’s
eyebrows; the vulnerability could have gone unnoticed for years. Fortunately, Things hired
a consultant to do a routine review of its code, and the consultant quickly found the error.

The vulnerability in this situation is that the customer (computer user) has unmediated
access to sensitive data. An application running on the user’s browser maintained the order
details but allowed the user to change those details at will. In fact, few of these values
should have been exposed in the URL sent from the client’s browser to the server. The
client’s application should have specified part number and quantity, but an application on
the server’s side should have returned the price per unit and total price.

If data can be changed, assume they have been.

This web program design flaw is easy to imagine in other settings. Those of us
interested in security must ask ourselves, How many similar problems are in running code
today? And how will those vulnerabilities ever be found? And if found, by whom?

Complete Mediation

Because the problem here is incomplete mediation, the solution is complete mediation.
Remember from Chapter 2 that one of our standard security tools is access control,
sometimes implemented according to the reference monitor concept. The three properties
of a reference monitor are (1) small and simple enough to give confidence of correctness,
(2) unbypassable, and (3) always invoked. These three properties combine to give us solid,
complete mediation.

Q5 [20]
Co-1

SO- a. Explain authentication. Describe password-based authentication in depth. [10]
BL-

FR ICR D7 FAC KH
--- page 28 ---
Ans.

3.2 PASSWORD-BASED

HENTIC.

ON

A widely used line of defense against intruders is the password system. Virtually all
multiuser systems, network-based servers, Web-based e-commerce sites, and other
similar services require that a user provide not only a name or identifier (ID) but also
a password. The system compares the password to a previously stored password for
that user ID, maintained in a system password file. The password serves to authen-
ticate the ID of the individual logging on to the system. In turn, the ID provides
security in the following ways:

e The ID determines whether the user is authorized to gain access to a system.
In some systems, only those who already have an ID filed on the system are
allowed to gain access.

e The ID determines the privileges accorded to the user. A few users may have
administrator or “superuser” status that enables them to read files and perform
functions that are especially protected by the operating system. Some systems
have guest or anonymous accounts, and users of these accounts have more
limited privileges than others.

¢ The ID is used in what is referred to as discretionary access control. For exam-
ple, by listing the IDs of the other users, a user may grant permission to them
to read files owned by that user.

The Vulnerability of Passwords

In this subsection, we outline the main forms of attack against password-based
authentication and briefly outline a countermeasure strategy. The remainder of
Section 3.2 goes into more detail on the key countermeasures.

Typically, a system that uses password-based authentication maintains a pass-
word file indexed by user ID. One technique that is typically used is to store not the
user’s password but a one-way hash function of the password, as described subsequently.

We can identify the following attack strategies and countermeasures:

© Offline dictionary attack: Typically, strong access controls are used to protect
the system’s password file. However, experience shows that determined hack-
ers can frequently bypass such controls and gain access to the file. The attacker
obtains the system password file and compares the password hashes against

FI ICR 2 QA HH
--- page 29 ---
hashes of commonly used passwords. If a match is found, the attacker can gain
access by that ID/password combination. Countermeasures include controls to
prevent unauthorized access to the password file, intrusion detection measures
to identify a compromise, and rapid reissuance of passwords should the pass-
word file be compromised.

Specific account attack: The attacker targets a specific account and submits
password guesses until the correct password is discovered. The standard coun-
termeasure is an account lockout mechanism, which locks out access to the
account after a number of failed login attempts. Typical practice is no more
than five access attempts.

Popular password attack: A variation of the preceding attack is to use a popu-
lar password and try it against a wide range of user IDs. A user’s tendency is
to choose a password that is easily remembered; this unfortunately makes the
password easy to guess. Countermeasures include policies to inhibit the selec-
tion by users of common passwords and scanning the IP addresses of authenti-
cation requests and client cookies for submission patterns.

Password guessing against single user: The attacker attempts to gain knowl-
edge about the account holder and system password policies and uses that
knowledge to guess the password. Countermeasures include training in and
enforcement of password policies that make passwords difficult to guess. Such
policies address the secrecy, minimum length of the password, character set,
prohibition against using well-known user identifiers, and length of time before
the password must be changed.

Workstation hijacking: The attacker waits until a logged-in workstation is unat-
tended. The standard countermeasure is automatically logging the workstation
out after a period of inactivity. Intrusion detection schemes can be used to
detect changes in user behavior.

Exploiting user mistakes: If the system assigns a password, then the user is
more likely to write it down because it is difficult to remember. This situation
creates the potential for an adversary to read the written password. A user may
intentionally share a password, to enable a colleague to share files, for example.
Also, attackers are frequently successful in obtaining passwords by using social
engineering tactics that trick the user or an account manager into revealing a
password. Many computer systems are shipped with preconfigured passwords
for system administrators. Unless these preconfigured passwords are changed,
they are easily guessed. Countermeasures include user training, intrusion detec-
tion, and simpler passwords combined with another authentication mechanism.

Exploiting multiple password use: Attacks can also become much more effec-
tive or damaging if different network devices share the same or a similar pass-
word for a given user. Countermeasures include a policy that forbids the same
or similar password on particular network devices.

Electronic monitoring: If a password is communicated across a network to log
on to a remote system, it is vulnerable to eavesdropping. Simple encryption will
not fix this problem, because the encrypted password is, in effect, the password
and can be observed and reused by an adversary.

FAR ICR QA HH
--- page 30 ---
CO-3
SO-   b.   Discuss privacy and android cell phones as an example of information flow controls.   [10]
BL-2
Ans.
********** 30 **********

[Text in pictures on this page, read by OCR]
Despite the many security vulnerabilities of passwords, they remain the most
commonly used user authentication technique, and this is unlikely to change in the
foreseeable future [HERL12]. Among the reasons for the persistent popularity of
passwords are the following:

1. Techniques that utilize client-side hardware, such as fingerprint scanners and
smart card readers, require the implementation of the appropriate user authen-
tication software to exploit this hardware on both the client and server systems.
Until there is widespread acceptance on one side, there is reluctance to imple-
ment on the other side, so we end up with a who-goes-first stalemate.

2. Physical tokens, such as smart cards, are expensive and/or inconvenient to carry
around, especially if multiple tokens are needed.

3. Schemes that rely on a single sign-on to multiple services, using one of the non-
password techniques described in this chapter, create a single point of security risk.

4, Automated password managers that relieve users of the burden of knowing and
entering passwords have poor support for roaming and synchronization across
multiple client platforms, and their usability had not be adequately researched.

Thus, it is worth our while to study the use of passwords for user authentication
in some detail.

17.6 Example Information Flow Controls

Like the program-based information flow mechanisms discussed in this chapter,
both special-purpose and general-purpose computer systems have information
flow controls at the system level. File access controls, integrity controls, and
other types of access controls are mechanisms that attempt to inhibit the flow
of information within a system, or between systems.

The first example follows a line of research that examines privacy in
information flow on cell phones. The second example describes firewalls, which
act to control information flow between (or among) networks.
--- page 31 ---
17.6.1. Privacy and Android Cell Phones

Cell phones are becoming ubiquitous and more powerful. Users can augment the
usual telephone functionality with millions of commercial and free applications
(apps) available for all brands. Many of the free apps use advertising libraries to
fetch advertising content, monitor clicks, and display the advertisements using the
WebView subsystem. Other products offer information or services or tailor their
in-app advertising to the habits, locations, and other personal characteristics of
the user.

Because of the complexity of the permissions structure of cell phones, apps
often are given permission to access all data and resources on the cell phone.
Further, the advertising (and other) libraries are part of the app, so they have
the same privilege. Thus, any web page downloaded and displayed will execute
any Javascript (or other) code with the privileges of the app. This violates the
principle of least privilege. It also means that the app can use the resources of
the phone to gather information it does not need, and send that information to
unknown parties. This puts the privacy of the user at risk, and possibly others
whose data is stored on the phone [284, 1397].

This is an information flow problem, because the confidential information
in the phone is flowing to an untrusted destination. Thus, tools have been
developed to analyze the flow of information in apps. Here, we focus on the
Android operating system because it has been extensively studied and is widely
used on a variety of cell phones.

Android is based on the Linux system. The executables are in a bytecode
format called Dalvik executables (DEX). The apps are event driven, and use
system libraries to carry out much of their functionality; for example, a native
OpenGL library manages the graphics and another, Webkit, handles web brows-
ing. These libraries are considered part of the underlying Android system and so
are considered trusted. Each app executes within a virtual machine, the Dalvik
VM interpreter. A subsystem called Binder controls interprocess communication,
which is communication between the Dalvik VMs of the processes.

The analysis uses a two-level security model. The higher level is called
untainted (U) and the lower level, tainted (T). This model has no security cate-
gories, so the levels form a linear ordering, with U > T. It is effectively a two-level
version of the Bell-LaPadula Model.

TaintDroid [634, 635] is an example of a dynamic Android information
flow analysis tool. It considers Android native libraries as trusted; those that
communicate information externally, such as a library that sends a message, are
also designated as taint sinks. Objects are tagged as U or T and the tags are
propagated throughout the execution of the app. The interpreters are augmented
to handle the tags. When an app communicates with another app, for example
by accessing shared objects, the tag is also communicated; so Binder also is
augmented to handle tags. When an untrusted app invokes a library that is a taint
sink, the taint tag of the data being sent is recorded.

FR ICR QI OH
--- page 32 ---
The bytecode defines several operations, and the tags are modified accord-
ing to the information flow rules described in section 17.3. To handle native
libraries, TaintDroid assigns taint tags to the external variables that the native
code accesses; it also assigns a taint tag to the returned value. The value assigned
depends upon knowledge of what the native code does; this is determined in a
variety of ways, including heuristics.

The interprocess communication mechanism sends messages composed of
one or more variables. Keeping track of the taint tags requires a trade-off between
precision and performance. If the entire message has one tag, the variables tagged
U will be subsumed and when the message is received it will have a T tag. But if
each byte in the message has its own tag, the performance suffers by a factor of
approximately 2. TaintDroid compromises by grouping tags of variables with the
same tag into a structure with a starting address and a size. Thus, two variables
that are adjacent in the message take up a single entry in the structure.

Files have a single taint tag that is updated when the file is written and
propagated into the appropriate variables when the file is read. As with interpro-
cess communication, this can lead to imprecision, but saves on memory usage
and minimizes performance impact. On the other hand, Android databases are
queried, and so the information retrieved can have taint values assigned based
on the database query responder. So the databases are not assigned a single taint
value.

Finally, the information obtained from the cell phone’s sensors may be
sensitive, and if so should be tagged as T. TaintDroid determines these tags
based on characteristics of the information. For example, data obtained from the
microphone or camera would be considered privacy sensitive, and hence tagged
T, as would the phone number and various cell phone and device identifiers.

Enck and his colleagues conducted two studies to determine the effective-
ness of TaintDroid. The first study [634], conducted in 2010, selected 30 popular
apps out of a set of 358 apps that required permission to access the Internet,
and any of the cell phone location, camera, or microphone. The apps could
also access cell phone information. In this set of apps, TaintDroid flagged 105
network connections as accessing data labeled T. Two of them sent cell phone
identification information such as the phone number to a server; of the nine that
sent device identifiers, two did not notify the user that they would do so. Fifteen
apps sent location information to third parties, and none indicated they would do
so. TaintDroid correctly identified all these messages. It had no false positives.

Two years later, the researchers revisited the 30 apps [635]. Only 18 of them
ran on the current version of Android, and of those 18, only 3 apps still sent
location information to third parties. However, 8 exposed device identification
information (3 that did so in 2010, and 5 new ones) without consent. They also
found two new flows that could reveal tainted information, because of the changes
they made to TaintDroid. Again, no false positives were observed.

Other dynamic analysis tools provide mechanisms for app creators to
constrain information flow. For example, DroidDisintegrator [1892] extends the

FIR ICR QD I HH
--- page 33 ---
techniques used in TaintDroid to enable app developers to do this. Jia et al. [967]
implement information flow constraints that allow multiple security and integrity
compartments.

Like other dynamic information flow analysis tools, TaintDroid detects
flows that occur during execution, so if a different set of inputs and conditions
would cause the apps to take a different execution path, those information flows
will not be examined unless they also occur in the current execution. Static
information flow analysis tools such as AndroidLeaks [766], Amandroid [1987],
FlowDroid [84], Epicc [1468], and CHEX [1212] implement the information flow
rules in Section 17.3, but each in a different way. All suffer from the limitations of
static analysis in being overly conservative.

AppAudit [2033] seeks to have the best of both static and dynamic analysis
by combining them. It examines the code statically. It looks for a potential path
from a source API that accesses sensitive information and a sink API that sends
data out of the device. If there is a path from a function to a source API and
a sink API, that function is labeled as suspicious. Complicating the detection of
suspicious functions are the callback functions that notify a listener that some
event occurred (such as a computation completing). As many trigger APIs may
register callback functions, the static analyzer cannot determine which callback
function will be heard. So, AppAudit treats those functions that call a trigger
API as invoking all possible callback functions of the registered type. This can
result in identifying potential flows that will never be realized, so AppAudit then
dynamically executes suspicious functions to determine if sensitive data could be
leaked. In tests, AppAudit reported no information flow paths that could not be
taken, and the information flow paths it missed depended on the contents of a
text message.

Q6 [20]
Co-1

SO- a. Explain DAC access control model and techniques to implement it. [10]
BL-2

FR ICR QQ I OH
--- page 34 ---
Ans.

Access Control Directory

One simple way to protect an object is to use a mechanism that works like a file
directory. Imagine we are trying to protect files (the set of objects) from users of a
computing system (the set of subjects). Every file has a unique owner who possesses
“control” access rights (including the rights to declare who has what access) and to revoke
access of any person at any time. Each user has a file directory, which lists all the files to
which that user has access.

Clearly, no user can be allowed to write in the file directory, because that would be a
way to forge access to a file. Therefore, the operating system must maintain all file
directories, under commands from the owners of files. The obvious rights to files are the
common read, write, and execute that are familiar on many shared systems. Furthermore,
another right, owner, is possessed by the owner, permitting that user to grant and revoke
access rights. Figure 2-9 shows an example of a file directory.

User A Directory Files User B Directory

” Access _ File Access _ Fi

FileName Rights Pointer FileName __Rights Pointe
PROGI.C ORW BIBLIOG R e
PROGILEXE | OX Liat TEST-TMP ox |
HELPTXT =| R «| —™ HELPTXT =|R e
HEMP ORW

FIGURE 2-9 Directory Access Rights

This approach is easy to implement because it uses one list per user, naming all the

FIR ICR I HOH
--- page 35 ---
objects that a user is allowed to access. However, several difficulties can arise. First, the
list becomes too large if many shared objects, such as libraries of subprograms or a
common table of users, are accessible to all users. The directory of each user must have
one entry for each such shared object, even if the user has no intention of accessing the
object. Deletion must be reflected in all directories.

A second difficulty is revocation of access. If owner A has passed to user B the right to
read file F, an entry for F is made in the directory for B. This granting of access implies a
level of trust between A and B. If A later questions that trust, A may want to revoke the
access right of B. The operating system can respond easily to the single request to delete
the right of B to access F, because that action involves deleting one entry from a specific
directory. But if A wants to remove the rights of everyone to access F, the operating
system must search each individual directory for the entry F, an activity that can be time
consuming on a large system. For example, large systems or networks of smaller systems
can easily have 5,000 to 10,000 active accounts. Moreover, B may have passed the access
right for F to another user C, a situation known as propagation of access rights, so A may
not know that C’s access exists and should be revoked. This problem is particularly
serious in a network.

A third difficulty involves pseudonyms. Owners A and B may have two different files
named F, and they may both want to allow access by S. Clearly, the directory for S cannot
contain two entries under the same name for different files. Therefore, S has to be able to
uniquely identify the F for A (or B). One approach is to include the original owner’s
designation as if it were part of the file name, with a notation such as A:F (or B:F).

Suppose, however, that S would like to use a name other than F to make the file’s
contents more apparent. The system could allow S to name F with any name unique to the
directory of S. Then, F from A could be called Q to S. As shown in Figure 2-10, S may
have forgotten that Q is F from A, and so S requests access again from A for F. But by
now A may have more trust in S, so A transfers F with greater rights than before. This
action opens up the possibility that one subject, S, may have two distinct sets of access
rights to F, one under the name Q and one under the name F. In this way, allowing
pseudonyms can lead to multiple permissions that are not necessarily consistent. Thus, the
directory approach is probably too simple for most object protection situations.

--- page 36 ---
User A Directory Files Directory

nie Access File ais
File Name Rights Pointer <--
F ORWX| ©
BIBLIOG = |ORW FE rw | ef!


HELPTXT = |R Coa HELPTXT |R «
PROGL.EXE |OX ‘Ne |
User B Directory

“ Access _ File
FileName Rights Pointer

HELP-TXT R °
TEMP ORW |

FIGURE 2-10 Ambiguous Access Rights

Access Control Matrix

We can think of the directory as a listing of objects accessible by a single subject, and
the access list as a table identifying subjects that can access a single object. The data in
these two representations are equivalent, the distinction being the ease of use in given
situations.

As an alternative, we can use an access control matrix, shown in Figure 2-11, a table in
which each row represents a subject, each column represents an object, and each entry is
the set of access rights for that subject to that object.

7 objects =
File A Printer System
Clock
Read
2g User W Write Write Read
x Own
3 ‘
a Admin Waite Control
Control

FIGURE 2-11 Access Control Matrix

A more detailed example representation of an access control matrix is shown in Table 2-
8. Access rights shown in that table are O, own; R, read; W, write; and X, execute. In
general, the access control matrix is sparse (meaning that most cells are empty): Most
subjects do not have access rights to most objects. The access matrix can be represented as

FR ICR RG IC HH
--- page 37 ---
a list of triples, each having the form Seubject, object, rights), as shown in Table 2-9.

Help (cm
Bibliog | Temp F txt Comp | Linker | Clock | Printer
USER B R - a R x x R Ww
USERS RW - R R x x R Ww
USER T — - R x x x R w
SYS MGR - - - RW Ox Ox ORW oO
USER SVCS | — _ - fe) x x R w

TABLE 2-8 Access Control Matrix

Subject Object Right
USER A Bibliog ORW
USER B Bibliog R
USER S Bibliog RW
USER A Temp ORW
USERA PF ORW
USER S R R

etc.

TABLE 2-9 List of Access Control Triples
This representation may be more efficient than the access control matrix because there

is no triple for any empty cell of the matrix (such as (usER T, Bibliog, -), Even though
the triples can be sorted by subject or object as needed, searching a large number of these
triples is inefficient enough that this implementation is seldom used.

Access Control List

An alternative representation is the access control list; as shown in Figure 2-12, this
representation corresponds to columns of the access control matrix. There is one such list
for each object, and the list shows all subjects who should have access to the object and
what their access is. This approach differs from the directory list because there is one
access control list per object; a directory is created for each subject. Although this
difference seems small, there are some significant advantages to this approach.

FR ICR QA OH
--- page 38 ---
File A Printer Systeat

Clock
Read
User W Write Write Read
Own
Admin Write Control
Control

FIGURE 2-12 Access Control List

The access control list representation can include default rights. Consider subjects A
and S, both of whom have access to object F. The operating system will maintain just one
access list for F, showing the access rights for A and S, as shown in Figure 2-13. The
access control list can include general default entries for any users. In this way, specific
users can have explicit rights, and all other users can have a default set of rights. With this
organization, all possible users of the system can share a public file or program without
the need for an entry for the object in the individual directory of each user.

Directory Access Lists Files
File “Star Lawl Rights BIBLIOG
BIBLIOG a   USER_A ORW
TEMP i USERB | R
2 users | RW —_—
ueterst | useR.A | ORW
F
USER_A ORW
users | R
USER_A R HELPTXT
USER_B R
USER_S R
USER_T R
SYSMGR | RW

USER_SVCS | O

FIGURE 2-13 Access Control List with Two Subjects

FIR ICR QA HH
--- page 39 ---
The Multics operating system used a form of access control list in which each user
belonged to three protection classes: a user, a group, and a compartment. The user
designation identified a specific subject, and the group designation brought together
subjects who had a common interest, such as their being coworkers on a project. The
compartment confined an untrusted object; a program executing in one compartment could
not access objects in another compartment without specific permission. The compartment
was also a way to collect objects that were related, such as all files for a single project.

To see how this type of protection might work, suppose every user who initiates access
to the system identifies a group and a compartment with which to work. If Adams logs in
as user Adams in group Decl and compartment Art2, only objects having Adams-Decl-
Art2 in the access control list are accessible in the session.

By itself, this kind of mechanism would be too restrictive to be usable. Adams cannot
create general files to be used in any session. Worse yet, shared objects would not only
have to list Adams as a legitimate subject but also have to list Adams under all acceptable
groups and all acceptable compartments for each group.

The solution is the use of wild cards, meaning placeholders that designate “any user”
(or “any group” or “any compartment”). An access control list might specify access by
Adams-Decl-Artl, giving specific rights to Adams if working in group Decl on
compartment Artl. The list might also specify Adams-*-Artl, meaning that Adams can
access the object from any group in compartment Artl. Likewise, a notation of *-Decl-*
would mean “any user in group Decl in any compartment.” Different placements of the
wildcard notation * have the obvious interpretations.

Unix uses a similar approach with user-group-world permissions. Every user belongs
to a group of related users—students in a common class, workers on a shared project, or
members of the same department. The access permissions for each object are a triple
(u,g,w) in which u is for the access rights of the user, g is for other members of the group,
and w is for all other users in the world.

The access control list can be maintained in sorted order, with * sorted as coming after
all specific names. For example, Adams-Decl-* would come after all specific
compartment designations for Adams. The search for access permission continues just
until the first match. In the protocol, all explicit designations are checked before wild
cards in any position, so a specific access right would take precedence over a wildcard
right. The last entry on an access list could be *-*-*, specifying rights allowable to any
user not explicitly on the access list. With this wildcard device, a shared public object can
have a very short access list, explicitly naming the few subjects that should have access
rights different from the default.

Co-4

SO- b. Discuss the security requirements of databases. [10]

BL-3

7.2 Security Requirements of Databases

The basic security requirements of database systems are not unlike those of other
computing systems we have studied. The basic problems—access control, exclusion of
spurious data, authentication of users, and reliability—have appeared in many contexts so
far in this book. Following is a list of requirements for database security.

+ Physical database integrity. The data of a database are immune from physical
Ans. problems, such as power failures, and someone can reconstruct the database if it

is destroyed through a catastrophe.

+ Logical database integrity. The structure of the database is preserved. With

logical integrity of a database, a modification to the value of one field does not

affect other fields, for example.

+ Element integrity. The data contained in each element are accurate.

+ Auditability. It is possible to track who or what has accessed (or modified) the

FIR ICR QQ FAR RH
--- page 40 ---
elements in the database.

+ Access control. A user is allowed to access only authorized data, and different
users can be restricted to different modes of access (such as read or write).

+ User authentication. Every user is positively identified, both for the audit trail
and for permission to access certain data.

+ Availability. Users can access the database in general and all the data for which
they are authorized.

We briefly examine each of these requirements.
Integrity of the Database

If a database is to serve as a central repository of data, users must be able to trust the
accuracy of the data values. This condition implies that the database administrator must be
assured that updates are performed only by authorized individuals. It also implies that the
data must be protected from corruption, either by an outside illegal program action or by
an outside force such as fire or a power failure. Two situations can affect the integrity of a
database: when the whole database is damaged (as happens, for example, if its storage
medium is damaged) or when individual data items are unreadable.

Integrity of the database as a whole is the responsibility of the DBMS, the operating
system, and the (human) computing system manager. From the perspective of the
operating system and the computing system manager, databases and DBMSs are files and
programs, respectively. Therefore, one way of protecting the database as a whole is to
regularly back up all files on the system. These periodic backups can be adequate controls
against catastrophic failure.

Sometimes an administrator needs to be able to reconstruct the database at the point of a
failure. For instance, when the power fails suddenly, a bank’s clients may be in the middle
of making transactions or students may be registering online for their classes. In these
cases, owners want to be able to restore the systems to a stable point without forcing users
to redo their recently completed transactions.

To handle these situations, the DBMS must maintain a log of transactions. For example,
suppose the banking system is designed so that a message is generated in a log (electronic
or paper or both) each time a transaction is processed. In the event of a system failure, the
system can obtain accurate account balances by reverting to a backup copy of the database
and reprocessing all later transactions from the log.

Element Integrity

The integrity of database elements is their correctness or accuracy. Ultimately,
authorized users are responsible for entering correct data in databases. However, users and
programs make mistakes collecting data, computing results, and entering values.
Therefore, DBMSs sometimes take special action to help catch errors as they are made
and to correct errors after they are inserted.

Databases achieve integrity of the database, its structure, and its
individual elements.

FRR ICR 71) AH OH
--- page 41 ---
This corrective action can be taken in three ways: by field checks, through access
control, and with change log.

First, the DBMS can apply field checks, activities that test for appropriate values in a
position. A field might be required to be numeric, an uppercase letter, or one of a set of
acceptable characters. The check ensures that a value falls within specified bounds or is
not greater than the sum of the values in two other fields. These checks prevent simple
errors as the data are entered. (Sidebar 7-1 demonstrates the importance of element
integrity.)

Sidebar 7-1 Element Integrity Failure Crashes Network
Crocker and Bernstein [CRO89] studied catastrophic failures of what was then
known as the ARPANET, the predecessor of today’s Internet. Several failures
came from problems with the routing tables used to direct traffic through the
network.

A 1971 error was called the “black hole.” A hardware failure caused one node
to declare that it was the best path to every other node in the network. This node
sent this declaration to other nodes, which soon propagated the erroneous
posting throughout the network. This node immediately became the black hole
of the network because all traffic was routed to it but never made it to the real
destination.

The ARPANET used simple tables, not a full-featured database management
system, so there was no checking of new values before they were installed in the
distributed routing tables. Had there been a database, integrity-checking
software could have checked for errors in the newly distributed values and
raised a flag for human review.

A second integrity action is afforded by access control. To see why, consider life
without databases. Data files may contain data from several sources, and redundant data
may be stored in several different places. For example, a student’s mailing address may be
stored in many different campus files: in the registrar’s office for formal correspondence,
in the food service office for dining hall privileges, at the bookstore for purchases, and in
the financial aid office for accounting. Indeed, the student may not even be aware that
each separate office has the address on file. If the student moves from one residence to
another, each of the separate files requires correction.

Without a database, you can imagine the risks to the data’s integrity. First, at a given
time, some data files could show the old address (they have not yet been updated) and
some simultaneously have the new address (they have already been updated). Second,
there is always the possibility that someone misentered a data field, again leading to files
with incorrect information. Third, the student may not even be aware of some files, so he
or she does not know to notify the file owner about updating the address information.
These problems are solved by databases. They enable collection and control of this data at
one central source, ensuring the student and users of having the correct address.

However, the centralization is easier said than done. Who owns this shared central file?
Who is authorized to update which elements? What if two people apply conflicting

FIR IC 77 FIC HOH
--- page 42 ---
modifications? What if modifications are applied out of sequence? How are duplicate
records detected? What action is taken when duplicates are found? These are policy
questions that must be resolved by the database administrator. Sidebar 7-2 describes how
these issues are addressed for managing the configuration of programs; similar formal
processes are needed for managing changes in databases.

Sidebar 7-2 Configuration Management and Access Control

Software engineers must address access control when they manage the
configurations of large computer systems. The code of a major system and
changes to the code over time are actually a database. In many instances
multiple programmers make changes to a system at the same time; the
configuration management database must help ensure that the correct and most
recent changes are stored.

The proliferation of versions and releases can be controlled in three primary
ways. [PFL10a]

+ Separate files: A separate file can be kept for each different version or
release. For instance, version 1 may exist for machines that store all data in
main memory, and version 2 is for machines that must put some data out to
a disk. Suppose the common functions are the same in both versions,
residing in components C, through C,, but memory management is done by
component M, for version 1 and M, for version 2. If new functionality is to
be added to the memory management routines, keeping both versions
current and correct may be difficult; the results must be the same from the
user’s point of view.

+ Deltas: One version of the system is deemed the main version, and all
other versions are considered to be variations from the main version. The
database keeps track only of the differences, in a file called a delta file. The
delta contains commands that are “applied” to the main version to
transform it into the alternative version. This approach saves storage space
but can become unwieldy.

* Conditional compilation: All versions are handled by a single file, and
conditional statements are used to determine which statements apply under
which conditions. In this case, shared code appears only once, so only one
correction is needed if a problem is found. But the code in this single file
can be very complex and difficult to maintain.

In any of these three cases, controlled access to the configuration files is
critical. Two programmers fixing different problems sometimes need to make
changes to the same component. If they do not coordinate access, the second
programmer can inadvertently undo (or worse, wreck) the changes of the first
programmer, resulting in not only recurrence of the initial problems but also
introduction of additional problems. For this reason, files are controlled in
several ways, including being locked while changes are made by one
programmer, and being subject to a group of people called a configuration
control board who ensure that no changed file is put back into production

FIR ICR 7 AC HOEK
--- page 43 ---
without the proper checking and testing. Shari Lawrence Pfleeger and Joanne
Atlee write about these techniques [PFL10a].

The third means of providing database integrity is maintaining a change log for the
database. A change log lists every change made to the database; it contains both original
and modified values. Using this log, a database administrator can undo any changes that
were made in error. For example, a library fine might erroneously be posted against
Charles W. Robertson, instead of Charles M. Robertson, flagging Charles W. Robertson as
ineligible to participate in varsity athletics. Upon discovering this error, the database
administrator obtains Charles W.’s original eligibility value from the log and corrects the
database.

Auditability

For some applications administrators may want to generate an audit record of all access
(read or write) to a database. Such a record can help to maintain the database’s integrity, or
at least to discover after the fact who had affected what values and when. A second
advantage, as we see later, is that users can access protected data incrementally; that is, no
single access reveals protected data, but a set of sequential accesses viewed together
reveals the data, much like discovering the clues in a detective novel. In this case, an audit
trail can identify which clues a user has already been given, as a guide to whether to tell
the user more.

As we note in Chapter 2, granularity can become an impediment in auditing. Audited
events in operating systems are actions like open file or call procedure; they are seldom as
specific as write record 3 or execute instruction I. To be useful for maintaining integrity,
database audit trails should include accesses at the record, field, and even element levels.
This detail is prohibitive for most database applications.

Furthermore, the database management system may access a record but not report the
data to a user, as when the user performs a select operation. For example, a residence hall
advisor might want a count of all students who have failed elementary French, and the
database management system reports 462. To get that number the system had to inspect all
student records and note those with failing grades, and it performed this lookup on behalf
of the advisor who is appropriately listed in the log as receiving the data. Thus, in a sense,
the advisor accessed all those student grades, although from the number 462 the advisor
cannot determine the grade of any individual student. (Accessing a record or an element
without transferring to the user the data received is called the pass-through problem.)
Thus, a log of all records accessed directly may both overstate and understate what a user
actually learns. The problem is even more nuanced than what we describe here, and we
consider some intricacies of disclosure later in this chapter.

Access Control

Databases are often separated logically by user access privileges. For example, all users
can be granted access to general data, but only the personnel department can obtain salary
data and only the marketing department can obtain sales data. Databases are useful
because they centralize the storage and maintenance of data. Limited access is both a
responsibility and a benefit of this centralization.

FIR ICR 72 FIC HOH
--- page 44 ---
The database administrator specifies who should be allowed access to which data, at the
view, relation, field, record, or even element level. The DBMS must enforce this policy,
granting access to all specified data or no access where prohibited. Furthermore, the
number of modes of access can be many. A user or program may have the right to read,
change, delete, or append to a value, add or delete entire fields or records, or reorganize
the entire database.

Superficially, access control for a database seems like access control for an operating
system or any other component of a computing system. However, the database problem is
more complicated, as we see throughout this chapter. Operating system objects, such as
files, are unrelated items, whereas records, fields, and elements are related. Although a
user probably cannot determine the contents of one file by reading others, a user might be
able to determine one data element just by reading others. The problem of obtaining data
values from others is called inference, and we consider it in depth later in this chapter.

It is important to notice that you can access data by inference without needing direct
access to the secure object itself. Restricting inference may mean prohibiting certain paths
to prevent possible inferences. However, restricting access to control inference also limits
queries from users who do not intend unauthorized access to values. Moreover, attempts to
check requested accesses for possible unacceptable inferences may actually degrade the
DBMS’s performance.

Finally, size or granularity is different between operating system objects and database
objects. An operating system can readily control access to files, as we explain in Chapter
5. However an access control list of several hundred files is much easier to implement
than an access control list for a database with several hundred files of perhaps a hundred
fields each. Size affects the efficiency of processing. Operating systems do not usually
“see into” a file to control access to items within a file.

Database management systems implement their own access control at a
level finer than what an operating system handles.

User Authentication

The DBMS can require rigorous user authentication. For example, a DBMS might insist
that a user pass both specific password and time-of-day checks. This authentication
supplements the authentication performed by the operating system. Typically, the DBMS
runs as an application program on top of the operating system. This system design means
that there is no trusted path from the DBMS to the operating system, so the DBMS must
be suspicious of any data it receives, including a user identity from the operating system.
Thus, the DBMS is forced to do its own authentication.

Availability

A DBMS has aspects of both a program and a system. It is a program that uses other
hardware and software resources, yet to many users it is the only application run. Users
often take the DBMS for granted, employing it as an essential tool with which to perform

particular tasks. But when the system is not available—busy serving other users or down
to be repaired or upgraded—the users are very aware of a DBMS’s unavailability. For

FIR ICR 7) I ROK HH
--- page 45 ---
Q7   [20]
CO-1   Write short note on the following.
SO-   a.   1. Threats   [10]
2. Policy and Mechanism
BL-2   3. Assumption and Trust
Ans.
********** 45 **********

[Text in pictures on this page, read by OCR]
example, two users may request the same record, and the DBMS must arbitrate; one user
is bound to be denied access for a while. Or the DBMS may withhold unprotected data to
avoid revealing protected data, leaving the requesting user unhappy. We examine these
problems in more detail later in this chapter. Problems like these result in high availability
requirements for a DBMS.

Integrity/Confidentiality/Availability

The three aspects of computer security—integrity, confidentiality, and availability—
clearly relate to database management systems. As we have described, integrity applies to
the individual elements of a database as well as to the database as a whole. Integrity is also
a property of the structure of the database (elements in one table correspond one to one
with those of another) and of the relationships of the database (records having the same
unique identifier, called a key, are related). Thus, integrity is a major concern in the design
of database management systems. We look more closely at integrity issues in the next
section.

Confidentiality is likewise a key issue with databases because databases are often used
to implement controlled sharing of sensitive data. Access to data can be direct (you
request a record and the database provides it) or indirect (you request some records and
from those results infer or intuit other data). Controlling direct access employs the access
control techniques we describe in Chapters 2 and 5. Indirect access, however, is more
difficult to control, and we explore it in more depth later in this chapter.

Finally, availability is important because of the shared access motivation underlying
database development. However, availability conflicts with confidentiality. The last
sections of the chapter address availability in an environment in which confidentiality is
also important.
--- page 46 ---
actions that could cause it to occur must be guarded against (or prepared for).
Those actions are called attacks. Those who execute such actions, or cause them
to be executed, are called attackers.

The three security services—confidentiality, integrity, and availability—
counter threats to the security of a system. Shirey [1739] divides threats into
four broad classes: disclosure, or unauthorized access to information; deception,
or acceptance of false data; disruption, or interruption or prevention of correct
operation; and usurpation, or unauthorized control of some part of a system.
These four broad classes encompass many common threats. Because the threats
are ubiquitous, an introductory discussion of each one will present issues that
recur throughout the study of computer security.

Snooping or eavesdropping, the unauthorized interception of information,
is a form of disclosure. It is passive, suggesting simply that some entity is listening
to (or reading) communications or browsing through files or system information.
Passive wiretapping is a form of snooping in which a network is monitored. (It is
called “wiretapping” because of the “wires” that compose the network, although
the term is used even if no physical wiring is involved.) Confidentiality services
seek to counter this threat.

Modification or alteration, an unauthorized change of information, covers
three classes of threats. The goal may be deception, in which some entity relies
on the modified data to determine which action to take, or in which incorrect
information is accepted as correct and is released. If the modified data controls
the operation of the system, the threats of disruption and usurpation arise. Unlike
snooping, modification is active; it results from an entity changing information.
Active wiretapping is a form of modification in which data moving across a
network is altered, new data is injected, or parts of the data are deleted; the term
“active” distinguishes it from snooping (“passive” wiretapping). An example is the
man-in-the-middle attack, in which an intruder reads messages from the sender and
sends (possibly modified) versions to the recipient, in hopes that the recipient and
sender will not realize the presence of the intermediary. Integrity services seek to
counter this threat.

Masquerading or spoofing, an impersonation of one entity by another, is
a form of both deception and usurpation. It lures a victim into believing that
the entity with which it is communicating is a different entity. For example, if a
user tries to log into a computer across the Internet but instead reaches another
computer that claims to be the desired one, the user has been spoofed. Similarly,
if a user tries to read a web page, but an attacker has arranged for the user to
be given a different page, another spoof has taken place. This may be a passive
attack (in which the user simply accesses the web page), but it is usually an active
attack (in which the attacker issues responses dynamically to mislead the user
about the web page). Although masquerading is primarily deception, it is often
used to usurp control of a system by an attacker impersonating an authorized
manager or controller. Integrity services (called “authentication services” in this
context) seek to counter this threat.

Some forms of masquerading may be allowed. Delegation occurs when one
entity authorizes a second entity to perform functions on its behalf. The distinc-
tions between delegation and masquerading are important. If Susan delegates to

FIR ICR 7] 6 AC HOH
--- page 47 ---
Thomas the authority to act on her behalf, she is giving permission for him to
perform specific actions as though she were performing them herself. All parties
are aware of the delegation. Thomas will not pretend to be Susan; rather, he will
say, “I am Thomas and I have authority to do this on Susan’s behalf.” If asked,
Susan will verify this. On the other hand, in a masquerade, Thomas will pretend to
be Susan. No other parties (including Susan) will be aware of the masquerade, and
Thomas will say, “I am Susan.” Should anyone discover that he or she is dealing
with Thomas and ask Susan about it, she will deny that she authorized Thomas to
act on her behalf. Even though masquerading is a violation of security, delegation
is not.

Repudiation of origin, a false denial that an entity sent (or created) some-
thing, is a form of deception. For example, suppose a customer sends a letter to a
vendor agreeing to pay a large amount of money for a product. The vendor ships
the product and then demands payment. The customer denies having ordered the
product and, according to a law in the customer’s state, is therefore entitled to
keep the unsolicited shipment without payment. The customer has repudiated
the origin of the letter. If the vendor cannot prove that the letter came from the
customer, the attack succeeds. A variant of this is denial by a user that he created
specific information or entities such as files. Integrity mechanisms try to cope with
this threat.

Denial of receipt, a false denial that an entity received some information
or message, is a form of deception. Suppose a customer orders an expensive
product, but the vendor demands payment before shipment. The customer pays,
and the vendor ships the product. The customer then asks the vendor when he will
receive the product. If the customer has already received the product, the question
constitutes a denial of receipt attack. The vendor can defend against this attack
only by proving that the customer did, despite his denials, receive the product.
Integrity and availability mechanisms attempt to guard against these attacks.

Delay, a temporary inhibition of a service, is a form of usurpation, although
itcan play a supporting role in deception. Typically, delivery of a message or service
requires some time ¢; if an attacker can force the delivery to take more than time
t, the attacker has successfully delayed delivery. This requires manipulation of
system control structures, such as network components or server components, and
hence is a form of usurpation. If an entity is waiting for an authorization message
that is delayed, it may query a secondary server for the authorization. Even though
the attacker may be unable to masquerade as the primary server, she might be
able to masquerade as that secondary server and supply incorrect information.
Availability mechanisms can often thwart this threat.

Denial of service, a long-term inhibition of service, is a form of usurpation,
although it is often used with other mechanisms to deceive. The attacker prevents a
server from providing a service. The denial may occur at the source (by preventing
the server from obtaining the resources needed to perform its function), at the
destination (by blocking the communications from the server), or along the
intermediate path (by discarding messages from either the client or the server,
or both). Denial of service poses the same threat as an infinite delay. Availability
mechanisms seek to counter this threat.

FRR IC 7 IC ROKK
--- page 48 ---
Denial of service or delay may result from direct attacks or from problems
unrelated to security. From our point of view, the cause and result are important;
the intention underlying them is not. If delay or denial of service compromises
system security, or is part of a sequence of events leading to the compromise
of a system, then we view it as an attempt to breach system security. But the
attempt may not be deliberate; indeed, it may be a user error, or the product of
environmental characteristics, rather than specific actions of an attacker.

1.3. Policy and Mechanism

Critical to our study of security is the distinction between policy and mechanism:

Definition 1-1. A security policy is a statement of what is, and what is not,
allowed.

Definition 1-2. A security mechanism is a method, tool, or procedure for
enforcing a security policy.

Mechanisms can be nontechnical, such as requiring proof of identity before
changing a password; in fact, policies often require some procedural mechanisms
that technology cannot enforce.

As an example, suppose a university’s computer science laboratory has a
policy that prohibits any student from copying another student’s homework files.
The computer system provides mechanisms for preventing others from reading a
user’s files. Anna fails to use these mechanisms to protect her homework files, and
Bill copies them. A breach of security has occurred, because Bill has violated the
security policy. Anna’s failure to protect her files does not authorize Bill to copy
them.

In this example, Anna could easily have protected her files. In other environ-
ments, such protection may not be easy. For example, the Internet provides only
the most rudimentary security mechanisms, which are not adequate to protect
information sent over that network. Nevertheless, acts such as the recording
of passwords and other sensitive information violate an implicit security policy
of most sites (specifically, that passwords are a user’s confidential property and
cannot be recorded by anyone).

Policies may be presented mathematically, as a list of allowed (secure) and
disallowed (nonsecure) states. For our purposes, we will assume that any given
policy provides an axiomatic description of secure states and nonsecure states. In
practice, policies are rarely so precise; they normally describe in English, or some
other natural language, what users and staff are allowed to do. The ambiguity
inherent in such a description leads to states that are not classified as “allowed”
or “disallowed.” For example, consider the homework policy discussed previously.
If someone looks through another user’s directory without copying homework

files, is that a violation of security? The answer depends on site custom, rules,
regulations, and laws, all of which are outside our focus and may change over
time.

When two different sites communicate or cooperate, the entity they com-
pose has a security policy based on the security policies of the two entities. If those
policies are inconsistent, either or both sites must decide what the security policy
for the combined site should be. The inconsistency often manifests itself as a
security breach. For example, if proprietary documents were given to a university,
the policy of confidentiality in the corporation would conflict with the more open
policies of most universities. The university and the company must develop a
mutual security policy that meets both their needs in order to produce a consistent
policy. When the two sites communicate through an independent third party, such
as an Internet service provider, the complexity of the situation grows rapidly.

Co-4

SO- b. Write short note on confidentiality policy and discuss Bell-LaPaduala Model. [10]

BL-2

--- page 49 ---
5.1. Goals of Confidentiality Policies

A confidentiality policy, also called an information flow policy, prevents the
unauthorized disclosure of information. Unauthorized alteration of information
is secondary. For example, the navy must keep confidential the date on which
a troop ship will sail. If the date is changed, the redundancy in the systems
and paperwork should catch that change. But if the enemy knows the date of

Ans. sailing, the ship could be sunk. Because of extensive redundancy in military
communications channels, availability is also less of a problem.

The term “governmental” covers several requirements that protect citizens’
privacy. In the United States, the Privacy Act requires that certain personal data
be kept confidential. Income tax returns are legally confidential and are available
only to the Internal Revenue Service or to legal authorities with a court order. The
principle of “executive privilege” and the system of nonmilitary classifications
suggest that the people working in the government need to limit the distribution of
certain documents and information. Governmental models represent the policies
that satisfy these requirements.

FRI ICR 7. AC OH
--- page 50 ---
5.2 The Bell-LaPadula Model

The Bell-LaPadula Model [149, 150] corresponds to military-style classifications.
It has influenced the development of many other models and indeed much of the
development of computer security technologies.

5.2.1. Informal Description

The simplest type of confidentiality classification is a set of security clearances
arranged in a linear (total) ordering (see Figure 5—1). These clearances represent
sensitivity levels. The higher the security clearance, the more sensitive the infor-
mation (and the greater the need to keep it confidential). A subject has a security
clearance. In the figure, Claire’s security clearance is C (for CONFIDENTIAL),
and Thomas’s is TS (for TOP SECRET). An object has a security classification;
the security classification of the electronic mail files is S (for SECRET), and that
of the telephone list files is UC (for UNCLASSIFIED). (When we refer to both
subject clearances and object classifications, we use the term “classification.”) The
goal of the Bell-LaPadula security model is to prevent information flowing from
objects at a security classification higher than a subject’s clearance to that subject.

The Bell-LaPadula security model combines mandatory and discretionary
access controls. In what follows, “S has discretionary read (or write) access to
O” means that the access control matrix entry for S and O corresponding to the
discretionary access control component contains a read (or write) right. In other
words, were the mandatory controls not present, S would be able to read (or
write) O.

Let L(S) = /, be the security clearance of subject S, and let L(O) = /, be the
security classification of object O. For all security classifications /;, i = 0,...,4 —1,
[i <Tist:

Simple Security Condition, Preliminary Version: S can read O if and only if J, < /s
and S has discretionary read access to O.

TOP SECRET (TS) Tamara, Thomas Personnel Files
SECRET (S) Sally, Samuel Electronic Mail Files

CONFIDENTIAL (C) — Claire, Clarence Activity Log Files
UNCLASSIFIED (UC) Ulaley, Ursula Telephone List Files

Figure 5-1 At the left is the basic confidentiality classification system. The four
security levels are arranged with the most sensitive at the top and the least
sensitive at the bottom. In the middle are individuals grouped by their security
clearances, and at the right is a set of documents grouped by their security
levels.

FR ICR 0) AC RH
--- page 51 ---
In Figure 5-1, for example, Claire and Clarence cannot read personnel files,
but Tamara and Sally can read the activity log files (and, in fact, Tamara can
read any of the files, given her clearance), assuming that the discretionary access
controls allow it.

Should Tamara decide to copy the contents of the personnel files into the
activity log files and set the discretionary access permissions appropriately, Claire
could then read the personnel files. Thus, for all practical purposes, Claire could
read the files at a higher level of security. A second property prevents this:

*-Property (Star Property), Preliminary Version: S can write O if and only if /, > /;
and S has discretionary write access to O.

Because the activity log files are classified C and Tamara has a clearance of
TS, she cannot write to the activity log files.

If both the simple security condition, preliminary version, and the
*-property, preliminary version, hold, call the system a secure system. A straight-
forward induction establishes the following theorem.

Theorem 5.1. Basic Security Theorem, Preliminary Version: Let S be a sys-
tem with a secure initial state so, and let T be a set of state transformations.
If every element of T preserves the simple security condition, preliminary
version, and the *-property, preliminary version, then every state s;,i > 0,
is secure.

Expand the model by adding a set of categories to each security clas-
sification. Each category describes a kind of information. Objects placed in
multiple categories have the kinds of information in all of those categories. These
categories arise from the “need to know” principle, which states that no subject
should be able to read objects unless reading them is necessary for that subject to
perform its functions. The sets of categories to which a person may have access
is simply the power set of the set of categories. For example, if the categories are
NUC, EUR, and US, someone can have access to any of the following sets of
categories: @ (none), { NUC }, { EUR }, { US }, { NUC, EUR }, { NUC, US },
{ EUR, US }, and { NUC, EUR, US}. These sets of categories form a lattice under
the operation C (subset of); see Figure 5—2. (Appendix A, “Lattices,” discusses the
mathematical nature of lattices.)

Each security clearance or classification and category forms a security
level.' As before, we say that subjects have clearance at (or are cleared into, or are
in) a security level and that objects are at the level of (or are in) a security level. For
example, William may be cleared into the level (SECRET, { EUR }) and George

'This terminology is not fully agreed upon. Some call security levels “compartments.” However,
other use this term as a synonym for “categories.” We follow the terminology of the unified
exposition [150].

FRR ICR 7 FA HH
--- page 52 ---
{ NUC, EUR, US}

{ NUC, EUR } { NUC, US } { EUR, US }

| ero eis
{ NUC } { EUR } { US}

——— |

Figure 5-2 Lattice generated by the categories NUC, EUR, and US. The lines
represent the ordering relation induced by c.

into the level (TOP SECRET, { NUC, US }). A document may be classified as
(CONFIDENTIAL, { EUR }).

Security levels change access. Because categories are based on a “need to
know,” someone with access to the category set { NUC, US } presumably has no
need to access items in the category EUR. Hence, read access should be denied,
even if the security clearance of the subject is higher than the security classification
of the object. But if the desired object is in any security level with category sets
@, { NUC }, { US }, or { NUC, US } and the subject’s security clearance is no
less than the document’s security classification, access should be granted because
the subject is cleared into the same category set as the object. This suggests a new
relation for capturing the combination of security classification and category set.
Define the relation dom (dominates) as follows.

Definition 5-1. The security level (L,C) dominates the security level
(L’, C’), written (L, C) dom(L’, C’), if and only if L’ < Land C’ CC.

We write (L, C) -dom(L’, C’) when (L, C) dom(L’, C’) is false. This relation
also induces a lattice on the set of security levels [534].

EXAMPLE: George is cleared into security level (SECRET, { NUC, EUR }), DocA
is classified as (CONFIDENTIAL, { NUC }), DocB is classified as (SECRET,
{ EUR, US }), and DocC is classified as (SECRET, { EUR }). Then:

* George dom DocA as CONFIDENTIAL < SECRET and { NUC} ¢
{ NUC, EUR }

* George -dom DocB as { EUR, US } ¢g { NUC, EUR }

* George dom DocC as SECRET < SECRET and { EUR } € { NUC,
EUR }

FRI ICR DD A HH
--- page 53 ---
Let C(S) be the category set of subject S, and let C(O) be the category set
of object O. The simple security condition, preliminary version, is modified in the
obvious way:

Simple Security Condition: S can read O if and only if SdomO and S has
discretionary read access to O.

In the previous example, George can read DocA and DocC but not DocB
(again, assuming that the discretionary access controls allow such access).

Suppose Paul is cleared into security level (SECRET, { EUR, US, NUC })
and has discretionary read access to DocB. Paul can read DocB; were he to copy
its contents to DocA and set its access permissions accordingly, George could then
read DocB. The modified *-property prevents this:

*-Property: S can write to O if and only if Odom S and S has discretionary write
access to O.
DocA dom Paul is false (because C(Paul) ¢ C(DocA)), so Paul cannot write to
DocA.

The simple security condition is often described as “no reads up” and the
*-property as “no writes down.”

Redefine a secure system to be a system in which both the simple security
property and the *-property hold. The analogue to the Basic Security Theorem,
preliminary version, can also be established by induction.

Theorem 5.2. Basic Security Theorem: Let S be a system with a secure initial
state sp, and let T be a set of state transformations. If every element of T
preserves the simple security condition and the *-property, then every state
5;,1 = 0, is secure.

At times, a subject must communicate with another subject at a lower level.
This requires the higher-level subject to write into a lower-level object that the
lower-level subject can read.

EXAMPLE: A colonel with (SECRET, { NUC, EUR }) clearance needs to send a
message to a major with (SECRET, { EUR }) clearance. The colonel must write a
document that has at most the (SECRET, { EUR }) classification. But this violates
the *-property, because (SECRET, { NUC, EUR }) dom(SECRET, { EUR }).

The model provides a mechanism for allowing this type of communication.
A subject has a maximum security level and a current security level. The maximum
security level must dominate the current security level. A subject may (effectively)
decrease its security level from the maximum in order to communicate with entities
at lower security levels.

FRR ICR 3 FI HR Ha
--- page 54 ---
EXAMPLE: The colonel’s maximum security level is (SECRET, { NUC, EUR }).
She changes her current security level to (SECRET, { EUR }). This is valid,
because the maximum security level dominates the current security level. She can
then create the document at the major’s clearance level and send it to him.

How this policy is instantiated in different environments depends on the
requirements of each environment. The conventional use is to define “read” as
“allowing information to flow from the object being read to the subject reading,”
and “write” as “allowing information to flow from the subject writing to the object
being written.” Thus, “read” usually includes “execute” (because by monitoring
the instructions executed, one can determine the contents of portions of the file)
and “write” includes “append” (as the information is placed in the file, it does not
overwrite what is already in the file, however). Other actions may be included as
appropriate; however, those who instantiate the model must understand exactly
what those actions are. Chapter 9, “Noninterference and Policy Composition,”
and Chapter 18, “Confinement Problem,” will discuss this subject in considerably
more detail.

FRR ICD A HOEK
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper f71b8c26b607

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7011/Information Security/ANS_Information Security(702CO0C039)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: mixed (45 pages), mean OCR confidence 90.8
- 11 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Information Security
Date: 05 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 45 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1   Define the following.
SO-   1. Access
2. Asset
a.   3. Exploit   [5]
BL-1   4. Exposure
5. Threat
6. Threat Agent
Ans.
********** 1 **********

[Text in pictures on this page, read by OCR]
* Access: A subject or object’s ability to use, manipulate, modify, or affect another sub-
ject or object. Authorized users have legal access to a system, whereas hackers must
gain illegal access to a system. Access controls regulate this ability.

* Asset: The organizational resource that ts being protected. An asset can be logical, such
as a Web site, software information, or data; or an asset can be physical, such as a
person, computer system, hardware, or other tangible object. Assets, particularly infor-
mation assets, are the focus of what security efforts are attempting to protect.

* Exploit: A technique used to compromise a system. This term can be a verb or a noun.
Threat agents may attempt to exploit a system or other information asset by using it
illegally for their personal gain. Or, an exploit can be a documented process to take
advantage of a vulnerability or exposure, usually in software, that is either inherent in
the software or created by the attacker. Exploits make use of existing software tools or
custom-made software components.

* Exposure: A condition or state of being exposed; in information security, exposure
exists when a vulnerability is known to an attacker.

* Threat: Any event or circumstance that has the potential to adversely affect operations
and assets. The term threat source is commonly used interchangeably with the more
generic term threat. While the two terms are technically distinct, in order to simplify
discussion, the text will continue to use the term threat to describe threat sources.

* Threat agent: The specific instance or a component of a threat. For example, the threat
source of “trespass or espionage” is a category of potential danger to information assets,
while “external professional hacker” (like Kevin Mitnick, who was convicted of hacking
into phone systems) is a specific threat agent. A lightning strike, hailstorm, or tornado is
a threat agent that is part of the threat source known as “acts of God/acts of nature.”
--- page 2 ---
COo-3

SO- b. Describe the simplified model of symmetric encryption scheme. [5]

BL-2

Symmetric Encryption

Symmetric encryption, also referred to as conventional encryption or single-key
encryption, was the only type of encryption in use prior to the introduction of public-key
encryption in the late 1970s. Countless individuals and groups, from Juli esar to the
German U-boat force to present-day diplomatic, military, and commercial users, have

Secret key shared by Secret key shared by

sender and recipient sender and recipient
—_ Transmitted —_

x ciphertext

— [8) —H>mell ee |
— i Y=E[K,X| i X=DK,Yy] | ==
Plaintext Plaintext
input Encryption algorithm Decryption algorithm ‘output

(e.g., DES) (reverse of encryption

algorithm.)

Figure 2.1 Simplified Model of Symmetric Encryption

used symmetric encryption for secret communication. It remains the more widely used
of the two types of encryption.
Asymmetric encryption scheme has five ingredients (Figure 2.1):

* Plaintext: This is the original message or data that is fed into the algorithm as
input.

Ans. © Encryption algorithm: The encryption algorithm performs various substitutions

and transformations on the plaintext.

* Secret key: The secret key is also input to the encryption algorithm. The exact
substitutions and transformations performed by the algorithm depend on the
key.

* Ciphertext: This is the scrambled message produced as output. It depends on
the plaintext and the secret key. For a given message, two different keys will
produce two different ciphertents.

* Decryption algorithm: This is essentially the encryption algorithm run in
reverse. It takes the ciphertext and the secret key and produces the original
plaintext.

There are two requirements for secure use of symmetric encryption:

1. We need a strong eneryption algorithm. Ata minimum, we would like the
algorithm to be such that an opponent who knows the algorithm and has
access to one or more ciphertexts would be unable to decipher the ciphertext
or figure out the key. This requirement is usually stated in a stronger form:
The opponent should be unable to decrypt ciphertext or discover the key even
if he or she is in possession of a number of ciphertexts together with the plain-
text that produced each ciphertext.

2. Sender and receiver must have obtained copies of the secret key in a secure
fashion and must keep the key secure. [f someone can discover the key and
knows the algorithm, all communication using this key is readable.

There are two general approaches to attacking a symmetric encryption
scheme. The first attack is known as cryptanalysis. Cryptanalytic attacks rely on

FIC 2 I HH ar
--- page 3 ---
CO-2
SO-   c.   List the various types of malicious code and their functions.   [5]
BL-1
Ans.
CO-3
SO-   d.   State the means of authentication.   [5]
BL-2
********** 3 **********

[Text in pictures on this page, read by OCR]
Yable 2.1 Average Time Required for Exhaustive Key Search

Number of Time Required Time Required
Key Size (bits) Alternative Keys at 1 Decryption/us at 10° Decryptions/us
32 2°=43 = 10° 2" pes = 35.8 minutes 2.15 milliseconds
56 2" = 7.2 x 1 2° pes = 1142 years 10.01 hours,
128 m=34 x 10" 27 us = 5.4% 10 years 5.4 ™ 10" years
16s 28=3.7 x 10" 2" us = 5.9 * 10" years 5.4% 10° years
26 characters
(permutation) 26!=4 x 10° 2™ LF us = 64 x 10° years 64% 10° years

the nature of the algorithm plus perhaps some knowledge of the general character-
istics of the plaintext or even some sample plaintext-ciphertext pairs. This type of
attack exploits the characteristics of the algorithm to attempt to deduce a specific
plaintext or to deduce the key being used. If the attack succeeds in deducing the
key, the effect is catastrophic: All future and past messages encrypted with that key
are compromised.

The second method, known as the brute-force attack, is to try every possible
key on a piece of ciphertext until an intelligible translation into plaintext is obtained.
On average, half of all possible keys must be t . Table 2.1 shows
how much time is involved for various key sizes. The table shows results for cach key
size, assuming that it takes | ps to perform a single decryption, a reasonable order of
magnitude for today’s computers. With the use of massively parallel organizations
of microprocessors, it may be possible to achieve processing rates many orders of
magnitude greater. The final column of the table considers the results for a system
that can process 1 million keys per microsecond. As one can see, al this performance
level, a 56-bit key can no longer be considered computationally secure.

MALICIOUS PROGRAM ERRORS

TYPES OF FUNCTION
MALICIOUS CODE

Virus Code that attaches to another program and copies itself to other programs.
* Transient virus — life depends on life of its host
* Resident virus — locates inside memory

Trojan Horse malicious effect is hidden from user (Ex: login script)

Logic viruses triggered by an event and goes off when specific condition occur

Time viruses triggered by a time or date

Trapdoor (backdoor) feature that allows access to program other than through normal channels

Worm program that spreads copies of itself through a network, can be stand alone program
Rabbit virus/worm that self-replicates without bound. Overtime, so many copies of Rabbit

would be running that it would clog the system, making it run slow and making it
more difficult to remove the program.
--- page 4 ---
Means of Authentication

There are four general means of authenticating a user’s identity, which can be used
alone or in combination:

e Something the individual knows: Examples include a password, a personal
identification number (PIN), or answers to a prearranged set of questions.

e Something the individual possesses: Examples include electronic keycards,
smart cards, and physical keys. This type of authenticator is referred to as a
token.

¢ Something the individual is (static biometrics): Examples include recognition
by fingerprint, retina, and face.

e Something the individual does (dynamic biometrics): Examples include recog-
nition by voice pattern, handwriting characteristics, and typing rhythm.

Ans. . .
ns All of these methods, properly implemented and used, can provide secure user

authentication. However, each method has problems. An adversary may be able to
guess or steal a password. Similarly, an adversary may be able to forge or steal a token.
A user may forget a password or lose a token. Further, there is a significant admin-
istrative overhead for managing password and token information on systems and
securing such information on systems. With respect to biometric authenticators, there
are a variety of problems, including dealing with false positives and false negatives,
user acceptance, cost, and convenience. Multifactor authentication refers to the use
of more than one of the authentication means in the preceding list (see Figure 3.2).
The strength of authentication systems is largely determined by the number of factors
incorporated by the system. Implementations that use two factors are considered to
be stronger than those that use only one factor; systems that incorporate three factors
are stronger than systems that only incorporate two of the factors, and so on.

Q2 [20]

COo-3

SO- a. Explain the working of AES in depth with the help of block diagrams. [10]

BL-2

FIC 7) IC HOH
--- page 5 ---
20.3 ADVANCED ENCRYPTION STANDARD

The Advanced Encryption Standard (AES) was issued as a federal information pro-
cessing standard (FIPS 197). It is intended to replace DES and triple DES with an
algorithm that is more secure and efficient.

Overview of the Algorithm

AES uses a block length of 128 bits and a key length that can be 128, 192, or 256 bits.
In the description of this section, we assume a key length of 128 bits, which is likely
to be the one most commonly implemented.

Figure 20.3 shows the overall structure of AES. The input to the encryption
and decryption algorithms is a single 128-bit block. In FIPS PUB 197, this block is
depicted as a square matrix of bytes. This block is copied into the State array, which
is modified at cach stage of encryption or decryption. After the final stage, State is
copied to an output matrix. Similarly, the 128-bit key is depicted as a square matrix
of bytes. This key is then expanded into an array of key schedule words; each word
is 4 bytes and the total key schedule is 44 words for the 128-bit key. The ordering
of bytes within a matrix is by column. So, for example, the first 4 bytes of a 128-bit
plaintext inpul to the encryption cipher occupy the first column of the im matrix,
the second 4 bytes occupy the second column, and so on. Similarly, the first 4 bytes
of the expanded key, which form a word, occupy the first column of the w matrix.

The following comments give some insight into AES:

Ans.

1. One noteworthy feature of this structure is that it is not a Feistel structure.
Recall that in the classic Feistel structure, half of the data block is used to
modify the other half of the data block, and then the halves are swapped. AES
does not use a Feistel structure but processes the entire data block in parallel
during cach round using substitutions and permutation.

2. The key that is provided as input is expanded into an array of forty-four 32-bit
words, w[i]. Four distinct words (128 bits) serve as a round key for each round.

3. Four different stages are used, one of permutation and three of substitution:

* Substitute Bytes: Uses a table, referred to as an S-box, to perform a byte-
by-byte substitution of the block

* Shift Rows: A simple permutation that is performed row by row

FIC DI EH ar
--- page 6 ---
Plaintext Key Plaintext
Add round key aw[0, 3] Add round key
=
| Substitute bytes | | Expand key | | Inverse sub bytes | =
= Inverse shift rows
B sees seep ee eeee------}----- ee j
2 J
w[4. 7] Add round key =
?

Inverse sub bytes g
Inverse shift rows

a Shift rows

|
a
é J
Add rownd key w[36, 39]
-
S z

i Shift rows | Inverse shift rows E

Add rownd key w[40, 43] Add round key
Ciphertext Ciphertext
(a) Encryption (b) Decryption

Figure 20.3 AES Encryption and Decryption

* Mix Columns: A substitution that alters each byte in a column as a function
of all of the bytes in the column

« Add Round key: A simple bitwise XOR of the current block with a portion
of the expanded key

4, The structure is quite simple. For both encryption and decryption, the cipher
begins with an Add Round Key stage, followed by nine rounds that each
includes all four stages, followed by a tenth round of three stages. Figure 20.4
depicts the structure of a full encryption round.

FIC 6 I HF
--- page 7 ---
‘State [

— bbddddd

oe

woe Yetmetef tae
. etoile ta el ta


Figure 20.4 AES Encryption Round

§. Only the Add Round Key stage makes use of the key. For this reason, the
cipher begins and ends with an Add Round Key stage. Any other stage,
applied at the beginning or end, is reversible without knowledge of the key
and so would add no security.

6. The Add Round Key stage by itself would not be formidable. The other three
stages together scramble the bits, but by themselves would provide no security
because they do not use the key. We can view the cipher as alternating opera-
tions of XOR encryption (Add Round Key) of a block, followed by scram-
bling of the block (the other three stages), followed by XOR encryption, and
so on. This scheme is both efficient and highly secure.

7. Each stage is easily reversible. For the Substitute Byte, Shift Row, and Mix
Columns stages, an inverse function is used in the decryption algorithm. For
the Add Round Key stage, the inverse is achieved by XORing the same round
key to the block, using the result that AS A @B = B.

8. As with most block ciphers, the decryption algorithm makes use of the
expanded key in reverse order. However, the decryption algorithm is not
identical to the encryption algorithm. This is a consequence of the particular
structure of AES.

FIC 7 IC OHH
--- page 8 ---
9, Once it is established that all four stages are reversible, it is easy lo verily
that decryption does recover the plaintext. Figure 20.3 lays out encryption
and deeryplion going in opposite vertical directions. At each horizontal point
(e.g., the dashed line in the figure), State is the same for both encryption and
decryption.

10. The final round of both encryption and decryption consists of only three
stages. Again, this is a consequence of the particular structure of AES and is
required to make the cipher reversible.

Algorithm Details

We now look briefly at the principal elements of AES in more detail.

Sussrircere Byres TRANSFORMATION ‘The forward substitute byte transformation,
called SubBytes, is a simple table lookup. AES defines a 16-16 matrix of byte values,
called an S-box (Table 20.2a), that contains a permutation of all possible 256 8-bit
values. Each individual byte of State is mapped into a new byte in the following
way: The leftmost 4 bits of the byte are used as a row value and the rightmost 4
bits are used as a column value. These row and column values serve as indexes
into the $-box to select a unique 8-bil output value. For example, the hexadecimal
value" {95} references row 9, column 5 of the S-box, which contains the value {2A}.
Accordingly, the value {95} is mapped into the value {2A}.

Here is an example of the SubBytes transformation:

The 8-box is constructed using properties of finite fields. The topic of finite
fields is beyond the scope of this book; it is discussed in detail in [STAL11b].

EA ao 65 a5 87 F2 4D o7
a3 45 5D Bo EC 6E 4c 90
5c 33 o8 BO 4a “3 4h ET

The inverse substitute byte transformation, called InvSubBytes, makes use of
the inverse $-box shown in Table 20.2b. Note, for example, that the input {2A} pro-
duces the output {95}, and the input {95} to the S-box produces {2.4}.

The S8-box is designed to be resistant to known cryptanalytic attacks.
Specifically, the AES developers sought a design that has a low correlation between
input bits and output bits and the property that the output cannot be described as a
simple mathematical function of the input.

Surry Row TraysrorMaTion For the forward shift row transformation, called
ShiftRows, the first row of State is not altered. For the second row, a 1-byte circular
left shift is performed. For the third row, a 2-byte circular left shift is performed.

FIC QF EH 1
--- page 9 ---
Fable 20.2

AES §-Boxes

(a) S-box
y


a 63) 7C | 77 | 7B | F2) 6B | 6F | C5 | 30 |] OL | 47 | 2B | FE} D7 | AB] 76
1 | CA] 82] CO | 7D] FA] 59 | 47 |] FO |} AD] D4 |] A2] AF} 9C ] Ad] 72 | CO
2 | BF | FD] % | 26 | 36 |] 3F | Fr] CC] 34 | AS] ES | Fl | 71 | DB] 31 | 15
3 O4 | cr] 23 | C3] 18 | % | 05 | OA] OF | 12 | 80 | E2 | BBY] 27 | B2] 75
4 oo |] 83 | 2C | 1A |] 1B | GE | SA] AD] 52 | 3B | D6 |] BS |} 29 | E3 | 2F | &4
5 53 | D1 | oo | ED] 20 | Fc | BI | 5B |] 6A |] CB] BE] 39 | 44] 4C | 58 | CF
6 | DO] EP} AA] FRY] 43 | 4D | 33 | 85 | 45 | FO | 02 | TF | S50 | 3C |) OF | AB
Xx 7 51 | AS] 40 | SF | 92 | 9D | 38 | F5 | BC] Be | DA! 21 | 10 | FF | F3 | D2
& | cD] 0c} 13 | EC] SF] 97 | 44] 17 | C4] AT] FE | 3D] 64 | SD] 19 | 73
a 6) | 81 | 4F | DC] 22) 2A] OF | 88 | 46 | EE] BS] 14 | DE] SE | 0B | DB
A | EO] 32] 3A] 0A 7 49 | 06 | 24 | 5C ] C2 | DS] AC! G2 | 91 | 95 | Ea] 7
B | EF | C8] 37 | 6D] 8D | DS | 4E] AD] oC | 56 | F4 | BAY] 65 | 7A | AB] OB
C | BA] 78 | 25 | 2B] 1c |] As | Ba] Ch | EX | DD] 74 | 1F | 4B | BD | 8B | SA
D | 7 | 3E ] BS | ob | 48 |] 03 | Fo | OE | @l | 35 | 57 |) BY | SH ] Cl | 1D | YE
E | El] Fe |] 98 | 11 |] 69 | DY] SE] 94 | 9B | 1E | 87 | BY | CE] 55 | 28 | DF
PF ac ] Al ao) | 0D | BF | Ea | 42 68 41 99 72D) OF | BO | 54 | BB] 16

(b) Inverse S-box
¥

a 52] 09 | 6A | DS | 30 | 36 | AS | 38 | BF | 40 | AS | YE | 81 | FS | DT | FB
1 7C | E3 | 39 | &2 | 9B | 2F | FF} 87 | 34 | BE | 43 | 44 | C4 | DE! EO | CB
2 54] 7B | 4 | 32 | Ab |] C2] 23 | 3D] EE | 4C |] 95 | OB | 42 | FA | C3 | 4E
3 O8 | 3B |) Al | 66 | 28 |] D9) 34] B2] Je | SB] AZ] 49 | 6D] 8B |] D1] 35
4 72 | FS | Fo | 64 | 86 |] 68 | OF | 16 | D4] Ad] SC |] CC] SD] 65 | BA | 9
5 | 6c | 70] 48 | 50 | FD | ED} BY] DA] SE] 15 | 46 | 57 | AT] 8D | OD |
if o | DS | AB] OO | BC] BC} D3] OA] F? | E4 |] 58 | 05 | BR] B3 | 45 | 06
Xx 7 | DO] 2C | 1E | 8F CA] 3F | OF | 02 | Cl | AF] BD] 03 | O1 | 13 | SA | OB
8 | 3A 7 91 di | 41 | 4F | 67 | DC] EA] 97 | F2 | CF] CE | Fo | B4 | Eo | 735
a 9h | AC] 74 | 22 | ET |] AD] 35 | 85 | E2 | FO | 37 | Es | 1c | 75 | DF] 6E
A | 47 |] FL] 1A] 71 | ID] 29 | C5 | 89 | GF | BF ] 62 | OE | AAT 18 | BE | 1B
B | FC |] 56 | 3E | 4B] Ch |] D2] 79 | 20 | 9A | DB] CO] FE | 78 | CD] 5A | FA
C | IF | DD] As} 33 7 88 ] oF | C7] 31] Bl | 12 | 10 |] 59 | 27 | BO | Be} AP
D | 6 | 51 |] 7F | AQ] 19 | BS | 4A] 0D | 2D | ES | 7A} OF | 93 | Co] OC | EF
E | Ad | Eo | 3B | 4D] AE] 2A] F5 ] BO | CR | EB] BB] 3C | 83 | 53] | al
F 17 | 2B | 4 | 7E | BA] 77 | De | 26 | El} 69 | 14 | 63 | 55 | 21 | oc | 7D

FIC QF OH ar
--- page 10 ---
For the third row, a 3-byte circular left shift is performed. The following is an
example of ShiftRows:

aT F2 4D oT cr Fi 4D a7
Ec 6E 4c 90 6E 4c 90 EC
4A C3 4 Er 46 E7 4A c3

The inverse shift row transformation, called InvShiltRows, performs the cir-
cular shifts in the opposite direction for each of the last three rows, with a 1-byte
circular right shift for the second row, and so on.

The shift row transformation is more substantial than it may first appear. This
is because the State, as well as the cipher input and outpul, is treated as an array of
four 4-byte columns. Thus, on encryption, the first 4 bytes of the plaintext are cop-
ied to the first column of State, and so on. Further, as will be seen, the round key is
applied to State column by column. Thus, a row shift moves an individual byte from
one column to another, which is a linear distance of a multiple of 4 bytes. Also note
that the transformation ensures that the 4 bytes of one column are spread out to
four different columns.

Mix Cotuwn Transrorwarion The forward mix column transformation,
called MixColumns, operates on cach column individually. Each byte of a column
is mapped into a new value that is a function of all 4 bytes in the column. The
mapping makes use of equations over finite fields. The following is an example of
MixColumns:

a7 F2 4D 7 47 40 AG 4c
6E 4c 0 EC a7 D4 70 oF
46 ET 4A c3 04 E4 3A 42

The mapping is designed to provide a good mixing among the bytes of each
column. The mix column transformation combined with the shift row transforma-
tion ensures that after a few rounds, all output bits depend on all input bits.

App Rounp Key TRANSFORMATION In the forward add round key
transformation, called AddRoundKey, the 128 bits of State are bitwise NORed
with the 128 bits of the round key. The operation is viewed as a column-wise
operation between the four bytes of a State column and one word of the round
key: it can also be viewed as a byte-level operation. The following is an example
of AddRoundKey:

FRR ICR 7 OI HOH
--- page 11 ---
a 40 Ag 4c AC 19 28 57 EB 39 5B 1B

0 Da 70) oF @ 77 FA DI 5c 40) 2E Al 3
eel E4 3A a2 66 DC 29 OO F2 ci] 13 42

The first matrix is State, and the second matrix is the round key.

The inverse add round key transformation is identical to the forward add
round key transformation, because the NOR operation is its own inverse.

The add round key transformation is as simple as possible and affects every
bit of State. The complexity of the round key expansion, plus the complexity of the
other stages of AES, ensure security.

AES Key Expansion The AES key expansion algorithm takes as input a 4-word
(16-byte) Key and produces a linear array of 44 words (156 bytes). This is sufficient
to provide a 4-word round key for the initial Add Round Key stage and each of the
10 rounds of the cipher.

The key is copied into the first four words of the expanded key. The remainder
of the expanded key is filled in four words at a time. Each added word w{i] depends on
the immediately preceding word, w[i— 1], and the word four positions back, w[i-4]. A
complex finite-field algorithm is used in generating the expanded key.

CO-2

SO- b. State the steps of risk analysis. Explain the first two steps in detail. [10]

BL-2

Steps of a Risk Analysis

Risk analysis is performed in many different contexts; for example, environmental and
health risks are analyzed for activities such as building dams, disposing of nuclear waste,
or changing a manufacturing process. Risk analysis for security is adapted from more
general management practices, placing special emphasis on the kinds of problems likely to
arise from security issues. By following well-defined steps, we can analyze the security
risks in a computing system.

A The basic steps of risk analysis are listed below.
ns. 1. Identify assets.

2. Determine vulnerabilities.

3. Estimate likelihood of exploitation.

4. Compute expected annual loss.

5. Survey applicable controls and their costs.
6. Project annual savings of control.

Sidebar 10-4 illustrates how different organizations take slightly different approaches,

FRI ICR 7 FI OH
--- page 12 ---
but the basic activities are still the same. These steps are described in detail in the
following sections.

Sidebar 10-4 Alternative Steps in Risk Analysis

There are many formal approaches to performing risk analysis. For example, the
U.S. Army used its Operations Security (OPSEC) guidelines during the Vietnam
War [SEC99]. The guidelines involve five steps:

1. Identify the critical information to be protected.

2. Analyze the threats.

3. Analyze the vulnerabilities.

4. Assess the risks.

5. Apply countermeasures.

Similarly, the U.S. Air Force uses an Operational Risk Management

procedure to support its decision making. [AIR00] The steps are

1. Identify hazards.

2. Assess hazards.

3. Make risk decisions.

4. Implement controls.

5. Supervise.

As you can see, the steps are similar, but their details are always tailored to
the particular situation at hand. For this reason, you may use someone else’s risk
analysis process as a framework, but then change it to match your own situation.

Step 1: Identify Assets

Before we can identify vulnerabilities, we must first decide what we need to protect.
Thus, the first step of a risk analysis is to identify the assets of the computing system. The
assets can be considered in categories, as listed below. The first three categories are the
assets identified in Chapter 1 and described throughout this book. The remaining items are
not strictly a part of a computing system but are important to its proper functioning.

+ hardware: processors, boards, keyboards, monitors, terminals,
microcomputers, workstations, tape drives, printers, disks, disk drives, cables,
connections, communications controllers, and communications media

* software: source programs, object programs, purchased programs, in-house
programs, utility programs, operating systems, systems programs (such as
compilers), and maintenance diagnostic programs

+ data: data used during execution, stored data on various media, printed data,
archival data, update logs, and audit records

+ people: skilled staff needed to run the computing system or specific programs,
as well as support personnel such as guards

+ documentation: on programs, hardware, systems, administrative procedures,
and the entire system

FRR ICR] DA KH
--- page 13 ---
+ supplies: paper, forms, laser cartridges, recordable media, and printer ink, as
well as power, heating and cooling, and necessary buildings or shelter
* reputation: company image

+ availability: ability to do business, ability to resume business rapidly and
efficiently after an incident

You have to tailor this list to your own situation. No two organizations will have the
same assets to protect, and something that is valuable in one organization may not be as
valuable to another. For example, if a project has one key designer, then that designer is an
essential asset; on the other hand, if a similar project has ten designers, any of whom could
do the project’s design, then each designer is not as essential because there are nine easily
available replacements. Thus, you must add to the list of assets the other people,
processes, and things that must be protected.

Not all business assets are tangible, and not all are easy to value.

In a sense, the list of assets is an inventory of the system, including intangibles and
human resource items. For security purposes, this inventory is more comprehensive than
the traditional inventory of hardware and software often performed for configuration
management or accounting purposes. The point is to identify all assets necessary for the
system to be usable.

Step 2: Determine Vulnerabilities

The next step in risk analysis is to determine the vulnerabilities of these assets. This
step requires imagination; we want to predict what damage might occur to the assets and
from what sources. We can enhance our imaginative skills by developing a clear idea of
the nature of vulnerabilities. This nature derives from the need to ensure the three basic
goals of computer security: confidentiality, integrity, and availability. Thus, a vulnerability
is any situation that could cause loss of confidentiality, integrity, and availability. We want
to use an organized approach to considering situations that could cause these losses for a
particular object.

Software engineering offers us several techniques for investigating possible problems.
Hazard analysis, described in Sidebar 10-5, explores failures that may occur and faults that
may cause them. These techniques have been used successfully in analyzing safety-critical
systems. However, additional techniques are tailored specifically to security concerns; we
address those techniques in this and following sections.

Sidebar 10-5 Hazard Analysis Techniques
Hazard analysis is a set of systematic but informal techniques intended to
expose potentially hazardous system states. Using hazard analysis helps us find
strategies to prevent or mitigate harm once we understand what problems can
occur. That is, hazard analysis ferrets out not only the effects of problems but
also their likely causes so that we can then apply an appropriate technique for
preventing a problem or softening its consequences. Hazard analysis usually
involves creating hazard lists as well as procedures for exploring “what if”
scenarios to trigger consideration of nonobvious hazards. The problems’ sources

FIR ICR 7] QI HO
--- page 14 ---
can be lurking in any artifacts of the development or maintenance process, not
just in the code. There are many kinds of problems, ranging from incorrect
information or code, to unclear consequences of a particular action. A good
hazard analysis takes all of them into account.

Different techniques support the identification and management of potential
hazards in complex critical systems. Among the most effective are hazard and
operability studies (HAZOP), failure modes and effects analysis (FMEA), and
fault tree analysis (FTA). HAZOP is a structured analysis technique originally
developed for the process control and chemical plant industries. FMEA is a
bottom-up technique applied at the system component level. A team identifies
each component’s possible faults or fault modes; then, it determines what could
trigger the fault and what systemwide effects each fault might have. By keeping
system consequences in mind, the team often finds possible system failures that
are not made visible by other analytical means. FTA complements FMEA. It is a
top-down technique that begins with a postulated hazardous system malfunction.
Then, the FTA team works backwards to identify the possible precursors to the
mishap. By tracing from a specific hazardous malfunction, the team can derive
unexpected contributors to mishaps and identify opportunities to mitigate the
risk of mishaps.

We decide which technique is most appropriate by understanding how much
we know about causes and effects. When we know the cause and effect of a
given problem, we can strengthen the description of how the system should
behave. If we can describe a known effect with unknown cause, then we use
deductive techniques such as FTA to help us understand the likely causes of the
unwelcome behavior. Conversely, we may know the cause of a problem but not
understand all the effects; here, we use inductive techniques such as FMEA to
help us trace from cause to all possible effects. Finally, to find problems about
which we may not yet be aware, we perform an exploratory analysis such as a
HAZOP study.

To organize the way we consider threats and assets, we can use a matrix such as the one
shown in Table 10-2. One vulnerability can affect more than one asset or cause more than
one type of loss. The table is a guide to stimulate thinking, but its format is not rigid.

Asset Confidentiality Integrity Availability

Hardware

Software

Data

People

Documentation

Supplies

TABLE 10-2 Assets and Security Properties

In thinking about the contents of each matrix entry, we can ask the following questions.

FRR IC 7 I OH
--- page 15 ---
+ What are the effects of unintentional errors? Consider typing the wrong
command, entering the wrong data, using the wrong data item, discarding the
wrong listing, and disposing of output insecurely.

+ What are the effects of willfully malicious insiders? Consider disgruntled
employees, bribery, and curious browsers.

+ What are the effects of outsiders? Consider network access, remote access,
hackers, people walking through the building, people snooping at coffee shops,
and people sifting through the trash.

+ What are the effects of natural and physical disasters? Consider fires, storms,
floods, power outages, and component failures.

Table 10-3 is a version of the previous table with some of the entries filled in. It shows
that certain general problems can affect the assets of a computing system. Planners at a
given installation will determine what can happen to specific hardware, software, data
items, and other assets.

Asset Secrecy Integrity Availability
Hardware overloaded failed
destroyed stolen
tampered with | destroyed
unavailable
Software stolen impaired by deleted
copied Trojan horse misplaced
pirated modified usage expired
tampered with
Data disclosed damaged deleted
accessed by | —software error | misplaced
outsider —hardware error | destroyed
inferred —user error
People quit
retired
terminated
on vacation
Documentation lost
stolen
destroyed
Supplies lost
stolen
damaged

TABLE 10-3 Assets and Attacks

Sidebar 10-6 Integrated Vulnerability Assessments and CARVER
The US. Navy (see

FRR IC 7 DA HOH
--- page 16 ---

performs Integrated Vulnerability Assessments (IVAs) as part of its risk analysis
process. An IVA uses checklists to review system vulnerabilities and suggest
appropriate mitigative strategies. The steps in an IVA include

1. identifying vulnerabilities

2. assigning priorities to the vulnerabilities

3. brainstorming countermeasures

4. assessing the risks

The Criticality, Accessibility, Recuperability, Vulnerability, Effect, and

Recognizability (CARVER) method is employed to assign priorities to the
vulnerabilities. Numeric ratings are applied to each vulnerability, and the sum
represents a vulnerability score. However, the summation procedure blurs the
distinctions among different types of risks, so the value of the overall score is
questionable. Nevertheless, [VAs and CARVER may be useful in making
security planning issues more visible.

Some organizations use other approaches to determining vulnerabilities and assessing
their importance. For example, Sidebar 10-6 describes the U.S. Navy’s approach to
vulnerability evaluation.

Alas, there is no simple checklist or easy procedure to list all vulnerabilities. But from
the earlier chapters of this book you have seen many examples of vulnerabilities to assets,
and your mind has been trained to think of harm that can occur. Tools can help us
conceive of vulnerabilities by providing a structured way to think. For example, assets
have certain properties that make them vulnerable. The properties exist in three categories:
aspects of the design or architecture, aspects of behavior, and general attributes. Table 10-
4 lists these properties in more detail. Notice that the properties apply to many kinds of
systems and at various places within a given system.

Design/Architecture Behavioral General
* Singularity * Behavioral sensitivity/fragility | + Accessible, detectable,
~ Uniqueness * Malevolence identifiable, transparent,
Centrality * Rigidity interceptable
Homogeneity * Malleability + Hard to manage or control
* Separability + Gullibility, deceivability, * Self-unawareness and
* Logic/implementation errors; | naiveté unpredictability
fallibitity * Complacency + Predictability
+ Design sensitivity, fragility, | + Corruptibility, controllability
Timits, finiteness

+ Unrecoverability

From [ANT02], copyright © RAND 2002, reprinted by permission.
TABLE 10-4 Attributes Contributing to Vulnerabilities

Q3 [20]

CO-2

SO- a. Explain the implications of overwriting memory with respective to buffer overflow. [10]

BL-2

FRR ICR 7 6 AC OH
--- page 17 ---
Implications of Overwriting Memory

Let us more closely examine the problem of overwriting memory. Be sure to recognize
that the potential overflow causes a serious problem only in some instances. The
problem’s occurrence depends on what is adjacent to the array sample. For example,
suppose each of the ten elements of the array sample is filled with the letter A and the
erroneous reference uses the letter B, as follows:

Click here to view code image
for (i=0; i<=9; i++)
sample[i] = ‘A’;
sample[10] = ‘B’

All program and data elements are in memory during execution, sharing space with the
operating system, other code, and resident routines. So four cases must be considered in
deciding where the ‘B’ goes, as shown in Figure 3-4. If the extra character overflows into
the user’s data space, it simply overwrites an existing variable value (or it may be written
into an as-yet unused location), perhaps affecting the program’s result but affecting no
other program or data.

User's Data
OO
wag AGKGBRREBEG

(a) Affects user's data

User's Data User's Program Code

Memory Jafalafafala}afafa}a |

(b) Affects user's code

User's Data System Data

Ans.

— AGEROOERODO

(c) Affects system

User’s Data System Program Code

Sane AGGEE

alafalaa |

(d) Affects system code
FIGURE 3-4 One-Character Overflow

In the second case, the ‘B’ goes into the user’s program area. If it overlays an already
executed instruction (which will not be executed again), the user should perceive no
effect. If it overlays an instruction that is not yet executed, the machine will try to execute
an instruction with operation code 0x42, the internal code for the character ‘B’. If there is
no instruction with operation code 0x42, the system will halt on an illegal instruction
exception. Otherwise, the machine will use subsequent bytes as if they were the rest of the
instruction, with success or failure depending on the meaning of the contents. Again, only
the user is likely to experience an effect.

The most interesting cases (from a security perspective) occur when the system owns
the space immediately after the array that overflows. Spilling over into system data or
code areas produces results similar to those for the user’s space: computing with a faulty
value or trying to execute an operation.

Program procedures use both local data, data used strictly within one procedure, and
shared or common or global data, which are shared between two or more procedures.
Memory organization can be complicated, but we simplify the layout as in Figure 3-5. In
that picture, local data are stored adjacent to the code of a procedure. Thus, as you can see,
a data overflow either falls strictly within a data space or it spills over into an adjacent
code area. The data end up on top of one of

+ another piece of your data
* an instruction of yours

FRR ICR] AC OH
--- page 18 ---
+ data or code belonging to another program
+ data or code belonging to the operating system

We consider each of these cases separately.

User |’s
code &
Proc M
data of
Proc M data
User 2’s Proc A
code &
data Proc A data
Operating Proc B
system’s Proc B data
code &
data

FIGURE 3-5 Memory of Different Procedures for Different Users
Affecting Your Own Data

Modifying your own data, especially with an unintended value, will obviously affect
your computing. Perhaps a loop will repeat too many or too few times, a sum will be
compromised, or a date will become garbled. You can imagine these possibilities for
yourself. The error may be so egregious that you will easily recognize something is
wrong, but a more subtle failure may escape your notice, perhaps forever.

From a security standpoint, few system controls protect you from this kind of error: You
own your data space and anything you want to store there is your business. Some, but not
all, programming languages generate checking code for things like arrays to ensure that
you store elements only within the space allocated. For this reason, the defensive
programming technique (discussed later in this chapter) recommends that you always
check to ensure that array elements and strings are within their boundaries. As Sidebar 3-3
demonstrates, sometimes such an error lies dormant for a long time.

FR ICR 7] QA HH
--- page 19 ---
specialized communications processors called IMPs. Each interface message
processor (IMP) controlled an individual subnetwork, much like today’s routers;
the IMPs connected to other IMPs through dedicated communications lines. For
reliability, each IMP had at least two distinct paths to each other IMP. The IMP
connections were added to a table dynamically as communication between two
IMPs was required by network traffic.

In 1988, one subnetwork added a connection to a 348th IMP. The table for
IMP connections had been hard-coded in 1969 to only 347 entries, which
seemed wildly excessive at the time, and in the intervening years people had
forgotten that table size if, indeed, it had ever been publicized. (In 1967, 347
IMPs was far more than the designers ever envisioned the network would have.)
Software handling the IMP’s table detected this overflow but handled it by
causing the IMP to reboot; upon rebooting, the IMP’s table was cleared and
would be repopulated as it discovered other reachable subnetworks. Apparently
the authors of that software assumed such a table overflow would be a sporadic
mistake from another cause, so clearing and rebooting would rid the table of the
faulty data. Because the fault was due to a real situation, in 1989 the refreshed
IMP ran for a while until its table refilled and then it failed and rebooted again.

It took some time to determine the source and remedy of this flaw, because
twenty years had passed between coding and failing; everybody associated with
the original design or implementation had moved on to other projects.

As this example shows, buffer overflows—like other program faults—can
remain unexploited and undetected for some time, but they are still present.

Affecting an Instruction of Yours

Again, the failure of one of your instructions affects you, and systems give wide latitude
to what you can do to yourself. If you store a string that does not represent a valid or
permitted instruction, your program may generate a fault and halt, returning control to the
operating system. However, the system will try to execute a string that accidentally does
represent a valid instruction, with effects depending on the actual value. Again, depending
on the nature of the error, this faulty instruction may have no effect (if it is not in the path
of execution or in a section that has already been executed), a null effect (if it happens not
to affect code or data, such as an instruction to move the contents of register 1 to itself), or
an unnoticed or readily noticed effect.

Destroying your own code or data is unpleasant, but at least you can say the harm was
your own fault. Unless, of course, it wasn’t your fault. One early flaw in Microsoft’s
Outlook involved the simple date field: A date is a few bytes long to represent a day,
month, year, and time in GMT (Greenwich Mean Time) format. In a former version of
Outlook, a message with a date of more than 1000 bytes exceeded the buffer space for
message headers and ran into reserved space. Simply downloading such a message from a
mail server would cause your system to crash, and each time you tried to restart, Outlook
would try to reload the same message and crash again. In this case, you suffered harm
from a buffer overflow involving only your memory area.

One program can accidentally modify code or data of another procedure that will not be

FRR ICR 7 QI OR
--- page 20 ---
CO-4   Explain any two of the following with the help of a example and diagrams.
SO-   1. Access Control Directory
b.   [10]
2. Access Control Matrix
BL-2   3. Access Control List
********** 20 **********

[Text in pictures on this page, read by OCR]
executed until much later, so the delayed impact can be almost as difficult to diagnose as if
the attack came from an unrelated, independent user. The most significant impact of a
buffer overflow occurs when the excess data affect the operating system’s code or data.

Modification of code and data for one user or another is significant, but it is not a major
computer security issue. However, as we show in the next section, buffer overflows
perpetrated on the operating system can have serious consequences.

Affecting the Operating System or a Critical Application

The same basic scenarios occur for operating system code or data as for users, although
again there are important variations. Exploring these differences also leads us to consider
motive, and so we shift from thinking of what are essentially accidents to intentional
malicious acts by an attacker.

Because the mix of programs changes continually on a computing system, there is little
opportunity to affect any one particular use. We now consider the case in which an
attacker who has already overtaken an ordinary user now wants to overtake the operating
system. Such an attack can let the attacker plant permanent code that is reactivated each
time a machine is restarted, for example. Or the attack may expose data, for example,
passwords or cryptographic keys that the operating system is entrusted to safeguard. So
now let us consider the impact a (compromised) user can have on the operating system.

Users’ code and data are placed essentially at random: wherever there is free memory of
an appropriate size. Only by tracing through system memory allocation tables can you
learn where your program and data appear in memory. However, certain portions of the
operating system are placed at particular fixed locations, and other data are located at
places that can easily be determined during execution. Fixed or easily determined location
distinguishes operating system routines, especially the most critical ones, from a user’s
code and data.

Asecond distinction between ordinary users and the operating system is that a user runs
without operating system privileges. The operating system invokes a user’s program as if
it were a subprocedure, and the operating system receives control back when the user’s
program exits. If the user can alter what the operating system does when it regains control,
the user can force the operating system to execute code the user wants to run, but with
elevated privileges (those of the operating system). Being able to modify operating system
code or data allows the user (that is, an attacker acting as the user) to obtain effective
privileged status.

Privilege escalation, executing attack code with higher system
permissions, is a bonus for the attacker.

The call and return sequence operates under a well-defined protocol using a data
structure called the stack. Aleph One (Elias Levy) describes how to use buffer overflows
to overwrite the call stack [ALE96]. In the next section we show how a programmer can
use an overflow to compromise a computer’s operation.
--- page 21 ---
Ans.

Access Control Directory

One simple way to protect an object is to use a mechanism that works like a file
directory. Imagine we are trying to protect files (the set of objects) from users of a
computing system (the set of subjects). Every file has a unique owner who possesses
“control” access rights (including the rights to declare who has what access) and to revoke
access of any person at any time. Each user has a file directory, which lists all the files to
which that user has access.

Clearly, no user can be allowed to write in the file directory, because that would be a
way to forge access to a file. Therefore, the operating system must maintain all file
directories, under commands from the owners of files. The obvious rights to files are the
common read, write, and execute that are familiar on many shared systems. Furthermore,
another right, owner, is possessed by the owner, permitting that user to grant and revoke
access rights. Figure 2-9 shows an example of a file directory.

User A Directory Files User B Directory

” Access _ File Access _ Fi

FileName Rights Pointer FileName __Rights Pointe
PROGI.C ORW BIBLIOG R e
PROGILEXE | OX Liat TEST-TMP ox |
HELPTXT =| R «| —™ HELPTXT =|R e
HEMP ORW

FIGURE 2-9 Directory Access Rights

This approach is easy to implement because it uses one list per user, naming all the

FI ICR D7 FAC HOH
--- page 22 ---
objects that a user is allowed to access. However, several difficulties can arise. First, the
list becomes too large if many shared objects, such as libraries of subprograms or a
common table of users, are accessible to all users. The directory of each user must have
one entry for each such shared object, even if the user has no intention of accessing the
object. Deletion must be reflected in all directories.

A second difficulty is revocation of access. If owner A has passed to user B the right to
read file F, an entry for F is made in the directory for B. This granting of access implies a
level of trust between A and B. If A later questions that trust, A may want to revoke the
access right of B. The operating system can respond easily to the single request to delete
the right of B to access F, because that action involves deleting one entry from a specific
directory. But if A wants to remove the rights of everyone to access F, the operating
system must search each individual directory for the entry F, an activity that can be time
consuming on a large system. For example, large systems or networks of smaller systems
can easily have 5,000 to 10,000 active accounts. Moreover, B may have passed the access
right for F to another user C, a situation known as propagation of access rights, so A may
not know that C’s access exists and should be revoked. This problem is particularly
serious in a network.

A third difficulty involves pseudonyms. Owners A and B may have two different files
named F, and they may both want to allow access by S. Clearly, the directory for S cannot
contain two entries under the same name for different files. Therefore, S has to be able to
uniquely identify the F for A (or B). One approach is to include the original owner’s
designation as if it were part of the file name, with a notation such as A:F (or B:F).

Suppose, however, that S would like to use a name other than F to make the file’s
contents more apparent. The system could allow S to name F with any name unique to the
directory of S. Then, F from A could be called Q to S. As shown in Figure 2-10, S may
have forgotten that Q is F from A, and so S requests access again from A for F. But by
now A may have more trust in S, so A transfers F with greater rights than before. This
action opens up the possibility that one subject, S, may have two distinct sets of access
rights to F, one under the name Q and one under the name F. In this way, allowing
pseudonyms can lead to multiple permissions that are not necessarily consistent. Thus, the
directory approach is probably too simple for most object protection situations.

FIR ICR DAC HH
--- page 23 ---
User A Directory Files Directory

nie Access File ais
File Name Rights Pointer <--
F ORWX| ©
BIBLIOG = |ORW FE rw | ef!


HELPTXT = |R Coa HELPTXT |R «
PROGL.EXE |OX ‘Ne |
User B Directory

“ Access _ File
FileName Rights Pointer

HELP-TXT R °
TEMP ORW |

FIGURE 2-10 Ambiguous Access Rights

Access Control Matrix

We can think of the directory as a listing of objects accessible by a single subject, and
the access list as a table identifying subjects that can access a single object. The data in
these two representations are equivalent, the distinction being the ease of use in given
situations.

As an alternative, we can use an access control matrix, shown in Figure 2-11, a table in
which each row represents a subject, each column represents an object, and each entry is
the set of access rights for that subject to that object.

7 objects =
File A Printer System
Clock
Read
2g User W Write Write Read
x Own
3 ‘
a Admin Waite Control
Control

FIGURE 2-11 Access Control Matrix

A more detailed example representation of an access control matrix is shown in Table 2-
8. Access rights shown in that table are O, own; R, read; W, write; and X, execute. In
general, the access control matrix is sparse (meaning that most cells are empty): Most
subjects do not have access rights to most objects. The access matrix can be represented as

FIR ICR 2 I OH
--- page 24 ---
a list of triples, each having the form Seubject, object, rights), as shown in Table 2-9.

Help (cm
Bibliog | Temp F txt Comp | Linker | Clock | Printer
USER B R - a R x x R Ww
USERS RW - R R x x R Ww
USER T — - R x x x R w
SYS MGR - - - RW Ox Ox ORW oO
USER SVCS | — _ - fe) x x R w

TABLE 2-8 Access Control Matrix

Subject Object Right
USER A Bibliog ORW
USER B Bibliog R
USER S Bibliog RW
USER A Temp ORW
USERA PF ORW
USER S R R

etc.

TABLE 2-9 List of Access Control Triples
This representation may be more efficient than the access control matrix because there

is no triple for any empty cell of the matrix (such as (usER T, Bibliog, -), Even though
the triples can be sorted by subject or object as needed, searching a large number of these
triples is inefficient enough that this implementation is seldom used.

Access Control List

An alternative representation is the access control list; as shown in Figure 2-12, this
representation corresponds to columns of the access control matrix. There is one such list
for each object, and the list shows all subjects who should have access to the object and
what their access is. This approach differs from the directory list because there is one
access control list per object; a directory is created for each subject. Although this
difference seems small, there are some significant advantages to this approach.

FRR IRD AC HOH
--- page 25 ---
File A Printer Systeat

Clock
Read
User W Write Write Read
Own
Admin Write Control
Control

FIGURE 2-12 Access Control List

The access control list representation can include default rights. Consider subjects A
and S, both of whom have access to object F. The operating system will maintain just one
access list for F, showing the access rights for A and S, as shown in Figure 2-13. The
access control list can include general default entries for any users. In this way, specific
users can have explicit rights, and all other users can have a default set of rights. With this
organization, all possible users of the system can share a public file or program without
the need for an entry for the object in the individual directory of each user.

Directory Access Lists Files
File “Star Lawl Rights BIBLIOG
BIBLIOG a   USER_A ORW
TEMP i USERB | R
2 users | RW —_—
ueterst | useR.A | ORW
F
USER_A ORW
users | R
USER_A R HELPTXT
USER_B R
USER_S R
USER_T R
SYSMGR | RW

USER_SVCS | O

FIGURE 2-13 Access Control List with Two Subjects

FI ICR AC KH
--- page 26 ---
Q4   [20]
CO-4
What are the logical components of IDS. Describe basic principle of IDS and desirable
SO-   a.   [10]
requirements for an IDS system.
BL-2
********** 26 **********

[Text in pictures on this page, read by OCR]
The Multics operating system used a form of access control list in which each user
belonged to three protection classes: a user, a group, and a compartment. The user
designation identified a specific subject, and the group designation brought together
subjects who had a common interest, such as their being coworkers on a project. The
compartment confined an untrusted object; a program executing in one compartment could
not access objects in another compartment without specific permission. The compartment
was also a way to collect objects that were related, such as all files for a single project.

To see how this type of protection might work, suppose every user who initiates access
to the system identifies a group and a compartment with which to work. If Adams logs in
as user Adams in group Decl and compartment Art2, only objects having Adams-Decl-
Art2 in the access control list are accessible in the session.

By itself, this kind of mechanism would be too restrictive to be usable. Adams cannot
create general files to be used in any session. Worse yet, shared objects would not only
have to list Adams as a legitimate subject but also have to list Adams under all acceptable
groups and all acceptable compartments for each group.

The solution is the use of wild cards, meaning placeholders that designate “any user”
(or “any group” or “any compartment”). An access control list might specify access by
Adams-Decl-Artl, giving specific rights to Adams if working in group Decl on
compartment Artl. The list might also specify Adams-*-Artl, meaning that Adams can
access the object from any group in compartment Artl. Likewise, a notation of *-Decl-*
would mean “any user in group Decl in any compartment.” Different placements of the
wildcard notation * have the obvious interpretations.

Unix uses a similar approach with user-group-world permissions. Every user belongs
to a group of related users—students in a common class, workers on a shared project, or
members of the same department. The access permissions for each object are a triple
(u,g,w) in which u is for the access rights of the user, g is for other members of the group,
and w is for all other users in the world.

The access control list can be maintained in sorted order, with * sorted as coming after
all specific names. For example, Adams-Decl-* would come after all specific
compartment designations for Adams. The search for access permission continues just
until the first match. In the protocol, all explicit designations are checked before wild
cards in any position, so a specific access right would take precedence over a wildcard
right. The last entry on an access list could be *-*-*, specifying rights allowable to any
user not explicitly on the access list. With this wildcard device, a shared public object can
have a very short access list, explicitly naming the few subjects that should have access
rights different from the default.
--- page 27 ---
Ans.

8.2 INTRUSION DETECTION

The following terms are relevant to our discussion:

security intrusion: Unauthorized act of bypassing the security mechanisms of a
system.

intrusion detection: A hardware or software function that gathers and analyzes
information from various areas within a computer or a network to identify possible
security intrusions.

An IDS comprises three logical components:

e Sensors: Sensors are responsible for collecting data. The input for a sensor may
be any part of a system that could contain evidence of an intrusion. Types of
input to a sensor includes network packets, log files, and system call traces.
Sensors collect and forward this information to the analyzer.

e Analyzers: Analyzers receive input from one or more sensors or from other ana-
lyzers. The analyzer is responsible for determining if an intrusion has occurred.
The output of this component is an indication that an intrusion has occurred.
The output may include evidence supporting the conclusion that an intrusion
occurred. The analyzer may provide guidance about what actions to take as a
result of the intrusion. The sensor inputs may also be stored for future analysis
and review in a storage or database component.

FR ICR D7 FAC KH
--- page 28 ---
¢ User interface: The user interface to an IDS enables a user to view output from
the system or control the behavior of the system. In some systems, the user
interface may equate to a manager, director, or console component.

An IDS may use a single sensor and analyzer, such as a classic HIDS on a host
or NIDS in a firewall device. More sophisticated IDSs can use multiple sensors, across
a range of host and network devices, sending information to a centralized analyzer
and user interface in a distributed architecture.

IDSs are often classified based on the source and type of data analyzed, as:

¢ Host-based IDS (HIDS): Monitors the characteristics of a single host and the
events occurring within that host, such as process identifiers and the system calls
they make, for evidence of suspicious activity.

¢ Network-based IDS (NIDS): Monitors network traffic for particular network
segments or devices and analyzes network, transport, and application protocols
to identify suspicious activity.

¢ Distributed or hybrid IDS: Combines information from a number of sensors,
often both host and network-based, in a central analyzer that is able to better
identify and respond to intrusion activity.

Basic Principles

Authentication facilities, access control facilities, and firewalls all play a role in coun-
tering intrusions. Another line of defense is intrusion detection, and this has been
the focus of much research in recent years. This interest is motivated by a number of
considerations, including the following:

1. If an intrusion is detected quickly enough, the intruder can be identified and
ejected from the system before any damage is done or any data are compro-
mised. Even if the detection is not sufficiently timely to preempt the intruder,
the sooner that the intrusion is detected, the less the amount of damage and
the more quickly that recovery can be achieved.

2. An effective IDS can serve as a deterrent, thus acting to prevent intrusions.

3. Intrusion detection enables the collection of information about intrusion tech-
niques that can be used to strengthen intrusion prevention measures.

Intrusion detection is based on the assumption that the behavior of the intruder
differs from that of a legitimate user in ways that can be quantified. Of course, we
cannot expect that there will be a crisp, exact distinction between an attack by an
intruder and the normal use of resources by an authorized user. Rather, we must
expect that there will be some overlap.

Figure 8.1 suggests, in abstract terms, the nature of the task confronting the
designer of an IDS. Although the typical behavior of an intruder differs from the typi-
cal behavior of an authorized user, there is an overlap in these behaviors. Thus, a loose
interpretation of intruder behavior, which will catch more intruders, will also lead to
a number of false positives, or false alarms, where authorized users are identified as
intruders. On the other hand, an attempt to limit false positives by a tight interpreta-
tion of intruder behavior will lead to an increase in false negatives, or intruders not

FI ICR 2 QA HH
--- page 29 ---
CO-3
Describe password-based authentication mechanism covering password vulnerability,
SO-   b.   [10]
attacks and reasons for the persistent popularity.
BL-2
********** 29 **********

[Text in pictures on this page, read by OCR]
Probability Profile of
density function authorized user
Profile of behavior

intruder behavior

Overlap in observed
or expected behavior

Average behavior Average behavior Measurable behavior
of intruder _of authorized user parameter

Figure 8.1 Profiles of Behavior of Intruders and Authorized Users

identified as intruders. Thus, there is an element of compromise and art in the practice
of intrusion detection. Ideally, you want an IDS to have a high detection rate, that is,
the ratio of detected to total attacks, while minimizing the false alarm rate, the ratio
of incorrectly classified to total normal usage [LAZA05].

In an important early study of intrusion [ANDE80], Anderson postulated that
one could, with reasonable confidence, distinguish between an outside attacker and a
legitimate user. Patterns of legitimate user behavior can be established by observing
past history, and significant deviation from such patterns can be detected. Anderson
suggests the task of detecting an inside attacker (a legitimate user acting in an unau-
thorized fashion) is more difficult, in that the distinction between abnormal and
normal behavior may be small. Anderson concluded that such violations would be
undetectable solely through the search for anomalous behavior. However, insider
behavior might nevertheless be detectable by intelligent definition of the class of
conditions that suggest unauthorized use. These observations, which were made in
1980, remain true today.

Requirements
[BALA9§] lists the following as desirable for an IDS. It must:

e Run continually with minimal human supervision.

¢ Be fault tolerant in the sense that it must be able to recover from system crashes
and reinitializations.

¢ Resist subversion. The IDS must be able to monitor itself and detect if it has
been modified by an attacker.

¢ Impose a minimal overhead on the system where it is running.

¢ Be able to be configured according to the security policies of the system that
is being monitored.

© Be able to adapt to changes in system and user behavior over time.
¢ Be able to scale to monitor a large number of hosts.

¢ Provide graceful degradation of service in the sense that if some components
of the IDS stop working for any reason, the rest of them should be affected as
little as possible.

¢ Allow dynamic reconfiguration; that is, the ability to reconfigure the IDS with-
out having to restart it.
--- page 30 ---
Ans.

3.2 PASSWORD-BASED

HENTIC.

ON

A widely used line of defense against intruders is the password system. Virtually all
multiuser systems, network-based servers, Web-based e-commerce sites, and other
similar services require that a user provide not only a name or identifier (ID) but also
a password. The system compares the password to a previously stored password for
that user ID, maintained in a system password file. The password serves to authen-
ticate the ID of the individual logging on to the system. In turn, the ID provides
security in the following ways:

e The ID determines whether the user is authorized to gain access to a system.
In some systems, only those who already have an ID filed on the system are
allowed to gain access.

e The ID determines the privileges accorded to the user. A few users may have
administrator or “superuser” status that enables them to read files and perform
functions that are especially protected by the operating system. Some systems
have guest or anonymous accounts, and users of these accounts have more
limited privileges than others.

¢ The ID is used in what is referred to as discretionary access control. For exam-
ple, by listing the IDs of the other users, a user may grant permission to them
to read files owned by that user.

The Vulnerability of Passwords

In this subsection, we outline the main forms of attack against password-based
authentication and briefly outline a countermeasure strategy. The remainder of
Section 3.2 goes into more detail on the key countermeasures.

Typically, a system that uses password-based authentication maintains a pass-
word file indexed by user ID. One technique that is typically used is to store not the
user’s password but a one-way hash function of the password, as described subsequently.

We can identify the following attack strategies and countermeasures:

© Offline dictionary attack: Typically, strong access controls are used to protect
the system’s password file. However, experience shows that determined hack-
ers can frequently bypass such controls and gain access to the file. The attacker
obtains the system password file and compares the password hashes against

FIR ICR QQ) A HH
--- page 31 ---
hashes of commonly used passwords. If a match is found, the attacker can gain
access by that ID/password combination. Countermeasures include controls to
prevent unauthorized access to the password file, intrusion detection measures
to identify a compromise, and rapid reissuance of passwords should the pass-
word file be compromised.

Specific account attack: The attacker targets a specific account and submits
password guesses until the correct password is discovered. The standard coun-
termeasure is an account lockout mechanism, which locks out access to the
account after a number of failed login attempts. Typical practice is no more
than five access attempts.

Popular password attack: A variation of the preceding attack is to use a popu-
lar password and try it against a wide range of user IDs. A user’s tendency is
to choose a password that is easily remembered; this unfortunately makes the
password easy to guess. Countermeasures include policies to inhibit the selec-
tion by users of common passwords and scanning the IP addresses of authenti-
cation requests and client cookies for submission patterns.

Password guessing against single user: The attacker attempts to gain knowl-
edge about the account holder and system password policies and uses that
knowledge to guess the password. Countermeasures include training in and
enforcement of password policies that make passwords difficult to guess. Such
policies address the secrecy, minimum length of the password, character set,
prohibition against using well-known user identifiers, and length of time before
the password must be changed.

Workstation hijacking: The attacker waits until a logged-in workstation is unat-
tended. The standard countermeasure is automatically logging the workstation
out after a period of inactivity. Intrusion detection schemes can be used to
detect changes in user behavior.

Exploiting user mistakes: If the system assigns a password, then the user is
more likely to write it down because it is difficult to remember. This situation
creates the potential for an adversary to read the written password. A user may
intentionally share a password, to enable a colleague to share files, for example.
Also, attackers are frequently successful in obtaining passwords by using social
engineering tactics that trick the user or an account manager into revealing a
password. Many computer systems are shipped with preconfigured passwords
for system administrators. Unless these preconfigured passwords are changed,
they are easily guessed. Countermeasures include user training, intrusion detec-
tion, and simpler passwords combined with another authentication mechanism.

Exploiting multiple password use: Attacks can also become much more effec-
tive or damaging if different network devices share the same or a similar pass-
word for a given user. Countermeasures include a policy that forbids the same
or similar password on particular network devices.

Electronic monitoring: If a password is communicated across a network to log
on to a remote system, it is vulnerable to eavesdropping. Simple encryption will
not fix this problem, because the encrypted password is, in effect, the password
and can be observed and reused by an adversary.

FR ICR QI OH
--- page 32 ---
Despite the many security vulnerabilities of passwords, they remain the most
commonly used user authentication technique, and this is unlikely to change in the
foreseeable future [HERL12]. Among the reasons for the persistent popularity of
passwords are the following:

1. Techniques that utilize client-side hardware, such as fingerprint scanners and
smart card readers, require the implementation of the appropriate user authen-
tication software to exploit this hardware on both the client and server systems.
Until there is widespread acceptance on one side, there is reluctance to imple-
ment on the other side, so we end up with a who-goes-first stalemate.

2. Physical tokens, such as smart cards, are expensive and/or inconvenient to carry
around, especially if multiple tokens are needed.

3. Schemes that rely on a single sign-on to multiple services, using one of the non-
password techniques described in this chapter, create a single point of security risk.

4, Automated password managers that relieve users of the burden of knowing and
entering passwords have poor support for roaming and synchronization across
multiple client platforms, and their usability had not be adequately researched.

Thus, it is worth our while to study the use of passwords for user authentication
in some detail.

Q5 [20]
CO-2

SO- a. Write short note on business continuity planning. [10]
BL-2

BUSINESS CONTINUITY PLANNING

MM The key to coping with such disasters is advance planning and
preparation, identifying activities that will keep a business viable

when the computing technology is disabled.

Wl The steps in business continuity planning are these:
© Assess the business impact of a crisis.
© Develop a strategy to control impact.

Ans.
© Develop and implement a plan for the strategy

BUSINESS CONTINUITY PLANNING - Assess Business Impact

ll Begin by asking two key questions:

Hl What are the essential assets? What are the things that will prevent

the business from doing business?

Hi What could disrupt use of these assets? The vulnerability is more

important than the threat agent.

FOI III 39 FC CR Ir
--- page 33 ---
BUSINESS CONTINUITY PLANNING - Develop Strategy

Ml The continuity strategy investigates how the key assets can be
safeguarded.
© In some cases, a backup copy of data or redundant hardware or
an alternative manual process is good enough.
© Sometimes, the most reasonable answer is reduced capacity.

Hl The result of a strategy analysis is a selection of the best actions,
organized by circumstances.

Ml The strategy can then be used as the basis for your business
continuity plan

BUSINESS CONTINUITY PLANNING - Develop Plan

ll The business continuity plan specifies several important things:
© whois in charge when an incident occurs
© what to do
© who does it

WM The plan justifies making advance arrangements, such as acquiring
redundant equipment, arranging for data backups, and stockpiling
supplies, before the catastrophe.

WM The plan also justifies advance training so that people know how they
should react.

BUSINESS CONTINUITY PLANNING = Incident Response Plans

i An incident response plan tells the staff how to deal with a
security incident.

I In contrast to the business continuity plan, the goal of incident
response is handling the current security incident, without regard for
the business issues.

I An incident response plan
© should define what constitutes an incident
© identify who is responsible for taking charge of the situation
©. describe the plan of action

FOI 32 FC ICR Ir
--- page 34 ---
BUSINESS CONTINUITY PLANNING

The plan usually has three phases:
HM Advance planning,

Wl Triage

Wi running the incident.

Hf A fourth phase, review, is useful after the situation abates so that this

incident can lead to improvement for future incident

BUSINESS CONTINUITY PLANNING

i Advance Planning

WM Advance planning works best because people can think logically,
unhurried, and without pressure.

i Response Team
© Director: person in charge of the incident, who decides what
actions to take and when to terminate the response.
© Lead technician: person who directs and coordinates the
response.
© Advisor(s): legal, human resources, or public relations staff
members as appropriate.

BUSINESS CONTINUITY PLANNING - Response Team

Hi Need to consider certain matters.

I Legal issues: An incident has legal ramifications.
HB Preserving evidence:

HB Records:

WH Public relations:

FOI FC ICR
--- page 35 ---
CO-3   Explain symmetric key encryption and issues related to key sharing. Also, explain
SO-   b.   with the help of a diagram the working of public-key certificate and digital envelope   [10]
BL-2   techniques for key sharing.
********** 35 **********

[Text in pictures on this page, read by OCR]
BUSINESS CONTINUITY PLANNING

ll After the Incident Is Resolved

I Eventually, the incident response team closes the case.

I At this point it will hold a review after the incident to consider two
things:

i Js any security control action to be taken?

I Did the incident response plan work?
--- page 36 ---
Ans.

Public-Key Certificates

On the face of it, the point of public-key encryption is that the public key is pub-
lic. Thus, if there is some broadly accepted public-key algorithm, such as RSA, any
participant can send his or her public key to any other participant or broadcast the
key to the community at large. Although this approach is convenient, it has a major
weakness. Anyone can forge such a public announcement. That is, some user could
pretend to be Bob and send a public key to another participant or broadcast such a
public key. Until such time as Bob discovers the forgery and alerts other participants,
the forger is able to read all encrypted messages intended for A and can use the
forged keys for authentication.

The solution to this problem is the public-key certificate. In essence, a certifi-
cate consists of a public key plus a user ID of the key owner, with the whole block
signed by a trusted third party. The certificate also includes some information about
the third party plus an indication of the period of validity of the certificate. Typically,
the third party is a certificate authority (CA) that is trusted by the user commu-
nity, such as a government agency or a financial institution. A user can present his
or her public key to the authority in a secure manner and obtain a signed cert
cate. The user can then publish the certificate. Anyone needing this user’s public key
can obtain the certificate and verify that it is valid by means of the attached trusted
signature. Figure 2.8 illustrates the process.

Bob's ID
information
Unsigned certificate:
contains user ID.

Recipient can verify
: : signature by comparing
information hash code values

WD Er —-_-Grypy

Generate hasll
code of unsigned

Signed certificate

Encrypt hash code Decrypt signature
with CA's private key with CA's public key
to form signature to recover bash code
— _ — _
en ee
Create signed Use certificate ti
digital certificate verify Bob's public key

Figure 2.8 Publie-Key Certificate Use

FR ICR RG IC HH
--- page 37 ---
One scheme has become universally accepted for formatting public-key
tes: the X.509 standard. X.509 certificates are used in most network security
ions, including IP Security (IPsec), Transport Layer Security (TLS), Secure
Shell (SSH), and Secure/Multipurpose Internet Mail Extension (S/MIME). We
examine most of these applications in Part Five.

Symmetric Key Exchange Using Public-Key Encryption

With symmetric encryption, a fundamental requirement for two parties to communi-
cate securely is that they share a secret key. Suppose Bob wants to create a messag-
ing application that will enable him to exchange e-mail securely with anyone who has
access to the Internet or to some other network that the two of them share. Suppose
Bob wants to do this using symmetric encryption. With symmetric encryption, Bob
and his correspondent, say, Alice, must come up with a way to share a unique secret
key that no one else knows. How are they going to do that? If Alice is in the next
room from Bob, Bob could generate a key and write it down on a piece of paper or
store it. ona disc or thumb drive and hand it to Alice. But if Alice is on the other side
of the continent or the world, what can Bob do? He could encrypt this key using
symmietric encryption and ¢-mail it to Alice, but this means that Bob and Alice must
share a secret key to encrypt this new secret key. Furthermore, Bob and everyone
else who uses this new e-mail package faces the same problem with every potential
correspondent: Each pair of correspondents must share a unique secret key.

One approach is the use of Diffie-Hellman key exchange. This approach is
indeed widely used. However, it suffers the drawback that, in its simplest form,
Diffie-Hellman provides no authentication of the two communicating partners.
There are variations to Diffie-Hellman thal overcome this problem. Also, there are
protocols using other public-key algorithms that achieve the same objective.

Digital Envelopes

Another application in which public-key encryption is used to protect a symmetric
key is the digital envelope, which can be used to protect a message without need-
ing to first arrange for sender and receiver to have the same secret key. The tech-
nique is referred to as a digital envelope, which is the equivalent of a sealed envelope
containing an unsigned letter. The general approach is shown in Figure 2.9. Suppose
Bob wishes to send a confidential message to Alice, but they do not share a symmet-
ric secret key. Bob does the following:
1. Prepare a message.
2. Generate a random symmetric key that will be used this one time only.
3. Encrypt that message using symmetric encryption the one-time key.
4, Encrypt the one-time key using public-key encryption with Alice’s public key.
§. Attach the encrypted one-time key to the encrypted message and send it to
Alice.
Only Alice is capable of decrypting the one-time key and therefore of recov-
ering the original message. If Bob obtained Alice’s public key by means of Alice’s
public-key certificate, then Bob is assured that it is a valid key.

FR ICR QA OH
--- page 38 ---
Message : : ee es

Encrypted

message
Random eo

symmeuic & |

. | (\. Som _— Digital
envelope
E pi

Receiver’s Enerypted
. symmetric

public a) sy

key key

(a) Creation of a digital envelope

stent atanahe a D \ Message

sata! aatate!
Encrypted
Message Random
~~ eo O= symmetric
~~. { \ 7
Digital }
envelope Gove D
Encrypted } iar
symmetric
y O=7 key

key

(b) Opening a digital envelope

Figure 2.9 Digital Envelopes

Q6 [20]
Co-1

SO- a. List and briefly define the fundamental security design principles. [10]
BL-1

FIR ICR QA HH
--- page 39 ---
Design Principles

> Principle of least privilege

> Principle of Fail-Safe Defaults

> Principle of Economy of Mechanism

> Principle of Complete Mediation

> Principle of Open Design

> Principle of Separation of privilege

> Principle of least common mechanism

> Principle of Psychological acceptability

Ans. ar °
Principle of Least Principle of Fail-Safe
Privilege Defaults.

> . a > Restricts how privileges are initialized
Restricts how privileges are granted when a subject or object is created

> “a subject should be given only those >
privilege that it needs in order to
complete its task”

“The principle of Fail-Safe defaults states

that, unless a subject is given explicit

access to an object, it should be denied

access to that object”

> If a specific action requires that a
subject’s access rights be augmented, >
those extra rights be relinquished
immediately on completion of the action.

This principle requires that the default
access to an object is none

Principle of Complete
Mediation

> Simplifies the design and implementation > this principle restricts the caching of
of security mechanisms information, which often leads to simpler
implementations of mechanisms

> “the principle of economy of mechanism
states that security mechanism should be > “The principle of complete mediation
as simple as possible” requires that all accesses to objects be
checked to ensure that they are allowed”

> If a design and implementations are
simple, fewer possibilities exist for errors > ifthe subject tries to read a resource again.
and _again, the system should check that the
subject is still allowed to read the object

FOI 3.0 FC CR
--- page 40 ---
CO-4
Explain now SIEM is a comprehensive approach to manage and analyse security
SO-   b.   [10]
events in an information technology environment.
BL-2
Ans.
********** 40 **********

[Text in pictures on this page, read by OCR]
Principle of Open Design Principle of Separation of
privilege
> The principle suggests that complexity
does not add security > This principle is restrictive because it

> “The principle of open design states that limits access to system entities

the security of a mechanism should not > The principle of separation of privilege
depend on the secrecy of its design or states that a system should not grant
implementation” permission based on single condition”
> Designers of a program must not depend > Company checks for more than $75,000
on secrecy of the details of their design must be signed by two officers of the
and implementation to ensure security company. If either does not sign, the check
> ithe stren gth of the program’s security is not valid. The two conditions are the

depends on the ignorance of the user, a signatures of two officers

knowledgeable user can defeat that
security mechanism

Principle of Psychological
acceptability

> this principle recognizes the human

> this principle is restrictive because it element in computer security

limits sharing > “The Principle of psychological
acceptability states that security
> The principle of least common mechanism should not make the resource
mechanism states that mechanisms used more difficult to access than if the security
to access resources should not be shared” mechanisms were not present”

> if security related software is too
complicated to configure, system
administrators may unintentionally set up
software in a non secure manner, security-
related user programs must be easy to use
and must output understandable messages

> Sharing resources provides a channel
along which information can be
transmitted, and so such sharing should
be minimized

Security Information and Event
Management

- SIEM, which stands for Security Information and Event Management, is a
comprehensive approach to managing and analyzing security events within an
information technology (IT) environment. SIEM systems collect and aggregate log data
generated throughout the organization's technology infrastructure, from host systems
and applications to network and security devices. The primary goal of SIEM is to
provide a centralized platform for real-time analysis of security alerts and events,

aiding in the detection of security incidents.
--- page 41 ---
Security Information and Event
Management

Components of SIEM

» Data Collection - SIEM systems collect log and event data from various sources across the IT
environment, such as firewalls, intrusion detection/prevention systems, servers, endpoints, and
applications.

» Log Management - SIEM platforms store and manage log data in a centralized repository. Logs are
indexed and normalized for easy searching and analysis.

» Normalization and Correlation Engine - Normalization standardizes log data from different
sources, making it consistent and understandable. The correlation engine identifies patterns and

relationships between seemingly unrelated events to detect potential security incidents.

Security Information and Event
Management

Components of SIEM

» Alerting and Notification - SIEM systems generate alerts and notifications based on predefined
rules and correlation logic. Security analysts are notified of potential security incidents that require
investigation.

» Dashboards and Reporting - SIEM solutions provide dashboards and reporting tools to present
summarized and detailed information about security events, trends, and incidents. Customizable
dashboards help security teams monitor key metrics.

» Incident Response - SIEM facilitates incident response by providing tools for investigation,
forensics, and tracking the lifecycle of security incidents. It helps security teams understand the

nature and scope of incidents and take appropriate actions.

Security Information and Event |
Management

Components of SIEM
» User and Entity Behavior Analytics (UEBA) - Some SIEM systems incorporate UEBA capabilities
to detect abnormal behavior patterns that may indicate insider threats or compromised accounts.

> Compliance Management - SIEM platforms assist in meeting regulatory compliance requirements
by providing reports and audit trails. They help organizations demonstrate adherence to security

policies and standards.

FIR IC 77 FIC HOH
--- page 42 ---
Security Information and Event
Management

Workflow of SIEM

» Data Collection - Log and event data is collected from various sources, including security devices,

servers, applications, and network infrastructure.

> Normalization - Raw log data is normalized to a consistent format, making it easier to analyze and

correlate events across different sources.

» Correlation - Correlation engines analyze normalized data to identify patterns and relationships

between events. This helps in detecting complex security incidents.

» Alerting - Alerts are generated based on predefined rules and correlation logic. Security teams are

notified of potential security incidents.

Security Information and Event
Management

Workflow of SIEM

» Investigation - Security analysts investigate alerts, using dashboards, reports, and analysis tools to
understand the context and severity of the incidents.
» Incident Response - Based on the investigation, security teams initiate incident response

procedures to contain, eradicate, and recover from security incidents.

» Reporting - SIEM platforms provide detailed reports and dashboards for ongoing monitoring,

compliance reporting, and management visibility.

Q7 [20]
CO-2

SO- a. Explain the concept of incomplete mediation in depth. [10]
BL-2

Incomplete Mediation

Mediation means checking: the process of intervening to confirm an actor’s
authorization before it takes an intended action. In the last chapter we discussed the steps
and actors in the authentication process: the access control triple that describes what
subject can perform what operation on what object. Verifying that the subject is authorized

Ans. to perform the operation on an object is called mediation. Incomplete mediation is a
security problem that has been with us for decades: Forgetting to ask “Who goes there?”
before allowing the knight across the castle drawbridge is just asking for trouble. In the
same way, attackers exploit incomplete mediation to cause security problems.

Definition

Consider the following URL. In addition to a web address, it contains two parameters,

FIR ICR 7 AC HOEK
--- page 43 ---
so you can think of it as input to a program:
Click} . ici

http://www. somesite.com/subpage/user input .asp?
parmi=(808)555-12124parm2=2015Jan17
As a security professional trying to find and fix problems before they occur, you might
examine the various parts of the URL to determine what they mean and how they might be
exploited. For instance, the parameters parm1 and parm2 look like a telephone number
and a date, respectively. Probably the client’s (user’s) web browser enters those two values
in their specified format for easy processing on the server’s side.

But what would happen if parm2 were submitted as 1800Jan01? Or 1800Feb30? Or
2048Min32? Or 1Aardvark2Many? Something in the program or the system with which it
communicates would likely fail. As with other kinds of programming errors, one
possibility is that the system would fail catastrophically, with a routine’s failing on a data
type error as it tried to handle a month named “Min” or even a year (like 1800) that was
out of expected range. Another possibility is that the receiving program would continue to
execute but would generate a very wrong result. (For example, imagine the amount of
interest due today on a billing error with a start date of 1 Jan 1800.) Then again, the
processing server might have a default condition, deciding to treat 1Aardvark2Many as 21
July 1951. The possibilities are endless.

A programmer typically dismisses considering bad input, asking why anyone would
enter such numbers. Everybody knows there is no 30th of February and, for certain
applications, a date in the 1800s is ridiculous. True. But ridiculousness does not alter
human behavior. A person can type 1800 if fingers slip or the typist is momentarily
distracted, or the number might have been corrupted during transmission. Worse, just
because something is senseless, stupid, or wrong doesn’t prevent people from doing it.
And if a malicious person does it accidentally and finds a security weakness, other people
may well hear of it. Security scoundrels maintain a robust exchange of findings. Thus,
programmers should not assume data will be proper; instead, programs should validate
that all data values are reasonable before using them.

Users make errors from ignorance, misunderstanding, distraction; user
errors should not cause program failures.

Validate All Input

One way to address potential problems is to try to anticipate them. For instance, the
programmer in the examples above may have written code to check for correctness on the
client’s side (that is, the user’s browser). The client program can search for and screen out
errors. Or, to prevent the use of nonsense data, the program can restrict choices to valid
ones only. For example, the program supplying the parameters might have solicited them
by using a drop-down box or choice list from which only the twelve conventional months
could have been selected. Similarly, the year could have been tested to ensure a reasonable
value (for example, between 2000 and 2050, according to the application) and date
numbers would have to be appropriate for the months in which they occur (no 30th of
February, for example). Using such verification, the programmer may have felt well

FIR ICR 72 FIC HOH
--- page 44 ---
insulated from the possible problems a careless or malicious user could cause.
Guard Against Users’ Fingers

However, the application is still vulnerable. By packing the result into the return URL,
the programmer left these data fields in a place where the user can access (and modify)
them. In particular, the user can edit the URL line, change any parameter values, and send
the revised line. On the server side, the server has no way to tell if the response line came
from the client’s browser or as a result of the user’s editing the URL directly. We say in
this case that the data values are not completely mediated: The sensitive data (namely, the
parameter values) are in an exposed, uncontrolled condition.

Unchecked data values represent a serious potential vulnerability. To demonstrate this
flaw’s security implications, we use a real example; only the name of the vendor has been
changed to protect the guilty. Things, Inc., was a very large, international vendor of
consumer products, called Objects. The company was ready to sell its Objects through a
web site, using what appeared to be a standard e-commerce application. The management
at Things decided to let some of its in-house developers produce a web site with which its
customers could order Objects directly from the web.

To accompany the web site, Things developed a complete price list of its Objects,
including pictures, descriptions, and drop-down menus for size, shape, color, scent, and
any other properties. For example, a customer on the web could choose to buy 20 of part
number 555A Objects. If the price of one such part were $10, the web server would
correctly compute the price of the 20 parts to be $200. Then the customer could decide
whether to have the Objects shipped by boat, by ground transportation, or sent
electronically. If the customer were to choose boat delivery, the customer’s web browser
would complete a form with parameters like these:

Click here to view code image
http://www. things. com/order .asp?cust ID=101&part=555A
&qy=20&price=10&ship=boat&shipcost=5atotal=205
So far, so good; everything in the parameter passing looks correct. But this procedure
leaves the parameter statement open for malicious tampering. Things should not need to
pass the price of the items back to itself as an input parameter. Things presumably knows
how much its Objects cost, and they are unlikely to change dramatically since the time the
price was quoted a few screens earlier.

There is no reason to leave sensitive data under control of an untrusted
user.

A malicious attacker may decide to exploit this peculiarity by supplying instead the
following URL, where the price has been reduced from $205 to $25:
Click} . ici

http://www. things .com/order .asp?cust ID=101par t=555A
&qy=20&price=1&ship=boat&shipcost=Satotal=25

Surprise! It worked. The attacker could have ordered Objects from Things in any
quantity at any price. And yes, this code was running on the web site for a while before

FIR ICR 7) I ROK HH
--- page 45 ---
the problem was detected.

From a security perspective, the most serious concern about this flaw was the length of
time that it could have run undetected. Had the whole world suddenly made a rush to
Things’ web site and bought Objects at a fraction of their actual price, Things probably
would have noticed. But Things is large enough that it would never have detected a few
customers a day choosing prices that were similar to (but smaller than) the real price, say,
30 percent off. The e-commerce division would have shown a slightly smaller profit than
other divisions, but the difference probably would not have been enough to raise anyone’s
eyebrows; the vulnerability could have gone unnoticed for years. Fortunately, Things hired
a consultant to do a routine review of its code, and the consultant quickly found the error.

The vulnerability in this situation is that the customer (computer user) has unmediated
access to sensitive data. An application running on the user’s browser maintained the order
details but allowed the user to change those details at will. In fact, few of these values
should have been exposed in the URL sent from the client’s browser to the server. The
client’s application should have specified part number and quantity, but an application on
the server’s side should have returned the price per unit and total price.

If data can be changed, assume they have been.

This web program design flaw is easy to imagine in other settings. Those of us
interested in security must ask ourselves, How many similar problems are in running code
today? And how will those vulnerabilities ever be found? And if found, by whom?

Complete Mediation

Because the problem here is incomplete mediation, the solution is complete mediation.
Remember from Chapter 2 that one of our standard security tools is access control,
sometimes implemented according to the reference monitor concept. The three properties
of a reference monitor are (1) small and simple enough to give confidence of correctness,
(2) unbypassable, and (3) always invoked. These three properties combine to give us solid,
complete mediation.

Co-1

Describe the NIST SP 800-35 security life cycle phases.

SO- b. [10]

BL-2

Explanation with example

NIST SP 800-35 Security Life Cycle

» Phase 1: Initiation : At this point the organisation is looking into implementing some IT security
service, device, or process.
Ans » Phase 2: Assessment : This phase involves determining and describing the organization's current
. security posture. It is recommended that this phase use quantifiable metrics.
» Phase 3: Solution : This is where various solutions are evaluated and one or more are selected.
» Phase 4: Implementation : In this phase the IT security service, device, or process is
implemented.

» Phase 5: Operations : Phase 5 is the ongoing operation and maintenance of the security service,
device, or process that was implemented in phase 4.

» Phase 6: Closeout : At some point, whatever was implemented in phase 4 will be concluded. Often
this is when a system is replaced by a newer and better system

FRAC 7D AC HOH
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper b91854c1e6aa

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CSBS_7036/Information Security/ANS_Information Security(702CO0C036)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: mixed (60 pages), mean OCR confidence 94.0
- 4 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Information Security
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 60 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of the remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q1   Answer briefly:   [20]
CO-1
SO-   a.   What is a threat. Explain different types of threats.   [5]
BL-2
Ans.
********** 1 **********

[Text in pictures on this page, read by OCR]
Threats

» A threat is a potential for violation of security or a possible danger that might exploit

vulnerability.

> In other words a threat is a set of activity that has ability to cause harm. The threat
can be either generated by Human or Computer.
» Threat is purposely created by an attacker to attack on the system. In other words, an

exploitation of vulnerability is attack on the system.

» There are four kinds of threats possible: Interception, Interruption, Modification,

and Fabrication.
--- page 2 ---
CO-2
SO-   b.   List the various types of malicious code and their functions.   [5]
BL-1
Ans.
CO-3
SO-   c.   What do you mean by identity on the web?   [5]
BL-2
********** 2 **********

[Text in pictures on this page, read by OCR]
Types of Threats

» Threats - A threat is a potential for violation of security or a possible danger that might exploit

vulnerability.
Interruption qi nterception Fabrication
> in interruption. » Interception is > in modification, > in fabrication,
the data may be keeping track of data is modified in attacker might
lost or traffic without some way. ; hide his own
unavailable due modification. In Receiver doesn’t identity and can
to some other words, some have any , send the data to
unauthorized unauthorized , knowledge of this receiver from
system has gained modification some trusted
Party access to an asset. host.

e- ee, @ @6°

MALICIOUS PROGRAM ERRORS

TYPES OF FUNCTION
MALICIOUS CODE

Virus Code that attaches to another program and copies itself to other programs.
* Transient virus — life depends on life of its host
+ Resident virus — locates inside memory

Trojan Horse malicious effect is hidden from user (Ex: login script)

Logic viruses triggered by an event and goes off when specific condition occur

Time viruses triggered by a time or date

Trapdoor (backdoor) feature that allows access to program other than through normal channels

Worm program that spreads copies of itself through a network, can be stand alone program
Rabbit virus/worm that self-replicates without bound. Ove: e, So many copies of Rabbit

would be running that it would clog the system, making it run slow and making it
more difficult to remove the program.
--- page 3 ---
Ans.

15.6 Identity on the Web

Certificates are not ubiquitous on the Internet. Several other means attach identity
to information, even though the binding may be very transient.

The Internet requires every host to have an address. The address may be
fixed or may change, and without cryptography the binding is weak. Many servers
send information about the state of the client’s interaction, so that when the client
reconnects, the server can resume the transaction or glean information about
previous transactions.

15.6.1. Host Identity

Host identity is intimately bound to networking. A host not connected to any
network can have any name, because the name is used only locally. A host
connected to a network can have many names or one name, depending on how
the interface to the network is structured and the context in which the name is
used.

The ISO/OSI model [1859] provides a context for the issue of naming.
Figure 12-6 shows the layers of the ISO/OSI model. Each host, conceptually, has
a principal at each layer that communicates with a peer on other hosts. These
principals communicate with principals at the same layer on other hosts. Each

principal on an individual host can have different names (also called “addresses”)
at each layer. All names identify the same host, but each one refers to a particular
context in which the host functions.

EXAMPLE: A computer has an Ethernet (media access control layer, or MAC)
address of 00:05:02:6B:A8:21, an IP address of 192.168.35.89, and a host name
of cherry.orchard.net, At the data link level, the system is known by its Ethernet
address. At the network level, it is known by its IP address. At the application level,
it is known by its host name. The system is also on an AppleTalk network, with
an AppleTalk address of network 51, node 235. Other systems on the AppleTalk
network identify the host by that name.

Shoch [1740] suggests that a “name” identifies a principal and an “address”
identifies where that principal is located. In the context of host identification, the
“address” indicates where on a network (and, sometimes, the specific network)
the host is located. A “name” indicates in what domain the host resides, and
corresponds to a particular address. Although Shoch’s terminology is instructive
in many contexts, in this context a location identifies a principal just as well as a
name. We do not distinguish between the two in the context of identification.

If an attacker is able to spoof the identity of another host, all protocols
that rely on that identity are relying on a faulty premise and are therefore being
spoofed. When a host has a sequence of names, each relying on the preceding
name, then an attacker spoofing the first identity can compromise all the other
identities. For example, the host identity is based on the IP identity. Similarly,
the IP identity is based on the Ethernet identity. If an attacker can alter entries
in databases containing the mapping of a lower-level identity to a higher-level
identity, the attacker can spoof one host by routing traffic to another.

15.6.1.1. Static and Dynamic Identifiers

An identifier can be either static or dynamic. A static identifier does not change
over time; a dynamic identifier changes either as a result of an event (such as a
connection to a network) or over time.

Databases contain mappings between different names. The best known of
these is the Domain Name Service (DNS) [1365, 1366], which associates host
names and IP addresses. In the absence of cryptographic authentication of hosts,
the consistency of the DNS is used to provide weak authentication.

EXAMPLE: The DNS contains forward records, which map host names into IP
addresses, and reverse records, which map IP addresses into names. A reverse
domain lookup occurs when a process extracts the IP address of its remote peer,
determines the associated host name (perhaps using the DNS), and then obtains
the set of IP addresses associated with that host name (again, possibly using the
DNS). If the IP address obtained from the peer matches any of the IP addresses
associated with that host name, then the host name is accepted as the one obtained
in the first lookup. Otherwise, the host name is rejected as untrusted.

FC QI a iar
--- page 4 ---
The belief in the trustworthiness of the host name in this case relies on the
integrity of the DNS database. Section 15.6.1.2, “Security Issues with the Domain
Name Service,” examines this issue.

Floating identifiers are assigned to principals for a limited time. Typically,
a server maintains a pool of identifiers. A client contacts the server using an
identifier agreed on between the two (the /ocal identifier). The server transmits
an identifier that the client can use in other contexts (the global identifier) and
notifies any intermediate hosts (such as gateways) of the association between the
local and global identifiers.

EXAMPLE: Bootless University provides a network to which students can hook
up laptops. Rather than assign each student laptop an IP address, the university
has created a DHCP server [589, 590] for this network. When a student connects
her laptop to the network, the laptop transmits its MAC address to the server. The
server responds with an unused IP address belonging to the network. The laptop
accepts that IP address and uses it to communicate on the Internet.

A gateway can translate between a local address and a global address.

EXAMPLE: The Zerbche company has 500 computers on a local area network, but
only 256 Internet addresses. The internal network assigns as (fixed) local addresses
the IP addresses 10.1.x.y, where x and y reflect internal configuration details not
relevant here. A gateway connects the internal network to the Internet.

When a user at host 10.1.3.241 wants to access the Internet, it forwards its
packets to the gateway. The gateway assigns a legitimate IP address to the internal,
local address; say that IP address is 101.43.21.241. The gateway then rewrites the
source address of each packet, changing 10.1.3.241 to 101.43.21.241, and puts the
packets out on the Internet. When the gateway receives packets destined for host
101.43.21.241, it checks its internal table, rewrites those addresses as 10.1.3.241,
and forwards them to the internal network, and the packets go to their destination.
This translation is invisible to either end of the communication, and enables up
to some number of hosts on the internal network to communicate with hosts on
the Internet. The Network Address Translation protocol (NAT) [1806] is used on
the Internet to perform this function.

In the absence of cryptography, authentication using dynamic naming is
different from authentication using static naming. The primary problem is that the
association of the identity with a principal varies over time, so any authentication
based on the name must also account for the time. For example, if the DNS record
entries corresponding to the dynamic name are not updated whenever the name
is reassigned, the reverse domain lookup method of authentication fails.’

COo-3

SO- d. Discuss the security features of ordinary Operating System. [5]

BL-2

FIC 7) IC HOH
--- page 5 ---
Ans.

Security Features of Ordinary Operating Systems

A multiprogramming operating system performs several functions that relate to security.
To see how, examine Figure 5-1, which illustrates how an operating system interacts with
users, provides services, and allocates resources.

Users

Ty

User Interface
| | | Synchronization,
Concurrency
- Control, Deadlock
Operating Services Manageme!

System :

Communic:

rs

Accounting

——_—_,,

EU To =| S35

Memory

OO

Program
Libraries

V/O Devices
FIGURE 5-1 Operating System Functions

We can see that the system addresses several particular functions that involve computer
security:

+ Enforced sharing. Resources should be made available to users as appropriate.
Sharing brings about the need to guarantee integrity and consistency. Table
lookup, combined with integrity controls such as monitors or transaction
processors, is often used to support controlled sharing.

+ Interprocess communication and synchronization. Executing processes
sometimes need to communicate with other processes or to synchronize their
accesses to shared resources. Operating systems provide these services by acting
as a bridge between processes, responding to process requests for asynchronous
communication with other processes or synchronization. Interprocess
communication is mediated by access control tables.

+ Protection of critical operating system data. The operating system must
maintain data by which it can enforce security. Obviously, if these data are not
protected against unauthorized access (read, modify, and delete), the operating
system cannot provide enforcement. Various techniques (including encryption,
hardware control, and isolation) support protection of operating system security
data.

FIC DI EH ar
--- page 6 ---
* Guaranteed fair service. All users expect CPU usage and other service to be
provided so that no user is indefinitely starved from receiving service. Hardware
clocks combine with scheduling disciplines to provide fairness. Hardware
facilities and data tables combine to provide control.

+ Interface to hardware. All users access hardware functionality. Fair access and
controlled sharing are hallmarks of multitask operating systems (those running
more than one task concurrently), but a more elementary need is that users
require access to devices, communications lines, hardware clocks, and
processors. Few users access these hardware resources directly, but all users
employ such things through programs and utility functions. Hardware interface
used to be more tightly bound into an operating system’s design; now, however,
operating systems are designed to run on a range of hardware platforms, both to
maximize the size of the potential market and to position the operating system
for hardware design enhancements.

+ User authentication. The operating system must identify each user who
requests access and must ascertain that the user is actually who he or she
purports to be. The most common authentication mechanism is password
comparison.

+ Memory protection. Each user’s program must run in a portion of memory
protected against unauthorized accesses. The protection will certainly prevent
outsiders’ accesses, and it may also control a user’s own access to restricted
parts of the program space. Differential security, such as read, write, and
execute, may be applied to parts of a user’s memory space. Memory protection
is usually performed by hardware mechanisms, such as paging or segmentation.

+ File and I/O device access control. The operating system must protect user and
system files from access by unauthorized users. Similarly, I/O device use must
be protected. Data protection is usually achieved by table lookup, as with an
access control matrix.

+ Allocation and access control to general objects. Users need general objects,
such as constructs to permit concurrency and allow synchronization. However,
access to these objects must be controlled so that one user does not have a
negative effect on other users. Again, table lookup is the common means by
which this protection is provided.

You can probably see security implications in many of these primitive operating
systems functions. Operating systems show several faces: traffic director, police agent,
preschool teacher, umpire, timekeeper, clerk, and housekeeper, to name a few. These
fundamental, primitive functions of an operating system are called kernel functions,
because they are basic to enforcing security as well as the other higher-level operations an
operating system provides. Indeed, the operating system kernel, which we describe
shortly, is the basic block that supports all higher-level operating system functions.

Operating systems did not sprout fully formed with the rich feature set we know today.
Instead, they evolved from simple support utilities, as we explain next. The history of
operating systems is helpful to explain why and how operating systems acquired the
security functionality they have today.

Q2 [20]
Co-
SO- a. Discuss the various strategies for control against program threats. [10]
BL-

FIC 6 I HF
--- page 7 ---
CONTROLS AGAINST PROGRAM THREATS

Wi There are many ways a program can fail and many ways to turn
the underlying faults into security failures.

i It is better to focus on prevention than cure; how do we use
controls during s/w development to find and eliminate the faults.

WM Three types of controls:
© Developmental controls
oO Operating system
© administrative

CONTROLS AGAINST PROGRAM THREATS

Hi Developmental controls:
i Many controls can be applied during s/w development to fix problems.

WB The nature of s/w development:
© specify
Ans. © Design
© Implement
Oo Test
O° Review
© Document the system
© Manage
O° maintain

CONTROLS AGAINST PROGRAM THREATS

Hi Modularity, Encapsulation and information hiding:

HB A key principle of SE is to create a design or code in small, self-contained units
called components/modules, when a system is written this way, it is called
modular

Hl if a component is isolated from the effects of other components, then
© itis easier to trace a problem to the fault that caused it
© easier to maintain the system
©. Easier to see where vulnerabilities may lie

BB This isolation is called encapsulation

Hf information hiding is another characteristic of modular s/w.

HB When information is hidden, each component hides its implementation from
others, so that when a change is needed, the overall design can remain intact.

FIC 7 IC OHH
--- page 8 ---
| CONTROLS AGAINST PROGRAM THREATS

Hi Modularity:

Hi Modularization is a process of dividing a task into subtasks.
Hl The goal is to have each component meet 4 conditions:

lf Single-purpose: performs one function

i Small: consists of an amount of information for which a human can
readily grasp both structure and content.

ll Simple: is of a low degree of complexity so that a human can readily
understand the purpose and structure of the module.

Hi Independent: performs a task isolated from other modules.

| CONTROLS AGAINST PROGRAM THREATS

Hi Modularity:

Hi Advantages:
© Maintenance
© Understandability
o Reuse
© Correctness
°o Testing

Hi A modular component has high cohesion and low coupling

| CONTROLS AGAINST PROGRAM THREATS

Modularity:

i Cohesion: all elements of a component have a logical and functional
reason; every aspect of the component is tied to the component’s
single purpose.

© Ahigh cohesive component has high degree of focus on purpose
© Low degree cohesion means that component’s are unrelated.

i Coupling: refers to the degree with which a component depends on
other components in the system
© Thus, low coupling is better than tight coupling.

FOCI 9 FCI IC Ir
--- page 9 ---
CONTROLS AGAINST PROGRAM THREATS

i Encapsulation:
© It hides a component’s implementation details, but it does not
necessarily mean complete isolation.
© The sharing is documented so that a component is affected only in
known ways by others.
© Sharing is minimized so that fewest interfaces possible are used.
i Information hiding:
© Component is a black box with certain well-defined inputs and
outputs and well-defined function.
© Other components do not need to know how the module completes
its function.

CONTROLS AGAINST PROGRAM THREATS

I Peer Reviews

HB Hazard Analysis — set of systematic techniques to expose potentially
hazardous system states

Hi Testing - unit testing, integration testing, function testing,
performance testing, acceptance testing, installation testing,
regression testing

IB Good Design
© Using a philosophy of fault tolerance
© Have a consistent policy for handling failures
© Capture the design rationale and history
© Use design patterns

CONTROLS AGAINST PROGRAM THREATS

lM Prediction — predict the risks involved in building and using the
system

i Static Analysis — Use tools and techniques to examine characteristics
of design and code to see if the characteristics warn of possible faults

HB Configuration Management — control changes during development
and maintenance

IB Analysis of Mistakes

I Proofs of Program Correctness — Can we prove that there are no
security holes?

FEI QF IG Ir
--- page 10 ---
CO-3   What do you mean by operating system security. Explain the following.
SO-   b.   1. separation   [10]
2. memory protection
BL-1   3. access control
Ans.
********** 10 **********

[Text in pictures on this page, read by OCR]
OPERATING SYSTEM CONTROLS ON USE OF PROGRAMS

Wl Trusted Software — code has been rigorously developed and analyzed
© Functional correctness
© Enforcement of integrity
© Limited privilege
© Appropriate confidence level
Hi Mutual Suspicion — assume other program is not trustworthy
i Confinement — limit resources that program can access

HB Access Log — list who access computer objects, when, and for how long

ADMINISTRATIVE CONTROLS

Wi Standards of Program Development
WM Standards of design
Wi Standards of documentation, language, and coding style
WB Standards of programming
lB Standards of testing
WB Standards of configuration management
ll Security Audits

I Separation of Duties

13.1 Introduction

In this chapter, we’ll look at some of the security issues related to operating
systems (OSs). OSs are large and complex pieces of software. Recall that in
Chapter 12 we argued that there are almost certain to be security flaws in
any large and complex computer program. But here we are concerned with
the security protection provided by the OS, not with the very real threat of
bad OS software. That is, we are concerned with the role of the OS as the
security enforcer. This is a large topic that ties into many other aspects of
security and we'll just barely scratch the surface.

First, we'll describe the primary security-related functions of any modern
operating system. Then we’ll discuss the notion of a trusted OS, and we’ll
conclude with a look at Microsoft’s fairly recent effort to develop a trusted
operating system, which goes by the catchy name of the Next Generation
Secure Computing Base, or better yet, NGSCB.
--- page 11 ---
13.2 OS Security Functions

An OS must deal with potential security issues whether they arise accidentally
or as part of a malicious attack. Modern OSs are designed for multi-user
environments and multi-tasking operations. Consequently, an OS must, at a
minimum, deal with separation, memory protection, and access control. We
briefly discuss each of these three topics below.

13.2.1 Separation

Arguably the most fundamental security issue for a modern OS is that of
separation. That is, the OS must keep users and processes separate from
each other.

There are several ways that separation can be enforced [235], including
the following:

e Physical separation — Users are restricted to separate devices. This
provides a strong form of separation, but it is often impractical.

e Temporal separation — Processes are separated in time. This eliminates
many problems that arise due to concurrency and simplifies the job of
the OS. However, there is a loss of efficiency.

e Logical separation — For example, each process might be allocated its
own “sandbox.” A process is free to do almost anything within its
sandbox, but it can do almost nothing outside of its sandbox.

e Cryptographic separation — Crypto can be used to make information
unintelligible to an outsider.

Of course, various combinations of these methods can be used.

13.2.2 Memory Protection

Another fundamental issue an OS must deal with is memory protection. This
includes protection for the memory that the OS itself uses as well as the
memory of user processes. A fence, or fence address, is one option for memory
protection. A fence is a particular address that users and their processes
cannot cross—only the OS can operate on one side of the fence, and users are
restricted to the other side.

A fence could be static, in which case there is a fixed fence address. How-
ever, this places a strict limit on the size of the OS, which is a major drawback
(or benefit, depending on your perspective). Alternatively, a dynamic fence
can be used, which can be implemented using a fence register to specify the
current fence address.

FRI ICR 7 FI OH
--- page 12 ---
In addition to a fence, base and bounds registers can be used. These
registers contain the lower and upper address limits of a particular user (or
process) space. The base and bounds register approach implicitly assumes
that the user (or process) space is contiguous in memory.

The OS must determine what protection to apply to a specific memory
location. In some cases it might be sufficient to apply the same protection
to all of a user’s (or process’s) memory. At the other extreme, tagging spec-
ifies the protection for each individual address. While this is as fine-grained
protection as possible, it introduces significant overhead. The overhead can
be reduced by tagging sections of the address space instead of each individ-
ual address. In any case, another drawback to tagging is compatibility, since
tagging schemes are not in common use.

The most common methods of memory protection are segmentation and
paging. While these are not as flexible as tagging, they’re much more efficient.
We briefly discuss each of these next.

Segmentation, as illustrated in Figure 13.1, divides the memory into log-
ical units, such as individual procedures or the data in one array. Then
appropriate access control can be enforced on each segments. A benefit of
segmentation is that any segment can be placed in any memory location—
provided the location is large enough to hold it. Of course, the OS must
keep track of the locations of all segments, which is accomplished using
<segment ,offset> pairs, where the cleverly named segment specifies the
segment, and the offset is the starting address of the specified segment.

memory

Figure 13.1: Segmentation

Other benefits of segmentation include the fact that segments can be
moved to different locations in memory and they can also be moved in and out
of memory. With segmentation, all address references must go through the
OS, so the OS can, in this respect, achieve complete mediation. Depending

FRR ICR] DA KH
--- page 13 ---
Q3   [20]
CO-3   Describe the following principles of secure design with example.
SO-   1. Principle of Separation of Privilege
a.   [10]
2. Principle of Least Common Mechanism
BL-2   3. Psychological of Least Astonishment
********** 13 **********

[Text in pictures on this page, read by OCR]
on the access control applied to particular segments, users can share access
to some segments or users can be restricted to specific segments.

One serious drawback to segmentation is that the segments are of variable
sizes. As a result, before the OS tries to reference any element of a given
segment it must know the size of the segment so that it can be sure that
the requested address is within the segment. But some segments—such as
those that include dynamic memory allocation—can grow during execution.
Consequently, the OS must keep track of dynamic segment sizes. And due
the variability of segment sizes, memory fragmentation is a potential problem.
Finally, when memory is compacted to make better use of the available space,
the segmentation tables change. In short, segmentation is complex and places
a significant burden on the OS.

Paging is like segmentation, except that all segments are of a fixed size,
as illustrated in Figure 13.2. With paging, access to a particular page uses a
pair of the form <page, offset>. The advantages of paging over segmentation
include no fragmentation, improved efficiency, and the fact that there are no
variable sizes to worry about. The disadvantages are that there is, in general,
no logical unity to pages, which makes it more difficult to determine the
proper access control to apply to a given page.

memory

Page 1
program fee
Page 0 ee eee

Page 1 |_fovee _|

Page 2 Poge.0

Page 3

Page 4 ne
Page 3

Figure 13.2: Paging

13.2.3. Access Control

OSs are the ultimate enforcers of access control. This is one reason why the
OS is such an attractive target for attack—a successful attack on the OS
can effectively nullify any protection built in at a higher level. We discussed
access control in Chapter 8 and we’ll briefly return to the subject in the next
section when we discuss the concept of a trusted OS.
--- page 14 ---
14.2.6 Principle of Separation of Privilege

This principle is restrictive because it limits access to system entities.

Definition 14-7. The principle of separation of privilege states that a system
should not grant permission based on a single condition.

This principle is equivalent to the separation of duty principle discussed in
Section 6.1. Company checks for more than $75,000 must be signed by two officers
of the company. If either does not sign, the check is not valid. The two conditions
are the signatures of both officers.

Similarly, systems and programs granting access to resources should do so
only when more than one condition is met. This provides a fine-grained control
over the resource as well as additional assurance that the access is authorized.

EXAMPLE: On Berkeley-based versions of the UNIX operating system, the pro-
gram su, which enables users to change from their accounts to the root account,
requires two conditions to be met. The first condition is that the user knows the
root password. The second condition is that the user is in the whee/ group (the
group with GID 0). Meeting either condition is not sufficient to acquire root
access; meeting both conditions is required.

Ans.

14.2.7 Principle of Least Common Mechanism

This principle is restrictive because it limits sharing.

Definition 14-8. The principle of least common mechanism states that
mechanisms used to access resources should not be shared.

Sharing resources provides a channel along which information can be
transmitted, and so such sharing should be minimized. In practice, if the operating
system provides support for virtual machines, the operating system will enforce
this privilege automatically to some degree (see Chapter 18, “Confinement Prob-
lem”). Otherwise, it will provide some support (such as a virtual memory space)
but not complete support (because the file system will appear as shared among
several processes).

EXAMPLE: A website provides electronic commerce services for a major company.
Attackers want to deprive the company of the revenue it obtains from that website.
They flood the site with messages and tie up the electronic commerce services.
Legitimate customers are unable to access the website and, as a result, take their
business elsewhere.

FRR IC 7 I OH
--- page 15 ---
Here, the sharing of the Internet with the attackers’ sites caused the attack
to succeed. The appropriate countermeasure would be to restrict the attackers’
access to the segment of the Internet connected to the website. Techniques for
doing this include proxy servers such as the Purdue SYN intermediary [1695]
or traffic throttling (see Section 7.4, “Availability and Network Flooding”). The
former targets suspect connections; the latter reduces the load on the relevant
segment of the network indiscriminately.

Minimizing the number of shared mechanisms also reduces the scope of an
attack that compromises such a mechanism. If all versions of an operating system
use the same program, then compromising that single program enables attackers
to compromise any system of that type. But if the systems each use a slightly
different version of the program, then compromise becomes more difficult.

EXAMPLE: Attack tools assume an underlying structure or configuration of a
system or program. In order to invalidate this assumption, researchers have
studied how to inject artificial diversity effectively into programs and systems.
Then the attack tools will not work properly.

Object code obfuscation tools scramble the flow of execution and the
placement of data in memory. For example, many attacks target the return address
for function calls, which is stored on a stack and thus in a predictable location.
Adding a layer of indirection requires changing the function call and return
sequence. Then an attempt to overwrite the return address will change the index
into the table instead. By appropriately constraining that value and obscuring
how the actual return addresses are stored, the attacker will be unlikely to guess
the actual location of the return address, defeating this class of attacks [381].
Other techniques randomize the order of variables and functions in memory
or introduce random gaps between formerly contiguous areas of storage, and
locations of memory regions. This renders ineffective attack tools that rely on
the memory layout of the program [193].

14.2.8 Principle of Least Astonishment

This principle recognizes the human element in computer security.

Definition 14-9. The principle of least astonishment states that security
mechanisms should be designed so that users understand the reason that the
mechanism works the way it does and that using the mechanism is simple.

This principle requires security mechanisms to use a model that the target
audience (users and system administrators, typically) can easily understand. If
the audience’s mental model is too different than that used by the designers and
implementers, then their confusion may undermine the security mechanisms.

FRR IC 7 DA HOH
--- page 16 ---
Thus, configuring and executing a program should be as easy and as
intuitive as possible, and any output should be clear, direct, and useful. If security-
related software is too complicated to configure, system administrators may
unintentionally set up the software in a nonsecure manner. Similarly, security-
related user programs must be easy to use and must output understandable
messages. If a user is changing a password, and the proposed password is rejected,
the password changing program should state why it was rejected rather than giving
acryptic error message. If a configuration file has an incorrect parameter, the error
message should describe the proper parameter.

EXAMPLE: The ssh program [131, 2058] allows a user to set up a public key
mechanism for enciphering communications between systems. The installation
and configuration mechanisms for the UNIX version allow one to arrange that
the public key be stored locally without any password protection. In this case,
one need not supply a password to connect to the remote system, but will still
obtain the enciphered connection. This mechanism satisfies the principle of least
astonishment.

On the other hand, security requires that the messages impart no unneces-
sary information.

EXAMPLE: When a user supplies the wrong password during login, the system
should reject the attempt with a message stating that the login failed. If it were to
say that the password was incorrect, the user would know that the account name
was legitimate. If the “user” were really an unauthorized attacker, she would then
know the name of an account for which she could try to guess a password.

Balancing the needs of security and the mental models of users requires
that the designers and implementers take into account the environment in which
the security mechanisms are used.

EXAMPLE: A mainframe system allows users to place passwords on files.
Accessing the files requires that the program supply the password. Although this
mechanism violates the principle as stated, it is considered sufficiently minimal to
be acceptable. On an interactive system, where the pattern of file accesses is more
frequent and more transient, this requirement would be too great a burden to be
acceptable.

14.2.8.1 Psychological Acceptability

The principle of least astonishment is similar to one of Saltzer’s and Schroeder's
original principles, the principle of psychological acceptability. That principle
stated that that security mechanisms should not make the resource more difficult
to access than if the security mechanisms were not present. The difference
between that principle and the principle of least astonishment is that the former
expressed an ideal, whereas the latter recognizes that security mechanisms may

add additional steps to accessing the resource. The question is whether those
additional steps are unnecessarily difficult to take to the particular population
of users of the system.

COo-3

SO- b. | Write short note on IDS and its types. [10]

BL-2

FRR ICR 7 6 AC OH
--- page 17 ---
Ans.
Explanation for each in detail with example.
Q4   [20]
CO-3
Discuss the points to be considered for securing the design of operating systems in
SO-   a.   [10]
depth.
BL-3
********** 17 **********

[Text in pictures on this page, read by OCR]
Intrusion Detection System & its
Types

» An intrusion occurs when an attacker attempts to gain entry into or disrupt the normal operations

of an information system, almost always with the intent to do harm.
» Intrusion detection consists of procedures and systems that identify system intrusions.
> Intrusion reaction encompasses the actions an organization takes when an intrusion is detected.

> Intrusion correction activities finalize the restoration of operations to a normal state and seek to
identify the source and method of the intrusion in order to ensure that the same type of attack

cannot occur again—thus reinitiating intrusion prevention.

Intrusion Detection System & its
Types

» Host-based IDS (HIDS) - Monitors and analyzes activities on individual hosts or devices within a
network. It focuses on detecting suspicious behavior at the host level, such as unauthorized access

or changes to system files.

» Network-based IDS (NIDS) - Examines network traffic and identifies suspicious patterns or
anomalies. NIDS is deployed at strategic points within the network to monitor traffic and detect

potential threats.

» Signature-based IDS - Relies on a database of predefined signatures or patterns associated with
known threats. It compares network or system activity against these signatures to identify and alert

on known attacks.

Intrusion Detection System & its
Types

» Anomaly-based IDS - Learns the baseline behavior of the network or system and triggers alerts
when deviations from the normal behavior are detected. Anomaly-based IDS is effective in

detecting new and unknown threats.

» Heuristic-based IDS - Uses predefined rules and algorithms to identify patterns or behaviors that
may indicate potential security incidents. Heuristic-based IDS combines aspects of both signature-

based and anomaly-based detection.

» Behavior-based IDS - Analyzes the behavior of users, applications, or systems to detect abnormal
activities that may indicate a security threat. This approach focuses on deviations from expected

behavior.
--- page 18 ---
Ans.

5.2 Security in the Design of Operating Systems

As we just discussed, operating systems are complex pieces of software. The
components come from many sources, some pieces are legacy code to support old
functions; other pieces date back literally decades, with long-forgotten design
characteristics. And some pieces were written just yesterday. Old and new pieces must
interact and interface successfully, and new designers must ensure that their code works
correctly with all existing previous versions, not to mention the numerous applications that
exist.

Exploit authors capitalize on this complexity by experimenting to locate interface
mismatches: a function no longer called, an empty position in the table of interrupts
handled, a forgotten device driver. The operating system opens many points to which code
can later attach as pieces are loaded during the boot process; if one of these pieces is not
present, the malicious code can attach instead.

Obviously, not all complex software is vulnerable to attack. The point we are making is
that the more complex the software, the more possibilities for unwanted software
introduction. A house with no windows leaves no chance for someone to break in through
a window, but each additional window in a house design increases the potential for this
harm and requires the homeowner to apply more security. Now extend this metaphor to
modern operating systems that typically include millions of lines of code: What is the

FR ICR 7] QA HH
--- page 19 ---
likelihood that every line is perfect for its use and fits perfectly with every other line?

The principles of secure program design we introduced in Chapter 3 apply equally well
to operating systems. Simple, modular, loosely coupled designs present fewer
opportunities to the attacker.

Simplicity of Design

Operating systems by themselves (regardless of their security constraints) are difficult
to design. They handle many duties, are subject to interruptions and context switches, and
must minimize overhead so as not to slow user computations and interactions. Adding the
responsibility for security enforcement to the operating system increases the difficulty of
design.

Nevertheless, the need for effective security is pervasive, and good software
engineering principles tell us how important it is to design in security at the beginning
than to shoehorn it in at the end. (See Sidebar 5-2 for more about good design principles.)
Thus, this section focuses on the design of operating systems for a high degree of security.
We look in particular at the design of an operating system’s kernel; how the kernel is
designed suggests whether security will be provided effectively. We study two different
interpretations of the kernel, and then we consider layered or ring-structured designs.

Layered Design

As described previously, a nontrivial operating system consists of at least four levels:
hardware, kernel, operating system, and user. Each of these layers can include sublayers.
For example, in [SCH83], the kernel has five distinct layers. The user level may also have
quasi-system programs, such as database managers or graphical user interface shells, that
constitute separate layers of security themselves.

Sidebar 5-2 The Importance of Good Design Principles

Every design, whether it be for hardware or software, must begin with a design
philosophy and guiding principles. These principles suffuse the design, are built
in from the beginning, and are preserved (according to the design philosophy) as
the design evolves.

The design philosophy expresses the overall intentions of the designers, not
only in terms of how the system will look and act but also in terms of how it will
be tested and maintained. Most systems are not built for short-term use. They
grow and evolve as the world changes over time. Features are enhanced, added,
or deleted. Supporting or communicating hardware and software change. The
system is fixed as problems are discovered and their causes rooted out. The
design philosophy explains how the system will “hang together,” maintaining its
integrity through all these changes. A good design philosophy will make a
system easy to test and easy to change.

The philosophy suggests a set of good design principles. Modularity,
information hiding, and other notions discussed in Chapter 3 form guidelines
that enable designers to meet their goals for software quality. Since security is
one of these goals, it is essential that security policy be consistent with the

FRR ICR 7 QI OR
--- page 20 ---
design philosophy and that the design principles enable appropriate protections
to be built into the system.

When the quality of the design is not considered up-front and embedded in
the development process, the result can be a sort of software anarchy. The
system may run properly at first, but as changes are made, the software degrades
quickly and in a way that makes future changes more difficult and time
consuming. The software becomes brittle, failing more often and sometimes
making it impossible for features, including security, to be added or changed.
Equally important, brittle and poorly designed software can easily hide
vulnerabilities because the software is so difficult to understand and the
execution states so hard to follow, reproduce, and test. Thus, good design is in
fact a security issue, and secure software must be designed well.

Layered Trust

As we discussed earlier in this chapter, the layered structure of a secure operating
system can be thought of as a series of concentric circles, with the most sensitive
operations in the innermost layers. An equivalent view is as a building, with the most
sensitive tasks assigned to lower floors. Then, the trustworthiness and access rights of a
process can be judged by the process’s proximity to the center: The more trusted processes
are closer to the center or bottom.

Implicit in the use of layering as a countermeasure is separation. Earlier in this chapter
we described ways to implement separation: physical, temporal, logical, and
cryptographic. Of these four, logical (software-based) separation is most applicable to
layered design, which means a fundamental (inner or lower) part of the operating system
must control the accesses of all outer or higher layers to enforce separation.

Peter Neumann [NEU86] describes the layered structure used for the Provably Secure
Operating System (PSOS). Some lower-level layers present some or all of their
functionality to higher levels, but each layer properly encapsulates those things below
itself.

A layered approach is another way to achieve encapsulation, presented in Chapter 3.
Layering is recognized as a good operating system design. Each layer uses the more
central layers as services, and each layer provides a certain level of functionality to the
layers farther out. In this way, we can “peel off” each layer and still have a logically
complete system with less functionality. Layering presents a good example of how to trade
off and balance design characteristics.

Another justification for layering is damage control. To see why, consider Neumann’s
two examples of risk. In a conventional, nonhierarchically designed system (shown in
Table 5-1), any problem—hardware failure, software flaw, or unexpected condition, even
in a supposedly irrelevant nonsecurity portion—can cause disaster because the effect of
the problem is unbounded and because the system’s design means that we cannot be
confident that any given function has no (indirect) security effect.

FRI ICR DO) A RH
--- page 21 ---
Level Functions Risk

all Noncritical functions Disaster possible
all Less critical functions Disaster possible
all More critical functions | Disaster possible

TABLE 5-1 Conventional (Nonhierarchical) Design
By contrast, as shown in Table 5-2, hierarchical structuring has two benefits:

+ Hierarchical structuring permits identification of the most critical parts, which
can then be analyzed intensely for correctness, so the number of problems
should be smaller.

+ Isolation limits effects of problems to the hierarchical levels at and above the
point of the problem, so the harmful effects of many problems should be

confined.
Level Functions Risk
Z Noncritical functions Few disasters likely from noncritical software

1 Less critical functions | Some failures possible from less critical functions, but because of
separation, impact limited

0 More critical functions | Disasters possible, but unlikely if system simple enough for more
critical functions to be analyzed extensively

TABLE 5-2 Hierarchically Designed System

These design properties—the kernel, separation, isolation, and hierarchical structure—
have been the basis for many trustworthy system prototypes. They have stood the test of
time as best design and implementation practices.

Layering ensures that a security problem affects only less sensitive layers.

Kernelized Design

A kernel is the part of an operating system that performs the lowest-level functions. In
standard operating system design, the kernel implements operations such as
synchronization, interprocess communication, message passing, and interrupt handling.
The kernel is also called a nucleus or core. The notion of designing an operating system
around a kernel is described by Butler Lampson and Howard Sturgis [LAM76] and by
Gerald Popek and Charles Kline [POP78}.

A security kernel is responsible for enforcing the security mechanisms of the entire
operating system. The security kernel provides the security interfaces among the
hardware, operating system, and other parts of the computing system. Typically, the
operating system is designed so that the security kernel is contained within the operating
system kernel. Security kernels are discussed in detail by Stan Ames [AME83].

Security kernel: locus of all security enforcement

FI ICR D7 FAC HOH
--- page 22 ---
There are several good design reasons why security functions may be isolated in a
security kernel.

* Coverage. Every access to a protected object must pass through the security
kernel. In a system designed in this way, the operating system can use the
security kernel to ensure that every access is checked.

+ Separation. Isolating security mechanisms both from the rest of the operating
system and from the user space makes it easier to protect those mechanisms
from penetration by the operating system or the users.

* Unity. All security functions are performed by a single set of code, so it is
easier to trace the cause of any problems that arise with these functions.

+ Modifiability. Changes to the security mechanisms are easier to make and
easier to test. And because of unity, the effects of changes are localized so
interfaces are easier to understand and control.

* Compactness. Because it performs only security functions, the security kernel
is likely to be relatively small.

+ Verifiability. Being relatively small, the security kernel can be analyzed
rigorously. For example, formal methods can be used to ensure that all security
situations (such as states and state changes) have been covered by the design.

Notice the similarity between these advantages and the design goals of operating
systems that we described earlier. These characteristics also depend in many ways on
modularity, as described in Chapter 3.

On the other hand, implementing a security kernel may degrade system performance
because the kernel adds yet another layer of interface between user programs and
operating system resources. Moreover, the presence of a kernel does not guarantee that it
contains all security functions or that it has been implemented correctly. And in some
cases a security kernel can be quite large.

How do we balance these positive and negative aspects of using a security kernel? The
design and usefulness of a security kernel depend somewhat on the overall approach to the
operating system’s design. There are many design choices, each of which falls into one of
two types: Either the security kernel is designed as an addition to the operating system or
it is the basis of the entire operating system. Let us look more closely at each design
choice.

Reference Monitor

The most important part of a security kernel is the reference monitor, the portion that
controls accesses to objects [AND72, LAM71]. We introduced reference monitors in
Chapter 2. The reference monitor separates subjects and objects, enforcing that a subject
can access only those objects expressly allowed by security policy. A reference monitor is
not necessarily a single piece of code; rather, it is the collection of access controls for
devices, files, memory, interprocess communication, and other kinds of objects. As shown
in Figure 5-15, a reference monitor acts like a brick wall around the operating system or
trusted software to mediate accesses by subjects (S) to objects (O).

FIR ICR DAC HH
--- page 23 ---
Sass p
OG i“ ;

Reference a
Monitor g

FIGURE 5-15 Reference Monitor
As stated in Chapter 2, a reference monitor must be

* tamperproof, that is, impossible to weaken or disable
+ unbypassable, that is, always invoked when access to any object is required

+ analyzable, that is, small enough to be subjected to analysis and testing, the
completeness of which can be ensured

The reference monitor is not the only security mechanism of a trusted operating system.
Other parts of the security suite include auditing and identification and authentication
processing, as well as setting enforcement parameters, such as who are allowable subjects
and what objects they are allowed to access. These other security parts interact with the
reference monitor, receiving data from the reference monitor or providing it with the data
it needs to operate.

The reference monitor concept has been used for many trusted operating systems and
also for smaller pieces of trusted software. The validity of this concept is well supported
both in research and in practice. Paul Karger [KAR90, KAR91] and Morrie Gasser
[GAS88] describe the design and construction of the kernelized DEC VAX operating
system that adhered strictly to use of a reference monitor to control access.

Correctness and Completeness

That security considerations pervade the design and structure of operating systems
requires correctness and completeness. Correctness implies that because an operating
system controls the interaction between subjects and objects, security must be considered
in every aspect of its design. That is, the operating system design must include definitions
of which objects will be protected in what ways, what subjects will have access and at
what levels, and so on. There must be a clear mapping from the security requirements to
the design so that all developers can see how the two relate.

Moreover, after designers have structured a section of the operating system, they must
check to see that the design actually implements the degree of security that it is supposed
to enforce. This checking can be done in many ways, including formal reviews or
simulations. Again, a mapping is necessary, this time from the requirements to design to
tests, so that developers can affirm that each aspect of operating system security has been

FIR ICR 2 I OH
--- page 24 ---
CO-2
What is a virus. Explain the various methods through which virus attaches itself to a
SO-   b.   [10]
host program.
BL-2
********** 24 **********

[Text in pictures on this page, read by OCR]
tested and shown to work correctly. Because security appears in every part of an operating
system, security design and implementation cannot be left fuzzy or vague until the rest of
the system is working and being tested.

Completeness requires that security functionality be included in all places necessary.
Although this requirement seems self-evident, not all developers are necessarily thinking
of security as they design and write code, so security completeness is challenging. It is
extremely hard to retrofit security features to an operating system designed with
inadequate security. Leaving an operating system’s security to the last minute is much like
trying to install plumbing or electrical wiring in a house whose foundation is set, floors
laid, and walls already up and painted; not only must you destroy most of what you have
built, but you may also find that the general structure can no longer accommodate all that
is needed (and so some has to be left out or compromised). And last-minute additions are
often done hastily under time pressure, which does not encourage completeness.

Security enforcement must be correct and complete.

Thus, security must be an essential part of the initial design of a trusted operating
system. Indeed, the security considerations may shape many of the other design decisions,
especially for a system with complex and constraining security requirements. For the same
reasons, the security and other design principles must be carried throughout
implementation, testing, and maintenance. Phrased differently, as explained in Sidebar 5-
3, security emphatically cannot be added on at the end.

Security seldom succeeds as an add-on; it must be part of the initial
philosophy, requirements, design, and implementation.

Sidebar 5-3 Security as an Add-On

In the 1980s, the U.S. State Department handled its diplomatic office functions
with a network of Wang computers. Each American embassy had at least one
Wang system, with specialized word processing software to create documents,
modify them, store and retrieve them, and send them from one location to
another. Supplementing Wang’s office automation software was the State
Department’s own Foreign Affairs Information System (FAIS).

In the mid-1980s, the State Department commissioned a private contractor to
add security to FAIS. Diplomatic and other correspondence was to be protected
by a secure “envelope” surrounding sensitive materials. The added protection
was intended to prevent unauthorized parties from “opening” an envelope and
reading the contents.

To design and implement the security features, the contractor had to
supplement features offered by Wang’s operating system and utilities. The
security design depended on the current Wang VS operating system design,
including the use of unused words in operating system files. As designed and
implemented, the new security features worked properly and met the State
Department requirements. But the system was bound for failure because the

evolutionary goals of VS were different from those of the State Department.
That is, Wang could not guarantee that future modifications to VS would
preserve the functions and structure required by the contractor’s security
software. In other words, Wang might need to appropriate some of the unused
words in operating system files for new system functions, regardless of whether
or not FAIS was using those words. Eventually, there were fatal clashes of intent
and practice, and the added-on security functions failed.
--- page 25 ---
Ans.

MALICIOUS PROGRAM ERRORS

| Computer Virus can slow down your computer by displaying useless messages.
“

(x) You are Heart Less.
You Wil Be Punished For This

pel

|_| might corrupt your system files.

|_| might make some programs faulty or corrupt.

| might damage your boot sector creating problems when you boot into the windows.

|| might steal important information from your computer and send to some other person.

| might change the power ratings of your computer and could blast the system.
Appended Viruses

A program virus attaches itself to a program; then, whenever the program is run, the
virus is activated. This kind of attachment is usually easy to design and implement.

In the simplest case, a virus inserts a copy of itself into the executable program file
before the first executable instruction. Then, all the virus instructions execute first; after
the last virus instruction, control flows naturally to what used to be the first program
instruction. Such a situation is shown in Figure 3-19.

+ Virus Code = Virus Code

Original
Program

Original
Program

FIGURE 3-19 Virus Attachment

This kind of attachment is simple and usually effective. The virus writer need not know
anything about the program to which the virus will attach, and often the attached program
simply serves as a carrier for the virus. The virus performs its task and then transfers to the
original program. Typically, the user is unaware of the effect of the virus if the original
program still does all that it used to. Most viruses attach in this manner.

Viruses That Surround a Program

An alternative to the attachment is a virus that runs the original program but has control
before and after its execution. For example, a virus writer might want to prevent the virus
from being detected. If the virus is stored on disk, its presence will be given away by its
file name, or its size will affect the amount of space used on the disk. The virus writer
might arrange for the virus to attach itself to the program that constructs the listing of files
on the disk. If the virus regains control after the listing program has generated the listing
but before the listing is displayed or printed, the virus could eliminate its entry from the
listing and falsify space counts so that it appears not to exist. A surrounding virus is shown
in Fi, -20.

FI ICR AC KH
--- page 26 ---
Q5   [20]
CO-1   Write short note on biometric authentication covering the following points.
SO-   1. physical characteristics used in biometric applications
a.   [10]
2. operation of biometric authentication system
BL-3   3. biometric accuracy
Ans.
********** 26 **********

[Text in pictures on this page, read by OCR]
Physically Logically

a Virus Code
Virus Code_| o0)

Original
Program
Original
Program
Virus Code
Part (b)

FIGURE 3-20 Surrounding Virus
Integrated Viruses and Replacements

A third situation occurs when the virus replaces some of its target, integrating itself into
the original code of the target. Such a situation is shown in Figure 3-21. Clearly, the virus
writer has to know the exact structure of the original program to know where to insert
which pieces of the virus.

Original + Virus = Modified
Program Code ia Program

FIGURE 3-21 Virus Insertion

Finally, the malicious code can replace an entire target, either mimicking the effect of
the target or ignoring its expected effect and performing only the virus effect. In this case,
--- page 27 ---
and dynamic characteristics, such as voiceprint and signature. In essence, biomet-
rics is based on pattern recognition. Compared to passwords and tokens, biometric
authentication is both technically more complex and expensive. While it is used in a
number of specific applications, biometrics has yet to mature as a standard tool for
user authentication to computer systems.

Physical Characteristics Used in Biometric Applications

A number of different types of physical characteristics are either in use or under
study for user authentication. The most common are the following:

° Facial characteristics: Facial characteristics are the most common means
of human-to-human identification; thus it is natural to consider them for
identification by computer. The most common approach is to define charac-
teristics based on relative location and shape of key facial features, such as
eyes, eyebrows, nose, lips, and chin shape. An alternative approach is to use an
infrared camera to produce a face thermogram that correlates with the underly-
ing vascular system in the human face.

¢ Fingerprints: Fingerprints have been used as a means of identification for cen-
turies, and the process has been systematized and automated particularly for
law enforcement purposes. A fingerprint is the pattern of ridges and furrows on
the surface of the fingertip. Fingerprints are believed to be unique across the
entire human population. In practice, automated fingerprint recognition and
matching system extract a number of features from the fingerprint for storage
as a numerical surrogate for the full fingerprint pattern.

° Hand geometry: Hand geometry systems identify features of the hand, includ-
ing shape, and lengths and widths of fingers.

¢ Retinal pattern: The pattern formed by veins beneath the retinal surface is
unique and therefore suitable for identification. A retinal biometric system
obtains a digital image of the retinal pattern by projecting a low-intensity beam
of visual or infrared light into the eye.

¢ Iris: Another unique physical characteristic is the detailed structure of the iris.

Signature: Each individual has a unique style of handwriting and this is reflected
especially in the signature, which is typically a frequently written sequence.
However, multiple signature samples from a single individual will not be identi-
cal. This complicates the task of developing a computer representation of the
signature that can be matched to future samples.

* Voice: Whereas the signature style of an individual reflects not only the unique
physical attributes of the writer but also the writing habit that has developed,
voice patterns are more closely tied to the physical and anatomical characteris-
tics of the speaker. Nevertheless, there is still a variation from sample to sample
over time from the same speaker, complicating the biometric recognition task.

Figure 3.8 gives a rough indication of the relative cost and accuracy of these
biometric measures. The concept of accuracy does not apply to user authentication
schemes using smart cards or passwords. For example, if a user enters a password,
it either matches exactly the password expected for that user or not. In the case of

FR ICR D7 FAC KH
--- page 28 ---
Hand
: Retina
z| Signature
1S)
Face Finger
Voice
Accuracy

Figure 3.8 Cost Versus Accuracy of Various Biometric
Characteristics in User Authentication Schemes

biometric parameters, the system instead must determine how closely a presented
biometric characteristic matches a stored characteristic. Before elaborating on the
concept of biometric accuracy, we need to have a general idea of how biometric
systems work.

Operation of a Biometric Authentication System

Figure 3.9 illustrates the operation of a biometric system. Each individual who is to be
included in the database of authorized users must first be enrolled in the system. This
is analogous to assigning a password to a user. For a biometric system, the user pres-
ents a name and, typically, some type of password or PIN to the system. At the same
time, the system senses some biometric characteristic of this user (e.g., fingerprint
of right index finger). The system digitizes the input then extracts a set of features
that can be stored as a number or set of numbers representing this unique biometric
characteristic; this set of numbers is referred to as the user’s template. The user is now
enrolled in the system, which maintains for the user a name (ID), perhaps a PIN or
password, and the biometric value.

Depending on application, user authentication on a biometric system involves
either verification or identification. Verification is analogous to a user logging on to
a system by using a memory card or smart card coupled with a password or PIN. For
biometric verification, the user enters a PIN and also uses a biometric sensor. The
system extracts the corresponding feature and compares that to the template stored
for this user. If there is a match, then the system authenticates this user.

For an identification system, the individual uses the biometric sensor but pres-
ents no additional information. The system then compares the presented template
with the set of stored templates. If there is a match, then this user is identified. Oth-
erwise, the user is rejected.

Biometric Accuracy

In any biometric scheme, some physical characteristic of the individual is mapped
into a digital representation. For each individual, a single digital representation, or

FI ICR 2 QA HH
--- page 29 ---
Name (PIN)

Biometric g Feature
sensor extractor

User interface

(a) Enrollment

Name (PIN)
Biometric g Feature
¥ sensor extractor
Y
User interface True/false Feature
matcher One template

(b) Verification

Biometric g Feature

sensor extractor
User interface User’s identity or Feature
“user unidentified” matcher N templates

(c) Identification

Figure 3.9 A Generic Biometric System Enrollment creates an association
between a user and the user’s biometric characteristics. Depending on the appli-
cation, user authentication either involves verifying that a claimed user is the
actual user or identifying an unknown user.

template, is stored in the computer. When the user is to be authenticated, the system
compares the stored template to the presented template. Given the complexities of
physical characteristics, we cannot expect that there will be an exact match between
the two templates. Rather, the system uses an algorithm to generate a matching
score (typically a single number) that quantifies the similarity between the input and
the stored template. To proceed with the discussion, we define the following terms.
The false match rate is the frequency with which biometric samples from different
sources are erroneously assessed to be from the same source. The false nonmatch rate
is the frequency with which samples from the same source are erroneously assessed
to be from different sources.

Figure 3.10 illustrates the dilemma posed to the system. If a single user is tested
by the system numerous times, the matching score s will vary, with a probability

FAR ICR QA HH
--- page 30 ---
Probability
density function
Decision

Imposter threshold () Profile of
profile ' genuine user

\ | i

nonmatch
possible

False
match
possible

| ' T
Average matching Average matching Matching score (s)
value of imposter value of genuine user

Figure 3.10 Profiles of a Biometric Characteristic of an Imposter and an
Authorized User In this depiction, the comparison between the presented
feature and a reference feature is reduced to a single numeric value. If
the input value (s) is greater than a preassigned threshold (f), a match is
declared.

density function typically forming a bell curve, as shown. For example, in the case of a
fingerprint, results may vary due to sensor noise; changes in the print due to swelling
or dryness; finger placement; and so on. On average, any other individual should have
a much lower matching score, but again will exhibit a bell-shaped probability density
function. The difficulty is that the range of matching scores produced by two individu-
als, one genuine and one an imposter, compared to a given reference template, are
likely to overlap. In Figure 3.10, a threshold value is selected thus that if the presented
value s = ta match is assumed, and fors < t,a mismatch is assumed. The shaded part
to the right of rindicates a range of values for which a false match is possible, and the
shaded part to the left indicates a range of values for which a false nonmatch is pos-
sible. A false match results in the acceptance of a user who should not be accepted,
and a false mismatch triggers the rejection of a valid user. The area of each shaded
part represents the probability of a false match or nonmatch, respectively. By moving
the threshold, left or right, the probabilities can be altered, but note that a decrease
in false match rate results in an increase in false nonmatch rate, and vice versa.

For a given biometric scheme, we can plot the false match versus false nonmatch
rate, called the operating characteristic curve. Figure 3.11 shows idealized curves for
two different systems. The curve that is lower and to the left performs better. The
dot on the curve corresponds to a specific threshold for biometric testing. Shifting
the threshold along the curve up and to the left provides greater security and the
cost of decreased convenience. The inconvenience comes from a valid user being
denied access and being required to take further steps. A plausible trade-off is to

FIR ICR QQ) A HH
--- page 31 ---
100%

10%

1%

0.1%
0.0001 % 0.001% 0.01% 0.1% 1% 10% 100%

False match rate

Figure 3.11 Idealized Biometric Measurement Operating Characteristic Curves
(log-log scale)

pick a threshold that corresponds to a point on the curve where the rates are equal.
A high-security application may require a very low false match rate, resulting in a
point farther to the left on the curve. For a forensic application, in which the system
is looking for possible candidates, to be checked further, the requirement may be for
a low false nonmatch rate.

Figure 3.12 shows characteristic curves developed from actual product testing.
The iris system had no false matches in over 2 million cross-comparisons. Note that
over a broad range of false match rates, the face biometric is the worst performer.

COo-3
SO- b. Discuss firewalls and DMZ as an example of information flow controls. [10]
BL-2

17.6 Example Information Flow Controls

Like the program-based information flow mechanisms discussed in this chapter,
both special-purpose and general-purpose computer systems have information
Ans. flow controls at the system level. File access controls, integrity controls, and
other types of access controls are mechanisms that attempt to inhibit the flow
of information within a system, or between systems.
The first example follows a line of research that examines privacy in
information flow on cell phones. The second example describes firewalls, which
act to control information flow between (or among) networks.

FR ICR QI OH
--- page 32 ---
17.6.2 Firewalls

Firewalls are systems that sit between networks, usually an organization’s internal
network and some other external network such as the Internet. The firewall
controls access between the networks. The advantage of firewalls is that they
can filter network traffic before it reaches the target host. They can also redirect
network connections as appropriate, or throttle traffic to limit the amount of
traffic that flows into (or out of) the internal network.

Definition 17-9. A firewall is a host that mediates access to a network,
allowing and disallowing certain types of access on the basis of a configured
security policy.

EXAMPLE: A company wishes to prevent any variants of the worm Conficker [85,
1144] from entering its networks. Conficker is a worm that connects to a botnet

FIR ICR QD I HH
--- page 33 ---
(the Conficker botnet) and can then be used for a variety of purposes, includ-
ing downloading other malware and controlling the infected system. Conficker
spreads through a vulnerability in the Microsoft Windows Service server [1145,
1332], so a firewall can be configured to examine packets that are targeting that
service to determine if they contain any variant of Conficker.

Once Conficker is resident, it generates a list of domain names and tries to
contact the botnet at those hosts. Every Conficker worm will generate the same set
of domain names, and it changes every three hours. The generation sequence, and
hence set of domains, is known. So the firewall can also be configured to block
outgoing traffic to those domains, neutralizing the “botnet” aspect of conficker.

There are two basic types of firewalls. The first accepts or rejects messages
on the basis of packet header information, such as destination addresses or ports.

Definition 17-10. A filtering firewall performs access control on the basis
of attributes of the packet headers, such as destination addresses, source
addresses, and options.

Routers and other infrastructure systems are typical examples of filtering
firewalls. They allow connections through the firewall, usually on the basis of
source and destination addresses and ports. Access control lists provide a natural
mechanism for representing these policies.

This contrasts with the second type of firewall, which never allows such
a direct connection. Instead, special agents called proxies control the flow of
information through the firewall.

Definition 17-11. A proxy is an intermediate agent or server that acts on
behalf of an endpoint without allowing a direct connection between the
two endpoints. A proxy (or application level) firewall uses proxies to perform
access control.

A proxy firewall adds to a filtering firewall the ability to base access on
content, either at the packet level or at a higher level of abstraction. Thus, a proxy
firewall can base access control on the contents of packets and messages, as well
as on attributes of the packet headers.

EXAMPLE: A company wishes to check all incoming electronic mail for computer
viruses. It implements a mail proxy at the firewall between the Internet and the
company intranet. The proxy has a virus scanning program (see Chapter 23).
When mail arrives at the firewall, the proxy mail daemon accepts the mail. It then
runs the virus scanner. If the scanner reports that there are no viruses in the mail or
in any associated attachments, the proxy forwards the mail to the desired recipient.
If the virus scanner reports that the mail or an attachment contains a virus, the
mail is discarded (or some other appropriate action is taken). The fact that the

FR ICR QQ I OH
--- page 34 ---
electronic mail message is reassembled at the firewall by a mail agent acting on
behalf of the mail agent at the ultimate destination makes this a proxy firewall.

EXAMPLE: Because Java applets usually come from untrusted sources, many
organizations want to block the applets from entering their internal networks.
A simple method of doing this is to block the applets at a firewall. When an HTTP
connection is made through the firewall, the firewall creates a proxy to reassemble
the packets and determine if they contain a Java applet. The proxy then may use
one of three approaches to block the applet.

First, it can rewrite the HTML tag to something other than “<applet>”.
When the page is delivered to the browser, the browser will not recognize the
applet and will not run it. This method requires the firewall to determine that
the connection is indeed an HTTP connection and to parse the HTML in that
connection. Both are nontrivial tasks.

The second approach is to look for incoming files with the hexadecimal
sequence “CA FE BA BE”. All Java class files must contain this four-byte
signature in order to be properly recognized and interpreted. If this sequence
is found, the file is immediately discarded. The danger here is a false positive.
Because ActiveX and Javascript code are different, this approach cannot block
those types of applets.

The third approach is to block based on file name, but this is far more
problematic because the names do not necessarily represent the contents of the
file. Many browsers require Java class files to end in “.class”. The firewall can
block these applets. However, more recent browsers allow Java class files to be
combined into archives. The names of these archives often end in “.zip”. This is
a popular format among users of MS-DOS and Windows, so it is not realistic to
block all such files.

Martin, Rajagopalan, and Rubin [1258] conclude that the situation is rather
bleak for stopping Java applets at the firewall.

A variant of the application-level firewall assembles enough of a packet to
determine whether it should be forwarded.

Definition 17-12. A stateful firewall is a firewall that keeps track of the state
of each connection.

Although no proxies are involved, a stateful firewall can examine the
contents of connections, even when the data in question is spread over several
packets. For example, a connection to port 25 typically indicates electronic mail,
as that is the standard port for the SMTP (email) protocol. A packet filtering
firewall would not detect that, for example, HTTP messages were being sent to
a host on the internal network if those messages were being sent to port 25 on
that host. A stateful firewall would detect that the messages were not messages
associated with the SMTP protocol and block them.

FIR ICR I HOH
--- page 35 ---
Q6   [20]
CO-   Write short note on implementing access control on the following points.
SO-   a.   1. Access Control Directory   [10]
2. Access Control Matrix
BL-   3. Access Control List
********** 35 **********

[Text in pictures on this page, read by OCR]
Organizations typically partition their network into several parts, with fire-
walls between parts to prevent information from leaking. A common arrangement
is to have two different internal networks, one accessible to the public and the other
not (see Figure 17-4).

Definition 17-13. The DMZ! is a portion of a network that separates a
purely internal network from an external network.

When information moves from the Internet to the internal network, con-
fidentiality is not at issue. However, integrity is. So there are firewalls between
the Internet and the DMZ, and between the DMZ and the internal network.
These must not accept messages that will cause servers to work incorrectly or
to crash. When information moves from the internal network to the Internet,
confidentiality and integrity are both at issue. The firewalls must ensure that no
confidential information goes to the Internet. The arrangement and configura-
tion of the firewalls provide the supporting access control mechanisms used to
implement the policy.

In addition to controlling information flow, a different point of view is
to use the firewall as an audit mechanism. In this role, the firewall analyzes the
packets that transit it. The firewall can then base actions on this analysis, leading
to traffic shaping (in which percentages of bandwidth are reserved for specific
types of traffic), changes in access permissions due to the amount and nature of
the traffic, and other controls.

(a) (b)

Figure 17-4 This figure shows two different common configurations for using
firewalls to protect company internal networks. In both cases, the subnets
labeled “DMZ” provide limited public access to various servers. In (a), the
firewall is dual-homed and routes messages to the internal network or the DMZ
as appropriate. In (b), the outer firewall sits between the Internet and the internal
network. The inner firewall sits between the DMZ and the subnets that are not
to be accessed by the public.
--- page 36 ---
Ans.

Access Control Directory

One simple way to protect an object is to use a mechanism that works like a file
directory. Imagine we are trying to protect files (the set of objects) from users of a
computing system (the set of subjects). Every file has a unique owner who possesses
“control” access rights (including the rights to declare who has what access) and to revoke
access of any person at any time. Each user has a file directory, which lists all the files to
which that user has access.

Clearly, no user can be allowed to write in the file directory, because that would be a
way to forge access to a file. Therefore, the operating system must maintain all file
directories, under commands from the owners of files. The obvious rights to files are the
common read, write, and execute that are familiar on many shared systems. Furthermore,
another right, owner, is possessed by the owner, permitting that user to grant and revoke
access rights. Figure 2-9 shows an example of a file directory.

User A Directory Files User B Directory

” Access _ File Access _ Fi

FileName Rights Pointer FileName __Rights Pointe
PROGI.C ORW BIBLIOG R e
PROGILEXE | OX Liat TEST-TMP ox |
HELPTXT =| R «| —™ HELPTXT =|R e
HEMP ORW

FIGURE 2-9 Directory Access Rights

This approach is easy to implement because it uses one list per user, naming all the

FR ICR RG IC HH
--- page 37 ---
objects that a user is allowed to access. However, several difficulties can arise. First, the
list becomes too large if many shared objects, such as libraries of subprograms or a
common table of users, are accessible to all users. The directory of each user must have
one entry for each such shared object, even if the user has no intention of accessing the
object. Deletion must be reflected in all directories.

A second difficulty is revocation of access. If owner A has passed to user B the right to
read file F, an entry for F is made in the directory for B. This granting of access implies a
level of trust between A and B. If A later questions that trust, A may want to revoke the
access right of B. The operating system can respond easily to the single request to delete
the right of B to access F, because that action involves deleting one entry from a specific
directory. But if A wants to remove the rights of everyone to access F, the operating
system must search each individual directory for the entry F, an activity that can be time
consuming on a large system. For example, large systems or networks of smaller systems
can easily have 5,000 to 10,000 active accounts. Moreover, B may have passed the access
right for F to another user C, a situation known as propagation of access rights, so A may
not know that C’s access exists and should be revoked. This problem is particularly
serious in a network.

A third difficulty involves pseudonyms. Owners A and B may have two different files
named F, and they may both want to allow access by S. Clearly, the directory for S cannot
contain two entries under the same name for different files. Therefore, S has to be able to
uniquely identify the F for A (or B). One approach is to include the original owner’s
designation as if it were part of the file name, with a notation such as A:F (or B:F).

Suppose, however, that S would like to use a name other than F to make the file’s
contents more apparent. The system could allow S to name F with any name unique to the
directory of S. Then, F from A could be called Q to S. As shown in Figure 2-10, S may
have forgotten that Q is F from A, and so S requests access again from A for F. But by
now A may have more trust in S, so A transfers F with greater rights than before. This
action opens up the possibility that one subject, S, may have two distinct sets of access
rights to F, one under the name Q and one under the name F. In this way, allowing
pseudonyms can lead to multiple permissions that are not necessarily consistent. Thus, the
directory approach is probably too simple for most object protection situations.

FR ICR QA OH
--- page 38 ---
User A Directory Files Directory

nie Access File ais
File Name Rights Pointer <--
F ORWX| ©
BIBLIOG = |ORW FE rw | ef!


HELPTXT = |R Coa HELPTXT |R «
PROGL.EXE |OX ‘Ne |
User B Directory

“ Access _ File
FileName Rights Pointer

HELP-TXT R °
TEMP ORW |

FIGURE 2-10 Ambiguous Access Rights

Access Control Matrix

We can think of the directory as a listing of objects accessible by a single subject, and
the access list as a table identifying subjects that can access a single object. The data in
these two representations are equivalent, the distinction being the ease of use in given
situations.

As an alternative, we can use an access control matrix, shown in Figure 2-11, a table in
which each row represents a subject, each column represents an object, and each entry is
the set of access rights for that subject to that object.

7 objects =
File A Printer System
Clock
Read
2g User W Write Write Read
x Own
3 ‘
a Admin Waite Control
Control

FIGURE 2-11 Access Control Matrix

A more detailed example representation of an access control matrix is shown in Table 2-
8. Access rights shown in that table are O, own; R, read; W, write; and X, execute. In
general, the access control matrix is sparse (meaning that most cells are empty): Most
subjects do not have access rights to most objects. The access matrix can be represented as

FIR ICR QA HH
--- page 39 ---
a list of triples, each having the form Seubject, object, rights), as shown in Table 2-9.

Help (cm
Bibliog | Temp F txt Comp | Linker | Clock | Printer
USER B R - a R x x R Ww
USERS RW - R R x x R Ww
USER T — - R x x x R w
SYS MGR - - - RW Ox Ox ORW oO
USER SVCS | — _ - fe) x x R w

TABLE 2-8 Access Control Matrix

Subject Object Right
USER A Bibliog ORW
USER B Bibliog R
USER S Bibliog RW
USER A Temp ORW
USERA PF ORW
USER S R R

etc.

TABLE 2-9 List of Access Control Triples
This representation may be more efficient than the access control matrix because there

is no triple for any empty cell of the matrix (such as (usER T, Bibliog, -), Even though
the triples can be sorted by subject or object as needed, searching a large number of these
triples is inefficient enough that this implementation is seldom used.

Access Control List

An alternative representation is the access control list; as shown in Figure 2-12, this
representation corresponds to columns of the access control matrix. There is one such list
for each object, and the list shows all subjects who should have access to the object and
what their access is. This approach differs from the directory list because there is one
access control list per object; a directory is created for each subject. Although this
difference seems small, there are some significant advantages to this approach.

FIR ICR QQ FAR RH
--- page 40 ---
File A Printer Systeat

Clock
Read
User W Write Write Read
Own
Admin Write Control
Control

FIGURE 2-12 Access Control List

The access control list representation can include default rights. Consider subjects A
and S, both of whom have access to object F. The operating system will maintain just one
access list for F, showing the access rights for A and S, as shown in Figure 2-13. The
access control list can include general default entries for any users. In this way, specific
users can have explicit rights, and all other users can have a default set of rights. With this
organization, all possible users of the system can share a public file or program without
the need for an entry for the object in the individual directory of each user.

Directory Access Lists Files
File “Star Lawl Rights BIBLIOG
BIBLIOG a   USER_A ORW
TEMP i USERB | R
2 users | RW —_—
ueterst | useR.A | ORW
F
USER_A ORW
users | R
USER_A R HELPTXT
USER_B R
USER_S R
USER_T R
SYSMGR | RW

USER_SVCS | O

FIGURE 2-13 Access Control List with Two Subjects

FRR ICR 71) AH OH
--- page 41 ---
The Multics operating system used a form of access control list in which each user
belonged to three protection classes: a user, a group, and a compartment. The user
designation identified a specific subject, and the group designation brought together
subjects who had a common interest, such as their being coworkers on a project. The
compartment confined an untrusted object; a program executing in one compartment could
not access objects in another compartment without specific permission. The compartment
was also a way to collect objects that were related, such as all files for a single project.

To see how this type of protection might work, suppose every user who initiates access
to the system identifies a group and a compartment with which to work. If Adams logs in
as user Adams in group Decl and compartment Art2, only objects having Adams-Decl-
Art2 in the access control list are accessible in the session.

By itself, this kind of mechanism would be too restrictive to be usable. Adams cannot
create general files to be used in any session. Worse yet, shared objects would not only
have to list Adams as a legitimate subject but also have to list Adams under all acceptable
groups and all acceptable compartments for each group.

The solution is the use of wild cards, meaning placeholders that designate “any user”
(or “any group” or “any compartment”). An access control list might specify access by
Adams-Decl-Artl, giving specific rights to Adams if working in group Decl on
compartment Artl. The list might also specify Adams-*-Artl, meaning that Adams can
access the object from any group in compartment Artl. Likewise, a notation of *-Decl-*
would mean “any user in group Decl in any compartment.” Different placements of the
wildcard notation * have the obvious interpretations.

Unix uses a similar approach with user-group-world permissions. Every user belongs
to a group of related users—students in a common class, workers on a shared project, or
members of the same department. The access permissions for each object are a triple
(u,g,w) in which u is for the access rights of the user, g is for other members of the group,
and w is for all other users in the world.

The access control list can be maintained in sorted order, with * sorted as coming after
all specific names. For example, Adams-Decl-* would come after all specific
compartment designations for Adams. The search for access permission continues just
until the first match. In the protocol, all explicit designations are checked before wild
cards in any position, so a specific access right would take precedence over a wildcard
right. The last entry on an access list could be *-*-*, specifying rights allowable to any
user not explicitly on the access list. With this wildcard device, a shared public object can
have a very short access list, explicitly naming the few subjects that should have access
rights different from the default.

Co-4

SO- b. State and explain in brief the security requirements of databases. [10]

BL-3

7.2 Security Requirements of Databases

The basic security requirements of database systems are not unlike those of other
computing systems we have studied. The basic problems—access control, exclusion of
spurious data, authentication of users, and reliability—have appeared in many contexts so
far in this book. Following is a list of requirements for database security.

+ Physical database integrity. The data of a database are immune from physical
Ans. problems, such as power failures, and someone can reconstruct the database if it

is destroyed through a catastrophe.

+ Logical database integrity. The structure of the database is preserved. With

logical integrity of a database, a modification to the value of one field does not

affect other fields, for example.

+ Element integrity. The data contained in each element are accurate.

+ Auditability. It is possible to track who or what has accessed (or modified) the

FIR IC 77 FIC HOH
--- page 42 ---
elements in the database.

+ Access control. A user is allowed to access only authorized data, and different
users can be restricted to different modes of access (such as read or write).

+ User authentication. Every user is positively identified, both for the audit trail
and for permission to access certain data.

+ Availability. Users can access the database in general and all the data for which
they are authorized.

We briefly examine each of these requirements.
Integrity of the Database

If a database is to serve as a central repository of data, users must be able to trust the
accuracy of the data values. This condition implies that the database administrator must be
assured that updates are performed only by authorized individuals. It also implies that the
data must be protected from corruption, either by an outside illegal program action or by
an outside force such as fire or a power failure. Two situations can affect the integrity of a
database: when the whole database is damaged (as happens, for example, if its storage
medium is damaged) or when individual data items are unreadable.

Integrity of the database as a whole is the responsibility of the DBMS, the operating
system, and the (human) computing system manager. From the perspective of the
operating system and the computing system manager, databases and DBMSs are files and
programs, respectively. Therefore, one way of protecting the database as a whole is to
regularly back up all files on the system. These periodic backups can be adequate controls
against catastrophic failure.

Sometimes an administrator needs to be able to reconstruct the database at the point of a
failure. For instance, when the power fails suddenly, a bank’s clients may be in the middle
of making transactions or students may be registering online for their classes. In these
cases, owners want to be able to restore the systems to a stable point without forcing users
to redo their recently completed transactions.

To handle these situations, the DBMS must maintain a log of transactions. For example,
suppose the banking system is designed so that a message is generated in a log (electronic
or paper or both) each time a transaction is processed. In the event of a system failure, the
system can obtain accurate account balances by reverting to a backup copy of the database
and reprocessing all later transactions from the log.

Element Integrity

The integrity of database elements is their correctness or accuracy. Ultimately,
authorized users are responsible for entering correct data in databases. However, users and
programs make mistakes collecting data, computing results, and entering values.
Therefore, DBMSs sometimes take special action to help catch errors as they are made
and to correct errors after they are inserted.

Databases achieve integrity of the database, its structure, and its
individual elements.

FIR ICR 7 AC HOEK
--- page 43 ---
This corrective action can be taken in three ways: by field checks, through access
control, and with change log.

First, the DBMS can apply field checks, activities that test for appropriate values in a
position. A field might be required to be numeric, an uppercase letter, or one of a set of
acceptable characters. The check ensures that a value falls within specified bounds or is
not greater than the sum of the values in two other fields. These checks prevent simple
errors as the data are entered. (Sidebar 7-1 demonstrates the importance of element
integrity.)

Sidebar 7-1 Element Integrity Failure Crashes Network
Crocker and Bernstein [CRO89] studied catastrophic failures of what was then
known as the ARPANET, the predecessor of today’s Internet. Several failures
came from problems with the routing tables used to direct traffic through the
network.

A 1971 error was called the “black hole.” A hardware failure caused one node
to declare that it was the best path to every other node in the network. This node
sent this declaration to other nodes, which soon propagated the erroneous
posting throughout the network. This node immediately became the black hole
of the network because all traffic was routed to it but never made it to the real
destination.

The ARPANET used simple tables, not a full-featured database management
system, so there was no checking of new values before they were installed in the
distributed routing tables. Had there been a database, integrity-checking
software could have checked for errors in the newly distributed values and
raised a flag for human review.

A second integrity action is afforded by access control. To see why, consider life
without databases. Data files may contain data from several sources, and redundant data
may be stored in several different places. For example, a student’s mailing address may be
stored in many different campus files: in the registrar’s office for formal correspondence,
in the food service office for dining hall privileges, at the bookstore for purchases, and in
the financial aid office for accounting. Indeed, the student may not even be aware that
each separate office has the address on file. If the student moves from one residence to
another, each of the separate files requires correction.

Without a database, you can imagine the risks to the data’s integrity. First, at a given
time, some data files could show the old address (they have not yet been updated) and
some simultaneously have the new address (they have already been updated). Second,
there is always the possibility that someone misentered a data field, again leading to files
with incorrect information. Third, the student may not even be aware of some files, so he
or she does not know to notify the file owner about updating the address information.
These problems are solved by databases. They enable collection and control of this data at
one central source, ensuring the student and users of having the correct address.

However, the centralization is easier said than done. Who owns this shared central file?
Who is authorized to update which elements? What if two people apply conflicting

FIR ICR 72 FIC HOH
--- page 44 ---
modifications? What if modifications are applied out of sequence? How are duplicate
records detected? What action is taken when duplicates are found? These are policy
questions that must be resolved by the database administrator. Sidebar 7-2 describes how
these issues are addressed for managing the configuration of programs; similar formal
processes are needed for managing changes in databases.

Sidebar 7-2 Configuration Management and Access Control

Software engineers must address access control when they manage the
configurations of large computer systems. The code of a major system and
changes to the code over time are actually a database. In many instances
multiple programmers make changes to a system at the same time; the
configuration management database must help ensure that the correct and most
recent changes are stored.

The proliferation of versions and releases can be controlled in three primary
ways. [PFL10a]

+ Separate files: A separate file can be kept for each different version or
release. For instance, version 1 may exist for machines that store all data in
main memory, and version 2 is for machines that must put some data out to
a disk. Suppose the common functions are the same in both versions,
residing in components C, through C,, but memory management is done by
component M, for version 1 and M, for version 2. If new functionality is to
be added to the memory management routines, keeping both versions
current and correct may be difficult; the results must be the same from the
user’s point of view.

+ Deltas: One version of the system is deemed the main version, and all
other versions are considered to be variations from the main version. The
database keeps track only of the differences, in a file called a delta file. The
delta contains commands that are “applied” to the main version to
transform it into the alternative version. This approach saves storage space
but can become unwieldy.

* Conditional compilation: All versions are handled by a single file, and
conditional statements are used to determine which statements apply under
which conditions. In this case, shared code appears only once, so only one
correction is needed if a problem is found. But the code in this single file
can be very complex and difficult to maintain.

In any of these three cases, controlled access to the configuration files is
critical. Two programmers fixing different problems sometimes need to make
changes to the same component. If they do not coordinate access, the second
programmer can inadvertently undo (or worse, wreck) the changes of the first
programmer, resulting in not only recurrence of the initial problems but also
introduction of additional problems. For this reason, files are controlled in
several ways, including being locked while changes are made by one
programmer, and being subject to a group of people called a configuration
control board who ensure that no changed file is put back into production

FIR ICR 7) I ROK HH
--- page 45 ---
without the proper checking and testing. Shari Lawrence Pfleeger and Joanne
Atlee write about these techniques [PFL10a].

The third means of providing database integrity is maintaining a change log for the
database. A change log lists every change made to the database; it contains both original
and modified values. Using this log, a database administrator can undo any changes that
were made in error. For example, a library fine might erroneously be posted against
Charles W. Robertson, instead of Charles M. Robertson, flagging Charles W. Robertson as
ineligible to participate in varsity athletics. Upon discovering this error, the database
administrator obtains Charles W.’s original eligibility value from the log and corrects the
database.

Auditability

For some applications administrators may want to generate an audit record of all access
(read or write) to a database. Such a record can help to maintain the database’s integrity, or
at least to discover after the fact who had affected what values and when. A second
advantage, as we see later, is that users can access protected data incrementally; that is, no
single access reveals protected data, but a set of sequential accesses viewed together
reveals the data, much like discovering the clues in a detective novel. In this case, an audit
trail can identify which clues a user has already been given, as a guide to whether to tell
the user more.

As we note in Chapter 2, granularity can become an impediment in auditing. Audited
events in operating systems are actions like open file or call procedure; they are seldom as
specific as write record 3 or execute instruction I. To be useful for maintaining integrity,
database audit trails should include accesses at the record, field, and even element levels.
This detail is prohibitive for most database applications.

Furthermore, the database management system may access a record but not report the
data to a user, as when the user performs a select operation. For example, a residence hall
advisor might want a count of all students who have failed elementary French, and the
database management system reports 462. To get that number the system had to inspect all
student records and note those with failing grades, and it performed this lookup on behalf
of the advisor who is appropriately listed in the log as receiving the data. Thus, in a sense,
the advisor accessed all those student grades, although from the number 462 the advisor
cannot determine the grade of any individual student. (Accessing a record or an element
without transferring to the user the data received is called the pass-through problem.)
Thus, a log of all records accessed directly may both overstate and understate what a user
actually learns. The problem is even more nuanced than what we describe here, and we
consider some intricacies of disclosure later in this chapter.

Access Control

Databases are often separated logically by user access privileges. For example, all users
can be granted access to general data, but only the personnel department can obtain salary
data and only the marketing department can obtain sales data. Databases are useful
because they centralize the storage and maintenance of data. Limited access is both a
responsibility and a benefit of this centralization.

FRAC 7D AC HOH
--- page 46 ---
The database administrator specifies who should be allowed access to which data, at the
view, relation, field, record, or even element level. The DBMS must enforce this policy,
granting access to all specified data or no access where prohibited. Furthermore, the
number of modes of access can be many. A user or program may have the right to read,
change, delete, or append to a value, add or delete entire fields or records, or reorganize
the entire database.

Superficially, access control for a database seems like access control for an operating
system or any other component of a computing system. However, the database problem is
more complicated, as we see throughout this chapter. Operating system objects, such as
files, are unrelated items, whereas records, fields, and elements are related. Although a
user probably cannot determine the contents of one file by reading others, a user might be
able to determine one data element just by reading others. The problem of obtaining data
values from others is called inference, and we consider it in depth later in this chapter.

It is important to notice that you can access data by inference without needing direct
access to the secure object itself. Restricting inference may mean prohibiting certain paths
to prevent possible inferences. However, restricting access to control inference also limits
queries from users who do not intend unauthorized access to values. Moreover, attempts to
check requested accesses for possible unacceptable inferences may actually degrade the
DBMS’s performance.

Finally, size or granularity is different between operating system objects and database
objects. An operating system can readily control access to files, as we explain in Chapter
5. However an access control list of several hundred files is much easier to implement
than an access control list for a database with several hundred files of perhaps a hundred
fields each. Size affects the efficiency of processing. Operating systems do not usually
“see into” a file to control access to items within a file.

Database management systems implement their own access control at a
level finer than what an operating system handles.

User Authentication

The DBMS can require rigorous user authentication. For example, a DBMS might insist
that a user pass both specific password and time-of-day checks. This authentication
supplements the authentication performed by the operating system. Typically, the DBMS
runs as an application program on top of the operating system. This system design means
that there is no trusted path from the DBMS to the operating system, so the DBMS must
be suspicious of any data it receives, including a user identity from the operating system.
Thus, the DBMS is forced to do its own authentication.

Availability

A DBMS has aspects of both a program and a system. It is a program that uses other
hardware and software resources, yet to many users it is the only application run. Users
often take the DBMS for granted, employing it as an essential tool with which to perform

particular tasks. But when the system is not available—busy serving other users or down
to be repaired or upgraded—the users are very aware of a DBMS’s unavailability. For

FIR ICR 7] 6 AC HOH
--- page 47 ---
example, two users may request the same record, and the DBMS must arbitrate; one user
is bound to be denied access for a while. Or the DBMS may withhold unprotected data to
avoid revealing protected data, leaving the requesting user unhappy. We examine these
problems in more detail later in this chapter. Problems like these result in high availability
requirements for a DBMS.

Integrity/Confidentiality/Availability

The three aspects of computer security—integrity, confidentiality, and availability—
clearly relate to database management systems. As we have described, integrity applies to
the individual elements of a database as well as to the database as a whole. Integrity is also
a property of the structure of the database (elements in one table correspond one to one
with those of another) and of the relationships of the database (records having the same
unique identifier, called a key, are related). Thus, integrity is a major concern in the design
of database management systems. We look more closely at integrity issues in the next
section.

Confidentiality is likewise a key issue with databases because databases are often used
to implement controlled sharing of sensitive data. Access to data can be direct (you
request a record and the database provides it) or indirect (you request some records and
from those results infer or intuit other data). Controlling direct access employs the access
control techniques we describe in Chapters 2 and 5. Indirect access, however, is more
difficult to control, and we explore it in more depth later in this chapter.

Finally, availability is important because of the shared access motivation underlying
database development. However, availability conflicts with confidentiality. The last
sections of the chapter address availability in an environment in which confidentiality is
also important.

Q7 [20]
Co-1

SO- a. Explain vulnerability-threat-control paradigm with respective to CIA. [10]
BL-2

The Vulnerability-Threat—Control Paradigm

The goal of computer security is protecting valuable assets. To study different ways of
protection, we use a framework that describes how assets may be harmed and how to

counter or mitigate that harm.

Ans. sea: . . .
A vulnerability is a weakness in the system, for example, in procedures, design, or

implementation, that might be exploited to cause loss or harm. For instance, a particular
system may be vulnerable to unauthorized data manipulation because the system does not
verify a user’s identity before allowing data access.

FRR IC 7 IC ROKK
--- page 48 ---
A vulnerability is a weakness that could be exploited to cause harm.

A threat to a computing system is a set of circumstances that has the potential to cause
loss or harm. To see the difference between a threat and a vulnerability, consider the
illustration in Figure 1-4. Here, a wall is holding water back. The water to the left of the
wall is a threat to the man on the right of the wall: The water could rise, overflowing onto
the man, or it could stay beneath the height of the wall, causing the wall to collapse. So the
threat of harm is the potential for the man to get wet, get hurt, or be drowned. For now, the
wall is intact, so the threat to the man is unrealized.

mit

FIGURE 1-4 Threat and Vulnerability

A threat is a set of circumstances that could cause harm.

However, we can see a small crack in the wall—a vulnerability that threatens the man’s
security. If the water rises to or beyond the level of the crack, it will exploit the
vulnerability and harm the man.

There are many threats to a computer system, including human-initiated and computer-
initiated ones. We have all experienced the results of inadvertent human errors, hardware
design flaws, and software failures. But natural disasters are threats, too; they can bring a
system down when the computer room is flooded or the data center collapses from an
earthquake, for example.

A human who exploits a vulnerability perpetrates an attack on the system. An attack
can also be launched by another system, as when one system sends an overwhelming flood
of messages to another, virtually shutting down the second system’s ability to function.
Unfortunately, we have seen this type of attack frequently, as denial-of-service attacks
deluge servers with more messages than they can handle. (We take a closer look at denial
of service in Chapter 6.)

How do we address these problems? We use a control or countermeasure as

--- page 49 ---
protection. That is, a control is an action, device, procedure, or technique that removes or
reduces a vulnerability. In Figure 1-4, the man is placing his finger in the hole, controlling
the threat of water leaks until he finds a more permanent solution to the problem. In
general, we can describe the relationship between threats, controls, and vulnerabilities in
this way:

Controls prevent threats from exercising vulnerabilities.

A threat is blocked by control of a vulnerability.

Before we can protect assets, we need to know the kinds of harm we have to protect
them against, so now we explore threats to valuable assets.

1.2 Threats

We can consider potential harm to assets in two ways: First, we can look at what bad
things can happen to assets, and second, we can look at who or what can cause or allow
those bad things to happen. These two perspectives enable us to determine how to protect
assets.

Think for a moment about what makes your computer valuable to you. First, you use it
as a tool for sending and receiving email, searching the web, writing papers, and
performing many other tasks, and you expect it to be available for use when you want it.
Without your computer these tasks would be harder, if not impossible. Second, you rely
heavily on your computer’s integrity. When you write a paper and save it, you trust that
the paper will reload exactly as you saved it. Similarly, you expect that the photo a friend
passes you on a flash drive will appear the same when you load it into your computer as
when you saw it on your friend’s computer. Finally, you expect the “personal” aspect of a
personal computer to stay personal, meaning you want it to protect your confidentiality.
For example, you want your email messages to be just between you and your listed
recipients; you don’t want them broadcast to other people. And when you write an essay,
you expect that no one can copy it without your permission.

These three aspects, confidentiality, integrity, and availability, make your computer
valuable to you. But viewed from another perspective, they are three possible ways to
make it less valuable, that is, to cause you harm. If someone steals your computer,
scrambles data on your disk, or looks at your private data files, the value of your computer
has been diminished or your computer use has been harmed. These characteristics are both
basic security properties and the objects of security threats.

We can define these three properties as follows.
+ availability: the ability of a system to ensure that an asset can be used by any
authorized parties
+ integrity: the ability of a system to ensure that an asset is modified only by
authorized parties
+ confidentiality: the ability of a system to ensure that an asset is viewed only
by authorized parties

FRI ICR 7. AC OH
--- page 50 ---
These three properties, hallmarks of solid security, appear in the literature as early as
James P. Anderson’s essay on computer security [AND73] and reappear frequently in
more recent computer security papers and discussions. Taken together (and rearranged),
the properties are called the C-I-A triad or the security triad. ISO 7498-2 [ISO89] adds
to them two more properties that are desirable, particularly in communication networks:

+ authentication: the ability of a system to confirm the identity of a sender

* nonrepudiation or accountability: the ability of a system to confirm that a
sender cannot convincingly deny having sent something

The U.S. Department of Defense [DOD85] adds auditability: the ability of a system to
trace all actions related to a given asset. The C-I-A triad forms a foundation for thinking
about security. Authenticity and nonrepudiation extend security notions to network
communications, and auditability is important in establishing individual accountability for
computer activity. In this book we generally use the C-I-A triad as our security taxonomy
so that we can frame threats, vulnerabilities, and controls in terms of the C-I-A properties
affected. We highlight one of these other properties when it is relevant to a particular
threat we are describing. For now, we focus on just the three elements of the triad.

C-I-A triad: confidentiality, integrity, availability

What can happen to harm the confidentiality, integrity, or availability of computer
assets? If a thief steals your computer, you no longer have access, so you have lost
availability; furthermore, if the thief looks at the pictures or documents you have stored,
your confidentiality is compromised. And if the thief changes the content of your music
files but then gives them back with your computer, the integrity of your data has been
harmed. You can envision many scenarios based around these three properties.

The C-I-A triad can be viewed from a different perspective: the nature of the harm
caused to assets. Harm can also be characterized by four acts: interception, interruption,
modification, and fabrication. These four acts are depicted in Figure 1-5. From this point
of view, confidentiality can suffer if someone intercepts data, availability is lost if
someone or something interrupts a flow of data or access to a computer, and integrity can
fail if someone or something modifies data or fabricates false data. Thinking of these four
kinds of acts can help you determine what threats might exist against the computers you
are trying to protect.

FR ICR 0) AC RH
--- page 51 ---
es)

Interception Interruption

—o

Modification Fabrication
FIGURE 1-5 Four Acts to Cause Security Harm

To analyze harm, we next refine the C-I-A triad, looking more closely at each of its
elements.

Confidentiality

Some things obviously need confidentiality protection. For example, students’ grades,
financial transactions, medical records, and tax returns are sensitive. A proud student may
run out of a classroom screaming “I got an A!” but the student should be the one to choose
whether to reveal that grade to others. Other things, such as diplomatic and military
secrets, companies’ marketing and product development plans, and educators’ tests, also
must be carefully controlled. Sometimes, however, it is not so obvious that something is
sensitive. For example, a military food order may seem like innocuous information, but a
sudden increase in the order could be a sign of incipient engagement in conflict. Purchases
of food, hourly changes in location, and access to books are not things you would
ordinarily consider confidential, but they can reveal something that someone wants to be
kept confidential.

The definition of confidentiality is straightforward: Only authorized people or systems
can access protected data. However, as we see in later chapters, ensuring confidentiality
can be difficult. For example, who determines which people or systems are authorized to
access the current system? By “accessing” data, do we mean that an authorized party can
access a single bit? the whole collection? pieces of data out of context? Can someone who
is authorized disclose data to other parties? Sometimes there is even a question of who
owns the data: If you visit a web page, do you own the fact that you clicked on a link, or
does the web page owner, the Internet provider, someone else, or all of you?

In spite of these complicating examples, confidentiality is the security property we
understand best because its meaning is narrower than that of the other two. We also
understand confidentiality well because we can relate computing examples to those of

FRR ICR 7 FA HH
--- page 52 ---
preserving confidentiality in the real world.

Confidentiality relates most obviously to data, although we can think of the
confidentiality of a piece of hardware (a novel invention) or a person (the whereabouts of
a wanted criminal). Here are some properties that could mean a failure of data
confidentiality:

+ An unauthorized person accesses a data item.
+ An unauthorized process or program accesses a data item.

+ A person authorized to access certain data accesses other data not authorized
(which is a specialized version of “an unauthorized person accesses a data
item”).

+ An unauthorized person accesses an approximate data value (for example, not
knowing someone’s exact salary but knowing that the salary falls in a particular
range or exceeds a particular amount).

+ An unauthorized person learns the existence of a piece of data (for example,
knowing that a company is developing a certain new product or that talks are
underway about the merger of two companies).

Notice the general pattern of these statements: A person, process, or program is (or is
not) authorized to access a data item in a particular way. We call the person, process, or
program a subject, the data item an object, the kind of access (such as read, write, or
execute) an access mode, and the authorization a policy, as shown in Figure 1-6. These
four terms reappear throughout this book because they are fundamental aspects of
computer security.

Policy:
Who + What + How= Yes/No

Object
Mode of access (what)

Subject | im (how) we
(who)

FIGURE 1-6 Access Control

One word that captures most aspects of confidentiality is view, although you should not
take that term literally. A failure of confidentiality does not necessarily mean that someone

FRI ICR DD A HH
--- page 53 ---
sees an object and, in fact, it is virtually impossible to look at bits in any meaningful way
(although you may look at their representation as characters or pictures). The word view
does connote another aspect of confidentiality in computer security, through the
association with viewing a movie or a painting in a museum: look but do not touch. In
computer security, confidentiality usually means obtaining but not modifying.
Modification is the subject of integrity, which we consider in the next section.

Integrity

Examples of integrity failures are easy to find. A number of years ago a malicious
macro in a Word document inserted the word “not” after some random instances of the
word “is;” you can imagine the havoc that ensued. Because the document was generally
syntactically correct, people did not immediately detect the change. In another case, a
model of the Pentium computer chip produced an incorrect result in certain circumstances
of floating-point arithmetic. Although the circumstances of failure were rare, Intel decided
to manufacture and replace the chips. Many of us receive mail that is misaddressed
because someone typed something wrong when transcribing from a written list. A worse
situation occurs when that inaccuracy is propagated to other mailing lists such that we can
never seem to correct the root of the problem. Other times we find that a spreadsheet
seems to be wrong, only to find that someone typed “space 123” in a cell, changing it from
a numeric value to text, so the spreadsheet program misused that cell in computation.
Suppose someone converted numeric data to roman numerals: One could argue that IV is
the same as 4, but IV would not be useful in most applications, nor would it be obviously
meaningful to someone expecting 4 as an answer. These cases show some of the breadth
of examples of integrity failures.

Integrity is harder to pin down than confidentiality. As Stephen Welke and Terry
Mayfield [WEL90, MAY91, NCS91a] point out, integrity means different things in
different contexts. When we survey the way some people use the term, we find several
different meanings. For example, if we say that we have preserved the integrity of an item,
we may mean that the item is

* precise

* accurate

* unmodified

* modified only in acceptable ways

* modified only by authorized people

* modified only by authorized processes
* consistent

+ internally consistent

* meaningful and usable

Integrity can also mean two or more of these properties. Welke and Mayfield recognize
three particular aspects of integrity—authorized actions, separation and protection of
resources, and error detection and correction. Integrity can be enforced in much the same

way as can confidentiality: by rigorous control of who or what can access which resources
in what ways.

FRR ICR 3 FI HR Ha
--- page 54 ---
Availability

A computer user’s worst nightmare: You turn on the switch and the computer does
nothing. Your data and programs are presumably still there, but you cannot get at them.
Fortunately, few of us experience that failure. Many of us do experience overload,

however: access gets slower and slower; the computer responds but not in a way we
consider normal or acceptable.

Availability applies both to data and to services (that is, to information and to
information processing), and it is similarly complex. As with the notion of confidentiality,
different people expect availability to mean different things. For example, an object or
service is thought to be available if the following are true:

+ It is present in a usable form.

+ It has enough capacity to meet the service’s needs.

+ It is making clear progress, and, if in wait mode, it has a bounded waiting time.
+ The service is completed in an acceptable period of time.

We can construct an overall description of availability by combining these goals.
Following are some criteria to define availability.

+ There is a timely response to our request.

+ Resources are allocated fairly so that some requesters are not favored over
others.

* Concurrency is controlled; that is, simultaneous access, deadlock management,
and exclusive access are supported as required.

+ The service or system involved follows a philosophy of fault tolerance,
whereby hardware or software faults lead to graceful cessation of service or to
work-arounds rather than to crashes and abrupt loss of information. (Cessation
does mean end; whether it is graceful or not, ultimately the system is
unavailable. However, with fair warning of the system’s stopping, the user may
be able to move to another system and continue work.)

+ The service or system can be used easily and in the way it was intended to be
used. (This is a characteristic of usability, but an unusable system may also
cause an availability failure.)

As you can see, expectations of availability are far-reaching. In Figure 1-7 we depict
some of the properties with which availability overlaps. Indeed, the security community is
just beginning to understand what availability implies and how to ensure it.

FRR ICD A HOEK
--- page 55 ---
Performance
Availability

FIGURE 1-7 Availability and Related Aspects

A person or system can do three basic things with a data item: view it, modify it, or use
it. Thus, viewing (confidentiality), modifying (integrity), and using (availability) are the
basic modes of access that computer security seeks to preserve.

Computer security seeks to prevent unauthorized viewing
(confidentiality) or modification (integrity) of data while preserving access
(availability).

A paradigm of computer security is access control: To implement a policy, computer
security controls all accesses by all subjects to all protected objects in all modes of access.
A small, centralized control of access is fundamental to preserving confidentiality and
integrity, but it is not clear that a single access control point can enforce availability.
Indeed, experts on dependability will note that single points of control can become single
points of failure, making it easy for an attacker to destroy availability by disabling the
single control point. Much of computer security’s past success has focused on
confidentiality and integrity; there are models of confidentiality and integrity, for example,
see David Bell and Leonard La Padula [BEL73, BEL76] and Kenneth Biba [BIB77].
Availability is security’s next great challenge.

We have just described the C-I-A triad and the three fundamental security properties it
represents. Our description of these properties was in the context of things that need
protection. To motivate your understanding we gave some examples of harm and threats to
cause harm. Our next step is to think about the nature of threats themselves.

Types of Threats
For some ideas of harm, look at Figure 1-8, taken from Willis Ware’s report [WAR70].

FRI ICR DD A HH
--- page 56 ---
Although it was written when computers were so big, so expensive, and so difficult to
operate that only large organizations like universities, major corporations, or government
departments would have one, Ware’s discussion is still instructive today. Ware was
concerned primarily with the protection of classified data, that is, preserving
confidentiality. In the figure, he depicts humans such as programmers and maintenance
staff gaining access to data, as well as radiation by which data can escape as signals. From
the figure you can see some of the many kinds of threats to a computer system.

COMPUTER NETWORK VULNERABILITIES
RADIAT!
TAPS

Tehri

[—— COMMUNICATION
ine . PROCESSOR : LINES

SWITCHING |
CENTER |)

FIGURE 1-8 Computer [Network] Vulnerabilities (from [WAR70])

One way to analyze harm is to consider the cause or source. We call a potential cause of
harm a threat. Harm can be caused by either nonhuman events or humans. Examples of
nonhuman threats include natural disasters like fires or floods; loss of electrical power;
failure of a component such as a communications cable, processor chip, or disk drive; or
attack by a wild boar.

Threats are caused both by human and other sources.

Human threats can be either benign (nonmalicious) or malicious. Nonmalicious kinds
of harm include someone’s accidentally spilling a soft drink on a laptop, unintentionally
deleting text, inadvertently sending an email message to the wrong person, and carelessly
typing “12” instead of “21” when entering a phone number or clicking “yes” instead of
“no” to overwrite a file. These inadvertent, human errors happen to most people; we just
hope that the seriousness of harm is not too great, or if it is, that we will not repeat the
mistake.

Threats can be malicious or not.

Most computer security activity relates to malicious, human-caused harm: A

FRR ICR DG FAC HH
--- page 57 ---
malicious person actually wants to cause harm, and so we often use the term attack for a
malicious computer security event. Malicious attacks can be random or directed. In a
random attack the attacker wants to harm any computer or user; such an attack is
analogous to accosting the next pedestrian who walks down the street. An example of a
random attack is malicious code posted on a website that could be visited by anybody.

In a directed attack, the attacker intends harm to specific computers, perhaps at one
organization (think of attacks against a political organization) or belonging to a specific
individual (think of trying to drain a specific person’s bank account, for example, by
impersonation). Another class of directed attack is against a particular product, such as
any computer running a particular browser. (We do not want to split hairs about whether
such an attack is directed—at that one software product—or random, against any user of
that product; the point is not semantic perfection but protecting against the attacks.) The
range of possible directed attacks is practically unlimited. Different kinds of threats are
shown in Figure 1-9.

Threats
Natural Human
causes causes
Examples: Fire, A i
Pes Benign Malicious
power failure 4
intent intent

Example:
Human error

Random Directed
Example: Malicious Example:
code on a general Impersonation

web site

FIGURE 1-9 Kinds of Threats

Threats can be targeted or random.

Although the distinctions shown in Figure 1-9 seem clear-cut, sometimes the nature of
an attack is not obvious until the attack is well underway, or perhaps even ended. A
normal hardware failure can seem like a directed, malicious attack to deny access, and
hackers often try to conceal their activity to look like ordinary, authorized users. As
computer security experts we need to anticipate what bad things might happen, instead of
waiting for the attack to happen or debating whether the attack is intentional or accidental.

FRR ICR D7 AC OH
--- page 58 ---
Neither this book nor any checklist or method can show you all the kinds of harm that
can happen to computer assets. There are too many ways to interfere with your use of
these assets. Two retrospective lists of known vulnerabilities are of interest, however. The
Common Vulnerabilities and Exposures (CVE) list (see http://cve.mitre.org/) is a
dictionary of publicly known security vulnerabilities and exposures. CVE’s common
identifiers enable data exchange between security products and provide a baseline index
point for evaluating coverage of security tools and services. To measure the extent of
harm, the Common Vulnerability Scoring System (CVSS) (see
http://nvd.nist.gov/cvss.cfm) provides a standard measurement system that allows accurate
and consistent scoring of vulnerability impact.

Advanced Persistent Threat

Security experts are becoming increasingly concerned about a type of threat called
advanced persistent threat. A lone attacker might create a random attack that snares a
few, or a few million, individuals, but the resulting impact is limited to what that single
attacker can organize and manage. A collection of attackers—think, for example, of the
cyber equivalent of a street gang or an organized crime squad—might work together to
purloin credit card numbers or similar financial assets to fund other illegal activity. Such
attackers tend to be opportunistic, picking unlucky victims’ pockets and moving on to
other activities.

Advanced persistent threat attacks come from organized, well financed, patient
assailants. Often affiliated with governments or quasi-governmental groups, these
attackers engage in long term campaigns. They carefully select their targets, crafting
attacks that appeal to specifically those targets; email messages called spear phishing
(described in Chapter 4) are intended to seduce their recipients. Typically the attacks are
silent, avoiding any obvious impact that would alert a victim, thereby allowing the
attacker to exploit the victim’s access rights over a long time.

The motive of such attacks is sometimes unclear. One popular objective is economic
espionage. A series of attacks, apparently organized and supported by the Chinese
government, was used in 2012 and 2013 to obtain product designs from aerospace
companies in the United States. There is evidence the stub of the attack code was loaded
into victim machines long in advance of the attack; then, the attackers installed the more
complex code and extracted the desired data. In May 2014 the Justice Department indicted
five Chinese hackers in absentia for these attacks.

In the summer of 2014 a series of attacks against J.P. Morgan Chase bank and up to a
dozen similar financial institutions allowed the assailants access to 76 million names,
phone numbers, and email addresses. The attackers—and even their country of origin—
remain unknown, as does the motive. Perhaps the attackers wanted more sensitive
financial data, such as account numbers or passwords, but were only able to get the less
valuable contact information. It is also not known if this attack was related to an attack a
year earlier that disrupted service to that bank and several others.

To imagine the full landscape of possible attacks, you may find it useful to consider the
kinds of people who attack computer systems. Although potentially anyone is an attacker,
certain classes of people stand out because of their backgrounds or objectives. Thus, in the

Co-4

SO- b. Discuss the hybrid Chinese Wall Model of security policy. [10]

BL-3

8.1. Chinese Wall Model

The Chinese Wall model [292] is a model of a security policy that refers equally to
confidentiality and integrity. It describes policies that involve a conflict of interest
in business, and is as important to those situations as the Bell-LaPadula Model

Ans. is to the military. For example, British law requires the use of a policy similar to
this, and correct implementation of portions of the model provides a defense in
cases involving certain criminal charges [2157, 2215]. The environment of a stock
exchange or investment house is the most natural environment for this model. In
this context, the goal of the model is to prevent a conflict of interest in which a
trader represents two clients, and the best interests of the clients conflict, so the
trader could help one gain at the expense of the other.

FRR ICR DQ ACH HH
--- page 59 ---
8.1.1 Informal Description

Consider the database of an investment house. It consists of companies’ records
about investment and other data that investors are likely to request. Analysts use
these records to guide the companies’ investments, as well as those of individuals.
Suppose Anthony counsels National Bank in its investments. If he also counsels
City Bank in its investments, he has a potential conflict of interest, because the
two banks’ investments may come into conflict. Hence, Anthony cannot counsel
both banks.
The following definitions capture this:

Definition 8-1. The objects of the database are items of information related
to a company.

Definition 8-2. A company dataset (CD) contains objects related to a single
company.

Definition 8-3. A conflict of interest class (COI) contains the datasets of
companies in competition.

Let COI(O) represent the COI class that contains object O, and let CD(O)
be the company dataset that contains object O. The model assumes that each
object belongs to exactly one COI class.

Anthony has access to the objects in the CD of National Bank. Because
the CD of City Bank is in the same COI class as that of National Bank, Anthony
cannot gain access to the objects in City Bank’s CD. Thus, this structure of the
database provides the required ability. (See Figure 8-1.)

This implies a temporal element. Suppose Anthony first worked on
National Bank’s portfolio and was then transferred to City Bank’s portfolio. Even

Bank COI Class Oil Company COI Class
National Bank Car Oil Co. Grease Co.
(a) (s) (e)
City Bank River Bank Veg Oil Co. Oil Co.
(c) (b) (u) (n)

Figure 8-1 The Chinese Wall model database. It has two COI classes. The one
for banks contains three CDs. The other one, for oil companies, contains four
CDs. Susan may have access to no more than one CD in each COI, so she could
access City Bank’s CD and Veg Oil Co.’s CD, but not City Bank’s CD and National
Bank’s CD.

FRR ICR DQ A HH
--- page 60 ---
though he is working only on one CD in the bank COI class at a time, much of
the information he learned from National Bank’s portfolio will be current. Hence,
he can guide City Bank’s investments using information about National Bank—
a conflict of interest. This leads to the following rule, where PR(S) is the set of
objects that S has read.

CW-Simple Security Condition, Preliminary Version: S can read O if and only if
either of the following is true:

1. There is an object O’ such that S has accessed O' and CD(O’) = CD(O).
2. For all objects O', O' € PR(S) > COI(O’) # COI(O).

Initially, PR(S) = @, and the initial read request is assumed to be granted.
Given these assumptions, in the situation above, National Bank’s COI class and
City Bank’s COI class are the same, so the second part of the CW-simple security
condition applies, and Anthony cannot access an object in the former, having
already accessed an object in the latter.

Two immediate consequences of this rule affect subject rights. First, once
a subject reads any object in a COI class, the only other objects in that COI class
that the subject can read are in the same CD as the read object. So, if Susan
accesses some information in City Bank’s CD, she cannot later access information
in National Bank’s CD.

Second, the minimum number of subjects needed to access every object
in a COI class is the same as the number of CDs in that COI class. If the oil
company COI class has four CDs, then at least four analysts are needed to access
all information in the COI class. Thus, any trading house must have at least four
analysts to access all information in that COI class without creating a conflict of
interest.

In practice, companies have information they can release publicly, such
as annual stockholders’ reports and filings before government commissions. The
Chinese Wall model should not consider this information restricted, because
it is available to all. Hence, the model distinguishes between sanitized data
and unsanitized data; the latter falls under the CW-simple security condition,
preliminary version, whereas the former does not.

This means that sanitized objects must reside in a COI class with a single
CD consisting only of sanitized objects. (See Exercise 1.)

The CW-simple security condition can be reformulated to include this
notion.

CW-Simple Security Condition: S can read O if and only if any of the following
is true:

1. There is an object O’ such that S has accessed O’ and CD(O’) = CD(O).
2. For all objects O’, O' € PR(S) => COI(O’) # COI(O).
3. Oisa sanitized object.

Suppose Anthony and Susan work in the same trading house. Anthony can
read objects in National Bank’s CD, and Susan can read objects in City Bank’s
CD. Both can read objects in Veg Oil’s CD. If Anthony can also write to objects in
Veg Oil’s CD, then he can read information from objects in National Bank’s CD
and write to objects in Veg Oil’s CD, and then Susan can read that information;
so, Susan can indirectly obtain information from National Bank’s CD, causing
a conflict of interest. The CW-simple security condition must be augmented to
prevent this.

CW-*-Property: A subject S may write to an object O if and only if both of the
following conditions hold:

1. The CW-simple security condition permits S to read O.
2. For all unsanitized objects O’, S can read O' > CD(O') = CD(O).

In the example above, Anthony can read objects in both National Bank’s
CD and Veg Oil’s CD. Thus, condition 1 is met. However, assuming that National
Bank’s CD contains unsanitized objects (a reasonable assumption), then because
Anthony can read those objects, condition 2 is false. Hence, Anthony cannot write
to objects in Veg Oil’s CD.

FI ICR GQ) AC HH
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 1c4eb80ee8e8

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CSE_DS_7011/Information Security/ANS_Information Security(702CO0C039)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2026
- Text: mixed (52 pages), mean OCR confidence 91.7
- 11 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Information Security
Date: 01 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 52 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1
List the threat consequences and the types of threats actions that caused each
SO-   a.   [5]
consequence.
BL-1
Ans.
CO-3
b.   Compare and contrast symmetric and asymmetric key cryptography.   [5]
SO-
********** 1 **********

[Text in pictures on this page, read by OCR]
Threat Consequence Threat Action (attack)

Unauthorized Disclosure Exposure: Sensitive data are directly released to an unauthorized
A. circumstance or event whereby entity.
to data for Interception: An unauthorized entity directly accesses sensitive
which the entity is not authorized. data traveling between authorized sources and destinations.

Inference: A threat action whereby an unauthoried entity
indirectly accesses scnsitive data (but not necessarily the
data contained in the communication) by reasoning from
characteristics or by-products of communications.

Intrusion: An unauthorized entity gains access to sensitive data
by circumventing a system's security protections.

Deception Masquerade: An unauthorized entity gains access to a system or
A circumstance or event that performs a malicious act by posing as an authorized entity.
may result in an authorized entity Falsificati False data deceive an authorized entity.

Sansa ets abled haber i Repudiation: An entity deceives another by falsely denying
HORE A responsibility for an act. , _—

Disruption Incapacitation: Prevents or interrupts system operation by
A circumstance or event that disabling a system component.
interrupts or prevents the correct Corruption: Undesirably alters system operation by adversely
(FEEL ion of system services and modifying system functions or data.
funetions. Obstruction: A threat action that interrupts delivery of system

services by hindering system operation.

Usurpation Misappropriation: An entity assumes unauthorized logical or
A. circumstance or event that results physical control of a system resource.
in control of system services or Misuse: Causes a system component to perform a function or

functions by an unauthorized entity. service that is detrimental to system security.
--- page 2 ---
BL-4

SYMMETRIC VS. ASYMMETRIC KEY CRYPTOGRAPHY

Characteristic Symmetric Key Asymmetric Key
Cryptography Cryptography
Key Used Same key for encryption & decryption One key for encryption & different
key for decryption
Speed Very fast Slower
Ans. Key agreement/exchange Abig problem No problem at all
Size of encrypted text Usually same or less than the original More than the PT size
PT size
No. of keys required as Equals about square of the no. of Same as the no. of participants
compared to participants participants
Usage Provide confidentiality. Can also provide authentication and
Cant be used for digital signature nonrepudiation.
Used for digital signature
Example DES, AES, Blowfish, RC4, RC5, RSA, Diffie-Hellman, El] Gamal,
ECC
CO-2
SO- c. What are the counter measures of SQLi attacks. [5]
BL-1

FIC 2 I HH ar
--- page 3 ---
Ans.
CO-3
How tokens are used for authentication. Describe active, passive, static and dynamic
SO-   d.   [5]
tokens.
BL-2
********** 3 **********

[Text in pictures on this page, read by OCR]
SQLi Countermeasures

Because SQLi attacks are so prevalent, damaging, and varied both by attack avenue
and type, a single countermeasure is insufficient. Rather an integrated set of tech-
niques is necessary. In this section, we provide a brief overview of the types of coun-
termeasures that are in use or being researched, using the classification in [SHAR 13].
These countermeasures can be classified into three types: defensive coding, detection,
and run-time prevention.

Many SOQLi attacks succeed because developers have used insecure coding prac-
tices, as we discuss in Chapter 11. Thus, defensive coding is an effective way to dramati-
cally reduce the threat from SQLi. Examples of defensive coding include the following:

e Manual defensive coding practices: A common vulnerability exploited by SQLi
attacks is insufficient input validation. The straightforward solution for elimi-
nating these vulnerabilities is to apply suitable defensive coding practices. An
example is input type checking, to check that inputs that are supposed to be
numeric contain no characters other than digits. This type of technique can
avoid attacks based on forcing errors in the database management system.
Another type of coding practice is one that performs pattern matching to try
to distinguish normal input from abnormal input.

e Parameterized query insertion: This approach attempts to prevent SQLi by
allowing the application developer to more accurately specify the structure
of an SOL query, and pass the value parameters to it separately such that any
unsanitary user input is not allowed to modify the query structure.

¢ SQL DOM: SOL DOM isa set of classes that enables automated data type vali-
dation and escaping [MCCLOS5]. This approach uses encapsulation of database
queries to provide a safe and reliable way to access databases. This changes the
query-building process from an unregulated one that uses string concatenation
to a systematic one that uses a type-checked API. Within the API, developers
are able to systematically apply coding best practices such as input filtering and
rigorous type checking of user input.

A variety of detection methods have been developed, including the following:

e Signature-based: This technique attempts to match specific attack patterns.
Such an approach must be constantly updated and may not work against self-
modifying attacks.

e Anomaly-based: This approach attempts to define normal behavior then
detect behavior patterns outside the normal range. A number of approaches

have been used. In general terms, there is a training phase, in which the
system learns the range of normal behavior, followed by the actual detec-
tion phase.

e Code analysis: Code analysis techniques involve the use of a test suite to detect
SQLi vulnerabilities. The test suite is designed to generate a wide range of SQLi
attacks and assess the response of the system.

Finally, a number of run-time prevention techniques have been developed as
SQLi countermeasures. These techniques check queries at runtime to see if they
conform to a model of expected queries. Various automated tools are available for
this purpose [CHAN11, SHAR13].
--- page 4 ---
Ans.

Authentication Based on Tokens: Something You Have

Something you have means that you have a physical object in your possession. One
physical authenticator with which you are probably familiar is a key. When you put your
key in your lock, the ridges in the key interact with pins in the lock to let the mechanism
turn. In a sense the lock authenticates you for authorized entry because you possess an
appropriate key. Of course, you can lose your key or duplicate it and give the duplicate to
someone else, so the authentication is not perfect. But it is precise: Only your key works,
and your key works only your lock. (For this example, we intentionally ignore master
keys.)

Other familiar examples of tokens are badges and identity cards. You may have an
“affinity card”: a card with a code that gets you a discount at a store. Many students and
employees have identity badges that permit them access to buildings. You must have an
identity card or passport to board an airplane or enter a foreign country. In these cases you
possess an object that other people recognize to allow you access or privileges.

Another kind of authentication token has data to communicate invisibly. Examples of
this kind of token include credit cards with a magnetic stripe, credit cards with an
embedded computer chip, or access cards with passive or active wireless technology. You
introduce the token into an appropriate reader, and the reader senses values from the card.
If your identity and values from your token match, this correspondence adds confidence
that you are who you say you are.

We describe different kinds of tokens next.
Active and Passive Tokens

As the names imply, passive tokens do nothing, and active ones take some action. A
photo or key is an example of a passive token in that the contents of the token never
change. (And, of course, with photos permanence can be a problem, as people change hair
style or color and their faces change over time.)

An active token can have some variability or interaction with its surroundings. For
example, some public transportation systems use cards with a magnetic strip. When you
insert the card into a reader, the machine reads the current balance, subtracts the price of
the trip and rewrites a new balance for the next use. In this case, the token is just a
repository to hold the current value. Another form of active token initiates a two-way
communication with its reader, often by wireless or radio signaling. These tokens lead to
the next distinction among tokens, static and dynamic interaction.

Passive tokens do not change. Active tokens communicate with a sensor.

Static and Dynamic Tokens

The value of a static token remains fixed. Keys, identity cards, passports, credit and

FIC 7) IC HOH
--- page 5 ---
Q2   [20]
CO-3
Write a short note on one-way hash functions. Also, state the properties that a hash
SO-   a.   [10]
function must have.
BL-2
********** 5 **********

[Text in pictures on this page, read by OCR]
other magnetic-stripe cards, and radio transmitter cards (called RFID devices) are
examples of static tokens. Static tokens are most useful for onsite authentication: When a
guard looks at your picture badge, the fact that you possess such a badge and that your
face looks (at least vaguely) like the picture causes the guard to pass your authentication
and allow you access.

We are also interested in remote authentication, that is, in your being able to prove your
identity to a person or computer somewhere else. With the example of the picture badge, it
may not be easy to transmit the image of the badge and the appearance of your face for a
remote computer to compare. Worse, distance increases the possibility of forgery: A local
guard could tell if you were wearing a mask, but a guard might not detect it from a remote
image. Remote authentication is susceptible to the problem of the token having been
forged.

Tokens are vulnerable to an attack called skimming. Skimming is the use of a device to
copy authentication data surreptitiously and relay it to an attacker. Automated teller
machines (ATMs) and point-of-sale credit card readers are particularly vulnerable to
skimming.* At an ATM the thief attaches a small device over the slot into which you insert
your bank card. Because all bank cards conform to a standard format (so you can use your
card at any ATM or merchant), the thief can write a simple piece of software to copy and
retain the information recorded on the magnetic stripe on your bank card. Some skimmers
also have a tiny camera to record your key strokes as you enter your PIN on the keypad.
Either instantaneously (using wireless communication) or later (collecting the physical
device), the thief thus obtains both your account number and its PIN. The thief simply
creates a dummy card with your account number recorded and, using the PIN for
authentication, visits an ATM and withdraws cash from your account or purchases things
with a cloned credit card.

1. Note that this discussion refers to the magnetic-stripe cards popular in the United States. Most other countries
use embedded computer chip cards that are substantially less vulnerable to skimming.

Another form of copying occurs with passwords. If you have to enter or speak your
password, someone else can look over your shoulder or overhear you, and now that
authenticator is easily copied or forged. To overcome copying of physical tokens or
passwords, we can use dynamic tokens. A dynamic token is one whose value changes.
Although there are several different forms, a dynamic authentication token is essentially a
device that generates an unpredictable value that we might call a pass number. Some
devices change numbers at a particular interval, for example, once a minute; others change
numbers when you press a button, and others compute a new number in response to an
input, sometimes called a challenge. In all cases, it does not matter if someone else sees or
hears you provide the pass number, because that one value will be valid for only one
access (yours), and knowing that one value will not allow the outsider to guess or generate
the next pass number.

Dynamic tokens have computing power on the token to change their
internal state.

Dynamic token generators are useful for remote authentication, especially of a person to
a computer. An example of a dynamic token is the SecurID token from RSA Laboratories,

shown in Figure 2-6. To use a SecurID token, you enter the current number displayed on
the token when prompted by the authenticating application. Each token generates a
distinct, virtually unpredictable series of numbers that change every minute, so the
authentication system knows what number to expect from your token at any moment. In
this way, two people can have SecurID tokens, but each token authenticates only its
assigned owner. Entering the number from another token does not pass your
authentication. And because the token generates a new number every minute, entering the
number from a previous authentication fails as well.

Token code: Clock
Changi
60 seconds

synchronized to
UCT
Unique seed
FIGURE 2-6 SecurID Token (Photo courtesy of RSA, the security division of EMS
and copyright © RSA Corporation, all rights reserved.)
We have now examined the three bases of authentication: something you know, are, or

have. Used in an appropriate setting, each can offer reasonable security. In the next
sections we look at some ways of enhancing the basic security from these three forms.
--- page 6 ---
Ans.

One-Way Hasu Funcrion An alternative to the message authentication code is
the one-way hash function. As with the message authentication code, a hash function
accepts a variable-size message M as input and produces a fixed-size message digest
H() as output (see Figure 2.4). Typically, the message is padded out to an integer
multiple of some fixed length (e.g., 1024 bits) and the padding includes the value of
the length of the original message in bits. The length field is a security measure to
increase the difficulty for an attacker to produce an alternative message with the
same hash value.

Unlike the MAC, a hash function does not take a secret key as input. Figure 2.5
illustrates three ways in which the message can be authenticated using a hash
function. The message digest can be encrypted using symmetric encryption

L bits

Message or data block M (variable length) PLL

-

Hash value h
(fixed length)

P, L = padding plus length field

Figure 2.4 Cryptographic Hash Function; h = H(M)

FIC 6 I HF
--- page 7 ---
Source A —<—— Destination B ———>-

2 2 2
ob ob ob
3 3 3
3 Z 3
= = =
(a) Using symmetric encryption

& & &
2 2 *\| =

Compare

Compare
PU,

(b) Using public-key encryption

K K

2 2 2

? ; f — i}
z | 7 |p > z

tf tf tf

2 2 =

K c-4 K Compare

t------- >

|__$§-fy

(c) Using secret value

Figure 2.5 Message Authentication Using a One-Way Hash Function

(see Figure 2.5a); if it is assumed that only the sender and receiver share the encryp-
tion key, then authenticity is assured. The message digest can also be encrypted using
public-key encryption (see Figure 2.5b); this is explained in Section 2.3. The public-
key approach has two advantages: It provides a digital signature as well as message
authentication, and it does not require the distribution of keys to communicating
parties.

FIC 7 IC OHH
--- page 8 ---
These two approaches have an advantage over approaches that encrypt the
entire message, in that less computation is required. But an even more common
approach is the use of a technique that avoids encryption altogether. Several reasons
for this interest are pointed out in [TSUD92]:

e Encryption software is quite slow. Even though the amount of data to be
encrypted per message is small, there may be a steady stream of messages into
and out of a system.

e Encryption hardware costs are nonnegligible. Low-cost chip implementations
of DES and AES are available, but the cost adds up if all nodes in a network
must have this capability.

e Encryption hardware is optimized toward large data sizes. For small blocks of
data, a high proportion of the time is spent in initialization/invocation overhead.

e Anencryption algorithm may be protected by a patent.

Figure 2.5c shows a technique that uses a hash function but no encryption for
message authentication. This technique, known as a keyed hash MAC, assumes that
two communicating parties, say A and B, share a common secret key K. This secret
key is incorporated into the process of generating a hash code. In the approach illus-
trated in Figure 2.5c, when A has a message to send to B, it calculates the hash function
over the concatenation of the secret key and the message: MDy = H(K||M||K).°
It then sends [M || MD,] to B. Because B possesses K, it can recompute H(K || M || K)
and verify MD. Because the secret key itself is not sent, it should not be possible
for an attacker to modify an intercepted message. As long as the secret key remains
secret, it should not be possible for an attacker to generate a false message.

Note the secret key is used as both a prefix and a suffix to the message. If the
secret key is used as either only a prefix or only a suffix, the scheme is less secure.
This topic will be discussed in Chapter 21. Chapter 21 also describes a scheme known
as HMAC, which is somewhat more complex than the approach of Figure 2.5¢ and
which has become the standard approach for a keyed hash MAC.

CO-2

SO- b. Explain the security incident response plan. [10]

BL-2

FIC QF EH 1
--- page 9 ---
Ans.

Incident Response Plans

A (security) incident response plan tells the staff how to deal with a security incident.
In contrast to the business continuity plan, the goal of incident response is handling the
current security incident, without direct regard for the business issues. The security
incident may at the same time be a business catastrophe, as addressed by the business
continuity plan. But as a specific security event, it might be less than catastrophic (that is,
it may not severely interrupt business) but could be a serious breach of security, such as a
hacker attack or a case of internal fraud. An incident could be a single event, a series of
events, or an ongoing problem.

An incident response plan details how to address security incidents of all
types.

An incident response plan should

+ define what constitutes an incident
+ identify who is responsible for taking charge of the situation
+ describe the plan of action

The plan usually has three phases: advance planning, triage, and running the incident. A
fourth phase, review, is useful after the situation abates so that this incident can lead to
improvement for future incidents.

Advance Planning

As with all planning functions, advance planning works best because people can think
logically, unhurried, and without pressure or emotion. What constitutes an incident may be
vague. We cannot know the details of an incident in advance. Typical characteristics
include harm or risk of harm to computer systems, data, processing, or people; initial
uncertainty as to the extent of damage; and similar uncertainty as to the source or method
of the incident. For example, you can see that the file is missing or the home page has
been defaced, but you do not know how or by whom or what other damage there may be.

In organizations that have not done incident planning, chaos may develop at this point.
Someone runs to the network manager. Someone sends email to the help desk. Someone
calls the FBI, the CERT, the newspapers, or the fire department. People start to investigate
on their own, without coordinating with the relevant staff in other departments, agencies,
or businesses. And conversation, rumor, and misinformation ensue: often more noise than
substance.

With an incident response plan in place, everybody is trained in advance to contact the
designated leader. The plan establishes a list of people to alert, in order, in case the first
person is unavailable. The leader decides what to do next, beginning by determining if this
is a real incident or a false alarm. Indeed, natural events sometimes look like incidents,
and the facts of the situation should be established first. If the leader decides this may be a
real incident, he or she invokes the response team.

An incident response plan tells whom to contact in the event of an

FIC QF OH ar
--- page 10 ---
incident, which may be just an unconfirmed, unusual situation.

Responding

The response team is the set of people charged with responding to the incident. The
response team may include

+ director: person in charge of the incident, who decides what actions to take and
when to terminate the response. The director is typically a management
employee.

* technician(s): people who perform the technical part of the response. The lead
technician decides where to focus attention, analyzes situation data, documents
the incident and how it was handled, and calls for other technical people to assist
with the analysis.

+ advisor(s): legal, human resources, or public relations staff members as
appropriate.

In a small incident a single person can handle more than one of these roles.
Nevertheless, a single person should be in charge, someone who directs the response
work, a single point of contact for “insiders” (employees, users), and a single official
representative for “the public.”

To develop policy and identify a response team, you need to consider certain matters.

+ Legal issues: An incident has legal ramifications. In some countries, computer
intrusions are illegal, so law enforcement officials must be involved in the
investigation. In other places, you have discretion in deciding whether to ask
law enforcement to participate. In addition to criminal action, you may be able
to bring a civil case. Both kinds of legal action have serious implications for the
response. For example, evidence must be gathered and maintained in specific
ways in order to be usable in court. Similarly, laws may limit what you can do
against the alleged attacker: Cutting off a connection is probably acceptable, but
launching a retaliatory denial-of-service attack may not be.

+ Preserving evidence: The most common reaction in an incident is to assume
the cause was internal or accidental. For instance, you may first assume that
hardware has failed or software isn’t working correctly. The staff may be
directed to change the configuration, reload the software, reboot the system, or
similarly attempt to resolve the problem by adjusting the software.
Unfortunately, each of these acts can irreparably distort or destroy evidence.
When dealing with a possible incident, do as little as possible before securing
the site and “dusting for fingerprints.”

+ Records: It may be difficult to remember what you have already done: Have
you already reloaded a particular file? What steps got you to the prompt asking
for the new DNS server’s address? If you call in an outside forensic investigator
or the police, you will need to tell exactly what you have already done. A list of
what was done can also help people who need to determine what happened, how
to prevent it in the future, and how to restore data and computing capabilities.

+ Public relations: In handling an incident your organization should speak with

FRR ICR 7 OI HOH
--- page 11 ---
one voice. You risk sending confusing messages if too many people speak. Only
one person should speak publicly if legal action may be taken. An unguarded
comment may tip off the attacker or have a negative effect on the case. You can
simply say that an incident occurred, tell briefly and generally what it was, and
state that the situation is now under control and normal operation will resume (at
a particular time, if a reliable estimate can be given).

Incident responders first perform triage: They investigate what has happened. “The
network is responding slowly” can have many causes, from heavy usage to electronic
malfunction to terrorist attack. Based on first analysis the team decides what steps to take
to address the incident.

“Is this really an incident” is the most important question.

Some incidents resolve themselves (for example, the heavy usage ends), some stay the
same (the malfunction does not heal itself), and some get worse (the attack intensifies).
Incident responders follow the case until they have identified the cause and done as much
as possible to return the system to normal. Then the team finishes documenting its work
and declares the incident over.

After the Incident Is Resolved

Eventually, the incident response team closes the case. At this point the team will hold a
review after the incident to consider two things:

+ Is any security control action to be taken? Did an intruder compromise a
system because security patches were not up to date; if so, should there be a
procedure to ensure that patches are applied when they become available? Was
access obtained because of a poorly chosen password; if so, should there be a
campaign to educate users on how to construct strong passwords? If there were
control failures, what should be done to prevent similar attacks in the future?

+ Did the incident response plan work? Did everyone know whom to notify? Did
the team have needed resources? Was the response fast enough? Were certain
critical resources unnecessarily affected? What should be done differently next
time?

The incident response plan ensures that incidents are handled promptly, efficiently, and
with minimal harm.

Incident Response Teams

Many organizations name and maintain a team of people trained and authorized to
handle a security incident. Such teams, called computer security incident response
teams (CSIRTs) or computer emergency response teams (CERTS) are standard at large
private and government organizations, as well as many smaller ones. A CSIRT can consist
of one person or it can be a flexible team of dozens of people on call for special skills they
can contribute.

The September—October 2014 issue of IEEE Security & Privacy magazine is devoted to
CSIRTs. Papers include a case study of a national CSIRT and its coordination with other

FRI ICR 7 FI OH
--- page 12 ---
CSIRTs, how CSIRTs can (and must) automate the evaluation of millions of data items
received hourly, and a study of CSIRT personnel from a psychological perspective to help
teams be more effective.

Types of CSIRTs

A single person, the computer or network administrator of a small organization, may
constitute the full and permanent incident response team. Responding to a major incident
may overtake other ordinary responsibilities. For this reason, as an organization’s
information technology operation becomes larger or more complex, the nature of its
response capability often changes.

But one person or one in-house response organization is not the full layout of incident
response throughout the world. Although some incidents are confined to one organization,
others involve multiple targets, sometimes across organizational, political, and geographic
boundaries. Here are some models for CSIRTs:

+a full organizational response team to cover all incidents; such a team may
include separate staff to deal with situations in different organizational units,
such as plants in separate locations or distinct business units of a larger company
* coordination centers to coordinate incident response activity across
organizations, so that work is not duplicated unnecessarily and efforts proceed
toward the same goals

* so-called national CSIRTs with coordination responsibility within a country
and to national CSIRTs of other countries

* sector CSIRTs to assist with investigating and handling incidents specific to a
particular business sector, for example, financial institutions or medical
facilities; some attacks focus on one type of target (for example, in 2013 large
banks were the target of massive denial-of-service attacks)

+ vendor CSIRTs to address or participate in incidents involving one
manufacturer’s products

* outsourced CSIRT teams, hired to perform incident response services on
contract to other companies

CSIRTs operate in organizations, nationally, internationally, by vendor,
and by business sector.

A related concept is the security operations center (SOC), which performs the day-to-
day monitoring of a network and may be the first to detect and report an unusual situation.
Also, information sharing and analysis centers (ISACs) perform some CSIRT functions by
sharing threat and incident data across CSIRTs.

CSIRT Activity
Responsibilities of a CSIRT include:

+ Reporting: receiving reports of suspected incidents and reporting as
appropriate to senior management

+ Detection: investigation to determine if an incident occurred

FRR ICR] DA KH
--- page 13 ---
+ Triage: immediate action to address urgent needs

+ Response: coordination of effort to address all aspects in a manner appropriate
to severity and time demands

+ Post-mortem: declaring the incident over and arranging to review the case to
improve future response

+ Education: preventing harm by advising on good security practices and
disseminating lessons learned from past incidents

The proactive role of a CSIRT in preventing attacks is increasing in importance, reports
Robin Ruefle’s team [RUE14]. Teams study current data to predict future attack trends as
a way to determine where to invest preventive resources.

Team Membership

Not uncommonly the incident response team of a large organization has 50 or more
members.

At different times response teams need a variety of skills, including the ability to

+ collect, analyze, and preserve digital forensic evidence

* analyze data to infer trends

* analyze the source, impact, and structure of malicious code

+ help manage installations and networks by developing defenses such as
signatures

+ perform penetration testing and vulnerability analysis

* understand current technologies used in attacks

Specialized skills can be brought into the response team as needed for specific
incidents.

Forming the team in advance lets an organization select people according to their
personal and technical skills, try out different member groupings to determine whether the
mix of people is effective, and let the team members develop camaraderie and trust before
having to work together on an incident. Additionally, at least some incident response team
members will have other jobs in the organization; that is, they do not work full time for the
incident team. With advance notice, managers can plan for other people to take over the
work of the person seconded to the incident response team for the duration of the incident.

Information Sharing

As Robin Ruefle and colleagues [RUE14] report, information sharing is a key
responsibility of CSIRTs. An incident affecting one site may also affect another, and
analysis from one place may help another. To date there are no standards for automated
information sharing between CSIRTs, however. Because of trust issues, much sharing now
takes place informally, by word of mouth, in which one CSIRT member interacts with a
known colleague at another. That model does not scale to larger scale operation, nor does
it support interchange with national and other coordinating CSIRTs. Information sharing is
also stymied because of fears of competition, negative publicity, and regulations.

FIR ICR 7] QI HO
--- page 14 ---
Q3   [20]
CO-2
What is a virus. Explain the various methods through which virus attaches itself to a
SO-   a.   [10]
host program.
BL-2
********** 14 **********

[Text in pictures on this page, read by OCR]
Incident response often requires sharing information—within an
organization, with similarly affected ones, and with national officials.

Determining Incident Scope

The scope of an incident is rarely obvious at the beginning. It may begin with
someone’s noticing something irregular. (See the example in Sidebar 10-3 of how a tiny
irregularity exploded into a major incident.)

Sidebar 10-3 Incorrect Account Balance Leads to Intruder

In 1986 Cliff Stoll was working as an astronomer at Lawrence Berkeley
Laboratory when he noticed the amounts for computer accounts he managed did
not add up properly. Although the mismatch was small, Stoll was unwilling just
to dismiss it as an unfathomable computer error. Someone had created an extra
account being charged against Stoll’s projects, but the monthly bill was not
being delivered to Stoll (or to anyone else, because the account had no billing
address). Coincidentally, Stoll received a report that someone from his site had
been breaking into military computers, but he didn’t initially connect these two
data points.

Stoll removed the unauthorized account but found that the attacker remained,
having acquired system administrator privileges. Thinking the attacker was a
student at a nearby university, Stoll and his colleagues wanted to catch the
attacker in the act. They soon found the flaw the attacker exploited but decided
to keep the culprit engaged so they could investigate his actions, using an
elaborate masquerade in which Stoll controlled everything the attacker could see
and do [STO88, STO89]. Stoll’s trap was one of the first examples of a
honeypot (introduced in Chapter 5).

After months of activity Stoll and authorities identified the attacker as a
German agent named Markus Hess, recruited by the Soviet KGB. German
authorities arrested Hess, who was convicted of espionage and sentenced to one
to three years in prison.

Accounting records that did not balance—off by just $0.75—led to

investigation and conviction of an international spy. When you begin to
investigate an incident, you seldom know what its scope will be.
--- page 15 ---
Ans.

MALICIOUS PROGRAM ERRORS

| Computer Virus can slow down your computer by displaying useless messages.
“

(x) You are Heart Less.
You Wil Be Punished For This

pel

|_| might corrupt your system files.

|_| might make some programs faulty or corrupt.

| might damage your boot sector creating problems when you boot into the windows.

|| might steal important information from your computer and send to some other person.

| might change the power ratings of your computer and could blast the system.
Appended Viruses

A program virus attaches itself to a program; then, whenever the program is run, the
virus is activated. This kind of attachment is usually easy to design and implement.

In the simplest case, a virus inserts a copy of itself into the executable program file
before the first executable instruction. Then, all the virus instructions execute first; after
the last virus instruction, control flows naturally to what used to be the first program
instruction. Such a situation is shown in Figure 3-19.

+ Virus Code = Virus Code

Original
Program

Original
Program

FIGURE 3-19 Virus Attachment

This kind of attachment is simple and usually effective. The virus writer need not know
anything about the program to which the virus will attach, and often the attached program
simply serves as a carrier for the virus. The virus performs its task and then transfers to the
original program. Typically, the user is unaware of the effect of the virus if the original
program still does all that it used to. Most viruses attach in this manner.

Viruses That Surround a Program

An alternative to the attachment is a virus that runs the original program but has control
before and after its execution. For example, a virus writer might want to prevent the virus
from being detected. If the virus is stored on disk, its presence will be given away by its
file name, or its size will affect the amount of space used on the disk. The virus writer
might arrange for the virus to attach itself to the program that constructs the listing of files
on the disk. If the virus regains control after the listing program has generated the listing
but before the listing is displayed or printed, the virus could eliminate its entry from the
listing and falsify space counts so that it appears not to exist. A surrounding virus is shown
in Fi, -20.

FRR IC 7 DA HOH
--- page 16 ---
Physically Logically

oa Virus Code
Virus Code_| o

Original
Program
Original
Program
Virus Code
Part (b)

FIGURE 3-20 Surrounding Virus
Integrated Viruses and Replacements

A third situation occurs when the virus replaces some of its target, integrating itself into
the original code of the target. Such a situation is shown in Figure 3-21. Clearly, the virus
writer has to know the exact structure of the original program to know where to insert
which pieces of the virus.

Original + Virus = Modified
Program Code ia Program

FIGURE 3-21 Virus Insertion

Finally, the malicious code can replace an entire target, either mimicking the effect of
the target or ignoring its expected effect and performing only the virus effect. In this case,

the user may perceive the loss of the original program.

Co-4

SO- b. | Explain DAC access control model in depth. [10]

BL-2

4.3 DISCRETIONARY ACCESS CONTROL

Ass was previously stated, a discretionary access control scheme is one in which an
Ans. entity may be granted access rights that permit the entity, by its own volition, to
enable another entity to access some resource. A general approach to DAC, as exer-
cised by an operating system or a database management system, is that of an access
matrix. The access matrix concept was formulated by Lampson [LAMP69, LAMP71],

FRR ICR 7 6 AC OH
--- page 17 ---
and subsequently refined by Graham and Denning [GRAH72, DENN71] and by
Harrison et al. [HARR76].

One dimension of the matrix consists of identified subjects that may attempt
data access to the resources. Typically, this list will consist of individual users or user
groups, although access could be controlled for terminals, network equipment, hosts,
or applications instead of or in addition to users. The other dimension lists the objects
that may be accessed. At the greatest level of detail, objects may be individual data
fields. More aggregate groupings, such as records, files, or even the entire database,
may also be objects in the matrix. Each entry in the matrix indicates the access rights
of a particular subject for a particular object.

Figure 4.2a, based on a figure in [SAND94], is a simple example of an access
matrix. Thus, user A owns files 1 and 3 and has read and write access rights to those
files. User B has read access rights to file 1, and so on.

In practice, an access matrix is usually sparse and is implemented by decom-
position in one of two ways. The matrix may be decomposed by columns, yielding
access control lists (ACLs) (see Figure 4.2b). For each object, an ACL lists users and
their permitted access rights. The ACL may contain a default, or public, entry. This
allows users that are not explicitly listed as having special rights to have a default set
of rights. The default set of rights should always follow the rule of least privilege or
read-only access, whichever is applicable. Elements of the list may include individual
users as well as groups of users.

When it is desired to determine which subjects have which access rights to a
particular resource, ACLs are convenient, because each ACL provides the informa-
tion for a given resource. However, this data structure is not convenient for determin-
ing the access rights available to a specific user.

Decomposition by rows yields capability tickets (see Figure 4.2c). A capability
ticket specifies authorized objects and operations for a particular user. Each user has a
number of tickets and may be authorized to loan or give them to others. Because tickets
may be dispersed around the system, they present a greater security problem than access
control lists. The integrity of the ticket must be protected, and guaranteed (usually by
the operating system). In particular, the ticket must be unforgeable. One way to accom-
plish this is to have the operating system hold all tickets on behalf of users. These tickets
would have to be held in a region of memory inaccessible to users. Another alternative is
to include an unforgeable token in the capability. This could be a large random password,
or a cryptographic message authentication code. This value is verified by the relevant
resource whenever access is requested. This form of capability ticket is appropriate for
use in a distributed environment, when the security of its contents cannot be guaranteed.

The convenient and inconvenient aspects of capability tickets are the opposite
of those for ACLs. It is easy to determine the set of access rights that a given user
has, but more difficult to determine the list of users with specific access rights for a
specific resource.

[SAND94] proposes a data structure that is not sparse, like the access matrix,
but is more convenient than either ACLs or capability lists (see Table 4.2). An autho-
rization table contains one row for one access right of one subject to one resource.
Sorting or accessing the table by subject is equivalent to a capability list. Sorting or
accessing the table by object is equivalent to an ACL. A relational database can easily
implement an authorization table of this type.

FRR ICR] AC OH
--- page 18 ---
OBJECTS

File | File 2 File3 File 4

User A

SUBJECTS   UserB

User C

(a) Access matrix

“Et a
“Hi “ae
ti

(b) Access control lists for files of part (a)
Figure 4.2. Example of Access Control Structures

File 2

An Access Control Model

This section introduces a general model for DAC developed by Lampson, Graham,
and Denning [LAMP71, GRAH72, DENN71]. The model assumes a set of subjects,
a set of objects, and a set of rules that govern the access of subjects to objects. Let us
define the protection state of a system to be the set of information, at a given point in
time, that specifies the access rights for each subject with respect to each object. We
can identify three requirements: representing the protection state, enforcing access
rights, and allowing subjects to alter the protection state in certain ways. The model
addresses all three requirements, giving a general, logical description of a DAC system.

FOI 7 QF Cr
--- page 19 ---
Table 4.2 Authorization Table for Files in Figure 4.2

Subject Access Mode Object
A Own File 1
A Read File |
A Write File 1
A Own File 3
A Read File 3
A Write File 3
B Read File 1
B Own File 2
B Read File 2
B Write File 2
B Write File 3
B Read File 4
c Read File 1
c Write File 1
c Read File 2
c Own File 4
c Read File 4
c Write File 4

To represent the protection state, we extend the universe of objects in the access
control matrix to include the following:

© Processes: Access rights include the ability to delete a process, stop (block), and
wake up a process.

* Devices: Access rights include the ability to read/write the device, to control its
operation (e.g., a disk seek), and to block/unblock the device for use.

* Memory locations or regions: Access rights include the ability to read/write
certain regions of memory that are protected such that the default is to disal-
low access.

© Subjects: Access rights with respect to a subject have to do with the ability
to grant or delete access rights of that subject to other objects, as explained
subsequently.

Figure 4.3 is an example. For an access control matrix A, each entry A[S, X]
contains strings, called access attributes, that specify the access rights of subject S to
object X. For example, in Figure 4.3, S; may read file F,, because ‘read’ appears in
AS, Fi.

From a logical or functional point of view, a separate access control module
is associated with each type of object (see Figure 4.4). The module evaluates each

FRR ICR 7 QI OR
--- page 20 ---
OBJECTS

Subjects Files Processes Disk drives

S, | control | owner com reads read | wakeup | wakeup | seek | owner
a Soniee) ovase
4
o
5S control writes | execute owner | seeks
=)
a
S; control write stop

+ = copy flag set

Figure 4.3 Extended Access Control Matrix

request by a subject to access an object to determine if the access right exists. An
access attempt triggers the following steps:

1. A subject Sp issues a request of type a for object X.

2. The request causes the system (the operating system or an access control interface
module of some sort) to generate a message of the form (Sp, @, X) to the control-
ler for X.

3. The controller interrogates the access matrix A to determine if a is in A[Sp, X].
If so, the access is allowed; if not, the access is denied and a protection violation
occurs. The violation should trigger a warning and appropriate action.

Figure 4.4 suggests that every access by a subject to an object is mediated by
the controller for that object, and that the controller’s decision is based on the cur-
rent contents of the matrix. In addition, certain subjects have the authority to make
specific changes to the access matrix. A request to modify the access matrix is treated
as an access to the matrix, with the individual entries in the matrix treated as objects.
Such accesses are mediated by an access matrix controller, which controls updates
to the matrix.

The model also includes a set of rules that govern modifications to the access
matrix, as shown in Table 4.3. For this purpose, we introduce the access rights ‘owner’
and ‘control’ and the concept of a copy flag, as explained in the subsequent paragraphs.

The first three rules deal with transferring, granting, and deleting access rights.
Suppose the entry a* exists in A[S), X]. This means Sy has access right a to subject
X and, because of the presence of the copy flag, can transfer this right, with or with-
out copy flag, to another subject. Rule R1 expresses this capability. A subject would
transfer the access right without the copy flag if there were a concern that the new
subject would maliciously transfer the right to another subject that should not have
that access right. For example, 5; may place ‘read’ or ‘read*” in any matrix entry in
the F, column. Rule R2 states that if Sp is designated as the owner of object X, then
So can grant an access right to that object for any other subject. Rule R2 states that

FRI ICR DO) A RH
--- page 21 ---
T T
{+ System intervention ————>}

Subjects ' Access control mechanisms ' Objects

s read F (S,, read, F)

1
wakeup P 1 (S,, wakeup, P)

s, 1
i
1
1 ; 1
H Terminal i
H ‘& device a
! manager !
1 1
' f '
' Instruction 1
' hardware H

s grantatoS,,X | 1(S,, grant, a, S,,X) !

r

1 Y !
delete B from S,,¥ _ 1(5,,, delete, B,S,,¥) | Access H
s. s ( le, By Spy ¥) matrix >
; ' monitor !
1

i |
i i
H Access H

write | matrix [read

Figure 44 An Organization of the Access Control Function

Sq can add any access right to A[S, X] for any S, if Sy has ‘owner’ access to X. Rule R3
permits Sy to delete any access right from any matrix entry in a row for which Sy con-
trols the subject, and for any matrix entry in a column for which Sy owns the object.
Rule R4 permits a subject to read that portion of the matrix that it owns or controls.

The remaining rules in Table 4.3 govern the creation and deletion of subjects
and objects. Rule RS states that any subject can create a new object, which it owns,
and can then grant and delete access to the object. Under Rule R6, the owner of an
object can destroy the object, resulting in the deletion of the corresponding column
of the access matrix. Rule R7 enables any subject to create a new subject; the creator
owns the new subject and the new subject has control access to itself. Rule R8 permits
the owner of a subject to delete the row and column (if there are subject columns)
of the access matrix designated by that subject.

The set of rules in Table 4.3 is an example of the rule set that could be defined
for an access control system. The following are examples of additional or alternative

FI ICR D7 FAC HOH
--- page 22 ---
Table 4.3 Access Control System Commands

Rule Command (by S,) Authorization Operation
en nt a CL woe {nas
m grant {<}rosx tered store {<}inais.n
R3 ‘control’ in A[S), 5]
delete @ from S, X° or delete a from A[S, X]
‘owner’ in A[S, X]
R4 ‘contro!’ in A[S), S]
we read SX or copy A[S, X] into w
‘owner’ in A[Sy, X]
RS create object X None add column for X to A; store
‘owner’ in A[So, X]
R6 destroy object X ‘owner’ in A[Sy, X] delete column for X from A
RT create subject S none add row for S to A; execute
create object S; store
‘control’ in A[S. S]
RS destroy subject S ‘owner’ in A[S), 5] delete row for $ from A;

execute destroy object S

tules that could be included. A transfer-only right could be defined, which results in
the transferred right being added to the target subject and deleted from the transfer-
ring subject. The number of owners of an object or a subject could be limited to one
by not allowing the copy flag to accompany the owner right.

The ability of one subject to create another subject and to have ‘owner’ access
right to that subject can be used to define a hierarchy of subjects. For example, in
Figure 4.3, S; owns S, and S;, so S, and S; are subordinate to S,. By the rules of Table
4.3, S; can grant and delete to S, access rights that S, already has. Thus, a subject can
create another subject with a subset of its own access rights. This might be useful, for
example, if a subject is invoking an application that is not fully trusted and does not
want that application to be able to transfer access rights to other subjects.

Q4 [20]

Co-4

SO- a. | Describe Host-based IDS system in depth. [10]

BL-2

FIR ICR DAC HH
--- page 23 ---
Ans.

8.4 HOST-BASED INTRUSION DETECTION

Host-based IDSs (HIDSs) add a specialized layer of security software to vulnerable
or sensitive systems; such as database servers and administrative systems. The HIDS
monitors activity on the system in a variety of ways to detect suspicious behavior. In
some cases, an IDS can halt an attack before any damage is done, as we will discuss
in Section 9.6, but its main purpose is to detect intrusions, log suspicious events, and
send alerts.

The primary benefit of a HIDS is that it can detect both external and internal
intrusions, something that is not possible either with network-based IDSs or firewalls.
As we discussed in the previous section, host-based IDSs can use either anomaly or
signature and heuristic approaches to detect unauthorized behavior on the monitored
host. We now review some common data sources and sensors used in HIDS, continue
with a discussion of how the anomaly, signature and heuristic approaches are used in
HIDS, then consider distributed HIDS.

Data Sources and Sensors

As noted previously, a fundamental component of intrusion detection is the sensor
that collects data. Some record of ongoing activity by users must be provided as input
to the analysis component of the IDS. Common data sources include:

¢ System call traces: A record of the sequence of systems calls by processes on
a system, is widely acknowledged as the preferred data source for HIDS since
the pioneering work of Forrest [CREE13]. While these work well on Unix and
Linux systems, they are problematic on Windows systems due to the extensive
use of DLLs that obscure which processes use specific system calls.

° Audit (log file) records': Most modern operating systems include account-
ing software that collects information on user activity. The advantage of
using this information is that no additional collection software is needed.

FIR ICR 2 I OH
--- page 24 ---
The disadvantages are that the audit records may not contain the needed infor-
mation or may not contain it in a convenient form, and that intruders may
attempt to manipulate these records to hide their actions.

« File integrity checksums: A common approach to detecting intruder activity
on a system is to periodically scan critical files for changes from the desired
baseline, by comparing a current cryptographic checksums for these files, with
a record of known good values. Disadvantages include the need to generate and
protect the checksums using known good files, and the difficulty monitoring
changing files. Tripwire is a well-known system using this approach.

° Registry access: An approach used on Windows systems is to monitor access
to the registry, given the amount of information and access to it used by pro-
grams on these systems. However, this source is very Windows specific, and has
recorded limited success.

The sensor gathers data from the chosen source, filters the gathered data to
remove any unwanted information and to standardize the information format, and
forwards the result to the IDS analyzer, which may be local or remote.

Anomaly HIDS

The majority of work on anomaly-based HIDS has been done on UNIX and Linux
systems, given the ease of gathering suitable data for this work. While some earlier
work used audit or accounting records, the majority is based on system call traces.
System calls are the means by which programs access core kernel functions, provid-
ing a wide range of interactions with the low-level operating system functions. Hence
they provide detailed information on process activity that can be used to classify it as
normal or anomalous. Table 8.2a lists the system calls used in current Ubuntu Linux
systems as an example. This data is typically gathered using an OS hook, such as the
BSM audit module. Most modern operating systems have highly reliable options for
collecting this type of information.

The system call traces are then analyzed by a suitable decision engine. [CREE13]
notes that the original work by Forrest et al. introduced the Sequence Time-Delay
Embedding (STIDE) algorithm, based on artificial immune system approaches, that
compares observed sequences of system calls with sequences from the training phase
to obtain a mismatch ratio that determines whether the sequence is normal or not.
Later work has used alternatives, such as Hidden Markov Models (HMM), Artificial
Neural Networks (ANN), Support Vector Machines (SVM), or Extreme Learning
Machines (ELM) to make this classification.

[CREE13] notes that these approaches all report providing reasonable intruder
detection rates of 95-99% while having false positive rates of less than 5%, though
on older test datasets. He updates these results using recent contemporary data and
example attacks, with a more extensive feature extraction process from the system
call traces and an ELM decision engine capable of a very high detection rate while
maintaining reasonable false positive rates. This approach should lead to even more
effective production HIDS products in the near future.

Windows systems have traditionally not used anomaly-based HIDS, as the
wide usage of Dynamic Link Libraries (DLLs) as an intermediary between process
requests for operating system functions and the actual system call interface has

FRR IRD AC HOH
--- page 25 ---
hindered the effective use of system call traces to classify process behavior. Some
work was done using either audit log entries, or registry file updates as a data source,
but neither approach was very successful. [CREE13] reports a new approach that
uses traces of key DLL function calls as an alternative data source, with results com-
parable to that found with Linux system call trace HIDS. Table 8.2b lists the key
DLLs and executables monitored. Note that all of the distinct functions within these
DLLs, numbering in their thousands, are monitored, forming the equivalent to the
system call list presented in Table 8.2a. The adoption of this approach should lead
to the development of more effective Windows HIDS, capable of detecting zero-day
attacks, unlike the current generation of signature and heuristic Windows HIDS that
we will discuss later.

While using system call traces provides arguably the richest information source
for a HIDS, it does impose a moderate load on the monitored system to gather and
classify this data. And as we noted earlier, the training phase for many of the decision
engines requires very significant time and computational resources. Hence, others
have trialed approaches based on audit (log) records. However, these both have a
lower detection rate than the system call trace approaches (80% reported), and are
more susceptible to intruder manipulation.

FI ICR AC KH
--- page 26 ---
A further alternative to examining current process behavior is to look for
changes to important files on the monitored host. This uses a cryptographic check-
sum to check for any changes from the known good baseline for the monitored files.
Typically, all program binaries, scripts, and configuration files are monitored, either
on each access, or on a periodic scan of the file system. The tripwire system is a
widely used implementation of this approach, and is available for all major operat-
ing systems including Linux, Mac OS, and Windows. This approach is very sensitive
to changes in the monitored files, as a result of intruder activity or for any other
reason. However, it cannot detect changes made to processes once they are running
on the system. Other difficulties include determining which files to monitor, since a
surprising number of files change in an operational system, having access to a known
good copy of each monitored file to establish the baseline value, and protecting the
database of file signatures.

Signature or Heuristic HIDS

The alternative of signature or heuristic-based HIDS is widely used, particularly as
seen in anti virus (A/V), more correctly viewed as anti malware, products. These are
very commonly used on client systems and increasingly on mobile devices, and also
incorporated into mail and Web application proxies on firewalls and in network-based
IDSs. They use either a database of file signatures, which are patterns of data found
in known malicious software, or heuristic rules that characterize known malicious
behavior.

These products are quite efficient at detecting known malware, however they
are not capable of detecting zero-day attacks that do not correspond to the known
signatures or heuristic rules. They are widely used, particularly on Windows systems,
which continue to be targeted by intruders, as we discussed in Section 6.9.

Distributed HIDS

Traditionally, work on host-based IDSs focused on single-system stand-alone opera-
tion. The typical organization, however, needs to defend a distributed collection of
hosts supported by a LAN or internetwork. Although it is possible to mount a defense
by using stand-alone IDSs on each host, a more effective defense can be achieved by
coordination and cooperation among IDSs across the network.

Porras points out the following major issues in the design of a distributed IDS
[PORR92]:

e A distributed IDS may need to deal with different sensor data formats. In a
heterogeneous environment, different systems may use different sensors and
approaches to gathering data for intrusion detection use.

* One or more nodes in the network will serve as collection and analysis points
for the data from the systems on the network. Thus, either raw sensor data or
summary data must be transmitted across the network. Therefore, there is a
requirement to assure the integrity and confidentiality of these data. Integrity
is required to prevent an intruder from masking his or her activities by alter-
ing the transmitted audit information. Confidentiality is required because the
transmitted audit information could be valuable.

FI ICR 2 6 FAH KK
--- page 27 ---
e Either a centralized or decentralized architecture can be used. With a central-
ized architecture, there is a single central point of collection and analysis of all
sensor data. This eases the task of correlating incoming reports but creates a
potential bottleneck and single point of failure. With a decentralized architec-
ture, there is more than one analysis center, but these must coordinate their
activities and exchange information.

A good example of a distributed IDS is one developed at the University of
California at Davis [HEBE92, SNAP91]; a similar approach has been taken for a
project at Purdue University [SPAF00, BALA98]. Figure 8.2 shows the overall archi-
tecture, which consists of three main components:

1. Host agent module: An audit collection module operating as a background
process on a monitored system. Its purpose is to collect data on security-related
events on the host and transmit these to the central manager. Figure 8.3 shows
details of the agent module architecture.

2. LAN monitor agent module: Operates in the same fashion as a host agent module
except that it analyzes LAN traffic and reports the results to the central manager.

3. Central manager module: Receives reports from LAN monitor and host agents
and processes and correlates these reports to detect intrusion.

The scheme is designed to be independent of any operating system or system
auditing implementation. Figure 8.3 shows the general approach that is taken. The
agent captures each audit record produced by the native audit collection system.
A filter is applied that retains only those records that are of security interest. These
records are then reformatted into a standardized format referred to as the host

LAN monitor

Host Host
Oo im y}— Asn
module
Router
Internet B a a
Central manager
Manager
= module

FR ICR D7 FAC KH
--- page 28 ---
OS audit
information Filter for

OS audit security Reformat
function 4 function
interest
Host audit record (HAR)

Alerts
Logic Analysis Central
module Notable module Qual manager

activity: response

signatures;

noteworthy
sessions

Templates
Modifications

Figure 8.3 Agent Architecture

audit record (HAR). Next, a template-driven logic module analyzes the records for
suspicious activity. At the lowest level, the agent scans for notable events that are
of interest independent of any past events. Examples include failed files, accessing
system files, and changing a file’s access control. At the next higher level, the agent
looks for sequences of events, such as known attack patterns (signatures). Finally,
the agent looks for anomalous behavior of an individual user based on a historical
profile of that user, such as number of programs executed, number of files accessed,
and the like.

When suspicious activity is detected, an alert is sent to the central manager. The
central manager includes an expert system that can draw inferences from received
data. The manager may also query individual systems for copies of HARs to correlate
with those from other agents.

The LAN monitor agent also supplies information to the central manager. The
LAN monitor agent audits host-host connections, services used, and volume of traffic.
It searches for significant events, such as sudden changes in network load, the use of
security-related services, and suspicious network activities.

The architecture depicted in Figures 8.2 and 8.3 is quite general and flexible.
It offers a foundation for a machine-independent approach that can expand from
stand-alone intrusion detection to a system that is able to correlate activity from
a number of sites and networks to detect suspicious activity that would otherwise
remain undetected.

COo-3

SO- b. Write short note on remote user authentication. [10]

BL-2

3.5 REMOTE USER

CATION

The simplest form of user authentication is local authentication, in which a user
attempts to access a system that is locally present, such as a stand-alone office PC
or an ATM machine. The more complex case is that of remote user authentication,
which takes place over the Internet, a network, or a communications link. Remote
user authentication raises additional security threats, such as an eavesdropper being

Ans.

FI ICR 2 QA HH
--- page 29 ---
@Face o©Fingerprint Voice ©OHand @Iris
100%

2 im ~
10%

g
a SSA
E

g

2 1%

1%
0.0001% — 0.001% 0.01% 0.1% 1% 10% 100%
False match rate

Figure 3.12 Actual Biometric Measurement Operating Characteristic
Curves To clarify differences among systems, a log-log scale is used.
Jan Kane. Biometric Product Testing Final Report. National Physics
Laboratory, United Kingdom, March 2001. United Kingdom National
Archives, Open Government Licence v3.0.

able to capture a password, or an adversary replaying an authentication sequence
that has been observed.

To counter threats to remote user authentication, systems generally rely on some
form of challenge-response protocol. In this section, we present the basic elements
of such protocols for each of the types of authenticators discussed in this chapter.

Password Protocol

Figure 3.13a provides a simple example of a challenge-response protocol for authen-
tication via password. Actual protocols are more complex, such as Kerberos, to be
discussed in Chapter 23. In this example, a user first transmits his or her identity to
the remote host. The host generates a random number r, often called a nonce, and
returns this nonce to the user. In addition, the host specifies two functions, h() and
f(), to be used in the response. This transmission from host to user is the challenge.
The user’s response is the quantity f(r’, h(P’)), where r’ = r and P’ is the user’s
password. The function h is a hash function, so the response consists of the hash func-
tion of the user’s password combined with the random number using the function f.

The host stores the hash function of each registered user’s password, depicted
as h(P(U)) for user U. When the response arrives, the host compares the incom-
ing f(r’, h(P’)) to the calculated f(r, h(P(U))). If the quantities match, the user is
authenticated.

This scheme defends against several forms of attack. The host stores not the
password but a hash code of the password. As discussed in Section 3.2, this secures
the password from intruders into the host system. In addition, not even the hash of the
password is transmitted directly, but rather a function in which the password hash is
one of the arguments. Thus, for a suitable function f, the password hash cannot be cap-
tured during transmission. Finally, the use of a random number as one of the arguments

FAR ICR QA HH
--- page 30 ---
Client Client

Host Host
U . U
U,Use ——U--p® U.User —U--’e
r, random number r, random number
(7. h0,f0) AQ, f0, functions (.40,f0) A, f), functions
P Pow
r’, return of r : password to
fe Wry) passcode via token —
if flr’, MP’) = , return of r fr’, KW")
fir, KP(U))) if fr’, KW’) =
yes/no then yes else no fir, KWL)
yes/no then yes else no

(a) Protocol for a password
(b) Protocol for a token

Client Client
Host Host
U , U
U,Usr —Ue-»> U,Use —U-e-»>
random number r, random number
(r, EQ) (), function x, random sequence
inn EO) challenge
B'—> BI biometric 0, function
D' biometric device p+ py pyr Bx BS’)
Fir’, D', BT’) + BStx!
1’, return of r “ ’, return of r E(r’, BS(x'))
EB", P' BP) = E!E(’, BS’) =
(', PB) (r, BS)
if’ =rANDD'=D extract B’
AND BT’ = BTU) from (’, BS'(x'))
then yes else no if’ =r AND x
yesino AND B = BU)
yes/no then yes else no
(c) Protocol for static biometric (d) Protocol for dynamic biometric

Figure 3.13 Basic Challenge-Response Protocols for Remote User Authentication
Source: Based on [OGORO3}.

of f defends against a replay attack, in which an adversary captures the user’s transmis-
sion and attempts to log on to a system by retransmitting the user’s messages.

Token Protocol

Figure 3.13b provides a simple example of a token protocol for authentication. As
before, a user first transmits his or her identity to the remote host. The host returns a

FIR ICR QQ) A HH
--- page 31 ---
random number and the identifiers of functions f() and h() to be used in the response.
At the user end, the token provides a passcode W’. The token either stores a static
passcode or generates a one-time random passcode. For a one-time random pass-
code, the token must be synchronized in some fashion with the host. In either case,
the user activates the passcode by entering a password P’. This password is shared
only between the user and the token and does not involve the remote host. The
token responds to the host with the quantity f(r’, h(W’)). For a static passcode, the
host stores the hashed value h(W(U)); for a dynamic passcode, the host generates a
one-time passcode (synchronized to that generated by the token) and takes its hash.
Authentication then proceeds in the same fashion as for the password protocol.

Static Biometric Protocol

Figure 3.13c is an example of a user authentication protocol using a static biometric.
As before, the user transmits an ID to the host, which responds with a random num-
ber r and, in this case, the identifier for an encryption E(). On the user side is a client
system that controls a biometric device. The system generates a biometric template
BT’ from the user’s biometric B’ and returns the ciphertext E(r', D', BT’), where D'
identifies this particular biometric device. The host decrypts the incoming message to
recover the three transmitted parameters and compares these to locally stored values.
For a match, the host must find r' = r. Also, the matching score between BT" and
the stored template must exceed a predefined threshold. Finally, the host provides
a simple authentication of the biometric capture device by comparing the incoming
device ID to a list of registered devices at the host database.

Dynamic Biometric Protocol

Figure 3.13d is an example of a user authentication protocol using a dynamic biomet-
ric. The principal difference from the case of a stable biometric is that the host pro-
vides a random sequence as well as a random number as a challenge. The sequence
challenge is a sequence of numbers, characters, or words. The human user at the client
end must then vocalize (speaker verification), type (keyboard dynamics verifica-
tion), or write (handwriting verification) the sequence to generate a biometric signal
BS'(x'). The client side encrypts the biometric signal and the random number. At
the host side, the incoming message is decrypted. The incoming random number r’
must be an exact match to the random number that was originally used as a challenge
(r). In addition, the host generates a comparison based on the incoming biometric
signal BS'(x'), the stored template B7(U) for this user and the original signal x. If
the comparison value exceeds a predefined threshold, the user is authenticated.

Q5 [20]
CO-2 Write short note on dealing with disasters on the following.

SO- a. 1. Power loss [10]
BL-2 2. Human Vandals

FR ICR QI OH
--- page 32 ---
Ans.

10.5 Dealing with Disaster

Much of this book has focused on technical issues in security and their technical
solutions: firewalls, encryption techniques, malware scanners, and more. But many threats
to security involve human or natural disasters, events that should also be addressed in the
security plan. For this reason, in this section we consider how to cope with the
nontechnical things that can go wrong. Dealing with nontechnical problems has two
aspects: preventing things that can be prevented and recovering from the things that
cannot be prevented. Physical security is the term used to describe protection needed
outside the computer system. Typical physical security controls include guards, locks, and
fences to deter direct attacks. In addition, there are other kinds of protection against less
direct disasters, such as floods and power outages; these, too, are part of physical security.
As this section shows, many physical security measures can be established simply by good
common sense, a characteristic that Mark Twain noted “is a most uncommon virtue.”

Other Natural Disasters

Computers are subject to wind storms, earthquakes, volcanoes, and similar events.
Although not natural disasters, building collapse, explosion, and damage from falling
objects can be considered in the same category. These kinds of catastrophes are difficult to
predict or value.

But we know these catastrophes will occur. Security managers cope with them in
several ways:

+ developing contingency plans so that people know how to react in emergencies
and business can continue

+ insuring physical assets—computers, buildings, devices, supplies—against
harm

* preserving sensitive data by maintaining copies in physically separated
locations

Power Loss

Computers need their food—electricity—and they require a constant, pure supply of it.
With a direct power loss, all computation ceases immediately. Because of possible damage
to media by sudden loss of power, many disk drives monitor the power level and quickly
retract the recording head if power fails. For certain time-critical applications, loss of
service from the system is intolerable; in these cases, alternative complete power supplies
must be instantly available.

Uninterruptible Power Supply

One protection against power loss is an uninterruptible power supply. This device stores
energy during normal operation so that it can return the backup energy if power fails. One
form of uninterruptible power supply uses batteries that are continually charged when the
power is on but which then provide power when electricity fails. However, size, heat,
flammability, and low output can be problems with batteries.

Some uninterruptible power supplies use massive wheels that are kept in continuous
motion when electricity is available. When the power fails, the inertia in the wheels
operates generators to produce more power. Size and limited duration of energy output are
problems with this variety of power supply. Both forms of power supplies are intended to
provide power for a limited time, just long enough to allow the current state of the

FIR ICR QD I HH
--- page 33 ---
computation to be saved so that no computation is lost.
Surge Suppressor

Another problem with power is its “cleanness.” Although most people are unaware of it,
a variation of 10 percent from the stated voltage of a line is considered acceptable, and
some power lines vary even more. A particular power line may consistently be up to 10
percent high or low.

In many places, lights dim momentarily when a large appliance, such as an air
conditioner, begins operation. When a large motor starts, it draws an exceptionally large
amount of current, which reduces the flow to other devices on the line. When a motor
stops, the sudden termination of draw can send a temporary surge along the line. Similarly,
lightning strikes may send a momentary large pulse. Thus, instead of being constant, the
power delivered along any electric line shows many brief fluctuations, called drops,
spikes, and surges. A drop is a momentary reduction in voltage, and a spike or surge is a
rise. For computing equipment, a drop is less serious than a surge. Most electrical
equipment is tolerant of rather large fluctuations of current.

These variations can be destructive to sensitive electronic equipment, however. Simple
devices called “surge suppressors” filter spikes from an electric line, blocking fluctuations
that would affect computers. These devices cost from $20 to $100; they should be
installed on every computer, printer, or other connected component. More sensitive
models are typically used on larger systems.

As mentioned previously, a lightning strike can send a surge through a power line. To
increase protection, personal computer users usually unplug their machines when they are
not in use, as well as during electrical storms. Another possible source of destruction is
lightning striking a telephone line. Because the power surge can travel along the phone
line and into the computer or peripherals, the phone line should be disconnected from the
modem during storms. These simple measures may save much work as well as valuable
equipment.

Human Vandals

Because computers and their media are sensitive to a variety of disruptions, a vandal
can destroy hardware, software, and data. Human attackers may be disgruntled employees,
bored operators, saboteurs, people seeking excitement, or unwitting bumblers. If physical
access is easy to obtain, crude attacks using axes or bricks can be very effective. One man
recently shot a computer that he claimed had been in the shop for repairs many times
without success.

Physical attacks by unskilled vandals are often easy to prevent; a guard can stop
someone approaching a computer installation with a threatening or dangerous object.
When physical access is difficult, more subtle attacks can be tried, resulting in quite
serious damage. People with modest technical knowledge of a system can short-circuit a
computer with a car key or disable a disk drive with a paper clip. These items are not
likely to attract attention until the attack is completed.

Unauthorized Access and Use

Films and newspaper reports exaggerate the ease of gaining access to a computing

FR ICR QQ I OH
--- page 34 ---
system. Still, as distributed computing systems become more prevalent, protecting the
system from outside access becomes more difficult and more important. Interception is a
form of unauthorized access; the attacker intercepts data and either breaks confidentiality
or prevents the data from being read or used by others. In this context, interception is a
passive attack. But we must also be concerned about active interception, in the sense that
the attacker can change or insert data before allowing it to continue to its destination.

Theft

Stealing a large mainframe computer or a rack of servers is challenging. Not only is
carrying it away difficult, but finding a willing buyer and arranging installation and
maintenance also require special assistance. However, printed reports and removable data
devices can be carried easily. If the theft is done well, the loss may not be detected for
some time.

Personal computers, laptops, smartphones, and personal digital assistants (PDAs, such
as tablets or Blackberries) are designed to be small and portable. Flash drives or memory
sticks are easily carried in a pocket or briefcase. Computers and media that are easy to
carry are also easy to conceal.

We can take one of three approaches to preventing theft: preventing access, preventing
portability, or detecting exit.

Preventing Access

The surest way to prevent theft is to keep the thief away from the equipment. However,
thieves can be either insiders or outsiders. Therefore, access control devices are needed
both to prevent access by unauthorized individuals and to record access by those
authorized. A record of accesses can help identify who committed a theft.

The oldest access control is a guard, not in the firewall sense we discussed in Chapter 6
but in the sense of a human being stationed at the door to control access to a room or to
equipment. Guards offer traditional protection; their role is well understood, and the
protection they offer is adequate in many situations. However, guards must be on duty
continuously in order to be effective; permitting breaks implies at least four guards for a
24-hour operation, with extras for vacation and illness. A guard must personally recognize
someone or recognize an access token, such as a badge. People can lose or forget badges;
terminated employees and forged badges are also problems. Unless the guards make a
record of everyone who has entered a facility, the security staff cannot know who
(employee or visitor) has had access before a problem is discovered.

The second oldest access control is a lock. This device is even easier, cheaper, and
simpler to manage than a guard. However, it too generates no record of who has had
access, and difficulties arise when keys are lost or duplicated. At computer facilities, you
cannot fumble for a key when your hands are filled with devices that might be ruined if
dropped. A site also cannot ignore piggybacking: a person who walks through the door
that someone else has just unlocked. Still, guards and locks afford simple, effective
security for access to facilities such as computer rooms. In many situations, simple is
better.

More exotic access control devices employ cards with radio transmitters, magnetic

FIR ICR I HOH
--- page 35 ---
stripe cards (similar to bank cards), and smart cards with chips containing electronic
circuitry that makes them difficult to duplicate. Because each of these devices interfaces
with a computer, the computer can capture identity information, generating a list of who
entered and left the facility, when, and by which routes. Some of these devices operate by
proximity, so that a person can carry the device in a pocket or clipped to a collar; the
person obtains easy access even when both hands are full. Because these devices are
computer controlled, the system administrators can readily invalidate an access authority
when someone quits or reports the access token lost or stolen.

The nature of the application or service determines how strict the access control needs
to be. Working in concert with computer-based authentication techniques, the access
controls can be part of defense in depth—using multiple mechanisms to provide security.

Preventing Portability

Portability is a mixed blessing. We can now carry around in our pockets devices that
provide as much computing power as mainframes did twenty years ago. Portability is in
fact a necessity in devices such as tablets and mobile phones. And we do not want to
permanently affix our personal computers to our desks, in case they need to be removed
for repair or replacement. Thus, we need to find ways to enable portability without
promoting theft.

One antitheft device is a pad connected to cable, similar to those used to secure
bicycles. The pad is glued to the desktop with extremely strong adhesive. The cables loop
around the equipment and are locked in place. Releasing the lock permits the equipment to
be moved. An alternative is to couple the base of the equipment to a secure pad, in much
the same way that televisions are locked in place in hotel rooms. Yet a third possibility is a
large, lockable cabinet in which the personal computer and its peripherals are kept when
they are not in use. Some people argue that cables, pads, and cabinets are unsightly and,
worse, they make the equipment inconvenient to use. And they are incompatible with
portable devices such as tablets and laptops.

Another alternative is to use movement-activated alarm devices when the equipment is
not in use. Small alarms are available that can be locked to a laptop or case. When
movement is detected, a loud, annoying whine or whistle warns that the equipment has
been disturbed. Such an alarm is especially useful when laptops must be left in meeting or
presentation rooms overnight or during a break. In Sidebar 10-8 we describe the
magnitude of the problem of lost and stolen laptops. Used in concert with guards, the
alarms can offer reasonable protection at reasonable cost.

Sidebar 10-8 Laptops Fly Away at Airports
Ponemon Institute conducted a survey of laptop loss at airports in the United
States and Europe [PON08]. At 36 of the largest U.S. airports they found an
average of 286 laptops are lost, misplaced, or stolen per week. For eight large
European airports, the figure is even larger: 474. Of these, 33 percent were
recovered either before or after the flight in the United States and 43 percent in
Europe.

Travelers reported feeling rushed at the airport (70 percent), carrying too

many items (69 percent), and worrying about flight delays (60 percent) as
contributing factors to the loss of a computer. Among those losing computers,
53 percent (United States) and 49 percent (Europe) said the lost devices
contained sensitive data, and 42 percent of both samples indicated the data were
not backed up. Worse, 65 percent (United States) and 55 percent (Europe) had
not taken steps to protect the sensitive data on the laptops.

Among Ponemon’s recommendations for computer users was to think twice
about information carried on a computer: Business travelers should consider
whether it is really necessary to have so much data with them.

Detecting Theft

For some devices, protection is more important than detection. We want to keep
someone from stealing certain systems or information at all costs. But for other devices, it
may be enough to detect that an attempt has been made to access or steal hardware or
software. For example, chaining down a disk makes it unusable. Instead, we try to detect
when someone tries to leave a protected area with the disk or other protected object. In
these cases, the protection mechanism should be small and unobtrusive.

One such mechanism is similar to the protection used by many libraries, bookstores, or
department stores. Each sensitive object is marked with a special label. Although the label
looks like a normal pressure-sensitive one, its presence can be detected by a machine at
the exit door if the label has not been disabled by an authorized party, such as a librarian
or sales clerk. Similar security code tags are available for vehicles, people, machinery, and
documents. Some tags are enabled by radio transmitters. When the detector sounds an
alarm, someone must apprehend the person trying to leave with the marked object.

CO-3

b. Explain the working of AES in depth with the help of block diagrams. [10]

--- page 36 ---
BL-2

20.3 ADVANCED ENCRYPTION STANDARD

The Advanced Encryption Standard (AES) was issued as a federal information pro-
cessing standard (FIPS 197). It is intended to replace DES and triple DES with an
algorithm that is more secure and efficient.

Overview of the Algorithm

AES uses a block length of 128 bits and a key length that can be 128, 192, or 256 bits.
In the description of this section, we assume a key length of 128 bits, which is likely
to be the one most commonly implemented.

Figure 20.3 shows the overall structure of AES. The input to the encryption
and decryption algorithms is a single 128-bit block. In FIPS PUB 197, this block is
depicted as a square matrix of bytes. This block is copied into the State array, which
is modified at cach stage of encryption or decryption. After the final stage, State is
copied to an output matrix. Similarly, the 128-bit key is depicted as a square matrix
of bytes. This key is then expanded into an array of key schedule words; each word
is 4 bytes and the total key schedule is 44 words for the 128-bit key. The ordering
of bytes within a matrix is by column. So, for example, the first 4 bytes of a 128-bit
plaintext inpul to the encryption cipher occupy the first column of the im matrix,
the second 4 bytes occupy the second column, and so on. Similarly, the first 4 bytes
of the expanded key, which form a word, occupy the first column of the w matrix.

The following comments give some insight into AES:

Ans.

1. One noteworthy feature of this structure is that it is not a Feistel structure.
Recall that in the classic Feistel structure, half of the data block is used to
modify the other half of the data block, and then the halves are swapped. AES
does not use a Feistel structure but processes the entire data block in parallel
during cach round using substitutions and permutation.

2. The key that is provided as input is expanded into an array of forty-four 32-bit
words, w[i]. Four distinct words (128 bits) serve as a round key for each round.

3. Four different stages are used, one of permutation and three of substitution:

* Substitute Bytes: Uses a table, referred to as an S-box, to perform a byte-
by-byte substitution of the block

* Shift Rows: A simple permutation that is performed row by row

FR ICR RG IC HH
--- page 37 ---
Plaintext Key Plaintext
Add round key aw[0, 3] Add round key
=
| Substitute bytes | | Expand key | | Inverse sub bytes | =
= Inverse shift rows
B sees seep ee eeee------}----- ee j
2 J
w[4. 7] Add round key =
?

Inverse sub bytes g
Inverse shift rows

a Shift rows

|
a
é J
Add rownd key w[36, 39]
-
S z

i Shift rows | Inverse shift rows E

Add rownd key w[40, 43] Add round key
Ciphertext Ciphertext
(a) Encryption (b) Decryption

Figure 20.3 AES Encryption and Decryption

* Mix Columns: A substitution that alters each byte in a column as a function
of all of the bytes in the column

« Add Round key: A simple bitwise XOR of the current block with a portion
of the expanded key

4, The structure is quite simple. For both encryption and decryption, the cipher
begins with an Add Round Key stage, followed by nine rounds that each
includes all four stages, followed by a tenth round of three stages. Figure 20.4
depicts the structure of a full encryption round.

FR ICR QA OH
--- page 38 ---
‘State [

— bbddddd

oe

woe Yetmetef tae
. etoile ta el ta


Figure 20.4 AES Encryption Round

§. Only the Add Round Key stage makes use of the key. For this reason, the
cipher begins and ends with an Add Round Key stage. Any other stage,
applied at the beginning or end, is reversible without knowledge of the key
and so would add no security.

6. The Add Round Key stage by itself would not be formidable. The other three
stages together scramble the bits, but by themselves would provide no security
because they do not use the key. We can view the cipher as alternating opera-
tions of XOR encryption (Add Round Key) of a block, followed by scram-
bling of the block (the other three stages), followed by XOR encryption, and
so on. This scheme is both efficient and highly secure.

7. Each stage is easily reversible. For the Substitute Byte, Shift Row, and Mix
Columns stages, an inverse function is used in the decryption algorithm. For
the Add Round Key stage, the inverse is achieved by XORing the same round
key to the block, using the result that AS A @B = B.

8. As with most block ciphers, the decryption algorithm makes use of the
expanded key in reverse order. However, the decryption algorithm is not
identical to the encryption algorithm. This is a consequence of the particular
structure of AES.

FIR ICR QA HH
--- page 39 ---
9, Once it is established that all four stages are reversible, it is easy lo verily
that decryption does recover the plaintext. Figure 20.3 lays out encryption
and deeryplion going in opposite vertical directions. At each horizontal point
(e.g., the dashed line in the figure), State is the same for both encryption and
decryption.

10. The final round of both encryption and decryption consists of only three
stages. Again, this is a consequence of the particular structure of AES and is
required to make the cipher reversible.

Algorithm Details

We now look briefly at the principal elements of AES in more detail.

Sussrircere Byres TRANSFORMATION ‘The forward substitute byte transformation,
called SubBytes, is a simple table lookup. AES defines a 16-16 matrix of byte values,
called an S-box (Table 20.2a), that contains a permutation of all possible 256 8-bit
values. Each individual byte of State is mapped into a new byte in the following
way: The leftmost 4 bits of the byte are used as a row value and the rightmost 4
bits are used as a column value. These row and column values serve as indexes
into the $-box to select a unique 8-bil output value. For example, the hexadecimal
value" {95} references row 9, column 5 of the S-box, which contains the value {2A}.
Accordingly, the value {95} is mapped into the value {2A}.

Here is an example of the SubBytes transformation:

The 8-box is constructed using properties of finite fields. The topic of finite
fields is beyond the scope of this book; it is discussed in detail in [STAL11b].

EA ao 65 a5 87 F2 4D o7
a3 45 5D Bo EC 6E 4c 90
5c 33 o8 BO 4a “3 4h ET

The inverse substitute byte transformation, called InvSubBytes, makes use of
the inverse $-box shown in Table 20.2b. Note, for example, that the input {2A} pro-
duces the output {95}, and the input {95} to the S-box produces {2.4}.

The S8-box is designed to be resistant to known cryptanalytic attacks.
Specifically, the AES developers sought a design that has a low correlation between
input bits and output bits and the property that the output cannot be described as a
simple mathematical function of the input.

Surry Row TraysrorMaTion For the forward shift row transformation, called
ShiftRows, the first row of State is not altered. For the second row, a 1-byte circular
left shift is performed. For the third row, a 2-byte circular left shift is performed.

FIR ICR QQ FAR RH
--- page 40 ---
Fable 20.2

AES §-Boxes

(a) S-box
y


a 63) 7C | 77 | 7B | F2) 6B | 6F | C5 | 30 |] OL | 47 | 2B | FE} D7 | AB] 76
1 | CA] 82] CO | 7D] FA] 59 | 47 |] FO |} AD] D4 |] A2] AF} 9C ] Ad] 72 | CO
2 | BF | FD] % | 26 | 36 |] 3F | Fr] CC] 34 | AS] ES | Fl | 71 | DB] 31 | 15
3 O4 | cr] 23 | C3] 18 | % | 05 | OA] OF | 12 | 80 | E2 | BBY] 27 | B2] 75
4 oo |] 83 | 2C | 1A |] 1B | GE | SA] AD] 52 | 3B | D6 |] BS |} 29 | E3 | 2F | &4
5 53 | D1 | oo | ED] 20 | Fc | BI | 5B |] 6A |] CB] BE] 39 | 44] 4C | 58 | CF
6 | DO] EP} AA] FRY] 43 | 4D | 33 | 85 | 45 | FO | 02 | TF | S50 | 3C |) OF | AB
Xx 7 51 | AS] 40 | SF | 92 | 9D | 38 | F5 | BC] Be | DA! 21 | 10 | FF | F3 | D2
& | cD] 0c} 13 | EC] SF] 97 | 44] 17 | C4] AT] FE | 3D] 64 | SD] 19 | 73
a 6) | 81 | 4F | DC] 22) 2A] OF | 88 | 46 | EE] BS] 14 | DE] SE | 0B | DB
A | EO] 32] 3A] 0A 7 49 | 06 | 24 | 5C ] C2 | DS] AC! G2 | 91 | 95 | Ea] 7
B | EF | C8] 37 | 6D] 8D | DS | 4E] AD] oC | 56 | F4 | BAY] 65 | 7A | AB] OB
C | BA] 78 | 25 | 2B] 1c |] As | Ba] Ch | EX | DD] 74 | 1F | 4B | BD | 8B | SA
D | 7 | 3E ] BS | ob | 48 |] 03 | Fo | OE | @l | 35 | 57 |) BY | SH ] Cl | 1D | YE
E | El] Fe |] 98 | 11 |] 69 | DY] SE] 94 | 9B | 1E | 87 | BY | CE] 55 | 28 | DF
PF ac ] Al ao) | 0D | BF | Ea | 42 68 41 99 72D) OF | BO | 54 | BB] 16

(b) Inverse S-box
¥

a 52] 09 | 6A | DS | 30 | 36 | AS | 38 | BF | 40 | AS | YE | 81 | FS | DT | FB
1 7C | E3 | 39 | &2 | 9B | 2F | FF} 87 | 34 | BE | 43 | 44 | C4 | DE! EO | CB
2 54] 7B | 4 | 32 | Ab |] C2] 23 | 3D] EE | 4C |] 95 | OB | 42 | FA | C3 | 4E
3 O8 | 3B |) Al | 66 | 28 |] D9) 34] B2] Je | SB] AZ] 49 | 6D] 8B |] D1] 35
4 72 | FS | Fo | 64 | 86 |] 68 | OF | 16 | D4] Ad] SC |] CC] SD] 65 | BA | 9
5 | 6c | 70] 48 | 50 | FD | ED} BY] DA] SE] 15 | 46 | 57 | AT] 8D | OD |
if o | DS | AB] OO | BC] BC} D3] OA] F? | E4 |] 58 | 05 | BR] B3 | 45 | 06
Xx 7 | DO] 2C | 1E | 8F CA] 3F | OF | 02 | Cl | AF] BD] 03 | O1 | 13 | SA | OB
8 | 3A 7 91 di | 41 | 4F | 67 | DC] EA] 97 | F2 | CF] CE | Fo | B4 | Eo | 735
a 9h | AC] 74 | 22 | ET |] AD] 35 | 85 | E2 | FO | 37 | Es | 1c | 75 | DF] 6E
A | 47 |] FL] 1A] 71 | ID] 29 | C5 | 89 | GF | BF ] 62 | OE | AAT 18 | BE | 1B
B | FC |] 56 | 3E | 4B] Ch |] D2] 79 | 20 | 9A | DB] CO] FE | 78 | CD] 5A | FA
C | IF | DD] As} 33 7 88 ] oF | C7] 31] Bl | 12 | 10 |] 59 | 27 | BO | Be} AP
D | 6 | 51 |] 7F | AQ] 19 | BS | 4A] 0D | 2D | ES | 7A} OF | 93 | Co] OC | EF
E | Ad | Eo | 3B | 4D] AE] 2A] F5 ] BO | CR | EB] BB] 3C | 83 | 53] | al
F 17 | 2B | 4 | 7E | BA] 77 | De | 26 | El} 69 | 14 | 63 | 55 | 21 | oc | 7D

FRR ICR 71) AH OH
--- page 41 ---
For the third row, a 3-byte circular left shift is performed. The following is an
example of ShiftRows:

aT F2 4D oT cr Fi 4D a7
Ec 6E 4c 90 6E 4c 90 EC
4A C3 4 Er 46 E7 4A c3

The inverse shift row transformation, called InvShiltRows, performs the cir-
cular shifts in the opposite direction for each of the last three rows, with a 1-byte
circular right shift for the second row, and so on.

The shift row transformation is more substantial than it may first appear. This
is because the State, as well as the cipher input and outpul, is treated as an array of
four 4-byte columns. Thus, on encryption, the first 4 bytes of the plaintext are cop-
ied to the first column of State, and so on. Further, as will be seen, the round key is
applied to State column by column. Thus, a row shift moves an individual byte from
one column to another, which is a linear distance of a multiple of 4 bytes. Also note
that the transformation ensures that the 4 bytes of one column are spread out to
four different columns.

Mix Cotuwn Transrorwarion The forward mix column transformation,
called MixColumns, operates on cach column individually. Each byte of a column
is mapped into a new value that is a function of all 4 bytes in the column. The
mapping makes use of equations over finite fields. The following is an example of
MixColumns:

a7 F2 4D 7 47 40 AG 4c
6E 4c 0 EC a7 D4 70 oF
46 ET 4A c3 04 E4 3A 42

The mapping is designed to provide a good mixing among the bytes of each
column. The mix column transformation combined with the shift row transforma-
tion ensures that after a few rounds, all output bits depend on all input bits.

App Rounp Key TRANSFORMATION In the forward add round key
transformation, called AddRoundKey, the 128 bits of State are bitwise NORed
with the 128 bits of the round key. The operation is viewed as a column-wise
operation between the four bytes of a State column and one word of the round
key: it can also be viewed as a byte-level operation. The following is an example
of AddRoundKey:

FIR IC 77 FIC HOH
--- page 42 ---
a 40 Ag 4c AC 19 28 57 EB 39 5B 1B

0 Da 70) oF @ 77 FA DI 5c 40) 2E Al 3
eel E4 3A a2 66 DC 29 OO F2 ci] 13 42

The first matrix is State, and the second matrix is the round key.

The inverse add round key transformation is identical to the forward add
round key transformation, because the NOR operation is its own inverse.

The add round key transformation is as simple as possible and affects every
bit of State. The complexity of the round key expansion, plus the complexity of the
other stages of AES, ensure security.

AES Key Expansion The AES key expansion algorithm takes as input a 4-word
(16-byte) Key and produces a linear array of 44 words (156 bytes). This is sufficient
to provide a 4-word round key for the initial Add Round Key stage and each of the
10 rounds of the cipher.

The key is copied into the first four words of the expanded key. The remainder
of the expanded key is filled in four words at a time. Each added word w{i] depends on
the immediately preceding word, w[i— 1], and the word four positions back, w[i-4]. A
complex finite-field algorithm is used in generating the expanded key.

Q6 [20]
Co-1

SO- a. List and briefly define categories of passive and active security attacks. [10]
BL-1

ComMMUNICATION LINES AND NETWORKS Network security attacks can be classified
as passive attacks and active attacks. A passive attack attempts to learn or make
use of information from the system but does not affect system resources. An active
attack attempts to alter system resources or affect their operation.

Passive attacks are in the nature of cavesdropping on, or monitoring of,

transmissions. The goal of the attacker is to obtain information that is being trans-
mitted. Two types of passive attacks are release of message contents and traffic
analysis.
The release of message contents is easily understood. A telephone conver-
sation, an electronic mail message, and a transferred file may contain sensitive or
confidential information. We would like to prevent an opponent [rom learning the
contents of these transmissions.

A second type of passive attack, traffic analysis, is subtler. Suppose that we
had a way of masking the contents of messages or other information traffic so that
opponents, even if they captured the message, could not extract the information
from the message. The common technique for masking contents is encryption. If we
had eneryplion protection in place, an opponent might still be able to observe the
pattern of these messages. The opponent could determine the location and identity
of communicating hosts and could observe the frequency and length of messages
being exchanged. This information might be useful in guessing the nature of the
communication that was taking place.

Passive attacks are very difficult to detect because they do not involve any
alteration of the data. Typically, the message traffic is sent and received in an
apparently normal fashion and neither the sender nor receiver is aware that a
third party has read the messages or observed the traffic pattern. However, il is
feasible to prevent the success of these attacks, usually by means of encryption.
Thus, the emphasis in dealing with passive attacks is on prevention rather than
detection.

Ans.

FIR ICR 7 AC HOEK
--- page 43 ---
CO-4
What are firewalls. List the various types of firewalls and explain packet filtering and
SO-   b.   [10]
stateful firewalls in depth.
BL-2
Ans.
********** 43 **********

[Text in pictures on this page, read by OCR]
Active attacks involve some modification of the data stream or the creation
of a false stream and can be subdivided into four categories: replay, masquerade,
modification of messages, and denial of service.

Replay involves the passive capture of a data unit and its subsequent retrans-
mission to produce an unauthorized effect.

A masquerade takes place when one entity pretends to be a different entity. A
masquerade attack usually includes one of the other forms of active attack. For exam-
ple, authentication sequences can be captured and replayed after a valid authentica-
tion sequence has taken place, thus enabling an authorized entity with few privileges
to obtain extra privileges by impersonating an entity that has those privileges.

Modification of messages simply means that some portion of a legitimate
message is altered, or that messages are delayed or reordered, to produce an
unauthorized effect. For example, a message stating, “Allow John Smith to read
confidential file accounts” is modified to say, “Allow Fred Brown to read confiden-
tial file accounts.”

The denial of service prevents or inhibits the normal use or management of
communications facilities. This attack may have a specific target; for example, an
entity may suppress all messages directed to a particular destination (e.g., the security
audit service). Another form of service denial is the disruption of an entire network,
either by disabling the network or by overloading it with messages so as to degrade
performance.

Active allacks present the opposite characteristics of passive attacks. Whereas
passive attacks are difficult to detect, measures are available to prevent their
success. On the other hand, it is quite difficult to prevent active attacks absolutely,
because to do so would require physical protection of all communications facilities
and paths at all times. Instead, the goal is to detect them and to recover from any
disruption or delays caused by them. Because the detection has a deterrent effect, it
may also contribute to preve
--- page 44 ---
9.3 TYPES OF FIREWALLS

A firewall can monitor network traffic at a number of levels, from low-level network
packets, either individually or as part of a flow, to all traffic within a transport con-
nection, up to inspecting details of application protocols. The choice of which level
is appropriate is determined by the desired firewall access policy. It can operate as a
positive filter, allowing to pass only packets that meet specific criteria, or as a negative

Internal (protected) network . External (untrusted) network
. Firewall
(e.g., enterprise network) (e.g., Internet)

(a) General model

End-to-end — End-to-end End-to-end — End-to-end
transport Application transport transport Application transport
connection connection connection connection

| | Transport Transport
Internet Internet
Network Network
access access
<=
Physical Physical
(b) Packet filtering firewall (c) Stateful inspection firewall
Application proxy Circuit-level proxy
Internal — — External Internal _ _ External
transport | |Application/<">/Application} | transport transport | |Application| Application} | transport
connection connection connection connection
t ‘Transport Tr Transport
Internet Internet Internet Internet
Network Network Network Network
access access access access
Physical Physical Physical Physical
(d) Application proxy firewall (c) Circuit-level proxy firewall

Figure 9.1 Types of Firewalls

FIR ICR 7) I ROK HH
--- page 45 ---
filter, rejecting any packet that meets certain criteria. The criteria implement the
access policy for the firewall that we discussed in the previous section. Depending
on the type of firewall, it may examine one or more protocol headers in each packet,
the payload of each packet, or the pattern generated by a sequence of packets. In this
section, we look at the principal types of firewalls.

Packet Filtering Firewall

A packet filtering firewall applies a set of rules to each incoming and outgoing
IP packet and then forward or discards the packet (see Figure 9.1b). The firewall is
typically configured to filter packets going in both directions (from and to the internal
network). Filtering rules are based on information contained in a network packet:

¢ Source IP address: The IP address of the system that originated the IP packet
(e.g., 192.178.1.1).

° Destination IP address: The IP address of the system the IP packet is trying to
reach (e.g., 192.168.1.2).

e Source and destination transport-level address: The transport-level (e.g., TCP
or UDP) port number, which defines applications such as SNMP or HTTP.

IP protocol field: Defines the transport protocol.

¢ Interface: For a firewall with three or more ports, which interface of the fire-
wall the packet came from or for which interface of the firewall the packet is
destined.

The packet filter is typically set up as a list of rules based on matches to fields
in the IP or TCP header. If there is a match to one of the rules, that rule is invoked to
determine whether to forward or discard the packet. If there is no match to any rule,
then a default action is taken. Two default policies are possible:

¢ Default = discard: That which is not expressly permitted is prohibited.
© Default = forward: That which is not expressly prohibited is permitted.

The default discard policy is more conservative. Initially, everything is
blocked, and services must be added on a case-by-case basis. This policy is more
visible to users, who are more likely to see the firewall as a hindrance. However,
this is the policy likely to be preferred by businesses and government organizations.
Further, visibility to users diminishes as rules are created. The default forward
policy increases ease of use for end users but provides reduced security; the secu-
rity administrator must, in essence, react to each new security threat as it becomes
known. This policy may be used by generally more open organizations, such as
universities.

Table 9.1 is a simplified example of a rule set for SMTP traffic. The goal is to
allow inbound and outbound e-mail traffic but to block all other traffic. The rules are
applied top to bottom to each packet. The intent of each rule is:

1. Inbound mail from an external source is allowed (port 25 is for SMTP incoming).
2. This rule is intended to allow a response to an inbound SMTP connection.
3. Outbound mail to an external source is allowed.

FRAC 7D AC HOH
--- page 46 ---
Table 9.1 Packet-Filtering Examples

Rule | Direction | Sre address Dest addresss Protocol Dest port Action
1 In External Internal TCP 25 Permit
2 Out Internal External TCP >1023 Permit
a Out Internal External TCP 25 Permit
4 In External Internal TCP >1023 Permit
5 Either Any Any Any Any Deny

4, This rule is intended to allow a response to an outbound SMTP connection.

5. This is an explicit statement of the default policy. All rule sets include this rule
implicitly as the last rule.

There are several problems with this rule set. Rule 4 allows external traffic to
any destination port above 1023. As an example of an exploit of this rule, an exter-
nal attacker can open a connection from the attacker’s port 5150 to an internal Web
proxy server on port 8080. This is supposed to be forbidden and could allow an attack
on the server. To counter this attack, the firewall rule set can be configured with a
source port field for each row. For rules 2 and 4, the source port is set to 25; for rules
1 and 3, the source port is set to >1023.

But a vulnerability remains. Rules 3 and 4 are intended to specify that any inside
host can send mail to the outside. A TCP packet with a destination port of 25 is routed
to the SMTP server on the destination machine. The problem with this rule is that
the use of port 25 for SMTP receipt is only a default; an outside machine could be
configured to have some other application linked to port 25. As the revised rule 4 is
written, an attacker could gain access to internal machines by sending packets with a
TCP source port number of 25. To counter this threat, we can add an ACK flag field
to each row. For rule 4, the field would indicate that the ACK flag must be set on the
incoming packet. Rule 4 would now look like this:

Sre Dest
Rule | Direction | address | Src port | address | Protocol | Dest port | Flag | Action
4 In External 25 Internal TCP >1023 ACK | Permit

The rule takes advantage of a feature of TCP connections. Once a connection
is set up, the ACK flag of a TCP segment is set to acknowledge segments sent from
the other side. Thus, this rule allows incoming packets with a source port number of
25 that include the ACK flag in the TCP segment.

One advantage of a packet filtering firewall is its simplicity. In addition, packet
filters typically are transparent to users and are very fast. NIST SP 800-41 lists the
following weaknesses of packet filter firewalls:

¢ Because packet filter firewalls do not examine upper-layer data, they cannot
prevent attacks that employ application-specific vulnerabilities or functions. For
example, a packet filter firewall cannot block specific application commands; if

FIR ICR 7] 6 AC HOH
--- page 47 ---
a packet filter firewall allows a given application, all functions available within
that application will be permitted.

¢ Because of the limited information available to the firewall, the logging func-
tionality present in packet filter firewalls is limited. Packet filter logs normally
contain the same information used to make access control decisions (source
address, destination address, and traffic type).

* Most packet filter firewalls do not support advanced user authentication
schemes. Once again, this limitation is mostly due to the lack of upper-layer
functionality by the firewall.

Packet filter firewalls are generally vulnerable to attacks and exploits that take
advantage of problems within the TCP/IP specification and protocol stack, such
as network layer address spoofing. Many packet filter firewalls cannot detect
a network packet in which the OSI Layer 3 addressing information has been
altered. Spoofing attacks are generally employed by intruders to bypass the
security controls implemented in a firewall platform.

¢ Finally, due to the small number of variables used in access control decisions,
packet filter firewalls are susceptible to security breaches caused by improper
configurations. In other words, it is easy to accidentally configure a packet filter
firewall to allow traffic types, sources, and destinations that should be denied
based on an organization’s information security policy.

Some of the attacks that can be made on packet filtering firewalls and the
appropriate countermeasures are the following:

¢ IP address spoofing: The intruder transmits packets from the outside with a
source IP address field containing an address of an internal host. The attacker
hopes that the use of a spoofed address will allow penetration of systems that
employ simple source address security, in which packets from specific trusted
internal hosts are accepted. The countermeasure is to discard packets with an
inside source address if the packet arrives on an external interface. In fact, this
countermeasure is often implemented at the router external to the firewall.

° Source routing attacks: The source station specifies the route that a packet
should take as it crosses the Internet, in the hopes that this will bypass security
measures that do not analyze the source routing information. A countermea-
sure is to discard all packets that use this option.

© Tiny fragment attacks: The intruder uses the IP fragmentation option to create
extremely small fragments and force the TCP header information into a sepa-
rate packet fragment. This attack is designed to circumvent filtering rules that
depend on TCP header information. Typically, a packet filter will make a filter-
ing decision on the first fragment of a packet. All subsequent fragments of that
packet are filtered out solely on the basis that they are part of the packet whose
first fragment was rejected. The attacker hopes the filtering firewall examines
only the first fragment and the remaining fragments are passed through. A tiny
fragment attack can be defeated by enforcing a rule that the first fragment of
a packet must contain a predefined minimum amount of the transport header.
If the first fragment is rejected, the filter can remember the packet and discard
all subsequent fragments.

FRR IC 7 IC ROKK
--- page 48 ---
Stateful Inspection Firewalls

A traditional packet filter makes filtering decisions on an individual packet basis
and does not take into consideration any higher-layer context. To understand what is
meant by context and why a traditional packet filter is limited with regard to context,
a little background is needed. Most standardized applications that run on top of TCP
follow a client/server model. For example, for the SMTP, e-mail is transmitted from
a client system to a server system. The client system generates new e-mail messages,
typically from user input. The server system accepts incoming e-mail messages and
places them in the appropriate user mailboxes. SMTP operates by setting up a TCP
connection between client and server, in which the TCP server port number, which
identifies the SMTP server application, is 25. The TCP port number for the SMTP
client is a number between 1024 and 65535 that is generated by the SMTP client.

In general, when an application that uses TCP creates a session with a remote
host, it creates a TCP connection in which the TCP port number for the remote
(server) application is a number less than 1024 and the TCP port number for the
local (client) application is a number between 1024 and 65535. The numbers less than
1024 are the “well-known” port numbers and are assigned permanently to particular
applications (e.g., 25 for server SMTP). The numbers between 1024 and 65535 are
generated dynamically and have temporary significance only for the lifetime of a
TCP connection.

A simple packet filtering firewall must permit inbound network traffic on all
these high-numbered ports for TCP-based traffic to occur. This creates a vulnerability
that can be exploited by unauthorized users.

A stateful packet inspection firewall tightens up the rules for TCP traffic by
creating a directory of outbound TCP connections, as shown in Table 9.2. There is
an entry for each currently established connection. The packet filter will now allow
incoming traffic to high-numbered ports only for those packets that fit the profile of
one of the entries in this directory.

Table 9.2 Example Stateful Firewall Connection State Table

Destination Connection
Source Address | Source Port Address Destination Port State
192.168.1100 1030 210.9.88.29 80 Established
192.168.1102 1031 216.32.42.123 80 Established
192.168.1.101 1033 173.66.32.122 eal Established
192.168.1.106 1035 177.231.32.12 79 Established
223.43.21.231 1990 192.168.1.6 80 Established
219.22.123,32 2112 192.168.1.6 80 Established
210.99.212.18 3321 192.168.1.6 80 Established
24.102.32.23 1025 192.168.1.6 80 Established
223.21.22.12 1046 192.168.1.6 80 Established

A stateful packet inspection firewall reviews the same packet information as
a packet filtering firewall, but also records information about TCP connections (see
Figure 9.1c). Some stateful firewalls also keep track of TCP sequence numbers to
prevent attacks that depend on the sequence number, such as session hijacking.
Some even inspect limited amounts of application data for some well-known pro-
tocols such as FTP, IM, and SIPS commands, in order to identify and track related
connections.

Q7 [20]
CO-2 Write short note on the following.

SO- a. 1. Boot Sector viruses [10]
BL-2 2. Memory-Resident viruses

--- page 49 ---
Boot Sector Viruses

A special case of virus attachment, but formerly a fairly popular one, is the so-called
boot sector virus. Attackers are interested in creating continuing or repeated harm, instead
of just a one-time assault. For continuity the infection needs to stay around and become an
integral part of the operating system. In such attackers, the easy way to become permanent
is to force the harmful code to be reloaded each time the system is restarted. Actually, a
similar technique works for most types of malicious code, so we first describe the process
for viruses and then explain how the technique extends to other types.

When a computer is started, control begins with firmware that determines which
hardware components are present, tests them, and transfers control to an operating system.
A given hardware platform can run many different operating systems, so the operating
system is not coded in firmware but is instead invoked dynamically, perhaps even by a
user’s choice, after the hardware test.

Ans. Modern operating systems consist of many modules; which modules are included on
any computer depends on the hardware of the computer and attached devices, loaded
software, user preferences and settings, and other factors. An executive oversees the boot
process, loading and initiating the right modules in an acceptable order. Putting together a
jigsaw puzzle is hard enough, but the executive has to work with pieces from many
puzzles at once, somehow putting together just a few pieces from each to form a
consistent, connected whole, without even a picture of what the result will look like when
it is assembled. Some people see flexibility in such a wide array of connectable modules;
others see vulnerability in the uncertainty of which modules will be loaded and how they
will interrelate.

Malicious code can intrude in this bootstrap sequence in several ways. An assault can
revise or add to the list of modules to be loaded, or substitute an infected module for a
good one by changing the address of the module to be loaded or by substituting a modified
routine of the same name. With boot sector attacks, the assailant changes the pointer to the
next part of the operating system to load, as shown in Figure 3-23.

FRI ICR 7. AC OH
--- page 50 ---
Boot Sector << her Sectors. ————____»

Bootstrap
Loader
chain
(a) Before infection
Boot Sector Other Sectors
Virus System Bootstrap

Initialization Loader
Femi

(b) After infection

FIGURE 3-23 Boot or Initialization Time Virus

chain

The boot sector is an especially appealing place to house a virus. The virus gains
control early in the boot process, before most detection tools are active, so that it can
avoid, or at least complicate, detection. The files in the boot area are crucial parts of the
operating system. Consequently, to keep users from accidentally modifying or deleting
them with disastrous results, the operating system makes them “invisible” by not showing
them as part of a normal listing of stored files, thereby preventing their deletion. Thus, the
virus code is not readily noticed by users.

Operating systems have gotten large and complex since the first viruses. The boot
process is still the same, but many more routines are activated during the boot process;
many programs—often hundreds of them—run at startup time. The operating system,
device handlers, and other necessary applications are numerous and have unintelligible
names, so malicious code writers do not need to hide their code completely; probably a
user even seeing a file named malware.exe, would more likely think the file a joke than
some real malicious code. Burying the code among other system routines and placing the
code on the list of programs started at computer startup are current techniques to ensure
that a piece of malware is reactivated.

Memory-Resident Viruses

Some parts of the operating system and most user programs execute, terminate, and
disappear, with their space in memory then being available for anything executed later.
For frequently used parts of the operating system and for a few specialized user programs,
it would take too long to reload the program each time it is needed. Instead, such code
remains in memory and is called “resident” code. Examples of resident code are the
routine that interprets keys pressed on the keyboard, the code that handles error conditions
that arise during a program’s execution, or a program that acts like an alarm clock,
sounding a signal at a time the user determines. Resident routines are sometimes called
TSRs or “terminate and stay resident” routines.

Virus writers also like to attach viruses to resident code because the resident code is
activated many times while the machine is running. Each time the resident code runs, the

virus does too. Once activated, the virus can look for and infect uninfected carriers. For
example, after activation, a boot sector virus might attach itself to a piece of resident code.
Then, each time the virus was activated, it might check whether any removable disk in a
disk drive was infected and, if not, infect it. In this way the virus could spread its infection
to all removable disks used during the computing session.

A virus can also modify the operating system’s table of programs to run. Once the virus
gains control, it can insert a registry entry so that it will be reinvoked each time the system
restarts. In this way, even if the user notices and deletes the executing copy of the virus
from memory, the system will resurrect the virus on the next system restart.

For general malware, executing just once from memory has the obvious disadvantage of
only one opportunity to cause malicious behavior, but on the other hand, if the infectious
code disappears whenever the machine is shut down, the malicious code is less likely to be
analyzed by security teams.

Co-1

SO- b. Describe in brief the security requirements for a system. [10]

BL-2

FR ICR 0) AC RH
--- page 51 ---
Access Control: Limit information system access to authorized users, processes acting on behalf of authorized
users, or devices (including other information systems) and to the types of transactions and functions that
authorized users are permitted to exercise.

Awareness and Training: (i) Ensure that managers and users of organizational information systems are made
aware of the security risks associated with their activities and of the applicable laws, regulations, and policies
related to the security of organizational information systems; and (it) ensure that personnel are adequately
trained to carry out their assigned information security-related duties and responsibilities.

Audit and Accountability: (i) Create, protect, and retain information system audit records to the

extent needed to enable the monitoring. analysis, investigation, and reporting of unlawful, unauthorized,
or inappropriate information system activity; and (11) ensure that the actions of individual information
system users can be uniquely traced to those users so they can be held accountable for their

actions.

Certification, Accreditation, and Security Assessments: (i) Periodically assess the security controls in
organizational information systems to determine if the controls are effective in their application; (ii) develop
and implement plans of action designed to correct deficiencies and reduce or eliminate vulnerabilities in
organizational information systems; (ii) authorize the operation of organizational information systems and
any associated information system connections; and (iv) monitor information system security controls on an
ongoing basis to ensure the continued effectiveness of the controls.

Configuration Management: (i) Establish and maintain baseline configurations and inventories of
organizational information systems (including hardware, software, firmware, and documentation)
throughout the respective system development life cycles; and (ii) establish and enforce security
configuration settings for information technology products employed in organizational information
systems.

Ans. Contingency Planning: Establish, maintain, and implement plans for emergency response, backup
operations, and postdisaster recovery for organizational information systems to ensure the availability
of critical information resources and continuity of operations in emergency situations.

Identification and Authentication: Identify information system users, processes acting on behalf of users, or
devices, and authenticate (or verify) the identities of those users, processes, or devices, as a prerequisite to
allowing access to organizational information systems.

Incident Response: (i) Establish an operational incident-handling capability for organizational information
systems that includes adequate preparation, detection, analysis, containment, recovery, and user-response
activities: and (ii) track, document, and report incidents to appropriate organizational officials and/or
authorities.

Maintenance: (i) Perform periodic and timely maintenance on organizational information systems; and
(ii) provide effective controls on the tools, techniques, mechanisms, and personnel used to conduct
information system maintenance.

Media Protectiom: (i) Protect information system media, both paper and digital; (ii) limit access to information
on information system media to authorized users; and (iii) sanitize or destroy information system media before
disposal or release for reuse.

Physical and Environmental Protection: (i) Limit physical access to information systems, equipment, and
the respective operating environments to authorized individuals: (ii) protect the physical plant and support
infrastructure for information systems; (iii) provide supporting utilities for information systems; (iv) protect
information systems against environmental hazards: and (v) provide appropriate environmental controls in
facilities containing information systems.

Planning: Develop, document, periodically update, and implement security plans for organizational informa-
tion systems that describe the security controls in place or planned for the information systems and the rules
of behavior for individuals accessing the information systems.

FRR ICR 7 FA HH
--- page 52 ---
Personnel Security: (1) Ensure that individuals occupying positions of responsibility within organizations
(including third-party service providers) are trustworthy and meet established security criteria for thase
positions: (ii) ensure that organizational information and information systems are protected during and after
personnel actions such as terminations and transfers; and (iii) employ formal sanctions for personnel failing to
comply with organizational security policies and procedures.

Risk Assessment: Periodically assess the risk to organizational operations (including mission, functions,
image, oF reputation), organizational assets, and individuals, resulting from the operation of organizational
information systems and the associated processing, storage, or transmission of organizational information.

Systems and Services Acquisition: (1) Allocate sufficient resources to adequately protect organizational
information systems; (il) employ system development life cycle processes that incorporate information security
considerations; (iii) employ software usage and installation restrictions; and (iv) ensure that third-party
providers employ adequate security measures to protect information, applications, and/or services outsourced
from the organization.

System and Communications Protection: (i) Monitor, control, and protect organizational communications
(Lc. information transmitted or received by organizational information systems) at the external boundaries
and key internal boundaries of the information systems; and (11) employ architectural designs, software devel-
opment techniques, and systems engineering principles that promote effective information security within
organizational information systems.

System and Information Integrity: (i) Identify, report, and correct information and information system flaws
in a timely manner; (i) provide protection from malicious code at appropriate locations within organizational
information systems; and (iii) monitor information system security alerts and advisories and take appropriate
actions in response.

FRI ICR DD A HH
````

## 2024-25 · Final-Exam · Sem 6 · Answer key · paper 433a19d55d5d

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_06/Final-Exam/BTech_CSE_DS_7011/Information Security/ANS_Information Security(702CO0C039)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Apr 2025
- Text: mixed (22 pages), mean OCR confidence 89.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2024-2025)
Subject: Information Security
Date: 29 Apr 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 22 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Figures in brackets on the right-hand side indicate full marks.
9. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
CO-1   a.
SO-1   State the various security goals of information security.   [5]
BL-2
Ans.
CO-3   b.   Demonstrate the issues faced due to common password and a
SO-2   [5]
countermeasure from the same.
BL-3
********** 1 **********

[Text in pictures on this page, read by OCR]
, Security Goals

> Confidentiality > Authentication
* Assuring that the communicating
entity is the one that it claims to be

> Access Control

* Only intended users should be able
to access the contents of a message

> Integrity * Who can access what resources and|
» Amessage should be preserved as it! under what conditions
travels from one point to another > Non-Repudiation
> Availability * Protection against denial by one of
the entities involved in a
» It ensures that the resources are communication

available to the authorized entities
at all time
--- page 2 ---
Ans. | Password Authentication

> Bank A
Bank A

pwd, | pw, wd ew
a Pwds| OW sacar ais
Fake Site

» User cannot reliably identify fake sites » Phishing attack or break-in at site B
» Captured password can be used at reveals pwd at A
target site » Server-side solutions will not
keep pwd safe

» Solution: Strengthen with client-
side support

Common Password

Salting

. BankA)
ae ARERG BankA salt at its most fundamental level is random

data. When a properly protected password

system receives a new password, it will create a

Sit hashed value for that password, create a new
eB) Site B random salt value, and then store that
. combined value in its database. This helps

hash(owd,,

* defend against dictionary attacks and known
» Generate a unique password per site hash attacks.
HMACfido:123(banka.com) > » For example, if a user uses the same password
Qz7a+0ekEXb on two different systems, if they used the same
HMACfido:123(siteb.com) > OzX2+ICiqe hashing algorithm, they could end up with the
. . * . ‘, same hash value. However, if even one of the
Hashed password is not usable at any other site systems uses salt with its hashes, the values will
Protects against password phishing be different.
Protects against common password
problem
co-3 |. _
So-2 Compare and contrast circuit level gateway and proxy firewalls. [5]
BL-4
Ans.

Firewall types - Circuit Level Gateways

» As another simplistic firewall type that is meant to quickly and easily approve or deny traffic
without consuming significant computing resources, circuit-level gateways work by verifying the
transmission control protocol (TCP) handshake. This TCP handshake check is designed to make

sure that the session the packet is from is legitimate.

» While extremely resource-efficient, these firewalls do not check the packet itself. So, if a packet
held malware, but had the right TCP handshake, it would pass right through. This is why circuit-

level gateways are not enough to protect your business by themselves.

FIC 2 I HH ar
--- page 3 ---
d.   State the following:
1. Risk identification
CO-2   2. Risk assessment
SO-2   [5]
3. Risk control
BL-1
4. Risk impact
5. Risk exposure
Ans.
********** 3 **********

[Text in pictures on this page, read by OCR]
Firewall types - Proxy

» Proxy firewalls operate at the application layer to filter incoming traffic between your network and
the traffic source—hence, the name “application-level gateway.” These firewalls are delivered via a
cloud-based solution or another proxy device. Rather than letting traffic connect directly, the proxy
firewall first establishes a connection to the source of the traffic and inspects the incoming data
packet.

» This check is similar_to the stateful inspection firewall in that it looks at both the packet and at the
TCP handshake protocol. However, proxy firewalls may also perform deep-layer packet inspections,
checking the actual contents of the information packet to verify that it contains no malware.

» Once the check is complete, and the packet is approved to connect to the destination, the proxy
sends it off. This creates an extra layer of separation between the “client” (the system where the
packet originated) and the individual devices on your network—obscuring them to create additional
anonymity and protection for your network.

» If there’s one drawback to proxy firewalls, it’s that they can create significant slowdown because of
the extra steps in the data packet transferal process.

Hi Risk Identification - is the examination and
documentation of the security posture of an organization’s
information technology and the risks it faces.

i Risk Assessment — is the determination of the extent to
which the organization’s information assets are exposed or at
risk.

i Risk Control — is the application of controls to reduce the
risks to an organization’s data and information systems

lf A risk is a potential problem that the system or its users
may experience.
i We distinguish a risk from other project events by looking for three
things
© A loss associated with an event. This loss is called the risk
impact.
© The likelihood that the event will occur. The probability of
occurrence associated with each risk is measured from o
(impossible) to 1 (certain).
© The degree to which we can change the outcome. Risk control

involves a set of actions to reduce or eliminate the risk.
6
--- page 4 ---
I Effects of a risk can be quantified by multiplying the risk impact by
the risk probability, known as risk exposure.

i For example, if the likelihood of virus attack is 0.3 and the cost to
clean up the affected files is Rs.10,000/- then the risk exposure is
Rs.3,000/-

Hl So we can use a calculation like this one to decide that a virus checker
is worth an investment of Rs.100, since it will prevent a much larger
potential loss.

Q2 [20]

Soo a. | What is a computer virus and describe the different types of viruses in (10)
BL-1 depth.

Ans. | MALICIOUS PROGRAM ERRORS

TYPES OF FUNCTION
MALICIOUS CODE

Virus Code that attaches to another program and copies itself to other programs.
+ Transient virus — life depends on life of its host
Resident virus — locates inside memory
Trojan Horse malicious effect is hidden from user (Ex: login script)
Logic viruses triggered by an event and goes off when specific condition occur

Time viruses triggered by a time or date

ONE TIME EXECUTION |

a The majority of viruses today execute only once, spreading
their infection and causing their effect in that one
execution.

= A virus often arrives as an e-mail attachment of a
document virus. It is executed just by being opened

BOOT SECTOR VIRUSES

= Aspecial case of virus attachment

m= When a computer is started, control begins with firmware that
determines which hardware components are present, tests them, and
transfers control to an operating system.

mu The operating system is software stored on disk. Code copies the
operating system from disk to memory and transfers control to it; this
copying is called the bootstrap (often boot) load

FIC 7) IC HOH
--- page 5 ---
BOOT SECTOR VIRUSES

m To allow for change, expansion, and uncertainty, hardware designers reserve
a large amount of space for the bootstrap load.

m The boot sector on a PC is slightly less than 512 bytes, but since the loader
will be larger than that, the hardware designers support "chaining," in which
each block of the bootstrap is chained to (contains the disk location of) the
next block.

m The virus writer simple breaks the chain at any point, inserts a pointer to the
virus code and reconnects the chain after the virus has been inserted.

BOOT SECTOR VIRUSES

The boot sector is an ee Cie Seco
appealing place to
house a virus. The ben) noni
virus gains control
before most a |
detection tools are (@) Before infection
active, so that it can
avoid detection. The Boot Sector =
virus code is not vn re perm
noticed by users. as = mcd

= Some parts of the operating system and most user programs execute,
terminate, and disappear, with their space in memory being available
for anything executed later.

a For very frequently used parts of the operating system and for a few
specialized user programs, it would take too long to reload the
program each time it is needed.

m Such code remains in memory and is called "resident" code.

= Virus writers like to attach viruses to resident code because the
resident code is activated many times while the machine is running.
Each time the resident code runs, the virus does too.

DOCUMENT VIRUSES

u It is implemented within a formatted document, such as a written
document, a database, a slide presentation, or a spreadsheet.

mu These documents are highly structured files that contain both data
(words or numbers) and commands (such as formulas, formatting

controls, links).

CcO-3 b. | Discuss the working of IDPS. List and explain the various types of

[10]
SO-2 IDPS.

FEISS (5 FC ICRF
--- page 6 ---
BL-2

“"s-| Intrusion Detection System & its

Types

» An intrusion occurs when an attacker attempts to gain entry into or disrupt the normal operations
of an information system, almost always with the intent to do harm.

» Intrusion detection consists of procedures and systems that identify system intrusions.

» Intrusion reaction encompasses the actions an organization takes when an intrusion is detected.

» Intrusion correction activities finalize the restoration of operations to a normal state and seek to

cannot occur again—thus reinitiating intrusion prevention.

Intrusion Detection System & its
Types

» Host-based IDS (HIDS) - Monitors and analyzes activities on individual hosts or devices within a
network. It focuses on detecting suspicious behavior at the host level, such as unauthorized access

or changes to system files.

» Network-based IDS (NIDS) - Examines network traffic and identifies suspicious patterns or
anomalies. NIDS is deployed at strategic points within the network to monitor traffic and detect
potential threats.

»   Signature-based IDS - Relies on a database of predefined signatures or patterns associated with
known threats. It compares network or system activity against these signatures to identify and alert
on known attacks.

Intrusion Detection System & its
Types

» Anomaly-based IDS - Learns the baseline behavior of the network or system and triggers alerts
when deviations from the normal behavior are detected. Anomaly-based IDS is effective in
detecting new and unknown threats.

» Heuristic-based IDS - Uses predefined rules and algorithms to identify patterns or behaviors that
may indicate potential security incidents. Heuristic-based IDS combines aspects of both signature-
based and anomaly-based detection.

» Behavior-based IDS - Analyzes the behavior of users, applications, or systems to detect abnormal
activities that may indicate a security threat. This approach focuses on deviations from expected
behavior.

Intrusion Prevention System & its
Types

» Intrusion prevention consists of activities that deter an intrusion. Some important
intrusion prevention activities are writing and implementing good enterprise
information security policy, planning and executing effective information security
programs, installing and _ testing technology-based information security
countermeasures (such as firewalls and intrusion detection systems), and conducting

and measuring the effectiveness of employee training and awareness activities.

FIC 6 I HF
--- page 7 ---
Q3   [20]
CO-3   a.   Report the different types of Access Control Models. Explain the Role
SO-2   [10]
BL-2   Based Access Control Model in depth.
Ans.
********** 7 **********

[Text in pictures on this page, read by OCR]
Intrusion Prevention System & its
Types

» Host-based IPS (HIPS) - Operates on individual hosts or devices to prevent malicious activities at
the host level. HIPS can enforce security policies and respond to threats on the specific host where
it is deployed.

» Network-based IPS (NIPS) - Monitors network traffic in real-time and actively blocks or prevents
malicious activities. NIPS is positioned inline on the network and can take immediate action to stop

or mitigate threats.

»   Signature-based IPS - Uses predefined signatures to identify known threats and takes action to
prevent their execution. Signature-based IPS is effective for blocking well-known attack patterns.

Intrusion Prevention System & its
Types

» Anomaly-based IPS - Analyzes deviations from normal behavior and takes proactive measures to

prevent potential threats. Anomaly-based IPS can dynamically adapt to changing attack patterns.

» Inline IPS - Operates directly in the network traffic path and can block or allow traffic in real-time.
Inline IPS is positioned strategically to provide immediate response to security threats.

» Passive IPS - Monitors network or system activities passively and generates alerts but does not take
direct action to block or prevent threats. Passive IPS can provide insights into potential security

incidents without disrupting normal operations.

» Behavior-based IPS - Analyzes the behavior of users, applications, or systems and takes action to
prevent abnormal activities. Behavior-based IPS focuses on proactively stopping threats based on

observed behaviors.

Mandatory Access Control (MAC) is an access control strategy in which access control
decisions are limited directly to software developers or system administrators, ensuring strict,
system-level control.

Discretionary Access Control (DAC) is an access control strategy in
which users have direct influence over access control decisions regarding their own data.

Role-Based Access Control (RBAC)

* Role-based access control (RBAC) assigns access permissions based on user roles within an
organization. This model simplifies management by grouping permissions into roles rather
than assigning them individually.

Efficient management
* Scalable for large organizations
* Requires well-defined roles
--- page 8 ---
Role-based access control (RBAC)

* Role-based access control (RBAC) restricts network access based on a
person's role within an organization.

* Employees are only allowed to access the information necessary to
effectively perform their job duties.

«Access can be based on several factors, such as authority,
responsibility, and job competency.

* In addition, access to computer resources can be limited to specific
tasks such as the ability to view, create, or modify a file.

* Arole is a collection of permissions that you can apply to users.

Role-based access control (RBAC)
! #3 | Fd — :
i i i : ee
Te) ED =
soe 5 gg |

' : r i
’ ‘ 4 Employee i
' ; ' Sales role 1 i) records '
: IT Sec \ :

Factors DAC MAC RBAC
Access Control to Through owner | Through fixed Through roles
Information of data tules
Access Control Discretion of Classification of | Classification
Based on owner of data users and data of roles
Flexibility for
Accessing High Low High
Information
Access Revocation Very complex Very easy Very easy
Complexity
Support for
Multilevel Database No Yes Yes
System
Used in Initial Unix The U.S. ATLAS
system department of experiment in
defense CERN
CO-4 b. | List the various attack vectors and security controls for information
SO-2 ; [10]
BL-1 security.

FIC QF EH 1
--- page 9 ---
Ans.
Q4   [20]
a.   What are the different types of authentication tokens. Explain the
CO-1   working of the following in detail with the help of a diagram:
SO-1   [10]
BL-1   1. challenge response tokens
2. time based tokens
********** 9 **********

[Text in pictures on this page, read by OCR]
Attack Vectors

» Cloud Computing Threat — Cloud computing is an on-demand delivery of IT capabilities where
sensitive data of organization and their client is stored. Flaw in one client’s application cloud
allows attackers to access other client’s data.

» Advance Persistent Threats — An attack that is focused on stealing information from victim
machine without user being aware of it.

» Viruses and Worms — The most prevalent networking threat that are capable of infecting a
network within seconds.

» Ransomware — Restricts access to the computer system’s files and folder and demands an online

ransom payment to the malware creator(s) in order to remove the restrictions.

» Mobile Threats — Focus have shifted to mobile devices as it has comparatively less security.

Attack Vectors

» Botnet — A huge network of compromised systems used by an intruder to perform various
network attacks.

» Web Application Threats — Attackers target web applications to steal credentials, set up phishing

site or acquire private information to threaten then performance of the website and hamper the

security.

» IoT Threats — loT devices include many software applications that are used to access the device
remotely. Flaws in IoT devices allow attackers access into the device remotely and perform various
attacks.
--- page 10 ---
Ans. | Authentication Token

Token and server are synchronized initially
Token generates fresh passwords periodically

» Same passwords are generated at the server

Authentication Token
Wosin request @) rer

Id: Atul
Password:101 Seed: ?

Client . Sever

| ow Successful Seed found:624 Atul 624

101

Seed: 624 @ ©)

Password: Correct
Password:101

Authentication Password
Token Validation
Program

Authentication Tokens Types

» Challenge Response Tokens
» Time Based Tokens
» Certificate bases Tokens

Challenge Response Authentication
Token

Dron request
Do
Encryption og. | | & Random
Process ~*~ Private Key | Public Key: 624 B
A ®@
Id: Atul \ |
Encngnted Random Challenge: 999 do | |
® Random Challenge: 810 ||
a Decryption Process + Public Key
»)
‘Server compare the two Random Challenge. if match then login successful

FRR ICR 7 OI HOH
--- page 11 ---
Time Based Authentication Token

@ Login request

=" Id: Atul =
Ghent. Password:101 >
, Login Successful Id seed
eedions Atul 624
(CF) Password:101 ee”
+101 5)
| ’
Authentication Token performs a Password Validation
cryptographic operation & generates a Process with system time
Password every 60 sec based on the seed &
system time
Co-4 b.
SO-2 Discuss the Mandatory Access Control Model. [10]
BL-2

[os F 50} oe
Ans. Mandatory Access Control (MAC) is an access control strategy in which access control
decisions are limited directly to software developers or system administrators, ensuring strict,
system-level control.

Discretionary Access Control (DAC) is an access control strategy in
which users have direct influence over access control decisions regarding their own data.

GRole-Based Access Control (RBAC)

* Role-based access control (RBAC) assigns access permissions based on user roles within an
organization. This model simplifies management by grouping permissions into roles rather
than assigning them individually.

¢ Efficient management

°

* Scalable for large organizations
* Requires well-defined roles

le; O
Mandatory Access Control (MAC) is a security model that strictly controls access to information
based on predefined policies set by a central authority. As mentioned previously, in MAC, the
system enforces access rules without giving users the ability to modify permissions for their own
data. This model is primarily designed to support confidentiality, ensuring that sensitive
information is only accessible to pre-authorized users - making it a highly secure but inflexible
model.

MAC Implementation and Examples

MAC is commonly used in highly sensitive environments. These systems use strict policies to
ensure that information remains secure and inaccessible to unauthorized users.

Consider, for example, developing an application for the Windows operating system. You want to
ensure that no other process can access the data in your application unless explicitly allowed by
you. MAC limits access to the data based on predefined policies set by the developer or system
administrator, ensuring only the intended user can access the application.

(Top Secret_)
(Secret)
“ai! Confidential ) ss

(Public)

FRI ICR 7 FI OH
--- page 12 ---
Q5   [20]
a.   Compute the plain text from the following message using Playfair
CO-3   Technique using the key ‘Ramayana’.
SO-2   Grief destroys one’s courage. It destroys one’s learning. It destroys   [10]
BL-5
one’s everything. There is no enemy greater than grief.
Ans.
Key matrix – 3 marks
Rules – 2 marks
Decryption process and explanation – 5 marks
********** 12 **********

[Text in pictures on this page, read by OCR]
Mandatory access control (MAC)

* In this non-discretionary model, people are granted access based on
an information clearance.

* A central authority regulates access rights based on different security
levels.

* It works on a hierarchy pattern.

* MAC is also called a non-discretionary contro! model, which means
that control isn’t gained at the discretion of the user or file owner.
Access provisioning is centrally administered.

* This model is common in government and military environments.

Mandatory access control (MAC)

* MAC uses label-based access control for data and clearance levels to
manage and control access to resources.
* It assigns a security label to every resource in the system.
* These security labels such as ‘confidential’, 'secret,' or ‘public’ are
identified on resources.
* Clearance levels are also assigned to individuals within the organization.
* The clearance level that each individual is assigned will determine the
resources to which they are granted access.
¢« Whenever a user wants to access a resource, the system evaluates
the security label and clearance level of the user to confirm if they
have the appropriate clearance before access is granted.

PLAYFAIR CYPHER

The Playfair cipher uses a 5 by 5 table containing a key word or phrase. Memorization of the
keyword and 4 simple rules was all that was required to create the 5 by 5 table and use the
cipher.

1. Ifboth letters are the same (or only one letter is left), add an "X" after the first letter.
Encrypt the new pair and continue. Some variants of Playfair use "Q" instead of "X", but
any letter, itself uncommon as a repeated pair, will do.

2. Ifthe letters appear on the same row of your table, replace them with the letters to their
immediate right respectively (wrapping around to the left side of the row if a letter in the
original pair was on the right side of the row).

3.. Ifthe letters appear on the same column of your table, replace them with the letters
immediately below respectively (wrapping around to the top side of the column if a letter
in the original pair was on the bottom side of the column).

4. If the letters are not on the same row or column, replace them with the letters on the
same row respectively but at the other pair of corners of the rectangle defined by the
original pair. The order is important — the first letter of the encrypted pair is the one that
lies on the same row as the first letter of the plaintext pair.
--- page 13 ---
b.   Describe non-malicious program errors. Explain the below stated three
error types in depth:
CO-2
SO-2   1. Buffer Overflow   [10]
BL-2
2. Incomplete Mediation
3. Time-to-check to Time-to-use
Ans.
********** 13 **********

[Text in pictures on this page, read by OCR]
NON-MALICIOUS PROGRAM ERRORS

u These errors cause program malfunctions but do not lead
to more serious security vulnerabilities

= We consider three classic error types:
© Buffer overflows
°o Incomplete mediation
© Time-to-check to Time-to-Use Errors

NON-MALICIOUS PROGRAM ERRORS - Buffer Overflow

mu A buffer is a space in which data can be held. A buffer’s capacity is
finite.

m= The programmer must declare the buffer’s max. size so that the
compiler can set aside that amount of space.

m= char sample[1o0];

mu The compiler sets aside 10 bytes to store this buffer.
m= sample[10]="B’

= The subscript is out of bounds

= sample[i]="B’

NON-MALICIOUS PROGRAM ERRORS - Buffer Overflow

Example:

char sample[io];

for (i=0; i<=9; i++)

sample[i] = ‘A’;

sample[10]=‘B’

All programs and data are in memory during execution, sharing space with the OS,
other code.

There are 4 cases to consider in deciding where ‘B’ goes.

= Buffer may overflow into (and change):
© User’s own data space
o User's program area
o System data space
o System program area
--- page 14 ---
NON-MALICIOUS PROGRAM ERRORS - Buffer Overflow

User’s Data

Memory A A A A A A A A A AB
a) Affects user’s data

User’s Program

User's Data code

Memory A A A A A A A A A AB

b) Affects user’s code

NON-MALICIOUS PROGRAM ERRORS - Buffer Overflow

User’s Data System data

Memory A A A A A AA AAA

c) Affects system data

System Program
User’s Data code

Memory A A A A A AA AAA

d) Affects system code

NON-MALICIOUS PROGRAM ERRORS - Buffer Overflow

= Buffer Overflows Security Implication:
o Attacker replaces code in the system space and takes control back
from the operating system
o Attacker uses the stack pointer or return register to execute other
codes
o Parameter passing to web server
e http://www.somesite.com/subpage/data&parm1=
(808)555-1212&parm2=2004Jano1
e What if one of the parameters is made longer?

ms Microsoft's Phone Dialer contains a buffer overrun that allows
execution of arbitary code

FRR IC 7 I OH
--- page 15 ---
NON-MALICIOUS PROGRAM ERRORS

Incomplete Mediation (data checking)

H mesite.com/subpage/data&parm1=

o What if parma is 1800Jano1 or 2004Feb30...

© Use dropdown lists to force the input, test ranges

o Even then, the user could send incorrect data to the server

= Security Implication
o Easy to exploit
Time-of-Check to Time-of-Use Errors
= Concerns Mediation that is performed with a “bait and switch” in the middle
(synchronization flaw)
= Security Implication
© to avoid checking one action and performing another — use digital signatures and

certificates
Q6 [20]
CO-1 a. | List and explain the various design principles for a secure system.
SO-1 [10]

BL-1

Ans.

Design Principles

> Principle of least privilege

> Principle of Fail-Safe Defaults

» Principle of Economy of Mechanism

» Principle of Complete Mediation

> Principle of Open Design

> Principle of Separation of privilege

> Principle of least common mechanism

» Principle of Psychological acceptability

Principle of Least Principle of Fail-Safe
Privilege Defaults.

> Restricts how privileges are granted > Restricts how privileges are initialized
when a subject or object is created
> “a subject should be given only those >
privilege that it needs in order to
complete its task”

“The principle of Fail-Safe defaults states

that, unless a subject is given explicit

access to an object, it should be denied

access to that object”

> ita specific action requires that a
subject’s access rights be augmented, >
those extra rights be relinquished
immediately on completion of the action.

This principle requires that the default
access to an object is none

FRR IC 7 DA HOH
--- page 16 ---
b.   Demonstrate the process of generating symmetric key exchange using
CO-2
SO-2   Diffie Hellman algorithm. And perform a man-in-the-middle attack on   [10]
BL-3
the same.
********** 16 **********

[Text in pictures on this page, read by OCR]
Principle of Complete
Mediation

> Simplifies the design and implementation > this principle restricts the caching of
of security mechanisms information, which often leads to simpler
implementations of mechanisms

> “the principle of economy of mechanism
states that security mechanism should be > “The principle of complete mediation
as simple as possible” requires that all accesses to objects be
checked to ensure that they are allowed”

> ita design and implementations are
simple, fewer possibilities exist for errors > ifthe subject tries to read a resource again
and again, the system should check that the
subject is still allowed to read the object

Principle of Open Design Principle of Separation of

privilege
> the principle suggests that complexity
does not add security > This principle is restrictive because it
> “rhe principle of open design states that limits access to system entities
the security of a mechanism should not > “The principle of separation of privilege
depend on the secrecy of its design or states that a system should not grant
implementation” permission based on single condition”
> Designers of a program must not depend > Company checks for more than 75,000
on secrecy of the details of their design must be signed by two officers of the
and implementation to ensure security company. If either does not sign, the check
> ifthe strength of the program's security is not valid. The two conditions are the

depends on the ignorance of the user, a signatures of two officers

knowledgeable user can defeat that
security mechanism

Principle of Psychological

acceptability
> Co _— . > This principle recognizes the human
This principle is restrictive because it element in computer security
limits sharing we .
> “The Principle of psychological
acceptability states that security
> “The principle of least common mechanism should not make the resource
mechanism states that mechanisms used more difficult to access than if the security
to access resources should not be shared” mechanisms were not present”

> if security related software is too
complicated to configure, system
administrators may unintentionally set up
software in a non secure manner, security-
related user programs must be easy to use
and must output understandable messages

> Sharing resources provides a channel
along which information can be
transmitted, and so such sharing should
be minimized
--- page 17 ---
Ans.
" | SYMMETRIC-KEY EXCHANGE

Diffie-Hellman Key Exchange

Alice Bob
Local key: ‘a’ l Local key: ‘b’
Intermediate key: 48 = ga Intermediate key:
lag = G2 Mod n n Iga = g> mod n
ge ®
Alice computes \en™ Bob computes
Igq® mod n Ing" mod n
= (g> mod n)? mod n = (g* mod n)® mod n
= (g>** mod n) = (g®*> mod n)
= Secret Key, Kags = Secret Key, Kas

Computes Kp, d les Kon
= (g>4 mod n)? mod n i mod n)® mod n

Q7 [20]
CO-2 a.
SO-2 Write a short note on business continuity planning. [10]
BL-1

Ans.
" | BUSINESS CONTINUITY PLANNING

ll The key to coping with such disasters is advance planning and
preparation, identifying activities that will keep a business viable
when the computing technology is disabled.

Hl The steps in business continuity planning are these:

© Assess the business impact of a crisis.
© Develop a strategy to control impact.
© Develop and implement a plan for the strategy

FRR ICR] AC OH
--- page 18 ---
BUSINESS CONTINUITY PLANNING - Assess Business Impact

i Begin by asking two key questions:
Hi What are the essential assets? What are the things that will prevent

the business from doing business?

Hi What could disrupt use of these assets? The vulnerability is more
important than the threat agent.

BUSINESS CONTINUITY PLANNING - Develop Strategy

I The continuity strategy investigates how the key assets can be
safeguarded.
© In some cases, a backup copy of data or redundant hardware or
an alternative manual process is good enough.
© Sometimes, the most reasonable answer is reduced capacity.

ll The result of a strategy analysis is a selection of the best actions,
organized by circumstances.

IM The strategy can then be used as the basis for your business
continuity plan

BUSINESS CONTINUITY PLANNING - Develop Plan

Wl The business continuity plan specifies several important things:
© whois in charge when an incident occurs
° what todo
© who does it

ll The plan justifies making advance arrangements, such as acquiring
redundant equipment, arranging for data backups, and stockpiling
supplies, before the catastrophe.

Wl The plan also justifies advance training so that people know how they
should react.

BUSINESS CONTINUITY PLANNING - incident Response Plans

Hf An incident response plan tells the staff how to deal with a
security incident.
lM In contrast to the business continuity plan, the goal of incident

response is handling the current security incident, without regard for
the business issues.

ll An incident response plan
© should define what constitutes an incident
© identify who is responsible for taking charge of the situation
© describe the plan of action

FOI 7 QF Cr
--- page 19 ---
BUSINESS CONTINUITY PLANNING
The plan usually has three phases:

li Triage

HB running the incident.

ll A fourth phase, review, is useful after the situation abates so that this

incident can lead to improvement for future incident

[ BUSINESS CONTINUITY PLANNING

HB Advance Planning

unhurried, and without pressure.

i Response Team
© Director: person in charge of the incident, who decides what
actions to take and when to terminate the response.
© Lead technician: person who directs and coordinates the
response.
© Advisor(s): legal, human resources, or public relations staff
members as appropriate.

BUSINESS CONTINUITY PLANNING - Response Team

Hl Need to consider certain matters.

I Legal issues: An incident has legal ramifications.
ll Preserving evidence:

I Records:

BB Public relations:

| BUSINESS CONTINUITY PLANNING

i After the Incident Is Resolved

lM Eventually, the incident response team closes the case.

i At this point it will hold a review after the incident to consider two
things:

Hl Js any security control action to be taken?

I Did the incident response plan work?

FOI 7 QF CR
--- page 20 ---
SoD b. | Describe the working of firewall. List and explain the various types of 0
- [10]
BL-2 firewalls.

Ans. | Firewalls

» A firewall is a type of cybersecurity tool that is used to filter traffic on a
network. Firewalls can be used to separate network nodes from external
traffic sources, internal traffic sources, or even specific applications.
Firewalls can be software, hardware, or cloud-based, with each type of

firewall having its own unique pros and cons.

» The primary goal of a firewall is to block malicious traffic requests and data

packets while allowing legitimate traffic through.
Firewall types - Packet Filtering

» As the most “basic” and oldest type of firewall architecture, packet-filtering firewalls basically
create a checkpoint at a traffic router or switch. The firewall performs a simple check of the data
packets coming through the router—inspecting information such as the destination and
origination IP address, packet type, port number, and other surface-level information without
opening up the packet to inspect its contents.

» Ifthe information packet doesn’t pass the inspection, it is dropped.

» The good thing about these firewalls is that they aren’t very resource-intensive. This means they
don’t have a huge impact on system performance and are relatively simple. However, they're also

relatively easy to bypass compared to firewalls with more robust inspection capabilities.

Firewall types - Circuit Level Gateways

» As another simplistic firewall type that is meant to quickly and easily approve or deny traffic
without consuming significant computing resources, circuit-level gateways work by verifying the
transmission control protocol (TCP) handshake. This TCP handshake check is designed to make

sure that the session the packet is from is legitimate.

» While extremely resource-efficient, these firewalls do not check the packet itself. So, if a packet
held malware, but had the right TCP handshake, it would pass right through. This is why circuit-

level gateways are not enough to protect your business by themselves.

Firewall types - Stateful Inspection

» These firewalls combine both packet inspection technology and TCP handshake
verification to create a level of protection greater than either of the previous two

architectures could provide alone.

» However, these firewalls do put more of a strain on computing resources as well. This

may slow down the transfer of legitimate packets compared to the other solutions

FRI ICR DO) A RH
--- page 21 ---
Firewall types - Proxy

» Proxy firewalls operate at the application layer to filter incoming traffic between your network and
the traffic source—hence, the name “application-level gateway.” These firewalls are delivered via a
cloud-based solution or another proxy device. Rather than letting traffic connect directly, the proxy
firewall first establishes a connection to the source of the traffic and inspects the incoming data
packet.

» This check is similar to the stateful inspection firewall in that it looks at both the packet and at the
TCP handshake protocol. However, proxy firewalls may also perform deep-layer packet inspections,
checking the actual contents of the information packet to verify that it contains no malware.

» Once the check is complete, and the packet is approved to connect to the destination, the proxy
sends it off. This creates an extra layer of separation between the “client” (the system where the
packet originated) and the individual devices on your network—obscuring them to create additional
anonymity and protection for your network.

» If there’s one drawback to proxy firewalls, it’s that they can create significant slowdown because of
the extra steps in the data packet transferal process.

Firewall types - Next Generation

» Many of the most recently-released firewall products are being touted as “next-generation”

architectures. However, there is not as much consensus on what makes a firewall truly next-gen.

» Some common features of next-generation firewall architectures include deep-packet inspection
(checking the actual contents of the data packet), TCP handshake checks, and surface-level packet
inspection. Next-generation firewalls may include other technologies as well, such as intrusion

prevention systems (IPSs) that work to automatically stop attacks against your network.

» The issue is that there is no one definition of a next-generation firewall, so it’s important to verify

what specific capabilities such firewalls have before investing in one.

Firewall types - Software

» Software firewalls include any type of firewall that is installed on a local device rather
than a separate piece of hardware (or a cloud server). The big benefit of a software
firewall is that it's highly useful for creating defense in depth by isolating individual

network endpoints from one another.

» However, maintaining individual software firewalls on different devices can be difficult
and time-consuming. Furthermore, not every device on a network may be compatible
with a single software firewall, which may mean having to use several different

software firewalls to cover every asset.
Firewall types - Hardware

» Hardware firewalls use a physical appliance that acts in a manner similar to a traffic router to
intercept data packets and traffic requests before they're connected to the network's servers.
Physical appliance-based firewalls like this excel at perimeter security by making sure malicious
traffic from outside the network is intercepted before the company’s network endpoints are exposed

to risk.

» The major weakness of a hardware-based firewall, however, is that it is often easy for insider
attacks to bypass them. Also, the actual capabilities of a hardware firewall may vary depending on
the manufacturer—some may have a more limited capacity to handle simultaneous connections

than others.

FI ICR D7 FAC HOH
--- page 22 ---
Firewall types - Cloud

» Whenever a cloud solution is used to deliver a firewall, it can be called a cloud firewall,
firewalls by many, since a cloud server is often used in a proxy firewall setup (though

the proxy doesn't necessarily have to be on the cloud, it frequently is).

» The big benefit of having cloud-based firewalls is that they are very easy to scale with
your organization. As your needs grow, you can add additional capacity to the cloud
server to filter larger traffic loads. Cloud firewalls, like hardware firewalls, excel at

perimeter security.

FIR ICR DAC HH
````

## 2024-25 · Re-Exam · Sem 6 · Answer key · paper ccff4ef08d30

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/BTech_CSE_DS_7011/Information Security/ANS_Information Security(702CO0C039)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2025
- Text: mixed (20 pages), mean OCR confidence 89.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2024-2025)
Subject: Information Security
Date: 02 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 20 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Figures in brackets on the right-hand side indicate full marks.
9. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
CO-1   a.   Identify and explain the data categories that hackers would use to create
SO-1   [5]
your identity.
BL-2
Ans.
b.   Describe the authentication system basics and also explain a
CO-3
SO-2   authentication system using mathematical concept of sets with an   [5]
BL-2   example.
********** 1 **********

[Text in pictures on this page, read by OCR]
Data Categories

= Any information about you is your data
« This data is used to identify you online

« Your computing devices have become the
portal to your data and generate information
about you

= Hackers want your money - that's a short
term profit

« Hackers want your identity - that a long term
profit

A ~~ | 7 |fat Qa Qa
--- page 2 ---
Ans. | Authentication Basic

» Authentication: binding of identity to subject
» Identity is that of external entity (my identity, Sam, etc.)
> Subject is computer entity (process, etc.)
» The information comes from one or more of the following
> What entity knows (eg. password)
> What entity has (eg. badge, smart card)
> What entity is (eg. fingerprints, retinal characteristics)
> Where entity is (eg. In front of a particular terminal)
» An authentication process consists of obtaining authentication information, analyzing the data

and determining if it is associated with that entity

Authentication System

> (A,C,F,L,S)
» Set A specific information with which entity proves their identity
» Set C complementary information stored on computer and used to validate
authentication information
> Set F complementation functions; f: A ~ -Cc
> Set L authentication functions that verify identity; 1:A*C —-» {true, false}
> Set S selection functions enabling entity to create, alter information in A or C

CO-3 c.
SO-2 Discuss the different types of filtering services. [5]
BL-2

Ans.

Types of Filtering services

» Firewall — Examines the content and make the decision based on the traffic.

» Intrusion Prevention System — Monitor network and/or system activities for
malicious exploits or security policy violations and take action to block or prevent
those activities.

» Antivirus and Antimalware Filters — Scan files and network traffic for known
patterns or signatures of malicious software and prevent them from entering the
network.

» Web Content Filtering — Control and restrict access to certain websites or content
categories based on predefined policies. This helps prevent users from accessing

malicious or inappropriate content.

FIC 2 I HH ar
--- page 3 ---
CO-2   d.
SO-2   Describe the three strategies for dealing with risk.   [5]
BL-2
Ans.
Q2   [20]
a.   Describe virus using the following points:
1. signature
CO-2
SO-2   2. storage patterns   [10]
BL-2
3. execution patterns
4. transmission patterns
********** 3 **********

[Text in pictures on this page, read by OCR]
Types of Filtering services

» Email Filtering — Scan email content and attachments for malicious code, phishing
attempts, or spam. Email filtering helps prevent the delivery of malicious content
through email.

» DNS Filtering — Block access to malicious websites by filtering DNS requests. DNS
filtering can prevent users from accessing known malicious domains or websites.

» Application Layer Filtering — Control or block specific applications or services at
the application layer. This can include filtering instant messaging, peer-to-peer file

sharing, or other applications that may pose security risks.

Types of Filtering services

» Virtual Private Network Filtering — Manage and control access to VPN
connections to ensure secure and authorized remote access to the network.

» Data Loss Prevention — Monitor and control the transfer of sensitive data within
the network to prevent unauthorized access or data leakage.

» Packet Filtering — Examines packets of data and makes decisions to allow or block
the transmission based on predefined rules.

» Behavioral Analysis — Analyze the behavior of network traffic and detect anomalies

or patterns indicative of potential security threats.

ll In general, we have three strategies for dealing with risk:

1. Avoiding the risk, by changing requirements for security or other
system characteristics

2. Transferring the risk, by allocating the risk to other systems,
people, organizations, or assets; or by buying insurance to cover any
financial loss should the risk become a reality

3. Assuming the risk, by accepting it, controlling it with available
resources, and preparing to deal with the loss if it occurs
--- page 4 ---
Ans. || VIRUS SIGNATURES

= Avirus cannot be completely invisible.

= Code must be stored somewhere, and the code must be in memory to
execute.

= Moreover, the virus executes in a particular way, using certain
methods to spread.

mu Each of these characteristics yields a pattern, called a signature, that
can be found by a program that knows to look for it.

m The virus's signature is important for creating a program, called a
virus scanner, that can automatically detect and, in some cases,
remove viruses.

m The scanner searches memory and long-term storage, monitoring
execution and watching for the signatures of viruses.

m When the scanner recognizes a known virus's pattern, it can then block
the virus, inform the user, and deactivate or remove the virus.
However, a virus scanner is effective only if it has been kept up-to-date
with the latest information on current viruses

= Most viruses attach to programs that are stored on
media such as disks. The attached virus piece is
invariant, so that the start of the virus code becomes | rated [S7—— recognizable —" ie
a detectable signature. The attached piece is always | VirusCode ‘signature elements
located at the same position relative to its attached
file.

. A virus may attach itself to a file, in which case the a=
file's size grows. Or the virus may obliterate all or Original
part of the underlying program, in which case the | Pram
program's size does not change but the program's
functioning will be impaired. The virus writer has to
choose one of these detectable effects.

= The virus scanner can use a code or checksum to Separate

detect changes to a file. It can also look for suspicious Meek
patterns, such as a JUMP instruction as the first
instruction of a system program

EXECUTION PATTERNS

= A virus writer may want a virus to do several things at the same time,
namely, spread infection, avoid detection, and cause harm.

= Unfortunately, many of these behaviours are perfectly normal and
might otherwise go undetected. For instance, one goal is modifying the
file directory; many normal programs create files, delete files, and
write to storage media. Thus, there are no key signals that point to the
presence of a virus.

FIC 7) IC HOH
--- page 5 ---
Attach to executable program Modify file directory
Write to executable program file

Attach to data or control file Modify directory, rewrite data, append to data, append data
to self
Remain in memory Intercept interrupt by modifying interrupt handler address
table
Load self in nontransient memory area
Infect disks Intercept interrupt
Intercept OS call (eg., to format disk)
Modify system file
Modify ordinary executable program
Conceal self Intercept system calls that would reveal self and falsify result
Spread infection Infect boot sector, infect systems program,

Infect ordinary program

Infect data ordinary program reads to control its execution
Prevent deactivation Activate before deactivating program and block deactivation

Store copy to reinfect after deactivation

CO-3 b. Explain the working on NAT. List and discuss the various types of
SO-2 [10]
BL-1 NAT.

Ans. | Network Address Translation (NAT)

+ Network Address Translation (NAT) - is a technique used in networking to map private IP
addresses within a local network to a single public IP address or a small pool of public IP addresses.
NAT enables multiple devices within a private network to share a common public IP address when
communicating with external networks like the Internet. This provides a level of security by hiding
internal network structures and conserves public IP address space.

Purpose of NAT
Address Conservation

Security

IPV4 Address Exhaustion Mitigation

Types of Network Address
Translation (NAT)

» Static (NAT) - A one-to-one mapping where a private IP address is permanently mapped to a
specific public IP address. Static NAT is often used for servers or devices that need to be
consistently accessible from the external network.

» Dynamic (NAT) - Maps private IP addresses to a pool of public IP addresses dynamically. As
devices within the private network initiate communication, they are assigned an available public IP
address from the pool.

Overloading (NAT Overload or PAT - Port Address Translation) - Maps multiple private IP

addresses to a single public IP address but uses different source ports to distinguish between

connections. This allows many internal devices to share a single public IP address.

FIC DI EH ar
--- page 6 ---
Types of Network Address
Translation (NAT)

» NAT64 - Facilitates communication between IPv6-only and IPv4-only devices by translating IPv6
addresses to IPv4 addresses and vice versa. NAT64 is used to bridge the gap between IPv4 and IPv6
networks.

» NAT-PT (Network Address Translation - Protocol Translation) - A more comprehensive approach
that not only translates addresses but also handles protocol translation between IPv6 and IPv4.
NAT-PT has been largely deprecated in favor of other transition mechanisms.

Components of Network Address
Translation (NAT)

» Inside Local Address - The private IP address assigned to a device within the local network.

» Inside Global Address - The public IP address assigned to a device within the local network after
translation.

» Outside Local Address - The private IP address of a device in the external network (e.g., the

Internet) before translation.

» Outside Global Address - The public IP address of a device in the external network after translation.

Network Address Translation (NAT)

Consideration and Challenges Inside Local Address

» Port Exhaustion - In NAT Overload (PAT), the limited number of source ports can be exhausted
under heavy usage, leading to performance issues.

» Application Compatibilities - Some applications may encounter issues when used across NAT,
especially if they embed IP addresses in the application data.

» Complex Configurations - Large-scale networks with complex applications may require careful
configuration and management of NAT rules.
IPv6 Transition - As the transition to IPv6 progresses, NAT may become less prevalent, and direct

end-to-end connectivity could be favored.

Q3 [20]

CO-3 a.
SO-2 Compare and Contrast DAC and MAC Access Control Models. [10]
BL-4

Ans.

FIC 6 I HF
--- page 7 ---
CO-4   b.   Discuss the phases of security policy development. Also, describe the
SO-2   [10]
BL-2   security policy categories, types and format.
********** 7 **********

[Text in pictures on this page, read by OCR]
Factors DAC MAC RBAC ABAC

Access Control to Through owner | Through fixed Through roles Through

Information of data tules attributes

Access Control Discretion of Classification of | Classification Evaluation of

Based on owner of data users and data of roles attributes

Flexibility for

Accessing High Low High Very high

Information

Access Revocation Very complex Very easy Very easy Very easy

Complexity

Support for

Multilevel Database No Yes Yes Yes

System

Used in Initial Unix The U.S. ATLAS The Federal
system department of experiment in government

defense CERN

MAC vs. DAC

Aspect Mandatory Access Control (MAC) Discretionary Access Control (DAC)

Definition System tevel control set by administrators User-level control over data and
or developers permissions

Control Level Centralized Decentralized

Flexibility Low High

Security Confidentiality User Agency

Requirement

Management Admins set policies and permissions Users manage their own permissions

Implementation Predefined policies strictly enforced Users define access controls for their
resources

Examples of Use Any strictly monitored system Social networks, file systems

Strengths - High security- Strict control - Flexibility- User autonomy

Limitations ~ Inflexibility- Not user-friendly ~- Security risks- Potential for

misconfigurations

User Management Managed by administrators Managed by individual users
--- page 8 ---
Ans.

Security Policy Development Phases

. a Gather Requirements
> Requirement gathering

s
> Regulatory requirements (industry specific)
E s 5 Define Project
» Advisory requirements (best practice) m7
> Information requirements (organization specific)
» Project definition and proposal based on requirements
=

> Policy development

> Review and approval

» Publication and distribution

» Ongoing maintenance (and revision)

Policy Category

» Regulatory : for audit and compliance purpose
» Advisory : generally based on security best practices

» Informative : which are not included in regulatory or advisory

Types of Security Policies

» A military security policy (also called a government security policy) is a security
policy developed primarily to provide confidentiality.

» A commercial security policy is a security policy developed primarily to provide
integrity.

» Aconfidentiality policy is a security policy dealing only with confidentiality.

» An integrity policy is a security policy dealing only with integrity.

Security Policy Format

1, Author - The policy writer 9. Exceptions - Who or what is not covered
2. Sponsor - The Executive champion by the policy
3. Authorizer - The Executive signer with 10. Enforcements - How the policy will be

ultimate authority enforced, and consequences for not
4. Effective date - When the policy is effective; following it

generally when authorized 11. Definitions - Terms the reader may need
5. Review date - Subject to agreement by all to know

parties; annually at least 12. References - Links to other related
6. Purpose - Why the policy exists; regulatory, policies and corporate documents

advisory, or informative

Scope - Who the policy affects and where
the policy is applied

8. Policy - What the policy is about

Q4

[20]

FIC QF EH 1
--- page 9 ---
CO-1   a.
SO-1   Explain the working on network authentication protocol.   [10]
BL-1
Ans.   Kerberos is a computer network security protocol that authenticates service requests
between two or more trusted hosts across an untrusted network, like the internet. It uses
secret-key cryptography and a trusted third party for authenticating client-server
applications and verifying users' identities.
Kerberos provides a credible security solution for businesses of all sizes. But how does
Kerberos authentication work, exactly?
Kerberos uses symmetric key cryptography and a key distribution center (KDC) to
authenticate and verify user identities. A KDC involves three aspects:
1. A ticket-granting server (TGS) that connects the user with the service server
(SS)
2. A Kerberos database that stores the password and identification of all verified
users
3. An authentication server (AS) that performs the initial authentication
During authentication, Kerberos stores the specific ticket for each session on the end-
user's device. Instead of a password, a Kerberos-aware service looks for this
ticket. Kerberos authentication takes place in a Kerberos realm, an environment in
which a KDC is authorized to authenticate a service, host, or user.
Kerberos authentication is a multistep process that consists of the following
components:
1. The client who initiates the need for a service request on the user's behalf
2. The server, which hosts the service that the user needs access to
3. The AS, which performs client authentication. If authentication is successful,
the client is issued a ticket-granting ticket (TGT) or user authentication token,
which is proof that the client has been authenticated.
4. The KDC and its three components: the AS, the TGS, and the Kerberos
database
The TGS application that issues service tickets
Advantages of Kerberos
•   Access Control
•   Mutual Authentication
•   Limited Ticket Lifetime
•   Reusable Authentication
Security
********** 9 **********

[Text in pictures on this page, read by OCR]
KERBEROS TICKET EXCHANGE

=e
£ OS ue

J
i Pda Here in my TGT. give me a Service

USER LOGINS
TO GAIN
NETWOK

4
Herein youn Service Ticket

ACCESS
--- page 10 ---
CO-4   b.
SO-2   Discuss Discretionary Access Control Model.   [10]
BL-2
Ans.
Q5   [20]
a.   Sketch the process of using public key certificate for digital signature.
CO-3
SO-2   And demonstrate how digital signatures provide message authentication   [10]
BL-3
and message integrity.
********** 10 **********

[Text in pictures on this page, read by OCR]
fo) F O ee
Mandatory Access Control (MAC) is an access control strategy in which access control
decisions are limited directly to software developers or system administrators, ensuring strict,
system-level control.

Discretionary Access Control (DAC) is an access control strategy in
which users have direct influence over access control decisions regarding their own data.

GRole-Based Access Control (RBAC)

* Role-based access control (RBAC) assigns access permissions based on user roles within an
organization. This model simplifies management by grouping permissions into roles rather
than assigning them individually.

* Efficient management

°

* Scalable for large organizations
* Requires well-defined roles

° O

What is Discretionary Access Control (DAC)?

Discretionary Access Control (DAC) is a strategy that grants users control over their own data. Unlike MAC, where
access decisions are made by the system administrators or developers, DAC allows the data owners to decide who
can access their data and what actions they can perform. This model emphasizes flexibility and user autonomy.

DAC Implementation and Examples:

DAC is widely used in environments where user flexibility and data sharing are essential. A common traditional
example is the way file permissions are managed in operating systems like Windows or Unix. Users can create files
and folders and then set permissions to determine who else can read, write, or execute those files.

Another common example is found in social networking platforms. Users can choose who sees their posts, who can
comment, and who can share their content. This level of control allows users to manage their privacy and
interactions directly.
Discretionary means that access decisions are made “at the discretion” of the users that have access to the data.
In this method, the owner or administrator of the protected system, data, or resource sets the policies for who is
allowed access.
Example of DAC: File and Folder permissions that exist in Windows and Unix-based operating systems.
DAC attributes include:

* User may transfer object ownership to another user(s).

* User may determine the access type of other users.

* After several attempts, authorization failures restrict user access.

Discretionary access control (DAC)

Discretionary access control (DAC):

¢ Applications:

* Social Networks: Many social media networks allow users to limit or regulate
access to the content they create. In social media networks, DAC allows the
data owner to decide who can or can’t view it.

* For example: Facebook’s friend:--The platform doesn’t allow users that see friend-locked
content to share the data.

* Google Docs and Google Sheets: The owner and creator of the document can
grant access privileges to the document on several different levels.

* Unix file mode: Computer file systems and UNIX, in particular, use the DAC
model for read, write, and view permissions of files.

* Smartphone applications: Application requires access to your location,
contacts, or media folders, granting those permissions is at the user’s
discretion.
--- page 11 ---
Ans. PUBLIC-KEY CERTIFICATE USE

1. User software (client) creates a pair of keys: one public and one private.

2. Client prepares an unsigned certificate that includes the user ID and user’s public key.

3. User provides the unsigned certificate to a CA in some secure manner. This might require a
face-to-face meeting, the use of registered e-mail, or happen via a web form with e-mail
verification.

4. CAcreates a signature as follows:

> CA uses a hash function to calculate the hash code of the unsigned certificate. A hash
function is one that maps a variable-length data block or message into a fixed-length
value called a hash code, such as SHA family.

> ca encrypts the hash code with the CA’s private key.

PUBLIC-KEY CERTIFICATE USE

5. CA attaches the signature to the unsigned certificate to create a signed certificate.
le returns the signed certificate to client.

6. cA the signed certifi li

7. Client may provide the signed certificate to any other user.

8. Any user may verify that the certificate is valid as follows:
> User calculates the hash code of certificate (not including signature).
> User decrypts the signature using CA’s known public key.
> User compares the results of (a) and (b). If there is a match, the certificate is
valid.

PUBLIC-KEY CERTIFICATE USE

Unsigned certiteate: on
contains user ID, and
user's public key, ‘ena
vals -
‘concerning the CA ‘Bob's public key
TA Recipient can verity
information

E EE
Generate hash Signed certificate
code of unsigned
certificate a
Encrypt hash code Decrypt signature
with CA's private key with CA's public key
to form signature to recover hash code
Create signed ‘Use certificate to
digital certificate verify Bob's public key

FRI ICR 7 FI OH
--- page 12 ---
DIGITAL SIGNATURE

Digital Signature Process
Alice Bob
TNs M: Message Pe
{ i 4 S: Signature ‘ ‘ ;
' Signing : ' Verifying :
| algorithm ' | algorithm :
a f------- (M, S) tld + Soeeeee,

ft — 4 M: Message enna y ann
iM Alice’s S: Signature | Alice’s We '
{| Siprivate key | ipublickey ff f
‘| Signing : Verifying |!
‘| algorithm H g algorithm |}
tanned }----------- (M.S) ee ——

A digital signature needs a public-key system.
The signer signs with her private key; the verifier verifies with the signer’s public key.

DIGITAL SIGNATURE
Signing the digest

Alice Bob

a i , M: Message eee 2

' Alice’s | S: Signature ' Alice’s '

' M Private key ' ‘ public key M '

Le
CO-2 b.
SO-2 List and explain the different types of controls against program threats. [10]
BL-2

FRR ICR] DA KH
--- page 13 ---
Ans. | T CONTROLS AGAINST PROGRAM THREATS

m There are many ways a program can fail and many ways to turn
the underlying faults into security failures.
m It is better to focus on prevention than cure; how do we use
controls during s/w development to find and eliminate the faults.
a Three types of controls:
© Developmental controls
© Operating system
© administrative

= Developmental controls:
= Many controls can be applied during s/w development to fix problems.

a The nature of s/w development:
©. specify
o Design
o Implement
o Test
°o Review
© Document the system
o Manage
© maintain

a Modularity, Encapsulation and information hiding:

= Akey principle of SE is to create a design or code in small, self-contained units
called components/modules, when a system is written this way, it is called
modular

= Ifacomponent is isolated from the effects of other components, then
© itis easier to trace a problem to the fault that caused it
© easier to maintain the system
co Easier to see where vulnerabilities may lie

a This isolation is called encapsulation

= Information hiding is another characteristic of modular s/w.

= When information is hidden, each component hides its implementation from
others, so that when a change is needed, the overall design can remain intact.

= Modularity:

= Modularization is a process of dividing a task into subtasks.
u_ The goal is to have each component meet 4 conditions:

= Single-purpose: performs one function

= Small: consists of an amount of information for which a human can
readily grasp both structure and content.

= Simple: is of a low degree of complexity so that a human can readily
understand the purpose and structure of the module.

= Independent: performs a task isolated from other modules.

FOI 7 2 FC CR
--- page 14 ---
CONTROLS AGAINST PROGRAM THREATS

a Modularity:

mu Advantages:
© Maintenance
© Understandability
© Reuse
© Correctness
o Testing

= A modular component has high cohesion and low coupling

CONTROLS AGAINST PROGRAM THREATS

Modularity:

= Cohesion: all elements of a component have a logical and functional
reason; every aspect of the component is tied to the component's single
purpose.
o Ahigh cohesive component has high degree of focus on purpose
© Low degree cohesion means that component’s are unrelated.

= Coupling: refers to the degree with which a component depends on
other components in the system
© Thus, low coupling is better than tight coupling.

CONTROLS AGAINST PROGRAM THREATS

= Encapsulation:
o It hides a component’s implementation details, but it does not
necessarily mean complete isolation.
© The sharing is documented so that a component is affected only in
known ways by others.
© Sharing is minimized so that fewest interfaces possible are used.
= Information hiding:
o Component is a black box with certain well-defined inputs and
outputs and well-defined function.
© Other components do not need to know how the module completes
its function.

CONTROLS AGAINST PROGRAM THREATS

m Peer Reviews

= Hazard Analysis — set of systematic techniques to expose potentially
hazardous system states

= Testing -— unit testing, integration testing, function testing,
performance testing, acceptance testing, installation _ testing,
regression testing

= Good Design

© Using a philosophy of fault tolerance

© Havea consistent policy for handling failures
o Capture the design rationale and history

© Use design patterns

FRR IC 7 I OH
--- page 15 ---
CONTROLS AGAINST PROGRAM THREATS

= Prediction — predict the risks involved in building and using the
system

= Static Analysis — Use tools and techniques to examine characteristics
of design and code to see if the characteristics warn of possible faults

= Configuration Management — control changes during development
and maintenance

m Analysis of Mistakes

= Proofs of Program Correctness — Can we prove that there are no
security holes?

ADMINISTRATIVE CONTROLS

m= Standards of Program Development
m Standards of design
m Standards of documentation, language, and coding style
= Standards of programming
m= Standards of testing
= Standards of configuration management
= Security Audits

= Separation of Duties

Q6 [20]
a. Write a short note on the following:
co-1 1. Vulnerabilities
SO-1 [10]
BL-1 2. Threats
3. Attacks
Ans. ce
Vulnerability Threats
= It’ weakness i ' it i t of
ie that mee fa deere ‘ike ne

potential to cause loss
or harm

exploited to cause loss on

= It can be human-
initiated and computer-
initiated ones, natural
disasters.

E.g.: Internal employee can
be a threat to the
organisation

FOI 7 5 FCI IC Cr
--- page 16 ---
Vulnerabilities

The basic questions regarding to security that can arise in our mind are
» Why attackers attack our system?

» Is there any weak component present in our system?

» What are the precautions we need to take against attack?

Vulnerability is nothing but the weakness in the system. Weakness in the system may exploit an
attack. Weakness can be in coding, design or can be anything related to software development. Types
of vulnerabilities are

> Hardware Vulnerability
>» Software Vulnerability

> Data Vulnerability

Threats

» A threat is a potential for violation of security or a possible danger that might exploit
vulnerability.

» In other words a threat is a set of activity that has ability to cause harm. The threat

can be either generated by Human or Computer.

» Threat is purposely created by an attacker to attack on the system. In other words, an

exploitation of vulnerability is attack on the system.

» There are four kinds of threats possible: Interception, Interruption, Modification,

and Fabrication.

Types of Threats

» Threats - A threat is a potential for violation of security or a possible danger that might exploit

vulnerability.
Interruption Interception Fabrication
> ininterruption » Interception is > In modification, | > In fabrication,
the data may be keeping track of data is modified in attacker might
lost or traffic without some way. hide his own
unavailable due modification. In Receiver doesn’t identity and can
to some other words, some have any - send the data to
unauthorized unauthorized knowledge of this receiver from
system has gained modification some trusted
Party access to an asset. host.

eo e|je 5 @ ee

Classification of Attacks

» Passive — Passive attacks attempts to gain information from the system.
» Active — Active attacks affect the availability, integrity and authenticity of data.

» Insider - An attack originating from within the security perimeter of an organization
is an inside attack and usually is caused by an “insider” who gains access to more

resources than expected.

» Outsider - An outside attack originates from a source outside the security perimeter,

such as the Internet or a remote access connection.

FRR ICR 7 6 AC OH
--- page 17 ---
CO-2   b.   Demonstrate the process of generating keys for encryption and
SO-2   [10]
BL-3   decryption using RSA algorithm with an example.
Ans.
********** 17 **********

[Text in pictures on this page, read by OCR]
Classification of Attacks

Passive Active Outsider
> Footprinting > Denial of service > Planting keylogger > shoulder sniffing
> Sniffing > Firewall and IDS > Data theft > Dumpster Diving,
attack - :
> Eavesdropping > > Theft of physical > Social _
> Network Traffic Spoofing devices engineering
Analysis > Replay > Wiretapping
> Decryption of > Password based
weakly > Man-in-middle

encrypted traffic > Backdoor access

> DNS and ARP
poisoning

RSA

1. Choose two large prime numbers P and Q.
2. Calculate N = Px Q.

3- Select the public key (i.e. the encryption key) E such that it is not a factor of (P — 1) and
(Q-1).

4. Select the private key (i.e. the decryption key) D such that the following equation is true:
(Dx E) mod (P - 1) x (Q-1) =1

5- For encryption, calculate the cipher text CT from the plain text PT as follows: CT = PT= mod N
6. Send CT as the cipher text to the receiver.

7. For decryption, calculate the plain text PT from the cipher text CT as follows: PT = CT? mod N

RSA EXAMPLE

| | Select primes p=11, q=3.
WB n=pq=11*3-=33
BB (p-0(q-9 = 10 *2 = 20
Choose E=3
Check ged (E, (p-1)(q-1) ) = ged(3, 20) =1
(i.e. 3 and 20 have no common factors except 1)
HB compute D such that (D *E) mod (p-1)(q-1)=1
ie. compute D = e* mod (p-1)(q-1)= 3% mod 20
i.e. find D such that 20 divides 3D-1.
Simple testing (d = 1, 2, ...) gives d =7
Check: 3*7 - 1 = 20, which is divisible by (p-1)(q-1)

Wh public key = (E,n) = (3,33) Private key = (D,n) = (7,33).
--- page 18 ---
Q7   [20]
CO-2   a.   Describe the process of risk management with the help of its
SO-2   [10]
BL-2   components.
Ans.
Explanation of each subheading carries 1 mark.
CO-3   b.   Justify the use of SIEM in providing information security in any
SO-2   [10]
BL-5   organization.
********** 18 **********

[Text in pictures on this page, read by OCR]
RSA EXAMPLE

| Now say we want to encrypt the message m = 7,
CT = PT? modn
= 78 mod 33
= 343 mod 33 = 13.
Hence the cipher text c = 13.
Bit decrypt we compute
PT=CT? modn
= 137 mod 33 = 7.
m = 137 mod 33 = 13'3*3+ mod 33 = 133.13%.13 mod 33
= (138 mod 33).(438 mod 33).(13 mod 33) mod 33
= (2197 mod 33).(2197 mod 33).(13 mod 33) mod 33
= 19.19.13 mod 33 = 4693 mod 33
=7
--- page 19 ---
As. | Security Information and Event

Management

SIEM, which stands for Security Information and Event Management, is a
comprehensive approach to managing and analyzing security events within an
information technology (IT) environment.

SIEM systems collect and aggregate log data generated throughout the organization's
technology infrastructure, from host systems and applications to network and security
devices.

The primary goal of SIEM is to provide a centralized platform for real-time analysis of

security alerts and events, aiding in the detection of security incidents.

Security Information and Event
Management
Components of SIEM

» Data Collection - SIEM systems collect log and event data from various sources across the IT
environment, such as firewalls, intrusion detection/prevention systems, servers, endpoints, and

applications.

» Log Management - SIEM platforms store and manage log data in a centralized repository. Logs are
indexed and normalized for easy searching and analysis.

» Normalization and Correlation Engine - Normalization standardizes log data from different
sources, making it consistent and understandable. The correlation engine identifies patterns and

relationships between seemingly unrelated events to detect potential security incidents.

Security Information and Event
Management

Components of SIEM

» Alerting and Notification - SIEM systems generate alerts and notifications based on predefined
rules and correlation logic. Security analysts are notified of potential security incidents that require
investigation.

» Dashboards and Reporting - SIEM solutions provide dashboards and reporting tools to present
summarized and detailed information about security events, trends, and incidents. Customizable
dashboards help security teams monitor key metrics.

» Incident Response - SIEM facilitates incident response by providing tools for investigation,
forensics, and tracking the lifecycle of security incidents. It helps security teams understand the

nature and scope of incidents and take appropriate actions.

Security Information and Event
Management

Components of SIEM
» User and Entity Behavior Analytics (UEBA) - Some SIEM systems incorporate UEBA capabilities
to detect abnormal behavior patterns that may indicate insider threats or compromised accounts.

» Compliance Management - SIEM platforms assist in meeting regulatory compliance requirements
by providing reports and audit trails. They help organizations demonstrate adherence to security
policies and standards.

FRR ICR 7 QI OR
--- page 20 ---
Security Information and Event
Management

Features and Capabilities of SIEM

» Data Aggregation - Log and event data is collected from various sources, including security devices,

servers, applications, and network infrastructure.

Normalization - Raw log data is normalized to a consistent format, making it easier to analyze and

correlate events across different sources.

Correlation - Correlation engines analyze normalized data to identify patterns and relationships

between events. This helps in detecting complex security incidents.

» Alerting - Alerts are generated based on predefined rules and correlation logic. Security teams are

notified of potential security incidents.

Security Information and Event
Management

Features and Capabilities of SIEM

Dashboard — Data pulled from various database networks is then presented in a visually accessible dashboard.
Featuring charts that unveil patterns and prevent the oversight of critical events.

Investigation - Security analysts investigate alerts, using dashboards, reports, and analysis tools to understand the
context and severity of the incidents.

Incident Response - Based on the investigation, security teams initiate incident response procedures to contain,

eradicate, and recover from security incidents.

Automation and Reporting - SIEM platforms provide detailed reports and dashboards for ongoing monitoring,
compliance reporting, and management visibility. Automation for incident analysis and incident response

mechanisms.

Security Information and Event
Management

Advantage of SIEM
» Rapid Threat Identification
» Holistic Security View
> Versatile Use Case
» Scalability
» Threat Detection and Alerts

» Forensic Analysis Capability

Security Information and Event
Management

Disadvantage of SIEM
» Implementation Time
Cost Factors
Expertise Requirement
»   Rule-Based Analysis

» Misconfiguration Risks

FRI ICR DO) A RH
````
