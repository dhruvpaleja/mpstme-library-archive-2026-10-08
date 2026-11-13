# IoT and Applications: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 3b4fe8693120

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIDS_7056/IoT and Applications/ANS_IoT and Applications(702CO0E017)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: IoT and Applications
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Q1 is compulsory
5. Answer any four of the remaining questions
6. Assume Suitable data if necessary.
7. In all 5 questions to be answered.
Q1   Answer Briefly
CO1-   a Explain the major challenges related to security in IoT.   [5]
SO1-
1 X 5 = 5M – 1M for each challenge with short description.
BL2
Energy Consumption, heterogeneity, security, reliability, Standardization,
regulatory compliance. Any 5 challenges to be considered.
CO3-   b How do security frameworks help in ensuring data integrity and privacy in   [5]
SO3-   IoT?
BL3
1M for each point mentioned to ensure data integrity and privacy.
Security frameworks help ensure data integrity and privacy in IoT by providing
structured guidelines and mechanisms:
• Encryption: Protects data during transmission and storage from
unauthorized access.
• Authentication & Authorization: Ensures only legitimate devices and
users can access the system.
• Data Integrity Checks: Uses hashing and digital signatures to detect
tampering.
• Secure Communication Protocols: (e.g., TLS, HTTPS) prevent
interception and attacks.
• Access Control Policies: Restrict who can view or modify sensitive data.
********** 1 **********
--- page 2 ---
CO4-   c Explain the IoT prototyping methods.   [5]
SO4-
1M for brief of each prototyping method.
BL1
IoT Prototyping Methods -
• Rapid Prototyping: Quickly build basic models using boards like
Arduino/ESP32 to test ideas.
• Proof of Concept (PoC): Demonstrates that the idea works technically.
•   Iterative Prototyping: Continuously improve the prototype based on testing
and feedback.
• Hardware-in-the-Loop (HIL): Combines real hardware with simulated
environments.
• Simulation-based Prototyping: Uses software tools to test system behavior
before hardware implementation.
CO4-   d Explain the role of cloud platforms in IoT.   [5]
SO4-   Any 5 of the below mentioned points 1M for each point.
BL2   Role of Cloud Platforms in IoT :
• Data Storage: Stores large volumes of sensor data securely.
• Data Processing & Analytics: Analyzes real-time and historical data for
insights.
• Device Management: Monitors, updates, and controls IoT devices remotely.
•   Scalability: Easily handles increasing number of devices and data.
•   Security: Provides authentication, encryption, and access control.
•   Integration: Connects IoT data with applications, dashboards, and other
services.
Q2   a A metropolitan city deploys an IoT-based traffic monitoring system with thousands [10]
CO1-   of cameras, vehicle counters, and pollution sensors installed at intersections. The
SO1-   system generates high-frequency streaming data every second. Some data such as
real-time traffic congestion alerts must be processed immediately to control traffic
BL5
signals, while historical data is analyzed weekly to identify long-term congestion
patterns. The city also wants to store video data for only 7 days due to storage
constraints, but keep aggregated traffic statistics for several years.
•   Identify the types of IoT data generated in this system.
• Suggest suitable IoT data management techniques to handle real-time and
historical data.
• Recommend an appropriate IoT storage model and justify your choice.
• Explain how data lifecycle management should be implemented in this scenario.
2M – types of data generated (video, image, event data like alerts, real time data
like pollution levels from sensors, aggregated data or historical data)
2M – IoT data management technique (Real time in edge, batch processing in
cloud, filtering and processing in cloud)
3M – Data storage model with proper justification
Hybrid storage model (Edge + Cloud):
• Edge storage: For real-time decision-making (low latency).
********** 2 **********
--- page 3 ---
• Cloud storage: For large-scale storage and analytics.
Ensures fast response for critical tasks and scalable long-term storage for
analysis.
3M – Data Lifecycle management
• Data collection: Sensors continuously generate data.
• Data processing: Real-time (instant alerts) + batch (weekly analysis).
• Data retention policy:
o Video data stored for 7 days only.
o Aggregated data stored for years.
• Data deletion: Automatic removal of expired video data.
• Data archiving: Store summarized data for long-term insights.
CO2-   b Explain the key features of 6LowPan protocol and give the packet format used for   [10]
SO2-   transmission.
BL1
6M for Key features + 4M Packet format
1. Header Compression
Reduces IPv6 header from 40 bytes to a few bytes.
2. Fragmentation
Splits large IPv6 packets into smaller frames.
3. Mesh Addressing
Supports multi-hop communication.
4. Stateless Address Autoconfiguration - 6LoWPAN supports automatic IPv6
address assignment.
Packet Format:
A 6LoWPAN packet includes:
 Dispatch header
 Compression header
 Fragmentation header (if needed)
 Payload
Dispatch Header - Identifies packet type:
 IPv6 packet
 Compressed packet
 Fragmented packet
Q3   a Explain the IoT reference architecture with a neat diagram.   [10]
CO3-
5M for Figure + 5M for explanation
SO3-
Layers in IoT Reference Architecture:
BL2
1. Perception Layer (Device Layer) – Sensors and actuators that collect data
from the environment.
2. Network Layer (Connectivity Layer) – Transfers data using
communication technologies (Wi-Fi, Zigbee, etc.).
3. Processing Layer (Middleware Layer) – Data processing, storage, and
analytics (often cloud/edge).
4. Application Layer – Provides services to users (smart traffic, healthcare,
smart homes).
********** 3 **********
--- page 4 ---
5. Business Layer – Manages overall system, policies, analytics, and decision-
making.
CO4-   b A company that manufactures elevators installs IoT sensors in all its elevators to [10]
SO4-   monitor vibration, usage frequency, and component wear. Instead of selling elevators
BL5   outright, the company charges building owners based on uptime and number of
elevator trips per month. The company is responsible for maintenance and
performance.
1. Identify the IoT business model used in this scenario.
2. Explain how IoT data enables this business model.
3. What advantages does this model provide to both the company and the
customers?
2M – Identify business model, 3M – IoT data assists the business model
5M – advantages of this model to both consumer and the company
Business Model - Product-as-a-Service (PaaS) / Usage based billing
• Real-time monitoring: Sensors track vibration, usage, and wear continuously.
• Predictive maintenance: Detects faults early and prevents breakdowns.
• Usage-based billing: Counts number of trips and uptime accurately.
• Performance tracking: Ensures service-level agreements (SLAs) are met.
For the Company:
• Continuous revenue (subscription/usage-based)
•   Better maintenance planning → reduced costs
• Improved product performance insights
For Customers:
• No high upfront cost
•   Reliable service with minimal downtime
• Pay only for actual usage
Q4   a Describe the term resource management. Elaborate techniques of resource [10]
CO1-   partitioning and resource discovery used in resource management.
SO1-
2M – Resource management definition
BL2
4M – Resource Partitioning 4M- Resource discovery
Discovering and identifying all available resources, partition them to maximize
utility function. In terms of cost, energy and performance and finally schedule the
tasks with the available resources.
Resource Partitioning in IoT
•   Definition: Dividing available resources (CPU, memory, bandwidth, storage)
among multiple IoT devices/tasks.
• Purpose: Ensures efficient utilization and avoids resource conflicts.
• Techniques:
o Virtualization and containerization
o Task scheduling and load balancing
•   Benefit: Improves performance, scalability, and reliability of IoT systems.
Resource Discovery in IoT
•   Definition: Process of identifying and locating available IoT devices and services
in a network.
********** 4 **********
--- page 5 ---
• Methods:
o Directory-based discovery
o Broadcast/Multicast methods
o Service discovery protocols (e.g., mDNS, CoAP)
• Purpose: Enables devices to find and communicate with each other dynamically.
•   Benefit: Supports interoperability and dynamic integration of IoT components.
CO4-   b A municipality installs IoT-enabled smart bins that monitor garbage levels and send
SO4-   alerts when they are full. Waste collection trucks are automatically routed to only
BL5   those bins that require collection.
1. Explain how IoT improves operational efficiency in this scenario.
2. Identify the IoT devices, communication technologies, and data management
strategies involved.
3. What challenges may arise when deploying this system across an entire city?
4M – IoT for operational efficiency, 4M – devices and communication technology
2M – challenges
• Real-time monitoring: Bins send alerts only when full → avoids unnecessary
trips
• Optimized routing: Trucks visit only required locations → saves fuel & time
• Reduced operational cost: Less manpower and better resource utilization
• Improved cleanliness: Prevents overflow and maintains hygiene
Devices:
• Smart bins with ultrasonic sensors (to detect fill level)
• GPS modules in trucks
•   Microcontrollers (e.g., Arduino/ESP32)
Communication Technologies:
• Low-power networks like LoRaWAN, NB-IoT, Zigbee
•   Internet connectivity via gateways/cloud
Data Management Strategies:
• Real-time data processing for alerts
• Cloud storage for monitoring and analytics
• Data aggregation to optimize routes
Challenges – any 2
• Network connectivity issues in remote or dense areas
• High initial cost of sensors and infrastructure
• Maintenance of devices (battery, damage, faults)
• Data security and privacy concerns
•   Scalability issues with large number of bins
• Integration with existing waste management systems
Q5   a Explain the key issues in traditional networks and how SDN would overcome the [10]
CO1-   problems.
SO1-
4M Key issues 2M – SDN 4 M – overcome the problems by SDN
BL2
Problems in Traditional Networks
********** 5 **********
--- page 6 ---
•   Tight coupling of control & data plane
• Manual configuration
• Poor scalability
• Vendor lock-in
Tight Coupling of Control & Data Plane → Decoupling in SDN
SDN separates the control plane (decision-making) from the data plane (packet
forwarding).
A centralized SDN controller manages the network, making it more flexible and
programmable.
Manual Configuration → Automated & Programmable Network
SDN uses APIs and software-based control to automate configuration. Reduces
human errors and enables quick network changes.
Poor Scalability → Centralized & Scalable Management
SDN controllers provide a global view of the network, allowing easy scaling.
New devices and policies can be added dynamically without complexity.
Vendor Lock-in → Open Standards & Interoperability
SDN supports open protocols (like OpenFlow), enabling multi-vendor environments.
CO2-   b Explain why MQTT is widely used in IoT systems with constrained devices and [10]
SO2-   networks.
BL3
3M for listing + 7M for explanation
• Lightweight Protocol: Minimal header size → low bandwidth usage, ideal
for low-power devices.
• Publish–Subscribe Model: Devices don’t communicate directly; a broker
handles messages → reduces complexity and network load.
• Low Power Consumption: Efficient communication → extends battery life
of IoT devices.
• Reliable Delivery: Supports QoS levels (0, 1, 2) → ensures message delivery
as needed.
• Works on Unreliable Networks: Handles intermittent connectivity with
features like message buffering and retained messages.
•   Scalability: Easily supports large number of devices via broker-based
architecture.
• Security Support: Can use TLS/SSL for secure communication.
Q6   a Identify the reliability issues in a smart health care system used for patient   [5]
CO1-   monitoring and provide solutions for the same.
SO1-   3M for issues + 2M for solutions
BL5   • Sensor failures / inaccurate readings
• Network connectivity issues (data loss, delay)
• Power/battery failure of devices
• Data loss or corruption
********** 6 **********
--- page 7 ---
• Latency in critical alerts
• Device malfunction or hardware faults
•   Security breaches affecting data reliability
Solutions - <any 2>
• Redundancy: Use multiple sensors/devices to cross-verify data
• Regular calibration & maintenance: Ensure accuracy of sensors
• Reliable communication protocols: Use MQTT/CoAP with QoS support
• Edge computing: Process critical data locally for faster response
• Backup power: Batteries/UPS for uninterrupted operation
• Data validation & error checking: Use checksums, hashing
• Low-latency alert systems: Priority handling for emergency data
• Strong security measures: Encryption, authentication to prevent tampering
CO3-   b Explain NIST security framework used in internet of things.   [5]
SO3-
1M Usage of NIST + 4M functions
BL1
NIST Framework helps organizations identify, prevent, detect, respond, and
recover from cybersecurity threats effectively.
Core Functions of NIST Framework
1. Identify - Understand assets, risks, and vulnerabilities
2. Protect- Implement safeguards (access control, encryption)
3. Detect- Identify security incidents quickly
4. Respond- Take action to contain and mitigate threats
5. Recover- Restore systems and improve after incidents
CO2-   c Explain the working of Routing Protocol for Low-Power and Lossy Networks   [10]
SO2-   (RPL) and highlight the types of communication and message types.
BL2
5M RPL working + 5M communication and message types.
• Root node starts the network.
• DIO message broadcast
• Nodes join DODAG
• Parent selection
• Upward routing
• DAO message for downward routing
Message   Full Form   Purpose
DODAG
DIO   Information   Builds routing structure
Object
Destination
Downward
DAO   Advertisement
routes
Object
********** 7 **********
--- page 8 ---
DODAG
DIS   Information   Requests routing info
Solicitation
Traffic Type   Description
Upward   Node → Root (sensor data upload)
Downward   Root → Node (control commands)
Point-to-Point   Node → Node communication
Q7   a A smart parking system uses IoT sensors installed in parking slots to detect vehicle   [10]
CO3-   presence. The sensors send data to a gateway, which then transmits it to the cloud.
SO3-   Hackers intercept the communication and modify the parking availability data
before it reaches the cloud. Which layer of the IoT security framework should be
BL6
strengthened to prevent this attack? Suggest appropriate security mechanism.
2M – Identify the security issue. 3M – Layer identification with justification 5M
Appropriate security mechanism.
Network / Communication Layer- The attack occurs during data transmission
(interception & modification) between sensors, gateway, and cloud. Appropriate
Security Mechanisms
• Encryption (TLS/SSL):
Protects data in transit so attackers cannot read or modify it.
• Message Integrity Checks: Use hashing / MAC (Message Authentication
Code) to detect tampering.
•   Authentication: Ensure only trusted devices communicate (mutual
authentication).
• Secure Protocols: Use secure versions like MQTTS / HTTPS / CoAP with
DTLS.
•   Digital Signatures: Verify that data has not been altered and comes from a
valid source.
CO4-   b Discuss the role of IoT in transforming traditional environments into smart   [10]
SO3-   environments.
BL3
2 X 5M = 10 M – Identify any 5 five with proper description
• Real-time Monitoring: Sensors continuously collect data (temperature, traffic,
energy use) → enables live tracking of conditions.
• Automation & Control: Devices can automatically respond (e.g., smart lights,
traffic signals) → reduces human intervention.
• Data-driven Decision Making: Collected data is analyzed to improve
efficiency and planning.
• Resource Optimization: Efficient use of energy, water, and infrastructure →
reduces waste and cost.
********** 8 **********
--- page 9 ---
• Remote Access & Control: Systems can be monitored and controlled from
anywhere via cloud/mobile apps.
• Predictive Maintenance: Detects faults early → avoids breakdowns and
improves reliability.
• Improved Quality of Life: Enhances convenience, safety, and comfort (smart
homes, healthcare, smart cities).
********** 9 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper a2b241870f23

- Departments: Computer Engineering, Data Science
- Programmes: BTech Computer 7002, BTech CSE DS 7057, Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSE_DS_7057/IoT and Applications/ANS_IoT and Applications(702CO0E017)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 25 Nov 2025
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech Intg. (CE)
Year: IV / VI/Semester VII/Semester XI(Exam Year: 2025-2026)
Subject: IoT and Applications
Date: 25 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q.1
1. Asset & fleet management: GPS and RFID track where assets are and what condition they’re
in from raw materials to finished goods and vehicles—reducing loss and improving dispatch.
2. Remote monitoring & control: Real-time monitoring of machines and sites allows quick
adjustments and faster fixes.
3. Quality assurance: Optical inspection and other sensors spot defects early, improving yield and
a.   cutting rework.
4. Production line monitoring: Live data shows bottlenecks and helps streamline workflows and
boost throughput.
5. Route optimization: Data from connected vehicles and sensors improves delivery routes,
lowering fuel use and delays.   5M
b.
********** 1 **********

[Text in pictures on this page, read by OCR]
Application Layer (CoAP)

Defined by Transport Layer (UDP)

Internet

pores Network Layer
(IPv6/ICMP/RPL)

Adaptation Layer (6LoWPAN)

ee | Link Layer (802.15.4 )
802.15.4
standard |

Physical Layer(802.15.4)
--- page 2 ---
Diagram 2M and Explanation 3M
1. Identify the value proposition: Define the concrete benefit your IoT solution delivers so
business goals align with real user needs.
2. Know your customer segments: Pinpoint the users or industries that gain the most; analyze
their pains, budgets, and buying process.
3. Define revenue streams: Choose models that fit the use case—subscription, pay-per-use,
outcome-based, or data monetization.
4. Set key resources and partnerships: Line up hardware makers, cloud providers, connectivity
partners, and analytics vendors.
c.   5. Build the cost structure: Estimate device BOM, connectivity, cloud/storage, security,
maintenance, and support.
6. Design delivery and support: Pick channels, onboarding, SLAs, and after-sales support to drive
retention.
7. Secure data and privacy: Enforce strong data handling, governance, and compliance across the
stack.
8. Continuously improve: Track performance, gather market feedback, and adjust the model as
technology and customer needs evolve.   5M
1. Sensors and nodes
2. Local processing
3. Connectivity and transmission
4. Cloud storage and analytics
5. Scheduling and routing
6. Alerts and automation
7. User interface and reporting
d.   8. Security and maintenance   3M
********** 2 **********

[Text in pictures on this page, read by OCR]
ULTRASONIC =}___})

DC MOTOR
SENSOR 1
ULTRASONIC
SENSOR 1 ESP8266
ARDUINO UNO
IR -—
SENSOR2 7

MOISTURE

Ne Z

SENSOR3
--- page 3 ---
2M
Q.2
2M
SDN separates a network’s control plane from its data plane so devices can be managed centrally in
software. The controller (control plane) decides how to route and secure traffic; switches and routers
(data plane) forward the packets accordingly. For IoT, this centralized, programmable model makes it
easier to scale, enforce policies, and secure large, mixed fleets of devices.   1M
a.
Aspect   Control Plane   Data Plane
Decides how traffic should be routed; holds Forwards packets according to the
Function
the network’s decision logic.   control plane’s instructions.
Centralized software controller (in SDN) that Physical or virtual devices switches,
Components
manages the whole network.   routers that move the data.
“Smart” layer: makes routing and policy “Forwarding”   layer:   executes
Intelligence
decisions.   commands; minimal built-in logic.
Traditional: bundled inside each device.
SDN   vs.   Both models: forwarding is performed
SDN: separated and moved to a central
Traditional   by the network devices themselves.
controller.
3M
Importance of SDN in IoT.
1. Centralized management: One controller configures and monitors the entire IoT network,
simplifying setup, changes, and troubleshooting across thousands of devices.
2. Enhanced security: Global visibility enables consistent policies, rapid threat response, and
actions like isolating nodes or dropping suspicious flows.
3. Flexibility and agility: Programmatic updates let you adapt routing, QoS, and access rules on
the fly as devices and apps change.
********** 3 **********

[Text in pictures on this page, read by OCR]
Software Defined Networking (SDN)

t Applications t

Control Plane [ SDN Controller |

SDN Datapath |

Data Plane [ Switches }

a

Pool of Application Servers
--- page 4 ---
4. Resource optimization: The controller allocates bandwidth and paths based on application
needs, improving performance and efficiency at scale.   4M
Key factors for IoT privacy: strong authentication and access control, end-to-end encryption (in transit
and at rest), regular updates and patching, segmented network design, and clear privacy notices so users
know how data is used. Addressing these protects sensitive data from unauthorized access, changes, and
misuse.   2M
•   Strong authentication: Use robust MFA or biometrics to verify users and devices.
•   Access controls: Enforce least-privilege, policy-based access to data and resources.
•   Encryption: Protect data on the wire and at rest with modern ciphers.
• Data management: Define how data is collected, stored, processed, shared, and deleted;
maintain integrity and confidentiality across its lifecycle.
• Network segmentation: Isolate IoT devices from critical systems to contain breaches.
b.   •   Secure communication: Use up-to-date, authenticated protocols between devices, gateways,
and cloud.
•   Device provisioning: Harden onboarding so new devices aren’t compromised at setup.
•   Secure firmware: Enable secure boot and verify firmware integrity before execution.
• Regular updates: Keep firmware/software current to close known flaws.
• Patch management: Apply security patches promptly as vulnerabilities emerge.
•   Clear privacy policies: State what you collect, why, and with whom it’s shared, in plain
language.
• User control: Let users view, export, and delete their data where possible.
•   Monitoring: Watch for anomalies and suspicious behavior in real time.
• Response tools: Automate detection and containment to shorten time to remediate.   8M
Q.3
A   temperature   sensor   (publisher) sends   readings   to a broker under a   topic   like
home/livingroom/temperature. Any client (subscriber)—e.g., a light controller or smart switch—
subscribes to that topic and receives updates the broker forwards. Core actions: connect →
publish/subscribe.
a.
Components
• MQTT client: Any device using an MQTT library; here, the sensor publishes and the controllers
subscribe.
•   Publisher: The temperature sensor sending data.
•   Subscriber: The light controller and smart switch receiving data.
********** 4 **********
--- page 5 ---
• MQTT broker: Central server that routes publisher messages to matching subscribers.
• MQTT   topic:   Hierarchical   label   used   to   categorize   messages   (e.g.,
home/livingroom/temperature).
• MQTT connection: TCP/IP session between client and broker enabling message exchange.
Diagram 2M and Explanation 5M
Common risks include weak auth, unencrypted traffic, and unpatched firmware. Mitigate with strong
authentication and encryption, timely updates, network segmentation, and tight device/data
management.   1M
Security threats in IoT
• Weak authentication/authorization (default or weak passwords, lax access controls)
•   Insecure data transmission (no encryption between devices and servers)
•   Software/firmware vulnerabilities ripe for exploits
•   Flat networks that let one breach spread laterally
• Malware and botnets (ransomware, DDoS)
b.   •   Physical tampering leading to theft or damage
•   Poor device management at fleet scale (tracking, monitoring, updates)   3M
Requirements for securing IoT
•   Strong authentication and authorization (MFA, least privilege)
•   End-to-end encryption (in transit and at rest)
•   Regular patching and updates across the fleet
•   Secure device lifecycle management (onboarding to decommission)
•   Secure development practices (threat modeling, code review, SBOM)   3M
Descriptive analytics: Summarizes past data to show what happened and highlight patterns/trends.
Diagnostic analytics: Explains why it happened by probing correlations, drivers, and root causes.
Predictive analytics: Uses statistical/ML models to forecast likely outcomes or trends.
c.   Prescriptive analytics: Recommends actions by pairing predictions with optimization or simulation.
Real-time analytics: Analyzes streaming data as it arrives for instant insight and anomaly detection.
Edge analytics: Processes data on devices or gateways to cut latency and bandwidth—vital at IoT scale.
6M
Q.4
********** 5 **********
--- page 6 ---
Explanation
1. System blueprint: Sensors at junctions, corridors, and vehicles capture counts, speed, occupancy,
and violations (cameras/RFID).
2. Data acquisition: Edge gateways clean, time-stamp, and compress streams, then forward relevant
events to cloud.
3. Cloud analytics: ML models predict congestion and optimize signal plans; stream processing
supports real-time alerts.
4. Control & feedback: Optimized timings and route advisories push to signals and VMS; effects
are measured and fed back.
5. User interface: Web/mobile views show live traffic, incidents, and best routes for drivers and
a.   authorities.
6. Network: Mixed 4G/5G/LPWAN links ensure low-latency, reliable connectivity between
roadside and cloud.
Challenges
•   Privacy: Continuous location/plate data needs anonymization, access controls, and retention
limits.
•   Connectivity: Dense urban RF, outages, or bandwidth caps can delay telemetry and control
signals.
•   Data management & security: High-volume streams require scalable storage and strong security
to prevent breaches or unauthorized control.
Diagram 3 + Explanation 4 + Challenges 3 = 10M
********** 6 **********
--- page 7 ---
b.
Diagram 4M Explanation 6M
Q.5
•   Asset-sharing: Multiple users share an IoT-enabled asset. Profits rise with high utilization and
shared upkeep; sustainable through resource efficiency and lower ownership costs.
•   Razor-blade: Core device priced low; margins come from consumables or connected services.
Highly profitable with steady repeat sales; sustainable if demand and support stay strong.
•   Pay-per-usage: Customers pay only for what they use. Profit hinges on usage frequency and
lean delivery; sustainable with accurate metering and fair billing.
•   Additional services: Premium add-ons (analytics, remote maintenance) atop the base offer.
Profits grow with clear differentiation; sustainability needs ongoing innovation and
a.
engagement.
• Data monetisation: Insights sold or used for targeted services. Can be very profitable if done
ethically; sustainability depends on privacy, compliance, and user trust.
• Outcome-based: Payment tied to results. Aligns revenue with customer success; profitability
needs reliable measurement, and shared risk boosts long-term viability.
•   Subscription: Recurring fees for continuous access. Predictable cash flow and strong lifetime
value; sustainable if quality and satisfaction remain high.   7M
b.
********** 7 **********

[Text in pictures on this page, read by OCR]
e loT architecture

Gateway |~ [| ———

Cloud _____ Control
oe gateway applications Models
* +

1} f

Sensors, actuators aa ED

and smart devices a x
Streaming (S"] Machine

data processor “learning

s. Data lake ———+ °
ensors, actuators Big dat
and smart devices ss Prat

warehouse

Web Data
application analytics

p——— User business

logic
Mobile
application
Device ee User Security

administration administration monitoring
--- page 8 ---
Basis   CoAP   MQTT
Message   Queuing   Telemetry
Abbreviation   Constrained Application Protocol
Transport
Communication
Request–response (client/server)   Publish–subscribe (via broker)
type
Supports synchronous-style requests and
Messaging mode   Asynchronous messaging
asynchronous notifications (e.g., Observe)
Primarily TCP (with TLS for
Transport protocol Primarily UDP (often with DTLS for security)
security)
2-byte fixed header (plus variable
Header size (min.) 4 bytes
header/payload)
Yes—REST-like   methods
RESTful   No—topic-based, not REST
(GET/POST/PUT/DELETE) and URIs
Session   persistence,   retained
No   built-in   session   persistence
Persistence/session   messages,   and QoS   states
(caching/proxying possible)
supported
Packet Identifiers for QoS flows;
Message   ID &   Token   fields   for
Message labeling   no app-level labeling like CoAP
deduplication/correlation
Tokens
Broad IoT telemetry; secured with
Typical use/security Utility/LLN devices; secured with DTLS
TLS
Effectiveness in   Lower—TCP overhead can be
High—small, UDP-based, low overhead
LLNs   heavier on constrained links
Communication   Many-to-many   via a   central
One-to-one (client ↔ server)
model   broker
Correct Differences 7M
Issue   Solutions
Build in security from day one: end-to-end encryption, strong auth, Privacy-
Security & privacy
by-Design. Run regular audits, intrusion detection, and secure OTA updates.
Interoperability &   Use open platforms and standardized APIs/protocols. Align vendors and
standards   stakeholders on common profiles to ensure devices talk to each other.
Mix networks (5G, LPWAN, satellite) for coverage and resilience. Add edge
Connectivity
processing to cut bandwidth and latency.
Scalability &   Start small and scale in phases. Use cloud management for centralized
c.
management   monitoring, config, and fleet control.
Plan CAPEX and OPEX; prioritize high-impact wins. Roll out in phases to
Cost
spread spend and validate ROI.
Choose low-power hardware, aggressive sleep cycles, and efficient firmware;
Power management
consider solar or energy harvesting.
Data management & Apply tiered storage and compression. Use real-time analytics and
analytics   automation to turn streams into actionable insight.
6M
********** 8 **********
--- page 9 ---
Q.6
IoT traits that raise security and privacy risks
Limited resources, massive connectivity, device diversity, and constant data collection make strong
protection hard. Weak protocols, slow patching, and fragile networks leave devices open to attacks and
leaks. On privacy, accountability is messy and transparency is thin—users often don’t know who collects
data, how it’s used, or how it’s protected.   2M
Characteristics leading to security & privacy challenges
•   Limited resources: Constrained CPU/RAM hinder strong encryption and defenses.
•   Connectivity & scale: Huge fleets and wide networks expand the attack surface.
•   Device diversity: Mixed OSes, protocols, and vendor practices resist uniform policy and
updates.
•   Insecure communication: Wireless traffic is exposed if not properly encrypted and
a.
authenticated.
• Data collection: Large volumes, often sensitive, raise concerns over storage, sharing, and use.
4M
Accountability and transparency in IoT systems
•   Accountability: Someone must be responsible for protection and compliance, but the chain—
manufacturer, developer, service provider, user makes fault hard to assign (e.g., weak device
design vs. poor passwords vs. lax network security).
• Transparency: Users need clear, accessible explanations of what’s collected, who sees it, and
retention. Many products don’t disclose full scope (e.g., voice-command data: storage location,
access, and duration remain unclear).   4M
********** 9 **********
--- page 10 ---
b.
Diagram with Explanation   6M
key characteristics of the Thread protocol
•   Security: AES-128 encryption and built-in authentication so only authorized devices join and
data stays protected.
c.   •   Reliability: Self-healing mesh removes single points of failure; traffic reroutes if a node drops.
• Power efficiency: Optimized sleep/idle behavior lets devices run for years on small batteries.
•   Scalability: Supports hundreds of nodes fit for large homes and building automation.
4M
Q.7
An IoT-based Smart Agriculture System can be designed to monitor environmental parameters and
automate irrigation to optimize water use and crop growth.
• System architecture: Sensor nodes feed a microcontroller over short runs; the controller processes
readings locally, drives a relay/pump, and forwards data to the cloud for monitoring and control.
a.   • Components used: Soil-moisture probes; DHT11/DHT22 for temperature/humidity; Arduino or
ESP32; relay module for pump/valves; Wi-Fi or GSM (or LPWAN) for backhaul.
• Data flow: Sensors stream values; the controller compares moisture against crop-specific thresholds.
If below set point, it energizes the relay to start irrigation; hysteresis prevents rapid cycling.
********** 10 **********

[Text in pictures on this page, read by OCR]
A Historic Timeline of Internet of Things

ado us
& “Be 0gv
The The The First Official loT Devices
Beginning First Entry of Internet Exceed 20

of TCP/IP Webpage of Things Billion"

The First loT is Coined Mirai Botnet
loT Device for the Almost Brings
First Time Down the Internet

&
--- page 11 ---
 Cloud & UI: Platforms like ThingSpeak/Blynk store and visualize trends, send alerts, and
expose a manual override so farmers can start/stop irrigation from a phone or browser.
• Control logic: Thresholds can incorporate weather forecasts or time-of-day windows; run-
time limits and flow feedback guard against leaks or dry-runs.
• Advantages: Cuts water use, reduces manual effort, and supports precision farming—keeping
soil in the ideal range to lift yield and sustainability.
Diagram 4M Explanation 6M
Challenges moving from prototype to full-scale
a. Scalability: Test rigs rarely handle production loads, more devices, data, and stricter
uptime/QoS.
b. Hardware limits: Dev boards (e.g., Arduino) aren’t built for industrial duty cycles, temperature
ranges, or EMC/ingress standards.
b.
c. Integration: Multiple devices, protocols, and data platforms at scale expose interoperability gaps
and brittle interfaces.
d. Security & privacy: Prototypes prioritize function; production needs hardened auth, encryption,
secure boot, OTA, and compliance.
e. Cost & manufacturing: Redesign for BOM cost, reliability, certifications, and testability before
volume build.
********** 11 **********
--- page 12 ---
Prototyping accelerates learning, but success at scale demands deliberate work on capacity, integration,
and security so the product is both robust and commercially viable.   6M
c.
Diagram 2M Explanation 2M
********** 12 **********

[Text in pictures on this page, read by OCR]
Send HTTP Request
(GET, POST, PUT, DELETE)

»
>

® Client (https://api.example.com/resource) ae Server

Gin
Receive JSON Response Cee

<

(eg: {"name": “archana", "age": "40"})
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 178e32e0b502

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSE_DS_7057/IoT and Applications/ANS_IoT and Applications(702CO0E017)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (16 pages)
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. TECH (CSE - DS)/B. Tech Intg. (CE)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: IoT and Applications
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary.
Q.1
Internet of things (IoT) is a collection of physical items wired with sensors, software, and
other technologies, which communicate and share information on the internet.   1M
Characteristics of IoT
Connectivity: This is the enabling feature, enabling devices to interact with each other, as
well as a central system, through the use of the internet or other standards of connectivity.
Scalability: IoT systems are meant to expand and scale to support a huge and continuously
growing number of devices.
Heterogeneity: IoT network devices are heterogeneous and differ in terms of their hardware
and software, as well as the communication protocols employed.
Dynamic and Self-Adapting: Devices may be added and removed to the network
a. dynamically, and the system is capable of adjusting to the environmental and network
changes.
Sensing: IoT devices have the functionalities of sensors to sense the physical environment.
Intelligence: Systems can analyze data and decide, and in most cases, involve machine
learning or artificial intelligence to do so.
Security: An essential feature that entails privacy and safety of data and guarding gadgets
against computer attacks.
Interoperability: This is the capability of devices manufactured by other manufacturers to
interact and co-exist.
Real-time Data Processing: It is the possibility to work with data in real-time, receiving the
results immediately and reacting to them in time.
********** 1 **********
--- page 2 ---
Self-Configuring/Self-Organizing: The devices may automatically configure themselves and
become part of the network without the need to do this manually in a large extent.   4M
b.
1M
RPL (Routing Protocols Low-Power Lossy Networks) involves the use of a few control
messages to define and ultimately maintain a network topology, whose primary messages are
DIO, DIS, DAO and DAO-ACK. The broadcast messages include DIO (DODAG Information
Object) informing the network, DIS (DODAG Information Solicitation) requesting a new
node to find out network information, DAO (Destination Advertisement Object) requesting a
new node to join a DODAG and DAO-ACK (acknowledgment) to the DAO request.   4M
Wire-framing is part way complete: Wire-framing by doing it correctly will leave a
substantially smaller number of things amiss in the User Interface, and the hardware design.
Content Hierarchy and Organization: In case of designing the IoT, ensure that there is
organization of content and content Hierarchy in a manner that makes it USP.
User feedback and reinforcing: Feedback of the users can also give some good information
regarding the hardware and the software design and what needs improvement.
c. Contrast: Contrast assists the User Interface in defining the content/visual hierarchy, which
puts emphasis on a focal point and imparts visual interest.
Alignment and Proximity: Alignment is flow of elements and Proximity is proximity of the
elements.
Repetition: Repetition is simply the number of times patterns, graphics or any other property
is repeated on the UI to present user with an easy to navigate application.
The implementation of these practices leads to effective, safe and versatile IoT system. 5M
•   Install air sensor of PM 2.5, PM 10, CO, NO2, and ozone and water sensor of pH,
turbidity, dissolved oxygen and conductivity.
• Connect sensor to microcontrollers or edge nodes which processes sensor data.
d.   • Send data to a central server by using proper connectivity like Wi Wi, cellular,
LoRaWAN or NB IoT.
•   Store incoming data in a time series database on cloud or edge server to quickly
retrieve the information.
********** 2 **********
--- page 3 ---
• Real time analytics- monitor threshold violations and Longer term analytics- monitor
trends and sources.
•   Offer a dashboard and mobile notifications to authorities and citizens to get live
readings and notice.
• Use security, data validation and periodic sensor calibration as a measure that reliable
and trusted measurements will be guaranteed.   4M
1M
Q.2
M2M communication is a subdivision of IoT, which deals with direct, more point to point,
communication between a few devices over a special network, whereas IoT is a more general
term which relies on the internet to link a huge, diverse variety of devices to the cloud to
analyze data and scale along with integration between different systems. IoT expands M2M
by extending the network past closed systems to operate over IP-based protocols to provide
internet access to the network, which are capable of the following features: cloud-based
processing of data, wider interoperability, and scalability that are not typical of M2M.
Basis   IoT   M2M
Abbreviation   Internet of Things   Machine to Machine
Devices have objects that are   Some degree of intelligence is
Intelligence
responsible for decision making   observed in this.
Connection type   The connection is via Network and The connection is a point to
used   using various communication types. point
Traditional protocols and
a. Communication   Internet protocols are used such as
communication technology
protocol used   HTTP, FTP, and Telnet.
techniques are used
Data is shared between other
Data is shared with only the
Data Sharing   applications that are used to improve
communicating parties.
the end-user experience.
Internet connection is required for   Devices are not dependent on
Internet
communication   the Internet.
Type of   It supports point-to-point
It supports cloud communication
Communication   communication.
Involves the usage of both Hardware Mostly hardware-based
Computer System
and Software.   technology
A large number of devices yet scope
Scope   Limited Scope for devices.
is large.
Business 2 Business(B2B) and
Business Type used   Business 2 Business (B2B)
Business 2 Consumer(B2C)
********** 3 **********
--- page 4 ---
There is no support for Open
Open API support Supports Open API integrations.
APIs
It requires   Generic commodity devices.   Specialized device solutions.
Communication and device
Centric   Information and service centric
centric.
Vertical system solution
Approach used   Horizontal enabler approach
approach .
Devices/sensors, connectivity, data   Device, area networks,
Components
processing, user interface   gateway, Application server.
Smart wearables, Big Data and   Sensors, Data and Information,
Examples
Cloud, etc.   etc.
Any Correct 6 Differences 6M
IoT networks are based on and extend M2M abilities by increasing its narrow, point-to-point
communication to a vast, internet-based environment. Although M2M is specifically
dedicated to data exchanges between machines when it comes to direct data exchange, IoT is
combined with cloud platforms, enhanced data analytics, and open APIs in order to enable
more extensive applications, increased scaling, and enhanced intelligence.
Global connectivity and accessibility: M2M is actively limited to closed or private networks.
IoT has broken such boundaries because it operates internet protocols to establish a network
between gadgets worldwide and that allows one to monitor and control a device anywhere in
the world.
Advanced data analytics: M2M records fundamental data, whereas IoT uses cloud
computing and big data analytics to draw more profound information. This also allows
applications to be made such as predictive maintenance where equipment can predict its own
failure far beyond simple alerts.
Integration of complex ecosystems: M2M may be used to connect the sensors to a central
server, but IoT treats different devices and applications of different manufacturers and
applications as part of one ecosystem. This enables a smart thermostat in the home to
communicate with the security system, weather forecast, and user schedules at the same time.
Increasing interoperability: A lot of M2M systems are based on proprietary protocols which
do not allow a lot of interoperability. IoT fosters open standards and APIs and disparate
devices and systems can more readily communicate and collaborate with each other.   4M
Obfuscation enhancing the security of the IoT.
Makes code more difficult to understand: Obfuscation prevents the theft of intellectual
property and causes attackers to find it more challenging to alter the software to carry out
b. malicious code.
Obstructs the dynamic and static analysis: It complicates the task that attackers can analyze
the software code directly (static analysis) or through its execution (dynamic analysis).
Resists usual attacks: Obfuscation makes code more difficult to understand, and by raising
the cost and effort required to create exploits, discourages attackers, and methods such as
********** 4 **********
--- page 5 ---
metamorphic code generation can be employed in countering attacks such as Return-Oriented
Programming (ROP).   4M
The role of diversification in enhancing the security of IoT.
Eliminates mass exploitation: The distinctness of software instances in each device obviates
the vulnerability of one device suggesting that all devices are vulnerable.
Resists interface attacks It is capable of diversifying system interfaces, including system calls
and operating system libraries, making it far more difficult to use them to obtain access to
valuable resources.
Uses unique instances: It generates unique instances of software interfaces, a major way of
enhancing resilience without a significant rise in resource consumption, which is important in
resource-constrained IoT devices.
Fights monocultures: It targets the issue of software monoculture directly where billions of
devices run the same or similar software that forms one point of failure.   4M
How they work together
Layered defense:
The methods are not mutually exclusive and can be used together to other security tools,
including access control, firewalls and encryption and form a more effective security system.
Proactive security:
They are measures that are proactive, thus complicating the ability of an attacker to locate and
exploit vulnerabilities in the first place, instead of having to solely rely on reactive measures
such as intrusion detection.   2M
Q.3
The common style of architecture used to create IoT systems is the Representational State
Transfer (REST) because of its client-server architecture, statelessness, and the usage of
conventional HTTP methodology to provide easy and scalable communication. This is
suitable to the distributed nature of IoT, and enables devices and applications to communicate
a.
via APIs with one another sharing representations of resources (such as sensor data) identified
by URIs. The advantages of application to REST in IoT are that it is easily implemented,
scaled, and component-independent with such features as caching and layered systems to
enhance efficiency and security.
********** 5 **********
--- page 6 ---
2M
Significant concepts and how they are implemented in IoT.
Client-Server Architecture: REST decouples the client (e.g. a mobile app, a dashboard) and
the server (e.g. a device or a cloud service), which is central to the nature of the decentralized
IoT where devices and applications must be able to talk to one another.
Statelessness: A request made by a client should include all the data that the server requires
in order to interpret and act on it, without having to use any prior stored session data. This is
essential to IoT where devices can be resource constrained and network access can be
unreliable.
Uniform interface: REST is based on a uniform interface, which is usually the methods of
the HTTP protocol (GET, POST, PUT, and DELETE) and applied to resources.
GET: To access sensor data, e.g. the temperature of a device.
POST: To address an actuator, e.g., to switch on a light.
PUT: To change the status of a device.
DELETE: To destroy a device or information.
Resource Identification: Each resource (a device, a data point, a user account) has its own
Uniform Resource Identifier (URI).
Caching: REST facilitates caching to enhance performance and scalability through
minimizing the process of requesting the server several times on a single piece of data.
Layered System: The structure may be layered, with an intermediate such as a gateway,
proxies or firewalls able to add either functionality or security without any impact on the client
or server.
4M
Advantages for IoT
Scalability: Stateless client-server architecture can be scaled, which is critical in large
applications of IoT and potentially millions of devices.
Simplicity: REST is easy to implement and easy to understand using regular HTTP protocols
even when the developer is dealing with resource-constrained IoT devices and cloud
platforms.
Interoperability: The standard interface allows the various devices and applications to be
connected without the need to know how another system works.   1M
********** 6 **********
--- page 7 ---
An Internet of Things (IoT) structure is susceptible to various assaults at every of the layers:
Perception Layer, Network Layer and Transport Layer.
Perception layer attacks
The physical devices, sensors and actuators are found in the perception layer and they gather
information about the environment and interface with the physical world. Hacks of this layer
may alter sensor information or affect the physical security of the device.
Eavesdropping: An attacker can also intercept communication between the devices and
networks of the IoT, and steal sensitive information.
Node capture: An attacker is able to have complete control of a central point in the network,
such as sensor or a gateway. This may result in sensitive information being revealed like
cryptographic keys and communication details.
Malicious code injection: This is because an attacker can inject malicious code into the
compromised node. It may lead to unintended actions by the device or may give the attacker
the control of the complete system.
False node injection: An attacker inserts a fake or malicious node to the network in order to
inject false data, disrupt operations, or destroy the network.
Physical attacks: The attackers would be able to access a device and physically interfere with
some of its parts to get information, install unwanted, or even harm a device. This poses a
b.
great danger to the gadgets in unmonitored places.
Replay attacks: An attacker intercepts the communications and retransmits the authenticated
information to a target in order to become a trusted user or device.
Network layer attacks
The network layer conveys information of the perception layer to other layers using different
network protocols. Incomplete communication protocols and lack of encryption make this
layer an easy target by attackers.
Denial-of-Service (DoS): A DoS attacker sends a lot of traffic to the network, causing
legitimate users to be unable to access network resources. Devices with weak default
passwords in IoT can be easily compromised and could be easily used to create botnets of
large scale DDoS attacks.
Man-in-the-Middle (MitM) attacks: A man intercepts and modifies messages between two
devices without their knowledge that they are communicating directly to each other.
Routing attacks: In this type of attack, a rogue node has a chance to intentionally divert the
data stream.
Transport layer attacks
The transport layer provides a dependable network to transfer data between end systems, and
some protocols, such as TCP and UDP are used. Incidents of attacks to this layer are usually
associated with overwhelming the connection capacity to serve traffic.
********** 7 **********
--- page 8 ---
Flooding attacks: Flooding attacks are the most frequent transport layer attacks and they
consist of DoS. An attacker overloads the target device by sending requests in order to cripple
its resources and disrupt services.
TCP-SYN flooding: An attacker makes floods of TCP connection requests (SYN packets), but
does not follow through with the handshake. This puts the server in a situation where it has
numerous open unfinished connections.
UDP flooding An attacker overloads a device with UDP packets, using a vast amount of
resources and causing the device to become unresponsive.
Desynchronization attacks: An attacker sends packets in a sequence to dis-synchronize the
connection between a client and a server, which results in loss of valid data packets.
Reconnaissance attacks: This is a kind of attack that will be aimed at collecting as much
information as possible about a target system in order to locate its flaws. Examples are port
scanning to determine open ports and services.   7M
Resource management in IoT involves optimizing the use of limited resources like processing
power, bandwidth, and energy across a network of connected devices to ensure performance
and efficiency. Techniques include load balancing to distribute tasks evenly, scheduling to
manage task order and resource allocation, and resource discovery to find available services
and devices. This is crucial for a network's stability, cost-effectiveness, and user experience.
IoT resource management example.
Consider a smart city in which thousands of sensors control traffic, air quality, and transport.
To avoid cases of overloading and slowness of the system, resource management is necessary.
A data-hungry sensor (e.g. a high-resolution traffic camera) requires a lot of bandwidth.
c. Unless managed, it may take up the network and make other sensors (e.g. the ones transmitting
small air quality readings) slide.
•   Load balancing
Would make sure that when a single processing server on the cloud is occupied; another server
with less traffic is submitted.
•   Scheduling
Assign less urgent activities to time-sensitive ones, such as periodic system diagnostics, to
enable priority to more urgent ones, such as emergency traffic lights changes.
•   Resource discovery
Would enable new sensors to have automatic scanning and connect to the network
automatically.   6M
Q.4
Rural homes can be made cost-effective to automate and control appliances using affordable
a.
and locally controllable devices to create a cost-effective IoT solution.
********** 8 **********
--- page 9 ---
Hardware installation Hardware: microcontrollers like Arduino Uno or ESP32 with low
prices and simple sensors and relays to turn the lights on and off, the fans, and the pumps.
They are low power consuming and can be easily programmed.
Local connectivity Local Connectivity Local connectivity will allow appliance to
communicate with the central controller, instead of using constant internet connectivity, use
Bluetooth, Zigbee, or a local Wi-Fi network. This enables the users to control appliances
remotely in the house via a mobile application.
Edge gateway - Deploy a Raspberry Pi or ESP8266 to an edge controller in order to locally
process data and automate tasks. This removes the reliance on the cloud network and provides
real-time control.
Automation logic - Simple rule-based automation, which can be implemented include turning
on fans when the temperature rises, or water pumps when the soil is dry, or when the clock
strikes a particular time.
Power management - Use the solar power or battery backup systems as an insurance that the
power will be available in regions where there is unreliable power.
Cost-effectiveness – The suggested system will keep hardware and network expenditures to
a minimum, use less data, and be less expensive to maintain. It offers a cheap and secure smart
home system that can be used by rural households with limited access to the internet.
Reason as to why edge computing is required in enhancing the performance of home
automation systems:
Rapid response - Local processing enables data to be processed locally and control of the
appliances in real time.
Less reliance on the internet - Systems would not depend on the internet and can operate with
reduced or no Internet.
Better reliability- Local processing can be used to maintain operation when the network goes
offline.
Improved privacy of data - Sensitive data in the house is handled locally rather than in the
cloud.
Reduced bandwidth expense -Only necessary data is transmitted to the cloud and the use of
the internet and costs are minimized.
Energy efficiency- Optimized local processing reduces the energy used in associated devices.
Diagram 3 + Explanation 4 + Justification 3 = 10 M
********** 9 **********
--- page 10 ---
2M
IoT manages identity and authentication by issuing unique device identities—typically via
PKI and digital certificates and validating them over secure protocols like TLS. Persistent
hurdles include weak or default credentials, uneven standards, complex lifecycle
management, and securing varied networks and exposed APIs.   2M
How IoT performs identity management and authentication
b.
Digital identities: Devices receive a unique identity at manufacture, usually a certificate
under PKI, enabling the network to verify legitimacy.
TLS authentication: Transport Layer Security sets up an encrypted channel; during the TLS
handshake, device and server validate each other’s certificates before exchanging data.
Access control: After authentication, devices get scoped permissions to use specific
resources, ensuring only authorized devices can access data and controls.   3M
Challenges in IoT identity management and authentication
•   Inadequate authentication: Default, weak, or shared credentials invite brute-force
attacks.
• Lack of standardization: No uniform framework across vendors and protocols
hampers consistent security.
•   Lifecycle management: Provisioning, rotating, and retiring credentials at scale is
difficult.
•   Updates and patching: Remote or constrained devices often miss timely firmware
fixes, widening exposure.
********** 10 **********

[Text in pictures on this page, read by OCR]
Identity Management System

Block 2 Block 1 Block 0
Hash Hash Hash
Identity Identity Identity

Assign unique
ID toevery
device Validate devices sent
to blockchain

Authenticate 10,
Devices

IOT Devices

Smart Contract
--- page 11 ---
•   Heterogeneous networks: Wi-Fi, cellular, Bluetooth, and others pose different,
compounding security risks.   3M
Q.5
Platform model: Connects makers and users via interoperable products and services. Example:
Amazon Alexa collects intent data to surface and sell related products.
Subscription model: Delivers ongoing value for a recurring fee, building long-term relationships
and personalized services.
Pay-per-use model: Pricing tied to actual consumption. Examples: Mileage-based auto insurance;
Rolls-Royce charging airlines per engine flight hour.
Asset-sharing model: Multiple customers share equipment to cut costs; sensors log usage and
health. Examples: Zipcar; shared construction gear.
Asset-tracking model: Connected tags track location and condition in real time to prevent loss
and streamline logistics. Example: Sierra Wireless for cold-chain monitoring.
a. Outcome-based model: Customers pay for results, not ownership. Examples: Devices that auto-
reorder supplies; wearables alerting clinicians to changes.
Compliance model: Automated data capture and reporting reduce regulatory overhead. Example:
IBM platforms helping utilities meet reporting requirements.
Data-driven model: Device data is analyzed to deliver insights or sold (with consent) to third
parties. Example: Building energy monitors informing landlords and utilities.
Service-adjacent model: Value-add services around existing devices, such as predictive
maintenance contracts.
IoT expertise as a service: Specialist partners design, deploy, and maintain fleets. Examples:
Qualcomm and Cisco offering industry-specific support.
Any 7 7M
MQTT is a lightweight publish–subscribe protocol with three parts: a broker, clients, and topics.
Clients don’t talk to each other directly; they send messages to the broker, which delivers them to
subscribers of the relevant topic.
Components of MQTT
MQTT Broker:
•   Central server that receives client messages and routes them to subscribers of matching
b.   topics.
• Manages connections, authentication, and session state.
MQTT Clients:
• Any device/app using an MQTT library that connects to the broker.
• Can publish to topics, subscribe to topics, or do both at once.
MQTT Topics:
********** 11 **********
--- page 12 ---
•   String labels that organize messages (e.g., home/livingroom/temperature).
•   Hierarchical structure enables precise filtering so only interested subscribers receive a
given message.   5M
2M
Core IoT data challenges: volume/velocity, security/privacy, integration, scalability, and data
quality. Fast streams need strong storage and processing; protecting sensitive data and ensuring
authenticity enable trustworthy decisions.   1M
Data Volume and Velocity
Continuous, high-rate streams quickly outgrow conventional databases and pipelines.
Security and Privacy
Protect sensitive data in transit and at rest across devices and clouds.
c.
Integration and Compatibility
Unify heterogeneous vendors, sensors, and protocols without shared standards.
Scalability
Scale compute, storage, and throughput as fleets and data expand.
Data Quality and Governance
Maintain accuracy, provenance, and consistency from noisy sources for compliant analytics.
5M
Q.6
Essential security requirements
Strong authentication and access control: Use MFA and RBAC so only authorized users and
devices reach the network and its data.
a.
• Data protection: Blocks unauthorized access and tampering.
•   Device/network protection: Stops rogue devices from joining; limits actions to defined
roles.
********** 12 **********

[Text in pictures on this page, read by OCR]
MQTT Clients MQTT Clients

Ex: Sensors » Ex: Valve

Te Dic. te
mp"

Publish: "6596"
Topic: “moisture

Ras Ai Ex: Cloud Server

N Sires is:
N acca ye

~
Meigs = = =
“Og
--- page 13 ---
Data encryption: Encrypt in transit and at rest.
• Data protection: Preserves confidentiality and integrity across links and storage.
• Network protection: Thwarts interception and reading of traffic.
Regular firmware and software updates: Patch devices and apps promptly.
• Data protection: Removes flaws that could expose data.
•   Device/network protection: Closes holes attackers use to seize devices or disrupt
services.
Network segmentation: Place IoT devices on separate segments/VLANs.
• Data protection: Keeps breaches from reaching critical business systems.
•   Device/network protection: Contains lateral movement from a compromised device.
Secure device management and monitoring: Enforce discovery, configs, logging, analytics, and
continuous anomaly detection.
• Data protection: Surfaces threats that could compromise data.
•   Device/network protection: Enables early detection/response to limit damage.
Physical security: Protect devices against tampering, theft, and hardware implants.
•   Device protection: Prevents unauthorized physical access or resets.   6M
Challenges of data management in IoT
• Volume: Massive data strains storage, processing, and analytics.
•   Variety: Many formats and vendors hinder standardization and consistency.
•   Velocity: Real-time streams demand low-latency pipelines and compute.
•   Security and privacy: Sensitive data must be protected across collection, transport, and
storage.
• Data governance: Clarify ownership, access, retention, and compliance across diverse
stakeholders.
4M
********** 13 **********
--- page 14 ---
b.
Diagram   2M
Explanation of IoT Protocols – 4M
Key 6LoWPAN features
• IPv6 adaptation: Fits large IPv6 packets into tiny IEEE 802.15.4 frames so constrained
nodes can speak IP end-to-end.
• Header compression: Strips redundant IPv6/UDP fields to cut overhead, vital for low
c.
bandwidth and small memory.
• Fragmentation & reassembly: Splits big packets into fragments over the air and rebuilds
them at the destination.
• Mesh routing: Forms self-healing, scalable meshes so nodes relay traffic beyond single-
hop range.   4M
Q.7
a.
********** 14 **********

[Text in pictures on this page, read by OCR]
APPLICATION LAYER


TRANSPORT LAYER

NETWORK LAYER


PHYSICAL AND DATALINK LAYER

BLU ErooTH | | ZIGBEE | | WI-FI |
--- page 15 ---
2M
An IoT-based smart inventory management system can be designed using RFID technology
to monitor stock levels automatically and update data in real time.
System design: Each item carries an RFID tag with a unique ID. Readers at warehouse entry/exit
points scan tags automatically as goods move.
Architecture: RFID tags/readers feed a microcontroller or IoT gateway, which sends data over
the network to a cloud store/analytics layer. A web or mobile dashboard surfaces the results.
Data flows: tags → readers → gateway → cloud.
Working mechanism: On entry or exit, the reader detects the tag and notifies the controller,
which updates inventory counts in the cloud in real time.
Cloud analytics: The cloud logs stock levels and movement history, and auto-generates reports
for availability, reorder points, and usage trends.
User interface: A live dashboard shows current stock, low-inventory alerts, and tools for
planning replenishment.
Advantages: Cuts manual errors, gives instant visibility, and reduces overstock and stock outs
delivering faster, more accurate, and cost-effective inventory control with IoT + RFID.   8M
1. Importance of rapid prototyping: Using Arduino or Raspberry Pi lets teams test IoT
ideas early—validating functionality, connectivity, and data flow before big investments.
b.
Early builds expose design flaws, hardware limits, and performance bottlenecks, saving
time, cost, and risk. These platforms also support quick iteration: swap sensors, update
********** 15 **********

[Text in pictures on this page, read by OCR]
Cloud Server

Node MCU

DHT-11 Sensor Relay Module
Fan
LDR Sensor

{ (_____| Light

Power Supply
--- page 16 ---
firmware, and observe system behavior so prototypes mirror real operating conditions and
clarify how the final product will work.
2. Role of user feedback in prototyping: Hands-on trials surface insights on usability,
features, and reliability. Feedback often points to clearer interfaces, better data
visualizations, or sturdier device behavior. Teams can adjust the design to match user
expectations and real-world usage.
Influence on final IoT design: Combining rapid prototyping with user input produces a tighter,
more practical system, technically sound, aligned to user needs and environmental constraints,
and better positioned for product-market fit and commercial success.   6M
The Constrained Application Protocol (CoAP) is an application-layer protocol built for
resource-limited IoT devices. Its architecture has two sublayers that split transport messaging
from request–response semantics.
Message layer
This lowest layer rides on UDP and handles asynchronous exchanges between endpoints.
It provides basic reliability with retransmissions, tracks message IDs to drop duplicates, and
c.
manages timeouts and acknowledgments.
Request/response layer
This layer implements the client–server model, much like HTTP but trimmed for constrained
nodes.
It defines methods and response codes, supports URIs and content negotiation, and keeps wire
overhead low so small devices can interact efficiently.   4M
********** 16 **********
````
