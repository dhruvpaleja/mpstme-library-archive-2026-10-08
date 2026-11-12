# Introduction to Data Communication and Networks: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 675ce8eabef3

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/Integrated_IT_7037/Introduction to Data Communication and Networks/ANS_Introduction to Data Communication and Networks(701IT0C004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2025
- Text: ocr (12 pages), mean OCR confidence 90.7

````text
SYNOPTICS

SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Semester V(Exam Year: 2025-2026)
Subject: Introduction to Data Communication and Networks
Date: 28 Nov 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.

Ql Answer briefly:

CO-1; a. | Explain full-duplex communication mode. Give a suitable example and discuss its | [5]
SO-2 ; advantages and disadvantages.

BL-1 «Answer: Full-Duplex Mode: In full-duplex mode, both stations can

transmit and receive simultaneously.

¢ — Full-duplex mode is used when communication in both directions is
required all the time.

* The capacity of the channel, however, must be divided between the two
directions.

* Example: Telephone Network in which there is communication between
two persons by a telephone line, through which both can talk and listen
at the same time.

* Advantages of Full-Duplex Mode: Full-duplex mode allows for
simultaneous bidirectional communication, which is ideal for real-time
applications such as video conferencing or online gaming.

¢ It is the most efficient mode of communication, as both devices can
transmit and receive data simultaneously.

*   Full-duplex mode provides a high level of reliability and accuracy, as there
is no need for error correction mechanisms.

Disadvantages of Full-Duplex Mode

¢   Full-duplex mode is the most expensive mode, as it requires two
communication channels.

* — It is more complex than simplex and half-duplex modes, as it requires two
physically separate transmission paths or a division of channel capacity.

¢   Full-duplex mode may not be suitable for all applications, as it requires a
high level of bandwidth and may not be necessary for some types of
communication.

FR 7 Ra ok &
--- page 2 ---
CO-1; b. | What is line coding? Describe its goals and discuss its various applications in [5]
SO-2 ; digital communication systems.
BL-1 * Answer: The process of converting the digital data into digital signal is
called as line coding which helps the receiver to get the original bits.
¢ The data that is in the form of text, numbers, audio, or video is
represented internally as series of 1s and Os.
* Line coding therefore transforms a set of bits into a digital signal.
* The sender side encrypts digital data into digital signals, while the
receiving side decodes the digital signal to regenerate the digital data.
* Example is sending data from computer to printer.
* Goals of Line Coding: Synchronization between sender and receiver
* — Efficient use of bandwidth
* No DC component (to avoid baseline drift)
¢ Error detection capability (sometimes)
¢ Applications: Ethernet
* USB (Universal Serial Bus)
* DSL (Digital Subscriber Line)
* — Digital communication over optical fiber

CO-2 ; c. | Explain how a network switch works. Also, discuss how a router differs from a [5]
SO-2 ; network switch.
BL-2 «Answer: When the source wants to send the data packet to the destination,

the packet first enters the switch and the switch reads its header and finds
the MAC address of the destination to identify the device then it sends the
packet out through the appropriate ports that lead to the destination
devices.

* Switch establishes a temporary connection between the source and
destination for communication and terminates the connection once the
conversation is done. Also, it offers full bandwidth to network traffic going to
and from a device simultaneously to reduce collision.

Network Switch Router

The router is primarily a device of Layer 3 of the OSI
Network Switch works on Layer 2 of the OSI Model.

Model.
The resource is shared among multiple devices with the help of a Data is moved between two or more computers
single LAN using a network switch with the help of a router.
Network switches uses data frames. Routers use data packets.
Switches only work in a Wired network connection. Router works with both wired and wifi networks.

Switches use MAC Addresses for transferring data to the proper
Routers use IP Addresses for the same work.
destination.

CO-2 ; d. | Explain the concept of an Intranet. Discuss the common challenges associated [5]
SO-2 ; with it.
BL-2 Answer: An Intranet is a private network that uses internet technologies (like TCP/IP,

web browsers, HTTP) within an organization. It’s designed to facilitate
communication, collaboration, and access to information among employees or
authorized users inside the company.

e = Think of it as a company’s internal website or private internet.

e = It is restricted to employees or members, not accessible to the public.

e It often hosts tools like email systems, document management, internal
databases, HR portals, project management platforms, and more.

Challenges Associated with Intranets:

FRR 2 fk AR KR
--- page 3 ---
1. Security Risks:
co Although internal, intranets are vulnerable to unauthorized access,
especially with remote access and mobile devices.
o Requires strong authentication, firewalls, and regular security
updates.
2. Content Management:
o Keeping content up-to-date and relevant is challenging.
o Information overload or outdated information can frustrate users.
3. User Adoption:
o Employees might resist or fail to use the intranet effectively if it’s not
user-friendly or doesn’t meet their needs.
o Lack of proper training can reduce effectiveness.
4. Integration Issues:
o Integrating diverse systems (HR, finance, document management)
into one intranet can be complex.
o Compatibility problems with legacy systems may arise.
5. Maintenance and Cost:
o Requires ongoing maintenance, technical support, and updates.
o Initial setup and running costs can be significant.
6. Performance and Accessibility:
o Ensuring fast, reliable access to intranet services, especially for
remote or mobile employees, can be difficult.
o Network congestion or poor infrastructure affects usability.

Attempt any 4

Q2 a. | Compare PAN and MAN in terms of geographic coverage, data transmission [10]
0-2: speed, propagation delay, fault tolerance and give suitable examples.
50-2: Answer:
BL-2 Parameter PAN (Personal Area Network) MAN (Metropolitan Area
Network)
Geographic Very small area (typically within 10||Covers a city or a large campus
Coverage meters) (range: 5-50 km)
Data . oe Typically low to moderate (e.g., 1— |/Higher speeds (e.g., 100 Mbps
Transmission
Speed 100 Mbps) to 1 Gbps or more)

Propagation
Delay

Moderate (due to longer
distances than PAN)

Low — fewer devices, so a single Higher — often designed with
failure can disrupt connectivity redundancy and multiple paths

Very low (due to short distances)

Fault Tolerance

- Bluetooth connection between

phone and earbuds - USB- - City-wide Wi-Fi networks -

Cable TV networks -

Examples connected peripherals - Broadband infrastructure
Smartwatch syncing with .
serving a metro area

smartphone
Q2 b. | Define the client/server model. Discuss its important features, advantages and [10]
co-1: disadvantages.
50-2 : * Answer: The Client/Server Model is a network architecture in which a
BL-2. client (computer, application, or device) requests services or resources,

and a server (powerful computer or program) provides those services or
resources over a network.
Key Features:

FOC IIR ICI ACH Ck a
--- page 4 ---
Q Client: A device or software that sends.
QO Server: A powerful computer/program that processes the request and
sends back the response.

Q) Network Medium: Communication happens over the internet.
Advantages:

v Centralized control (server manages everything).

v Easier to update and maintain.

v Secure (data stored in one place).
Disadvantages:

X_ If the server crashes ~ all clients are affected.

X Requires strong server performance.

Q3 a. | Explain the functionality of each layer of the TCP/IP reference model in detail. [10]
cO-3; Answer:

S0-2 : 1. Network Access Layer (Link Layer)

BL-3. Function:

e Responsible for the physical transmission of data on the local network.
e Handles hardware addressing (MAC addresses), frame formatting, and
error detection at the link level.

Examples:

e Ethernet, Wi-Fi (802.11), PPP (Point-to-Point Protocol)

2. Internet Layer
Function:

e Responsible for routing packets across multiple networks.
e Defines logical addressing (IP addresses).
e Handles packet forwarding and fragmentation.

Protocols:

e IP (Internet Protocol) — IPv4, IPv6

e ICMP (Internet Control Message Protocol) — for error messages, ping
e ARP (Address Resolution Protocol) — maps IP to MAC addresses

e RARP (Reverse ARP) — maps MAC to IP (obsolete)

3. Transport Layer
Function:

e Provides end-to-end communication between devices.
e Ensures reliable or unreliable data transfer depending on the protocol
used.

Protocols:

e TCP (Transmission Control Protocol):
o Reliable, connection-oriented.
o Error checking, flow control, acknowledgments.
o Example: Web browsing (HTTP), Email (SMTP).
e UDP (User Datagram Protocol):

FRR oR CR AR oR
--- page 5 ---
o Unreliable, connectionless.
o Faster, lower overhead.
o Example: Video streaming, DNS lookups.

4. Application Layer
Function:

e Closest to the end user.

e Provides network services to applications like email, web, file transfer,
etc.

e Handles high-level protocols, data formatting, and session control.

Protocols:

e HTTP/HTTPS — Web browsing

e FTP/SFTP — File transfer

e¢ SMTP, POP3, IMAP — Email

e DNS-— Domain name resolution
e SNMP — Network management

Q3 b. | Explain enterprise networks. Discuss their features, describe the essential [10]
CO-2 ; components, and provide examples of enterprise networks used in multinational

SO-2 ; companies.

BL-2 «Answer: An Enterprise Network is a large-scale computer network used

by a business, organization, or corporation to connect its employees,
departments, offices, and data centers.
* — It allows communication, resource sharing, and centralized management
within the organization.
* Typically larger, more secure and more complex than home or small
office networks.
Key Features of Enterprise Networks:
1. Scalability - Can handle hundreds or thousands of users.
2. Security — Includes firewalls, VPNs, and access controls.
3. Reliability — Extra connections and backup systems to keep the network
working all the time.
4. Centralized Management — Network devices and servers are centrally
monitored and managed.
5. Connectivity — Connects multiple offices, branch locations, and
sometimes remote employees.
Components of an Enterprise Network: Routers & Switches — For directing
network traffic.
QO) Firewalls & Security Appliances — For protection.
QO) Servers — For applications, databases, and file storage.
Q Wireless Access Points — For Wi-Fi connectivity.
Q WAN Links — Connect different office locations.
Examples: A multinational company like Microsoft connecting its offices in India,
USA, and Germany.
* A university campus network connecting all departments, hostels, and
labs.
* A bank network linking branches, ATMs, and data centers.

FOO ICO ACI ACA CHK a
--- page 6 ---
Q4 a. | How does Analog-to-Digital Conversion (ADC) work? Explain in detail the three [10]

CO-1; main steps involved — Sampling, Quantization, and Encoding.
SO-2 ; * Answer: Microphones create analog voice and camera creates analog
BL-2 videos, which are treated is analog data. To transmit this analog data

over digital signals, we need analog to digital conversion.

¢   Analog-to-Digital Conversion is the process of converting continuous
analog signals (like sound, temperature, voltage) into a digital form that
computers and digital devices can understand and process.

* Sampling: The analog signal is sampled every T interval.

* Most important factor in sampling is the rate at which analog signal is
sampled.

* According to Nyquist Theorem, the sampling rate must be at least two
times of the highest frequency of the signal.

* Quantization: Sampling yields discrete form of continuous analog signal.

* Every discrete pattern shows the amplitude of the analog signal at that
instance.

* The quantization is done between the maximum amplitude value and the
minimum amplitude value.

* — Encoding: In encoding, each approximated value is then converted into
binary format.

Q4 b. | Explain hybrid topology. Discuss the factors to be considered when choosing a [10]
CO-2 ; topology in a hybrid network scenario, and describe its advantages and

SO-2 ; disadvantages.

BL-2 * Answer: A hybrid topology combines two or more different network

topologies, such as star, bus, and ring, to create a single network that
leverages the strengths of each.
* This approach offers flexibility, scalability, and improved fault tolerance
by allowing for optimized performance and redundancy
* Acommon example is a "star-wired ring" topology, where multiple star
networks are interconnected by a ring topology.
Factors to Consider When Choosing a Topology:
* Scalability: How easy is it to add more devices?
* Cost: Some topologies require more wiring or equipment than others.
* Reliability: Some topologies are more fault-tolerant than others.
* Performance: How does the network handle traffic under heavy load?
Advantages of Hybrid Topology:
* This topology is very flexible.
¢ The size of the network can be easily expanded by adding new devices.
Disadvantages of Hybrid Topology:
* — It is challenging to design the architecture of the Hybrid Network.
* Hubs used in this topology are very expensive.
* The infrastructure cost is very high as a hybrid network requires a lot of
cabling and network devices .

Qs a. | What are Mobile Networks? Explain their working mechanism and describe their | [10]
CO-2 ; benefits and limitations.

SO-2 ; Answer:

BL-3 Mobile networks are wireless communication networks that allow mobile devices

(like smartphones, tablets, laptops) to connect and communicate over a wide
geographical area without being physically connected by cables.

FOCI 6 ACK ACH Ck a
--- page 7 ---
They enable voice calls, text messaging, and data services (e.g., internet access) by
using cellular technology, where the coverage area is divided into cells served by
base stations (cell towers).

Working Mechanism of Mobile Networks

1. Cellular Structure:
o The coverage area is divided into small regions called cells.
o Each cell is served by a base station (cell tower) with an antenna.
o This allows frequency reuse, improving capacity and coverage.
2. Mobile Device Communication:
o Amobile device connects wirelessly to the nearest base station
via radio waves.
o Voice/data from the device is transmitted to the base station.
3. Base Station to Network Core:
co. The base station forwards data to the Mobile Switching Center
(MSC) or core network, which routes it to its destination (another
mobile device, the internet, etc.).
4. Handover (Handoff):
o Asauser moves, the mobile network transfers the connection to
a neighboring cell to maintain uninterrupted service.
5. Backhaul and Internet Access:
o The core network is connected to external networks (e.g., the
public telephone network or the internet) via backhaul links.
6. Authentication and Security:
o User identity is verified using a SIM card and network credentials.
o Encryption ensures data privacy and security.

Benefits of Mobile Networks

1. Mobility: Users can access network services anywhere within coverage.

2. Wireless Communication: No need for physical cables; easier
infrastructure deployment.

3. Internet Access: Mobile broadband supports email, browsing, video, and
apps.

4. Global Connectivity: Roaming services allow international access.

5. Supports Diverse Applications: From simple calls to loT, GPS, remote
monitoring, etc.

Limitations of Mobile Networks

1. Coverage Gaps: Remote or rural areas may have weak or no signal.

2. Bandwidth Constraints: Network congestion can reduce speed and
quality.

3. Security Risks: Wireless signals are vulnerable to interception and attacks.

4. Battery Usage: Mobile communication consumes significant battery
power.

5. High Cost: Infrastructure, spectrum licensing, and maintenance are
expensive.

6. Latency: Especially in older generations (2G/3G), real-time
communication suffers.

FR 7 oR RA oR &
--- page 8 ---
Q5 b. | What is bandwidth? Compare and contrast digital and analog systems based on [10]

CO-1; technology, data transmission, uses, and examples.

SO-2 ; ¢ Answer: Bandwidth: Bandwidth refers to the maximum rate at which data

BL-2 can be transmitted over a communication channel in a given amount of
time.

* It determines how much data can be sent or received per second.

* Bandwidth is often measured in bits per second (bps), kilobits per second
(kbps), megabits per second (Mbps), or gigabits per second (Gbps).

* It represents the range of frequencies available for transmitting data over
a communication link.

¢* A higher bandwidth allows for faster data transfer rates.

Difference Between Digital And Analog System

Analog System Digital System
sion Aitalody signal rapresinns:ptiseat Dioital sionals are discrete and generated by digital
measurements. modulation
Waves Sine Waves Square Waves
Continuous range of values to represent
Representation Uses discrete values to represent information
information
, Samples analog waveforms into a limited set of numbers
Technology Records waveforms as they are. ie nae ba
pata “Asrseee By moles dig transmission And | i tmune-du ing transmission and write/read cycle.
transmissions writelread cycle.
Response to
More likely to get affected Less likely to get affected
Noise
Q6 a. | Discuss the OSI model by explaining its key features. Describe its benefits and [10]
CO-3 ; limitations, and enlist the major standardization bodies that define networking
SO-2 ; standards.
BL-2 Answer:

The OSI! (Open Systems Interconnection) model is a conceptual framework
developed by ISO (International Organization for Standardization) that standardizes
the functions of a communication system into seven distinct layers.

It helps different networking systems to communicate using standard protocols,
regardless of their underlying architecture.

Key Features:

e Layered Architecture:
o Breaks communication into smaller, manageable parts.
e Standard Interface Definitions:
o Each layer has defined functions and interacts only with its
adjacent layers.
e Modular Design:
o Easier to develop, test, and update one layer without affecting
others.
e Protocol Independence:
co Any protocol fitting the role of a layer can be swapped in.
e Interoperability:
o Ensures communication between different hardware and
software vendors.
e Abstract Model:

FOCI ACI ACH Ak a
--- page 9 ---
o Conceptual guide for designing real-world networking protocols
(e.g., TCP/IP)

Benefits: 1. Standardization

e Provides a universal framework for network communication, allowing
different systems and vendors to interoperate.
e Ensures compatibility through well-defined protocols at each layer.

2. Layered Approach

e Each layer handles a specific function, which makes the model modular
and easier to understand.
e Changes in one layer do not affect others, improving flexibility.

3. Easier Troubleshooting

e Problems can be diagnosed more easily by isolating them to a specific
layer (e.g., transport vs. network issues).

4. Promotes Interoperability

e Encourages the development of interoperable hardware and software,
reducing vendor lock-in.

e Devices from different manufacturers can communicate as long as they
follow standard protocols.

Limitations:
1. Theoretical and Complex

e The OSI model is more of a theoretical framework than a practical
implementation.

e In real-world networking, protocols don’t always fit neatly into its 7
layers.

2. Redundancy in Functions

e Some tasks, like error control and flow control, are handled by multiple
layers, which can create confusion and inefficiency.

3. Poor Adoption in Practice

e The TCP/IP model, which is simpler and more practical, is more widely
used in real-world internet systems.
e Most network protocol stacks are based on TCP/IP, not OSI.

4. Unclear Layer Boundaries

e In many real protocols, the functions of different layers overlap, making it
difficult to strictly apply the OSI layer separation.
e 1SO (International Organization for Standardization)
o Developed the OSI Reference Model.
o Sets international standards for technology.

FOC ICO OQ) ICI ACH Ak a
--- page 10 ---
e   JEEE (Institute of Electrical and Electronics Engineers)
o Focuses on networking hardware and LAN standards (e.g., IEEE
802.3 Ethernet, 802.11 Wi-Fi).
e IETF (Internet Engineering Task Force)
o Develops and promotes TCP/IP protocols.
o Publishes RFCs (Request for Comments), e.g., RFC 791 for IP.
e ITU-T (International Telecommunication Union - Telecommunication
Standardization Sector)
o Standardizes telecommunication protocols, e.g., signaling, voice,
and video.
e W3C (World Wide Web Consortium)
o Standardizes web protocols like HTTP, HTML, XML.

Q6 b. | Define the concept of access to information. Discuss in detail the fundamental [10]
co-1; factors that influence access to information and describe its essential

SO-2 ; components.

BL-3 ¢ Answer: Access to information refers to the ability of users or systems to

retrieve, share, and utilize data over a communication network.

* In data communication and networking, ensuring efficient and reliable
access to information is a fundamental goal.

* Networks enable multiple users and devices to connect, communicate,
and exchange information regardless of their physical location.

Fundamental Factors:

* Data Availability: Information must be available and accessible when
needed.

* Resource Sharing: Networks allow sharing of data, applications, and
hardware resources among users.

* Communication Channels: Efficient data transmission over various
channels (wired, wireless) ensures timely access.

* Security and Authorization: Proper controls must be in place to restrict
access to authorized users only, ensuring confidentiality and integrity.

* Latency and Speed: Faster networks provide quicker access, reducing
delays in data retrieval.

Q Components: Network Infrastructure:

= Routers > Direct data packets between different networks.

= Switches > Connect multiple devices within the same network (LAN).

= Hubs (less common now) > Basic device to connect devices in a network.

=" Access Points (APs) > Provide wireless connectivity (Wi-Fi).

= Firewalls > Control and monitor incoming/outgoing traffic for security.

Q Protocols:

= IP (Internet Protocol) > Defines addressing and routing of packets. (IPv4,
IPv6)

= TCP (Transmission Control Protocol) > Connection-oriented, reliable data
transfer.

= UDP (User Datagram Protocol) > Connectionless, faster but less reliable
(used in streaming, gaming).

= HTTP / HTTPS > Web communication

Q 1 Internet Access:

= Computers, Laptops, Smartphones, loT Devices > Need internet access to
send/receive data.

Q7 a. | Explain network technology, describe its goals, and discuss the essential [10]
CO-2 ; components of a network along with their roles.

SO-2 ; Answer:

BL-2

FORIIC CR ICICI ACA CA ka
--- page 11 ---
Network technology refers to the tools, protocols, hardware, and software used to
connect computers and other devices so they can communicate, share resources,
and exchange data.

It includes wired (like Ethernet) and wireless (like Wi-Fi, 4G/5G) technologies, and
supports everything from small home networks to the global Internet.

Goals:
Reliable Communication

e Ensure accurate and dependable data transfer between devices.
Resource Sharing

e Allow devices to share files, printers, internet access, and storage.
Scalability

e Enable the network to grow without performance issues.
Security

e Protect data from unauthorized access, tampering, or loss.
Efficiency

e Maximize data transmission speed while minimizing delays and
congestion.

Interoperability

e Support communication between different hardware and software
systems.

Accessibility

e Allow authorized users to access network resources anytime, from
anywhere.

Components:
1. Devices (Nodes)

e Role: Generate, transmit, or receive data.
2.Network Interface Card (NIC)

e Role: Connects a device to the network, handling data transmission and
reception.

FARR 7] RR OR
--- page 12 ---
3. Switch

e Role: Connects multiple devices within a LAN and forwards data to the
correct device using MAC addresses.

4. Router

e Role: Connects different networks (e.g., LAN to the Internet), directing
data using IP addresses.

5. Modem

e Role: Converts digital signals from a network into analog signals for
transmission over telephone or cable lines (and vice versa).

6. Access Point (AP)

e Role: Extends a wireless network by providing connectivity to Wi-Fi

devices
Q7 b. | What is transmission mode? Explain in detail the serial and parallel modes of [10]
CO-1; data transmission with suitable diagrams.
SO-2 ; Answer:
BL-2 * The transmission mode decides how data is transmitted between two
computers.

* The binary data in the form of 1s and Os can be sent in two different
modes: Parallel and Serial.

“The binary bits are organized

¢ Parallel Transmission:
in-to groups of fixed length.

* Both sender and receiver are connected in parallel with the equal
number of data lines.

* Both computers distinguish between high order and low order data lines.

* The sender sends all the bits at once on all lines.

* Because the data lines are equal to the number of bits in a group or data
frame, a complete group of bits (data frame) is sent in one go.

¢ Advantage of Parallel transmission is high speed and

* disadvantage is the cost of wires, as it is equal to the number of bits sent
in parallel.

¢ — Serial Transmission: In serial transmission, bits are sent one after another
in a queue manner.

* Serial transmission requires only one communication channel.

FRR 7 DR RR
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 28bea3e3ad41

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/Integrated_IT_7037/Introduction to Data Communication and Networks/ANS_Introduction to Data Communication and Networks(701IT0C004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Introduction to Data Communication and Networks
Date: 05 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
Q1   Answer briefly:
CO-1 ; SO-2 ;   a.   What is a digital system? Explain its features in detail.   [5]
BL-1   •   Answer: A digital system is one whose signal
has a finite number of discrete values. So, the
digital system works on digital signals and is
limited to binary values 0 or 1.
•   Digital systems are used to process
information in digital form.
•   The digital system has wide applications in
digital instruments like calculators, computers,
Telephones, etc.
•   Features of Digital Systems:
•   Uses Binary Code: Digital systems use binary
code, which is a combination of zeros and
ones, to represent information.
•   Accuracy: Digital systems are more accurate
than analog systems because the information is
represented in a precise and consistent
manner.
•   Processing Speed: Digital systems are capable
of processing large amounts of data quickly
and accurately.
•   Noise Immunity: Digital systems are immune to
noise and interference, which means that the
transmitted information is less likely to be
corrupted.
CO-1 ; SO-2 ;   b.   Explain spread spectrum and discuss its benefits.   [5]
BL-1   •   Answer: Spread Spectrum is a modulation
technique where the signal is spread over a
********** 1 **********
--- page 2 ---
wide frequency band, much wider than the
minimum bandwidth required.
This technique enhances security, resistance to
interference, and robustness of the transmission.
Benefits of Spread Spectrum:
-Difficult to intercept or jam without knowing the
spreading code
-Spread signal is less affected by narrowband
interference
- Reduces issues from signal reflection
- Supports multiple users (in CDMA)
CO-2 ; SO-2 ;   c.   Define routing algorithms. Classify them into types and   [5]
BL-2   describe applications where these routing algorithms
are used.
Answer:
•   Routing algorithms are used to determine the
best path for data to travel from one point to
another within a network.
•   These algorithms are crucial for ensuring
efficient communication and optimal
performance in computer networks, whether
they be local area networks (LANs), wide area
networks (WANs), or the internet itself.
•   There are several types of routing algorithms,
and they can be classified based on how they
find the best route and how they update
routing tables.
Classifications of Routing Algorithms:
a. Static Routing Algorithms
•   These algorithms use fixed paths to route data.
The routes do not change unless manually
updated.
•   Advantages: Simple to implement and easy to
configure.
•   Disadvantages: Not adaptive to network
changes (e.g., failures or congestion).
b. Dynamic Routing Algorithms
•   These algorithms adapt to network changes in
real-time and adjust routing tables accordingly.
•   Advantages: More flexible and robust to
network topology changes.
•   Disadvantages: More complex to configure and
manage.
Applications of Routing Algorithms:
•   Internet traffic routing: Algorithms like BGP
ensure efficient data routing between
networks and across regions.
•   Enterprise networks: OSPF help route data
efficiently within large, complex organizational
networks.
•   Mobile ad-hoc networks (MANETs): Special
routing algorithms are used to handle the
dynamic nature of these networks.
********** 2 **********
--- page 3 ---
•   Software-defined networks (SDN): Algorithms
are often implemented in the controller to
optimize traffic flow.
CO-2 ; SO-2 ;   d.   Explain the concept of the Internet and discuss its   [5]
BL-2   organizational benefits.
Answer: What is the Internet?
The Internet is a global network of interconnected
computers and devices that communicate with each
other using standardized protocols. It allows for the
exchange of information and access to services such as
websites, email, file sharing, video conferencing, and
more.
At its core, the Internet is a vast system that links
millions of private, public, academic, business, and
government networks, enabling users worldwide to
share data and resources seamlessly.
Organizational Benefits of the Internet
1. Improved Communication:
o Enables instant communication through
emails, messaging apps, and video
conferencing.
o   Facilitates collaboration among
employees regardless of their
geographic location.
2. Access to Information:
o Provides organizations with easy access
to vast amounts of data, research,
market trends, and customer insights.
o Helps in decision-making processes by
enabling quick information retrieval.
3. Cost Savings:
o Reduces costs associated with travel,
phone calls, and traditional mail
through digital communication tools.
o Enables remote work, saving on office
space and related expenses.
4. Enhanced Collaboration:
o Supports teamwork through tools like
cloud storage, project management
software, and collaborative platforms.
o Allows multiple users to work on the
same document or project in real-time.
5. Marketing and Customer Engagement:
o   Facilitates digital marketing through
social media, websites, and email
campaigns.
o Improves customer service with online
support, chatbots, and feedback
systems.
6. Efficiency and Productivity:
o Automates routine tasks through online
tools and software.
********** 3 **********
--- page 4 ---
o Streamlines business operations and
workflows.
7. Global Reach:
o Enables organizations to reach
international markets easily.
o Supports global supply chains and
partnerships.
Attempt any 4
Q2   a.   Compare LAN and WAN in terms of geographic   [10]
coverage, data transmission speed, propagation delay,
CO-2 ; SO-2 ;
fault tolerance and give suitable examples.
BL-2
Answer:
LAN (Local Area   WAN (Wide Area
Aspect
Network)   Network)
Limited to a
Covers a large
small geographic
geographic area, often
Geographic area such as a
spanning cities,
Coverage   single building,
countries, or even
office, or
continents.
campus.
Generally high   Usually slower
speed (typically compared to LANs,
100 Mbps to 10 speeds can vary widely
Data
Gbps or more)   (from a few Mbps to
Transmission
due to close   several Gbps)
Speed
proximity and   depending on the
less   technology and
interference.   infrastructure.
Low propagation
Higher propagation
delay because
delay due to long
Propagation devices are close
distances and multiple
Delay   together and
network devices/links
connections are
between endpoints.
direct.
Typically higher
fault tolerance
within the   Fault tolerance can
network due to   vary; large-scale WANs
Fault   redundancy and may have redundancy,
Tolerance   easier   but faults can cause
management.   major disruptions and
Faults are easier take longer to resolve.
to isolate and fix
quickly.
********** 4 **********
--- page 5 ---
Office network   The Internet, corporate
connecting   networks connecting
computers,   offices in different
Examples
printers, and   cities or countries,
servers within a telecommunications
building.   networks.
Q2   b.   What is Electronic Commerce (E-Commerce)? Explain   [10]
its four main types: Business-to-Business, Business-to-
CO-1 ; SO-2 ;
Consumer, Consumer-to-Business, and Consumer-to-
BL-2
Consumer, in detail with suitable examples.
•   Answer: Electronic Commerce (E-Commerce)
refers to the buying and selling of goods and
services over the internet or other computer
networks.
B2B (Business-to-Business):It involves various online
transactions, including shopping, banking, and
auctions.
•   Definition: Transactions where one business
sells goods or services to another business.
•   These usually involve bulk orders, wholesale,
raw materials, or enterprise software solutions.
•   Example: Alibaba supplying raw materials to
manufacturers, or Salesforce selling software
to companies.
B2C (Business-to-Consumer): Definition: A business
sells products or services directly to individual
customers through online platforms.
•   It is the most common form of e-commerce
that people use daily.
•   Example: Buying clothes on Myntra, ordering
groceries on Blinkit, or booking a movie ticket
on BookMyShow.
• C2C (Consumer-to-Consumer): Definition:
Individuals sell products or services directly to
other individuals using an online marketplace
platform.
•   The platform usually acts as a mediator to
connect buyers and sellers.
•   Example: Selling second-hand items on OLX,
eBay, or Quikr.
C2B (Consumer-to-Business): Definition: Individuals
offer their products or services to businesses. In this
model, consumers set prices or offer services, and
businesses purchase or hire them.
•   Example: A freelancer designing a website for a
company on Upwork or Fiverr.
Q3   a.   Discuss the functionality of each layer of the OSI   [10]
Reference Model in detail.
CO-3 ; SO-2 ;
BL-3
********** 5 **********
--- page 6 ---
Answer:
1. Physical Layer (Layer 1)
•   Function: Deals with the physical connection
between devices and the transmission of raw
bit streams over a physical medium.
•   Responsibilities:
o Defines electrical, mechanical,
procedural, and functional
specifications for activating,
maintaining, and deactivating the
physical link.
o Transmits raw bits (0s and 1s) over
cables, fiber optics, wireless.
o Handles modulation, voltage levels,
timing, data rates, and physical
connectors.
•   Examples: Ethernet cables, USB, Bluetooth,
hubs, repeaters.
2. Data Link Layer (Layer 2)
•   Function: Provides node-to-node data
transfer—a reliable link between two directly
connected nodes.
•   Responsibilities:
o Frames data packets from the network
layer into frames.
o Performs error detection and
correction to ensure data integrity.
o Manages MAC (Media Access Control)
addresses to identify devices on the
same network.
o Controls access to the physical medium
(who transmits when).
•   Sub-layers:
o MAC (Media Access Control): Controls
hardware addressing and access to the
medium.
o LLC (Logical Link Control): Manages
error checking and flow control.
•   Examples: Switches, bridges, Ethernet, PPP
(Point-to-Point Protocol).
3. Network Layer (Layer 3)
•   Function: Manages device addressing, tracks
the location of devices on the network, and
determines the best way to move data.
•   Responsibilities:
o Routing packets from source to
destination across multiple networks.
o   Logical addressing through IP
addresses.
********** 6 **********
--- page 7 ---
o Fragmentation and reassembly of
packets if necessary.
•   Examples: Routers, IP (Internet Protocol), ICMP
(Internet Control Message Protocol).
4. Transport Layer (Layer 4)
•   Function: Ensures reliable data transfer
between end systems, error recovery, and flow
control.
•   Responsibilities:
o Segmentation of data from upper
layers into smaller units for
transmission.
o End-to-end error detection and
correction.
o Flow control to prevent overwhelming
receivers.
o Provides either connection-oriented
(TCP) or connectionless (UDP)
communication.
•   Examples: TCP (Transmission Control Protocol),
UDP (User Datagram Protocol).
5. Session Layer (Layer 5)
•   Function: Manages and controls connections
(sessions) between computers.
•   Responsibilities:
o   Establishes, maintains, and terminates
sessions.
o Synchronizes data exchange by adding
checkpoints (so if a connection drops, it
can resume from a checkpoint).
o Manages dialog control (who transmits,
when).
•   Examples: Session establishment in
applications like remote procedure calls,
NetBIOS.
6. Presentation Layer (Layer 6)
•   Function: Translates, encrypts, and compresses
data for the application layer.
•   Responsibilities:
o Data translation between different
formats (e.g., ASCII to EBCDIC).
o Data encryption and decryption for
security.
o Data compression and decompression
to reduce size.
•   Examples: Encryption protocols (SSL/TLS),
JPEG, MPEG, GIF formats.
********** 7 **********
--- page 8 ---
7. Application Layer (Layer 7)
•   Function: Provides network services directly to
end-users or applications.
•   Responsibilities:
o   Interfaces directly with software
applications.
o Handles high-level protocols, issues of
representation, encoding, and dialog
control.
o Provides services such as email, file
transfer, and web browsing.
•   Examples: HTTP, FTP, SMTP, DNS, Telnet.
Q3   b.   Explain a transit network, describe its features, and   [10]
CO-2 ; SO-2 ;   provide examples of transit network providers.
BL-2   Illustrate with a scenario how a transit network is used
in real-world communication.
•   Answer: A transit network (or IP transit) is a
service where one network pays another
network operator (its upstream provider) to
carry (“transit”) its traffic to or from the rest of
the Internet.
•   The transit provider gives access to a broad
range of Internet routes (in effect the whole
global Internet, or large parts of it) rather than
only specific networks.
• A Transit Network is a type of computer
network that helps data move between two or
more other networks.
•   In simple words:
- It is like a middleman network that connects
different networks so data can pass through it
to reach its final destination.
Features:
❑ It does not belong to the sender or the receiver
network.
❑ Its main job is to forward traffic between
networks.
❑ Often used in large organizations and ISPs
(Internet Service Providers).
Examples of Transit Network Providers:
1. NetIX
• A global internet exchange and transit
provider.
•   Offers direct routes between ISPs, data
centers, and networks.
2.Tata Communications
•   India-based global telecom giant.
•   Operates submarine cables and provides
international IP transit.
3.GTT(Global Telecom & Technology) Communications
********** 8 **********
--- page 9 ---
•   Global internet backbone provider.
•   Provides IP Transit and interconnection
services across continents.
Scenario: Two company branches (Branch A and
Branch C) are connected to the Head Office Network
(B).
•   If Branch A sends data to Branch C, the Head
Office Network (B) acts as a Transit Network —
the data just passes through it.
Q4   a.   What is multiplexing? Explain why it is needed in   [10]
CO-1 ; SO-2 ;   communication systems. Compare a multiplexer and a
BL-2   demultiplexer.
•   Answer: Multiplexing is a technique used to
combine multiple signals and transmit them
simultaneously over a single communication
channel, making efficient use of available
bandwidth.
Why Multiplexing?
•   Saves infrastructure cost
•   Maximizes bandwidth utilization
•   Enables simultaneous data transmission
Q4   b.   Explain the working of star topology and ring topology.   [10]
CO-2 ; SO-2 ;   Illustrate each with a diagram and elaborate their
BL-2   advantages and disadvantages.
Answer:
Star Topology: A star topology is a network layout
where every device connects to a single central hub,
like a switch or router.
•   Data travels from the sender to the central
hub, which then forwards it to the intended
recipient, similar to how a star has a central
point with points radiating outwards.
•   This setup simplifies management and isolation
of problems, as a failure in one device's
connection does not affect the others, though
a failure in the central hub will bring down the
entire network.
********** 9 **********
--- page 10 ---
•   Advantages of Star Topology: Easy to manage
and configure: It is relatively simple to add new
devices, troubleshoot issues, and maintain the
network.
•   Reliability: If one device fails, it does not affect
the rest of the network.
•   Scalable: New devices can be added without
disturbing the rest of the network.
Disadvantages of Star Topology:
•   Central point of failure: If the central
hub/switch fails, the entire network is down.
Ring Topology: Ring topology is a network
configuration where each device is connected to
exactly two other devices, creating a circular, closed-
loop pathway for data.
•   Data travels in a single direction
(unidirectional) around the ring, passed from
one device to the next until it reaches its
destination.
•   This setup minimizes data collisions because
each device gets an opportunity to transmit
when it receives a special token, but a single
point of failure in one device or cable can
disrupt the entire network.
Advantages of Ring Topology:
•   Data transfer is predictable and consistent,
making it suitable for time-sensitive
applications.
•   Performs well in environments with moderate
traffic and is efficient in certain types of
networks.
********** 10 **********
--- page 11 ---
Disadvantages of Ring Topology:
•   Single point of failure: If one device or cable in
the ring fails, the entire network can be
disrupted (unless it's a dual ring).
•   Troubleshooting can be difficult, especially in
larger networks.
•   Adding or removing devices requires the
network to be temporarily shut down.
Q5   a.   What are wireless networks? Explain their working   [10]
CO-2 ; SO-2 ;   mechanism and classify the types of wireless networks
BL-3   used in communication.
Answer:
Wireless networks are communication networks that use
wireless data connections between network nodes
instead of wired connections. In a wireless network, data
is transmitted over the air using radio waves, infrared,
satellite signals, or other wireless communication
methods.
Wireless networks enable devices like smartphones,
laptops, sensors, and other equipment to connect to
each other and to the internet without the need for
physical cables.
Working Mechanism of Wireless Networks
1. Transmission Medium:
o Wireless networks use electromagnetic
waves (typically radio waves or
infrared) to transmit data through the
air.
o Devices have wireless network
interface cards (NICs) equipped with
antennas to send and receive signals.
2. Communication Process:
o Data is converted into a signal by the
transmitting device.
o The signal is modulated onto a carrier
wave and broadcasted over the
wireless medium.
o The receiving device demodulates the
signal to retrieve the original data.
o Wireless protocols manage how data is
formatted, transmitted, detected, and
error-checked.
3. Access and Coordination:
o Wireless networks use protocols like
CSMA/CA (Carrier Sense Multiple
Access with Collision Avoidance) to
coordinate access to the shared
medium and avoid collisions.
o Devices can connect through wireless
access points (like Wi-Fi routers) or
directly in peer-to-peer modes.
4. Security:
********** 11 **********
--- page 12 ---
o Wireless networks implement
encryption protocols (e.g., WPA3 for
Wi-Fi) to secure data transmission and
prevent unauthorized access.
Classification of Wireless Networks:
1. Wireless Personal Area Network (WPAN)
•   Coverage: A few meters (typically up to 10
meters).
•   Purpose: Connects personal devices in close
proximity.
•   Examples: Bluetooth, Infrared, ZigBee.
• Use Case: Connecting wireless headphones to a
phone, smart home devices communication.
2. Wireless Local Area Network (WLAN)
•   Coverage: Tens to hundreds of meters.
•   Purpose: Connects devices within a limited
area like homes, offices, or campuses.
•   Examples: Wi-Fi (IEEE 802.11 standards).
• Use Case: Internet access in homes, offices,
coffee shops.
3. Wireless Metropolitan Area Network (WMAN)
•   Coverage: Several kilometers, covering a city or
metropolitan area.
•   Purpose: Provides broadband wireless access
within cities.
•   Examples: WiMAX (Worldwide Interoperability
for Microwave Access).
• Use Case: Providing internet to city-wide areas
or large campuses.
Q5   b.   Discuss the three modes of communication: Simplex,   [10]
CO-1 ; SO-2 ;   Half-Duplex, and Full-Duplex. Write their advantages
BL-2   and disadvantages.
•   Answer: Simplex Mode: In Simplex mode, the
communication is unidirectional, as on a one-
way street.
•   Only one of the two devices on a link can
transmit, the other can only receive.
•   The simplex mode can use the entire capacity
of the channel to send data in one direction.
•   Eg: Keyboard and traditional monitors. The
keyboard can only introduce input, the monitor
can only give the output.
•   Advantages of Simplex Mode: Only one-way
communication is possible.
•   There is no way to verify if the transmitted
data has been received correctly.
********** 12 **********
--- page 13 ---
•   Simplex mode is not suitable for applications
that require bidirectional communication.
• mode is the easiest and most reliable mode of
communication.
•   It is the most cost-effective mode, as it only
requires one communication channel.
•   There is no need for coordination between the
transmitting and receiving devices, which
simplifies the communication process.
•   Simplex mode is particularly useful in situations
where feedback or response is not required,
such as broadcasting or surveillance.
•   Disadvantages of Simplex Mode: Half-Duplex
Mode: In half-duplex mode, each station can
both transmit and receive, but not at the same
time.
• When one device is sending, the other can only
receive, and vice versa.
•   The half-duplex mode is used in cases where
there is no need for communication in both
directions at the same time.
•   Advantages of Half Duplex Mode: Half-duplex
mode allows for bidirectional communication,
which is useful in situations where devices
need to send and receive data.
•   It is a more efficient mode of communication
than simplex mode, as the channel can be used
for both transmission and reception.
•   Half-duplex mode is less expensive than full-
duplex mode, as it only requires one
communication channel.
•   Disadvantages of Half Duplex Mode: Half-
duplex mode is less reliable than Full-Duplex
mode, as both devices cannot transmit at the
same time.
•   There is a delay between transmission and
reception, which can cause problems in some
applications.
•   There is a need for coordination between the
transmitting and receiving devices, which can
complicate the communication process.
•   Full-Duplex Mode: In full-duplex mode, both
stations can transmit and receive
simultaneously.
•   Full-duplex mode is used when communication
in both directions is required all the time.
•   The capacity of the channel, however, must be
divided between the two directions.
•   Advantages of Full-Duplex Mode: Full-duplex
mode allows for simultaneous bidirectional
communication, which is ideal for real-time
applications such as video conferencing or
online gaming.
********** 13 **********
--- page 14 ---
•   It is the most efficient mode of communication,
as both devices can transmit and receive data
simultaneously.
•   Full-duplex mode provides a high level of
reliability and accuracy, as there is no need for
error correction mechanisms.
•   Disadvantages of Full-Duplex Mode: Full-duplex
mode is the most expensive mode, as it
requires two communication channels.
•   It is more complex than simplex and half-
duplex modes, as it requires two physically
separate transmission paths or a division of
channel capacity.
•   Full-duplex mode may not be suitable for all
applications, as it requires a high level
of bandwidth and may not be necessary for
some types of communication.
Q6   a.   Explain the design goals of a network protocol. Discuss   [10]
CO-3 ; SO-2 ;   protocol layering and describe the benefits.
BL-2   Answer: Design Goals of a Network Protocol
A network protocol is a set of rules that govern
communication between devices on a network. The
main design goals are:
1. Reliability: Ensure data is delivered accurately
and in order, handling errors and lost packets.
2. Efficiency: Maximize the use of network
resources (bandwidth, processing power) while
minimizing delay.
3. Scalability: Support many devices and expand
smoothly as the network grows.
4. Flexibility: Work over different types of
hardware and network technologies.
5. Interoperability: Enable communication
between different systems and manufacturers.
6. Security: Protect data from unauthorized
access and tampering.
7. Simplicity: Be easy to implement and maintain,
reducing complexity.
Protocol Layering
Protocol layering is the organization of network
protocols into layers, where each layer handles a
specific part of the communication process and
interacts only with the layer directly above or below it.
Common Models:
•   OSI Model (7 layers): Physical, Data Link,
Network, Transport, Session, Presentation,
Application.
•   TCP/IP Model (4 layers): Link, Internet,
Transport, Application.
********** 14 **********
--- page 15 ---
Benefits of Protocol Layering
1. Modularity: Each layer can be designed,
implemented, and updated independently.
2. Simplifies troubleshooting: Problems can be
isolated to a specific layer.
3. Interoperability: Standardized layers enable
devices from different vendors to
communicate.
4. Flexibility: Layers can be replaced or upgraded
without affecting the entire system.
5. Abstraction: Higher layers don’t need to know
the details of lower layers, enabling easier
design.
6. Reuse: Common functions (e.g., routing, error
detection) are handled once at appropriate
layers and reused by many applications.
Q6   b.   What do you mean by Person-to-Person   [10]
CO-1 ; SO-2 ;   Communication? Describe its key aspects and
BL-3   elaborate its applications in different fields like
education, business, and social networking.
•   Answer: Person-to-person communication
refers to the direct exchange of information
between two individuals over a communication
network.
•   This type of communication often involves
interactive and real-time data transfer,
allowing users to send messages, talk, or share
information instantly.
•   Key aspects of person-to-person
communication: Decentralized Structure:
Unlike client-server networks where a central
server manages communication, P2P networks
allow individuals or devices to act as both
clients and servers, communicating directly
with one another.
•   Direct Exchange: Information and data are
transferred directly between the
communicating parties.
•   Applications: Instant messaging (IM) and chat
rooms: Enabling real-time text-based
conversations between users. example:
WhatsApp, Facebook Messenger, or Telegram
•   Video conferencing: Facilitating face-to-face
interactions over a network. example: Zoom,
Microsoft Teams, or Google Meet
•   File sharing: Allowing users to share files and
data directly from their own devices to others
within the network. Example: Dropbox,
OneDrive, Google Drive
•   Social media: Providing platforms for users to
connect and share content with each other.
********** 15 **********
--- page 16 ---
Q7   a.   Define Internetworks. Illustrate with examples, and   [10]
CO-2 ; SO-2 ;   explain their advantages and disadvantages.
BL-2   Answer:
An internetwork (or internet in a generic sense) is a
network of networks. It is formed by connecting
multiple smaller networks (like LANs, WANs) using
devices such as routers and gateways, enabling
communication between these different networks.
In simpler terms, an internetwork allows separate
networks, which may use different protocols or
technologies, to communicate as a single larger
network.
Examples of Internetworks
• The Internet: The largest and most famous
example of an internetwork. It connects
millions of private, public, academic, business,
and government networks worldwide.
•   Corporate Internetwork: A company may have
multiple branch offices, each with its own local
network (LAN). These LANs are connected via
WAN links to form a corporate internetwork.
• Campus Network: A university might connect
several departmental networks across multiple
buildings to create a campus internetwork.
Advantages of Internetworks
1. Resource Sharing: Users on different networks
can share resources like files, printers, and
internet access.
2. Scalability: Internetworks can grow by simply
connecting more networks.
3. Communication: Enables communication
across geographically dispersed networks.
4. Flexibility: Different network types and
protocols can coexist and interoperate.
5. Reliability: Multiple paths between networks
can improve fault tolerance and load balancing.
6. Centralized Management: Organizations can
manage multiple networks as a unified whole.
Disadvantages of Internetworks
1. Complexity: Designing, managing, and
troubleshooting internetworks is more complex
than standalone networks.
2. Security Risks: Connecting multiple networks
increases exposure to cyber threats and
requires robust security measures.
********** 16 **********
--- page 17 ---
3. Cost: Building and maintaining internetworks
can be expensive due to hardware (routers,
switches) and management tools.
4. Performance Issues: Communication delays or
bottlenecks may arise due to increased traffic
or inefficient routing.
5. Compatibility Issues: Networks using different
technologies or protocols may face challenges
in integration, requiring gateways or protocol
converters.
Q7   b.   What are the goals of line coding? Explain the unipolar   [10]
CO-1 ; SO-2 ;   and polar types of line coding in detail.
BL-2   Answer: Goals of Line Coding:
•   Synchronization between sender and receiver
•   Efficient use of bandwidth
• No DC component (to avoid baseline drift)
•   Error detection capability (sometimes)
•   Unipolar: Unipolar encoding schemes use
single voltage level to represent data.
•   In this case, to represent binary 1, high voltage
is transmitted and to represent 0, no voltage is
transmitted.
•   It is also called Unipolar-Non-return-to-zero,
because there is no rest condition i.e. it either
represents 1 or 0.
•   Polar: Polar encoding scheme uses multiple
voltage levels to represent binary values.
•   Polar encodings is available in four types
•   Polar Non-Return to Zero (Polar NRZ): It uses
two different voltage levels to represent binary
values. Generally, positive voltage represents 1
and negative value represents 0. It is also NRZ
because there is no rest condition.
• NRZ scheme has two variants: NRZ-L and NRZ-I.
Return to Zero (RZ):
•   Problem with NRZ is that the receiver cannot
conclude when a bit ended and when the next
bit is started, in case when sender and
receivers clock are not synchronized.
********** 17 **********
--- page 18 ---
❑ Manchester
•   This encoding scheme is a combination of RZ
and NRZ-L. Bit time is divided into two halves.
It transits in the middle of the bit and changes
phase when a different bit is encountered.
❑ Differential Manchester
•   This encoding scheme is a combination of RZ
and NRZ-I. It also transit at the middle of the
bit but changes phase only when 1 is
encountered.
********** 18 **********
````

## 2024-25 · Final-Exam · Sem 5 · Answer key · paper 1867b78e89dc

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2024/Sem_05/Final-Exam/Integrated_IT_7037/Introduction to Data Communication and Networks/ANS_Introduction to Data Communication and Networks(701IT0C004)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Nov 2024
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (INFORMATION TECHNOLOGY)SIX
YEARS INTEGRATED PROGRAM
Year: III/Semester V(Exam Year: 2024-2025)
Subject: Introduction to Data Communication and Networks
Date: 28 Nov 2024   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question 1 is compulsory.
5. Answer any 4 of the remaining questions.
Q1   Answer the following questions briefly:   [20]
a.   Explain the real-life applications of Metropolitan Area Networks (MAN) in brief.
Answer:
•   City infrastructure: Interconnect critical communication infrastructure like telephone exchanges, and
cellular networks within a city.
•   Institutional connectivity: Educational institutes and hospitals use MANs to connect campuses in the city. 5
•   Carrier services: Telecom providers use MANs for delivering services within a metro region.
•   Disaster management: MANs help coordinate disaster response by connecting emergency services.
•   Public services access: Provide access to metropolitan municipal services like transport, utilities, parking,
surveillance etc.
b.   Discuss the key features of the Internet.
Answer:
❑ Globally available: The internet is an international service with universal access. People living in isolated
areas of an archipelago or even in the depths of Africa can now access the internet.
❑ Easy to use: The software used to connect to the internet (web browser) is user-friendly and easy to 5
understand. It’s also relatively easy to create.
❑ Compatible with other types of media: The internet provides a high level of engagement with photos and
videos, among other media.
❑ Affordable: Internet service development, as well as maintenance costs, are modest.
❑ Flexible: Internet-based communication is highly adaptable. It supports text, audio, and video
communication. These services are available at both individual and organizational levels.
c.   Distinguish between Mesh and Star topologies.
Answer:
Star Topology
Structure:
•   All devices are connected to a central hub or switch.
•   Each device has a dedicated connection to the hub.   5
Advantages:
•   Simplicity: Easy to install and manage.
•   Fault Isolation: If one cable fails, only the connected device is affected, while the rest of the network
remains operational.
•   Scalability: New devices can be added easily without disrupting the network.
Disadvantages:
•   Single Point of Failure: If the central hub fails, the entire network goes down.
********** 1 **********
--- page 2 ---
•   Cost: Requires more cabling than some other topologies and may need more expensive networking
hardware (hubs/switches).
Mesh Topology
Structure:
•   Each device is connected to every other device in the network (full mesh) or at least some devices
(partial mesh).
Advantages:
•   Reliability: Highly resilient; if one connection fails, data can be routed through another connection.
• No Single Point of Failure: Since multiple paths exist for data, the failure of one device or link
doesn’t impact the entire network.
Disadvantages:
•   Complexity: More complex to design and manage due to the multiple connections.
•   Cost: Higher installation and maintenance costs due to the amount of cabling and networking
equipment needed.
Use Cases:
•   Star topology is commonly used in home and small office networks due to its simplicity and ease
of management.
• Mesh topology is often used in critical applications where reliability is crucial, such as in large
enterprise networks or military communications.
d.   Discuss the advantages of protocol layering in network communication.
Answer:
Modularity:
•   Layering makes the design of network protocols modular. Each layer can be developed and
maintained independently as long as it follows the rules for interacting with the layers above and
below it.
Simplified Troubleshooting and Maintenance:
•   Problems can be isolated and addressed within a specific layer without affecting the entire system,
making debugging and troubleshooting easier.
Interoperability:
•   Protocol layering promotes interoperability between different systems and devices, as each layer
follows a standardized set of rules. This allows devices from different manufacturers to communicate 5
with each other seamlessly.
Scalability:
•   The modular structure allows for easier updates and scalability. New protocols or technologies can
be added or modified at one layer without needing significant changes to other layers.
Abstraction:
•   Each layer abstracts its functions from the others, simplifying complex processes. For example,
higher layers do not need to know how the lower layers manage data transmission; they only need to
know that data will be delivered.
Reusability:
•   Functions implemented at each layer can be reused by different applications or services, leading to
more efficient and cost-effective software and hardware development.
Q2   Answer the following questions.   [20]
a.   “Fiber-optic considered the most preferred mode of broadband connection” Justify the statement with proper
reasoning.
Answer:
Fibre-optic broadband is considered the most preferred mode of broadband connection due to its numerous
advantages, which include:   10
1. High-Speed Data Transmission:
o   Fibre-optic technology uses light to transmit data, allowing for much higher speeds compared to
other types of broadband connections like DSL, cable, and satellite. It can support speeds
ranging from hundreds of Mbps to several Gbps, which is essential for applications that require
high bandwidth, such as video streaming, online gaming, and large file transfers.
2. Greater Bandwidth:
********** 2 **********
--- page 3 ---
o   Fibre-optic cables have a much higher bandwidth capacity than copper cables used in DSL and
cable connections. This means that more data can be transmitted simultaneously, which is ideal
for businesses and homes with multiple devices connected to the internet at the same time.
3. Longer Distance without Signal Loss:
o   Unlike copper cables, fibre-optic cables can carry signals over long distances without significant
loss of speed or signal quality. This makes it suitable for connecting remote areas and providing
a stable internet connection over large distances.
4.   Reliability and Consistency:
o   Fibre-optic connections are less susceptible to interference from electromagnetic signals or
weather conditions compared to other broadband technologies. This ensures a more reliable and
consistent connection, even during peak usage times or adverse weather.
5. Low Latency:
o   Fibre-optic internet has lower latency, which is the delay between sending and receiving data.
Low latency is crucial for applications that require real-time data transmission, such as video
conferencing, online gaming, and VoIP calls.
6. Future-Proof Technology:
o   Fibre-optic infrastructure is considered future-proof because it can support the growing demand
for faster internet speeds and higher bandwidth requirements. As technology advances and
internet needs increase, fibre-optic networks can be easily upgraded without significant changes
to the existing infrastructure.
7. Enhanced Security:
o   Data transmitted through fibre-optic cables is more secure than data sent through copper wires,
as it is difficult to intercept without disrupting the signal. This makes fibre-optic broadband a
safer option for organizations and individuals concerned about data privacy and security.
8. Cost-Effective in the Long Run:
o While the initial installation cost of fibre-optic broadband might be higher than other broadband
options, its long-term benefits in terms of speed, reliability, and low maintenance costs make it
a cost-effective solution. The reduced need for frequent repairs and upgrades further adds to its
cost-efficiency.
These factors combined make fibre-optic broadband the most preferred mode of internet connection,
especially for businesses and users who require high-speed, reliable, and secure internet access.
b.   Explain how home networks differ from traditional LANs in terms of setup, management, and application.
Discuss the advantages and disadvantages of using a Home Area Network (HAN).
Answer:
Home networks and traditional Local Area Networks (LANs) differ in several ways, including setup,
management, and application:
Differences Between Home Networks and Traditional LANs
1. Setup:
o Home Networks (HAN): Generally have a simpler setup compared to traditional LANs.
They often use consumer-grade equipment like Wi-Fi routers, modems, and smart devices.
Configuration is usually plug-and-play, designed to be user-friendly and easy for non- 10
technical users.
o   Traditional LANs: Require more advanced equipment like switches, routers, Ethernet
cables, and sometimes network servers. The setup process is more complex and often
requires technical expertise for proper installation and configuration.
2. Management:
o Home Networks: Managed by the user, often with basic control interfaces provided by the
router or network management apps. Home networks may use features like parental
controls, guest networks, and basic firewall settings for security.
o   Traditional LANs: Usually managed by IT professionals or network administrators who
handle more sophisticated control settings, including VLANs, advanced security protocols,
centralized user authentication, and network monitoring.
3. Application:
o Home Networks: Primarily designed for personal use, enabling activities like internet
browsing, streaming media, gaming, home automation, and connecting IoT devices. They
focus on providing convenient connectivity for multiple devices in a household.
********** 3 **********
--- page 4 ---
o   Traditional LANs: Typically used in business environments for resource sharing, data
communication, running organizational software, and hosting applications like databases,
email servers, and file servers. They are built for higher performance and reliability.
Advantages of Home Area Network (HAN)
1.   Accessibility: Home networks provide easy access to the internet and shared resources for all
connected devices, making it convenient for users to connect laptops, smartphones, tablets, smart
TVs, and other devices.
2. Resource Sharing: Resources like printers, files, and media can be easily shared among devices
within the network, enhancing productivity and collaboration among household members.
3. Enhanced Security: With proper setup, HANs can be secured using passwords, firewalls, and
encryption, providing protection from unauthorized access and data breaches.
4. Ease of Management: Home networks are relatively easy to manage using the built-in settings
provided by routers. They often come with intuitive user interfaces that allow non-experts to control
the network.
5. Cost-Effective: Setting up a HAN is generally less expensive than a traditional LAN. It does not
require enterprise-grade hardware or extensive infrastructure, reducing the overall cost.
6. Comfort and Automation: With the integration of IoT devices, HANs enable automation of
household tasks, like controlling smart lights, security cameras, and home appliances, enhancing the
convenience and lifestyle of the users.
Disadvantages of Home Area Network (HAN)
1. Slow Connectivity: When multiple devices are connected and actively using the network, internet
speed and data transfer rates may slow down, especially if the network bandwidth is limited.
2. Limited Range: Home networks generally cover a limited geographical area, which might not be
suitable for larger homes or outdoor areas without using range extenders or additional access points.
3. Security Risks: If not properly secured, HANs can be vulnerable to cyberattacks. An attacker
gaining access to the network could potentially access sensitive data from any connected device.
4. Expensive Devices: Setting up a fully functional HAN can be costly if it involves purchasing smart
devices, appliances, and high-quality networking equipment to ensure efficient performance.
5. Interference Issues: Wireless home networks may face interference from other wireless devices or
physical obstructions, which can affect signal strength and network stability.
Q3   Answer the following questions.   [20]
a.   A video streaming service is looking to improve the quality of their content delivery to users across different
geographic locations. How can using a content delivery network (CDN) help the service achieve faster content
load times and reduced latency for their users?
Answer:
A Content Delivery Network (CDN) can significantly improve the quality of content delivery for a video
streaming service by achieving faster load times and reducing latency. Here's how a CDN can help in
enhancing the user experience:
1. Geographically Distributed Servers
• CDNs consist of a network of servers that are strategically distributed across multiple geographic
locations around the world. These servers store cached versions of the video content. When a user
requests to stream a video, the CDN delivers the content from the server that is closest to the user's 10
location, reducing the distance that data needs to travel.
•   This proximity to the user decreases latency, meaning that the video content loads faster and playback
is smoother, regardless of where the user is located.
2. Reduced Latency
•   Latency is the delay between a user's request for content and the moment that content starts to be
delivered. CDNs help reduce latency by serving content from local servers rather than a central server
that might be far away from the user.
•   This reduction in latency is crucial for video streaming services as it leads to faster video startup
times, minimal buffering, and an overall more seamless viewing experience.
3. Load Balancing and Scalability
• CDNs employ load balancing techniques to distribute traffic evenly across multiple servers,
preventing any single server from becoming overloaded. During peak times when the demand for
********** 4 **********
--- page 5 ---
streaming content is high, load balancing ensures that users experience consistent performance
without delays or interruptions.
•   This capability helps the video streaming service handle sudden spikes in traffic, such as during live
events or the release of popular new content, without compromising on streaming quality.
4. Improved Reliability and Availability
• CDNs enhance the reliability and availability of video streaming services by automatically rerouting
user requests to the next closest server if one server fails or becomes unavailable. This redundancy
ensures that the content remains accessible to users even in the case of server issues or network
outages.
•   High reliability is essential for streaming services to provide an uninterrupted experience, which is
crucial to retaining viewers and maintaining user satisfaction.
5. Optimized Bandwidth Usage
• By storing and serving cached copies of video content from local servers, CDNs reduce the load on
the origin server and the amount of data that needs to travel over the internet backbone. This
optimization leads to more efficient bandwidth usage and faster delivery speeds.
•   Reduced bandwidth consumption also lowers costs for the video streaming service, as less data is
being transmitted from the main server to users across long distances.
6. Adaptive Bitrate Streaming
• Many CDNs support adaptive bitrate streaming, which automatically adjusts the video quality based
on the user's internet speed and connection stability. This ensures that viewers experience the highest
possible video quality without buffering or interruptions, even if their network conditions fluctuate.
7. Enhanced Security
• CDNs offer built-in security features such as Distributed Denial-of-Service (DDoS) protection,
secure socket layer (SSL) encryption, and content protection against unauthorized access or piracy.
These features help ensure that the streaming service remains secure while delivering high-quality
content to users.
b.   Discuss the components of 2G architecture with a diagram.
Answer:
The architecture of 2G (Second Generation) cellular networks, which primarily used digital technology for
voice communication, is composed of several key components that work together to manage communication
between mobile devices and the wider telecommunications network. The main components of a 2G
architecture include:
10
1. Mobile Station (MS)
********** 5 **********
--- page 6 ---
•   Mobile Equipment (ME): This refers to the mobile device itself, such as a cell phone or a data
terminal. It includes the hardware and software required for communication, including the
transceiver, display, and user interface.
•   Subscriber Identity Module (SIM): The SIM card is a removable smart card that contains user
identification data, authentication information, and subscriber-related information like phone
number, service plans, and network settings. It allows users to switch devices easily while keeping
their subscriber identity.
2. Base Station Subsystem (BSS)
The BSS is responsible for handling communication between the mobile station and the network. It consists
of the following components:
•   Base Transceiver Station (BTS): The BTS is the hardware that communicates directly with the
mobile devices. It includes radio transceivers and antennas that manage the transmission and
reception of radio signals to and from mobile stations.
•   Base Station Controller (BSC): The BSC controls multiple BTSs and manages radio resources,
such as frequency allocation, handover (when a mobile device moves from one BTS to another), and
power control. It also acts as a gateway between the BTS and the core network.
3. Network and Switching Subsystem (NSS)
The NSS is the core component of the 2G architecture that handles call control, subscriber management, and
routing of calls and data. It includes:
•   Mobile Switching Center (MSC): The MSC is the primary component that handles call setup, call
routing, and call termination. It also manages mobility features like handover and roaming, enabling
users to move between different network areas without losing their connections.
• Home Location Register (HLR): The HLR is a centralized database that contains subscriber
information, including user profiles, authentication details, and current location. It stores permanent
data about each subscriber and plays a critical role in managing subscriber mobility.
•   Visitor Location Register (VLR): The VLR is a temporary database linked to the MSC. It contains
information about subscribers who are currently roaming in the area served by that particular MSC.
It stores information like the user's location, temporary mobile number, and authentication details.
•   Authentication Center (AuC): The AuC is responsible for authenticating the identity of subscribers
to ensure that only legitimate users can access the network. It stores security information like
encryption keys and authentication algorithms used to protect communication.
•   Equipment Identity Register (EIR): The EIR is a database that stores information about mobile
devices. It is used to verify the identity of mobile equipment by checking its International Mobile
Equipment Identity (IMEI) number. The EIR helps detect stolen or unauthorized devices on the
network.
4. Operation and Support Subsystem (OSS)
•   The OSS is responsible for managing the overall operation, maintenance, and administration of the
2G network. It provides tools for network monitoring, fault detection, performance analysis, and
system configuration. The OSS ensures that the network operates efficiently and with minimal
downtime.
Q4   Answer the following questions.   [20]
a.   Distinguish between synchronous and asynchronous transmission (Any 5 points). Explain the challenges
associated with implementing synchronous serial data transmission.
Answer:
10
Section   Synchronous Transmission   Asynchronous Transmission
********** 6 **********
--- page 7 ---
Data is transmitted in a continuous Data   is   transmitted   character by
Data Transfer
stream synchronized by a common character, with start and stop bits
Method
clock signal.   framing each character.
Clock   It   requires   precise   clock There   is   no   need   for   clock
Synchronizatio   synchronization between the sender synchronization; each character is self-
n   and receiver.   contained.
Less efficient due to the overhead of start
Efficient for high-speed data transfer
Efficiency   and stop bits, especially for large data
with minimal overhead.
sets.
Limited by start and stop bit overhead;
Data Transfer
Supports higher data transfer rates.   may not be suitable for high-speed
Speed
applications.
More   complex hardware   and
Hardware   Generally   simpler   hardware
software are required for maintaining
Complexity   requirements.
synchronization.
Better error detection and correction Basic error detection through parity bits
Error Detection
capabilities.   may not be as robust.
Commonly used in slower data transfer
Suitable for real-time applications and
Applications   applications,   such   as   serial
high-speed data transfer.
communication.
RS-232 serial communication, USB
Examples   Ethernet, Fiber Channel, USB 3.0.
keyboards, and mice.
Implementing synchronous serial data transmission comes with several challenges that need to be addressed
for effective communication. Here are the key challenges:
•   Clock Synchronization:
Synchronous serial transmission relies on a shared clock signal between the sender and receiver to ensure
data is transmitted and received in the same time frame.
Maintaining precise clock synchronization is challenging, especially over long distances or in
environments with fluctuating temperatures or electrical conditions.
Any slight mismatch in clock timing can lead to data errors, making synchronization critical to the
system's reliability.
•   Complexity of Hardware and Software:
Synchronous transmission typically requires more intricate hardware and software configurations to
maintain synchronization.
The need for specialized components, such as phase-locked loops (PLLs) or clock recovery circuits,
increases the complexity and cost of the system.
The implementation of protocols to manage the synchronization and error handling further complicates
the setup.
•   Single Point of Failure:
The system's reliance on a single clock source makes it vulnerable to a single point of failure.
If the clock signal is lost or corrupted, it can disrupt the entire communication process, leading to data
loss or transmission errors.
********** 7 **********
--- page 8 ---
Ensuring redundancy in clock distribution or recovery mechanisms can help mitigate this risk, but it also
adds to the complexity.
•   Latency:
Synchronous serial transmission requires waiting for the clocks to synchronize before data transmission
can begin.
This initial synchronization process can introduce delays in communication, especially when starting or
re-establishing a connection.
While data transfer rates are generally high once synchronization is achieved, the setup time can impact
real-time or time-sensitive applications.
•   Scalability Issues:
Synchronous transmission can become challenging to scale as the number of devices or nodes in the
network increases.
Managing clock signals and maintaining synchronization across multiple devices can be complex,
particularly in large networks.
The more devices there are, the harder it becomes to ensure that all are synchronized to the same clock
signal, leading to potential data timing issues.
•   Environmental Factors:
External factors, such as electromagnetic interference (EMI) or variations in temperature, can affect the
stability and accuracy of the clock signal.
Fluctuations in the signal due to these factors can lead to timing errors, impacting the reliability of data
transmission.
These challenges highlight the importance of precise timing and specialized equipment in synchronous serial
data transmission, making it suitable for high-speed and high-reliability applications but less flexible and cost-
effective compared to asynchronous transmission methods.
b.   Explain the concept of store and forward mechanism. Discuss how does the 'store and forward' mechanism in
message switching impacts real-time data transfer.
Answer:
• When the whole data is considered as a single data packet and transferred in one go, such a switching
technique is referred to as message switching.
•   It uses the store and forward mechanism.
•   If the data is very huge and cannot be transferred in one go, it is first broken down into smaller pieces of
data and sent to the intermediary node.
•   This intermediary node then constructs the full message after receiving all the data pieces.
•   After making the full message or the complete unit, then only it forwards the data.
•   It is not suitable for real-time applications and streaming media.
10
1. Increased Latency
•   Processing Time: Each message is stored at an intermediate node before being forwarded to the next
node. This introduces a delay at each step, as the message must be fully received, processed, and
then sent on.
• Queue Delays: If the network is busy or congested, messages may be queued at nodes, causing
further delays in transmission.
2. Non-Continuous Transmission
•   Batch Processing: Unlike circuit switching, where a dedicated path allows for continuous data flow,
message switching requires messages to be stored and then sent when resources are available. This
can interrupt the smooth flow of data necessary for real-time applications.
********** 8 **********
--- page 9 ---
•   Buffering: Messages may be held in buffers at various points in the network, which can delay their
arrival even if the next node is ready to receive them.
3. Potential for Packet Loss
•   Storage Limitations: If a node’s buffer is full due to high traffic, incoming messages may be
dropped or discarded, which can lead to data loss, particularly critical for real-time applications.
•   Retries and Acknowledgments: If messages are lost, they may need to be resent, further increasing
latency and impacting real-time performance.
4. Variability in Delivery Time
•   Unpredictable Delays: The time taken for a message to travel from source to destination can vary
significantly, making it challenging to ensure that data arrives within the time constraints required
for real-time applications (like VoIP or video conferencing).
•   Jitter: The variability in message arrival times can result in jitter, which can degrade the quality of
real-time communications, especially in audio and video streams.
5. Suitability for Non-Real-Time Applications
•   Efficiency for Bulk Data: Message switching is well-suited for non-real-time applications (like
email or file transfer) where latency is less critical, and messages can be sent and received with some
delay.
• Load Balancing: It can effectively manage data bursts and evenly distribute traffic across the
network, improving overall resource utilization.
Q5   Answer the following questions.   [20]
a.   An organization is planning to use satellites for transmitting data for its global communication network.
Considering satellite communication's susceptibility to noise, which modulation technique would be the most
efficient and reliable for data transmission: Amplitude Shift Keying (ASK), Frequency Shift Keying (FSK),
or Phase Shift Keying (PSK)? Explain your reasoning.
Answer:
For satellite communication, where noise and signal integrity are critical concerns, Phase Shift Keying
(PSK) is the most efficient and reliable modulation technique compared to Amplitude Shift Keying (ASK)
and Frequency Shift Keying (FSK). Here’s why:
Reasons for Choosing PSK:
1. High Noise Immunity:
o PSK, especially Binary Phase Shift Keying (BPSK) and Quadrature Phase Shift Keying
(QPSK), offers better resistance to noise and interference than ASK and FSK.
o   Unlike ASK, where signal amplitude changes (and is therefore more susceptible to noise
variations), PSK encodes data in the phase of the carrier wave, making it less affected by
amplitude-based noise.
2. Power Efficiency:   10
o PSK is more power-efficient than both ASK and FSK, making it ideal for satellite
communication, where power resources are often limited.
o The consistent amplitude of the PSK signal also means that it can be amplified without
distortion, which is crucial for long-distance satellite transmissions.
3. Bandwidth Efficiency:
o PSK provides better bandwidth efficiency compared to ASK and FSK. Techniques like QPSK
can transmit two bits of data per symbol, effectively doubling the data rate without increasing
the bandwidth.
o   Higher-order PSK techniques (such as 8-PSK or 16-PSK) can be used to further increase the
data throughput within the same bandwidth, making it more suitable for high-speed data
transmission over satellites.
4. Error Detection and Correction:
o PSK allows for the implementation of advanced error detection and correction techniques, which
are crucial for maintaining data integrity in satellite communication.
o By using phase information instead of amplitude, PSK systems are more resilient to signal
distortions caused by environmental factors, which are common in satellite links.
Limitations of ASK and FSK in Satellite Communication:
********** 9 **********
--- page 10 ---
•   Amplitude Shift Keying (ASK):
o ASK is highly susceptible to noise because it relies on changes in the amplitude of the signal,
which can be easily distorted during transmission.
o   Environmental factors such as atmospheric disturbances and signal attenuation can severely
affect the quality of ASK signals, making it less reliable for satellite communication.
•   Frequency Shift Keying (FSK):
o While FSK has better noise immunity than ASK, it still requires more bandwidth to transmit
data compared to PSK.
o   In satellite communication, where bandwidth is a valuable resource, the higher bandwidth
requirements of FSK make it less efficient.
o FSK also has lower spectral efficiency compared to PSK, meaning that for the same amount of
bandwidth, PSK can transmit more data.
b.   Compare and contrast virtual circuit switching and datagram packet switching.
Answer:
Virtual circuit switching and datagram packet switching are two fundamental methods for transmitting data
across networks. Here’s a breakdown of each concept and their differences:
Virtual Circuit Switching
Concept:
•   Virtual circuit switching combines elements of both circuit switching and packet switching. It
establishes a predefined path (virtual circuit) between the sender and receiver before data is
transmitted. This path remains in use for the duration of the session.
Characteristics:
•   Connection Establishment: Before data transmission begins, a virtual circuit is established through
signaling. This setup can involve resource allocation along the path.
•   Fixed Path: Once the virtual circuit is established, all packets are sent along the same path, ensuring
consistent ordering and quality of service.
•   Packet Format: Packets include information about the virtual circuit identifier, allowing routers to
identify which virtual circuit they belong to.
Advantages:
•   Reliability: Since packets follow the same path, there is less variability in transmission time and
improved delivery order.
•   Quality of Service (QoS): Virtual circuits can provide guaranteed bandwidth and lower latency for
applications that require steady communication, like voice and video.
Disadvantages:
•   Setup Delay: Establishing a virtual circuit requires initial signaling, which can add delay before data 10
transmission begins.
•   Resource Allocation: Resources may be tied up for the duration of the session, which can be
inefficient if the circuit is underutilized.
Datagram Packet Switching
Concept:
•   Datagram packet switching is a connectionless method of transmitting data where each packet is
treated independently. Each packet can take a different path to reach the destination.
Characteristics:
• No Connection Establishment: There is no need to establish a dedicated path before sending
packets. Each packet is routed based on the destination address contained within it.
•   Independent Packets: Packets can arrive out of order, be duplicated, or even get lost during
transmission. Each packet is processed independently by routers.
•   Routing Flexibility: Packets may take different paths through the network, which can optimize
resource usage and increase resilience to failures.
Advantages:
•   Simplicity: No need for setup and teardown phases, allowing for immediate data transmission.
•   Efficiency: More flexible in handling varying traffic loads and can adapt quickly to network changes.
Disadvantages:
•   Unpredictable Delivery: Packets may arrive out of order, which can complicate data reconstruction
at the destination.
• Lack of QoS: It may not guarantee bandwidth or low latency, which can affect performance for real-
time applications.
Key Differences
********** 10 **********
--- page 11 ---
Feature   Virtual Circuit Switching   Datagram Packet Switching
Connection
Requires setup before transmission   No connection setup needed
Establishment
Fixed path for the duration of the Independent   routing   for each
Packet Routing
session   packet
Order of Delivery   Packets arrive in order   Packets may arrive out of order
Resource Allocation   Dedicated resources during session   Resources are shared dynamically
Quality of Service (QoS) Can provide guaranteed QoS   Limited or no QoS guarantees
Q6   Answer the following questions.   [20]
a.   Discuss the concept of layering in data communication and networking. Provide two examples where layering
architecture is used.
Answer:
The concept of layering in data communication and networking refers to the organization of communication
processes into separate layers, where each layer performs a specific function. This approach simplifies the
design, implementation, and troubleshooting of complex network systems by breaking them down into
manageable components. Each layer is responsible for specific tasks, and it interacts only with the layer
directly above or below it, following a set of predefined protocols.
Layering provides several benefits, including:
•   Modularity: Changes can be made to one layer without affecting the others, allowing for easier updates
and modifications.
•   Interoperability: Different hardware and software components from various vendors can work together
as long as they follow the same standards for communication.
•   Simplified Troubleshooting: Issues can be isolated and resolved within individual layers, making
problem-solving more efficient.
Examples of Layering Architecture
OSI (Open Systems Interconnection) Model
The OSI model is a conceptual framework used to understand and implement standard communication
between different network devices. It consists of seven layers:   10
•   Physical Layer: Deals with the transmission of raw data bits over a physical medium.
•   Data Link Layer: Handles error detection, correction, and frame synchronization.
•   Network Layer: Manages data routing, addressing, and packet forwarding.
•   Transport Layer: Ensures reliable data transfer and flow control.
•   Session Layer: Manages sessions or connections between applications.
•   Presentation Layer: Translates data into a format that can be processed by the application layer.
•   Application Layer: Provides network services to end-user applications (e.g., email, file transfer).
Each layer in the OSI model communicates with its corresponding layer in another network device, making it
a well-structured and modular approach to data communication.
TCP/IP (Transmission Control Protocol/Internet Protocol) Model
The TCP/IP model is the foundation of the internet and is widely used in modern networks. It has four layers:
•   Network Interface Layer: Corresponds to the physical and data link layers in the OSI model; handles
hardware-level communication.
•   Internet Layer: Maps to the network layer of the OSI model; deals with logical addressing and routing of
data packets.
•   Transport Layer: Ensures end-to-end communication and data transfer reliability (e.g., using TCP for
connection-oriented and UDP for connectionless communication).
•   Application Layer: Combines the functions of the OSI's session, presentation, and application layers;
deals with network services like HTTP, FTP, and SMTP.
The TCP/IP model's streamlined approach makes it practical for real-world implementation, focusing on
ensuring data delivery across different network architectures.
********** 11 **********
--- page 12 ---
These two examples, the OSI and TCP/IP models, demonstrate the use of layering architecture in data
communication, where each layer has specific responsibilities that contribute to the overall functionality of
network communication.
b.   A university campus wants to use IoT technology to manage energy consumption in its buildings and optimize
space utilization. What IoT solutions could be implemented to achieve these goals, and how can they help in
reducing operational costs?
Answer:
To manage energy consumption and optimize space utilization in a university campus using IoT technology,
several solutions can be implemented. These solutions will help improve efficiency, reduce operational costs,
and create a more sustainable environment. Here are some key IoT solutions that could be used:
1. Smart Lighting Systems
•   Solution: Install smart lighting systems with sensors that detect occupancy and natural light levels
in classrooms, labs, offices, and common areas.
• How It Helps: These systems can automatically adjust the lighting based on the presence of people
and daylight, reducing unnecessary energy usage and lowering electricity costs.
2. Smart Thermostats and HVAC Control
•   Solution: Use IoT-enabled thermostats and HVAC (Heating, Ventilation, and Air Conditioning)
systems that can be programmed and controlled remotely.
• How It Helps: These systems adjust temperature settings based on room occupancy and weather
conditions, ensuring energy-efficient heating and cooling. By maintaining optimal temperatures only
when spaces are in use, the university can significantly reduce its energy consumption.
3. Space Utilization Sensors
•   Solution: Install sensors in classrooms, study areas, and meeting rooms to monitor how often and
how long these spaces are used.
• How It Helps: The data collected from these sensors can help the university understand space usage
patterns and identify underutilized areas. This insight can lead to better space management, such as
repurposing unused areas or optimizing room bookings to maximize their use.
4. Energy Monitoring Systems
•   Solution: Deploy IoT energy monitoring systems that track the power consumption of various
devices and equipment in real time.
• How It Helps: By analyzing energy consumption data, the university can identify areas with high
energy usage and implement strategies to reduce it, such as scheduling equipment shutdowns when 10
not in use or replacing old appliances with more energy-efficient models.
5. Smart Plug and Power Management Systems
•   Solution: Use smart plugs and power management systems that can remotely control and monitor
connected devices like computers, printers, and other electrical appliances.
• How It Helps: These systems can automatically turn off devices that are not in use or during off-
hours, helping to reduce energy waste and lower utility bills.
6. Automated Building Management Systems (BMS)
•   Solution: Implement a centralized Building Management System that integrates all IoT devices for
lighting, HVAC, and other utilities.
• How It Helps: A BMS allows for real-time monitoring, control, and optimization of the building's
energy systems. It can automate responses to changes in occupancy or environmental conditions,
leading to reduced energy consumption and improved building efficiency.
7. Predictive Maintenance for Equipment
•   Solution: Use IoT sensors to monitor the performance of critical equipment, such as HVAC systems,
elevators, and electrical appliances, and detect any potential issues before they lead to failures.
• How It Helps: Predictive maintenance helps extend the lifespan of equipment and prevents costly
repairs or replacements. It also reduces downtime, ensuring that energy systems run more efficiently.
8. Smart Metering for Utilities
•   Solution: Install smart meters for electricity, water, and gas consumption to track usage patterns in
real time.
• How It Helps: By collecting detailed usage data, the university can identify peak consumption
periods and implement strategies to reduce usage during these times, leading to lower utility bills.
Benefits of Implementing IoT Solutions for Energy Management and Space Utilization:
1. Cost Savings: Automated control of energy systems and optimized space utilization can significantly
reduce operational costs, including lower utility bills and maintenance expenses.
2. Enhanced Efficiency: Real-time data from IoT devices enables quick decision-making and prompt
adjustments to optimize resource usage.
3.   Sustainability: Reduced energy consumption and optimized space use contribute to a more
sustainable campus, aligning with green initiatives and reducing the university's carbon footprint.
********** 12 **********
--- page 13 ---
4. Improved User Experience: Automated systems can create a comfortable environment for students
and staff by maintaining optimal lighting, temperature, and space conditions.
5. Data-Driven Decision Making: Insights from IoT data help in planning future campus expansions,
resource allocation, and space management strategies.
Q7   Answer the following questions.   [20]
a.   Discuss how the ability to share files and data improves communication in a networked environment.
Answer:
The ability to share files and data in a networked environment significantly enhances communication in
several ways:
1. Real-Time Collaboration: Networked environments allow multiple users to work on the same document
or project simultaneously. Tools like cloud storage and collaborative software (e.g., Google Workspace,
Microsoft 365) enable real-time editing and updates, facilitating faster decision-making and problem-
solving.
2.   Accessibility: Files and data can be accessed from anywhere within the network, allowing users to
retrieve and share information quickly. This reduces the delays associated with physical document sharing
and improves overall efficiency.
3. Centralized Information: Storing files on a centralized server ensures that all team members have access
to the latest versions of documents and data. This minimizes confusion and ensures everyone is on the
same page.   10
4. Streamlined Communication: Sharing files directly within communication platforms (like Slack or
Microsoft Teams) allows users to send relevant information quickly without needing to switch between
applications, reducing the time spent searching for files.
5. Improved Record Keeping: Networks often provide tools for version control and tracking changes. This
helps maintain a history of document edits, making it easier to review previous versions and understand
the evolution of projects.
6. Enhanced Data Security: Sharing files over a secure network can reduce the risks associated with
physical data loss or theft. Networked environments often include security protocols that protect sensitive
information during transmission.
7. Support for Remote Work: As remote work becomes more prevalent, the ability to share files and data
allows teams to maintain effective communication regardless of their physical location, supporting a
flexible work environment.
8. Integration with Other Tools: Networked environments often allow for integration with various
applications and services, enabling automated data sharing and reducing the manual effort required to
keep different systems updated.
b.   Discuss the functionality of each layer of the OSI model.
Answer:
The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the
functions of a telecommunication or computing system into seven layers. Each layer has a specific role in
handling various aspects of communication. Here's a breakdown of the seven layers, starting from the lowest
(Layer 1) to the highest (Layer 7):
1. Physical Layer (Layer 1)
•   Role: The physical layer is responsible for the physical connection between devices. It deals with the 10
transmission and reception of raw bit streams over a physical medium (such as cables, fiber optics,
or radio waves).
• Key Functions: Defines electrical, optical, mechanical, and procedural specifications for activating,
maintaining, and deactivating the physical link.
2. Data Link Layer (Layer 2)
•   Role: This layer is responsible for node-to-node data transfer and error detection and correction. It
ensures that data frames are transmitted accurately across a physical link.
• Key Functions: Organizes data into frames, manages error detection (using techniques like
checksums), and controls how data is accessed and transmitted on the network.
3. Network Layer (Layer 3)
********** 13 **********
--- page 14 ---
•   Role: The network layer is responsible for determining the best path for data to travel from the source
to the destination across multiple networks.
• Key Functions: Handles packet routing, logical addressing (such as IP addresses), and forwarding
data to the correct destination. It ensures that data is delivered even if there are multiple intermediate
nodes.
4. Transport Layer (Layer 4)
•   Role: This layer ensures reliable data transfer between devices, handling error recovery and flow
control. It establishes, maintains, and terminates communication sessions between devices.
• Key Functions: Manages end-to-end communication, segmenting data into smaller units for easier
transmission (segments) and ensuring complete data delivery using protocols like TCP
(Transmission Control Protocol) and UDP (User Datagram Protocol).
5. Session Layer (Layer 5)
•   Role: The session layer manages and controls the connections between computers, establishing,
maintaining, and terminating communication sessions.
• Key Functions: Provides dialog control between devices, organizing communication into sessions
to keep track of different streams of data and recover from any interruptions.
6. Presentation Layer (Layer 6)
•   Role: This layer translates data between the application layer and the network. It ensures that data
sent by the application layer of one system is readable by the application layer of another system.
• Key Functions: Handles data encryption, decryption, data compression, and data format translation
(e.g., converting file formats).
7. Application Layer (Layer 7)
•   Role: The application layer is the closest layer to the end user and interacts directly with software
applications that use communication services.
• Key Functions: Provides network services to applications, such as email, file transfer, and web
browsing. It enables end-users to access network resources through various protocols like HTTP,
FTP, SMTP, and others.
********** 14 **********
````
