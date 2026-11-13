# Image and Video Processing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 148f1ad2294f

- Departments: Computer Engineering, Computer Science
- Programmes: BTech CS 7055, Integrated Computer 7032, MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CS_7055/Image and Video Processing/ANS_Image and Video Processing(702EX0E004)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: mixed (15 pages), mean OCR confidence 80.3

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester IX/Semester V(Exam Year: 2025-2026)
Subject: Image and Video Processing
Date: 08 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Compare JPEG and PNG image file formats with respect to features and usage:   [4]
SO-1;
BL-2   Answer:
Any 4 comparison points for 4 marks:
S. No   Parameter   JPEG   PNG
1   Compression   lossy   lossless
2   Bits   8- bits   8/24-bits
3   Colour   Not transparent   Better transparency
4   Interlacing   JPEG Images are not   PNG Images not
interlaced   interlaced
5   Application   Best for the final   Best suited for editing
distribution of   pictures.
photographic-type images
due to smaller file size.
CO-2;   b. Consider the following 3 × 3 grayscale image region:   [4]
SO-1;
BL-3   10 20 30
𝐼= 40 50 60
70 80 90
Using a Laplacian filter having positive centre without diagonal elements for sharpening,
compute the output value at the center pixel (50).
Answer:
Mask → 1 mark
********** 1 **********
--- page 2 ---
Substitution → 1 mark
Calculation → 1 mark
Final answer → 1 mark
Mask:
0 −1 0
−1 4 −1
0 −1 0
Output center pixel= 0
CO-3;   c.   State morphological erosion. Perform morphological erosion on the following image for   [4]
SO-1;   object ‘A’ using the structuring element ‘B’. Circle indicates origin
BL-4
A =
0   1   0   0
0   1   1   0
0   1   1   0
0   1   0   0
B =
1   1
1   1
Answer
Eroded image, 𝐴⊖𝐵:
0   0   0   0
0   1   0   0
0   0   0   0
0   0   0   0
Erosion definition: 2 Marks
Output Image: 2 Marks
CO-4;   d. What is adjacency in image processing?   [4]
SO-1;
BL-4   Consider the following 5 × 5 binary image. The origin is at top-left and coordinates are
written as (row,column) with 1-based indexing. Foreground pixels have value 1 (set 𝑉=
{1}).
1 1 0 0 1
1 1 0 1 0
𝐼 = 0 0 0 0 0
0 1 0 0 0
0 0 1 0 0
********** 2 **********
--- page 3 ---
Draw dashed lines showing connections between pixels of the same label under:
1. 8-adjacency
2. m-adjacency
Answer
Definitions: adjacency (2 marks)
For 8-adjacency (1 mark)
For m- adjacency (1 mark)
CO-5;   e.   Differentiate between spatial redundancy and temporal redundancy in video data.   [4]
SO-1;
BL-2   Answer:
Aspect   Spatial Redundancy   Temporal Redundancy
Definition   Repetition of similar   Repetition of similar information
information within a single   across consecutive frames in a
frame.   video sequence.
Cause   Neighboring pixels in an   Successive frames often contain
image often have similar   the same objects with small motion
intensity or color values.   or background changes.
Redundancy   Spatial (within frame) —   Temporal (between frames) —
Type   related to image structure.   related to motion over time.
Reduction   Removed by Intra-frame   Removed by Inter-frame coding
Method   coding (e.g., DCT, JPEG).   (e.g., motion estimation,
prediction).
********** 3 **********
--- page 4 ---
Q2   a An image has the following gray levels and corresponding number of pixels:   [10]
CO-2;
Gray level rₖ   0 1 2 3 4   5 6 7
SO-1;
BL-3   No. of pixels nₖ 2 3 5 8 10 20 8 4
Compute the gray level distribution using histogram equalization. Also plot the histogram
of the input and output (equalized) images.
Answer:
1) Histogram equalization steps (6 marks)
2) I/P and O/P histograms (4 marks).
PDF =
CDF =
rₖ   nₖ   p(rₖ) - PDF   P(rₖ) (CDF)   SK = 7*P(rK)   Rounded SK
0   2   2/60 = 0.033333...   0.0333333   0.2333333   0
1   3   3/60 = 0.05   0.0833333   0.5833333   1
2   5   5/60 = 0.083333...   0.1666667   1.1666667   1
3   8   8/60 = 0.133333...   0.3000000   2.1000000   2
4   10   10/60 = 0.166666...   0.4666667   3.2666667   3
5   20   20/60 = 0.333333...   0.8000000   5.6000000   6
6   8   8/60 = 0.133333...   0.9333333   6.5333333   7
7   4   4/60 = 0.066666...   1.0000000   7.0000000   7
New Gray levels New no. of pixels
0   2
1   8
2   8
3   10
6   20
7   12
********** 4 **********
--- page 5 ---
Q2   b   Convert a RGB color model with R=100, G=200, B=50 to HSI color model.   [10]
CO-2;
Answer:
SO-1;
Formulae (4 Marks)
BL-3
If B > G , then H=360o – H
Substitution & Calculation (6 Marks)
(a) Intensity (I):
(b) Saturation (S):
(c) Hue (H):
Final HSI Values
Q3   a   Find 2-D Hadamard Transform of the following image ‘f’   [4]
CO-2;
SO-1;   𝑓= [2 6
3 5]
BL-3
Answer:
𝐹(𝑢, 𝑣) = 𝐻 . 𝑓(𝑥, 𝑦) . 𝐻𝑇
********** 5 **********

[Text in pictures on this page, read by OCR]
Numerator:
0.5 x [((R — G) + (R— B)| = 0.5 x [(100 — 200) + (100 — 50)| = 0.5 x (—100 + 50) = —25

Denominator:

V/(R - G)? + (R- B)(G — B) = v/(—100)? + (50)(150) = 10000 + 7500 = 17500 = 132.29

Now,

— cog ( 228) — et _ °
H = cos 732.39) ~ © (—0.189) = 100.9

Since B < G, we keep H as is.
--- page 6 ---
𝐹(𝑢, 𝑣) = [1 1   . [2 6   . [1   1
1 −1]   3 5]   1 −1]
𝐹(𝑢, 𝑣) = [ 5 11 ] . [1 1 = [16 −6
−1 1   1 −1]   0 −2]
Q3   b   Apply the Horizontal and Vertical Sobel operators on the image, then compute the   [8]
gradient magnitude, using pixel replication at borders.
CO-3;
SO-1;
10   10   10   10
BL-4
10   10   10   10
100   100   100   100
100   100   100   100
Answer:
Standard Sobel kernels for:
After applying kernels,
********** 6 **********
--- page 7 ---
Sobel kernels – 1 mark
Gx Matrix - 2marks
Gy Matrix - 2marks
Formula of M - 1marks
Output Matrix - 2marks
Q3   c   What is morphological opening? Perform morphological opening on the following image   [8]
A (size 9x9) using the structuring element ‘B’.
CO-3;
SO-1;
BL-4   0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
0   0   1   1   0   1   1   0   0
0   0   0   1   1   1   0   0   0
0   0   1   1   1   1   1   0   0
0   0   1   1   0   1   1   0   0
0   0   1   1   1   1   1   0   0
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
Image A
1   0   1
1   1   1
1   0   1
Structuring element ‘B’, Center position is origin
Answer:
********** 7 **********

[Text in pictures on this page, read by OCR]
Gradient magnitude

0 0 0 0
360 360 360 360

M = ,/G2+G2=|G,|=
z+ Gy= |G, 360 360 360 360

0 0 0 0
--- page 8 ---
Morphological opening definition: 2 marks
Image after erosion: 3 marks
After dilation (Final Image): 3 marks
Q4   a   Apply median filter of size 3 x 3 on the circled pixels of the input image give below.   [4]
CO-2;
147   163   169   122   51
SO-1;
BL-3   152   168   148   255   48
176   167   97   44   57
185   121   45   50   63
132   55   43   61   67
Answer:
Each step 2 marks:
1) 44, 48, 51, 57, 97, 122, 148, 169, 255 = Median value is 97.
2) 44, 45, 50, 97, 121, 148, 167, 168, 255 = Median value is 121.
Q4   b. Find a 2-dimensional Discrete Cosine Transform (DCT) of the following image ‘f’ using   [8]
the transform matrix.
CO-2;
SO-1;
BL-3
********** 8 **********
--- page 9 ---
1 2 2 1
2 2 1 1
𝑓= [   ]
1 2 2 1
1 2 1 2
Answer:
Formula (1 mark)
DCT matrix (2 marks)
C =
𝐶. 𝑓=
(2 marks)
𝐹= 𝐶. 𝑓. 𝐶𝑇=
(3 marks)
Q4   c   Discuss the Three-Step Search (TSS) algorithm for motion estimation. Explain how it   [8]
balances accuracy and computational efficiency in video compression.
CO-5;
SO-1;
BL-2
Answer:
Method:
Divide search area (±7 pixels typical).
Step 1: Search 9 points with step size 4.
Step 2: Move to point with lowest error → reduce step to 2.
Step 3: Repeat with step 1 → final motion vector.
Advantages:
Far fewer search points (25 vs 225 in exhaustive).
Good balance between speed and accuracy.
Widely used in MPEG and H.26x codecs.
Limitation: May miss true vector in fast motion cases.
********** 9 **********
--- page 10 ---
Q5   a   For the given image below:   [4]
CO-3;
2   4   6
SO-1;
1   5   7
BL-4
3   9   8
Compute Gradient Direction for the center pixel using Prewitt operator.
Answer:
Mask – 1 mark
Gx, Gy - 2 marks
Direction - 1 mark
Q5   b An image has 4 gray levels: 0, 1, 2, 3. The number of pixels corresponding to each gray [8]
level is as follows:
CO-4;
SO-1;
BL-4
********** 10 **********
--- page 11 ---
Gray level (r)   0 1 2 3
No. of pixels (n)   4 5 3 2
Find optimal threshold using Otsu for threshold values 1 and 2 only.
Answer:
Calculate parameters for each threshold
T   w₀   w₁   μ₀   μ₁   σB²
1   0.643   0.357   0.555   2.400   0.382
2   0.857   0.143   0.887   3.000   0.460
For T=1
Background and foreground mean calculations (1 marks)
P1 calculation (1 marks)
Between class variance (1mark)
For T=2
Background and foreground mean calculations (1 marks)
P1 calculation (1 marks)
Between class variance (1 mark)
Optimum threshold at which σB² is maximum: T=2 (2 marks)
Q5   c   Perform boundary extraction on the following binary image A using the structuring [8]
element SE shown below.
CO-3;
SO-1;
A =
BL-4
0   1   2   3   4   5   6
0   0   0   0   0   0   0   0
1   0   1   1   1   1   0   0
2   0   1   1   1   1   1   0
3   0   1   1   1   1   1   0
4   0   1   1   1   1   1   0
5   0   1   1   1   1   0   0
6   0   0   0   0   0   0   0
SE =
1
1   1   1
1
********** 11 **********
--- page 12 ---
Answer:

Formula 2 marks
Erosion 3 marks
Output Image 3 marks

Boundary extraction =

B=A-—(A6SE)

Erosion A CG SE

Output Image:

FRR ICR] DA KH
--- page 13 ---
Q6   a An image segment is shown below. Let, V be the set of Gray-level values used to define [4]
connectivity in the image.
CO-1;
Compute: De, D4, D8 and Dm distances between pixels ‘p’ and ‘q’ for: V = {1,2}.
SO-1;
BL-2
0   1   2(q)
2   3   2
1(p) 1   3
Answer:
Each part 1 mark.
Co-ordinates for (p x, y, q s, t) are p (0,2) and q (2,0).
1) De (p, q) = √(𝑥−𝑠)2 + (𝑦−𝑡)2 = √8 units
2) D4 (p, q) = |(𝑥−𝑠)| + |𝑦−𝑡| = 4 units
3) D8 (p, q) = 𝑀𝑎𝑥[|(𝑥−𝑠)|, |𝑦−𝑡|] = 2 units
4) Dm (p, q) for V = {1,2} = 3 units
Q6   b   Perform region splitting and merging on the following image with threshold value T <=   [8]
10.
CO-4;
SO-1;
80   85   78   82
BL-4
83   82   79   84
200   195   198   202
199   201   197   196
Answer
Key Steps:
1.   Start with the entire 4×4 region— not homogeneous → split into four 2×2
subregions.
2.   Test each 2×2 region for homogeneity
3.   Continue until all subregions satisfy the homogeneity condition.
4.   Merge adjacent regions if they satisfy the condition.
5.   Present the final region map after splitting and merging.
Splitting – 4 marks
********** 13 **********
--- page 14 ---
Merging – 4 marks
Q6   c   Describe the YUV color model and its significance in video processing.   [8]
CO-1;
Anwer:
SO-1;
Definition/Concept – 2
BL-2
YUV components explanation – 4
Application/Importance – 2
Definition: Separates luminance (Y) from chrominance (U,V).
Components:
Y: Brightness information
U: Blue-luminance difference
V: Red-luminance difference
Significance:
Reduces bandwidth in video compression by down sampling chrominance.
Used in TV, MPEG, JPEG compression.
Q7   a   Explain Exhaustive Search Block Matching Algorithm in video processing. Discuss its   [10]
advantages and disadvantages.
CO-5;
SO-1;
Answer:
BL-2
Exhaustive Search Block Matching Algorithm – 6marks
Advantages and disadvantages – 4marks
Q7   b What is difference between Power-Law Transformation and Contrast Stretching? Apply   [10]
the Power-Law (Gamma) Transformation on the following image with C=1.2, and 𝛾 =
CO-2;
0.6 and obtain the final output image matrix.
SO-1;
BL-3
f(x, y) =
0   20   40
60   80   100
110   120   127
********** 14 **********

[Text in pictures on this page, read by OCR]
80 85 78 82
R14
83 82 79 84
200 195 198 202
201 197 196

R3 199

R4
--- page 15 ---
Answer:
Difference between Power-Law Transformation and Contrast Stretching - 2marks
s=1.2×r0.6
r   r0.6   s = 1.2 x r0.6   Rounded s
0   0.000   0.00   0
20   6.037   7.24   7
40   9.155   10.99   11
60   11.664   13.99   14
80   13.764   16.52   17
100   15.860   19.03   19
110   16.844   20.21   20
120   17.777   21.33   21
127   18.415   22.10   22
Output Matrix
Formula and substitution 2 marks
Intermediate calculations 4 marks
Final matrix (rounded)   2 marks
********** 15 **********
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper f98333db4ddc

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_Computer_7002/Image and Video Processing/ANS_Image and Video Processing(702EX0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: mixed (17 pages), mean OCR confidence 80.0

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026
Program/s: B Tech /MBA Tech   Year: II Semester: IV
Stream/s: B Tech (Artificial Intelligence)/ MBA (Tech) (Artificial Intelligence)/ B Tech
(Arti Intelligen and Mach Learn)/ B Tech (Artificial Intellige & Data Sci)
Subject: Signal and Image Processing   Time:3 hrs
Date:   /   /2025   No. of Pages:
Marks: 100
Final Examination (2025-26)
Synoptic Answers
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.
1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4___ questions.
3) In all ___5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Compare JPEG and PNG image file formats with respect to features and usage:   [4]
SO-1;
BL-2   Answer:
Any 4 comparison points for 4 marks:
S. No   Parameter   JPEG   PNG
1   Compression   lossy   lossless
2   Bits   8- bits   8/24-bits
3   Colour   Not transparent   Better transparency
4   Interlacing   JPEG Images are not   PNG Images not interlaced
interlaced
1
--- page 2 ---
5   Application   Best for the final   Best suited for editing
distribution of   pictures.
photographic-type
images due to smaller
file size.
CO-2;   b. Consider the following 3 × 3 grayscale image region:   [4]
SO-1;
BL-3   10 20 30
𝐼= 40 50 60
70 80 90
Using a Laplacian filter having positive centre without diagonal elements for sharpening,
compute the output value at the center pixel (50).
Answer:
Mask → 1 mark
Substitution → 1 mark
Calculation → 1 mark
Final answer → 1 mark
Mask:
0 −1 0
−1 4 −1
0 −1 0
Output center pixel= 0
CO-3;   c.   State morphological erosion. Perform morphological erosion on the following image for   [4]
SO-1;   object ‘A’ using the structuring element ‘B’. Circle indicates origin
BL-4
A =
0   1   0   0
0   1   1   0
0   1   1   0
0   1   0   0
B =
1   1
1   1
2
--- page 3 ---
Answer
Eroded image, 𝐴⊖𝐵:
0   0   0   0
0   1   0   0
0   0   0   0
0   0   0   0
Erosion definition: 2 Marks
Output Image: 2 Marks
CO-4;   d. What is adjacency in image processing?   [4]
SO-1;
BL-4   Consider the following 5 × 5 binary image. The origin is at top-left and coordinates are
written as (row,column) with 1-based indexing. Foreground pixels have value 1 (set 𝑉=
{1}).
1 1 0 0 1
1 1 0 1 0
𝐼 = 0 0 0 0 0
0 1 0 0 0
0 0 1 0 0
Draw dashed lines showing connections between pixels of the same label under:
1. 8-adjacency
2. m-adjacency
Answer
Definitions: adjacency (2 marks)
For 8-adjacency (1 mark)
3
--- page 4 ---
For m- adjacency (1 mark)
CO-5;   e.   Differentiate between spatial redundancy and temporal redundancy in video data.   [4]
SO-1;
BL-2   Answer:
Aspect   Spatial Redundancy   Temporal Redundancy
Definition   Repetition of similar   Repetition of similar information
information within a single   across consecutive frames in a
frame.   video sequence.
Cause   Neighboring pixels in an   Successive frames often contain
image often have similar   the same objects with small motion
intensity or color values.   or background changes.
Redundancy   Spatial (within frame) —   Temporal (between frames) —
Type   related to image structure.   related to motion over time.
Reduction   Removed by Intra-frame   Removed by Inter-frame coding
Method   coding (e.g., DCT, JPEG).   (e.g., motion estimation,
prediction).
Q2   a An image has the following gray levels and corresponding number of pixels:   [10]
CO-2;
Gray level rₖ   0 1 2 3 4   5 6 7
SO-1;
BL-3   No. of pixels nₖ 2 3 5 8 10 20 8 4
Compute the gray level distribution using histogram equalization. Also plot the histogram
of the input and output (equalized) images.
Answer:
1) Histogram equalization steps (6 marks)
2) I/P and O/P histograms (4 marks).
4
--- page 5 ---
PDF =
CDF =
rₖ   nₖ   p(rₖ) - PDF   P(rₖ) (CDF)   SK = 7*P(rK)   Rounded SK
0   2   2/60 = 0.033333...   0.0333333   0.2333333   0
1   3   3/60 = 0.05   0.0833333   0.5833333   1
2   5   5/60 = 0.083333...   0.1666667   1.1666667   1
3   8   8/60 = 0.133333...   0.3000000   2.1000000   2
4   10   10/60 = 0.166666...   0.4666667   3.2666667   3
5   20   20/60 = 0.333333...   0.8000000   5.6000000   6
6   8   8/60 = 0.133333...   0.9333333   6.5333333   7
7   4   4/60 = 0.066666...   1.0000000   7.0000000   7
New Gray levels New no. of pixels
0   2
1   8
2   8
3   10
6   20
7   12
Q2   b   Convert a RGB color model with R=100, G=200, B=50 to HSI color model.   [10]
CO-2;
Answer:
SO-1;
Formulae (4 Marks)
BL-3
5
--- page 6 ---
If B > G , then H=360o – H
Substitution & Calculation (6 Marks)
(a) Intensity (I):
(b) Saturation (S):
(c) Hue (H):
Final HSI Values
Q3   a   Find a 2-dimensional 2-D Hadamard Transform of the following image ‘f’   [4]
CO-2;
SO-1;   𝑓= [2 6
3 5]
BL-3
6

[Text in pictures on this page, read by OCR]
Numerator:
0.5 x ((R — G) + (R— B)| = 0.5 x [(100 — 200) + (100 — 50)| = 0.5 x (—100 + 50) = —25

Denominator:

V(R— G)? + (R— B)(G — B) = \/(—100)? + (50)(150) = 10000 + 7500 = V/17500 = 132.29

Now,
—25

132.29

H =cos? ( ) =cos '(—0.189) = 100.9°

Since B < G, we keep H as is.
--- page 7 ---
Answer:
𝐹(𝑢, 𝑣) = 𝐻 . 𝑓(𝑥, 𝑦) . 𝐻𝑇
𝐹(𝑢, 𝑣) = [1   1   . [2 6   . [1 1
1 −1]   3 5]   1 −1]
𝐹(𝑢, 𝑣) = [ 5 11 ] . [1 1 = [16 −6
−1 1   1 −1]   0 −2]
Q3   b   Apply the Horizontal and Vertical Sobel operators on the image, then compute the   [8]
gradient magnitude, using pixel replication at borders.
CO-3;
SO-1;
10   10   10   10
BL-4
10   10   10   10
100   100   100   100
100   100   100   100
Answer:
Standard Sobel kernels for:
After applying kernels,
7
--- page 8 ---
Prewitt kernels – 1 mark
Gx Matrix - 2marks
Gy Matrix - 2marks
Formula of M - 1marks
Output Matrix - 2marks
Q3   c What is morphological opening? Perform morphological opening on the following   [8]
image A (size 9x9) using the structuring element ‘B’.
CO-3;
SO-1;
BL-4   0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
0   0   1   1   0   1   1   0   0
0   0   0   1   1   1   0   0   0
0   0   1   1   1   1   1   0   0
0   0   1   1   0   1   1   0   0
0   0   1   1   1   1   1   0   0
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
Image A
1   0   1
1   1   1
1   0   1
Structuring element ‘B’, Center position is origin
8

[Text in pictures on this page, read by OCR]
Gradient magnitude

0 0 0 0
360 360 360 360

M = ,/G2+G2=|G,| =
2+ Gy = |G) 360 360 360 360

0 0 0 0
--- page 9 ---
Answer:
Morphological opening definition: 2 marks
Image after erosion: 3 marks
After dilation (Final Image): 3 marks
Q4   a   Apply median filter of size 3 x 3 on the circle pixel of the input image give below.   [4]
CO-2;
147   163   169   122   51
SO-1;
BL-3
152   168   148   255   48
176   167   97   44   57
185   121   45   50   63
132   55   43   61   67
Answer:
Each step 2 marks:
9
--- page 10 ---
1) 44, 48, 51, 57, 97, 122, 148, 169, 255 = Median value is 97.
2) 44, 45, 50, 97, 121, 148, 167, 168, 255 = Median value is 121.
Q4   b. Find a 2-dimensional Discrete Cosine Transform (DCT) of the following image ‘f’ using   [8]
the transform matrix.
CO-2;
SO-1;
BL-3   1 2 2 1
2 2 1 1
𝑓= [   ]
1 2 2 1
1 2 1 2
Answer:
Formula (1 mark)
DCT matrix (2 marks)
C =
𝐶. 𝑓=
(2 marks)
𝐹= 𝐶. 𝑓. 𝐶𝑇=
(3 marks)
10
--- page 11 ---
Q4   c   Discuss the Three-Step Search (TSS) algorithm for motion estimation. Explain how it   [8]
balances accuracy and computational efficiency in video compression.
CO-5;
SO-1;
BL-2
Answer:
Method:
Divide search area (±7 pixels typical).
Step 1: Search 9 points with step size 4.
Step 2: Move to point with lowest error → reduce step to 2.
Step 3: Repeat with step 1 → final motion vector.
Advantages:
Far fewer search points (25 vs 225 in exhaustive).
Good balance between speed and accuracy.
Widely used in MPEG and H.26x codecs.
Limitation: May miss true vector in fast motion cases.
Q5   a   For the given image below:   [4]
CO-3;
2   4   6
SO-1;
1   5   7
BL-4
3   9   8
Compute Gradient Direction for the center pixel using Prewitt operator.
Answer:
11

[Text in pictures on this page, read by OCR]
Horizontal mask (for vertical edges):
—-1 0 +1
G,=]-1 0 41
-1 0 +1
Vertical mask (for horizontal edges):
+1 41 41
G,=|0 0 0
-1 -1 -1
--- page 12 ---
Mask – 1 mark
Gx, Gy - 2 marks
Direction - 1 mark
Q5   b An image has 4 gray levels: 0, 1, 2, 3. The number of pixels corresponding to each gray [8]
level is as follows:
CO-4;
SO-1;
Gray level (r)   0 1 2 3
BL-4
No. of pixels (n)   4 5 3 2
Find optimal threshold using Otsu for threshold values 1 and 2 only.
Answer:
Calculate parameters for each threshold
T   w₀   w₁   μ₀   μ₁   σB²
1   0.643   0.357   0.555   2.400   0.781
2   0.857   0.143   0.917   3.000   0.532
12
--- page 13 ---
For T=1
Background and foreground mean calculations (1 marks)
P1 calculation (1 marks)
Between class variance (1mark)
For T=2
Background and foreground mean calculations (1 marks)
P1 calculation (1 marks)
Between class variance (1 mark)
Optimum threshold at which σB² is maximum: T=1 (2 marks)
Q5   c   Perform boundary extraction on the following binary image A using the structuring [8]
element SE shown below.
CO-3;
SO-1;
A =
BL-4
0   1   2   3   4   5   6
0   0   0   0   0   0   0   0
1   0   1   1   1   1   0   0
2   0   1   1   1   1   1   0
3   0   1   1   1   1   1   0
4   0   1   1   1   1   1   0
5   0   1   1   1   1   0   0
6   0   0   0   0   0   0   0
SE =
1
1   1   1
1
Answer:
Formula 2 marks
Erosion 3 marks
Output Image 3 marks
13
--- page 14 ---
Boundary extraction =

B= A-(A@ SE)

Erosion A G SE

Output Image:

14
--- page 15 ---
Q6   a An image segment is shown below. Let, V be the set of Gray-level values used to define [4]
CO-1;   connectivity in the image.
SO-1;   Compute: De, D4, D8 and Dm distances between pixels ‘p’ and ‘q’ for: V = {1,2}.
BL-2   0   1   2(q)
2   3   2
1(p) 1   3
Answer:
Each part 1 mark.
Co-ordinates for (p x, y, q s, t) are p (0,2) and q (2,0).
1) De (p, q) = √(𝑥−𝑠)2 + (𝑦−𝑡)2 = √8 units
2) D4 (p, q) = |(𝑥−𝑠)| + |𝑦−𝑡| = 4 units
3) D8 (p, q) = 𝑀𝑎𝑥[|(𝑥−𝑠)|, |𝑦−𝑡|] = 2 units
4) Dm (p, q) for V = {1,2} = 3 units
Q6   b   Perform region splitting and merging on the following image with threshold value T <=   [8]
10.
CO-4;
SO-1;
80   85   78   82
BL-4
83   82   79   84
200   195   198   202
199   201   197   196
Answer
Key Steps:
1.   Start with the entire 4×4 region— not homogeneous → split into four 2×2
subregions.
2.   Test each 2×2 region for homogeneity
3.   Continue until all subregions satisfy the homogeneity condition.
4.   Merge adjacent regions if they satisfy the condition.
5.   Present the final region map after splitting and merging.
Splitting – 4 marks
15
--- page 16 ---
Merging – 4 marks
Q6   c   Describe the YUV color model and its significance in video processing.   [8]
CO-1;
Anwer:
SO-1;
Definition/Concept – 2
BL-2
YUV components explanation – 4
Application/Importance – 2
Definition: Separates luminance (Y) from chrominance (U,V).
Components:
Y: Brightness information
U: Blue-luminance difference
V: Red-luminance difference
Significance:
Reduces bandwidth in video compression by down sampling chrominance.
Used in TV, MPEG, JPEG compression.
Q7   a   Explain Exhaustive Search Block Matching Algorithm in video processing. Discuss its   [10]
advantages and disadvantages.
CO-5;
SO-1;
Answer:
BL-2
Exhaustive Search Block Matching Algorithm – 6marks
Advantages and disadvantages – 4marks
16

[Text in pictures on this page, read by OCR]
80 85 78 82
R14
83 82 79 84
200 195 198 202
201 197 196

R3 199

R4
--- page 17 ---
Q7   b What is difference between Power-Law Transformation and Contrast Stretching? Apply   [10]
the Power-Law (Gamma) Transformation on the following image with C=1.2, and 𝛾 =
CO-2;
0.6 and obtain the final output image matrix.
SO-1;
BL-3
f(x, y) =
0   20   40
60   80   100
110   120   127
Answer:
Difference between Power-Law Transformation and Contrast Stretching - 2marks
s=1.2×r0.6
r   r0.6   s = 1.2 x r0.6   Rounded s
0   0.000   0.00   0
20   6.037   7.24   7
40   9.155   10.99   11
60   11.664   13.99   14
80   13.764   16.52   17
100   15.860   19.03   19
110   16.844   20.21   20
120   17.777   21.33   21
127   18.415   22.10   22
Output Matrix
Formula and substitution 2 marks
Intermediate calculations 4 marks
Final matrix (rounded)   2 marks
17
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 940a8194af65

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7011/Image and Video Processing/ANS_Image and Video Processing(702EX0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Image and Video Processing
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is Compulsory.
5. Attempt any 4 from remaining questions.
6. Assume Suitbale data wherever necessary.
7. Draw clear diagram and write justification if required.
1A   What is a Digital Image? Discuss following for any image   [04]
[CO1, BL2]   example.   i. Intensity Range   ii. Resolution.
Definition of digital image and matrix example [2 marks]
Explanation of intensity range [1 mark]
Explanation of Resolution [1 Mark]
1B   Take an example and discuss the application of any two-   [04]
[CO2, BL3]   point processing approaches of image enhancement.
Students are expected to
1. choose any two approaches from following list and
apply on any digital image matrix.
• Image negative
• Image thresholding
• Contrast stretching
• Gray level slicing with and without background
•   Bit Plane slicing
• Log transformation
2. discuss the impact seen on the input image. [ 2 marks
for each chosen approach]
1C   “Morphological operation and edge detector can be useful to   [04]
[CO3, BL4]   extract the boundary of any object” justify this statement
using an image example and relevant operations.
********** 1   **********
--- page 2 ---
Students are expected to explain following with example image
1. Boundary extraction using –
inner boundary = original image – Eroded image
[2 Marks]
2. Usage of any edge detector which can help to extract
edges of image boundary. [2 Marks]
1D   Compare region growing and Region merging approaches   [04]
[CO4, BL4]   of image segmentation.
Region growing example – step by step working of the
approach on the image matrix [2 Marks]
Region merging – step by step working of the approach on the
image matrix [2 Marks]
1E   Explain temporal correlation in video processing.   [04]
[CO5, BL2]
2 A   Explain following in detail: i. Relationship among pixels   [10]
[CO1, BL2]   ii. Importance of grey level and frequency resolution
Students are expected to … [2 Marks each]
i.   Explain the 4, 8 and m connectivity to identify the
difference among neighboring pixels in the image
matrix.
ii.   Explain the smooth, blur and high frequency regions
in the image
iii.   Take an example of each type of images to discuss
the interrelationship discussed in above 2 steps.
iv.   Definition of gray and frequency resolution.
v.   How these resolutions affect the overall image
quality when one is varying keeping other one
constant.
2 B   Explain attest 5 real life applications of image and video   [10]
[CO1, BL2]   processing.
Students are expected to explain any 5 applications [2 Marks
each]. Sample applications given below.
1. User authenticity or imposing security
2. Law enforcement – CCTV image and video processing
3. Legal document preservation.
4. Film and advertising /media industry.
5. Healthcare- MRI/X-RAY/CT-SCAN etc.
********** 2   **********
--- page 3 ---
3 A   “Any digital image content can be analyzed for presence of   [10]
[CO2, BL3]   various patterns in it by using the Hadamard transforms”
Take an example and justify.
Students are expected to … [2 Marks each]
1. Draw 4x4 matrix of Hadamard transform
2. Explain steps of generating basis image patterns from
the basic transform matrix.
3. Generate basis image
4. Discuss these patterns
5. Discuss usage of these patterns for image content
analytics and feature extraction.
3 B   Discuss the difference in impact observed on resultant   [10]
[[CO2, BL3]   image after applying following operations: 1. Gray level
slicing with background. 2. Thresholding
Students are expected to [2 Marks each]
1. Generate image matrix of suitable size and content.
2. Apply Gray level slicing with background on that matrix
3. Discuss the resultant matrix.
4. Apply thresholding approach on original input matrix
5. Discuss the resultant matrix.
4 A   [10]
[CO3, BL4]   Analyze and discuss the impact of following line detectors
on any digital image. i. Horizontal ii. Vertical iii. diagonal
iv Reverse Diagonal.
Students are expected to [2 Marks each]
1. Generate 4 different image matrices having lines of four
orientations.
2. Draw line detector operators of these four orientations.
3. Apply these operators on all 4 image matrices
separately.
4. Discuss the resultant images
5. Compare all results and conclude the findings.
4 B   [10]
[CO3, BL4]   Analyze and explain the effect of Opening and closing on a
digital image having dark circular object with white
background.
Students are expected to [2 Marks each]
1. Generate image matrix and described in the question.
2. Apply opening operation on the original input image.
3. Apply Closing operation on the original input image.
********** 3   **********
--- page 4 ---
4. Compare both the outputs.
5. Conclude the final findings based on the analyses
carried out.
[10]
5 A   Compare the step by step working of Otsu segmentation
[CO4, BL4]   approach with region splitting segmentation.
Sample answer is given below.
Otsu’s Segmentation [ 5 Marks]
• Method: A global thresholding technique that
automatically finds the optimal threshold by maximizing
between-class variance in pixel intensities.
•   Steps:
1. Compute grayscale histogram.
2. Calculate class probabilities (background vs.
foreground).
3. Find class means.
4. Compute between-class variance.
5. Select threshold that maximizes variance.
•   Strengths: Simple, fast, no manual tuning, effective for
bimodal histograms.
•   Limitations: Sensitive to noise/uneven illumination, not
ideal for multi-peak histograms.
•   Applications: Medical imaging, OCR, object detection,
quality inspection.
Region Splitting Segmentation [ 5 Marks]
• Method: Start with the entire image and iteratively split
it into smaller regions until each satisfies a
uniformity/similarity criterion.
•   Steps:
1. Begin with full image.
2. Split into subregions based on homogeneity.
3. Continue until all regions meet similarity
conditions.
4. Optionally merge adjacent regions if they are
similar.
•   Strengths: Good for identifying homogeneous areas,
systematic approach.
•   Limitations: Computationally heavier, may struggle
with noisy or complex images.
•   Applications: Medical imaging, clustering
comparisons, educational demonstrations.
Key Comparison
• Otsu: Works best when histogram is bimodal; efficient
and automatic.
********** 4   **********
--- page 5 ---
• Region Splitting: More flexible for complex images;
relies on region homogeneity rather than global intensity
5 B   “Bad illumination affects the quality of segmentation using   [10]
[CO4, BL4]   thresholding” justify this statement with step by step
working of the process applied on suitable digital image.
Students are expected to. [ 2 Marks each]
1. Discuss the step by step working of global
thresholding approach by drawing histogram of
image matrix carrying clear cut distinct valley
region.
2. Modify the original input image matrix by
introducing the darker region
3. Draw the histogram of the modified image with
disappearing valley region.
4. Discuss the difficulty in choosing the threshold
to distinguish the foreground with background
5. Justify the statement
6 A   How digital video data is represented? Explain the importance   [10]
[CO5, BL2]   of I, P and B frames in video compression. Explain with
example.
Digital video is represented as a sequence of digital images
(frames) encoded into data streams, typically compressed using
formats like MPEG-2, H.264, or AV1, and displayed at
standard frame rates such as 24, 30, or 60 frames per second
I-frames, P-frames, and B-frames are the backbone of
modern video compression. I-frames store complete images
and act as reference points, P-frames predict from past frames
to save space, and B-frames predict from both past and future
frames for maximum compression efficiency. Together, they
balance quality and file size in formats like MPEG and H.264.
🔹 Importance of Each Frame Type
1. I-Frames (Intra-coded frames)
•   Definition: Full, self-contained image (like a JPEG).
• Role: Serve as keyframes or reference points in a video
stream.
• Importance:
o Enable random access (you can start playback
from an I-frame).
o Provide resilience against errors—if data is lost,
the next I-frame restores quality.
o Less compressible, so they take up more storage
space.
********** 5   **********
--- page 6 ---
2. P-Frames (Predicted frames)
•   Definition: Store only changes compared to the
previous I-frame or P-frame.
• Role: Reduce redundancy by encoding motion and
differences.
• Importance:
o More compressible than I-frames.
o Depend on earlier frames, so errors can
propagate until the next I-frame.
o Balance efficiency with moderate storage needs.
3. B-Frames (Bi-directional predicted frames)
•   Definition: Use data from both previous and future
frames for prediction.
• Role: Achieve the highest compression efficiency.
• Importance:
o   Significantly reduce file size.
o Require more processing power to
encode/decode.
o Cannot exist without surrounding I or P frames.
📊 Comparison Table
Frame   Data
Compression Dependency Use Case
Type   Stored
Keyframes,
I-Frame Full image Lowest   None   random
access
Differences   Efficient
P-Frame   Medium   Previous I/P
from past   compression
Differences
Maximum
B-Frame from past   Highest   Both I/P
compression
& future
⚖️ Why They Matter
•   Efficiency: Using P and B frames reduces file size
dramatically compared to storing every frame as an
I-frame.
• Quality Control: I-frames ensure playback stability and
allow seeking.
• Streaming & Storage: Modern codecs (H.264, HEVC,
AV1) rely on this structure to deliver high-quality video
at manageable bitrates.
6 B
[CO5, BL2]   Discuss:
1. Block matching
********** 6   **********
--- page 7 ---
Block Matching in Motion Estimation is a fundamental
technique used in video compression (like MPEG, H.264,
HEVC) to reduce redundancy between frames. It works by
finding how blocks of pixels move from one frame to another,
so instead of storing entire frames, only the motion information
and differences are encoded.
🔹 How Block Matching Works
1. Frame Division:
o Each frame is divided into small square blocks
(commonly 8×8 or 16×16 pixels).
2. Search Window:
o For each block in the current frame, the encoder
searches within a defined area (search window)
in the reference frame (previous or future frame).
3. Matching Criterion:
o The encoder compares blocks using metrics like:
▪ Mean Squared Error (MSE)
▪ Sum of Absolute Differences (SAD)
o The block in the reference frame that minimizes
the difference is chosen.
4. Motion Vector:
o The displacement between the original block and
the matched block is stored as a motion vector.
o Example: If a block moved 3 pixels right and 2
pixels down, the motion vector is (3, 2).
5. Residual Encoding:
o Differences between the predicted block and the
actual block (residuals) are also encoded to
preserve accuracy.
📊 Importance in Video Compression
• Reduces Redundancy: Instead of encoding every pixel,
only motion vectors + residuals are stored.
•   Efficiency: Achieves high compression ratios while
maintaining visual quality.
• Foundation of P and B Frames: Block matching is
what allows predictive frames (P, B) to exist.
• Streaming & Storage: Enables HD/4K video to be
transmitted over limited bandwidth.
⚖️ Advantages vs Limitations
Aspect   Advantage   Limitation
Compression High efficiency   Computationally intensive
Preserves motion Errors propagate if motion
Quality
smoothly   estimation is wrong
********** 7   **********
--- page 8 ---
Struggles with complex
Works for most
Flexibility   motion (rotation,
video content
deformation)
Block matching is the heart of motion estimation—it finds how
parts of an image move across frames, allowing modern codecs
to compress video efficiently without noticeable loss in quality.
2. Exhaustive Search:
The Exhaustive Search Approach (also called Full Search) in
motion estimation is the simplest and most accurate method for
finding motion vectors between frames in video compression. It
works by checking every possible block position within a
search window to find the best match.
🔹 Steps in Exhaustive Search
1. Divide the frame into blocks (e.g., 16×16 pixels).
2. Define a search window in the reference frame
(previous or future frame).
3. Compare the current block with all candidate blocks
inside the search window.
4. Compute similarity/difference using metrics like:
o SAD (Sum of Absolute Differences)
o MSE (Mean Squared Error)
5. Select the best match (the block with minimum error).
6. Record the displacement as the motion vector.
Feature   Description
Accuracy   Highest, since all possibilities are checked
Complexity Very high computational cost
Speed   Slow, especially for large search windows
Benchmarking, high-quality encoding, small-scale
Use Case
applications
• Advantages:
o Guarantees the best possible motion vector.
o Simple to implement conceptually.
o Provides a baseline for comparing other faster
algorithms.
•   Limitations:
o Extremely computationally expensive (O(N²)
comparisons per block).
o Not practical for real-time encoding or high-
resolution video.
o Power-hungry for hardware implementations.
Exhaustive search is the gold standard for accuracy in motion
estimation but is rarely used in practice due to its heavy
computational load. Instead, faster algorithms like Three-Step
Search, Diamond Search, or Hierarchical Search are often
used, trading a little accuracy for massive speed gains.
********** 8   **********
--- page 9 ---
Would you like me to also walk you through one of these faster
alternatives (like Three-Step Search) so you can see how they
improve efficiency compared to exhaustive search?
7 A   [10]
[CO3, BL4]   Analyze the impact of following structuring elements:
Diamond and line on any suitable digital image.
Students are expected to [ 2 Marks each]
1. Generate a Gray scale digital image matrix
2. Generate 3x3 structuring element contains
diamond shape in it
3. Apply the structuring element and showcase the
step by step working of any one morphological
operations [erosion /dilation]
4. Generate 3x3 structuring element containing line
shape in it.
5. Apply the structuring element and showcase the
step by step working of any same morphological
operation applied on original input image as did
in step 3. Compare results of step 3 & 5. Justify
the result.
7 B   [10]
[CO3, BL4]   Analyze the impact of Sobel and Prewitt operators on a digital
image.
Students are expected to [ 2 Marks each]
1. Generate a Gray scale digital image matrix
2. Generate Sobel matrix (Gx, Gy and combined)
3. Apply the Sobel on input image showcase the
step by step working of it.
4. Generate Prewitt matrix (Gx, Gy and combined)
5. Apply the Prewitt operator on the input image
matrix. showcase the step by step working of it.
Compare results of step 3 & 5. Justify the result.
********** 9   **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 439110c20dea

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CS_7055/Image and Video Processing/ANS_Image and Video Processing(702EX0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: mixed (18 pages), mean OCR confidence 67.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Image and Video Processing
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Compute D4, D8 and De distances between pixel “p” and “q” for V = {2,3,4}   [4]
SO-1;
BL-2   3   2   1   3   1
4   2   3(q)   6   2
5   3   2   3   5
2(p)   4   3   4   6
4   5   2   3   3
Answer:
Co-ordinates for (p x, y, q s, t) are p (3, 0) and q (1, 2).
D4 (p, q) = |(𝑥−𝑠)| + |𝑦−𝑡| = 2+2 = 4   (1 mark)
𝐷8 = max(2, 2) = 2 (1 mark)
𝐷𝑒= √22 + 22 = √8 ≈2.828 (2 marks)
CO-2;   b.   Differentiate between Point Processing and Neighborhood Processing techniques in image   [4]
SO-1;   processing.
BL-3
********** 1 **********
--- page 2 ---
Answer:
Point Processing   Neighborhood Processing
Output pixel depends only on the   Output pixel depends on the intensity
intensity of the same input pixel   values of neighboring pixels
Image negative, Contrast stretching,
Filtering, Smoothing, Edge detection
Thresholding
Complex, requires kernel/mask
Simple, faster (pixel-wise operations)
operations
Local region around the pixel is
Local to a single pixel
considered
1 mark for each difference
CO-3;   c.   State morphological dilation. Perform morphological dilation on the following image for   [4]
SO-1;   object ‘A’ using the structuring element ‘B’. Circle indicates origin
BL-4
A =
0   0   0   0
0   1   1   0
0   0   1   0
0   0   0   0
B =
1
1
Answer
Output image, 𝐴⨁𝐵:
0   1   1   0
0   1   1   0
0   0   1   0
0   0   0   0
********** 2 **********
--- page 3 ---
Dilation definition: 2 Marks
Output Image: 2 Marks
CO-4;   d. What is image segmentation? Consider the following 5 × 5 grayscale image:   [4]
SO-1;
BL-4   200   50   10   101   99
105   250   255   103   56
200   102   55   204   210
110   98   99   77   65
199   204   97   101   99
Perform image segmentation using global thresholding with threshold 𝑇= 100. Write the
segmented binary image.
Answer:
Image segmentation definition: 1 mark
Image segmentation using Thresholding rule: 1 mark
Segmented binary image: 2 marks
1   0   0   1   0
1   1   1   1   0
1   1   0   1   1
1   0   0   0   0
1   1   0   1   0
CO-5;   e. Define digital video. List and explain any two key parameters that determine video quality.   [4]
SO-1;
BL-2   Hint:
Frame rate, resolution, colour depth — higher values improve quality but increase data rate.
Definition – 1mark
Any two key parameters – 3marks
Q2   a   Compute the gray level distribution using histogram equalization of the following image [10]
matrix having 8 gray levels (0–7). Also draw the original and equalized histogram.
CO-2;
SO-1;
BL-3
********** 3 **********
--- page 4 ---
2   5   3   5   2
1   1   2   1   1
5   2   5   5   2
2   1   1   1   1
3   2   5   5   2
Answer:
.
1) Histogram equalization steps (6 marks)
2) I/P and O/P histograms (4 marks).
rₖ   nₖ   p(rₖ) (PDF)   P(rₖ) (CDF)   SK = 7×P(rk)   Rounded SK
(exact)
0   0   0.000   0.000   0.00   0
1   8   0.320   0.320   2.24   2
2   8   0.320   0.640   4.48   4
3   2   0.080   0.720   5.04   5
4   0   0.000   0.720   5.04   5
5   7   0.280   1.000   7.00   7
6   0   0.000   1.000   7.00   7
7   0   0.000   1.000   7.00   7
New Gray levels New no. of pixels
0   0
2   8
4   8
5   2
7   7
********** 4 **********
--- page 5 ---
Q2   b   Convert an RGB pixel (R = 100, G = 150, B = 200) into CMY color model Also write at   [10]
least three applications of CMY model.
CO-2;
SO-1;
BL-3   Answer:
The CMY color model is a subtractive color model used in color printing. It represents
colors using Cyan (C), Magenta (M), and Yellow (Y) components. CMY is derived from
the RGB model, which is additive.
The relationship between the two models is:
𝐶= 1 −(𝑅/255)
𝑀= 1 −(𝐺/255)
𝑌= 1 −(𝐵/255)
Formula (3 Marks)
Calculation (3 Marks)
Component Formula Calculation   Result
C   −𝑅   −100   0.6078
1   1   = 1 −0.3922
255   255
M   −𝐺   −150   0.4118
1   1   = 1 −0.5882
255   255
Y   −𝐵   −200   0.2157
1   1   = 1 −0.7843
255   255
Final CMY Values (1 Mark)
(𝐶, 𝑀, 𝑌) = (0.6078,0.4118,0.2157)
Applications of CMY Color Model (3 Marks)
• Used in color printing and photographic reproduction.
• Used in scanners, copiers, and inkjet printers.
•   Suitable for subtractive mixing, where white light is reflected from paper.
********** 5 **********
--- page 6 ---
Q3   a   Find a 2-dimensional Discrete Fourier Transform (DFT) of the following image ‘f’   [4]
using the twiddle matrix.
CO-2;
SO-1;   𝑓= [1 2
BL-3   1 5]
Answer:
𝐹(𝑢, 𝑣) = 𝑊 . 𝑓(𝑥, 𝑦) . 𝑊𝑇
𝐹(𝑢, 𝑣) = [1 1   . [1 2   . [1 1
1 −1]   1 5]   1 −1]
𝐹(𝑢, 𝑣) = [2 7   . [1 1 = [ 9 −5 ]
0 −3]   1 −1]   −3 3
Q3   b   Apply the Horizontal and Vertical Prewitt operators to detect edges on the following image,   [8]
then compute the gradient magnitude, using pixel replication at borders.
CO-3;
SO-1;   100   100   20   20
BL-4
100   100   20   20
100   100   20   20
100   100   20   20
Answer:
********** 6 **********

[Text in pictures on this page, read by OCR]
Prewitt kernels:
-1 01 1 1 1
G,-—|-1 0 1 Gy -—|0 0 0
-1 01 -1 -1 -1
--- page 7 ---
Prewitt kernels – 1 mark
Gx Matrix - 2marks
Gy Matrix - 2marks
Formula of M - 1marks
Output Matrix - 2marks
Q3   c What is morphological closing? Perform morphological closing on the following 9x9   [8]
image for object ‘A’ using the structuring element ‘B’.
CO-3;
SO-1;   0   0   0   0   0   0   0   0   0
BL-4   0   0   0   0   0   0   0   0   0
0   0   0   1   1   1   0   0   0
0   0   1   1   0   1   1   0   0
0   0   1   0   0   0   1   0   0
0   0   1   1   0   1   1   0   0
0   0   0   1   1   1   0   0   0
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
Image, 1-valued elements indicate ‘A’
********** 7 **********

[Text in pictures on this page, read by OCR]
Horizontal derivative G_:

0 —240 —240
0 —240 —240
0 —240 —240
0 —240 —240

Vertical derivative Gy:

Gradient magnitude M = ,/G? + G3 = |G;':

0 240 240
0 240 240
0 240 240
0 240 240

M=
--- page 8 ---
1   1   1
1   1   1
1   0   1
Structuring element ‘B’, Center position is origin
Answer:
Morphological closing definition: 2 marks
Image after dilation: 3 marks
After erosion (Final Image): 3 marks
********** 8 **********

[Text in pictures on this page, read by OCR]
After Dilation (A ©® B):

(2) 12)
1 12)
1 1
1 1
1 1
1 1
1 1
1 12)
(2) 12)
OB):
(2) (2)
(2) 12)
(2) 12)
1 12)
1 @
1 (2)
(2) 12)
12) 12)
2) 12)
--- page 9 ---
Q4   a   Consider the given input image given below. Sketch and apply 3x3 Laplacian filter having [4]
positive centre without diagonal elements to get the response on the shaded (underlined)
CO-2;   central 3 x 3 pixels of the input image.
SO-1;
BL-3
10 10 10 10 10
10 10 10 10 10
50 50 50 50   50
50 50 50 50 50
50 50 50 50 50
Answer: 3 x3 Laplacian filter having positive centre without diagonal elements: (1 mark)
0   -1   0
-1   4   -1
0   -1   0
Convolution and output: (3 marks)
Final o/p image =
10   10   10   10   10
10   − 40 − 40 − 40   10
50   40   40   40   50
50   0   0   0   50
50   50   50   50   50
Q4   b. Find the 2-dimensional Discrete Cosine Transform (DCT) of the following image ‘f’.   [8]
CO-2;   2 4 4 2
SO-1;   4 6 8 3
𝑓= [   ]
BL-3   2 8 10 4
3 8 6 2
********** 9 **********
--- page 10 ---
Answer:
DCT matrix (2 marks)
𝐹= 𝐶. 𝑓. 𝐶𝑇   (1 mark)
5.5   13   14   5.5
𝐶. 𝑓= [ −0.112 −3.153 −1.847 −0.2705 ]   (2 marks)
−0.5   −1   −4   −1.5
−1.5765   0.224   0.765   0.653
19   −0.2705   −8   0.653
𝐹= 𝐶. 𝑓. 𝐶𝑇= [ −2.691 −0.2498   2.309   0.8957 ]   (3marks)
−3.5   1.4645   1.5   −1.6885
0.0327 −1.6022 −0.956 −0.2498
Q4   c   Discuss the classification of video frames based on their encoding techniques. Explain how   [8]
intra-frame and inter-frame coding differ in reducing redundancy.
CO-5;
SO-1;
BL-2   Answer:
Classification of video frames – 6 marks
In video compression (e.g., MPEG, H.264), frames are classified based on how they are
encoded:
1. I-Frame (Intra-coded Frame):
o Encoded independently without reference to other frames.
o Acts like a still image (JPEG).
o Provides random access points for decoding.
o Large in size but high in quality.
2. P-Frame (Predicted Frame):
o Encoded using motion-compensated prediction from a previous I or P frame.
o Stores only changes (differences) from reference frame.
o Smaller size than I-frames.
3. B-Frame (Bi-directional Predicted Frame):
o Uses data from both previous and future I or P frames for prediction.
o Achieves highest compression efficiency.
o Requires more computation and not used for random access.
Differences: 2marks
Intra = independent → higher quality, more bits.
Intra-frame coding reduces spatial redundancy within a frame.
Inter = dependent → higher compression, less data.
Inter-frame coding reduces temporal redundancy across frames, leading to more
efficient video compression.
********** 10 **********
--- page 11 ---
Q5   a   Using the Sobel operator, compute the gradient direction at the center pixel of the following   [4]
3×3 image.
CO-3;
SO-1;   10 20 30
BL-4
5   15 25
0   10 20
Answer:
Mask – 2 marks
Gx, Gy - 1 mark
Direction - 1 mark
Q5   b   Using Otsu’s method, find the optimal threshold that separates the image into two classes. [8]
Compute the between-class variance (𝜎𝐵 2) for thresholds T = 2 and 3 only.
CO-4;
SO-1;
BL-4
********** 11 **********

[Text in pictures on this page, read by OCR]
Gz = (—1)(10) + (0)(20) + (1)(80) + (—2)(5) + (0)(15) + (2)(25) + (—1)(0) + (0)(20) + (1)(20)
G, = (—10+0+30-10+0+4+50+0+0+ 20) = 80

Gy = (1)(10) + (2)(20) + (1)(80) + (0)(5) + (0)(15) + (0)(25) + (-1)(0) + (—2)(10) + (—1)(20)
G, = (10 + 40 + 30 +0 +0+0~-0- 20-20) = 40

Gz =80, Gy=40

Gradient Direction:

G 40
6=tan? (2) = tan! ) = tan7!(0.5) = 26.56°

r
--- page 12 ---
5   7   1   2   1
6   2   4   1   2
4   0   5   6   0
3   5   2   1   1
2   7   5   3   3
Answer:
T   w₀   w₁   μ₀   μ₁   σB²
2   0.48   0.52   1.2500   4.8462   3.22791
3   0.60   0.40   1.6000   5.4000   3.46560
For T=2
Background and foreground mean calculations (1 marks)
P1 calculation (1 marks)
Between class variance (1mark)
For T=3
Background and foreground mean calculations (1 marks)
P1 calculation (1 marks)
Between class variance (1 mark)
Optimum threshold at which σB² is maximum is T = 3 (2 marks)
Q5   c   Perform the Hit-or-Miss Transform on the following 10x10 binary image A to detect the   [8]
pattern represented by the structuring element B.
CO-3;
SO-1;
BL-4
********** 12 **********
--- page 13 ---
Answer:
Formula — HMT (A, B) = (A@B1)N(ASOBz2) (1mark)

Erosion A © B, (2marks)

68@@e@88860 6 6
8eeoee8 88 B

A‘ (1 mark)

FIR ICR 7] QI HO
--- page 14 ---
Erosion A° © Bz (2 marks)

Output (2marks)

FRR IC 7 I OH
--- page 15 ---
Q6   a   Compare JPEG and TIFF image file formats.   [4]
CO-1;
SO-1;   Answer
BL-2
Any 4 comparison points for 4 marks:
Feature   JPEG (Joint Photographic   TIFF (Tagged Image File Format)
Experts Group)
1. Compression   Uses lossy compression —   Supports lossless or lossy
Type   some image quality is lost to   compression — retains full image
reduce file size.   quality if lossless is used.
2. File Size   Smaller file size due to   Larger file size because of high-
compression.   quality, detailed data storage.
3. Image   Slight loss of detail; suitable   High-quality images suitable for
Quality   for photographs and web use.   printing, editing, and archiving.
4. Layers and   Does not support layers or   Supports layers, multiple pages,
Transparency   transparency.   and transparency.
5. Common   Web images, digital cameras, Scanning, printing, professional
Uses   social media.   photography, and image editing.
6. File   .jpg or .jpeg   .tif or .tiff
Extension
Q6   b What is Region-Based image segmentation? Consider the following 5×5 image where the [8]
gray-level intensity values are given. Use the Region Growing technique starting from the
CO-4;   seed pixel (marked in bold and underlined) with a threshold T=2. Use 4-connectivity. Identify
SO-1;   the final grown region.
BL-4
5   4   5   6   8
5   6   7   7   9
4   5   6   7   8
2   4   5   6   7
1   3   4   5   6
Answer:
Region-Based Image segmentation definition - 2 marks
Region growing: Conditions and steps - 4marks
Final Output: 2 marks
********** 15 **********
--- page 16 ---
Region-Based Segmentation divides an image into regions that are homogeneous according
to predefined criteria such as intensity, color, or texture.
Given:
Seed pixel = (3,3) → Intensity = 6
Threshold 𝑇= 2
Neighboring criterion: |I(neighbor) – seed point| ≤ 2
Connectivity: 4-connected
All pixels with values 4, 5, 6, 7, and 8 form the segmented region.
Output:
1 1 1 1 1
1 1 1 1 0
1 1 1 1 1
0 1 1 1 1
0 0 1 1 1
Q6   c   Explain different color models and their importance in image processing.   [8]
CO-1;
SO-1;
BL-2   Answer:
Meaning of Color Models
A color model is a mathematical and systematic way to represent colors as tuples of
numerical values.
Each color model defines a color space, where every color can be represented using specific
parameters such as Red, Green, and Blue (RGB) or Hue, Saturation, and Intensity (HSI).
These models are essential because digital systems (cameras, monitors, printers) store and
process color as numbers — not as visual hues.
Common Colour Models in Image Processing
Color Model   Components Description / Use
RGB   (Red,   Green, (R, G, B)   Additive color model where colors are formed
Blue)   by combining red, green, and blue light. Used
in display devices like monitors and cameras.
CMY / CMYK (Cyan, (C, M, Y, Subtractive model used in printing; colors are
Magenta,   Yellow, [K])   obtained by absorbing (subtracting) light.
[Black])
********** 16 **********
--- page 17 ---
HSI   / HSV (Hue, (H, S, I)   Separates   color information (Hue and
Saturation,   Saturation) from   brightness   (Intensity).
Intensity/Value)   Useful for image segmentation and color
enhancement.
YUV / YCbCr   (Y, U, V) or Separates luminance (Y) and chrominance
(Y, Cb, Cr)   (Cb, Cr). Used in video compression
standards (e.g., JPEG, MPEG).
Importance of colour models:
• Represent colors numerically for processing
• Allow manipulation, enhancement, compression
Colour models, Description, Application, Importance – 2 marks each
Q7   a   Explain 2D-Log Search motion estimation algorithms. Discuss its advantages and [10]
disadvantages.
CO-5;
SO-1;   Answer:
BL-2   2D-Log Search motion estimation algorithms – 6marks
Advantages and disadvantages – 4marks
Q7   b   Explain Digital negative and thresholding related to point processing techniques of image [10]
processing. Perform intensity level slicing with preserving background on the given 3-bit
CO-2;   image. Let r1 = 3 & r2 = 5. Draw the modified image using with background
SO-1;   transformation.
BL-3
2   1   2   2   1
2   3   4   5   2
6   2   7   6   0
2   6   6   5   1
0   3   2   2   1
Answer:
Digital negative and thresholding explanation 5marks
Gray level slicing with background;   5marks
s = r for, r < r1   Range: [0,1,2]
s = 7 for, r1 ≤ r ≤ r2 Range: [3,4,5]
s = r for, r > r2 Range: [6,7]
********** 17 **********
--- page 18 ---
Therefore, the modified output image is;

FR ICR 7] QA HH
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 20373f098710

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_Computer_7002/Image and Video Processing/ANS_Image and Video Processing(702EX0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: mixed (18 pages), mean OCR confidence 67.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Image and Video Processing
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Compute D4, D8 and De distances between pixel “p” and “q” for V = {2,3,4}   [4]
SO-1;
BL-2   3   2   1   3   1
4   2   3(q)   6   2
5   3   2   3   5
2(p)   4   3   4   6
4   5   2   3   3
Answer:
Co-ordinates for (p x, y, q s, t) are p (3, 0) and q (1, 2).
D4 (p, q) = |(𝑥−𝑠)| + |𝑦−𝑡| = 2+2 = 4   (1 mark)
𝐷8 = max(2, 2) = 2 (1 mark)
𝐷𝑒= √22 + 22 = √8 ≈2.828 (2 marks)
CO-2;   b.   Differentiate between Point Processing and Neighborhood Processing techniques in image   [4]
SO-1;   processing.
BL-3
********** 1 **********
--- page 2 ---
Answer:
Point Processing   Neighborhood Processing
Output pixel depends only on the   Output pixel depends on the intensity
intensity of the same input pixel   values of neighboring pixels
Image negative, Contrast stretching,
Filtering, Smoothing, Edge detection
Thresholding
Complex, requires kernel/mask
Simple, faster (pixel-wise operations)
operations
Local region around the pixel is
Local to a single pixel
considered
1 mark for each difference
CO-3;   c.   State morphological dilation. Perform morphological dilation on the following image for   [4]
SO-1;   object ‘A’ using the structuring element ‘B’. Circle indicates origin
BL-4
A =
0   0   0   0
0   1   1   0
0   0   1   0
0   0   0   0
B =
1
1
Answer
Output image, 𝐴⨁𝐵:
0   1   1   0
0   1   1   0
0   0   1   0
0   0   0   0
********** 2 **********
--- page 3 ---
Dilation definition: 2 Marks
Output Image: 2 Marks
CO-4;   d. What is image segmentation? Consider the following 5 × 5 grayscale image:   [4]
SO-1;
BL-4   200   50   10   101   99
105   250   255   103   56
200   102   55   204   210
110   98   99   77   65
199   204   97   101   99
Perform image segmentation using global thresholding with threshold 𝑇= 100. Write the
segmented binary image.
Answer:
Image segmentation definition: 1 mark
Image segmentation using Thresholding rule: 1 mark
Segmented binary image: 2 marks
1   0   0   1   0
1   1   1   1   0
1   1   0   1   1
1   0   0   0   0
1   1   0   1   0
CO-5;   e. Define digital video. List and explain any two key parameters that determine video quality.   [4]
SO-1;
BL-2   Hint:
Frame rate, resolution, colour depth — higher values improve quality but increase data rate.
Definition – 1mark
Any two key parameters – 3marks
Q2   a   Compute the gray level distribution using histogram equalization of the following image [10]
matrix having 8 gray levels (0–7). Also draw the original and equalized histogram.
CO-2;
SO-1;
BL-3
********** 3 **********
--- page 4 ---
2   5   3   5   2
1   1   2   1   1
5   2   5   5   2
2   1   1   1   1
3   2   5   5   2
Answer:
.
1) Histogram equalization steps (6 marks)
2) I/P and O/P histograms (4 marks).
rₖ   nₖ   p(rₖ) (PDF)   P(rₖ) (CDF)   SK = 7×P(rk)   Rounded SK
(exact)
0   0   0.000   0.000   0.00   0
1   8   0.320   0.320   2.24   2
2   8   0.320   0.640   4.48   4
3   2   0.080   0.720   5.04   5
4   0   0.000   0.720   5.04   5
5   7   0.280   1.000   7.00   7
6   0   0.000   1.000   7.00   7
7   0   0.000   1.000   7.00   7
New Gray levels New no. of pixels
0   0
2   8
4   8
5   2
7   7
********** 4 **********
--- page 5 ---
Q2   b   Convert an RGB pixel (R = 100, G = 150, B = 200) into CMY color model Also write at   [10]
least three applications of CMY model.
CO-2;
SO-1;
BL-3   Answer:
The CMY color model is a subtractive color model used in color printing. It represents
colors using Cyan (C), Magenta (M), and Yellow (Y) components. CMY is derived from
the RGB model, which is additive.
The relationship between the two models is:
𝐶= 1 −(𝑅/255)
𝑀= 1 −(𝐺/255)
𝑌= 1 −(𝐵/255)
Formula (3 Marks)
Calculation (3 Marks)
Component Formula Calculation   Result
C   −𝑅   −100   0.6078
1   1   = 1 −0.3922
255   255
M   −𝐺   −150   0.4118
1   1   = 1 −0.5882
255   255
Y   −𝐵   −200   0.2157
1   1   = 1 −0.7843
255   255
Final CMY Values (1 Mark)
(𝐶, 𝑀, 𝑌) = (0.6078,0.4118,0.2157)
Applications of CMY Color Model (3 Marks)
• Used in color printing and photographic reproduction.
• Used in scanners, copiers, and inkjet printers.
•   Suitable for subtractive mixing, where white light is reflected from paper.
********** 5 **********
--- page 6 ---
Q3   a   Find a 2-dimensional Discrete Fourier Transform (DFT) of the following image ‘f’   [4]
using the twiddle matrix.
CO-2;
SO-1;   𝑓= [1 2
BL-3   1 5]
Answer:
𝐹(𝑢, 𝑣) = 𝑊 . 𝑓(𝑥, 𝑦) . 𝑊𝑇
𝐹(𝑢, 𝑣) = [1 1   . [1 2   . [1 1
1 −1]   1 5]   1 −1]
𝐹(𝑢, 𝑣) = [2 7   . [1 1 = [ 9 −5 ]
0 −3]   1 −1]   −3 3
Q3   b   Apply the Horizontal and Vertical Prewitt operators to detect edges on the following image,   [8]
then compute the gradient magnitude, using pixel replication at borders.
CO-3;
SO-1;   100   100   20   20
BL-4
100   100   20   20
100   100   20   20
100   100   20   20
Answer:
********** 6 **********

[Text in pictures on this page, read by OCR]
Prewitt kernels:
-1 01 1 1 1
G,-—|-1 0 1 Gy -—|0 0 0
-1 01 -1 -1 -1
--- page 7 ---
Prewitt kernels – 1 mark
Gx Matrix - 2marks
Gy Matrix - 2marks
Formula of M - 1marks
Output Matrix - 2marks
Q3   c What is morphological closing? Perform morphological closing on the following 9x9   [8]
image for object ‘A’ using the structuring element ‘B’.
CO-3;
SO-1;   0   0   0   0   0   0   0   0   0
BL-4   0   0   0   0   0   0   0   0   0
0   0   0   1   1   1   0   0   0
0   0   1   1   0   1   1   0   0
0   0   1   0   0   0   1   0   0
0   0   1   1   0   1   1   0   0
0   0   0   1   1   1   0   0   0
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
Image, 1-valued elements indicate ‘A’
********** 7 **********

[Text in pictures on this page, read by OCR]
Horizontal derivative G_:

0 —240 —240
0 —240 —240
0 —240 —240
0 —240 —240

Vertical derivative Gy:

Gradient magnitude M = ,/G? + G3 = |G;':

0 240 240
0 240 240
0 240 240
0 240 240

M=
--- page 8 ---
1   1   1
1   1   1
1   0   1
Structuring element ‘B’, Center position is origin
Answer:
Morphological closing definition: 2 marks
Image after dilation: 3 marks
After erosion (Final Image): 3 marks
********** 8 **********

[Text in pictures on this page, read by OCR]
After Dilation (A ©® B):

(2) 12)
1 12)
1 1
1 1
1 1
1 1
1 1
1 12)
(2) 12)
OB):
(2) (2)
(2) 12)
(2) 12)
1 12)
1 @
1 (2)
(2) 12)
12) 12)
2) 12)
--- page 9 ---
Q4   a   Consider the given input image given below. Sketch and apply 3x3 Laplacian filter having [4]
positive centre without diagonal elements to get the response on the shaded (underlined)
CO-2;   central 3 x 3 pixels of the input image.
SO-1;
BL-3
10 10 10 10 10
10 10 10 10 10
50 50 50 50   50
50 50 50 50 50
50 50 50 50 50
Answer: 3 x3 Laplacian filter having positive centre without diagonal elements: (1 mark)
0   -1   0
-1   4   -1
0   -1   0
Convolution and output: (3 marks)
Final o/p image =
10   10   10   10   10
10   − 40 − 40 − 40   10
50   40   40   40   50
50   0   0   0   50
50   50   50   50   50
Q4   b. Find the 2-dimensional Discrete Cosine Transform (DCT) of the following image ‘f’.   [8]
CO-2;   2 4 4 2
SO-1;   4 6 8 3
𝑓= [   ]
BL-3   2 8 10 4
3 8 6 2
********** 9 **********
--- page 10 ---
Answer:
DCT matrix (2 marks)
𝐹= 𝐶. 𝑓. 𝐶𝑇   (1 mark)
5.5   13   14   5.5
𝐶. 𝑓= [ −0.112 −3.153 −1.847 −0.2705 ]   (2 marks)
−0.5   −1   −4   −1.5
−1.5765   0.224   0.765   0.653
19   −0.2705   −8   0.653
𝐹= 𝐶. 𝑓. 𝐶𝑇= [ −2.691 −0.2498   2.309   0.8957 ]   (3marks)
−3.5   1.4645   1.5   −1.6885
0.0327 −1.6022 −0.956 −0.2498
Q4   c   Discuss the classification of video frames based on their encoding techniques. Explain how   [8]
intra-frame and inter-frame coding differ in reducing redundancy.
CO-5;
SO-1;
BL-2   Answer:
Classification of video frames – 6 marks
In video compression (e.g., MPEG, H.264), frames are classified based on how they are
encoded:
1. I-Frame (Intra-coded Frame):
o Encoded independently without reference to other frames.
o Acts like a still image (JPEG).
o Provides random access points for decoding.
o Large in size but high in quality.
2. P-Frame (Predicted Frame):
o Encoded using motion-compensated prediction from a previous I or P frame.
o Stores only changes (differences) from reference frame.
o Smaller size than I-frames.
3. B-Frame (Bi-directional Predicted Frame):
o Uses data from both previous and future I or P frames for prediction.
o Achieves highest compression efficiency.
o Requires more computation and not used for random access.
Differences: 2marks
Intra = independent → higher quality, more bits.
Intra-frame coding reduces spatial redundancy within a frame.
Inter = dependent → higher compression, less data.
Inter-frame coding reduces temporal redundancy across frames, leading to more
efficient video compression.
********** 10 **********
--- page 11 ---
Q5   a   Using the Sobel operator, compute the gradient direction at the center pixel of the following   [4]
3×3 image.
CO-3;
SO-1;   10 20 30
BL-4
5   15 25
0   10 20
Answer:
Mask – 2 marks
Gx, Gy - 1 mark
Direction - 1 mark
Q5   b   Using Otsu’s method, find the optimal threshold that separates the image into two classes. [8]
Compute the between-class variance (𝜎𝐵 2) for thresholds T = 2 and 3 only.
CO-4;
SO-1;
BL-4
********** 11 **********

[Text in pictures on this page, read by OCR]
Gz = (—1)(10) + (0)(20) + (1)(80) + (—2)(5) + (0)(15) + (2)(25) + (—1)(0) + (0)(20) + (1)(20)
G, = (—10+0+30-10+0+4+50+0+0+ 20) = 80

Gy = (1)(10) + (2)(20) + (1)(80) + (0)(5) + (0)(15) + (0)(25) + (-1)(0) + (—2)(10) + (—1)(20)
G, = (10 + 40 + 30 +0 +0+0~-0- 20-20) = 40

Gz =80, Gy=40

Gradient Direction:

G 40
6=tan? (2) = tan! ) = tan7!(0.5) = 26.56°

r
--- page 12 ---
5   7   1   2   1
6   2   4   1   2
4   0   5   6   0
3   5   2   1   1
2   7   5   3   3
Answer:
T   w₀   w₁   μ₀   μ₁   σB²
2   0.48   0.52   1.2500   4.8462   3.22791
3   0.60   0.40   1.6000   5.4000   3.46560
For T=2
Background and foreground mean calculations (1 marks)
P1 calculation (1 marks)
Between class variance (1mark)
For T=3
Background and foreground mean calculations (1 marks)
P1 calculation (1 marks)
Between class variance (1 mark)
Optimum threshold at which σB² is maximum is T = 3 (2 marks)
Q5   c   Perform the Hit-or-Miss Transform on the following 10x10 binary image A to detect the   [8]
pattern represented by the structuring element B.
CO-3;
SO-1;
BL-4
********** 12 **********
--- page 13 ---
Answer:
Formula — HMT (A, B) = (A@B1)N(ASOBz2) (1mark)

Erosion A © B, (2marks)

68@@e@88860 6 6
8eeoee8 88 B

A‘ (1 mark)

FIR ICR 7] QI HO
--- page 14 ---
Erosion A° © Bz (2 marks)

Output (2marks)

FRR IC 7 I OH
--- page 15 ---
Q6   a   Compare JPEG and TIFF image file formats.   [4]
CO-1;
SO-1;   Answer
BL-2
Any 4 comparison points for 4 marks:
Feature   JPEG (Joint Photographic   TIFF (Tagged Image File Format)
Experts Group)
1. Compression   Uses lossy compression —   Supports lossless or lossy
Type   some image quality is lost to   compression — retains full image
reduce file size.   quality if lossless is used.
2. File Size   Smaller file size due to   Larger file size because of high-
compression.   quality, detailed data storage.
3. Image   Slight loss of detail; suitable   High-quality images suitable for
Quality   for photographs and web use.   printing, editing, and archiving.
4. Layers and   Does not support layers or   Supports layers, multiple pages,
Transparency   transparency.   and transparency.
5. Common   Web images, digital cameras, Scanning, printing, professional
Uses   social media.   photography, and image editing.
6. File   .jpg or .jpeg   .tif or .tiff
Extension
Q6   b What is Region-Based image segmentation? Consider the following 5×5 image where the [8]
gray-level intensity values are given. Use the Region Growing technique starting from the
CO-4;   seed pixel (marked in bold and underlined) with a threshold T=2. Use 4-connectivity. Identify
SO-1;   the final grown region.
BL-4
5   4   5   6   8
5   6   7   7   9
4   5   6   7   8
2   4   5   6   7
1   3   4   5   6
Answer:
Region-Based Image segmentation definition - 2 marks
Region growing: Conditions and steps - 4marks
Final Output: 2 marks
********** 15 **********
--- page 16 ---
Region-Based Segmentation divides an image into regions that are homogeneous according
to predefined criteria such as intensity, color, or texture.
Given:
Seed pixel = (3,3) → Intensity = 6
Threshold 𝑇= 2
Neighboring criterion: |I(neighbor) – seed point| ≤ 2
Connectivity: 4-connected
All pixels with values 4, 5, 6, 7, and 8 form the segmented region.
Output:
1 1 1 1 1
1 1 1 1 0
1 1 1 1 1
0 1 1 1 1
0 0 1 1 1
Q6   c   Explain different color models and their importance in image processing.   [8]
CO-1;
SO-1;
BL-2   Answer:
Meaning of Color Models
A color model is a mathematical and systematic way to represent colors as tuples of
numerical values.
Each color model defines a color space, where every color can be represented using specific
parameters such as Red, Green, and Blue (RGB) or Hue, Saturation, and Intensity (HSI).
These models are essential because digital systems (cameras, monitors, printers) store and
process color as numbers — not as visual hues.
Common Colour Models in Image Processing
Color Model   Components Description / Use
RGB   (Red,   Green, (R, G, B)   Additive color model where colors are formed
Blue)   by combining red, green, and blue light. Used
in display devices like monitors and cameras.
CMY / CMYK (Cyan, (C, M, Y, Subtractive model used in printing; colors are
Magenta,   Yellow, [K])   obtained by absorbing (subtracting) light.
[Black])
********** 16 **********
--- page 17 ---
HSI   / HSV (Hue, (H, S, I)   Separates   color information (Hue and
Saturation,   Saturation) from   brightness   (Intensity).
Intensity/Value)   Useful for image segmentation and color
enhancement.
YUV / YCbCr   (Y, U, V) or Separates luminance (Y) and chrominance
(Y, Cb, Cr)   (Cb, Cr). Used in video compression
standards (e.g., JPEG, MPEG).
Importance of colour models:
• Represent colors numerically for processing
• Allow manipulation, enhancement, compression
Colour models, Description, Application, Importance – 2 marks each
Q7   a   Explain 2D-Log Search motion estimation algorithms. Discuss its advantages and [10]
disadvantages.
CO-5;
SO-1;   Answer:
BL-2   2D-Log Search motion estimation algorithms – 6marks
Advantages and disadvantages – 4marks
Q7   b   Explain Digital negative and thresholding related to point processing techniques of image [10]
processing. Perform intensity level slicing with preserving background on the given 3-bit
CO-2;   image. Let r1 = 3 & r2 = 5. Draw the modified image using with background
SO-1;   transformation.
BL-3
2   1   2   2   1
2   3   4   5   2
6   2   7   6   0
2   6   6   5   1
0   3   2   2   1
Answer:
Digital negative and thresholding explanation 5marks
Gray level slicing with background;   5marks
s = r for, r < r1   Range: [0,1,2]
s = 7 for, r1 ≤ r ≤ r2 Range: [3,4,5]
s = r for, r > r2 Range: [6,7]
********** 17 **********
--- page 18 ---
Therefore, the modified output image is;

FR ICR 7] QA HH
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper da9f4759f76e

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_Computer_7047/Image and Video Processing/ANS_Image and Video Processing(702EX0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: mixed (18 pages), mean OCR confidence 67.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Image and Video Processing
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Compute D4, D8 and De distances between pixel “p” and “q” for V = {2,3,4}   [4]
SO-1;
BL-2   3   2   1   3   1
4   2   3(q)   6   2
5   3   2   3   5
2(p)   4   3   4   6
4   5   2   3   3
Answer:
Co-ordinates for (p x, y, q s, t) are p (3, 0) and q (1, 2).
D4 (p, q) = |(𝑥−𝑠)| + |𝑦−𝑡| = 2+2 = 4   (1 mark)
𝐷8 = max(2, 2) = 2 (1 mark)
𝐷𝑒= √22 + 22 = √8 ≈2.828 (2 marks)
CO-2;   b.   Differentiate between Point Processing and Neighborhood Processing techniques in image   [4]
SO-1;   processing.
BL-3
********** 1 **********
--- page 2 ---
Answer:
Point Processing   Neighborhood Processing
Output pixel depends only on the   Output pixel depends on the intensity
intensity of the same input pixel   values of neighboring pixels
Image negative, Contrast stretching,
Filtering, Smoothing, Edge detection
Thresholding
Complex, requires kernel/mask
Simple, faster (pixel-wise operations)
operations
Local region around the pixel is
Local to a single pixel
considered
1 mark for each difference
CO-3;   c.   State morphological dilation. Perform morphological dilation on the following image for   [4]
SO-1;   object ‘A’ using the structuring element ‘B’. Circle indicates origin
BL-4
A =
0   0   0   0
0   1   1   0
0   0   1   0
0   0   0   0
B =
1
1
Answer
Output image, 𝐴⨁𝐵:
0   1   1   0
0   1   1   0
0   0   1   0
0   0   0   0
********** 2 **********
--- page 3 ---
Dilation definition: 2 Marks
Output Image: 2 Marks
CO-4;   d. What is image segmentation? Consider the following 5 × 5 grayscale image:   [4]
SO-1;
BL-4   200   50   10   101   99
105   250   255   103   56
200   102   55   204   210
110   98   99   77   65
199   204   97   101   99
Perform image segmentation using global thresholding with threshold 𝑇= 100. Write the
segmented binary image.
Answer:
Image segmentation definition: 1 mark
Image segmentation using Thresholding rule: 1 mark
Segmented binary image: 2 marks
1   0   0   1   0
1   1   1   1   0
1   1   0   1   1
1   0   0   0   0
1   1   0   1   0
CO-5;   e. Define digital video. List and explain any two key parameters that determine video quality.   [4]
SO-1;
BL-2   Hint:
Frame rate, resolution, colour depth — higher values improve quality but increase data rate.
Definition – 1mark
Any two key parameters – 3marks
Q2   a   Compute the gray level distribution using histogram equalization of the following image [10]
matrix having 8 gray levels (0–7). Also draw the original and equalized histogram.
CO-2;
SO-1;
BL-3
********** 3 **********
--- page 4 ---
2   5   3   5   2
1   1   2   1   1
5   2   5   5   2
2   1   1   1   1
3   2   5   5   2
Answer:
.
1) Histogram equalization steps (6 marks)
2) I/P and O/P histograms (4 marks).
rₖ   nₖ   p(rₖ) (PDF)   P(rₖ) (CDF)   SK = 7×P(rk)   Rounded SK
(exact)
0   0   0.000   0.000   0.00   0
1   8   0.320   0.320   2.24   2
2   8   0.320   0.640   4.48   4
3   2   0.080   0.720   5.04   5
4   0   0.000   0.720   5.04   5
5   7   0.280   1.000   7.00   7
6   0   0.000   1.000   7.00   7
7   0   0.000   1.000   7.00   7
New Gray levels New no. of pixels
0   0
2   8
4   8
5   2
7   7
********** 4 **********
--- page 5 ---
Q2   b   Convert an RGB pixel (R = 100, G = 150, B = 200) into CMY color model Also write at   [10]
least three applications of CMY model.
CO-2;
SO-1;
BL-3   Answer:
The CMY color model is a subtractive color model used in color printing. It represents
colors using Cyan (C), Magenta (M), and Yellow (Y) components. CMY is derived from
the RGB model, which is additive.
The relationship between the two models is:
𝐶= 1 −(𝑅/255)
𝑀= 1 −(𝐺/255)
𝑌= 1 −(𝐵/255)
Formula (3 Marks)
Calculation (3 Marks)
Component Formula Calculation   Result
C   −𝑅   −100   0.6078
1   1   = 1 −0.3922
255   255
M   −𝐺   −150   0.4118
1   1   = 1 −0.5882
255   255
Y   −𝐵   −200   0.2157
1   1   = 1 −0.7843
255   255
Final CMY Values (1 Mark)
(𝐶, 𝑀, 𝑌) = (0.6078,0.4118,0.2157)
Applications of CMY Color Model (3 Marks)
• Used in color printing and photographic reproduction.
• Used in scanners, copiers, and inkjet printers.
•   Suitable for subtractive mixing, where white light is reflected from paper.
********** 5 **********
--- page 6 ---
Q3   a   Find a 2-dimensional Discrete Fourier Transform (DFT) of the following image ‘f’   [4]
using the twiddle matrix.
CO-2;
SO-1;   𝑓= [1 2
BL-3   1 5]
Answer:
𝐹(𝑢, 𝑣) = 𝑊 . 𝑓(𝑥, 𝑦) . 𝑊𝑇
𝐹(𝑢, 𝑣) = [1 1   . [1 2   . [1 1
1 −1]   1 5]   1 −1]
𝐹(𝑢, 𝑣) = [2 7   . [1 1 = [ 9 −5 ]
0 −3]   1 −1]   −3 3
Q3   b   Apply the Horizontal and Vertical Prewitt operators to detect edges on the following image,   [8]
then compute the gradient magnitude, using pixel replication at borders.
CO-3;
SO-1;   100   100   20   20
BL-4
100   100   20   20
100   100   20   20
100   100   20   20
Answer:
********** 6 **********

[Text in pictures on this page, read by OCR]
Prewitt kernels:
-1 01 1 1 1
G,-—|-1 0 1 Gy -—|0 0 0
-1 01 -1 -1 -1
--- page 7 ---
Prewitt kernels – 1 mark
Gx Matrix - 2marks
Gy Matrix - 2marks
Formula of M - 1marks
Output Matrix - 2marks
Q3   c What is morphological closing? Perform morphological closing on the following 9x9   [8]
image for object ‘A’ using the structuring element ‘B’.
CO-3;
SO-1;   0   0   0   0   0   0   0   0   0
BL-4   0   0   0   0   0   0   0   0   0
0   0   0   1   1   1   0   0   0
0   0   1   1   0   1   1   0   0
0   0   1   0   0   0   1   0   0
0   0   1   1   0   1   1   0   0
0   0   0   1   1   1   0   0   0
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
Image, 1-valued elements indicate ‘A’
********** 7 **********

[Text in pictures on this page, read by OCR]
Horizontal derivative G_:

0 —240 —240
0 —240 —240
0 —240 —240
0 —240 —240

Vertical derivative Gy:

Gradient magnitude M = ,/G? + G3 = |G;':

0 240 240
0 240 240
0 240 240
0 240 240

M=
--- page 8 ---
1   1   1
1   1   1
1   0   1
Structuring element ‘B’, Center position is origin
Answer:
Morphological closing definition: 2 marks
Image after dilation: 3 marks
After erosion (Final Image): 3 marks
********** 8 **********

[Text in pictures on this page, read by OCR]
After Dilation (A ©® B):

(2) 12)
1 12)
1 1
1 1
1 1
1 1
1 1
1 12)
(2) 12)
OB):
(2) (2)
(2) 12)
(2) 12)
1 12)
1 @
1 (2)
(2) 12)
12) 12)
2) 12)
--- page 9 ---
Q4   a   Consider the given input image given below. Sketch and apply 3x3 Laplacian filter having [4]
positive centre without diagonal elements to get the response on the shaded (underlined)
CO-2;   central 3 x 3 pixels of the input image.
SO-1;
BL-3
10 10 10 10 10
10 10 10 10 10
50 50 50 50   50
50 50 50 50 50
50 50 50 50 50
Answer: 3 x3 Laplacian filter having positive centre without diagonal elements: (1 mark)
0   -1   0
-1   4   -1
0   -1   0
Convolution and output: (3 marks)
Final o/p image =
10   10   10   10   10
10   − 40 − 40 − 40   10
50   40   40   40   50
50   0   0   0   50
50   50   50   50   50
Q4   b. Find the 2-dimensional Discrete Cosine Transform (DCT) of the following image ‘f’.   [8]
CO-2;   2 4 4 2
SO-1;   4 6 8 3
𝑓= [   ]
BL-3   2 8 10 4
3 8 6 2
********** 9 **********
--- page 10 ---
Answer:
DCT matrix (2 marks)
𝐹= 𝐶. 𝑓. 𝐶𝑇   (1 mark)
5.5   13   14   5.5
𝐶. 𝑓= [ −0.112 −3.153 −1.847 −0.2705 ]   (2 marks)
−0.5   −1   −4   −1.5
−1.5765   0.224   0.765   0.653
19   −0.2705   −8   0.653
𝐹= 𝐶. 𝑓. 𝐶𝑇= [ −2.691 −0.2498   2.309   0.8957 ]   (3marks)
−3.5   1.4645   1.5   −1.6885
0.0327 −1.6022 −0.956 −0.2498
Q4   c   Discuss the classification of video frames based on their encoding techniques. Explain how   [8]
intra-frame and inter-frame coding differ in reducing redundancy.
CO-5;
SO-1;
BL-2   Answer:
Classification of video frames – 6 marks
In video compression (e.g., MPEG, H.264), frames are classified based on how they are
encoded:
1. I-Frame (Intra-coded Frame):
o Encoded independently without reference to other frames.
o Acts like a still image (JPEG).
o Provides random access points for decoding.
o Large in size but high in quality.
2. P-Frame (Predicted Frame):
o Encoded using motion-compensated prediction from a previous I or P frame.
o Stores only changes (differences) from reference frame.
o Smaller size than I-frames.
3. B-Frame (Bi-directional Predicted Frame):
o Uses data from both previous and future I or P frames for prediction.
o Achieves highest compression efficiency.
o Requires more computation and not used for random access.
Differences: 2marks
Intra = independent → higher quality, more bits.
Intra-frame coding reduces spatial redundancy within a frame.
Inter = dependent → higher compression, less data.
Inter-frame coding reduces temporal redundancy across frames, leading to more
efficient video compression.
********** 10 **********
--- page 11 ---
Q5   a   Using the Sobel operator, compute the gradient direction at the center pixel of the following   [4]
3×3 image.
CO-3;
SO-1;   10 20 30
BL-4
5   15 25
0   10 20
Answer:
Mask – 2 marks
Gx, Gy - 1 mark
Direction - 1 mark
Q5   b   Using Otsu’s method, find the optimal threshold that separates the image into two classes. [8]
Compute the between-class variance (𝜎𝐵 2) for thresholds T = 2 and 3 only.
CO-4;
SO-1;
BL-4
********** 11 **********

[Text in pictures on this page, read by OCR]
Gz = (—1)(10) + (0)(20) + (1)(80) + (—2)(5) + (0)(15) + (2)(25) + (—1)(0) + (0)(20) + (1)(20)
G, = (—10+0+30-10+0+4+50+0+0+ 20) = 80

Gy = (1)(10) + (2)(20) + (1)(80) + (0)(5) + (0)(15) + (0)(25) + (-1)(0) + (—2)(10) + (—1)(20)
G, = (10 + 40 + 30 +0 +0+0~-0- 20-20) = 40

Gz =80, Gy=40

Gradient Direction:

G 40
6=tan? (2) = tan! ) = tan7!(0.5) = 26.56°

r
--- page 12 ---
5   7   1   2   1
6   2   4   1   2
4   0   5   6   0
3   5   2   1   1
2   7   5   3   3
Answer:
T   w₀   w₁   μ₀   μ₁   σB²
2   0.48   0.52   1.2500   4.8462   3.22791
3   0.60   0.40   1.6000   5.4000   3.46560
For T=2
Background and foreground mean calculations (1 marks)
P1 calculation (1 marks)
Between class variance (1mark)
For T=3
Background and foreground mean calculations (1 marks)
P1 calculation (1 marks)
Between class variance (1 mark)
Optimum threshold at which σB² is maximum is T = 3 (2 marks)
Q5   c   Perform the Hit-or-Miss Transform on the following 10x10 binary image A to detect the   [8]
pattern represented by the structuring element B.
CO-3;
SO-1;
BL-4
********** 12 **********
--- page 13 ---
Answer:
Formula — HMT (A, B) = (A@B1)N(ASOBz2) (1mark)

Erosion A © B, (2marks)

68@@e@88860 6 6
8eeoee8 88 B

A‘ (1 mark)

FIR ICR 7] QI HO
--- page 14 ---
Erosion A° © Bz (2 marks)

Output (2marks)

FRR IC 7 I OH
--- page 15 ---
Q6   a   Compare JPEG and TIFF image file formats.   [4]
CO-1;
SO-1;   Answer
BL-2
Any 4 comparison points for 4 marks:
Feature   JPEG (Joint Photographic   TIFF (Tagged Image File Format)
Experts Group)
1. Compression   Uses lossy compression —   Supports lossless or lossy
Type   some image quality is lost to   compression — retains full image
reduce file size.   quality if lossless is used.
2. File Size   Smaller file size due to   Larger file size because of high-
compression.   quality, detailed data storage.
3. Image   Slight loss of detail; suitable   High-quality images suitable for
Quality   for photographs and web use.   printing, editing, and archiving.
4. Layers and   Does not support layers or   Supports layers, multiple pages,
Transparency   transparency.   and transparency.
5. Common   Web images, digital cameras, Scanning, printing, professional
Uses   social media.   photography, and image editing.
6. File   .jpg or .jpeg   .tif or .tiff
Extension
Q6   b What is Region-Based image segmentation? Consider the following 5×5 image where the [8]
gray-level intensity values are given. Use the Region Growing technique starting from the
CO-4;   seed pixel (marked in bold and underlined) with a threshold T=2. Use 4-connectivity. Identify
SO-1;   the final grown region.
BL-4
5   4   5   6   8
5   6   7   7   9
4   5   6   7   8
2   4   5   6   7
1   3   4   5   6
Answer:
Region-Based Image segmentation definition - 2 marks
Region growing: Conditions and steps - 4marks
Final Output: 2 marks
********** 15 **********
--- page 16 ---
Region-Based Segmentation divides an image into regions that are homogeneous according
to predefined criteria such as intensity, color, or texture.
Given:
Seed pixel = (3,3) → Intensity = 6
Threshold 𝑇= 2
Neighboring criterion: |I(neighbor) – seed point| ≤ 2
Connectivity: 4-connected
All pixels with values 4, 5, 6, 7, and 8 form the segmented region.
Output:
1 1 1 1 1
1 1 1 1 0
1 1 1 1 1
0 1 1 1 1
0 0 1 1 1
Q6   c   Explain different color models and their importance in image processing.   [8]
CO-1;
SO-1;
BL-2   Answer:
Meaning of Color Models
A color model is a mathematical and systematic way to represent colors as tuples of
numerical values.
Each color model defines a color space, where every color can be represented using specific
parameters such as Red, Green, and Blue (RGB) or Hue, Saturation, and Intensity (HSI).
These models are essential because digital systems (cameras, monitors, printers) store and
process color as numbers — not as visual hues.
Common Colour Models in Image Processing
Color Model   Components Description / Use
RGB   (Red,   Green, (R, G, B)   Additive color model where colors are formed
Blue)   by combining red, green, and blue light. Used
in display devices like monitors and cameras.
CMY / CMYK (Cyan, (C, M, Y, Subtractive model used in printing; colors are
Magenta,   Yellow, [K])   obtained by absorbing (subtracting) light.
[Black])
********** 16 **********
--- page 17 ---
HSI   / HSV (Hue, (H, S, I)   Separates   color information (Hue and
Saturation,   Saturation) from   brightness   (Intensity).
Intensity/Value)   Useful for image segmentation and color
enhancement.
YUV / YCbCr   (Y, U, V) or Separates luminance (Y) and chrominance
(Y, Cb, Cr)   (Cb, Cr). Used in video compression
standards (e.g., JPEG, MPEG).
Importance of colour models:
• Represent colors numerically for processing
• Allow manipulation, enhancement, compression
Colour models, Description, Application, Importance – 2 marks each
Q7   a   Explain 2D-Log Search motion estimation algorithms. Discuss its advantages and [10]
disadvantages.
CO-5;
SO-1;   Answer:
BL-2   2D-Log Search motion estimation algorithms – 6marks
Advantages and disadvantages – 4marks
Q7   b   Explain Digital negative and thresholding related to point processing techniques of image [10]
processing. Perform intensity level slicing with preserving background on the given 3-bit
CO-2;   image. Let r1 = 3 & r2 = 5. Draw the modified image using with background
SO-1;   transformation.
BL-3
2   1   2   2   1
2   3   4   5   2
6   2   7   6   0
2   6   6   5   1
0   3   2   2   1
Answer:
Digital negative and thresholding explanation 5marks
Gray level slicing with background;   5marks
s = r for, r < r1   Range: [0,1,2]
s = 7 for, r1 ≤ r ≤ r2 Range: [3,4,5]
s = r for, r > r2 Range: [6,7]
********** 17 **********
--- page 18 ---
Therefore, the modified output image is;

FR ICR 7] QA HH
````

## 2025-26 · Re-Exam · Sem 9 · Answer key · paper d2008210df98

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_09/Re-Exam/Integrated_Computer_7032/Image and Video Processing/ANS_Image and Video Processing(702EX0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: mixed (18 pages), mean OCR confidence 67.0

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Image and Video Processing
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Compute D4, D8 and De distances between pixel “p” and “q” for V = {2,3,4}   [4]
SO-1;
BL-2   3   2   1   3   1
4   2   3(q)   6   2
5   3   2   3   5
2(p)   4   3   4   6
4   5   2   3   3
Answer:
Co-ordinates for (p x, y, q s, t) are p (3, 0) and q (1, 2).
D4 (p, q) = |(𝑥−𝑠)| + |𝑦−𝑡| = 2+2 = 4   (1 mark)
𝐷8 = max(2, 2) = 2 (1 mark)
𝐷𝑒= √22 + 22 = √8 ≈2.828 (2 marks)
CO-2;   b.   Differentiate between Point Processing and Neighborhood Processing techniques in image   [4]
SO-1;   processing.
BL-3
********** 1 **********
--- page 2 ---
Answer:
Point Processing   Neighborhood Processing
Output pixel depends only on the   Output pixel depends on the intensity
intensity of the same input pixel   values of neighboring pixels
Image negative, Contrast stretching,
Filtering, Smoothing, Edge detection
Thresholding
Complex, requires kernel/mask
Simple, faster (pixel-wise operations)
operations
Local region around the pixel is
Local to a single pixel
considered
1 mark for each difference
CO-3;   c.   State morphological dilation. Perform morphological dilation on the following image for   [4]
SO-1;   object ‘A’ using the structuring element ‘B’. Circle indicates origin
BL-4
A =
0   0   0   0
0   1   1   0
0   0   1   0
0   0   0   0
B =
1
1
Answer
Output image, 𝐴⨁𝐵:
0   1   1   0
0   1   1   0
0   0   1   0
0   0   0   0
********** 2 **********
--- page 3 ---
Dilation definition: 2 Marks
Output Image: 2 Marks
CO-4;   d. What is image segmentation? Consider the following 5 × 5 grayscale image:   [4]
SO-1;
BL-4   200   50   10   101   99
105   250   255   103   56
200   102   55   204   210
110   98   99   77   65
199   204   97   101   99
Perform image segmentation using global thresholding with threshold 𝑇= 100. Write the
segmented binary image.
Answer:
Image segmentation definition: 1 mark
Image segmentation using Thresholding rule: 1 mark
Segmented binary image: 2 marks
1   0   0   1   0
1   1   1   1   0
1   1   0   1   1
1   0   0   0   0
1   1   0   1   0
CO-5;   e. Define digital video. List and explain any two key parameters that determine video quality.   [4]
SO-1;
BL-2   Hint:
Frame rate, resolution, colour depth — higher values improve quality but increase data rate.
Definition – 1mark
Any two key parameters – 3marks
Q2   a   Compute the gray level distribution using histogram equalization of the following image [10]
matrix having 8 gray levels (0–7). Also draw the original and equalized histogram.
CO-2;
SO-1;
BL-3
********** 3 **********
--- page 4 ---
2   5   3   5   2
1   1   2   1   1
5   2   5   5   2
2   1   1   1   1
3   2   5   5   2
Answer:
.
1) Histogram equalization steps (6 marks)
2) I/P and O/P histograms (4 marks).
rₖ   nₖ   p(rₖ) (PDF)   P(rₖ) (CDF)   SK = 7×P(rk)   Rounded SK
(exact)
0   0   0.000   0.000   0.00   0
1   8   0.320   0.320   2.24   2
2   8   0.320   0.640   4.48   4
3   2   0.080   0.720   5.04   5
4   0   0.000   0.720   5.04   5
5   7   0.280   1.000   7.00   7
6   0   0.000   1.000   7.00   7
7   0   0.000   1.000   7.00   7
New Gray levels New no. of pixels
0   0
2   8
4   8
5   2
7   7
********** 4 **********
--- page 5 ---
Q2   b   Convert an RGB pixel (R = 100, G = 150, B = 200) into CMY color model Also write at   [10]
least three applications of CMY model.
CO-2;
SO-1;
BL-3   Answer:
The CMY color model is a subtractive color model used in color printing. It represents
colors using Cyan (C), Magenta (M), and Yellow (Y) components. CMY is derived from
the RGB model, which is additive.
The relationship between the two models is:
𝐶= 1 −(𝑅/255)
𝑀= 1 −(𝐺/255)
𝑌= 1 −(𝐵/255)
Formula (3 Marks)
Calculation (3 Marks)
Component Formula Calculation   Result
C   −𝑅   −100   0.6078
1   1   = 1 −0.3922
255   255
M   −𝐺   −150   0.4118
1   1   = 1 −0.5882
255   255
Y   −𝐵   −200   0.2157
1   1   = 1 −0.7843
255   255
Final CMY Values (1 Mark)
(𝐶, 𝑀, 𝑌) = (0.6078,0.4118,0.2157)
Applications of CMY Color Model (3 Marks)
• Used in color printing and photographic reproduction.
• Used in scanners, copiers, and inkjet printers.
•   Suitable for subtractive mixing, where white light is reflected from paper.
********** 5 **********
--- page 6 ---
Q3   a   Find a 2-dimensional Discrete Fourier Transform (DFT) of the following image ‘f’   [4]
using the twiddle matrix.
CO-2;
SO-1;   𝑓= [1 2
BL-3   1 5]
Answer:
𝐹(𝑢, 𝑣) = 𝑊 . 𝑓(𝑥, 𝑦) . 𝑊𝑇
𝐹(𝑢, 𝑣) = [1 1   . [1 2   . [1 1
1 −1]   1 5]   1 −1]
𝐹(𝑢, 𝑣) = [2 7   . [1 1 = [ 9 −5 ]
0 −3]   1 −1]   −3 3
Q3   b   Apply the Horizontal and Vertical Prewitt operators to detect edges on the following image,   [8]
then compute the gradient magnitude, using pixel replication at borders.
CO-3;
SO-1;   100   100   20   20
BL-4
100   100   20   20
100   100   20   20
100   100   20   20
Answer:
********** 6 **********

[Text in pictures on this page, read by OCR]
Prewitt kernels:
-1 01 1 1 1
G,-—|-1 0 1 Gy -—|0 0 0
-1 01 -1 -1 -1
--- page 7 ---
Prewitt kernels – 1 mark
Gx Matrix - 2marks
Gy Matrix - 2marks
Formula of M - 1marks
Output Matrix - 2marks
Q3   c What is morphological closing? Perform morphological closing on the following 9x9   [8]
image for object ‘A’ using the structuring element ‘B’.
CO-3;
SO-1;   0   0   0   0   0   0   0   0   0
BL-4   0   0   0   0   0   0   0   0   0
0   0   0   1   1   1   0   0   0
0   0   1   1   0   1   1   0   0
0   0   1   0   0   0   1   0   0
0   0   1   1   0   1   1   0   0
0   0   0   1   1   1   0   0   0
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
Image, 1-valued elements indicate ‘A’
********** 7 **********

[Text in pictures on this page, read by OCR]
Horizontal derivative G_:

0 —240 —240
0 —240 —240
0 —240 —240
0 —240 —240

Vertical derivative Gy:

Gradient magnitude M = ,/G? + G3 = |G;':

0 240 240
0 240 240
0 240 240
0 240 240

M=
--- page 8 ---
1   1   1
1   1   1
1   0   1
Structuring element ‘B’, Center position is origin
Answer:
Morphological closing definition: 2 marks
Image after dilation: 3 marks
After erosion (Final Image): 3 marks
********** 8 **********

[Text in pictures on this page, read by OCR]
After Dilation (A ©® B):

(2) 12)
1 12)
1 1
1 1
1 1
1 1
1 1
1 12)
(2) 12)
OB):
(2) (2)
(2) 12)
(2) 12)
1 12)
1 @
1 (2)
(2) 12)
12) 12)
2) 12)
--- page 9 ---
Q4   a   Consider the given input image given below. Sketch and apply 3x3 Laplacian filter having [4]
positive centre without diagonal elements to get the response on the shaded (underlined)
CO-2;   central 3 x 3 pixels of the input image.
SO-1;
BL-3
10 10 10 10 10
10 10 10 10 10
50 50 50 50   50
50 50 50 50 50
50 50 50 50 50
Answer: 3 x3 Laplacian filter having positive centre without diagonal elements: (1 mark)
0   -1   0
-1   4   -1
0   -1   0
Convolution and output: (3 marks)
Final o/p image =
10   10   10   10   10
10   − 40 − 40 − 40   10
50   40   40   40   50
50   0   0   0   50
50   50   50   50   50
Q4   b. Find the 2-dimensional Discrete Cosine Transform (DCT) of the following image ‘f’.   [8]
CO-2;   2 4 4 2
SO-1;   4 6 8 3
𝑓= [   ]
BL-3   2 8 10 4
3 8 6 2
********** 9 **********
--- page 10 ---
Answer:
DCT matrix (2 marks)
𝐹= 𝐶. 𝑓. 𝐶𝑇   (1 mark)
5.5   13   14   5.5
𝐶. 𝑓= [ −0.112 −3.153 −1.847 −0.2705 ]   (2 marks)
−0.5   −1   −4   −1.5
−1.5765   0.224   0.765   0.653
19   −0.2705   −8   0.653
𝐹= 𝐶. 𝑓. 𝐶𝑇= [ −2.691 −0.2498   2.309   0.8957 ]   (3marks)
−3.5   1.4645   1.5   −1.6885
0.0327 −1.6022 −0.956 −0.2498
Q4   c   Discuss the classification of video frames based on their encoding techniques. Explain how   [8]
intra-frame and inter-frame coding differ in reducing redundancy.
CO-5;
SO-1;
BL-2   Answer:
Classification of video frames – 6 marks
In video compression (e.g., MPEG, H.264), frames are classified based on how they are
encoded:
1. I-Frame (Intra-coded Frame):
o Encoded independently without reference to other frames.
o Acts like a still image (JPEG).
o Provides random access points for decoding.
o Large in size but high in quality.
2. P-Frame (Predicted Frame):
o Encoded using motion-compensated prediction from a previous I or P frame.
o Stores only changes (differences) from reference frame.
o Smaller size than I-frames.
3. B-Frame (Bi-directional Predicted Frame):
o Uses data from both previous and future I or P frames for prediction.
o Achieves highest compression efficiency.
o Requires more computation and not used for random access.
Differences: 2marks
Intra = independent → higher quality, more bits.
Intra-frame coding reduces spatial redundancy within a frame.
Inter = dependent → higher compression, less data.
Inter-frame coding reduces temporal redundancy across frames, leading to more
efficient video compression.
********** 10 **********
--- page 11 ---
Q5   a   Using the Sobel operator, compute the gradient direction at the center pixel of the following   [4]
3×3 image.
CO-3;
SO-1;   10 20 30
BL-4
5   15 25
0   10 20
Answer:
Mask – 2 marks
Gx, Gy - 1 mark
Direction - 1 mark
Q5   b   Using Otsu’s method, find the optimal threshold that separates the image into two classes. [8]
Compute the between-class variance (𝜎𝐵 2) for thresholds T = 2 and 3 only.
CO-4;
SO-1;
BL-4
********** 11 **********

[Text in pictures on this page, read by OCR]
Gz = (—1)(10) + (0)(20) + (1)(80) + (—2)(5) + (0)(15) + (2)(25) + (—1)(0) + (0)(20) + (1)(20)
G, = (—10+0+30-10+0+4+50+0+0+ 20) = 80

Gy = (1)(10) + (2)(20) + (1)(80) + (0)(5) + (0)(15) + (0)(25) + (-1)(0) + (—2)(10) + (—1)(20)
G, = (10 + 40 + 30 +0 +0+0~-0- 20-20) = 40

Gz =80, Gy=40

Gradient Direction:

G 40
6=tan? (2) = tan! ) = tan7!(0.5) = 26.56°

r
--- page 12 ---
5   7   1   2   1
6   2   4   1   2
4   0   5   6   0
3   5   2   1   1
2   7   5   3   3
Answer:
T   w₀   w₁   μ₀   μ₁   σB²
2   0.48   0.52   1.2500   4.8462   3.22791
3   0.60   0.40   1.6000   5.4000   3.46560
For T=2
Background and foreground mean calculations (1 marks)
P1 calculation (1 marks)
Between class variance (1mark)
For T=3
Background and foreground mean calculations (1 marks)
P1 calculation (1 marks)
Between class variance (1 mark)
Optimum threshold at which σB² is maximum is T = 3 (2 marks)
Q5   c   Perform the Hit-or-Miss Transform on the following 10x10 binary image A to detect the   [8]
pattern represented by the structuring element B.
CO-3;
SO-1;
BL-4
********** 12 **********
--- page 13 ---
Answer:
Formula — HMT (A, B) = (A@B1)N(ASOBz2) (1mark)

Erosion A © B, (2marks)

68@@e@88860 6 6
8eeoee8 88 B

A‘ (1 mark)

FIR ICR 7] QI HO
--- page 14 ---
Erosion A° © Bz (2 marks)

Output (2marks)

FRR IC 7 I OH
--- page 15 ---
Q6   a   Compare JPEG and TIFF image file formats.   [4]
CO-1;
SO-1;   Answer
BL-2
Any 4 comparison points for 4 marks:
Feature   JPEG (Joint Photographic   TIFF (Tagged Image File Format)
Experts Group)
1. Compression   Uses lossy compression —   Supports lossless or lossy
Type   some image quality is lost to   compression — retains full image
reduce file size.   quality if lossless is used.
2. File Size   Smaller file size due to   Larger file size because of high-
compression.   quality, detailed data storage.
3. Image   Slight loss of detail; suitable   High-quality images suitable for
Quality   for photographs and web use.   printing, editing, and archiving.
4. Layers and   Does not support layers or   Supports layers, multiple pages,
Transparency   transparency.   and transparency.
5. Common   Web images, digital cameras, Scanning, printing, professional
Uses   social media.   photography, and image editing.
6. File   .jpg or .jpeg   .tif or .tiff
Extension
Q6   b What is Region-Based image segmentation? Consider the following 5×5 image where the [8]
gray-level intensity values are given. Use the Region Growing technique starting from the
CO-4;   seed pixel (marked in bold and underlined) with a threshold T=2. Use 4-connectivity. Identify
SO-1;   the final grown region.
BL-4
5   4   5   6   8
5   6   7   7   9
4   5   6   7   8
2   4   5   6   7
1   3   4   5   6
Answer:
Region-Based Image segmentation definition - 2 marks
Region growing: Conditions and steps - 4marks
Final Output: 2 marks
********** 15 **********
--- page 16 ---
Region-Based Segmentation divides an image into regions that are homogeneous according
to predefined criteria such as intensity, color, or texture.
Given:
Seed pixel = (3,3) → Intensity = 6
Threshold 𝑇= 2
Neighboring criterion: |I(neighbor) – seed point| ≤ 2
Connectivity: 4-connected
All pixels with values 4, 5, 6, 7, and 8 form the segmented region.
Output:
1 1 1 1 1
1 1 1 1 0
1 1 1 1 1
0 1 1 1 1
0 0 1 1 1
Q6   c   Explain different color models and their importance in image processing.   [8]
CO-1;
SO-1;
BL-2   Answer:
Meaning of Color Models
A color model is a mathematical and systematic way to represent colors as tuples of
numerical values.
Each color model defines a color space, where every color can be represented using specific
parameters such as Red, Green, and Blue (RGB) or Hue, Saturation, and Intensity (HSI).
These models are essential because digital systems (cameras, monitors, printers) store and
process color as numbers — not as visual hues.
Common Colour Models in Image Processing
Color Model   Components Description / Use
RGB   (Red,   Green, (R, G, B)   Additive color model where colors are formed
Blue)   by combining red, green, and blue light. Used
in display devices like monitors and cameras.
CMY / CMYK (Cyan, (C, M, Y, Subtractive model used in printing; colors are
Magenta,   Yellow, [K])   obtained by absorbing (subtracting) light.
[Black])
********** 16 **********
--- page 17 ---
HSI   / HSV (Hue, (H, S, I)   Separates   color information (Hue and
Saturation,   Saturation) from   brightness   (Intensity).
Intensity/Value)   Useful for image segmentation and color
enhancement.
YUV / YCbCr   (Y, U, V) or Separates luminance (Y) and chrominance
(Y, Cb, Cr)   (Cb, Cr). Used in video compression
standards (e.g., JPEG, MPEG).
Importance of colour models:
• Represent colors numerically for processing
• Allow manipulation, enhancement, compression
Colour models, Description, Application, Importance – 2 marks each
Q7   a   Explain 2D-Log Search motion estimation algorithms. Discuss its advantages and [10]
disadvantages.
CO-5;
SO-1;   Answer:
BL-2   2D-Log Search motion estimation algorithms – 6marks
Advantages and disadvantages – 4marks
Q7   b   Explain Digital negative and thresholding related to point processing techniques of image [10]
processing. Perform intensity level slicing with preserving background on the given 3-bit
CO-2;   image. Let r1 = 3 & r2 = 5. Draw the modified image using with background
SO-1;   transformation.
BL-3
2   1   2   2   1
2   3   4   5   2
6   2   7   6   0
2   6   6   5   1
0   3   2   2   1
Answer:
Digital negative and thresholding explanation 5marks
Gray level slicing with background;   5marks
s = r for, r < r1   Range: [0,1,2]
s = 7 for, r1 ≤ r ≤ r2 Range: [3,4,5]
s = r for, r > r2 Range: [6,7]
********** 17 **********
--- page 18 ---
Therefore, the modified output image is;

FR ICR 7] QA HH
````
