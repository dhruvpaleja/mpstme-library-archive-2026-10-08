# Computer Networks: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper 0a47f515df5b

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Computer Networks/ANS_Computer Networks(703AI0C004)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 Nov 2025
- Text: text (24 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester I(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 27 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 24 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1 ) a) “SCTP protocol is ideal for applications like telephony over the Internet and signalling in
mobile networks.” Justify
1 mark – Definition / Introduction
SCTP (Stream Control Transmission Protocol) is a reliable, message-oriented Transport Layer
protocol that combines the features of TCP and UDP.
It was originally designed for telephony signaling (SS7 over IP) but is now used for applications
requiring high reliability and timing efficiency, such as VoIP and multimedia systems.
1 mark – Key Concept
SCTP provides reliable, connection-oriented communication like TCP, but it differs by supporting
multi-streaming and multi-homing within a single connection (called an association).
It transmits data in the form of messages (chunks) rather than a continuous byte stream.
2 marks – Step-by-Step Explanation of SCTP Services
Service   Explanation
1. Reliable Data   SCTP ensures that data is delivered error-free, in sequence, and without
Transfer   duplication using acknowledgment and retransmission mechanisms.
2. Message-Oriented   Unlike TCP’s byte stream, SCTP preserves message boundaries, meaning
Communication   each message sent by the sender is received exactly as a unit by the receiver.
********** 1 **********
--- page 2 ---
Service   Explanation
SCTP divides data into multiple independent streams within one
3. Multi-Streaming   association. If one stream experiences loss, it does not block others —
reducing head-of-line blocking.
SCTP supports multiple IP addresses (interfaces) per endpoint. If one path
4. Multi-Homing   fails, data can automatically switch to another available path — providing
fault tolerance.
5. Flow and Congestion SCTP uses TCP-like flow and congestion control mechanisms, preventing
Control   buffer overflow and ensuring fair use of network bandwidth.
6. Security (Four-Way SCTP uses a four-way handshake with a cookie mechanism to protect
Handshake)   against SYN-flooding and DoS attacks, making it more secure than TCP.
1 mark – Conclusion
In summary, SCTP offers reliable, secure, and efficient data transfer with unique features such as
multi-streaming and multi-homing. It enhances performance and resilience in real-time
communication systems like VoIP, video conferencing, and signaling applications. Hence the
protocol is ideal for applications like telephony over the Internet and signaling in mobile networks.
Q1 ) b) With the help of diagram elaborate OSI Model.
Ans) 1 mark – Definition / Introduction
The OSI (Open Systems Interconnection) Model is a conceptual framework developed by the ISO
(International Organization for Standardization) that standardizes how communication takes place
between two networked systems.
It divides the entire communication process into seven distinct layers, each having specific functions.
1 mark – Key Concept
The OSI model helps different systems communicate irrespective of their underlying architectures by
defining clear layer-wise responsibilities.
Each layer provides services to the layer above and receives services from the layer below.
2 marks – Diagram + Explanation
OSI Model Diagram
7. Application Layer ← User interface (e.g., HTTP, FTP)
6. Presentation Layer ← Data translation, encryption
5. Session Layer   ← Session management, synchronization
4. Transport Layer ← Reliable delivery (TCP, UDP)
3. Network Layer   ← Logical addressing & routing (IP)
2. Data Link Layer   ← Framing, error detection (MAC)
********** 2 **********
--- page 3 ---
1. Physical Layer   ← Bits transmission (Cables, Signals)
Layer-Wise Explanation
Layer   Functions   Examples
1. Physical   Deals with hardware transmission of raw bits over physical   Ethernet cables,
Layer   media (voltages, cables, connectors).   hubs
2. Data Link   Provides error detection, framing, and flow control. Divided   Switches, MAC
Layer   into MAC and LLC sublayers.   addresses
3. Network   Handles logical addressing and path selection (routing)   IP, ICMP,
Layer   between source and destination.   Routers
4. Transport
Ensures reliable, end-to-end delivery and flow control.   TCP, UDP
Layer
Manages sessions between communicating systems; establishes,
5. Session Layer   NetBIOS, RPC
maintains, and terminates connections.
6. Presentation   Translates data into a format understandable by the application   JPEG, SSL,
Layer   layer; handles encryption, compression, encoding.   ASCII
7. Application   Provides network services to end-users, such as file transfer,   HTTP, FTP,
Layer   email, web browsing, etc.   DNS, SMTP
1 mark – Conclusion
Thus, the OSI model provides a structured approach for understanding and designing network
systems.
It ensures interoperability, modularity, and troubleshooting efficiency by clearly separating
networking functions into seven layers.
Q1 c) With the help of example explain IPv6 addressing, notation and its types.
1 mark
• Ans) An IPv6 address consists of 16 bytes (octets); it is 128 bits long.
• IPv6 addresses are represented using two notations: Binary and Colon hexadecimal.
2 marks
• The colon hexadecimal divides the address into eight sections each made of four hexadecimal
digits separated by colons.
Original Address:8000:0000:0000:0000:0123:4567:89AB:CDEF
Compressed Address: 8000::123:4567:89AB:CDEF
• The address space of IPv6 contains 2128 addresses. This address is 296 times the IPv4 address.
2 marks
Address Types: (Explain in short)
1. Unicast Address
2. Anycast Address
3. Multicast Address
Q1 d) Explain following networking devices Hub, Repeater, Bridge, Switch, and Router
********** 3 **********
--- page 4 ---
Ans) 1. Hub (½ mark)
• A Hub is a basic networking device that connects multiple computers in a LAN.
•   It broadcasts data to all connected devices, whether they need it or not.
• Works at the Physical Layer (Layer 1) of the OSI model.
Example: Connecting 4–5 PCs in a small office.
2. Repeater (½ mark)
• A Repeater is used to regenerate and amplify weak signals in a network cable.
•   It helps to extend the distance over which data can travel.
• Works at the Physical Layer (Layer 1).
Example: Used in long Ethernet cables to boost signal strength.
3. Bridge (1 mark)
• A Bridge connects two or more LAN segments and filters data based on MAC addresses.
•   It reduces network traffic by forwarding only necessary data.
• Works at the Data Link Layer (Layer 2).
Example: Connecting two LANs in different rooms of a building.
4. Switch (1 mark)
• A Switch is an intelligent device that connects multiple devices in a LAN and sends data only to
the intended device.
•   It uses MAC addresses to forward data efficiently.
• Works at the Data Link Layer (Layer 2) (some advanced switches also work at Layer 3).
Example: Commonly used in offices and schools for efficient LAN connections.
5. Router (2 marks)
• A Router connects multiple networks together (e.g., a home network to the Internet).
•   It forwards data based on IP addresses and chooses the best path for data delivery.
• Works at the Network Layer (Layer 3).
Example: The Wi-Fi router in your home that connects to the Internet.
Q2 a)Explain how the collision can be avoided by CSMA/CA
Ans) 1 mark – Definition / Introduction
CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance) is a network access method
used mainly in wireless networks (like Wi-Fi) to avoid data collisions during transmission.
It helps ensure that two devices do not send data at the same time.
********** 4 **********
--- page 5 ---
1 mark – Key Concept
Unlike CSMA/CD (Collision Detection) used in wired Ethernet, CSMA/CA focuses on avoiding
collisions before they happen, because in wireless communication, collisions cannot be detected
easily.
2 marks – Step-by-Step Working of CSMA/CA
Step 1: Carrier Sensing
Before sending data, the device listens to the channel to check if it is idle (free) or busy.
If the channel is busy → the device waits.
Step 2: Wait for Interframe Space (IFS)
Once the channel becomes idle, the device waits for a short random time called Interframe Space (IFS)
to ensure no other device has started transmitting.
Step 3: Backoff Mechanism
If multiple devices are waiting, each chooses a random backoff time.
The device with the shortest wait transmits first — preventing simultaneous transmissions.
Step 4: RTS/CTS (Optional Collision Avoidance Technique)
• The sender sends a Request To Send (RTS) signal to the receiver.
• The receiver replies with Clear To Send (CTS).
• Other devices hearing RTS or CTS stay silent, preventing collisions.
Step 5: Data Transmission
After receiving CTS, the sender transmits data safely — reducing the chance of collisions.
1 mark – Conclusion
✅ In summary:
CSMA/CA avoids collisions by:
•   Listening before sending (Carrier Sense)
• Using random backoff timing
• Using RTS/CTS handshakes
This method ensures efficient and collision-free communication in wireless LANs (like IEEE 802.11
/ Wi-Fi).
Q2 b) An ISP is granted a block of addresses 172.16.0.0/16 (65,536 addresses).
The ISP must distribute these addresses to three classes of customers:
• Group A: 30 corporate customers; each needs 1,000 addresses.
• Group B: 60 medium business customers; each needs 200 addresses.
********** 5 **********
--- page 6 ---
• Group C: 120 small-office customers; each needs 40 addresses.
Design the subblocks.
For each group, determine:
• The subnet mask used per customer.
•   Total addresses consumed by the group.
• Remaining addresses in the /16 block.
Show your calculations and state the remaining contiguous address count.
Ans) Step 1 — Choose subnet size per customer
• Group A — need 1,000 → smallest power-of-two ≥ 1000 is 1024 → /22
o /22 size = 232−22=10242^{32-22}=1024232−22=1024 addresses
o Subnet mask: 255.255.252.0
• Group B — need 200 → smallest power-of-two ≥ 200 is 256 → /24
o /24 size = 232−24=2562^{32-24}=256232−24=256 addresses
o Subnet mask: 255.255.255.0
• Group C — need 40 → smallest power-of-two ≥ 40 is 64 → /26
o /26 size = 232−26=642^{32-26}=64232−26=64 addresses
o Subnet mask: 255.255.255.192
Step 2 — Total addresses consumed by each group
Use total addresses per allocated subnet (network + broadcast included):
• Group A: 30 customers × 1024 = 30,720 addresses
• Group B: 60 customers × 256 = 15,360 addresses
• Group C: 120 customers × 64 = 7,680 addresses
Total allocated = 30,720 + 15,360 + 7,680 = 53,760 addresses
Step 3 — Remaining addresses in /16
•   /16 total = 65,536 addresses
• Remaining = 65,536 − 53,760 = 11,776 addresses unused.
Step 4 — Contiguous allocation (largest-first) and ranges
If we allocate blocks contiguously starting at 172.16.0.0, allocate Group A (largest subnets) first, then
Group B, then Group C:
Group A (30 × /22 = 30 × 1024 = 30,720 addresses)
•   Start: 172.16.0.0
• Count in /24s: 30,720 / 256 = 120 /24s → covers third-octet 0 through 119.
• Used range: 172.16.0.0 — 172.16.119.255
Next free address: 172.16.120.0
********** 6 **********
--- page 7 ---
Group B (60 × /24 = 60 × 256 = 15,360 addresses)
•   Start: 172.16.120.0
• 60 /24s → covers third-octet 120 through 179.
• Used range: 172.16.120.0 — 172.16.179.255
Next free address: 172.16.180.0
Group C (120 × /26 = 120 × 64 = 7,680 addresses)
•   Start: 172.16.180.0
• 7,680 /256 = 30 /24s → covers third-octet 180 through 209.
• Used range: 172.16.180.0 — 172.16.209.255
Next free address: 172.16.210.0
Remaining unused (contiguous)
•   Start: 172.16.210.0
• End: 172.16.255.255
• Count: 11,776 addresses (matches calculation above)
Step 5 — Remaining contiguous block expressed as CIDR blocks
We can represent the remaining contiguous range 172.16.210.0 – 172.16.255.255 (11,776 addresses) as
a set of aligned CIDR blocks (greedy/alignment decomposition):
• 172.16.210.0/23 → covers .210–.211 (512 addresses)
• 172.16.212.0/22 → covers .212–.215 (1,024 addresses)
• 172.16.216.0/21 → covers .216–.223 (2,048 addresses)
• 172.16.224.0/19 → covers .224–.255 (8,192 addresses)
512 + 1,024 + 2,048 + 8,192 = 11,776 addresses (exact).
Q3 a) Explain how the Bellman–Ford algorithm is implemented in RIP (Routing Information Protocol).
Ans) 1. Introduction – 1 Mark
The Routing Information Protocol (RIP) is a Distance Vector Routing Protocol that uses the
Bellman–Ford algorithm to determine the shortest path (in hops) to each destination network.
Each router periodically exchanges routing tables with its immediate neighbors to keep its route
information updated.
2. Bellman–Ford Algorithm in RIP – 3 Marks
Principle:
RIP applies the Bellman–Ford shortest-path algorithm to compute the minimum distance (hop count)
between routers.
Bellman–Ford Formula:
D(X,Y)=min⁡[C(X,N)+D(N,Y)]D(X, Y) = \min [C(X, N) + D(N, Y)]D(X,Y)=min[C(X,N)+D(N,Y)]
Where:
• D(X,Y)D(X, Y)D(X,Y): Cost from router X to destination Y
• C(X,N)C(X, N)C(X,N): Cost from X to its neighbor N (usually 1 hop)
• D(N,Y)D(N, Y)D(N,Y): Cost from neighbor N to destination Y
********** 7 **********
--- page 8 ---
Step-by-Step Implementation
Step 1: Initialization
Each router knows only the distance to its directly connected networks (cost = 1). All others are set to ∞
(unreachable).
Step 2: Table Exchange
Routers periodically broadcast their routing tables to neighbors via UDP port 520 (every 30 seconds).
Step 3: Update Calculation (Applying Bellman–Ford)
When a router receives a neighbor’s routing table:
•   It adds 1 to the neighbor’s distance (since it’s one hop away).
•   It updates its own table if the new route has a smaller hop count.
Step 4: Convergence
After repeated updates, all routers agree on the shortest path — this state is called network
convergence.
Step 5: Failure Handling
If a route becomes unreachable, RIP sets the hop count to 16 (infinity) — meaning "destination
unreachable."
3. Problems Faced by RIP – 3 Marks
Problem   Description
1. Count-to-Infinity When a route fails, routers keep increasing the hop count indefinitely before
Problem   realizing the destination is unreachable.
It takes a long time for all routers to learn about a topology change or network
2. Slow Convergence
failure.
RIP allows a maximum hop count of 15; beyond that, the network is
3. Limited Hop Count
considered unreachable — not suitable for large networks.
4. High Bandwidth   RIP broadcasts the entire routing table every 30 seconds, consuming
Usage   unnecessary bandwidth.
Temporary loops can occur due to incorrect or outdated routing table
5. Routing Loops
information.
4. Techniques Used to Overcome RIP Problems – 2 Marks
Technique   Purpose / How It Helps
Prevents routing information from being sent back in the direction it came
1. Split Horizon
from — avoids loops.
Sends back the route to a neighbor but marks it as infinite (unreachable) —
2. Poisoned Reverse
breaks count-to-infinity cycles.
When a route is marked as unreachable, updates about it are ignored for a
3. Hold-Down Timer
fixed time to avoid false route restorations.
Instead of waiting 30 seconds, routers immediately send updates when a
4. Triggered Updates
change occurs — helps in faster convergence.
********** 8 **********
--- page 9 ---
Technique   Purpose / How It Helps
5. Use of Infinity (Hop
Prevents endless looping by setting an upper limit on route distances.
Count = 16)
5. Example Diagram – 1 Mark
(2)
(3 hops)
• Suppose link A–B fails.
• B informs A using RIP update (Bellman–Ford) that route is now unreachable (hop count = 16).
•   Split Horizon + Poisoned Reverse ensure that A does not re-advertise B’s route back to B —
avoiding infinite looping.
6. Conclusion – 1 Mark
In summary, RIP implements the Bellman–Ford algorithm to compute shortest paths based on hop
counts, making it simple and easy to implement.
However, issues like slow convergence and count-to-infinity are major drawbacks.
These are mitigated through mechanisms like Split Horizon, Poisoned Reverse, Hold-Down Timers,
and Triggered Updates, which make RIP more stable for small to medium-sized networks.
Q3) b) Describe DNS in detail with the help of example
Ans) 1. Introduction – 1 Mark
The Domain Name System (DNS) is a hierarchical and distributed naming system used on the
Internet to translate human-readable domain names (like www.google.com) into machine-readable
IP addresses (like 142.250.183.78).
It acts as the “phonebook of the Internet”, enabling users to access websites using names instead of
numerical addresses.
2. Key Concept / Purpose – 2 Marks
• Computers communicate using IP addresses, but humans find domain names easier to
remember.
• DNS provides a mapping service between domain names and IP addresses.
•   It follows a client-server model where a DNS client (resolver) sends queries to DNS servers to
find the corresponding IP.
Functions of DNS:
1. Name Resolution – Converts domain names to IP addresses.
2. Host Aliasing – Maps multiple names to a single IP.
3. Load Distribution – Maps one domain to multiple IPs for balancing traffic.
4. Mail Exchange (MX Records) – Directs emails to the correct mail servers.
3. Structure of DNS (Hierarchy) – 2 Marks
DNS is organized in a hierarchical tree structure:
********** 9 **********
--- page 10 ---
Levels:
1. Root Domain (.) — The top-most level of DNS.
2. Top-Level Domains (TLDs) — Examples: .com, .org, .edu, .in, .net.
3. Second-Level Domains — Examples: google in google.com.
4. Subdomains — Example: mail.google.com.
5. Hostnames — The actual machine or service (e.g., www).
4. Step-by-Step Working of DNS – 3 Marks
example:
User enters: www.example.com in a web browser.
Step 1: DNS Query Initiation
The client (resolver) checks its local DNS cache for www.example.com.
If not found, it sends a recursive query to the Local DNS Server (LDNS) provided by the ISP.
Step 2: Root Server Lookup
If the LDNS doesn’t know the address, it contacts a Root DNS server, which responds with the IP
address of the .com TLD server.
Step 3: TLD Server Lookup
The LDNS then queries the .com TLD server, which responds with the IP address of the authoritative
server for example.com.
Step 4: Authoritative Name Server Lookup
The LDNS queries the authoritative DNS server for example.com, which finally provides the IP
address (say 93.184.216.34) for www.example.com.
Step 5: Response to Client
The LDNS stores this mapping in its cache and returns the IP address to the user’s browser.
The browser then uses this IP to establish a TCP connection to the web server and fetch the webpage.
5. Example Illustration – 2 Marks
Example: Resolving www.google.com
Step Query Sent To   Response Received
1   Local DNS   No record found → forwards request
2   Root DNS Server   Returns IP of .com TLD server
3   .com TLD Server   Returns IP of google.com authoritative server
4   Authoritative Server Returns IP 142.250.183.78 for www.google.com
5   Local DNS   Sends IP back to browser → connection established
6. Conclusion – 1 Mark
In conclusion, DNS is a distributed database system that efficiently translates domain names into IP
addresses, ensuring smooth Internet communication.
It enhances user experience by allowing websites to be accessed via easy-to-remember names, while
managing billions of queries per day with speed, redundancy, and scalability.
Q4a) Discuss Virtual circuit networks.
********** 10 **********
--- page 11 ---
Ans) 1. Introduction – 1 Mark
A Virtual Circuit Network (VCN) is a type of packet-switched network where a logical path (called
a virtual circuit) is established before data transmission between the sender and receiver.
Even though the path is logical (not physically dedicated), all packets follow the same route,
maintaining order and reliability — similar to a telephone connection but implemented in software.
2. Key Concept / Principle – 2 Marks
•   In a Virtual Circuit Network, communication occurs in three phases:
1. Connection Setup – A route is established between the source and destination.
2. Data Transfer – Data packets follow that predefined route.
3. Connection Teardown – The path is released after communication ends.
• Each packet contains a Virtual Circuit Identifier (VCI) instead of a full destination address.
This reduces overhead and speeds up packet forwarding.
• Examples: Frame Relay, ATM (Asynchronous Transfer Mode), and X.25 networks use virtual
circuits.
3. Characteristics of Virtual Circuit Networks – 2 Marks
Feature   Description
Connection-Oriented A logical path is established before data transfer begins.
Fixed Route   All packets follow the same route, preserving sequence.
Header Simplicity   Only a short VCI is used instead of a full address.
Reliability   Connection setup ensures that both ends are ready for communication.
Error Control   Achieved through acknowledgments and retransmissions.
Congestion Control Easier, since the network knows which paths are active.
4. Step-by-Step Working – 3 Marks
Phase 1: Connection Setup
• The sender sends a setup request to establish a virtual path.
• Each router along the path stores a mapping between incoming and outgoing VCI values.
• Once confirmed, both ends agree on the VCI.
Phase 2: Data Transfer
• Data is divided into packets.
• Each packet carries only the VCI, not the destination address.
•   Intermediate routers forward packets based on VCI lookup tables.
• Packets arrive in order since they follow the same route.
Phase 3: Connection Teardown
•   After the communication is complete, a teardown message is sent.
•   All routers on the path delete the VCI entries, freeing up resources.
********** 11 **********
--- page 12 ---
5. Example Diagram – 1.5 Marks
Sender ---- Router1 ---- Router2 ---- Receiver
Explanation:
• A virtual circuit with ID 12 is established across routers.
•   All packets from the sender to receiver use this same logical path.
6. Advantages and Disadvantages – 1.5 Marks
Advantages   Disadvantages
Reliable and ordered data delivery   Delay during setup phase
Easier error and congestion control   Failure of one node breaks the circuit
Low header overhead (VCI instead of full address) Less flexible than datagram networks
7. Conclusion – 1 Mark
In conclusion, Virtual Circuit Networks provide a connection-oriented service that combines the
reliability of circuit switching with the flexibility of packet switching.
They are well-suited for applications requiring consistent performance and ordered delivery, such as
video conferencing, VoIP, and ATM-based networks.
Q4b) Explain UDP operations and use of UDP protocol
Ans) Introduction – 1 Mark
UDP (User Datagram Protocol) is a connectionless, transport layer protocol in the TCP/IP model.
It provides a simple way to send messages, called datagrams, between devices without establishing a
connection.
UDP is defined in RFC 768 and is mainly used where speed and efficiency are more important than
reliability.
2. Key Concept / Principle – 2 Marks
• UDP is connectionless, meaning data is sent directly to the receiver without a prior handshake.
•   It is unreliable — there are no acknowledgments, retransmissions, or error recovery.
• However, UDP has low overhead, making it faster and suitable for real-time applications.
Features of UDP:
1. Provides process-to-process communication using port numbers.
2. Supports one-to-one, one-to-many, and broadcast transmission.
3. Preserves message boundaries (unlike TCP, which uses a stream of bytes).
4. Operates over IP (Internet Protocol) and adds minimal control information.
3. UDP Packet Format – 2 Marks
Field   Description
Source Port (16 bits)   Identifies the sending application.
********** 12 **********
--- page 13 ---
Field   Description
Destination Port (16 bits) Identifies the receiving application.
Length (16 bits)   Total length of the UDP segment (header + data).
Checksum (16 bits)   Used for error detection (optional).
Data   The actual information being sent.
4. Step-by-Step UDP Operations – 3 Marks
Step 1: Data Preparation
The application (e.g., video app, DNS query) passes the message to UDP.
UDP adds its header (source port, destination port, length, checksum).
Step 2: Transmission
The UDP segment is passed down to the IP layer, which adds the IP header and delivers it as an IP
datagram to the receiver’s IP address.
Step 3: Reception
The receiver’s IP layer removes the IP header and passes the UDP segment to the UDP layer, which
checks the checksum for errors.
Step 4: Delivery to Application
Based on the destination port number, UDP delivers the data to the correct application (e.g., DNS,
TFTP, VoIP).
5. Example of UDP Communication – 1 Mark
Example: When a user performs a DNS lookup for www.example.com:
1. The DNS client sends a small UDP query to port 53 (DNS server).
2. The server responds with the IP address in another UDP message.
Since it’s a small and quick exchange, there’s no need for a connection.
6. Uses of UDP Protocol – 1.5 Marks
Application / Service   Port   Description
DNS (Domain Name System)   53   For fast name-to-IP translation
DHCP (Dynamic Host Configuration
67/68   Assigns IP addresses to clients
Protocol)
TFTP (Trivial File Transfer Protocol)   69   Simple file transfer protocol
VoIP / Video Streaming   Dynamic Real-time communication, low delay
Quick response times more important than
Online Gaming   Dynamic
reliability
7. Advantages and Disadvantages – 1 Mark
Advantages   Disadvantages
Faster data transfer (no connection setup) No reliability or acknowledgment
Low overhead and lightweight   No flow or congestion control
Suitable for real-time applications   Packets may arrive out of order or get lost
********** 13 **********
--- page 14 ---
8. Conclusion – 0.5 Mark
In summary, UDP provides a fast and efficient way to send data across networks with minimal
overhead.
It is ideal for real-time or time-sensitive applications where a few lost packets are tolerable, such as
streaming, gaming, and VoIP.
Q5 a) Describe logical to physical address mapping using ARP(Also give example).
Ans) Introduction – 1 Mark
In computer networks, every device on a LAN has two types of addresses:
• A logical address (IP address) – used by the Network Layer for routing.
• A physical address (MAC address) – used by the Data Link Layer for actual delivery of
frames.
However, devices communicate physically using MAC addresses, not IP addresses.
The Address Resolution Protocol (ARP) is used to map a logical (IP) address to its corresponding
physical (MAC) address.
2. Key Concept / Definition of ARP – 2 Marks
• ARP (Address Resolution Protocol) is a Network Layer protocol (defined in RFC 826) used
in IPv4 networks.
•   It operates between the Data Link Layer and Network Layer of the OSI model.
• ARP enables a device to find the MAC address of another device on the same network when
only its IP address is known.
Purpose:
ARP = “Who has this IP address? Please tell me your MAC address.”
Used in: Ethernet and Wi-Fi networks.
3. ARP Packet Format – 1.5 Marks
Important Fields:
• Operation: ARP Request (1) or ARP Reply (2)
• Sender MAC/IP: Address of the sender
• Target IP/MAC: The address being queried
4. Step-by-Step Working of ARP – 3 Marks
Let’s understand how ARP maps IP → MAC within a local area network (LAN):
Step 1: ARP Request
• Suppose Host A (192.168.1.10) wants to send data to Host B (192.168.1.20).
• Host A knows Host B’s IP address, but not its MAC address.
• Host A broadcasts an ARP Request frame:
“Who has 192.168.1.20? Tell 192.168.1.10.”
********** 14 **********
--- page 15 ---
Step 2: ARP Broadcast
• This request is broadcast to all devices in the LAN using the address FF:FF:FF:FF:FF:FF.
Step 3: ARP Reply
• Host B (192.168.1.20) recognizes its own IP and responds with an ARP Reply directly to Host
A:
“I am 192.168.1.20, my MAC address is 00-AA-BB-CC-DD-EE.”
Step 4: Cache Update
• Host A stores this mapping (192.168.1.20 → 00-AA-BB-CC-DD-EE) in its ARP cache for
future use.
• Next time, A can send data directly to B using the stored MAC address.
Step 5: Frame Delivery
• Host A encapsulates the packet in a frame with destination MAC = 00-AA-BB-CC-DD-EE and
sends it to B.
5. Example with Diagram – 2 Marks
Example:
Host IP Address   MAC Address
Host A 192.168.1.10 00-11-22-33-44-55
Host B 192.168.1.20 00-AA-BB-CC-DD-EE
ARP Operation:
[Host A] ---ARP Request---> (Broadcast: FF:FF:FF:FF:FF:FF)
"Who has 192.168.1.20?"
[Host B] ---ARP Reply---> (Unicast to Host A)
"192.168.1.20 is at 00-AA-BB-CC-DD-EE"
Result:
Host A now maps → 192.168.1.20 : 00-AA-BB-CC-DD-EE
and uses it for direct communication.
6. Advantages and Limitations – 0.5 Marks
Advantages:
•   Simplifies communication by automatically resolving IP-to-MAC mappings.
• Reduces manual configuration.
Limitations:
• Can be exploited for ARP spoofing or poisoning attacks if not protected.
********** 15 **********
--- page 16 ---
7. Conclusion – 0.5 Marks
In summary, ARP plays a vital role in logical-to-physical address mapping, enabling seamless
communication between devices in a LAN.
By dynamically translating IP addresses to MAC addresses, ARP ensures that data frames are
correctly delivered at the link layer.
Q5b ) Describe logical to physical address mapping using ARP (Also give example).
i) Why are error detection and correction techniques important in digital communication systems?
ii) Two binary codewords are used in a communication system:
C₁ = 1001101
C₂ = 1101001
Compute the Hamming distance between C₁ and C₂.
iii) A new codeword C₃ = 1011001 is added to the set.
Compute the pairwise Hamming distances between C₃ and the other codewords.
iv) Based on the minimum Hamming distance of the code, determine how many errors the code can
detect and correct.
Justify your answer.
Ans) Error detection and correction techniques are essential in digital communication systems
because they ensure data integrity during transmission. Noise and other interferences can
cause bit errors, so these techniques help identify and fix such errors to maintain reliable
communication.
[1 mark for concept of integrity, 1 mark for cause (noise/interference)]
ii)
Given:
C₁ = 1001101
C₂ = 1101001
To find the Hamming distance, compare bit-by-bit and count the differences:
C₁: 1 0 0 1 1 0 1
C₂: 1 1 0 1 0 0 1
↑ ↑   ↑
Differences at positions: 2, 5, 7 → Total = 3 differences
Hamming distance = 3
[2 marks]
********** 16 **********
--- page 17 ---
iii)
C₃ = 1011001
Compare with C₁ (1001101):
C₁: 1 0 0 1 1 0 1
C₃: 1 0 1 1 0 0 1
↑ ↑
Differences at positions: 3, 5 → Distance = 2
Compare with C₂ (1101001):
C₂: 1 1 0 1 0 0 1
C₃: 1 0 1 1 0 0 1
↑ ↑
Differences at positions: 2, 3 → Distance = 2
Hamming distances:
• d(C₁, C₃) = 2
• d(C₂, C₃) = 2
[1 mark per distance]
iv)
The minimum Hamming distance (dₘᵢₙ) among the codewords = 2
To detect up to d errors:
Maximum detectable errors = dₘᵢₙ – 1 = 1
To correct up to t errors:
Maximum correctable errors = ⌊(dₘᵢₙ – 1) / 2⌋ = 0
Therefore:
• The code can detect 1 error
• The code cannot correct any errors
Justification: Based on standard error correction bounds, a code with dₘᵢₙ = 2 allows for
detection of 1-bit errors but not correction.
2 marks for detection/correction, 2 marks for justification]
Q6a) Explain CSMA and its methods.
Ans) 1. Introduction – 1 Mark
CSMA (Carrier Sense Multiple Access) is a medium access control (MAC) protocol used in
computer networks to reduce collisions when multiple stations share the same transmission medium
(like Ethernet or Wi-Fi).
********** 17 **********
--- page 18 ---
It is based on the principle of “Listen Before You Send” — a station first checks if the channel is idle
before transmitting data.
2. Key Concept / Working Principle – 2 Marks
• Multiple Access: Many devices (nodes) share the same communication channel.
• Carrier Sense: Before sending data, each station listens (senses) the channel to check if it’s
busy.
•   If the channel is idle, the station transmits.
•   If the channel is busy, the station waits for some time before trying again.
The goal of CSMA is to minimize collisions, not completely eliminate them (since two stations may
still sense the channel as idle simultaneously).
3. Steps in CSMA Operation – 2 Marks
1. Carrier Sensing:
Each station monitors the channel before transmission.
2. Idle / Busy Check:
o   If the medium is idle, the station transmits immediately.
o   If the medium is busy, the station waits for it to become free.
3. Collision Occurrence:
If two stations transmit at the same time, a collision occurs.
4. Backoff / Retry:
The stations wait for a random backoff time and try again after the channel is idle.
4. Methods (Types) of CSMA – 3 Marks
CSMA has four main methods, differing in how long a station waits before re-transmitting after
sensing the medium:
1. 1-Persistent CSMA
• A station constantly senses the channel.
•   If the channel is idle, it transmits immediately (persistence = 1).
•   If the channel is busy, it keeps sensing until the channel becomes free.
Advantage: Simple and ensures fast transmission.
Disadvantage: High chance of collision if multiple stations sense the channel simultaneously.
2. Non-Persistent CSMA
• The station waits a random time before rechecking the channel if it is busy.
• Reduces collisions because not all stations try to send immediately.
Advantage: Lower collision probability.
Disadvantage: More idle time → lower efficiency.
********** 18 **********
--- page 19 ---
3. p-Persistent CSMA (used in slotted channels like Wi-Fi)
• The channel time is divided into slots.
• When the channel is idle, each station transmits with probability p, and defers with probability
(1–p) to the next slot.
Advantage: Balances between efficiency and collision rate.
Disadvantage: Requires synchronization of time slots.
4. CSMA/CD (Collision Detection)
• Used in wired Ethernet (IEEE 802.3).
• A station listens while transmitting — if it detects a collision, it stops immediately and sends a
jam signal to inform others.
•   After a random backoff, it retries transmission.
Advantage: Saves time and bandwidth by aborting collided transmissions.
Limitation: Works only in wired networks (cannot detect collisions in wireless).
5. Diagram – 1 Mark
Time Line of CSMA Operation:
Idle Medium   Busy Medium   Idle Again
OR for CSMA/CD:
Station A: ----Tx----X(Collision)--Stop--Wait--Retry-->
Station B: ----Tx----X(Collision)--Stop--Wait--Retry-->
6. Advantages and Disadvantages – 0.5 + 0.5 Marks
Advantages:
•   Efficient use of shared medium.
• Reduces chances of collision compared to ALOHA.
• Easy to implement.
Disadvantages:
•   Still susceptible to collisions.
• Performance degrades under heavy traffic.
•   Collision detection not possible in wireless (CSMA/CA used instead).
7. Conclusion – 1 Mark
In summary, CSMA improves network efficiency by sensing the channel before transmitting, reducing
collision rates.
Different variants (1-persistent, non-persistent, p-persistent, and CSMA/CD) offer trade-offs between
efficiency, delay, and collision probability, making CSMA a key foundation of Ethernet and Wi-Fi
communication systems
Q6) b) Discuss SMTP step by step with the help of example
********** 19 **********
--- page 20 ---
Ans) Introduction — 1 Mark
SMTP (Simple Mail Transfer Protocol) is the standard application-layer protocol used to send e-
mail between mail hosts on an IP network.
SMTP is responsible for message submission and transfer from a sender’s Mail User Agent (MUA) to
the sender’s Mail Transfer Agent (MTA) and between MTAs until the message reaches the recipient’s
mail server.
2. Key Concepts / Features — 2 Marks
• Connection-oriented: SMTP uses TCP (typically port 25 for MTA→MTA, 587 or 465 for
message submission with authentication/TLS).
• Text-based request/response protocol: ASCII commands from client, numeric response codes
from server (e.g., 220, 250, 354, 550).
• Commands & Replies: Core commands include HELO/EHLO, MAIL FROM, RCPT TO,
DATA, RSET, QUIT, and extensions like STARTTLS and AUTH.
• MIME & attachments: SMTP transfers message data; MIME defines multipart/attachments and
content types.
• Relaying & authentication: MTAs may require authentication to prevent open relay abuse;
encryption via STARTTLS is used to secure the session.
3. Step-by-Step SMTP Operation — 4 Marks
Step 1 — TCP Connection:
Client (sending MTA or MUA) opens a TCP connection to the server’s SMTP port. Server responds
with a 220 greeting.
Step 2 — Greeting / Extended Hello:
Client sends EHLO client.example.com. Server responds with 250 and lists supported extensions (e.g.,
STARTTLS, AUTH, SIZE).
Step 3 — Optional STARTTLS / AUTH:
•   If encryption desired, client uses STARTTLS to upgrade to TLS; then repeats EHLO.
•   If required, client performs AUTH (PLAIN, LOGIN, or others) to authenticate.
Step 4 — Envelope: MAIL FROM:
Client supplies sender envelope: MAIL FROM:<alice@example.com>. Server replies 250 OK if
accepted.
Step 5 — Envelope: RCPT TO:
Client issues one or more recipients: RCPT TO:<bob@dest.com>. Server replies 250 OK (or 550/451 if
rejected/temporary failure).
Step 6 — DATA (message content):
Client sends DATA. Server replies 354 Start mail input; end with <CRLF>.<CRLF>.
Client transmits the message headers (From, To, Subject, Date, MIME headers) and body. The message
ends with a single dot . on a line by itself. Server replies 250 OK if accepted.
Step 7 — Repeat / Terminate / Queueing:
• For multiple recipients, server may accept some RCPTs and reject others; accepted recipients get
delivery attempt.
•   Client can send RSET to reset the envelope, or QUIT to close. On QUIT, server replies 221 Bye
and closes the TCP connection.
********** 20 **********
--- page 21 ---
Step 8 — MTA to MTA forwarding:
If recipient is on remote domain, MTA looks up MX record (DNS), opens SMTP to recipient’s mail
server, and repeats the steps (MAIL FROM/RCPT TO/DATA) until final delivery or bounce.
4. Example SMTP Session (commands + server replies) — 2 Marks
compact example showing typical text exchanges (client lines prefixed C:; server replies S:):
S: 220 mail.example.net ESMTP Service Ready
C: EHLO client.example.com
S: 250-mail.example.net Hello client.example.com
S: 250-STARTTLS
S: 250-AUTH LOGIN PLAIN
S: 250 SIZE 35882577
.
.
.
.
5. Conclusion — 1 Mark
Conclusion: SMTP is the backbone protocol for e-mail transfer: connection over TCP, command/reply
model, envelope commands (MAIL/RCPT/DATA) and extensible via EHLO for security (STARTTLS)
and auth.
Q7) a) Given a message polynomial M(x) = x⁷ + x³ + x + 1
and generator polynomial G(x) = x⁴ + x + 1,
generate a 4-bit CRC, determine the transmitted frame, and explain error detection.
Ans) Intro / purpose — 1 mark
CRC (Cyclic Redundancy Check) is computed by treating message and generator as polynomials over
GF(2). To send, we append r zero bits (r = degree of G(x)G(x)G(x)) to M(x)M(x)M(x), divide by
G(x)G(x)G(x) and append the remainder (CRC) to the message. Receiver divides received frame by
G(x)G(x)G(x); a non-zero remainder indicates error.
2) Key concept / formula — 2 marks
• Degree of G(x)G(x)G(x) is r=4r=4r=4 ⇒ CRC length = 4 bits.
• Transmitted polynomial T(x)=xrM(x)+R(x)T(x) = x^rM(x) + R(x)T(x)=xrM(x)+R(x) where
R(x)R(x)R(x) is remainder of xrM(x)x^rM(x)xrM(x) divided by G(x)G(x)G(x).
• Binary division is XOR division (no carries).
3) Step-by-step CRC generation — 4 marks
(a) Message → bit string
M(x)=x7+x3+x+1M(x)=x^7 + x^3 + x + 1M(x)=x7+x3+x+1 corresponds to bits from x7x^7x7 down to
x0x^0x0:
1 0 0 0 1 0 1 1 → 10001011.
(b) Append 4 zeros (shift left by 4):
dividend = 10001011 0000 (12 bits).
********** 21 **********
--- page 22 ---
(c) Divide by generator polynomial G(x)=x4+x+1G(x)=x^4 + x + 1G(x)=x4+x+1. The divisor bits
(coefficients x⁴..x⁰) are 1 0 0 1 1.
Perform binary (XOR) long division of 100010110000 by 10011:
• Step 1: XOR divisor with bits 11..7 (leading 1) → zeros appear except at positions updated;
continue.
• Step 2: Next meaningful XOR occurs when a leading 1 appears; continue until end.
(Doing the XOR steps yields the final remainder — shown below.)
Resulting remainder (4 bits) = 0000.
So the CRC bits are 0000.
(d) Transmitted frame = original message bits + CRC =
10001011 0000. (You may write it grouped as 100010110000.)
4) Example: Error detection demonstration — 1.5 marks
If a single-bit error occurs in transmission, the received frame becomes
R′(x)=T(x)+E(x)R'(x)=T(x)+E(x)R′(x)=T(x)+E(x) where E(x)E(x)E(x) is the error polynomial (e.g., a
single bit flip is xkx^kxk). The receiver divides R′(x)R'(x)R′(x) by G(x)G(x)G(x) — if result ≠ 0, an
error is detected.
Concrete example: Suppose the last bit (least significant bit) is flipped during transmission.
Sent: 100010110000
Received (error in LSB): 100010110001.
Divide 100010110001 by 10011 as before: the remainder becomes 0001 (non-zero), so the receiver
detects the error.
(We computed this by the same XOR division steps; the remainder is nonzero, therefore error detected.)
5) Why CRC detects errors — 1.5 marks
•   If E(x)E(x)E(x) (the error pattern) is not divisible by G(x)G(x)G(x), division yields non-zero
remainder → error detected.
• A well-chosen G(x)G(x)G(x) (like the given one) detects:
o   all single-bit errors (since G(x)G(x)G(x) has at least two terms and is not divisible by
xxx),
o many multiple-bit errors and burst errors up to length < degree(G) are detected (more
precise guarantees depend on polynomial factors).
•   In our case, G(x)=x4+x+1G(x)=x^4+x+1G(x)=x4+x+1 will detect single-bit errors — as the
example showed.
6) Conclusion / Final answer — 0.5 mark
• CRC (4 bits) = 0000.
• Transmitted frame = 10001011 0000 (i.e., message 10001011 followed by CRC 0000).
•   If any non-zero remainder is obtained at receiver (example gave remainder 0001), the receiver
flags an error.
Q7) b) Discuss open-loop congestion control.
********** 22 **********
--- page 23 ---
Ans) 1. Introduction – 2 Mark
Congestion control is a network mechanism that prevents excessive data from entering the network,
avoiding packet loss and performance degradation.
There are two main approaches:
1. Open-loop congestion control (preventive)
2. Closed-loop congestion control (reactive)
In open-loop congestion control, decisions are made without feedback from the network — i.e.,
actions are taken before congestion occurs to prevent it.
2. Key Concept / Principle – 2 Marks
• Open-loop control is preventive in nature.
•   It focuses on controlling how data is transmitted and managed at the source and intermediate
nodes to avoid congestion from happening.
• No feedback path exists — once the data is sent, the source does not adjust its behavior based
on network conditions.
Goal:
To maintain network efficiency and reduce the likelihood of congestion by using pre-defined rules
and policies.
3. Policies Used in Open-Loop Congestion Control – 4 Marks
There are several policies implemented at various layers to minimize congestion chances.
Layer /
Policy   Explanation
Function
Retransmission   Determines when and how lost packets are retransmitted. Avoids
Transport Layer
Policy   unnecessary retransmissions that could worsen congestion.
Manages the number of outstanding packets sent before
Window Policy   Transport Layer acknowledgment. Proper window sizing prevents overwhelming
the receiver or network.
Acknowledgment   Controls how acknowledgments (ACKs) are sent — e.g.,
Transport Layer
Policy   cumulative ACKs or delayed ACKs reduce control traffic.
Routers may discard less important packets early (e.g., old or
Discard Policy   Network Layer
low-priority data) to prevent buffer overflow.
Determines whether to accept new traffic into the network. If the
Admission Policy   Network Layer
network is near capacity, new requests are denied or delayed.
Data Link /   Decides the order of packet transmission (e.g., FIFO, priority
Scheduling Policy
Network Layer scheduling) to maintain fairness and avoid congestion build-up.
4. Example – 1 Marks
Let’s say a video streaming service sends data packets over the Internet.
Using open-loop control, the sender follows a fixed transmission rate and window size determined in
advance.
If the network becomes congested, the sender doesn’t get feedback (no “slow down” message).
********** 23 **********
--- page 24 ---
Thus, congestion must be prevented proactively — e.g., by optimizing window size, discarding old
frames, or using priority scheduling for key video packets.
6. Advantages and Disadvantages – 0.5 + 0.5 Marks
Advantages:
• Simple and efficient for stable networks.
• No overhead for monitoring or feedback messages.
Disadvantages:
• Cannot adapt to changing network conditions.
•   Ineffective in dynamic or unpredictable environments.
7. Conclusion – 1 Mark
In summary, open-loop congestion control is a preventive mechanism that uses static policies — like
retransmission control, window sizing, and scheduling — to reduce the likelihood of congestion.
While it is efficient in predictable networks, modern systems often combine it with closed-loop
feedback methods for adaptive performance.
********** 24 **********
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 9370de7dfd4e

- Departments: Artificial Intelligence, Computer Engineering, Computer Science, Cyber Security, Data Science, Electronics and Telecommunication, Information Technology
- Programmes: BTech AI 7012, BTech CS 7055, BTech CSE DS 7057, BTech CyberSecurity 7010, BTech EXTC 7006, BTech IT 7001, Integrated Computer 7032, MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CS_7055/Computer Networks/ANS_Computer Networks(702AI0C023)_2025-2026.pdf` (+7 identical copies)
- Text: mixed (28 pages), mean OCR confidence 88.7

````text
CO,
BL,   Mark
SO   Q No   Question   s
CO1   A university plans to set up a campus network. Apply the concepts of wired and
BL3   wireless communication to explain how each could be used in this network with
SO1   respect to speed, reliability and security.
Q1 a   5
SYNOPTIC
Wired Communication (Ethernet, Fiber Optic):
• Implementation: Connecting classrooms, labs, and offices using Ethernet
cables or fiber optics.
• Speed: High data transfer rates; suitable for heavy traffic like video streaming
and large file transfers.
•   Reliability: Very reliable; less affected by interference or obstacles.
•   Security: More secure; physical access required to tap into the network.
Wireless Communication (Wi-Fi):
• Implementation: Providing connectivity to mobile devices, laptops, and
guest users via access points across the campus.
• Speed: Moderate; can be affected by distance, number of users, and
interference.
•   Reliability: Less reliable than wired; signal may degrade with obstacles or
high traffic.
•   Security: Requires encryption (WPA3/WPA2); more vulnerable to attacks
than wired networks.
Soln
--- page 2 ---
Marking Scheme (5 Marks):
Wired Communication-Correctly explains implementation, speed, reliability and
security- 2 Marks
Wireless Communication- Correctly explains implementation, speed, reliability
and security - 2 Marks
Explains practical usage of wired and wireless networks in campus context-1
Marks
CO1,
BL 2,
SO 1
Q1 b   Compare and contrast the TCP/IP model with the OSI model on any five points   5
▪ Number of Layers: OSI has seven layers, while the TCP/IP model typically
consists of four or five layers.
▪   Protocol Dependency: TCP/IP was developed from a protocol-driven
approach based on real-world protocols, while OSI is a theoretical model that
is protocol-independent.
▪ Layers Combined: The TCP/IP model combines the OSI's Session,
Presentation, and Application layers into a single "Application Layer" and
merges the Data Link and Physical layers into a "Network Access Layer".
▪   Reliability: The TCP/IP model's reliability features are primarily handled by
the Transport layer (TCP protocol), while the OSI model's reliability
mechanisms are spread across different layers.
▪ Usage: The TCP/IP model is the practical, widely implemented model used
for the internet. The OSI model is primarily used as a reference or teaching
tool.
Soln
CO 2
BL-2   In a Slotted ALOHA system, the average number of frames generated per frame
SO 1   time is G = 1. Calculate the throughput S. What is the maximum throughput in
Q1 c   Slotted ALOHA   5
(2MARKS)
•   It can be proven that the average number of successful transmissions for
slotted ALOHA is S = G *e^-G.
• The maximum throughput Smax is 0.368, when G = 1. In other words, if one
frame is generated during one frame transmission time, then 36.8 percent of
these frames reach their destination successfully.
• We expect G = 1 to produce maximum throughput because the vulnerable
time is equal to the frame transmission time.
Soln
--- page 3 ---
•   Therefore, if a station generates only one frame in this vulnerable time (and
no other station generates a frame during this time), the frame will reach its
destination successfully.
(2MARKS)
Formula:
S=G×e^−G
Substitution:
S=1×e^−1
=1×0.3679
=0.368S
(1MARKS)
Throughput ≈ 0.368 (36.8%)
So throughput = 36.8% efficiency.
CO-3;
SO-2;
BL-3   A block of address is granted to a small organization and one of the address is
200.140.64.48/26. Determine the first address and last address in the block.
Q1 d   Determine the total number of addresses in the block.   5
IP address = 200.140.64.48/26
Step   Interpret /26
• Subnet mask length = 26 bits
• So network part = 26 bits, host part = 32−26=6 bits.
That means:
Soln
--- page 4 ---
• Number of addresses per block = 26=64
Step — Find the network (first) address
In dotted decimal:
/26 mask →
255.255.255.192
(because the 26th bit boundary falls inside the 4th octet:
11111111.11111111.11111111.11000000)
Each block starts at multiples of 64 in the 4th octet:
0, 64, 128, 192.
Now, given IP is 200.140.64.48, and 48 lies between 0 and 63.
So this IP belongs to the subnet that starts at .0.
Network address = 200.140.64.0 - 2 mark
Step — Find the broadcast (last) address
Add 63 (since 64 addresses per block, counting from 0):
0 + 63 = 63 → 200.140.64.63
Last address (broadcast address) = 200.140.64.63 – 2 mark
Step — Compute total number of addresses
2(32−26)=26=64
Total addresses = 64   - 1 mark
CO-   i) Explain the block coding method for error detection and correction. (2 marks)
2; SO-   ii)Two binary codewords are used in a communication system:
1;
BL-3   • C1 = 1001101
• C2 = 1110001
Compute the Hamming distance between C1 and C2 . (2 marks)
iii) A new codeword C3 = 1010101 is added to the set. Compute the pairwise
Hamming distances between C3 and the other codewords. (2 marks)
iv) Based on the minimum Hamming distance of the code, determine how many
errors the code can detect and how many it can correct. Justify your answer. (4
Q2 a   marks)   10
--- page 5 ---
i) Explain the block coding method for error detection and correction. (2 marks)
•   In block coding, the message is divided into blocks, each of k bits, called
data words .
•   r redundant bits are added to each block to make the length n=k+r
• The resulting n bit blocks are called codewords. (1 mark)
• The block coding process is one-to-one; the same dataword is always
encoded as the same codeword.
• Message bits (k): The actual data to be sent
• Codeword bits (n): The message bits plus redundant bits
• Redundant bits (n - k): Extra bits added for error detection and correction
(1 mark)
ii) Compute the Hamming distance between C1 and C2
Step : (1 mark)
Final answer: No of 1’s = 4 . Hence Hamming Distance = 4 (1 mark)
iii) A new codeword C3 = 1010101 is added to the set. Compute the pairwise
Hamming distances between C3 and the other codewords.
A. ( C3 = 1010101 ) vs ( C1 = 1001101 )
Steps to show (1 mark)
Hamming distance = 2   (1 mark)
B.( C3 = 1010101 ) vs ( C2 = 1110001 )
Steps to show (1 mark)
Hamming distance = 2   (1 mark)
iv) Determine error detection and correction capabilities
•   ( d(C_1, C_2) = 4 )
•   ( d(C_1, C_3) = 2 )
•   ( d(C_2, C_3) = 2 )
so, d{min} = 2   (1mark)
Error detection: (1 mark)
• A code can detect up to ( d_{min} - 1 ) errors.
•   So: can detect ( 2 - 1 = 1 ) error
Error correction: 0 error (1 mark)
Final concluding answer with justification (2 mark)
• Minimum distance = 2
• Can detect 1 error, correct 0 errors
Soln
--- page 6 ---
CO-3;   A company wants to set up a network for smooth data transfer between its offices.
SO-1;   Based on your understanding, which switching technique—circuit, packet, or
BL-3   message—would you recommend? Explain how each works and compare their
Q2 b   pros, cons, and best use cases to support your choice.   10
Switchin
g   Working   Advantag   Disadvantag   Best Use
Techniq   Principle   es   es   Case
ue
Dedicated
Reliable,   Voice
path is   Inefficient
Circuit   continuou   communicatio
established   for data; idle
Switchin   s   n (e.g.,
before   time wastes
g   connectio   telephone
communicati   resources.
n.   networks).
on begins.
Data is split
into packets   Efficient
sent   bandwidth
Packet   Possible   Internet, real-
independentl   usage;
Switchin   delays,   time data
y and   supports
g   packet loss.   transmission.
reassembled   multiple
at   users.
destination.
Entire
No need
message is
for   High delay   Email, non-
Message   stored and
dedicated   due to   real-time
Switchin forwarded
path;   storage at   communicatio
g   through
flexible   each node.   n.
intermediate
routing.
nodes.
Recommendation -Packet switching is recommended for the company’s network
due to its efficiency, scalability, and ability to handle diverse data types across
multiple branches.
Explanation of all three techniques (working principles)- 3 marks
Comparison of advantages and disadvantages -   3 marks
Identification of suitable applications-   2 marks
Soln   Justified recommendation based on scenario-   2 marks
BL 1,
CO 1,
SO 1 Q3 a   Define the following:- a) LAN b) MAN c)PAN d) WAN e) ARPANET   5
--- page 7 ---
1 mark for each definition
a) LAN (Local Area Network):
A Local Area Network is a network that connects computers and devices within a
limited geographical area such as a home, school, office building, or campus.
• Example: A network connecting computers in a computer lab.
• Data transfer speed: High (typically 100 Mbps to 10 Gbps).
b) MAN (Metropolitan Area Network):
A Metropolitan Area Network covers a larger area than a LAN, usually spanning a
city or a large campus. It connects multiple LANs together within a metropolitan
area.
• Example: A network connecting different branches of a university within a
city.
c) PAN (Personal Area Network):
A Personal Area Network is the smallest type of network, used for connecting
personal devices within a short range (usually within 10 meters).
• Example: Connecting a smartphone to a laptop via Bluetooth.
d) WAN (Wide Area Network):
A Wide Area Network covers a very large geographical area, often a country or
even globally. It connects multiple LANs and MANs using public networks like
the Internet or satellite links.
• Example: The Internet is the largest WAN.
e) ARPANET (Advanced Research Projects Agency Network):
ARPANET was the first operational packet-switching network and the precursor to
the modern Internet. It was developed in the late 1960s by the U.S. Department of
Defense’s ARPA (now DARPA) to connect research institutions and allow
Soln   resource sharing.
CO3,
BL2   Explain the different types of OSPF packets used for communication between
SO 1 Q3 b   routers.   5
OSPF uses five types of packets for communication between routers:
1. Hello Packet – Used to discover and maintain neighbor relationships.
2. Database Description (DBD) Packet – Used to summarize the contents of a
router’s link-state database.
3. Link-State Request (LSR) Packet – Sent to request specific link-state
information from a neighbor.
4. Link-State Update (LSU) Packet – Carries detailed link-state information
Soln   (LSAs) to other routers.
--- page 8 ---
5. Link-State Acknowledgment (LSAck) Packet – Confirms the receipt of
LSUs to ensure reliable delivery.
Summary:
OSPF uses 5 packet types — Hello, DBD, LSR, LSU, and LSAck — to form
neighbors, exchange topology data, and keep the network synchronized.
CO5   Explain, with the help of a neat diagram, how the World Wide Web (WWW)
BL 2   enables users to access online information through the HTTP protocol. Describe
SO 1   the components and working mechanism of the Web, and interpret how HTTP
facilitates communication between a client and a server when a user enters a URL
Q3 c   such as http://www.example.com   10
The World Wide Web (WWW) is a global information system that enables users to
access interlinked documents and multimedia content over the Internet. It operates
on a client–server model, where the HTTP protocol governs communication
between browsers (clients) and web servers.
Diagram and explanation: WWW and HTTP Communication Flow (4 marks)
• Request–Response Model:
HTTP follows a simple two-way exchange — the client sends a request,
and the server responds.
•   Stateless Protocol:
Each request is independent, improving scalability and simplicity.
•   Structured Message Format:
o Request Line: Method, resource, version
o Headers: Metadata (host, content type, etc.)
o Body: Optional data (for POST requests)
•   Reliable Transport:
Soln.   Uses TCP to ensure ordered, error-free data delivery.
--- page 9 ---
•   Status Codes:
Help the browser understand response outcomes (e.g., 200 OK, 404 Not
Found).
Components of the World Wide Web (3 marks)
Component   Description
Application (e.g., Chrome, Firefox) used to send requests
Web Browser (Client)
display web pages.
Computer that stores and serves web pages when request
Web Server
clients.
Uniform Resource   Unique address that identifies a specific web resource. Ex
Locator (URL)   http://www.example.com/index.html.
HTTP (Hypertext   Communication protocol used for transferring web docum
Transfer Protocol)   between browser and server.
HTML (Hypertext
Standard language used to structure and format web page
Markup Language)
Working Mechanism of the WWW (3 marks)
When a user types http://www.example.com in the browser:
1. URL Parsing:
The browser divides the URL into:
o Protocol → http
o Host name → www.example.com
o File/resource → default index.html
2. DNS Resolution:
The browser queries the DNS to obtain the IP address of the web server
hosting www.example.com.
3. Connection Establishment:
A TCP connection is initiated between the client and the server on port 80
(default for HTTP).
4. HTTP Request:
The browser sends an HTTP request message (e.g., GET /index.html
HTTP/1.1) asking for the web page.
5. HTTP Response:
The server locates the requested file, encapsulates it in an HTTP response
message with a status code and sends it back to the browser.
6. Rendering the Page:
The browser interprets the HTML, CSS, and scripts received and displays
the webpage to the user.
--- page 10 ---
7. Connection Termination:
Once the transfer is complete, the TCP connection is closed.
CO-3
SO-1   Summarize the IPv6 address 0:15::1:12:1213 to its full, original form. Write a
BL-2   comparison between IPv4 and IPv6 packet headers.
Q4 a   10
First, we need to align the left side of the double colon (::) with the left side of the
original IPv6 address pattern, and the right side of the double colon with the right
side of the original pattern. This helps us determine how many groups of zeros we
need to replace the double colon with.
For the given the address:
0:15::1:12:1213
We align the known parts as:
0:15: (left side), then the double colon ::, then 1:12:1213 (right side).
By counting how many groups of zeros are missing between the left and right parts
to complete the full 8-group IPv6 address, we find that the double colon represents
four groups of zeros.
Therefore, the original expanded address is:
0000:0015:0000:0000:0000:0001:0012:1213
Comparison between IPv4 and IPv6 packet headers:
➢ The header length field is removed in IPv6 because the header length is fixed
in this version.
➢ The service type field is also removed in IPv6. Instead, the priority and flow
label fields together perform the function that the service type field used to
handle.
➢ The total length field from IPv4 is replaced by the payload length field in
IPv6.
➢ The identification, flag, and offset fields are no longer part of the base header
in IPv6. Instead, they are included in a separate fragmentation extension
header.
➢ The TTL (Time To Live) field in IPv4 is renamed to hop limit in IPv6.
➢ The protocol field in IPv4 is replaced by the next header field in IPv6.
➢ The header checksum is eliminated in IPv6 because checksums are handled
by upper-layer protocols, so it is not needed at the IPv6 header level.
➢ The option fields that exist in IPv4 are implemented as extension headers in
IPv6.
(The IPv6 address 0:15::1:12:1213 to its full, original form-05M and
Soln
--- page 11 ---
Any five point of comparison between IPv4 and IPv6 packet headers-05M)
BL- 2
CO-4   Describe the User Datagram Protocol (UDP) in detail with suitable diagram (6
SO-1 Q4 b   marks). Also explain how it differs from TCP (4 marks)?   10
(6 marks)
The User Datagram Protocol (UDP) is called a connectionless, unreliable transport
protocol. It does not add anything to the services of IP except to provide process-to-
process communication instead of host-to-host communication.
• The User Datagram Protocol (UDP) is called a connectionless, unreliable
transport protocol.
•   It does not add anything to the services of IP except to provide process-to-
process communication instead of host-to-host communication.
•   It performs very limited error checking.
•   If UDP is so powerless, why would a process want to use it?
• UDP is a very simple protocol using a minimum of overhead.
•   If a process wants to send a small message and does not care much
about reliability, it can use UDP.
• Sending a small message by using UDP takes much less interaction
between the sender and receiver than using TCP (Transmission
control protocol) or SCTP (Stream control transmission protocol).
UDP Operations:
Connectionless Services: Each user datagram sent by UDP is an independent
datagram. There is no relationship between the different user datagrams even if they
are coming from the same source process and going to the same destination program.
The user datagrams are not numbered. Also, there is no connection establishment
and no connection termination, as is the case for TCP. This means that each user
datagram can travel on a different path. Each request must be small enough to fit
into one user datagram. Only those processes sending short messages should use
UDP.
Flow and Error Control:
UDP is a very simple, unreliable transport protocol. There is no flow control and
hence no window mechanism. The receiver may overflow with incoming messages.
There is no error control mechanism in UDP except for the checksum. This means
Soln   that the sender does not know if a message has been lost or duplicated. When the
--- page 12 ---
receiver detects an error through the checksum, the user datagram is silently
discarded.
Encapsulation and Decapsulation:
To send a message from one process to another, the UDP protocol encapsulates and
decapsulates messages in an IP datagram.
Encapsulation
When a process has a message to send through UDP, it passes the message to UDP
along with a pair of socket addresses and the length of data.
UDP receives the data and adds the UDP header.
UDP then passes the user datagram to IP with the socket addresses.
IP adds its own header, using the value 17 in the protocol field, indicating that the
data has come from the UDP protocol.
Decapsulation
When the message arrives at the destination host, the physical layer decodes the
signals into
bits and passes it to the data link layer.
The data link layer uses the header (and the trailer) to check the data. If there is no
error, the header and trailer are dropped and the datagram is passed to IP.
The IP software does its checking. If there is no error, the header is dropped and the
user datagram is passed to UDP with the sender and receiver IP addresses.
Queuing:
--- page 13 ---
(4 marks)
Transmission   Control   Protocol   User Datagram Protocol
Basis   (TCP)   (UDP)
UDP is the Datagram-
oriented protocol. This is
TCP is   a   connection-oriented   because there   is   no
protocol.   Connection orientation   overhead for opening a
means   that   the communicating   connection, maintaining
Type   of
devices   should   establish   a   a   connection,   or
Service
connection before transmitting data   terminating   a
and should close the connection after   connection. UDP   is
transmitting the data.   efficient for broadcast
and multicast types of
network transmission.
TCP is reliable as it guarantees the The delivery of data to
Reliability
delivery of data to the destination   the destination cannot be
router.   guaranteed in UDP.
Error   TCP   provides   extensive error- UDP has only the basic
checking   checking mechanisms. It is because   error-checking
mechanis   it   provides   flow   control and mechanism
m   acknowledgment of data.   using checksums.
Acknowle An acknowledgment segment   is No   acknowledgment
dgment   present.   segment.
--- page 14 ---
There is no sequencing
Sequencing of data is a feature of
of data in UDP. If the
Transmission   Control Protocol
Sequence   order is required, it has to
(TCP). this means that packets arrive
be managed by   the
in order at the receiver.
application layer.
UDP is faster, simpler,
TCP is comparatively slower than
Speed   and more efficient than
UDP.
TCP.
There   is   no
retransmission of   lost
Retransmi   Retransmission of lost packets is
packets   in   the User
ssion   possible in TCP, but not in UDP.
Datagram   Protocol
(UDP).
Header   TCP has a (20-60) bytes variable UDP has an 8 bytes
Length   length header.   fixed-length header.
Weight   TCP is heavy-weight.   UDP is lightweight.
Handshak
It's   a   connectionless
ing   Uses handshakes such as SYN,
protocol   i.e.   No
Technique ACK, SYN-ACK
handshake
s
Broadcast   UDP   supports
TCP doesn't support Broadcasting.
ing   Broadcasting.
CO-2,   Apply the principles of the Selective Repeat ARQ Sliding Window Protocol to
BL-3   determine the maximum permissible sender and receiver window sizes for frame
SO-1   sequence number field of 3 bits, and explain with the help of diagram how frames
are transmitted, acknowledged, and buffered at both the sender and receiver ends.
Justify why this window size is chosen, and analyze how incorrect window sizing
can lead to frame mis ordering or acknowledgment ambiguity.
Q5 a   10
--- page 15 ---
Explanation of Selective Repeat ARQ   (1 marks),
window size   (1marks),
explanation of frame transmission   (3 marks),
justification of window size 5 marks   ( 3 explanation and 2 marks diagram)
Solution: In Selective Repeat ARQ only the lost or error frames are retransmitted,
whereas correct frames are received and buffered. The receiver while keeping track
of sequence numbers buffers the frames in memory and sends NACK for only
frames which are missing or damaged. The sender will send/retransmit a packet for
which NACK is received.
Step 1 − Frame 0 sends from sender to receiver and set timer.
Step 2 − Without waiting for acknowledgement from the receiver another frame,
Frame1 is sent by sender by setting the timer for it.
Step 3 − In the same way frame2 is also sent to the receiver by setting the timer
without waiting for previous acknowledgement.
Step 4 − Whenever sender receives the ACK0 from receiver, within the frame 0
timer then it is closed and sent to the next frame, frame 3.
Step 5 − whenever the sender receives the ACK1 from the receiver, within the
frame 1 timer then it is closed and sent to the next frame, frame 4.
Step 6 − If the sender doesn’t receive the ACK2 from the receiver within the time
slot, it declares timeout for frame 2 and resends the frame 2 again, because it
thought the frame2 may be lost or damaged.
Soln
--- page 16 ---
Figure 11.23 Flow diagramfor Example 11.8

Sender Receiver

mn

O° Sf Sn . J R,
Request

Initial

Arrival

Request

Request

Arrival

Request

H wee — | [5[6[7] Arrival

1 n <Lo '
Fo H
Arrival '
Frame | (resend)
1 R,
1 a ps CK
Arrival t>fo111213 Arrival
H Frames 1,2,3
Y Y delivered

Window Sizes
We can now show why the size of the sender and receiver windows must be at most one-
half of 2”. For an example, we choose m = 2, which means the size of the window is 2”/2,
or 2. Figure 11.21 compares a window size of 2 with a window size of 3.

If the size of the window 1s 2 and all acknowledgments are lost, the timer for frame 0
expires and frame 0 is resent. However, the window of the receiver is now expecting

frame 2, not frame 0, so this duplicate frame is correctly discarded. When the size of
the window is 3 and all acknowledgments are lost, the sender sends a duplicate of
frame 0. However, this time, the window of the receiver expects to receive frame 0 (0 is
part of the window), so it accepts frame 0, not as a duplicate, but as the first frame in
the next cycle. This is clearly an error.

In Selective Repeat ARQ, the size of the sender and receiver window
must be at most one-half of 2””+
--- page 17 ---
BL: 2,   Explain SMTP and its role in email communication. Describe the different phases
SO: 2   of SMTP communication, detailing the purpose of each phase and the typical
CO: 5   commands used. Illustrate your answer with a labelled diagram showing the flow
Q5 b   between the client and server   10
SMTP Explanation: 2 marks
Diagram: 2 marks
Phases: 6 marks
•One of the most popular Internet services is electronic mail (e-mail).
•E-mail allow users to exchange messages. It is considered as a one-way transaction.
User Agent:
Soln
--- page 18 ---
•A user agent is a software package that composes , reads , replies to , and forwards
messages.
•Types of user agents:
Command driven
GUI based
•Mailing list: E-mail allows one name, an alias to represent several different e-mail
addresses
The protocol that defines the MTA client and server in the internet is called as
Simple Mail Transfer Protocol(SMTP)
•SMTP uses commands and responses to transfer messages between an MTA client
and MTA server.
•Commands: Keyword: argument(s)
•Responses: Responses are sent from the server to the client. A response is a three
digit code that may be followed by additional textual information
MAIL TRANSFER PHASES
Connection Establishment
1.The server sends code 220(service ready) to tell the client that it is ready to receive
mail. If the server is not ready it sends code 421(service not available)
2.The client sends the HELLO message to identify itself, using its domain name
address.
3.The server responds with code 250(request command completed)
Message transfers
1.The client sends the MAIL FROM message to introduce the sender of the message.
2.The server responds with code 250 or some other appropriate code.
3.The client sends the RCPT TO message, which includes the mail address of the
recipient.
--- page 19 ---
4.The server responds with code 250 or some other appropriate code.
5.The client sends the DATA message to initialize the message transfer.
6.The server responds with code 354(start mail input)
7.The client sends the contents of the message in consecutive lines.
8.The server responds with code 250 or some other appropriate code
Connection Termination
1.The client sends the QUIT command
2.The server responds with code 221(service closing transmission channel)
CO1
SO1
BL-1   List different types of unguided transmission media and write any two
Q6 a   characteristics of each.   5
Radio waves
Radio waves are Omnidirectional, useful for multicasting. AM and FM radio,
television, maritime radio, cordless phones, and paging are examples of
multicasting.
Radio waves a good candidate for long-distance broadcasting.
Advantage: receives signal inside a building
Disadvantage: Cannot isolate a communication
Microwaves
Microwave propagation is line-of-sight.
Soln
--- page 20 ---
Very high-frequency microwaves cannot penetrate walls
The microwave band is relatively wide, almost 299 GHz. Therefore wider
subbands can be assigned, and a high data rate is possible
Use of certain portions of the band requires permission from authorities.
Microwaves are used in cellular phones , satellite networks and
wireless LANs
Infrared Waves
Infrared signals can be used for short-range communication in a closed area using
line-of-sight propagation.
Infrared waves, having high frequencies, cannot penetrate walls.
The wide bandwidth can be used to transmit digital data with a very high data rate.
Infrared waves, having high frequencies, cannot penetrate walls.
The wide bandwidth can be used to transmit digital data with a very high data rate.
The recent standard defines a data rate of 4 Mbps.
CO2,
BL-4   Compare 1-persistent, non-persistent, and p-persistent CSMA strategies with
SO-1 Q6 b   diagrammatic representations   5
Points of 1-persistent, non-persistent, and p-persistent 1M each )- 3M , diagram
2M
1-Persistent CSMA
• Working:
The node listens to the channel.
Soln   o   If idle → transmit immediately.
--- page 21 ---
o   If busy → keep listening continuously and transmit immediately
when it becomes free.
•   Pros: Simple, high channel utilization.
• Cons: High chance of collisions if multiple nodes are waiting (because they
all send immediately once the channel is free).
Non-Persistent CSMA
• Working:
o The node listens to the channel.
o   If idle → transmit immediately.
o   If busy → does not continuously sense. Instead, it waits a random
backoff time and then checks again.
•   Pros: Lower chance of collisions.
• Cons: Higher delay, because nodes may wait even if the channel becomes
free.
p-Persistent CSMA (used in slotted channels, e.g., LANs)
• Working:
o The channel is divided into discrete time slots.
o When the channel is sensed idle:
▪ Transmit with probability p.
▪ Wait until the next time slot with probability 1 − p, then
repeat.
•   Pros: Balance between efficiency and collision probability; reduces chance
of many nodes transmitting at once.
• Cons: Performance depends on proper tuning of p.
CO-4
BL-2   Explain open loop and closed loop congestion control policy in transmission
SO-1 Q6 c   control protocol. Describe any two policies from each type.   10
--- page 22 ---
Open Loop: Open loop congestion control mechanisms try to remove the congestion
before it happens.
Works independently of feedback from the network.   ---- 1M
Closed Loop: Closed loop congestion control mechanisms try to remove the
congestion after it happens.
Uses feedback from the network (ACKs, packet loss, delays) to adjust transmission.
--- 1M
Open Loop Policies (any 2)   ----- 2 *2 = 4M
Retransmission Policy
• The sender retransmits a packet, if it feels that the packet it has sent is lost or
corrupted.
• However retransmission in general may increase the congestion in the network.
But we need to implement good retransmission policy to prevent congestion.
• The retransmission policy and the retransmission timers need to be designed to
optimize efficiency and at the same time prevent the congestion.
Window Policy
• To implement window policy, selective reject window method is used for
congestion control.
• Selective Reject method is preferred over Go-back-n window as in Go-back-n
method, when timer for a packet times out, several packets are resent, although some
may have arrived safely at the receiver. Thus, this duplication may make congestion
worse.
• Selective reject method sends only the specific lost or damaged packets.
Soln
--- page 23 ---
Acknowledgement Policy
• The acknowledgement policy imposed by the receiver may also affect congestion.
• If the receiver does not acknowledge every packet it receives, it may slow down
the sender and help prevent congestion.
• Acknowledgments also add to the traffic load on the network. Thus, by sending
fewer acknowledgements we can reduce load on the network.
• To implement it, several approaches can be used:
1. A receiver may send an acknowledgement only if it has a packet to be sent.
2. A receiver may also decide to acknowledge only N packets at a time.
Admission Policy
• An admission policy, which is a quality-of-service mechanism, can also prevent
congestion in virtual circuit networks.
• Switches in a flow first check the resource requirement of a flow before admitting
it to the network.
• A router can deny establishing a virtual circuit connection if there is congestion in
the "network or if there is a possibility of future congestion.
Closed Loop Policies (any 2)   ------- 2*2 = 4M
Backpressure
• Backpressure is a node-to-node congestion control that starts with a node and
propagates, in the opposite direction of data flow.
• The backpressure technique can be applied only to virtual circuit networks. In such
virtual circuit each node knows the upstream node from which a data flow is coming.
--- page 24 ---
• In this method of congestion control, the congested node stops receiving data from
the immediate upstream node or nodes.
• This may cause the upstream node on nodes to become congested, and they, in turn,
reject data from their upstream node or nodes.
• As shown in fig node 3 is congested and it stops receiving packets and informs its
upstream node 2 to slow down. Node 2 in turns may be congested and informs node
1 to slow down. Now node 1 may create congestion and informs the source node to
slow down. In this way the congestion is alleviated. Thus, the pressure on node 3 is
moved backward to the source to remove the congestion.
Choke Packet
• In this method of congestion control, congested router or node sends a special type
of packet called choke packet to the source to inform it about the congestion.
• Here, congested node does not inform its upstream node about the congestion as in
backpressure method.
• In choke packet method, congested node sends a warning directly to the source
station i.e. the intermediate nodes through which the packet has travelled are not
warned.
--- page 25 ---
CO3,   Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The
BL3,   directed edges between these nodes and their corresponding positive weights
4 ,   are given in the table below
SO2
Edge   Distance
A->B   4
A->C   2
B->C   5
B->D   10
C->D   3
C->E   4
D->E   1
D->F   2
E->F   3
F->G   5
Using Dijkstra’s Algorithm:
i. Determine the shortest path from the source node A to the destination node
G.
ii. Compute the shortest distance from node A to node G.
iii. Show all intermediate steps, including the initialization, selection of the
minimum distance node, for each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edge
Q7 a   10
Soln
--- page 26 ---
The shortest path A->C ->D->F->G, shortest distance is 12
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
(iii)   Intermediate Steps - 3marks
(iv)   Original network topology ( 1marks) + final shortest path
with the corresponding distance values clearly marked on
the edges ( 1 marks)
1) Edge costs
Edge Weight
A → B 4
A → C 2
B → C 5
B → D 10
C → D 3
C → E 4
D → E 1
D → F 2
E → F 3
F → G 5
2) Iteration table
--- page 27 ---
CO-4;
SO-1;   Draw a neat diagram and explain the working of the Token Bucket Algorithm.
BL-2 Q7 b   State any two limitations of the Token Bucket algorithm   10
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for
limitations.
Explanation of working based on the following points is expected.
• A bucket holds tokens, each token allowing the transmission of a certain
number of bytes (usually 1 token = 1 byte or 1 packet).
• Tokens are added to the bucket at a constant rate r (tokens per second).
• The bucket has a maximum capacity B (in tokens).
• When a packet arrives:
Soln
--- page 28 ---
o   If there are enough tokens, the packet is transmitted, and tokens are
removed from the bucket.
o   If not enough tokens, the packet is either delayed (until enough tokens
are available) or dropped (if there's no buffering).
This allows bursts of traffic up to B bytes to be sent at once (if the bucket is full),
but enforces an average rate of r bytes/sec over time.
Two Limitations of the Token Bucket Algorithm
1. Complexity with Bursty Traffic:
o While the algorithm allows short bursts, if traffic bursts are too
frequent or too large, it may still overwhelm downstream systems,
leading to queue overflows.
2. No Built-in Fairness or Priority:
o The algorithm does not distinguish between different types of traffic.
So, critical or high-priority packets can be delayed just like any
others, making   it unsuitable for quality of service (QoS)
differentiation without additional mechanisms.
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 3666ede0aa50

- Departments: AI and Data Science, Computer Engineering
- Programmes: BTech AIDS 7056, MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/MBATech_Computer_7047/Computer Networks/ANS_Computer Networks(702AI0C023)_2025-2026.pdf` (+1 identical copies)
- Text: mixed (28 pages), mean OCR confidence 88.7

````text
CN TEE Synoptic AY – 25-26
CO,
BL,   Mark
SO   Q No   Question   s
CO1   A university plans to set up a campus network. Apply the concepts of wired and
BL3   wireless communication to explain how each could be used in this network with
SO1   respect to speed, reliability and security.
Q1 a   5
SYNOPTIC
Wired Communication (Ethernet, Fiber Optic):
• Implementation: Connecting classrooms, labs, and offices using Ethernet
cables or fiber optics.
• Speed: High data transfer rates; suitable for heavy traffic like video streaming
and large file transfers.
•   Reliability: Very reliable; less affected by interference or obstacles.
•   Security: More secure; physical access required to tap into the network.
Wireless Communication (Wi-Fi):
• Implementation: Providing connectivity to mobile devices, laptops, and
guest users via access points across the campus.
• Speed: Moderate; can be affected by distance, number of users, and
interference.
•   Reliability: Less reliable than wired; signal may degrade with obstacles or
high traffic.
•   Security: Requires encryption (WPA3/WPA2); more vulnerable to attacks
than wired networks.
Marking Scheme (5 Marks):
Wired Communication-Correctly explains implementation, speed, reliability and
security- 2 Marks
Wireless Communication- Correctly explains implementation, speed, reliability
and security - 2 Marks
Explains practical usage of wired and wireless networks in campus context-1
Marks
Soln
CO1,
BL 2,
SO 1
Q1 b   Compare and contrast the TCP/IP model with the OSI model on any five points   5
--- page 2 ---
▪ Number of Layers: OSI has seven layers, while the TCP/IP model typically
consists of four or five layers.
▪   Protocol Dependency: TCP/IP was developed from a protocol-driven
approach based on real-world protocols, while OSI is a theoretical model that
is protocol-independent.
▪ Layers Combined: The TCP/IP model combines the OSI's Session,
Presentation, and Application layers into a single "Application Layer" and
merges the Data Link and Physical layers into a "Network Access Layer".
▪   Reliability: The TCP/IP model's reliability features are primarily handled by
the Transport layer (TCP protocol), while the OSI model's reliability
mechanisms are spread across different layers.
▪ Usage: The TCP/IP model is the practical, widely implemented model used
for the internet. The OSI model is primarily used as a reference or teaching
tool.
Soln
CO 2
BL-2   In a Slotted ALOHA system, the average number of frames generated per frame
SO 1   time is G = 1. Calculate the throughput S. What is the maximum throughput in
Q1 c   Slotted ALOHA   5
(2MARKS)
•   It can be proven that the average number of successful transmissions for
slotted ALOHA is S = G *e^-G.
• The maximum throughput Smax is 0.368, when G = 1. In other words, if one
frame is generated during one frame transmission time, then 36.8 percent of
these frames reach their destination successfully.
• We expect G = 1 to produce maximum throughput because the vulnerable
time is equal to the frame transmission time.
•   Therefore, if a station generates only one frame in this vulnerable time (and
no other station generates a frame during this time), the frame will reach its
destination successfully.
(2MARKS)
Soln
--- page 3 ---
Formula:
S=G×e^−G
Substitution:
S=1×e^−1
=1×0.3679
=0.368S
(1MARKS)
Throughput ≈ 0.368 (36.8%)
So throughput = 36.8% efficiency.
CO-3;
SO-2;
BL-3   A block of address is granted to a small organization and one of the address is
200.140.64.48/26. Determine the first address and last address in the block.
Q1 d   Determine the total number of addresses in the block.   5
IP address = 200.140.64.48/26
Step   Interpret /26
• Subnet mask length = 26 bits
• So network part = 26 bits, host part = 32−26=6 bits.
That means:
• Number of addresses per block = 26=64
Step — Find the network (first) address
In dotted decimal:
/26 mask →
255.255.255.192
(because the 26th bit boundary falls inside the 4th octet:
11111111.11111111.11111111.11000000)
Each block starts at multiples of 64 in the 4th octet:
0, 64, 128, 192.
Soln
--- page 4 ---
Now, given IP is 200.140.64.48, and 48 lies between 0 and 63.
So this IP belongs to the subnet that starts at .0.
Network address = 200.140.64.0 - 2 mark
Step — Find the broadcast (last) address
Add 63 (since 64 addresses per block, counting from 0):
0 + 63 = 63 → 200.140.64.63
Last address (broadcast address) = 200.140.64.63 – 2 mark
Step — Compute total number of addresses
2(32−26)=26=64
Total addresses = 64   - 1 mark
CO-   i) Explain the block coding method for error detection and correction. (2 marks)
2; SO-   ii)Two binary codewords are used in a communication system:
1;
BL-3   • C1 = 1001101
• C2 = 1110001
Compute the Hamming distance between C1 and C2 . (2 marks)
iii) A new codeword C3 = 1010101 is added to the set. Compute the pairwise
Hamming distances between C3 and the other codewords. (2 marks)
iv) Based on the minimum Hamming distance of the code, determine how many
errors the code can detect and how many it can correct. Justify your answer. (4
Q2 a   marks)   10
i) Explain the block coding method for error detection and correction. (2 marks)
•   In block coding, the message is divided into blocks, each of k bits, called
data words .
•   r redundant bits are added to each block to make the length n=k+r
• The resulting n bit blocks are called codewords. (1 mark)
• The block coding process is one-to-one; the same dataword is always
encoded as the same codeword.
• Message bits (k): The actual data to be sent
• Codeword bits (n): The message bits plus redundant bits
• Redundant bits (n - k): Extra bits added for error detection and correction
(1 mark)
Soln   ii) Compute the Hamming distance between C1 and C2
--- page 5 ---
Step : (1 mark)
Final answer: No of 1’s = 4 . Hence Hamming Distance = 4 (1 mark)
iii) A new codeword C3 = 1010101 is added to the set. Compute the pairwise
Hamming distances between C3 and the other codewords.
A. ( C3 = 1010101 ) vs ( C1 = 1001101 )
Steps to show (1 mark)
Hamming distance = 2   (1 mark)
B.( C3 = 1010101 ) vs ( C2 = 1110001 )
Steps to show (1 mark)
Hamming distance = 2   (1 mark)
iv) Determine error detection and correction capabilities
•   ( d(C_1, C_2) = 4 )
•   ( d(C_1, C_3) = 2 )
•   ( d(C_2, C_3) = 2 )
so, d{min} = 2   (1mark)
Error detection: (1 mark)
• A code can detect up to ( d_{min} - 1 ) errors.
•   So: can detect ( 2 - 1 = 1 ) error
Error correction: 0 error (1 mark)
Final concluding answer with justification (2 mark)
• Minimum distance = 2
• Can detect 1 error, correct 0 errors
CO-3;   A company wants to set up a network for smooth data transfer between its offices.
SO-1;   Based on your understanding, which switching technique—circuit, packet, or
BL-3   message—would you recommend? Explain how each works and compare their
Q2 b   pros, cons, and best use cases to support your choice.   10
Switchin
g   Working   Advantag   Disadvantag   Best Use
Techniq   Principle   es   es   Case
ue
Dedicated
Reliable,   Voice
path is   Inefficient
Circuit   continuou   communicatio
established   for data; idle
Switchin   s   n (e.g.,
before   time wastes
g   connectio   telephone
communicati   resources.
n.   networks).
Soln   on begins.
--- page 6 ---
Data is split
into packets   Efficient
sent   bandwidth
Packet   Possible   Internet, real-
independentl   usage;
Switchin   delays,   time data
y and   supports
g   packet loss.   transmission.
reassembled   multiple
at   users.
destination.
Entire
No need
message is
for   High delay   Email, non-
Message   stored and
dedicated   due to   real-time
Switchin forwarded
path;   storage at   communicatio
g   through
flexible   each node.   n.
intermediate
routing.
nodes.
Recommendation -Packet switching is recommended for the company’s network
due to its efficiency, scalability, and ability to handle diverse data types across
multiple branches.
Explanation of all three techniques (working principles)- 3 marks
Comparison of advantages and disadvantages -   3 marks
Identification of suitable applications-   2 marks
Justified recommendation based on scenario-   2 marks
BL 1,
CO 1,
SO 1 Q3 a   Define the following:- a) LAN b) MAN c)PAN d) WAN e) ARPANET   5
1 mark for each definition
a) LAN (Local Area Network):
A Local Area Network is a network that connects computers and devices within a
limited geographical area such as a home, school, office building, or campus.
• Example: A network connecting computers in a computer lab.
• Data transfer speed: High (typically 100 Mbps to 10 Gbps).
b) MAN (Metropolitan Area Network):
A Metropolitan Area Network covers a larger area than a LAN, usually spanning a
city or a large campus. It connects multiple LANs together within a metropolitan
area.
Soln
--- page 7 ---
• Example: A network connecting different branches of a university within a
city.
c) PAN (Personal Area Network):
A Personal Area Network is the smallest type of network, used for connecting
personal devices within a short range (usually within 10 meters).
• Example: Connecting a smartphone to a laptop via Bluetooth.
d) WAN (Wide Area Network):
A Wide Area Network covers a very large geographical area, often a country or
even globally. It connects multiple LANs and MANs using public networks like
the Internet or satellite links.
• Example: The Internet is the largest WAN.
e) ARPANET (Advanced Research Projects Agency Network):
ARPANET was the first operational packet-switching network and the precursor to
the modern Internet. It was developed in the late 1960s by the U.S. Department of
Defense’s ARPA (now DARPA) to connect research institutions and allow
resource sharing.
CO3,
BL2   Explain the different types of OSPF packets used for communication between
SO 1 Q3 b   routers.   5
OSPF uses five types of packets for communication between routers:
1. Hello Packet – Used to discover and maintain neighbor relationships.
2. Database Description (DBD) Packet – Used to summarize the contents of a
router’s link-state database.
3. Link-State Request (LSR) Packet – Sent to request specific link-state
information from a neighbor.
4. Link-State Update (LSU) Packet – Carries detailed link-state information
(LSAs) to other routers.
5. Link-State Acknowledgment (LSAck) Packet – Confirms the receipt of
LSUs to ensure reliable delivery.
Summary:
OSPF uses 5 packet types — Hello, DBD, LSR, LSU, and LSAck — to form
neighbors, exchange topology data, and keep the network synchronized.
Soln
CO5   Explain, with the help of a neat diagram, how the World Wide Web (WWW)
BL 2   enables users to access online information through the HTTP protocol. Describe
SO 1   the components and working mechanism of the Web, and interpret how HTTP
facilitates communication between a client and a server when a user enters a URL
Q3 c   such as http://www.example.com   10
The World Wide Web (WWW) is a global information system that enables users to
Soln.   access interlinked documents and multimedia content over the Internet. It operates
--- page 8 ---
on a client–server model, where the HTTP protocol governs communication
between browsers (clients) and web servers.
Diagram and explanation: WWW and HTTP Communication Flow (4 marks)
• Request–Response Model:
HTTP follows a simple two-way exchange — the client sends a request,
and the server responds.
•   Stateless Protocol:
Each request is independent, improving scalability and simplicity.
•   Structured Message Format:
o Request Line: Method, resource, version
o Headers: Metadata (host, content type, etc.)
o Body: Optional data (for POST requests)
•   Reliable Transport:
Uses TCP to ensure ordered, error-free data delivery.
•   Status Codes:
Help the browser understand response outcomes (e.g., 200 OK, 404 Not
Found).
Components of the World Wide Web (3 marks)
Component   Description
Application (e.g., Chrome, Firefox) used to send requests
Web Browser (Client)
display web pages.
Computer that stores and serves web pages when request
Web Server
clients.
--- page 9 ---
Uniform Resource   Unique address that identifies a specific web resource. Example:
Locator (URL)   http://www.example.com/index.html.
HTTP (Hypertext   Communication protocol used for transferring web documents
Transfer Protocol)   between browser and server.
HTML (Hypertext
Standard language used to structure and format web pages.
Markup Language)
Working Mechanism of the WWW (3 marks)
When a user types http://www.example.com in the browser:
1. URL Parsing:
The browser divides the URL into:
o Protocol → http
o Host name → www.example.com
o File/resource → default index.html
2. DNS Resolution:
The browser queries the DNS to obtain the IP address of the web server
hosting www.example.com.
3. Connection Establishment:
A TCP connection is initiated between the client and the server on port 80
(default for HTTP).
4. HTTP Request:
The browser sends an HTTP request message (e.g., GET /index.html
HTTP/1.1) asking for the web page.
5. HTTP Response:
The server locates the requested file, encapsulates it in an HTTP response
message with a status code and sends it back to the browser.
6. Rendering the Page:
The browser interprets the HTML, CSS, and scripts received and displays
the webpage to the user.
7. Connection Termination:
Once the transfer is complete, the TCP connection is closed.
CO-3
SO-1   Summarize the IPv6 address 0:15::1:12:1213 to its full, original form. Write a
BL-2   comparison between IPv4 and IPv6 packet headers.
Q4 a   10
First, we need to align the left side of the double colon (::) with the left side of the
original IPv6 address pattern, and the right side of the double colon with the right
side of the original pattern. This helps us determine how many groups of zeros we
need to replace the double colon with.
Soln
--- page 10 ---
For the given the address:
0:15::1:12:1213
We align the known parts as:
0:15: (left side), then the double colon ::, then 1:12:1213 (right side).
By counting how many groups of zeros are missing between the left and right parts
to complete the full 8-group IPv6 address, we find that the double colon represents
four groups of zeros.
Therefore, the original expanded address is:
0000:0015:0000:0000:0000:0001:0012:1213
Comparison between IPv4 and IPv6 packet headers:
➢ The header length field is removed in IPv6 because the header length is fixed
in this version.
➢ The service type field is also removed in IPv6. Instead, the priority and flow
label fields together perform the function that the service type field used to
handle.
➢ The total length field from IPv4 is replaced by the payload length field in
IPv6.
➢ The identification, flag, and offset fields are no longer part of the base header
in IPv6. Instead, they are included in a separate fragmentation extension
header.
➢ The TTL (Time To Live) field in IPv4 is renamed to hop limit in IPv6.
➢ The protocol field in IPv4 is replaced by the next header field in IPv6.
➢ The header checksum is eliminated in IPv6 because checksums are handled
by upper-layer protocols, so it is not needed at the IPv6 header level.
➢ The option fields that exist in IPv4 are implemented as extension headers in
IPv6.
(The IPv6 address 0:15::1:12:1213 to its full, original form-05M and
Any five point of comparison between IPv4 and IPv6 packet headers-05M)
BL- 2
CO-4   Describe the User Datagram Protocol (UDP) in detail with suitable diagram. Also
SO-1 Q4 b   explain how it differs from TCP?   10
(6 marks)
The User Datagram Protocol (UDP) is called a connectionless, unreliable transport
protocol. It does not add anything to the services of IP except to provide process-to-
process communication instead of host-to-host communication.
• The User Datagram Protocol (UDP) is called a connectionless, unreliable
transport protocol.
Soln
--- page 11 ---
•   It does not add anything to the services of IP except to provide process-to-
process communication instead of host-to-host communication.
•   It performs very limited error checking.
•   If UDP is so powerless, why would a process want to use it?
• UDP is a very simple protocol using a minimum of overhead.
•   If a process wants to send a small message and does not care much
about reliability, it can use UDP.
• Sending a small message by using UDP takes much less interaction
between the sender and receiver than using TCP (Transmission
control protocol) or SCTP (Stream control transmission protocol).
UDP Operations:
Connectionless Services: Each user datagram sent by UDP is an independent
datagram. There is no relationship between the different user datagrams even if they
are coming from the same source process and going to the same destination program.
The user datagrams are not numbered. Also, there is no connection establishment
and no connection termination, as is the case for TCP. This means that each user
datagram can travel on a different path. Each request must be small enough to fit
into one user datagram. Only those processes sending short messages should use
UDP.
Flow and Error Control:
UDP is a very simple, unreliable transport protocol. There is no flow control and
hence no window mechanism. The receiver may overflow with incoming messages.
There is no error control mechanism in UDP except for the checksum. This means
that the sender does not know if a message has been lost or duplicated. When the
receiver detects an error through the checksum, the user datagram is silently
discarded.
Encapsulation and Decapsulation:
To send a message from one process to another, the UDP protocol encapsulates and
decapsulates messages in an IP datagram.
--- page 12 ---
Encapsulation
When a process has a message to send through UDP, it passes the message to UDP
along with a pair of socket addresses and the length of data.
UDP receives the data and adds the UDP header.
UDP then passes the user datagram to IP with the socket addresses.
IP adds its own header, using the value 17 in the protocol field, indicating that the
data has come from the UDP protocol.
Decapsulation
When the message arrives at the destination host, the physical layer decodes the
signals into
bits and passes it to the data link layer.
The data link layer uses the header (and the trailer) to check the data. If there is no
error, the header and trailer are dropped and the datagram is passed to IP.
The IP software does its checking. If there is no error, the header is dropped and the
user datagram is passed to UDP with the sender and receiver IP addresses.
Queuing:
--- page 13 ---
(4 marks)
Transmission   Control   Protocol   User Datagram Protocol
Basis   (TCP)   (UDP)
UDP is the Datagram-
oriented protocol. This is
TCP is   a   connection-oriented   because there   is   no
protocol.   Connection orientation   overhead for opening a
means   that   the communicating   connection, maintaining
Type   of
devices   should   establish   a   a   connection,   or
Service
connection before transmitting data   terminating   a
and should close the connection after   connection. UDP   is
transmitting the data.   efficient for broadcast
and multicast types of
network transmission.
TCP is reliable as it guarantees the The delivery of data to
Reliability
delivery of data to the destination   the destination cannot be
router.   guaranteed in UDP.
Error   TCP   provides   extensive error- UDP has only the basic
checking   checking mechanisms. It is because   error-checking
mechanis   it   provides   flow   control and mechanism
m   acknowledgment of data.   using checksums.
Acknowle An acknowledgment segment   is No   acknowledgment
dgment   present.   segment.
--- page 14 ---
There is no sequencing
Sequencing of data is a feature of
of data in UDP. If the
Transmission   Control Protocol
Sequence   order is required, it has to
(TCP). this means that packets arrive
be managed by   the
in order at the receiver.
application layer.
UDP is faster, simpler,
TCP is comparatively slower than
Speed   and more efficient than
UDP.
TCP.
There   is   no
retransmission of   lost
Retransmi   Retransmission of lost packets is
packets   in   the User
ssion   possible in TCP, but not in UDP.
Datagram   Protocol
(UDP).
Header   TCP has a (20-60) bytes variable UDP has an 8 bytes
Length   length header.   fixed-length header.
Weight   TCP is heavy-weight.   UDP is lightweight.
Handshak
It's   a   connectionless
ing   Uses handshakes such as SYN,
protocol   i.e.   No
Technique ACK, SYN-ACK
handshake
s
Broadcast   UDP   supports
TCP doesn't support Broadcasting.
ing   Broadcasting.
CO-2,   Apply the principles of the Selective Repeat ARQ Sliding Window Protocol to
BL-3   determine the maximum permissible sender and receiver window sizes for frame
SO-1   sequence number field of 3 bits, and explain with the help of diagram how frames
are transmitted, acknowledged, and buffered at both the sender and receiver ends.
Justify why this window size is chosen, and analyze how incorrect window sizing
can lead to frame mis ordering or acknowledgment ambiguity.
Q5 a   10
--- page 15 ---
Explanation of Selective Repeat ARQ   (1 marks),
window size   (1marks),
explanation of frame transmission   (3 marks),
justification of window size 5 marks   ( 3 explanation and 2 marks diagram)
Solution: In Selective Repeat ARQ only the lost or error frames are retransmitted,
whereas correct frames are received and buffered. The receiver while keeping track
of sequence numbers buffers the frames in memory and sends NACK for only
frames which are missing or damaged. The sender will send/retransmit a packet for
which NACK is received.
Step 1 − Frame 0 sends from sender to receiver and set timer.
Step 2 − Without waiting for acknowledgement from the receiver another frame,
Frame1 is sent by sender by setting the timer for it.
Step 3 − In the same way frame2 is also sent to the receiver by setting the timer
without waiting for previous acknowledgement.
Step 4 − Whenever sender receives the ACK0 from receiver, within the frame 0
timer then it is closed and sent to the next frame, frame 3.
Step 5 − whenever the sender receives the ACK1 from the receiver, within the
frame 1 timer then it is closed and sent to the next frame, frame 4.
Step 6 − If the sender doesn’t receive the ACK2 from the receiver within the time
slot, it declares timeout for frame 2 and resends the frame 2 again, because it
thought the frame2 may be lost or damaged.
Soln
--- page 16 ---
Figure 11.23 Flow diagramfor Example 11.8

Sender Receiver

mn

O° Sf Sn . J R,
Request

Initial

Arrival

Request

Request

Arrival

Request

H wee — | [5[6[7] Arrival

1 n <Lo '
Fo H
Arrival '
Frame | (resend)
1 R,
1 a ps CK
Arrival t>fo111213 Arrival
H Frames 1,2,3
Y Y delivered

Window Sizes
We can now show why the size of the sender and receiver windows must be at most one-
half of 2”. For an example, we choose m = 2, which means the size of the window is 2”/2,
or 2. Figure 11.21 compares a window size of 2 with a window size of 3.

If the size of the window 1s 2 and all acknowledgments are lost, the timer for frame 0
expires and frame 0 is resent. However, the window of the receiver is now expecting

frame 2, not frame 0, so this duplicate frame is correctly discarded. When the size of
the window is 3 and all acknowledgments are lost, the sender sends a duplicate of
frame 0. However, this time, the window of the receiver expects to receive frame 0 (0 is
part of the window), so it accepts frame 0, not as a duplicate, but as the first frame in
the next cycle. This is clearly an error.

In Selective Repeat ARQ, the size of the sender and receiver window
must be at most one-half of 2””+
--- page 17 ---
BL: 2,   Explain SMTP and its role in email communication. Describe the different phases
SO: 2   of SMTP communication, detailing the purpose of each phase and the typical
CO: 5   commands used. Illustrate your answer with a labelled diagram showing the flow
Q5 b   between the client and server   10
SMTP Explanation: 2 marks
Diagram: 2 marks
Phases: 6 marks
•One of the most popular Internet services is electronic mail (e-mail).
•E-mail allow users to exchange messages. It is considered as a one-way transaction.
User Agent:
Soln
--- page 18 ---
•A user agent is a software package that composes , reads , replies to , and forwards
messages.
•Types of user agents:
Command driven
GUI based
•Mailing list: E-mail allows one name, an alias to represent several different e-mail
addresses
The protocol that defines the MTA client and server in the internet is called as
Simple Mail Transfer Protocol(SMTP)
•SMTP uses commands and responses to transfer messages between an MTA client
and MTA server.
•Commands: Keyword: argument(s)
•Responses: Responses are sent from the server to the client. A response is a three
digit code that may be followed by additional textual information
MAIL TRANSFER PHASES
Connection Establishment
1.The server sends code 220(service ready) to tell the client that it is ready to receive
mail. If the server is not ready it sends code 421(service not available)
2.The client sends the HELLO message to identify itself, using its domain name
address.
3.The server responds with code 250(request command completed)
Message transfers
1.The client sends the MAIL FROM message to introduce the sender of the message.
2.The server responds with code 250 or some other appropriate code.
3.The client sends the RCPT TO message, which includes the mail address of the
recipient.
--- page 19 ---
4.The server responds with code 250 or some other appropriate code.
5.The client sends the DATA message to initialize the message transfer.
6.The server responds with code 354(start mail input)
7.The client sends the contents of the message in consecutive lines.
8.The server responds with code 250 or some other appropriate code
Connection Termination
1.The client sends the QUIT command
2.The server responds with code 221(service closing transmission channel)
CO1
SO1
BL-1   List different types of unguided transmission media and write any two
Q6 a   characteristics of each.   5
Radio waves
Radio waves are Omnidirectional, useful for multicasting. AM and FM radio,
television, maritime radio, cordless phones, and paging are examples of
multicasting.
Radio waves a good candidate for long-distance broadcasting.
Advantage: receives signal inside a building
Disadvantage: Cannot isolate a communication
Microwaves
Microwave propagation is line-of-sight.
Soln
--- page 20 ---
Very high-frequency microwaves cannot penetrate walls
The microwave band is relatively wide, almost 299 GHz. Therefore wider
subbands can be assigned, and a high data rate is possible
Use of certain portions of the band requires permission from authorities.
Microwaves are used in cellular phones , satellite networks and
wireless LANs
Infrared Waves
Infrared signals can be used for short-range communication in a closed area using
line-of-sight propagation.
Infrared waves, having high frequencies, cannot penetrate walls.
The wide bandwidth can be used to transmit digital data with a very high data rate.
Infrared waves, having high frequencies, cannot penetrate walls.
The wide bandwidth can be used to transmit digital data with a very high data rate.
The recent standard defines a data rate of 4 Mbps.
CO2,
BL-4   Compare 1-persistent, non-persistent, and p-persistent CSMA strategies with
SO-1 Q6 b   diagrammatic representations   5
Points of 1-persistent, non-persistent, and p-persistent 1M each )- 3M , diagram
2M
1-Persistent CSMA
• Working:
The node listens to the channel.
Soln   o   If idle → transmit immediately.
--- page 21 ---
o   If busy → keep listening continuously and transmit immediately
when it becomes free.
•   Pros: Simple, high channel utilization.
• Cons: High chance of collisions if multiple nodes are waiting (because they
all send immediately once the channel is free).
Non-Persistent CSMA
• Working:
o The node listens to the channel.
o   If idle → transmit immediately.
o   If busy → does not continuously sense. Instead, it waits a random
backoff time and then checks again.
•   Pros: Lower chance of collisions.
• Cons: Higher delay, because nodes may wait even if the channel becomes
free.
p-Persistent CSMA (used in slotted channels, e.g., LANs)
• Working:
o The channel is divided into discrete time slots.
o When the channel is sensed idle:
▪ Transmit with probability p.
▪ Wait until the next time slot with probability 1 − p, then
repeat.
•   Pros: Balance between efficiency and collision probability; reduces chance
of many nodes transmitting at once.
• Cons: Performance depends on proper tuning of p.
CO-4
BL-2   Explain open loop and closed loop congestion control policy in transmission
SO-1 Q6 c   control protocol. Describe any two policies from each type.   10
--- page 22 ---
Open Loop: Open loop congestion control mechanisms try to remove the congestion
before it happens.
Works independently of feedback from the network.   ---- 1M
Closed Loop: Closed loop congestion control mechanisms try to remove the
congestion after it happens.
Uses feedback from the network (ACKs, packet loss, delays) to adjust transmission.
--- 1M
Open Loop Policies (any 2)   ----- 2 *2 = 4M
Retransmission Policy
• The sender retransmits a packet, if it feels that the packet it has sent is lost or
corrupted.
• However retransmission in general may increase the congestion in the network.
But we need to implement good retransmission policy to prevent congestion.
• The retransmission policy and the retransmission timers need to be designed to
optimize efficiency and at the same time prevent the congestion.
Window Policy
• To implement window policy, selective reject window method is used for
congestion control.
• Selective Reject method is preferred over Go-back-n window as in Go-back-n
method, when timer for a packet times out, several packets are resent, although some
may have arrived safely at the receiver. Thus, this duplication may make congestion
worse.
• Selective reject method sends only the specific lost or damaged packets.
Soln
--- page 23 ---
Acknowledgement Policy
• The acknowledgement policy imposed by the receiver may also affect congestion.
• If the receiver does not acknowledge every packet it receives, it may slow down
the sender and help prevent congestion.
• Acknowledgments also add to the traffic load on the network. Thus, by sending
fewer acknowledgements we can reduce load on the network.
• To implement it, several approaches can be used:
1. A receiver may send an acknowledgement only if it has a packet to be sent.
2. A receiver may also decide to acknowledge only N packets at a time.
Admission Policy
• An admission policy, which is a quality-of-service mechanism, can also prevent
congestion in virtual circuit networks.
• Switches in a flow first check the resource requirement of a flow before admitting
it to the network.
• A router can deny establishing a virtual circuit connection if there is congestion in
the "network or if there is a possibility of future congestion.
Closed Loop Policies (any 2)   ------- 2*2 = 4M
Backpressure
• Backpressure is a node-to-node congestion control that starts with a node and
propagates, in the opposite direction of data flow.
• The backpressure technique can be applied only to virtual circuit networks. In such
virtual circuit each node knows the upstream node from which a data flow is coming.
--- page 24 ---
• In this method of congestion control, the congested node stops receiving data from
the immediate upstream node or nodes.
• This may cause the upstream node on nodes to become congested, and they, in turn,
reject data from their upstream node or nodes.
• As shown in fig node 3 is congested and it stops receiving packets and informs its
upstream node 2 to slow down. Node 2 in turns may be congested and informs node
1 to slow down. Now node 1 may create congestion and informs the source node to
slow down. In this way the congestion is alleviated. Thus, the pressure on node 3 is
moved backward to the source to remove the congestion.
Choke Packet
• In this method of congestion control, congested router or node sends a special type
of packet called choke packet to the source to inform it about the congestion.
• Here, congested node does not inform its upstream node about the congestion as in
backpressure method.
• In choke packet method, congested node sends a warning directly to the source
station i.e. the intermediate nodes through which the packet has travelled are not
warned.
--- page 25 ---
CO3,   Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The
BL3,   directed edges between these nodes and their corresponding positive weights
4 ,   are given in the table below
SO2
Edge   Distance
A->B   4
A->C   2
B->C   5
B->D   10
C->D   3
C->E   4
D->E   1
D->F   2
E->F   3
F->G   5
Using Dijkstra’s Algorithm:
i. Determine the shortest path from the source node A to the destination node
G.
ii. Compute the shortest distance from node A to node G.
iii. Show all intermediate steps, including the initialization, selection of the
minimum distance node, for each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edge
Q7 a   10
Soln
--- page 26 ---
The shortest path A->C ->D->F->G, shortest distance is 12
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
(iii)   Intermediate Steps - 3marks
(iv)   Original network topology ( 1marks) + final shortest path
with the corresponding distance values clearly marked on
the edges ( 1 marks)
1) Edge costs
Edge Weight
A → B 4
A → C 2
B → C 5
B → D 10
C → D 3
C → E 4
D → E 1
D → F 2
E → F 3
F → G 5
2) Iteration table
--- page 27 ---
CO-4;
SO-1;   Draw a neat diagram and explain the working of the Token Bucket Algorithm.
BL-2 Q7 b   State any two limitations of the Token Bucket algorithm   10
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for
limitations.
Explanation of working based on the following points is expected.
• A bucket holds tokens, each token allowing the transmission of a certain
number of bytes (usually 1 token = 1 byte or 1 packet).
• Tokens are added to the bucket at a constant rate r (tokens per second).
• The bucket has a maximum capacity B (in tokens).
• When a packet arrives:
Soln
--- page 28 ---
o   If there are enough tokens, the packet is transmitted, and tokens are
removed from the bucket.
o   If not enough tokens, the packet is either delayed (until enough tokens
are available) or dropped (if there's no buffering).
This allows bursts of traffic up to B bytes to be sent at once (if the bucket is full),
but enforces an average rate of r bytes/sec over time.
Two Limitations of the Token Bucket Algorithm
1. Complexity with Bursty Traffic:
o While the algorithm allows short bursts, if traffic bursts are too
frequent or too large, it may still overwhelm downstream systems,
leading to queue overflows.
2. No Built-in Fairness or Priority:
o The algorithm does not distinguish between different types of traffic.
So, critical or high-priority packets can be delayed just like any
others, making   it unsuitable for quality of service (QoS)
differentiation without additional mechanisms.
````

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 3408b0ba5215

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/MBATech_IT_7041/Computer Networks/ANS_Computer Networks(702AI0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Dec 2025
- Text: mixed (24 pages), mean OCR confidence 28.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / III / IV/Semester III/Semester V/Semester VII(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 05 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 24 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
CO,
BL,   Mark
SO   Q No   Question   s
CO1   A university plans to set up a campus network. Apply the concepts of wired and
BL3   wireless communication to explain how each could be used in this network with
SO1   Q1 a   respect to speed, reliability and security.   5
Wired Communication (Ethernet, Fiber Optic):
• Implementation: Connecting classrooms, labs, and offices using Ethernet
cables or fiber optics.
• Speed: High data transfer rates; suitable for heavy traffic like video
streaming and large file transfers.
•   Reliability: Very reliable; less affected by interference or obstacles.
•   Security: More secure; physical access required to tap into the network.
Wireless Communication (Wi-Fi):
• Implementation: Providing connectivity to mobile devices, laptops, and
guest users via access points across the campus.
• Speed: Moderate; can be affected by distance, number of users, and
interference.
•   Reliability: Less reliable than wired; signal may degrade with obstacles or
high traffic.
•   Security: Requires encryption (WPA3/WPA2); more vulnerable to attacks
than wired networks.
Soln   Marking Scheme (5 Marks):
********** 1 **********
--- page 2 ---
Wired Communication-Correctly explains implementation, speed, reliability
and security- 2 Marks
Wireless Communication- Correctly explains implementation, speed, reliability
and security - 2 Marks
Explains practical usage of wired and wireless networks in campus context-1
Marks
CO1,
BL 2,
SO 1 Q1 b   Compare and contrast the TCP/IP model with the OSI model on any five points   5
▪ Number of Layers: OSI has seven layers, while the TCP/IP model
typically consists of four or five layers.
▪   Protocol Dependency: TCP/IP was developed from a protocol-driven
approach based on real-world protocols, while OSI is a theoretical model
that is protocol-independent.
▪ Layers Combined: The TCP/IP model combines the OSI's Session,
Presentation, and Application layers into a single "Application Layer" and
merges the Data Link and Physical layers into a "Network Access Layer".
▪   Reliability: The TCP/IP model's reliability features are primarily handled
by the Transport layer (TCP protocol), while the OSI model's reliability
mechanisms are spread across different layers.
▪ Usage: The TCP/IP model is the practical, widely implemented model
used for the internet. The OSI model is primarily used as a reference or
teaching tool.
Soln
CO 2
BL-2   In a Slotted ALOHA system, the average number of frames generated per frame
SO 1   time is G = 1. Calculate the throughput S. What is the maximum throughput in
Q1 c   Slotted ALOHA   5
(2MARKS)
•   It can be proven that the average number of successful transmissions for
slotted ALOHA is S = G *e^-G.
• The maximum throughput Smax is 0.368, when G = 1. In other words, if
one frame is generated during one frame transmission time, then 36.8
percent of these frames reach their destination successfully.
• We expect G = 1 to produce maximum throughput because the vulnerable
time is equal to the frame transmission time.
•   Therefore, if a station generates only one frame in this vulnerable time
(and no other station generates a frame during this time), the frame will
reach its destination successfully.
Soln
********** 2 **********
--- page 3 ---
(2MARKS)
Formula:
S=G×e^−G
Substitution:
S=1×e^−1
=1×0.3679
=0.368S
(1MARKS)
Throughput ≈ 0.368 (36.8%)
So throughput = 36.8% efficiency.
CO-3;
SO-2;
BL-3   A block of address is granted to a small organization and one of the address is
200.140.64.48/26. Determine the first address and last address in the block.
Q1 d   Determine the total number of addresses in the block.   5
IP address = 200.140.64.48/26
Step 1⃣   Interpret /26
• Subnet mask length = 26 bits
• So network part = 26 bits, host part = 32−26=6 bits.
That means:
• Number of addresses per block = 26=64
Step 2⃣ — Find the network (first) address
In dotted decimal:
/26 mask →
255.255.255.192
(because the 26th bit boundary falls inside the 4th octet:
Soln   11111111.11111111.11111111.11000000)
********** 3 **********
--- page 4 ---
Each block starts at multiples of 64 in the 4th octet:
0, 64, 128, 192.
Now, given IP is 200.140.64.48, and 48 lies between 0 and 63.
So this IP belongs to the subnet that starts at .0.
Network address = 200.140.64.0   - 2 mark
Step 3⃣ — Find the broadcast (last) address
Add 63 (since 64 addresses per block, counting from 0):
0 + 63 = 63 → 200.140.64.63
Last address (broadcast address) = 200.140.64.48 – 2 mark
Step 4️⃣ — Compute total number of addresses
2(32−26)=26=64
Total addresses = 64   - 1 mark
CO-   i) Explain the block coding method for error detection and correction. (2 marks)
2;   ii)Two binary codewords are used in a communication system:
SO-
1;   • C1 = 1001101
BL-3   • C2 = 1110001
Compute the Hamming distance between C1 and C2 . (2 marks)
iii) A new codeword C3 = 1010101 is added to the set. Compute the pairwise
Hamming distances between C3 and the other codewords. (2 marks)
iv) Based on the minimum Hamming distance of the code, determine how many
errors the code can detect and how many it can correct. Justify your answer. (4
Q2 a   marks)   10
i) Explain the block coding method for error detection and correction. (2 marks)
•   In block coding, the message is divided into blocks, each of k bits,
called data words .
•   r redundant bits are added to each block to make the length n=k+r
• The resulting n bit blocks are called codewords. (1 mark)
• The block coding process is one-to-one; the same dataword is always
encoded as the same codeword.
• Message bits (k): The actual data to be sent
• Codeword bits (n): The message bits plus redundant bits
• Redundant bits (n - k): Extra bits added for error detection and
correction (1 mark)
ii) Compute the Hamming distance between C1 and C2
Step : (1 mark)
Final answer: No of 1’s = 4️ . Hence Hamming Distance = 4️ (1
mark)
Soln
********** 4 **********
--- page 5 ---
iii) A new codeword C3 = 1010101 is added to the set. Compute the pairwise
Hamming distances between C3 and the other codewords.
A. ( C3 = 1010101 ) vs ( C1 = 1001101 )
Steps to show (1 mark)
Hamming distance = 2   (1 mark)
B.( C3 = 1010101 ) vs ( C2 = 1110001 )
Steps to show (1 mark)
Hamming distance = 2   (1 mark)
iv) Determine error detection and correction capabilities
•   ( d(C_1, C_2) = 4 )
•   ( d(C_1, C_3) = 2 )
•   ( d(C_2, C_3) = 2 )
so, d{min} = 2   (1mark)
Error detection: (1 mark)
• A code can detect up to ( d_{min} - 1 ) errors.
•   So: can detect ( 2 - 1 = 1 ) error
Error correction: 0 error (1 mark)
Final concluding answer with justification (2 mark)
• Minimum distance = 2
• Can detect 1 error, correct 0 errors
CO-3;   A company wants to set up a network for smooth data transfer between its
SO-1;   offices. Based on your understanding, which switching technique—circuit,
BL-3   packet, or message—would you recommend? Explain how each works and
Q2 b   compare their pros, cons, and best use cases to support your choice.   10
Switchin
g   Working   Advantag Disadvantag   Best Use
Techniq   Principle   es   es   Case
ue
Dedicated
Reliable,   Voice
path is   Inefficient
Circuit   continuou   communicati
established   for data; idle
Switchin   s   on (e.g.,
before   time wastes
g   connectio   telephone
communicati   resources.
n.   networks).
on begins.
Data is split
into packets   Efficient
sent   bandwidt
Packet   Possible   Internet, real-
independentl h usage;
Switchin   delays,   time data
y and   supports
g   packet loss.   transmission.
reassembled   multiple
at   users.
Soln   destination.
********** 5 **********
--- page 6 ---
Entire
No need
message is
for   High delay   Email, non-
Message   stored and
dedicated due to   real-time
Switchin forwarded
path;   storage at   communicati
g   through
flexible   each node.   on.
intermediate
routing.
nodes.
Recommendation -Packet switching is recommended for the company’s
network due to its efficiency, scalability, and ability to handle diverse data
types across multiple branches.
Explanation of all three techniques (working principles)- 3 marks
Comparison of advantages and disadvantages -   3 marks
Identification of suitable applications-   2 marks
Justified recommendation based on scenario-   2 marks
BL 1,
CO 1,
SO 1 Q3 a   Define the following:- a) LAN b) MAN c)PAN d) WAN e) ARPANET   5
1 mark for each definition
a) LAN (Local Area Network):
A Local Area Network is a network that connects computers and devices within
a limited geographical area such as a home, school, office building, or campus.
• Example: A network connecting computers in a computer lab.
• Data transfer speed: High (typically 100 Mbps to 10 Gbps).
b) MAN (Metropolitan Area Network):
A Metropolitan Area Network covers a larger area than a LAN, usually
spanning a city or a large campus. It connects multiple LANs together within a
metropolitan area.
• Example: A network connecting different branches of a university
within a city.
c) PAN (Personal Area Network):
A Personal Area Network is the smallest type of network, used for connecting
personal devices within a short range (usually within 10 meters).
• Example: Connecting a smartphone to a laptop via Bluetooth.
d) WAN (Wide Area Network):
A Wide Area Network covers a very large geographical area, often a country or
even globally. It connects multiple LANs and MANs using public networks like
the Internet or satellite links.
Soln
********** 6 **********
--- page 7 ---
• Example: The Internet is the largest WAN.
e) ARPANET (Advanced Research Projects Agency Network):
ARPANET was the first operational packet-switching network and the
precursor to the modern Internet. It was developed in the late 1960s by the U.S.
Department of Defense’s ARPA (now DARPA) to connect research institutions
and allow resource sharing.
CO3,
BL2   Explain the different types of OSPF packets used for communication between
SO 1 Q3 b   routers.   5
OSPF uses five types of packets for communication between routers:
1. Hello Packet – Used to discover and maintain neighbor relationships.
2. Database Description (DBD) Packet – Used to summarize the contents
of a router’s link-state database.
3. Link-State Request (LSR) Packet – Sent to request specific link-state
information from a neighbor.
4. Link-State Update (LSU) Packet – Carries detailed link-state
information (LSAs) to other routers.
5. Link-State Acknowledgment (LSAck) Packet – Confirms the receipt
of LSUs to ensure reliable delivery.
Summary:
OSPF uses 5 packet types — Hello, DBD, LSR, LSU, and LSAck — to form
neighbors, exchange topology data, and keep the network synchronized.
Soln
CO5   Explain, with the help of a neat diagram, how the World Wide Web (WWW)
BL 2   enables users to access online information through the HTTP protocol. Describe
SO 1   the components and working mechanism of the Web, and interpret how HTTP
facilitates communication between a client and a server when a user enters a
Q3 c   URL such as http://www.example.com   10
The World Wide Web (WWW) is a global information system that enables
users to access interlinked documents and multimedia content over the Internet.
It operates on a client–server model, where the HTTP protocol governs
Soln.   communication between browsers (clients) and web servers.
********** 7 **********
--- page 8 ---
Diagram and explanation: WWW and HTTP Communication Flow (4
marks)
• Request–Response Model:
HTTP follows a simple two-way exchange — the client sends a request,
and the server responds.
•   Stateless Protocol:
Each request is independent, improving scalability and simplicity.
• Structured Message Format:
o Request Line: Method, resource, version
o Headers: Metadata (host, content type, etc.)
o Body: Optional data (for POST requests)
• Reliable Transport:
Uses TCP to ensure ordered, error-free data delivery.
• Status Codes:
Help the browser understand response outcomes (e.g., 200 OK, 404
Not Found).
Components of the World Wide Web (3 marks)
Component   Description
Application (e.g., Chrome, Firefox) used to send reque
Web Browser (Client)
display web pages.
Computer that stores and serves web pages when reque
Web Server
clients.
Uniform Resource   Unique address that identifies a specific web resource.
Locator (URL)   Example: http://www.example.com/index.html.
HTTP (Hypertext   Communication protocol used for transferring web doc
Transfer Protocol)   between browser and server.
HTML (Hypertext
Standard language used to structure and format web pa
Markup Language)
Working Mechanism of the WWW (3 marks)
********** 8 **********
--- page 9 ---
When a user types http://www.example.com in the browser:
1. URL Parsing:
The browser divides the URL into:
o Protocol → http
o Host name → www.example.com
o File/resource → default index.html
2. DNS Resolution:
The browser queries the DNS to obtain the IP address of the web server
hosting www.example.com.
3. Connection Establishment:
A TCP connection is initiated between the client and the server on port
80 (default for HTTP).
4. HTTP Request:
The browser sends an HTTP request message (e.g., GET
/index.html HTTP/1.1) asking for the web page.
5. HTTP Response:
The server locates the requested file, encapsulates it in an HTTP
response message with a status code and sends it back to the browser.
6. Rendering the Page:
The browser interprets the HTML, CSS, and scripts received and
displays the webpage to the user.
7. Connection Termination:
Once the transfer is complete, the TCP connection is closed.
CO-3
SO-1
BL-2   Summarize the IPv6 address 0:15::1:12:1213 to its full, original form. Write a
Q4 a   comparison between IPv4 and IPv6 packet headers.   10
First, we need to align the left side of the double colon (::) with the left side of
the original IPv6 address pattern, and the right side of the double colon with the
right side of the original pattern. This helps us determine how many groups of
zeros we need to replace the double colon with.
For the given the address:
0:15::1:12:1213
We align the known parts as:
0:15: (left side), then the double colon ::, then 1:12:1213 (right side).
By counting how many groups of zeros are missing between the left and right
parts to complete the full 8-group IPv6 address, we find that the double colon
represents four groups of zeros.
Therefore, the original expanded address is:
0000:0015:0000:0000:0000:0001:0012:1213
Comparison between IPv4 and IPv6 packet headers:
➢ The header length field is removed in IPv6 because the header length is
Soln   fixed in this version.
********** 9 **********
--- page 10 ---
➢ The service type field is also removed in IPv6. Instead, the priority and
flow label fields together perform the function that the service type field
used to handle.
➢ The total length field from IPv4 is replaced by the payload length field in
IPv6.
➢ The identification, flag, and offset fields are no longer part of the base
header in IPv6. Instead, they are included in a separate fragmentation
extension header.
➢ The TTL (Time To Live) field in IPv4 is renamed to hop limit in IPv6.
➢ The protocol field in IPv4 is replaced by the next header field in IPv6.
➢ The header checksum is eliminated in IPv6 because checksums are
handled by upper-layer protocols, so it is not needed at the IPv6 header
level.
➢ The option fields that exist in IPv4 are implemented as extension headers
in IPv6.
(The IPv6 address 0:15::1:12:1213 to its full, original form-05M and
Any five point of comparison between IPv4 and IPv6 packet headers-05M)
BL- 2
CO-4   Describe the User Datagram Protocol (UDP) in detail with suitable diagram.
SO-1 Q4 b   Also explain how it differs from TCP?   10
The User Datagram Protocol (UDP) is called a connectionless, unreliable
transport protocol. It does not add anything to the services of IP except to provide
process-to-process communication instead of host-to-host communication.
• The User Datagram Protocol (UDP) is called a connectionless, unreliable
transport protocol.
•   It does not add anything to the services of IP except to provide process-
to-process communication instead of host-to-host communication.
•   It performs very limited error checking.
•   If UDP is so powerless, why would a process want to use it?
• UDP is a very simple protocol using a minimum of overhead.
•   If a process wants to send a small message and does not care much
about reliability, it can use UDP.
• Sending a small message by using UDP takes much less interaction
between the sender and receiver than using TCP (Transmission
control protocol) or SCTP (Stream control transmission protocol).
UDP Operations:
Connectionless Services: Each user datagram sent by UDP is an independent
datagram. There is no relationship between the different user datagrams even if
they are coming from the same source process and going to the same destination
program. The user datagrams are not numbered. Also, there is no connection
establishment and no connection termination, as is the case for TCP. This means
Soln   that each user datagram can travel on a different path. Each request must be small
********** 10 **********
--- page 11 ---
enough to fit into one user datagram. Only those processes sending short
messages should use UDP.
Flow and Error Control:
UDP is a very simple, unreliable transport protocol. There is no flow control and
hence no window mechanism. The receiver may overflow with incoming
messages.
There is no error control mechanism in UDP except for the checksum. This means
that the sender does not know if a message has been lost or duplicated. When the
receiver detects an error through the checksum, the user datagram is silently
discarded.
Encapsulation and Decapsulation:
To send a message from one process to another, the UDP protocol encapsulates
and decapsulates messages in an IP datagram.
Encapsulation
When a process has a message to send through UDP, it passes the message to
UDP along with a pair of socket addresses and the length of data.
UDP receives the data and adds the UDP header.
UDP then passes the user datagram to IP with the socket addresses.
IP adds its own header, using the value 17 in the protocol field, indicating that
the data has come from the UDP protocol.
Decapsulation
When the message arrives at the destination host, the physical layer decodes the
signals into
bits and passes it to the data link layer.
The data link layer uses the header (and the trailer) to check the data. If there is
no error, the header and trailer are dropped and the datagram is passed to IP.
The IP software does its checking. If there is no error, the header is dropped and
the user datagram is passed to UDP with the sender and receiver IP addresses.
Queuing:
********** 11 **********
--- page 12 ---
Transmission   Control   Protocol   User Datagram Protocol
Basis   (TCP)   (UDP)
UDP is the Datagram-
oriented protocol. This
is because there is no
TCP is   a   connection-oriented
overhead for opening a
protocol.   Connection orientation
connection,
means that the communicating
Type   of   maintaining   a
devices   should   establish   a
Service   connection,   or
connection before transmitting data
terminating   a
and should close the connection
connection. UDP   is
after transmitting the data.
efficient for broadcast
and multicast types of
network transmission.
TCP is reliable as it guarantees the The delivery of data to
Reliabilit
delivery of data to the destination   the destination cannot
y
router.   be guaranteed in UDP.
Error   TCP   provides   extensive error- UDP has only the basic
checking   checking mechanisms. It is because   error-checking
mechanis   it provides flow   control and mechanism
m   acknowledgment of data.   using checksums.
Acknowle An acknowledgment segment is No   acknowledgment
dgment   present.   segment.
********** 12 **********
--- page 13 ---
There is no sequencing
Sequencing of data is a feature of
of data in UDP. If the
Transmission   Control Protocol
Sequence   order is required, it has
(TCP). this means that packets
to be managed by the
arrive in order at the receiver.
application layer.
UDP is faster, simpler,
TCP is comparatively slower than
Speed   and more efficient than
UDP.
TCP.
There   is   no
retransmission of lost
Retransmi   Retransmission of lost packets is
packets in the User
ssion   possible in TCP, but not in UDP.
Datagram   Protocol
(UDP).
Header   TCP has a (20-60) bytes variable UDP has an 8 bytes
Length   length header.   fixed-length header.
Weight   TCP is heavy-weight.   UDP is lightweight.
Handshak
It's a connectionless
ing   Uses handshakes such as SYN,
protocol   i.e.   No
Techniqu   ACK, SYN-ACK
handshake
es
Broadcast   UDP   supports
TCP doesn't support Broadcasting.
ing   Broadcasting.
CO-2,   Apply the principles of the Selective Repeat ARQ Sliding Window Protocol to
BL-3   determine the maximum permissible sender and receiver window sizes for
SO-1   frame sequence number field of 3 bits, and explain with the help of diagram
how frames are transmitted, acknowledged, and buffered at both the sender and
receiver ends.
Justify why this window size is chosen, and analyze how incorrect window
Q5 a   sizing can lead to frame mis ordering or acknowledgment ambiguity.   10
Explanation of Selective Repeat ARQ   (1 marks),
window size   (1marks),
Soln   explanation of frame transmission   (3 marks),
********** 13 **********
--- page 14 ---
justification of window size 5 marks   ( 3 explanation and 2 marks
diagram)
Solution: In Selective Repeat ARQ only the lost or error frames are
retransmitted, whereas correct frames are received and buffered. The receiver
while keeping track of sequence numbers buffers the frames in memory and
sends NACK for only frames which are missing or damaged. The sender will
send/retransmit a packet for which NACK is received.
Step 1 − Frame 0 sends from sender to receiver and set timer.
Step 2 − Without waiting for acknowledgement from the receiver another
frame, Frame1 is sent by sender by setting the timer for it.
Step 3 − In the same way frame2 is also sent to the receiver by setting the timer
without waiting for previous acknowledgement.
Step 4 − Whenever sender receives the ACK0 from receiver, within the frame 0
timer then it is closed and sent to the next frame, frame 3.
Step 5 − whenever the sender receives the ACK1 from the receiver, within the
frame 1 timer then it is closed and sent to the next frame, frame 4.
Step 6 − If the sender doesn’t receive the ACK2 from the receiver within the
time slot, it declares timeout for frame 2 and resends the frame 2 again, because
it thought the frame2 may be lost or damaged.
********** 14 **********
--- page 15 ---
BL:   Explain SMTP and its role in email communication. Describe the different
2,   phases of SMTP communication, detailing the purpose of each phase and the
SO: 2   typical commands used. Illustrate your answer with a labelled diagram showing
CO: 5 Q5 b   the flow between the client and server   10
SMTP Explanation: 2 marks
Diagram: 2 marks
Phases: 6 marks
Soln   •One of the most popular Internet services is electronic mail (e-mail).
********** 15 **********
--- page 16 ---
•E-mail allow users to exchange messages. It is considered as a one-way
transaction.
User Agent:
•A user agent is a software package that composes , reads , replies to , and
forwards messages.
•Types of user agents:
Command driven
GUI based
•Mailing list: E-mail allows one name, an alias to represent several different e-
mail addresses
The protocol that defines the MTA client and server in the internet is called as
Simple Mail Transfer Protocol(SMTP)
•SMTP uses commands and responses to transfer messages between an MTA
client and MTA server.
•Commands: Keyword: argument(s)
•Responses: Responses are sent from the server to the client. A response is a three
digit code that may be followed by additional textual information
MAIL TRANSFER PHASES
Connection Establishment
********** 16 **********
--- page 17 ---
1.The server sends code 220(service ready) to tell the client that it is ready to
receive mail. If the server is not ready it sends code 421(service not available)
2.The client sends the HELLO message to identify itself, using its domain name
address.
3.The server responds with code 250(request command completed)
Message transfers
1.The client sends the MAIL FROM message to introduce the sender of the
message.
2.The server responds with code 250 or some other appropriate code.
3.The client sends the RCPT TO message, which includes the mail address of the
recipient.
4.The server responds with code 250 or some other appropriate code.
5.The client sends the DATA message to initialize the message transfer.
6.The server responds with code 354(start mail input)
7.The client sends the contents of the message in consecutive lines.
8.The server responds with code 250 or some other appropriate code
Connection Termination
1.The client sends the QUIT command
2.The server responds with code 221(service closing transmission channel)
CO1
SO1   List different types of unguided transmission media and write any two
BL-1 Q6 a   characteristics of each.   5
Radio waves
Radio waves are Omnidirectional, useful for multicasting. AM and FM radio,
television, maritime radio, cordless phones, and paging are examples of
multicasting.
Radio waves a good candidate for long-distance broadcasting.
Advantage: receives signal inside a building
Soln   Disadvantage: Cannot isolate a communication
********** 17 **********
--- page 18 ---
Microwaves
Microwave propagation is line-of-sight.
Very high-frequency microwaves cannot penetrate walls
The microwave band is relatively wide, almost 299 GHz. Therefore wider
subbands can be assigned, and a high data rate is possible
Use of certain portions of the band requires permission from authorities.
Microwaves are used in cellular phones , satellite networks and
wireless LANs
Infrared Waves
Infrared signals can be used for short-range communication in a closed area
using line-of-sight propagation.
Infrared waves, having high frequencies, cannot penetrate walls.
The wide bandwidth can be used to transmit digital data with a very high data
rate.
Infrared waves, having high frequencies, cannot penetrate walls.
The wide bandwidth can be used to transmit digital data with a very high data
rate.
The recent standard defines a data rate of 4 Mbps.
CO2,
BL-4   Compare 1-persistent, non-persistent, and p-persistent CSMA strategies with
SO-1 Q6 b   diagrammatic representations   5
Points of 1-persistent, non-persistent, and p-persistent 1M each )- 3M , diagram
2M
1-Persistent CSMA
• Working:
The node listens to the channel.
o   If idle → transmit immediately.
o   If busy → keep listening continuously and transmit immediately
when it becomes free.
•   Pros: Simple, high channel utilization.
• Cons: High chance of collisions if multiple nodes are waiting (because
they all send immediately once the channel is free).
Non-Persistent CSMA
• Working:
o The node listens to the channel.
Soln   o   If idle → transmit immediately.
********** 18 **********
--- page 19 ---
o   If busy → does not continuously sense. Instead, it waits a random
backoff time and then checks again.
•   Pros: Lower chance of collisions.
• Cons: Higher delay, because nodes may wait even if the channel
becomes free.
p-Persistent CSMA (used in slotted channels, e.g., LANs)
• Working:
o The channel is divided into discrete time slots.
o When the channel is sensed idle:
▪ Transmit with probability p.
▪ Wait until the next time slot with probability 1 − p, then
repeat.
•   Pros: Balance between efficiency and collision probability; reduces
chance of many nodes transmitting at once.
• Cons: Performance depends on proper tuning of p.
CO-4
BL-2
SO-1   Explain open loop and closed loop congestion control policy in transmission
Q6 c   control protocol. Describe any two policies from each type.   10
Open Loop: Open loop congestion control mechanisms try to remove the
congestion before it happens.
Works independently of feedback from the network.   ---- 1M
Closed Loop: Closed loop congestion control mechanisms try to remove the
congestion after it happens.
Uses feedback from the network (ACKs, packet loss, delays) to adjust
transmission.
--- 1M
Open Loop Policies (any 2)   -----   2 *2 = 4M
Soln
********** 19 **********
--- page 20 ---
Retransmission Policy
• The sender retransmits a packet, if it feels that the packet it has sent is lost or
corrupted.
• However retransmission in general may increase the congestion in the network.
But we need to implement good retransmission policy to prevent congestion.
• The retransmission policy and the retransmission timers need to be designed to
optimize efficiency and at the same time prevent the congestion.
Window Policy
• To implement window policy, selective reject window method is used for
congestion control.
• Selective Reject method is preferred over Go-back-n window as in Go-back-n
method, when timer for a packet times out, several packets are resent, although
some may have arrived safely at the receiver. Thus, this duplication may make
congestion worse.
• Selective reject method sends only the specific lost or damaged packets.
Acknowledgement Policy
• The acknowledgement policy imposed by the receiver may also affect
congestion.
• If the receiver does not acknowledge every packet it receives, it may slow down
the sender and help prevent congestion.
• Acknowledgments also add to the traffic load on the network. Thus, by sending
fewer acknowledgements we can reduce load on the network.
• To implement it, several approaches can be used:
1. A receiver may send an acknowledgement only if it has a packet to be sent.
2. A receiver may also decide to acknowledge only N packets at a time.
Admission Policy
• An admission policy, which is a quality-of-service mechanism, can also prevent
congestion in virtual circuit networks.
• Switches in a flow first check the resource requirement of a flow before
admitting it to the network.
• A router can deny establishing a virtual circuit connection if there is congestion
in the "network or if there is a possibility of future congestion.
********** 20 **********
--- page 21 ---
Closed Loop Policies (any 2)   ------- 2*2 = 4M
Backpressure
• Backpressure is a node-to-node congestion control that starts with a node and
propagates, in the opposite direction of data flow.
• The backpressure technique can be applied only to virtual circuit networks. In
such virtual circuit each node knows the upstream node from which a data flow
is coming.
• In this method of congestion control, the congested node stops receiving data
from the immediate upstream node or nodes.
• This may cause the upstream node on nodes to become congested, and they, in
turn, reject data from their upstream node or nodes.
• As shown in fig node 3 is congested and it stops receiving packets and informs
its upstream node 2 to slow down. Node 2 in turns may be congested and informs
node 1 to slow down. Now node 1 may create congestion and informs the source
node to slow down. In this way the congestion is alleviated. Thus, the pressure
on node 3 is moved backward to the source to remove the congestion.
Choke Packet
• In this method of congestion control, congested router or node sends a special
type of packet called choke packet to the source to inform it about the congestion.
• Here, congested node does not inform its upstream node about the congestion
as in backpressure method.
• In choke packet method, congested node sends a warning directly to the source
station i.e. the intermediate nodes through which the packet has travelled are not
warned.
********** 21 **********
--- page 22 ---
CO3,   Consider a network topology consisting of nodes A, B, C, D, E, F, and G.
BL3,   The directed edges between these nodes and their corresponding positive
4 ,   weights are given in the table below
SO2
Edge   Distance
A->B   4
A->C   2
B->C   5
B->D   10
C->D   3
C->E   4
D->E   1
D->F   2
E->F   3
F->G   5
Using Dijkstra’s Algorithm:
i. Determine the shortest path from the source node A to the destination
node G.
ii. Compute the shortest distance from node A to node G.
iii. Show all intermediate steps, including the initialization, selection of the
minimum distance node, for each iteration.
iv.   Illustrate the original network topology and the final shortest path with
the corresponding distance values clearly marked on the edge
Q7 a   10
The shortest path A->C ->D->F->G, shortest distance is 12
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
(iii)   Intermediate Steps - 3marks
(iv)   Original network topology ( 1marks) + final shortest
path with the corresponding distance values clearly
marked on the edges ( 1 marks)
Soln
CO-4;
SO-1;   Draw a neat diagram and explain the working of the Token Bucket Algorithm.
BL-2 Q7 b   State any two limitations of the Token Bucket algorithm   10
********** 22 **********
--- page 23 ---
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for
limitations.
Explanation of working based on the following points is expected.
• A bucket holds tokens, each token allowing the transmission of a certain
number of bytes (usually 1 token = 1 byte or 1 packet).
• Tokens are added to the bucket at a constant rate r (tokens per second).
• The bucket has a maximum capacity B (in tokens).
• When a packet arrives:
o   If there are enough tokens, the packet is transmitted, and tokens
are removed from the bucket.
o   If not enough tokens, the packet is either delayed (until enough
tokens are available) or dropped (if there's no buffering).
This allows bursts of traffic up to B bytes to be sent at once (if the bucket is full),
but enforces an average rate of r bytes/sec over time.
Two Limitations of the Token Bucket Algorithm
1. Complexity with Bursty Traffic:
o While the algorithm allows short bursts, if traffic bursts are too
frequent or too large, it may still overwhelm downstream systems,
leading to queue overflows.
2. No Built-in Fairness or Priority:
o The algorithm does not distinguish between different types of
traffic. So, critical or high-priority packets can be delayed just like
any others, making it unsuitable for quality of service (QoS)
Soln   differentiation without additional mechanisms.
********** 23 **********
--- page 24 ---
FRR IRD AC HOH
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 050265d8b3bf

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CSBS_7036/Computer Networks/ANS_Computer Networks(702AI0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSBS)
Year: II / III/Semester IV/Semester VI(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures on the right-hand side indicate full marks.
Q1
Answer briefly:   [20]
CO-1;   a.   Discuss all types of guided transmission media in communication.   [5]
BL-2
Ans.   Explanation of guided transmission media – [3 marks]
Diagrams – 2 marks
Guided media, which are those that provide a conduit from one device to
another, include twisted-pair cable, coaxial cable, and fiber-optic cable.
Twisted-Pair Cable
Coaxial Cable
Coaxial cable has an inner conductor that is surrounded by an insulating
layer, which has conductive shielding around it.
********** 1 **********
--- page 2 ---
Fiber-Optic Cable
A fiber-optic cable is composed of very thin strands of glass or plastic
known as optical fibers.
b.   Draw and explain the procedure for the pure ALOHA protocol. Describe
how vulnerable time is calculated in pure ALOHA with the following.
CO-2;   [5]
BL-3   A pure ALOHA network transmits 300bit frames on a shared channel of
200 kbps. Calculate the vulnerable time.
Ans.   Pure ALOHA explanation – 3 marks
◼ The original ALOHA protocol is called pure ALOHA.
◼ The idea is that each station sends a frame whenever it has a frame
to send.
◼ However, since there is only one channel to share, there is the
possibility of collision between frames from different stations
Vulnerable time calculation – 2 marks
Vulnerable Time=2×Tf
Vulnerable Time=2×1.5 ms=3 ms
Vulnerable Time=3 ms
c.   Illustrate the work of ARP and RARP with examples and differentiate
CO-3;   [5]
BL-2   them.
Ans. ARP explanation with example 2 marks
********** 2 **********
--- page 3 ---
RARP explanation with example 2 marks
Difference 1 mark
ARP associates an Internet Protocol (IP) address with its physical
address. On a typical physical network, such as a LAN, each device on a
link is identified by a physical or station address that is usually imprinted
on the network interface card (NIC).
An ARP request is broadcast; an ARP reply is unicast.
RARP finds the logical address for a machine that only knows its
physical address.
The RARP request packets are broadcast; the RARP reply packets are
unicast.
d.   Describe the token bucket algorithm in traffic shaping with a suitable
CO-4;   diagram and example to justify the improvement in the quality of [5]
BL-2
services.
Ans.   Quality of Services improvement 1 mark
Token Bucket algorithm with diagram 4 marks
Token Bucket
• The leaky bucket is very restrictive. It does not credit an idle host.
• For example, if a host is not sending for a while, its bucket
becomes empty.
• Now if the host has bursty data, the leaky bucket allows only an
average rate. The time when the host was idle is not taken into
account.
• On the other hand, the token bucket algorithm allows idle hosts to
accumulate credit for the future in the form of tokens.
•   Let’s assume that the bucket capacity is 10,000 tokens and tokens
are added at the rate of 1000 tokens per second.
•   If the system is idle for 10 seconds (or more), the bucket collects
10,000 tokens and becomes full.
•   In other words, the host can send bursty data as long as the bucket
is not empty.
• The token bucket allows bursty traffic at a regulated maximum
rate.
********** 3 **********
--- page 4 ---
Q2   a.   Explain the CSMA protocol in the data link layer. Describe all types of
[10]
CO-2;   persistence methods of CSMA with their advantages and disadvantages.
BL-2
Ans. CSMA explanation 1 marks
1-persistent CSMA with advantages and disadvantages 3 marks
p-persistent CSMA with advantages and disadvantages 3 marks
non-persistent CSMA with advantages and disadvantages 3 marks
********** 4 **********
--- page 5 ---
b.   Elaborate on the concept of 3-way handshaking in the TCP protocol and
CO-4;
how it improves the reliability as compared to UDP. Define the SCTP   [10]
BL-2
protocol with its applications.
Ans. 3-way handshaking explanation – 3 marks
Improvement of reliability – 3 marks
SCTP with application – 4 marks
TCP 3 way Handshake Process
The TCP (Transmission Control Protocol) connection establishment
follows a three-way handshake process to ensure that both the client and
the server are ready to exchange data.
A SYN segment cannot carry data, but it consumes one sequence
number.
A SYN + ACK segment cannot carry data, but does consume one
sequence number.
An ACK segment, if carrying no data, consumes no sequence number.
After this three-way handshake, the client and server can start
transmitting data in both directions.
The FIN segment consumes one sequence number if it does
not carry data.
********** 5 **********
--- page 6 ---
The FIN + ACK segment consumes one sequence number if it
does not carry data.
SCTP
Stream Control Transmission   Protocol (SCTP) is a new reliable,
message-oriented transport layer protocol. SCTP is a message-oriented,
reliable protocol that combines the best features of UDP and TCP. An
association in SCTP can involve multiple streams. SCTP association
allows multiple IP addresses for each end. In SCTP, a data chunk is
numbered using a Transmission Sequence Number (TSN). To
distinguish between different streams, SCTP uses an Stream Identifier
(SI). To distinguish between different data chunks belonging to the
same stream, SCTP uses Stream Sequence Numbers (SSN). TCP has
segments; SCTP has packets.
a.   Evaluate the final routing table of each node using RIP routing protocol.
Show all steps to determine the final routing table of at least one node.
Discuss the count to infinity problem in RIP with an example.
Q3
[10]
CO-3;
BL-3
Ans.   Routing table of each node 4 marks
Detail steps for one node is 3 marks
Count to infinity problem 3 marks
Final Routing Tables (All Nodes)
The final state represents the shortest path from each node to every
other node in the network.
Final Routing Tables (All Nodes)
The final state represents the shortest path from each node to every
other node in the network.
Destinatio
n   A   B   C   D   E   F
0
A's Table   (Direct) 4 (B)   5 (C)   13 (B)   8 (C)   14 (C)
0
B's Table 4 (A)   (Direct) 9 (A)   9 (D)   7 (E)   11 (D)
********** 6 **********
--- page 7 ---
0
C's Table 5 (A)   9 (A)   (Direct) 12 (E)   3 (E)   9 (E)
0
D's Table 13 (B)   9 (B)   12 (E)   (Direct) 8 (F)   2 (F)
0
E's Table 8 (C)   7 (B)   3 (C)   8 (F)   (Direct) 6 (F)
0
F's Table   14 (E)   11 (D)   9 (E)   2 (D)   6 (E)   (Direct)
Count to Infinity Problem
The Count to Infinity problem occurs in Distance Vector protocols when
a link fails, and two nodes update each other with outdated information,
creating a routing loop where the cost keeps incrementing slowly toward
infinity.
Example based on the Graph:
Imagine the link between A and B (cost 4) goes down.
1. Node A loses its direct path to B. It sees its table and thinks: "I
can't reach B directly, but Node C told me earlier it can reach B
in 9 hops."
2. Node A updates its table: A to B = 14 (Path: A $\to$ C $\to$ E
$\to$ B).
3. However, Node C's path to B actually went through A! Now Node
C sees A's new cost (14) and thinks the path to B has become more
expensive.
4. Node C updates: C to B = 19 (Path: C $\to$ A $\to$ ...).
5. They continue to bounce this update back and forth, adding the
link cost each time, until the metric reaches the RIP maximum
(16), which is defined as "infinity."
b.   Describe TCP/IP model in detail and show the use of each layer while
CO-1;
sending and receiving the message. Also, compare it with the OSI   [10]
BL-2
model.
Ans. Comparison of model 2 marks
TCP/IP explanation 2 marks
Functionality of each layer of model 6 marks
The layers in the TCP/IP protocol suite do not exactly match those in
the OSI model. The original TCP/IP protocol suite was defined as
having four layers: host-to-network, internet, transport, and
application. However, when TCP/IP is compared to OSI, we can say
********** 7 **********
--- page 8 ---
that the TCP/IP protocol suite is made of five layers: physical, data
link, network, transport, and application.
a.   An ISP is granted a block of addresses starting with 190.100.0.0/16
(65,536 addresses). The ISP needs to distribute these addresses to three
groups of customers as follows:
The first group has 128 customers; each needs 256 addresses.
The second group has 128 customers; each needs 128 addresses.
Q4
The third group has 128 customers; each needs 64 addresses.
CO-3;   [10]
BL-3   i.   Find the number of allocated addresses in each of the ISP
blocks.
ii.   Find the range of addresses for each organization and the
number of unallocated addresses.
Ans.   Designing all 3 blocks 3 marks
Start and end address of each subblocks 6 marks
Remaining number of address 1 marks
Customer Addresses/Custome Total
Group   s   r   Addresses
128×256=32,76
Group 1   128   256 8
128×128=16,38
Group 2   128   128 4
Group 3   128   64 128×64=8,192
Total
Allocated   57,344
Group 1 (32,768 addresses)
This group requires 2^{15} addresses, which corresponds to a /17 mask.
• Range: 190.100.0.0 to 190.100.127.255
********** 8 **********
--- page 9 ---
• Subnetting Note: Each of the 128 customers gets a /24 (256
addresses).
o Customer 1: 190.100.0.0/24
o ...Customer 128: 190.100.127.0/24
Group 2 (16,384 addresses)
This group requires 2^{14} addresses, which corresponds to a /18 mask.
• Range: 190.100.128.0 to 190.100.191.255
• Subnetting Note: Each of the 128 customers gets a /25 (128
addresses).
o Customer 1: 190.100.128.0/25
o ...Customer 128: 190.100.191.128/25
Group 3 (8,192 addresses)
This group requires 2^{13} addresses, which corresponds to a /19 mask.
• Range: 190.100.192.0 to 190.100.223.255
• Subnetting Note: Each of the 128 customers gets a /26 (64
addresses).
o Customer 1: 190.100.192.0/26
o ...Customer 128: 190.100.223.192/26
b.   Discuss open-loop and closed-loop congestion control mechanisms.
CO-4;
Elaborate on at least 4 open-loop and 4 closed-loop congestion control   [10]
BL-2
algorithms in the transport layer.
Ans.   • Congestion control refers to techniques and mechanisms that can
either prevent congestion before it happens or remove
congestion after it has happened.
•   In general, we can divide congestion control mechanisms into
two broad categories:
• Open-loop congestion control (prevention) and
• Closed-loop congestion control (removal).
•   In open-loop congestion control, policies are applied to prevent
congestion before it happens.
•   In these mechanisms, congestion control is handled by either the
source or the destination.
Open-loop congestion control (prevention)
• We give a brief list of policies that can prevent congestion.
• Retransmission Policy:- Retransmission is sometimes
unavoidable. If the sender feels that a sent packet is lost or
corrupted, the packet needs to be retransmitted.
********** 9 **********
--- page 10 ---
•   Retransmission in general may increase congestion in the
network. However, a good retransmission policy can prevent
congestion.
• Window Policy:- The type of window at the sender may also
affect congestion.
• The Selective Repeat window is better than the Go-Back-N
window for congestion control.
• Acknowledgment Policy:- The acknowledgment policy imposed
by the receiver may also affect congestion.
•   If the receiver does not acknowledge every packet it receives, it
may slow down the sender and help prevent congestion.
• Sending fewer acknowledgments means imposing less load on
the network.
• Discarding Policy:- A good discarding policy by the routers
may prevent congestion and at the same time may not harm the
integrity of the transmission.
• Admission Policy:- An admission policy, which is a quality-of-
service mechanism, can also prevent congestion in virtual-circuit
networks.
• Switches in a flow first check the resource requirement of a flow
before admitting it to the network.
• A router can deny establishing a virtual-circuit connection if
there is congestion in the network or if there is a possibility of
future congestion.
Closed-loop congestion control (removal).
•   Closed-loop congestion control mechanisms try to alleviate
congestion after it happens.
•   Several mechanisms have been used by different protocols. We
describe a few of them here.
❑ Backpressure :- The technique of backpressure refers to a
congestion control mechanism in which a congested node stops
receiving data from the immediate upstream node or nodes.
• This may cause the upstream node or nodes to become
congested, and they, in turn, reject data from their upstream node
or nodes, and so on.
********** 10 **********
--- page 11 ---
• Backpressure is a node-to-node congestion control that starts
with a node and propagates, in the opposite direction of data
flow, to the source.
• The backpressure technique can be applied only to virtual circuit
networks, in which each node knows the upstream node from
which a flow of data is coming.
❑ Choke Packet:- A choke packet is a packet sent by a node to the
source to inform it of congestion.
Note the difference between the backpressure and choke-packet
methods.
•   In backpressure, the warning is from one node to its upstream
node, although the warning may eventually reach the source
station.
•   In the choke-packet method, the warning is from the router,
which has encountered congestion, directly to the source station.
• The intermediate nodes through which the packet has traveled
are not warned.
❑ Implicit Signaling:- In implicit signaling, there is no
communication between the congested node or nodes and the
source.
• The source guesses that there is congestion somewhere in the
network from other symptoms.
• For example, when a source sends several packets and there is
no acknowledgment for a while, one assumption is that the
network is congested.
• The delay in receiving an acknowledgment is interpreted as
congestion in the network; the source should slow down.
❑ Explicit Signaling:- The node that experiences congestion can
explicitly send a signal to the source or destination. The explicit-
signaling method, however, is different from the choke-packet
method.
•   In the choke-packet method, a separate packet is used for this
purpose; in the explicit-signaling method, the signal is included
in the packets that carry data.
********** 11 **********
--- page 12 ---
•   Explicit signaling can occur in either the forward or the
backward direction.
Q5   a.
What do you understand by CIDR in the network layer? Elaborate on
CO-3;   [10]
IPv6 addressing and its header format with a suitable diagram.
BL-1
Ans.   Classless Inter-Domain Routing addressing 2 marks
IPV6 addressing with header format 6 marks
Explanation of IPV6 header 2 marks
Classful addressing, which is almost obsolete, is replaced with classless
addressing.
In IPv4 addressing, a block of addresses can be defined as x.y.z.t /n
in which x.y.z.t defines one of the addresses and the /n defines the
mask.
The first address in the block can be found by setting the rightmost
32 − n bits to 0s.
The last address in the block can be found by setting the rightmost
32 − n bits to 1s.
b.   Describe Selective Repeat sliding window protocols. Show the sender
and receiver windows for a system having a window size =4 with the
following scenario.
CO-2;   i.   Frame 0 sent and acknowledged
[10]
BL-3   ii.   Frame 1,2,3 sent and received except frame 2
iii.   Show retransmission of frame 2
iv.   After acknowledgement of frames 2, frame 4 and frame 5 sent
and received with acknowledgement
********** 12 **********
--- page 13 ---
v.   Show the timeout for frame 6.
Ans.   Selective Repeat explanation 4 marks
◼ Go-Back-N always discards out-of-order frames
◼ Losing one frame may result in retransmission of
multiple frames
◼ Very inefficient in noisy link
◼ Selective Repeat ARQ allows frames to be received out of order
◼ Therefore, receive window > 1
Send and Receive Windows
◼ Sender and receiver share window space equally
◼ For m-bit sequence numbers
◼ Send window: up to 2m-1
◼ Receive window: up to 2m-1
Explain it with an example, Sender, receiver window diagram with
frame number 6 marks
Q6   a.
Illustrate HTTP and FTP protocols and their usage in real-world
CO-4;   [10]
applications.
BL-2
Ans. HTTP and FTP explanation 3 +3 = 6 marks
Real world applications 2 +2 = 4 marks
File Transfer Protocol (FTP)
Transferring files from one computer to another is one of the most
common tasks expected from a networking or internetworking
********** 13 **********
--- page 14 ---
environment. As a matter of fact, the greatest volume of data exchange
in the Internet today is due to file transfer.
FTP uses the services of TCP. It needs two TCP connections.
The well-known port 21 is used for the control connection and the well-
known port 20 for the data connection
Communication over Control Section
◼ FTP uses the same approach as SMTP to communicate across
the control connection.
◼   It uses the 7-bit ASCII character set Communication is achieved
through commands and responses.
◼ This simple method is adequate for the control connection
because we send one command (or response) at a time.
◼ Each command or response is only one short line, so we need not
worry about file format or file structure.
◼ Each line is terminated with a two-character (carriage return and
line feed) end-of-line token.
HTTP
◼ The Hypertext Transfer Protocol (HTTP) is a protocol used
mainly to access data on the World Wide Web.
◼ HTTP functions as a combination of FTP and SMTP.
◼ Unlike SMTP, the HTTP messages are not destined to be read by
humans; they are read and interpreted by the HTTP server and
HTTP client (browser).
◼ SMTP messages are stored and forwarded, but HTTP messages
are delivered immediately.
◼ The contents of the requested file or other information are
embedded in a response message.
◼ HTTP uses the services of TCP on well-known port 80
◼ Although HTTP uses the services of TCP, HTTP itself is a
stateless protocol.
◼ The client initializes the transaction by sending a request
message.
◼ The server replies by sending a response.
CO-1;   b.   Explain at least 4 network topologies with their advantages and
[10]
BL-2   disadvantages.
********** 14 **********
--- page 15 ---
Ans. Each topology with advantages and disadvantages [ 2*4=8 marks]
Diagrams and comparison 2 marks
BUS Topology
•   In a bus network, every device is connected to a single cable that
runs from one end of the network to the other at any instant at
most one machine is the master and is allowed to transmit.
•   All other machines are required to refrain from sending.
• Some mechanism is needed to resolve conflicts when two or
machines want to transmit simultaneously.
• For example : IEEE 802.3, Ethernet.
• Computers on an Ethernet can transmit whenever they want to;
•   If two or more packets collide, each computer just waits a
random
time and tries again later.
Star Topology
•   In this type of topology all the computers are connected to a
single hub through a cable. This hub is the central node and
all others nodes are connected to the central node.
Features of Star Topology
• Every node has its own dedicated connection to the hub.
• Hub acts as a repeater for data flow.
Advantages of Star Topology
•   Fast performance with few nodes and low network traffic.
• Hub can be upgraded easily.
• Easy to troubleshoot.
• Easy to setup and modify.
• Only that node is affected which has failed, rest of the nodes
can work smoothly.
Disadvantages of Star Topology
• Cost of installation is high.
• Expensive to use.
•   If the hub fails then the whole network is stopped because all
the nodes depend on the hub.
• Performance is based on the hub that is it depends on its
capacity
Mesh Topology
•   It is a point-to-point connection to other nodes or devices. All
the network nodes are connected to each other.
• Mesh has n(n-1)/2 physical channels to link n devices.
• There are two techniques to transmit data over the Mesh
topology, they are :
1. Routing
********** 15 **********
--- page 16 ---
2. Flooding
•   In routing, the nodes have a routing logic, as per the network
requirements. Like routing logic to direct the data to reach the
destination using the shortest distance.
•   In flooding, the same data is transmitted to all the network
nodes, hence no routing logic is required.
• The network is robust, and the its very unlikely to lose the data.
But it leads to unwanted load over the network.
Features of Mesh Topology
•   Fully connected.
•   Robust.
• Not flexible.
Advantages of Mesh Topology
• Each connection can carry its own data load.
•   It is robust.
•   Fault is diagnosed easily.
•   Provides security and privacy.
Disadvantages of Mesh Topology
•   Installation and configuration is difficult.
• Cabling cost is more.
• Bulk wiring is required.
Tree Topology
•   It has a root node and all other nodes are connected to it forming
a hierarchy. It is also called hierarchical topology. It should at
least have three levels to the hierarchy.
Features of Tree Topology
•   Ideal if workstations are located in groups.
• Used in Wide Area Network.
Advantages of Tree Topology
•   Extension of bus and star topologies.
• Expansion of nodes is possible and easy.
•   Easily managed and maintained.
•   Error detection is easily done.
Disadvantages of Tree Topology
• Heavily cabled.
********** 16 **********
--- page 17 ---
•   Costly.
•   If more nodes are added maintenance is difficult.
•   Central hub fails, network fails.
a.   Discuss block coding in computer networks.
Q7   Demonstrate CRC with the following example.
CO-2;   Evaluate transmitted frame using CRC with generator X3+X+1 and   [10]
BL-3   message bits 101101101. At the receiver side frame received is
10110110110110, justify if the message received correctly or not.
Ans. Block coding explanation 2 marks
Calculate the transmitted message 4 marks
Check received message 3 marks
Transmitter Side (Encoding)
Divisor (G) = 1011 (Degree m = 3)
Append m zeros (3 zeros) to the message bits (101101101).
Dividend = 101101101000
CRC = 101
Transmitted Frame: Message + CRC = 101101101101
Receiver Side (Verification)
The Remainder is NOT zero. (In this specific division, the remainder is
110).
Conclusion: The message was NOT received correctly.
CO-3;   b.   What is switching? Explain and compare packet switching and message
[10]
BL-2   switching with an appropriate example.
Ans.   Switching 1 mark
Packet switching with example 5 marks
Message switching with example 2 marks
Comparison 2 marks
◼ Switching techniques in computer networks to connect
devices and allow them to communicate with each other.
◼ Additionally, we can utilize switching techniques to transfer data
from one device to another.
◼ Switching allows multiple devices to share the same
communication channel simultaneously.
◼ As a result, it improves the efficiency of the network.
Furthermore, switching also enables the network to route data to
its intended destination.
********** 17 **********
--- page 18 ---
◼ Additionally, it provides a mechanism for error checking and
correction
Packet Switching
◼ Packet switching is a method used to transmit data over a
network.
◼ We divide data into small packets and transmit them over the
network independently.
◼ Each packet contains the data and destination address
information required to route the packet to its destination.
◼ In packet switching, each packet travels separately through the
network and can take different paths to reach its destination.
◼ This approach allows for more efficient use of network resources
because we can transmit multiple packets simultaneously over
the same network.
Message Switching
◼ Message switching is a method of data transmission that was
popular in the early days of networking, before the development
of packet switching. In message switching, we divide a message
into fixed-length blocks or frames.
◼ Furthermore, we transmit each frame independently through the
network. Additionally, each intermediate node stores the frames
until the entire message is received. Finally, the nodes forward
the entire message to its destination.
◼ Unlike packet switching, message switching is a store-and-
forward method of data transmission.
◼ It means that each intermediate node stores the entire message
until it can be forwarded to the next node.
◼ This can result in longer transmission times compared to packet
switching. We can only transmit each message when an
intermediate node receives all the parts of the message.
********** 18 **********
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 55eaaaf1296b

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_AIDS_7056/Computer Networks/ANS_Computer Networks(702AI0C007)_2025-2026.docx`
- Text: docx (1 page)

````text
CN TEE Synoptic AY – 25-26

CO, BL, SO
| Q No
| Question
| Marks
|
CO1 BL3
SO1
| Q1 a
| A university plans to set up a campus network. Apply the concepts of wired and wireless communication to explain how each could be used in this network with respect to speed, reliability and security.
| 5
|

| Soln
| SYNOPTIC
Wired Communication (Ethernet, Fiber Optic):
Implementation: Connecting classrooms, labs, and offices using Ethernet cables or fiber optics.
Speed: High data transfer rates; suitable for heavy traffic like video streaming and large file transfers.
Reliability: Very reliable; less affected by interference or obstacles.
Security: More secure; physical access required to tap into the network.
Wireless Communication (Wi-Fi):
Implementation: Providing connectivity to mobile devices, laptops, and guest users via access points across the campus.
Speed: Moderate; can be affected by distance, number of users, and interference.
Reliability: Less reliable than wired; signal may degrade with obstacles or high traffic.
Security: Requires encryption (WPA3/WPA2); more vulnerable to attacks than wired networks.
Marking Scheme (5 Marks):
Wired Communication-Correctly explains implementation, speed, reliability and security- 2 Marks
Wireless Communication- Correctly explains implementation, speed, reliability and security - 2 Marks
Explains practical usage of wired and wireless networks in campus context-1 Marks

|
|
CO1,BL 2,   SO 1
| Q1 b
| Compare and contrast the TCP/IP model with the OSI model on any five points
| 5
|

| Soln
| Number of Layers: OSI has seven layers, while the TCP/IP model typically consists of four or five layers.
Protocol Dependency: TCP/IP was developed from a protocol-driven approach based on real-world protocols, while OSI is a theoretical model that is protocol-independent.
Layers Combined: The TCP/IP model combines the OSI's Session, Presentation, and Application layers into a single "Application Layer" and merges the Data Link and Physical layers into a "Network Access Layer".
Reliability: The TCP/IP model's reliability features are primarily handled by the Transport layer (TCP protocol), while the OSI model's reliability mechanisms are spread across different layers.
Usage: The TCP/IP model is the practical, widely implemented model used for the internet. The OSI model is primarily used as a reference or teaching tool.

|
|
CO 2 BL-2 SO 1
| Q1 c
| In a Slotted ALOHA system, the average number of frames generated per frame time is G = 1. Calculate the throughput S. What is the maximum throughput in Slotted ALOHA
| 5
|

| Soln
| (2MARKS)
It can be proven that the average number of successful transmissions for slotted ALOHA is S = G *e^-G.
The maximum throughput Smax is 0.368, when G = 1. In other words, if one frame is generated during one frame transmission time, then 36.8 percent of these frames reach their destination successfully.
We expect G = 1 to produce maximum throughput because the vulnerable time is equal to the frame transmission time.
Therefore, if a station generates only one frame in this vulnerable time (and no other station generates a frame during this time), the frame will reach its destination successfully.

(2MARKS)
Formula:
S=G×e^−G
Substitution:
S=1×e^−1
=1×0.3679
=0.368S
(1MARKS)
Throughput ≈ 0.368 (36.8%)
So throughput = 36.8% efficiency.

|
|
CO-3; SO-2;
BL-3
| Q1 d
| A block of address is granted to a small organization and one of the address is 200.140.64.48/26. Determine the first address and last address in the block. Determine the total number of addresses in the block.
| 5
|

|  Soln
| IP address = 200.140.64.48/26
Step 1️⃣   Interpret /26
Subnet mask length = 26 bits
So network part = 26 bits, host part = 32−26=6 bits.
That means:
Number of addresses per block = 26=64
Step 2️⃣ — Find the network (first) address
In dotted decimal:
/26 mask →
255.255.255.192
(because the 26th bit boundary falls inside the 4th octet:
11111111.11111111.11111111.11000000)
Each block starts at multiples of 64 in the 4th octet:
0, 64, 128, 192.
Now, given IP is 200.140.64.48, and 48 lies between 0 and 63.
So this IP belongs to the subnet that starts at .0.
Network address = 200.140.64.0   - 2 mark

Step 3️⃣ — Find the broadcast (last) address
Add 63 (since 64 addresses per block, counting from 0):
0 + 63 = 63 → 200.140.64.63
Last address (broadcast address) = 200.140.64.63 – 2 mark

Step 4️⃣ — Compute total number of addresses
2(32−26)=26=64
Total addresses = 64   - 1 mark
|
|

|
|
|
|
CO- 2; SO- 1;
BL-3
| Q2 a
| i) Explain the block coding method for error detection and correction. (2 marks)
ii)Two binary codewords are used in a communication system:
C1 = 1001101
C2 = 1110001
Compute the Hamming distance between  C1 and  C2 . (2 marks)
iii) A new codeword  C3 = 1010101  is added to the set. Compute the pairwise Hamming distances between  C3  and the other codewords.  (2 marks)
iv) Based on the minimum Hamming distance of the code, determine how many errors the code can detect and how many it can correct. Justify your answer. (4 marks)
| 10
|

| Soln
| i) Explain the block coding method for error detection and correction. (2 marks)

In block coding, the message is divided into blocks, each of k bits, called data words .
r redundant bits are added to each block to make the length n=k+r
The resulting n bit blocks are called codewords. (1 mark)
The block coding process is one-to-one; the same dataword is always   encoded as the same codeword.
Message bits (k): The actual data to be sent
Codeword bits (n): The message bits plus redundant bits
Redundant bits (n - k): Extra bits added for error detection and correction   (1 mark)

ii)  Compute the Hamming distance between  C1 and  C2

Step : (1 mark)
Final answer: No of 1’s = 4 . Hence Hamming Distance = 4  (1 mark)

iii)  A new codeword  C3 = 1010101  is added to the set. Compute the pairwise Hamming distances between  C3  and the other codewords.
A. ( C3 = 1010101 ) vs ( C1 = 1001101 )
Steps to show (1 mark)
Hamming distance = 2    (1 mark)
B.( C3 = 1010101 ) vs ( C2 = 1110001 )
Steps to show (1 mark)
Hamming distance = 2    (1 mark)
iv) Determine error detection and correction capabilities
( d(C_1, C_2) = 4 )
( d(C_1, C_3) = 2 )
( d(C_2, C_3) = 2 )
so,  d{min} = 2       (1mark)

Error detection: (1 mark)
A code can detect up to ( d_{min} - 1 ) errors.
So: can detect ( 2 - 1 = 1 ) error
Error correction: 0 error  (1 mark)
Final concluding answer with justification (2 mark)
Minimum distance = 2
Can detect 1 error, correct 0 errors

|
|
CO-3; SO-1;
BL-3
| Q2 b
| A company wants to set up a network for smooth data transfer between its offices. Based on your understanding, which switching technique—circuit, packet, or message—would you recommend? Explain how each works and compare their pros, cons, and best use cases to support your choice.
| 10
|

| Soln
|
Switching Technique
| Working Principle
| Advantages
| Disadvantages
| Best Use Case
|
Circuit Switching
| Dedicated path is established before communication begins.
| Reliable, continuous connection.
| Inefficient for data; idle time wastes resources.
| Voice communication (e.g., telephone networks).
|
Packet Switching
| Data is split into packets sent independently and reassembled at destination.
| Efficient bandwidth usage; supports multiple users.
| Possible delays, packet loss.
| Internet, real-time data transmission.
|
Message Switching
| Entire message is stored and forwarded through intermediate nodes.
| No need for dedicated path; flexible routing.
| High delay due to storage at each node.
| Email, non-real-time communication.
|

Recommendation -Packet switching is recommended for the company’s network due to its efficiency, scalability, and ability to handle diverse data types across multiple branches.

Explanation of all three techniques (working principles)- 3 marks
Comparison of advantages and disadvantages -   3 marks
Identification of suitable applications-   2 marks
Justified recommendation based on scenario-   2 marks
|
|

|
|
|
|
BL 1, CO 1, SO 1
| Q3 a
| Define the following:-   a) LAN b) MAN c)PAN d) WAN e) ARPANET
| 5
|

| Soln
|
1 mark for each definition
a) LAN (Local Area Network):
A Local Area Network is a network that connects computers and devices within a limited geographical area such as a home, school, office building, or campus.
Example: A network connecting computers in a computer lab.
Data transfer speed: High (typically 100 Mbps to 10 Gbps).
b) MAN (Metropolitan Area Network):
A Metropolitan Area Network covers a larger area than a LAN, usually spanning a city or a large campus. It connects multiple LANs together within a metropolitan area.
Example: A network connecting different branches of a university within a city.
c) PAN (Personal Area Network):
A Personal Area Network is the smallest type of network, used for connecting personal devices within a short range (usually within 10 meters).
Example: Connecting a smartphone to a laptop via Bluetooth.
d) WAN (Wide Area Network):
A Wide Area Network covers a very large geographical area, often a country or even globally. It connects multiple LANs and MANs using public networks like the Internet or satellite links.
Example: The Internet is the largest WAN.
e) ARPANET (Advanced Research Projects Agency Network):
ARPANET was the first operational packet-switching network and the precursor to the modern Internet. It was developed in the late 1960s by the U.S. Department of Defense’s ARPA (now DARPA) to connect research institutions and allow resource sharing.
|
|
CO3, BL2 SO 1
| Q3 b
| Explain the different types of OSPF packets used for communication between routers.
| 5
|

| Soln
| OSPF uses five types of packets for communication between routers:
Hello Packet – Used to discover and maintain neighbor relationships.
Database Description (DBD) Packet – Used to summarize the contents of a router’s link-state database.
Link-State Request (LSR) Packet – Sent to request specific link-state information from a neighbor.
Link-State Update (LSU) Packet – Carries detailed link-state information (LSAs) to other routers.
Link-State Acknowledgment (LSAck) Packet – Confirms the receipt of LSUs to ensure reliable delivery.
Summary:
OSPF uses 5 packet types — Hello, DBD, LSR, LSU, and LSAck — to form neighbors, exchange topology data, and keep the network synchronized.

|
|
CO5 BL 2 SO 1
| Q3 c
| Explain, with the help of a neat diagram, how the World Wide Web (WWW) enables users to access online information through the HTTP protocol. Describe the components and working mechanism of the Web, and interpret how HTTP facilitates communication between a client and a server when a user enters a URL such as http://www.example.com
| 10
|

| Soln.
| The World Wide Web (WWW) is a global information system that enables users to access interlinked documents and multimedia content over the Internet. It operates on a client–server model, where the HTTP protocol governs communication between browsers (clients) and web servers.
Diagram and explanation: WWW and HTTP Communication Flow (4 marks)

Request–Response Model:
HTTP follows a simple two-way exchange — the client sends a request, and the server responds.
Stateless Protocol:
Each request is independent, improving scalability and simplicity.
Structured Message Format:
Request Line: Method, resource, version
Headers: Metadata (host, content type, etc.)
Body: Optional data (for POST requests)
Reliable Transport:
Uses TCP to ensure ordered, error-free data delivery.
Status Codes:
Help the browser understand response outcomes (e.g., 200 OK, 404 Not Found).

Components of the World Wide Web (3 marks)
Component
| Description
|
Web Browser (Client)
| Application (e.g., Chrome, Firefox) used to send requests and display web pages.
|
Web Server
| Computer that stores and serves web pages when requested by clients.
|
Uniform Resource Locator (URL)
| Unique address that identifies a specific web resource. Example: http://www.example.com/index.html.
|
HTTP (Hypertext Transfer Protocol)
| Communication protocol used for transferring web documents between browser and server.
|
HTML (Hypertext Markup Language)
| Standard language used to structure and format web pages.
|
Working Mechanism of the WWW (3 marks)
When a user types http://www.example.com in the browser:
URL Parsing:
The browser divides the URL into:
Protocol → http
Host name → www.example.com
File/resource → default index.html
DNS Resolution:
The browser queries the DNS to obtain the IP address of the web server hosting www.example.com.
Connection Establishment:
A TCP connection is initiated between the client and the server on port 80 (default for HTTP).
HTTP Request:
The browser sends an HTTP request message (e.g., GET /index.html HTTP/1.1) asking for the web page.
HTTP Response:
The server locates the requested file, encapsulates it in an HTTP response message with a status code and sends it back to the browser.
Rendering the Page:
The browser interprets the HTML, CSS, and scripts received and displays the webpage to the user.
Connection Termination:
Once the transfer is complete, the TCP connection is closed.
|
|

|
|
|
|
CO-3   SO-1
BL-2

| Q4 a
| Summarize the IPv6 address 0:15::1:12:1213 to its full, original form.   Write a comparison between IPv4 and IPv6 packet headers.
| 10
|

| Soln
| First, we need to align the left side of the double colon (::) with the left side of the original IPv6 address pattern, and the right side of the double colon with the right side of the original pattern. This helps us determine how many groups of zeros we need to replace the double colon with.

For the given the address:
0:15::1:12:1213
We align the known parts as:
0:15: (left side), then the double colon ::, then 1:12:1213 (right side).
By counting how many groups of zeros are missing between the left and right parts to complete the full 8-group IPv6 address, we find that the double colon represents four groups of zeros.
Therefore, the original expanded address is:
0000:0015:0000:0000:0000:0001:0012:1213

Comparison between IPv4 and IPv6 packet headers:
The header length field is removed in IPv6 because the header length is fixed in this version.
The service type field is also removed in IPv6. Instead, the priority and flow label fields together perform the function that the service type field used to handle.
The total length field from IPv4 is replaced by the payload length field in IPv6.
The identification, flag, and offset fields are no longer part of the base header in IPv6. Instead, they are included in a separate fragmentation extension header.
The TTL (Time To Live) field in IPv4 is renamed to hop limit in IPv6.
The protocol field in IPv4 is replaced by the next header field in IPv6.
The header checksum is eliminated in IPv6 because checksums are handled by upper-layer protocols, so it is not needed at the IPv6 header level.
The option fields that exist in IPv4 are implemented as extension headers in IPv6.

(The IPv6 address 0:15::1:12:1213 to its full, original form-05M and
Any five point of comparison between IPv4 and IPv6 packet headers-05M)

|
|
BL- 2   CO-4
SO-1
| Q4 b
| Describe the User Datagram Protocol (UDP) in detail with suitable diagram. Also explain how it differs from TCP?
| 10
|

| Soln
| (6 marks)
The User Datagram Protocol (UDP) is called a connectionless, unreliable transport protocol. It does not add anything to the services of IP except to provide process-to-process communication instead of host-to-host communication.
The User Datagram Protocol (UDP) is called a connectionless, unreliable transport protocol.
It does not add anything to the services of IP except to provide process-to-process communication instead of host-to-host communication.
It performs very limited error checking.
If UDP is so powerless, why would a process want to use it?
UDP is a very simple protocol using a minimum of overhead.
If a process wants to send a small message and does not care much about reliability, it can use UDP.
Sending a small message by using UDP takes much less interaction between the sender and receiver than using TCP (Transmission control protocol) or SCTP (Stream control transmission protocol).
UDP Operations:
Connectionless Services:   Each user datagram sent by UDP is an independent datagram.   There is no relationship between the different user datagrams even if they are coming from the same source process and going to the same destination program.   The user datagrams are not numbered. Also, there is no connection establishment and no connection termination, as is the case for TCP. This means that each user datagram can travel on a different path. Each request must be small enough to fit into one user datagram. Only those processes sending short messages should use UDP.
Flow and Error Control:
UDP is a very simple, unreliable transport protocol. There is no flow control and hence no window mechanism. The receiver may overflow with incoming messages.
There is no error control mechanism in UDP except for the checksum. This means that the sender does not know if a message has been lost or duplicated. When the receiver detects an error through the checksum, the user datagram is silently discarded.

Encapsulation and Decapsulation:
To send a message from one process to another, the UDP protocol encapsulates and decapsulates messages in an IP datagram.

Encapsulation
When a process has a message to send through UDP, it passes the message to UDP along with a pair of socket addresses and the length of data.
UDP receives the data and adds the UDP header.
UDP then passes the user datagram to IP with the socket addresses.
IP adds its own header, using the value 17 in the protocol field, indicating that the data has come from the UDP protocol.

Decapsulation
When the message arrives at the destination host, the physical layer decodes the signals into
bits and passes it to the data link layer.
The data link layer uses the header (and the trailer) to check the data. If there is no error, the header and trailer are dropped and the datagram is passed to IP.
The IP software does its checking. If there is no error, the header is dropped and the user datagram is passed to UDP with the sender and receiver IP addresses.
Queuing:

(4 marks)
Basis
| Transmission Control Protocol (TCP)
| User Datagram Protocol (UDP)
|
Type of Service
| TCP is a connection-oriented protocol. Connection orientation means that the communicating devices should establish a connection before transmitting data and should close the connection after transmitting the data.
| UDP is the Datagram-oriented protocol. This is because there is no overhead for opening a connection, maintaining a connection, or terminating a connection. UDP is efficient for broadcast and multicast types of network transmission.
|
Reliability
| TCP is reliable as it guarantees the delivery of data to the destination router.
| The delivery of data to the destination cannot be guaranteed in UDP.
|
Error checking mechanism
| TCP provides extensive error-checking mechanisms. It is because it provides flow control and acknowledgment of data.
| UDP has only the basic error-checking mechanism using checksums.
|
Acknowledgment
| An acknowledgment segment is present.
| No acknowledgment segment.
|
Sequence
| Sequencing of data is a feature of Transmission Control Protocol (TCP). this means that packets arrive in order at the receiver.
| There is no sequencing of data in UDP. If the order is required, it has to be managed by the application layer.
|
Speed
| TCP is comparatively slower than UDP.
| UDP is faster, simpler, and more efficient than TCP.
|
Retransmission
| Retransmission of lost packets is possible in TCP, but not in UDP.
| There is no retransmission of lost packets in the User Datagram Protocol (UDP).
|
Header Length
| TCP has a (20-60) bytes variable length header.
| UDP has an 8 bytes fixed-length header.
|
Weight
| TCP is heavy-weight.
| UDP is lightweight.
|
Handshaking Techniques
| Uses handshakes such as SYN, ACK, SYN-ACK
| It's a connectionless protocol i.e. No handshake
|
Broadcasting
| TCP doesn't support Broadcasting.
| UDP supports Broadcasting.
|

|
|

|
|
|
|
CO-2, BL-3 SO-1
| Q5 a
| Apply the principles of the Selective Repeat ARQ Sliding Window Protocol to determine the maximum permissible sender and receiver window sizes for frame sequence number field of 3 bits, and explain with the help of diagram how frames are transmitted, acknowledged, and buffered at both the sender and receiver ends.
Justify why this window size is chosen, and analyze how incorrect window sizing can lead to frame mis ordering or acknowledgment ambiguity.
| 10
|

| Soln
| Explanation of Selective Repeat ARQ   (1 marks),
window size   (1marks),
explanation of frame transmission   (3 marks),
justification of window size 5 marks   ( 3 explanation and 2 marks diagram)
Solution: In Selective Repeat ARQ only the lost or error frames are retransmitted, whereas correct frames are received and buffered. The receiver while keeping track of sequence numbers buffers the frames in memory and sends NACK for only frames which are missing or damaged. The sender will send/retransmit a packet for which NACK is received.
Step 1 − Frame 0 sends from sender to receiver and set timer.
Step 2 − Without waiting for acknowledgement from the receiver another frame, Frame1 is sent by sender by setting the timer for it.
Step 3 − In the same way frame2 is also sent to the receiver by setting the timer without waiting for previous acknowledgement.
Step 4 − Whenever sender receives the ACK0 from receiver, within the frame 0 timer then it is closed and sent to the next frame, frame 3.
Step 5 − whenever the sender receives the ACK1 from the receiver, within the frame 1 timer then it is closed and sent to the next frame, frame 4.
Step 6 − If the sender doesn’t receive the ACK2 from the receiver within the time slot, it declares timeout for frame 2 and resends the frame 2 again, because it thought the frame2 may be lost or damaged.

|
|
BL: 2, SO: 2 CO: 5
| Q5 b
| Explain SMTP and its role in email communication. Describe the different phases of SMTP communication, detailing the purpose of each phase and the typical commands used. Illustrate your answer with a labelled diagram showing the flow between the client and server
| 10
|

| Soln
| SMTP Explanation: 2 marks
Diagram: 2 marks
Phases: 6 marks
•One of the most popular Internet services is electronic mail (e-mail).
•E-mail allow users to exchange messages. It is considered as a one-way transaction.

User Agent:
•A user agent is a software package that composes , reads , replies to ,   and forwards messages.
•Types of user agents:
Command driven
GUI   based
•Mailing list: E-mail allows one name, an alias to represent several different e-mail addresses

The protocol that defines the MTA client and server in the internet is called as Simple Mail Transfer Protocol(SMTP)
•SMTP uses commands and responses to transfer messages between an MTA client and MTA server.
•Commands: Keyword: argument(s)
•Responses: Responses are sent from the server to the client. A response is a three digit code that may be followed by additional textual information
MAIL TRANSFER PHASES
Connection Establishment
1.The server sends code 220(service ready) to tell the client that it is ready to receive mail. If the server is not ready it sends code 421(service not available)
2.The client sends the HELLO message to identify itself, using its domain name address.
3.The server responds with code 250(request command completed)
Message transfers
1.The client sends the MAIL FROM message to introduce the sender of the message.
2.The server responds with code 250 or some other appropriate code.
3.The client sends the RCPT TO message, which includes the mail address of the recipient.
4.The server responds with code 250 or some other appropriate code.
5.The client sends the DATA message to initialize the message transfer.
6.The server responds with code 354(start mail input)
7.The client sends the contents of the message in consecutive lines.
8.The server responds with code 250 or some other appropriate code
Connection Termination
1.The client sends the QUIT command
2.The server responds with code 221(service closing transmission channel)

|
|

|
|
|
|
CO1 SO1 BL-1
| Q6 a
| List different types of   unguided transmission media and write any two characteristics of each.
| 5
|

| Soln
|

Radio waves

Radio waves are Omnidirectional, useful for multicasting. AM and FM radio, television, maritime radio, cordless phones, and paging are examples of multicasting.
Radio waves a good candidate for long-distance broadcasting.
Advantage: receives signal inside a building
Disadvantage: Cannot isolate a communication

Microwaves

Microwave propagation is line-of-sight.
Very high-frequency microwaves cannot penetrate walls
The microwave band is relatively wide, almost 299 GHz. Therefore wider
subbands can be assigned, and a high data rate is possible
Use of certain portions of the band requires permission from authorities.

Microwaves are used in cellular phones , satellite networks and
wireless LANs

Infrared Waves

Infrared signals can be used for short-range communication in a closed area using line-of-sight propagation.

Infrared waves, having high frequencies, cannot penetrate walls.

The wide bandwidth can be used to transmit digital data with a very high data rate.

Infrared waves, having high frequencies, cannot penetrate walls.

The wide bandwidth can be used to transmit digital data with a very high data rate.

The recent standard defines a data rate of 4 Mbps.
|
|
CO2,BL-4 SO-1
| Q6 b
| Compare 1-persistent, non-persistent, and p-persistent CSMA strategies with diagrammatic representations
| 5
|

| Soln
| Points of 1-persistent, non-persistent, and p-persistent 1M each )- 3M , diagram 2M
1-Persistent CSMA
Working:
The node listens to the channel.
If idle → transmit immediately.
If busy → keep listening continuously and transmit immediately when it becomes free.
Pros: Simple, high channel utilization.
Cons: High chance of collisions if multiple nodes are waiting (because they all send immediately once the channel is free).
Non-Persistent CSMA
Working:
The node listens to the channel.
If idle → transmit immediately.
If busy → does not continuously sense. Instead, it waits a random backoff time and then checks again.
Pros: Lower chance of collisions.
Cons: Higher delay, because nodes may wait even if the channel becomes free.
p-Persistent CSMA (used in slotted channels, e.g., LANs)
Working:
The channel is divided into discrete time slots.
When the channel is sensed idle:
Transmit with probability p.
Wait until the next time slot with probability 1 − p, then repeat.
Pros: Balance between efficiency and collision probability; reduces chance of many nodes transmitting at once.
Cons: Performance depends on proper tuning of p.

|
|
CO-4 BL-2 SO-1

| Q6 c
| Explain open loop and closed loop congestion control policy in transmission control protocol. Describe any two policies from each type.
| 10
|

| Soln
| Open Loop: Open loop congestion control mechanisms try to remove the congestion before it happens.
Works independently of feedback from the network.   ----   1M

Closed Loop: Closed loop congestion control mechanisms try to remove the congestion after it happens.
Uses feedback from the network (ACKs, packet loss, delays) to adjust transmission.
---   1M
Open Loop Policies (any 2)   -----   2 *2 =   4M
Retransmission Policy
• The sender retransmits a packet, if it feels that the packet it has sent is lost or corrupted.
• However retransmission in general may increase the congestion in the network. But we need to implement good retransmission policy to prevent congestion.
• The retransmission policy and the retransmission timers need to be designed to optimize efficiency and at the same time prevent the congestion.

Window Policy
• To implement window policy, selective reject window method is used for congestion control.
• Selective Reject method is preferred over Go-back-n window as in Go-back-n method, when timer for a packet times out, several packets are resent, although some may have arrived safely at the receiver. Thus, this duplication may make congestion worse.
• Selective reject method sends only the specific lost or damaged packets.

Acknowledgement Policy
• The acknowledgement policy imposed by the receiver may also affect congestion.
• If the receiver does not acknowledge every packet it receives, it may slow down the sender and help prevent congestion.
• Acknowledgments also add to the traffic load on the network. Thus, by sending fewer acknowledgements we can reduce load on the network.
• To implement it, several approaches can be used:
1. A receiver may send an acknowledgement only if it has a packet to be sent.
2. A receiver may also decide to acknowledge only N packets at a time.

Admission Policy
• An admission policy, which is a quality-of-service mechanism, can also prevent congestion in virtual circuit networks.
• Switches in a flow first check the resource requirement of a flow before admitting it to the network.
• A router can deny establishing a virtual circuit connection if there is congestion in the "network or if there is a possibility of future congestion.

Closed Loop Policies (any 2)   ------- 2*2 =   4M
Backpressure
• Backpressure is a node-to-node congestion control that starts with a node and propagates, in the opposite direction of data flow.
• The backpressure technique can be applied only to virtual circuit networks. In such virtual circuit each node knows the upstream node from which a data flow is coming.
• In this method of congestion control, the congested node stops receiving data from the immediate upstream node or nodes.
• This may cause the upstream node on nodes to become congested, and they, in turn, reject data from their upstream node or nodes.
• As shown in fig node 3 is congested and it stops receiving packets and informs its upstream node 2 to slow down. Node 2 in turns may be congested and informs node 1 to slow down. Now node 1 may create congestion and informs the source node to slow down. In this way the congestion is alleviated. Thus, the pressure on node 3 is moved backward to the source to remove the congestion.

Choke Packet
• In this method of congestion control, congested router or node sends a special type of packet called choke packet to the source to inform it about the congestion.
• Here, congested node does not inform its upstream node about the congestion as in backpressure method.
• In choke packet method, congested node sends a warning directly to the source station i.e. the intermediate nodes through which the packet has travelled are not warned.

|
|

|
|
|
|
CO3, BL3, 4 , SO2
| Q7 a
| Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed edges between these nodes and their corresponding positive weights are given in the table below
Edge
| Distance
|
A->B
| 4
|
A->C
| 2
|
B->C
| 5
|
B->D
| 10
|
C->D
| 3
|
C->E
| 4
|
D->E
| 1
|
D->F
| 2
|
E->F
| 3
|
F->G
| 5
|

Using Dijkstra’s Algorithm:

i. Determine the shortest path from the source node A to the destination node G.
ii. Compute the shortest distance from node A to node G.
iii. Show all intermediate steps, including the initialization, selection of the minimum distance node, for each iteration.
Illustrate the original network topology and the final shortest path with the corresponding distance values clearly marked on the edge

| 10
|

| Soln
|

The shortest path A->C ->D->F->G, shortest distance is 12
Shortest Path calculation - 3 marks
Computing Shortest Distance - 2 marks
Intermediate Steps - 3marks
Original network topology ( 1marks) + final shortest path with the corresponding distance values clearly marked on the edges ( 1 marks)

1) Edge costs
Edge
| Weight
|
A → B
| 4
|
A → C
| 2
|
B → C
| 5
|
B → D
| 10
|
C → D
| 3
|
C → E
| 4
|
D → E
| 1
|
D → F
| 2
|
E → F
| 3
|
F → G
| 5
|

2) Iteration table

|
|
CO-4; SO-1;
BL-2
| Q7 b
| Draw a neat diagram and explain the working of the Token Bucket Algorithm. State any two limitations of the Token Bucket algorithm
| 10
|

| Soln
|
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for limitations.

Explanation of working based on the following points is expected.
A bucket holds tokens, each token allowing the transmission of a certain number of bytes (usually 1 token = 1 byte or 1 packet).
Tokens are added to the bucket at a constant rate r (tokens per second).
The bucket has a maximum capacity B (in tokens).
When a packet arrives:
If there are enough tokens, the packet is transmitted, and tokens are removed from the bucket.
If not enough tokens, the packet is either delayed (until enough tokens are available) or dropped (if there's no buffering).
This allows bursts of traffic up to B bytes to be sent at once (if the bucket is full), but enforces an average rate of r bytes/sec over time.

Two Limitations of the Token Bucket Algorithm
Complexity with Bursty Traffic:
While the algorithm allows short bursts, if traffic bursts are too frequent or too large, it may still overwhelm downstream systems, leading to queue overflows.
No Built-in Fairness or Priority:
The algorithm does not distinguish between different types of traffic. So, critical or high-priority packets can be delayed just like any others, making it unsuitable for quality of service (QoS) differentiation without additional mechanisms.

|
|
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 709415b53d00

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSBS_7036/Computer Networks/ANS_Computer Networks(702AI0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSBS)
Year: II / III/Semester IV/Semester VI(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures on the right-hand side indicate full marks.
Q1
Answer briefly:   [20]
CO-1;   a.   Discuss all types of guided transmission media in communication.   [5]
BL-2
Ans.   Explanation of guided transmission media – [3 marks]
Diagrams – 2 marks
Guided media, which are those that provide a conduit from one device to
another, include twisted-pair cable, coaxial cable, and fiber-optic cable.
Twisted-Pair Cable
Coaxial Cable
Coaxial cable has an inner conductor that is surrounded by an insulating
layer, which has conductive shielding around it.
********** 1 **********
--- page 2 ---
Fiber-Optic Cable
A fiber-optic cable is composed of very thin strands of glass or plastic
known as optical fibers.
b.   Draw and explain the procedure for the pure ALOHA protocol. Describe
how vulnerable time is calculated in pure ALOHA with the following.
CO-2;   [5]
BL-3   A pure ALOHA network transmits 300bit frames on a shared channel of
200 kbps. Calculate the vulnerable time.
Ans.   Pure ALOHA explanation – 3 marks
◼ The original ALOHA protocol is called pure ALOHA.
◼ The idea is that each station sends a frame whenever it has a frame
to send.
◼ However, since there is only one channel to share, there is the
possibility of collision between frames from different stations
Vulnerable time calculation – 2 marks
Vulnerable Time=2×Tf
Vulnerable Time=2×1.5 ms=3 ms
Vulnerable Time=3 ms
c.   Illustrate the work of ARP and RARP with examples and differentiate
CO-3;   [5]
BL-2   them.
Ans. ARP explanation with example 2 marks
********** 2 **********
--- page 3 ---
RARP explanation with example 2 marks
Difference 1 mark
ARP associates an Internet Protocol (IP) address with its physical
address. On a typical physical network, such as a LAN, each device on a
link is identified by a physical or station address that is usually imprinted
on the network interface card (NIC).
An ARP request is broadcast; an ARP reply is unicast.
RARP finds the logical address for a machine that only knows its
physical address.
The RARP request packets are broadcast; the RARP reply packets are
unicast.
d.   Describe the token bucket algorithm in traffic shaping with a suitable
CO-4;   diagram and example to justify the improvement in the quality of [5]
BL-2
services.
Ans.   Quality of Services improvement 1 mark
Token Bucket algorithm with diagram 4 marks
Token Bucket
• The leaky bucket is very restrictive. It does not credit an idle host.
• For example, if a host is not sending for a while, its bucket
becomes empty.
• Now if the host has bursty data, the leaky bucket allows only an
average rate. The time when the host was idle is not taken into
account.
• On the other hand, the token bucket algorithm allows idle hosts to
accumulate credit for the future in the form of tokens.
•   Let’s assume that the bucket capacity is 10,000 tokens and tokens
are added at the rate of 1000 tokens per second.
•   If the system is idle for 10 seconds (or more), the bucket collects
10,000 tokens and becomes full.
•   In other words, the host can send bursty data as long as the bucket
is not empty.
• The token bucket allows bursty traffic at a regulated maximum
rate.
********** 3 **********
--- page 4 ---
Q2   a.   Explain the CSMA protocol in the data link layer. Describe all types of
[10]
CO-2;   persistence methods of CSMA with their advantages and disadvantages.
BL-2
Ans. CSMA explanation 1 marks
1-persistent CSMA with advantages and disadvantages 3 marks
p-persistent CSMA with advantages and disadvantages 3 marks
non-persistent CSMA with advantages and disadvantages 3 marks
********** 4 **********
--- page 5 ---
b.   Elaborate on the concept of 3-way handshaking in the TCP protocol and
CO-4;
how it improves the reliability as compared to UDP. Define the SCTP   [10]
BL-2
protocol with its applications.
Ans. 3-way handshaking explanation – 3 marks
Improvement of reliability – 3 marks
SCTP with application – 4 marks
TCP 3 way Handshake Process
The TCP (Transmission Control Protocol) connection establishment
follows a three-way handshake process to ensure that both the client and
the server are ready to exchange data.
A SYN segment cannot carry data, but it consumes one sequence
number.
A SYN + ACK segment cannot carry data, but does consume one
sequence number.
An ACK segment, if carrying no data, consumes no sequence number.
After this three-way handshake, the client and server can start
transmitting data in both directions.
The FIN segment consumes one sequence number if it does
not carry data.
********** 5 **********
--- page 6 ---
The FIN + ACK segment consumes one sequence number if it
does not carry data.
SCTP
Stream Control Transmission   Protocol (SCTP) is a new reliable,
message-oriented transport layer protocol. SCTP is a message-oriented,
reliable protocol that combines the best features of UDP and TCP. An
association in SCTP can involve multiple streams. SCTP association
allows multiple IP addresses for each end. In SCTP, a data chunk is
numbered using a Transmission Sequence Number (TSN). To
distinguish between different streams, SCTP uses an Stream Identifier
(SI). To distinguish between different data chunks belonging to the
same stream, SCTP uses Stream Sequence Numbers (SSN). TCP has
segments; SCTP has packets.
a.   Evaluate the final routing table of each node using RIP routing protocol.
Show all steps to determine the final routing table of at least one node.
Discuss the count to infinity problem in RIP with an example.
Q3
[10]
CO-3;
BL-3
Ans.   Routing table of each node 4 marks
Detail steps for one node is 3 marks
Count to infinity problem 3 marks
Final Routing Tables (All Nodes)
The final state represents the shortest path from each node to every
other node in the network.
Final Routing Tables (All Nodes)
The final state represents the shortest path from each node to every
other node in the network.
Destinatio
n   A   B   C   D   E   F
0
A's Table   (Direct) 4 (B)   5 (C)   13 (B)   8 (C)   14 (C)
0
B's Table 4 (A)   (Direct) 9 (A)   9 (D)   7 (E)   11 (D)
********** 6 **********
--- page 7 ---
0
C's Table 5 (A)   9 (A)   (Direct) 12 (E)   3 (E)   9 (E)
0
D's Table 13 (B)   9 (B)   12 (E)   (Direct) 8 (F)   2 (F)
0
E's Table 8 (C)   7 (B)   3 (C)   8 (F)   (Direct) 6 (F)
0
F's Table   14 (E)   11 (D)   9 (E)   2 (D)   6 (E)   (Direct)
Count to Infinity Problem
The Count to Infinity problem occurs in Distance Vector protocols when
a link fails, and two nodes update each other with outdated information,
creating a routing loop where the cost keeps incrementing slowly toward
infinity.
Example based on the Graph:
Imagine the link between A and B (cost 4) goes down.
1. Node A loses its direct path to B. It sees its table and thinks: "I
can't reach B directly, but Node C told me earlier it can reach B
in 9 hops."
2. Node A updates its table: A to B = 14 (Path: A $\to$ C $\to$ E
$\to$ B).
3. However, Node C's path to B actually went through A! Now Node
C sees A's new cost (14) and thinks the path to B has become more
expensive.
4. Node C updates: C to B = 19 (Path: C $\to$ A $\to$ ...).
5. They continue to bounce this update back and forth, adding the
link cost each time, until the metric reaches the RIP maximum
(16), which is defined as "infinity."
b.   Describe TCP/IP model in detail and show the use of each layer while
CO-1;
sending and receiving the message. Also, compare it with the OSI   [10]
BL-2
model.
Ans. Comparison of model 2 marks
TCP/IP explanation 2 marks
Functionality of each layer of model 6 marks
The layers in the TCP/IP protocol suite do not exactly match those in
the OSI model. The original TCP/IP protocol suite was defined as
having four layers: host-to-network, internet, transport, and
application. However, when TCP/IP is compared to OSI, we can say
********** 7 **********
--- page 8 ---
that the TCP/IP protocol suite is made of five layers: physical, data
link, network, transport, and application.
a.   An ISP is granted a block of addresses starting with 190.100.0.0/16
(65,536 addresses). The ISP needs to distribute these addresses to three
groups of customers as follows:
The first group has 128 customers; each needs 256 addresses.
The second group has 128 customers; each needs 128 addresses.
Q4
The third group has 128 customers; each needs 64 addresses.
CO-3;   [10]
BL-3   i.   Find the number of allocated addresses in each of the ISP
blocks.
ii.   Find the range of addresses for each organization and the
number of unallocated addresses.
Ans.   Designing all 3 blocks 3 marks
Start and end address of each subblocks 6 marks
Remaining number of address 1 marks
Customer Addresses/Custome Total
Group   s   r   Addresses
128×256=32,76
Group 1   128   256 8
128×128=16,38
Group 2   128   128 4
Group 3   128   64 128×64=8,192
Total
Allocated   57,344
Group 1 (32,768 addresses)
This group requires 2^{15} addresses, which corresponds to a /17 mask.
• Range: 190.100.0.0 to 190.100.127.255
********** 8 **********
--- page 9 ---
• Subnetting Note: Each of the 128 customers gets a /24 (256
addresses).
o Customer 1: 190.100.0.0/24
o ...Customer 128: 190.100.127.0/24
Group 2 (16,384 addresses)
This group requires 2^{14} addresses, which corresponds to a /18 mask.
• Range: 190.100.128.0 to 190.100.191.255
• Subnetting Note: Each of the 128 customers gets a /25 (128
addresses).
o Customer 1: 190.100.128.0/25
o ...Customer 128: 190.100.191.128/25
Group 3 (8,192 addresses)
This group requires 2^{13} addresses, which corresponds to a /19 mask.
• Range: 190.100.192.0 to 190.100.223.255
• Subnetting Note: Each of the 128 customers gets a /26 (64
addresses).
o Customer 1: 190.100.192.0/26
o ...Customer 128: 190.100.223.192/26
b.   Discuss open-loop and closed-loop congestion control mechanisms.
CO-4;
Elaborate on at least 4 open-loop and 4 closed-loop congestion control   [10]
BL-2
algorithms in the transport layer.
Ans.   • Congestion control refers to techniques and mechanisms that can
either prevent congestion before it happens or remove
congestion after it has happened.
•   In general, we can divide congestion control mechanisms into
two broad categories:
• Open-loop congestion control (prevention) and
• Closed-loop congestion control (removal).
•   In open-loop congestion control, policies are applied to prevent
congestion before it happens.
•   In these mechanisms, congestion control is handled by either the
source or the destination.
Open-loop congestion control (prevention)
• We give a brief list of policies that can prevent congestion.
• Retransmission Policy:- Retransmission is sometimes
unavoidable. If the sender feels that a sent packet is lost or
corrupted, the packet needs to be retransmitted.
********** 9 **********
--- page 10 ---
•   Retransmission in general may increase congestion in the
network. However, a good retransmission policy can prevent
congestion.
• Window Policy:- The type of window at the sender may also
affect congestion.
• The Selective Repeat window is better than the Go-Back-N
window for congestion control.
• Acknowledgment Policy:- The acknowledgment policy imposed
by the receiver may also affect congestion.
•   If the receiver does not acknowledge every packet it receives, it
may slow down the sender and help prevent congestion.
• Sending fewer acknowledgments means imposing less load on
the network.
• Discarding Policy:- A good discarding policy by the routers
may prevent congestion and at the same time may not harm the
integrity of the transmission.
• Admission Policy:- An admission policy, which is a quality-of-
service mechanism, can also prevent congestion in virtual-circuit
networks.
• Switches in a flow first check the resource requirement of a flow
before admitting it to the network.
• A router can deny establishing a virtual-circuit connection if
there is congestion in the network or if there is a possibility of
future congestion.
Closed-loop congestion control (removal).
•   Closed-loop congestion control mechanisms try to alleviate
congestion after it happens.
•   Several mechanisms have been used by different protocols. We
describe a few of them here.
❑ Backpressure :- The technique of backpressure refers to a
congestion control mechanism in which a congested node stops
receiving data from the immediate upstream node or nodes.
• This may cause the upstream node or nodes to become
congested, and they, in turn, reject data from their upstream node
or nodes, and so on.
********** 10 **********
--- page 11 ---
• Backpressure is a node-to-node congestion control that starts
with a node and propagates, in the opposite direction of data
flow, to the source.
• The backpressure technique can be applied only to virtual circuit
networks, in which each node knows the upstream node from
which a flow of data is coming.
❑ Choke Packet:- A choke packet is a packet sent by a node to the
source to inform it of congestion.
Note the difference between the backpressure and choke-packet
methods.
•   In backpressure, the warning is from one node to its upstream
node, although the warning may eventually reach the source
station.
•   In the choke-packet method, the warning is from the router,
which has encountered congestion, directly to the source station.
• The intermediate nodes through which the packet has traveled
are not warned.
❑ Implicit Signaling:- In implicit signaling, there is no
communication between the congested node or nodes and the
source.
• The source guesses that there is congestion somewhere in the
network from other symptoms.
• For example, when a source sends several packets and there is
no acknowledgment for a while, one assumption is that the
network is congested.
• The delay in receiving an acknowledgment is interpreted as
congestion in the network; the source should slow down.
❑ Explicit Signaling:- The node that experiences congestion can
explicitly send a signal to the source or destination. The explicit-
signaling method, however, is different from the choke-packet
method.
•   In the choke-packet method, a separate packet is used for this
purpose; in the explicit-signaling method, the signal is included
in the packets that carry data.
********** 11 **********
--- page 12 ---
•   Explicit signaling can occur in either the forward or the
backward direction.
Q5   a.
What do you understand by CIDR in the network layer? Elaborate on
CO-3;   [10]
IPv6 addressing and its header format with a suitable diagram.
BL-1
Ans.   Classless Inter-Domain Routing addressing 2 marks
IPV6 addressing with header format 6 marks
Explanation of IPV6 header 2 marks
Classful addressing, which is almost obsolete, is replaced with classless
addressing.
In IPv4 addressing, a block of addresses can be defined as x.y.z.t /n
in which x.y.z.t defines one of the addresses and the /n defines the
mask.
The first address in the block can be found by setting the rightmost
32 − n bits to 0s.
The last address in the block can be found by setting the rightmost
32 − n bits to 1s.
b.   Describe Selective Repeat sliding window protocols. Show the sender
and receiver windows for a system having a window size =4 with the
following scenario.
CO-2;   i.   Frame 0 sent and acknowledged
[10]
BL-3   ii.   Frame 1,2,3 sent and received except frame 2
iii.   Show retransmission of frame 2
iv.   After acknowledgement of frames 2, frame 4 and frame 5 sent
and received with acknowledgement
********** 12 **********
--- page 13 ---
v.   Show the timeout for frame 6.
Ans.   Selective Repeat explanation 4 marks
◼ Go-Back-N always discards out-of-order frames
◼ Losing one frame may result in retransmission of
multiple frames
◼ Very inefficient in noisy link
◼ Selective Repeat ARQ allows frames to be received out of order
◼ Therefore, receive window > 1
Send and Receive Windows
◼ Sender and receiver share window space equally
◼ For m-bit sequence numbers
◼ Send window: up to 2m-1
◼ Receive window: up to 2m-1
Explain it with an example, Sender, receiver window diagram with
frame number 6 marks
Q6   a.
Illustrate HTTP and FTP protocols and their usage in real-world
CO-4;   [10]
applications.
BL-2
Ans. HTTP and FTP explanation 3 +3 = 6 marks
Real world applications 2 +2 = 4 marks
File Transfer Protocol (FTP)
Transferring files from one computer to another is one of the most
common tasks expected from a networking or internetworking
********** 13 **********
--- page 14 ---
environment. As a matter of fact, the greatest volume of data exchange
in the Internet today is due to file transfer.
FTP uses the services of TCP. It needs two TCP connections.
The well-known port 21 is used for the control connection and the well-
known port 20 for the data connection
Communication over Control Section
◼ FTP uses the same approach as SMTP to communicate across
the control connection.
◼   It uses the 7-bit ASCII character set Communication is achieved
through commands and responses.
◼ This simple method is adequate for the control connection
because we send one command (or response) at a time.
◼ Each command or response is only one short line, so we need not
worry about file format or file structure.
◼ Each line is terminated with a two-character (carriage return and
line feed) end-of-line token.
HTTP
◼ The Hypertext Transfer Protocol (HTTP) is a protocol used
mainly to access data on the World Wide Web.
◼ HTTP functions as a combination of FTP and SMTP.
◼ Unlike SMTP, the HTTP messages are not destined to be read by
humans; they are read and interpreted by the HTTP server and
HTTP client (browser).
◼ SMTP messages are stored and forwarded, but HTTP messages
are delivered immediately.
◼ The contents of the requested file or other information are
embedded in a response message.
◼ HTTP uses the services of TCP on well-known port 80
◼ Although HTTP uses the services of TCP, HTTP itself is a
stateless protocol.
◼ The client initializes the transaction by sending a request
message.
◼ The server replies by sending a response.
CO-1;   b.   Explain at least 4 network topologies with their advantages and
[10]
BL-2   disadvantages.
********** 14 **********
--- page 15 ---
Ans. Each topology with advantages and disadvantages [ 2*4=8 marks]
Diagrams and comparison 2 marks
BUS Topology
•   In a bus network, every device is connected to a single cable that
runs from one end of the network to the other at any instant at
most one machine is the master and is allowed to transmit.
•   All other machines are required to refrain from sending.
• Some mechanism is needed to resolve conflicts when two or
machines want to transmit simultaneously.
• For example : IEEE 802.3, Ethernet.
• Computers on an Ethernet can transmit whenever they want to;
•   If two or more packets collide, each computer just waits a
random
time and tries again later.
Star Topology
•   In this type of topology all the computers are connected to a
single hub through a cable. This hub is the central node and
all others nodes are connected to the central node.
Features of Star Topology
• Every node has its own dedicated connection to the hub.
• Hub acts as a repeater for data flow.
Advantages of Star Topology
•   Fast performance with few nodes and low network traffic.
• Hub can be upgraded easily.
• Easy to troubleshoot.
• Easy to setup and modify.
• Only that node is affected which has failed, rest of the nodes
can work smoothly.
Disadvantages of Star Topology
• Cost of installation is high.
• Expensive to use.
•   If the hub fails then the whole network is stopped because all
the nodes depend on the hub.
• Performance is based on the hub that is it depends on its
capacity
Mesh Topology
•   It is a point-to-point connection to other nodes or devices. All
the network nodes are connected to each other.
• Mesh has n(n-1)/2 physical channels to link n devices.
• There are two techniques to transmit data over the Mesh
topology, they are :
1. Routing
********** 15 **********
--- page 16 ---
2. Flooding
•   In routing, the nodes have a routing logic, as per the network
requirements. Like routing logic to direct the data to reach the
destination using the shortest distance.
•   In flooding, the same data is transmitted to all the network
nodes, hence no routing logic is required.
• The network is robust, and the its very unlikely to lose the data.
But it leads to unwanted load over the network.
Features of Mesh Topology
•   Fully connected.
•   Robust.
• Not flexible.
Advantages of Mesh Topology
• Each connection can carry its own data load.
•   It is robust.
•   Fault is diagnosed easily.
•   Provides security and privacy.
Disadvantages of Mesh Topology
•   Installation and configuration is difficult.
• Cabling cost is more.
• Bulk wiring is required.
Tree Topology
•   It has a root node and all other nodes are connected to it forming
a hierarchy. It is also called hierarchical topology. It should at
least have three levels to the hierarchy.
Features of Tree Topology
•   Ideal if workstations are located in groups.
• Used in Wide Area Network.
Advantages of Tree Topology
•   Extension of bus and star topologies.
• Expansion of nodes is possible and easy.
•   Easily managed and maintained.
•   Error detection is easily done.
Disadvantages of Tree Topology
• Heavily cabled.
********** 16 **********
--- page 17 ---
•   Costly.
•   If more nodes are added maintenance is difficult.
•   Central hub fails, network fails.
a.   Discuss block coding in computer networks.
Q7   Demonstrate CRC with the following example.
CO-2;   Evaluate transmitted frame using CRC with generator X3+X+1 and   [10]
BL-3   message bits 101101101. At the receiver side frame received is
10110110110110, justify if the message received correctly or not.
Ans. Block coding explanation 2 marks
Calculate the transmitted message 4 marks
Check received message 3 marks
Transmitter Side (Encoding)
Divisor (G) = 1011 (Degree m = 3)
Append m zeros (3 zeros) to the message bits (101101101).
Dividend = 101101101000
CRC = 101
Transmitted Frame: Message + CRC = 101101101101
Receiver Side (Verification)
The Remainder is NOT zero. (In this specific division, the remainder is
110).
Conclusion: The message was NOT received correctly.
CO-3;   b.   What is switching? Explain and compare packet switching and message
[10]
BL-2   switching with an appropriate example.
Ans.   Switching 1 mark
Packet switching with example 5 marks
Message switching with example 2 marks
Comparison 2 marks
◼ Switching techniques in computer networks to connect
devices and allow them to communicate with each other.
◼ Additionally, we can utilize switching techniques to transfer data
from one device to another.
◼ Switching allows multiple devices to share the same
communication channel simultaneously.
◼ As a result, it improves the efficiency of the network.
Furthermore, switching also enables the network to route data to
its intended destination.
********** 17 **********
--- page 18 ---
◼ Additionally, it provides a mechanism for error checking and
correction
Packet Switching
◼ Packet switching is a method used to transmit data over a
network.
◼ We divide data into small packets and transmit them over the
network independently.
◼ Each packet contains the data and destination address
information required to route the packet to its destination.
◼ In packet switching, each packet travels separately through the
network and can take different paths to reach its destination.
◼ This approach allows for more efficient use of network resources
because we can transmit multiple packets simultaneously over
the same network.
Message Switching
◼ Message switching is a method of data transmission that was
popular in the early days of networking, before the development
of packet switching. In message switching, we divide a message
into fixed-length blocks or frames.
◼ Furthermore, we transmit each frame independently through the
network. Additionally, each intermediate node stores the frames
until the entire message is received. Finally, the nodes forward
the entire message to its destination.
◼ Unlike packet switching, message switching is a store-and-
forward method of data transmission.
◼ It means that each intermediate node stores the entire message
until it can be forwarded to the next node.
◼ This can result in longer transmission times compared to packet
switching. We can only transmit each message when an
intermediate node receives all the parts of the message.
********** 18 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 62a861bfc753

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/Integrated_IT_7037/Computer Networks/ANS_Computer Networks(702AI0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Dec 2025
- Text: mixed (24 pages), mean OCR confidence 28.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / III / IV/Semester III/Semester V/Semester VII(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 05 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 24 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
CO,
BL,   Mark
SO   Q No   Question   s
CO1   A university plans to set up a campus network. Apply the concepts of wired and
BL3   wireless communication to explain how each could be used in this network with
SO1   Q1 a   respect to speed, reliability and security.   5
Wired Communication (Ethernet, Fiber Optic):
• Implementation: Connecting classrooms, labs, and offices using Ethernet
cables or fiber optics.
• Speed: High data transfer rates; suitable for heavy traffic like video
streaming and large file transfers.
•   Reliability: Very reliable; less affected by interference or obstacles.
•   Security: More secure; physical access required to tap into the network.
Wireless Communication (Wi-Fi):
• Implementation: Providing connectivity to mobile devices, laptops, and
guest users via access points across the campus.
• Speed: Moderate; can be affected by distance, number of users, and
interference.
•   Reliability: Less reliable than wired; signal may degrade with obstacles or
high traffic.
•   Security: Requires encryption (WPA3/WPA2); more vulnerable to attacks
than wired networks.
Soln   Marking Scheme (5 Marks):
********** 1 **********
--- page 2 ---
Wired Communication-Correctly explains implementation, speed, reliability
and security- 2 Marks
Wireless Communication- Correctly explains implementation, speed, reliability
and security - 2 Marks
Explains practical usage of wired and wireless networks in campus context-1
Marks
CO1,
BL 2,
SO 1 Q1 b   Compare and contrast the TCP/IP model with the OSI model on any five points   5
▪ Number of Layers: OSI has seven layers, while the TCP/IP model
typically consists of four or five layers.
▪   Protocol Dependency: TCP/IP was developed from a protocol-driven
approach based on real-world protocols, while OSI is a theoretical model
that is protocol-independent.
▪ Layers Combined: The TCP/IP model combines the OSI's Session,
Presentation, and Application layers into a single "Application Layer" and
merges the Data Link and Physical layers into a "Network Access Layer".
▪   Reliability: The TCP/IP model's reliability features are primarily handled
by the Transport layer (TCP protocol), while the OSI model's reliability
mechanisms are spread across different layers.
▪ Usage: The TCP/IP model is the practical, widely implemented model
used for the internet. The OSI model is primarily used as a reference or
teaching tool.
Soln
CO 2
BL-2   In a Slotted ALOHA system, the average number of frames generated per frame
SO 1   time is G = 1. Calculate the throughput S. What is the maximum throughput in
Q1 c   Slotted ALOHA   5
(2MARKS)
•   It can be proven that the average number of successful transmissions for
slotted ALOHA is S = G *e^-G.
• The maximum throughput Smax is 0.368, when G = 1. In other words, if
one frame is generated during one frame transmission time, then 36.8
percent of these frames reach their destination successfully.
• We expect G = 1 to produce maximum throughput because the vulnerable
time is equal to the frame transmission time.
•   Therefore, if a station generates only one frame in this vulnerable time
(and no other station generates a frame during this time), the frame will
reach its destination successfully.
Soln
********** 2 **********
--- page 3 ---
(2MARKS)
Formula:
S=G×e^−G
Substitution:
S=1×e^−1
=1×0.3679
=0.368S
(1MARKS)
Throughput ≈ 0.368 (36.8%)
So throughput = 36.8% efficiency.
CO-3;
SO-2;
BL-3   A block of address is granted to a small organization and one of the address is
200.140.64.48/26. Determine the first address and last address in the block.
Q1 d   Determine the total number of addresses in the block.   5
IP address = 200.140.64.48/26
Step 1⃣   Interpret /26
• Subnet mask length = 26 bits
• So network part = 26 bits, host part = 32−26=6 bits.
That means:
• Number of addresses per block = 26=64
Step 2⃣ — Find the network (first) address
In dotted decimal:
/26 mask →
255.255.255.192
(because the 26th bit boundary falls inside the 4th octet:
Soln   11111111.11111111.11111111.11000000)
********** 3 **********
--- page 4 ---
Each block starts at multiples of 64 in the 4th octet:
0, 64, 128, 192.
Now, given IP is 200.140.64.48, and 48 lies between 0 and 63.
So this IP belongs to the subnet that starts at .0.
Network address = 200.140.64.0   - 2 mark
Step 3⃣ — Find the broadcast (last) address
Add 63 (since 64 addresses per block, counting from 0):
0 + 63 = 63 → 200.140.64.63
Last address (broadcast address) = 200.140.64.48 – 2 mark
Step 4️⃣ — Compute total number of addresses
2(32−26)=26=64
Total addresses = 64   - 1 mark
CO-   i) Explain the block coding method for error detection and correction. (2 marks)
2;   ii)Two binary codewords are used in a communication system:
SO-
1;   • C1 = 1001101
BL-3   • C2 = 1110001
Compute the Hamming distance between C1 and C2 . (2 marks)
iii) A new codeword C3 = 1010101 is added to the set. Compute the pairwise
Hamming distances between C3 and the other codewords. (2 marks)
iv) Based on the minimum Hamming distance of the code, determine how many
errors the code can detect and how many it can correct. Justify your answer. (4
Q2 a   marks)   10
i) Explain the block coding method for error detection and correction. (2 marks)
•   In block coding, the message is divided into blocks, each of k bits,
called data words .
•   r redundant bits are added to each block to make the length n=k+r
• The resulting n bit blocks are called codewords. (1 mark)
• The block coding process is one-to-one; the same dataword is always
encoded as the same codeword.
• Message bits (k): The actual data to be sent
• Codeword bits (n): The message bits plus redundant bits
• Redundant bits (n - k): Extra bits added for error detection and
correction (1 mark)
ii) Compute the Hamming distance between C1 and C2
Step : (1 mark)
Final answer: No of 1’s = 4️ . Hence Hamming Distance = 4️ (1
mark)
Soln
********** 4 **********
--- page 5 ---
iii) A new codeword C3 = 1010101 is added to the set. Compute the pairwise
Hamming distances between C3 and the other codewords.
A. ( C3 = 1010101 ) vs ( C1 = 1001101 )
Steps to show (1 mark)
Hamming distance = 2   (1 mark)
B.( C3 = 1010101 ) vs ( C2 = 1110001 )
Steps to show (1 mark)
Hamming distance = 2   (1 mark)
iv) Determine error detection and correction capabilities
•   ( d(C_1, C_2) = 4 )
•   ( d(C_1, C_3) = 2 )
•   ( d(C_2, C_3) = 2 )
so, d{min} = 2   (1mark)
Error detection: (1 mark)
• A code can detect up to ( d_{min} - 1 ) errors.
•   So: can detect ( 2 - 1 = 1 ) error
Error correction: 0 error (1 mark)
Final concluding answer with justification (2 mark)
• Minimum distance = 2
• Can detect 1 error, correct 0 errors
CO-3;   A company wants to set up a network for smooth data transfer between its
SO-1;   offices. Based on your understanding, which switching technique—circuit,
BL-3   packet, or message—would you recommend? Explain how each works and
Q2 b   compare their pros, cons, and best use cases to support your choice.   10
Switchin
g   Working   Advantag Disadvantag   Best Use
Techniq   Principle   es   es   Case
ue
Dedicated
Reliable,   Voice
path is   Inefficient
Circuit   continuou   communicati
established   for data; idle
Switchin   s   on (e.g.,
before   time wastes
g   connectio   telephone
communicati   resources.
n.   networks).
on begins.
Data is split
into packets   Efficient
sent   bandwidt
Packet   Possible   Internet, real-
independentl h usage;
Switchin   delays,   time data
y and   supports
g   packet loss.   transmission.
reassembled   multiple
at   users.
Soln   destination.
********** 5 **********
--- page 6 ---
Entire
No need
message is
for   High delay   Email, non-
Message   stored and
dedicated due to   real-time
Switchin forwarded
path;   storage at   communicati
g   through
flexible   each node.   on.
intermediate
routing.
nodes.
Recommendation -Packet switching is recommended for the company’s
network due to its efficiency, scalability, and ability to handle diverse data
types across multiple branches.
Explanation of all three techniques (working principles)- 3 marks
Comparison of advantages and disadvantages -   3 marks
Identification of suitable applications-   2 marks
Justified recommendation based on scenario-   2 marks
BL 1,
CO 1,
SO 1 Q3 a   Define the following:- a) LAN b) MAN c)PAN d) WAN e) ARPANET   5
1 mark for each definition
a) LAN (Local Area Network):
A Local Area Network is a network that connects computers and devices within
a limited geographical area such as a home, school, office building, or campus.
• Example: A network connecting computers in a computer lab.
• Data transfer speed: High (typically 100 Mbps to 10 Gbps).
b) MAN (Metropolitan Area Network):
A Metropolitan Area Network covers a larger area than a LAN, usually
spanning a city or a large campus. It connects multiple LANs together within a
metropolitan area.
• Example: A network connecting different branches of a university
within a city.
c) PAN (Personal Area Network):
A Personal Area Network is the smallest type of network, used for connecting
personal devices within a short range (usually within 10 meters).
• Example: Connecting a smartphone to a laptop via Bluetooth.
d) WAN (Wide Area Network):
A Wide Area Network covers a very large geographical area, often a country or
even globally. It connects multiple LANs and MANs using public networks like
the Internet or satellite links.
Soln
********** 6 **********
--- page 7 ---
• Example: The Internet is the largest WAN.
e) ARPANET (Advanced Research Projects Agency Network):
ARPANET was the first operational packet-switching network and the
precursor to the modern Internet. It was developed in the late 1960s by the U.S.
Department of Defense’s ARPA (now DARPA) to connect research institutions
and allow resource sharing.
CO3,
BL2   Explain the different types of OSPF packets used for communication between
SO 1 Q3 b   routers.   5
OSPF uses five types of packets for communication between routers:
1. Hello Packet – Used to discover and maintain neighbor relationships.
2. Database Description (DBD) Packet – Used to summarize the contents
of a router’s link-state database.
3. Link-State Request (LSR) Packet – Sent to request specific link-state
information from a neighbor.
4. Link-State Update (LSU) Packet – Carries detailed link-state
information (LSAs) to other routers.
5. Link-State Acknowledgment (LSAck) Packet – Confirms the receipt
of LSUs to ensure reliable delivery.
Summary:
OSPF uses 5 packet types — Hello, DBD, LSR, LSU, and LSAck — to form
neighbors, exchange topology data, and keep the network synchronized.
Soln
CO5   Explain, with the help of a neat diagram, how the World Wide Web (WWW)
BL 2   enables users to access online information through the HTTP protocol. Describe
SO 1   the components and working mechanism of the Web, and interpret how HTTP
facilitates communication between a client and a server when a user enters a
Q3 c   URL such as http://www.example.com   10
The World Wide Web (WWW) is a global information system that enables
users to access interlinked documents and multimedia content over the Internet.
It operates on a client–server model, where the HTTP protocol governs
Soln.   communication between browsers (clients) and web servers.
********** 7 **********
--- page 8 ---
Diagram and explanation: WWW and HTTP Communication Flow (4
marks)
• Request–Response Model:
HTTP follows a simple two-way exchange — the client sends a request,
and the server responds.
•   Stateless Protocol:
Each request is independent, improving scalability and simplicity.
• Structured Message Format:
o Request Line: Method, resource, version
o Headers: Metadata (host, content type, etc.)
o Body: Optional data (for POST requests)
• Reliable Transport:
Uses TCP to ensure ordered, error-free data delivery.
• Status Codes:
Help the browser understand response outcomes (e.g., 200 OK, 404
Not Found).
Components of the World Wide Web (3 marks)
Component   Description
Application (e.g., Chrome, Firefox) used to send reque
Web Browser (Client)
display web pages.
Computer that stores and serves web pages when reque
Web Server
clients.
Uniform Resource   Unique address that identifies a specific web resource.
Locator (URL)   Example: http://www.example.com/index.html.
HTTP (Hypertext   Communication protocol used for transferring web doc
Transfer Protocol)   between browser and server.
HTML (Hypertext
Standard language used to structure and format web pa
Markup Language)
Working Mechanism of the WWW (3 marks)
********** 8 **********
--- page 9 ---
When a user types http://www.example.com in the browser:
1. URL Parsing:
The browser divides the URL into:
o Protocol → http
o Host name → www.example.com
o File/resource → default index.html
2. DNS Resolution:
The browser queries the DNS to obtain the IP address of the web server
hosting www.example.com.
3. Connection Establishment:
A TCP connection is initiated between the client and the server on port
80 (default for HTTP).
4. HTTP Request:
The browser sends an HTTP request message (e.g., GET
/index.html HTTP/1.1) asking for the web page.
5. HTTP Response:
The server locates the requested file, encapsulates it in an HTTP
response message with a status code and sends it back to the browser.
6. Rendering the Page:
The browser interprets the HTML, CSS, and scripts received and
displays the webpage to the user.
7. Connection Termination:
Once the transfer is complete, the TCP connection is closed.
CO-3
SO-1
BL-2   Summarize the IPv6 address 0:15::1:12:1213 to its full, original form. Write a
Q4 a   comparison between IPv4 and IPv6 packet headers.   10
First, we need to align the left side of the double colon (::) with the left side of
the original IPv6 address pattern, and the right side of the double colon with the
right side of the original pattern. This helps us determine how many groups of
zeros we need to replace the double colon with.
For the given the address:
0:15::1:12:1213
We align the known parts as:
0:15: (left side), then the double colon ::, then 1:12:1213 (right side).
By counting how many groups of zeros are missing between the left and right
parts to complete the full 8-group IPv6 address, we find that the double colon
represents four groups of zeros.
Therefore, the original expanded address is:
0000:0015:0000:0000:0000:0001:0012:1213
Comparison between IPv4 and IPv6 packet headers:
➢ The header length field is removed in IPv6 because the header length is
Soln   fixed in this version.
********** 9 **********
--- page 10 ---
➢ The service type field is also removed in IPv6. Instead, the priority and
flow label fields together perform the function that the service type field
used to handle.
➢ The total length field from IPv4 is replaced by the payload length field in
IPv6.
➢ The identification, flag, and offset fields are no longer part of the base
header in IPv6. Instead, they are included in a separate fragmentation
extension header.
➢ The TTL (Time To Live) field in IPv4 is renamed to hop limit in IPv6.
➢ The protocol field in IPv4 is replaced by the next header field in IPv6.
➢ The header checksum is eliminated in IPv6 because checksums are
handled by upper-layer protocols, so it is not needed at the IPv6 header
level.
➢ The option fields that exist in IPv4 are implemented as extension headers
in IPv6.
(The IPv6 address 0:15::1:12:1213 to its full, original form-05M and
Any five point of comparison between IPv4 and IPv6 packet headers-05M)
BL- 2
CO-4   Describe the User Datagram Protocol (UDP) in detail with suitable diagram.
SO-1 Q4 b   Also explain how it differs from TCP?   10
The User Datagram Protocol (UDP) is called a connectionless, unreliable
transport protocol. It does not add anything to the services of IP except to provide
process-to-process communication instead of host-to-host communication.
• The User Datagram Protocol (UDP) is called a connectionless, unreliable
transport protocol.
•   It does not add anything to the services of IP except to provide process-
to-process communication instead of host-to-host communication.
•   It performs very limited error checking.
•   If UDP is so powerless, why would a process want to use it?
• UDP is a very simple protocol using a minimum of overhead.
•   If a process wants to send a small message and does not care much
about reliability, it can use UDP.
• Sending a small message by using UDP takes much less interaction
between the sender and receiver than using TCP (Transmission
control protocol) or SCTP (Stream control transmission protocol).
UDP Operations:
Connectionless Services: Each user datagram sent by UDP is an independent
datagram. There is no relationship between the different user datagrams even if
they are coming from the same source process and going to the same destination
program. The user datagrams are not numbered. Also, there is no connection
establishment and no connection termination, as is the case for TCP. This means
Soln   that each user datagram can travel on a different path. Each request must be small
********** 10 **********
--- page 11 ---
enough to fit into one user datagram. Only those processes sending short
messages should use UDP.
Flow and Error Control:
UDP is a very simple, unreliable transport protocol. There is no flow control and
hence no window mechanism. The receiver may overflow with incoming
messages.
There is no error control mechanism in UDP except for the checksum. This means
that the sender does not know if a message has been lost or duplicated. When the
receiver detects an error through the checksum, the user datagram is silently
discarded.
Encapsulation and Decapsulation:
To send a message from one process to another, the UDP protocol encapsulates
and decapsulates messages in an IP datagram.
Encapsulation
When a process has a message to send through UDP, it passes the message to
UDP along with a pair of socket addresses and the length of data.
UDP receives the data and adds the UDP header.
UDP then passes the user datagram to IP with the socket addresses.
IP adds its own header, using the value 17 in the protocol field, indicating that
the data has come from the UDP protocol.
Decapsulation
When the message arrives at the destination host, the physical layer decodes the
signals into
bits and passes it to the data link layer.
The data link layer uses the header (and the trailer) to check the data. If there is
no error, the header and trailer are dropped and the datagram is passed to IP.
The IP software does its checking. If there is no error, the header is dropped and
the user datagram is passed to UDP with the sender and receiver IP addresses.
Queuing:
********** 11 **********
--- page 12 ---
Transmission   Control   Protocol   User Datagram Protocol
Basis   (TCP)   (UDP)
UDP is the Datagram-
oriented protocol. This
is because there is no
TCP is   a   connection-oriented
overhead for opening a
protocol.   Connection orientation
connection,
means that the communicating
Type   of   maintaining   a
devices   should   establish   a
Service   connection,   or
connection before transmitting data
terminating   a
and should close the connection
connection. UDP   is
after transmitting the data.
efficient for broadcast
and multicast types of
network transmission.
TCP is reliable as it guarantees the The delivery of data to
Reliabilit
delivery of data to the destination   the destination cannot
y
router.   be guaranteed in UDP.
Error   TCP   provides   extensive error- UDP has only the basic
checking   checking mechanisms. It is because   error-checking
mechanis   it provides flow   control and mechanism
m   acknowledgment of data.   using checksums.
Acknowle An acknowledgment segment is No   acknowledgment
dgment   present.   segment.
********** 12 **********
--- page 13 ---
There is no sequencing
Sequencing of data is a feature of
of data in UDP. If the
Transmission   Control Protocol
Sequence   order is required, it has
(TCP). this means that packets
to be managed by the
arrive in order at the receiver.
application layer.
UDP is faster, simpler,
TCP is comparatively slower than
Speed   and more efficient than
UDP.
TCP.
There   is   no
retransmission of lost
Retransmi   Retransmission of lost packets is
packets in the User
ssion   possible in TCP, but not in UDP.
Datagram   Protocol
(UDP).
Header   TCP has a (20-60) bytes variable UDP has an 8 bytes
Length   length header.   fixed-length header.
Weight   TCP is heavy-weight.   UDP is lightweight.
Handshak
It's a connectionless
ing   Uses handshakes such as SYN,
protocol   i.e.   No
Techniqu   ACK, SYN-ACK
handshake
es
Broadcast   UDP   supports
TCP doesn't support Broadcasting.
ing   Broadcasting.
CO-2,   Apply the principles of the Selective Repeat ARQ Sliding Window Protocol to
BL-3   determine the maximum permissible sender and receiver window sizes for
SO-1   frame sequence number field of 3 bits, and explain with the help of diagram
how frames are transmitted, acknowledged, and buffered at both the sender and
receiver ends.
Justify why this window size is chosen, and analyze how incorrect window
Q5 a   sizing can lead to frame mis ordering or acknowledgment ambiguity.   10
Explanation of Selective Repeat ARQ   (1 marks),
window size   (1marks),
Soln   explanation of frame transmission   (3 marks),
********** 13 **********
--- page 14 ---
justification of window size 5 marks   ( 3 explanation and 2 marks
diagram)
Solution: In Selective Repeat ARQ only the lost or error frames are
retransmitted, whereas correct frames are received and buffered. The receiver
while keeping track of sequence numbers buffers the frames in memory and
sends NACK for only frames which are missing or damaged. The sender will
send/retransmit a packet for which NACK is received.
Step 1 − Frame 0 sends from sender to receiver and set timer.
Step 2 − Without waiting for acknowledgement from the receiver another
frame, Frame1 is sent by sender by setting the timer for it.
Step 3 − In the same way frame2 is also sent to the receiver by setting the timer
without waiting for previous acknowledgement.
Step 4 − Whenever sender receives the ACK0 from receiver, within the frame 0
timer then it is closed and sent to the next frame, frame 3.
Step 5 − whenever the sender receives the ACK1 from the receiver, within the
frame 1 timer then it is closed and sent to the next frame, frame 4.
Step 6 − If the sender doesn’t receive the ACK2 from the receiver within the
time slot, it declares timeout for frame 2 and resends the frame 2 again, because
it thought the frame2 may be lost or damaged.
********** 14 **********
--- page 15 ---
BL:   Explain SMTP and its role in email communication. Describe the different
2,   phases of SMTP communication, detailing the purpose of each phase and the
SO: 2   typical commands used. Illustrate your answer with a labelled diagram showing
CO: 5 Q5 b   the flow between the client and server   10
SMTP Explanation: 2 marks
Diagram: 2 marks
Phases: 6 marks
Soln   •One of the most popular Internet services is electronic mail (e-mail).
********** 15 **********
--- page 16 ---
•E-mail allow users to exchange messages. It is considered as a one-way
transaction.
User Agent:
•A user agent is a software package that composes , reads , replies to , and
forwards messages.
•Types of user agents:
Command driven
GUI based
•Mailing list: E-mail allows one name, an alias to represent several different e-
mail addresses
The protocol that defines the MTA client and server in the internet is called as
Simple Mail Transfer Protocol(SMTP)
•SMTP uses commands and responses to transfer messages between an MTA
client and MTA server.
•Commands: Keyword: argument(s)
•Responses: Responses are sent from the server to the client. A response is a three
digit code that may be followed by additional textual information
MAIL TRANSFER PHASES
Connection Establishment
********** 16 **********
--- page 17 ---
1.The server sends code 220(service ready) to tell the client that it is ready to
receive mail. If the server is not ready it sends code 421(service not available)
2.The client sends the HELLO message to identify itself, using its domain name
address.
3.The server responds with code 250(request command completed)
Message transfers
1.The client sends the MAIL FROM message to introduce the sender of the
message.
2.The server responds with code 250 or some other appropriate code.
3.The client sends the RCPT TO message, which includes the mail address of the
recipient.
4.The server responds with code 250 or some other appropriate code.
5.The client sends the DATA message to initialize the message transfer.
6.The server responds with code 354(start mail input)
7.The client sends the contents of the message in consecutive lines.
8.The server responds with code 250 or some other appropriate code
Connection Termination
1.The client sends the QUIT command
2.The server responds with code 221(service closing transmission channel)
CO1
SO1   List different types of unguided transmission media and write any two
BL-1 Q6 a   characteristics of each.   5
Radio waves
Radio waves are Omnidirectional, useful for multicasting. AM and FM radio,
television, maritime radio, cordless phones, and paging are examples of
multicasting.
Radio waves a good candidate for long-distance broadcasting.
Advantage: receives signal inside a building
Soln   Disadvantage: Cannot isolate a communication
********** 17 **********
--- page 18 ---
Microwaves
Microwave propagation is line-of-sight.
Very high-frequency microwaves cannot penetrate walls
The microwave band is relatively wide, almost 299 GHz. Therefore wider
subbands can be assigned, and a high data rate is possible
Use of certain portions of the band requires permission from authorities.
Microwaves are used in cellular phones , satellite networks and
wireless LANs
Infrared Waves
Infrared signals can be used for short-range communication in a closed area
using line-of-sight propagation.
Infrared waves, having high frequencies, cannot penetrate walls.
The wide bandwidth can be used to transmit digital data with a very high data
rate.
Infrared waves, having high frequencies, cannot penetrate walls.
The wide bandwidth can be used to transmit digital data with a very high data
rate.
The recent standard defines a data rate of 4 Mbps.
CO2,
BL-4   Compare 1-persistent, non-persistent, and p-persistent CSMA strategies with
SO-1 Q6 b   diagrammatic representations   5
Points of 1-persistent, non-persistent, and p-persistent 1M each )- 3M , diagram
2M
1-Persistent CSMA
• Working:
The node listens to the channel.
o   If idle → transmit immediately.
o   If busy → keep listening continuously and transmit immediately
when it becomes free.
•   Pros: Simple, high channel utilization.
• Cons: High chance of collisions if multiple nodes are waiting (because
they all send immediately once the channel is free).
Non-Persistent CSMA
• Working:
o The node listens to the channel.
Soln   o   If idle → transmit immediately.
********** 18 **********
--- page 19 ---
o   If busy → does not continuously sense. Instead, it waits a random
backoff time and then checks again.
•   Pros: Lower chance of collisions.
• Cons: Higher delay, because nodes may wait even if the channel
becomes free.
p-Persistent CSMA (used in slotted channels, e.g., LANs)
• Working:
o The channel is divided into discrete time slots.
o When the channel is sensed idle:
▪ Transmit with probability p.
▪ Wait until the next time slot with probability 1 − p, then
repeat.
•   Pros: Balance between efficiency and collision probability; reduces
chance of many nodes transmitting at once.
• Cons: Performance depends on proper tuning of p.
CO-4
BL-2
SO-1   Explain open loop and closed loop congestion control policy in transmission
Q6 c   control protocol. Describe any two policies from each type.   10
Open Loop: Open loop congestion control mechanisms try to remove the
congestion before it happens.
Works independently of feedback from the network.   ---- 1M
Closed Loop: Closed loop congestion control mechanisms try to remove the
congestion after it happens.
Uses feedback from the network (ACKs, packet loss, delays) to adjust
transmission.
--- 1M
Open Loop Policies (any 2)   -----   2 *2 = 4M
Soln
********** 19 **********
--- page 20 ---
Retransmission Policy
• The sender retransmits a packet, if it feels that the packet it has sent is lost or
corrupted.
• However retransmission in general may increase the congestion in the network.
But we need to implement good retransmission policy to prevent congestion.
• The retransmission policy and the retransmission timers need to be designed to
optimize efficiency and at the same time prevent the congestion.
Window Policy
• To implement window policy, selective reject window method is used for
congestion control.
• Selective Reject method is preferred over Go-back-n window as in Go-back-n
method, when timer for a packet times out, several packets are resent, although
some may have arrived safely at the receiver. Thus, this duplication may make
congestion worse.
• Selective reject method sends only the specific lost or damaged packets.
Acknowledgement Policy
• The acknowledgement policy imposed by the receiver may also affect
congestion.
• If the receiver does not acknowledge every packet it receives, it may slow down
the sender and help prevent congestion.
• Acknowledgments also add to the traffic load on the network. Thus, by sending
fewer acknowledgements we can reduce load on the network.
• To implement it, several approaches can be used:
1. A receiver may send an acknowledgement only if it has a packet to be sent.
2. A receiver may also decide to acknowledge only N packets at a time.
Admission Policy
• An admission policy, which is a quality-of-service mechanism, can also prevent
congestion in virtual circuit networks.
• Switches in a flow first check the resource requirement of a flow before
admitting it to the network.
• A router can deny establishing a virtual circuit connection if there is congestion
in the "network or if there is a possibility of future congestion.
********** 20 **********
--- page 21 ---
Closed Loop Policies (any 2)   ------- 2*2 = 4M
Backpressure
• Backpressure is a node-to-node congestion control that starts with a node and
propagates, in the opposite direction of data flow.
• The backpressure technique can be applied only to virtual circuit networks. In
such virtual circuit each node knows the upstream node from which a data flow
is coming.
• In this method of congestion control, the congested node stops receiving data
from the immediate upstream node or nodes.
• This may cause the upstream node on nodes to become congested, and they, in
turn, reject data from their upstream node or nodes.
• As shown in fig node 3 is congested and it stops receiving packets and informs
its upstream node 2 to slow down. Node 2 in turns may be congested and informs
node 1 to slow down. Now node 1 may create congestion and informs the source
node to slow down. In this way the congestion is alleviated. Thus, the pressure
on node 3 is moved backward to the source to remove the congestion.
Choke Packet
• In this method of congestion control, congested router or node sends a special
type of packet called choke packet to the source to inform it about the congestion.
• Here, congested node does not inform its upstream node about the congestion
as in backpressure method.
• In choke packet method, congested node sends a warning directly to the source
station i.e. the intermediate nodes through which the packet has travelled are not
warned.
********** 21 **********
--- page 22 ---
CO3,   Consider a network topology consisting of nodes A, B, C, D, E, F, and G.
BL3,   The directed edges between these nodes and their corresponding positive
4 ,   weights are given in the table below
SO2
Edge   Distance
A->B   4
A->C   2
B->C   5
B->D   10
C->D   3
C->E   4
D->E   1
D->F   2
E->F   3
F->G   5
Using Dijkstra’s Algorithm:
i. Determine the shortest path from the source node A to the destination
node G.
ii. Compute the shortest distance from node A to node G.
iii. Show all intermediate steps, including the initialization, selection of the
minimum distance node, for each iteration.
iv.   Illustrate the original network topology and the final shortest path with
the corresponding distance values clearly marked on the edge
Q7 a   10
The shortest path A->C ->D->F->G, shortest distance is 12
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
(iii)   Intermediate Steps - 3marks
(iv)   Original network topology ( 1marks) + final shortest
path with the corresponding distance values clearly
marked on the edges ( 1 marks)
Soln
CO-4;
SO-1;   Draw a neat diagram and explain the working of the Token Bucket Algorithm.
BL-2 Q7 b   State any two limitations of the Token Bucket algorithm   10
********** 22 **********
--- page 23 ---
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for
limitations.
Explanation of working based on the following points is expected.
• A bucket holds tokens, each token allowing the transmission of a certain
number of bytes (usually 1 token = 1 byte or 1 packet).
• Tokens are added to the bucket at a constant rate r (tokens per second).
• The bucket has a maximum capacity B (in tokens).
• When a packet arrives:
o   If there are enough tokens, the packet is transmitted, and tokens
are removed from the bucket.
o   If not enough tokens, the packet is either delayed (until enough
tokens are available) or dropped (if there's no buffering).
This allows bursts of traffic up to B bytes to be sent at once (if the bucket is full),
but enforces an average rate of r bytes/sec over time.
Two Limitations of the Token Bucket Algorithm
1. Complexity with Bursty Traffic:
o While the algorithm allows short bursts, if traffic bursts are too
frequent or too large, it may still overwhelm downstream systems,
leading to queue overflows.
2. No Built-in Fairness or Priority:
o The algorithm does not distinguish between different types of
traffic. So, critical or high-priority packets can be delayed just like
any others, making it unsuitable for quality of service (QoS)
Soln   differentiation without additional mechanisms.
********** 23 **********
--- page 24 ---
FRR IRD AC HOH
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper e79fc1f97000

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CS_7055/Computer Networks/ANS_Computer Networks(702AI0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 518ebb22e5bf

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_Computer_7002/Computer Networks/ANS_Computer Networks(702AI0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper b2ded4fc3d00

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CyberSecurity_7010/Computer Networks/ANS_Computer Networks(702AI0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 252628cfe636

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_IT_7001/Computer Networks/ANS_Computer Networks(702AI0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 33c09b8af7a9

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MBATech_Computer_7047/Computer Networks/ANS_Computer Networks(702AI0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 27b8258bd379

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MBATech_IT_7041/Computer Networks/ANS_Computer Networks(702AI0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper feecaf7089c1

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CSBS_7036/Computer Networks/ANS_Computer Networks(702AI0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (CSBS)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures on the right-hand side indicate full marks.
Q1
Answer briefly:   [20]
a.   Discuss all unguided media used for communication in computer
CO-1 ;   [5]
BL-2   networks.
Ans. Each unguided transmission: 1.5 * 3= 4.5 Marks
List all type correctly: 0.5 Mark
Unguided media transport electromagnetic waves without using a
physical conductor. This type of communication is often referred to as
wireless communication.
Infrared   Radio Waves   Microwaves
Infrared is used for   Radio waves are   Microwaves are a line
short-range   the type of wireless   of sight transmission,
communication like   communication that   meaning both the
TV remotes, mobile   can travel large   antennas sending and
distances as well as
********** 1 **********
--- page 2 ---
phones, personal   can penetrate any   receiving should be
computers, etc.   wall   properly aligned.
The frequency range   The frequency range   Microwaves have a
of infrared rays   of radio waves:3KHz   frequency range
300GHz – 400THz   – 1GHz.   between 1GHz –
300GHz.
The limitation of   They are
infrared rays is that   unidirectional, as they
they cannot penetrate   can move in only one
any obstacles and can   It can travel large   direction, and
only use for short-   distances as well as   therefore it is used in
range   can penetrate any wall   point-to-point
( Omni-directional,   communication or
unicast
communication such
as radar and satellite.
b.   Consider two stations on wireless Aloha network are 500 km apart. Signal
CO-2 ;   propagates at 3 x 108 m/s. Find out the back off time for different values [5]
BL-3
of K=1 and 2.
Ans.   Distance between stations = 500 km = 500 × 10³ m
Propagation speed = 3 × 10⁸ m/s
Step 1: Calculate Propagation Time (Tp)
Step 2: Backoff Time Formula (ALOHA)
In ALOHA, the backoff time is:
where:
• K = random integer (given)
• Tp = propagation time
Step 3: Compute Backoff Time
Case 1: K = 1
********** 2 **********
--- page 3 ---
Case 2: K = 2
Final Answer
• For K = 1 → Backoff Time = 1.67 ms
• For K = 2 → Backoff Time = 3.34 ms
CO-3 ;   c.   Explain the role of ARP, RARP and DHCP protocol in address mapping. [5]
BL-2
Ans. ARP explanation 2 marks
RARP explanation 1 mark
DHCP explanation 2 marks
ARP associates an Internet Protocol (IP) address with its physical
address. On a typical physical network, such as a LAN, each device on a
link is identified by a physical or station address that is usually imprinted
on the network interface card (NIC).
An ARP request is broadcast; an ARP reply is unicast.
RARP finds the logical address for a machine that only knows its
physical address.
The RARP request packets are broadcast; the RARP reply packets are
unicast.
DHCP
The Dynamic Host Configuration Protocol (DHCP) has been devised to
provide static and dynamic address allocation that can be manual or
automatic. A DHCP server has a database that statically binds physical
addresses to IP addresses.
CO-4 ;   d.   Give comparison between UDP and TCP protocols in detail   [5]
BL-2
Ans. At least 5 comparisons: 5 Marks
TCP (Transmission Control UDP (User Datagram
Feature   Protocol)   Protocol)
Connection-Oriented:   Connectionless: Just starts
Establishes a session via a   sending data without
Connection   "Three-way Handshake"   checking if the receiver is
Type   before sending data.   ready.
Guaranteed: If a packet is   Unreliable: "Best-effort"
lost, it is retransmitted. Data   delivery. If a packet is lost,
Reliability   arrives intact.   it stays lost.
Ordered: Packets are   Unordered: Packets may
reassembled in the exact   arrive in any order; the
Ordering   sequence they were sent.   application must handle it.
********** 3 **********
--- page 4 ---
Slower: Overhead from   Faster: Minimal overhead
headers (20-60 bytes) and   (8-byte header) and no
Speed   acknowledgment wait times.   delay for acknowledgments.
Yes: It slows down   No: It sends data at a
Flow/Conges transmission if the network is constant rate regardless of
tion Control   congested.   network health.
a.   Show the working of CSMA/CD with the help of appropriate flow
Q2
chart.   [10]
CO-2;
BL-2   Discuss how CSMA/CD is helpful in collision finding.
Ans.   Description of CSMA/CD with flowchart: 7 Marks
CSMA/CD is helpful in collision finding: 3 Marks
CO-4;   b.   Draw the TCP header format and explain the meaning of every fields.
[10]
BL-2   Why TCP is called as connection-oriented protocol?
Ans. TCP Header format diagram 4 Marks
Description of each field 4 Marks
TCP as connection-oriented 2 Marks
********** 4 **********
--- page 5 ---
Q3   a.   Explain Distance vector routing algorithm with an example. Also
[10]
CO-3;   discuss all type of timers used by RIP protocol.
BL-3
Ans.   Distance vector routing with example: 3 +3 = 6 Marks
RIP Timers : 4 Marks
Distance Vector Routing
◼ In distance vector routing, a router need not know the entire
path to every network segment; it only requires to know the
direction or vector in which to send the packet.
◼ The technique determines the direction (vector) and distance
(hop count) to any network in the internetwork.
◼ Distance vector routing algorithms periodically send all or parts
of their routing table to their adjacent neighbours.
◼ The routers running a distance vector routing protocol will
automatically send periodic updates even if there are no changes
in the network.
********** 5 **********
--- page 6 ---
◼ A router can verify all the known routes and alters its local
routing table on the basis of the updated information received
from neighboring routing.
◼ This process is referred to as “routing by rumour” because the
routing information that a router has of the network topology is
based on the perspective of the routing table of the neighbor
router.
◼ RIP and IGRP is a commonly used distance vector protocol that
uses hop counts or its routing metrics.
Example
RIP Timers
CO-1;   b.   Describe all layers and compare ISO-OSI model and TCP/IP model in
[10]
BL-2   detail.
Ans.   All 7 layers discription 7 Marks
Comparison between OSI and TCP/IP model 3 Marks
********** 6 **********
--- page 7 ---
a.   An ISP is granted a block of addresses starting with 200.50.0.0/16
(65,536 addresses). The ISP needs to distribute these addresses to three
groups of customers as follows:
The first group has 64 customers; each need 250 addresses.
Q4
The second group has 128 customers; each need 120 addresses.
CO-3;   The third group has 256 customers; each need 60 addresses.   [10]
BL-3
i.   Find the number of allocated addresses in each of the ISP blocks.
ii.   Find the range of addresses for each organization and the
number of unallocated addresses.
Ans. Finding number of addresses allocated in each block: 3 Marks
Calculating remaining address: 1 Mark
Finding range of address for each block : 6 Marks
Total
Group   Address Range
Allocated
Group 1   200.50.0.0 – 200.50.63.255/24   16,384
Group 2   200.50.64.0 – 200.50.127.255/25 16,384
Group 3   200.50.128.0 – 200.50.191.255/26 16,384
Unallocated 200.50.192.0 – 200.50.255.255   16,384
CO-4;   b.   Justify the role of leaky bucket and token bucket algorithm in quality of
[10]
BL-2   service. Illustrate these protocols in detail with diagram.
Ans.   Quality of Services improvement 2 marks
Token Bucket algorithm with diagram 4 marks
Leaky Bucket algorithm with diagram 4 marks
Leaky Bucket
•   If a bucket has a small hole at the bottom, the water leaks from
the bucket at a constant rate as long as there is water in the bucket.
********** 7 **********
--- page 8 ---
• The rate at which the water leaks does not depend on the rate at
which the water is input unless the bucket is empty.
•   If the bucket is full, the water overflows. The input rate can vary,
but the output rate remains constant.
•   Similarly, in networking, a technique called leaky bucket can
smooth out bursty traffic. Bursty chunks are stored in the bucket
and sent out at an average rate.
Token Bucket
• The leaky bucket is very restrictive. It does not credit an idle host.
• For example, if a host is not sending for a while, its bucket
becomes empty.
• Now if the host has bursty data, the leaky bucket allows only an
average rate. The time when the host was idle is not taken into
account.
• On the other hand, the token bucket algorithm allows idle hosts to
accumulate credit for the future in the form of tokens.
•   Let’s assume that the bucket capacity is 10,000 tokens and tokens
are added at the rate of 1000 tokens per second.
•   If the system is idle for 10 seconds (or more), the bucket collects
10,000 tokens and becomes full.
•   In other words, the host can send bursty data as long as the bucket
is not empty.
• The token bucket allows bursty traffic at a regulated maximum
rate.
********** 8 **********
--- page 9 ---
Q5   a.
Discuss classful addressing in network layer. Draw the header format of
CO-3;   [10]
IPV4 and explain in detail.
BL-1
Ans.   Classful addressing: 4 Marks
IPV4 header with explanation: 6 Marks
Classful addressing
IPV4 Header Format
CO-2;   b.   Draw and explain GO Back N ARQ window protocol with data flow
[10]
BL-3   diagram of m=2 bits.
Ans. Go back N explanation 4 marks
Explain it with an example, Sender, receiver window diagram with
frame number 6 marks
◼ Allows multiple frames to be sent before waiting for ACK
********** 9 **********
--- page 10 ---
◼ These frames must be numbered differently
◼ Frame numbers are called Sequence numbers
◼ Frames must be received in the correct order
◼ If a frame is lost, the lost frame and all of the following frames
must be retransmitted
Window Size
◼ For m-bit sequence numbers
◼ Send window size: at most 2m-1
→ Up to 2m-1 frames can be sent without ACK
◼ Receive window size: 1
→ Frames must be received in order
◼ In the followed figures, the send window is an abstract concept
defining an imaginary box of size 2m − 1 with three variables:
Sf, Sn, and Ssize.
◼ The send window can slide one or more slots when a valid
acknowledgment arrives.
◼ The receive window is an abstract concept defining an imaginary
box of size 1 with one single variable Rn.
◼ The window slides when a correct frame has arrived; sliding
occurs one slot at a time.
********** 10 **********
--- page 11 ---
Q6   a.
Describe the working of DNS servers in detail, their labeling of name
CO-4;   [10]
spaces, distribution of name space and resolution.
BL-2
Ans. DNS server 2 Marks
Name Space: 2 Marks
Distribution: 3 Marks
Resolution: 3 Marks
DNS servers
◼ To identify an entity, TCP/IP protocols use the IP address, which
uniquely identifies the connection of a host to the Internet.
◼ However, people prefer to use names instead of numeric
addresses.
◼ Therefore, we need a system that can map a name to an address
or an address to a name.
◼ A user of an e-mail program may know the recipient’s e-mail
address; however, the IP protocol needs the IP address.
◼ The DNS client program requests a DNS server to map the e-
mail address to the corresponding IP address.
Namespace
◼ To be unambiguous, the names assigned to machines must be
carefully selected from a namespace with complete control over
the binding between the names and IP addresses.
********** 11 **********
--- page 12 ---
◼ In other words, the names must be unique because the addresses
are unique.
◼ A name space that maps each address to a unique name can be
organized in two ways: Flat or Hierarchical.
Distribution of Name Space
◼ The information contained in the domain name space must be
stored.
◼ However, it is very inefficient and also unreliable to have just
one computer store such a huge amount of information.
◼   It is inefficient because responding to requests from all over the
world places a heavy load on the system.
◼ It is not reliable because any failure makes the data inaccessible
DNS Resolution
********** 12 **********
--- page 13 ---
CO-1;   b.   Explain various network topologies with its advantages and
[10]
BL-2   disadvantages.
Ans. Each topology with advantages and disadvantages [ 2*4=8 marks]
Diagrams and comparison 2 marks
BUS Topology
•   In a bus network, every device is connected to a single cable that
runs from one end of the network to the other at any instant at
most one machine is the master and is allowed to transmit.
•   All other machines are required to refrain from sending.
• Some mechanism is needed to resolve conflicts when two or
machines want to transmit simultaneously.
• For example : IEEE 802.3, Ethernet.
• Computers on an Ethernet can transmit whenever they want to;
•   If two or more packets collide, each computer just waits a
random
time and tries again later.
Star Topology
•   In this type of topology all the computers are connected to a
single hub through a cable. This hub is the central node and
all others nodes are connected to the central node.
Features of Star Topology
• Every node has its own dedicated connection to the hub.
• Hub acts as a repeater for data flow.
Advantages of Star Topology
•   Fast performance with few nodes and low network traffic.
• Hub can be upgraded easily.
• Easy to troubleshoot.
• Easy to setup and modify.
• Only that node is affected which has failed, rest of the nodes
can work smoothly.
Disadvantages of Star Topology
• Cost of installation is high.
• Expensive to use.
•   If the hub fails then the whole network is stopped because all
the nodes depend on the hub.
• Performance is based on the hub that is it depends on its
capacity
Mesh Topology
•   It is a point-to-point connection to other nodes or devices. All
the network nodes are connected to each other.
• Mesh has n(n-1)/2 physical channels to link n devices.
********** 13 **********
--- page 14 ---
• There are two techniques to transmit data over the Mesh
topology, they are :
1. Routing
2. Flooding
•   In routing, the nodes have a routing logic, as per the network
requirements. Like routing logic to direct the data to reach the
destination using the shortest distance.
•   In flooding, the same data is transmitted to all the network
nodes, hence no routing logic is required.
• The network is robust, and the its very unlikely to lose the data.
But it leads to unwanted load over the network.
Features of Mesh Topology
•   Fully connected.
•   Robust.
• Not flexible.
Advantages of Mesh Topology
• Each connection can carry its own data load.
•   It is robust.
•   Fault is diagnosed easily.
•   Provides security and privacy.
Disadvantages of Mesh Topology
•   Installation and configuration is difficult.
• Cabling cost is more.
• Bulk wiring is required.
Tree Topology
•   It has a root node and all other nodes are connected to it forming
a hierarchy. It is also called hierarchical topology. It should at
least have three levels to the hierarchy.
Features of Tree Topology
•   Ideal if workstations are located in groups.
• Used in Wide Area Network.
Advantages of Tree Topology
•   Extension of bus and star topologies.
• Expansion of nodes is possible and easy.
•   Easily managed and maintained.
********** 14 **********
--- page 15 ---
•   Error detection is easily done.
Disadvantages of Tree Topology
• Heavily cabled.
•   Costly.
•   If more nodes are added maintenance is difficult.
Central hub fails, network fails.
Q7   a.   What is CRC? Consider a message 110010 represented by the
CO-2;   polynomial divisor 1101. Generate the transmitted message and check   [10]
BL-3   whether it is correctly accepted or not.
Ans. CRC definition 2 Marks
Creating transmitted frame: 5 Marks
Receive frame and check for correctness: 3 Marks
CRC is an error-detection technique used in the Data Link Layer to
detect accidental changes in transmitted data.
• The sender treats the data as a binary polynomial.
•   It divides the data (after appending zeros) by a generator
polynomial.
• The remainder (CRC bits) is appended to the data to form the
transmitted frame.
• At the receiver, the same division is performed:
o Remainder = 0 → No error
o Remainder ≠ 0 → Error detected
Given Problem
• Message (Dataword) = 110010
• Generator Polynomial = 1101 (degree = 3)
Step 1: Append Zeros
Append 3 zeros (degree of generator):
110010000110010000110010000
Step 2: Perform Binary Division (Modulo-2)
Divide 110010000 by 1101.
Division Steps (Key XOR Operations)
1100 ⊕ 1101 = 0001 → bring down next bit → 0011
0011 ⊕ 0000 = 0011 → bring down next bit → 0110
0110 ⊕ 0000 = 0110 → bring down next bit → 1100
1100 ⊕ 1101 = 0001 → bring down next bit → 0010
********** 15 **********
--- page 16 ---
0010 ⊕ 0000 = 0010 → bring down next bit → 0100
0100 ⊕ 0000 = 0100
Remainder (CRC bits) = 100
Step 3: Form Transmitted Frame
Step 4: Receiver Side Verification
Now divide the received frame 110010100 by 1101.
• Performing the same division yields:
Remainder=000
Final Conclusion
• Transmitted Frame = 110010100
• Receiver Remainder = 000
Since the remainder is zero, the message is correctly received (no
error detected).
CO-3;   b.   Define switching in computer network. Explain various switching
[10]
BL-2   technique.
Ans. Switching 1 mark
Packet switching 3 marks
Message switching 3 marks
Message switching 3 marks
◼ Switching techniques in computer networks to connect devices
and allow them to communicate with each other.
◼ Additionally, we can utilize switching techniques to transfer data
from one device to another.
◼ Switching allows multiple devices to share the same
communication channel simultaneously.
◼ As a result, it improves the efficiency of the network.
Furthermore, switching also enables the network to route data to
its intended destination.
◼ Additionally, it provides a mechanism for error checking and
correction
********** 16 **********
--- page 17 ---
Packet Switching
◼ Packet switching is a method used to transmit data over a
network.
◼ We divide data into small packets and transmit them over the
network independently.
◼ Each packet contains the data and destination address
information required to route the packet to its destination.
◼ In packet switching, each packet travels separately through the
network and can take different paths to reach its destination.
◼ This approach allows for more efficient use of network resources
because we can transmit multiple packets simultaneously over
the same network.
Message Switching
◼ Message switching is a method of data transmission that was
popular in the early days of networking, before the development
of packet switching. In message switching, we divide a message
into fixed-length blocks or frames.
◼ Furthermore, we transmit each frame independently through the
network. Additionally, each intermediate node stores the frames
until the entire message is received. Finally, the nodes forward
the entire message to its destination.
◼ Unlike packet switching, message switching is a store-and-
forward method of data transmission.
◼ It means that each intermediate node stores the entire message
until it can be forwarded to the next node.
◼ This can result in longer transmission times compared to packet
switching. We can only transmit each message when an
intermediate node receives all the parts of the message.
◼ We mainly use circuit switching in traditional telephone
networks.
Circuit Switching
◼ When two devices want to communicate in a circuit-switched
network, they establish a connection by setting up a dedicated
path between them.
********** 17 **********
--- page 18 ---
◼ This path is reserved exclusively for the duration of the
communication. Hence, no other devices can use it during that
specific time.
◼ Once we establish the connection, we can transfer data between
devices over the dedicated path.
◼ This path typically comprises a series of
interconnected switches or nodes that route the data to its
destination.
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 0d00c7851ac4

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_AIDS_7056/Computer Networks/ANS_Computer Networks(702AI0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper c36eb59663fe

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_AIML_7053/Computer Networks/ANS_Computer Networks(702AI0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper eb85f4d18c7b

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_AI_7012/Computer Networks/ANS_Computer Networks(702AI0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper a86e381378e4

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CSE_DS_7057/Computer Networks/ANS_Computer Networks(702AI0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper a477df0d6d63

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_EXTC_7006/Computer Networks/ANS_Computer Networks(702AI0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper f904b17329e1

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_AI_7051/Computer Networks/ANS_Computer Networks(702AI0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper f712308eea44

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/Integrated_Computer_7032/Computer Networks/ANS_Computer Networks(702AI0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 8c806e27a832

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/Integrated_IT_7037/Computer Networks/ANS_Computer Networks(702AI0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: mixed (26 pages), mean OCR confidence 89.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. TECH (CSE - DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech
Intg. (IT)/B. Tech (IT)/MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (COMPUTER ENGINEERING)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: II / III / IV/Sem 3 Re-exam/Sem 5 Re-exam/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Computer Networks
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 26 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsary. Attempt any 4 out of the remaining questions.
5. All questions carry equal marks.
6. Assume suitable data if necessary.
********** 1 **********
--- page 2 ---
CO, BL,
SO
Q No   Question
CO-1   An organization plans to deploy an online collaboration platform. Apply the concepts
BL-3   of the Client–Server model and the Peer-to-Peer model to explain how each could be
SO-1   Q1 a   implemented in this scenario with respect to performance, scalability, and reliability.
Client–Server Model :
• All user requests pass through a central server.
• Server manages authentication, file storage, version control, and communication.
• Performance: Efficient for small to medium users; may suffer bottlenecks under
heavy load.
•   Scalability: Limited by server capacity; scaling requires costly hardware
upgrades.
•   Reliability: Single point of failure—if the server crashes, the platform is
unavailable.
Peer-to-Peer (P2P) Model :
• Each participant (peer) can directly share resources such as files, messages, or
media.
• Performance: Distributes load across nodes; can handle large-scale access better.
•   Scalability: Increases as more peers join; no central bottleneck.
•   Reliability: More resilient; if some peers fail, others still maintain availability.
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Marking Scheme (5 Marks):
Explains Definition or practical usage (online collaboration) of Client–Server Model
and Peer-to-Peer (P2P) Model- 1 marks
Client–Server Model -Correctly explains implementation, performance, scalability, and
reliability - 2 Marks
Peer-to-Peer (P2P) Model - Correctly explains implementation, performance,
scalability, and reliability- 2 Marks
Soln
CO-1
BL-2   Draw the labelled diagram of TCP/IP reference model and explain the task of all
SO-1   Q1 b   layers
A diagram of TCP/IP model [1 M]
Tasks of each layer   [4 M]
1. Network Access Layer
▪ Manages the hardware aspects of the network, including cables, wireless signals,
Soln   and network interface cards (NICs).
********** 2 **********
--- page 3 ---
▪ Handles the physical addressing (MAC addresses) for local network
communication.
▪ Encapsulates IP packets into frames for transmission and decapsulates them upon
reception.
2. Internet Layer
▪ Provides logical addressing (IP addresses) for unique device identification across
the internet.
▪ Routes packets from a source to a destination by determining the best path across
interconnected networks.
▪ Handles packet fragmentation and reassembly if a packet is too large for the
network media.
3. Transport Layer
▪ Provides end-to-end communication services between applications on different
devices.
▪ Uses TCP (Transmission Control Protocol) for reliable, connection-oriented data
transfer, which includes flow control, sequencing, and error checking.
▪ Uses UDP (User Datagram Protocol) for faster, connectionless transfer where
speed is more important than guaranteed delivery (e.g., video streaming).
4. Application Layer
▪ Provides network services to end-user applications, allowing them to
communicate over the network.
▪   Integrates the functions of the session, presentation, and application layers of the
OSI model.
▪ Handles the formatting, encryption, and other symbolic tasks needed for
application-level communication.
5. Physical Layer
▪ Converts binary data into physical signals (electrical, optical, or radio waves).
▪ Sends the encoded signals over the physical medium, like a cable or Wi-Fi.
▪ Defines and handles specifications for physical network components, such as
cables and connectors.
▪ Uses timing to ensure both the sender and receiver are synchronized at the bit
level.
▪   Specifies the physical layout of the network, such as a bus, ring, or star
configuration.
CO 2
BL-2   In a Pure ALOHA system, the average number of frames generated per frame time is G
SO-1   = 0.5. Calculate the throughput S. What is the maximum possible throughput in Pure
Q1 c   ALOHA?
(2MARKS)
• G is the average number of frames generated by the system during one frame
transmission time. Then it can be proven that the average number of successfully
transmitted frames for pure ALOHA is S = G * e^-2G.
• The maximum throughput Smax is 0.184, for G = 1/2.
•   In other words, if one-half a frame is generated during one frame transmission
time (one frame during two frame transmission times), then 18.4 percent of these
frames reach their destination successfully.
Soln
********** 3 **********
--- page 4 ---
• We expect G = 1/2 to produce the maximum throughput because the vulnerable
time is 2 times the frame transmission time. Therefore, if a station generates only
one frame in this vulnerable time (and no other stations generate a frame during
this time), the frame will reach its destination successfully.
Formula:   (2 MARK)
𝑆=𝐺×𝑒^−2𝐺
Substitution:
S=0.5×e^−2×0.5
=0.5×e−1
=0.5×0.3679
=0.1839
Throughput ≈ 0.184 (18.4%)
(1MARKS)
Maximum throughput for Pure ALOHA occurs at G=0.5, with Smax=0.184
Smax=0.184.
So throughput = 18.4% efficiency.
CO-3
BL-3
SO-2   A block of address is granted to a small organization and one of the address is
193.20.35.40/26. Determine the first address and last address in the block. Determine
Q1 d   the total number of address in the block.
Solution D[1]
First address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32−26=6 rightmost bits to 0, we get
11000001 00010100 00100011 00000000
or
193.20.35.0. which is the first address.
Last address[2 marks]
The binary representation of the given address is
11000001 00010100 00100011 00101000
If we set 32 – 26=6 rightmost bits to 1, we get
11000001 00010100 00100011 00111111
or
193.20.35.63. which is the last address.
Total number of addresses in block[1 mark]
The number of addresses in the block can be found by using the formula
232−n.
The value of n is 26, which means that number
Soln   of addresses is 2 32−26 or 64
********** 4 **********
--- page 5 ---
CO- 2   Consider a message represented by the polynomial M(x)=x5+x4+x.
BL-3   Consider a generating polynomial G(x)=x3+x2+1. Generate a 3 bit CRC and show what
SO-1   Q2 a   will be the transmitted frame. How is error detected by CRC?
Step 1: Represent the polynomials in binary [03 Marks]
The message polynomial is given by
M(x)=x5+x4+
(𝑥)=𝑥5+𝑥4+𝑥. The coefficients are 1, 1, 0, 0, 1, 0.
The binary representation of the message is 110010.
The generator polynomial is
. The coefficients are 1, 1, 0, 1.
G(x)=1x3+1x2+0x1+1x
The binary representation of the generator is 1101.
Step 2: Generate the CRC [04 Marks]
To generate a 3-bit CRC, we must first append 3 zeros to the original message.
This is because the degree of the generator polynomial is 3.
The augmented message is 110010000.
Next, perform modulo-2 binary division of the augmented message by the
generator polynomial's binary string. The remainder of this division is the CRC.
The remainder is the last 3 bits from the division, which is 100. This is the 3-bit
CRC.
Step 3: Show the transmitted frame by [02 Marks]
The transmitted frame is the original message followed by the CRC.
Original message: 110010
CRC: 100
The transmitted frame is 110010111.
The 3-bit CRC is 100. The transmitted frame is 110010100. Error is detected by
dividing the received frame by the generator polynomial and checking if the
remainder is zero. A non-zero remainder indicates an error. [01 Marks]
Soln
CO-3   A university has been allocated an IP block of 172.16.0.0/16 (65,536 addresses) for its
BL-3   internal network. The university needs to divide this block among three departments as
SO-1   follows:
Department A: 32 labs, each requiring 128 addresses
Department B: 64 labs, each requiring 64 addresses
Department C: 16 labs, each requiring 512 addresses
Design the subnet allocations for each department and calculate how many IP addresses
remain unused after the allocation.
Q2 b
********** 5 **********
--- page 6 ---
Given IP Block: 172.16.0.0/16 → Total addresses = 65,536
🔹 Department A: 32 Labs, Each Needs 128 Addresses
• Addresses per lab: 128
• Nearest subnet size: /25 (2⁷ = 128 addresses)
• Number of subnets needed: 32
• Total addresses used: 32 × 128 = 4,096
CIDR Range Example:
•   172.16.0.0/25 → 172.16.0.127
• 172.16.0.128/25 → 172.16.0.255
• … up to 32 subnets
🔹 Department B: 64 Labs, Each Needs 64 Addresses
• Addresses per lab: 64
• Nearest subnet size: /26 (2⁶ = 64 addresses)
• Number of subnets needed: 64
• Total addresses used: 64 × 64 = 4,096
CIDR Range Example:
• 172.16.16.0/26 → 172.16.16.63
• 172.16.16.64/26 → 172.16.16.127
• … up to 64 subnets
🔹 Department C: 16 Labs, Each Needs 512 Addresses
• Addresses per lab: 512
• Nearest subnet size: /23 (2⁹ = 512 addresses)
• Number of subnets needed: 16
• Total addresses used: 16 × 512 = 8,192
CIDR Range Example:
• 172.16.32.0/23 → 172.16.33.255
• 172.16.34.0/23 → 172.16.35.255
• … up to 16 subnets
🔸 Summary of Allocation
Departmen   Subnet   Subnet   Total
Address Range
t   Size   s   Used
A   /25   32   4,096   172.16.0.0 – 172.16.15.255
172.16.16.0 –
B   /26   64   4,096
172.16.31.255
172.16.32.0 –
C   /23   16   8,192
Soln   172.16.63.255
********** 6 **********
--- page 7 ---
🔸 Total Addresses Used= 16,384
🔸 Remaining Addresses = 65536-16384 = 49152
Correct subnet size selection (/25, /26, /23)-   3 marks
Accurate calculation of total addresses used   2 marks
First and last address identification for each department   3 marks
Remaining address calculation and clarity   2 marks
CO-1
BL-1   Define computer networks? Discuss any two types of network topologies in computer
SO-1   Q3 a   network with suitable diagram.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
‘‘Computer network'' to mean a collection of autonomous computers interconnected by a
single technology. Two computers are said to be interconnected if they are able to
exchange information.
Bus Topology
A bus topology is a type of network topology in which all devices (computers, printers,
etc.) are connected to a single central communication line, called a bus or backbone
cable.
How it Works
•   All nodes share the same communication medium (the bus).
• When one device sends a signal, it travels in both directions along the bus.
• Every device checks the signal, and only the intended recipient accepts the data.
• Terminators are placed at both ends of the bus to prevent signal reflection.
Ring Topology
In a ring topology, each device is connected to exactly two other devices, forming a
closed loop or ring. Data travels in one or both directions around the ring until it
Soln   reaches its destination.
********** 7 **********
--- page 8 ---
Advantages
• Easy to install and reconfigure.
• Data flows in an orderly manner (less chance of collision).
• Performs better than bus topology under heavy load.
Disadvantages
• A failure in one device or link can affect the entire network.
•   Difficult to troubleshoot.
• Adding or removing devices disrupts the network.
Star Topology
In a star topology, all devices are connected to a central hub or switch. The hub acts
as a repeater for data flow.
Advantages
• Easy to install and manage.
•   If one cable fails, only that device is affected.
• Easy to detect faults and add new devices.
Disadvantages
•   Failure of the hub/switch can bring down the whole network.
• Requires more cabling than bus topology.
Mesh Topology
In a mesh topology, each device is connected to every other device in the network.
There are two types:
•   Full Mesh: Every device connects to every other device.
********** 8 **********
--- page 9 ---
•   Partial Mesh: Some devices are connected to all, others only to selected ones.
Advantages
• Very reliable — even if one link fails, data can take another path.
• High privacy and security.
•   Ideal for mission-critical applications.
Disadvantages
• Very expensive due to high cabling cost.
• Complex to install and maintain.
Hybrid Topology
A hybrid topology combines two or more different types of topologies (like star + bus,
or star + ring) to form a larger, more flexible network.
Advantages
•   Flexible and scalable.
• Can be designed to meet specific network requirements.
•   Fault isolation is easier.
Disadvantages
• Complex design and expensive.
•   Difficult to configure and maintain.
Computer Network Definition – 1 mark
Explanation of any 2 topology with diagram– 2 marks for each topology
CO-3   Q3 b   Summarize how OSPF determines the best path to a destination network
********** 9 **********
--- page 10 ---
BL-2
SO-1
OSPF (Open Shortest Path First) determines the best path to a destination network by
using the Shortest Path First (SPF) algorithm, also known as Dijkstra’s algorithm.
Each OSPF router collects information about the network’s topology from all other
routers within the same area through Link-State Advertisements (LSAs). This
information is stored in the Link-State Database (LSDB), which represents a complete
map of the network.
OSPF then calculates the shortest or most efficient route to each destination based on
the cost of each link. The cost is typically derived from the bandwidth of the interface
— higher bandwidth links have lower costs.
The path with the lowest total cost (sum of all link costs from source to destination) is
selected as the best path, and this route is added to the router’s routing table.
Summary:
OSPF → Exchanges LSAs → Builds LSDB → Runs SPF (Dijkstra) algorithm →
Chooses path with lowest total cost → Updates routing table.
Soln
CO-5   With the help of a neat diagram, explain the hierarchical structure of the domain
BL-2   namespace in the Domain Name System (DNS) and describe how this structure
SO-1   Q3 c   ensures the uniqueness of domain names across the Internet
The Domain Name System (DNS) organizes all Internet domain names into a
hierarchical namespace, making them easy to manage and ensuring that every domain
name is unique worldwide.
Hierarchical Structure of Domain Namespace explanation (3 marks)
The DNS namespace follows an inverted-tree structure.
Each level in this tree represents a domain, and each node may branch into
subdomains.
Level   Example   Description
The topmost node that references all top-
Root Domain   .
level domains.
Top-Level Domain   Represents major categories or country
.com, .org, .edu, .in
(TLD)   codes.
Second-Level
google.com, mit.edu Owned by organizations or individuals.
Domain
www.google.com,   Identifies specific servers or services within
Subdomain / Host
mail.mit.edu   an organization.
Soln   Diagram: Hierarchical Structure of DNS (4 marks)
********** 10 **********
--- page 11 ---
How the Hierarchical Structure Ensures Uniqueness (3 marks)
1. Distributed Authority:
Each level of the hierarchy controls only its portion of the namespace.
The root controls TLDs; each TLD controls its registered second-level domains.
2. Unique Labels at Each Level:
Domains under the same parent must have different labels (e.g., google.com and
amazon.com cannot both exist under .com).
3. Fully Qualified Domain Name (FQDN):
The combination of labels from the host up to the root creates a globally unique
name
(www.google.com ≠ www.mit.edu).
4. Decentralized Management:
Because authority is divided among many servers, duplication is prevented
while allowing scalability.
CO-3
BL-2
SO-1
Q4 a   Construct the IPv6 packet format and explain the purpose of each field
Soln
********** 11 **********
--- page 12 ---
Each packet is composed of a base header followed by the payload. The base header
occupies 40 bytes, whereas payload can be up to 65,535 bytes of information.
➢ Version. The 4-bit version field defines the version number of the IP. For IPv6,
the value is 6.
➢ Traffic class. The 8-bit traffic class field is used to distinguish different payloads
with different delivery requirements. It replaces the type-of-service field in IPv4.
➢ Flow label. The flow label is a 20-bit field that is designed to provide special
handling for a particular flow of data. We will discuss this field later.
➢ Payload length. The 2-byte payload length field defines the length of the IP
datagram excluding the header. Note that IPv4 defines two fields related to the
length: header length and total length. In IPv6, the length of the base header is
fixed (40 bytes); only the length of the payload needs to be defined.
➢ Next header. The next header is an 8-bit field defining the type of the first
extension header (if present) or the type of the data that follows the base header
in the datagram. This field is similar to the protocol field in IPv4, but we talk
more about it when we discuss the payload.
➢ Hop limit. The 8-bit hop limit field serves the same purpose as the TTL field in
IPv4.
➢ Source and destination addresses. The source address field is a 16-byte (128-bit)
Internet address that identifies the original source of the datagram. The
destination address field is a 16-byte (128-bit) Internet address that identifies the
destination of the datagram.
(Figure of IPV6 packet format-05M & Explanation of each field-05)
CO-4   What is the TCP 3-way handshaking mechanism? Describe the connection
BL-2   establishment, Data Transfer and Connection termination process in detail with the help
SO-1   Q4 b   of diagram?
A connection-oriented transport protocol establishes a virtual path between the source
and destination. All the segments belonging to a message are then sent over this virtual
path. Using a single virtual pathway for the entire message facilitates the
acknowledgment process as well as retransmission of damaged or lost frames. TCP uses
the services of IP to deliver individual segments to the receiver, but it controls the
connection itself. If a segment is lost or corrupted, it is retransmitted. Unlike TCP, IP is
unaware of this retransmission. If a segment arrives out of order, TCP holds it until the
missing segments arrive; IP is unaware of this reordering. In TCP, connection-oriented
transmission requires three phases: connection establishment, data transfer, and
Soln   connection termination.
********** 12 **********
--- page 13 ---
Connection Establishment:

Client ——]

A: ACK flag —|
S: SYN flag _

Active
open

Seq: 8000
Passive

open

seq: 8000

ACK

Y Y

Time Time

1. The client sends the first segment, a SYN segment, in which only the SYN flag is set.
This segment is for synchronization of sequence numbers. It consumes one sequencd
number. When the data transfer starts, the sequence number is incremented by 1. Wd
can say that the SYN segment carries no real data, but we can think ofit as containing
1 imaginary byte.

A SYN segment cannot carry data, but it consumes one sequence number.

2. The server sends the second segment, a SYN + ACK segment, with 2 flag bits set
SYN and ACK. This segment has a dual purpose. It is a SYN segment for commu
nication in the other direction and serves as the acknowledgment for the SYN
segment. It consumes one sequence number.

A SYN + ACK segment cannot carry data,
but does consume one sequence number.

3. The client sends the third segment. This is just an ACK segment. It acknowledge
the receipt of the second segment with the ACK flag and acknowledgment numbe
field. Note that the sequence number in this segment is the same as the one in thd
SYN segment; the ACK segment does not consume any sequence numbers.

An ACK segment, ifcarrying no data, consumes no sequence number.

Data Transfer:

FIR ICR 7] QI HO
--- page 14 ---
After connection is established, bidirectional data transfer can take place. The client and
server can both send data and acknowledgments. The acknowledgment is piggybacked
with the data. The client sends 2000 bytes of data in two segments. The server then sends
2000 bytes in one segment. The client sends one more segment. The first three segments
carry both data and acknowledgment, but the last segment carries only an
acknowledgment because there are no more data to be sent.
Note the values of the sequence and acknowledgment numbers. The data segments sent
by the client have the PSH (push) flag set so that the server TCP knows to deliver data
to the server process as soon as they are received. The segment from the server, on the
other hand, does not set the push flag. Most TCP implementations have the option to set
or not set this flag.
Connection Termination:
********** 14 **********
--- page 15 ---
CO-2   Apply the concept of the Go-Back-N ARQ Sliding Window Protocol for window size =
BL-3   7 and explain its working in real-time transmission scenarios. Illustrate with diagrams
SO-1   and examples how the sender and receiver windows move in the following three cases:
a. Normal transmission (no error)
Q5 a   b. Lost data frame
********** 15 **********
--- page 16 ---
c. Lost acknowledgment (ACK)
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery.
Concept /introduction to Go Back n ARQ) – 1 mark
a. Normal transmission (no error) – explanation with diagram – 2.5 marks
b. Lost data frame – explanation with diagram – 2.5 marks
c. Lost acknowledgment (ACK) – explanation with diagram – 2.5 marks
Analyze how retransmission and window shifting occur in each case to ensure reliable
data delivery. – 1.5 marks
Detailed Solution for Reference: In Go-Back-N ARQ, N is the sender's window size.
For Go-Back-7, which means that the seven frames can be sent at a time before
expecting the acknowledgment from the receiver. If sender have ten frames and the
concept is Go-Back-7, which means that the seven frames can be sent retransmitted
Soln   before expecting the acknowledgment for first frame.
********** 16 **********
--- page 17 ---
In the Go-Back-N Protocol, the sequence numbers are modulo 2”,
where m is the size of the sequence number field in bits. The sequence
numbers range from 0 to 2 power m- 1, For example, if m is 4, the only
sequence numbers are 0 through 15 inclusive,

5; Send wires, 5, Send windew,
first outstaneling frame next frame to send

Lota tats tat sted 7 is to fot |i fis fia):

Frames that can be sent, Frames that
but not received fron upper layer cannot be sent

Frames already Frames sent, but not
acknowledged acknowledged (outstanding)

Send window, sive S)..= 2.1

a. Send window before sliding

ay 3,

ariarish ot 1 ya Tapas fet? | s fo piofu tit iatiatist of |

b, Send window after sliding

The sender window at any time divides the possible sequence numbers
into four regions,

The first region, from the far left to the left wall of the window, defines
the sequence numbers belonging to frames that are already acknowledged,
The sender does not worry about these frames and keeps no copies of them,

The second region, colored in Figure (a), defines the range of sequence
numbers belonging to the frames that are sent and have an unknown status,
The sender needs to wait to find out if these frames have been received or
were lost, We call these outstanding frames.

The third range, white in the figure, defines the range of sequence
numbers for frames that can be sent; however, the corresponding data
packets have not yet been received from the network layer,

Finally, the fourth region defines sequence numbers that cannot be used
until the window slides
The send window is an abstract concept defining an imaginary box of
size 2” — 1 with three variables: 5;, S,, and S.izo. The variable Sf defines
the sequence number of the first (oldest) outstanding frame. The variable Sn
holds the sequence number that will be assigned to the next frame to be sent,
Finally, the variable Ssize defines the size of the window,

Figure (b) shows how a send window can slide one or more slots to the
right when an acknowledgment arrives from the other end, The
acknowledgments in this protocol are cumulative, meaning that more than one
frame can be acknowledged by an ACK frame. In Figure, frames 0, |, and 2 are

FRR ICR] AC OH
--- page 18 ---
Lost Frame: If the frame is lost during transmission and the acknowledgment of a
frame is not received within an agreed-upon time period, then all the frames available
in the current window will be retransmitted. Suppose we have sent the frame no 5, but
we didn't receive the acknowledgment of frame no 1, and the current window is holding
three frames, then these three frames will be retransmitted.
********** 18 **********
--- page 19 ---
Lost Acknowledgement: For example, if the acknowledgement (ACK) for frame 2 is
lost in transit due to an error, the sender’s behavior depends on the timer status. If the
sender receives subsequent acknowledgements before the timer for frame 2 expires, it
advances its sending window accordingly. However, if the timer for frame 2 expires
before any cumulative ACK is received, the sender assumes that frame 2 and all
subsequent frames have been lost. Consequently, it retransmits all frames from 2 to 6,
even though the receiver may have already received them correctly. Upon receiving
these retransmitted frames, the receiver identifies them as duplicates, discards them,
and resends the cumulative acknowledgement (ACK7) to confirm successful receipt of
all the frames.
********** 19 **********
--- page 20 ---
CO-5
BL-2   Explain what the File Transfer Protocol (FTP) is and describe the functions of the
SO-2   Q5 b   control connection and the data connection.
FTP explanation: 2 marks
Control Connection with diagram: 4 marks
Data Connection with diagram: 4 marks
● The control connection remains connected during the entire interactive FTP
session.
● The data connection is opened and then closed for each file transferred. It opens
each time commands that involve transferring files are used, and it closes when
the file is transferred.
● In other words, when a user starts an FTP session, the control connection opens.
While the control connection is open, the data connection can be opened and
closed multiple times if several files are transferred.
Communication over Control Connection
●   It uses the 7-bit ASCII character set . Communication is achieved through
commands and responses.
● This simple method is adequate for the control connection because we send one
command (or response) at a time.
● Each command or response is only one short line, so we need not worry about file
format or file structure.
● Each line is terminated with a two-character (carriage return and line feed) end-
Soln   of-line token.
********** 20 **********
--- page 21 ---
■
Communication over Data Connection
● File transfer occurs over the data connection under the control of the commands
sent over the control connection.
● However, we should remember that file transfer in FTP means one of three things:
● A file is to be copied from the server to the client. This is called retrieving aft/e.
It is done under the supervision of the RETR command.
● A file is to be copied from the client to the server. This is called storing aft/e. It
is done under the supervision of the STOR command.
● A list of directory or file names is to be sent from the server to the client. This is
done under the supervision of the LIST command.
● Note that FTP treats a list of directory or file names as a file. It is sent over the
data connection.
● The client must define the type of file to be transferred, the structure of the data,
and the transmission mode.
● Before sending the file through the data connection, we prepare for transmission
through the control connection.
● The heterogeneity problem is resolved by defining three attributes of
communication: file type, data structure, and transmission mode .
■
● File Type: FTP can transfer one of the following file types across the data
connection: an ASCII file, EBCDIC file, or image file.
● Data Structure : FTP can transfer a file across the data connection by using one
of the following interpretations about the structure of the data: file structure,
record structure, and page structure.
● Transmission Mode: FTP can transfer a file across the data connection by using
one of the following three transmission modes: stream mode, block mode, and
compressed mode.
CO-1
BL-1   How is transmission media classified ? List advantages and disadvantages of
SO-1   Q6 a   optical fiber.
Soln
********** 21 **********
--- page 22 ---
Optical Fiber
Data or information is transmitted as light pulses.Carries more data for longer distances
and much more speed as compare to other media.
Requires more protection.
There are two modes of optical fiber.
Multimode AND Single mode
Multimode is used for short distances whereas single mode is used for longer distances.
Advantages
Optical fiber is not affected by outer noise.
No crosstalk
Fast Speed
Disadvantages
Attenuation is caused by tight bends
Bends causes cracks in the cladding and light rays are
scattered.
Scattering, absorption, dispersion, improper installation
causes fiber losses.
CO-2   A pure ALOHA network transmits 200-bit frames on a shared channel of 200 kbps.
BL-4   What is the throughput if the system (all stations together) produces?
SO-1   a. 1000 frames per second
b. 500 frames per second
Q6 b   c. 250 frames per second
The frame transmission time is 200/200 kbps or 1 ms. – 1M,
Soln   S = G× e−2 G   : formula of throughput 1 M
********** 22 **********
--- page 23 ---
a. If the system creates 1000 frames per second, this is 1 frame per millisecond. The
load is 1. In this case
S = G× e−2 G or S = 0.135 (13.5 percent). This means that the throughput is 1000 ×
0.135 = 135 frames. Only 135 frames out of 1000 will probably survive. 1M
b. If the system creates 500 frames per second, this is
(1/2) frame per millisecond. The load is (1/2).
In this case S = G × e −2G or S = 0.184 (18.4 percent). This means that the throughput is
500 × 0.184 = 92 and that only 92 frames out of 500 will probably survive. Note that
this is the maximum throughput case, percentagewise.1M
c. If the system creates 250 frames per second, this is (1/4)
frame per millisecond. The load is (1/4). In this case
S = G × e −2G or S = 0.152 (15.2 percent). This means
that the throughput is 250 × 0.152 = 38. Only 38
frames out of 250 will probably survive. 1M
CO-4
SO-1
BL-2   Q6 c   Compare UDP, TCP and SCTP with appropriate points (any 8 points).
Each point – 1.25 M; 1.25*8 = 10M
Definition
UDP (User Datagram Protocol): A simple, connectionless, lightweight protocol used for
fast transmission without reliability guarantees.
TCP (Transmission Control Protocol): A connection-oriented protocol that ensures
reliable, ordered, and error-checked delivery of data streams between applications.
SCTP (Stream Control Transmission Protocol): A transport protocol that combines
features of TCP (reliability) and UDP (message-oriented) with advanced features like
multi-streaming and multi-homing.
Performance
UDP: Fastest, lowest overhead.
TCP: Slower due to reliability overhead.
SCTP: Slightly slower than TCP (extra features), but more efficient in multi-stream
environments.
Soln
********** 23 **********
--- page 24 ---
Consider a network topology consisting of nodes A, B, C, D, E, F, and G. The directed
edges between these nodes and their corresponding weights are given in the table
below:
Edge   Distance
A->B   7
A->C   6
A->D   5
B->E   -2
D->C   -2
CO-3   C->B   -2
BL-4   C->E   1
SO-2   E->G   5
D->F   3
F->G   4
Using the Bellman-Ford algorithm:
i.   Determine the shortest path from the source node A to the destination node G.
ii.   Compute the shortest distance from node A to node G.
iii.   Show all intermediate steps of the Bellman-Ford algorithm, including the
relaxation process at each iteration.
iv.   Illustrate the original network topology and the final shortest path with the
corresponding distance values clearly marked on the edges.
Q7 a
Shortest path from A to G:  A  →  D  →  C  →  B  →  E  →  G , Shortest distance d(A,
G)= =5+ (−2)+(−2)+(−2)+5=4
(i)   Shortest Path calculation - 3 marks
(ii)   Computing Shortest Distance - 2 marks
Soln   (iii)   Intermediate Steps - 3marks
********** 24 **********
--- page 25 ---
(iv)   Original network topology (original diagram) - 1mark
final shortest path diagram with the corresponding distance values clearly
marked on the edges - 1 mark
CO-4   Draw a neat diagram and explain the working of the Leaky Bucket Algorithm. Is the
SO-1   Leaky Bucket Algorithm advantageous than the Token Bucket Algorithm? Justify your
BL-2   Q7 b   answer.
Diagram for 3 marks and explanation on working for 5 marks. 2 marks for justification.
Explanation of working based on the following points is expected.
The Leaky Bucket Algorithm works like water leaking from a bucket with a hole at the
bottom:
1. Bucket (Buffer) Capacity:
o The bucket has a fixed size (i.e., a limit on how much data or how many
packets it can hold).
2. Input:
o Data packets arrive at irregular intervals and can be bursty (sometimes
a lot comes at once).
3. Leaking (Output):
o The bucket leaks (sends) data at a constant rate (e.g., 10 packets/sec)
regardless of input rate.
o This ensures a smooth output flow.
4. Overflow Handling:
o   If incoming data arrives faster than it leaks and the bucket is full, the
excess packets are discarded (dropped).
Key Advantages of Token Bucket
1. Allows Bursty Traffic: This is its most significant advantage. In real-world
applications (like TCP/IP traffic), data often arrives in short, rapid bursts. The
Token Bucket can handle these bursts as long as there are sufficient tokens,
Soln   utilizing the available network capacity efficiently.
********** 25 **********
--- page 26 ---
2. Higher Throughput Efficiency: By allowing short bursts, it can better utilize
the available bandwidth without needing to queue or drop packets immediately,
leading to better overall throughput and lower latency for typical internet traffic.
Flexibility: It separates the average rate (token generation rate) from the burst size
(bucket capacity), offering two distinct parameters for fine-tuning traffic control.
********** 26 **********
````

## 2024-25 · Final-Exam · Sem 1 · Answer key · paper 5ae8bc982d6f

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_01/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Computer Networks/ANS_Computer Networks(703AI0C004)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 Nov 2024
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester I(Exam Year: 2024-2025)
Subject: Computer Networks
Date: 27 Nov 2024   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks
7. Answer to each new question to be started on a fresh page
8. Figures in brackets on the right hand side indicate full marks
9. Assume Suitable data if necessary.
Q
Answer Briefly:   [20]
1
Describe and differentiate between LAN, MAN and WAN
Differences Between LAN, MAN, and WAN
Feature   LAN   MAN   WAN
Small (within a   Medium (within a Large (spanning cities,
Geographical
building or   city or metropolitan countries, or
Scope
campus)   area)   continents)
High (100 Mbps Moderate (10 Mbps Variable (1.5 Mbps to
Speed
to 10 Gbps)   to 10 Gbps)   100 Gbps or more)
Managed by telecom
Can be private or
Ownership   Privately owned   providers; services are
leased
a   leased   [5]
High cost due to
Low setup and
Cost   Moderate cost   infrastructure and
maintenance cost
coverage
MPLS, ATM, Frame
Ethernet, Wi-Fi,   Fiber-optic cables,
Technology   Relay, fiber optics,
Token Ring   Ethernet, wireless
satellites
City-wide   Global networks,
Office buildings,
Application   networks, large   enterprise networks,
campuses
institutions   Internet
Office network   The Internet, or a
City's municipal
Example   with PCs and   multinational's
network
printers   network
********** 1 **********
--- page 2 ---
Compare 1-persistent, non-persistent and p-persistent methods.
1. 1-persistent CSMA
Description:
In 1-persistent CSMA, when a node has data to send, it continuously listens to the
channel (carrier sensing) until it is idle (free to transmit).
Once the channel is idle, the node transmits its data immediately with 1 (100%)
probability.
If the channel is busy when the node tries to send, the node waits until the channel
becomes idle, then sends its data.
In case of a collision, the node waits for a random amount of time (backoff) before
trying again.
Characteristics:
Collision Likelihood: High collision probability if multiple nodes are waiting for the
channel to become idle at the same time.
Efficiency: Can lead to frequent collisions, particularly under high traffic, reducing
efficiency.
Delay: Low delay if the channel is idle when the node senses it, but higher under
collision conditions.
Use Case:
Works best in low-traffic networks where the probability of simultaneous transmissions
is low.
2. Non-persistent CSMA
Description:
In Non-persistent CSMA, when a node has data to send, it listens to the channel. If the
channel is busy, the node does not continuously sense the channel.
Instead, the node waits for a random amount of time (without monitoring the channel),
and then checks the channel again.
If the channel is idle when the node checks again, it transmits the data. If the channel is
still busy, the node waits for another random period before retrying.
b   [5]
Characteristics:
Collision Likelihood: Lower collision probability than 1-persistent since nodes do not
continuously sense the channel and avoid creating simultaneous bursts of transmission.
Efficiency: More efficient in high-traffic environments, as it reduces the chances of
multiple nodes transmitting at the same time after a busy period.
Delay: Potentially higher delay, especially under high traffic, because nodes wait for
random intervals before checking the channel again.
Use Case:
Suitable for networks with moderate to heavy traffic, as it reduces the likelihood of
collisions.
3. p-persistent CSMA
Description:
In p-persistent CSMA, the node senses the channel and if it finds the channel idle, it
transmits data with a probability p.
If the node does not transmit in that slot (with probability 1 - p), it waits for the next
time slot and senses the channel again.
This process repeats, with the node transmitting with probability p in each subsequent
time slot as long as the channel remains idle.
If the channel is busy, the node waits for a random backoff time and retries after the
channel is idle again.
Characteristics:
Collision Likelihood: Collisions are reduced as nodes do not transmit immediately
upon detecting an idle channel; instead, they take turns probabilistically.
Efficiency: Balances the trade-off between collision avoidance and delay. The choice
of p determines how aggressive the protocol is: a high p (closer to 1) means more
aggressive transmission, while a low p means a more conservative approach.
Delay: Lower delay than non-persistent but higher than 1-persistent for small p values.
The delay and collision likelihood can be fine-tuned by adjusting p.
Use Case:
********** 2 **********
--- page 3 ---
Works well in slotted systems like slotted ALOHA or wireless systems where time
slots are available. It is useful in networks where a balance between collision
probability and delay is needed
• IP Address: 182.44.82.16
• Subnet Mask: /26 (255.255.255.192)
c   • Network Address: 182.44.82.0 [2.5]   [5]
• Broadcast Address: 182.44.82.63 [2.5]
User Datagram Protocol (UDP): Connectionless transport protocol in the TCP/IP suite.
It provides fast, unreliable data transmission, with no flow control, error recovery, or
acknowledgment. Used in time-sensitive applications like video streaming.
[4 + 1
d   DIAGRAM
]
a Describe OSI Model in detail.   [10]
OSI (Open Systems Interconnection) Model: A 7-layer conceptual model for
networking, defining the functions of each layer:
1. Physical Layer: Transmission of raw data bits over physical media.
2. Data Link Layer: Error detection, MAC addressing, frame
synchronization.
3. Network Layer: Routing, addressing (IP).
4. Transport Layer: End-to-end communication, reliability (TCP/UDP).
5. Session Layer: Managing sessions between applications.
6. Presentation Layer: Data format translation (encryption, compression).
7. Application Layer: User interface (HTTP, FTP, DNS).
b   [10]
Given a network topology, apply Dijkstra algorithm on the following graph and find
the shortest path from the source node ‘A’
********** 3 **********
--- page 4 ---
B   C   D   E   F
A   3   5   9   ∞   ∞
AB   3   5   7   10   ∞
ABC   3   5   7   10   13
ABCD   3   5   7   9   9
ABCDEF
A   0   A-A
B   3   A-B
C   5   A-C
D   7   A-B-D
E   9   A-B-D-E
F   9   A-B-D-F
Q
3
Explain IPv4 packet format in detail. [8 +2]
IPv4 Packet Format: Composed of fields such as:
• Version: IPv4 or IPv6.
• Header Length: Length of the header in 32-bit words.
• Type of Service: Priority and quality of service.
• Total Length: Total packet size (header + data).
a   [10]
•   Identification: Used in fragmentation.
• Flags and Fragment Offset: Controls packet fragmentation.
• TTL (Time to Live): Limits packet lifespan.
• Protocol: Specifies the higher-layer protocol (TCP, UDP).
• Source/Destination IP Address: Addressing.
• Header Checksum: Error-checking for the header.
********** 4 **********
--- page 5 ---
Explain the sequence of messages exchanged between a client and a server during the
3-way handshake process.
The 3-way handshake establishes a TCP connection:
1. SYN: Client sends a SYN (synchronize) request to the server.
2. SYN-ACK: Server acknowledges the SYN with a SYN-ACK.
3. ACK: Client sends an ACK to confirm the connection.
b   [10]
********** 5 **********
--- page 6 ---
Q
4
a Define switching. Compare between datagram switching and circuit switching.   [10]
Switching: Process of forwarding packets across a network.
• Circuit Switching: Dedicated path for the entire duration of
communication.
• Datagram Switching: Packets take independent paths, each routed
individually.
Explain Distance vector routing Algorithm. What leads to ‘count-to-infinity’ problem?
• Distance Vector Routing: Routers share routing tables periodically with
neighbors. [ 6MARKS]
b   •   Count-to-Infinity: A routing loop problem where routers continuously   [10]
increase the metric (hop count) to an unreachable destination. [4
MARKS]
Q
5
a Given a data bit sequence 1101011011, and the generator polynomial x3+x+1, calculate   [10]
the CRC code that will be appended to the data sequence for error detection. Also,
demonstrate how the receiver would detect an error using the CRC code. Show all steps
involved in both the sender and receiver processes
Redundant bits: 100
Codeword : 1101011011100
SENDER SIDE : 6 MARKS
RECEIVER SIDE: 4 MARKS
Explain the working of leaky bucket and token bucket in traffic shaping with the help
of suitable diagram.
b • Leaky Bucket: Controls traffic by outputting at a constant rate.   [10]
• Token Bucket: Allows burst traffic by accumulating tokens, which are used
to send data.
********** 6 **********
--- page 7 ---
Q
6
a   Illustrate the working of Go-Back N ARQ with the following scenarios   [10]
1) Frame 1 is sent and acknowledged [2]
2) Frame 3 is lost [4]
3) Acknowledgment 5 is lost [4]
Go-Back-N ARQ: A sliding window protocol for reliable transmission. The sender can
send multiple frames, but must retransmit from the lost frame in case of errors (e.g.,
lost frame or acknowledgment).
Explain the advantages and disadvantages of different types of guided media.
Guided Media: Includes twisted pair, coaxial cables, and fiber optics.
• Twisted Pair: Low cost, but susceptible to interference.
b   [10]
• Coaxial Cable: Better shielding, but more expensive.
• Fiber Optic: High speed, long distance, but costly.
Q
7
Explain HTTP and DNS protocol.
• HTTP (Hypertext Transfer Protocol): Communication protocol used by
a   [10]
web browsers to retrieve content from servers.
• DNS (Domain Name System): Translates domain names to IP addresses.
A slotted ALOHA network transmits 300bit frames using a shared channel with a 200
kbps bandwidth. Find the throughput if the system produces 500 frames per second.
• Frame size = 300 bits
• Bandwidth = 200 kbps (200,000 bits per second)
• Frame production rate = 500 frames per second
Step 1: Calculate the time required to transmit one frame
To find the time taken to transmit one frame, we divide the frame size by the
bandwidth:
Time to transmit one frame=Frame sizeBandwidth=300 bits200,000 bits per sec
ond milliseconds}=1.5 milliseconds
b   [5]
Step 2: Calculate the channel utilization
The slotted ALOHA system allows transmission during discrete time slots,
where each time slot is the time it takes to send one frame.
To calculate the offered load GGG, we need to know how many frames are
generated relative to the number of slots available. Given that 500 frames are
produced per second, and each time slot is 1.5 ms, we can calculate G
G = 500*1.5/1000 = 0.75
Step 3: Calculate the throughput
********** 7 **********
--- page 8 ---
The throughput of slotted ALOHA is maximized when:
S=G×e−GS = G \times e^{-G}S=G×e−G
Substituting G=0.75G = 0.75G=0.75:
Step 4: Convert throughput to bits per second
Now, we calculate the throughput in bits per second by multiplying the frames
per time slot by the frame size and the number of frames per second:
Throughput=0.354×300×500=53,100 bits per second{Throughput} = 0.354
\times 300 \times 500 = 53,100 { bits per
second}Throughput=0.354×300×500=53,100 bits per second
Thus, the throughput of the slotted ALOHA network is approximately 53.1 kbps
Write a short note on Address Resolution Protocol.
• Resolves IP addresses to MAC addresses in a local area network.
c   [5]
********** 8 **********
````

## 2024-25 · Re-Exam · Sem 1 · Answer key · paper c64d19d37490

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_01/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Computer Networks/ANS_Computer Networks(703AI0C004)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 Feb 2025
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 1 Re-exam(Exam Year: 2024-2025)
Subject: Computer Networks
Date: 15 Feb 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Question No. 1 is compulsory.
4. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted.
6. All questions carry equal marks
7. Answer to each new question to be started on a fresh page
8. Figures in brackets on the right hand side indicate full marks
9. Assume Suitable data if necessary.
Q1   Answer Briefly:   [20]
Define Network topology. Draw diagram to illustrate star and mesh topology and
explain it with suitable diagram, advantages and disadvantages.
Network Topology: The arrangement of different elements (links, nodes, etc.) in a
computer network.
Star Topology:
All nodes connect to a central hub.
a   [2.5+2.5]
Advantages: Easy to install, centralized management, scalable.
Disadvantages: Hub failure brings down the network, more cabling required.
Mesh Topology:
Each node connects to every other node.
Advantages: High fault tolerance, data can be transmitted simultaneously.
Disadvantages: Expensive and complex cabling.
b   A pure ALOHA network transmits 200-bit frames using a shared channel with a 200-
kbps bandwidth. Find the throughput if the system produces 250 frames per second
[2+3]
ANSWER: G = 1.25, S= 0.28.
c   Describe the following IPv4 Header fields (also mention the field size)
1. Fragmentation Offset
2. HLEN
[2.5+2.5]
Fragmentation Offset (13 bits): Indicates where a fragmented packet fits in relation
to the original unfragmented packet.
HLEN (4 bits): Header Length, specifies the length of the header in 32-bit words.
Describe 6 control bits of TCP protocol
d   URG, PSH, SYN, ACK, FIN, RST   [5]
********** 1 **********
--- page 2 ---
URG: Urgent pointer field is significant.
PSH: Push data to the receiving application.
SYN: Synchronize sequence numbers during connection setup.
ACK: Acknowledgment field is significant.
FIN: Finish, no more data from the sender.
RST: Reset the connection.
Q2
a   Compare OSI and TCP/IP Model.
OSI Model: 7 layers – Physical, Data Link, Network, Transport, Session, Presentation,
Application.
TCP/IP Model: 4 layers – Network Interface, Internet, Transport, Application.
Comparison:
•   OSI is theoretical; TCP/IP is practical.   [10]
•   OSI distinguishes between presentation and session layers, while TCP/IP
merges these into the application layer.
•   OSI provides clear guidelines for protocol development; TCP/IP is simpler and
more standardized for the internet.
b   Given a network topology, apply Dijkstra algorithm on the following graph and find
the shortest path from the source node ‘0’
[10]
0   0   0-0
1   3   0-1
2   8   0-1-2
3   10   0-1-8-3
4   18   0-1-8-3-4
5   10   0-1-8-2-5
6   9   0-7-6
7   7   0-7
8   7   0-1-8
Q3
An ISP is assigned a block of addresses starting with 192.168.0.0/16 (65,536
addresses). The ISP needs to allocate these addresses to two groups of customers as
a   [5+5]
follows:
********** 2 **********
--- page 3 ---
a. The first group has 200 customers; each customer needs 128 addresses.
b. The second group has 100 customers; each customer needs 256 addresses.
Design the sub-blocks and calculate how many addresses remain unallocated after
these distributions.
Address block: 192.168.0.0/16 (65,536 addresses).
Group 1: 200 customers, 128 addresses each. Needs 200 * 128 = 25,600 addresses
(192.168.0.0/17).
Group 2: 100 customers, 256 addresses each. Needs 100 * 256 = 25,600 addresses
(192.168.128.0/18).
Remaining: 14,336 addresses unallocated.
Compare and contrast the two transport layer protocols, TCP & UDP
b   [10]
Q4
a   Explain Virtual circuit switching in detail. List the phases involved in Virtual Circuit
Switching. Describe how data is transferred in a Virtual Circuit Switching network
and how it differs from Datagram Packet Switching.
Phases: [6]
1. Call setup
2. Data transfer
3. Call teardown   [10]
Data transfer: Packets follow the established path, maintaining order.
Comparison with Datagram Switching: [4]
•   Virtual Circuit is connection-oriented, with a predefined route.
• Datagram Packet Switching sends each packet independently, possibly taking
different routes.
Explain how the Link State Routing Algorithm operates and describe its key
b   components.   [10]
[2 marks each]
********** 3 **********
--- page 4 ---
1. discover neighbors
2. calculate delay
3. form LSP
4. FLOOD LSP
5. DIJKSTRA
Q5
a   Given a data bit sequence 1101011011 and the generator polynomial x 4+x+1,
calculate the Cyclic Redundancy Check (CRC) code that will be appended to the data
sequence for error detection. Demonstrate the steps involved in both the sender
and receiver processes, and explain how the receiver would detect an error using
the CRC code.
[10]
SENDER END [6 MARKS]
RECEIVER END [4 MARKS]
REDUNDANT BITS: 1110
CODEWORD: 11010110111110
Explain open loop and closed loop congestion control in transport layer [5 MARKS
EACH]
b   [10]
Q6
a   Illustrate the working of Selective Repeat ARQ with the following scenarios
1) Frame 1 is sent and acknowledged [2 MARKS]
2) Frame 3 is lost [4 MARKS]
[10]
3) Acknowledgment 5 is lost [4 MARKS]
Explain the advantages and disadvantages of different types of Unguided media.
Types: Radio, Microwave, Infrared
Advantages:
b   [10]
•   Wireless communication, broad coverage.
Disadvantages:
•   Susceptible to interference, security issues.
********** 4 **********
--- page 5 ---
Q7
Explain SMTP AND FTP protocols.
SMTP: Used for sending emails, operates over TCP, port 25. It forwards emails
a   [5+5]
between servers.
FTP: File Transfer Protocol, uses separate control and data connections, operates
over TCP.
Explain the working principle of CSMA/CD.
CSMA/CD: Carrier Sense Multiple Access with Collision Detection. Nodes listen to
the channel, send data if free, and detect collisions to resend.
Flow diagram (3 marks)
b   [05]
Write a short note on RARP and DHCP.
RARP: Reverse Address Resolution Protocol, maps MAC addresses to IP addresses.
c.   [05]
DHCP: Dynamic Host Configuration Protocol, dynamically assigns IP addresses to
hosts in a network.
********** 5 **********
````
