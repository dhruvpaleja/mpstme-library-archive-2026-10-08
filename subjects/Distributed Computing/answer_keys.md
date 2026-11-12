# Distributed Computing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper a0b09f2431b3

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CS_7055/Distributed Computing/ANS_Distributed Computing(702CO0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / IV / V/Semester VI/Semester VIII/Semester X(Exam Year: 2025-2026)
Subject: Distributed Computing
Date: 12 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain any two real life examples of distributed systems in brief.
CO- 1;
SO- 1,2;   Any two example- 2.5 marks each   [5]
BL-2   Possible examples: Internet, Cloud computing systems
b.   State the differences between various transmission modes of stream-   [5]
based communication
◼ To capture timing aspects, there are different transmission
modes:
◼ In asynchronous transmission mode the data items (discrete) in
a stream are transmitted one after the other, but there are no
further timing constraints on when transmission of items should
take place.
CO-2 ;   For example, a file can be transferred as a data stream, but it is mostly
SO-1,2 ;   irrelevant exactly when the transfer of each item completes
BL-4   ◼ In synchronous transmission mode, there is a maximum end-to-
end delay defined for each unit in a data stream. Whether a data
unit is transferred much faster than the maximum tolerated delay
is not important.
◼ For example, a sensor may sample temperature at a certain rate
and pass it through a network to an operator.
◼ In isochronous transmission mode, it is necessary that data units
are transferred on time. This means that data transfer is subject
to a maximum and minimum end-to-end delay, also referred to
as bounded (delay) jitter.
********** 1 **********
--- page 2 ---
◼ Isochronous transmission mode is particularly interesting for
distributed multimedia systems, as it plays a crucial role in
representing audio and video.
c.   Define omission failure in distributed systems and apply the concept to a   [5]
real-life example, explaining how the system fails.
CO-3 ;
Crash failure- 1 marks
SO-1,2 ;
Real life example- 2 marks
BL-3
Explanation- 2 marks
Omission failure: a server fails to respond to incoming requests
d.   Explain how a directory node and a leaf node differ in structured   [5]
naming system?
Definition of leaf and director node: 02 marks
Structural differences: 03 marks
Leaf Node: Represents a named entity (file), has no outgoing edges, and
CO-4;
stores the address of the entity. Directory Node: Represents a directory,
SO-1,2;
has one or more outgoing edges, and stores a directory table mapping
BL-3
names to node identifiers.
Structural Differences:
Edges: Leaf node = none; Directory node = one or more outgoing edges.
Data Stored: Leaf node = entity address; Directory node = directory table.
Graph Role: Leaf node = terminal node; Directory node =
branching/intermediate node guiding traversal.
a.   Explain the benefits of application layering in centralized architectures
focusing on user interface, processing and data levels
Description of Layers (5 marks)
In centralized architectures, application layering divides the system
into distinct functional layers to improve organization and efficiency.
The three main layers are:
• User Interface (UI) Layer
Q2   • Processing (Application/Logic) Layer
• Data (Storage) Layer
CO-1;   [10]
SO-1,2;   This separation is known as separation of concerns.
BL-3   a) User Interface Layer
• Handles interaction with users
• Displays data and collects input
• Example: Web browser or mobile app interface
b) Processing Layer
• Contains business logic and computations
• Processes user requests and performs operations
********** 2 **********
--- page 3 ---
• Acts as a bridge between UI and data
c) Data Layer
• Responsible for data storage and management
• Uses databases to store and retrieve information
• Ensures data consistency and integrity
Benefits of Application Layering (5 marks)
a) Modularity
• Each layer performs a specific function
• Makes the system easier to design and understand
b) Maintainability
• Changes in one layer do not affect others
•   Easier debugging and updates
c) Reusability
• Components of one layer can be reused in other applications
d) Scalability
•   Individual layers can be optimized or scaled independently
e) Improved Security
•   Sensitive data is isolated in the data layer
• Access control can be enforced between layers
b.   What are the different types of faults? Analyze how redundancy helps
in achieving fault tolerance.
Types of faults- 3 marks
Redundancy- 7 marks
❑
transient,
Q2   ◼ Transient faults occur once and then disappear.
◼ For example, a bird flying through the beam of a
CO-3;   microwave transmitter may cause loss of bits.
[10]
SO-1,2;   ❑ intermittent,
◼ fault occurs, then vanishes of its own accord, then
BL-4   reappears, and so on.
◼ Eg., a loose connector
❑ Permanent.
◼ continues to exist until the faulty component is
replaced, e.g. Burnt-out chips, software bugs.
❑ The idea is to hide failures from other processes.
❑ The key technique for masking faults is to use redundancy.
❑ Three kinds are possible:
********** 3 **********
--- page 4 ---
❑ information redundancy,
◼ With information redundancy, extra bits are added
to allow recovery from garbled bits.
◼ For example, a Hamming code can be added to
transmitted data to recover from noise on the
transmission line.
❑ Time redundancy,
◼ an action is performed, and then. if need be, it is
performed again, e.g. redo of transaction.
❑ physical redundancy
◼ Extra equipment is added.
Triple Modular redundancy
a.   Define Distributed System and provide a detailed explanation of the
four core goals that a distributed system should meet.
Distributed System – 2 marks
Four goals- 2 marks each
Access remote resources
❑ Share resources
❑ Connecting users and resources
❑ Data sharing- Groupwares for Collaborative editing,
Q3   teleconferencing, video conferencing etc.
CO-;1   ❑ Problem: Security and an increase in unwanted   [10]
SO-:2
communication
BL-:2
❑ A system that is able to present its users and applications
as if it were only a single computer system is said to be
transparent.
❑ It is to hide the fact that its processes and resources are
physically distributed across multiple computers
❑ Different kinds of transparency exist for distributed
systems.
********** 4 **********
--- page 5 ---
Openness: System that offers services according to
standard rules that describe the syntax and semantics of
those services.
◼ In DS, Services are specified through interfaces described in an
Interface Definition Language(IDL).
◼ An interface definition allows an arbitrary process that needs a
certain interface to talk to another process that provides that
interface.
Scalability:
❑ Size scalability
◼ Can add more users and resources
❑ Geographical scalability
◼ Can spread across different geographical areas
❑ Administrative scalability
Can be manageable even if it spans many independent administrative
organizations
b.   Discuss the working of Reliable multicast services in Reliable Group
Communication.
Reliable multicast services: Such services guarantee that
messages are delivered to all members in a process group.
Multicasting is considered to be reliable when it can be
guaranteed that all nonfaulty group members receive the
message. Consider the case that a single sender wants to
multicast a message to multiple receivers. Assume that the
underlying communication system offers only unreliable
multicasting, meaning that a multicast message may be lost part
Q3
way and delivered to some, but not all, of the intended receivers.
CO-3;
[10]
SO-2;
BL-3
********** 5 **********
--- page 6 ---
A simple solution is shown in Fig. 8-9. The sending process assigns a
sequence number to each message it multicasts. We assume that
messages are received in the order they are sent. In this way, it is easy
for a receiver to detect it is missing a message. Each multicast message
is stored locally in a history buffer at the sender. Assuming the
receivers are known to the sender, the sender simply keeps the message
in its history buffer until each receiver has returned an
acknowledgment. If a receiver detects it is missing a message, it may
return a negative acknowledgment, requesting the sender for a
retransmission. Alternatively, the sender may automatically retransmit
the message when it has not received all acknowledgments within a
certain time.
a.   Explain Remote Method Invocation (RMI) architecture. How does it
differ   from   RPC?
RMI architecture with diagram- 6 marks
Java RMI (Remote Method Invocation) allows:
An object running in one JVM to invoke methods on an
object in another JVM (possibly on a different machine).
It supports object-oriented distributed communication
Q4   Key Components
CO-2;
• Remote Interface   [10]
SO-1,2;   • Remote Object (Implementation)
BL-2   • RMI Registry
• Client Application
• Stub (Proxy)
Step 1: Define Remote Interface
Step 2: Implement Remote Object
Step 3: Create and Start RMI Server
Step 4: Start RMI Registry
Step 5: Create Client Program
Step 6: Compile and Run
********** 6 **********
--- page 7 ---
Remote Machine
bind
RMI Server
Registry
skeleton
return   call   lookup
stub
RMI Client
Local Machine
RMI vs RPC- 4 marks
Feature   RPC   RMI
Remote Procedure
Full Form   Remote Method Invocation
Call
Programming
Procedural   Object-Oriented
Style
Language   Language-
Java-specific
Support   independent
Passes data   Passes objects (supports
Data Handling
(parameters)   serialization)
Communication Function-based   Object method-based
Complexity   Simpler   More complex
Platform
Cross-platform   Java platform dependent
Dependency
Better security (Java
Security   Limited
features)
Flexibility   Less flexible   More flexible
Example   C-based RPC   Java RMI
b.   A system has multiple processes requesting access to a critical section.
Apply Centralized algorithm to determine the order of execution. Show
message exchange using a diagram.
Q4
CO-3;   Algorithm- 7 marks
Diagram-3 marks   [10]
SO-1,2;   ◼ One process is elected as a coordinator
BL-3   ◼ A process that wants to access a shared resource sends a request
message to the coordinator mentioning the resource and seeking
permission.
◼ The coordinator sends that process a reply message, if no other
process is accessing that resource.
********** 7 **********
--- page 8 ---
◼ When the process receives a reply message from the coordinator,
it accesses the shared resource.
◼ After accessing the shared resource, the process sends a release
message to the coordinator and proceeds with its execution.
a.   Explain how vector logical clocks overcome the limitations of lamport’s
logical clocks? Using a suitable example, demonstrate how timestamps
are assigned and used for event ordering using Vector clocks
Advantages[ 4 marks]
Q5   Vector clocks rules: 3 marks
❑ Before   executing   an   event,   Pi   executes
CO-3;   VCi [ i ] ← VCi [i ] + 1.   [10]
SO-1,2;   ❑ When process Pi sends a message m to Pj, it sets m’s
(vector) timestamp ts (m) equal to VCi after having
BL-4   executed the previous step.
❑ Upon the receipt of a message m, process Pj adjusts its own
vector   by   setting
VCj [k ] ← max{VCj [k ], ts (m)[k ]} for each k, after which
it executes the first step and delivers the message to the
application.
Example- 3 marks
b.   What are flat names? Explain any two techniques used for resolving flat
names?
Flat names- 2 marks
Q5   ◼ Identifiers are random bit strings, which are unstructured or flat
names.
CO-4;   ◼ Property: it does not contain any information on how to locate   [10]
SO-2;   the access point of its associated entity.
BL-2   ◼ Flat names can be efficiently handled by machines
◼ – E.g., IP addresses, Ethernet addresses
Any two techniques. Each carries 4 marks.
❑ Simple Solutions
❑ Home-Based approaches
********** 8 **********
--- page 9 ---
❑ Distributed Hash Tables
❑ Hierarchical approaches
Q6   a.   Explain   stream-oriented   communication   and   discuss   how
CO-2;   synchronization of streams is achieved in multimedia systems.
[10]
SO-1,2;
stream-oriented communication- 4 marks
BL-3   synchronization – 6 marks
b.   Explain the need for physical clock synchronization in distributed
systems. Illustrate how synchronization is achieved using any one
physical clock synchronization technique.
Need- 4 marks
a) Event Ordering
• Helps in determining the correct sequence of events across
different nodes.
b) Coordination of Distributed Processes
Q6   • Required for tasks like transaction processing, logging, and
CO-3;   scheduling.
c) Consistency and Data Integrity   [10]
SO-1,2;
• Ensures operations occur in the correct temporal order.
BL-2   d) Real-Time Applications
•   Critical for systems like banking, stock trading, and
multimedia streaming.
e) Fault Detection
Any one technique- 6 marks
Cristain’s algorithm
NTP
Berkeley’s algorithm
a.   A   distributed e-commerce system uses message queues   for
communication. Analyze how persistent communication ensures
Q7
reliability in such a system
CO-2;
[10]
SO-1,2;   Persistent communication – 2marks
BL-4   Role of message queues- 3 marks
Ensures reliability- 5 marks
b.   A distributed system uses different naming concepts. With respect to it,
Q7   answer the following
a) Importance of names, identifiers and addresses [5 marks]
CO-4;
b) Explain any one name resolution technique used for structured   [10]
SO-1,2;   naming [5 marks]
BL-3   •   Identifier:
A unique, location-independent reference to an object. It remains
constant even if the object moves.
********** 9 **********
--- page 10 ---
• Address:
Represents the actual location of the object in the system. It may
change when the object moves.
• Key Difference:
Identifier = identity of object
Address = location of object
• Location Independence: Objects can move without changing their
identifier.
• Reduced Overhead: Only mapping between identifier and address
needs updating.
•   Scalability: Efficient for managing large and dynamic systems.
Flexibility: Supports migration, replication, and load balancing.
Iterative name resolution or recursive name resolution
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 18d1f052bb53

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/Distributed Computing/ANS_Distributed Computing(702CO0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / IV / V/Semester VI/Semester VIII/Semester X(Exam Year: 2025-2026)
Subject: Distributed Computing
Date: 12 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain any two real life examples of distributed systems in brief.
CO- 1;
SO- 1,2;   Any two example- 2.5 marks each   [5]
BL-2   Possible examples: Internet, Cloud computing systems
b.   State the differences between various transmission modes of stream-   [5]
based communication
◼ To capture timing aspects, there are different transmission
modes:
◼ In asynchronous transmission mode the data items (discrete) in
a stream are transmitted one after the other, but there are no
further timing constraints on when transmission of items should
take place.
CO-2 ;   For example, a file can be transferred as a data stream, but it is mostly
SO-1,2 ;   irrelevant exactly when the transfer of each item completes
BL-4   ◼ In synchronous transmission mode, there is a maximum end-to-
end delay defined for each unit in a data stream. Whether a data
unit is transferred much faster than the maximum tolerated delay
is not important.
◼ For example, a sensor may sample temperature at a certain rate
and pass it through a network to an operator.
◼ In isochronous transmission mode, it is necessary that data units
are transferred on time. This means that data transfer is subject
to a maximum and minimum end-to-end delay, also referred to
as bounded (delay) jitter.
********** 1 **********
--- page 2 ---
◼ Isochronous transmission mode is particularly interesting for
distributed multimedia systems, as it plays a crucial role in
representing audio and video.
c.   Define omission failure in distributed systems and apply the concept to a   [5]
real-life example, explaining how the system fails.
CO-3 ;
Crash failure- 1 marks
SO-1,2 ;
Real life example- 2 marks
BL-3
Explanation- 2 marks
Omission failure: a server fails to respond to incoming requests
d.   Explain how a directory node and a leaf node differ in structured   [5]
naming system?
Definition of leaf and director node: 02 marks
Structural differences: 03 marks
Leaf Node: Represents a named entity (file), has no outgoing edges, and
CO-4;
stores the address of the entity. Directory Node: Represents a directory,
SO-1,2;
has one or more outgoing edges, and stores a directory table mapping
BL-3
names to node identifiers.
Structural Differences:
Edges: Leaf node = none; Directory node = one or more outgoing edges.
Data Stored: Leaf node = entity address; Directory node = directory table.
Graph Role: Leaf node = terminal node; Directory node =
branching/intermediate node guiding traversal.
a.   Explain the benefits of application layering in centralized architectures
focusing on user interface, processing and data levels
Description of Layers (5 marks)
In centralized architectures, application layering divides the system
into distinct functional layers to improve organization and efficiency.
The three main layers are:
• User Interface (UI) Layer
Q2   • Processing (Application/Logic) Layer
• Data (Storage) Layer
CO-1;   [10]
SO-1,2;   This separation is known as separation of concerns.
BL-3   a) User Interface Layer
• Handles interaction with users
• Displays data and collects input
• Example: Web browser or mobile app interface
b) Processing Layer
• Contains business logic and computations
• Processes user requests and performs operations
********** 2 **********
--- page 3 ---
• Acts as a bridge between UI and data
c) Data Layer
• Responsible for data storage and management
• Uses databases to store and retrieve information
• Ensures data consistency and integrity
Benefits of Application Layering (5 marks)
a) Modularity
• Each layer performs a specific function
• Makes the system easier to design and understand
b) Maintainability
• Changes in one layer do not affect others
•   Easier debugging and updates
c) Reusability
• Components of one layer can be reused in other applications
d) Scalability
•   Individual layers can be optimized or scaled independently
e) Improved Security
•   Sensitive data is isolated in the data layer
• Access control can be enforced between layers
b.   What are the different types of faults? Analyze how redundancy helps
in achieving fault tolerance.
Types of faults- 3 marks
Redundancy- 7 marks
❑
transient,
Q2   ◼ Transient faults occur once and then disappear.
◼ For example, a bird flying through the beam of a
CO-3;   microwave transmitter may cause loss of bits.
[10]
SO-1,2;   ❑ intermittent,
◼ fault occurs, then vanishes of its own accord, then
BL-4   reappears, and so on.
◼ Eg., a loose connector
❑ Permanent.
◼ continues to exist until the faulty component is
replaced, e.g. Burnt-out chips, software bugs.
❑ The idea is to hide failures from other processes.
❑ The key technique for masking faults is to use redundancy.
❑ Three kinds are possible:
********** 3 **********
--- page 4 ---
❑ information redundancy,
◼ With information redundancy, extra bits are added
to allow recovery from garbled bits.
◼ For example, a Hamming code can be added to
transmitted data to recover from noise on the
transmission line.
❑ Time redundancy,
◼ an action is performed, and then. if need be, it is
performed again, e.g. redo of transaction.
❑ physical redundancy
◼ Extra equipment is added.
Triple Modular redundancy
a.   Define Distributed System and provide a detailed explanation of the
four core goals that a distributed system should meet.
Distributed System – 2 marks
Four goals- 2 marks each
Access remote resources
❑ Share resources
❑ Connecting users and resources
❑ Data sharing- Groupwares for Collaborative editing,
Q3   teleconferencing, video conferencing etc.
CO-;1   ❑ Problem: Security and an increase in unwanted   [10]
SO-:2
communication
BL-:2
❑ A system that is able to present its users and applications
as if it were only a single computer system is said to be
transparent.
❑ It is to hide the fact that its processes and resources are
physically distributed across multiple computers
❑ Different kinds of transparency exist for distributed
systems.
********** 4 **********
--- page 5 ---
Openness: System that offers services according to
standard rules that describe the syntax and semantics of
those services.
◼ In DS, Services are specified through interfaces described in an
Interface Definition Language(IDL).
◼ An interface definition allows an arbitrary process that needs a
certain interface to talk to another process that provides that
interface.
Scalability:
❑ Size scalability
◼ Can add more users and resources
❑ Geographical scalability
◼ Can spread across different geographical areas
❑ Administrative scalability
Can be manageable even if it spans many independent administrative
organizations
b.   Discuss the working of Reliable multicast services in Reliable Group
Communication.
Reliable multicast services: Such services guarantee that
messages are delivered to all members in a process group.
Multicasting is considered to be reliable when it can be
guaranteed that all nonfaulty group members receive the
message. Consider the case that a single sender wants to
multicast a message to multiple receivers. Assume that the
underlying communication system offers only unreliable
multicasting, meaning that a multicast message may be lost part
Q3
way and delivered to some, but not all, of the intended receivers.
CO-3;
[10]
SO-2;
BL-3
********** 5 **********
--- page 6 ---
A simple solution is shown in Fig. 8-9. The sending process assigns a
sequence number to each message it multicasts. We assume that
messages are received in the order they are sent. In this way, it is easy
for a receiver to detect it is missing a message. Each multicast message
is stored locally in a history buffer at the sender. Assuming the
receivers are known to the sender, the sender simply keeps the message
in its history buffer until each receiver has returned an
acknowledgment. If a receiver detects it is missing a message, it may
return a negative acknowledgment, requesting the sender for a
retransmission. Alternatively, the sender may automatically retransmit
the message when it has not received all acknowledgments within a
certain time.
a.   Explain Remote Method Invocation (RMI) architecture. How does it
differ   from   RPC?
RMI architecture with diagram- 6 marks
Java RMI (Remote Method Invocation) allows:
An object running in one JVM to invoke methods on an
object in another JVM (possibly on a different machine).
It supports object-oriented distributed communication
Q4   Key Components
CO-2;
• Remote Interface   [10]
SO-1,2;   • Remote Object (Implementation)
BL-2   • RMI Registry
• Client Application
• Stub (Proxy)
Step 1: Define Remote Interface
Step 2: Implement Remote Object
Step 3: Create and Start RMI Server
Step 4: Start RMI Registry
Step 5: Create Client Program
Step 6: Compile and Run
********** 6 **********
--- page 7 ---
Remote Machine
bind
RMI Server
Registry
skeleton
return   call   lookup
stub
RMI Client
Local Machine
RMI vs RPC- 4 marks
Feature   RPC   RMI
Remote Procedure
Full Form   Remote Method Invocation
Call
Programming
Procedural   Object-Oriented
Style
Language   Language-
Java-specific
Support   independent
Passes data   Passes objects (supports
Data Handling
(parameters)   serialization)
Communication Function-based   Object method-based
Complexity   Simpler   More complex
Platform
Cross-platform   Java platform dependent
Dependency
Better security (Java
Security   Limited
features)
Flexibility   Less flexible   More flexible
Example   C-based RPC   Java RMI
b.   A system has multiple processes requesting access to a critical section.
Apply Centralized algorithm to determine the order of execution. Show
message exchange using a diagram.
Q4
CO-3;   Algorithm- 7 marks
Diagram-3 marks   [10]
SO-1,2;   ◼ One process is elected as a coordinator
BL-3   ◼ A process that wants to access a shared resource sends a request
message to the coordinator mentioning the resource and seeking
permission.
◼ The coordinator sends that process a reply message, if no other
process is accessing that resource.
********** 7 **********
--- page 8 ---
◼ When the process receives a reply message from the coordinator,
it accesses the shared resource.
◼ After accessing the shared resource, the process sends a release
message to the coordinator and proceeds with its execution.
a.   Explain how vector logical clocks overcome the limitations of lamport’s
logical clocks? Using a suitable example, demonstrate how timestamps
are assigned and used for event ordering using Vector clocks
Advantages[ 4 marks]
Q5   Vector clocks rules: 3 marks
❑ Before   executing   an   event,   Pi   executes
CO-3;   VCi [ i ] ← VCi [i ] + 1.   [10]
SO-1,2;   ❑ When process Pi sends a message m to Pj, it sets m’s
(vector) timestamp ts (m) equal to VCi after having
BL-4   executed the previous step.
❑ Upon the receipt of a message m, process Pj adjusts its own
vector   by   setting
VCj [k ] ← max{VCj [k ], ts (m)[k ]} for each k, after which
it executes the first step and delivers the message to the
application.
Example- 3 marks
b.   What are flat names? Explain any two techniques used for resolving flat
names?
Flat names- 2 marks
Q5   ◼ Identifiers are random bit strings, which are unstructured or flat
names.
CO-4;   ◼ Property: it does not contain any information on how to locate   [10]
SO-2;   the access point of its associated entity.
BL-2   ◼ Flat names can be efficiently handled by machines
◼ – E.g., IP addresses, Ethernet addresses
Any two techniques. Each carries 4 marks.
❑ Simple Solutions
❑ Home-Based approaches
********** 8 **********
--- page 9 ---
❑ Distributed Hash Tables
❑ Hierarchical approaches
Q6   a.   Explain   stream-oriented   communication   and   discuss   how
CO-2;   synchronization of streams is achieved in multimedia systems.
[10]
SO-1,2;
stream-oriented communication- 4 marks
BL-3   synchronization – 6 marks
b.   Explain the need for physical clock synchronization in distributed
systems. Illustrate how synchronization is achieved using any one
physical clock synchronization technique.
Need- 4 marks
a) Event Ordering
• Helps in determining the correct sequence of events across
different nodes.
b) Coordination of Distributed Processes
Q6   • Required for tasks like transaction processing, logging, and
CO-3;   scheduling.
c) Consistency and Data Integrity   [10]
SO-1,2;
• Ensures operations occur in the correct temporal order.
BL-2   d) Real-Time Applications
•   Critical for systems like banking, stock trading, and
multimedia streaming.
e) Fault Detection
Any one technique- 6 marks
Cristain’s algorithm
NTP
Berkeley’s algorithm
a.   A   distributed e-commerce system uses message queues   for
communication. Analyze how persistent communication ensures
Q7
reliability in such a system
CO-2;
[10]
SO-1,2;   Persistent communication – 2marks
BL-4   Role of message queues- 3 marks
Ensures reliability- 5 marks
b.   A distributed system uses different naming concepts. With respect to it,
Q7   answer the following
a) Importance of names, identifiers and addresses [5 marks]
CO-4;
b) Explain any one name resolution technique used for structured   [10]
SO-1,2;   naming [5 marks]
BL-3   •   Identifier:
A unique, location-independent reference to an object. It remains
constant even if the object moves.
********** 9 **********
--- page 10 ---
• Address:
Represents the actual location of the object in the system. It may
change when the object moves.
• Key Difference:
Identifier = identity of object
Address = location of object
• Location Independence: Objects can move without changing their
identifier.
• Reduced Overhead: Only mapping between identifier and address
needs updating.
•   Scalability: Efficient for managing large and dynamic systems.
Flexibility: Supports migration, replication, and load balancing.
Iterative name resolution or recursive name resolution
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 3dbf543c2495

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/Distributed Computing/ANS_Distributed Computing(702CO0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / IV / V/Semester VI/Semester VIII/Semester X(Exam Year: 2025-2026)
Subject: Distributed Computing
Date: 12 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain any two real life examples of distributed systems in brief.
CO- 1;
SO- 1,2;   Any two example- 2.5 marks each   [5]
BL-2   Possible examples: Internet, Cloud computing systems
b.   State the differences between various transmission modes of stream-   [5]
based communication
◼ To capture timing aspects, there are different transmission
modes:
◼ In asynchronous transmission mode the data items (discrete) in
a stream are transmitted one after the other, but there are no
further timing constraints on when transmission of items should
take place.
CO-2 ;   For example, a file can be transferred as a data stream, but it is mostly
SO-1,2 ;   irrelevant exactly when the transfer of each item completes
BL-4   ◼ In synchronous transmission mode, there is a maximum end-to-
end delay defined for each unit in a data stream. Whether a data
unit is transferred much faster than the maximum tolerated delay
is not important.
◼ For example, a sensor may sample temperature at a certain rate
and pass it through a network to an operator.
◼ In isochronous transmission mode, it is necessary that data units
are transferred on time. This means that data transfer is subject
to a maximum and minimum end-to-end delay, also referred to
as bounded (delay) jitter.
********** 1 **********
--- page 2 ---
◼ Isochronous transmission mode is particularly interesting for
distributed multimedia systems, as it plays a crucial role in
representing audio and video.
c.   Define omission failure in distributed systems and apply the concept to a   [5]
real-life example, explaining how the system fails.
CO-3 ;
Crash failure- 1 marks
SO-1,2 ;
Real life example- 2 marks
BL-3
Explanation- 2 marks
Omission failure: a server fails to respond to incoming requests
d.   Explain how a directory node and a leaf node differ in structured   [5]
naming system?
Definition of leaf and director node: 02 marks
Structural differences: 03 marks
Leaf Node: Represents a named entity (file), has no outgoing edges, and
CO-4;
stores the address of the entity. Directory Node: Represents a directory,
SO-1,2;
has one or more outgoing edges, and stores a directory table mapping
BL-3
names to node identifiers.
Structural Differences:
Edges: Leaf node = none; Directory node = one or more outgoing edges.
Data Stored: Leaf node = entity address; Directory node = directory table.
Graph Role: Leaf node = terminal node; Directory node =
branching/intermediate node guiding traversal.
a.   Explain the benefits of application layering in centralized architectures
focusing on user interface, processing and data levels
Description of Layers (5 marks)
In centralized architectures, application layering divides the system
into distinct functional layers to improve organization and efficiency.
The three main layers are:
• User Interface (UI) Layer
Q2   • Processing (Application/Logic) Layer
• Data (Storage) Layer
CO-1;   [10]
SO-1,2;   This separation is known as separation of concerns.
BL-3   a) User Interface Layer
• Handles interaction with users
• Displays data and collects input
• Example: Web browser or mobile app interface
b) Processing Layer
• Contains business logic and computations
• Processes user requests and performs operations
********** 2 **********
--- page 3 ---
• Acts as a bridge between UI and data
c) Data Layer
• Responsible for data storage and management
• Uses databases to store and retrieve information
• Ensures data consistency and integrity
Benefits of Application Layering (5 marks)
a) Modularity
• Each layer performs a specific function
• Makes the system easier to design and understand
b) Maintainability
• Changes in one layer do not affect others
•   Easier debugging and updates
c) Reusability
• Components of one layer can be reused in other applications
d) Scalability
•   Individual layers can be optimized or scaled independently
e) Improved Security
•   Sensitive data is isolated in the data layer
• Access control can be enforced between layers
b.   What are the different types of faults? Analyze how redundancy helps
in achieving fault tolerance.
Types of faults- 3 marks
Redundancy- 7 marks
❑
transient,
Q2   ◼ Transient faults occur once and then disappear.
◼ For example, a bird flying through the beam of a
CO-3;   microwave transmitter may cause loss of bits.
[10]
SO-1,2;   ❑ intermittent,
◼ fault occurs, then vanishes of its own accord, then
BL-4   reappears, and so on.
◼ Eg., a loose connector
❑ Permanent.
◼ continues to exist until the faulty component is
replaced, e.g. Burnt-out chips, software bugs.
❑ The idea is to hide failures from other processes.
❑ The key technique for masking faults is to use redundancy.
❑ Three kinds are possible:
********** 3 **********
--- page 4 ---
❑ information redundancy,
◼ With information redundancy, extra bits are added
to allow recovery from garbled bits.
◼ For example, a Hamming code can be added to
transmitted data to recover from noise on the
transmission line.
❑ Time redundancy,
◼ an action is performed, and then. if need be, it is
performed again, e.g. redo of transaction.
❑ physical redundancy
◼ Extra equipment is added.
Triple Modular redundancy
a.   Define Distributed System and provide a detailed explanation of the
four core goals that a distributed system should meet.
Distributed System – 2 marks
Four goals- 2 marks each
Access remote resources
❑ Share resources
❑ Connecting users and resources
❑ Data sharing- Groupwares for Collaborative editing,
Q3   teleconferencing, video conferencing etc.
CO-;1   ❑ Problem: Security and an increase in unwanted   [10]
SO-:2
communication
BL-:2
❑ A system that is able to present its users and applications
as if it were only a single computer system is said to be
transparent.
❑ It is to hide the fact that its processes and resources are
physically distributed across multiple computers
❑ Different kinds of transparency exist for distributed
systems.
********** 4 **********
--- page 5 ---
Openness: System that offers services according to
standard rules that describe the syntax and semantics of
those services.
◼ In DS, Services are specified through interfaces described in an
Interface Definition Language(IDL).
◼ An interface definition allows an arbitrary process that needs a
certain interface to talk to another process that provides that
interface.
Scalability:
❑ Size scalability
◼ Can add more users and resources
❑ Geographical scalability
◼ Can spread across different geographical areas
❑ Administrative scalability
Can be manageable even if it spans many independent administrative
organizations
b.   Discuss the working of Reliable multicast services in Reliable Group
Communication.
Reliable multicast services: Such services guarantee that
messages are delivered to all members in a process group.
Multicasting is considered to be reliable when it can be
guaranteed that all nonfaulty group members receive the
message. Consider the case that a single sender wants to
multicast a message to multiple receivers. Assume that the
underlying communication system offers only unreliable
multicasting, meaning that a multicast message may be lost part
Q3
way and delivered to some, but not all, of the intended receivers.
CO-3;
[10]
SO-2;
BL-3
********** 5 **********
--- page 6 ---
A simple solution is shown in Fig. 8-9. The sending process assigns a
sequence number to each message it multicasts. We assume that
messages are received in the order they are sent. In this way, it is easy
for a receiver to detect it is missing a message. Each multicast message
is stored locally in a history buffer at the sender. Assuming the
receivers are known to the sender, the sender simply keeps the message
in its history buffer until each receiver has returned an
acknowledgment. If a receiver detects it is missing a message, it may
return a negative acknowledgment, requesting the sender for a
retransmission. Alternatively, the sender may automatically retransmit
the message when it has not received all acknowledgments within a
certain time.
a.   Explain Remote Method Invocation (RMI) architecture. How does it
differ   from   RPC?
RMI architecture with diagram- 6 marks
Java RMI (Remote Method Invocation) allows:
An object running in one JVM to invoke methods on an
object in another JVM (possibly on a different machine).
It supports object-oriented distributed communication
Q4   Key Components
CO-2;
• Remote Interface   [10]
SO-1,2;   • Remote Object (Implementation)
BL-2   • RMI Registry
• Client Application
• Stub (Proxy)
Step 1: Define Remote Interface
Step 2: Implement Remote Object
Step 3: Create and Start RMI Server
Step 4: Start RMI Registry
Step 5: Create Client Program
Step 6: Compile and Run
********** 6 **********
--- page 7 ---
Remote Machine
bind
RMI Server
Registry
skeleton
return   call   lookup
stub
RMI Client
Local Machine
RMI vs RPC- 4 marks
Feature   RPC   RMI
Remote Procedure
Full Form   Remote Method Invocation
Call
Programming
Procedural   Object-Oriented
Style
Language   Language-
Java-specific
Support   independent
Passes data   Passes objects (supports
Data Handling
(parameters)   serialization)
Communication Function-based   Object method-based
Complexity   Simpler   More complex
Platform
Cross-platform   Java platform dependent
Dependency
Better security (Java
Security   Limited
features)
Flexibility   Less flexible   More flexible
Example   C-based RPC   Java RMI
b.   A system has multiple processes requesting access to a critical section.
Apply Centralized algorithm to determine the order of execution. Show
message exchange using a diagram.
Q4
CO-3;   Algorithm- 7 marks
Diagram-3 marks   [10]
SO-1,2;   ◼ One process is elected as a coordinator
BL-3   ◼ A process that wants to access a shared resource sends a request
message to the coordinator mentioning the resource and seeking
permission.
◼ The coordinator sends that process a reply message, if no other
process is accessing that resource.
********** 7 **********
--- page 8 ---
◼ When the process receives a reply message from the coordinator,
it accesses the shared resource.
◼ After accessing the shared resource, the process sends a release
message to the coordinator and proceeds with its execution.
a.   Explain how vector logical clocks overcome the limitations of lamport’s
logical clocks? Using a suitable example, demonstrate how timestamps
are assigned and used for event ordering using Vector clocks
Advantages[ 4 marks]
Q5   Vector clocks rules: 3 marks
❑ Before   executing   an   event,   Pi   executes
CO-3;   VCi [ i ] ← VCi [i ] + 1.   [10]
SO-1,2;   ❑ When process Pi sends a message m to Pj, it sets m’s
(vector) timestamp ts (m) equal to VCi after having
BL-4   executed the previous step.
❑ Upon the receipt of a message m, process Pj adjusts its own
vector   by   setting
VCj [k ] ← max{VCj [k ], ts (m)[k ]} for each k, after which
it executes the first step and delivers the message to the
application.
Example- 3 marks
b.   What are flat names? Explain any two techniques used for resolving flat
names?
Flat names- 2 marks
Q5   ◼ Identifiers are random bit strings, which are unstructured or flat
names.
CO-4;   ◼ Property: it does not contain any information on how to locate   [10]
SO-2;   the access point of its associated entity.
BL-2   ◼ Flat names can be efficiently handled by machines
◼ – E.g., IP addresses, Ethernet addresses
Any two techniques. Each carries 4 marks.
❑ Simple Solutions
❑ Home-Based approaches
********** 8 **********
--- page 9 ---
❑ Distributed Hash Tables
❑ Hierarchical approaches
Q6   a.   Explain   stream-oriented   communication   and   discuss   how
CO-2;   synchronization of streams is achieved in multimedia systems.
[10]
SO-1,2;
stream-oriented communication- 4 marks
BL-3   synchronization – 6 marks
b.   Explain the need for physical clock synchronization in distributed
systems. Illustrate how synchronization is achieved using any one
physical clock synchronization technique.
Need- 4 marks
a) Event Ordering
• Helps in determining the correct sequence of events across
different nodes.
b) Coordination of Distributed Processes
Q6   • Required for tasks like transaction processing, logging, and
CO-3;   scheduling.
c) Consistency and Data Integrity   [10]
SO-1,2;
• Ensures operations occur in the correct temporal order.
BL-2   d) Real-Time Applications
•   Critical for systems like banking, stock trading, and
multimedia streaming.
e) Fault Detection
Any one technique- 6 marks
Cristain’s algorithm
NTP
Berkeley’s algorithm
a.   A   distributed e-commerce system uses message queues   for
communication. Analyze how persistent communication ensures
Q7
reliability in such a system
CO-2;
[10]
SO-1,2;   Persistent communication – 2marks
BL-4   Role of message queues- 3 marks
Ensures reliability- 5 marks
b.   A distributed system uses different naming concepts. With respect to it,
Q7   answer the following
a) Importance of names, identifiers and addresses [5 marks]
CO-4;
b) Explain any one name resolution technique used for structured   [10]
SO-1,2;   naming [5 marks]
BL-3   •   Identifier:
A unique, location-independent reference to an object. It remains
constant even if the object moves.
********** 9 **********
--- page 10 ---
• Address:
Represents the actual location of the object in the system. It may
change when the object moves.
• Key Difference:
Identifier = identity of object
Address = location of object
• Location Independence: Objects can move without changing their
identifier.
• Reduced Overhead: Only mapping between identifier and address
needs updating.
•   Scalability: Efficient for managing large and dynamic systems.
Flexibility: Supports migration, replication, and load balancing.
Iterative name resolution or recursive name resolution
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 562354ec674f

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AIML_7053/Distributed Computing/ANS_Distributed Computing(702CO0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & ML)/B. TECH (CSE - DS)
Year: III / IV/Semester V/Semester VII(Exam Year: 2025-2026)
Subject: Distributed Computing
Date: 03 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 01 is compulsory.
5. Out of the remaining questions, attempt any_4_questions.
6. In all_5_questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q 1
a. What is the role of a daemon in client-to-server binding?   [4 Marks]
Answer:
A daemon plays a crucial role in client-to-server binding when services use dynamically assigned ports instead of
fixed ones. In such cases, the client cannot directly know which port to contact for a specific service. The daemon
helps by:
1. Tracking Service Ports: It maintains a table of current port numbers for all local services running on the
server machine.   [1 Mark]
2. Listening on a Well-Known Port: The daemon itself listens on a predefined port, making it easy for clients to
locate it.   [1 Mark]
3. Providing Port Information: When a client wants to connect to a service, it first contacts the daemon. The
daemon responds with the correct port number of the desired service.[1 Mark]
4. Enabling Reliable Connections: This mechanism allows clients to reliably connect to services running on
dynamically allocated ports, ensuring flexibility and scalability in distributed systems
[1 Mark]
b. What is the role of a stub in Remote Method Invocation (RMI)?   [ 4 Marks]
Answer:
In Remote Method Invocation (RMI), a stub acts as a proxy for the remote object on the client side. It plays a crucial
role in enabling transparent communication between the client and the server in a distributed Java application.
********** 1 **********
--- page 2 ---
Here are the key functions of a stub:
1. Acts as a Gateway: The stub receives method calls from the client and forwards them to the remote object
on the server.   [1 Mark]
2. Handles Communication: It interacts with the Remote Reference Layer (RRL) to manage references and pass
requests across the network.   [1 Mark]
3. Encapsulates Method Calls: The stub packages the method name and parameters into a request and sends it
to the server via the transport layer.   [1 Mark]
4. Maintains Transparency: To the client, invoking a method on the stub feels like calling a local method, even
though the actual execution happens remotely.   [1 Mark]
c. What is the ‘happens-before’ relation in Lamport’s logical clocks? How is it used to assign timestamps to events?
[4 Marks]
The ‘happens-before’ relation (→) in Lamport’s logical clocks defines a partial ordering of events in a distributed
system. It is used to determine the causal relationship between events and is defined as follows:
[2 Marks]
1. Same Process: If event a occurs before event b in the same process, then a → b.
2. Message Passing: If a is the sending of a message and b is the receipt of that message, then a → b.
3. Transitivity: If a → b and b → c, then a → c.
[2 Marks]
Using this relation, Lamport assigns a logical timestamp C(a) to each event a such that:
   If a → b, then C(a) < C(b).
   Clocks must always move forward; corrections are made by adding positive values, never subtracting.
This ensures that all processes agree on the order of causally related events, even if their physical clocks are
unsynchronized. Events that are not causally related are considered concurrent, and no ordering is enforced between
them.
d. Define fault tolerance and explain its need in distributed systems.   [ 4 Marks]
Answer :
Fault tolerance is the ability of a distributed system to continue functioning correctly even when part of the system
fails. It ensures that the system can recover from partial failures without significantly affecting overall performance.
In distributed systems, fault tolerance is essential because:
1. Partial Failures Are Common: Unlike single-machine systems, distributed systems may experience failures in
one part while others continue to operate. Fault tolerance helps maintain service continuity.
2. Dependability Requirements: It supports key dependability attributes such as:
o   Availability – readiness for use at any moment.
o   Reliability – continuous operation over time.
********** 2 **********
--- page 3 ---
o   Safety – prevention of catastrophic outcomes during failures.
o   Maintainability – ease of repair and recovery.
3. Service Continuity: Even when faults occur, the system should still provide its services, possibly in a degraded
but acceptable manner.
4. Error and Fault Handling: Fault tolerance allows systems to detect, mask, and recover from errors caused by
faults (e.g., hardware issues, software bugs, or network problems)
e. Describe the Resource Description Framework (RDF) and its role in attribute-based naming.
[4 Marks]
1. Definition of RDF (1 mark):
The Resource Description Framework (RDF) is a model used to describe resources in distributed systems. It
represents data as triplets consisting of a subject, a predicate, and an object. For example, the triplet (Person, name,
Alice) describes a resource named "Person" whose name is "Alice".
2. Role in Attribute-Based Naming (1 mark):
RDF supports attribute-based naming by allowing entities to be described using structured metadata. Each
component of the triplet—subject, predicate, or object—can itself be a resource, enabling flexible and detailed
descriptions.
3. Use of URLs and Resource References (1 mark):
In RDF, references are typically URLs, which means resources can be linked and retrieved across distributed systems.
For instance, "Alice" may be a reference to a file, and the predicate may link to a textual description.
4. Querying and Centralized Storage (1 mark):
When RDF descriptions are stored centrally, applications can query the system to retrieve information based on
attributes. For example, querying for a person named "Alice" would return the associated resource, which can then
be fetched.
Q.2
a. Apply the concept of Remote Procedure Call (RPC) to implement a distributed file access system. Describe the
steps involved.   [10 Marks]
1. Introduction to RPC (1 mark)
Remote Procedure Call (RPC) allows a program to invoke a procedure on a remote machine as if it were local. It hides
the complexity of message passing and provides access transparency, making distributed programming simpler.
2. Objective of Distributed File Access System (1 mark)
The goal is to enable a client to access files stored on a remote server using RPC. The client sends a request (e.g., to
read a file), and the server processes it and returns the result, just like a local function call.
3. Components Involved (2 marks)
********** 3 **********
--- page 4 ---
   Client Stub: Acts as a proxy for the remote procedure. It packs parameters into a message and sends it to the
server.
   Server Stub: Unpacks the message and invokes the actual procedure on the server.
   Operating Systems: Handle message transmission between client and server.
   Procedure (e.g., read(fd, buf, nbytes)): Executes on the server and returns the result.
4. Steps in RPC-based File Access (4 marks)
1. Client Procedure Call:
The client calls a procedure like read(fd, buf, nbytes).
2. Client Stub Execution:
o Packs parameters into a message.
o Sends the message to the server via the local OS.
o Waits for a reply (blocks until response arrives).
3. Server Stub Execution:
o Receives the message.
o Unpacks parameters.
o   Calls the actual file access procedure (e.g., reads data from file).
4. Server Response:
o Packs the result (e.g., file data) into a message.
o Sends it back to the client stub.
5. Client Stub Completion:
o Unpacks the result.
o Returns control and data to the calling procedure.
5. Parameter Marshaling (1 mark)
Packing procedure parameters into a message is called marshaling. For example, in read(fd, buf, nbytes), the client
stub includes the procedure name and parameters in the message.
6. Transparency and Efficiency (1 mark)
To the client, the file access appears local. RPC ensures transparency, and asynchronous RPC can be used to improve
efficiency when no immediate result is needed.
b. Explain the concept of replication transparency. Why is it important in distributed systems? [10 Marks]
********** 4 **********
--- page 5 ---
1. Definition of Replication Transparency (2 marks)
Replication transparency refers to the ability of a distributed system to hide the existence of multiple copies
(replicas) of a resource from users and applications.
Users interact with a resource as if there is only one copy, even though the system may maintain several replicas for
performance and reliability.
2. Purpose of Replication (2 marks)
Replication is used to:
   Increase availability: If one replica fails, others can still serve the request.
 Improve performance: By placing replicas closer to users, access latency is reduced.
   Balance load: Requests can be distributed across multiple replicas.
3. Achieving Transparency (2 marks)
To achieve replication transparency:
   All replicas must have the same name.
 The system must ensure consistency among replicas.
   Users should not need to know which replica is being accessed.
4. Importance in Distributed Systems (2 marks)
Replication transparency is crucial because:
   It simplifies user experience by abstracting complexity.
   It supports fault tolerance and scalability.
   It enables continuous service even during failures or high demand.
5. Example Scenario (2 marks)
Consider a web server hosting a popular document:
 The document is replicated across multiple servers.
 A user accessing the document is unaware of which server serves it.
 The system automatically selects the best replica based on location or load.
Q.3
a. Explain Lamport’s logical clock algorithm. How does it help in ordering events in distributed systems?
Illustrate with an example.   [10 Marks]
1. Introduction to the Problem (1 mark)
********** 5 **********
--- page 6 ---
In distributed systems, each process runs on a separate machine with its own clock. Due to the absence of
a global clock and clock skew, it becomes difficult to determine the correct order of events across
processes. Lamport’s logical clocks provide a solution by assigning timestamps that help in maintaining a
consistent event ordering.
2. The Happens-Before Relation (2 marks)
Lamport introduced the happens-before (→) relation to define causal ordering:
   If event a occurs before b in the same process, then a → b.
   If a is the sending of a message and b is its receipt, then a → b.
   If a → b and b → c, then a → c (transitive).
Events that are not causally related are considered concurrent.
3. Lamport’s Logical Clock Rules (2 marks)
Each process Pi maintains a logical clock Ci:
   Before executing any event:
𝐶𝑖←𝐶𝑖+ 1
 When Pi sends a message m:
𝑡𝑠(𝑚) = 𝐶𝑖
 Upon receiving m, process Pj updates:
𝐶𝑗←max⁡(𝐶𝑗, 𝑡𝑠(𝑚))
Then:
𝐶𝑗←𝐶𝑗+ 1
This ensures that the receiver’s clock is always ahead of the sender’s timestamp, preserving causal order.
4. Example Illustration (3 marks)
Consider three processes P1, P2, and P3 with different clock rates:
 P1 sends message m1 at time 6 to P2.
 P2 receives it at time 16 and adjusts its clock.
   Later, P3 sends message m3 at time 60 to P2, but P2’s clock reads 56 — this is incorrect.
 Lamport’s algorithm corrects this by ensuring m3 arrives at 61, maintaining the correct order.
This prevents causality violations, such as a message appearing to arrive before it was sent.
5. Importance in Distributed Systems (2 marks)
Lamport’s logical clocks:
********** 6 **********
--- page 7 ---
   Provide a consistent ordering of events across distributed processes.
 Enable coordination in tasks like replicated database updates, mutual exclusion, and event logging.
 Are foundational for algorithms requiring total ordering, such as totally ordered multicast.
b. Explain the concept of process resilience in distributed systems. How do process groups contribute to
fault tolerance and ensure reliable service delivery despite failures? [10 Marks]
1. Introduction to Process Resilience (2 marks)
Process resilience refers to the ability of a distributed system to continue functioning correctly even when
one or more processes fail. This is achieved by designing systems that can tolerate partial failures, allowing
unaffected components to operate normally while faulty ones are repaired.
2. Role of Process Groups (2 marks)
A key strategy for achieving process resilience is the use of process groups. These are collections of
multiple identical processes that cooperate to provide the appearance of a single logical process. If one
process in the group fails, others can take over its responsibilities, ensuring that clients do not notice any
disruption.
3. Fault Tolerance through Redundancy (2 marks)
Process groups implement physical redundancy, which is one of the main techniques for fault masking. By
replicating processes, the system can tolerate the loss or malfunction of individual components. This
redundancy ensures that services remain available and reliable even during failures.
4. Reliable Communication and Atomic Multicasting (2 marks)
Reliable communication between processes in a group is essential. Techniques like atomic multicasting
ensure that messages are delivered consistently to all group members. This helps maintain synchronization
and consistency, which are critical for fault-tolerant behavior.
5. Example Scenario (2 marks)
Consider a distributed database system where updates are handled by a group of replicated processes. If
one process crashes, others in the group continue processing updates. Clients interacting with the system
experience no interruption, demonstrating process resilience.
Q.4
a. Discuss the structure and functioning of Distributed Hash Tables (DHTs) with reference to the Chord
system. How is key resolution achieved efficiently?
********** 7 **********
--- page 8 ---
1. Introduction to DHTs (2 marks)
Distributed Hash Tables (DHTs) are decentralized systems that provide a scalable and efficient way to store
and retrieve key-value pairs across a distributed network. Each node and data item is assigned a unique
identifier using a hash function, typically SHA-1 or similar.
2. Structure of Chord System (3 marks)
 Chord is a ring-based DHT where both nodes and keys are assigned m-bit identifiers (e.g., 160-bit).
 The identifier space is circular, ranging from 0 to 2^m - 1.
 Each node is responsible for keys that are equal to or follow its identifier in the ring.
 The node responsible for a key k is called successor(k).
 Each node maintains a finger table with up to m entries, where the i-th entry points to the node
that succeeds (n + 2^{i-1}) mod 2^m, helping in fast routing.
3. Key Resolution Mechanism (3 marks)
 To resolve a key k, a node forwards the request to the closest preceding node in its finger table.
   This process continues until the node responsible for k is found.
 The lookup requires O(log N) hops in a network of N nodes, making it highly efficient.
 Example: To resolve key 26 from node 1, the request may pass through nodes 1 → 18 → 20 → 21 →
28 (responsible for key 26).
4. Node Join and Leave (1 mark)
 When a node joins, it contacts an existing node to find its successor and updates its finger table.
 When a node leaves, its predecessor and successor update their pointers.
 Nodes periodically stabilize to maintain correct finger tables and ensure consistency.
5. Conclusion (1 mark)
Chord provides a robust, scalable, and fault-tolerant mechanism for key-based routing in distributed
systems. Its logarithmic lookup time and decentralized structure make it ideal for large-scale applications
like peer-to-peer networks.
b. Describe the concept of virtual synchrony in distributed systems.
How does it ensure consistency during group membership changes?
********** 8 **********
--- page 9 ---
1. Introduction to Virtual Synchrony (2 marks)
Virtual synchrony is a communication model used in fault-tolerant distributed systems to ensure that all
non-faulty processes in a group maintain a consistent view of the system, especially during group
membership changes (e.g., when a process joins, leaves, or crashes).
It ensures that messages are delivered in a consistent manner across all processes that share the same
group view.
2. Key Concepts (2 marks)
 A group view is the list of processes that are considered active members of a group at a given time.
 A view change occurs when the group membership is updated due to a join, leave, or failure.
 A message is associated with the view in which it was sent.
   Virtual synchrony ensures that either all members of a view receive a message or none do.
3. Ensuring Consistency During View Changes (4 marks)
 When a view change is detected (e.g., due to a crash), a view-change message is multicast to all
members.
   Before installing the new view, each process:
o Forwards any unstable messages (messages not yet delivered to all members) to the new
group.
o Marks those messages as stable once they are known to be received by all.
 Each process then sends a flush message indicating it is ready to install the new view.
 Once all flush messages are received, the new view is installed.
This mechanism ensures that no message from the previous view is lost, and all processes move to the
new view in a synchronized manner.
4. Example Scenario (1 mark)
If a process P3 crashes after sending a message to P2 and P4 but not to P1, virtual synchrony ensures that
none of the processes deliver that message, maintaining consistency across the group.
5. Conclusion (1 mark)
Virtual synchrony provides a robust framework for reliable multicast in dynamic distributed systems. It
ensures that all non-faulty processes agree on the set of messages delivered and the group membership,
thereby maintaining system consistency even in the presence of failures.
********** 9 **********
--- page 10 ---
5.
a. Explain the working of Remote Procedure Call (RPC) with the help of a diagram. How does it achieve
transparency in distributed systems?
Introduction (2 Marks)
Remote Procedure Call (RPC) is a communication mechanism used in distributed systems that allows a
program to invoke a procedure on a remote machine as if it were a local call. It abstracts the complexities
of network communication, providing access transparency to the programmer.
Working of RPC (5 Marks)
The RPC mechanism involves several components and steps:
1. Client Stub:
   Acts as a proxy for the actual remote procedure.
 Packs the procedure name and parameters into a message (marshalling).
 Sends the message to the server via the local operating system.
2. Server Stub:
 Waits for incoming messages.
 Unpacks the message (unmarshalling).
   Calls the actual server-side procedure with the unpacked parameters.
3. Server Procedure:
   Executes the requested operation.
 Returns the result to the server stub.
4. Return Path:
   Server stub packs the result into a message.
 Sends it back to the client stub.
   Client stub unpacks the result and returns it to the calling procedure.
Transparency in RPC (3 Marks)
RPC achieves transparency in the following ways:
 Access Transparency: The programmer writes code as if calling a local function. The underlying
message-passing is hidden.
   Location Transparency: The client does not need to know the physical location of the server.
 Communication Transparency: The complexities of network protocols, data serialization, and error
handling are abstracted away.
********** 10 **********
--- page 11 ---
This makes distributed programming simpler and more modular.
b. What is a superpeer-based peer-to-peer architecture in distributed systems?
1. Introduction (2 Marks)
A Superpeer-based Peer-to-Peer (P2P) architecture is a hybrid model that combines the benefits of both
centralized and decentralized systems. It addresses the inefficiencies of pure unstructured P2P networks by
introducing Superpeers—special nodes that act as intermediaries between regular peers and the broader
network.
2. Architecture and Working (4 Marks)
In this architecture:
 Regular Peers: These are standard nodes with limited capabilities. They connect to a Superpeer and
rely on it for communication and resource discovery.
 Superpeers:
o Act as local servers for a group of regular peers.
o Maintain indexes of data or resources shared by their connected peers.
o Handle search queries and route them efficiently.
o Communicate with other Superpeers to locate resources not found locally.
Working Mechanism:
1. A regular peer connects to a Superpeer.
2. When a peer wants to find a resource, it sends a query to its Superpeer.
3. The Superpeer checks its local index:
o   If the resource is found, it returns the result.
o   If not, it forwards the query to other Superpeers.
4. Once the resource is located, the Superpeer facilitates the connection between the requesting peer
and the peer holding the resource.
3. Diagram (Optional for Exams)
Regular Peer 1 Regular Peer 2
|   |
|
[Superpeer A]------[Superpeer B]
|   |
********** 11 **********
--- page 12 ---
Regular Peer 3 Regular Peer 4
   All communication from regular peers goes through their associated Superpeer.
 Superpeers form a structured overlay network among themselves.
4. Advantages (2 Marks)
 Improved Search Efficiency: Reduces flooding by using indexed searches.
   Scalability: Supports large networks by distributing load among Superpeers.
   Fault Tolerance: If a Superpeer fails, peers can reconnect to another Superpeer.
 Resource Coordination: Superpeers can manage and optimize resource sharing.
5. Use Cases and Examples (2 Marks)
 Kazaa and Skype are well-known applications that used Superpeer architectures.
   Suitable for collaborative content delivery networks (CDNs) and file-sharing systems where
efficient resource discovery is crucial.
6
a. Explain the Berkeley Algorithm for clock synchronization. How does it differ from Cristian’s method and
what are its advantages ?
1. Introduction to Berkeley Algorithm (2 marks)
The Berkeley Algorithm is an internal clock synchronization method used in distributed systems where no
machine has access to an accurate external time source like UTC. Instead of relying on a passive time
server, it uses an active time daemon that periodically polls all machines to synchronize their clocks.
2. Working of the Berkeley Algorithm (4 marks)
The synchronization process involves the following steps:
   Polling: The time daemon sends a request to all machines asking for their current clock values.
 Response Collection: Each machine replies with its local time.
 Average Calculation: The daemon calculates the average time from all responses, excluding any
outliers (e.g., faulty clocks).
   Clock Adjustment: The daemon sends each machine a message indicating how much to adjust its
clock—either to advance or slow down.
This process ensures that all machines agree on a common time, even if it doesn't match real-world time.
********** 12 **********
--- page 13 ---
3. Difference from Cristian’s Method (2 marks)
   Cristian’s Method: A client requests the current time from a time server that has access to an
accurate clock (e.g., via WWV or GPS). The client estimates the delay and adjusts its clock
accordingly.
 Berkeley Algorithm: No machine has an accurate external clock. The time daemon actively collects
times from all machines and computes an average, which becomes the new synchronized time.
4. Advantages of Berkeley Algorithm (2 marks)
 No need for external time source: Suitable for isolated systems without access to UTC.
   Fault tolerance: Can ignore faulty or outlier clocks during averaging.
   Uniformity: Ensures all machines agree on a common time, which is sufficient for internal
consistency.
b. Discuss the four key attributes of dependable systems: availability, reliability, safety, and maintainability.
How do these attributes contribute to fault tolerance?   [10 Marks]
1. Introduction to Dependable Systems (2 marks)
Dependable systems are designed to consistently deliver services that can be trusted. In distributed
systems, dependability is crucial due to the possibility of partial failures. Fault tolerance is a core aspect of
dependability, enabling systems to continue functioning correctly even when some components fail.
2. Availability (2 marks)
   Definition: Availability refers to the probability that a system is operational and ready to perform its
functions at any given moment.
   Contribution to Fault Tolerance: A highly available system ensures that services are accessible even
during failures. Techniques like redundancy and failover mechanisms help maintain availability.
3. Reliability (2 marks)
   Definition: Reliability is the ability of a system to operate continuously without failure over a
specified time interval.
   Contribution to Fault Tolerance: Reliable systems minimize interruptions and ensure consistent
service delivery. Fault-tolerant designs aim to reduce the frequency and impact of failures, thereby
enhancing reliability.
4. Safety (2 marks)
********** 13 **********
--- page 14 ---
   Definition: Safety ensures that even when a system fails, it does not cause catastrophic
consequences.
   Contribution to Fault Tolerance: In critical systems (e.g., nuclear control, aerospace), safety
mechanisms prevent harmful outcomes during faults. Fault-tolerant systems incorporate safeguards
to detect and mitigate unsafe conditions.
5. Maintainability (2 marks)
   Definition: Maintainability refers to how easily a system can be repaired after a failure.
   Contribution to Fault Tolerance: Systems with high maintainability can quickly recover from faults,
reducing downtime. Automated fault detection and recovery tools enhance maintainability and
overall fault tolerance.
7.
a. Explain the process of name resolution in a hierarchical naming system like DNS. How does recursive
lookup work in such systems?
1. Introduction to Name Resolution in DNS (2 marks)
In distributed systems, name resolution is the process of translating a human-readable name (like
ftp.cs.vu.nl) into an address that can be used to access the corresponding entity. DNS (Domain Name
System) is a hierarchical naming system that resolves structured names through a distributed set of name
servers.
2. Hierarchical Structure of DNS (2 marks)
DNS is organized into a hierarchical name space with multiple layers:
 Root layer: Contains top-level domains (e.g., .com, .org, .nl)
   Administrative layer: Represents domains managed by organizations (e.g., vu.nl)
 Managerial layer: Includes subdomains and hostnames (e.g., ftp.cs.vu.nl)
Each layer is managed by different name servers, and the resolution process traverses these layers to find
the final address.
3. Recursive Name Resolution Process (4 marks)
In recursive name resolution, the client sends the full domain name to a local name server, which then
takes responsibility for resolving the name completely. The process involves:
1. The local name server contacts the root name server to resolve the top-level domain (e.g., .nl).
2. The root server returns the address of the name server responsible for .nl.
********** 14 **********
--- page 15 ---
3. The local server then contacts the .nl server to resolve vu.nl, and receives the address of the vu.nl
server.
4. This continues recursively through cs.vu.nl, ftp.cs.vu.nl, and finally to the server hosting the
requested resource (e.g., index.html).
5. The final result is returned to the client by the local name server.
This process is illustrated in the presentation using a path like nl:[vu, cs, ftp, pub, globe, index.html].
4. Advantages and Drawbacks of Recursive Resolution (2 marks)
Advantages:
   Efficient caching: Intermediate results can be cached by name servers, reducing future lookup time.
 Reduced client-side complexity: The client delegates the entire resolution process.
Drawbacks:
 Higher load on name servers: Each server must handle full resolution requests.
 Performance demands: Recursive resolution requires more processing and coordination among
servers.
Due to these demands, recursive resolution is typically used in local or administrative layers, while
iterative resolution is preferred in the global layer.
b. How does gossip-based failure detection work in distributed systems?   [5 Marks]
Gossip-based failure detection is a decentralized method where each node in a distributed system
periodically shares its availability status with neighboring nodes. This information is then disseminated
throughout the network via gossip, allowing all nodes to gradually learn about the status of others.
 Each node announces its presence regularly, helping others track its activity.
   If a node stops receiving updates about another node, it may suspect a failure.
 To confirm, it can query other neighbors to check if they can still reach the suspected node.
   This method helps distinguish between node and network failures, improving accuracy.
 Over time, nodes build a local view of system health, enabling robust failure detection without
centralized control.
Gossip-based detection is scalable and fault-tolerant, making it suitable for large, dynamic distributed
systems.
********** 15 **********
--- page 16 ---
c. Discuss the concept of agreement in faulty systems. Why is it difficult to achieve consensus in
asynchronous systems with faulty processes?   [5 Marks]
In distributed systems, agreement refers to the ability of all non-faulty processes to reach a common
decision or consensus on a particular issue, such as electing a coordinator, committing a transaction, or
synchronizing actions.
Achieving agreement becomes challenging in the presence of faulty processes, especially when some may
behave arbitrarily (Byzantine faults). The goal is to ensure that all correct processes agree on the same
value, even if some processes are faulty or malicious.
[1 Marks]
In asynchronous systems, where:
 There is no bound on message delivery time,
 Message ordering is not guaranteed, and
 Processes may fail silently or behave unpredictably,
reaching consensus is particularly difficult. This is because it's impossible to distinguish between a slow
process and a failed one, leading to uncertainty. The FLP impossibility result (Fischer, Lynch, and Paterson)
proves that in a purely asynchronous system, no deterministic algorithm can guarantee consensus if even
one process fails.   [2 Marks]
To overcome this, systems often rely on:
 Timeouts (though they can cause false positives),
   Reliable message delivery (e.g., TCP),
 Or partial synchrony assumptions.
Thus, agreement in faulty, asynchronous systems is a fundamental and complex problem in distributed
computing.   [2 Marks]
********** 16 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper db23f5fb1e2b

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_IT_7041/Distributed Computing/ANS_Distributed Computing(702CO0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / IV / V/Semester VI/Semester VIII/Semester X(Exam Year: 2025-2026)
Subject: Distributed Computing
Date: 12 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain any two real life examples of distributed systems in brief.
CO- 1;
SO- 1,2;   Any two example- 2.5 marks each   [5]
BL-2   Possible examples: Internet, Cloud computing systems
b.   State the differences between various transmission modes of stream-   [5]
based communication
◼ To capture timing aspects, there are different transmission
modes:
◼ In asynchronous transmission mode the data items (discrete) in
a stream are transmitted one after the other, but there are no
further timing constraints on when transmission of items should
take place.
CO-2 ;   For example, a file can be transferred as a data stream, but it is mostly
SO-1,2 ;   irrelevant exactly when the transfer of each item completes
BL-4   ◼ In synchronous transmission mode, there is a maximum end-to-
end delay defined for each unit in a data stream. Whether a data
unit is transferred much faster than the maximum tolerated delay
is not important.
◼ For example, a sensor may sample temperature at a certain rate
and pass it through a network to an operator.
◼ In isochronous transmission mode, it is necessary that data units
are transferred on time. This means that data transfer is subject
to a maximum and minimum end-to-end delay, also referred to
as bounded (delay) jitter.
********** 1 **********
--- page 2 ---
◼ Isochronous transmission mode is particularly interesting for
distributed multimedia systems, as it plays a crucial role in
representing audio and video.
c.   Define omission failure in distributed systems and apply the concept to a   [5]
real-life example, explaining how the system fails.
CO-3 ;
Crash failure- 1 marks
SO-1,2 ;
Real life example- 2 marks
BL-3
Explanation- 2 marks
Omission failure: a server fails to respond to incoming requests
d.   Explain how a directory node and a leaf node differ in structured   [5]
naming system?
Definition of leaf and director node: 02 marks
Structural differences: 03 marks
Leaf Node: Represents a named entity (file), has no outgoing edges, and
CO-4;
stores the address of the entity. Directory Node: Represents a directory,
SO-1,2;
has one or more outgoing edges, and stores a directory table mapping
BL-3
names to node identifiers.
Structural Differences:
Edges: Leaf node = none; Directory node = one or more outgoing edges.
Data Stored: Leaf node = entity address; Directory node = directory table.
Graph Role: Leaf node = terminal node; Directory node =
branching/intermediate node guiding traversal.
a.   Explain the benefits of application layering in centralized architectures
focusing on user interface, processing and data levels
Description of Layers (5 marks)
In centralized architectures, application layering divides the system
into distinct functional layers to improve organization and efficiency.
The three main layers are:
• User Interface (UI) Layer
Q2   • Processing (Application/Logic) Layer
• Data (Storage) Layer
CO-1;   [10]
SO-1,2;   This separation is known as separation of concerns.
BL-3   a) User Interface Layer
• Handles interaction with users
• Displays data and collects input
• Example: Web browser or mobile app interface
b) Processing Layer
• Contains business logic and computations
• Processes user requests and performs operations
********** 2 **********
--- page 3 ---
• Acts as a bridge between UI and data
c) Data Layer
• Responsible for data storage and management
• Uses databases to store and retrieve information
• Ensures data consistency and integrity
Benefits of Application Layering (5 marks)
a) Modularity
• Each layer performs a specific function
• Makes the system easier to design and understand
b) Maintainability
• Changes in one layer do not affect others
•   Easier debugging and updates
c) Reusability
• Components of one layer can be reused in other applications
d) Scalability
•   Individual layers can be optimized or scaled independently
e) Improved Security
•   Sensitive data is isolated in the data layer
• Access control can be enforced between layers
b.   What are the different types of faults? Analyze how redundancy helps
in achieving fault tolerance.
Types of faults- 3 marks
Redundancy- 7 marks
❑
transient,
Q2   ◼ Transient faults occur once and then disappear.
◼ For example, a bird flying through the beam of a
CO-3;   microwave transmitter may cause loss of bits.
[10]
SO-1,2;   ❑ intermittent,
◼ fault occurs, then vanishes of its own accord, then
BL-4   reappears, and so on.
◼ Eg., a loose connector
❑ Permanent.
◼ continues to exist until the faulty component is
replaced, e.g. Burnt-out chips, software bugs.
❑ The idea is to hide failures from other processes.
❑ The key technique for masking faults is to use redundancy.
❑ Three kinds are possible:
********** 3 **********
--- page 4 ---
❑ information redundancy,
◼ With information redundancy, extra bits are added
to allow recovery from garbled bits.
◼ For example, a Hamming code can be added to
transmitted data to recover from noise on the
transmission line.
❑ Time redundancy,
◼ an action is performed, and then. if need be, it is
performed again, e.g. redo of transaction.
❑ physical redundancy
◼ Extra equipment is added.
Triple Modular redundancy
a.   Define Distributed System and provide a detailed explanation of the
four core goals that a distributed system should meet.
Distributed System – 2 marks
Four goals- 2 marks each
Access remote resources
❑ Share resources
❑ Connecting users and resources
❑ Data sharing- Groupwares for Collaborative editing,
Q3   teleconferencing, video conferencing etc.
CO-;1   ❑ Problem: Security and an increase in unwanted   [10]
SO-:2
communication
BL-:2
❑ A system that is able to present its users and applications
as if it were only a single computer system is said to be
transparent.
❑ It is to hide the fact that its processes and resources are
physically distributed across multiple computers
❑ Different kinds of transparency exist for distributed
systems.
********** 4 **********
--- page 5 ---
Openness: System that offers services according to
standard rules that describe the syntax and semantics of
those services.
◼ In DS, Services are specified through interfaces described in an
Interface Definition Language(IDL).
◼ An interface definition allows an arbitrary process that needs a
certain interface to talk to another process that provides that
interface.
Scalability:
❑ Size scalability
◼ Can add more users and resources
❑ Geographical scalability
◼ Can spread across different geographical areas
❑ Administrative scalability
Can be manageable even if it spans many independent administrative
organizations
b.   Discuss the working of Reliable multicast services in Reliable Group
Communication.
Reliable multicast services: Such services guarantee that
messages are delivered to all members in a process group.
Multicasting is considered to be reliable when it can be
guaranteed that all nonfaulty group members receive the
message. Consider the case that a single sender wants to
multicast a message to multiple receivers. Assume that the
underlying communication system offers only unreliable
multicasting, meaning that a multicast message may be lost part
Q3
way and delivered to some, but not all, of the intended receivers.
CO-3;
[10]
SO-2;
BL-3
********** 5 **********
--- page 6 ---
A simple solution is shown in Fig. 8-9. The sending process assigns a
sequence number to each message it multicasts. We assume that
messages are received in the order they are sent. In this way, it is easy
for a receiver to detect it is missing a message. Each multicast message
is stored locally in a history buffer at the sender. Assuming the
receivers are known to the sender, the sender simply keeps the message
in its history buffer until each receiver has returned an
acknowledgment. If a receiver detects it is missing a message, it may
return a negative acknowledgment, requesting the sender for a
retransmission. Alternatively, the sender may automatically retransmit
the message when it has not received all acknowledgments within a
certain time.
a.   Explain Remote Method Invocation (RMI) architecture. How does it
differ   from   RPC?
RMI architecture with diagram- 6 marks
Java RMI (Remote Method Invocation) allows:
An object running in one JVM to invoke methods on an
object in another JVM (possibly on a different machine).
It supports object-oriented distributed communication
Q4   Key Components
CO-2;
• Remote Interface   [10]
SO-1,2;   • Remote Object (Implementation)
BL-2   • RMI Registry
• Client Application
• Stub (Proxy)
Step 1: Define Remote Interface
Step 2: Implement Remote Object
Step 3: Create and Start RMI Server
Step 4: Start RMI Registry
Step 5: Create Client Program
Step 6: Compile and Run
********** 6 **********
--- page 7 ---
Remote Machine
bind
RMI Server
Registry
skeleton
return   call   lookup
stub
RMI Client
Local Machine
RMI vs RPC- 4 marks
Feature   RPC   RMI
Remote Procedure
Full Form   Remote Method Invocation
Call
Programming
Procedural   Object-Oriented
Style
Language   Language-
Java-specific
Support   independent
Passes data   Passes objects (supports
Data Handling
(parameters)   serialization)
Communication Function-based   Object method-based
Complexity   Simpler   More complex
Platform
Cross-platform   Java platform dependent
Dependency
Better security (Java
Security   Limited
features)
Flexibility   Less flexible   More flexible
Example   C-based RPC   Java RMI
b.   A system has multiple processes requesting access to a critical section.
Apply Centralized algorithm to determine the order of execution. Show
message exchange using a diagram.
Q4
CO-3;   Algorithm- 7 marks
Diagram-3 marks   [10]
SO-1,2;   ◼ One process is elected as a coordinator
BL-3   ◼ A process that wants to access a shared resource sends a request
message to the coordinator mentioning the resource and seeking
permission.
◼ The coordinator sends that process a reply message, if no other
process is accessing that resource.
********** 7 **********
--- page 8 ---
◼ When the process receives a reply message from the coordinator,
it accesses the shared resource.
◼ After accessing the shared resource, the process sends a release
message to the coordinator and proceeds with its execution.
a.   Explain how vector logical clocks overcome the limitations of lamport’s
logical clocks? Using a suitable example, demonstrate how timestamps
are assigned and used for event ordering using Vector clocks
Advantages[ 4 marks]
Q5   Vector clocks rules: 3 marks
❑ Before   executing   an   event,   Pi   executes
CO-3;   VCi [ i ] ← VCi [i ] + 1.   [10]
SO-1,2;   ❑ When process Pi sends a message m to Pj, it sets m’s
(vector) timestamp ts (m) equal to VCi after having
BL-4   executed the previous step.
❑ Upon the receipt of a message m, process Pj adjusts its own
vector   by   setting
VCj [k ] ← max{VCj [k ], ts (m)[k ]} for each k, after which
it executes the first step and delivers the message to the
application.
Example- 3 marks
b.   What are flat names? Explain any two techniques used for resolving flat
names?
Flat names- 2 marks
Q5   ◼ Identifiers are random bit strings, which are unstructured or flat
names.
CO-4;   ◼ Property: it does not contain any information on how to locate   [10]
SO-2;   the access point of its associated entity.
BL-2   ◼ Flat names can be efficiently handled by machines
◼ – E.g., IP addresses, Ethernet addresses
Any two techniques. Each carries 4 marks.
❑ Simple Solutions
❑ Home-Based approaches
********** 8 **********
--- page 9 ---
❑ Distributed Hash Tables
❑ Hierarchical approaches
Q6   a.   Explain   stream-oriented   communication   and   discuss   how
CO-2;   synchronization of streams is achieved in multimedia systems.
[10]
SO-1,2;
stream-oriented communication- 4 marks
BL-3   synchronization – 6 marks
b.   Explain the need for physical clock synchronization in distributed
systems. Illustrate how synchronization is achieved using any one
physical clock synchronization technique.
Need- 4 marks
a) Event Ordering
• Helps in determining the correct sequence of events across
different nodes.
b) Coordination of Distributed Processes
Q6   • Required for tasks like transaction processing, logging, and
CO-3;   scheduling.
c) Consistency and Data Integrity   [10]
SO-1,2;
• Ensures operations occur in the correct temporal order.
BL-2   d) Real-Time Applications
•   Critical for systems like banking, stock trading, and
multimedia streaming.
e) Fault Detection
Any one technique- 6 marks
Cristain’s algorithm
NTP
Berkeley’s algorithm
a.   A   distributed e-commerce system uses message queues   for
communication. Analyze how persistent communication ensures
Q7
reliability in such a system
CO-2;
[10]
SO-1,2;   Persistent communication – 2marks
BL-4   Role of message queues- 3 marks
Ensures reliability- 5 marks
b.   A distributed system uses different naming concepts. With respect to it,
Q7   answer the following
a) Importance of names, identifiers and addresses [5 marks]
CO-4;
b) Explain any one name resolution technique used for structured   [10]
SO-1,2;   naming [5 marks]
BL-3   •   Identifier:
A unique, location-independent reference to an object. It remains
constant even if the object moves.
********** 9 **********
--- page 10 ---
• Address:
Represents the actual location of the object in the system. It may
change when the object moves.
• Key Difference:
Identifier = identity of object
Address = location of object
• Location Independence: Objects can move without changing their
identifier.
• Reduced Overhead: Only mapping between identifier and address
needs updating.
•   Scalability: Efficient for managing large and dynamic systems.
Flexibility: Supports migration, replication, and load balancing.
Iterative name resolution or recursive name resolution
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper 942a31fb2d61

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_Computer_7032/Distributed Computing/ANS_Distributed Computing(702CO0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / IV / V/Semester VI/Semester VIII/Semester X(Exam Year: 2025-2026)
Subject: Distributed Computing
Date: 12 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Explain any two real life examples of distributed systems in brief.
CO- 1;
SO- 1,2;   Any two example- 2.5 marks each   [5]
BL-2   Possible examples: Internet, Cloud computing systems
b.   State the differences between various transmission modes of stream-   [5]
based communication
◼ To capture timing aspects, there are different transmission
modes:
◼ In asynchronous transmission mode the data items (discrete) in
a stream are transmitted one after the other, but there are no
further timing constraints on when transmission of items should
take place.
CO-2 ;   For example, a file can be transferred as a data stream, but it is mostly
SO-1,2 ;   irrelevant exactly when the transfer of each item completes
BL-4   ◼ In synchronous transmission mode, there is a maximum end-to-
end delay defined for each unit in a data stream. Whether a data
unit is transferred much faster than the maximum tolerated delay
is not important.
◼ For example, a sensor may sample temperature at a certain rate
and pass it through a network to an operator.
◼ In isochronous transmission mode, it is necessary that data units
are transferred on time. This means that data transfer is subject
to a maximum and minimum end-to-end delay, also referred to
as bounded (delay) jitter.
********** 1 **********
--- page 2 ---
◼ Isochronous transmission mode is particularly interesting for
distributed multimedia systems, as it plays a crucial role in
representing audio and video.
c.   Define omission failure in distributed systems and apply the concept to a   [5]
real-life example, explaining how the system fails.
CO-3 ;
Crash failure- 1 marks
SO-1,2 ;
Real life example- 2 marks
BL-3
Explanation- 2 marks
Omission failure: a server fails to respond to incoming requests
d.   Explain how a directory node and a leaf node differ in structured   [5]
naming system?
Definition of leaf and director node: 02 marks
Structural differences: 03 marks
Leaf Node: Represents a named entity (file), has no outgoing edges, and
CO-4;
stores the address of the entity. Directory Node: Represents a directory,
SO-1,2;
has one or more outgoing edges, and stores a directory table mapping
BL-3
names to node identifiers.
Structural Differences:
Edges: Leaf node = none; Directory node = one or more outgoing edges.
Data Stored: Leaf node = entity address; Directory node = directory table.
Graph Role: Leaf node = terminal node; Directory node =
branching/intermediate node guiding traversal.
a.   Explain the benefits of application layering in centralized architectures
focusing on user interface, processing and data levels
Description of Layers (5 marks)
In centralized architectures, application layering divides the system
into distinct functional layers to improve organization and efficiency.
The three main layers are:
• User Interface (UI) Layer
Q2   • Processing (Application/Logic) Layer
• Data (Storage) Layer
CO-1;   [10]
SO-1,2;   This separation is known as separation of concerns.
BL-3   a) User Interface Layer
• Handles interaction with users
• Displays data and collects input
• Example: Web browser or mobile app interface
b) Processing Layer
• Contains business logic and computations
• Processes user requests and performs operations
********** 2 **********
--- page 3 ---
• Acts as a bridge between UI and data
c) Data Layer
• Responsible for data storage and management
• Uses databases to store and retrieve information
• Ensures data consistency and integrity
Benefits of Application Layering (5 marks)
a) Modularity
• Each layer performs a specific function
• Makes the system easier to design and understand
b) Maintainability
• Changes in one layer do not affect others
•   Easier debugging and updates
c) Reusability
• Components of one layer can be reused in other applications
d) Scalability
•   Individual layers can be optimized or scaled independently
e) Improved Security
•   Sensitive data is isolated in the data layer
• Access control can be enforced between layers
b.   What are the different types of faults? Analyze how redundancy helps
in achieving fault tolerance.
Types of faults- 3 marks
Redundancy- 7 marks
❑
transient,
Q2   ◼ Transient faults occur once and then disappear.
◼ For example, a bird flying through the beam of a
CO-3;   microwave transmitter may cause loss of bits.
[10]
SO-1,2;   ❑ intermittent,
◼ fault occurs, then vanishes of its own accord, then
BL-4   reappears, and so on.
◼ Eg., a loose connector
❑ Permanent.
◼ continues to exist until the faulty component is
replaced, e.g. Burnt-out chips, software bugs.
❑ The idea is to hide failures from other processes.
❑ The key technique for masking faults is to use redundancy.
❑ Three kinds are possible:
********** 3 **********
--- page 4 ---
❑ information redundancy,
◼ With information redundancy, extra bits are added
to allow recovery from garbled bits.
◼ For example, a Hamming code can be added to
transmitted data to recover from noise on the
transmission line.
❑ Time redundancy,
◼ an action is performed, and then. if need be, it is
performed again, e.g. redo of transaction.
❑ physical redundancy
◼ Extra equipment is added.
Triple Modular redundancy
a.   Define Distributed System and provide a detailed explanation of the
four core goals that a distributed system should meet.
Distributed System – 2 marks
Four goals- 2 marks each
Access remote resources
❑ Share resources
❑ Connecting users and resources
❑ Data sharing- Groupwares for Collaborative editing,
Q3   teleconferencing, video conferencing etc.
CO-;1   ❑ Problem: Security and an increase in unwanted   [10]
SO-:2
communication
BL-:2
❑ A system that is able to present its users and applications
as if it were only a single computer system is said to be
transparent.
❑ It is to hide the fact that its processes and resources are
physically distributed across multiple computers
❑ Different kinds of transparency exist for distributed
systems.
********** 4 **********
--- page 5 ---
Openness: System that offers services according to
standard rules that describe the syntax and semantics of
those services.
◼ In DS, Services are specified through interfaces described in an
Interface Definition Language(IDL).
◼ An interface definition allows an arbitrary process that needs a
certain interface to talk to another process that provides that
interface.
Scalability:
❑ Size scalability
◼ Can add more users and resources
❑ Geographical scalability
◼ Can spread across different geographical areas
❑ Administrative scalability
Can be manageable even if it spans many independent administrative
organizations
b.   Discuss the working of Reliable multicast services in Reliable Group
Communication.
Reliable multicast services: Such services guarantee that
messages are delivered to all members in a process group.
Multicasting is considered to be reliable when it can be
guaranteed that all nonfaulty group members receive the
message. Consider the case that a single sender wants to
multicast a message to multiple receivers. Assume that the
underlying communication system offers only unreliable
multicasting, meaning that a multicast message may be lost part
Q3
way and delivered to some, but not all, of the intended receivers.
CO-3;
[10]
SO-2;
BL-3
********** 5 **********
--- page 6 ---
A simple solution is shown in Fig. 8-9. The sending process assigns a
sequence number to each message it multicasts. We assume that
messages are received in the order they are sent. In this way, it is easy
for a receiver to detect it is missing a message. Each multicast message
is stored locally in a history buffer at the sender. Assuming the
receivers are known to the sender, the sender simply keeps the message
in its history buffer until each receiver has returned an
acknowledgment. If a receiver detects it is missing a message, it may
return a negative acknowledgment, requesting the sender for a
retransmission. Alternatively, the sender may automatically retransmit
the message when it has not received all acknowledgments within a
certain time.
a.   Explain Remote Method Invocation (RMI) architecture. How does it
differ   from   RPC?
RMI architecture with diagram- 6 marks
Java RMI (Remote Method Invocation) allows:
An object running in one JVM to invoke methods on an
object in another JVM (possibly on a different machine).
It supports object-oriented distributed communication
Q4   Key Components
CO-2;
• Remote Interface   [10]
SO-1,2;   • Remote Object (Implementation)
BL-2   • RMI Registry
• Client Application
• Stub (Proxy)
Step 1: Define Remote Interface
Step 2: Implement Remote Object
Step 3: Create and Start RMI Server
Step 4: Start RMI Registry
Step 5: Create Client Program
Step 6: Compile and Run
********** 6 **********
--- page 7 ---
Remote Machine
bind
RMI Server
Registry
skeleton
return   call   lookup
stub
RMI Client
Local Machine
RMI vs RPC- 4 marks
Feature   RPC   RMI
Remote Procedure
Full Form   Remote Method Invocation
Call
Programming
Procedural   Object-Oriented
Style
Language   Language-
Java-specific
Support   independent
Passes data   Passes objects (supports
Data Handling
(parameters)   serialization)
Communication Function-based   Object method-based
Complexity   Simpler   More complex
Platform
Cross-platform   Java platform dependent
Dependency
Better security (Java
Security   Limited
features)
Flexibility   Less flexible   More flexible
Example   C-based RPC   Java RMI
b.   A system has multiple processes requesting access to a critical section.
Apply Centralized algorithm to determine the order of execution. Show
message exchange using a diagram.
Q4
CO-3;   Algorithm- 7 marks
Diagram-3 marks   [10]
SO-1,2;   ◼ One process is elected as a coordinator
BL-3   ◼ A process that wants to access a shared resource sends a request
message to the coordinator mentioning the resource and seeking
permission.
◼ The coordinator sends that process a reply message, if no other
process is accessing that resource.
********** 7 **********
--- page 8 ---
◼ When the process receives a reply message from the coordinator,
it accesses the shared resource.
◼ After accessing the shared resource, the process sends a release
message to the coordinator and proceeds with its execution.
a.   Explain how vector logical clocks overcome the limitations of lamport’s
logical clocks? Using a suitable example, demonstrate how timestamps
are assigned and used for event ordering using Vector clocks
Advantages[ 4 marks]
Q5   Vector clocks rules: 3 marks
❑ Before   executing   an   event,   Pi   executes
CO-3;   VCi [ i ] ← VCi [i ] + 1.   [10]
SO-1,2;   ❑ When process Pi sends a message m to Pj, it sets m’s
(vector) timestamp ts (m) equal to VCi after having
BL-4   executed the previous step.
❑ Upon the receipt of a message m, process Pj adjusts its own
vector   by   setting
VCj [k ] ← max{VCj [k ], ts (m)[k ]} for each k, after which
it executes the first step and delivers the message to the
application.
Example- 3 marks
b.   What are flat names? Explain any two techniques used for resolving flat
names?
Flat names- 2 marks
Q5   ◼ Identifiers are random bit strings, which are unstructured or flat
names.
CO-4;   ◼ Property: it does not contain any information on how to locate   [10]
SO-2;   the access point of its associated entity.
BL-2   ◼ Flat names can be efficiently handled by machines
◼ – E.g., IP addresses, Ethernet addresses
Any two techniques. Each carries 4 marks.
❑ Simple Solutions
❑ Home-Based approaches
********** 8 **********
--- page 9 ---
❑ Distributed Hash Tables
❑ Hierarchical approaches
Q6   a.   Explain   stream-oriented   communication   and   discuss   how
CO-2;   synchronization of streams is achieved in multimedia systems.
[10]
SO-1,2;
stream-oriented communication- 4 marks
BL-3   synchronization – 6 marks
b.   Explain the need for physical clock synchronization in distributed
systems. Illustrate how synchronization is achieved using any one
physical clock synchronization technique.
Need- 4 marks
a) Event Ordering
• Helps in determining the correct sequence of events across
different nodes.
b) Coordination of Distributed Processes
Q6   • Required for tasks like transaction processing, logging, and
CO-3;   scheduling.
c) Consistency and Data Integrity   [10]
SO-1,2;
• Ensures operations occur in the correct temporal order.
BL-2   d) Real-Time Applications
•   Critical for systems like banking, stock trading, and
multimedia streaming.
e) Fault Detection
Any one technique- 6 marks
Cristain’s algorithm
NTP
Berkeley’s algorithm
a.   A   distributed e-commerce system uses message queues   for
communication. Analyze how persistent communication ensures
Q7
reliability in such a system
CO-2;
[10]
SO-1,2;   Persistent communication – 2marks
BL-4   Role of message queues- 3 marks
Ensures reliability- 5 marks
b.   A distributed system uses different naming concepts. With respect to it,
Q7   answer the following
a) Importance of names, identifiers and addresses [5 marks]
CO-4;
b) Explain any one name resolution technique used for structured   [10]
SO-1,2;   naming [5 marks]
BL-3   •   Identifier:
A unique, location-independent reference to an object. It remains
constant even if the object moves.
********** 9 **********
--- page 10 ---
• Address:
Represents the actual location of the object in the system. It may
change when the object moves.
• Key Difference:
Identifier = identity of object
Address = location of object
• Location Independence: Objects can move without changing their
identifier.
• Reduced Overhead: Only mapping between identifier and address
needs updating.
•   Scalability: Efficient for managing large and dynamic systems.
Flexibility: Supports migration, replication, and load balancing.
Iterative name resolution or recursive name resolution
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 48ae4d88ab97

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CS_7055/Distributed Computing/ANS_Distributed Computing(702CO0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Jul 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / IV / V/Sem 10 Re-exam/Sem 6 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Distributed Computing
Date: 08 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   What is an open distributed system and what benefits does openness
provide?
open distributed system- 1 mark
benefits – 4 marks
An open distributed system is essentially a system that offer
components that can easily be used by or integrated into another system,
originated from elsewhere.
several key advantages that openness provides to a distributed system:
•   Interoperability: This is the ability of two implementations
from different vendors to work together by relying on each   [5]
other's services as defined by the common standards.
•   Portability: This ensures that an application developed for one
distributed system can be executed on another distributed system
that implements the same interfaces without requiring significant
modification.
•   Extensibility: An open system is easy to configure and
reconfigure. It allows for the easy addition of new components
or the replacement of existing ones (even from different
developers) without affecting the rest of the system.
•   Flexibility: Because the interfaces are standardized, parts of the
system can be updated or optimized independently, allowing the
system to evolve over time to meet new requirements.
b.   Differentiate between RPC and RMI.   [5]
Any five points – 1 mark each
********** 1 **********
--- page 2 ---
c.   What are the requirements of a dependable systems in distributed system?   [5]
What is dependable system- 1 mark
Four requirements- 1 mark each
Being fault tolerant is strongly related to what are called
dependable systems.
Dependability is a term that covers a number of useful
requirements for
distributed systems including the following:
1. Availability
2. Reliability
3. Safety
4. Maintainability
Availability is defined as the property that a system is ready to be used
immediately. Reliability refers to the property that a system can run
continuously without failure. Safety refers to the situation that when a
system temporarily fails to operate correctly, nothing catastrophic happens.
maintainability refers to how easy a failed system can be repaired.
d.   Explain how identifiers differ from addresses and analyze why identifiers [5]
are preferred in dynamic distributed systems?
Difference between Identifier and Address (2 Marks)
•   Identifier:
A unique, location-independent reference to an object. It remains
constant even if the object moves.
• Address:
Represents the actual location of the object in the system. It may
change when the object moves.
• Key Difference:
Identifier = identity of object
Address = location of object
Why Identifiers are Preferred (3 Marks)
********** 2 **********
--- page 3 ---
• Location Independence: Objects can move without changing their
identifier.
• Reduced Overhead: Only mapping between identifier and address
needs updating.
•   Scalability: Efficient for managing large and dynamic systems.
Flexibility: Supports migration, replication, and load balancing.
a.   Define Hybrid Architecture in distributed systems. Using BitTorrent as
an example, explain how combining centralized and decentralized
elements optimizes performance.
Hybrid architecture – 3 marks
BitTorrent example – 7 marks
•   In this type of architecture client-server solution is combined
with decentralize architecture.
• hybrid architecture is formed by edge-server systems.
• These systems are deployed on the Internet where servers are
placed "at the edge" of the network.
• This edge is formed by the boundary between enterprise
networks and the actual Internet, for example,
as provided by an Internet Service Provider (ISP).
It is a communication protocol for P2P file sharing.
It allows to download pieces of a file from many different users
simultaneously.
The basic idea is that when an end user is looking for a file ,he
Q2   downloads chunks of a file from other users   [10]
until the download chunks can be assembled together yielding the
complete file.
1. Client note: end user computer that initiate the search for a file
and eventually assemble the downloaded chunks into a full
file.
2. Web server and webpages: the user first access a global
directory to look up a specific file. The webpages provides a
link or references to the necessary meta data.
3. File server(. Torrent file.):A user downloads a small torrent file
from this file server. This file does not contain the actual
********** 3 **********
--- page 4 ---
content it contains a reference to the tracker and information
about the file chunk.
4. Trackers: specialised server that maintains an updated list of
nodes currently storing the file(or part of file)
5. Nodes:are other peer nodes. The client node connect to a
subside of this node to file chunk back and forth.
b.   Analyze the limitations of Reliable Multicasting and explain how it is
overcome in Non-hierarchical Feedback Control scheme.
Limitations- 3 marks
Non-hierarchical Feedback Control- 5 marks
Diagram – 2 marks
The main problem with the reliable multicast scheme just
described is that it cannot support large numbers of receivers
(WAN).
If there are N receivers, the sender must be prepared to accept at
least N acknowledgments.
With many receivers, the sender may be swamped with such
feedback messages, which is also referred to as a feedback
implosion.
Nonhierarchical Feedback Control
A popular model that has been applied to several wide-area
applications is feedback suppression. This scheme underlies the
Scalable Reliable Multicasting (SRM) protocol. First, in SRM,
receivers never acknowledge the successful delivery of a
Q2   multicast message, but instead, report only when they are
missing a message.   [10]
Only negative acknowledgments are returned as feedback.
Whenever a receiver notices that it missed a message, it
multicasts its feedback to the rest of the group.
Multicasting feedback allows another group member to suppress
its own feedback.
Basic idea: Let a process P suppress its own feedback when it
notices another process Q is already asking for a retransmission
Assumptions:
•   All receivers listen to a common feedback channel to which
feedback messages are submitted
•   Process P schedules its own feedback message randomly, and
suppresses it when observing another feedback message
********** 4 **********
--- page 5 ---
a.   Discuss the general Design Issues of Servers in Distributed Systems in
detail
Explanation of each issue- 2.5 marks
general design issues:
1. General organization
2. where clients contact a server
3. Whether and how a server can be interrupted
4. Whether or not the server is stateless
1. Types of Server
Iterative Server:
The server itself handles the request and, if necessary, returns
a response to the requesting client.
An iterative server can process only one request at a time
Concurrent Server:
A concurrent server does not handle the request itself, but
passes it to a separate thread or another process, after which
it immediately waits for the next incoming request.
A multithreaded server is an example of a concurrent server.
two or more clients can run at the same time on a machine
2. where clients contact a server
Each server listens to a specific end point
Q3   In all cases, clients send requests to an end point, also called a port,   [10]
at the machine where the server is running.
3. a server is whether and how a server can be interrupted.
Client ends the connection abruptly and connects again to
restart.
Server has a separate control end point to which thew client
sends out-of-band data.
4. Whether or not the server is stateless
A stateless server does not keep information on the state of its
clients, and can change its own state without having to inform any
client.
A Web server, for example, is stateless. It merely responds to
incoming HTTP requests, which can be either for uploading a file to
the server or (most often) for fetching a file. When the request has
been processed, the Web server forgets the client completely.
A stateful server generally maintains persistent information on its
clients.
This means that the information needs to be explicitly deleted by the
server.
A typical example is a file server that allows a client to keep a local
copy of a file, even for performing update operations. Such a server
would maintain a table containing (client, file) entries
Q3   b.   Explain following failure models with an example for each
a. Crash failure   [10]
b. Omission failure
********** 5 **********
--- page 6 ---
c. Timing
d. Response
e. Arbitrary
Each type of failure- 2 marks
A crash failure occurs when a server prematurely halts, but was
working
correctly until it stopped. An important aspect of crash failures is that
once the server has halted, nothing is heard from it anymore. A typical
example of a crash failure is an operating system that comes to a
grinding halt, and for which there is only one solution: reboot it.
An omission failure occurs when a server fails to respond to a request.
Several things might go wrong. In the case of a receive omission
failure, possibly the server never got the request in the first place. Note
that it may well be the case that the connection between a client and a
server has been correctly established, but that there was no thread
listening to incoming requests. Likewise, a send omission failure
happens when the server has done its work, but somehow fails in
sending a response. Such a failure may happen, for example, when a
send buffer overflows while the server was not prepared for such a
situation.
Other types of omission failures not related to communication may be
caused by software errors such as infinite loops or improper memory
management by which the server is said to "hang."
Timing failures occur when the response lies outside a specified real-
time interval. Providing data too soon may easily cause trouble for a
recipient if there is not enough buffer space to hold all the incoming
data. More common, however, is that a server responds too late, in
which case a performance failure is said to occur.
A serious type of failure is a response failure, by which the server's
response is simply incorrect. Two kinds of response failures may
happen. In the case of a value failure, a server simply provides the
wrong reply to a request. For example, a search engine that
systematically returns Web pages not related to any of the
search terms used. has failed. The other type of response failure is
known as a state transition failure. This kind of failure happens when
the server reacts unexpectedly to an incoming request. For example, if a
server receives a message it cannot recognize, a state transition failure
happens if no measures have been taken to handle such messages.
In particular, a faulty server may incorrectly take default actions it
should never have initiated.
The most serious are arbitrary failures, also known as Byzantine failures.
In effect, when arbitrary failures occur, clients should be prepared for the
worst. In particular, it may happen that a server is producing output it
should never have produced, but which cannot be detected as being
incorrect Worse yet a faulty server may even be maliciously working
together with other servers to produce intentionally wrong answers
Q4   a.   Describe socket programming primitives used in transient
communication? Also illustrate the pattern followed for connection-   [10]
oriented communication using sockets with the help of a diagram
********** 6 **********
--- page 7 ---
Transient communication refers to communication where:
• Both sender and receiver must be active at the same time
• Messages are not stored for later delivery
This is typically implemented using sockets
A socket is an endpoint for communication between two processes over
a network
It is identified by:
• IP Address
•   Port Number
Types of Sockets
• Stream Sockets (TCP) → reliable, connection-oriented
• Datagram Sockets (UDP) → connectionless, faster
b.   Explain the goal of Election algorithms? Illustrate the step-by-step
working of bully algorithm using suitable diagrams
goal of Election algorithms- 2 marks
Bully algorithm steps – 5 marks
Diagram- 3 marks
Q4
[10]
Several distributed algorithms require that there should be coordinator
process that perform some type of coordination needed for the smooth
running of other processes in the system
It assumes that each process has a unique number.
Election algorithms attempt to locate the process with the highest
process number and designate it as coordinator.
It also assumes that every process knows the process no. of every other
process.
********** 7 **********
--- page 8 ---
It then ensures that when an election starts, it concludes with all
processes agreeing on who the new coordinator is.
The Bully Algorithm:
When a process notices that the coordinator is no longer
responding, it initiates an election. A process P holds an
election as follows:
P sends an ELECTION message to all processes with higher
numbers.
If no one responds, P wins the election and becomes
coordinator.
If one of the higher-ups answers, it takes over. P’s job is
done.
a.   Multiple processes in a distributed system simultaneously request
access to a shared resource using the Ricart–Agrawala mutual exclusion
algorithm.
Apply the algorithm to determine how a process responds to incoming
REQUEST messages under different conditions.
It requires that there be total ordering of all events in the
Q5   system.
Algorithm works as follows:   [10]
When a process wants to access a shared resource, it builds a
message containing the name of the resource, its process
number and the current (logical) time.
It then sends the message to all other processes.
When a process receives a request message ,the action it
takes depends on its own state w.r.t. the resource in the
message
◼ Three different cases:
********** 8 **********
--- page 9 ---
❑ If the receiver is not accessing the resource and does not
want to access it, it sends back an OK message to the
sender.
❑ If the receiver already has access to the resource, it
simply does not reply. Instead, it queues the request.
❑ If the receiver wants to access the resource as well but
has not yet done so, it compares the timestamp of the
incoming message with the one contained in the message
that it has sent everyone. The lowest one wins.
(a) Two processes want to access a
shared resource at the same moment.
(b) Process 0 has the lowest timestamp, so it wins.
(c) When process 0 is done, it sends an OK also, so 2 can now go ahead.
b.   What is structured naming in distributed systems? Apply the concepts
of iterative and recursive name resolution to show how a DNS query
would be processed differently in each method.
Definition of structural naming: 02 marks
Definition of iterative and recursive name resolution: 02 marks
Step-by-step explanation of iterative DNS query: 03 marks
Step-by-step explanation of recursive DNS query: 03 marks
Structural naming in distributed systems organizes names in a
hierarchical structure, where each name consists of multiple components
arranged in levels (such as directory paths or domain names).
Iterative name resolution means the client contacts each DNS server in
Q5
sequence, receiving referrals until it reaches the authoritative server.   [10]
Recursive name resolution means the client sends the query to one DNS
server, which then performs the entire lookup on behalf of the client and
returns the final answer.
In iterative DNS resolution, the client first queries the local resolver,
which contacts the root server. The root returns a referral to the
appropriate TLD server. The resolver then queries the TLD server, which
provides the authoritative server address. Finally, the resolver queries the
authoritative server to obtain the IP address and sends it back to the client.
In recursive DNS resolution, the client sends a single query to the local DNS
resolver. The resolver contacts the root server, then the TLD server, and
finally the authoritative server. After collecting the IP address, the resolver
returns the final result to the client, completing the lookup.
Q6   a.   Describe the different RPC semantics in the presence of failures. Explain
how distributed systems handle such failures.   [10]
********** 9 **********
--- page 10 ---
Each class of failure- 2 marks
Five classes of PC failure can be identified:
1. The client is unable to locate the server.
2. The request message from the client to the server is lost.
3. The reply message from the server to the client is lost.
4. The server crashes after receiving a request.
5. The client crashes after sending a request
1. The client is unable to locate the server:
Causes:
Sever might be down
Version mismatch between client and server stubs
Possible solutions:
Raising exceptions
Relying on programming languages, transparency is compromised
2. The request message from the client to the server is lost
Easiest to handle
Use timers
Retransmission
Duplicate detection at the server end
3. The reply message from the server to the client is lost.
Timer at client: client is not sure whether the reply is lost or server is
slow
Idempotent operations
Sequence numbers in requests
-   Server refuses to perform a duplicate request
-   Server should maintain state of each client
A bit in the message to distinguish initial request from retransmissions
4. The server crashes after receiving a request
Servers can crash either before executing or after executing (before
sending reply)
Crash after execution needs to be reported to client
Crash before execution can be handled by retransmission
Client’s OS cannot distinguish between the two
Server crashes are dealt with by implementing one of three possible
implementation philosophies:
•   At least once semantics: a guarantee is given that the RPC
occurred at least once, but (also) possibly more that once.
•   At most once semantics: a guarantee is given that the RPC
occurred at most once, but possibly not at all.
• No semantics: nothing is guaranteed, and client and servers take
their chances!
5. The client crashes after sending a request
Can lead to orphans
Wastage of resources
Confusion or reboots
Solution 1: Extermination with logging
-   Maintain logs of RPC calls
-   Explicit termination of orphans
- Logging is expensive
Solution 2: Reincarnation
- Time is divided into epochs
********** 10 **********
--- page 11 ---
-   Broadcast epoch on client reboot
- Orphans are killed when a server receives new epoch
announcement
-   Solution 3: Gentler re-incarnation
-   - kill computations whose owners cannot be located
-   Solution 4: Expiration
-   - time window for completion with explicit extension
-   Client waits before rebooting
b.
What are the advantages of logical clocks over physical clocks?
Explain the rules used in advancing the time using Lamport’s logical
clocks with an example.
advantages of logical clocks over physical clocks [4 marks]
Rules – 4 marks
Example- 2 marks
Advantages:
No Need for Clock Synchronization
Ensures Correct Event Ordering
Captures Causality
Immune to Clock Drift and Skew
Rules:
◼ To implement Lamport’s Logical clock each process maintains a
Q6   local counter which is updated as follows:
◼ Before executing an event, Pi executes   [10]
Ci ← Ci + 1.
◼ When process Pi sends a message m to Pj, it sets m’s timestamp
ts (m) equal to Ci after having executed the previous step.
◼ Upon the receipt of a message m, process Pj adjusts its own local
counter as
Cj ← max{Cj , ts (m)}, after which it then executes the first step
and delivers the message to the application.
Example: this is just for reference.
Q7   a.   With reference to stream-oriented communication, answer the
[10]
following:
********** 11 **********
--- page 12 ---
i ) different transmission modes [5 marks]
ii) Quality of Service (QoS) mechanisms [5 marks]
◼ In asynchronous transmission mode the data items (discrete) in a
stream are transmitted one after the other, but there are no further
timing constraints on when transmission of items should take
place.
◼ For example, a file can be transferred as a data stream, but it is
mostly irrelevant exactly when the transfer of each item
completes.
In synchronous transmission mode, there is a maximum end-to-end
delay defined for each unit in a data stream. Whether a data unit is
transferred much faster than the maximum tolerated delay is not
important. For example, a sensor may sample temperature at a certain rate
and pass it through a network to an operator
◼ In isochronous transmission mode, it is necessary that data units
are transferred on time. This means that data transfer is subject to
a maximum and minimum end-to-end delay, also referred to as
bounded (delay) jitter.
Isochronous transmission mode is particularly interesting for distributed
multimedia systems, as it plays a crucial role in representing audio and
video
b.   A distributed system uses a home-based naming approach to track
Q7
mobile objects.   [10]
a) Explain the role of a home server in maintaining object location
information and the working of home based approach
********** 12 **********
--- page 13 ---
b) Analyze how frequent object migration affects lookup latency and
system performance in the home-based approach.
a) Role of Home Server (3 Marks)
• A home server maintains the permanent record (home location)
of an object.
•   It stores a mapping from object identifier → current location
(address).
•   Clients first contact the home server to locate the object.
• Even if the object moves, the home server keeps track of its
latest position.
• Ensures location transparency for users.
• Working [ 4 marks]
To support mobile entities
home location keeps track of the current location of an entity.
Each mobile host uses a fixed IP address.
All communication to that IP address is initially directed to the
mobile host’s home agent.
Whenever the mobile host moves to another n/w, it requests a
temporary address that it can use for communication (care-of
address) which is registered to home agent.
b) Impact of Frequent Migration (3 Marks)
1. Increased Lookup Latency
• Every lookup must go through the home server, adding extra
delay.
2. Home Server Bottleneck
• Frequent updates and queries overload the home server.
********** 13 **********
--- page 14 ---
3. Higher Update Overhead
• Each movement requires updating the home server, increasing
communication cost.
4. Reduced Performance
Frequent migrations lead to network congestion and slower response
times.
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper ecb6ebdb9282

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_Computer_7002/Distributed Computing/ANS_Distributed Computing(702CO0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Jul 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / IV / V/Sem 10 Re-exam/Sem 6 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Distributed Computing
Date: 08 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   What is an open distributed system and what benefits does openness
provide?
open distributed system- 1 mark
benefits – 4 marks
An open distributed system is essentially a system that offer
components that can easily be used by or integrated into another system,
originated from elsewhere.
several key advantages that openness provides to a distributed system:
•   Interoperability: This is the ability of two implementations
from different vendors to work together by relying on each   [5]
other's services as defined by the common standards.
•   Portability: This ensures that an application developed for one
distributed system can be executed on another distributed system
that implements the same interfaces without requiring significant
modification.
•   Extensibility: An open system is easy to configure and
reconfigure. It allows for the easy addition of new components
or the replacement of existing ones (even from different
developers) without affecting the rest of the system.
•   Flexibility: Because the interfaces are standardized, parts of the
system can be updated or optimized independently, allowing the
system to evolve over time to meet new requirements.
b.   Differentiate between RPC and RMI.   [5]
Any five points – 1 mark each
********** 1 **********
--- page 2 ---
c.   What are the requirements of a dependable systems in distributed system?   [5]
What is dependable system- 1 mark
Four requirements- 1 mark each
Being fault tolerant is strongly related to what are called
dependable systems.
Dependability is a term that covers a number of useful
requirements for
distributed systems including the following:
1. Availability
2. Reliability
3. Safety
4. Maintainability
Availability is defined as the property that a system is ready to be used
immediately. Reliability refers to the property that a system can run
continuously without failure. Safety refers to the situation that when a
system temporarily fails to operate correctly, nothing catastrophic happens.
maintainability refers to how easy a failed system can be repaired.
d.   Explain how identifiers differ from addresses and analyze why identifiers [5]
are preferred in dynamic distributed systems?
Difference between Identifier and Address (2 Marks)
•   Identifier:
A unique, location-independent reference to an object. It remains
constant even if the object moves.
• Address:
Represents the actual location of the object in the system. It may
change when the object moves.
• Key Difference:
Identifier = identity of object
Address = location of object
Why Identifiers are Preferred (3 Marks)
********** 2 **********
--- page 3 ---
• Location Independence: Objects can move without changing their
identifier.
• Reduced Overhead: Only mapping between identifier and address
needs updating.
•   Scalability: Efficient for managing large and dynamic systems.
Flexibility: Supports migration, replication, and load balancing.
a.   Define Hybrid Architecture in distributed systems. Using BitTorrent as
an example, explain how combining centralized and decentralized
elements optimizes performance.
Hybrid architecture – 3 marks
BitTorrent example – 7 marks
•   In this type of architecture client-server solution is combined
with decentralize architecture.
• hybrid architecture is formed by edge-server systems.
• These systems are deployed on the Internet where servers are
placed "at the edge" of the network.
• This edge is formed by the boundary between enterprise
networks and the actual Internet, for example,
as provided by an Internet Service Provider (ISP).
It is a communication protocol for P2P file sharing.
It allows to download pieces of a file from many different users
simultaneously.
The basic idea is that when an end user is looking for a file ,he
Q2   downloads chunks of a file from other users   [10]
until the download chunks can be assembled together yielding the
complete file.
1. Client note: end user computer that initiate the search for a file
and eventually assemble the downloaded chunks into a full
file.
2. Web server and webpages: the user first access a global
directory to look up a specific file. The webpages provides a
link or references to the necessary meta data.
3. File server(. Torrent file.):A user downloads a small torrent file
from this file server. This file does not contain the actual
********** 3 **********
--- page 4 ---
content it contains a reference to the tracker and information
about the file chunk.
4. Trackers: specialised server that maintains an updated list of
nodes currently storing the file(or part of file)
5. Nodes:are other peer nodes. The client node connect to a
subside of this node to file chunk back and forth.
b.   Analyze the limitations of Reliable Multicasting and explain how it is
overcome in Non-hierarchical Feedback Control scheme.
Limitations- 3 marks
Non-hierarchical Feedback Control- 5 marks
Diagram – 2 marks
The main problem with the reliable multicast scheme just
described is that it cannot support large numbers of receivers
(WAN).
If there are N receivers, the sender must be prepared to accept at
least N acknowledgments.
With many receivers, the sender may be swamped with such
feedback messages, which is also referred to as a feedback
implosion.
Nonhierarchical Feedback Control
A popular model that has been applied to several wide-area
applications is feedback suppression. This scheme underlies the
Scalable Reliable Multicasting (SRM) protocol. First, in SRM,
receivers never acknowledge the successful delivery of a
Q2   multicast message, but instead, report only when they are
missing a message.   [10]
Only negative acknowledgments are returned as feedback.
Whenever a receiver notices that it missed a message, it
multicasts its feedback to the rest of the group.
Multicasting feedback allows another group member to suppress
its own feedback.
Basic idea: Let a process P suppress its own feedback when it
notices another process Q is already asking for a retransmission
Assumptions:
•   All receivers listen to a common feedback channel to which
feedback messages are submitted
•   Process P schedules its own feedback message randomly, and
suppresses it when observing another feedback message
********** 4 **********
--- page 5 ---
a.   Discuss the general Design Issues of Servers in Distributed Systems in
detail
Explanation of each issue- 2.5 marks
general design issues:
1. General organization
2. where clients contact a server
3. Whether and how a server can be interrupted
4. Whether or not the server is stateless
1. Types of Server
Iterative Server:
The server itself handles the request and, if necessary, returns
a response to the requesting client.
An iterative server can process only one request at a time
Concurrent Server:
A concurrent server does not handle the request itself, but
passes it to a separate thread or another process, after which
it immediately waits for the next incoming request.
A multithreaded server is an example of a concurrent server.
two or more clients can run at the same time on a machine
2. where clients contact a server
Each server listens to a specific end point
Q3   In all cases, clients send requests to an end point, also called a port,   [10]
at the machine where the server is running.
3. a server is whether and how a server can be interrupted.
Client ends the connection abruptly and connects again to
restart.
Server has a separate control end point to which thew client
sends out-of-band data.
4. Whether or not the server is stateless
A stateless server does not keep information on the state of its
clients, and can change its own state without having to inform any
client.
A Web server, for example, is stateless. It merely responds to
incoming HTTP requests, which can be either for uploading a file to
the server or (most often) for fetching a file. When the request has
been processed, the Web server forgets the client completely.
A stateful server generally maintains persistent information on its
clients.
This means that the information needs to be explicitly deleted by the
server.
A typical example is a file server that allows a client to keep a local
copy of a file, even for performing update operations. Such a server
would maintain a table containing (client, file) entries
Q3   b.   Explain following failure models with an example for each
a. Crash failure   [10]
b. Omission failure
********** 5 **********
--- page 6 ---
c. Timing
d. Response
e. Arbitrary
Each type of failure- 2 marks
A crash failure occurs when a server prematurely halts, but was
working
correctly until it stopped. An important aspect of crash failures is that
once the server has halted, nothing is heard from it anymore. A typical
example of a crash failure is an operating system that comes to a
grinding halt, and for which there is only one solution: reboot it.
An omission failure occurs when a server fails to respond to a request.
Several things might go wrong. In the case of a receive omission
failure, possibly the server never got the request in the first place. Note
that it may well be the case that the connection between a client and a
server has been correctly established, but that there was no thread
listening to incoming requests. Likewise, a send omission failure
happens when the server has done its work, but somehow fails in
sending a response. Such a failure may happen, for example, when a
send buffer overflows while the server was not prepared for such a
situation.
Other types of omission failures not related to communication may be
caused by software errors such as infinite loops or improper memory
management by which the server is said to "hang."
Timing failures occur when the response lies outside a specified real-
time interval. Providing data too soon may easily cause trouble for a
recipient if there is not enough buffer space to hold all the incoming
data. More common, however, is that a server responds too late, in
which case a performance failure is said to occur.
A serious type of failure is a response failure, by which the server's
response is simply incorrect. Two kinds of response failures may
happen. In the case of a value failure, a server simply provides the
wrong reply to a request. For example, a search engine that
systematically returns Web pages not related to any of the
search terms used. has failed. The other type of response failure is
known as a state transition failure. This kind of failure happens when
the server reacts unexpectedly to an incoming request. For example, if a
server receives a message it cannot recognize, a state transition failure
happens if no measures have been taken to handle such messages.
In particular, a faulty server may incorrectly take default actions it
should never have initiated.
The most serious are arbitrary failures, also known as Byzantine failures.
In effect, when arbitrary failures occur, clients should be prepared for the
worst. In particular, it may happen that a server is producing output it
should never have produced, but which cannot be detected as being
incorrect Worse yet a faulty server may even be maliciously working
together with other servers to produce intentionally wrong answers
Q4   a.   Describe socket programming primitives used in transient
communication? Also illustrate the pattern followed for connection-   [10]
oriented communication using sockets with the help of a diagram
********** 6 **********
--- page 7 ---
Transient communication refers to communication where:
• Both sender and receiver must be active at the same time
• Messages are not stored for later delivery
This is typically implemented using sockets
A socket is an endpoint for communication between two processes over
a network
It is identified by:
• IP Address
•   Port Number
Types of Sockets
• Stream Sockets (TCP) → reliable, connection-oriented
• Datagram Sockets (UDP) → connectionless, faster
b.   Explain the goal of Election algorithms? Illustrate the step-by-step
working of bully algorithm using suitable diagrams
goal of Election algorithms- 2 marks
Bully algorithm steps – 5 marks
Diagram- 3 marks
Q4
[10]
Several distributed algorithms require that there should be coordinator
process that perform some type of coordination needed for the smooth
running of other processes in the system
It assumes that each process has a unique number.
Election algorithms attempt to locate the process with the highest
process number and designate it as coordinator.
It also assumes that every process knows the process no. of every other
process.
********** 7 **********
--- page 8 ---
It then ensures that when an election starts, it concludes with all
processes agreeing on who the new coordinator is.
The Bully Algorithm:
When a process notices that the coordinator is no longer
responding, it initiates an election. A process P holds an
election as follows:
P sends an ELECTION message to all processes with higher
numbers.
If no one responds, P wins the election and becomes
coordinator.
If one of the higher-ups answers, it takes over. P’s job is
done.
a.   Multiple processes in a distributed system simultaneously request
access to a shared resource using the Ricart–Agrawala mutual exclusion
algorithm.
Apply the algorithm to determine how a process responds to incoming
REQUEST messages under different conditions.
It requires that there be total ordering of all events in the
Q5   system.
Algorithm works as follows:   [10]
When a process wants to access a shared resource, it builds a
message containing the name of the resource, its process
number and the current (logical) time.
It then sends the message to all other processes.
When a process receives a request message ,the action it
takes depends on its own state w.r.t. the resource in the
message
◼ Three different cases:
********** 8 **********
--- page 9 ---
❑ If the receiver is not accessing the resource and does not
want to access it, it sends back an OK message to the
sender.
❑ If the receiver already has access to the resource, it
simply does not reply. Instead, it queues the request.
❑ If the receiver wants to access the resource as well but
has not yet done so, it compares the timestamp of the
incoming message with the one contained in the message
that it has sent everyone. The lowest one wins.
(a) Two processes want to access a
shared resource at the same moment.
(b) Process 0 has the lowest timestamp, so it wins.
(c) When process 0 is done, it sends an OK also, so 2 can now go ahead.
b.   What is structured naming in distributed systems? Apply the concepts
of iterative and recursive name resolution to show how a DNS query
would be processed differently in each method.
Definition of structural naming: 02 marks
Definition of iterative and recursive name resolution: 02 marks
Step-by-step explanation of iterative DNS query: 03 marks
Step-by-step explanation of recursive DNS query: 03 marks
Structural naming in distributed systems organizes names in a
hierarchical structure, where each name consists of multiple components
arranged in levels (such as directory paths or domain names).
Iterative name resolution means the client contacts each DNS server in
Q5
sequence, receiving referrals until it reaches the authoritative server.   [10]
Recursive name resolution means the client sends the query to one DNS
server, which then performs the entire lookup on behalf of the client and
returns the final answer.
In iterative DNS resolution, the client first queries the local resolver,
which contacts the root server. The root returns a referral to the
appropriate TLD server. The resolver then queries the TLD server, which
provides the authoritative server address. Finally, the resolver queries the
authoritative server to obtain the IP address and sends it back to the client.
In recursive DNS resolution, the client sends a single query to the local DNS
resolver. The resolver contacts the root server, then the TLD server, and
finally the authoritative server. After collecting the IP address, the resolver
returns the final result to the client, completing the lookup.
Q6   a.   Describe the different RPC semantics in the presence of failures. Explain
how distributed systems handle such failures.   [10]
********** 9 **********
--- page 10 ---
Each class of failure- 2 marks
Five classes of PC failure can be identified:
1. The client is unable to locate the server.
2. The request message from the client to the server is lost.
3. The reply message from the server to the client is lost.
4. The server crashes after receiving a request.
5. The client crashes after sending a request
1. The client is unable to locate the server:
Causes:
Sever might be down
Version mismatch between client and server stubs
Possible solutions:
Raising exceptions
Relying on programming languages, transparency is compromised
2. The request message from the client to the server is lost
Easiest to handle
Use timers
Retransmission
Duplicate detection at the server end
3. The reply message from the server to the client is lost.
Timer at client: client is not sure whether the reply is lost or server is
slow
Idempotent operations
Sequence numbers in requests
-   Server refuses to perform a duplicate request
-   Server should maintain state of each client
A bit in the message to distinguish initial request from retransmissions
4. The server crashes after receiving a request
Servers can crash either before executing or after executing (before
sending reply)
Crash after execution needs to be reported to client
Crash before execution can be handled by retransmission
Client’s OS cannot distinguish between the two
Server crashes are dealt with by implementing one of three possible
implementation philosophies:
•   At least once semantics: a guarantee is given that the RPC
occurred at least once, but (also) possibly more that once.
•   At most once semantics: a guarantee is given that the RPC
occurred at most once, but possibly not at all.
• No semantics: nothing is guaranteed, and client and servers take
their chances!
5. The client crashes after sending a request
Can lead to orphans
Wastage of resources
Confusion or reboots
Solution 1: Extermination with logging
-   Maintain logs of RPC calls
-   Explicit termination of orphans
- Logging is expensive
Solution 2: Reincarnation
- Time is divided into epochs
********** 10 **********
--- page 11 ---
-   Broadcast epoch on client reboot
- Orphans are killed when a server receives new epoch
announcement
-   Solution 3: Gentler re-incarnation
-   - kill computations whose owners cannot be located
-   Solution 4: Expiration
-   - time window for completion with explicit extension
-   Client waits before rebooting
b.
What are the advantages of logical clocks over physical clocks?
Explain the rules used in advancing the time using Lamport’s logical
clocks with an example.
advantages of logical clocks over physical clocks [4 marks]
Rules – 4 marks
Example- 2 marks
Advantages:
No Need for Clock Synchronization
Ensures Correct Event Ordering
Captures Causality
Immune to Clock Drift and Skew
Rules:
◼ To implement Lamport’s Logical clock each process maintains a
Q6   local counter which is updated as follows:
◼ Before executing an event, Pi executes   [10]
Ci ← Ci + 1.
◼ When process Pi sends a message m to Pj, it sets m’s timestamp
ts (m) equal to Ci after having executed the previous step.
◼ Upon the receipt of a message m, process Pj adjusts its own local
counter as
Cj ← max{Cj , ts (m)}, after which it then executes the first step
and delivers the message to the application.
Example: this is just for reference.
Q7   a.   With reference to stream-oriented communication, answer the
[10]
following:
********** 11 **********
--- page 12 ---
i ) different transmission modes [5 marks]
ii) Quality of Service (QoS) mechanisms [5 marks]
◼ In asynchronous transmission mode the data items (discrete) in a
stream are transmitted one after the other, but there are no further
timing constraints on when transmission of items should take
place.
◼ For example, a file can be transferred as a data stream, but it is
mostly irrelevant exactly when the transfer of each item
completes.
In synchronous transmission mode, there is a maximum end-to-end
delay defined for each unit in a data stream. Whether a data unit is
transferred much faster than the maximum tolerated delay is not
important. For example, a sensor may sample temperature at a certain rate
and pass it through a network to an operator
◼ In isochronous transmission mode, it is necessary that data units
are transferred on time. This means that data transfer is subject to
a maximum and minimum end-to-end delay, also referred to as
bounded (delay) jitter.
Isochronous transmission mode is particularly interesting for distributed
multimedia systems, as it plays a crucial role in representing audio and
video
b.   A distributed system uses a home-based naming approach to track
Q7
mobile objects.   [10]
a) Explain the role of a home server in maintaining object location
information and the working of home based approach
********** 12 **********
--- page 13 ---
b) Analyze how frequent object migration affects lookup latency and
system performance in the home-based approach.
a) Role of Home Server (3 Marks)
• A home server maintains the permanent record (home location)
of an object.
•   It stores a mapping from object identifier → current location
(address).
•   Clients first contact the home server to locate the object.
• Even if the object moves, the home server keeps track of its
latest position.
• Ensures location transparency for users.
• Working [ 4 marks]
To support mobile entities
home location keeps track of the current location of an entity.
Each mobile host uses a fixed IP address.
All communication to that IP address is initially directed to the
mobile host’s home agent.
Whenever the mobile host moves to another n/w, it requests a
temporary address that it can use for communication (care-of
address) which is registered to home agent.
b) Impact of Frequent Migration (3 Marks)
1. Increased Lookup Latency
• Every lookup must go through the home server, adding extra
delay.
2. Home Server Bottleneck
• Frequent updates and queries overload the home server.
********** 13 **********
--- page 14 ---
3. Higher Update Overhead
• Each movement requires updating the home server, increasing
communication cost.
4. Reduced Performance
Frequent migrations lead to network congestion and slower response
times.
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 8cc7725dac9d

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_Computer_7047/Distributed Computing/ANS_Distributed Computing(702CO0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Jul 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / IV / V/Sem 10 Re-exam/Sem 6 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Distributed Computing
Date: 08 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   What is an open distributed system and what benefits does openness
provide?
open distributed system- 1 mark
benefits – 4 marks
An open distributed system is essentially a system that offer
components that can easily be used by or integrated into another system,
originated from elsewhere.
several key advantages that openness provides to a distributed system:
•   Interoperability: This is the ability of two implementations
from different vendors to work together by relying on each   [5]
other's services as defined by the common standards.
•   Portability: This ensures that an application developed for one
distributed system can be executed on another distributed system
that implements the same interfaces without requiring significant
modification.
•   Extensibility: An open system is easy to configure and
reconfigure. It allows for the easy addition of new components
or the replacement of existing ones (even from different
developers) without affecting the rest of the system.
•   Flexibility: Because the interfaces are standardized, parts of the
system can be updated or optimized independently, allowing the
system to evolve over time to meet new requirements.
b.   Differentiate between RPC and RMI.   [5]
Any five points – 1 mark each
********** 1 **********
--- page 2 ---
c.   What are the requirements of a dependable systems in distributed system?   [5]
What is dependable system- 1 mark
Four requirements- 1 mark each
Being fault tolerant is strongly related to what are called
dependable systems.
Dependability is a term that covers a number of useful
requirements for
distributed systems including the following:
1. Availability
2. Reliability
3. Safety
4. Maintainability
Availability is defined as the property that a system is ready to be used
immediately. Reliability refers to the property that a system can run
continuously without failure. Safety refers to the situation that when a
system temporarily fails to operate correctly, nothing catastrophic happens.
maintainability refers to how easy a failed system can be repaired.
d.   Explain how identifiers differ from addresses and analyze why identifiers [5]
are preferred in dynamic distributed systems?
Difference between Identifier and Address (2 Marks)
•   Identifier:
A unique, location-independent reference to an object. It remains
constant even if the object moves.
• Address:
Represents the actual location of the object in the system. It may
change when the object moves.
• Key Difference:
Identifier = identity of object
Address = location of object
Why Identifiers are Preferred (3 Marks)
********** 2 **********
--- page 3 ---
• Location Independence: Objects can move without changing their
identifier.
• Reduced Overhead: Only mapping between identifier and address
needs updating.
•   Scalability: Efficient for managing large and dynamic systems.
Flexibility: Supports migration, replication, and load balancing.
a.   Define Hybrid Architecture in distributed systems. Using BitTorrent as
an example, explain how combining centralized and decentralized
elements optimizes performance.
Hybrid architecture – 3 marks
BitTorrent example – 7 marks
•   In this type of architecture client-server solution is combined
with decentralize architecture.
• hybrid architecture is formed by edge-server systems.
• These systems are deployed on the Internet where servers are
placed "at the edge" of the network.
• This edge is formed by the boundary between enterprise
networks and the actual Internet, for example,
as provided by an Internet Service Provider (ISP).
It is a communication protocol for P2P file sharing.
It allows to download pieces of a file from many different users
simultaneously.
The basic idea is that when an end user is looking for a file ,he
Q2   downloads chunks of a file from other users   [10]
until the download chunks can be assembled together yielding the
complete file.
1. Client note: end user computer that initiate the search for a file
and eventually assemble the downloaded chunks into a full
file.
2. Web server and webpages: the user first access a global
directory to look up a specific file. The webpages provides a
link or references to the necessary meta data.
3. File server(. Torrent file.):A user downloads a small torrent file
from this file server. This file does not contain the actual
********** 3 **********
--- page 4 ---
content it contains a reference to the tracker and information
about the file chunk.
4. Trackers: specialised server that maintains an updated list of
nodes currently storing the file(or part of file)
5. Nodes:are other peer nodes. The client node connect to a
subside of this node to file chunk back and forth.
b.   Analyze the limitations of Reliable Multicasting and explain how it is
overcome in Non-hierarchical Feedback Control scheme.
Limitations- 3 marks
Non-hierarchical Feedback Control- 5 marks
Diagram – 2 marks
The main problem with the reliable multicast scheme just
described is that it cannot support large numbers of receivers
(WAN).
If there are N receivers, the sender must be prepared to accept at
least N acknowledgments.
With many receivers, the sender may be swamped with such
feedback messages, which is also referred to as a feedback
implosion.
Nonhierarchical Feedback Control
A popular model that has been applied to several wide-area
applications is feedback suppression. This scheme underlies the
Scalable Reliable Multicasting (SRM) protocol. First, in SRM,
receivers never acknowledge the successful delivery of a
Q2   multicast message, but instead, report only when they are
missing a message.   [10]
Only negative acknowledgments are returned as feedback.
Whenever a receiver notices that it missed a message, it
multicasts its feedback to the rest of the group.
Multicasting feedback allows another group member to suppress
its own feedback.
Basic idea: Let a process P suppress its own feedback when it
notices another process Q is already asking for a retransmission
Assumptions:
•   All receivers listen to a common feedback channel to which
feedback messages are submitted
•   Process P schedules its own feedback message randomly, and
suppresses it when observing another feedback message
********** 4 **********
--- page 5 ---
a.   Discuss the general Design Issues of Servers in Distributed Systems in
detail
Explanation of each issue- 2.5 marks
general design issues:
1. General organization
2. where clients contact a server
3. Whether and how a server can be interrupted
4. Whether or not the server is stateless
1. Types of Server
Iterative Server:
The server itself handles the request and, if necessary, returns
a response to the requesting client.
An iterative server can process only one request at a time
Concurrent Server:
A concurrent server does not handle the request itself, but
passes it to a separate thread or another process, after which
it immediately waits for the next incoming request.
A multithreaded server is an example of a concurrent server.
two or more clients can run at the same time on a machine
2. where clients contact a server
Each server listens to a specific end point
Q3   In all cases, clients send requests to an end point, also called a port,   [10]
at the machine where the server is running.
3. a server is whether and how a server can be interrupted.
Client ends the connection abruptly and connects again to
restart.
Server has a separate control end point to which thew client
sends out-of-band data.
4. Whether or not the server is stateless
A stateless server does not keep information on the state of its
clients, and can change its own state without having to inform any
client.
A Web server, for example, is stateless. It merely responds to
incoming HTTP requests, which can be either for uploading a file to
the server or (most often) for fetching a file. When the request has
been processed, the Web server forgets the client completely.
A stateful server generally maintains persistent information on its
clients.
This means that the information needs to be explicitly deleted by the
server.
A typical example is a file server that allows a client to keep a local
copy of a file, even for performing update operations. Such a server
would maintain a table containing (client, file) entries
Q3   b.   Explain following failure models with an example for each
a. Crash failure   [10]
b. Omission failure
********** 5 **********
--- page 6 ---
c. Timing
d. Response
e. Arbitrary
Each type of failure- 2 marks
A crash failure occurs when a server prematurely halts, but was
working
correctly until it stopped. An important aspect of crash failures is that
once the server has halted, nothing is heard from it anymore. A typical
example of a crash failure is an operating system that comes to a
grinding halt, and for which there is only one solution: reboot it.
An omission failure occurs when a server fails to respond to a request.
Several things might go wrong. In the case of a receive omission
failure, possibly the server never got the request in the first place. Note
that it may well be the case that the connection between a client and a
server has been correctly established, but that there was no thread
listening to incoming requests. Likewise, a send omission failure
happens when the server has done its work, but somehow fails in
sending a response. Such a failure may happen, for example, when a
send buffer overflows while the server was not prepared for such a
situation.
Other types of omission failures not related to communication may be
caused by software errors such as infinite loops or improper memory
management by which the server is said to "hang."
Timing failures occur when the response lies outside a specified real-
time interval. Providing data too soon may easily cause trouble for a
recipient if there is not enough buffer space to hold all the incoming
data. More common, however, is that a server responds too late, in
which case a performance failure is said to occur.
A serious type of failure is a response failure, by which the server's
response is simply incorrect. Two kinds of response failures may
happen. In the case of a value failure, a server simply provides the
wrong reply to a request. For example, a search engine that
systematically returns Web pages not related to any of the
search terms used. has failed. The other type of response failure is
known as a state transition failure. This kind of failure happens when
the server reacts unexpectedly to an incoming request. For example, if a
server receives a message it cannot recognize, a state transition failure
happens if no measures have been taken to handle such messages.
In particular, a faulty server may incorrectly take default actions it
should never have initiated.
The most serious are arbitrary failures, also known as Byzantine failures.
In effect, when arbitrary failures occur, clients should be prepared for the
worst. In particular, it may happen that a server is producing output it
should never have produced, but which cannot be detected as being
incorrect Worse yet a faulty server may even be maliciously working
together with other servers to produce intentionally wrong answers
Q4   a.   Describe socket programming primitives used in transient
communication? Also illustrate the pattern followed for connection-   [10]
oriented communication using sockets with the help of a diagram
********** 6 **********
--- page 7 ---
Transient communication refers to communication where:
• Both sender and receiver must be active at the same time
• Messages are not stored for later delivery
This is typically implemented using sockets
A socket is an endpoint for communication between two processes over
a network
It is identified by:
• IP Address
•   Port Number
Types of Sockets
• Stream Sockets (TCP) → reliable, connection-oriented
• Datagram Sockets (UDP) → connectionless, faster
b.   Explain the goal of Election algorithms? Illustrate the step-by-step
working of bully algorithm using suitable diagrams
goal of Election algorithms- 2 marks
Bully algorithm steps – 5 marks
Diagram- 3 marks
Q4
[10]
Several distributed algorithms require that there should be coordinator
process that perform some type of coordination needed for the smooth
running of other processes in the system
It assumes that each process has a unique number.
Election algorithms attempt to locate the process with the highest
process number and designate it as coordinator.
It also assumes that every process knows the process no. of every other
process.
********** 7 **********
--- page 8 ---
It then ensures that when an election starts, it concludes with all
processes agreeing on who the new coordinator is.
The Bully Algorithm:
When a process notices that the coordinator is no longer
responding, it initiates an election. A process P holds an
election as follows:
P sends an ELECTION message to all processes with higher
numbers.
If no one responds, P wins the election and becomes
coordinator.
If one of the higher-ups answers, it takes over. P’s job is
done.
a.   Multiple processes in a distributed system simultaneously request
access to a shared resource using the Ricart–Agrawala mutual exclusion
algorithm.
Apply the algorithm to determine how a process responds to incoming
REQUEST messages under different conditions.
It requires that there be total ordering of all events in the
Q5   system.
Algorithm works as follows:   [10]
When a process wants to access a shared resource, it builds a
message containing the name of the resource, its process
number and the current (logical) time.
It then sends the message to all other processes.
When a process receives a request message ,the action it
takes depends on its own state w.r.t. the resource in the
message
◼ Three different cases:
********** 8 **********
--- page 9 ---
❑ If the receiver is not accessing the resource and does not
want to access it, it sends back an OK message to the
sender.
❑ If the receiver already has access to the resource, it
simply does not reply. Instead, it queues the request.
❑ If the receiver wants to access the resource as well but
has not yet done so, it compares the timestamp of the
incoming message with the one contained in the message
that it has sent everyone. The lowest one wins.
(a) Two processes want to access a
shared resource at the same moment.
(b) Process 0 has the lowest timestamp, so it wins.
(c) When process 0 is done, it sends an OK also, so 2 can now go ahead.
b.   What is structured naming in distributed systems? Apply the concepts
of iterative and recursive name resolution to show how a DNS query
would be processed differently in each method.
Definition of structural naming: 02 marks
Definition of iterative and recursive name resolution: 02 marks
Step-by-step explanation of iterative DNS query: 03 marks
Step-by-step explanation of recursive DNS query: 03 marks
Structural naming in distributed systems organizes names in a
hierarchical structure, where each name consists of multiple components
arranged in levels (such as directory paths or domain names).
Iterative name resolution means the client contacts each DNS server in
Q5
sequence, receiving referrals until it reaches the authoritative server.   [10]
Recursive name resolution means the client sends the query to one DNS
server, which then performs the entire lookup on behalf of the client and
returns the final answer.
In iterative DNS resolution, the client first queries the local resolver,
which contacts the root server. The root returns a referral to the
appropriate TLD server. The resolver then queries the TLD server, which
provides the authoritative server address. Finally, the resolver queries the
authoritative server to obtain the IP address and sends it back to the client.
In recursive DNS resolution, the client sends a single query to the local DNS
resolver. The resolver contacts the root server, then the TLD server, and
finally the authoritative server. After collecting the IP address, the resolver
returns the final result to the client, completing the lookup.
Q6   a.   Describe the different RPC semantics in the presence of failures. Explain
how distributed systems handle such failures.   [10]
********** 9 **********
--- page 10 ---
Each class of failure- 2 marks
Five classes of PC failure can be identified:
1. The client is unable to locate the server.
2. The request message from the client to the server is lost.
3. The reply message from the server to the client is lost.
4. The server crashes after receiving a request.
5. The client crashes after sending a request
1. The client is unable to locate the server:
Causes:
Sever might be down
Version mismatch between client and server stubs
Possible solutions:
Raising exceptions
Relying on programming languages, transparency is compromised
2. The request message from the client to the server is lost
Easiest to handle
Use timers
Retransmission
Duplicate detection at the server end
3. The reply message from the server to the client is lost.
Timer at client: client is not sure whether the reply is lost or server is
slow
Idempotent operations
Sequence numbers in requests
-   Server refuses to perform a duplicate request
-   Server should maintain state of each client
A bit in the message to distinguish initial request from retransmissions
4. The server crashes after receiving a request
Servers can crash either before executing or after executing (before
sending reply)
Crash after execution needs to be reported to client
Crash before execution can be handled by retransmission
Client’s OS cannot distinguish between the two
Server crashes are dealt with by implementing one of three possible
implementation philosophies:
•   At least once semantics: a guarantee is given that the RPC
occurred at least once, but (also) possibly more that once.
•   At most once semantics: a guarantee is given that the RPC
occurred at most once, but possibly not at all.
• No semantics: nothing is guaranteed, and client and servers take
their chances!
5. The client crashes after sending a request
Can lead to orphans
Wastage of resources
Confusion or reboots
Solution 1: Extermination with logging
-   Maintain logs of RPC calls
-   Explicit termination of orphans
- Logging is expensive
Solution 2: Reincarnation
- Time is divided into epochs
********** 10 **********
--- page 11 ---
-   Broadcast epoch on client reboot
- Orphans are killed when a server receives new epoch
announcement
-   Solution 3: Gentler re-incarnation
-   - kill computations whose owners cannot be located
-   Solution 4: Expiration
-   - time window for completion with explicit extension
-   Client waits before rebooting
b.
What are the advantages of logical clocks over physical clocks?
Explain the rules used in advancing the time using Lamport’s logical
clocks with an example.
advantages of logical clocks over physical clocks [4 marks]
Rules – 4 marks
Example- 2 marks
Advantages:
No Need for Clock Synchronization
Ensures Correct Event Ordering
Captures Causality
Immune to Clock Drift and Skew
Rules:
◼ To implement Lamport’s Logical clock each process maintains a
Q6   local counter which is updated as follows:
◼ Before executing an event, Pi executes   [10]
Ci ← Ci + 1.
◼ When process Pi sends a message m to Pj, it sets m’s timestamp
ts (m) equal to Ci after having executed the previous step.
◼ Upon the receipt of a message m, process Pj adjusts its own local
counter as
Cj ← max{Cj , ts (m)}, after which it then executes the first step
and delivers the message to the application.
Example: this is just for reference.
Q7   a.   With reference to stream-oriented communication, answer the
[10]
following:
********** 11 **********
--- page 12 ---
i ) different transmission modes [5 marks]
ii) Quality of Service (QoS) mechanisms [5 marks]
◼ In asynchronous transmission mode the data items (discrete) in a
stream are transmitted one after the other, but there are no further
timing constraints on when transmission of items should take
place.
◼ For example, a file can be transferred as a data stream, but it is
mostly irrelevant exactly when the transfer of each item
completes.
In synchronous transmission mode, there is a maximum end-to-end
delay defined for each unit in a data stream. Whether a data unit is
transferred much faster than the maximum tolerated delay is not
important. For example, a sensor may sample temperature at a certain rate
and pass it through a network to an operator
◼ In isochronous transmission mode, it is necessary that data units
are transferred on time. This means that data transfer is subject to
a maximum and minimum end-to-end delay, also referred to as
bounded (delay) jitter.
Isochronous transmission mode is particularly interesting for distributed
multimedia systems, as it plays a crucial role in representing audio and
video
b.   A distributed system uses a home-based naming approach to track
Q7
mobile objects.   [10]
a) Explain the role of a home server in maintaining object location
information and the working of home based approach
********** 12 **********
--- page 13 ---
b) Analyze how frequent object migration affects lookup latency and
system performance in the home-based approach.
a) Role of Home Server (3 Marks)
• A home server maintains the permanent record (home location)
of an object.
•   It stores a mapping from object identifier → current location
(address).
•   Clients first contact the home server to locate the object.
• Even if the object moves, the home server keeps track of its
latest position.
• Ensures location transparency for users.
• Working [ 4 marks]
To support mobile entities
home location keeps track of the current location of an entity.
Each mobile host uses a fixed IP address.
All communication to that IP address is initially directed to the
mobile host’s home agent.
Whenever the mobile host moves to another n/w, it requests a
temporary address that it can use for communication (care-of
address) which is registered to home agent.
b) Impact of Frequent Migration (3 Marks)
1. Increased Lookup Latency
• Every lookup must go through the home server, adding extra
delay.
2. Home Server Bottleneck
• Frequent updates and queries overload the home server.
********** 13 **********
--- page 14 ---
3. Higher Update Overhead
• Each movement requires updating the home server, increasing
communication cost.
4. Reduced Performance
Frequent migrations lead to network congestion and slower response
times.
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper de35d0ae29b1

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/MBATech_IT_7041/Distributed Computing/ANS_Distributed Computing(702CO0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Jul 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / IV / V/Sem 10 Re-exam/Sem 6 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Distributed Computing
Date: 08 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   What is an open distributed system and what benefits does openness
provide?
open distributed system- 1 mark
benefits – 4 marks
An open distributed system is essentially a system that offer
components that can easily be used by or integrated into another system,
originated from elsewhere.
several key advantages that openness provides to a distributed system:
•   Interoperability: This is the ability of two implementations
from different vendors to work together by relying on each   [5]
other's services as defined by the common standards.
•   Portability: This ensures that an application developed for one
distributed system can be executed on another distributed system
that implements the same interfaces without requiring significant
modification.
•   Extensibility: An open system is easy to configure and
reconfigure. It allows for the easy addition of new components
or the replacement of existing ones (even from different
developers) without affecting the rest of the system.
•   Flexibility: Because the interfaces are standardized, parts of the
system can be updated or optimized independently, allowing the
system to evolve over time to meet new requirements.
b.   Differentiate between RPC and RMI.   [5]
Any five points – 1 mark each
********** 1 **********
--- page 2 ---
c.   What are the requirements of a dependable systems in distributed system?   [5]
What is dependable system- 1 mark
Four requirements- 1 mark each
Being fault tolerant is strongly related to what are called
dependable systems.
Dependability is a term that covers a number of useful
requirements for
distributed systems including the following:
1. Availability
2. Reliability
3. Safety
4. Maintainability
Availability is defined as the property that a system is ready to be used
immediately. Reliability refers to the property that a system can run
continuously without failure. Safety refers to the situation that when a
system temporarily fails to operate correctly, nothing catastrophic happens.
maintainability refers to how easy a failed system can be repaired.
d.   Explain how identifiers differ from addresses and analyze why identifiers [5]
are preferred in dynamic distributed systems?
Difference between Identifier and Address (2 Marks)
•   Identifier:
A unique, location-independent reference to an object. It remains
constant even if the object moves.
• Address:
Represents the actual location of the object in the system. It may
change when the object moves.
• Key Difference:
Identifier = identity of object
Address = location of object
Why Identifiers are Preferred (3 Marks)
********** 2 **********
--- page 3 ---
• Location Independence: Objects can move without changing their
identifier.
• Reduced Overhead: Only mapping between identifier and address
needs updating.
•   Scalability: Efficient for managing large and dynamic systems.
Flexibility: Supports migration, replication, and load balancing.
a.   Define Hybrid Architecture in distributed systems. Using BitTorrent as
an example, explain how combining centralized and decentralized
elements optimizes performance.
Hybrid architecture – 3 marks
BitTorrent example – 7 marks
•   In this type of architecture client-server solution is combined
with decentralize architecture.
• hybrid architecture is formed by edge-server systems.
• These systems are deployed on the Internet where servers are
placed "at the edge" of the network.
• This edge is formed by the boundary between enterprise
networks and the actual Internet, for example,
as provided by an Internet Service Provider (ISP).
It is a communication protocol for P2P file sharing.
It allows to download pieces of a file from many different users
simultaneously.
The basic idea is that when an end user is looking for a file ,he
Q2   downloads chunks of a file from other users   [10]
until the download chunks can be assembled together yielding the
complete file.
1. Client note: end user computer that initiate the search for a file
and eventually assemble the downloaded chunks into a full
file.
2. Web server and webpages: the user first access a global
directory to look up a specific file. The webpages provides a
link or references to the necessary meta data.
3. File server(. Torrent file.):A user downloads a small torrent file
from this file server. This file does not contain the actual
********** 3 **********
--- page 4 ---
content it contains a reference to the tracker and information
about the file chunk.
4. Trackers: specialised server that maintains an updated list of
nodes currently storing the file(or part of file)
5. Nodes:are other peer nodes. The client node connect to a
subside of this node to file chunk back and forth.
b.   Analyze the limitations of Reliable Multicasting and explain how it is
overcome in Non-hierarchical Feedback Control scheme.
Limitations- 3 marks
Non-hierarchical Feedback Control- 5 marks
Diagram – 2 marks
The main problem with the reliable multicast scheme just
described is that it cannot support large numbers of receivers
(WAN).
If there are N receivers, the sender must be prepared to accept at
least N acknowledgments.
With many receivers, the sender may be swamped with such
feedback messages, which is also referred to as a feedback
implosion.
Nonhierarchical Feedback Control
A popular model that has been applied to several wide-area
applications is feedback suppression. This scheme underlies the
Scalable Reliable Multicasting (SRM) protocol. First, in SRM,
receivers never acknowledge the successful delivery of a
Q2   multicast message, but instead, report only when they are
missing a message.   [10]
Only negative acknowledgments are returned as feedback.
Whenever a receiver notices that it missed a message, it
multicasts its feedback to the rest of the group.
Multicasting feedback allows another group member to suppress
its own feedback.
Basic idea: Let a process P suppress its own feedback when it
notices another process Q is already asking for a retransmission
Assumptions:
•   All receivers listen to a common feedback channel to which
feedback messages are submitted
•   Process P schedules its own feedback message randomly, and
suppresses it when observing another feedback message
********** 4 **********
--- page 5 ---
a.   Discuss the general Design Issues of Servers in Distributed Systems in
detail
Explanation of each issue- 2.5 marks
general design issues:
1. General organization
2. where clients contact a server
3. Whether and how a server can be interrupted
4. Whether or not the server is stateless
1. Types of Server
Iterative Server:
The server itself handles the request and, if necessary, returns
a response to the requesting client.
An iterative server can process only one request at a time
Concurrent Server:
A concurrent server does not handle the request itself, but
passes it to a separate thread or another process, after which
it immediately waits for the next incoming request.
A multithreaded server is an example of a concurrent server.
two or more clients can run at the same time on a machine
2. where clients contact a server
Each server listens to a specific end point
Q3   In all cases, clients send requests to an end point, also called a port,   [10]
at the machine where the server is running.
3. a server is whether and how a server can be interrupted.
Client ends the connection abruptly and connects again to
restart.
Server has a separate control end point to which thew client
sends out-of-band data.
4. Whether or not the server is stateless
A stateless server does not keep information on the state of its
clients, and can change its own state without having to inform any
client.
A Web server, for example, is stateless. It merely responds to
incoming HTTP requests, which can be either for uploading a file to
the server or (most often) for fetching a file. When the request has
been processed, the Web server forgets the client completely.
A stateful server generally maintains persistent information on its
clients.
This means that the information needs to be explicitly deleted by the
server.
A typical example is a file server that allows a client to keep a local
copy of a file, even for performing update operations. Such a server
would maintain a table containing (client, file) entries
Q3   b.   Explain following failure models with an example for each
a. Crash failure   [10]
b. Omission failure
********** 5 **********
--- page 6 ---
c. Timing
d. Response
e. Arbitrary
Each type of failure- 2 marks
A crash failure occurs when a server prematurely halts, but was
working
correctly until it stopped. An important aspect of crash failures is that
once the server has halted, nothing is heard from it anymore. A typical
example of a crash failure is an operating system that comes to a
grinding halt, and for which there is only one solution: reboot it.
An omission failure occurs when a server fails to respond to a request.
Several things might go wrong. In the case of a receive omission
failure, possibly the server never got the request in the first place. Note
that it may well be the case that the connection between a client and a
server has been correctly established, but that there was no thread
listening to incoming requests. Likewise, a send omission failure
happens when the server has done its work, but somehow fails in
sending a response. Such a failure may happen, for example, when a
send buffer overflows while the server was not prepared for such a
situation.
Other types of omission failures not related to communication may be
caused by software errors such as infinite loops or improper memory
management by which the server is said to "hang."
Timing failures occur when the response lies outside a specified real-
time interval. Providing data too soon may easily cause trouble for a
recipient if there is not enough buffer space to hold all the incoming
data. More common, however, is that a server responds too late, in
which case a performance failure is said to occur.
A serious type of failure is a response failure, by which the server's
response is simply incorrect. Two kinds of response failures may
happen. In the case of a value failure, a server simply provides the
wrong reply to a request. For example, a search engine that
systematically returns Web pages not related to any of the
search terms used. has failed. The other type of response failure is
known as a state transition failure. This kind of failure happens when
the server reacts unexpectedly to an incoming request. For example, if a
server receives a message it cannot recognize, a state transition failure
happens if no measures have been taken to handle such messages.
In particular, a faulty server may incorrectly take default actions it
should never have initiated.
The most serious are arbitrary failures, also known as Byzantine failures.
In effect, when arbitrary failures occur, clients should be prepared for the
worst. In particular, it may happen that a server is producing output it
should never have produced, but which cannot be detected as being
incorrect Worse yet a faulty server may even be maliciously working
together with other servers to produce intentionally wrong answers
Q4   a.   Describe socket programming primitives used in transient
communication? Also illustrate the pattern followed for connection-   [10]
oriented communication using sockets with the help of a diagram
********** 6 **********
--- page 7 ---
Transient communication refers to communication where:
• Both sender and receiver must be active at the same time
• Messages are not stored for later delivery
This is typically implemented using sockets
A socket is an endpoint for communication between two processes over
a network
It is identified by:
• IP Address
•   Port Number
Types of Sockets
• Stream Sockets (TCP) → reliable, connection-oriented
• Datagram Sockets (UDP) → connectionless, faster
b.   Explain the goal of Election algorithms? Illustrate the step-by-step
working of bully algorithm using suitable diagrams
goal of Election algorithms- 2 marks
Bully algorithm steps – 5 marks
Diagram- 3 marks
Q4
[10]
Several distributed algorithms require that there should be coordinator
process that perform some type of coordination needed for the smooth
running of other processes in the system
It assumes that each process has a unique number.
Election algorithms attempt to locate the process with the highest
process number and designate it as coordinator.
It also assumes that every process knows the process no. of every other
process.
********** 7 **********
--- page 8 ---
It then ensures that when an election starts, it concludes with all
processes agreeing on who the new coordinator is.
The Bully Algorithm:
When a process notices that the coordinator is no longer
responding, it initiates an election. A process P holds an
election as follows:
P sends an ELECTION message to all processes with higher
numbers.
If no one responds, P wins the election and becomes
coordinator.
If one of the higher-ups answers, it takes over. P’s job is
done.
a.   Multiple processes in a distributed system simultaneously request
access to a shared resource using the Ricart–Agrawala mutual exclusion
algorithm.
Apply the algorithm to determine how a process responds to incoming
REQUEST messages under different conditions.
It requires that there be total ordering of all events in the
Q5   system.
Algorithm works as follows:   [10]
When a process wants to access a shared resource, it builds a
message containing the name of the resource, its process
number and the current (logical) time.
It then sends the message to all other processes.
When a process receives a request message ,the action it
takes depends on its own state w.r.t. the resource in the
message
◼ Three different cases:
********** 8 **********
--- page 9 ---
❑ If the receiver is not accessing the resource and does not
want to access it, it sends back an OK message to the
sender.
❑ If the receiver already has access to the resource, it
simply does not reply. Instead, it queues the request.
❑ If the receiver wants to access the resource as well but
has not yet done so, it compares the timestamp of the
incoming message with the one contained in the message
that it has sent everyone. The lowest one wins.
(a) Two processes want to access a
shared resource at the same moment.
(b) Process 0 has the lowest timestamp, so it wins.
(c) When process 0 is done, it sends an OK also, so 2 can now go ahead.
b.   What is structured naming in distributed systems? Apply the concepts
of iterative and recursive name resolution to show how a DNS query
would be processed differently in each method.
Definition of structural naming: 02 marks
Definition of iterative and recursive name resolution: 02 marks
Step-by-step explanation of iterative DNS query: 03 marks
Step-by-step explanation of recursive DNS query: 03 marks
Structural naming in distributed systems organizes names in a
hierarchical structure, where each name consists of multiple components
arranged in levels (such as directory paths or domain names).
Iterative name resolution means the client contacts each DNS server in
Q5
sequence, receiving referrals until it reaches the authoritative server.   [10]
Recursive name resolution means the client sends the query to one DNS
server, which then performs the entire lookup on behalf of the client and
returns the final answer.
In iterative DNS resolution, the client first queries the local resolver,
which contacts the root server. The root returns a referral to the
appropriate TLD server. The resolver then queries the TLD server, which
provides the authoritative server address. Finally, the resolver queries the
authoritative server to obtain the IP address and sends it back to the client.
In recursive DNS resolution, the client sends a single query to the local DNS
resolver. The resolver contacts the root server, then the TLD server, and
finally the authoritative server. After collecting the IP address, the resolver
returns the final result to the client, completing the lookup.
Q6   a.   Describe the different RPC semantics in the presence of failures. Explain
how distributed systems handle such failures.   [10]
********** 9 **********
--- page 10 ---
Each class of failure- 2 marks
Five classes of PC failure can be identified:
1. The client is unable to locate the server.
2. The request message from the client to the server is lost.
3. The reply message from the server to the client is lost.
4. The server crashes after receiving a request.
5. The client crashes after sending a request
1. The client is unable to locate the server:
Causes:
Sever might be down
Version mismatch between client and server stubs
Possible solutions:
Raising exceptions
Relying on programming languages, transparency is compromised
2. The request message from the client to the server is lost
Easiest to handle
Use timers
Retransmission
Duplicate detection at the server end
3. The reply message from the server to the client is lost.
Timer at client: client is not sure whether the reply is lost or server is
slow
Idempotent operations
Sequence numbers in requests
-   Server refuses to perform a duplicate request
-   Server should maintain state of each client
A bit in the message to distinguish initial request from retransmissions
4. The server crashes after receiving a request
Servers can crash either before executing or after executing (before
sending reply)
Crash after execution needs to be reported to client
Crash before execution can be handled by retransmission
Client’s OS cannot distinguish between the two
Server crashes are dealt with by implementing one of three possible
implementation philosophies:
•   At least once semantics: a guarantee is given that the RPC
occurred at least once, but (also) possibly more that once.
•   At most once semantics: a guarantee is given that the RPC
occurred at most once, but possibly not at all.
• No semantics: nothing is guaranteed, and client and servers take
their chances!
5. The client crashes after sending a request
Can lead to orphans
Wastage of resources
Confusion or reboots
Solution 1: Extermination with logging
-   Maintain logs of RPC calls
-   Explicit termination of orphans
- Logging is expensive
Solution 2: Reincarnation
- Time is divided into epochs
********** 10 **********
--- page 11 ---
-   Broadcast epoch on client reboot
- Orphans are killed when a server receives new epoch
announcement
-   Solution 3: Gentler re-incarnation
-   - kill computations whose owners cannot be located
-   Solution 4: Expiration
-   - time window for completion with explicit extension
-   Client waits before rebooting
b.
What are the advantages of logical clocks over physical clocks?
Explain the rules used in advancing the time using Lamport’s logical
clocks with an example.
advantages of logical clocks over physical clocks [4 marks]
Rules – 4 marks
Example- 2 marks
Advantages:
No Need for Clock Synchronization
Ensures Correct Event Ordering
Captures Causality
Immune to Clock Drift and Skew
Rules:
◼ To implement Lamport’s Logical clock each process maintains a
Q6   local counter which is updated as follows:
◼ Before executing an event, Pi executes   [10]
Ci ← Ci + 1.
◼ When process Pi sends a message m to Pj, it sets m’s timestamp
ts (m) equal to Ci after having executed the previous step.
◼ Upon the receipt of a message m, process Pj adjusts its own local
counter as
Cj ← max{Cj , ts (m)}, after which it then executes the first step
and delivers the message to the application.
Example: this is just for reference.
Q7   a.   With reference to stream-oriented communication, answer the
[10]
following:
********** 11 **********
--- page 12 ---
i ) different transmission modes [5 marks]
ii) Quality of Service (QoS) mechanisms [5 marks]
◼ In asynchronous transmission mode the data items (discrete) in a
stream are transmitted one after the other, but there are no further
timing constraints on when transmission of items should take
place.
◼ For example, a file can be transferred as a data stream, but it is
mostly irrelevant exactly when the transfer of each item
completes.
In synchronous transmission mode, there is a maximum end-to-end
delay defined for each unit in a data stream. Whether a data unit is
transferred much faster than the maximum tolerated delay is not
important. For example, a sensor may sample temperature at a certain rate
and pass it through a network to an operator
◼ In isochronous transmission mode, it is necessary that data units
are transferred on time. This means that data transfer is subject to
a maximum and minimum end-to-end delay, also referred to as
bounded (delay) jitter.
Isochronous transmission mode is particularly interesting for distributed
multimedia systems, as it plays a crucial role in representing audio and
video
b.   A distributed system uses a home-based naming approach to track
Q7
mobile objects.   [10]
a) Explain the role of a home server in maintaining object location
information and the working of home based approach
********** 12 **********
--- page 13 ---
b) Analyze how frequent object migration affects lookup latency and
system performance in the home-based approach.
a) Role of Home Server (3 Marks)
• A home server maintains the permanent record (home location)
of an object.
•   It stores a mapping from object identifier → current location
(address).
•   Clients first contact the home server to locate the object.
• Even if the object moves, the home server keeps track of its
latest position.
• Ensures location transparency for users.
• Working [ 4 marks]
To support mobile entities
home location keeps track of the current location of an entity.
Each mobile host uses a fixed IP address.
All communication to that IP address is initially directed to the
mobile host’s home agent.
Whenever the mobile host moves to another n/w, it requests a
temporary address that it can use for communication (care-of
address) which is registered to home agent.
b) Impact of Frequent Migration (3 Marks)
1. Increased Lookup Latency
• Every lookup must go through the home server, adding extra
delay.
2. Home Server Bottleneck
• Frequent updates and queries overload the home server.
********** 13 **********
--- page 14 ---
3. Higher Update Overhead
• Each movement requires updating the home server, increasing
communication cost.
4. Reduced Performance
Frequent migrations lead to network congestion and slower response
times.
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 10 · Answer key · paper 447a9a8d3e89

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_10/Re-Exam/Integrated_Computer_7032/Distributed Computing/ANS_Distributed Computing(702CO0C034)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Jul 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / IV / V/Sem 10 Re-exam/Sem 6 Re-exam/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Distributed Computing
Date: 08 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   What is an open distributed system and what benefits does openness
provide?
open distributed system- 1 mark
benefits – 4 marks
An open distributed system is essentially a system that offer
components that can easily be used by or integrated into another system,
originated from elsewhere.
several key advantages that openness provides to a distributed system:
•   Interoperability: This is the ability of two implementations
from different vendors to work together by relying on each   [5]
other's services as defined by the common standards.
•   Portability: This ensures that an application developed for one
distributed system can be executed on another distributed system
that implements the same interfaces without requiring significant
modification.
•   Extensibility: An open system is easy to configure and
reconfigure. It allows for the easy addition of new components
or the replacement of existing ones (even from different
developers) without affecting the rest of the system.
•   Flexibility: Because the interfaces are standardized, parts of the
system can be updated or optimized independently, allowing the
system to evolve over time to meet new requirements.
b.   Differentiate between RPC and RMI.   [5]
Any five points – 1 mark each
********** 1 **********
--- page 2 ---
c.   What are the requirements of a dependable systems in distributed system?   [5]
What is dependable system- 1 mark
Four requirements- 1 mark each
Being fault tolerant is strongly related to what are called
dependable systems.
Dependability is a term that covers a number of useful
requirements for
distributed systems including the following:
1. Availability
2. Reliability
3. Safety
4. Maintainability
Availability is defined as the property that a system is ready to be used
immediately. Reliability refers to the property that a system can run
continuously without failure. Safety refers to the situation that when a
system temporarily fails to operate correctly, nothing catastrophic happens.
maintainability refers to how easy a failed system can be repaired.
d.   Explain how identifiers differ from addresses and analyze why identifiers [5]
are preferred in dynamic distributed systems?
Difference between Identifier and Address (2 Marks)
•   Identifier:
A unique, location-independent reference to an object. It remains
constant even if the object moves.
• Address:
Represents the actual location of the object in the system. It may
change when the object moves.
• Key Difference:
Identifier = identity of object
Address = location of object
Why Identifiers are Preferred (3 Marks)
********** 2 **********
--- page 3 ---
• Location Independence: Objects can move without changing their
identifier.
• Reduced Overhead: Only mapping between identifier and address
needs updating.
•   Scalability: Efficient for managing large and dynamic systems.
Flexibility: Supports migration, replication, and load balancing.
a.   Define Hybrid Architecture in distributed systems. Using BitTorrent as
an example, explain how combining centralized and decentralized
elements optimizes performance.
Hybrid architecture – 3 marks
BitTorrent example – 7 marks
•   In this type of architecture client-server solution is combined
with decentralize architecture.
• hybrid architecture is formed by edge-server systems.
• These systems are deployed on the Internet where servers are
placed "at the edge" of the network.
• This edge is formed by the boundary between enterprise
networks and the actual Internet, for example,
as provided by an Internet Service Provider (ISP).
It is a communication protocol for P2P file sharing.
It allows to download pieces of a file from many different users
simultaneously.
The basic idea is that when an end user is looking for a file ,he
Q2   downloads chunks of a file from other users   [10]
until the download chunks can be assembled together yielding the
complete file.
1. Client note: end user computer that initiate the search for a file
and eventually assemble the downloaded chunks into a full
file.
2. Web server and webpages: the user first access a global
directory to look up a specific file. The webpages provides a
link or references to the necessary meta data.
3. File server(. Torrent file.):A user downloads a small torrent file
from this file server. This file does not contain the actual
********** 3 **********
--- page 4 ---
content it contains a reference to the tracker and information
about the file chunk.
4. Trackers: specialised server that maintains an updated list of
nodes currently storing the file(or part of file)
5. Nodes:are other peer nodes. The client node connect to a
subside of this node to file chunk back and forth.
b.   Analyze the limitations of Reliable Multicasting and explain how it is
overcome in Non-hierarchical Feedback Control scheme.
Limitations- 3 marks
Non-hierarchical Feedback Control- 5 marks
Diagram – 2 marks
The main problem with the reliable multicast scheme just
described is that it cannot support large numbers of receivers
(WAN).
If there are N receivers, the sender must be prepared to accept at
least N acknowledgments.
With many receivers, the sender may be swamped with such
feedback messages, which is also referred to as a feedback
implosion.
Nonhierarchical Feedback Control
A popular model that has been applied to several wide-area
applications is feedback suppression. This scheme underlies the
Scalable Reliable Multicasting (SRM) protocol. First, in SRM,
receivers never acknowledge the successful delivery of a
Q2   multicast message, but instead, report only when they are
missing a message.   [10]
Only negative acknowledgments are returned as feedback.
Whenever a receiver notices that it missed a message, it
multicasts its feedback to the rest of the group.
Multicasting feedback allows another group member to suppress
its own feedback.
Basic idea: Let a process P suppress its own feedback when it
notices another process Q is already asking for a retransmission
Assumptions:
•   All receivers listen to a common feedback channel to which
feedback messages are submitted
•   Process P schedules its own feedback message randomly, and
suppresses it when observing another feedback message
********** 4 **********
--- page 5 ---
a.   Discuss the general Design Issues of Servers in Distributed Systems in
detail
Explanation of each issue- 2.5 marks
general design issues:
1. General organization
2. where clients contact a server
3. Whether and how a server can be interrupted
4. Whether or not the server is stateless
1. Types of Server
Iterative Server:
The server itself handles the request and, if necessary, returns
a response to the requesting client.
An iterative server can process only one request at a time
Concurrent Server:
A concurrent server does not handle the request itself, but
passes it to a separate thread or another process, after which
it immediately waits for the next incoming request.
A multithreaded server is an example of a concurrent server.
two or more clients can run at the same time on a machine
2. where clients contact a server
Each server listens to a specific end point
Q3   In all cases, clients send requests to an end point, also called a port,   [10]
at the machine where the server is running.
3. a server is whether and how a server can be interrupted.
Client ends the connection abruptly and connects again to
restart.
Server has a separate control end point to which thew client
sends out-of-band data.
4. Whether or not the server is stateless
A stateless server does not keep information on the state of its
clients, and can change its own state without having to inform any
client.
A Web server, for example, is stateless. It merely responds to
incoming HTTP requests, which can be either for uploading a file to
the server or (most often) for fetching a file. When the request has
been processed, the Web server forgets the client completely.
A stateful server generally maintains persistent information on its
clients.
This means that the information needs to be explicitly deleted by the
server.
A typical example is a file server that allows a client to keep a local
copy of a file, even for performing update operations. Such a server
would maintain a table containing (client, file) entries
Q3   b.   Explain following failure models with an example for each
a. Crash failure   [10]
b. Omission failure
********** 5 **********
--- page 6 ---
c. Timing
d. Response
e. Arbitrary
Each type of failure- 2 marks
A crash failure occurs when a server prematurely halts, but was
working
correctly until it stopped. An important aspect of crash failures is that
once the server has halted, nothing is heard from it anymore. A typical
example of a crash failure is an operating system that comes to a
grinding halt, and for which there is only one solution: reboot it.
An omission failure occurs when a server fails to respond to a request.
Several things might go wrong. In the case of a receive omission
failure, possibly the server never got the request in the first place. Note
that it may well be the case that the connection between a client and a
server has been correctly established, but that there was no thread
listening to incoming requests. Likewise, a send omission failure
happens when the server has done its work, but somehow fails in
sending a response. Such a failure may happen, for example, when a
send buffer overflows while the server was not prepared for such a
situation.
Other types of omission failures not related to communication may be
caused by software errors such as infinite loops or improper memory
management by which the server is said to "hang."
Timing failures occur when the response lies outside a specified real-
time interval. Providing data too soon may easily cause trouble for a
recipient if there is not enough buffer space to hold all the incoming
data. More common, however, is that a server responds too late, in
which case a performance failure is said to occur.
A serious type of failure is a response failure, by which the server's
response is simply incorrect. Two kinds of response failures may
happen. In the case of a value failure, a server simply provides the
wrong reply to a request. For example, a search engine that
systematically returns Web pages not related to any of the
search terms used. has failed. The other type of response failure is
known as a state transition failure. This kind of failure happens when
the server reacts unexpectedly to an incoming request. For example, if a
server receives a message it cannot recognize, a state transition failure
happens if no measures have been taken to handle such messages.
In particular, a faulty server may incorrectly take default actions it
should never have initiated.
The most serious are arbitrary failures, also known as Byzantine failures.
In effect, when arbitrary failures occur, clients should be prepared for the
worst. In particular, it may happen that a server is producing output it
should never have produced, but which cannot be detected as being
incorrect Worse yet a faulty server may even be maliciously working
together with other servers to produce intentionally wrong answers
Q4   a.   Describe socket programming primitives used in transient
communication? Also illustrate the pattern followed for connection-   [10]
oriented communication using sockets with the help of a diagram
********** 6 **********
--- page 7 ---
Transient communication refers to communication where:
• Both sender and receiver must be active at the same time
• Messages are not stored for later delivery
This is typically implemented using sockets
A socket is an endpoint for communication between two processes over
a network
It is identified by:
• IP Address
•   Port Number
Types of Sockets
• Stream Sockets (TCP) → reliable, connection-oriented
• Datagram Sockets (UDP) → connectionless, faster
b.   Explain the goal of Election algorithms? Illustrate the step-by-step
working of bully algorithm using suitable diagrams
goal of Election algorithms- 2 marks
Bully algorithm steps – 5 marks
Diagram- 3 marks
Q4
[10]
Several distributed algorithms require that there should be coordinator
process that perform some type of coordination needed for the smooth
running of other processes in the system
It assumes that each process has a unique number.
Election algorithms attempt to locate the process with the highest
process number and designate it as coordinator.
It also assumes that every process knows the process no. of every other
process.
********** 7 **********
--- page 8 ---
It then ensures that when an election starts, it concludes with all
processes agreeing on who the new coordinator is.
The Bully Algorithm:
When a process notices that the coordinator is no longer
responding, it initiates an election. A process P holds an
election as follows:
P sends an ELECTION message to all processes with higher
numbers.
If no one responds, P wins the election and becomes
coordinator.
If one of the higher-ups answers, it takes over. P’s job is
done.
a.   Multiple processes in a distributed system simultaneously request
access to a shared resource using the Ricart–Agrawala mutual exclusion
algorithm.
Apply the algorithm to determine how a process responds to incoming
REQUEST messages under different conditions.
It requires that there be total ordering of all events in the
Q5   system.
Algorithm works as follows:   [10]
When a process wants to access a shared resource, it builds a
message containing the name of the resource, its process
number and the current (logical) time.
It then sends the message to all other processes.
When a process receives a request message ,the action it
takes depends on its own state w.r.t. the resource in the
message
◼ Three different cases:
********** 8 **********
--- page 9 ---
❑ If the receiver is not accessing the resource and does not
want to access it, it sends back an OK message to the
sender.
❑ If the receiver already has access to the resource, it
simply does not reply. Instead, it queues the request.
❑ If the receiver wants to access the resource as well but
has not yet done so, it compares the timestamp of the
incoming message with the one contained in the message
that it has sent everyone. The lowest one wins.
(a) Two processes want to access a
shared resource at the same moment.
(b) Process 0 has the lowest timestamp, so it wins.
(c) When process 0 is done, it sends an OK also, so 2 can now go ahead.
b.   What is structured naming in distributed systems? Apply the concepts
of iterative and recursive name resolution to show how a DNS query
would be processed differently in each method.
Definition of structural naming: 02 marks
Definition of iterative and recursive name resolution: 02 marks
Step-by-step explanation of iterative DNS query: 03 marks
Step-by-step explanation of recursive DNS query: 03 marks
Structural naming in distributed systems organizes names in a
hierarchical structure, where each name consists of multiple components
arranged in levels (such as directory paths or domain names).
Iterative name resolution means the client contacts each DNS server in
Q5
sequence, receiving referrals until it reaches the authoritative server.   [10]
Recursive name resolution means the client sends the query to one DNS
server, which then performs the entire lookup on behalf of the client and
returns the final answer.
In iterative DNS resolution, the client first queries the local resolver,
which contacts the root server. The root returns a referral to the
appropriate TLD server. The resolver then queries the TLD server, which
provides the authoritative server address. Finally, the resolver queries the
authoritative server to obtain the IP address and sends it back to the client.
In recursive DNS resolution, the client sends a single query to the local DNS
resolver. The resolver contacts the root server, then the TLD server, and
finally the authoritative server. After collecting the IP address, the resolver
returns the final result to the client, completing the lookup.
Q6   a.   Describe the different RPC semantics in the presence of failures. Explain
how distributed systems handle such failures.   [10]
********** 9 **********
--- page 10 ---
Each class of failure- 2 marks
Five classes of PC failure can be identified:
1. The client is unable to locate the server.
2. The request message from the client to the server is lost.
3. The reply message from the server to the client is lost.
4. The server crashes after receiving a request.
5. The client crashes after sending a request
1. The client is unable to locate the server:
Causes:
Sever might be down
Version mismatch between client and server stubs
Possible solutions:
Raising exceptions
Relying on programming languages, transparency is compromised
2. The request message from the client to the server is lost
Easiest to handle
Use timers
Retransmission
Duplicate detection at the server end
3. The reply message from the server to the client is lost.
Timer at client: client is not sure whether the reply is lost or server is
slow
Idempotent operations
Sequence numbers in requests
-   Server refuses to perform a duplicate request
-   Server should maintain state of each client
A bit in the message to distinguish initial request from retransmissions
4. The server crashes after receiving a request
Servers can crash either before executing or after executing (before
sending reply)
Crash after execution needs to be reported to client
Crash before execution can be handled by retransmission
Client’s OS cannot distinguish between the two
Server crashes are dealt with by implementing one of three possible
implementation philosophies:
•   At least once semantics: a guarantee is given that the RPC
occurred at least once, but (also) possibly more that once.
•   At most once semantics: a guarantee is given that the RPC
occurred at most once, but possibly not at all.
• No semantics: nothing is guaranteed, and client and servers take
their chances!
5. The client crashes after sending a request
Can lead to orphans
Wastage of resources
Confusion or reboots
Solution 1: Extermination with logging
-   Maintain logs of RPC calls
-   Explicit termination of orphans
- Logging is expensive
Solution 2: Reincarnation
- Time is divided into epochs
********** 10 **********
--- page 11 ---
-   Broadcast epoch on client reboot
- Orphans are killed when a server receives new epoch
announcement
-   Solution 3: Gentler re-incarnation
-   - kill computations whose owners cannot be located
-   Solution 4: Expiration
-   - time window for completion with explicit extension
-   Client waits before rebooting
b.
What are the advantages of logical clocks over physical clocks?
Explain the rules used in advancing the time using Lamport’s logical
clocks with an example.
advantages of logical clocks over physical clocks [4 marks]
Rules – 4 marks
Example- 2 marks
Advantages:
No Need for Clock Synchronization
Ensures Correct Event Ordering
Captures Causality
Immune to Clock Drift and Skew
Rules:
◼ To implement Lamport’s Logical clock each process maintains a
Q6   local counter which is updated as follows:
◼ Before executing an event, Pi executes   [10]
Ci ← Ci + 1.
◼ When process Pi sends a message m to Pj, it sets m’s timestamp
ts (m) equal to Ci after having executed the previous step.
◼ Upon the receipt of a message m, process Pj adjusts its own local
counter as
Cj ← max{Cj , ts (m)}, after which it then executes the first step
and delivers the message to the application.
Example: this is just for reference.
Q7   a.   With reference to stream-oriented communication, answer the
[10]
following:
********** 11 **********
--- page 12 ---
i ) different transmission modes [5 marks]
ii) Quality of Service (QoS) mechanisms [5 marks]
◼ In asynchronous transmission mode the data items (discrete) in a
stream are transmitted one after the other, but there are no further
timing constraints on when transmission of items should take
place.
◼ For example, a file can be transferred as a data stream, but it is
mostly irrelevant exactly when the transfer of each item
completes.
In synchronous transmission mode, there is a maximum end-to-end
delay defined for each unit in a data stream. Whether a data unit is
transferred much faster than the maximum tolerated delay is not
important. For example, a sensor may sample temperature at a certain rate
and pass it through a network to an operator
◼ In isochronous transmission mode, it is necessary that data units
are transferred on time. This means that data transfer is subject to
a maximum and minimum end-to-end delay, also referred to as
bounded (delay) jitter.
Isochronous transmission mode is particularly interesting for distributed
multimedia systems, as it plays a crucial role in representing audio and
video
b.   A distributed system uses a home-based naming approach to track
Q7
mobile objects.   [10]
a) Explain the role of a home server in maintaining object location
information and the working of home based approach
********** 12 **********
--- page 13 ---
b) Analyze how frequent object migration affects lookup latency and
system performance in the home-based approach.
a) Role of Home Server (3 Marks)
• A home server maintains the permanent record (home location)
of an object.
•   It stores a mapping from object identifier → current location
(address).
•   Clients first contact the home server to locate the object.
• Even if the object moves, the home server keeps track of its
latest position.
• Ensures location transparency for users.
• Working [ 4 marks]
To support mobile entities
home location keeps track of the current location of an entity.
Each mobile host uses a fixed IP address.
All communication to that IP address is initially directed to the
mobile host’s home agent.
Whenever the mobile host moves to another n/w, it requests a
temporary address that it can use for communication (care-of
address) which is registered to home agent.
b) Impact of Frequent Migration (3 Marks)
1. Increased Lookup Latency
• Every lookup must go through the home server, adding extra
delay.
2. Home Server Bottleneck
• Frequent updates and queries overload the home server.
********** 13 **********
--- page 14 ---
3. Higher Update Overhead
• Each movement requires updating the home server, increasing
communication cost.
4. Reduced Performance
Frequent migrations lead to network congestion and slower response
times.
********** 14 **********
````
