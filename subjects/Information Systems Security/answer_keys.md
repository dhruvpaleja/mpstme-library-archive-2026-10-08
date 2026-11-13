# Information Systems Security: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper b9564189ee13

- Departments: Information Technology
- Programmes: BTech IT 7001, MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_IT_7001/Information Systems Security/ANS_Information Systems Security(702IT0C029)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: mixed (16 pages), mean OCR confidence 72.9
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (IT)/MBA Tech (IT)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: Information Systems Security
Date: 08 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure on the right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary
Q
Answer briefly:
1
a. Describe the critical characteristics of Information
Critical Characteristics of Information
The value of information comes from the characteristics it possesses.
Availability – Enables users who need to access information to do so without
interference or obstruction and in the required format. The information is said to be
available to an authorized user when and where needed and in the correct format.
Accuracy – Free from mistake or error and having the value that the end user expects.
CO   If information contains a value different from the user’s expectations due to the
-
1;   intentional or unintentional modification of its content, it is no longer accurate.   [05]
BL- 2   Authenticity –The quality or state of being genuine or original, rather than a
reproduction or fabrication. Information is authentic when it is the information that was
originally created, placed, stored, or transferred.
Confidentiality – The quality or state of preventing disclosure or exposure to
unauthorized individuals or systems.
Integrity – The quality or state of being whole, complete, and uncorrupted. The integrity
of information is threatened when the information is exposed to corruption, damage,
destruction, or other disruption of its authentic state.
********** 1 **********
--- page 2 ---
Utility – The quality or state of having value for some purpose or end. Information has
value when it serves a particular purpose. This means that if information is available,
but not in a format meaningful to the end user, it is not useful.
Possession – The quality or state of having ownership or control of some object or item.
Information is said to be in possession if one obtains it, independent of format or other
characteristic. While a breach of confidentiality always results in a breach of possession,
a breach of possession does not always result in a breach of confidentiality.
b   Symmetric Key
Feature   Asymmetric Key Cryptography
.   Cryptography
Same key for encryption and Different keys for encryption
Key Usage
decryption   (public) and decryption (private)
Faster, less computationally
Speed   Slower due to complex algorithms
intensive
CO   Key   Requires secure key   No need to exchange private key;
-   Distribution   exchange channel   public key can be shared openly
2;   [05]
BL   Vulnerable if key is   More secure for key exchange and
Security
– 2   intercepted   authentication
Common
AES, DES, 3DES   RSA, ECC, DSA
Algorithms
Bulk data encryption,   Secure communications, digital
Use Cases
internal systems   signatures
Poor for large networks (key Better scalability with public key
Scalability
management issue)   infrastructure (PKI)
c. Distinguish between BIBA and BLP model
Aspect   BLP (Bell-LaPadula) Model   BIBA Model
Purpose   Ensures confidentiality of data Ensures integrity of data
Primary   Prevent unauthorized read   Prevent unauthorized write or
Concern   access to sensitive info   modification
Focus   Protects against data leakage   Protects against data corruption
CO   - Simple Integrity Property: No
- Simple Security Property: No
-5;   read-down (cannot read lower   [05]
BL   Security Rules read-up (no read of higher level) integrity data) - Star Property
– 2   - Star Property (*): No write-
(*): No write-up (cannot write to
down (no write to lower level)
higher integrity level)
Direction of   Information flows from low to   Information flows from high to
Information   high clearance (write up, read   low integrity (write down, read up)
Flow   down) to protect confidentiality to protect integrity
Military, government,
Systems where data integrity is
Used In   organizations needing strict
critical, e.g., financial systems
confidentiality
CO d
-   Impact on Individuals:
3;   .   • Cybercrimes like cyberstalking, fake profiles, email hacking, phishing, obscene [05]
BL-   emails, and blackmailing directly target people.
2
********** 2 **********
--- page 3 ---
• Victims face harassment, defamation, loss of privacy, identity theft, and even
psychological trauma.
• Example: Fake profile creation leading to harassment of individuals.
Impact on Property:
• Criminals can steal, alter, or destroy data and digital assets, which are considered
valuable property. Examples:
• Data diddling, software piracy, virus dissemination, illegal money transfer, and
online stock fraud.
• Organizations face financial losses, operational disruptions, and reputational
damage.
Impact on Government:
• Cybercrime can take the form of cyber terrorism or attacks on critical
infrastructure.
• These crimes may spread propaganda, disrupt essential services, or create
national security threats.
• Example: Objectionable online content against leaders, communities, or the
nation.
a. Program-Level Information Security Policy
1.0 Policy Name: Enterprise Data Protection & Secure Development Policy
1.1 Policy Number: PL-IS-001
1.2 Effective Date:
1.3 Policy Owner: Chief Information Security Officer (CISO)
2.0 Core Objective
The core objective of this program-level policy is to establish a company-wide
framework of accountability and standardized practices to protect the confidentiality,
integrity, and availability of all company and client data throughout its entire lifecycle,
Q   from creation and processing to storage and disposal, thereby creating a consistent and
2   defensible security posture.
[10
CO   3.0 High-Level Policy Statements
-   ]
1;   3.1 Policy Statement: Data Encryption & Endpoint Security
BL-
3   Statement: All company data, whether at rest on any storage medium (including laptops,
mobile devices, and removable media) or in transit across any network, must be
protected using approved encryption standards.
Addresses: Incident A (Lost laptop with unencrypted client data).
Enforcement Procedure/Technical Control:
Control: Implementation of a centralized Mobile Device Management (MDM) solution.
Procedure: The MDM will be configured to automatically enforce full-disk encryption
on all company-owned laptops. The system will block device access if encryption is
disabled and will provide the capability to remotely wipe data from lost or stolen
devices.
********** 3 **********
--- page 4 ---
3.2 Policy Statement: Secure Development Lifecycle & Secrets Management
Statement: All system development and operational activities must integrate security
practices throughout the lifecycle, including the mandatory use of secure, automated
tools for handling credentials and secrets. Hardcoding secrets in application code is
strictly prohibited.
Addresses: Incident B (Developer uploaded API keys to a public repository).
Enforcement Procedure/Technical Control:
Control: Implementation of a Secrets Management Solution and integration of Static
Application Security Testing (SAST) tools into the CI/CD pipeline.
Procedure: Developers will be required to retrieve all API keys, passwords, and tokens
programmatically from the central secrets manager. The SAST tool will be configured
with rules to scan every code commit for patterns matching secrets and any finding will
automatically fail the build and alert the security team.
b Risk Management Recommendations
.   1. Risk A: Sophisticated Phishing Emails Targeting Customers
Recommended Approach: Risk Mitigation
Justification: The bank cannot prevent attackers from sending phishing emails, and it
cannot avoid offering online services to its customers. Therefore, the goal is to reduce
both the likelihood and impact of a successful attack.
Specific Actions:
1. Multi-Factor Authentication (MFA): Mandate MFA for all customer logins and high-
value transactions. This reduces the impact because a stolen password alone is
Q
insufficient for access.
2
CO   2. AI-Powered Email Filtering: Deploy advanced security controls to detect and [10
-   quarantine sophisticated phishing emails before they reach customers, reducing the   ]
4;
BL-   likelihood of exposure.
3
3.   Customer Security Awareness Campaigns: Run ongoing education to teach
customers how to identify phishing attempts. This reduces the likelihood of them falling
victim.
2. Risk B: Using Outdated, Insecure Software
Recommended Approach: Risk Avoidance
Justification: The risk posed by this software is fundamental and severe. It is a known
weakness with readily available exploits. The "cheap" cost is vastly outweighed by the
potential financial and reputational damage of a breach.
Specific Actions:
********** 4 **********
--- page 5 ---
1. Immediate Decommissioning: Immediately remove the outdated software from the
network.
2. Procure or Develop a Secure Alternative: Replace it with a modern, supported
software solution that receives regular security patches.
3. Policy Update: Formalize a policy that prohibits the use of unsupported or end-of-
life software.
a. Explain RSA algorithm. Compute the value of private key, d if two prime numbers p
and q are 41 and 7 respectively and public key, e=23 using RSA algorithm.
Algorithm
Choose two large prime numbers p, q
Let n = pq; then (n) = (p–1)(q–1)
Choose e < (n) such that e is relatively prime to (n).
Compute d such that ed mod (n) = 1
Q
Public key: (e, n); private key: (d,n)
3
Encipher: c = me mod n   [10
CO
-   Decipher: m = cd mod n   ]
2;
BL-
3
n=287
(n)=240
e=23
d=167
Appropriate explanation – 6 Marks
Calculation of d with all steps – 4 mark each
b Kerberos is a trusted third-party authentication protocol that can be used to provide a
.   single sign-on solution and to provide protection for logon credentials.
Kerberos provides the security services of confidentiality and integrity protection for
Q   authentication traffic.
3   Two versions in use: 4 & 5
[10
CO   Kerberos Components
-   ]
5;   The Kerberos authentication mechanism centers on a trusted server (or servers) that host
BL-
3   the functions of the KDC, Ticket Granting Service (TGS), and Authentication Service
(AS).
Generally, the Kerberos central server that hosts all of these services is simply referred
to as the KDC.
********** 5 **********
--- page 6 ---
Working
Limitations:
If the KDC is ever compromised, then the secret key of every system on the network is
also compromised.
Also, if the KDC goes offline, no subject authentication is possible.
Issued tickets are stored in memory on the client and server.
Malicious subjects can replay captured tickets if they are reused within their lifetime
window.
Issued tickets, specifically the Ticket Granting Ticket (TGT), are based on a hash of the
user’s password with an added time stamp for expiration.
Kerberos only encrypts authentication traffic (i.e., mechanisms for proving identity), it
does not provide any security for subsequent communication sessions or data
transmissions.
Description of components – 3 marks
Working – 5 marks
Limitations – 2 marks
a. Systems that employ role-based or task-based access controls define the ability of a
subject to access an object through the use of subject roles (i.e., job descriptions) or
Q
tasks (i.e., work functions).
4
If a subject is in a management position, they will have greater access to resources than [10
CO
-5;   someone who is in a temporary position.   ]
BL-
Role-based access controls are useful in environments with frequent personnel changes
2
because access is based on a job description (i.e., a role or task) rather than on a subject’s
identity.
********** 6 **********

[Text in pictures on this page, read by OCR]
1. Client Logon

Key Distribution Center

Authentication Server

Client 9 TCT
<
3 A
3 3. TGT
a rd
=
g 3
a = 4. Client-to-Server ticket
£ 2
= <
2 o
oO
ov

Server

Ticket Granting Server
--- page 7 ---
Note the difference between groups and roles: groups define sets of users while roles
define sets of privileges.
Advantages of RBAC
Simplified access management: Instead of assigning individual permissions,
administrators can assign users to roles with predefined access rights. This greatly
reduces the administrative overhead associated with onboarding, offboarding, or
changing employee roles.
Enhanced security: RBAC enforces the principle of least privilege, ensuring users only
have access to the information and functions necessary for their job. This minimizes the
risk of unauthorized data access and reduces the potential damage from a compromised
user account.
Improved compliance and auditing: For regulated industries (e.g., healthcare and
finance), RBAC provides a structured, auditable framework for managing data access.
It makes it easier to demonstrate that access controls are in place and to generate audit
trails showing who accessed what and when.
Greater operational efficiency: Standardized role-based permissions allow employees to
get the access they need without manual intervention from IT, eliminating bottlenecks
and increasing overall productivity.
Better visibility and control: Managers and administrators gain a clear overview of who
has access to what within the organization. This increased visibility helps them monitor
usage and enforce security rules consistently.
Scalability: The model is easily scalable. As an organization grows, administrators don't
need to create a new set of permissions for every new hire. Instead, they simply assign
a user to an existing role.
Limitations of RBAC
Can be inflexible in dynamic environments: Because permissions are tied to static roles,
RBAC can struggle to adapt to the fluid nature of modern project teams, temporary
********** 7 **********
--- page 8 ---
assignments, and remote work. Temporary permission changes can become a manual
administrative hassle.
Potential for "role explosion": In large, complex organizations, a rigid adherence to
RBAC can lead to the creation of too many highly specific roles to accommodate minor
differences in job functions. Managing hundreds or thousands of roles can become
confusing and unwieldy, defeating the purpose of simplified management.
Requires extensive upfront planning: For RBAC to be effective, it requires a deep
understanding of organizational workflows to define roles correctly. If not implemented
thoughtfully, roles can be misaligned with actual business needs.
Difficulty handling exceptions: Making one-off, minor exceptions for an individual user
can be cumbersome and may lead to the creation of new, unnecessary roles. This can
result in "privilege creep," where users accumulate more access than they need over
time.
Inadequate for fine-grained, contextual access control: RBAC determines access solely
on a user's role. It cannot make decisions based on dynamic, contextual factors, such as
a user's location, the time of day, or the sensitivity of the specific data being accessed.
For this, organizations often need to combine RBAC with another model, such as
Attribute-Based Access Control (ABAC).
Separation of duties (SoD) can be complex: While RBAC supports SoD, it requires
careful design to ensure a single individual is not assigned multiple conflicting roles.
For example, a single user should not have roles that allow them to both initiate and
approve a financial transaction.
Appropriate explanation of RBAC – 6 Marks
Advantages – 2 Marks
Limitations – 2 marks
********** 8 **********
--- page 9 ---
chanel

channel

channel

“SSH User Authentication Protocol

publickey. caliber icarar |

password. password!

bosrbased user, hast

“Be aspen Praiacal

TCP

=

H H ty kep-esncbange j
i od — i 7 7 algerie ,
H H Set fig, Dilffic-Aiedlmen

4 én ; Server Authentication
<o [aurhentcator
a application software (e.g. ssh, sshd, scp, slip, sftp_server)
3 $SH Authentication Protocol (SSH-AUTH] = SSH Connection Protocal [5SH-CONN]
dient outhentication TCP port ond X Forwarding
publickey quthenticofion agent forwarding
password interaclive session support
password changing flow con
pseuda-terminals
terminal hondling
modes, window size
signal propagation
dota compression
$SH Transport Pratocel [SSH-TRANS]
server authentication
algorithm negotiation
session key exchonge
privacy
integrity
session ID
TEP (or other transparent, relioble, duplex byte-stream via the PraxyCommand feature}
Q | a. | Explain the types of attacks possible on cryptosystems citing real life examples. [10
5 ]

FIC QF OH ar
--- page 10 ---
CO   Ciphertext Only Attacks (COA) − In this method, the attacker has access to a set of
-
2;   ciphertext(s). He does not have access to corresponding plaintext. COA is said to be
BL-
successful when the corresponding plaintext can be determined from a given set of
2
ciphertext. Occasionally, the encryption key can be determined from this attack. Modern
cryptosystems are guarded against ciphertext-only attacks.
Known Plaintext Attack (KPA) − In this method, the attacker knows the plaintext for
some parts of the ciphertext. The task is to decrypt the rest of the ciphertext using this
information. This may be done by determining the key or via some other method. The
best example of this attack is linear cryptanalysis against block ciphers.
Chosen Plaintext Attack (CPA) − In this method, the attacker has the text of his choice
encrypted. So he has the ciphertext-plaintext pair of his choice. This simplifies his task
of determining the encryption key. An example of this attack is differential
cryptanalysis applied against block ciphers as well as hash functions. A popular public
key cryptosystem, RSA is also vulnerable to chosen-plaintext attacks.
Dictionary Attack − This attack has many variants, all of which involve compiling a
‘dictionary’. In simplest method of this attack, attacker builds a dictionary of ciphertexts
and corresponding plaintexts that he has learnt over a period of time. In future, when an
attacker gets the ciphertext, he refers the dictionary to find the corresponding plaintext.
Brute Force Attack (BFA) − In this method, the attacker tries to determine the key by
attempting all possible keys. If the key is 8 bits long, then the number of possible keys
is 28 = 256. The attacker knows the ciphertext and the algorithm, now he attempts all
the 256 keys one by one for decryption. The time to complete the attack would be very
high if the key is long.
Birthday Attack − This attack is a variant of brute-force technique. It is used against
the cryptographic hash function. When students in a class are asked about their
birthdays, the answer is one of the possible 365 dates. Let us assume the first student's
birthdate is 3rd Aug. Then to find the next student whose birthdate is 3rd Aug, we need
to enquire 1.25*√365 ≈ 25 students. Similarly, if the hash function produces 64-bit hash
values, the possible hash values are 1.8x1019. By repeatedly evaluating the function for
different inputs, the same output is expected to be obtained after about 5.1x109 random
inputs. If the attacker is able to find two different inputs that give the same hash value,
it is a collision and that hash function is said to be broken.
Man in Middle Attack (MIM) − The targets of this attack are mostly public key
cryptosystems where key exchange is involved before communication takes place.
Host A wants to communicate to host B, hence requests public key of B.
********** 10 **********
--- page 11 ---
An attacker intercepts this request and sends his public key instead.
Thus, whatever host A sends to host B, the attacker is able to read.
In order to maintain communication, the attacker re-encrypts the data after reading with
his public key and sends to B.
The attacker sends his public key as A’s public key so that B takes it as if it is taking it
from A.
Side Channel Attack (SCA) − This type of attack is not against any particular type of
cryptosystem or algorithm. Instead, it is launched to exploit the weakness in physical
implementation of the cryptosystem.
Timing Attacks − They exploit the fact that different computations take different times
to compute on processor. By measuring such timings, it is be possible to know about a
particular computation the processor is carrying out. For example, if the encryption
takes a longer time, it indicates that the secret key is long.
Power Analysis Attacks − These attacks are similar to timing attacks except that the
amount of power consumption is used to obtain information about the nature of the
underlying computations.
Fault analysis Attacks − In these attacks, errors are induced in the cryptosystem and
the attacker studies the resulting output for useful information.
Acoustic cryptanalysis - attacks that exploit sound produced during a computation
(rather like power analysis).
Data Remanence - in which sensitive data are read after supposedly having been
deleted. (i.e. Cold boot attack)
b   • Manage and control network traffic: Firewalls filter incoming and outgoing traffic
based on predefined security rules, ensuring that only authorized traffic is allowed
.
through.
•   Packet Inspection:
• A process used in network security to analyze and monitor data packets
transmitted over a network.
•   Source IP address and Source port
Q   •   Destination IP address and Destination port
5   •   IP protocol
•   Packet header information (sequence numbers, checksums, data flags,
CO   payload information, and so on)   [10
-   •   Connections and State:   ]
5;   •   Connections refer to the established communication links between devices
BL-   on a network.
3   •   Stateful Packet Inspection:
• A firewall technology that tracks the state of active connections and makes
filtering decisions based on the context of the traffic.
•   Authenticate access: They can verify the identity of users and devices trying to access
the network, helping to ensure that only legitimate users gain entry.
•   Input of a username and password to access firewall.
• Use of certificates and public keys
•   Authentication can be handled through the use of pre-shared keys
********** 11 **********
--- page 12 ---
•   Act as an intermediary: Firewalls can serve as intermediaries between internal networks
and external networks, allowing secure communication while monitoring and controlling
data flow.
• A proxy functions by effectively mimicking the host it is trying to protect.
•   In many cases, this function as a proxy is complemented by using a firewall that is
capable of inspecting the actual application data to ensure that it is legitimate and
non-malicious data.
• When functioning in this manner, the firewall is known as working as an
application proxy
•   Protect resources: By blocking unauthorized access and potential threats, firewalls help
safeguard sensitive data and network resources from attacks.
•   Service control: Determines the types of Internet services that can be accessed,
inbound or outbound
•   Direction control: Determines the direction in which particular service requests
are allowed to flow
•   User control: Controls access to a service according to which user is attempting to
access it
•   Behavior control: Controls how particular services are used (e.g., it may enable
external access to only a portion of local information).
• Record and report on events: Firewalls log traffic and security events, providing
valuable insights for security monitoring and incident response, helping organizations
detect and analyze suspicious activities.
•   Console notification: presents a notification to the console. The drawback of this
method is that it requires someone to be actively monitoring the console to check
for alarms.
•   Simple Network Management Protocol (SNMP) notification: used to generate
traps that are sent to the network management system (NMS) that is monitoring
the firewall.
•   Paging notification: When an event occurs, send a page to an administrator. It can
be numeric or alphanumeric, depending on the type of pager carried by the
administrator.
E-mail notification: Similar to paging, here the firewall sends an e-mail to the registered e-
mail address.
a. The hacker group's campaign against ShopEasy follows a structured attack lifecycle,
with each phase aligning to a specific tactic and technique within the MITRE ATT&CK
framework.
1.   Reconnaissance via Active Scanning: The attack begins with the Reconnaissance
phase. The adversaries perform Active Scanning to systematically probe ShopEasy's
Q   internet-exposed network surfaces, identifying vulnerable services and weak points for
6   exploitation.
CO   [10
2.   Initial Access via Phishing: To gain their first foothold inside the network, the
-   ]
1;   group moves to the Initial Access phase. They use Phishing, crafting targeted emails to
BL-
3   deceive an employee into executing malicious code or revealing their login credentials,
thereby breaching the perimeter.
3.   Persistence via a Web Shell: Once initial access is achieved, the attackers focus
on Persistence to ensure they can maintain access even if the initial point is closed. They
install malware, specifically a Web Shell, on an internal server. This acts as a secret
backdoor, providing them with reliable, long-term remote control.
********** 12 **********
--- page 13 ---
4.   Collection from Information Repositories: With a firm foothold, the group
proceeds to their primary goal of data theft in the Collection phase. They specifically
target and exfiltrate Data from Information Repositories, which in this case is the
sensitive customer database.
5.   Impact via Data Encryption: Finally, to maximize damage and extort money,
they launch an Impact attack. They deploy ransomware to execute Data Encrypted for
Impact, crippling ShopEasy's operations by encrypting critical servers and demanding
a ransom for their restoration. This end-to-end attack chain demonstrates a progression
from external probing to data theft and culminating in a disruptive ransomware event.
The attack follows a classic kill chain:
1. The attacker gathers information (Reconnaissance).
2. They gain a foothold (Initial Access).
3. They secure their access for the future (Persistence).
4. They locate and take the target data (Collection).
5. They disrupt business operations for extortion (Impact).
This mapping helps defenders understand the adversary's playbook, allowing them to
implement detections and mitigations for each specific technique.
b   Steps:
•   Step1 :Identify valuable assets of the organization
.
•   Step2: Identify any risks to those assets.
•   Step3: Determine how likely each risk can occur.
•   Step4: Take some action to manage the risk.
Step 1: Identify the information assets in your organization (hardware, software, and data)
and place values on them.
• Most common valuation methods include the following:
•   Replacement cost valuation puts a dollar value on an asset corresponding to the
cost that the organization would incur if the asset had to be replaced at market
prices.
Q   •   Original cost valuation uses the original purchase price of an asset as that asset's
value.
6
•   Depreciated valuation use the original cost minus some allowance for the
CO   deterioration in value of the asset since the time it was purchased.   [10
-   •   Qualitative valuation assign priorities to assets based upon their value to the   ]
4;   organization.
BL-
Step 2: Identify the risks facing those assets. Some key risk assessment terms:
3   • A Vulnerability is a weakness in a system that may be exploited to degrade or
bypass standard security mechanisms. e.g. a system does not have antivirus
software would constitute vulnerability.
• A Threat is a set of external circumstances that may allow a vulnerability to be
exploited. e.g. the existence of a particular virus represents a threat to a system.
• A Risk occurs when a threat and a corresponding vulnerability both exist. e.g.
the threat of a particular virus + the vulnerability of a system
•   without antivirus software combines to constitute a risk to that system.
•   There are two major classifications of risk assessment techniques:
•   Qualitative risk assessment
•   Quantitative risk assessment.
Step 3: Determine How Likely Each Risk Can Occur :
********** 13 **********
--- page 14 ---
• Purpose: Assess the probability and frequency of each identified risk to
prioritize mitigation efforts.
• Process:
o Use qualitative methods (low, medium, high) or quantitative methods
(statistical analysis, historical data) to estimate likelihood.
o Consider factors such as previous incidents, exposure level, and
vulnerability severity.
o Rank risks based on their probability and potential impact.
Step 4: Take Some Action to Manage the Risk
• Purpose: Implement measures to mitigate, transfer, accept, or avoid risks to
protect assets.
• Process:
o Mitigation: Install firewalls, encryption, backups, or access controls.
o Transfer: Use insurance or outsource certain functions.
o Acceptance: Decide to accept low-impact, low-likelihood risks.
o Avoidance: Stop activities that expose critical assets to high risks.
o Continuously monitor and update mitigation strategies to address new
threats.
Q   a. Key Characteristics of a Worm   [10
7   A computer worm possesses three key characteristics that make it particularly   ]
CO   dangerous:
-
1;   1. Self-Replication: Unlike a virus, which requires a user to execute a host file, a worm
BL-
3   can independently copy itself from one system to another without any human
interaction.
2. Network Propagation: It spreads automatically across a network by exploiting
vulnerabilities in operating systems, applications, or through weak security
configurations. It does not need to attach itself to a software program.
3. Autonomous Execution: Once it has infiltrated a system, it can activate and run on
its own, carrying out its malicious payload.
Two Specific Technical Controls for Prevention
To prevent this worm from infecting company systems, the following technical controls
are critical:
1. Aggressive and Centralized Patch Management:
Action: Immediately deploy the official security patch for the specific operating system
vulnerability the worm exploits. This must be done across all affected devices—servers,
workstations, and network equipment.
How it Prevents the Worm: A worm relies on unpatched vulnerabilities to gain entry.
By applying the patch, you eliminate the very weakness the worm is designed to exploit,
rendering it ineffective. A centralized management system ensures no device is missed.
2. Network Segmentation with Strict Firewall Rules:
********** 14 **********
--- page 15 ---
Action: Divide the corporate network into smaller, isolated segments using internal
firewalls or VLANs. Configure firewall rules to block all unnecessary traffic between
these segments.
How it Prevents the Worm: Even if the worm infects one machine in one segment,
network segmentation acts as a barrier, containing the outbreak and preventing it from
spreading laterally to critical systems in other segments
Q   b   Ethical Hierarchy in Cybersecurity Decision-Making: The ethical hierarchy provides a [10
layered approach for evaluating actions and their broader impact:
7   .   ]
CO
-
3;
BL-
3
The ethical hierarchy refers to the structured prioritization of ethical considerations that
professionals use to influence their decisions in cybersecurity as follows
• Humanity Ethics: The primary ethical responsibility is to provide universal human
values that apply across all professions. Cybersecurity professionals must prioritize
actions that protect user integrity, privacy, and safety. Decisions should reflect
compassion, justice and integrity when the human safety is at risk.
•   Professionalism Ethics: professional responsibilities shared across different fields. It
emphasizes acting ethically, competently, and with concern for the public good.
In cybersecurity, this includes being transparent about risks, responsibly handling
vulnerabilities, and contributing to the security and trust of digital systems for societal
benefit.
•   Professions Ethics: the unique ethical standards, rules and codes of conduct established
by professional bodies. In Cybersecurity, professionals must follow industry-specific
guidelines, policies, and legal requirements while ensuring their conduct aligns with the
broader principles of professionalism and humanity.
•   Ethical Principles in Cybersecurity: Two primary ethical frameworks guide moral
reasoning in cybersecurity decisions:
•   Teleological (Consequence) Ethics: Focuses on the ethical value of an action
is determined by its outcomes.
•   Deontological (rule-Based) Ethics: Focuses on fulfilling one’s professional
and moral obligations, regardless of outcomes.
********** 15 **********
--- page 16 ---
Consequence-based Rule-based

Individual Based on consequences to Based on rules acquired by
individual the individualfrom religion,
experience, analysis
Universal Based on consequences to all | Based on universal rules,
of society evident to everyone

FRR ICR 7 6 AC OH
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper c4096d43d94b

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_IT_7001/Information Systems Security/ANS_Information Systems Security(702IT0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Cybersecurity Fundamentals
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a. A replay attack on an authentication system involves an attacker intercepting valid
authentication data and re-transmitting it to impersonate a legitimate user and gain
unauthorized access. The simplicity of this attack—which can succeed even if the
data is encrypted—makes robust countermeasures critical.
CO-1;   Countermeasures for replay attacks
BL- 2   • Timestamps
• Nonces
• Challenge-response authentication
• One-time passwords (OTPs)
• Secure communication protocols
b.   • Lack of understanding
• Lack of physical evidence
CO-3   • Lack of recognition of assets
BL-2   • Lack of political impact
• Complexity of case
• Age of defendant
CO-1   c. An advanced persistent threat (APT) uses multiple phases to break into a network,
BL-2   avoid detection, and harvest valuable information over the long term.
********** 1 **********
--- page 2 ---
d.   •   Intent
• The DBMS gathers the resources it needs to perform the update.
• Commit
• The commit flag means that the DBMS has passed the point of no
return. After committing, the DBMS begins making permanent
changes.
The two-phase commit (2PC) mechanism improves security by ensuring the
CO-2   integrity and consistency of data across a distributed database system. While not a
BL-2   traditional security control like a firewall, 2PC defends against a specific class of
vulnerabilities related to data corruption and inconsistent states that could be
exploited by an attacker or cause severe business damage.
How two-phase commit improves security?
• Preventing data integrity attacks
• Maintaining data consistency
• Protecting against certain failure-based attacks
A    To trust any program, we base our trust on rigorous analysis and testing,   [10]
looking for certain key characteristics:
 Functional correctness. The program does what it is supposed to,
and it works correctly.
 Enforcement of integrity. Even if presented erroneous commands or
commands from unauthorized users, the program maintains the
correctness of the data with which it has contact.
Q2    Limited privilege. The program is allowed to access secure data, but
CO-2   the access is minimized and neither the access rights nor the data are
BL-2   passed along to other untrusted programs or back to an untrusted
caller.
 Appropriate confidence level. The program has been examined and
rated at a degree of trust appropriate for the kind of data and
environment in which it is to be used.
 A defined policy that details what security qualities it enforces
 Appropriate measures and mechanisms by which it can enforce that security
adequately
********** 2 **********

[Text in pictures on this page, read by OCR]
1. RECONNAISSANCE 4, CAPTURE

Attacker leverages information froma Attackers access unprotected systems
variety of factors to understand their and capture information over an
target. extended period.

They mi Iso install malware t retl
2. INCURSION ley may also instal jare to secretly

acquire data or disrupt operations.
Attackers break into network by using
social engineering to deliver targeted 5. EXFILTRATION
malware to vulnerable systems and

people. Captured information is sent back to

attack team’s home base for analysis and
3. DISCOVERY further exploitation fraud—or worse.

Once in, the attackers stay “low and
slow” to avoid detection.

They then map the organization's
defenses from the inside and create a
battle plan and deploy multiple parallel
kill chains to ensure success.
--- page 3 ---
 Independent scrutiny or evaluation to ensure that the mechanisms have
been selected and implemented properly so that the security policy is in fact
enforced.
How Trusted Systems Improve Cybersecurity
• Prevent Unauthorized Access: By enforcing strong authentication and
access controls, trusted systems stop attackers from gaining unauthorized
entry.
• Ensure Data Integrity: Prevent tampering with data, which is critical for
trustworthy operations, especially in financial or healthcare systems.
• Enable Accountability: Auditing allows tracing actions back to their source,
deterring malicious behavior and aiding in incident response.
• Limit Damage: Isolation and minimal TCB reduce the impact of a breach
by containing attacks within limited parts of the system.
• Increase Reliability: Fault tolerance ensures the system remains
operational, which is essential during an attack or failure.
• Build User Confidence: Users and organizations can trust that the system
behaves securely, fostering adoption and compliance.
B   ▪ Data within IP packet is encrypted, but header information is not   [10]
▪ Allows user to establish secure link directly with remote host, encrypting
only data contents of packet
▪ Two popular uses:
▪ End-to-end transport of encrypted data
▪ Remote access worker connects to office network over Internet by
connecting to a VPN server on the perimeter
CO- 2
BL-2
A   ▪ Combines packet filtering router with separate, dedicated firewall such as an [10]
application proxy server
▪ Allows router to prescreen packets to minimize traffic/load on internal proxy
▪ Separate host is often referred to as bastion host; can be rich target for
external attacks and should be very thoroughly secured
Q3   ▪ Advantages:
CO- 2   ▪ Adds an additional layer of defense.
BL-2   ▪ Bastion host can provide detailed traffic inspection and logging.
▪ Limits direct access to the internal network.
▪ Disadvantages:
▪ Single point of failure: bastion host can be targeted heavily.
▪ Performance bottleneck if the bastion host is overwhelmed.
▪ More complex than a simple screening router.
********** 3 **********
--- page 4 ---
B Five Threats:   [10]
1. Impersonation/Fake Login: Someone other than the enrolled student logs
in to take the exam.
2. Man-in-the-Middle Attack: An attacker intercepts exam data transmission
and manipulates answers or steals information.
3. Denial of Service (DoS): Attackers overwhelm the system, preventing
students from logging in or submitting exams on time.
4. Data Tampering: Altering exam questions or student answers either during
transmission or in storage.
5. Privacy Breach: Unauthorized access to students’ personal data and exam
results.
CO-1   Countermeasures:
BL-4
• Implement multi-factor authentication (MFA) to verify student identity
beyond just username/password.
• Use end-to-end encryption (SSL/TLS) to protect data during transmission.
• Deploy firewalls and traffic filtering to mitigate DoS attacks and maintain
system availability.
• Use digital signatures and audit logs to ensure data integrity and detect
tampering.
• Enforce strict access controls and regular security audits to protect
sensitive student data.
Note: there may be other threats as well as countermeasures.
Each appropriate threat explanation- 5 Marks
Counter measures – 5 Marks
A    Encrypted virus: A portion of the virus creates a random encryption [10]
key and encrypts the remainder of the virus. The key is stored with
the virus.
 Stealth virus: A form of virus explicitly designed to hide itself from
Q4   detection by antivirus software. Thus, the entire virus, not just a
CO-1   payload is hidden.
BL-2    Polymorphic virus: A virus that mutates with every infection,
making detection by the “signature” of the virus impossible.
 Metamorphic virus: As with a polymorphic virus, a metamorphic
virus mutates with every infection. The difference is that a
metamorphic virus rewrites itself completely at each iteration,
********** 4 **********
--- page 5 ---
increasing the difficulty of detection. Metamorphic viruses may
change their behavior as well as their appearance.
B   •   Ethical challenges in balancing security with other values   [10]
•   Ethical challenges in threat/incident response
•   Ethical challenges in security breach/vulnerability
•   Ethical challenges in network monitoring and user privacy
•   Ethical challenges with competing interests & obligations
CO-3   •   Ethical challenges in data storage and encryption
BL-2   •   Ethical challenges in IoT, smart grid, and product design
•   Ethical challenges with accountability for cybersecurity
•   Ethical challenges in security research and testing
• Understanding broader impacts of cybersecurity practice
Appropriate Explanation of any five ethical challenges – 2 marks each.
A    DAC is also called identity-based access control (IBAC) or authorization- [10]
based access control
 A system that employs DAC allows the owner or creator of an object to
control and define subject access to that object.
 Access is granted or denied in a discretionary environment based on the
identity of the subject.
 DACs are often implemented using access control lists (ACLs) on objects.
 Discretionary access control does not offer a centrally controlled
Q5   management system because owners can alter the ACLs on their objects.
CO-2   Thus, access is more dynamic than it is with mandatory access controls.
BL-2    Advantages
 Simplicity, flexibility and ease of implementation
 Drawback
 There is no formal assurance concerning the flow of information
 Examples for DAC
 Passwords for file access
 Owner/Group/Other
 Access control lists (ACL)
B A buffer overflow is a software vulnerability where a program writes more data to a [10]
memory buffer than it was allocated, causing the excess data to "overflow" and
overwrite adjacent memory locations. Attackers can exploit this error to gain
unauthorized access, crash systems, or execute malicious code.
char sample[10];
for (i=0; i<=10; i++) sample[i] = ‘A’;
Last ‘A’ goes into user data, user code, system data, or system code
CO-1   If data is overwritten, can affect results
BL-2   If system is overwritten, unpredictable results
Countermeasures:
 Use secure programming languages like Java or C#.
 Use secure functions in C/C++ like strncpy instead of strcpy.
 Audit code properly.
 Make stack non executable.
 Use safe C compliers or safe libraries that check the memory access at run
time.
 Hardware solutions like use of register to store return address have been
proposed.
********** 5 **********
--- page 6 ---
A The Secure Systems Development Lifecycle (SSDLC) is an enhanced version of the [10]
traditional Systems Development Lifecycle (SDLC) that intentionally integrates
security activities and considerations into every phase of development. The core
purpose is to "shift security left," meaning to address vulnerabilities and risks early
in the process, rather than leaving them as a final consideration before deployment.
Investigation
The investigation of the SecSDLC begins with a directive from upper management,
dictating the process, outcomes, and goals of the project, as well as the constraints
placed on the activity.
Frequently, this phase begins with a statement of program security policy that
outlines the implementation of security.
Teams of responsible managers, employees, and contractors are organized, problems
are analyzed, and scope is defined, including goals, objectives, and constraints not
covered in the program policy.
Finally, an organizational feasibility analysis is performed to determine whether the
organization has the resources and commitment necessary to conduct a successful
security analysis and design.
Analysis
In the analysis phase, the documents from the investigation phase are studied.
The development team conducts a preliminary analysis of existing security policies
or programs, along with documented current threats and associated controls.
This phase also includes an analysis of relevant legal issues that could impact the
design of the security solution.
The risk management task – identifying, assessing and evaluating the levels of risk
Q6   facing the organization – also begins in this stage.
CO-2   Logical Design
BL-2   The logical design phase creates and develops the blueprints for security, and it
examines and implements key policies that influence later decisions.
Also at this stage, critical planning is developed for incident response actions to be
taken in the event of partial or catastrophic loss.
Next, a feasibility analysis determines whether or not the project should continue or
should be outsourced.
Physical Design
In the physical design phase, the security technology needed to support the blueprint
outlined in the logical design is evaluated, alternative solutions are generated, and
a final design is agreed upon.
The security blueprint may be revisited to keep it synchronized with the changes
needed when the physical design is completed.
Criteria needed to determine the definition of successful solutions is also prepared
during this phase.
Included at this time are the designs for physical security measures to support the
proposed technological solutions.
At the end of this phase, a feasibility study should determine the readiness of the
organization for the proposed project, and then the champion and users are presented
with the design.
At this time, all parties involved have a chance to approve the project before
implementation begins.
Implementation
The implementation phase is similar to the traditional SDLC.
The security solutions are acquired (made or bought), tested, implemented, and
tested again.
********** 6 **********
--- page 7 ---
Personnel issues are evaluated, and specific training and education programs are
conducted.
Finally, the entire tested package is presented to upper management for final
approval.
Maintenance and Change
The maintenance and change phase, though last, is perhaps most important, given
the high level of ingenuity in today’s threats.
The reparation and restoration of information is a constant duel with an often-unseen
adversary.
As new threats emerge and old threats evolve, the information security profile of an
organization requires constant adaptation to prevent threats from successfully
penetrating sensitive data
Advantages:
•   Identifies and remediates vulnerabilities early
• Reduces costs and improve efficiency
• Creates a security-aware cultures
• Strengthens compliance and governance
• Protects against advanced threats
B Defense in depth:   [10]
The principle of "defense in depth" is a cybersecurity strategy that uses multiple,
overlapping security controls to protect an organization's systems and data. The core
idea, which comes from a military concept, is that if one layer of defense fails,
another layer is in place to provide a backup and stop the threat from causing
significant damage.
This approach assumes that no single security control is foolproof and that a
determined attacker may eventually breach one line of defense. By layering various
safeguards, a defense-in-depth strategy creates redundancy, significantly increasing
the difficulty and complexity for an attacker to succeed.
Separation of privilege principle:
No single person should have enough authority to cause a critical event to happen
Many examples from outside of computing, e.g., two keys needed to launch a missile
CO-2
Tradeoff between security gained and manpower required to achieve it
BL-2
CIO should not have access to all systems
DBA should not have access to encryption key
Example:
•Accountant with privilege to write check as well as balance the businesses account
is potential for abuse
Least privilege principle
 An individual should have only the minimum level of access controls
necessary to carry out job functions
 A common violation of this principle occurs because of administrator
inattention
•Users are placed in groups that are too broad
 Another common violation occurs because of privilege creep
•Users are granted new privileges when they change roles without reviewing
existing privileges
Q7   A Simple Security Property ("no read up")   [10]
CO-2
********** 7 **********
--- page 8 ---
BL-2   • A subject cannot read data at a higher security level than its own
clearance.
• Example: A user cleared for Secret cannot read Top Secret documents.
• This prevents leakage of sensitive information to lower clearance levels.
Star Property ("no write down")
• A subject cannot write information to a lower security level.
• Example: A user cleared for Top Secret cannot write data into a Secret or
Confidential file.
• This prevents confidential information from being leaked down to less
secure levels.
Discretionary Security Property
• Access is also controlled by discretionary access control (DAC)
mechanisms — like file permissions — on top of mandatory controls.
How This Ensures Confidentiality
• The "no read up" rule prevents unauthorized access to sensitive
information by users without the proper clearance.
• The "no write down" rule prevents sensitive information from being
leaked to lower security levels where unauthorized users might access it.
•   Together, these rules restrict information flow, maintaining strict control
over who can see or transmit sensitive data, effectively preventing
unauthorized disclosure.
CO-2 B   ▪ Network-Based, which monitors network traffic for particular network [10]
BL-3   segments or devices and analyses the network and application protocol
activity to identify suspicious activity.
▪ Wireless, which monitors wireless network traffic and analyses it to
identify suspicious activity involving the wireless networking
protocols themselves.
▪ Network Behaviour Analysis (NBA), which examines network traffic
to identify threats that generate unusual traffic flows, such as DDoS
attacks, scanning, and certain forms of malware.
Recommendation:
Network Based IDPS
Justification:
********** 8 **********

[Text in pictures on this page, read by OCR]
Host IDS: Examines the data in files stored on host
and alerts systems administrators of changes

External router

Untrusted
network

Network IDS: Examines packets on network
and alerts administrators of unusual patterns

Intrusion Detection Systems
--- page 9 ---
Deploy and Configure the NIDPS at the network perimeter to monitor traffic
coming into your company’s web servers.
Apply signature-based rules to detect known DDoS attack patterns like SYN
floods.
Set thresholds for traffic volume to identify abnormal spikes indicating
possible attacks.
When suspicious traffic is detected, use the NIDPS’s prevention capability to
block malicious IPs in real-time.
Continuously monitor logs and alerts from the NIDPS to verify if the attack
has been mitigated and ensure normal traffic resumes.
********** 9 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 048434be324f

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/MBATech_IT_7041/Information Systems Security/ANS_Information Systems Security(702IT0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (IT)/MBA Tech (IT)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Information Systems Security
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure on the right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary
Q
Answer briefly:
1
a. The components of a program level policy
Purpose includes the objectives and goals of the program,
▪ Security needs related to CIA
▪   E.g., Mission critical database- reduction in error, data loss/corruption, data
recovery will be stressed upon
▪   E.g., Confidential Data- Data protection mechanism against unauthorized
CO -   disclosure
1;   [05]
BL-   Scope resources covered by the policy. coverage may include: facilities, hardware,
2
software, information, personnel
Responsibilities to manage and implement policy are assigned. Distinguishes
providers, managers and consumers.
Compliance ensures policy's enforcement. Includes two issues
▪ General compliance – meeting requirements
▪ Use of specified penalties and disciplinary actions.
b. Goals of cryptography
▪ Confidentiality
CO -
2;   ▪   Integrity   [05]
BL –
2   ▪ Non repudiation
▪ Authentication
********** 1 **********
--- page 2 ---
▪ Appropriate explanation with an example 4*1.25 = 5 Marks
c.
CO -
5;   [05]
BL –
2
Appropriate explanation of each factor = 3*1.5 = 4.5 marks
Example – 0.5 mark
d. ▪ Data Collection
▪ Examination
▪ Analysis
▪ Reporting
CO -
3;   [05]
BL-
2
a. Issue-Specific Social Media Policy: Protection of Intellectual Property
Policy Number: HR-SOCIAL-2.1
Effective Date: ____
Q   Policy Owner: Chief Information Security Officer (CISO)
2   1.0 Purpose
[10]
CO -   This policy establishes clear guidelines to prevent the inadvertent disclosure of
1;
BL-   confidential company information, trade secrets, and intellectual property (IP) on
3
social media platforms, stemming from incidents involving well-intentioned but high-
risk employee posts.
2.0 Scope
********** 2 **********

[Text in pictures on this page, read by OCR]
Knowledge Possession Inherence

Factor Factor Factor
(something you know) | (something you have) (something you are)
—
YN
HHH
@
Password Smartphone Fingerprint
.
(?) =
Cy
oo)
'
Security Question Smart Card Retina Pattern
Ca
1234 (| OS
L* J

PIN Hardware Token Face Recognition
--- page 3 ---
This policy applies to all employees, contractors, and interns of _____ when
referencing the company, its projects, or its work environment in any personal or
professional social media activity.
3.0 The "Clean Zone" Rule for Photos and Videos
Before capturing or sharing any image or video in a company workspace (including
offices, home offices, and labs), employees must:
3.1 Clear All Backgrounds: Ensure whiteboards, monitors, sticky notes, notebooks, and
printed documents are entirely erased, cleared, or removed from the camera's field of
view. A "clean" background must be confirmed before posting.
3.2 Sanitize Screen Content: All computer monitors in the frame must be turned off or
display a neutral, non-informative screen (e.g., a login screen or company logo). No
code, data, architectural diagrams, or internal applications may be visible.
4.0 The "No Operational Secrets" Rule for Posts and Discussions
Employees are prohibited from describing, hinting at, or discussing specific internal
systems, technologies, or projects. This includes, but is not limited to:
4.1 Technical Details: Do not reference algorithms, code, data flows, security
measures, system architectures, or unreleased product features.
4.2 Project-Specific Information: Do not mention project codenames, internal
performance metrics, or specific technical challenges related to confidential projects.
4.3 Approved Messaging: When in doubt, employees must use only pre-approved,
high-level public messaging from the Corporate Communications department.
5.0 Mandatory Pre-Post Review for Technical Staff
5.1 Affected Roles: All employees in Engineering, R&D, Data Science, IT, Security,
and Product Management roles must submit any social media post that discusses their
work (even in general terms) for review.
5.2 Review Process: Submission must be made via the dedicated `social-
review@company.com` channel at least 48 hours prior to intended posting. Approval
from both Communications and the CISO's office is required.
6.0 Violations
Violations of this policy will be treated seriously and may result in disciplinary action,
up to and including termination of employment, and potential legal action if company
IP is compromised.
Q   b. Risk Analysis and Recommendation
2   a) Single Loss Expectancy (SLE)   [10]
CO -   SLE = Asset Value (AV) × Exposure Factor (EF) = $500,000 × 0.30
4;
********** 3 **********
--- page 4 ---
BL-   SLE = $150,000
3   b) Annualized Loss Expectancy (ALE) without IPS
ALE = SLE × Annual Rate of Occurrence (ARO)
ARO without IPS: Once every 2 years = 0.5
ALE = $150,000 × 0.5
ALE (without IPS) = $75,000
c) Annualized Loss Expectancy (ALE) with IPS
ARO with IPS: Once every 10 years = 0.1
ALE = $150,000 × 0.1
ALE (with IPS) = $15,000
d) Annual Benefit of the IPS
Benefit = ALE (without IPS) - ALE (with IPS) = $75,000 - $15,000 = $60,000
e) Recommendation and Justification
Recommendation: Yes, the bank should purchase and implement the Intrusion
Prevention System (IPS).
Justification: The financial analysis demonstrates a clear and compelling return on
investment.
The IPS provides an annual risk reduction benefit of $60,000.
The annualized cost of the IPS is $15,000.
Therefore, the net annual saving for the bank is $60,000 - $15,000 = $45,000.
By spending $15,000 annually on the IPS, the bank avoids an expected annual loss of
$75,000, reducing it to an expected annual loss of $15,000. This results in a net positive
financial impact, making the IPS a cost-effective security control.
a. Explain Diffie Hellman Key exchange algorithm. Alice and Bob have selected two
prime numbers as 11 and 23. Alice select 6 and Bob select 15 as the secret numbers or
private keys. Compute the key that Alice and Bob should use.
Q
3
[10]
CO -
2;
BL-
3
A= 116mod 23 = 9
********** 4 **********

[Text in pictures on this page, read by OCR]
. Firstly, Alice and Bob agree on two large prime numbers, n and g. These two integers need not
be kept secret. Alice and Bob can use an insecure channel to agree on them.

. Alice chooses another large random number x, and calculates A such that:
A=g* modn

. Alice sends the number A to Bob.

. Bob independently chooses another large random integer y and calculates B such that:
B=g’ modn

. Bob sends the number B to Alice.

. A now computes the secret key K1 as follows:
K1 = BX mod n
. B now computes the secret key K2 as follows:
K2 = AY mod n
--- page 5 ---
B = 1115 mod 23 = 10
K1 = 106 mod 23 =6
K2 = 915 mod 23 =6
Appropriate explanation – 6 Marks
Calculation of A, B, K1 and K2 – 1 mark each
b. Brute force attack: An attacker tries many username and password combinations
repeatedly to guess the correct credentials.
Dictionary attacks: Trial-and-error from a list of potential passwords
1. Account lockout: Temporarily lock accounts after a few failed login attempts.
2. Rate limiting: Limit the number of login attempts from a single IP address.
3. Strong password policies: Enforce complex passwords to reduce guessability.
4. Multi-factor authentication (MFA): Add an extra layer of security beyond
passwords.
5. Detect and block suspicious IPs: Monitor and block IPs with multiple failed
Q
attempts.
3
6. Encourage unique passwords: Educate users not to reuse passwords.   [10]
CO -
5;   7. Implement MFA: Makes stolen passwords alone insufficient.
BL-
3   8. Use login anomaly detection: Alert or block login attempts from unusual
locations or devices.
9. Password hashing and salting: Securely store passwords to reduce risk in case
of breaches.
10. Backoff Mechanism: A backoff mechanism is a security strategy that
progressively increases the delay between login attempts after a certain number
of failed tries, making online dictionary attacks impractically slow.
Appropriate explanation of brute force and dictionary attack – 6 marks
Countermeasures – 4 marks
a. Explain Clark Wilson model. Consider banking scenario. Identify at-least two UDI,
CDI, TP and IVP.
Q
 The Clark-Wilson integrity model provides a foundation for specifying and
4   analyzing an integrity policy for a computing system.
CO -    The model is primarily concerned with formalizing the notion of information [10]
5;   integrity.
BL-    Information integrity is maintained by preventing corruption of data items in a
3   system due to either error or malicious intent.
 An integrity policy describes how the data items in the system should be kept valid
from one state of the system to the next and specifies the capabilities of various
principals in the system.
 The model defines enforcement rules and certification rules.
********** 5 **********
--- page 6 ---
 Clark and Wilson claimed that the following are four fundamental concerns of any
reasonable commercial integrity model:
   Authentication: identity of all users must be properly authenticated.
   Audit: Modiﬁcations should be logged to record every program executed
and by whom, in a way that cannot be subverted.
   Well-formed transactions: users manipulate data only in constrained
ways. Only legitimate accesses are allowed.
   Separation of duty: the system associates with each user a valid set of
programs they can run and prevents unauthorized modiﬁcations, thus preserving
integrity and consistency with the real world.
 The core of the model is based on the notion of a transaction.
 A well-formed transaction is a series of operations that transition a system
from one consistent state to another consistent state.
 In this model the integrity policy addresses the integrity of the transactions.
 The principle of separation of duty requires that the certifier of a transaction
and the implementer be different entities.
 Establishes a system of access to object by Subject through program and not
directly.
Component   Example in Banking Scenario
- Account balances, Transaction records, Loan details, Customer
CDIs
account information
- User inputs for transactions (e.g., deposit amount), External data
UDIs
(e.g., exchange rates), New account applications
- Funds transfer procedure, Deposit processing, Withdrawal
TPs
processing, Loan approval workflow, Interest calculation program
- Account reconciliation procedures, Audit trail verification,
IVPs
Transaction validation routines, Balance consistency checks
Appropriate explanation – 6 marks
Identifications of components – 4 marks
b. Dual-Homed Host firewalls is a server with two network interfaces that acts as a gateway
between trusted and untrusted network.
Q
4
CO -   [10]
5;
BL-
2   Key Components
• Dual-Homed Host:
– A dedicated server or computer that has two network interfaces (NICs). One
NIC connects to the external network (e.g., the internet), while the other
connects to the internal network.
– The dual-homed host runs firewall software that monitors and controls the
traffic between the two networks.
•   Firewall Software:
********** 6 **********

[Text in pictures on this page, read by OCR]
Dual-homed host
used as a firewall providing Internal filtering
Network Address Translation router
(NAT)

Trusted network

Se , :
- - i - GQ - GS" - - - -- + - :-- 4 ---
: H
Blocked S ; :
aioe internal
saab data packets
data packets

Public IP addresses NAT assigned local addresses

Extemal Proxy access

filtering router

Untrusted
network
--- page 7 ---
– The firewall software on the dual-homed host is responsible for filtering
traffic based on predefined security policies. It can analyze both incoming
and outgoing traffic to ensure only authorized communications are allowed.
•   Architecture Overview
•   Traffic Flow:
– Incoming traffic from the external network first reaches the dual-homed host.
The firewall software inspects the packets based on its rules.
–   If the traffic is deemed safe, it is forwarded to the internal network.
Conversely, outgoing traffic from the internal network is filtered before it is
sent to the external network.
•   Isolation of Networks:
– The dual-homed host serves as a barrier between the internal and external
networks, preventing direct access from the outside to the internal network
resources.
Screened Subnet Firewalls (with DMZ): consists of two or more internal bastion hosts behind
packet filtering router, with each host protecting trusted network:
▪   Connections from outside (untrusted network) routed through external filtering
router
▪   Connections from outside (untrusted network) are routed into and out of
routing firewall to separate network segment known as DMZ
▪   Connections into trusted internal network allowed only from DMZ bastion host
servers
Key Components
•   Screening Router:
– A router that serves as the first line of defense, filtering incoming and
outgoing traffic based on predefined security rules. It typically sits at the
perimeter of the network.
–   It controls traffic between the internet, the DMZ, and the internal network.
• DMZ (Demilitarized Zone):
– A separate network segment that hosts external-facing services (e.g., web
servers, mail servers, FTP servers).
– The DMZ is accessible from both the external network (internet) and the
internal network, but the internal network cannot be accessed directly from
the DMZ.
•   Internal Network:
– The secure area of the network where sensitive data and resources are stored.
It is protected from direct exposure to external traffic.
• Second Firewall:
–   Often, a second firewall is used between the DMZ and the internal network
to provide additional security, filtering traffic that attempts to access the
internal resources from the DMZ.
•   Architecture Overview
•   Traffic Flow:
********** 7 **********
--- page 8 ---
– Incoming traffic from the internet first hits the screening router, which applies
filtering rules.
– Allowed traffic is then forwarded to the DMZ, where public-facing services
reside.
–   If traffic needs to reach the internal network, it must pass through the second
firewall, which enforces strict security policies.
•   Isolation:
– The DMZ acts as a buffer zone, isolating the internal network from the internet.
Even if a service in the DMZ is compromised, the internal network remains
protected.
a. Broad Level steps
Do the following one-time initialization processes:
◦ Expand the 16-byte key to get the actual key block to be used
◦ Do one time initialization of the 16-byte plain text block (called state)
◦ XOR the state with the key block
For each round except final round, do the following:
Q   ◦ Apply S-box to each of the plain text bytes (SubBytes)
5   ◦ Rotate row k of the plain text block (i.e state) by k bytes (ShiftRows).
CO -   ◦ Perform a mix column operation (MixColumns).   [10]
2;   ◦ XOR the state with the key block (AddRoundKey)
BL-   ◦   (Note: in final round MixColumn operation is not performed)
3
Appropriate explanation of algorithm – 6 marks
Steps and Final State – 4 marks
74 26 44
21 A4 21
44 26 74
b. • Trusted VPN
▪ Definition: A Trusted VPN operates over a trusted network infrastructure,
typically provided by a single organization or an entity that both ends of the
VPN trust. This type of VPN relies on the inherent security of the underlying
network.
▪ Key Characteristics:
▪ Trusted Environment: Used in scenarios where both parties (e.g., an
organization and its branch offices) trust the intermediary networks.
▪ Minimal Encryption: May use less stringent encryption methods since the
Q   network is considered secure.
▪ Cost-Effective: Generally, less expensive to implement because it doesn’t
5
require extensive security measures.
CO -   ▪ Use Cases:   [10]
5;   ▪   Internal corporate networks.
BL-
▪ Connections between offices of the same organization.
3   • Secure VPN
▪ Definition: A Secure VPN prioritizes security by utilizing strong encryption
protocols and various security measures to ensure data integrity,
confidentiality, and authentication over potentially untrusted networks (like
the internet).
▪ Key Characteristics:
▪ Robust Encryption: Implements high-level encryption standards (e.g.,
AES) and secure protocols (e.g., OpenVPN, L2TP/IPsec).
▪ Authentication: Enforces strong user authentication mechanisms to ensure
that only authorized users can connect.
********** 8 **********
--- page 9 ---
▪ Data Integrity: Uses techniques to ensure that the data has not been altered
in transit.
▪ Use Cases:
▪ Remote work solutions for employees accessing company networks from
home or public locations.
▪ Secure connections for sensitive transactions (e.g., financial services).
• Hybrid VPN
▪ Definition: A Hybrid VPN combines elements of both Trusted and Secure
VPNs, leveraging the advantages of each to provide a balanced approach to
connectivity and security.
▪ Key Characteristics:
▪ Flexible Security: Can operate in both trusted and untrusted environments,
applying stronger security measures when necessary.
▪ Dynamic Configuration: May adjust its security protocols based on the
type of network it’s operating over.
▪ Cost and Performance Optimization: Offers a balance between security
needs and performance efficiency.
▪ Use Cases:
▪ Organizations with varying security requirements across different branches
or remote users.
▪ Businesses that need to connect secure data centers to less secure locations
while maintaining flexibility.
Q   a.
6
CO -   Student can draw any one phase of SecSDLC.   [10]
1;
BL-
3
b.   Type   Definition   Characteristics   Advantages   Disadvantages
Hot   Site A   fully All   necessary Minimal   - Very high
(Proactive)   equipped   hardware, software, downtime;   cost   due   to
backup   and   network operations   continuous
facility that is configurations are continue   maintenance
Q
always   in place.   almost   and
6
operational   Data   is seamlessly.   infrastructure.
CO -   [10]
4;   and can take continuously   Ideal   for
BL-
over business backed up for real- high-
3
functions   time   availability
immediately   synchronization.   organizations
or   with   Staff can move and   (e.g., banks,
minimal   resume operations financial
downtime.   quickly.   institutions).
********** 9 **********
--- page 10 ---
Warm Site A   partially Basic infrastructure More   cost-   -   Longer
(Preventive) equipped   is in place, not all effective   recovery time
backup   systems are live.   than hot site. compared   to
facility that is Data backups are Provides   hot site.
not   fully regular,   but   not faster
operational   real-time.   recovery
but can be   Requires   setup than   cold
quickly   time   after   site.
configured.   disruption.
Cold   Site A   backup No   Lowest cost Longest
(Reactive)   facility   that equipment/software with minimal recovery time.
only provides installed.   maintenance. Not   suitable
space;   lacks Data   must   be Suitable   if for   critical
pre-installed   restored   from downtime is operations.
infrastructure. external backups.   acceptable.
Q   a. The two security design principles being violated are:   [10]
7   1. Principle of Psychological Acceptability
CO -   Violated by: Rule 1 (complex 5-step authentication for routine tasks)
1;
BL-   This principle states that security mechanisms should not make accessing a resource
3
more difficult than if the mechanism were absent. A 5-step, 2-minute authentication
process frustrates users, reduces productivity, and encourages workarounds (e.g.,
writing down passwords, avoiding the system). Security should balance protection with
usability to ensure compliance and effectiveness.
2. Principle of Least Privilege
Violated by: Rule 2 (full read access to financial data for all employees)
This principle requires granting users the minimum access necessary to perform their
jobs. Providing all employees with unrestricted access to sensitive financial forecasting
data unnecessarily expands the attack surface. For example, an intern or compromised
account could leak or misuse data irrelevant to their role, increasing insider threat risks.
Q   b. Negligence in data handling occurs when an employee fails to follow established [10]
7   security protocols, leading to unauthorized access, disclosure, or loss of sensitive
CO -   information. Even if such actions are unintentional, they can have serious ethical and
3;
BL-   legal repercussions for both the individual and the organization.
3
1. Ethical Consequences: From an ethical standpoint, negligence reflects a failure of
professional responsibility and moral duty.
********** 10 **********
--- page 11 ---
Breach of trust: Employees are ethically bound to protect customer information.
Mishandling data violates the principles of confidentiality,   integrity, and
accountability.
Negligence vs. intent: Even without malicious intent, carelessness shows poor
judgment and disregard for ethical standards.
Damage to reputation: Ethical lapses erode stakeholder trust and harm the
organization’s credibility.
Ethical principles violated:
Deontological ethics – Failing in duty to protect information.
Utilitarian ethics – The harm caused (data misuse, customer distress) outweighs any
good intention.
Legal Consequences: From a legal perspective, negligence in data handling can amount
to a violation of cyber laws and data protection regulations.
Under the Information Technology Act, 2000 (India):
Section 43 (a–c): Prohibits unauthorized access, downloading, or transfer of data.
Section 72A: Penalizes disclosure of personal information without consent or in breach
of a lawful contract.
Legal accountability: The law focuses on the outcome rather than intent; hence, even
unintentional leaks may be considered cybercrimes.
Consequences for employees: Disciplinary action, fines, or criminal liability for breach
of confidentiality.
Consequences for the organization: Legal penalties, regulatory sanctions, financial
losses, and reputational damage under data protection and privacy laws.
Organizational Impact
Financial losses due to lawsuits, fines, or compensations.
Loss of client confidence and potential business contracts.
Increased regulatory scrutiny and compliance burdens.
Need for retraining and policy reinforcement to prevent recurrence.
********** 11 **********
````
