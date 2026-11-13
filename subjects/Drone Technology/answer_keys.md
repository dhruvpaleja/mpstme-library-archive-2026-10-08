# Drone Technology: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper cd7983f2283e

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIML_7053/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper e81927654908

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AI_7012/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper e660f2476186

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7057/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 78c762be9f8c

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CS_7055/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 40bf453ff67e

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 35f946c0be9c

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CyberSecurity_7010/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper cf69471fd208

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_DS_7009/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 82100b8ed7d0

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_EXTC_7006/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 8ee170c2fdf5

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_IT_7001/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper f4f227f47368

- Departments: Mechanical
- Programmes: BTech Mechanical 7003
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Mechanical_7003/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 5cc7c631300e

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Mechatronics_7004/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper a9ac2f468206

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_AI_7051/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 32791e0bb577

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 4f1a1c370540

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_IT_7041/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 9 · Answer key · paper 31999678510b

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_09/Final-Exam/Integrated_DS_7038/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Dec 2025
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: III / V/Semester IX/Semester V(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 10 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. Part A is compulsory.
5. Out of the remaining questions From Part B, Attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1.   Part A Compulsory   20M
CO-1 ;   A.   Explain with examples the classification of UAVs based on nano, micro and small.   [5]
BL-2   *[Classification-3M, Example-2M]
Nano UAVs are the smallest category, typically weighing less than 250 grams with
a wingspan of under 15 cm. They can operate up to an altitude of around 100 meters
and have a short flight endurance of about 5 to 20 minutes. Due to their compact
size and low weight, they are ideal for indoor or close-range outdoor applications.
Examples: DJI Tello, FLIR Black Hornet Nano
Micro UAVs fall in the weight range of 250 grams to 2 kilograms, with a wingspan
between 15 to 50 cm. They can fly up to about 1 km and typically have an endurance
of 20 to 60 minutes. These drones are portable and can carry small cameras or
sensors, making them suitable for aerial photography, environmental monitoring,
and academic research.
Examples: Parrot Anafi and DJI Mini 4 Pro
Small UAVs are larger and more capable, generally weighing between 2 and 25
kilograms with a wingspan of 0.5 to 2m. They can operate at altitudes up to about
3 km (line of sight) and have flight times ranging from one to two hours. These
drones can carry heavier payloads such as LiDAR, thermal, or multispectral
cameras, making them suitable for industrial and professional applications.
Examples: DJI Matrice 300 RTK, SenseFly eBee X.
CO-2 ;   B.   Define ESC firmware and explain its purpose in UAVs. List the common types of   [5]
BL-1,2   ESC firmware and identify which type is most suitable for smooth and responsive
flight, justifying your choice.
*[Def-1M, Purpose=1M,List-1M, Identification and Justification-2M]
An Electronic Speed Controller (ESC) firmware is the embedded software
programmed into the ESC that governs how it interprets control signals from the
flight controller and regulates the power supplied to the drone’s brushless motors.
********** 1 **********
--- page 2 ---
The purpose of ESC firmware in UAVs is to ensure smooth and precise motor
control by managing motor speed, acceleration, and braking.
The common types of ESC firmware used in UAVs include:
1. BLHeli
2. BLHeli_S
3. BLHeli_32
4. SimonK
5. KISS (Keep It Super Simple)
Among these, BLHeli_32 is the most suitable for achieving smooth and responsive
flight. This is because it operates on a 32-bit architecture, enabling faster signal
processing, precise motor control, and advanced features such as active braking
(damped light), bidirectional communication.
CO- 3;   C.   Define a drone imaging system and list its key components. Explain the function   [5]
BL-2,3   of each component and discuss how they work together to enable accurate aerial
imaging, data collection, and real-time monitoring in practical UAV applications.
*[Def-1M, Components-4M]
A drone imaging system refers to the integrated setup of hardware and software
components mounted on an Unmanned Aerial Vehicle (UAV) that enables the
capture, processing, and transmission of aerial images or videos for applications
such as mapping, inspection, surveillance, and environmental monitoring.
Key Components of a Drone Imaging System
1. Camera
• The camera is the core component responsible for capturing images or videos
of the target area. Depending on the application, different types of cameras are
used — such as RGB (visual), thermal infrared, multispectral, or LiDAR
sensors. Function is captures raw visual or sensor data from the environment.
2. Gimbal
• The gimbal is a mechanical stabilizer that keeps the camera steady during flight,
compensating for vibrations and drone movements. Function is ensures stable
and blur-free images by maintaining the camera’s orientation using gyroscopic
sensors and brushless motors.
3. GPS Module
• The GPS provides geolocation data for each image captured, which is essential
for mapping and geo-referencing. Function is tags each image with precise
latitude, longitude, and altitude coordinates, enabling accurate spatial mapping.
4. Inertial Measurement Unit (IMU)
• The IMU consists of accelerometers and gyroscopes that measure the drone’s
orientation, angular velocity, and acceleration. Function is provides orientation
and movement data, ensuring proper alignment between image frames and
improving image stitching accuracy.
5. Flight Controller
• The flight controller acts as the central processor that manages flight dynamics
and communicates with all onboard components. Function is controls motor
speed, stabilizes the drone, and synchronizes camera triggering with drone
position and movement.
6. Data Storage
• This includes onboard SD cards or wireless modules for storing and transmitting
captured data to the ground control station. Function is stores high-resolution
images or streams real-time video data for monitoring and analysis.
7. Ground Control Station (GCS)
• The GCS is the interface used by operators to monitor the drone’s status, view
live imagery, and control the imaging process. Function is enables mission
planning, real-time monitoring, and post-flight data analysis (e.g., image
stitching, mapping).
********** 2 **********
--- page 3 ---
CO- 4;   D.   [5]
BL-4   A quadcopter experiences rapid oscillations during sudden wind gusts. Analyze the
role of a Derivative controller in stabilizing the UAV; Evaluate the consequences
of incorrect D gain settings.   *[Role-2M Effect -3M]
• Derivative term produces a control action proportional to the rate of change of
the error (or of the measured state). For a quadcopter facing a sudden wind gust,
the disturbance causes the vehicle’s attitude or angular rates to change quickly.
• The D-term senses this rapid change and produces an immediate control
command that opposes the rate of error, i.e. it “pushes back” against how fast
the error is growing.
• When a gust induces a sudden angular acceleration, the gyro/IMU sees a spike
in angular rate. The D-term produces an opposing torque proportional to that
rate, reducing the amplitude and duration of the transient.
Tuning Issue Effect on Drone Stability
High D-Gain Excessive dampening, causing delayed response.
Low D-Gain Drone becomes susceptible to sudden external disturbances (wind).
2.   80M
1.   [20]
CO-1;   A.   Explain the parts of a drone, including its hardware, software, and mechanical   [10]
BL-2   subsystems. For each subsystem, describe its primary functions and discuss how it
contributes to flight stability. *[Hardware-5M, Software-2M, Mechanical-3M]
Hardware Subsystem
Battery (LiPo)
•   Provides power to the entire quadcopter system.
•   Supplies high-current output needed for motors.
Power Distribution Board (PDB)
•   Distributes electrical power from the battery to all components.
•   Supplies power to the ESCs, flight controller, and other electronics.
• Some PDBs include voltage regulators for different voltage requirements.
Electronic Speed Controllers (ESCs)
•   Receives power from the PDB and control signals from the flight controller.
•   Regulates power to each motor to control speed and rotation.
•   Converts DC battery power into a controlled AC signal for brushless
motors.
Motors
•   Generate thrust by spinning propellers at varying speeds.
•   Controlled individually by ESCs to achieve movement and stability.
Flight Controller
• The brain of the quadcopter that processes sensor data and pilot commands.
• Sends control signals to ESCs to adjust motor speeds for stability.
• Uses gyroscopes, accelerometers, and other sensors for precise flight
control.
Communication Module
• Allows wireless control and data transmission between the drone and the
ground control station.
Onboard Sensors (Barometer, Ultrasonic, Optical Flow, LiDAR)
• Measure altitude, ground distance, and environmental parameters for
enhanced control.
Software Subsystem
Firmware (e.g., PX4, ArduPilot, Betaflight):
• The embedded code running on the flight controller. It implements control
algorithms (PID loops), sensor fusion, and mission logic. Processes IMU
********** 3 **********
--- page 4 ---
and GPS data to compute control outputs that stabilize the drone in real
time.
Ground Control Software (e.g., QGroundControl, Mission Planner):
• Allows operators to plan flight paths, monitor telemetry, and adjust
parameters remotely. Enables mission management and real-time tuning of
flight parameters for safe operation.
Mechanical Subsystem
Frame
• The skeleton that holds all components together. Made from materials like
carbon fiber or aluminum for strength and lightweight design. Provides rigidity
to minimize vibration and maintain symmetrical weight distribution for
balanced flight.
Propeller
• Determines thrust and aerodynamic efficiency. Balanced propellers reduce
vibration. Smooth and even thrust output ensures vibration-free and steady flight.
CO-2;   B.   Explain the key factors in selecting an Electronic speed controller (ESC). Compare   [10]
BL-3   PWM, OneShot, and DShot protocols, and recommend the most suitable one for
precise, low-latency motor control. Justifying your choice.
*[Factors-4M, Comparison-4M, Justification-2M]
When selecting an ESC (Electronic Speed Controller) for a drone or UAV, several
key factors determine performance, compatibility, and efficiency:
1. Current Rating (A):
The ESC must handle the maximum current drawn by the motor plus a safety
margin (usually 20–30%). Underrated ESCs can overheat or fail during high
throttle operations.
2. Voltage Rating (V):
Must match the battery voltage (e.g., 3S–6S LiPo). Using an ESC with a lower
voltage rating than the battery can damage it.
3. Firmware Type:
Common firmware: BLHeli, SimonK, and KISS. BLHeli_32 and KISS support
advanced protocols (like DShot) and offer smooth, precise control and telemetry
feedback.
4. Communication Protocol:
Defines how fast and accurately the flight controller sends throttle commands
to the ESC (discussed below).
5. Built-in Features:
BEC (Battery Eliminator Circuit): Provides power to the flight controller or
receiver. Telemetry support: Reports motor RPM, voltage, and temperature
back to the flight controller. Current sensing: Helps monitor power
consumption.
6.   Size and Weight:
Important for small drones; mini ESCs reduce payload but may have lower
current capacity.
Feature   PWM   OneShot   DShot
Analog (shorter pulse
Signal Type   Analog   Digital
width)
Update Rate   50–490 Hz   ~2–4 kHz   Up to 30–40 kHz
Latency   High   Moderate   Very Low
16   bit   (digital
Resolution   8–10 bit   11–12 bit
precision)
********** 4 **********
--- page 5 ---
Very Low   (error-
Noise Sensitivity   High   Moderate
checked)
Calibration
Yes   Yes   No (auto-calibrates)
Needed
Yes (with bi-
Telemetry Support No   Limited
directional DShot)
Recommended Protocol: DShot: Reason: Digital precision, Low latency, Error-free
communication, No calibration required, Supports telemetry
2.   [20]
CO-3;   A.   Explain the Self-level, Acro & Horizon flight modes in a drone. Discuss how each   [10]
BL-2,3   mode responds to control stick inputs, highlighting differences in pilot control and
flight stability.   *[ Self- 3.5M, Acro-3.5M, Horizon-3M]
Drones use different flight modes that define how the flight controller interprets
the pilot’s stick inputs and how much stabilization assistance it provides.
1. Self-Level Mode
• The flight controller automatically stabilizes the drone using data from the
accelerometer and gyroscope.
• When the control sticks are centered, the drone returns to level flight
automatically. Stick deflection sets the tilt angle (pitch or roll) — not the
rotation rate. The maximum tilt is limited by a predefined angle (e.g., ±45°).
• When sticks are released, the flight controller commands the drone to return
to a flat, level attitude. High stability, minimal pilot workload — ideal for
beginners or stable camera flights. Limited agility; cannot perform flips or
rolls.
2. Acro Mode
• The flight controller does not self-level the drone. Only the gyroscope is used
to measure angular rates. Stick inputs correspond to angular velocity how fast
the drone rotates about each axis. Small stick movement → slow rotation,
Large stick movement → faster rotation.
• When sticks are released, the drone maintains its current attitude instead of
levelling itself. No automatic stabilization, full manual control, requires skill,
as the pilot must constantly correct orientation, Offers maximum freedom for
aerobatics and racing.
3. Horizon Mode
• A hybrid between Self-Level and Acro modes. Uses both accelerometer and
gyroscope data for control.
• At small stick deflections, the drone behaves like Self-Level Mode —
automatically levels when sticks are released.
• At large stick deflections, the drone behaves like Acro Mode, allowing flips,
rolls, and acrobatics. Moderate stability with acrobatic capability.
CO-4;   B.   Analyze how the P, I, and D components affect a drone’s flight. Evaluate the impact   [10]
BL-4,5   of too low or too high gains and explain why a combined PID controller ensures
more stable and responsive flight than using P, I, or D alone.
*[Individual P,I,D-7M, PID-3M]
P controller :
•   It provides control action proportional to the error between the desired
set point and the measured process variable. Imagine you are piloting a drone
and you want it to stay at a specific height. You set the desired height on the
controller, which is like the set point (SP) in the proportional control system.
• The drone has sensors that measure the current height, which is the process
variable (PV). Now, let us say the drone is flying too high. In proportional
control, the correction applied to the drone’s height will be proportional to the
difference between the desired height and the current height.
The P controller applies a correction proportional to the current error.
Control Output=P × Error
********** 5 **********
--- page 6 ---
Tuning Issue   Effect on Drone Stability
High P-Gain   Drone oscillates aggressively, leading to instability
Low P-Gain   Drone responds slowly, making it sluggish
D controller:
• It looks at how fast the altitude is changing and calculates the derivative of this
change. This helps the controller make adjustments to keep things in balance
and prevent things from changing too quickly. Without a D-controller, external
factors like wind gusts or payload changes could cause uncontrollable altitude
fluctuations.
Tuning Issue   Effect on Drone Stability
High D-Gain   Excessive dampening, causing delayed response
Low D-Gain   Drone becomes susceptible to sudden external disturbances (wind)
I controller:
• An integral controller, also known as an I-controller works by accumulating
the error signal over time and using this integrated value to make
appropriate adjustments to control inputs. For example, when the drone
deviates from its set point, the integral controller takes note of the duration
and magnitude of the error and applies corrective actions proportionally.
Tuning   Effect on Drone Stability
Issue
High I-Gain Leads to overshoot and sluggish correction.
Low I-Gain Drone struggles to hold altitude or position over time.
• A combined PID controller ensures stable and responsive flight by integrating
the strengths of all three components—Proportional, Integral, and Derivative.
The P term provides immediate corrective action to minimize current errors,
making the drone responsive to disturbances or pilot inputs.
• The I term eliminates steady-state errors caused by constant external forces
like wind, ensuring the drone maintains its position or attitude accurately over
time.
• The D term predicts and counteracts rapid changes, reducing overshoot and
oscillations for smoother control.
• Together, these actions create a balanced feedback system that delivers fast,
accurate, and stable flight performance, which cannot be achieved by using P,
I, or D individually.
3.   [20]
CO-1   A.   Explain pitch, roll, and yaw in a quadcopter and how each affects its orientation   [10]
BL-3   and flight path. Suggest how a pilot or flight controller should adjust these inputs
to maintain stable flight and identify which axis is most sensitive to sudden control
changes.   *[ Pitch-3M, Roll-3M, Yaw-3M, identify-1M]
Pitch
• Forward Pitch: To pitch the drone
forward (nose down), the motors at
the rear (rear left and rear right)
should have higher thrust.
• Backward Pitch: To pitch the drone
backward (nose up), the motors at the
front (front left and front right)
should have higher thrust.
********** 6 **********
--- page 7 ---
Roll
• Right Roll: To tilt the drone to the
right (roll to the right), the motors
on the left side (front left and rear
left) should have higher thrust.
• Left Roll: To tilt the drone to the
left (roll to the left), the motors on
the right side (front right and rear
right) should have higher thrust.
Yaw   • Yaw refers to the rotation of the
drone around its vertical axis.
This involves the drone turning to
the left or right without changing
its position in the sky.
• When a drone yaws, it rotates
horizontally, causing its nose to
point   left   or   right   while
maintaining its altitude.
• Yawing allows the drone to
change its orientation or direction
without necessarily changing its
position relative to the ground.
The roll axis is typically the most sensitive to sudden control changes because:
•   It directly affects side-to-side balance
•   Small tilts can rapidly shift the center of thrust, causing fast lateral motion
or loss of stability,
•   Especially in small drones with low inertia.
CO-2,   B.   Define the role of motors in a quadcopter. Explain the key factors to consider when   [10]
BL-2,3   choosing the motor for a drone. Justify why brushless DC motors are preferred over
brushed DC motors in drone applications.
*[Role-1M, Factors- 5M, Justification-4M]
Motors are responsible for converting electrical energy from the drone's battery into
mechanical power, which drives the propellers to produce thrust.
key characteristics of DC Motors for Drones
1. KV Rating:
Indicates the motor’s RPM (revolutions per minute) per volt applied. A higher KV
rating means higher speed but lower torque, suitable for lightweight, high-speed
drones. A lower KV rating means lower speed but higher torque, suitable for
carrying heavier payloads
2.Thrust:
The force produced by the motor, which should be sufficient to lift the drone and
its payload.
3.Voltage (V):
The operating voltage range, typically matching the battery voltage.
4.Current (A):
The current draw, affecting the power consumption and   flight time.
5. Weight:
The motor's weight, which affects the overall weight and performance of the drone.
6.Propeller Compatibility:
The motor must be compatible with the propellers you plan to use
in terms of size and mounting.
********** 7 **********
--- page 8 ---
Brushless DC Motor
Brushless DC motors are widely used in
modern drones because they offer high
efficiency, precision, and reliability. Unlike
brushed motors, BLDC motors have no
physical brushes; instead, they rely on
electronic commutation using an Electronic
Speed   Controller (ESC). This   design
minimizes friction and wear, resulting in
greater   efficiency   (around   80–90%),
smoother operation, and a much longer
lifespan.
Their high torque-to-weight ratio allows
rapid acceleration and stable hovering, which
are essential for flight control. BLDC motors
also generate less heat and require very little
maintenance, making them   ideal   for
continuous, high-speed drone applications.
Brushed DC Motor
Brushed DC motors, on the other hand, use
mechanical brushes and a commutator to
switch current direction within the motor.
This creates higher friction and wear,
reducing   efficiency and   limiting   their
lifespan. They tend to overheat faster and
require frequent maintenance due to brush
erosion.
Speed control is less accurate compared to
brushless motors, which can lead to delayed
response during flight maneuvers. Although
they are cheaper and simpler to operate, their
lower torque output and reduced reliability
make them unsuitable for high-performance
drones. Hence, while brushed motors may
still be used in small toy drones or
educational kits, brushless motors are the
standard choice for professional, stable, and
energy-efficient UAV applications.
4.   [20]
CO-1;   A.   Define a ground-based controller and explain its role in drone operation, real-time   [5]
BL-2   navigation.   *[ Def-1M, role in drone-2M, role in navigation-2M]
A Ground-Based Controller (GBC), also known as a Ground Control Station
(GCS), is the interface or system used by a human operator to monitor, control,
and manage the operation of an Unmanned Aerial Vehicle (UAV) or drone from
the ground. It serves as the primary communication link between the drone and
the operator, enabling command transmission and data reception in real time.
Role in Drone Operation
1. Command and Control Interface:
o The GBC sends flight commands such as takeoff, landing, altitude
adjustments, and waypoint navigation to the drone.
o   It allows manual or semi-autonomous control through joysticks,
radio transmitters, or software interfaces.
********** 8 **********
--- page 9 ---
2. Telemetry Monitoring:
o Displays critical drone parameters such as battery level, GPS
coordinates, altitude, airspeed, and motor status.
o Helps operators ensure safe and stable flight by providing live
feedback.
3. Communication Link:
o Uses radio frequency (RF), Wi-Fi, or satellite communication to
establish a reliable data link between the UAV and the operator.
o Ensures smooth exchange of control signals and sensor data.
Role in Real-Time Navigation
1. Flight Path Tracking:
o Provides live mapping of the drone’s trajectory using GPS
coordinates.
o Allows operators to adjust the route dynamically based on
environmental conditions or mission requirements.
2. Obstacle Avoidance and Geofencing:
o Displays nearby obstacles and restricted zones in real time.
o Enables the operator to re-route the drone instantly to prevent
collisions or boundary violations.
3. Sensor Data Visualization:
o Streams real-time data from onboard sensors (camera, LiDAR,
IMU, etc.) to assist in precise navigation and situational awareness.
CO-3;   B.   Discuss the importance of onboard sensors such as the IMU, GPS, magnetometer,   [15]
BL-3   and barometer in ensuring UAV navigation accuracy and flight stability. Explain
how sensor fusion contributes to precise attitude and position control.
*[Each sensor description-3M each and Sensor fusion-3M]
Inertial Measurement Units (IMUs):
• IMU functions by continuously monitoring the drone’s motion and
orientation through its built-in sensors.
Accelerometer:
•   It measures the force of acceleration acting on the drone in any direction.
• The accelerometer can detect changes in speed and direction, allowing the
drone to understand how fast it is moving and if it is ascending, descending,
or moving horizontally.
•   If the drone is accelerating too quickly or too slowly in one direction, the
flight controller adjusts the motor speeds to stabilize it.
Ex:
•   If the drone tilts forward, the accelerometer detects that tilt and the flight
controller increases the back motors’ speed to balance the drone.
Gyroscope:
•   It is responsible for detecting rotational movements around the drone’s
axes—this includes the drone’s tilt (pitch), rotation (yaw), and roll.
•   For instance, if wind tilts the drone to the left, the gyroscope senses this tilt
and sends data to the flight controller, which then adjusts the motors to level
the drone back to its original orientation.
GPS:
•   It is a satellite system that allows you to determine the precise geographical
location of an object anywhere in the world.
•   It works through a network of satellites orbiting the Earth that transmit
signals to receiving devices, which then use these signals to triangulate their
exact position.
•   Enables position hold, waypoint navigation, and return-to-home (RTH)
functions.
********** 9 **********
--- page 10 ---
•   Ensures the UAV follows a defined flight path during autonomous
missions.
• Compensates for drift that may occur due to IMU sensor errors over time.
Magnetometer:
• The magnetometer detects the Earth’s magnetic field and helps the drone
maintain its heading or direction, similar to how a compass works.
•   This is especially important for autonomous drones, as the magnetometer
ensures they stay on course, even in areas where GPS signals might be
weak.
•   In self-flying drones, the magnetometer helps the drone stay in the right
direction even if GPS is not working well
Barometer:
•   It is also known as Pressure sensors in drones.
•   It measures the atmospheric pressure to estimate the drone’s altitude.
•   As we know atmospheric pressure decreases with height, these sensors
calculate the altitude by comparing pressure readings with standard
pressure values at sea level.
Sensor fusion combines data from multiple sensors using algorithms such as the
Kalman Filter or Complementary Filter to produce more accurate and reliable
estimates of the UAV’s state. Through sensor fusion, these sensors collectively
enhance the accuracy of attitude estimation and position tracking, ensuring stable,
autonomous, and reliable UAV flight performance.
5.   [20]
CO-2;   A.   Discuss the key characteristics to consider when selecting motors, ESCs, propellers,   [10]
BL-2,3   flight controller and battery for a racing drone. Explain how these choices influence
the drone’s performance.   *[Each component-2M ]
Motors
• KV Rating (RPM/Volt):
o High KV (2300–2700 KV) → Faster RPM, more agility, shorter flight
time.
o Low KV (1500–2000 KV) → higher torque, supports larger propellers,
more stable but slower response.
•   Size (e.g., 2205, 2306): Larger motors provide more thrust but consume
more power.
•   Efficiency and Build Quality: Bearings and winding quality affect
smoothness and heat dissipation.
High-KV, lightweight motors allow rapid acceleration, quick directional changes,
and high top speeds ideal for racing. However, they require powerful ESCs and
high-current batteries to avoid overheating.
Electronic Speed Controllers (ESCs)
•   Current Rating (A): Must exceed the motor’s maximum current draw (e.g.,
35A–60A for racing drones).
•   Firmware: Modern ESCs use BLHeli_32 or SimonK, supporting fast
response and smooth throttle control.
•   Protocol: DShot and OneShot protocols provide lower latency and precise
speed control.
High-quality ESCs ensure rapid motor response, smooth throttle transitions, and
better handling during sharp maneuvers, which are critical in racing.
********** 10 **********
--- page 11 ---
Propellers
•   Size and Pitch:
o Smaller props (4–5 inches) → Quicker acceleration and higher agility.
o Higher pitch (4.5”–5”) → More thrust and top speed but increased
power consumption.
•   Material: Carbon fiber propellers are strong and stiff, while plastic ones are
lighter but flexible.
•   Blade Count: 3-blade props provide better control and thrust; 2-blade props
are more efficient and faster.
Propeller choice affects speed, agility, and battery drain. High-pitch and multi-
blade props increase thrust but reduce efficiency and flight time.
Flight Controller (FC)
•   Processor Speed: F4 or F7 flight controllers offer faster processing for real-
time stabilization.
• Firmware Support: Compatible with Betaflight, Cleanflight, or INAV for
customizable flight tuning.
•   Sensor Quality: Integrated IMU, barometer improve flight precision and
telemetry feedback.
•   Filter and PID Tuning Capability: Enables fine control over responsiveness.
A fast and well-tuned flight controller ensures stable flight, quick corrections, and
precise maneuvering, essential for tight racing tracks.
Battery
•   Type: Lithium Polymer (LiPo) battery.
•   Cell Count (S): Higher cell count (4S–6S) → higher voltage and faster
response.
•   Capacity (mAh): Determines flight duration (1300–1800 mAh for racing).
• C Rating: Indicates discharge rate — higher C (75C–120C) supports high
current draw for racing.
A properly matched battery provides consistent power delivery, fast throttle
response, and stable voltage during aggressive maneuvers. Too small a battery
causes voltage sag, while a heavy one reduces agility.
CO-4;   B.   Define the term Drone Security Threat in the context of UAV operations. Describe   [10]
BL-5   major drone security threats in areas such as terrorist attacks, illegal surveillance,
and reconnaissance. Evaluate the effectiveness of current drone countermeasure
technologies in preventing terrorist misuse.
*[ Def-1M, Describe-5M, Evaluate-4M]
A Drone Security Threat refers to any malicious or unauthorized use of an
Unmanned Aerial Vehicle (UAV) that poses a risk to public safety, national
security, privacy, or critical infrastructure. Such threats arise when drones are
exploited for unlawful activities like surveillance, smuggling, espionage, or
physical attacks, either by individuals or organized groups.
Major Drone Security Threats :
Terrorist Attacks
• Drones can be weaponized to deliver explosives or hazardous payloads to
targeted areas, bypassing ground-based security systems.
• They enable remote execution of attacks with minimal human risk to
perpetrators.
Illegal Surveillance
•   Unauthorized drones equipped with high-resolution cameras or thermal
sensors can capture sensitive images or videos of restricted zones, defense
installations, or private properties.
********** 11 **********
--- page 12 ---
• Such intrusions violate privacy laws and compromise national or corporate
confidentiality.
Reconnaissance and Intelligence Gathering
• Drones can be used for pre-attack reconnaissance by collecting terrain,
troop, or facility data.
•   Criminals and hostile entities may use UAVs to map security layouts, track
movements, or identify vulnerabilities in strategic assets.
Evaluation of Drone Countermeasure Technologies
Current counter-UAV technologies aim to detect, track, identify, and neutralize
unauthorized drones. Their effectiveness varies based on environment, range, and
type of threat.
1. Radio Frequency (RF) Jammers
• Effective in disrupting control and communication links between
drone and operator.
• Non-discriminatory—may interfere with legitimate radio services;
limited effectiveness   against autonomous drones using pre-
programmed missions.
2. Radar and Electro-Optical Detection Systems
• Provide early detection and classification using radar signatures or
visual/infrared imagery.
• Small drones with low radar cross-sections and non-metallic bodies are
hard to detect in cluttered environments.
3. GPS Spoofing and Signal Hijacking Prevention
• Protects UAV navigation integrity by authenticating GNSS signals.
• Sophisticated attackers can employ encrypted or inertial navigation
backups to bypass spoofing.
4. Anti-Drone Interception Systems
• Physically neutralize or disable hostile drones without collateral
damage.
• Limited range, requires line-of-sight, and may not be suitable for
swarm attacks.
6.
CO-4   A.   Design and develop a quadcopter equipped with thermal and optical cameras using   [20]
BL-6   OpenCV, Raspberry Pi, and a PixHawk controller for search-and-rescue operations.
Evaluate its use in locating missing persons, mapping disaster zones, and guiding
rescue teams.
********** 12 **********
--- page 13 ---
1. Define Requirements   1M
•   Clearly define the type of UAV (e.g., quadcopter, hexacopter, or fixed-
wing).
•   Mention payload requirements such as cameras, sensors, or sprayers.
•   Specify flight endurance, range, altitude, and the mission objectives (e.g.,
mapping, inspection, or monitoring).
2.Select Hardware component   3M
Component   Function
Lightweight, durable structure (carbon
Drone Frame
fiber recommended).
Handles stabilization, GPS navigation,
Pixhawk Flight Controller
and sensor fusion.
Raspberry Pi / Companion   Runs AI, image processing (OpenCV),
Computer   and ML models.
Camera (RGB / Thermal /   Captures visual or thermal data depending
Multispectral)   on the mission.
Generate thrust for lift and
Motors & ESCs
maneuverability.
LiPo Battery   Supplies power for all onboard systems.
Enable autonomous navigation and stable
GPS + IMU Sensors
flight.
Specialized Sensors (e.g.,   Task-specific sensing (e.g., obstacle
LiDAR, Gas, NDVI)   detection, pollution analysis).
Enables live data, video, and command
Telemetry Module   exchange with Ground Control Station
(GCS).
Onboard SSD/SD, PDB with regulated
Storage & power management:
5V/12V for Pi/gimbal.
3.Assemble the Drone:   1M
• Assemble the drone components according to the manufacturer's instructions
and best practices for safety and reliability
4.Software Configuration:   3M
• Flash the Pixhawk flight controller with the appropriate firmware, such as
ArduPilot or PX4, and configure it for your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to ensure accurate readings.
• Preprocessing: lens correction, stabilization (gimbal + software), image
alignment between thermal and RGB.
• Thermal hotspot detection: thresholding + connected components to find heat
blobs. Works well for night or obscured scenes.
• RGB person detection: lightweight neural net (Tiny-YOLO for bounding
boxes. OpenCV DNN can run models on Raspberry Pi or offload to NPU.
• Geotagging: use PixHawk GPS + camera orientation to compute lat/long of
detection (bearing + slant range approximate from altitude). Report coordinates
to GCS.
• Mapping: stitch RGB images for orthomosaic or use Structure-from-Motion
(SfM) to create 2D/3D maps of the disaster zone. Thermal map overlay if
needed.
5.Mission Planning and Waypoints:   2M
• Use mission planning software (e.g., Mission Planner, QGroundControl) to
define waypoints, flight paths, and mission parameters.
********** 13 **********
--- page 14 ---
• Set up geofencing and safety parameters to prevent the drone from flying into
restricted areas or in unfavorable conditions.
6. Implementation   5M
A. Locating missing persons
Strengths
• Thermal camera excels at night and can see people under light foliage or
dust if temperature contrast exists.
•   Faster area coverage than ground teams.
•   Geo-tagged detections quickly direct rescuers to likely locations.
Limitations
• Dense canopy, rubble, or subterranean victims may be occluded.
•   Heat signatures similar to background (sun-warmed rocks, machinery) can
cause false positives—fusion with RGB and human detector reduces this.
Metrics to evaluate
•   Detection range (meters) for person (depends on thermal res & altitude).
• True positive rate (TPR), false positive rate (FPR).
• Time to detect per square km.
B. Mapping disaster zones
Strengths
• Rapid creation of orthophotos and 3D models for situational awareness
(blocked roads, collapsed structures).
• Thermal overlay helps find hotspots (fires, survivors).
Limitations
• Photogrammetry needs good overlap and sunlight (RGB). Smoke, dust
reduce image quality.
•   Flight time limits area covered per sortie.
Metrics
• Map ground sampling distance (GSD) in cm/pixel.
• Area surveyed per sortie (hectares).
• Time to deliver actionable map to teams.
C. Guiding rescue teams
Strengths
•   Real-time video & coordinate feeds let rescuers approach likely locations
faster.
• Lower risk to human searchers; remote vetting before entry.
Limitations
•   Coordinate accuracy depends on GPS, camera-to-target geometry — may
need close approach for precision.
• Communications latency and link reliability in remote areas.
Metrics
•   Coordinate error (meters).
•   Latency from detection to operator notification.
7. Telemetry and Ground Control Station:   1M
• Set up telemetry systems for communication between the ground control
station (GCS) and the drone.
• Use a GCS software to monitor the drone's status, update missions in real-
time, and take control when needed.
********** 14 **********
--- page 15 ---
8. Testing and Calibration:   1M
• Conduct extensive testing in controlled environments to ensure the drone's
safety and navigation accuracy.
• Calibrate and fine-tune the drone's parameters, including PID controllers, to
optimize performance.
9.Safety Measures   1M
• Implement safety features like return-to-home (RTH) and fail-safe modes to
handle unexpected situations.
• Comply with local regulations and obtain necessary permissions for
autonomous flights.
10.Integration of Payload   1M
• If your drone is intended for specific tasks like aerial photography or
surveying, integrate and configure the payload accordingly.
11.Deployment   1M
Deploy the drone for autonomous navigation missions, monitoring its
performance and making adjustments as needed.
********** 15 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper 8cc0d9cb7e13

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_Computer_7032/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper e854d79b664e

- Departments: Information Technology
- Programmes: Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_IT_7037/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 May 2026
- Text: mixed (14 pages), mean OCR confidence 93.4

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 15 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Summarize the classification of Drone.   [05]
• Weight/Size
• Range
• Aerodynamic
•   Single-rotor UAV: Uses one main rotor (like a
helicopter); efficient for heavy payloads but
mechanically complex.
• Flapping-wing UAV: Mimics bird or insect flight using
flapping wings; mainly used for research and bio-
inspired studies.
• Fixed-wing UAV: Has rigid wings like an airplane;
offers long endurance and high-speed flight but needs a
runway or launcher.
• Multi-rotor UAV: Uses multiple rotors (quad, hexa,
octa); easy to control, capable of vertical takeoff and
hovering.
• Hybrid UAV: Combines fixed-wing and rotor features;
supports vertical takeoff with efficient forward flight
********** 1 **********
--- page 2 ---
CO-2, SO-1, BL-2   b.   Explain the impact of battery size, weight and capacity on drone   [05]
flight.
CO-3, SO-1, BL-3   c.   Explain the role of the Inertial Sensor in a drone / UAV.   [05]
Accelerometer measures linear acceleration (forward/backward,
up/down, side-to-side) and helps determine tilt and movement.
Gyroscope measures angular velocity (rotation around X, Y, Z
axes) and helps track how fast the drone is rotating, essential for
stabilization and smooth turning.
Magnetometer helps with heading direction and acts like a
compass by measuring heading relative to Earth’s magnetic
field.
Without inertial sensors, the drone would not know its
orientation and may drift uncontrollably and the stable flight
would be nearly impossible. The inertial sensor continuously
measures how the drone is moving and rotating in 3D space. It
enables the drone to maintain stable flight, detect changes in
********** 2 **********
--- page 3 ---
direction, balance itself automatically and execute precise
manoeuvres.
CO-4, SO-1, BL-3   d.   Define Proportional, Integral, and Derivative controllers and   [05]
analyze their roles in ensuring stable and autonomous flight of a
quadcopter.
[Def-1M each and 2M-Roles]
Proportional (P) Controller:
The proportional controller generates an output that is directly
proportional to the current error (difference between desired and
actual state). It provides immediate corrective action, helping the
quadcopter quickly respond to disturbances such as wind or
sudden tilting. A higher proportional gain (Kp) improves
responsiveness but may cause oscillations if too large, while a
low Kp leads to a slow and weak response.
Integral (I) Controller:
The integral controller considers the accumulation of past errors
over time. Its main role is to eliminate steady-state error,
ensuring that the quadcopter eventually reaches and maintains
its desired position or orientation (e.g., perfectly hovering at a
fixed height). However, excessive integral gain (Ki) can lead to
overshoot and instability, often causing slow oscillations.
Derivative (D) Controller:
The derivative controller predicts future error by considering the
rate of change of the error. It acts as a damping mechanism,
reducing overshoot and oscillations by slowing down the system
as it approaches the desired state. A properly tuned derivative
gain (Kd) improves stability, but too high a value can make the
system sensitive to noise and cause erratic behaviour.
Role in Stable and Autonomous Flight:
Together, these three controllers ensure smooth and controlled
flight. The proportional component provides fast correction, the
integral component ensures accuracy by removing persistent
errors, and the derivative component enhances stability by
damping oscillations.
Attempt any four.   [80]
Q2   a.   Explain FPV drones. Which additional components are required   [10]
CO-1, SO-1, BL-2   in a FPV drone and for what purpose?
********** 3 **********
--- page 4 ---
* It has a small camera in the front that sends
live video to a screen or special goggles worn by
the pilot.

* The pilot uses a remote controller to fly the
drone while watching the video feed.

* It feels like you are sitting inside the drone and
flying it yourself.

FPV Drones FPV -First-Person View.

FPV means First Person View — seeing through the eyes of the drone using goggles
Designed at our Institute

FPV Goggles

* Live video feed from the drone’s onboard camera to the
pilot’s eyes.
* Helps in precise navigation, especially in racing.

Camera > Video Transmitter (VTX) > Goggles Receiver >
Display in goggles.

Q2 b. Describe all functions of a flight controller. [10]
CO-2, SO-1, BL-2

FIC 7) IC HOH
--- page 5 ---
Q3   a.   How does a drone's Return-to-Home (RTH) function work and   [10]
CO-3, SO-1, BL-3   why is it important? When does it get triggered in UAV/drone ?
Working-4 marks, importance-3 marks, trigger conditions -
3 marks
When the drone takes off, it uses Global Positioning System to
store its exact starting coordinates as the home point and the
Return-to-Home (RTH) function is a safety and navigation
feature that allows a drone to automatically fly back to its takeoff
/ home point and land.
During flight, the drone continuously tracks its location via GPS
and   its movement and   orientation using the   Inertial
Measurement Unit. These systems work together to know where
the drone is relative to home.
********** 5 **********
--- page 6 ---
Once RTH is activated (manually or automatically), the drone
Ascends   to a safe   altitude   (to avoid obstacles   like
trees/buildings), Calculates a direct path back to the home point,
Flies back automatically using GPS guidance, Descends and
lands precisely at or near the takeoff spot.
RTH gets triggered under following cases
1.Pilot presses an RTH button on the controller or app.
2.When battery reaches a critical level, the drone initiates RTH
to avoid crashing.
3.If connection between controller and drone is lost for a few
seconds, The drone autonomously returns instead of drifting
away.
4.Pre-configured system warnings
5.Some drones trigger RTH if sensors detect unsafe flight
conditions.
Q3   b.   Describe different types of drone security threats and their   [10]
CO-5, SO-1, BL-3   impact on public safety (atleast 5 types).
[ at least 5 -2M Each]
Unauthorized Surveillance
Drones equipped with cameras can be used to spy on individuals,
private properties, or sensitive locations without permission.
This leads to serious privacy violations and may result in leakage
of confidential or personal information, posing risks to both
individuals and national security.
Terrorist Attacks
Drones can be misused to carry explosives or hazardous
materials and target crowded public places, government
buildings, or critical infrastructure. Such attacks can cause loss
of life, destruction of property, and widespread panic among
people, creating major security concerns.
Smuggling and Illegal Transport
Drones are increasingly being used to transport illegal items
such as drugs, weapons, or contraband across borders or into
restricted areas like prisons. This facilitates criminal activities,
makes law enforcement more difficult, and threatens public
order and safety.
Signal Jamming and Spoofing
Attackers can disrupt drone communication through signal
jamming (blocking signals) or spoofing (sending fake signals).
This can result in loss of control, drone crashes, or even
hijacking, which can be dangerous in populated areas.
********** 6 **********
--- page 7 ---
Hacking and Cyber Attacks
Drones are vulnerable to hacking, where unauthorized users can
gain control over the system or access sensitive data. This can
lead to misuse of drones for illegal activities, data breaches, and
serious cybersecurity threats.
Collision with Aircraft
Improper use of drones near airports or restricted airspace can
lead to collisions with manned aircraft. Such incidents can cause
severe aviation accidents, endangering the lives of passengers
and crew and disrupting air traffic operations.
Swarm Attacks
Multiple drones can be coordinated to operate as a swarm,
overwhelming security systems and making detection and
prevention difficult. These attacks have the potential to cause
large-scale damage,   especially when   targeting   critical
infrastructure.
Q4   a.   In the drone flight why two motors are required to rotate in clock   [10]
CO-1, SO-1, BL-2   wise and remaining two in anticlockwise direction? Explain.
When a motor rotates a propeller, it produces a reaction torque
on the drone body according to Newton's Third Law of Motion.
If all four motors rotated in the same direction, the drone body
would spin uncontrollably in the opposite direction. To prevent
this spinning, two motors rotate clockwise (CW) and the other
two rotate counter-clockwise (CCW). The torques produced by
these opposite rotations cancel each other, keeping the drone
stable. Equal opposite rotations ensure that the net rotational
force around the vertical axis is zero, allowing the drone to hover
without rotating To rotate the drone intentionally, the flight
controller slightly increases the speed of one pair of motors and
decreases the speed of the opposite pair. This creates a small
torque difference that causes the drone to yaw (rotate) in the
desired direction. This CW–CCW motor configuration allows
the drone to maintain balance, directional control, and smooth
flight, which is essential for quadcopters used in photography,
surveillance, and research
Q4   b.   Describe the process of distribution of power in a drone using a   [10]
CO-2, SO-1, BL-2   diagram.
Diagram - 5 marks, explanation - 5 marks
********** 7 **********
--- page 8 ---
PDB: It distributes power from battery to various components of
drone.
ESC: It regulates the power to the motor based on control signals
from the controller.
Q5   a.   What is the role of Physics in drone flight? Explain in short.   [05]
CO-1, SO-1, BL-2   Drone flight physics is based on the balance of forces acting on
the drone and the principles of Newton's Laws of Motion. The
propellers rotate at high speed and push air downward,
generating upward thrust that lifts the drone. When the thrust
equals the drone’s weight, it hovers; when thrust is greater than
weight, it ascends, and when it is less, it descends. By varying
the speed of individual motors, the drone changes its orientation
through roll, pitch, and yaw, allowing it to move forward,
backward, sideways, or rotate. Thus, drone flight depends on
controlled thrust, balanced torque, and aerodynamic forces.
Q5   b.   Illustrate how the accelerometer, gyroscope, magnetometer and   [15]
CO-3, SO-1, BL-3   barometer work together to ensure stable and accurate flight in a
UAV / drone.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time. Accelerometer
(measures linear motion) detects acceleration along X, Y, Z axes
and helps determine tilt (pitch & roll) using gravity direction. It
is useful for detecting sudden movements. Limitation: Noisy
and affected by vibrations. Magnetometer (acts like a compass)
********** 8 **********
--- page 9 ---
measures Earth’s magnetic field giving absolute heading (yaw
direction).   Limitation: Disturbed by nearby metals or
electronics. Barometer (measures altitude) measures air pressure
to estimate height, it helps maintain stable altitude (hovering).
Limitation: Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   What features are required in racer and non-racer drones?   [10]
CO-2, SO-1, BL-2   Compare and justify the differences in motor specifications for
racer and non-racer types of drones(7 parameters).
Q6   b.   Explain the roles of wireless camera and modem units in drone   [10]
CO-4, SO-1, BL-3   operation, and design a communication framework integrating
them to ensure efficient and reliable flight.
*[Roles-4M, Framework-6M]
Roles:
The wireless camera unit is responsible for capturing real-time
video and images during flight and transmitting them to the
ground station. It enables applications such as surveillance,
mapping, inspection, and navigation. The live video feed helps
the operator monitor the drone’s surroundings, avoid obstacles,
and make control decisions.
The modem unit provides the communication link between the
drone and the ground control station (GCS). It transmits and
receives data such as control commands, telemetry (altitude,
speed, GPS location), and system status. The modem ensures
long-range communication,   reliable data   transfer, and
coordination between drone components
Framework:
********** 9 **********
--- page 10 ---
1. Integrating key components
• The communication framework of a drone is designed by
integrating key components such as the flight controller,
wireless camera, modem/telemetry unit, and ground
control station (GCS). The flight controller acts as the core
processing unit, managing motor control and sensor data.
• The wireless camera captures real-time video and transmits
it to the ground station, while the modem or telemetry unit
enables communication between the drone and the GCS.
The ground control station serves as the user interface for
monitoring   flight   parameters and   sending   control
commands.
2. Data flow:
• The data flow in this framework is divided into uplink and
downlink communication.
• In the uplink (from ground to drone), control commands
such as throttle, roll, pitch, and yaw are transmitted through
the modem to the flight controller.
• In the downlink (from drone to ground), telemetry data
including GPS position, battery status, and altitude is sent
back via the modem, while the live video stream is
transmitted separately through the wireless camera system.
3. Integrated framework
• In the integrated framework, the camera module is
connected to a video transmitter (VTx), which sends the live
video feed to a receiver at the ground station. The modem is
interfaced with the flight controller to handle bidirectional
communication, including both control commands and
telemetry data.
• To ensure reliable performance, the video transmission and
telemetry communication operate on separate frequencies or
channels to prevent interference. Additionally, an onboard
processing unit can be incorporated to combine camera and
sensor data, enabling intelligent decision-making and
supporting advanced autonomous drone operations.
Q7   Design and develop a quadcopter with a multispectral camera   [20]
CO-4, SO-1, BL-3   and LiDAR using OpenCV, Raspberry Pi, and Pixhawk for
precision agriculture, and evaluate its effectiveness in crop
health monitoring, irrigation management, and yield prediction.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
********** 10 **********
--- page 11 ---
Block diagram of the drone and the signal flow between its
components
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk flight controller is
the central component that manages flight control,
navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size, and
payload capacity.
3. Motors and Propellers: Choose motors and propellers that
provide the required thrust for your drone.
4. ESCs   (Electronic Speed   Controllers):   Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power your
drone for the desired flight time.
6. Raspberry Pi captures multispectral images and LiDAR
scans. OpenCV processes images in real-time for NDVI and
********** 11 **********
--- page 12 ---
plant detection. Data is stored onboard or transmitted via
telemetry to GCS. Post-processing generates crop health
maps, irrigation zones, and yield predictions.
7. Sensors: Depending on your navigation requirements, add
sensors like GPS, IMU (Inertial Measurement Unit), Lidar,
Multispectral Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
LiDAR (Light Detection and Ranging)
• Uses laser pulses to generate high-resolution 3D maps of
the terrain or crop canopy. Supports height measurement,
obstacle detection, and precision mapping.
Multispectral Camera
• Captures images in multiple bands (RGB + NIR) to
analyze plant health, vegetation indices (NDVI), and crop
stress. Useful for monitoring crop growth and detecting
disease.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
1. Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
missionParameters.
********** 12 **********
--- page 13 ---
2. Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
1. Crop Health Monitoring:
o NDVI maps identify areas with stressed
vegetation.
o Early detection of nutrient deficiencies, pest
infestations, or disease spread.
2. Irrigation Management:
o 3D terrain mapping from LiDAR allows
calculation of water runoff and soil moisture
zones.
o Optimizes irrigation by targeting areas that need
water, reducing waste.
3. Yield Prediction:
o Combines canopy cover, plant height, and NDVI
data over time to model crop growth.
o Provides predictive analytics for expected yield
per plot or hectare.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
********** 13 **********
--- page 14 ---
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evluation-2M
Application   Benefit   Evaluation Metrics
Crop Health Detect   stressed NDVI   maps,   disease
Monitoring   crops early   detection   accuracy,
stress identification rate
Irrigation   Efficient   water Soil   moisture   maps,
Management usage,   reduced irrigation   efficiency,
wastage   water saving percentage
Yield   Predict   harvest Accuracy   of   growth
Prediction   output   and prediction,   canopy
optimize planning   density   correlation,
actual vs predicted yield
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper cefedafa3e2b

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_Computer_7002/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 Feb 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (CIVIL)/B. Tech (COMP)/B. Tech
(CS)/B. Tech (CSE - CS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(DS)/B. Tech Intg. (IT)/B. Tech Intg. (Mech)/B. Tech (IT)/B. Tech (MECH)/B. Tech
(MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA Tech (DS)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 12 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No. Part A is compulsory.
5. Out of the remaining questions From Part B, Attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
1.   Part A Compulsory   20M
CO-1 ;   A.   Explain the role of lift, thrust, drag, and weight on a UAV in flight and   [5]
BL-2   analyze how these forces vary under different flight conditions.
*[Lift-1M, Thrust-2M, drag-1M, weight-1M]
Lift
•   For drones with horizontal rotors (like quadcopters),   lift is
essentially the vertical component of thrust that counteracts
gravity, allowing the drone to rise, hover, or descend.
•   In fixed-wing drones, lift is generated by the wings due to air
pressure differences.
Changes with conditions:
•   Faster flying = more lift.
•   Higher altitude = less air, so lift decreases.
• When turning, lift may need to increase to avoid losing altitude.
Thrust
•   Thrust is the forward or upward force generated by the propellers
that pushes air downwards, creating an equal and opposite reaction
that lifts the drone.
Changes with conditions:
• Hovering = thrust just equals weight.
• Climbing = thrust must be higher than drag to go up.
•   Fast flight = more thrust needed to overcome drag.
Drag
•   It is the aerodynamic resistance a drone experiences when moving
through air. It opposes the drone’s forward motion and is caused
********** 1 **********
--- page 2 ---
by the drone’s body, propellers, and any payload disrupting
airflow.
Changes with conditions:
•   Higher speed = drag increases a lot.
• Low speed = drag is less, but the drone may need to tilt more to
maintain lift.
•   Turns or maneuvers = drag increases.
Weight
•   Weight is the gravitational force acting downward on a UAV due
to the mass of all its components. It always acts vertically toward
the center of the Earth and opposes the upward lift produced by the
propellers or wings.
•   The magnitude of weight is given by the formula: W=m×g.
Changes with conditions:
•   Weight itself doesn’t change unless the payload changes.
•   During turns or acceleration, the drone “feels heavier,” so more lift
may be needed.
CO-2 ;   B.   Explain propeller pitch in drone design and compare the high-pitch Vs low-   [5]
BL-1,2   pitch propellers.   *[Explanation-1M, Comparison 4 pts-4M]
Propeller pitch refers to the distance (in inches or cm) that the propeller
would move forward during one complete revolution if it were moving
through a solid medium
Pitch Design:
High-Pitch Propellers:
•   High-pitch propellers have a steeper angle of attack, meaning the
blades are pitched at a greater angle relative to the plane of rotation.
This design allows them to generate more thrust per revolution
compared to low-pitch propellers.
Low-Pitch Propellers:
•   Low-pitch propellers have a shallower angle of attack, with blades
pitched at a lesser angle. As a result, they generate less thrust per
revolution compared to high-pitch propellers.
Thrust Output:
High-Pitch Propellers:
•   High-pitch propellers are designed to provide higher thrust output
at the expense of efficiency. They are more suitable for applications
requiring high-speed flight or heavy payloads.
Low-Pitch Propellers:
•   Low-pitch propellers produce less thrust per revolution but are
more efficient in converting power into forward motion. They are
commonly used in applications where endurance and efficiency are
prioritized over sheer thrust, such as aerial photography or long-
range flights.
Speed Vs Efficiency
High-Pitch Propellers:
• Due to their ability to generate, high thrust levels, high-pitch
propellers are often used in applications where speed and
acceleration are critical, such as racing drones or high-performance
********** 2 **********
--- page 3 ---
aircraft. However, they may consume more power and have
reduced flight times compared to low-pitch propellers.
Low-Pitch Propellers:
•   Low-pitch propellers are preferred for applications where
endurance and efficiency are paramount. They can help maximize
flight time by requiring less power to maintain flight, making them
suitable for tasks like aerial surveillance, mapping, or search and
rescue operations.
Flight Characteristics:
High-Pitch Propellers:
•   High-pitch propellers tend to provide more aggressive and
responsive flight characteristics, allowing for quick acceleration,
sharp maneuvers, and rapid changes in altitude. They are favored
by experienced pilots who prioritize agility and performance.
Low-Pitch Propellers:
•   Low-pitch propellers offer smoother and more stable flight
characteristics, making them well-suited for applications requiring
precise control, steady hovering, and smooth aerial footage
capture.
CO- 3;   C.   Explain the drone flight features Fail-Safe, Loiter, and Return-to-Home   [5]
BL-2,3   (RTH). Discuss how each feature improves flight safety and mission
reliability, with examples of situations where they prevent accidents or
drone loss.   *[Each Features - 1M each and example-2M]
Fail-safe
• It is a protective feature that automatically activates a predefined action
when the drone loses control signal, GPS, or encounters critical system
failures.
• When communication between the transmitter and flight controller is
lost, or battery voltage drops below a safe limit, the fail-safe system
triggers Hover in place, Land immediately, Return-to-Home (RTH)
• Prevents flyaways (uncontrolled drift after signal loss).
• Minimizes crash risk due to uncontrolled descent.
• Protects payloads and onboard sensors by ensuring a controlled
response.
Ex: A drone used for bridge inspection flies behind a large pillar and
loses radio connection.
Loiter
• This mode also known as Position Hold allows the drone to maintain a
fixed GPS position and altitude, automatically adjusting for wind and
drift using its GPS, barometer, and inertial sensors.
In Loiter mode
• Flight controller continuously corrects position and altitude.
• The drone hovers in a stable position, allowing the pilot to take
hands off the controls.
• Prevents drift in windy conditions.
• Allows safe pause during missions (e.g., when obstacles or
interference are detected).
• Helps in emergency hover while the operator re-establishes link or
situational awareness.
********** 3 **********
--- page 4 ---
Ex: Prevents the drone from entering uncertain GPS zones or colliding
with obstacles.
Return-to-Home Mode
• Return-to-Home (RTH) is an autonomous feature that commands the
drone to fly back to its take-off point (home position) when triggered
manually or automatically
• Prevents loss of the drone due to long-range or signal interruptions.
• Ensures automatic recovery when pilot loses visibility or control.
Ex: The drone climbs to 50 m, returns along a safe route, and lands near
the launch pad.
CO- 4;   D.   Define the term autonomous UAV flight. Analyze the major challenges in   [5]
BL-4   achieving fully autonomous UAV operation.
*[ Def-1M, any 4 challenges decription-4M]
Autonomous UAV flight refers to the capability of a drone to perform flight
operations without direct human control, using onboard sensors,
processors, and pre-programmed algorithms to make real-time decisions.
In this mode, the UAV can plan its path, navigate, avoid obstacles, maintain
stability, and complete assigned missions—such as surveillance, mapping,
or delivery—based on data from systems like GPS, IMUs, cameras, and
LiDAR.
Challenges:
Limited Payload Capacity
•   Mini quadcopters have strict weight limitations, restricting the
integration of advanced sensors, processors, and communication
modules.
Power and Battery Constraints
•   Smaller drones have smaller batteries, leading to limited flight
times
Inaccurate and Noisy Sensor Data
•   Mini quadcopters rely on lightweight sensors (IMU, optical flow,
ultrasonic) that may have lower accuracy compared to larger
drones.
Computational Limitations
•   Mini quadcopters have low-power microcontrollers or embedded
processors, restricting the complexity of onboard AI algorithms.
Environmental Factors
•   Mini quadcopters are more sensitive to external disturbances like
wind and electromagnetic interference.
Communication and Network Dependency
•   Mini drones often rely on WiFi or Bluetooth for control and data
transmission, which has limited range and potential interference.
2.   Part B (Attempt Any 4)   80M
1.   [20]
CO-1;   A.   Define Flight Controller. Explain its main functions and describe how it   [10]
BL-2   helps a drone to stay stable during flight.
*[Def-1M, Each function-1.5M, stability explanation -1.5M]
********** 4 **********
--- page 5 ---
A flight controller is the central processing unit of a drone that regulates
its movement, stability, and navigation.
1.Attitude Stabilization (Auto-Leveling & Orientation Control)
•   Uses gyroscope and accelerometer (IMU) to maintain yaw, pitch,
and roll stability.
•   Automatically adjusts motor speeds to counteract disturbances
(e.g., wind).
•   Ensures smooth and stable flight in manual and autonomous modes.
•   Essential for hovering, takeoff, and landing precision.
2. Motor Control & Throttle Management
•   Sends PWM signals to Electronic Speed Controllers (ESCs) to
adjust motor speeds.
•   Regulates thrust distribution for different maneuvers (e.g.,
climbing, turning).
•   Enables precise altitude hold and directional movement.
•   Ensures efficient power management for better flight endurance.
3. Sensor Data Processing & Fusion
•   Collects real-time data from IMU, GPS, barometer, and LiDAR.
•   Uses sensor fusion algorithms to improve flight accuracy.
•   Enhances navigation precision, even in GPS-denied environments.
•   Helps in collision avoidance and terrain-following applications.
4.Autonomous Navigation & GPS Integration
•   Processes GPS waypoints for autonomous missions   (e.g.,
surveying, inspections).
•   Assists in return-to-home (RTH) and fail-safe operations.
•   Enables long-range autonomous   flights   for mapping and
monitoring tasks.
•   Improves flight safety by preventing loss of control.
5. Communication & Telemetry Management
•   Exchanges real-time data with ground control stations (GCS) via
telemetry modules.
•   Sends live flight parameters like altitude, speed, and battery status.
•   Allows remote monitoring and control via radio or WiFi links.
•   Supports mission planning and real-time adjustments for drone
The FC constantly monitors sensor feedback to detect any unwanted tilt or
deviation. It automatically adjusts motor speeds to restore balance and
keep the drone level in the air. This real-time correction allows the drone
to hover steadily, resist external disturbances, and execute smooth,
controlled maneuvers.
CO-2;   B.   I. Why LiPo   batteries   are commonly   preferred   for   drones.   [10]
BL-3   Discuss the key parameters to consider when selecting a battery for a
UAV.
II. Consider 2 quadcopters, each equipped with a motor rated 1000 RPM/V
and powered by a 12V battery. Assume air density ρ= 1.225 kg/m³
• Quadcopter A uses a 9 × 4.5-inch propeller , Assume CT=0.11
• Quadcopter B uses a 9 × 5-inch propeller , Assume CT=0.12
a. Calculate the approximate thrust generated by each configuration.
b. Compare the results and analyze how the difference in propeller
pitch and diameter affects lift, responsiveness, and overall flight
efficiency
*[Reason of LiPo-2M, any 5 Key parameters-4M, Numerical-4M]
********** 5 **********
--- page 6 ---
• Lithium Polymer batteries are due to their high energy density,
lightweight, and ability to provide high discharge rates.
key parameters for battery
•   Voltage (V)
•   Capacity (mAh or Ah)
•   Continuous discharge rating (C)
•   Peak discharge rating
•   Weight
•   Physical size / connector type / balance lead
•   Safety features & handling
1) *[4M- Formula-1M, Thrust calculation-1M each and analysis-1M]
Calculate Motor RPM
Convert RPM to Revolutions per Second (rps)
Convert Propeller Diameter to Meters
Calculate Thrust
Quadcopter A
TA ≈ 14.7 N per motor
Quadcopter B
TB ≈ 16 N per motor
2)
Quadcopter A: Slightly lower thrust, more responsive at low speeds
Quadcopter B: Higher thrust, better lift and climb, slightly less efficient in
hover
2.   [20]
CO-3;   A.   Explain the role of the Transmitter and Receiver systems in UAV   [10]
BL-2,3   operations. Discuss how they enable control between the UAV and ground
control station. Draw a labelled Transmitter–Receiver block diagram
showing the flow of control signals and data.
*[Role-3M each, Diagram-4M]
Transmitter (Ground Side)
The transmitter is a device at the ground control station that sends control signals
to the UAV.
Function:
1. Converts pilot’s input (joystick movements, switches, autopilot
commands) into electrical signals.
2. Modulates these signals for wireless transmission using radio
frequencies (RF).
3. Sends the signals to the UAV over the air.
********** 6 **********
--- page 7 ---
Role in UAV Operations:
• Ensures the pilot can command UAV movement: throttle, pitch, roll,
yaw, and other actions.
• Transmits important mission commands such as waypoint navigation
for autonomous flight.
Receiver (UAV Side)
The receiver is the UAV component that receives signals from the
transmitter and converts them into commands for the UAV’s flight
controller.
Function:
1. Captures the radio signals sent by the transmitter.
2. Demodulates the signals back into usable control commands.
3. Sends these commands to the UAV’s flight controller, which adjusts
motor speed, servos, or other actuators accordingly.
Role in UAV Operations:
• Ensures the UAV responds accurately and promptly to pilot inputs.
• Provides a feedback link (if bidirectional) for telemetry data like
battery status, GPS location, and UAV health.
Block diagram
CO-4;   B.   Define a PID controller and explain the role of its Proportional (P), Integral   [10]
BL-4,5   (I), and Derivative (D) components in drone flight control. Analyze and
evaluate the effects of under tuned and over tuned PID gains on drone
behavior.   *[Def-1M, Function of each-1.5M, Effect-1.5M each]
A PID controller (Proportional–Integral–Derivative controller) is a
feedback control system used to maintain a desired output by continuously
adjusting the control input based on the error between a setpoint (desired
value) and the measured process variable (actual value).
In drones, PID controllers are widely used in flight control systems to
stabilize roll, pitch, yaw, and altitude by regulating motor speeds.
A. Proportional (P)
•   Function: Produces an output proportional to the current error.
•   Effect on flight: Corrects deviations in roll, pitch, yaw, or altitude
immediately.
********** 7 **********
--- page 8 ---
•   High Kp: Strong immediate correction, faster response.
• Low Kp: Drone responds sluggishly; may drift from setpoint.
B. Integral (I)
•   Function: Accumulates past errors over time and eliminates steady-
state error.
•   Effect on flight: Corrects small persistent offsets (e.g., drift caused
by unequal motor thrust or wind).
•   High Ki: Corrects errors quickly but may introduce oscillations or
overshoot.
• Low Ki: Steady-state error persists; drone may slowly drift.
C. Derivative (D)
•   Function: Responds to the rate of change of error, predicting future
error.
•   Effect on flight: Dampens oscillations, smooths movements, and
improves stability.
•   High Kd: Strong damping; prevents overshoot but may make
response sluggish.
• Low Kd: Drone may oscillate or wobble due to momentum.
3.   [20]
CO-1;   A.   Define a Power Distribution Board (PDB) and Electronic Speed Controller   [10]
BL-2   used in drones and explain its need in UAV operations. Draw a labelled
connection diagram showing the interconnections between the battery,
ESCs, motors, and flight controller through the PDB in a quadcopter.
*[ Def-1M each , need-2.5M each , Diagram-4M]
PDB
A Power Distribution Board (PDB) is a centralized electrical hub in a drone
that distributes electrical power from the main battery to all electronic
components. It simplifies wiring, reduces clutter, and ensures each
component receives stable and reliable voltage and current.
Need
Centralized Power Management:
•   Eliminates the need for multiple direct connections from the battery
to individual components.
•   Simplifies the drone’s wiring layout.
Reliable Power Delivery:
•   Ensures ESCs, flight controller, and payloads receive consistent
voltage and current required for stable flight.
Safety and Protection:
•   Supports fuses, current-limiting circuits, and voltage regulators to
prevent overcurrent, short circuits, or damage to electronics.
Supports Payloads and Accessories:
• Allows connection of additional electronics such as cameras,
LiDAR, GPS, and companion computers   safely, without
overloading the system.
Simplified Maintenance and Troubleshooting:
•   Organized connections make it easier to inspect, repair, or upgrade
components without disturbing the entire wiring system.
Simplified Wiring & Maintenance:
•   Neatly organizes connections, making troubleshooting easier.
• Reduces weight and clutter from multiple wires running from the
battery.
********** 8 **********
--- page 9 ---
ESC
An ESC is an electronic device that controls the speed, direction, and
braking of a brushless motor in a drone.
Functions:
• Converts low-power signals from the flight controller into high-power
PWM signals for the motors.
• Adjusts motor speed in real time for stabilization and maneuvering.
• Provides safety features like overcurrent or thermal protection.
CO-2;   B.   Compare the key features and functionalities of BLHeli_32 and BLHeli_S   [10]
BL-2,3   ESC firmware. Based on your analysis, recommend which firmware is best
suited for a high-speed racing drone and which for a medium-sized
autonomous quadcopter. Justify your choices.
*[Comparison of any 5 points-5M, Identify-1M, reason-4M]
Feature   BLHeli_S   BLHeli_32
Processor   8-bit MCU   32-bit MCU
PWM, OneShot,   PWM, OneShot, MultiShot, DShot
Input Protocols   MultiShot,   (full support, up to DShot1200)
DShot (limited)
Update Rate   Up to 8 kHz   Up to 32 kHz
Telemetry   Limited   Advanced telemetry (RPM, current,
Support   temperature)
Current Sensing   Basic   High-precision   current   sensing;
allows power monitoring
Advanced motor timing control;
Motor Timing   Fixed or adjustable   dynamic   timing   adjustments
possible
Highly configurable; allows per-
Configurability   Basic   motor settings, advanced damping,
startup, and braking options
• BLHeli_32 is more advanced, configurable, and precise than
BLHeli_S due to its 32-bit architecture and support for modern
communication protocols and telemetry.
• High-speed racing drones need fast response, minimal latency, and
smooth motor control- BLHeli_32 is ideal.
• Medium-sized autonomous drones   benefit from   telemetry,
reliability, and programmable ESC behavior -BLHeli_32 is also
preferred.
********** 9 **********
--- page 10 ---
4.   [20]
CO-1;   A.   Explain the applications of drones in military and commercial sectors,   [5]
BL-2   highlighting their key roles and benefits in each domain.
*[ Each application-2.5M each (role-1.5M and benefits-1M)]
Military Applications:
Drones play a crucial role in modern defense operations due to their ability
to operate in high-risk environments without endangering human lives.
Key applications include:
• Surveillance   and   Reconnaissance:   Gathering   intelligence,
monitoring enemy movements, and conducting border patrols.
• Target Acquisition and Strike: Armed drones can engage targets
with precision, reducing collateral damage.
• Electronic Warfare: Intercepting communications, jamming enemy
signals, or performing electronic snooping.
• Logistics and Supply Delivery: Transporting supplies to remote or
dangerous locations.
Benefits in Military:
•   Reduced risk to personnel.
•   Cost-effective compared to manned aircraft.
•   Extended operational range and endurance.
•   Real-time data collection and battlefield awareness.
Commercial Applications:
In the commercial sector, drones are increasingly used to improve
efficiency, reduce costs, and enhance data collection.
Key applications include:
•   Aerial Photography and Videography: For media, marketing, and
cinematography.
•   Agriculture: Crop monitoring, spraying fertilizers/pesticides, and
precision farming.
•   Infrastructure Inspection: Monitoring bridges, power   lines,
pipelines, and telecom towers.
•   Delivery Services: Transporting goods, medical supplies, and
packages to hard-to-reach areas.
•   Environmental Monitoring: Wildlife surveys, forest management,
and disaster assessment.
Benefits in Commercial Use:
•   Faster and safer operations in difficult terrains.
•   Cost savings compared to traditional methods.
•   High-resolution and real-time data collection.
•   Enhanced operational efficiency and productivity.
CO-3;   B.   Define a sensor in the context of UAV and explain its role in achieving   [15]
BL-3   flight stability and autonomous operation. List the key sensors commonly
integrated in drones. Select any 3 sensors and analyze their working
principle, placement on the UAV and Contribution to UAV performance.
*[Def-1M, Role-3M, List-2M, sensor explanation-3M each]
• A sensor is a device that detects and measures physical or
environmental parameters and converts them into signals that the
UAV's flight control system can interpret.
•   Sensors provide critical information about the UAV's orientation,
position, speed, environment, and system health, which is essential for
maintaining flight stability, navigation, and autonomous operations.
Role
1. Flight Stability:
********** 10 **********
--- page 11 ---
Sensors such as gyroscopes, accelerometers, and barometers provide
real-time feedback on orientation, acceleration, and altitude. This
feedback allows the flight controller to make precise adjustments to the
motors and control surfaces to maintain stable flight.
2. Autonomous Operation:
Sensors enable autonomous navigation by detecting obstacles, mapping
terrain, measuring GPS position, and sensing environmental conditions.
This allows UAVs to perform tasks like waypoint navigation, obstacle
avoidance, and automated landing without human intervention.
Key Sensors Commonly Integrated in Drones
• Inertial Measurement Unit (IMU)
• GPS Module
• Barometer: Magnetometer (Compass)
• Ultrasonic / LiDAR Sensors
• Vision / Camera Sensors
• Infrared / Thermal Sensors
*Student may explain any 3
IMU (Accelerometer + Gyroscope)
Accelerometer: Measures linear acceleration along X, Y, Z axes using a
mass-spring system.
Gyroscope: Measures angular velocity using MEMS vibration or spinning
mass principle.
Contribution :
Provides orientation, tilt, and motion data critical for stability, hovering,
and smooth maneuvering.
GPS Module
It uses signals from multiple satellites to calculate the UAV’s latitude,
longitude, and altitude through trilateration.
Contribution :
Enables waypoint navigation, geofencing, and autonomous routing.
Essential for outdoor operations.
LiDAR / Ultrasonic Sensor
LiDAR: Emits laser pulses and measures the time of flight to detect
distance.
Ultrasonic: Emits sound waves and measures echo time to calculate
distance.
Contribution :
Enables collision avoidance, precise landing, and obstacle-aware
autonomous flight.
5.   [20]
CO-2;   A.   Define the thrust-to-weight ratio and explain its effect on a drone’s flight   [10]
BL-2,3   performance and energy efficiency. For a 3 kg quadcopter, calculate the
required thrust per motor for hovering. Relate your explanation to the UAV
flight forces – lift, thrust, drag, and weight.
*[Def-1M, Effect-3M, Calculation-4M, Relation-2M]
The thrust-to-weight ratio of a drone is the ratio of the total thrust produced
by its motors to the weight of the drone.
Effect on Flight Performance and Energy Efficiency:
1. Flight Performance:
• T/W > 1: Drone can ascend vertically, hover stably, and perform agile
maneuvers.
• T/W = 1: Drone can hover, but has no vertical acceleration margin.
********** 11 **********
--- page 12 ---
• T/W < 1: Drone cannot lift off.
2. Energy Efficiency:
• Higher thrust for the same weight - higher power consumption -
shorter flight time.
• Lower thrust (just enough to hover) - maximizes flight efficiency.
Calculate total weight in Newtons
For hovering, total thrust equals weight:
For a quadcopter:
Relation to UAV Flight Forces
• Lift: Must at least equal weight to hover; increasing thrust increases
effective lift.
• Thrust: Directly controls vertical and horizontal motion; higher thrust
allows climbing and faster acceleration.
• Drag: Affected indirectly; higher thrust can overcome drag during
forward flight.
• Weight: The opposing force; T/W ratio shows how much thrust is
available relative to weight.
CO-4;   B.   Define electronic snooping and mid-air collisions in drone communication   [10]
BL-5   systems. Evaluate the role of international drone regulations in mitigating
threats like illegal reconnaissance, electronic snooping, and mid-air
collisions, discussing their effectiveness and limitations.
* [Def-3M, Role-4M, effectiveness and limitations-1.5 each]
Electronic snooping:
Electronic snooping in drone communication systems refers to the
unauthorized interception or monitoring of a drone’s data transmissions,
including telemetry, control signals, or video feeds. It can compromise
privacy, reveal sensitive information, or allow malicious actors to take
control of the drone.
Mid-Air Collisions:
It occur when a drone collides with another aerial vehicle or object during
flight. Such collisions can cause damage to the drone, other aircraft, or
people on the ground, and may result from poor situational awareness, lack
of collision avoidance systems, or human error.
Role of International Drone Regulations:
International drone regulations aim to mitigate threats like illegal
reconnaissance, electronic snooping, and mid-air collisions through:
1. Airspace management: Restricting drone operations in sensitive
areas, near airports, or over crowds.
2. Communication and encryption standards: Ensuring secure control
links to prevent interception or hacking.
********** 12 **********
--- page 13 ---
3. Mandatory   registration   and   identification:   Facilitating
accountability and traceability of drones.
4. Operational limits: Specifying maximum altitude, speed, and visual
line-of-sight rules to reduce collision risks.
5. Mandatory safety technologies: Requiring drones to include
geofencing or detect-and-avoid systems in some regions.
Effectiveness: Regulations reduce incidents of unauthorized surveillance,
increase situational awareness, and promote safe drone integration into
airspace.
Limitations: Enforcement is challenging across borders; technological
countermeasures like signal jamming or hacking may bypass regulations;
and rapid innovation in drones often outpaces legal frameworks.
6.
CO-4;   A.   Design & Develop a quadcopter with a thermal and smoke detection sensor   [20]
BL-6   using OpenCV, Raspberry Pi, and a PixHawk controller for forest fire
detection. Evaluate its use in early warning systems, hotspot localization,
and fire spread mapping.
1. Define Requirements   1M
•   Clearly define the type of UAV (e.g., quadcopter, hexacopter, or
fixed-wing).
•   Mention payload requirements such as cameras, sensors, or
sprayers.
•   Specify flight endurance, range, altitude, and the mission
objectives (e.g., mapping, inspection, or monitoring).
2.Select Hardware component   3M
Component   Function
Lightweight, durable structure (carbon
Drone Frame
fiber recommended).
Handles stabilization, GPS navigation,
Pixhawk Flight Controller
and sensor fusion.
Raspberry Pi / Companion Runs AI, image processing (OpenCV),
Computer   and ML models.
Captures thermal data depending on the
Thermal camera
mission.
Generate thrust for lift and
Motors & ESCs
maneuverability.
LiPo Battery   Supplies power for all onboard systems.
Enable autonomous navigation and stable
GPS + IMU Sensors
flight.
********** 13 **********
--- page 14 ---
Specialized Sensors (e.g.,
Task-specific sensing
LiDAR, Gas, NDVI)
Enables live data, video, and command
Telemetry Module   exchange with Ground Control Station
(GCS).
3.Assemble the Drone:   1M
• Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability
4.Software Configuration:   3M
• Flash the Pixhawk flight controller with the appropriate firmware, such
as ArduPilot or PX4, and configure it for your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to ensure accurate
readings.
• Image capture & sync: timestamp thermal and RGB frames with PixHawk
telemetry.
• Thermal detection (OpenCV):
1. Convert thermal image to temperature map (if camera provides temps)
or normalized intensity.
2. Simple thresholding to find high-temperature blobs → connected
components for hotspot detection.
3. Morphological filters to remove noise.
Smoke detection:
1. Particle sensor (PM2.5) readings above threshold → flag potential
smoke.
2. Combine with thermal / RGB evidence to reduce false positives.
RGB verification / person or vehicle filter:
• Run lightweight object detection (MobileNet SSD / Tiny-YOLO) to
verify presence of flames, smoke plumes, or human activity near
hotspot.
• Geotagging: use PixHawk GPS + camera orientation to compute
lat/long of detection (bearing + slant range approximate from altitude).
Report coordinates to GCS.
• Mapping: Store images for post-flight thermal orthomosaic / time-
series to map fire spread using photogrammetry / mosaic stitching.
5.Mission Planning and Waypoints:   2M
• Use   mission   planning   software   (e.g.,   Mission   Planner,
QGroundControl) to define waypoints, flight paths, and mission
parameters.
• Set up geofencing and safety parameters to prevent the drone from
flying into restricted areas or in unfavorable conditions.
6. Implementation   5M
A. Early warning
• Smoke sensors can detect rising particulate levels; thermal detects
hotspots before visible flames.
• Drones can cover areas faster than ground teams, giving early
alerts.
Limitations
•   False positives from sun-heated rocks or industrial plumes—fusion
reduces this.
********** 14 **********
--- page 15 ---
B. Hotspot localization
• Geotagged thermal detections give coordinates to responders. RTK
improves localization to <1–3 m; normal GPS ≈ 5–15 m depending
on conditions.
Limitations
•   Geolocation error due to slant range & camera angle at high altitude
requires corrected geometry and calibration.
C. Fire spread mapping
• Thermal orthomosaics and time-series imagery map active fire
front and burnt area extent. This supports resource allocation and
risk modeling.
Limitations
• Photogrammetry accuracy decreases with smoke, dust, and low
visibility. Repeated sorties needed to monitor spread.
7. Telemetry and Ground Control Station:   1M
• Set up telemetry systems for communication between the ground
control station (GCS) and the drone.
• Use a GCS software to monitor the drone's status, update missions in
real-time, and take control when needed.
8. Testing and Calibration:   1M
• Conduct extensive testing in controlled environments to ensure the
drone's safety and navigation accuracy.
• Calibrate and fine-tune the drone's parameters, including PID
controllers, to optimize performance.
9.Safety Measures   1M
• Implement safety features like return-to-home (RTH) and fail-safe
modes to handle unexpected situations.
• Comply with local regulations and obtain necessary permissions for
autonomous flights.
10.Integration of Payload   1M
• If your drone is intended for specific tasks like aerial photography or
surveying, integrate and configure the payload accordingly.
11.Deployment   1M
• Deploy the drone for autonomous navigation missions, monitoring
its performance and making adjustments as needed.
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 14e17ca7413e

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CSE_DS_7057/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Identify the challenges in designing a Drone.   [05]
❑ Mechanical Design Challenges
Weight Optimization
❑ Power & Battery Management
Limited Battery Life
Power Distribution
❑ Communication & Control
Autonomous Navigation
Latency in Control Loops
Component Integration
CO-2, SO-1, BL-2   b.   Discuss the benefits of intermediate and advanced flight   [05]
controllers as compared to basic ones.
********** 1 **********
--- page 2 ---
CO-3, SO-1, BL-2   c.   What is the function of a barometer in a drone?   [05]
A barometer measures air pressure, which decreases as altitude
increases. Using this principle, the drone estimates how high it
is above the ground. Altitude estimation is done by converting
air pressure readings into height (altitude). barometer provides
continuous vertical position data.
Stable hovering helps the drone hold a fixed height without
constant pilot input which is essential for smooth, steady flight.
Vertical movement control detects whether the drone is
Climbing Descending, allowing precise control of up/down
motion.
The barometer (pressure sensor) in a drone is mainly used to
measure altitude and help the drone maintain a stable height
during flight.
Barometer values can be used with GPS and IMU to support
Return-to-Home (RTH), auto takeoff and landing and waypoint
navigation.
Barometer readings are affected by weather changes (pressure
variations), sensor values can drift over time.
CO-4, SO-1, BL-3   d.   Describe the functions of wireless camera and modem units in a   [05]
drone and analyze the challenges faced   in real-time
communication.
[Function of wireless camera and modem units-3M, Challenges-
2M]
The wireless camera is used to capture live video and images
during flight. It transmits real-time visual data to the operator,
which is essential for surveillance, navigation, mapping, and
inspection tasks. This allows the user to make immediate
********** 2 **********
--- page 3 ---
decisions based on what the drone sees, especially in
applications like search-and-rescue or security monitoring.
The modem unit (communication module) is responsible for
transmitting and receiving data between the drone and the
ground control system. It handles control signals (commands
sent to the drone) and telemetry data (such as altitude, speed,
GPS location, and battery status).   It ensures continuous
connectivity, enabling autonomous as well as manual control of
the drone.
Challenges include:
One major issue is signal interference, which can occur due to
obstacles, weather conditions, or other wireless devices
operating on similar frequencies. Another challenge is latency,
where delays in data transmission can affect timely decision-
making and control accuracy. Limited bandwidth can restrict
the quality of video streaming, leading to reduced resolution or
frame drops. Additionally, range limitations can cause
communication loss when the drone moves too far from the
controller. Ensuring data security   is also   critical, as
communication links may be vulnerable to hacking or
unauthorized access.
Attempt any four.   [80]
Q2   a.   How do the laws of physics govern the movement and stability   [10]
CO-1, SO-1, BL-2   of a drone during flight.
Role of Basic Forces
Drone flight is controlled by four main forces: thrust, gravity
(weight), drag, and lift. Thrust produced by the propellers
pushes air downward, creating an upward force that allows the
drone to rise. According to the laws of motion, every action
has an equal and opposite reaction. When the propellers push
air downward, the drone experiences an upward reaction force,
allowing it to lift and remain airborne. Increasing the speed of
the motors increases thrust, which allows the drone to ascend.
Decreasing thrust causes the drone to descend due to gravity.
Control of Direction and Motion. A drone changes direction
by varying the speed of individual motors. This creates
differences in thrust that cause the drone to tilt forward,
backward, or sideways, enabling motion in different directions.
Stability and Balance. Stability is maintained using onboard
sensors such as gyroscopes and accelerometers, which
constantly measure orientation and motion. The flight
controller automatically adjusts motor speeds to keep the drone
balanced and stable. Air resistance or drag affects the speed
********** 3 **********
--- page 4 ---
and efficiency of the drone. Proper design of propellers and
frame improves aerodynamic performance and flight stability.
Q2   b.   Explain the functions of ESC (any 5).   [10]
CO-2, SO-1, BL-2
Q3   a.   List and explain different types of RF communication modules   [10]
CO-3, SO-1, BL-2   used in drones?
RF (Radio Frequency) communication modules allow a drone to
send and receive data wirelessly—between the drone, the remote
controller, ground station, or other devices.
Depending of application different RF modules are used to
address the range, data rate and reliability.
Wi-Fi Modules based on standard Wi-Fi (2.4 GHz / 5 GHz) are
used in many consumer drones. They provide high data rate and
easy integration with application stacks (business layer)
Control Link uses 2.4 GHz or 915 MHz or 865mhz or 433 mhz
for low latency reliable control signals. These links provide long
range (1–10 km). these links have limited data bandwidth and
are used for control signals and cannot be used for video
streaming.
Telemetry Modules are again low bandwidth links meant for
data transfer between drone and base station. They are used for
Two-way communication to send data like GPS data, Battery
status, Speed, altitude etc. data is often exchanged using data
protocols like MAVLink.
Cellular Modules (4G/5G) uses mobile networks like 4G LTE
and 5G. they provide extremely long range (wherever network
coverage exists) and access to real-time cloud.
********** 4 **********
--- page 5 ---
Video Transmission Systems (First Person View - FPV) employs
dedicated RF systems for live video (often 5.8 GHz
analog/digital) for Low latency Real-time video feed. The only
issue is it has limited range and range extenders can increase
cost.
Q3   b.   Define drone security threats. Analyze the different types of   [10]
CO-5, SO-1, BL-3   drone security threats and Examine how these threats exploit
vulnerabilities in UAV systems (atleast 4 types).
[Def-2M, Security threats explanation any 4 2M each]
Drone security threats refer to any malicious or unauthorized
activities involving Unmanned Aerial Vehicles (UAVs) that
exploit system vulnerabilities to cause harm to people, property,
data, or national security.
Unauthorized Surveillance
Drones can be used for spying and unauthorized data collection
using onboard cameras and sensors. Attackers exploit the lack of
encryption and access control in data transmission systems to
capture sensitive images or videos. Weak privacy protections
and unsecured video links make such surveillance easier.
Terrorist Attacks
Drones can carry explosives or hazardous materials and be
directed toward targets. These attacks exploit navigation system
vulnerabilities (GPS dependence) and lack of geofencing
enforcement, allowing drones to enter restricted areas and
execute harmful operations.
Smuggling and Illegal Transport
Drones are used to transport contraband such as drugs or
weapons. Criminals take advantage of limited airspace
monitoring and absence of real-time tracking systems, enabling
drones to bypass traditional security measures and deliver illegal
goods undetected.
Signal Jamming and Spoofing
In this type of attack, communication signals between the drone
and controller are disrupted (jamming) or falsified (spoofing).
These threats exploit unsecured wireless communication
protocols and lack of authentication mechanisms, leading to loss
of control, redirection, or crashes.
Hacking and Cyber Attacks
Hackers can gain unauthorized access to drone systems and take
control or steal data. This occurs due to weak cybersecurity
measures, such as poor encryption, outdated firmware, or
insecure APIs, allowing attackers to manipulate drone
operations remotely.
********** 5 **********
--- page 6 ---
Collision with Aircraft
Drones flying in restricted airspace can collide with manned
aircraft. This risk arises from lack of airspace awareness systems
and poor integration with air traffic management, which allows
drones to operate without proper coordination or detection.
Swarm Attacks
Multiple drones can be coordinated to act as a swarm,
overwhelming   defense   systems. These   attacks   exploit
limitations   in detection and tracking technologies and
inadequate counter-UAV systems, making   it difficult to
neutralize multiple threats simultaneously.
Q4   a.   Explain the reason for using Brush less DC Motor in Drone.   [10]
CO-1, SO-1, BL-2
Q4   b.   Explain KV rating of a motor and its significance. Which other   [10]
CO-2, SO-1, BL-2   specifications are to be considered while selecting a motor for a
drone?
********** 6 **********
--- page 7 ---
Q5   a.   Explain the use of Newton’s law in Drone Flight.   [05]
CO-1, SO-1, BL-2   Drone flight works according to Newton’s laws, which explain
how forces produce motion. The rotating propellers push air
downward, creating an equal and opposite upward force that lifts
the drone. By increasing or decreasing the thrust of the motors,
the drone can take off, hover, or descend. Unequal thrust
between motors causes roll, pitch, and yaw, allowing the drone
to change direction and move in the air.
Q5   b.   Illustrate   the   role   of   the   accelerometer,   gyroscope,   [15]
CO-3, SO-1, BL-3   magnetometer and barometer in a UAV / drone. Explain the
concept of sensor fusion and discuss the advantage of sensor
fusion in flight control.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time.
********** 7 **********
--- page 8 ---
Accelerometer (measures linear motion) detects acceleration
along X, Y, Z axes and helps determine tilt (pitch & roll) using
gravity direction. It is useful for detecting sudden movements.
Limitation: Noisy and affected by vibrations.
Magnetometer (acts like a compass) measures Earth’s magnetic
field giving absolute heading (yaw direction).   Limitation:
Disturbed by nearby metals or electronics.
Barometer (measures altitude) measures air pressure to estimate
height, it helps maintain stable altitude (hovering). Limitation:
Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   Explain with a block diagram the flow of signals and power   [10]
CO-2, SO-1, BL-2   between transmitter and receiver.
********** 8 **********
--- page 9 ---
Q6   b.   Compare P controller, PI controller, PD controller, and PID   [10]
CO-4, SO-1, BL-3   controller for drone flight control and justify your choice based
on performance metrics.
[ Each controller- 2M Each and Justification-2M]
Proportional (P) controller provides a fast response with
simple implementation, but it suffers from steady-state error and
tends to produce high overshoot, making it only suitable for
basic stabilization.
Proportional-Integral (PI) controller improves accuracy by
eliminating steady-state error due to the integral action, which
makes it useful for tasks like altitude control; however, it results
********** 9 **********
--- page 10 ---
in slower response, increased overshoot, and longer settling
time.
Proportional-Derivative (PD) controller enhances system
stability and reduces overshoot by predicting future error using
the derivative term, leading to faster settling and better damping,
but it cannot eliminate steady-state error and is sensitive to
noise.
Proportional-Integral-Derivative (PID) controller combines
the advantages of all three actions, offering fast response, zero
steady-state error, low overshoot, and excellent stability.
PID controller is preferred as it provides fast response, zero
steady-state error, low overshoot, and excellent stability for
reliable drone flight control.
Q7   Design and develop a quadcopter with LiDAR and a high-   [20]
CO-4, SO-1, BL-3   resolution camera using OpenCV, Raspberry Pi, and Pixhawk
for mining operations, and evaluate its effectiveness in site
surveying, volume estimation, and safety inspection.
Design and develop a quadcopter with LiDAR and a high-
resolution camera using OpenCV, Raspberry Pi, and Pixhawk
for mining operations, and evaluate its effectiveness in site
surveying, volume estimation, and safety inspection.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
Block diagram of the drone and the signal flow between its
components
********** 10 **********
--- page 11 ---
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk   flight
controller is the central component that manages flight
control, navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size,
and payload capacity.
3. Motors and Propellers: Choose motors and propellers
that provide the required thrust for your drone.
4. ESCs (Electronic Speed Controllers): Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power
your drone for the desired flight time.
6. Raspberry Pi: Acts as an onboard processing unit,
handling real-time data analysis using OpenCV.
7. Sensors: Depending on your navigation requirements,
add sensors like GPS, IMU (Inertial Measurement
Unit), Lidar, Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
********** 11 **********
--- page 12 ---
LiDAR Sensor:
• Generates high-precision 3D maps of the terrain,
stockpiles, and mining structures.
High-Resolution Camera:
• Captures detailed visual data for inspection, monitoring,
and photogrammetry.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
• Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
mission Parameters.
• Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
Site Surveying:
1. LiDAR and camera data generate high-resolution 3D
maps of the mining site.
2. Enables measurement of terrain, roads, and excavation
areas without manual surveys.
Volume Estimation:
1. 3D models allow calculation of stockpile volumes for
ore, sand, or gravel.
********** 12 **********
--- page 13 ---
2. Reduces the need for manual measurements and
improves accuracy.
Safety Inspection:
1. High-resolution images detect cracks, landslides, or
unstable slopes.
2. Monitors worker activity and heavy machinery zones
remotely, minimizing risk.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evaluation-2M
Application   Benefits   Evaluation Metrics
Site   Fast, accurate   Mapping resolution,
Surveying   mapping without   area coverage,
manual labor   geospatial accuracy
Volume   Accurate stockpile Volume measurement
Estimation   volume   error, repeatability
calculation
Safety   Reduces human   Detection accuracy,
Inspection   risk, detects   response time, coverage
hazards early   of dangerous areas
********** 13 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 45d2e634a113

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CS_7055/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Identify the challenges in designing a Drone.   [05]
❑ Mechanical Design Challenges
Weight Optimization
❑ Power & Battery Management
Limited Battery Life
Power Distribution
❑ Communication & Control
Autonomous Navigation
Latency in Control Loops
Component Integration
CO-2, SO-1, BL-2   b.   Discuss the benefits of intermediate and advanced flight   [05]
controllers as compared to basic ones.
********** 1 **********
--- page 2 ---
CO-3, SO-1, BL-2   c.   What is the function of a barometer in a drone?   [05]
A barometer measures air pressure, which decreases as altitude
increases. Using this principle, the drone estimates how high it
is above the ground. Altitude estimation is done by converting
air pressure readings into height (altitude). barometer provides
continuous vertical position data.
Stable hovering helps the drone hold a fixed height without
constant pilot input which is essential for smooth, steady flight.
Vertical movement control detects whether the drone is
Climbing Descending, allowing precise control of up/down
motion.
The barometer (pressure sensor) in a drone is mainly used to
measure altitude and help the drone maintain a stable height
during flight.
Barometer values can be used with GPS and IMU to support
Return-to-Home (RTH), auto takeoff and landing and waypoint
navigation.
Barometer readings are affected by weather changes (pressure
variations), sensor values can drift over time.
CO-4, SO-1, BL-3   d.   Describe the functions of wireless camera and modem units in a   [05]
drone and analyze the challenges faced   in real-time
communication.
[Function of wireless camera and modem units-3M, Challenges-
2M]
The wireless camera is used to capture live video and images
during flight. It transmits real-time visual data to the operator,
which is essential for surveillance, navigation, mapping, and
inspection tasks. This allows the user to make immediate
********** 2 **********
--- page 3 ---
decisions based on what the drone sees, especially in
applications like search-and-rescue or security monitoring.
The modem unit (communication module) is responsible for
transmitting and receiving data between the drone and the
ground control system. It handles control signals (commands
sent to the drone) and telemetry data (such as altitude, speed,
GPS location, and battery status).   It ensures continuous
connectivity, enabling autonomous as well as manual control of
the drone.
Challenges include:
One major issue is signal interference, which can occur due to
obstacles, weather conditions, or other wireless devices
operating on similar frequencies. Another challenge is latency,
where delays in data transmission can affect timely decision-
making and control accuracy. Limited bandwidth can restrict
the quality of video streaming, leading to reduced resolution or
frame drops. Additionally, range limitations can cause
communication loss when the drone moves too far from the
controller. Ensuring data security   is also   critical, as
communication links may be vulnerable to hacking or
unauthorized access.
Attempt any four.   [80]
Q2   a.   How do the laws of physics govern the movement and stability   [10]
CO-1, SO-1, BL-2   of a drone during flight.
Role of Basic Forces
Drone flight is controlled by four main forces: thrust, gravity
(weight), drag, and lift. Thrust produced by the propellers
pushes air downward, creating an upward force that allows the
drone to rise. According to the laws of motion, every action
has an equal and opposite reaction. When the propellers push
air downward, the drone experiences an upward reaction force,
allowing it to lift and remain airborne. Increasing the speed of
the motors increases thrust, which allows the drone to ascend.
Decreasing thrust causes the drone to descend due to gravity.
Control of Direction and Motion. A drone changes direction
by varying the speed of individual motors. This creates
differences in thrust that cause the drone to tilt forward,
backward, or sideways, enabling motion in different directions.
Stability and Balance. Stability is maintained using onboard
sensors such as gyroscopes and accelerometers, which
constantly measure orientation and motion. The flight
controller automatically adjusts motor speeds to keep the drone
balanced and stable. Air resistance or drag affects the speed
********** 3 **********
--- page 4 ---
and efficiency of the drone. Proper design of propellers and
frame improves aerodynamic performance and flight stability.
Q2   b.   Explain the functions of ESC (any 5).   [10]
CO-2, SO-1, BL-2
Q3   a.   List and explain different types of RF communication modules   [10]
CO-3, SO-1, BL-2   used in drones?
RF (Radio Frequency) communication modules allow a drone to
send and receive data wirelessly—between the drone, the remote
controller, ground station, or other devices.
Depending of application different RF modules are used to
address the range, data rate and reliability.
Wi-Fi Modules based on standard Wi-Fi (2.4 GHz / 5 GHz) are
used in many consumer drones. They provide high data rate and
easy integration with application stacks (business layer)
Control Link uses 2.4 GHz or 915 MHz or 865mhz or 433 mhz
for low latency reliable control signals. These links provide long
range (1–10 km). these links have limited data bandwidth and
are used for control signals and cannot be used for video
streaming.
Telemetry Modules are again low bandwidth links meant for
data transfer between drone and base station. They are used for
Two-way communication to send data like GPS data, Battery
status, Speed, altitude etc. data is often exchanged using data
protocols like MAVLink.
Cellular Modules (4G/5G) uses mobile networks like 4G LTE
and 5G. they provide extremely long range (wherever network
coverage exists) and access to real-time cloud.
********** 4 **********
--- page 5 ---
Video Transmission Systems (First Person View - FPV) employs
dedicated RF systems for live video (often 5.8 GHz
analog/digital) for Low latency Real-time video feed. The only
issue is it has limited range and range extenders can increase
cost.
Q3   b.   Define drone security threats. Analyze the different types of   [10]
CO-5, SO-1, BL-3   drone security threats and Examine how these threats exploit
vulnerabilities in UAV systems (atleast 4 types).
[Def-2M, Security threats explanation any 4 2M each]
Drone security threats refer to any malicious or unauthorized
activities involving Unmanned Aerial Vehicles (UAVs) that
exploit system vulnerabilities to cause harm to people, property,
data, or national security.
Unauthorized Surveillance
Drones can be used for spying and unauthorized data collection
using onboard cameras and sensors. Attackers exploit the lack of
encryption and access control in data transmission systems to
capture sensitive images or videos. Weak privacy protections
and unsecured video links make such surveillance easier.
Terrorist Attacks
Drones can carry explosives or hazardous materials and be
directed toward targets. These attacks exploit navigation system
vulnerabilities (GPS dependence) and lack of geofencing
enforcement, allowing drones to enter restricted areas and
execute harmful operations.
Smuggling and Illegal Transport
Drones are used to transport contraband such as drugs or
weapons. Criminals take advantage of limited airspace
monitoring and absence of real-time tracking systems, enabling
drones to bypass traditional security measures and deliver illegal
goods undetected.
Signal Jamming and Spoofing
In this type of attack, communication signals between the drone
and controller are disrupted (jamming) or falsified (spoofing).
These threats exploit unsecured wireless communication
protocols and lack of authentication mechanisms, leading to loss
of control, redirection, or crashes.
Hacking and Cyber Attacks
Hackers can gain unauthorized access to drone systems and take
control or steal data. This occurs due to weak cybersecurity
measures, such as poor encryption, outdated firmware, or
insecure APIs, allowing attackers to manipulate drone
operations remotely.
********** 5 **********
--- page 6 ---
Collision with Aircraft
Drones flying in restricted airspace can collide with manned
aircraft. This risk arises from lack of airspace awareness systems
and poor integration with air traffic management, which allows
drones to operate without proper coordination or detection.
Swarm Attacks
Multiple drones can be coordinated to act as a swarm,
overwhelming   defense   systems. These   attacks   exploit
limitations   in detection and tracking technologies and
inadequate counter-UAV systems, making   it difficult to
neutralize multiple threats simultaneously.
Q4   a.   Explain the reason for using Brush less DC Motor in Drone.   [10]
CO-1, SO-1, BL-2
Q4   b.   Explain KV rating of a motor and its significance. Which other   [10]
CO-2, SO-1, BL-2   specifications are to be considered while selecting a motor for a
drone?
********** 6 **********
--- page 7 ---
Q5   a.   Explain the use of Newton’s law in Drone Flight.   [05]
CO-1, SO-1, BL-2   Drone flight works according to Newton’s laws, which explain
how forces produce motion. The rotating propellers push air
downward, creating an equal and opposite upward force that lifts
the drone. By increasing or decreasing the thrust of the motors,
the drone can take off, hover, or descend. Unequal thrust
between motors causes roll, pitch, and yaw, allowing the drone
to change direction and move in the air.
Q5   b.   Illustrate   the   role   of   the   accelerometer,   gyroscope,   [15]
CO-3, SO-1, BL-3   magnetometer and barometer in a UAV / drone. Explain the
concept of sensor fusion and discuss the advantage of sensor
fusion in flight control.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time.
********** 7 **********
--- page 8 ---
Accelerometer (measures linear motion) detects acceleration
along X, Y, Z axes and helps determine tilt (pitch & roll) using
gravity direction. It is useful for detecting sudden movements.
Limitation: Noisy and affected by vibrations.
Magnetometer (acts like a compass) measures Earth’s magnetic
field giving absolute heading (yaw direction).   Limitation:
Disturbed by nearby metals or electronics.
Barometer (measures altitude) measures air pressure to estimate
height, it helps maintain stable altitude (hovering). Limitation:
Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   Explain with a block diagram the flow of signals and power   [10]
CO-2, SO-1, BL-2   between transmitter and receiver.
********** 8 **********
--- page 9 ---
Q6   b.   Compare P controller, PI controller, PD controller, and PID   [10]
CO-4, SO-1, BL-3   controller for drone flight control and justify your choice based
on performance metrics.
[ Each controller- 2M Each and Justification-2M]
Proportional (P) controller provides a fast response with
simple implementation, but it suffers from steady-state error and
tends to produce high overshoot, making it only suitable for
basic stabilization.
Proportional-Integral (PI) controller improves accuracy by
eliminating steady-state error due to the integral action, which
makes it useful for tasks like altitude control; however, it results
********** 9 **********
--- page 10 ---
in slower response, increased overshoot, and longer settling
time.
Proportional-Derivative (PD) controller enhances system
stability and reduces overshoot by predicting future error using
the derivative term, leading to faster settling and better damping,
but it cannot eliminate steady-state error and is sensitive to
noise.
Proportional-Integral-Derivative (PID) controller combines
the advantages of all three actions, offering fast response, zero
steady-state error, low overshoot, and excellent stability.
PID controller is preferred as it provides fast response, zero
steady-state error, low overshoot, and excellent stability for
reliable drone flight control.
Q7   Design and develop a quadcopter with LiDAR and a high-   [20]
CO-4, SO-1, BL-3   resolution camera using OpenCV, Raspberry Pi, and Pixhawk
for mining operations, and evaluate its effectiveness in site
surveying, volume estimation, and safety inspection.
Design and develop a quadcopter with LiDAR and a high-
resolution camera using OpenCV, Raspberry Pi, and Pixhawk
for mining operations, and evaluate its effectiveness in site
surveying, volume estimation, and safety inspection.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
Block diagram of the drone and the signal flow between its
components
********** 10 **********
--- page 11 ---
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk   flight
controller is the central component that manages flight
control, navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size,
and payload capacity.
3. Motors and Propellers: Choose motors and propellers
that provide the required thrust for your drone.
4. ESCs (Electronic Speed Controllers): Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power
your drone for the desired flight time.
6. Raspberry Pi: Acts as an onboard processing unit,
handling real-time data analysis using OpenCV.
7. Sensors: Depending on your navigation requirements,
add sensors like GPS, IMU (Inertial Measurement
Unit), Lidar, Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
********** 11 **********
--- page 12 ---
LiDAR Sensor:
• Generates high-precision 3D maps of the terrain,
stockpiles, and mining structures.
High-Resolution Camera:
• Captures detailed visual data for inspection, monitoring,
and photogrammetry.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
• Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
mission Parameters.
• Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
Site Surveying:
1. LiDAR and camera data generate high-resolution 3D
maps of the mining site.
2. Enables measurement of terrain, roads, and excavation
areas without manual surveys.
Volume Estimation:
1. 3D models allow calculation of stockpile volumes for
ore, sand, or gravel.
********** 12 **********
--- page 13 ---
2. Reduces the need for manual measurements and
improves accuracy.
Safety Inspection:
1. High-resolution images detect cracks, landslides, or
unstable slopes.
2. Monitors worker activity and heavy machinery zones
remotely, minimizing risk.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evaluation-2M
Application   Benefits   Evaluation Metrics
Site   Fast, accurate   Mapping resolution,
Surveying   mapping without   area coverage,
manual labor   geospatial accuracy
Volume   Accurate stockpile Volume measurement
Estimation   volume   error, repeatability
calculation
Safety   Reduces human   Detection accuracy,
Inspection   risk, detects   response time, coverage
hazards early   of dangerous areas
********** 13 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper f64642c9f936

- Departments: Cyber Security
- Programmes: BTech CyberSecurity 7010
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CyberSecurity_7010/Drone Technology/ANS_Drone Technology(702EX0I002)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/B. Tech (COMP)/B. Tech (CS)/B. Tech (CSE -
CS)/B. TECH (CSE - DS)/B. Tech (DS)/B. Tech (EXTC)/B. Tech Intg. (CE)/B. Tech Intg.
(IT)/B. Tech (IT)/B. Tech (MECH)/B. Tech (MXTC)/MBA Tech (AI)/MBA Tech (Comp)/MBA
Tech (IT)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Drone Technology
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Q.1. is compulsory.
3. Attempt any 4 out of the remaining questions.
4. Assume suitable data wherever necessary.
5. Figures on the right indicate maximum marks.
Q1   Answer briefly.   [20]
CO-1, SO-1, BL-2   a.   Identify the challenges in designing a Drone.   [05]
❑ Mechanical Design Challenges
Weight Optimization
❑ Power & Battery Management
Limited Battery Life
Power Distribution
❑ Communication & Control
Autonomous Navigation
Latency in Control Loops
Component Integration
CO-2, SO-1, BL-2   b.   Discuss the benefits of intermediate and advanced flight   [05]
controllers as compared to basic ones.
********** 1 **********
--- page 2 ---
CO-3, SO-1, BL-2   c.   What is the function of a barometer in a drone?   [05]
A barometer measures air pressure, which decreases as altitude
increases. Using this principle, the drone estimates how high it
is above the ground. Altitude estimation is done by converting
air pressure readings into height (altitude). barometer provides
continuous vertical position data.
Stable hovering helps the drone hold a fixed height without
constant pilot input which is essential for smooth, steady flight.
Vertical movement control detects whether the drone is
Climbing Descending, allowing precise control of up/down
motion.
The barometer (pressure sensor) in a drone is mainly used to
measure altitude and help the drone maintain a stable height
during flight.
Barometer values can be used with GPS and IMU to support
Return-to-Home (RTH), auto takeoff and landing and waypoint
navigation.
Barometer readings are affected by weather changes (pressure
variations), sensor values can drift over time.
CO-4, SO-1, BL-3   d.   Describe the functions of wireless camera and modem units in a   [05]
drone and analyze the challenges faced   in real-time
communication.
[Function of wireless camera and modem units-3M, Challenges-
2M]
The wireless camera is used to capture live video and images
during flight. It transmits real-time visual data to the operator,
which is essential for surveillance, navigation, mapping, and
inspection tasks. This allows the user to make immediate
********** 2 **********
--- page 3 ---
decisions based on what the drone sees, especially in
applications like search-and-rescue or security monitoring.
The modem unit (communication module) is responsible for
transmitting and receiving data between the drone and the
ground control system. It handles control signals (commands
sent to the drone) and telemetry data (such as altitude, speed,
GPS location, and battery status).   It ensures continuous
connectivity, enabling autonomous as well as manual control of
the drone.
Challenges include:
One major issue is signal interference, which can occur due to
obstacles, weather conditions, or other wireless devices
operating on similar frequencies. Another challenge is latency,
where delays in data transmission can affect timely decision-
making and control accuracy. Limited bandwidth can restrict
the quality of video streaming, leading to reduced resolution or
frame drops. Additionally, range limitations can cause
communication loss when the drone moves too far from the
controller. Ensuring data security   is also   critical, as
communication links may be vulnerable to hacking or
unauthorized access.
Attempt any four.   [80]
Q2   a.   How do the laws of physics govern the movement and stability   [10]
CO-1, SO-1, BL-2   of a drone during flight.
Role of Basic Forces
Drone flight is controlled by four main forces: thrust, gravity
(weight), drag, and lift. Thrust produced by the propellers
pushes air downward, creating an upward force that allows the
drone to rise. According to the laws of motion, every action
has an equal and opposite reaction. When the propellers push
air downward, the drone experiences an upward reaction force,
allowing it to lift and remain airborne. Increasing the speed of
the motors increases thrust, which allows the drone to ascend.
Decreasing thrust causes the drone to descend due to gravity.
Control of Direction and Motion. A drone changes direction
by varying the speed of individual motors. This creates
differences in thrust that cause the drone to tilt forward,
backward, or sideways, enabling motion in different directions.
Stability and Balance. Stability is maintained using onboard
sensors such as gyroscopes and accelerometers, which
constantly measure orientation and motion. The flight
controller automatically adjusts motor speeds to keep the drone
balanced and stable. Air resistance or drag affects the speed
********** 3 **********
--- page 4 ---
and efficiency of the drone. Proper design of propellers and
frame improves aerodynamic performance and flight stability.
Q2   b.   Explain the functions of ESC (any 5).   [10]
CO-2, SO-1, BL-2
Q3   a.   List and explain different types of RF communication modules   [10]
CO-3, SO-1, BL-2   used in drones?
RF (Radio Frequency) communication modules allow a drone to
send and receive data wirelessly—between the drone, the remote
controller, ground station, or other devices.
Depending of application different RF modules are used to
address the range, data rate and reliability.
Wi-Fi Modules based on standard Wi-Fi (2.4 GHz / 5 GHz) are
used in many consumer drones. They provide high data rate and
easy integration with application stacks (business layer)
Control Link uses 2.4 GHz or 915 MHz or 865mhz or 433 mhz
for low latency reliable control signals. These links provide long
range (1–10 km). these links have limited data bandwidth and
are used for control signals and cannot be used for video
streaming.
Telemetry Modules are again low bandwidth links meant for
data transfer between drone and base station. They are used for
Two-way communication to send data like GPS data, Battery
status, Speed, altitude etc. data is often exchanged using data
protocols like MAVLink.
Cellular Modules (4G/5G) uses mobile networks like 4G LTE
and 5G. they provide extremely long range (wherever network
coverage exists) and access to real-time cloud.
********** 4 **********
--- page 5 ---
Video Transmission Systems (First Person View - FPV) employs
dedicated RF systems for live video (often 5.8 GHz
analog/digital) for Low latency Real-time video feed. The only
issue is it has limited range and range extenders can increase
cost.
Q3   b.   Define drone security threats. Analyze the different types of   [10]
CO-5, SO-1, BL-3   drone security threats and Examine how these threats exploit
vulnerabilities in UAV systems (atleast 4 types).
[Def-2M, Security threats explanation any 4 2M each]
Drone security threats refer to any malicious or unauthorized
activities involving Unmanned Aerial Vehicles (UAVs) that
exploit system vulnerabilities to cause harm to people, property,
data, or national security.
Unauthorized Surveillance
Drones can be used for spying and unauthorized data collection
using onboard cameras and sensors. Attackers exploit the lack of
encryption and access control in data transmission systems to
capture sensitive images or videos. Weak privacy protections
and unsecured video links make such surveillance easier.
Terrorist Attacks
Drones can carry explosives or hazardous materials and be
directed toward targets. These attacks exploit navigation system
vulnerabilities (GPS dependence) and lack of geofencing
enforcement, allowing drones to enter restricted areas and
execute harmful operations.
Smuggling and Illegal Transport
Drones are used to transport contraband such as drugs or
weapons. Criminals take advantage of limited airspace
monitoring and absence of real-time tracking systems, enabling
drones to bypass traditional security measures and deliver illegal
goods undetected.
Signal Jamming and Spoofing
In this type of attack, communication signals between the drone
and controller are disrupted (jamming) or falsified (spoofing).
These threats exploit unsecured wireless communication
protocols and lack of authentication mechanisms, leading to loss
of control, redirection, or crashes.
Hacking and Cyber Attacks
Hackers can gain unauthorized access to drone systems and take
control or steal data. This occurs due to weak cybersecurity
measures, such as poor encryption, outdated firmware, or
insecure APIs, allowing attackers to manipulate drone
operations remotely.
********** 5 **********
--- page 6 ---
Collision with Aircraft
Drones flying in restricted airspace can collide with manned
aircraft. This risk arises from lack of airspace awareness systems
and poor integration with air traffic management, which allows
drones to operate without proper coordination or detection.
Swarm Attacks
Multiple drones can be coordinated to act as a swarm,
overwhelming   defense   systems. These   attacks   exploit
limitations   in detection and tracking technologies and
inadequate counter-UAV systems, making   it difficult to
neutralize multiple threats simultaneously.
Q4   a.   Explain the reason for using Brush less DC Motor in Drone.   [10]
CO-1, SO-1, BL-2
Q4   b.   Explain KV rating of a motor and its significance. Which other   [10]
CO-2, SO-1, BL-2   specifications are to be considered while selecting a motor for a
drone?
********** 6 **********
--- page 7 ---
Q5   a.   Explain the use of Newton’s law in Drone Flight.   [05]
CO-1, SO-1, BL-2   Drone flight works according to Newton’s laws, which explain
how forces produce motion. The rotating propellers push air
downward, creating an equal and opposite upward force that lifts
the drone. By increasing or decreasing the thrust of the motors,
the drone can take off, hover, or descend. Unequal thrust
between motors causes roll, pitch, and yaw, allowing the drone
to change direction and move in the air.
Q5   b.   Illustrate   the   role   of   the   accelerometer,   gyroscope,   [15]
CO-3, SO-1, BL-3   magnetometer and barometer in a UAV / drone. Explain the
concept of sensor fusion and discuss the advantage of sensor
fusion in flight control.
Stable and accurate flight comes from combining multiple
sensors with each sensor measuring a different aspect of motion.
These sensors are fused together for stable state of drone.
Gyroscope (measures rotation) measures angular velocity (how
fast the drone rotates) and provides very fast and smooth
orientation changes. It is Crucial for real-time stabilization.
Limitation: Suffers from drift over time.
********** 7 **********
--- page 8 ---
Accelerometer (measures linear motion) detects acceleration
along X, Y, Z axes and helps determine tilt (pitch & roll) using
gravity direction. It is useful for detecting sudden movements.
Limitation: Noisy and affected by vibrations.
Magnetometer (acts like a compass) measures Earth’s magnetic
field giving absolute heading (yaw direction).   Limitation:
Disturbed by nearby metals or electronics.
Barometer (measures altitude) measures air pressure to estimate
height, it helps maintain stable altitude (hovering). Limitation:
Affected by weather and pressure changes.
the drone uses sensor fusion algorithms (like the Kalman filter)
to combine all inputs into a reliable estimate of Position,
Orientation (roll, pitch, yaw) and Altitude.
Orientation control is achieved using Gyroscope, Accelerometer
and Magnetometer.   Altitude control is achieved using
barometer and accelerometer (z-axis) resulting in Smooth
hovering and height control.
Gyroscope drift must be corrected using Accelerometer (for tilt)
and magnetometer (for direction) preventing the drone from
slowly losing orientation.
The flight controller continuously reads all sensors and
combines data using sensor fusion then adjusts motor speeds
instantly to keep the drone level and stable.
Q6   a.   Explain with a block diagram the flow of signals and power   [10]
CO-2, SO-1, BL-2   between transmitter and receiver.
********** 8 **********
--- page 9 ---
Q6   b.   Compare P controller, PI controller, PD controller, and PID   [10]
CO-4, SO-1, BL-3   controller for drone flight control and justify your choice based
on performance metrics.
[ Each controller- 2M Each and Justification-2M]
Proportional (P) controller provides a fast response with
simple implementation, but it suffers from steady-state error and
tends to produce high overshoot, making it only suitable for
basic stabilization.
Proportional-Integral (PI) controller improves accuracy by
eliminating steady-state error due to the integral action, which
makes it useful for tasks like altitude control; however, it results
********** 9 **********
--- page 10 ---
in slower response, increased overshoot, and longer settling
time.
Proportional-Derivative (PD) controller enhances system
stability and reduces overshoot by predicting future error using
the derivative term, leading to faster settling and better damping,
but it cannot eliminate steady-state error and is sensitive to
noise.
Proportional-Integral-Derivative (PID) controller combines
the advantages of all three actions, offering fast response, zero
steady-state error, low overshoot, and excellent stability.
PID controller is preferred as it provides fast response, zero
steady-state error, low overshoot, and excellent stability for
reliable drone flight control.
Q7   Design and develop a quadcopter with LiDAR and a high-   [20]
CO-4, SO-1, BL-3   resolution camera using OpenCV, Raspberry Pi, and Pixhawk
for mining operations, and evaluate its effectiveness in site
surveying, volume estimation, and safety inspection.
Design and develop a quadcopter with LiDAR and a high-
resolution camera using OpenCV, Raspberry Pi, and Pixhawk
for mining operations, and evaluate its effectiveness in site
surveying, volume estimation, and safety inspection.
Block diagram-2M
Flowchart of the selection process of Hardware design
framework
Block diagram of the drone and the signal flow between its
components
********** 10 **********
--- page 11 ---
Define Requirements: 1M
Clearly define the requirements for your autonomous navigation
drone, including the type of drone (e.g., quadcopter, hexacopter,
fixed-wing), payload (e.g., camera, sensors), flight range,
endurance, and specific tasks it should perform.
Select Hardware Components: 3M
Choose appropriate hardware components for your drone,
including:
1. Pixhawk Flight Controller: The Pixhawk   flight
controller is the central component that manages flight
control, navigation, and autopilot functions.
2. Frame: Select a frame that suits your drone type, size,
and payload capacity.
3. Motors and Propellers: Choose motors and propellers
that provide the required thrust for your drone.
4. ESCs (Electronic Speed Controllers): Select ESCs
compatible with your motors.
5. Battery: Determine the appropriate battery to power
your drone for the desired flight time.
6. Raspberry Pi: Acts as an onboard processing unit,
handling real-time data analysis using OpenCV.
7. Sensors: Depending on your navigation requirements,
add sensors like GPS, IMU (Inertial Measurement
Unit), Lidar, Camera, Telemetry
GPS (Global Positioning System)
• Provides the quadcopter’s geographical position and
altitude. Essential for waypoint navigation, mapping, and
maintaining accurate flight paths.
IMU (Inertial Measurement Unit)
• Measures linear acceleration and angular velocity to
determine the drone’s orientation, roll, pitch, and yaw.
Crucial for flight stabilization and motion control.
********** 11 **********
--- page 12 ---
LiDAR Sensor:
• Generates high-precision 3D maps of the terrain,
stockpiles, and mining structures.
High-Resolution Camera:
• Captures detailed visual data for inspection, monitoring,
and photogrammetry.
Telemetry System
• Enables   real-time   communication   between   the
quadcopter and ground control station. Transmits sensor
data, flight status, and receives control commands for
monitoring and control.
Assemble the Drone: 1M
Assemble the drone components according to the manufacturer's
instructions and best practices for safety and reliability.
Software Configuration:2M
• Flash the Pixhawk flight controller with the appropriate
firmware, such as ArduPilot or PX4, and configure it for
your specific drone setup.
• Calibrate the sensors, including the IMU and GPS, to
ensure accurate readings.
Mission Planning and Waypoints:2M
• Use mission planning software (e.g., Mission Planner,
QGroundControl) to define waypoints, flight paths, and
mission Parameters.
• Set up geofencing and safety parameters to prevent the
drone from flying into restricted areas or in unfavorable
conditions.
Implement Autonomous Navigation Algorithms 2M
Develop or configure autonomous navigation algorithms,
including:
• GPS-based navigation for waypoint following.
• Obstacle avoidance using Lidar or other proximity
sensors.
• Altitude and attitude control for stable flight.
Data Processing and Analysis
Site Surveying:
1. LiDAR and camera data generate high-resolution 3D
maps of the mining site.
2. Enables measurement of terrain, roads, and excavation
areas without manual surveys.
Volume Estimation:
1. 3D models allow calculation of stockpile volumes for
ore, sand, or gravel.
********** 12 **********
--- page 13 ---
2. Reduces the need for manual measurements and
improves accuracy.
Safety Inspection:
1. High-resolution images detect cracks, landslides, or
unstable slopes.
2. Monitors worker activity and heavy machinery zones
remotely, minimizing risk.
Telemetry and Ground Control Station: 1M
1. Set up telemetry systems for communication between the
ground control station (GCS) and the drone.
2. Use a GCS software to monitor the drone's status, update
missions in real-time, and take control when needed.
Testing and Calibration:1M
1. Conduct extensive testing in controlled environments to
ensure the drone's safety and navigation accuracy.
2. Calibrate and fine-tune the drone's parameters, including
PID controllers, to optimize performance.
Safety Measures:1M
1. Implement safety features like return-to-home (RTH)
and fail-safe modes to handle unexpected situations.
2. Comply with local regulations and obtain necessary
permissions for autonomous flights.
Integration of Payload:1M
If your drone is intended for specific tasks like aerial
photography or surveying, integrate and configure the payload
accordingly.
Deployment:1M
Deploy the drone for autonomous navigation missions,
monitoring its performance and making adjustments as needed.
Evaluation-2M
Application   Benefits   Evaluation Metrics
Site   Fast, accurate   Mapping resolution,
Surveying   mapping without   area coverage,
manual labor   geospatial accuracy
Volume   Accurate stockpile Volume measurement
Estimation   volume   error, repeatability
calculation
Safety   Reduces human   Detection accuracy,
Inspection   risk, detects   response time, coverage
hazards early   of dangerous areas
********** 13 **********
````
