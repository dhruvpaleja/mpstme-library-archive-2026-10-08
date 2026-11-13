# Robotic Systems Design: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 0a4693dee76f

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_Mechatronics_7004/Robotic Systems Design/ANS_Robotic Systems Design(702MH0C021)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: mixed (16 pages), mean OCR confidence 73.7
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: Robotic Systems Design
Date: 03 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20
]
a. Compare hard and soft automation with industrial examples.   5
Hard automation (also called fixed automation) and soft automation (also known as
flexible automation) are two key approaches in industrial automation, each suited to
different production requirements. The following table provides a clear comparison
with relevant industrial examples:
Feature   Hard Automation (Fixed)   Soft Automation (Flexible)
Uses specialized equipment   Uses programmable machinery to
Definition   designed for a specific, repetitive   perform various tasks and adapt to
task   changes
Low – dedicated to a single   High – easily adaptable to product
Flexibility
product or family   changes
Changeover   Long (requires significant
Short (re-programming possible)
Time   retooling)
Moderately high for variable
Productivity   Very high for specific products
products
Moderate (higher than hard per unit
Investment   High initial setup, efficient for
for large volumes, but cost-effective
Cost   mass production
for multiple product variants)
Automobile assembly lines (e.g., CNC machines, industrial robots in
Examples   body welding presses), bottling   electronics assembly, automated
plants, stamping machines   guided vehicles in warehouses
********** 1 **********
--- page 2 ---
Batch production, products with
Application   Mass production, high-volume,
frequent design changes or
Area   unchanging products
customisation
Soft Automation: Electronics manufacturing robots assembling different circuit boards,
CNC machines cutting a variety of component shapes with simple program changes—
such systems can adapt to changing products without major hardware changes.
Hard automation excels in speed and consistency for large-volume, fixed designs, while
soft automation provides adaptability for evolving product lines and batch production
needs.
b. Solve for [𝑚2]𝐹 following the motion mentioned below, Let 𝐹= {𝑓1, 𝑓2, 𝑓3} and 𝑀=   5
{𝑚1, 𝑚2, 𝑚3} be two initially coincident fixed and mobile orthonormal coordinate
frames respectively. Suppose we,
i.   Rotate M along 𝑓2 by 𝜋/4 radians
ii.   Also draw the vector diagrams
2
1
Final answer
[𝑚2]𝐹= [0 1 0]𝑇
2
********** 2 **********

[Text in pictures on this page, read by OCR]
1) Fundamental rotation matrix (about f / y-axis)

cosO 0 sin?
R,(@)=| 0 1 0 | with@= , cos9= %, sing = %.

—sin@d 0 cosé
So
ig
R(3)=| 0 1 0

29 4
--- page 3 ---
c. Define “workspace” and with neat diagram show how it is for a cylindrical, cartesian   5
and SCARA robot.
The workspace of a robot is the total area or volume in which the robot's end-effector
(or tool) can operate and move. It's also known as the work envelope and is determined
by the robot's physical design, including the length of its arms and the types of joints it
has. The workspace is a crucial factor when selecting a robot for a specific application,
as it dictates the physical space the robot can access to perform its tasks.
1. Cylindrical Robot
A cylindrical robot has a workspace shaped like a hollow cylinder. This is achieved
through a combination of a rotary joint at the base and prismatic joints that allow the
arm to move up, down, and in and out radially. This design is well-suited for tasks that
require a wide range of vertical motion and rotation around a central axis, like machine
tending or assembly on a central point.
2. Cartesian Robot
A Cartesian robot, also known as a gantry robot, has a rectangular or cubic workspace.
Its motion is defined by three perpendicular linear axes (X, Y, and Z), which allows it
to move in straight lines. This simple, rigid structure makes it ideal for applications
requiring high precision and linear movements, such as 3D printing, laser cutting, or
pick-and-place operations over a specific area.
3. SCARA Robot
A SCARA (Selective Compliance Assembly Robot Arm) robot has a quasi-cylindrical
workspace. It is designed for high-speed, precise tasks in a horizontal plane. The
SCARA robot typically has two parallel rotary joints that provide motion in the X-Y
plane and a single linear (prismatic) joint for vertical movement along the Z-axis. This
combination of joints results in a limited vertical reach but excellent speed and accuracy
for assembly and pick-and-place tasks.
d. Compare the functional differences between proportional, integral, and derivative   5
control actions with practical robotic scenarios.
In robotics, PID (Proportional-Integral-Derivative) control is a feedback loop
mechanism that precisely controls a system's output by calculating the difference
between a desired setpoint and the current process variable. Each of the three control
actions—proportional, integral, and derivative—has a distinct function that contributes
to the overall control strategy.
Functional Differences Between P, I, and D
The proportional action provides an immediate response to the current error, the
integral action corrects for past errors, and the derivative action anticipates future
errors. Together, they create a balanced and stable control system.
Proportional (P) Control
The proportional term addresses the current error between the setpoint and the
measured value. Its output is directly proportional to the magnitude of this error. For
example, if a robot arm needs to move to a specific position, a P controller will
********** 3 **********
--- page 4 ---
command a motor speed proportional to how far away it is. A larger error means a
faster motor speed. While this provides a quick response, it can lead to overshoot and
a steady-state error, where the arm settles slightly off its target.
Integral (I) Control
The integral term deals with the accumulation of past errors over time. This is crucial
for eliminating the steady-state error that the P term can't fix. The I term "remembers"
the offset and continues to increase the control output until the error is zero. In the robot
arm example, if the arm is consistently off by a small amount due to friction or a load,
the I term will slowly increase the motor's power until the arm reaches the exact target
position. However, if the I term is too aggressive, it can cause the system to oscillate
around the setpoint.
Derivative (D) Control
The derivative term anticipates future errors by considering the rate of change of the
current error. It provides a damping effect to the system, helping to reduce overshoot
and oscillations. For the robot arm, if the arm is moving too quickly towards its target,
the D term will apply a braking force to slow it down before it overshoots. This makes
the system more stable and helps it settle at the setpoint faster. The D term can be
sensitive to noise in the sensor data, which may cause erratic behavior.
********** 4 **********
--- page 5 ---
Q2   a. Derive the forward kinematic equations and find the position and orientation of Tool [10]
in workspace for the given kinematic parameter table for a 2-axis planar robot (d2 =
220mm, θ1 = 40∘)
2
2
2
2
2
b. Explain with a neat block diagram how a single-axis PID controller stabilizes a robotic
joint, discussing the effect of increased integral gain.   [10]
A single-axis PID controller (Proportional-Integral-Derivative) stabilizes a robotic
joint by continuously adjusting the motor's output to minimize the difference between
********** 5 **********

[Text in pictures on this page, read by OCR]
1. D-H parameters (given)

Axis k Oe dj, a ak
1 6; ty) Cy) —n/2
2 0 dy 0 0

We use the standard D-H homogeneous transform

Ty °= .
0 sin a, cos ay, dy

0 0 0 1

2. Individual link transforms

Link 1 (01, d; = 0,a, = 0, a, = —7/2)— substitute cosa; = 0, sina; = —1:
cos#; O —sin#, 0
0 sind; O cos), 0
‘~J}0 -1 0 0
0 0 0 1

Link 2 (02 = 0, d2,a2 = 0,a2 = 0):

100 0
, jo 10 0
T, =
001 ad
000 1
3. ARM (base — tool) matrix
cos#; O —sin@, —dysin6,
sing, O cos 0, d2 cos 4,
1? = T°T =
0 —1 0 0

0 0 0 1
--- page 6 ---
the desired joint position (setpoint) and the actual joint position (process variable). This
is achieved through a feedback loop.
Block Diagram and Functionality
The process is as follows:
•   Setpoint (Ki): This is the desired position or angle for the robotic joint. It's the
target value the controller aims to achieve.
• Process Variable (Ki): This is the actual, measured position of the robotic joint,
typically obtained from an encoder attached to the joint's motor.
•   Error (Ki): The core of the feedback loop, the error is calculated by subtracting
the process variable from the setpoint: . This value represents how far the joint
is from its target.
• PID Controller: This is the "brain" of the system. It takes the error signal and
calculates a control output based on three terms:
o Proportional (P): This term produces a control output proportional to the
current error. A larger error results in a stronger corrective action. It
helps in quickly reducing the error but can lead to oscillations if the gain
is too high.
o Integral (I): This term integrates the error over time. It's designed to
eliminate steady-state error, which is a persistent, small error that the
proportional term might not be able to correct. It ensures the joint
eventually reaches its exact target position.
o Derivative (D): This term calculates the rate of change of the error. It
anticipates future error and dampens oscillations. It acts like a brake,
slowing down the motor as it approaches the setpoint, preventing
overshoot.
• Control Signal (ut): The sum of the P, I, and D terms forms the control signal,
which is sent to the motor driver.
• Actuator (Motor & Gearbox): This receives the control signal and converts it
into mechanical torque or force to move the robotic joint.
• Sensor (Encoder): An encoder measures the joint's current position and feeds
this information back to the controller, closing the feedback loop.
Effect of Increased Integral Gain (Ki)
Increasing the integral gain (Ki) in a PID controller has a direct and significant effect
on the system's performance, primarily impacting the steady-state error and response
time.
•   Elimination of Steady-State Error: The primary purpose of the integral term is
to eliminate steady-state error. A higher means the controller accumulates the
error faster over time. This leads to a more aggressive corrective action to drive
the steady-state error to zero, ensuring the joint reaches and holds the exact
desired position.
•   Increased Overshoot and Oscillations: While a higher helps eliminate steady-
state error, it also makes the system more susceptible to overshoot and
oscillations. The integral term "remembers" past errors and keeps adding to the
control signal even as the proportional term is decreasing. This can cause the
joint to overshoot the target position and then oscillate around it before settling.
********** 6 **********
--- page 7 ---
• Slower Transient Response: Counterintuitively, a very high integral gain can
sometimes lead to a slower overall response. This is because the integral term
can cause the controller to become "wind-up," where it accumulates a large error
signal during a large initial transient, leading to a delayed reaction once the joint
approaches the setpoint.
• Reduced Stability Margin: An excessively high can push the system towards
instability. The aggressive accumulation of error can lead to a runaway control
signal, causing the joint to oscillate uncontrollably or even become unstable.
The system's stability margin is reduced, making it more sensitive to
disturbances.
********** 7 **********
--- page 8 ---
Q3   a. Analyze a 5 axis Microbot Alpha II Robotic Arm and compute the following.   [20]
i.   Link coordinate diagram
7
ii. Link coordinate table.
5
iii. Individual Link coordinate transformation matrices.
8
Q4   a. Solve for [𝑝]𝐹if [𝑝]𝑀= [6 8 10 1]𝑇, Let 𝐹= {𝑓1, 𝑓2, 𝑓3} and 𝑀= [10]
{𝑚1, 𝑚2, 𝑚3} be two initially coincident fixed and mobile orthonormal coordinate
frames respectively. Suppose we,
i.   Rotate M along 𝑓1 by 𝜋/2 radians
ii.   Translate M along 𝑓2 by 20 units.
iii.   Rotate M along 𝑓3 by 𝜋 radians
Also draw the vector diagrams.
********** 8 **********

[Text in pictures on this page, read by OCR]
TABLE 2-2 KINEMATIC PARAMETERS FOR THE ALPHA II ROBOT

Axis (] d a a Home
1 6; 215.0 mm 0 —1/2 0
2 0, 0 177.8 mm 0 0
3 6; 0 177.8 mm 0 0
4 64 0 0 —a/2 —n/2

5 4s 129.5 mm 0 6 0
--- page 9 ---
Step 1— Elementary homogeneous transforms

Rotation about f (x) by 7/2:

10 0 0
R z) 0 0 -1 0
AN=5 1 9 0
00 0 1
Translation along f? (y) by 20:
100 Of
T, (20) 1 0 20
ue 010
000 1]
Rotation about f (z) by 7:
-1 0 00
0 -1 00
R.(m) =
0 10
0 0 O01
-1 0 0 Oo] fi 0 0 0 -1 00 0
0 -1 0 0} JO 0 —1 20 0 0 1 —20
Tresutt = R:(7) M, = =
0 0 1 0} }0 1 0 +0 0 10 +0
0 0 oO 1/ {0 0 0 1 000 1
—6
[ple = |—10
8

FIC QF OH ar
--- page 10 ---
b. Develop a Link coordinate diagram and kinematic parameter table for Yaskawa   [10]
Motoman 6 axis Robot.
Link coordinate diagram   5
kinematic parameter table   5
Q5   a. Analyze the arm matrix derived from the kinematics parameter table given below:   [20]
Axis   𝜽𝒌   𝒅𝒌   𝒂𝒌   𝜶𝒌
1   𝑞1   0   0   0
2   0   𝑞2   0   −𝜋2 ⁄
3   0   𝑞3   0   0
3
3
3
i. Perform the Inverse Kinematics analysis and find equations for q1, q2 and q3.
********** 10 **********
--- page 11 ---
2
3
3
ii. Also solve for the values of Joint angles required to move to point p located at [10
12 16]
3
Q6   a.   List and elaborate on typical sources of steady-state error in robot control and suggest [10]
remedies for each.
Steady-state error is the difference between a robot's desired output and its actual output
after the system has reached a stable condition. This error can result from various
factors, including the control system's design limitations and external forces.
Minimizing this error is crucial for achieving high precision in robotics.
Sources of Steady-State Error
1. System Type and Input Signal: A primary source of steady-state error is the
mismatch between the control system's type and the nature of the input signal.
The system type is determined by the number of integrators (poles at the origin)
in its open-loop transfer function.
o Step Input (Constant Position): A robotic arm needs to hold a fixed
position. A Type 0 system will have a constant, non-zero error, meaning
the arm will not reach the exact target.
o Ramp Input (Constant Velocity): The arm needs to move at a constant
speed. A Type 1 system will exhibit a constant, non-zero error, causing
a persistent lag behind the desired trajectory. A Type 0 system would
have an infinite error.
********** 11 **********

[Text in pictures on this page, read by OCR]
1. From the third equation,

2. From the first two, form the radial distance in the ry-plane:

as = V/(—43 sing)? + (a3 cos)? = Vx? + y?.

Assuming the conventional prismatic range g3 > 0,

g= Vr?+y?.

3. To get q;, divide the pair:
©

sing, = a" cos gq) = x
3 3

A robust way to combine those in a single expression is with the two-argument

arctangent:

qi = atan2(—x, y) + 2kz, keZ.
--- page 12 ---
o Parabolic Input (Constant Acceleration): The arm needs to accelerate
continuously. A Type 2 system will show a constant error. Systems with
a lower type would have an infinite error.
2. External Disturbances and Environmental Factors: Robotic manipulators
often operate in environments with unpredictable forces that can push them off
their desired path.
o Gravity: A robotic arm's weight creates a bias on its joints, and the
required torque to counteract gravity changes depending on the arm's
configuration. A simple controller might not fully compensate for this
dynamic change.
o Friction: Friction in the robot's joints and gears resists motion, causing
the actual position to lag behind the commanded position. This is
especially noticeable at low speeds.
o Payloads: The weight of a held object changes the robot's dynamics,
altering the inertia and required motor torques. An uncompensated
system will show errors when carrying different loads.
3. Controller Limitations and Unmodeled Dynamics: Even with a well-
designed feedback loop, inherent limitations of the control system can introduce
steady-state errors.
o Proportional-only Control: A proportional-only (P) controller adjusts
the output based on the current error. While it can reduce the error, it
often leaves a small residual error because a perfect output would require
the error to be zero, which would then eliminate the control signal.
o System Nonlinearities: Real-world robots have complex, nonlinear
dynamics (e.g., backlash in gears, motor saturation) that are difficult to
model accurately. A linear controller may not be able to perfectly
compensate for these behaviors, leading to a steady-state error.
b. Explain in detail with schematic how robotic part inspection using a vision system is [10]
carried out in a robotic work cell.
Robotic part inspection using a vision system is a quality control process that uses a
robot to manipulate a part, while a camera system inspects it for defects. This process
is highly accurate, repeatable, and efficient, surpassing human capabilities. It's often
carried out in a robotic work cell, a self-contained, integrated system designed for a
specific task.
Step-by-Step Process of Robotic Part Inspection
1. Part Presentation: A part is delivered to a designated pick-up location within
the work cell, often by a conveyor system. The part may be in a random
orientation, which the vision system will correct for.
2. Image Acquisition: The robot's vision system captures an image of the part.
This can be a 2D image for tasks like label verification or a 3D scan using laser
scanners or structured light for tasks requiring precise dimensional
********** 12 **********
--- page 13 ---
measurements or surface defect detection. The lighting system is crucial here to
ensure a clear, well-lit image free of shadows or glare.
3. Image Processing and Analysis: The captured image is sent to the computer
for analysis. The image processing software, often powered by AI and machine
learning, performs a series of checks. It compares the captured image to a pre-
trained model of a perfect part, looking for specific criteria such as:
o Dimensional Accuracy: Verifying that the part's dimensions, features,
and tolerances are within an acceptable range.
o Defect Detection: Identifying surface flaws like scratches, cracks, dents,
or discoloration. AI algorithms are particularly good at this, as they can
"learn" what constitutes a defect from a large dataset of good and bad
parts.
o Component Presence: Confirming that all required components are
present and correctly assembled.
o Label/Barcode Verification: Reading and verifying text, barcodes, or
QR codes on the part.
4. Decision and Action: Based on the analysis, the controller makes a pass/fail
decision.
o   If the part meets all the quality criteria, the robot is commanded to place
it in the "OK" bin.
o   If the part is defective, the robot places it in the "NOK" (Not OK) bin,
or a specific bin for a particular type of defect.
Cycle Repetition: The robot retracts to its home position and waits for the next part,
repeating the entire cycle. The data from the inspection can also be logged and used to
create quality reports, track trends, and provide insights for process improvement.
Remedies for Each Source
1. Remedy for System Type/Input Mismatch:
o Add an Integrator: The most effective way to eliminate steady-state
error for a given input is to increase the system's type number by
adding an integrator in the forward path. A PID controller's integral (I)
term effectively does this. The integrator accumulates the error over
time, generating an increasingly strong control signal until the error is
eliminated. This ensures the robotic arm will eventually reach its target
position with zero error for a constant position command.
2. Remedy for External Disturbances:
o Integrator in the Control Loop: The integral term of a PID controller
is also highly effective at compensating for constant disturbances like
gravity and friction. It continuously increases the motor output to
overcome these resistive forces until the error is zero.
o Advanced Control Strategies: For more complex disturbances or
rapidly changing conditions, adaptive control or reinforcement
********** 13 **********
--- page 14 ---
learning can be used. These methods can estimate and compensate for
unmodeled dynamics and disturbances in real-time, improving tracking
accuracy and reducing errors. For instance, a hybrid approach combining
a traditional PID controller with a neural network can compensate for
modeling errors.
3. Remedy for Controller Limitations:
o Implement a PID Controller: The Proportional-Integral-Derivative
(PID) controller is the standard remedy for steady-state error in robotics.
The integral term is specifically included to eliminate steady-state error,
while the proportional and derivative terms handle the transient
response.
o Tuning the Controller: Proper tuning of the PID gains is critical.
Increasing the proportional gain can reduce steady-state error, but if it's
too high, it can lead to instability and oscillations. The integral gain
must be carefully tuned to eliminate the error without causing excessive
overshoot or sluggishness.
o Increase System Gain: In general, increasing the system's gain K can
reduce the steady-state error. However, like with the proportional term,
this can negatively impact stability, so a trade-off is often required.
Q7   a. Explain the concept and significance of Homogeneous Coordinate Transformation [10]
Matrix (HCTM) and Composite Rotation Algorithm in robotic manipulator kinematics.
The Homogeneous Coordinate Transformation Matrix (HCTM)
The Homogeneous Coordinate Transformation Matrix (HCTM) is a 4x4 matrix that
serves as a fundamental tool in robotics for representing and manipulating the pose
(position and orientation) of a rigid body in three-dimensional space. It combines a
3x3 rotation matrix and a 3x1 translation vector into a single, unified matrix. This
structure simplifies complex spatial transformations by allowing rotation, translation,
and even scaling to be represented by a single matrix multiplication.
The general form of an HCTM, , is:
•   is a 3x3 rotation matrix that defines the orientation.
•   is a 3x1 translation vector that defines the position.
• The bottom row, , allows for the mathematical convenience of matrix
multiplication.
The significance of HCTMs in robotics is that they enable forward kinematics, which
is the process of calculating the position and orientation of a robot's end-effector
based on its joint angles. By assigning a coordinate frame to each link of the robot,
the HCTM can be used to describe the relationship between adjacent frames. This
allows engineers to chain transformations from the base of the robot to the end-
effector.
The Composite Rotation Algorithm
The composite rotation algorithm is a method for combining a sequence of individual
rotations into a single, equivalent rotation matrix. In robotics, a manipulator's
movement is often a series of rotations around different axes. For example, a robotic
arm may rotate around its base (Z-axis), then its shoulder (Y-axis), and finally its
elbow (X-axis).
********** 14 **********
--- page 15 ---
A key aspect of this algorithm is the order of matrix multiplication. Since matrix
multiplication is not commutative, the order of rotations matters and will produce
different results.
There are two primary methods for composing rotations:
1. Fixed-Frame Rotation: Each subsequent rotation is performed with respect to a
fixed, global coordinate system. This is done by pre-multiplying the composite
rotation matrix with the next rotation matrix.
2. Current-Frame Rotation: Each subsequent rotation is performed with respect to
the robot's current, local coordinate system. This is done by post-multiplying
the composite rotation matrix with the next rotation matrix.
b. Discuss the pick-and-place operation of a robotic arm, describing the process steps and [10]
its speed control mechanism.
A pick-and-place robotic arm automates the movement of objects from one location
to another with high precision and repeatability. This is a common task in
manufacturing and logistics, used for everything from sorting products to assembling
components. The entire operation is a well-coordinated sequence of actions, managed
by a sophisticated control system.
Process Steps of a Pick-and-Place Operation
The typical pick-and-place process involves a series of sequential steps:
1. Object Detection: The process begins with the robot "seeing" the object. This
is usually done with a vision system that uses cameras and sensors to identify
the object's position, orientation, and characteristics. Advanced systems use AI
algorithms to determine the optimal grasp points for different items based on
factors like weight and fragility.
2. Motion Planning: Once the object is located, the robot's controller calculates
a precise, collision-free trajectory. This involves complex calculations to
determine the most efficient path for the arm to move from its current position
to the object's location. This path is designed to balance speed and accuracy.
3. Approach and Grasp: The robotic arm moves along the planned trajectory
and approaches the object. The end-effector (the robot's "hand," which could
be a gripper, suction cup, or magnetic attachment) is then activated to securely
grasp the item. The system may use force sensors to ensure the grip is strong
enough without damaging the object.
4. Transport: With the object securely held, the arm moves along a new, pre-
calculated path to the drop-off location. The control system continuously
monitors and adjusts the arm's movement to maintain a smooth acceleration
and deceleration, preventing the object from slipping or being damaged.
5. Placement and Release: The arm arrives at the designated placement location.
It then positions the object with high precision and releases it by opening the
end-effector.
6. Retraction: The arm moves away from the newly placed object to a safe
position, ready to begin the cycle again.
Robotic Arm Speed Control Mechanism
********** 15 **********
--- page 16 ---
The precise speed control of a robotic arm is crucial for its accuracy and efficiency.
This is achieved through a combination of hardware and software components
working in a feedback loop.
• Actuators and Motors: The arm's movements are powered by motors
(typically electric servo motors) that convert electrical energy into mechanical
motion. A motor controller sits between the main CPU and the motors, taking
digital commands and converting them into analog voltages or currents to
drive the motors.
• Sensors: To ensure smooth and precise motion, the robot relies on a variety of
sensors:
o Encoders: These are the most essential sensors for speed and position
control. They measure the rotation of the motor shafts, providing
feedback on the arm's current position and velocity. This information is
fed back to the controller in real time.
o Gyroscopes: These sensors measure the angular velocity and
orientation of the arm, allowing the control system to make fine-tuned
adjustments to maintain a smooth path.
o Force Sensors: These can detect the force or torque applied to the arm,
which is crucial for handling delicate objects and preventing collisions.
• Control System: The brain of the operation, the control system, uses the data
from the sensors to execute the planned motion. It compares the desired speed
(from the motion plan) with the actual speed (from the encoders) and adjusts
the motor's output accordingly. A common method for this is a PID controller
(Proportional-Integral-Derivative), which continuously works to minimize the
error between the desired and actual values. The PID controller compensates
for forces like gravity and inertia to ensure the arm follows its trajectory
accurately without overshooting or instability.
The speed and precision of the arm are determined by the ability of its control system
to process sensor data, calculate the necessary adjustments, and send commands to the
motors with minimal delay.
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 961d5f8c74f1

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_Mechatronics_7004/Robotic Systems Design/ANS_Robotic Systems Design(702MH0C021)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: mixed (14 pages), mean OCR confidence 73.1
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Robotic Systems Design
Date: 10 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
a. Describe the various operating environments an Industrial robot must work in and also   5
specify its effect.
Environment
Description   Effects on Robot Design/Operation
Type
Requires robustness to mechanical
Includes factory floors with
Manufacturing   stress, dust, vibration, and chemical
assembly lines, welding,
Environment   exposure. Needs modularity for diverse
painting, material handling
tasks.
Exposure to extreme   Robots must have protective covers,
Harsh
temperatures, chemicals,   corrosion-resistant materials, and sealed
Environment
moisture, and dust   joints for longevity and reliability.
Semiconductor,   Robots need special clean designs with
pharmaceutical industries   non-shedding materials, internal
Clean Room
with controlled temperature,   evacuation of particles, and strict
Environment
humidity, and particulate   contamination control to avoid damaging
matter   sensitive products.
Safety features, sensors, and compliant
Collaborative   Shared workspace with   mechanisms to prevent accidents and
Environment   human operators (Cobots)   ensure seamless human-robot
interaction.
Highly specialized robots with radiation
Hazardous or   Nuclear plants, underwater,
shielding, remote operation capability,
Extreme   space exploration, high
autonomy, and robust power systems to
Environment   radiation areas
operate safely in dangerous conditions.
********** 1 **********
--- page 2 ---
b. Let 𝐹= {𝑓1, 𝑓2, 𝑓3} and 𝑀= {𝑚1, 𝑚2, 𝑚3} be two initially coincident fixed and mobile   5
orthonormal coordinate frames respectively. Suppose we,
i.   Rotate M along 𝑓2 axis by angle ∅ radians.
Derive the fundamental rotation matrix which represents the above rotation.
c. Explain the role of the Screw transformation matrix in robotic coordinate transformations.   5
The screw transformation matrix is a powerful tool in robotics that represents a rigid
body's motion as a combination of a rotation about and a translation along the same axis.
This is based on Chasles' theorem, which states that any spatial displacement can be
represented by a single screw motion.
Role in Coordinate Transformations
The screw transformation matrix provides a compact and efficient way to describe the
movement of a robotic link. Unlike standard homogeneous transformation matrices
(HCTMs) that separate rotation and translation, a screw transformation matrix combines
them into a single mathematical entity. This is particularly useful in modern robotics,
especially for:
• Forward Kinematics: The product of exponentials (PoE) formula, a fundamental
approach to forward kinematics, relies on screw transformations. For a robot arm
with multiple joints, the overall pose of the end-effector is calculated by
multiplying a series of screw transformation matrices, one for each joint. Each
matrix represents the screw motion of that joint and its corresponding link. This
method is often more elegant and computationally efficient than the traditional
Denavit-Hartenberg (DH) convention for certain robot architectures.
• Trajectory Planning: When planning a robot's path, it's often more intuitive to
define a motion as a smooth twist from a starting point to an end point. The screw
transformation matrix allows for the representation of these continuous motions,
facilitating the generation of smooth, collision-free trajectories. It is an element of
the Lie group , which is the space of rigid-body motions.
•   Velocity Kinematics: The time derivative of a screw transformation matrix gives
a twist, which is a 6-vector representing the instantaneous linear and angular
********** 2 **********

[Text in pictures on this page, read by OCR]
3. Rotation about fixed f? (the y-axis)

When we rotate a coordinate frame M by an angle ¢ about the fixed y-axis (f7):
» m'andm* change direction.

. m (the rotation axis) remains unchanged.

Thus, geometrically:
m= cos¢f'+0-f?+sing f*,
m= 0-f'+1-f?+0-f%,
m’ = —sing f'+0- f? + cos¢ f*.

The fundamental rotation matrix representing rotation of the mobile frame M about the

fixed axis f? by an angle @ radians is:

: cosd 0 —sing
PRy=| 0 1 0
sind 0 cos@d
--- page 3 ---
velocity of a rigid body. This is used to relate the joint velocities to the end-
effector's linear and angular velocity, a key component of velocity kinematics.
The screw transformation matrix is derived from a screw axis, which is a 6-vector that
defines the direction, location, and pitch of the screw motion. The matrix is created by
taking the matrix exponential of a skew-symmetric matrix representation of the screw
axis.
d. Describe the impact of integral and derivative components in PID on robotic system   5
accuracy.
The integral and derivative components of a PID (Proportional-Integral-Derivative)
controller significantly impact a robot's accuracy by addressing different types of error.
The integral term handles persistent or long-term errors, while the derivative term
manages the rate of change of the error, helping to prevent overshoot and oscillations. A
well-tuned combination of these terms is essential for achieving precise, stable, and
accurate robotic motion.
Integral Component's Impact (I)
The integral component addresses steady-state error, a persistent, small difference
between the robot's desired position and its actual position. A proportional-only controller
might not be able to eliminate this error, as a constant force is often needed to counteract
external factors like gravity or friction.
• Eliminates Steady-State Error: The integral term continuously sums up the error
over time. As long as there is an error, the integral term's output will increase,
causing a stronger corrective action. This forces the system to drive the error to
zero, ensuring the robot eventually reaches its exact target position.
• Drawbacks: A high integral gain can lead to overshoot and instability. Because
the integral term "remembers" past errors, it can cause the robot to overcorrect,
moving past the setpoint. This can lead to oscillations around the target position
before the system settles.
Derivative Component's Impact (D)
The derivative component addresses the rate of change of the error, essentially predicting
future error. It acts as a dampener, counteracting rapid changes and helping the system
settle more quickly and smoothly.
• Reduces Overshoot and Oscillations: The derivative term applies a braking force
as the robot's error starts to decrease rapidly. This "pre-emptive" action slows the
system down as it approaches the setpoint, preventing it from overshooting and
minimizing oscillations.
• Improves Stability: By actively opposing fast movements, the derivative term
enhances the overall stability of the robotic system, making its motion smoother
and more controlled.
• Drawbacks: A high derivative gain can make the system overly sensitive to noise
in sensor readings. Small, rapid fluctuations can be amplified, leading to jerky or
erratic movements. In some cases, a high derivative gain can also slow down the
system's response time.
Q2   a. Derive all the Link coordinate transformation matrix from the kinematic parameter table [10]
given below of a 4 axes SCARA Adept I Robotic arm.
Axis   𝜽𝒌   𝒅𝒌   𝒂𝒌   𝜶𝒌
1   𝜃1   𝑑1   𝑎1   𝜋
2   𝜃2   0   𝑎2   0
3   0   𝑑3   0   0
4   𝜃4   𝑑4   0   0
********** 3 **********
--- page 4 ---
2
*
5
b. Explain the importance of feedback control in robotic systems. Contrast it with open-loop [10]
control with examples.
Feedback control is crucial in robotic systems because it allows automatic correction of
errors and disturbances during operation, ensuring accuracy, stability, and robust
performance. In feedback control, sensors measure the output or state, compare it to the
desired input (reference), and the controller adjusts the actuator inputs to minimize the
********** 4 **********

[Text in pictures on this page, read by OCR]
2 — Individual link transforms Aj ... Ay
Link 1: 0, d,, ai, a, =7
Use cosm = —1, sin = 0. Plug in:

cos#; sin; 0 a,cosh;

A sin®; —cos#; O asin
J 0 0 1 dk
0 0 0 1
(Notice the second column becomes — sin 6; cos = — sin 0,(—1) = sin @,, etc. third

column entries involving sin @; vanish.)

Link 2: 2, dz = 0, a2, a2 = 0

With cos 0 = 1, sin0 = 0:

cos@, —sinO. 0 aycos6,

Ay = sinf. cos#; 0 aysin®
0 0 1 0
0 0 0 1

This is a pure planar rotation about z and a translation along x by dg in frame 2.

Link 3: 6; = 0, d3, az = 0, a3 = 0

03 = 0 > cs = 1,83 = 0; a3 = 0

100 0
010 0
As= lo 0 1 asl?
0001

i.e. a pure translation along the local z-axis by d3 (prismatic joint).

Link 4: 64, dy, ay =0, ay =0

cos#, —sinés 0 O

A sinf; cos; O 0
4 1 0 0 1 ds
0 0 0 1

This adds final end-effector rotation about the local z and translation along z by dy.
--- page 5 ---
difference (error), allowing the system to respond dynamically to changes in load,
environment, or parameters(see the generated image above).RSD-Set-A_Synopsis3.docx
Importance of Feedback Control in Robotics
• Error correction: Continuously compares actual vs desired position, velocity, or
force to reduce deviations.
• Disturbance rejection: Compensates for unexpected external forces or changes.
• Improved precision and stability: Maintains system stability even in uncertain or
varying conditions.
•   Adaptability: Can adjust parameters in real-time to changing dynamics and
payloads.
•   Safety: Prevents excessive movement or collision by correcting motions actively.
Open-Loop Control Contrast
An open-loop control system operates without feedback — it sends commands to actuators
based only on input instructions without measuring actual output. Such systems cannot
correct errors once an action starts and are suited only for repeatable, predictable processes
without disturbances(see the generated image above).
Feature   Feedback Control (Closed-Loop)   Open-Loop Control
Error   No correction once command is
Yes, continuously corrects errors
correction   issued
Can be unstable if system dynamics
Stability   Maintains stability under disturbances
change
High accuracy due to real-time   Accuracy depends on model
Accuracy
adjustments   accuracy
More complex due to sensors,
Complexity   Simpler, fewer components
feedback, and controllers
Robotic arm position control using   Conveyor belt running at fixed
Examples   encoders, autonomous robot   speed without adjustment, timed
navigation with sensors   motor operations
Examples
• Feedback Control: A robotic manipulator uses encoder feedback for precise joint
positioning, correcting deviations due to payload changes.
• Open-Loop Control: A pick-and-place robot that performs repetitive motions
without sensor feedback, working effectively if parts are always positioned
perfectly.
Feedback control is essential for adaptable, precise, and safe robotic operation, while open-
loop is used in simpler, highly predictable tasks(see the generated image above).Feedback
control is vital in robotic systems as it provides continuous error correction by comparing
the actual output with the desired input, ensuring precision, stability, disturbance rejection,
and adaptability during operation. It actively adjusts actuator inputs based on sensor
measurements, which enhances accuracy and robustness especially in dynamic or
uncertain environments.RSD-Set-A_Synopsis3.docx
In contrast, open-loop control operates without feedback; it sends commands to actuators
based solely on predefined inputs without sensing actual output. Such systems cannot
correct errors once execution begins and are suitable only for repeatable, disturbance-free
tasks.
Q3   a. Analyze a 5 axis RHINO XR3 Robotic Arm and compute the following.   [20]
********** 5 **********
--- page 6 ---
i.   Link coordinate diagram
7
ii. Link coordinate table.
5
iii. Individual Link coordinate transformation matrices.
8
Q4   a. Solve for [𝑚1]𝐹following the motions mentioned below, Let 𝐹= {𝑓1, 𝑓2, 𝑓3} and [10]
𝑀= {𝑚1, 𝑚2, 𝑚3} be two initially coincident fixed and mobile orthonormal coordinate
frames respectively. Suppose we,
********** 6 **********

[Text in pictures on this page, read by OCR]
Axis a d a a Home
1 a a 0 —x/2 0
2 a2 0 a2 0 =7/2
3 qa 0 ay ii] m/2
4 qa ia] ds —a/2 0
5 qs ds 0 0 —a/2
--- page 7 ---
i.   Rotate M along 𝑓2 by −𝜋 radians
ii.   Translate M along 𝑓1 by 100 units.
Also find [𝑚1]𝐹 if the order of rotation and translation is reversed. Also draw the vector
diagrams.
5
Part A
ParT B
5
b. Describe bounded deviation algorithm and how it enhances robot motor control.   [10]
The bounded deviation algorithm is a method for simplifying a robot's trajectory by
approximating a series of setpoints (the desired path) with a single, smoother path. It works
by taking a sequence of waypoints and creating a new, simplified path that stays within a
specified maximum distance (the "bounded deviation") of the original path. This enhances
robot motor control by reducing the number of complex calculations and motor commands,
leading to smoother, more efficient, and faster motion.
How It Works
The algorithm works as follows:
1. Waypoint Path: The robot's desired path is initially defined by a series of discrete
points or waypoints. This path is often generated by a higher-level motion planner
and may contain many redundant or closely spaced points.
2. Starting Point: The algorithm begins with the first point in the waypoint list.
3. Path Approximation: It then extends a line segment from this starting point to
subsequent waypoints, one by one. For each new waypoint, it checks if the entire
line segment between the starting point and the current waypoint stays within the
defined deviation boundary of the original path.
4. Tolerance Check: The "bounded deviation" is a user-defined tolerance. If the line
segment deviates from the original path by more than this tolerance, the algorithm
determines that the segment is too long. The last point before the deviation
exceeded the boundary is selected as the next waypoint.
********** 7 **********

[Text in pictures on this page, read by OCR]
-1 0 0 —100
o 1 0 0
o @ -1 0
o 0 0 1

Ty =

* Orientation (columns of Ft) is same as Case A:

im? |* = |-1,0,0)"
--- page 8 ---
5. New Waypoint: A new, straight-line segment is then drawn from the start of the
previous segment to this new waypoint. This point becomes the new starting point
for the next iteration.
6. Iteration: The process repeats, with the algorithm building a series of straight-line
segments that approximate the original path while remaining within the specified
deviation boundary. The result is a simplified, "smoothed" path with far fewer
waypoints.
Enhancement of Robot Motor Control
The bounded deviation algorithm significantly enhances robot motor control in several
ways:
• Smoother Motion: By replacing a series of small, discrete movements with longer,
continuous segments, the algorithm minimizes abrupt changes in velocity and
acceleration. This allows the robot's motor controller to execute smoother
movements, reducing wear and tear on the mechanical components and improving
the overall quality of the motion.
• Reduced Computational Load: With fewer waypoints to track and process, the
robot's controller has less data to handle. This frees up computational resources,
allowing the controller to focus on real-time feedback and dynamic adjustments,
leading to more responsive and accurate control.
• Increased Speed and Efficiency: The simplified path allows the robot to move
more efficiently. The robot doesn't have to constantly accelerate and decelerate to
hit a large number of closely spaced waypoints, which translates to faster cycle
times and increased productivity.
• Improved Accuracy: While it simplifies the path, the algorithm ensures that the
new path remains within a defined tolerance of the original. This allows the user to
balance the need for speed and efficiency with the required level of accuracy. By
setting a small deviation boundary, the robot's path will be very close to the
original, while a larger boundary can be used for less critical tasks to maximize
speed.
Q5   a. Analyze the arm matrix derived from the kinematics parameter table given below:   [20]
Axis   𝜽𝒌   𝒅𝒌   𝒂𝒌   𝜶𝒌
1   𝑞1   𝑑1   0   −𝜋2 ⁄
2   0   𝑞2   0   −𝜋2 ⁄
3   0   𝑞3   0   0
i. Perform the Inverse Kinematics analysis and find equations for q1, q2 and q3.
ii. Also solve for the values of Joint angles required to move to point p located at [24 36
48]
********** 8 **********
--- page 9 ---
(B Step: Link Transformation Matrices

General DH transformation matrix:

cos#; —sin@;cosa; sin@jsina; a; cos6;

A= sin@; cos@;cosa;   —cos@;sina; a;sin6;
_— 0 sin a; COs Qj d;
0 0 0 1

2a) Link 1 (61 = q1, d1 constant, a1 = 0, a1 = -m/2)

cosgq;) O -—sing, O

A= sing, 0 cos qi 0
rm] 0 -1 0 dy
0 0 0 1

2b) Link 2 (62 = 0, d2 = q2, a2 = 0, a2 = -n/2)

1 0 00
0 0 10
A= Jy 4 0 w
0001

2c) Link 3 (63 = 0, d3 = q3, a3 = 0, a3 = 0)

100 0
010 0
A3=
0 0 1 gq
000 1
3a) Compute A1*A2
cosqm 0 -—sing O 1 0 0 0 cosgi; sing) 0 —singge
AA, = sings 0 cos qi 0 0 O 1 Of] _ |sing: —cosqm 0 cos qig2
me) 0-1 0 d;|]0 -1 0 ql | 0 0 -1 d,
0 0 0 1 0 0 0 1 0 0 0 1
3b) Multiply by A3
cosg; sing; 0 -singg|}]1 0 0 0 cosq, sing; 0 —sin qq.
_ _ |sing. —cosq 0 cos gig2 0 1:0 Of _ |sing: —cosq O cos gig2
T = (AiA2)As = |g 0 4 a 001 q{| | 0 0 -1 d-4q
0 0 0 1 0001 0 0 0 1

FIC QF OH ar
--- page 10 ---
2
3
Q6   a. Compare the features and applications of open-loop and closed-loop robotic control [10]
systems.
Open-Loop Control System
An open-loop control system operates without any feedback mechanism. It sends a
command to a robotic arm, and the arm executes the motion based on a pre-programmed
sequence of instructions, without verifying if the desired outcome was achieved. The
controller assumes that the action will produce the correct result.
Features
• No Feedback: There are no sensors to measure the actual position, velocity, or
force of the robotic arm. The system doesn't know if an error has occurred.
• Simple and Low-Cost: The absence of sensors and complex feedback algorithms
makes open-loop systems simpler to design and less expensive to manufacture.
• Inaccurate and Prone to Errors: Since the system cannot correct for external
disturbances, such as unexpected loads or friction, its accuracy is often low. The
final position of the arm might deviate significantly from the desired position.
•   Non-Iterative: The output is not compared to the input, so the system cannot adjust
its actions in real time.
Applications
Open-loop systems are used for simple, low-precision tasks in highly predictable and
controlled environments.
• Automated Conveyors: Moving items at a fixed speed.
• Basic Pick-and-Place: Used when the robot's motion is highly repeatable and the
payload is consistent, such as in simple component transfer tasks.
• Some Washing Machines: The machine runs a pre-programmed cycle for a set
amount of time without checking the cleanliness of the clothes.
Closed-Loop Control System
********** 10 **********

[Text in pictures on this page, read by OCR]
Step 1: Solve q1

From FK equations:

r= -qqsing, y= q2cosq
© Divide y/x:
¥Y_ cos _
= = ——— =-cotq
2 —q sing
q, = arctan 2(—z, y)
Substitute:

qi = arctan 2(—24, 36)

qi = arctan 2(—24, 36) ~ —0.588 rad ~ —33.69°

Step 2: Solve q2

= Vr? + yp = 242 + 362 = V576 + 1296 = 1872 ~ 43.27

Step 3: Solve q3
z=d,—-q = g3=d-2z
© If d is known (say, constant), e.g., assume d; = 100 (typical link offset), then

43 = 100 — 48 = 52
--- page 11 ---
A closed-loop control system, also known as a feedback control system, uses sensors to
monitor the robot's output and adjust its actions in real time. It continuously compares the
actual output to the desired input and makes corrections to minimize the error.
Features
• Feedback Mechanism: Sensors like encoders, gyroscopes, and force sensors
provide real-time data about the arm's state.
• High Accuracy and Robustness: The system can correct for external disturbances
and unmodeled dynamics, making it highly accurate and reliable.
• Complex and High-Cost: The use of sensors, a controller with a feedback
algorithm (like a PID controller), and more complex wiring increases the system's
cost and complexity.
•   Iterative: The system continuously adjusts its output based on the feedback loop
until the error is minimized.
Applications
Closed-loop systems are essential for applications requiring high precision, adaptability,
and reliability.
•   Industrial Robotic Arms: Used in manufacturing for welding, painting, and
precision assembly where the robot must precisely follow a path and apply a
specific force.
•   Surgical Robots: Used in delicate operations where extreme precision and a real-
time response to the environment are critical.
• Autonomous Vehicles: The control system uses sensors to continuously adjust
steering, braking, and acceleration to follow a planned path and react to its
surroundings.
b. Derive the tool configuration needed to grasp the part in figure given below.   [10]
Assume the position of part from the camera too be [0 -5 19] and position of camera from
the base of the robot to be [15 25 20].
********** 11 **********
--- page 12 ---
3
3
1
3
Q7   a. Let 𝐹= {𝑓1, 𝑓2, 𝑓3} and 𝑀= {𝑚1, 𝑚2, 𝑚3} be two initially coincident fixed and mobile [10]
orthonormal coordinate frames respectively. Suppose we,
i.   Rotate M along 𝑓1 by 𝜋/2 radians
ii.   Rotate M along 𝑓2 by −𝜋/2 radians.
iii.   Rotate M along 𝑓3 by 𝜋 radians
Derive the Yaw-Pitch-Roll Transformation Matrix and find the resultant rotation matrix
by substituting the given values. Also draw the vector diagrams.
5
********** 12 **********

[Text in pictures on this page, read by OCR]
The = Tene" Titers

= (Totten) ' Titers
ro -1 0 15) [0-1 0 0
_|-i 0 0 25 -1 0 0-5
~ 10 0 -1 20 0 oOo -1 19
10 0 0 ff 0 0 0 1
ro -1 0 2]f 0-1 0 0O
_|-l1 0 0 15}]-1 0 Oo -5
~ 1a o -1 2}]/ 0 oO -1 19
fo 0 0 1ff0 0 0 1
1 0 0! 30
_ jo 1 08 15
~ 10 0 bf 1

1— Fundamental rotation matrices

Using standard right-handed active rotations (rotate vectors):

1 0 0 cos#@ 0 sin@
R:(¢)= |0 cosé —sind|, R,(@)= 0 1 0 |,
0 sind cosd —sin@ 0 cosé@

cosy —sinw 0
R.(v)=|sind’ cosd 0
0 0 1

Then the general Yaw-Pitch-Roll matrix (extrinsic roll—pitch—yaw) is

[RW,,6) = R.(Y) Ry(6) Re(¢)-]

Multiplying those three gives the symbolic form (useful to lecture from):
R(wv,0,¢) = |sinvcos#@ sinwsin#ésind+cosycosd sinwsin#cos@— cosy sind

—sind cos @ sind cos @ cos

(You can derive that by multiplying the three 3x3 matrices — it's a standard result.)
--- page 13 ---
5
b. Explain the concept of reach and stroke of a robotic arm. Classify robots based on drive [10]
systems with examples.
Reach and Stroke of a Robotic Arm
• Reach: The reach of a robotic arm refers to the maximum horizontal distance its
end-effector can extend from the center of its base. It defines the size of the
robot's workspace, which is the total volume of space the arm can access. A
robot's reach is determined by the lengths of its links and the joint configurations.
• Stroke: The stroke of a robotic arm, particularly for linear axes, is the maximum
distance the robot can move along a straight line. For a prismatic joint, the stroke
is the total travel distance of the sliding link. In the context of a robotic arm, it can
also refer to the total range of motion of a single joint, whether rotational or
linear.
Classification of Robots Based on Drive Systems
Robots can be classified into three main types based on the drive systems that power their
joints:
1. Electric Drives
This is the most common type of drive system in modern robotics. Electric motors,
usually DC or AC servo motors or stepper motors, provide the torque and speed for
joint movements.
•   Features: Electric drives offer precise control over speed, position, and
acceleration. They are clean, quiet, and highly energy-efficient.
•   Applications: Found in a wide range of robots, from large industrial manipulators
used for welding and assembly to small, precise robots used in electronics
manufacturing and medical surgery.
• Examples:
********** 13 **********

[Text in pictures on this page, read by OCR]
2 — Substitute the given angles
The problem gives the sequential rotations about the fixed axes:
* Rotate about f! by ¢ = ; (roll),

* Rotate about f? by @ = 5 (pitch),
* Rotate about f* by o = x (yaw).

Compute each elementary matrix (exact trig values):

us _ : . .
cos>=0, sin5=1, cos(— $)=0, sin(- §) =-1, cost=-1, sinx=0.
So

10 0 00 -1
R.(¥)=|0 0 -1], &,(-%)=]0 1 Of,
0 0 10 0
-1 0 0
RAr)=|0 -1 0
0 o 1
Now multiply

R= R(x) Ry(~3) Re (3).

Carrying out the product (I've checked the algebra carefully) gives the resultant rotation
matrix

010
R= |0 01
10 0
--- page 14 ---
o Industrial Robots: A 6-axis robot arm in an automotive factory for
welding or painting.
o Collaborative Robots (Cobots): Robots designed to work safely
alongside humans in manufacturing environments.
2. Hydraulic Drives
Hydraulic drives use pressurized fluid to power linear or rotary actuators. A pump
pressurizes the fluid, which is then directed to the actuators to create motion.
•   Features: Hydraulic systems are known for their ability to generate immense
force and high power-to-weight ratios. They are suitable for heavy-duty
applications. However, they can be messy due to oil leaks and require more
maintenance.
•   Applications: Used in applications that require moving very heavy loads.
• Examples:
o Heavy-Duty Robots: Robots used in foundries, forging, and stamping
operations.
o Construction and Mining Robots: Large manipulators for demolition or
excavation.
3. Pneumatic Drives
Pneumatic drives use compressed air to power linear or rotary actuators. The compressed
air is controlled by valves to move pistons in cylinders or rotate motors.
•   Features: Pneumatic systems are simple, inexpensive, and fast. They are clean
and easy to maintain. However, they offer less precise control over speed and
position compared to electric or hydraulic systems.
•   Applications: Ideal for simple, fast, and repetitive tasks, especially in pick-and-
place operations.
• Examples:
o Simple Pick-and-Place Robots: Used for sorting objects on a conveyor
belt.
o Automated Grippers: Robotic grippers that open and close using a
pneumatic cylinder to grasp and release objects.
********** 14 **********
````
