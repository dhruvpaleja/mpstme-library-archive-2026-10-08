# Mobile Computing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2024-25 · Final-Exam · Sem 12 · Answer key · paper f9006a1eb0f1

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2024/Sem_12/Final-Exam/Integrated_Computer_7032/Mobile Computing/ANS_Mobile Computing(701CO0C016)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 May 2025
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER ENGINEERING) SIX YEARS
INTEGRATED PROGRAM
Year: VI/Semester XII(Exam Year: 2024-2025)
Subject: Mobile Computing
Date: 10 May 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
CO-2 ;   a.   Compare the efficiency and effectiveness of CDMA, TDMA, and
SO-1 ;   FDMA in addressing the unique challenges of wireless communication [5]
BL-2   environments.
********** 1 **********
--- page 2 ---
Comparison between CDMA , TDMA and FDMA appropriately with
above points = 5 marks
b.   Explain process migration and the state that is transferred during the
migration process. List the steps involved in process migration.
Process migration consists of extracting the state of the process on the
source node, transferring it to the destination node where a new instance
of the process is created, and updating the connections with other
CO-3 ;   processes on communicating nodes.
SO- 1;   [5]
BL-2   The transferred state includes the process’s address space
Execution Point( Register Contents)
Communication State( Open files and message channels)
OS-dependent states
During migration two instances of the migrating process exist: source
instance and destination instance.
********** 2 **********
--- page 3 ---
After migration destination instance becomes migrated process
A process running on another machine is called remote process.
These steps are given bbelow
• A migration request is issued to a remote node
• A process is detached from its source node
• Communication is temporarily redirected
• The process state is extracted
• A destination process instance is created
• State is transferred and imported into a new instance
• Some means of forwarding references maintained
• The new instance is resumed
Definition ( 1 mark) + contents transferred ( 4 marks) + Listing steps( 5
marks)
c.   Distinguish between Indirect TCP and Snooping TCP. Briefly explain
any two advantages and disadvantages of each.
Indirect TCP
no changes to the TCP protocol for hosts connected to the wired
Internet, millions of computers use (variants of) this protocol
optimized TCP protocol for mobile hosts
splitting of the TCP connection at, e.g., the foreign agent into 2 TCP
connections, no real end-to-end connection any longer
CO-3 ;
SO-1 ;   [5]
BL-3   hosts in the fixed part of the net do not notice the characteristics of the
wireless part
Snooping TCP
▪ Data transfer to the mobile host
– FA buffers data until it receives ACK of the MH, FA
detects packet loss via duplicated ACKs or time-out
–   fast retransmission possible, transparent for the fixed
network
▪ Data transfer from the mobile host
– FA detects packet loss on the wireless link via sequence
numbers, FA answers directly with a NACK to the MH
********** 3 **********
--- page 4 ---
– MH can now retransmit data with only a very short delay
▪   Integration of the MAC layer
– MAC layer often has similar mechanisms to those of TCP
–   thus, the MAC layer can already detect duplicated
packets due to retransmissions and discard them
comparison ( 6 marks) + advantages and disadvantages of each ( 4
marks)
d.   Compare and contrast routing in wired networks and ad-hoc networks.
Briefly explain any one application of ad-hoc network.
Points to be considered: ( 4 marks)
CO4- ;   • Asymmetric Links
SO-6 ;   [5]
• Redundant Links
BL-3
• Interference
• Dynamic Topology
Any one application ( 1 mark)
a. Discuss how mobile computing is utilized in emergency applications
and vehicular communication systems? Justify how mobile computing
improve response times, coordination, and communication in
emergency services and vehicular systems.
Emergency Applications ( 3 marks)
• Real-time Communication: Enables first responders to
communicate instantly via mobile networks.
• Location Tracking & GPS: Assists in locating victims and
[10]
Q2   guiding rescue teams.
CO-1;   • IoT-based Monitoring: Wearable and sensor-based monitoring
SO-2;
for real-time health status updates.
BL-2
• Cloud-based Data Access: Emergency personnel can access
medical records and disaster management databases remotely.
• Drone & UAV Integration: Helps in aerial surveillance and
disaster assessment.
Vehicular Communication Systems ( 3 marks)
•   Intelligent Transport Systems (ITS): Enhances road safety by
enabling vehicle-to-vehicle (V2V) and vehicle-to-infrastructure
(V2I) communication.
********** 4 **********
--- page 5 ---
•   Traffic Management & Navigation: Real-time traffic updates
and alternate route suggestions via mobile apps.
• Autonomous & Connected Vehicles: Supports self-driving
technology and connected car ecosystems.
•   Fleet & Logistics Monitoring: GPS-based tracking for efficient
logistics and fleet management
Justification: How Mobile Computing Improves Efficiency ( 4 marks)
Enhanced Response Time: Instant data sharing reduces delays in
emergency response and vehicle navigation.
Improved Coordination: Seamless communication between emergency
teams and traffic management authorities.
Reliable Communication: Ensures uninterrupted connectivity even in
critical conditions like natural disasters.
Data-driven Decision Making: Enables AI-based predictive analysis
for proactive emergency handling.
b.   Illustrate the interaction between Mobile Stations, Base Transceiver
Station ,Base Station Controllers, and the Network and Switching
Subsystem with a labeled diagram, and analyze each of its role in
managing radio transmission.
CO-4; SO-
6;
BL-2
Base Station(BSS)-- The following stations subsystem comprises of
two parts:
********** 5 **********
--- page 6 ---
1.Base Transceiver Station (BTS).
2.Base Station Controller(BSC).
The BSS consists many BSC that connect to a single MSC. Each BSC
controls upto several hundred BTS.
Base Transceiver Station(BTS)-BTS
It has radio transceiver that define a cell and are capable of handling
radio link protocols with MS.
Functions of BTS are
1. Handling radio link protocols
2. Providing FD communication to MS.
Base Station controller(BSC) IT manages radio resources for one or
more BTS.It controls several hundred BTS al are connected to single
MSC.
Functions of BTS are
• To control BTS.
• Radio resource management
• Handoff management and control
• Radio channel setup and frequency hoping
Network Subsystem( NSS)
1.It handles the switching of GSM calls between external networks
and indoor BSC
2.It includes three different data bases for mobility management as
A .HLR (Home Location Register)
B .VLR (Visitor Location Register)
C. AUC (Authentication center)
Diagram ( 4 marks) + Explanation ( 6 marks)
a.   Consider an emergency response   scenario where   traditional
communication networks are unavailable, and a Zone Routing Protocol
[10]
(ZRP) is implemented in an ad-hoc network. Illustrate the step-by-step
Q3
process of routing within and beyond a zone using a labeled diagram.
CO-4; SO-
6; BL-3   Analyze the advantages of ZRP in maintaining communication in an
emergency response network.
1. Step-by-Step Routing Process in ZRP (5 Marks)
********** 6 **********
--- page 7 ---
Step 1: Node Discovery (Intra-zone Routing)
Each node maintains local topology within a predefined zone using
proactive routing.
Step 2: Establishing Routes within the Zone
Nodes communicate using precomputed routes for fast and efficient
data transfer.
Step 3: Detecting Inter-zone Communication Need
If the destination is outside the zone, ZRP switches to reactive routing.
Step 4: Route Query in Border Nodes (Inter-zone Routing)
Border nodes initiate a route request to locate the destination.
Step 5: Route Establishment and Data Transmission
Once the route is determined, data is transmitted efficiently through
optimized paths.
Diagram ( 3 marks) + analyzing advantages ( 2 marks) = 10 marks
b.   Briefly explain how the Android OS architecture differentiate its key
components? Give a labeled diagram to illustrate the layered structure
and explain the role of each layer.
Android OS is designed with a layered architecture that provides
modularity and efficient resource management. The key layers in
CO-1; SO-
Android OS include:
2; BL-3
Linux Kernel
Acts as the foundation of the Android OS.
Manages hardware abstraction, memory, power management, and
process scheduling.
********** 7 **********
--- page 8 ---
Provides essential security features, such as user permissions and
process isolation.
Hardware Abstraction Layer (HAL)
Serves as an interface between the Linux Kernel and higher system
layers.
Allows Android to support multiple hardware components like
cameras, sensors, and Bluetooth.
Native Libraries
Includes C/C++ libraries such as OpenGL for graphics, WebKit for
browsing, and SQLite for data storage.
Enhances multimedia processing with libraries like Media Framework
and Surface Manager.
Android Runtime (ART)
Replaces the older Dalvik Virtual Machine (DVM).
Uses Ahead-of-Time (AOT) compilation for better performance and
efficiency.
Provides key runtime features like garbage collection and memory
optimization.
Application Framework
Contains system services such as Activity Manager, Notification
Manager, and Content Providers.
Manages application lifecycle, resource allocation, and user interface
components.
Applications Layer
Houses pre-installed and user-installed applications.
Runs apps like Phone, Messages, Camera, and third-party
applications.
********** 8 **********
--- page 9 ---
Explanation ( 6 marks) + Diagram 4 marks = 10 marks
a.   Explain the mobile aglet architecture with the help of labelled
diagram. Discuss the key requirements that should be considered
while designing mobile agents.
[10]
Q4
CO-3; SO-
1; BL-2
▪ A context is an Aglet’s workplace.
▪   It is a stationary object that provides a means for
maintaining and managing running Aglets in a uniform
execution environment.
One node in a computer network may host multiple contexts
▪ A proxy is a representative of an Aglet.
▪   Serves as a shield for the aglet
▪   Protects it from direct access to its public methods.
********** 9 **********
--- page 10 ---
The proxy also provides location transparency for the Aglet. That is,
it can hide the real location of the Aglet.
A message is an object exchanged between Aglets through proxies
only.
It allows for synchronous as well as asynchronous message passing
between Aglets.
The message manager allows for concurrency control of incoming
messages.
An itinerary is an Aglet’s travel plan.
An identifier is bound to each aglet. This is globally unique and
immutable throughout the lifetime of the Aglet.
Requirements:
•   Portability
• Ubiquity
• Network Communication
• Server Security
• Agent Security
• Resource Accounting
Aglet architecture Diagram ( 2 marks) + Explanation ( 4 marks) + Any
4 requirements ( 4 marks) = 10 marks
b.   Distinguish between distributed and centralized medium access control
techniques. Discuss the performance metrics used for evaluating the
medium access control technique.
CO-2; SO-
1; BL-3
Normalized throughput
fraction of link capacity used to carry non-retransmitted packets
example with no collisions, 1000 packets/sec
********** 10 **********
--- page 11 ---
with a particular scheme and workload, 250 packets/sec
=> Throughput = 0.25
Mean delay
amount of time a station has to wait before it successfully transmits a
packet depends on the load and the characteristics of the medium.
Stability
•   with heavy load, is all the time spent on resolving
contentions?
• => unstable
•   with a stable algorithm, throughput does not decrease
with offered load
•   if infinite number of uncontrolled stations share a link,
then instability is guaranteed
•   but if sources reduce load when overload is detected, can
achieve stability
Fairness
• no single definition
•   ‘no-starvation’: source eventually gets a chance to send
• max-min fair share
Comparison ( 6 marks) + performance metrics ( 4 marks) = 10 marks
a.   Describe the primary purpose of M-TCP (Mobile –TCP), and how does
it handle disconnections in a mobile network? Briefly explain any two
advantages of M-TCP over I-TCP (Indirect TCP).
Why MTCP?
Improve overall throughput
[10]
To lower the delay
Q5
To maintain end-to-end semantics of TCP,
CO3-; SO-
To provide a more efficient handover.
1; BL-1
Additionally, M-TCP is especially adapted to the problems arising
from lengthy or frequent disconnections
M-TCP splits as I-TCP does
unmodified TCP fixed network to supervisory host (SH)
optimized TCP SH to MH
Supervisory host
********** 11 **********
--- page 12 ---
no caching, no retransmission
monitors all packets, if disconnection detected
set sender window size to 0
sender automatically goes into persistent mode
old or new SH reopen the window
Advantages
maintains semantics, supports disconnection, no buffer forwarding
Disadvantages
loss on wireless link propagated into fixed network
adapted TCP on wireless link( Requires bandwidth manager)
Purpose ( 3 marks) + how it handles disconnections( 5 marks)+
Advantages ( 2 marks) = 10 marks
b.   Describe the Destination-Sequenced Distance Vector (DSDV) protocol
used in ad-hoc networks. With the help of an example, illustrate how
route updates are performed in DSDV. Discuss how the protocol
prevents the count-to-infinity problem.
DSDV
DSDV is Destination Based
No global view of topology
• DSDV is Proactive (Table Driven)
• Each node maintains routing information for all known
CO4-; SO-   destinations
6; BL-2   • Routing information must be updated periodically
•   Traffic overhead even if there is no change in network topology
• Maintains routes which are never used
Keep the simplicity of Distance Vector
Guarantee Loop Freeness
New Table Entry for Destination Sequence Number
Allow fast reaction to topology changes
Make immediate route advertisement on significant changes in routing
table   but   wait   with   advertising   of   unstable   routes
(damping fluctuations)
********** 12 **********
--- page 13 ---
Advertise to each neighbor own routing information
Destination Address
Metric = Number of Hops to Destination
Destination Sequence Number
Rules to set sequence number information
On each advertisement increase own destination sequence number (use
only even numbers)
If a node is no more reachable (timeout) increase sequence number of
this node by 1 (odd sequence number) and set metric = infinity
Update information is compared to own routing table
1. Select route with higher destination sequence number (This ensure to
use always newest information from destination)
2. Select the route with better metric when sequence numbers are equal.
********** 13 **********
--- page 14 ---
Explanation ( 4 marks) + Illustration ( 3 marks) + How to handle count
to infinity ( 3marks) = 10 marks
a.
[10]
Q6
CO-4;   Explain the push and pull operation in Wireless Application protocol
SO6-; BL-   with the help of diagrams.
2
********** 14 **********
--- page 15 ---
Push Operation explanation ( 3 marks ) + Diagram ( 2 marks)
Pull Operation explanation ( 3 marks ) + Diagram ( 2 marks)
b   When a mobile node 𝑁 enters a foreign network, it must obtain a
Care-of Address (CoA) to maintain seamless communication.
Compare and contrast the two primary techniques used for acquiring a
CO-3; SO-   CoA. Describe the mechanism by which the mobile node N notifies its
[10]
1; BL-4   home network of the newly assigned address.
Comparative explanation of Agent Advertisement ( 3 marks) and
Agent Solicitation ( 3marks)
********** 15 **********
--- page 16 ---
Steps of Registration ( 4 marks)
a.   Evaluate the design issues in mobile databases, and propose solutions
to address these challenges. Elaborate how the CODA file system
addresses the fundamental challenges of file access in disconnected and
weakly-connected mobile environments.
Design Issues:
The query optimization process requires selecting the best method of
query evaluation. Mobility results in dynamically changing the
communication costs, which complicate the optimization process.
This complicates query processing since   it become difficult to
determine the optimal location at which to send the result of the query.
User time is a highly valuable commodity in most business applications
today.
Database retrieval techniques should be fast and efficient.
Connection time is the unit of monetary charge in most cellular
systems.
The number of bytes or packets transferred may be the unit of charge.
Energy consumption has to be limited, because battery power is a
[10]
Q7   scarce resource in a handheld and should be optimized
The query must be processed speedily
CO-4; SO-
Solution: Adaptive Query Processing, Energy-Efficient Query
6; BL-2
Execution
How   it handled disconnected ad weakly connected mobile
enviornments:
Server replication
It allows volumes to have read-write replicas at more than one server,
called Volume Storage group (VSG)
At each client what is currently accessible is its Accessible Volume
Storage Group (AVSG)
Venus uses a cache coherence protocol to guarantee that the latest copy
of a file in the AVSG is available to each client by servers notifying
clients when their cached copies are no longer valid
Modifications are propagated in parallel to all AVSG sites and
eventually to missing VSG sites.
Disconnected operation
Venus services file system requests by relying solely on the contents of
the cache
When disconnection ends, Venus propagates modifications and reverts
to server replication.
Different states of Venus
Hoarding: Venus hoards data in anticipation of disconnection
********** 16 **********
--- page 17 ---
Prefetch files while still connected
If the client is connected to server with a strong connection - hoarding
prefetches files currently used.
Coda decides on current cache content using the LRU strategy.
Emulation: Venus acts as pseudo-server, has responsibility for access
and semantic checks. It generates temporary file ids for new objects
Allows read and write access to all files.
System keeps a record of changes files.
After reconnection, CODA compares the replicates with the files on the
server
If Coda notices that two different users have changed a file,
reintegration of this file fails and Coda saves the changes file as a copy
on the server to allow for manual integration.
Reintegration: Venus changes roles from pseudo-server to cache
manager. Venus propagates changes made during emulation and
updates its cache to reflect current server state
Design issues and solutions ( 5 marks) + how it handles disconnected
/weakly connected ( 5 marks) = 10 marks
b.   Compare and contrast Pure ALOHA and Slotted ALOHA protocols in
terms of their operational mechanisms, throughput performance, and
collision handling techniques. Analyze how the introduction of time
synchronization in Slotted ALOHA affects network efficiency
compared to the original ALOHA protocol.
1. Operational Mechanisms
Pure ALOHA:
Nodes transmit data whenever they have data to send, without waiting
for a specific time slot.
If a collision occurs, the node waits for a random backoff period before
retransmitting.
Slotted ALOHA:
CO-2; SO-
1; BL-3   Time is divided into fixed-length slots, and nodes are allowed to
transmit only at the beginning of a time slot.
Reduces the chances of collisions since transmissions are synchronized
to time slots.
2. Throughput Performance
Pure ALOHA:
Maximum achievable throughput is 18.4% (1/2e).
Higher collision probability as nodes can transmit at any time.
Slotted ALOHA:
Maximum achievable throughput is 36.8% (1/e).
Reduces collision probability by ensuring transmissions start only at
designated slots.
3. Collision Handling Techniques
********** 17 **********
--- page 18 ---
Pure ALOHA:
Collisions can occur at any time, leading to more retransmissions.
Uses exponential backoff for retransmission attempts.
Slotted ALOHA:
Collisions are limited to the beginning of time slots, reducing their
frequency.
Nodes that experience a collision wait for the next available time slot.
Impact of Time Synchronization on Network Efficiency
Pure ALOHA:
No time synchronization, leading to a higher probability of collisions.
Inefficient in high-traffic networks due to frequent retransmissions.
Slotted ALOHA:
Requires time synchronization but improves efficiency by halving the
probability of collisions.
Increases   channel   utilization by   ensuring more   successful
transmissions per time slot.
Comparison on 3 points = 6 marks + impact of time
synchronization ( 4marks) = 10 marks
********** 18 **********
````

## 2024-25 · Re-Exam · Sem 12 · Answer key · paper 9200938695d8

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2024/Sem_12/Re-Exam/Integrated_Computer_7032/Mobile Computing/ANS_Mobile Computing(701CO0C016)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Jul 2025
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER ENGINEERING) SIX YEARS
INTEGRATED PROGRAM
Year: VI/Sem 12 Re-exam(Exam Year: 2024-2025)
Subject: Mobile Computing
Date: 07 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 13 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q1
Answer briefly:   [20]
a.   Explain the cause of the hidden node problem in wireless networks and
briefly explain any two methods to prevent it.
Cause of the Hidden Node Problem (2 Marks)
• Occurs when two nodes (A & C) cannot directly communicate but
both attempt to send data to a common node (B).
CO-2 ; SO-   • Node A cannot detect ongoing transmission from Node C, leading [05]
1 ; BL-2
to packet collisions at Node B.
Methods to Prevent the Hidden Node Problem (3 Marks)
• Request to Send / Clear to Send (RTS/CTS) Mechanism (1.5
Marks)
• Using Directional Antennas (1.5 Marks)
b.   Describe the advantages of process migration and distinguish it from
mobile agents.
Any 3 advantages ( 3marks)
Dynamic load distribution
CO-3 ; SO-   Fault resilience   [05]
1; BL-2
Improved system administration
Data access locality
Resource sharing
Difference ( 2marks)
********** 1 **********
--- page 2 ---
Process Migration: Moving an executing process from one system to
another, Controlled by the operating system, Transfers execution state,
memory, and resources.
Mobile Agents: Self-contained code that moves between systems to
perform tasks, Moves autonomously based on pre-defined logic, Mobile
Agents: Carries its own data and execution logic.
c.   Consider the case in mobile IP where packets are continuously sent to the
old FA even after an MN has moved to another FA. Suggest mechanism
to solve this issue. Illustrate with help of diagram.
Binding warning:
If MN has changed it’s FA in some new foreign network.
If a node decapsulates a packet for an MN, but it is not the current FA for
this MN – node sends a warning message.
Warning contains – MN’s home address, target node address- address of
the node that tried to decapsulate packet and send it to MN.
Recipient of warning message (may be HA) will try for new binding in
order to know new COA address of MN.
CO-3 ; SO-   [05]
1 ; BL-3
Explanation of mechanism ( 3 marks) + Diagram ( 2 marks) = 5marks
d.   Analyze the impact of using the DSDV routing protocol in a lightly
loaded network where only a small amount of data is transmitted. Suggest
a possible modification in the protocol to improve efficiency.
Impact ( 3 marks)
• Unnecessary Periodic Updates,
CO4- ; SO-   •   Increased Overhead,   [05]
6 ; BL-3
• Stable Route Maintenance,
• Battery Drain in Mobile Nodes
Modifications for Improved Efficiency ( 2 marks)
• Adaptive Update Interval, Event Triggered Updates, Reduced
Broadcast Frequency
********** 2 **********
--- page 3 ---
a.   Explain the mobile computing architecture with the help of a diagram.
Describe the role of different types of middleware in enabling mobile
computing applications.
Q2
[10]
CO-1; SO-
2; BL-2
Mobile Computing Architecture 3 layers ( 3marks)
Diagram ( 2 marks)
Middleware Definition ( 1 marks)
Role of following 4 types of middleware ( 4 marks)
Message oriented middleware
Transaction Processing middleware
Communication middleware
Transcoding middleware
b.   Illustrate Bluetooth protocol stack and explain how the core protocols
enables personal area networking in mobile environments.
CO-4; SO-
6;   [10]
BL-2
********** 3 **********
--- page 4 ---
Core protocols − This includes Bluetooth radio, Baseband, Link Manager
Protocol (LMP), Logical Link Control and Adaptation Protocol (L2CAP),
and Service Discovery Protocol (SDP).
Radio − This is a physical layer equivalent protocol that lays down the
physical structure and specifications for transmission of radio waves. It
defines air interface, frequency bands, frequency hopping specifications
and modulation techniques.
Baseband − This protocol takes the services of radio protocol. It defines
the addressing scheme, packet frame format, timing, and power control
algorithms.
Link Manager Protocol (LMP) − LMP establishes logical links between
Bluetooth devices and maintains the links for enabling communications.
The other main functions of LMP are device authentication, message
encryption, and negotiation of packet sizes.
Logical Link Control and Adaptation Protocol (L2CAP) − L2CAP
provides adaption between upper layer frame and baseband layer frame
format. L2CAP provides support for both connection-oriented as well as
connectionless services.
Service Discovery Protocol (SDP) − SDP takes care of service-related
queries like device information so as to establish a connection between
contending Bluetooth devices.
Bluetooth protocol stack diagram ( 2 marks) + explanation of 4 protocols
( 8 marks) = 10 marks
a.   Given a network topology with 7 nodes, where nodes are connected as
follows:
A------B, A-----C
B -----D, B -----E
C------F,C------G
D-----G, E------F
If node A wants to send data to node G, describe the steps and sequence
of route request and route reply packets exchanged using DSR (Dynamic
Source Routing) protocol. Consider the case where link between node C
and G fails while A is communicating with G. Show how the DSR
protocol updates the route. Identify alternative routes and the mechanism
Q3   used to handle broken links.
[10]
CO-4; SO-
6; BL-3   Initial Route Discovery from A to G:
Route Request (RREQ) Packet Propagation:
Node A initiates an RREQ packet to find a route to node G.
The packet is broadcasted, and nodes append their addresses as it
propagates.
Possible routes explored:
A → B → D → G
A → C → G
Route Reply (RREP) Packet Transmission:
If G receives an RREQ, it sends an RREP back along the same path.
Assuming both routes exist, G replies via:
********** 4 **********
--- page 5 ---
A → C → G (shortest path)
A → B → D → G (alternative route)
Handling Link Failure (C to G Fails While Transmitting Data):
Error Detection and Route Maintenance:
Node C detects that G is unreachable and sends a Route Error (RERR)
message back to A.
The broken link (C → G) is removed from the route cache.
Route Repair and Alternative Path Selection:
A checks its route cache and finds an alternative valid path:
A → B → D → G
If no cached route exists, A initiates a new Route Discovery process.
Updated Communication via New Route:
A transmits data via the updated path: A → B → D → G
The new route is stored in the cache for future use.
Route discovery ( Route Request and Route Reply ) = 6 marks,
Route update ( RERR) after link failure = 4 marks
b.   Compare and Contrast the Symbian OS and Android OS highlighting the
key features and components.
Key Features
Symbian OS:
Designed for low-power, resource-constrained mobile devices.
Efficient multitasking with real-time capabilities.
Native C++ programming support with a unique event-driven
architecture.
Limited third-party app support due to strict security policies.
Android OS:
Open-source Linux-based operating system.
Supports multitasking and advanced UI features with a large developer
community.
Java-based application framework with support for Kotlin.
Extensive third-party app ecosystem via Google Play Store.
CO-1; SO-
2. System Architecture & Components   [10]
2; BL-3   Symbian OS:
Microkernel-based architecture for efficient resource management.
Separate domains for user applications and system processes for security.
Uses an Active Scheduler for event handling.
Android OS:
Monolithic Linux kernel with built-in security features.
Uses a Dalvik/ART virtual machine for running applications.
Supports various middleware components like media frameworks and UI
libraries.
3. Application & Developer Support
Symbian OS:
Uses native Symbian C++ and Java ME for application development.
Limited support for modern development frameworks.
Android OS:
********** 5 **********
--- page 6 ---
Supports Java, Kotlin, and C++ for app development.
Provides Android Studio as an integrated development environment
(IDE).
4. Security & Updates
Symbian OS:
Had limited security updates and vendor-dependent updates.
Applications required Symbian Signed certification.
Android OS:
Frequent updates and security patches from Google.
Permission-based security model for app access control.
Key Features: 4 Marks System Architecture & Components: 3 Marks+
Application & Developer Support: 2 Marks+ Security & Updates: 1 Mark
a   Explain the life cycle of Aglets with the help of a diagram. Distinguish
between the three types of event-based listeners.
Creation
The creation of an Aglet takes place in a context. The new Aglet is
Q4   assigned an identifier, inserted in the context, and initialized. The Aglet
starts executing as soon as it has successfully been initialized.   [10]
CO-3; SO-   Cloning
1; BL-2
The cloning of an Aglet produces an almost identical copy of the original
Aglet in the same context. The only differences are the assigned
identifier and that the execution restarts in the new Aglet.
Dispatching an Aglet from one context to another will remove it from its
current context and insert it into the destination context, where it will
restart execution (execution threads will not migrate). We say that the
Aglet has been pushed to its new context.
The retraction of an Aglet will pull (remove) it from its current context
and insert it into the context from which the retraction was requested.
The deactivation of an Aglet is the ability to temporarily remove it from
its current context and store it in secondary storage. Activation of an
Aglet will restore it in a context.
********** 6 **********
--- page 7 ---
The disposal of an Aglet will halt its current execution and remove it from
its current context
The aglet programming is event based. Three kinds of listeners exist:
• Clone listener
• Mobility listener
• Persistence listener
Diagram of Life cycle ( 3 marks) + stages ( 4 marks) + role of each
listener ( 3 marks)
b.   Describe the Demand Assigned Multiple Access (DAMA) scheme and
how it manages channel allocation. Compare it with the Slotted ALOHA
scheme.
Improvement of Aloha access systems can also be achieved by
reservation mechanisms and combinations with some (fixed) TDM
patterns.
These schemes typically have a reservation period followed by a
transmission period.
Explicit reservation of slots
Initially regular Aloha; only for reservation of slots
Later data transmission in assigned slots
No collisions during data transmissions
Initial time needed to reserve slots
If there are few or one nodes, time is wasted in reserving slots
If too many contending nodes, slot assignment may take more time
Slots are assigned after Aloha
No mechanism to assign priorities to nodes
CO-2; SO-   A node may always lose the Aloha competition.   [10]
1; BL-3
Different stations on earth try to reserve access time for satellite
transmission.
Collisions during the reservation phase do not destroy data transmission,
but only the short requests for data transmission.
If successful, a time slot in the future is reserved, and no other station is
allowed to transmit during this slot.
Therefore, the satellite collects all successful requests (the others are
destroyed) and sends back a reservation list indicating access rights for
future slots.
All ground stations have to obey this list.
To maintain the fixed TDM pattern of reservation and transmission, the
stations have to be synchronized from time to time.
DAMA is an explicit reservation scheme. Each transmission slot has to
be reserved explicitly.
Comparison: DAMA vs. Slotted ALOHA
DAMA
********** 7 **********
--- page 8 ---
DAMA: Centralized, demand-based Channel allocation.
Controlled access managed by a central authority, High efficiency as
channels are assigned only when needed. Ideal for satellite networks with
limited bandwidth.
Slotted ALOHA: Decentralized, random access. Time-based random
access with pre-defined time slots, Lower efficiency due to frequent
collisions, Suitable for wireless LANs where occasional collisions are
acceptable.
DAMA explanation ( 6 marks ) + comparison with Slotted ALOHA
( 4 marks) = 10 marks
a.   Define DHCP protocol. List and describe the steps involved in assigning
an IP address to a device using DHCP. Illustrate with DHCP process with
the help of the diagram.
Dynamic host configuration protocol – standardized networking protocol
used by servers on an IP network to allocate IP addresses to computer.
Q5
[10]
CO3-; SO-
1; BL-1
Steps with explanation ;DHCP Discover, DHCP Offer, DHCPRequest,
DHCP ACK, DHCP Release
Definition ( 1 mark) + Diagram with steps ( 4 marks) + explanation of
steps ( 5 marks)
b.   Distinguish between reactive and proactive routing protocol. Justify the
need for power aware routing. Briefly describe any 4 performance metrics
used in power aware routing.
CO4-; SO-   Proactive protocols   [10]
6; BL-2
Traditional distributed shortest-path protocols
Maintain routes between every host pair at all times
Based on periodic updates; High routing overhead
********** 8 **********
--- page 9 ---
Example: DSDV (destination sequenced distance vector)
Reactive protocols
Determine route if and when needed
Source initiates route discovery
Example: DSR (dynamic source routing)
Proactive protocols
Always maintain routes
Little or no delay for route determination
Consume bandwidth to keep routes up-to-date
Maintain routes which may never be used
Example DSDV – Destination sequenced distance vector
Reactive protocols
Lower overhead since routes are determined on demand, source initiate
route discovery
Significant delay in route determination
Employ flooding (global search)
Example DSR – Dynamic source routing
Power Aware Routing Uses
• Prolonging Network Lifetime
• Reducing Node Failures
• Enhancing Network Reliability
• Supporting Energy-Constrained Devices
• Minimizing Communication Overhead
Power aware routing Metrics:
• Energy consumption
• Link quality
• Distance
•   Traffic Load
• Battery Life
Distinguish between ( 4 marks) + Justify for power aware routing ( 2
marks) + Power Aware metrics ( 4 marks) = 10 marks
Q6   a.
Summarize the WAP (Wireless Application Protocol) Protocol Stack
CO-4;   with a detailed diagram. Outline the key responsibilities of each layer in [10]
SO6-; BL-   enabling wireless communication.
2
********** 9 **********
--- page 10 ---
WAE : Wireless Application Environment
holds the tools that wireless Internet content developers use.
These include WML and WMLScript.
WSP: Wireless Session protocol:
determines whether a session between the device and the network will
be connection-oriented or connectionless.
In a connection-oriented session, data is passed both ways between the
device and the network; WSP then sends the packet to the Wireless
Transaction Protocol layer.
If the session is connectionless, then WSP redirects the packet to the
Wireless Datagram Protocol layer
WTP - The Wireless Transaction Protocol
It also determines how to classify each transaction request: Reliable two-
way Reliable one-way Unreliable one-way
The WSP and WTP layers correspond to Hypertext Transfer Protocol
(HTTP) in theTCP/IP protocol suite.
WTLS - Wireless Transport Layer Security
provides many of the same security features found in theTransport Layer
Security (TLS) part of TCP/IP
checks data integrity, provides encryption and performs client and
server authentication.
WDP - The Wireless Datagram Protocol works in conjunction with the
network carrier layer
Same as UDP
Offers a consistent interface for the upper layers, in spite of
communication being done using any bearer service.
Bearer services- also called network carriers
Supports any mobile phone systems, including GSM, CDMA etc..
Diagram ( 4 marks) + proper explanation of protocol layers ( 6 marks ) =
10 marks
********** 10 **********
--- page 11 ---
b.   A self-driving vehicle system relies on real-time data transmission
between the vehicle and a remote control center via a wireless network.
The system continuously sends telemetry data, including speed, location,
and sensor readings, while also receiving navigation updates. However,
due to frequent handoffs between cellular towers, the vehicle experiences
temporary disconnections and high packet loss, leading to delays and
inconsistencies in data exchange.
Compare and Contrast how mobile TCP and Indirect TCP handles this
scenario.
Mobile TCP (M-TCP)
Mobile TCP (M-TCP) splits the TCP connection into two parts: an
unmodified TCP connection between the sender and the Supervisory Host
(SH) in the fixed network and an optimized TCP connection between the
SH and the Mobile Host (MH). The SH monitors all packets but does not
cache or retransmit data. When a disconnection is detected, M-TCP sets
the sender’s window size to zero, causing the sender to enter persistent
mode, preventing unnecessary retransmissions. Once the mobile device
reconnects, either the old or a new SH reopens the window, allowing data
transmission to resume smoothly. This approach maintains end-to-end
TCP semantics and supports disconnection handling efficiently.
However, a major drawback is that packet loss on the wireless link is
propagated   into   the   fixed   network,   leading   to   unnecessary
CO-3; SO-
retransmissions. Additionally, M-TCP requires a bandwidth manager to
1; BL-4   optimize TCP performance over wireless connections. While M-TCP
reduces delay by preventing unnecessary congestion control activation,
its effectiveness is limited in highly dynamic environments due to its
reliance on end-to-end TCP mechanisms.
Indirect TCP (I-TCP)
Indirect TCP (I-TCP) addresses mobility challenges by splitting the TCP
connection at the base station, creating a stable wired TCP link between
the sender and the base station and a separate wireless TCP link between
the base station and the mobile device. This division prevents the sender
from detecting disruptions in the wireless network, as the base station
locally handles retransmissions and maintains the TCP connection. By
isolating wireless issues from the core network, I-TCP ensures
continuous connectivity and minimizes the impact of frequent handoffs.
Unlike M-TCP, which propagates wireless packet losses into the fixed
network, I-TCP confines retransmission management to the wireless
segment, reducing unnecessary retransmissions from the sender. This
results in lower end-to-end latency and improved reliability in high-
mobility environments. While I-TCP does not maintain strict end-to-end
TCP semantics, its ability to prevent disruptions makes it more suitable
for self-driving vehicle systems that experience frequent handoffs and
varying wireless conditions.
Comparison of M-TCP and I-TCP 5 marks each ( 5* 2 =10 marks)
Q7   a.
Describe the client structure in Coda file system with a labelled diagram.
[10]
CO-4; SO-   List and briefly explain any two design rationale of Coda file system.
6; BL-2
********** 11 **********
--- page 12 ---
Venus designed at user-level rather than kernel level.
CODA uses a small in-kernel mini cache, which filters out many Venus-
kernel interactions
System calls on a CODA object are first forwarded for service to the mini
cache
If cannot service, mini cache calls Venus to service the call, by contacting
the remote servers.
Control then returns to the application program from Venus via the mini
cache
Mini cache states updated by Venus
Design rationale: Any two
• Conventional off-the-shelf hardware
• Preserving transparency
•   Scalability
• Portable workstations
•   Availability
• Consistency
Diagram of Coda Client Structure (2 marks) + explanation of Coda Client
Structure ( 4 marks) + Design Rationale ( 4 marks, 2 marks for each)
b.   Explain multiple access with collision avoidance (MACA). Examine the
possibility of collision in MACA scheme. Briefly explain any one
drawback of MACA.
Multiple access with collision avoidance (MACA)
Solves hidden\exposed terminal problem.
CO-2; SO-   Does not need a base station (central controller)
1; BL-3   Still a random access aloha scheme – with dynamic reservation.
MACA
When a node wants to transmit a data packet, it first transmit a RTS
(Request To Send) frame.
The receiver node, on receiving the RTS packet, if it is ready to receive
the data packet, transmits a CTS (Clear to Send) packet.
********** 12 **********
--- page 13 ---
Once the sender receives the CTS packet without any error, it starts
transmitting the data packet.
If a packet transmitted by a node is lost, the node uses the binary
exponential back-off (BEB) algorithm to back off a random interval of
time before retrying.
MACA avoids the problem of hidden terminals
A and C want to send to B
A sends RTS first.
B will receive RTS .
C cannot here RTS send by A.
B will send CTS to A.
C can listen to CTS send by B.
C waits after receiving CTS from B
MACA avoids the problem of exposed terminals
B wants to send to A, C
want to send to D.
B will send RTS to A.
RTS will be received by C also.
A will send CTS to B. C can’t listen CTS from A.
So C will continue its transmission to D.
Collision can occur during sending of RTS.
Both A and C could send RTS to B at same time.
RTS is very small compared to the data transmission, so the
probability of a collision is much lower.
B resolves contention and can acknowledge on station in the CTS (if
it was able to recover the RTS at all).
No transmission allowed without an appropriate CTS.
Problem with MACA:
Overheads associated with the RTS and CTS transmissions.
For short and time critical data packets – not feasible.
Explanation of MACA ( 5 marks) + 3 marks ( description of how
collision can handle ) + Problems of MACA ( 2 marks) = 10 marks
********** 13 **********
````
