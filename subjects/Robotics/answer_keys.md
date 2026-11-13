# Robotics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper a7fe8066178e

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AI_7012/Robotics/ANS_Robotics(702AI0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Robotics
Date: 06 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 1   a. Explain different types of operating environment for the robot in industry with   [05]
necessary precautions to be taken.
Environment-wise precautions
Normal production floor: Use fences, interlocks, emergency stop buttons, warning
signs, and defined safety zones to keep workers outside the robot work envelope.
Dusty or dirty environment: Choose robots designed for dirty conditions, protect
sliding parts and cables, and carry out regular cleaning and inspection to prevent
wear or malfunction.
Hot environment, welding, foundry: Use heat-resistant components, shielding, and
protective routing for cables and sensors; also protect workers from thermal
hazards and sparks.
Wet, chemical, food, or clean-room area: Select robots with sealed construction
suited to washdown, contamination control, or chemical exposure, and maintain
strict hygiene or contamination procedures as required.
Hazardous or explosive area: Use specially rated equipment, eliminate ignition
sources, and follow strict area safety procedures because flammable surroundings
increase risk.
Human-robot shared workspace: Use light curtains, safety mats, floor sensors,
presence detection, speed limiting, and safe stop features to reduce collision risk.
General precautions
********** 1 **********
--- page 2 ---
Necessary precautions for all robot environments include a proper risk assessment
before installation, selecting the robot to match the task and surroundings, training
workers in hazards and emergency procedures, and applying lockout/tagout during
maintenance. Regular inspection of guards, sensors, electrical systems, and
emergency stops is also essential because electrical faults, unexpected motion, and
unauthorized entry are common industrial robot hazards.
CO- 2 b Compare proportional and integral control systems on various parameters.   [05]
.
Parameter   Proportional (P) control   Integral (I) control
Control   Depends on present error   Depends on accumulated error
action   magnitude   over time
Response   Slower because output builds
Fast and immediate
speed   gradually
Steady-   Usually cannot eliminate   Eliminates steady-state error or
state error   offset completely   offset
Initial
Strong for sudden error   Weak initially; increases with
corrective
change   time if error persists
effort
Generally better than I-only,   More likely to increase
Stability   but too high gain can cause   oscillation and instability if too
oscillation   strong
Overshoot   Can increase overshoot when   Often increases overshoot
tendency   gain is high   because of accumulated action
Moderate, due to residual   Higher steady-state accuracy
Accuracy
offset   because offset is removed
Harder to tune because
Tuning
Comparatively easier to tune   excessive integral action can
difficulty
destabilize the system
Used when quick response is
Used when very small or zero
Suitability   more important than zero
steady-state error is required
offset
Main   Slow response, oscillation risk,
Residual error remains
drawback   and windup problem
CO- 4   c. For a fixed frame F and mobile frame M initially coincident, suppose we perform   [05]
following operations:
********** 2 **********
--- page 3 ---
(i) Rotate M along f 2 axis by -π/2 radians,
(ii) Translate M along f 1 axis by 12 units.
Derive the resultant transformation matrix. Draw vector diagrams.
0 0 −1 0
1. Rotation about fixed 𝑓2 axis by −𝜋/2: 𝑅𝑦(−𝜋/2) = [ 0 1 0   0 ]   2
1 0 0   0
0 0 0   1
1 0 0 12
2. Translation along fixed 𝑓1 axis by 12 units: 𝑝= [ 0 1 0 0 ]
0 0 1 0
0 0 0 1
3. Resultant transformation matrix:   2
0 0 −1 12
0 1 0   0
[   ]
1 0 0   0
0 0 0   1
1
CO- 3 d   Explain kinematic parameters with help of neat diagram, also comment on when   [05]
.   they will be constant or variable.
(With Diagrams)
Meaning of the parameters
• 𝜃𝑘 joint angle: rotation about the previous joint axis 𝑧𝑘−1.
• 𝑑𝑘 joint displacement: translation along the previous joint axis 𝑧𝑘−1.
• 𝑎𝑘 link length: distance between successive joint axes measured along 𝑥𝑘.
• 𝛼𝑘 link twist: angle between 𝑧𝑘−1 and 𝑧𝑘, measured about 𝑥𝑘.
Constant or variable
These parameters are not all variable in every robot.
• For a revolute joint, 𝜃𝑘 is variable and 𝑑𝑘 is constant.
• For a prismatic joint, 𝑑𝑘 is variable and 𝜃𝑘 is constant.
********** 3 **********
--- page 4 ---
• The link parameters 𝑎𝑘 and 𝛼𝑘 are usually constant for a given robot
because they depend on the physical geometry of the links.
So, kinematic parameters are used to define the relative position and orientation of
adjacent links in a robot. Joint parameters change during motion, while link
parameters generally remain fixed for a given manipulator structure.
Q2   a. Explain the following terms with respect to industrial robots:   [10]
CO-1   i.   Define Robot.
An industrial robot is an automatically controlled, reprogrammable, multipurpose
manipulator programmed in three or more axes and used in industrial automation.
In simple words, it is a machine that performs tasks such as welding, pick-and-
place, assembly, painting, and material handling with minimal human intervention.
ii.   Continuous motion and point to point motion (With Diagrams)
Point-to-point (PTP) motion means the robot moves from one taught point to
another, and the path between the points is not important; only the start and end
positions matter. Continuous motion means the robot follows a defined path
smoothly, so both the path and the final position are important, as in welding,
cutting, or painting operations. PTP is usually faster for positioning tasks, while
continuous motion is used when the robot must maintain a specific trajectory.
iii.   Repeatability and Accuracy.
With Diagrams
Repeatability is the ability of a robot to return to the same taught position again
and again under the same conditions. Accuracy is the closeness of the robot’s
actual position to the commanded or desired position. A robot may have very good
repeatability but still not be highly accurate if all repeated positions are consistently
offset from the target.
iv.   Fixed and Mobile co-ordinate frames.
With Diagrams
A fixed coordinate frame is attached to a stationary reference, such as the robot
base, cell, or world frame, and does not move during operation. A mobile
coordinate frame is attached to a moving object such as the robot arm, end-effector,
or a carried workpiece, so its position and orientation change as the robot moves.
These frames are used to describe position and orientation clearly in robot
kinematics and motion analysis.
********** 4 **********
--- page 5 ---
CO-3; b Suppose, F = {f1, f2, f3} and M = {m1, m2, m3} are two initially coincident fixed   [10]
.   and mobile orthonormal coordinate frames, respectively. Suppose we perform the
following sequence of operations:
1. Rotate the M frame along the f 2 -axis by π/2 radians.
2. Rotate the frame M about the f 3 -axis by -π radians.
3. Translate the M frame along the f 1-axis by 7 units.
a. Calculate the Resultant Transformation Matrix
b. Find [q]F given [q]M = [2 1 2]T
c. Considering only the first two rotations calculate the resultant fundamental
rotation matrix also find [p]M given [p]F = [3 3 3]T
a) Resultant transformation matrix
For the first rotation about 𝑓2 by 𝜋/2,
0   0 1 0
𝑅𝑦(𝜋 = [ 0   1 0 0 ]
2)   −1 0 0 0
0   0 0 1   2
For the second rotation about 𝑓3 by −𝜋,
−1 0   0 0
0 −1 0 0
𝑅𝑧(−𝜋) = [   ]
0   0   1 0
0   0   0 1
Using the composite method for fixed-axis operations, the total rotation is
0   0 −1 0
𝑅= 𝑅𝑧(−𝜋) 𝑅𝑦(𝜋 = [ 0 −1 0   0 ]
2)   −1 0   0   0
0   0   0   1
The translation is along fixed 𝑓1 by 7 units, so
1 0 0 7
0 1 0 0
𝑝= [   ]
0 0 1 0
0 0 0 1   3
Hence the resultant HCTM is
0   0 −1 7
0 −1 0   0
𝑇= [   ]
−1 0   0   0
0   0   0   1
b)Find [𝒒]𝑭 given [𝒒]𝑴= 𝟐 𝟏 𝟐 𝟏]𝑻
Using [𝑞]𝐹= 𝑇[𝑞]𝑀,
2
********** 5 **********
--- page 6 ---
0   0 −1 7 2   5
[ 𝑞]𝐹= [ 0 −1   0 0 ] [ 1 ] = [ −1 ]
−1   0   0 0 2   −2
0   0   0 1 1   1
So,
[q]F = [5 −1 −2 ] T
c) Fundamental rotation matrix and [𝒑]𝑴   1
Considering only the first two rotations, the resultant fundamental rotation matrix
is
0   0 −1
𝑅= [ 0 −1 0 ]
−1 0   0
To find [𝑝]𝑀 given
3
[ 𝑝]𝐹= [ 3 ]
3
we use
[𝑝]𝐹= 𝑅[𝑝]𝑀⇒[𝑝]𝑀= 𝑅𝑇[𝑝]𝐹
2
Since 𝑅𝑇= 𝑅 here,
0   0 −1 3   −3
[ 𝑝]𝑀= [ 0 −1   0 ] [ 3 ] = [ −3 ]
−1   0   0 3   −3
Thus,
[p]M = [−3 −3 −3]T
Q3   a. Analyze the kinematic parameter table for a 4 axis robot as follows   [10]
CO-3;   Axis   𝜽𝒌   𝒅𝒌   𝒂𝒌   𝜶𝒌   Variable
1   𝜃1   𝑑1   0   −𝜋2 ⁄   𝜃1
2   𝜃2   0   𝑎2   −𝜋2 ⁄   𝜃2
3   𝜃3   0   𝑎3   0   𝜃3
4   𝜃4   𝑑4   0   −𝜋2 ⁄   𝜃4
Derive all the Individual Link co-ordinate transformation Matrices for all the
joints.
********** 6 **********
--- page 7 ---
Individual link matrices
2
1) Link 1
With 𝑎1 = 0 and 𝛼1 = −𝜋/2,
cos 𝜃1   0   −sin⁡ 𝜃1 0
sin 𝜃1   0   cos 𝜃1   0
𝐴1 = [   ]
0   −1   0   𝑑1
0   0   0   1   2
2) Link 2
With 𝑑2 = 0 and 𝛼2 = −𝜋/2,
cos 𝜃2   0   −sin⁡ 𝜃2 𝑎2cos⁡ 𝜃2
𝐴2 = [ sin 𝜃2   0   cos 𝜃2   𝑎2sin⁡ 𝜃2 ]
0   −1   0   0
0   0   0   1   2
3) Link 3
With 𝛼3 = 0 and 𝑑3 = 0,
cos 𝜃3 −sin⁡ 𝜃3 0 𝑎3cos⁡ 𝜃3
𝐴3 = [ sin 𝜃3   cos 𝜃3   0   𝑎3sin⁡ 𝜃3 ]
0   0   1   0
0   0   0   1   2
4) Link 4
With 𝑎4 = 0 and 𝛼4 = −𝜋/2,
cos 𝜃4   0   −sin⁡ 𝜃4 0
sin 𝜃4   0   cos 𝜃4   0
𝐴4 = [   ]   2
0   −1   0   𝑑4
0   0   0   1
CO-2; b   Discuss the role of derivative control in robotics, including its mathematical   [10]
.
representation, response characteristics, and limitations, also discuss two real life
examples where it can be used.
(With Diagrams)
Derivative control is a control action in which the control signal is proportional to
the rate of change of error, so it predicts the future trend of the system response
and acts in advance to reduce rapid changes. In robotics, it is mainly used to
improve stability, reduce overshoot, damp oscillations, and make the response
smoother in fast dynamic systems.
Mathematical representation
********** 7 **********
--- page 8 ---
Let the error be
𝑒(𝑡) = setpoint −output
Then the derivative control signal is given by
𝑑𝑒(𝑡)
𝑢(𝑡) = 𝐾𝑑
𝑑𝑡
where 𝑢(𝑡) is the control signal, 𝐾𝑑 is the derivative gain, and 𝑑𝑒(𝑡) is the rate of
𝑑𝑡
change of error with respect to time. This means the controller does not act on the
magnitude of error alone, but on how fast that error is changing.
Response characteristics
Derivative control has an anticipatory nature because it predicts system behaviour
from the slope of the error curve. If the error changes rapidly, it produces a strong
corrective action; if the error changes slowly, the derivative action is small; and if
the error is constant, derivative action becomes zero. Because of this, derivative
control reduces overshoot, damps oscillations, improves stability, and gives faster
settling time compared with proportional control alone.
Limitations
Derivative control is highly sensitive to noise because even small high-frequency
variations in the error signal can produce large changes in the derivative output. It
also does not remove steady-state error, since for constant error the derivative term
becomes zero and no correction is applied. Another limitation is that the derivative
gain must be tuned carefully; if 𝐾𝑑 is too high, the system may become noisy or
unstable, while if it is too low, sufficient damping is not obtained.
Real-life examples
One important application is in a self-balancing robot, where derivative control
predicts the rate of tilt and applies corrective action quickly so that the robot does
not tip over or oscillate excessively. Another application is drone altitude control,
where derivative control smooths altitude changes and reduces oscillations when
the drone rises or falls rapidly.
Thus, derivative control plays an important role in robotics by providing predictive
action based on the rate of change of error. Although it cannot eliminate steady-
state error and is sensitive to noise, it is very useful for reducing overshoot,
improving damping, and achieving faster and smoother response in robotic
systems.
Q4   a. Describe the Bounded Deviation Algorithm, including its working principles,   [10]
CO-4;   advantages, and limitations.
The Bounded Deviation Algorithm is a control strategy used to maintain
a system’s output within a specified range or deviation from a desired value, or
setpoint. This method ensures that a system operates within an acceptable
tolerance, even in the presence of disturbances, noise, or uncertainties in the system
dynamics.
********** 8 **********
--- page 9 ---
This algorithm is especially useful in applications where small deviations
from the setpoint are acceptable, but large deviations could lead to system
instability, poor performance, or potential damage. The key idea behind this
algorithm is to define bounds around the setpoint and use these bounds to guide the
control actions.
Concept of Bounded Deviation
In control systems, the output often does not match the desired setpoint
exactly due to system limitations or external disturbances. However, it is
acceptable if the deviation from the setpoint remains within certain bounds. These
bounds represent a tolerance range within which the system's performance is
considered acceptable. The bounded deviation algorithm aims to keep the
system’s deviation within these defined bounds.
Mathematically, the deviation e(t) is defined as:
e(t) = Setpoint – Actual Output
In the bounded deviation approach, we aim to maintain e(t) such that:
−Δ ≤ e(t) ≤ +Δ
where Δ is the allowable bound (tolerance) for the deviation.
Working of the Bounded Deviation Algorithm
The bounded deviation algorithm consists of the following key steps:
1. Set Tolerance Bounds: The algorithm begins by defining upper and lower
bounds around the setpoint. These bounds represent the acceptable range
within which the system output can deviate.
2. Monitor System Output: The system’s output is continuously monitored
and compared to the setpoint. The deviation e(t) is calculated as the
difference between the setpoint and the actual output.
3. Check Deviation Against Bounds: The deviation e(t) is checked to see
whether it falls within the pre-set bounds:
********** 9 **********
--- page 10 ---
o   If e(t) is within the bounds (i.e., −Δ ≤ e(t) ≤ +Δ), no corrective action
is required, as the system is operating within acceptable limits.
o   If e(t) exceeds the bounds (i.e., e(t) > +Δ or e(t) <−Δ), corrective
control action is triggered to bring the system back within the
allowable bounds.
4. Apply Corrective Action: If the deviation exceeds the bounds, the
controller adjusts the control input to minimize the error and bring the
system back within the allowable deviation. This control action could
involve adjusting gains or activating feedback mechanisms like in a PID
controller.
5. Repeat Continuously: The algorithm continuously repeats this process to
ensure the system stays within the desired bounds despite disturbances or
changes in the system.
Advantages of Bounded Deviation Algorithm
1. Robustness to Disturbances: The algorithm helps systems maintain
performance despite external disturbances, keeping deviations within the
acceptable range.
2. Simplicity: The bounded deviation algorithm is relatively simple to
implement as it only requires monitoring deviations against predefined
bounds.
3. Improved Stability: By limiting large deviations, the algorithm prevents
the system from becoming unstable or oscillatory.
4. Reduced Control Effort: Since control actions are only applied when
deviations exceed the bounds, the control effort is minimized, leading to
energy efficiency in some systems.
Limitations of Bounded Deviation Algorithm
1. Limited Precision: If high precision is required, bounded deviation may
not be suitable, as small deviations within the bounds are allowed without
correction.
2. Dependence on Bound Setting: The performance of the algorithm heavily
depends on how the bounds are set. If bounds are too tight, it may result in
frequent corrections, leading to instability. If the bounds are too wide, the
system may operate far from the setpoint.
********** 10 **********
--- page 11 ---
3. Delay in Response: The system only corrects deviations when they exceed
the bounds, which may introduce a delay in responding to small changes in
the system.
CO-2; b   Explain open-loop control using the example of a washing machine timer or a   [10]
.   conveyor belt. Draw and describe the block diagram, identifying the roles of input,
controller, plant, and why there is no feedback path.
An open-loop control system is one in which the output has no effect on the
control action. In other words, the system operates without using feedback. The
controller sends a signal to the process, but it has no way of verifying if the output
achieved matches the desired result.
Example: A washing machine is a common example of an open-loop control
system. Once the program is set, the machine will run through its cycle without any
knowledge of how clean the clothes are. The operation is based solely on pre-set
conditions.
Characteristics of Open-Loop Control Systems:
1. No feedback mechanism: The system cannot adjust based on the actual
output.
2. Simpler design: Since there is no feedback, the design is straightforward
and less expensive.
3. Less accurate: Without feedback, the system cannot correct errors.
4. Predefined control actions: The controller acts according to a predetermined
set of inputs, regardless of the output.
5. Stable: Open-loop systems are inherently stable as they do not react to
changing outputs.
Block Diagram of an Open-Loop Control System
The typical block diagram of an open-loop control system consists of three
components:
1. Input: The command or desired setpoint given to the system.
2. Controller: The component that processes the input and sends a command
signal to the process.
3. Process (or Plant): The part of the system that performs the operation or
action.
4. Output: The result or the outcome of the system.
Open-Loop Control System Block Diagram:
In this diagram, notice that there is no feedback path from the output to the
input, meaning the system cannot self-correct.
********** 11 **********
--- page 12 ---
Mathematical Representation of Open-Loop Systems
The behaviour of an open-loop control system can be mathematically
modelled using transfer functions. The system's input-output relationship is usually
linear.
For an open-loop system:
Y(s) = G(s) ⋅ X(s)
Where:
• Y(s) is the Laplace transform of the output.
• X(s) is the Laplace transform of the input.
• G(s) is the transfer function of the system (representing the relationship
between the input and output).
Examples of Open-Loop Control Systems
1. Toaster
In a toaster, the heating element stays on for a predefined time set by the
user, regardless of the actual colour or condition of the bread.
Block Diagram:
Since there is no feedback mechanism to check whether the bread is
properly toasted, this is an open-loop system.
2. Electric Kettle
An electric kettle without an automatic shut-off is another example of an
open-loop system. It heats water based on the time set, without measuring the actual
water temperature.
Block Diagram:
There is no feedback to indicate whether the water has reached the desired
temperature.
Advantages and Disadvantages of Open-Loop Control Systems
Advantages:
1. Simplicity: Open-loop systems are easier to design and implement because
they do not require feedback or sensors to monitor the output.
2. Cost-Effective: These systems are generally cheaper because they do not
require the components needed for feedback and error correction.
3. No Stability Issues: Open-loop systems are inherently stable, as there are
no feedback loops that could cause oscillations or instability.
Disadvantages:
1. Lack of Accuracy: Open-loop systems cannot correct any errors between
the desired and actual output. This can lead to imprecise results.
********** 12 **********
--- page 13 ---
2. Disturbance Sensitivity: Since the system cannot detect disturbances or
changes in the output, any variations in the process or environment can
degrade performance.
3. No Adaptability: Open-loop systems cannot adapt to changing conditions
or correct deviations from the desired output.
Output Behaviour of an Open-Loop System
The response of an open-loop control system can be observed using a step
input (a sudden change in the input signal). The output waveform is typically
delayed and may not follow the input closely due to the lack of feedback.
Example: Step Input Response
Consider an open-loop system where a step input is applied, such as
switching on a heating element. The system will follow a predictable path based
on the pre-set parameters but cannot adjust based on the output.
Step Input Response Waveform:
In this case, the system achieves the desired output (a rise in temperature)
but without any ability to detect or correct deviations.
Q5   a. Suppose, F = {f1, f2, f3} and M = {m1, m2, m3} are two initially coincident   [10]
CO-2;   fixed and mobile orthonormal coordinate frames, respectively. Suppose we
perform the following sequence of operations:
1. Rotate the frame M about the f 3 -axis by −𝜋⁡radians.
2. Rotate the frame M about the f 2 -axis by 𝜋/2⁡radians.
3. Rotate the frame M about the f 1 -axis by 𝜋⁡radians.
a. Calculate the resultant rotation matrix after composite rotations.
b. Solve for [m1]F [m2]F and [m3]F.
The standard fundamental rotation matrices about the fixed axes are
1   0   0
𝑅1(𝜃) = [ 0 cos 𝜃 −sin⁡ 𝜃 ]
0   sin 𝜃   cos 𝜃
********** 13 **********
--- page 14 ---
cos 𝜃 −sin⁡ 𝜃 0
𝑅3(𝜃) = [ sin 𝜃   cos 𝜃   0 ]
0   0   1
Substituting the given angles:
−1   0 0
𝑅3(−𝜋) = [ 0 −1 0 ]
0   0 1
0 0 1
𝑅2 (𝜋 2) = [ 0 1 0 ]
−1 0 0
1 0   0
𝑅1(𝜋) = [ 0 −1 0 ]
0 0 −1
a) Resultant rotation matrix
First multiply the first two rotations:
0 0 1
𝑅2 (𝜋 2) 𝑅3(−𝜋) = [ 0 −1 0 ]
1 0 0
Now multiply by 𝑅1(𝜋):
0 0 1
𝑅= 𝑅1(𝜋) 𝑅2 (𝜋 2) 𝑅3(−𝜋) = [ 0 1 0 ]
−1 0 0
So, the resultant composite rotation matrix is
0 0 1
𝑅= [ 0 1 0 ]
−1 0 0
b) Find [𝑚1]𝐹, [𝑚2]𝐹, and [𝑚3]𝐹
In a rotation matrix, the columns represent the mobile frame axes expressed in the
fixed frame. Thereforescribd+1
0   0   1
[𝑚1]𝐹= [ 0 ] , [𝑚2]𝐹= [ 1 ] , [𝑚3]𝐹= [ 0 ]
−1   0   0
CO-4; b   Explain in detail with schematic how robotic part inspection using a vision system   [10]
.   is carried out in a robotic work cell.
A vision system in a robotic work cell is used for automated part inspection to
ensure quality, precision, and efficiency. The process involves image acquisition,
processing, decision-making, and robotic actions. Below are the detailed steps
involved:
********** 14 **********
--- page 15 ---
Step 1: Image Acquisition
•   The vision system captures images of the part using cameras (2D or 3D),
laser scanners, or infrared sensors.
•   Proper lighting techniques (LED, infrared, structured light) are used to
enhance contrast and eliminate shadows.
•   The camera may be fixed (mounted on a stand) or robot-mounted (attached
to the robotic arm).
Example: A high-resolution camera captures a circuit board for missing
components.
Step 2: Image Preprocessing
•   The raw image is processed to remove noise and enhance features for better
inspection.
•   Common preprocessing techniques include:
o   Grayscale conversion: Simplifies image by removing color variations.
o   Contrast adjustment: Improves defect visibility.
o   Edge detection: Identifies object boundaries using Sobel or Canny edge
detection.
Thresholding: Converts images into black & white for easier defect identification.
Example: The system enhances scratches on a metal surface by adjusting contrast
and applying edge detection.
Step 3: Feature Extraction
•   The system identifies key characteristics of the part, such as:
o   Shape (circular, rectangular, irregular).
o   Size (measuring dimensions).
o   Texture (surface roughness or patterns).
o   Color (RGB analysis).
Example: A robotic vision system measures the diameter of a gear to ensure it
meets specifications.
Step 4: Object Identification & Classification
•   The system compares extracted features with predefined models using:
o   Template Matching: Compares images with reference parts.
o   Machine Learning-Based Classification: Uses trained AI models for defect
detection.
o   Optical Character Recognition (OCR): Reads serial numbers or barcodes.
********** 15 **********
--- page 16 ---
Example: A robotic arm sorts screws by thread type and length using a vision
system.
Step 5: Defect Detection & Quality Control
•   The system checks for common defects, including:
o   Cracks, dents, or scratches on metal parts.
o   Missing components in PCB assembly.
o   Incorrect part dimensions in manufactured products.
•   If a defect is found, the system flags the part for rejection or rework.
Example: A robotic vision system detects a missing resistor on a PCB board and
sends it for rework.
Step 6: Decision-Making & Robotic Action
•   The robot decides the next step based on inspection results:
o   Pass: The part is accepted and moved to the next stage.
o   Fail: The part is rejected and sent for rework or disposal.
o   Reorientation: If the part is misaligned, the robot adjusts its position.
•   The robot uses pick-and-place techniques to sort parts accordingly.
Example: A robotic arm removes faulty glass panels from a production line and
places them in a rejection bin.
Step 7: Data Logging & Feedback for Process Improvement
•   Inspection data is recorded for analysis to improve the manufacturing
process.
•   Machine Learning (ML) models analyze defect trends and help predict
future failures.
•   The system adjusts parameters in real-time for continuous improvement.
Example: A vision system logs defect rates in semiconductor chip production and
suggests tuning machine parameters.
Q6   a. Analyze a 3 Axis Cylindrical Robotic Arm and compute the following.   [20]
CO-3;
i.   Link coordinate diagram
********** 16 **********
--- page 17 ---
7
ii.   Link coordinate table.
5
iii. ARM Matrix.
2
2
2
ARM Matrix
2
Q7   a. Analyze the kinematic parameter table for a two axis RP Robotic arm as follows   [20]
CO-4;   Axis   𝜽𝒌   𝒅𝒌   𝒂𝒌   𝜶𝒌   Variable
1   𝜃1   0   0   −𝜋2 ⁄   𝜃1
2   0   𝑑2   0   0   𝑑2
********** 17 **********
--- page 18 ---
i.   Derive the ARM Matrix.
ii.   For Theta = 60o and d2 = 120 mm find the transformation matrix.
iii.   Derive TCV from the arm matrix and corresponding equations.
iv.   Derive joint equations for all the joints.
The individual link transformation matrices are:
cos 𝜃1   0   −sin⁡ 𝜃1 0
𝐴1 = [ sin 𝜃1   0   cos 𝜃1   0 ]   2
0   −1   0   0
0   0   0   1
1 0 0 0
0 1 0 0
𝐴2 = [   ]
0 0 1 𝑑2
0 0 0 1   2
Hence, the ARM matrix is
cos 𝜃1   0   −sin⁡ 𝜃1 −𝑑2sin⁡ 𝜃1
𝑇= 𝐴1𝐴2 = [ sin 𝜃1   0   cos 𝜃1   𝑑2cos⁡ 𝜃1 ]
0   −1   0   0
0   0   0   1
ii) Transformation matrix for 𝜃1 = 60∘ and 𝑑2 = 120 mm   2
Substituting cos⁡ 60∘= 1 and sin⁡ 60∘= √3 in the ARM matrix:
2   2
1   −√3   √3
0   −120
2   2   2
𝑇= √3   1   1
0   120
2   2   2
0 −1   0   0
[ 0   0   0   1   ]
Therefore,   2
0.5   0   −0.866 −103.92
0.866 0   0.5   60
𝑇= [   ]
0   −1   0   0
0   0   0   1
iii) TCV from the arm matrix and corresponding equations
From the arm matrix, the tool configuration vector is obtained by combining tool
position and orientation terms in compact form as done in the attached inverse
kinematics material. From the above matrix,
𝑥= −𝑑2sin⁡ 𝜃1, 𝑦= 𝑑2cos⁡ 𝜃1, 𝑧= 0
Also, from the rotation part,   3
cos 𝜃1   0   −sin⁡ 𝜃1
𝑛= [ sin 𝜃1 ] , 𝑠= [ 0 ] , 𝑎= [ cos 𝜃1 ]
0   −1   0
Hence the corresponding equations are:
𝑥= −𝑑2sin⁡ 𝜃1   2
********** 18 **********
--- page 19 ---
𝑦= 𝑑2cos⁡ 𝜃1
𝑧= 0
These are the required position equations for the RP robot.
iv) Joint equations for all joints
From
𝑥= −𝑑2sin⁡ 𝜃1, 𝑦= 𝑑2cos⁡ 𝜃1   3
squaring and adding,
𝑥2 + 𝑦2 = 𝑑2 2
Therefore, the prismatic joint equation is
𝑑2 = √𝑥2 + 𝑦2
Now dividing the two equations,
𝑥   −𝑑2sin⁡ 𝜃1
𝑦=   = −tan⁡ 𝜃1
𝑑2cos⁡ 𝜃1
Hence the revolute joint equation is   4
𝜃1 = tan⁡−1 (−𝑥 𝑦)
Thus, the joint equations are
𝑑2 = √𝑥2 + 𝑦2
𝜃1 = tan⁡−1 (−𝑥 𝑦)
These are the required joint-variable equations for the given two-axis RP robot.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 90daf488396f

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_AI_7051/Robotics/ANS_Robotics(702AI0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Robotics
Date: 06 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 1   a. Explain different types of operating environment for the robot in industry with   [05]
necessary precautions to be taken.
Environment-wise precautions
Normal production floor: Use fences, interlocks, emergency stop buttons, warning
signs, and defined safety zones to keep workers outside the robot work envelope.
Dusty or dirty environment: Choose robots designed for dirty conditions, protect
sliding parts and cables, and carry out regular cleaning and inspection to prevent
wear or malfunction.
Hot environment, welding, foundry: Use heat-resistant components, shielding, and
protective routing for cables and sensors; also protect workers from thermal
hazards and sparks.
Wet, chemical, food, or clean-room area: Select robots with sealed construction
suited to washdown, contamination control, or chemical exposure, and maintain
strict hygiene or contamination procedures as required.
Hazardous or explosive area: Use specially rated equipment, eliminate ignition
sources, and follow strict area safety procedures because flammable surroundings
increase risk.
Human-robot shared workspace: Use light curtains, safety mats, floor sensors,
presence detection, speed limiting, and safe stop features to reduce collision risk.
General precautions
********** 1 **********
--- page 2 ---
Necessary precautions for all robot environments include a proper risk assessment
before installation, selecting the robot to match the task and surroundings, training
workers in hazards and emergency procedures, and applying lockout/tagout during
maintenance. Regular inspection of guards, sensors, electrical systems, and
emergency stops is also essential because electrical faults, unexpected motion, and
unauthorized entry are common industrial robot hazards.
CO- 2 b Compare proportional and integral control systems on various parameters.   [05]
.
Parameter   Proportional (P) control   Integral (I) control
Control   Depends on present error   Depends on accumulated error
action   magnitude   over time
Response   Slower because output builds
Fast and immediate
speed   gradually
Steady-   Usually cannot eliminate   Eliminates steady-state error or
state error   offset completely   offset
Initial
Strong for sudden error   Weak initially; increases with
corrective
change   time if error persists
effort
Generally better than I-only,   More likely to increase
Stability   but too high gain can cause   oscillation and instability if too
oscillation   strong
Overshoot   Can increase overshoot when   Often increases overshoot
tendency   gain is high   because of accumulated action
Moderate, due to residual   Higher steady-state accuracy
Accuracy
offset   because offset is removed
Harder to tune because
Tuning
Comparatively easier to tune   excessive integral action can
difficulty
destabilize the system
Used when quick response is
Used when very small or zero
Suitability   more important than zero
steady-state error is required
offset
Main   Slow response, oscillation risk,
Residual error remains
drawback   and windup problem
CO- 4   c. For a fixed frame F and mobile frame M initially coincident, suppose we perform   [05]
following operations:
********** 2 **********
--- page 3 ---
(i) Rotate M along f 2 axis by -π/2 radians,
(ii) Translate M along f 1 axis by 12 units.
Derive the resultant transformation matrix. Draw vector diagrams.
0 0 −1 0
1. Rotation about fixed 𝑓2 axis by −𝜋/2: 𝑅𝑦(−𝜋/2) = [ 0 1 0   0 ]   2
1 0 0   0
0 0 0   1
1 0 0 12
2. Translation along fixed 𝑓1 axis by 12 units: 𝑝= [ 0 1 0 0 ]
0 0 1 0
0 0 0 1
3. Resultant transformation matrix:   2
0 0 −1 12
0 1 0   0
[   ]
1 0 0   0
0 0 0   1
1
CO- 3 d   Explain kinematic parameters with help of neat diagram, also comment on when   [05]
.   they will be constant or variable.
(With Diagrams)
Meaning of the parameters
• 𝜃𝑘 joint angle: rotation about the previous joint axis 𝑧𝑘−1.
• 𝑑𝑘 joint displacement: translation along the previous joint axis 𝑧𝑘−1.
• 𝑎𝑘 link length: distance between successive joint axes measured along 𝑥𝑘.
• 𝛼𝑘 link twist: angle between 𝑧𝑘−1 and 𝑧𝑘, measured about 𝑥𝑘.
Constant or variable
These parameters are not all variable in every robot.
• For a revolute joint, 𝜃𝑘 is variable and 𝑑𝑘 is constant.
• For a prismatic joint, 𝑑𝑘 is variable and 𝜃𝑘 is constant.
********** 3 **********
--- page 4 ---
• The link parameters 𝑎𝑘 and 𝛼𝑘 are usually constant for a given robot
because they depend on the physical geometry of the links.
So, kinematic parameters are used to define the relative position and orientation of
adjacent links in a robot. Joint parameters change during motion, while link
parameters generally remain fixed for a given manipulator structure.
Q2   a. Explain the following terms with respect to industrial robots:   [10]
CO-1   i.   Define Robot.
An industrial robot is an automatically controlled, reprogrammable, multipurpose
manipulator programmed in three or more axes and used in industrial automation.
In simple words, it is a machine that performs tasks such as welding, pick-and-
place, assembly, painting, and material handling with minimal human intervention.
ii.   Continuous motion and point to point motion (With Diagrams)
Point-to-point (PTP) motion means the robot moves from one taught point to
another, and the path between the points is not important; only the start and end
positions matter. Continuous motion means the robot follows a defined path
smoothly, so both the path and the final position are important, as in welding,
cutting, or painting operations. PTP is usually faster for positioning tasks, while
continuous motion is used when the robot must maintain a specific trajectory.
iii.   Repeatability and Accuracy.
With Diagrams
Repeatability is the ability of a robot to return to the same taught position again
and again under the same conditions. Accuracy is the closeness of the robot’s
actual position to the commanded or desired position. A robot may have very good
repeatability but still not be highly accurate if all repeated positions are consistently
offset from the target.
iv.   Fixed and Mobile co-ordinate frames.
With Diagrams
A fixed coordinate frame is attached to a stationary reference, such as the robot
base, cell, or world frame, and does not move during operation. A mobile
coordinate frame is attached to a moving object such as the robot arm, end-effector,
or a carried workpiece, so its position and orientation change as the robot moves.
These frames are used to describe position and orientation clearly in robot
kinematics and motion analysis.
********** 4 **********
--- page 5 ---
CO-3; b Suppose, F = {f1, f2, f3} and M = {m1, m2, m3} are two initially coincident fixed   [10]
.   and mobile orthonormal coordinate frames, respectively. Suppose we perform the
following sequence of operations:
1. Rotate the M frame along the f 2 -axis by π/2 radians.
2. Rotate the frame M about the f 3 -axis by -π radians.
3. Translate the M frame along the f 1-axis by 7 units.
a. Calculate the Resultant Transformation Matrix
b. Find [q]F given [q]M = [2 1 2]T
c. Considering only the first two rotations calculate the resultant fundamental
rotation matrix also find [p]M given [p]F = [3 3 3]T
a) Resultant transformation matrix
For the first rotation about 𝑓2 by 𝜋/2,
0   0 1 0
𝑅𝑦(𝜋 = [ 0   1 0 0 ]
2)   −1 0 0 0
0   0 0 1   2
For the second rotation about 𝑓3 by −𝜋,
−1 0   0 0
0 −1 0 0
𝑅𝑧(−𝜋) = [   ]
0   0   1 0
0   0   0 1
Using the composite method for fixed-axis operations, the total rotation is
0   0 −1 0
𝑅= 𝑅𝑧(−𝜋) 𝑅𝑦(𝜋 = [ 0 −1 0   0 ]
2)   −1 0   0   0
0   0   0   1
The translation is along fixed 𝑓1 by 7 units, so
1 0 0 7
0 1 0 0
𝑝= [   ]
0 0 1 0
0 0 0 1   3
Hence the resultant HCTM is
0   0 −1 7
0 −1 0   0
𝑇= [   ]
−1 0   0   0
0   0   0   1
b)Find [𝒒]𝑭 given [𝒒]𝑴= 𝟐 𝟏 𝟐 𝟏]𝑻
Using [𝑞]𝐹= 𝑇[𝑞]𝑀,
2
********** 5 **********
--- page 6 ---
0   0 −1 7 2   5
[ 𝑞]𝐹= [ 0 −1   0 0 ] [ 1 ] = [ −1 ]
−1   0   0 0 2   −2
0   0   0 1 1   1
So,
[q]F = [5 −1 −2 ] T
c) Fundamental rotation matrix and [𝒑]𝑴   1
Considering only the first two rotations, the resultant fundamental rotation matrix
is
0   0 −1
𝑅= [ 0 −1 0 ]
−1 0   0
To find [𝑝]𝑀 given
3
[ 𝑝]𝐹= [ 3 ]
3
we use
[𝑝]𝐹= 𝑅[𝑝]𝑀⇒[𝑝]𝑀= 𝑅𝑇[𝑝]𝐹
2
Since 𝑅𝑇= 𝑅 here,
0   0 −1 3   −3
[ 𝑝]𝑀= [ 0 −1   0 ] [ 3 ] = [ −3 ]
−1   0   0 3   −3
Thus,
[p]M = [−3 −3 −3]T
Q3   a. Analyze the kinematic parameter table for a 4 axis robot as follows   [10]
CO-3;   Axis   𝜽𝒌   𝒅𝒌   𝒂𝒌   𝜶𝒌   Variable
1   𝜃1   𝑑1   0   −𝜋2 ⁄   𝜃1
2   𝜃2   0   𝑎2   −𝜋2 ⁄   𝜃2
3   𝜃3   0   𝑎3   0   𝜃3
4   𝜃4   𝑑4   0   −𝜋2 ⁄   𝜃4
Derive all the Individual Link co-ordinate transformation Matrices for all the
joints.
********** 6 **********
--- page 7 ---
Individual link matrices
2
1) Link 1
With 𝑎1 = 0 and 𝛼1 = −𝜋/2,
cos 𝜃1   0   −sin⁡ 𝜃1 0
sin 𝜃1   0   cos 𝜃1   0
𝐴1 = [   ]
0   −1   0   𝑑1
0   0   0   1   2
2) Link 2
With 𝑑2 = 0 and 𝛼2 = −𝜋/2,
cos 𝜃2   0   −sin⁡ 𝜃2 𝑎2cos⁡ 𝜃2
𝐴2 = [ sin 𝜃2   0   cos 𝜃2   𝑎2sin⁡ 𝜃2 ]
0   −1   0   0
0   0   0   1   2
3) Link 3
With 𝛼3 = 0 and 𝑑3 = 0,
cos 𝜃3 −sin⁡ 𝜃3 0 𝑎3cos⁡ 𝜃3
𝐴3 = [ sin 𝜃3   cos 𝜃3   0   𝑎3sin⁡ 𝜃3 ]
0   0   1   0
0   0   0   1   2
4) Link 4
With 𝑎4 = 0 and 𝛼4 = −𝜋/2,
cos 𝜃4   0   −sin⁡ 𝜃4 0
sin 𝜃4   0   cos 𝜃4   0
𝐴4 = [   ]   2
0   −1   0   𝑑4
0   0   0   1
CO-2; b   Discuss the role of derivative control in robotics, including its mathematical   [10]
.
representation, response characteristics, and limitations, also discuss two real life
examples where it can be used.
(With Diagrams)
Derivative control is a control action in which the control signal is proportional to
the rate of change of error, so it predicts the future trend of the system response
and acts in advance to reduce rapid changes. In robotics, it is mainly used to
improve stability, reduce overshoot, damp oscillations, and make the response
smoother in fast dynamic systems.
Mathematical representation
********** 7 **********
--- page 8 ---
Let the error be
𝑒(𝑡) = setpoint −output
Then the derivative control signal is given by
𝑑𝑒(𝑡)
𝑢(𝑡) = 𝐾𝑑
𝑑𝑡
where 𝑢(𝑡) is the control signal, 𝐾𝑑 is the derivative gain, and 𝑑𝑒(𝑡) is the rate of
𝑑𝑡
change of error with respect to time. This means the controller does not act on the
magnitude of error alone, but on how fast that error is changing.
Response characteristics
Derivative control has an anticipatory nature because it predicts system behaviour
from the slope of the error curve. If the error changes rapidly, it produces a strong
corrective action; if the error changes slowly, the derivative action is small; and if
the error is constant, derivative action becomes zero. Because of this, derivative
control reduces overshoot, damps oscillations, improves stability, and gives faster
settling time compared with proportional control alone.
Limitations
Derivative control is highly sensitive to noise because even small high-frequency
variations in the error signal can produce large changes in the derivative output. It
also does not remove steady-state error, since for constant error the derivative term
becomes zero and no correction is applied. Another limitation is that the derivative
gain must be tuned carefully; if 𝐾𝑑 is too high, the system may become noisy or
unstable, while if it is too low, sufficient damping is not obtained.
Real-life examples
One important application is in a self-balancing robot, where derivative control
predicts the rate of tilt and applies corrective action quickly so that the robot does
not tip over or oscillate excessively. Another application is drone altitude control,
where derivative control smooths altitude changes and reduces oscillations when
the drone rises or falls rapidly.
Thus, derivative control plays an important role in robotics by providing predictive
action based on the rate of change of error. Although it cannot eliminate steady-
state error and is sensitive to noise, it is very useful for reducing overshoot,
improving damping, and achieving faster and smoother response in robotic
systems.
Q4   a. Describe the Bounded Deviation Algorithm, including its working principles,   [10]
CO-4;   advantages, and limitations.
The Bounded Deviation Algorithm is a control strategy used to maintain
a system’s output within a specified range or deviation from a desired value, or
setpoint. This method ensures that a system operates within an acceptable
tolerance, even in the presence of disturbances, noise, or uncertainties in the system
dynamics.
********** 8 **********
--- page 9 ---
This algorithm is especially useful in applications where small deviations
from the setpoint are acceptable, but large deviations could lead to system
instability, poor performance, or potential damage. The key idea behind this
algorithm is to define bounds around the setpoint and use these bounds to guide the
control actions.
Concept of Bounded Deviation
In control systems, the output often does not match the desired setpoint
exactly due to system limitations or external disturbances. However, it is
acceptable if the deviation from the setpoint remains within certain bounds. These
bounds represent a tolerance range within which the system's performance is
considered acceptable. The bounded deviation algorithm aims to keep the
system’s deviation within these defined bounds.
Mathematically, the deviation e(t) is defined as:
e(t) = Setpoint – Actual Output
In the bounded deviation approach, we aim to maintain e(t) such that:
−Δ ≤ e(t) ≤ +Δ
where Δ is the allowable bound (tolerance) for the deviation.
Working of the Bounded Deviation Algorithm
The bounded deviation algorithm consists of the following key steps:
1. Set Tolerance Bounds: The algorithm begins by defining upper and lower
bounds around the setpoint. These bounds represent the acceptable range
within which the system output can deviate.
2. Monitor System Output: The system’s output is continuously monitored
and compared to the setpoint. The deviation e(t) is calculated as the
difference between the setpoint and the actual output.
3. Check Deviation Against Bounds: The deviation e(t) is checked to see
whether it falls within the pre-set bounds:
********** 9 **********
--- page 10 ---
o   If e(t) is within the bounds (i.e., −Δ ≤ e(t) ≤ +Δ), no corrective action
is required, as the system is operating within acceptable limits.
o   If e(t) exceeds the bounds (i.e., e(t) > +Δ or e(t) <−Δ), corrective
control action is triggered to bring the system back within the
allowable bounds.
4. Apply Corrective Action: If the deviation exceeds the bounds, the
controller adjusts the control input to minimize the error and bring the
system back within the allowable deviation. This control action could
involve adjusting gains or activating feedback mechanisms like in a PID
controller.
5. Repeat Continuously: The algorithm continuously repeats this process to
ensure the system stays within the desired bounds despite disturbances or
changes in the system.
Advantages of Bounded Deviation Algorithm
1. Robustness to Disturbances: The algorithm helps systems maintain
performance despite external disturbances, keeping deviations within the
acceptable range.
2. Simplicity: The bounded deviation algorithm is relatively simple to
implement as it only requires monitoring deviations against predefined
bounds.
3. Improved Stability: By limiting large deviations, the algorithm prevents
the system from becoming unstable or oscillatory.
4. Reduced Control Effort: Since control actions are only applied when
deviations exceed the bounds, the control effort is minimized, leading to
energy efficiency in some systems.
Limitations of Bounded Deviation Algorithm
1. Limited Precision: If high precision is required, bounded deviation may
not be suitable, as small deviations within the bounds are allowed without
correction.
2. Dependence on Bound Setting: The performance of the algorithm heavily
depends on how the bounds are set. If bounds are too tight, it may result in
frequent corrections, leading to instability. If the bounds are too wide, the
system may operate far from the setpoint.
********** 10 **********
--- page 11 ---
3. Delay in Response: The system only corrects deviations when they exceed
the bounds, which may introduce a delay in responding to small changes in
the system.
CO-2; b   Explain open-loop control using the example of a washing machine timer or a   [10]
.   conveyor belt. Draw and describe the block diagram, identifying the roles of input,
controller, plant, and why there is no feedback path.
An open-loop control system is one in which the output has no effect on the
control action. In other words, the system operates without using feedback. The
controller sends a signal to the process, but it has no way of verifying if the output
achieved matches the desired result.
Example: A washing machine is a common example of an open-loop control
system. Once the program is set, the machine will run through its cycle without any
knowledge of how clean the clothes are. The operation is based solely on pre-set
conditions.
Characteristics of Open-Loop Control Systems:
1. No feedback mechanism: The system cannot adjust based on the actual
output.
2. Simpler design: Since there is no feedback, the design is straightforward
and less expensive.
3. Less accurate: Without feedback, the system cannot correct errors.
4. Predefined control actions: The controller acts according to a predetermined
set of inputs, regardless of the output.
5. Stable: Open-loop systems are inherently stable as they do not react to
changing outputs.
Block Diagram of an Open-Loop Control System
The typical block diagram of an open-loop control system consists of three
components:
1. Input: The command or desired setpoint given to the system.
2. Controller: The component that processes the input and sends a command
signal to the process.
3. Process (or Plant): The part of the system that performs the operation or
action.
4. Output: The result or the outcome of the system.
Open-Loop Control System Block Diagram:
In this diagram, notice that there is no feedback path from the output to the
input, meaning the system cannot self-correct.
********** 11 **********
--- page 12 ---
Mathematical Representation of Open-Loop Systems
The behaviour of an open-loop control system can be mathematically
modelled using transfer functions. The system's input-output relationship is usually
linear.
For an open-loop system:
Y(s) = G(s) ⋅ X(s)
Where:
• Y(s) is the Laplace transform of the output.
• X(s) is the Laplace transform of the input.
• G(s) is the transfer function of the system (representing the relationship
between the input and output).
Examples of Open-Loop Control Systems
1. Toaster
In a toaster, the heating element stays on for a predefined time set by the
user, regardless of the actual colour or condition of the bread.
Block Diagram:
Since there is no feedback mechanism to check whether the bread is
properly toasted, this is an open-loop system.
2. Electric Kettle
An electric kettle without an automatic shut-off is another example of an
open-loop system. It heats water based on the time set, without measuring the actual
water temperature.
Block Diagram:
There is no feedback to indicate whether the water has reached the desired
temperature.
Advantages and Disadvantages of Open-Loop Control Systems
Advantages:
1. Simplicity: Open-loop systems are easier to design and implement because
they do not require feedback or sensors to monitor the output.
2. Cost-Effective: These systems are generally cheaper because they do not
require the components needed for feedback and error correction.
3. No Stability Issues: Open-loop systems are inherently stable, as there are
no feedback loops that could cause oscillations or instability.
Disadvantages:
1. Lack of Accuracy: Open-loop systems cannot correct any errors between
the desired and actual output. This can lead to imprecise results.
********** 12 **********
--- page 13 ---
2. Disturbance Sensitivity: Since the system cannot detect disturbances or
changes in the output, any variations in the process or environment can
degrade performance.
3. No Adaptability: Open-loop systems cannot adapt to changing conditions
or correct deviations from the desired output.
Output Behaviour of an Open-Loop System
The response of an open-loop control system can be observed using a step
input (a sudden change in the input signal). The output waveform is typically
delayed and may not follow the input closely due to the lack of feedback.
Example: Step Input Response
Consider an open-loop system where a step input is applied, such as
switching on a heating element. The system will follow a predictable path based
on the pre-set parameters but cannot adjust based on the output.
Step Input Response Waveform:
In this case, the system achieves the desired output (a rise in temperature)
but without any ability to detect or correct deviations.
Q5   a. Suppose, F = {f1, f2, f3} and M = {m1, m2, m3} are two initially coincident   [10]
CO-2;   fixed and mobile orthonormal coordinate frames, respectively. Suppose we
perform the following sequence of operations:
1. Rotate the frame M about the f 3 -axis by −𝜋⁡radians.
2. Rotate the frame M about the f 2 -axis by 𝜋/2⁡radians.
3. Rotate the frame M about the f 1 -axis by 𝜋⁡radians.
a. Calculate the resultant rotation matrix after composite rotations.
b. Solve for [m1]F [m2]F and [m3]F.
The standard fundamental rotation matrices about the fixed axes are
1   0   0
𝑅1(𝜃) = [ 0 cos 𝜃 −sin⁡ 𝜃 ]
0   sin 𝜃   cos 𝜃
********** 13 **********
--- page 14 ---
cos 𝜃 −sin⁡ 𝜃 0
𝑅3(𝜃) = [ sin 𝜃   cos 𝜃   0 ]
0   0   1
Substituting the given angles:
−1   0 0
𝑅3(−𝜋) = [ 0 −1 0 ]
0   0 1
0 0 1
𝑅2 (𝜋 2) = [ 0 1 0 ]
−1 0 0
1 0   0
𝑅1(𝜋) = [ 0 −1 0 ]
0 0 −1
a) Resultant rotation matrix
First multiply the first two rotations:
0 0 1
𝑅2 (𝜋 2) 𝑅3(−𝜋) = [ 0 −1 0 ]
1 0 0
Now multiply by 𝑅1(𝜋):
0 0 1
𝑅= 𝑅1(𝜋) 𝑅2 (𝜋 2) 𝑅3(−𝜋) = [ 0 1 0 ]
−1 0 0
So, the resultant composite rotation matrix is
0 0 1
𝑅= [ 0 1 0 ]
−1 0 0
b) Find [𝑚1]𝐹, [𝑚2]𝐹, and [𝑚3]𝐹
In a rotation matrix, the columns represent the mobile frame axes expressed in the
fixed frame. Thereforescribd+1
0   0   1
[𝑚1]𝐹= [ 0 ] , [𝑚2]𝐹= [ 1 ] , [𝑚3]𝐹= [ 0 ]
−1   0   0
CO-4; b   Explain in detail with schematic how robotic part inspection using a vision system   [10]
.   is carried out in a robotic work cell.
A vision system in a robotic work cell is used for automated part inspection to
ensure quality, precision, and efficiency. The process involves image acquisition,
processing, decision-making, and robotic actions. Below are the detailed steps
involved:
********** 14 **********
--- page 15 ---
Step 1: Image Acquisition
•   The vision system captures images of the part using cameras (2D or 3D),
laser scanners, or infrared sensors.
•   Proper lighting techniques (LED, infrared, structured light) are used to
enhance contrast and eliminate shadows.
•   The camera may be fixed (mounted on a stand) or robot-mounted (attached
to the robotic arm).
Example: A high-resolution camera captures a circuit board for missing
components.
Step 2: Image Preprocessing
•   The raw image is processed to remove noise and enhance features for better
inspection.
•   Common preprocessing techniques include:
o   Grayscale conversion: Simplifies image by removing color variations.
o   Contrast adjustment: Improves defect visibility.
o   Edge detection: Identifies object boundaries using Sobel or Canny edge
detection.
Thresholding: Converts images into black & white for easier defect identification.
Example: The system enhances scratches on a metal surface by adjusting contrast
and applying edge detection.
Step 3: Feature Extraction
•   The system identifies key characteristics of the part, such as:
o   Shape (circular, rectangular, irregular).
o   Size (measuring dimensions).
o   Texture (surface roughness or patterns).
o   Color (RGB analysis).
Example: A robotic vision system measures the diameter of a gear to ensure it
meets specifications.
Step 4: Object Identification & Classification
•   The system compares extracted features with predefined models using:
o   Template Matching: Compares images with reference parts.
o   Machine Learning-Based Classification: Uses trained AI models for defect
detection.
o   Optical Character Recognition (OCR): Reads serial numbers or barcodes.
********** 15 **********
--- page 16 ---
Example: A robotic arm sorts screws by thread type and length using a vision
system.
Step 5: Defect Detection & Quality Control
•   The system checks for common defects, including:
o   Cracks, dents, or scratches on metal parts.
o   Missing components in PCB assembly.
o   Incorrect part dimensions in manufactured products.
•   If a defect is found, the system flags the part for rejection or rework.
Example: A robotic vision system detects a missing resistor on a PCB board and
sends it for rework.
Step 6: Decision-Making & Robotic Action
•   The robot decides the next step based on inspection results:
o   Pass: The part is accepted and moved to the next stage.
o   Fail: The part is rejected and sent for rework or disposal.
o   Reorientation: If the part is misaligned, the robot adjusts its position.
•   The robot uses pick-and-place techniques to sort parts accordingly.
Example: A robotic arm removes faulty glass panels from a production line and
places them in a rejection bin.
Step 7: Data Logging & Feedback for Process Improvement
•   Inspection data is recorded for analysis to improve the manufacturing
process.
•   Machine Learning (ML) models analyze defect trends and help predict
future failures.
•   The system adjusts parameters in real-time for continuous improvement.
Example: A vision system logs defect rates in semiconductor chip production and
suggests tuning machine parameters.
Q6   a. Analyze a 3 Axis Cylindrical Robotic Arm and compute the following.   [20]
CO-3;
i.   Link coordinate diagram
********** 16 **********
--- page 17 ---
7
ii.   Link coordinate table.
5
iii. ARM Matrix.
2
2
2
ARM Matrix
2
Q7   a. Analyze the kinematic parameter table for a two axis RP Robotic arm as follows   [20]
CO-4;   Axis   𝜽𝒌   𝒅𝒌   𝒂𝒌   𝜶𝒌   Variable
1   𝜃1   0   0   −𝜋2 ⁄   𝜃1
2   0   𝑑2   0   0   𝑑2
********** 17 **********
--- page 18 ---
i.   Derive the ARM Matrix.
ii.   For Theta = 60o and d2 = 120 mm find the transformation matrix.
iii.   Derive TCV from the arm matrix and corresponding equations.
iv.   Derive joint equations for all the joints.
The individual link transformation matrices are:
cos 𝜃1   0   −sin⁡ 𝜃1 0
𝐴1 = [ sin 𝜃1   0   cos 𝜃1   0 ]   2
0   −1   0   0
0   0   0   1
1 0 0 0
0 1 0 0
𝐴2 = [   ]
0 0 1 𝑑2
0 0 0 1   2
Hence, the ARM matrix is
cos 𝜃1   0   −sin⁡ 𝜃1 −𝑑2sin⁡ 𝜃1
𝑇= 𝐴1𝐴2 = [ sin 𝜃1   0   cos 𝜃1   𝑑2cos⁡ 𝜃1 ]
0   −1   0   0
0   0   0   1
ii) Transformation matrix for 𝜃1 = 60∘ and 𝑑2 = 120 mm   2
Substituting cos⁡ 60∘= 1 and sin⁡ 60∘= √3 in the ARM matrix:
2   2
1   −√3   √3
0   −120
2   2   2
𝑇= √3   1   1
0   120
2   2   2
0 −1   0   0
[ 0   0   0   1   ]
Therefore,   2
0.5   0   −0.866 −103.92
0.866 0   0.5   60
𝑇= [   ]
0   −1   0   0
0   0   0   1
iii) TCV from the arm matrix and corresponding equations
From the arm matrix, the tool configuration vector is obtained by combining tool
position and orientation terms in compact form as done in the attached inverse
kinematics material. From the above matrix,
𝑥= −𝑑2sin⁡ 𝜃1, 𝑦= 𝑑2cos⁡ 𝜃1, 𝑧= 0
Also, from the rotation part,   3
cos 𝜃1   0   −sin⁡ 𝜃1
𝑛= [ sin 𝜃1 ] , 𝑠= [ 0 ] , 𝑎= [ cos 𝜃1 ]
0   −1   0
Hence the corresponding equations are:
𝑥= −𝑑2sin⁡ 𝜃1   2
********** 18 **********
--- page 19 ---
𝑦= 𝑑2cos⁡ 𝜃1
𝑧= 0
These are the required position equations for the RP robot.
iv) Joint equations for all joints
From
𝑥= −𝑑2sin⁡ 𝜃1, 𝑦= 𝑑2cos⁡ 𝜃1   3
squaring and adding,
𝑥2 + 𝑦2 = 𝑑2 2
Therefore, the prismatic joint equation is
𝑑2 = √𝑥2 + 𝑦2
Now dividing the two equations,
𝑥   −𝑑2sin⁡ 𝜃1
𝑦=   = −tan⁡ 𝜃1
𝑑2cos⁡ 𝜃1
Hence the revolute joint equation is   4
𝜃1 = tan⁡−1 (−𝑥 𝑦)
Thus, the joint equations are
𝑑2 = √𝑥2 + 𝑦2
𝜃1 = tan⁡−1 (−𝑥 𝑦)
These are the required joint-variable equations for the given two-axis RP robot.
********** 19 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper a3afef35a574

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_AI_7012/Robotics/ANS_Robotics(702AI0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/MBA Tech (AI)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Robotics
Date: 02 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-   a. Explain the concept of workspace (work-envelope) and classify industrial robots based [05]
1   on their workspace geometries. Provide neat sketches for Cartesian and SCARA robots
with their applications.
Workspace or work-envelope is the region in space within which a robot can move
its wrist or end-effector and perform useful work. It depends mainly on the robot’s
reach, flexibility, and the arrangement of its first three major joints, so different robot
structures produce different workspace geometries.
The gross work envelope is the locus of points in three-dimensional space reachable
by the wrist, and its geometry is determined by the sequence of the first three major
axes used to position the wrist.
Classification
Industrial robots can be classified based on workspace geometry as follows:   3
•   Cartesian or rectilinear robot, joint combination PPP, workspace is a
rectangular box.
•   Cylindrical robot, joint combination RPP, workspace is a hollow cylinder or
volume between concentric cylinders.
•   Spherical or polar robot, joint combination RRP, workspace is a partial hollow
sphere or spherical shell.
•   Articulated or jointed-arm robot, joint combination RRR, workspace is
irregular and typically complex, often crescent-like in side view.
• SCARA robot, joint combination RRP with all three major axes vertical,
workspace is generally a cylindrical-type volume with a complex horizontal
cross-section depending on joint limits.
********** 1 **********
--- page 2 ---
2
Applications of Cartesian robot:
• Pick and place work
•   Application of sealant
• Assembly operations
• Handling machine tools
• Arc welding
Applications of SCARA robot:
• Pick and place work
• Assembly operations, especially electronic assembly
•   Application of sealant
• Handling machine tools
CO-   b. Compare Proportional, Integral, and Derivative control actions with respect to their [05]
4   effect on settling time, overshoot, and steady-state error in a robotic joint.
Control
Settling time   Overshoot   Steady-state error
action
Usually improves
Cannot eliminate it
response speed, but if   Can increase
Proportional   completely; some
𝐾𝑝is too high it can   overshoot when
(P)   residual error may
cause oscillations and   gain is high
remain
poor settling
Tends to increase
Can increase
settling time because   Eliminates steady-
overshoot,
Integral (I)   the response is slower   state error over
especially with
and may oscillate   time
large integral gain
before settling
Reduces   Does not eliminate
Derivative   Decreases settling time
overshoot and   steady-state error
(D)   by damping rapid
oscillations   directly
********** 2 **********
--- page 3 ---
changes and stabilizing
the response faster
CO-   c.   Justify the transformation matrix for motions consisting of rotation π/4 about axis f 3 [05]
2
at origin, followed by translation of 6 units along the same axis, is part of Screw
transformation.
This motion is a screw transformation because it consists of a rotation and a translation
along the same axis 𝑓3, and for this special case the two homogeneous transformation
matrices commute, so 𝐴𝐵= 𝐵𝐴
First rotate by 𝜋/4 about axis 𝑓3 at the origin, then translate by 6 units along the same
axis 𝑓3. Such a motion is a screw transformation: a linear displacement along an axis   1
together with an angular displacement about the same axis.
the screw transformation is
𝑇= 𝐴𝐵= Rot(𝜋/4,3) Tran(6𝐢3)
and, because the translation and rotation are along the same axis, these matrices
commute, so it can also be written as
𝑇= 𝐵𝐴= Tran(6𝐢3) Rot(𝜋/4,3)
4
This proves that the given motion is a screw transformation because it combines
angular displacement 𝜋/4 and linear displacement 6 along the same axis 𝑓3 ,
with 𝐴𝐵= 𝐵𝐴.
CO-   d. Explain the following general properties of inverse kinematic solution.   [05]
3   i.   Existence of Solution.
ii.   Uniqueness of Solution.
Existence of solution
Existence of solution means determining whether, for a given desired tool
position 𝑝 and orientation 𝑅, there is at least one joint vector 𝑞 that satisfies the arm
equation. If the desired tool-tip position lies outside the robot’s work envelope, then
no inverse kinematic solution can exist.
Even if the desired position lies inside the work envelope, a solution may still not exist   2.5
if the required orientation cannot be achieved without violating joint limits, or if the
robot has fewer than three degrees of freedom for orientation so that some tool
orientations are unrealizable. The notes also explain that although the arm equation
appears to provide 12 equations, only 6 of them are independent because the rotation
matrix columns must be mutually orthogonal and of unit length, so for general
********** 3 **********
--- page 4 ---
manipulation a robot must have at least six axes, 𝑛≥6, though this is only a necessary
condition and not a sufficient one.
Uniqueness of solution
Uniqueness of solution means checking whether the inverse kinematics gives only one
joint configuration for the specified tool configuration or more than one. When   2.5
solutions do exist, they are often not unique.
One reason is kinematic redundancy: if a robot has more than six axes, then it has extra
degrees of freedom, and infinitely many joint vectors may achieve the same tool
position and orientation. Another reason is that even nonredundant robots can have
several distinct solutions for the same tool configuration, such as elbow-up and elbow-
down configurations in an articulated robot, where both produce the same 𝑝 and 𝑅 in
tool space but correspond to different points in joint space.
Q2   a. Explain the following with respect to Industrial robots,   [10]
CO-   i.   Tool Orientation
1   Tool orientation means the angular position of the robot tool or end effector in space
while the tool tip is at a given point. It is usually described by three wrist
motions: yaw, pitch, and roll, where yaw is rotation about one axis, pitch about
another, and roll about the tool’s own axis.   3
In robot kinematics, the first three major axes usually position the wrist, while the
remaining minor axes orient the tool. If three independent orientation axes are
available, the tool can take arbitrary orientations in three-dimensional space.
ii.   Motion Types
Industrial robots generally use two basic motion types: point-to-point motion and
continuous-path motion. In point-to-point motion, the robot moves the tool between
specified positions, and the exact path between those points is not important.   2
Point-to-point motion is used in jobs such as spot welding, pick-and-place, and loading
or unloading. Continuous-path motion is used when the robot must follow a specified
path while working, such as in spray painting, arc welding, gluing, or sealing.
iii.   Number of Axis
The number of axes is the number of independent joint motions available in the robot,
and it is usually the same as the robot’s degrees of freedom. Each joint adds one axis,
and these axes may be revolute for rotary motion or prismatic for linear motion.   2
Usually, axes 1 to 3 are major axes used to position the wrist, while axes 4 to 6 are
minor axes used to orient the tool. A six-axis robot is considered a general manipulator
because it can place the tool at an arbitrary position and arbitrary orientation within
its workspace, while practical industrial robots commonly have four to six axes.
iv.   Reach of the robot
Reach is the maximum distance the robot can extend within its work envelope. More
specifically, horizontal reach is the maximum radial distance of the wrist mounting   3
flange from the robot’s base axis, and vertical reach is the maximum height the wrist
can attain above the work surface.
Reach gives a rough measure of the size of the robot’s work envelope and is important
when selecting a robot for a task. A robot with greater reach can access a larger
working area, but the actual usable workspace also depends on robot geometry, joint
limits, and flexibility.
********** 4 **********
--- page 5 ---
CO-   b. Suppose, F = {f1, f2, f3} and M = {m1, m2, m3} are two initially coincident fixed [10]
3
and mobile orthonormal coordinate frames, respectively. Suppose we perform the
following sequence of operations:
1. Rotate the mobile frame M about the f 3-axis by π radians.
2
2. Translate the mobile frame along the f 1 -axis by 8 units.
3. Rotate the mobile frame about its own f 2 -axis by π radians.
2
a. Calculate the Resultant Transformation Matrix
The composite matrix is
𝑇𝑏= 𝑇𝑅2(𝜋/2) 𝑇𝑥(8) 𝑇𝑅3(𝜋)   1
Multiply the first two matrices
0 0 1 0
0 1 0 0
𝑇𝑅2(𝜋/2)𝑇𝑥(8) = [   ]
−1 0 0 −8
0 0 0 1
Multiply by the last rotation
0 0 1 0 −1   0 0 0   2
0 1 0 0   0 −1 0 0
𝑇𝑏= [   ] [   ]
−1 0 0 −8   0   0 1 0
0 0 0 1   0   0 0 1
This gives
0 0   1 0
0 −1 0 0
𝑇𝑏= [   ]
1 0   0 −8
0 0   0 1
b. Calculate the Resultant Transformation Matrix if the order of motions is
reversed.
The composite transformation is
𝑇𝑎= 𝑇𝑅3(𝜋) 𝑇𝑥(8) 𝑇𝑅2(𝜋/2)
********** 5 **********
--- page 6 ---
Multiply first two matrices
−1 0   0 −8
0 −1 0 0
𝑇𝑅3(𝜋)𝑇𝑥(8) = [   ]
0   0   1 0
0   0   0 1
because the −1 on the 𝑥-axis flips the translation to −8.
Multiply by the final rotation
−1 0   0 −8   0 0 1 0
0 −1 0 0   0 1 0 0   2
𝑇𝑎= [   ] [   ]
0   0   1 0 −1 0 0 0
0   0   0 1   0 0 0 1
Carrying out the multiplication:
0   0 −1 −8
0 −1 0   0
𝑇𝑎= [   ]
−1 0   0   0
0   0   0   1
Find [p]F in both cases (a & b) given [p]M = [3 4 5]T
Case a
3
Case b
Q3   a. Analyze the kinematic parameter table for a 5 axis robot as follows   [10]
CO-   Axis   𝜽𝒌   𝒅𝒌   𝒂𝒌   𝜶𝒌   Variable
3
1   𝜃1   𝑑1   0   −𝜋2 ⁄   𝜃1
2   𝜃2   0   𝑎2   0   𝜃2
3   𝜃3   0   𝑎3   0   𝜃3
4   𝜃4   0   0   −𝜋2 ⁄   𝜃4
5   𝜃5   𝑑5   0   0   𝜃5
Derive all the Individual Link co-ordinate transformation Matrices for all the joints.
For the given D-H table, the individual transformation from frame 𝑘 to frame 𝑘−1 is
obtained from the standard D-H homogeneous matrix
********** 6 **********
--- page 7 ---
2*5
b. Explain open‑loop control in robotics with at least two detailed industrial examples. [10]
Comment on accuracy, disturbance sensitivity, and suitability for repetitive robotic
tasks.
Open-loop control in robotics means the controller sends commands to actuators
without measuring the actual output, so the output does not influence the control action
during operation. In practice, the robot follows pre-set instructions, timing, or motion
sequences, but it does not verify whether the commanded motion, position, or task
outcome was achieved.   2
How it works
********** 7 **********
--- page 8 ---
An open-loop robotic system typically has an input command, a controller, actuators,
and the robot mechanism, but no feedback path from sensors to correct errors in real   2
time. This makes the design simpler, cheaper, and inherently stable, but also less
accurate and less adaptable than a closed-loop system.
In robotics, open-loop control is most useful when the environment is predictable, the
motions are repeatable, and the process can be calibrated in advance. Educational and
some simple industrial robots have used open-loop position control with stepper
motors, while more advanced robots usually add feedback when precision is critical.
Industrial examples
• Simple pick-and-place material handling robot: A basic parts-transfer robot
can be programmed to move from a taught pickup point to a taught drop-off
point using fixed motor commands and timing, without checking whether the
part was grasped or placed correctly. This kind of non-servo or endpoint-style   2
operation is associated with simple, repetitive transfer tasks and is attractive
because it is low cost, fast, and easy to program for stable production lines.
• Pneumatic non-servo robot on an assembly or packaging line: Pneumatic
robots are widely used for short-cycle pick-and-place operations where
compressed air drives simple sliding or rotating joints and the robot repeats the
same motion sequence again. These systems suit repetitive loading, unloading,
and packaging tasks, but their control accuracy is limited because air
compressibility reduces precision and the robot typically does not correct for
part misalignment or load variation during motion.   2
• Open-loop stepper-motor educational or light-duty articulated arm: Some
tabletop robots use open-loop position control with stepper motors, meaning
the controller assumes each commanded step is executed and does not measure
the true joint position. This approach is acceptable for low-load demonstrations
or highly repeatable bench tasks, but missed steps, friction, or unexpected loads
can accumulate into position errors because there is no feedback-based
correction.
Accuracy and disturbances   2
Open-loop robotic control is generally less accurate because it cannot detect or
correct the difference between desired motion and actual motion. Any error caused by
calibration drift, backlash, missed motor steps, actuator variation, or part-position
changes remains uncorrected unless a human recalibrates or reprograms the system.
It is also highly sensitive to disturbances such as load changes, friction changes, air-
pressure variation, slippage, or fixture misalignment, since the controller has no
measured output to compensate for those effects. By contrast, feedback-based robotic
systems are preferred when the task requires automatic correction, high precision, or
adaptation to changing conditions.
Repetitive-task suitability
Open-loop control is well suited to repetitive robotic tasks when the workpiece
location, robot motion, and process conditions remain nearly constant from cycle to
cycle. Typical examples include repeated transfer between fixed points, simple
machine loading and unloading, and high-speed packaging motions where low cost
and simplicity matter more than fine accuracy.
********** 8 **********
--- page 9 ---
Its limitation is that repetitive does not always mean robust, because even in repetitive
factories small disturbances can accumulate and degrade quality over time. For that
reason, open-loop control is best for simple, well-structured tasks, while closed-loop
control is usually chosen for welding, precision assembly, vision-guided handling, or
any task that must maintain accuracy under uncertainty.
Q4   a. Discuss the pick-and-place operation of a robotic arm, describing the process steps [10]
CO-   and its speed control mechanism.
4
A pick-and-place operation is a basic robotic material-handling task in which the robot
moves to a part, grasps it, transports it to a target location, and releases it there. It is
usually treated as a point-to-point motion problem, because the important requirement
is reaching specific discrete positions such as pick, lift-off, set-down, and place points.
3
Process steps
The minimal pick-and-place trajectory uses four key points: the pick point where the
part is grasped, a nearby lift-off point above it, the place point where the part is
deposited, and a nearby set-down point above the destination. The lift-off and set-
down points are intermediate safe approach positions that let the robot make a fast
gross motion first and then a careful fine motion near the work surface.
A typical operating sequence is:
• Move quickly to the lift-off point.
• Pause briefly so vibrations or ringing decay.   3
• Move very slowly down to the pick point.
• Close the gripper and grasp the part, then move slowly back to the lift-off point.
• Travel at high speed through the gross path, sometimes via obstacle-avoiding
intermediate points, to the set-down point.
• Pause again, move very slowly to the place point, release the part, and retreat
slowly back to set-down.
The pick orientation and place orientation are chosen so the tool’s approach vector is
usually normal to the surface, which helps the gripper approach and depart cleanly
without scraping or misplacing the part. The robot must also hold the part firmly
enough to prevent slipping but gently enough to avoid damage, and it must avoid
collisions with surrounding objects during approach and withdrawal.   2
Speed control
The speed control mechanism in pick-and-place is usually based on varying robot
speed across different segments of the trajectory rather than using one constant speed
for the whole cycle. Gross transfer motions between lift-off and set-down are
********** 9 **********

[Text in pictures on this page, read by OCR]
Gross motion

Gross
motion

Gross
motion

Litt-off EJ Set-down
Fine Fine
motion motion

Pick Place

Work surface
--- page 10 ---
performed fast for productivity, while the fine approach and departure motions near
the pick and place surfaces are performed slowly for safety and accuracy.
A standard segment-wise speed pattern is shown below:
Segment   Motion type   Typical speed
To lift-off   Gross   Fast
Pause before pick   Fine settling   Zero
Lift-off to pick   Fine   Very slow
2
Grasp   Fine   Slow
Pick to lift-off   Fine   Slow
Lift-off to set-down or via points   Gross   Fast
Pause before place   Fine settling   Zero
Set-down to place   Fine   Very slow
Release   Fine   Slow
Place to set-down   Fine   Slow
CO-   b. Discuss PID controller and discuss various tuning methods, including steps and their [10]
2   suitability for robotic systems.
A PID controller is a feedback controller that combines proportional, integral, and
derivative actions to drive a system output toward a desired setpoint with a balance of
speed, accuracy, and stability. In robotics, PID control is widely used for joint position
control, motor speed control, balancing robots, robotic arms, and drones because it can
correct present error, accumulated past error, and the predicted trend of error at the
same time.
3
PID controller
The control signal in PID control is formed from three parts: proportional action reacts
to the current error, integral action accumulates error over time to remove steady-state
error, and derivative action responds to the rate of change of error to reduce overshoot
********** 10 **********
--- page 11 ---
and improve damping. A well-tuned PID controller therefore gives fast response, small
or zero steady-state error, and smoother settling than P, PI, or PD alone.
Each term has a specific effect on robotic performance:
•   Proportional gain 𝐾𝑝 speeds up response, but too much can cause overshoot
and oscillation.
•   Integral gain 𝐾𝑖 removes residual error, but too much can slow the system and
create overshoot or windup.
•   Derivative gain 𝐾𝑑 damps motion and reduces overshoot, but it is sensitive to
measurement noise.   3
In robotic arms, PID is often applied per joint, so each axis has its own control loop
and gains, which keeps implementation simple and practical for many commercial
robots. Its main weakness is that changing loads, gravity effects, friction, and coupling
between joints can reduce performance, especially in fast multi-axis motion.
Tuning methods
PID tuning means choosing 𝐾𝑝, 𝐾𝑖, and 𝐾𝑑 so the robot responds quickly without
excessive overshoot, oscillation, or slow settling. Common methods include manual
tuning, Ziegler-Nichols tuning, and Cohen-Coon tuning, while many robotic systems
also use software-assisted or auto-tuning as a starting point.
Method Main idea   Basic steps   Suitability
Set 𝐾𝑖= 0, 𝐾𝑑= 0; raise   4
𝐾𝑝until oscillation starts; Good for simple robots,
Trial-and-error
Manual   add 𝐾𝑑to damp   lab systems, and when a
adjustment of
tuning   oscillation; add   precise model is
gains
𝐾𝑖gradually to remove   unavailable
steady-state error
Set 𝐾𝑖= 0, 𝐾𝑑= 0;
Use ultimate   increase 𝐾𝑝until   Fast and systematic, but
gain and   sustained oscillation;   can be aggressive for
Ziegler-
oscillation   record ultimate gain   robots that must avoid
Nichols
period to   𝐾𝑢and period 𝑇𝑢;   overshoot Control-
compute gains   compute gains from   Systems.pdf+1
standard formulas
Perform open-loop step   Better for systems with
Use open-loop   test; estimate process   dead time, but more
Cohen-
step-response   gain, dead time, and time process-model oriented
Coon
data   constant; calculate PID   and less convenient for
gains from formulas   many robot joints
Q5   a. Suppose, F = {f1, f2, f3} and M = {m1, m2, m3} are two initially coincident fixed [10]
CO-   and mobile orthonormal coordinate frames, respectively.
2
1. Suppose we rotate mobile coordinate frame M along f1 axis of fixed coordinate
frame by π/2 rad
********** 11 **********
--- page 12 ---
2. Suppose we rotate mobile coordinate frame M from the origin about f2 axis of
fixed coordinate frame by -π rad.
a. Calculate the Resultant Matrix for both individual rotations
2
2
b. Solve for [q]M after each rotation given [q]F = [10 12 14]T in both cases.
Case 1
4
Case 2
c. Also draw vector diagrams.
Vector diagram for case 1:
2
• 𝑚1 stays along +𝑓1
• 𝑚2 moves to +𝑓3
• 𝑚3 moves to −𝑓2
Vector diagram for case 2:
• 𝑚1 moves to −𝑓1
• 𝑚2 stays along +𝑓2
• 𝑚3 moves to −𝑓3
CO-   b. Explain in detail with schematic how robotic part inspection using a vision system is [10]
4   carried out in a robotic work cell.
Robotic part inspection with a vision system in a work cell is carried out by first
imaging the part, extracting its position, orientation, and quality features, and then
********** 12 **********
--- page 13 ---
using that information to command the robot to accept, reject, or reorient the part. In
a typical single-robot cell, a part is placed in the viewing area of an overhead camera,   2
the vision system inspects it, and the robot controller sends the part to a pass bin or a
reject bin based on the inspection result.
Cell layout
A common arrangement is a feeder or conveyor, an inspection zone under an overhead
camera with controlled lighting, a robot arm with gripper, and separate pass and reject
bins. The camera observes the part, the vision processor determines the part pose and
condition, and the robot uses that result to plan a pick-and-place motion.
Inspection sequence
The process usually follows a fixed sequence: image acquisition, preprocessing,
feature extraction, identification, defect detection, decision-making, and robotic
handling. The document on the robotic work cell explicitly lists these stages and notes
that proper lighting and either fixed or robot-mounted cameras are used to improve
inspection quality.
The main steps are:
• Image acquisition: the camera captures the part image, often with LED,
infrared, or structured lighting to improve contrast and reduce shadows.
• Image preprocessing: the image is cleaned and enhanced using grayscale
conversion, contrast adjustment, thresholding, and edge detection so important   6
boundaries and defects are easier to isolate.
•   Feature extraction: the system measures features such as shape, size, texture,
and sometimes color.
•   Identification and classification: the extracted features are compared with a
reference model using methods such as template matching, OCR, or trained
classifiers.
• Defect detection: the system checks for faults such as cracks, dents, scratches,
missing components, or wrong dimensions.
• Decision and action: the robot either accepts the part, rejects it, or reorients it
for downstream handling.
Coordinate conversion   2
A key part of the work cell is converting what the camera sees into robot coordinates,
because the camera measures the part pose in the camera frame while the robot moves
in its base frame. This is done with homogeneous transformation matrices so the part
pose relative to the robot base can be computed from the camera-to-part and camera-
to-base   transformations.Fundamentals-of-Robotics_-Analysis-and-Control-
PDFDrive.com.pdf+1
In the worked example, the system uses
𝑇𝑏𝑎𝑠𝑒 𝑝𝑎𝑟𝑡= (𝑇𝑐𝑎𝑚𝑒𝑟𝑎 𝑏𝑎𝑠𝑒 )−1𝑇𝑐𝑎𝑚𝑒𝑟𝑎 𝑝𝑎𝑟𝑡
Q6   a. Analyze the four axis SCARA Adept One Robotic Arm and compute the following.   [20]
CO-
3
********** 13 **********
--- page 14 ---
i. Link coordinate diagram
8
ii. Link coordinate table.
Axis 𝑘   𝜃𝑘   𝑑𝑘   𝑎𝑘   𝛼𝑘   Joint type
4
1   𝑞1   𝑑1   𝑎1   0   Revolute
2   𝑞2   0   𝑎2   𝜋   Revolute
3   0   𝑑3   0   0   Prismatic
4   𝑞4   𝑑4   0   0   Revolute
iii. Individual Link coordinate transformation matrices.
Using the standard D-H adjacent-link transform
********** 14 **********
--- page 15 ---
2*4
Q7   a. Analyze the ARM matrix for a 3-axis PARA robot:   [20]
CO-   𝐶123 −𝑆123 0 𝑎1𝐶1 + 𝑎2𝐶12
4   𝑆123   𝐶123 0 𝑎1𝑆1 + 𝑎2𝑆12
[   ]
0   0   1   𝑑3
0   0   0   1
i.   Extract the Tool Configuration Vector (TCV)
For the planar robot shown in your image, the arm matrix is
𝐶123 −𝑆123 0 𝑎1𝐶1 + 𝑎2𝐶12
𝑇= [ 𝑆123   𝐶123   0 𝑎1𝑆1 + 𝑎2𝑆12 ]
0   0   1   𝑑3
0   0   0   1
where 𝐶12 = cos (𝑞1 + 𝑞2), 𝑆12 = sin (𝑞1 + 𝑞2), and 𝐶123, 𝑆123 describe the planar
tool orientation. The attached note extracts the tool-configuration vector as
𝑎1𝐶1 + 𝑎2𝐶12
𝑎1𝑆1 + 𝑎2𝑆12
𝑑3
𝑤(𝑞) =
0
0
[ exp (𝑞3/𝜋) ]
5
So the six scalar TCV equations are:
• 𝑤1 = 𝑎1𝐶1 + 𝑎2𝐶12
• 𝑤2 = 𝑎1𝑆1 + 𝑎2𝑆12
• 𝑤3 = 𝑑3
• 𝑤4 = 0
• 𝑤5 = 0
• 𝑤6 = exp (𝑞3/𝜋)
ii.   Derive the complete inverse kinematic equations for q1, q2, q3
To isolate the second joint, square and add 𝑤1 and 𝑤2, which eliminates 𝑞1 and
yields
𝑤1 2 + 𝑤2 2 = 𝑎1 2 + 2𝑎1𝑎2cos 𝑞2 + 𝑎2 2
********** 15 **********
--- page 16 ---
. Therefore,   6
2 + 𝑤2 2 −𝑎1 2 −𝑎2 2
𝑞2 = ±arccos (𝑤1   )
2𝑎1𝑎2
which gives the two standard planar-arm configurations, often called left-handed and
right-handed solutions.
With 𝑞2 known, rewrite the first two TCV equations as
𝑤1 = (𝑎1 + 𝑎2𝐶2)𝐶1 −(𝑎2𝑆2)𝑆1
and
𝑤2 = (𝑎2𝑆2)𝐶1 + (𝑎1 + 𝑎2𝐶2)𝑆1
6
Solving these for 𝑞1 gives
𝑞1 = atan2 ((𝑎1 + 𝑎2𝐶2)𝑤2 −(𝑎2𝑆2)𝑤1,  (𝑎1 + 𝑎2𝐶2)𝑤1 + (𝑎2𝑆2)𝑤2)
Third joint
The third joint follows directly from the last component of the tool-configuration
vector because 𝑤6 = exp (𝑞3/𝜋). Taking the natural logarithm gives   3
𝑞3 = 𝜋ln (𝑤6)
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 24c3af2c2b4a

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_AI_7051/Robotics/ANS_Robotics(702AI0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/MBA Tech (AI)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Robotics
Date: 02 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of the remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-   a. Explain the concept of workspace (work-envelope) and classify industrial robots based [05]
1   on their workspace geometries. Provide neat sketches for Cartesian and SCARA robots
with their applications.
Workspace or work-envelope is the region in space within which a robot can move
its wrist or end-effector and perform useful work. It depends mainly on the robot’s
reach, flexibility, and the arrangement of its first three major joints, so different robot
structures produce different workspace geometries.
The gross work envelope is the locus of points in three-dimensional space reachable
by the wrist, and its geometry is determined by the sequence of the first three major
axes used to position the wrist.
Classification
Industrial robots can be classified based on workspace geometry as follows:   3
•   Cartesian or rectilinear robot, joint combination PPP, workspace is a
rectangular box.
•   Cylindrical robot, joint combination RPP, workspace is a hollow cylinder or
volume between concentric cylinders.
•   Spherical or polar robot, joint combination RRP, workspace is a partial hollow
sphere or spherical shell.
•   Articulated or jointed-arm robot, joint combination RRR, workspace is
irregular and typically complex, often crescent-like in side view.
• SCARA robot, joint combination RRP with all three major axes vertical,
workspace is generally a cylindrical-type volume with a complex horizontal
cross-section depending on joint limits.
********** 1 **********
--- page 2 ---
2
Applications of Cartesian robot:
• Pick and place work
•   Application of sealant
• Assembly operations
• Handling machine tools
• Arc welding
Applications of SCARA robot:
• Pick and place work
• Assembly operations, especially electronic assembly
•   Application of sealant
• Handling machine tools
CO-   b. Compare Proportional, Integral, and Derivative control actions with respect to their [05]
4   effect on settling time, overshoot, and steady-state error in a robotic joint.
Control
Settling time   Overshoot   Steady-state error
action
Usually improves
Cannot eliminate it
response speed, but if   Can increase
Proportional   completely; some
𝐾𝑝is too high it can   overshoot when
(P)   residual error may
cause oscillations and   gain is high
remain
poor settling
Tends to increase
Can increase
settling time because   Eliminates steady-
overshoot,
Integral (I)   the response is slower   state error over
especially with
and may oscillate   time
large integral gain
before settling
Reduces   Does not eliminate
Derivative   Decreases settling time
overshoot and   steady-state error
(D)   by damping rapid
oscillations   directly
********** 2 **********
--- page 3 ---
changes and stabilizing
the response faster
CO-   c.   Justify the transformation matrix for motions consisting of rotation π/4 about axis f 3 [05]
2
at origin, followed by translation of 6 units along the same axis, is part of Screw
transformation.
This motion is a screw transformation because it consists of a rotation and a translation
along the same axis 𝑓3, and for this special case the two homogeneous transformation
matrices commute, so 𝐴𝐵= 𝐵𝐴
First rotate by 𝜋/4 about axis 𝑓3 at the origin, then translate by 6 units along the same
axis 𝑓3. Such a motion is a screw transformation: a linear displacement along an axis   1
together with an angular displacement about the same axis.
the screw transformation is
𝑇= 𝐴𝐵= Rot(𝜋/4,3) Tran(6𝐢3)
and, because the translation and rotation are along the same axis, these matrices
commute, so it can also be written as
𝑇= 𝐵𝐴= Tran(6𝐢3) Rot(𝜋/4,3)
4
This proves that the given motion is a screw transformation because it combines
angular displacement 𝜋/4 and linear displacement 6 along the same axis 𝑓3 ,
with 𝐴𝐵= 𝐵𝐴.
CO-   d. Explain the following general properties of inverse kinematic solution.   [05]
3   i.   Existence of Solution.
ii.   Uniqueness of Solution.
Existence of solution
Existence of solution means determining whether, for a given desired tool
position 𝑝 and orientation 𝑅, there is at least one joint vector 𝑞 that satisfies the arm
equation. If the desired tool-tip position lies outside the robot’s work envelope, then
no inverse kinematic solution can exist.
Even if the desired position lies inside the work envelope, a solution may still not exist   2.5
if the required orientation cannot be achieved without violating joint limits, or if the
robot has fewer than three degrees of freedom for orientation so that some tool
orientations are unrealizable. The notes also explain that although the arm equation
appears to provide 12 equations, only 6 of them are independent because the rotation
matrix columns must be mutually orthogonal and of unit length, so for general
********** 3 **********
--- page 4 ---
manipulation a robot must have at least six axes, 𝑛≥6, though this is only a necessary
condition and not a sufficient one.
Uniqueness of solution
Uniqueness of solution means checking whether the inverse kinematics gives only one
joint configuration for the specified tool configuration or more than one. When   2.5
solutions do exist, they are often not unique.
One reason is kinematic redundancy: if a robot has more than six axes, then it has extra
degrees of freedom, and infinitely many joint vectors may achieve the same tool
position and orientation. Another reason is that even nonredundant robots can have
several distinct solutions for the same tool configuration, such as elbow-up and elbow-
down configurations in an articulated robot, where both produce the same 𝑝 and 𝑅 in
tool space but correspond to different points in joint space.
Q2   a. Explain the following with respect to Industrial robots,   [10]
CO-   i.   Tool Orientation
1   Tool orientation means the angular position of the robot tool or end effector in space
while the tool tip is at a given point. It is usually described by three wrist
motions: yaw, pitch, and roll, where yaw is rotation about one axis, pitch about
another, and roll about the tool’s own axis.   3
In robot kinematics, the first three major axes usually position the wrist, while the
remaining minor axes orient the tool. If three independent orientation axes are
available, the tool can take arbitrary orientations in three-dimensional space.
ii.   Motion Types
Industrial robots generally use two basic motion types: point-to-point motion and
continuous-path motion. In point-to-point motion, the robot moves the tool between
specified positions, and the exact path between those points is not important.   2
Point-to-point motion is used in jobs such as spot welding, pick-and-place, and loading
or unloading. Continuous-path motion is used when the robot must follow a specified
path while working, such as in spray painting, arc welding, gluing, or sealing.
iii.   Number of Axis
The number of axes is the number of independent joint motions available in the robot,
and it is usually the same as the robot’s degrees of freedom. Each joint adds one axis,
and these axes may be revolute for rotary motion or prismatic for linear motion.   2
Usually, axes 1 to 3 are major axes used to position the wrist, while axes 4 to 6 are
minor axes used to orient the tool. A six-axis robot is considered a general manipulator
because it can place the tool at an arbitrary position and arbitrary orientation within
its workspace, while practical industrial robots commonly have four to six axes.
iv.   Reach of the robot
Reach is the maximum distance the robot can extend within its work envelope. More
specifically, horizontal reach is the maximum radial distance of the wrist mounting   3
flange from the robot’s base axis, and vertical reach is the maximum height the wrist
can attain above the work surface.
Reach gives a rough measure of the size of the robot’s work envelope and is important
when selecting a robot for a task. A robot with greater reach can access a larger
working area, but the actual usable workspace also depends on robot geometry, joint
limits, and flexibility.
********** 4 **********
--- page 5 ---
CO-   b. Suppose, F = {f1, f2, f3} and M = {m1, m2, m3} are two initially coincident fixed [10]
3
and mobile orthonormal coordinate frames, respectively. Suppose we perform the
following sequence of operations:
1. Rotate the mobile frame M about the f 3-axis by π radians.
2
2. Translate the mobile frame along the f 1 -axis by 8 units.
3. Rotate the mobile frame about its own f 2 -axis by π radians.
2
a. Calculate the Resultant Transformation Matrix
The composite matrix is
𝑇𝑏= 𝑇𝑅2(𝜋/2) 𝑇𝑥(8) 𝑇𝑅3(𝜋)   1
Multiply the first two matrices
0 0 1 0
0 1 0 0
𝑇𝑅2(𝜋/2)𝑇𝑥(8) = [   ]
−1 0 0 −8
0 0 0 1
Multiply by the last rotation
0 0 1 0 −1   0 0 0   2
0 1 0 0   0 −1 0 0
𝑇𝑏= [   ] [   ]
−1 0 0 −8   0   0 1 0
0 0 0 1   0   0 0 1
This gives
0 0   1 0
0 −1 0 0
𝑇𝑏= [   ]
1 0   0 −8
0 0   0 1
b. Calculate the Resultant Transformation Matrix if the order of motions is
reversed.
The composite transformation is
𝑇𝑎= 𝑇𝑅3(𝜋) 𝑇𝑥(8) 𝑇𝑅2(𝜋/2)
********** 5 **********
--- page 6 ---
Multiply first two matrices
−1 0   0 −8
0 −1 0 0
𝑇𝑅3(𝜋)𝑇𝑥(8) = [   ]
0   0   1 0
0   0   0 1
because the −1 on the 𝑥-axis flips the translation to −8.
Multiply by the final rotation
−1 0   0 −8   0 0 1 0
0 −1 0 0   0 1 0 0   2
𝑇𝑎= [   ] [   ]
0   0   1 0 −1 0 0 0
0   0   0 1   0 0 0 1
Carrying out the multiplication:
0   0 −1 −8
0 −1 0   0
𝑇𝑎= [   ]
−1 0   0   0
0   0   0   1
Find [p]F in both cases (a & b) given [p]M = [3 4 5]T
Case a
3
Case b
Q3   a. Analyze the kinematic parameter table for a 5 axis robot as follows   [10]
CO-   Axis   𝜽𝒌   𝒅𝒌   𝒂𝒌   𝜶𝒌   Variable
3
1   𝜃1   𝑑1   0   −𝜋2 ⁄   𝜃1
2   𝜃2   0   𝑎2   0   𝜃2
3   𝜃3   0   𝑎3   0   𝜃3
4   𝜃4   0   0   −𝜋2 ⁄   𝜃4
5   𝜃5   𝑑5   0   0   𝜃5
Derive all the Individual Link co-ordinate transformation Matrices for all the joints.
For the given D-H table, the individual transformation from frame 𝑘 to frame 𝑘−1 is
obtained from the standard D-H homogeneous matrix
********** 6 **********
--- page 7 ---
2*5
b. Explain open‑loop control in robotics with at least two detailed industrial examples. [10]
Comment on accuracy, disturbance sensitivity, and suitability for repetitive robotic
tasks.
Open-loop control in robotics means the controller sends commands to actuators
without measuring the actual output, so the output does not influence the control action
during operation. In practice, the robot follows pre-set instructions, timing, or motion
sequences, but it does not verify whether the commanded motion, position, or task
outcome was achieved.   2
How it works
********** 7 **********
--- page 8 ---
An open-loop robotic system typically has an input command, a controller, actuators,
and the robot mechanism, but no feedback path from sensors to correct errors in real   2
time. This makes the design simpler, cheaper, and inherently stable, but also less
accurate and less adaptable than a closed-loop system.
In robotics, open-loop control is most useful when the environment is predictable, the
motions are repeatable, and the process can be calibrated in advance. Educational and
some simple industrial robots have used open-loop position control with stepper
motors, while more advanced robots usually add feedback when precision is critical.
Industrial examples
• Simple pick-and-place material handling robot: A basic parts-transfer robot
can be programmed to move from a taught pickup point to a taught drop-off
point using fixed motor commands and timing, without checking whether the
part was grasped or placed correctly. This kind of non-servo or endpoint-style   2
operation is associated with simple, repetitive transfer tasks and is attractive
because it is low cost, fast, and easy to program for stable production lines.
• Pneumatic non-servo robot on an assembly or packaging line: Pneumatic
robots are widely used for short-cycle pick-and-place operations where
compressed air drives simple sliding or rotating joints and the robot repeats the
same motion sequence again. These systems suit repetitive loading, unloading,
and packaging tasks, but their control accuracy is limited because air
compressibility reduces precision and the robot typically does not correct for
part misalignment or load variation during motion.   2
• Open-loop stepper-motor educational or light-duty articulated arm: Some
tabletop robots use open-loop position control with stepper motors, meaning
the controller assumes each commanded step is executed and does not measure
the true joint position. This approach is acceptable for low-load demonstrations
or highly repeatable bench tasks, but missed steps, friction, or unexpected loads
can accumulate into position errors because there is no feedback-based
correction.
Accuracy and disturbances   2
Open-loop robotic control is generally less accurate because it cannot detect or
correct the difference between desired motion and actual motion. Any error caused by
calibration drift, backlash, missed motor steps, actuator variation, or part-position
changes remains uncorrected unless a human recalibrates or reprograms the system.
It is also highly sensitive to disturbances such as load changes, friction changes, air-
pressure variation, slippage, or fixture misalignment, since the controller has no
measured output to compensate for those effects. By contrast, feedback-based robotic
systems are preferred when the task requires automatic correction, high precision, or
adaptation to changing conditions.
Repetitive-task suitability
Open-loop control is well suited to repetitive robotic tasks when the workpiece
location, robot motion, and process conditions remain nearly constant from cycle to
cycle. Typical examples include repeated transfer between fixed points, simple
machine loading and unloading, and high-speed packaging motions where low cost
and simplicity matter more than fine accuracy.
********** 8 **********
--- page 9 ---
Its limitation is that repetitive does not always mean robust, because even in repetitive
factories small disturbances can accumulate and degrade quality over time. For that
reason, open-loop control is best for simple, well-structured tasks, while closed-loop
control is usually chosen for welding, precision assembly, vision-guided handling, or
any task that must maintain accuracy under uncertainty.
Q4   a. Discuss the pick-and-place operation of a robotic arm, describing the process steps [10]
CO-   and its speed control mechanism.
4
A pick-and-place operation is a basic robotic material-handling task in which the robot
moves to a part, grasps it, transports it to a target location, and releases it there. It is
usually treated as a point-to-point motion problem, because the important requirement
is reaching specific discrete positions such as pick, lift-off, set-down, and place points.
3
Process steps
The minimal pick-and-place trajectory uses four key points: the pick point where the
part is grasped, a nearby lift-off point above it, the place point where the part is
deposited, and a nearby set-down point above the destination. The lift-off and set-
down points are intermediate safe approach positions that let the robot make a fast
gross motion first and then a careful fine motion near the work surface.
A typical operating sequence is:
• Move quickly to the lift-off point.
• Pause briefly so vibrations or ringing decay.   3
• Move very slowly down to the pick point.
• Close the gripper and grasp the part, then move slowly back to the lift-off point.
• Travel at high speed through the gross path, sometimes via obstacle-avoiding
intermediate points, to the set-down point.
• Pause again, move very slowly to the place point, release the part, and retreat
slowly back to set-down.
The pick orientation and place orientation are chosen so the tool’s approach vector is
usually normal to the surface, which helps the gripper approach and depart cleanly
without scraping or misplacing the part. The robot must also hold the part firmly
enough to prevent slipping but gently enough to avoid damage, and it must avoid
collisions with surrounding objects during approach and withdrawal.   2
Speed control
The speed control mechanism in pick-and-place is usually based on varying robot
speed across different segments of the trajectory rather than using one constant speed
for the whole cycle. Gross transfer motions between lift-off and set-down are
********** 9 **********

[Text in pictures on this page, read by OCR]
Gross motion

Gross
motion

Gross
motion

Litt-off EJ Set-down
Fine Fine
motion motion

Pick Place

Work surface
--- page 10 ---
performed fast for productivity, while the fine approach and departure motions near
the pick and place surfaces are performed slowly for safety and accuracy.
A standard segment-wise speed pattern is shown below:
Segment   Motion type   Typical speed
To lift-off   Gross   Fast
Pause before pick   Fine settling   Zero
Lift-off to pick   Fine   Very slow
2
Grasp   Fine   Slow
Pick to lift-off   Fine   Slow
Lift-off to set-down or via points   Gross   Fast
Pause before place   Fine settling   Zero
Set-down to place   Fine   Very slow
Release   Fine   Slow
Place to set-down   Fine   Slow
CO-   b. Discuss PID controller and discuss various tuning methods, including steps and their [10]
2   suitability for robotic systems.
A PID controller is a feedback controller that combines proportional, integral, and
derivative actions to drive a system output toward a desired setpoint with a balance of
speed, accuracy, and stability. In robotics, PID control is widely used for joint position
control, motor speed control, balancing robots, robotic arms, and drones because it can
correct present error, accumulated past error, and the predicted trend of error at the
same time.
3
PID controller
The control signal in PID control is formed from three parts: proportional action reacts
to the current error, integral action accumulates error over time to remove steady-state
error, and derivative action responds to the rate of change of error to reduce overshoot
********** 10 **********
--- page 11 ---
and improve damping. A well-tuned PID controller therefore gives fast response, small
or zero steady-state error, and smoother settling than P, PI, or PD alone.
Each term has a specific effect on robotic performance:
•   Proportional gain 𝐾𝑝 speeds up response, but too much can cause overshoot
and oscillation.
•   Integral gain 𝐾𝑖 removes residual error, but too much can slow the system and
create overshoot or windup.
•   Derivative gain 𝐾𝑑 damps motion and reduces overshoot, but it is sensitive to
measurement noise.   3
In robotic arms, PID is often applied per joint, so each axis has its own control loop
and gains, which keeps implementation simple and practical for many commercial
robots. Its main weakness is that changing loads, gravity effects, friction, and coupling
between joints can reduce performance, especially in fast multi-axis motion.
Tuning methods
PID tuning means choosing 𝐾𝑝, 𝐾𝑖, and 𝐾𝑑 so the robot responds quickly without
excessive overshoot, oscillation, or slow settling. Common methods include manual
tuning, Ziegler-Nichols tuning, and Cohen-Coon tuning, while many robotic systems
also use software-assisted or auto-tuning as a starting point.
Method Main idea   Basic steps   Suitability
Set 𝐾𝑖= 0, 𝐾𝑑= 0; raise   4
𝐾𝑝until oscillation starts; Good for simple robots,
Trial-and-error
Manual   add 𝐾𝑑to damp   lab systems, and when a
adjustment of
tuning   oscillation; add   precise model is
gains
𝐾𝑖gradually to remove   unavailable
steady-state error
Set 𝐾𝑖= 0, 𝐾𝑑= 0;
Use ultimate   increase 𝐾𝑝until   Fast and systematic, but
gain and   sustained oscillation;   can be aggressive for
Ziegler-
oscillation   record ultimate gain   robots that must avoid
Nichols
period to   𝐾𝑢and period 𝑇𝑢;   overshoot Control-
compute gains   compute gains from   Systems.pdf+1
standard formulas
Perform open-loop step   Better for systems with
Use open-loop   test; estimate process   dead time, but more
Cohen-
step-response   gain, dead time, and time process-model oriented
Coon
data   constant; calculate PID   and less convenient for
gains from formulas   many robot joints
Q5   a. Suppose, F = {f1, f2, f3} and M = {m1, m2, m3} are two initially coincident fixed [10]
CO-   and mobile orthonormal coordinate frames, respectively.
2
1. Suppose we rotate mobile coordinate frame M along f1 axis of fixed coordinate
frame by π/2 rad
********** 11 **********
--- page 12 ---
2. Suppose we rotate mobile coordinate frame M from the origin about f2 axis of
fixed coordinate frame by -π rad.
a. Calculate the Resultant Matrix for both individual rotations
2
2
b. Solve for [q]M after each rotation given [q]F = [10 12 14]T in both cases.
Case 1
4
Case 2
c. Also draw vector diagrams.
Vector diagram for case 1:
2
• 𝑚1 stays along +𝑓1
• 𝑚2 moves to +𝑓3
• 𝑚3 moves to −𝑓2
Vector diagram for case 2:
• 𝑚1 moves to −𝑓1
• 𝑚2 stays along +𝑓2
• 𝑚3 moves to −𝑓3
CO-   b. Explain in detail with schematic how robotic part inspection using a vision system is [10]
4   carried out in a robotic work cell.
Robotic part inspection with a vision system in a work cell is carried out by first
imaging the part, extracting its position, orientation, and quality features, and then
********** 12 **********
--- page 13 ---
using that information to command the robot to accept, reject, or reorient the part. In
a typical single-robot cell, a part is placed in the viewing area of an overhead camera,   2
the vision system inspects it, and the robot controller sends the part to a pass bin or a
reject bin based on the inspection result.
Cell layout
A common arrangement is a feeder or conveyor, an inspection zone under an overhead
camera with controlled lighting, a robot arm with gripper, and separate pass and reject
bins. The camera observes the part, the vision processor determines the part pose and
condition, and the robot uses that result to plan a pick-and-place motion.
Inspection sequence
The process usually follows a fixed sequence: image acquisition, preprocessing,
feature extraction, identification, defect detection, decision-making, and robotic
handling. The document on the robotic work cell explicitly lists these stages and notes
that proper lighting and either fixed or robot-mounted cameras are used to improve
inspection quality.
The main steps are:
• Image acquisition: the camera captures the part image, often with LED,
infrared, or structured lighting to improve contrast and reduce shadows.
• Image preprocessing: the image is cleaned and enhanced using grayscale
conversion, contrast adjustment, thresholding, and edge detection so important   6
boundaries and defects are easier to isolate.
•   Feature extraction: the system measures features such as shape, size, texture,
and sometimes color.
•   Identification and classification: the extracted features are compared with a
reference model using methods such as template matching, OCR, or trained
classifiers.
• Defect detection: the system checks for faults such as cracks, dents, scratches,
missing components, or wrong dimensions.
• Decision and action: the robot either accepts the part, rejects it, or reorients it
for downstream handling.
Coordinate conversion   2
A key part of the work cell is converting what the camera sees into robot coordinates,
because the camera measures the part pose in the camera frame while the robot moves
in its base frame. This is done with homogeneous transformation matrices so the part
pose relative to the robot base can be computed from the camera-to-part and camera-
to-base   transformations.Fundamentals-of-Robotics_-Analysis-and-Control-
PDFDrive.com.pdf+1
In the worked example, the system uses
𝑇𝑏𝑎𝑠𝑒 𝑝𝑎𝑟𝑡= (𝑇𝑐𝑎𝑚𝑒𝑟𝑎 𝑏𝑎𝑠𝑒 )−1𝑇𝑐𝑎𝑚𝑒𝑟𝑎 𝑝𝑎𝑟𝑡
Q6   a. Analyze the four axis SCARA Adept One Robotic Arm and compute the following.   [20]
CO-
3
********** 13 **********
--- page 14 ---
i. Link coordinate diagram
8
ii. Link coordinate table.
Axis 𝑘   𝜃𝑘   𝑑𝑘   𝑎𝑘   𝛼𝑘   Joint type
4
1   𝑞1   𝑑1   𝑎1   0   Revolute
2   𝑞2   0   𝑎2   𝜋   Revolute
3   0   𝑑3   0   0   Prismatic
4   𝑞4   𝑑4   0   0   Revolute
iii. Individual Link coordinate transformation matrices.
Using the standard D-H adjacent-link transform
********** 14 **********
--- page 15 ---
2*4
Q7   a. Analyze the ARM matrix for a 3-axis PARA robot:   [20]
CO-   𝐶123 −𝑆123 0 𝑎1𝐶1 + 𝑎2𝐶12
4   𝑆123   𝐶123 0 𝑎1𝑆1 + 𝑎2𝑆12
[   ]
0   0   1   𝑑3
0   0   0   1
i.   Extract the Tool Configuration Vector (TCV)
For the planar robot shown in your image, the arm matrix is
𝐶123 −𝑆123 0 𝑎1𝐶1 + 𝑎2𝐶12
𝑇= [ 𝑆123   𝐶123   0 𝑎1𝑆1 + 𝑎2𝑆12 ]
0   0   1   𝑑3
0   0   0   1
where 𝐶12 = cos (𝑞1 + 𝑞2), 𝑆12 = sin (𝑞1 + 𝑞2), and 𝐶123, 𝑆123 describe the planar
tool orientation. The attached note extracts the tool-configuration vector as
𝑎1𝐶1 + 𝑎2𝐶12
𝑎1𝑆1 + 𝑎2𝑆12
𝑑3
𝑤(𝑞) =
0
0
[ exp (𝑞3/𝜋) ]
5
So the six scalar TCV equations are:
• 𝑤1 = 𝑎1𝐶1 + 𝑎2𝐶12
• 𝑤2 = 𝑎1𝑆1 + 𝑎2𝑆12
• 𝑤3 = 𝑑3
• 𝑤4 = 0
• 𝑤5 = 0
• 𝑤6 = exp (𝑞3/𝜋)
ii.   Derive the complete inverse kinematic equations for q1, q2, q3
To isolate the second joint, square and add 𝑤1 and 𝑤2, which eliminates 𝑞1 and
yields
𝑤1 2 + 𝑤2 2 = 𝑎1 2 + 2𝑎1𝑎2cos 𝑞2 + 𝑎2 2
********** 15 **********
--- page 16 ---
. Therefore,   6
2 + 𝑤2 2 −𝑎1 2 −𝑎2 2
𝑞2 = ±arccos (𝑤1   )
2𝑎1𝑎2
which gives the two standard planar-arm configurations, often called left-handed and
right-handed solutions.
With 𝑞2 known, rewrite the first two TCV equations as
𝑤1 = (𝑎1 + 𝑎2𝐶2)𝐶1 −(𝑎2𝑆2)𝑆1
and
𝑤2 = (𝑎2𝑆2)𝐶1 + (𝑎1 + 𝑎2𝐶2)𝑆1
6
Solving these for 𝑞1 gives
𝑞1 = atan2 ((𝑎1 + 𝑎2𝐶2)𝑤2 −(𝑎2𝑆2)𝑤1,  (𝑎1 + 𝑎2𝐶2)𝑤1 + (𝑎2𝑆2)𝑤2)
Third joint
The third joint follows directly from the last component of the tool-configuration
vector because 𝑤6 = exp (𝑞3/𝜋). Taking the natural logarithm gives   3
𝑞3 = 𝜋ln (𝑤6)
********** 16 **********
````
