# Cyber Forensics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 49f5459943e7

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/Cyber Forensics/ANS_Cyber Forensics(702IT0E024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / V/Semester VI/Semester VIII/Semester X(Exam Year: 2025-2026)
Subject: Cyber Forensics
Date: 12 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q CO;BL   Question   Marks   Detailed Answer (Paragraph)   Rubrics of
No   Evaluation
Q1 CO1;   Explain the   5   Chain of custody ensures that   1 mark: Definition;
A BL2   importance of   digital evidence is properly   2 marks:
chain of custody   collected, documented, and   Importance; 2
with a real-world   preserved from the time of   marks: Real-world
cybercrime   acquisition to presentation in   example
example.   court. It maintains integrity and
prevents tampering. For example,
in a cyber fraud case, if a seized
laptop is not properly logged (who
handled it, when, and why), the
defense may challenge its
authenticity, leading to rejection
in court. Proper documentation,
sealing, labeling, and logging are
essential to maintain credibility.
Q1 CO2;   Analyze how   5   Metadata contains hidden   1 mark: Definition;
B   BL4   metadata in   information such as author name,   2 marks:
documents can be   creation/modification date, device   Types/uses; 2
used as digital   details, and file path. Investigators marks:
evidence.   use metadata to establish   Analysis/example
timelines, identify authorship, and
detect tampering. For instance, a
document claiming to be original
may show metadata indicating it
was edited later, revealing fraud.
Metadata analysis tools help
extract and correlate such
********** 1 **********
--- page 2 ---
information for evidence
validation.
Q1 CO2;   Apply forensic   5   Even after formatting, data   2 marks: Process; 2
C   BL3   techniques to   remains recoverable using   marks:
extract evidence   forensic techniques. Investigators   Tools/techniques; 1
from a formatted   use disk imaging tools (e.g., FTK   mark: Preservation
USB drive.   Imager), data carving methods,   method
and file signature analysis to
recover deleted files. A write
blocker is used to prevent
modification. The process
includes creating a bit-by-bit
image, scanning for residual data,
and reconstructing files based on
headers/footers.
Q1 CO3;   Evaluate the   5   Investigators often access private   2 marks: Issues; 2
D BL5   ethical challenges   data such as emails, photos, and   marks: Evaluation;
in handling   financial records. Ethical   1 mark: Ethical
sensitive personal   challenges include maintaining   practices
data during   confidentiality, avoiding misuse,
investigations.   and ensuring minimal invasion of
privacy. Unauthorized disclosure
or bias may compromise
investigation integrity. Adhering
to legal guidelines, obtaining
proper authorization, and
maintaining professionalism are
critical.
Q2 CO1;   Reconstruct   10   When logs are deleted,   3 marks: Sources; 4
A BL4   attack timeline   investigators reconstruct timelines marks: Process; 3
after logs   using alternative sources such as   marks:
deletion.   system artifacts, registry entries,   Tools/examples
shadow copies, network logs, and
timestamps. File metadata,
browser history, and intrusion
detection system logs help
correlate events. Timeline analysis
tools (e.g., Autopsy) are used to
sequence activities and identify
attack patterns.
Q2 CO1;   Role of hashing   10   Hashing algorithms like MD5 and   3 marks: Concept; 4
B   BL3   algorithms in data   SHA generate unique hash values   marks: Application;
integrity.   for files. Even a minor change   3 marks: Example
alters the hash, ensuring integrity.
During forensic acquisition,
original and copied data hashes
are compared to verify
authenticity. Hashing also helps
detect tampering and ensures
admissibility in court.
Q3 CO1;   Recover deleted   10   NTFS stores file records in MFT.   3 marks: NTFS
A BL4   files in NTFS.   Deleted files are marked but not   concept; 4 marks:
erased immediately. Recovery
********** 2 **********
--- page 3 ---
involves analyzing MFT entries,   Recovery methods;
using data carving, and restoring   3 marks: Case
file fragments. Tools like EnCase
help reconstruct deleted data. Case
example: recovering deleted
emails from disk sectors.
Q3 CO1;   BIOS & UEFI   10   BIOS and UEFI initialize   3 marks:
B   BL2   forensic   hardware during boot. UEFI   Explanation; 4
relevance.   provides advanced features like   marks: Differences;
secure boot. Forensically, boot   3 marks: Relevance
logs help identify system
modifications, malware
persistence, and unauthorized
firmware changes.
Q4 CO1;   Steganography   10   Steganography hides data within   3 marks: Concept; 4
A BL4   and detection.   files (images, audio). Detection   marks: Techniques;
involves statistical analysis, file   3 marks: Detection
size comparison, and stego tools.
Investigators identify anomalies in
pixel values or file structures to
uncover hidden data.
Q4 CO2;   Analyze   10   Encrypted containers (e.g.,   3 marks:
B   BL3   encrypted   VeraCrypt) store hidden data.   Identification; 4
containers.   Investigators identify suspicious   marks: Analysis; 3
partitions, analyze entropy levels,   marks: Tools
and use brute-force or key
recovery methods. Memory
analysis may reveal encryption
keys during live acquisition.
Q5 CO2;   Cloud vs   10   Cloud forensics deals with   3 marks:
A BL3   traditional   distributed data, multi-tenancy,   Explanation; 4
forensics.   and lack of physical access.   marks: Differences;
Challenges include jurisdiction,   3 marks: Challenges
data volatility, and provider
dependency. Unlike traditional
forensics, investigators rely on
logs and APIs instead of physical
devices.
Q5 CO2;   DNS logs in   10   DNS logs track domain requests.   3 marks: Concept; 4
B   BL4   investigation.   Malicious domains, phishing   marks: Analysis; 3
attempts, and botnet activity can   marks: Application
be identified through abnormal
queries. Correlation with IP logs
helps trace attacker behavior.
Q6 CO2;   Volatile vs non-   10   Volatile memory (RAM) loses   3 marks:
A BL2   volatile memory.   data when power is off, while   Definitions; 4
non-volatile memory (HDD/SSD)   marks: Differences;
retains data. RAM contains active   3 marks:
processes, encryption keys, and   Importance
network sessions, making it
crucial in live forensics.
********** 3 **********
--- page 4 ---
Q6 CO2;   RAM evidence   10   Capturing RAM is challenging   3 marks:
B   BL3   challenges &   due to volatility, risk of data   Challenges; 4
strategy.   alteration, and tool limitations.   marks: Strategy; 3
Strategy includes using trusted   marks: Application
tools, minimizing system
interaction, and prioritizing
memory acquisition before
shutdown. Analysis reveals
running processes and hidden
malware.
Q7 CO3;   Role of cyber   10   Cyber laws like IT Act 2000   3 marks: Law
A BL2   laws in India.   govern digital evidence handling.   concept; 4 marks:
They ensure legality,   Provisions; 3
admissibility, and protection   marks: Importance
against cybercrime. Sections
define offenses and penalties,
supporting forensic investigations.
Q7 CO3;   Phishing attack   10   Investigation includes analyzing   3 marks: Steps; 4
B   BL5   investigation.   email headers, tracing IP   marks: Analysis; 3
addresses, examining DNS logs,   marks: Prevention
and identifying phishing domains.
User credentials misuse is tracked
through transaction logs.
Preventive measures include
awareness and multi-factor
authentication.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper f60118a850cc

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_IT_7041/Cyber Forensics/ANS_Cyber Forensics(702IT0E024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / V/Semester VI/Semester VIII/Semester X(Exam Year: 2025-2026)
Subject: Cyber Forensics
Date: 12 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q CO;BL   Question   Marks   Detailed Answer (Paragraph)   Rubrics of
No   Evaluation
Q1 CO1;   Explain the   5   Chain of custody ensures that   1 mark: Definition;
A BL2   importance of   digital evidence is properly   2 marks:
chain of custody   collected, documented, and   Importance; 2
with a real-world   preserved from the time of   marks: Real-world
cybercrime   acquisition to presentation in   example
example.   court. It maintains integrity and
prevents tampering. For example,
in a cyber fraud case, if a seized
laptop is not properly logged (who
handled it, when, and why), the
defense may challenge its
authenticity, leading to rejection
in court. Proper documentation,
sealing, labeling, and logging are
essential to maintain credibility.
Q1 CO2;   Analyze how   5   Metadata contains hidden   1 mark: Definition;
B   BL4   metadata in   information such as author name,   2 marks:
documents can be   creation/modification date, device   Types/uses; 2
used as digital   details, and file path. Investigators marks:
evidence.   use metadata to establish   Analysis/example
timelines, identify authorship, and
detect tampering. For instance, a
document claiming to be original
may show metadata indicating it
was edited later, revealing fraud.
Metadata analysis tools help
extract and correlate such
********** 1 **********
--- page 2 ---
information for evidence
validation.
Q1 CO2;   Apply forensic   5   Even after formatting, data   2 marks: Process; 2
C   BL3   techniques to   remains recoverable using   marks:
extract evidence   forensic techniques. Investigators   Tools/techniques; 1
from a formatted   use disk imaging tools (e.g., FTK   mark: Preservation
USB drive.   Imager), data carving methods,   method
and file signature analysis to
recover deleted files. A write
blocker is used to prevent
modification. The process
includes creating a bit-by-bit
image, scanning for residual data,
and reconstructing files based on
headers/footers.
Q1 CO3;   Evaluate the   5   Investigators often access private   2 marks: Issues; 2
D BL5   ethical challenges   data such as emails, photos, and   marks: Evaluation;
in handling   financial records. Ethical   1 mark: Ethical
sensitive personal   challenges include maintaining   practices
data during   confidentiality, avoiding misuse,
investigations.   and ensuring minimal invasion of
privacy. Unauthorized disclosure
or bias may compromise
investigation integrity. Adhering
to legal guidelines, obtaining
proper authorization, and
maintaining professionalism are
critical.
Q2 CO1;   Reconstruct   10   When logs are deleted,   3 marks: Sources; 4
A BL4   attack timeline   investigators reconstruct timelines marks: Process; 3
after logs   using alternative sources such as   marks:
deletion.   system artifacts, registry entries,   Tools/examples
shadow copies, network logs, and
timestamps. File metadata,
browser history, and intrusion
detection system logs help
correlate events. Timeline analysis
tools (e.g., Autopsy) are used to
sequence activities and identify
attack patterns.
Q2 CO1;   Role of hashing   10   Hashing algorithms like MD5 and   3 marks: Concept; 4
B   BL3   algorithms in data   SHA generate unique hash values   marks: Application;
integrity.   for files. Even a minor change   3 marks: Example
alters the hash, ensuring integrity.
During forensic acquisition,
original and copied data hashes
are compared to verify
authenticity. Hashing also helps
detect tampering and ensures
admissibility in court.
Q3 CO1;   Recover deleted   10   NTFS stores file records in MFT.   3 marks: NTFS
A BL4   files in NTFS.   Deleted files are marked but not   concept; 4 marks:
erased immediately. Recovery
********** 2 **********
--- page 3 ---
involves analyzing MFT entries,   Recovery methods;
using data carving, and restoring   3 marks: Case
file fragments. Tools like EnCase
help reconstruct deleted data. Case
example: recovering deleted
emails from disk sectors.
Q3 CO1;   BIOS & UEFI   10   BIOS and UEFI initialize   3 marks:
B   BL2   forensic   hardware during boot. UEFI   Explanation; 4
relevance.   provides advanced features like   marks: Differences;
secure boot. Forensically, boot   3 marks: Relevance
logs help identify system
modifications, malware
persistence, and unauthorized
firmware changes.
Q4 CO1;   Steganography   10   Steganography hides data within   3 marks: Concept; 4
A BL4   and detection.   files (images, audio). Detection   marks: Techniques;
involves statistical analysis, file   3 marks: Detection
size comparison, and stego tools.
Investigators identify anomalies in
pixel values or file structures to
uncover hidden data.
Q4 CO2;   Analyze   10   Encrypted containers (e.g.,   3 marks:
B   BL3   encrypted   VeraCrypt) store hidden data.   Identification; 4
containers.   Investigators identify suspicious   marks: Analysis; 3
partitions, analyze entropy levels,   marks: Tools
and use brute-force or key
recovery methods. Memory
analysis may reveal encryption
keys during live acquisition.
Q5 CO2;   Cloud vs   10   Cloud forensics deals with   3 marks:
A BL3   traditional   distributed data, multi-tenancy,   Explanation; 4
forensics.   and lack of physical access.   marks: Differences;
Challenges include jurisdiction,   3 marks: Challenges
data volatility, and provider
dependency. Unlike traditional
forensics, investigators rely on
logs and APIs instead of physical
devices.
Q5 CO2;   DNS logs in   10   DNS logs track domain requests.   3 marks: Concept; 4
B   BL4   investigation.   Malicious domains, phishing   marks: Analysis; 3
attempts, and botnet activity can   marks: Application
be identified through abnormal
queries. Correlation with IP logs
helps trace attacker behavior.
Q6 CO2;   Volatile vs non-   10   Volatile memory (RAM) loses   3 marks:
A BL2   volatile memory.   data when power is off, while   Definitions; 4
non-volatile memory (HDD/SSD)   marks: Differences;
retains data. RAM contains active   3 marks:
processes, encryption keys, and   Importance
network sessions, making it
crucial in live forensics.
********** 3 **********
--- page 4 ---
Q6 CO2;   RAM evidence   10   Capturing RAM is challenging   3 marks:
B   BL3   challenges &   due to volatility, risk of data   Challenges; 4
strategy.   alteration, and tool limitations.   marks: Strategy; 3
Strategy includes using trusted   marks: Application
tools, minimizing system
interaction, and prioritizing
memory acquisition before
shutdown. Analysis reveals
running processes and hidden
malware.
Q7 CO3;   Role of cyber   10   Cyber laws like IT Act 2000   3 marks: Law
A BL2   laws in India.   govern digital evidence handling.   concept; 4 marks:
They ensure legality,   Provisions; 3
admissibility, and protection   marks: Importance
against cybercrime. Sections
define offenses and penalties,
supporting forensic investigations.
Q7 CO3;   Phishing attack   10   Investigation includes analyzing   3 marks: Steps; 4
B   BL5   investigation.   email headers, tracing IP   marks: Analysis; 3
addresses, examining DNS logs,   marks: Prevention
and identifying phishing domains.
User credentials misuse is tracked
through transaction logs.
Preventive measures include
awareness and multi-factor
authentication.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper b2a7295abe60

- Departments: AI and Data Science, Computer Engineering
- Programmes: BTech AIDS 7056, Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AIDS_7056/Cyber Forensics/ANS_Cyber Forensics(702IT0E024)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 Nov 2025
- Text: text (3 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech Intg. (CE)
Year: IV / VI/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Cyber Forensics
Date: 27 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory and covers all units.
5. Attempt any four questions from Q2 to Q7.
6. All questions carry equal marks (20 each).
7. Begin each answer on a fresh page.
8. Assume suitable data if necessary.
9. Use of calculator/graph paper is permitted wherever applicable.
Q1
a. Cyber Forensics – Definition, Role & Importance (5 Marks)
Cyber Forensics is the scientific process of identifying, collecting, analysing, and preserving digital evidence
from electronic devices for use in legal investigations.
Role & Importance:
•   Helps trace the origin of cybercrimes (e.g., hacking, data theft).
•   Ensures evidence integrity and admissibility in court.
•   Supports law enforcement in reconstructing digital events.
•   Aids in prevention and future mitigation of cyber incidents.
b. Types of Cybercrimes (5 Marks)
•   Financial crimes: Credit card fraud, phishing.
•   Hacking: Unauthorised access to systems.
•   Cyberstalking & harassment: Threats via digital platforms.
•   Identity theft: Using personal data fraudulently.
• Malware attacks: Viruses, ransomware.
Example: A phishing email stealing bank credentials.
c. Forensic Process Model (5 Marks)
Phases include:
1. Identification – Recognising potential digital evidence.
2. Preservation – Maintaining integrity using write blockers.
3. Collection/Acquisition – Imaging and documenting data.
4. Examination & Analysis – Extracting relevant information.
5. Documentation & Reporting – Presenting findings systematically.
d. Ethical, Professional & Legal Issues (5 Marks)
•   Ethical: Confidentiality, objectivity, avoiding bias.
•   Professional: Competence, integrity, accurate documentation.
•   Legal: Compliance with IT Act 2000, chain of custody, admissibility under Indian Evidence Act.
********** 1 **********
--- page 2 ---
Q2
a. FAT and NTFS File Systems (10 Marks)
• FAT (File Allocation Table): Simple structure; uses a table to track clusters; common in removable
drives.
• NTFS (New Technology File System): Uses MFT (Master File Table); supports file permissions,
journaling, compression, encryption.
Diagram: FAT—linked list structure; NTFS—MFT with metadata attributes.
b. Role in Forensics (10 Marks)
Understanding file systems helps investigators:
• Recover deleted or hidden files.
•   Interpret file timestamps.
•   Trace user activity and system logs.
•   Detect tampering and fragmentation patterns.
Q3
a. Forensic Imaging & Data Acquisition (10 Marks)
•   Process: Identify → Prepare tools → Acquire bit-by-bit image → Verify hash → Document.
•   Tools: FTK Imager, EnCase, X-Ways, Autopsy.
•   Ensures original evidence remains unaltered using hash validation (MD5/SHA1).
b. Data Carving & Recovery (10 Marks)
•   Extracts files from unallocated space using header/footer patterns.
•   Tools: PhotoRec, Scalpel.
Example: Recovering deleted JPEG images using signature “FFD8–FFD9”.
Q4
a. Network Traffic Analysis (10 Marks)
•   Involves capturing and inspecting packets using tools (Wireshark, tcpdump).
•   Analyses headers, protocols, IPs, and ports.
•   Detects suspicious activities like DoS, malware communication, or data exfiltration.
b. Malware Analysis & Hidden Data Detection (10 Marks)
•   Static Analysis: Reviewing code without execution.
• Dynamic Analysis: Executing in sandbox to observe behaviour.
• Hidden Data: Detect via steganalysis, hex editors, or memory dumps.
•   Tools: IDA Pro, OllyDbg, Volatility, Autopsy.
Q5
a. Mobile Device & SIM Data Acquisition (10 Marks)
•   Steps: Isolation (Faraday bag) → Logical/Physical acquisition → Hashing → Verification.
•   Tools: Cellebrite UFED, Oxygen Forensic Suite, MOBILedit.
• Data Types: Contacts, SMS, call logs, app data, SIM IMSI/ICCID.
b. Challenges in Mobile Forensics (10 Marks)
•   Encryption and passcodes.
•   Device diversity (Android/iOS).
•   Cloud-synced data.
•   Volatile memory loss.
• Network evidence correlation — linking call detail records (CDRs) with device logs.
Q6
a. Cyber Laws in India (10 Marks)
•   IT Act, 2000: Governs cyber offences and digital signatures.
•   Sections 65–74: Address tampering, hacking, and data theft.
•   Indian Evidence Act (Amendment 2000): Recognises digital evidence.
********** 2 **********
--- page 3 ---
• Data Privacy: Governed under IT Rules, 2011 and DPDP Act, 2023.
b. Forensic Report Writing (10 Marks)
•   Structure:
1. Case details & objective
2. Evidence collection summary
3. Tools used
4. Analysis results (screenshots, logs)
5. Findings & interpretation
6. Conclusion & recommendations
•   Should maintain neutrality, accuracy, and chain of custody reference.
Q7
a. Ransomware Investigation Case (10 Marks)
Phases:
1. Incident Response: Containment & isolation of infected systems.
2. Acquisition: Imaging affected drives.
3. Analysis: Identifying encryption keys, ransom notes, malware signatures.
4. Attribution: Tracing IPs, wallets, attacker IDs.
5. Reporting: Documenting findings for law enforcement.
b. Forensic Tools & Chain of Custody (10 Marks)
•   Tools: EnCase (imaging), FTK (analysis), Volatility (RAM), Wireshark (network), Cellebrite (mobile).
•   Integrity Measures:
o Hash verification.
o Evidence bagging and sealing.
o Documented transfer logs.
o Access control maintained throughout investigation.
********** 3 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 1cb539510647

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_Computer_7002/Cyber Forensics/ANS_Cyber Forensics(702IT0E024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 Nov 2025
- Text: text (3 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech Intg. (CE)
Year: IV / VI/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: Cyber Forensics
Date: 27 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory and covers all units.
5. Attempt any four questions from Q2 to Q7.
6. All questions carry equal marks (20 each).
7. Begin each answer on a fresh page.
8. Assume suitable data if necessary.
9. Use of calculator/graph paper is permitted wherever applicable.
Q1
a. Cyber Forensics – Definition, Role & Importance (5 Marks)
Cyber Forensics is the scientific process of identifying, collecting, analysing, and preserving digital evidence
from electronic devices for use in legal investigations.
Role & Importance:
•   Helps trace the origin of cybercrimes (e.g., hacking, data theft).
•   Ensures evidence integrity and admissibility in court.
•   Supports law enforcement in reconstructing digital events.
•   Aids in prevention and future mitigation of cyber incidents.
b. Types of Cybercrimes (5 Marks)
•   Financial crimes: Credit card fraud, phishing.
•   Hacking: Unauthorised access to systems.
•   Cyberstalking & harassment: Threats via digital platforms.
•   Identity theft: Using personal data fraudulently.
• Malware attacks: Viruses, ransomware.
Example: A phishing email stealing bank credentials.
c. Forensic Process Model (5 Marks)
Phases include:
1. Identification – Recognising potential digital evidence.
2. Preservation – Maintaining integrity using write blockers.
3. Collection/Acquisition – Imaging and documenting data.
4. Examination & Analysis – Extracting relevant information.
5. Documentation & Reporting – Presenting findings systematically.
d. Ethical, Professional & Legal Issues (5 Marks)
•   Ethical: Confidentiality, objectivity, avoiding bias.
•   Professional: Competence, integrity, accurate documentation.
•   Legal: Compliance with IT Act 2000, chain of custody, admissibility under Indian Evidence Act.
********** 1 **********
--- page 2 ---
Q2
a. FAT and NTFS File Systems (10 Marks)
• FAT (File Allocation Table): Simple structure; uses a table to track clusters; common in removable
drives.
• NTFS (New Technology File System): Uses MFT (Master File Table); supports file permissions,
journaling, compression, encryption.
Diagram: FAT—linked list structure; NTFS—MFT with metadata attributes.
b. Role in Forensics (10 Marks)
Understanding file systems helps investigators:
• Recover deleted or hidden files.
•   Interpret file timestamps.
•   Trace user activity and system logs.
•   Detect tampering and fragmentation patterns.
Q3
a. Forensic Imaging & Data Acquisition (10 Marks)
•   Process: Identify → Prepare tools → Acquire bit-by-bit image → Verify hash → Document.
•   Tools: FTK Imager, EnCase, X-Ways, Autopsy.
•   Ensures original evidence remains unaltered using hash validation (MD5/SHA1).
b. Data Carving & Recovery (10 Marks)
•   Extracts files from unallocated space using header/footer patterns.
•   Tools: PhotoRec, Scalpel.
Example: Recovering deleted JPEG images using signature “FFD8–FFD9”.
Q4
a. Network Traffic Analysis (10 Marks)
•   Involves capturing and inspecting packets using tools (Wireshark, tcpdump).
•   Analyses headers, protocols, IPs, and ports.
•   Detects suspicious activities like DoS, malware communication, or data exfiltration.
b. Malware Analysis & Hidden Data Detection (10 Marks)
•   Static Analysis: Reviewing code without execution.
• Dynamic Analysis: Executing in sandbox to observe behaviour.
• Hidden Data: Detect via steganalysis, hex editors, or memory dumps.
•   Tools: IDA Pro, OllyDbg, Volatility, Autopsy.
Q5
a. Mobile Device & SIM Data Acquisition (10 Marks)
•   Steps: Isolation (Faraday bag) → Logical/Physical acquisition → Hashing → Verification.
•   Tools: Cellebrite UFED, Oxygen Forensic Suite, MOBILedit.
• Data Types: Contacts, SMS, call logs, app data, SIM IMSI/ICCID.
b. Challenges in Mobile Forensics (10 Marks)
•   Encryption and passcodes.
•   Device diversity (Android/iOS).
•   Cloud-synced data.
•   Volatile memory loss.
• Network evidence correlation — linking call detail records (CDRs) with device logs.
Q6
a. Cyber Laws in India (10 Marks)
•   IT Act, 2000: Governs cyber offences and digital signatures.
•   Sections 65–74: Address tampering, hacking, and data theft.
•   Indian Evidence Act (Amendment 2000): Recognises digital evidence.
********** 2 **********
--- page 3 ---
• Data Privacy: Governed under IT Rules, 2011 and DPDP Act, 2023.
b. Forensic Report Writing (10 Marks)
•   Structure:
1. Case details & objective
2. Evidence collection summary
3. Tools used
4. Analysis results (screenshots, logs)
5. Findings & interpretation
6. Conclusion & recommendations
•   Should maintain neutrality, accuracy, and chain of custody reference.
Q7
a. Ransomware Investigation Case (10 Marks)
Phases:
1. Incident Response: Containment & isolation of infected systems.
2. Acquisition: Imaging affected drives.
3. Analysis: Identifying encryption keys, ransom notes, malware signatures.
4. Attribution: Tracing IPs, wallets, attacker IDs.
5. Reporting: Documenting findings for law enforcement.
b. Forensic Tools & Chain of Custody (10 Marks)
•   Tools: EnCase (imaging), FTK (analysis), Volatility (RAM), Wireshark (network), Cellebrite (mobile).
•   Integrity Measures:
o Hash verification.
o Evidence bagging and sealing.
o Documented transfer logs.
o Access control maintained throughout investigation.
********** 3 **********
````

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper 9282a5e852f4

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_Computer_7047/Cyber Forensics/ANS_Cyber Forensics(702IT0E024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / V/Semester VI/Semester VIII/Semester X(Exam Year: 2025-2026)
Subject: Cyber Forensics
Date: 12 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q CO;BL   Question   Marks   Detailed Answer (Paragraph)   Rubrics of
No   Evaluation
Q1 CO1;   Explain the   5   Chain of custody ensures that   1 mark: Definition;
A BL2   importance of   digital evidence is properly   2 marks:
chain of custody   collected, documented, and   Importance; 2
with a real-world   preserved from the time of   marks: Real-world
cybercrime   acquisition to presentation in   example
example.   court. It maintains integrity and
prevents tampering. For example,
in a cyber fraud case, if a seized
laptop is not properly logged (who
handled it, when, and why), the
defense may challenge its
authenticity, leading to rejection
in court. Proper documentation,
sealing, labeling, and logging are
essential to maintain credibility.
Q1 CO2;   Analyze how   5   Metadata contains hidden   1 mark: Definition;
B   BL4   metadata in   information such as author name,   2 marks:
documents can be   creation/modification date, device   Types/uses; 2
used as digital   details, and file path. Investigators marks:
evidence.   use metadata to establish   Analysis/example
timelines, identify authorship, and
detect tampering. For instance, a
document claiming to be original
may show metadata indicating it
was edited later, revealing fraud.
Metadata analysis tools help
extract and correlate such
********** 1 **********
--- page 2 ---
information for evidence
validation.
Q1 CO2;   Apply forensic   5   Even after formatting, data   2 marks: Process; 2
C   BL3   techniques to   remains recoverable using   marks:
extract evidence   forensic techniques. Investigators   Tools/techniques; 1
from a formatted   use disk imaging tools (e.g., FTK   mark: Preservation
USB drive.   Imager), data carving methods,   method
and file signature analysis to
recover deleted files. A write
blocker is used to prevent
modification. The process
includes creating a bit-by-bit
image, scanning for residual data,
and reconstructing files based on
headers/footers.
Q1 CO3;   Evaluate the   5   Investigators often access private   2 marks: Issues; 2
D BL5   ethical challenges   data such as emails, photos, and   marks: Evaluation;
in handling   financial records. Ethical   1 mark: Ethical
sensitive personal   challenges include maintaining   practices
data during   confidentiality, avoiding misuse,
investigations.   and ensuring minimal invasion of
privacy. Unauthorized disclosure
or bias may compromise
investigation integrity. Adhering
to legal guidelines, obtaining
proper authorization, and
maintaining professionalism are
critical.
Q2 CO1;   Reconstruct   10   When logs are deleted,   3 marks: Sources; 4
A BL4   attack timeline   investigators reconstruct timelines marks: Process; 3
after logs   using alternative sources such as   marks:
deletion.   system artifacts, registry entries,   Tools/examples
shadow copies, network logs, and
timestamps. File metadata,
browser history, and intrusion
detection system logs help
correlate events. Timeline analysis
tools (e.g., Autopsy) are used to
sequence activities and identify
attack patterns.
Q2 CO1;   Role of hashing   10   Hashing algorithms like MD5 and   3 marks: Concept; 4
B   BL3   algorithms in data   SHA generate unique hash values   marks: Application;
integrity.   for files. Even a minor change   3 marks: Example
alters the hash, ensuring integrity.
During forensic acquisition,
original and copied data hashes
are compared to verify
authenticity. Hashing also helps
detect tampering and ensures
admissibility in court.
Q3 CO1;   Recover deleted   10   NTFS stores file records in MFT.   3 marks: NTFS
A BL4   files in NTFS.   Deleted files are marked but not   concept; 4 marks:
erased immediately. Recovery
********** 2 **********
--- page 3 ---
involves analyzing MFT entries,   Recovery methods;
using data carving, and restoring   3 marks: Case
file fragments. Tools like EnCase
help reconstruct deleted data. Case
example: recovering deleted
emails from disk sectors.
Q3 CO1;   BIOS & UEFI   10   BIOS and UEFI initialize   3 marks:
B   BL2   forensic   hardware during boot. UEFI   Explanation; 4
relevance.   provides advanced features like   marks: Differences;
secure boot. Forensically, boot   3 marks: Relevance
logs help identify system
modifications, malware
persistence, and unauthorized
firmware changes.
Q4 CO1;   Steganography   10   Steganography hides data within   3 marks: Concept; 4
A BL4   and detection.   files (images, audio). Detection   marks: Techniques;
involves statistical analysis, file   3 marks: Detection
size comparison, and stego tools.
Investigators identify anomalies in
pixel values or file structures to
uncover hidden data.
Q4 CO2;   Analyze   10   Encrypted containers (e.g.,   3 marks:
B   BL3   encrypted   VeraCrypt) store hidden data.   Identification; 4
containers.   Investigators identify suspicious   marks: Analysis; 3
partitions, analyze entropy levels,   marks: Tools
and use brute-force or key
recovery methods. Memory
analysis may reveal encryption
keys during live acquisition.
Q5 CO2;   Cloud vs   10   Cloud forensics deals with   3 marks:
A BL3   traditional   distributed data, multi-tenancy,   Explanation; 4
forensics.   and lack of physical access.   marks: Differences;
Challenges include jurisdiction,   3 marks: Challenges
data volatility, and provider
dependency. Unlike traditional
forensics, investigators rely on
logs and APIs instead of physical
devices.
Q5 CO2;   DNS logs in   10   DNS logs track domain requests.   3 marks: Concept; 4
B   BL4   investigation.   Malicious domains, phishing   marks: Analysis; 3
attempts, and botnet activity can   marks: Application
be identified through abnormal
queries. Correlation with IP logs
helps trace attacker behavior.
Q6 CO2;   Volatile vs non-   10   Volatile memory (RAM) loses   3 marks:
A BL2   volatile memory.   data when power is off, while   Definitions; 4
non-volatile memory (HDD/SSD)   marks: Differences;
retains data. RAM contains active   3 marks:
processes, encryption keys, and   Importance
network sessions, making it
crucial in live forensics.
********** 3 **********
--- page 4 ---
Q6 CO2;   RAM evidence   10   Capturing RAM is challenging   3 marks:
B   BL3   challenges &   due to volatility, risk of data   Challenges; 4
strategy.   alteration, and tool limitations.   marks: Strategy; 3
Strategy includes using trusted   marks: Application
tools, minimizing system
interaction, and prioritizing
memory acquisition before
shutdown. Analysis reveals
running processes and hidden
malware.
Q7 CO3;   Role of cyber   10   Cyber laws like IT Act 2000   3 marks: Law
A BL2   laws in India.   govern digital evidence handling.   concept; 4 marks:
They ensure legality,   Provisions; 3
admissibility, and protection   marks: Importance
against cybercrime. Sections
define offenses and penalties,
supporting forensic investigations.
Q7 CO3;   Phishing attack   10   Investigation includes analyzing   3 marks: Steps; 4
B   BL5   investigation.   email headers, tracing IP   marks: Analysis; 3
addresses, examining DNS logs,   marks: Prevention
and identifying phishing domains.
User credentials misuse is tracked
through transaction logs.
Preventive measures include
awareness and multi-factor
authentication.
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper 668d6d830154

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_IT_7037/Cyber Forensics/ANS_Cyber Forensics(702IT0E024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: III / IV / V/Semester VI/Semester VIII/Semester X(Exam Year: 2025-2026)
Subject: Cyber Forensics
Date: 12 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q CO;BL   Question   Marks   Detailed Answer (Paragraph)   Rubrics of
No   Evaluation
Q1 CO1;   Explain the   5   Chain of custody ensures that   1 mark: Definition;
A BL2   importance of   digital evidence is properly   2 marks:
chain of custody   collected, documented, and   Importance; 2
with a real-world   preserved from the time of   marks: Real-world
cybercrime   acquisition to presentation in   example
example.   court. It maintains integrity and
prevents tampering. For example,
in a cyber fraud case, if a seized
laptop is not properly logged (who
handled it, when, and why), the
defense may challenge its
authenticity, leading to rejection
in court. Proper documentation,
sealing, labeling, and logging are
essential to maintain credibility.
Q1 CO2;   Analyze how   5   Metadata contains hidden   1 mark: Definition;
B   BL4   metadata in   information such as author name,   2 marks:
documents can be   creation/modification date, device   Types/uses; 2
used as digital   details, and file path. Investigators marks:
evidence.   use metadata to establish   Analysis/example
timelines, identify authorship, and
detect tampering. For instance, a
document claiming to be original
may show metadata indicating it
was edited later, revealing fraud.
Metadata analysis tools help
extract and correlate such
********** 1 **********
--- page 2 ---
information for evidence
validation.
Q1 CO2;   Apply forensic   5   Even after formatting, data   2 marks: Process; 2
C   BL3   techniques to   remains recoverable using   marks:
extract evidence   forensic techniques. Investigators   Tools/techniques; 1
from a formatted   use disk imaging tools (e.g., FTK   mark: Preservation
USB drive.   Imager), data carving methods,   method
and file signature analysis to
recover deleted files. A write
blocker is used to prevent
modification. The process
includes creating a bit-by-bit
image, scanning for residual data,
and reconstructing files based on
headers/footers.
Q1 CO3;   Evaluate the   5   Investigators often access private   2 marks: Issues; 2
D BL5   ethical challenges   data such as emails, photos, and   marks: Evaluation;
in handling   financial records. Ethical   1 mark: Ethical
sensitive personal   challenges include maintaining   practices
data during   confidentiality, avoiding misuse,
investigations.   and ensuring minimal invasion of
privacy. Unauthorized disclosure
or bias may compromise
investigation integrity. Adhering
to legal guidelines, obtaining
proper authorization, and
maintaining professionalism are
critical.
Q2 CO1;   Reconstruct   10   When logs are deleted,   3 marks: Sources; 4
A BL4   attack timeline   investigators reconstruct timelines marks: Process; 3
after logs   using alternative sources such as   marks:
deletion.   system artifacts, registry entries,   Tools/examples
shadow copies, network logs, and
timestamps. File metadata,
browser history, and intrusion
detection system logs help
correlate events. Timeline analysis
tools (e.g., Autopsy) are used to
sequence activities and identify
attack patterns.
Q2 CO1;   Role of hashing   10   Hashing algorithms like MD5 and   3 marks: Concept; 4
B   BL3   algorithms in data   SHA generate unique hash values   marks: Application;
integrity.   for files. Even a minor change   3 marks: Example
alters the hash, ensuring integrity.
During forensic acquisition,
original and copied data hashes
are compared to verify
authenticity. Hashing also helps
detect tampering and ensures
admissibility in court.
Q3 CO1;   Recover deleted   10   NTFS stores file records in MFT.   3 marks: NTFS
A BL4   files in NTFS.   Deleted files are marked but not   concept; 4 marks:
erased immediately. Recovery
********** 2 **********
--- page 3 ---
involves analyzing MFT entries,   Recovery methods;
using data carving, and restoring   3 marks: Case
file fragments. Tools like EnCase
help reconstruct deleted data. Case
example: recovering deleted
emails from disk sectors.
Q3 CO1;   BIOS & UEFI   10   BIOS and UEFI initialize   3 marks:
B   BL2   forensic   hardware during boot. UEFI   Explanation; 4
relevance.   provides advanced features like   marks: Differences;
secure boot. Forensically, boot   3 marks: Relevance
logs help identify system
modifications, malware
persistence, and unauthorized
firmware changes.
Q4 CO1;   Steganography   10   Steganography hides data within   3 marks: Concept; 4
A BL4   and detection.   files (images, audio). Detection   marks: Techniques;
involves statistical analysis, file   3 marks: Detection
size comparison, and stego tools.
Investigators identify anomalies in
pixel values or file structures to
uncover hidden data.
Q4 CO2;   Analyze   10   Encrypted containers (e.g.,   3 marks:
B   BL3   encrypted   VeraCrypt) store hidden data.   Identification; 4
containers.   Investigators identify suspicious   marks: Analysis; 3
partitions, analyze entropy levels,   marks: Tools
and use brute-force or key
recovery methods. Memory
analysis may reveal encryption
keys during live acquisition.
Q5 CO2;   Cloud vs   10   Cloud forensics deals with   3 marks:
A BL3   traditional   distributed data, multi-tenancy,   Explanation; 4
forensics.   and lack of physical access.   marks: Differences;
Challenges include jurisdiction,   3 marks: Challenges
data volatility, and provider
dependency. Unlike traditional
forensics, investigators rely on
logs and APIs instead of physical
devices.
Q5 CO2;   DNS logs in   10   DNS logs track domain requests.   3 marks: Concept; 4
B   BL4   investigation.   Malicious domains, phishing   marks: Analysis; 3
attempts, and botnet activity can   marks: Application
be identified through abnormal
queries. Correlation with IP logs
helps trace attacker behavior.
Q6 CO2;   Volatile vs non-   10   Volatile memory (RAM) loses   3 marks:
A BL2   volatile memory.   data when power is off, while   Definitions; 4
non-volatile memory (HDD/SSD)   marks: Differences;
retains data. RAM contains active   3 marks:
processes, encryption keys, and   Importance
network sessions, making it
crucial in live forensics.
********** 3 **********
--- page 4 ---
Q6 CO2;   RAM evidence   10   Capturing RAM is challenging   3 marks:
B   BL3   challenges &   due to volatility, risk of data   Challenges; 4
strategy.   alteration, and tool limitations.   marks: Strategy; 3
Strategy includes using trusted   marks: Application
tools, minimizing system
interaction, and prioritizing
memory acquisition before
shutdown. Analysis reveals
running processes and hidden
malware.
Q7 CO3;   Role of cyber   10   Cyber laws like IT Act 2000   3 marks: Law
A BL2   laws in India.   govern digital evidence handling.   concept; 4 marks:
They ensure legality,   Provisions; 3
admissibility, and protection   marks: Importance
against cybercrime. Sections
define offenses and penalties,
supporting forensic investigations.
Q7 CO3;   Phishing attack   10   Investigation includes analyzing   3 marks: Steps; 4
B   BL5   investigation.   email headers, tracing IP   marks: Analysis; 3
addresses, examining DNS logs,   marks: Prevention
and identifying phishing domains.
User credentials misuse is tracked
through transaction logs.
Preventive measures include
awareness and multi-factor
authentication.
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 7cd49f82cef3

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_Computer_7002/Cyber Forensics/ANS_Cyber Forensics(702IT0E024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Feb 2026
- Text: text (3 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech (COMP)/B. Tech Intg. (CE)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Cyber Forensics
Date: 04 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory and covers all units.
5. Attempt any four questions from Q2 to Q7.
6. All questions carry equal marks (20 each).
7. Begin each answer on a fresh page.
8. Assume suitable data if necessary.
9. Use of calculator/graph paper is permitted wherever applicable.
Q1
a. Definition, Scope & Relevance of Digital Forensics (5 Marks)
•   Definition: Digital Forensics is the scientific process of identifying, acquiring, preserving, analysing, and
presenting data from digital devices in a legally acceptable manner.
• Scope: Includes computer, mobile, network, and cloud forensics.
•   Relevance: Essential for investigating cybercrimes, insider threats, data breaches, and ensuring
compliance with cybersecurity frameworks in the digital ecosystem.
b. Classification of Cybercrimes & Recent Examples (5 Marks)
• Types:
o   Financial frauds (phishing, card cloning, UPI scams)
o Data breaches (unauthorised access or leakage)
o Cyberstalking & identity theft
o Hacking and malware deployment
• Recent Examples:
o 2024 Zerodha account breach – customer data compromised.
o AIIMS ransomware attack (2022) – patient database encrypted and held for ransom.
c. Digital Evidence & Evidence Lifecycle (5 Marks)
• Concept: Any information stored or transmitted digitally that can prove or disprove an event (e.g.,
emails, logs, metadata).
•   Lifecycle Steps:
1. Collection: Identifying and securing potential evidence.
2. Preservation: Using write blockers, hashing.
3. Analysis: Extracting relevant data using forensic tools.
4. Documentation: Maintaining detailed logs.
5. Presentation: Reporting findings in court-admissible form.
d. Ethical & Professional Responsibilities (5 Marks)
•   Maintain confidentiality, integrity, and impartiality.
• Avoid bias or tampering with evidence.
********** 1 **********
--- page 2 ---
•   Respect privacy laws and chain-of-custody standards.
• Follow professional codes such as ISFCE and NIST guidelines.
• Handle ethical dilemmas where client confidentiality conflicts with legal duty.
Q2
a. Comparison of FAT32 and NTFS (10 Marks)
Feature   FAT32   NTFS
Directory Structure Linked list   Master File Table (MFT)
Allocation   Simple cluster mapping   Uses metadata and journaling
Security   No file permissions   Supports ACLs, encryption (EFS)
File Size Limit   4 GB   16 TB+
Forensic View   Easier carving but lacks metadata Rich metadata, aids timestamp analysis
b. Boot Sector & Windows Registry in Forensics (10 Marks)
• Boot Sector: Contains OS loader, partition table—critical for detecting boot-kits or MBR tampering.
•   Registry: Stores configuration data (user accounts, USB history, last login).
•   Forensic Relevance:
o Helps reconstruct user activity timelines.
o   Identifies malware persistence and unauthorised system modifications.
Q3
a. File Reconstruction & Data Carving (10 Marks)
• Header Analysis: Identifies file type using magic numbers (e.g., JPEG: FFD8–FFD9).
• Data Carving: Recovers files from unallocated or slack space using pattern recognition.
• Procedure: Identify → Scan sectors → Extract data blocks → Rebuild → Validate via hash.
•   Tools: PhotoRec, Scalpel, Autopsy.
b. Whole Disk Encryption & Forensic Imaging (10 Marks)
•   Encryption (e.g., BitLocker, VeraCrypt) prevents direct imaging.
•   Effects:
o Requires pre-boot key or live acquisition before power-off.
o Decryption key recovery from memory dump (RAM) often essential.
•   Mitigation: Capture memory first, then create encrypted image clone with hash verification.
Q4
a. Live Network Traffic Capture & Analysis (10 Marks)
• Methods: Packet sniffing, port mirroring, network taps.
•   Tools: Wireshark, tcpdump, NetworkMiner, Zeek (Bro).
•   Process:
1. Capture real-time packets.
2. Filter IPs, ports, and protocols.
3. Analyse payloads, DNS logs, anomalies.
4. Reconstruct sessions or identify malicious traffic.
b. Malware Analysis & Data Hiding in Network (10 Marks)
•   Phases:
1. Static analysis (hash, signature, PE header).
2. Dynamic analysis (sandbox execution).
3. Behavioural correlation (registry, process, network activity).
• Data Hiding: Steganography, tunnelling (DNS/HTTP), encryption.
•   Detection: Entropy analysis, payload inspection, correlation with IoCs.
Q5
a. Mobile Acquisition (Android & iOS) (10 Marks)
• Android: ADB backup, logical extraction, physical image via bootloader or JTAG.
• iOS: iTunes backup, logical extraction, or DFU mode imaging.
********** 2 **********
--- page 3 ---
•   Limitations: Encryption, root/jailbreak restrictions, volatile data loss, cloud dependency.
•   Tools: Cellebrite UFED, Oxygen Forensic, MOBILedit, Magnet AXIOM.
b. Wi-Fi & Bluetooth Artifacts in Correlation (10 Marks)
• Wi-Fi: SSID logs, MAC addresses, connection timestamps help place a suspect.
•   Bluetooth: Device pairings, UUIDs link accessories or shared data.
•   Correlation: Combine network logs with mobile metadata for timeline reconstruction.
Q6
a. IT Act 2000 (Amended 2008) & Admissibility (10 Marks)
• Key Provisions:
o Sec. 43 & 66: Unauthorised access/hacking.
o Sec. 67: Obscene content publication.
o Sec. 69: Decryption powers.
o Sec. 79A: Appointment of Examiner of Electronic Evidence.
•   Admissibility: Section 65B of Indian Evidence Act – electronic evidence must include certification,
authenticity, and hash verification.
b. File Timestamp Metadata & Legal Challenges (10 Marks)
• Timestamps: Created, modified, accessed (MAC times).
• Use: Establish activity sequence and suspect behaviour.
•   Challenges:
o Clock manipulation, timezone mismatch.
o Metadata alteration via copying.
o Validation through cross-source logs (system, registry, network).
Q7
a. Forensic Plan – Bank Fund Transfer Case (10 Marks)
•   Incident Response: Isolate compromised systems.
• Data Collection: Secure logs (firewall, proxy, email headers).
•   Analysis: Correlate timestamps, identify IPs, detect privilege escalation.
• System Artifacts: Event logs, browser history, registry entries.
•   Attribution: Map internal account access and user IDs to transaction trails.
•   Reporting: Summarise findings for legal and compliance submission.
b. Preventive Measures & Reporting Standards (10 Marks)
•   Preventive:
o Maintain proper chain of custody and hash records.
o Use court-recognised tools (EnCase, FTK).
o Document acquisition details (time, personnel, media).
• Reporting Standards:
o Follow ISO/IEC 27037 and NIST SP 800-86.
o Ensure reports are factual, reproducible, and legally admissible.
o Attach digital signatures, certification, and audit trail logs.
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 8 · Answer key · paper d8da4b0e2e3f

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_08/Re-Exam/MBATech_Computer_7047/Cyber Forensics/ANS_Cyber Forensics(702IT0E024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Jul 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech (IT)
Year: IV/Sem 8 Re-exam(Exam Year: 2025-2026)
Subject: Cyber Forensics
Date: 08 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks
8. Assume Suitable data if necessary
Q CO;BL   Question   Marks   Detailed Answer (Paragraph)   Rubrics of
No   Evaluation
Q1 CO1;   Explain the   5   The digital evidence lifecycle includes   2 marks: Phases;
A BL2   concept of   identification, collection, preservation,   2 marks:
digital   examination, analysis, and   Explanation; 1
evidence   presentation. Evidence is first   mark: Flow
lifecycle.   identified at the crime scene, then
collected using forensic tools while
maintaining integrity. It is preserved
using hashing and chain of custody,
followed by examination and analysis
to extract meaningful information.
Finally, it is presented in court in a
legally acceptable manner.
Q1 CO2;   Compare lossy   5   Lossy compression reduces file size by   2 marks:
B   BL4   and lossless   discarding some data (e.g., JPEG),   Comparison; 2
compression in   which may affect evidence integrity.   marks: Forensic
forensic   Lossless compression (e.g., PNG, ZIP)   impact; 1 mark:
analysis.   preserves original data without loss. In   Example
forensics, lossless methods are
preferred to maintain evidential
accuracy, while lossy formats may
distort critical details such as pixel data
or metadata.
********** 1 **********
--- page 2 ---
Q1 CO2;   Describe how   5   Evidence acquisition from a damaged   2 marks: Process;
C   BL3   you would   disk involves using hardware-based   2 marks: Tools; 1
acquire   imaging tools, write blockers, and   mark:
evidence from   specialized recovery software.   Preservation
a damaged   Techniques include sector-by-sector
hard disk.   imaging, use of cleanroom facilities for
physical damage, and logical extraction
where possible. Ensuring no further
damage and maintaining data integrity
are critical.
Q1 CO3;   Discuss legal   5   Improper handling can lead to evidence 2 marks: Risks; 2
D BL5   risks involved   tampering, loss of integrity, and   marks: Legal
in improper   inadmissibility in court. Legal risks   impact; 1 mark:
evidence   include case dismissal, investigator   Preventive
handling.   liability, and violation of privacy laws.   measures
Maintaining proper documentation,
chain of custody, and adherence to
legal standards is essential to avoid
such risks.
Q2 CO1;   Detect data   10   Investigators analyze USB logs,   3 marks: Sources;
A BL4   leakage using   registry entries, file transfer records,   4 marks:
external   and system artifacts to detect   Analysis; 3
storage.   unauthorized data transfer. Tools like   marks: Proof
EnCase help trace file movement.
Correlating timestamps, user activity,
and device identifiers helps prove data
leakage.
Q2 CO1;   Explain FAT   10   FAT structure includes boot sector,   3 marks:
B   BL3   structure and   FAT table, and data region. It tracks   Structure; 4
forensic   file allocation and deletion.   marks: Working;
significance.   Forensically, deleted files can be   3 marks:
recovered as entries are marked but not   Significance
erased. FAT helps identify file
fragmentation and hidden data.
Q3 CO1;   Registry   10   Windows Registry stores system and   3 marks:
A BL4   forensics for   user activity data such as login times,   Concept; 4
user activity.   installed programs, and USB usage.   marks:
Investigators analyze keys like   Keys/examples; 3
HKEY_LOCAL_MACHINE and   marks:
HKEY_CURRENT_USER to   Application
reconstruct user behavior and detect
suspicious activities.
********** 2 **********
--- page 3 ---
Q3 CO1;   Disk imaging   10   Disk imaging involves creating an   3 marks: Process;
B   BL2   process and   exact bit-by-bit copy of storage media   4 marks: Tools; 3
tools.   using tools like FTK Imager or dd.   marks: Integrity
Write blockers ensure no modification.
Hash values verify integrity. Imaging
preserves original evidence for
analysis.
Q4 CO1;   Anti-forensic   10   Attackers use anti-forensic techniques   3 marks:
A BL4   techniques.   such as data wiping, encryption,   Techniques; 4
steganography, log deletion, and   marks:
timestamp manipulation. These   Explanation; 3
methods aim to hide evidence and   marks: Detection
mislead investigators. Detecting such
techniques requires advanced analysis
tools and cross-validation.
Q4 CO2;   Acquire data   10   Investigators use methods like logical   3 marks:
B   BL3   from locked   acquisition, chip-off, JTAG, and   Methods; 4
smartphone.   exploiting vulnerabilities to extract   marks: Process; 3
data. Maintaining chain of custody and   marks: Integrity
avoiding data alteration is crucial.
Tools like Cellebrite assist in mobile
data extraction while ensuring
integrity.
Q5 CO2;   Analyze   10   Investigators extract chat logs, media   3 marks:
A BL3   mobile   files, and metadata from messaging   Extraction; 4
cyberstalking   apps using forensic tools. Timeline   marks: Analysis;
evidence.   analysis, geolocation data, and   3 marks:
communication patterns help establish   Evidence
cyberstalking behavior. Deleted   correlation
messages may be recovered from
backups or databases.
Q5 CO2;   Firewall logs   10   Firewall logs record incoming and   3 marks:
B   BL4   in   outgoing traffic, blocked attempts, and   Concept; 4
investigation.   suspicious IPs. Analysis helps detect   marks: Analysis;
intrusion attempts, unauthorized   3 marks:
access, and malware communication.   Application
Correlation with other logs strengthens
evidence.
Q6 CO2;   Packet sniffing 10   Packet sniffing captures network traffic 3 marks:
A BL2   in forensics.   using tools like Wireshark. It helps   Concept; 4
analyze communication patterns, detect marks: Working;
anomalies, and identify malicious   3 marks: Use
********** 3 **********
--- page 4 ---
packets. It is essential in network
intrusion investigations.
Q6 CO2;   Trace spoofed   10   Investigators use packet analysis,   3 marks:
B   BL3   IP in DDoS   ingress filtering, log correlation, and   Techniques; 4
attack.   traceback techniques to identify real   marks: Analysis;
sources behind spoofed IPs. IDS and   3 marks:
network monitoring tools assist in   Challenges
filtering fake traffic and tracing attack
paths.
Q7 CO3;   Legal   10   Digital evidence must comply with   3 marks: Laws; 4
A BL2   admissibility of   Information Technology Act, 2000 and   marks:
digital   Indian Evidence Act, 1872 (Section   Requirements; 3
evidence.   65B). Proper certification, integrity   marks:
verification, and chain of custody   Application
ensure admissibility in court.
Q7 CO3;   Ransomware   10   Investigation involves identifying   3 marks: Steps; 4
B   BL5   investigation.   malware entry points, analyzing   marks: Analysis;
encrypted files, tracing attacker   3 marks:
communication, and recovering   Recovery
evidence from backups or logs.
Decryption tools and forensic analysis
help restore data and identify
perpetrators.
********** 4 **********
````
