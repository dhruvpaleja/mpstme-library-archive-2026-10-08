# Cyber Security: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 3fc52d8b688d

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Cyber Security/ANS_Cyber Security(703AI0C005)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 26 Nov 2025
- Text: mixed (6 pages), mean OCR confidence 73.2

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Cyber Security
Date: 26 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory. Out of remaining questions, attempt any 4 questions.
5. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO1; SO1 ;BL-   a.   Discuss the importance of Key Security Components in real world   [5]
low   software applications.
CIA components-3m
importance-2 mark each
CO2; SO1 ;BL-   b.   Discuss importance and working of One-Time Password.   [5]
moderate
Importance-2M
Working-3M
CO3; SO1;BL-   c.   Discuss Transport mode of VPN. Compare it with Tunnel mode VPN.   [5]
low
Transport mode explanation-3m
comparison-2m
CO4; SO1;BL2   d. What is Risk management? Enlist Steps in Risk Management.   [5]
RM-1M
Steps-4M
Q2
CO1; SO1; BL2   a.   Explain different types of attacks. Consider a smart home application that   [10]
controls connected devices like cameras and door locks. Who could target
this system for an attack? What kind of damage might they want to cause?
What weaknesses might they exploit to gain unauthorized access?
Types of attacks-4m
Potential attackers: -2m
Hackers, cyberstalkers, burglars, privacy invaders.
Intended harm: -2m
Unauthorized surveillance, control over home devices, data leaks,
physical security breaches.
Possible vulnerabilities: -2m
********** 1 **********
--- page 2 ---
Poor encryption, weak passwords, outdated firmware, insecure
communication protocols.
CO2; SO1; BL2   b. What are transposition ciphers? Compare them with substitution ciphers.   [10]
Explain any two types of transposition ciphers with suitable examples.
transposition ciphers -2m
comparison-4m
2m per type
Q3
CO1; SO1;BL2   a.   Write the steps of RSA algorithm and use them to encrypt the message   [10]
value ‘16’. Consider P=3 and Q=5; Assume suitable values for E and
D.
Steps of the RSA Algorithm [5 Marks]
1. Key Generation:
o Choose two large prime numbers p and q.
o Compute n=p×q, which forms part of the public and
private key pair.
o Compute ϕ(n)=(p−1)×(q−1) (Euler's totient function).
o Choose a public exponent e, such that 1<e<ϕ(n) and
gcd(e, ϕ(n))=1.
o Compute the private key d, the modular inverse of e
mod ϕ(n). This means solving d×e≡1 mod ϕ(n) using the
Extended Euclidean Algorithm.
o The public key is (e, n) and the private key is (d, n).
2. Encryption:
o The sender takes the plaintext message M and computes
the ciphertext C using the recipient's public key (e, n):
C ≡ Me mod n
o The ciphertext C is sent to the recipient.
3. Decryption:
o The recipient uses their private key (d, n) to decrypt the
ciphertext C back into plaintext M:
M ≡ Cd mod n
Computation of E and D : 3 marks
********** 2 **********
--- page 3 ---
Encryption: 2 marks
CO2; SO1;BL2   b. How biometric authentication is better than other authentication methods?   [10]
Discuss various biometric features with applications used   for
authentication.
biometric authentication is better-3m
Features with applications-7m
Q4
CO3; SO1;BL2   a. Summarize the steps in DES algorithm with neat diagram.   [10]
DES steps-7 m
diagram -3m
 Step 1: Apply an initial permutation on a block.
 Result is B=IP(P) where P is the 64 bit block IP Initial
Permutation function and B the result.
   Step 2: Split B into 32 bit blocks
   Li = leftmost 32 bits
Ri = rightmost 32 bits.
********** 3 **********
--- page 4 ---
   Step 3: Pick a 56 bit key. Permute it
   Step 4: Left circular shift it by 1 bit giving K1.
 Step 5: Perform a complex sequence of operations and obtain
 X1 = F(R1,K1) (The complex set of operations include table
look up and dropping bits).
 Step 6: Find R2 = L1 + X1
 Step 7: Set L2 = R1
 Repeat steps 2 to 7 , 16 times to get B16 = L16,R16
 Step 8: Apply inverse of initial permutation on B16
 The result is the encrypted block
CO4; SO1;BL2   b.   Explain Access Control Matrices with suitable example. Compare them   [10]
with Access Control Lists.
ACM-6m
Comparison-4m
Q5
CO3; SO1;BL2   a. What are non-malicious program errors? Explain their major types.   [10]
1 m – non-malicious program errors
3 marks for each type
CO4; SO2;BL2   b.   Explain Link encryption with the help of neat diagram and compare it   [10]
with End-to-End Encryption.
Link encryption with diagram-5m
Comparison-5m
Link Encryption In link encryption, data are encrypted justbefore the
system places them on the physical communications link. at layer 1 or 2
in the OSI model. Similarly, decryption occurs just as the communication
arrives at and enters the receiving computer
Q6
********** 4 **********
--- page 5 ---
CO1; SO2;BL4   a. What are Stateful inspection firewalls? Compare them with Application   [10]
Proxy firewalls and Packet filtering firewalls.
Stateful inspection firewalls -3m
comparison-7m
CO4; SO1;BL2   b. A hospital network in a hurricane-prone region assessing risks related to   [10]
extreme weather events.Summarize the steps involved in Risk Analysis for
it.
6m- steps
Steps of a Risk Analysis
1. Identify assets.
2. Determine vulnerabilities.
3. Estimate likelihood of exploitation.
4. Compute expected annual loss.
5. Survey applicable controls and their costs.
6. Project annual savings of control
4m – examples/solutions for given scenario
This includes evaluating the stability of infrastructure, emergency
response plans, continuity of care during power outages, access to
electronic health records, and patient evacuation procedures to mitigate the
impact of natural disasters on service delivery.
Q7
CO3; SO1; BL1   a.   Discuss design goals of Kerberos systems. Give all the steps involved   [10]
in authentication mechanism of Kerberos.
Goals- 3m
No passwords are communicated on the network.
Provides cryptographic protection against spoofing.
Limited period of validity (of tickets)
Mutual authentication
Steps-7m
CO2; SO1; BL2   b. Why Digital signatures are important? Discuss the process for creating and   [10]
verifying Digital Signatures. How are they different from Digital
certificates?
********** 5 **********
--- page 6 ---
Importance-2m

Process-6m
Creating and verifying a digital signature
[=| Cant , Encrypt the hasheode with \
= key of the sender
=|"
Creation of a digitally
signed document
(sender)
Verifying the
digital signature
(receiver)

ithe calculated hasheode does not match the result of the decrypted signature. eather the document was:
changed after signing, or the signature was not generated with the private key of the alleged sender,

Comparison-2m

FEC 6 FC IG Ir
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper eceaaff8945d

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CS_7055/Cyber Security/ANS_Cyber Security(702AI0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Cyber Security
Date: 04 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
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
a. Define CIA triad. A bank provides a mobile application that supports balance inquiry, fund   [5]
transfers, bill payments, and transaction history. Authentication is performed using
biometrics and OTP. Customers expect the service to be accessible at all times, including
during national holidays. Any inconsistency in transaction records may lead to financial
disputes. From the given scenario, identify the confidentiality, integrity, and availability
requirements of the system.
Ans.
Definitions of CIA (Each 1 marks). Scenario answer (2 marks)
CIA Triad Definition:
The CIA Triad is a fundamental concept in information security consisting of three key
principles:
•   Confidentiality – Ensures that sensitive information is accessed only by
authorized users.
•   Integrity – Ensures that data remains accurate, consistent, and unaltered.
•   Availability – Ensures that systems and data are accessible to users whenever
needed.
Application to the Given Banking Scenario:
1. Confidentiality:
The mobile banking app must protect sensitive customer data such as account
details, transaction history, and login credentials. The use of biometric
authentication and OTP ensures that only authorized users can access the account,
preventing unauthorized access.
2. Integrity:
The system must ensure that all transaction records (balance, fund transfers, bill
payments) are accurate and not tampered with. Any inconsistency in records can
lead to financial disputes, so data must remain consistent and reliable at all times.
3. Availability:
The banking application should be available to customers 24/7, including during
********** 1 **********
--- page 2 ---
national holidays. Users expect uninterrupted access to services like balance
inquiry and fund transfers, so system downtime must be minimized.
b. Explain the additive cipher and encrypt the plaintext “ROCKSTAR” with the key value =   [5]
12.
Ans:
Definition: (1 Marks)
The additive cipher is a simple substitution cipher where each letter in the plaintext is
shifted a fixed number of positions down the alphabet. This fixed number is the key.
• Encryption Process:
o Assign numerical values to letters (A=0, B=1, ..., Z=25).
o For each letter in the plaintext, add the key value (k) to its numerical
value.
o Take the result modulo 26 (to wrap around the alphabet).
o Convert the resulting numerical value back to a letter.
• Formula: Ciphertext (C) = (Plaintext (P) + Key (k)) mod 26
Encryption of "ROCKSTAR" with Key = 12: (3 Marks)
1. Convert to Numbers:
o R = 17, O = 14, C = 2, K = 10, S = 18, T = 19, A = 0, R = 17
2. Apply the Cipher (Add 12, mod 26):
o R (17) + 12 = 29 mod 26 = 3 (D)
o O (14) + 12 = 26 mod 26 = 0 (A)
o C (2) + 12 = 14 mod 26 = 14 (O)
o K (10) + 12 = 22 mod 26 = 22 (W)
o S (18) + 12 = 30 mod 26 = 4 (E)
o T (19) + 12 = 31 mod 26 = 5 (F)
o A (0) + 12 = 12 mod 26 = 12 (M)
3. Ciphertext: (1 Mark)
o "DAOWEFMD"
c. What are biometrics and how does biometric authentication work with suitable diagram?   [5]
Marks Distribution:
1 mark for definition of biometrics
2 marks for explaining biometric authentication process
2 marks for diagram
Answer:
Biometrics refers to the automated examination of biological or behavioral traits of a
human being with the aim of identifying them. It is premised on distinct physical or
behavioral characteristics of people.
In Biometric authentication, biometric information like fingerprint or voice pattern of the
user is stored in the system upon registration. When the user is logging in, the system will
again take the user biometric information and match it with the stored information. In the
event the match falls within an acceptable limit the user is authenticated, otherwise the
access is denied. Fingerprints and voice recognition are two examples of biometric
methods.
Fingerprint recognition is the method of identifying an individual using the distinctive
arrangement of crests and furrows on his or her fingers. Voice recognition is based on the
features of the voice of the individual e.g. tone and pitch to identify a person.
Diagram:
********** 2 **********
--- page 3 ---
d.   Enlist and explain firewall filter characteristics   [5]
Ans.
Listing of any three kind of firewall filter 0.5M and Write any two characteristics for
each one: 1.5 marks for each [0.5 + 4.5]
Packet Filtering:
 The firewall examines incoming and outgoing packets based on predefined rules.
   It checks parameters such as source IP, destination IP, port number, and protocol.
Stateful Inspection
 Tracks the state of active connections.
 Allows packets only if they belong to an established and legitimate session.
Application-Level Filtering
 Monitors and controls traffic based on specific applications or services.
 Can block suspicious application behaviors (e.g., unknown executables,
malware).
Q2 a   Differentiate between DAC and RBAC   [10]
Ans.
Marks Bifurcation: 01marks for one difference
Discretionary Access Control   Role-Based Access Control
Parameter
(DAC)   (RBAC)
Access control mechanism
Access control mechanism
where permissions are assigned
Definition   where the owner of a resource
to roles, and users are assigned
decides who can access it.
roles.
Control   Resource owner controls access System administrator defines
Authority   permissions.   roles and permissions.
Permissions are assigned to
Access   Permissions are assigned directly
roles, then users inherit
Assignment   to users.
permissions through roles.
User → Role → Permission →
Access Structure User → Resource → Permission
Resource
Highly flexible because users   Less flexible but more structured
Flexibility
can grant access to others.   and manageable.
Lower security due to risk of
Higher security because access
Security Level   permission propagation and
is controlled centrally.
misuse.
********** 3 **********
--- page 4 ---
Difficult to manage in large
Highly scalable for large
Scalability   organizations due to many user
enterprises with many users.
permissions.
High administrative overhead as Lower overhead because
Administrative
permissions must be managed   permissions are managed
Effort
individually.   through roles.
Principle of   Easier to enforce by designing
Difficult to enforce consistently.
Least Privilege   appropriate roles.
In an organization, an employee
In a file system, a user shares a
assigned the “Manager” role
Example   file and grants read/write access
automatically receives
to other users.
predefined permissions.
Q2 b   Describe the SYN spoofing attack and explain with the help of a simple diagram.   [10]
Ans.
Marks Bifurcation: 5marks explanation and 5marks diagram
A SYN spoofing attack is a type of Denial of Service (DoS) attack where the attacker
abuses the TCP three-way handshake by sending a large number of SYN (synchronize)
requests with forged (spoofed) IP addresses.
How the Attack Works
1. Attacker Sends Fake SYN Requests
2. Server Responds with SYN-ACK
3. No ACK Comes Back
4. Server Resources Get Exhausted
Diagram:
The diagram illustrates how an attacker performs a SYN spoofing attack by exploiting
the TCP three-way handshake. It involves three main roles:
 Attacker
 Server (victim)
 Spoofed Client (a fake or non-existent IP address)
Q3 a   Encrypt the Message = “CYBER SECURITY” using Key = “DIPLOMAT” using Playfair   [10]
Scheme. Explain the steps involved.
Ans.
Step 1 Key Table construction: [2 Marks]
********** 4 **********
--- page 5 ---
D I/J P L O
M A T B C
E F G H K
N Q R S U
V W X Y Z
Step 2 Apply Playfair Scheme Rules for encryption [7 Marks- 1 marks for each pair]
Pair 1 = (C,Y) = (B,Z)
PAIR 2 = (BE) = (M,H)
PAIR 3 = (R,S) = (S,U)
PAIR 4 = (E,C) = (K,M)
PAIR 5 = (U,R) = (N,S)
PAIR 6 = (I,T) = (P,A)
PAIR 7 = (Y,X) = (Z,Y)
Step 3: Final Ciphertext: [1 mark]
BZMHSUKMNSPAZY
Q3 b   Explain the various types of malware in detail. Compare them based on their methods of   [10]
propagation and their behavioral characteristics.
Ans.
Marks Bifurcation: Introduction to Malware – 1 Mark, Explanation of Types of Malware
– 5 Marks, Comparison Based on Propagation – 2 Marks, Comparison Based on
Behavioral Characteristics – 2 Marks
Introduction to Malware: Malware (malicious software) refers to any program
intentionally developed to damage, infiltrate, disrupt, or gain unauthorized access to
computer systems.
Types of Malware: Virus, Worm, Trojan horse, Ransomware, Spyware, Rootkit, Botnets
Comparison Based on Methods of Propagation:
Malware Type   Propagation Method
Virus   Spreads through file sharing; requires execution by user.
Worm   Self-propagates   across   networks by   exploiting
vulnerabilities.
Trojan horse   Delivered through   social engineering; no   self-
spreading.
Ransomware   Email phishing, malicious links, exploit kits.
Spyware   Installed with bundled software or Trojans.
Rootkit   Installed after gaining admin privileges; often via
Trojans
Botnets   Spread via worms, Trojans, or drive-by downloads.
Q4 a   Answer the following questions with respect to Data Encryption Standard.   [10]
i)   How many rounds are used?
ii)   Is Data Encryption Standard used now-a-days?
iii)   What was the significance of the Data Encryption Standard in the history of
cryptography?
iv)   Are there any known weaknesses in Data Encryption Standard?
v)   Discuss the internal function working used in each round of Data Encryption
Standard.
vi)   How the 64-bit key is converted to 48-bit key as input to the function of each
round?
Ans.
i) How many rounds are used? (1 Mark)
DES uses 16 rounds of encryption.
********** 5 **********
--- page 6 ---
ii) Is Data Encryption Standard considered secure today? (1 Mark)
No, DES is not considered secure today. Its 56-bit key length is too short and can be
easily cracked using modern computing power.
iii) What was the significance of the Data Encryption Standard in the history of
cryptography? (1 Mark)
DES was a landmark in the history of cryptography. It was the first widely adopted
symmetric-key encryption algorithm standardized by the U.S. government (NBS, now
NIST). It played a crucial role in the development and understanding of modern
cryptography and was used for a long time in various applications, including financial
transactions.
iv) Are there any known weaknesses in Data Encryption Standard? (2 Mark)
Yes, there are several known weaknesses:
i)   Short Key Length: The 56-bit key is its primary weakness,
making it susceptible to brute-force attacks.
ii)   Weak S-Boxes: Some researchers have suggested that the S-
boxes were designed with potential backdoors, although this
has never been definitively proven.
iii)   Semi-Weak Keys: There are a few semi-weak keys that can
produce the same ciphertext when used for both encryption
and decryption.
v)   Discuss the internal function working used in each round of Data Encryption
Standard. (2.5 Marks)
Each round in DES involves the following steps: 1. Expansion Permutation (E-Box): The
32-bit right half of the data is expanded to 48 bits using the E-box. 2. Key Mixing: The
48-bit expanded data is XORed with a 48-bit round key. 3. S-Box Substitution: The 48-
bit result is divided into eight 6-bit blocks, each of which is input into a corresponding S-
box. The S-boxes perform a non-linear substitution, reducing the 48 bits back to 32 bits.
4. Permutation (P-Box): The 32-bit output of the S-boxes is permuted using the P-box. 5.
XOR with Left Half: The 32-bit output of the P-box is XORed with the 32-bit left half of
the data. 6. Swap: The left and right halves are swapped for the next round (except for
the last round).
vi) How is the 64-bit key converted to a 48-bit key as input to the function of each
round? (2.5 Marks)
The 64-bit key undergoes the following process:
1. Permuted Choice 1 (PC-1): The 64-bit key has 8 parity bits, which are discarded. The
remaining 56 bits are permuted using PC-1.
2. Key Splitting and Shifting: The 56-bit key is split into two 28-bit halves. Each half is
circularly left-shifted by either 1 or 2 bits, depending on the round.
3. Permuted Choice 2 (PC-2): The 56-bit shifted halves are combined and permuted
using PC-2, resulting in a 48-bit round key. This 48-bit round key is then used in the
round function.
Q4 b   Analyze the concept of a honeypot by examining its purpose in a security architecture.   [10]
Compare different types of honeypots and evaluate how each type contributes differently
to threat detection.
Marks Bifurcation: Introduction to Honeypots – 1 Mark, Purpose of Honeypots in Security
Architecture – 2 Marks, Types of Honeypots (Explanation) – 4 Marks, Comparison &
Evaluation of Honeypots – 3 Marks
Introduction to Honeypots: A honeypot is a deliberately vulnerable system, service, or
network resource designed to attract attackers.
Purpose of Honeypots in Security Architecture:
i. Threat Detection
ii. Attack Analysis
iii. Deception and Diversion
********** 6 **********
--- page 7 ---
iv. Early Warning System
Types of Honeypots:
Low-Interaction Honeypots: 1marks
Simulate only limited services (e.g., SSH banner, fake FTP). Capture basic scanning
attempts, automated malware.
Medium-Interaction Honeypots: 1marks
Provide partial implementation of services. Engage attackers long enough to analyze
tactics.
High-Interaction Honeypots: 1marks
Real operating systems with actual services. Provide the most detailed information about
attacker behavior.
Research Honeypots: 1marks
Used by security researchers to study advanced threats. Capture deep insights into attacker
motives and methodologies.
Comparison & Evaluation of Honeypots:
Type   Data Collected   Risk Level   Use
Low-   Minimal (scans, probes) Very low   Detect basic malware,
Interaction   bots
Medium-   More details   Medium   Analyze   attack
Interaction   techniques
High-   Extensive, deep insights High   Research   APTs,
Interaction   sophisticated attackers
Q5 a   Define risk and explain the need for risk analysis for information security. State and   [10]
explain all the terminologies related to risk analysis.
Marks Bifurcation: Definition of Risk – 1 Mark, Need for Risk Analysis – 3 Marks, Risk
Analysis Terminologies (Explanation) – 6 Marks
Definition of Risk – Risk is the potential for loss, damage, or negative impact to an
organization’s assets due to a threat exploiting a vulnerability.
Need for Risk Analysis:
i. Prioritization of Security Efforts
ii. Optimal Resource Allocation
iii. Compliance and Legal Requirements
iv. Preventing Financial and Reputation Loss
v. Improved Decision-Making
Risk Analysis Terminologies:
i. Asset
ii. Threat
iii. Vulnerability
iv. Likelihood
v. Risk
vi. Risk Assessment
vii. Risk Mitigation
viii. Residual Risk
Q5 b   Explain how an attacker can exploit a buffer overflow vulnerability to gain control over a   [10]
system. Analyze the sequence of events involved in such an attack.
Ans.
Marks Bifurcation: Introduction to Buffer Overflow – 2 Marks, How Attackers Exploit
Buffer Overflow – 4 Marks, Sequence of Events in a Buffer Overflow Attack – 4 Marks
Introduction to Buffer Overflow:
A buffer overflow occurs when a program writes more data into a buffer than it can hold.
This extra data overwrites adjacent memory areas such as return addresses, function
pointers, or control structures. Attackers exploit buffer overflow vulnerabilities to inject
malicious code and execute it, ultimately gaining unauthorized control over a system.
********** 7 **********
--- page 8 ---
How Attackers Exploit a Buffer Overflow:
i. Overwriting Memory Locations
ii. Injecting Malicious Shellcode
iii. Redirecting Program Execution
iv. Gaining System Control
Sequence of Events in a Buffer Overflow Attack:
Step 1: Identifying a Vulnerable Program
Step 2: Crafting Malicious Input
Step 3: Triggering the Overflow
Step 4: Hijacking the Control Flow
Step 5: Execution of Malicious Code
Q6 a   Explain the working of the Kerberos authentication process with a neat diagram.   [10]
Marks Bifurcation: 5m diagram, 5m explanation
Explanation:
Kerberos is a network authentication protocol that uses symmetric-key cryptography and
a trusted third party called the Key Distribution Center (KDC). The KDC consists of two
main components: Authentication Server (AS) and Ticket Granting Server (TGS)
Step-by-Step Working of Kerberos:
1. User Login & Request to Authentication Server (AS)
2. Authentication Server Verifies User & Issues TGT
3. Client Requests Service Ticket from TGS
4. TGS Verifies Ticket & Authenticator, Issues Service Ticket
5. Client Requests Access from Service Server
6. Service Server Validates & Grants Access
Diagram:
Q6 b   Mention and explain the steps for risk analysis and management   [10]
Ans.
********** 8 **********
--- page 9 ---
Marks Bifurcation: Introduction to Risk Analysis & Management – 2 Marks, Steps in
Risk Analysis – 4 Marks, Steps in Risk Management – 4 Marks
Introduction to Risk Analysis & Management:
Risk analysis and management is a systematic process used to identify, evaluate, and
treat risks that can impact information assets.
Steps in Risk Analysis:
Step 1: Asset Identification
Step 2: Threat Identification
Step 3: Vulnerability Assessment
Step 4: Risk Assessment
Steps in Risk Management:
Step 1: Risk Evaluation & Prioritization
Step 2: Risk Treatment (Mitigation Strategies)
Step 3: Implementation of Controls
Step 4: Monitoring & Review
Q7 a   Explain the digital signature working and its advantages. Discuss how RSA digital   [10]
signature can be used for ensuring authentication using block diagram?
Ans
Digital Signature Process: (3 Marks)
1. Hashing:
o The sender generates a unique fixed-size hash (digest) of the message
using a cryptographic hash function (e.g., SHA-256).
o The hash represents the message's content.
2. Signing:
o The sender encrypts the hash using their private key.
o This encrypted hash is the digital signature.
3. Appending:
o The sender appends the digital signature to the message.
4. Verification:
o The receiver receives the message and the digital signature.
o The receiver generates a hash of the received message using the same
hash function.
o The receiver decrypts the digital signature using the sender's public key.
o The receiver compares the generated hash with the decrypted signature.
o   If the hashes match, the signature is valid, and the message is authentic.
Benefits of Digital Signatures: (2 Marks)
•   Authentication: Verifies the sender's identity.
•   Integrity: Ensures the message has not been altered.
•   Non-repudiation: Prevents the sender from denying sending the message.
Block Diagram: (2 Marks)
Explanation: (3 Marks)
1. Sender (A) Side:
o Sender (A) creates a message (M).
o Sender (A) generates a hash (H) of the message using a hash function.
o Sender (A) encrypts the hash (H) using their private key (dA) to create the
digital signature (S).
********** 9 **********
--- page 10 ---
o Sender (A) sends the message (M) and the digital signature (S) to
Receiver (B).
2. Receiver (B) Side:
o Receiver (B) receives the message (M) and the digital signature (S).
o Receiver (B) generates a hash (H') of the received message (M) using the
same hash function.
o Receiver (B) decrypts the digital signature (S) using Sender (A)'s public
key (eA).
o Receiver (B) compares the generated hash (H') with the decrypted
signature (S).
If H' and S are identical, the signature is valid, and the message is authenticated.
Q7 b   Apply your understanding of cybersecurity concepts to compare threats and vulnerabilities   [5]
with suitable real-world examples.
Ans.
Marks Bifurcation: Definition of Threat – 1 Mark, Definition of Vulnerability – 1 Mark,
Comparison Between Threats & Vulnerabilities – 2 Marks, Example: 01 marks
Definition of Threat:
A threat is any potential event, actor, or action that can exploit a weakness and cause harm
to an information system.
Definition of Vulnerability:
A vulnerability is a weakness or flaw in a system, process, or control that can be exploited
by a threat.
Comparison Between Threats and Vulnerabilities:
Comparison   Threat   Vulnerability
parameter
Meaning   Potential danger   or   attack Weakness   that can be
source   exploited
Nature   External or internal   Internal system flaw
Example   Hacker trying to steal data   Weak access control
Role   Initiates the attack   Enables the attack
Real-World Examples:
 Phishing Attack
 Ransomware Attack
Q7 c What is password aging in security systems, and why is storing past passwords in cleartext   [5]
considered risky?
Mark Distribution:
 Concept of password aging and storing previous passwords – 2.5 mark
 Risk of storing passwords in cleartext – 2.5 marks
Password aging: this makes users modify their passwords at a certain time interval and
systems might retain the old passwords so that they are not re-used. These old passwords
should not however be stored in cleartext in disk as they are insecure. When an intruder
enters the system or password file, it is possible that he will immediately access all the past
passwords. This will enable the attacker to masquerade as users particularly when the users
are likely to use the same or make slight modifications to old-fashioned passwords. Also,
the past passwords are easier to guess because attackers usually have knowledge over the
past passwords, therefore, they will be able to guess the current passwords, as users tend
to adopt familiar patterns to change passwords. Thus, it is dangerous to keep past
passwords in plaintext and one should not do it. Rather, safe practices such as hashing are
to be employed.
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 09c524d5e8d7

- Departments: Computer Engineering
- Programmes: BTech Computer 7002, Integrated Computer 7032, MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/Cyber Security/ANS_Cyber Security(702AI0E004)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Cyber Security
Date: 04 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
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
a. Define CIA triad. A bank provides a mobile application that supports balance inquiry, fund   [5]
transfers, bill payments, and transaction history. Authentication is performed using
biometrics and OTP. Customers expect the service to be accessible at all times, including
during national holidays. Any inconsistency in transaction records may lead to financial
disputes. From the given scenario, identify the confidentiality, integrity, and availability
requirements of the system.
Ans.
Definitions of CIA (Each 1 marks). Scenario answer (2 marks)
CIA Triad Definition:
The CIA Triad is a fundamental concept in information security consisting of three key
principles:
•   Confidentiality – Ensures that sensitive information is accessed only by
authorized users.
•   Integrity – Ensures that data remains accurate, consistent, and unaltered.
•   Availability – Ensures that systems and data are accessible to users whenever
needed.
Application to the Given Banking Scenario:
1. Confidentiality:
The mobile banking app must protect sensitive customer data such as account
details, transaction history, and login credentials. The use of biometric
authentication and OTP ensures that only authorized users can access the account,
preventing unauthorized access.
2. Integrity:
The system must ensure that all transaction records (balance, fund transfers, bill
payments) are accurate and not tampered with. Any inconsistency in records can
lead to financial disputes, so data must remain consistent and reliable at all times.
3. Availability:
The banking application should be available to customers 24/7, including during
********** 1 **********
--- page 2 ---
national holidays. Users expect uninterrupted access to services like balance
inquiry and fund transfers, so system downtime must be minimized.
b. Explain the additive cipher and encrypt the plaintext “ROCKSTAR” with the key value =   [5]
12.
Ans:
Definition: (1 Marks)
The additive cipher is a simple substitution cipher where each letter in the plaintext is
shifted a fixed number of positions down the alphabet. This fixed number is the key.
• Encryption Process:
o Assign numerical values to letters (A=0, B=1, ..., Z=25).
o For each letter in the plaintext, add the key value (k) to its numerical
value.
o Take the result modulo 26 (to wrap around the alphabet).
o Convert the resulting numerical value back to a letter.
• Formula: Ciphertext (C) = (Plaintext (P) + Key (k)) mod 26
Encryption of "ROCKSTAR" with Key = 12: (3 Marks)
1. Convert to Numbers:
o R = 17, O = 14, C = 2, K = 10, S = 18, T = 19, A = 0, R = 17
2. Apply the Cipher (Add 12, mod 26):
o R (17) + 12 = 29 mod 26 = 3 (D)
o O (14) + 12 = 26 mod 26 = 0 (A)
o C (2) + 12 = 14 mod 26 = 14 (O)
o K (10) + 12 = 22 mod 26 = 22 (W)
o S (18) + 12 = 30 mod 26 = 4 (E)
o T (19) + 12 = 31 mod 26 = 5 (F)
o A (0) + 12 = 12 mod 26 = 12 (M)
3. Ciphertext: (1 Mark)
o "DAOWEFMD"
c. What are biometrics and how does biometric authentication work with suitable diagram?   [5]
Marks Distribution:
1 mark for definition of biometrics
2 marks for explaining biometric authentication process
2 marks for diagram
Answer:
Biometrics refers to the automated examination of biological or behavioral traits of a
human being with the aim of identifying them. It is premised on distinct physical or
behavioral characteristics of people.
In Biometric authentication, biometric information like fingerprint or voice pattern of the
user is stored in the system upon registration. When the user is logging in, the system will
again take the user biometric information and match it with the stored information. In the
event the match falls within an acceptable limit the user is authenticated, otherwise the
access is denied. Fingerprints and voice recognition are two examples of biometric
methods.
Fingerprint recognition is the method of identifying an individual using the distinctive
arrangement of crests and furrows on his or her fingers. Voice recognition is based on the
features of the voice of the individual e.g. tone and pitch to identify a person.
Diagram:
********** 2 **********
--- page 3 ---
d.   Enlist and explain firewall filter characteristics   [5]
Ans.
Listing of any three kind of firewall filter 0.5M and Write any two characteristics for
each one: 1.5 marks for each [0.5 + 4.5]
Packet Filtering:
 The firewall examines incoming and outgoing packets based on predefined rules.
   It checks parameters such as source IP, destination IP, port number, and protocol.
Stateful Inspection
 Tracks the state of active connections.
 Allows packets only if they belong to an established and legitimate session.
Application-Level Filtering
 Monitors and controls traffic based on specific applications or services.
 Can block suspicious application behaviors (e.g., unknown executables,
malware).
Q2 a   Differentiate between DAC and RBAC   [10]
Ans.
Marks Bifurcation: 01marks for one difference
Discretionary Access Control   Role-Based Access Control
Parameter
(DAC)   (RBAC)
Access control mechanism
Access control mechanism
where permissions are assigned
Definition   where the owner of a resource
to roles, and users are assigned
decides who can access it.
roles.
Control   Resource owner controls access System administrator defines
Authority   permissions.   roles and permissions.
Permissions are assigned to
Access   Permissions are assigned directly
roles, then users inherit
Assignment   to users.
permissions through roles.
User → Role → Permission →
Access Structure User → Resource → Permission
Resource
Highly flexible because users   Less flexible but more structured
Flexibility
can grant access to others.   and manageable.
Lower security due to risk of
Higher security because access
Security Level   permission propagation and
is controlled centrally.
misuse.
********** 3 **********
--- page 4 ---
Difficult to manage in large
Highly scalable for large
Scalability   organizations due to many user
enterprises with many users.
permissions.
High administrative overhead as Lower overhead because
Administrative
permissions must be managed   permissions are managed
Effort
individually.   through roles.
Principle of   Easier to enforce by designing
Difficult to enforce consistently.
Least Privilege   appropriate roles.
In an organization, an employee
In a file system, a user shares a
assigned the “Manager” role
Example   file and grants read/write access
automatically receives
to other users.
predefined permissions.
Q2 b   Describe the SYN spoofing attack and explain with the help of a simple diagram.   [10]
Ans.
Marks Bifurcation: 5marks explanation and 5marks diagram
A SYN spoofing attack is a type of Denial of Service (DoS) attack where the attacker
abuses the TCP three-way handshake by sending a large number of SYN (synchronize)
requests with forged (spoofed) IP addresses.
How the Attack Works
1. Attacker Sends Fake SYN Requests
2. Server Responds with SYN-ACK
3. No ACK Comes Back
4. Server Resources Get Exhausted
Diagram:
The diagram illustrates how an attacker performs a SYN spoofing attack by exploiting
the TCP three-way handshake. It involves three main roles:
 Attacker
 Server (victim)
 Spoofed Client (a fake or non-existent IP address)
Q3 a   Encrypt the Message = “CYBER SECURITY” using Key = “DIPLOMAT” using Playfair   [10]
Scheme. Explain the steps involved.
Ans.
Step 1 Key Table construction: [2 Marks]
********** 4 **********
--- page 5 ---
D I/J P L O
M A T B C
E F G H K
N Q R S U
V W X Y Z
Step 2 Apply Playfair Scheme Rules for encryption [7 Marks- 1 marks for each pair]
Pair 1 = (C,Y) = (B,Z)
PAIR 2 = (BE) = (M,H)
PAIR 3 = (R,S) = (S,U)
PAIR 4 = (E,C) = (K,M)
PAIR 5 = (U,R) = (N,S)
PAIR 6 = (I,T) = (P,A)
PAIR 7 = (Y,X) = (Z,Y)
Step 3: Final Ciphertext: [1 mark]
BZMHSUKMNSPAZY
Q3 b   Explain the various types of malware in detail. Compare them based on their methods of   [10]
propagation and their behavioral characteristics.
Ans.
Marks Bifurcation: Introduction to Malware – 1 Mark, Explanation of Types of Malware
– 5 Marks, Comparison Based on Propagation – 2 Marks, Comparison Based on
Behavioral Characteristics – 2 Marks
Introduction to Malware: Malware (malicious software) refers to any program
intentionally developed to damage, infiltrate, disrupt, or gain unauthorized access to
computer systems.
Types of Malware: Virus, Worm, Trojan horse, Ransomware, Spyware, Rootkit, Botnets
Comparison Based on Methods of Propagation:
Malware Type   Propagation Method
Virus   Spreads through file sharing; requires execution by user.
Worm   Self-propagates   across   networks by   exploiting
vulnerabilities.
Trojan horse   Delivered through   social engineering; no   self-
spreading.
Ransomware   Email phishing, malicious links, exploit kits.
Spyware   Installed with bundled software or Trojans.
Rootkit   Installed after gaining admin privileges; often via
Trojans
Botnets   Spread via worms, Trojans, or drive-by downloads.
Q4 a   Answer the following questions with respect to Data Encryption Standard.   [10]
i)   How many rounds are used?
ii)   Is Data Encryption Standard used now-a-days?
iii)   What was the significance of the Data Encryption Standard in the history of
cryptography?
iv)   Are there any known weaknesses in Data Encryption Standard?
v)   Discuss the internal function working used in each round of Data Encryption
Standard.
vi)   How the 64-bit key is converted to 48-bit key as input to the function of each
round?
Ans.
i) How many rounds are used? (1 Mark)
DES uses 16 rounds of encryption.
********** 5 **********
--- page 6 ---
ii) Is Data Encryption Standard considered secure today? (1 Mark)
No, DES is not considered secure today. Its 56-bit key length is too short and can be
easily cracked using modern computing power.
iii) What was the significance of the Data Encryption Standard in the history of
cryptography? (1 Mark)
DES was a landmark in the history of cryptography. It was the first widely adopted
symmetric-key encryption algorithm standardized by the U.S. government (NBS, now
NIST). It played a crucial role in the development and understanding of modern
cryptography and was used for a long time in various applications, including financial
transactions.
iv) Are there any known weaknesses in Data Encryption Standard? (2 Mark)
Yes, there are several known weaknesses:
i)   Short Key Length: The 56-bit key is its primary weakness,
making it susceptible to brute-force attacks.
ii)   Weak S-Boxes: Some researchers have suggested that the S-
boxes were designed with potential backdoors, although this
has never been definitively proven.
iii)   Semi-Weak Keys: There are a few semi-weak keys that can
produce the same ciphertext when used for both encryption
and decryption.
v)   Discuss the internal function working used in each round of Data Encryption
Standard. (2.5 Marks)
Each round in DES involves the following steps: 1. Expansion Permutation (E-Box): The
32-bit right half of the data is expanded to 48 bits using the E-box. 2. Key Mixing: The
48-bit expanded data is XORed with a 48-bit round key. 3. S-Box Substitution: The 48-
bit result is divided into eight 6-bit blocks, each of which is input into a corresponding S-
box. The S-boxes perform a non-linear substitution, reducing the 48 bits back to 32 bits.
4. Permutation (P-Box): The 32-bit output of the S-boxes is permuted using the P-box. 5.
XOR with Left Half: The 32-bit output of the P-box is XORed with the 32-bit left half of
the data. 6. Swap: The left and right halves are swapped for the next round (except for
the last round).
vi) How is the 64-bit key converted to a 48-bit key as input to the function of each
round? (2.5 Marks)
The 64-bit key undergoes the following process:
1. Permuted Choice 1 (PC-1): The 64-bit key has 8 parity bits, which are discarded. The
remaining 56 bits are permuted using PC-1.
2. Key Splitting and Shifting: The 56-bit key is split into two 28-bit halves. Each half is
circularly left-shifted by either 1 or 2 bits, depending on the round.
3. Permuted Choice 2 (PC-2): The 56-bit shifted halves are combined and permuted
using PC-2, resulting in a 48-bit round key. This 48-bit round key is then used in the
round function.
Q4 b   Analyze the concept of a honeypot by examining its purpose in a security architecture.   [10]
Compare different types of honeypots and evaluate how each type contributes differently
to threat detection.
Marks Bifurcation: Introduction to Honeypots – 1 Mark, Purpose of Honeypots in Security
Architecture – 2 Marks, Types of Honeypots (Explanation) – 4 Marks, Comparison &
Evaluation of Honeypots – 3 Marks
Introduction to Honeypots: A honeypot is a deliberately vulnerable system, service, or
network resource designed to attract attackers.
Purpose of Honeypots in Security Architecture:
i. Threat Detection
ii. Attack Analysis
iii. Deception and Diversion
********** 6 **********
--- page 7 ---
iv. Early Warning System
Types of Honeypots:
Low-Interaction Honeypots: 1marks
Simulate only limited services (e.g., SSH banner, fake FTP). Capture basic scanning
attempts, automated malware.
Medium-Interaction Honeypots: 1marks
Provide partial implementation of services. Engage attackers long enough to analyze
tactics.
High-Interaction Honeypots: 1marks
Real operating systems with actual services. Provide the most detailed information about
attacker behavior.
Research Honeypots: 1marks
Used by security researchers to study advanced threats. Capture deep insights into attacker
motives and methodologies.
Comparison & Evaluation of Honeypots:
Type   Data Collected   Risk Level   Use
Low-   Minimal (scans, probes) Very low   Detect basic malware,
Interaction   bots
Medium-   More details   Medium   Analyze   attack
Interaction   techniques
High-   Extensive, deep insights High   Research   APTs,
Interaction   sophisticated attackers
Q5 a   Define risk and explain the need for risk analysis for information security. State and   [10]
explain all the terminologies related to risk analysis.
Marks Bifurcation: Definition of Risk – 1 Mark, Need for Risk Analysis – 3 Marks, Risk
Analysis Terminologies (Explanation) – 6 Marks
Definition of Risk – Risk is the potential for loss, damage, or negative impact to an
organization’s assets due to a threat exploiting a vulnerability.
Need for Risk Analysis:
i. Prioritization of Security Efforts
ii. Optimal Resource Allocation
iii. Compliance and Legal Requirements
iv. Preventing Financial and Reputation Loss
v. Improved Decision-Making
Risk Analysis Terminologies:
i. Asset
ii. Threat
iii. Vulnerability
iv. Likelihood
v. Risk
vi. Risk Assessment
vii. Risk Mitigation
viii. Residual Risk
Q5 b   Explain how an attacker can exploit a buffer overflow vulnerability to gain control over a   [10]
system. Analyze the sequence of events involved in such an attack.
Ans.
Marks Bifurcation: Introduction to Buffer Overflow – 2 Marks, How Attackers Exploit
Buffer Overflow – 4 Marks, Sequence of Events in a Buffer Overflow Attack – 4 Marks
Introduction to Buffer Overflow:
A buffer overflow occurs when a program writes more data into a buffer than it can hold.
This extra data overwrites adjacent memory areas such as return addresses, function
pointers, or control structures. Attackers exploit buffer overflow vulnerabilities to inject
malicious code and execute it, ultimately gaining unauthorized control over a system.
********** 7 **********
--- page 8 ---
How Attackers Exploit a Buffer Overflow:
i. Overwriting Memory Locations
ii. Injecting Malicious Shellcode
iii. Redirecting Program Execution
iv. Gaining System Control
Sequence of Events in a Buffer Overflow Attack:
Step 1: Identifying a Vulnerable Program
Step 2: Crafting Malicious Input
Step 3: Triggering the Overflow
Step 4: Hijacking the Control Flow
Step 5: Execution of Malicious Code
Q6 a   Explain the working of the Kerberos authentication process with a neat diagram.   [10]
Marks Bifurcation: 5m diagram, 5m explanation
Explanation:
Kerberos is a network authentication protocol that uses symmetric-key cryptography and
a trusted third party called the Key Distribution Center (KDC). The KDC consists of two
main components: Authentication Server (AS) and Ticket Granting Server (TGS)
Step-by-Step Working of Kerberos:
1. User Login & Request to Authentication Server (AS)
2. Authentication Server Verifies User & Issues TGT
3. Client Requests Service Ticket from TGS
4. TGS Verifies Ticket & Authenticator, Issues Service Ticket
5. Client Requests Access from Service Server
6. Service Server Validates & Grants Access
Diagram:
Q6 b   Mention and explain the steps for risk analysis and management   [10]
Ans.
********** 8 **********
--- page 9 ---
Marks Bifurcation: Introduction to Risk Analysis & Management – 2 Marks, Steps in
Risk Analysis – 4 Marks, Steps in Risk Management – 4 Marks
Introduction to Risk Analysis & Management:
Risk analysis and management is a systematic process used to identify, evaluate, and
treat risks that can impact information assets.
Steps in Risk Analysis:
Step 1: Asset Identification
Step 2: Threat Identification
Step 3: Vulnerability Assessment
Step 4: Risk Assessment
Steps in Risk Management:
Step 1: Risk Evaluation & Prioritization
Step 2: Risk Treatment (Mitigation Strategies)
Step 3: Implementation of Controls
Step 4: Monitoring & Review
Q7 a   Explain the digital signature working and its advantages. Discuss how RSA digital   [10]
signature can be used for ensuring authentication using block diagram?
Ans
Digital Signature Process: (3 Marks)
1. Hashing:
o The sender generates a unique fixed-size hash (digest) of the message
using a cryptographic hash function (e.g., SHA-256).
o The hash represents the message's content.
2. Signing:
o The sender encrypts the hash using their private key.
o This encrypted hash is the digital signature.
3. Appending:
o The sender appends the digital signature to the message.
4. Verification:
o The receiver receives the message and the digital signature.
o The receiver generates a hash of the received message using the same
hash function.
o The receiver decrypts the digital signature using the sender's public key.
o The receiver compares the generated hash with the decrypted signature.
o   If the hashes match, the signature is valid, and the message is authentic.
Benefits of Digital Signatures: (2 Marks)
•   Authentication: Verifies the sender's identity.
•   Integrity: Ensures the message has not been altered.
•   Non-repudiation: Prevents the sender from denying sending the message.
Block Diagram: (2 Marks)
Explanation: (3 Marks)
1. Sender (A) Side:
o Sender (A) creates a message (M).
o Sender (A) generates a hash (H) of the message using a hash function.
o Sender (A) encrypts the hash (H) using their private key (dA) to create the
digital signature (S).
********** 9 **********
--- page 10 ---
o Sender (A) sends the message (M) and the digital signature (S) to
Receiver (B).
2. Receiver (B) Side:
o Receiver (B) receives the message (M) and the digital signature (S).
o Receiver (B) generates a hash (H') of the received message (M) using the
same hash function.
o Receiver (B) decrypts the digital signature (S) using Sender (A)'s public
key (eA).
o Receiver (B) compares the generated hash (H') with the decrypted
signature (S).
If H' and S are identical, the signature is valid, and the message is authenticated.
Q7 b   Apply your understanding of cybersecurity concepts to compare threats and vulnerabilities   [5]
with suitable real-world examples.
Ans.
Marks Bifurcation: Definition of Threat – 1 Mark, Definition of Vulnerability – 1 Mark,
Comparison Between Threats & Vulnerabilities – 2 Marks, Example: 01 marks
Definition of Threat:
A threat is any potential event, actor, or action that can exploit a weakness and cause harm
to an information system.
Definition of Vulnerability:
A vulnerability is a weakness or flaw in a system, process, or control that can be exploited
by a threat.
Comparison Between Threats and Vulnerabilities:
Comparison   Threat   Vulnerability
parameter
Meaning   Potential danger   or   attack Weakness   that can be
source   exploited
Nature   External or internal   Internal system flaw
Example   Hacker trying to steal data   Weak access control
Role   Initiates the attack   Enables the attack
Real-World Examples:
 Phishing Attack
 Ransomware Attack
Q7 c What is password aging in security systems, and why is storing past passwords in cleartext   [5]
considered risky?
Mark Distribution:
 Concept of password aging and storing previous passwords – 2.5 mark
 Risk of storing passwords in cleartext – 2.5 marks
Password aging: this makes users modify their passwords at a certain time interval and
systems might retain the old passwords so that they are not re-used. These old passwords
should not however be stored in cleartext in disk as they are insecure. When an intruder
enters the system or password file, it is possible that he will immediately access all the past
passwords. This will enable the attacker to masquerade as users particularly when the users
are likely to use the same or make slight modifications to old-fashioned passwords. Also,
the past passwords are easier to guess because attackers usually have knowledge over the
past passwords, therefore, they will be able to guess the current passwords, as users tend
to adopt familiar patterns to change passwords. Thus, it is dangerous to keep past
passwords in plaintext and one should not do it. Rather, safe practices such as hashing are
to be employed.
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 316630adeb7f

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/Cyber Security/ANS_Cyber Security(702AI0E004)_2025-2026_316630adeb.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Cyber Security
Date: 04 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
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
a. Define CIA triad. A bank provides a mobile application that supports balance inquiry, fund   [5]
transfers, bill payments, and transaction history. Authentication is performed using
biometrics and OTP. Customers expect the service to be accessible at all times, including
during national holidays. Any inconsistency in transaction records may lead to financial
disputes. From the given scenario, identify the confidentiality, integrity, and availability
requirements of the system.
Ans.
Definitions of CIA (Each 1 marks). Scenario answer (2 marks)
CIA Triad Definition:
The CIA Triad is a fundamental concept in information security consisting of three key
principles:
•   Confidentiality – Ensures that sensitive information is accessed only by
authorized users.
•   Integrity – Ensures that data remains accurate, consistent, and unaltered.
•   Availability – Ensures that systems and data are accessible to users whenever
needed.
Application to the Given Banking Scenario:
1. Confidentiality:
The mobile banking app must protect sensitive customer data such as account
details, transaction history, and login credentials. The use of biometric
authentication and OTP ensures that only authorized users can access the account,
preventing unauthorized access.
2. Integrity:
The system must ensure that all transaction records (balance, fund transfers, bill
payments) are accurate and not tampered with. Any inconsistency in records can
lead to financial disputes, so data must remain consistent and reliable at all times.
3. Availability:
The banking application should be available to customers 24/7, including during
********** 1 **********
--- page 2 ---
national holidays. Users expect uninterrupted access to services like balance
inquiry and fund transfers, so system downtime must be minimized.
b. Explain the additive cipher and encrypt the plaintext “ROCKSTAR” with the key value =   [5]
12.
Ans:
Definition: (1 Marks)
The additive cipher is a simple substitution cipher where each letter in the plaintext is
shifted a fixed number of positions down the alphabet. This fixed number is the key.
• Encryption Process:
o Assign numerical values to letters (A=0, B=1, ..., Z=25).
o For each letter in the plaintext, add the key value (k) to its numerical
value.
o Take the result modulo 26 (to wrap around the alphabet).
o Convert the resulting numerical value back to a letter.
• Formula: Ciphertext (C) = (Plaintext (P) + Key (k)) mod 26
Encryption of "ROCKSTAR" with Key = 12: (3 Marks)
1. Convert to Numbers:
o R = 17, O = 14, C = 2, K = 10, S = 18, T = 19, A = 0, R = 17
2. Apply the Cipher (Add 12, mod 26):
o R (17) + 12 = 29 mod 26 = 3 (D)
o O (14) + 12 = 26 mod 26 = 0 (A)
o C (2) + 12 = 14 mod 26 = 14 (O)
o K (10) + 12 = 22 mod 26 = 22 (W)
o S (18) + 12 = 30 mod 26 = 4 (E)
o T (19) + 12 = 31 mod 26 = 5 (F)
o A (0) + 12 = 12 mod 26 = 12 (M)
3. Ciphertext: (1 Mark)
o "DAOWEFMD"
c. What are biometrics and how does biometric authentication work with suitable diagram?   [5]
Marks Distribution:
1 mark for definition of biometrics
2 marks for explaining biometric authentication process
2 marks for diagram
Answer:
Biometrics refers to the automated examination of biological or behavioral traits of a
human being with the aim of identifying them. It is premised on distinct physical or
behavioral characteristics of people.
In Biometric authentication, biometric information like fingerprint or voice pattern of the
user is stored in the system upon registration. When the user is logging in, the system will
again take the user biometric information and match it with the stored information. In the
event the match falls within an acceptable limit the user is authenticated, otherwise the
access is denied. Fingerprints and voice recognition are two examples of biometric
methods.
Fingerprint recognition is the method of identifying an individual using the distinctive
arrangement of crests and furrows on his or her fingers. Voice recognition is based on the
features of the voice of the individual e.g. tone and pitch to identify a person.
Diagram:
********** 2 **********
--- page 3 ---
d.   Enlist and explain firewall filter characteristics   [5]
Ans.
Listing of any three kind of firewall filter 0.5M and Write any two characteristics for
each one: 1.5 marks for each [0.5 + 4.5]
Packet Filtering:
 The firewall examines incoming and outgoing packets based on predefined rules.
   It checks parameters such as source IP, destination IP, port number, and protocol.
Stateful Inspection
 Tracks the state of active connections.
 Allows packets only if they belong to an established and legitimate session.
Application-Level Filtering
 Monitors and controls traffic based on specific applications or services.
 Can block suspicious application behaviors (e.g., unknown executables,
malware).
Q2 a   Differentiate between DAC and RBAC   [10]
Ans.
Marks Bifurcation: 01marks for one difference
Discretionary Access Control   Role-Based Access Control
Parameter
(DAC)   (RBAC)
Access control mechanism
Access control mechanism
where permissions are assigned
Definition   where the owner of a resource
to roles, and users are assigned
decides who can access it.
roles.
Control   Resource owner controls access System administrator defines
Authority   permissions.   roles and permissions.
Permissions are assigned to
Access   Permissions are assigned directly
roles, then users inherit
Assignment   to users.
permissions through roles.
User → Role → Permission →
Access Structure User → Resource → Permission
Resource
Highly flexible because users   Less flexible but more structured
Flexibility
can grant access to others.   and manageable.
Lower security due to risk of
Higher security because access
Security Level   permission propagation and
is controlled centrally.
misuse.
********** 3 **********
--- page 4 ---
Difficult to manage in large
Highly scalable for large
Scalability   organizations due to many user
enterprises with many users.
permissions.
High administrative overhead as Lower overhead because
Administrative
permissions must be managed   permissions are managed
Effort
individually.   through roles.
Principle of   Easier to enforce by designing
Difficult to enforce consistently.
Least Privilege   appropriate roles.
In an organization, an employee
In a file system, a user shares a
assigned the “Manager” role
Example   file and grants read/write access
automatically receives
to other users.
predefined permissions.
Q2 b   Describe the SYN spoofing attack and explain with the help of a simple diagram.   [10]
Ans.
Marks Bifurcation: 5marks explanation and 5marks diagram
A SYN spoofing attack is a type of Denial of Service (DoS) attack where the attacker
abuses the TCP three-way handshake by sending a large number of SYN (synchronize)
requests with forged (spoofed) IP addresses.
How the Attack Works
1. Attacker Sends Fake SYN Requests
2. Server Responds with SYN-ACK
3. No ACK Comes Back
4. Server Resources Get Exhausted
Diagram:
The diagram illustrates how an attacker performs a SYN spoofing attack by exploiting
the TCP three-way handshake. It involves three main roles:
 Attacker
 Server (victim)
 Spoofed Client (a fake or non-existent IP address)
Q3 a   Encrypt the Message = “CYBER SECURITY” using Key = “DIPLOMAT” using Playfair   [10]
Scheme. Explain the steps involved.
Ans.
Step 1 Key Table construction: [2 Marks]
********** 4 **********
--- page 5 ---
D I/J P L O
M A T B C
E F G H K
N Q R S U
V W X Y Z
Step 2 Apply Playfair Scheme Rules for encryption [7 Marks- 1 marks for each pair]
Pair 1 = (C,Y) = (B,Z)
PAIR 2 = (BE) = (M,H)
PAIR 3 = (R,S) = (S,U)
PAIR 4 = (E,C) = (K,M)
PAIR 5 = (U,R) = (N,S)
PAIR 6 = (I,T) = (P,A)
PAIR 7 = (Y,X) = (Z,Y)
Step 3: Final Ciphertext: [1 mark]
BZMHSUKMNSPAZY
Q3 b   Explain the various types of malware in detail. Compare them based on their methods of   [10]
propagation and their behavioral characteristics.
Ans.
Marks Bifurcation: Introduction to Malware – 1 Mark, Explanation of Types of Malware
– 5 Marks, Comparison Based on Propagation – 2 Marks, Comparison Based on
Behavioral Characteristics – 2 Marks
Introduction to Malware: Malware (malicious software) refers to any program
intentionally developed to damage, infiltrate, disrupt, or gain unauthorized access to
computer systems.
Types of Malware: Virus, Worm, Trojan horse, Ransomware, Spyware, Rootkit, Botnets
Comparison Based on Methods of Propagation:
Malware Type   Propagation Method
Virus   Spreads through file sharing; requires execution by user.
Worm   Self-propagates   across   networks by   exploiting
vulnerabilities.
Trojan horse   Delivered through   social engineering; no   self-
spreading.
Ransomware   Email phishing, malicious links, exploit kits.
Spyware   Installed with bundled software or Trojans.
Rootkit   Installed after gaining admin privileges; often via
Trojans
Botnets   Spread via worms, Trojans, or drive-by downloads.
Q4 a   Answer the following questions with respect to Data Encryption Standard.   [10]
i)   How many rounds are used?
ii)   Is Data Encryption Standard used now-a-days?
iii)   What was the significance of the Data Encryption Standard in the history of
cryptography?
iv)   Are there any known weaknesses in Data Encryption Standard?
v)   Discuss the internal function working used in each round of Data Encryption
Standard.
vi)   How the 64-bit key is converted to 48-bit key as input to the function of each
round?
Ans.
i) How many rounds are used? (1 Mark)
DES uses 16 rounds of encryption.
********** 5 **********
--- page 6 ---
ii) Is Data Encryption Standard considered secure today? (1 Mark)
No, DES is not considered secure today. Its 56-bit key length is too short and can be
easily cracked using modern computing power.
iii) What was the significance of the Data Encryption Standard in the history of
cryptography? (1 Mark)
DES was a landmark in the history of cryptography. It was the first widely adopted
symmetric-key encryption algorithm standardized by the U.S. government (NBS, now
NIST). It played a crucial role in the development and understanding of modern
cryptography and was used for a long time in various applications, including financial
transactions.
iv) Are there any known weaknesses in Data Encryption Standard? (2 Mark)
Yes, there are several known weaknesses:
i)   Short Key Length: The 56-bit key is its primary weakness,
making it susceptible to brute-force attacks.
ii)   Weak S-Boxes: Some researchers have suggested that the S-
boxes were designed with potential backdoors, although this
has never been definitively proven.
iii)   Semi-Weak Keys: There are a few semi-weak keys that can
produce the same ciphertext when used for both encryption
and decryption.
v)   Discuss the internal function working used in each round of Data Encryption
Standard. (2.5 Marks)
Each round in DES involves the following steps: 1. Expansion Permutation (E-Box): The
32-bit right half of the data is expanded to 48 bits using the E-box. 2. Key Mixing: The
48-bit expanded data is XORed with a 48-bit round key. 3. S-Box Substitution: The 48-
bit result is divided into eight 6-bit blocks, each of which is input into a corresponding S-
box. The S-boxes perform a non-linear substitution, reducing the 48 bits back to 32 bits.
4. Permutation (P-Box): The 32-bit output of the S-boxes is permuted using the P-box. 5.
XOR with Left Half: The 32-bit output of the P-box is XORed with the 32-bit left half of
the data. 6. Swap: The left and right halves are swapped for the next round (except for
the last round).
vi) How is the 64-bit key converted to a 48-bit key as input to the function of each
round? (2.5 Marks)
The 64-bit key undergoes the following process:
1. Permuted Choice 1 (PC-1): The 64-bit key has 8 parity bits, which are discarded. The
remaining 56 bits are permuted using PC-1.
2. Key Splitting and Shifting: The 56-bit key is split into two 28-bit halves. Each half is
circularly left-shifted by either 1 or 2 bits, depending on the round.
3. Permuted Choice 2 (PC-2): The 56-bit shifted halves are combined and permuted
using PC-2, resulting in a 48-bit round key. This 48-bit round key is then used in the
round function.
Q4 b   Analyze the concept of a honeypot by examining its purpose in a security architecture.   [10]
Compare different types of honeypots and evaluate how each type contributes differently
to threat detection.
Marks Bifurcation: Introduction to Honeypots – 1 Mark, Purpose of Honeypots in Security
Architecture – 2 Marks, Types of Honeypots (Explanation) – 4 Marks, Comparison &
Evaluation of Honeypots – 3 Marks
Introduction to Honeypots: A honeypot is a deliberately vulnerable system, service, or
network resource designed to attract attackers.
Purpose of Honeypots in Security Architecture:
i. Threat Detection
ii. Attack Analysis
iii. Deception and Diversion
********** 6 **********
--- page 7 ---
iv. Early Warning System
Types of Honeypots:
Low-Interaction Honeypots: 1marks
Simulate only limited services (e.g., SSH banner, fake FTP). Capture basic scanning
attempts, automated malware.
Medium-Interaction Honeypots: 1marks
Provide partial implementation of services. Engage attackers long enough to analyze
tactics.
High-Interaction Honeypots: 1marks
Real operating systems with actual services. Provide the most detailed information about
attacker behavior.
Research Honeypots: 1marks
Used by security researchers to study advanced threats. Capture deep insights into attacker
motives and methodologies.
Comparison & Evaluation of Honeypots:
Type   Data Collected   Risk Level   Use
Low-   Minimal (scans, probes) Very low   Detect basic malware,
Interaction   bots
Medium-   More details   Medium   Analyze   attack
Interaction   techniques
High-   Extensive, deep insights High   Research   APTs,
Interaction   sophisticated attackers
Q5 a   Define risk and explain the need for risk analysis for information security. State and   [10]
explain all the terminologies related to risk analysis.
Marks Bifurcation: Definition of Risk – 1 Mark, Need for Risk Analysis – 3 Marks, Risk
Analysis Terminologies (Explanation) – 6 Marks
Definition of Risk – Risk is the potential for loss, damage, or negative impact to an
organization’s assets due to a threat exploiting a vulnerability.
Need for Risk Analysis:
i. Prioritization of Security Efforts
ii. Optimal Resource Allocation
iii. Compliance and Legal Requirements
iv. Preventing Financial and Reputation Loss
v. Improved Decision-Making
Risk Analysis Terminologies:
i. Asset
ii. Threat
iii. Vulnerability
iv. Likelihood
v. Risk
vi. Risk Assessment
vii. Risk Mitigation
viii. Residual Risk
Q5 b   Explain how an attacker can exploit a buffer overflow vulnerability to gain control over a   [10]
system. Analyze the sequence of events involved in such an attack.
Ans.
Marks Bifurcation: Introduction to Buffer Overflow – 2 Marks, How Attackers Exploit
Buffer Overflow – 4 Marks, Sequence of Events in a Buffer Overflow Attack – 4 Marks
Introduction to Buffer Overflow:
A buffer overflow occurs when a program writes more data into a buffer than it can hold.
This extra data overwrites adjacent memory areas such as return addresses, function
pointers, or control structures. Attackers exploit buffer overflow vulnerabilities to inject
malicious code and execute it, ultimately gaining unauthorized control over a system.
********** 7 **********
--- page 8 ---
How Attackers Exploit a Buffer Overflow:
i. Overwriting Memory Locations
ii. Injecting Malicious Shellcode
iii. Redirecting Program Execution
iv. Gaining System Control
Sequence of Events in a Buffer Overflow Attack:
Step 1: Identifying a Vulnerable Program
Step 2: Crafting Malicious Input
Step 3: Triggering the Overflow
Step 4: Hijacking the Control Flow
Step 5: Execution of Malicious Code
Q6 a   Explain the working of the Kerberos authentication process with a neat diagram.   [10]
Marks Bifurcation: 5m diagram, 5m explanation
Explanation:
Kerberos is a network authentication protocol that uses symmetric-key cryptography and
a trusted third party called the Key Distribution Center (KDC). The KDC consists of two
main components: Authentication Server (AS) and Ticket Granting Server (TGS)
Step-by-Step Working of Kerberos:
1. User Login & Request to Authentication Server (AS)
2. Authentication Server Verifies User & Issues TGT
3. Client Requests Service Ticket from TGS
4. TGS Verifies Ticket & Authenticator, Issues Service Ticket
5. Client Requests Access from Service Server
6. Service Server Validates & Grants Access
Diagram:
Q6 b   Mention and explain the steps for risk analysis and management   [10]
Ans.
********** 8 **********
--- page 9 ---
Marks Bifurcation: Introduction to Risk Analysis & Management – 2 Marks, Steps in
Risk Analysis – 4 Marks, Steps in Risk Management – 4 Marks
Introduction to Risk Analysis & Management:
Risk analysis and management is a systematic process used to identify, evaluate, and
treat risks that can impact information assets.
Steps in Risk Analysis:
Step 1: Asset Identification
Step 2: Threat Identification
Step 3: Vulnerability Assessment
Step 4: Risk Assessment
Steps in Risk Management:
Step 1: Risk Evaluation & Prioritization
Step 2: Risk Treatment (Mitigation Strategies)
Step 3: Implementation of Controls
Step 4: Monitoring & Review
Q7 a   Explain the digital signature working and its advantages. Discuss how RSA digital   [10]
signature can be used for ensuring authentication using block diagram?
Ans
Digital Signature Process: (3 Marks)
1. Hashing:
o The sender generates a unique fixed-size hash (digest) of the message
using a cryptographic hash function (e.g., SHA-256).
o The hash represents the message's content.
2. Signing:
o The sender encrypts the hash using their private key.
o This encrypted hash is the digital signature.
3. Appending:
o The sender appends the digital signature to the message.
4. Verification:
o The receiver receives the message and the digital signature.
o The receiver generates a hash of the received message using the same
hash function.
o The receiver decrypts the digital signature using the sender's public key.
o The receiver compares the generated hash with the decrypted signature.
o   If the hashes match, the signature is valid, and the message is authentic.
Benefits of Digital Signatures: (2 Marks)
•   Authentication: Verifies the sender's identity.
•   Integrity: Ensures the message has not been altered.
•   Non-repudiation: Prevents the sender from denying sending the message.
Block Diagram: (2 Marks)
Explanation: (3 Marks)
1. Sender (A) Side:
o Sender (A) creates a message (M).
o Sender (A) generates a hash (H) of the message using a hash function.
o Sender (A) encrypts the hash (H) using their private key (dA) to create the
digital signature (S).
********** 9 **********
--- page 10 ---
o Sender (A) sends the message (M) and the digital signature (S) to
Receiver (B).
2. Receiver (B) Side:
o Receiver (B) receives the message (M) and the digital signature (S).
o Receiver (B) generates a hash (H') of the received message (M) using the
same hash function.
o Receiver (B) decrypts the digital signature (S) using Sender (A)'s public
key (eA).
o Receiver (B) compares the generated hash (H') with the decrypted
signature (S).
If H' and S are identical, the signature is valid, and the message is authenticated.
Q7 b   Apply your understanding of cybersecurity concepts to compare threats and vulnerabilities   [5]
with suitable real-world examples.
Ans.
Marks Bifurcation: Definition of Threat – 1 Mark, Definition of Vulnerability – 1 Mark,
Comparison Between Threats & Vulnerabilities – 2 Marks, Example: 01 marks
Definition of Threat:
A threat is any potential event, actor, or action that can exploit a weakness and cause harm
to an information system.
Definition of Vulnerability:
A vulnerability is a weakness or flaw in a system, process, or control that can be exploited
by a threat.
Comparison Between Threats and Vulnerabilities:
Comparison   Threat   Vulnerability
parameter
Meaning   Potential danger   or   attack Weakness   that can be
source   exploited
Nature   External or internal   Internal system flaw
Example   Hacker trying to steal data   Weak access control
Role   Initiates the attack   Enables the attack
Real-World Examples:
 Phishing Attack
 Ransomware Attack
Q7 c What is password aging in security systems, and why is storing past passwords in cleartext   [5]
considered risky?
Mark Distribution:
 Concept of password aging and storing previous passwords – 2.5 mark
 Risk of storing passwords in cleartext – 2.5 marks
Password aging: this makes users modify their passwords at a certain time interval and
systems might retain the old passwords so that they are not re-used. These old passwords
should not however be stored in cleartext in disk as they are insecure. When an intruder
enters the system or password file, it is possible that he will immediately access all the past
passwords. This will enable the attacker to masquerade as users particularly when the users
are likely to use the same or make slight modifications to old-fashioned passwords. Also,
the past passwords are easier to guess because attackers usually have knowledge over the
past passwords, therefore, they will be able to guess the current passwords, as users tend
to adopt familiar patterns to change passwords. Thus, it is dangerous to keep past
passwords in plaintext and one should not do it. Rather, safe practices such as hashing are
to be employed.
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 33e660779bb6

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Cyber Security/ANS_Cyber Security(703AI0C005)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: text (6 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Cyber Security
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory. Out of remaining questions, attempt any 4 questions.
5. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
a.   What are different types of security threats? Explain with the help of suitable   [5]
examples.
threats-4m
examples-1 mark
b.   Discuss importance and working of Challenge-Response Protocols   [5]
Importance-2M
Working-3M
c.   Discuss Tunnel mode of VPN. Compare it with Transport mode VPN.   [5]
Tunnel mode explanation -3m
Comparison-2m
d.   What are software Risks? Discuss strategies for dealing with risk.   [5]
Risk-2M
Strategies-3M
strategies for dealing with risk:
1. avoiding the risk, by changing requirements for security or other system
characteristics
2. transferring the risk, by allocating the risk to other systems, people,
organizations, or assets; or by buying insurance to cover any financial loss should
the risk become a reality
3. assuming the risk, by accepting it, controlling it with available resources, and
preparing to deal with the loss if it occurs
Q2
a.   Explain different types of attacks. Consider a cloud storage service that stores   [10]
sensitive business documents. Who might try to breach this system? What potential
harm could they cause? Which vulnerabilities might they take advantage of to
succeed in their attack?
Types of attacks- 4m
********** 1 **********
--- page 2 ---
Potential attackers: 2m
Cybercriminals, competitors, disgruntled employees, hacktivists.
Intended harm: 2m
Data theft, reputational damage, financial loss, service disruption.
Possible vulnerabilities: 2m
Weak access controls, misconfigured cloud settings, insecure APIs, phishing-
induced credential leaks.
b.   What are substitution ciphers? Explain any four types of substitution ciphers with   [10]
suitable examples.
substitution ciphers -2m
2m per type
Q3
a.   Write the steps of RSA algorithm and use them to encrypt the message value   [10]
‘15’. Consider P=3 and Q=11; Assume suitable values for E and D.
Steps of the RSA Algorithm [5 Marks]
1. Key Generation:
o Choose two large prime numbers p and q.
o Compute n=p×q, which forms part of the public and private key
pair.
o Compute ϕ(n)=(p−1)×(q−1) (Euler's totient function).
o Choose a public exponent e, such that 1<e<ϕ(n) and gcd(e,
ϕ(n))=1.
o Compute the private key d, the modular inverse of e mod ϕ(n).
This means solving d×e≡1 mod ϕ(n) using the Extended
Euclidean Algorithm.
o The public key is (e, n) and the private key is (d, n).
2. Encryption:
o The sender takes the plaintext message M and computes the
ciphertext C using the recipient's public key (e, n):
C ≡ Me mod n
o The ciphertext C is sent to the recipient.
3. Decryption:
o The recipient uses their private key (d, n) to decrypt the
ciphertext C back into plaintext M:
M ≡ Cd mod n
Computation of E and D : 3 marks
********** 2 **********
--- page 3 ---
Encryption of message : 2 marks
b.   How biometric authentication is better than other authentication methods? Discuss   [10]
various biometric features with applications used for authentication.
biometric authentication is better-3m
Features with applications-7m
Q4
a.   Summarize the steps in DES algorithm. Compare it with AES algorithm.   [10]
DES steps-6 m
 Step 1: Apply an initial permutation on a block.
********** 3 **********
--- page 4 ---
 Result is B=IP(P) where P is the 64 bit block IP Initial Permutation
function and B the result.
   Step 2: Split B into 32 bit blocks
   Li = leftmost 32 bits
Ri = rightmost 32 bits.
   Step 3: Pick a 56 bit key. Permute it
   Step 4: Left circular shift it by 1 bit giving K1.
 Step 5: Perform a complex sequence of operations and obtain
 X1 = F(R1,K1) (The complex set of operations include table look up
and dropping bits).
 Step 6: Find R2 = L1 + X1
 Step 7: Set L2 = R1
 Repeat steps 2 to 7 , 16 times to get B16 = L16,R16
 Step 8: Apply inverse of initial permutation on B16
 The result is the encrypted block
Comparison-4m
DES   AES
Date   1976   1999
Block size   64 bits   128 bits
Key length   56 bits   128, 192, 256 bits
Encryptio   Substitution,   Substitution, shift, bit
n   permutation   mixing
primitives
Cryptogra   Confusion,   Confusion, diffusion
phic   diffusion
primitives
Design   Open   Open
Design   Closed   Open
rationale
Selection   Secret   Secret, but accepted
process   open public comment
Source   IBM, enhanced by   Independent Dutch
NSA   cryptographers
b.   Explain Access Control Lists with suitable example. Compare them with Access   [10]
Control Matrices.
ACL-6m
Comparison-4m
Q5
a.   How viruses gain control? Explain different types of Viruses with their working   [10]
mechanisms.
 One time execution
 Boot sector viruses
 Memory resident viruses
 Document viruses
How viruses gain control-3m
types of Viruses-7m
b.   Explain End-to-End Encryption with the help of neat diagram and compare it   [10]
with Link Encryption.
********** 4 **********
--- page 5 ---
End-to-end encryption with diagram-5m
Comparison-5m
End-to-End Encryption
 provides security from one end of a transmission to the other
 Can be done by hardware or software
 performed at the highest network levels (layer 7, application, or
perhaps at layer 6, presentation) of the OSI model
Q6
a.   What are Application Proxy firewalls? Compare them with Stateful inspection   [10]
firewalls and Packet filtering firewalls.
Application Proxy Firewalls-3m
comparison-7m
b. A large urban hospital preparing for a pandemic situation, such as COVID-19.   [10]
Summarize the steps involved in Risk Analysis for it.
6m- steps
Steps of a Risk Analysis
1. Identify assets.
2. Determine vulnerabilities.
3. Estimate likelihood of exploitation.
4. Compute expected annual loss.
5. Survey applicable controls and their costs.
6. Project annual savings of control
4m – examples/solutions for given scenario
********** 5 **********
--- page 6 ---
Risk analysis would identify vulnerabilities related to staff shortages, equipment
scarcity, disruptions in care, and supply chain issues, allowing the hospital to
prioritize resource allocation and contingency plans accordingly to maintain
patient safety and operational continuity.
Q7
a.   Discuss design goals of Kerberos systems. Give all the steps involved in   [10]
authentication mechanism of Kerberos.
Goals- 3m
No passwords are communicated on the network.
Provides cryptographic protection against spoofing.
Limited period of validity (of tickets)
Mutual authentication
Steps-7m
b.   Why Digital signatures are important? Discuss the process for creating and   [10]
verifying Digital Signatures. How are they different from Digital certificates?
Importance-2m
Process-6m
Comparison-2m
********** 6 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 32cd0e68c7b4

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_Computer_7002/Cyber Security/ANS_Cyber Security(702AI0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Cyber Security
Date: 30 Jun 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
a. What are passive attacks and active attacks in cybersecurity? Give a simple   [5]
definition and one basic example of each.
Ans.
Marks Bifurcation:
Definition of Passive Attack – 1 mark
Example of Passive Attack – 1 mark
Definition of Active Attack – 1 mark
Example of Active Attack – 1 mark
Any one key difference – 1 mark
Definition of Passive Attack –
A passive attack is an attack where the attacker only monitors or intercepts data
without altering it.
Example: Eavesdropping
Active Attack: An active attack is an attack where the attacker modifies, disrupts,
or injects data into the communication.
Example: Man-in-the-middle (MITM) attack
Key Difference: Key Difference
b.   Apply your understanding of public key cryptography to describe how a public key   [5]
cryptosystem works. Use a block diagram to illustrate the encryption and decryption
processes, and explain the role of each component.
Ans.
Marks Bifurcation:
Concept of Public Key Cryptography – 1 mark
Encryption Process Description – 1 mark
Decryption Process Description – 1 mark
Block Diagram – 1 mark
Role of Components – 1 mark
Concept of Public Key Cryptography –
Public key cryptography uses two keys: public key and private key.
Encryption Process Description –
********** 1 **********
--- page 2 ---
Sender takes the plaintext. Applies the encryption algorithm using the receiver’s
public key. Produces ciphertext that is securely transmitted.
Decryption Process Description –
Receiver takes the ciphertext. Uses the decryption algorithm with their private key.
Recovers the original plaintext.
Block Diagram –
Role of Components –
Public Key: Used by anyone to encrypt data for the receiver.
Private Key: Only known to receiver; decrypts messages encrypted with the
matching public key.
Encryption Algorithm: Converts plaintext → ciphertext.
Decryption Algorithm: Converts ciphertext → plaintext.
Diagram:
c.   Explain the meaning of the keystroke dynamics in biometric authentication. Write   [5]
any two distinctions between the dynamic and the static keystroke recognition. And
one benefit of this approach, as well.
Ans.
Marks Bifurcation:
2 marks for explaining keystroke dynamics
2 marks for differentiating static and dynamic recognition 1 mark for advantage
Keystroke dynamics is a behavioral biometric method of identifying a user through
his typing pattern. It compares the typing speed, time span between key press,
duration of key press and typing pressure. These trends are deemed to be individual.
In the static keystroke recognition, typing pattern is verified at the time of a single
instance at log-in typically by typing a set password or phrase. Once authentication
is done, there is no further monitoring. In dynamic recognition of keystroke, the
typing behaviour of the user is constantly observed during the session and this
makes it more secure. One of the merits of keystroke dynamics is that, it needs no
special hardware and can be compatible with a normal keyboard.
d.   Describe the capabilities and limitations of a firewall by explaining how it helps   [5]
protect a network and what types of threats or attacks it cannot defend against.
Ans.
Marks Bifurcation:
Definition of Firewall – 1 mark
Capabilities (any two points) – 2 marks
Limitations (any two points) – 2 marks
Definition:
A firewall is a security device or software that monitors and controls incoming and
outgoing network traffic based on predefined security rules
********** 2 **********
--- page 3 ---
Capabilities (any two points) –
Traffic Filtering
Access Control
Packet Inspection
Protects Against External Attacks
Limitations:
Cannot Stop Internal Attacks
Cannot Detect Encrypted Malware
Cannot Block Malware Already Inside
Q2   a.   Assume, a computer system has 4 users: Kate, Alice, Bob, and Mike. Kate owns   [10]
file Katefile, the other three people can only read the file. Mike and Kate can read
and write file Alicefile (owner Alice). Only Bob can read and write the file Bobfile
which he owns. Mike owns the file Mikefile and Bob and Kate can read and write
the file Mikefile. Assume the owner of a file can execute it.
1. Create an access control matrix describing this system.
2. Suppose the owner of a file can add and remove permissions to that file.
Mike removes Kate's permission and give permission to Alice to read and
write Mikefile. Show the new access control matrix.
3. Suppose the commands to add or remove permissions can be written into a
file, then that file is executed with the permissions of its owner. Does this
change what operations are considered trusted? Explain.
Ans.
Marks Bifurcation:
Create an access control matrix describing this system: 04marks
Suppose the owner of a file can add and remove permissions to that file. Mike
removes Kate's permission and give permission to Alice to read and write Mikefile.
Show the new access control matrix: 04marks
Suppose the commands to add or remove permissions can be written into a file, then
that file is executed with the permissions of its owner. Does this change what
operations are considered trusted? Explain.: 04marks
3) if a user (user A) is granted write + execute permissions on a file owned by another user
(user B), then user A gains indirect control permissions on that file (and all other files
owned by user B). This changes the trust level of the write+execute operations
Q2   b.   Explain the concept of a Host-Based Intrusion Detection System with the help of a   [10]
neat diagram, and describe how it works using a simple example.
Ans.
Marks Bifurcation:
********** 3 **********
--- page 4 ---
Definition of HIDS – 2 marks
Diagram – 2 marks
Components of HIDS – 2 marks
Working of HIDS – 2 marks
Simple Example – 2 marks
Definition of HIDS –
A Host-Based Intrusion Detection System (HIDS) is a security tool installed on an
individual host (computer/server) to monitor system activities, detect unauthorized
changes, and identify malicious actions on that specific machine.
Diagram –
Components of HIDS –
Data Collection Module, Analysis Engine, Alert/Reporting System, Policy/Rule Set
Working of HIDS –
• IDS continuously monitors the host’s system files, logs, and processes.
•   It checks for unexpected modifications; such as changes to configuration
files or unauthorized login attempts.
• The analysis engine evaluates the activity using signature-based (known
attacks) or anomaly-based (abnormal behavior) detection.
•   If a threat is detected, the HIDS generates an alert for the administrator.
Simple Example –
An attacker tries to modify the file /etc/passwd on a Linux server.
• HIDS detects that the file’s checksum has changed unexpectedly.
•   It identifies this as suspicious behavior.
Q3   a.   Apply the Hill Cipher encryption process to compute the ciphertext for the message   [10]
‘SECURE HOME’ using the key matrix derived from the key ‘ROCK’. Show the
step-by-step calculation.
Ans.
The key given is “ROCK”, so the key matrix will be   . [2 Mark]
The key given is “ROCK”, so the key matrix will be   . [2 Mark]
Using formula Ciphertext (C) = K * P mod 26.
Pair 1 (18,4): [1 Mark]
mod 26
O/P =(24,24) = (Y,Y).
Similar operation will be performed for each pair.
Pair 2 (2,20): [1 Mark]
O/P=(2,22) = (C,W)
********** 4 **********
--- page 5 ---
Pair 3 (17,4): [1 Mark]
O/P=(7,22)=(H,W)
Pair 4 (7,14): [1 Mark]
O/P=(3,24)=(D,Y)
Pair 5 (12,4): [1 Mark]
O/P = (0,12) = (A,M)
Final Ciphertext: YYCWHWDYAM. [1 Marks]
Q3   b.   Describe in detail any 2 types of non-malicious program errors.   [10]
Ans.
Marks Bifurcation:
Definition of Non-Malicious Program Errors: 02marks
Type 1 Description (Explanation): 04marks
Type 2 Description (Explanation): 04marks
Definition of Non-Malicious Program Errors:
Non-malicious program errors are unintentional software faults or mistakes caused
by design flaws, coding errors, or misconfigurations.
Type 1: Buffer Overflow Error
A buffer overflow occurs when a program writes data beyond the allocated memory
space, causing memory corruption.
How It Happens: Programmer allocates a fixed-size buffer (e.g., 20 bytes). User
inputs more than 20 bytes → extra data overwrites adjacent memory.
Impact: Program crashes or behaves unpredictably. Can unintentionally create a
security vulnerability allowing attackers to inject malicious code. System instability
due to overwritten memory.
Type 2: Incomplete Mediation
Incomplete mediation refers to a situation where a system does not properly check,
validate, or filter user inputs or requests before processing them.
How It Happens: The program receives input from a user or external source. It fails
to check whether the input is valid, safe, within limits, or allowed. The system
processes the invalidated input → leading to incorrect results or security risks.
Impact: Unauthorized access, Data corruption, Application crashes
Q4   a. What the differences between symmetric and public key encryption. Define   [10]
steganography and provide three examples steganography techniques.
Ans.
• Symmetric (Private) encryption: Uses the same key for both encryption and
decryption. Examples: AES, DES. Faster but key distribution is a challenge.
(2.5 mark)
• Asymmetric encryption: Uses two separate keys: a public key for encryption
and a private key for decryption. Example: RSA. Slower but solves the key
distribution problem. (2.5 mark)
• Steganography: The art of concealing a message within another message or
physical object. (2 marks)
•   Techniques: Hiding messages in images, audio files, or video files. (3 mark)
Q4   b.   Analyze the concept of Denial of Service (DoS) by explaining how it disrupts   [10]
system availability. Examine the characteristics of a classic DoS attack and discuss
how its mechanisms overwhelm a target to cause service failure.
Ans.
Marks Bifurcation:
Concept of DoS – 2 marks
********** 5 **********
--- page 6 ---
How DoS disrupts system availability – 2 marks
Characteristics of a classic DoS attack – 3 marks
Mechanisms used to overwhelm the target – 3 marks
Concept of DoS –
A Denial of Service (DoS) attack is a cyberattack that prevents legitimate users
from accessing a service by overwhelming the target system, server, or network
with excessive traffic or resource requests.
How DoS disrupts system availability –
A system has limited resources such as CPU, RAM, network bandwidth, and
connection limits. The attacker sends excessive or malformed requests, causing
resource exhaustion. Legitimate user requests cannot be processed, leading to: Slow
response, System crash and Complete service unavailability.
Characteristics of a classic DoS attack –
• Single Source Attack: Originates from one attacker or one machine.
• Resource Exhaustion: Focuses on consuming server resources such as CPU,
memory, or bandwidth.
• Volume-Based or Logic-Based: Uses heavy traffic (e.g., ICMP flood) or
malformed packets (e.g., Ping of Death).
• No Unauthorized Access Needed: The attacker does not need to breach the
system; only overload it.
Mechanisms used to overwhelm the target –
• Flooding Attacks: The attacker sends an extremely high volume of traffic
(e.g., ICMP flood, UDP flood). The server becomes too busy responding to
requests. Legitimate traffic gets dropped.
• Sending Malformed or Oversized Packets: Packets that violate protocol
rules can cause: Buffer overflow and Buffer overflow.
• Exploiting Protocol Weaknesses: The attacker uses vulnerabilities in
protocols (e.g., TCP three-way handshake). Example: SYN Flood
Q5   a.   Explain Business Impact Analysis (BIA) in detail. Also discuss key terms such as   [10]
Recovery Time Objective (RTO) and Recovery Point Objective (RPO).
Ans.
Definition & Purpose of BIA – 2 marks
Steps/Process of BIA – 4 marks
Recovery Time Objective (RTO) – 2 marks
Recovery Point Objective (RPO) – 2 marks
Definition & Purpose of BIA –
Business Impact Analysis (BIA) is a systematic process used to identify and
evaluate the effects of disruptions on critical business operations.
Steps/Process of BIA –
i. Identify Critical Business Functions
ii. Assess Impact of Disruption
iii. Determine Maximum Acceptable Outage (MAO)
iv. Identify Dependencies
v. Recommend Recovery Priorities
Recovery Time Objective (RTO) –
RTO is the maximum allowable time within which a business process or system
must be restored after a disruption.
Recovery Point Objective (RPO) –
RPO is the maximum acceptable amount of data loss, measured in time, that an
organization can tolerate.
Q5   b.   Analyze the different types of computer viruses by comparing and contrasting their   [10]
characteristics and behaviors. Also examine the various stages in the lifecycle of a
virus.
********** 6 **********
--- page 7 ---
Ans.
Marks Bifurcation:
Definition of Computer Virus – 1 mark
Any 3 Types of Viruses (Characteristics + Behavior) – 6 marks
Lifecycle of a Virus – 3 marks
Definition of a Computer Virus:
A computer virus is a malicious self-replicating program that attaches itself to
legitimate files and spreads from one system to another, often causing damage or
unauthorized actions.
Types of Computer Viruses:
•   File Infector Virus
• Macro Virus
• Boot Sector Virus
• Polymorphic Virus
• Metamorphic Virus
Lifecycle of a Virus:
i. Dormant Phase
ii. Propagation Phase
iii. Triggering Phase
iv. Execution / Payload Phase
Q6   a.   Explain the difference between Mandatory Access Control (MAC) and   [10]
Discretionary Access Control (DAC) by describing how each model works and how
they differ in terms of control and permissions.
Ans.
Marks Bifurcation:
Definition of MAC – 2 marks
Definition of DAC – 2 marks
How MAC works – 2 marks
How DAC works – 2 marks
Difference between MAC & DAC – 2 marks
Definition of MAC –
Mandatory Access Control is a strict, rule-based access model in which access
decisions are made by the system or security administrator, not by users.
Definition of DAC –
Discretionary Access Control allows the owner of a resource to decide who can
access it and what permissions are granted.
How MAC works –
• Every user and resource is assigned a security label (e.g., Top Secret,
Confidential, Public).
• The system decides access based on these labels using predefined policies.
• Users cannot modify permissions.
• Common in military, government, and high-security environments.
How DAC works –
• Each file or resource has an owner.
• Owners can grant or deny permissions (read/write/execute) to other users.
•   Flexible but less secure, as permissions may be misconfigured or misused.
• Common in personal computers and enterprise systems.
Difference between MAC & DAC – 2 marks
Feature   MAC   DAC
Control of Permissions   Controlled   by   Controlled by   resource
system/admin   owner
Flexibility   Rigid, rule-based   Flexible, user-controlled
********** 7 **********
--- page 8 ---
Security Level   Very high   Moderate
Risk   Low (users cannot change Higher (users may share
permissions)   access accidentally)
Q6   b.   Explain various terminologies associated with risk management, such as threat,   [10]
vulnerability, likelihood, impact, and risk exposure, with suitable examples.
Ans.
Marks Bifurcation:
Threat – 2 marks
Vulnerability – 2 marks
Likelihood – 2 marks
Impact – 2 marks
Risk Exposure – 2 marks
Threat –
A threat is any potential danger that can exploit a weakness and cause harm to an
organization.
Example: A hacker attempting to break into the network is a threat.
Vulnerability –
A vulnerability is a weakness or flaw in a system, process, or control that can be
exploited by a threat.
Example: Using outdated software with known bugs is a vulnerability
Likelihood –
A vulnerability is a weakness or flaw in a system, process, or control that can be
exploited by a threat.
Example: If employees frequently click unknown links, the likelihood of phishing
success is high.
Impact –
Impact is the degree of damage or loss that results when a threat exploits a
vulnerability.
Example: A ransomware attack causing loss of customer data leads to high impact.
Risk Exposure –
Risk exposure represents the overall level of risk, calculated using both likelihood
and impact.
Q7   a.   Describe the RSA algorithm and provide the formula for encrypting the message   [10]
(M) and decrypting the ciphertext to achieve confidentiality. In a public key system
using RSA, receiver receives the cipher text C=8, encrypted using public key (e) =
13 and two prime numbers where P=3 and Q=11. What is the plain text M?
Ans.
The RSA algorithm is a widely used public-key cryptosystem that relies on the
difficulty of factoring large prime numbers. It is used for secure data transmission,
including encryption, digital signatures, and key exchange. RSA consists of two
keys: a public key for encryption and a private key for decryption.
Steps of the RSA Algorithm
1. Key Generation: [3 Marks]
o Choose two large prime numbers p and q.
o Compute n=p×q, which forms part of the public and private key pair.
o Compute ϕ(n)=(p−1)×(q−1) (Euler's totient function).
o Choose a public exponent e, such that 1<e<ϕ(n) and gcd(e, ϕ(n))=1.
o Compute the private key d, the modular inverse of e mod ϕ(n). This
means solving d×e≡1 mod ϕ(n) using the Extended Euclidean
Algorithm.
o The public key is (e, n) and the private key is (d, n).
2. Encryption: [1 marks]
********** 8 **********
--- page 9 ---
o The sender takes the plaintext message M and computes the
ciphertext C using the recipient's public key (e, n):
C ≡ Me mod n
o The ciphertext C is sent to the recipient.
3. Decryption: [1 marks]
o The recipient uses their private key (d, n) to decrypt the ciphertext C
back into plaintext M:
M ≡ Cd mod n
Calculation: - [5 Marks: Each step 1 marks]
********** 9 **********
--- page 10 ---
Q7   b. An Amazon runs a large-scale online shopping platform that allows customers to   [5]
register accounts, browse products, place orders, and complete payments using
multiple digital payment options. The platform stores user profiles, order histories,
and transaction logs in a centralized database. During major festive sales, the system
experiences a sudden surge in user traffic, and even brief downtime can lead to
significant revenue loss. The company has also faced customer complaints related
to incorrect order statuses and disputed payment transactions. Additionally, any
exposure of customer data could damage the company’s reputation and lead to legal
consequences. From the given scenario, identify the confidentiality, integrity, and
availability requirements of the system. For each requirement, justify its degree of
importance in the context of the examination process.
Ans.
Marks Bifurcation:
Definition (1 marks), CIA requirements (Each 1 marks), Degree (1 marks)
Definition of Cyber Security:
refers to the practice of protecting computer systems, networks, programs, and
data from unauthorized access, attacks, damage, or theft. It ensures the safety of
digital information and maintains the confidentiality, integrity, and availability
(CIA) of data.
CIA Requirements in the Given Amazon Scenario
1. Confidentiality (Very High Importance):
The platform stores sensitive customer data such as user profiles, payment details,
and transaction logs. This information must be protected from unauthorized access
or data breaches. Any exposure of such data can damage the company’s reputation
and may lead to legal consequences. Hence, strong encryption, secure
authentication, and access control are essential.
2. Integrity (High Importance):
The system must ensure that order details, payment transactions, and order
statuses remain accurate and consistent. Customer complaints about incorrect
order status and disputed payments highlight the need for maintaining data
integrity. If data is altered or incorrect, it can lead to financial loss and loss of
********** 10 **********
--- page 11 ---
customer trust. Therefore, mechanisms like validation checks and secure
transaction processing are necessary.
3. Availability (Very High Importance):
The platform must be available at all times, especially during festive sales when
traffic is very high. Even short downtime can result in major revenue loss and
poor customer experience. Hence, the system should have high availability
through load balancing, backup servers, and fault-tolerant infrastructure.
Q7   c.   Describe the concept of proactive password choice. Which passwords are regarded   [5]
to be weak and easy to crack?
Ans.
Marks Bifurcation:
Concept of Proactive Password Choice: 3 marks
Weak Password Examples & Reason: 2 marks
Proactive Password Choice: Proactive password choice refers to a security
mechanism where users are guided to create strong passwords and weak passwords
are rejected at the time of creation.
Systems often enforce rules such as: Minimum length, Complexity requirements
(uppercase, lowercase, digits, symbols), Avoiding previously used or commonly
leaked passwords, Checking against password dictionaries.
Weak and Easy-to-Crack Passwords:
Passwords considered weak include: Very short passwords, Common dictionary
words/names, Keyboard patterns, Personal information, Reused passwords, Simple
numeric sequences
********** 11 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 4f3554ddbd1f

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_Computer_7047/Cyber Security/ANS_Cyber Security(702AI0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Cyber Security
Date: 30 Jun 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
a. What are passive attacks and active attacks in cybersecurity? Give a simple   [5]
definition and one basic example of each.
Ans.
Marks Bifurcation:
Definition of Passive Attack – 1 mark
Example of Passive Attack – 1 mark
Definition of Active Attack – 1 mark
Example of Active Attack – 1 mark
Any one key difference – 1 mark
Definition of Passive Attack –
A passive attack is an attack where the attacker only monitors or intercepts data
without altering it.
Example: Eavesdropping
Active Attack: An active attack is an attack where the attacker modifies, disrupts,
or injects data into the communication.
Example: Man-in-the-middle (MITM) attack
Key Difference: Key Difference
b.   Apply your understanding of public key cryptography to describe how a public key   [5]
cryptosystem works. Use a block diagram to illustrate the encryption and decryption
processes, and explain the role of each component.
Ans.
Marks Bifurcation:
Concept of Public Key Cryptography – 1 mark
Encryption Process Description – 1 mark
Decryption Process Description – 1 mark
Block Diagram – 1 mark
Role of Components – 1 mark
Concept of Public Key Cryptography –
Public key cryptography uses two keys: public key and private key.
Encryption Process Description –
********** 1 **********
--- page 2 ---
Sender takes the plaintext. Applies the encryption algorithm using the receiver’s
public key. Produces ciphertext that is securely transmitted.
Decryption Process Description –
Receiver takes the ciphertext. Uses the decryption algorithm with their private key.
Recovers the original plaintext.
Block Diagram –
Role of Components –
Public Key: Used by anyone to encrypt data for the receiver.
Private Key: Only known to receiver; decrypts messages encrypted with the
matching public key.
Encryption Algorithm: Converts plaintext → ciphertext.
Decryption Algorithm: Converts ciphertext → plaintext.
Diagram:
c.   Explain the meaning of the keystroke dynamics in biometric authentication. Write   [5]
any two distinctions between the dynamic and the static keystroke recognition. And
one benefit of this approach, as well.
Ans.
Marks Bifurcation:
2 marks for explaining keystroke dynamics
2 marks for differentiating static and dynamic recognition 1 mark for advantage
Keystroke dynamics is a behavioral biometric method of identifying a user through
his typing pattern. It compares the typing speed, time span between key press,
duration of key press and typing pressure. These trends are deemed to be individual.
In the static keystroke recognition, typing pattern is verified at the time of a single
instance at log-in typically by typing a set password or phrase. Once authentication
is done, there is no further monitoring. In dynamic recognition of keystroke, the
typing behaviour of the user is constantly observed during the session and this
makes it more secure. One of the merits of keystroke dynamics is that, it needs no
special hardware and can be compatible with a normal keyboard.
d.   Describe the capabilities and limitations of a firewall by explaining how it helps   [5]
protect a network and what types of threats or attacks it cannot defend against.
Ans.
Marks Bifurcation:
Definition of Firewall – 1 mark
Capabilities (any two points) – 2 marks
Limitations (any two points) – 2 marks
Definition:
A firewall is a security device or software that monitors and controls incoming and
outgoing network traffic based on predefined security rules
********** 2 **********
--- page 3 ---
Capabilities (any two points) –
Traffic Filtering
Access Control
Packet Inspection
Protects Against External Attacks
Limitations:
Cannot Stop Internal Attacks
Cannot Detect Encrypted Malware
Cannot Block Malware Already Inside
Q2   a.   Assume, a computer system has 4 users: Kate, Alice, Bob, and Mike. Kate owns   [10]
file Katefile, the other three people can only read the file. Mike and Kate can read
and write file Alicefile (owner Alice). Only Bob can read and write the file Bobfile
which he owns. Mike owns the file Mikefile and Bob and Kate can read and write
the file Mikefile. Assume the owner of a file can execute it.
1. Create an access control matrix describing this system.
2. Suppose the owner of a file can add and remove permissions to that file.
Mike removes Kate's permission and give permission to Alice to read and
write Mikefile. Show the new access control matrix.
3. Suppose the commands to add or remove permissions can be written into a
file, then that file is executed with the permissions of its owner. Does this
change what operations are considered trusted? Explain.
Ans.
Marks Bifurcation:
Create an access control matrix describing this system: 04marks
Suppose the owner of a file can add and remove permissions to that file. Mike
removes Kate's permission and give permission to Alice to read and write Mikefile.
Show the new access control matrix: 04marks
Suppose the commands to add or remove permissions can be written into a file, then
that file is executed with the permissions of its owner. Does this change what
operations are considered trusted? Explain.: 04marks
3) if a user (user A) is granted write + execute permissions on a file owned by another user
(user B), then user A gains indirect control permissions on that file (and all other files
owned by user B). This changes the trust level of the write+execute operations
Q2   b.   Explain the concept of a Host-Based Intrusion Detection System with the help of a   [10]
neat diagram, and describe how it works using a simple example.
Ans.
Marks Bifurcation:
********** 3 **********
--- page 4 ---
Definition of HIDS – 2 marks
Diagram – 2 marks
Components of HIDS – 2 marks
Working of HIDS – 2 marks
Simple Example – 2 marks
Definition of HIDS –
A Host-Based Intrusion Detection System (HIDS) is a security tool installed on an
individual host (computer/server) to monitor system activities, detect unauthorized
changes, and identify malicious actions on that specific machine.
Diagram –
Components of HIDS –
Data Collection Module, Analysis Engine, Alert/Reporting System, Policy/Rule Set
Working of HIDS –
• IDS continuously monitors the host’s system files, logs, and processes.
•   It checks for unexpected modifications; such as changes to configuration
files or unauthorized login attempts.
• The analysis engine evaluates the activity using signature-based (known
attacks) or anomaly-based (abnormal behavior) detection.
•   If a threat is detected, the HIDS generates an alert for the administrator.
Simple Example –
An attacker tries to modify the file /etc/passwd on a Linux server.
• HIDS detects that the file’s checksum has changed unexpectedly.
•   It identifies this as suspicious behavior.
Q3   a.   Apply the Hill Cipher encryption process to compute the ciphertext for the message   [10]
‘SECURE HOME’ using the key matrix derived from the key ‘ROCK’. Show the
step-by-step calculation.
Ans.
The key given is “ROCK”, so the key matrix will be   . [2 Mark]
The key given is “ROCK”, so the key matrix will be   . [2 Mark]
Using formula Ciphertext (C) = K * P mod 26.
Pair 1 (18,4): [1 Mark]
mod 26
O/P =(24,24) = (Y,Y).
Similar operation will be performed for each pair.
Pair 2 (2,20): [1 Mark]
O/P=(2,22) = (C,W)
********** 4 **********
--- page 5 ---
Pair 3 (17,4): [1 Mark]
O/P=(7,22)=(H,W)
Pair 4 (7,14): [1 Mark]
O/P=(3,24)=(D,Y)
Pair 5 (12,4): [1 Mark]
O/P = (0,12) = (A,M)
Final Ciphertext: YYCWHWDYAM. [1 Marks]
Q3   b.   Describe in detail any 2 types of non-malicious program errors.   [10]
Ans.
Marks Bifurcation:
Definition of Non-Malicious Program Errors: 02marks
Type 1 Description (Explanation): 04marks
Type 2 Description (Explanation): 04marks
Definition of Non-Malicious Program Errors:
Non-malicious program errors are unintentional software faults or mistakes caused
by design flaws, coding errors, or misconfigurations.
Type 1: Buffer Overflow Error
A buffer overflow occurs when a program writes data beyond the allocated memory
space, causing memory corruption.
How It Happens: Programmer allocates a fixed-size buffer (e.g., 20 bytes). User
inputs more than 20 bytes → extra data overwrites adjacent memory.
Impact: Program crashes or behaves unpredictably. Can unintentionally create a
security vulnerability allowing attackers to inject malicious code. System instability
due to overwritten memory.
Type 2: Incomplete Mediation
Incomplete mediation refers to a situation where a system does not properly check,
validate, or filter user inputs or requests before processing them.
How It Happens: The program receives input from a user or external source. It fails
to check whether the input is valid, safe, within limits, or allowed. The system
processes the invalidated input → leading to incorrect results or security risks.
Impact: Unauthorized access, Data corruption, Application crashes
Q4   a. What the differences between symmetric and public key encryption. Define   [10]
steganography and provide three examples steganography techniques.
Ans.
• Symmetric (Private) encryption: Uses the same key for both encryption and
decryption. Examples: AES, DES. Faster but key distribution is a challenge.
(2.5 mark)
• Asymmetric encryption: Uses two separate keys: a public key for encryption
and a private key for decryption. Example: RSA. Slower but solves the key
distribution problem. (2.5 mark)
• Steganography: The art of concealing a message within another message or
physical object. (2 marks)
•   Techniques: Hiding messages in images, audio files, or video files. (3 mark)
Q4   b.   Analyze the concept of Denial of Service (DoS) by explaining how it disrupts   [10]
system availability. Examine the characteristics of a classic DoS attack and discuss
how its mechanisms overwhelm a target to cause service failure.
Ans.
Marks Bifurcation:
Concept of DoS – 2 marks
********** 5 **********
--- page 6 ---
How DoS disrupts system availability – 2 marks
Characteristics of a classic DoS attack – 3 marks
Mechanisms used to overwhelm the target – 3 marks
Concept of DoS –
A Denial of Service (DoS) attack is a cyberattack that prevents legitimate users
from accessing a service by overwhelming the target system, server, or network
with excessive traffic or resource requests.
How DoS disrupts system availability –
A system has limited resources such as CPU, RAM, network bandwidth, and
connection limits. The attacker sends excessive or malformed requests, causing
resource exhaustion. Legitimate user requests cannot be processed, leading to: Slow
response, System crash and Complete service unavailability.
Characteristics of a classic DoS attack –
• Single Source Attack: Originates from one attacker or one machine.
• Resource Exhaustion: Focuses on consuming server resources such as CPU,
memory, or bandwidth.
• Volume-Based or Logic-Based: Uses heavy traffic (e.g., ICMP flood) or
malformed packets (e.g., Ping of Death).
• No Unauthorized Access Needed: The attacker does not need to breach the
system; only overload it.
Mechanisms used to overwhelm the target –
• Flooding Attacks: The attacker sends an extremely high volume of traffic
(e.g., ICMP flood, UDP flood). The server becomes too busy responding to
requests. Legitimate traffic gets dropped.
• Sending Malformed or Oversized Packets: Packets that violate protocol
rules can cause: Buffer overflow and Buffer overflow.
• Exploiting Protocol Weaknesses: The attacker uses vulnerabilities in
protocols (e.g., TCP three-way handshake). Example: SYN Flood
Q5   a.   Explain Business Impact Analysis (BIA) in detail. Also discuss key terms such as   [10]
Recovery Time Objective (RTO) and Recovery Point Objective (RPO).
Ans.
Definition & Purpose of BIA – 2 marks
Steps/Process of BIA – 4 marks
Recovery Time Objective (RTO) – 2 marks
Recovery Point Objective (RPO) – 2 marks
Definition & Purpose of BIA –
Business Impact Analysis (BIA) is a systematic process used to identify and
evaluate the effects of disruptions on critical business operations.
Steps/Process of BIA –
i. Identify Critical Business Functions
ii. Assess Impact of Disruption
iii. Determine Maximum Acceptable Outage (MAO)
iv. Identify Dependencies
v. Recommend Recovery Priorities
Recovery Time Objective (RTO) –
RTO is the maximum allowable time within which a business process or system
must be restored after a disruption.
Recovery Point Objective (RPO) –
RPO is the maximum acceptable amount of data loss, measured in time, that an
organization can tolerate.
Q5   b.   Analyze the different types of computer viruses by comparing and contrasting their   [10]
characteristics and behaviors. Also examine the various stages in the lifecycle of a
virus.
********** 6 **********
--- page 7 ---
Ans.
Marks Bifurcation:
Definition of Computer Virus – 1 mark
Any 3 Types of Viruses (Characteristics + Behavior) – 6 marks
Lifecycle of a Virus – 3 marks
Definition of a Computer Virus:
A computer virus is a malicious self-replicating program that attaches itself to
legitimate files and spreads from one system to another, often causing damage or
unauthorized actions.
Types of Computer Viruses:
•   File Infector Virus
• Macro Virus
• Boot Sector Virus
• Polymorphic Virus
• Metamorphic Virus
Lifecycle of a Virus:
i. Dormant Phase
ii. Propagation Phase
iii. Triggering Phase
iv. Execution / Payload Phase
Q6   a.   Explain the difference between Mandatory Access Control (MAC) and   [10]
Discretionary Access Control (DAC) by describing how each model works and how
they differ in terms of control and permissions.
Ans.
Marks Bifurcation:
Definition of MAC – 2 marks
Definition of DAC – 2 marks
How MAC works – 2 marks
How DAC works – 2 marks
Difference between MAC & DAC – 2 marks
Definition of MAC –
Mandatory Access Control is a strict, rule-based access model in which access
decisions are made by the system or security administrator, not by users.
Definition of DAC –
Discretionary Access Control allows the owner of a resource to decide who can
access it and what permissions are granted.
How MAC works –
• Every user and resource is assigned a security label (e.g., Top Secret,
Confidential, Public).
• The system decides access based on these labels using predefined policies.
• Users cannot modify permissions.
• Common in military, government, and high-security environments.
How DAC works –
• Each file or resource has an owner.
• Owners can grant or deny permissions (read/write/execute) to other users.
•   Flexible but less secure, as permissions may be misconfigured or misused.
• Common in personal computers and enterprise systems.
Difference between MAC & DAC – 2 marks
Feature   MAC   DAC
Control of Permissions   Controlled   by   Controlled by   resource
system/admin   owner
Flexibility   Rigid, rule-based   Flexible, user-controlled
********** 7 **********
--- page 8 ---
Security Level   Very high   Moderate
Risk   Low (users cannot change Higher (users may share
permissions)   access accidentally)
Q6   b.   Explain various terminologies associated with risk management, such as threat,   [10]
vulnerability, likelihood, impact, and risk exposure, with suitable examples.
Ans.
Marks Bifurcation:
Threat – 2 marks
Vulnerability – 2 marks
Likelihood – 2 marks
Impact – 2 marks
Risk Exposure – 2 marks
Threat –
A threat is any potential danger that can exploit a weakness and cause harm to an
organization.
Example: A hacker attempting to break into the network is a threat.
Vulnerability –
A vulnerability is a weakness or flaw in a system, process, or control that can be
exploited by a threat.
Example: Using outdated software with known bugs is a vulnerability
Likelihood –
A vulnerability is a weakness or flaw in a system, process, or control that can be
exploited by a threat.
Example: If employees frequently click unknown links, the likelihood of phishing
success is high.
Impact –
Impact is the degree of damage or loss that results when a threat exploits a
vulnerability.
Example: A ransomware attack causing loss of customer data leads to high impact.
Risk Exposure –
Risk exposure represents the overall level of risk, calculated using both likelihood
and impact.
Q7   a.   Describe the RSA algorithm and provide the formula for encrypting the message   [10]
(M) and decrypting the ciphertext to achieve confidentiality. In a public key system
using RSA, receiver receives the cipher text C=8, encrypted using public key (e) =
13 and two prime numbers where P=3 and Q=11. What is the plain text M?
Ans.
The RSA algorithm is a widely used public-key cryptosystem that relies on the
difficulty of factoring large prime numbers. It is used for secure data transmission,
including encryption, digital signatures, and key exchange. RSA consists of two
keys: a public key for encryption and a private key for decryption.
Steps of the RSA Algorithm
1. Key Generation: [3 Marks]
o Choose two large prime numbers p and q.
o Compute n=p×q, which forms part of the public and private key pair.
o Compute ϕ(n)=(p−1)×(q−1) (Euler's totient function).
o Choose a public exponent e, such that 1<e<ϕ(n) and gcd(e, ϕ(n))=1.
o Compute the private key d, the modular inverse of e mod ϕ(n). This
means solving d×e≡1 mod ϕ(n) using the Extended Euclidean
Algorithm.
o The public key is (e, n) and the private key is (d, n).
2. Encryption: [1 marks]
********** 8 **********
--- page 9 ---
o The sender takes the plaintext message M and computes the
ciphertext C using the recipient's public key (e, n):
C ≡ Me mod n
o The ciphertext C is sent to the recipient.
3. Decryption: [1 marks]
o The recipient uses their private key (d, n) to decrypt the ciphertext C
back into plaintext M:
M ≡ Cd mod n
Calculation: - [5 Marks: Each step 1 marks]
********** 9 **********
--- page 10 ---
Q7   b. An Amazon runs a large-scale online shopping platform that allows customers to   [5]
register accounts, browse products, place orders, and complete payments using
multiple digital payment options. The platform stores user profiles, order histories,
and transaction logs in a centralized database. During major festive sales, the system
experiences a sudden surge in user traffic, and even brief downtime can lead to
significant revenue loss. The company has also faced customer complaints related
to incorrect order statuses and disputed payment transactions. Additionally, any
exposure of customer data could damage the company’s reputation and lead to legal
consequences. From the given scenario, identify the confidentiality, integrity, and
availability requirements of the system. For each requirement, justify its degree of
importance in the context of the examination process.
Ans.
Marks Bifurcation:
Definition (1 marks), CIA requirements (Each 1 marks), Degree (1 marks)
Definition of Cyber Security:
refers to the practice of protecting computer systems, networks, programs, and
data from unauthorized access, attacks, damage, or theft. It ensures the safety of
digital information and maintains the confidentiality, integrity, and availability
(CIA) of data.
CIA Requirements in the Given Amazon Scenario
1. Confidentiality (Very High Importance):
The platform stores sensitive customer data such as user profiles, payment details,
and transaction logs. This information must be protected from unauthorized access
or data breaches. Any exposure of such data can damage the company’s reputation
and may lead to legal consequences. Hence, strong encryption, secure
authentication, and access control are essential.
2. Integrity (High Importance):
The system must ensure that order details, payment transactions, and order
statuses remain accurate and consistent. Customer complaints about incorrect
order status and disputed payments highlight the need for maintaining data
integrity. If data is altered or incorrect, it can lead to financial loss and loss of
********** 10 **********
--- page 11 ---
customer trust. Therefore, mechanisms like validation checks and secure
transaction processing are necessary.
3. Availability (Very High Importance):
The platform must be available at all times, especially during festive sales when
traffic is very high. Even short downtime can result in major revenue loss and
poor customer experience. Hence, the system should have high availability
through load balancing, backup servers, and fault-tolerant infrastructure.
Q7   c.   Describe the concept of proactive password choice. Which passwords are regarded   [5]
to be weak and easy to crack?
Ans.
Marks Bifurcation:
Concept of Proactive Password Choice: 3 marks
Weak Password Examples & Reason: 2 marks
Proactive Password Choice: Proactive password choice refers to a security
mechanism where users are guided to create strong passwords and weak passwords
are rejected at the time of creation.
Systems often enforce rules such as: Minimum length, Complexity requirements
(uppercase, lowercase, digits, symbols), Avoiding previously used or commonly
leaked passwords, Checking against password dictionaries.
Weak and Easy-to-Crack Passwords:
Passwords considered weak include: Very short passwords, Common dictionary
words/names, Keyboard patterns, Personal information, Reused passwords, Simple
numeric sequences
********** 11 **********
````

## 2025-26 · Re-Exam · Sem 10 · Answer key · paper 8476b9e75407

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_10/Re-Exam/Integrated_Computer_7032/Cyber Security/ANS_Cyber Security(702AI0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 10 Re-exam/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Cyber Security
Date: 30 Jun 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No. _1___ is compulsory.
3. Out of remaining questions, attempt any __4___ questions.
4. In all ___5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
a. What are passive attacks and active attacks in cybersecurity? Give a simple   [5]
definition and one basic example of each.
Ans.
Marks Bifurcation:
Definition of Passive Attack – 1 mark
Example of Passive Attack – 1 mark
Definition of Active Attack – 1 mark
Example of Active Attack – 1 mark
Any one key difference – 1 mark
Definition of Passive Attack –
A passive attack is an attack where the attacker only monitors or intercepts data
without altering it.
Example: Eavesdropping
Active Attack: An active attack is an attack where the attacker modifies, disrupts,
or injects data into the communication.
Example: Man-in-the-middle (MITM) attack
Key Difference: Key Difference
b.   Apply your understanding of public key cryptography to describe how a public key   [5]
cryptosystem works. Use a block diagram to illustrate the encryption and decryption
processes, and explain the role of each component.
Ans.
Marks Bifurcation:
Concept of Public Key Cryptography – 1 mark
Encryption Process Description – 1 mark
Decryption Process Description – 1 mark
Block Diagram – 1 mark
Role of Components – 1 mark
Concept of Public Key Cryptography –
Public key cryptography uses two keys: public key and private key.
Encryption Process Description –
********** 1 **********
--- page 2 ---
Sender takes the plaintext. Applies the encryption algorithm using the receiver’s
public key. Produces ciphertext that is securely transmitted.
Decryption Process Description –
Receiver takes the ciphertext. Uses the decryption algorithm with their private key.
Recovers the original plaintext.
Block Diagram –
Role of Components –
Public Key: Used by anyone to encrypt data for the receiver.
Private Key: Only known to receiver; decrypts messages encrypted with the
matching public key.
Encryption Algorithm: Converts plaintext → ciphertext.
Decryption Algorithm: Converts ciphertext → plaintext.
Diagram:
c.   Explain the meaning of the keystroke dynamics in biometric authentication. Write   [5]
any two distinctions between the dynamic and the static keystroke recognition. And
one benefit of this approach, as well.
Ans.
Marks Bifurcation:
2 marks for explaining keystroke dynamics
2 marks for differentiating static and dynamic recognition 1 mark for advantage
Keystroke dynamics is a behavioral biometric method of identifying a user through
his typing pattern. It compares the typing speed, time span between key press,
duration of key press and typing pressure. These trends are deemed to be individual.
In the static keystroke recognition, typing pattern is verified at the time of a single
instance at log-in typically by typing a set password or phrase. Once authentication
is done, there is no further monitoring. In dynamic recognition of keystroke, the
typing behaviour of the user is constantly observed during the session and this
makes it more secure. One of the merits of keystroke dynamics is that, it needs no
special hardware and can be compatible with a normal keyboard.
d.   Describe the capabilities and limitations of a firewall by explaining how it helps   [5]
protect a network and what types of threats or attacks it cannot defend against.
Ans.
Marks Bifurcation:
Definition of Firewall – 1 mark
Capabilities (any two points) – 2 marks
Limitations (any two points) – 2 marks
Definition:
A firewall is a security device or software that monitors and controls incoming and
outgoing network traffic based on predefined security rules
********** 2 **********
--- page 3 ---
Capabilities (any two points) –
Traffic Filtering
Access Control
Packet Inspection
Protects Against External Attacks
Limitations:
Cannot Stop Internal Attacks
Cannot Detect Encrypted Malware
Cannot Block Malware Already Inside
Q2   a.   Assume, a computer system has 4 users: Kate, Alice, Bob, and Mike. Kate owns   [10]
file Katefile, the other three people can only read the file. Mike and Kate can read
and write file Alicefile (owner Alice). Only Bob can read and write the file Bobfile
which he owns. Mike owns the file Mikefile and Bob and Kate can read and write
the file Mikefile. Assume the owner of a file can execute it.
1. Create an access control matrix describing this system.
2. Suppose the owner of a file can add and remove permissions to that file.
Mike removes Kate's permission and give permission to Alice to read and
write Mikefile. Show the new access control matrix.
3. Suppose the commands to add or remove permissions can be written into a
file, then that file is executed with the permissions of its owner. Does this
change what operations are considered trusted? Explain.
Ans.
Marks Bifurcation:
Create an access control matrix describing this system: 04marks
Suppose the owner of a file can add and remove permissions to that file. Mike
removes Kate's permission and give permission to Alice to read and write Mikefile.
Show the new access control matrix: 04marks
Suppose the commands to add or remove permissions can be written into a file, then
that file is executed with the permissions of its owner. Does this change what
operations are considered trusted? Explain.: 04marks
3) if a user (user A) is granted write + execute permissions on a file owned by another user
(user B), then user A gains indirect control permissions on that file (and all other files
owned by user B). This changes the trust level of the write+execute operations
Q2   b.   Explain the concept of a Host-Based Intrusion Detection System with the help of a   [10]
neat diagram, and describe how it works using a simple example.
Ans.
Marks Bifurcation:
********** 3 **********
--- page 4 ---
Definition of HIDS – 2 marks
Diagram – 2 marks
Components of HIDS – 2 marks
Working of HIDS – 2 marks
Simple Example – 2 marks
Definition of HIDS –
A Host-Based Intrusion Detection System (HIDS) is a security tool installed on an
individual host (computer/server) to monitor system activities, detect unauthorized
changes, and identify malicious actions on that specific machine.
Diagram –
Components of HIDS –
Data Collection Module, Analysis Engine, Alert/Reporting System, Policy/Rule Set
Working of HIDS –
• IDS continuously monitors the host’s system files, logs, and processes.
•   It checks for unexpected modifications; such as changes to configuration
files or unauthorized login attempts.
• The analysis engine evaluates the activity using signature-based (known
attacks) or anomaly-based (abnormal behavior) detection.
•   If a threat is detected, the HIDS generates an alert for the administrator.
Simple Example –
An attacker tries to modify the file /etc/passwd on a Linux server.
• HIDS detects that the file’s checksum has changed unexpectedly.
•   It identifies this as suspicious behavior.
Q3   a.   Apply the Hill Cipher encryption process to compute the ciphertext for the message   [10]
‘SECURE HOME’ using the key matrix derived from the key ‘ROCK’. Show the
step-by-step calculation.
Ans.
The key given is “ROCK”, so the key matrix will be   . [2 Mark]
The key given is “ROCK”, so the key matrix will be   . [2 Mark]
Using formula Ciphertext (C) = K * P mod 26.
Pair 1 (18,4): [1 Mark]
mod 26
O/P =(24,24) = (Y,Y).
Similar operation will be performed for each pair.
Pair 2 (2,20): [1 Mark]
O/P=(2,22) = (C,W)
********** 4 **********
--- page 5 ---
Pair 3 (17,4): [1 Mark]
O/P=(7,22)=(H,W)
Pair 4 (7,14): [1 Mark]
O/P=(3,24)=(D,Y)
Pair 5 (12,4): [1 Mark]
O/P = (0,12) = (A,M)
Final Ciphertext: YYCWHWDYAM. [1 Marks]
Q3   b.   Describe in detail any 2 types of non-malicious program errors.   [10]
Ans.
Marks Bifurcation:
Definition of Non-Malicious Program Errors: 02marks
Type 1 Description (Explanation): 04marks
Type 2 Description (Explanation): 04marks
Definition of Non-Malicious Program Errors:
Non-malicious program errors are unintentional software faults or mistakes caused
by design flaws, coding errors, or misconfigurations.
Type 1: Buffer Overflow Error
A buffer overflow occurs when a program writes data beyond the allocated memory
space, causing memory corruption.
How It Happens: Programmer allocates a fixed-size buffer (e.g., 20 bytes). User
inputs more than 20 bytes → extra data overwrites adjacent memory.
Impact: Program crashes or behaves unpredictably. Can unintentionally create a
security vulnerability allowing attackers to inject malicious code. System instability
due to overwritten memory.
Type 2: Incomplete Mediation
Incomplete mediation refers to a situation where a system does not properly check,
validate, or filter user inputs or requests before processing them.
How It Happens: The program receives input from a user or external source. It fails
to check whether the input is valid, safe, within limits, or allowed. The system
processes the invalidated input → leading to incorrect results or security risks.
Impact: Unauthorized access, Data corruption, Application crashes
Q4   a. What the differences between symmetric and public key encryption. Define   [10]
steganography and provide three examples steganography techniques.
Ans.
• Symmetric (Private) encryption: Uses the same key for both encryption and
decryption. Examples: AES, DES. Faster but key distribution is a challenge.
(2.5 mark)
• Asymmetric encryption: Uses two separate keys: a public key for encryption
and a private key for decryption. Example: RSA. Slower but solves the key
distribution problem. (2.5 mark)
• Steganography: The art of concealing a message within another message or
physical object. (2 marks)
•   Techniques: Hiding messages in images, audio files, or video files. (3 mark)
Q4   b.   Analyze the concept of Denial of Service (DoS) by explaining how it disrupts   [10]
system availability. Examine the characteristics of a classic DoS attack and discuss
how its mechanisms overwhelm a target to cause service failure.
Ans.
Marks Bifurcation:
Concept of DoS – 2 marks
********** 5 **********
--- page 6 ---
How DoS disrupts system availability – 2 marks
Characteristics of a classic DoS attack – 3 marks
Mechanisms used to overwhelm the target – 3 marks
Concept of DoS –
A Denial of Service (DoS) attack is a cyberattack that prevents legitimate users
from accessing a service by overwhelming the target system, server, or network
with excessive traffic or resource requests.
How DoS disrupts system availability –
A system has limited resources such as CPU, RAM, network bandwidth, and
connection limits. The attacker sends excessive or malformed requests, causing
resource exhaustion. Legitimate user requests cannot be processed, leading to: Slow
response, System crash and Complete service unavailability.
Characteristics of a classic DoS attack –
• Single Source Attack: Originates from one attacker or one machine.
• Resource Exhaustion: Focuses on consuming server resources such as CPU,
memory, or bandwidth.
• Volume-Based or Logic-Based: Uses heavy traffic (e.g., ICMP flood) or
malformed packets (e.g., Ping of Death).
• No Unauthorized Access Needed: The attacker does not need to breach the
system; only overload it.
Mechanisms used to overwhelm the target –
• Flooding Attacks: The attacker sends an extremely high volume of traffic
(e.g., ICMP flood, UDP flood). The server becomes too busy responding to
requests. Legitimate traffic gets dropped.
• Sending Malformed or Oversized Packets: Packets that violate protocol
rules can cause: Buffer overflow and Buffer overflow.
• Exploiting Protocol Weaknesses: The attacker uses vulnerabilities in
protocols (e.g., TCP three-way handshake). Example: SYN Flood
Q5   a.   Explain Business Impact Analysis (BIA) in detail. Also discuss key terms such as   [10]
Recovery Time Objective (RTO) and Recovery Point Objective (RPO).
Ans.
Definition & Purpose of BIA – 2 marks
Steps/Process of BIA – 4 marks
Recovery Time Objective (RTO) – 2 marks
Recovery Point Objective (RPO) – 2 marks
Definition & Purpose of BIA –
Business Impact Analysis (BIA) is a systematic process used to identify and
evaluate the effects of disruptions on critical business operations.
Steps/Process of BIA –
i. Identify Critical Business Functions
ii. Assess Impact of Disruption
iii. Determine Maximum Acceptable Outage (MAO)
iv. Identify Dependencies
v. Recommend Recovery Priorities
Recovery Time Objective (RTO) –
RTO is the maximum allowable time within which a business process or system
must be restored after a disruption.
Recovery Point Objective (RPO) –
RPO is the maximum acceptable amount of data loss, measured in time, that an
organization can tolerate.
Q5   b.   Analyze the different types of computer viruses by comparing and contrasting their   [10]
characteristics and behaviors. Also examine the various stages in the lifecycle of a
virus.
********** 6 **********
--- page 7 ---
Ans.
Marks Bifurcation:
Definition of Computer Virus – 1 mark
Any 3 Types of Viruses (Characteristics + Behavior) – 6 marks
Lifecycle of a Virus – 3 marks
Definition of a Computer Virus:
A computer virus is a malicious self-replicating program that attaches itself to
legitimate files and spreads from one system to another, often causing damage or
unauthorized actions.
Types of Computer Viruses:
•   File Infector Virus
• Macro Virus
• Boot Sector Virus
• Polymorphic Virus
• Metamorphic Virus
Lifecycle of a Virus:
i. Dormant Phase
ii. Propagation Phase
iii. Triggering Phase
iv. Execution / Payload Phase
Q6   a.   Explain the difference between Mandatory Access Control (MAC) and   [10]
Discretionary Access Control (DAC) by describing how each model works and how
they differ in terms of control and permissions.
Ans.
Marks Bifurcation:
Definition of MAC – 2 marks
Definition of DAC – 2 marks
How MAC works – 2 marks
How DAC works – 2 marks
Difference between MAC & DAC – 2 marks
Definition of MAC –
Mandatory Access Control is a strict, rule-based access model in which access
decisions are made by the system or security administrator, not by users.
Definition of DAC –
Discretionary Access Control allows the owner of a resource to decide who can
access it and what permissions are granted.
How MAC works –
• Every user and resource is assigned a security label (e.g., Top Secret,
Confidential, Public).
• The system decides access based on these labels using predefined policies.
• Users cannot modify permissions.
• Common in military, government, and high-security environments.
How DAC works –
• Each file or resource has an owner.
• Owners can grant or deny permissions (read/write/execute) to other users.
•   Flexible but less secure, as permissions may be misconfigured or misused.
• Common in personal computers and enterprise systems.
Difference between MAC & DAC – 2 marks
Feature   MAC   DAC
Control of Permissions   Controlled   by   Controlled by   resource
system/admin   owner
Flexibility   Rigid, rule-based   Flexible, user-controlled
********** 7 **********
--- page 8 ---
Security Level   Very high   Moderate
Risk   Low (users cannot change Higher (users may share
permissions)   access accidentally)
Q6   b.   Explain various terminologies associated with risk management, such as threat,   [10]
vulnerability, likelihood, impact, and risk exposure, with suitable examples.
Ans.
Marks Bifurcation:
Threat – 2 marks
Vulnerability – 2 marks
Likelihood – 2 marks
Impact – 2 marks
Risk Exposure – 2 marks
Threat –
A threat is any potential danger that can exploit a weakness and cause harm to an
organization.
Example: A hacker attempting to break into the network is a threat.
Vulnerability –
A vulnerability is a weakness or flaw in a system, process, or control that can be
exploited by a threat.
Example: Using outdated software with known bugs is a vulnerability
Likelihood –
A vulnerability is a weakness or flaw in a system, process, or control that can be
exploited by a threat.
Example: If employees frequently click unknown links, the likelihood of phishing
success is high.
Impact –
Impact is the degree of damage or loss that results when a threat exploits a
vulnerability.
Example: A ransomware attack causing loss of customer data leads to high impact.
Risk Exposure –
Risk exposure represents the overall level of risk, calculated using both likelihood
and impact.
Q7   a.   Describe the RSA algorithm and provide the formula for encrypting the message   [10]
(M) and decrypting the ciphertext to achieve confidentiality. In a public key system
using RSA, receiver receives the cipher text C=8, encrypted using public key (e) =
13 and two prime numbers where P=3 and Q=11. What is the plain text M?
Ans.
The RSA algorithm is a widely used public-key cryptosystem that relies on the
difficulty of factoring large prime numbers. It is used for secure data transmission,
including encryption, digital signatures, and key exchange. RSA consists of two
keys: a public key for encryption and a private key for decryption.
Steps of the RSA Algorithm
1. Key Generation: [3 Marks]
o Choose two large prime numbers p and q.
o Compute n=p×q, which forms part of the public and private key pair.
o Compute ϕ(n)=(p−1)×(q−1) (Euler's totient function).
o Choose a public exponent e, such that 1<e<ϕ(n) and gcd(e, ϕ(n))=1.
o Compute the private key d, the modular inverse of e mod ϕ(n). This
means solving d×e≡1 mod ϕ(n) using the Extended Euclidean
Algorithm.
o The public key is (e, n) and the private key is (d, n).
2. Encryption: [1 marks]
********** 8 **********
--- page 9 ---
o The sender takes the plaintext message M and computes the
ciphertext C using the recipient's public key (e, n):
C ≡ Me mod n
o The ciphertext C is sent to the recipient.
3. Decryption: [1 marks]
o The recipient uses their private key (d, n) to decrypt the ciphertext C
back into plaintext M:
M ≡ Cd mod n
Calculation: - [5 Marks: Each step 1 marks]
********** 9 **********
--- page 10 ---
Q7   b. An Amazon runs a large-scale online shopping platform that allows customers to   [5]
register accounts, browse products, place orders, and complete payments using
multiple digital payment options. The platform stores user profiles, order histories,
and transaction logs in a centralized database. During major festive sales, the system
experiences a sudden surge in user traffic, and even brief downtime can lead to
significant revenue loss. The company has also faced customer complaints related
to incorrect order statuses and disputed payment transactions. Additionally, any
exposure of customer data could damage the company’s reputation and lead to legal
consequences. From the given scenario, identify the confidentiality, integrity, and
availability requirements of the system. For each requirement, justify its degree of
importance in the context of the examination process.
Ans.
Marks Bifurcation:
Definition (1 marks), CIA requirements (Each 1 marks), Degree (1 marks)
Definition of Cyber Security:
refers to the practice of protecting computer systems, networks, programs, and
data from unauthorized access, attacks, damage, or theft. It ensures the safety of
digital information and maintains the confidentiality, integrity, and availability
(CIA) of data.
CIA Requirements in the Given Amazon Scenario
1. Confidentiality (Very High Importance):
The platform stores sensitive customer data such as user profiles, payment details,
and transaction logs. This information must be protected from unauthorized access
or data breaches. Any exposure of such data can damage the company’s reputation
and may lead to legal consequences. Hence, strong encryption, secure
authentication, and access control are essential.
2. Integrity (High Importance):
The system must ensure that order details, payment transactions, and order
statuses remain accurate and consistent. Customer complaints about incorrect
order status and disputed payments highlight the need for maintaining data
integrity. If data is altered or incorrect, it can lead to financial loss and loss of
********** 10 **********
--- page 11 ---
customer trust. Therefore, mechanisms like validation checks and secure
transaction processing are necessary.
3. Availability (Very High Importance):
The platform must be available at all times, especially during festive sales when
traffic is very high. Even short downtime can result in major revenue loss and
poor customer experience. Hence, the system should have high availability
through load balancing, backup servers, and fault-tolerant infrastructure.
Q7   c.   Describe the concept of proactive password choice. Which passwords are regarded   [5]
to be weak and easy to crack?
Ans.
Marks Bifurcation:
Concept of Proactive Password Choice: 3 marks
Weak Password Examples & Reason: 2 marks
Proactive Password Choice: Proactive password choice refers to a security
mechanism where users are guided to create strong passwords and weak passwords
are rejected at the time of creation.
Systems often enforce rules such as: Minimum length, Complexity requirements
(uppercase, lowercase, digits, symbols), Avoiding previously used or commonly
leaked passwords, Checking against password dictionaries.
Weak and Easy-to-Crack Passwords:
Passwords considered weak include: Very short passwords, Common dictionary
words/names, Keyboard patterns, Personal information, Reused passwords, Simple
numeric sequences
********** 11 **********
````

## 2024-25 · Final-Exam · Sem 3 · Answer key · paper 46a1c5092a5a

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `00_Original_Downloads/2024/65008__Semester III.zip :: Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Cyber Security/ANS_Final-Exam_Cyber Security(703AI0C002)_Semester III_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13 Dec 2024
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: II/Semester III(Exam Year: 2024-2025)
Subject: Cyber Security
Date: 13 Dec 2024   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory. Out of remaining questions, attempt any 4 questions.
5. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO1; SO1 ;BL-   a. What are active attacks? Explain any three types of active attacks.   [5]
low
active attacks-2m
types-1 mark each
CO2; SO1 ;BL-   b.   Describe Discretionary Access Control with strengths and limitations.   [5]
moderate   DAC-3m
Strengths-1m
Limitations-1m
CO3; SO1;BL-   c.   Discuss Transport mode of VPN with neat diagram.   [5]
low
Transport mode explanation-3m
Diag-2m
CO4; SO1;BL2   d. What is Risk management? Enlist Steps in Risk Management.   [5]
RM-1M
Steps-4M
Q2
CO1; SO1; BL2   a.   Explain different types of attacks. Consider an online banking application.   [10]
Who might want to attack the program? What types of harm might they
want to cause? What kinds of vulnerabilities might they exploit to cause
harm?
Types of attacks-3m
Who might want to attack the program-2m
1. Cybercriminals
2. Hacktivists
3. Insiders
4. State-sponsored actors
Types of Harm-3m
1. Financial Loss: Direct theft of funds or unauthorized transactions.
********** 1 **********
--- page 2 ---
2. Data Breaches: Exposure of sensitive customer data, leading to
identity theft.
3. Reputation Damage: Loss of customer trust and business, which
can have long-term consequences.
4. Service Disruption: Denial of service attacks can incapacitate the
banking application, preventing legitimate users from accessing
services.
Vulnerabilities-2m
CO2; SO1; BL2   b. With suitable examples explain any four types of substitution ciphers.   [10]
Compare substitution ciphers with transposition ciphers.
substitution ciphers -8m
Comparison -2m
Q3
CO1; SO1;BL2   a. Apply RSA algorithm to encrypt and decrypt the message string “ABC”.   [10]
Assume suitable values for p, q, encryption key and decryption key.
 Select primes p=11, q=3.
 n = pq = 11x3 = 33
φ (n) = (p-1)(q-1) = 10x2 = 20
 Choose e=3
Check gcd (e, φ (n) ) = gcd(3, 20) = 1
(i.e. 3 and 20 have no common factors except 1)
 Compute d such that ed ≡ 1 mod φ (n)
i.e. compute d = e-1 mod φ (n) = 3-1 mod 20
i.e. find a value for d such that φ divides (ed-1)
i.e. find d such that 20 divides 3d-1.
Simple testing (d = 1, 2, ...) gives d = 7
Check: ed-1 = 3.7 - 1 = 20, which is divisible by φ (n).
 Public key = (e,n) = (3, 33)   Private key = (d,n) = (7,33).
CO2; SO1;BL2   b.   Discuss various biometric features with applications used   for   [10]
authentication. Also summarize Problems with biometrics.
Features with applications-7m
Problems-3m
Problems:
Biometrics are relatively new and some people find their use intrusive
Devices are costly
It can become a single point of failure
Although equipment is improving, there are still false readings
Q4
CO3; SO1;BL2   a. Summarize the steps in DES algorithm. Compute the output using   [10]
following S-box 1 for input value 101110. Write the steps followed
for the same.
********** 2 **********
--- page 3 ---
DES steps-7 m
s-box output with steps-3m
 Step 1: Apply an initial permutation on a block.
 Result is B=IP(P) where P is the 64 bit block IP Initial
Permutation function and B the result.
   Step 2: Split B into 32 bit blocks
   Li = leftmost 32 bits
Ri = rightmost 32 bits.
   Step 3: Pick a 56 bit key. Permute it
   Step 4: Left circular shift it by 1 bit giving K1.
 Step 5: Perform a complex sequence of operations and obtain
 X1 = F(R1,K1) (The complex set of operations include table
look up and dropping bits).
 Step 6: Find R2 = L1 + X1
 Step 7: Set L2 = R1
 Repeat steps 2 to 7 , 16 times to get B16 = L16,R16
 Step 8: Apply inverse of initial permutation on B16
 The result is the encrypted block
CO4; SO1;BL2   b. With neat diagram, explain working of Kerberos system.   [10]
Discuss any five types of access controls with suitable examples.
2 marks for each type
Q5
CO3; SO1;BL2   a. What are non-malicious program errors? Explain their major types.   [10]
1 m – non-malicious program errors
3 marks for each type
CO4; SO2;BL2   b.   Explain Link encryption with the help of neat diagram and compare it   [10]
with End-to-End Encryption.
********** 3 **********
--- page 4 ---
Link encryption with diagram-5m
Comparison-5m
Link Encryption In link encryption, data are encrypted justbefore the
system places them on the physical communications link. at layer 1 or 2
in the OSI model. Similarly, decryption occurs just as the communication
arrives at and enters the receiving computer
Q6
CO1; SO2;BL4   a. What are Intrusion Detection Systems? Explain any four types of   [10]
Intrusion Detection Systems with their drawbacks.
IDS-2m
IDS types- 2m for each type
CO4; SO1;BL2   b. Summarize the steps involved in Risk Analysis for a chain of hospitals.   [10]
6m- steps
4m – examples/solutions for given scenario
Steps of a Risk Analysis
1. Identify assets.
2. Determine vulnerabilities.
3. Estimate likelihood of exploitation.
4. Compute expected annual loss.
5. Survey applicable controls and their costs.
6. Project annual savings of control
Q7
CO3; SO1; BL1   a. Why Digital signatures are important? Discuss the process for creating and   [5]
verifying Digital Signatures.
********** 4 **********
--- page 5 ---
CO2; SO1; BL2   b. What are the characteristics of a good password?   [5]
Length: At least 12-16 characters long. Longer passwords are generally
more secure.
Complexity: A mix of uppercase and lowercase letters, numbers, and
special characters (e.g., !, @, #).
Unpredictability: Avoid common words, phrases, or easily guessable
information like birthdays or names.
c.   Discuss developmental Controls against program threats.
Modularity, Encapsulation and information hiding
d.   Explain Tunnel mode VPN with neat diagram.
********** 5 **********
````
