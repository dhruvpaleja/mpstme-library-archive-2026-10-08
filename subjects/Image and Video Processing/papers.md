# Image and Video Processing: question papers in full

39 unique papers · 2017-18 to 2025-26 · Computer Engineering, Electronics and Telecommunication, Computer Science, Data Science

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 5 · paper 79e565eaa0b6

- Departments: Computer Engineering, Computer Science
- Programmes: BTech Computer 7002, BTech CS 7055, Integrated Computer 7032, MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CS_7055/Image and Video Processing/QP_Image and Video Processing(702EX0E004)_2025-2026.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: text (6 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester IX/Semester V(Exam Year: 2025-2026)
Subject: Image and Video Processing
Date: 08 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO-1;   a. Compare JPEG and PNG image file formats with respect to features and usage:   [4]
SO-1;
BL-2
CO-2;   b. Consider the following 3 × 3 grayscale image region:   [4]
SO-1;
BL-3   10 20 30
𝐼= 40 50 60
70 80 90
Using a Laplacian filter having positive centre without diagonal elements for sharpening,
compute the output value at the center pixel (50).
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
********** 1 **********
--- page 2 ---
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
CO-5;   e.   Differentiate between spatial redundancy and temporal redundancy in video data.   [4]
SO-1;
BL-2
Q2   a An image has the following gray levels and corresponding number of pixels:   [10]
CO-2;
SO-1;
Gray level rₖ   0   1 2 3   4   5   6 7
BL-3
No. of pixels nₖ   2   3 5 8 10 20 8 4
Compute the gray level distribution using histogram equalization. Also plot the
histogram of the input and output (equalized) images.
Q2   b   Convert a RGB color model with R=100, G=200, B=50 to HSI color model.   [10]
CO-2;
SO-1;
BL-3
Q3   a   Find 2-D Hadamard Transform of the following image ‘f’   [4]
CO-2;   𝑓= [2 6
SO-1;   3 5]
BL-3
********** 2 **********
--- page 3 ---
Q3   b   Apply the Horizontal and Vertical Sobel operators on the image, then compute the   [8]
gradient magnitude, using pixel replication at borders.
CO-3;
SO-1;   10   10   10   10
BL-4
10   10   10   10
100   100   100   100
100   100   100   100
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
Structuring element ‘B’,
Center position is origin
Q4   a   Apply median filter of size 3 x 3 on the circled pixels of the input image give below.   [4]
CO-2;   147   163   169   122   51
SO-1;
152   168   148   255   48
BL-3
176   167   97   44   57
185   121   45   50   63
132   55   43   61   67
Q4   b. Find a 2-dimensional Discrete Cosine Transform (DCT) of the following image ‘f’ using   [8]
the transform matrix.
********** 3 **********
--- page 4 ---
CO-2;
SO-1;
BL-3   1 2 2 1
2 2 1 1
𝑓= [   ]
1 2 2 1
1 2 1 2
Q4   c   Discuss the Three-Step Search (TSS) algorithm for motion estimation. Explain how it   [8]
balances accuracy and computational efficiency in video compression.
CO-5;
SO-1;
BL-2
Q5   a   For the given image below:   [4]
CO-3;
SO-1;   2   4   6
BL-4
1   5   7
3   9   8
Compute Gradient Direction for the center pixel using Prewitt operator.
Q5   b An image has 4 gray levels: 0, 1, 2, 3. The number of pixels corresponding to each gray [8]
level is as follows:
CO-4;
SO-1;
BL-4   Gray level (r)   0   1   2   3
No. of pixels (n)   4   5   3   2
Find optimal threshold using Otsu for threshold values 1 and 2 only.
Q5   c   Perform boundary extraction on the following binary image A using the structuring [8]
element SE shown below.
CO-3;
SO-1;
BL-4   SE =
1
1   1   1
1
********** 4 **********
--- page 5 ---
A=
0   1   2   3   4   5   6
0   0   0   0   0   0   0   0
1   0   1   1   1   1   0   0
2   0   1   1   1   1   1   0
3   0   1   1   1   1   1   0
4   0   1   1   1   1   1   0
5   0   1   1   1   1   0   0
6   0   0   0   0   0   0   0
Q6   a An image segment is shown below. Let, V be the set of Gray-level values used to define [4]
connectivity in the image.
CO-1;
Compute: De, D4, D8 and Dm distances between pixels ‘p’ and ‘q’ for: V = {1,2}.
SO-1;
BL-2   0   1   2(q)
2   3   2
1(p) 1   3
Q6   b   Perform region splitting and merging on the following image with threshold value T <=   [8]
10.
CO-4;
SO-1;   80   85   78   82
BL-4   83   82   79   84
200   195   198   202
199   201   197   196
Q6   c   Describe the YUV color model and its significance in video processing.   [8]
CO-1;
SO-1;
BL-2
Q7   a   Explain Exhaustive Search Block Matching Algorithm in video processing. Discuss its   [10]
advantages and disadvantages.
CO-5;
SO-1;
BL-2
********** 5 **********
--- page 6 ---
Q7   b What is difference between Power-Law Transformation and Contrast Stretching? Apply   [10]
the Power-Law (Gamma) Transformation on the following image with C=1.2, and 𝛾 =
CO-2;   0.6 and obtain the final output image matrix.
SO-1;
BL-3   f(x, y) =
0   20   40
60   80   100
110   120   127
********** 6 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper be33ccfb8546

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7011/Image and Video Processing/QP_Image and Video Processing(702EX0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (2 pages)

````text
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
1. This question paper contains 2 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is Compulsory.
5. Attempt any 4 from remaining questions.
6. Assume Suitbale data wherever necessary.
7. Draw clear diagram and write justification if required.
1A   What is a Digital Image? Discuss following for any image example.   [04]
[CO1, BL2]   i. Intensity Range   ii. Resolution
1B   Take an example and discuss the application of any two-point   [04]
[CO2, BL3]   processing approaches of image enhancement.
1C   “Morphological operation and edge detector can be useful to   [04]
[CO3, BL4]   extract the boundary of any object” justify this statement using
an image example and relevant operations.
1D   Compare region growing and Region merging approaches of   [04]
[CO4, BL4]   image segmentation.
1E   Explain temporal correlation in video processing.   [04]
[CO5, BL2]
2 A   Explain following in detail: i. Relationship among pixels   [10]
[CO1, BL2]   ii. Importance of grey level and frequency resolution
2 B   Explain attest 5 real life applications of image and video   [10]
[CO1, BL2]   processing.
3 A   “Any digital image content can be analyzed for presence of   [10]
[CO2, BL3]   various patterns in it by using the Hadamard transforms” Take an
example and justify.
3 B   Discuss the difference in impact observed on resultant image   [10]
[[CO2, BL3]   after applying following operations: 1. Gray level slicing with
background. 2. Thresholding
********** 1 **********
--- page 2 ---
4 A   [10]
[CO3, BL4]   Analyze and discuss the impact of following line detectors on any
digital image. i. Horizontal ii. Vertical iii. diagonal iv Reverse
Diagonal.
4 B   [10]
[CO3, BL4]   Analyze and explain the effect of Opening and closing on a digital
image having dark circular object with white background.
[10]
5 A   Compare the step by step working of Otsu segmentation
[CO4, BL4]   approach with region splitting segmentation.
5 B   “Bad illumination affects the quality of segmentation using   [10]
[CO4, BL4]   thresholding” justify this statement with step by step working of
the process applied on suitable digital image.
6 A   How digital video data is represented? Explain the importance of   [10]
[CO5, BL2]   I, P and B frames in video compression. Explain with example.
6 B
[CO5, BL2]   Discuss:
1. Block matching
2. Exhaustive search
7 A   [10]
[CO3, BL4]   Analyze the impact of following structuring elements: Diamond
and line on any suitable digital image.
7 B   [10]
[CO3, BL4]   Analyze the impact of Sobel and Prewitt operators on a digital
image.
****************
********** 2 **********
````

## 2025-26 · Final-Exam · Sem 5 · paper df441605d233

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, B.TECH INTEGRATED / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/IMAGE & VIDEO PROCESSING/Image and Video Processing 2025-26 Final.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 Dec 2025
- Text: ocr (6 pages), mean OCR confidence 85.7

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (
Year: III / V/Semester [X/Semester V(Exam Year: 2025-2026)

Subject: Image and Video Processing .
Date: 08 Dec 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100

FINAL EXAMINATION (Acad. Year:2025-2026)

Instructions:

This question paper contains 6 pages.,

2. Answer to each new question to be started on a fresh page. ~
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
a
Ql Answer briefly: [20]
CO-1; | a. | Compare JPEG and PNG image file formats with respect to features and usage: [4]
SO-1;
BL-2
CO-2; | b. | Consider the following 3 x 3 grayscale image region: [4]
SO-1;
BL-3 10 20 30
1=40 50 60
70 80 90
Using a Laplacian filter having positive centre without diagonal elements for sharpening,
compute the output value at the center pixel (50).
CO-3; | c. | State morphological erosion. Perform morphological erosion on the following image for | [4]
SO-1; object ‘A’ using the structuring element ‘B’. Circle indicates origin
“| BL-4
j A=
0 1 0 0
0 1 1 0
0 1 1 0
0 1 0 0
\ TN
4 . Ww t
1 1

RRR 7 RR
--- page 2 ---
CO-4; | d. | What is adjacency in image processing? [4]
SO-1;

BL-4 Consider the following 5 x 5 binary image. The origin is at top-left and coordinates are
written as (row,column) with 1-based indexing. Foreground pixels have value 1) (set V =
{1}). < »
110041
1.1010
T=0 00 0 0
01000
. 0010 0

Draw dashed lines showing connections between pixels of the same label under:

1. 8-adjacency
2. m-adjacency

CO-5; | e. | Differentiate between spatial redundancy and temporal redundancy in video data. [4]
SO-1;
BL-2

Q2 a | An image has the following gray levels and corresponding number of pixels: [10]

CO-2;

ate Graylevelrn, | 0 [1/2/31 4] 5 [6] 7

No. of pixelsn, | 2 |-3 | 5]8] 10} 20/84

Compute the gray level distribution using histogram equalization. Also plot the
histogram of the input and output (equalized) images.

Q2 b_ | Convert a RGB color model with R=100, G=200, B=50 to HSI color model. [10]
CO-2;

SO-1;

BL-3

Q3 a | Find 2-D Hadamard Transform of the following image ‘f [4]
CO-2; _[2 6

SO-1; f [; 5

BL-3

RRR RRR RRR DORR RR RE
--- page 3 ---
ee STRESS eS Oe oe

Q3 b_ | Apply the Horizontal and Vertical Sobel operators on the image, then compute the [8]
gradient magnitude, using pixel replication at borders.

CO-3;
SO-1; 10 10 10-] 10 | .
BL-4 ©
10 10 10 10
100 100 100 100
100 100 100 100
Q3 c¢ | What is morphological opening? Perform morphological opening on the following image [8]
A (size 9x9) using the structuring element ‘B’.
CO-3;
SO-1;
BL-4

Image A
1/0} 1
1} 1]
1/0] 1
Structuring element ‘B’,
a Center position is origin
Q4 a | Apply median filter of size 3x 3 on the circled pixels of the input image give below. [4]
CO-2: [ 147 | 163 [ 169 [122 7 si |
SO-1;
BL-3 152 168 148 255 48
176 | 167 | (7) | 44 57
185 121 45 50 63
4 132 55 | 43 61 67
Q4 b. | Find a 2-dimensional Discrete Cosine Transform (DCT) of the following image ‘f? using | [8]
iZ the transform matrix. |

FORE tok ae
.
--- page 4 ---
CO-2;

SO-1;
BL-3 12 2 1
{2 2 1 «41
f= 122 1 << »
12 1 2 “a
Q4 c | Discuss the Three-Step Search (TSS) algorithm for motion estimation. Explain how it | [8]
balances accuracy and computational efficiency in video compression. *
CO-5; 7
SO-1; 7
BL-2
Q5 a_| For the given image below: [4]
CO-3;
SO-1; 2 |4 |6
BL-4
1 5 7
3 19° 18
Compute Gradient Direction for the center pixel using Prewitt operator.
Q5 b | An image has 4 gray levels: 0, 1, 2, 3. The number of pixels corresponding to each gray | [8]
level is as follows:
CO-4;
SO-1;
BL4 Gray level (r) 0)]1)/2)3
No. of pixels (n) 4 5 3 2
Find optimal threshold using Otsu for threshold values 1 and 2 only.
Q5 c | Perform boundary extraction on the following binary image A using the structuring | [8]
element SE shown below.
CO-3;
SO-1;
BL-4 SE=
1
1 1 1
‘ | 1

FR IGRI RR Ak
--- page 5 ---
Le ee

A=
0 1 2 3 4 5 6
0 0 0 0 0 0 0 0
1 [0] 4 i i i—ofo|*
2 0 1 1 1 1 1 0
3 0 1 1 1 1 1 0
4 0 1 1 1 1 1 0 .
5) 0 1 1 1 1 0 0
6 0 0 0 0 0 0 0
Q6 An image segment is shown below. Let, V be the set of Gray-level values used to define | [4]
connectivity in the image. ;
_ : Compute: De, D4, Dg and Dm distances between pixels ‘p’ and ‘q? for: V = {1,2}.
BL-2 0 1 }2(q)
2 3 | 2
l(p)} 1 3
Q6 Perform region splitting and merging on the following image with threshold value T <= | [8]
10.
CO-4;
SO-1; 80 85 78 82
Bet 83 | 82 | 79 | 84
200 195 198 202
199 201 197 196
Q6 Describe the YUV color model and its significance in video processing. [8]
CO-1;,
SO-1;
BL-2
Q7 Explain Exhaustive Search Block Matching Algorithm in video processing. Discuss its [10]
advantages and disadvantages.
CO-5;
SO-1;
BL-2

FRR OAR RR RR
--- page 6 ---
~

Q7 b_ | What is difference between Power-Law Transformation and Contrast Stretching? Apply | [10]
the Power-Law (Gamma) Transformation on the following image with C=1.2, and y =

CO-2; 0.6 and obtain the final output image matrix.
SO-1;
BL-3 f(x, y) = .
0 20 | 40
60 80 | 100
110 | 120 | 127 ~

FOGG 6 AK

4 .
````

## 2025-26 · Re-Exam · Sem 5 · paper 46abde71cafa

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CS_7055/Image and Video Processing/QP_Image and Video Processing(702EX0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: text (6 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Image and Video Processing
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
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
CO-2;   b.   Differentiate between Point Processing and Neighborhood Processing techniques in image   [4]
SO-1;   processing.
BL-3
CO-3;   c.   State morphological dilation. Perform morphological dilation on the following image for   [4]
SO-1;   object ‘A’ using the structuring element ‘B’. Circle indicates origin.
BL-4
A =
0   0   0   0
0   1   1   0
0   0   1   0
0   0   0   0
********** 1 **********
--- page 2 ---
B =
1
1
CO-4;   d. What is image segmentation? Consider the following 5 × 5 grayscale image:   [4]
SO-1;
BL-4   200   50   10   101   99
105   250   255   103   56
200   102   55   204   210
110   98   99   77   65
199   204   97   101   99
Perform image segmentation using global thresholding with threshold 𝑇= 100. Write the
segmented binary image.
CO-5;   e. Define digital video. List and explain any two key parameters that determine video quality.   [4]
SO-1;
BL-2
Q2   a   Compute the gray level distribution using histogram equalization of the following image [10]
matrix having 8 gray levels (0–7). Also draw the original and equalized histogram.
CO-2;
SO-1;
BL-3
2   5   3   5   2
1   1   2   1   1
5   2   5   5   2
2   1   1   1   1
3   2   5   5   2
Q2   b   Convert an RGB pixel (R = 100, G = 150, B = 200) into CMY color model Also write at   [10]
least three applications of CMY model.
CO-2;
SO-1;
BL-3
********** 2 **********
--- page 3 ---
Q3   a   Find a 2-dimensional Discrete Fourier Transform (DFT) of the following image ‘f’   [4]
using the twiddle matrix.
CO-2;
SO-1;   𝑓= [1 2
BL-3   1 5]
Q3   b   Apply the Horizontal and Vertical Prewitt operators to detect edges on the following image,   [8]
then compute the gradient magnitude, using pixel replication at borders.
CO-3;
SO-1;   100   100   20   20
BL-4
100   100   20   20
100   100   20   20
100   100   20   20
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
1   1   1
1   1   1
1   0   1
Structuring element ‘B’, Center position is origin
********** 3 **********
--- page 4 ---
Q4   a   Consider the given input image given below. Sketch and apply 3x3 Laplacian filter having [4]
positive centre without diagonal elements to get the response on the shaded (underlined)
CO-2;   central 3 x 3 pixels of the input image.
SO-1;
BL-3
10   10   10   10   10
10   10   10   10   10
50   50   50   50   50
50   50   50   50   50
50   50   50   50   50
Q4   b. Find the 2-dimensional Discrete Cosine Transform (DCT) of the following image ‘f’.   [8]
CO-2;   2 4 4 2
SO-1;   4 6 8 3
𝑓= [   ]
BL-3   2 8 10 4
3 8 6 2
Q4   c   Discuss the classification of video frames based on their encoding techniques. Explain how   [8]
intra-frame and inter-frame coding differ in reducing redundancy.
CO-5;
SO-1;
BL-2
Q5   a   Using the Sobel operator, compute the gradient direction at the center pixel of the following   [4]
3×3 image.
CO-3;
SO-1;   10   20   30
BL-4
5   15   25
0   10   20
Q5   b   Using Otsu’s method, find the optimal threshold that separates the image into two classes.   [8]
Compute the between-class variance (𝜎𝐵 2) for thresholds T = 2 and 3 only.
CO-4;
SO-1;
BL-4   5   7   1   2   1
6   2   4   1   2
4   0   5   6   0
3   5   2   1   1
2   7   5   3   3
********** 4 **********
--- page 5 ---
Q5   c   Perform the Hit-or-Miss Transform on the following 10x10 binary image A to detect the   [8]
pattern represented by the structuring element B.
CO-3;
SO-1;
BL-4
Q6   a   Compare JPEG and TIFF image file formats.   [4]
CO-1;
SO-1;
BL-2
Q6   b What is Region-Based image segmentation? Consider the following 5×5 image where the [8]
gray-level intensity values are given. Use the Region Growing technique starting from the
CO-4;   seed pixel (marked in bold and underlined) with a threshold T=2. Use 4-connectivity. Identify
SO-1;   the final grown region.
BL-4   5   4   5   6   8
5   6   7   7   9
4   5   6   7   8
2   4   5   6   7
1   3   4   5   6
Q6   c   Explain different color models and their importance in image processing.   [8]
CO-1;
SO-1;
BL-2
********** 5 **********
--- page 6 ---
Q7   a   Explain 2D-Log Search motion estimation algorithms. Discuss its advantages and [10]
disadvantages.
CO-5;
SO-1;
BL-2
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
********** 6 **********
````

## 2025-26 · Re-Exam · Sem 5 · paper 858932341738

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_Computer_7002/Image and Video Processing/QP_Image and Video Processing(702EX0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: text (6 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Image and Video Processing
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
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
CO-2;   b.   Differentiate between Point Processing and Neighborhood Processing techniques in image   [4]
SO-1;   processing.
BL-3
CO-3;   c.   State morphological dilation. Perform morphological dilation on the following image for   [4]
SO-1;   object ‘A’ using the structuring element ‘B’. Circle indicates origin.
BL-4
A =
0   0   0   0
0   1   1   0
0   0   1   0
0   0   0   0
********** 1 **********
--- page 2 ---
B =
1
1
CO-4;   d. What is image segmentation? Consider the following 5 × 5 grayscale image:   [4]
SO-1;
BL-4   200   50   10   101   99
105   250   255   103   56
200   102   55   204   210
110   98   99   77   65
199   204   97   101   99
Perform image segmentation using global thresholding with threshold 𝑇= 100. Write the
segmented binary image.
CO-5;   e. Define digital video. List and explain any two key parameters that determine video quality.   [4]
SO-1;
BL-2
Q2   a   Compute the gray level distribution using histogram equalization of the following image [10]
matrix having 8 gray levels (0–7). Also draw the original and equalized histogram.
CO-2;
SO-1;
BL-3
2   5   3   5   2
1   1   2   1   1
5   2   5   5   2
2   1   1   1   1
3   2   5   5   2
Q2   b   Convert an RGB pixel (R = 100, G = 150, B = 200) into CMY color model Also write at   [10]
least three applications of CMY model.
CO-2;
SO-1;
BL-3
********** 2 **********
--- page 3 ---
Q3   a   Find a 2-dimensional Discrete Fourier Transform (DFT) of the following image ‘f’   [4]
using the twiddle matrix.
CO-2;
SO-1;   𝑓= [1 2
BL-3   1 5]
Q3   b   Apply the Horizontal and Vertical Prewitt operators to detect edges on the following image,   [8]
then compute the gradient magnitude, using pixel replication at borders.
CO-3;
SO-1;   100   100   20   20
BL-4
100   100   20   20
100   100   20   20
100   100   20   20
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
1   1   1
1   1   1
1   0   1
Structuring element ‘B’, Center position is origin
********** 3 **********
--- page 4 ---
Q4   a   Consider the given input image given below. Sketch and apply 3x3 Laplacian filter having [4]
positive centre without diagonal elements to get the response on the shaded (underlined)
CO-2;   central 3 x 3 pixels of the input image.
SO-1;
BL-3
10   10   10   10   10
10   10   10   10   10
50   50   50   50   50
50   50   50   50   50
50   50   50   50   50
Q4   b. Find the 2-dimensional Discrete Cosine Transform (DCT) of the following image ‘f’.   [8]
CO-2;   2 4 4 2
SO-1;   4 6 8 3
𝑓= [   ]
BL-3   2 8 10 4
3 8 6 2
Q4   c   Discuss the classification of video frames based on their encoding techniques. Explain how   [8]
intra-frame and inter-frame coding differ in reducing redundancy.
CO-5;
SO-1;
BL-2
Q5   a   Using the Sobel operator, compute the gradient direction at the center pixel of the following   [4]
3×3 image.
CO-3;
SO-1;   10   20   30
BL-4
5   15   25
0   10   20
Q5   b   Using Otsu’s method, find the optimal threshold that separates the image into two classes.   [8]
Compute the between-class variance (𝜎𝐵 2) for thresholds T = 2 and 3 only.
CO-4;
SO-1;
BL-4   5   7   1   2   1
6   2   4   1   2
4   0   5   6   0
3   5   2   1   1
2   7   5   3   3
********** 4 **********
--- page 5 ---
Q5   c   Perform the Hit-or-Miss Transform on the following 10x10 binary image A to detect the   [8]
pattern represented by the structuring element B.
CO-3;
SO-1;
BL-4
Q6   a   Compare JPEG and TIFF image file formats.   [4]
CO-1;
SO-1;
BL-2
Q6   b What is Region-Based image segmentation? Consider the following 5×5 image where the [8]
gray-level intensity values are given. Use the Region Growing technique starting from the
CO-4;   seed pixel (marked in bold and underlined) with a threshold T=2. Use 4-connectivity. Identify
SO-1;   the final grown region.
BL-4   5   4   5   6   8
5   6   7   7   9
4   5   6   7   8
2   4   5   6   7
1   3   4   5   6
Q6   c   Explain different color models and their importance in image processing.   [8]
CO-1;
SO-1;
BL-2
********** 5 **********
--- page 6 ---
Q7   a   Explain 2D-Log Search motion estimation algorithms. Discuss its advantages and [10]
disadvantages.
CO-5;
SO-1;
BL-2
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
********** 6 **********
````

## 2025-26 · Re-Exam · Sem 5 · paper bb8c1720bf9b

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_Computer_7047/Image and Video Processing/QP_Image and Video Processing(702EX0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: text (6 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Image and Video Processing
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
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
CO-2;   b.   Differentiate between Point Processing and Neighborhood Processing techniques in image   [4]
SO-1;   processing.
BL-3
CO-3;   c.   State morphological dilation. Perform morphological dilation on the following image for   [4]
SO-1;   object ‘A’ using the structuring element ‘B’. Circle indicates origin.
BL-4
A =
0   0   0   0
0   1   1   0
0   0   1   0
0   0   0   0
********** 1 **********
--- page 2 ---
B =
1
1
CO-4;   d. What is image segmentation? Consider the following 5 × 5 grayscale image:   [4]
SO-1;
BL-4   200   50   10   101   99
105   250   255   103   56
200   102   55   204   210
110   98   99   77   65
199   204   97   101   99
Perform image segmentation using global thresholding with threshold 𝑇= 100. Write the
segmented binary image.
CO-5;   e. Define digital video. List and explain any two key parameters that determine video quality.   [4]
SO-1;
BL-2
Q2   a   Compute the gray level distribution using histogram equalization of the following image [10]
matrix having 8 gray levels (0–7). Also draw the original and equalized histogram.
CO-2;
SO-1;
BL-3
2   5   3   5   2
1   1   2   1   1
5   2   5   5   2
2   1   1   1   1
3   2   5   5   2
Q2   b   Convert an RGB pixel (R = 100, G = 150, B = 200) into CMY color model Also write at   [10]
least three applications of CMY model.
CO-2;
SO-1;
BL-3
********** 2 **********
--- page 3 ---
Q3   a   Find a 2-dimensional Discrete Fourier Transform (DFT) of the following image ‘f’   [4]
using the twiddle matrix.
CO-2;
SO-1;   𝑓= [1 2
BL-3   1 5]
Q3   b   Apply the Horizontal and Vertical Prewitt operators to detect edges on the following image,   [8]
then compute the gradient magnitude, using pixel replication at borders.
CO-3;
SO-1;   100   100   20   20
BL-4
100   100   20   20
100   100   20   20
100   100   20   20
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
1   1   1
1   1   1
1   0   1
Structuring element ‘B’, Center position is origin
********** 3 **********
--- page 4 ---
Q4   a   Consider the given input image given below. Sketch and apply 3x3 Laplacian filter having [4]
positive centre without diagonal elements to get the response on the shaded (underlined)
CO-2;   central 3 x 3 pixels of the input image.
SO-1;
BL-3
10   10   10   10   10
10   10   10   10   10
50   50   50   50   50
50   50   50   50   50
50   50   50   50   50
Q4   b. Find the 2-dimensional Discrete Cosine Transform (DCT) of the following image ‘f’.   [8]
CO-2;   2 4 4 2
SO-1;   4 6 8 3
𝑓= [   ]
BL-3   2 8 10 4
3 8 6 2
Q4   c   Discuss the classification of video frames based on their encoding techniques. Explain how   [8]
intra-frame and inter-frame coding differ in reducing redundancy.
CO-5;
SO-1;
BL-2
Q5   a   Using the Sobel operator, compute the gradient direction at the center pixel of the following   [4]
3×3 image.
CO-3;
SO-1;   10   20   30
BL-4
5   15   25
0   10   20
Q5   b   Using Otsu’s method, find the optimal threshold that separates the image into two classes.   [8]
Compute the between-class variance (𝜎𝐵 2) for thresholds T = 2 and 3 only.
CO-4;
SO-1;
BL-4   5   7   1   2   1
6   2   4   1   2
4   0   5   6   0
3   5   2   1   1
2   7   5   3   3
********** 4 **********
--- page 5 ---
Q5   c   Perform the Hit-or-Miss Transform on the following 10x10 binary image A to detect the   [8]
pattern represented by the structuring element B.
CO-3;
SO-1;
BL-4
Q6   a   Compare JPEG and TIFF image file formats.   [4]
CO-1;
SO-1;
BL-2
Q6   b What is Region-Based image segmentation? Consider the following 5×5 image where the [8]
gray-level intensity values are given. Use the Region Growing technique starting from the
CO-4;   seed pixel (marked in bold and underlined) with a threshold T=2. Use 4-connectivity. Identify
SO-1;   the final grown region.
BL-4   5   4   5   6   8
5   6   7   7   9
4   5   6   7   8
2   4   5   6   7
1   3   4   5   6
Q6   c   Explain different color models and their importance in image processing.   [8]
CO-1;
SO-1;
BL-2
********** 5 **********
--- page 6 ---
Q7   a   Explain 2D-Log Search motion estimation algorithms. Discuss its advantages and [10]
disadvantages.
CO-5;
SO-1;
BL-2
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
********** 6 **********
````

## 2025-26 · Re-Exam · Sem 9 · paper fe64d45e68fb

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_09/Re-Exam/Integrated_Computer_7032/Image and Video Processing/QP_Image and Video Processing(702EX0E004)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Feb 2026
- Text: text (6 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Image and Video Processing
Date: 03 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
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
CO-2;   b.   Differentiate between Point Processing and Neighborhood Processing techniques in image   [4]
SO-1;   processing.
BL-3
CO-3;   c.   State morphological dilation. Perform morphological dilation on the following image for   [4]
SO-1;   object ‘A’ using the structuring element ‘B’. Circle indicates origin.
BL-4
A =
0   0   0   0
0   1   1   0
0   0   1   0
0   0   0   0
********** 1 **********
--- page 2 ---
B =
1
1
CO-4;   d. What is image segmentation? Consider the following 5 × 5 grayscale image:   [4]
SO-1;
BL-4   200   50   10   101   99
105   250   255   103   56
200   102   55   204   210
110   98   99   77   65
199   204   97   101   99
Perform image segmentation using global thresholding with threshold 𝑇= 100. Write the
segmented binary image.
CO-5;   e. Define digital video. List and explain any two key parameters that determine video quality.   [4]
SO-1;
BL-2
Q2   a   Compute the gray level distribution using histogram equalization of the following image [10]
matrix having 8 gray levels (0–7). Also draw the original and equalized histogram.
CO-2;
SO-1;
BL-3
2   5   3   5   2
1   1   2   1   1
5   2   5   5   2
2   1   1   1   1
3   2   5   5   2
Q2   b   Convert an RGB pixel (R = 100, G = 150, B = 200) into CMY color model Also write at   [10]
least three applications of CMY model.
CO-2;
SO-1;
BL-3
********** 2 **********
--- page 3 ---
Q3   a   Find a 2-dimensional Discrete Fourier Transform (DFT) of the following image ‘f’   [4]
using the twiddle matrix.
CO-2;
SO-1;   𝑓= [1 2
BL-3   1 5]
Q3   b   Apply the Horizontal and Vertical Prewitt operators to detect edges on the following image,   [8]
then compute the gradient magnitude, using pixel replication at borders.
CO-3;
SO-1;   100   100   20   20
BL-4
100   100   20   20
100   100   20   20
100   100   20   20
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
1   1   1
1   1   1
1   0   1
Structuring element ‘B’, Center position is origin
********** 3 **********
--- page 4 ---
Q4   a   Consider the given input image given below. Sketch and apply 3x3 Laplacian filter having [4]
positive centre without diagonal elements to get the response on the shaded (underlined)
CO-2;   central 3 x 3 pixels of the input image.
SO-1;
BL-3
10   10   10   10   10
10   10   10   10   10
50   50   50   50   50
50   50   50   50   50
50   50   50   50   50
Q4   b. Find the 2-dimensional Discrete Cosine Transform (DCT) of the following image ‘f’.   [8]
CO-2;   2 4 4 2
SO-1;   4 6 8 3
𝑓= [   ]
BL-3   2 8 10 4
3 8 6 2
Q4   c   Discuss the classification of video frames based on their encoding techniques. Explain how   [8]
intra-frame and inter-frame coding differ in reducing redundancy.
CO-5;
SO-1;
BL-2
Q5   a   Using the Sobel operator, compute the gradient direction at the center pixel of the following   [4]
3×3 image.
CO-3;
SO-1;   10   20   30
BL-4
5   15   25
0   10   20
Q5   b   Using Otsu’s method, find the optimal threshold that separates the image into two classes.   [8]
Compute the between-class variance (𝜎𝐵 2) for thresholds T = 2 and 3 only.
CO-4;
SO-1;
BL-4   5   7   1   2   1
6   2   4   1   2
4   0   5   6   0
3   5   2   1   1
2   7   5   3   3
********** 4 **********
--- page 5 ---
Q5   c   Perform the Hit-or-Miss Transform on the following 10x10 binary image A to detect the   [8]
pattern represented by the structuring element B.
CO-3;
SO-1;
BL-4
Q6   a   Compare JPEG and TIFF image file formats.   [4]
CO-1;
SO-1;
BL-2
Q6   b What is Region-Based image segmentation? Consider the following 5×5 image where the [8]
gray-level intensity values are given. Use the Region Growing technique starting from the
CO-4;   seed pixel (marked in bold and underlined) with a threshold T=2. Use 4-connectivity. Identify
SO-1;   the final grown region.
BL-4   5   4   5   6   8
5   6   7   7   9
4   5   6   7   8
2   4   5   6   7
1   3   4   5   6
Q6   c   Explain different color models and their importance in image processing.   [8]
CO-1;
SO-1;
BL-2
********** 5 **********
--- page 6 ---
Q7   a   Explain 2D-Log Search motion estimation algorithms. Discuss its advantages and [10]
disadvantages.
CO-5;
SO-1;
BL-2
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
********** 6 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper d072c8a58d4d

- Departments: Data Science
- Programmes: B TECH / CSE Data Science (311)
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSE Data Science (311)/SEM-VI/IMAGE & VIDEO PROCESSING/B Tech, Image and Video Processing, Sem-VI, Batch 2025-26, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Jul 2026
- Text: ocr (2 pages), mean OCR confidence 86.7

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AN

ENGINEERING (DATA SCIENCE) °
Year: II/Sem 6 Re-exam(Exam Year: 2025-2026) me
Subject: Image and Video Processing
Date: 06 Jul 2026 Time: 10:00 am to 01:00 pm (03:00 Hrs.)

Max. Marks: 100

RE EXAMINATION (Acad. Year:2025-2026)

Instructions:

1. This question paper contains 2 pages.

2. Answer to each new question to be started on a fresh page.

3. Figure in right hand side indicates full marks

4. Question No. | is Compulsory.

5. Attempt any 4 from remaining questions.

6. Assume Suitbale data wherever necessary.

7. Draw clear diagram and write justification if required.

»

Q1: Answer following questions
A [CO1] [BL-2] Describe the quality features of the given digital image: f(x,y) having 25 pixels and 8 [04]

BPP
B [CO2] [BL-3]   Equalize any darkest 8-bit digital image. , [04]
C [C03] [BL-4] “Erosion is different than Closing” prove this statement with working examples. [04]
D [CO4] [BL-4] “Presence of noise in the image affects the quality of segmentation using . [04]

discontinuity approach.” Justify this statement with an example.

E [CO5] [BL-2] Describe the differences between digital images and videos. [04]

Q2: Answer following questions

A[CO1] [BL-2] Take an example of a digital image and describe the importance of gray level , [10]
: resolution.
B [CO1] [BL-2] Explain the pixel relationships and its importance in the image. Explain all possible [10]

ways of exploring these relationships.

Q3: Answer following questions
A [CO2] [BL-3] “Low pass filter is not suitable for salt and paper noise removal” Justify this [10]

statement based on a working example.

B [CO2] [BL-3] Apply thresholding on a digital image and compare its result with the gray level [10]
slicing.

FR KR
--- page 2 ---
rr

Q4: Answer following questions *

A [CO3] [BL-4] Suggest sequence of morphological operations to extract the features of any.
signature image for developing the signature recognition system.

B [CO3] [BL-4] . Suggest sequence of morphological operations for extracting features of fingerprint
images.

Q5: Answer following questions
A [CO4] [BL-4] Compare Region growing approach with Segmentation using thresholding.

B [CO4] [BL-4] “Segmentation of any digital image focusing on the presence of discontinuities in the
image has different approaches” Discuss this statement with examples.

Q6: Answer following questions
A [COS] [BL-2] Explain various color models in detail.

B [COS] [BL-2] Write notes on video representation.

Q7: Answer following questions .
A [CO3] [BL-4] Discuss the following: a. Thinning b. Skeletonization.
B [CO3] [BL-4] Discuss step by step working of Hit or Miss Transformation.

FGI GIG Rc a a kk a ak a ka a a a

RAR 2 RRR

{10}

[10]

[10]

[10]

[10]

[10]

[10]

[10]
````

## 2024-25 · Final-Exam · Sem 5 · paper f45fd7272ef0

- Departments: Computer Engineering, Electronics and Telecommunication
- Programmes: B TECH / COMPUTER, B TECH / EXTC, B.TECH INTEGRATED / EXTC, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/IMAGE & VIDEO PROCESSING/Image and Video Processing Batch 2024-25 Final.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07/12/2024
- Text: ocr (4 pages), mean OCR confidence 83.3

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS EN GINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: B Tech /MBA Tech /BTI i Year: II/V Semester: V/IX
Stream/s: Computer Engineering/ Computer Science/ Electronics &Telecommunication

Engineering

Subject: Image and Video Processing Time:3 hrs (2.00pm to 5.00pm)
Date: 07/12/2024 No. of Pages: 4

Marks: 100

Final Examination (2024-25) 4 |

: 1°
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover

’
' @ of the Answer Book, which is provided for their use. 4
1) Question No. _1___ is compulsory. oa
2) Out of remaining questions, attempt any 4 __ questions.
3)Inall___5__ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Ql Answer briefly: a : [20]
Apply Median filter of size 3x3 on pixel underlined in the below image. Use zero padding.
8] 17] 4 | 10] 15
co-; 3 [30] 6 | 32] 3
sol. | a is}io| 7} 5] 9 BI
SORBL-
BL-2 4 )29|3 }si| 1
16 | 7 4 3 0
How do TIFF and JPEG differ in terms of compression methods, what impact does this have on image quality?
Explain the Erosion operation in detail. Consider a binary image
1 ij 1 0 1 1 1 1 1 0
1 1 1 0 1 1 1 1 1 0
CO-2; 1 1 1 1 1 1 1 1 1 1
sor, }& |f a [a fa fa fafaifaifafi [4 5]
BL-3 1 1 [1 1 1 1 1 1 1 I
1 1 1 1 1 1 1 1 1 1 x

The object takes up most of the image; with just four background pixels. Now, erode with a 3 x 3 structuring
element of all 1’s.
--- page 2 ---
»

c. | Apply region growing on the following, image. Consider initial point at (3,3), threshold value 2 and 4-

connectivity. 1 , 3
4
CO-3;
SO-1; 1 [0 1 2 0 [5]
BL3 2 2 5 6 [> 1 |:
3 1 4 7 3
4 0 2 5 1 |
CO-4; Explain the additive mixing for RGB color model in detail.
So-1; | 4. [5]
BL-2 : .
Explain the neighborhood and adjacency. According to the following intensity values of a 5X5 image, show the
paths by drawing dashed lines for 4-adjacency,8-adjacency and m-adjacency. let V= {1,2,3}.
2 5 8 3 4 2 .
Q ; 4 8 7 1 3 >|
CO-1; Ja 5 ; 1 ; 3 7 [lo] °
SO-1; -
| BL-3 8 2 3 6 1 .
2 4 6 9 3 j
Consider the given images
50 | 50 | 50 | 10 30 [| 10 | 10 | 10
50 50 50 10 10 50 10 10
Q2: 50 50 50 10 10 10 50 10
50 50 50 10 10 10 10 50
CO-3; | 5 Image 1 Image 2« [10]
SO-1; , é
BL-3 a) Apply the Horizontal and vertical Prewitt Operator on image | and find the magnitude of gradient,
b) Apply forward and backward Prewitt operator to identify the diagonal edges in image 2.
c) Write the observations on results found in (b).
Apply histogram equalization on the input image of 8x8 below. Let the input and output gray levels be in the )
range of [0, 7]. Also plot histogram of input image and histogram equalized image.
1 1 5 5 0 0 1 0
TPi;y2f2fPofi)ott1
Q3 :
CO-1; a 1 7 6 6 5 5 0 0 [10]
SO-1, O17); 677/575 7s 75
BL-3
--- page 3 ---
Q3
CO-4;
SO-1: b Explain the key differences between I-frames, P-frames, and B-frames. [10]

BL-2

Q4 For video processing, answer the following

CO-4; | 4 | a) Whatis the effect of Block size and Search space size in the block-matching algorithm of motion estimation?

[10]
SO-1; b) What are the key evaluation methods used in block matching for motion estimation?
BL-2

Apply Hit or Miss Transform to the original image to detect shape given in the following image. Discuss each

step in details.

a
%
Q4 Teh 1 1
CO-2; |», [10]
SO-1; 1
BL-3
_o 1
Original Image Shape *
On the given 4-bit image, apply gray level Slicing, without preserving background and with preserving
background. Show all the steps. Use T;=5 and T2=10.
Q5 12/5 ]/6)71]8
£0-1; | 4 . m/i4/is{3]4 [oy]
-2;
BL-3 8) 9] 5] 11] 12
715 ])]6]810
213 14 | 10] 13
A simple 6x6 image with only 6 grayscale levels shown below. Find optimal threshold using Otsu for threshold
value 3 and 4.
Image Histogram
Qs g ]
CO-3; b [10]
SO-1;
BL-3
--- page 4 ---
Q6

°

oa a | Explain the concept of Color Slicing in color image processing. [10]
BL-2
Explain the 2D Discrete Cosine Transform (DCT) with equations. Find the frequency domain representation
Q6 of the given 4x4 image f(x,y) using DCT.
cO-1; | 5 1fififi [10]
SO-1; x / L1{1l]1]1
BL-3 212|2/2
1{1}1 ji
Q7
cron a | Explain the Three-step search method for block searching between two video frames. [10]
BL-2 a
Explain the contract stretching of an image and apply it on the given 4x4 image. Consider rl=1, s1=2, r2=5
and s2=6. Note: The location of the points (r1, s1) &-(r2, s2) control the shape of the transformation function.
5
Ll
Q7 od (nia d
Bote b 2 1 2 1 [10]
a 4 5 6 oo
BL-3 8 b
3 2 1 4 ‘
6 2 1 6 j|eeeee ‘ :
0 at n L-1 ’

Apply the average filter at underlined pixel of a given image.
````

## 2024-25 · Final-Exam · Sem 6 · paper a4918285a336

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/EXTC/VI SEMESTER/IMAGE AND VIDEO PROCESSING/Image and Video Processing, Sem VI, Year 2024-25 Final Exam.pdf`
- Text: ocr (4 pages), mean OCR confidence 81.7

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
, SCHOOL OF TECHNOLOGY MANAGEMENT
Academie Year: 2024-2025

Program/s: B Tech /BTI Year: JII/VI: Semester: VI/XII

aE Tair
Stream/s ; EXTC/CSBS/ CSEDS
Subject: Image and Video Processing Time: 3 _ hrs ({osopayato 4:00pm)
Date:_10_/ 05 / 2025 No. of Pages:_4
Marks: _ 100

Final Examination(24- 25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover °
of the Answer Book, which is provided for their use.

1) Question No. _1_- is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) In all___5_ questions to be attempted. :

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi
Answer briefly: [20]

CO-1; a. : :

SO- 1; -Explain fundamental steps in digital image processing. [5]
BL-2 .

CO- 2; b. . 7 . : . “
§0- 1: Explain how to compute the gradient magnitude using Prewitt/Sobel [5] :
BL-2. operators.

co-4; Jc. ;

SO- 1; Compare global and adaptive thresholding with one example. [5]

BL-2

CO- 2; d.

SO- 1; Explain the different methods of histogram equalization of color images [5]

Pp q

BL-2
Q2 a Apply histogram equalization on the following grayscale image histogram:
CO-2; | Intensity o)i)2)3)4)5 16 (10) >
SO-1; Level :
BL-3

Frequency 50 | 100 | 200 | 150 | 165 | 121 | 173
--- page 2 ---
b With necessary equations and graphs, explain the following:

CO-2: @ Log Transformation
SO-1; Gi) Contrast Stretching [10]
BL-2

(iii) Image Thresholding

(iv) | Power Law Transformation

a Construct a 4x4 Hadamard matrix. Determine the Hadamard transform for
Q3 the given image matrix.
CO-2; 09 (7 (3 |) [10]
SO-1; 3/6 |4 |6 :
BL-5,6 2 |4 [2 [2
1/2 {5 {3
CO-5; |b ; Bee a aaa ;
SO-l; Explain what is motion estimation and why is it used in video compression? | [10]
BL-2 Explain the general steps involved in motion estimation.
a For the given binary image,
0 |1 |0 |0 |0
1 |1 |/0 {1 |0
Oo |i jl 1 |90
0/0 ;O |1 [tl
4
Q 0 j1 {0 |0 }0
CO-1; [10]
pea Determine whether pixel (1,1) is connected to pixel (2,3) using: ,
(i) 4-connectivity,
(ii) 8 -connectivity and
(iii) m-connectivity
Also calculate the Euclidean distance and chessboard between pixel (1,1)
and pixel (4,3).
CO-4, b : . : .
SO-1; Demonstrate the region growing segmentation process in detail: How does | [10]
BL-3,1 the merge tree contribute to improving the segmentation results?
--- page 3 ---
a Explain the significance of Otsu's method in image segmentation. Apply
Otsu's thresholding (within class variance) on the given input image and -
compute the optimal threshold T. Check for T=3 and T=5.

~

606 121 2 121

Q5 22222 2 2 2
ee $3 3 3 3 3 3 3 [10]
BL-23 $34444 44

44444444
5 6 6 5 5 5 5 6
6 666 77790

ae b Explain HSI model. With the help of equations, explain how HSI color [10]
BL-2 model is converted to RGB color model
a. (i) Explain opening and closing operations.
(ii) Apply the opening operation on the following binary image A using
06 structure elements By. Show all steps.
CO-3; @1110 10
SO-1; Piidi =e : 0)
BL-2.3 A=]l 1111 =
; 11liii i111
o1110
b. An image matrix is given below:
120 135 | 150 | 160
100 125 | 140 | 145
0-2: 80 [110 | 130 | 135
SO-1; 70 90 115 | 120 [10]
BL-3
Apply 3x3 mask for the following:
(i) Averaging Filter
Giy Median Filter
ii) High Pass Filter
Do zero padding.
--- page 4 ---
a 1]

Q7 (i) Explain I-frames, P-frames, and B-frames in video
compression?
Sone (ii) Explain how does an I-frame differ from a P-frame? [5]
BL2
b. 0) Explain the working of the 3-step search method. 15]
a s (ii) | Compare 3-step search and 2D-log search method of motion {5]
BL-3 estimation.
````

## 2024-25 · Final-Exam · Sem 12 · paper 744041adb481

- Departments: Electronics and Telecommunication
- Programmes: B.TECH INTEGRATED / EXTC
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/6th YEAR/EXTC/Sem_12/Image and Video Processing/Image and Video Processing Batch 2024-25 Final.pdf`
- Printed on paper: max marks: 100
- Text: ocr (4 pages), mean OCR confidence 79.5

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGI
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: B Tech /BTI Year: JII/VI: Semester: VI/XII

as war
Stream/s ; EXTC/CSBS/ CSEDS :
Subject: Image and Video Processing Time: _3__ hrs ({osopamto 1300 pw)
Date:_10_ / 05 /2025 No. of Pages:_4
Marks: 100

=

Final Examination(24- 25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover -
of the Answer Book, which is provided for their use. 4

1) Question No. _1_- is compulsory. “~

2) Out of remaining questions, attempt any __4 -__ questions. : :
3) In all___5__ questions.to be attempted. : . -,
4) All questions carry equal marks. :

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.

7) Assume Suitable data if necessary.

Qi

Answer briefly: ; . [20]
CO-1 ; a. .
SO- 1; Explain fundamental steps in digital image processing. [5]
BL-2 ; 4.
CO- 2; b. : . . : . *
SO- 1: Explain how to compute the gradient magnitude using Prewitt/Sobel [5] .
BL2. operators.
CO- 4; c. .
SO- 1; Compare global and adaptive thresholding with one example. [5]
BL-2
CO- 2; d.
SO- 1; Explain the different methods of histogram equalization of color images [5]

q :

BL-2 ‘
Q2 a Apply histogram equalization on the following grayscale image histogram:
CO-2; Intensity ofi/2{]3i14~1 5 /6 [10] ¢
SO-1; Level
BL-3 Frequency 50 | 100 | 200 [150 | 165 | 121 | 173
--- page 2 ---
b

With necessary equations and graphs, explain the following:

CO-2: (i) Log Transformation
SO-1; (ii) Contrast Stretching _ [10]
BLS (iii) Image Thresholding
(iv) | Power Law Transformation
: Construct a 4x4 Hadamard matrix. Determine the Hadamard transform for
Q3 the given image matrix.
CO-2; 017 |3 |i [10]
SO-1; 3.16 |4 16
BL-5,6 2 [4 $2 |2
1 |2 |5 13
CO-S; b F 2 sg :
SO-1; Explain what is motion estimation and why is it used in video compression? | [10]
BL-2 Explain the general steps involved in motion estimation.
a For the given binary image,
Oo /1 {0 {0 |0
1 }1 ;0 |1 /0
0 {1 J1-J]1 = |0
0 }0 |O0 |1°}1
4
® 0 }1 |0 |0 |0
CO-1; [10]
. ; Determine whether pixel (1,1) is connected to pixel (2,3) using: ;
(0) 4-connectivity,
(ii) 8 -connectivity and
(iii) | m-connectivity
Also calculate the Euclidean distance and chessboard between pixel (1,1)
and pixel (4,3).
CO-4; b . :
SO-; Demonsirate the region growing segmentation process in detail: How does [10]
BL-3,1 the merge tree contribute to improving the segmentation results?
--- page 3 ---
¥

a Explain the significance of Otsu's method in image segmentation. Apply”
Otsu's thresholding (within class variance) on the given input image and -
compute the optimal threshold T. Check for T=3 and T=S.

c¢ 00 i tL idiil

Q5 222222 2 2
Sot . 3.3 3 3 3 3 3 ~3 [10]
BL23 3.3 444444

44444444
5 56 56 5 5 5 5 6
666 6 7 7 7 0

Sou. b Explain HSI model. With the help of equations, explain how HSI color [10]
BL-2 model is converted to RGB color model
a. (i) Explain opening.and closing operations.
(ii) Apply the opening operation on the following binary image A using
Q6 structure elements B,. Show all steps.
CO-3; 01110 ; 10
SO-1; l1liidtl mala 9 4 ; [10]
BL-2,3 A=|{l 1111 i=l t
tidiii iid
0 1110
b. An image matrix is given below:
120 | 135 | 150 | 160
100 | 125 | 140 | 145
CO-2: 80 110 | 130 | 135
SO-: ‘170 [90 | 115 | 120 [10]
BL-3

Apply 3x3 mask for the following:
(i) Averaging Filter
(ii) Median Filter
(iii) High Pass Filter

Do zero padding.
--- page 4 ---
: an 5]

Q7 (i) Explain I-frames, P-frames, and B-frames in video
compression?
Sone (ii) | Explain how does an I-frame differ from a P-frame? [5]
~BL-2
b. (i) Explain the working of the 3-step search method. 5]
—_ : (ii) | Compare 3-step search and 2D-log search method of motion [5]
BL3 estimation.

rey
````

## 2024-25 · Re-Exam · Sem 5 · paper 45c95f1f3aae

- Departments: Computer Engineering, Electronics and Telecommunication
- Programmes: B TECH / COMPUTER, B TECH / EXTC, B.TECH INTEGRATED / COMPUTER, B.TECH INTEGRATED / EXTC, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/IMAGE & VIDEO PROCESSING/Image and Video Processing, Sem-V, Batch 2024-25, Re Exam.pdf` (+4 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15/02/2025
- Text: ocr (4 pages), mean OCR confidence 88.5

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2024-2025
Program/s: B Tech /MBA Tech /BTI , Year: II/V Semester: V/IX

Stream/s: Computer Engineering/ Computer Science/ Electronics &Telecommunication

Engineering

Subject: Image and Video Processing Time:3 hrs (2.00pm to 5.00pm)
Date: 15/02/2025 No. of Pages: 4
Marks: 100

Re Exam (202.4 -25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql ;
Answer briefly: [20]
Explain sampling and quantization in detail. Apply sampling (T=0.6sec) and Quantization (L=4 levels) to the
given signal by considering the voltage from (0 to 16). And find its pixel values?
IB orp
16 a
14h
Voltaget? +
CO-1; 10}.
SO-1; a. ak [5]
BL-2 6
4
2
<!) L L x ‘ smetfail a L L x ‘
0.6 1.20 18 24 30 36 42 48 54 60
Time
Sampling points are (0.6,3), (1.2,10), (1.8,5), (2.4,13), (3.0, 8), (3.6,1), (4.2,12), (4.8,5), (5.4,9), (6.0,6)
A 8-bit Gray scale image with zero padding is shown below. Apply gray level Dilation operation on this
C0-2: image with the flat 3X3 structure element.
1: |b. [5
te 0 0 0 0 0 0 0
0 10 20 30 40 50 0
0 60 70 80 90 100 0
--- page 2 ---
0 110 120 130 140 150 0

0 160 170 180 190 200 0
0 210 220 230 240 250 0
0 0 0 0 0 0 0

Given an image patch of 3-bit gray scale image and perform the following tasks without changing the output
image resolution.

a) Compute the First-Order and second order Derivative of 3" row. Write the observations on results.

b) Apply region splitting of a given image with the threshold value 4.

Cc
1 2 3 4 5 6 i 8
CO-3; 1 1 || 17271 ine
80-1: | 2.) (Bom R20 on 2m Nom zn mom| me [5]
BL-3 8 4 7 d 1 2 3 3 7
4 3 3 3 3 3 5) 5) 3
5 6 6 6 6 3 3 3 8
6 3 3 3 3 3 3 3 3
7 3 3 3 5 3 3 3 3
8 3 8) 3 3 1 1 1 1
pork d. | Explain the YUV color model and its components. Discuss the advantages of using the YUV color model in [5]
4 video compression.
BL-2
For the given image, S(x,y)
a) Identify the type of image (binary/ gray/ color)
b) How many bits required to represent this image by considering the range of pixel values.
c) Find the Euclidean, City block and chess board Distance between S(2,1) to S(4,5)?
d) Convert image into binary with Threshold 45 and find the number of bits required for storing the binary
image?
Q2 e) What happens if we reduce the number bits required to represent a pixel?
CO-1; a f) What are common bit depths used for grayscale images? How does bit depth affect the grayscale [10]
SO-1; resolution of an image?
BL-3
1 2 3 4 5
1 65 25 95 65 40
2 10 95 40 65 25
3 95 25 65 40 65
4 65 40 40 10 25
5 25 65 10 65 10
Consider the given images
10 10 10 10 30 10 10 10
Q2 10 10 10 10 10 30 30 10
co-3; | 4 30 | 30 | 30 | 30 10 | 30 | 30 | 10 10)
SO-1; 30 30 30 30 10 10 10 30
BL-3 Image 1 Image 2

a) Apply the Horizontal and vertical Sobel Operator on image 1 and find the magnitude of gradient.
b) Apply forward and backward Sobel operator to identify the diagonal edges in image 2.
--- page 3 ---
c) Write the observations on results found in (a) and (b).

Calculate the histogram equalization of the given 3-bit image segment. Plot the histogram of input and resultant
image. Analyze the histograms.

7 6 6 3 1 0

Q3 2/5/5115 1110 :
CO-1; a [10]
SO-1: 28 se olson ales
Bu 2 Sela isis
3 7 2 5 2. 3.
5 6 6 2 2, 2
Q3 F
For video processing,
CO-4; .
oe b a) What is pixel difference motion estimation, how does it work? [10]
aL > b) What are its advantages and disadvantages in the context of video compression and motion tracking?
Q4
a a | Explain the Exhaustive block search algorithm of motion estimation in detail. [10]
BL-2
Apply Hit or Miss Transform to the original image A to detect shape B1 given in the following image.
Discuss each step in details.
Image A
Qs |
CO-2; |p. |— [10]
SO-1;
BL-3
In gray level transformations,
a) Calculate the image negative, log and power law transformations (for C=1 and gamma= 0.5) of the
given image.
5)
Q b) What is Gamma Correction and how does the value of gamma affect the image?
ane nanan ime [10]
SO-2;
BL-3

1 2 2 6

1 2 0 6

7 1 5) 5
--- page 4 ---
A 3-bit image matrix is given below. Find optimal threshold using Otsu for threshold value 3 and 4.

95 7 5 1 1 2
CO-3; |» 1 0 5 6 6 [10]
SO-1;
BL-3 0 2 4 4 2
3) 5 2 1 1
5 3 3 2 7
Q6
ot 2 a | What are the main characteristics that differentiate the RGB, CMYK, HSI, HSV, and YUV color models? [10]
BL-2
a) Calculate the Hadamard transform for a 4x4 f(x,y) as shown below.
b) Discuss the energy compaction characteristics of the Hadamard transform and how it differ from the
Discrete Cosine Transform (DCT).
Q6 10 10 10 10
CO-1;
sou |? 20 20 20 20 [10]
BL-
20 20 20 20
20 20 20 20
Q7 For video processing,
CO-4; Ja a) Explain the two-dimensional logarithmic search method for block searching between two video | [10]
SO-1; frames.
BL-2 b) Write the advantages and disadvantages of this method.
Given an image patch of 3-bit image and perform the following tasks without changing the output image
resolution.
a) Calculate the response at pixel location (2,3) using 3X3 mean filter
b) Calculate the response at pixel location (1,2) using 3X3 average and weighted average filter
c) Calculate the response at pixel location (2,1) using Laplacian filter (without diagonals)
d) Calculate the response at pixel location (2,1) using Laplacian filter (with diagonals)
Q7 e) What is the role of average, weighted average and Laplacian filters in image enhancement?
CO-1; | ; 1 2 3 4 5 [10]
SO-1;
BL-3 1 4 4 4 4 4
2 2 2} 3 5 5
3 2 2 3 =) 5
4 6 6 6 6 6
5) 1 i 1 1 1
````

## 2023-24 · Exam not stated · Sem 5 · paper c2adf28ac9a2

- Departments: Computer Engineering, Electronics and Telecommunication
- Programmes: B TECH / COMPUTER, B TECH / EXTC, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/IMAGE & VIDEO PROCESSING/B Tech, (COMP EXTC), Image and Video Processing, Semester-V, Batch 2023-24 & 2024_89f51633.pdf` (+2 identical copies)
- Printed on paper: max marks: 100
- Text: ocr (3 pages), mean OCR confidence 86.7

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2025-2026

Program/s: BTECH INTG /B TECH /MBATECH Year: mpg Semester: V/re.
Stream/s: COMP/EXTC

Subject: Image and Video Processing Time: 3 __ hrs (2:00 pnto 5:00 pm
Date:_0 8 /Deg/ 2025 No. of Pages: 3

Marks: 100

Re-Examination (2023-2024, 2024-2025)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.

2) Out of remaining questions, attempt any 4 __ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
Col; What is the difference between 4- and 8-connectivity in a digital image?
SO-1; a list two discrepancies. 5M
BL-l ;
C02 ;
SO-1; b. | Explain Walsh Transform with equation. 5M
BL-2
Co3 Compare the results of boundary extraction and edge detection — how do
SO-1: c. | they differ in output and purpose? 5M
BL-2
CO4 Describe region-based segmentation techniques. What criteria are used to ri
an d, | determine pixel inclusion?
Q2
COl: Apply histogram equalization on the given 8x8 image. The gray level
Sol; distribution is given below:
BL3

1|Page
--- page 2 ---
[10]

Gray level |0 j 1 2 13 4 5 6 7

No. of

pixéls 18 {10 |}3 |2 2 |3 14 12

Draw the original histogram and the equalized histogram.

Determine Discrete Cosine Transform of the following Image matrix:

Q2 b 52 55 61 66
Sox. 78 61 64 73 [10]
’
BLS; 63 65 66 68
58 62 6@ 59
Q3
Col; a | Explain Bit plane slicing and contrast stretching with neat sketch. [12]
Sol;
BL2;
Q3
Sox: b | State the properties of Hadamard and Walsh Transform. [08]
BL2;
Q4 Discuss thinning and thickening operations in morphological image
“an a | processing. How are they implemented, and in what scenarios are they [10]
BLE: useful?
Apply region growing on the following image.
b Row\Col 1 2 3 4 #5
1 16 18 12 56 52
Q4 2 10 12 13 51 358
C04, 3 1212 14 «49 «48 [10]
SO}; 4 ao 78 79 49 47
BL3;
5 82 81 88 46 45

Consider initial point at (3, 3), threshold value 2- and 4-point connectivity.

2}|Page
--- page 3 ---
Q5 4 | Discuss neighborhood processing techniques in image enhancement. How

_ do smoothing spatial filters differ from sharpening filters, and what are [12]
BLS: their respective roles in noise reduction and edge enhancement?
Q5 b
COl: Compare the energy compaction of DCT and Hadamard transform. Which
; . . . [08]
SOl; transform retains more energy in fewer coefficients?
BL4
a_ | Given a 4x4 image
10 42 14 46}
11 13 15 47
AA 50 52 54 56
i Si 53 55 57
SOl; [10]
BL4; . . . : . ae
Starting with 2x2 regions from the image above, merge adjacent regions if
the difference in mean intensity is less than 5. Show the final merged
regions.
Q6 b__| Perform iterative thresholding starting with T = 100 for: Group A: [40, 50,
Son 60, 70} Group B: [130, 140, 150, 160] Compute the new threshold and [10]
BL3 repeat until convergence.
Q7 4 | Describe the classification of video frames in compressed video streams.
Sor: What are I-frames, P-frames, and B-frames, and how do they contribute to | [10]
BL2 efficient video encoding and decoding?
Q7 b- | Discuss the block matching approach to motion estimation. How does it
con work, and what are the key parameters involved in evaluating motion [10]
BL6 vectors?

3|Page
````

## 2023-24 · Final + Re-Exam · Sem 5 · paper 181c75eef8a3

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/IMAGE & VIDEO PROCESSING/Image and Video Processing ,Final,Re-exam 23-24,22-23.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (7 pages), mean OCR confidence 80.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINE
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2023-2024

Program/s: BTech/ MBA Tech Year: III Semester: V
Stream/s ; CE/CS

Subject: Image and Video Processing
~ Date:_28 /11 2023
Marks: 100

Time: 03 hrs (02pm to 05pm)
No. of Pages: 07

Final Examination/Re-Examination ( 2023-24] 2022-23)
Instructions: Candidates should read carefull

y the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for th

eir use.

1) Question No. _|___ is compulsory.

2) Out of remaining questions, attempt any 4
3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary,

questions.

[Qi ]
Answer briefly: (20]
CO-1; Jal. Tin a digital image, how does the 4-connectivity differ from the [02]
ek 8-connectivity? Give any 2 differences.
CO-1; a. 2.
SO-1; Enlist four applications of image enhancement in spatial domain. [02]
BL-1
CO-2; |b .
= SO- 1: Prove that 2 x 2 Hadamard transform matrix is Unitary. [04]
BL-4
CO-3; c. _
SO-1; What is Hit-or-Miss Transform? Why it is used for? [04]
BL- |
CO-3; |d .
SO- 1: What is thresholding? Explain different types of Thresholding. [04]
BL-1
CO- 4; e. | Consider a scenario of a video signal. Two consecutive frames (each of
SO-1.6 ; size, MXN) of video are same except that an object in one frame is located
BL-5

at a different location in the next frame. Justify that instead of saving two [02]
frames, first frame and motion vector for the second frame should be saved

L in memory.

Page 1of7
--- page 2 ---
CO-4 ;

e.2. | State whether the following statement is true or false and justify your

BOs 1183 answer:

BL-5 7 ee | [02]
“Increasing the block size reduces computational complexity” while
compromising on compression efficiency”.

Q2 a. Describe process to obtain image negative. On the below image of size
mas g

CO-I: 5 x 5. Apply described process to obtain digital negative image of the 3 BPP

SO-1; image shown below:

BL-3 1 2 2 2 2 [04]

3 2 4 5 2
7 7 7 7 6
2 2 2 3 3
4 4 4 4 4

CO-1; b. Imagine you are working on a task to digitize old photographs for a

aa historical archive. Explain, in detail, the processes of sampling and
quantization in the context of converting analog photographs into digital [08]
images. Discuss the relationship of quantization with gray level resolution.

Also, analyse how the number of bits in an image define the size and quality
of the image.
CO-2; | ¢. Derive 4 x 4 Hadamard transform matrix from 2 x 2 Hadamard transform
nae matrix. Compute Hadamard Transform of the following 4 x 4 image.
2 }1 42 [1 [08]
1 1 |2 42
2 Z 1 1 ;
1 }2 |1 |2
Q3 a. Consider the following image matrix of size 7 x 7.
0o;0;0]0;]0/]0 i; 0
CO-3;
SO-1: 0 {10}; 0}; 0} 0} 10} 0
BL-2 0 [0 | 10] 0 | 10] 0 | 0
0} 0/;/0/;/10}; 0} 01] 0 [04]

0 | 0/10}; 0 {10} 0} 0

0 |10/} 0/0; 0 4} 10; 0

0}; 0;0}]0]0/]04 0
Show the effect of diagonal line detector on image matrix.

Page 2 of 7

5
--- page 3 ---
oo

CO-1; | b. Illustrate the concept of Bit-plane Slicing. Also, apply Bit-plane Slicing oh |
ne given below 3-bit image. Size of image is 5 x 5. Po
110 | 111 | 110 ] 110 | 111
000 | 000 | 000 | 001 -| 010 [08]
001 001 | 001 | 010 | 011
100 | 101 | 101 | 100 | 010
| aa 100; 110 ; Til | 111
CO-2; | c. Calculate Discrete Cosine Transform of following image of size 4 x 4.
ae 2 [2 [2 |2
1 1 1 l [08]
1 }1 1 1
2 1/2 |2 |2
Q4 a.
sO. Explain about Predicted frame (P-frame) of a motion picture. [04]
BL-5
CO-3; |b. Perform the following operations on the shown below image of size 5 x 5
SO-1;
BL-3
1, Obtain the thresholded image for 3 BPP image A, shown below.
Consider threshold value=4.
1 2 2 2 2 .
3 2 4 5 2 [08]

2. Apply histogram equalization on the above image A.

Page 3 of 7
--- page 4 ---
CO-3; | c. Interpret the result of Erosion operation on given image A using given i

Me structuring element B. Size of image A is 10 x 10.
0}0}0}0}0;0}0]0)0/0
O} 1} 1} 1/0}0]0}.0]}0)0

O} 1} 1} 1)O; 1; 1} ry} tyo

ee

0; 0;O;}1} 1} 1} 1} 1)0]0 [08]
0; O/O;1} 1} 1} 1) 1}; 0]0
0}0/0/0/0}0}0)0/0]0
A
0}; 140
1}1)1
0;1)0
B
Q5 Co For a video compression standard, justify the use of B frames and prove
SO a that B frames provide maximum compression. [04]
BL-5 x
CO-4; | b.
SO-1,6; Explain exhaustive search algorithm of motion estimation in detail. [08]
BL-2
aan, c. What is the concept of edge linking? Explain local processing approach [08]
BL-2 used for edge linking using suitable example.
Q6 a
Sola Explain with block diagrams the working of a video encoder and decoder. | [04]
BL-3
con be Consider the following image matrices [08]

Page 4 of 7
--- page 5 ---
vo

BL-5S 3 |3 |6 16 30 | 30 | 30 | 30 | 30
0 |0 |0 |0 30 | 30 | 30 | 30 | 30
3 |3 | 6 |6 60 | 60 | 60 | 60 | 60 “oe
S10 ie 60 | 60 | 60 | 60 | 60
3 |3 |6 |6
0 |0 |0 |0
3 |3 |6 |6
0 |0 |0 {0
3 |3 |6 |6
0 {0 (oO |0
Image 1 Image 2
1. Use Prewitt Operator to determine Gradient Vectors g, and gy
2. Determine Magnitude and angle of gradient vector
Which of the edges are found in each of given images.
CO-3; c. Apply Opening operation on given image A using given structuring
ted element B. Size of image A is 5 x 7.
0}0/0}0)0
O}1};1)0/0
O}1)/1])0)0
O;1{}1]0])0
O; 1) 1) 1]0 [08]
0/;0}1)1)0
0}0}0])0)}0
nN :
0}1)90
1J1]1
0}1)0
B
Q7 a. Compute the Mean of Absolute Differences (MAD) and the Sum of
CO-4; Absolute Differences (SAD) between —
SO-1,6; [04]
BL-S a) blocks A and B

b) blocks A and C

Page 5 of 7
--- page 6 ---
Conclude whether B or C is a better candidate for motion estimation wur.t

ia ee
fl 72 ]1 -
2/4 |2
1 |2 1
Block A
2 )1 2
4/2 4
2 (1 2
Block B
1 |2 |2
2 |4 4
2. \2 ]
~ BlockC
CO-3; | b. For a given image perform segmentation by applying region growing.
BLE 7/7)7[5|2]12]|7 | 6

. 08)
Choose a seed point at (2,3) and (6,6), where row and column indices start
from 1. Predicate is that the difference between minimum and maximum
intensity should be less than or equal to 3. Use four neighbors’ concept to
examine predicate on new candidates.

Size of image is 8 * 8.

Page 6 of 7
--- page 7 ---
,~

CO-3;
SO-1;
BL-3

c.

Apply Closing operation on given image A using given structuring
element B. Size of image A is 5 x 7.

0/0/0}/0)0

O} 1} 1}0}0

O; 1} 1}/0}0

[08]

Page 7 of 7
````

## 2023-24 · Final-Exam · Sem 5 · paper ed5f06cd95c6

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/IMAGE & VIDEO PROCESSING/Image & Video Processing, Sem-V, A Y 2023-24, Final Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 /11 2023
- Text: ocr (7 pages), mean OCR confidence 82.0

````text
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT&

Program/s: BTech/ MBATech

Stream/s ; CE/CS

SCHOOL OF T

Subject: Image and Video Processing

~ Date: 28 /11 2023
Marks: 100

Final Examination/Re-
Instructions: Candidates should read carefully the i

Academic Year: 2023-2024

SVKM’S NMIMS

ECHNOLOGY MANAGEMENT

wis UNIVERS

dod ———
Year: III Semester: V

Time: 03 hrs (02pm to 05pm)
No. of Pages: 07

Examination ( 2023-24/2022-23)

nstructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use

1) Question No, Jk

2) Out of remainin:
3) In all

—_5_ questions to be attempted.

___ is compulsory.
questions, attempt any 4

4) All questions carry equal marks.

5) Answer to each

new question to be started on

6) Figures in brackets on the right hand side ind

7) Assume Suitable da

ta if necessary,

questions.

a fresh page.
icate full marks.

Answer briefly: [20]
In a digital image, how does the 4-connectivity differ from the [02]
8-connectivity? Give any 2 differences.
Enlist four applications of image enhancement in spatial domain. [02]
. . . ‘
SO- 1; Prove that 2 x 2 Hadamard transform matrix is Unitary. [04]
BL-4
CO-3; jc. Cn . a
What is Hit-or-Miss Transform? Why it is used for? [04]
What is thresholding? Explain different types of Thresholding. [04]

frames, first frame and moti
in memory.

next frame. Justify that instead of saving two | [02]
On vector for the second frame should be saved

Page 1 of 7
--- page 2 ---
é

CO-4; |e.2. | State whether the following statement is true or false and justify your

SO- 1,63 answer:
ald 3 , 3° | [02]
“Increasing the block size reduces computational complexity while
compromising on compression efficiency”.
Q2 a. Describe process to obtain image negative. On the below image of size
CO-1: 5 x 5. Apply described process to obtain digital negative image of the 3 BPP
SO-1; image shown below:
BL-3 1 2 2 2 2 [04]
3 2 4 5 2
7 7 7 7 6
2 2 2 3 3
4 4 4 4 4
CO-1; | b. Imagine you are working on a task to digitize old photographs for a
ae historical archive. Explain, in detail, the processes of sampling and
quantization in the context of converting analog photographs into digital [08]
images. Discuss the relationship of quantization with gray level resolution.
Also, analyse how the number of bits in an image define the size and quality
of the image.
CO-2; c. Derive 4 x 4 Hadamard transform matrix from 2 x 2 Hadamard transform
a matrix. Compute Hadamard Transform of the following 4 x 4 image.
2 |1 42 [1
08
[1 Toy 2 2 iv
2 2 1 1
1 {2 |i {2 c
Q3 a. Consider the following image matrix of size 7 x 7.
CO-3: oyololo}ojo|o
80-1: 01/10; 0 | 0 | 0 | 10] 0
BL-2 o{/o [10] 0|10| 0 | 0
o|o}ofiolo|o|o [04]
0/0 | 10] 0 | 10| 0 | 0
Oale10c) On| O=-201-10 4150
o|fofofo|o|o jo
Show the effect of diagonal line detector on image matrix. +]

Page 2 of 7
--- page 3 ---
é

Illustrate the concept of Bit-plane Slicing. Also, apply Bit

-plane Slicing on
Paes
given below 3-bit image. Size of image is 5 x 5,

1. Obtain the thresholded image for 3 BPP image A, shown below.

Consider threshold value=4,

2. Apply histogram equalization on the above image A.

Page 3 of 7
--- page 4 ---
&

Interpret the result of Erosion operation on given image A using given |

CO-3; C;
ra structuring element B. Size of image A is 10 * 10. a
010] 0; 0] 0}0|0)|0}0)0
Ol1i1}1/ofo0}o)0}0;0
Oar 1 Fag) 04 er | pe
Olifalifififijiy2yo
Oli/1iijofif}ijy1)1)6
Ol1}1/1]0/0}0|0/0)0
010] 0/0] 0)/0{0} 010) 0
ofololi{if{ifil{1)ojo [08]
Ofolofiljifijiji{oj}o
Olofololojojoj;oj;oj;o) ,
A
fo}1]o
1{a[
0};140
B
Q5 For a video compression standard, justify the use of B frames and prove
aout: that B frames provide maximum compression. [04]
BL-5
CO-4; r
SO-1,6; Explain exhaustive search algorithm of motion estimation in detail. [08]
BL-2
ey What is the concept of edge linking? Explain local processing approach [08]
BL-2 used for edge linking using suitable example.
Q6
eet: Explain with block diagrams the working of a video encoder and decoder. | [04]
BL-3
can Consider the following image matrices [08]

Page 4 of 7
--- page 5 ---
BL-5 Bie Pee a fceaina 30 | 30 | 30 | 30 | 30 4

0 }0 |o Jo 30 | 30 | 30 130 [30] 4»
3/3 16 6 60 | 60 | 60 | 60 | 60 |
0 |0 10 {0 60 | 60 | 60 | 60 | 60

3 [3 16 [6

0 |0 |o Jo

3 13 16 l6

0 |}0 [0 Jo

313 16 [6

0 |o 10 Jo

Image | Image 2

1. Use Prewitt Operator to determine Gradient Vectors g, and Iy

2. Determine Magnitude and angle of gradient vector

Which of the edges are found in each of given images.

CO-3; Jc. Apply Opening operation on given image A using given structuring
cay element B. Size of image A is 5 x 7.
0/0/0/0)0
0; 1)1/0}0
O;1}1)0];0
O}1}1])0/;0
Oe fede|P 1.0 [08]
O;O0}1];1])0
0}0/0}0/0
A ‘
0;1)0
1/1} 1
0}1)0
B
Q7 a. Compute the Mean of Absolute Differences (MAD) and the Sum of
CO-4; Absolute Differences (SAD) between —
Ar a) blocks A and B [04]

b) blocks A and C

Page 5 of 7
--- page 6 ---
4

Conclude whether B or C is a better candidate for motion estimation w.r.t

A. oat
feat ey =
214 12
1 [2 ]
Block A
2.|:1 2
4/2 |4
pe | 2
Block B
Disp2 2] 2
214 |4
242 1
Block C
CO-3; | b. For a given image perform segmentation by applying region growing.
pie PDN Te S| 2 | 2 oe 6

sis} 5},6;4} 7] 8/7 ‘

08
Choose a seed point at (2,3) and (6,6), where row and column indices start ies
from 1. Predicate is that the difference between minimum and maximum
intensity should be less than or equal to 3. Use four neighbors’ concept to
examine predicate on new candidates.

Size of image is 8 x 8.

Page 6 of 7
--- page 7 ---
Apply Closing operation on given image A usin

ig given structuring ©
sat
element B. Size of image A is 5 x 7,

Page 7 of 7
````

## 2023-24 · Final-Exam · Sem 8 · paper 7982616b71ec

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC, B.TECH INTEGRATED / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/EXTC/Sem_08/IMAGE & VIDEO PROCESSING/Image and Video Processing Batch 2023-24 Final.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 86.0

````text
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING

Academic Year: 2023-2024 ao
whe
Program: BTech / BTI Stream: CSBS / EXTC Year: 2023-24 Semester: VIII/ XII
Subject: Image and Video Processing Time: 3 hrs (10.00am -1.00 pm)

Date:_ 29/4/2024 . No. of Pages: 05

Marks: 100

A=

Final Examination fi oo.
Instructions: Candidates should read carefully the instructions printed on the question paper and‘on

of the Answer Book, which is provided for their use.
1) Question No. _1_ is compulsory.
2) Out of remaining questions, attempt any _4 questions. Sy.
3) In all_5_ questions to be attempted. ~
4) All questions carry equal marks.
= 5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Fh oe

—
Ql Answer briefly:
CO-1 | a.
SO-1 Justify the importance of spatial resolution in deciding image quality. [04]
BL- 5
b. | Apply median filtering on both the given 5x5 images to generate 3x3 output images
(ignore border pixels). To what conclusion do you reach after comparing both output
images?
100 100 100 100 100
100 0 100 100 100
100 100 100 0 100
™ 100 100 0 100 0
. col 0 100 | 100 | 100 | 100
Sor Image (A) ~ [04]
BL- 3
0 100 0 100 0
100 0 0 0 100
0 100 100 100 0
100 100 0 0 0
0 100 0 100 0
Image(B)
CO-3 | c. . . . . . :
S0-1 Describe the effect of applying the Hit-or-Miss transform operation on the binary [04]
image.
BL-2 8 |

1|Page
--- page 2 ---
i

CO-3 | d.

S0-1 Summarize how LoG operator performs better than the Laplacian filter in edge [04]
BL-4 detection.
CO-4 |e. F : a en
SO- 1 Write a note on the three-step search method for motion estimation in video [04]
BL-2 processing.

a.

Apply erosion on the given input image A using the given structuring element B.
Size of the image is 9x9. Also list 4 uses of Erosion operation.

O;O/0;O0;O0loToToTo
O;/1;0;/0}0};0;1fo0fo

Q2 Of1;0;0;1}1]}1 7170
CO-3 O1}1;1;0];1{1]717fo0To
SO-I Ofififolilfilililo o7;i To [10] >
BL-3 Ofofololilililolo Bua
O;O;O;1y;isfililoto a
o;oOfo;ifolilolilo ae ON Peg
O;O;O;O0;0lo;oTlalo B
Input Image “A” Structuring Element
Q2 b. | Apply histogram equalization on the given 10x15 image. Draw the original
CO-1 histogram and the equalized histogram. The gray level distribution is given below:
$0-1 Gray levels | 0 1 2 3 4 5 6 7 [10]
BL-3 No. of 5/10} 25] 60]35] 5 | 5
pixels

a. | Apply Hadamard transform on both the given images. Analyze why the DC [10]
coefficients of both images same even though both images are different and
comment on the nature of the images from their Hadamard coefficients.

2 0 1 1
Q3 2 0 1 1
CO-2 2 0 1 1
SO- 1 2 0 1 1
BL- 4 Image (A)
2 1 1 0
2 1 1 0
2 1 1 0
2 1 1 0
Image (B)

2| Page
--- page 3 ---
on

Pa

i

b.

Using the highlighted pixel as the seed value, apply region-growing sepraeptation on | [10]
the given image using the following conditions —

a. 4 connectivity

b. The threshold value is 4. [(max — min) <= 4]

Q3
CO-3 r}a}s]{fets]5
SO-1 2 1 6 7 4 6
BL-3 3 | 714] 6 ]7
1;/o;5];s5]71]6
2/o0]4]6]8]5
o/i}e6]4]s5]a
Q4 a. [10]
CO-1 ‘ . . .
$0-1 Illustrate the process of up-sampling and down-sampling using suitable examples.
BL-3
b. | In medical imaging, doctors often rely on various image processing techniques to | [10]
analyze and interpret diagnostic images effectively. Consider a scenario where a
radiologist is examining X-ray images of a patient's chest to diagnose potential
respiratory conditions such as pneumonia.
Using morphological operations, the radiologist intends to enhance the visibility of
Q4 lung nodules, which are small abnormal masses that may indicate the presence of
CO- 3 pneumonia. The radiologist plans to apply dilation and erosion operations to highlight
SO-1 these nodules while minimizing noise and artifacts present in the X-ray images.
BL-5 Given this scenario:
a) Discuss how morphological operations and algorithms can be applied to analyze
medical images effectively by giving the steps involved in each operation.
b) Provide insights into the potential challenges and considerations when applying
these techniques to medical imaging data and discuss the impact of accurate image
processing on patient care and outcomes.
a. | Consider the given input image. Apply the following edge detection techniques on [10]
the highlighted pixels of the image- (ignore border pixels)
a) Horizontal Sobel operator (3x3)
Qs b) Vertical Prewitt operator (3x3)
CO-4 0 1 0 2 7
SO-1 2
BL-2 5
1

5 4 2 2 5

3|Page
--- page 4 ---
bre

Qs. |b. P [10]
COo- 3 Explain Chroma subsampling in video processing in detail.
SO-1
BL- 3
a. i. Apply 3x3 smoothing filter on the given 5x5 image and produce 3x3 output | [10]
image.
50 | 50 | 50 | 50 | 50
50 | 200 | 200 | 200} 50
50 | 200 | 200 | 200} 50
50 | 200 | 200 | 200] 50
oo 50 | 50 | 50 | 50 | 50
SO-1 ii. Apply 3x3 sharpening filter on the given 5x5 image and produce 3x3 output
BL-3 image.
50 | 50 | 50 | 50 | 50
50 | 200 | 200 | 200} 50
50 | 200 | 200 | 200] 50
50 | 200 | 200 | 200} SO
50 |-50 | 50 | 50 | 50
iii. Prove that: 1 — (low pass filter) = (high pass filter).
b. | Compute the DCT coefficients of the given image. Also find: [10]
i. Energy of each coefficient
ii. Total energy
Q6 iii. Percentage of total energy contained in DC coefficient
CO-2 Analyze why the first coefficient is called the DC coefficient and has the highest
SO-1 value.
BL-4 1 4 3 2
2 i a !
3 2 1 4
4 3 2 1
Q7 a. | Describe the process of segmentation using thresholding and how it can be applied to [06]
CO- 3 partition an image based on intensity levels. Provide examples to illustrate the
SO-1 application of thresholding for image segmentation and discuss the factors that
BL-3 influence the selection of appropriate thresholding techniques.
b | Apply thresholding on the given input image. Consider T = 75. Also list applications | [04]
Q7 of thresholding.
CO- 3 200 | 50 | 100 | 250 | 170 | 60
SO-1 20 100 | 100 | 100 | 20 | 100
BL-3 70 100 | 250 |50 |70 | 170

230 | 170 | 100 | 20 100 | 20

4|Page
--- page 5 ---
cs

r [10]
Justify the importance of | frames and P frames in video compression with suitable

diagrams.

; 5|Page
````

## 2023-24 · Re-Exam · Sem 5 · paper d66554f617bc

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/IMAGE & VIDEO PROCESSING/Image & Video Processing , Re-exam 2023-24,2022-23.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (6 pages), mean OCR confidence 79.6

````text
SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING

SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024

Program/s: BTech/ MBATech
Stream/s ; CE/CS

Subject: Image and Video Processing
Date: 06/o2]2024

Marks: 100
Re-Examination ( 2023-24/ 2022-23)

Instructions: Candidates should read carefully the instructions printed on the question pape
of the Answer Book, which is provided for their use. '

1) Question No. _1 is compulsory.
2) Out of remaining questions, attempt any _4 questions.

Year: III Semester: V

Time: 03 hrs (02pm to 05pm)
No. of Pages: 06

r and on the cover

4“
| 3) In all __5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
{Ql ~
Answer briefly: [20]
CO-1; |a.1. | Explain the concept of sampling in digital image processing. Provide an
an example to illustrate how these processes affect the representation of a | [02]
continuous image in a digital form.
| CO-1; | a.2.
SO-1; What is Logarithmic transform for image enhancement? ‘ [02]
| BL-S
CO-2; |b. Compare Discrete Cosine Transform and Hadamard transform [04]
SO-1 ; . . ;
> ~ sh)?
BL-4 (write 04 points for each)?
CO-3; | ¢.
SO-1; Compare Dilation and Erosion operation (write 04 points for each)? [04]
BL-4 P
CO-03; | d.
SO-01; Consider the following image matrix of size 7 * 7.
BL-05 [04]
L_

Page 1 of 6
--- page 2 ---
Oo} 0/}/0/10} 0}0+40 |
0} 0;]0 410} 0} 0] 0 :
0 | 07;]0{10} 0} 0) 0 vi,

10 | 10 | 10 | 10 | 10 | 10 | 0 ~

Oo} 0/0 ]10} 0] 04] 0

0 | 0/0 {10} 0} 01] 0

0 | 0 {10 {10} 0} 0] 0

Show the effect of horizontal and vertical line detector on image matrix.

CO:4; /|el , :
SO: 1, 6; For video signals, justify the use of Chroma Subsampling. [02]
BL: 5
CO:4; |e. 2.
» 6 Justify the need of motion estimation in video processing. [02]
5
Q2 a. Describe process to perform gray level slicing. Apply gray. level slicing
CO-1: without preserving background on the following 3 Bits Per Pixel image
SO-1; given below. Assume rj=2 and m=5. Size of image is 5 x 5.
BL-3
1 1. 1 1 2
6 6 6 6 1 [04]
4 4 4 1 1
3 3 3 3 3
1 1 1 1 1
CO-1; |b. Explain the concept of pixel neighbourhood in digital image processing.
-l: ‘
aoe , An image segment is shown below. Let, V be the set of gray level values
used to define connectivity in the image. Compute D4 (City block) and D8
(Chess Board) distances between pixels ‘p’ and ‘q’.
[08]
2 (p} 3 2 6 l
6 2 3 6 2
2 3 2 3 BS)
2 4 3 5 2
4 5 2 3 6 (q)
Page 2 of 6
--- page 3 ---
cewer

CO-2; Ic. Compute Discrete Cosine Transform of following 4 x 4 image.

SO-1 ; j
BL-3. 1 }]1 ]2 42 ,
1 fi [2/2 ty [08]
1 ]1 |2 |2
1 ]1 |2 |2
Q3 a. Formulate how the derivatives are obtained in edge detection. Compute first
CO-03; and second order derivative of intensity of pixels along line of grayscale
g gray
SO-01; : 04
BL-02 image. [04]
f(x) =[121350660]
CO-1; | b. Apply 3 x3 averaging filter and median filter on given image to remove salt
oe and pepper noise. Give statement on which is better filter to remove salt and
pepper noise. Size of image is 5 x 5.
2 2 {3 5 5
2 7 3 5 5 [08]
2 2 3 1 5
2 2 3 5 5
2 2, 3 5 5
CO-2 ; a. Calculate Walsh Transform of following 4 x 4 image.
a ; 2 [1 2 1
1/2 |3 4|2 ‘ [08]
2 13 J4 43
1 {2 |3 42
Q4 a.
CO- 4; ; : ,
' Compare the level of compression provided I, P and B frames of video.
SO-1, 6; [04]
BL-5 Justify your answer.
CO-1; | b. Apply histogram equalization on the following image, which has 8 discrete
Mee pixel levels (0-7). Justify importance of histogram equalization in image [08]
processing.

Page 3 of 6
--- page 4 ---
Size of image is 6 x 6.

CO-3; | c¢. Determine the Hit-or-Miss transformed image from the given image using
ake given structuring elements. Size of image A is 7 x 7.
0/0 ;0 /0 |0.;0 }0
Ol) y1 1 yr tt fo
O};1 }1 ]1 yi 41 40
O};1l yi Ji yl fl jo
O};1 fl {1 fi ]1 40 [08]
O};LiL }i yi fl jo
0/0 }0 |0 {0 |0 |0
A
i 1
I 0
Bl B2
Q5 a. For a video signal, consider the sequence of frames for the following
‘
CO-4; display order. Choose sequence of first four frames to show bit stream
il order to achieve compression
BL-6 _ P j [04]
| B B P B B P B B P B BOI
| 2 3 4 5 6 7 8 9 10 HN 12 3
CO-4; | b. , :
SO-1, 6; Explain 2D log search algorithm of motion estimation in detail. [08]
BL-2
Soon, G. Compute the global threshold for the image given below using Otsu’s
0-01;
BL-03 method. Also perform intensity thresholding on given image. Show all the

Page 4 of 6

aN
--- page 5 ---
steps for computing the threshold, expression of intensity thresholding and

the output image. Size of image is 6 x 5. ‘

Q6 a.
CO- 4; Define evaluation metrics used in motion estimation. What should be the
Soe ideal values of these metrics for accurate motion estimation? 4]
CO-03; | b. Consider a binary image of size 8 x 8 pixels that contains a square of 1’s
eke of size 4 x 4 pixels at its center. The rest of the pixels in this image are
background pixels labelled as 0’s. [08]
1. Use Sobel Operator to determine Gradient Vectors g, and gy.
2. Determine Magnitude and angle of gradient vector.
CO-3; | c¢. Modify the given image A (Any ONE from Binary version or shaded
ie version) in such a way that its boundary can be achieved. Use B as the
structuring element of 1’s of size 3 x 3 with central pixel represents pixel
under process. Also comment on the output image with respect to input
image. Size of image A is 10 x 5.
Pad image A using 0 (or using background pixel). 7
1] 1} 1) 0} 1) 1) 1) 1) 1) 0 : [08]

1} 1} 1) 0} 1) 1} 1) 1) 1)0

OR

Page 5 of 6
--- page 6 ---
——

7

an 4; * Differentiate between exhaustive search and 3 step ——_ algorithms of [04]

SO-1, 6; motion estimation giving 4 points of difference.

BL-3

CO-03; | b. Consider the following image matrix of size 8x 8.

SO-01;

BL-05 0 fo ]i]i [i fi fo fo ®
0;0 }1 }1 J1 41 40 }0
0 /0.;1 }1 {1 71 410 }0
0/0 |0.}1 71 {0 }0 J0
0/0 }0 }1 41 70/0 }0 [08]
0;0 {1 }1 ]1 41 10 JO
0;0 }1 /1 41 41 10 JO
0 ;0 }1 }1 4141 4/0 }0

Apply the Region Split and Merge Technique to segment the objects in the
given image. Also, show the quad tree representation.

CO-3; | c. Interpret the result of Dilation operation on given image using given

SO-1; structuring element. Size of image A is 10 x 10.

BL-5 0}0;0;/0/0/0}0/0/0)0
O;} 1} 1/1)/0}/0}0;0/0]0
ofifififoli{i]ififo ‘
Oy; LJ TJ 1} iyifryiyi1}o , i
O; 1/1) 1}0}1}1}1]}1]0
O;}1}1/1]/0};0}0;0/0]0
0}/0;0/0/0;/0}0j;0;0]0 [08]

A
0} 1/0
1} 1} 1
OL 1,0
B

Page 6 of 6
````

## 2023-24 · Re-Exam · Sem 5 · paper 6700ac255f37

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/IMAGE & VIDEO PROCESSING/Image and Video Processing, Sem-V, Batch 2023-24, Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 84.9

````text
MPSTME

LIBRARY

SVKM’S NMIMS ;
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2024-2025

Program: B.Tech/MBA.Tech Stream : Computer Engg /CS/EXTC Year: III/Semester: V/1X
. ® Tek Tot puter Engg /c¢/ ; ie
Subject: Image and Video Processing Time: 03 hrs (2 to 5 pm)
Date:_07/12/2024 No. of Pages: 05

Marks: 100

Re-Examination (Batch 2023-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use. i

1) Question No. _1___ is compulsory. + poy

2) Out of remaining questions, attempt any _4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.

Q.1 Attempt all questions 20
CO-1, SO- a | Calculate the Euclidean distance, city block distance and chessboard distance 04
1, BL-3 between two pixels located at (0, 4) and (6, 1).
CO-2, SO- | b | State the equations to compute Hadamard transform and inverse Hadamard 04
1, BL-3 transform. Compute the Hadamard transform of the following image:
o

2 3

1 2
CO-3, SO- | c | Explain erosion on binary images in brief. 04
1, BL-2
CO-4,SO- | d | Discuss the method of segmentation using thresholding. 04
1, BL-2
CO-5,SO- | e | Explain chroma subsampling of video in brief. List subsampling formats used 04
1, BL-2 for various applications.
Q.2
CO-1,SO- | a | Describe spatial resolution and gray level resolution, Discuss the effects of 10
1, BL-2 decreased spatial and gray level resolution on the appearance of the image.

Deliberate on the disadvantage of having increased resolution.

Page 1 of 5
--- page 2 ---
CO-2, SO-

Calculate the DCT of the given image, and the percentage of the fotal energy

10
1, BL-3 contained in the DC coefficient.
2 1 1 2
20 2 1 1
1 1 2 2
2 1 2 1
Q.3
CO-1, SO- Perform histogram equalization on the given 8x8 image. The gray level 10
1, BL-3 pe 2 oe! oe
distribution is given below:
Gray level | 0 1 2 3 4 5 6 7
No. of
. 18 | 10 | 43 2 2 3 14 12
pixels ;
Draw the original histogram and the equalized histogram.
CO-2, SO- Compute the forward and inverse Walsh transform of the given image. 10
1, BL-3
2 1 2 1
1 2 3 4 2
2 3 - 3
: 1 2 3 2
Q.4
CO-3, SO- State mathematical expression of morphological opening operation. Perform 10
1, BL-3

opening operation on the given image (A). Use structuring element SE1 for
erosion and SE2 for dilation. (Assume shaded regions have intensity 1 and

unshaded regions have intensity 0). State applications of opening operation.

Page 2 of 5
--- page 3 ---
SEY SE2

oad

CO-1,SO- | b | Draw low pass and high pass filter masks. Justify why the sum of the 10
1, Bet coefficients of a high pass filter should be zero. On the given image, apply 3x3
low pass and high pass filters to produce 3x3 output images.
50 | 50 | 50 | 50 | 50
200 | 200 | 200 | 200 | 200
200 | 200 | 200 | 200 | 200
200 | 200 | 200 | 200 | 200 :
: 50 | 50 | 50 | 50 | 50 |
Q.5
a al a | Apply appropriate masks of Sobel and Prewitt operators to detect edges in the 10
» BL-

given images (generate 4x4 output images). Compare the outputs and comment
on the performance of both operators.

Image |:

50 | 50 | 50 | 50 | 50 | 50
50 | 50 | 50 | 50 | 50 | 50
200 | 200 | 200 | 200 | 200 | 200
200 | 200 | 200 | 200 | 200 | 200
200 | 200 | 200 | 200 | 200 | 200
200 | 200 | 200 | 200 | 200 | 200

Page 3 of 5
--- page 4 ---
Image 2:

50 | 50 | SO | 200 | 200 | 200
50 | 50 | 50 | 200 | 200 | 200
50 | 50 | 50 | 200 | 200 | 200
50 | 50 | 50 | 200 | 200 | 200
50 | 50 | 50 | 200 | 200 | 200
50 | 50 | SO | 200 | 200 | 200

CO-5,SO- | b | Illustrate the 2D log search motion estimation algorithm and explain its 10
1, BL-3 .

working. we
Q.6 on
CO-4, SO- | a | On the given image (A), perform region growing using given seed pixels (seed 10
1, BL-3

pixels are underlined). Use 4-neighbourhood for growing regions. The

predicate is |f(seed)—f(pixel)| <3

8/7]/9]9]8])9]9 77 7157 15°
8 |7)9|]91819 191151141 14
8|/7]/9 | 918 ] 9 | 14] 145 [213 | 13
8 | 7/9 | 9 | 8 113 | 13 | 13 [14 7 14
8 | 7/9 | 9 | 14] 15 | 13 | 14] 15 | 13
8|/7]9]/9]15];15;o0]2]1 1) 0

8 1 O | 12} 12} 12] 0 | 2 1 0
1 O | 12}; 12) 12] 12] 2 1 0] 0
Image (A)

Page 40f5
--- page 5 ---
On the given image (B), perform region split and merge. Minimum ane
size during splitting is 1x1. The predicate is |f(seed)—f(pixel)| <3

8} 7}9}9 |} 9] 7 | 15 } 15

8) 7 | 9] 9 | 9 | 15 | 14 | 14

8 | 7 9 | 9 | 14] 15 | 13 | 13

8 | 7 | 9 | 9 | 13} 13 |} 14 | 14

8 | 7 | 9 1 1 2 1 0

8 | 7 1 0 1 2 1 0

8 1 0 12] 0 2 1 0

1 0 | 12) 12] 2 1 0 | 0

. Image (B)
CO-3, SO- | b | Describe boundary extraction in detail with an example. 10
1, BL-2
Q.7
CO-5, SO- a | Describe in detail I, P and B frames in a video. Illustrate how they can be 10
1, BL-4

arranged in a Group of Pictures.

CO-1,SO- | b | On the given image, perform contrast stretching using two location points (5,2) 10
1, BL-3
and (10, 13)

173])5]7)]9 10) 13) 15
1/3 )51719 111131 15
1/3 }s5{]7)911) 13] 15
7/3 }s51]71)9 10113115

Page 5 of 5
````

## 2023-24 · Re-Exam · Sem 8 · paper c2583990ddea

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC, B.TECH INTEGRATED / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/EXTC/Sem_08/IMAGE & VIDEO PROCESSING/Image and Video Processing Batch 2023-24 Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 86.8

````text
/

SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERI
SSIS UNIVE -

Academic Year: 2023-2024 Se

aw foe

Program: BTech / BTI Stream: CSBS / EXTC Year: 2095-24 Semester: VI/ XI
Subject: Image and Video Processing Time: 3 hrs (10.00am -1.00 pm)
Date:_29/6/24 No. of Pages: 05

Marks: 100 °

Re Examination
Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1_ is compulsory.

2) Out of remaining questions, attempt any _4_ questions.

3) In all_5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly:
Co- 1 a.
SO-1 Differentiate between sampling and quantization. [04]
BL-4 :
b.

Apply the following operations on the 4-bit, 5x5 image. Also write the mathematical
expression and draw the graph of the transformation function.
i. Thresholding with a suitable threshold to differentiate object from

background.
Co- 1 3 . .
_ 50-1 ii. Digital negative. [04]
4 BL-3 2 2 10 2 2
: 3 10 10 10 3
0 10 10 10 0
3 10 10 10 3
2 2 10 2 ]
CO- 3 : 1: ‘ :
0-1 Perform boundary extraction on the following image A, using structuring element [04]
BL- 3 Bi

1|Page
--- page 2 ---
t}1ijt
1}ij1
A B
CcO- 3 . . tee ee : . .
50-1 Discuss the importance of edge detection in image processing and its role in [04] |
BL-2 identifying significant features within an image.
CO- 4
SO-1 Write a note on 2D- log search method for motion estimation in video processing. [04]
BL- 2
Apply closing operation on the given input image A using the given structuring
element B. Size of the image is 8x8. Also give representation equation of closing
operation.
0 0 0 0 0 0 0 0
0 0 1 1 0 0 0 0
0 0 0 1 1 1 0 0
0 1 1 1 1 1 1 0
en 3 0 0 1 1 0 1 1 0
50-1 0 0 0 1 1 0 0 0 [10] -
BL-3 0 0 0 0 1 0 0 0

Input Image “A”

af
1
1

Structuring Element “B”

2|Page

\ _ ee
--- page 3 ---
i

b. | Apply histogram equalization on the given 15x10 image. Draw thg. original

Q2 histogram and the equalized histogram. The gray level distribution is given below:
Co- |
Gray levels | 0 1 2 3 4 5 6 7
50-1 y : [10]
No. 0
aa 60/40/20; 10 | s | 5} 5 | 5
pixels

a. | Apply Hadamard transform on both the given images. Analyze why the DC | [10]
coefficients of both images same even though both images are different and
comment on the nature of the images from their Hadamard coefficients.

Q3

CO-2 Image A Image B

SO- 1 1 1 2 2 1 2 1 2

BL- 4 1 1 2 2 1 2 1 2
1 1 r] 2 1 2 1 2
1 1 2 2 1 2 1 2

b. | Consider the given input image. Apply the following edge detection techniques on | [10]
the highlighted pixels of the image—
a) Vertical Sobel operator (3x3)
Q3 b) Horizontal Prewitt operator (3x3)
Pore o f[1 [o |2 {7

SO-1
. 2 ESE 0

ac co a6
mo OGe8

5 4 2 2, 5
a. | Calculate Dm distance, Euclidean distance and city block distance between | [5]

Q4 underlined pixels of the following image.
CO- | oor
SO-1 0 1 #0
BL-3 ~
0 oO 1
Q4 b [5]
Co- 1 . ; ae er .
S0-1 Justify the importance of gray level resolution in deciding image quality.
BL-5
Q4 c ais . . Lo. . . [10]
Co- Apply Dilation morphological operation on the given input image A, using the
50 given structuring element B. Size of the image is 9x9. Also list 4 uses of Dilation
BL- operation.

3|Page
--- page 4 ---
O;1;1};O0};1]} 1] 1fF1]0 9} 1) 0

Ofofol;ifofifolilo we LL
O;O;0;O0;0;O]O0];o]0 B
Input Image “A” Structuring Element
Q5 a. [10] as
CO- 4 Justify the importance of I frames and P frames in video compression with suitable
SO-1,6 diagrams.
BL-5
b. | Apply region splitting on the given image, considering the threshold value to be <=4 | [10]
and minimum split size 2x2. Draw the quad tree also.
6 7 7 7 8 8 7 7
Qs 7 8 7 8 6 6 5 8
CO-3 7 7 5 5 4 3 6 7
SO-1 6 5 6 5 3 4 5 7
BL-3 0 4 3 4 4 3 5 8
0 0 0 0 3 3 6 7
2 2 0 2 0 4 5 5
2 0 2 0 3 4 6 5
a. | On the given 4-bit, 7x5 image, apply contrast stretching using two location points | [10] (>
(rl,s1)=(6,3) and (r2,s2)=(10, 13).
“4 14} 3 | 12] 7 5 9 1
(r2, s2)
14); 3 | 12] 7 5 9 1
oo 1 i 144); 3 | 12} 7 5 9 1
SO- 1 s 144} 3 | 12] 7 5 9 1
BL-3

144) 3] 12} 7 3 9 1

(r1, 81)

4|Page
--- page 5 ---
om

Compute the DCT coefficients of the given image. Also find: a [10]
i. Energy of each coefficient -
ii. Total energy

Q6 iii. Percentage of total energy contained in DC coefficient
Co-2 Analyze why the first coefficient,is called the DC coefficient and has the highest
SO-1 value.
BL-4 0 3 2 1
1 0 3 2
2 1 0 3
3 2 1 0
Q7 [10]
CO- 3 Describe global thresholding and adaptive (local) thresholding in detail. Justify the
SO-1 need of adaptive thresholding by giving suitable example.
BL-2
Q7 [10]
CO- 4 Explain in detail the block-matching technique for motion estimation using suitable
SO-1,6 diagram.
BL-2

5|Page
````

## 2023-24 · Re-Exam · Sem 9 · paper 6d36fce86da9

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/5th YEAR/COMPUTER/SEM IX/Image and Video Processing/Image and Video Processing Batch 2023-24 Re Exam0001.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15/02/2025
- Text: ocr (5 pages), mean OCR confidence 88.4

````text
SVKM’S NMIMS on
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2024-2025

Program: B.Tech/MBA.Tech Stream : Computer Engg Year: uy Semester: VIX
; err ; cs /EXTC .

Subject: Image and Video Processing Time: 03 hrs (2 to 5 pm)

Date: 15/02/2025 No. of Pages: 05

Marks: 100

Re-Examination (Batch 2023-24)

‘> Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory. _

2) Out of remaining questions, attempt any 4 _ questions.

3) Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 Attempt all questions * 20
CO-1,SO- | a | Discuss adjacencies (connectivities) between pixels in an image with an 04
1, BL-3 example.
CO-2, SO- | b | State the equations to compute Walsh transform and inverse Walsh transform. 04
1, BL-3 Compute the Walsh transform of the following image:

4 4

1 1
CO-3, SO- | ¢ | Explain dilation on binary images in brief. 04
1, BL-2
CO-4,SO- | d | Discuss the method of segmentation using thresholding. 04
1, BL-2
CO-5,SO- | e | Define Sum of Absolute Differences (SAD). Discuss its importance in motion 04
1, BL-2 estimation.
Q.2
CO-1,SO- | a | Describe spatial resolution and gray level resolution. Discuss the effects of 10
1, BL-2 decreased spatial and gray level resolution on the appearance of the image.

Deliberate on the disadvantage of having increased resolution.

Page 1 of 5
--- page 2 ---
CO-2, SO- | b | Calculate the DCT of the given image, and the percentage of the total acre 10
1, BL-3 contained in the DC coefficient.

1 2 1 2

1 2 1 2

1 2 1 2

1 2 1 2
Q3
CO-1,SO- | a | Perform histogram equalization on the given image. The gray level 10
1, BL-3 Pe Se ts

distribution is given below:
Gray level | 0 1 2 3 4 5 6 7
No. of ;
: 0 | 0 | O | 200 | 200 | 300} 300 0
pixels .
Draw the original histogram and the equalized histogram.

CO-2,SO- | b | Compute the forward and inverse Hadamard transform of the given image. 10
1, BL-3

3 4 1 2

3 4 1 2

1 2 3 4

1 2 3 4
Q4
CO-3,SO- | a | State mathematical expression of morphological closing operation. Perform 10
1, BL-3

closing operation on the given image (A) using structuring element SE1.
(Assume shaded regions have intensity 1 and unshaded regions have intensity

0). Conclude as to what effect closing operation had on the image.

Page 2 of 5

aN
--- page 3 ---
Image (A)

oy

SE1

CO-1, SO- | b | On the given image, apply 3x3 low pass and median filters to produce 3x5 10
bal’ output images. Compare the outputs and conclude as to which filter was better
at removing the noise. Justify your answer.

100 | 100 | 100 | 100 | 100) 100 | 100

100 | 100 | 250} 100 | 10 | 100 | 100

100 | 100 | 100 | 250 | 100 | 100 | 100

100 | 10 | 100} 100 | 100} 10 | 100

100 | 100 | 100 | 100 | 100 | 100 | 100

Q.5

CO-4, SO- | a | Apply appropriate masks of Sobel and Prewitt operators to detect edges in the 10
1, BL-3 :. § .

given images (generate 4x4 output images). Compare the outputs and comment
on the performance of both operators.

Image 1:

Page 3 of 5
--- page 4 ---
10] 10] 10] 10 | 10] 10 ve
10 | 10 | 10 | 10 | 10 | 10
10 | 10 | 10 | 10 | 10 | 10
250 | 250 | 250 | 250 | 250 | 250
250 | 250 | 250 | 250 | 250 | 250
250 | 250 | 250 | 250 | 250 | 250

Image 2:

10 | 10 | 10 | 250 | 250 | 250
10 | 10 | 10 | 250 | 250 | 250
10 | 10 | 10 | 250 | 250 | 250
10 | 10 | 10: | 250 | 250 | 250
10 | 10 | 40 | 250 | 250 | 250
10 | 10 | 10 | 250 | 250 | 250

CO-5, SO-

b | Illustrate the 3-step search motion estimation algorithm and explain its 10
1, BL-3 .
working.
Q.6
CO-4, SO- | a | On the given image (A), perform region growing using given seed pixels (seed 10
1, BL-3

pixels are underlined). Use 4-neighbourhood for growing regions. The

predicate is |f(seed)—f(pixel)| <3

1 2 1 2 3 1 2 3 1 2

1 2 1. 2 3 1 2 ) 1 2

1 2 as 2 3 7 8 8 8 7

iL, 14 14 14 3 1 7 9 7 2
1 | 13 | 13 | 13 | 3 1 2/7 1 2
1 | 15} 15/15 | 3 1 7 9 7 | 2
1 | 14] 14] 14} 3 7 8 8 8 7
1 2 | 13 | 2 | 3 1 2 | 3 1 2
1 2 1 2 | 3 1 2 | 3 1 2
1 2 1 2 | 3 1 2 | 3 1 2
Image (A)

Page 4 of 5
--- page 5 ---
On the given image (B), perform region split and merge. Minimum sub-image

size during splitting is 1x1. The predicate is |f(seed)—f(pixel)| <3

2 1 2 3 ul 2 3 1

a 15 | 2. 3 7 8 8 8

14 | 14] 14 3 1 7 9 7

13] 13/13 | 3 | 1] 24)7 4 1
15 | 15,45 | 3 1 7 9 7
14 | 14} 14 |] 3 7 8 8 8
2 13 | 2 3 1 2 3 1
2 1 2 3 1 2 3 1

Image (B)
CO-3, SO- | b | Describe thinning operation in detail with an example. 10
1, BL-2
Q.7
CO-5, SO- a | Describe in detail I, P and B frames in a video. Illustrate how they can be 10
LBL arranged in a Group of Pictures.
CO-1,SO- | b | Write the mathematical equations and draw graphs 6f grey level slicing with 10
1, BL-3

and without background.
Compute the image pixel values after applying grey level slicing with
background and without background on pixels having intensity between 5 and

10 (both inclusive).

5 4 3 2 1
0 1 2 3 4
15 14 13 12 11
6 7 8 9 10
4 3 a 1 0

Compute the digital negative of the given image.

Page 5 of 5
````

## 2023-24 · Re-Exam · Sem 5 · paper 67a4d903cb9b

- Departments: Computer Engineering
- Programmes: MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/MBA TECH/3RD YEAR/Computer/SEM V/Image and Video Processing/Image and Video Processing , Re-exam 2023-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15/02/2025
- Text: ocr (6 pages), mean OCR confidence 86.0

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGIN EERING
Academic Year: 2024-2025

Program: B.Tech/MBA.Tech Stream : Computer Engg Year: uy Semester: VWAIK
: err : cs /ExTe

Subject: Image and Video Processing Time: 03 hrs (2 to 5 pm)

Date: 15/02/2025 No. of Pages: 05

Marks: 100

Re-Examination (Batch 2023-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 Attempt all questions 20
CO-1, SO- | a | Discuss adjacencies (connectivities) between pixels in an image with an 04
1, BL-3 example.
CO-2, SO- b | State the equations to compute Walsh transform and inverse Walsh transform. 04
1, BL-3 Compute the Walsh transform of the following image:

474

1 1
CO-3, SO- | ¢ | Explain dilation on binary images in brief. 04
1, BL-2
CO-4, SO- | d | Discuss the method of segmentation using thresholding. 04
1, BL-2
CO-5,SO- | e | Define Sum of Absolute Differences (SAD). Discuss its importance in motion 04
1, BL-2 estimation.
Q.2
CO-1,SO- | a | Describe spatial resolution and gray level resolution. Discuss the effects of 10
1, BL-2 decreased spatial and gray level resolution on the appearance of the image.

Deliberate on the disadvantage of having increased resolution.

Page lof5
--- page 2 ---
10

CO-2, SO- | b | Calculate the DCT of the given image, and the percentage of the total energy
1, BL-3 contained in the DC coefficient.
1 D 1 2
1 2 1 2:
1 2 1 2)
1 2 1 2,
Q3
CO-1, SO- | a | Perform histogram equalization on the given image. The gray level 10
ay distribution is given below:
Gray level | 0 2 3 4 § 6 7
No. of
ae 0 | 0.} 0 | 200 | 200 | 300 | 300 0
pixels
Draw the original histogram and the equalized histogram.
CO-2,S0- | b | Compute the forward and inverse Hadamard transform of the given image. 10
1, BL-3
3 4 1 2
3 4 1 2
1 2 3 4
1 2 3 4
Q4
CO-3, SO- | a | State mathematical expression of morphological closing operation. Perform 10
1, BL-3

closing operation on the given image (A) using structuring element SE1.
(Assume shaded regions have intensity 1 and unshaded regions have intensity

0). Conclude as to what effect closing operation had on the image.

Page 2 of 5
--- page 3 ---
Image (A)

bed
SEl
CO-1,SO- | b | On the given image, apply 3x3 low pass and median filters to produce 3x5 10
nlitet output images. Compare the outputs and conclude as to which filter was better
at removing the noise. Justify your answer.

100 | 100 | 100 | 100 | 100 | 100 | 100

100 | 100 | 250 | 100] 10 | 100 | 100

100 | 100 | 100 | 250 | 100 | 100 | 100

100 | 10 | 100} 100} 100} 10 | 100

100 | 100 | 100 | 100 | 100 | 100 | 100
Q.5
CO-4, SO- | a | Apply appropriate masks of Sobel and Prewitt operators to detect edges in the 10
1, BL-3

given images (generate 4x4 output images). Compare the outputs and comment
on the performance of both operators.

Image 1:

Page 3 of 5
--- page 4 ---
LOS PLOF S10" | 10F 1.075) 10
10 | 10 | 10 | 10 |] 10 | 10
10 | 10 | 10 | 10) 10 | 10
250 | 250 | 250 | 250 | 250 | 250
250 | 250 | 250 | 250 | 250 | 250
250 | 250 | 250 | 250 | 250 | 250

Image 2:
10 | 10 | 10 | 250 | 250 | 250
LOM) 10) FLO) 25031250!) 250
10 | 10 | 10 | 250} 250 | 250
10 | 10 | 10 | 250 | 250 | 250
10 | 10 | 10 | 250 | 250 | 250
10 | 10 | 10 | 250 | 250 | 250
CO-5,SO- | b | Illustrate the 3-step search motion estimation algorithm and explain its 10
ee working.
Q6

CO-4,SO- | a | On the given image (A), perform region growing using given seed pixels (seed 10
tere pixels are underlined). Use 4-neighbourhood for growing regions. The
predicate is |f(seed)—f(pixel)| <3

1 2 1 2 3) 1 2 3 1 2

il 2 1 2 3 a 2 3 1 2
oT 2 a5 Z 3) 7 8 8 8 i

1 | TA TAe | aa se 7 Oe 7 | 22

ease SSG Se al ee pe tele

ee |e et5e |S sl oS, 1 TEMES) 7 2,

epee] esa | |RSS ED 7 8 aR Srey 87

1 2 || ats} fez. 3 1 2 3 1 2

mS She sae | Sehr ke

1 2 1 2 e) 1 2. 3 1 2
Image (A)

Page 40f5
--- page 5 ---
On the given image (B), perform region split and merge. Minimum sub-image
size during splitting is 1x1. The predicate is \f(seed)—-f(pixel)| <3
2 1 Z 3 1 2 3 1

2p ss aay aes

14 | 14] 14] 3 1 7 ) 7

yp ces] a) | SS Sih 4G Sea
15S 15e |e 1S 3 1 7 9 7
144) 14/ 14/3/71 8 8 8
2 ee ae 3 1 2} B 1
y 1 2 3 1 2 3 1

Image (B)
CO-3, SO- | b | Describe thinning operation in detail with an example. 10
1, BL-2
Q7
CO-5, SO- a | Describe in detail I, P and B frames in a video. Illustrate how they can be 10
Sas arranged in a Group of Pictures.
CO-1,SO- | b | Write the mathematical equations and draw graphs of grey level slicing with 10
1, BL-3

and without background.

Compute the image pixel values after applying grey level slicing with

background and without background on pixels having intensity between 5 and
10 (both inclusive).

5 4 3 2 1
0 1 2 3 4
15 14 13 12 11
6 7 8 9 10
4 3 2 1 0

Compute the digital negative of the given image.

Page 5 of 5
--- page 6 ---

````

## 2022-23 · Final-Exam · Sem 5 · paper c336bad522f6

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/IMAGE & VIDEO PROCESSING/Image & Video Processing, 3rd Year, Sem V, Year 2022-23, Final Exam.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 15 December 2022
- Text: ocr (5 pages), mean OCR confidence 87.8

````text
/ SVKM’s NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT &
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGIN.

Academic Year: 2022-23
Programme: B. Tech /MBA Tech (Computer) Year: II

Subject: Image and Video Processing
Marks: 100 .

Date: 15 December 2022 Time: 10.30 am - 1.30 pm
Durations: 3 (Hrs)
No. of Pages: 5

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

~~. 2) Out of remaining questions, attempt any __4 _ questions.
3)Inall___5_ questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi

Answer in brief

a. Consider a video with rate, 25 frames per second. Each frame of the video is an 8-

CO- 4; SO-1 bit color image of 200 rows and 200 columns. Compute the memory (in bits)

BL-5 required to store the video of 1 second. If each frame of the video is converted to

5]

4-bit image, find the amount of memory saved for storing this video?

b. | Discrete Cosine Transform (DCT) coefficients of two images are given below.
Compute total energy of DCT coefficients for each image. For which of the

following images, DCT is more effective in compression? Justify your answer.

oe So-1 DCT coefficients of image 1 DCT coefficients of image 2 [5]
10 | 2 1 1 10 |9 8 6
2 |3 1 1 8 9 8 6
2 1 0 1 8 8 8 i
1 |2 10 |0 6 6 1 i
--- page 2 ---
A binary image is shown below. Diameters of circular objects are 3, 7 and 11
pixels. Sizes of square objects are 7x7, 11x11 and 15x15 pixels. Which
morphological operation should be used to eliminate all the objects except the
largest square? What should be the size, shape and intensity of structuring element?

CO-3; SO- 1 Show image before and after morphological operation showing size of each object. [5]
BL-2

” A 3x3 median filter is used to filter an 8-bit image matrix shown below. Show
filtered image matrix. Explain application of median filter using this example.
CO-1; SO-1 100 | 100 | 100 | 100 ; 5]
BL-2 100 | 255 100 | 100
100 100 |5 100
100 100 100 | 100
Q2 a. | Explain the use of motion vector for block matching in video compression. Also
CO-4; $O-1 explain how Sum of Absolute Difference (SAD) is used to determine the motion [10]
BL-2 vector. Use example frames for explaining the same.
Q b Compare I, P and B frames of video and show how these frames are utilized for
one SO-1 video compression. mt
Q3 a Explain two dimensional logarithmic search method for block searching between 110]
See SO-1 two video frames
b An 8-bit 4x4 image has two horizontal bars. First bar is of size 1x4 with pixels of [10]
intensity 10. Second bar has size of 3x4 with intensity 20.
Q3 i) Determine Hadamard Transform of image
Le SO-1 ii) Retain top four coefficients (first two rows and two columns) of the result

in (i) and convert remaining coefficients to zero. Determine inverse
Hadamard Transform of these modified coefficients.

iii) Why is original image different from the result in (ii)?

2/s-
--- page 3 ---
a Consider the following image matrix. [10]
80 | 80 | 40 | 40 | 40
80 | 80 | 40 | 40 | 40
80 | 80 | 40 | 40 | 40
80 | 80 | 40 | 40 | 40

Q4 80 | 80 | 40 | 40 | 40
CO-2; SO-1 Image
BL-5

Apply the following filters on the given image.
i) Laplacian filter of size 3x3
ii) Average filters of size 3x3
iii) Average filters of size 5x5
Comment on the above results showing applications of Laplacian filter and

average filter of both the sizes.

b A 3-bit image is shown below: [10]
2 |2 42 1 1 1
5 |0 {0 |6 |2 {0
3 3 3 13 3 13
6 |6 |}6 |0 |4 {4
0 {5 {2 |5 |4 [5
7 (7 17 |5 [7 [5

Q4 @ Improve contrast of the image using local histogram equalization of
CO-1; SO-1 subimages, each of size 3x6. Show histogram of each subimage
BL-6 before and after equalization

(ii) Improve contrast of the entire image using histogram equalization.
Show histogram of images before and after equalization

(iii) . Discuss the need of local histogram equalization
--- page 4 ---
Consider the following image and structuring element.

a [10]
Q5
CO-3; SO-1
BL-4
Image
Structuring Blentent, SE
(i) Show and explain the effect of dilation using given Structuring Element
(ii) Show and explain the effects of erosion followed by dilation using given
Structuring Element
(iii) Compare the results of (i) and (ii).
b Consider two images represented by the following image matrices: [10]
20 |20 |20 | 20 10 | 10 | 100 | 100
20 20 20 20 10 10 100 | 100
60 |60 | 60 | 60 10 | 10 | 100 | 100
Q5 60 |60 |60 |60 / 10 | 10 | 100 | 100
CO-4; SO-1 Image, A Image, B
BL-4 For both the images,

i) Use Sobel operator to determine gradient vectors, gx and gy
ii) Determine magnitude and angle of gradient vector

iii) Interpret the direction of edges

iv), Identify the image which has stronger edge?

als
--- page 5 ---
a Consider the following image and a structuring element [10]
Image Structuring element
a 2
06 real L : a , S|
CO-3; SO-1 be aes
Biss (i) Erode image by structuring element and subtract eroded image from the
original image. Explain each step in details. Prove that this process
detects the boundary of object.
(ii) Given image and structuring elements are modified by changing white to
dark and dark to white pixels. Repeat steps in (i) for this image and
structuring element.
wo . Justify the need of edge linking after detection of the edges in an image. Explain [10]
oe = the steps involved in edge linking algorithm using examples.
Q7 a Explain the following methods of segmentation with examples: [10]
CO-3; SO-1 i) Thresholding based on histogram of image with and without noise.
BL-5 ii) Region growing
b Consider the following image matrix. : [10]
50 | 60 | 75 | 70 | 68 | 68 | 68 | 68
60 | 60 | 74 | 70 | 64 | 64 | 64 | 64
80 | 80 | 80 | 80 | 64 | 64 | 64 | 64
80 | 80 | 75 | 75 | 68 | 68 | 68 | 68
84 | 84 | 75 | 75 | 70 | 70 -) 70 | 70
Q7 84 | 84 | 75 | 75 | 70 | 70 | 70 | 70
ea 30 [80 |75 [75 | 70 [70 | 90 | 90

80 | 80 | 75 | 75 | 90 | 90 | 80 | 80

Demonstrate region merge technique to segment the objects of the given image.
The difference between the two consecutive pixels should be <= 5.

(i) Minimum size 2x2.

(ii) Repeat the same for minimum size of 4x4

“Gii) Comment on the results in (i) and (ii)

fs
````

## 2022-23 · Final-Exam · Sem 5 · paper 2ebda32d4788

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/IMAGE & VIDEO PROCESSING/Image and Video Processing, 3rd Year, Sem V, Year 2022-23, Final Exam_2ebda32d47.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 17 November 2022
- Text: ocr (4 pages), mean OCR confidence 86.2

````text
SVKM’s NMIMS (
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING.

%
S

Academic Year: 2022-23

Programme: B. Tech /MBA Tech (Computer) Year: Ill Semester: V
Subject: Image and Video Processing

; . Marks: 100
Date: 17 November 2022 - Time: 10.00 am - 1.00 pm _

Durations: 3 (Hrs)

No. of Pages: _O%.

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi Answer briefly: [20]
CO1;SO01; a. | Assume that a gray scale image of resolution 1280 x 720 is to be sent to a mobile device with [02]
BL-1 resolution 640 x 360. Which technique should be used for the same? Explain in brief.
b. | Intensity of pixels along a line of a gray scale image is as given below. Write the expression
7 °° 1; and compute the first order and second order derivative for these pixels. [02]
; f(x) = [231007713]
— ¢. | State whether it is true or false. DCT provides energy compactness. Justify. [02]
d. | Why is erosion used in image processing? The given original binary image is eroded by a
1 x 3 structuring element. Draw the structuring element to get the eroded image shown below.
C03; SO1; [02]
BL-2,3
Original binary Image Eroded Image
conse 13) e. Explain in brief Chroma subsampling. [02]
cons >| £ | List two differences between Wavelet transform and Fourier transform. [02]
g. | The least significant bit of each pixel of the 3-bit image given below is replaced with 0. Draw
the resultant image. Also, draw the histogram of the original and the resultant image.
CO1;SO1; 0 1 2 3 [02]
BL-3,4 4 5 6 7

Image

yy
--- page 2 ---
h.

CO1:SO1: Two pixel values of an image are given as 0 and 1000. What is the resultant value after applying [02]
BL-3 log transformation to the two pixels? Assume constant c=1. Comment on the results obtained.
oe ; SO1;| i. | Write the expression to extract the skeleton of a binary image. [02]
co3;so1:| + List the two conditions for linking an edge pixel with coordinates (s, t ) to another edge pixel [02]
BL-1 at coordinate (x, y).
Perform the following operations on the 4-bit image shown below.
1. Contrast stretching using the transformation characteristics given below.
2. Histogram equalization of the image.
Comment on the effect of each. ‘
S4
Q2 a. [2 [3 ]7 10)
CO2; SO1; 11 | 14 | 6 9 [
BL-3 4 7 3 2
0 7 10 | 7
Image
£
(0,0) 5 10 15
Transformation characteristics
Draw the block diagram and explain the process of spatial sampling and quantization to digitize
an analog image. What is the resultant output image if the gray scale image given below is
down sampled by a factor of 2? Further at the receiver, the down-sampled image is up-sampled
by factor of 2 by averaging. Write the resultant up-sampled image.
Q2 b.
CO1;SO1; 5/2/3 ]1 [10]
BL-2
4/1/)6/4
310/915
217)8]2
Image
Q3 Explain the following:
C04; $01 ; (i) I, B and P frames in a video sequence. [10]
BL-1 (ii) Sequence of frames in display order and bit stream order.

(ii) 1 frame require maximum memory and B frame require minimum memory.

2%

—
--- page 3 ---
Write the expression for thinning morphological operation. Generate the structuring element
B2 from the structuring element B1 given below. Perform thinning operation on the binary

image given below using B1 and B2.

Pyifyiyuyiryryirydyl

Q3
| b. 0 0
CO3 ; SO1; ° 1fof}ojoj{ijifajfaqa [10]
BL-3
x | 1] x rfo}ijo};ijojojoj1
1 1 1 1Jiljr}ry ry) oy 1y;oryd
Structuring element (B1) rlidatadadayadyadi
Image
Consider the 4-bit image given below. Perform region growing with seed pixel value of 6,
which is highlighted in the image. Predicate is that the difference between two consecutive
pixels is <3.
Q4 8 | 11] 12] 7-} 10} 9 | 15] 0
12/15/6}|5 | 6 {2 | 1 {10
_ ; 10
COs; $01; 1)4}s17)]4)]10| 5 {15 aa
BL-3 a.
10} 15] 8 | 6 | 5] 1 1 | 6
10} 15} 5] 4 ]5 41 415] 5
0o}/4/6;]5}]6)]4 {| 0 | 13
o{i1} 5 | 4 | 4 | 14] 104 15
4 }10] 9 5 12] 0 0 4
For the grey scale image segment shown below apply 3 = 3 mask for the following operation
and show the resultant image.
1. Averaging filter
2. Weighted averaging filter
4 3. Median filter
Q 4, Laplacian filter
C02, $01; 10 [20 [30 [40 Hol
40 [30 | 20 | 10
b. 10 | 20 | 30 | 40
40 | 30 | 20 | 10
Image
Also, comment on the results. Ignore rows and columns at the extreme edges of the image
while performing the operations.
Apply Prewitt gradient operators to find horizontal and vertical edges in the given image. Also,
q, | find the magnitude of gradient vector. Show all the steps and the final image matrix. Use zero
padding at the extreme edges while performing the operation.
Q5
5 | 10 | 10
CO3;SO1; | . [10]
BL-3 . 5 10 | 10
5 10 | 10
Image

3fy
--- page 4 ---
Q5 b. | Write the expression and explain the following morphological operations with examples on
binary image clearly stating the background and the foreground pixels.

. . [10
ae (Erosion :
> (ii) Opening
Compute the global threshold for the image given below and perform intensity thresholding
without background. Show all the steps for computing the threshold, expression of intensity
thresholding and the output image. Also, explain how would you improve the quality of the
segmented image if the input image is captured with non-uniform illumination.
Q6 O71; 2),3 1744
CO3; SO1; 5/O}1]/2]3]7 [10]
BL-3,4 a

6;/5]0]1]2]3

7)/6)5]0]142

1);7)6})5]0]71

Image

Q6 What is motion estimation for video signal? Explain block-matching method of motion
CO4;SO1;] b. | estimation: Also, explain the effect of selecting large and small block size on motion [10]
BL-2 estimation.

Q7 a. | Draw the block diagram of subband coding for multiresolution analysis of an image. List the
CO2; SO1; subbands and the details of the image provided by each subband. [10]
BL-2

Let F(u, v) shown below be the Discrete Cosine Transform of an image segment where, w is
the row and v is the column. Compute the energy of each of the coefficients and the total energy
of the transformed image segment.

Suppose image is compressed by retaining some of the coefficients in F(u,v). Find the
Q7 coefficients, which should be retained in order to preserve:

C02; $01; | b. (86 % of energy [10]
(ii) 87.5 % of total energy

BL-4 (iii) 94 % of the total energy
Show all the computations.
° 5 0.19 —0.5 —0.46
—| 046 -—0.35 —0.73 0.35
FUVM=! 95 -084 00 0.73
0.19 0.35 0.84 —0.35

‘4
````

## 2022-23 · Re-Exam · Sem 5 · paper d869d6ebef43

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/IMAGE & VIDEO PROCESSING/Image and Video Processing, 3rd Year, Sem-V, Year 2022-23, Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 January 2023
- Text: ocr (5 pages), mean OCR confidence 88.3

````text
rd SVKM’'S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING /
SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING

Program: B. Tech /MBA Tech (Computer) Year: III Semester : V

AcademicY ear: 2022-2023

Subject: Image and Video Processing Marks: 100
arks:

Date : 27 January 2023 Time: 10.00 am - 1.00 pm
Durations: 3 (Hrs)

No. of Pages:_95
Re-Examination (2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer in brief
a. An image matrix of a 4-bit grey image is given below:
8/5 |5 |5 |7
5.18 [5 |7 [5
5.{5 [8 |5 [5
on 1. 5 |7 [5 |8 {5 [5]
oe)
BL-3 7 {5 [5 [5 [8

i) Highlight pixels with white in the intensity range 40% to 60% of the
om maximum possible intensity. Intensity of remaining pixels should be black
ii) Identify the type (horizontal/vertical/diagonal) segmented lines

b.
Compute Hadamard transform of the following image matrix. Comment on the
energy of transformed image
CO-2 ;
SO-1; 10 | 10 | 10 | 10 [5]
BL-3 10 | 10 | 10 | 10

10 | 10 | 10 | 10
10 | 10 | 10 | 10
--- page 2 ---
Apply dilation operation on the following binary image. Choose black 3x3
structuring element. Justify the change in the given image after dilation.

CO-3;
SO- 1; [5]
BL-2
C64 d. Why are I frames required for video compression? Justify that P frames provide
SO- a more compression than I frames and less compression than B frames. Also justify [5]
BL-1 that B frames are least reliable.
a, : Justify the following
Q i) Image smoothing is done before applying edge detection algorithm.
CO-1,2; “~« Show images at each step. ; [10]
SO-1; ii) DCT transform is used for image compression. Assume a DCT
BL-5 transformed image matrix and show how compression can be done.
Q b. Explain Three Step Search for block matching in video processing.
CO-4; [10]
SO-1;
BL-2
a In relation to video signal, explain the following terms:
i) Temporal sampling interval or frame time
ii) Number of lines/frame
Q3 ey we
iii) Line rate
CO-4; . . . [10]
SO-1; iv) Number of pixels/line
BL-6 v) Frame rate in bits/sec
If each of the terms is increased discuss the effect on quality of video. Also discuss
the effect if each of the terms is reduced.
b {10}
Q3
CO-2; List the limitations of Short Time Fourier Transform for small and large
page windows? How Wavelet Transform is used to avoid these limitations.

2/5
--- page 3 ---
a Consider the following image matrices.

20 | 20 | 40 | 40 | 40 20 | 20 | 20 | 20
20 | 20 | 40 | 40 | 40 20 | 20 | 20 | 20
20 | 20 | 40 | 40 | 40 40 | 40 | 40 | 40
20 | 20 | 40 | 40 | 40 40 | 40 | 40 | 40
Q4 20 |20 | 40 | 40 | 40 40 | 40 | 40 | 40
CO-3; Image 1 Image2 {10}
SO-1; 40 | 40. | 40 | 20
BL-
ine 20 | 40 | 20 | 40
40 | 20 | 40} 40
> 20 | 40 | 20 | 40
Image 3
Apply suitable filters to detect horizontal, vertical and diagonal edges.
Which of the edges are found in each of the given images?
b Determine histogram equalization of the following 3-bit image. Show: [10]
i) Equalized image matrix
Q4 ii) Histogram before and after equalization
CO-1; 4 4 4 4 4
SO-1; 3 3 5 5 k
BL-5 3 3 5 5 3
3 3 5 5 3
4 4 4 4 0
a [10]
Q5
m CO-4: For video processing, compare the effects of large and small block sizes used for
SO-1; motion estimation. Explain the above with examples of video frames.
BL-5

3/5
--- page 4 ---
Consider the following 4-bit image matrix and image transformation matrix:

2 3 8 8
4 5 10 | 10
4 5 8 8
7 7 8 8

{10]

Q5
CO-4;
SO-1;
BL-5
0 3 8 15
Transformation Matrix
i) Apply the given transformation function on the image. _
ii) | Draw histogram of image before and after transformation
iii) __ Compare contrast of image before and after transformation
Apply Hit or Miss Transform to detect square A in the following image. Discuss [10]
each step in details. Show images at each intermediate step.
Q6
CO-3;
SO-1;
BL-3
Explain erosion? Erode the given binary image using each of the given [10]
structuring elements.
Q6
CO-3;
SO-1;
BL-3

Image Structuring Elements

5
--- page 5 ---
i Qi a Show how magnitude and direction of gradient (first order derivative) are used [10]

CO-1; for the detection of isolated points and edges. Explain it with example of an

SO-1; . : :
BL-1 image with horizontal edge.
b [10]

For the given image, apply segmentation by region growing. Choose seed points at
(2,2) and (5,5), where row and column numbers start from 0. Condition is that the
difference between pixels should be less than 5.
Justify the use of multiple seeds for segmentation. Show how two seeds are useful
for the given image

Q7

CO-3; 20 [13 [13 [11 [60 |70 |50 |20

SO-1; 20 | 12 12 12 60 70 50 20

BL-5 12 | 12 15 11 60 70 50 20

20 | 12 12 12 20 70 50 20
20 | 30 ll ll 23 24 20 20
20 | 30 40 21 23 24 24 23
20 | 30 40 50 23 24 22 23
20 | 30 40 50 50 24 24 23

. a

5/8
````

## 2022-23 · Re-Exam · Sem 5 · paper 763df7bff41d

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/V SEMESTER/IMAGE & VIDEO PROCESSING/Image and Video Processing, Sem-V, Year 2022-23, Special Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 88.3

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENG
Academic Year: 2022-2023

Program: B. Tech/ MBA Tech (Computer) ; Year: II] Semester: V

Subject: Image and Video Processing Time: 03 Hrs. @1:00amto 2:00 pm)
Date:_12 /06 / 2023 No. of Pages: 04

Marks: 100

Special Re- Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1_ is compulsory.
2) Out-of remaining questions, attempt any __4__ questions.
3) In all_5_ questions to be attempted.

4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
1
Q Answer briefly:
a. What is gray level slicing? Perform gray level slicing with background and
without background on following image with r1=6 and r2=10.
Cco-01; zZ 10 |10 |3 9
SO-01; 5 2 7 6 15 [05]
BL-03 0 0 5 5 13
12 |1 7 6 13
1 5 3 14 | 13
j™ b. Give the Hadamard transformation matrix of 4 X 4. Compute the Walsh
. transform of the following image.
CO-02; 2 4 4 2
SO-01; a le 18 13 [05]
BL-06
2 8 10 |4
3 8 6 2
case; || © Explai ith ample bound tracti sing morphological
xplain with an example boundary extraction usin
50-01; p p y g p 8 [05]
operations.
BL-02
CcO-04; d. ;
SO-01; Write a note on Chroma subsampling. [05]
BL-01

Page 1 of 4
--- page 2 ---
| Perform histogram equalization and draw new equalized histogram of the
Q2 following gray level distribution “
CO-01;
mers en 0 | 1 |2 |3 |4 [5 6 |7 [10]
BL-03 levels
No. of | 550 | 900 | 650 | 150 | 300 | 250 | 110 90
Pixels
Q2 ae ; , ;
c0-02: ; What are the limitations of Short Time Fourier Transform in analyzing non-
50-01; stationary signal? How wavelets are useful in analyzing non-stationary [10]
BL-02 signals?
Q3 4 . ; . : F
c0-03: List different Region-based image segmentation techniques. Discuss
50-01; Region growing and Region Merging techniques of image segmentation [10]
BL-03 with example.
Q3.
CO-04; Explain New Three Step Search algorithm for block matching in video [10]
SO-01; processing.
BL-02
Consider the following image segment,
Fao [40 |40 |40 | 40
40 |40 |40 |40 | 40
80 80 80 80 80
go |60 |80 |80 | 80
Q4 [go [80 |so [80 |80 |
oon Apply 3 X 3 mask for the following operations and show the resultant | [10]

images for each operation.

BL-03 1. Averaging filter
2. Weighted averaging filter
3. Median filter
4. High pass filter
Also, comment on the results. Ignore rows and columns at the extreme
edges of the image while performing the operations.
0.03; b. Explain following morphological operations with example
50-01: 1. Opening [10]
2. Closing
BL-03

Page 2 of 4
--- page 3 ---
Give 3 X 3 masks for the following edge extraction operators

1. Sobel
2. Prewitt
Q5 Use these masks on following image and show the resultant image, ignore
CO-03; the border pixel. (10)
SO-01; 20 20 | 45 45 45
BL-03 20 20 45 45 45
20 20 45 45 45
20 20 45 45 45
20 20 45 45 45
QS
C 20-04; Explain the significance of | frames, P frames and B frames in block [10]
SO-01; matching and random access of video signals.
BL-02
Explain the process of Sampling and Quantization with neat sketch. Apply. | [10]
the process of down sampling by factor of 2 on the image given below. Also
Q6 at receiver, the down sampled image is up sampled by factor of 2 by
CO-01; replication.
50-01: [7 | 3 {9 |
BL-03 5 4 3 2
6 8 10 12
Z 7 8 2
| Find discrete cosine transform of the following image, [05]
6 0.02 |_° ; ° .
, 3 1 2 1
= apes
1 ll 2 iL |
06 Compute the memory (in bits) required to store the video signal of 30 | [05]
CO-04: seconds, with frame rate 30 frames per second. Each frame of video is an
a 8-bit monochrome image of 256 rows and 256 columns. If each frame of
BL-05 the video is converted to 4-bit image, find the amount of storage space
saved for storing this video.
Q7 [10]
CO-03; . . .
50-01: Explain the morphological thinning operation with suitable example.
BL-03

Page 3 of 4
--- page 4 ---
Q7
CO-03;
SO-01;
BL-05

Explain the process of ségmentation using Thresholding. Also, explain the
limitation of global thresholding and how local thresholding is used to
overcome limitation of global thresholding.

[10]

Page 4 of 4

aan
````

## 2021-22 · Final-Exam · Sem 6 · paper 3c8c3d490e51

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/EXTC/VI SEMESTER/IMAGE AND VIDEO PROCESSING/B Tech, EXTC, Image and Video Processing, 3rd Year, Sem-VI, Final Exam, Year 2021-22 (2).pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 16 April 2022
- Text: ocr (4 pages), mean OCR confidence 90.0

````text
sae

SVKM’s NMIMS :
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING /

SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Academic Year: 2021-22

Programme: B. Tech (EXTC) Year: III Semester: VI

Subject: Image and Video Processing
ee NES Marks: 100

Time: 10.00 am to 1.00 pm
Durations: 3 (hrs)
No. of Pages: 64-_

Date: 16 April 2022

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on-the cover
of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.

2) Out of remaining questions, attempt any__4 __ questions.
3)Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

1

= Answer briefly in 2-3 sentences
. a. An 8-bit image of size 20x20 is downsampled with the rate 1/2. Downsampled

CO-1; F : he x . .
SO-1. image is converted to 4-bit image. Determine the size of processed image. Also (2]
BL-3. determine required memory (in bits) to save the processed image.
Co- 1; b. no) Ges : ; Tol: :
SO-1: A pixel, ‘r’ of an image is transformed to ‘s’ using the following- [2]
BL-2 > s=cxr’, where ‘c’ is a constant. Describe the effect on the image if y<1.
Co- 1; Gs A binary image consists of a white object against black background. If location of
“fie the object changes, histogram of the image changes or not? Justify your answer.
ner d: An 8-bit 3x3 image consists of all white pixels except the center pixel which is
So- Lt black. A 3x3 median filter is applied on the image. Show the image matrix for | [2]
BL-3 filtered image.
CO-2; e. ; . [2]
SO- 1; DCT transform of an image is useful for image compression. Justify
BL-5

Page 1 of 4
--- page 2 ---
f. [2]
A 5x5 binary image has a white background. It consists of a black square of size

So. : 3x3 in the center. If this image is eroded by a black structuring element of size 3x3,
BL-3 show eroded image.
CO-3; g. Describe first order derivative of the image. Write the significance of magnitude | [2]
ce of first order derivative.
CO-1; h. : [2]
SO-1; . Consider histogram of an image, which has a valley at 100 and two peaks at 50 and
BL-2 200 respectively. Draw histogram of the image and expression for thresholding to
convert this image to binary image.
CO-4; i. Consider two frames of a video. In the reference frame, top left corner of a macro [2]
7 block is located at (20,50). In the other frame, the same micro blocks is located at
(30,40). Compute motion vector. Indicate the direction of movement of this block.
CO-1; j. Assume that a color image is represented by RGB model. Write coordinates of [2]
ae black and white pixels on the cube.
a, An 8-bit image matrix is given below:
70 30 220 | 220
70 30 220 | 220
100 100 150 150
Q2 100 100 150 150
CO-1; [10]
a ri (i) Apply contrast stretching to this image to cover the entire range of pixel
intensities ranging from 0 to the maximum possible value.
(ii) Show image matrix after contrast stretching.
(iii) Draw transformation characteristic
(iv) Discuss the application of contrast stretching.
b. A 3-bit 60x60 grey image has four vertical bars of intensities 0, 2, 6 and 7
respectively. Each bar is of 15 pixels wide.
Q @ Apply histogram equalization on the image .
CO-1; (ii) Show the transformation characteristic [10]
a i (iii) | Draw histogram before and after equalization.

Page 2 of 4
--- page 3 ---
a. An image matrix of an 8-bit image is given below-
60 60 60 60
60 20 20 60
60 20 20 60

Q3 60. 60 60 60

CO-1; Determine image matrix for the following operations on the given image and | [10]
SO-1; °

BLS. comment on filtered image after each operation:

(69) 3x3 average filter

(ii) Laplacian operator

(iii) Vertical Edge detection
(iv) Horizontal filter

Q3 b. Assume that a Low Pass filter is used for filtering a 200x200 image in DFT
CO-1: domain. Size of filter is 200x200. Write the steps of filtering of this image in 110}
SO-6; DFT domain explaining the function of each step. Discuss the effect of change in
li cutoff frequency of low pass filter on filtered image.
a. Hadamard Transformed matrix for an 8-bit image is given below. Matrix is
compressed by ignoring coefficients which are less than 10% of the maximum
value.
(i) Show compressed matrix.
Q4 (ii) Determine the difference in the number of coefficients of matrix
CO-2: before and after ignoring the Hadamard coefficients.
an 7 . (iii) _ Evaluate Inverse Hadamard transform of the compressed matrix. [10]
BL-6 Hadamard Transformed of Image
50 10 6 1
10 10 6 1
6 6 6 1
4 4 2 1
b. (i) Image matrix of a binary image and structuring element are given below:
Image Structuring element
0 0 0 0 0 0 1 1 1
Q4 0 0 0 0 0 0 1 1 1
CO-3; 0 1 0 [0 1 0 1 oii ii [10]
SO-6; 0 0 0 0 1 0
BL-3 0 0 0 0 0 0
Image is dilated by the above structuring element. Dilated image is eroded
by the same structuring element. Show the images at each step.
Page 3 of 4
--- page 4 ---
(ii) Assume that an image consists of rectangular objects of 3x3, 7x7 and 11x11.
Objects of size 3x3 are to be removed, which morphological operation
should be performed? What should be the size of structuring element? :

5 a.
oe Explain the steps involved in Canny edge detection. [10]
BL-3
b. For the given image matrix, apply Region Split and Merge operation for
segmentation. Condition for the segmentation is that the difference between two
pixels should be less than 10 and minimum size of the region is 2x2.
50 55 155 150 180 185 180 180
55 50 155 150 185 180 180 180
Q5 50 55 150 150 280 285 220 230
Fe 5s |s5 | 145 | 140 | 290 | 295 | 240 | 240 [10]
BL-5
Ts 120 125 120 125 220 225 225 225
125 120 120 120 225 220 225 220
120 125 125 120 220 225 220 225
120 125 125 120 225 220 225 220
Interpret the result if minimum size of the split is 4x4.
Q6 a.
CO-4: Explain why motion vectors are preferable over pixel difference in frames for 110)
SO-6; video compression. Show macroblock search for motion vector estimation
BL-2
Q6 b. Write in brief about the following:
Ea (i) RGB and CMYK color models [10]
BL-6 (ii) I, P and B frame for video compression :

Page 4 of 4
````

## 2021-22 · Re-Exam · Sem 6 · paper 826b88ce446d

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/EXTC/VI SEMESTER/IMAGE AND VIDEO PROCESSING/Image and Video Processing, Sem-VI, Re-Exam, Year 2021-22.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 June 2022
- Text: ocr (5 pages), mean OCR confidence 88.3

````text
YS + . RSUIUTE OF SS
< Yo <M

SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & E!

| SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEE.
Academic Year: 2021-22
Programme: B. Tech (EXTC) Year: Il Semester: VI

Subject: Image and Video Processing
Marks: 100

Date: 10 June 2022 Time: 2.00 pm to 5.00 pm
Durations: 3 (Hrs)

No. of Pages: _©OS

, - Re-Examination (2021-22)

5 anni ssa sis is a pits it is Sepampee
‘ Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
a of the Answer Book, which is provided for their use.

1) Question No. _1___- is compulsory.
2) Out of remaining questions, attempt any__4 _ questions.
3) Inall___5_ questions to be attempted.
4) All questions carry equal marks.
‘ 5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

= Answer briefly in 2-3 sentences
Co- 1; a. Good intensity resolution is preferred for reading number plate of a car and poor
aa a intensity resolution is acceptable for counting the cars in an image. Justify P]

b. An 8-bit image has black, white and grey pixels. Using thresholding, highlight | [2]
CO- 1; pixels with intensity more than 70% and less than 30% of the maximum intensity.
=e . Remaining pixels are unchanged. Evaluate threshold and draw transformation

characteristic for this transformation.
CO-1; ©, Consider a dark image with poor contrast. Draw histogram of the given image | [2]
a before and after histogram equalization.
CO-1: d. An 8-bit 3x3 image consists of all white pixels except the center pixel which is | [2]
SO-2; black. A 3x3 average filter is applied on the image. Show the image matrix for
—— Bie filtered image.

e. . . . [2]
co: Consider an image of size 16x16 and Hadamard Transform matrix is of size 8x8.
SO-1; Hadamard Transform of this image is to be computed. How many times Hadamard
BL-4

Transformation operation is required?
--- page 2 ---
f. An 8-bit binary image consists of a black square against white background. If size [2]

SO. : : of the square is to be increased, which morphological operation should be applied?
BL-5 State whether structuring element should be black or white. Justify.
CO-3; g. . [2]
SO-1; Show filter mask to detect diagonal edges with 45 and -45 degree.
BL-2
CO-3; h. Histogram of an 8bit-image has peaks at 50 and 200 respectively. Show how | [2]
+ 2 thresholding is used to segment this image.
‘ i. Consider two frames of a video. In reference frame, top left corners of two macro | [2]
. CO-4; blocks are located at (8,10) and ( 50,15) respectively. In the other frame, the same
a micro blocks are located at (6,20) and (40,30) respectively. Compute motion
vectors.
. Consider that a color image is represented by a RGB model. Assume that ms
CO-1; coordinates of a point on RGB color cube are (x,y,z), where x, y and z represent
~ r Red, Green and Blue components of a pixel respectively. If pixel intensity is |
located (1,1,1) on the RGB color cube, what is the color of this pixel?
a. A 4-bit image matrix is given below:
10 10 10 10
15 15 15 15
8 8 8 8
6 6 6 6
Q2
CO-1; Assume that last two least significant bits of each pixel are ignored. [10]
SO-1; (i) Show the image matrix of compressed image
BLS (ii) Evaluate Root Means Square Error of the compressed image.
(iii) | Determine size (in bits) of the image before and after compression.
ata

215
--- page 3 ---
b. +} A 3-bit 40x40 grey image has four horizontal bars of intensities 0, 1, 2 and 7

Q2
CO-L: respectively. Each horizontal bar is 10 rows wide. Apply histogram equalization
SO-1; on the image. Show the transformation characteristic and histogram before and
BL-3 a
after equalization.
a. An image matrix of an 8-bit image is given below-
50 50 10 10
. 50 50 -10 10
} 50 50 10 10
Q3
* Cua: 50 50 10 10 [10]
* S0-6: Determine image matrix for the following operations and comment on filtered
BL3 image after each operation:
(i) Laplacian operator
(ii) 3x3 weighted average filter
(iii) 3x3 median filter
(iv) Vertical edge detection
93 b. For image filtering in frequency domain, describe the following in brief:
CO-1; (i) Process to center DFT coefficients
(ii) Process to reduce the dynamic range of DFT coefficients with an example | [10]
SO-6; (iii) Ideal Low pass filter in DFT domain and its image representation
BL-2 (iv) Advantage of Gaussian filter over ideal filter
a. Image matrix of an image is given below:
(i) Determine DCT transform of this image
(ii) Transformed image is compressed by ignoring DCT coefficients if
their absolute value are less than 20% of the maximum value. Show
DCT coefficient matrix after modification.
Image matrix
Q4 0 [50 [0 [0
CO-2; 50 0 50 0 {10}
SO-1; 0 0 0 0
BL-3 0 0 0 0
= DCT Transform Matrix is

0.5 0.5 0.5 0.5
0.6 0.2 -0.2 | -0.6
0.5 -0.5 | -0.5 | 0.5
0.2 -0.6 | 0.6 -0.2
--- page 4 ---
(i) Image matrices of binary image and structuring element are given below:

Image Structuring element
0 0 0 0 0 1 1 1
1 1 1 1 0 1 1 1
Q4 1 1 1 1 1 1 ji ji
1 1 1 1 1
CO-3;
SOL: i 1 1 i 0 [10]
BL-5
Image is eroded by the given structuring element. Eroded image is dilated
} by the same structuring element. Show the images at each step.
(ii) Assume that a binary image has white background. This image consists of
4 several circular black objects touching each other. If these object are to be
e : separated, which morphological operation should be performed? What
should be the shape and intensity of structuring element?
Q5 a.
CO-1: List features of HSI model for color image. Show the steps for determining HSI 110)
SO-1; components from the RGB components of an image.
BL-1
b. For the given image matrix,
(i) Apply region growing segmentation. Condition for the segmentation is ii
that the difference between two pixels should be less than 15. Seed for
the segmentation is shown in bold and is underlined in the matrix.
(ii) List the limitations of this method. How is this limitation avoided in
Region splitting method for segmentation?
Qs -
CO-3: 50 55 100 110 120 100 110
[10]
SO-6; 55 45 100 | 120 | 175 | 115 | 205
BL-1

200 160 120 125 300 120 130

105 155 130 205 100 110 120

120 125 130 135 120 225 130

125 130 135 140 225 230 135

130 135 140 145 230 235 140
--- page 5 ---
CO-4: Discuss how motion vectors of video frames are utilized for video compression. 10]
SO-1; Also describe role of I, P and B frames for video compression
BL-2
06 b. | For video compression, draw and explain two dimensional logarithemic search for
.for motion estimation.
CO- ; [10]
SO-1; Also discuss the effect of block size on motion estimation
BL-4
i
i ——
é
bat

5[5
````

## 2019-20 · Final-Exam · Sem 7 · paper 5e3ce3275300

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/EXTC/Sem_07/IMAGE AND VIDEO PROCCESING/IMAGE_AND_VIDEO_PROCESSING_B TECH (EXTC), FINAL_EXAM_2019-20_.pdf`
- Printed on paper: exam date: 13 Novepiber 2019
- Text: ocr (3 pages), mean OCR confidence 87.5

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: B.Tech/ B.Tech Jniegrated (EXT) Year: IV/ V Semester: VII/ Ix
ie

; Academic Year: 2019-20
Subject: Image and Vide Processing

Date: 13 Novepiber 2019 Time: 2

Final Examination (2019-20)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.
1) Question No._1___ is compulsory.
2) Out of remaining questions, attempt any __4 __ questions.
3) Inall___5_ questions to be attempted.
4) All questions carry equal marks.
. 5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume suitable data if necessary.

Ql Attempt any 4
a) | Write equations for the following morphological operations [3.5]
i. Translation
ii. Thickening
iii. Thinning

b) Obtain 4X4 Hadamard matrix from 2X2 Hadamard matrix using Kronecker product. [3.5]
Find Hadamard transform for the given vector x(n) = [1, 2,3, 4]

c) What are bidirectional predictive coded B frames with reference to digital video [3.5]
processing? Explain the terms forward and back prediction.

d) | Segmentation of poorly illuminated images could be difficult. Justify/Contradict 3.5]
e) Quality of a picture depends on spatial and grey level illumination. Justify/Contradict [3.5]

f) Explain thresholding with reference to point processing. For the digital image shown, [3.5]

eee apply thresholding. Take threshold r = 3
1 }2 |2 |2
4 |5 1 2

0 |5 |6 |7
--- page 2 ---
he

Q2

Q3

Q4

Q5

a)

b)

a)

b)

a)

b)

a)

b)

Consider the following image. Perform low pass and high pass filtering operations
using a 3X3 mask on the central 3X3 pixels. Using the same results, show that
HPF image = Original image - LPF image.

0 {0 |5 |4 |0

014 {3 |7 {0

010 |0 |0 |0
Explain RGB colour model. Write expressions for converting RGB model to HSI
model

A 4X4, 3 bits/pixel original image is given below. Apply histogram equalization to
the given image. Sketch the histograms of the original and the equalized image.

4 {5 |2 3
4 {5 55 i
5 [6/4 3
6 {5 |4 5

Discuss progressive and interlaced scanning with reference to video processing

Explain Hough’s transform. Given 4 points in xy plane, with coordinates (1,1), (2,2),
(3,3), (4,4), use Hough’s transform to join these points.

Write the expressions for forward and inverse 1D Discrete Cosine Transform (DCT).
Write DCT transform matrix for N=4. Using the DCT transform matrix, find DCT for
the vector, x = [1,0,1,0]

Explain image segmentation using region split and merge technique.

Segment the following image using split and merge technique. The predicate is that
all the pixels in the region have the same value. Draw quad tree representation for the
corresponding segmentation.

0 |0 [0 1
0 {0 /1 1
0 jl jl 1
1 ji jl l

Discuss boundary extraction morphological algorithm using suitable example.

2f&

-

[7]

[7]

[7]

[7]
[7]

[7]

[7]

[7]
--- page 3 ---
Q6 a) Apply opening and closing operation on the following image using the given [7]
structuring element

Image A Structuring element B

‘ [7]
b) What is the objective of motion estimation algorithm? Explain any one motion
estimation algorithm.
Q7 Write a short note (Any two)
a) Filtering in frequency domain (7]
b) Discrete Wavelet Transform [7]
c)   Thresholding based segmentation [7]
````

## 2019-20 · Final-Exam · Sem 9 · paper bed9d222d87b

- Departments: Electronics and Telecommunication
- Programmes: B.TECH INTEGRATED / EXTC
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/5th YEAR/EXTC/SEM IX/IMAGE AND VIDEO PROCESSING/Image and Video Processing 2019-20 Final.pdf`
- Text: ocr (3 pages), mean OCR confidence 87.3

````text
\
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING
Programme: B.Tech/ B.Tech Jutegrated (EXT) Year: IV/ V Semester: VII/ IX
Fl

; Academic Year: 2019-20
Subject: Image and Tigeo Processing

Date: 13 aa aaa 2019

Final Examination (2019-20)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures ‘in brackets on the right hand side indicate full marks.

7) Assume suitable data if necessary.

Ql Attempt any 4
a) Write equations for the following morphological operations [3.5]
i. Translation
ii, Thickening
iii. Thinning
b) Obtain 4X4 Hadamard matrix from 2X2 Hadamard matrix using Kronecker product. [3.5]
Find Hadamard transform for the given vector x(n) = [1,2,3,4] «

c) | What are bidirectional predictive coded B frames with reference to digital video [3.5]
processing? Explain the terms forward and back prediction.

d) Segmentation of poorly illuminated images could be difficult. Justify/Contradict [3.5]

e) Quality ofa picture depends on spatial and grey level illumination. Justify/Contradict [3.5]

f) Explain thresholding with reference to point processing. For the digital image shown, [3.5]
apply thresholding. Take threshold r = 3

1 |/2 {2 {2
4 |5 |1 42
0 |5 |6 |7
1 |2 |4 13
--- page 2 ---
Q2

Q3

Q4

Q5

a)

b)

a)

b)

a)

b)

a)

b)

Consider the following image. Perform low pass and high pass filtering operations
using a 3X3 mask on the central 3X3 pixels. Using the same results, show that
HPF image = Original image - LPF image.

0 {0 |5 |4 {0

014 (3 |7 {0

0 |0 |0 [0 {0
Explain RGB colour model. Write expressions for converting RGB model to HSI
model

A 4X4, 3 bits/pixel original image is given below. Apply histogram equalization to
the given image. Sketch the histograms of the original and the equalized image.

4 {5 |2 3
4 {5 [5 7
5 |6 |4 3
6 |5 |4 5

Discuss progressive and interlaced scanning with reference to video processing

Explain Hough’s transform. Given 4 points in xy plane, with coordinates (1,1), (2,2),
(3,3), (4,4), use Hough’s transform to join these points.

Write the expressions for forward and inverse 1D Discrete Cosine Transform (DCT).
Write DCT transform matrix for N=4. Using the DCT transform matrix, find DCT for
the vector, x = [1,0,1,0] -

Explain image segmentation using region split and merge technique.

Segment the following image using split and merge technique. The predicate is that
all the pixels in the region have the same value. Draw quad tree representation for the
corresponding segmentation.

0 |0 |0 1
0 |0 {1 1
0 jl jl 1
1 ji fi 1

Discuss boundary extraction morphological algorithm using suitable example.

2[&

“”

[7]

[7]

[7]

[7]
[7]

[7]

[7]

[7]
--- page 3 ---
Q6 a) Apply opening and closing operation on the following image using the given [7]
structuring element

Image A Structuring element B

Z ZZ

. [7]

b) | What is the objective of motion estimation algorithm? Explain any one motion

estimation algorithm.
Q7 Write a short note (Any two)

a) Filtering in frequency domain [7]
. b) Discrete Wavelet Transform (7]
c) Thresholding based segmentation [7]
````

## 2018-19 · Final-Exam · Sem 7 · paper 2d851cf46913

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/EXTC/Sem_07/IMAGE AND VIDEO PROCCESING/IMAGE_AND_VIDEO_PROCESSING_B TECH (EXTC), FINAL_EXAM_2018-19_.pdf`
- Printed on paper: exam date: 19 November 2018
- Text: ocr (3 pages), mean OCR confidence 89.3

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: B. Tech (EXTC) ~ Year: IV Semester: VII ‘—

1 Academic Year: 2018-2019 <

|
| sO MPSTME ~
Subject: Image and Video Processing ~ LIBRARY
Marks\io”
Date: 19 November 2018 Time: 28Qpn
* Durations: {

No. of Pages:

Instructions: Candidates should read carefully the instructions printed on the question
paper and on the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume -suitable data if necessary. ,

Q.1 State whether the following statements are true or false. Justify your 14
answer in 2-3 sentences. (Attempt any.seven)
(a) For enhancement of a grey image, n‘ root of pixels maps narrow
range of low range of values to lower range of values.
(b) For isolated points in a grey image, second order derivative has
lower value than that for the first order derivative.
(c) Low pass filter on image causes blurring in an the image
(d) Discrete Cosine Transform (DCT) can be used for image
compression.
(e) For an image, dilation can be used to increase the size of objects
(f) For segmentation of an image, region splitting starts with a set of
seed points and grows the region around seed point.
(g) For color image using HS! model, hue is a measure of how much a pure
colour is diluted with white
(h) For video signals, intra frames are coded using predecessor.
i For video signal, since scene content does not change much from frame
to frame, motion vectors can be used for video compression.
--- page 2 ---
Q.2 (a) A 4-bit grey image matrix is given below.

[4 [13 [13 [13/8
} ’ 9 15 [14/7 |1
i 10;10/6 |1 |0
9 {6 |12}7 |1
5 ;11)12/11;8
(i) Highlight pixels with intensity in the range 20% to 60% of the
maximuin. Intensity of remaining pixels should remain unchanged.
(ii) Draw transfer characteristic for this transformation.
(b) Describe in details the motion vectors for video signals. 7
Q.3 (a) An image matrix is given below. 8

53 | 56 | 52 | 47
48 | 52 | 49 | 49
51 | 12 {50 | 100
48 | 53 | 52 | 48

Apply 3x3 mask for the following

(i) Averaging filter

(ii) Median filter

(iii) Sobel operator for horizontal edge enhancement
Ignore extreme rows and columns at the edge of image.

(b) Describe HSI color model and show how RGB model is converted to 6
HIS model.

Q.4 (a) Construct a 4x4 Hadamard Transform matrix. Determine Hadamard 7
Transform for the following image matrix.

8 6 5 0
4 3 1 4
2 4 6 2
--- page 3 ---
(b) Describe boundary extraction operation using morphological 7
Operations. Apply boundary extraction operation on the binary
image given below.

Given structuring element is

Q.5 (a) ‘Describe gradient magnitude and direction for images. Show how 7
these parameters are used for edge linking.

(b) In relation to digital video explain frame rate, vertical sampling 7
interval, horizontal sampling interval, data rate and chroma
subsampling.

Q.6 (a) Describe how intensity thresholding is used to segment images. 7
Explain it with an example. Describe global thresholding method to
determine threshold value.

(b) List steps for region growing algorithm for segmentation. For the 7
following image matrix, predicate for region growing is that
difference between two consecutive pixels should be less than 10,
Seed point is 45.

68 | 68 | 68 | 68 | 68 | 68 | 80

70 | 70 | 38 | 41 | 70 | 70 | 10

81 | 81 | 38 | 40 | 46 | 51 | 79

50 | 50 | 52 | 45 | 52 | 52 | 63

81 | 81 | 81 | 81 | 52 | 52 | 63

52 | 81 | 52 | 81 | 81 | 81 | 63

Q.7 Write short notes on any two of the following. 14
aa (a) Block based motion estimation for video signal
(b) 2-D Discrete Wavelet Transform for image
ae (c) optical flow for motion estimation

(d) pseudo color processing

sf
````

## 2017-18 · Final-Exam · Sem 7 · paper 4194a2330c9a

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/EXTC/Sem_07/IMAGE AND VIDEO PROCCESING/IMAGE AND VIDEO PROCESSING B TECH (EXTC), 2017-18 FINAL EXAM.pdf`
- Printed on paper: max marks: 60; exam date: 28 November 2017
- Text: ocr (2 pages), mean OCR confidence 86.5

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: B. Tech (EXTC) _ Year: IV ~ Semester: VII -

cr

Academic Year: 2017-2018

Subject: Image and Video Processing 7, goes
: Marks: 60 pg .

Date: 28 November 2017 Time: 10.00 i¢ 1,

Durations:
No. of Page

‘Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover

of the Answer Book, which is provided for their use.

Final-Examination

1) Question No. | is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume suitable data if necessary.

Ql. State True or False and justify [12]
‘ (i) If all the pixels in an image are shuffled, the histogram of the image also changes.
(ii) Convolutional filters are linear.
(iii) From Isopreference curve it can be concluded that images with large amount of details
require few gray level for representation.
(iv) | Median filter is the best to remove salt and pepper noise.
(v) Laplacian filter can be used to remove noise.
(vi) Erosion results in expansion of the image foreground.

Q2. (i) Perform histogram equalization for 8 x 8 image shown in the table. Draw the original and
equalized histogram. [06]

Gray levels | 0] 1 | 2/3/41] 5 | 6|7
No. of Pixels | 0 | 10] 10) 2 |} 20} 16] 4} 2

a=
° (ii) Obtain Hadamard matrix H(8) from simple second order H(2). 212/4/4
pee Find Walsh transform of the given image. [06] f(xy)=]2]/2]4]4
212/414
212/)4/4
Page 1 of 2
--- page 2 ---
nae

Q3. (i) a) Perform contrast stretching on the [3[3]|4]|4]|5]6 nN 7
i given image segment according to the |4|5/41|1|2|4 eB 6
transfer function shown in figure. [03] 3 : s ; : gz 5 /
. . Thiet = 4 /
b) Draw the histogram of the modified [7716771010 3 3
image obtained in the above case if bit plane 3 2
slicing is performed on the image and the LSB plane is converted S$ [
into all zero values. [03]

0123 45 67
Original Intensity >

(ii) With reference to the image shown explain the technique of image |0|0]| 1] 1
segmentation using split and merge technique. For any region g(x,y) the predicate | 0|1]| 1] 0
is that all the pixels in a region have the same value. Also draw the quad tree. | 0 | 1| 1 | 0

[06] 1) 1})0/0
_Q4. (i) What is morphology? Explain the opening and closing operations of image morphology. [06]
: (ii) Explain the concept of I, B and P frames in digital video. Explain the ITU-RBT 601 standard for

digital video. [06]

QS. (i) Explain how boundary extraction can be done using morphology, also explain how morphology
can be applied to gray scale images. [06]

(ii) What is optical flow? Explain the Exhaustive Block Matching algorithm used in digital video
processing. [06]

Q6. (i) State and explain the various models used for colour images. [06]

(ii) Using Hough transform, find the line passing through the points given:

(1,5), (2,7), (3,9), (4,11), (5,13) [06]
= Q7. Write short notes on any two [12]
. (a) Discrete Wavelet Transform
‘ : (b) Homomorphic Filters

(c) Image filtering in frequency domain
(d) Multiresolution motion estimation

Page 2 of 2
````

## 2017-18 · Re-Exam · Sem 7 · paper c680e41e7456

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/EXTC/Sem_07/IMAGE AND VIDEO PROCCESING/IMAGE AND VIDEO PROCESSING B TECH (EXTC), BATCH 17-18 RE EXAM 2017-18.pdf`
- Printed on paper: duration hours: 3; exam date: 29 May 2018
- Text: ocr (2 pages), mean OCR confidence 81.5

````text
SVKM’s NMIMS G
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERIN

Programme: B. Tech (EXTC) ” Year: IV Semester: VII
: : 2017-18 « AO ag
face Academic Year: 2017-2018 (. aa —<
subject: ideo P sing ¢ i f F . 7
Subject: Image & Video Processing Marke: 60 g ¥ Tuy
Date: 29 May 2018 ” Time: 2.00 pm to s O05 mm“ “Rp fe
ate: ‘Yy Durations: 3 (hrs) “4% ne, i
No. of Pages: NRE rere ae

Re-Examination “mtg

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) Inall___5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer any four
a Median filtering performs well in images corrupted with impulse noise. Justify 3M
b Laplacian is called isotropic filter 3M
c Define dilation and erosion morphological operations 3M
d Give classification of video frames 3M
e Describe RGB colour model 3M
Q2 a Perform histogram equalization on the following grey level distribution 6M
Grey 0 1 2 3 4 5 6 7
level
Number] 790 1023 850 656 329 245 122 81
of
—— pixels
b Explain sampling of video signal in three dimension 6M

Page 1 of 2
--- page 2 ---
Q3

Q4

Q5

Q6

Q7

Compute Hadamard Transform on the following image

2{1 {2 ]1
1 {2/3 |2
2 {3 |4 |3
1 {2 |3 [2

Describe Watershed Segmentation Algorithm
Discuss morphological process of skeletonization

Find distances Da, Ds ,Dm andD-(Euclidean distance) for the following image between
points p and q. Given that V= {0,1}

1 | 2 | 3 | 440

5 | 3 | 2 {1 1

4/2 {1/3 | 0

3 | 1] 0] 24] 5

1}2]0]341

Using Hough’s Transform, join the following set of points
A(L,4), B@,3), C3,1), DGD, EG,0)
Describe various quality measures in digital video processing

Describe motion estimation by block matching method
Describe 2 dimensional DWT-level one decomposition with the help of block diagram

Write short note on any two

Hit or Miss Transform
Homomorphic filtering
Progressive and interlaced scans

Page 2 of 2

6M

6M

8M

4M

6M

6M

6M
6M

12M
````
