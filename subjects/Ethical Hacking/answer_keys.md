# Ethical Hacking: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 6647a9b3375e

- Departments: Computer Engineering, Data Science
- Programmes: BTech Computer 7002, BTech CSE DS 7011, Integrated Computer 7032, MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSE_DS_7011/Ethical Hacking/ANS_Ethical Hacking(702IT0E028)_2025-2026.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: IV / VI/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Ethical Hacking
Date: 04 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is Compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume suitable data if necessary
Q1   Answer briefly:   Marks
a. Describe the OSSTMM and PTES testing methodologies used in ethical hacking. 5
Highlight their key phases and how they guide penetration testing processes.
2.5 marks for each method
OSSTMM
• OSSTMM is a peer-reviewed security testing framework for performing
accurate and repeatable security tests
•   It provides a scientific and standardized approach to security assessments
— across all types of systems: networks, physical security, wireless,
telecommunications, and human factors.
• Created by ISECOM (Institute for Security and Open Methodologies)
• Focuses on measuring the operational security of systems, people, and
infrastructure
BL 1,   •   Offers a neutral, vendor-independent framework for ethical hacking and
CO 3   penetration testing
•   It’s not just about finding vulnerabilities — it’s about measuring how
secure something really is in practice.
OSSTMM tests security across five main channels:
• Human Security: Tests how people behave, social engineering, phishing
•   Physical Security: Buildings, access controls, surveillance systems
• Wireless Security: Wi-Fi, Bluetooth, RFID, and other wireless
technologies
• Telecommunications: Phone systems, VoIP, PBX, signal tapping
• Data Networks: Traditional IT systems like firewalls, routers, and servers
OSSTMM Testing Process Overview
1. Define Scope – Determine what will be tested (e.g., physical office,
network).
2. Information Gathering – Passive and active reconnaissance
********** 1 **********
--- page 2 ---
3. Classification – Assign values to controls, trust, openness
4. Execution – Perform tests using authorized methods
5. Analysis – Use RAV model to assess metrics
6. Reporting – Provide a formal report with findings, scores, and
recommendations
7. The Penetration Testing Execution Standard (PTES) is a comprehensive
framework that defines how professional penetration testing should be
conducted.
8. It provides structured guidance to ensure that penetration tests are
consistent, thorough, and repeatable.
Purpose of PTES
• To standardize the penetration testing process across the industry
• To ensure quality, depth, and consistency
• To align technical testing with business goals
• To produce actionable, understandable reports for organizations
1. Pre-engagement Interactions
2. Intelligence Gathering
3. Threat Modelling
4. Vulnerability Analysis
5. Exploitation
6. Post Exploitation.
7. Reporting
b. Distinguish between Passive Sniffing and Active Sniffing.   5
•   Passive Sniffing:
o Sniffing without interaction—just plug in and capture data.
o Requires the machine’s NIC to be in the same collision domain as
the target.
o Hubs are ideal for passive sniffing since they broadcast all network
messages to every port.
BL 4,   o All devices on a hub receive every message, making it easier to
capture data.
CO 1
• Active Sniffing:
o Requires additional techniques like packet injection or network
manipulation.
o Necessary when the collision domain is segmented (e.g., when using
a switch).
o Switches isolate ports, sending data only to the intended port,
complicating sniffing.
2.5 marks for each Passive Sniffing and Active Sniffing
c. Explain how social engineering is integrated into spoofing attacks.   5
Social engineering is integrated into spoofing attacks by manipulating the target's
psychology, often using psychological tactics like fear or urgency, to trick them
BL 2,
into believing the spoofed identity is legitimate. The attacker then uses this trust,
CO 1
sometimes by impersonating a known person or organization, to exploit the victim
into divulging sensitive information or taking specific actions, such as transferring
funds or clicking a malicious link.
Social Engineering explanation 2 marks. Integration with spoofing 3 marks
********** 2 **********
--- page 3 ---
d. You have just completed a penetration test for a mid-sized company. List the key 5
components you would include in the final report and explain how an effective
report can drive remediation and improve the company’s security.
1. Executive Summary
Provides a high-level overview of the test objectives, scope, major findings, and
overall security posture. Written in non-technical language for senior management.
2. Scope and Objectives
Defines the systems, networks, and applications tested, along with the testing
methodology and limitations. Ensures clarity on what was included/excluded.
3. Methodology
Explains the step-by-step approach used — reconnaissance, scanning, exploitation,
post-exploitation, and reporting. Mentions the testing standards followed (e.g.,
PTES, OWASP).
4. Findings / Vulnerabilities Identified
Lists all discovered vulnerabilities with details such as description, affected
BL 3,   systems, evidence (screenshots/logs), severity rating (critical/high/medium/low),
CO 3   and CVSS score if applicable.
5. Risk Analysis and Impact Assessment
Explains the business impact of each finding — e.g., data leakage, service
disruption, or reputation loss. Helps management prioritize remediation.
6. Recommendations and Mitigation Steps
Provides clear, practical steps to fix or mitigate each vulnerability, along with
references to security best practices or patches.
7. Tools and Techniques Used
Lists the key tools used during testing (e.g., Nmap, Burp Suite, Metasploit,
Wireshark) and their purpose in the assessment.
8. Conclusion and Overall Security Rating
Summarizes the organization’s current security level and readiness, offering
guidance for future improvements.
9. Appendix / Technical Evidence
• Contains detailed logs, payloads, scripts, screenshots, and proof of concept
(PoC) evidence supporting each finding.
a   Briefly describe the phases of ethical hacking and, for each phase, give its main   10
objective and two example tools.
steps in the ethical hacking process:
Q2   Reconnaissance
BL 2,   Scanning
CO 1,   Gaining Access
Maintaining Access
Clearing Tracks
2 marks for each step if mentioned along with tool and objectives
********** 3 **********
--- page 4 ---
b What are DoS and DDoS attacks? Describe how attackers execute these attacks,   10
the types of resources targeted, and provide a comprehensive list of preventive
and reactive mitigation techniques.
A DoS attack floods a target with overwhelming traffic from a single device,
BL 4,
while a DDoS (Distributed Denial of Service) attack uses many compromised
CO 2
devices (a botnet) to launch a much larger and harder-to-detect attack against a
single target, causing legitimate users to be unable to access the service.
DoS and DDoS attacks and execution 2 marks
Target 1 mark
Mitigation techniques 2 marks
a   Explain the key techniques in Network Reconnaissance.   10
1. Ping Sweeping: Ping sweep is a technique used to determine the active devices
within a network by sending ICMP Echo Request packets to a range of IP addresses.
Devices that respond with an ICMP Echo Reply are considered active. Banner
grabbing, or OS fingerprinting, is a method used to determine the OS that is running
on a remote target system.
Active Banner Grabbing: Specially crafted packets are sent to the remote OS, and
the responses are noted, which are then compared with a database to determine the
OS. Responses from different OSes vary, because of differences in the TCP/IP stack
implementation.
Passive Banner Grabbing: This depends on the differential implementation of the
stack and the various ways an OS responds to packets. Passive banner grabbing
Q3   includes banner grabbing from error messages, sniffing the network traffic, and
BL 1,   banner grabbing from page extensions.
CO 1
2. Port Scanning:
Port scanning is used to discover open ports on a networked device. By scanning a
range of ports, an attacker can identify services running on the target and determine
which ports are open, closed, or filtered.
TCP Scanning: Probes TCP ports to see which ones are open.
UDP Scanning: Probes UDP ports, which are less likely to be monitored but can
expose critical services.
3. Service enumeration: involves identifying and probing the services running on
open ports. This includes determining the version of software, supported protocols,
and any potential vulnerabilities in those services.
4. Network Mapping:
Network mapping involves creating a visual or textual map of the network’s
structure, including routers, switches, firewalls, and hosts.
********** 4 **********
--- page 5 ---
This helps attackers understand the layout of the network, including how traffic
flows and where security measures are likely implemented.
5. Vulnerability Scanning
Vulnerability scanning involves using automated tools to detect known
vulnerabilities in network devices and services.
This can include missing patches, outdated software, or default configurations that
could be exploited.
Any 5 techniques = 5 x 2 marks = 10 marks
b Why is it important for ethical hackers to document and report successful AV   10
evasion techniques and not just the vulnerabilities they exploit?
BL,   Ethical hackers must document and report successful antivirus (AV) evasion
CO 2   techniques to strengthen overall cybersecurity, not just report the vulnerabilities
they exploited. Antivirus software is a critical defensive layer, and bypassing it
exposes how an attacker could operate undetected, even if the initial vulnerability
is patched.
a   Explain the main objective of the OWASP Mobile Top 10 list. How does it help   5
developers and security professionals improve mobile application security? List
the top vulnerabilities.
Sample answer: The OWASP Mobile Top 10 is an awareness and prioritization
Q4   list that identifies the most critical risks in mobile applications to guide
BL 1,   developers, testers, and organizations in focusing security efforts and mitigations.
CO 1   The OWASP Mobile Top 10 aims to raise awareness of the most significant
mobile app risks and provide a consensus-driven prioritization to help teams focus
testing and defenses where it matters most.
Objective 2 marks
1 mark for improve mobile application security
2 marks for list
b Describe web-based reconnaissance with tools and techniques used.   10
Web-based reconnaissance is a method of gathering information about a target
using internet resources and publicly accessible data.
It allows the attacker to build a comprehensive profile of the target without direct
interaction, minimizing the risk of detection.
BL 3,   Key Techniques in Web-Based Reconnaissance
1. Search Engine Queries:
CO 1
Google Dorking: Using advanced search operators to locate sensitive data or
misconfigurations.
For example: site: example.com filetype: pdf to find all PDFs hosted on a specific
domain.
inurl: admin to identify URLs with "admin" in them, potentially leading to
administrative panels.
2.   WHOIS Lookup:
********** 5 **********
--- page 6 ---
WHOIS Database: Provides information about domain ownership, registration, and
expiry dates, as well as contact details of domain owners or administrators.
Tools like WHOIS Lookup can be used to query this information.
3.   DNS Interrogation:
nslookup and dig: Used to query DNS records, revealing information about the
target's IP addresses, mail servers (MX records), and other DNS entries.
Reverse DNS Lookup: To identify which domain names are associated with a
specific IP address.
4.   Website and Web Application Analysis:
Crawling and Scraping: Tools like HTTrack, Scrapy, or Burp Suite's web crawler
can be used to mirror websites, discovering hidden directories, exposed files, and
internal links.
Metadata Extraction: Extracting metadata from documents (e.g., using ExifTool) to
find information about the software used, document author, and sometimes network
paths.
Wayback Machine: Reviewing historical snapshots of a website to identify changes
over time, potentially uncovering outdated or exposed information.
5.   Social Media Intelligence (SOCMINT):
Analyzing public profiles on platforms like LinkedIn, Twitter, and Facebook to
gather information about employees, job roles, and organizational structure.
Monitoring for posts, check-ins, or hashtags that could reveal details about
company operations or upcoming events.
Email Harvesting:
Tools like TheHarvester can collect email addresses associated with a domain by
scanning public sources, which can be used for spear-phishing attacks.
Hunter.io: Another service that searches for email addresses and validates them
Shodan and Censys:
Shodan: A search engine for discovering devices connected to the internet,
including servers, webcams, and IoT devices. It provides details on open ports,
services, and vulnerabilities.
Censys: Similar to Shodan, it offers more in-depth analysis, including information
on SSL certificates, configuration, and exposed databases
Description of each technique with tool = 2 marks x 5 = 10 marks
c   Discuss the importance and necessity of enacting the Information Technology   5
Act, 2000 in India. Describe the key amendments and new provisions added in the
IT (Amendment) Act, 2008.
The Information Technology (IT) Act, 2000 was enacted to:
BL 2,   • Provide legal recognition to electronic records and digital signatures.
CO 3   •   Facilitate e-commerce and e-governance by allowing online contracts and
digital communication.
• Define and penalize cybercrimes such as hacking, data theft, and
unauthorized access.
•   Establish authorities like the Controller of Certifying Authorities (CCA)
for managing digital certificates.
• Promote trust and security in digital transactions.
********** 6 **********
--- page 7 ---
the IT Act was amended in 2008 to strengthen data protection, privacy, and
cybercrime enforcement.
1. Recognition of Electronic Signatures
2. Introduction of New Cyber Offences
3. Data Protection and Privacy
4. Legal Recognition of Electronic Contracts
5. Intermediary Liability (Section 79)
6. Empowering the Government
7. Adjudicating Officers and Cyber Appellate Tribunal
a A mobile banking application reports several incidents where user sessions were 10
hijacked, and unauthorized fund transfers occurred. Preliminary investigation
reveals potential weaknesses in the mobile app’s authentication module and
backend server configuration. Analyse the possible attack vectors and
vulnerabilities involved in this incident and discuss how you would test and secure
the system. Explain the relevant OWASP Top 10 vulnerabilities that may have been
exploited.
The incident likely involves several attack vectors and vulnerabilities that
compromise the integrity and confidentiality of user sessions.
1. Attack Vectors and Vulnerabilities
Session Hijacking: Exploiting insecure session tokens or cookies to take over
active sessions.
•   Insecure Authentication: Weak login mechanisms allowing credential theft
or brute-force attacks.
Q5   • Improper Session Token Management: Predictable, non-expiring, or
BL 5,   unencrypted session tokens.
CO 1   • Misconfigured Backend Servers: Exposed APIs, open ports, or improper
access controls.
2. Relevant OWASP Top 10 Vulnerabilities
Web Application Vulnerabilities:
• A02:2021 – Broken Authentication → Weak login controls and session
management.
• A04:2021 – Insecure Design / Sensitive Data Exposure → Unprotected
communication channels.
• A05:2021 – Security Misconfiguration → Default credentials, missing
patches, exposed admin interfaces.
Mobile Application Vulnerabilities:
• Improper Platform Usage → Misuse of Android/iOS security features.
•   Insecure Communication → Lack of HTTPS, certificate pinning, or
encryption.
3. Testing and Validation
• Conduct penetration testing using:
• OWASP Testing Guide – for systematic assessment of web vulnerabilities.
• PTES methodology – for structured testing phases (reconnaissance to
exploitation).
• Use tools like:
********** 7 **********
--- page 8 ---
•   Metasploit: To exploit vulnerabilities and simulate real-world attacks.
•   Meterpreter: To test post-exploitation behavior like session hijacking and
privilege escalation.
4. Mitigation and Security Measures
• Implement multi-factor authentication (MFA) to strengthen user
verification.
• Enforce secure session handling (token rotation, timeouts, encryption).
• Apply server hardening (disable unused services, enforce least privilege).
• Ensure encryption of sensitive data both in transit and at rest.
• Schedule regular vulnerability assessments and patch management.
2.5 marks for each point ( 2.5 marks x 4 = 10 Marks)
b Describe metasploit and meterpreter with the help of a real world example.   10
BL 2,   Metasploit is an open-source framework used by cybersecurity professionals and
CO 2   hackers to develop, test, and execute exploits against vulnerable computer
systems. A key component of Metasploit is its advanced payload, Meterpreter,
which provides stealthy, in-memory control over a compromised machine.
a   Describe how fileless malware and Living off the Land techniques help attackers   5
evade traditional antivirus, including two native tools commonly abused on
Windows or Linux.
Q6   Sample answer: Fileless malware runs mainly in memory and avoids writing
BL2,
payloads to disk, evading signature-based antivirus that relies on file artifacts.
CO 1
Living off the Land techniques abuse trusted native tools to blend in with normal
operations; commonly misused tools include certutil.exe and regsvr32.exe on
Windows, and bash/awk on Linux.
IDS vs IPS
b What are different types of hackers? Analyse and mention the difference between   10
them.
All these types of hackers discovered the following SQL injection vulnerability in
the company’s login page.
Explain how the actions of every type of hacker would differ after finding this
vulnerability.
BL 4,
Vulnerability: A company’s web application contains a vulnerability in its login
CO 3
page that allows SQL injection, which could expose customer data.
Type of Hackers and definitions: 2M
White, grey and black hat hackers
Difference 3 Marks
Action of hackers: 5M
********** 8 **********
--- page 9 ---
c Define network scanning. Explain the primary objectives of scanning and describe 5
any two widely used scanning tools.
Scanning is a technique used by attackers to identify active hosts, open ports, and
services running on a network.
•   It is often the second phase of a cyberattack after reconnaissance and serves
to map out the target network's structure.
BL 1,   •   Objectives of Scanning
CO 1   o Network Mapping: Identify the structure and topology of the target
network.
o Service Discovery: Determine the services and applications running
on network hosts.
o Vulnerability Identification: Discover potential vulnerabilities that
can be exploited
Any two widely used scanning tools are Nmap and Nessus.
o Definition ( 1 mark) + Objectives (3) + Any two tools ( 1 mark) = 5
marks
a An attacker performs ARP cache manipulation in a local network to intercept traffic 5
between Machine A and Machine B. Briefly explain how ARP spoofing enables a
Man-in-the-Middle attack in this scenario. Suggest two practical countermeasures
that network administrators can deploy to detect or prevent ARP spoofing.
ARP cache manipulation is a key hacking technique:
Systems rely on the ARP cache to send frames based on MAC addresses.
Altering the ARP cache can redirect traffic intended for another machine to the
Q7
attacker’s system.
BL 3,
Man-in-the-Middle (MitM) Attack via ARP spoofing:
CO 2
Modify Machine A’s ARP cache to associate Machine B’s IP with the attacker’s
MAC address.
The attacker intercepts all communication between Machine A and Machine B.
Static ARP Entries: Manually map IP addresses to known MAC addresses to
prevent ARP cache poisoning.
Dynamic ARP Inspection (DAI)/ARP Monitoring: Inspect ARP packets against
trusted IP-MAC bindings to detect and block spoofing in real time.
********** 9 **********

[Text in pictures on this page, read by OCR]
Aspect Ethical Hacker Hacker (Malicious)

To identify and report the vulnerability | To exploit the vulnerability for
Intention responsibly. personal gain or damage.

Informs the company’s security team
and provides a report to help fix the | Extracts or manipulates confidential

Action Taken | issue. customer data without permission.
Has written permission from the

Authorization | company to test systems. Has no authorization — acts illegally.
Improves the company’s security Causes data breaches, financial loss,

Outcome posture. or reputation damage.
--- page 10 ---
Other Measures: Use port security, VPNs/encrypted traffic (TLS/HTTPS), and IDS
to monitor and mitigate ARP anomalies.
Explanation ( 3 marks) + countermeasures ( 2 marks) = 5mark
b Explain the role of the "session ID" in a web session. How is it used for session   5
hijacking?
BL3,   The "session ID" in a web session plays a crucial role in maintaining state and
CO1   continuity for a user's interactions with a web application. Due to the stateless
nature of the HTTP protocol, where each request is independent of previous ones,
a mechanism is needed to associate multiple requests from the same user into a
single, ongoing interaction or "session."
c Analyze how improper API Key usage and insufficient cryptography can lead to   5
major security risks in mobile applications
Improper API key usage (for example, hardcoding keys or storing them
BL 4,   insecurely) exposes credentials to reverse engineering and theft, directly aligning
CO 3   with M1 Improper Credential Usage and related concerns noted by OWASP.
Insufficient cryptography (M10) such as weak algorithms, hardcoded keys, or
poor key management undermines confidentiality and integrity, which OWASP’s
testing guidance addresses by recommending secure keystores and proper key
handling.
d A security analyst is asked to assess an organization’s defenses not just from a   5
defensive point of view, but by thinking like a potential attacker. Explain why this
adversarial mindset is essential and how it supports the goals of penetration
testing.
Adversarial thinking is the ability to think like an attacker — to anticipate,
predict, and simulate how a malicious hacker might attempt to breach a system.
It involves understanding the attacker’s motives, methods, and mindset to identify
weaknesses that may not be obvious through normal defensive thinking.
Need for Adversarial Thinking:
1. Proactive Security Approach:
BL 2,   Instead of waiting for attacks, adversarial thinking helps security
CO 3   professionals identify and fix vulnerabilities before they are exploited.
2. Realistic Risk Assessment:
By simulating actual attack strategies, organizations get a clearer picture
of which assets are truly at risk.
3. Improved Defense Strategies:
Helps design more resilient security controls by anticipating how attackers
could bypass them.
4. Bridges the Gap Between Offense and Defense:
Encourages defenders to understand the techniques, tactics, and
procedures (TTPs) of attackers.
Enhances Incident Response:
Teams trained in adversarial thinking can detect, respond, and recover faster from
real-world attacks.
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper c952091f6b53

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_Computer_7002/Ethical Hacking/ANS_Ethical Hacking(702IT0E028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Feb 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Ethical Hacking
Date: 11 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is Compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume suitable data if necessary
Q1   Answer briefly:   Marks
a. A company hires an ethical hacker to perform a penetration test on its internal 5
network. During the assessment, the ethical hacker discovers that by exploiting an
unprotected database, they can access sensitive employee information.
Based on this situation, explain the limitations and protocols that the ethical hacker
must follow while performing such security testing.
Expected answer points:
BL 1,   Limitations:
CO 3   • Cannot access or modify data beyond the agreed scope.
• Must not disrupt business operations or cause system downtime.
• Cannot exploit vulnerabilities for personal gain.
• Must stop testing if unexpected sensitive data is encountered.
Protocols:
• Obtain written permission and scope definition before testing.
• Follow responsible disclosure procedures.
• Maintain confidentiality of all findings.
• Provide a detailed report to authorized stakeholders only.
b. What is OS fingerprinting? List tools used for OS fingerprinting.   5
BL 4,
CO 1   Definition 2 marks
tools 3 marks
c. Explain the difference between vertical and horizontal privilege escalation, and   5
BL 2,   illustrate each with a brief example based on how access changes between user
CO 2   accounts.
********** 1 **********
--- page 2 ---
Vertical privilege escalation is moving from a lower privilege to a higher one (for
example, user to root/admin), while horizontal privilege escalation is moving
sideways to another user account at the same privilege level.
After initial access, attackers often escalate privileges to deepen control or pivot
laterally, making early detection critical.Fileless and LOTL
d. Discuss the purpose and key objectives of the Information Technology Act, 2000 in 5
India.
The Information Technology (IT) Act, 2000 was enacted to:
• Provide legal recognition to electronic records and digital signatures.
BL 3,   •   Facilitate e-commerce and e-governance by allowing online contracts and
CO 3   digital communication.
• Define and penalize cybercrimes such as hacking, data theft, and unauthorized
access.
•   Establish authorities like the Controller of Certifying Authorities (CCA) for
managing digital certificates.
• Promote trust and security in digital transactions.
a   Define Penetration Testing. Discuss its key benefits. Explain and differentiate the   10
various types of penetration testing with suitable example scenarios for each.
Definition: 2 marks
Benefits of Penetration Testing: 2 marks
Types and differentiation: 6 marks
Q2
BL 2,
Penetration Testing (Pen Testing) is a controlled and authorized simulation of a
CO 1,
cyberattack on a computer system, network, or application to identify and exploit
vulnerabilities before malicious hackers can do so.
It helps assess the security strength of an organization’s defenses.
based on information provided to the tester: black box, white box, gray box
based on the specific system or component being tested: network, web application,
mobile app, cloud, wireless, social engineering
b How could you explain hacking wireless networks? Discuss in details.   10
Hacking a wireless network involves exploiting vulnerabilities in communication
BL 4,
protocols, configurations, or hardware to gain unauthorized access. Because
CO 1
wireless signals are broadcast over the air, they can be intercepted by anyone
within range, making them an attractive target for malicious actors.
a What is DNS-based reconnaissance? Elaborate on how security testers use Google 10
Q3   hacking to find sensitive information, and explain the legal boundaries and best
BL 1,   practices that must be observed when using these techniques.
CO 3
DNS-based reconnaissance: 4 marks
********** 2 **********
--- page 3 ---
Google hacking: 4 marks
Legal boundaries: 2 marks
b Define SQL injection. Explain its working impact it creates. State the   10
countermeasures to prevent SQL injection.
SQL injection (SQLi) is a code injection technique that exploits a vulnerability in
a data-driven application. An attacker inserts malicious Structured Query
BL,
Language (SQL) code into web input fields, such as a search bar or login form, to
CO 2
gain unauthorized access to a database.
Definition 2 marks.
Working 4 marks
Countermeasures 4 marks
a Name two OWASP tools that demonstrate mobile application vulnerabilities   5
Q4   OWASP iGoat is an intentionally vulnerable iOS learning platform with guided
BL 1,   lessons to exploit and then fix common mobile weaknesses.
CO 1   OWASP GoatDroid is an intentionally vulnerable Android training environment
(archived but still referenced) designed to teach Android security pitfalls via apps
like FourGoats and HerdFinancial.
b Discuss the types of reconnaissance (active and passive) carried out during ethical   10
hacking. Explain the steps involved and mention suitable tools used in every
phase.
3 Marks
Passive Reconnaissance: Gathering information without interacting directly with
the target systems (low/no risk of detection).
Active Reconnaissance: Directly probing the target to discover live hosts, open
ports, services and detailed configuration (higher risk and likely to be noticed).
steps involved 5 marks
1. Identifying Targets - The first step is to identify which systems or organizations
BL 3,
to footprint by scanning networks for open ports or performing reconnaissance
CO 1
using Google searches and tools like Shodan.
2. Gathering Information - After the target has been identified, the next step is to
gather as much information about it as possible using tools like Nmap, Netcat, and
Whois to identify open ports and services, usernames and passwords, web server
information, and more.
3. Analyzing Results - After all relevant data has been collected, it needs to be
analyzed to determine the most vulnerable points. This is done by identifying
common weaknesses across multiple systems or comparing results against known
exploits.
********** 3 **********
--- page 4 ---
4. Planning Attacks - The final step is to use the information gathered during
footprinting to plan a successful attack against the target’s systems, networks, and
devices. This may involve developing custom exploits or choosing a suitable
attack vector based on the data collected.
Tools for every phase 2 marks
c   Describe the essential elements a penetration testing report must contain to satisfy 5
governance and compliance needs, and analyse how well-crafted reporting
influences security decision-making at the executive level.
1. Executive Summary
Provides a high-level overview of the test objectives, scope, major findings, and
overall security posture. Written in non-technical language for senior management.
2. Scope and Objectives
Defines the systems, networks, and applications tested, along with the testing
methodology and limitations. Ensures clarity on what was included/excluded.
3. Methodology
Explains the step-by-step approach used — reconnaissance, scanning, exploitation,
post-exploitation, and reporting. Mentions the testing standards followed (e.g.,
PTES, OWASP).
4. Findings / Vulnerabilities Identified
Lists all discovered vulnerabilities with details such as description, affected
BL 2,
systems, evidence (screenshots/logs), severity rating (critical/high/medium/low),
CO 3
and CVSS score if applicable.
5. Risk Analysis and Impact Assessment
Explains the business impact of each finding — e.g., data leakage, service
disruption, or reputation loss. Helps management prioritize remediation.
6. Recommendations and Mitigation Steps
Provides clear, practical steps to fix or mitigate each vulnerability, along with
references to security best practices or patches.
7. Tools and Techniques Used
Lists the key tools used during testing (e.g., Nmap, Burp Suite, Metasploit,
Wireshark) and their purpose in the assessment.
8. Conclusion and Overall Security Rating
Summarizes the organization’s current security level and readiness, offering
guidance for future improvements.
9. Appendix / Technical Evidence
Contains detailed logs, payloads, scripts, screenshots, and proof of concept (PoC)
evidence supporting each finding.
a An e-commerce company experiences multiple reports of unauthorized product 10
orders and data leaks from its customer accounts. Initial investigation reveals that
Q5
several users had clicked on phishing links that redirected them to a fake login page
BL 5,
identical to the original website. Furthermore, the company’s mobile shopping app
CO 2
was found to store authentication tokens in plaintext within local storage. Analyse
how both social engineering and insecure mobile data storage contributed to the
********** 4 **********
--- page 5 ---
compromise of customer accounts. Explain how the attacker could exploit these
weaknesses to achieve unauthorized access.
The incident involves a combination of social engineering through phishing and
technical weaknesses in mobile data storage, leading to unauthorized access and
data compromise. The following analysis outlines how these factors contributed to
the breach.
1. Social Engineering and Phishing Attack
User Deception: Attackers created a fake login page visually identical to the
legitimate e-commerce site to trick users into entering their credentials.
Credential Harvesting: The stolen usernames and passwords were transmitted to the
attacker’s server, allowing unauthorized logins.
Trust Exploitation: Users trusted the phishing link because it appeared authentic
(similar domain name, branded visuals, or HTTPS symbol).
2. Insecure Mobile Data Storage
Plaintext Token Storage: The app stored authentication tokens in unencrypted local
storage, making them easily retrievable.
Physical or Malware Access: If a user’s device was compromised, malware or a
malicious app could extract these tokens.
Token Reuse: Attackers could use the stolen tokens to bypass login mechanisms and
directly access user accounts.
Absence of Security Controls: Lack of data encryption, secure storage APIs, and
token expiration policies amplified the risk.
3. Attack Exploitation Process
Step 1 – Credential Theft: Attackers collected valid credentials through phishing.
Step 2 – Token Extraction: They leveraged insecure storage to extract active tokens
from compromised devices.
Step 3 – Account Takeover: Using credentials or tokens, attackers logged in as
legitimate users.
Step 4 – Unauthorized Actions: Orders were placed, and personal data was
exfiltrated.
4. Security Implications and Preventive Measures
Multi-Factor Authentication (MFA): Reduces risk of unauthorized access even with
stolen credentials.
Encrypted Token Storage: Implement secure storage mechanisms (e.g., Android
Keystore, iOS Keychain).
User Awareness Training: Educate customers on recognizing phishing attempts and
verifying URLs.
Regular Security Audits: Conduct penetration tests and code reviews to identify
insecure data handling and update app security policies.
2.5 marks for each point ( 2.5 marks x 4 = 10 Marks)
********** 5 **********
--- page 6 ---
b Explain the "dwell time" concept in relation to privilege escalation. What does an   10
attacker typically do during this phase?
BL 2,
"Dwell time" is the period an attacker remains undetected inside a compromised
CO 1
network. During this phase, which can last for weeks or months, the attacker
conducts crucial reconnaissance to understand the environment and identify
opportunities for privilege escalation.
a Summarize the three main categories of DoS/DDoS attacks (volumetric, protocol,   5
application layer) and state the primary goal characteristic of each category.
Sample answer: Volumetric attacks focus on saturating bandwidth with large
volumes of traffic so legitimate users cannot reach the service, such as ICMP
Q6   floods or Smurf attacks.
BL2,   Sample answer: Protocol attacks exploit weaknesses in protocols to exhaust state
CO 1   tables or intermediary device resources, as seen in SYN floods where half-open
connections overwhelm servers.
Application-layer attacks send legitimate-looking requests that stress application
logic and resources, like HTTP floods that cause the app to slow or crash under
request load.
Privilege escalation
b Describe in detail the steps in the ethical hacking process. Highlight the objectives 10
and tools (2 tools each) used in the process
steps in the ethical hacking process:
BL 4,   Reconnaissance
CO 1   Scanning
Gaining Access
Maintaining Access
Clearing Tracks
2 marks for each step if mentioned along with tool and objectives
c   Define port scanning and describe its role in the reconnaissance phase of ethical 5
hacking. Discuss the countermeasures that organizations can implement to detect
and prevent port scanning.
Port scanning is a network-reconnaissance technique used to identify open ports and
BL 1,
running   services   on   a   target   system.
CO 2
It helps determine which ports are listening (open), closed, or filtered by a firewall.
Each port represents a specific application or service (for example, Port 80 – HTTP,
Port   22   –   SSH).
By scanning these ports, a hacker or ethical hacker can understand what software
or network services are active and possibly exploitable.
********** 6 **********
--- page 7 ---
Role of Port Scanning in the Reconnaissance Phase:
In ethical hacking, reconnaissance (information-gathering) is the first phase of a
penetration   test   or   attack   simulation.
Port scanning plays a crucial role here by:
• Mapping the network — identifying active hosts and services.
• Detecting vulnerabilities — finding open or misconfigured ports that may
be exploited.
• Determining system details — such as operating system, firewall presence,
and running applications.
For example, if a scan reveals Port 21 (FTP) is open, the tester may check for
anonymous login vulnerabilities.
Common tools:
• Nmap (Network Mapper) – used for scanning and service detection.
• Zenmap – graphical interface for Nmap that visualizes scan results.
Countermeasures to Detect and Prevent Port Scanning
1. Use Firewalls:
o Block or restrict access to unnecessary ports.
o Configure rules to allow only trusted IPs and services.
2. Deploy Intrusion Detection and Prevention Systems (IDS/IPS):
o Monitor network traffic for unusual connection attempts.
o Detect scanning patterns (e.g., multiple connection requests from
one source).
3. Enable Logging and Monitoring:
o Maintain detailed logs of incoming/outgoing network connections.
o Regularly review logs for suspicious activity.
4. Rate Limiting and Connection Throttling:
o Limit the number of requests from a single IP within a short time.
o Prevent mass scanning or brute-force connection attempts.
5. Use Port-Knocking Techniques:
o Keep ports closed until a specific sequence of connection attempts
(“knock”) is received.
o Makes open ports invisible to scanners.
6. Implement Stealth Mode / TCP Stack Tweaking:
o Configure systems not to respond to ping or unused ports.
o Reduces visibility to scanners.
7. Deploy Honeypots:
o Set up decoy systems or fake services to lure and identify attackers.
o Helps in studying attack behavior.
8. Network Segmentation:
o Separate internal networks from public-facing systems.
o Limits the exposure of internal services to external scans.
9. Regular Patch and Update Management:
o Keep all systems, software, and network devices updated.
o Close vulnerabilities that could be discovered through open ports.
10. Conduct Regular Vulnerability Scans
o Perform self-assessments using authorized tools (like Nmap or
Nessus).
o Detects open ports before attackers do.
a   Explain any 2 techniques for sniffing. Mention the countermeasures.   5
Q7
********** 7 **********
--- page 8 ---
BL 3,   2 techniques 2 marks each.
CO 2   Countermeasures 1 mark
b   Differentiate IDS and IPS in terms of placement and action, and describe one   5
concrete example tool or deployment scenario for each. (understanding)
An IDS is typically deployed out-of-band to monitor and alert on suspicious
BL3,
activity, while an IPS is placed inline to detect and automatically block malicious
CO1
traffic in real time.
Example deployments include Snort or Suricata as a network IDS on a SPAN/TAP
port, and Cisco Firepower or a Palo Alto NGFW as an inline IPS to enforce
blocking policies.
c How do the OWASP iGoat and Damn Vulnerable iOS Application (DVIA) differ   5
in scope, target audience?
Both iGoat and DVIA are intentionally vulnerable iOS apps that provide hands-on
BL 4,   practice for learning mobile exploitation and defenses, covering topics like data
CO 1   storage, authentication, network security, and broken cryptography.
iGoat follows a lesson-based flow (introduce, exploit, remediate) as an OWASP
project, while DVIA (community-led) offers challenge modules spanning areas
such as local storage, runtime manipulation, jailbreak detection bypass, and crypto
flaws.
d An organization wants to perform a thorough security assessment of its web   5
applications and network infrastructure. As a security professional, explain which
are the testing methodologies you would apply to ensure a complete and ethical
penetration test.
For this organization’s requirement — covering both web applications and
network infrastructure — I would apply a combination of PTES and OSSTMM.
OSSTMM
• OSSTMM is a peer-reviewed security testing framework for performing
accurate and repeatable security tests
•   It provides a scientific and standardized approach to security assessments
— across all types of systems: networks, physical security, wireless,
BL 2,   telecommunications, and human factors.
CO 3   • Created by ISECOM (Institute for Security and Open Methodologies)
• Focuses on measuring the operational security of systems, people, and
infrastructure
•   Offers a neutral, vendor-independent framework for ethical hacking and
penetration testing
•   It’s not just about finding vulnerabilities — it’s about measuring how
secure something really is in practice.
• Purpose of OSSTMM
o To standardize how security assessments are performed
o To provide measurable results (metrics-based approach)
o To assess real-world security — not just theoretical weaknesses
o To ensure legally compliant, repeatable, and scientifically valid
security tests
OSSTMM tests security across five main channels:
********** 8 **********
--- page 9 ---
• Human Security: Tests how people behave, social engineering, phishing
•   Physical Security: Buildings, access controls, surveillance systems
• Wireless Security: Wi-Fi, Bluetooth, RFID, and other wireless technologies
• Telecommunications: Phone systems, VoIP, PBX, signal tapping
• Data Networks: Traditional IT systems like firewalls, routers, and servers
OSSTMM Testing Process Overview
1. Define Scope – Determine what will be tested (e.g., physical office,
network).
2. Information Gathering – Passive and active reconnaissance
3. Classification – Assign values to controls, trust, openness
4. Execution – Perform tests using authorized methods
5. Analysis – Use RAV model to assess metrics
6. Reporting – Provide a formal report with findings, scores, and
recommendations
7. The Penetration Testing Execution Standard (PTES) is a comprehensive
framework that defines how professional penetration testing should be
conducted.
8. It provides structured guidance to ensure that penetration tests are
consistent, thorough, and repeatable.
Purpose of PTES
• To standardize the penetration testing process across the industry
• To ensure quality, depth, and consistency
• To align technical testing with business goals
• To produce actionable, understandable reports for organizations
1. Pre-engagement Interactions
2. Intelligence Gathering
3. Threat Modelling
4. Vulnerability Analysis
5. Exploitation
6. Post Exploitation.
7. Reporting
********** 9 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 366b95e68569

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/MBATech_Computer_7047/Ethical Hacking/ANS_Ethical Hacking(702IT0E028)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 Feb 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CSE - DS) (311)/B. Tech Intg. (CE)/MASTER OF
BUSINESS ADMINISTRATION IN TECHNOLOGY MANAGEMENT (COMPUTER
ENGINEERING)/MBA Tech (Comp)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Ethical Hacking
Date: 11 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is Compulsory
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume suitable data if necessary
Q1   Answer briefly:   Marks
a. A company hires an ethical hacker to perform a penetration test on its internal 5
network. During the assessment, the ethical hacker discovers that by exploiting an
unprotected database, they can access sensitive employee information.
Based on this situation, explain the limitations and protocols that the ethical hacker
must follow while performing such security testing.
Expected answer points:
BL 1,   Limitations:
CO 3   • Cannot access or modify data beyond the agreed scope.
• Must not disrupt business operations or cause system downtime.
• Cannot exploit vulnerabilities for personal gain.
• Must stop testing if unexpected sensitive data is encountered.
Protocols:
• Obtain written permission and scope definition before testing.
• Follow responsible disclosure procedures.
• Maintain confidentiality of all findings.
• Provide a detailed report to authorized stakeholders only.
b. What is OS fingerprinting? List tools used for OS fingerprinting.   5
BL 4,
CO 1   Definition 2 marks
tools 3 marks
c. Explain the difference between vertical and horizontal privilege escalation, and   5
BL 2,
illustrate each with a brief example based on how access changes between user
CO 2
accounts.
********** 1 **********
--- page 2 ---
Vertical privilege escalation is moving from a lower privilege to a higher one (for
example, user to root/admin), while horizontal privilege escalation is moving
sideways to another user account at the same privilege level.
After initial access, attackers often escalate privileges to deepen control or pivot
laterally, making early detection critical.Fileless and LOTL
d. Discuss the purpose and key objectives of the Information Technology Act, 2000 in 5
India.
The Information Technology (IT) Act, 2000 was enacted to:
• Provide legal recognition to electronic records and digital signatures.
BL 3,   •   Facilitate e-commerce and e-governance by allowing online contracts and
CO 3   digital communication.
• Define and penalize cybercrimes such as hacking, data theft, and unauthorized
access.
•   Establish authorities like the Controller of Certifying Authorities (CCA) for
managing digital certificates.
• Promote trust and security in digital transactions.
a   Define Penetration Testing. Discuss its key benefits. Explain and differentiate the   10
various types of penetration testing with suitable example scenarios for each.
Definition: 2 marks
Benefits of Penetration Testing: 2 marks
Types and differentiation: 6 marks
Q2
BL 2,
Penetration Testing (Pen Testing) is a controlled and authorized simulation of a
CO 1,
cyberattack on a computer system, network, or application to identify and exploit
vulnerabilities before malicious hackers can do so.
It helps assess the security strength of an organization’s defenses.
based on information provided to the tester: black box, white box, gray box
based on the specific system or component being tested: network, web application,
mobile app, cloud, wireless, social engineering
b How could you explain hacking wireless networks? Discuss in details.   10
Hacking a wireless network involves exploiting vulnerabilities in communication
BL 4,
protocols, configurations, or hardware to gain unauthorized access. Because
CO 1
wireless signals are broadcast over the air, they can be intercepted by anyone
within range, making them an attractive target for malicious actors.
a What is DNS-based reconnaissance? Elaborate on how security testers use Google 10
Q3
hacking to find sensitive information, and explain the legal boundaries and best
BL 1,
practices that must be observed when using these techniques.
CO 3
********** 2 **********
--- page 3 ---
DNS-based reconnaissance: 4 marks
Google hacking: 4 marks
Legal boundaries: 2 marks
b Define SQL injection. Explain its working impact it creates. State the   10
countermeasures to prevent SQL injection.
SQL injection (SQLi) is a code injection technique that exploits a vulnerability in
a data-driven application. An attacker inserts malicious Structured Query
BL,
Language (SQL) code into web input fields, such as a search bar or login form, to
CO 2
gain unauthorized access to a database.
Definition 2 marks.
Working 4 marks
Countermeasures 4 marks
a Name two OWASP tools that demonstrate mobile application vulnerabilities   5
Q4   OWASP iGoat is an intentionally vulnerable iOS learning platform with guided
BL 1,   lessons to exploit and then fix common mobile weaknesses.
CO 1   OWASP GoatDroid is an intentionally vulnerable Android training environment
(archived but still referenced) designed to teach Android security pitfalls via apps
like FourGoats and HerdFinancial.
b Discuss the types of reconnaissance (active and passive) carried out during ethical   10
hacking. Explain the steps involved and mention suitable tools used in every
phase.
3 Marks
Passive Reconnaissance: Gathering information without interacting directly with
the target systems (low/no risk of detection).
Active Reconnaissance: Directly probing the target to discover live hosts, open
ports, services and detailed configuration (higher risk and likely to be noticed).
steps involved 5 marks
BL 3,   1. Identifying Targets - The first step is to identify which systems or organizations
CO 1   to footprint by scanning networks for open ports or performing reconnaissance
using Google searches and tools like Shodan.
2. Gathering Information - After the target has been identified, the next step is to
gather as much information about it as possible using tools like Nmap, Netcat, and
Whois to identify open ports and services, usernames and passwords, web server
information, and more.
3. Analyzing Results - After all relevant data has been collected, it needs to be
analyzed to determine the most vulnerable points. This is done by identifying
common weaknesses across multiple systems or comparing results against known
exploits.
********** 3 **********
--- page 4 ---
4. Planning Attacks - The final step is to use the information gathered during
footprinting to plan a successful attack against the target’s systems, networks, and
devices. This may involve developing custom exploits or choosing a suitable
attack vector based on the data collected.
Tools for every phase 2 marks
c   Describe the essential elements a penetration testing report must contain to satisfy 5
governance and compliance needs, and analyse how well-crafted reporting
influences security decision-making at the executive level.
1. Executive Summary
Provides a high-level overview of the test objectives, scope, major findings, and
overall security posture. Written in non-technical language for senior management.
2. Scope and Objectives
Defines the systems, networks, and applications tested, along with the testing
methodology and limitations. Ensures clarity on what was included/excluded.
3. Methodology
Explains the step-by-step approach used — reconnaissance, scanning, exploitation,
post-exploitation, and reporting. Mentions the testing standards followed (e.g.,
PTES, OWASP).
4. Findings / Vulnerabilities Identified
Lists all discovered vulnerabilities with details such as description, affected
BL 2,
systems, evidence (screenshots/logs), severity rating (critical/high/medium/low),
CO 3
and CVSS score if applicable.
5. Risk Analysis and Impact Assessment
Explains the business impact of each finding — e.g., data leakage, service
disruption, or reputation loss. Helps management prioritize remediation.
6. Recommendations and Mitigation Steps
Provides clear, practical steps to fix or mitigate each vulnerability, along with
references to security best practices or patches.
7. Tools and Techniques Used
Lists the key tools used during testing (e.g., Nmap, Burp Suite, Metasploit,
Wireshark) and their purpose in the assessment.
8. Conclusion and Overall Security Rating
Summarizes the organization’s current security level and readiness, offering
guidance for future improvements.
9. Appendix / Technical Evidence
Contains detailed logs, payloads, scripts, screenshots, and proof of concept (PoC)
evidence supporting each finding.
********** 4 **********
--- page 5 ---
a An e-commerce company experiences multiple reports of unauthorized product 10
orders and data leaks from its customer accounts. Initial investigation reveals that
several users had clicked on phishing links that redirected them to a fake login page
identical to the original website. Furthermore, the company’s mobile shopping app
was found to store authentication tokens in plaintext within local storage. Analyse
how both social engineering and insecure mobile data storage contributed to the
compromise of customer accounts. Explain how the attacker could exploit these
weaknesses to achieve unauthorized access.
The incident involves a combination of social engineering through phishing and
technical weaknesses in mobile data storage, leading to unauthorized access and
data compromise. The following analysis outlines how these factors contributed to
the breach.
1. Social Engineering and Phishing Attack
User Deception: Attackers created a fake login page visually identical to the
legitimate e-commerce site to trick users into entering their credentials.
Credential Harvesting: The stolen usernames and passwords were transmitted to the
attacker’s server, allowing unauthorized logins.
Trust Exploitation: Users trusted the phishing link because it appeared authentic
(similar domain name, branded visuals, or HTTPS symbol).
Q5
BL 5,   2. Insecure Mobile Data Storage
CO 2   Plaintext Token Storage: The app stored authentication tokens in unencrypted local
storage, making them easily retrievable.
Physical or Malware Access: If a user’s device was compromised, malware or a
malicious app could extract these tokens.
Token Reuse: Attackers could use the stolen tokens to bypass login mechanisms and
directly access user accounts.
Absence of Security Controls: Lack of data encryption, secure storage APIs, and
token expiration policies amplified the risk.
3. Attack Exploitation Process
Step 1 – Credential Theft: Attackers collected valid credentials through phishing.
Step 2 – Token Extraction: They leveraged insecure storage to extract active tokens
from compromised devices.
Step 3 – Account Takeover: Using credentials or tokens, attackers logged in as
legitimate users.
Step 4 – Unauthorized Actions: Orders were placed, and personal data was
exfiltrated.
4. Security Implications and Preventive Measures
Multi-Factor Authentication (MFA): Reduces risk of unauthorized access even with
stolen credentials.
Encrypted Token Storage: Implement secure storage mechanisms (e.g., Android
Keystore, iOS Keychain).
********** 5 **********
--- page 6 ---
User Awareness Training: Educate customers on recognizing phishing attempts and
verifying URLs.
Regular Security Audits: Conduct penetration tests and code reviews to identify
insecure data handling and update app security policies.
2.5 marks for each point ( 2.5 marks x 4 = 10 Marks)
b Explain the "dwell time" concept in relation to privilege escalation. What does an   10
attacker typically do during this phase?
BL 2,
"Dwell time" is the period an attacker remains undetected inside a compromised
CO 1
network. During this phase, which can last for weeks or months, the attacker
conducts crucial reconnaissance to understand the environment and identify
opportunities for privilege escalation.
a Summarize the three main categories of DoS/DDoS attacks (volumetric, protocol,   5
application layer) and state the primary goal characteristic of each category.
Sample answer: Volumetric attacks focus on saturating bandwidth with large
volumes of traffic so legitimate users cannot reach the service, such as ICMP
Q6   floods or Smurf attacks.
BL2,   Sample answer: Protocol attacks exploit weaknesses in protocols to exhaust state
CO 1   tables or intermediary device resources, as seen in SYN floods where half-open
connections overwhelm servers.
Application-layer attacks send legitimate-looking requests that stress application
logic and resources, like HTTP floods that cause the app to slow or crash under
request load.
Privilege escalation
b Describe in detail the steps in the ethical hacking process. Highlight the objectives 10
and tools (2 tools each) used in the process
steps in the ethical hacking process:
BL 4,   Reconnaissance
CO 1   Scanning
Gaining Access
Maintaining Access
Clearing Tracks
2 marks for each step if mentioned along with tool and objectives
c   Define port scanning and describe its role in the reconnaissance phase of ethical 5
hacking. Discuss the countermeasures that organizations can implement to detect
and prevent port scanning.
BL 1,
CO 2
Port scanning is a network-reconnaissance technique used to identify open ports and
running   services   on   a   target   system.
It helps determine which ports are listening (open), closed, or filtered by a firewall.
********** 6 **********
--- page 7 ---
Each port represents a specific application or service (for example, Port 80 – HTTP,
Port   22   –   SSH).
By scanning these ports, a hacker or ethical hacker can understand what software
or network services are active and possibly exploitable.
Role of Port Scanning in the Reconnaissance Phase:
In ethical hacking, reconnaissance (information-gathering) is the first phase of a
penetration   test   or   attack   simulation.
Port scanning plays a crucial role here by:
• Mapping the network — identifying active hosts and services.
• Detecting vulnerabilities — finding open or misconfigured ports that may
be exploited.
• Determining system details — such as operating system, firewall presence,
and running applications.
For example, if a scan reveals Port 21 (FTP) is open, the tester may check for
anonymous login vulnerabilities.
Common tools:
• Nmap (Network Mapper) – used for scanning and service detection.
• Zenmap – graphical interface for Nmap that visualizes scan results.
Countermeasures to Detect and Prevent Port Scanning
1. Use Firewalls:
o Block or restrict access to unnecessary ports.
o Configure rules to allow only trusted IPs and services.
2. Deploy Intrusion Detection and Prevention Systems (IDS/IPS):
o Monitor network traffic for unusual connection attempts.
o Detect scanning patterns (e.g., multiple connection requests from
one source).
3. Enable Logging and Monitoring:
o Maintain detailed logs of incoming/outgoing network connections.
o Regularly review logs for suspicious activity.
4. Rate Limiting and Connection Throttling:
o Limit the number of requests from a single IP within a short time.
o Prevent mass scanning or brute-force connection attempts.
5. Use Port-Knocking Techniques:
o Keep ports closed until a specific sequence of connection attempts
(“knock”) is received.
o Makes open ports invisible to scanners.
6. Implement Stealth Mode / TCP Stack Tweaking:
o Configure systems not to respond to ping or unused ports.
o Reduces visibility to scanners.
7. Deploy Honeypots:
o Set up decoy systems or fake services to lure and identify attackers.
o Helps in studying attack behavior.
8. Network Segmentation:
o Separate internal networks from public-facing systems.
o Limits the exposure of internal services to external scans.
9. Regular Patch and Update Management:
o Keep all systems, software, and network devices updated.
o Close vulnerabilities that could be discovered through open ports.
10. Conduct Regular Vulnerability Scans
o Perform self-assessments using authorized tools (like Nmap or
Nessus).
********** 7 **********
--- page 8 ---
o Detects open ports before attackers do.
a   Explain any 2 techniques for sniffing. Mention the countermeasures.   5
Q7
BL 3,
2 techniques 2 marks each.
CO 2
Countermeasures 1 mark
b   Differentiate IDS and IPS in terms of placement and action, and describe one   5
concrete example tool or deployment scenario for each. (understanding)
An IDS is typically deployed out-of-band to monitor and alert on suspicious
BL3,
activity, while an IPS is placed inline to detect and automatically block malicious
CO1
traffic in real time.
Example deployments include Snort or Suricata as a network IDS on a SPAN/TAP
port, and Cisco Firepower or a Palo Alto NGFW as an inline IPS to enforce
blocking policies.
c How do the OWASP iGoat and Damn Vulnerable iOS Application (DVIA) differ   5
in scope, target audience?
Both iGoat and DVIA are intentionally vulnerable iOS apps that provide hands-on
BL 4,   practice for learning mobile exploitation and defenses, covering topics like data
CO 1   storage, authentication, network security, and broken cryptography.
iGoat follows a lesson-based flow (introduce, exploit, remediate) as an OWASP
project, while DVIA (community-led) offers challenge modules spanning areas
such as local storage, runtime manipulation, jailbreak detection bypass, and crypto
flaws.
d An organization wants to perform a thorough security assessment of its web   5
applications and network infrastructure. As a security professional, explain which
are the testing methodologies you would apply to ensure a complete and ethical
penetration test.
For this organization’s requirement — covering both web applications and
network infrastructure — I would apply a combination of PTES and OSSTMM.
OSSTMM
• OSSTMM is a peer-reviewed security testing framework for performing
BL 2,   accurate and repeatable security tests
CO 3   •   It provides a scientific and standardized approach to security assessments
— across all types of systems: networks, physical security, wireless,
telecommunications, and human factors.
• Created by ISECOM (Institute for Security and Open Methodologies)
• Focuses on measuring the operational security of systems, people, and
infrastructure
•   Offers a neutral, vendor-independent framework for ethical hacking and
penetration testing
•   It’s not just about finding vulnerabilities — it’s about measuring how
secure something really is in practice.
• Purpose of OSSTMM
o To standardize how security assessments are performed
********** 8 **********
--- page 9 ---
o To provide measurable results (metrics-based approach)
o To assess real-world security — not just theoretical weaknesses
o To ensure legally compliant, repeatable, and scientifically valid
security tests
OSSTMM tests security across five main channels:
• Human Security: Tests how people behave, social engineering, phishing
•   Physical Security: Buildings, access controls, surveillance systems
• Wireless Security: Wi-Fi, Bluetooth, RFID, and other wireless technologies
• Telecommunications: Phone systems, VoIP, PBX, signal tapping
• Data Networks: Traditional IT systems like firewalls, routers, and servers
OSSTMM Testing Process Overview
1. Define Scope – Determine what will be tested (e.g., physical office,
network).
2. Information Gathering – Passive and active reconnaissance
3. Classification – Assign values to controls, trust, openness
4. Execution – Perform tests using authorized methods
5. Analysis – Use RAV model to assess metrics
6. Reporting – Provide a formal report with findings, scores, and
recommendations
7. The Penetration Testing Execution Standard (PTES) is a comprehensive
framework that defines how professional penetration testing should be
conducted.
8. It provides structured guidance to ensure that penetration tests are
consistent, thorough, and repeatable.
Purpose of PTES
• To standardize the penetration testing process across the industry
• To ensure quality, depth, and consistency
• To align technical testing with business goals
• To produce actionable, understandable reports for organizations
1. Pre-engagement Interactions
2. Intelligence Gathering
3. Threat Modelling
4. Vulnerability Analysis
5. Exploitation
6. Post Exploitation.
7. Reporting
********** 9 **********
````

## 2024-25 · Final-Exam · Sem 12 · Answer key · paper 515ec0d1d93c

- Departments: Electronics and Telecommunication
- Programmes: BTech (ELECTRONICS & TELECOMMUNICATION
- Source: `02_Question_Papers/2024/Sem_12/Final-Exam/BTech (ELECTRONICS & TELECOMMUNICATION _e9090790/Ethical Hacking/ANS_Ethical Hacking(702IT0E028)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Apr 2025
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING) SIX YEARS INTEGRATED PROGRAM
Year: VI/Semester XII(Exam Year: 2024-2025)
Subject: Ethical Hacking
Date: 28 Apr 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 4 pages.
2. Question No.1 is compulsory
3. Out of remaining questions, attempt any 4 Questions
4. In all 5 Question to be attempted
5. All Questions carry equal marks
6. Answer to each new question to be started on a fresh page
7. Figure in brackets on the right hand side indicate fill marks
8. Assume suitable data if necessary
QNo   Parameters   Marks
Q1a   Classify Hacker based on Hat Categories
Soln   Definition of a Hacker   1
Classification of Hackers   2
(White Hat, Black Hat, Grey Hat).
Characteristics – explanation of each type   1
Example of each type   1
Q1b   Describe Web –Based recon technique
Soln   Introduction to Reconnaissance   1
Types of Web-Based Recon(active and Passive)   2
Technique used (tools and methods)   1
Need of reconnaissance is used in ethical hacking   1
Q1c   What is Google Hacking   1
Soln   Definition of Google Hacking   1
Purpose of Google Hacking(ethical and unethical)   2
Google Search Operators(site:, filetype:, intitle: with examples.)   1
Preventive Measures
Q1d   Differentiate between Ethical Hacking and Hacking
Soln   Definition ethical hacking and hacking   1
Authorization   1
Intent   1
Purpose   1
Tools used   1
********** 1 **********
--- page 2 ---
examples
Q2A   What is IP spoofing? Suggest countermeasures to prevent IP Spoofing
Soln   Definition   2
Working (Process of IP Spoofing using a step-by-step approach. Describe how   2
packets are altered.)
Types of Attacks Using IP Spoofing DDoS, MITM (Man-in-the-Middle), and   3
Session Hijacking.
Countermeasures to Prevent IP Spoofing (Suggest practical countermeasures like   3
packet filtering, authentication mechanisms, and network monitoring.)
Q2B   What are different types of PEN testing? Explain the benefits of PEN testing
Soln   Definition of Penetration Testing   2
Types of PEN Testing (At Least 4)( Black Box, White Box, Gray Box, External,   5
Internal)
Benefits of PEN Testing( 3 to 4 )   3
Q3A   Explain any Five challenges faced by an ethical hacker
Soln   Introduction to Ethical Hacking   1
Explanation of Challenges (five relevant challenges faced by ethical hackers)   7
Impact and Consequences   2
Q3b   What is Sniffing?Explain any one technique used for sniffing and its Counter
Measures
Soln   Definition of Sniffing   2
Working(how sniffing works by intercepting and capturing network packets.)   3
Explanation of One Sniffing Technique(e.g., Passive Sniffing, Active Sniffing,   3
ARP Spoofing, DNS Poisoning). Provide examples.)
Countermeasures to Prevent Sniffing(Suggest practical countermeasures such as   2
encryption, network monitoring, and secure protocols.)
Q4A MPSTME provides various online service to students, Faculty members and
staff. They have deployed various security solutions like firewall to ensure
security of data and Insfrastructure.MPSTME CISCO wants to know the
security posture of their organization. They want to ensure that the security
solutions they have deployed are working properly. Want are various steps that
you will follow as a independent pen tester to meet the expectation of MPSTME
CISO?Explain the activities in each phase.
Soln   Introduction to Penetration Testing   1
Phase 1: Planning and Preparation(Explain the activities in this phase including   2
defining scope, objectives, legal permissions, and gathering information.)
Phase 2: Reconnaissance and Information Gathering Describe techniques like   2
passive reconnaissance, active reconnaissance, and social engineering.)
Phase 3: Vulnerability Assessment(Explain how vulnerabilities are identified   2
using tools and techniques such as vulnerability scanners.)
Phase 4: Exploitation and Testing(Discuss how identified vulnerabilities are   2
exploited to understand their potential impact.)
********** 2 **********
--- page 3 ---
Phase 5: Reporting and Recommendation(Explain how findings are documented   1
and provide actionable recommendations for improving security.)
Q4B   Explain the need for IT act.what are the Features of IT amended act 2008
Soln   Introduction to IT Act   1
Need of IT Act (Describe the need for the IT Act with examples, focusing on   3
cybercrime prevention, data protection, and e-commerce regulation.)
Introduction to IT Amended Act 2008(brief introduction to the amendment and its   2
importance.)
Features of the IT Amended Act 2008 (Give least 4 key features of the IT   4
Amended Act 2008, focusing on cybersecurity, data privacy, and legal aspects.)
Q5A   Explain any five mobile risk defined by OWASP
Soln   Introduction to OWASP and Mobile Risks(OWASP and explain its role in   1
cybersecurity)
Explanation of Five Mobile Risks(Describe five key risks from the OWASP   7
Mobile Top 10 list.)
Impact of Mobile Risks(Explain how these risks can compromise security, user   1
data, or application performance.)
Counter Measures(Suggest effective countermeasures for mitigating these risks.)   1
Q5B   What is MAC flooding attack?How will you prevent it?
Soln   Definition of MAC Flooding Attack   1
Working of MAC Flooding Attack(Describe how MAC Flooding works, including   3
the role of switches and MAC tables. with an example.)
Impact of MAC Flooding(Explain the consequences of a successful MAC Flooding   3
Attack, including network disruptions and security risks.)
Counter Measures(Suggest effective countermeasures to prevent MAC Flooding   3
Attacks.)
Q6A   Explain error based SQL injection attack with an example. Suggest Counter
measures
Soln   Definition of SQL Injection   1
Explanation of Error-Based SQL Injection(Describe how error-based SQL   4
Injection works, using error messages to extract information.)
Example of Error-Based SQL Injection(Provide a step-by-step example   3
demonstrating an error-based SQL Injection attack.)
Countermeasures to Prevent SQL Injection(Suggest effective countermeasures to   2
prevent SQL Injection attacks.)
Q6B   What is meterpreter?Describe the metasploit architecture
Soln   Definition of Meterpreter and Metasploit   2
Features and Functions of Meterpreter(Explain key features of Meterpreter, such as   3
command execution, file manipulation, and session management.)
Explanation of Metasploit Architecture(Describe the architecture of Metasploit,   5
covering its components (e.g., Modules, Payloads, Exploits, Auxiliary, Encoders).)
Q7A   Explain Architecture of Android OS
Soln   Introduction to Android OS
********** 3 **********
--- page 4 ---
Layer 1: Linux Kernel( Explain the role of the Linux Kernel in managing drivers,
memory, and hardware communication.)
Layer 2: Hardware Abstraction Layer (HAL)( Describe how HAL provides
standard interfaces to interact with hardware components.)
Layer 3: Android Runtime (ART)( Explain the role of Android Runtime and its
Just-In-Time (JIT) compiler for executing applications.)
Layer 4: Native Libraries(Describe key native libraries such as SQLite, WebKit,
and OpenGL ES for various functions.)
Layer 5: Application Framework (Explain the role of the application framework in
providing APIs for application development.)
Layer 6: Applications(Describe the topmost layer where applications like phone,
messages, and browser run.)
Q7B   Explain DDos Attack?How will you prevent it?
Soln   Definition of DDoS Attack   2
Working of DDoS Attack (Describe how DDoS attacks work using botnets and   4
malicious traffic. Explain different types of DDoS attacks.)
Impact of DDoS Attack (Explain the consequences of a successful DDoS attack on   2
businesses, governments, or networks.)
Counter Measures(Suggest effective countermeasures to prevent or mitigate DDoS   2
attacks.)
********** 4 **********
````
