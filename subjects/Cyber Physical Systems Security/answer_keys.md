# Cyber Physical Systems Security: answer keys

Answer keys and model answers published on the portal, newest first.

## 2024-25 · Final-Exam · Sem 12 · Answer key · paper eff6a9283ce2

- Departments: Electronics and Telecommunication
- Programmes: BTech (ELECTRONICS & TELECOMMUNICATION
- Source: `02_Question_Papers/2024/Sem_12/Final-Exam/BTech (ELECTRONICS & TELECOMMUNICATION _e9090790/Cyber Physical Systems Security/ANS_Cyber Physical Systems Security(702IT0E030)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2025
- Text: text (6 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING) SIX YEARS INTEGRATED PROGRAM
Year: VI/Semester XII(Exam Year: 2024-2025)
Subject: Cyber Physical Systems Security
Date: 02 May 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data whenever required
5. Q.1 is compulsory
Q1   a) Explain different attack detection mechanisms employed in Cyber-Physical Systems   [20]
Attack detection mechanisms in Cyber-Physical Systems (CPS) operate across multiple layers to
identify malicious activities and anomalous behaviors. The primary mechanisms include:
Signature-based detection monitors network traffic and system operations for known attack patterns or
signatures. While efficient for recognized threats, it struggles with zero-day attacks and requires
constant signature updates.
Anomaly-based detection establishes baselines of normal system behavior and flags deviations. This
approach is particularly effective in CPS environments where physical processes follow predictable
patterns, enabling the detection of subtle changes in sensor readings or actuator commands that might
indicate an attack.
Specification-based detection leverages formal models and specifications of the CPS to identify
violations of expected behavior. This method bridges the gap between signature and anomaly detection
by focusing on violations of system rules rather than just deviations from normal patterns.
Physics-based detection utilizes knowledge of the physical processes being controlled to identify
attacks that violate physical laws or constraints. For example, detecting sensor readings that show
impossible physical states or unrealistic rates of change.
Hybrid approaches combine multiple detection mechanisms to overcome limitations of individual
methods. These often incorporate machine learning techniques to improve detection accuracy and
reduce false positives.
b) Analyze the challenges in implementing secure key distribution in large-scale CPS
Implementing secure key distribution in large-scale Cyber-Physical Systems presents several
significant challenges:
Resource constraints limit the computational capabilities of many CPS devices, making traditional
public key cryptography impractical. Lightweight alternatives often compromise security for
efficiency, creating potential vulnerabilities.
Network heterogeneity in CPS environments involves diverse communication protocols and hardware
platforms, making standardized key distribution difficult. Systems must accommodate various security
capabilities across different components and legacy subsystems.
Scale and distribution problems arise as CPS deployments often span wide geographical areas with
thousands of nodes. Key management becomes exponentially more complex, particularly when devices
are deployed in physically insecure or inaccessible locations.
Long operational lifetimes of CPS components (often 10-20 years) exceed the secure lifespan of
cryptographic keys and algorithms. Key rotation and algorithm updates must occur without disrupting
critical operations, requiring sophisticated transition mechanisms.
Physical security concerns emerge as attackers may gain physical access to devices, risking key
extraction. Tamper-resistant hardware and physical unclonable functions (PUFs) help mitigate these
risks but add cost and complexity.
c) Discuss the security implications of connecting legacy Industrial Control Systems to modern
networks
Connecting legacy Industrial Control Systems (ICS) to modern networks introduces profound security
implications:
********** 1 **********
--- page 2 ---
Inherent security weaknesses exist in legacy ICS, which were designed with availability and safety as
priorities rather than security. These systems often lack basic security controls like authentication,
encryption, and access control, operating under the assumption of air-gapped isolation.
Lack of security updates is common as many legacy components run outdated or unsupported operating
systems and software that vendors no longer patch. This creates persistent vulnerabilities that cannot be
remediated without system replacement.
Protocol vulnerabilities arise as legacy industrial protocols (like Modbus, DNP3, and PROFIBUS) were
designed without security features. When exposed to modern networks, these plaintext communications
become vulnerable to eavesdropping, replay attacks, and manipulation.
Increased attack surface emerges when previously isolated systems connect to corporate networks or
the internet. Each new connection point represents a potential entry for attackers, dramatically
expanding the attack surface beyond what the systems were designed to withstand.
Operational technology/information technology (OT/IT) convergence challenges create conflict
between IT security practices and OT operational requirements. Security measures common in IT
environments (like regular patching or rebooting) may disrupt critical industrial processes.
d) Compare and contrast Cyber-Physical Systems, Internet of Things (IoT)
Cyber-Physical Systems (CPS) and Internet of Things (IoT) represent overlapping but distinct
technological paradigms:
Purpose and focus: CPS primarily integrate computational and physical processes to monitor and
control physical entities through feedback loops, with emphasis on real-time control and safety-critical
operations. IoT focuses more on connecting everyday objects to the internet for data collection, remote
monitoring, and convenience services.
Timing requirements: CPS typically have strict real-time constraints and deterministic behavior
requirements, as they often control critical infrastructure or industrial processes where timing is
crucial. IoT systems generally have more relaxed timing requirements and can often tolerate delays or
occasional disconnections.
Autonomy and intelligence: CPS incorporate sophisticated control algorithms and often operate
autonomously with minimal human intervention, making complex decisions based on physical system
states. IoT devices typically focus on data collection and transmission to cloud services, with advanced
processing occurring in the cloud rather than at the edge.
Security implications: CPS security breaches can directly impact physical world safety, potentially
causing physical damage, environmental hazards, or endangering human lives. IoT security breaches
primarily affect data privacy and information security, though this boundary is blurring as IoT extends
into critical domains.
Scale and architecture: CPS architectures are often tightly integrated, customized systems with a focus
on closed-loop control. IoT deployments tend toward highly distributed, heterogeneous networks of
simpler devices using standardized communications and cloud platforms.
Despite these differences, the boundaries between CPS and IoT are increasingly blurring as IoT
technologies are adopted in industrial and critical infrastructure settings, creating Industrial IoT (IIoT)
as a hybrid domain that incorporates elements of both paradigms.
Q.2   a) Explain the role of feedback loops in Cyber-Physical Systems   [20]
Feedback loops are fundamental to Cyber-Physical Systems (CPS), serving as the core mechanism that
enables intelligent interaction between computational and physical components. Their primary roles
include:
Control and automation: Feedback loops enable CPS to continuously monitor physical processes
through sensors, process this data computationally, and adjust physical parameters via actuators. This
creates a self-regulating system that maintains desired states despite external disturbances.
System stability: By constantly comparing actual system states with desired states, feedback loops help
maintain system stability and performance within operational parameters. Negative feedback
mechanisms are particularly important in dampening oscillations and preventing runaway conditions.
Adaptation to changing conditions: Feedback mechanisms allow CPS to adapt to environmental
changes or varying operational conditions without human intervention. Advanced CPS may implement
adaptive control algorithms that modify their response based on observed system behavior.
Error detection and correction: Feedback loops facilitate the identification of anomalies by comparing
expected and actual system behavior. This capability is crucial for both operational reliability and
security monitoring.
Learning and optimization: In advanced CPS, feedback data provides the foundation for machine
learning algorithms to optimize system performance over time, improving efficiency and effectiveness
through experience.
b) Discuss the challenges in implementing security measures in resource-constrained CPS
environments
Implementing security in resource-constrained CPS environments presents several significant
challenges:
********** 2 **********
--- page 3 ---
Computational limitations: Many CPS devices operate with minimal processing power, memory, and
energy resources. This restricts the use of traditional security mechanisms like strong encryption,
complex authentication schemes, or intensive intrusion detection systems.
Real-time requirements: Security measures introduce computational overhead that can conflict with the
strict timing constraints of many CPS applications. Delays in processing caused by security operations
may compromise system functionality and safety.
Battery and energy constraints: For battery-powered or energy-harvesting CPS devices, security
operations must be extremely energy-efficient. Each cryptographic operation consumes power, creating
a direct trade-off between security strength and operational longevity.
Limited communication bandwidth: Many CPS networks operate with restricted bandwidth, making
security protocols with significant overhead impractical. This often forces compromises in security
design.
Legacy integration issues: Security solutions must often integrate with existing legacy components that
weren't designed with security in mind, requiring careful adaptation of security measures to avoid
disrupting critical operations.
Physical accessibility concerns: Many CPS devices are deployed in physically accessible locations,
making them vulnerable to tampering. Implementing physical security mechanisms adds further
resource requirements.
Q.3   a) Explain the concept of lightweight cryptography in the context of Cyber-Physical Systems   [20]
Lightweight cryptography refers to cryptographic algorithms and implementations specifically
designed for resource-constrained environments common in Cyber-Physical Systems:
Optimized resource usage: Lightweight cryptographic solutions minimize computational complexity,
memory requirements, and energy consumption while maintaining an acceptable security level. This
often involves streamlined algorithms with smaller key sizes, simpler operations, and reduced rounds.
Hardware-friendly design: Many lightweight cryptographic primitives are designed for efficient
hardware implementation, using operations that map well to simple logic circuits and can be
implemented with minimal gate count.
Balanced security trade-offs: These approaches accept certain security compromises to achieve
practical deployability, offering "right-sized" security that defends against realistic threat models rather
than theoretical maximum security.
Standardization efforts: Organizations like NIST have initiated dedicated programs to standardize
lightweight cryptographic algorithms for constrained environments, recognizing the distinct needs of
CPS and IoT applications.
Application-specific optimization: Lightweight cryptography often tailors solutions to specific use
cases, such as authenticated encryption for sensor data or efficient key exchange protocols for device
commissioning.
Examples: Notable lightweight cryptographic primitives include PRESENT, SIMON, SPECK, and
Ascon for encryption; and lightweight hash functions like PHOTON and SPONGENT. These provide
security guarantees with significantly reduced resource requirements compared to traditional
algorithms like AES or SHA-3.
b) Analyze the following attacks on Industrial Control Systems: Stuxnet, Ukraine Power Grid Attack
Stuxnet (discovered 2010)
Stuxnet represented a watershed moment in ICS security as the first documented cyber-physical attack
specifically targeting industrial infrastructure:
Attack characteristics: This highly sophisticated malware targeted Siemens SCADA systems
controlling uranium enrichment centrifuges in Iran. It propagated through multiple vectors including
USB drives to bridge air-gapped networks.
Technical sophistication: Stuxnet utilized an unprecedented four zero-day vulnerabilities and stolen
digital certificates for legitimacy. Its modular design included PLC rootkits that modified Siemens
Step7 software to alter centrifuge speeds while displaying normal readings to operators.
Physical impact: The attack caused physical damage to centrifuges by repeatedly changing rotor speeds
while masking these changes from monitoring systems, demonstrating how digital attacks could cause
tangible physical destruction.
Attribution and significance: Widely attributed to state-sponsored actors (reportedly US and Israel),
Stuxnet demonstrated the reality of cyber-physical attacks against critical infrastructure and ushered in
a new era of ICS security awareness.
Ukraine Power Grid Attack (2015/2016)
The attacks on Ukraine's power distribution companies demonstrated a coordinated cyber assault on
critical infrastructure with direct public impact:
Attack methodology: Attackers gained initial access through spear-phishing emails containing
BlackEnergy malware, established persistence, conducted reconnaissance, and ultimately executed a
coordinated attack that remotely triggered circuit breakers at multiple substations.
********** 3 **********
--- page 4 ---
Sophistication elements: The attackers demonstrated domain knowledge of industrial control systems,
developed custom firmware to disable protective relays, and coordinated a telephone denial-of-service
attack against customer service centers to prevent customers from reporting outages.
Impact and scale: The 2015 attack affected approximately 230,000 customers for up to 6 hours in the
middle of winter. The 2016 follow-up attack targeted a transmission-level substation with more
sophisticated techniques including the Industroyer/CrashOverride malware specifically designed to
target power grid operations.
Attribution and significance: Generally attributed to Russian state-sponsored actors, these attacks
demonstrated the feasibility of disrupting critical infrastructure on a regional scale and revealed the
vulnerability of power grids to coordinated cyber attacks. They highlighted the geopolitical dimension
of cyber-physical attacks and their potential use in hybrid warfare scenarios.
Q.4   a) Analyze the use of Software Defined Networks in securing Cyber-Physical Systems   [20]
Software Defined Networks (SDN) offer significant security advantages for Cyber-Physical Systems
through:
Network visibility and control: SDN's separation of control and data planes provides comprehensive
visibility across the entire CPS network, enabling security administrators to monitor traffic patterns and
detect anomalies more effectively than in traditional network architectures.
Dynamic security policy enforcement: The programmable nature of SDN allows for real-time, network-
wide security policy implementation and adaptation. Security rules can be instantly deployed across all
network devices from a centralized controller in response to emerging threats.
Network segmentation and isolation: SDN facilitates granular microsegmentation of CPS networks,
creating secure zones that isolate critical control systems from potentially compromised sections, thus
limiting lateral movement by attackers and containing security breaches.
Traffic inspection and filtering: SDN can dynamically redirect suspicious traffic to security appliances
like intrusion detection systems without disrupting the network topology, enabling more thorough
inspection without performance degradation.
Rapid threat response: Upon detecting attacks, SDN controllers can automatically reconfigure network
paths, quarantine compromised devices, or implement security countermeasures across the entire CPS
infrastructure in seconds rather than hours or days.
b) Discuss the security implications of Bring Your Own Device (BYOD) policies
BYOD policies introduce several significant security implications for organizations:
Expanded attack surface: Personal devices typically have varying security postures and patch levels,
creating numerous potential entry points for attackers to exploit. The diversity of operating systems and
configurations complicates uniform security enforcement.
Data leakage risks: Corporate data stored on personal devices may be exposed through consumer
applications, cloud backups, or when devices are shared with family members. Data boundaries
become blurred, increasing the risk of inadvertent information disclosure.
Limited visibility and control: Organizations have restricted ability to monitor, manage, and secure
personal devices compared to corporate-owned assets. This creates blind spots in security monitoring
and incident response capabilities.
Malware propagation concerns: Infected personal devices can serve as vectors to introduce malware
into corporate networks, potentially compromising critical systems upon connection. Consumer
behavior on personal devices often involves higher-risk activities than on work-dedicated devices.
Compliance challenges: Personal devices accessing regulated data may create compliance violations if
they don't meet required security standards. This is particularly problematic in industries with strict
regulatory requirements like healthcare, finance, or critical infrastructure.
Q.5   a) Discuss the technical requirements for real-time operation in Cyber-Physical Systems   [20]
Real-time operation in Cyber-Physical Systems demands specific technical requirements to ensure
reliable and predictable performance:
Deterministic timing: CPS must guarantee consistent response times with bounded latency to ensure
physical processes are controlled within strict temporal constraints. This often requires specialized
real-time operating systems that provide deterministic scheduling.
High reliability and fault tolerance: Real-time CPS must maintain operational integrity even during
partial system failures. This necessitates redundant components, fail-safe mechanisms, and graceful
degradation capabilities to prevent catastrophic failures.
Low-latency communication: Communication protocols must prioritize minimal and predictable delays
over high throughput. Industrial protocols like EtherCAT, PROFINET RT, or Time-Sensitive
Networking (TSN) provide guaranteed message delivery within time constraints.
Precise synchronization: Distributed CPS components require precise time synchronization (often sub-
millisecond) across the system. Protocols like IEEE 1588 Precision Time Protocol enable the tight
coordination necessary for distributed control actions.
********** 4 **********
--- page 5 ---
Resource adequacy: Computing resources must be sufficient to handle worst-case processing scenarios
within timing constraints, not just average cases. This often requires careful hardware dimensioning
and resource reservation techniques.
b) Analyze the privacy implications of data collection and processing in Cyber-Physical Systems
Data collection and processing in Cyber-Physical Systems raise significant privacy concerns:
Pervasive surveillance capabilities: CPS often incorporate extensive sensor networks that can collect
data beyond their intended operational purposes. Smart buildings, industrial systems, and urban
infrastructure can inadvertently enable continuous monitoring of individual behavior and movement
patterns.
Unintended information disclosure: Data collected for operational purposes may reveal sensitive
information when analyzed. For example, smart grid power consumption data can reveal occupancy
patterns, lifestyle details, and even specific activities within homes or facilities.
Data fusion and re-identification risks: When CPS data is combined with other datasets, seemingly
anonymous operational data can lead to identification of individuals. The richness of sensor data often
enables inference of personal information even when direct identifiers are removed.
Inadequate consent mechanisms: Many CPS environments (public spaces, workplaces, infrastructure)
offer limited or no practical means for individuals to opt out of data collection. Users often lack
awareness of what data is being gathered and how it might be used.
Regulatory compliance challenges: The global patchwork of privacy regulations creates complex
compliance requirements for CPS that may operate across jurisdictional boundaries. Design choices
must address varying requirements for data minimization, purpose limitation, and individual rights.
Q.6   a) Cyber-Physical System Defense Layers Analysis   [20]
A Cyber-Physical System (CPS) integrates computational elements with physical processes, typically
involving sensors, actuators, and control systems that interact with the physical world.
For the defense layer calculations:
Processing time for each layer path:
Layer 1 only: 2ms (detection)
Layers 1+2: 5ms (2ms detection + 3ms analysis)
Layers 1+2+3: 10ms (2ms detection + 3ms analysis + 5ms response)
Number of attacks per path:
Layer 1: 60 attacks (60%)
Layer 2: 30 attacks (30%)
Layer 3: 10 attacks (10%)
Total processing time:
= (60 × 2ms) + (30 × 5ms) + (10 × 10ms)
= 120ms + 150ms + 100ms
= 370ms
Average response time:
= Total time ÷ Total attacks
= 370ms ÷ 100
= 3.7ms
b) Smart Grid Anomaly Detection
For the hourly power consumption readings {2.3, 2.5, 8.9, 2.4, 2.6, 2.2} kWh:
Mean calculation:
= (2.3 + 2.5 + 8.9 + 2.4 + 2.6 + 2.2) ÷ 6
= 20.9 ÷ 6
= 3.48 kWh
Standard deviation calculation:
Calculate variance: Σ(x - mean)² ÷ (n-1)
Standard deviation = √variance
Calculated value = 2.66 kWh
Anomaly detection using 2σ rule:
********** 5 **********
--- page 6 ---
Lower threshold = mean - 2σ = 3.48 - 2(2.66) = -1.84 kWh
Upper threshold = mean + 2σ = 3.48 + 2(2.66) = 8.80 kWh
Any reading outside this range is anomalous
The reading 8.9 kWh exceeds the upper threshold, indicating an anomaly
Therefore, the 8.9 kWh reading is identified as anomalous, potentially indicating unauthorized usage or
a system malfunction.
Q7   a) Encryption is a process of converting information into a code to prevent unauthorized access,   [20]
ensuring that only intended recipients with the proper decryption key can access the original
information.
For the key storage calculations:
Given information:
1,000 devices in the CPS network
Each device requires a unique pair of public and private keys
Key size is 256 bits for both keys
Storage calculation for private keys:
Converting bits to bytes: 256 bits = 32 bytes (8 bits = 1 byte)
Total bytes for 1,000 private keys = 1,000 × 32 bytes = 32,000 bytes
Converting to megabytes: 32,000 bytes ÷ 1,048,576 bytes/MB = 0.0305 MB
Storage calculation for public keys:
Since public keys are also 256 bits (32 bytes) each
Total bytes for 1,000 public keys = 1,000 × 32 bytes = 32,000 bytes
Converting to megabytes: 32,000 bytes ÷ 1,048,576 bytes/MB = 0.0305 MB
Therefore, the storage required is 0.0305 MB for all private keys and 0.0305 MB for all public keys.
b) Threshold Cryptography Scheme
For the threshold cryptography problem:
Given information:
5 nodes with security weights: {0.7, 0.7, 0.9, 0.8, 0.6}
Threshold scheme requires any 3 nodes for key reconstruction
Minimum acceptable security threshold is 0.7
Calculate minimum security threshold:
The security threshold for a combination is the product of the individual node security weights
For 3-node combinations, we need to calculate this product for all possible combinations. Students
should write-down all possible combinations
********** 6 **********
````
