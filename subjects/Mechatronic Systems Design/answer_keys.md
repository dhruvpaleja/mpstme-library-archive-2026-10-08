# Mechatronic Systems Design: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper ccb4b5f30754

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_Mechatronics_7004/Mechatronic Systems Design/ANS_Mechatronic Systems Design(702MH0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: Mechatronic Systems Design
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1.
a) Explanation about Model- based monitoring system. - 03 M
Diagram of Model based monitoring system. - 02 M
Model-based monitoring systems generally use a set of modelling equations and an estimation
algorithm (such as a state observer) to estimate the signal important to the machine performance.
In model-based monitoring, the purpose of the model is to represent the behaviour of the structure
also sensed externally and recorded. Local sensors provide an output signal related to the
measurement. The difference between the model output and the actual process output signals
provides a concise mechanism for incorporating diagnostics, which is an attractive alternative to
empirical rule-based decision systems.
Figure shows how the controller applies commands to the process such that various sensed values
are maintained (or regulated) at desired values. Remote sensors may sense some of the diagnostic
signals in difficult-to-access locations. In some cases, estimation algorithms are used based on the
system
structure and the signal of interest. Modeling procedures (some based on the previous knowledge)
are used to produce simple, accurate models to improve estimation accuracy.
********** 1 **********
--- page 2 ---
b) Explanation about constructional features and operation of a CISS sensor. - 05 M
The CISS (Connected Industrial Sensor Solution) is an advanced multi-sensor device designed for
industrial and IoT applications. It integrates several sensing elements into a single compact unit to
monitor multiple physical parameters such as acceleration, vibration, temperature, humidity,
magnetic field, and orientation. The sensor’s construction includes a sensor module, a
microcontroller unit (MCU), a communication interface, and a power supply, all enclosed within
a rugged and compact housing suitable for harsh industrial environments. The sensor module
consists of MEMS-based sensors that detect changes in physical quantities. The MCU acts as the
processing core, collecting signals from the sensors, filtering out noise, and processing data for
meaningful output. The communication interface allows the processed data to be transmitted to
external systems through wired or wireless connections such as Bluetooth or serial communication
(USB). The power supply provides stable operation, often powered by bus or a small battery.
In operation, the CISS sensor continuously monitors environmental and machine parameters. Each
sensing element measures specific variables, and the MCU interprets these signals to generate
reliable data. This data is then communicated to control systems, data loggers, or cloud-based
platforms for analysis. Through this process, the CISS sensor enables effective condition
monitoring, predictive maintenance, and process optimization in industrial settings. Its robust
design, multi-sensing capability, and smart data handling make it a vital component in modern
mechatronic and industrial automation systems.
c) Comparison between permanent magnet DC motor and permanent magnet stepper motor
based on constructional features, working, control strategies, applications, advantages,
limitations etc. (Any 5 Points)- 05 M.
d) Explanation about operation and applications of a time proportioning controller. – 05 M
In time proportioning controller (TPC) the output of the controller is continually switched on and
off. This method is also called PWM (Pulse Width Modulation). Here the ratio of On time (Ton)
to Total time (Ton+ Toff) called as duty cycle is varied as per the changes in the feedback signal.
In this On versus off times are varied dependent upon process requirements.
Applications of time proportioning controllers include motor speed control, temperature control in
ovens, furnaces, water heaters, level control in tanks, and other thermal or mechanical processes
where the process response is slower than the controller switching time. It is widely used in
industrial systems due to its simplicity, cost-effectiveness, and reliability for on/off type actuators.
Time proportioning controller is used for the speed control of a DC motor by rapidly switching the
motor’s supply voltage ON and OFF for a proportion of each fixed control cycle. The controller
continuously compares the actual speed of the motor, measured through a tachogenerator or
encoder, with the desired setpoint speed. Based on the difference, it determines the duty cycle, i.e.,
the fraction of time the motor receives full voltage within the cycle. For example, if the motor is
running slower than the setpoint, the TPC increases the ON-time to accelerate the motor; if it is
faster, the ON-time is reduced to slow it down. By adjusting the proportion of ON and OFF times,
the TPC effectively maintains the motor speed at the desired value without the need for complex
analog control.
Q2.
a) Justification of the statement, “Mechatronics is the result of applying information system to
physical system.” - 03 M
Mechatronic system consist of a physical system made up of mechanical, electrical, and computer
systems as well as actuators, sensors, and real-time interfacing. Mechatronics is really nothing but
good design practice in which information system is applied to physical systems. The basic idea
is to apply new controls to extract new levels of performance from a mechanical device. Sensors
and actuators are used to transduce energy from high power, usually the mechanical side to low
power, the electrical and computer side. The mechatronic system design follows concurrent design
********** 2 **********
--- page 3 ---
approach and results in far better accuracy than the electromechanical systems. Also, automatic
control is one of the key elements in a mechatronic system, so it is also higher than just a control
system.
Diagram of key constituent elements used in mechatronic system. - 03 M
Explanation of each constituent elements in mechatronic system. - 04 M
b) Diagram of Capacitive fingerprint scanner. - 03 M
Explanation of its working. - 04 M
Comparison of capacitive fingerprint scanner with optical fingerprint scanner. - 03 M
Like optical scanners, capacitive fingerprint scanners generate an image of the ridges and valleys
that make up a fingerprint. But instead of sensing the print using light, the capacitors use electrical
current. The diagram shows a simple capacitive sensor. The sensor is made up of one or more
semiconductor chips containing an array of tiny cells. Each cell includes two conductor plates,
covered with an insulating layer. The cells are tiny and smaller than the width of one ridge on a
finger. The sensor is connected to an integrator, an electrical circuit built around an inverting
operational amplifier. The two conductor plates form a basic capacitor. The surface of the finger
acts as a third capacitor plate, separated by the insulating layers in the cell structure and, in the
case of the fingerprint valleys, a pocket of air. Varying the distance between the capacitor plates
(by moving the finger closer or farther away from the conducting plates) changes the total
capacitance (ability to store charge) of the capacitor. Because of this quality, the capacitor in a cell
under a ridge will have a greater capacitance than the capacitor in a cell under a valley. To scan
the finger, the processor first closes the reset switch for each cell, which shorts each amplifier's
input and output to balance the integrator circuit. When the switch is opened again, and the
processor applies a fixed charge to the integrator circuit, the capacitors charge up. The capacitance
of the feedback loop's capacitor affects the voltage at the amplifier's input, which affects the
amplifier's output. Since the distance to the finger alters capacitance, a finger ridge will result in a
different voltage output than a finger valley. The scanner processor reads this voltage output and
determines whether it is characteristic of a ridge or a valley. By reading every cell in the sensor
array, the processor can put together an overall picture of the fingerprint, similar to the image
captured by an optical scanner.
********** 3 **********
--- page 4 ---
Like optical scanners, capacitive fingerprint scanners generate an image of the ridges and valleys
that make up a fingerprint. But instead of sensing the print using light, the capacitors use electrical
current.
The main advantage of a capacitive scanner over the optical scanner is that it requires a real
fingerprint type shape, rather than the pattern of light and dark that makes up the visual impression
of a fingerprint.   This makes the system harder to trick. Additionally, since they use a
semiconductor chip rather than a CCD unit, capacitive scanners tend to be more compact than
optical devices.
Q3.
a) Flow chart of steps involved in design of mechatronic system. - 05 M
Explanation with reference to the sequence of steps. - 05 M
The mechatronic design process consists of three phases: modeling and simulation, prototyping,
and deployment. All modeling, whether based on first principles or the more detailed physics,
should be modular in structure. A first principle model is a simple model which captures some of
the fundamental behaviour of a subsystem. A detailed model is an extension of the first principle
model providing more function and accuracy than the first level model. Connecting the modules or
blocks together may create complex models. Each block represents a subsystem, which corresponds
to some physically or functionally realizable operations, and can be encapsulated into a block with
input/output limited to input signals, parameters, and output signals. Of course, this limitation may
not always be possible or desirable; however, its use will produce modular subsystem blocks which
easily can be maintained, exercised independently, substituted for one another, and reused in other
applications. Because of their modularity, mechatronic systems are well suited for applications that
require reconfiguration. Such products can be reconfigured either during the design stage by
substituting various subsystem modules or during the life span of the product. Since many of the
steps in the mechatronic design process rely on computer-based tasks such as information fusion,
management, and design testing, an efficient computer-aided prototyping environment is essential.
The comprehensive development of mechatronic systems starts with modeling and simulation,
model building for static and dynamic models, transformation into simulation models,
programming and computer-based control, and final implementation. In this atmosphere, hardware
in the loop simulation plays a major part. Using visual simulation tools in a real-time environment,
********** 4 **********
--- page 5 ---
major portions of the mechatronic product could be simulated along with the hardware in the loop
simulation.
b) Development of the block diagram model for given system using a 3-step procedure
employing a free body diagram and equations of motion.
Free body diagram. -02 M
F1   FK2   FC2
M1   M2
FC1   FK1 FK2 FC2
Step 1: For both the masses in the illustration, writing the equation F= Ma, solving it for the
acceleration of the particular mass and developing the primary block diagram. - 02 M
********** 5 **********
--- page 6 ---
Step 2: For each of the two masses writing the force equation in terms of its components, the
input (external force), spring force, and damping force. - 02 M
Sum of Forces at Mass 1 = F1 − k1x1 − c1˙x1 - k2(x1−x2) - c2(˙x1−˙x2)
Sum of Forces at Mass 2 = k2(x1−x2) + c2(˙x1−˙x2)
Step 3: Implementing the step 2 equations on the primary diagram drawn in step 1 and
creating a final block diagram. - 04 M
Q4.
a) Development of the block diagram model for given transfer system using a 6-step procedure
by creating an intermediate variable.
Step 1: factoring out the leading coefficients of the Numerator(s) and Denominator(s) to
make them both monic polynomials. Creating the state variable, x(t), by sliding the
numerator part of the transfer function into a new block located to the right of the
denominator part of the transfer function. Connecting the denominator and numerator
blocks with an arrow and label the signal, x(t), the state variable. - 02 M
𝒀 (𝒔)   𝒔𝟐 −𝟑 𝒔+ 𝟒
𝑻(𝒔) =   =
𝑹 (𝒔)   𝒔𝟒 + 𝟐 𝒔𝟑 −𝟓 𝒔𝟐 + 𝟐 𝒔−𝟗
********** 6 **********
--- page 7 ---
Step 2: From step 1, writing the state equation (SE) as the differential equation relating the
input, r(t), to the state, x(t). - 01 M
𝒙 (𝒕)   𝟏
=
𝒓 (𝒕)   𝒔𝟒 + 𝟐 𝒔𝟑 −𝟓 𝒔𝟐 + 𝟐 𝒔−𝟗
Step 3: Constructing the primary block diagram by connecting 4 integrators in series as the
order of equation is four. - 01 M
Step 4: Solving the state equation of step 2 and extending the primary block diagram
implemented in step 3. - 03 M
Step 5 and 6: From step 1, writing the output equation as the differential equation relating
the output, y(t), to the state, x(t), and its derivatives and extending the block diagram.
Neglecting the initial conditions as mentioned in the problem. - 03 M
𝒚 (𝒕)
= 𝒔𝟐 −𝟑 𝒔+ 𝟒
𝒙 (𝒕)
********** 7 **********
--- page 8 ---
b) Block Diagram of Fuzzy logic-based controller. - 02 M
Explanation of the operation of the fuzzy logic controller for a specific application like
temperature control or automatic washing machine. - 08 M
Fuzzy logic is an approach for nonlinear mapping of one set of variables into another set of
variables.
Principle of operation of the fuzzy controller significantly differs from neural networks. The block
diagram of a fuzzy controller is shown in Figure. In the first step, analog inputs are converted into
a set of fuzzy variables. In this step, for each analog input, 3–9 fuzzy variables typically are
generated. Each fuzzy variable has an analog value between zero and one. In the next step, a fuzzy
logic is applied to the input fuzzy variables and a resulting set of output variables is generated. In
the last step, known as defuzzification, from a set of output fuzzy variables, one or more output
analog variables are generated, which are used as control variables.
Fuzzification: The purpose of fuzzification is to convert an analog variable input into a set of fuzzy
variables. For higher accuracy, more fuzzy variables will be chosen. To illustrate the fuzzification
process, consider that the input variable is the temperature and is coded into five fuzzy variables: cold,
cool, normal, warm, and hot as shown in following figure. Each fuzzy variable should obtain a value
between zero and one, which describes a degree of association of the analog input (temperature) within
the given fuzzy variable. Sometimes, instead of the term degree of association, the term degree of
membership is used.
Rule Evaluation: In contrary to Boolean logic where variables can have only binary states, in fuzzy
logic all variables may have any values between zero and one. The fuzzy logic consists of the same
basic:
********** 8 **********
--- page 9 ---
∧—AND ∨—OR, and NOT operators.
A ∧ B ∧ C ⇒ min {A, B, C}—smallest value of A or B or C
A ∨ B ∨ C ⇒ max {A, B, C}—largest value of A or B or C
A ⇒ 1–A—one minus value of A
Fuzzy rules are specified in the fuzzy table as it is shown below for the considered example.
Defuzzification: As a result of fuzzy rule evaluation, each analog output variable is represented by
several fuzzy variables. The purpose of defuzzification is to obtain analog outputs. This can be done
by using a membership function. In the first step, fuzzy variables obtained from rule evaluations are
used to modify the membership function employing the formula-
µK∗ (z) = min {µK (z), zK}
For example, if the output fuzzy variables are 0, 0.2, 0.7, 0.0, then the modified membership functions
have shapes shown by the thick line in the figure below. The analog value of the z variable is found as
a center of gravity of modified membership function µK∗ (z).
********** 9 **********
--- page 10 ---
Q5.
a) Structural diagram of the smart sensor. - 04 M
Explanation of the smart sensor structure and working. - 06 M
b) Design of a parallel electronic PID controller using OP-Amps. - 05 M
********** 10 **********
--- page 11 ---
Description of its operation using equation and characteristics. - 05 M
One of the most powerful but complex controller mode operations combines the proportional,
integral and derivative modes. The system can be used for virtually any process condition.
The analytical expression for this controller along with the characteristics is given below.
This mode eliminates the offset of the proportional mode and still provides fast response.
P= KpEp + Ki ∫𝑬𝒑 𝒕   𝒅𝒕 + 𝑲𝒅 𝒅𝑬𝒑 𝒅𝒕+ 𝑷𝒊 (𝟎)
𝟎
Q6.
a) Development of block diagram model for the three-tank fluid system using 4 step procedure
of modified analogy approach.
Step 1: Creating and simplifying the impedance diagram. - 02 M
Step 2: Identifying all independent flow variable (FV) and potential variable (PV) nodes in
the impedance diagram and labelling all signals. - 02 M
********** 11 **********
--- page 12 ---
Step 3: Representing select nodes as a summing junction and selecting the output of the
summing junction such that when it is connected to its associated impedance blocks either
gain or integral causality results. - 02 M
Causality is only an issue with the tank impedances, because for these elements, the input must be
a flow variable (volume flow rate) for integral causality. This means that the three summing
junctions used for the three FV node equations must have q10, q20, and q30 as outputs.
Step 4: Adding the impedance blocks, connecting, and creating all necessary intermediate
and output signals to complete the block diagram. - 04 M
b) Constructional diagram of a brushless DC motor. - 03 M
Explanation of its working. - 04 M
Description of applications of brushless DC motor in mechatronic systems. – 03 M
These motors have position feedback of some kind so that the input waveforms can be kept in the
proper timing with respect to the rotor position. Solid-state switching devices are used to control
the input signals, and the brushless dc motor can be operated at much higher speeds with full torque
available at those speeds. The brushless motor can normally be rapidly accelerated from zero to
operating speed as a PM motor. On reaching operating speed, the motor can then be switched over
to synchronous operation.
The brushless motor system consists of a wound stator, a permanent magnet rotor, a rotor position
sensor, and a solid-state switching assembly. The wound stator can be made with two or more
input phases. Figure below gives the schematic representation of a two-phase brushless motor.
The brushless dc motor will duplicate the performance characteristics of a conventional dc motor
only if it is properly commutated. Proper commutation involves exciting the stator windings in a
sequence that keeps the magnetic field produced by the stator approximately 90 electrical degrees
ahead of the rotor field. The brushless dc motor therefore relies heavily on the position feedback
system for effective commutation. It might also be apparent that the brushless motor as described
is not strictly a dc machine, but a form of ac machine with position feedback.
********** 12 **********
--- page 13 ---
Brushless DC (BLDC) motors are extensively used in mechatronic systems because of their high
efficiency, precise speed control, low maintenance, and compact design. They are ideal for
applications that require accurate motion control and reliable performance over long periods. In
robotics, BLDC motors enable precise positioning and smooth movement of robotic arms and
mobile robots. In CNC machines, they drive spindles and actuators where controlled speed and
torque are essential. They are also used in drones and UAVs, providing high-speed rotation with
efficient power usage. In the medical field, BLDC motors are employed in surgical tools and
imaging equipment for accurate, quiet, and dependable operation. Additionally, in automotive
systems, they are used in electric power steering, cooling fans, and pumps in modern vehicles.
Overall, BLDC motors are preferred in mechatronic systems wherever precision, efficiency, and
reliability are crucial.
Q7.
a) Comparison between hardware in the loop simulation and computer-based simulation. -05
Computer-based simulation takes place in a virtual environment with virtual inputs producing
virtual outputs. It is required to check authenticity of the primary model developed for the
mechatronic system. It does not require connection with the real world through additional data
acquisition hardware.
In the prototyping step of mechatronic system design, many of the non-computer subsystems of
the model are replaced with actual hardware. Sensors and actuators provide the interface signals
necessary to connect the hardware subsystems back to the model. The resulting model is part
mathematical and part real. Because the real part of the model inherently evolves in real time and
the mathematical part evolves in simulated time, it is essential that the two parts be synchronized.
The process of fusing and synchronizing model, sensor, and actuator information is called real
time interfacing or hardware-in-the-loop simulation.
b) Explanation of different Components of Pneumatic actuation system. - 03 M
Diagram of Pneumatic actuation system. – 02 M
The components of a pneumatic actuation system are:
• The compressed air generation system, consisting of the compressor, the cooler, possibly a
dryer, the storage tank, and the intake and output filters.
• The compressed air treatment unit, usually consisting of the FRL assembly (filter, pressure
regulator, and possibly a purifier), which permits filtration and local regulation of the
supply pressure to the actuator valve.
• The valve, that is, the regulator of pneumatic power.
• The actuator, which converts the pneumatic power into mechanical power.
• The piping which transmits the pneumatic power.
• The sensors and transducers.
• The system display, physical magnitude measurement, and control devices.
********** 13 **********
--- page 14 ---
c) Explanation about frequency response method used for controller tuning. – 05 M
This method involves use of Bode Plot for the process and control loops.
The method is based on the application of the Bode plot stability criterion and the effects that the
proportional gain, integral time and derivative time have on the Bode plot.
Bode plot stability criterion is as follows:
•   If the phase is less than 140 degrees at the unity gain frequency the system is stable. This
then is 40 degrees phase margin from the limiting value of 180 degrees .
•   If the gain is 5 dB below unity when the phase lag is 180 degrees, the system is stable.
This is then 5 dB gain margin.
The operations of tuning using frequency response method involve adjustments of the controller
parameters until the stability is proved by the appropriate phase and gain margins.
Proportional Action : Multiplies gain curve by a constant and no effect on phase.
Integral Action : Integral gain= Ki/ω and Integral phase = - 90 degrees (lag).
Derivative Action : Derivative gain = Kd*ω and Derivative phase= 90 degrees (lead).
d) Discussion about principle, materials and working of a magnetostrictive actuators. - 05 M
Magnetostrictive actuators have emerged as a promising technology in the field of precision
motion control and actuation. These actuators exploit the magnetostrictive effect, a phenomenon
in which certain ferromagnetic materials change shape when subjected to a magnetic field. The
resulting motion can be harnessed for a wide variety of applications, from aerospace to biomedical
engineering.
Magnetostriction occurs in certain ferromagnetic materials due to the interaction between their
atomic magnetic moments and the external magnetic field. When a magnetic field is applied, the
material’s atomic magnetic moments align with the field, causing a change in the material’s
dimensions. This change is known as the magnetostrictive strain, and it can be either positive
(elongation) or negative (contraction). The most commonly used magnetostrictive materials
include Terfenol-D, Metglas, and Galfenol. Terfenol-D, an alloy of terbium, dysprosium, and iron,
exhibits the largest magnetostrictive strain among commercially available materials. Galfenol, an
iron-gallium alloy, offers excellent mechanical robustness, while Metglas, a metallic glass, is
known for its rapid response to magnetic fields.
A typical magnetostrictive actuator comprises three main components: the magnetostrictive
material, a coil, and a mechanical assembly for transmitting motion. The coil generates a magnetic
field when current flows through it, causing the magnetostrictive material to change shape. The
mechanical assembly then transforms this shape change into useful motion, such as linear or rotary
motion.
Magnetostrictive actuators can be designed in various configurations, depending on the specific
application requirements. For example, a linear magnetostrictive actuator may use a rod-shaped
magnetostrictive material, while a rotary actuator may incorporate a ring-shaped material.
********** 14 **********
--- page 15 ---
Additionally, the actuator’s performance can be tuned by adjusting factors such as the coil’s
geometry, the magnetostrictive material’s dimensions, and the mechanical assembly’s design.
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 51f38e4e8843

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_Mechatronics_7004/Mechatronic Systems Design/ANS_Mechatronic Systems Design(702MH0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: Mechatronic Systems Design
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1.
a) Architectural diagram of an intelligent supervisory control system. - 02 M
Explanation about its configuration and working. – 03 M
Figure shows a framework for an intelligent supervisory control system which integrates
heterogeneous systems, involving the position and velocity control of a machine tool, local
inspection of a process, global inspection of the overall process, and finally, classification.
A hierarchical control structure where the controller elects position and velocity at the machine
level, force and wear at the process level, and quality control issues (like dimension and roughness)
at the product level.
The lowest level is servo control, where the motion of the cutting tool relative to the workpiece
(such as its position and velocity) is controlled. This involves cycle times of approximately 1
millisecond.
At the process control level, process variables (such as cutting forces and tool wear) are controlled
with typical cycle times of around 10 milliseconds. Control level strategies are aimed at
compensating for factors not explicitly considered in the design of the servo and process level
controllers.
********** 1 **********
--- page 2 ---
The highest level is the supervisory level, which directly measures product-related variables (such
as part dimension and surface roughness). The supervisory level also performs functions such as
chatter detection and tool monitoring. The supervisory level operates at cycle times of
approximately 1 second. Finally, all of this information can be used to achieve online optimization
of the machining process at the shop floor and plant control level.
b) Discussion about various characteristics and specifications of a CISS sensor like parameters
measured, voltage rating, communication protocols used, ranges, accuracy, applications and
tolerances. – 05 M
A CISS (Connected Industrial Sensor Solution) is a compact, multi-functional device designed to
monitor and transmit various physical and environmental parameters in industrial and mechatronic
systems. It integrates multiple sensors within a single unit, including temperature, humidity,
vibration, acceleration, magnetic field, and light sensors, making it ideal for Industry 4.0 and IoT-
based applications. The CISS continuously collects data from equipment or surroundings and
communicates it wirelessly via Bluetooth or through serial communication (USB) to a central
control or cloud platform for analysis and monitoring.
The measurement ranges of key parameters typically include temperature from –20°C to +80°C,
humidity from 10% to 100% rH, vibration up to 16 g, acceleration within ±2 g to ±16 g (14 bit
resolution), magnetic field in the range of ±1300 µT, Gyroscope ±2000 o/s, Pressure from 300 to
1100 hPa and illumination up to 2112800 lux. These ranges enable the CISS to effectively detect
variations in operating conditions, supporting predictive maintenance, machine health monitoring,
and process optimization.
The important characteristics of a CISS include multi-sensor integration, high accuracy, compact
size, low power consumption, and real-time communication. It can process data locally using an
embedded microcontroller and transmit actionable insights to supervisory systems. Owing to its
versatility and reliability, the CISS is widely used in industrial automation, robotics, logistics, and
structural health monitoring, playing a crucial role in advancing smart manufacturing and
mechatronic system intelligence.
c) Comparison between Hydraulic and Pneumatic actuation systems based on energy carrier,
components used, power density, parameters, efficiency, linear movements, path accuracy,
controlling techniques, advantages, limitations and applications. (Any 5 points) - 05 M
********** 2 **********
--- page 3 ---
d) Explanation about configuration, operation and applications of an ON-OFF controller. – 05
ON-OFF Controller is Used for slow acting operations where lag is unavoidable. Final correcting
element is either fully-on or fully-off. The primary drawback of on-off control is the rapid
switching of the final control element. On-off differential or hysteresis is programmed into the
controller to reduce cycling. Dead band refers to the differing level at which a controller switches
on and off.
The analytical equation for On-Off controller is given as
P= 0 %   Ep < 0
P= 100 % Ep > 0
Applications of On-Off controller: It is best adapted to large scale systems with relatively slow
process rates. Examples of such process are
• Room heating or air conditioning system
• Liquid bath temperature control
• Level control in large volume tanks
Q2.
a) Discussion about the integrated design issues in mechatronic systems. -- 03 M
Diagram for the scheme of hardware and software integration used in mechatronic system
design. -- 03 M
Explanation of the integration scheme. - 04 M
The inherent concurrency or simultaneous engineering of the mechatronic systems relies heavily
on the use of system modeling and simulation throughout the design and prototyping stages.
Because the model will be used and altered by engineers from multiple disciplines, it is especially
important that it be programmed in a visually intuitive environment. Such environments include
block diagrams, flow charts, state transition diagrams, and bond graphs.
In contrast to the more conventional programming languages such as Fortran, Visual Basic, C, and
Pascal, the visual modeling environment requires little training due to its inherent intuitiveness.
Today, the most widely used visual programming environment is the block diagram. This
environment is extremely versatile, low in cost, and often includes a code generator option, which
translates the block diagram into a C (or similar) high-level language suitable for target system
implementation.
Block diagram-based modeling and simulation packages are offered by many vendors, including
MATRIXx, Easy5, Simulink, Agilent VEE, DASYLab, VisSim and LabVIEW.
Mechatronics is a design philosophy: an integrating approach to engineering design.
An important characteristic of mechatronic devices and systems is their built-in intelligence that
results through a combination of precision in mechanical and electrical engineering, and real-time
programming integrated into the design process. Mechatronics uses the control systems to provide
a coherent framework of component interactions for system analysis.
The integration within a mechatronic system is performed through the combination of hardware
(components) and software (information processing).
Hardware integration results from designing the mechatronic system as an overall system and
bringing together the sensors, actuators, and microcomputers into the mechanical system.
Software integration is primarily based on advanced control functions.
Figure below illustrates how the hardware and software integration take place.
It also shows how an additional contribution of the process knowledge and information processing
is involved besides the feedback process.
********** 3 **********
--- page 4 ---
b) Explanation about the operation of a retina scanner. – 07 M
Comparison between retina scanner and iris scanner. – 03 M
Developed in the 1980s, retinal scanning is one of the most well-known biometric technologies,
but it is also one of the least deployed. Retinal scans map the unique patterns of a person’s retina.
The blood vessels within the retina absorb light more readily than the surrounding tissue and are
easily identified with appropriate lighting. A retinal scan is performed by casting an unperceived
beam of low-energy infrared light into a person’s eye as they look through the scanner’s eyepiece.
This beam of light traces a standardized path on the retina. Once the scanner device captures a
retinal image, specialized software compiles the unique features of the network of retinal blood
vessels into a template. Retinal scan algorithms require a high-quality image and will not let a user
enroll or verify until the system is able to capture an image of sufficient quality. The retina template
generated is typically one of the smallest of any biometric technology. Retinal scan is a highly
dependable technology because it is highly accurate and difficult to spoof, in terms of
identification. Technology, however, has notable disadvantages including difficult image
acquisition and limited user applications. Often enrollment in a retinal scan biometric system is
lengthy due to requirement of multiple image capture, which can cause user discomfort. However,
once user is acclimated to the process, an enrolled person can be identified with a retinal scan
process in seconds. Retinal scan technology has robust matching capabilities and is typically
configured to do one-to-many identification against a database of users. However, because quality
image acquisition is so difficult, many attempts are often required to get to the point where a match
can take place. While the algorithms themselves are robust, it can be a difficult process to provide
sufficient data for matching to take place. In many cases, a user may be falsely rejected because
of an inability to provide adequate data to generate a match template. Because retinal blood vessels
are more absorbent of log-energy infrared light than the rest of the eye, the amount of reflection
varies during the scan. The pattern of variations is converted to computer code and stored in a
database.
Retinal scans should therefore not be confused with another ocular-based technology, iris
recognition, which is described as the process of recognizing a person by analyzing the random
pattern of the iris.
The retina’s intricate network of blood vessels is a physiological characteristic that remains stable
throughout the life of a person. As with fingerprints and iris patterns, genetic factors do not
determine the exact pattern of blood vessels in the retina. This allows retinal scan technology to
differentiate between identical twins and provide robust identification. The retina contains at least
as much individual data as a fingerprint, but, unlike a fingerprint, is an internal organ and is less
susceptible to either intentional or unintentional modification. Certain eye-related medical
********** 4 **********
--- page 5 ---
conditions and diseases, such as cataracts and glaucoma, can render a person unable to use retina-
scan technology, as the blood vessels can be obscured.
Q3.
a) Justification of the statement, “Mechatronics is a methodology used for the optimal design
of electromechanical products.” - 03 M
The branch of engineering called systems engineering uses a concurrent approach for preliminary
design. In a way, mechatronics is an extension of the system engineering approach, but it is
supplemented with information systems to guide the design and is applied at all stages of design
not just to the preliminary design step thus making it more comprehensive. There is a synergy in
the integration of mechanical, electrical, and computer systems with information systems for the
design and manufacture of products and processes. The synergy is generated by the right
combination of parameters; the final product can be better than just the sum of its parts. Therefore,
mechatronic products exhibit optimal performance characteristics that were previously difficult to
achieve without the synergistic combination.
Flow chart of steps involved in mechatronic design process. - 04 M
Explanation of mechatronic design process. - 03 M
The mechatronic design process consists of three phases: modeling and simulation, prototyping,
and deployment. All modeling, whether based on first principles or the more detailed physics,
should be modular in structure. A first principle model is a simple model which captures some of
the fundamental behaviour of a subsystem. A detailed model is an extension of the first principle
model providing more function and accuracy than the first level model. Connecting the modules or
blocks together may create complex models. Each block represents a subsystem, which corresponds
to some physically or functionally realizable operations, and can be encapsulated into a block with
input/output limited to input signals, parameters, and output signals. Of course, this limitation may
not always be possible or desirable; however, its use will produce modular subsystem blocks which
easily can be maintained, exercised independently, substituted for one another, and reused in other
applications. Because of their modularity, mechatronic systems are well suited for applications that
require reconfiguration. Such products can be reconfigured either during the design stage by
substituting various subsystem modules or during the life span of the product. Since many of the
steps in the mechatronic design process rely on computer-based tasks such as information fusion,
management, and design testing, an efficient computer-aided prototyping environment is essential.
The comprehensive development of mechatronic systems starts with modeling and simulation,
model building for static and dynamic models, transformation into simulation models,
programming and computer-based control, and final implementation. In this atmosphere, hardware
in the loop simulation plays a major part. Using visual simulation tools in a real-time environment,
major portions of the mechatronic product could be simulated along with the hardware in the loop
simulation.
********** 5 **********
--- page 6 ---
b) Development of the block diagram model for given transfer system using a 6-step procedure
by creating an intermediate variable.
Step 1: factoring out the leading coefficients of the Numerator(s) and Denominator(s) to
make them both monic polynomials. Creating the state variable, x(t), by sliding the
numerator part of the transfer function into a new block located to the right of the
denominator part of the transfer function. Connecting the denominator and numerator
blocks with an arrow and label the signal, x(t), the state variable. - 02 M
𝒀 (𝒔)   𝟎. 𝟔
𝑻(𝒔) =   =
𝑹 (𝒔)   𝒔𝟐 + 𝟏. 𝟔 𝒔+ 𝟐.𝟔
Step 2: From step 1, writing the state equation (SE) as the differential equation relating the
input, r(t), to the state, x(t). - 01 M
𝒙 (𝒕)   𝟏
=
𝒓 (𝒕)   𝒔𝟐 + 𝟏.𝟔 𝒔+ 𝟐. 𝟔
Step 3: Constructing the primary block diagram by connecting 2 integrators in series as the
order of equation is two. - 01 M
********** 6 **********
--- page 7 ---
Step 4: Solving the state equation of step 2 and extending the primary block diagram
implemented in step 3. - 02 M
Step 5: From step 1, writing the output equation as the differential equation relating the
output, y(t), to the state, x(t), and its derivatives and extending the block diagram. - 02 M
0.6x(t) = y(t)
Step 6: Adding the initial conditions to the block diagram in step 5 by finding the values of
state variable, x(t) and its derivatives. - 02 M
0.6x(0) = y (0) = 3 therefore x (0) = 5 and value of first derivative of x (0) = -5
********** 7 **********
--- page 8 ---
Q4.
a) Development of the block diagram model for given system using a 3-step procedure
employing a free body diagram and equations of motion.
Free body diagram. -02 M
F   FB
M1   M2
FK1 FB   FK2
Step 1: For both the masses in the illustration, writing the equation F= Ma, solving it for the
acceleration of the particular mass and developing the primary block diagram. - 02 M
Step 2: For each of the two masses writing the force equation in terms of its components, the
input (external force), spring force, and damping force. - 02 M
Sum of Forces at Mass 1 = F − k1x1 – B (˙x1−˙x2)
Sum of Forces at Mass 2 = B (˙x1−˙x2) - k2x2
Step 3: Implementing the step 2 equations on the primary diagram drawn in step 1 and
creating a final block diagram. - 04 M
********** 8 **********
--- page 9 ---
b) Constructional Diagram of the model predictive controller. - 04 M
Explanation of the operation of a model predictive controller considering a specific industrial
application. -- 06 M
Model predictive control (MPC) was developed in the 1970s and 1980s to meet control challenges of
refineries. Since then, it has become the most effective advanced control technique for a wide range
of industries. The advantages of MPC are most evident when it is used as a multivariable controller
integrated with an optimizer. The greatest MPC benefits are realized in applications with dead time
dominance, interactions, constraints, and the need for optimization. Model predictive control
considers the effect of past actions of manipulated and disturbance variables on the future profile of
controlled and constraint variables and computes a sequence of controller moves to achieve the desired
future profile of controlled variables.
The majority of MPC applications assume linear process models and apply linear programming (LP)
for optimization. The refining and petrochemical industries lead in MPC applications. MPC is also
widely used in other industries including pulp and paper, chemicals, cement, power, food processing,
automotive, metallurgy, and pharmaceuticals.
Figure shows an MPC controller for a process with two inputs and one output that allows one to see
the analogy to a typical feedback control loop. The process has a manipulated variable (MV) and a
disturbance variable (DV) on the input and a controlled variable (CV) on the output.
A simple MPC controller used in this configuration has three basic components:
A process model that predicts the process output in the future up to the prediction horizon (typically,
120 or more scans). A future trajectory of the set point for the same number of scans as the trajectory
of the predicted process output. A control algorithm for computing a control action based on the error
vector as the difference between the future trajectories of the set point and the predicted process output.
The controller output is an MV that is applied to the inputs of the process and the process model,
which is a part of every MPC controller. A measured load upset to the process input is also applied as
a DV to the model input. The process model computes a predicted trajectory of the CV that is the
process output.
After correction of this trajectory for any mismatch between the predicted and an actual measured
value of the controlled variable the predicted trajectory is subtracted from the future trajectory of the
set point to form an error vector as shown in following figure.It is then applied on the predictive
controller input.
The predictive control algorithm develops outputs to minimize the sum of squared errors over the
prediction horizon, taking into account several future MV moves in its calculations.
********** 9 **********
--- page 10 ---
Q5.
a) Flow chart of steps involved in designing a pattern recognition system. - 05 M
Explanation of the steps with relevant example. - 05 M
********** 10 **********
--- page 11 ---
b) Design of a non-interacting (ideal) electronic PID controller using OP-Amps. - 05 M
Description of its operation using equation and characteristics. - 05 M
One of the most powerful but complex controller mode operations combines the proportional,
integral and derivative modes. The system can be used for virtually any process condition.
The analytical expression for this controller along with the characteristics is given below.
This mode eliminates the offset of the proportional mode and still provides fast response.
P= KpEp + KpKi ∫𝑬𝒑 𝒕   𝒅𝒕 + 𝑲𝒑𝑲𝒅 𝒅𝑬𝒑 𝒅𝒕+ 𝑷𝒊 (𝟎)
𝟎
********** 11 **********
--- page 12 ---
Q6.
a) Comparison between the modified analogy approach and analogy approach of block diagram
modeling. – 03 M
The modified analogy approach is a process which allows you to convert an illustration of a
physical system to a block diagram model. The approach is based on the electrical notion of
impedance and a four-step conversion process.
The difference between the modified analogy approach and the basic analogy approach is the
manner in which nonlinearities are handled. The basic analogy approach is restricted to linear
applications. If a nonlinearity exists, it must be linearized prior to incorporating it into the model.
Linearization provides only an approximation to the behaviour of the nonlinearity, the difference
between the linearized and actual behaviour becomes an undesirable modeling error. The modified
approach removes this limitation by allowing the actual nonlinearity to be incorporated into the
model. This results in a more accurate model with better predictive capability and less modeling
error.
Development of block diagram model for the parallel resonant circuit using 4 step procedure
of modified analogy approach.
Step 1: Creating and simplifying the impedance diagram. - 02 M
Step 2: Identifying all independent flow variable (FV) and potential variable (PV) nodes in
the impedance diagram and labelling all signals. - 01 M
Step 3: Representing select nodes as a summing junction and selecting the output of the
summing junction such that when it is connected to its associated impedance blocks either
gain or integral causality results. - 01 M
********** 12 **********
--- page 13 ---
Step 4: Adding the impedance blocks, connecting, and creating all necessary intermediate
and output signals to complete the block diagram. - 03 M
b) Constructional Diagram of Variable Reluctance Stepper Motor. - 04 M
Explanation of its operation with reference to diagram. - 06 M
This type of stepper motor has a soft iron multi-toothed rotor with a wound stator. The number of
teeth on the rotor and stator, together with the winding configuration and excitation determines the
step angle. This type of stepper motor provides small to medium sized step angles and is capable
of operating at high stepping rates.
The principle of operation of a stepper motor can be illustrated with reference to a variable
reluctance, four-phase machine shown in figure. This motor usually has eight stator teeth and six
rotor teeth. If phase 1 of the stator is activated alone, two diametrically opposite rotor teeth align
themselves with the phase 1 teeth of the stator. The next adjacent set of rotor teeth in the clockwise
direction are then 15° out of step with those of the stator. Activation of the phase 2 winding on its
own, would cause the rotor to rotate a further 15° in the anti-clockwise direction to align the
adjacent pair of diametrically opposite rotor teeth. If the stator windings are excited in the sequence
1, 2, 3, 4, then the rotor will move in consecutive 15° steps in the anti-clockwise direction.
Reversing the excitation sequence will cause a clockwise rotation of the rotor
********** 13 **********
--- page 14 ---
Q7.
a) Comparison between the internal bus system and external bus system used for real time
interfacing in mechatronic applications. - 05 M
There are two types of real time interface systems: external and internal bus system.
An internal bus system is computer specific and consists of a board, or card, which plugs into
internal computer bus and an external screw terminal or termination, board connected to the
internal card via ribbon cable. Internal bus systems are popular because of their high speed, low
cost and small size.
External bus systems are computer independent and normally connected to the host computer
through its serial port, which is responsible for the relatively slow data rates, for example RS-232
is limited to 9600 baud. Often slower and more expensive external bus systems do most of their
processing independently of the host computer. Because they have their own microprocessor,
power supply, and memory, the host computer is relieved of much of the data acquisition and
control processing functions. External bus systems are well suited to remote and distributed
sensing and control applications. Using RS-422, distances between the host and the external bus
system can approach half a mile.
b) Short note on piezoelectric actuators. -- 05 M
Piezoelectric effect was discovered by brothers Curie in 1880. The direct piezoelectric effect
consists in ability of certain materials to generate electric charge in proportion to externally applied
force. The inverse piezoelectric effect of these materials consists in their expansion under the
action of electric field parallel to the direction of polarization. Effects are lasting if force or electric
field is acting. Effects have been used for actuating/sensing functions in engineering applications.
Materials that exhibit a significant and useful piezoelectric effect fall into three main groups:
natural (quartz, Rochelle salt) and synthetic crystals (lithium sulphate, ammonium dihydrogen
phosphate), polarized ferroelectric ceramics, and certain polymer films. The main piezomaterial
for engineering applications is ferroelectric ceramics, Lead Zirconate Titanate (PZT) especially.
The latter is characterized by high coupling factors, and piezoelectric and dielectric constants over
extended temperature and stress ranges. Barium titanate, lead magnesium niobate, modified lead
titanate, and bismuth titanate compounds are used as well as other special compositions. Because
of their natural asymmetric structure, crystal materials exhibit the effect without further processing.
However, ferroelectric ceramics must be artificially polarized by a strong electric field while the
material is heated above its Curie point and then slowly cooled with field applied. Remnant
polarization being retained, the material exhibits the piezoeffect. Piezopolymers like
polyvinylidene fluorides (PVDF or PVF2) are a special class of fluoropolymer that exhibit a high
degree of piezoelectric activity. They are used for manufacturing piezofilms of low thickness (less
than 30 μm), which may be laminated on the structural materials. Piezoactuating elements in a
wide range of sizes are produced as squares, rectangles, rings, discs, spheres, hemispheres, bars
and cylinders, and special elements. Typical thickness is from 20 μm to 15 mm and up to 100 mm
length or external diameter. Due to unique properties of the material, quick response, high stiffness,
low power consumption, and high electromechanical conversion efficiency they can be used
directly as actuators.
c) Explanation about Ziegler-Nichols continuous cycling method used for controller tuning. -
05 M
The Ziegler–Nichols Continuous Cycling Method is a classical and widely used technique for
tuning PID controllers based on the closed-loop response of a system. This method provides
empirical formulas for determining the controller parameters proportional gain (Kp), integral time
(Ti), and derivative time (Td) so as to achieve a desired dynamic response.
In this method, the integral and derivative actions of the PID controller are first turned off, leaving
only the proportional control active. The proportional gain (Kp) is gradually increased from a low
********** 14 **********
--- page 15 ---
value until the system output exhibits sustained oscillations of constant amplitude. The gain value
at this point is called the ultimate gain (Ku), and the corresponding oscillation period is known as
the ultimate period (Pu).
Once Ku and Pu are determined experimentally, the controller settings are calculated using the
Ziegler–Nichols tuning rules as shown below.
Proportional only controller: Kp = 0.5Ku
Proportional – Integral controller: Kp = 0.45Ku and Ti = Pu/1.2
Proportional – Integral - Derivative controller: Kp = 0.6Ku, Ti = Pu/2 and Td = Pu/8
d) Description of   various factors to be considered for choosing a solenoid actuator in
mechatronic systems. – 05 M
Force, stroke, temperature, and duty cycle are the four major parameters to be considered for
selection of solenoids. A linear solenoid can provide up to 30 lb of force from a unit less than 2.25
inches long. A rotary solenoid can provide well over 100 lb of torque from a unit also less than
2.25 inches long. Also, the relationship between force and stroke can be modified by changing the
design of some internal components. Higher performance, e.g., force output, can be achieved by
increasing the current to the coil winding. However, higher current tends to increase the winding
temperature. As the winding temperature increases, the wire resistance increases. This will reduce
the output force level. Solenoids are often rated as operating under continuous duty cycle or
intermittent duty cycle. A solenoid rated for 100% duty cycle may be energized at its rated voltage
continuously because its total coil temperature will not exceed maximum allowable ratings, while
an intermittent duty cycle solenoid has an associated allowable on time which must not be
exceeded. Intermittent duty coils provide considerably higher forces than continuous duty
solenoids. The maximum operating temperature for a solenoid is determined by the rated
temperature of the insulation material used in the winding.
********** 15 **********
````
