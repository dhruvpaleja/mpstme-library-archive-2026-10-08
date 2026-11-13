# Cryptography and Network Security: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 3cdb79e2729d

- Departments: Computer Engineering, Computer Science, Computer Science and Business Systems, Data Science
- Programmes: BTech Computer 7002, BTech CS 7055, BTech CSBS 7036, BTech CSE DS 7057, Integrated Computer 7032, MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CSE_DS_7057/Cryptography and Network Security/ANS_Cryptography and Network Security(702AI0E007)_2025-2026.pdf` (+5 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: mixed (13 pages), mean OCR confidence 92.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B.
TECH (CSE- DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Cryptography and Network Security
Date: 01 Dec 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory. Out of remaining, attempt any 4 questions.
5. In all, 5 questions to be attempted. All questions carry equal marks.
6. Assume Suitable data if necessary
Q1
Answer briefly (each sub-question carries 5 marks):   [20]
CO1 ; SO1   a How does DES achieve confusion and diffusion? Give the answer
;   .   with justification.
BL-
moderate   Marks bifurcation:
Confusion: 2.5 Marks (Give the Definition 01 Marks +
Justification of Ans. 1.5 Marks)
Diffusion: 2.5 Marks (Give the Definition 01 Marks +
Justification of Ans. 1.5 Marks)
Synoptic Ans. DES achieves confusion and diffusion as follows:
Confusion: DES introduces confusion by using S-box substitutions
in each Feistel round. The S-boxes replace input bits with output
bits in a non-linear manner, making the relationship between the
ciphertext and the encryption key complex and obscured.
Diffusion: DES achieves diffusion through permutations (P-boxes)
and the Feistel structure, which spread the influence of each input
bit across many output bits over 16 rounds. This ensures that a small
change in the plaintext or key affects many bits of the ciphertext.
CO2 ; SO1 b Find GCD (2740,1760) using Eucledian algorithm.
;   .
BL- Apply   Sol:- (4 mark for detailed steps+ 1 mark for correct final answer)
& Analyze
gcd(a, b) = gcd(b, a  mod  b)
--- page 2 ---
Step 1:
2740 = 1760×1 + 980
⇒ gcd (2740, 1760) = gcd (1760, 980)
Step 2:
1760 = 980×1 + 780
⇒ gcd(1760, 980) = gcd(980, 780)
Step 3:
980=780×1+200
⇒ gcd(980, 780) = gcd(780, 200)
Step 4:
780 = 200×3 + 180
⇒ gcd(780, 200) = gcd(200, 180)
Step 5:
200 = 180 × 1 + 20
⇒ gcd(200, 180) = gcd(180, 20)
Step 6:
180 = 20×9 + 0
Final Answer: gcd(2740, 1760) = 20
CO3 ;   c
SO1,SO2 ;   .   Explain IP Security (IPsec) transport and tunnel modes. How do
BL-   they defer?
Understand
Synoptic Answer (5 marks):
1. Transport mode (1.5 marks):
In IPsec transport mode, only the payload of the IP packet
is encrypted and/or authenticated, leaving the IP header
intact. This mode is typically used for end-to-end
communication between two hosts.
2. Tunnel mode (1.5 marks):
In IPsec tunnel mode, the entire IP packet (both header and
payload) is encrypted and then encapsulated in a new IP
packet with a new header. Tunnel mode is commonly used
for network-to-network communications or VPNs.
3. At least 2 well explained Differences- 2marks
CO4 ; SO4 d Explain the term SIEM and enlist the benefits of the same.
;   .
BL-   SIEM-3 marks
Understand   Benefits- 2 marks
Security information and event management, or SIEM, is a security
solution that helps organizations recognize and address potential
security threats and vulnerabilities before they have a chance to
disrupt business operations.
--- page 3 ---
SIEM combines two functions:
•   Security information management
•   Security event management
This combination provides real-time security monitoring,
allowing teams to track and analyze events and maintain
security data logs for auditing and compliance purposes.
• SIEM makes behavioral anomalies visible to security
teams, enhancing the monitoring process with AI to
automate incident detection and response processes.
It has replaced many manual tasks, becoming a ubiquitous
tool for any security operation center (SOC).
Q2   a Discuss the various principles involved in private and public key [10]
CO1; SO1;   .   cryptography. Suppose two users want to exchange confidential
BL-low   data, discuss how key distribution process vary in each technique
along with its advantages and disadvantages.
Principles of Private key cryptography [2 marks]
Principles of Public key cryptography [2 marks]
Public-key cryptography is based on mathematical functions,
unlike the symmetric ciphers that are based on operations on bit
patterns. • Public-key cryptography is asymmetric, involving the
use of two separate keys. • Each user has two keys: Public key of a
user is known to others; private key of the user is known only to the
user. • Either of the two keys can be used for encryption/
decryption. However, a message encrypted with one key can be
decrypted only with the other key. • Examples: RSA
Key distribution in private and public types [4 marks]
--- page 4 ---
Advantages/Disadvantages [2 marks]
Q2   b What is Expansion Permutation? Describe any three roles of the [10
CO2; SO1;   .   expansion permutation in the DES round function and illustrate its   ]
BL-   working with neat diagram.
Moderate
Marks bifurcation:
What is it? :03 Marks
Three roles of the expansion permutation in the DES: 03 Marks
Working with Diagram: 04 Marks
Synoptic Ans.
What is Expansion Permutation:
Expansion Permutation DES is a process that expands 32-bit input
to 48 bits, repeating and rearranging bits for diffusion.
Role of Expansion Permutation in DES Round Function
•   Bit Expansion for Key Mixing: Expands 32 bits to 48 bits
so it can be XORed with the 48-bit round key. This
ensures proper integration of the key into the round
function.
•   Facilitates Diffusion Across S-boxes: By rearranging and
expanding bits, bits from different positions influence
multiple S-box inputs. This promotes diffusion, spreading
the effect of each input bit across the output.
• Aligns Data Size with the Round Key: Expansion increases
the 32-bit half-block to match the 48-bit round key,
enabling proper XOR operation during the round function.
This ensures consistent processing in all 16 DES rounds.
Diagram:
Q3   a Summarize the steps in DES algorithm. Compute the output using [10
CO1; SO1;   .   following S-box 1 for input value 111010. Write the steps   ]
BL-High   followed for the same.
S1 0   1   2   3   4   5   6   7   8   9 10 11 12 13
0 14   4 13   1   2 15 11   8   3 10   6 12   5   9

[Text in pictures on this page, read by OCR]
1

Block 1
23 4

Block 8
29 30 31 32

1

2

3 4 5 6

7 8 9 10 11 12
--- page 5 ---
1   0 15   7   4 14   2 13   1 10   6 12 11   9   5   3   8
2   4   1 14   8 13   6   2 11 15 12   9   7   3 10   5   0
3 15 12   8   2   4   9   1   7   5 11   3 14 10   0   6 13
DES steps in detail -7 m
Output-1m (1010)
Steps for finding output-2m
Q3   b Explain all the steps of RSA algorithm. Jai and Veeru agreed to use [10
CO2; SO4;   . RSA algorithm for the secret communication. Jai securely choose   ]
BL-high   two prime numbers, p=5 and q=7 and a secret key d=23. Jai uses
this public key and sends a ciphertext C=12 to Veeru. Find the
original plaintext.
RSA steps-5 marks
Numnerical -5 marks
Step 1 — Compute n and φ(n) (2 marks)
n = p × q = 5x7 =35
φ(n) = (p−1) (q−1) = 4x6 = 24
Step 2 — Decrypt ciphertext C=12 to get plaintext M (3 marks)
We must compute
M ≡ Cd  mod  n = 1223 mod  35.
M = 3.
Q4   a Explain encryption and decryption process in AES with neat [10
CO1; SO1;   .   diagram. Determine the output after ShiftRow transformation for   ]
BL-high   the state given below:
A1 B2 C3 D4
E5 F6 07 18
19 2A 3B 4C
5D 6E 7F 80
Ans.
Marks bifurcation:
Encryption & decryption process in AES: 08 marks (diagram 3
marks+ explanation 5 marks)
Solving for Output after shiftrow transformation: 02marks
Encryption and decryption process in AES:
Diagram
--- page 6 ---
The encryption process in AES starts from the round function. Each
round comprises of four sub-processes.
a. SubBytes: The 16 input bytes are substituted by looking up a
fixed table (S-box) given in design. The result is in a matrix of four
rows and four columns.
b. Shiftrows: Each of the four rows of the matrix is shifted to the
left.
c. MixColumns: Each column of four bytes is now transformed
using a special mathematical function. This function takes as input
the four bytes of one column and outputs four completely new
bytes, which replace the original column. The result is another new
matrix consisting of 16 new bytes.
d. Addroundkey: The 16 bytes of the matrix are now considered as
128 bits and are XORed to the 128 bits of the round key. If this is
the last round, then the output is the ciphertext. Otherwise, the
resulting 128 bits are interpreted as 16 bytes and we begin another
similar round.
Decryption –above steps in reverse order
Solving for Output after shiftrow transformation: After Shift row
transformation
A1 B2 C3 D4
F6 07 18 E5
3B 4C 19 2A
80 5D 6E 7F
Q4   b Describe different types of keys involved in Diffie-Hellman   [10
CO2; SO1;   .   algorithm. Alice and Bob agree on a prime number q=11 and a   ]

[Text in pictures on this page, read by OCR]
Key F
¥

w10, 31 Add round key

jaintet

Xpand key ]

Inverse mix ce

:
rq

Add round key W136, 39]

[suns J

Add round key wI40, 43] Add round key

Ciphertext Ciphertext

Deerypti
--- page 7 ---
BL-high   primitive root g=2. If Alice's private key is a=3 and Bob's private
key is b=5, what is the shared secret key they exchange?
Types of Keys- 5 marks
Numerical solution-5 marks
The Diffie-Hellman algorithm involves different types of keys
working together to securely establish a shared secret key between
two parties over an insecure channel. Here are the key types
involved:
1. Public Parameters (Public Keys):
2. Private Keys:
3. Public Keys (Generated from Private Keys):
• Using their private keys, parties compute their
public keys:
A=gamod  pA=gamodp (Alice’s public key)
B=gbmod  pB=gbmodp (Bob’s public key)
• These public keys are exchanged openly.
4. Shared Secret Key:
This shared secret key can then be used for symmetric encryption
to secure communications.

[Text in pictures on this page, read by OCR]
Step 1: Calculate Alice's public key A = g* mod q
A=2' mod11=8 mod11=8

Step 2: Calculate Bob's public key B = g° mod q
Calculate 2° mod 11:

21=2
?=4
23 =8

24=16=5 modll
2° =5x2=10 mod 11
So,

B=10
--- page 8 ---
Q5   a Describe different types of active attacks with the help of suitable [10
CO1; SO1;   .   examples. Compare Active attacks with Passive attacks.   ]
BL-low
Active attacks ( 1 mark)- are a type of cybersecurity attack in which
an attacker attempts to alter, destroy, or disrupt the normal
operation of a system or network.
▪ Types of active attacks: (any four -4 marks)
▪ Masquerade
▪ Modification of messages
▪ Repudiation
▪ Replay
▪ Denial of Service
Comparison (any 5 differences: 5 marks)
Active Attacks   Passive Attacks
Attempts to alter, disrupt, or damage Attempts to monitor or gathe
systems/data   information silently
Intrusive and disruptive   Stealthy and non-intrusive
Modify, delete, or corrupt data; gain   Collect sensitive data withou
control   detection
Often noticeable due to system   Hard to detect; no changes m
changes or failures   system
Data modification, DoS attacks,   Eavesdropping, traffic analy
spoofing   keylogging
Firewalls, intrusion   Encryption, secure protocols
detection/prevention systems   obfuscation

[Text in pictures on this page, read by OCR]
Step 3: Calculate shared secret key S
* Alice computes S = B? mod q=10* mod 11

Calculate:
107 =100=1 mod 11
10° = 10? x 10=1x10=10 mod 11
* Bob computes S = A’ mod q=8° mod 11
Calculate powers of 8 modulo 11:
g'=8
8?=64=9 mod 11
88 =9x8=72=6 mod 11
8'=6x8=48=4 mod 11
8° =4x8=32=10 mod 11

Both get S = 10.
--- page 9 ---
Immediate and potentially severe   Long-term risk due to data leakage
Q5   b Explain the properties that make a hash function suitable for   [10
CO2; SO4;   .   cryptographic applications and describe at least two practical   ]
BL-low   scenarios where hash functions are vital. Discuss features of
Message Digest and Secure Hash Function families.
Hash function propersties-4 marks
Applications-2m
features of MD-2m
features of SHA-2m
Q6   a Discuss working of PGP encryption. Explain Message generation   [10
CO3; SO1;   .   and reception process in PGP in detail.   ]
BL-
moderate   working -3 m
•Step1:PGPgeneratesahuge,one-time-use public encryption
algorithm that can not be guessed, which becomes the random
session key.
•Step2:The session key is then encrypted using the recipient’s
public key, which protects the message while being transmitted.
The recipient shares that key with anyone they want to receive
messages from.
•Step3:The message sender submits their sessionkey, then the
recipient can decrypt the message using their privatekey.
Generation -3.5 m
•Key Pair Generation:
•The sender generates a key pair consisting of a public key and a
private key.
•Key Distribution:
•The sender shares their public key with the intended recipient.
•Digital Signature:
•The sender signs the message with their private key to create a
digital signature, ensuring authenticity
•Message Encryption:
•The sender encrypts the message using the recipient's public key
to ensure confidentiality.
•Transmission:
•The encrypted message and digital signature are transmitted to
the recipient.
Message reception-3.5m
•Key Pair Import:
•The recipient imports the sender's public key and uses their
private key.
•Digital Signature Verification:
•The recipient verifies the digital signature using the sender's
public key to confirm the message's authenticity.
•Message Decryption:
--- page 10 ---
•The recipient decrypts the message using their private key to
reveal the original content.
•Message Authentication:
•The recipient, having verified the signature and decrypted the
message, ensures that the content is unchanged.
•Message Display:
•The decrypted and verified message is displayed to the recipient.
Q6   b CityGrid Utilities manages power grids and water systems through [10
CO4; SO4;   .   connected SCADA networks. These systems are increasingly   ]
BL-   targeted by nation-state actors and malware designed for industrial
Analyze   control systems. They must implement deep packet inspection,
anomaly detection, and segmented network zones to reduce risks.
Which combination of   firewalls, IDS/IPS, and network
segmentation strategies would best protect CityGrid’s operational
technology (OT) and prevent lateral movement by attackers?
Solution- [List benefits of network segmentation, Firewalls or IDS
6M + Provide combinations 4M]
For CityGrid Utilities, the key goal is to protect operational
technology (OT) such as SCADA networks from sophisticated
attacks, including malware and nation-state threats, while
preventing   lateral movement and maintaining operational
continuity. Here’s a structured approach combining firewalls,
IDS/IPS, and segmentation strategies:
• Network Segmentation - Segmentation is critical in OT
environments to isolate critical systems from IT networks
and limit lateral movement. Use industrial firewalls at each
boundary. Implement VLANs or physical separation to
isolate OT segments. Restrict traffic to explicitly allowed
protocols and ports only (whitelisting).
•   Firewalls - Firewalls act as the first line of defense,
controlling inbound/outbound   traffic. Industrial-Grade
Firewalls can be Deployed .
o Default deny-all policy, allow only necessary
SCADA traffic.
o Use   stateful   inspection   to   track   legitimate
connections.
o Place firewalls between DMZ and Control Zone for
safe remote access
• IDS/IPS (Intrusion Detection/Prevention) - Detect and
block suspicious activities without disrupting operations:
o Deploy passive IDS sensors in critical OT segments
for monitoring.
o OT networks have predictable traffic patterns;
anomaly   detection   can   spot   malware   or
unauthorized commands.
o Use tools that understand industrial protocols.
• Deep Packet Inspection (DPI)
•   Inspect industrial protocol traffic at the application layer.
--- page 11 ---
•   Identify malicious commands, unauthorized access, or
unusual patterns.
• Combine with IDS/IPS for automated threat prevention.
Suggested Combination < any two combinations 5M>
Layer   Tool/Strategy   Purpose
OT   Control access to SCADA/PLC
Industrial Firewall
Perimeter   networks
OT   Internal Firewalls / Prevent   lateral   movement
Segments VLANs   between zones
OT   Detect anomalies and block
IDS/IPS with DPI
Network   malicious traffic
IT-OT   DMZ + Firewall + Secure remote access & limit
Boundary IDS   IT-OT traffic
SIEM + Anomaly Correlate alerts, detect early
Monitoring
Detection   threats
Q7   a Explain the importance and working of SSL/TLS protocols with   [10
CO3; SO4;   .   emphasis on the handshake process. Compare TLS connection   ]
BL-   with TLS session.
moderate
Importance of SSL in security (2 marks):
SSL provides data confidentiality, integrity, and authentication,
making it essential for securing online transactions, emails, and
other sensitive data over the internet.
SSL/TLS are cryptographic protocols that provide secure
communication over a computer network by using encryption,
authentication, and integrity mechanisms.
1. Handshake process (4 marks):
○ Step 1: ClientHello:
The client initiates the handshake by sending a
message that includes SSL version, cipher settings,
session ID, and a randomly generated number.
○ Step 2: ServerHello:
The server responds with its own SSL version,
cipher settings, session ID, and its random number,
along with its digital certificate.
○ Step 3: Server authentication and pre-master secret:
The server's certificate is verified by the client. The
client then generates a pre-master secret, encrypts
it using the server’s public key, and sends it to the
server.
--- page 12 ---
○ Step 4: Session keys generated:
Both the client and server generate session keys
using the pre-master secret and the random
numbers.
2. Data transmission with encryption:
Once the session keys are exchanged, the client and server
use symmetric encryption to securely transmit data. The
integrity of the message is maintained using MAC
(Message Authentication Code).
3. Session resumption
SSL/TLS allows session resumption where previously
negotiated session parameters can be reused to avoid the
overhead of a full handshake.
Comparison: 4m (any 4 points)
Q7   b Discuss Packet-filtering firewalls. Compare them with Stateful [10
CO4; SO1;   .   Inspection firewalls and Application proxies.   ]
BL-
moderate   Packet-filtering firewalls-4m
Comparison with Stateful Inspection firewalls- at least 3
differences-3Marks
Comparison with Application proxies.- - at least 3 differences-
3Marks

[Text in pictures on this page, read by OCR]
TLS Connection & TLS Session

TLS connection TLS session

Itis a transport that provides a suitable type of Itis an association between a client and a serve
service

Created by the Handshake Protocol
For TLS, such connections are peer-to-peer

relationships
is Define a set of cryptographic security parametd

which can be shared among multiple connectio}
Connections are transient i.e. temporary

Used to avoid the expensive negotiation of ne
Every connection is associated with one session security parameters for each connection
--- page 13 ---
Packet Filtering Stateful Inspection | Application Proxy | Guard Personal Firew|

Simplest More complex Even more complex | Most complex Similar to packe
filtering firewall
Sees only addresses | Can see either Sees full data Sees full text of Can see full dat:
and service protocol | addresses or data portion of packet communication portion of packe|
type
Auditing difficult Auditing possible Can audit activity Can audit activity Canand usually
doesaudit activi
Screens based on Screens based on Screens based on Screens based on Typically, scree
connection rules information across | behavior of proxies | interpretation of based on
packetsin either message content information in |
header or data field single packet, u:
header or data
Complex addressing | Usually Simple proxies can | Complex guard Usually starts in|
rules can make preconfigured to substitute for functionality can "deny all inbouy

configuration tricky | detect certain attack | complex addressing | limit assurance mode, to which
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper e7f861854abb

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSBS_7036/Cryptography and Network Security/ANS_Cryptography and Network Security(702AI0E007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. TECH (CSE
- DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Cryptography and Network Security
Date: 01 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory. Out of remaining, attempt any 4 questions.
5. In all, 5 questions to be attempted. All questions carry equal marks.
6. Assume Suitable data if necessary
Q1
Answer briefly (each sub-question carries 5 marks):   [20]
CO1 ; SO1 ;   a. How does DES achieve confusion and diffusion? Give the answer with
BL-   justification.
moderate
Marks bifurcation:
Confusion: 2.5 Marks (Give the Proper Ans. 01 Marks + Justification of
Ans. 1.5 Marks)
Diffusion: 2.5 Marks (Give the Proper Ans. 01 Marks + Justification of
Ans. 1.5 Marks)
Synoptic Ans. DES achieves confusion and diffusion as follows:
Confusion: DES introduces confusion by using S-box substitutions in each
Feistel round. The S-boxes replace input bits with output bits in a non-linear
manner, making the relationship between the ciphertext and the encryption
key complex and obscured.
Diffusion: DES achieves diffusion through permutations (P-boxes) and the
Feistel structure, which spread the influence of each input bit across many
output bits over 16 rounds. This ensures that a small change in the plaintext
or key affects many bits of the ciphertext.
CO2 ; SO1 ;   b. Find GCD (2740,1760) using Eucledian algorithm.
BL- Apply   Sol:- We apply the Euclidean algorithm: (5 Marks: 1 mark for each step)
& Analyze   gcd(a, b) = gcd(b, a  mod  b)
Step 1:
2740 = 1760×1 + 980
⇒ gcd (2740, 1760) = gcd (1760, 980)
Step 2:
1760 = 980×1 + 780
⇒ gcd(1760, 980) = gcd(980, 780)
Step 3:
980=780×1+200
⇒ gcd(980, 780) = gcd(780, 200)
********** 1 **********
--- page 2 ---
Step 4:
780 = 200×3 + 180
⇒ gcd(780, 200) = gcd(200, 180)
Step 5:
200 = 180 × 1 + 20
⇒ gcd(200, 180) = gcd(180, 20)
Step 6:
180 = 20×9 + 0
Final Answer: gcd(2740, 1760) = 20
CO3 ;   c.
SO1,SO2 ;   Explain IP Security (IPsec) transport and tunnel modes. How do they defer?
BL-
Understand   Synoptic Answer (5 marks):
1. Transport mode (1.5 marks):
In IPsec transport mode, only the payload of the IP packet is
encrypted and/or authenticated, leaving the IP header intact. This
mode is typically used for end-to-end communication between two
hosts.
2. Tunnel mode (1.5 marks):
In IPsec tunnel mode, the entire IP packet (both header and
payload) is encrypted and then encapsulated in a new IP packet
with a new header. Tunnel mode is commonly used for network-to-
network communications or VPNs.
3. Differnces- 2marks
CO4 ; SO4 ;   d. Explain the term SIEM and enlist the benefits of the same.
BL-
Understand   Security information and event management, or SIEM, is a security solution
that helps organizations recognize and address potential security threats and
vulnerabilities before they have a chance to disrupt business operations.
SIEM combines two functions:
• Security information management
• Security event management
This combination provides real-time security monitoring, allowing
teams to track and analyze events and maintain security data logs
for auditing and compliance purposes.
• SIEM makes behavioral anomalies visible to security teams,
enhancing the monitoring process with AI to automate incident
detection and response processes.
It has replaced many manual tasks, becoming a ubiquitous tool for
any security operation center (SOC).
Q2   a. Discuss the various principles involved in private and public key [10]
CO1; SO1;   cryptography. Suppose two users want to exchange confidential data,
BL-low   discuss how key distribution process vary in each technique along with its
advantages and disadvantages.
Private key cryptography [3 marks]
********** 2 **********
--- page 3 ---
Public key cryptography [3 marks]
Public-key cryptography is based on mathematical functions, unlike the
symmetric ciphers that are based on operations on bit patterns. • Public-key
cryptography is asymmetric, involving the use of two separate keys. • Each
user has two keys: Public key of a user is known to others; private key of
the user is known only to the user. • Either of the two keys can be used for
encryption/ decryption. However, a message encrypted with one key can be
decrypted only with the other key. • Examples: RSA
Key distribution [4 marks]
Q2   b. What is Expansion Permutation? Describe any three roles of the expansion [10]
CO2; SO1;   permutation in the DES round function and illustrate its working with neat
BL-   diagram.
Moderate
Marks bifurcation:
What is it? :03 Marks
Three roles of the expansion permutation in the DES: 03 Marks
Diagram: 04 Marks
Synoptic Ans.
What is Expansion Permutation:
Expansion Permutation DES is a process that expands 32-bit input to 48
bits, repeating and rearranging bits for diffusion.
Role of Expansion Permutation in DES Round Function
• Bit Expansion for Key Mixing: Expands 32 bits to 48 bits so it can
be XORed with the 48-bit round key. This ensures proper integration
of the key into the round function.
•   Facilitates Diffusion Across S-boxes: By rearranging and expanding
bits, bits from different positions influence multiple S-box inputs.
This promotes diffusion, spreading the effect of each input bit across
the output.
• Aligns Data Size with the Round Key: Expansion increases the 32-
bit half-block to match the 48-bit round key, enabling proper XOR
********** 3 **********

[Text in pictures on this page, read by OCR]
Bob

To public —

Key-generation
Alice I Public-key distribution procedure

a H channel
1

Public key ¢ f Private key
a |} hee} [

Plaintext Ciphertext Insecure channel Ciphertext Plaintext
--- page 4 ---
operation during the round function. This ensures consistent
processing in all 16 DES rounds.
Diagram:
Q3   a. Summarize the steps in DES algorithm. Compute the output using [10]
CO1; SO1;   following S-box 1 for input value 111010. Write the steps followed
BL-High   for the same.
S1   0   1   2   3   4   5   6   7   8   9   10 11 12 13 14 15
0   14   4 13   1   2 15 11   8   3 10   6 12   5   9   0   7
1   0 15   7   4 14   2 13   1 10   6 12 11   9   5   3   8
2   4   1 14   8 13   6   2 11 15 12   9   7   3 10   5   0
3   15 12   8   2   4   9   1   7   5 11   3 14 10   0   6 13
DES steps-7 m
Output-1m
Steps for finding output-2m
Q3   b. Explain all the steps of RSA algorithm. Jai and Veeru agreed to use RSA [10]
CO2; SO4;   algorithm for the secret communication. Jai securely choose two prime
BL-high   numbers, p=5 and q=7 and a secret key d=23. Jai uses this public key and
sends a ciphertext C=12 to Veeru. Find the original plaintext.
RSA steps-5 marks
Step 1 — Compute n and φ(n) (2 marks)
n = p × q = 5x7 =35
φ(n) = (p−1) (q−1) = 4x6 = 24
Step 2 — Decrypt ciphertext C=12 to get plaintext M (3 marks)
We must compute
M ≡ Cd  mod  n = 1223 mod  35.
M = 3.
Q4   a. Explain encryption and decryption process in AES with neat diagram. [10]
CO1; SO1;   Determine the output after ShiftRow transformation for the state given
BL-high   below:
A1 B2 C3 D4
E5 F6 07 18
19 2A 3B 4C
5D 6E 7F 80
Ans.
Marks bifurcation:
********** 4 **********

[Text in pictures on this page, read by OCR]
Block 1 Block 2 Block 8
123 4 § 676 29 30 31 32

1238 45 6 7 8 9 10 11 12 43 44 45 46 47 48
--- page 5 ---
Encryption & decryption process in AES: 08 marks (diagram 3 marks+
explanation 5 marks)
Solving for Output after shiftrow transformation: 02marks
Encryption and decryption process in AES:
Diagram
The encryption process in AES starts from the round function. Each round
comprises of four sub-processes.
a. SubBytes: The 16 input bytes are substituted by looking up a fixed table
(S-box) given in design. The result is in a matrix of four rows and four
columns.
b. Shiftrows: Each of the four rows of the matrix is shifted to the left.
c. MixColumns: Each column of four bytes is now transformed using a
special mathematical function. This function takes as input the four bytes
of one column and outputs four completely new bytes, which replace the
original column. The result is another new matrix consisting of 16 new
bytes.
d. Addroundkey: The 16 bytes of the matrix are now considered as 128 bits
and are XORed to the 128 bits of the round key. If this is the last round,
then the output is the ciphertext. Otherwise, the resulting 128 bits are
interpreted as 16 bytes and we begin another similar round.
Decryption –above steps in reverse order
Solving for Output after shiftrow transformation: After Shift row
transformation
A1 B2 C3 D4
F6 07 18 E5
3B 4C 19 2A
80 5D 6E 7F
********** 5 **********

[Text in pictures on this page, read by OCR]
Key

+

w0, 3] Add round key

atext

Expand key] [Limverse sup bytes]

Inverse shift rows

yt

wI36, 39]

a:

wi40, 43]

Ciphertext

(a) ption
--- page 6 ---
Q4   b. Describe different types of keys involved in Diffie-Hellman algorithm.   [10]
CO2; SO1;   Alice and Bob agree on a prime number q=11 and a primitive root g=2. If
BL-high   Alice's private key is a=3 and Bob's private key is b=5, what is the shared
secret key they exchange?
Types of Keys- 5 marks
Numerical solution-5 marks
The Diffie-Hellman algorithm involves different types of keys working
together to securely establish a shared secret key between two parties over
an insecure channel. Here are the key types involved:
1. Public Parameters (Public Keys):
2. Private Keys:
3. Public Keys (Generated from Private Keys):
• Using their private keys, parties compute their public keys:
A=gamod  pA=gamodp (Alice’s public key)
B=gbmod  pB=gbmodp (Bob’s public key)
• These public keys are exchanged openly.
4. Shared Secret Key:
This shared secret key can then be used for symmetric encryption to
secure communications.
********** 6 **********

[Text in pictures on this page, read by OCR]
Step 1: Calculate Alice's public key A = g* mod q
A=2> mod11=8 mod 11=8

Step 2: Calculate Bob's public key B = g° mod q
Calculate 2° mod 11:

21=2
?=4
23 =8

24=16=5 modll
2 =5x2=10 modil
So,

B=10
--- page 7 ---
Q5   a. Describe different types of active attacks with the help of suitable [10]
CO1; SO1;   examples. Compare Active attacks with Passive attacks.
BL-low
Active attacks ( 1 mark)- are a type of cybersecurity attack in which an
attacker attempts to alter, destroy, or disrupt the normal operation of a
system or network.
▪ Types of active attacks: (any four -4 marks)
▪ Masquerade
▪ Modification of messages
▪ Repudiation
▪ Replay
▪ Denial of Service
Comparison (any 5: 5 marks)
Active Attacks   Passive Attacks
Attempts to alter, disrupt, or   Attempts to monitor or gather
damage systems/data   information silently
Intrusive and disruptive   Stealthy and non-intrusive
Modify, delete, or corrupt data; gain Collect sensitive data without
control   detection
Often noticeable due to system   Hard to detect; no changes made
changes or failures   to system
Data modification, DoS attacks,   Eavesdropping, traffic analysis,
spoofing   keylogging
Firewalls, intrusion   Encryption, secure protocols,
detection/prevention systems   traffic obfuscation
Long-term risk due to data
Immediate and potentially severe
leakage
********** 7 **********

[Text in pictures on this page, read by OCR]
Step 3: Calculate shared secret key S
* Alice computes S = B? mod q= 10° mod 11

Calculate:
107=100=1 mod 11
10° =10? x 10=1x10=10 mod11
* Bob computes S = A’ mod q=8° mod 11
Calculate powers of 8 modulo 11:
g'=8
8?=64=9 mod 11
88 =9x8=72=6 mod 11
8'=6x8=48=4 mod 1l
8° =4x8=32=10 mod 11

Both get S = 10.
--- page 8 ---
Q5   b. Explain the properties that make a hash function suitable for cryptographic   [10]
CO2; SO4;   applications and describe at least two practical scenarios where hash
BL-low   functions are vital. Discuss features of Message Digest and Secure Hash
Function families.
Hash function propersties-4 marks
Applications-2m
features of MD-2m
features of SHA-2m
Q6   a. Discuss working of PGP encryption. Explain Message generation and   [10]
CO3; SO1;   reception process in PGP in detail.
BL-
moderate   working -3 m
•Step1:PGPgeneratesahuge,one-time-use public encryption algorithm that
can not be guessed, which becomes the random session key.
•Step2:The session key is then encrypted using the recipient’s public key,
which protects the message while being transmitted. The recipient shares
that key with anyone they want to receive messages from.
•Step3:The message sender submits their sessionkey, then the recipient
can decrypt the message using their privatekey.
Generation -3.5 m
•Key Pair Generation:
•The sender generates a key pair consisting of a public key and a private
key.
•Key Distribution:
•The sender shares their public key with the intended recipient.
•Digital Signature:
•The sender signs the message with their private key to create a digital
signature, ensuring authenticity
•Message Encryption:
•The sender encrypts the message using the recipient's public key to
ensure confidentiality.
•Transmission:
•The encrypted message and digital signature are transmitted to the
recipient.
Message reception-3.5m
•Key Pair Import:
•The recipient imports the sender's public key and uses their private key.
•Digital Signature Verification:
•The recipient verifies the digital signature using the sender's public key
to confirm the message's authenticity.
•Message Decryption:
•The recipient decrypts the message using their private key to reveal the
original content.
•Message Authentication:
•The recipient, having verified the signature and decrypted the message,
ensures that the content is unchanged.
•Message Display:
•The decrypted and verified message is displayed to the recipient.
********** 8 **********
--- page 9 ---
Q6   b. CityGrid Utilities manages power grids and water systems through [10]
CO4; SO4;   connected SCADA networks. These systems are increasingly targeted by
BL-Analyze   nation-state actors and malware designed for industrial control systems.
They must implement deep packet inspection, anomaly detection, and
segmented network zones to reduce risks. Which combination of firewalls,
IDS/IPS, and network segmentation strategies would best protect
CityGrid’s operational technology (OT) and prevent lateral movement by
attackers?
Solution- [List benefits of network segmentation, Firewalls or IDS 6M +
Provide combinations 4M]
For CityGrid Utilities, the key goal is to protect operational technology
(OT) such as SCADA networks from sophisticated attacks, including
malware and nation-state threats, while preventing lateral movement and
maintaining operational continuity. Here’s a structured approach
combining firewalls, IDS/IPS, and segmentation strategies:
• Network Segmentation   - Segmentation   is   critical   in OT
environments to isolate critical systems from IT networks and limit
lateral movement. Use industrial firewalls at each boundary.
Implement VLANs or physical separation to isolate OT segments.
Restrict traffic to explicitly allowed protocols and ports only
(whitelisting).
•   Firewalls - Firewalls act as the first line of defense, controlling
inbound/outbound   traffic. Industrial-Grade Firewalls can be
Deployed .
o Default deny-all policy, allow only necessary SCADA
traffic.
o Use stateful inspection to track legitimate connections.
o Place firewalls between DMZ and Control Zone for safe
remote access
• IDS/IPS (Intrusion Detection/Prevention) - Detect and block
suspicious activities without disrupting operations:
o Deploy passive IDS sensors in critical OT segments for
monitoring.
o OT networks have predictable traffic patterns; anomaly
detection can spot malware or unauthorized commands.
o Use tools that understand industrial protocols.
• Deep Packet Inspection (DPI)
•   Inspect industrial protocol traffic at the application layer.
•   Identify malicious commands, unauthorized access, or unusual
patterns.
• Combine with IDS/IPS for automated threat prevention.
Suggested Combination < any two combinations 5M>
********** 9 **********
--- page 10 ---
Layer   Tool/Strategy   Purpose
OT   Control access to SCADA/PLC
Industrial Firewall
Perimeter   networks
OT   Internal Firewalls   / Prevent lateral movement between
Segments   VLANs   zones
Detect   anomalies   and   block
OT Network IDS/IPS with DPI
malicious traffic
IT-OT   DMZ + Firewall + Secure remote access & limit IT-
Boundary   IDS   OT traffic
SIEM + Anomaly
Monitoring   Correlate alerts, detect early threats
Detection
Q7   a. Explain the importance and working of SSL/TLS protocols with emphasis   [10]
CO3; SO4;   on the handshake process. Compare TLS connection with TLS session.
BL-
moderate   Importance of SSL in security (2 marks):
SSL provides data confidentiality, integrity, and authentication, making it
essential for securing online transactions, emails, and other sensitive data
over the internet.
SSL/TLS are cryptographic protocols that provide secure communication
over a computer network by using encryption, authentication, and
integrity mechanisms.
1. Handshake process (4 marks):
○ Step 1: ClientHello (1 mark):
The client initiates the handshake by sending a message that
includes SSL version, cipher settings, session ID, and a
randomly generated number.
○ Step 2: ServerHello (1 mark):
The server responds with its own SSL version, cipher
settings, session ID, and its random number, along with its
digital certificate.
○ Step 3: Server authentication and pre-master secret:
The server's certificate is verified by the client. The client
then generates a pre-master secret, encrypts it using the
server’s public key, and sends it to the server.
○ Step 4: Session keys generated:
Both the client and server generate session keys using the
pre-master secret and the random numbers.
2. Data transmission with encryption:
Once the session keys are exchanged, the client and server use
symmetric encryption to securely transmit data. The integrity of
the message is maintained using MAC (Message Authentication
Code).
3. Session resumption
SSL/TLS allows session resumption where previously negotiated
session parameters can be reused to avoid the overhead of a full
handshake.
Comparison: 4m (any 4 points)
********** 10 **********
--- page 11 ---
Q7   b. Discuss Packet-filtering firewalls. Compare them with Stateful Inspection [10]
CO4; SO1;   firewalls and Application proxies.
BL-
moderate   Packet-filtering firewalls-4m
Comparison-6m
********** 11 **********

[Text in pictures on this page, read by OCR]
TLS Connection & TLS Session

TLS connection TLS session

Itis a transport that provides a suitable type of It is an association between a client and a server
service

Created by the Handshake Protocol
For TLS, such connections are peer-to-peer

relationships
is Define a set of cryptographic security parameters

which can be shared among multiple connections
Connections are transient i.e. temporary

Used to avoid the expensive negotiation of new
Every connection is associated with one session security parameters for each connection

Packet Filtering Stateful Inspection | Application Proxy | Guard Personal Firewall

Simplest More complex Even more complex | Most complex Similar to packet
filtering firewall
Sees only addresses | Can see either Sees full data Sees full text of Can see full data
and service protocol | addresses or data portion of packet communication portion of packet
type
Auditing difficult Auditing possible Can audit activity Can audit activity Canand usually
doesaudit activity
Screens based on Screens based on Screens based on Screens based on Typically, screens
connection rules information across | behavior of proxies | interpretation of based on
packetsin either message content information in a
header or data field single packet, using
header or data
Complex addressing | Usually Simple proxies can | Complex guard Usually starts in
rules can make preconfigured to substitute for functionality can "deny all inbound"

configuration tricky | detect certain attack | complex addressing | limit assurance mode, to which user
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper f37be6ef82fc

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSE_DS_7011/Cryptography and Network Security/ANS_Cryptography and Network Security(702AI0E007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. TECH (CSE
- DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Cryptography and Network Security
Date: 01 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory. Out of remaining, attempt any 4 questions.
5. In all, 5 questions to be attempted. All questions carry equal marks.
6. Assume Suitable data if necessary
Q1
Answer briefly (each sub-question carries 5 marks):   [20]
CO1 ; SO1 ;   a. How does DES achieve confusion and diffusion? Give the answer with
BL-   justification.
moderate
Marks bifurcation:
Confusion: 2.5 Marks (Give the Proper Ans. 01 Marks + Justification of
Ans. 1.5 Marks)
Diffusion: 2.5 Marks (Give the Proper Ans. 01 Marks + Justification of
Ans. 1.5 Marks)
Synoptic Ans. DES achieves confusion and diffusion as follows:
Confusion: DES introduces confusion by using S-box substitutions in each
Feistel round. The S-boxes replace input bits with output bits in a non-linear
manner, making the relationship between the ciphertext and the encryption
key complex and obscured.
Diffusion: DES achieves diffusion through permutations (P-boxes) and the
Feistel structure, which spread the influence of each input bit across many
output bits over 16 rounds. This ensures that a small change in the plaintext
or key affects many bits of the ciphertext.
CO2 ; SO1 ;   b. Find GCD (2740,1760) using Eucledian algorithm.
BL- Apply   Sol:- We apply the Euclidean algorithm: (5 Marks: 1 mark for each step)
& Analyze   gcd(a, b) = gcd(b, a  mod  b)
Step 1:
2740 = 1760×1 + 980
⇒ gcd (2740, 1760) = gcd (1760, 980)
Step 2:
1760 = 980×1 + 780
⇒ gcd(1760, 980) = gcd(980, 780)
Step 3:
980=780×1+200
⇒ gcd(980, 780) = gcd(780, 200)
********** 1 **********
--- page 2 ---
Step 4:
780 = 200×3 + 180
⇒ gcd(780, 200) = gcd(200, 180)
Step 5:
200 = 180 × 1 + 20
⇒ gcd(200, 180) = gcd(180, 20)
Step 6:
180 = 20×9 + 0
Final Answer: gcd(2740, 1760) = 20
CO3 ;   c.
SO1,SO2 ;   Explain IP Security (IPsec) transport and tunnel modes. How do they defer?
BL-
Understand   Synoptic Answer (5 marks):
1. Transport mode (1.5 marks):
In IPsec transport mode, only the payload of the IP packet is
encrypted and/or authenticated, leaving the IP header intact. This
mode is typically used for end-to-end communication between two
hosts.
2. Tunnel mode (1.5 marks):
In IPsec tunnel mode, the entire IP packet (both header and
payload) is encrypted and then encapsulated in a new IP packet
with a new header. Tunnel mode is commonly used for network-to-
network communications or VPNs.
3. Differnces- 2marks
CO4 ; SO4 ;   d. Explain the term SIEM and enlist the benefits of the same.
BL-
Understand   Security information and event management, or SIEM, is a security solution
that helps organizations recognize and address potential security threats and
vulnerabilities before they have a chance to disrupt business operations.
SIEM combines two functions:
• Security information management
• Security event management
This combination provides real-time security monitoring, allowing
teams to track and analyze events and maintain security data logs
for auditing and compliance purposes.
• SIEM makes behavioral anomalies visible to security teams,
enhancing the monitoring process with AI to automate incident
detection and response processes.
It has replaced many manual tasks, becoming a ubiquitous tool for
any security operation center (SOC).
Q2   a. Discuss the various principles involved in private and public key [10]
CO1; SO1;   cryptography. Suppose two users want to exchange confidential data,
BL-low   discuss how key distribution process vary in each technique along with its
advantages and disadvantages.
Private key cryptography [3 marks]
********** 2 **********
--- page 3 ---
Public key cryptography [3 marks]
Public-key cryptography is based on mathematical functions, unlike the
symmetric ciphers that are based on operations on bit patterns. • Public-key
cryptography is asymmetric, involving the use of two separate keys. • Each
user has two keys: Public key of a user is known to others; private key of
the user is known only to the user. • Either of the two keys can be used for
encryption/ decryption. However, a message encrypted with one key can be
decrypted only with the other key. • Examples: RSA
Key distribution [4 marks]
Q2   b. What is Expansion Permutation? Describe any three roles of the expansion [10]
CO2; SO1;   permutation in the DES round function and illustrate its working with neat
BL-   diagram.
Moderate
Marks bifurcation:
What is it? :03 Marks
Three roles of the expansion permutation in the DES: 03 Marks
Diagram: 04 Marks
Synoptic Ans.
What is Expansion Permutation:
Expansion Permutation DES is a process that expands 32-bit input to 48
bits, repeating and rearranging bits for diffusion.
Role of Expansion Permutation in DES Round Function
• Bit Expansion for Key Mixing: Expands 32 bits to 48 bits so it can
be XORed with the 48-bit round key. This ensures proper integration
of the key into the round function.
•   Facilitates Diffusion Across S-boxes: By rearranging and expanding
bits, bits from different positions influence multiple S-box inputs.
This promotes diffusion, spreading the effect of each input bit across
the output.
• Aligns Data Size with the Round Key: Expansion increases the 32-
bit half-block to match the 48-bit round key, enabling proper XOR
********** 3 **********

[Text in pictures on this page, read by OCR]
Bob

To public —

Key-generation
Alice I Public-key distribution procedure

a H channel
1

Public key ¢ f Private key
a |} hee} [

Plaintext Ciphertext Insecure channel Ciphertext Plaintext
--- page 4 ---
operation during the round function. This ensures consistent
processing in all 16 DES rounds.
Diagram:
Q3   a. Summarize the steps in DES algorithm. Compute the output using [10]
CO1; SO1;   following S-box 1 for input value 111010. Write the steps followed
BL-High   for the same.
S1   0   1   2   3   4   5   6   7   8   9   10 11 12 13 14 15
0   14   4 13   1   2 15 11   8   3 10   6 12   5   9   0   7
1   0 15   7   4 14   2 13   1 10   6 12 11   9   5   3   8
2   4   1 14   8 13   6   2 11 15 12   9   7   3 10   5   0
3   15 12   8   2   4   9   1   7   5 11   3 14 10   0   6 13
DES steps-7 m
Output-1m
Steps for finding output-2m
Q3   b. Explain all the steps of RSA algorithm. Jai and Veeru agreed to use RSA [10]
CO2; SO4;   algorithm for the secret communication. Jai securely choose two prime
BL-high   numbers, p=5 and q=7 and a secret key d=23. Jai uses this public key and
sends a ciphertext C=12 to Veeru. Find the original plaintext.
RSA steps-5 marks
Step 1 — Compute n and φ(n) (2 marks)
n = p × q = 5x7 =35
φ(n) = (p−1) (q−1) = 4x6 = 24
Step 2 — Decrypt ciphertext C=12 to get plaintext M (3 marks)
We must compute
M ≡ Cd  mod  n = 1223 mod  35.
M = 3.
Q4   a. Explain encryption and decryption process in AES with neat diagram. [10]
CO1; SO1;   Determine the output after ShiftRow transformation for the state given
BL-high   below:
A1 B2 C3 D4
E5 F6 07 18
19 2A 3B 4C
5D 6E 7F 80
Ans.
Marks bifurcation:
********** 4 **********

[Text in pictures on this page, read by OCR]
Block 1 Block 2 Block 8
123 4 § 676 29 30 31 32

1238 45 6 7 8 9 10 11 12 43 44 45 46 47 48
--- page 5 ---
Encryption & decryption process in AES: 08 marks (diagram 3 marks+
explanation 5 marks)
Solving for Output after shiftrow transformation: 02marks
Encryption and decryption process in AES:
Diagram
The encryption process in AES starts from the round function. Each round
comprises of four sub-processes.
a. SubBytes: The 16 input bytes are substituted by looking up a fixed table
(S-box) given in design. The result is in a matrix of four rows and four
columns.
b. Shiftrows: Each of the four rows of the matrix is shifted to the left.
c. MixColumns: Each column of four bytes is now transformed using a
special mathematical function. This function takes as input the four bytes
of one column and outputs four completely new bytes, which replace the
original column. The result is another new matrix consisting of 16 new
bytes.
d. Addroundkey: The 16 bytes of the matrix are now considered as 128 bits
and are XORed to the 128 bits of the round key. If this is the last round,
then the output is the ciphertext. Otherwise, the resulting 128 bits are
interpreted as 16 bytes and we begin another similar round.
Decryption –above steps in reverse order
Solving for Output after shiftrow transformation: After Shift row
transformation
A1 B2 C3 D4
F6 07 18 E5
3B 4C 19 2A
80 5D 6E 7F
********** 5 **********

[Text in pictures on this page, read by OCR]
Key

+

w0, 3] Add round key

atext

Expand key] [Limverse sup bytes]

Inverse shift rows

yt

wI36, 39]

a:

wi40, 43]

Ciphertext

(a) ption
--- page 6 ---
Q4   b. Describe different types of keys involved in Diffie-Hellman algorithm.   [10]
CO2; SO1;   Alice and Bob agree on a prime number q=11 and a primitive root g=2. If
BL-high   Alice's private key is a=3 and Bob's private key is b=5, what is the shared
secret key they exchange?
Types of Keys- 5 marks
Numerical solution-5 marks
The Diffie-Hellman algorithm involves different types of keys working
together to securely establish a shared secret key between two parties over
an insecure channel. Here are the key types involved:
1. Public Parameters (Public Keys):
2. Private Keys:
3. Public Keys (Generated from Private Keys):
• Using their private keys, parties compute their public keys:
A=gamod  pA=gamodp (Alice’s public key)
B=gbmod  pB=gbmodp (Bob’s public key)
• These public keys are exchanged openly.
4. Shared Secret Key:
This shared secret key can then be used for symmetric encryption to
secure communications.
********** 6 **********

[Text in pictures on this page, read by OCR]
Step 1: Calculate Alice's public key A = g* mod q
A=2> mod11=8 mod 11=8

Step 2: Calculate Bob's public key B = g° mod q
Calculate 2° mod 11:

21=2
?=4
23 =8

24=16=5 modll
2 =5x2=10 modil
So,

B=10
--- page 7 ---
Q5   a. Describe different types of active attacks with the help of suitable [10]
CO1; SO1;   examples. Compare Active attacks with Passive attacks.
BL-low
Active attacks ( 1 mark)- are a type of cybersecurity attack in which an
attacker attempts to alter, destroy, or disrupt the normal operation of a
system or network.
▪ Types of active attacks: (any four -4 marks)
▪ Masquerade
▪ Modification of messages
▪ Repudiation
▪ Replay
▪ Denial of Service
Comparison (any 5: 5 marks)
Active Attacks   Passive Attacks
Attempts to alter, disrupt, or   Attempts to monitor or gather
damage systems/data   information silently
Intrusive and disruptive   Stealthy and non-intrusive
Modify, delete, or corrupt data; gain Collect sensitive data without
control   detection
Often noticeable due to system   Hard to detect; no changes made
changes or failures   to system
Data modification, DoS attacks,   Eavesdropping, traffic analysis,
spoofing   keylogging
Firewalls, intrusion   Encryption, secure protocols,
detection/prevention systems   traffic obfuscation
Long-term risk due to data
Immediate and potentially severe
leakage
********** 7 **********

[Text in pictures on this page, read by OCR]
Step 3: Calculate shared secret key S
* Alice computes S = B? mod q= 10° mod 11

Calculate:
107=100=1 mod 11
10° =10? x 10=1x10=10 mod11
* Bob computes S = A’ mod q=8° mod 11
Calculate powers of 8 modulo 11:
g'=8
8?=64=9 mod 11
88 =9x8=72=6 mod 11
8'=6x8=48=4 mod 1l
8° =4x8=32=10 mod 11

Both get S = 10.
--- page 8 ---
Q5   b. Explain the properties that make a hash function suitable for cryptographic   [10]
CO2; SO4;   applications and describe at least two practical scenarios where hash
BL-low   functions are vital. Discuss features of Message Digest and Secure Hash
Function families.
Hash function propersties-4 marks
Applications-2m
features of MD-2m
features of SHA-2m
Q6   a. Discuss working of PGP encryption. Explain Message generation and   [10]
CO3; SO1;   reception process in PGP in detail.
BL-
moderate   working -3 m
•Step1:PGPgeneratesahuge,one-time-use public encryption algorithm that
can not be guessed, which becomes the random session key.
•Step2:The session key is then encrypted using the recipient’s public key,
which protects the message while being transmitted. The recipient shares
that key with anyone they want to receive messages from.
•Step3:The message sender submits their sessionkey, then the recipient
can decrypt the message using their privatekey.
Generation -3.5 m
•Key Pair Generation:
•The sender generates a key pair consisting of a public key and a private
key.
•Key Distribution:
•The sender shares their public key with the intended recipient.
•Digital Signature:
•The sender signs the message with their private key to create a digital
signature, ensuring authenticity
•Message Encryption:
•The sender encrypts the message using the recipient's public key to
ensure confidentiality.
•Transmission:
•The encrypted message and digital signature are transmitted to the
recipient.
Message reception-3.5m
•Key Pair Import:
•The recipient imports the sender's public key and uses their private key.
•Digital Signature Verification:
•The recipient verifies the digital signature using the sender's public key
to confirm the message's authenticity.
•Message Decryption:
•The recipient decrypts the message using their private key to reveal the
original content.
•Message Authentication:
•The recipient, having verified the signature and decrypted the message,
ensures that the content is unchanged.
•Message Display:
•The decrypted and verified message is displayed to the recipient.
********** 8 **********
--- page 9 ---
Q6   b. CityGrid Utilities manages power grids and water systems through [10]
CO4; SO4;   connected SCADA networks. These systems are increasingly targeted by
BL-Analyze   nation-state actors and malware designed for industrial control systems.
They must implement deep packet inspection, anomaly detection, and
segmented network zones to reduce risks. Which combination of firewalls,
IDS/IPS, and network segmentation strategies would best protect
CityGrid’s operational technology (OT) and prevent lateral movement by
attackers?
Solution- [List benefits of network segmentation, Firewalls or IDS 6M +
Provide combinations 4M]
For CityGrid Utilities, the key goal is to protect operational technology
(OT) such as SCADA networks from sophisticated attacks, including
malware and nation-state threats, while preventing lateral movement and
maintaining operational continuity. Here’s a structured approach
combining firewalls, IDS/IPS, and segmentation strategies:
• Network Segmentation   - Segmentation   is   critical   in OT
environments to isolate critical systems from IT networks and limit
lateral movement. Use industrial firewalls at each boundary.
Implement VLANs or physical separation to isolate OT segments.
Restrict traffic to explicitly allowed protocols and ports only
(whitelisting).
•   Firewalls - Firewalls act as the first line of defense, controlling
inbound/outbound   traffic. Industrial-Grade Firewalls can be
Deployed .
o Default deny-all policy, allow only necessary SCADA
traffic.
o Use stateful inspection to track legitimate connections.
o Place firewalls between DMZ and Control Zone for safe
remote access
• IDS/IPS (Intrusion Detection/Prevention) - Detect and block
suspicious activities without disrupting operations:
o Deploy passive IDS sensors in critical OT segments for
monitoring.
o OT networks have predictable traffic patterns; anomaly
detection can spot malware or unauthorized commands.
o Use tools that understand industrial protocols.
• Deep Packet Inspection (DPI)
•   Inspect industrial protocol traffic at the application layer.
•   Identify malicious commands, unauthorized access, or unusual
patterns.
• Combine with IDS/IPS for automated threat prevention.
Suggested Combination < any two combinations 5M>
********** 9 **********
--- page 10 ---
Layer   Tool/Strategy   Purpose
OT   Control access to SCADA/PLC
Industrial Firewall
Perimeter   networks
OT   Internal Firewalls   / Prevent lateral movement between
Segments   VLANs   zones
Detect   anomalies   and   block
OT Network IDS/IPS with DPI
malicious traffic
IT-OT   DMZ + Firewall + Secure remote access & limit IT-
Boundary   IDS   OT traffic
SIEM + Anomaly
Monitoring   Correlate alerts, detect early threats
Detection
Q7   a. Explain the importance and working of SSL/TLS protocols with emphasis   [10]
CO3; SO4;   on the handshake process. Compare TLS connection with TLS session.
BL-
moderate   Importance of SSL in security (2 marks):
SSL provides data confidentiality, integrity, and authentication, making it
essential for securing online transactions, emails, and other sensitive data
over the internet.
SSL/TLS are cryptographic protocols that provide secure communication
over a computer network by using encryption, authentication, and
integrity mechanisms.
1. Handshake process (4 marks):
○ Step 1: ClientHello (1 mark):
The client initiates the handshake by sending a message that
includes SSL version, cipher settings, session ID, and a
randomly generated number.
○ Step 2: ServerHello (1 mark):
The server responds with its own SSL version, cipher
settings, session ID, and its random number, along with its
digital certificate.
○ Step 3: Server authentication and pre-master secret:
The server's certificate is verified by the client. The client
then generates a pre-master secret, encrypts it using the
server’s public key, and sends it to the server.
○ Step 4: Session keys generated:
Both the client and server generate session keys using the
pre-master secret and the random numbers.
2. Data transmission with encryption:
Once the session keys are exchanged, the client and server use
symmetric encryption to securely transmit data. The integrity of
the message is maintained using MAC (Message Authentication
Code).
3. Session resumption
SSL/TLS allows session resumption where previously negotiated
session parameters can be reused to avoid the overhead of a full
handshake.
Comparison: 4m (any 4 points)
********** 10 **********
--- page 11 ---
Q7   b. Discuss Packet-filtering firewalls. Compare them with Stateful Inspection [10]
CO4; SO1;   firewalls and Application proxies.
BL-
moderate   Packet-filtering firewalls-4m
Comparison-6m
********** 11 **********

[Text in pictures on this page, read by OCR]
TLS Connection & TLS Session

TLS connection TLS session

Itis a transport that provides a suitable type of It is an association between a client and a server
service

Created by the Handshake Protocol
For TLS, such connections are peer-to-peer

relationships
is Define a set of cryptographic security parameters

which can be shared among multiple connections
Connections are transient i.e. temporary

Used to avoid the expensive negotiation of new
Every connection is associated with one session security parameters for each connection

Packet Filtering Stateful Inspection | Application Proxy | Guard Personal Firewall

Simplest More complex Even more complex | Most complex Similar to packet
filtering firewall
Sees only addresses | Can see either Sees full data Sees full text of Can see full data
and service protocol | addresses or data portion of packet communication portion of packet
type
Auditing difficult Auditing possible Can audit activity Can audit activity Canand usually
doesaudit activity
Screens based on Screens based on Screens based on Screens based on Typically, screens
connection rules information across | behavior of proxies | interpretation of based on
packetsin either message content information in a
header or data field single packet, using
header or data
Complex addressing | Usually Simple proxies can | Complex guard Usually starts in
rules can make preconfigured to substitute for functionality can "deny all inbound"

configuration tricky | detect certain attack | complex addressing | limit assurance mode, to which user
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 2da5734b575c

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSE_DS_7057/Cryptography and Network Security/ANS_Cryptography and Network Security(702AI0E007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. TECH (CSE
- DS)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / IV / VI/Semester V/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Cryptography and Network Security
Date: 01 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory. Out of remaining, attempt any 4 questions.
5. In all, 5 questions to be attempted. All questions carry equal marks.
6. Assume Suitable data if necessary
Q1
Answer briefly (each sub-question carries 5 marks):   [20]
CO1 ; SO1 ;   a. How does DES achieve confusion and diffusion? Give the answer with
BL-   justification.
moderate
Marks bifurcation:
Confusion: 2.5 Marks (Give the Proper Ans. 01 Marks + Justification of
Ans. 1.5 Marks)
Diffusion: 2.5 Marks (Give the Proper Ans. 01 Marks + Justification of
Ans. 1.5 Marks)
Synoptic Ans. DES achieves confusion and diffusion as follows:
Confusion: DES introduces confusion by using S-box substitutions in each
Feistel round. The S-boxes replace input bits with output bits in a non-linear
manner, making the relationship between the ciphertext and the encryption
key complex and obscured.
Diffusion: DES achieves diffusion through permutations (P-boxes) and the
Feistel structure, which spread the influence of each input bit across many
output bits over 16 rounds. This ensures that a small change in the plaintext
or key affects many bits of the ciphertext.
CO2 ; SO1 ;   b. Find GCD (2740,1760) using Eucledian algorithm.
BL- Apply   Sol:- We apply the Euclidean algorithm: (5 Marks: 1 mark for each step)
& Analyze   gcd(a, b) = gcd(b, a  mod  b)
Step 1:
2740 = 1760×1 + 980
⇒ gcd (2740, 1760) = gcd (1760, 980)
Step 2:
1760 = 980×1 + 780
⇒ gcd(1760, 980) = gcd(980, 780)
Step 3:
980=780×1+200
⇒ gcd(980, 780) = gcd(780, 200)
********** 1 **********
--- page 2 ---
Step 4:
780 = 200×3 + 180
⇒ gcd(780, 200) = gcd(200, 180)
Step 5:
200 = 180 × 1 + 20
⇒ gcd(200, 180) = gcd(180, 20)
Step 6:
180 = 20×9 + 0
Final Answer: gcd(2740, 1760) = 20
CO3 ;   c.
SO1,SO2 ;   Explain IP Security (IPsec) transport and tunnel modes. How do they defer?
BL-
Understand   Synoptic Answer (5 marks):
1. Transport mode (1.5 marks):
In IPsec transport mode, only the payload of the IP packet is
encrypted and/or authenticated, leaving the IP header intact. This
mode is typically used for end-to-end communication between two
hosts.
2. Tunnel mode (1.5 marks):
In IPsec tunnel mode, the entire IP packet (both header and
payload) is encrypted and then encapsulated in a new IP packet
with a new header. Tunnel mode is commonly used for network-to-
network communications or VPNs.
3. Differnces- 2marks
CO4 ; SO4 ;   d. Explain the term SIEM and enlist the benefits of the same.
BL-
Understand   Security information and event management, or SIEM, is a security solution
that helps organizations recognize and address potential security threats and
vulnerabilities before they have a chance to disrupt business operations.
SIEM combines two functions:
• Security information management
• Security event management
This combination provides real-time security monitoring, allowing
teams to track and analyze events and maintain security data logs
for auditing and compliance purposes.
• SIEM makes behavioral anomalies visible to security teams,
enhancing the monitoring process with AI to automate incident
detection and response processes.
It has replaced many manual tasks, becoming a ubiquitous tool for
any security operation center (SOC).
Q2   a. Discuss the various principles involved in private and public key [10]
CO1; SO1;   cryptography. Suppose two users want to exchange confidential data,
BL-low   discuss how key distribution process vary in each technique along with its
advantages and disadvantages.
Private key cryptography [3 marks]
********** 2 **********
--- page 3 ---
Public key cryptography [3 marks]
Public-key cryptography is based on mathematical functions, unlike the
symmetric ciphers that are based on operations on bit patterns. • Public-key
cryptography is asymmetric, involving the use of two separate keys. • Each
user has two keys: Public key of a user is known to others; private key of
the user is known only to the user. • Either of the two keys can be used for
encryption/ decryption. However, a message encrypted with one key can be
decrypted only with the other key. • Examples: RSA
Key distribution [4 marks]
Q2   b. What is Expansion Permutation? Describe any three roles of the expansion [10]
CO2; SO1;   permutation in the DES round function and illustrate its working with neat
BL-   diagram.
Moderate
Marks bifurcation:
What is it? :03 Marks
Three roles of the expansion permutation in the DES: 03 Marks
Diagram: 04 Marks
Synoptic Ans.
What is Expansion Permutation:
Expansion Permutation DES is a process that expands 32-bit input to 48
bits, repeating and rearranging bits for diffusion.
Role of Expansion Permutation in DES Round Function
• Bit Expansion for Key Mixing: Expands 32 bits to 48 bits so it can
be XORed with the 48-bit round key. This ensures proper integration
of the key into the round function.
•   Facilitates Diffusion Across S-boxes: By rearranging and expanding
bits, bits from different positions influence multiple S-box inputs.
This promotes diffusion, spreading the effect of each input bit across
the output.
• Aligns Data Size with the Round Key: Expansion increases the 32-
bit half-block to match the 48-bit round key, enabling proper XOR
********** 3 **********

[Text in pictures on this page, read by OCR]
Bob

To public —

Key-generation
Alice I Public-key distribution procedure

a H channel
1

Public key ¢ f Private key
a |} hee} [

Plaintext Ciphertext Insecure channel Ciphertext Plaintext
--- page 4 ---
operation during the round function. This ensures consistent
processing in all 16 DES rounds.
Diagram:
Q3   a. Summarize the steps in DES algorithm. Compute the output using [10]
CO1; SO1;   following S-box 1 for input value 111010. Write the steps followed
BL-High   for the same.
S1   0   1   2   3   4   5   6   7   8   9   10 11 12 13 14 15
0   14   4 13   1   2 15 11   8   3 10   6 12   5   9   0   7
1   0 15   7   4 14   2 13   1 10   6 12 11   9   5   3   8
2   4   1 14   8 13   6   2 11 15 12   9   7   3 10   5   0
3   15 12   8   2   4   9   1   7   5 11   3 14 10   0   6 13
DES steps-7 m
Output-1m
Steps for finding output-2m
Q3   b. Explain all the steps of RSA algorithm. Jai and Veeru agreed to use RSA [10]
CO2; SO4;   algorithm for the secret communication. Jai securely choose two prime
BL-high   numbers, p=5 and q=7 and a secret key d=23. Jai uses this public key and
sends a ciphertext C=12 to Veeru. Find the original plaintext.
RSA steps-5 marks
Step 1 — Compute n and φ(n) (2 marks)
n = p × q = 5x7 =35
φ(n) = (p−1) (q−1) = 4x6 = 24
Step 2 — Decrypt ciphertext C=12 to get plaintext M (3 marks)
We must compute
M ≡ Cd  mod  n = 1223 mod  35.
M = 3.
Q4   a. Explain encryption and decryption process in AES with neat diagram. [10]
CO1; SO1;   Determine the output after ShiftRow transformation for the state given
BL-high   below:
A1 B2 C3 D4
E5 F6 07 18
19 2A 3B 4C
5D 6E 7F 80
Ans.
Marks bifurcation:
********** 4 **********

[Text in pictures on this page, read by OCR]
Block 1 Block 2 Block 8
123 4 § 676 29 30 31 32

1238 45 6 7 8 9 10 11 12 43 44 45 46 47 48
--- page 5 ---
Encryption & decryption process in AES: 08 marks (diagram 3 marks+
explanation 5 marks)
Solving for Output after shiftrow transformation: 02marks
Encryption and decryption process in AES:
Diagram
The encryption process in AES starts from the round function. Each round
comprises of four sub-processes.
a. SubBytes: The 16 input bytes are substituted by looking up a fixed table
(S-box) given in design. The result is in a matrix of four rows and four
columns.
b. Shiftrows: Each of the four rows of the matrix is shifted to the left.
c. MixColumns: Each column of four bytes is now transformed using a
special mathematical function. This function takes as input the four bytes
of one column and outputs four completely new bytes, which replace the
original column. The result is another new matrix consisting of 16 new
bytes.
d. Addroundkey: The 16 bytes of the matrix are now considered as 128 bits
and are XORed to the 128 bits of the round key. If this is the last round,
then the output is the ciphertext. Otherwise, the resulting 128 bits are
interpreted as 16 bytes and we begin another similar round.
Decryption –above steps in reverse order
Solving for Output after shiftrow transformation: After Shift row
transformation
A1 B2 C3 D4
F6 07 18 E5
3B 4C 19 2A
80 5D 6E 7F
********** 5 **********

[Text in pictures on this page, read by OCR]
Key

+

w0, 3] Add round key

atext

Expand key] [Limverse sup bytes]

Inverse shift rows

yt

wI36, 39]

a:

wi40, 43]

Ciphertext

(a) ption
--- page 6 ---
Q4   b. Describe different types of keys involved in Diffie-Hellman algorithm.   [10]
CO2; SO1;   Alice and Bob agree on a prime number q=11 and a primitive root g=2. If
BL-high   Alice's private key is a=3 and Bob's private key is b=5, what is the shared
secret key they exchange?
Types of Keys- 5 marks
Numerical solution-5 marks
The Diffie-Hellman algorithm involves different types of keys working
together to securely establish a shared secret key between two parties over
an insecure channel. Here are the key types involved:
1. Public Parameters (Public Keys):
2. Private Keys:
3. Public Keys (Generated from Private Keys):
• Using their private keys, parties compute their public keys:
A=gamod  pA=gamodp (Alice’s public key)
B=gbmod  pB=gbmodp (Bob’s public key)
• These public keys are exchanged openly.
4. Shared Secret Key:
This shared secret key can then be used for symmetric encryption to
secure communications.
********** 6 **********

[Text in pictures on this page, read by OCR]
Step 1: Calculate Alice's public key A = g* mod q
A=2> mod11=8 mod 11=8

Step 2: Calculate Bob's public key B = g° mod q
Calculate 2° mod 11:

21=2
?=4
23 =8

24=16=5 modll
2 =5x2=10 modil
So,

B=10
--- page 7 ---
Q5   a. Describe different types of active attacks with the help of suitable [10]
CO1; SO1;   examples. Compare Active attacks with Passive attacks.
BL-low
Active attacks ( 1 mark)- are a type of cybersecurity attack in which an
attacker attempts to alter, destroy, or disrupt the normal operation of a
system or network.
▪ Types of active attacks: (any four -4 marks)
▪ Masquerade
▪ Modification of messages
▪ Repudiation
▪ Replay
▪ Denial of Service
Comparison (any 5: 5 marks)
Active Attacks   Passive Attacks
Attempts to alter, disrupt, or   Attempts to monitor or gather
damage systems/data   information silently
Intrusive and disruptive   Stealthy and non-intrusive
Modify, delete, or corrupt data; gain Collect sensitive data without
control   detection
Often noticeable due to system   Hard to detect; no changes made
changes or failures   to system
Data modification, DoS attacks,   Eavesdropping, traffic analysis,
spoofing   keylogging
Firewalls, intrusion   Encryption, secure protocols,
detection/prevention systems   traffic obfuscation
Long-term risk due to data
Immediate and potentially severe
leakage
********** 7 **********

[Text in pictures on this page, read by OCR]
Step 3: Calculate shared secret key S
* Alice computes S = B? mod q= 10° mod 11

Calculate:
107=100=1 mod 11
10° =10? x 10=1x10=10 mod11
* Bob computes S = A’ mod q=8° mod 11
Calculate powers of 8 modulo 11:
g'=8
8?=64=9 mod 11
88 =9x8=72=6 mod 11
8'=6x8=48=4 mod 1l
8° =4x8=32=10 mod 11

Both get S = 10.
--- page 8 ---
Q5   b. Explain the properties that make a hash function suitable for cryptographic   [10]
CO2; SO4;   applications and describe at least two practical scenarios where hash
BL-low   functions are vital. Discuss features of Message Digest and Secure Hash
Function families.
Hash function propersties-4 marks
Applications-2m
features of MD-2m
features of SHA-2m
Q6   a. Discuss working of PGP encryption. Explain Message generation and   [10]
CO3; SO1;   reception process in PGP in detail.
BL-
moderate   working -3 m
•Step1:PGPgeneratesahuge,one-time-use public encryption algorithm that
can not be guessed, which becomes the random session key.
•Step2:The session key is then encrypted using the recipient’s public key,
which protects the message while being transmitted. The recipient shares
that key with anyone they want to receive messages from.
•Step3:The message sender submits their sessionkey, then the recipient
can decrypt the message using their privatekey.
Generation -3.5 m
•Key Pair Generation:
•The sender generates a key pair consisting of a public key and a private
key.
•Key Distribution:
•The sender shares their public key with the intended recipient.
•Digital Signature:
•The sender signs the message with their private key to create a digital
signature, ensuring authenticity
•Message Encryption:
•The sender encrypts the message using the recipient's public key to
ensure confidentiality.
•Transmission:
•The encrypted message and digital signature are transmitted to the
recipient.
Message reception-3.5m
•Key Pair Import:
•The recipient imports the sender's public key and uses their private key.
•Digital Signature Verification:
•The recipient verifies the digital signature using the sender's public key
to confirm the message's authenticity.
•Message Decryption:
•The recipient decrypts the message using their private key to reveal the
original content.
•Message Authentication:
•The recipient, having verified the signature and decrypted the message,
ensures that the content is unchanged.
•Message Display:
•The decrypted and verified message is displayed to the recipient.
********** 8 **********
--- page 9 ---
Q6   b. CityGrid Utilities manages power grids and water systems through [10]
CO4; SO4;   connected SCADA networks. These systems are increasingly targeted by
BL-Analyze   nation-state actors and malware designed for industrial control systems.
They must implement deep packet inspection, anomaly detection, and
segmented network zones to reduce risks. Which combination of firewalls,
IDS/IPS, and network segmentation strategies would best protect
CityGrid’s operational technology (OT) and prevent lateral movement by
attackers?
Solution- [List benefits of network segmentation, Firewalls or IDS 6M +
Provide combinations 4M]
For CityGrid Utilities, the key goal is to protect operational technology
(OT) such as SCADA networks from sophisticated attacks, including
malware and nation-state threats, while preventing lateral movement and
maintaining operational continuity. Here’s a structured approach
combining firewalls, IDS/IPS, and segmentation strategies:
• Network Segmentation   - Segmentation   is   critical   in OT
environments to isolate critical systems from IT networks and limit
lateral movement. Use industrial firewalls at each boundary.
Implement VLANs or physical separation to isolate OT segments.
Restrict traffic to explicitly allowed protocols and ports only
(whitelisting).
•   Firewalls - Firewalls act as the first line of defense, controlling
inbound/outbound   traffic. Industrial-Grade Firewalls can be
Deployed .
o Default deny-all policy, allow only necessary SCADA
traffic.
o Use stateful inspection to track legitimate connections.
o Place firewalls between DMZ and Control Zone for safe
remote access
• IDS/IPS (Intrusion Detection/Prevention) - Detect and block
suspicious activities without disrupting operations:
o Deploy passive IDS sensors in critical OT segments for
monitoring.
o OT networks have predictable traffic patterns; anomaly
detection can spot malware or unauthorized commands.
o Use tools that understand industrial protocols.
• Deep Packet Inspection (DPI)
•   Inspect industrial protocol traffic at the application layer.
•   Identify malicious commands, unauthorized access, or unusual
patterns.
• Combine with IDS/IPS for automated threat prevention.
Suggested Combination < any two combinations 5M>
********** 9 **********
--- page 10 ---
Layer   Tool/Strategy   Purpose
OT   Control access to SCADA/PLC
Industrial Firewall
Perimeter   networks
OT   Internal Firewalls   / Prevent lateral movement between
Segments   VLANs   zones
Detect   anomalies   and   block
OT Network IDS/IPS with DPI
malicious traffic
IT-OT   DMZ + Firewall + Secure remote access & limit IT-
Boundary   IDS   OT traffic
SIEM + Anomaly
Monitoring   Correlate alerts, detect early threats
Detection
Q7   a. Explain the importance and working of SSL/TLS protocols with emphasis   [10]
CO3; SO4;   on the handshake process. Compare TLS connection with TLS session.
BL-
moderate   Importance of SSL in security (2 marks):
SSL provides data confidentiality, integrity, and authentication, making it
essential for securing online transactions, emails, and other sensitive data
over the internet.
SSL/TLS are cryptographic protocols that provide secure communication
over a computer network by using encryption, authentication, and
integrity mechanisms.
1. Handshake process (4 marks):
○ Step 1: ClientHello (1 mark):
The client initiates the handshake by sending a message that
includes SSL version, cipher settings, session ID, and a
randomly generated number.
○ Step 2: ServerHello (1 mark):
The server responds with its own SSL version, cipher
settings, session ID, and its random number, along with its
digital certificate.
○ Step 3: Server authentication and pre-master secret:
The server's certificate is verified by the client. The client
then generates a pre-master secret, encrypts it using the
server’s public key, and sends it to the server.
○ Step 4: Session keys generated:
Both the client and server generate session keys using the
pre-master secret and the random numbers.
2. Data transmission with encryption:
Once the session keys are exchanged, the client and server use
symmetric encryption to securely transmit data. The integrity of
the message is maintained using MAC (Message Authentication
Code).
3. Session resumption
SSL/TLS allows session resumption where previously negotiated
session parameters can be reused to avoid the overhead of a full
handshake.
Comparison: 4m (any 4 points)
********** 10 **********
--- page 11 ---
Q7   b. Discuss Packet-filtering firewalls. Compare them with Stateful Inspection [10]
CO4; SO1;   firewalls and Application proxies.
BL-
moderate   Packet-filtering firewalls-4m
Comparison-6m
********** 11 **********

[Text in pictures on this page, read by OCR]
TLS Connection & TLS Session

TLS connection TLS session

Itis a transport that provides a suitable type of It is an association between a client and a server
service

Created by the Handshake Protocol
For TLS, such connections are peer-to-peer

relationships
is Define a set of cryptographic security parameters

which can be shared among multiple connections
Connections are transient i.e. temporary

Used to avoid the expensive negotiation of new
Every connection is associated with one session security parameters for each connection

Packet Filtering Stateful Inspection | Application Proxy | Guard Personal Firewall

Simplest More complex Even more complex | Most complex Similar to packet
filtering firewall
Sees only addresses | Can see either Sees full data Sees full text of Can see full data
and service protocol | addresses or data portion of packet communication portion of packet
type
Auditing difficult Auditing possible Can audit activity Can audit activity Canand usually
doesaudit activity
Screens based on Screens based on Screens based on Screens based on Typically, screens
connection rules information across | behavior of proxies | interpretation of based on
packetsin either message content information in a
header or data field single packet, using
header or data
Complex addressing | Usually Simple proxies can | Complex guard Usually starts in
rules can make preconfigured to substitute for functionality can "deny all inbound"

configuration tricky | detect certain attack | complex addressing | limit assurance mode, to which user
````
