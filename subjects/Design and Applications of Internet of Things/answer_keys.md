# Design and Applications of Internet of Things: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 5561127f16a9

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CS_7055/Design and Applications of Internet of Things/ANS_Design and Applications of Internet of Things(702CS0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Design and Applications of Internet of Things
Date: 08 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary
Section-A
Q1
CO-1   A.   Define Internet of Things (IoT). List any four real-world applications of   [05]
BL-1
IoT and explain one in brief.
Ans. • Definition: The Internet of Things (IoT) is a network of interconnected
physical devices embedded with sensors, software, and communication
technologies that enable them to collect, exchange, and act on data over the
internet without human intervention. (1 Marks)
• Applications (any 4):
• Smart Home
•   Healthcare
• Smart Agriculture
• Smart City (2 Marks)
• explain one in brief. (4 Mark)
The Internet of Things (IoT) is a network of interconnected physical
devices embedded with sensors, software, and communication
technologies that enable them to collect, exchange, and act on data over
the internet without human intervention.
🔹 Real-World Applications (Any Four) (2 Marks)
1. Smart Home Automation
2. Healthcare Monitoring Systems
3. Smart Agriculture
4. Smart Cities (traffic, parking, lighting)
********** 1 **********
--- page 2 ---
🔹 Explanation of One Application (1 Mark)
Example: Smart Home Automation
In a smart home system, devices such as lights, fans, security cameras,
and sensors are connected through the internet. Users can monitor and
control these devices remotely using a mobile application. Sensors detect
conditions like motion or temperature, and actuators perform actions such
as turning lights ON/OFF automatically, improving convenience and
energy efficiency.
Diagram and explanation (3 Marks)
CO-1   B.   Explain RFID technology and its types with suitable examples.   [05]
BL-2
Ans. • Definition of RFID (2 Marks)
• Types: Passive & Active (2 Marks)
• Example (inventory, access control) (1 Mark)
🔹 RFID Technology (2 Marks)
RFID (Radio Frequency Identification) is a wireless communication
technology that uses electromagnetic waves to identify, track, and store
information about objects or people without physical contact.
It consists of three main components:
• RFID Tag (stores data)
• RFID Reader (reads data)
********** 2 **********
--- page 3 ---
• Antenna (enables communication)
🔹 Types of RFID (2 Marks)
1. Passive RFID
• Does not have an internal power source
•   Gets energy from the reader’s electromagnetic field
•   Short range and low cost
2. Active RFID
• Has its own battery
• Can transmit signals over longer distances
•   Higher cost but better performance
(Optional: Semi-passive can also be mentioned for extra clarity)
🔹 Examples (1 Mark)
•   Passive RFID: Inventory management in retail stores
•   Active RFID: Vehicle tracking or toll collection systems
CO-2   C.   Differentiate between sensors and actuators. Give one IoT application for   [05]
BL-3
each.
Ans. • Sensor explanation (2 Marks)
• Actuator explanation (2 Marks)
• Example (IoT application) (1 Mark)
🔹 Difference Between Sensors and Actuators (4 Marks)
BASIS   SENSOR   ACTUATOR
FUNCTION   Converts physical quantity   Converts electrical
into electrical signal   signal into physical
action
ROLE   Input device   Output device
EXAMPLE   Temperature sensor,   Motor, solenoid
humidity sensor   valve
OPERATION   Detects environment   Performs action
based on input
🔹 IoT Applications (1 Mark)
•   Sensor Application:
Smart Agriculture – Soil moisture sensor detects water level in soil.
•   Actuator Application:
Smart Irrigation System – Water pump/valve (actuator) turns ON/OFF
based on sensor data.
********** 3 **********
--- page 4 ---
CO-3   D.   Analyze the role of the Network Layer in IoT architecture.   [05]
BL-4
Ans. • Definition (1 Marks)
• Functions (data transfer, connectivity) (2 Marks)
• Example (Wi-Fi/MQTT) (2 Mark)
🔹 Definition of Network Layer (1 Marks)
The Network Layer in IoT architecture is responsible for transmitting
data from the perception layer (sensors/devices) to the processing
systems (cloud/edge) through wired or wireless communication networks.
🔹 Key Functions (2 Marks)
1. Data Transmission
Transfers data collected by sensors to servers or cloud platforms.
2. Connectivity Management
Provides connectivity using technologies like Wi-Fi, Bluetooth, Zigbee,
LoRaWAN, 4G/5G.
3. Routing of Data
Determines the best path for data transmission between devices and
servers.
4. Protocol Handling
Uses communication protocols such as MQTT, CoAP, HTTP for efficient
data exchange.
🔹 Importance / Role in IoT (1 Marks)
•   Enables real-time communication between devices
•   Ensures reliable and efficient data transfer
•   Supports scalability for large IoT networks
• Connects physical devices to cloud systems
🔹 Example (1 Mark)
In a smart home system, temperature sensor data is transmitted via Wi-
Fi through the network layer to a cloud server, where users can monitor it
through a mobile app.
Section- B
Q2
CO-1 A   Explain power management techniques in IoT systems. How do they   [10]
BL-3   improve system efficiency?
Ans. • Concept of power management (2 Marks)
• Techniques (any 3–4):
********** 4 **********
--- page 5 ---
•   Sleep mode
• Duty cycling
• Energy harvesting
• Low-power protocols (4 Marks)
• Benefits (efficiency, battery life) (3 Marks)
• Diagram/clarity (1 Mark)
Power management techniques in IoT systems involve
optimizing hardware and software to minimize energy consumption, primarily
using duty cycling (sleep modes), power gating, and dynamic voltage/frequency
scaling (DVFS). These techniques extend battery life, reduce maintenance costs,
and enable long-term deployment in remote areas by ensuring components only
use power when necessary.
Key Power Management Techniques:
•   Sleep modes: Turning off the device while keeping only the most
essential parts active
• Energy harvesting: Using energy-harvesting devices to extend the
life of sensor nodes
• Low-power design principles: Using low-power components and
modes to reduce power consumption
• Network optimization: Choosing a connectivity solution that
minimizes energy consumption
• Hardware energy optimization: Selecting energy-efficient
components like microcontrollers
•   Real-time energy monitoring: Using IoT-enabled sensors to monitor
energy consumption in real time
• Smart energy management: Using IoT to automate energy-heavy
tasks and adjust energy use based on demand
How They Improve System Efficiency:
1. Extended Battery Life: By only operating at full capacity during
active tasks, devices can last months or years on a single battery,
reducing the need for constant recharging.
2. Increased Reliability: Optimized power consumption prevents
overheating and lowers the risk of abrupt shutdown, which is critical
for remote sensors.
3. Reduced Operational Costs: Devices that use less power, or
harvest their own, decrease the labor-intensive costs of replacing
batteries in large-scale deployments,
4. Optimized Performance: Techniques like DVFS ensure the device
is not wasting energy by running too fast for simple tasks
CO-2 B   Analyze the working and interfacing of motion and gas sensors in IoT   [10]
BL-4   systems. Explain their role in real-time monitoring applications.
********** 5 **********
--- page 6 ---
Ans. • Motion sensor working (PIR) (3 Marks)
• Gas sensor working (MQ series) (3 Marks)
• Interfacing with controller (2 Marks)
• Applications (2 Marks)
1. Working of Motion Sensor (PIR) (3 Marks)
• A PIR (Passive Infrared) sensor detects motion by sensing changes in
infrared radiation emitted by objects (humans/animals).
• When motion is detected, the sensor outputs a HIGH signal; otherwise,
it remains LOW.
•   It is commonly used in security and automation systems.
🔹 2. Working of Gas Sensor (MQ Series) (3 Marks)
• Gas sensors (e.g., MQ-2, MQ-135) detect the concentration of gases
like LPG, CO, smoke.
• They work based on change in resistance of a sensing material when
exposed to gas.
• Output is either analog (varying voltage) or digital (threshold-based
detection).
🔹 3. Interfacing with IoT Systems (2 Marks)
• Both sensors are connected to a microcontroller (Arduino/ESP8266).
•   PIR → Digital pin (HIGH/LOW signal)
• Gas sensor → Analog pin (voltage output)
• Data is processed and sent to the cloud or application via IoT
protocols (MQTT/HTTP).
🔹 4. Role in Real-Time Monitoring (2 Marks)
•   Enables instant detection of motion or gas leakage
•   Triggers alerts/notifications (mobile app, alarms)
• Used in smart homes, industrial safety, and surveillance systems
•   Helps in preventing accidents and improving security
Q3
CO-2 A   Explain SPI and I2C communication protocols used in IoT sensor   [10]
BL-3   interfacing.
Ans. • SPI explanation (3 Marks)
• I2C explanation (3 Marks)
• Comparison (3 Marks)
• Diagram/clarity (1 Mark)
CO-3 B   Analyze the 5-layer IoT architecture with a neat diagram.   [10]
BL-4
********** 6 **********
--- page 7 ---
Ans. • Diagram (3 Marks)
• Layer explanation (any 5 layers) (5 Marks)
• Example/application (2 Marks)
Q4
CO-3 A   A smart home system uses temperature, motion, and humidity sensors. The   [10]
BL-3   data is sent to a cloud platform, and users can monitor and control devices
through a mobile application answer the following with the help suitable
diagram.
a) Identify and explain the IoT architecture layers involved.
b) Explain the role of the network layer in data transmission.
c) Suggest a suitable communication protocol (MQTT/HTTP) and justify.
Ans. • Architecture layers identified (4 Marks)
• Network layer role (3 Marks)
• Protocol justification (MQTT/HTTP) (3 Marks)
🔹 (a) IoT Architecture Layers (4 Marks)
In the given smart home system, the following IoT layers are involved:
1. Perception Layer (Sensing Layer)
o Includes temperature, motion, and humidity sensors
o   Collects real-time environmental data
2. Network Layer
o Transfers data from sensors to cloud using Wi-Fi/Internet
3. Processing Layer (Cloud Layer)
o Stores and processes data
o Performs analytics and decision-making
4. Application Layer
o Mobile application used by users to monitor and control
devices
(b) Role of Network Layer (3 Marks)
•   Responsible for data transmission from sensors to the cloud
•   Provides connectivity using Wi-Fi, Bluetooth, or Internet
•   Ensures reliable and real-time communication
• Uses protocols like MQTT/HTTP for data exchange
🔹 (c) Suitable Protocol (3 Marks)
MQTT is more suitable
Justification:
•   Lightweight protocol (low bandwidth usage)
• Uses publish-subscribe model
•   Ideal for real-time IoT applications
********** 7 **********
--- page 8 ---
•   Efficient for low-power devices
(HTTP can also be used but is heavier and slower for IoT systems)
CO-3 B   A company wants to provide remote access to applications for employees   [10]
BL-4
across multiple locations.
Which technology (Cloud Computing or Virtualization) would be more
suitable? Justify your answer based on scalability, accessibility, and
flexibility.
Ans. • Cloud explanation (3 Marks)
• Virtualization explanation (3 Marks)
• Comparison (scalability, accessibility, flexibility) (3 Marks)
• Conclusion (1 Mark)
Q5
CO-4 A   A city installs IoT-enabled street lights that automatically turn ON/OFF   [10]
BL-3   based on ambient light and motion detection.
Questions:
a) Analyze how sensors and actuators work together in this system. (4
Marks)
b) Explain the role of IoT protocols in communication. (3 Marks)
c) Identify challenges such as scalability and energy efficiency. (3 Marks)
Ans. • Sensor-actuator interaction (4 Marks)
• Protocol role (3 Marks)
• Challenges (scalability, energy) (3 Marks)
CO-3 B   Analyze and explain WebSocket protocol and its advantages over HTTP   [10]
BL-4   in IoT systems.
Ans. • WebSocket explanation (3 Marks)
• HTTP explanation (3 Marks)
• Comparison (3 Marks)
• Conclusion (1 Mark)
Q6
CO-2 A   Explain different types of sensors used in IoT with suitable examples.   [10]
BL-2
Ans. • Types (any 4–5) (5 Marks)
• Explanation (3 Marks)
• Examples (2 Marks)
********** 8 **********
--- page 9 ---
CO-4 B   Explain the working principle of a solenoid valve and describe how it can   [10]
BL-4   be interfaced with a microcontroller in an IoT system.
Ans. • Working principle (electromagnetic) (4 Marks)
• Interfacing (relay/MOSFET) (3 Marks)
• Application (irrigation/automation) (2 Marks)
• Diagram/clarity (1 Mark)
Q7
CO-3 A   Analyze routing protocols used in IoT and   their performance   [10]
BL-4   considerations.
Ans. • Routing concept (3 Marks)
• Protocols (RPL, etc.) (4 Marks)
• Performance factors (latency, energy) (3 Marks)
CO-4 B   An IoT-based system is designed to detect forest fires using temperature,   [10]
BL-6   gas, and smoke sensors. Alerts are sent to authorities through cloud
platforms explain the following with help of suitable diagram.
a) Design the IoT system architecture for this application.
b) Select appropriate sensors and explain their working.
c) Explain how real-time monitoring helps in disaster prevention.
Ans. • Architecture design (4 Marks)
• Sensor’s selection (3 Marks)
• Real-time monitoring explanation (3 Marks)
X-----------------------------------------------------------------------------------------------------------------
X
********** 9 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper b5185798186b

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CS_7055/Design and Applications of Internet of Things/ANS_Design and Applications of Internet of Things(702CS0C007)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: mixed (19 pages), mean OCR confidence 84.8

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Design and Applications of Internet of Things
Date: 04 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary
Section-A
Q1
CO-1   A.   Define IoT. Explain any four characteristics of IoT.   [05]
BL-1
Ans.   •   Definition (1 Mark): IoT = network of interconnected physical
devices with sensors, software, internet connectivity.
• Any 4 Characteristics (1 Mark each):
o Connectivity
o   Intelligence (data processing)
o Heterogeneity
o Dynamic nature
o   Scalability
o Security
Evaluation Scheme:
•   Definition: 1
• 4 characteristics: 4 × 1 = 4
The Internet of Things (IoT) refers to a network of interconnected
physical devices embedded with sensors, software, and communication
technologies that enable them to collect, exchange, and act on data over
the internet without human intervention.
Characteristics of IoT:
1. Connectivity: Devices are connected via networks like Wi-Fi, Bluetooth,
Zigbee, etc.
2. Intelligence: Devices process data and make decisions using embedded
systems or cloud computing.
********** 1 **********
--- page 2 ---
3. Heterogeneity: IoT devices vary in hardware, software, and
communication protocols.
4. Scalability: The system can handle a large number of devices
efficiently.
5. Dynamic Changes: Devices continuously update their status and
environment conditions.
6. Security: Ensures safe data transmission and device authentication.
CO-1   B.   Explain transmission and reception in IoT communication.   [05]
BL-2
Ans. Synoptics:
• Data transmission via sensors → gateway → cloud
• Communication mediums (Wi-Fi, Zigbee, Bluetooth)
• Modulation & encoding
•   Reception: decoding → processing → action
Evaluation Scheme:
• Transmission explanation: 2
• Reception explanation: 2
• Diagram / example: 1
Transmission:
•   Sensors collect environmental data (temperature, humidity, etc.).
• Data is converted into digital signals.
•   Transmitted via communication protocols (Wi-Fi, Zigbee, Bluetooth,
LoRa).
•   Sent to a gateway or cloud server.
Reception:
• Data is received by a server/cloud platform.
• Decoding and processing occur.
• Data is analyzed and actions are triggered (alerts, automation).
********** 2 **********
--- page 3 ---
Flow:
Sensor → Microcontroller → Communication Module → Cloud →
User/Application
CO-2   C.   Explain temperature and humidity sensor interfacing in IoT.   [05]
BL-3
Ans. Synoptics:
• Example: DHT11/DHT22 sensor
•   Interfacing with microcontroller (ESP32/Arduino)
• Data pin connection
• Output reading (digital signal)
• Use in IoT dashboard/cloud
Evaluation Scheme:
• Sensor explanation: 1
•   Circuit/interface: 2
•   Working/output: 2
• Common sensors: DHT11 / DHT22
• Measures temperature and humidity digitally.
Interfacing Steps:
• Connect VCC → Power (3.3V/5V)
• GND → Ground
• Data pin → Microcontroller GPIO
•   Pull-up resistor used
Working:
•   Sensor captures data
********** 3 **********
--- page 4 ---
• Sends digital signal to microcontroller
• Data processed and sent to cloud/dashboard
Applications:
• Weather monitoring
• Smart agriculture
• Smart homes
CO-3   D.   Analyze the Processing Layer (Middleware) in IoT architecture.   [05]
BL-4
Ans. Synoptics:
• Acts as bridge between hardware & application
• Data storage & management
• Device management
•   Security & authentication
• Data analytics
Evaluation Scheme:
•   Definition: 1
•   Functions (any 4): 4
The Processing Layer (Middleware) acts as an interface between
hardware (devices) and application layer.
Functions:
• Data storage and management
• Data processing and filtering
•   Device management
•   Security (authentication & encryption)
• Data analytics and decision-making
********** 4 **********
--- page 5 ---
Importance:
• Reduces complexity
•   Enables interoperability
•   Supports scalability
Section- B
Q2
CO-1 A   Explain transponder and RFID working in IoT systems.   [10]
BL-3
Ans. Synoptics:
• RFID components: tag, reader, antenna
• Working principle (radio waves)
• Transponder = transmitter + responder
•   Active vs passive RFID
•   Applications (tracking, smart cards)
Evaluation Scheme:
• RFID explanation: 3
• Working: 3
• Transponder concept: 2
•   Diagram/applications: 2
RFID (Radio Frequency Identification):
A technology used for automatic identification using radio waves.
Components:
•   RFID Tag (contains data)
********** 5 **********
--- page 6 ---
•   RFID Reader
• Antenna
Working:
1. Reader emits radio signals
2. Tag receives signal and activates
3. Tag sends stored data back
4. Reader processes information
Transponder:
A device that receives and transmits signals automatically.
•   Passive RFID: no battery
•   Active RFID: battery-powered
Applications:
•   Access control
•   Inventory management
•   Toll collection
CO-2 B   Analyze different types of IoT sensors and their working principles.   [10]
BL-4
Ans. Synoptics:
• Temperature (thermistor)
•   Pressure (piezoelectric)
• Motion (PIR)
•   Light (LDR)
• Gas sensors
• Working principles
Evaluation Scheme:
• Types (any 4–5): 5
********** 6 **********
--- page 7 ---
• Working principles: 5
1. Temperature Sensor
• Measures heat (Thermistor/RTD)
2. Pressure Sensor
• Uses piezoelectric effect
3. Motion Sensor (PIR)
•   Detects infrared radiation
4. Light Sensor (LDR)
•   Resistance changes with light
5. Gas Sensor
•   Detects harmful gases
Working Principle:
Sensors convert physical parameters → electrical signals → processed by
microcontroller.
Q3
CO-2 A   Explain SPI vs I2C with suitable diagrams.   [10]
BL-3
Ans. Synoptics:
•   SPI: full duplex, faster, more pins
•   I2C: half duplex, fewer pins
• Clock & data lines
• Addressing (I2C)
• Comparison table + diagram
********** 7 **********
--- page 8 ---
Evaluation Scheme:
• SPI explanation: 3
• I2C explanation: 3
•   Differences: 2
• Diagram: 2
SPI (Serial Peripheral Interface):
•   Full duplex communication
• Uses 4 lines: MOSI, MISO, SCLK, SS
•   High speed
I2C (Inter-Integrated Circuit):
•   Half duplex
• Uses 2 lines: SDA, SCL
•   Supports multiple devices via addressing
SPI :
I2C :
********** 8 **********
--- page 9 ---
Feature   SPI   I2C
Speed   High   Moderate
Pins   More   Less
Addressi No   Yes
ng
Complex Low   Moderate
ity
CO-3 B   Analyze 3-layer vs 5-layer IoT architecture.   [10]
BL-4
Ans, Synoptics:
•   3-layer: Perception, Network, Application
•   5-layer: adds Transport, Processing layers
• Advantages of 5-layer
• Comparison
Evaluation Scheme:
•   3-layer: 3
•   5-layer: 3
•   Comparison/analysis: 4
3-Layer Architecture:
1. Perception Layer (Sensors)
2. Network Layer (Communication)
3. Application Layer
5-Layer Architecture:
1. Perception
2. Transport
3. Processing
4. Application
5. Business Layer
********** 9 **********
--- page 10 ---
Comparison:
•   5-layer provides better data processing & management
• More scalable and secure than 3-layer
Q4
CO-3 A   Explain CoAP protocol and its use in IoT.   [10]
BL-3
Ans. Synoptics:
•   Lightweight REST-based protocol
• Works on UDP
•   Request/response model
• Low power usage
• Used in constrained devices
Evaluation Scheme:
•   Definition: 2
•   Features: 4
• Working: 2
•   Applications: 2
CoAP (Constrained Application Protocol) is a lightweight protocol for
IoT devices.
********** 10 **********
--- page 11 ---
Features:
• Based on UDP
• REST architecture
• Low power consumption
•   Supports multicast
Working:
•   Client-server model
• Uses GET, POST, PUT, DELETE
Applications:
• Smart homes
•   Industrial IoT
CO-3 B   A smart building uses IoT sensors to monitor electricity consumption. The   [10]
BL-4
system automatically turns off unused devices and optimizes power usage.
a) Analyze how IoT helps in energy optimization.
b) Explain the role of cloud and data analytics.
c) Suggest suitable hardware platforms for implementation.
Ans. Synoptics:
(a) Energy optimization (3):
•   Sensors detect usage
• Auto shutdown
• Smart scheduling
(b) Cloud & analytics (3):
• Data storage
•   Pattern analysis
•   Decision making
********** 11 **********
--- page 12 ---
(c) Hardware (4):
• ESP32 / Raspberry Pi
• Smart meters
•   Sensors
Evaluation Scheme:
•   (a): 3
•   (b): 3
•   (c): 4
(a) Energy Optimization:
•   Sensors detect usage patterns
• Automatic switching off devices
• Smart scheduling reduces waste
(b) Cloud & Analytics:
• Data stored in cloud
•   Analysis identifies trends
•   Helps in decision-making
(c) Hardware Platforms:
• ESP32
•   Arduino
•   Raspberry Pi
• Smart meters
Q5
CO-4 A   Sensors are installed in parking slots to detect availability. Users can check   [10]
BL-3   parking status via a mobile app.
a) Explain the working of the IoT system in this scenario.
********** 12 **********
--- page 13 ---
b) Identify suitable communication protocols.
c) Analyze the challenges in implementing this system.
Ans. Synoptics:
(a) Working (4):
•   Sensors detect vehicle
• Data → cloud → app
(b) Protocols (3):
• MQTT, HTTP, LoRa
(c) Challenges (3):
• Cost
•   Connectivity
•   Scalability
Evaluation Scheme:
•   (a): 4
•   (b): 3
•   (c): 3
(a) Working:
•   Sensors detect vehicle presence
• Data sent to cloud
• Mobile app shows availability
(b) Protocols:
• MQTT
• HTTP
• LoRa
(c) Challenges:
•   High cost
• Network reliability
• Maintenance
********** 13 **********
--- page 14 ---
CO-3 B   Analyze MQTT vs HTTP protocols in IoT systems.   [10]
BL-4
Ans. Synoptics:
• MQTT: lightweight, publish-subscribe
• HTTP: request-response
•   Efficiency comparison
• Use cases
Evaluation Scheme:
• MQTT: 3
• HTTP: 3
• Comparison: 4
MQTT:
•   Lightweight
•   Publish/Subscribe model
• Low bandwidth
HTTP:
• Request/Response
•   Higher overhead
********** 14 **********
--- page 15 ---
Q6
CO-2 A   Explain pressure sensors and their IoT applications.   [10]
BL-2
Ans. Synoptics:
• Types: piezoelectric, capacitive
• Working principle
•   Applications (industry, healthcare)
Evaluation Scheme:
• Types: 3
• Working: 4
•   Applications: 3
Types:
•   Piezoelectric
•   Capacitive
********** 15 **********
--- page 16 ---
•   Resistive
Working:
Pressure → deformation → electrical signal
Applications:
•   Industrial monitoring
•   Healthcare (BP devices)
• Automotive systems
CO-4 B   Explain ThingSpeak API and data visualization process.   [10]
BL-4
Ans. Synoptics:
• Data collection via API keys
• Upload via HTTP/MQTT
•   Visualization graphs
• Cloud storage
Evaluation Scheme:
• API concept: 3
• Data flow: 3
•   Visualization: 4
ThingSpeak:
Cloud platform for IoT data collection and analysis by MathWorks.
Working:
•   Devices send data via API key
• Data stored in channels
• Graphs generated
Visualization:
•   Real-time graphs
• Data analysis using MATLAB
********** 16 **********
--- page 17 ---
Q7
CO-3 A   Analyze routing and performance issues in IoT networks.   [10]
BL-4
Ans. Synoptics:
• Routing challenges (dynamic topology)
• Energy constraints
• Latency
•   Packet loss
•   Scalability
Evaluation Scheme:
• Routing issues: 5
• Performance issues: 5
Routing Issues:
• Dynamic topology
•   Limited bandwidth
•   Energy constraints
Performance Issues:
•   Latency
•   Packet loss
•   Scalability problems
********** 17 **********
--- page 18 ---
CO-4 B   A farmer uses IoT sensors (soil moisture, temperature, humidity) to automate   [10]
irrigation. The system sends data to the cloud and controls water pumps.
BL-6
a) Design the system architecture.
b) Select suitable sensors and communication protocols.
c) Explain how automation improves water efficiency.
Ans. Synoptics:
(a) Architecture (4):
•   Sensors → controller → cloud → actuator
(b) Sensors & protocols (3):
•   Soil moisture, temp, humidity
• MQTT / LoRa
(c) Automation benefits (3):
• Water saving
•   Efficiency
• Reduced manual effort
Evaluation Scheme:
•   (a): 4
•   (b): 3
•   (c): 3
(a) Architecture:
Sensors → Microcontroller → Cloud → Actuator (pump)
(b) Sensors & Protocols:
•   Soil moisture sensor
• Temperature & humidity sensor
• MQTT / LoRa
(c) Benefits:
•   Saves water
• Improves crop yield
********** 18 **********
--- page 19 ---
e Reduces manual effort

Wireless
communication
Weather prediction - module
algorithm

Server
and
Data

storage

Local processing unit

Water controller/

valve +
. Sensor network in the

Web Application field

(Temperature, humidity,
soil moisture level)

Manual user inputs/
remote monitoring

FOI 7 QF CR
````
