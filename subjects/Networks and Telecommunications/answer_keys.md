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

[Text in pictures on this page, read by OCR]
Three main ideas provide much of the motivation for data
communications and help define the scope

1. The sources of information can be of arbitrary types

2. Transmission uses a physical system

3. Multiple sources of information can share the underlying medium
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

[Text in pictures on this page, read by OCR]
Basic Service Set (BSS) for an AP is defined as set of devices
that can hear the AP

APs interconnect through wired network

range oj
interconnect such as a switch ——»(— access we

wireless JT

computer J F point
J Ay cy

AP AP AP

“ 7 # “5 # “7, #

BSS #1 BSS #2 BSS #3

e Infrastructure mode

— Wireless devices communicate through an access point
(AP)

— APs connect to each other and (usually) the Internet

— Typical uses: corporate wireless LAN, Internet cafe
e Ad hoc mode

— Direct communication among wireless devices

— Forwarding possible

— Seldom used
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

[Text in pictures on this page, read by OCR]
Application LAYER 5

Transport LAYER 4

Internet LAYER 3

Network Interface LAYER 2

LAYER 1

Physical
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

[Text in pictures on this page, read by OCR]
Class Leading Network Host No. of Addresses per IP Address Range

Bits ID Bits ID Bits Networks Network
0.0.0.0 -
A 0 8 24 27 = 128 224 = 16,777,216
127.255.255.255
128.0.0.0-
B 10 16 16 244 = 16,384 236 = 65,536
191.255.255.255
c 110 24 8 ue 28 = 256 192.0.0.0—
2,097,152 - 223.255.255.255
. 224.0.0.0 -
D 1110 _ _ Multicast _
239.255.255.255
240.0.0.0 -
E 1111 — _ Experimental -

255.255.255.255

HyperText Transfer Protocol (HTTP) is the primary transfer
protocol that a browser uses to interact with a web server

A browser is a client that extracts a server name from a URL
and contacts the server

Most URLs contain an explicit protocol reference of http:// or
omit the protocol altogether (HTTP is assumed)

HTTP can be characterized as follows:
— Uses textual control messages

— Transfers binary data files

— Can download or upload data

— Incorporates caching
--- page 5 ---
CO 2; B What is a frame. Explain framing in serial communication and how byte stuffing works.   [10]
SO 1;
BL 2   Definition of frame – 2 marks
Framing in serial communication – 3 marks
Byte stuffing and its working – 5 marks
********** 5 **********

[Text in pictures on this page, read by OCR]
Request Description

Requests a document; server responds by sending status

oer information followed by a copy of the document

Requests status information; server responds by sending

we status information, but does not send a copy of the document

POST Sends data to a server; the server appends the data toa
specified item (e.g., a message is appended to a list)

PUT Sends data to a server; the server uses the data to completely
replace the specified item (i.e., overwrites the previous data)

* The first line of a response header contains a status code
— that tells the browser whether the server handled the request

— Ifthe request was incorrectly formed or the requested item was not
available, the status code pinpoints the problem
+ For example, a server returns status code 404 if the requested item cannot be found
+ When it honors a request, a server returns status code 200

Status Code Corresponding Status String

200 OK
400 Bad Request
| 404 | Not Found |
* Additional lines of the header give further information, such as

- its length
— when it was last modified
- and the content type
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

[Text in pictures on this page, read by OCR]
+ Nyquist's Theorem provides an absolute maximum that cannot be
achieved in practice
— areal system is subject to small amounts of electrical noise
— such noise makes it impossible to achieve the theoretical maximum
transmission rate

* Claude Shannon extended Nyquist's work to specify the maximum data
rate that could be achieved over a transmission system that experiences

noise
— The result, called Shannon's Theorem

C = B log)(1 + S/N)
where

+ Cis the effective limit on the channel capacity in bits per second

+ Bis the hardware bandwidth

+ S/Nis the signal-to-noise ratio, the ratio of the average signal power divided by
the average noise power
--- page 8 ---
CO 4; B   Explain the process of fragmentation and reassembly with reference to the MTU concept.   [10]
SO 1;   Why is reassembly done at the destination and not at intermediate routers? Why
BL 2   Fragmenting a fragment is performed.
Fragmentation and reassembly – 6 marks
Reassembly at destination reason – 2 marks
Fragmenting a fragment – 2marks
********** 8 **********

[Text in pictures on this page, read by OCR]
Shannon's Theorem suggests one way to reduce errors:

— increase the signal-to-noise ratio (either by increasing the signal or
lowering noise if possible)

Mechanisms like shielded wiring can help lower noise
Physical transmission system is always susceptible to errors
— it may not be possible to change the signal-to-noise ratio
Noise/interference cannot be eliminated completely

— But many transmission errors can be detected

— In some cases, errors can be corrected automatically

We will see that error detection adds overhead

Error handling is a tradeoff

— in which a system designer must decide whether a given error is
likely to occur, and if so, what the consequences will be

MTU, Datagram Size, and Encapsulation

Defn: The maximum transmission unit (MTU) is the maximum amount of data that a
frame can carry.

Each hardware technology specifies its own MTU.
+ There is no exception to the MTU limit.
+ Adatagram must be smaller or equal to the MTU in order to be transmitted.

Difficulty: In a heterogeneous network, a router can connect networks with different
MTUs.

Hy R Hz

Oo Net 1 (MTU=1500) a Net 2 (MTU=1000) o

Fragmentation & Reassembly

When a datagram is larger than the MTU of the network over which it must be sent,
the router divides the datagram into smaller pieces called fragments, and sends each
fragment independently.

+ The fragments have the same format as other datagrams

* The FLAG field contains a bit that means the datagram is a fragment.

* Other fields in the header contain information that allows the fragments to be
reassembled.

* Each fragment has a copy of the original header with fields modified as necessary.

[P_Headet original datagram data area__|

{iP Hdrt| data1 | [IP Hdr2|   data2 [IP Har 3] data3_ |
--- page 9 ---
Q.5
CO 1; A   Explain the Client-Server model. How is a server identified using IP address and port   [10]
SO 1;   number.
BL 2
Client server model- 4 marks
Server identification – 4 marks
Diagram – 2 marks
********** 9 **********

[Text in pictures on this page, read by OCR]
Reassembly
The process of creating the original datagram from the fragments is called reassembly.

Note: The final fragment has a special bit set in the header to signal that all fragments
have arrived successfully.

The Internet Protocol specifies that the u/timate destination host should reassembly
the fragments.

Two advantages to reassembly at the destination:
+ Reduces the amount of information in each router.

+ It allows the routes to change dynamically.

In the figure, H, will perform reassembly. R, will simply forward the fragments.

Te n, T

Net 1 (MTU=1500) ——t}— Net 2 (MTU=1000) ——C}+—_ Net 3 (MTU=1500)

Fragmenting a Fragment

¢ Ifthe MTU ofa subsequent network is smaller than the one that caused
fragmentation, the fragments must be fragmented further.

¢ The IP fragmentation scheme allows this fragmentation with all fragments still
being treated in exactly the same way.

Example:

hy . I"

a
Net 1 (MTU=1500) ——C}+— ~ Net 2 (MTU=1000) ——CH— Net 3 (MTU- 592 _

Server Application Client Application

Starts first Starts second
Does not need to know which client | Must know which server to
will contact it contact

Waits passively and arbitrarily long | Initiates a contact whenever
for contact from a client communication is needed

Communicates with a client by both | Communicates with a server by
sending and receiving data sending and receiving data

Stays running after servicing one May terminate after interacting
client, and waits for another with a server
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

[Text in pictures on this page, read by OCR]
Server Identification and Demultiplexing

How does a client identify a server? The Internet protocols divide identification
into two pieces:

e An identifier for the computer on which a server runs

e An identifier for a particular service on the computer

Identifying A Computer.

* Each computer in the Internet is assigned a unique 32-bit identifier known as an
Internet Protocol address (IP address).

* When it contacts a server, a client must specify the server’s IP address. To make
server identification easy for humans, each computer is also assigned a name, and the
Domain Name System is used to translate a name into an address. Thus, a user
specifies a name such as www.cisco.com rather than an integer address.

Identifying A Service.

* Each service available in the Internet is assigned a unique 16-bit identifier known
as a protocol port number (often abbreviated port number).

* For example, email is assigned port number 25, and the web is assigned port
number 80.

* When a server begins execution, it registers with its local system by specifying the
port number for the service it offers. When a client contacts a remote server to
request service, the request contains a port number.

¢ Thus, when a request arrives at a server, software on the server uses the port
number in the request to determine which application on the server computer
should handle the request.

© Start after server is ° Start before any of
already running the clients

e Obtain server name © Register port N with
from user the local system

¢ Use DNS to translate
name to IP address

¢ Wait for contact
from a client

° Specify that the ¢ Interact with client
service uses port N until client finishes
¢ Contact server and © Wait for contact from

interact the next client...
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

[Text in pictures on this page, read by OCR]
CSMA/CA

e Alternative to CODMA/CD
e Used in wireless networks (Wi-Fi)
¢ Needed because signals have limited distance, 6

e Example: computer | cannot receive transmission when
computers 2 and 3 communicate

[ ; i ; =)
aay Ca ame?

computer 1 computer 2 computer 3

e All computers in range of computers 2 and 3 must be
informed that a transmission will occur

Illustration Of CSMA/CA

1: ready to send (RTS)

2: clear to send (CTS) 2: clear to send (CTS)

3: packet transmission

= =

computer 1 computer 2 computer 3

Communicating pair exchange RTS and CTS before packet
transmission

Any computer less than 6 away from either computer 2 or 3
hears at least one of the RTS/CTS messages
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

[Text in pictures on this page, read by OCR]
packets arrive packets extracted
in bursts at a uniform rate

jitter buffer

playback displa
kk d >| process dics

connection
to Internet

Stream Paradigm Message Paradigm

Connection-oriented Connectionless

1-to-1 communication Many-to-many communication

Sequence of individual bytes | Sequence of individual messages

Arbitrary length transfer Each message limited to 64 Kbytes

Used by most applications Used for multimedia applications

Built on TCP protocol Built on UDP protocol
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

[Text in pictures on this page, read by OCR]
Early computer network were designed when computers were large and
very expensive, and the main motivation was resource sharing
— Networks were devised to connect multiple users
* each with a screen and keyboard, to a large centralized computer
— Later networks allowed multiple users to share peripheral devices
* Early network were designed to permit sharing of expensive, centralized resources
Department of Defense for Advanced Research Projects Agency
(DARPA or ARPA) interested in finding ways to share resources (1960s)
— Researchers needed powerful computers
+ but these computers were very expensive
* the ARPA budget was insufficient to fund many computers

— ARPA planned to interconnect all computers with a network

* and devise software that would allow a researcher to use whichever computer was
best suited to perform a given task

ARPA did the following to achieve the visionary work:

— gathered some of the best minds available

— focused them on computer network research

— hired contractors to turn the designs into a working system: ARPANET
The research turned out to be revolutionary
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

[Text in pictures on this page, read by OCR]
Frequency Assignment

e Goal: minimize interference

e Principle

Interference can be minimized if an adjacent pair of cells do not
use the same frequency.

e Method: devise an assignment of frequencies such that two
adjacent cells are not assigned the same frequency

e Technique: create a pattern that can be repeated

e Known as a cluster approach
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

[Text in pictures on this page, read by OCR]
1: Physical header (possible, but not likely)
2: Network Interface header

3: Internet header

(_ 4: Transport header

i—_—__—_——————_ message the application sent ————————_

MTU, Datagram Size, and Encapsulation

Defn: The maximum transmission unit (MTU) is the maximum amount of data that a
frame can carry.

Each hardware technology specifies its own MTU.
* There is no exception to the MTU limit.
+ A datagram must be smaller or equal to the MTU in order to be transmitted.

Difficulty: In a heterogeneous network, a router can connect networks with different
MITUs.

Hy R H,
oO Net 1 (MTU=1500) O- Net 2 (MTU=1000) Oo
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

[Text in pictures on this page, read by OCR]
Standard Purpose

HyperText Markup | Arepresentation standard used to specify the
Language (HTML) | contents and layout of a web page

Uniform Resource | A representation standard that specifies the
Locator (URL) format and meaning of web page identifiers

HyperText Transfer | A transfer protocol that specifies how a browser
Protocol (HTTP) interacts with a web server to transfer data

The Web uses a syntactic form known as a Uniform
Resource Locator (URL) to specify a web page

The general form of a URL is:

protocol ://computer_name: port/document_name%eparameters
where

— protocol is the name of the protocol used to access the document

— computer_name is the domain name of the computer on which the
document resides

— port (optional) port number at which the server is listening

— document_name (optional) name of the document—lf we do not
enter a name, index.htm! is assumed

— % (optional) parameters for the page—error in text—it should be “?”
instead of “%”

— Example:
http://www _netbook.cs.purdue.edu/toc/toc01.htm

In a typical URL, a user can omit many of the parts
www_netbook.cs purdue. edu

Which omits

— the protocol (http is assumed)

— the port (80 is assumed)

— the document name (index.html is assumed)

— and parameters (none are assumed)
A URL contains the information a browser needs to retrieve a page
Browser uses the separator characters

— colon, slash, and percent, to divide the URL into four components:

* aprotocol, a computer name, a document name, and parameters

Browser uses the computer name and protocol port to form a connection
to the server on which the page resides

Browser uses the document name and parameters to request a page
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

[Text in pictures on this page, read by OCR]
Name Expansion Description

LAN Local Area Network Least expensive; spans a single
room or a single building

MAN | Metropolitan Area Network | Medium expense; spans a major
city or a metroplex

WAN | Wide Area Network Most expensive; spans sites in
multiple cities

Name Expansion Description

PAN Personal Area Network | Spans the area around an individual
used for earphones

SAN Storage Area Network Spans the distance between a disk
farm and processors in a data center

CAN Chip Area Network Spans a single chip and connects
processor, memories, etc.
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

[Text in pictures on this page, read by OCR]
e An application using UDP can
— Send a message to any receiver (universal)
— Send at any time (asynchronous)
— Stop sending at any time (unterminated)

e That is, a sender does not

— Inform the network before sending (1.e., does not
establish a communication channel)

— Inform the other endpoint before sending

— Inform the network or other endpoint that no more
messages will be sent
--- page 9 ---
UDP Encapsulation
Q.5
CO 1; A How does a concurrent server use threads to handle multiple clients? Explain circular   [10]
SO 1;   dependencies among server.
BL 2
Explanation – concurrent server – 5marks
Circular dependencies- 5marks
********** 9 **********

[Text in pictures on this page, read by OCR]
16

31

UDP SOURCE PORT

UDP DESTINATION PORT

UDP MESSAGE LENGTH

UDP CHECKSUM

PAYLOAD (MESSAGE DATA)

UDP Checksum

16-bit 1s-complement checksum

Covers entire UDP packet, including data (recall: IP does
not checksum the payload)

Is optional: value of zero means sender did not compute a
checksum

Includes extra pseudo header that contains IP addresses

Example of IPv4 pseudo header:

as

Es

IP SOURCE ADDRESS

IP DESTINATION ADDRESS

ZERO PROTO UDP LENGTH
--- page 10 ---
CO 2; B Explain the two strategies for handling channel errors? Define dataword, codeword, and   [10]
SO 1;   codebook using (n, k) notation with an example.
BL 2
Explanation of strategies- 3 marks each
Definition with example of codebook – 4 marks
********** 10 **********

[Text in pictures on this page, read by OCR]
Concurrent Servers

¢ Although a serial approach works in a few trivial cases, most servers are concurrent.
That is, a server uses more than one thread of control, to handle multiple clients at the
same time.

* The details of concurrent execution depend on the operating system.

* Concurrent server code is divided into two pieces, a main program (thread) and <
handler.

* The main thread merely accepts contact from a client, and creates a thread of
control for the client. Each thread of control interacts with a single client, and
runs the handler code.

¢ After handling one client, the thread terminates.

* Meanwhile, the main thread keeps the server alive — after creating a thread to
handle a request, the main thread waits for another request to arrive.

* iif N clients are simultaneously using a concurrent server, N+1 threads
will be running: the main thread is waiting for additional requests, and N
threads are each interacting with a single client.

Circular Dependencies among Servers

* Any program that contacts another is acting as a client, and any program that accepts
contact from another is acting as a server.
* In practice, the distinction blurs because a server for one service can act as a client for
another.
* For example, before it can fill in a web page, a web server may need to become a
client of a database. A server may also become the client of a security service
(e.g., to verify that a client is allowed to access the service).
* Ofcourse, programmers must be careful to avoid circular dependencies among
servers.

* For example, consider what can happen if a server for service X1 becomes a client of
service X2, which becomes a client of service X3, which becomes a client of X1. The
chain of requests can continue indefinitely until all three servers exhaust resources.
The potential for circularity is especially high when services are designed
independently because no single programmer controls all servers
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

[Text in pictures on this page, read by OCR]
* The two types of FEC techniques satisfy separate needs:

* Block Error Codes
— It divides the data to be sent into a set of blocks
— It attaches extra information known as redundancy to each block
— The encoding for a given block of bits depends only on the bits
themselves, not on bits that were sent earlier
— They are memoryless in the sense that the encoding mechanism
does not carry state information from one block of data to the next

* Convolutional Error Codes

— It treats data as a series of bits, and computes a code over a
continuous series

— Thus, the code computed for a set of bits depends on the current
input and some of the previous bits in the stream

— Convolutional codes are said to be codes with memory

— we define the set of all possible messages to be a set of datawords

— and define the set of all possible encoded versions to be a set of
codewords

¢ Ifa dataword contains k bits and r additional bits are added

to form a codeword, we say that the result is an
(n, k) encoding scheme

— where n=k+r

* The key to successful error detection lies in choosing a
subset of the 2 possible combinations that are valid
codewords
— The valid subset is known as a codebook
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

[Text in pictures on this page, read by OCR]
* The Internet stream service is connection-oriented, which means the service operates
analogous to a telephone call: before they can communicate, two applications must
request that a connection be created.

* Once it has been established, the connection allows the applications to send data in
either direction.

¢ Finally, when they finish communicating, the applications request that the connection
be terminated.

Fiber Modems

Communicate over an optical fiber
Can span long distance
Provide standard network interface (e.g., Ethernet)

Can be used to extend connection between computer and
network
Illustration of an extended network connection

connection
from computer optical fiber
Ethernet hub

a, 1

! |

fiber modem fiber modem
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

[Text in pictures on this page, read by OCR]
Repeaters

e Operate at layer 1 (do not understand packets)
e Repeat and amplify signals
e Low cost

e Example use: extended infrared sensor on a cable box

connection to
cable box extended connection

remote
Cable box Bali

e Disadvantage: amplifies and repeats noise

Bridge
Originally sold as stand-alone device to extend two LAN
segments
Operates at layer 2
Can connect two or more segments

Listens in promiscuous mode on each segment and sends
copy of each frame to other segments

Does not copy noise, collisions, or frames that are incorrectly
formed

Makes connected segments appear to be a single, large LAN

Uses source MAC address in frames to learn computer
locations automatically, and uses destination MAC address to
filter frames
--- page 16 ---
The RTP header has sequence number, timestamp, and source identifier fields that help
thereceiver implement the functionality of a jitter buffer.
RTP fields also provides support for video encodings that send incremental changes after a full
frame,
multiple senders to a multicast address, and the mixing of multiple streams by intermediate
systems.
********** 16 **********

[Text in pictures on this page, read by OCR]
ol 3

8 16

31

VER|P)X

cc

M| PAYTYPE SEQUENCE NUMBER

TIMESTAMP

SYNCHRONIZATION SOURCE IDENTIFIER

CONTRIBUTING SOURCE IDENTIFIER
````

## 2024-25 · Final-Exam · Sem 6 · Answer key · paper 7c09c1b6e88a

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_06/Final-Exam/BTech_CSE_DS_7011/Networks and Telecommunications/ANS_Networks and Telecommunications(702EX0C023)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2025
- Text: mixed (16 pages), mean OCR confidence 90.4
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

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

[Text in pictures on this page, read by OCR]
Identifying A Computer.

* Each computer in the Internet is assigned a unique 32-bit identifier known as an
Internet Protocol address (IP address).

* When it contacts a server, a client must specify the server’s IP address. To make
server identification easy for humans, each computer is also assigned a name, and the
Domain Name System is used to translate a name into an address. Thus, a user
specifies a name such as www.cisco.com rather than an integer address.

Identifying A Service.

* Each service available in the Internet is assigned a unique 16-bit identifier known
as a protocol port number (often abbreviated port number).

¢ For example, email is assigned port number 25, and the web is assigned port
number 80.

* When a server begins execution, it registers with its local system by specifying the
port number for the service it offers. When a client contacts a remote server to
request service, the request contains a port number.

* Thus, when a request arrives at a server, software on the server uses the port
number in the request to determine which application on the server computer
should handle the request.
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

[Text in pictures on this page, read by OCR]
¢ Start after server is ¢ Start before any of

already running the clients
© Obtain server name ¢ Register port N with
from user the local system

¢ Use DNS to translate ¢ Wait for contact

name to IP address from a client
* Specify that the ¢ Interact with client
service uses port N until client finishes
* Contact server and ¢ Wait for contact from

interact the next client...

Infrastructure mode

— Wireless devices communicate through an access point
(AP)

— APs connect to each other and (usually) the Internet
— Typical uses: corporate wireless LAN, Internet cafe
Ad hoc mode

— Direct communication among wireless devices

— Forwarding possible

— Seldom used
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

[Text in pictures on this page, read by OCR]
Class Starting Bits First Octet Range Subnet Mask Usage

A Oxxx 1-126 255.0.0.0 Large Networks

B 10xx 128-191 255.255.0.0 Medium Networks
c 110x 192 - 223 255.255.255.0 Small Networks

D 1110 224 - 239 N/A Multicasting

E 1111 240-255 N/A Experimental
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

[Text in pictures on this page, read by OCR]
A client or server consists of an application program, and a computer can run mul-
tiple applications at the same time. As a consequence, a computer can run:

¢ A single client

¢ A single server

¢ Multiple copies of a client that contact a given server
¢ Multiple clients that each contact a particular server

¢ Multiple servers, each for a particular service

¢ Allowing a given computer to operate multiple servers is useful because the hardware
can be shared. In addition, a single computer has lower system administration
overhead than multiple computer systems.

* A server can remain idle for long periods of time. An idle server does not use the CPU
while waiting for a request to arrive. Thus, if demand for services is low,
consolidating servers on a single computer can dramatically reduce cost without
significantly reducing performance.

* Asingle, powerful computer can offer multiple services at the same time; a separate
server program is needed for each service.
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

[Text in pictures on this page, read by OCR]
Physical Channel
(noise & interference)

t the t

Demodulator

Demultiplexor

Channel Decoder Channel Decoder
Source Decoder Source Decoder

1 1

Destination 1 Destination N

e A router has connections to multiple physical networks.

¢ Each IP address contains a prefix that specifies a physical network.

Thus, a single IP address does not suffice for a router because each router connects
to multiple networks and each network has a unique prefix. The IP scheme can be ex-
plained by a fundamental principle:

An IP address does not identify a specific computer. Instead, each IP
address identifies a connection between a computer and a network. A
computer with multiple network connections (e.g., a router) must be
assigned one IP address for each connection.
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

[Text in pictures on this page, read by OCR]
Ethernet 131.108.0.0/16

router 1
Fh

Ly.
131.108.99.5 i < 223.240.129.2

Wi-Fi Net
223.240.129.0/24

223.240.129.17 9
router 2
aur 78.0.0.17 —* | _
The address prefix identifies the network. aa ——— —_

Need one router address per connection. Cc : WAN 78.0.0.0/8
Ck

Standard Purpose

HyperText Markup A representation standard used to specify the
Language (HTML) contents and layout of a web page

Uniform Resource A representation standard that specifies the
Locator (URL) format and meaning of web page identifiers

HyperText Transfer | A transfer protocol that specifies how a browser
Protocol (HTTP) interacts with a web server to transfer data

* HTML is classified as declarative
— It allows one to specify what is to be done, not how to do it

* HTML is classified as a markup language
— It only gives general guidelines for display and does not include
detailed formatting instructions
— HTML allows a page to specify the level of importance of a headin
— HTML does not require the author to specify the exact font, typefad
point size, or spacing for the heading

* HTML extensions have been created that do allow the specification of an
exact font, typeface, point size, and formatting.

+ A browser chooses all display details
— The use of a markup language is important
* because it allows a browser to adapt the page to the underlying display
hardware
* a page can be formatted for a high resolution or low resolution display, a
large screen or a small hand-held device such as an iPhone or PDA
--- page 8 ---
Q4   b.   (i) Explain the block codes and the convolution error codes and its utilization.   [5]
CO-2;
SO-2;
BL-3   Explanation-2M each
Utilization – 1M
********** 8 **********

[Text in pictures on this page, read by OCR]
* The Web uses a syntactic form known as a Uniform
Resource Locator (URL) to specify a web page

* The general form of a URL is:

protocol ://computer_name: port/document_name parameters
* where

— protocol is the name of the protocol used to access the document

— computer_name is the domain name of the computer on which the
document resides

— port (optional) port number at which the server is listening

— document_name (optional) name of the document—lf we do not
enter a name, index.html! is assumed

— % (optional) parameters for the page—error in text—it should be “?”
instead of “%”

— Example:
http://www_.netbook.cs.purdue.edw/toc/toc0 1 htm

HyperText Transfer Protocol (HTTP) is the primary transfer

protocol that a browser uses to interact with a web server

A browser is a client that extracts a server name from a URL
and contacts the server

Most URLs contain an explicit protocol reference of http:// or
omit the protocol altogether (HTTP is assumed)

HTTP can be characterized as follows:

— Uses textual control messages

— Transfers binary data files

— Can download or upload data
— Incornoratesc cachina

Request Description

GET Requests a document; server responds by sending status
information followed by a copy of the document

Requests status information; server responds by sending

READ status information, but does not send a copy of the document

POST Sends data to a server; the server appends the data to a
specified item (e.g., a message is appended to a list)

PUT Sends data to a server; the server uses the data to completely

replace the specified item (i.e., overwrites the previous data)
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

[Text in pictures on this page, read by OCR]
Block Error Codes
— It divides the data to be sent into a set of blocks
— It attaches extra information known as redundancy to each block

— The encoding for a given block of bits depends only on the bits
themselves, not on bits that were sent earlier

— They are memoryless in the sense that the encoding mechanism
does not carry state information from one block of data to the next
Convolutional Error Codes

— It treats data as a series of bits, and computes a code over a
continuous series

— Thus, the code computed for a set of bits depends on the current
input and some of the previous bits in the stream

— Convolutional codes are said to be codes with memory

Type Description

ALOHA Historic protocol used in an early radio network in
Hawaii; popular in textbooks and easy to analyze,
but not used in real networks

CSMA/CD | Carrier Sense Multi-Access with Collision Detection
The basis for the original Ethernet, and the most widely
used random access protocol

CSMA/CA Carrier Sense Multi-Access with Collision Avoidance
The basis for Wi-Fi wireless networks
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

[Text in pictures on this page, read by OCR]
Illustration Of CSMA/CA

1: ready to send (RTS)

~

2: clear to send (CTS) 2: clear to send (CTS)

3: packet transmission

= =

computer 1 computer 2 computer 3

Communicating pair exchange RTS and CTS before packet
transmission

Any computer less than 6 away from either computer 2 or 3
hears at least one of the RTS/CTS messages
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

[Text in pictures on this page, read by OCR]
1: Physical header (possible, but not likely)
2: Network Interface header

3: Internet header

aa,

|< message the application sent. ———————>

Figure 1.2 Illustration of how data passes among protocol layers when com-
puters communicate across a network. Each computer has a set

of layered protocols, and data passes through cach layer.
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

[Text in pictures on this page, read by OCR]
* Network Applications And Network Programming

+ A programmer who understands the underlying network mechanisms and technologies can
write network applications that are more reliable, correct, and efficient.

* Data Communications
+ Data communications provides a foundation of concepts on which the rest of networking
is built.
¢ Packet Switching And Networking Technologies

* Each network technology is created to meet various requirements for speed, distance, and
economic cost, many packet switching technologies exist. Technologies differ in details
such as the size of packets and the method used to identify a recipient.

* internetworking With LUP/Ir

* The Internet is formed by interconnecting multiple packet switching
networks. Internetworking is substantially more powerful than a sin- gle
networking technology because the approach permits new technologies to
be incorporated at any time without requiring the replacement of old
technologies.

¢ Additional Networking Concepts And Technologies
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
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

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

[Text in pictures on this page, read by OCR]
Caching provides an important optimization for web access
— because users tend to visit the same web sites repeatedly

Much of the content at a given site consists of large images
— Graphics Image Format (GIF)

— Joint Picture Encoding Group (JPEG)

Such images often contain backgrounds or banners

— they do not change frequently
A browser can reduce download times significantly

— by saving a copy of each image in a cache on the user's disk and
using the cached copy

Whenever a browser obtains a document from a web server, the header
specifies the last time the document was changed

A browser saves the Last-Modified date information along with the
cached copy

— Abrowser makes a HEAD request to the server and compares the Last-
Modified date of the server's copy to the Last-Modified date in the cached

— Ifthe cached version is stale, the browser downloads the new version
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

[Text in pictures on this page, read by OCR]
Name | Expansion Description

Direct Similar to CDMA where a sender multiplies
DSSS | Sequence the outgoing data by a sequence to form

Spread multiple frequencies and the receiver

Spectrum multiplies by the same sequence to decode

Frequency A sender uses a sequence of frequencies

FHSS | Hopping to transmit data, and a receiver uses the
Spread same sequence of frequencies to extract
Spectrum data

Orthogonal A frequency division multiplexing scheme

OFDM | Frequency where the transmission band is divided
Division into many carriers in such a way that
Multiplexing | the carriers do not interfere
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

[Text in pictures on this page, read by OCR]
* Any program that contacts another is acting as a client, and any program that accepts
contact from another is acting as a server.
* In practice, the distinction blurs because a server for one service can act as a client for
another.
* For example, before it can fill in a web page, a web server may need to become a
client of a database. A server may also become the client of a security service
(e.g., to verify that a client is allowed to access the service).
* Ofcourse, programmers must be careful to avoid circular dependencies among
servers.

* For example, consider what can happen if a server for service X1 becomes a client of
service X2, which becomes a client of service X3, which becomes a client of X1. The
chain of requests can continue indefinitely until all three servers exhaust resources.
The potential for circularity is especially high when services are designed
independently because no single programmer controls all servers.

The question arises, “can Internet services be provided without creating a central
bottleneck?”

* One way to avoid a bottleneck forms the basis of file-sharing applications known
as a peer-to-peer (p2p) architecture, the scheme avoids placing data on a central
server. Conceptually, data is distributed equally among a set of N servers, and
each client request is sent to the appropriate server.

¢ Because a given server only provides 1/N of the data, the amount of traffic
between a server and the Internet is 1/N as much as in the single-server
architecture. Thus, the server software can run on the same computers as the
clients.
--- page 4 ---
Q3   a. Explain the types of guided and unguided transmission media in detail along with the   [10]
CO- 2;   diagram of each.
SO-1;
BL-2   Explanation of guided transmission– 6 M
Explanation of unguided transmission– 2 M
Diagrams if any – 2M
********** 4 **********

[Text in pictures on this page, read by OCR]
Circuit switching provides 1-to-1 dedicated connections

—_— network
- a ~" > —_. -
XS F

Packet switching provides statistical TDM sharing

packet-switched network

>
“mmo oo =
< ON AL >»

=

Scenario Circuit-Switched Example Packet-Switched Example

Phone Call Traditional landline call using PSTN VoIP call over Skype or WhatsApp

Internet N/A (Web traffic cannot use circuit Data packets sent over the Internet (TCP/IP)
Browsing switching)

TV Broadcasting Dedicated satellite TV transmission Streaming services like Netflix, YouTube
Office Network Private leased lines for voice calls Ethernet or Wi-Fi network for data

transmission
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

[Text in pictures on this page, read by OCR]
Ba Guided/ Bounded Media UnGuided/ UnBounded Media
Transmission Guided is wired transmission, in | Unguided/ Unbounded
which data signals are guided communication is wireless
along a physical path i.e. within | transmission. To exchange bits
awire of data for laptop, notebook,

smart watch, without wires,
you need wireless
communication.

Also, called? Guided transmission is also UnGuided transmission is also
known as Bounded known as UnBounded
Transmission Media. Transmission Media.

Media Types Some well-known Guided UnGuided Transmission media
Transmission media includes includes Microwave
Twisted Pair Cable, Coaxial Transmission, Satellite
cable, fiber optic cable, etc. Communication, etc.

Media The media can be seen and The media is wireless and
touched i.e. tangible. cannot be seen and touched i.e.

intangible.
Distance Used for shorter distance. Used for larger distance.
Penetration Guided Media cannot UnGuided Media can penetrate

penetrate through the buildings | through the buildings.
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

[Text in pictures on this page, read by OCR]
Prefix Suffix | Type Of Address Purpose

all-Os all-Os | this computer used during bootstrap

network | all-Os | network identifies a network

network | all-1s | directed broadcast | broadcast on specified net

all-1s all-is | limited broadcast broadcast on local net

127/8 any loopback testing

Server Application Client Application

Starts first Starts second

Does not need to know which client | Must know which server to
will contact it contact

Waits passively and arbitrarily long | Initiates a contact whenever
for contact from a client communication is needed

Communicates with a client by both | Communicates with a server by
sending and receiving data sending and receiving data

Stays running after servicing one May terminate after interacting
client, and waits for another with a server
--- page 7 ---
Q4   b.   a) A communication channel has a bandwidth of 5 kHz. What is the maximum data rate that   [5]
CO-2;   can be transmitted through this channel if it is a noise-free channel using binary signaling?
SO-2;
BL-3   Step marking – 5M each
b) A channel has a bandwidth of 3 kHz and a signal-to-noise ratio (SNR) of 30 dB. Calculate   [5]
the maximum data rate that can be achieved using Shannon’s Capacity formula.
********** 7 **********

[Text in pictures on this page, read by OCR]
The term refers to a program that waits passively for communication, and not to the
computer on which it executes. However, when a computer is dedicated to running
one or more server programs, the computer itself is sometimes called a server.
Hardware vendors contribute to the confusion because they classify computers that
have fast CPUs, large memories, and powerful operating systems as server machines.

client runs Server runs in
in a standard a server-class
computer computer

| connection Internet
— | _£ < > >
9 ——————— > :

€ nN 2 )

Nyquist theorem states that the maximum data rate for a noiseless channel is:
C=2-x Bx log,(M)

For binary signaling (IM = 2):
C = 2 x 5000 x logs(2)

Since log, (2) = 1:

C =2 x 5000 x 1= 10,000 bps (or 10 kbps)
--- page 8 ---
Q5   a. Classify Addressing in Local Area Networks (LAN). Explain MAC addressing, its   [10]
CO-2;   components, and differentiate between unicast, multicast, and broadcast addressing.
SO-1;
BL-2   Explanation of each sub parts – 5M
********** 8 **********

[Text in pictures on this page, read by OCR]
Shannon's theorem states:
C = Blog»(1+ SNR)
Given:
¢ B= 3000 Hz
e¢ SNR in dB = 30 dB
First, convert SNR from dB to a linear scale:
SN Riimear = 10(SNRan/10) _ 19 (30/10) _ 493 — 1999
Now, apply the formula:
C = 3000 log,(1 + 1000)
C = 3000 log,(1001)
Approximating logs(1001) ~ 9.97:

C = 3000 x 9.97 = 29,910 bps (or 29.91 kbps)

Formal name: JEEE Media Access Control address (MAC
address)

Informally called an Ethernet address
Each address is 48 bits long

Assigned to Network Interface Card (NIC) when device
manufactured

Divided into subfields
— 3-byte Organizationally Unique ID (OUI)
— 3-byte Network Interface Controller (NIC)
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

[Text in pictures on this page, read by OCR]
Illustration Of Fields In An IEEE 48-Bit Address

3 bytes 3 bytes
T T T T
Organizationally Unique Network Interface Controller
Identifier (OUI) (NIC) specific

4 1 i 4

/ bits of most significant byte
L1l2[s[4[sje]7][e}

0 — unicast, 1—> multicast
0 — global, 1 local

e Address types

Address Type Meaning And Packet Delivery

unicast Destination is a single computer; only that computer
should receive a copy of the packet

broadcast Destination is all computers on a network; they
should each receive a copy of the packet

multicast A subset of the computers on a network should
receive a copy of the packet
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

[Text in pictures on this page, read by OCR]
LAYER 5

Application
Transport LAYER 4
Internet LAYER 3
LAYER 2

Network Interface

LAYER |

Physical
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

[Text in pictures on this page, read by OCR]
router R, router R, router R,

ers WA “one / a as/

{30.0.0.0/8 GSD | GD" Ge 1.0. a 9 a 2.4.10,0/2

40.0.0.7 128.1.0.8 192.4.10.9
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

[Text in pictures on this page, read by OCR]
The growth in NW has an economic impact:

— Data NW have made telecommuting available to
individuals and have changed business communication

— In addition, an entire industry has emerged that develops
NW technologies, products, and services

— The popularity and importance of computer NW has
produced a demand in all industries for people with more
NW expertise

— Companies need workers to plan, acquire, install, operate,
and manage the hardware (HW) and software (SW)
systems that comprise computer NW and internets

NW can be especially confusing to a beginner
— because there is no single underlying theory that explains the
relationship among all parts.
In fact, various organizations and research groups have
attempted to define conceptual models that can be used
— to explain the differences and similarities among NW HW and
SW systems
Unfortunately, the set of technologies is diverse and
changing rapidly
— models are either so simplistic that they do not distinguish
among details
— or so complex that they do not help simplify the subject

Address 1 Address 2 Address 3 Payload
CTL|DUR! (destination) | (source) (dest.2) |SEQ) Address 4 (oto 2412 bytes) [CRC

| |

AP or wireless sender's router's used in
computer's MAC MAC address MAC address ad hoc mode
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

[Text in pictures on this page, read by OCR]
Feature 802.11 (Wi-Fi) Frame Ethernet Frame

Number of MAC Addresses 4 (to handle wireless forwarding) 2 (source and destination only)
Medium Wireless (Wi-Fi) Wired (Ethernet cable)
Frame Transmission Uses Access Points (APs) and routers Directly between devices via a switch

Mobility Support Supports roaming between APs Typically used in fixed networks

Component Description

Operates like a conventional telephone, but

IP telephone uses IP to send digitized voice

Provides control and coordination between
Media Gateway Controller | IP telephones for services such as call setup,
call termination, and call forwarding

Provides a connection between two networks
Media Gateway that use different encodings, and translates
as a call passes between them

Connects to two networks that use different
Signaling Gateway signaling mechanisms, and translates call
management requests and responses
--- page 14 ---
FRR IC 7 I OH
````
