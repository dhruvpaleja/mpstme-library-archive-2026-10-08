# Networks and Telecommunications: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper d8101eab50fc

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7011/Networks and Telecommunications/ANS_Networks and Telecommunications(702EX0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 May 2026
- Text: mixed (15 pages), mean OCR confidence 89.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Networks and Telecommunications
Date: 13 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q.1   Answer Briefly   Marks
CO 1; A   Explain the five key aspects of computer networking.   [5]
SO 1;
BL 2   Explanation – 5marks
• Network Applications and Network Programming
• Data Communications
•   Packet Switching and Networking Technologies
•   Internetworking With TCP/IP
•   Additional Networking Concepts and Technologies
CO 2; B What are the main motivations behind data communication system design?   [5]
SO 1;
BL 1   Explanation of Motivation – 5 marks
CO 3; C What is a BSS in wireless LAN? Distinguish Infrastructure mode from Ad hoc mode.   [5]
SO 1;
BL 2   Definition BSS- 2marks
Differences – 3marks
********** 1 **********
--- page 2 ---
CO 4; D   Define internetworking. Why is heterogeneity a challenge in networking?   [5]
SO 1;   Defintion – 2 marks
BL 1   Heterogeneity and challenge – 3 marks
Internetworking - A router can interconnect networks that use different technologies,
including different
media and media access techniques, physical addressing schemes, or frame formats
Heterogeneity
Incompatibilities among networks exist.
There are different:
•Electrical properties
•Signaling and data encoding
•Packet formats
•Physical Addresses
Attempt Any Four
Q.2
CO 1; A   Explain the five layers of the TCP/IP model with one protocol example per layer. Draw   [10]
SO 1;   the complete structure diagram.
BL 2
Diagram – 3 marks
Each layer description- 5 marks
Protocols at each layer – 2marks
********** 2 **********
--- page 3 ---
Layer 1: Physical
Protocols in the Physical layer specify details about the underlying transmission
medium and the associated hardware. All specifications related to electrical properties,
radio frequencies, and signals belong in layer 1.
Layer 2: Network Interface
Protocols in the Network Interface layer specify details about communication
between higher layers of protocols, which are usually implemented in software, and the
underlying network, which is implemented in hardware. Specifications about network
addresses and the maximum packet size that a network can support, protocols used to
access the underlying medium, and hardware addressing belong in layer 2.
Layer 3: Internet
Protocols in the Internet layer form the fundamental basis for the Internet. Layer 3
protocols specify communication between two computers across the Internet (i.e., across
multiple interconnected networks). The Internet addressing structure, the format of
Internet packets, the method for dividing a large Internet packet into smaller packets for
transmission, and mechanisms for reporting errors belong in layer 3.
Layer 4: Transport
Protocols in the Transport layer provide for communication from an application
program on one computer to an application program on another. Specifications that
control the maximum rate a receiver can accept data, mechanisms to avoid network
congestion, and techniques to insure that all data is received in the correct order belong in
layer 4.
Layer 5: Application
Protocols in the top layer of the TCP/IP stack specify how a pair of applications
interact when they communicate. Layer 5 protocols specify details about the format and
meaning of messages that applications can exchange as well as procedures to be followed
during communication. Specifications for email exchange, file transfer, web browsing,
telephone services, and video teleconferencing all belong in layer 5.
CO 4; B   Explain in detail the classful IP addressing with class of IP address and its limitations.   [10]
SO 1;
BL 2   Classful IP address – 7 marks
Limitations – 3marks
********** 3 **********
--- page 4 ---
The problem with this classful addressing method is that millions of class A addresses are
wasted, many of the class B addresses are wasted, whereas, number of addresses
available in class C is so small that it cannot cater to the needs of organizations. Class D
addresses are used for multicast routing and are therefore available as a single block only.
Class E addresses are reserved. Since there are these problems, Classful networking was
replaced by Classless Inter-Domain Routing (CIDR).
Q.3
CO 1; A   Explain Hypertext Transfer Protocol (HTTP) along with the request types and response   [10]
SO 1;   structure.
BL 2
Explanation with characteristics – HTTP –4 marks
Request types – 4 marks, response – 2 marks
********** 4 **********
--- page 5 ---
CO 2; B What is a frame. Explain framing in serial communication and how byte stuffing works.   [10]
SO 1;
BL 2   Definition of frame – 2 marks
Framing in serial communication – 3 marks
Byte stuffing and its working – 5 marks
********** 5 **********
--- page 6 ---
Framing And Serial Communications Systems

e Consider sending packets over a leased circuit

e Circuit hardware either provides a stream of bits or a stream
of bytes (characters)

e We will consider hardware that provides a byte stream
— No frame boundaries
— Any 8-bit value can appear in the data

e How can we send packets over such a system?

e Answer: sender and receiver must agree on framing

Example Framing Used With A Leased Circuit

e Use SOH and EOT characters to mark the start and end of a
frame

6 bytes arbitrary bytes

SOH HEADER PAYLOAD EOT

e Use byte stuffing within the payload

| Byte In Payload | Sequence Sent |

SOH ESC A
EOT ESC B

Illustration Of Byte Stuffing

original data

=| Fl sl Jee

C

x x_+ id y \ \ \

| esc| c | Jesc| A | [esc] B Jesc| c | |

stuffed data

e Internet uses SLIP or PPP (standards) for transmission over
serial circuits

e Bit stuffing techniques are also available for systems that
transfer a stream of bits

FIC 6 I HF
--- page 7 ---
Q.4
CO 2; A   Explain the main sources of transmission errors in data communications. Explain   [10]
SO 1;   Shannon's Theorem and show with an example how the signal-to-noise ratio relates to
BL 2   error reduction.
Sources of transmission error- 3 marks
Shannon’s theorem and example – 4 marks
S/N relation to error reduction – 3 marks
There are three main categories of transmission errors:
Interference
–electromagnetic radiation emitted from devices such as electric motors and background
cosmic radiation can cause noise that can disturb radio transmissions and signals
traveling across wires
Distortion
–All physical systems distort signals
–As a pulse travels along an optical fiber, the pulse disperses
–Wires have properties of capacitance and inductance
•that block signals at some frequencies while admitting signals at other frequencies
–Placing a wire near a large metal object can change the set of frequencies that can pass
through the wire
–Metal objects can block some frequencies of radio waves, while passing others
Attenuation
–As a signal passes across a medium, the signal becomes weaker
•signals on wires or optical fibers become weaker over long distances, just as a radio
signal becomes weaker with distance
********** 7 **********
--- page 8 ---
CO 4; B   Explain the process of fragmentation and reassembly with reference to the MTU concept.   [10]
SO 1;   Why is reassembly done at the destination and not at intermediate routers? Why
BL 2   Fragmenting a fragment is performed.
Fragmentation and reassembly – 6 marks
Reassembly at destination reason – 2 marks
Fragmenting a fragment – 2marks
********** 8 **********
--- page 9 ---
Q.5
CO 1; A   Explain the Client-Server model. How is a server identified using IP address and port   [10]
SO 1;   number.
BL 2
Client server model- 4 marks
Server identification – 4 marks
Diagram – 2 marks
********** 9 **********
--- page 10 ---
CO 2; B Draw and explain the conceptual framework of a data communication system.   [10]
SO 1;
BL 2   Diagram- 4 marks
Explain of each component of transmitter and receiver side – 6 marks
Information Sources
–The source of information can be either analog or digital
–Important concepts include characteristics of signals, such as amplitude, frequency, and
phase, and classification as either periodic or aperiodic
********** 10 **********
--- page 11 ---
–The subtopic focuses on the conversion between analog and digital representations of
information
Source Encoder and Decoder
–Once information has been digitized, digital representations can be transformed and
converted
–Concepts include data compression and consequences for communications
Encryptor and Decryptor
–To protect information and keep it private, the information can be encrypted (i.e.,
scrambled) before transmission and decrypted upon reception
–Concepts include cryptographic techniques and algorithms
Channel Encoder and Decoder
–Channel coding is used to detect and correct transmission errors
–Topics include methods to detect and limit errors
–Practical techniques like parity checking, checksums, and cyclic redundancy codes that
are employed in computer networks
Multiplexor and Demultiplexor
–Multiplexing refers to the way information from multiple sources is combined for
transmission across a shared medium
–Concepts include techniques for simultaneous sharing as well as techniques that allow
sources to take turns when using the medium
Modulator and Demodulator
–Modulation refers to the way electromagnetic radiation is used to send information
–Concepts include both analog and digital modulation schemes
–Devices known as modems that perform the modulation and demodulation
Physical Channel and Transmission
–transmission media
–transmission modes, such as serial and parallel
–channel bandwidth
–electrical noise and interference
–channel capacity
Q.6
CO 2; A   Explain random access protocol with all types and their working.   [10]
SO 1;
BL 2   Types –2 marks
Description and working of each protocol – 6 marks
Diagram – 2 marks
********** 11 **********
--- page 12 ---
Type Description

ALOHA Historic protocol used in an early radio network in
Hawaii; popular in textbooks and easy to analyze,
but not used in real networks

CSMA/CD | Carrier Sense Multi-Access with Collision Detection
The basis for the original Ethernet, and the most widely
used random access protocol

CSMA/CA | Carrier Sense Multi-Access with Collision Avoidance
The basis for Wi-Fi wireless networks

Used in early network in Hawaii (ALOHAnet)
Two carrier frequencies, inbound and outbound

Central transmitter rebroadcast each incoming packet

outbound frequency =|
—

—
inbound frequency

central

——_~ ransmitter

outlying station

If inbound packets collide, each sender waits a random time
and retransmits

Channel utilization under 20%

CSMA/CD

e Used in original Ethernet (1973)
e Provides access to shared medium
e Principle features

— Carrier Sense (CS)

— Multiple Access (MA)

— Collision Detection (CD)

e Uses binary exponential backoff

FRR ICR] DA KH
--- page 13 ---
CO 4; B What is Realtime Multimedia? Explain the concept of delayed playback and Jitter Buffers   [10]
SO 1;   with a suitable diagram.
BL 2
Realtime Multimedia- 4 marks
concept of delayed playback and Jitter Buffers- 4 marks
Diagram – 2marks
Real-Time Data Transmission And Best-Effort Delivery
Multimedia data is audio and/or video, possibly mixed with text.
Realtime Multimedia is multimedia that has to be reproduced at the same rate it was
captured.
The question arises how the mere best-effort service underlying the Internet can reliably
deliver such services as realtime multimedia.
Protocols for realtime multimedia are concerned mainly with dealing with jitter, so that
playback will be smooth. There's seldom any point in performing retransmission, since
packets that arrive significantly late are too late to be included in playback.
Delayed Playback and Jitter Buffers
********** 13 **********
--- page 14 ---
The receiver of realtime multimedia for playback typically utilizes timestamps of some
kind to assure the content is played in the correct order.
To achieve smooth playback, a receiver may delay the playback of the contents of the
initial packet, so that a certain number of packets can accumulate in an input buffer called
a jitter buffer.
From then on, the receiver plays content from the buffer at a constant rate.
Due to jitter, the number of items in the buffer may vary significantly over time.
However, as long as the jitter is not too extreme, the item that has to be played next will
always be in the buffer.
Q.7
CO 1; A Compare the Stream Paradigm and the Message Paradigm of Internet communication.   [5]
SO 1;
BL 2   Comparison – 2.5 marks each
CO 3; B   List and explain PAN technologies with their data rates and use cases.   [5]
SO 1;
BL 2   Types – 3marks
Data rates and use cases – 1 mark each
********** 14 **********
--- page 15 ---
Bluetooth – 3Mbps – Audio straming, file/image transfer
InfraRed – 4Mbps – Remote control
ZigBee- 250 kbps – Home Automation
CO 4; B   Explain IP Telephony (VoIP). Compare SIP and H.323 as VoIP signaling protocols. List   [10]
SO 1;   key differences.
BL 1
IP telephony – 4marks
SIP and H.323 – 3 marks
IP Telephony
•   IP Telephony aka Voice over IP (VoIP) is the practice of transmitting voice
conversations over the Internet.
• Much of the motivation is economic: it is cheaper to set up Internet routers and
networks than a system of telephone switches, and it is simpler to use the Internet
for both voice and data than to have separate systems.
• Although the basic idea of VoIP is simple, there are significant obstacles to
implementation, especially the difficulty of making it backward compatible with
the Public Switched Telephone Network (PSTN).
•   Challenges include: real-time processing constraints; call setup and termination;
dialing; translation of telephone numbers into IP addresses; call acceptance and
answering; 'patching through' among Internet, cellular system, and PSTN
systems; and implementing call forwarding, call waiting, voice mail, conference
calls, caller ID, and PBX features.
SIP Characteristics and Methods
• SIP operates at the application layer
• SIP does signaling
• SIP provides services like call-forwarding
• SIP uses multicast for conference calls
• SIP allows the two sides of a call to negotiate capabilities, media, and parameters.
• A SIP Uniform Resource Identifier (URI) contains a user name and domain name,
for example
sip:smith@somecompany.com
• SIP defines six basic message types called methods and seven extensions.
H.323 Characteristics
• H.323 protocols work together to handle:
o   all aspects of digital telephone calls
o   signaling to set up and manage calls
o transmission of video and data during voice calls
o binary messages
o   security protocols
o Multipoint Control Unit hardware for conference calls
o   servers for tasks such as phone number to IP address
translation, authentication, authorization, and accounting.
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper ac9fae2d94f2

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CSE_DS_7011/Networks and Telecommunications/ANS_Networks and Telecommunications(702EX0C023)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2026
- Text: mixed (16 pages), mean OCR confidence 87.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Networks and Telecommunications
Date: 09 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q.1   Answer Briefly   Marks
CO 1; A Explain the concept of resource sharing for computer networks. How did ARPA plan to address   [5]
SO 1;   the high cost of computers through networking.
BL 2
Resource sharing – 3 marks
ARPA vision – 2marks
CO 2; B What is the essence of data communications. Why must information be digitized before   [5]
SO 1;   transmission.
BL 1
Essence – 2 marks
Digitized information – 3marks
Essence –
********** 1 **********
--- page 2 ---
Involves the transmission of information over physical media
•The subject draws on ideas about electric current, light, and other forms of electromagnetic
radiation
•Information is digitized and digital data is transmitted
•Data communications uses mathematics and includes various forms of analysis
–Goal is to develop practical ways to design and build transmission systems
Information is digitized before transmission—converted from continuous analog signals
(voice, video, physical documents) into discrete binary code (0s and 1s)—primarily to ensure
reliable, high-speed, and error-resistant communication. Digital data allows for efficient error
detection/correction, significant noise reduction, compact storage, and high-speed transmission
over networks.
CO 3; C Explain the concept of frequency assignment in cellular networks. What is a 7-cell cluster in   [5]
SO 1;   cellular networks? How does it prevent co-channel interference?
BL 2
Frequency assignment – 2 marks
Cell cluster – 2 marks
Prevention – 1 mark
********** 2 **********
--- page 3 ---
CO 4; D What is the goal of internetworking? List the five properties an ideal internet communication   [5]
SO 1;   system should have.
BL 1
Goal – 2 marks
Properties – 3marks
Internetworking create a communication system that is:
•Seamless
•Uniform
•General-purpose
•Universal
•Hides heterogeneity from the user
Attempt Any Four
Q.2
CO 1; A Explain the concept of nested protocol headers using a suitable diagram. How does data travel   [10]
SO 1;   through TCP/IP layers during communication?
BL 2
Nested protocol header – Explanation 3 marks
Diagram – 2 marks
Data communication – Explanation – 3 marks
Diagram- 2marks
********** 3 **********
--- page 4 ---
To understand how protocols operate, consider two computers connected to a network. Figure 1.2
illustrates layered protocols on the two computers. As the figure shows, each computer contains a
set of layered protocols. When an application sends data, the data is placed in a packet, and the
outgoing packet passes down through each layer of protocols. Once it has passed through all
layers of protocols on the sending computer, the packet leaves the computer and is transmitted
across the underlying physical network†. When it reaches the receiving computer, the packet
passes up through the layers of protocols. If the application on the receiving computer sends a
response, the process is reversed. That is, a response passes down through the layers on its way
out, and up through the layers on the computer that receives the response
CO 4; B Discuss the MTU (Maximum Transmission Unit) in detail. Explain fragmentation and reassembly   [10]
SO 1;   with a worked example involving three networks with MTUs of 1500, 1000, and 532 bytes.
BL 2
MTU – 3 marks
Fragmentation and reassembly – 5 marks
Example explanation – 2marks
********** 4 **********
--- page 5 ---
Fragmentation & Reassembly

When a datagram is larger than the MTU of the network over which it must be sent,
the router divides the datagram into smaller pieces called fragments, and sends each
fragment independently.

* The fragments have the same format as other datagrams.

¢ The FLAG field contains a bit that means the datagram is a fragment.

* Other fields in the header contain information that allows the fragments to be
reassembled.

¢ Each fragment has a copy of the original header with fields modified as necessary.

|PHeadet _ original datagram data area __|

[IP Hdri] data1 | [IP Hdr2| data2 [IP Hdr 3] data3_ |

Reassembly
The process of creating the original datagram from the fragments is called reassembly.

Note: The final fragment has a special bit set in the header to signal that all fragments
have arrived successfully.

The Internet Protocol specifies that the ultimate destination host should reassembly
the fragments.

Two advantages to reassembly at the destination:
* Reduces the amount of information in each router.

¢ It allows the routes to change dynamically.

In the figure, H, will perform reassembly. R, will simply forward the fragments.

T" i
R, Ra

Net 1 (MTU=1500) —t}— _ Net 2 (MTU=1000) ——+1}+—_ Net 3 (MTU=1500)

Fragmenting a Fragment

¢ Ifthe MTU ofa subsequent network is smaller than the one that caused
fragmentation, the fragments must be fragmented further.

¢ The IP fragmentation scheme allows this fragmentation with all fragments still
being treated in exactly the same way.

Example:

1 i
Ry R,

Net 1 (MTU=1500) ——(}+— Net 2(MTU=1000) ——C}H—~ Net 3 (MTU: 532 |

FIC DI EH ar
--- page 6 ---
Q.3
CO 1; A Explain the purpose of HTML, URL, and HTTP as three key standards of the WWW. Explain the   [10]
SO 1;   general structure and the components of the URL.
BL 2
Purpose of each – 1 mark
Explanation - URL general structure – 3 marks
Components – 4 marks
CO 2; B Explain in detail the types of networks belong to the categories of packet switched networks.   [10]
SO 1;
BL 2   Explanation – 6 marks
Diagrams – 4 marks
********** 6 **********
--- page 7 ---
Q.4
CO 2; A Draw and explain the conceptual framework of a data communication system.   [10]
SO 1;
BL 2   Diagram- 4 marks
Explain of each component of transmitter and receiver side – 6 marks
Information Sources
–The source of information can be either analog or digital
–Important concepts include characteristics of signals, such as amplitude,frequency,and phase,
and classification as either periodic or aperiodic
–The subtopic focuses on the conversion between analog and digital representations of
information
Source Encoder and Decoder
–Once information has been digitized, digital representations can be transformed and converted
–Concepts include data compression and consequences for communications
Encryptor and Decryptor
–To protect information and keep it private, the information can be encrypted (i.e., scrambled)
before transmission and decrypted upon reception
–Concepts include cryptographic techniques and algorithms
********** 7 **********
--- page 8 ---
Channel Encoder and Decoder
–Channel coding is used to detect and correct transmission errors
–Topics include methods to detect and limit errors
–Practical techniques like parity checking, checksums, and cyclic redundancy codes that are
employed in computer networks
Multiplexor and Demultiplexor
–Multiplexing refers to the way information from multiple sources is combined for transmission
across a shared medium
–Concepts include techniques for simultaneous sharing as well as techniques that allow sources to
take turns when using the medium
Modulator and Demodulator
–Modulation refers to the way electromagnetic radiation is used to send information
–Concepts include both analog and digital modulation schemes
–Devices known as modems that perform the modulation and demodulation
Physical Channel and Transmission
–transmission media
–transmission modes, such as serial and parallel
–channel bandwidth
–electrical noise and interference
–channel capacity
CO 4; B Why UDP is a connectionless protocol. Explain UDP frame format in detail along with the   [10]
SO 1;   encapsulation process.
BL 2
Connectionless – 3 marks
UDP frame format – 3 marks
Encapsulation – 2marks
Diagram – 2 marks
UDP frame format
********** 8 **********
--- page 9 ---
UDP Encapsulation
Q.5
CO 1; A How does a concurrent server use threads to handle multiple clients? Explain circular   [10]
SO 1;   dependencies among server.
BL 2
Explanation – concurrent server – 5marks
Circular dependencies- 5marks
********** 9 **********
--- page 10 ---
CO 2; B Explain the two strategies for handling channel errors? Define dataword, codeword, and   [10]
SO 1;   codebook using (n, k) notation with an example.
BL 2
Explanation of strategies- 3 marks each
Definition with example of codebook – 4 marks
********** 10 **********
--- page 11 ---
Q.6
CO 2; A Explain the frame format used in ethernet technology. Why ethernet address filtering is   [10]
SO 1;   performed and how frame demultiplexing is done.
BL 2
frame format- 3marks
address filtering – 3 marks
frame demultiplexing – 2 marks
diagrams – 2marks
********** 11 **********
--- page 12 ---
e Invented at Xerox PARC in 1973
e Standardized by Digital, Intel, and Xerox (DIX) in 1978

e Frame has a 14-byte header followed by payload of 46 to
1500 bytes

e Frame format and addressing have survived virtually
unchanged

| header 46 - 1500 bytes of payload | |

—, LO f
a — 4-byte eRe

6-byte
destination address

6-byte
source address

2-byte

type | header details

Ethernet Address Filtering
e Recall: station accepts a copy of the frame if destination
address matches
— The station’s unicast address
— The broadcast address (all 1s)
— A multicast address to which station is listening
e Other frames are ignored

e Promiscuous mode allows a station to receive all frames
regardless of address

— Basis of protocol analyzer software such as Wireshark

Illustration Of Frame Demultiplexing

IPy4 IPv6
module

module
0800 86DD

frame
‘arrives

demultiplexing

e Performed when frame arrives
e Usually handled by protocol software

e Frame type field examined and frame passed to appropriate
protocol module; unrecognized types are discarded

FRR ICR] DA KH
--- page 13 ---
CO 4; B Explain the concept of Content Caching and Web Load Balancers. How do they help scalable   [10]
SO 1;   Internet services?
BL 2
Content caching and web load balancer- 3 marks each
Help in Scalable internet – 4 marks
Content Caching (Akamai)Some companies offer a distributed caching service.
For example, Akamai has a set of servers all over the Internet.
An organization can pay Akamai for the privilege of pre-loading Akamai server caches with
theorganization's web pages.
Links on the organization's web site direct customer clicks to Akamai server content.
The organization is allowed to send updates of their 'content' to the Akamai caches.
The scheme reduces load on the servers of the organization.
Web Load Balancer
Web server optimization gets a lot of attention because businesses rely on the web to make sales.
A load balancer is a device that distributes incoming requests among multiple computers running
identical web servers.
Typically the servers share the same customer database.
The load balancers have the ability to direct a series of requests from the same source to the same
server.
Server Virtualization
Some systems support process migration - the capability of an executing program to move to
another computer.
Given infrastructure for process migration, it is possible for a server on an overloaded machine to
move to another machine where resources like CPU time are in more plentiful supply.
Peer-to-Peer Communication
P2P is a technology used to increase the speed of file downloads.
Clients fetch pieces of the file.
Various servers all over the Internet have various pieces of the file.
Clients try to fetch pieces from nearby servers.
Clients agree to be servers for the pieces of the file they have downloaded.
Well-known examples were created mainly for downloading music files: e.g. Napster & Kazaa
Distributed Data Centers and Replication
Google gets so much traffic that it has resorted to another approach.
********** 13 **********
--- page 14 ---
When a browser connects with DNS to resolve the name www.google.com, different IP numbers
are 'suggested' at different times.
This has the effect of balancing the load over multiple Google data centers distributed in various
geographic locations.
Q.7
CO 1; A What is connection-oriented communication. How two applications communicate over it.   [5]
SO 1;
BL 1   connection-oriented communication- 3marks
Communication – 2marks
CO 3; B Briefly explain the principle of fiber modem, repeater and the bridge.   [5]
SO 1;
BL 2   Explanation – 3 marks
Diagram – 2 marks
********** 14 **********
--- page 15 ---
CO 4; B Define multimedia and explain the best-effort delivery mechanism of the Internet. How RTP is   [10]
SO 1;   useful in handling the delay.
BL 2
Definition – 2 marks
Best effort delivery – 2 marks
RTP – 3 marks
Diagram – 2marks
Multimedia data is audio and/or video, possibly mixed with text.
Realtime Multimedia is multimedia that has to be reproduced at the same rate it was captured.
The question arises how the mere best-effort service underlying the Internet can reliably deliver
such services as realtime multimedia.
Protocols for realtime multimedia are concerned mainly with dealing with jitter, so that playback
will be smooth. There's seldom any point in performing retransmission, since packets that arrive
significantly late are too late to be included in playback.
Real-Time Transport Protocol
Real-Time Transport Protocol (RTP) is an application layer protocol for transfer of realtime data.
********** 15 **********
--- page 16 ---
The RTP header has sequence number, timestamp, and source identifier fields that help
thereceiver implement the functionality of a jitter buffer.
RTP fields also provides support for video encodings that send incremental changes after a full
frame,
multiple senders to a multicast address, and the mixing of multiple streams by intermediate
systems.
********** 16 **********
````

## 2024-25 · Final-Exam · Sem 6 · Answer key · paper 7c09c1b6e88a

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_06/Final-Exam/BTech_CSE_DS_7011/Networks and Telecommunications/ANS_Networks and Telecommunications(702EX0C023)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2025
- Text: mixed (16 pages), mean OCR confidence 90.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2024-2025)
Subject: Networks and Telecommunications
Date: 07 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 16 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 1;   a. What is the role of server identification and demultiplexing in network communication?   [5]
SO- 1;
BL-1
Explanation -5M
********** 1 **********
--- page 2 ---
CO- 2;   b. What are ways of representing the signals along with the diagram of each.   [5]
SO-1;
BL-1
Explanation of all signals with diagram – 5M
Analog and Digital signal
Periodic and Aperiodic signal – sin waves and its characteristics
Composite signal
CO- 3;   c. What is Infrastructure Mode and Ad Hoc Mode. Give their advantages and [5]
SO-1;   disadvantages.
BL-1
Definition -3M
Advantage and Disadvantage – 2M
Infrastructure mode:
********** 2 **********
--- page 3 ---
Advantages:
Centralized control improves security and management.
Allows connection to wired networks (Internet, servers).
Supports roaming, where devices switch between APs for seamless
connectivity.
Disadvantages:
Requires an Access Point (AP), adding cost.
Single point of failure – if the AP fails, all devices lose connection.
Less efficient for direct device-to-device communication.
Ad Hoc Mode
Advantages:
No need for an Access Point – simple and cost-effective.
Useful in emergency situations or temporary networks.
Ideal for small and short-range device-to-device communication.
Disadvantages:
Limited range – devices must be close to each other.
No centralized control, making network management difficult.
No Internet access unless one device shares its connection.
CO- 4;   d. How to identifying a class of IP address. Is this method still recognized.   [5]
SO-1;
BL-1
Explanation of IP address- 4M
Reasoning -1M
An IP address is a unique identifier assigned to devices in a network. Traditionally, IPv4
addresses (32-bit) were classified into five classes (A, B, C, D, E) based on the first few
bits of the address. This method is known as classful addressing.
No, classful addressing is outdated and has been replaced by CIDR (Classless
Inter-Domain Routing). CIDR notation (e.g., 192.168.1.0/24) is used instead
of fixed-class boundaries.
Q2   a.   Explain the principle of executing the multiple applications at the same time?   [5]
********** 3 **********
--- page 4 ---
CO-1;   Discuss the importance of Concurrent Servers and explain how they handle multiple   [5]
SO-1;   client requests simultaneously.
BL-2
Explanation of each with diagram – 5M
• A concurrent server can handle multiple client requests simultaneously
by using multiple threads or processes.
•   Instead of handling requests sequentially (one at a time), a concurrent
server allows parallel execution.
• This improves performance, reduces waiting time, and ensures
efficient resource utilization.
• Example: A web server like Apache creates separate threads for each
incoming HTTP request.
Q2   b.   Illustrate and Explain Different LAN Topologies. Show the advantages and   [10]
disadvantages of each topology with examples.
CO-2;
SO-1;
BL-2
Explanation -6M
Diagram – 2M
Advantage and disadvantage-2M
********** 4 **********
--- page 5 ---
Q3   a.   Demonstrate the conceptual pieces of communication System with neat labelled   [10]
diagram.
CO- 2;
SO-1;
BL-2
Diagram -4M
Explanation -6M
********** 5 **********
--- page 6 ---
Q3   b.   Explain the working of a router in detail, including its functions and routing tables.   [10]
Provide a suitable example.
CO- 4;
SO-1;
BL-2,2
Explanation – 6M
Router example with roouting table and forwarding – 4M
********** 6 **********
--- page 7 ---
Q4   a.   In which way the web protocols standards being used. How well they are effective in   [10]
services used in the internet.
CO- 1;
SO-2;
BL-2
Categories of web protocol -3M
Explanation of any 2 – 6M
Effectiveness – 1M
********** 7 **********
--- page 8 ---
Q4   b.   (i) Explain the block codes and the convolution error codes and its utilization.   [5]
CO-2;
SO-2;
BL-3   Explanation-2M each
Utilization – 1M
********** 8 **********
--- page 9 ---
(ii) A sender wants to transmit a 4-bit data 1101 using the CRC generator polynomial
P(x)=x3+x+1. Find the CRC codeword that will be transmitted.
Representation of bits and divisor – 1 M
Addition od zeros – 1M
Complete solution – 3M
The transmitted CRC codeword is 11010101.
[5]
Q5   a.   Classify the random-access Protocols in Networking. Explain their working   [10]
principles and how they facilitate multiple access communication.
CO-2;
SO-1;
BL-2
Classification – 3M
Explanation – 6M, Diagram -1M
********** 9 **********
--- page 10 ---
Used in early network in Hawaii (ALOHAnet)
Two carrier frequencies, inbound and outbound

Central transmitter rebroadcast each incoming packet

ee ee

inbound frequency

central
transmitter

——— outlying station

If inbound packets collide, each sender waits a random time
and retransmits

Channel utilization under 20%

CSMA/CD Algorithm

Method:

When a packet is ready, perform CS (wait for access);

Delay for the interpacket gap;

Set variable x to the standard backoff range, d;

Attempt to transmit the packet and perform CD;

While (collision occurred during transmission) {
Choose q to be a random delay between O and x;
Delay for q microseconds;

Double x in case needed for the next round;
Attempt to retransmit the packet and perform CD;

FRR ICR 7 OI HOH
--- page 11 ---
Q5   b.   Explain the concept of the following:   [10]
CO-4;   (i) Distributed data centers and replication
SO-1;   (ii) Universal representation
BL-2   (iii) Mobility and wireless networking
Explanation of each -3M
Diagram-1M
•   Distributed Data Centers and Replication
o Google gets so much traffic that it has resorted to another approach.
o When a browser connects with DNS to resolve the name
www.google.com, different IP numbers are 'suggested' at different
times.
o This has the effect of balancing the load over multiple Google data
centers distributed in various geographic locations.
•   Universal Representation (XML)
o XML allows programmers to choose arbitrary tags so the documents
can be understood by multiple applications.
o Documents can include a style sheet that specifies legitimate document
structure.
o Uses:
▪ on interface between web server and database
▪   load balancers parsing XML
********** 11 **********
--- page 12 ---
▪ XML controlling downloads in mobile devices
▪ XML representing specifications used by network management
systems
•   Mobility and Wireless Networking
o Users now expect to be connected continuously to the Internet.
o Wireless technologies receive a lot of attention and are targeted for
rapid development.
o Mobile phone networks are converging with the Internet.
o Mobile computer users rely on WiFi and Virtual Private Networks
(VPN)
Q6   a.   Explain the purpose of protocol header in TCP/IP protocol suite? How it could be   [10]
updated while connecting from sender to receiver or vice a versa. Will it have any
CO-1;
relation with the network interoperability.
SO-1;
BL-2
Explanation of each part -2M
Diagram – 4M
********** 12 **********
--- page 13 ---
The protocol header plays a vital role in network interoperability by ensuring
that devices from different vendors and networks can communicate effectively.
This is achieved through:
• Standardization – The TCP/IP protocol suite follows universally
accepted standards (e.g., IETF RFCs), allowing different networks and
devices to understand and process headers correctly.
• Backward Compatibility – Older and newer devices can still
communicate as long as they follow the same header format.
•   Interoperability with Different Networks – Whether it’s a wired
Ethernet network, a wireless Wi-Fi connection, or a mobile LTE
network, the TCP/IP headers enable seamless data transfer.
• Protocol Adaptability – Network devices like gateways can translate
between different protocols while preserving key header information.
Q6   b. A packet is sent from a host with IP 30.0.5.20 to a destination 192.4.10.200.   [10]
Answer the following:
CO-4;
SO-1;   (i) Identify the first hop at Router R₁ and justify your answer based on the
BL-3   routing table.
(ii) Determine the next hop when the packet reaches Router R₂.
(iii)Does Router R₃ deliver the packet directly, or does it require further
forwarding? Explain.
(iv) Suppose the subnet mask for the 192.4.10.0 network is changed from /24
to /26. Would Router R₃ still deliver the packet directly? Why or why
not?
Solution
(i)   3 M
(ii)   3 M
(iii)   2 M
(iv)   2 M
Step 1: Forwarding Decision at Router R₁ (3 Marks)
• The source IP 30.0.5.20 belongs to 30.0.0.0/8.
• The destination 192.4.10.200 does not match any directly connected
networks at R₁.
********** 13 **********
--- page 14 ---
• The routing table of R₁ specifies that traffic for 30.0.0.0/8 should be
forwarded to 40.0.0.7.
• Answer: The packet is forwarded to 40.0.0.7.
Step 2: Forwarding Decision at Router R₂ (3 Marks)
• The packet reaches Router R₂.
• The destination 192.4.10.200 falls under 192.4.10.0/24, which is routed
via 128.1.0.9.
• Answer: The packet is forwarded to 128.1.0.9.
Step 3: Forwarding at Router R₃ (2 Marks)
• The packet arrives at Router R₃, which has a directly connected network
192.4.10.0/24.
•   Since 192.4.10.200 is part of this network, the router delivers the packet
directly.
• Answer: The packet is delivered directly by Router R₃.
Step 4: Impact of Changing Subnet Mask to /26 (2 Marks)
•   If the subnet mask changes from /24 (255.255.255.0) to /26
(255.255.255.192), the addressable range changes:
o 192.4.10.0/26: 192.4.10.0 - 192.4.10.63
o 192.4.10.64/26: 192.4.10.64 - 192.4.10.127
o 192.4.10.128/26: 192.4.10.128 - 192.4.10.191
o 192.4.10.192/26: 192.4.10.192 - 192.4.10.255
•   192.4.10.200 falls into the 192.4.10.192/26 subnet.
•   If Router R₃ only has 192.4.10.0/26, it does not cover 192.4.10.200, and
additional routing is needed.
• Answer: If R₃ does not have a route for 192.4.10.192/26, it cannot
deliver directly, and the packet may be dropped or require another hop.
Q7   a. What are the key aspects of networking that data communications cover? Provide   [5]
relevant examples.
CO-1;
SO-1;
BL-1
Explanation – 3M
Example -2M
********** 14 **********
--- page 15 ---
Q7   b.   Explain the concept of cellular structure in mobile communication. How does   [5]
frequency reuse help in optimizing network performance.
CO-3;
SO-1;
BL-1
Explanation of each part -2M
Diagram -1M
Cellular Structure in Mobile Communication
The cellular network is designed to efficiently use the radio spectrum by dividing a
geographical area into small hexagonal regions called cells. Each cell is served by a
Base Station (BS) that connects mobile users to the network.
• Each cell has a unique frequency range to avoid interference with
neighboring cells.
• Adjacent cells do not use the same frequencies to minimize signal
interference.
• As a user moves from one cell to another, a process called handover ensures
uninterrupted communication.
Frequency Reuse:
✔ Efficient use of limited frequency spectrum.
✔ Increases capacity by allowing more simultaneous users.
✔ Reduces interference when planned correctly.
Q7   c.   Explain the role of multimedia in digital communication. How do multimedia   [10]
technologies enhance user experience in various applications such as education,
CO-4;
entertainment, and business? Also, how to overcome the jitter for smooth play back of
SO-1;
video (real time data)?
BL-2
********** 15 **********
--- page 16 ---
Explanation each part -3M
Diagram-1M
Multimedia refers to the integration of text, audio, images, video, and animations in
communication. It plays a crucial role in various domains:
1. Education – Enhances learning through interactive tutorials, virtual
classrooms, and e-learning platforms.
2. Entertainment – Enables streaming services, video games, and digital media
consumption.
3. Business – Improves marketing, remote collaboration, and customer
engagement through presentations, webinars, and advertisements.
Enhancement of User Experience:
•   Interactivity – Encourages engagement through interactive content.
• Improved Retention – Visual and auditory learning helps retain information
better.
•   Personalization – AI and adaptive technologies create personalized
experiences.
To overcome jitter and achieve smooth playback of real-time data, two chief techniques
are employed:
•   Timestamps. A sender provides a timestamp for each piece of data.
A receiver uses the timestamps to handle out-of-order packets and
to display the data in the correct time sequence.
•   Jitter Buffer. To accommodate jitter (i.e., small variances in delay), a receiver
buffers data and delays playback.
********** 16 **********
````

## 2024-25 · Re-Exam · Sem 6 · Answer key · paper cf3ea67a3337

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/BTech_CSE_DS_7011/Networks and Telecommunications/ANS_Networks and Telecommunications(702EX0C023)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Jul 2025
- Text: mixed (14 pages), mean OCR confidence 33.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2024-2025)
Subject: Networks and Telecommunications
Date: 09 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 14 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 1;   a. What is the purpose of caching in browser? How effectively it is useful?   [5]
SO- 1;
BL-1   Explanation – 5 M
********** 1 **********
--- page 2 ---
CO- 2;   b. What is the motivation of data communications, how it can be done?   [5]
SO-1;
BL-1   Explanation – 5 M
Scope
1. The sources of information can be of arbitrary types
2. Transmission uses a physical system
3. Multiple sources of information can share the underlying medium
Sharing plays a fundamental role in most computer networks – A network usually permits
multiple pairs of communicating entities to communicate over a given physical medium –
There are possible ways underlying facilities can be shared – We should understand advantages
and disadvantages of each and the resulting modes of communication
CO- 3;   c. What is Spread Spectrum Transmission? Why it is used?   [5]
SO-1;
BL-1   Explanation – 5 M
CO- 4;   d. Define Internetworking and explain its significance in networking.   [5]
SO-1;
BL-1   Explanation – 5 M
Internetworking refers to connecting multiple networks using devices like routers, gateways,
and switches to enable seamless data exchange.
It ensures scalability, interoperability, and efficient resource utilization across different
networks.
Q2   a. b) Explain the concept of Circular Dependencies among Servers with an example, and   [5]
CO-1;   discuss the challenges it poses in network communication.
SO-1;   c) What is Peer-to-Peer (P2P) Interactions, and how does it help in avoiding network   [5]
BL-2   bottlenecks? Provide an example of a P2P application.
Explanation of each – 3 M
Examples of each – 2M
a) Occurs when a server acting as a client depends on another server, which in turn
depends on the first server.
Example: A web server requests data from a database server, which then requests
authentication from another server, which again requests data from the web server.
********** 2 **********
--- page 3 ---
Such dependencies can lead to infinite loops, deadlocks, and resource exhaustion.
Proper system design and dependency management help prevent circular dependencies.
b)
Q2   b. Compare Circuit Switching and Packet Switching with respect to their working,   [10]
CO-2;   advantages, and disadvantages. Provide suitable examples for both in relation to the types of
SO-1;   networks.
BL-2   Comparison – 8 M
Examples – 2M
********** 3 **********
--- page 4 ---
Q3   a. Explain the types of guided and unguided transmission media in detail along with the   [10]
CO- 2;   diagram of each.
SO-1;
BL-2   Explanation of guided transmission– 6 M
Explanation of unguided transmission– 2 M
Diagrams if any – 2M
********** 4 **********
--- page 5 ---
Q3   b.   a) For the given IP address 172.16.50.0/20, Determine the first and last address of the   [5]
CO-4;   network.
SO-1;
BL-2   Change to binary for each – 2M
First and last ip address – 3M
Binary form of IP address - 10101100.00010000.00110010.00000000
Binary form of 20 bit mask - 11111111.11111111.11110000.00000000
First Usable IP: Network Address + 1
172.16.48.1
Last Usable IP: Broadcast Address - 1
172.16.63.254
b) Explain all the special IP addresses and its importance.   [5]
List and explanation – 5M
********** 5 **********
--- page 6 ---
Q4   a.   Illustrate the Client-Server Model of Interaction and explain how it ensures proper   [10]
CO-1;   communication between applications on different computers.
SO-2;
BL-2   Explanation CS with diagram – 6M
Proper communication between applications – 4M
Involves two applications: a client that initiates the request and a server that waits
for client connections.
Servers run continuously, listening for client requests, while clients actively send
requests when needed.
Examples include web browsing (HTTP), email services (SMTP), and database
queries (SQL servers).
Ensures efficient communication by structuring interactions in a way that prevents
connection conflicts.
********** 6 **********
--- page 7 ---
Q4   b.   a) A communication channel has a bandwidth of 5 kHz. What is the maximum data rate that   [5]
CO-2;   can be transmitted through this channel if it is a noise-free channel using binary signaling?
SO-2;
BL-3   Step marking – 5M each
b) A channel has a bandwidth of 3 kHz and a signal-to-noise ratio (SNR) of 30 dB. Calculate   [5]
the maximum data rate that can be achieved using Shannon’s Capacity formula.
********** 7 **********
--- page 8 ---
Q5   a. Classify Addressing in Local Area Networks (LAN). Explain MAC addressing, its   [10]
CO-2;   components, and differentiate between unicast, multicast, and broadcast addressing.
SO-1;
BL-2   Explanation of each sub parts – 5M
********** 8 **********
--- page 9 ---
Q5   b. Explain the concept of the following:   [10]
CO-4;   (i) Content caching
SO-1;   (ii) Web load balancer
BL-2   (iii) Server virtualization
Explanation of each – 3M
Diagram – 1M
• Content Caching (Akamai)
o Some companies offer a distributed caching service.
o For example, Akamai has a set of servers all over the Internet.
o An organization can pay Akamai for the privilege of pre-loading Akamai
server caches with the organization's web pages.
o Links on the organization's web site direct customer clicks to Akamai server
content.
o The organization is allowed to send updates of their 'content' to the Akamai
caches.
o The scheme reduces load on the servers of the organization.
•   32.4 Web Load Balancers
o Web server optimization gets a lot of attention because businesses rely on the
web to make sales.
o A load balancer is a device that distributes incoming requests among
multiple computers running identical web servers.
o   Typically the servers share the same customer database.
o The load balancers have the ability to direct a series of requests from the
same source to the same server.
•   32.5 Server Virtualization
o Some systems support process migration - the capability of an executing
program to move to another computer.
********** 9 **********
--- page 10 ---
o Given infrastructure for process migration, it is possible for a server on an
overloaded machine to move to another machine where resources like CPU
time are in more plentiful supply.
Q6   a. Explain in detail the TCP/IP protocol suite with its layer diagram.   [10]
CO-1;
SO-1;   Diagram- 2M
BL-2   Explanation of layers -8M
Layer 1: Physical
Protocols in the Physical layer specify details about the underlying transmission
medium and the associated hardware. All specifications related to electrical properties, radio
frequencies, and signals belong in layer 1.
Layer 2: Network Interface
Protocols in the Network Interface layer specify details about communication
between higher layers of protocols, which are usually implemented in software, and the
underlying network, which is implemented in hardware. Specifications about network
addresses and the maximum packet size that a network can support, protocols used to access
the underlying medium, and hardware addressing belong in layer 2.
Layer 3: Internet
Protocols in the Internet layer form the fundamental basis for the Internet. Layer 3
protocols specify communication between two computers across the Internet (i.e., across
multiple interconnected networks). The Internet addressing structure, the format of Internet
packets, the method for dividing a large Internet packet into smaller packets for transmission,
and mechanisms for reporting errors belong in layer 3.
Layer 4: Transport
Protocols in the Transport layer provide for communication from an application
program on one computer to an application program on another. Specifications that
control the maximum rate a receiver can accept data, mechanisms to avoid network
congestion, and techniques to insure that all data is received in the correct order belong in
layer 4.
Layer 5: Application
Protocols in the top layer of the TCP/IP stack specify how a pair of applications
interact when they communicate. Layer 5 protocols specify details about the format and
meaning of messages that applications can exchange as well as procedures to be followed
during communication. Specifications for email exchange, file transfer, web browsing,
telephone services, and video teleconferencing all belong in layer 5.
Q6   b. Consider the given network topology with routers R1,R2, and R3 and the routing table;   [10]
CO-4;   Answer the following question with proper reasoning.
SO-1;
BL-3
********** 10 **********
--- page 11 ---
(i) Explain how the routing decisions are made when a packet with the destination IP
address 192.4.10.5 arrives at router R2.
(ii) If a new network 50.0.0.0/8 is introduced and connected to 40.0.0.8, how would the
routing table need to be updated?
(iii) Identify the significance of the subnet masks used in the routing table. How do they
impact packet forwarding?
Answer
Explanation and solution (i), (ii) – 3M each
Explanation (iii) -$M
Router R₂ correctly forwards packets to 192.4.10.5 via 128.1.0.9.
If 50.0.0.0/8 is introduced, an additional route must be added with 40.0.0.8 as the next
hop.
The subnet masks determine how broad or specific a route is, affecting how packets are
handled in the routing process.
1. Routing Decision for Destination IP 192.4.10.5 at Router R₂
When a packet with the destination IP 192.4.10.5 arrives at Router R₂, the router will check
its routing table to determine the next hop.
• The destination IP 192.4.10.5 belongs to the 192.4.10.0/24 network.
•   In the routing table, the entry for 192.4.10.0 has a subnet mask of 255.255.255.0 and
a next hop of 128.1.0.9.
•   Since 192.4.10.5 falls within the 192.4.10.0/24 subnet, Router R₂ will forward the
packet to Router R₃ at IP 128.1.0.9.
•   Router R₃ will then forward the packet to its final destination in the 192.4.10.0/24
network.
2. Routing Table Update for the New Network 50.0.0.0/8 at Router R₂
If a new network 50.0.0.0/8 is introduced and connected to 40.0.0.8, the routing table at
Router R₂ must be updated to include this new entry.
•   Since the 50.0.0.0/8 network is connected via 40.0.0.8, Router R₂ must add the
following entry:
Destination Mask   Next Hop
50.0.0.0   255.0.0.0 40.0.0.8
•   This ensures that packets destined for 50.0.0.x addresses are correctly forwarded via
40.0.0.8.
3. Significance of Subnet Masks in Packet Forwarding
Subnet masks determine the network portion of an IP address and play a crucial role in
packet forwarding decisions:
•   255.0.0.0 (/8) → Covers a large network (e.g., 30.0.0.0/8 and 40.0.0.0/8), meaning
any destination in 30.x.x.x or 40.x.x.x will be routed as a single entity.
•   255.255.0.0 (/16) → Covers a smaller range, ensuring finer control of routing (e.g.,
128.1.0.0/16 is handled separately from other networks).
•   255.255.255.0 (/24) → Ensures that individual small subnets, like 192.4.10.0/24, are
recognized and handled precisely.
********** 11 **********
--- page 12 ---
Q7   a. How to define the growth of computer networks and complexity arises in setting up the   [5]
CO-1;   networking.
SO-1;
BL-1   Explanation – 5M
Q7   b. Explain the structure of an 802.11 frame and describe the significance of the four MAC   [5]
CO-3;   addresses used in wireless communication. How does it differ from an Ethernet frame?
SO-1;
BL-1   Explanation of frame structure with MAC address– 3M
Difference- 2M
********** 12 **********
--- page 13 ---
Q7   c. Explain the key components and working principles of Voice over Internet Protocol (VoIP).   [10]
CO-4;   Analyze its advantages and challenges in modern communication systems.
SO-1;
BL-2   Explanation -key components -4 M
Diagram – 2M
Advantages and challenges – 2M each
Key Components and Working Principles of VoIP
Voice over Internet Protocol (VoIP) is a technology that enables voice communication over
the internet instead of traditional telephone networks. The key components of VoIP include:
1. IP Phones – These are hardware or software-based phones that use VoIP to make
and receive calls.
2. VoIP Gateway – Converts voice signals from analog to digital and vice versa.
3. VoIP Server (Softswitch) – Routes calls between different users and manages call
functionalities.
4. Codecs – Compress and decompress voice signals for efficient transmission.
5. Internet Connection – A stable broadband connection is essential for VoIP
communication.
Working Principles:
•   Voice signals are converted into digital packets.
•   These packets are transmitted over an IP network.
• The recipient's device receives and reassembles the packets into an audio signal.
•   Various protocols such as SIP (Session Initiation Protocol) and RTP (Real-time
Transport Protocol) are used for communication.
Advantages of VoIP
• Cost Savings – Lower call rates, especially for international communication.
•   Scalability – Easy to add new users without additional hardware.
•   Flexibility – Supports mobile and remote work.
•   Feature-rich – Includes video calling, call forwarding, and voicemail.
Challenges of VoIP
•   Reliability Issues – Dependent on internet connectivity and bandwidth.
•   Security Risks – Vulnerable to cyber threats like hacking and eavesdropping.
• Latency and Jitter – Network congestion may affect voice quality.
• Power Dependency – Unlike traditional phones, VoIP requires electricity to
function.
********** 13 **********
--- page 14 ---
FRR IC 7 I OH
````
