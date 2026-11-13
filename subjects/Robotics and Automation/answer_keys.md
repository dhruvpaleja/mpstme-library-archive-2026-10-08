# Robotics and Automation: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper a92547cec7c6

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_EXTC_7006/Robotics and Automation/ANS_Robotics and Automation(702EX0E014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: mixed (12 pages), mean OCR confidence 46.6
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: Robotics and Automation
Date: 04 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
a. Explain with respect to industrial robot,   5
1. Number of Axes
2. Load carrying capacity and speed
Number of Axes
• The number of axes in an industrial robot refers to the number of independent
joints that enable the robot to move and orient its end-effector in space.
•   Typical industrial robots range from 3 to 7 axes.
• 3 axes: Basic movement—usually for simple linear tasks like pick-and-
place.
• 6 axes: Most common in industrial robotics, capable of positioning and
orienting tools in 3D space with flexibility.
• 7 axes or more: Used for highly complex tasks such as welding or
assembly in tight spaces, providing extra degrees of freedom for
manoeuvring.
2. Load Carrying Capacity and Speed
• Load Carrying Capacity:
•   Varies widely, from a few grams in precision micro-robots to thousands
of kilograms in large industrial robots. Typical payloads range from 5 kg
to 2000 kg depending on application.
• Speed:
•   Varies based on the type and purpose of the robot.
• For example, robotic arms used in assembly lines can reach 1 m/sec or
more for end-effector speed.
• High-speed robots for packaging or pick-and-place can operate at up to
10-20 cycles per second, depending on the load and size.
b. Explain in brief image representation in a robotic vision system.   5
********** 1 **********
--- page 2 ---
Image representation in a robotic vision system refers to the way the visual information
captured by cameras or sensors is digitally encoded and stored for processing and
analysis. In robotic vision:
• An image is typically represented as a two-dimensional array (matrix) of pixels.
• Each pixel contains intensity values that denote brightness or color information.
• For grayscale images, pixel values usually range from 0 (black) to 255 (white).
• For color images, each pixel contains multiple components (e.g., RGB - Red,
Green, Blue values).
• The resolution (number of pixels in width and height) determines image detail.
• This digital image data serves as the input for further processing steps like
filtering, feature detection (edges, corners), and object recognition in the robotic
vision system.
Thus, image representation is the foundational format enabling robots to interpret,
analyze, and react to their visual environment effectively.
c.   List the considerations to be considered before decision to automate a new or existing   5
facility. Compare Mechanization and Automation.
Considerations Before Automating a New or Existing Facility
1. Cost Analysis: Evaluate initial investment, operating costs, and potential
savings.
2. Production Volume: Automation is more feasible for high-volume consistent
production.
3. Product Complexity and Variety: Low variability favors automation; high
variety may require flexible systems.
4. Existing Infrastructure: Compatibility of automation technology with current
equipment and layout.
5. Labor Skill Levels: Availability of skilled personnel for operation and
maintenance.
6. Return on Investment (ROI): Expected time frame to recover automation costs.
7. Safety and Working Conditions: Potential improvements in worker safety.
8. Quality Improvement: Capability of automation to enhance product consistency
and quality.
9. Flexibility Requirements: Whether the process needs to adapt quickly to
changes.
10. Maintenance and Support: Availability of support services and parts for
automation systems.
********** 2 **********
--- page 3 ---
Feature   Mechanization   Automation
Use of machines to assist   Use of control systems including
Definition   human labor, replacing   computers or PLCs to operate
physical effort   machinery automatically
Low; machines perform operations
Human   High; humans still control
automatically with minimal human
Involvement   and operate machinery
intervention
Eliminate or minimize human
Reduce manual labor;
Purpose   control for consistency and
increase efficiency
productivity
Relatively simple mechanical Complex control systems with
Complexity
devices   sensors, feedback, and logic
Often less flexible, suited for More flexible; adaptable to process
Flexibility
specific tasks   changes through programming
Industrial robots, CNC machines,
Examples   Power tools, conveyors
PLC controlled systems
d. Generate ladder diagram for following logic gates.   5
i.   AND
2
ii.   OR
********** 3 **********
--- page 4 ---
2
1
iii.   NOT
Q2   a.   Classify robots based on their work envelop and list industrial application of each robot. [10]
Work
Industrial
Robot Type   Envelope   Description
Applications
Shape
Cartesian   Consists of three linear Used in CNC
Rectangular
(Rectangular)   slides to move in X, Y, machines, 3D
box-shaped
Robots   and Z directions within   printing, assembly,
********** 4 **********
--- page 5 ---
a rectangular   pick and place,
workspace.   packaging.
Combination of
Cylindrical   Material handling,
rotational and linear
Cylindrical   shape within a   welding, assembly,
movements along
Robots   radius and   machine tool
cylindrical
height   operations.
coordinates.
Rotary base with an   Handling heavy or
Spherical   Dome-shaped   extendable arm that   bulky items, die
(Polar) Robots   or spherical   moves in a spherical   casting, and sealing
workspace.   operations.
Assembly,
Selective Compliance
packaging, and
Assembly Robot Arm,
SCARA   Horizontal   palletizing in
good for lateral
Robots   donut-shaped   electronics and
movements with
automotive
vertical compliance.
industries.
Almost   Welding, painting,
Multiple rotary joints
Articulated   spherical with   assembly lines, spot
resembling a human
Robots   many degrees   welding, material
arm; highly flexible.
of freedom   handling.
Multiple arms   High-speed pick-
Complex
Parallel Robots   connected to a single   and-place in
polyhedral
(Delta)   platform, high speed   packaging and food
workspace
and precision.   processing.
b.   Derive the ARM matrix using the DH convention.   [10]
Compute the end-effector position (x, y, z) and overall orientation of the tool with
respect to the base frame.
(θ1 = 60∘, d2 = 150mm, a2 = 180mm)
Axis   𝜽𝒌   𝒅𝒌   𝒂𝒌   𝜶𝒌
1   𝜃1   0   0   −𝜋/2
2   0   𝑑2   𝑎2   0
4
********** 5 **********
--- page 6 ---
3
3
Q3   a. Analyze a 5 Axis Microbot Alpha II Robotic Arm and compute the following.   [20]
i.   Link coordinate diagram
7
ii.   Link coordinate table.
5
********** 6 **********
--- page 7 ---
8
iii.   Individual Link coordinate transformation matrices.
Q4   a. Compare different types of force sensors and write a short note on Tactile sensors.   [10]
Sensor   Working   Typical
Advantages   Limitations
Type   Principle   Applications
Measures
Sensitive to
Strain   strain-induced   High accuracy,   Load cells,
temperature,
Gauge   resistance   small size,   torque
requires
Sensors   change in a   robust   measurement
calibration
material
Generates   Cannot
electric charge   High-frequency   measure static   Vibration,
Piezoelectri
under   response, wide   forces, needs   impact force
c Sensors
mechanical   dynamic range   charge   measurement
stress   amplifier
Measures
change in   High sensitivity,   Sensitive to   Tactile
Capacitive
capacitance   good for   environmental   sensing,
Force
due to force-   dynamic/static   noise and   precision
Sensors
induced   forces   humidity   tasks
displacement
Measures
force by
Immune to   Surgical
Optical   detecting
electromagnetic   Complex and   robots,
Force   changes in
interference,   costly setup   delicate
Sensors   light
high sensitivity   manipulation
transmission
or reflection
********** 7 **********
--- page 8 ---
Uses changes   Contactless,   Sensitive to
Magnetic   Industrial
in magnetic   robust, good for   external
Force   automation,
field due to   harsh   magnetic
Sensors   automotive
applied force   environments   disturbances
Short Note on Tactile Sensors
•   Definition: Tactile sensors detect and measure properties related to touch, such
as force, pressure distribution, texture, and vibration.
• Function: They mimic the human sense of touch and provide feedback about
the surface being interacted with.
• Types: Include force-sensitive resistors, piezoresistive, capacitive tactile arrays,
and optical tactile sensors.
•   Applications: Used in robotic grippers for object manipulation, quality
inspection, and human-robot interaction.
• Importance: Enhance robot dexterity and safety by enabling precise grip
control and environmental awareness.
Tactile sensors are crucial for robots to perform delicate tasks requiring fine force
control and texture recognition, enabling safer and smarter robotic operations
b. Explain with proper block diagram, also list advantages and limitations of Hydraulic [10]
system.
•   Reservoir: Stores the hydraulic fluid (oil) required for the system.
• Pump: Converts mechanical energy into hydraulic energy by pressurizing the
fluid.
•   Filter: Removes impurities from the fluid to prevent damage to components.
•   Control Valves: Regulate flow and pressure; include directional control valves,
pressure relief valves, and flow control valves.
•   Hydraulic Actuator: Converts hydraulic energy into mechanical motion (linear
or rotary) to perform work.
•   Sensors: Measure pressure, position, or flow for feedback and control.
•   Controller: Manages the entire system operation based on sensor inputs and
programmed logic.
********** 8 **********
--- page 9 ---
Advantages of Hydraulic Systems
• High Power Density: Capable of generating very large forces and torques in a
compact size.
•   Precise Control: Smooth and accurate control over speed, force, and position.
•   Reliability: Robust and durable in harsh industrial environments.
• Overload Protection: Equipped with pressure relief valves to prevent damage.
• Simple Mechanism: Fewer mechanical parts compared to other drive systems.
Limitations of Hydraulic Systems
• Leakage Issues: Hydraulic fluids can leak, causing environmental hazards and
maintenance concerns.
• Complex Maintenance: Requires regular checking for fluid quality and system
integrity.
•   Cost: Initial system costs and maintenance may be high.
•   Bulkiness: Requires pipes, hoses, and reservoirs which add to system size.
•   Noise: Pump and fluid flow can generate operational noise.
Hydraulic systems are widely used in robotics and industrial machinery where large
force and precise control are essential despite their maintenance requirements.
Q5   a. Evaluate the values of performance index for the image and template given below. Also [15]
find the best match.
I(k,j)   2   1   0   1   2   1   2   1   T(k,j)
0   1   3   2   1   0   1   0
1   2   1   2   0
0   1   0   2   1
pos_x pos_y SSD ZNCC
0   0   10.0 0.307
1   0   13.0 -0.255
2   0   15.0 -0.218
0   1   9.0 0.588
1   1   6.0 0.657
2   1   10.0 0.392
0   2   0.0 1.000
1   2   7.0 0.566
2   2   13.0 0.255
b. Explain the general properties of Inverse Kinematics.   [5]
General Properties of Inverse Kinematics
1. Multiple   Solutions:
Inverse kinematics often has multiple possible solutions for a given end-effector
position and orientation due to the manipulator's joint redundancies.
2. Existence   of   Solutions:
Solutions may not always exist for all desired positions; unreachable or singular
positions may have no valid joint configurations.
Q6   a. Explain with proper block diagram the internal architecture of a PLC System and [10]
explain each block in brief.
********** 9 **********
--- page 10 ---
Explanation of Each Block
1. Power Supply:
Provides regulated DC voltage to all PLC components, ensuring stable
operation.
2. Central Processing Unit (CPU):
The brain of the PLC, it interprets control instructions, executes the user
program, processes inputs, and updates outputs based on logic.
3. Memory:
• Program Memory: Stores the control program (firmware or user ladder
logic).
• Data Memory: Stores variables, input/output status, timers, counters,
and other data used during operation.
4. Input Interface:
Receives signals from external input devices such as sensors and switches. It
conditions and converts these signals into a format suitable for the CPU, often
providing electrical isolation.
5. Output Interface:
Sends control signals from the CPU to actuators and output devices. It converts
CPU output signals to appropriate power levels and provides isolation.
6. Communication Interface:
Allows the PLC to communicate with other PLCs, computers, or networks for
data exchange and remote control.
********** 10 **********
--- page 11 ---
b. Solve for [𝑞]𝐹if   [10]
4
[𝑞]𝑀= [ 6 ]
8
1
Let 𝐹= {𝑓1, 𝑓2, 𝑓3} and 𝑀= {𝑚1, 𝑚2, 𝑚3} be two initially coincident fixed and
mobile orthonormal coordinate frames, respectively. Suppose we perform the following
sequence of transformations on the mobile frame 𝑀:
1. Translate 𝑀along 𝑓3by 15 units
2. Rotate 𝑀about 𝑓2by -π radians
3. Rotate 𝑀about 𝑓1by π/2 radians
Q7   a. Analyze an ARM Matrix for 3 Axis PARA and answer the following.   [20]
𝐶123 −𝑆123 0 𝑎1𝐶1 + 𝑎2𝐶12
𝑆123   𝐶123 0 𝑎1𝑆1 + 𝑎2𝑆12
[   ]
0   0   1   𝑑3
0   0   0   1
i. Derive TCV from the arm matrix and corresponding equations.
ii. Derive joint equations for all the joints. (q1, q2, q3)
********** 11 **********
--- page 12 ---
aC, + aC2
4S) + aS)

exp (q3/7)

w2 a ee |
= 1+ W3 ~ ay ~ a5
Qz = tarccos ——____—___—..

2a, a5
!

q, = atan2 [a, — a,C,)w, + @g8,wo, (a, + a,C,)w, — a,S,W,]

{

q3 = 7 Inw,

FRR ICR] DA KH
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper d029d7167d8b

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_EXTC_7006/Robotics and Automation/ANS_Robotics and Automation(702EX0E014)_2025-2026_d029d7167d.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Dec 2025
- Text: mixed (12 pages), mean OCR confidence 46.6
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: Robotics and Automation
Date: 04 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
a. Explain with respect to industrial robot,   5
1. Number of Axes
2. Load carrying capacity and speed
Number of Axes
• The number of axes in an industrial robot refers to the number of independent
joints that enable the robot to move and orient its end-effector in space.
•   Typical industrial robots range from 3 to 7 axes.
• 3 axes: Basic movement—usually for simple linear tasks like pick-and-
place.
• 6 axes: Most common in industrial robotics, capable of positioning and
orienting tools in 3D space with flexibility.
• 7 axes or more: Used for highly complex tasks such as welding or
assembly in tight spaces, providing extra degrees of freedom for
manoeuvring.
2. Load Carrying Capacity and Speed
• Load Carrying Capacity:
•   Varies widely, from a few grams in precision micro-robots to thousands
of kilograms in large industrial robots. Typical payloads range from 5 kg
to 2000 kg depending on application.
• Speed:
•   Varies based on the type and purpose of the robot.
• For example, robotic arms used in assembly lines can reach 1 m/sec or
more for end-effector speed.
• High-speed robots for packaging or pick-and-place can operate at up to
10-20 cycles per second, depending on the load and size.
b. Explain in brief image representation in a robotic vision system.   5
********** 1 **********
--- page 2 ---
Image representation in a robotic vision system refers to the way the visual information
captured by cameras or sensors is digitally encoded and stored for processing and
analysis. In robotic vision:
• An image is typically represented as a two-dimensional array (matrix) of pixels.
• Each pixel contains intensity values that denote brightness or color information.
• For grayscale images, pixel values usually range from 0 (black) to 255 (white).
• For color images, each pixel contains multiple components (e.g., RGB - Red,
Green, Blue values).
• The resolution (number of pixels in width and height) determines image detail.
• This digital image data serves as the input for further processing steps like
filtering, feature detection (edges, corners), and object recognition in the robotic
vision system.
Thus, image representation is the foundational format enabling robots to interpret,
analyze, and react to their visual environment effectively.
c.   List the considerations to be considered before decision to automate a new or existing   5
facility. Compare Mechanization and Automation.
Considerations Before Automating a New or Existing Facility
1. Cost Analysis: Evaluate initial investment, operating costs, and potential
savings.
2. Production Volume: Automation is more feasible for high-volume consistent
production.
3. Product Complexity and Variety: Low variability favors automation; high
variety may require flexible systems.
4. Existing Infrastructure: Compatibility of automation technology with current
equipment and layout.
5. Labor Skill Levels: Availability of skilled personnel for operation and
maintenance.
6. Return on Investment (ROI): Expected time frame to recover automation costs.
7. Safety and Working Conditions: Potential improvements in worker safety.
8. Quality Improvement: Capability of automation to enhance product consistency
and quality.
9. Flexibility Requirements: Whether the process needs to adapt quickly to
changes.
10. Maintenance and Support: Availability of support services and parts for
automation systems.
********** 2 **********
--- page 3 ---
Feature   Mechanization   Automation
Use of machines to assist   Use of control systems including
Definition   human labor, replacing   computers or PLCs to operate
physical effort   machinery automatically
Low; machines perform operations
Human   High; humans still control
automatically with minimal human
Involvement   and operate machinery
intervention
Eliminate or minimize human
Reduce manual labor;
Purpose   control for consistency and
increase efficiency
productivity
Relatively simple mechanical Complex control systems with
Complexity
devices   sensors, feedback, and logic
Often less flexible, suited for More flexible; adaptable to process
Flexibility
specific tasks   changes through programming
Industrial robots, CNC machines,
Examples   Power tools, conveyors
PLC controlled systems
d. Generate ladder diagram for following logic gates.   5
i.   AND
2
ii.   OR
********** 3 **********
--- page 4 ---
2
1
iii.   NOT
Q2   a.   Classify robots based on their work envelop and list industrial application of each robot. [10]
Work
Industrial
Robot Type   Envelope   Description
Applications
Shape
Cartesian   Consists of three linear Used in CNC
Rectangular
(Rectangular)   slides to move in X, Y, machines, 3D
box-shaped
Robots   and Z directions within   printing, assembly,
********** 4 **********
--- page 5 ---
a rectangular   pick and place,
workspace.   packaging.
Combination of
Cylindrical   Material handling,
rotational and linear
Cylindrical   shape within a   welding, assembly,
movements along
Robots   radius and   machine tool
cylindrical
height   operations.
coordinates.
Rotary base with an   Handling heavy or
Spherical   Dome-shaped   extendable arm that   bulky items, die
(Polar) Robots   or spherical   moves in a spherical   casting, and sealing
workspace.   operations.
Assembly,
Selective Compliance
packaging, and
Assembly Robot Arm,
SCARA   Horizontal   palletizing in
good for lateral
Robots   donut-shaped   electronics and
movements with
automotive
vertical compliance.
industries.
Almost   Welding, painting,
Multiple rotary joints
Articulated   spherical with   assembly lines, spot
resembling a human
Robots   many degrees   welding, material
arm; highly flexible.
of freedom   handling.
Multiple arms   High-speed pick-
Complex
Parallel Robots   connected to a single   and-place in
polyhedral
(Delta)   platform, high speed   packaging and food
workspace
and precision.   processing.
b.   Derive the ARM matrix using the DH convention.   [10]
Compute the end-effector position (x, y, z) and overall orientation of the tool with
respect to the base frame.
(θ1 = 60∘, d2 = 150mm, a2 = 180mm)
Axis   𝜽𝒌   𝒅𝒌   𝒂𝒌   𝜶𝒌
1   𝜃1   0   0   −𝜋/2
2   0   𝑑2   𝑎2   0
4
********** 5 **********
--- page 6 ---
3
3
Q3   a. Analyze a 5 Axis Microbot Alpha II Robotic Arm and compute the following.   [20]
i.   Link coordinate diagram
7
ii.   Link coordinate table.
5
********** 6 **********
--- page 7 ---
8
iii.   Individual Link coordinate transformation matrices.
Q4   a. Compare different types of force sensors and write a short note on Tactile sensors.   [10]
Sensor   Working   Typical
Advantages   Limitations
Type   Principle   Applications
Measures
Sensitive to
Strain   strain-induced   High accuracy,   Load cells,
temperature,
Gauge   resistance   small size,   torque
requires
Sensors   change in a   robust   measurement
calibration
material
Generates   Cannot
electric charge   High-frequency   measure static   Vibration,
Piezoelectri
under   response, wide   forces, needs   impact force
c Sensors
mechanical   dynamic range   charge   measurement
stress   amplifier
Measures
change in   High sensitivity,   Sensitive to   Tactile
Capacitive
capacitance   good for   environmental   sensing,
Force
due to force-   dynamic/static   noise and   precision
Sensors
induced   forces   humidity   tasks
displacement
Measures
force by
Immune to   Surgical
Optical   detecting
electromagnetic   Complex and   robots,
Force   changes in
interference,   costly setup   delicate
Sensors   light
high sensitivity   manipulation
transmission
or reflection
********** 7 **********
--- page 8 ---
Uses changes   Contactless,   Sensitive to
Magnetic   Industrial
in magnetic   robust, good for   external
Force   automation,
field due to   harsh   magnetic
Sensors   automotive
applied force   environments   disturbances
Short Note on Tactile Sensors
•   Definition: Tactile sensors detect and measure properties related to touch, such
as force, pressure distribution, texture, and vibration.
• Function: They mimic the human sense of touch and provide feedback about
the surface being interacted with.
• Types: Include force-sensitive resistors, piezoresistive, capacitive tactile arrays,
and optical tactile sensors.
•   Applications: Used in robotic grippers for object manipulation, quality
inspection, and human-robot interaction.
• Importance: Enhance robot dexterity and safety by enabling precise grip
control and environmental awareness.
Tactile sensors are crucial for robots to perform delicate tasks requiring fine force
control and texture recognition, enabling safer and smarter robotic operations
b. Explain with proper block diagram, also list advantages and limitations of Hydraulic [10]
system.
•   Reservoir: Stores the hydraulic fluid (oil) required for the system.
• Pump: Converts mechanical energy into hydraulic energy by pressurizing the
fluid.
•   Filter: Removes impurities from the fluid to prevent damage to components.
•   Control Valves: Regulate flow and pressure; include directional control valves,
pressure relief valves, and flow control valves.
•   Hydraulic Actuator: Converts hydraulic energy into mechanical motion (linear
or rotary) to perform work.
•   Sensors: Measure pressure, position, or flow for feedback and control.
•   Controller: Manages the entire system operation based on sensor inputs and
programmed logic.
********** 8 **********
--- page 9 ---
Advantages of Hydraulic Systems
• High Power Density: Capable of generating very large forces and torques in a
compact size.
•   Precise Control: Smooth and accurate control over speed, force, and position.
•   Reliability: Robust and durable in harsh industrial environments.
• Overload Protection: Equipped with pressure relief valves to prevent damage.
• Simple Mechanism: Fewer mechanical parts compared to other drive systems.
Limitations of Hydraulic Systems
• Leakage Issues: Hydraulic fluids can leak, causing environmental hazards and
maintenance concerns.
• Complex Maintenance: Requires regular checking for fluid quality and system
integrity.
•   Cost: Initial system costs and maintenance may be high.
•   Bulkiness: Requires pipes, hoses, and reservoirs which add to system size.
•   Noise: Pump and fluid flow can generate operational noise.
Hydraulic systems are widely used in robotics and industrial machinery where large
force and precise control are essential despite their maintenance requirements.
Q5   a. Evaluate the values of performance index for the image and template given below. Also [15]
find the best match.
I(k,j)   2   1   0   1   2   1   2   1   T(k,j)
0   1   3   2   1   0   1   0
1   2   1   2   0
0   1   0   2   1
pos_x pos_y SSD ZNCC Performance Index
0   0   10.0 0.307 = 6
1   0   13.0 -0.255 = 7
2   0   15.0 -0.218 = 0
0   1   9.0 0.588 = 7
1   1   6.0 0.657 = 6
2   1   10.0 0.392 = 6
0   2   0.0 1.000 = 8
1   2   7.0 0.566 = 4
2   2   13.0 0.255 = 3
b. Explain the general properties of Inverse Kinematics.   [5]
General Properties of Inverse Kinematics
1. Multiple   Solutions:
Inverse kinematics often has multiple possible solutions for a given end-effector
position and orientation due to the manipulator's joint redundancies.
2. Existence   of   Solutions:
Solutions may not always exist for all desired positions; unreachable or singular
positions may have no valid joint configurations.
Q6   a. Explain with proper block diagram the internal architecture of a PLC System and [10]
explain each block in brief.
********** 9 **********
--- page 10 ---
Explanation of Each Block
1. Power Supply:
Provides regulated DC voltage to all PLC components, ensuring stable
operation.
2. Central Processing Unit (CPU):
The brain of the PLC, it interprets control instructions, executes the user
program, processes inputs, and updates outputs based on logic.
3. Memory:
• Program Memory: Stores the control program (firmware or user ladder
logic).
• Data Memory: Stores variables, input/output status, timers, counters,
and other data used during operation.
4. Input Interface:
Receives signals from external input devices such as sensors and switches. It
conditions and converts these signals into a format suitable for the CPU, often
providing electrical isolation.
5. Output Interface:
Sends control signals from the CPU to actuators and output devices. It converts
CPU output signals to appropriate power levels and provides isolation.
6. Communication Interface:
Allows the PLC to communicate with other PLCs, computers, or networks for
data exchange and remote control.
********** 10 **********
--- page 11 ---
b. Solve for [𝑞]𝐹if   [10]
4
[𝑞]𝑀= [ 6 ]
8
1
Let 𝐹= {𝑓1, 𝑓2, 𝑓3} and 𝑀= {𝑚1, 𝑚2, 𝑚3} be two initially coincident fixed and
mobile orthonormal coordinate frames, respectively. Suppose we perform the following
sequence of transformations on the mobile frame 𝑀:
1. Translate 𝑀along 𝑓3by 15 units
2. Rotate 𝑀about 𝑓2by -π radians
3. Rotate 𝑀about 𝑓1by π/2 radians
Q7   a. Analyze an ARM Matrix for 3 Axis PARA and answer the following.   [20]
𝐶123 −𝑆123 0 𝑎1𝐶1 + 𝑎2𝐶12
𝑆123   𝐶123 0 𝑎1𝑆1 + 𝑎2𝑆12
[   ]
0   0   1   𝑑3
0   0   0   1
i. Derive TCV from the arm matrix and corresponding equations.
ii. Derive joint equations for all the joints. (q1, q2, q3)
********** 11 **********
--- page 12 ---
aC, + aC2
4S) + aS)

exp (q3/7)

w2 a ee |
= 1+ W3 ~ ay ~ a5
Qz = tarccos ——____—___—..

2a, a5
!

q, = atan2 [a, — a,C,)w, + @g8,wo, (a, + a,C,)w, — a,S,W,]

{

q3 = 7 Inw,

FRR ICR] DA KH
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 7cfb50a7efd9

- Departments: Electronics and Telecommunication
- Programmes: BTech EXTC 7006
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_EXTC_7006/Robotics and Automation/ANS_Robotics and Automation(702EX0E014)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Robotics and Automation
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
a. Define a ‘Workspace’ and explain Hard automation used in industrial robots with   5
industrial examples.
A 'Workspace' in robotics refers to the total volume or area within which a robot’s
end-effector or tool can operate, move, and perform tasks effectively based on its
range of motion and geometric configuration. The workspace is determined by the
design of the robot’s joints, arms, and actuators, and it is essential for understanding
where and how the robot can reach and interact with its environment.
Hard Automation in Industrial Robots
Hard automation, also known as fixed automation, involves highly specialized
machines and systems designed to perform a specific set of tasks repetitively and
efficiently. These systems are generally rigid and unable to accommodate product
changes without major reconfiguration. Hard automation is characterized by the
use of mechanical components such as cams, gears, levers, and linkages to execute
operations with high speed and precision. It is commonly used for mass production
where reliability, consistency, and throughput are critical requirements.
Industrial Examples
Automotive Assembly Lines: Robots used for spot welding, painting, or inserting
components on car frames are configured for fixed operations, offering rapid cycles
and high repeatability.
Bottling and Packaging Plants: Systems where robots fill, cap, label, and seal
bottles in a continuous process exemplify hard automation, as the robots perform
programmed sequential steps with little variation.
Sheet Metal Stamping: Large presses fitted with robotic arms execute precise,
repetitive stamping operations to shape sheet metal parts. The robots are
programmed for a single product design and are not easily changeable for different
tasks. Hard automation provides efficiency and reliability for high-volume
********** 1 **********
--- page 2 ---
manufacturing but lacks the flexibility of soft or programmable automation
systems.
b. Explain corner point detection with necessary templates for corner detection in an   5
image.
Corner point detection is an essential image processing technique used to identify
points in an image where the intensity changes sharply in multiple directions,
indicating corners or intersection of edges. It is a key step in robotic vision and
object recognition because corners are stable features and easy to track within
different views of an object or scene.
Corner Point Detection: Concept
The process involves analyzing local regions of an image using mathematical
operators to find points where the pixel intensity has significant variations in both
the horizontal and vertical directions. These points typically denote places such as
the corner of a window, the tip of an object, or junctions in structural layouts.
Corners are useful in mapping, registration, and tracking, as well as for object
identification in robots.
Templates and Algorithms for Corner Detection
One common method is the Harris Corner Detector, which looks for regions where
the intensity changes rapidly in multiple directions. The Harris detector uses a
mathematical structure called the autocorrelation matrix for each pixel, with
templates that highlight changes in intensity.
Typical corner detection works by applying templates such as:
•   Horizontal and vertical edge templates (like Sobel operators)
• Diagonal edge templates
• The autocorrelation (structure) matrix, calculated over a window, with
corner points indicated where both eigenvalues of the matrix are large
Example of a simple corner detection template:
text
[ -1 0 1 ]
[ -1 0 1 ]
[ -1 0 1 ]
or
text
[ 1 0 -1 ]
[ 1 0 -1 ]
[ 1 0 -1 ]
These templates are applied in different orientations to check for high intensity
changes in pixels. Other algorithms include the Shi-Tomasi detector, which is an
improvement over Harris for stability under noise.
Applications
Corner detection is widely used in:
• Robot navigation and mapping
•   Object recognition/tracking
• Automated inspection
•   Stereo vision to calculate depth information
********** 2 **********
--- page 3 ---
Thus, corner point detection via feature-based representation (using templates like
Harris, Sobel, etc.) forms a foundational block in robotic perception systems,
enabling efficient and reliable identification of salient points in images.
c. Automation does not need to bring about unemployment, as some people fear, list   5
and explain three very positive reasons for it.
Automation does not necessarily lead to unemployment; in fact, it can bring about
several positive impacts in the workplace and economy. Here are three key reasons:
Increased Productivity and Economic Growth
Automation enables higher production output per hour of labor input, which is
essential for boosting a nation's standard of living and overall income levels. As
production becomes more efficient, companies can scale up operations and meet
larger market demands, resulting in economic growth and the potential creation of
new job opportunities in related sectors.
Enhanced Safety and Job Quality
Automation often allows employees to assume supervisory or technical roles
instead of performing repetitive, hazardous, or physically demanding tasks. For
example, activities like welding, die casting, and spray painting—known for their
health risks—can be mechanized, decreasing the chances of workplace injuries and
improving overall job quality.
New Employment Opportunities and Skill Development
The adoption of automation requires a workforce with new, specialized skills, such
as system programming, robot maintenance, and process optimization. This shift
encourages upskilling and creates new roles, including robot programmers,
maintenance engineers, and automation consultants, fostering innovation and long-
term employability for those who adapt to emerging technologies. Automation
helps make production more efficient, improves worker safety, and drives demand
for new skills—resulting in improved job quality and increased opportunities rather
than widespread unemployment.
d. Compare Microprocessor controlled system and programable logic controller.   5
********** 3 **********
--- page 4 ---
Q2   a. Explain reach and stroke in robotic manipulators and draw the workspace for cartesian, [10]
cylindrical and spherical robot.
Programmable Logic
Aspect   Microprocessor Controlled System
Controller (PLC)
Consists of CPU, memory,
Integrated CPU, memory, built-in
input/output interfaces, and requires
Architecture   IO modules, and rugged
additional components like RAM,
enclosure for industrial use.
ROM, and peripherals.
Programs written in low-level   Uses specialized languages like
languages (Assembly) or high-level   Ladder Logic, Function Block
Programming
languages (C/C++). Requires detailed   Diagram, and Structured Text
hardware-software knowledge.   designed for ease by technicians.
Highly reliable, designed for
Generally less robust for industrial   harsh industrial conditions
Reliability &
environments; sensitive to electrical   including electrical noise,
Robustness
noise, temperature, and shocks.   temperature extremes, and
vibrations.
Used in general-purpose computing,
Primarily for industrial
embedded systems, and applications
Applications   automation, repetitive tasks,
requiring complex computation and
process control, and robotics.
multitasking.
Higher initial cost due to
Lower initial cost but may need
Cost &   specialized hardware; modular
additional hardware/software;
Scalability   IO and networking for easy
scalable via hardware additions.
scalability.
Designed for ease of use with
Requires significant technical
Ease of Use &   intuitive programming and
expertise for programming, design,
Maintenance   diagnostic tools; maintainable by
and maintenance.
trained technicians.
b. Derive the ARM matrix using the DH convention.   [10]
Compute the end-effector position (x, y, z) and overall orientation of the tool with respect
to the base frame.
(θ1 = 30∘, θ2 = 45∘, a1 = 150mm, a2 = 120mm)
Axis   𝜽𝒌   𝒅𝒌   𝒂𝒌   𝜶𝒌
1   𝜃1   0   𝑎1   0
2   𝜃2   0   𝑎2   0
4
********** 4 **********
--- page 5 ---
3
3
Q3   a. Analyze a 4 Axis SCARA Adept I Robotic Arm and compute the following.   [20]
i.   Link coordinate diagram
ii. Link coordinate table.
iii. Individual Link coordinate transformation matrices.
7
5
8
********** 5 **********
--- page 6 ---
Q4   a. Explain with respect to robotic Position Sensors.   [10]
i.   Linear Position Sensors
ii.   Rotary Position Sensors
Compare the two also.
Robotic Position Sensors
Position sensors in robotics are devices used to detect and measure the position or
displacement of a robotic component with respect to a reference point. They are classified
mainly into two types:
i. Linear Position Sensors
•   Definition: Linear position sensors measure the displacement or movement of an
object along a straight line.
• Common Types:
•   Linear Potentiometer: Uses a resistive track and sliding wiper; output
voltage changes with linear displacement.
•   Linear Variable Differential Transformer (LVDT): Electromagnetic
sensor with primary and secondary coils plus a movable magnetic core;
displacement changes the induced voltage.
• Working Principle: Converts linear movement into a proportional electrical signal
(voltage or current).
•   Applications: Used in robotic arms for linear motion tracking, industrial
automation, throttle control in automotive, and assembly lines.
• Advantages: Simple, cost-effective, and provides accurate linear position
measurement.
•   Limitations: Limited measurement range; mechanical wear in potentiometers;
sensitive to environmental factors like dust and moisture.
ii. Rotary Position Sensors
•   Definition: Rotary position sensors measure angular displacement or rotation
around an axis.
• Common Types:
• Rotary Encoders: Can be incremental (measuring relative position
increments) or absolute (providing exact angular position and retaining it
after power loss). Typically uses an optical or magnetic disc.
********** 6 **********
--- page 7 ---
•   Resolvers: Electromagnetic devices providing continuous angular
feedback.
• Working Principle: Translates rotation into pulses or coded signals corresponding
to angular position.
•   Applications: Widely used in robotic joints, CNC machines for spindle position,
digital cameras for lens focus, and aerospace controls.
• Advantages: High precision, reliable, and suitable for full rotation measurements.
•   Limitations: Requires precise installation; optical types sensitive to dust and dirt;
higher cost compared to linear sensors.
Feature   Linear Position Sensors   Rotary Position Sensors
Measurement   Linear displacement (straight line   Angular displacement
Type   movement)   (rotation around an axis)
Common
Linear potentiometer, LVDT   Rotary encoder, resolver
Examples
Voltage proportional to linear   Pulses or coded signals
Output Signal
distance   proportional to angle
Linear axis tracking, assembly   Robotic joints, CNC spindle
Applications
lines, throttle control   control, camera focus
Simple, cost-effective, accurate   High precision, can measure
Advantages
over limited range   unlimited rotation
Limited range, mechanical wear,   Sensitive to installation, dust,
Limitations
environmental sensitivity   higher cost
b. Explain with proper block diagram, also list advantages and limitations of Pneumatics [10]
system.
Pneumatics System Explanation with Block Diagram
A pneumatics system uses compressed air to transmit and control energy. It is widely
used in industrial automation and robotics due to its simplicity, reliability, and cost-
effectiveness.
********** 7 **********
--- page 8 ---
•   Air Compressor: Generates compressed air from atmospheric air.
•   Air Reservoir: Stores compressed air and maintains system pressure.
•   Pressure Regulator: Controls air pressure for consistent operation.
•   Control Valves: Direct compressed air to actuators; types include directional
control valves, flow control valves.
•   Actuator: Converts compressed air energy into mechanical motion; e.g.,
pneumatic cylinders (linear motion) or pneumatic motors (rotary motion).
•   Sensors: Monitor position, speed, or pressure.
•   Controller: Controls the sequence and operation of valves and actuators based on
the feedback from sensors.
Advantages of Pneumatics System
•   Simplicity and Reliability: Pneumatic systems have fewer moving parts and are
relatively simple, making them reliable and easy to maintain.
• Speed and Force: Pneumatic actuators provide fast response and can deliver
considerable force.
•   Safety: Pneumatic systems are inherently safe in explosive environments since
they use compressed air, not electrical components.
•   Cost-Effective: Components are generally inexpensive and easy to install.
• Clean Operation: Compressed air does not contaminate environments like
hydraulic fluids.
Limitations of Pneumatics System
•   Compressibility: Air is compressible, causing less precise control of motion
compared to hydraulics or electric systems.
• Energy Efficiency: Pneumatic systems are less energy-efficient due to air leaks
and compression losses.
• Force Limitations: Pneumatic actuators provide lower force compared to
hydraulic actuators.
•   Noise: Air exhaust and compressor operation generate noise pollution.
•   Control Complexity: Achieving precise control requires sophisticated valves and
feedback, increasing system complexity.
Q5   a. Evaluate the zeroth, first, second order moments and centroid for the image given below. [15]
0   0   1   1   0   0   0   0
0   1   0   1   0   0   1   0
1   0   0   1   0   0   1   0
0   0   0   1   1   0   0   0
0   0   0   0   0   1   1   0
********** 8 **********
--- page 9 ---
0   1   0   0   0   0   0   0
1   0   0   0   1   0   0   1
0   0   0   1   0   0   0   0
7
3
b. Explain in brief Direct and Inverse Kinematic analysis of a Robotic ARM.   [5]
Direct (Forward) Kinematics
•   Definition: Forward kinematics is the process of determining the position and
orientation of the robot's end-effector (gripper or tool) in space based on given
joint parameters (angles for revolute joints, displacements for prismatic joints).
•   Purpose: To calculate where the robot's hand will be when the joint variables
are set.
•   Process: Uses geometric and trigonometric relations or transformation matrices
to map joint space coordinates to Cartesian coordinates of the end-effector.
• Example: Given   joint angles of a 3-axis robotic arm, forward kinematics
computes the exact position (x, y, z) and orientation of the arm's end-effector.
Inverse Kinematics
•   Definition: Inverse kinematics is the process of determining the required joint
parameters that will place the end-effector at a desired position and orientation
in space.
•   Purpose: To find the joint angles or displacements needed for the robot to reach a
specific point.
•   Process: Generally more complex than forward kinematics,   often requiring
solving nonlinear equations and may result in multiple or no solutions.
• Example: Given   a   target position   for the   robotic   hand,   inverse
kinematics computes the corresponding joint angles for the arm to reach that
position.
Q6   a. Explain with proper block diagram the basic PLC System and explain each block in brief. [10]
********** 9 **********
--- page 10 ---
Input Devices:
These are sensors and switches that detect changes in physical parameters like position,
temperature, pressure, or user commands. They convert real-world signals into
electrical signals for the PLC. Common devices include push buttons, limit switches,
photoelectric sensors, and temperature sensors.
Input Interface:
The input interface conditions, filters, and converts signals from the input devices into a
format that the processor (CPU) can understand. It provides electrical isolation between
the PLC and the input devices to protect the CPU from voltage spikes or noise.
Processor (CPU):
The CPU is the brain of the PLC. It executes the control program stored in its memory
by reading inputs, processing logic, and updating outputs accordingly. It contains the
arithmetic and logic unit (ALU), control unit, and internal memory. The CPU also
manages communication with external devices.
Memory and Program Storage:
This stores the user’s control program as well as data required for execution, such as
input/output status, timers, counters, and variables. Memory types include ROM (for
firmware), RAM (for user program and data), and non-volatile memory to retain the
program when power is off.
Output Interface:
Converts the CPU signals into suitable power and signals to activate actuators and
devices. It provides isolation and amplification as necessary. Output devices could be
motors, solenoids, valves, lights, or relays.
Output Devices/Actuators:
These perform the physical operations or actions based on the control signals from the
PLC output interface. Examples include hydraulic valves, pneumatic cylinders, motors,
and indicator lights.
b. Solve for [𝑝]𝐹if   [10]
********** 10 **********
--- page 11 ---
5
[𝑝]𝑀= [ 10 ]
15
1
Let 𝐹= {𝑓1, 𝑓2, 𝑓3} and 𝑀= {𝑚1, 𝑚2, 𝑚3} be two initially coincident fixed and mobile
orthonormal coordinate frames, respectively. Suppose we perform the following
sequence of transformations on the mobile frame 𝑀:
1. Rotate 𝑀about the fixed axis 𝑓3by π/2 radians
2. Translate 𝑀along 𝑓1by 10 units
3. Rotate 𝑀about the fixed axis 𝑓2by π radians
6
2
2
********** 11 **********
--- page 12 ---
Q7   a. Analyze an ARM Matrix for 4 Axis SCARA Adept I and answer the following.   [20]
𝐶1−2−4   𝑆1−2−4   0   𝑎1𝐶1 + 𝑎2𝐶1−2
𝑆1−2−4 −𝐶1−2−4   0   𝑎1𝑆1 + 𝑎2𝑆1−2
[   ]
0   0   −1   𝑑1 −𝑞3 −𝑑4
0   0   0   1
i.   Derive TCV from the arm matrix and corresponding equations.
ii.   Derive joint equations for all the joints. (q1, q2, q3 and q4)
5
5
4
3
3
********** 12 **********
````

## 2024-25 · Final-Exam · Sem 12 · Answer key · paper 8e113bb4050d

- Departments: Electronics and Telecommunication
- Programmes: BTech (ELECTRONICS & TELECOMMUNICATION
- Source: `02_Question_Papers/2024/Sem_12/Final-Exam/BTech (ELECTRONICS & TELECOMMUNICATION _e9090790/Robotics and Automation/ANS_Robotics and Automation(702EX0E014)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Apr 2025
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ELECTRONICS &
TELECOMMUNICATION ENGINEERING) SIX YEARS INTEGRATED PROGRAM
Year: VI/Semester XII(Exam Year: 2024-2025)
Subject: Robotics and Automation
Date: 30 Apr 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1
a) Explanation about the importance of direct kinematics in robotic manipulators. --- 05 M
Direct kinematics is crucial in robotic manipulators as it determines the position and orientation of the
end effector based on the given joint parameters, such as angles or displacements. This analysis is
essential for controlling the robot's movement, ensuring accuracy in tasks like assembly, welding, and
pick-and-place operations.
By solving the direct kinematics equations, engineers can predict the robot's behaviour without trial and
error, leading to more efficient programming and operation. Moreover, it serves as a foundation for
inverse kinematics, trajectory planning, and real-time control. Understanding direct kinematics also
helps in error detection, calibration, and optimization of robotic systems, ultimately enhancing their
reliability and precision in industrial and research applications.
b) Explanation about region growing technique used for image segmentation. --- 05 M
The region growing technique in image segmentation is a pixel-based approach that groups
neighbouring pixels with similar properties to form distinct regions. It starts with a seed pixel, chosen
based on predefined criteria such as intensity, color, or texture. Then, it examines neighbouring pixels
and adds them to the region if they meet the similarity condition. This process continues until no more
pixels satisfy the criteria.
For example, in medical imaging, region growing can be used to segment a tumor from an MRI scan
by selecting a seed pixel within the tumor and expanding the region based on intensity similarities.
This technique ensures accurate and contiguous segmentation but requires careful selection of the seed
point and similarity threshold to avoid over-segmentation or under-segmentation.
c) Constructional diagram of a solenoid actuator. --- 02 M
Explanation of working. --- 03 M
Solenoid is the simplest electromagnetic actuators that are used in linear as well as rotary actuations
for valves, switches, and relays. As the name indicates, a solenoid consists of a stationary iron frame
(stator), a coil (solenoid), and a ferromagnetic plunger (armature) in the center of the coil as shown
below.
********** 1 **********
--- page 2 ---
As the coil is energized, a magnetic field is induced inside the coil. The movable plunger moves to
increase the flux linkage by closing the air gap between the plunger and the stationary frame. The
magnetic force generated is approximately proportional to the square of the applied current i and is
inverse proportional to the square of the air gap δ , which is the stroke of the solenoid.
The solenoid comes with different types of plungers. For strokes less than 0.060 in., the flat face
plunger is recommended with a pull or push force three to five times greater than 60° plungers. For
longer strokes up to 0.750 in., the 60° plunger offers the greatest advantage over the flat face plunger.
When the coil is de-energized, the field decreases, and the plunger will return to the original location
either by the load itself or through a return spring. All linear solenoids basically pull the plunger into
the coil when energized. Push-type solenoids are implemented by extending the plunger through a hole
in the backstop. Return motion, upon de-energizing the coil, is provided by the load itself i.e., the
weight of the load and/or by a return spring, which can be provided as an integral part of the solenoid
assembly. Force, stroke, temperature, and duty cycle are the four major design and selection
considerations for solenoids.
d) PLC ladder logic program for Motor ON-OFF control with proper addressing. -- 05 M
********** 2 **********
--- page 3 ---
Q2.
a) Comparison between hydraulic drive and electric drive systems used for industrial robots. ---
04 M
Hydraulic Drives: They make use of hydraulic actuators that use pressurized fluid to create motion.
They are known for their high force and power, making them suitable for heavy-duty tasks in robotics.
The working principle of a hydraulic actuator is based on Pascal's law, which states that pressure
applied at any point in a confined incompressible fluid is transmitted equally in all directions. In a
hydraulic actuator, a pump pressurizes a fluid (usually oil), which is then used to move a piston. The
movement of the piston can then be used to create linear or rotary motion. Hydraulic actuators also
offer high durability and robustness. They can withstand harsh conditions and heavy loads, making
them suitable for use in challenging environments such as construction sites or industrial settings.
However, hydraulic actuators also have some limitations. They require a hydraulic system, which can
be complex and require maintenance. They can also be slower and less precise.
Electric Drives: They make use of electric actuators that convert electrical energy into mechanical
motion. They are among the most commonly used actuators in robotics due to their high speed,
precision, and ease of control. The working principle of an electric actuator is based on the use of an
electric motor. The motor generates rotary motion, which is then converted into linear motion or other
forms of motion through a series of mechanical components such as gears, belts, or screws. Electric
motors serve as the foundation for both linear actuators and rotary actuators. For instance, DC motors,
including stepper motors and servo motors, are widely used in various robotic configurations due to
their reliability. However, certain applications may require alternative motor types for specific needs.
Additionally, brushless DC motors are frequently chosen for their efficiency and extended operational
lifespan, making them a popular choice in numerous applications.
Structural Configuration of SCARA robot. --- 03 M
Structural Configuration of Articulated robot. --- 03 M
********** 3 **********
--- page 4 ---
b) Classification of proximity sensors. --- 03 M
1) Inductive Proximity Sensors
2) Capacitive Proximity Sensors- Conductive Capacitive and Dielectric Capacitive.
3) Ultrasonic Proximity Sensors
4) Optical (Photoelectric) Proximity Sensors- Through-Beam, Diffuse Reflective, and Retroreflective
Sensors
5) Magnetic Proximity Sensors
Constructional diagram of retroreflective proximity sensor. --- 03 M
Explanation of its working with reference to diagram. --- 04 M
Q3.
a) Link coordinate diagram for four axis SCARA Adept One robot. --- 02 M
********** 4 **********
--- page 5 ---
Tool configuration vector for SCARA robot. --- 02 M
Derivation of equation for Elbow joint. --- 02 M
Derivation of equation for Base Joint. --- 02 M
Derivation of equation for Vertical Extension joint. ---- 01 M
Derivation of equation for Tool roll Joint. --- 01 M
b) Constructional diagram of an absolute optical encoder. --- 03 M
Discussion of its working. ---- 05 M
Optical Encoder uses an opaque disk (code disk) that has one or more circular tracks, with some
arrangement of identical transparent windows (slit) in each track. A beam of light is projected to all
the tracks from one side of the disk. The transmitted light is then picked off using a bank of photo
sensors on the other side of the disk that typically has one sensor on each track. Since the light from
********** 5 **********
--- page 6 ---
the source is interrupted by the opaque areas of the track, the output signal from the probe is a series
of voltage pulses. This signal is interpreted to obtain the angular position and angular velocity of the
disk. Different types of optical encoders are Incremental encoder, Incremental encoder with quadrature
output and Absolute encoder. Absolute encoder has many pulse tracks on its transducer disk. When
the disk rotates, several pulses trains equal to the number of tracks on the disk, are generated
simultaneously. At a given instant, the magnitude of each pulse signal will have one of two signal
levels (i.e. binary state), as determined by level detector. This signal level corresponds to binary 1 or
0. Thus the set of pulse trains gives an encoded binary number. The pulse windows on the tracks can
be organized into some pattern (code) so that each of these binary numbers corresponds to the angular
position of the encoder disk at the time when the particular binary number is detected. It has several
rows of tracks, equal in number to the bit size of the output data word. It needs at least as many signals
pick off sensors as there are tracks. Commonly used to measure fractions of a revolution.
Reason for using Gray coding in absolute encoders. --- 02 M
There is a data interpretation problem associated with using binary codes in absolute encoder. For E.g.-
The transition from 0011 to 0100 requires three bits switching. Here rotation was from angle 2 to angle
3 actually rotation was from angle 3 to angle 4 such errors can be avoided using gray coding. If the
sensors are not aligned properly, manufacturing errors and printing on the disk have resulted in large
number of errors in binary code. However, in gray coding there is only one bit change in consecutive
position so more than one bit change can be very easily identified as caused due to errors.
Q4.
a) The image is of size 4*5 and template is of size 3*3, the possible translations are
0 < x < 1 and 0 < y < 2. --- 02 M
The performance indices are
P (0, 0) = 8
P (0, 1) = 32
P (0, 2) = 16   --- 06 M
P (1, 0) = 30
P (1, 1) = 04
P (1, 2) = 32
The best match is P (1, 1) = 04 --- 02 M
********** 6 **********
--- page 7 ---
b) Explanation about memory organization of PLC with relevant example. --- 10 M
Q5.
a) Various benefits of automation. ---- 03 M
1) Increased productivity
2) Increased product quality
3) Increased flexibility and convertibility
4) Reduced manpower
5) Reduction in accidents
6) Reduction in cost of product
7) Better inventory control
8) Increased profit
Block diagram of elements of an automation system. ---- 03 M
Description of each element. ---- 04 M
********** 7 **********
--- page 8 ---
b) The zeroth order moment m00 = 8 --- 02 M
The first order moments m10 = 20, m01 = 34 --- 02 M
Centroid = (2.5, 3.0) ---- 02 M
Second order moments m20 = 52, m02 = 84 and m11 = 58 --- 04 M
Q6
a) Pneumatic circuit design using proper symbols. --- 05 M
Electric control circuit design using proper symbols. --- 05 M
********** 8 **********
--- page 9 ---
b) Block diagram of PLC structure representing major components. --- 03 M
Explanation about each component used in PLC structure. --- 07 M
Q7.
a) Derivation of YPR matrix. --- 03 M
𝟎 𝟏 𝟎
𝒀𝑷𝑹(𝜽) = [ 𝟎 𝟎 𝟏 ]-- 03 M
𝟏 𝟎 𝟎
𝒓𝑭= [𝟎. 𝟓 𝟏. 𝟎 𝟎. 𝟓]𝑻 --- 02 M
Sketches for sequence of tool position after each rotation. --- 02 M
b) Identification of the components used in the given hydraulic actuation system. ----- 05 M
Single acting- spring loaded hydraulic cylinder, Hydraulic Pump, Tank, Filter, Pressure relief valve
(PRV), 3/2 manually operated spring return.
Explanation of the operation of the given hydraulic actuation system. ------ 05 M
The figure shows a two- position, three way, manually operated, spring offset directional control valve
( DCV ) used to control the operation of a single acting cylinder. In the spring offset mode, full pump
flow goes the tank via pressure relief valve. The spring in the rod end of the cylinder retracts the piston
as oil from the blank end drains back to the rank.
When the valve is manually actuated the pump flow goes to the cylinder blank end via DCV position
1. This extends the cylinder. At full extension, pump flow goes through the relief valve. Deactivation
of the DCV allows the cylinder to retract as the DCV shift into its spring offset mode
********** 9 **********
````
