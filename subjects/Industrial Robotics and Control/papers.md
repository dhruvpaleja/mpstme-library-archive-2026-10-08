# Industrial Robotics and Control: question papers in full

2 unique papers · 2021-22 to 2022-23 · Common (all branches)

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2022-23 · Final-Exam · Sem 7 · paper 72f96861383b

- Departments: Common (all branches)
- Programmes: B TECH, MBA TECH
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/ALL STREAMS/SEM-VII/INDUSTRIAL ROBOTICS & CONTROL/Industrial Robotics & Control, 4th Year, Sem VII, Year 2022-23, Final Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 December 2022
- Text: ocr (7 pages), mean OCR confidence 72.0

````text
/

|

4

‘SVKM’s NMIMS fs
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Academic Year: 2022-23

Programme: B.Tech / MBA Tech (All Stream) Year: IV Semester: VII
Subject: Industrial Robotics and Control , :

Marks: 100
Date: 01 December 2022 / . Time: 2.00 pm - 5.00 pm »

Durations: 3 (Hrs) /

No. of Pages:_a
Final Examination ; ;

Instructions: Candidates should read carefully the instructions printed on the question
paper and on the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any _4__-_ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks. ;

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

al Answer briefly: [20]
a3 a Classification and Structures of Robots. [04]
es ated (a Compare and contrast direct kinematics and inverse kinematics. [04]
real SO- |c. Explain shrink and swell operators. [04]
CO-3,4 ; d. ‘

SO-6 “BL-2 Hard and soft automation [04]
CO-2 ; e.

SO-7 ‘BL-6 Total work envelop and dexterous work envelope . [04]
Q2

te ae Lis Solve inverse kinematics problem of a two axis articulated robot. [10]
BL-3

Consider two coordinate frames: a base frame denoted by OXYZ

B |-and a moving frame denoted by OUVW, which are initially
coincident. The moving frame will be transformed according to the’

Q2 following order:
as BALA: i. arotation of a angle about OY; [10]
We S04; ii. a translation of d units along the original OV ;

iii. a translation of e units along the new OU;
. iv. arotation of angle about the original OZ
Compute the homogenous transformation matrices for the above

individual transformations and the composite transformation matrix
--- page 2 ---
of the above transformations in the given order. (Note that you do
not need to explicitly multiply the 4x4 matrices). .

ELBOW
EXTENSION

SHOULDER
‘SWIVEL 4

ae Nila :
Q3 Qual) .
CO-1,2,4; [A =) Ss 10]
S0-1,2; BL- ©)
13,4 RSSTFout
Determine the number of degrees of freedom of the robot given.
Explain how many major and minor axes are present for the given
robot?
Q3 Construct the Robot Motion Planning flowchart with short 7 0]
Soo. SO-6; | B | explanation of each block.
a4 ‘Determine TCV of a SCARA robot when the vector of joint variables
A is given by:
CO-1; SO-1; q =[ 0°, 0°, 100mm, 90°] [10]
BL3- d =[877, 0, d3, 200]' mm ;
a =[ 425, 375, 0,0 ]’ mm
eae 4 B Explain with sketches horizontal plane and vertical plane (reaches 110]
SO-1 ‘BL-2 and strokes) of a SCARA robot. ;
The base joint of a cylindrical coordinate robot is driven by a 10-bit
DAC and has a swing range of 360°. The radial axis is driven by a
42-bit DAC and has horizontal reach of 330mm and a horizontal
Q5 A | stroke of 240mm. Finally, the vertical axes are driven by an 8-bit
CO-2; SO-6; DAC and has vertical reach of 480mm and a verticai stroke of [10]
BL-5 300mm
a) Evaluate work volume of the cylindrical coordinate robot?
b). Evaluate vertical precision Az?
c) Evaluate radial precision Ar?
on so-2: | B Explain perspective and inverse perspective transformation in [10]
BL-3 ’ , robotics vision.
Q6 vo : 8 . . .
CO-4: S0-2: A | Highlight various applications of Al in robotics and explain any one [10]
BL-3 , , application.

aR
--- page 3 ---
An 8x8 gray level image with 16 gray levels is shown in figure

Q6
CO-3: SO-6: below. Construct the histogram of the image and convert the image
BL-34 , into a binary image using a suitable threshold value
, 7 3 3 3 5 5°53 #1
3 147 4 5 10 12 5
B 0 14 10 8 3 13 13 3
4 13 13 12 13 15 14 3
3 14 13 13 12 14 10 5
[10]
4 1110 5 5 14 13 4
3 13 ll 3 0-12 10 7
5 3 4 363 4 4
Q7 Compute the composite rotation matrix by rotating the tool about
‘2 CO-1; $O-1; | A | the fixed axis of F frame with a yaw of 11/2 followed by a pitch of [10]
BL3- -1/2 and finally a roll of 1/2. If [pJ™ = [0,0,0.6]", find [p]f
Q7 B .| List the Factors on which workspace of a robot depends. [10]
ir alien Analyze the work space of a 2 DOF SCARA Robot shown in the fig.
y
ce pee os x.
c
X
3[%
--- page 4 ---
No. of axis

2 axis planar articulated robot

Link Coordinate
diagram

x!

Kinematic parameter
table :

Link Joint angle(®) | Joint distance(d) | Link length(a) Link twist angle(a)
1 qi 0 ai : 0
Z q2 0) a2 0

Arm matrix

T = [cya —Saz 0 04Cy + A202 $12 Crp 0 A454 + a254200100001]

Cyn —Fyq 8 yey + 2Q¢19

pea} 12 12% 151 * 42819
0 0 1, 0
0 o 0 1

Tool coordinate vector

w(q) = [ares + aacaz aSs + 42512 000 [exp exp ) lI

Inverse kinematics
(Variable link
parameters)

qz=rInwe

qu=atan2{[(a1-a2ce)wita2s2Wel / [(arta2ce)w2-a2S2W:]}

APE
--- page 5 ---
No. of axis

3 axis planar articulated robot

Link Coordinate
diagram

Kinematic parameter
| table

8 ~-
Base x
Link Joint angle(8) | Joint distance(d) Link length(a) Link twist angle(a)
1 qi 0 a1 ie}
2 q2 0 : a2 0
3 q3 | d3 0 0

Arm matrix

T = [e123 — $123 0 A101 + G2C12 $123 C123 0 aysy + 42512 001d; 000 1]

1Cy23, 8123 0 at, + aCi2
Sis Crs 0 aS + a2Si2
o 90 L as
0 0.) 60 i

Tool coordinate vector

w(q) = fares + pC42 81 + AgS12 d3 00 [exp exp (®) | |

5fR
--- page 6 ---
*

al, + mCy
aS) + Sp
: ds :
W(g) = jpean--n--=--
0
0

| exp (q3/7)

Inverse kinematics
(Variable link
parameters)

qp=tarccostite-ainae
r= 2ayaz

qu=atan2[(a1-a2c2)wita2s2W2 / (a1+a2C2)W2-a2S2Wi]

qs3=mInwe

wi + wi — a? — a8

Q> = tarecos
.? 2ay ay

7

‘q, = atan2 [{a, — a, Ca}w, + agS5wy, (a, + agGylws — aS2wy)

{

q3 = 7 Inws

le
--- page 7 ---
No. of axis 4 axis (SCARA)

Link Coordinate Vertical
diagram Stbow extension
; Se ;
by M2
x x?

t a —e
| vA] 2 ah 2 |
| wi acto, fT
—e
CjDa rs f ,

dy
ia a |
2s ¥ yt / Toot
= eee xt Tt
Pl
Baso
Kinematic parameter
table Link - Joint angle(®) | Joint distance(d) | Link length(a) Link twist angle(a)
1 qi di ai Tt
9 qQ2 ie} a2 ie}
a 0 d3 0 0
4 qa ~ | da 0 0
Arm matrix Cerne -Steree 0 | GC + @2Ci-r
Sjo2-4   —Ci-a-4, 0 d as, + @Si-2
TRL = }0 0 -1 H di — qs — dy
0 0 0: 1
Tool coordinate vector + JaCy +-aCy-2
aS; + a2Si-2
a- gana d&
W@) = [a
0
0
~exp (qs/m)

a i
````

## 2021-22 · Final-Exam · Sem 6 · paper 87985ae8912f

- Departments: Common (all branches)
- Programmes: MBA TECH
- Source: `02_Question_Papers/Legacy/MBA TECH/3RD YEAR/Common For All Stream/SEM VI/Industrial Robotics and Control/Industrial Robotics and Control,Sem6,Final,2021-22.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 22 April 2022
- Text: ocr (3 pages), mean OCR confidence 88.8

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Academic Year: 2021-22

Programme: MBA Tech (All Streams) Year: III Semester: VI

Subject: Industrial Robotics and Control
Marks: 100
Date: 22 April 2022 Time: 2.00 pm to 5.00 pm

Durations: 3 (hrs)

No. of Pages: __2%

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question
paper and on the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi Answer briefly: [20]
ae : $0-1 | 2. | Classification and Structures of Robots. [04]
ar oore |G. Compare and contrast direct kinematics and inverse kinematics. [04]
cord SO- |G Explain shrink and swell operators. [04]
CO-3,4; d. .
SO-6 :BL-2 Hard and soft automation [04]
CO-2 ; e.
SO-7 ‘BL-6 Total work envelop and dexterous work envelope [04]
Q2
nia SO- | | solve inverse kinematics problem of a two axis articulated robot. [10]
BL-3

Consider two coordinate frames: a base frame denoted by OXYZ
Q2 B | and a moving frame denoted by OUVW , which are initially 10]
CO-1; SO-1; coincident. The moving frame will be transformed according to the
BL-3 following order:

i. a rotation of a angle about OY;

1p
--- page 2 ---
ii. a translation of d units along the original ov;

iii. a translation of e units along the new ou;

iv. arotation of angle 2 about the original OZ .
Compute the homogenous transformation matrices for the above
individual transformations and the composite transformation matrix
of the above transformations in the given order. (Note that you do
not need to explicitly multiply the 4x4 matrices).

ELBOW

EXTENSION

. Q3

CO-1,2,4; A
SO-1,2: BL- [10]
3,4

Explain how many major and minor axes are present for the given

robot?
Q3 Construct the Robot Motion Planning flowchart with short [10]
Soe SO-6; | B | explanation of each block.

Determine TCV of a SCARA robot when the vector of joint variables
Q4 re ;

A | isgiven by:
CO-1; SO-1; q =[ 0°, 0°, 100mm, 90°] [10]
BL3- d = [ 877, 0, d3, 200]' mm
a =[ 425, 375, 0,0]’mm

one 4: B Explain with sketches horizontal plane and vertical plane (reaches 110]
S0-1:BL-2 and strokes) of a SCARA robot.

The base joint of a cylindrical coordinate robot is driven by a 10-bit

DAC and has a swing range of 360°. The radial axis is driven by a

12-bit DAC and has horizontal reach of 330mm and a horizontal
Q5 A | stroke of 240mm. Finally, the vertical axes are driven by an 8-bit
CO-2; SO-6; DAC and has vertical reach of 480mm and a vertical stroke of [10]

, BL-5 300mm

a) Evaluate work volume of the cylindrical coordinate robot?
b) Evaluate vertical precision Az?
c) Evaluate radial precision Ar?

P
--- page 3 ---
Qs

B | Explain perspective and inverse perspective transformation in

[10]

CO-3; SO-2; are

BL-3 robotics vision.

Q6 A | Highlight various applications of Al in robotics and explain any one

CO-4; SO-2; llcati [10]
BL-3 » application.

Qé An 8x8 gray level image with 16 gray levels is shown in figure

CO-3: SO-6: below. Construct the histogram of the image and convert the image
BL-3.4 , into a binary image using a suitable threshold value

7 3 3 3 5 5 5 1
3 14 7 4 5 10 12 5
p| 0° 14 10 8 3 13 13 3
4 13 13 12 13 15 14 3
3 14 13 13 12 14 10 5
4 11 10 5 5 14 13 4
3 13 11 3 #0 12 10 7
5 3 4 3 6 3 4 4

[10]
````
