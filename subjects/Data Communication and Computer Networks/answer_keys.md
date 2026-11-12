# Data Communication and Computer Networks: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 13151166fa54

- Departments: Computer Engineering
- Programmes: DIPLOMA IN COMPUTER ENGINEERING - 7073
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN COMPUTER ENGINEERING - 7073/Data Communication and Computer Networks/ANS_Data Communication and Computer Networks(701EX0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Data Communication and Computer Networks
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO1;   a   Define Bandwidth and Latency with an example of each   [5]
SO-1;
BL-1
Bandwidth explanation with example -- 3M
Latency explanation with example -- 2M
Bandwidth in Hertz : It is the range of frequencies contained in a composite
signal or the range of frequencies a channel can pass.
For ex, BW of a subscriber telephone line is 4 kHz
Bandwidth in Bits per Seconds :
It is the number of bits per second that a channel, a link or even a network can
transmit.
Ex: BW of fast Ethernet network (or the links in this network) is a maximum
of 100 Mbps. This means that the network can send 100 Mbps.
The latency or delay defines how long it takes for an entire message to
completely arrive at the destination from the first bit is sent out from the
source. Latency is made of four components.
Latency means whenever we give input to the system and the total time period
it takes to give output so that particular time period/interval is known as
latency.
Latency is the in-between handling time of computers, the signal or data
follows the proper traceroute for reaching its final destination.
********** 1 **********
--- page 2 ---
Ping checks the value of latency by just sending 4 packets of data to the
address provided by the user to check the ping and then calculates the total
time when the response comes to it, that total time is called latency.
CO-2 ;   b   Discuss physical address and logical address in computer networks. Explain   [5]
SO-1;   their roles and differences with a suitable example.
BL-2
A physical address (also called MAC address) is assigned at the data link
layer (Layer 2) and is used for communication within a local network (LAN).
It identifies the actual hardware device on the local network.
Key Characteristics:
Hardcoded into the network interface card (NIC)
Usually permanent (though can be spoofed)
48-bit hexadecimal format
Example: 00:1A:2B:3C:4D:5E
A logical address is assigned at the network layer (Layer 3) and is used for
end-to-end communication across different networks.
It identifies which network and which device within that network should
receive the data.
Key Characteristics:
Assigned by software (manually or via DHCP)
Can change depending on the network
Used for routing packets over the internet
Example: 192.168.1.10
CO-4;   c   Explain the function of ARP (Address Resolution Protocol) in the network   [5]
SO-1 ;   layer with a labeled diagram.
BL-2
********** 2 **********
--- page 3 ---
CO-5 ;   d   Explain the IEEE 802.11 (Wi-Fi) protocol stack physical and data link layer.   [5]
SO-1 ;
BL-2
Wi-Fi technology is governed by the IEEE 802.11 standard, which primarily
focuses on the bottom two layers of the OSI model:
Physical Layer (PHY): Responsible for the actual transmission of data bits
over radio waves. It handles frequency (2.4GHz or 5GHz), modulation
techniques (like OFDM), and data rates.
Data Link Layer: This is split into two sub-layers:
Logical Link Control (LLC): Manages addressing and error checking.
Media Access Control (MAC): This is the "brain" of Wi-Fi. It uses CSMA/CA
(Carrier Sense Multiple Access with Collision Avoidance) to manage how
devices share the airwaves to prevent data collisions.
Q2   a   Describe all types of guided and unguided media. Mention one application of   [10]
CO-3;   each of the media.
SO-1;
BL-2   Explanation of 3 guided media --- 3M
Application of 3 guided media   --- 2M
Explanation of 3 unguided media --- 3M
Application of 3 unguided media   --- 2M
Twisted-pair cable:
It consists of two independently insulated wires twisted around one another.
The use of two wires twisted together helps to reduce crosstalk
and electromagnetic induction
Co-axial cable:
It has 2 conductors separated by dielectric material. The centre and outer
conductor(e.g. shield) are configured to form concentric cylinders with
common axis and hence the name.
Fiber optic cable :
The working principle of optical fiber is the transmission of the information in
the form of light atoms or photons.
The cores of the fiberglass & the cladding have a special refractive index to
twist inward light at a particular angle.
********** 3 **********
--- page 4 ---
Radio waves are used for multicast communications, such as radio, television,
and paging systems.
Microwaves are used for unicast communication such as cellular telephones,
satellite networks,
and wireless LANs.
Infrared signals can be used for short-range communication in a closed area.
Q2   b   Discuss in detail the three-way handshaking process in connection   [10]
CO-4;
SO-1;   establishment, data transfer and connection termination in TCP with labelled
BL-2   diagram for connection establishment process.
Three-Way Handshaking
Explanation --- 7M
Diagram   ----- 3M
The connection establishment in TCP is called three way handshaking.
The process starts with the server. The server program tells its TCP that it is
ready to accept a connection. This is called a request for a passive open.
Although the server TCP is ready to accept any connection from any machine
in the world, it cannot make the connection itself.
The client program issues a request for an active open. A client that wishes to
connect to an open server tells its TCP that it needs to be connected to that
particular server.
********** 4 **********
--- page 5 ---
Q3   a   [10]
CO-1;
SO-1;
BL-2   Compare analog and digital communication (any 10 suitable points)
ANALOG COMMUNICATION   DIGITAL COMMUNICATION
Analog communication uses analog signal   Digital communication uses digital signal whose
whose amplitude varies continuously with   amplitude is of two levels either Low i.e., 0 or either
time from 0 to 100.   High i.e., 1.
1
It gets affected by noise highly during
It gets affected by noise less during transmission
transmission through communication
through communication channel.
channel.
2
Only limited number of channels can be   It can broadcast large number of channels
broadcasted simultaneously.   simultaneously.
3
Error Probability is high.   Error Probability is low.
4
Noise immunity is poor.   Noise immunity is good.
5
Coding is possible and different coding techniques can
Coding is not possible.
6   be used to detect and correct errors.
********** 5 **********
--- page 6 ---
ANALOG COMMUNICATION   DIGITAL COMMUNICATION
Separating out noise and signal in analog   Separating out noise and signal in digital
7   communication is not possible.   communication is possible.
Have complex hardware and less flexible.   Have less complex hardware and more flexible.
8
Frequency division multiplexing (FDM) is Time division multiplexing (TDM) is used for
used for multiplexing   multiplexing
10   Cost efficient   Costly
It requires low bandwidth.   It requires high bandwidth.
11
12   Power consumption is high.   Power consumption is low.
Q3   b What is encryption? Explain the basic principles of cryptography.   [10]
CO-5;
SO-1;   Differentiate between symmetric encryption and asymmetric encryption with
BL-1, 2   examples.
Encryption ---- 2M
Principles --- 3M
Difference ---- 6M
Encryption is the process of converting plain text (readable data) into cipher
text (unreadable data) using an algorithm and a key, so that unauthorized users
cannot access the information. The original data can be recovered only by
using the correct decryption key.
Basic Principles of Cryptography
Cryptography is used to secure communication and protect data. It is based on
the following four basic principles:
(i) Confidentiality
Ensures that information is accessible only to authorized users.
Achieved using encryption.
Example: Encrypted email messages.
(ii) Integrity
Ensures that data is not altered during transmission.
Achieved using hash functions and message authentication codes (MAC).
Example: If a file is modified, the hash value changes.
(iii) Authentication
Ensures that the sender and receiver are genuine.
Achieved using digital signatures and certificates.
Example: OTP verification, digital certificates.
(iv) Non-Repudiation
Ensures that the sender cannot deny sending the message.
********** 6 **********
--- page 7 ---
Achieved using digital signatures.
Example: Online transactions using digital signatures.
Q4   a A bit stream 1001011011 is transmitted using the standard CRC   [10]
CO-3;   method. The generator polynomial is 𝑥4+x+1. Solve for finding the codeword.
SO-1;
BL-3
Given :
Augmented data=10010110110000   ---- 2M
Modulo-2 Division (XOR Division)
Divide 10010110110000 by 10011.
********** 7 **********
--- page 8 ---
------ 6M
Final Remainder and Codeword
After processing all bits, the remaining 4 bits are the CRC.
• Remainder: 0001
• Original Message: 1001011011
• Final Codeword: 10010110110001   ----- 2M
Q4   b   Discuss Software Defined Network (SDN) Controller and construct its   [10]
CO-5;   architecture diagram.
SO-1;
BL- 2, 3
Definition -- 2M
Figure   -- 3M
Explanation of each layer/plane --- 5M
Definition:
Software-Defined Networking (SDN) is an advanced networking paradigm
that transforms traditional network design by separating the control plane
from the data plane. This separation allows centralized control,
programmability, and dynamic network management, making SDN highly
suitable for modern applications such as cloud computing, IoT, and 5G
networks.
********** 8 **********
--- page 9 ---
The SDN architecture is divided into three main layers (planes):
Application Plane
Control Plane
Data Plane (Infrastructure Layer)
These layers communicate through well-defined interfaces:
Northbound Interfaces (NBI)
Southbound Interfaces (SBI)
Q5   a   [10]
CO-4;
SO-1;   Discuss Class A, Class B and Class C addressing with the range of each class
BL-2   address in decimal format. Explain the concept of subnetting and supernetting.
Classful IP Addressing
Class A Addressing
• Used for very large networks.
•   First octet represents network ID.
• Remaining three octets represent host ID.
• Supports millions of hosts per network.
Format:
| Network | Host | Host | Host |
Example: 10.0.0.1
Network = 10
Host = 0.0.1
********** 9 **********
--- page 10 ---
Class B Addressing
• Used for medium-sized networks.
•   First two octets → Network ID
•   Last two octets → Host ID
Format:
| Network | Network | Host | Host |
Example:
172.16.0.1
Network = 172.16
Host = 0.1
Class C Addressing
• Used for small networks.
•   First three octets → Network ID
•   Last octet → Host ID
Format:
| Network | Network | Network | Host |
Example: 192.168.1.1
Network = 192.168.1
Host = 1   ---- 6M
Subnetting
Subnetting is the process of dividing one large network into multiple smaller
networks (subnets) by borrowing bits from the host portion.
Class C default mask:
192.168.1.0 → 255.255.255.0
If we borrow 2 bits:
New mask = 255.255.255.192 (/26)
Subnets = 2^2 = 4
Hosts per subnet = 2^6 − 2 = 62
Formula:
Number of subnets = 2^n
Number of hosts = 2^h − 2
Where:
• n = number of borrowed bits
• h = number of host bits
Supernetting
Supernetting is the process of combining multiple smaller networks into one larger
network. It is also called CIDR (Classless Inter-Domain Routing).
Example:
Combine 4 Class C networks:
192.168.0.0
192.168.1.0
192.168.2.0
192.168.3.0
Supernet:192.168.0.0/22
Mask = 255.255.252.0   ---- 4M
********** 10 **********
--- page 11 ---
Q5   b   [10]
CO-5;
SO-1;   Explain the concept of Internet of Things (IoT) with examples and describe its
BL-2   basic architecture with diagram.
Concept   --- 2M
Examples --- 2M
Diagram   ---- 2M
Architecture ---- 4M
Concept - IoT connects physical objects to the internet so that they can sense,
communicate, and make decisions.
Examples of IoT:
Smart home (smart lights, smart fans, smart AC)
Smart health monitoring systems
Smart agriculture (soil moisture sensors)
Smart cities (traffic control systems)
Industrial automation
Basic Architecture –
IoT architecture is generally divided into three layers:
Perception Layer
Network Layer
Application Layer
(a) Perception Layer (Sensor Layer)
Function: This is the physical layer that interacts with the environment.
Responsibilities:
Collect data using sensors, Identify objects, Measure physical parameters
like:
Temperature, Humidity, Pressure, Motion, Light, Sound
Devices used:
********** 11 **********
--- page 12 ---
Sensors, RFID tags, Cameras, Actuators, GPS
Example: Temperature sensor in smart agriculture.
(b) Network Layer (Transport Layer)
Function: Transfers the data collected by the perception layer to the
application layer through networks.
Responsibilities:
Data transmission, Device connectivity, Routing, Communication between
devices and cloud
Technologies used:
Wi-Fi, Bluetooth, ZigBee, 4G/5G, Ethernet, LoRaWAN
Example: Sensor data sent to cloud server via Wi-Fi.
(c) Application Layer
Function: Provides services to the user based on the data received from the
network layer.
Responsibilities:
Data processing, Data analysis, Decision making, User interface, Automation
control
Q6   a   [10]
CO-2;
SO-1;   Describe the Open Systems Interconnection (OSI) model by drawing its
BL-2   layered architecture and explaining the role and responsibilities of each layer.
Detailed explanation of each layer – 8M
Figure – 2 M
Q6   b   [10]
CO-3;
SO-1;   Explain the process of Carrier Sense Multiple Access with Collision
BL-2   Avoidance (CSMA/CA) with neat diagram
Explanation ---- 6M
Diagram   ---- 4M
********** 12 **********
--- page 13 ---
⚫ We need to avoid collisions on wireless networks because they cannot
be detected.
⚫ Carrier sense multiple access with collision avoidance (CSMAlCA) was
invented for this network.
⚫ Collisions are avoided through the use of CSMA/CA's three strategies:
the interframe space, the contention window, and acknowledgments
⚫ When a frame is ready, the transmitting station checks whether the
channel is idle or busy.
⚫ If the channel is busy, the station waits until the channel becomes idle.
⚫ If the channel is idle, the station waits for an Inter-frame space (IFS)
amount of time.
⚫ If after the IFS time the channel is still idle, the station can send, but it
still needs to wait a time equal to the contention time.
⚫ The contention window is an amount of time divided into slots. A
station that is ready to send chooses a random number of slots as its
wait time. The number of slots in the window changes according to the
binary exponential back-off strategy. Here the station needs to sense
the channel after each time slot for sending a frame.
⚫ After sending the frame, it sets a timer.
⚫ The station then waits for acknowledgement from the receiver. If it
receives the acknowledgement before expiry of timer, it marks a
successful transmission.
Otherwise, it waits for a back-off time period and restarts.
Q7   a   [5]
CO-4;
SO-1;   What is queuing in User Datagram Protocol (UDP). Explain any two
BL-1,2   applications of UDP.
Queuing   --- 3M
Appln (any 2) --- 2M
Queuing
• In UDP, queues are associated with ports.
• At the client site, when a process starts, it requests a port number from
the operating system.
• Even if a process wants to communicate with multiple processes, it
obtains only one port number and eventually one outgoing and one
incoming queue.
• The queues function as long as the process is running.
• When the process terminates, the queues are destroyed
Applns
********** 13 **********
--- page 14 ---
• UDP is suitable for a process with internal flow and error control
mechanisms.
• For example, the Trivial File Transfer Protocol (TFTP) process
includes flow and error control. It can easily use UDP.
• UDP is a suitable transport protocol for multicasting.
•   Multicasting capability is embedded in the UDP software but not in the
TCP software.
• UDP is used for management processes such as SNMP (Simple
Network Management Protocol).
• UDP is used for some route updating protocols such as Routing
Information Protocol (RIP)
Q7   b   [5]
CO-1;
SO-1;   Explain simplex, half duplex and duplex communication system with an
BL-2   example of each.
Explanation of each - 3M
Example of each - 2M
Examples -
Simplex – Radio, TV
Half duplex – walkie talkie
Full duplex – mobile phone
Q7   c   [10]
CO-5;
SO-1;   Explain Cloud Networking. Provide examples of Cloud Networking Services.
BL-2,3   Identify and discuss any three use cases of Cloud Networking Services.
Cloud Networking --- 2M
Services   ---- 2M
Use cases (any 3) ----- 6M
Cloud networking is the use of cloud-based services and infrastructure to
manage, control, and deliver networking resources such as routers, switches,
firewalls, load balancers, and virtual networks over the internet. Instead of
relying on physical hardware, cloud networking uses virtualized network
********** 14 **********
--- page 15 ---
resources hosted in data centers and managed through cloud service providers
like AWS, Microsoft Azure, and Google Cloud.
Cloud networking allows organizations to create and manage networks
without installing physical networking devices, enabling remote access,
scalability, and centralized control.
Examples of Cloud Networking Services
Some major cloud providers and their networking services are:
These platforms provide virtual networking infrastructure such as IP
addressing, routing, DNS, load balancing, and security services.
Use – Cases
Case 1: Web Application Hosting
Cloud networking is used to host websites and web applications. Load
balancers distribute user requests across multiple servers, and DNS services
map domain names to IP addresses. This ensures high availability and
scalability for websites such as e-commerce platforms and online services.
Example: Hosting an e-commerce website using cloud servers and load
balancing.
Case 2: Data Storage and Backup
Organizations use cloud networking to store data in cloud storage and access
it over the internet. Cloud networking ensures secure data transfer between
users and cloud storage. It is also used for backup and disaster recovery.
Example: Google Drive, OneDrive, Dropbox use cloud networking for file
storage and sharing.
Case 3: Virtual Private Network (VPN)
Cloud networking provides VPN services to securely connect remote users or
branch offices to the company’s cloud network. Employees can securely
access company resources from remote locations.
Example: A company connecting its branch offices using Cloud VPN.
Case 4 (Optional): IoT Applications
Cloud networking connects IoT devices to cloud servers where data is stored,
processed, and analyzed.
Example: Smart home systems, smart city traffic monitoring systems.
********** 15 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper ef5a0817d533

- Departments: Computer Science
- Programmes: DIPLOMA IN COMPUTER SCIENCE AND ENGINEE
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN COMPUTER SCIENCE AND ENGINEE_04f07abf/Data Communication and Computer Networks/ANS_Data Communication and Computer Networks(701EX0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Data Communication and Computer Networks
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO1;   a   Define Bandwidth and Latency with an example of each   [5]
SO-1;
BL-1
Bandwidth explanation with example -- 3M
Latency explanation with example -- 2M
Bandwidth in Hertz : It is the range of frequencies contained in a composite
signal or the range of frequencies a channel can pass.
For ex, BW of a subscriber telephone line is 4 kHz
Bandwidth in Bits per Seconds :
It is the number of bits per second that a channel, a link or even a network can
transmit.
Ex: BW of fast Ethernet network (or the links in this network) is a maximum
of 100 Mbps. This means that the network can send 100 Mbps.
The latency or delay defines how long it takes for an entire message to
completely arrive at the destination from the first bit is sent out from the
source. Latency is made of four components.
Latency means whenever we give input to the system and the total time period
it takes to give output so that particular time period/interval is known as
latency.
Latency is the in-between handling time of computers, the signal or data
follows the proper traceroute for reaching its final destination.
********** 1 **********
--- page 2 ---
Ping checks the value of latency by just sending 4 packets of data to the
address provided by the user to check the ping and then calculates the total
time when the response comes to it, that total time is called latency.
CO-2 ;   b   Discuss physical address and logical address in computer networks. Explain   [5]
SO-1;   their roles and differences with a suitable example.
BL-2
A physical address (also called MAC address) is assigned at the data link
layer (Layer 2) and is used for communication within a local network (LAN).
It identifies the actual hardware device on the local network.
Key Characteristics:
Hardcoded into the network interface card (NIC)
Usually permanent (though can be spoofed)
48-bit hexadecimal format
Example: 00:1A:2B:3C:4D:5E
A logical address is assigned at the network layer (Layer 3) and is used for
end-to-end communication across different networks.
It identifies which network and which device within that network should
receive the data.
Key Characteristics:
Assigned by software (manually or via DHCP)
Can change depending on the network
Used for routing packets over the internet
Example: 192.168.1.10
CO-4;   c   Explain the function of ARP (Address Resolution Protocol) in the network   [5]
SO-1 ;   layer with a labeled diagram.
BL-2
********** 2 **********
--- page 3 ---
CO-5 ;   d   Explain the IEEE 802.11 (Wi-Fi) protocol stack physical and data link layer.   [5]
SO-1 ;
BL-2
Wi-Fi technology is governed by the IEEE 802.11 standard, which primarily
focuses on the bottom two layers of the OSI model:
Physical Layer (PHY): Responsible for the actual transmission of data bits
over radio waves. It handles frequency (2.4GHz or 5GHz), modulation
techniques (like OFDM), and data rates.
Data Link Layer: This is split into two sub-layers:
Logical Link Control (LLC): Manages addressing and error checking.
Media Access Control (MAC): This is the "brain" of Wi-Fi. It uses CSMA/CA
(Carrier Sense Multiple Access with Collision Avoidance) to manage how
devices share the airwaves to prevent data collisions.
Q2   a   Describe all types of guided and unguided media. Mention one application of   [10]
CO-3;   each of the media.
SO-1;
BL-2   Explanation of 3 guided media --- 3M
Application of 3 guided media   --- 2M
Explanation of 3 unguided media --- 3M
Application of 3 unguided media   --- 2M
Twisted-pair cable:
It consists of two independently insulated wires twisted around one another.
The use of two wires twisted together helps to reduce crosstalk
and electromagnetic induction
Co-axial cable:
It has 2 conductors separated by dielectric material. The centre and outer
conductor(e.g. shield) are configured to form concentric cylinders with
common axis and hence the name.
Fiber optic cable :
The working principle of optical fiber is the transmission of the information in
the form of light atoms or photons.
The cores of the fiberglass & the cladding have a special refractive index to
twist inward light at a particular angle.
********** 3 **********
--- page 4 ---
Radio waves are used for multicast communications, such as radio, television,
and paging systems.
Microwaves are used for unicast communication such as cellular telephones,
satellite networks,
and wireless LANs.
Infrared signals can be used for short-range communication in a closed area.
Q2   b   Discuss in detail the three-way handshaking process in connection   [10]
CO-4;
SO-1;   establishment, data transfer and connection termination in TCP with labelled
BL-2   diagram for connection establishment process.
Three-Way Handshaking
Explanation --- 7M
Diagram   ----- 3M
The connection establishment in TCP is called three way handshaking.
The process starts with the server. The server program tells its TCP that it is
ready to accept a connection. This is called a request for a passive open.
Although the server TCP is ready to accept any connection from any machine
in the world, it cannot make the connection itself.
The client program issues a request for an active open. A client that wishes to
connect to an open server tells its TCP that it needs to be connected to that
particular server.
********** 4 **********
--- page 5 ---
Q3   a   [10]
CO-1;
SO-1;
BL-2   Compare analog and digital communication (any 10 suitable points)
ANALOG COMMUNICATION   DIGITAL COMMUNICATION
Analog communication uses analog signal   Digital communication uses digital signal whose
whose amplitude varies continuously with   amplitude is of two levels either Low i.e., 0 or either
time from 0 to 100.   High i.e., 1.
1
It gets affected by noise highly during
It gets affected by noise less during transmission
transmission through communication
through communication channel.
channel.
2
Only limited number of channels can be   It can broadcast large number of channels
broadcasted simultaneously.   simultaneously.
3
Error Probability is high.   Error Probability is low.
4
Noise immunity is poor.   Noise immunity is good.
5
Coding is possible and different coding techniques can
Coding is not possible.
6   be used to detect and correct errors.
********** 5 **********
--- page 6 ---
ANALOG COMMUNICATION   DIGITAL COMMUNICATION
Separating out noise and signal in analog   Separating out noise and signal in digital
7   communication is not possible.   communication is possible.
Have complex hardware and less flexible.   Have less complex hardware and more flexible.
8
Frequency division multiplexing (FDM) is Time division multiplexing (TDM) is used for
used for multiplexing   multiplexing
10   Cost efficient   Costly
It requires low bandwidth.   It requires high bandwidth.
11
12   Power consumption is high.   Power consumption is low.
Q3   b What is encryption? Explain the basic principles of cryptography.   [10]
CO-5;
SO-1;   Differentiate between symmetric encryption and asymmetric encryption with
BL-1, 2   examples.
Encryption ---- 2M
Principles --- 3M
Difference ---- 6M
Encryption is the process of converting plain text (readable data) into cipher
text (unreadable data) using an algorithm and a key, so that unauthorized users
cannot access the information. The original data can be recovered only by
using the correct decryption key.
Basic Principles of Cryptography
Cryptography is used to secure communication and protect data. It is based on
the following four basic principles:
(i) Confidentiality
Ensures that information is accessible only to authorized users.
Achieved using encryption.
Example: Encrypted email messages.
(ii) Integrity
Ensures that data is not altered during transmission.
Achieved using hash functions and message authentication codes (MAC).
Example: If a file is modified, the hash value changes.
(iii) Authentication
Ensures that the sender and receiver are genuine.
Achieved using digital signatures and certificates.
Example: OTP verification, digital certificates.
(iv) Non-Repudiation
Ensures that the sender cannot deny sending the message.
********** 6 **********
--- page 7 ---
Achieved using digital signatures.
Example: Online transactions using digital signatures.
Q4   a A bit stream 1001011011 is transmitted using the standard CRC   [10]
CO-3;   method. The generator polynomial is 𝑥4+x+1. Solve for finding the codeword.
SO-1;
BL-3
Given :
Augmented data=10010110110000   ---- 2M
Modulo-2 Division (XOR Division)
Divide 10010110110000 by 10011.
********** 7 **********
--- page 8 ---
------ 6M
Final Remainder and Codeword
After processing all bits, the remaining 4 bits are the CRC.
• Remainder: 0001
• Original Message: 1001011011
• Final Codeword: 10010110110001   ----- 2M
Q4   b   Discuss Software Defined Network (SDN) Controller and construct its   [10]
CO-5;   architecture diagram.
SO-1;
BL- 2, 3
Definition -- 2M
Figure   -- 3M
Explanation of each layer/plane --- 5M
Definition:
Software-Defined Networking (SDN) is an advanced networking paradigm
that transforms traditional network design by separating the control plane
from the data plane. This separation allows centralized control,
programmability, and dynamic network management, making SDN highly
suitable for modern applications such as cloud computing, IoT, and 5G
networks.
********** 8 **********
--- page 9 ---
The SDN architecture is divided into three main layers (planes):
Application Plane
Control Plane
Data Plane (Infrastructure Layer)
These layers communicate through well-defined interfaces:
Northbound Interfaces (NBI)
Southbound Interfaces (SBI)
Q5   a   [10]
CO-4;
SO-1;   Discuss Class A, Class B and Class C addressing with the range of each class
BL-2   address in decimal format. Explain the concept of subnetting and supernetting.
Classful IP Addressing
Class A Addressing
• Used for very large networks.
•   First octet represents network ID.
• Remaining three octets represent host ID.
• Supports millions of hosts per network.
Format:
| Network | Host | Host | Host |
Example: 10.0.0.1
Network = 10
Host = 0.0.1
********** 9 **********
--- page 10 ---
Class B Addressing
• Used for medium-sized networks.
•   First two octets → Network ID
•   Last two octets → Host ID
Format:
| Network | Network | Host | Host |
Example:
172.16.0.1
Network = 172.16
Host = 0.1
Class C Addressing
• Used for small networks.
•   First three octets → Network ID
•   Last octet → Host ID
Format:
| Network | Network | Network | Host |
Example: 192.168.1.1
Network = 192.168.1
Host = 1   ---- 6M
Subnetting
Subnetting is the process of dividing one large network into multiple smaller
networks (subnets) by borrowing bits from the host portion.
Class C default mask:
192.168.1.0 → 255.255.255.0
If we borrow 2 bits:
New mask = 255.255.255.192 (/26)
Subnets = 2^2 = 4
Hosts per subnet = 2^6 − 2 = 62
Formula:
Number of subnets = 2^n
Number of hosts = 2^h − 2
Where:
• n = number of borrowed bits
• h = number of host bits
Supernetting
Supernetting is the process of combining multiple smaller networks into one larger
network. It is also called CIDR (Classless Inter-Domain Routing).
Example:
Combine 4 Class C networks:
192.168.0.0
192.168.1.0
192.168.2.0
192.168.3.0
Supernet:192.168.0.0/22
Mask = 255.255.252.0   ---- 4M
********** 10 **********
--- page 11 ---
Q5   b   [10]
CO-5;
SO-1;   Explain the concept of Internet of Things (IoT) with examples and describe its
BL-2   basic architecture with diagram.
Concept   --- 2M
Examples --- 2M
Diagram   ---- 2M
Architecture ---- 4M
Concept - IoT connects physical objects to the internet so that they can sense,
communicate, and make decisions.
Examples of IoT:
Smart home (smart lights, smart fans, smart AC)
Smart health monitoring systems
Smart agriculture (soil moisture sensors)
Smart cities (traffic control systems)
Industrial automation
Basic Architecture –
IoT architecture is generally divided into three layers:
Perception Layer
Network Layer
Application Layer
(a) Perception Layer (Sensor Layer)
Function: This is the physical layer that interacts with the environment.
Responsibilities:
Collect data using sensors, Identify objects, Measure physical parameters
like:
Temperature, Humidity, Pressure, Motion, Light, Sound
Devices used:
********** 11 **********
--- page 12 ---
Sensors, RFID tags, Cameras, Actuators, GPS
Example: Temperature sensor in smart agriculture.
(b) Network Layer (Transport Layer)
Function: Transfers the data collected by the perception layer to the
application layer through networks.
Responsibilities:
Data transmission, Device connectivity, Routing, Communication between
devices and cloud
Technologies used:
Wi-Fi, Bluetooth, ZigBee, 4G/5G, Ethernet, LoRaWAN
Example: Sensor data sent to cloud server via Wi-Fi.
(c) Application Layer
Function: Provides services to the user based on the data received from the
network layer.
Responsibilities:
Data processing, Data analysis, Decision making, User interface, Automation
control
Q6   a   [10]
CO-2;
SO-1;   Describe the Open Systems Interconnection (OSI) model by drawing its
BL-2   layered architecture and explaining the role and responsibilities of each layer.
Detailed explanation of each layer – 8M
Figure – 2 M
Q6   b   [10]
CO-3;
SO-1;   Explain the process of Carrier Sense Multiple Access with Collision
BL-2   Avoidance (CSMA/CA) with neat diagram
Explanation ---- 6M
Diagram   ---- 4M
********** 12 **********
--- page 13 ---
⚫ We need to avoid collisions on wireless networks because they cannot
be detected.
⚫ Carrier sense multiple access with collision avoidance (CSMAlCA) was
invented for this network.
⚫ Collisions are avoided through the use of CSMA/CA's three strategies:
the interframe space, the contention window, and acknowledgments
⚫ When a frame is ready, the transmitting station checks whether the
channel is idle or busy.
⚫ If the channel is busy, the station waits until the channel becomes idle.
⚫ If the channel is idle, the station waits for an Inter-frame space (IFS)
amount of time.
⚫ If after the IFS time the channel is still idle, the station can send, but it
still needs to wait a time equal to the contention time.
⚫ The contention window is an amount of time divided into slots. A
station that is ready to send chooses a random number of slots as its
wait time. The number of slots in the window changes according to the
binary exponential back-off strategy. Here the station needs to sense
the channel after each time slot for sending a frame.
⚫ After sending the frame, it sets a timer.
⚫ The station then waits for acknowledgement from the receiver. If it
receives the acknowledgement before expiry of timer, it marks a
successful transmission.
Otherwise, it waits for a back-off time period and restarts.
Q7   a   [5]
CO-4;
SO-1;   What is queuing in User Datagram Protocol (UDP). Explain any two
BL-1,2   applications of UDP.
Queuing   --- 3M
Appln (any 2) --- 2M
Queuing
• In UDP, queues are associated with ports.
• At the client site, when a process starts, it requests a port number from
the operating system.
• Even if a process wants to communicate with multiple processes, it
obtains only one port number and eventually one outgoing and one
incoming queue.
• The queues function as long as the process is running.
• When the process terminates, the queues are destroyed
Applns
********** 13 **********
--- page 14 ---
• UDP is suitable for a process with internal flow and error control
mechanisms.
• For example, the Trivial File Transfer Protocol (TFTP) process
includes flow and error control. It can easily use UDP.
• UDP is a suitable transport protocol for multicasting.
•   Multicasting capability is embedded in the UDP software but not in the
TCP software.
• UDP is used for management processes such as SNMP (Simple
Network Management Protocol).
• UDP is used for some route updating protocols such as Routing
Information Protocol (RIP)
Q7   b   [5]
CO-1;
SO-1;   Explain simplex, half duplex and duplex communication system with an
BL-2   example of each.
Explanation of each - 3M
Example of each - 2M
Examples -
Simplex – Radio, TV
Half duplex – walkie talkie
Full duplex – mobile phone
Q7   c   [10]
CO-5;
SO-1;   Explain Cloud Networking. Provide examples of Cloud Networking Services.
BL-2,3   Identify and discuss any three use cases of Cloud Networking Services.
Cloud Networking --- 2M
Services   ---- 2M
Use cases (any 3) ----- 6M
Cloud networking is the use of cloud-based services and infrastructure to
manage, control, and deliver networking resources such as routers, switches,
firewalls, load balancers, and virtual networks over the internet. Instead of
relying on physical hardware, cloud networking uses virtualized network
********** 14 **********
--- page 15 ---
resources hosted in data centers and managed through cloud service providers
like AWS, Microsoft Azure, and Google Cloud.
Cloud networking allows organizations to create and manage networks
without installing physical networking devices, enabling remote access,
scalability, and centralized control.
Examples of Cloud Networking Services
Some major cloud providers and their networking services are:
These platforms provide virtual networking infrastructure such as IP
addressing, routing, DNS, load balancing, and security services.
Use – Cases
Case 1: Web Application Hosting
Cloud networking is used to host websites and web applications. Load
balancers distribute user requests across multiple servers, and DNS services
map domain names to IP addresses. This ensures high availability and
scalability for websites such as e-commerce platforms and online services.
Example: Hosting an e-commerce website using cloud servers and load
balancing.
Case 2: Data Storage and Backup
Organizations use cloud networking to store data in cloud storage and access
it over the internet. Cloud networking ensures secure data transfer between
users and cloud storage. It is also used for backup and disaster recovery.
Example: Google Drive, OneDrive, Dropbox use cloud networking for file
storage and sharing.
Case 3: Virtual Private Network (VPN)
Cloud networking provides VPN services to securely connect remote users or
branch offices to the company’s cloud network. Employees can securely
access company resources from remote locations.
Example: A company connecting its branch offices using Cloud VPN.
Case 4 (Optional): IoT Applications
Cloud networking connects IoT devices to cloud servers where data is stored,
processed, and analyzed.
Example: Smart home systems, smart city traffic monitoring systems.
********** 15 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 9a641989784c

- Departments: Information Technology
- Programmes: DIPLOMA IN INFORMATION TECHNOLOGY - 7075
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/DIPLOMA IN INFORMATION TECHNOLOGY - 7075/Data Communication and Computer Networks/ANS_Data Communication and Computer Networks(701EX0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: Diploma (COMP)/Diploma (CSE)/Diploma (IT)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Data Communication and Computer Networks
Date: 09 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO1;   a   Define Bandwidth and Latency with an example of each   [5]
SO-1;
BL-1
Bandwidth explanation with example -- 3M
Latency explanation with example -- 2M
Bandwidth in Hertz : It is the range of frequencies contained in a composite
signal or the range of frequencies a channel can pass.
For ex, BW of a subscriber telephone line is 4 kHz
Bandwidth in Bits per Seconds :
It is the number of bits per second that a channel, a link or even a network can
transmit.
Ex: BW of fast Ethernet network (or the links in this network) is a maximum
of 100 Mbps. This means that the network can send 100 Mbps.
The latency or delay defines how long it takes for an entire message to
completely arrive at the destination from the first bit is sent out from the
source. Latency is made of four components.
Latency means whenever we give input to the system and the total time period
it takes to give output so that particular time period/interval is known as
latency.
Latency is the in-between handling time of computers, the signal or data
follows the proper traceroute for reaching its final destination.
********** 1 **********
--- page 2 ---
Ping checks the value of latency by just sending 4 packets of data to the
address provided by the user to check the ping and then calculates the total
time when the response comes to it, that total time is called latency.
CO-2 ;   b   Discuss physical address and logical address in computer networks. Explain   [5]
SO-1;   their roles and differences with a suitable example.
BL-2
A physical address (also called MAC address) is assigned at the data link
layer (Layer 2) and is used for communication within a local network (LAN).
It identifies the actual hardware device on the local network.
Key Characteristics:
Hardcoded into the network interface card (NIC)
Usually permanent (though can be spoofed)
48-bit hexadecimal format
Example: 00:1A:2B:3C:4D:5E
A logical address is assigned at the network layer (Layer 3) and is used for
end-to-end communication across different networks.
It identifies which network and which device within that network should
receive the data.
Key Characteristics:
Assigned by software (manually or via DHCP)
Can change depending on the network
Used for routing packets over the internet
Example: 192.168.1.10
CO-4;   c   Explain the function of ARP (Address Resolution Protocol) in the network   [5]
SO-1 ;   layer with a labeled diagram.
BL-2
********** 2 **********
--- page 3 ---
CO-5 ;   d   Explain the IEEE 802.11 (Wi-Fi) protocol stack physical and data link layer.   [5]
SO-1 ;
BL-2
Wi-Fi technology is governed by the IEEE 802.11 standard, which primarily
focuses on the bottom two layers of the OSI model:
Physical Layer (PHY): Responsible for the actual transmission of data bits
over radio waves. It handles frequency (2.4GHz or 5GHz), modulation
techniques (like OFDM), and data rates.
Data Link Layer: This is split into two sub-layers:
Logical Link Control (LLC): Manages addressing and error checking.
Media Access Control (MAC): This is the "brain" of Wi-Fi. It uses CSMA/CA
(Carrier Sense Multiple Access with Collision Avoidance) to manage how
devices share the airwaves to prevent data collisions.
Q2   a   Describe all types of guided and unguided media. Mention one application of   [10]
CO-3;   each of the media.
SO-1;
BL-2   Explanation of 3 guided media --- 3M
Application of 3 guided media   --- 2M
Explanation of 3 unguided media --- 3M
Application of 3 unguided media   --- 2M
Twisted-pair cable:
It consists of two independently insulated wires twisted around one another.
The use of two wires twisted together helps to reduce crosstalk
and electromagnetic induction
Co-axial cable:
It has 2 conductors separated by dielectric material. The centre and outer
conductor(e.g. shield) are configured to form concentric cylinders with
common axis and hence the name.
Fiber optic cable :
The working principle of optical fiber is the transmission of the information in
the form of light atoms or photons.
The cores of the fiberglass & the cladding have a special refractive index to
twist inward light at a particular angle.
********** 3 **********
--- page 4 ---
Radio waves are used for multicast communications, such as radio, television,
and paging systems.
Microwaves are used for unicast communication such as cellular telephones,
satellite networks,
and wireless LANs.
Infrared signals can be used for short-range communication in a closed area.
Q2   b   Discuss in detail the three-way handshaking process in connection   [10]
CO-4;
SO-1;   establishment, data transfer and connection termination in TCP with labelled
BL-2   diagram for connection establishment process.
Three-Way Handshaking
Explanation --- 7M
Diagram   ----- 3M
The connection establishment in TCP is called three way handshaking.
The process starts with the server. The server program tells its TCP that it is
ready to accept a connection. This is called a request for a passive open.
Although the server TCP is ready to accept any connection from any machine
in the world, it cannot make the connection itself.
The client program issues a request for an active open. A client that wishes to
connect to an open server tells its TCP that it needs to be connected to that
particular server.
********** 4 **********
--- page 5 ---
Q3   a   [10]
CO-1;
SO-1;
BL-2   Compare analog and digital communication (any 10 suitable points)
ANALOG COMMUNICATION   DIGITAL COMMUNICATION
Analog communication uses analog signal   Digital communication uses digital signal whose
whose amplitude varies continuously with   amplitude is of two levels either Low i.e., 0 or either
time from 0 to 100.   High i.e., 1.
1
It gets affected by noise highly during
It gets affected by noise less during transmission
transmission through communication
through communication channel.
channel.
2
Only limited number of channels can be   It can broadcast large number of channels
broadcasted simultaneously.   simultaneously.
3
Error Probability is high.   Error Probability is low.
4
Noise immunity is poor.   Noise immunity is good.
5
Coding is possible and different coding techniques can
Coding is not possible.
6   be used to detect and correct errors.
********** 5 **********
--- page 6 ---
ANALOG COMMUNICATION   DIGITAL COMMUNICATION
Separating out noise and signal in analog   Separating out noise and signal in digital
7   communication is not possible.   communication is possible.
Have complex hardware and less flexible.   Have less complex hardware and more flexible.
8
Frequency division multiplexing (FDM) is Time division multiplexing (TDM) is used for
used for multiplexing   multiplexing
10   Cost efficient   Costly
It requires low bandwidth.   It requires high bandwidth.
11
12   Power consumption is high.   Power consumption is low.
Q3   b What is encryption? Explain the basic principles of cryptography.   [10]
CO-5;
SO-1;   Differentiate between symmetric encryption and asymmetric encryption with
BL-1, 2   examples.
Encryption ---- 2M
Principles --- 3M
Difference ---- 6M
Encryption is the process of converting plain text (readable data) into cipher
text (unreadable data) using an algorithm and a key, so that unauthorized users
cannot access the information. The original data can be recovered only by
using the correct decryption key.
Basic Principles of Cryptography
Cryptography is used to secure communication and protect data. It is based on
the following four basic principles:
(i) Confidentiality
Ensures that information is accessible only to authorized users.
Achieved using encryption.
Example: Encrypted email messages.
(ii) Integrity
Ensures that data is not altered during transmission.
Achieved using hash functions and message authentication codes (MAC).
Example: If a file is modified, the hash value changes.
(iii) Authentication
Ensures that the sender and receiver are genuine.
Achieved using digital signatures and certificates.
Example: OTP verification, digital certificates.
(iv) Non-Repudiation
Ensures that the sender cannot deny sending the message.
********** 6 **********
--- page 7 ---
Achieved using digital signatures.
Example: Online transactions using digital signatures.
Q4   a A bit stream 1001011011 is transmitted using the standard CRC   [10]
CO-3;   method. The generator polynomial is 𝑥4+x+1. Solve for finding the codeword.
SO-1;
BL-3
Given :
Augmented data=10010110110000   ---- 2M
Modulo-2 Division (XOR Division)
Divide 10010110110000 by 10011.
********** 7 **********
--- page 8 ---
------ 6M
Final Remainder and Codeword
After processing all bits, the remaining 4 bits are the CRC.
• Remainder: 0001
• Original Message: 1001011011
• Final Codeword: 10010110110001   ----- 2M
Q4   b   Discuss Software Defined Network (SDN) Controller and construct its   [10]
CO-5;   architecture diagram.
SO-1;
BL- 2, 3
Definition -- 2M
Figure   -- 3M
Explanation of each layer/plane --- 5M
Definition:
Software-Defined Networking (SDN) is an advanced networking paradigm
that transforms traditional network design by separating the control plane
from the data plane. This separation allows centralized control,
programmability, and dynamic network management, making SDN highly
suitable for modern applications such as cloud computing, IoT, and 5G
networks.
********** 8 **********
--- page 9 ---
The SDN architecture is divided into three main layers (planes):
Application Plane
Control Plane
Data Plane (Infrastructure Layer)
These layers communicate through well-defined interfaces:
Northbound Interfaces (NBI)
Southbound Interfaces (SBI)
Q5   a   [10]
CO-4;
SO-1;   Discuss Class A, Class B and Class C addressing with the range of each class
BL-2   address in decimal format. Explain the concept of subnetting and supernetting.
Classful IP Addressing
Class A Addressing
• Used for very large networks.
•   First octet represents network ID.
• Remaining three octets represent host ID.
• Supports millions of hosts per network.
Format:
| Network | Host | Host | Host |
Example: 10.0.0.1
Network = 10
Host = 0.0.1
********** 9 **********
--- page 10 ---
Class B Addressing
• Used for medium-sized networks.
•   First two octets → Network ID
•   Last two octets → Host ID
Format:
| Network | Network | Host | Host |
Example:
172.16.0.1
Network = 172.16
Host = 0.1
Class C Addressing
• Used for small networks.
•   First three octets → Network ID
•   Last octet → Host ID
Format:
| Network | Network | Network | Host |
Example: 192.168.1.1
Network = 192.168.1
Host = 1   ---- 6M
Subnetting
Subnetting is the process of dividing one large network into multiple smaller
networks (subnets) by borrowing bits from the host portion.
Class C default mask:
192.168.1.0 → 255.255.255.0
If we borrow 2 bits:
New mask = 255.255.255.192 (/26)
Subnets = 2^2 = 4
Hosts per subnet = 2^6 − 2 = 62
Formula:
Number of subnets = 2^n
Number of hosts = 2^h − 2
Where:
• n = number of borrowed bits
• h = number of host bits
Supernetting
Supernetting is the process of combining multiple smaller networks into one larger
network. It is also called CIDR (Classless Inter-Domain Routing).
Example:
Combine 4 Class C networks:
192.168.0.0
192.168.1.0
192.168.2.0
192.168.3.0
Supernet:192.168.0.0/22
Mask = 255.255.252.0   ---- 4M
********** 10 **********
--- page 11 ---
Q5   b   [10]
CO-5;
SO-1;   Explain the concept of Internet of Things (IoT) with examples and describe its
BL-2   basic architecture with diagram.
Concept   --- 2M
Examples --- 2M
Diagram   ---- 2M
Architecture ---- 4M
Concept - IoT connects physical objects to the internet so that they can sense,
communicate, and make decisions.
Examples of IoT:
Smart home (smart lights, smart fans, smart AC)
Smart health monitoring systems
Smart agriculture (soil moisture sensors)
Smart cities (traffic control systems)
Industrial automation
Basic Architecture –
IoT architecture is generally divided into three layers:
Perception Layer
Network Layer
Application Layer
(a) Perception Layer (Sensor Layer)
Function: This is the physical layer that interacts with the environment.
Responsibilities:
Collect data using sensors, Identify objects, Measure physical parameters
like:
Temperature, Humidity, Pressure, Motion, Light, Sound
Devices used:
********** 11 **********
--- page 12 ---
Sensors, RFID tags, Cameras, Actuators, GPS
Example: Temperature sensor in smart agriculture.
(b) Network Layer (Transport Layer)
Function: Transfers the data collected by the perception layer to the
application layer through networks.
Responsibilities:
Data transmission, Device connectivity, Routing, Communication between
devices and cloud
Technologies used:
Wi-Fi, Bluetooth, ZigBee, 4G/5G, Ethernet, LoRaWAN
Example: Sensor data sent to cloud server via Wi-Fi.
(c) Application Layer
Function: Provides services to the user based on the data received from the
network layer.
Responsibilities:
Data processing, Data analysis, Decision making, User interface, Automation
control
Q6   a   [10]
CO-2;
SO-1;   Describe the Open Systems Interconnection (OSI) model by drawing its
BL-2   layered architecture and explaining the role and responsibilities of each layer.
Detailed explanation of each layer – 8M
Figure – 2 M
Q6   b   [10]
CO-3;
SO-1;   Explain the process of Carrier Sense Multiple Access with Collision
BL-2   Avoidance (CSMA/CA) with neat diagram
Explanation ---- 6M
Diagram   ---- 4M
********** 12 **********
--- page 13 ---
⚫ We need to avoid collisions on wireless networks because they cannot
be detected.
⚫ Carrier sense multiple access with collision avoidance (CSMAlCA) was
invented for this network.
⚫ Collisions are avoided through the use of CSMA/CA's three strategies:
the interframe space, the contention window, and acknowledgments
⚫ When a frame is ready, the transmitting station checks whether the
channel is idle or busy.
⚫ If the channel is busy, the station waits until the channel becomes idle.
⚫ If the channel is idle, the station waits for an Inter-frame space (IFS)
amount of time.
⚫ If after the IFS time the channel is still idle, the station can send, but it
still needs to wait a time equal to the contention time.
⚫ The contention window is an amount of time divided into slots. A
station that is ready to send chooses a random number of slots as its
wait time. The number of slots in the window changes according to the
binary exponential back-off strategy. Here the station needs to sense
the channel after each time slot for sending a frame.
⚫ After sending the frame, it sets a timer.
⚫ The station then waits for acknowledgement from the receiver. If it
receives the acknowledgement before expiry of timer, it marks a
successful transmission.
Otherwise, it waits for a back-off time period and restarts.
Q7   a   [5]
CO-4;
SO-1;   What is queuing in User Datagram Protocol (UDP). Explain any two
BL-1,2   applications of UDP.
Queuing   --- 3M
Appln (any 2) --- 2M
Queuing
• In UDP, queues are associated with ports.
• At the client site, when a process starts, it requests a port number from
the operating system.
• Even if a process wants to communicate with multiple processes, it
obtains only one port number and eventually one outgoing and one
incoming queue.
• The queues function as long as the process is running.
• When the process terminates, the queues are destroyed
Applns
********** 13 **********
--- page 14 ---
• UDP is suitable for a process with internal flow and error control
mechanisms.
• For example, the Trivial File Transfer Protocol (TFTP) process
includes flow and error control. It can easily use UDP.
• UDP is a suitable transport protocol for multicasting.
•   Multicasting capability is embedded in the UDP software but not in the
TCP software.
• UDP is used for management processes such as SNMP (Simple
Network Management Protocol).
• UDP is used for some route updating protocols such as Routing
Information Protocol (RIP)
Q7   b   [5]
CO-1;
SO-1;   Explain simplex, half duplex and duplex communication system with an
BL-2   example of each.
Explanation of each - 3M
Example of each - 2M
Examples -
Simplex – Radio, TV
Half duplex – walkie talkie
Full duplex – mobile phone
Q7   c   [10]
CO-5;
SO-1;   Explain Cloud Networking. Provide examples of Cloud Networking Services.
BL-2,3   Identify and discuss any three use cases of Cloud Networking Services.
Cloud Networking --- 2M
Services   ---- 2M
Use cases (any 3) ----- 6M
Cloud networking is the use of cloud-based services and infrastructure to
manage, control, and deliver networking resources such as routers, switches,
firewalls, load balancers, and virtual networks over the internet. Instead of
relying on physical hardware, cloud networking uses virtualized network
********** 14 **********
--- page 15 ---
resources hosted in data centers and managed through cloud service providers
like AWS, Microsoft Azure, and Google Cloud.
Cloud networking allows organizations to create and manage networks
without installing physical networking devices, enabling remote access,
scalability, and centralized control.
Examples of Cloud Networking Services
Some major cloud providers and their networking services are:
These platforms provide virtual networking infrastructure such as IP
addressing, routing, DNS, load balancing, and security services.
Use – Cases
Case 1: Web Application Hosting
Cloud networking is used to host websites and web applications. Load
balancers distribute user requests across multiple servers, and DNS services
map domain names to IP addresses. This ensures high availability and
scalability for websites such as e-commerce platforms and online services.
Example: Hosting an e-commerce website using cloud servers and load
balancing.
Case 2: Data Storage and Backup
Organizations use cloud networking to store data in cloud storage and access
it over the internet. Cloud networking ensures secure data transfer between
users and cloud storage. It is also used for backup and disaster recovery.
Example: Google Drive, OneDrive, Dropbox use cloud networking for file
storage and sharing.
Case 3: Virtual Private Network (VPN)
Cloud networking provides VPN services to securely connect remote users or
branch offices to the company’s cloud network. Employees can securely
access company resources from remote locations.
Example: A company connecting its branch offices using Cloud VPN.
Case 4 (Optional): IoT Applications
Cloud networking connects IoT devices to cloud servers where data is stored,
processed, and analyzed.
Example: Smart home systems, smart city traffic monitoring systems.
********** 15 **********
````
