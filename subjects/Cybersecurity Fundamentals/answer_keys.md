# Cybersecurity Fundamentals: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper ffed0043a144

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CyberSecurity_7010/Cybersecurity Fundamentals/ANS_Cybersecurity Fundamentals(702IT0C013)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 Nov 2025
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Semester V(Exam Year: 2025-2026)
Subject: Cybersecurity Fundamentals
Date: 24 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a. A dictionary attack is a method of password hacking where an attacker uses a pre-
generated list of words, phrases, and permutations to guess a user's login credentials.
The attack is automated using software and is highly effective against weak or
predictable passwords that are based on common phrases.
Countermeasures for replay attacks
CO-1;   • Use long and strong passphrases
BL- 2   • Enable multi-factor authentication (MFA)
• Use a password manager
• Avoid password reuse
• Enforce strong password policies
• Limit login attempts (Rate-limiting)
b.   •   Issue 1: Jurisdictional (state to state and federal to state)
•   Issue 2: Computer evidence presentation difficulties
•   Issue 3: Criminal prosecution vs. civil litigation
•   Issue 4: International cooperation in legal practice
CO-3
•   Issue 5: Access and exchange of information
BL-2
•   Issue 6: Confidential records and business systems privacy
•   Issue 7: Privacy protection for data transmission laws
•   Issue 8: Privacy issues and workplace surveillance
•   Issue 9: Interpretation of laws affecting digital evidence
c. Characteristics
 Complete - Address all critical areas of information risk.
 Organized – Policies based on a recognized standard or frameworks (ISO
CO-1
27002)
BL-2
 Documented – Written and maintained with clear ownership and version
history.
 Updated – Periodically reviewed for updates based on the latest risks.
********** 1 **********
--- page 2 ---
 Communicated – Policies are read and understood by all people in the
organization.
d. Data disclosures
 Exact Data
 Bounds
 Negative Result
 Existence
 Probable Value
CO-2    Inference
BL-2   Prevention
 Suppress obviously sensitive information
 Track what the user knows
 Disguise the data
 Data suppression blocks release of sensitive data; data concealing releases
part or an approximation of sensitive data.
A    Trusted Computing Base: everything necessary for a system to enforce its   [10]
security policy.
 TCB Functions
 Process activation. In a multiprogramming environment, activation
and deactivation of processes occur frequently. Changing from one
process to another requires a complete change of registers,
relocation maps, file access lists, process status information, and
other pointers, much of which is security sensitive information.
Q2    Execution domain switching. Processes running in one domain often
CO-2   invoke processes in other domains to obtain more or less sensitive
BL-2   data or services.
 Memory protection. Because each domain includes code and data
stored in memory, the TCB must monitor memory references to
ensure secrecy and integrity for each domain.
 I/O operation. In some systems, software is involved with each
character transferred in an I/O operation. This software connects a
user program in the outermost domain to an I/O device in the
innermost (hardware) domain. Thus, I/O operations can cross all
domains.
********** 2 **********
--- page 3 ---
B   A bastion host, or "jump box," is a specialized server designed and hardened [10]
to withstand attacks.
It acts as a secure, controlled access point for administrators and other
authorized users to access a private internal network from an external,
untrusted network like the internet.
Key Characteristics:
Minimal services: To reduce its attack surface, a bastion host is stripped of
all unnecessary software, ports, and user accounts.
Hardened: It is heavily secured and configured with tight restrictions to
CO- 2
prevent compromise.
BL-2
Logging and monitoring: All activity on the bastion host is meticulously
logged and audited to detect suspicious behavior.
Strong authentication: Access is controlled through strong authentication
methods, such as public-key cryptography (SSH) and multi-factor
authentication (MFA).
Controlled access: The bastion host is configured to only allow specific,
necessary network traffic
A NIST recommends four locations for NIDS sensors:   [10]
Location 1: Behind each external firewall, in the network DMZ
•   IDPS sees attacks that originate from the outside world and may penetrate
the network’s perimeter defenses.
•   IDPS can identify problems with the network firewall policy or
performance.
Q3
•   IDPS sees attacks that might target the Web server or ftp server, both of
CO- 2
which commonly reside in this DMZ.
BL-2
•   Even if the incoming attack is not detected, the IDPS can sometimes
recognize, in the outgoing traffic, patterns that suggest that the server has
been compromised.
Location 2: Outside an external firewall
•   IDPS documents the number of attacks originating on the Internet that target
the network.
********** 3 **********

[Text in pictures on this page, read by OCR]
User applications

Utilities

User request interpreter
User process coordination, synchronization
Non-TCB xs 5
User environment: objects, names (e.g., files)
User /0
Procedures, user processes
Creation and deletion of user objects
Directories
Extended types
Vv Segmentation, paging, memory management

Primitive /O
Basic operations
TCB Clocks, timing
Interrupt handling
Hardware; registers, memory
Vv Capabilities
--- page 4 ---
•   IDPS documents the types of attacks originating on the Internet that target
the network.
Location 3: On major network backbones
•   IDPS monitors a large amount of a network’s traffic, thus increasing its
chances of spotting attacks.
•   IDPS detects unauthorized activity by authorized users within the
organization’s security perimeter.
Location 4: On critical subnets
•   IDPS detects attacks targeting critical systems and resources.
•   Location allows organizations with limited resources to focus these
resources on the network assets considered of greatest value.
B Five Threats:   [10]
1. Credential Theft: Attackers steal employee login credentials to falsify
attendance.
2. Replay Attacks: Someone captures legitimate login data and reuses it to
mark false attendance.
3. Insider Manipulation: Employees or administrators modify attendance
records for personal gain.
4. System Downtime: Server outages prevent accurate attendance recording,
CO-1   causing disputes.
BL-4   5. Data Leakage: Attendance data exposed to unauthorized parties, violating
privacy.
Countermeasures:
• Use strong password policies and MFA to prevent unauthorized access.
• Implement nonce-based authentication or token expiration to prevent
replay attacks.
• Maintain immutable logs and segregation of duties to detect and prevent
insider manipulation.
********** 4 **********
--- page 5 ---
• Ensure redundant servers and failover mechanisms to maintain system
uptime.
• Encrypt attendance data in transit and at rest, and limit data access based on
roles
Note: there may be other threats as well as countermeasures.
Each appropriate threat explanation- 5 Marks
Counter measures – 5 Marks
A Phases:   [10]
Dormant phase: The virus is idle. The virus will eventually be activated by some
event, such as a date, the presence of another program or file, or the capacity of the
disk exceeding some limit. Not all viruses have this stage.
Propagation phase: The virus places a copy of itself into other programs or into
certain system areas on the disk. The copy may not be identical to the propagating
version; viruses often morph to evade detection. Each infected program will now
contain a clone of the virus, which will itself enter a propagation phase.
Triggering phase: The virus is activated to perform the function for which it was
intended. As with the dormant phase, the triggering phase can be caused by a variety
of system events, including a count of the number of times that this copy of the virus
Q4   has made copies of itself.
CO-1   Execution phase: The function is performed. The function may be harmless, such
BL-2   as a message on the screen, or damaging, such as the destruction of programs and
data files.
Virus prevention:
 Use only commercial software acquired from reliable, well-established
vendors
 Test all new software on an isolated computer
 Open attachments only when you know them to be safe
 Make a recoverable system image and store it safely
 Make and retain backup copies of executable system files.
 Use virus detectors daily and update them regularly
B   ▪ Hacking (Under Section 66 ITAA 2008)   [10]
▪ Denial of Service (DoS) attack or Distributed Denial-of-Service (DDoS)
attack
▪ Spreading viruses and malware (Under Section 66 of ITAA,2008 or Sec.66F
ITAA,2008 in case if it is done against country or to strike terror in the
people)
CO-3
▪ Website defacement(Under Section 66 of ITAA 2008 or Sec.66F ITAA,2008
BL-2
in case if it is done against country or to strike terror in the people)
▪ Cyber terrorism (Under Section 66F of ITAA 2008)
▪ Spoofing (Under Section , 66D of ITAA 2008
▪ Skimming (Under Section 66C of ITAA 2008)
▪ Spamming(Under Section of 67 ITAA 2008)
A    Systems that employ role-based or task-based access controls define the [10]
Q5   ability of a subject to access an object through the use of subject roles (i.e.,
CO-2   job descriptions) or tasks (i.e., work functions).
BL-2      If a subject is in a management position, they will have greater access to
resources than someone who is in a temporary position.
********** 5 **********
--- page 6 ---
 Role-based access controls are useful in environments with frequent
personnel changes because access is based on a job description (i.e., a role
or task) rather than on a subject’s identity.
 Note the difference between groups and roles: groups define sets of users
while roles define sets of privileges.
 Advantages:
 Authorization management
 Hierarchical roles
 Based on well known security principles of
 Least privilege
 Separation of duties
B Privilege escalation is the unauthorized act of a user or program gaining higher-level [10]
permissions than they were initially granted. An attacker who has already breached
a system, even with low-level access, will attempt privilege escalation to gain full
control and carry out more destructive actions.
This escalation can be achieved through software vulnerabilities, system
misconfigurations, or exploiting weak access controls. Attackers use privileged
access to steal sensitive data, deploy malware, or maintain a persistent backdoor into
the network.
CO-1   Mitigation
BL-2   • Access and identity management
• Implement multi-factor authentication (MFA)
• Use Privileged Access Management (PAM)
• Disable or secure default and unused accounts
• Apply patches promptly
• Harden all systems
• Monitor user and system activity
• Employee awareness
A The six NIST CSF functions   [10]
• Govern (GV): Introduced in CSF 2.0, this function sets the foundation for an
organization's cybersecurity program by aligning it with the overall mission,
objectives, and legal requirements. It includes categories like Risk
Q6
Management Strategy and Organizational Context.
CO-2
•   Identify (ID): This function involves understanding the organization's
BL-2
systems, assets, data, and capabilities to manage cybersecurity risk
effectively. Categories include Asset Management and Risk Assessment.
• Protect (PR): This function focuses on implementing safeguards to ensure
the delivery of critical services and limit the impact of potential cybersecurity
********** 6 **********
--- page 7 ---
events through proactive controls. Categories include Identity Management
and Access Control and Data Security.
• Detect (DE): This function enables the timely discovery of cybersecurity
events by actively monitoring for anomalies and suspicious activity.
Categories include Anomalies and Events and Security Continuous
Monitoring.
• Respond (RS): This function outlines actions to take when a cybersecurity
incident is detected to contain the impact and initiate mitigation and
communication   plans. Categories include Response Planning and
Communications.
• Recover (RC): This function focuses on restoring capabilities or services
impaired by an incident, ensuring business continuity and resilience through
recovery planning. Categories include Recovery Planning and Improvements
B The fail-safe default principle means that when a system fails or encounters an error, [10]
it should default to a secure state that denies access or privileges rather than allowing
access by default. This minimizes the risk of unauthorized access or damage during
unexpected failures. In other words, if the system can’t decide whether to allow or
deny a request (because of a failure or ambiguity), it should deny by default.
Why is this important?
• Prevents accidental exposure or access when something goes wrong.
CO-2   • Ensures   security   isn’t   compromised   during   system   crashes,
BL-2   misconfigurations, or unexpected conditions.
Example
Imagine a file server that controls access based on permissions.
Fail-safe default approach: If the permission system fails (e.g., the access control
list cannot be read), the server denies all access to files until the problem is resolved.
Fail-open (unsafe) alternative: The server would grant access if it can’t verify
permissions, risking unauthorized access.
Q7   A   [10]
CO-2
BL-2
Advantages of Kerberos
1. Strong Authentication
********** 7 **********

[Text in pictures on this page, read by OCR]
1. Client Logon

Key Distribution Center

Authentication Server

Client 2 GT
3 A N
3 o 3. TGT
3 3
: 3
a > 4. Client-to-Server ticket
£ 2
z <
: ©
(s)
oy

Server

Ticket Granting Server
--- page 8 ---
2. Mutual Authentication
3. Single Sign-On (SSO)
4. Reduced Password Exposure
5. Ticket-Based System
6. Widely Supported
7. Scalability
Limitations of Kerberos
1. If the KDC is ever compromised, then the secret key of every system on the
network is also compromised.
2. Also, if the KDC goes offline, no subject authentication is possible.
3. Issued tickets are stored in memory on the client and server.
4. Malicious subjects can replay captured tickets if they are reused within
their lifetime window.
5. Issued tickets, specifically the Ticket Granting Ticket (TGT), are based on
a hash of the user’s password with an added time stamp for expiration.
6. Kerberos only encrypts authentication traffic (i.e., mechanisms for proving
identity), it does not provide any security for subsequent communication
sessions or data transmissions.
CO-2 B   ▪ When selecting firewall, consider a number of factors:   [10]
BL-3   ▪ What firewall offers right balance between protection and cost for
needs of organization?
▪ Which features are included in base price and which are not?
▪ Ease of setup and configuration? How accessible are staff technicians
who can configure the firewall?
▪ Can firewall adapt to organization’s growing network?
▪ Second most important issue is cost
Decision Factors:
•   Cost-effectiveness and ease of deployment.
•   Basic protection against common threats like DDoS attacks and SQL
injection.
•   Minimal management overhead and easy updates.
•   Support for cloud services since the website is hosted on a cloud platform.
Firewall Selection Considerations:
•Should the startup choose a cloud-based firewall-as-a-service to avoid hardware
costs?
•Or a simple software firewall integrated into the hosting environment?
********** 8 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper c4096d43d94b

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CyberSecurity_7010/Cybersecurity Fundamentals/ANS_Cybersecurity Fundamentals(702IT0C013)_2025-2026.pdf`
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
