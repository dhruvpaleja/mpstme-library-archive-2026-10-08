# Mobile Device Security and Forensics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 7485ceeaee97

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CyberSecurity_7010/Mobile Device Security and Forensics/ANS_Mobile Device Security and Forensics(702IT0E019)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Mobile Device Security and Forensics
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figures in brackets on the right-hand side indicate full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary
Q1   Answer briefly:   Marks
CO-1;   a. Describe the Design Challenges in Wireless Systems covering capacity, [5]
BL-2
mobility, heterogeneous applications, and energy constraints
[1 mark each for any 5 challenges]
• Capacity-Limited Medium: Wireless channels are broadcast media
shared by all users; limited spectrum means limited capacity
• Mobility & Dynamic Conditions: Traffic patterns, user locations, and
network conditions change constantly — design must adapt in real-time
• Heterogeneous Applications: Voice, data, and video have very different
QoS requirements (delay, loss, BER, data rate) — one-size-fits-all
protocols fail
• Energy & Delay Constraints: Battery-powered mobile devices impose
strict limits; sleep modes save energy but complicate protocol design
• Interference & Propagation: Signals fade over distance, reflect off
surfaces, and interfere with co-channel transmissions
• Crosslayer Design: Energy, delay, and rate constraints must be balanced
across hardware,   link, access, network, and application layers
simultaneously
CO-1; b. Enumerate the types of Hand-offs in mobile systems and briefly describe each [5]
BL-2
type
[1 mark each for any 5 types with description]
• Intra-cell Handoff (Soft Handoff): Transfers connection between
channels within the same cell to optimize resource use
********** 1 **********
--- page 2 ---
• Inter-cell Handoff (Hard Handoff): Transfers connection from one cell to
another when device moves out of coverage; more complex, may involve
multiple base stations
• Mobile-Assisted Handoff (MAHO): Mobile device measures signal
strengths from neighboring cells and reports to network to assist decision
• Network-Controlled Handoff: Network determines when/where handoff
occurs based on signal strength, quality, and cell load — device not
actively involved
• Vertical Handoff: Switches between different network types (e.g.,
cellular to Wi-Fi), maintaining connectivity across technologies
• Horizontal Handoff: Switches between cells of the same network
technology (e.g., one LTE cell to another LTE cell)
CO-2;   c. Explain the role of the Trusted Execution Environment (TEE) and describe [5]
BL-2
how it is used to secure sensitive operations in mobile devices
[2 marks definition/concept + 3 marks for use in mobile security]
• Definition: A TEE is an isolated, secure area within the main processor,
separated from the regular OS (REE — Rich Execution Environment)
• Data Protection: Ensures sensitive data is stored, processed, and protected
in a hardware-isolated environment
• End-to-End   Security:   Provides   authenticated   code   execution,
confidentiality, authenticity, privacy, system integrity, and data access
rights
• Use in Mobile Devices: Used for mobile payments, biometric
authentication, DRM, and secure key storage — prevents malware from
accessing sensitive operations
• Remote Management: Allows specific managers to control subsets of
trusted applications without interfering with others
• TEE vs REE: TEE runs parallel to the OS; even if OS is compromised,
TEE remains secure — critical for banking apps, UPI, and biometric data
CO-2; d.   Illustrate the File System of a SIM Card (UICC) and explain the four types of [5]
BL-2
files it contains
[1 mark each for 4 file types + 1 mark for context]
• Master File (MF): Root of the UICC file system; all files descend from
here; acts as the top-level directory
• Dedicated Files (DF): Subdirectories under MF; group related EFs
together (e.g., DF_GSM for GSM data, DF_Telecom for telecom
services)
• Application Dedicated Files (ADF): Similar to DFs but specific to a
particular UICC application (e.g., ADF_USIM for USIM app data)
• Elementary Files (EF): Actual data files that store user/network data such
as ICCID, IMSI, SMS, phonebook (ADN), LOCI, FPLMN, and LND
• Forensic Significance: An examiner navigates this hierarchy using APDU
commands to locate and extract specific EFs as evidence
********** 2 **********
--- page 3 ---
Q2   a. Demonstrate how Malware Forensics is carried out on Volatile and Non- [10]
CO-2;
Volatile memory in Mobile Devices, covering collection, preservation,
BL-3
analysis, and interpretation for each memory type
[5 marks Volatile Memory + 5 marks Non-Volatile Memory]
Volatile Memory Forensics [5 marks]
• Collection (1 mark): RAM contains data lost on power-off; must be
acquired immediately using tools like Cellebrite UFED, Magnet AXIOM,
or Volatility Framework
• Preservation (1 mark): Create a memory dump / RAM image stored in a
forensically sound manner to maintain integrity
• Analysis (1.5 marks): Analyze dump for running processes, network
connections, open files, encryption keys using Volatility Framework
plugins for Android/iOS
• Interpretation (1.5 marks): Identify anomalies — unexpected processes,
unauthorized network connections, indicators of compromise (IoC)
Non-Volatile Memory Forensics [5 marks]
• Collection (1 mark): Internal storage (eMMC, UFS) and microSD cards
retain data when powered off; tools: Cellebrite UFED, Oxygen Forensic
Detective, XRY
• Preservation (1 mark): Acquired data preserved using hashing (MD5 /
SHA-256) to generate checksums verifying integrity
• Analysis (1.5 marks): Identify malware-infected files, suspicious apps,
system configs; file carving to recover deleted files / hidden data
• Interpretation   (1.5   marks):   Analyze   malware   binaries, C2
communications, attack timeline; reconstruct malware capabilities and
impact on device
Q2   b. Explain   the following Bluetooth   vulnerabilities along with   their [10]
CO-1;
countermeasures:
BL-3
[2 marks each: 1 mark description + 1 mark countermeasure]
• i) BlueBorne (2 marks)
◦ Flaws in Bluetooth implementation (not the standard itself) that
allow attacker to take control of any nearby BT-enabled device
without pairing
◦ Attack spreads to other nearby vulnerable BT devices — can listen
to calls, access/steal data
◦ Countermeasure: Keep device firmware updated; disable Bluetooth
when not in use
• ii) Bleeding Bit (2 marks)
◦ Exploits vulnerability in Texas Instruments Bluetooth chips; does not
require pairing — only needs BT to be ON and in range
◦ 'Contagious' — spreads through entire network once one device is
compromised
◦ Countermeasure: Apply firmware patches from Texas Instruments;
update all BT-chip-based devices
• iii) KNOB — Key Negotiation of Bluetooth (2 marks)
********** 3 **********
--- page 4 ---
◦ Forces devices to use an extremely weak encryption key (as short as
1 byte) during pairing; attacker brute-forces the key and decrypts all
communications
◦ Works because Bluetooth allows 1-byte keys, exchange   is
unencrypted, and pairing device must accept low-entropy key
◦ Countermeasure: Apply patches enforcing minimum key lengths; use
modern BT versions (5.1+) with KNOB protections
• iv) SweynTooth (2 marks)
◦ Vulnerabilities in BLE devices (including medical equipment) with
three attack types: crash devices, reboot/deadlock devices, override
device security
◦ Third type gives attacker full control of the BLE device
◦ Countermeasure: Patch BLE firmware; avoid using vulnerable BLE
chipsets in critical devices
• v) Short PINs in Bluetooth Pairing (2 marks)
◦ Short PINs (access codes for pairing) are easier to crack; attacker
captures key exchange and brute-forces the PIN
◦ User convenience often leads to weak PINs being chosen
◦ Countermeasure: Use longer PINs;   pair devices only   in
private/secure environments; avoid pairing in public
Q3   a. Discuss the NIST Digital Forensics Framework along with its four phases and [10]
CO-2;
explain the advantages of using this framework
BL-2
[5 marks four phases + 5 marks advantages]
Four Phases [5 marks — 1.25 each]
• Phase 1 — Collection: Identify potential sources of digital evidence
(devices, cloud, network logs); follow chain-of-custody; acquire data
using bit-by-bit imaging; ensure integrity using hashing (MD5/SHA-
1/SHA-256)
• Phase 2 — Examination: Process raw data to make it analysis-ready;
recover deleted files, hidden data, unallocated space; extract logs, registry
entries, browser history; use tools like EnCase, FTK, Autopsy
• Phase 3 — Analysis: Interpret and correlate extracted information;
reconstruct events and timelines; identify malicious activities; correlate
logs across devices; determine attack path and tools used
• Phase 4 — Reporting: Prepare legally acceptable findings; document
methods, tools, findings, conclusions; provide screenshots and timelines;
maintain chain-of-custody records; present to court/stakeholders
Advantages [5 marks — 1 each]
• Standardized & Structured: Clear step-by-step methodology ensures
consistency across investigators and cases
• Legally Defensible: Emphasizes evidence integrity, chain-of-custody,
and proper documentation — results acceptable in court
• Tool-Independent & Flexible: Does not mandate specific tools; works for
mobile, network, memory, cloud, and IoT forensics
• Enhances Evidence Integrity: Uses hashing, secure imaging, and proper
acquisition — reduces contamination risk
• Supports Repeatability: Methodological approach ensures findings can be
reproduced if challenged in legal proceedings
********** 4 **********
--- page 5 ---
Q3   b. Enlist the advantages and disadvantages of Jailbreaking in iOS, and explain [10]
CO-1;
the four types of Jailbreaks
BL-2
[2 marks advantages + 2 marks disadvantages + 4 marks types + 2 marks
forensics]
Advantages [2 marks]
• Install apps not available on the App Store; customize UI with tweaks;
bypass Apple's walled-garden restrictions
• Access the file system directly; remove bloatware; enable advanced
functionality not permitted by Apple
Disadvantages [2 marks]
• Weakens iOS sandboxing, increases malware risk, breaks app-based
DRM and secure containers
• Voids warranty; may violate EULAs; some apps (banking, UPI) stop
working; Apple patches exploits quickly
Four Types of Jailbreak [4 marks — 1 each]
• Tethered: Device won't boot without connecting to PC after every reboot;
jailbreak is lost on each restart — least convenient
• Semi-Tethered: Device boots normally but without jailbreak features;
must connect to PC to re-enable jailbreak tweaks after reboot
• Semi-Untethered: Device boots normally; jailbreak disabled after reboot
but re-enabled via an app on the device (no PC needed) — e.g., Unc0ver,
Chimera
• Untethered: Jailbreak remains active after every reboot automatically —
no PC or app needed; rarest type as Apple patches exploits quickly
Forensic Impact [2 marks]
• Jailbroken iPhones provide full file-system access, enabling easier data
extraction using tools like Cellebrite UFED and GrayKey
• However, jailbreaking may compromise evidence integrity — data
admissibility in court may be challenged
Q4   a. Elaborate the five components used to locate User Data from a SIM Card   [10]
CO-2;
BL-2   [2 marks each component]
1. SMS — EF_SMS (2 marks)
◦ Located on UICC; records up to 176 bytes; first byte = status
(unused/sent/received); bytes 2–176 = TPDU (Transport Protocol
Data Unit)
◦ Forensic value: Status 'Unused' with content present = deleted SMS
recoverable; TPDU reveals sender, timestamp, message content
2. Contacts — EF_ADN / Abbreviated Dialing Numbers (2 marks)
◦ Under DF_Telecom (SIM) and DF_Phonebook (USIM); up to 250
records in standard ADN; thousands in global USIM phonebook
◦ Data coded in BCD format with alpha identifier (name); overflow
stored in EF_EXT1; forensic tool may miss EXT1 data
3. Fixed Dialing Numbers — EF_FDN (2 marks)
◦ Restricts outgoing calls to specific numbers only; protected by CHV2
(PIN 2); used to create a 'secret phonebook'
********** 5 **********
--- page 6 ---
◦ Forensic importance: No mobile forensic tool currently checks
EF_FDN — must be manually examined by investigator
4. Call Logs — EF_LND (Last Numbers Dialed) (2 marks)
◦ Stores last numbers dialed (up to 10 records typically); older records
overwritten in circular manner; incoming calls NOT stored on SIM
◦ Contains alpha identifier, phone number (BCD), TON/NPI,
extension byte
5. Dialing Number — EF_MSISDN (2 marks)
◦ Subscriber's own phone number(s) stored on UICC; under
DF_Telecom; not always present (carrier may omit it)
◦ Multiple MSISDN records allow one SIM to have personal, business,
and fax numbers with a single IMSI
Q4   b. Compare the Third Generation (3G), Fourth Generation (4G LTE), and Fifth [10]
CO-1;
Generation (5G) of Mobile Communication Systems in terms of speed,
BL-4
technology, latency, and applications
[3 marks 3G + 3 marks 4G + 4 marks 5G]
3G [3 marks]
• Launched: 2001 by NTT DoCoMo (Japan)
• Technologies: CDMA2000 (North America/Asia) and WCDMA/UMTS
(GSM-based global)
• Speed: Hundreds of Kbps to several Mbps; enabled mobile internet,
email, video calling, and multimedia apps
• Latency: ~100-500 ms; Applications: Mobile internet, video calling,
basic streaming
4G LTE [3 marks]
• Launched: 2009 (Sweden); ITU IMT-Advanced standard with LTE and
WiMAX (LTE became dominant)
• Technologies: LTE (Long-Term Evolution) and WiMAX; uses OFDMA
and MIMO antenna technology
• Speed: 100 Mbps to 1 Gbps peak download; Low latency: ~30-50 ms
• Applications: HD video streaming, online gaming, mobile broadband,
augmented reality
5G [4 marks]
• Launched: 2019+ globally; Technologies: New Radio (NR), Millimeter-
Wave (24 GHz+), Massive MIMO
• Speed: 1 Gbps to 100 Gbps peak; Latency: As low as 1 ms
• Massive Connectivity: Supports up to 1 million devices per sq km —
ideal for IoT and smart cities
• Applications: AR/VR, autonomous vehicles, remote surgery, industrial
automation, smart cities, mission-critical communications
Q5   a. Using a suitable diagram, show how the Secure Enclave helps build customer [10]
CO-1;
trust in iOS and describe its role in protecting biometric data, encryption keys,
BL-2
and payment credentials
********** 6 **********
--- page 7 ---
[3 marks concept/diagram + 3 marks biometric data + 2 marks
encryption keys + 2 marks payment]
Concept & Diagram [3 marks]
• The Secure Enclave is a dedicated hardware chip (co-processor) isolated
from the main application processor — analogous to TPM in PCs
• It has its own encrypted memory and runs a dedicated microkernel; even
if iOS is compromised, Secure Enclave remains protected
• Diagram concept: [Main Processor] ←→ [Secure Enclave co-processor]
←→ [Secure Storage]; the Secure Enclave never exposes raw keys
outside its boundary
Biometric Data Protection [3 marks]
• Touch ID / Face ID data (fingerprint templates and face maps) are stored
exclusively within the Secure Enclave — never uploaded to iCloud or
Apple
• Biometric data is encrypted with a key tied to the device's unique UID,
making it impossible to transfer to another device
• Authentication decisions are made entirely within the Secure Enclave;
only a pass/fail result is returned to iOS
Encryption Key Protection [2 marks]
• Encryption keys, including file protection keys and Data Protection class
keys, are stored inside the Secure Enclave
• The Secure Enclave generates and stores keys that never leave — apps
can request cryptographic operations without ever seeing the raw key
Payment Credentials [2 marks]
• Apple Pay tokenized payment credentials are managed by the Secure
Enclave; actual card numbers are never stored on the device or Apple
servers
• NFC payment transactions are authorized by the Secure Enclave,
ensuring that even a compromised iOS cannot access payment data
Q5   b. Highlight the significance of FDMA, TDMA, CDMA, and SDMA [10]
CO-1;
Multiplexing techniques used in mobile systems and compare their
BL-2
advantages and disadvantages
[2.5 marks each technique: 1 mark concept + 0.75 advantage + 0.75
disadvantage]
• FDMA — Frequency Division Multiple Access (2.5 marks)
◦ Concept: Spectrum divided into frequency bands; each user gets a
dedicated frequency band simultaneously
◦ Advantages: Simple implementation; applicable to both analog and
digital signals; simultaneous transmission
◦ Disadvantages: Low flexibility; bandwidth wastage when users are
inactive; susceptible to intermodulation distortion
• TDMA — Time Division Multiple Access (2.5 marks)
◦ Concept: Full spectrum used in time slots; users take turns — each
gets the entire frequency for a brief time frame
********** 7 **********
--- page 8 ---
◦ Advantages: Single user per slot; less complex and more flexible
than FDMA; efficient for digital voice
◦ Disadvantages: Requires   tight   synchronization;   difficult   to
implement; guard times between slots waste bandwidth
• CDMA — Code Division Multiple Access (2.5 marks)
◦ Concept: Each channel assigned a unique orthogonal chip code
sequence (+1/-1); all users share spectrum simultaneously using
different codes
◦ Advantages: Highly efficient spectrum use; less interference;
supports more users per frequency band
◦ Disadvantages: Lower data transmission rates; complex receiver
design; near-far problem if power control is poor
• SDMA — Space Division Multiple Access (2.5 marks)
◦ Concept: Combines FDM and TDM concepts; spatial separation of
signals using directional antennas; cells reuse frequencies
◦ Advantages: High data transmission rate; optimal use of time and
frequency bands; basis of cellular frequency reuse
◦ Disadvantages:   Interference problems between   cells;   high
infrastructure costs; complex frequency planning
Q6   a. Classify the guidelines for searching and seizing a mobile device for forensics [10]
CO-2;
including scene documentation, network isolation, evidence packaging, and
BL-2
chain of custody
[1 mark each for 10 guidelines]
1. Document the Scene: Photograph the device's location; record date, time,
condition, and contextual details before any action
2. Wear Gloves: Avoid contaminating fingerprint or DNA evidence; handle
device with sterile gloves
3. Power Off the Device: If powered on, turn it off to prevent remote wipe,
data modification, or network communication; if off — do not power on
4. Network Isolation: Place device in Faraday bag immediately to block all
RF signals (GSM/Wi-Fi/Bluetooth/GPS) and prevent remote access or wipe
5. Document Device Details: Record make, model, IMEI, serial number,
carrier, condition, and any visible security mechanisms (passcode/biometrics)
6. Collect All Accessories: Seize chargers, SIM cards, microSD cards, cables,
and cases together as associated evidence
7. Evidence Packaging: Place in clean evidence bag with tamper-evident
seals; use anti-static or Faraday bags for electronics
8. Chain of Custody Documentation: Label bag with case number, date, time,
location, collector's name; record every person who handles the device
9. Transport Securely: Transport to forensic lab under controlled conditions;
maintain evidence integrity during transit
10. Notify Authorities: Follow legal protocols; obtain necessary warrants;
notify relevant law enforcement and document all legal authorizations
Q6   b. Enlist the System Access Threats to wireless devices and explain the ways to [10]
CO-1;
mitigate each threat
BL-2
[3 marks DoS + 4 marks Evil Twins + 3 marks Rogue APs]
********** 8 **********
--- page 9 ---
1. Denial of Service (DoS) Attacks [3 marks]
• WLANs vulnerable to both network-based DoS and radio-based jamming
attacks
• Radio jamming: Powerful transmitter creates interference on 2.4 GHz
band, blocking all Bluetooth/Wi-Fi communication
• Mitigation: Use less-crowded 5 GHz band; spread-spectrum modulation
(FHSS/DSSS); frequency hopping to avoid jamming
2. Evil Twin Access Points [4 marks]
• Attacker configures rogue AP with same SSID (ESSID) as legitimate
network; devices auto-connect to strongest signal
• 802.11 management packets easily forged; WEP/WPA2 cannot prevent
association with evil twin (encryption only activates post-association)
• Setup: Attacker uses tools like Hotspotter, Airshark, or NetStumbler to
capture legitimate SSID; runs software-based AP on laptop
• Mitigation: Disable auto-connect; use VPN on public Wi-Fi; check
HTTPS padlock; use 802.1X certificate-based authentication; enable
MAC address randomization
3. Rogue Access Points [3 marks]
• Unauthorized APs installed in a building — either by frustrated
employees (dead zones) or attackers who gain physical access
• Corporate network unaware of rogue AP; creates an unmonitored entry
point into internal network
• Mitigation: Regular RF site surveys; wireless intrusion prevention
systems (WIPS); enforce physical security; MAC address filtering on
network
Q7   a. Explain the Sandboxing mechanism and File System Permissions on Android, [10]
CO-1;
and describe how they work together to prevent privilege escalation attacks at
BL-2
the kernel level
[5 marks sandbox + 5 marks file system permissions & privilege
escalation]
Android Sandbox [5 marks]
• Android is built on the Linux kernel; uses Linux's multiuser model to
isolate applications
• Each app is assigned a unique User ID (UID) and runs as a separate Linux
process with its own Dalvik/ART VM instance
• This configuration isolates each app's files, resources, devices, and
memory from all other apps
• Inter-process communication (IPC) is fully controlled; a memory crash
in one app cannot compromise other apps or the OS
• Even malicious code executing after a crash is confined to the affected
app's UID and cannot 'leak' to other applications
File System Permissions [5 marks]
• Linux file system permissions enforce that one UID (app) cannot read,
write, or execute files belonging to another UID
********** 9 **********
--- page 10 ---
• Files created by App A cannot be accessed by App B unless App A
explicitly declares a content provider or shared permission
• Privilege Escalation Attack: If an attacker gains root access, they bypass
this model — all UID boundaries are rendered ineffective
• Android SDK Security Features prevent privilege escalation:
◦ ProPolice: Prevents stack buffer overflows
◦ No-eXecute (NX): Hardware parameter preventing code execution
on the stack or heap
◦ ASLR (Address Space Layout Randomization): Randomizes
memory addresses to prevent predictable exploits
• Only the OS kernel and a small subset of core applications run with root
permissions — all user-installed apps run with limited UID privileges
Q7   b. Describe the contents of a Standard Operating Procedure (SOP) Document [10]
CO-2;
used in mobile forensic investigations and explain the importance of each
BL-2
section for maintaining forensic integrity
[1 mark each for 10 sections]
1. Title Page: SOP title, organization name/logo, document version number,
creation/revision date, author(s) or department
2. Table of Contents: Lists sections, subsections, and page numbers for easy
navigation
3. Introduction (Purpose & Scope): Purpose — seize, secure, and collect
digital data from mobile device at off-site location; Scope — outlines
procedures for mobile forensic assistance at off-site location (not a training
document)
4. Definitions: Lists and defines all acronyms and technical terms used in the
procedural sections
5. Equipment: Lists all items required to successfully accomplish the
procedure (Faraday bags, forensic tools, evidence bags, gloves, etc.)
6. General Information: Defines limitations and background information
regarding performing the duties outlined in the SOP
7. Objective: Specific goals of the forensic examination — determining
authenticity, preserving integrity, supporting legal proceedings
8. Responsibilities: Outlines roles of forensic examiners; specifies who is
responsible for collection, analysis, comparison, and reporting
9. Procedure: Step-by-step instructions for document collection, preservation,
examination, analysis, and reporting
10. Quality Assurance, References, Appendices, Revision History: Peer
review procedures; cited standards; sample forms; record of SOP changes
over time
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 0ddae3b9dfbf

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CyberSecurity_7010/Mobile Device Security and Forensics/ANS_Mobile Device Security and Forensics(702IT0E019)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Mobile Device Security and Forensics
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figures in brackets on the right-hand side indicate full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary
Q1   Answer briefly:   Marks
CO-1;   a. Explain the Multimedia Requirements for Wireless Networks (Voice, Data, [5]
BL-2
Video) and why a one-size-fits-all protocol does not work
[2 marks table + 3 marks why one-size-fits-all fails]
• Wireless networks must support three main media types, each with
fundamentally different QoS requirements:
◦ Voice: 8-32 Kbps; Delay <100ms; Packet Loss <1%; BER 10⁻³;
Continuous traffic
◦ Data: 1-100 Mbps; No delay constraint; Zero packet loss; BER 10⁻⁶;
Bursty traffic
◦ Video: 1-20 Mbps; Delay <100ms; Packet Loss <1%; BER 10⁻⁶;
Continuous traffic
• Why One-Size-Fits-All Fails:
◦ Voice tolerates some loss but is very delay-sensitive; data cannot
tolerate any loss but delay is irrelevant
◦ A protocol optimized for data reliability (retransmission) adds delay
— unacceptable for real-time voice
◦ Wired networks attempted this approach with poor results; wireless
systems require adaptive, application-aware QoS mechanisms
CO-1; b. Explain how Evil Twin Access Points are set up by attackers and describe the [5]
BL-2
threats they pose to wireless users
[2 marks how set up + 3 marks threats]
• How Evil Twin is Set Up:
********** 1 **********
--- page 2 ---
◦ Attacker uses tools like Hotspotter, Airshark, or NetStumbler to
capture the ESSID of a legitimate WLAN
◦ Runs a software-based AP on a laptop (not a hardware AP) configured
with the same SSID — often near the victim client
◦ Most devices auto-connect to the AP with the strongest signal; 802.11
management packets are easily forged — devices cannot verify AP
identity
• Threats Posed:
◦ Eavesdropping / MITM: All user traffic passes through attacker's
device — credentials, passwords, session tokens stolen
◦ Phishing: Captive portal injects fake login pages to harvest
credentials for banking, email, social media
◦ Neither WEP nor WPA/WPA2 prevents association with evil twin —
encryption only activates after association
CO-2;   c. Describe the role of Chain of Custody in Mobile Forensics and explain why it [5]
BL-2
is critical for evidence admissibility in court
[2 marks definition + 3 marks importance]
• Definition: A documented record of every individual who handles digital
evidence — from the moment of collection through analysis, storage, and
court presentation
• What is Documented: Device make/model/IMEI/condition; collector's
identity; date/time of every transfer; storage location; any changes in
custody
• Importance — Evidence Admissibility: Courts require proof that evidence
was not tampered with; unbroken CoC demonstrates integrity
• Importance — Legal Defensibility: Investigators can testify clearly about
who had access to the device at every stage — prevents defence challenges
• Importance — Forensic Integrity: Ensures forensic image matches
original device (verified by hash values); CoC links hash verification to
each transfer of custody
CO-2; d. Discuss the significance of the ICCID and IMSI numbers stored on a SIM Card [5]
BL-2
and their use in mobile forensics
[2.5 marks ICCID + 2.5 marks IMSI]
• ICCID — Integrated Circuit Card Identifier (2.5 marks)
◦ Unique serial number of the UICC (up to 20 digits); printed on SIM
exterior
◦ Structure: System Code (89) + Country Code + Issuer ID + UICC
Number + Checksum
◦ Forensic use: Uniquely identifies the SIM card; if PIN-locked,
examiner uses ICCID to obtain PUK from carrier
• IMSI — International Mobile Subscriber Identity (2.5 marks)
◦ Unique subscriber identifier (15 digits): MCC (country) + MNC
(network) + MSIN (subscriber)
◦ Required in GSM and CDMA networks for all call delivery, data, and
transactional information
◦ Forensic use: Identifies subscriber's home country and carrier; links
the SIM/device to a specific registered user account
********** 2 **********
--- page 3 ---
Q2   a. Explain the following terms associated with SIM Card and UICC forensic [10]
CO-2;
analysis:
BL-3
[2 marks each]
i) ICCID — Integrated Circuit Card Identifier (2 marks)
◦ Unique serial number of the UICC (up to 20 digits); structure: System
Code (89) + Country Code + Issuer ID + UICC Number + Checksum
◦ Forensic use: Uniquely identifies the SIM; enables retrieval of PUK
from carrier when PIN-locked
ii) IMSI — International Mobile Subscriber Identity (2 marks)
◦ 15-digit unique subscriber ID: MCC (3 digits) + MNC (2-3 digits) +
MSIN; identifies subscriber on the cellular network
◦ Forensic use: Links device/SIM to registered subscriber; identifies
country and carrier of use
iii) 2FF / 3FF / 4FF / Embedded UICC Form Factors (2 marks)
◦ 1FF (ID-1): Credit card size — never used in mobile; 2FF (Plug-in):
Used in feature phones until 2004; 3FF (Mini-UICC): Used until
2012; 4FF (Nano-UICC): Current standard in modern smartphones
◦ Embedded UICC (MFF2): Soldered to PCB; used in IoT, automotive,
wearables; eSIM requires different forensic acquisition tools
iv) FPLMN — Forbidden Public Land Mobile Network (2 marks)
◦ EF under DF_GSM listing networks that rejected the device's location
update (MCC+MNC pairs); holds up to n records with circular
overwrite
◦ Forensic use: Can prove device was in a specific country/region even
if user denies it
v) TPDU — Transport Protocol Data Unit (2 marks)
◦ Content bytes 2–176 of the EF_SMS record; contains message data
depending on type: SMS-SUBMIT (sent) or SMS-DELIVER
(received)
◦ Includes: originating/destination address, timestamp, message
encoding (7-bit GSM / UCS2), message reference number
Q2   b. Describe the working of Bluetooth along with its Security Modes 1, 2, 3, and [10]
CO-1;
4, and explain how Secure Simple Pairing enhances security
BL-3
[4 marks working + 4 marks security modes + 2 marks SSP]
Working of Bluetooth [4 marks]
• Bluetooth is a Wireless PAN (WPAN) operating on the 2.4 GHz ISM band
• Uses Adaptive Frequency Hopping (AFH) spread spectrum — hops across
79 frequencies, changing 1,600 times per second to avoid interference
• Range: ~10 m (up to 100 m with amplifiers); supports both voice and data;
no line-of-sight required
• Piconet: One master + up to 7 active slaves; Scatternet: Multiple
overlapping piconets
Security Modes [4 marks]
• Mode 1 (No Security): No security features — device is non-secure;
vulnerable to all attacks
********** 3 **********
--- page 4 ---
• Mode 2 (Service-Level Security): Authorization required before accessing
certain services; security enforced after connection
• Mode 3 (Link-Level Security): Security enforced before physical link is
established; authentication and encryption are mandatory for   all
connections
• Mode 4 (Secure Simple Pairing — SSP): Introduced in Bluetooth 2.1;
service-level mode using SSP for secure pairing
Secure Simple Pairing (SSP) [2 marks]
• SSP uses Elliptic Curve Diffie-Hellman (ECDH) for key exchange,
making pairing more secure and user-friendly
• SSP methods: Numeric Comparison, Passkey Entry, Just Works, Out of
Band (OOB) — each suited to different device capabilities
Q3   a. Discuss the procedures to collect a mobile device from a crime scene, [10]
CO-2;
including documentation, isolation from network, and evidence bagging
BL-2
[1 mark each for 10 steps]
1. Document the Scene: Photograph and note device location, surroundings,
date, time, and condition before touching anything
2. Ensure Safety and Integrity: Wear gloves; avoid unnecessary handling;
preserve potential fingerprints or DNA evidence
3. Power Off the Device: If ON, power it off to preserve current state and
prevent remote wipe or data alteration; if already OFF, do not power on
4. Document Device Details: Record make, model, serial number (IMEI/ESN),
carrier, security mechanisms (passcode, biometrics, encryption)
5. Collect Device and Accessories: Collect chargers, cables, SIM cards,
memory cards, and protective cases together as potential evidence
6. Bagging and Sealing: Place device in a clean sterile evidence bag; use
Faraday bags to prevent remote tampering / wiping; seal with tamper-evident
seals
7. Labelling and Chain of Custody: Label bag with case number, date, time,
location, description, collector's name; document chain of custody
8. Transport and Storage: Transport securely to forensic lab; store in a
controlled-access location until processed by trained examiners
9. Document Collection Process: Record all steps taken, observations,
individuals involved, and any deviations from standard procedures
10. Notify Relevant Authorities: Inform law enforcement and follow
established evidence-handling and chain-of-custody protocols
Q3   b. Compare the Android Security Model and Apple Security Model across 5 [10]
CO-1;
unique dimensions including sandboxing, encryption, app provenance,
BL-3
permission model, and rooting / jailbreaking
[2 marks each dimension]
1. Sandboxing (2 marks)
◦ Android: Each app runs in its own Linux process with a unique UID;
Dalvik/ART VM isolated; no inter-app data leakage
◦ iOS: Each app is sandboxed in its own container; cannot access other
app data unless explicitly granted; based on FreeBSD UNIX security
model
********** 4 **********
--- page 5 ---
2. Encryption (2 marks)
◦ Android: File-Based Encryption (FBE) mandatory from Android 10+;
Adiantum for low-power devices; keys derived from user credentials
◦ iOS: Hardware-based encryption enabled by default; tied to user
passcode + device UID; Full-disk encryption with Secure Enclave
3. App Provenance (2 marks)
◦ Android: Apps can be side-loaded from third-party sources; Google
Play Protect scans apps but not mandatory
◦ iOS: Strict App Store review — only digitally signed apps from
registered developers allowed; digital certificate ensures code
integrity
4. Permission Model (2 marks)
◦ Android:   Runtime   permissions   (Android   6.0+);
Normal/Dangerous/Signature permission categories; user grants at
runtime
◦ iOS: Permission-based access; user prompted at first use; granular
control per app for camera, location, contacts, etc.
5. Rooting / Jailbreaking (2 marks)
◦ Android: Rooting via bootloader unlock + SU binary; breaks security
protections; full partition access for forensics
◦ iOS: Jailbreaking uses iOS exploits; bypasses Apple restrictions;
provides full file-system access; four types (tethered to untethered)
Q4   a. Elaborate the components used to locate Network Information Data from a [10]
CO-2;
SIM Card and explain the forensic significance of ICCID, IMSI, FPLMN, and
BL-3
the ciphering key (Ki)
[2.5 marks each component]
1. ICCID — Integrated Circuit Card Identifier (2.5 marks)
◦ Up to 20 digits; unique serial number of the UICC; printed on exterior
of SIM
◦ Structure: System Code (89) + Country Code + Issuer Identifier +
UICC Number + Checksum
◦ Forensic use: Identify the specific SIM; if SIM is PIN-locked, ICCID
allows examiner to obtain PUK from carrier
2. IMSI — International Mobile Subscriber Identity (2.5 marks)
◦ Unique subscriber identifier on the cellular network; 15 digits = MCC
(3) + MNC (2-3) + MSIN
◦ Required in GSM and CDMA networks for call delivery and network
registration
◦ Forensic use: Identifies subscriber's home country and carrier; links
device to a specific user account
3. FPLMN — Forbidden Public Land Mobile Network (2.5 marks)
◦ EF under DF_GSM; lists networks that rejected the device's location
update (no roaming agreement)
◦ Can hold up to n records (MCC+MNC pairs); circular overwrite when
full
◦ Forensic use: Can prove device was used in a specific country even if
user denies it
4. Ciphering Key (Ki) (2.5 marks)
********** 5 **********
--- page 6 ---
◦ Secret authentication key stored on SIM — essential for network
authentication process
◦ Although present on all SIM cards, Ki is inaccessible to forensic
examiners using any forensic software
◦ Forensic significance: Its existence is acknowledged but cannot be
extracted — understanding this limitation is critical for investigators
Q4   b. Describe the features and key technologies of 5G including New Radio (NR), [10]
CO-1;
Millimeter-Wave spectrum, and Massive MIMO, along with the applications
BL-2
enabled by 5G
[3 marks NR + 3 marks mmWave + 2 marks Massive MIMO + 2 marks
applications]
New Radio (NR) [3 marks]
• Foundational air interface technology for 5G; defines how devices
communicate wirelessly over the airwaves
• Highly flexible design: accommodates diverse use cases and frequency
bands (sub-6 GHz and mmWave)
• Enables both eMBB (enhanced mobile broadband) and URLLC (ultra-
reliable low-latency communication) applications
Millimeter-Wave Spectrum [3 marks]
• Uses frequencies of 24 GHz and above; significantly larger bandwidths
enabling ultra-fast data rates
• Allows extremely high data speeds — up to 100 Gbps in ideal conditions;
supports massive device density in dense urban areas
• Challenge: Short range and poor penetration through walls; mitigated
using beamforming and small cell densification
Massive MIMO [2 marks]
• Deploys large number of antennas at base station (64-256+); enables
simultaneous multi-user spatial multiplexing
• Benefits: Increased data throughput, enhanced coverage, improved
spectral efficiency — critical for 5G's capacity targets
Applications [2 marks]
• IoT & Smart Cities: Connects up to 1 million devices per sq km; enables
smart traffic, energy, healthcare management
• AR/VR, autonomous vehicles, remote surgery, industrial automation —
all enabled by 5G's ultra-low latency and massive bandwidth
Q5   a. Explain the Android Sandbox mechanism and describe how File System [10]
CO-1;
Permissions enforced by the Linux kernel prevent privilege escalation and
BL-2
inter-application data leakage
[5 marks sandbox mechanism + 5 marks file system permissions]
Android Sandbox Mechanism [5 marks]
• Foundation: Android built on Linux kernel; uses Linux multiuser model
to isolate applications from each other
********** 6 **********
--- page 7 ---
• Unique UID per App: Android security system assigns a unique User ID
(UID) to each installed application
• Process Isolation: Each app runs in its own Dalvik/ART VM instance as a
separate Linux process with its own permissions
• Isolation Scope: Extends to OS libraries, application frameworks, and
runtime — isolates files, resources, devices, and memory
• Memory Safety: A memory crash in App A cannot compromise App B;
arbitrary code execution is confined to the crashed app's UID and
permissions
File System Permissions & Privilege Escalation Prevention [5 marks]
• Linux Permission Model: Each file is owned by a UID; other UIDs cannot
read, write, or execute it without explicit permission
• Inter-App Isolation: Files created by App A cannot be accessed by App B
unless App A declares a Content Provider with explicit access grants
• Privilege Escalation Attack: Attacker tries to gain root UID — breaks all
sandbox boundaries; Android mitigates this with:
◦ ProPolice: Prevents stack buffer overflow attacks
◦ No-eXecute (NX) bit: Prevents code execution from stack/heap
memory regions
◦ Integer overflow protection and format string protection in memory
allocation
• Only Kernel & Core Apps have Root: Reduces attack surface — user-
installed apps cannot escalate to root without exploiting a kernel
vulnerability
Q5   b. Explain the five key parameters that impact the design of wireless systems: [10]
CO-1;
delay   constraints,   energy   constraints,   interference,   mobility, and
BL-2
heterogeneous application requirements
[2 marks each parameter]
1. Delay Constraints (2 marks)
◦ Voice and video require <100 ms delay; data has no strict delay
constraint
◦ Real-time applications (VoIP, gaming) mandate low latency; protocol
stack must minimize processing and queuing delays
2. Energy Constraints (2 marks)
◦ Mobile devices run on limited batteries; transmit energy minimized
by maximizing bit time but circuit energy increases with bit time —
creating a delay vs energy tradeoff
◦ Sleep modes save energy but complicate networking; bit allocation
must be optimized across all protocol layers
3. Interference (2 marks)
◦ Wireless channels are shared broadcast media; co-channel
interference occurs between cells using the same frequency
◦ Modulation techniques (OFDM, CDMA), power control, and
frequency planning are used to mitigate interference
4. Mobility (2 marks)
◦ User locations, traffic patterns, and network conditions change
constantly; system must support seamless handoff between cells
********** 7 **********
--- page 8 ---
◦ Crosslayer design must adapt — dynamic resource allocation,
mobility management, and handoff protocols are essential
5. Heterogeneous Application Requirements (2 marks)
◦ Voice (8-32 Kbps, <100 ms delay, <1% loss), data (1-100 Mbps, 0
loss), video (1-20 Mbps, <100 ms delay) — all different QoS needs
◦ One-size-fits-all protocols fail; adaptive QoS mechanisms must
allocate resources dynamically based on application type
Q6   a. Discuss the Device Control Threats to wireless devices including unauthorized [10]
CO-2;
clients, ad hoc connections, endpoint attacks (Metasploit), Bluetooth Wi-Fi
BL-3
hacks, and NFC proximity hacking, and explain mitigation strategies for each
[2 marks each threat: 1 mark description + 1 mark mitigation]
1. Unauthorized & Modified Clients (2 marks)
◦ User’s jailbreak/root devices or create hotspots without security,
creating backdoors; corporate network treats them as authorized
clients
◦ Mitigation: MDM (Mobile Device Management) policies; enforce
device compliance; block non-compliant devices from network access
2. Ad Hoc Connections & Software-Based Access Points (2 marks)
◦ Ad hoc networks easily set up using modern smart devices; easily
exploited as they bypass normal network security controls
◦ Mitigation: Disable ad hoc networking in corporate policy; use MDM
to prevent mobile hotspot creation without security
3. Endpoint Attacks — Metasploit (2 marks)
◦ Metasploit probes Wi-Fi   clients   for thousands   of known
vulnerabilities; once exploited, Wi-Fi client can be fully controlled
and monitored
◦ Mitigation: Regular firmware and OS updates; disable unnecessary
network services; network segmentation
4. Bluetooth Wi-Fi Hacks (2 marks)
◦ Bluetooth set to non-discovery by default; if user enables discovery,
hackers can gain access to and control mobile devices using BT
exploits
◦ Mitigation: Keep Bluetooth off or in non-discoverable mode; restrict
BT in BYOD policy; apply firmware patches regularly
5. NFC & Proximity Hacking (2 marks)
◦ NFC enables automatic ad hoc connection between devices within
inches; used for payments and data exchange; pairing is automatic (no
user consent)
◦ Mitigation: Disable NFC when not in use; use tokenized payment
systems; be alert to proximity in crowded areas
Q6   b.   Illustrate the complete forensic process and procedure for mobile devices [10]
CO-1;
covering all 10 steps from identification of digital evidence to storage and
BL-3
preservation of the forensic image
[1 mark each step]
1. Identification of Digital Evidence: Identify mobile devices containing
relevant evidence — smartphones, tablets, wearables associated with the case
********** 8 **********
--- page 9 ---
2. Securing the Scene: Secure crime scene; restrict unauthorized access;
prevent contamination, damage, or tampering with the device
3. Documentation and Chain of Custody: Document device make, model, serial
number (IMEI), condition; establish chain of custody recording every handler
4. Acquisition of Digital Evidence: Use forensic tools (Cellebrite UFED,
Magnet AXIOM) to create bit-by-bit forensic image of internal memory, SIM,
and microSD
5. Data Extraction and Analysis: Analyze forensic image for call logs, SMS,
emails, photos, videos, contacts, browsing history, and app data
6. Recovery of Deleted Data: Employ file carving and forensic techniques to
recover deleted messages, files, or artifacts from storage
7. Verification and Validation: Verify integrity of acquired data using
MD5/SHA-256 hash comparison; ensure forensic image matches original
device
8. Reporting and Documentation: Prepare comprehensive report documenting
methods, findings, analysis results, and conclusions for legal proceedings
9. Expert Testimony: If required, forensic examiner provides court testimony
explaining findings, methodologies, and evidence interpretations objectively
10. Storage and Preservation of Evidence: Store forensic image and all
evidence securely in controlled-access facility for future legal proceedings or
re-analysis
Q7   a. Explain the Sandbox and Application Provenance features in iOS and describe [10]
CO-1;
how they work together to ensure application integrity, user trust, and
BL-3
resistance to malware
[5 marks iOS Sandbox + 5 marks Application Provenance]
iOS Sandbox [5 marks]
• iOS is based on Apple's OS X (derived from FreeBSD UNIX); security
model based on access control, app security, encryption, and isolation
• Each app is confined to its own sandbox container — cannot access files,
data, or resources of other apps
• System resources (contacts, camera, microphone, location) are accessible
only via permission-based APIs — user must explicitly grant access
• Even compromised apps cannot break out of the sandbox to attack the OS
or other apps — hardware-enforced isolation
• Jailbreaking bypasses sandboxing — weakens isolation, increases
malware risk, breaks DRM and secure containers
Application Provenance [5 marks]
• Apple's Walled Garden: Apps distributed exclusively through the App
Store; developers must register, pay, and receive a digital certificate
• Only digitally signed apps from authorized developers can be uploaded —
digital signature ensures code integrity post-release
• Apple tests all apps for security and malware before approval; rogue
developers are identified, banned, and possibly prosecuted
• Digital certificate makes it impossible for cybercriminals to modify or
tamper with released apps — attackers must create new apps from scratch
********** 9 **********
--- page 10 ---
• Limitations: Spoofing is possible (stolen developer identity); however, the
accountability mechanism has proven effective — very little malware
targets non-jailbroken iOS devices
Q7   b.   Illustrate the approaches and best practices to protect personal data if a mobile [10]
CO-2;
phone is lost or stolen, covering remote wipe, device lock, IMEI blocking,
BL-3
iCloud/Google account security, and law enforcement reporting
[2 marks each approach]
1. Remote Wipe (2 marks)
◦ iOS: Find My iPhone → Erase iPhone; Android: Find My Device →
Erase Device — completely wipes data remotely
◦ Best practice: Enable before device is lost; requires active internet on
device or will execute on next connection
2. Device Lock (2 marks)
◦ Use strong passcode + biometrics (Face ID / Fingerprint); enable
Auto-Lock after short idle period
◦ Prevents casual access; combined with iOS Secure Enclave / Android
encryption, makes data extraction extremely difficult even with
physical access
3. IMEI Blocking (2 marks)
◦ Report IMEI to carrier — carrier blacklists IMEI blocking the device
from connecting to any network
◦ Internationally shared IMEI blacklists (GSMA IMEI database)
prevent use across different carriers and countries
4. iCloud / Google Account Security (2 marks)
◦ Change iCloud/Google account password immediately; enable 2FA
to prevent account takeover
◦ Revoke app access tokens and active sessions from iCloud/Google
account settings — prevents attacker using synced credentials
5. Law Enforcement Reporting (2 marks)
◦ File police report with device IMEI, make/model, date/time/location
of loss — IMEI can be tracked via carrier cooperation
◦ Forensic teams can use IMEI and ICCID to trace device movements
through network tower records
********** 10 **********
````

## 2024-25 · Final-Exam · Sem 12 · Answer key · paper 5aadd54fc385

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2024/Sem_12/Final-Exam/Integrated_Computer_7032/Mobile Device Security and Forensics/ANS_Mobile Device Security and Forensics(702IT0E019)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2025
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER ENGINEERING) SIX YEARS
INTEGRATED PROGRAM
Year: VI/Semester XII(Exam Year: 2024-2025)
Subject: Mobile Device Security and Forensics
Date: 12 May 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 17 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   Answer the following
[20]
CO-1; SO-   What is a cellular coverage map? What factors influence cellular coverage?
3;   a.   [05]
BL-2
●   Cellular coverage maps are graphical representations showing the geographic areas where a mobile
network (like those of Verizon, AT&T, or Vodafone) offers service.
● These maps help users understand the strength and availability of the signal in different locations.
● The coverage is typically depicted with different colors or shading to indicate signal strength or the
type of network available (2G, 3G, 4G, 5G).
Factors influence Cellular Coverage Maps:
● Signal Strength: Often shown as a gradient (e.g., red for strong signals, yellow for weak signals),
representing how well a device can connect to the network in specific areas.
● Network Type: Coverage maps may indicate which network technology (e.g., 2G, 3G, 4G LTE, 5G) is
available in a given area.
● Geographical Area: These maps cover urban, suburban, rural, and remote areas. They can help users
plan where they’ll likely get the best service or identify areas where coverage might be sparse or
absent.
● Topography: Mountains, valleys, and other natural barriers can block signals, reducing coverage.
●   Infrastructure: The density of cell towers and antennas in an area influences signal strength.
● Obstructions: Buildings, large structures, and even trees can interfere with signals, leading to weaker
reception.
● Network Load: The number of users accessing the network in a particular area can affect speed and
quality of service.
CO-1; SO-   Give and explain any 3 security threats to mobile devices.
2;   b.   [05]
BL-2
There are a number of threats to mobile devices, including annoyance, stealing money, invading privacy,
propagation, and malicious tools.
********** 1 **********
--- page 2 ---
●   Botnets: attackers infect multiple machines with malware that victims generally acquire via e-mail
attachments or from compromised applications or websites. The malware then gives hackers remote
control of “zombie” devices, which can then be instructed to perform harmful acts.
● Malicious applications: hackers upload malicious programs or games to third-party smartphone
application marketplaces. The programs steal personal information and open backdoor
communication channels to install additional applications and cause other problems. Malicious links
on social networks: an effective way to spread malware where hackers can place Trojans, spyware,
and backdoors.
● Spyware: hackers use this to hijack phones, allowing them to hear calls, see text messages and e-mails
as well as track someone’s location through GPS updates.
CO-2;   Differentiate between Security Enclaves and Trusted Execution Environment?
SO-3;   c.   [05]
BL-4
CO-2; SO-   What is the purpose and use of Magnet AXIOM and Oxygen Forensic
3;   d.   Detective in forensic analysis?   [05]
BL-3
Magnet AXIOM
●   Extracts and analyzes data from smartphones, computers, and cloud storage.
● Recovers deleted files, conversations, and location history.
● Supports advanced analytics and reporting.
Oxygen Forensic Detective
●   Extracts data from mobile devices, SIM cards, and cloud services.
● Includes password-cracking capabilities.
● Supports drone and IoT device forensics.
Q2   What is Handover? What are the different types of Handovers in mobile
CO-1; SO-   a.   communication?   [10]
2;
BL-4
Handoff (or handover) refers to the process where a mobile device switches from one cell tower or base
station to another as it moves. This process is crucial for maintaining uninterrupted communication, especially
during calls or data sessions, as users travel or change locations.
1.Hard Handoff:
********** 2 **********

[Text in pictures on this page, read by OCR]
Trusted Execution Environment

Feature (TEE) Secure Enclave
Location Inside the main processor Separate co-processor
Protection High Higher

Level

Purpose Secure app execution Secure keys &

biometrics
--- page 3 ---
1.In a hard handoff, the device loses its connection to the first cell tower before connecting to the next
one. This type of handoff is usually seen in older 2G or 3G networks.
2.It might result in a brief drop in the connection, such as a small gap in a voice call or data session.
2.Soft Handoff:
1.Soft handoff happens in 3G, 4G, and 5G networks. In this case, the device is connected to both the
old and new cell towers simultaneously during the transition.
2.This process ensures a more seamless handoff with no interruptions in service, which is particularly
important for real-time communications like voice calls.
3. Intra-cell Handoff: When the device moves from one sector or antenna of the same cell tower to another
sector of the same tower.
4. Inter-cell Handoff: When the device switches between two different cell towers (either within the same
network or across different networks).
5. Inter-system Handoff: This occurs when the device switches between two different types of networks (e.g.,
moving from a 4G to a 5G network).
Q2   What are the security issues with Bluetooth devices?
CO-1,2;   b.   [10]
SO-2;
BL-4
Bluetooth can pose security risks if not correctly implemented or configured. Here are some common security
issues with Bluetooth and ways to mitigate them:
•Eavesdropping: Bluetooth signals can be intercepted by third-party devices within range, allowing hackers
to access sensitive information such as personal contacts and messages. To prevent eavesdropping, it is
essential to use strong encryption when transmitting sensitive data and to disable Bluetooth when not in use.
•Man-in-the-Middle Attacks: Bluetooth connections can be intercepted by a hacker who poses as a legitimate
device to gain access to sensitive information. To prevent man-in-the-middle attacks, it is important to verify
the authenticity of devices before connecting to them and to use secure authentication protocols.
•Unauthorized Access: Bluetooth devices can be configured to be discoverable, making them vulnerable to
unauthorized access. To prevent unauthorized access, it is vital to configure devices to be non-discoverable
and to use strong passwords or PINs to secure them.
Q3   What are the IOS sandbox security features? Give any 3 vulnerabilities in IOS.
CO-1,2;   a.   [10]
SO-3;
BL-2
Apple’s iOS sandboxing is a critical security mechanism designed to isolate apps from each other and the
system, preventing unauthorized access and enhancing user privacy. It ensures that apps run in a restricted
environment, limiting their ability to interact with other apps and sensitive system files.
Key Security Features of iOS Sandboxing
1. App Isolation (Sandboxing)
● Each app runs in its own isolated container.
●   It cannot access other app data or system files unless explicitly permitted.
● Prevents malware from spreading across the system.
Example: A malicious app cannot read your WhatsApp messages or steal Facebook credentials.
2. Restricted File System Access
********** 3 **********
--- page 4 ---
● Apps can only access files within their sandboxed directory:
○ /private/var/mobile/Containers/Data/Application/{App_ID}/
● System files and other app data are off-limits.
● Temporary files are stored in /tmp but are deleted when the app is closed.
Example: A photo editing app can’t access photos from another app unless the user grants permission.
3. App Permissions (User Consent via App Store Guidelines)
● iOS requires explicit user permission for sensitive data access (e.g., Camera, Microphone, Location,
Contacts).
● Permissions are managed via the Privacy Settings (Settings → Privacy & Security).
● Apps must declare permissions in Info.plist before requesting access.
Example: An app cannot secretly record audio without microphone permission.
4. Inter-Process Communication (XPC & URL Schemes Restrictions)
● iOS limits direct communication between apps.
● Apps use XPC (Cross Process Communication) or URL Schemes with system-defined restrictions.
● Prevents unauthorized data exchange between apps.
Example: A malicious app cannot directly send commands to another app without permission.
Despite the robust security architecture, iOS has its vulnerabilities, and Apple continually addresses them via
patches and updates. Some common concerns include:
•Zero-day exploits: Hackers often target undisclosed vulnerabilities.
•Phishing: Malicious apps or websites that trick users into revealing sensitive information.
•App permissions abuse: Even with iOS’s permission-based model, users may inadvertently grant access to
sensitive data.
•Malicious enterprise apps: Although rare, there have been incidents of malware spreading through
unauthorized enterprise certificates.
Apple mitigates these risks through rapid updates, app vetting, and App Store guidelines.
Q3   Explain the process of maintaining the chain of custody for a mobile device
CO-3; SO-   b.   from its seizure at a crime scene to its presentation as evidence in court. What   [10]
1;   specific steps, documentation, and handling procedures are required at each
BL-4   stage to ensure the device’s integrity and prevent tampering or
contamination?
Stage 1: Seizure at the Crime Scene
Objective: Secure and document the mobile device as evidence.
Steps:
********** 4 **********
--- page 5 ---
1. Identify & Isolate the Device
○ Locate the mobile device.
○ Prevent remote access (put the phone in Airplane Mode or use a Faraday bag to block signals).
2. Photograph & Document the Device
○ Take photos from all angles (front, back, screen status, physical condition).
○ Note device make, model, IMEI number, serial number, and visible damage.
3. Label & Secure the Evidence
○ Place the device in a tamper-proof evidence bag.
○ Label with case number, date, time, investigator’s name, and location of seizure.
○   If possible, power off the device safely (if forensic policies allow).
4. Seize Associated Accessories
○ Include SIM cards, SD cards, chargers, and external storage.
5.   Fill Out the Chain of Custody Form
○ Record who collected the evidence, time, date, and location.
○ Each handoff must be logged.
Stage 2: Transport & Storage
Objective: Securely transport and store the device to prevent tampering.
Steps:
1. Transport in a Secure Evidence Container
○ Use a Faraday bag or evidence box to block signals.
○ Maintain a sealed and documented chain of custody during transportation.
2. Log Entry into the Evidence Storage System
○   Store in a restricted access evidence locker.
○ Maintain a logbook of evidence movement.
3. Monitor & Maintain Storage Conditions
○ Keep the device in a climate-controlled, secure storage area.
○ Limit access to authorized personnel only.
Stage 3: Forensic Examination
********** 5 **********
--- page 6 ---
Objective: Extract and analyze data without altering evidence integrity.
Steps:
1. Use Write-Protection Methods
○ Prevent modifications using write-blockers and forensic tools.
○ Create a bit-by-bit forensic image of the device (using Cellebrite, Magnet AXIOM, or Autopsy).
2. Document the Analysis Process
○ Record software tools used, extraction methods, timestamps, and examiner details.
○ Maintain an audit trail of all actions.
3. Store the Original Device Securely
○ Always work on forensic copies, not the original device.
Stage 4: Reporting & Legal Submission
Objective: Present findings in court while maintaining evidence integrity.
Steps:
1. Prepare a Forensic Analysis Report
○ Include device details, extraction methods, recovered data, timestamps, and findings.
○ Clearly state whether any modifications were made.
2. Ensure Proper Handling in Court
○ Present original device and forensic images securely.
○ Maintain chain of custody documentation in case of legal challenges.
3. Testify in Court
○ The forensic examiner may explain methods, findings, and evidence integrity under oath.
Key Documentation in the Chain of Custody
Essential Records:
1. Chain of Custody Form – Tracks each transfer of evidence.
2. Evidence Collection Form – Details how and where the device was seized.
3. Forensic Imaging Report – Documents extraction methods and findings.
4. Examination Log – Keeps track of all forensic activities performed on the device.
********** 6 **********
--- page 7 ---
5. Court Submission Log – Records when and how evidence is presented in legal proceedings.
Q4   Explain the key phases of the NIST Mobile Forensics Framework and their
CO-3; SO-   a.   role in ensuring data integrity and admissibility. What challenges do forensic   [10]
3;   experts face in applying this framework?
BL-4
NIST digital forensics phases
•Collection: Identify and gather relevant data from all possible sources.
•Examination: Examine the collected data to get the information needed.
•Analysis: Analyze the data.
•Reporting: Report the findings.
Despite its structured approach, forensic experts face multiple challenges when applying the NIST Mobile
Forensics Framework:
1️⃣ Device Encryption & Security Mechanisms
🔹 Challenge:
● iOS & Android encryption make full data extraction difficult.
● File-Based Encryption (FBE) and Secure Enclave in iOS restrict forensic access.
🔹 Solution:
✅ Use tools like GrayKey (iOS) or Cellebrite for bypassing encryption (if legally permitted).
✅ Acquire data from cloud backups when physical extraction is blocked.
2️⃣ Constant OS & App Updates
🔹 Challenge:
● Frequent updates change security protocols, blocking forensic tools.
● New Android/iOS versions restrict file access (e.g., Scoped Storage).
🔹 Solution:
✅ Keep forensic tools updated to match new OS versions.
✅ Research and test alternative extraction techniques.
3️⃣ Remote Data Wiping & Self-Destructing Apps
🔹 Challenge:
● Find My iPhone (Apple) & Factory Reset Protection (Android) allow remote wipes.
● Apps like Telegram, Signal, and Snapchat use self-destructing messages.
🔹 Solution:
✅ Isolate the device immediately (Faraday bags, airplane mode).
✅ Use RAM acquisition tools before the data disappears.
4️⃣ Cloud-Based Storage & Remote Access
********** 7 **********
--- page 8 ---
🔹 Challenge:
● Many apps store data in the cloud (iCloud, Google Drive, OneDrive) instead of local storage.
● Cloud data is encrypted and requires legal approval (warrant/subpoena) to access.
🔹 Solution:
✅ Obtain a court order to access cloud backups.
✅ Use forensic tools like Magnet AXIOM & Oxygen Forensic Cloud Extractor.
5️⃣ Chain of Custody Risks
🔹 Challenge:
●   If the chain of custody is broken, evidence may be challenged in court.
● Unsecured handling can lead to data modification or loss.
🔹 Solution:
✅ Maintain strict chain of custody documentation.
✅ Use tamper-proof bags & evidence lockers.
Q4   What are the different types of SIM Cards based on size? Explain in detail.
CO-1,2;   b.   [10]
SO-4;
BL-4
Types of SIM Cards Based on Size
SIM cards come in different sizes to accommodate various mobile devices:
(1) Full-Size SIM (1FF - First Form Factor)
📏 Size: 85.6 mm × 53.98 mm (credit card-sized)
📅 Introduced: 1991
🔹 Usage: Early mobile phones, now obsolete.
This was the first generation of SIM cards, commonly used in the 1990s. It was large, resembling a credit
card, and had to be inserted into bulky mobile phones.
📌 (2) Mini SIM (2FF - Second Form Factor)
📏 Size: 25 mm × 15 mm
📅 Introduced: Late 1990s
🔹 Usage: Feature phones, early smartphones (e.g., Nokia, Blackberry).
The Mini SIM replaced the Full-Size SIM and was widely used in mobile devices until smartphones started
demanding smaller form factors.
📌 (3) Micro SIM (3FF - Third Form Factor)
********** 8 **********
--- page 9 ---
📏 Size: 15 mm × 12 mm
📅 Introduced: 2003
🔹 Usage: Smartphones (e.g., iPhone 4, Samsung Galaxy S3).
Due to space constraints in modern smartphones, the Micro SIM became popular, allowing manufacturers to
shrink device sizes while keeping SIM functionality intact.
📌 (4) Nano SIM (4FF - Fourth Form Factor)
📏 Size: 12.3 mm × 8.8 mm
📅 Introduced: 2012
🔹 Usage: Most modern smartphones (e.g., iPhone 5 & later, Samsung Galaxy S6 & later).
The Nano SIM is the smallest physical SIM and removes excess plastic from the Micro SIM while keeping
the same functionality. It allows manufacturers to free up internal space for batteries and additional
components.
📌 (5) eSIM (Embedded SIM)
📏 Size: 6 mm × 5 mm (chip soldered onto the device)
📅 Introduced: 2016
🔹 Usage: High-end smartphones, smartwatches, IoT devices (e.g., iPhone 14, Google Pixel, Samsung Galaxy
S23).
🔹 Key Features:
✅ No physical card – SIM profile is stored digitally.
✅ Supports multiple carriers – Users can switch networks remotely.
✅ Used in IoT devices – Found in smartwatches, tablets, and embedded devices.
The eSIM is the future of mobile connectivity, as it eliminates the need for physical SIM swapping and
enables remote activation.
Q5   How can Bluetooth vulnerabilities be exploited to gain unauthorized access to
CO-1,2;   a.   a device?   [10]
SO-4;
BL-2
********** 9 **********
--- page 10 ---
Q5   A forensic team is assigned to investigate data leaks in a corporate
CO-3; SO-   b.   organization where employees may have shared confidential information via   [10]
1;   mobile devices. What steps should the forensic team follow based on the NIST
BL-4   Mobile Forensics Framework to collect, analyze, and report findings?
When a forensic team investigates a corporate data leak involving mobile devices, it must follow a structured
approach to ensure evidence integrity, compliance with legal requirements, and admissibility in court. The
investigation typically follows the NIST Mobile Forensics Framework, which consists of the following key
phases:
📌 1. Preparation Phase (Pre-Investigation)
🔹 Objective: Establish the scope, legal authorization, and tools required for the investigation.
🔹 Steps:
✅ Obtain legal authorization – Secure warrants, employee consent, or corporate compliance approval.
✅ Identify suspected devices – Determine which mobile devices (company-issued or personal) may be
involved.
✅ Gather forensic tools – Ensure tools like Cellebrite UFED, Magnet AXIOM, Oxygen Forensics are available.
✅ Set up chain of custody documentation – Log every action taken on the evidence.
🔹 Challenges:
🔸 Employees may delete data or use encrypted apps (Signal, Telegram).
🔸 Corporate policies on BYOD (Bring Your Own Device) may limit access to personal devices.
📌 2. Evidence Collection & Preservation Phase
🔹 Objective: Secure mobile devices to prevent tampering, remote wipes, or data loss.
🔹 Steps:
✅ Seize and Isolate Devices – Use Faraday bags to block remote access.
********** 10 **********

[Text in pictures on this page, read by OCR]
Attack Name Method Used Impact Affected Devices

BlueBorne Remote code execution via Device takeover, malware Android, iOS, Windows,
Bluetooth vulnerability injection Linux
BIAS Attack Impersonation of trusted devices Unauthorized access Bluetooth 4.2 & older
Bluesnarfing Unauthorized data retrieval Data theft (contacts, SMS, Older mobile phones
files)
Bluebugging Remote control of mobile device Calls, texts, internet access Bluetooth 1.x, 2.x phones
hijacked
MITM Attack _Intercepting Bluetooth Eavesdropping, data theft Weakly encrypted
communication Bluetooth connections
BLE Fake BLE devices trick phones Phishing, tracking loT, BLE-enabled devices
Spoofing
DoS Attack Signal jamming Bluetooth device All Bluetooth-enabled

disruption devices
--- page 11 ---
✅ Identify Communication Channels – Check for emails, messaging apps, cloud storage, USB transfers.
✅ Clone Device Memory (Forensic Imaging) – Create a bit-by-bit copy to maintain original data integrity.
✅ Extract Network Logs & Cloud Data – Investigate company VPN, Wi-Fi, and cloud sync history.
✅ Check External Storage – Analyze USB drives, SD cards, or connected PCs.
🔹 Challenges:
🔸 Employees may use encrypted cloud storage (Google Drive, Dropbox).
🔸 Devices may have self-destructing messages (WhatsApp, Snapchat, Signal).
📌 3. Data Extraction & Analysis Phase
🔹 Objective: Retrieve and examine digital artifacts to determine if confidential data was leaked.
🔹 Key Data Sources & Tools:
Artifact Type   Data Extracted   Tools Used
📁 File System   Documents, PDFs, Media files   Cellebrite, Magnet AXIOM
📨 Emails & Messages   SMS, WhatsApp, Telegram, Signal, Slack   Oxygen Forensics, XRY
📊 Call Logs   Incoming & outgoing call details   UFED, Paraben E3
🌍 Browser History   Websites visited, downloaded files   FTK Imager, Axiom
Cloud Sync Data   iCloud, Google Drive access logs   Elcomsoft Cloud Explorer
Deleted Data   Recovered deleted messages/files   Autopsy, EnCase
🔹 Steps:
✅ Analyze metadata – Identify timestamps, sender/receiver details, and file transfers.
✅ Extract communication logs – Investigate WhatsApp, Telegram, Signal, Slack, SMS, and emails.
✅ Recover deleted files – Use forensic carving techniques to retrieve erased data.
✅ Check for unauthorized access – Review VPN logs, corporate network access, and Wi-Fi logs.
✅ Detect data exfiltration – Identify if sensitive files were transferred via email, USB, Bluetooth, or cloud.
🔹 Challenges:
🔸 Encrypted messages may prevent full content recovery.
🔸 Employees may use anonymous sharing platforms (WeTransfer, ProtonMail, Tor).
📌 4. Reporting & Legal Documentation Phase
********** 11 **********
--- page 12 ---
🔹 Objective: Compile findings into an official forensic report that can be used in court or corporate
disciplinary actions.
🔹 Steps:
✅ Summarize evidence collected – Devices, timestamps, communication logs, file transfers.
✅ Document forensic methods – Tools used, steps followed, and hash values for data integrity.
✅ Include chain of custody – Ensure every device interaction is logged.
✅ Provide expert analysis – Explain whether company policies were violated and how data was leaked.
✅ Prepare for legal or corporate action – Assist legal teams with digital evidence presentation.
🔹 Challenges:
🔸 Employees may claim involuntary data sharing or device compromise.
🔸 Legal teams must validate forensic methods to ensure court admissibility.
📌 5. Post-Investigation & Security Recommendations
🔹 Objective: Strengthen company security policies to prevent future data leaks.
🔹 Recommendations:
✅ Enforce strict access controls – Limit data access based on job roles.
✅ Implement Data Loss Prevention (DLP) tools – Block unauthorized file transfers.
✅ Monitor and log file activity – Use SIEM (Security Information & Event Management) solutions.
✅ Encrypt sensitive files – Prevent unauthorized sharing or theft.
✅ Train employees on cybersecurity – Raise awareness about insider threats.
Q6   A rooted Android device has been found in a cybercrime investigation. What
CO-2,3;   a.   forensic methods can be used to extract and analyze data from this device?   [10]
SO-1;
BL-1,4
When a rooted Android device is found in a cybercrime investigation, forensic analysts must use specialized
methods to extract, preserve, and analyze data while maintaining its integrity. Rooted devices present both
challenges and opportunities—they may provide deeper access to system files but also pose risks due to
altered security settings.
📌 1. Initial Preparation & Device Isolation
🔹 Objective: Prevent remote access, data tampering, or wiping.
🔹 Steps:
✅ Seize the device properly – Use Faraday bags to block network signals.
✅ Preserve device state – Avoid rebooting as it may trigger encryption or self-destruct mechanisms.
✅ Document device details – Capture model, OS version, installed apps, root method used (Magisk,
SuperSU).
✅ Photograph the screen – Note any active apps, running processes, or notifications.
🔹 Challenges:
🔸 Rooted devices may have modified bootloaders, which can wipe data on restart.
********** 12 **********
--- page 13 ---
🔸 Remote wipe commands (via Google, MDM, or malware) could erase evidence if the device is connected to
a network.
📌 2. Data Extraction Methods
Since the device is rooted, forensic analysts can leverage both standard and advanced techniques to extract
data.
(A) Logical Extraction (Non-Invasive)
🔹 Uses: Extracts contacts, call logs, messages, installed apps, and media files without altering the system.
🔹 Tools:
✅ ADB (Android Debug Bridge) – Extracts app data, logs, and system files.
✅ Magnet AXIOM, Cellebrite UFED – Recovers user data from file system and application databases.
✅ Oxygen Forensics, MOBILedit – Extracts cloud data and synced accounts.
✅ ADB Backup – Captures /data partition if not encrypted.
Command Example (ADB):
bash
CopyEdit
adb backup -apk -shared -all -f backup.ab
Limitations:
🔸 Cannot access deleted files or low-level system data.
🔸 Some app data may be encrypted, even on a rooted device.
(B) File System Extraction (Rooted Devices Only)
🔹 Uses: Extracts entire /data partition, including private app files.
🔹 Tools:
✅ TWRP Custom Recovery – Creates full NANDroid backup.
✅ Magisk Modules – Can be used to extract deep system data.
✅ Cellebrite UFED, XRY, Autopsy – Parses SQLite databases, chat logs, browser history.
✅ Android Terminal Emulator (su commands) – Manually access /system and /data partitions.
Example (Dumping file system via ADB on a rooted device):
bash
CopyEdit
adb shell su -c "tar -cf /sdcard/data.tar /data"
adb pull /sdcard/data.tar
🔹 Advantages:
✔️ Access to deleted messages, app caches, and logs.
✔️ Can analyze system logs for malware traces.
********** 13 **********
--- page 14 ---
🔹 Challenges:
🔸 If SELinux is enforced, access may be limited.
🔸 Corrupt or incomplete data may result from modified partitions.
(C) Physical Extraction (Bit-by-Bit Copy)
🔹 Uses: Captures full NAND memory, including deleted files and hidden partitions.
🔹 Tools:
✅ dd (Linux command) – Dumps raw disk image.
✅ Autopsy, FTK Imager – Parses memory dumps for forensic analysis.
✅ Cellebrite UFED 4PC, Belkasoft Evidence Center – Extracts file systems and databases.
Example (Using dd to extract full image from /dev/block/mmcblk0):
bash
CopyEdit
adb shell su -c "dd if=/dev/block/mmcblk0 of=/sdcard/android_dump.img bs=4096"
adb pull /sdcard/android_dump.img
🔹 Advantages:
✔️ Extracts deleted files, hidden malware, and unallocated space.
✔️ Allows timeline reconstruction for forensic investigation.
🔹 Challenges:
🔸 Large data size – Requires significant storage for analysis.
🔸 Encrypted partitions may still prevent full data recovery.
📌 3. Data Analysis & Evidence Recovery
(A) Extracting App Data & Communication Logs
🔹 What to Look For?
✅ Chat apps: WhatsApp, Telegram, Signal, Snapchat.
✅ Emails & SMS: Gmail, Outlook, default messaging apps.
✅ Social Media: Facebook, Instagram, Twitter logs.
✅ Call logs & VoIP: Google Voice, Skype, Zoom records.
🔹 Forensic Tools Used:
✅ SQLite Forensics – Recovers messages, contacts, and metadata.
✅ Autopsy, Belkasoft X – Parses extracted databases for chats.
✅ AXIOM, UFED – Analyzes social media artifacts.
🔹 Example: Recovering WhatsApp Messages (Manually from SQLite DB):
bash
CopyEdit
adb pull /data/data/com.whatsapp/databases/msgstore.db
sqlite3 msgstore.db "SELECT key_remote_jid, data, timestamp FROM messages"
(B) Identifying Malware, Keyloggers, & Hidden Apps
********** 14 **********
--- page 15 ---
🔹 What to Look For?
✅ Root exploits (SU binaries, Magisk logs).
✅ Malicious APKs (Spyware, keyloggers, RATs).
✅ Modified system files (hosts file, DNS changes).
🔹 Forensic Methods:
✅ Check installed apps – adb shell pm list packages -3
✅ Scan for malware – VirusTotal, Kaspersky, or ClamAV
✅ Inspect log files – /var/log/system.log, /data/system/dropbox/
✅ Analyze running processes – adb shell ps -A
🔹 Example: Searching for Malware Apps in the Device’s File System
bash
CopyEdit
adb shell su -c "ls -la /system/app/"
adb shell su -c "grep -i suspicious /data/system/packages.list"
(C) Network Traffic & Cloud Analysis
🔹 What to Look For?
✅ Unauthorized data transfers – Cloud backups, remote control apps.
✅ VPN logs – HideMyAss, NordVPN, ProtonVPN usage.
✅ Wi-Fi connections – Identifies past locations and access points.
🔹 Forensic Methods:
✅ Wireshark/TCPDump – Capture network packets.
✅ Cloud data extraction – Elcomsoft, Oxygen Forensics.
✅ Router logs analysis – Check device activity on the network.
📌 4. Reporting & Legal Documentation
🔹 Forensic Report Must Include:
✅ Device details – Model, IMEI, Android version, root status.
✅ Tools & methods used – ADB, UFED, Autopsy, etc.
✅ Extracted evidence – Messages, emails, deleted files.
✅ Metadata & timestamps – Logs of activities and communications.
✅ Legal chain of custody – Ensures evidence integrity.
Q6
CO-2; SO-   b.   What security features are bypassed when an iOS device is jailbroken?   [10]
1;
BL-2
● Higher risk of malware infections – Jailbroken devices are frequently targeted by spyware, adware,
and trojans.
● No security updates – Apple won’t provide updates, leaving the device vulnerable.
●   Financial loss & identity theft – Banking and payment apps may be compromised.
● Legal & warranty issues –Jailbreaking voids the Apple warranty and may violate terms of service.
Q7
CO-3; SO-   a.   What are the steps of collecting mobile devices from the crime scene?   [05]
1;
********** 15 **********
--- page 16 ---
BL-2
When collecting mobile devices from a crime scene, the following steps should be followed:
1.Initial Assessment: Identifying all mobile devices at the scene that may be relevant to the investigation.
2.Avoiding Alteration: If the device is on, it should not be altered unless necessary to preserve data. This may
involve immediately disconnecting it from networks (e.g., turning off Wi-Fi or mobile data). If the device is off,
it should remain off unless analysis requires otherwise.
3.Seizing Devices: Handle devices carefully to avoid physical damage. Proper documentation should be
maintained, including the device’s state (powered on/off, passcode locked/unlocked).
4.Labeling and Documentation: Every device should be labeled with unique identifiers and photographed to
ensure a clear chain of custody.
5.Transporting Devices: Devices should be transported in tamper-proof bags to prevent any tampering or
alteration.
Q7
CO-2; SO-   b.   What is the primary purpose of the SIM card's file system? What type of data   [05]
1;   is primarily stored in SIM card's file system?
BL-2
The primary purpose of the SIM card's file system is to securely store subscriber identity, authentication
credentials, and network-related data required for mobile communication. It enables users to access mobile
networks, authenticate themselves, and store limited personal information.
Types of Data Stored in the SIM Card's File System
The SIM card's file system follows a hierarchical structure, organized into three main levels:
1. Master File (MF) – Root directory of the SIM file system.
2. Dedicated Files (DF) – Subdirectories containing related files.
3. Elementary Files (EF) – Actual data storage locations.
1. Subscriber Identity & Authentication Data
✅ International Mobile Subscriber Identity (IMSI) – Unique ID linking the SIM to a mobile network.
✅ Authentication Key (Ki) – Secret key used for network authentication (not directly accessible).
✅ Operator-Specific Data – Security parameters for network access.
2. Network Configuration & Carrier Data
✅ Preferred Public Land Mobile Network (PLMN) – List of preferred mobile networks.
✅ Network Parameters (LOCI, TMSI, LAI) – Stores location information for mobile towers.
✅ Access Control Data – Defines roaming restrictions and permitted networks.
3. Contact & Messaging Data
✅ Phonebook Contacts (EF_ADN) – Stores names and numbers (limited to ~250 entries).
✅ SMS Messages (EF_SMS) – Stores text messages, usually limited to 20–50 messages.
✅ Call Logs (EF_LND, EF_ICI, EF_OCI) – Recent dialed and received calls (in some SIMs).
********** 16 **********
--- page 17 ---
4. Encryption & Security Keys
✅ PIN & PUK Codes (EF_PIN, EF_PUK) – Personal Identification Number (PIN) and unlock code.
✅ Authentication Algorithms (MILENAGE, COMP128) – Used for network security.
5. Application & Custom Data (Newer SIMs)
✅ eSIM Profiles – Stores multiple carrier profiles in embedded SIMs.
✅ Mobile Payment Data – Some SIMs support NFC-based payments.
✅ Service Provider-Specific Data – Operator settings, SIM toolkit (STK) applications.
Q7
CO-1,2;   c.   Differentiate between Android and iOS Security Model   [05]
SO-2;
BL-4
Q7
CO-1,2;   d.   As a part of the forensic investigation process for popular mobile applications   [05]
SO-1;   like WhatsApp on Android and iOS. What artifacts can be collected?
BL-4
Artifacts Collected:
● Chat Logs (msgstore.db, wa.db) – Found in /data/data/com.whatsapp/databases/ (Android) and
ChatStorage.sqlite (iOS).
● Deleted Messages – Recoverable from msgstore.db.cryptXX backups.
● Media Files – Stored in /WhatsApp/Media/ (Android) or App Sandbox (iOS).
● Cloud Backups – Google Drive (Android) & iCloud (iOS).
● Encryption Keys – Found in /data/data/com.whatsapp/files/key (Android, requires root).
********** 17 **********

[Text in pictures on this page, read by OCR]
Feature Android Security iOS Security

App Sandboxing Linux-based, per-app UID Stricter sandboxing, XPC for inter-app

communication

File Access Scoped storage, per-app private Full file isolation, access via APIs only
data

Permissions Runtime & manifest-based Explicit approval, enforced at all levels

Malware Google Play Protect, SafetyNet App Store screening, notarization

Protection

Secure Boot Verified Boot with rollback Secure Enclave for cryptographic security
protection

Encryption File-Based Encryption (FBE) Hardware-backed File Encryption
````
