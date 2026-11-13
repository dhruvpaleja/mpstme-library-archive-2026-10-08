# Network Security: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper aa34906cdae8

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CyberSecurity_7010/Network Security/ANS_Network Security(702IT0C014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 26 Nov 2025
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Semester V(Exam Year: 2025-2026)
Subject: Network Security
Date: 26 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 11 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
a. Discuss the security mechanisms with an example authentication exchange, 5
traffic padding, routing control, and notarization.
Marking Scheme: 1 mark per mechanism with example (total 4 × 1.25 = 5
marks)
Answer:
1. Authentication Exchange:
o Mechanism to verify identity of communicating entities before
data exchange.
o Example: Kerberos uses tickets for mutual authentication
between client and server.
2. Traffic Padding:
CO- 1;
o Adds dummy data to disguise real traffic volume and timing to
BL-2
resist traffic analysis.
o Example: VPNs may pad packets to a fixed length.
3. Routing Control:
o Ensures data travels through secure or approved network paths.
o Example: Using BGP filters or secure routing policies to avoid
untrusted nodes.
4. Notarization:
o Involves a trusted third party verifying data authenticity and
timestamp.
o Example: Digital notarization using blockchain for document
validation.
b. Discuss the SSH connection layer with a diagram.   5
CO- 2;
BL-2   Marking Scheme: 2 marks – SSH layer overview, 2 marks – Connection
layer explanation, 1 mark – Diagram
********** 1 **********
--- page 2 ---
Answer:
• Overview:
SSH (Secure Shell) is structured in three layers:
1. Transport Layer: Provides server authentication,
confidentiality, and integrity using symmetric encryption.
2. Authentication Layer: Authenticates the client using passwords,
keys, or certificates.
3. Connection Layer: Manages multiple logical channels (like
shell, SCP, port forwarding) within one secure tunnel.
Example:
When a user connects via SSH to a server, the transport layer establishes
encryption, the authentication layer validates credentials, and the connection
layer opens a terminal session.
c.   Distinguish between transport vs tunnel mode in IP security mechanism. (Any 5
5 points)
Marking Scheme: 1 mark per valid comparison point
Answer:
Feature   Transport Mode   Tunnel Mode
Encryption   Encrypts only data payload   Encrypts entire IP packet
CO- 3;   Scope
BL-4   Header   Retains original IP header   Adds a new IP header
Handling
Usage Scenario   Host-to-host communication   Gateway-to-gateway
(VPN)
Overhead   Lower (less encapsulation)   Higher due to extra
header
Example   End-to-end email or SSH   Site-to-site VPN between
security   offices
********** 2 **********
--- page 3 ---
d. Distinguish between Declarative vs Imperative approach used in Benefits of 5
Infrastructure as Code (Any 5 Points).
Marking Scheme:
• 1 mark per valid difference (5 × 1 = 5 marks)
Aspect   Declarative Approach   Imperative Approach
Definition   Describes what the final Defines how to build it step-by-
infrastructure should   step
CO-2;   look like
BL-2   Control   The tool determines   The user controls every
steps to achieve the   operation
desired state
Example Tools   Terraform,   Ansible, Shell Scripts
CloudFormation
Ease of   Easier to maintain and   Requires procedural expertise
Maintenance   version
Focus   End state (desired   Process (execution sequence)
configuration)
a. Discuss the security services defined by IETF with an example   [10]
Marking Scheme: 2 marks per correctly explained service (5 × 2 = 10 marks)
Answer:
The IETF defines the following security services under RFC 4949 and ISO
7498-2:
1. Authentication:
o Confirms the identity of the sender or receiver.
o Example: Digital certificates in TLS validate a server’s identity.
Q2   2. Access Control:
o   Restricts unauthorized access to resources.
CO-1;   o Example: Firewalls or NAC policies allow only authorized
BL-3   users.
3. Data Confidentiality:
o Ensures data is only readable by authorized entities.
o Example: AES encryption in IPsec or HTTPS.
4. Data Integrity:
o Protects data from being altered during transmission.
o Example: HMAC-SHA256 ensures message integrity in TLS.
5. Non-Repudiation:
o Prevents sender from denying sending a message.
o Example: Digital signatures in PGP verify message origin.
b. During a campus event, a guest device connected to the guest Wi-Fi begins [10]
generating suspicious traffic patterns. Network administrators suspect a
CO-1;   malware infection. Describe how NAC monitoring tools can detect abnormal
BL-4   traffic from guest devices. Suggest enforcement actions NAC could take to
isolate or quarantine the compromised device.
Marking Scheme: 5 marks – Detection (monitoring methods, indicators), 5
marks – Enforcement (isolation/quarantine actions)
********** 3 **********
--- page 4 ---
Answer:
• Scenario:
A guest device on campus Wi-Fi shows abnormal traffic — large data
uploads, irregular port scans — suggesting a malware infection.
Detection:
• NAC uses real-time traffic monitoring and behavioral analytics to
detect anomalies.
• Tools analyze bandwidth usage, session duration, and protocol types.
•   Integration with IDS/IPS systems (like Cisco ISE or ForeScout) helps
flag suspicious patterns.
• Example: NAC detects a spike in outbound connections from one IP,
triggering a security alert.
Enforcement:
• Immediate Quarantine: Move device to a restricted VLAN or
remediation network.
• Access Restriction: Block specific services (e.g., internal servers).
•   Notification: Inform user to run antivirus scan or patch updates.
• Remediation Portal: Allows compliant re-authentication post-cleanup.
•   Alerting: Notify IT admin for further investigation.
a. Discuss the working EAP-TTLS mechanism with a diagram and benefits of [10]
using EAP-TTLS.
Marking Scheme: 3 marks – Explanation of EAP-TTLS mechanism (phases),
2 marks – Diagram (labeled, clear steps), 3 marks – Benefits, 2 marks –
Example or context of use (e.g., enterprise Wi-Fi)
Answer:
• Working Mechanism:
• Phase 1 – Outer TLS Tunnel Creation:
1. The client and authentication server establish a secure TLS tunnel
using server-side certificates.
2. The server authenticates itself to the client, ensuring that the client
communicates with a trusted server.
• Phase 2 – Inner Authentication:
1. Inside the encrypted tunnel, the client authenticates using legacy
Q3   methods like PAP, CHAP, or MS-CHAPv2.
2. The TLS layer protects these inner credentials from eavesdropping.
CO-1;   •   Result:
BL-2   1. Once mutual authentication is successful, session keys are
generated and distributed for secure communication.
Benefits:
• Only the server requires a certificate (reduces PKI complexity).
********** 4 **********
--- page 5 ---
•   Protects user credentials within TLS tunnel.
• Compatible with existing authentication methods.
•   Provides mutual authentication and dynamic session key generation.
•   Efficient and secure for Wi-Fi enterprise authentication.
b. Compare and contrast WPA2 and WPA3 algorithms used in WiFi security.   [10]
Marking Scheme:
• 5 marks – WPA2 explanation and features
• 5 marks – WPA3 enhancements and comparison (any five valid points)
Feature   WPA2   WPA3
Encryption   AES-CCMP (Counter   AES-GCMP (Galois Counter
Algorithm   Mode CBC-MAC)   Mode) – stronger integrity
and speed
Key   PSK (Pre-Shared Key) or SAE (Simultaneous
Exchange   802.1X   Authentication of Equals) –
resists offline dictionary
attacks
Forward   Not guaranteed   Ensured – new keys for each
CO-1;   Secrecy   session
BL-4   Open   Unencrypted data   Opportunistic Wireless
Networks   transmission   Encryption (OWE) provides
encryption even without
password
Authenticati Vulnerable to brute-force   Strong mutual authentication
on   PSK attacks   with password element
Protection   binding
Device   IoT devices may have   WPA3-Enterprise supports
Security   weak PSK   192-bit security suite
Ease of   Manual PSK entry   WPA3 Easy Connect (QR
Configuratio   code–based configuration)
n
Status   Older (2004), vulnerable   Latest standard (2018),
to KRACK   improved cryptographic
resilience
a. Discuss how TLS ensures data confidentiality, integrity, and authentication [10]
during secure communication. Support your answer with examples of
encryption and hashing mechanisms used in TLS.
Marking Scheme: 3 marks – Confidentiality explanation with example, 3
marks – Integrity explanation with example, 3 marks – Authentication
explanation with example, 1 mark – Overall flow/clarity
Answer:
Q4
CO-2;   •   Confidentiality:
BL-2   TLS ensures that transmitted data is encrypted using symmetric algorithms
such as AES or ChaCha20, making it unreadable to attackers.
Example: When a user logs in to an HTTPS website, their credentials are
encrypted during transmission.
•   Integrity:
TLS uses Message Authentication Codes (MACs) or Authenticated
Encryption (AEAD) to ensure data is not altered during transmission.
Example: TLS 1.2 uses HMAC-SHA256, while TLS 1.3 uses AEAD with
AES-GCM to verify data integrity.
********** 5 **********
--- page 6 ---
• Authentication:
The server (and optionally client) presents digital certificates signed by a
trusted Certificate Authority (CA). The client validates the certificate to
ensure it is communicating with the legitimate server.
Example: A browser verifies a server’s SSL certificate issued by DigiCert
before establishing a session.
• Flow:
1. TLS handshake authenticates parties using asymmetric encryption
(RSA, ECDHE).
2. Session keys are derived and exchanged securely.
3. Subsequent communication uses symmetric encryption for speed.
b. A cybersecurity analyst notices that DNS responses from a government [10]
domain are being spoofed, leading users to malicious sites. The analyst
recommends implementing DNSSEC. Apply your knowledge of DNSSEC to
describe how digital signatures and public key validation can prevent DNS
spoofing. Suggest steps for proper DNSSEC deployment and verification at
resolver level.
Marking Scheme: 4 marks – Explanation of DNS spoofing prevention using
signatures/keys, 3 marks – Steps for DNSSEC deployment, 3 marks –
Resolver-level verification
Answer:
• DNSSEC Overview:
DNSSEC (Domain Name System Security Extensions) adds digital
signatures to DNS records to verify authenticity and integrity.
Each DNS zone signs its records using its private key, generating RRSIG
records. Resolvers use the DNSKEY and chain of trust to verify these
signatures.
CO-2;   • How It Prevents Spoofing:
BL-3   o Attackers can’t forge signed DNS data since they don’t have the
private key.
o The resolver validates responses using public keys published in
DNSKEY records.
o   If the signature verification fails, the resolver discards the fake
response, preventing redirection to malicious sites.
• Steps for Proper DNSSEC Deployment:
o Generate zone-signing (ZSK) and key-signing keys (KSK).
o Sign zone records to produce RRSIGs.
o Publish the DS record in the parent zone for trust chaining.
o Regularly rotate and manage keys securely.
• Resolver Verification:
o Enable DNSSEC validation at resolver (e.g., Unbound, BIND9).
o Resolver verifies RRSIG with DNSKEY and validates DS chain of
trust up to root.
o   If validation succeeds → authentic data; if fails → reject the
response.
********** 6 **********
--- page 7 ---
a. An educational institution deploys DMARC to protect against domain [10]
spoofing in student notifications. Explain the function of DMARC in aligning
SPF and DKIM results. Describe how DMARC policies (“none”,
“quarantine”, “reject”) influence message delivery.
Marking Scheme: 3 marks – Function of DMARC and alignment concept, 3
marks – Explanation of SPF and DKIM alignment, 4 marks – DMARC policy
types and their effect on message delivery
Answer:
• DMARC (Domain-based Message Authentication, Reporting, and
Conformance) is an email authentication protocol designed to detect and
prevent email spoofing by aligning SPF and DKIM results with the
domain in the “From” header.
• Function:
o DMARC ensures that the domain used in SPF (envelope sender)
and DKIM (signed domain) matches the domain in the visible
Q5
From address.
CO-2;   o   If either SPF or DKIM passes and the alignment is valid, the email
BL-2   passes DMARC authentication.
• Alignment Example:
o SPF: Checks if the sender’s IP is authorized for the domain.
o DKIM: Verifies digital signature created by the sender’s private
key.
o DMARC: Confirms that both results align with the “From” domain.
• DMARC Policies:
o p=none – Monitor only; no action taken. Used for testing and data
collection.
o p=quarantine – Suspicious messages are sent to spam/junk folders.
o p=reject – Messages failing authentication are rejected before
delivery.
Example:
If an email pretends to come from university.edu but fails SPF/DKIM
alignment, DMARC with policy p=reject blocks it, preventing spoofed student
notifications.
b. A multinational company connects its branch offices through the Internet [10]
using Virtual Private Networks (VPNs). The network administrator decides
to implement IPSec to secure all inter-branch communications. Explain how
IPSec ensures confidentiality, integrity, and authentication of data
transmitted over public networks. Describe the roles of Authentication
Header (AH) and Encapsulating Security Payload (ESP) in achieving these
CO-2;   objectives.
BL-2
Marking Scheme: 3 marks – Explanation of confidentiality, integrity, and
authentication, 3 marks – Description of IPSec operation, 4 marks – Roles of
AH and ESP
Answer:
********** 7 **********
--- page 8 ---
• IPSec Overview:
IPSec secures IP communication by encrypting and authenticating each IP
packet. It operates in transport or tunnel mode and uses security
associations (SAs) established by IKE (Internet Key Exchange).
•   Security Objectives:
o Confidentiality: Achieved using symmetric encryption algorithms
such as AES or 3DES, ensuring data cannot be read by
unauthorized entities.
o Integrity: Achieved through HMAC (Hash-based Message
Authentication Code), ensuring data is not altered in transit.
o Authentication: Validates source identity using digital signatures
or pre-shared keys.
• Roles of Headers:
o Authentication Header (AH):
▪   Provides connectionless integrity and data origin
authentication.
▪   Protects most IP header fields and payload.
▪ Does not provide encryption (no confidentiality).
o Encapsulating Security Payload (ESP):
▪   Provides encryption (confidentiality), integrity, and
authentication of payload.
▪ Can work independently or combined with AH for stronger
security.
a. A company’s IT administrator notices multiple failed login attempts from [10]
various geographic locations on their Infrastructure as a Service (IaaS)
dashboard. Explain how this activity indicates a possible brute-force or
credential-stuffing attack. Discuss how logging, monitoring, and intrusion
detection can help identify and respond to such attacks in a cloud
environment.
Marking Scheme: 4 marks – Explanation of attack indicators, 3 marks – Role
of logging and monitoring, 3 marks – Role of intrusion detection in response
Answer:
Q6
• Attack Indicators:
CO-3;   Multiple failed login attempts from different geographic regions indicate
BL-3   brute-force or credential-stuffing attacks, where attackers try numerous
username-password combinations to gain unauthorized access.
• Logging and Monitoring:
o Logs track failed login attempts, IP addresses, and timestamps.
o Correlating this data reveals unusual access patterns (e.g., multiple
countries in short time).
o Continuous monitoring tools (e.g., AWS CloudTrail, Azure
Monitor) detect anomalies.
•   Intrusion Detection and Response:
o IDS/IPS systems (like Snort or Suricata) can trigger alerts for
excessive failed logins.
o Automated actions include blocking suspicious IPs, enforcing
multi-factor authentication, and throttling repeated login attempts.
********** 8 **********
--- page 9 ---
o Administrators can analyze logs and take mitigation steps — such
as password resets or API key revocation.
Example:
An attacker tries 1,000 login attempts on an IaaS portal. IDS flags abnormal
login rate → system blocks IP → triggers MFA enforcement policy.
b. Explain the role of network monitoring tools in maintaining network [10]
performance and security. Discuss three key benefits of implementing
automated network monitoring systems.
Marking Scheme: 4 marks – Explanation of role in performance and security,
6 marks – Three benefits explained clearly with examples (2 marks each)
Answer:
• Role:
Network monitoring tools continuously observe network traffic, device
health, and performance metrics. They help detect faults, performance
degradation, and potential intrusions in real time.
• Key Benefits:
CO-3;   1. Early Detection of Threats: Identifies abnormal traffic or
BL-2   bandwidth spikes that could indicate malware or DDoS attacks.
Example: Wireshark or SolarWinds alerts admins to excessive ICMP
packets.
2. Performance Optimization: Monitors latency, packet loss, and
throughput to ensure network reliability and prevent downtime.
Example: PRTG detects overloaded routers and triggers alerts.
3. Automated   Alerts &   Reporting:   Provides   dashboards,
notifications,   and   logs   for   faster   troubleshooting.
Example: Nagios auto-notifies admins when CPU usage crosses a
threshold.
Summary:
Automated network monitoring ensures both security visibility and
performance stability, enabling proactive response to incidents.
a. A financial institution’s mobile app uses TLS 1.0 for secure transactions. [10]
Security auditors recommend upgrading to TLS 1.3. Explain why using
outdated TLS versions poses security risks. Describe the improvements TLS
1.3 introduces in the handshake and encryption. Discuss how these changes
enhance data confidentiality and integrity.
Q7
CO-3;   Marking Scheme: 3 marks – Explanation of risks in TLS 1.0, 4 marks – TLS
BL-2   1.3 improvements (handshake, encryption), 3 marks – Explanation of how
confidentiality and integrity are enhanced
Answer:
• Risks of TLS 1.0:
********** 9 **********
--- page 10 ---
o Uses outdated cipher suites (e.g., RC4, SHA-1) vulnerable to
cryptographic attacks.
o Susceptible to BEAST and POODLE attacks exploiting weak block
cipher modes.
o Longer handshake increases latency and exposure to downgrade
attacks.
• Improvements in TLS 1.3:
o Simplified Handshake: Reduces to one round trip (1-RTT),
minimizing attack surface.
o Forward Secrecy: Mandates use of ephemeral key exchanges
(ECDHE), preventing decryption of past sessions even if keys are
compromised.
o Stronger Encryption: Supports only modern algorithms like AES-
GCM and ChaCha20-Poly1305.
o Removed Insecure Features: No RSA key exchange or static keys;
compression and renegotiation eliminated.
• Enhancement of Security:
o Confidentiality: End-to-end encryption with ephemeral keys
ensures privacy of session data.
o Integrity: Authenticated Encryption (AEAD) verifies message
authenticity.
o Authentication: Server authentication via certificates remains
mandatory.
Summary:
TLS 1.3 delivers faster, more private, and more secure communication by
eliminating legacy vulnerabilities and enforcing modern cryptography —
protecting financial transactions and sensitive mobile data.
b. Explain the counter measures to be considered to secure a mobile device with [10]
an example.
Marking Scheme: 2 marks for each point
❑ Device Access Protection
❑ Enable auto-lock and require a PIN, password, or biometric
authentication.
❑ Encrypt emails and stored data so they can only be accessed with
the PIN/password.
❑ Data Security
❑ Prohibit storage of sensitive data, or ensure it is encrypted.
CO-3;   ❑ Avoid auto-complete features that save usernames and passwords.
BL-2   Enable remote wipe and disable lost/stolen devices to prevent data
theft.
❑ Administrative Controls
❑ IT staff should have remote management access to wipe or lock
devices.
❑ Disable unnecessary features (e.g., camera use) when not required.
❑ Network and Application Security
❑ Ensure SSL/TLS protection is enabled for communication.
❑ Keep operating systems and applications up to date with patches.
❑ Install and update antivirus software as available.
❑ Use whitelisting (allow only trusted apps) and sandboxing (isolate
apps).
********** 10 **********
--- page 11 ---
❑ Restrict synchronization and cloud storage to trusted services.
❑ User Awareness and Training
❑ Train employees to recognize untrusted content (e.g., phishing
links, malicious QR codes).
❑ Encourage safe practices when connecting to public Wi-Fi or
installing apps
********** 11 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper d374ceccf9b6

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CyberSecurity_7010/Network Security/ANS_Network Security(702IT0C014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (CYBER SECURITY)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Network Security
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer the following questions.   [20]
a. Discuss the terms with an example encipherment, digital signatures, access 5
controls, and data integrity.
Answer:
Marking Scheme: 1.25 marks per term (definition + example × 4 = 5 marks)
1. Encipherment:
o Conversion of plaintext into ciphertext using an encryption
algorithm and key to ensure confidentiality.
o Example: AES encryption used in secure file transfer.
2. Digital Signatures:
o Provide authentication and non-repudiation using asymmetric
cryptography.
CO- 1;
o Example: Signing an email using PGP ensures sender authenticity.
BL-2
3. Access Controls:
o Mechanisms that restrict user access to authorized resources based
on identity or role.
o Example: File permissions in Linux that allow access only to certain
users.
4. Data Integrity:
o Ensures that information has not been altered or tampered during
transmission or storage.
o Example: Using SHA-256 hash verification for downloaded
software.
CO- 2;   b. Explain the working of HTTPs with a diagram.   5
BL-2   Answer:
********** 1 **********
--- page 2 ---
Marking Scheme: 2 marks – Explanation of HTTPS process, 2 marks – TLS
handshake description, 1 mark – Diagram or labeled steps
• HTTPS (Hypertext Transfer Protocol Secure) is HTTP layered on top
of TLS (Transport Layer Security) to provide encryption, authentication,
and data integrity.
Working Steps:
1. Client Hello: Browser sends supported cipher suites and TLS version.
2. Server Hello: Server responds with chosen cipher and its digital certificate.
3. Key Exchange: Client verifies certificate and generates a session key.
4. Encrypted Session: Data between browser and server is encrypted using
symmetric encryption.
c. Discuss the limitations and challenges of sender policy framework.   5
Answer:
Marking Scheme: 1 mark each for five limitations
• DNS lookup limitations: SPF specification restricts servers to 10 DNS
lookups to resolve an SPF record, preventing DoS attacks.
CO- 2;   • Character limitations: SPF records have a 255-character limit for a
BL-2   single string, similar to DNS TXT records.
• Incomplete solution: SPF does not offer complete end-to-end encryption
or protection against phishing attacks using lookalike domains.
•   Difficulty in maintaining SPF records: Complex email infrastructures
and additional email servers can complicate SPF record maintenance.
• Breakable via improper email forwarding: Emails forwarded through
unauthorized servers can fail SPF authentication.
d. Discuss the main steps involved in this secure query process from user input 5
to result decryption.
Answer:
Marking Scheme: 1 mark per correct step (5 steps total)
CO-3 ;
BL-2   1. User creates a plaintext query on client side.
2. Client-side processor encrypts/encodes the query using client-held keys
and metadata.
3. Encrypted query is transmitted to cloud server.
4. Cloud executes query over encrypted data and returns encrypted results.
********** 2 **********
--- page 3 ---
5. Client decrypts results locally to obtain plaintext output.
a. Discuss any four active attacks with an example.
Answer:
Marking Scheme: 2.5 marks per attack: definition + example
1. Masquerade Attack:
o An attacker pretends to be a legitimate user to gain unauthorized
access.
o Example: Logging into a system using stolen credentials.
2. Replay Attack:
Q2
o Valid data transmissions are maliciously repeated or delayed.
CO-1;   [10]
o Example: Re-sending a valid payment request to duplicate a
BL-3
transaction.
3. Modification of Messages:
o Alteration of data in transit without detection.
o Example: Changing transfer amounts in a banking transaction
packet.
4. Denial of Service (DoS) Attack:
o Overwhelms system resources, making services unavailable.
o Example: Flooding a web server with SYN packets.
b. The university allows students to bring personal devices for accessing e-
learning resources. However, IT must ensure these devices don’t
compromise network integrity. Suggest a NAC policy for verifying the
compliance of personal devices before granting access. Explain how role-
based access control (RBAC) can be integrated with NAC to segregate
student and faculty access levels.
Answer:
CO-1;
Marking Scheme: 5 marks NAC policy details, 5 marks RBAC-NAC   [10]
BL-2
integration explanation
• NAC Policy for BYOD Compliance:
o Enforce device registration and authentication via 802.1X.
o Perform pre-admission checks for OS patch level, antivirus, and
encryption.
********** 3 **********
--- page 4 ---
o Non-compliant devices are redirected to a remediation VLAN.
o Continuous   post-admission   monitoring   ensures   policy
compliance.
• RBAC Integration with NAC:
o Roles are assigned based on user identity and device compliance.
o Students: Granted access only to e-learning portals and Wi-Fi.
o Faculty: Granted additional access to lab systems or administrative
resources.
o NAC dynamically enforces VLAN assignment or ACLs based on
user role.
Example:
A student’s tablet failing antivirus check is quarantined, while a faculty laptop
passes compliance and is mapped to a higher-access VLAN.
a. Discuss the working EAP-GPSK mechanism with a diagram and benefits of
using EAP-GPSK.
Answer:
Marking Scheme: 5 marks working & diagram, 5 marks benefits/use-cases
Working:
1. EAP-GPSK (Extensible Authentication Protocol–Generic Pre-Shared
Key) uses a shared secret key between client and server.
2. Mutual authentication occurs through message exchanges using nonce
values.
3. Both parties derive session keys for encryption and integrity
protection.
Q3
CO-1;   [10]
BL-2
Benefits:
•   Lightweight – suitable for IoT and embedded devices.
• Does not require digital certificates.
•   Provides mutual authentication and key derivation.
********** 4 **********
--- page 5 ---
•   Resistant to dictionary attacks due to nonce-based exchange.
b. Discuss man-in-the-middle (MitM) attacks affect wireless access points,
and what measures can be taken to mitigate them.
Answer:
Marking Scheme: 5 marks MitM effects/examples, 5 marks mitigations
• MitM Attack Explanation:
• An attacker positions themselves between client and access point (AP)
to intercept or alter communications.
CO-1;   • Example: A rogue AP mimics a legitimate Wi-Fi network name to
[10]
BL-2   capture login credentials.
• Countermeasures:
1. Use WPA3 or 802.1X authentication with digital certificates.
2. Enable mutual authentication to verify both client and AP.
3. Implement HTTPS and VPNs for end-to-end encryption.
4. Use Wireless Intrusion Detection Systems (WIDS) to detect rogue
APs.
5. Disable automatic Wi-Fi connections and verify SSIDs manually.
a. Explain the role of public and private keys in the TLS encryption process. [10]
How does asymmetric encryption transition to symmetric encryption during
data transmission?
Answer:
Marking Scheme: Public/Private key explanation – 3 marks, Asymmetric to
symmetric transition – 4 marks, Example and clarity – 3 marks
• Public and Private Keys in TLS:
o TLS uses asymmetric encryption during the handshake phase to
securely exchange session keys.
o The server sends its public key (inside its digital certificate) to
Q4
the client.
CO-2;
o The client uses this public key to encrypt a randomly generated
BL-2
session key.
o Only the server’s private key can decrypt this session key,
ensuring confidentiality.
• Transition to Symmetric Encryption:
o Once both sides share the session key, the connection switches to
symmetric encryption (e.g., AES).
o Symmetric keys are much faster for bulk data transfer and ensure
confidentiality during communication.
• Example:
o In HTTPS, TLS first uses RSA or Diffie–Hellman for key
exchange, then uses AES-128/256 for data encryption.
********** 5 **********
--- page 6 ---
b. A company’s legal team uses PGP for signing and encrypting contracts sent [10]
to clients. However, a recipient reports that the message signature could not
be verified. Apply your understanding of PGP’s digital signature
mechanism to identify possible reasons for this issue. Suggest steps to re-
establish secure, verifiable communication using key management and
signature verification.
Answer:
Marking Scheme: Reasons for verification failure – 5 marks, Corrective
steps and explanation – 5 marks
•   Possible Reasons:
1. The sender’s public key used for signature verification is missing
or expired.
CO-2;
2. The message was modified after being signed.
BL-3
3. The sender’s keypair has been revoked or replaced.
4. Key ID mismatch between the message and the keyring.
5. Incorrect trust level assigned to the sender’s key in the
recipient’s PGP client.
• Steps to Re-establish Secure Communication:
1. The sender should publish or resend their updated public key
via a trusted key server.
2. The recipient should import and verify the new key’s fingerprint
through an out-of-band method (e.g., phone verification).
3. Both parties should refresh their keyrings and confirm that keys
are not revoked.
4. Re-sign and re-encrypt the message using verified keys.
a. A government agency’s DNS infrastructure is upgraded with DNSSEC. [10]
Q5
Explain how DNSSEC adds authentication and integrity to traditional DNS
CO-2;
queries. Describe the purpose of RRSIG, DNSKEY, and DS records in
BL-2
validating DNS responses.
********** 6 **********
--- page 7 ---
Answer:
Marking Scheme: DNSSEC purpose & working – 4 marks, Explanation of
records – 6 marks
• DNSSEC Overview:
o DNSSEC (Domain Name System Security Extensions) ensures
that DNS data has not been tampered with and comes from a
legitimate source.
o   It adds digital signatures to DNS records, allowing resolvers to
validate authenticity.
• Key Records:
o RRSIG (Resource Record Signature):
▪   Contains the digital signature of DNS records created
using the zone’s private key.
▪   Validates data integrity.
o DNSKEY:
▪ Holds the public key used to verify the RRSIG signature.
▪ Ensures the authenticity of the zone.
o DS (Delegation Signer):
▪ Links a child zone’s DNSKEY to its parent zone, forming
a chain of trust from the root to the domain.
Example:
When a resolver requests “gov.in,” it verifies the RRSIG using the DNSKEY
and checks the DS record in the parent zone to ensure authenticity.
b. During a cybersecurity audit, an organization’s VPN connections are found [10]
to lack proper key management, making them vulnerable to replay attacks.
The security team decides to implement Internet Key Exchange (IKE) with
IPSec. Explain how the IKE protocol establishes and manages Security
Associations (SAs) in IPSec. Describe how these SAs contribute to secure
key exchange and protection from replay or impersonation attacks.
Answer:
Marking Scheme: IKE phase explanation – 4 marks, SA management – 3
marks, Replay protection – 3 marks
CO-2;   • IKE and SA Establishment:
BL-2   o IKE (Internet Key Exchange) operates in two phases:
1. Phase 1: Establishes an IKE SA using Diffie–Hellman
key exchange, authenticating peers and setting up a secure
channel.
2. Phase 2: Creates multiple IPSec SAs for data encryption
and integrity (ESP or AH).
•   Security Associations (SAs):
o Define the parameters for encryption, authentication, and key
lifetimes.
o Each SA is unidirectional, ensuring data confidentiality and
integrity per direction.
• Replay & Impersonation Protection:
********** 7 **********
--- page 8 ---
o Sequence numbers and anti-replay windows detect and block
duplicate packets.
o IKE authentication (digital signatures or PSKs) prevents
impersonation.
a. An educational institution uses a Software as a Service (SaaS) platform for [10]
online examinations. Students report issues with fake emails redirecting
them to phishing websites resembling the cloud portal. Explain why cloud-
based services are susceptible to phishing and spoofing attacks. Describe
how digital certificates and multi-layer authentication can protect users
from such threats.
Answer:
Marking Scheme: Cloud phishing risk – 5 marks, Security countermeasures
– 5 marks
• Why Cloud Services Are Vulnerable:
Q6
o Cloud-based systems are accessible globally, making URL
CO-3;
spoofing and fake login pages easy to host.
BL-2
o Attackers mimic legitimate SaaS portals to steal credentials.
• Countermeasures:
o Digital Certificates (HTTPS/TLS): Authenticate genuine portals
and prevent man-in-the-middle attacks.
o Multi-layer Authentication: Use MFA or token-based systems
for user verification.
o Email Filtering: Block phishing domains using DMARC and
SPF.
o User Awareness: Train users to identify fake links and phishing
attempts.
b. Explain the concept of packet capturing in network monitoring. Describe [10]
any three techniques used for packet capturing and explain how each method
helps in analyzing network performance.
Answer:
Marking Scheme: 3 marks- Concept of packet capturing, 6 marks -
Explanation of three techniques, 1 mark -Clarity and relevance to network
performance
•   Concept   of   Packet   Capturing:
CO-3;   Packet capturing is the process of intercepting and recording data packets
BL-2   traveling across a network. It allows network administrators and cybersecurity
professionals to analyze the flow of traffic, detect anomalies, troubleshoot
issues, and verify security protocols. Tools like Wireshark, tcpdump, and
SolarWinds are commonly used for this purpose.
• Techniques for Packet Capturing:
1. Port Mirroring (SPAN):
o The switch duplicates all traffic from one or more ports to a
designated monitoring port.
o This allows administrators to capture packets without disrupting
network operations.
********** 8 **********
--- page 9 ---
o Use: Helpful for analyzing traffic between servers and detecting
congestion or packet loss.
2. Network TAP (Test Access Point):
o A physical device inserted between two network nodes to copy
all data passing through.
o Unlike SPAN, TAPs work independently of switches and
guarantee full packet capture.
o Use: Common in high-security environments to capture raw,
unaltered data for forensic analysis.
3. Software-Based Capture:
o Packet sniffers like Wireshark or tcpdump run directly on
endpoints or network gateways.
o They capture packets in real time for protocol analysis and
troubleshooting.
o Use: Ideal for identifying application-layer issues or verifying
encrypted session setup.
a. During a cybersecurity lab, students capture HTTPS packets using [10]
Wireshark and observe Client Hello, Server Hello, and Certificate messages.
Interpret the purpose of each message in the TLS handshake.
Explain how these exchanges establish a secure session between client and
server. Summarize how symmetric keys are derived for secure data
transmission.
Answer:
Marking Scheme: 4 marks message purposes, 4 marks session
establishment, 2 marks key derivation
• Purpose of Each Message:
1. Client Hello:
o Sent by the client to initiate the TLS handshake.
o Includes supported protocol versions, cipher suites, and a
random number (Client Random).
2. Server Hello:
Q7   o Server responds with its chosen protocol, cipher suite, and
CO-3;   another random number (Server Random).
BL-2,4   o These random values help in session key generation.
3. Certificate:
o The server sends its digital certificate, which contains its
public key and identity.
o The client verifies this certificate using a trusted Certificate
Authority (CA).
Establishing a Secure Session:
• Once the client verifies the server’s identity, it generates a pre-master
secret, encrypts it with the server’s public key, and sends it to the
server.
• Both sides then use this secret, along with Client and Server Random
values, to derive the same session keys.
•   After this exchange, encryption shifts to symmetric mode for faster
data transfer.
Symmetric Key Derivation:
• The pre-master secret is input into a pseudo-random function (PRF)
along with random values to generate session keys.
********** 9 **********
--- page 10 ---
• These keys are used for data encryption (AES) and message
integrity (HMAC) during transmission.
b. Explain any five threats in mobile device with an example.   [10]
Answer:
Marking Scheme: 2 marks per threat + example
Answer:
1. Lack of Physical Security: Mobile devices are easily lost or stolen.
Attackers could access stored data or use the device to connect to
organizational resources.
2. Untrusted Mobile Devices: Employees often use their own
CO-3;   smartphones/tablets. These devices may not follow company
BL-2   security standards, making them risky.
3. Untrusted Networks: On-campus, devices connect through secure
Wi-Fi. Off-campus, public Wi-Fi or cellular networks can be unsafe,
exposing data to eavesdropping or man-in-the-middle attacks.
4. Untrusted Applications: Mobile devices allow quick installation of
third-party apps. Malicious apps can steal data or install malware.
5. Interaction with Other Systems: Devices often auto-sync with
laptops or cloud storage. This may spread malware or store data in
unsecured locations.
********** 10 **********
````
