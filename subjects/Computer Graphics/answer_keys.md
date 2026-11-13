# Computer Graphics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 520e10c34101

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/Integrated_Computer_7032/Computer Graphics/ANS_Computer Graphics(701CO0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: mixed (20 pages), mean OCR confidence 54.7
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Computer Graphics
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions attempt any 4 questions
4. All question carry equal marks
5. Answer to each new question to be started on a fresh page
6. Figures in brackets on the right hand side indicate full marks
7. Assume suitable data if necessary
Q1   Answer briefly
[20]
CO- a. Analyse the concept of aliasing in computer graphics. Discuss its causes and list
1;   the different techniques used to reduce aliasing effects in digital images.
BL- Solution:
3   Definition of aliasing   2 marks
Causes (any 2–3 explained)   2 marks
Techniques (any 3–4 explained)   1 mark
Definition:
Aliasing in computer graphics refers to the visual distortion that occurs when a
continuous image is represented using a finite number of pixels. It results in
artifacts such as jagged edges (staircase effect), flickering, or moiré patterns,
especially along diagonal or curved lines.
Causes of Aliasing:
•   Insufficient sampling resolution – When the image is sampled at a rate
lower than required (violating Nyquist criterion).   [5]
•   Discrete pixel representation – Continuous objects are approximated
using square pixels.
• High-frequency details – Fine patterns or sharp edges are not captured
accurately.
Techniques to Reduce Aliasing (Anti-Aliasing):
1. Super Sampling (SSAA)
• Image is rendered at a higher resolution and then downsampled.
2. Multi-Sample Anti-Aliasing (MSAA)
• Samples multiple points per pixel to smooth edges.
3. Post-Processing Filters (FXAA, MLAA)
• Smooth edges after rendering using image processing.
4. Area Sampling
•   Pixel color is computed based on the area covered by the object.
5. Prefiltering / Low-pass Filtering
• Removes high-frequency components before sampling.
********** 1 **********
--- page 2 ---
CO- b.Explain the even-odd test used to determine whether a point lies inside or
2;   outside a polygon. Demonstrate the method with an example.
BL- Solution:
2   Definition & concept
Rule (odd/even explanation)
Explanation of method
Example
The even–odd test (also called the ray casting method) is used to determine
whether a given point lies inside or outside a polygon.
Concept:
Draw an imaginary ray (horizontal or vertical line) from the given point to
infinity.
Count how many times this ray intersects the edges of the polygon.
👉 Rule:
If the number of intersections is odd → the point lies inside the polygon
If the number of intersections is even → the point lies outside the polygon   [5]
Consider a polygon and a point P.
• Draw a horizontal ray from point P toward the right.
• Suppose the ray intersects the polygon edges 3 times.
👉 Since 3 is odd,
➡️ Point P lies inside the polygon
If the ray had intersected 2 or 4 times (even),
➡️ the point would be outside.
CO- c. A triangle has vertices A(3,4), B(6,4), and C(5,6). Apply shearing
3;   transformation about the x-axis with shear parameter 2 and about the y-axis with
BL- shear parameter 3 separately. Calculate the transformed coordinates.
3   Solution:   [5]
Formula (both shears) 1
X-shear calculations 2
Y-shear calculations 2
********** 2 **********
--- page 3 ---
@ 1. Shearing about X-axis (Shx = 2)

Formula:

a’ =2r+Shr-y, y=y

Calculate new coordinates:

Point A(3.4)

2 =34+2(4)=11, y'=4
a A’ =(11,4)
Point B(6,4)

a’ =6+2(4)=14, y'=4
o@ B= (14, 4)
Point C(5,6)

v’=5+2(6)=17, y' =6
oC = (17,6)

@ After X-shear:
A‘(11,4), B(14,4), C'(17,6)

® 2. Shearing about Y-axis (Shy = 3)
Formula:

v=2, y'=y+Shy,-z

Calculate new coordinates:

Point A(3,4)

y =44+3(3)=13, 2 =3
@ A’ = G3, 13)
Point B(6,4)

y =4+3(6)=22, 2 =6
o@ B = (6, 22)
Point C(5,6)

y =64+3(5)=21, 2’ =5
o@ C'= (5,21)

Gi After Y-shear:
A‘(3,13), B'(6,22), C'(5,21)

FC QI a iar
--- page 4 ---
CO- d.Explain the scan-line algorithm used for hidden surface removal. Describe the
4;   steps involved and how it determines visible surfaces with the help of a diagram.
BL- Solution:
4   Definition & concept   1
Steps explanation   2
Visibility determination (Z-buffer logic) 1
Diagram   1
The scan-line algorithm is a technique used in computer graphics to
determine visible surfaces of objects by processing the scene one
horizontal line (scan line) at a time. It is efficient because it avoids
handling the entire image at once and works incrementally across scan
lines.
🔹 Concept
• The screen is divided into horizontal scan lines.
•   For each scan line, the algorithm determines which surfaces are visible.
•   It uses depth comparison (Z-values) to decide which surface is in front.
[5]
Steps of the Scan-Line Algorithm
1. Initialize Data Structures
o Edge Table (ET): Stores polygon edges
o Active Edge Table (AET): Stores edges intersecting current scan
line
2. Process Each Scan Line
o   Start from the top scan line and move downward
3. Update Active Edge Table
o Add edges that intersect the current scan line
o Remove edges that are no longer active
4. Find Intersections
o Compute intersection points of scan line with polygon edges
5. Sort Intersections
o   Sort intersection points from left to right
6. Determine Visible Surface
o Compare depth (Z-values) of overlapping surfaces
o The surface with the smallest Z-value (closest to viewer) is visible
7.   Fill Pixels
o   Fill pixels between pairs of intersections with the visible surface
How Visibility is Determined:
********** 4 **********
--- page 5 ---
When multiple polygons overlap on a scan line: Their Z-values are compared
at each pixel. The polygon with the minimum depth (closest) is displayed This
ensures correct rendering of overlapping surfaces
Q2 a. Write and Apply the Liang–Barsky algorithm for clipping a line segment
CO- against a rectangular window. A line segment with endpoints P(20, 30) and
3;   Q(80, 90) is to be clipped against a rectangular window defined by:xwmin = 30,
BL- xwmax = 70,  ywmin = 40,  ywmax = 80
3
Solution:
Algorithm: 4 marks
Solution: 6 marks
[10]
********** 5 **********
--- page 6 ---
Q2 b.What are the steps involved in filling a polygon using the scanline method,
CO- elaborate using its special cases.
2;
BL- Solution:
2   Method: 6 marks
Special Cases: 2 marks
Diagram:2 marks
• Scanline filling is basically filling up of polygons using horizontal lines or
scanlines.
• The purpose of the SLPF algorithm is to fill (color) the interior pixels of a
polygon given only the vertices of the figure.
• This algorithm works by intersecting scanline with polygon edges and fills
the polygon between pairs of intersections.
Steps:
Step 1 − Accept the number of vertices in the polygon and the co-ordinates of
the vertices.
Step 2 − Active Edge List is prepared for each scanline intersecting the polygon
that contains the list of edges intersecting the scanline.
Step 3 −For each polygon edge in the AEL intersection points are calculated. [10]
Step 4: Sort all the edge intersecting points in increasing order of x-values.
The first x values gives the left boundary and second x value gives the right
boundary.
Step 5: Fill all the pixel positions between left and right boundary with the
specified color value.
Repeat the steps 2 to 5 for all the scanlines.
Special cases of polygon vertices:
•   If both lines intersecting at the vertex are on the same side of the scanline,
consider it as two points.
•   If lines intersecting at the vertex are at opposite sides of the scanline,
consider it as only one point.
********** 6 **********
--- page 7 ---
Q3 a. Explain the 3D viewing pipeline in computer graphics. Describe the stages
CO- involved in transforming a 3D object from world coordinates to screen
3;   coordinates. Also explain the concept of 3D clipping.
BL- Solution:
2   Component   Marks
Definition of pipeline   2
Stages explanation (6 stages) 6
3D clipping concept   2
The 3D viewing pipeline is the sequence of transformations that converts a 3D
object from its original definition into a 2D image on the screen. It transforms
coordinates from world space → viewing space → screen space.
Stages of 3D Viewing Pipeline
1. Model Transformation (Object → World Coordinates)
• Converts object coordinates into world coordinates   [10]
• Applies transformations like translation, rotation, scaling
2. Viewing Transformation (World → Eye Coordinates)
• Transforms world coordinates into view (camera) coordinates
• Defines camera position, orientation, and viewing direction
3. Projection Transformation (3D → 2D)
• Converts 3D view into a 2D representation
• Two types:
➢ Parallel Projection (orthographic)
➢ Perspective Projection (realistic depth effect)
4. Clipping
• Removes parts of objects outside the viewing volume (view frustum)
• Ensures only visible portions are processed further
5. Normalization
• Converts coordinates into a standard range (usually -1 to +1)
•   Simplifies further processing
6. Viewport Transformation (Screen Mapping)
• Maps normalized coordinates to actual screen coordinates (pixels)
• Determines final image position on display
3D clipping is the process of removing parts of objects that lie outside the
viewing volume before rendering.
Clipping Volume (View Frustum):
Defined by:
•   Left, Right
• Top, Bottom
********** 7 **********
--- page 8 ---
• Near plane
• Far plane
Purpose:
• Improves efficiency
• Avoids unnecessary rendering
• Ensures correct visibility
Q3 b.Explain the area subdivision method in detail. Discuss how recursive
CO- subdivision works and stopping conditions.
4;   Solution:
BL-   Component   Marks
2   Definition & concept 2
Working principle   2
Steps explanation   2
Recursive subdivision 1.5
Stopping conditions 2
Diagram   1
The Area Subdivision Method is a hidden surface removal technique in
computer graphics that determines visible surfaces by recursively dividing the
viewing area into smaller regions. Instead of processing individual pixels or
entire objects, it works by analyzing areas (regions) of the screen.
Working Principle
• The entire screen is treated as a single region.
• The algorithm checks whether the region:
o Contains only one surface → display it
o Contains multiple overlapping surfaces → subdivide further   [10]
👉 This process continues recursively until visibility can be clearly
determined.
🔹 Steps of the Algorithm
1. Start with Entire Viewing Area
o Consider the whole screen as one region
2. Classify Surfaces in Region
o Determine which polygons intersect or lie within the region
3. Test Visibility Conditions
o   If one surface completely covers the region → fill it
o   If no surface is present → leave it blank
4. Apply Subdivision
o   If multiple surfaces overlap, divide the region into four
smaller regions (quadtree approach)
5. Repeat Recursively
o Apply the same process to each sub-region
6. Render Final Visible Surfaces
o Continue until each region satisfies a stopping condition
Tests to determine the visibility of a single surface within a specified area are
made by comparing surfaces to the boundary of the area.
********** 8 **********
--- page 9 ---
 There are four possible relationships that a surface can have with a
specified area boundary.
➢ Surrounding surface - One that completely encloses the area.
➢ Overlapping surface - One that is partly inside and partly outside the
area.
➢ Inside surface - One that is completely inside the area.
➢ Outside surface - One that is completely outside the area.
Recursive Subdivision
• The region is divided into four equal parts repeatedly
• Each subdivision reduces ambiguity in visibility
• This forms a quadtree structure
👉 Example:
• Large region → contains 3 polygons
• Subdivide → smaller regions
• Some regions → only 1 polygon → directly visible
 The tests for determining surface visibility within an area can be
stated in terms of these four classifications.
 No further subdivisions of a specified area are needed if one of the
following conditions is true:
1. All surfaces are outside surfaces with respect to the area.
2. Only one inside, overlapping, or surrounding surface is in the area.
3. A surrounding surface obscures all other surfaces within the area
boundaries.
Q4 a. Examine the role and significance of computer graphics in: Computer-Aided
CO- Design (CAD), Entertainment Industry, Educational Technology, Scientific
3;   Visualization and AR/VR.
BL-
2   Solution:
Each application 2 marks
Computer graphics plays a crucial role in transforming data into visual content,
enabling better understanding, design, and interaction across multiple domains. [10]
Its impact is significant in fields such as Computer-Aided Design (CAD),
Entertainment, Educational Technology,   Scientific   Visualization, and
Augmented/Virtual Reality (AR/VR).
1. Computer-Aided Design (CAD)
Role:
• Used to create precise 2D and 3D models of products, buildings,
and machines
********** 9 **********
--- page 10 ---
• Enables simulation, modification, and optimization of designs
Significance:
• Improves accuracy and reduces design errors
• Saves time and cost in prototyping
• Widely used in engineering, architecture, and manufacturing
2. Entertainment Industry
Role:
• Used in animation, movies, gaming, and visual effects (VFX)
• Creates realistic characters, environments, and special effects
Significance:
• Enhances storytelling and visual appeal
• Enables immersive gaming and cinematic experiences
• Drives innovation in media and digital content
3. Educational Technology
Role:
• Provides visual simulations, animations, and virtual labs
• Helps explain complex concepts in an interactive way
Significance:
• Improves understanding and retention
• Supports remote and personalized learning
• Makes education more engaging and accessible
4. Scientific Visualization
Role:
• Converts complex data into visual formats like graphs, models, and
simulations
• Used in fields such as medicine, meteorology, and physics
Significance:
• Helps analyze large datasets effectively
• Supports research and decision-making
• Enables discovery of patterns and trends
5. Augmented Reality (AR) and Virtual Reality (VR)
Role:
• AR overlays digital content on the real world
********** 10 **********
--- page 11 ---
• VR creates fully immersive virtual environments
Significance:
• Used in training, healthcare, gaming, and education
• Enhances user interaction and experience
• Enables real-time simulation and visualization
Q4 b. Write the Midpoint Circle Algorithm. Using this algorithm, tabulate the steps
CO- for drawing a circle centered at (2, 2) with a radius of 8. Show all calculations
2;   and the points generated in each step.
BL- Solution:
3   Algorithm: 4 marks
Sum: 6 marks
[10]
********** 11 **********
--- page 12 ---
Q5 a. Explain rigid body transformations in computer graphics. Write the matrix
CO- representations for translation, rotation, and scaling using homogeneous
3;   coordinates. Show the inverse transformation matrices for each.
BL- Solution:
4   Definition: 2 marks
Normal Transformation: 4 marks
Inverse Transformations: 4 marks
Rigid body transformations are transformations that preserve shape and
size (i.e., distances and angles remain unchanged).
👉 They include:
• Translation
• Rotation
[10]
Q5 b.Write the Digital Differential Analyzer (DDA) line drawing algorithm. Using
CO- this algorithm, compute all points for the line joining (6, 3) to (12, 9). Show
2;   stepwise calculations and the final coordinates.   [10]
BL- Solution:
3   Algorithm: 4 marks
Sum: 6 marks
********** 12 **********
--- page 13 ---
Q6 a. A window is defined by coordinates (0,0) to (100,100) and a viewport is defined
CO- by (200,200) to (400,300). Derive the transformation equations, determine the
3;   scaling factors, and compute the mapped coordinates of the point (25,75). Also, [10]
BL-   illustrate the mapping of the window onto the viewport with a neat diagram and
4   steps.
********** 13 **********
--- page 14 ---
Solution:
Component   Marks
Formula derivation   2
Scaling factors   2
Numerical computation 3
Final answer   1
Diagram   2
Q6 b.Explain   perspective   projection   in   detail.
CO- Discuss one-point and two-point perspective projections with diagrams.
1;   Solution:
[10]
BL- Definition & concept 2
3   Explanation 2
One-point perspective 2
Two-point perspective   2
********** 14 **********
--- page 15 ---
Diagrams   2
Comparison / conclusion   1
Perspective projection is a method of representing a 3D object on a 2D plane
such that objects farther from the viewer appear smaller, mimicking human
visual perception.
 Another method for generating a view of a three-dimensional scene is to
project points to the display plane along converging paths.
 This causes objects farther from the viewing position to be displayed smaller
than objects of the same size that are nearer to the viewing position.
 In a perspective projection, parallel lines in a scene that are not parallel to the
display plane are projected into converging lines.
 Scenes displayed using perspective projections appear more realistic, since
this is the way that our eyes and a camera lens form images.
 The point at which a set of projected parallel lines appear to converge is
called a vanishing point.
 Each set of projected parallel lines will have a separate vanishing point and
in general a scene can have any number of vanishing points depending
on how many sets of parallel lines there are in the scene.
 The vanishing point for any set of lines that are parallel to one of the
principal axes of an object is referred to as a principal vanishing point.
1. One-Point Perspective Projection
Concept:
•   Only one vanishing point
•   Objects face the viewer directly
• Depth is along one axis
Features:
• One vanishing point on horizon
• Common in roads, railways, hallways
********** 15 **********
--- page 16 ---
•   Simple and easy to implement
2. Two-Point Perspective Projection
Concept:
• Two vanishing points
•   Object is viewed at an angle
• Depth along two axes
Features:
• Two vanishing points (left & right)
• More realistic than one-point
• Used in architectural drawings
Q7 a. Write the Cohen–Sutherland algorithm and clip the line joining:
CO- P1 = (5, 40) and P2 = (75, 95) with clipping window: xwmin = 20, ywmin =
3;   30, xwmax = 60,ywmax = 80
BL-
Solution:
3
Algorithm: 4 marks
Solution: 6 marks
[10]
********** 16 **********
--- page 17 ---
FRR ICR] AC OH
--- page 18 ---
Q7 b.A rectangle has vertices A(1,2), B(5,2), C(5,6), D(1,6).
CO- Perform the following homogeneous composite transformations and show the
3;   intermediate matrix calculations:   [10]
BL-   1. Reflection about the y-axis
3   2. Shearing in y-direction (Shy = 1)
3. Scaling with Sx = 2, Sy = 0.5
********** 18 **********
--- page 19 ---
Solution:
Component Marks
Matrices (3 transformations)   3
Matrix multiplication   3
Applying transformation   3
Final answers   1
********** 19 **********
--- page 20 ---
® Step 3: Apply Transformation

Multiply each point (x, y, 1)

Point A(1,2)
z' = —2(1) = -2
y = —0.5(1) + 0.5(2) = -0.5+1=0.5

o@ A’ = (-2, 0.5)

Point B(5,2)
zx’ = —2(5) = —10
y = —0.5(5) + 0.5(2) = -25+1=-15

@& B’ = (-10, -1.5)

® Point C(5,6)
x’ = —10
y' = —0.5(5) + 0.5(6) = -2.54+3=0.5

o@ C' = (-10, 0.5)

Point D(1,6)
zr’ =-2

y' = —0.5(1) + 0.57) = 0.5 +3 = 2.5

@ D' = (-2, 2.5)

FRI ICR DO) A RH
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 0a92846ebe4e

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/Integrated_DS_7038/Computer Graphics/ANS_Computer Graphics(701CO0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 May 2026
- Text: mixed (20 pages), mean OCR confidence 54.7
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Computer Graphics
Date: 16 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions attempt any 4 questions
4. All question carry equal marks
5. Answer to each new question to be started on a fresh page
6. Figures in brackets on the right hand side indicate full marks
7. Assume suitable data if necessary
Q1   Answer briefly
[20]
CO- a. Analyse the concept of aliasing in computer graphics. Discuss its causes and list
1;   the different techniques used to reduce aliasing effects in digital images.
BL- Solution:
3   Definition of aliasing   2 marks
Causes (any 2–3 explained)   2 marks
Techniques (any 3–4 explained)   1 mark
Definition:
Aliasing in computer graphics refers to the visual distortion that occurs when a
continuous image is represented using a finite number of pixels. It results in
artifacts such as jagged edges (staircase effect), flickering, or moiré patterns,
especially along diagonal or curved lines.
Causes of Aliasing:
•   Insufficient sampling resolution – When the image is sampled at a rate
lower than required (violating Nyquist criterion).   [5]
•   Discrete pixel representation – Continuous objects are approximated
using square pixels.
• High-frequency details – Fine patterns or sharp edges are not captured
accurately.
Techniques to Reduce Aliasing (Anti-Aliasing):
1. Super Sampling (SSAA)
• Image is rendered at a higher resolution and then downsampled.
2. Multi-Sample Anti-Aliasing (MSAA)
• Samples multiple points per pixel to smooth edges.
3. Post-Processing Filters (FXAA, MLAA)
• Smooth edges after rendering using image processing.
4. Area Sampling
•   Pixel color is computed based on the area covered by the object.
5. Prefiltering / Low-pass Filtering
• Removes high-frequency components before sampling.
********** 1 **********
--- page 2 ---
CO- b.Explain the even-odd test used to determine whether a point lies inside or
2;   outside a polygon. Demonstrate the method with an example.
BL- Solution:
2   Definition & concept
Rule (odd/even explanation)
Explanation of method
Example
The even–odd test (also called the ray casting method) is used to determine
whether a given point lies inside or outside a polygon.
Concept:
Draw an imaginary ray (horizontal or vertical line) from the given point to
infinity.
Count how many times this ray intersects the edges of the polygon.
👉 Rule:
If the number of intersections is odd → the point lies inside the polygon
If the number of intersections is even → the point lies outside the polygon   [5]
Consider a polygon and a point P.
• Draw a horizontal ray from point P toward the right.
• Suppose the ray intersects the polygon edges 3 times.
👉 Since 3 is odd,
➡️ Point P lies inside the polygon
If the ray had intersected 2 or 4 times (even),
➡️ the point would be outside.
CO- c. A triangle has vertices A(3,4), B(6,4), and C(5,6). Apply shearing
3;   transformation about the x-axis with shear parameter 2 and about the y-axis with
BL- shear parameter 3 separately. Calculate the transformed coordinates.
3   Solution:   [5]
Formula (both shears) 1
X-shear calculations 2
Y-shear calculations 2
********** 2 **********
--- page 3 ---
@ 1. Shearing about X-axis (Shx = 2)

Formula:

a’ =2r+Shr-y, y=y

Calculate new coordinates:

Point A(3.4)

2 =34+2(4)=11, y'=4
a A’ =(11,4)
Point B(6,4)

a’ =6+2(4)=14, y'=4
o@ B= (14, 4)
Point C(5,6)

v’=5+2(6)=17, y' =6
oC = (17,6)

@ After X-shear:
A‘(11,4), B(14,4), C'(17,6)

® 2. Shearing about Y-axis (Shy = 3)
Formula:

v=2, y'=y+Shy,-z

Calculate new coordinates:

Point A(3,4)

y =44+3(3)=13, 2 =3
@ A’ = G3, 13)
Point B(6,4)

y =4+3(6)=22, 2 =6
o@ B = (6, 22)
Point C(5,6)

y =64+3(5)=21, 2’ =5
o@ C'= (5,21)

Gi After Y-shear:
A‘(3,13), B'(6,22), C'(5,21)

FC QI a iar
--- page 4 ---
CO- d.Explain the scan-line algorithm used for hidden surface removal. Describe the
4;   steps involved and how it determines visible surfaces with the help of a diagram.
BL- Solution:
4   Definition & concept   1
Steps explanation   2
Visibility determination (Z-buffer logic) 1
Diagram   1
The scan-line algorithm is a technique used in computer graphics to
determine visible surfaces of objects by processing the scene one
horizontal line (scan line) at a time. It is efficient because it avoids
handling the entire image at once and works incrementally across scan
lines.
🔹 Concept
• The screen is divided into horizontal scan lines.
•   For each scan line, the algorithm determines which surfaces are visible.
•   It uses depth comparison (Z-values) to decide which surface is in front.
[5]
Steps of the Scan-Line Algorithm
1. Initialize Data Structures
o Edge Table (ET): Stores polygon edges
o Active Edge Table (AET): Stores edges intersecting current scan
line
2. Process Each Scan Line
o   Start from the top scan line and move downward
3. Update Active Edge Table
o Add edges that intersect the current scan line
o Remove edges that are no longer active
4. Find Intersections
o Compute intersection points of scan line with polygon edges
5. Sort Intersections
o   Sort intersection points from left to right
6. Determine Visible Surface
o Compare depth (Z-values) of overlapping surfaces
o The surface with the smallest Z-value (closest to viewer) is visible
7.   Fill Pixels
o   Fill pixels between pairs of intersections with the visible surface
How Visibility is Determined:
********** 4 **********
--- page 5 ---
When multiple polygons overlap on a scan line: Their Z-values are compared
at each pixel. The polygon with the minimum depth (closest) is displayed This
ensures correct rendering of overlapping surfaces
Q2 a. Write and Apply the Liang–Barsky algorithm for clipping a line segment
CO- against a rectangular window. A line segment with endpoints P(20, 30) and
3;   Q(80, 90) is to be clipped against a rectangular window defined by:xwmin = 30,
BL- xwmax = 70,  ywmin = 40,  ywmax = 80
3
Solution:
Algorithm: 4 marks
Solution: 6 marks
[10]
********** 5 **********
--- page 6 ---
Q2 b.What are the steps involved in filling a polygon using the scanline method,
CO- elaborate using its special cases.
2;
BL- Solution:
2   Method: 6 marks
Special Cases: 2 marks
Diagram:2 marks
• Scanline filling is basically filling up of polygons using horizontal lines or
scanlines.
• The purpose of the SLPF algorithm is to fill (color) the interior pixels of a
polygon given only the vertices of the figure.
• This algorithm works by intersecting scanline with polygon edges and fills
the polygon between pairs of intersections.
Steps:
Step 1 − Accept the number of vertices in the polygon and the co-ordinates of
the vertices.
Step 2 − Active Edge List is prepared for each scanline intersecting the polygon
that contains the list of edges intersecting the scanline.
Step 3 −For each polygon edge in the AEL intersection points are calculated. [10]
Step 4: Sort all the edge intersecting points in increasing order of x-values.
The first x values gives the left boundary and second x value gives the right
boundary.
Step 5: Fill all the pixel positions between left and right boundary with the
specified color value.
Repeat the steps 2 to 5 for all the scanlines.
Special cases of polygon vertices:
•   If both lines intersecting at the vertex are on the same side of the scanline,
consider it as two points.
•   If lines intersecting at the vertex are at opposite sides of the scanline,
consider it as only one point.
********** 6 **********
--- page 7 ---
Q3 a. Explain the 3D viewing pipeline in computer graphics. Describe the stages
CO- involved in transforming a 3D object from world coordinates to screen
3;   coordinates. Also explain the concept of 3D clipping.
BL- Solution:
2   Component   Marks
Definition of pipeline   2
Stages explanation (6 stages) 6
3D clipping concept   2
The 3D viewing pipeline is the sequence of transformations that converts a 3D
object from its original definition into a 2D image on the screen. It transforms
coordinates from world space → viewing space → screen space.
Stages of 3D Viewing Pipeline
1. Model Transformation (Object → World Coordinates)
• Converts object coordinates into world coordinates   [10]
• Applies transformations like translation, rotation, scaling
2. Viewing Transformation (World → Eye Coordinates)
• Transforms world coordinates into view (camera) coordinates
• Defines camera position, orientation, and viewing direction
3. Projection Transformation (3D → 2D)
• Converts 3D view into a 2D representation
• Two types:
➢ Parallel Projection (orthographic)
➢ Perspective Projection (realistic depth effect)
4. Clipping
• Removes parts of objects outside the viewing volume (view frustum)
• Ensures only visible portions are processed further
5. Normalization
• Converts coordinates into a standard range (usually -1 to +1)
•   Simplifies further processing
6. Viewport Transformation (Screen Mapping)
• Maps normalized coordinates to actual screen coordinates (pixels)
• Determines final image position on display
3D clipping is the process of removing parts of objects that lie outside the
viewing volume before rendering.
Clipping Volume (View Frustum):
Defined by:
•   Left, Right
• Top, Bottom
********** 7 **********
--- page 8 ---
• Near plane
• Far plane
Purpose:
• Improves efficiency
• Avoids unnecessary rendering
• Ensures correct visibility
Q3 b.Explain the area subdivision method in detail. Discuss how recursive
CO- subdivision works and stopping conditions.
4;   Solution:
BL-   Component   Marks
2   Definition & concept 2
Working principle   2
Steps explanation   2
Recursive subdivision 1.5
Stopping conditions 2
Diagram   1
The Area Subdivision Method is a hidden surface removal technique in
computer graphics that determines visible surfaces by recursively dividing the
viewing area into smaller regions. Instead of processing individual pixels or
entire objects, it works by analyzing areas (regions) of the screen.
Working Principle
• The entire screen is treated as a single region.
• The algorithm checks whether the region:
o Contains only one surface → display it
o Contains multiple overlapping surfaces → subdivide further   [10]
👉 This process continues recursively until visibility can be clearly
determined.
🔹 Steps of the Algorithm
1. Start with Entire Viewing Area
o Consider the whole screen as one region
2. Classify Surfaces in Region
o Determine which polygons intersect or lie within the region
3. Test Visibility Conditions
o   If one surface completely covers the region → fill it
o   If no surface is present → leave it blank
4. Apply Subdivision
o   If multiple surfaces overlap, divide the region into four
smaller regions (quadtree approach)
5. Repeat Recursively
o Apply the same process to each sub-region
6. Render Final Visible Surfaces
o Continue until each region satisfies a stopping condition
Tests to determine the visibility of a single surface within a specified area are
made by comparing surfaces to the boundary of the area.
********** 8 **********
--- page 9 ---
 There are four possible relationships that a surface can have with a
specified area boundary.
➢ Surrounding surface - One that completely encloses the area.
➢ Overlapping surface - One that is partly inside and partly outside the
area.
➢ Inside surface - One that is completely inside the area.
➢ Outside surface - One that is completely outside the area.
Recursive Subdivision
• The region is divided into four equal parts repeatedly
• Each subdivision reduces ambiguity in visibility
• This forms a quadtree structure
👉 Example:
• Large region → contains 3 polygons
• Subdivide → smaller regions
• Some regions → only 1 polygon → directly visible
 The tests for determining surface visibility within an area can be
stated in terms of these four classifications.
 No further subdivisions of a specified area are needed if one of the
following conditions is true:
1. All surfaces are outside surfaces with respect to the area.
2. Only one inside, overlapping, or surrounding surface is in the area.
3. A surrounding surface obscures all other surfaces within the area
boundaries.
Q4 a. Examine the role and significance of computer graphics in: Computer-Aided
CO- Design (CAD), Entertainment Industry, Educational Technology, Scientific
3;   Visualization and AR/VR.
BL-
2   Solution:
Each application 2 marks
Computer graphics plays a crucial role in transforming data into visual content,
enabling better understanding, design, and interaction across multiple domains. [10]
Its impact is significant in fields such as Computer-Aided Design (CAD),
Entertainment, Educational Technology,   Scientific   Visualization, and
Augmented/Virtual Reality (AR/VR).
1. Computer-Aided Design (CAD)
Role:
• Used to create precise 2D and 3D models of products, buildings,
and machines
********** 9 **********
--- page 10 ---
• Enables simulation, modification, and optimization of designs
Significance:
• Improves accuracy and reduces design errors
• Saves time and cost in prototyping
• Widely used in engineering, architecture, and manufacturing
2. Entertainment Industry
Role:
• Used in animation, movies, gaming, and visual effects (VFX)
• Creates realistic characters, environments, and special effects
Significance:
• Enhances storytelling and visual appeal
• Enables immersive gaming and cinematic experiences
• Drives innovation in media and digital content
3. Educational Technology
Role:
• Provides visual simulations, animations, and virtual labs
• Helps explain complex concepts in an interactive way
Significance:
• Improves understanding and retention
• Supports remote and personalized learning
• Makes education more engaging and accessible
4. Scientific Visualization
Role:
• Converts complex data into visual formats like graphs, models, and
simulations
• Used in fields such as medicine, meteorology, and physics
Significance:
• Helps analyze large datasets effectively
• Supports research and decision-making
• Enables discovery of patterns and trends
5. Augmented Reality (AR) and Virtual Reality (VR)
Role:
• AR overlays digital content on the real world
********** 10 **********
--- page 11 ---
• VR creates fully immersive virtual environments
Significance:
• Used in training, healthcare, gaming, and education
• Enhances user interaction and experience
• Enables real-time simulation and visualization
Q4 b. Write the Midpoint Circle Algorithm. Using this algorithm, tabulate the steps
CO- for drawing a circle centered at (2, 2) with a radius of 8. Show all calculations
2;   and the points generated in each step.
BL- Solution:
3   Algorithm: 4 marks
Sum: 6 marks
[10]
********** 11 **********
--- page 12 ---
Q5 a. Explain rigid body transformations in computer graphics. Write the matrix
CO- representations for translation, rotation, and scaling using homogeneous
3;   coordinates. Show the inverse transformation matrices for each.
BL- Solution:
4   Definition: 2 marks
Normal Transformation: 4 marks
Inverse Transformations: 4 marks
Rigid body transformations are transformations that preserve shape and
size (i.e., distances and angles remain unchanged).
👉 They include:
• Translation
• Rotation
[10]
Q5 b.Write the Digital Differential Analyzer (DDA) line drawing algorithm. Using
CO- this algorithm, compute all points for the line joining (6, 3) to (12, 9). Show
2;   stepwise calculations and the final coordinates.   [10]
BL- Solution:
3   Algorithm: 4 marks
Sum: 6 marks
********** 12 **********
--- page 13 ---
Q6 a. A window is defined by coordinates (0,0) to (100,100) and a viewport is defined
CO- by (200,200) to (400,300). Derive the transformation equations, determine the
3;   scaling factors, and compute the mapped coordinates of the point (25,75). Also, [10]
BL-   illustrate the mapping of the window onto the viewport with a neat diagram and
4   steps.
********** 13 **********
--- page 14 ---
Solution:
Component   Marks
Formula derivation   2
Scaling factors   2
Numerical computation 3
Final answer   1
Diagram   2
Q6 b.Explain   perspective   projection   in   detail.
CO- Discuss one-point and two-point perspective projections with diagrams.
1;   Solution:
[10]
BL- Definition & concept 2
3   Explanation 2
One-point perspective 2
Two-point perspective   2
********** 14 **********
--- page 15 ---
Diagrams   2
Comparison / conclusion   1
Perspective projection is a method of representing a 3D object on a 2D plane
such that objects farther from the viewer appear smaller, mimicking human
visual perception.
 Another method for generating a view of a three-dimensional scene is to
project points to the display plane along converging paths.
 This causes objects farther from the viewing position to be displayed smaller
than objects of the same size that are nearer to the viewing position.
 In a perspective projection, parallel lines in a scene that are not parallel to the
display plane are projected into converging lines.
 Scenes displayed using perspective projections appear more realistic, since
this is the way that our eyes and a camera lens form images.
 The point at which a set of projected parallel lines appear to converge is
called a vanishing point.
 Each set of projected parallel lines will have a separate vanishing point and
in general a scene can have any number of vanishing points depending
on how many sets of parallel lines there are in the scene.
 The vanishing point for any set of lines that are parallel to one of the
principal axes of an object is referred to as a principal vanishing point.
1. One-Point Perspective Projection
Concept:
•   Only one vanishing point
•   Objects face the viewer directly
• Depth is along one axis
Features:
• One vanishing point on horizon
• Common in roads, railways, hallways
********** 15 **********
--- page 16 ---
•   Simple and easy to implement
2. Two-Point Perspective Projection
Concept:
• Two vanishing points
•   Object is viewed at an angle
• Depth along two axes
Features:
• Two vanishing points (left & right)
• More realistic than one-point
• Used in architectural drawings
Q7 a. Write the Cohen–Sutherland algorithm and clip the line joining:
CO- P1 = (5, 40) and P2 = (75, 95) with clipping window: xwmin = 20, ywmin =
3;   30, xwmax = 60,ywmax = 80
BL-
Solution:
3
Algorithm: 4 marks
Solution: 6 marks
[10]
********** 16 **********
--- page 17 ---
FRR ICR] AC OH
--- page 18 ---
Q7 b.A rectangle has vertices A(1,2), B(5,2), C(5,6), D(1,6).
CO- Perform the following homogeneous composite transformations and show the
3;   intermediate matrix calculations:   [10]
BL-   1. Reflection about the y-axis
3   2. Shearing in y-direction (Shy = 1)
3. Scaling with Sx = 2, Sy = 0.5
********** 18 **********
--- page 19 ---
Solution:
Component Marks
Matrices (3 transformations)   3
Matrix multiplication   3
Applying transformation   3
Final answers   1
********** 19 **********
--- page 20 ---
® Step 3: Apply Transformation

Multiply each point (x, y, 1)

Point A(1,2)
z' = —2(1) = -2
y = —0.5(1) + 0.5(2) = -0.5+1=0.5

o@ A’ = (-2, 0.5)

Point B(5,2)
zx’ = —2(5) = —10
y = —0.5(5) + 0.5(2) = -25+1=-15

@& B’ = (-10, -1.5)

® Point C(5,6)
x’ = —10
y' = —0.5(5) + 0.5(6) = -2.54+3=0.5

o@ C' = (-10, 0.5)

Point D(1,6)
zr’ =-2

y' = —0.5(1) + 0.57) = 0.5 +3 = 2.5

@ D' = (-2, 2.5)

FRI ICR DO) A RH
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper ef7a2a93ed2b

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/Integrated_Computer_7032/Computer Graphics/ANS_Computer Graphics(701CO0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: mixed (19 pages), mean OCR confidence 72.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Computer Graphics
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions attempt any 4 questions
4. All question carry equal marks
5. Answer to each new question to be started on a fresh page
6. Figures in brackets on the right hand side indicate full marks
7. Assume suitable data if necessary
Q1   Answer briefly
[20]
CO-1;   a.   Define raster scan display and random scan display. Differentiate between them.
BL-2   Solution:
Definition: 2 marks
Differentiate: 3 marks
Raster Scan Display:
Raster scan display stores picture information in a frame buffer and displays the image
by scanning the screen line by line from top to bottom. The electron beam refreshes
pixels sequentially.
Random Scan Display:
Random scan display (vector display) draws images by directing the electron beam only
to the points where lines are to be drawn instead of scanning the whole screen.
[5]
********** 1 **********
--- page 2 ---
CO-2;   b.   Explain the concept of polygon filling and describe the scanline algorithm in detail.
BL-2   Illustrate the steps involved with a suitable diagram.
Solution:
Explanation of Polygon Filling : 1 mark
Algorithm : 3 marks
Diagram: 1 mark
Polygon filling is the process of coloring or shading the interior region of a polygon
after its boundary has been drawn. In computer graphics, once the polygon edges are
displayed, the area enclosed by the edges must be filled with a specified color or
pattern.
Algorithm:
• Step 1 − Accept the number of vertices in the polygon and the co-ordinates of
the vertices.
• Step 2 − Active Edge List is prepared for each scanline intersecting the polygon
that contains the list of edges intersecting the scanline.
• Step 3 −For each polygon edge in the AEL intersection points are calculated.   [5]
• Step 4: Sort all the edge intersecting points in increasing order of x-values.
➢ The first x values gives the left boundary and second x value gives the right
boundary.
• Step 5: Fill all the pixel positions between left and right boundary with the
specified color value.
➢ Repeat the steps 2 to 5 for all the scanlines.
CO-3;   c.   Write the reflection matrices for the lines y = x and y = −x. Apply each transformation
[5]
BL-3   separately to the point (6, 2) and show the resulting coordinates.
Solution: 2.5 Marks for solving each correctly
********** 2 **********
--- page 3 ---
CO-4;   d.   Explain the concept of backface detection. How is it used in computer graphics to
BL-4   improve rendering efficiency? Illustrate with a suitable example.
Solution:
Concept: 2 marks
Rendering Efficiency: 2 marks
Example: 1 mark
Backface detection is the process of identifying and removing the surfaces (faces) of
a 3D object that are not visible to the viewer. These surfaces are called back faces
because they face away from the camera or observer.
In a 3D object, each surface has a normal vector perpendicular to the face.
[5]
The visibility of a face is determined by comparing:
• Surface normal vector (N)
• Viewing direction vector (V)
If the dot product is:
N⋅V>0 → face is visible
If
N⋅V<0 → face is hidden (back face)
********** 3 **********
--- page 4 ---
Backface detection improves performance by:
•   reducing the number of polygons to be rendered
•   saving computation time
• improving frame rate
•   reducing memory usage
For complex 3D models with thousands of polygons, many faces are hidden. By
ignoring these hidden faces, rendering becomes much faster.
Example:
Consider a cube. A cube has 6 faces. When viewed from the front, only 3 faces are
generally visible. The remaining 3 faces are back faces. Instead of rendering all 6
faces, the system renders only 3 visible faces. This reduces processing by almost 50%.
Q2   a.   Analyze the working of the Cohen–Sutherland line clipping algorithm used in computer
CO-3;   graphics. Given a line segment joining the points (10,50) and (100,20), analyze how the
BL- 3   algorithm determines the visible portion of the line when clipped against the rectangular
window defined by (20,20) and (80,80). Draw the region codes window and the diagram
demonstrating the line and the clipping window. Determine the region codes,
intersection points, and the final clipped line segment, showing all intermediate steps.
Solution:
Region codes window: 2 marks
Line Region Codes: 2 marks
Intersection Points: 6 marks
Line endpoints:
P1 = (10, 50)
P2 = (100, 20)
Clipping window:
xmin = 20
ymin = 20   [10]
xmax = 80
ymax = 80
Step 1: Find Region Codes
For P1 (10, 50): x < xmin → Left
Region code: 0001
For P2 (100, 20): x > xmax → Right
Region code: 0010
Step 2: Check Visibility
0001 AND 0010 = 0000
Result: Partially visible line → clipping required.
Step 3: Find Intersection with Left Boundary
Slope calculation:
********** 4 **********
--- page 5 ---
m = (y2 − y1) / (x2 − x1)
m = (20 − 50) / (100 − 10)
m = −30 / 90 = −1/3
Equation of line:
y − 50 = −1/3 (x − 10)
At x = 20 (left boundary):
y − 50 = −1/3 (20 − 10)
y − 50 = −10/3
y = 46.67
New point: P1' = (20, 46.67)
Step 4: Clip Right Boundary
At x = 80:
y − 50 = −1/3 (80 − 10)
y − 50 = −70/3
y = 26.67
New point: P2' = (80, 26.67)
Final Clipped Line
After clipping, the visible portion of the line is:
(20, 46.67) to (80, 26.67)
Q2 CO- b.   Explain the concept of the seed fill approach in polygon filling. Describe both boundary
2;   fill and flood fill procedures for an 8-connected region. Discuss the differences between
BL-2,   the two methods.
Solution:
Seed fill Approach: 2 marks
Boundary Fill and Flood Fill Approaches: 6 marks
Differences: 2 marks
The seed fill approach is a polygon filling technique in which a starting point (seed
point) inside the polygon is selected, and the region is filled from that point outward
until the boundary is reached.The filling process continues by checking neighboring
pixels and coloring all connected pixels that belong to the interior region.This method is
[10]
mainly used for closed regions in raster graphics.
Boundary Fill Algorithm (8-Connected Region)
The boundary fill algorithm fills a region until it encounters a specified boundary color.
It starts from a seed point inside the polygon and fills all neighboring pixels that are not
the boundary color.
BoundaryFill(x,y,fillColor,boundaryColor)
{
if pixel(x,y) != boundaryColor
and pixel(x,y) != fillColor
{
setPixel(x,y,fillColor)
********** 5 **********
--- page 6 ---
BoundaryFill(x+1,y)
BoundaryFill(x-1,y)
BoundaryFill(x,y+1)
BoundaryFill(x,y-1)
BoundaryFill(x+1,y+1)
BoundaryFill(x-1,y-1)
BoundaryFill(x+1,y-1)
BoundaryFill(x-1,y+1)
}
}
Flood Fill Algorithm (8-Connected Region)
Flood fill fills all pixels having the same old color as the seed point.It continues filling
until pixels of a different color are encountered.
FloodFill(x,y,oldColor,newColor)
{
if pixel(x,y) == oldColor
{
setPixel(x,y,newColor)
FloodFill(x+1,y)
FloodFill(x-1,y)
FloodFill(x,y+1)
FloodFill(x,y-1)
FloodFill(x+1,y+1)
FloodFill(x-1,y-1)
FloodFill(x+1,y-1)
FloodFill(x-1,y+1)
}
}
Q3 CO- a.   Define Projection in Computer Graphics. Examine the characteristics of Parallel
3;   Projection and Perspective Projection with diagram, and differentiate between them.
BL-2   Solution:
[10]
Define: 1 Mark
Parallel Projection: 3 marks
Perspective Projection: 3 marks
Differentiate: 3 marks
********** 6 **********
--- page 7 ---
A projection is the process of representing a 3D object on a 2D viewing plane
(screen).It converts 3D coordinates (x,y,z)(x, y, z)(x,y,z) into 2D coordinates (x,y)(x,
y)(x,y) so that objects can be displayed on a monitor.
Projections are mainly classified into:
1. Parallel Projection
2. Perspective Projection
Parallel Projection
In parallel projection, all projection lines (projectors) are parallel to each other
and perpendicular or inclined to the projection plane.
The center of projection is assumed to be at infinity.
Characteristics
•   Parallel projectors
• No vanishing point
• Object size remains constant irrespective of distance
• Used for engineering drawings and CAD
•   Preserves shape and dimensions
Types
Orthographic Projection
Projectors are perpendicular to the plane.
Examples:
• Front view
• Top view
• Side view
Oblique Projection
Projectors are inclined to the plane.
Examples:
********** 7 **********
--- page 8 ---
•   Cavalier projection
• Cabinet projection
Perspective Projection
In perspective projection, all projection lines converge at a single point called
the center of projection (COP).
This mimics how the human eye sees objects.
Characteristics
• Converging projectors
• One or more vanishing points
•   Distant objects appear smaller
• Gives realistic appearance
• Used in games, animation, 3D rendering
Types
• One-point perspective
• Two-point perspective
•   Three-point perspective
Q3   b.   Compare and contrast the Z-Buffer method and the Scanline method for hidden surface
CO-4;   elimination.
BL-2   Solution:
Each Method explanation: 5 marks
Difference: 5 marks
Hidden surface elimination is used in computer graphics to remove surfaces or parts of [10]
objects that are not visible to the viewer.
Two commonly used methods are:
• Z-Buffer Method
• Scanline Method
Z-Buffer Method
********** 8 **********
--- page 9 ---
The Z-buffer method (also called depth-buffer method) stores the depth value
(z-value) of every pixel in a separate buffer called the Z-buffer.
For each pixel:
• compare the current pixel’s z-value with the stored z-value
•   display the pixel with the smallest z-value (closest to viewer)
Working
1. Initialize Z-buffer with maximum depth
2. For every polygon, calculate z-value of each pixel
3. Compare with existing depth
4. Update pixel color and depth if nearer
Advantages
• Simple and widely used
•   Suitable for complex scenes
• Hardware implementation possible
2) Scanline Method
The scanline method processes the image one horizontal line at a time.
For each scanline:
• determine visible surfaces intersecting the scanline
• compare depths along that line
•   display nearest surface
It works using:
• edge tables
•   active edge lists
Working
1. Take one scanline
2. Find intersecting polygons
3. Compute visible portions
4. Draw nearest polygon segment
5. Move to next scanline
********** 9 **********
--- page 10 ---
Q4 CO- a.   Analyze the working of a Color CRT Monitor using the Beam Penetration Method and
3;   Shadow Mask Method, and compare the two techniques.
BL-2   Solution:
Methods Explanation: 6 marks
Comparison: 4 marks
A Color CRT (Cathode Ray Tube) Monitor produces color images by using
electron beams to excite phosphor-coated screens. Two main methods are used to
generate colors:
• Beam Penetration Method
• Shadow Mask Method
1. Beam Penetration Method
Working:
•   The screen is coated with multiple layers of phosphor (usually red and green).
•   A single electron beam is used.
[10]
•   By controlling the speed (energy) of the electron beam, different layers are excited:
o Low speed → excites outer layer (Red)
o   High speed → penetrates deeper (Green)
•   Intermediate speeds produce mixed colors like orange and yellow.
Features:
•   Limited color range
•   Simple design
•   Low cost
Shadow Mask Method
Working:
•   Uses three electron guns (Red, Green, Blue).
•   The screen has phosphor dots of RGB colors.
•   A shadow mask (metal plate with holes) is placed behind the screen.
•   The shadow mask ensures each electron beam hits only its corresponding color dot:
o Red gun → Red phosphor
o   Green gun → Green phosphor
o   Blue gun → Blue phosphor
********** 10 **********
--- page 11 ---
•   By combining RGB intensities, a wide range of colors is produced.
Features:
•   Produces millions of colors
•   High image quality
Beam Penetration   Shadow Mask
Basis
Method   Method
Number of electron
Single beam   Three beams (RGB)
beams
Wide range
Color capability   Limited colors
(millions)
Multiple phosphor
Screen coating   RGB phosphor dots
layers
Image quality   Lower   Higher
Cost   Cheaper   Expensive
Complexity   Simple   Complex
Raster scan
Applications   Random scan displays
displays
Q4 CO- b.   Write the Digital Differential Analyzer (DDA) line drawing algorithm. Using this
2;   algorithm, find all intermediate points for the line joining (4, 4) to (10, 10). Show all
BL-3,   calculations step by step.   [10]
Solution:
Algorithm : 5 marks
Sum: 5 marks
********** 11 **********
--- page 12 ---
Q5 CO- a.   Define homogeneous coordinates. Derive the transformation matrix for rotation about a
3;   fixed point. Explain its significance in computer graphics and illustrate with an
BL-4   example.
[10]
Solution:
Define: 2 marks
Transformation Matrix: 6 marks
Example: 2 Marks
********** 12 **********
--- page 13 ---
General Pivot Point Rotation
 Imagine rotating a polygon around a point other than the origin.
 Translate to origin
 Rotate around origin
 Translate back to center point
Q5 CO- b.   Using Midpoint Ellipse algorithm, generate an ellipse with rx = 6 and ry = 4. Tabulate
2;   all intermediate points
BL-3,   Solution:
[10]
********** 13 **********
--- page 14 ---
Q6 CO- a.   Define window and viewport. Explain window-to-viewport transformation algorithm
3;   with diagram.
BL-4   Solution:
Define: 4 marks
Algorithm: 6 marks
[10]
Algorithm:
Translate the object so that the lower left corner of the window is moved to origin.
Scale the object so that the window has the dimensions of the viewport.
Translate the object so that the scaled window area is positioned to viewport.
Q6 CO- b.   Explain 3D transformations: translation, rotation, and scaling with matrices.   [10]
1;   Solution:
********** 14 **********
--- page 15 ---
BL-3   Each Transformation: 3 marks
Define: 1 mark
3D transformations are used to change the position, size, and orientation of objects
in 3D space.
The basic transformations are:
1. Translation
2. Rotation
3. Scaling
These are represented using 4 × 4 homogeneous transformation matrices.
Rotation changes the orientation of the object.
In 3D, rotation can occur about:
•   x-axis
•   y-axis
•   z-axis
********** 15 **********
--- page 16 ---
Q7 CO- a. A   rectangle   has   vertices A(2,1), B(6,1), C(6,4), D(2,4).
3;   Perform the following homogeneous composite transformations:
BL-3   •   Scaling with Sx = 2, Sy = 2
•   Shearing in x-direction with Shx = 1
[10]
•   Translate by (-2, 1)
Solution:
Individual Matrix: 3 marks
Composite Matrix 3 marks
Final co-ordinates: 4 marks
********** 16 **********
--- page 17 ---
Step 1: Scaling Matrix
20 0
S=]0 20
001

Step 2: X-Shearing Matrix

For x-direction shearing:
110
Sh=|0 1 0
001

a’ =2+ Shy

because

yy

1 0 —2
T=|0 1 1
00 1

Since transformations are applied in this order:

Step 3: Translation Matrix

Step 4: Composite Matrix

T-Sh-S

First multiply Sh - S

1 1 0] J2 0 0
ShS=}|0 1 O} |O 2 0
0 0 1) [0 0 1

2 2 0
= |0 2 0
0 0 1

Now multiply T(SAS)

1 0 2) )2 2 0
M=j)j0 1 1 0 2 0
00 21 0 0 1

22 -2
=|]0 2 1
0 0 21

Final Composite Matrix

22 -2
M=j)0 2 1
00 1

FRR ICR] AC OH
--- page 18 ---
Q7 CO- b. A line joining the points (10,30) and (100,70) is clipped against the rectangular window
3;   defined by (20,20) to (80,60). Apply the Liang Barsky algorithm to compute the clipped
BL-3   line segment and evaluate the decision process using the parametric values obtained.
Solution:
Given Data
Line: P1(10, 30) to P2(100, 70)
Window: xmin = 20, ymin = 20, xmax = 80, ymax = 60
Viewport: (0,0) to (200,200)
[10]
2. Liang–Barsky Clipping
dx = 100 - 10 = 90
dy = 70 - 30 = 40
p1 = -90, q1 = 10 - 20 = -10
p2 = 90, q2 = 80 - 10 = 70
p3 = -40, q3 = 30 - 20 = 10
p4 = 40, q4 = 60 - 30 = 30
********** 18 **********
--- page 19 ---
t1 = max(0, q1/p1, q3/p3) = max(0, (-10/-90), (10/-40))
q1/p1 = 0.1111
q3/p3 = -0.25
t1 = max(0, 0.1111) = 0.1111
q2/p2 = 70/90 = 0.7778
q4/p4 = 30/40 = 0.75
t2 = min(1, 0.7778, 0.75) = 0.75
Since t1 ≤ t2, the line is partially visible.
3. Clipped Coordinates
At t = 0.1111:
x = 10 + 0.1111 × 90 = 20
y = 30 + 0.1111 × 40 = 34.44
Point ≈ (20, 34.44)
At t = 0.75:
x = 10 + 0.75 × 90 = 77.5
y = 30 + 0.75 × 40 = 60
Point = (77.5, 60)
********** 19 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 3b8d4df4802a

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/Integrated_DS_7038/Computer Graphics/ANS_Computer Graphics(701CO0C008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: mixed (19 pages), mean OCR confidence 72.5

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Computer Graphics
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions attempt any 4 questions
4. All question carry equal marks
5. Answer to each new question to be started on a fresh page
6. Figures in brackets on the right hand side indicate full marks
7. Assume suitable data if necessary
Q1   Answer briefly
[20]
CO-1;   a.   Define raster scan display and random scan display. Differentiate between them.
BL-2   Solution:
Definition: 2 marks
Differentiate: 3 marks
Raster Scan Display:
Raster scan display stores picture information in a frame buffer and displays the image
by scanning the screen line by line from top to bottom. The electron beam refreshes
pixels sequentially.
Random Scan Display:
Random scan display (vector display) draws images by directing the electron beam only
to the points where lines are to be drawn instead of scanning the whole screen.
[5]
********** 1 **********
--- page 2 ---
CO-2;   b.   Explain the concept of polygon filling and describe the scanline algorithm in detail.
BL-2   Illustrate the steps involved with a suitable diagram.
Solution:
Explanation of Polygon Filling : 1 mark
Algorithm : 3 marks
Diagram: 1 mark
Polygon filling is the process of coloring or shading the interior region of a polygon
after its boundary has been drawn. In computer graphics, once the polygon edges are
displayed, the area enclosed by the edges must be filled with a specified color or
pattern.
Algorithm:
• Step 1 − Accept the number of vertices in the polygon and the co-ordinates of
the vertices.
• Step 2 − Active Edge List is prepared for each scanline intersecting the polygon
that contains the list of edges intersecting the scanline.
• Step 3 −For each polygon edge in the AEL intersection points are calculated.   [5]
• Step 4: Sort all the edge intersecting points in increasing order of x-values.
➢ The first x values gives the left boundary and second x value gives the right
boundary.
• Step 5: Fill all the pixel positions between left and right boundary with the
specified color value.
➢ Repeat the steps 2 to 5 for all the scanlines.
CO-3;   c.   Write the reflection matrices for the lines y = x and y = −x. Apply each transformation
[5]
BL-3   separately to the point (6, 2) and show the resulting coordinates.
Solution: 2.5 Marks for solving each correctly
********** 2 **********
--- page 3 ---
CO-4;   d.   Explain the concept of backface detection. How is it used in computer graphics to
BL-4   improve rendering efficiency? Illustrate with a suitable example.
Solution:
Concept: 2 marks
Rendering Efficiency: 2 marks
Example: 1 mark
Backface detection is the process of identifying and removing the surfaces (faces) of
a 3D object that are not visible to the viewer. These surfaces are called back faces
because they face away from the camera or observer.
In a 3D object, each surface has a normal vector perpendicular to the face.
[5]
The visibility of a face is determined by comparing:
• Surface normal vector (N)
• Viewing direction vector (V)
If the dot product is:
N⋅V>0 → face is visible
If
N⋅V<0 → face is hidden (back face)
********** 3 **********
--- page 4 ---
Backface detection improves performance by:
•   reducing the number of polygons to be rendered
•   saving computation time
• improving frame rate
•   reducing memory usage
For complex 3D models with thousands of polygons, many faces are hidden. By
ignoring these hidden faces, rendering becomes much faster.
Example:
Consider a cube. A cube has 6 faces. When viewed from the front, only 3 faces are
generally visible. The remaining 3 faces are back faces. Instead of rendering all 6
faces, the system renders only 3 visible faces. This reduces processing by almost 50%.
Q2   a.   Analyze the working of the Cohen–Sutherland line clipping algorithm used in computer
CO-3;   graphics. Given a line segment joining the points (10,50) and (100,20), analyze how the
BL- 3   algorithm determines the visible portion of the line when clipped against the rectangular
window defined by (20,20) and (80,80). Draw the region codes window and the diagram
demonstrating the line and the clipping window. Determine the region codes,
intersection points, and the final clipped line segment, showing all intermediate steps.
Solution:
Region codes window: 2 marks
Line Region Codes: 2 marks
Intersection Points: 6 marks
Line endpoints:
P1 = (10, 50)
P2 = (100, 20)
Clipping window:
xmin = 20
ymin = 20   [10]
xmax = 80
ymax = 80
Step 1: Find Region Codes
For P1 (10, 50): x < xmin → Left
Region code: 0001
For P2 (100, 20): x > xmax → Right
Region code: 0010
Step 2: Check Visibility
0001 AND 0010 = 0000
Result: Partially visible line → clipping required.
Step 3: Find Intersection with Left Boundary
Slope calculation:
********** 4 **********
--- page 5 ---
m = (y2 − y1) / (x2 − x1)
m = (20 − 50) / (100 − 10)
m = −30 / 90 = −1/3
Equation of line:
y − 50 = −1/3 (x − 10)
At x = 20 (left boundary):
y − 50 = −1/3 (20 − 10)
y − 50 = −10/3
y = 46.67
New point: P1' = (20, 46.67)
Step 4: Clip Right Boundary
At x = 80:
y − 50 = −1/3 (80 − 10)
y − 50 = −70/3
y = 26.67
New point: P2' = (80, 26.67)
Final Clipped Line
After clipping, the visible portion of the line is:
(20, 46.67) to (80, 26.67)
Q2 CO- b.   Explain the concept of the seed fill approach in polygon filling. Describe both boundary
2;   fill and flood fill procedures for an 8-connected region. Discuss the differences between
BL-2,   the two methods.
Solution:
Seed fill Approach: 2 marks
Boundary Fill and Flood Fill Approaches: 6 marks
Differences: 2 marks
The seed fill approach is a polygon filling technique in which a starting point (seed
point) inside the polygon is selected, and the region is filled from that point outward
until the boundary is reached.The filling process continues by checking neighboring
pixels and coloring all connected pixels that belong to the interior region.This method is
[10]
mainly used for closed regions in raster graphics.
Boundary Fill Algorithm (8-Connected Region)
The boundary fill algorithm fills a region until it encounters a specified boundary color.
It starts from a seed point inside the polygon and fills all neighboring pixels that are not
the boundary color.
BoundaryFill(x,y,fillColor,boundaryColor)
{
if pixel(x,y) != boundaryColor
and pixel(x,y) != fillColor
{
setPixel(x,y,fillColor)
********** 5 **********
--- page 6 ---
BoundaryFill(x+1,y)
BoundaryFill(x-1,y)
BoundaryFill(x,y+1)
BoundaryFill(x,y-1)
BoundaryFill(x+1,y+1)
BoundaryFill(x-1,y-1)
BoundaryFill(x+1,y-1)
BoundaryFill(x-1,y+1)
}
}
Flood Fill Algorithm (8-Connected Region)
Flood fill fills all pixels having the same old color as the seed point.It continues filling
until pixels of a different color are encountered.
FloodFill(x,y,oldColor,newColor)
{
if pixel(x,y) == oldColor
{
setPixel(x,y,newColor)
FloodFill(x+1,y)
FloodFill(x-1,y)
FloodFill(x,y+1)
FloodFill(x,y-1)
FloodFill(x+1,y+1)
FloodFill(x-1,y-1)
FloodFill(x+1,y-1)
FloodFill(x-1,y+1)
}
}
Q3 CO- a.   Define Projection in Computer Graphics. Examine the characteristics of Parallel
3;   Projection and Perspective Projection with diagram, and differentiate between them.
BL-2   Solution:
[10]
Define: 1 Mark
Parallel Projection: 3 marks
Perspective Projection: 3 marks
Differentiate: 3 marks
********** 6 **********
--- page 7 ---
A projection is the process of representing a 3D object on a 2D viewing plane
(screen).It converts 3D coordinates (x,y,z)(x, y, z)(x,y,z) into 2D coordinates (x,y)(x,
y)(x,y) so that objects can be displayed on a monitor.
Projections are mainly classified into:
1. Parallel Projection
2. Perspective Projection
Parallel Projection
In parallel projection, all projection lines (projectors) are parallel to each other
and perpendicular or inclined to the projection plane.
The center of projection is assumed to be at infinity.
Characteristics
•   Parallel projectors
• No vanishing point
• Object size remains constant irrespective of distance
• Used for engineering drawings and CAD
•   Preserves shape and dimensions
Types
Orthographic Projection
Projectors are perpendicular to the plane.
Examples:
• Front view
• Top view
• Side view
Oblique Projection
Projectors are inclined to the plane.
Examples:
********** 7 **********
--- page 8 ---
•   Cavalier projection
• Cabinet projection
Perspective Projection
In perspective projection, all projection lines converge at a single point called
the center of projection (COP).
This mimics how the human eye sees objects.
Characteristics
• Converging projectors
• One or more vanishing points
•   Distant objects appear smaller
• Gives realistic appearance
• Used in games, animation, 3D rendering
Types
• One-point perspective
• Two-point perspective
•   Three-point perspective
Q3   b.   Compare and contrast the Z-Buffer method and the Scanline method for hidden surface
CO-4;   elimination.
BL-2   Solution:
Each Method explanation: 5 marks
Difference: 5 marks
Hidden surface elimination is used in computer graphics to remove surfaces or parts of [10]
objects that are not visible to the viewer.
Two commonly used methods are:
• Z-Buffer Method
• Scanline Method
Z-Buffer Method
********** 8 **********
--- page 9 ---
The Z-buffer method (also called depth-buffer method) stores the depth value
(z-value) of every pixel in a separate buffer called the Z-buffer.
For each pixel:
• compare the current pixel’s z-value with the stored z-value
•   display the pixel with the smallest z-value (closest to viewer)
Working
1. Initialize Z-buffer with maximum depth
2. For every polygon, calculate z-value of each pixel
3. Compare with existing depth
4. Update pixel color and depth if nearer
Advantages
• Simple and widely used
•   Suitable for complex scenes
• Hardware implementation possible
2) Scanline Method
The scanline method processes the image one horizontal line at a time.
For each scanline:
• determine visible surfaces intersecting the scanline
• compare depths along that line
•   display nearest surface
It works using:
• edge tables
•   active edge lists
Working
1. Take one scanline
2. Find intersecting polygons
3. Compute visible portions
4. Draw nearest polygon segment
5. Move to next scanline
********** 9 **********
--- page 10 ---
Q4 CO- a.   Analyze the working of a Color CRT Monitor using the Beam Penetration Method and
3;   Shadow Mask Method, and compare the two techniques.
BL-2   Solution:
Methods Explanation: 6 marks
Comparison: 4 marks
A Color CRT (Cathode Ray Tube) Monitor produces color images by using
electron beams to excite phosphor-coated screens. Two main methods are used to
generate colors:
• Beam Penetration Method
• Shadow Mask Method
1. Beam Penetration Method
Working:
•   The screen is coated with multiple layers of phosphor (usually red and green).
•   A single electron beam is used.
[10]
•   By controlling the speed (energy) of the electron beam, different layers are excited:
o Low speed → excites outer layer (Red)
o   High speed → penetrates deeper (Green)
•   Intermediate speeds produce mixed colors like orange and yellow.
Features:
•   Limited color range
•   Simple design
•   Low cost
Shadow Mask Method
Working:
•   Uses three electron guns (Red, Green, Blue).
•   The screen has phosphor dots of RGB colors.
•   A shadow mask (metal plate with holes) is placed behind the screen.
•   The shadow mask ensures each electron beam hits only its corresponding color dot:
o Red gun → Red phosphor
o   Green gun → Green phosphor
o   Blue gun → Blue phosphor
********** 10 **********
--- page 11 ---
•   By combining RGB intensities, a wide range of colors is produced.
Features:
•   Produces millions of colors
•   High image quality
Beam Penetration   Shadow Mask
Basis
Method   Method
Number of electron
Single beam   Three beams (RGB)
beams
Wide range
Color capability   Limited colors
(millions)
Multiple phosphor
Screen coating   RGB phosphor dots
layers
Image quality   Lower   Higher
Cost   Cheaper   Expensive
Complexity   Simple   Complex
Raster scan
Applications   Random scan displays
displays
Q4 CO- b.   Write the Digital Differential Analyzer (DDA) line drawing algorithm. Using this
2;   algorithm, find all intermediate points for the line joining (4, 4) to (10, 10). Show all
BL-3,   calculations step by step.   [10]
Solution:
Algorithm : 5 marks
Sum: 5 marks
********** 11 **********
--- page 12 ---
Q5 CO- a.   Define homogeneous coordinates. Derive the transformation matrix for rotation about a
3;   fixed point. Explain its significance in computer graphics and illustrate with an
BL-4   example.
[10]
Solution:
Define: 2 marks
Transformation Matrix: 6 marks
Example: 2 Marks
********** 12 **********
--- page 13 ---
General Pivot Point Rotation
 Imagine rotating a polygon around a point other than the origin.
 Translate to origin
 Rotate around origin
 Translate back to center point
Q5 CO- b.   Using Midpoint Ellipse algorithm, generate an ellipse with rx = 6 and ry = 4. Tabulate
2;   all intermediate points
BL-3,   Solution:
[10]
********** 13 **********
--- page 14 ---
Q6 CO- a.   Define window and viewport. Explain window-to-viewport transformation algorithm
3;   with diagram.
BL-4   Solution:
Define: 4 marks
Algorithm: 6 marks
[10]
Algorithm:
Translate the object so that the lower left corner of the window is moved to origin.
Scale the object so that the window has the dimensions of the viewport.
Translate the object so that the scaled window area is positioned to viewport.
Q6 CO- b.   Explain 3D transformations: translation, rotation, and scaling with matrices.   [10]
1;   Solution:
********** 14 **********
--- page 15 ---
BL-3   Each Transformation: 3 marks
Define: 1 mark
3D transformations are used to change the position, size, and orientation of objects
in 3D space.
The basic transformations are:
1. Translation
2. Rotation
3. Scaling
These are represented using 4 × 4 homogeneous transformation matrices.
Rotation changes the orientation of the object.
In 3D, rotation can occur about:
•   x-axis
•   y-axis
•   z-axis
********** 15 **********
--- page 16 ---
Q7 CO- a. A   rectangle   has   vertices A(2,1), B(6,1), C(6,4), D(2,4).
3;   Perform the following homogeneous composite transformations:
BL-3   •   Scaling with Sx = 2, Sy = 2
•   Shearing in x-direction with Shx = 1
[10]
•   Translate by (-2, 1)
Solution:
Individual Matrix: 3 marks
Composite Matrix 3 marks
Final co-ordinates: 4 marks
********** 16 **********
--- page 17 ---
Step 1: Scaling Matrix
20 0
S=]0 20
001

Step 2: X-Shearing Matrix

For x-direction shearing:
110
Sh=|0 1 0
001

a’ =2+ Shy

because

yy

1 0 —2
T=|0 1 1
00 1

Since transformations are applied in this order:

Step 3: Translation Matrix

Step 4: Composite Matrix

T-Sh-S

First multiply Sh - S

1 1 0] J2 0 0
ShS=}|0 1 O} |O 2 0
0 0 1) [0 0 1

2 2 0
= |0 2 0
0 0 1

Now multiply T(SAS)

1 0 2) )2 2 0
M=j)j0 1 1 0 2 0
00 21 0 0 1

22 -2
=|]0 2 1
0 0 21

Final Composite Matrix

22 -2
M=j)0 2 1
00 1

FRR ICR] AC OH
--- page 18 ---
Q7 CO- b. A line joining the points (10,30) and (100,70) is clipped against the rectangular window
3;   defined by (20,20) to (80,60). Apply the Liang Barsky algorithm to compute the clipped
BL-3   line segment and evaluate the decision process using the parametric values obtained.
Solution:
Given Data
Line: P1(10, 30) to P2(100, 70)
Window: xmin = 20, ymin = 20, xmax = 80, ymax = 60
Viewport: (0,0) to (200,200)
[10]
2. Liang–Barsky Clipping
dx = 100 - 10 = 90
dy = 70 - 30 = 40
p1 = -90, q1 = 10 - 20 = -10
p2 = 90, q2 = 80 - 10 = 70
p3 = -40, q3 = 30 - 20 = 10
p4 = 40, q4 = 60 - 30 = 30
********** 18 **********
--- page 19 ---
t1 = max(0, q1/p1, q3/p3) = max(0, (-10/-90), (10/-40))
q1/p1 = 0.1111
q3/p3 = -0.25
t1 = max(0, 0.1111) = 0.1111
q2/p2 = 70/90 = 0.7778
q4/p4 = 30/40 = 0.75
t2 = min(1, 0.7778, 0.75) = 0.75
Since t1 ≤ t2, the line is partially visible.
3. Clipped Coordinates
At t = 0.1111:
x = 10 + 0.1111 × 90 = 20
y = 30 + 0.1111 × 40 = 34.44
Point ≈ (20, 34.44)
At t = 0.75:
x = 10 + 0.75 × 90 = 77.5
y = 30 + 0.75 × 40 = 60
Point = (77.5, 60)
********** 19 **********
````

## 2024-25 · Final-Exam · Sem 6 · Answer key · paper be3442b86193

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2024/Sem_06/Final-Exam/Integrated_Computer_7032/Computer Graphics/ANS_Computer Graphics(701CO0C008)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2025
- Text: mixed (15 pages), mean OCR confidence 69.7

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Semester VI(Exam Year: 2024-2025)
Subject: Computer Graphics
Date: 05 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 15 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions attempt any 4 questions
4. In all 5 questions to be attempted
5. Answer to each new question to be started on a fresh page.
6. Figure in right hand side indicates full marks
7. Assume suitable data if necessary
Q1   Answer briefly
[20]
a. Drawing : 2 marks
Explanation: 3 marks
A Cathode Ray Tube (CRT) is a type of video display device that has been
widely used in televisions and computer monitors for several decades. The
working principle of a CRT is based on the interaction between electrons
and phosphorescent material to generate visible light.
1. Electron Gun: The CRT contains an electron gun at one end of the tube,
which generates a stream of electrons. The electron gun consists of a
heated cathode (which emits electrons), a control grid (which regulates
the flow of electrons), and an anode (which accelerates the electrons).
2. Electron Beam: When the electron gun is activated, it fires a focused
beam of electrons towards the screen of the CRT. These electrons travel
in a straight line through the vacuum inside the tube.
3. Deflection System: The electron beam is directed to specific locations [5]
on the screen by a deflection system, typically consisting of
electromagnetic coils (or in some cases, electrostatic plates). These coils
create a magnetic field that can deflect the electron beam in both the
horizontal and vertical directions. The deflection system moves the beam
across the screen in a raster scan pattern (i.e., scanning from left to right
and top to bottom, row by row).
4. Phosphorescent Coating: The inside of the CRT screen is coated with
phosphorescent material that emits light when struck by the electron
beam. In a color CRT, the phosphor coating is arranged in tiny red, green,
and blue subpixels (or phosphor dots). When the electron beam strikes the
phosphor coating, it causes the phosphor material to glow, and this glow
creates the image on the screen.
5. Image Formation: The screen is divided into a grid of rows and columns
(pixels). As the electron beam scans the screen, it activates different pixels
in different colors depending on the intensity of the electron beam. By
********** 1 **********
--- page 2 ---
varying the intensity of the electron beam and the combination of colors,
a full image can be generated.
6. Refreshing the Image: To create a continuous image, the electron beam
must scan the screen many times per second (refresh rate). Typically,
CRTs operate at refresh rates of 60 Hz to 85 Hz, meaning the image is
refreshed 60-85 times per second.
b.
•Once the polygon is entered in the display file, we can draw the outline
of the polygon.
•To show polygon as a solid object we have to set the pixel inside the
polygon as well as pixels on the boundary of it.
•Now the question is how to determine whether or not a point is inside of
a polygon.
•One simple method of doing this is to draw a line segment and count
how many intersections of the line segment with the polygon boundary
occur.   [5]
•If there are an odd number of intersections, then the point is inside,
otherwise it is outside.
•This method is called the even-odd method of determining polygon
inside points.
c. Write the relection matrix: 2 marks   [5]
Solution : 3 marks
********** 2 **********
--- page 3 ---
Similarly in Y direction;
=   -2   -5   -4
3   4   1
1   1   1
d. Explanation: 3 marks
Significance: 2 marks
1. A fast and simple object-space method for identifying the back
faces of a polyhedron is based on the "inside-outside" tests.
2. A point (x, y, z) is "inside" a polygon surface with plane
parameters A, B, C, and D if Ax + By + Cz + D < 0.
3. When an inside point is along the line of sight to the surface, the
polygon must be a back face.
4. Consider the normal vector N to a polygon surface, which has
Cartesian components (A, B, C).
5. n general, if V is a vector in the viewing direction from the eye (or [5]
"camera") position, then this polygon is a back face if V.N>0
Significance:
Backface detection is a fundamental technique in computer graphics and
is commonly used in conjunction with Z-buffering or depth sorting for
more efficient hidden surface removal. It serves as a preliminary step in
many rendering pipelines, reducing computational overhead and
improving rendering performance.
Q2   a.   Definition: 4 marks
[10]
Algorithm with matrices: 6 marks
********** 3 **********
--- page 4 ---
Window
•A world-coordinate area selected for display.
•defines what is to be viewed
Viewport
•An area on a display device to which a window is mapped.
•defines where it is to be displayed
Window to viewport transformation:
1.Translate the object so that the lower left corner of the window is moved
to origin.
2.Scale the object so that the window has the dimensions of the viewport.
3.Translate the object so that the scaled window area is positioned to
viewport.
Q2   b. Algorithm : 5 marks
Differentiate: 5 marks
FloodFill(x, y, targetColor, fillColor):
If the pixel at (x, y) is not targetColor or is already fillColor:
Return
Set the pixel at (x, y) to fillColor
FloodFill(x+1, y, targetColor, fillColor) // Right
FloodFill(x-1, y, targetColor, fillColor) // Left
FloodFill(x, y+1, targetColor, fillColor) // Down
FloodFill(x, y-1, targetColor, fillColor) // Up
[10]
Q3   a.   Projection: 2 marks
Types: 8 marks
[10]
Once the view volume is determined, a projection transformation will
convert the object in the 3D view volume to a 2D image on the projection
plane.
********** 4 **********
--- page 5 ---
Perspective
Projection:
1. Give a realistic view of 3D objects, but does not preserve shape of
object or scale.
2. Perspective images of parallel lines not parallel with projection
plane converge to a point called vanishing point.
3. Size of object is diminished with distance
4. The point at which a set of projected parallel lines appear to
converge is called a vanishing point.
5. Each set of projected parallel lines will have a separate vanishing
point and in general a scene can have any number of vanishing
points depending on how many sets of parallel lines there are in
the scene.
6. The vanishing point for any set of lines that are parallel to one of
the principal axes of an object is referred to as a principal
vanishing point.
Parallel Projection:
1. One method for generating a view of a solid object is to project
points on the object surface along parallel lines onto the display
plane.
2. By selecting different viewing positions, we can project visible
points on the object onto the display plane to obtain different two-
dimensional views of the object.
3. In a parallel projection, parallel lines in the world-coordinate scene
project into parallel lines on the two-dimensional display plane.
4. This technique is used in engineering and architectural drawings
to represent an object with a set of views that maintain relative
proportions of the object.
5. The appearance of the solid object can then be reconstructed from
the major views.
********** 5 **********
--- page 6 ---
Parallel projection is categorized into 2 main types:
1.When the direction of projection is perpendicular to the view plane it is
called as Orthographic Projection.
2. When the direction of projection is not perpendicular to the view plane
it is called as Oblique Projection.
Q3   b.
[10]
Q4   a. Rigid body transformations: 5 marks
Uniform and non-uniform scaling: 5 marks
Rigid Body Transformations - transformations that do not change the
object.
Translate
If you translate a rectangle, it is still a rectangle
Scale   [10]
If you scale a rectangle, it is still a rectangle
Rotate
If you rotate a rectangle, it is still a rectangle
•Scale - Alters the size of an object.
•Scales about a fixed point
Uniform Scaling:
********** 6 **********
--- page 7 ---
1.5 0
0 0.8

Non-Uniform Scaling

Q4

Solution: Assume that the circle is centered at origin and proceed to solve. After finding the
points add center (5, 5) to each point.
The initial point (Xo, yo)=(0,8)

Po = 1-r = 1-8=-7

(X0,Yo) = (0, 8)

Po=-7

P,=-7+2+1=-4 (-ve, case (i))

Po=-44+4+1=1

(+ve, case (ii))

P3=1+6-14+1=-6 (-ve, case (i))

K PK Xie Yast ee Yea)
1

071 8 (6,13)
142 8 (7,13)
ALG | S| (8,12)
3) 6) 4) ez (9,12)

43 5 6 (10,11)
52 6 5 (11,10)

Midpoint Circle Algorithm

1. Input radius r and circle center (x. y.), and obtain the first point on
the circumference of a circle centered on the origin as

(Xq, Yo) = (0, r)

2. Calculate the initial value of the decision parameter as
atny
ae

3. At each x, position, starting at k = 0, perform the following test: If
Px <0, the next point along the circle centered on (0, 0) is (x,.1, y) and
Prva = Prt Whnyy #1
Otherwise, the next point along the circle is (x, + 1, y, — 1) and
Prot = Pa + 2Xey + 1 Qyper

where 2x,,, = 2x, + 2and 2y.., = 2y, — 2.

4. Determine symmetry points in the other seven octants.

5. Move each calculated pixel position (x, y) onto the circular path cen-
tered on (x,, y,) and plot the coordinate values:

Z=X4% Y=¥tKh

6. Repeat steps 3 through 5 until x > y.

[10]

FIC 7 IC OHH
--- page 8 ---
Q5   a.   Rotation: 4 marks
Each axis rotation : 2 marks each
1. In general, rotations are specified by a rotation axis and an angle.
2. In two-dimensions there is only one choice of a rotation axis that
leaves points in the xy plane.
3. The easiest rotation axes are those that parallel to the coordinate
axis
4. Positive rotation angles produce counterclockwise rotations about
a coordinate axis, if we are looking along the positive half of the
axis toward the coordinate origin
5.
[10]
********** 8 **********
--- page 9 ---
Q5 b. Sol: Since the line has a slope m=3/8 =0.375 the following set of equations would be
valid
Po=2Ay-Ax, Ay=3, Ax=8
Po=6-8=-2
Represent first pixel as (Xo, Yo) =(2,2).
Po=-2, since, Po —ve use case (i) i.e. next pixel is (X1,Y1) =(Xo+1,Yo)=(3,2) and
Compute P; =Pp +2*3 = -2+6=4, P, +ve use case (ii)

K | Px | Xket | Yor

0 | -2 3 2

1 | 4 4 3

[10]
Bresenham’s Line-Drawing Algorithm for |m| <1
1. Input the two line endpoints and store the left endpoint in (xp, yq)-
2. Load (xo, y9) into the frame buffer; that is, plot the first point.
3. Calculate constants Ax, dy, 24y, and ZAy — 2Ax, and obtain the start-
ing value for the decision parameter as.
Po = 2ay ~ Ax
4. Ateach x, along the line, starting at k = 0, perform the following test:
If p, < 0, the next point to plot is (x, + 1, y,) and
Pas = Pe + 2Ay
Otherwise, the next point to plot is (x, + 1, yj, + 1) and |
Pony = Pe + 2hy ~ Jay |
5. Repeat step 4 Ax times.
Q6 a. | Algorithm : 4 marks [10]

Sum: 6 Marks

FIC QF OH ar
--- page 10 ---
Algorithm:

1. Define the line equation in parametric form:
r=2,+t(r2— 21)
y= tt(yo—m)

where ft varies from 0 to 1, representing points along the line segment.
2. Compute the direction components:
dr=2,—a%, dy=y-m
3. Determine the four possible edge constraints of the clipping window:
e Left boundary: 2,;, = 1 - py = —dz, qy = ©, — Prin
e Right boundary: 2ynax = 6 — po = d&, go = Bax — 21
© Bottom boundary: ymin = 1 - ps = —dy. gg = yi — Ymin
© Top boundary: Yinax = 4 ps = dy. ds = Yinax — Yt
4. Compute the values of foptor aNd Lexie?
e lf pi < 0, compute t = q;/p; (potential entry)
¢ If p; > 0, compute t = q;/p; (potential exit)
e If p; = Oandq; < 0, the line is completely outside.
5. Find the largest t..,:.. and the smallest ¢,..:¢-
© lf tonter > texit- the line is completely outside.

e¢ Otherwise, compute the new clipped line coordinates.

Step-by-Step Analysis of Given Line:
Given Data:
«Line: P(2,3) to Q(8,5)
© Clipping Window: (min = 1, Yimin = 1) to (max = 6, Ymax = 4)
Step 1: Compute dz and dy
dx =2.—-2,=8-—-2=6
dy=y-y=5-3=2

Step 2: Compute p; and q;

Boundary Pi Gi t=#

Left (x = 1) —dx = -6 21 —2min =2-1=1 t = 4, = -0.167

Right (2 = 6) dz =6 2max —21=6-2=4 ty = 4 = 0.667

Bottom (y = 1) —dy = -2 Yi — Ymin =3-1=2

Top (y = 4) dy =2 Yax — yi =4—-3=1 &=4=05
For P<0,

T1l= max(0,-0.167,-1.0)=0

For P>0O
T2=min(1, 0.667,0.5) =0.5

FRR ICR 7 OI HOH
--- page 11 ---
As t1<t2
X’=x1+ t1*dx   y’=y1+ t1*dy
X’= 2   y’=3
X”= x1+t2*dx   Y”= y1+t2*dy
X”=2+0.5(6)=5   Y”= 3+ 0.5(2) = 4
Q6   b. A Raster Scan Display is a type of display technology used in most
modern monitors, including CRT (Cathode Ray Tube), LCD, and LED
screens. The term "raster" refers to the rectangular grid or pattern of lines
that make up the screen, and raster scan refers to the method by which
images are generated by systematically scanning the screen line by line in
a specific order.
How Raster Scan Display Works to Generate Images:
The process of generating an image on a raster scan display involves
several steps, where the electron beam (in CRT displays) or pixels (in flat-
panel displays) are sequentially activated to produce the final image. The
process can be broken down into the following key steps:
1. Screen Division into Pixels (Raster Grid):
○ The screen is divided into a grid of pixels (short for "picture elements").
A pixel is the smallest unit of a display, typically represented by a
combination of red, green, and blue subpixels in color displays.
○ In a CRT monitor, this grid is composed of tiny phosphor dots that emit
light when struck by the electron beam. In flat-panel displays, each pixel
is made of liquid crystals or LEDs that can change their color or
brightness.
2. Scanning the Screen:
○ The image is generated by scanning the screen with a raster pattern,
meaning the screen is refreshed row by row, starting from the top left and
moving horizontally across the screen. Once the rightmost column of the [10]
screen is reached, the scan continues by moving to the next line below (to
the leftmost side) and repeats the process.
○ This method of scanning is similar to how a printer scans and fills in
each line of text or image sequentially.
3. Electron Beam (in CRT):
○ In a CRT monitor, an electron gun fires an electron beam at the screen.
The beam is directed by electromagnetic coils to different positions on the
screen.
○ The beam is directed horizontally across the screen (line by line) in a
left-to-right motion. After completing one line, the beam moves vertically
down to the next line and repeats the scanning.
○ The CRT screen’s phosphor coating emits light when hit by the electron
beam, creating a visible image on the screen.
4.   Frame Buffer and Pixel Data: ○ The image displayed on a raster
scan display is typically stored in a frame buffer, which is a portion of
memory that holds the pixel data for the image. ○ Each pixel in the buffer
corresponds to a particular location on the screen, and its value
determines the color or intensity of that pixel. The frame buffer stores
the color information for every pixel, and the display
5.   Refresh Rate: ○ The process of scanning the screen is repeated
multiple times per second. The number of times the screen is scanned
and updated per second is known as the refresh rate. Common refresh
rates are 60 Hz (60 times per second) to 85 Hz or higher. ○ At high
********** 11 **********
--- page 12 ---
refresh rates, the human eye perceives a smooth, continuous image with
no flickering, but at lower refresh rates, flickering may become
noticeable.
6.   Interlaced vs. Progressive Scan: ○ Interlaced scanning: In older
CRT displays, the screen would be scanned in two passes—first by
displaying all the odd-numbered lines, and then the even-numbered lines.
This method reduces the amount of data needed to generate each frame
but can result in visual artifacts like "interlace flicker." ○ Progressive
scanning: Modern displays use progressive scanning, where every line of
the screen is drawn sequentially in one pass. This results in a smoother
and clearer image, with no flicker.
Steps in a Raster Scan Display:
1. Electron Beam Activation (CRT Displays):
○ The electron gun fires the beam at the top-left corner of the screen (the
first pixel). As the beam moves across the screen, it hits the phosphor
layer, and each pixel is illuminated based on the information stored in the
frame buffer.
2. Horizontal Scanning:
○ The electron beam moves horizontally from left to right along each row
of pixels, activating the pixels based on their color data (red, green, and
blue components) stored in memory.
3. Vertical Scanning:
○ Once the beam reaches the rightmost side of the screen, it quickly
returns to the leftmost side and moves down to the next row of pixels.
This process continues until the entire screen has been scanned (from top
to bottom).
4. Refresh:
○ After the electron beam completes scanning the entire screen, the image
is refreshed by scanning the screen again to ensure continuous display,
especially at high refresh rates for smooth image updates.
********** 12 **********
--- page 13 ---
Q7

a.

Rotation Matrix

The 90° clockwise rotation matrix is:

0 10
R=]-1 00
0 01

Rectangle Matrix Representation

Matrix Multiplication

(Ox 1+1x 1)
= |(-1x14+0x1)
1

Scaling Matrix

The scaling transformation for

Matrix Multiplication

(2x 1+0x -1)
=|(x1+3x-1)
1

Translation Matrix

The translation matrix for shifting by

Matrix Multiplication

1
= |0
0

(1x 2+0x-3+3x1)
= |(0x2+1x-3+2x1)
1

1441
P=}]1 13 3
Piddl

P'=RxP

0 10 1441
=|-1 0 0] xJ]1 13 3
0 OL Pidd

(0x4+1x1) (0x4+4+1x3) (0x14+1x3)
(-1x4+0x1) (-1x4+0x3) (-1x1+0x3)

1 1

1 1 3 3
=|-l1 -4 -4 -1
1 1 1 1

Sp = 2,8, =3is:
20 0
S=|]0 3 0
001
P"=S xP
200 1 1 3 3
0 3 O}| x |-1 -4 -4 -1
001 ne a el

1

(2x14+0x-4) (2x3+0x-4) (2x3+0x-1)
(Ox1+3x—4) (0x3+3x -4) (0x3+3x-1)

1 1

2 2 6 6
= |-3 —-12 -12
1 1 1 1

(+3, +2) is:
103
T=|0 1 2
001
PU_ Ty Pp"

0 3 2 2 6 6
1 2) x ]-3 —-12 -12 -3
ol 1 1 1 1

(Lx 2+0x-12+3x1) (1x6+0x -12+3x 1)
(0x 24+1x-124+2x1) (0x6+1x-124+2x1)
1 1

5 5 9 9
=]|-1 -10 -10 -1
1 1 1 1

1

(1x 6+0x -3+3x1)
(0x 6+1x -3+2x1)
1

[10]

FIR ICR 7] QI HO
--- page 14 ---
Qi b.

[10]

RK KKK RK KK 14 2h KKK RK Kk KK
--- page 15 ---
RK KKK RK KK 15 2h KKK RK Kk KK
````

## 2024-25 · Final-Exam · Sem 6 · Answer key · paper 1b945c5aec69

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2024/Sem_06/Final-Exam/Integrated_DS_7038/Computer Graphics/ANS_Computer Graphics(701CO0C008)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2025
- Text: mixed (15 pages), mean OCR confidence 69.7

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Semester VI(Exam Year: 2024-2025)
Subject: Computer Graphics
Date: 05 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 15 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions attempt any 4 questions
4. In all 5 questions to be attempted
5. Answer to each new question to be started on a fresh page.
6. Figure in right hand side indicates full marks
7. Assume suitable data if necessary
Q1   Answer briefly
[20]
a. Drawing : 2 marks
Explanation: 3 marks
A Cathode Ray Tube (CRT) is a type of video display device that has been
widely used in televisions and computer monitors for several decades. The
working principle of a CRT is based on the interaction between electrons
and phosphorescent material to generate visible light.
1. Electron Gun: The CRT contains an electron gun at one end of the tube,
which generates a stream of electrons. The electron gun consists of a
heated cathode (which emits electrons), a control grid (which regulates
the flow of electrons), and an anode (which accelerates the electrons).
2. Electron Beam: When the electron gun is activated, it fires a focused
beam of electrons towards the screen of the CRT. These electrons travel
in a straight line through the vacuum inside the tube.
3. Deflection System: The electron beam is directed to specific locations [5]
on the screen by a deflection system, typically consisting of
electromagnetic coils (or in some cases, electrostatic plates). These coils
create a magnetic field that can deflect the electron beam in both the
horizontal and vertical directions. The deflection system moves the beam
across the screen in a raster scan pattern (i.e., scanning from left to right
and top to bottom, row by row).
4. Phosphorescent Coating: The inside of the CRT screen is coated with
phosphorescent material that emits light when struck by the electron
beam. In a color CRT, the phosphor coating is arranged in tiny red, green,
and blue subpixels (or phosphor dots). When the electron beam strikes the
phosphor coating, it causes the phosphor material to glow, and this glow
creates the image on the screen.
5. Image Formation: The screen is divided into a grid of rows and columns
(pixels). As the electron beam scans the screen, it activates different pixels
in different colors depending on the intensity of the electron beam. By
********** 1 **********
--- page 2 ---
varying the intensity of the electron beam and the combination of colors,
a full image can be generated.
6. Refreshing the Image: To create a continuous image, the electron beam
must scan the screen many times per second (refresh rate). Typically,
CRTs operate at refresh rates of 60 Hz to 85 Hz, meaning the image is
refreshed 60-85 times per second.
b.
•Once the polygon is entered in the display file, we can draw the outline
of the polygon.
•To show polygon as a solid object we have to set the pixel inside the
polygon as well as pixels on the boundary of it.
•Now the question is how to determine whether or not a point is inside of
a polygon.
•One simple method of doing this is to draw a line segment and count
how many intersections of the line segment with the polygon boundary
occur.   [5]
•If there are an odd number of intersections, then the point is inside,
otherwise it is outside.
•This method is called the even-odd method of determining polygon
inside points.
c. Write the relection matrix: 2 marks   [5]
Solution : 3 marks
********** 2 **********
--- page 3 ---
Similarly in Y direction;
=   -2   -5   -4
3   4   1
1   1   1
d. Explanation: 3 marks
Significance: 2 marks
1. A fast and simple object-space method for identifying the back
faces of a polyhedron is based on the "inside-outside" tests.
2. A point (x, y, z) is "inside" a polygon surface with plane
parameters A, B, C, and D if Ax + By + Cz + D < 0.
3. When an inside point is along the line of sight to the surface, the
polygon must be a back face.
4. Consider the normal vector N to a polygon surface, which has
Cartesian components (A, B, C).
5. n general, if V is a vector in the viewing direction from the eye (or [5]
"camera") position, then this polygon is a back face if V.N>0
Significance:
Backface detection is a fundamental technique in computer graphics and
is commonly used in conjunction with Z-buffering or depth sorting for
more efficient hidden surface removal. It serves as a preliminary step in
many rendering pipelines, reducing computational overhead and
improving rendering performance.
Q2   a.   Definition: 4 marks
[10]
Algorithm with matrices: 6 marks
********** 3 **********
--- page 4 ---
Window
•A world-coordinate area selected for display.
•defines what is to be viewed
Viewport
•An area on a display device to which a window is mapped.
•defines where it is to be displayed
Window to viewport transformation:
1.Translate the object so that the lower left corner of the window is moved
to origin.
2.Scale the object so that the window has the dimensions of the viewport.
3.Translate the object so that the scaled window area is positioned to
viewport.
Q2   b. Algorithm : 5 marks
Differentiate: 5 marks
FloodFill(x, y, targetColor, fillColor):
If the pixel at (x, y) is not targetColor or is already fillColor:
Return
Set the pixel at (x, y) to fillColor
FloodFill(x+1, y, targetColor, fillColor) // Right
FloodFill(x-1, y, targetColor, fillColor) // Left
FloodFill(x, y+1, targetColor, fillColor) // Down
FloodFill(x, y-1, targetColor, fillColor) // Up
[10]
Q3   a.   Projection: 2 marks
Types: 8 marks
[10]
Once the view volume is determined, a projection transformation will
convert the object in the 3D view volume to a 2D image on the projection
plane.
********** 4 **********
--- page 5 ---
Perspective
Projection:
1. Give a realistic view of 3D objects, but does not preserve shape of
object or scale.
2. Perspective images of parallel lines not parallel with projection
plane converge to a point called vanishing point.
3. Size of object is diminished with distance
4. The point at which a set of projected parallel lines appear to
converge is called a vanishing point.
5. Each set of projected parallel lines will have a separate vanishing
point and in general a scene can have any number of vanishing
points depending on how many sets of parallel lines there are in
the scene.
6. The vanishing point for any set of lines that are parallel to one of
the principal axes of an object is referred to as a principal
vanishing point.
Parallel Projection:
1. One method for generating a view of a solid object is to project
points on the object surface along parallel lines onto the display
plane.
2. By selecting different viewing positions, we can project visible
points on the object onto the display plane to obtain different two-
dimensional views of the object.
3. In a parallel projection, parallel lines in the world-coordinate scene
project into parallel lines on the two-dimensional display plane.
4. This technique is used in engineering and architectural drawings
to represent an object with a set of views that maintain relative
proportions of the object.
5. The appearance of the solid object can then be reconstructed from
the major views.
********** 5 **********
--- page 6 ---
Parallel projection is categorized into 2 main types:
1.When the direction of projection is perpendicular to the view plane it is
called as Orthographic Projection.
2. When the direction of projection is not perpendicular to the view plane
it is called as Oblique Projection.
Q3   b.
[10]
Q4   a. Rigid body transformations: 5 marks
Uniform and non-uniform scaling: 5 marks
Rigid Body Transformations - transformations that do not change the
object.
Translate
If you translate a rectangle, it is still a rectangle
Scale   [10]
If you scale a rectangle, it is still a rectangle
Rotate
If you rotate a rectangle, it is still a rectangle
•Scale - Alters the size of an object.
•Scales about a fixed point
Uniform Scaling:
********** 6 **********
--- page 7 ---
1.5 0
0 0.8

Non-Uniform Scaling

Q4

Solution: Assume that the circle is centered at origin and proceed to solve. After finding the
points add center (5, 5) to each point.
The initial point (Xo, yo)=(0,8)

Po = 1-r = 1-8=-7

(X0,Yo) = (0, 8)

Po=-7

P,=-7+2+1=-4 (-ve, case (i))

Po=-44+4+1=1

(+ve, case (ii))

P3=1+6-14+1=-6 (-ve, case (i))

K PK Xie Yast ee Yea)
1

071 8 (6,13)
142 8 (7,13)
ALG | S| (8,12)
3) 6) 4) ez (9,12)

43 5 6 (10,11)
52 6 5 (11,10)

Midpoint Circle Algorithm

1. Input radius r and circle center (x. y.), and obtain the first point on
the circumference of a circle centered on the origin as

(Xq, Yo) = (0, r)

2. Calculate the initial value of the decision parameter as
atny
ae

3. At each x, position, starting at k = 0, perform the following test: If
Px <0, the next point along the circle centered on (0, 0) is (x,.1, y) and
Prva = Prt Whnyy #1
Otherwise, the next point along the circle is (x, + 1, y, — 1) and
Prot = Pa + 2Xey + 1 Qyper

where 2x,,, = 2x, + 2and 2y.., = 2y, — 2.

4. Determine symmetry points in the other seven octants.

5. Move each calculated pixel position (x, y) onto the circular path cen-
tered on (x,, y,) and plot the coordinate values:

Z=X4% Y=¥tKh

6. Repeat steps 3 through 5 until x > y.

[10]

FIC 7 IC OHH
--- page 8 ---
Q5   a.   Rotation: 4 marks
Each axis rotation : 2 marks each
1. In general, rotations are specified by a rotation axis and an angle.
2. In two-dimensions there is only one choice of a rotation axis that
leaves points in the xy plane.
3. The easiest rotation axes are those that parallel to the coordinate
axis
4. Positive rotation angles produce counterclockwise rotations about
a coordinate axis, if we are looking along the positive half of the
axis toward the coordinate origin
5.
[10]
********** 8 **********
--- page 9 ---
Q5 b. Sol: Since the line has a slope m=3/8 =0.375 the following set of equations would be
valid
Po=2Ay-Ax, Ay=3, Ax=8
Po=6-8=-2
Represent first pixel as (Xo, Yo) =(2,2).
Po=-2, since, Po —ve use case (i) i.e. next pixel is (X1,Y1) =(Xo+1,Yo)=(3,2) and
Compute P; =Pp +2*3 = -2+6=4, P, +ve use case (ii)

K | Px | Xket | Yor

0 | -2 3 2

1 | 4 4 3

[10]
Bresenham’s Line-Drawing Algorithm for |m| <1
1. Input the two line endpoints and store the left endpoint in (xp, yq)-
2. Load (xo, y9) into the frame buffer; that is, plot the first point.
3. Calculate constants Ax, dy, 24y, and ZAy — 2Ax, and obtain the start-
ing value for the decision parameter as.
Po = 2ay ~ Ax
4. Ateach x, along the line, starting at k = 0, perform the following test:
If p, < 0, the next point to plot is (x, + 1, y,) and
Pas = Pe + 2Ay
Otherwise, the next point to plot is (x, + 1, yj, + 1) and |
Pony = Pe + 2hy ~ Jay |
5. Repeat step 4 Ax times.
Q6 a. | Algorithm : 4 marks [10]

Sum: 6 Marks

FIC QF OH ar
--- page 10 ---
Algorithm:

1. Define the line equation in parametric form:
r=2,+t(r2— 21)
y= tt(yo—m)

where ft varies from 0 to 1, representing points along the line segment.
2. Compute the direction components:
dr=2,—a%, dy=y-m
3. Determine the four possible edge constraints of the clipping window:
e Left boundary: 2,;, = 1 - py = —dz, qy = ©, — Prin
e Right boundary: 2ynax = 6 — po = d&, go = Bax — 21
© Bottom boundary: ymin = 1 - ps = —dy. gg = yi — Ymin
© Top boundary: Yinax = 4 ps = dy. ds = Yinax — Yt
4. Compute the values of foptor aNd Lexie?
e lf pi < 0, compute t = q;/p; (potential entry)
¢ If p; > 0, compute t = q;/p; (potential exit)
e If p; = Oandq; < 0, the line is completely outside.
5. Find the largest t..,:.. and the smallest ¢,..:¢-
© lf tonter > texit- the line is completely outside.

e¢ Otherwise, compute the new clipped line coordinates.

Step-by-Step Analysis of Given Line:
Given Data:
«Line: P(2,3) to Q(8,5)
© Clipping Window: (min = 1, Yimin = 1) to (max = 6, Ymax = 4)
Step 1: Compute dz and dy
dx =2.—-2,=8-—-2=6
dy=y-y=5-3=2

Step 2: Compute p; and q;

Boundary Pi Gi t=#

Left (x = 1) —dx = -6 21 —2min =2-1=1 t = 4, = -0.167

Right (2 = 6) dz =6 2max —21=6-2=4 ty = 4 = 0.667

Bottom (y = 1) —dy = -2 Yi — Ymin =3-1=2

Top (y = 4) dy =2 Yax — yi =4—-3=1 &=4=05
For P<0,

T1l= max(0,-0.167,-1.0)=0

For P>0O
T2=min(1, 0.667,0.5) =0.5

FRR ICR 7 OI HOH
--- page 11 ---
As t1<t2
X’=x1+ t1*dx   y’=y1+ t1*dy
X’= 2   y’=3
X”= x1+t2*dx   Y”= y1+t2*dy
X”=2+0.5(6)=5   Y”= 3+ 0.5(2) = 4
Q6   b. A Raster Scan Display is a type of display technology used in most
modern monitors, including CRT (Cathode Ray Tube), LCD, and LED
screens. The term "raster" refers to the rectangular grid or pattern of lines
that make up the screen, and raster scan refers to the method by which
images are generated by systematically scanning the screen line by line in
a specific order.
How Raster Scan Display Works to Generate Images:
The process of generating an image on a raster scan display involves
several steps, where the electron beam (in CRT displays) or pixels (in flat-
panel displays) are sequentially activated to produce the final image. The
process can be broken down into the following key steps:
1. Screen Division into Pixels (Raster Grid):
○ The screen is divided into a grid of pixels (short for "picture elements").
A pixel is the smallest unit of a display, typically represented by a
combination of red, green, and blue subpixels in color displays.
○ In a CRT monitor, this grid is composed of tiny phosphor dots that emit
light when struck by the electron beam. In flat-panel displays, each pixel
is made of liquid crystals or LEDs that can change their color or
brightness.
2. Scanning the Screen:
○ The image is generated by scanning the screen with a raster pattern,
meaning the screen is refreshed row by row, starting from the top left and
moving horizontally across the screen. Once the rightmost column of the [10]
screen is reached, the scan continues by moving to the next line below (to
the leftmost side) and repeats the process.
○ This method of scanning is similar to how a printer scans and fills in
each line of text or image sequentially.
3. Electron Beam (in CRT):
○ In a CRT monitor, an electron gun fires an electron beam at the screen.
The beam is directed by electromagnetic coils to different positions on the
screen.
○ The beam is directed horizontally across the screen (line by line) in a
left-to-right motion. After completing one line, the beam moves vertically
down to the next line and repeats the scanning.
○ The CRT screen’s phosphor coating emits light when hit by the electron
beam, creating a visible image on the screen.
4.   Frame Buffer and Pixel Data: ○ The image displayed on a raster
scan display is typically stored in a frame buffer, which is a portion of
memory that holds the pixel data for the image. ○ Each pixel in the buffer
corresponds to a particular location on the screen, and its value
determines the color or intensity of that pixel. The frame buffer stores
the color information for every pixel, and the display
5.   Refresh Rate: ○ The process of scanning the screen is repeated
multiple times per second. The number of times the screen is scanned
and updated per second is known as the refresh rate. Common refresh
rates are 60 Hz (60 times per second) to 85 Hz or higher. ○ At high
********** 11 **********
--- page 12 ---
refresh rates, the human eye perceives a smooth, continuous image with
no flickering, but at lower refresh rates, flickering may become
noticeable.
6.   Interlaced vs. Progressive Scan: ○ Interlaced scanning: In older
CRT displays, the screen would be scanned in two passes—first by
displaying all the odd-numbered lines, and then the even-numbered lines.
This method reduces the amount of data needed to generate each frame
but can result in visual artifacts like "interlace flicker." ○ Progressive
scanning: Modern displays use progressive scanning, where every line of
the screen is drawn sequentially in one pass. This results in a smoother
and clearer image, with no flicker.
Steps in a Raster Scan Display:
1. Electron Beam Activation (CRT Displays):
○ The electron gun fires the beam at the top-left corner of the screen (the
first pixel). As the beam moves across the screen, it hits the phosphor
layer, and each pixel is illuminated based on the information stored in the
frame buffer.
2. Horizontal Scanning:
○ The electron beam moves horizontally from left to right along each row
of pixels, activating the pixels based on their color data (red, green, and
blue components) stored in memory.
3. Vertical Scanning:
○ Once the beam reaches the rightmost side of the screen, it quickly
returns to the leftmost side and moves down to the next row of pixels.
This process continues until the entire screen has been scanned (from top
to bottom).
4. Refresh:
○ After the electron beam completes scanning the entire screen, the image
is refreshed by scanning the screen again to ensure continuous display,
especially at high refresh rates for smooth image updates.
********** 12 **********
--- page 13 ---
Q7

a.

Rotation Matrix

The 90° clockwise rotation matrix is:

0 10
R=]-1 00
0 01

Rectangle Matrix Representation

Matrix Multiplication

(Ox 1+1x 1)
= |(-1x14+0x1)
1

Scaling Matrix

The scaling transformation for

Matrix Multiplication

(2x 1+0x -1)
=|(x1+3x-1)
1

Translation Matrix

The translation matrix for shifting by

Matrix Multiplication

1
= |0
0

(1x 2+0x-3+3x1)
= |(0x2+1x-3+2x1)
1

1441
P=}]1 13 3
Piddl

P'=RxP

0 10 1441
=|-1 0 0] xJ]1 13 3
0 OL Pidd

(0x4+1x1) (0x4+4+1x3) (0x14+1x3)
(-1x4+0x1) (-1x4+0x3) (-1x1+0x3)

1 1

1 1 3 3
=|-l1 -4 -4 -1
1 1 1 1

Sp = 2,8, =3is:
20 0
S=|]0 3 0
001
P"=S xP
200 1 1 3 3
0 3 O}| x |-1 -4 -4 -1
001 ne a el

1

(2x14+0x-4) (2x3+0x-4) (2x3+0x-1)
(Ox1+3x—4) (0x3+3x -4) (0x3+3x-1)

1 1

2 2 6 6
= |-3 —-12 -12
1 1 1 1

(+3, +2) is:
103
T=|0 1 2
001
PU_ Ty Pp"

0 3 2 2 6 6
1 2) x ]-3 —-12 -12 -3
ol 1 1 1 1

(Lx 2+0x-12+3x1) (1x6+0x -12+3x 1)
(0x 24+1x-124+2x1) (0x6+1x-124+2x1)
1 1

5 5 9 9
=]|-1 -10 -10 -1
1 1 1 1

1

(1x 6+0x -3+3x1)
(0x 6+1x -3+2x1)
1

[10]

FIR ICR 7] QI HO
--- page 14 ---
Qi b.

[10]

RK KKK RK KK 14 2h KKK RK Kk KK
--- page 15 ---
RK KKK RK KK 15 2h KKK RK Kk KK
````

## 2024-25 · Re-Exam · Sem 6 · Answer key · paper 48755d8f1313

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/Integrated_Computer_7032/Computer Graphics/ANS_Computer Graphics(701CO0C008)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Jul 2025
- Text: mixed (15 pages), mean OCR confidence 75.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech Intg. (CE)/B. Tech Intg. (DS)
Year: III/Sem 6 Re-exam(Exam Year: 2024-2025)
Subject: Computer Graphics
Date: 07 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 15 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions attempt any 4 questions
4. In all 5 questions to be attempted
5. Answer to each new question to be started on a fresh page.
6. Figure in right hand side indicates full marks
7. Assume suitable data if necessary
Q1   Answer briefly
[20]
a. Each definition: 1 mark each
At the end of each scan line, the electron beam returns to the left side of the screen
to begin displaying the next scan line. The return to the left of the screen, after
refreshing each scan line is called the horizontal retrace. And at the end of each
frame, the electron beam returns to the top left corner of the screen to begin the next
frame is called the vertical retrace.
b. The maximum number of points that can be displayed without overlap on a CRT
is referred to as the resolution.
c. Scan Conversion is the process of converting digital images, which are
represented in terms of pixel-based data (such as images created using computer [5]
graphics), into a format that can be displayed on devices like a CRT (Cathode Ray
Tube) or other display devices. It involves converting vector graphics or geometric
shapes (such as lines, circles, and polygons) into a raster format (a grid of pixels),
which can then be displayed on a screen. In simpler terms, scan conversion is the
method used to translate the mathematical representation of an image (often a set of
coordinates and geometric data) into a rasterized form where the image is
represented by pixels on a display.
d. Pixel or Pel is defined as "the smallest addressable screen element"
e. The frame buffer is the video memory (RAM) that is used to hold or map the
image displayed on the screen. OR A framebuffer (frame buffer, or sometimes
framestore) is a portion of RAM containing a bitmap that drives a video display.
b Aspect ratio is a number which gives the ratio of vertical points to horizontal points
.   necessary to produce equal length lines in both directions on the screen. An aspect [5]
ratio of ¾ means that a vertical line plotted with three points has the same length as
a horizontal line plotted with 4 points. It is Ratio of width to height. Some standard
********** 1 **********
--- page 2 ---
aspect ratios are ex: 4:3, 16:9. These settings can be commonly noticed on
Television displays.
c.
[5]
d The Scanline method is an image-space algorithm used in hidden surface
.   elimination to determine which surfaces of 3D objects are visible in a scene. It
processes the image one horizontal scanline at a time, comparing depth values of
[5]
overlapping surfaces to determine which surface should be displayed at each pixel.
Working Principle
1. Divide the image into scanlines: The entire viewport is divided into
horizontal scanlines, each corresponding to a row of pixels.
********** 2 **********
--- page 3 ---
2. Process active polygons: For each scanline, identify which polygons intersect
it.
3. Sort by depth (Z-values): Compare the depth (Z-value) of overlapping
polygons at each pixel along the scanline.
4. Render the visible surface: The pixel is assigned the color of the nearest
polygon at that point.
5. Continue to the next scanline: The process repeats until all scanlines are
processed.
Advantages of the Scanline Method
✅ Efficient for scenes with overlapping polygons: Unlike Z-buffering, which
processes every pixel independently, the Scanline method processes multiple pixels
at once, making it more memory-efficient.
✅ Reduces redundant calculations: Since scanlines are processed in sequence,
shared edges between adjacent scanlines do not need to be recalculated.
✅ Handles multiple surfaces at each scanline: Unlike painter’s algorithm, which
sorts objects and draws them back to front, the scanline method resolves visibility
at each pixel level.
Limitations of the Scanline Method
❌ Not suitable for curved surfaces: Works well with polygonal surfaces but requires
additional techniques to handle curved objects.
❌ More complex than Z-buffering: Requires sorting and depth calculations for each
scanline, making it harder to implement compared to simpler algorithms like Z-
buffering.
❌ Difficulties with transparency and shadows: Since it works at the scanline level,
handling semi-transparent objects or self-shadowing can be complex.
********** 3 **********
--- page 4 ---
Q2

a.

DDA Line Algorithm

1. Read the line end points (x, y;) and (xa, y) such that they are not equal.
(if equal then plot that point and exit]
2 dx=|x,-x] and dy=|y_-y,|
3. if(Ax2Ay) then
length = Ax
else
length = Ay
end if
4. Ax =(x,—x,)/length
Ay = (¥p—y,)/length
{This makes either Ax or Ay equal to 1 because length is either |x,
or ly¥2 - yi]. Therefore, the incremental value for either x or yisoa
5. x =x, + 0.5 * Sign (Ax)
y =y, + 0.5 * Sign (Ay)

(Here, Sign function makes the algorithm work in all quadrant
returns - 1, 0, 1 depending on whether its argument is < 0, = 0,
respectively. The factor 0.5 makes it possible to round the value
the integer function rather than truncating them.]

6. i=1 [Begins the loop, in this loop points are plotted]
While (i < length)
{
Plot (Integer (x), Integer (y) )
x=x+Ax
y=ytdy
i=i+1

[10]

FOCI 7) AO AOR x
--- page 5 ---
Q2 |b X;=0,Y)=0
X= 4, Y2=6
Length = /Y2— Y,|=6
AX=|X—X,|/ Length = 4/6
AY =|Y2-Yi|/ Length = 6/6=1
Initial value for,
X=0 + 0.5 x (4/6) = 0.5
Y =0+0.5x(1)=0.5

Plot integer now:

1. Plot (0,0), x=x+AX=0.5+4/6=1.167, y=y+ AY=0.5+1=1.5 [10]
2.Plot (1,1), x=x+AX=1.167+4/6=1.833 y=y+ AY=1.5+1=2.5

3.Plot (1,2), x=x+AX=1.833+4/6=2.5 y=yt AY=2.5+1=3.5

4.Plot (2,3), x=x+AX=2.5+4/6=3.167 y=y+ AY=3.5+1=4.5

5.Plot (3,4), x=x+AX=3.167+4/6=3.833 y=y+ AY=4.5+1=5.5

6.Plot (3,5), x=x+AX=3.833+4/6=4.5 y=y+ AY=5.5+1=6.5

Tabulating the results of each iteration in the step 7 we get,

i Plot x y
0.5 0.5
1 (0,0) 1.167 1.5
2 dl) 1.833 2.5
3 (1,2) 2.5 3.5
4 (2,3) 3.167 45
5 (3,4) 3.833 5.5
6 G,5) 45 6.5

FIC DI EH ar
--- page 6 ---
Q3   a.
1. Clipping in three dimensions can be accomplished using extensions of two-
[10]
dimensional clipping methods.
2. Instead of clipping against straight-line window boundaries, we now clip
objects against the boundary planes of the view volume.
********** 6 **********
--- page 7 ---
3. An endpoint (x, y, z) of a line segment is outside a boundary plane if Ax +
By + Cz + D > 0, where A, B , C, and D are the plane parameters for that
boundary.
4. Similarly, the point is inside the boundary if Ax + By + Cz + D < 0.
5. Lines with both endpoints outside a boundary plane are discarded, and those
with both endpoints inside all boundary planes are saved.
6. The intersection of a line with a boundary is found using the line equations
along with the plane equation.
7. Intersection coordinates (x1, y1 , z1) are values that are on the line and that
satisfy the plane equation
8.   Ax1, + By1 + Cz1, + D = 0.
9. Mapping positions within a rectangular view volume to a three-dimensional
rectangular viewport is accomplished with a combination of scaling and
translation, similar to the operations needed for a two-dimensional window-
to viewport mapping.
Q3 b The Area Subdivision Method is a hidden surface removal technique based on
.   the concept of divide and conquer. Instead of working on individual polygons or
pixels, this method recursively subdivides the viewing area (image space) into
smaller regions until they are simple enough to be easily resolved.
Working Principle
1. Start with the entire screen (viewport): Consider the whole image as a
single area.
2. Classify surfaces in the current area:
o A surface is completely inside the area.
[10]
o A surface is completely outside the area.
o A surface partially overlaps the area.
o Multiple surfaces overlap within the area.
3. Subdivide the area if needed:
o   If multiple surfaces overlap, divide the area into smaller regions
(usually into quadrants).
o Recursively apply the process to each sub-region.
4. Stop subdivision when:
o The area contains only one visible surface.
o The area is empty (no surfaces present).
o The area is small enough to resolve visibility directly.
********** 7 **********
--- page 8 ---
5. Render the final image: Once all sub-areas are resolved, the image is
constructed.
Use in Complex Scenes
The Area Subdivision Method is particularly useful for complex scenes where
multiple overlapping surfaces exist. It efficiently eliminates hidden surfaces by
focusing on image regions rather than individual polygons.
Why is it useful?
✅ Efficient for hierarchical structures: Works well with octrees or quadtrees,
making it suitable for large, structured scenes like cityscapes or CAD models.
✅ Reduces unnecessary computations: If an entire sub-area is covered by one
surface, no further checks are needed.
✅ Handles transparent objects: Since it works at an area level, it can
accommodate transparency and layering effects better than per-pixel methods.
Limitations
❌ Less efficient for highly detailed scenes: If the image has many small objects,
subdivision can become excessive and computationally expensive.
❌ Not ideal for real-time rendering: Compared to Z-buffering, this method is
slower due to its recursive nature.
❌ Handling curved surfaces is complex: The method is primarily designed for
polygonal data, requiring extra steps for spline-based or curved objects.
********** 8 **********
--- page 9 ---
Q4

a.

Translation Matrix

The translation matrix for shifting by (

+2, +3) is:

T-|0 1 3

Triangle Matrix Representation

In homogeneous coordinates:

Matrix Multiplication

(lx14+0x2+42x 1)
= |(0x14+1x2+3x1)
1

Step 2: Rotation by 90°

Rotation Matrix

P'-TxP

1 0 2 13 °5
0 1 3)x)]2 4 1
001 111i

(1x340x442x1) (1x540x14+2x1)
(Ox3+1x44+3x1) (0x5+4+1x1+3x1)
1 1

Counterclockwise

The 90° counterclockwise rotation matrix is:

Matrix Multiplication

R=

0 -1 0
1 0 0

0 0 1

P"=RxP'

0 1 0 305 7
=|l 0 O} x5 7 4
0 0 1 111i

(0x 3+ (-1)x5+0x 1)
=|] (1x340x5+4+0x1)
1

(Ox 5+(-1)x7+0x1) (0x7+(-1)x440x1)
(1x5+0x7+0x1) (lx 7+0x4+0x1)
1 1

—5 7 —
=|3 5 7
1 1 1

[10]

FIC QF OH ar
--- page 10 ---
Q4 b
.
[10]
Q5   a.    Another method for generating a view of a three-dimensional scene is to
project points to the display plane along converging paths.
 This causes objects farther from the viewing position to be displayed smaller
than objects of the same size that are nearer to the viewing position.
 In a perspective projection, parallel lines in a scene that are not parallel to [10]
the display plane are projected into converging lines.
 Scenes displayed using perspective projections appear more realistic, since
this is the way that our eyes and a camera lens form images.
 The point at which a set of projected parallel lines appear to converge is
called a vanishing point.
********** 10 **********
--- page 11 ---
 Each set of projected parallel lines will have a separate vanishing point and
in general a scene can have any number of vanishing points depending on
how many sets of parallel lines there are in the scene.
 The vanishing point for any set of lines that are parallel to one of the principal
axes of an object is referred to as a principal vanishing point.
Q5 b
•Step 1 − Accept the number of vertices in the polygon and the co-ordinates of the
.
vertices.
•Step 2 − Active Edge List is prepared for each scanline intersecting the polygon
that contains the list of edges intersecting the scanline.
•Step 3 −For each polygon edge in the AEL intersection points are calculated.
•Step 4: Sort all the edge intersecting points in increasing order of x-values.
The first x values gives the left boundary and second x value gives the right
boundary.
•Step 5: Fill all the pixel positions between left and right boundary with the
specified color value.
Repeat   the   steps   2   to   5   for   all   the   scanlines.
[10]
Special cases of polygon vertices:
•If both lines intersecting at the vertex are on the same side of the scanline, consider
it as two points.
•If lines intersecting at the vertex are at opposite sides of the scanline, consider it
as only one point.
Q6   a. Left Clipping:   [10]
********** 11 **********
--- page 12 ---
[v1,v2] : inside-inside -> saving v2
[v2,v3] : inside-inside -> saving v3
[v3,v4] : inside-inside -> saving v4
[v4,v1] : inside-inside -> saving v1

Bottom Clipping:

[v1,v2] : outside-outside -> saving nothing
[v2,v3] : outside-inside -> saving v2'.v3
[v3,v4] : inside-inside -> saving v4

[v4,v1] : inside-outside -> saving v4’

Right Clipping:

[v2’,v3] : outside-outside -> saving nothing
[v3,v4] : outside-outside -> saving nothing
[v4,v4'] : outside-inside -> saving v4", v4’
[v4',v2’] : inside-outside -> saving v4™

® !

\

[v4’,v4"] : inside-inside -> saving v4"
[v4",v4"] : inside-inside -> saving v4”
[v4",v4'] : inside-inside -> saving v4’

FRR ICR] DA KH
--- page 13 ---
Q6 b
.
[10]
Q7   a.   1. A point (x, y) can be re-written in homogeneous coordinates as (xh, yh, h)
2. We   can   conveniently   choose   h   =   1   so   that
[10]
(x, y) becomes (x, y, 1)
3. Using homogeneous coordinates allows us use matrix multiplication to
calculate transformations – extremely efficient
********** 13 **********
--- page 14 ---
2. Deriving the Combined Rotation Matrix
Using the general rotation matrices:

cos#, —sind; 0
R(0;) = |sin®, cos 0
0 0 1

cos0. —sin 8, 1

R(O2) = |sin@.   cosb. 0
0 0 1

Now, multiplying R(02) x R(01):
cosO. —sind. 0 cos#; —sin@; 0
Rota = |sin@2   cosA OO] x |sin@; cosh 0
0 0 1 0 0 1
Performing matrix multiplication:
cos 62 cos 4; — sin @2sin@; —cos@2sin@, —sin62cos0, 0
Rota = | sin 02 cos 0; + cos 02 sin@,; —sin@2sin 0; +cos@2cos#, 0
0 0 1
Using trigonometric identities:
cos(A + B) = cos Acos B — sin Asin B
sin(A + B) = sin Acos B + cos Asin B

We simplify:

cos(0, + 02) —sin(@: +02) 0
Reotar = | sin(@:+ 42)   cos(, +642) 0
0 0 1

Q7 |b

[10]

RK KKK RK KK 14 2h KKK RK Kk KK
--- page 15 ---
P= 0100
Q= 0000
As logical AND is 0000, the line is a clipping candidate.
Y’=ywmin
X’= x1+ 1/m(ywmin-y1)
X’= 25+ 0.9 (20-10)
X’= 34
Clipped Co-ordinates are: (34,20)
********** 15 **********
````
