# Digital Voice and Broadband Communication: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper dc4b2060cbb2

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006, MBATech (ELECTRONICS TELECOMMUNICATION
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_EXTC_7006/Digital Voice and Broadband Communication/ANS_Digital Voice and Broadband Communication(702EX0C027)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: mixed (16 pages), mean OCR confidence 81.2
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (EXTC)/MBA Tech (EXTC)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: Digital Voice and Broadband Communication
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1; SO-1;   a.   Define the following terms in context of telephone traffic theory:   [5]
BL-1   (i) Traffic offered
(ii) Traffic carried
(iii) Lost calls
Explain their significance in traffic engineering.
Answer- 3marks
•   Carried traffic is the volume of traffic actually carried by a switch, and
offered traffic is the volume of traffic offered to a switch.
•   Offered traffic minus carried traffic equals lost calls.
• A lost call is one that does not make it through a switch.
• A call is “lost” usually because it meets congestion or blockage at that
switch.
Significance in determining the GOS. 2 marks
• Grade of service expresses the probability of meeting blockage during
the BH and is commonly expressed by the letter p.
•   p = GOS=(A-A0)/A = Lost traffic/Offered traffic
CO-2; SO-   b.   Explain the need for network synchronization in digital communication   [5]
1;   systems. List the methods used to achieve synchronization.
BL-2   Answer-
Need – 3M
In digital communication systems, network synchronization is essential
to ensure that all devices (switches, multiplexers, transmission
equipment) operate in time alignment. Proper synchronization is
required to:
1. Prevent Bit Slips: Misalignment between transmitter and
receiver clocks can cause bits to be lost or inserted.
********** 1 **********
--- page 2 ---
2. Maintain Frame Integrity: Digital systems transmit data in
frames; timing errors can cause frame misalignment.
3. Avoid Jitter and Delay: Unsynchronized clocks can introduce
timing variations, affecting voice and data quality.
4. Enable Efficient Multiplexing: In systems like PDH/SDH,
precise timing is needed to combine multiple channels without
interference.
5. Ensure Reliable Network Operation: Large networks require
consistent timing to avoid propagation of errors and maintain
high-quality service.
Methods of Network Synchronization 2M
– Plesiochronous – Network wide Pulse Stuffing – Mutual Synchronization –
Network Master – Master-slave clocking – Packetization
CO-3; SO-1;   c.   What is companding. Explain the techniques of it with their significance.   [5]
BL-1,2
Answer-
Definition – 2M
•   compressing and expanding.
• A PCM compression technique where analogue   signal values are
rounded on a non-linear scale.
• The data is compressed before sent and then expanded at the receiving
end using the same non-linear scale.
• Companding reduces the noise and crosstalk levels at the receiver.
Techniques- 3M
(i) A-law Companding Technique
•   Uniform quantization is achieved at A = 1, where the characteristic
curve is linear and no compression is done.
• A-law has mid-rise at the origin. Hence, it contains a non-zero value.
• A-law companding is used for PCM telephone systems.
(ii) µ-law Companding Technique
•   Uniform quantization is achieved at µ = 0, where the characteristic
curve is linear and no compression is done.
•   µ-law has mid-tread at the origin. Hence, it contains a zero value.
•   µ-law companding is used for speech and music signals.
CO-4; SO-   d.   Explain the Digital Subscriber Line Access Multiplexer (DSLAM)   [5]
1;   architecture and its role in enabling broadband access.
BL-1,2
Answer-
Architecture diagram – 4M
********** 2 **********
--- page 3 ---
Role – 1M
• DSL modem is required at each end of the local loop.
• DSL actually signifies the pair of modems at each end of a line
and not the line at all.
Q2   a.   (i)   List and explain advantages of Common Channel Signaling (CCS)   [5]
CO-2; SO-1;   over Channel Associated Signaling (CAS).   - 5M
BL-2
• Channel Associated Signaling (CAS): Each voice channel
carries its own signaling information along with the voice (in-
band or out-of-band).
• Common Channel Signaling (CCS): A separate signaling
channel is used for multiple voice channels; the signaling is
independent of individual voice circuits (e.g., SS7).
Advantages of CCS over CAS:
Feature   Advantage of CCS
A single signaling channel can handle multiple
Efficiency
voice circuits, reducing signaling overhead.
Faster call setup and teardown because signaling is
Speed
independent of the voice channel.
Supports complex signaling like call forwarding,
Flexibility
caller ID, and advanced services.
Signaling is not blocked if voice channels are busy;
Reliability
more robust against congestion.
Security & Centralized signaling allows better monitoring,
Control   management, and protection against fraud.
Maintenanc Easier network management as signaling can be
e   upgraded independently from voice channels.
(ii)   Distinguish between Circuit-Related Signaling and Non-Circuit-
Related Signaling in SS7. Provide examples of each.   [5]
– 2.5 M each
1. Circuit-Related Signaling (CRS):
Definition: Signaling messages associated with establishing, maintaining, and
releasing a specific voice circuit.
********** 3 **********

[Text in pictures on this page, read by OCR]
==; Voice Switch

POTS _ 0
DSL Access Local Loop DSL Modem
Multiplexer (carrying both POTS
DSL data and DSL data/voice)

Customer Premises

Data
Network > mT
--- page 4 ---
Purpose: Ensures the circuit is ready before the call, monitors its state, and
releases it after completion.
Examples:
ISUP messages in SS7: IAM (Initial Address Message), ACM (Address
Complete Message), ANM (Answer Message), REL (Release Message)
2. Non-Circuit-Related Signaling (NCRS):
Definition: Signaling messages not tied to a specific circuit, used for network
management, database queries, or maintenance.
Purpose: Provides services like routing, mobility management, and database
access independently of a particular voice call.
Examples:
SCCP messages: MAP (Mobile Application Part) queries for mobile roaming,
HLR/VLR lookup, network management messages
Q2   b.   Explain the various variants of Digital Subscriber Line (DSL) technology   [10]
CO-4; SO-   including ADSL, HDSL, VDSL, and RADSL. Compare their characteristics,
1;   applications, and data rates in a tabular format.
BL-2
Answer – DSL variants naming – 4 M
Comparison including application – 6 M
Maximum
Maximum   Maximum
Wire   Customer
DSL Type Downstream   Upstream
Length   Applications
Data Rate   Data Rate
(Approx.)
Symmetric
DSL
HDSL   For enterprise data
1.544 Mbps   1.544 Mbps   3 km
(High-bit-   lines; replaces leased
(T1)   (T1)   (10,000 ft)
rate DSL)   lines for small offices
SDSL   Individual subscriber
3 km
(Single-line 2.3 Mbps   2.3 Mbps   premises; small office
(10,000 ft)
DSL)   use
SHDSL   Business applications
(Single-pair   3 km   requiring symmetric
2.3 Mbps   2.3 Mbps
High-speed   (10,000 ft) bandwidth in both
DSL)   directions
Asymmetric
DSL
Home and small office
ADSL   users requiring high-
5.5 km
(Asymmetric Up to 8 Mbps Up to 1 Mbps   speed internet, web
(18,000 ft)
DSL)   access, email,
multimedia
Residential and small
Up to 1.5   Up to 384
ADSL Lite   5.5 km   office users needing
Mbps   kbps
basic internet
********** 4 **********
--- page 5 ---
Improved performance
ADSL 2   Up to 12 Mbps Up to 3 Mbps 5.5 km   over ADSL; better for
video, VoIP
High-speed internet;
ADSL 2+   Up to 24 Mbps Up to 3 Mbps 5.5 km   supports IPTV and
multimedia streaming
Symmetric
&
Asymmetric
DSL
Campus environments,
Symmetric: up Symmetric: up   multi-dwelling units;
VDSL
to 52 Mbps   to 52 Mbps   1.2 km   supports video, data,
(Very-high-
Asymmetric:   Asymmetric:   (4,000 ft)   VoIP,
bit-rate DSL)
up to 55 Mbps up to 16 Mbps   teleconferencing, and
surveillance
Applications:
HDSL- Data only
SDSL- Individual subscriber premises with single telephone line
SHDSL- Business application
ADSL- Home and Small offices which requires faster download rates
ADSL lite- Residential and small office users – simple plug and play setup
ADSL 2 – demand for more bandwidth to support services
ADSL 2+ and ADSL 2++ - greater downstream data rates for subscriber who
are relatively near the telephone exchange
VDSL – Campus environment
Q3   a.   (i) Demonstrate the Session Initiation Protocol (SIP) architecture with neat   [7]
CO-3; SO-1;   and labeled diagram.
BL-2   (ii) Give a significant example of SIP message format.   [3]
Answer – SIP architecture – 3M ; Explanation – 4M
Message format – 3M
Message format
********** 5 **********

[Text in pictures on this page, read by OCR]
SIP - Architecture

SIP Proxy Server
SIP Redirect Server
SIP Registrar Server

SIP

Router
( Access Node
Gateway )

SIP Phone

( User Agents /
SIP End-points / softphones }
--- page 6 ---
Q3   b.   (i) Compare and contrast Gigabit PON (GPON) and Ethernet PON   [8]
CO-5; SO-1;   (EPON) technologies. Discuss the following aspects:
BL-2   •   Data rates and transmission speeds
•   Frame structures and encapsulation methods
•   Standards (ITU-T vs IEEE)
•   Advantages and typical applications
(ii) Draw the architecture of both PON systems with proper labeling.   [2]
Answer –
Comparison each 4 M
(i) Comparison of GPON and EPON
GPON (Gigabit Passive EPON (Ethernet Passive
Feature
Optical Network)   Optical Network)
Symmetric: 1 Gbps
Data Rates / Downstream: 2.488 Gbps,
downstream/upstream
Transmissio Upstream: 1.244 Gbps
(10G-EPON also
n Speeds   (GPON standard)
available)
Uses GTC (GPON
Transmission
Uses standard Ethernet
Frame   Convergence) layer;
frames (IEEE 802.3);
Structures / supports variable-length
encapsulates Ethernet
Encapsulati GEM frames;
directly without additional
on   encapsulates various
layers
protocols including
Ethernet, ATM, TDM
Standards ITU-T G.984 series   IEEE 802.3ah / 802.3av
Efficient bandwidth   Simpler implementation;
utilization; supports   uses existing Ethernet
multiple service types   infrastructure; easy
Advantages
(voice, video, data); QoS   integration with LANs;
support; longer reach (~20 lower cost; flexible
km)   upgrades
********** 6 **********

[Text in pictures on this page, read by OCR]
INVITE sip:6455389@ rad.co.il SIP/2.0
From: WoP student

To Yaakov (7) Stein

Call-ID: 5531212 @bynet-academy.co.il
CSeq: | INVITE

Subject How to use SIP

Content-Type: application/sdp

etc.
--- page 7 ---
Triple-play services   FTTH for residential or
Typical
(Internet, IPTV, VoIP);   small business; enterprise
Application
FTTH deployments   access networks; cost-
s
requiring high bandwidth   sensitive deployments
Architectur
e – 2M
Q4   a.   Explain timing inaccuracies in digital communication networks. Demonstrate   [10]
CO-2; SO-1;   the following in detail with neat diagram.:
BL-2   •   The concept of slips (positive and negative slips)
•   How elastic stores (buffers) are used to prevent slips
Answer-
Timing Inaccuracies - 5M
• Three types of timing Inaccuracies – Slips – Asynchronous Multiplexing –
Waiting Time Jitter
• Slips (Bit Slips / Frame Slips)
•   Definition: Loss or insertion of a bit or frame due to a mismatch
between transmitter and receiver clocks.
• Cause: Small differences in clock frequency (transmitter faster
or slower than receiver).
•   Effect: Can corrupt data or voice, requiring error
detection/correction.
• Asynchronous Multiplexing
•   Definition: Occurs when multiplexing of digital signals is done
without strict timing alignment between input signals.
********** 7 **********

[Text in pictures on this page, read by OCR]
Need multipoint Internet VLAN:
all services need a VLAN ID.

Ethernet segment

No need VLAN:
for provider only

Ethernet segment
--- page 8 ---
• Cause: Input signals have slightly different clock rates, leading
to timing misalignment.
•   Effect: Requires justification bits or buffer adjustments to
accommodate differences, otherwise leads to errors.
• Waiting Time Jitter (Delay Variation)
•   Definition: Variation in arrival time of data packets or frames at
the receiver.
• Cause: Network delays, buffering, or variable processing times.
•   Effect: Causes voice or data distortion, especially in real-time
communications; may require jitter buffers to compensate.
Slips - Explain and diagram – 2.5 M each
• Disruption in data stream caused by underflow and overflow is called Slip. •
Uncontrolled Slip can lead to loss of frame synchronization. • Approach to
control slip is to repeat or delete entire frame when slip occurs. • Thus the
time slot counters and framing logic associated with the multiplex group
remain synchronize. • Controlled slips comprising entire frames can be carried
out by using ES that can store at least one frame of storage (data).
• Elastic store is a data buffer that is written by one clock and read by another
clock.
• ES absorbs instability in clock by using recovered clock based on received
stream clk.
• If short-term instability exists in either clk, ES absorbs the difference in the
amount of data transmitted and the amount of data received.
• If there is sustained clock offset the ES will eventually overflow or
underflow causing timing inaccuracies.
• When R2 is greater than R1, the elastic store at the first digital switch
overflows, causing a loss of data. If R2 is less than R1, the same elastic store
underflows, causing extraneous data to be inserted into the bit stream entering
the switch
Q4   b.   Illustrate the both types of Cable Modem Service architecture in detail.   [10]
CO-5; SO-
1;   Answer- Both type CM diagram – 6 M , Explanation 4 M ,
BL- 2
********** 8 **********
--- page 9 ---
Q5   a.   Explain voice coding techniques comprehensively. classify the following:   [10]
CO-3; SO-1;   •   Properties of speech that enable compression
BL-2,   •   Codec Principles and approaches
Answer – each techniques – 3M , any diagram – 1 M
Speech Codecs
• Waveform codec • Source codec (vocoders) • Hybrid codec
Waveform Codec
• Waveform codecs reconstructed signal whose waveform is as close as
possible to the original without the knowledge of how signal to be coded was
generated. • This means that in theory they should be signal independent and
work well with non-speech signals. • Generally they are low complexity
codec’s which produce high quality speech at rates above about 16 kbits/s. •
When the data rate is lowered below this level the reconstructed speech
quality that can be obtained degradesrapidly. • Pulse code modulation (PCM)
is the simplest way of waveform coding which simply involves sampling and
quantizing the input waveform.
Source Codec (vocoder)
• Source coders operate using a model of how the source was generated, and
attempt to extract parameters, from the signal being coded, the parameters of
********** 9 **********

[Text in pictures on this page, read by OCR]
Cable modem transmission system (CMTS)

l yi | Fiber
From head end—+ Wee Combiner

| A |

Distribution hub
| |
| |

Toand from | Data —ap |
the Internet — | |
--- page 10 ---
the model. • It is these model parameters that are transmitted to the decoder. •
Source coders for speech are called vocoders, and work as follows. • The
vocal tract is represented as a time-varying filter and is excited with either a
white noise source, for unvoiced speech segments, or a train of pulses
separated by the pitch period for voiced speech. • Therefore the information
which must be sent to the decoder is the filter specification, a voiced/unvoiced
flag, the necessary variance of the excitation signal, and the pitch period for
voiced speech.
Hybrid Codec
• Hybrid codecs attempt to fill the gap between waveform and source codecs. •
Waveform coders are capable of providing good quality speech at bit rates
down to about 16 kbits/s, but are of limited use at rates below this. • Source
coders on the other hand can provide intelligible speech at 2.4 kbits/s and
below, but cannot provide natural sounding speech at any bit rate. • Although
other forms of hybrid codecs exist, the most successful and commonly used
are time domain Analysis-by-Synthesis (AbS) codecs.
Q5   b.   (i) Illustrate the operating principle of Discrete Multitone (DMT)   [4]
CO-4; SO-1;   modulation.
BL-2   (ii) Explain two significant advantages of DMT in handling frequency- [2]
selective channel impairments.
(iii) Compare DMT with Carrierless Amplitude Phase (CAP) modulation.   [4]
Answer-
(i) Operating Principle of Discrete Multitone (DMT) Modulation –
4M
Discrete Multitone (DMT) is a multicarrier modulation technique used
in DSL systems to transmit high-speed data over existing copper
telephone lines.
Operating Principle:
1. The available bandwidth of the telephone line is divided into
multiple orthogonal subcarriers (typically 256 or more).
2. Each subcarrier is independently modulated using QAM
(Quadrature Amplitude Modulation).
3. Data bits are distributed among the subcarriers according to
the signal-to-noise ratio (SNR) of each subcarrier (adaptive bit
loading).
4. Subcarriers with high noise carry fewer bits, while clear
subcarriers carry more bits.
5. At the receiver, a Fast Fourier Transform (FFT) separates
subcarriers and recovers the transmitted data.
(ii) Two Significant Advantages of DMT in Handling Frequency-
Selective Channel Impairments – 2M
1. Adaptive Bit Loading:
o DMT measures the SNR of each subcarrier and
allocates bits accordingly.
o Subcarriers affected by attenuation or noise carry fewer
bits or are disabled, while clear subcarriers carry more.
********** 10 **********
--- page 11 ---
o Advantage: Maximizes overall data rate and minimizes
errors despite frequency-dependent impairments.
2. Parallel Transmission over Multiple Subcarriers:
o Data is transmitted simultaneously on many narrowband
subcarriers rather than a single wideband carrier.
o Advantage: Reduces the impact of frequency-selective
fading, as poor subcarriers do not affect the entire signal.
(iii) Comparison of DMT and Carrierless Amplitude Phase (CAP) Modulation
- 2M each
DMT (Discrete   CAP (Carrierless Amplitude
Feature
Multitone)   Phase)
Modulation   Multicarrier QAM over   Single-carrier two-dimensional
Technique   orthogonal subcarriers   amplitude/phase modulation
Divides available
Bandwidth   Uses full available bandwidth
bandwidth into many
Utilization   as one channel
subcarriers
Resilience to High; bad subcarriers can Less; entire channel affected
Noise   be avoided   by noise in one frequency band
Higher; requires FFT/IFFT
Complexity   Lower; simpler implementation
processing
Can achieve higher data
Moderate; limited by single-
Data Rate   rates with adaptive bit
carrier frequency response
loading
Adaptive bit loading per
Fixed modulation; less
Adaptability subcarrier for line
adaptive
conditions
Early ADSL implementations,
Use Case   ADSL, VDSL
legacy DSL systems
Q6   a.   (i) Explain the Erlang B and Erlang C formulas used in telephone traffic   [6]
CO-1; SO-2;   theory. Discuss:
BL-2   •   The mathematical formulation of both formulas
•   When each formula is appropriately used (loss systems vs.
delay systems)
•   The assumptions underlying each formula
Answer-
Each formula and concept – 3 marks
Erlang B specifies the probability of blocking for a system with random
arrivals from an infinite source and arbitrary holding time distributions.
********** 11 **********
--- page 12 ---
Blocking probability : B Offered traffic intensity : A Number of circuits
provided/channles/servers : N
Erlang's Delay Formula or Erlang's C formula
(ii) In a telephone exchange, 400 calls are offered during the busy hour.   [4]
The average call duration is 4 minutes.
a. Calculate the total traffic offered in Erlangs.
b. Determine how many circuits (channels) would be occupied on
average during the busy hour.
c. Comment briefly on what the result implies in terms of network
capacity planning.
Answer-
Number of calls = 400 calls/hour
Average call duration = 4 minutes = 4/60 = 0.0667 hours   - 1M
Traffic offered (A):   Formula and calculation 2M
A=400×0.0667=26.68Erlangs
Interpretation: 1M
• This means that, on average, 26.68 circuits are continuously
occupied during the busy hour.
• The exchange must therefore have more than 27 circuits to
handle this load efficiently without excessive call blocking.
Q6   b.   (i) Explain LoRaWAN working principle.   [3]
CO-5; SO-1;   (ii) Compare LoRaWAN with Narrowband IoT (NB-IoT) technology on   [7]
BL-2   various parameters.
Answer –
Working principle – 3M
LoRaWAN (Long Range Wide Area Network) is a low-power, wide-area
network protocol designed for IoT devices that need long-range
communication with low data rates. It uses a star-of-stars topology, where
battery-powered end devices (sensors/actuators) communicate with gateways
via LoRa modulation. Gateways act as transparent relays, forwarding
messages to a network server, which manages device authentication,
deduplication, and security, and then passes the data to an application server
for processing. LoRaWAN supports uplink and downlink communication,
uses adaptive data rate (ADR) to optimize battery life and network efficiency,
********** 12 **********

[Text in pictures on this page, read by OCR]
So, the probability that a call experiences congestion and therefore it
delayed is given by-

7 NB

~ N—A(1— B)

Where, N= no. of servers, A= ofered load (Er) and B = Blocking
Probability for LCC system.

Prob(delay)= P(> 0)
--- page 13 ---
and provides end-to-end encryption. Its combination of long-range, low power
consumption, and simple infrastructure makes it ideal for IoT applications
such as smart agriculture, smart cities, and asset tracking.
Comparison- 7 M
Basic   LoRaWAN   NB−IoT
Parameter
System   It is supported by LoRa   It supports 3GPP.
Alliance.
License   It is unlicensed by ISM.   It is Licensed by LTE
spectrum.
Security   LoRaWAN is not licensed   NB&miuns;IoT is licensed
which leads to security   which leads to increased
issues.   security.
Spectrum   It is optimized over a   As it is licensed, they are very
long−range using Internet   expensive.
of Things sensors that is
free.
Network type   LoRaWAN is flexible so it   NB−IoT is fixed for the 4G
can choose among the   technology that is LTE (Long
public, private, and hybrid   Term Evolution).
networks.
Data Rate   The Data rate ranges   The data rate is somewhat
between 293bps and   near 20kbps.
50kbps.
Implementation   The deployment cost is   The deployment cost is very
Cost   very low and it can be   high and it can be installed by
installed by anyone.   mobile network operators.
Mobility   It provides a mobility   It is limited to idle mode.
function.
Q7   a.   What is traffic characterization in telephone networks? Explain the concepts   [5]
CO-1; SO-1;   of arrival time distribution and holding time distribution with suitable
BL-1,2   examples.
Answer –
Basic assumption in traffic analysis :   1M
– Arrival from one source is independent of the arrival from other sources.
In those cases where call arrivals tend to be correlate, useful results can be
obtained by modifying a random arrival analysis.
Average call arrival rate from a large group of subscriber lines=λ (arrivals /
second)
********** 13 **********
--- page 14 ---
Arrival Time – 2M
Holding Time – 2M
Q7   b.   Explain the Phase Locked Loop (PLL) technique used for timing recovery in   [5]
CO-2; SO-1;   network synchronization. Draw a block diagram and describe its operation.
BL-2
Explanation – 3M and diagram – 2M
********** 14 **********
--- page 15 ---
PLL Clock Recovery

¢ Phase detector
continuously measures
the phase difference
between I/C Clk and

Local Clk.

* Measures the
difference in zero
crossing between two
clocks.

PLL Clock Recovery

* When zero crossing of line Clk
precedes the zero crossing of local
Clk +ve voltage is generated
otherwise —-ve

+ This voltage is used for adjusting
Voltage Control Oscillator (VCO) to
reduce the phase difference

* Local Clock maintains the desired
average frequency but using PLL
produces short term variations of
phase & frequency to maintain
underlying frequency of the line

clock
Q7 Cc. Compare PSTN and VoIP networks, atleast 8 points to be mentioned. [5]
CO-3; SO-1;
BL-2 Answer — each network — 2.5 M

SS ES
Underlying Technology TDM circuit switching

Network resource reserved . :
Yes No
at call setup
. (Class 4, Class § switching Gateways, gateway
Network ekments ° ve .
systenas controllers, routers

. ae , Mostly integrated in Inseparate gateways and
Call processing intelligence ce .
switching system controllers

Bandwidth per call Variable §- 64+ kh's

MF, DTME, S37 SIP, H.323, MGC PYH.248

Depends on network

Transport TDM in access, edge, core topology (IF, ATM, other)

FRR IC 7 DA HOH
--- page 16 ---
Q7   d.   Explain the functions of Optical Line Termination (OLT) and Optical   [5]
CO-5; SO-1;   Network Terminals (ONT) in Passive Optical Network (PON) architecture
BL-2
Answer – Explanation – 3 M , Diagram – 2M
downstream
upstream
NNI
ptical istributionNetwork   ptical Network nits
core
splitter
ptical ine Terminal   UNI
ptical ccessNetwork   Terminal quipment
********** 16 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 7fbc43acec79

- Departments: Electronics and Telecommunication
- Programmes: MBATech (ELECTRONICS & TELECOMMUNICATIO
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/MBATech (ELECTRONICS & TELECOMMUNICATIO_ba3ceaa3/Digital Voice and Broadband Communication/ANS_Digital Voice and Broadband Communication(702EX0C027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: mixed (16 pages), mean OCR confidence 81.2
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (EXTC)/MBA Tech (EXTC)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: Digital Voice and Broadband Communication
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1; SO-1;   a.   Define the following terms in context of telephone traffic theory:   [5]
BL-1   (i) Traffic offered
(ii) Traffic carried
(iii) Lost calls
Explain their significance in traffic engineering.
Answer- 3marks
•   Carried traffic is the volume of traffic actually carried by a switch, and
offered traffic is the volume of traffic offered to a switch.
•   Offered traffic minus carried traffic equals lost calls.
• A lost call is one that does not make it through a switch.
• A call is “lost” usually because it meets congestion or blockage at that
switch.
Significance in determining the GOS. 2 marks
• Grade of service expresses the probability of meeting blockage during
the BH and is commonly expressed by the letter p.
•   p = GOS=(A-A0)/A = Lost traffic/Offered traffic
CO-2; SO-   b.   Explain the need for network synchronization in digital communication   [5]
1;   systems. List the methods used to achieve synchronization.
BL-2   Answer-
Need – 3M
In digital communication systems, network synchronization is essential
to ensure that all devices (switches, multiplexers, transmission
equipment) operate in time alignment. Proper synchronization is
required to:
1. Prevent Bit Slips: Misalignment between transmitter and
receiver clocks can cause bits to be lost or inserted.
********** 1 **********
--- page 2 ---
2. Maintain Frame Integrity: Digital systems transmit data in
frames; timing errors can cause frame misalignment.
3. Avoid Jitter and Delay: Unsynchronized clocks can introduce
timing variations, affecting voice and data quality.
4. Enable Efficient Multiplexing: In systems like PDH/SDH,
precise timing is needed to combine multiple channels without
interference.
5. Ensure Reliable Network Operation: Large networks require
consistent timing to avoid propagation of errors and maintain
high-quality service.
Methods of Network Synchronization 2M
– Plesiochronous – Network wide Pulse Stuffing – Mutual Synchronization –
Network Master – Master-slave clocking – Packetization
CO-3; SO-1;   c.   What is companding. Explain the techniques of it with their significance.   [5]
BL-1,2
Answer-
Definition – 2M
•   compressing and expanding.
• A PCM compression technique where analogue   signal values are
rounded on a non-linear scale.
• The data is compressed before sent and then expanded at the receiving
end using the same non-linear scale.
• Companding reduces the noise and crosstalk levels at the receiver.
Techniques- 3M
(i) A-law Companding Technique
•   Uniform quantization is achieved at A = 1, where the characteristic
curve is linear and no compression is done.
• A-law has mid-rise at the origin. Hence, it contains a non-zero value.
• A-law companding is used for PCM telephone systems.
(ii) µ-law Companding Technique
•   Uniform quantization is achieved at µ = 0, where the characteristic
curve is linear and no compression is done.
•   µ-law has mid-tread at the origin. Hence, it contains a zero value.
•   µ-law companding is used for speech and music signals.
CO-4; SO-   d.   Explain the Digital Subscriber Line Access Multiplexer (DSLAM)   [5]
1;   architecture and its role in enabling broadband access.
BL-1,2
Answer-
Architecture diagram – 4M
********** 2 **********
--- page 3 ---
Role – 1M
• DSL modem is required at each end of the local loop.
• DSL actually signifies the pair of modems at each end of a line
and not the line at all.
Q2   a.   (i)   List and explain advantages of Common Channel Signaling (CCS)   [5]
CO-2; SO-1;   over Channel Associated Signaling (CAS).   - 5M
BL-2
• Channel Associated Signaling (CAS): Each voice channel
carries its own signaling information along with the voice (in-
band or out-of-band).
• Common Channel Signaling (CCS): A separate signaling
channel is used for multiple voice channels; the signaling is
independent of individual voice circuits (e.g., SS7).
Advantages of CCS over CAS:
Feature   Advantage of CCS
A single signaling channel can handle multiple
Efficiency
voice circuits, reducing signaling overhead.
Faster call setup and teardown because signaling is
Speed
independent of the voice channel.
Supports complex signaling like call forwarding,
Flexibility
caller ID, and advanced services.
Signaling is not blocked if voice channels are busy;
Reliability
more robust against congestion.
Security & Centralized signaling allows better monitoring,
Control   management, and protection against fraud.
Maintenanc Easier network management as signaling can be
e   upgraded independently from voice channels.
(ii)   Distinguish between Circuit-Related Signaling and Non-Circuit-
Related Signaling in SS7. Provide examples of each.   [5]
– 2.5 M each
1. Circuit-Related Signaling (CRS):
Definition: Signaling messages associated with establishing, maintaining, and
releasing a specific voice circuit.
********** 3 **********

[Text in pictures on this page, read by OCR]
==; Voice Switch

POTS _ 0
DSL Access Local Loop DSL Modem
Multiplexer (carrying both POTS
DSL data and DSL data/voice)

Customer Premises

Data
Network > mT
--- page 4 ---
Purpose: Ensures the circuit is ready before the call, monitors its state, and
releases it after completion.
Examples:
ISUP messages in SS7: IAM (Initial Address Message), ACM (Address
Complete Message), ANM (Answer Message), REL (Release Message)
2. Non-Circuit-Related Signaling (NCRS):
Definition: Signaling messages not tied to a specific circuit, used for network
management, database queries, or maintenance.
Purpose: Provides services like routing, mobility management, and database
access independently of a particular voice call.
Examples:
SCCP messages: MAP (Mobile Application Part) queries for mobile roaming,
HLR/VLR lookup, network management messages
Q2   b.   Explain the various variants of Digital Subscriber Line (DSL) technology   [10]
CO-4; SO-   including ADSL, HDSL, VDSL, and RADSL. Compare their characteristics,
1;   applications, and data rates in a tabular format.
BL-2
Answer – DSL variants naming – 4 M
Comparison including application – 6 M
Maximum
Maximum   Maximum
Wire   Customer
DSL Type Downstream   Upstream
Length   Applications
Data Rate   Data Rate
(Approx.)
Symmetric
DSL
HDSL   For enterprise data
1.544 Mbps   1.544 Mbps   3 km
(High-bit-   lines; replaces leased
(T1)   (T1)   (10,000 ft)
rate DSL)   lines for small offices
SDSL   Individual subscriber
3 km
(Single-line 2.3 Mbps   2.3 Mbps   premises; small office
(10,000 ft)
DSL)   use
SHDSL   Business applications
(Single-pair   3 km   requiring symmetric
2.3 Mbps   2.3 Mbps
High-speed   (10,000 ft) bandwidth in both
DSL)   directions
Asymmetric
DSL
Home and small office
ADSL   users requiring high-
5.5 km
(Asymmetric Up to 8 Mbps Up to 1 Mbps   speed internet, web
(18,000 ft)
DSL)   access, email,
multimedia
Residential and small
Up to 1.5   Up to 384
ADSL Lite   5.5 km   office users needing
Mbps   kbps
basic internet
********** 4 **********
--- page 5 ---
Improved performance
ADSL 2   Up to 12 Mbps Up to 3 Mbps 5.5 km   over ADSL; better for
video, VoIP
High-speed internet;
ADSL 2+   Up to 24 Mbps Up to 3 Mbps 5.5 km   supports IPTV and
multimedia streaming
Symmetric
&
Asymmetric
DSL
Campus environments,
Symmetric: up Symmetric: up   multi-dwelling units;
VDSL
to 52 Mbps   to 52 Mbps   1.2 km   supports video, data,
(Very-high-
Asymmetric:   Asymmetric:   (4,000 ft)   VoIP,
bit-rate DSL)
up to 55 Mbps up to 16 Mbps   teleconferencing, and
surveillance
Applications:
HDSL- Data only
SDSL- Individual subscriber premises with single telephone line
SHDSL- Business application
ADSL- Home and Small offices which requires faster download rates
ADSL lite- Residential and small office users – simple plug and play setup
ADSL 2 – demand for more bandwidth to support services
ADSL 2+ and ADSL 2++ - greater downstream data rates for subscriber who
are relatively near the telephone exchange
VDSL – Campus environment
Q3   a.   (i) Demonstrate the Session Initiation Protocol (SIP) architecture with neat   [7]
CO-3; SO-1;   and labeled diagram.
BL-2   (ii) Give a significant example of SIP message format.   [3]
Answer – SIP architecture – 3M ; Explanation – 4M
Message format – 3M
Message format
********** 5 **********

[Text in pictures on this page, read by OCR]
SIP - Architecture

SIP Proxy Server
SIP Redirect Server
SIP Registrar Server

SIP

Router
( Access Node
Gateway )

SIP Phone

( User Agents /
SIP End-points / softphones }
--- page 6 ---
Q3   b.   (i) Compare and contrast Gigabit PON (GPON) and Ethernet PON   [8]
CO-5; SO-1;   (EPON) technologies. Discuss the following aspects:
BL-2   •   Data rates and transmission speeds
•   Frame structures and encapsulation methods
•   Standards (ITU-T vs IEEE)
•   Advantages and typical applications
(ii) Draw the architecture of both PON systems with proper labeling.   [2]
Answer –
Comparison each 4 M
(i) Comparison of GPON and EPON
GPON (Gigabit Passive EPON (Ethernet Passive
Feature
Optical Network)   Optical Network)
Symmetric: 1 Gbps
Data Rates / Downstream: 2.488 Gbps,
downstream/upstream
Transmissio Upstream: 1.244 Gbps
(10G-EPON also
n Speeds   (GPON standard)
available)
Uses GTC (GPON
Transmission
Uses standard Ethernet
Frame   Convergence) layer;
frames (IEEE 802.3);
Structures / supports variable-length
encapsulates Ethernet
Encapsulati GEM frames;
directly without additional
on   encapsulates various
layers
protocols including
Ethernet, ATM, TDM
Standards ITU-T G.984 series   IEEE 802.3ah / 802.3av
Efficient bandwidth   Simpler implementation;
utilization; supports   uses existing Ethernet
multiple service types   infrastructure; easy
Advantages
(voice, video, data); QoS   integration with LANs;
support; longer reach (~20 lower cost; flexible
km)   upgrades
********** 6 **********

[Text in pictures on this page, read by OCR]
INVITE sip:6455389@ rad.co.il SIP/2.0
From: WoP student

To Yaakov (7) Stein

Call-ID: 5531212 @bynet-academy.co.il
CSeq: | INVITE

Subject How to use SIP

Content-Type: application/sdp

etc.
--- page 7 ---
Triple-play services   FTTH for residential or
Typical
(Internet, IPTV, VoIP);   small business; enterprise
Application
FTTH deployments   access networks; cost-
s
requiring high bandwidth   sensitive deployments
Architectur
e – 2M
Q4   a.   Explain timing inaccuracies in digital communication networks. Demonstrate   [10]
CO-2; SO-1;   the following in detail with neat diagram.:
BL-2   •   The concept of slips (positive and negative slips)
•   How elastic stores (buffers) are used to prevent slips
Answer-
Timing Inaccuracies - 5M
• Three types of timing Inaccuracies – Slips – Asynchronous Multiplexing –
Waiting Time Jitter
• Slips (Bit Slips / Frame Slips)
•   Definition: Loss or insertion of a bit or frame due to a mismatch
between transmitter and receiver clocks.
• Cause: Small differences in clock frequency (transmitter faster
or slower than receiver).
•   Effect: Can corrupt data or voice, requiring error
detection/correction.
• Asynchronous Multiplexing
•   Definition: Occurs when multiplexing of digital signals is done
without strict timing alignment between input signals.
********** 7 **********

[Text in pictures on this page, read by OCR]
Need multipoint Internet VLAN:
all services need a VLAN ID.

Ethernet segment

No need VLAN:
for provider only

Ethernet segment
--- page 8 ---
• Cause: Input signals have slightly different clock rates, leading
to timing misalignment.
•   Effect: Requires justification bits or buffer adjustments to
accommodate differences, otherwise leads to errors.
• Waiting Time Jitter (Delay Variation)
•   Definition: Variation in arrival time of data packets or frames at
the receiver.
• Cause: Network delays, buffering, or variable processing times.
•   Effect: Causes voice or data distortion, especially in real-time
communications; may require jitter buffers to compensate.
Slips - Explain and diagram – 2.5 M each
• Disruption in data stream caused by underflow and overflow is called Slip. •
Uncontrolled Slip can lead to loss of frame synchronization. • Approach to
control slip is to repeat or delete entire frame when slip occurs. • Thus the
time slot counters and framing logic associated with the multiplex group
remain synchronize. • Controlled slips comprising entire frames can be carried
out by using ES that can store at least one frame of storage (data).
• Elastic store is a data buffer that is written by one clock and read by another
clock.
• ES absorbs instability in clock by using recovered clock based on received
stream clk.
• If short-term instability exists in either clk, ES absorbs the difference in the
amount of data transmitted and the amount of data received.
• If there is sustained clock offset the ES will eventually overflow or
underflow causing timing inaccuracies.
• When R2 is greater than R1, the elastic store at the first digital switch
overflows, causing a loss of data. If R2 is less than R1, the same elastic store
underflows, causing extraneous data to be inserted into the bit stream entering
the switch
Q4   b.   Illustrate the both types of Cable Modem Service architecture in detail.   [10]
CO-5; SO-
1;   Answer- Both type CM diagram – 6 M , Explanation 4 M ,
BL- 2
********** 8 **********
--- page 9 ---
Q5   a.   Explain voice coding techniques comprehensively. classify the following:   [10]
CO-3; SO-1;   •   Properties of speech that enable compression
BL-2,   •   Codec Principles and approaches
Answer – each techniques – 3M , any diagram – 1 M
Speech Codecs
• Waveform codec • Source codec (vocoders) • Hybrid codec
Waveform Codec
• Waveform codecs reconstructed signal whose waveform is as close as
possible to the original without the knowledge of how signal to be coded was
generated. • This means that in theory they should be signal independent and
work well with non-speech signals. • Generally they are low complexity
codec’s which produce high quality speech at rates above about 16 kbits/s. •
When the data rate is lowered below this level the reconstructed speech
quality that can be obtained degradesrapidly. • Pulse code modulation (PCM)
is the simplest way of waveform coding which simply involves sampling and
quantizing the input waveform.
Source Codec (vocoder)
• Source coders operate using a model of how the source was generated, and
attempt to extract parameters, from the signal being coded, the parameters of
********** 9 **********

[Text in pictures on this page, read by OCR]
Cable modem transmission system (CMTS)

l yi | Fiber
From head end—+ Wee Combiner

| A |

Distribution hub
| |
| |

Toand from | Data —ap |
the Internet — | |
--- page 10 ---
the model. • It is these model parameters that are transmitted to the decoder. •
Source coders for speech are called vocoders, and work as follows. • The
vocal tract is represented as a time-varying filter and is excited with either a
white noise source, for unvoiced speech segments, or a train of pulses
separated by the pitch period for voiced speech. • Therefore the information
which must be sent to the decoder is the filter specification, a voiced/unvoiced
flag, the necessary variance of the excitation signal, and the pitch period for
voiced speech.
Hybrid Codec
• Hybrid codecs attempt to fill the gap between waveform and source codecs. •
Waveform coders are capable of providing good quality speech at bit rates
down to about 16 kbits/s, but are of limited use at rates below this. • Source
coders on the other hand can provide intelligible speech at 2.4 kbits/s and
below, but cannot provide natural sounding speech at any bit rate. • Although
other forms of hybrid codecs exist, the most successful and commonly used
are time domain Analysis-by-Synthesis (AbS) codecs.
Q5   b.   (i) Illustrate the operating principle of Discrete Multitone (DMT)   [4]
CO-4; SO-1;   modulation.
BL-2   (ii) Explain two significant advantages of DMT in handling frequency- [2]
selective channel impairments.
(iii) Compare DMT with Carrierless Amplitude Phase (CAP) modulation.   [4]
Answer-
(i) Operating Principle of Discrete Multitone (DMT) Modulation –
4M
Discrete Multitone (DMT) is a multicarrier modulation technique used
in DSL systems to transmit high-speed data over existing copper
telephone lines.
Operating Principle:
1. The available bandwidth of the telephone line is divided into
multiple orthogonal subcarriers (typically 256 or more).
2. Each subcarrier is independently modulated using QAM
(Quadrature Amplitude Modulation).
3. Data bits are distributed among the subcarriers according to
the signal-to-noise ratio (SNR) of each subcarrier (adaptive bit
loading).
4. Subcarriers with high noise carry fewer bits, while clear
subcarriers carry more bits.
5. At the receiver, a Fast Fourier Transform (FFT) separates
subcarriers and recovers the transmitted data.
(ii) Two Significant Advantages of DMT in Handling Frequency-
Selective Channel Impairments – 2M
1. Adaptive Bit Loading:
o DMT measures the SNR of each subcarrier and
allocates bits accordingly.
o Subcarriers affected by attenuation or noise carry fewer
bits or are disabled, while clear subcarriers carry more.
********** 10 **********
--- page 11 ---
o Advantage: Maximizes overall data rate and minimizes
errors despite frequency-dependent impairments.
2. Parallel Transmission over Multiple Subcarriers:
o Data is transmitted simultaneously on many narrowband
subcarriers rather than a single wideband carrier.
o Advantage: Reduces the impact of frequency-selective
fading, as poor subcarriers do not affect the entire signal.
(iii) Comparison of DMT and Carrierless Amplitude Phase (CAP) Modulation
- 2M each
DMT (Discrete   CAP (Carrierless Amplitude
Feature
Multitone)   Phase)
Modulation   Multicarrier QAM over   Single-carrier two-dimensional
Technique   orthogonal subcarriers   amplitude/phase modulation
Divides available
Bandwidth   Uses full available bandwidth
bandwidth into many
Utilization   as one channel
subcarriers
Resilience to High; bad subcarriers can Less; entire channel affected
Noise   be avoided   by noise in one frequency band
Higher; requires FFT/IFFT
Complexity   Lower; simpler implementation
processing
Can achieve higher data
Moderate; limited by single-
Data Rate   rates with adaptive bit
carrier frequency response
loading
Adaptive bit loading per
Fixed modulation; less
Adaptability subcarrier for line
adaptive
conditions
Early ADSL implementations,
Use Case   ADSL, VDSL
legacy DSL systems
Q6   a.   (i) Explain the Erlang B and Erlang C formulas used in telephone traffic   [6]
CO-1; SO-2;   theory. Discuss:
BL-2   •   The mathematical formulation of both formulas
•   When each formula is appropriately used (loss systems vs.
delay systems)
•   The assumptions underlying each formula
Answer-
Each formula and concept – 3 marks
Erlang B specifies the probability of blocking for a system with random
arrivals from an infinite source and arbitrary holding time distributions.
********** 11 **********
--- page 12 ---
Blocking probability : B Offered traffic intensity : A Number of circuits
provided/channles/servers : N
Erlang's Delay Formula or Erlang's C formula
(ii) In a telephone exchange, 400 calls are offered during the busy hour.   [4]
The average call duration is 4 minutes.
a. Calculate the total traffic offered in Erlangs.
b. Determine how many circuits (channels) would be occupied on
average during the busy hour.
c. Comment briefly on what the result implies in terms of network
capacity planning.
Answer-
Number of calls = 400 calls/hour
Average call duration = 4 minutes = 4/60 = 0.0667 hours   - 1M
Traffic offered (A):   Formula and calculation 2M
A=400×0.0667=26.68Erlangs
Interpretation: 1M
• This means that, on average, 26.68 circuits are continuously
occupied during the busy hour.
• The exchange must therefore have more than 27 circuits to
handle this load efficiently without excessive call blocking.
Q6   b.   (i) Explain LoRaWAN working principle.   [3]
CO-5; SO-1;   (ii) Compare LoRaWAN with Narrowband IoT (NB-IoT) technology on   [7]
BL-2   various parameters.
Answer –
Working principle – 3M
LoRaWAN (Long Range Wide Area Network) is a low-power, wide-area
network protocol designed for IoT devices that need long-range
communication with low data rates. It uses a star-of-stars topology, where
battery-powered end devices (sensors/actuators) communicate with gateways
via LoRa modulation. Gateways act as transparent relays, forwarding
messages to a network server, which manages device authentication,
deduplication, and security, and then passes the data to an application server
for processing. LoRaWAN supports uplink and downlink communication,
uses adaptive data rate (ADR) to optimize battery life and network efficiency,
********** 12 **********

[Text in pictures on this page, read by OCR]
So, the probability that a call experiences congestion and therefore it
delayed is given by-

7 NB

~ N—A(1— B)

Where, N= no. of servers, A= ofered load (Er) and B = Blocking
Probability for LCC system.

Prob(delay)= P(> 0)
--- page 13 ---
and provides end-to-end encryption. Its combination of long-range, low power
consumption, and simple infrastructure makes it ideal for IoT applications
such as smart agriculture, smart cities, and asset tracking.
Comparison- 7 M
Basic   LoRaWAN   NB−IoT
Parameter
System   It is supported by LoRa   It supports 3GPP.
Alliance.
License   It is unlicensed by ISM.   It is Licensed by LTE
spectrum.
Security   LoRaWAN is not licensed   NB&miuns;IoT is licensed
which leads to security   which leads to increased
issues.   security.
Spectrum   It is optimized over a   As it is licensed, they are very
long−range using Internet   expensive.
of Things sensors that is
free.
Network type   LoRaWAN is flexible so it   NB−IoT is fixed for the 4G
can choose among the   technology that is LTE (Long
public, private, and hybrid   Term Evolution).
networks.
Data Rate   The Data rate ranges   The data rate is somewhat
between 293bps and   near 20kbps.
50kbps.
Implementation   The deployment cost is   The deployment cost is very
Cost   very low and it can be   high and it can be installed by
installed by anyone.   mobile network operators.
Mobility   It provides a mobility   It is limited to idle mode.
function.
Q7   a.   What is traffic characterization in telephone networks? Explain the concepts   [5]
CO-1; SO-1;   of arrival time distribution and holding time distribution with suitable
BL-1,2   examples.
Answer –
Basic assumption in traffic analysis :   1M
– Arrival from one source is independent of the arrival from other sources.
In those cases where call arrivals tend to be correlate, useful results can be
obtained by modifying a random arrival analysis.
Average call arrival rate from a large group of subscriber lines=λ (arrivals /
second)
********** 13 **********
--- page 14 ---
Arrival Time – 2M
Holding Time – 2M
Q7   b.   Explain the Phase Locked Loop (PLL) technique used for timing recovery in   [5]
CO-2; SO-1;   network synchronization. Draw a block diagram and describe its operation.
BL-2
Explanation – 3M and diagram – 2M
********** 14 **********
--- page 15 ---
PLL Clock Recovery

¢ Phase detector
continuously measures
the phase difference
between I/C Clk and

Local Clk.

* Measures the
difference in zero
crossing between two
clocks.

PLL Clock Recovery

* When zero crossing of line Clk
precedes the zero crossing of local
Clk +ve voltage is generated
otherwise —-ve

+ This voltage is used for adjusting
Voltage Control Oscillator (VCO) to
reduce the phase difference

* Local Clock maintains the desired
average frequency but using PLL
produces short term variations of
phase & frequency to maintain
underlying frequency of the line

clock
Q7 Cc. Compare PSTN and VoIP networks, atleast 8 points to be mentioned. [5]
CO-3; SO-1;
BL-2 Answer — each network — 2.5 M

SS ES
Underlying Technology TDM circuit switching

Network resource reserved . :
Yes No
at call setup
. (Class 4, Class § switching Gateways, gateway
Network ekments ° ve .
systenas controllers, routers

. ae , Mostly integrated in Inseparate gateways and
Call processing intelligence ce .
switching system controllers

Bandwidth per call Variable §- 64+ kh's

MF, DTME, S37 SIP, H.323, MGC PYH.248

Depends on network

Transport TDM in access, edge, core topology (IF, ATM, other)

FRR IC 7 DA HOH
--- page 16 ---
Q7   d.   Explain the functions of Optical Line Termination (OLT) and Optical   [5]
CO-5; SO-1;   Network Terminals (ONT) in Passive Optical Network (PON) architecture
BL-2
Answer – Explanation – 3 M , Diagram – 2M
downstream
upstream
NNI
ptical istributionNetwork   ptical Network nits
core
splitter
ptical ine Terminal   UNI
ptical ccessNetwork   Terminal quipment
********** 16 **********
````
