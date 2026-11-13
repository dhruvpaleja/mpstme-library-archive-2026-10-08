# Internet of Things: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 796c5a2f6e51

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_EXTC_7006/Internet of Things (IoT)/ANS_Internet of Things (IoT)(702EX0E003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Internet of Things (IoT)
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer the following questions in brief   [20]
a.   Explain working of Ultrasonic sensor with neat diagram and steps.
Answer:
1. Principle (1 Mark)
• Works on echo principle using ultrasonic waves.
2. Components (1 Mark)
• TRIG pin, ECHO pin, transmitter, receiver
3. Working Steps (2 Marks)   5
• TRIG sends ultrasonic pulse
• Wave reflects from object
• ECHO receives reflected signal
• Time calculated → distance computed
4. Formula/Diagram (1 Mark)
•   Distance = (Time × Speed of Sound) / 2
• (Diagram: Sensor → Object → Echo return)
b.   Discuss the features of Raspberry Pi in brief.
5
Answer:
********** 1 **********
--- page 2 ---
1. Small and Low Cost (1 Mark)
• Compact single-board computer
2. GPIO Pins (1 Mark)
• Used for interfacing sensors and devices
3. Connectivity (1 Mark)
• Supports Wi-Fi, Bluetooth, Ethernet
4. OS Support (1 Mark)
• Runs Linux-based OS (Raspberry Pi OS)
5. Multimedia & Processing (1 Mark)
• HDMI support, camera interface, sufficient processing power
c.   Define classification and regression with one IoT example each.
Answer:
1. Classification (2 Marks)
•   Predicts categorical output
• Example: Detect gas leak (Yes/No)
2. Regression (2 Marks)   5
•   Predicts continuous values
• Example: Predict temperature level
3. Difference (1 Mark)
•   Classification → discrete output, Regression → continuous output
d.   Explain ZigBee architecture and its components with a diagram.
Answer:
1. Definition (1 Mark)
5
• Low-power wireless communication protocol
2. Components (2 Marks)
•   Coordinator (controls network)
• Router (forwards data)
********** 2 **********
--- page 3 ---
• End Device (sensing node)
3. Working (1 Mark)
• Data transmitted via coordinator through routers to devices
4. Diagram (1 Mark)
Coordinator → Router → End Devices
Q2
Answer the following questions   [20]
a   Write an Arduino program to measure distance using Ultrasonic sensor and
display output.
Answer:
1. Circuit Setup (2 Marks)
• TRIG → Digital Pin
• ECHO → Digital Pin
2. Code (5 Marks)
int trigPin = 9;
int echoPin = 10;
long duration;
int distance;
10
void setup() {
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
Serial.begin(9600);
}
void loop() {
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
********** 3 **********
--- page 4 ---
duration = pulseIn(echoPin, HIGH);
distance = duration * 0.034 / 2;
Serial.print("Distance: ");
Serial.println(distance);
}
3. Working (3 Marks)
•   Trigger pulse sent
• Echo received
•   Distance calculated and displayed
b   Analyze IoT challenges and justify how cloud and fog computing can overcome
latency issues.
Answer:
1. IoT Challenges (4 Marks)
• High latency
• Bandwidth limitations
•   Security issues
•   Scalability
2. Cloud Computing Role (3 Marks)
10
•   Centralized processing
•   Storage and analytics
•   Scalable infrastructure
3. Fog Computing Role (2 Marks)
•   Processing near edge
• Reduces latency
4. Justification (1 Mark)
• Combination improves real-time response and efficiency
Q3
Answer the following questions   [20]
a   Design a Smart Air Quality Monitoring System using IoT and Cloud Integration.   10
********** 4 **********
--- page 5 ---
•   Selection and justification of sensors and microcontroller
• Data acquisition and transmission using suitable communication protocol
•   Integration with cloud platform for real-time monitoring and storage
•   Security considerations in cloud communication
• Block diagram and working explanation of the complete system
Answer:
1. Sensors & Controller (2 Marks)
• Gas sensor (MQ-135), Temperature sensor
• NodeMCU/Arduino
2. Block Diagram (2 Marks)
Sensors → Controller → Internet → Cloud → Dashboard
3. Data Transmission (2 Marks)
•   Protocol: MQTT (lightweight, efficient)
4. Cloud Integration (2 Marks)
•   Platform: ThingSpeak / AWS IoT
•   Stores and visualizes data
5. Security (1 Mark)
•   Encryption, authentication
6. Working (1 Mark)
•   Sensors collect data → send to cloud → user monitors pollution levels
b   Explain IoT Level 4 with a suitable example. Draw a neat diagram.
Answer:
Definition (2 Marks)
• A level-4 IoT system has multiple nodes that perform local analysis. Data
is stored in the cloud and the application is cloud-based.
•   Level-4 contains local and cloud- based observer nodes which can subscribe
10
to and receive information collected in the cloud from IoT devices.
•   Level-4 IoT systems are suitable for solutions where multiple nodes are
required, the data involved is big and the analysis requirements are
computationally intensive.
Architecture (3 Marks)
********** 5 **********
--- page 6 ---
•   Devices → Gateway → Local processing → Cloud → User
Diagram (2 Marks)
Example (3 Marks)
• Smart city system
o Local processing handles immediate decisions
o Cloud performs analytics and long-term storage
Q4
Answer the following questions   [20]
a   Compare MQTT and CoAP protocols based on communication model and
efficiency.
Answer:
1. MQTT Overview (2 Marks)
•   Publish-Subscribe model
• Uses TCP protocol
2. CoAP Overview (2 Marks)   10
• Request-Response model
• Uses UDP protocol
3. Communication Model (2 Marks)
• MQTT: Broker-based, asynchronous
• CoAP: Client-server, synchronous
4. Efficiency Comparison (3 Marks)
********** 6 **********
--- page 7 ---
Feature   MQTT   CoAP
Latency   Low   Very Low
Bandwidth   Low   Very Low
Reliability   High (TCP)   Moderate (UDP)
Complexity   Moderate   Low
5. Conclusion (1 Mark)
• MQTT better for reliable communication; CoAP better for lightweight, fast
transmission
b   Explain the functional components of Raspberry Pi and describe how they interact
during the execution of an IoT application. Explain the role of different input/output
interfaces (GPIO, HDMI, USB, Ethernet/Wi-Fi) in connecting external peripherals.
Answer:
1. Core Components (3 Marks)
• CPU (processor), RAM, Storage (SD card)
2. Interaction in IoT Application (3 Marks)
•   Sensors send data via GPIO
• CPU processes data   10
•   Results sent to cloud via network
3. I/O Interfaces (3 Marks)
• GPIO: sensor/actuator connection
• HDMI: display output
• USB: keyboard, camera
•   Ethernet/Wi-Fi: internet connectivity
4. Summary (1 Mark)
•   All components work together to enable sensing, processing, and
communication
Q5   Answer the following questions   [20]
a   Design an IoT-based smart parking system using an ultrasonic sensor and
NodeMCU. Illustrate the system with a neat block diagram and explain the working,
including sensor interfacing, distance measurement logic, and real-time data 10
transmission for parking status monitoring.
Answer:
********** 7 **********
--- page 8 ---
1. Components (2 Marks)
•   Ultrasonic sensor, NodeMCU, LED/App
2. Block Diagram (2 Marks)
Sensor → NodeMCU → Wi-Fi → Cloud → User
3. Sensor Interfacing (2 Marks)
• TRIG & ECHO pins connected to NodeMCU
4. Working (3 Marks)
• Sensor measures distance
•   Detects vehicle presence
• NodeMCU sends data to cloud
•   Parking status updated in real time
5. Application (1 Mark)
• Smart parking management
b   Explain Linear Regression with an IoT example.
Answer:
1. Definition (2 Marks)
•   Predicts continuous output using linear relationship
2. Equation (2 Marks)
10
• y=mx+cy = mx + cy=mx+c
3. Working (3 Marks)
•   Input features → model learns relationship → predicts output
4. IoT Example (3 Marks)
•   Predict temperature/humidity trends in smart agriculture
Q6   Answer the following questions   [20]
a   Explain IPv6 and its role in IoT scalability in detail.
Answer:
10
1. Definition (2 Marks)
********** 8 **********
--- page 9 ---
• IPv6 is next-generation IP addressing system
2. Features (3 Marks)
•   128-bit addressing
• Large address space
•   Auto-configuration
3. Role in IoT (3 Marks)
• Supports billions of devices
•   Eliminates address exhaustion
• Enables direct device communication
4. Conclusion (2 Marks)
•   Essential for scalable IoT networks
b   Explain K-means clustering algorithm with steps.
Answer:
1. Definition (2 Marks)
• Unsupervised learning algorithm
2. Steps (5 Marks)
10
1. Choose K clusters
2. Initialize centroids
3. Assign data points to nearest centroid
4. Update centroids
5. Repeat until convergence
3. Example (3 Marks)
• Group IoT sensors based on usage patterns
Q7   Answer the following questions   [20]
a   Evaluate and compare IoT communication protocols (MQTT, and CoAP) for cloud-
based IoT systems in terms of latency, bandwidth efficiency, scalability, and
security. Based on your analysis, justify the selection of the most suitable protocol
for a smart traffic management system, where real-time data from sensors and
10
cameras is used to dynamically control traffic signals and reduce congestion.
Answer:
1. Requirements (2 Marks)
********** 9 **********
--- page 10 ---
• Low latency, scalability, real-time
2. MQTT Analysis (2 Marks)
• Low bandwidth, scalable, reliable
3. CoAP Analysis (2 Marks)
•   Lightweight, fast, less reliable
4. Comparison (2 Marks)
Factor   MQTT   CoAP
Latency   Low   Very Low
Scalability High   Moderate
Security   Strong   Moderate
5. Justification (2 Marks)
• MQTT preferred for smart traffic due to reliability and scalability
b   Explain Decision Tree algorithm and evaluation metrics with an example.
Answer:
1. Definition (2 Marks)
•   Supervised learning algorithm using tree structure
2. Working (3 Marks)
• Data split based on conditions
• Nodes represent decisions   10
• Leaves represent output
3. Evaluation Metrics (3 Marks)
• Accuracy
•   Precision
•   Recall
4. Example (2 Marks)
•   Predict traffic congestion level (High/Low)
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 3b1764d21d80

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/Internet of Things (IoT)/ANS_Internet of Things (IoT)(702EX0E003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Internet of Things (IoT)
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer the following questions in brief   [20]
a.   Explain working of Ultrasonic sensor with neat diagram and steps.
Answer:
1. Principle (1 Mark)
• Works on echo principle using ultrasonic waves.
2. Components (1 Mark)
• TRIG pin, ECHO pin, transmitter, receiver
3. Working Steps (2 Marks)   5
• TRIG sends ultrasonic pulse
• Wave reflects from object
• ECHO receives reflected signal
• Time calculated → distance computed
4. Formula/Diagram (1 Mark)
•   Distance = (Time × Speed of Sound) / 2
• (Diagram: Sensor → Object → Echo return)
b.   Discuss the features of Raspberry Pi in brief.
5
Answer:
********** 1 **********
--- page 2 ---
1. Small and Low Cost (1 Mark)
• Compact single-board computer
2. GPIO Pins (1 Mark)
• Used for interfacing sensors and devices
3. Connectivity (1 Mark)
• Supports Wi-Fi, Bluetooth, Ethernet
4. OS Support (1 Mark)
• Runs Linux-based OS (Raspberry Pi OS)
5. Multimedia & Processing (1 Mark)
• HDMI support, camera interface, sufficient processing power
c.   Define classification and regression with one IoT example each.
Answer:
1. Classification (2 Marks)
•   Predicts categorical output
• Example: Detect gas leak (Yes/No)
2. Regression (2 Marks)   5
•   Predicts continuous values
• Example: Predict temperature level
3. Difference (1 Mark)
•   Classification → discrete output, Regression → continuous output
d.   Explain ZigBee architecture and its components with a diagram.
Answer:
1. Definition (1 Mark)
5
• Low-power wireless communication protocol
2. Components (2 Marks)
•   Coordinator (controls network)
• Router (forwards data)
********** 2 **********
--- page 3 ---
• End Device (sensing node)
3. Working (1 Mark)
• Data transmitted via coordinator through routers to devices
4. Diagram (1 Mark)
Coordinator → Router → End Devices
Q2
Answer the following questions   [20]
a   Write an Arduino program to measure distance using Ultrasonic sensor and
display output.
Answer:
1. Circuit Setup (2 Marks)
• TRIG → Digital Pin
• ECHO → Digital Pin
2. Code (5 Marks)
int trigPin = 9;
int echoPin = 10;
long duration;
int distance;
10
void setup() {
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
Serial.begin(9600);
}
void loop() {
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
********** 3 **********
--- page 4 ---
duration = pulseIn(echoPin, HIGH);
distance = duration * 0.034 / 2;
Serial.print("Distance: ");
Serial.println(distance);
}
3. Working (3 Marks)
•   Trigger pulse sent
• Echo received
•   Distance calculated and displayed
b   Analyze IoT challenges and justify how cloud and fog computing can overcome
latency issues.
Answer:
1. IoT Challenges (4 Marks)
• High latency
• Bandwidth limitations
•   Security issues
•   Scalability
2. Cloud Computing Role (3 Marks)
10
•   Centralized processing
•   Storage and analytics
•   Scalable infrastructure
3. Fog Computing Role (2 Marks)
•   Processing near edge
• Reduces latency
4. Justification (1 Mark)
• Combination improves real-time response and efficiency
Q3
Answer the following questions   [20]
a   Design a Smart Air Quality Monitoring System using IoT and Cloud Integration.   10
********** 4 **********
--- page 5 ---
•   Selection and justification of sensors and microcontroller
• Data acquisition and transmission using suitable communication protocol
•   Integration with cloud platform for real-time monitoring and storage
•   Security considerations in cloud communication
• Block diagram and working explanation of the complete system
Answer:
1. Sensors & Controller (2 Marks)
• Gas sensor (MQ-135), Temperature sensor
• NodeMCU/Arduino
2. Block Diagram (2 Marks)
Sensors → Controller → Internet → Cloud → Dashboard
3. Data Transmission (2 Marks)
•   Protocol: MQTT (lightweight, efficient)
4. Cloud Integration (2 Marks)
•   Platform: ThingSpeak / AWS IoT
•   Stores and visualizes data
5. Security (1 Mark)
•   Encryption, authentication
6. Working (1 Mark)
•   Sensors collect data → send to cloud → user monitors pollution levels
b   Explain IoT Level 4 with a suitable example. Draw a neat diagram.
Answer:
Definition (2 Marks)
• A level-4 IoT system has multiple nodes that perform local analysis. Data
is stored in the cloud and the application is cloud-based.
•   Level-4 contains local and cloud- based observer nodes which can subscribe
10
to and receive information collected in the cloud from IoT devices.
•   Level-4 IoT systems are suitable for solutions where multiple nodes are
required, the data involved is big and the analysis requirements are
computationally intensive.
Architecture (3 Marks)
********** 5 **********
--- page 6 ---
•   Devices → Gateway → Local processing → Cloud → User
Diagram (2 Marks)
Example (3 Marks)
• Smart city system
o Local processing handles immediate decisions
o Cloud performs analytics and long-term storage
Q4
Answer the following questions   [20]
a   Compare MQTT and CoAP protocols based on communication model and
efficiency.
Answer:
1. MQTT Overview (2 Marks)
•   Publish-Subscribe model
• Uses TCP protocol
2. CoAP Overview (2 Marks)   10
• Request-Response model
• Uses UDP protocol
3. Communication Model (2 Marks)
• MQTT: Broker-based, asynchronous
• CoAP: Client-server, synchronous
4. Efficiency Comparison (3 Marks)
********** 6 **********
--- page 7 ---
Feature   MQTT   CoAP
Latency   Low   Very Low
Bandwidth   Low   Very Low
Reliability   High (TCP)   Moderate (UDP)
Complexity   Moderate   Low
5. Conclusion (1 Mark)
• MQTT better for reliable communication; CoAP better for lightweight, fast
transmission
b   Explain the functional components of Raspberry Pi and describe how they interact
during the execution of an IoT application. Explain the role of different input/output
interfaces (GPIO, HDMI, USB, Ethernet/Wi-Fi) in connecting external peripherals.
Answer:
1. Core Components (3 Marks)
• CPU (processor), RAM, Storage (SD card)
2. Interaction in IoT Application (3 Marks)
•   Sensors send data via GPIO
• CPU processes data   10
•   Results sent to cloud via network
3. I/O Interfaces (3 Marks)
• GPIO: sensor/actuator connection
• HDMI: display output
• USB: keyboard, camera
•   Ethernet/Wi-Fi: internet connectivity
4. Summary (1 Mark)
•   All components work together to enable sensing, processing, and
communication
Q5   Answer the following questions   [20]
a   Design an IoT-based smart parking system using an ultrasonic sensor and
NodeMCU. Illustrate the system with a neat block diagram and explain the working,
including sensor interfacing, distance measurement logic, and real-time data 10
transmission for parking status monitoring.
Answer:
********** 7 **********
--- page 8 ---
1. Components (2 Marks)
•   Ultrasonic sensor, NodeMCU, LED/App
2. Block Diagram (2 Marks)
Sensor → NodeMCU → Wi-Fi → Cloud → User
3. Sensor Interfacing (2 Marks)
• TRIG & ECHO pins connected to NodeMCU
4. Working (3 Marks)
• Sensor measures distance
•   Detects vehicle presence
• NodeMCU sends data to cloud
•   Parking status updated in real time
5. Application (1 Mark)
• Smart parking management
b   Explain Linear Regression with an IoT example.
Answer:
1. Definition (2 Marks)
•   Predicts continuous output using linear relationship
2. Equation (2 Marks)
10
• y=mx+cy = mx + cy=mx+c
3. Working (3 Marks)
•   Input features → model learns relationship → predicts output
4. IoT Example (3 Marks)
•   Predict temperature/humidity trends in smart agriculture
Q6   Answer the following questions   [20]
a   Explain IPv6 and its role in IoT scalability in detail.
Answer:
10
1. Definition (2 Marks)
********** 8 **********
--- page 9 ---
• IPv6 is next-generation IP addressing system
2. Features (3 Marks)
•   128-bit addressing
• Large address space
•   Auto-configuration
3. Role in IoT (3 Marks)
• Supports billions of devices
•   Eliminates address exhaustion
• Enables direct device communication
4. Conclusion (2 Marks)
•   Essential for scalable IoT networks
b   Explain K-means clustering algorithm with steps.
Answer:
1. Definition (2 Marks)
• Unsupervised learning algorithm
2. Steps (5 Marks)
10
1. Choose K clusters
2. Initialize centroids
3. Assign data points to nearest centroid
4. Update centroids
5. Repeat until convergence
3. Example (3 Marks)
• Group IoT sensors based on usage patterns
Q7   Answer the following questions   [20]
a   Evaluate and compare IoT communication protocols (MQTT, and CoAP) for cloud-
based IoT systems in terms of latency, bandwidth efficiency, scalability, and
security. Based on your analysis, justify the selection of the most suitable protocol
for a smart traffic management system, where real-time data from sensors and
10
cameras is used to dynamically control traffic signals and reduce congestion.
Answer:
1. Requirements (2 Marks)
********** 9 **********
--- page 10 ---
• Low latency, scalability, real-time
2. MQTT Analysis (2 Marks)
• Low bandwidth, scalable, reliable
3. CoAP Analysis (2 Marks)
•   Lightweight, fast, less reliable
4. Comparison (2 Marks)
Factor   MQTT   CoAP
Latency   Low   Very Low
Scalability High   Moderate
Security   Strong   Moderate
5. Justification (2 Marks)
• MQTT preferred for smart traffic due to reliability and scalability
b   Explain Decision Tree algorithm and evaluation metrics with an example.
Answer:
1. Definition (2 Marks)
•   Supervised learning algorithm using tree structure
2. Working (3 Marks)
• Data split based on conditions
• Nodes represent decisions   10
• Leaves represent output
3. Evaluation Metrics (3 Marks)
• Accuracy
•   Precision
•   Recall
4. Example (2 Marks)
•   Predict traffic congestion level (High/Low)
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 9914bb481196

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_IT_7041/Internet of Things (IoT)/ANS_Internet of Things (IoT)(702EX0E003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Internet of Things (IoT)
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer the following questions in brief   [20]
a.   Explain working of Ultrasonic sensor with neat diagram and steps.
Answer:
1. Principle (1 Mark)
• Works on echo principle using ultrasonic waves.
2. Components (1 Mark)
• TRIG pin, ECHO pin, transmitter, receiver
3. Working Steps (2 Marks)   5
• TRIG sends ultrasonic pulse
• Wave reflects from object
• ECHO receives reflected signal
• Time calculated → distance computed
4. Formula/Diagram (1 Mark)
•   Distance = (Time × Speed of Sound) / 2
• (Diagram: Sensor → Object → Echo return)
b.   Discuss the features of Raspberry Pi in brief.
5
Answer:
********** 1 **********
--- page 2 ---
1. Small and Low Cost (1 Mark)
• Compact single-board computer
2. GPIO Pins (1 Mark)
• Used for interfacing sensors and devices
3. Connectivity (1 Mark)
• Supports Wi-Fi, Bluetooth, Ethernet
4. OS Support (1 Mark)
• Runs Linux-based OS (Raspberry Pi OS)
5. Multimedia & Processing (1 Mark)
• HDMI support, camera interface, sufficient processing power
c.   Define classification and regression with one IoT example each.
Answer:
1. Classification (2 Marks)
•   Predicts categorical output
• Example: Detect gas leak (Yes/No)
2. Regression (2 Marks)   5
•   Predicts continuous values
• Example: Predict temperature level
3. Difference (1 Mark)
•   Classification → discrete output, Regression → continuous output
d.   Explain ZigBee architecture and its components with a diagram.
Answer:
1. Definition (1 Mark)
5
• Low-power wireless communication protocol
2. Components (2 Marks)
•   Coordinator (controls network)
• Router (forwards data)
********** 2 **********
--- page 3 ---
• End Device (sensing node)
3. Working (1 Mark)
• Data transmitted via coordinator through routers to devices
4. Diagram (1 Mark)
Coordinator → Router → End Devices
Q2
Answer the following questions   [20]
a   Write an Arduino program to measure distance using Ultrasonic sensor and
display output.
Answer:
1. Circuit Setup (2 Marks)
• TRIG → Digital Pin
• ECHO → Digital Pin
2. Code (5 Marks)
int trigPin = 9;
int echoPin = 10;
long duration;
int distance;
10
void setup() {
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
Serial.begin(9600);
}
void loop() {
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
********** 3 **********
--- page 4 ---
duration = pulseIn(echoPin, HIGH);
distance = duration * 0.034 / 2;
Serial.print("Distance: ");
Serial.println(distance);
}
3. Working (3 Marks)
•   Trigger pulse sent
• Echo received
•   Distance calculated and displayed
b   Analyze IoT challenges and justify how cloud and fog computing can overcome
latency issues.
Answer:
1. IoT Challenges (4 Marks)
• High latency
• Bandwidth limitations
•   Security issues
•   Scalability
2. Cloud Computing Role (3 Marks)
10
•   Centralized processing
•   Storage and analytics
•   Scalable infrastructure
3. Fog Computing Role (2 Marks)
•   Processing near edge
• Reduces latency
4. Justification (1 Mark)
• Combination improves real-time response and efficiency
Q3
Answer the following questions   [20]
a   Design a Smart Air Quality Monitoring System using IoT and Cloud Integration.   10
********** 4 **********
--- page 5 ---
•   Selection and justification of sensors and microcontroller
• Data acquisition and transmission using suitable communication protocol
•   Integration with cloud platform for real-time monitoring and storage
•   Security considerations in cloud communication
• Block diagram and working explanation of the complete system
Answer:
1. Sensors & Controller (2 Marks)
• Gas sensor (MQ-135), Temperature sensor
• NodeMCU/Arduino
2. Block Diagram (2 Marks)
Sensors → Controller → Internet → Cloud → Dashboard
3. Data Transmission (2 Marks)
•   Protocol: MQTT (lightweight, efficient)
4. Cloud Integration (2 Marks)
•   Platform: ThingSpeak / AWS IoT
•   Stores and visualizes data
5. Security (1 Mark)
•   Encryption, authentication
6. Working (1 Mark)
•   Sensors collect data → send to cloud → user monitors pollution levels
b   Explain IoT Level 4 with a suitable example. Draw a neat diagram.
Answer:
Definition (2 Marks)
• A level-4 IoT system has multiple nodes that perform local analysis. Data
is stored in the cloud and the application is cloud-based.
•   Level-4 contains local and cloud- based observer nodes which can subscribe
10
to and receive information collected in the cloud from IoT devices.
•   Level-4 IoT systems are suitable for solutions where multiple nodes are
required, the data involved is big and the analysis requirements are
computationally intensive.
Architecture (3 Marks)
********** 5 **********
--- page 6 ---
•   Devices → Gateway → Local processing → Cloud → User
Diagram (2 Marks)
Example (3 Marks)
• Smart city system
o Local processing handles immediate decisions
o Cloud performs analytics and long-term storage
Q4
Answer the following questions   [20]
a   Compare MQTT and CoAP protocols based on communication model and
efficiency.
Answer:
1. MQTT Overview (2 Marks)
•   Publish-Subscribe model
• Uses TCP protocol
2. CoAP Overview (2 Marks)   10
• Request-Response model
• Uses UDP protocol
3. Communication Model (2 Marks)
• MQTT: Broker-based, asynchronous
• CoAP: Client-server, synchronous
4. Efficiency Comparison (3 Marks)
********** 6 **********
--- page 7 ---
Feature   MQTT   CoAP
Latency   Low   Very Low
Bandwidth   Low   Very Low
Reliability   High (TCP)   Moderate (UDP)
Complexity   Moderate   Low
5. Conclusion (1 Mark)
• MQTT better for reliable communication; CoAP better for lightweight, fast
transmission
b   Explain the functional components of Raspberry Pi and describe how they interact
during the execution of an IoT application. Explain the role of different input/output
interfaces (GPIO, HDMI, USB, Ethernet/Wi-Fi) in connecting external peripherals.
Answer:
1. Core Components (3 Marks)
• CPU (processor), RAM, Storage (SD card)
2. Interaction in IoT Application (3 Marks)
•   Sensors send data via GPIO
• CPU processes data   10
•   Results sent to cloud via network
3. I/O Interfaces (3 Marks)
• GPIO: sensor/actuator connection
• HDMI: display output
• USB: keyboard, camera
•   Ethernet/Wi-Fi: internet connectivity
4. Summary (1 Mark)
•   All components work together to enable sensing, processing, and
communication
Q5   Answer the following questions   [20]
a   Design an IoT-based smart parking system using an ultrasonic sensor and
NodeMCU. Illustrate the system with a neat block diagram and explain the working,
including sensor interfacing, distance measurement logic, and real-time data 10
transmission for parking status monitoring.
Answer:
********** 7 **********
--- page 8 ---
1. Components (2 Marks)
•   Ultrasonic sensor, NodeMCU, LED/App
2. Block Diagram (2 Marks)
Sensor → NodeMCU → Wi-Fi → Cloud → User
3. Sensor Interfacing (2 Marks)
• TRIG & ECHO pins connected to NodeMCU
4. Working (3 Marks)
• Sensor measures distance
•   Detects vehicle presence
• NodeMCU sends data to cloud
•   Parking status updated in real time
5. Application (1 Mark)
• Smart parking management
b   Explain Linear Regression with an IoT example.
Answer:
1. Definition (2 Marks)
•   Predicts continuous output using linear relationship
2. Equation (2 Marks)
10
• y=mx+cy = mx + cy=mx+c
3. Working (3 Marks)
•   Input features → model learns relationship → predicts output
4. IoT Example (3 Marks)
•   Predict temperature/humidity trends in smart agriculture
Q6   Answer the following questions   [20]
a   Explain IPv6 and its role in IoT scalability in detail.
Answer:
10
1. Definition (2 Marks)
********** 8 **********
--- page 9 ---
• IPv6 is next-generation IP addressing system
2. Features (3 Marks)
•   128-bit addressing
• Large address space
•   Auto-configuration
3. Role in IoT (3 Marks)
• Supports billions of devices
•   Eliminates address exhaustion
• Enables direct device communication
4. Conclusion (2 Marks)
•   Essential for scalable IoT networks
b   Explain K-means clustering algorithm with steps.
Answer:
1. Definition (2 Marks)
• Unsupervised learning algorithm
2. Steps (5 Marks)
10
1. Choose K clusters
2. Initialize centroids
3. Assign data points to nearest centroid
4. Update centroids
5. Repeat until convergence
3. Example (3 Marks)
• Group IoT sensors based on usage patterns
Q7   Answer the following questions   [20]
a   Evaluate and compare IoT communication protocols (MQTT, and CoAP) for cloud-
based IoT systems in terms of latency, bandwidth efficiency, scalability, and
security. Based on your analysis, justify the selection of the most suitable protocol
for a smart traffic management system, where real-time data from sensors and
10
cameras is used to dynamically control traffic signals and reduce congestion.
Answer:
1. Requirements (2 Marks)
********** 9 **********
--- page 10 ---
• Low latency, scalability, real-time
2. MQTT Analysis (2 Marks)
• Low bandwidth, scalable, reliable
3. CoAP Analysis (2 Marks)
•   Lightweight, fast, less reliable
4. Comparison (2 Marks)
Factor   MQTT   CoAP
Latency   Low   Very Low
Scalability High   Moderate
Security   Strong   Moderate
5. Justification (2 Marks)
• MQTT preferred for smart traffic due to reliability and scalability
b   Explain Decision Tree algorithm and evaluation metrics with an example.
Answer:
1. Definition (2 Marks)
•   Supervised learning algorithm using tree structure
2. Working (3 Marks)
• Data split based on conditions
• Nodes represent decisions   10
• Leaves represent output
3. Evaluation Metrics (3 Marks)
• Accuracy
•   Precision
•   Recall
4. Example (2 Marks)
•   Predict traffic congestion level (High/Low)
********** 10 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper d1ccc77f9530

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_IT_7037/Internet of Things (IoT)/ANS_Internet of Things (IoT)(702EX0E003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Internet of Things (IoT)
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer the following questions in brief   [20]
a.   Explain working of Ultrasonic sensor with neat diagram and steps.
Answer:
1. Principle (1 Mark)
• Works on echo principle using ultrasonic waves.
2. Components (1 Mark)
• TRIG pin, ECHO pin, transmitter, receiver
3. Working Steps (2 Marks)   5
• TRIG sends ultrasonic pulse
• Wave reflects from object
• ECHO receives reflected signal
• Time calculated → distance computed
4. Formula/Diagram (1 Mark)
•   Distance = (Time × Speed of Sound) / 2
• (Diagram: Sensor → Object → Echo return)
b.   Discuss the features of Raspberry Pi in brief.
5
Answer:
********** 1 **********
--- page 2 ---
1. Small and Low Cost (1 Mark)
• Compact single-board computer
2. GPIO Pins (1 Mark)
• Used for interfacing sensors and devices
3. Connectivity (1 Mark)
• Supports Wi-Fi, Bluetooth, Ethernet
4. OS Support (1 Mark)
• Runs Linux-based OS (Raspberry Pi OS)
5. Multimedia & Processing (1 Mark)
• HDMI support, camera interface, sufficient processing power
c.   Define classification and regression with one IoT example each.
Answer:
1. Classification (2 Marks)
•   Predicts categorical output
• Example: Detect gas leak (Yes/No)
2. Regression (2 Marks)   5
•   Predicts continuous values
• Example: Predict temperature level
3. Difference (1 Mark)
•   Classification → discrete output, Regression → continuous output
d.   Explain ZigBee architecture and its components with a diagram.
Answer:
1. Definition (1 Mark)
5
• Low-power wireless communication protocol
2. Components (2 Marks)
•   Coordinator (controls network)
• Router (forwards data)
********** 2 **********
--- page 3 ---
• End Device (sensing node)
3. Working (1 Mark)
• Data transmitted via coordinator through routers to devices
4. Diagram (1 Mark)
Coordinator → Router → End Devices
Q2
Answer the following questions   [20]
a   Write an Arduino program to measure distance using Ultrasonic sensor and
display output.
Answer:
1. Circuit Setup (2 Marks)
• TRIG → Digital Pin
• ECHO → Digital Pin
2. Code (5 Marks)
int trigPin = 9;
int echoPin = 10;
long duration;
int distance;
10
void setup() {
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
Serial.begin(9600);
}
void loop() {
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
********** 3 **********
--- page 4 ---
duration = pulseIn(echoPin, HIGH);
distance = duration * 0.034 / 2;
Serial.print("Distance: ");
Serial.println(distance);
}
3. Working (3 Marks)
•   Trigger pulse sent
• Echo received
•   Distance calculated and displayed
b   Analyze IoT challenges and justify how cloud and fog computing can overcome
latency issues.
Answer:
1. IoT Challenges (4 Marks)
• High latency
• Bandwidth limitations
•   Security issues
•   Scalability
2. Cloud Computing Role (3 Marks)
10
•   Centralized processing
•   Storage and analytics
•   Scalable infrastructure
3. Fog Computing Role (2 Marks)
•   Processing near edge
• Reduces latency
4. Justification (1 Mark)
• Combination improves real-time response and efficiency
Q3
Answer the following questions   [20]
a   Design a Smart Air Quality Monitoring System using IoT and Cloud Integration.   10
********** 4 **********
--- page 5 ---
•   Selection and justification of sensors and microcontroller
• Data acquisition and transmission using suitable communication protocol
•   Integration with cloud platform for real-time monitoring and storage
•   Security considerations in cloud communication
• Block diagram and working explanation of the complete system
Answer:
1. Sensors & Controller (2 Marks)
• Gas sensor (MQ-135), Temperature sensor
• NodeMCU/Arduino
2. Block Diagram (2 Marks)
Sensors → Controller → Internet → Cloud → Dashboard
3. Data Transmission (2 Marks)
•   Protocol: MQTT (lightweight, efficient)
4. Cloud Integration (2 Marks)
•   Platform: ThingSpeak / AWS IoT
•   Stores and visualizes data
5. Security (1 Mark)
•   Encryption, authentication
6. Working (1 Mark)
•   Sensors collect data → send to cloud → user monitors pollution levels
b   Explain IoT Level 4 with a suitable example. Draw a neat diagram.
Answer:
Definition (2 Marks)
• A level-4 IoT system has multiple nodes that perform local analysis. Data
is stored in the cloud and the application is cloud-based.
•   Level-4 contains local and cloud- based observer nodes which can subscribe
10
to and receive information collected in the cloud from IoT devices.
•   Level-4 IoT systems are suitable for solutions where multiple nodes are
required, the data involved is big and the analysis requirements are
computationally intensive.
Architecture (3 Marks)
********** 5 **********
--- page 6 ---
•   Devices → Gateway → Local processing → Cloud → User
Diagram (2 Marks)
Example (3 Marks)
• Smart city system
o Local processing handles immediate decisions
o Cloud performs analytics and long-term storage
Q4
Answer the following questions   [20]
a   Compare MQTT and CoAP protocols based on communication model and
efficiency.
Answer:
1. MQTT Overview (2 Marks)
•   Publish-Subscribe model
• Uses TCP protocol
2. CoAP Overview (2 Marks)   10
• Request-Response model
• Uses UDP protocol
3. Communication Model (2 Marks)
• MQTT: Broker-based, asynchronous
• CoAP: Client-server, synchronous
4. Efficiency Comparison (3 Marks)
********** 6 **********
--- page 7 ---
Feature   MQTT   CoAP
Latency   Low   Very Low
Bandwidth   Low   Very Low
Reliability   High (TCP)   Moderate (UDP)
Complexity   Moderate   Low
5. Conclusion (1 Mark)
• MQTT better for reliable communication; CoAP better for lightweight, fast
transmission
b   Explain the functional components of Raspberry Pi and describe how they interact
during the execution of an IoT application. Explain the role of different input/output
interfaces (GPIO, HDMI, USB, Ethernet/Wi-Fi) in connecting external peripherals.
Answer:
1. Core Components (3 Marks)
• CPU (processor), RAM, Storage (SD card)
2. Interaction in IoT Application (3 Marks)
•   Sensors send data via GPIO
• CPU processes data   10
•   Results sent to cloud via network
3. I/O Interfaces (3 Marks)
• GPIO: sensor/actuator connection
• HDMI: display output
• USB: keyboard, camera
•   Ethernet/Wi-Fi: internet connectivity
4. Summary (1 Mark)
•   All components work together to enable sensing, processing, and
communication
Q5   Answer the following questions   [20]
a   Design an IoT-based smart parking system using an ultrasonic sensor and
NodeMCU. Illustrate the system with a neat block diagram and explain the working,
including sensor interfacing, distance measurement logic, and real-time data 10
transmission for parking status monitoring.
Answer:
********** 7 **********
--- page 8 ---
1. Components (2 Marks)
•   Ultrasonic sensor, NodeMCU, LED/App
2. Block Diagram (2 Marks)
Sensor → NodeMCU → Wi-Fi → Cloud → User
3. Sensor Interfacing (2 Marks)
• TRIG & ECHO pins connected to NodeMCU
4. Working (3 Marks)
• Sensor measures distance
•   Detects vehicle presence
• NodeMCU sends data to cloud
•   Parking status updated in real time
5. Application (1 Mark)
• Smart parking management
b   Explain Linear Regression with an IoT example.
Answer:
1. Definition (2 Marks)
•   Predicts continuous output using linear relationship
2. Equation (2 Marks)
10
• y=mx+cy = mx + cy=mx+c
3. Working (3 Marks)
•   Input features → model learns relationship → predicts output
4. IoT Example (3 Marks)
•   Predict temperature/humidity trends in smart agriculture
Q6   Answer the following questions   [20]
a   Explain IPv6 and its role in IoT scalability in detail.
Answer:
10
1. Definition (2 Marks)
********** 8 **********
--- page 9 ---
• IPv6 is next-generation IP addressing system
2. Features (3 Marks)
•   128-bit addressing
• Large address space
•   Auto-configuration
3. Role in IoT (3 Marks)
• Supports billions of devices
•   Eliminates address exhaustion
• Enables direct device communication
4. Conclusion (2 Marks)
•   Essential for scalable IoT networks
b   Explain K-means clustering algorithm with steps.
Answer:
1. Definition (2 Marks)
• Unsupervised learning algorithm
2. Steps (5 Marks)
10
1. Choose K clusters
2. Initialize centroids
3. Assign data points to nearest centroid
4. Update centroids
5. Repeat until convergence
3. Example (3 Marks)
• Group IoT sensors based on usage patterns
Q7   Answer the following questions   [20]
a   Evaluate and compare IoT communication protocols (MQTT, and CoAP) for cloud-
based IoT systems in terms of latency, bandwidth efficiency, scalability, and
security. Based on your analysis, justify the selection of the most suitable protocol
for a smart traffic management system, where real-time data from sensors and
10
cameras is used to dynamically control traffic signals and reduce congestion.
Answer:
1. Requirements (2 Marks)
********** 9 **********
--- page 10 ---
• Low latency, scalability, real-time
2. MQTT Analysis (2 Marks)
• Low bandwidth, scalable, reliable
3. CoAP Analysis (2 Marks)
•   Lightweight, fast, less reliable
4. Comparison (2 Marks)
Factor   MQTT   CoAP
Latency   Low   Very Low
Scalability High   Moderate
Security   Strong   Moderate
5. Justification (2 Marks)
• MQTT preferred for smart traffic due to reliability and scalability
b   Explain Decision Tree algorithm and evaluation metrics with an example.
Answer:
1. Definition (2 Marks)
•   Supervised learning algorithm using tree structure
2. Working (3 Marks)
• Data split based on conditions
• Nodes represent decisions   10
• Leaves represent output
3. Evaluation Metrics (3 Marks)
• Accuracy
•   Precision
•   Recall
4. Example (2 Marks)
•   Predict traffic congestion level (High/Low)
********** 10 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper fe77a2d76903

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_EXTC_7006/Internet of Things (IoT)/ANS_Internet of Things (IoT)(702EX0E003)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (EXTC)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (IT)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Internet of Things (IoT)
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Question No.1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
Answer the following questions in brief   [20]
a.   Explain the working of Gas Sensor (MQ-2/MQ-135) with neat diagram and its
applications.
Ans:
A gas sensor is used to detect the presence and concentration of harmful gases
in the environment. Common sensors used are MQ-2 (for LPG, smoke, methane)
and MQ-135 (for air quality, CO2, ammonia, benzene).
Working Principle:
CO1,   These sensors work based on the change in resistance of the sensing material 5
BL2
(usually SnO₂ – Tin Dioxide).
•   In clean air, the sensor has a certain resistance.
• When harmful gas is present, the resistance changes.
• This change produces a corresponding voltage output.
• The microcontroller reads this analog voltage and determines gas
concentration.
Diagram:
********** 1 **********
--- page 2 ---
Applications:
1. LPG gas leakage detection
2. Air quality monitoring
3. Industrial safety systems
4. Fire and smoke detection
5. Smart home safety systems
b.   Discuss the major accessories and add-ons used with Raspberry Pi and explain
any two in brief.
Ans:
Raspberry Pi supports many accessories and add-ons to build IoT applications.
Major Accessories:
1. Power Adapter
2. Micro SD Card
3. HDMI Cable
4. USB Keyboard and Mouse
5. Camera Module
CO4,   5
BL2   6. Display Monitor
7. GPIO Expansion Board
8. Wi-Fi Dongle (for older models)
9. Sensors and Actuators
10. Heat Sink and Cooling Fan
Explanation of Any Two:
1. Micro SD Card
•   It acts as the primary storage device of Raspberry Pi.
•   It stores the operating system, programs, and user files.
2. Camera Module
********** 2 **********
--- page 3 ---
•   It is connected using the CSI port.
• Used in applications like surveillance, face detection, and smart
monitoring systems.
c.   Explain supervised learning and unsupervised learning with one IoT example
each.
Ans:
Machine learning helps IoT systems analyze data and make decisions.
Supervised Learning
In supervised learning, the model is trained using labeled data.
Example:
Predicting whether a machine will fail (Yes/No) using sensor data.
Algorithms:
•   Logistic Regression
CO3,   • Decision Tree   5
BL2
• Random Forest
Unsupervised Learning
In unsupervised learning, the model works on unlabeled data and finds hidden
patterns.
Example:
Grouping similar temperature sensors based on usage patterns.
Algorithms:
• K-Means Clustering
•   Hierarchical Clustering
d.   Explain the features of IEEE 802.15.4 protocol used in IoT communication.
Ans:
IEEE 802.15.4 is a standard used for low-rate wireless personal area networks
(LR-WPANs).
Features:
CO2,   1. Low Power Consumption   5
BL2
Suitable for battery-operated IoT devices.
2. Low Data Rate
Supports low-speed communication required in sensors.
3. Short Range Communication
Works efficiently within short distances.
********** 3 **********
--- page 4 ---
4. Low Cost
Cheap implementation for IoT applications.
5. Supports Star and Peer-to-Peer Topology
Flexible network design.
6. Reliable Communication
Provides error detection and acknowledgement.
Used in protocols like ZigBee and 6LoWPAN.
Q2
Answer the following questions   [20]
a   Design an IoT-based water level monitoring system using Ultrasonic sensor
and Arduino. Draw the block diagram and explain the working.
Ans:
This system monitors water level in tanks using an ultrasonic sensor.
Components:
•   Ultrasonic Sensor (HC-SR04)
• Arduino Uno
• Water Tank
• Buzzer/LED
• LCD Display (optional)
• Wi-Fi Module (optional)
CO4,
Block Diagram:   10
BL4
Working:
1. The ultrasonic sensor sends ultrasonic waves toward the water surface.
2. Waves reflect back and are received by the sensor.
********** 4 **********
--- page 5 ---
3. Time taken is measured.
4. Distance is calculated using:
Distance = (Time × Speed of Sound)/2
5. Water level is determined from tank height.
6. If water level is low/high, alert is generated.
7. Data can also be sent to cloud for remote monitoring.
b   Analyze the role of IoT levels and justify how fog computing improves
performance in delay-sensitive IoT applications.
Ans:
IoT levels define the complexity of IoT systems based on devices, gateways,
cloud, and analytics.
Role of IoT Levels:
• Small systems use fewer levels
• Large systems use multiple levels with cloud and edge processing
Example:
Level 1 → Simple monitoring
Level 6 → Large smart city system
Fog Computing
Fog computing brings computation closer to IoT devices.
CO2,
Why Needed:   10
BL5
Cloud-only systems create:
• High latency
• Network congestion
• Slow response
Improvements by Fog Computing:
1. Reduced Latency
Processing happens near devices.
2. Faster Decision Making
Useful in healthcare and traffic systems.
3. Reduced Bandwidth Usage
Only important data sent to cloud.
4. Better Reliability
Local systems continue even if cloud fails.
********** 5 **********
--- page 6 ---
Thus fog computing improves delay-sensitive IoT applications significantly.
Q3
Answer the following questions   [20]
a   Design an IoT-based smart street lighting system using cloud services. Explain
the complete architecture including sensors, communication protocol, cloud
integration, and security mechanisms.
Ans:
A smart street lighting system automatically controls street lights based on
environmental conditions and human activity, reducing energy consumption and
improving efficiency.
Components:
• LDR Sensor (light intensity detection)
• PIR Sensor (motion detection)
• NodeMCU / Arduino
• LED Street Lights
• Wi-Fi Module (if Arduino used)
• Cloud Platform (ThingSpeak / Adafruit IO / AWS IoT)
CO4,
Block Diagram   10
BL3
Working:
1. LDR detects day/night conditions.
2. PIR detects movement of vehicles or pedestrians.
3. During daytime, lights remain OFF.
4. At night, lights turn ON only when motion is detected.
********** 6 **********
--- page 7 ---
5. Sensor data is sent to cloud using MQTT or HTTP.
6. Cloud stores data and provides monitoring dashboard.
7. Municipal authorities can monitor and control lights remotely.
Communication Protocol:
MQTT is preferred because:
• Lightweight
• Low bandwidth usage
•   Reliable real-time communication
Security Mechanisms:
• User authentication
• Data encryption using TLS
• Secure cloud API access
• Role-based access control
b   Explain IoT Level 6 with a suitable example. Draw a neat diagram.
Ans:
IoT Level 6 is the most advanced IoT system involving multiple devices,
gateways, cloud services, big data analytics, and decision-making systems.
Features:
• Large number of devices
• Multiple sensors and gateways
• Cloud + local analytics
• Big data processing
• Machine learning integration
CO1,   • Real-time monitoring and control
10
BL2
Diagram:
********** 7 **********
--- page 8 ---
Example: Smart City
In a smart city:
•   Traffic sensors monitor roads
•   Pollution sensors monitor air quality
• Parking sensors manage vehicle slots
• Cloud performs analytics
• Mobile apps provide real-time updates to users
This requires IoT Level 6 due to large-scale operation.
Q4
Answer the following questions   [20]
a   Explain REST protocol in IoT communication and compare it with MQTT based
on working and efficiency.
Ans:
REST (Representational State Transfer) is a web-based communication method
used between client and server using HTTP methods like GET, POST, PUT,
DELETE.
Working of REST:
1. Client sends request to server
2. Server processes request
3. Response is returned in JSON/XML format
CO2,
Example:   10
BL2
Temperature sensor sends data using HTTP POST request.
Comparison with MQTT:
Feature   REST   MQTT
Model   Request-Response   Publish-Subscribe
Protocol   HTTP   TCP
Communication   Synchronous   Asynchronous
Bandwidth   Higher   Lower
IoT Suitability   Moderate   High
Latency   Higher   Lower
Conclusion:
********** 8 **********
--- page 9 ---
MQTT is better for continuous sensor communication, while REST is useful for
web integration and API services.
b   Explain the operating system installation and initial configuration steps of
Raspberry Pi for IoT development.
Ans:
Raspberry Pi requires operating system installation before IoT development.
Steps:
1. Download Raspberry Pi OS
Download from official Raspberry Pi website.
2. Flash OS to SD Card
Use Raspberry Pi Imager or Balena Etcher.
3. Insert SD Card and Boot
Insert SD card into Raspberry Pi and power ON.
4. Initial Setup
Configure:
• Language
CO4,   • Time zone
10
BL2   • Password
• Display settings
5. Network Configuration
Connect using:
• Wi-Fi
•   Ethernet
Enable:
• SSH
• VNC for remote access
6. Update System
sudo apt update
sudo apt upgrade
7. Install Required Libraries
Install Python libraries for sensors and GPIO.
Now Raspberry Pi is ready for IoT application development.
Q5   Answer the following questions   [20]
********** 9 **********
--- page 10 ---
a   Design an IoT-based smart irrigation system using soil moisture sensor and
NodeMCU or Ardunio. Draw the block diagram and explain the complete
working.
Ans:
This system automates irrigation based on soil moisture conditions.
Components:
•   Soil Moisture Sensor
• NodeMCU / Arduino
• Water Pump
• Relay Module
• Wi-Fi Module
• Cloud Platform
Block Diagram:
CO4,
10
BL4
Working:
1. Sensor measures soil moisture.
2. Controller reads moisture value.
3. If soil is dry:
o Pump turns ON
4. If moisture is sufficient:
o Pump turns OFF
5. Data is sent to cloud for remote monitoring.
This saves water and improves crop productivity.
CO3,   b   Explain Logistic Regression with suitable IoT application example.
10
BL2   Ans:
********** 10 **********
--- page 11 ---
Logistic Regression is a supervised learning algorithm used for classification
problems.
It predicts output in binary form:
YES/NO, ON/OFF, SAFE/UNSAFE
Mathematical Model:
Uses Sigmoid Function:
P = 1 / (1 + e^(-z))
where z = wx + b
Output value lies between 0 and 1.
IoT Example:
Gas Leakage Detection
Input:
• Gas level
• Temperature
•   Pressure
Output:
• Safe
• Unsafe
The model predicts whether danger exists based on sensor readings.
Q6   Answer the following questions   [20]
a   Explain 6LoWPAN architecture and discuss its advantages in IoT applications.
Ans:
CO2,
6LoWPAN stands for IPv6 over Low Power Wireless Personal Area Networks. 10
BL2
It allows IPv6 communication over low-power wireless networks like IEEE
802.15.4.
********** 11 **********
--- page 12 ---
Advantages:
1. IPv6 Support
Large address space for billions of IoT devices
2. Low Power Usage
Ideal for battery-operated devices
3. Low Cost
Affordable implementation
4. Small Packet Size
Efficient communication
5. Direct Internet Connectivity
No need for complex translation
Used in smart homes and industrial IoT.
b   Explain model validation and performance evaluation in machine learning with
suitable examples.
Ans:
Model validation checks whether a machine learning model performs well on
unseen data.
CO3,
Validation Methods:   10
BL2
1. Train-Test Split
Data divided into:
• Training set
•   Testing set
2. Cross Validation
Multiple testing rounds improve reliability
********** 12 **********
--- page 13 ---
Performance Metrics:
For Classification:
• Accuracy
•   Precision
•   Recall
• F1 Score
For Regression:
• MAE
• MSE
• RMSE
• R² Score
Example:
Predicting machine failure:
Accuracy helps evaluate correct predictions.
This ensures the model is reliable before deployment.
Q7   Answer the following questions   [20]
a   A smart warehouse uses IoT devices for inventory monitoring, temperature
control, and automated alerts. Evaluate MQTT and CoAP protocols for this
system and justify the most suitable protocol considering scalability, latency,
and security.
Ans:
A smart warehouse uses sensors for:
• Inventory monitoring
CO2,
• Temperature control   10
BL3
•   Alert systems
System requires:
• Low latency
• High scalability
• Secure communication
MQTT vs CoAP
********** 13 **********
--- page 14 ---
Feature   MQTT   CoAP
Protocol   TCP   UDP
Model   Publish-Subscribe   Request-Response
Reliability   High   Moderate
Latency   Low   Very Low
Security   Strong   Moderate
Scalability   High   Medium
Best Choice: MQTT
Justification:
•   Reliable message delivery
• Supports multiple devices
•   Better for continuous monitoring
•   Efficient cloud integration
• Strong authentication and TLS security
Hence MQTT is preferred for smart warehouse systems.
b   Explain the difference between supervised and unsupervised learning in IoT data
analytics with suitable examples. Also, discuss the commonly used model
performance metrics for evaluating machine learning models.
Ans:
Supervised Learning
Uses labeled data.
Example:
Predicting equipment failure
Algorithms:
CO3,   • Decision Tree
10
BL3   •   Logistic Regression
Unsupervised Learning
Uses unlabeled data.
Example:
Grouping sensors by behavior patterns
Algorithms:
• K-Means Clustering
Differences
********** 14 **********
--- page 15 ---
Feature   Supervised   Unsupervised
Data   Labeled   Unlabeled
Output   Known classes   Hidden groups
Example   Failure prediction   Sensor grouping
Performance Metrics
Classification:
• Accuracy
•   Precision
•   Recall
• F1 Score
Clustering:
•   Silhouette Score
•   Inertia
These metrics help evaluate how well models perform in IoT analytics.
********** 15 **********
````
