# Probabilistic Robotics — syllabus

3 syllabus section(s) for this course in the archive, newest batch first. Text comes from the PDF (OCR for scanned pages; check figures against the source). All programmes' syllabi: [`syllabi/`](../README.md).

## M Tech · Artificial Intelligence · batch 2020-2022 · Sem 3

- Course as printed: Probabilistic Robotics (code 703DB0E011)
- Source: `04_Syllabi_Archive/M Tech/Artificial Intelligence/Batch ( 2020 To 2022 )/Semester - 3.pdf`, page 12-15

````text
Program: M. Tech. – Artificial Intelligence   Semester :III
Course: Probabilistic Robotics   Module Code : 703DB0E011
Teaching Scheme   Evaluation Scheme
Internal
Lecture   Tutorial   Term End Examinations
Practical   Continuous
(Hours   (Hours   (TEE)
(Hours per   Credit   Assessment
per   per   (Marks -100   in
week)   (ICA)
week)   week)   Question Paper)
(Marks -50)
3   0   0   3   Marks Scaled to 50   Marks Scaled to 50
Pre-requisite: Probability/Python/Programming language/Robotics
Objectives:
1. Robotics is the science of perceiving and manipulating the physical world through
computer-controlled mechanical devices. Examples of successful robotic systems
include mobile platforms for planetary exploration, robotics arms in assembly lines,
cars that travel autonomously on highways, actuated arms that assist surgeons.
2. Robotics systems have in common that they are situated in the physical world, perceive
their environments through sensors, and manipulate their environment through things
that move.
Outcomes:
After completion of the course, students would be able to :
1. Environments. Physical worlds are inherently unpredictable. While the degree of
uncertainty in well-structured environments such assembly lines is small, environments
such as highways and private homes are highly dynamic and unpredictable.
2. Sensors. Sensors are inherently limited in what they can perceive. Limitations arise from
two primary factors. First, range and resolution of a sensor is subject to physical laws. For
example, Cameras can’t see through walls, and even within the perceptual range the
spatial resolution of camera images is limited. Second, sensors are subject to noise, which
perturbs sensor measurements in unpredictable ways and hence limits the information
that can be extracted from sensor measurements.
3. Robots. Robot actuation involves motors that are, at least to some extent, unpredictable,
due effects like control noise and wear-and-tear. Some actuators, such as heavy-duty
industrial robot arms, are quite accurate. Others, like low-cost mobile robots, can be
extremely inaccurate.
4. Models. Models are inherently inaccurate. Models are abstractions of the real world. As
such, they only partially model the underlying physical processes of the robot and its
Signature
(Prepared by Concerned Faculty/HOD)
M. Tech /AI/2021-22/SEM III /Page 12 of 16
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
environment. Model errors are a source of uncertainty that has largely been ignored in
robotics, despite the fact that most robotic models used in state-or-the-art robotics systems
are rather crude.
5. Computation. Robots are real-time systems, which limits the amount of computation that
can be carried out. Many state-of-the-art algorithms (such as most of the algorithms
described in this book) are approximate, achieving timely response through sacrificing
accuracy.
Detailed Syllabus: (per session plan)
Unit   Description   Duration
1   INTRODUCTION   3
2   RECURSIVE STATE ESTIMATION   3
3   GAUSSIAN FILTERS   3
4   NONPARAMETRIC FILTERS   3
5   ROBOT MOTION   3
6   MEASUREMENTS   3
7   MOBILE ROBOT LOCALIZATION   3
8   GRID AND MONTE CARLO LOCALIZATION   3
9   OCCUPANCY GRID MAPPING   3
10   SIMULTANEOUS LOCALIZATION AND MAPPING   3
11   THE EXTENDED INFORMATION FORM ALGORITHM   3
12   THE SPARSE EXTENDED INFORMATION FILTER   3
13   MAPPING WITH UNKNOWN DATA ASSOCIATION   3
14   FAST INCREMENTAL MAPPING ALGORITHMS   3
15   MARKOV DEVISION PROCESSES   3
Total   45
Text Books:
1. Probabilistic Robotics, by Sebastian Thrun, Wolfram Burgard, Dieter Fox, 2012
Reference Books:
1. Robotics Hand book
Any other information: NIL
Total Marks of Internal Continuous Assessment (ICA): 50 Marks
Signature
(Prepared by Concerned Faculty/HOD)
M. Tech /AI/2021-22/SEM III /Page 13 of 16
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Distribution of ICA Marks:
Description of ICA   Marks
Test Marks   20
Term Work Marks   30
Total Marks :   50
Details of Term work:
1. Practical based on 10 Experiments
2. Two class tests.
3. Minimum two assignment
Signature
(Prepared by Concerned Faculty/HOD)
M. Tech /AI/2021-22/SEM III /Page 14 of 16
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Program: M. Tech. – Artificial Intelligence   Semester :   III
````

## M Tech · Artificial Intelligence · batch 2019-2021 · Sem 3

- Course as printed: Probabilistic Robotics (code MTAI03006)
- Source: `04_Syllabi_Archive/M Tech/Artificial Intelligence/Batch ( 2019 To 2021 )/Semester - 3.pdf`, page 11-13

````text
Program: M. Tech. – Artificial Intelligence   Semester :III
Course: Probabilistic Robotics   Module Code : MTAI03006
Teaching Scheme   Evaluation Scheme
Lecture   Internal Continuous   Term End Examinations
Practical   Tutorial
(Hours   Assessment   (TEE)
(Hours per   (Hours   Credit
per   (ICA)   (Marks -100   in
week)   per week)
week)   (Marks -50)   Question Paper)
3   0   0   3   Marks Scaled to 50   Marks Scaled to 50
Pre-requisite: Probability/Python/Programming language/Robotics
Objectives:
Robotics is the science of perceiving and manipulating the physical world through computer-
controlled mechanical devices. Examples of successful robotic systems include mobile platforms for
planetary exploration, robotics arms in assembly lines, cars that travel autonomously on highways,
actuated arms that assist surgeons.
Robotics systems have in common that they are situated in the physical world, perceive their
environments through sensors, and manipulate their environment through things that move.
Outcomes:
After completion of the course, students would be able to :
1. Environments. Physical worlds are inherently unpredictable. While the degree of uncertainty in
well-structured environments such assembly lines is small, environments such as highways and
private homes are highly dynamic and unpredictable.
2. Sensors. Sensors are inherently limited in what they can perceive. Limitations arise from two
primary factors. First, range and resolution of a sensor is subject to physical laws. For example,
Cameras can’t see through walls, and even within the perceptual range the spatial resolution of
camera images is limited. Second, sensors are subject to noise, which perturbs sensor
measurements in unpredictable ways and hence limits the information that can be extracted from
sensor measurements.
3. Robots. Robot actuation involves motors that are, at least to some extent, unpredictable, due effects
like control noise and wear-and-tear. Some actuators, such as heavy-duty industrial robot arms,
are quite accurate. Others, like low-cost mobile robots, can be extremely inaccurate.
4. Models. Models are inherently inaccurate. Models are abstractions of the real world. As such, they
only partially model the underlying physical processes of the robot and its environment. Model
errors are a source of uncertainty that has largely been ignored in robotics, despite the fact that
most robotic models used in state-or-the-art robotics systems are rather crude.
5. Computation. Robots are real-time systems, which limits the amount of computation that can be
carried out. Many state-of-the-art algorithms (such as most of the algorithms described in this
book) are approximate, achieving timely response through sacrificing accuracy.
Detailed Syllabus: (per session plan)
Unit   Description   Duration
1   INTRODUCTION   3
___________   ____________
Signature   Signature
(Prepared by Concerned Faculty/HOD)   (Approved by Dean)
M. TECH /AI/2020-21/SEM III /Page 11 of 14
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
2   RECURSIVE STATE ESTIMATION   3
3   GAUSSIAN FILTERS   3
4   NONPARAMETRIC FILTERS   3
5   ROBOT MOTION   3
6   MEASUREMENTS   3
7   MOBILE ROBOT LOCALIZATION   3
8   GRID AND MONTE CARLO LOCALIZATION   3
9   OCCUPANCY GRID MAPPING   3
10   SIMULTANEOUS LOCALIZATION AND MAPPING   3
11   THE EXTENDED INFORMATION FORM ALGORITHM   3
12   THE SPARSE EXTENDED INFORMATION FILTER   3
13   MAPPING WITH UNKNOWN DATA ASSOCIATION   3
14   FAST INCREMENTAL MAPPING ALGORITHMS   3
15   MARKOV DEVISION PROCESSES   3
Total   45
Text Books:
1. Probabilistic Robotics, by Sebastian Thrun, Wolfram Burgard, Dieter Fox, 2012
Reference Books:
1. Robotics Hand book
Any other information: NIL
Total Marks of Internal Continuous Assessment (ICA): 50 Marks
Distribution of ICA Marks:
Description of ICA   Marks
Test Marks   20
Term Work Marks   30
Total Marks :   50
Details of Term work:
1. Practical based on 10 Experiments
2. Two class tests.
3. Minimum two assignment
___________   ____________
Signature   Signature
(Prepared by Concerned Faculty/HOD)   (Approved by Dean)
M. TECH /AI/2020-21/SEM III /Page 12 of 14
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Program: M. Tech. – Artificial Intelligence   Semester :   III
````

## M Tech · Artificial Intelligence · batch 2018-2020 · Sem 3

- Course as printed: Probabilistic Robotics (code MTAI03006)
- Source: `04_Syllabi_Archive/M Tech/Artificial Intelligence/Batch ( 2018 To 2020 )/Semester - 3.pdf`, page 11-13

````text
Program: M. Tech. - Artificial Intelligence Semester :III
Course: Probabilistic Robotics Module Code: MTAI03006
Teaching Scheme Evaluation Scheme
L Practical | Tutorial Internal Continuous Term End
ecture Bocrpi
(Hours-per (Hours | (Hours Credit Assessment Examinations (TEE)
per per (ICA) (Marks -100

weedy week) week) (Marks -50) in Question Paper)
3 0 0 3 Marks Scaled to 50 | Marks Scaled to 50

Pre-requisite: Probability / Python/ Programming language/ Robotics

Objectives:

Robotics is the science of perceiving and manipulating the physical world through
computer-controlled mechanical devices. Examples of successful robotic systems include
mobile platforms for planetary exploration, robotics arms in assembly lines, cars that travel
autonomously on highways, actuated arms that assist surgeons.

Robotics systems have in common that they are situated in the physical world, perceive

their environments through sensors, and manipulate their environment through things that
move.

Outcomes:

After completion of the course, students would be able to :

1. Environments. Physical worlds are inherently unpredictable. While the degree of
uncertainty in well-structured environments such assembly lines is small, environments
such as highways and private homes are highly dynamic and unpredictable.

2. Sensors. Sensors are inherently limited in what they can perceive. Limitations arise
from two primary factors. First, range and resolution of a sensor is subject to physical
laws. For example, Cameras can’t see through walls, and even within the perceptual
range the spatial resolution of camera images is limited. Second, sensors are subject to
noise, which perturbs sensor measurements in unpredictable ways and hence limits the
information that can be extracted from sensor measurements.

3. Robots. Robot actuation involves motors that are, at least to some extent, unpredictable,
due effects like control noise and wear-and-tear. Some actuators, such as heavy-duty
industrial robot arms, are quite accurate. Others, like low-cost mobile robots, can be
extremely inaccurate.

4. Models. Models are inherently inaccurate. Models are abstractions of the real world. As
such, they only partially model the underlying physical processes of the robot and its
environment. Model errors are a source of uncertainty that has largely been ignored in
robotics, despite the fact that most robotic models used in state-or-the-art robotics
systems are rather crude.

5. Computation. Robots are real-time systems, which limits the amount of computation
that can be carried out. Many state-of-the-art algorithms (such as most of the algorithms

described in this book) are approximate, achieving timely response through sacrificing
accuracy.

11.
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering

Detailed Syllabus:
Unit Description Duration
1 INTRODUCTION 3
2 RECURSIVE STATE ESTIMATION 3
a GAUSSIAN FILTERS 3
4 NONPARAMETRIC FILTERS 3
5 ROBOT MOTION 3
6 MEASUREMENTS 3
7 MOBILE ROBOT LOCALIZATION 3
8 GRID AND MONTE CARLO LOCALIZATION 3
9 OCCUPANCY GRID MAPPING 3
10 SIMULTANEOUS LOCALIZATION AND MAPPING 3
11 THE EXTENDED INFORMATION FORM ALGORITHM 3
12 THE SPARSE EXTENDED INFORMATION FILTER 3
13 MAPPING WITH UNKNOWN DATA ASSOCIATION 3
14 FAST INCREMENTAL MAPPING ALGORITHMS 3
15 MARKOV DEVISION PROCESSES 3
Total 45
Text Books:

1. Probabilistic Robotics, by Sebastian Thrun, Wolfram Burgard, Dieter Fox, 2012
Reference Books:
1. Robotics Hand book

Any other information: NIL

Details of Internal Continuous Assessment (ICA):
Test Marks: 20
Term Work Marks: 30

Details of Term work:

1. Practical based on 10 Experiments

2. Two class tests.

3. Minimum two assignments ‘

_ Gites =

‘me an
Signature Signature
(Prepared by Concerned Faculty/HOD) (Approved by Dean)

12
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering

Program: M. Tech. - Artificial Intelligence Semester: III
````
