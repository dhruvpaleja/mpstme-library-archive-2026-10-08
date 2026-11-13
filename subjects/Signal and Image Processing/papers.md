# Signal and Image Processing: question papers in full

20 unique papers · 2021-22 to 2025-26 · Artificial Intelligence, AI and Data Science, AI and Machine Learning

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 4 · paper 6cf9f08d687f

- Departments: AI and Data Science, Artificial Intelligence
- Programmes: BTech AIDS 7056, MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AIDS_7056/Signal and Image Processing/QP_Signal and Image Processing(702AI0C033)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Signal and Image Processing
Date: 11 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data if necessary.
Q1   Answer briefly:
CO-1;   a   Given the signal x(n)={2, 0, 1, 2, 1}   [04]
SO-1;   ↑
BL-3   Perform the following operations:
i.   Time shifting, 𝑥(𝑛−1)
ii.   Time reversal, 𝑥(−𝑛)
iii.   Scaling, 2𝑥(𝑛)
CO-2;   b   Briefly discuss the following two properties of Discrete Fourier Transform   [04]
SO-1;
(DFT): linearity and periodicity.
BL-2
CO-3;   c   Explain the effect of digital negative transformation on histogram   [04]
SO-1;
redistribution using the image below.
BL-3
3   2   4   5   1
4   5   6   7   1
3   4   2   1   0
4   5   1   2   3
7   6   5   4   1
CO-4;   d   Illustrate the concept of morphological opening operations on binary images.   [04]
SO-1;
Explain the process step-by-step, including intermediate steps.
BL-3
CO-6;   e   Briefly explain the significance of motion vectors and residuals in motion   [04]
SO-1;
estimation.
BL-2
Answer any four from Q2 to Q7
Q2   a   Consider the following grayscale image.   [10]
CO-5;   For homogeneity, (max intensity − min intensity) ≤ T.
SO-1;
BL-3
********** 1 **********
--- page 2 ---
i.   Use region splitting (quadtree approach) with threshold T = 5. Show
image matrix with regions.
ii.   If the threshold is increased to T = 10, show how this change affects
the number of final regions.
iii.   If entire image is homogeneous, determine the threshold and justify
your answer.
CO-3;   b   Compute shape and size for a 3-channel image consisting of 232 rows, 425   [10]
SO-1;
columns, and 8 bits per pixel. Also, find the number of possible colors for
BL-3
this image.
Write the key advantages of binary, grayscale, and color images, and their
applications.
Q3   a   Find the even and odd components of the following signals. Middle element   [10]
CO-1;   is at the origin in each sequence.
SO-1;
i.   𝑥[𝑛] = {−2, 1, 0, 1, −2}
BL-3
↑
ii.   𝑥[𝑛] = {2, 2, 1, 2, 2}
↑
iii.   𝑥[𝑛] = {−1, −3, −4, 3, 1}
↑
CO-2;   b   Find the circular convolution of the following two sequences using DFT-   [10]
SO-1;
IDFT method.
BL-3
𝑥1(𝑛) = {0, 2, 1, 0}   and   𝑥2(𝑛) = {2, 1, 0, 0}
Q4   a   Identify whether the following systems are static or dynamic and causal or   [10]
CO-1;
non-causal. Justify your answer.
SO-1;
BL-3   i.   𝑦[𝑛] = 𝑥[5𝑛]
ii.   𝑦[𝑛−9] + 𝑢[𝑛+ 1] = 𝑥[2𝑛]
iii.   ℎ[𝑛] = 𝑢[𝑛−1] + 6
CO-2;   b   Given x(n) = {1, 0, 0, 1, -1, 0, 0, -1}, compute the 8-point discrete Fourier   [10]
SO-1;
BL-3   transform (DFT) using fast Fourier transform (FFT) with Radix-2.
Q5   a   i.   Perform contrast stretching on the following grayscale image using   [10]
CO-3;   𝑠1 = 3 = 1.5   ,   𝑠2 − 𝑠1 = 4−3 = 1   , and   (𝐿−1) − 𝑠2 = 7−4 = 0.75
SO-1;   𝑟1   2   𝑟2 − 𝑟1   3−2   (𝐿−1) − 𝑟2   7−3
BL-3   ii.   Apply log transformation on the following image with C = 1.5 (and
logarithm of base 10). Normalize the log transformed image using the
formula 𝑠𝑛𝑜𝑟𝑚𝑎𝑙𝑖𝑧𝑒𝑑= 𝑠 × (𝐿−1)
𝑠𝑚𝑎𝑥.
********** 2 **********
--- page 3 ---
5   4   2   3
7   6   0   1
1   1   7   6
2   2   4   5
CO-4;   b   Consider the following binary image and structuring element.   [10]
SO-1;
i.   Apply the dilation operation and determine the resulting output
BL-3
image.
ii.   Describe the effect of dilation on the hole (zeros) present at the center
of the image and justify your answer.
iii.   If the size of the structuring element is increased to a 5×5 matrix (all
elements with value 1) and is defined symmetrically about the origin,
describe the effect of dilation on the image.
Given: The origin is located at the center of the structuring element.
0 0 0 0 0 0 0 0   1 1 1
0 0 0 0 0 0 0 0   [ 1 1 1 ]
0 0 1 1 1 1 0 0   1 1 1
0 0 1 0 0 1 0 0
0 0 1 1 1 1 0 0
0 0 0 0 0 0 0 0
[ 0 0 0 0 0 0 0 0]
Image   Structuring Element
Q6   a   Apply the following filters on the given grayscale image without zero   [10]
CO-3;   padding.
SO-1;
i. A Laplacian filter of size 3×3 with diagonals and its center coefficient
BL-3
with negative sign.
ii. A Laplacian filter of size 3×3 with no diagonals but its center
coefficient with negative sign.
iii.   Median filter of size 3×3.
0   7   1   2
7   1   7   1
2   7   1   7
3   4   5   6
********** 3 **********
--- page 4 ---
CO-1;   b   Perform convolution sum of the following two sequences by tabulation   [05]
SO-1;
method.
BL-3
Index (n)   -3   -2   1   0   1
x(n)   5   4   3   2   1
h(n)   1   2   2   2   2
CO-2;   c   Find the Discrete Fourier transform (DFT) of the 1-D signal, 𝑥(𝑛) =   [05]
SO-1;
BL-3   {4,2,1,2}
Q7   a   Normalize the following grayscale image matrix to the range [0, 1] using the   [05]
CO-3;   formula [ 𝑥 − 𝑥𝑚𝑖𝑛   ]. Then apply the power-law (gamma) transformation
SO-1;   𝑥𝑚𝑎𝑥 − 𝑥𝑚𝑖𝑛
BL-3   with c=1 and γ=0.5. Show the final output image matrix.
2   3   4   5
2   2   2   2
1   1   1   1
4   6   7   0
CO-5;   b   Explain why image smoothing is applied before thresholding when   [05]
SO-1;
converting a grayscale image to a binary image. Illustrate your answer with
BL-3
an example by comparing the image and its corresponding histogram before
and after smoothing.
CO-6;   c   Briefly explain any two measures of digital video quality.   [05]
SO-1;
BL-2
CO-6;   d   State the advantages and limitations of the Exhaustive Search Block   [05]
SO-1;
Matching method in video processing.
BL-2
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 4 · paper 12ade54703af

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AIML_7053/Signal and Image Processing/QP_Signal and Image Processing(702AI0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Signal and Image Processing
Date: 11 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data if necessary.
Q1   Answer briefly:
CO-1;   a   Given the signal x(n)={2, 0, 1, 2, 1}   [04]
SO-1;   ↑
BL-3   Perform the following operations:
i.   Time shifting, 𝑥(𝑛−1)
ii.   Time reversal, 𝑥(−𝑛)
iii.   Scaling, 2𝑥(𝑛)
CO-2;   b   Briefly discuss the following two properties of Discrete Fourier Transform   [04]
SO-1;
(DFT): linearity and periodicity.
BL-2
CO-3;   c   Explain the effect of digital negative transformation on histogram   [04]
SO-1;
redistribution using the image below.
BL-3
3   2   4   5   1
4   5   6   7   1
3   4   2   1   0
4   5   1   2   3
7   6   5   4   1
CO-4;   d   Illustrate the concept of morphological opening operations on binary images.   [04]
SO-1;
Explain the process step-by-step, including intermediate steps.
BL-3
CO-6;   e   Briefly explain the significance of motion vectors and residuals in motion   [04]
SO-1;
estimation.
BL-2
Answer any four from Q2 to Q7
Q2   a   Consider the following grayscale image.   [10]
CO-5;   For homogeneity, (max intensity − min intensity) ≤ T.
SO-1;
BL-3
********** 1 **********
--- page 2 ---
i.   Use region splitting (quadtree approach) with threshold T = 5. Show
image matrix with regions.
ii.   If the threshold is increased to T = 10, show how this change affects
the number of final regions.
iii.   If entire image is homogeneous, determine the threshold and justify
your answer.
CO-3;   b   Compute shape and size for a 3-channel image consisting of 232 rows, 425   [10]
SO-1;
columns, and 8 bits per pixel. Also, find the number of possible colors for
BL-3
this image.
Write the key advantages of binary, grayscale, and color images, and their
applications.
Q3   a   Find the even and odd components of the following signals. Middle element   [10]
CO-1;   is at the origin in each sequence.
SO-1;
i.   𝑥[𝑛] = {−2, 1, 0, 1, −2}
BL-3
↑
ii.   𝑥[𝑛] = {2, 2, 1, 2, 2}
↑
iii.   𝑥[𝑛] = {−1, −3, −4, 3, 1}
↑
CO-2;   b   Find the circular convolution of the following two sequences using DFT-   [10]
SO-1;
IDFT method.
BL-3
𝑥1(𝑛) = {0, 2, 1, 0}   and   𝑥2(𝑛) = {2, 1, 0, 0}
Q4   a   Identify whether the following systems are static or dynamic and causal or   [10]
CO-1;
non-causal. Justify your answer.
SO-1;
BL-3   i.   𝑦[𝑛] = 𝑥[5𝑛]
ii.   𝑦[𝑛−9] + 𝑢[𝑛+ 1] = 𝑥[2𝑛]
iii.   ℎ[𝑛] = 𝑢[𝑛−1] + 6
CO-2;   b   Given x(n) = {1, 0, 0, 1, -1, 0, 0, -1}, compute the 8-point discrete Fourier   [10]
SO-1;
BL-3   transform (DFT) using fast Fourier transform (FFT) with Radix-2.
Q5   a   i.   Perform contrast stretching on the following grayscale image using   [10]
CO-3;   𝑠1 = 3 = 1.5   ,   𝑠2 − 𝑠1 = 4−3 = 1   , and   (𝐿−1) − 𝑠2 = 7−4 = 0.75
SO-1;   𝑟1   2   𝑟2 − 𝑟1   3−2   (𝐿−1) − 𝑟2   7−3
BL-3   ii.   Apply log transformation on the following image with C = 1.5 (and
logarithm of base 10). Normalize the log transformed image using the
formula 𝑠𝑛𝑜𝑟𝑚𝑎𝑙𝑖𝑧𝑒𝑑= 𝑠 × (𝐿−1)
𝑠𝑚𝑎𝑥.
********** 2 **********
--- page 3 ---
5   4   2   3
7   6   0   1
1   1   7   6
2   2   4   5
CO-4;   b   Consider the following binary image and structuring element.   [10]
SO-1;
i.   Apply the dilation operation and determine the resulting output
BL-3
image.
ii.   Describe the effect of dilation on the hole (zeros) present at the center
of the image and justify your answer.
iii.   If the size of the structuring element is increased to a 5×5 matrix (all
elements with value 1) and is defined symmetrically about the origin,
describe the effect of dilation on the image.
Given: The origin is located at the center of the structuring element.
0 0 0 0 0 0 0 0   1 1 1
0 0 0 0 0 0 0 0   [ 1 1 1 ]
0 0 1 1 1 1 0 0   1 1 1
0 0 1 0 0 1 0 0
0 0 1 1 1 1 0 0
0 0 0 0 0 0 0 0
[ 0 0 0 0 0 0 0 0]
Image   Structuring Element
Q6   a   Apply the following filters on the given grayscale image without zero   [10]
CO-3;   padding.
SO-1;
i. A Laplacian filter of size 3×3 with diagonals and its center coefficient
BL-3
with negative sign.
ii. A Laplacian filter of size 3×3 with no diagonals but its center
coefficient with negative sign.
iii.   Median filter of size 3×3.
0   7   1   2
7   1   7   1
2   7   1   7
3   4   5   6
********** 3 **********
--- page 4 ---
CO-1;   b   Perform convolution sum of the following two sequences by tabulation   [05]
SO-1;
method.
BL-3
Index (n)   -3   -2   1   0   1
x(n)   5   4   3   2   1
h(n)   1   2   2   2   2
CO-2;   c   Find the Discrete Fourier transform (DFT) of the 1-D signal, 𝑥(𝑛) =   [05]
SO-1;
BL-3   {4,2,1,2}
Q7   a   Normalize the following grayscale image matrix to the range [0, 1] using the   [05]
CO-3;   formula [ 𝑥 − 𝑥𝑚𝑖𝑛   ]. Then apply the power-law (gamma) transformation
SO-1;   𝑥𝑚𝑎𝑥 − 𝑥𝑚𝑖𝑛
BL-3   with c=1 and γ=0.5. Show the final output image matrix.
2   3   4   5
2   2   2   2
1   1   1   1
4   6   7   0
CO-5;   b   Explain why image smoothing is applied before thresholding when   [05]
SO-1;
converting a grayscale image to a binary image. Illustrate your answer with
BL-3
an example by comparing the image and its corresponding histogram before
and after smoothing.
CO-6;   c   Briefly explain any two measures of digital video quality.   [05]
SO-1;
BL-2
CO-6;   d   State the advantages and limitations of the Exhaustive Search Block   [05]
SO-1;
Matching method in video processing.
BL-2
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 4 · paper fea028ed3452

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AI_7012/Signal and Image Processing/QP_Signal and Image Processing(702AI0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Signal and Image Processing
Date: 11 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data if necessary.
Q1   Answer briefly:
CO-1;   a   Given the signal x(n)={2, 0, 1, 2, 1}   [04]
SO-1;   ↑
BL-3   Perform the following operations:
i.   Time shifting, 𝑥(𝑛−1)
ii.   Time reversal, 𝑥(−𝑛)
iii.   Scaling, 2𝑥(𝑛)
CO-2;   b   Briefly discuss the following two properties of Discrete Fourier Transform   [04]
SO-1;
(DFT): linearity and periodicity.
BL-2
CO-3;   c   Explain the effect of digital negative transformation on histogram   [04]
SO-1;
redistribution using the image below.
BL-3
3   2   4   5   1
4   5   6   7   1
3   4   2   1   0
4   5   1   2   3
7   6   5   4   1
CO-4;   d   Illustrate the concept of morphological opening operations on binary images.   [04]
SO-1;
Explain the process step-by-step, including intermediate steps.
BL-3
CO-6;   e   Briefly explain the significance of motion vectors and residuals in motion   [04]
SO-1;
estimation.
BL-2
Answer any four from Q2 to Q7
Q2   a   Consider the following grayscale image.   [10]
CO-5;   For homogeneity, (max intensity − min intensity) ≤ T.
SO-1;
BL-3
********** 1 **********
--- page 2 ---
i.   Use region splitting (quadtree approach) with threshold T = 5. Show
image matrix with regions.
ii.   If the threshold is increased to T = 10, show how this change affects
the number of final regions.
iii.   If entire image is homogeneous, determine the threshold and justify
your answer.
CO-3;   b   Compute shape and size for a 3-channel image consisting of 232 rows, 425   [10]
SO-1;
columns, and 8 bits per pixel. Also, find the number of possible colors for
BL-3
this image.
Write the key advantages of binary, grayscale, and color images, and their
applications.
Q3   a   Find the even and odd components of the following signals. Middle element   [10]
CO-1;   is at the origin in each sequence.
SO-1;
i.   𝑥[𝑛] = {−2, 1, 0, 1, −2}
BL-3
↑
ii.   𝑥[𝑛] = {2, 2, 1, 2, 2}
↑
iii.   𝑥[𝑛] = {−1, −3, −4, 3, 1}
↑
CO-2;   b   Find the circular convolution of the following two sequences using DFT-   [10]
SO-1;
IDFT method.
BL-3
𝑥1(𝑛) = {0, 2, 1, 0}   and   𝑥2(𝑛) = {2, 1, 0, 0}
Q4   a   Identify whether the following systems are static or dynamic and causal or   [10]
CO-1;
non-causal. Justify your answer.
SO-1;
BL-3   i.   𝑦[𝑛] = 𝑥[5𝑛]
ii.   𝑦[𝑛−9] + 𝑢[𝑛+ 1] = 𝑥[2𝑛]
iii.   ℎ[𝑛] = 𝑢[𝑛−1] + 6
CO-2;   b   Given x(n) = {1, 0, 0, 1, -1, 0, 0, -1}, compute the 8-point discrete Fourier   [10]
SO-1;
BL-3   transform (DFT) using fast Fourier transform (FFT) with Radix-2.
Q5   a   i.   Perform contrast stretching on the following grayscale image using   [10]
CO-3;   𝑠1 = 3 = 1.5   ,   𝑠2 − 𝑠1 = 4−3 = 1   , and   (𝐿−1) − 𝑠2 = 7−4 = 0.75
SO-1;   𝑟1   2   𝑟2 − 𝑟1   3−2   (𝐿−1) − 𝑟2   7−3
BL-3   ii.   Apply log transformation on the following image with C = 1.5 (and
logarithm of base 10). Normalize the log transformed image using the
formula 𝑠𝑛𝑜𝑟𝑚𝑎𝑙𝑖𝑧𝑒𝑑= 𝑠 × (𝐿−1)
𝑠𝑚𝑎𝑥.
********** 2 **********
--- page 3 ---
5   4   2   3
7   6   0   1
1   1   7   6
2   2   4   5
CO-4;   b   Consider the following binary image and structuring element.   [10]
SO-1;
i.   Apply the dilation operation and determine the resulting output
BL-3
image.
ii.   Describe the effect of dilation on the hole (zeros) present at the center
of the image and justify your answer.
iii.   If the size of the structuring element is increased to a 5×5 matrix (all
elements with value 1) and is defined symmetrically about the origin,
describe the effect of dilation on the image.
Given: The origin is located at the center of the structuring element.
0 0 0 0 0 0 0 0   1 1 1
0 0 0 0 0 0 0 0   [ 1 1 1 ]
0 0 1 1 1 1 0 0   1 1 1
0 0 1 0 0 1 0 0
0 0 1 1 1 1 0 0
0 0 0 0 0 0 0 0
[ 0 0 0 0 0 0 0 0]
Image   Structuring Element
Q6   a   Apply the following filters on the given grayscale image without zero   [10]
CO-3;   padding.
SO-1;
i. A Laplacian filter of size 3×3 with diagonals and its center coefficient
BL-3
with negative sign.
ii. A Laplacian filter of size 3×3 with no diagonals but its center
coefficient with negative sign.
iii.   Median filter of size 3×3.
0   7   1   2
7   1   7   1
2   7   1   7
3   4   5   6
********** 3 **********
--- page 4 ---
CO-1;   b   Perform convolution sum of the following two sequences by tabulation   [05]
SO-1;
method.
BL-3
Index (n)   -3   -2   1   0   1
x(n)   5   4   3   2   1
h(n)   1   2   2   2   2
CO-2;   c   Find the Discrete Fourier transform (DFT) of the 1-D signal, 𝑥(𝑛) =   [05]
SO-1;
BL-3   {4,2,1,2}
Q7   a   Normalize the following grayscale image matrix to the range [0, 1] using the   [05]
CO-3;   formula [ 𝑥 − 𝑥𝑚𝑖𝑛   ]. Then apply the power-law (gamma) transformation
SO-1;   𝑥𝑚𝑎𝑥 − 𝑥𝑚𝑖𝑛
BL-3   with c=1 and γ=0.5. Show the final output image matrix.
2   3   4   5
2   2   2   2
1   1   1   1
4   6   7   0
CO-5;   b   Explain why image smoothing is applied before thresholding when   [05]
SO-1;
converting a grayscale image to a binary image. Illustrate your answer with
BL-3
an example by comparing the image and its corresponding histogram before
and after smoothing.
CO-6;   c   Briefly explain any two measures of digital video quality.   [05]
SO-1;
BL-2
CO-6;   d   State the advantages and limitations of the Exhaustive Search Block   [05]
SO-1;
Matching method in video processing.
BL-2
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 4 · paper 53445e5c3ac1

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AIDS_7056/Signal and Image Processing/QP_Signal and Image Processing(702AI0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 Jul 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Signal and Image Processing
Date: 14 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data if necessary.
Q1   Answer briefly:
CO-1;   a   Perform time shifting on the following discrete time signal to determine 𝑥(𝑛−   [04]
SO-1;
2) and 𝑥(−𝑛).
BL-3
CO-2;   b   Perform circular convolution of the sequences x1(n) = {2, 1, 2, 1} and   [04]
SO-1;
x2(n) = {1, 2, 1, 2} using the matrix multiplication method.
BL-3
CO-3;   c   Explain the concept of gray level slicing. For the given 4-bit grayscale image,   [04]
SO-1;
perform gray level slicing without preserving the background using thresholds
BL-3
T1 = 6 and T2 = 11. Show all the steps and discuss how different threshold
ranges affect image enhancement and background information loss.
15   11   6   7   8
10   12   15   3   1
8   9   5   11   12
7   5   6   8   0
12   3   4   10   13
CO-5;   d   Discuss the concept of region merging in image segmentation and illustrate it   [04]
SO-1;
with an example.
BL-3
CO-6;   e   Explain motion estimation in video processing. Mention any three motion   [04]
SO-1;
estimation algorithms used in video processing?
BL-2
Answer any four from Q2 to Q7
********** 1 **********
--- page 2 ---
Q2   a   [10]
Explain the steps involved in finding the optimal threshold using Otsu’s
CO-5;
SO-1;   thresholding method for image segmentation.
BL-2
CO-3;   b   i.   Mention any three-color models used in image processing.   [10]
SO-1;
BL-3   ii.   Convert the RGB color value (0.2,0.4,0.7) into the CMYK color
model.
iii.   Consider the following 5×5 binary image. The origin is at the top-left
corner, and coordinates are written as (row, column) using 1-based
indexing. Foreground pixels have value 1 (set V= {1}).
1 0 1 0 0
1 1 0 0 1
𝐼 = 0 0 1 0 0
0 1 0 1 0
0 0 0 0 1
Draw lines showing the connections between pixels of the same label
under:
• 4-adjacency
• 8-adjacency
Q3   a   State the commutative and distributive properties of convolution. Perform   [10]
CO-1;   convolution sum of the following two sequences by tabulation method and
SO-1;
matrix methods.
BL-3
Index (n)   -2   -1   0   1
x(n)   2   2   1   2
h(n)   1   1   1   -2
CO-2;   b   Given x(n) = {1, 1, 1, 1, 0, 0, 0, 0}, compute the 8-point discrete Fourier   [10]
SO-1;
transform (DFT) using fast Fourier transform (FFT) with Radix-2.
BL-3
Q4   a   Find the even and odd components of the following signal and sketch the same.   [10]
CO-1;
Index (n)   -3   -2   -1   0   1   2   3   4
SO-1;
x(n)   1   2   3   4   5   6   7   8
BL-3
CO-2;   b   Find the response of Linear Time Invariant (LTI) system with input, x(n) =   [10]
SO-1;
{2,2,2}, and impulse function, h(n) = {1, 1} using decimation in time (DIT)
BL-3
with radix-2 Fast Fourier Transform (FFT).
Q5   a   Consider the following images:   [10]
CO-3;   10   10   10   10   10   30   30   30
SO-1;   30   30   30   30   10   30   30   30
BL-3   30   30   30   30   10   30   30   30
30   30   30   30   10   30   30   30
Image 1   Image 2
********** 2 **********
--- page 3 ---
i.   Apply the horizontal and vertical Sobel operators (without zero
padding) to Image 1 and Image 2 and compute the gradient magnitude
for both images.
ii.   Write your observations based on the results obtained in part (i).
CO-5;   b   Consider the following grayscale image. Two seed points are selected at   [10]
SO-1;
locations (1,1) and (4,1), which are shown in bold. Assume 8-connectivity.
BL-3
𝟏𝟎 11 10 80 80
11 10 11 80 81
10 11 10 80 80
𝟓𝟎 51 50 55 55
[ 50 50 51 55 55]
i.   Apply region growing with a threshold of ±2 and show the pixels
included in the segmented regions.
ii.   Apply region growing with thresholds of ±10 and ±1, and show the
pixels included in the segmented regions.
iii.   Illustrate the effect of small and large threshold values on segmentation
using the above results.
Q6   a   Calculate the histogram equalization of the given 3-bit image segment. Plot   [10]
CO-3;   the histogram before and after histogram equalization. Analyze the histograms
SO-1;
and show the resultant image.
BL-3
6   6   6   6   6   6
0   5   5   5   5   0
3   2   2   2   2   3
3   1   1   1   1   3
3   6   7   7   6   3
3   4   4   4   4   3
CO-1;   b   Determine whether the following signals are energy signal or power signal.   [05]
SO-1;   i.   x[n] = u[n]
BL-3   ii.   x[n] = 5
CO-2;   c   Calculate the discrete Fourier transform (DFT) for the signal, x(n) = {1, 1, 1,   [05]
SO-1;
1}, using the twiddle matrix method.
BL-3
Q7   a   Define the Ideal Low-Pass Filter (ILPF) in the frequency domain. Explain its   [05]
CO-3;   effect on an image and discuss the occurrence of ringing artifacts. Also explain
SO-1;
the role of cutoff frequency.
********** 3 **********
--- page 4 ---
BL-2
CO-4;   b A binary image is shown below. The diameters of the circular objects are 3, 5,   [05]
SO-1;
and 7 pixels. The sizes of the square objects are 9×9, 11×11, and 15×15 pixels.
BL-3
i.   Apply erosion to eliminate all the objects except the largest square.
Justify your answer.
ii.   Determine the size, shape, and intensity (value) of the structuring
element required.
CO-6;   c   Compare I-frames, P-frames, and B-frames in video compression. Write at   [05]
SO-1;
least five differences between them.
BL-2
CO-6;   d   [05]
SO-1;   Explain the Three-Step Search (TSS) method used in video processing.
BL-2
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 4 · paper 025a2d5a28be

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AI_7012/Signal and Image Processing/QP_Signal and Image Processing(702AI0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 Jul 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Signal and Image Processing
Date: 14 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data if necessary.
Q1   Answer briefly:
CO-1;   a   Perform time shifting on the following discrete time signal to determine 𝑥(𝑛−   [04]
SO-1;
2) and 𝑥(−𝑛).
BL-3
CO-2;   b   Perform circular convolution of the sequences x1(n) = {2, 1, 2, 1} and   [04]
SO-1;
x2(n) = {1, 2, 1, 2} using the matrix multiplication method.
BL-3
CO-3;   c   Explain the concept of gray level slicing. For the given 4-bit grayscale image,   [04]
SO-1;
perform gray level slicing without preserving the background using thresholds
BL-3
T1 = 6 and T2 = 11. Show all the steps and discuss how different threshold
ranges affect image enhancement and background information loss.
15   11   6   7   8
10   12   15   3   1
8   9   5   11   12
7   5   6   8   0
12   3   4   10   13
CO-5;   d   Discuss the concept of region merging in image segmentation and illustrate it   [04]
SO-1;
with an example.
BL-3
CO-6;   e   Explain motion estimation in video processing. Mention any three motion   [04]
SO-1;
estimation algorithms used in video processing?
BL-2
Answer any four from Q2 to Q7
********** 1 **********
--- page 2 ---
Q2   a   [10]
Explain the steps involved in finding the optimal threshold using Otsu’s
CO-5;
SO-1;   thresholding method for image segmentation.
BL-2
CO-3;   b   i.   Mention any three-color models used in image processing.   [10]
SO-1;
BL-3   ii.   Convert the RGB color value (0.2,0.4,0.7) into the CMYK color
model.
iii.   Consider the following 5×5 binary image. The origin is at the top-left
corner, and coordinates are written as (row, column) using 1-based
indexing. Foreground pixels have value 1 (set V= {1}).
1 0 1 0 0
1 1 0 0 1
𝐼 = 0 0 1 0 0
0 1 0 1 0
0 0 0 0 1
Draw lines showing the connections between pixels of the same label
under:
• 4-adjacency
• 8-adjacency
Q3   a   State the commutative and distributive properties of convolution. Perform   [10]
CO-1;   convolution sum of the following two sequences by tabulation method and
SO-1;
matrix methods.
BL-3
Index (n)   -2   -1   0   1
x(n)   2   2   1   2
h(n)   1   1   1   -2
CO-2;   b   Given x(n) = {1, 1, 1, 1, 0, 0, 0, 0}, compute the 8-point discrete Fourier   [10]
SO-1;
transform (DFT) using fast Fourier transform (FFT) with Radix-2.
BL-3
Q4   a   Find the even and odd components of the following signal and sketch the same.   [10]
CO-1;
Index (n)   -3   -2   -1   0   1   2   3   4
SO-1;
x(n)   1   2   3   4   5   6   7   8
BL-3
CO-2;   b   Find the response of Linear Time Invariant (LTI) system with input, x(n) =   [10]
SO-1;
{2,2,2}, and impulse function, h(n) = {1, 1} using decimation in time (DIT)
BL-3
with radix-2 Fast Fourier Transform (FFT).
Q5   a   Consider the following images:   [10]
CO-3;   10   10   10   10   10   30   30   30
SO-1;   30   30   30   30   10   30   30   30
BL-3   30   30   30   30   10   30   30   30
30   30   30   30   10   30   30   30
Image 1   Image 2
********** 2 **********
--- page 3 ---
i.   Apply the horizontal and vertical Sobel operators (without zero
padding) to Image 1 and Image 2 and compute the gradient magnitude
for both images.
ii.   Write your observations based on the results obtained in part (i).
CO-5;   b   Consider the following grayscale image. Two seed points are selected at   [10]
SO-1;
locations (1,1) and (4,1), which are shown in bold. Assume 8-connectivity.
BL-3
𝟏𝟎 11 10 80 80
11 10 11 80 81
10 11 10 80 80
𝟓𝟎 51 50 55 55
[ 50 50 51 55 55]
i.   Apply region growing with a threshold of ±2 and show the pixels
included in the segmented regions.
ii.   Apply region growing with thresholds of ±10 and ±1, and show the
pixels included in the segmented regions.
iii.   Illustrate the effect of small and large threshold values on segmentation
using the above results.
Q6   a   Calculate the histogram equalization of the given 3-bit image segment. Plot   [10]
CO-3;   the histogram before and after histogram equalization. Analyze the histograms
SO-1;
and show the resultant image.
BL-3
6   6   6   6   6   6
0   5   5   5   5   0
3   2   2   2   2   3
3   1   1   1   1   3
3   6   7   7   6   3
3   4   4   4   4   3
CO-1;   b   Determine whether the following signals are energy signal or power signal.   [05]
SO-1;   i.   x[n] = u[n]
BL-3   ii.   x[n] = 5
CO-2;   c   Calculate the discrete Fourier transform (DFT) for the signal, x(n) = {1, 1, 1,   [05]
SO-1;
1}, using the twiddle matrix method.
BL-3
Q7   a   Define the Ideal Low-Pass Filter (ILPF) in the frequency domain. Explain its   [05]
CO-3;   effect on an image and discuss the occurrence of ringing artifacts. Also explain
SO-1;
the role of cutoff frequency.
********** 3 **********
--- page 4 ---
BL-2
CO-4;   b A binary image is shown below. The diameters of the circular objects are 3, 5,   [05]
SO-1;
and 7 pixels. The sizes of the square objects are 9×9, 11×11, and 15×15 pixels.
BL-3
i.   Apply erosion to eliminate all the objects except the largest square.
Justify your answer.
ii.   Determine the size, shape, and intensity (value) of the structuring
element required.
CO-6;   c   Compare I-frames, P-frames, and B-frames in video compression. Write at   [05]
SO-1;
least five differences between them.
BL-2
CO-6;   d   [05]
SO-1;   Explain the Three-Step Search (TSS) method used in video processing.
BL-2
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 4 · paper 864f6576472d

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_AI_7051/Signal and Image Processing/QP_Signal and Image Processing(702AI0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 Jul 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Signal and Image Processing
Date: 14 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data if necessary.
Q1   Answer briefly:
CO-1;   a   Perform time shifting on the following discrete time signal to determine 𝑥(𝑛−   [04]
SO-1;
2) and 𝑥(−𝑛).
BL-3
CO-2;   b   Perform circular convolution of the sequences x1(n) = {2, 1, 2, 1} and   [04]
SO-1;
x2(n) = {1, 2, 1, 2} using the matrix multiplication method.
BL-3
CO-3;   c   Explain the concept of gray level slicing. For the given 4-bit grayscale image,   [04]
SO-1;
perform gray level slicing without preserving the background using thresholds
BL-3
T1 = 6 and T2 = 11. Show all the steps and discuss how different threshold
ranges affect image enhancement and background information loss.
15   11   6   7   8
10   12   15   3   1
8   9   5   11   12
7   5   6   8   0
12   3   4   10   13
CO-5;   d   Discuss the concept of region merging in image segmentation and illustrate it   [04]
SO-1;
with an example.
BL-3
CO-6;   e   Explain motion estimation in video processing. Mention any three motion   [04]
SO-1;
estimation algorithms used in video processing?
BL-2
Answer any four from Q2 to Q7
********** 1 **********
--- page 2 ---
Q2   a   [10]
Explain the steps involved in finding the optimal threshold using Otsu’s
CO-5;
SO-1;   thresholding method for image segmentation.
BL-2
CO-3;   b   i.   Mention any three-color models used in image processing.   [10]
SO-1;
BL-3   ii.   Convert the RGB color value (0.2,0.4,0.7) into the CMYK color
model.
iii.   Consider the following 5×5 binary image. The origin is at the top-left
corner, and coordinates are written as (row, column) using 1-based
indexing. Foreground pixels have value 1 (set V= {1}).
1 0 1 0 0
1 1 0 0 1
𝐼 = 0 0 1 0 0
0 1 0 1 0
0 0 0 0 1
Draw lines showing the connections between pixels of the same label
under:
• 4-adjacency
• 8-adjacency
Q3   a   State the commutative and distributive properties of convolution. Perform   [10]
CO-1;   convolution sum of the following two sequences by tabulation method and
SO-1;
matrix methods.
BL-3
Index (n)   -2   -1   0   1
x(n)   2   2   1   2
h(n)   1   1   1   -2
CO-2;   b   Given x(n) = {1, 1, 1, 1, 0, 0, 0, 0}, compute the 8-point discrete Fourier   [10]
SO-1;
transform (DFT) using fast Fourier transform (FFT) with Radix-2.
BL-3
Q4   a   Find the even and odd components of the following signal and sketch the same.   [10]
CO-1;
Index (n)   -3   -2   -1   0   1   2   3   4
SO-1;
x(n)   1   2   3   4   5   6   7   8
BL-3
CO-2;   b   Find the response of Linear Time Invariant (LTI) system with input, x(n) =   [10]
SO-1;
{2,2,2}, and impulse function, h(n) = {1, 1} using decimation in time (DIT)
BL-3
with radix-2 Fast Fourier Transform (FFT).
Q5   a   Consider the following images:   [10]
CO-3;   10   10   10   10   10   30   30   30
SO-1;   30   30   30   30   10   30   30   30
BL-3   30   30   30   30   10   30   30   30
30   30   30   30   10   30   30   30
Image 1   Image 2
********** 2 **********
--- page 3 ---
i.   Apply the horizontal and vertical Sobel operators (without zero
padding) to Image 1 and Image 2 and compute the gradient magnitude
for both images.
ii.   Write your observations based on the results obtained in part (i).
CO-5;   b   Consider the following grayscale image. Two seed points are selected at   [10]
SO-1;
locations (1,1) and (4,1), which are shown in bold. Assume 8-connectivity.
BL-3
𝟏𝟎 11 10 80 80
11 10 11 80 81
10 11 10 80 80
𝟓𝟎 51 50 55 55
[ 50 50 51 55 55]
i.   Apply region growing with a threshold of ±2 and show the pixels
included in the segmented regions.
ii.   Apply region growing with thresholds of ±10 and ±1, and show the
pixels included in the segmented regions.
iii.   Illustrate the effect of small and large threshold values on segmentation
using the above results.
Q6   a   Calculate the histogram equalization of the given 3-bit image segment. Plot   [10]
CO-3;   the histogram before and after histogram equalization. Analyze the histograms
SO-1;
and show the resultant image.
BL-3
6   6   6   6   6   6
0   5   5   5   5   0
3   2   2   2   2   3
3   1   1   1   1   3
3   6   7   7   6   3
3   4   4   4   4   3
CO-1;   b   Determine whether the following signals are energy signal or power signal.   [05]
SO-1;   i.   x[n] = u[n]
BL-3   ii.   x[n] = 5
CO-2;   c   Calculate the discrete Fourier transform (DFT) for the signal, x(n) = {1, 1, 1,   [05]
SO-1;
1}, using the twiddle matrix method.
BL-3
Q7   a   Define the Ideal Low-Pass Filter (ILPF) in the frequency domain. Explain its   [05]
CO-3;   effect on an image and discuss the occurrence of ringing artifacts. Also explain
SO-1;
the role of cutoff frequency.
********** 3 **********
--- page 4 ---
BL-2
CO-4;   b A binary image is shown below. The diameters of the circular objects are 3, 5,   [05]
SO-1;
and 7 pixels. The sizes of the square objects are 9×9, 11×11, and 15×15 pixels.
BL-3
i.   Apply erosion to eliminate all the objects except the largest square.
Justify your answer.
ii.   Determine the size, shape, and intensity (value) of the structuring
element required.
CO-6;   c   Compare I-frames, P-frames, and B-frames in video compression. Write at   [05]
SO-1;
least five differences between them.
BL-2
CO-6;   d   [05]
SO-1;   Explain the Three-Step Search (TSS) method used in video processing.
BL-2
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 4 · paper 60da27ef29b4

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/ARTIFICIAL INTELLIGENCE/SEM-IV/SIGNAL AND IMAGE PROCESSING/Signal and Image Processing, Sem-IV, Batch 2022-23, 2023-24 &2024-25, 2025-26, Re Exam.pdf`
- Printed on paper: max marks: 100; exam date: 14th July 2026
- Text: ocr (4 pages), mean OCR confidence 85.6

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING

Academic Year: 2025-26
Program: B Tech/MBA Tech (AI&DS/AIML/AT)

Year: I Semester : IV
e
Subject: Signal and Image Processing
: a Time: 2.00 pm to 5.00 pm (3 bff MPSTME
Date : 14th July 2026 LIBRARY
No. of Pages: O4
Marks: 100
Re-Exam (2022-23/2023-24/2024-25/2025-26)
Instructions: 7 :

tr»

1. This question paper contains 4 pages.

2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks

4. Assume suitable data if necessary.

Ql Answer briefly:
CO-1; a_ | Perform time shifting on the following discrete time signal to determine x(n— | [04]
SO-1;
BL-3 2) and x(—n).

x[n]?
I 1

Go 1 2 an

CO-2;| b | Perform circular convolution of the sequences xi(n) = {2, 1, 2, 1} and] [04]
SO-1;

BL-3 x2(n) = {1, 2, 1, 2} using the matrix multiplication method.
CO-3; | c¢ | Explain the concept of gray level slicing. For the given 4-bit grayscale image, [04]
es perform gray level slicing without preserving the background using thresholds

Ti = 6 and T2 = 11. Show all the steps and discuss how different threshold
ranges affect image enhancement and background information loss.

IS | 11 | 6 7 8

10} 12 | 15] 3 l

. 8 {9 fs ful 12
7/5 76/8] 0
12) 3 [4] 10] 2

L
CO-5;) d_ | Discuss the concept of region merging in image segmentation and illustrate it [04]
ed) with an example
BL-3 pes .
CO-6; e | Explain motion estimation in video processing. Mention any three motion | [04]
SO-1; . . . oo, .
BL2 |» estimation algorithms used in video processing?

£

Answer any four from Q2 to Q7

RRR 7 RRR EK
--- page 2 ---
=o

Q2 a [10]

Explain the steps involved in finding-the optimal threshold using Otsu’s

CO-5;
SO-1; thresholding method for image segmentation. as
BL-2 :
CO-3; b i. Mention any three-color models used in image processing. {10]
SO-1;
BL-3 ii. Convert the RGB color value (0.2,0.4,0.7) into the CMYK color
model.
iii. | Consider the following 5x5 binary image. The origin is at the top-left
corner, and coordinates are written as (row, column) using |-based
indexing. Foreground pixels have value | (set V= {1}).
1 01 0 0
11001
7=0 010 0
01010
0000 21
Draw lines showing the connections between pixels of the same label
under: . E>
e 4-adjacency
e   8-adjacency :
Q3 a | State the commutative and distributive properties of convolution. Perform | [10]
CO-1; convolution sum of the following two sequences by tabulation method and
SO-1; .
BL-3 matrix methods.
Index (n) -2 -1 0 1
x(n) 2 2 1 2
h(n) 1 1 1 -2

CO-2; b | Given x(n) = {1, 1, 1, 1, 0, 0, 0, 0}, compute the 8-point discrete Fourier | [10]

sil; transform (DFT) using fast Fourier transform (FFT) with Radix-2.

BL-3

Q4 a | Find the even and odd components of the following signal and sketch the same. | [10]
Son Index (n) 3]2/14,/0,/1,/2|]3]4 ant
BL-3 x(n) l 2 3 4{,5|6/;7|8

CO-2;| b_ | Find the response of Linear Time Invariant (LTI) system with input, x(n) =| [10]

asl; {2,2,2}, and impulse function, h(n) = {1, 1} using decimation in time (DIT)

BL-3
with radix-2 Fast Fourier Transform (FFT).
Q5 a Consider the following images: [10]
CO-3; 10 | 10 | 10,) 10 10 | 30 | 30 | 30
SO-1; 30 | 30 | 30 | 30 10 | 30 | 30 | 30
BL-3 30 | 30 | 30 | 30 10 | 30 | 30 | 30
£ 30 | 30 | 30 | 30 10 | 30 | 30 | 30

Image | Image 2

BRK RAK 2 RRR KR K
--- page 3 ---
»4

yr

i. Apply the horizontal and vertical Sobel operators (without zero
padding) to Image | and Image 2 and compute the gradient magnitude
for both images. °

ii. Write your observations based on the results obtained in part’(i).

CO-S5; b | Consider the following grayscale image. Two seed points are selected at | [10]
ea locations (1,1) and (4,1), which are shown in bold. Assume 8-connectivity.
10 11 10 80 80
11 10 11 80 81
10 11 10 80 80
50 51 50 55 55
50 50 51 55 55
i. Apply region growing with a threshold of +2 and show the pixels
included in the segmented regions.
ii. Apply region growing with thresholds of +10 and +1, and show the
pixels included in the segmented regions.
iii.   Ilustrate the effect of small and large threshold values on segmentation
using the above results.
Q6 a | Calculate the histogram equalization of the given 3-bit image segment. Plot | [10]
CO-3; the histogram before and after histogram equalization. Analyze the histograms
SO-1; .
BL-3 and show the resultant image.
6 | 6 | 6) 6 | 6 | 6
0 5 5 5 5 0
3 | 2 2 | 2 | 2 3
3 l 1 1 1 3
3 6 7 7 | 6 3
. 3 4})4)4 |) 4 | 3
CO-1; |b | Determine whether the following signals are energy signal or power signal. [05]
SO-1; , i. x{n] = un]
BL-3 ii. _x[n] =5
CO-2; c | Calculate the discrete Fourier transform (DFT) for the signal, x(n) = {1, 1, 1, | [05]
ae 1}, using the twiddle matrix method.
Q7 a | Define the Ideal Low-Pass Filter (ILPF) in the frequency domain. Explain its | [05]
CO-3; effect on an image and discuss the occurrence of ringing artifacts. Also explain
SO-1;

the role of cutoff frequency.

FR OR HR x
--- page 4 ---
vy

BL-2

CO-4; A binary image is shown below. The Gancies of the circular gbjects are 3,5, | [05]
ae and 7 pixels. The sizes of the square objects are 9x9, 11x11, and 15x15 pixels.
i. Apply erosion to eliminate all the objects except the largest square.
Justify your answer. ;
ii. Determine the size, shape, and intensity (value) of the structuring
element required.
CO-6; Compare I-frames, P-frames, and B-frames in video compression. Write at | [05]
oe least five differences between them.
CO-6; . [05]
SO-1; Explain the Three-Step Search (TSS) method used in video processing.
BL-2

FRR RRR QR RR K
````

## 2024-25 · Final + Re-Exam · Sem 4 · paper e42a58d5cfe4

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/ARTIFICIAL INTELLIGENCE/SEM-IV/SIGNAL AND IMAGE PROCESSING/Signal and Image Processing, Sem IV, Final Exam 2024-25 & Re Exam 2022-23 and 2023-24.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12/ 5/2025
- Text: ocr (4 pages), mean OCR confidence 80.7

````text
_ SVKM’SNMIMS__
_ MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2024-2025 ;
Program/s: B Tech /MBA Tech ’ , Year: II Semester: IV
Stream/s: AV/ AIML/ AIDS ,
Subject: Signal and Image Processing
Date:12/ 5/2025

Marks: 100

Time:3 hrs @Oz00am +0 4.200pin)
No. of Pages: 3

Final Examination 2024-25/ Re-Exam 2022-23, 2023-24

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use. : ;
1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any _ 4 questions.

3) Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qu Answer briefly: om oever . _ | [20]
a | Define Sampling and sketch the following signals
i. r(n) u(2 —7n)
CO-1: ii. A discrete time signal x(n) is defined as
80-1; | 145; -3<ns-4 [5]
ecu | -   *@)=1 4". genes
: 0 ‘* elsewhere .
Determine the values of x(n) and sketch it and Sketch x(-n-4) and x(n-4)
. {b
50.1, | _ | Explain the Ideal Low-Pass Filter (LPR) and the Butterworth Low:Pass Filter (BLPP) in ey
i? detail. :
BL-3 ‘ A
c | Original image A:
0 {0/0 |0 {0 |0 [0 Jo
Oo j|o |o {1 {1 {1 [o [o
0 {0 |i 1 1 {1 |0 |0
CO-3; Oo {1 [1 |1 {1 J|0 [0 Jo
SO-1; Oo {1° /1 |1 [0 {0 Jo 0 [5]
BL-3 Oo |1 {1 {1 {0 |o [0 To .

Structuring Element B:
--- page 2 ---
x 1 %

1 1 1

x 1 x |- .
Define dilation and erosion morphological operation in image processing. Per:
the image A using the structuring element B given. Comment on the results obtained.

form erosion on

a Compare P-frames and B-frames in terms of their role in video compression. Discuss their [5]
BL2 _adyantages and disadvantages. . .
CO-1: Define convolution sum with equation. Compute the linear and circular convolution of the two
“SO-1: sequences { 2, —1, 3, 0} and {1,2,-1,2}. Write the differences between linear and circular | [10]
; convolution.
BL-3 ;
b | (i) What is contrast stretching and perform contract stretching of a given 6x6 image. Consider
rl=1, s1=2, r2=5 and s2=6. Note: The location of the points (rl, s1) & (r2, s2) control the
shape of the transformation function. :
(ii) Calculate image negative and log transformation of the given image
a Pale 77573 )11,7 | 2 |
SO-1: 1 2 \ 1 2 1 5 ‘ [10]
BL-3 6 4 6 5 6 1 :

(i) Given an image patch of 8 Gray levels and perform the
Is 2 3 4 Laplacian filter (without diagonals), horizontal and vertical
Sobel edge detector without zero padding: Find the

1 1 3 7 3. magnitude spectrum of Sobel operator.

Q3 (ii) Explain the difference between gradient-based and
C02: : ; Laplacian-based edge detection methods.
SO-1; ;
BL-3

(10)

4 1 5 | 5 Z

@ fe For video processing, (i) Explain the two-dimensional logarithmic search method for block

hd searching between two video frames. (ii) Write the advantages and disadvantages of this | [10]
BL2. method. : ; ;

Q4 a | Determine whether the following systems y1(n) and y2(n) are

CO-1; (i) Static/dynamic (ii) causal/noncausal (iii) linear/nonlinear (iv) time-invariant/time-varying [10]
SO-1; - (v) BIBO stable/unstable , :

BL-3 yl(n) = cos(x(n)) and y2(n) =2 n? x(n) +n x(n-1)

2
--- page 3 ---
b. | @) Explain the neighbourhood and adjacency of pixels and their types in digital image
processing. :

(ii) According to the following intensity values of a 5X5 image, show the paths by drawing
dashed lines from p to q for 4-adjacéncy and 8-adjacency. let V={1,2,3}. Find the D4 and D8

Q4 distances between pixel “p” and “q”. _- : .
CO-2; i : .
SO-1; -_ [10]
BL3 2(p) | 3} 2 6 | 1
6 2.| 3 6 2
5 3 2} 3 5
2 4 3 5 2
4 5| 2 3_ | 1@
a 3: as Explain the first-order and second-order edge detection methods. Find the first and second
S0-2; order derivatives of the given scan line and write the observation. : f10]]
pes | |L2171 71716] s[4]3[2]1[il/ijil7 [717]
Q5 b : .
CO-1; Find the linear convolution of the two sequences x1(n) = { 1, 1} and x2(n) = { 1, 1, 2, 1} [10]
SO-1; using DFT and IDFT method. . . .
BL-3 :
Q6 a ? .
CO-1; Compute the DFT of the finite length sequence x(n) = {1, 2, 1, 1, 0, 1, 0, 0} using direct [10]
SO-1; method. Plot the magnitude spectrum. .
BL-3 : :
; b (i) Perform region growing on the following image. 1 2 3 4
Q6 Consider initial point at (3,3), threshold value 2 an 1: 0 1 5) 0
CO-4; 4-connectivity. : 2 5) 5 = 6 1 [10]
SO-1; (ii) Perform region splitting on the following image. 3 1 : 4 7 3 ,
BL-3 Assume threshold value <=6. .
i 4 0 2 5 1
Q7 a a ; DE
CO-1; Compute the IDFT of the sequence X(k) = { 7, -0.707-0.707j, -j, 0.707-0.707j, 1, 0.707+0.707j, [10]
SO-1; j, -0.707+0.707)} using DIT FFT method
BL-2 a
b Explain the concepts of morphological opening and closing. What are their effects on binary
images? Perform closing operation to the given binary image.and with the given structure
| element of all 1’s. é ;
7 0 0 0 0 0 0 0
CO-3: 0 0 0 1 1 1 0
SO-1; ~O f of 1 fayi fifo 1 [10]
BL3 | ‘ifoyat)1)attitto le 1
ofifij]i|.o}oy]o !
--- page 4 ---

````

## 2023-24 · Final + Re-Exam · Sem 4 · paper a984c033e8ff

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/ARTIFICIAL INTELLIGENCE/SEM-IV/SIGNAL AND IMAGE PROCESSING/Signal and Image Processing, Sem-IV, Final & Re Exam 2022-23.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 83.8

````text
AL,

SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2023-2024
Program/s: B Tech/MBA Tech Year: II Semester: IV
Stream/s ;AI/AIML/AIDS

Subject: Signal and Image Processing : Time: 3 hrs (fozocamto Leoopm
Date:_2> / 04 / 2024 No. of Pages: 4
Marks: 100

Final Examination/Re-Examination (2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

von 1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any __4 __ questions.
3) Inall__5_ questions to be attempted.
4) All questions carry equal marks. .
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
a. Consider a discrete time signal x(n) = {2,—1,0, 2,1, 1, 0}.
t
cule Determine the following signals and represent them graphically. [05]
BL-3 i. = =yy(n) =x(n—- 3) x(1—-n)
7 ii, =y,(n) = x(n— 3) d(m—- 2)
@ CO-2 ; b. With reference to grey scale images, explain the concept of point processing
a 2 and neighborhood processing techniques. (091
CO-3 ; c. Explain the concept of dilation and erosion operation with reference to
_ : morphological operations es
CO. 4: Describe the concept of inter frame, intra frame and bidirectional frame with
SO- 1; reference to digital video processing. Which type of frame require lowest [05]
BL-2

number of bits for encoding?
--- page 2 ---
Apply linear convolution y (n) = x(n) * h(n) of the following signals

Q2 using matrix method. Verify the results using fold-shift-multiply-sunt
CO-1; method. [10]
SO-1;
BL-3.4 x(n) = {—2,0,-1} and h(n) = {4,1,3}
Sketch the masks for Robert , Prewit and Sobel operators and give
significance of each. Apply a suitable Sobel mask to detect the edge in the
image given below
es 50 [50 [50 | 100 | 100 | 100 0
BI 3 50 50 50 100 | 100 | 100 [10]
“ 50 50 50 100 | 100 | 100
50 50 50 100 | 100 | 100
50 50 50 100 | 100 | 100
50 50 50 100 | 100 | 100
Solve the 4-point DFT X(k) for the sequence x(n) = 2+ sin" using
Q3
CO-1: twiddle factor matrix method. [10]
SO-1; On X(k) obtained above, apply IDFT using radix 2 DIT FFT algorithm to
BL-3 . oe
retrieve original sequence x(n).
Write short note on-
CO-2; i. Any two colour models.
SO-1; . ; ; ; wa [10]
BL-2 ii. Contrast stretching technique for image enhancement with suitable
example.
Q4 Demonstrate circular convolution using graphical method on the following
oe two sequences- x,(n) = {1, 2,0, 1} and x2(n) = {2, 2,1, 1} for N=4. [10]
BL-3.4 Verify the result using matrix method.
CO-3: With reference to region based segmentation, explain region growing, and
SO-1; region splitting techniques with the help of suitable examples. Draw quad | [10]
BL-2

tree for region splitting technique.

—
--- page 3 ---
@

a

2

Apply histogram equalization on the image given below. Plot the histogram

of the image before and after equalization. Plot the transformation function.

Q5 Draw the new image. Comment on the result obtained.
CO-2; [10]
SO-1; 6|6|7)|7 | 6
BL-3,4,5 5 |2]2]3/4
3 | 3 | 4] 4 1] °5
5 | 7 | 3 | 6 | 2
71, 6/5 }]5 {4
Compare the following —
Soo i. DFT algorithm and DIT FFT algorithm based on number of [10]
BL-2. complex multiplications and additions using suitable example
ii. Spatial resolution and grey level resolution
Apply the Low pass and High pass filters given below on the original
image matrix to get the new images. (Use zero padding on input image).
i. Convolve the original image using Low pass filter mask to obtain
3 x 3 filtered output image.
ii. Convolve the original image using High pass filter mask to obtain
Q6 3 x 3 filtered output image.
CO-2; lii. Verify whether: High pass filtered image = Original image — Low [10]
SO-1; pass filtered image
BL-3,4,5
iv. Comment on the result obtained in (i), (ii) and (iii).
Original image LPF mask HPF mask
9 {244 1/9 | 1/9 | 1/9 1/9 | 1/9 | 1/9
4 [200] 2 1/9 | 1/9 | 1/9 1/9 | -8/9 | 1/9
2|;0]4 1/9 | 1/9 | 1/9 1/9 | 1/9 | 1/9
Soe With reference to motion estimation algorithm in video processing [10]
BL2. elaborate on exhaustive block search and 2D log search methods
--- page 4 ---
i

[ a

State & explain the following properties of DFT using relevant expressions

Q7
(i) Time Shift
CO-1; (ii) Frequency shift [10]
SO-1; (iii) Linearity
BL-2 (iv) — Convolution
b Consider an input image A and the structuring element B. Perform the
morphological operation (A @ B)©B on the input image A using the
given structuring element B. Elaborate on the operation performed.
CO-1; Image A Structuring Element B
SO-1; [10]
BL-3,4 0}0/0{0/0/0}0/0]0 Om
OJOTLIIJO} 1} 1/010
O/O}1{O}1}0} 0} 1) 0} 1 l
````

## 2023-24 · Re-Exam · Sem 4 · paper 97ed677a5775

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/ARTIFICIAL INTELLIGENCE/SEM-IV/SIGNAL AND IMAGE PROCESSING/Signal and Image Processing , Re-exam 2022-2023.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 82.1

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& EN rE
SCHOOL OF TECHNOLOGY MANAGEMENT

Academic Year: 2023-2024

Program/s: B Tech/MBA Tech Year: II Semester: IV

Stream/s ;AVAIML/AIDS :

Subject: Signal and Image Processing Time: 3 hrs (jo:qnauto_ 1+ 00pm)
Date:_3_/ 7/2024 No. of Pages: 4

Marks: 100 .

____Re-Examination (2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
7 ()" forO<n<3
Sketch the discrete time signal x(n) = }\4 =" = ° graphically.
Son > 0 otherwise [05]
et > Determine the signal y2(n) = x(n — 2) 6(n — 2) and sketch the same.
Gi b. With reference to grey scale images, explain spatial resolution and grey
SO-1 : level resolution. [05]
BL-2
CO-; c. :
SO-; Discuss the concept of image segmentation based on thresholding. [05]
BL-2
66-4 d. Explain the concept of spatial sampling, temporal sampling, inter frame
So- na coding and intra frame coding with reference to digital video processing. [05]
BL-2
--- page 2 ---
¥
a > ‘a

Determine the 4-point DFT X(k) for the sequence x(n) = {1,1,—2, -2

Q2
ee using radix 2 DIT FFT algorithm. State the advantages of DIT FFT [10)
SO-1: algorithm over DFT. Calculate the number of complex multiplications for
BL-2,3 DFT and DIT FFT algorithm for the above example.
b Solve the morphological operation (A © B) @ B on the given image A
using the structuring element B.
Elaborate on the operation performed. Comment-on the results obtained.
CO-3; Image A Structuring Element B
SO-1; [10]
BL34 0 |0 |0 {0 {0 0 {1 {0
; o {1 {1 }1 [0 1 (@|1
oO j1 fl {1 [0 oO {1 [0
Oo {1 {1 {i {0
0 {0 }0 {0 {1
a Explain region-splitting technique for region based segmentation.
Perform segmentation on the following image using region splitting
technique. Draw the quad tree. Predicate is max(x, y) — min(x,y) < 3.
Q3 4 |6 |6 |6 |7 |7 |6 |6
6 |7 |6 {7 {5 5 |4 |7
a: 6 1615 14 13.12 |5 [6 [10]
BL23 5 [4 [5 |4 {2 |6 |4 |3
> 0 {0 |2 {3 [5 |2 |4 |4
0 1 0 |o |2 |7 |3 |6
1/3 jo |1 {0 |3 |4 |4
1 {oO {1 |O {2 {3 {5 {2
b With reference to DFT properties, explain the following properties-
i Parseval’s Energy Theorem ;
CO-1; «   Periodicit
ii Periodicity propert:
SO-1; “1 - py [10]
i iii Time reversal propert:
BL2 property P

iv Linearity property
--- page 3 ---
od

—

Compute the linear convolution y (n) = x(n) x h(n) of the following

Q4
signals fold-shift-multiply-sum method. Verify the results using matrix
CO-1; 8 7 ° [10]
SO-1; method
BL-3 :
x(n) = {1,1,0,0} and h(n) = {1,2,3, 4}
Consider an 8 x 8 image for which gray level and the corresponding
frequency is as shown in table below. Plot the histogram of the image before
ena and after equalization. Plot the transformation function. Comment on the
SO-1; results obtained. [10]
,73,4,5
Gray Level (rk) o/1) 2/3) 4 |5 |6|7
Number of pixels (nx) | 9 | 8 | 11 | 4 10| 15} 4) 3
Q5
CO-1: Consider two sequences x[n]={1,0,0,1} and h[n]={0,1,0,1}. Perform 110]
SO-1; circular convolution DFT and IDFT method.
BL-3
cO-2; Write a short note on-
SO-1; i. JPEG and TIFF Colour formats [10]
BL-2 " A A . .
ii. Image enhancement using point processing technique.

Q6
CO-2;
SO-1;
BL-3

Compare spatial domain filtering techniques with frequency domain

filtering techniques.
Consider the original image matrix given below. Apply 3x3 mask to
perform the following operations in spatial domain on pixel at d;):
i. - Low Pass Filtering
ii. High Pass Filtering
iii. | Median Filtering

10 [20 | 30
40. (50 | 60 P
70 (80 [90

[10]
--- page 4 ---
i

Discuss the concept of,motion estimation and compensation with reference

CO-4; Zhe
SO-1; to digital video processing. Explain 2D log search algorithm to search | [10]
BL-2 motion vector.
Q7
co-3° With reference to image segmentation based on discontinuities, explain with [10]
SO-1; the help of suitable operators the concept of point, line and edge detection.
BL-2
With reference to discrete time signals, explain the following types of
signals-
CO-1; i Energy and Power Signals 2
SO-1; . Lo. Loe gs (10)
BL-2 ii Periodic and Aperiodic Signals
iii Symmetric and Antisymmetric Signals
iv Causal and Non-Causal Signals
>
````

## 2022-23 · Final-Exam · Sem 4 · paper 33f2d84b7089

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/ARTIFICIAL INTELLIGENCE/SEM-IV/SIGNAL AND IMAGE PROCESSING/Signal and Image Processing,Final exam 2022-23.pdf` (+1 identical copies)
- Printed on paper: max marks: 100
- Text: ocr (3 pages), mean OCR confidence 87.6

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& EN
Academic Year: 2022-2023

Program: B.Tech/MBA Tech - Year: II Semester: IV

Stream: Artificial Intelligence/ Artificial Intelligence and Machine
Learning/ Artificial Intelligence & Data Science

Subject: Signal and Image Processing Time:10:00 am-1:00 pm
Date: 29" April 2023 No. of Pages: 3
Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of the remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.

7) Assume Suitable data if necessary.

Qi a. | A discrete-time signal is given by x[n]={1, -1, 2, 0, 1, 1, 2}. Sketch the | [04]
_ SO-1 following signals t

i) x(2n+1) , ii) x(n-ld(n—-2)
CO-1,S0-1_| b. | The first five points of the 8-point DFT of a sequence x(n) are given as | [04]
ad X(k) = {0.25, 0.125 — j0.3018, 0, 0.125 — j0.0150 ,0}.
Determine the remaining 3-points using the DFT property. Discuss about
the property used.

C0-2,S0-1_ | ¢, | Define Euclidean, city block and chess board distance measures. An | [04]
BLS image segment is shown below. Let V be the set of gray level values used
to define connectivity in the image. Compute D4 , Ds, Dm distance
between pixel p and q for V=[2,3]

2(p)| 3 [2] 6] 1
6 |2|]3]|6]| 2
5 |3]2]/ 3] 5
2;4/3/5]2
4 [5]2] 3 | 6(q)

CO-3,S0-1_| d. | For enhancing details over a small area in an image, local histogram | [04]
Be processing is preferred over global histogram processing. State true or
false and justify your answer

C0-4,S0-1_| e, | Suppose the block being encoded is an 8x8 block between pixel locations | [04]

BL-2.5 (22, 40) and (29, 47). If the block that best matches it in the previous
frame is located between pixels at location (21, 39) and (28, 46), then
compute the motion vector.
--- page 2 ---
Q2 a. | Explain linear & non-linear, static & dynamic system [10]
CO-1, SO-1 . . .
BL-2,5 The discrete-time systems are given below-
i) y(n) = x(n)+ n x(n+1), ii) y(n)= x(2n)
Determine whether these systems are: linear or non-linear, static or
dynamic.
oy S0-1_ | b. | Differentiate between linear convolution and circular convolution (4 pts) [10]
” Compute the linear convolution using the graphical or fold shift multiply
method of the following signals: x(n)= {% 0, 1}, h(n)= { } 2, 1}
Q3 a. | Calculate the percentage saving in calculations in 4-point radix 2 FFT | [10]
et when compared to DFT.
’ Given: x(n) = {1,1,1,0}. Compute X(k) using DIT-FFT algorithm.
a So-1_| b. | Compute the Circular convolution of x1(n)={1,1,1,1} and x2(n)={1,1,0,0} | [10]
using DFT and IDFT method. * t
Q4 a. | Explain High Pass Filter in image enhancement. [6]
0-2, SO-1
BL-1,2
cO-2,S0-1 | b | Highlight the intensity in the range of 30-60% of the maximum value for | [4]
BESS the given image. The intensity of the remaining pixels should be made
equal to zero. Comment on the result obtained. What is this technique
called?
al 5 3 | 14 | 13
5 2 7 6 | 15
ie} e) 5 5 | 13
12] 1 7 6 | 13
2 |} 10] 10) 3 9
CO-2,S0-1 | ¢. | Discuss Histogram equalization. Perform histogram equalization on the
BL-4,5 following image. Draw the histogram before and after equalization. State
your observations about the original image and the equalized image. [10]
2 2 2 2 2
1 2 5 2 1
1 5 5 5 1
2 2 2 2 2
1 2 5 2 1
Q5 a. | Discuss region spilt and merge technique. [10]
era Perform segmentation on the following image. Apply region split and merge

technique. Draw the quad tree. Predicate is max(x, y) — min(x,y) < 3

>
--- page 3 ---
co-3,S0-1 | b. | Sketch the mask for the following operators also enlist their functionality: | [10]
BL-2,5

a) Prewitt Operator
b) Sobel Operator
c) Laplacian filter mask

Compute the effect of applying the Laplacian filter on the center 3 x 3
pixel of input image (which are highlighted)

10 10 10 10 | 10 1) 1 ]1

10 10 |10 | 10 | 10 1|-8|1

10 10 | 10 |10 | 10 1;,1]1

100 | 100 | 100 | 100 | 100 .

M
100 | 100 | 100 | 100 | 100 Hes feb
Input image

Q6 a. | Explain Motion Estimation and Motion Compensation in detail. [8]
CO-4, SO-1
BL-2

co-4,S0-1 | b. | With reference to digital video, explain the significance of inter-frames, | [4]
eee intra frames and bidirectional frames.

cO-2,50-1 | e. | Discuss the significance of image enhancement. Write transformation | [8]

Biot equations for the thresholding and image negative.
Perform thresholding with threshold (T)=5 and image negative point
processing operations on the following image. Draw the new image and
transformation graphs.
2 | 10] 10] 3 9
5 2 7 6 | 15
0 e) 13] 5 | 13
12 | 1 7 6 | 13
1 5 3 | 14} 13
Qi [20]
CO-1, CO-2, | a. (Compare between (Any 4 pts) [8]
ae i. Morphological dilation and erosion.
ii. Energy and power signal.
Co-2,S0-1 | b. | Explain in brief JPEG file format and give advantages and disadvantages. [4]
BL-2
CO-1,S0-1_| ¢, | Compare DFT and FFT (any 4 pts) [8]
Bits Find the 4-point IDFT for X(k) = {6,(—2+ 2j),—-2,(—2 — 2))} using

the twiddle-factor matrix method.
````

## 2022-23 · Re-Exam · Sem 4 · paper 9fab64e3f5d8

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/ARTIFICIAL INTELLIGENCE/SEM-IV/SIGNAL AND IMAGE PROCESSING/Signal and Image Processing, Sem-IV, Year 2022-23, Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (3 pages), mean OCR confidence 84.8

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2022-2023

Program: B.Tech/MBA Tech Year: Il Semester: IV

Stream: Artificial Intelligence/ Artificial Intelligence and Machine
Learning/ Artificial Intelligence & Data Science

Subject: Signal and Image Processing Time: 10:00 am-1:00 pm(3 Hrs.)
Date: 30/06] 2023 No. of Pages: 3
Marks: 100

Re-Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.
1) Question No. 1 is compulsory.
2) Out of rerfiaining questions, attempt any 4 questions.
a 3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql a. | A x{n] ={-0.5, 0.5, 1, 1, 1, 1, 0.5}. Sketch the following [04]
— i) x(n) u(3-n), ii) x(-n+3)
C0-1,S0-1 | b. | The first five points of the 8-point DFT of a real valued sequence x(n) are | [04]
ahs given as X(k) = (28, —4 + 9.565, —4+j4, —4 + j1.656,—4}.
Determine the remaining 3-points using the DFT property. Discuss about
the property used.
C0-2,S0-1_ | ¢. | Describe 4,8 and m adjacency. Determine the shortest 4, 8 and m path | [04]
BLa3 between p and q for given V= {0,1}.
= 3 1 | 2 | 1(q)
2 210 4
~ 1 251 1

1(p)}O}1] 1

What is thresholding in image processing? Compare local thresholding and | [04]

global thresholding used in image segmentation (any 3 pt)

CO-4,S0-1_| @, | i. With reference to video quality measures, state the expressions for | [04]

BL28 Mean Square Error and Mean Absolute Difference.

ii. The pixel values in a row of an original video frame is (240,
241,239,242] and the pixel values in a row of a reconstructed video
frame is [239,241,240,241]. Evaluate the mean square error.

co-3,50-1 | d.
BL-2
--- page 2 ---
Q2 a. | Explain time variant Invariant, causal- non causal system. i {10]

a The discrete time systems are given below-
, i) y(n) = x(-n+2) , ii) y(n)= e%(")
Determine whether these systems are: causal or non-causal, time-variant
or invariant.
ey S0-1 | b. | Explain energy and power signal. Find the energy and power of the | [10]

following signal.

i) x(n) =u(n) ii) x(n) = (5) men

Q3 a. |i. Calculate the number of complex multiplications and addition needed in | [10]

re the calculation of DFT and FFT with a 4-point sequence.
‘ ii, Given: x(n) = {1,2,3,4}. Compute X(k) using the DIT-FFT algorithm.
ne S0-1 | b. | Compute the Circular convolution of xi(n)= % 1,1,1} and xa(n)={1,0,1,0] | [10]
; using DFT and IDFT method. ,
Q4 a. | What is Image Enhancement in image processing? Enlist different types of | [6] | —~
oe point processing techniques. Explain any one-point processing technique
‘ . | in detail.
nea b | Perform median filtering the on center pixel (which is highlighted in the | [4]

input image) using a 3X3 mask on the following image. Comment on your
observations.

1/2]2/]2]2
3/2]/2]5] 2 t
1 | 2/414] 2] 2
3 {22/3 |] 3] 2
o{2/3 {2/4

CO-2,S0-1_ | ¢. | What is Histogram equalization? Perform histogram equalization on the

a following image. Draw the histogram before and after equalization. State | [10]
your observations about the original image and the equalized image.
1{/1]1f/1]1 _
1 i 1 1 1
2 5 5 5 2
2 2 5 2 2
2 2 5 2 2
Q5 a. | What is image segmentation? Explain region splitting technique. Perform
et segmentation on the following image using region splitting technique.

Draw the quad tree. Predicate is max(x,y) — min(x,y) < 3 [10]
--- page 3 ---
[10]

C0-3,50-1 | b. | Compare morphological Dilation and Erosion (3 points).
BL-2, 5 j
For the given binary image determine the output of this morphological
equation (A © B)@B using the given structuring element. Comment on
the operation performed. '
oloj/ojojo;/ojo}o0}0|0
oloj1j/1j1}/1}/1}1),0|0 1
oloj1j/1}/1/1/1}1/0|0 @)
O{o}1}a}4j4j4j41/olo Structuring element B
olfoj1}/1}/1{/1}1}1,0]0
0/0;/0;0}/0/1{0};0|0|,0
o/o}/o;/o0{0}1{0},0|0/0
o}oj/1j}/1}1};1{/1}1},0]0
oloji}/t}ajajijr1j{oj}o
oloj/ojojojo|o{|o}o]o0
Original Image A
Q6 a. | Discuss 2D Log search method with reference to digital video processing. [8]
CO-4, SO-1 .
BL-2
C0-4,S0-1 | b. Discuss digital video processing. Describe the three types of video frames- {4]
Be |, Pand B.
c0-2,50-1 | ¢. | Perform intensity level (gray level) slicing on a 3-bit original image. Let ra = [8]
Ba 3 & r2 = 5. Draw the modified image using with background & without
background transformation.
2 1 2, 2 1
2 3 4 5 2
6 2 7 6 0
2 6 6 5 1
0) 3 2 2 1
Qi a. | Differentiate between ( 4 marks each) [20]
0-1, CO-2, i. Image sampling and quantization. {12]
30 ii. Morphological opening and closing.
BL-2 vee .
iii.. Even or odd signal.
co-1,S0-1 | b. | Justify: DFT is slow as compared to FFT [8]
BL-4,5

Find the 4-point DFT for x(n) = cos=t using the twiddle-factor matrix

method.
````

## 2021-22 · Exam not stated · Sem 4 · paper 9acfc20b42e4

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/ARTIFICIAL INTELLIGENCE/SEM-IV/SIGNAL AND IMAGE PROCESSING/B Tech, Artificial Intelligence, Signal and Image Processing, 2nd Year, Sem-IV, F_735cece6.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 20 April 2022
- Text: ocr (5 pages), mean OCR confidence 81.3
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
é
/

SVKM’s NMIMS ren :
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGIN

MPSTME ~
uti a

/ Academic Year: 2021-22

Programme: B.Tech Artificial Intelligence Year: II Semester: IV

Subject: Signal and Image Processing

Marks: 100

Time: 10.00 am to 1.00 pm
Durations: 3 (hrs)
No. of Pages:_ OS

Date: 20 April 2022

; Final Examination
e Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover

of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.
2) Out of remaining questions, attempt any__4 _ questions.
3) In all__5_ questions to be attempted.
*-4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume suitable data if necessary.

Ql a. A discrete time signal is defined as [04]
CO-1 | 1+5for—3<n<-1

SO-1 x(n) = <n<

BL-I 1for0<n<3

0 otherwise
Sketch the following discrete time signals

i. x(n)u(n)
ii, x(n)d(n — 2)
Co- | b The first five DFT coefficients of a real eight point sequence x(n) are [04]
SO-1
BL-3 X(0) = 2,X() = 3 +j,X(2) = 24 3j,X(3) = —j,X(4) = 4
el Find the remaining coefficients X(5), X(6), X(7) using DFT property.

Discuss the property used.
--- page 2 ---
Co-2 c. Define Euclidean, city block and chess board distance measures. Find | [04]
SO-1

BL-13 De, D4 and Dg distanced between points p and q for the following image.
2(q) 1 2 3 1
2 2 0 2 2
1 2 1 1 1
1 0 2(p) 2 3
1 2 1 1 [2
| CO-3 d. Define morphological opening and closing with the help of appropriate | [04]
SO-1 F 5 ; , :
BL-1 expressions. State properties of morphological opening and closing
CO-4 e Explain intra frame coding and inter frame coding with reference to digital | [04]
a video.
Q2 a Compute 8 point DFT of the sequence x(n) = {2,0, —2, 0,2,0, —2,0}, to [10]
Co-1 obtain X(k) using DIT FFT algorithm.
SO-1 ;
BL-3
CO-2 b Perform histogram equalization on the image given below. Plot the [10]
an histograms of the image before and after equalization. Plot the

transformation function. Draw the new image. Comment on the results
obtained after equalization.

2 1 1 2 1

0 2 5 1 1

0 1 2 2 6
--- page 3 ---
Q3 a Explain Exhaustive Search Block Matching motion estimation algorithm [10]
Co-4 and Hierarchical Block Matching motion estimation algorithm
SO-1
BL-2
CO-4 b Explain the significance of digital video quality measures. [06]
a Define the following objective quality measurement metric with reference
to digital video
i. Mean Square Error
ii. Peak Signal to Noise Ratio
iii. | Mean Absolute Difference
CO-2 c Explain intensity resolution and spatial resolution with reference to a grey | [04]
aan scale image.
Q4 a For the image given below, obtain the new image using [10]
CO 2 i. Power law transformation using c = 1 and gamma (y) = 0.5
Od ii. Log transformation using c = 1
0 0 10 |10 |20 |20 | 255 | 255
0 0 10 |10 |20 |20 | 255 | 255
255 | 255 | 255 | 255 | 175 | 175 | 200 | 200
255 | 255 | 255 | 175 | 175 | 255 | 255 | 255
255 | 255 | 0 0 0 255 | 255 | 255
20 |20 |20 |20 |20 | 255 | 255 | 255
0 0 10 |10 |20 |20 | 175 | 175
Draw the new image for both the operations and comment on the results
obtained.
co 1 Explain causal-non causal, and linear-nonlinear systems. [10]
BLD. 5 b Determine whether

i. y(n) = 2x(m) — 3 is linear or non linear

ii. y(n) = x(—n) is causal or non-causal

is
--- page 4 ---
Q5 a Explain morphological dilation and erosion with appropriate expressions. | [10]
CO-3 Perform dilation on the image A using the structuring element B given
BL, 4 below. Draw the dilated image. Comment on the results obtained.
' Original image A Structuring
element B

0 ;0 |0 |}0 |0 }0 |}0 }0 JO |0 1

0 ;0 |0 |0 ;0 }0 ;}0 |0 |0 0 1 1

0 |;0 ;1 |1 |1 |1 J1 J1 JO JO

0/0 }1 }1 |1 [1 41 ~ 41 :=10 [0

0 |;0 |1 /1 |0 {0 |1 |1 70 JO

0/0 }1 }/1 |0 |/0 |1 J|1 40 JO

0/0 }1 }]1 J1 |1 41 41 70 JO

0/0 }1 |]1 J1 Jt f1-j1 [0 JO

0/0 {0 |0 |]0 |0 |0 J}0 |0 J0

0/0 ;0 |}0 ;0 |0 }0 J|0 |0 JO
COo-1 b Cousider the following two 4-point sequences [10]
SO-1 1
BL-3 x(n) = cos (5n) and h(n) = 2”

Obtain circular convolution of these two sequences using matrix method.

Q6 a Explain image segmentation based on discontinuities. Apply a suitable [10]
CO-3; mask to detect the vertical line in the image given below. Draw the new
eee image.

0 0 0 10 |0 0 0

0 0 0 10 |0 0 0

0 0 10 10 10 | 0 0

0 0 0 10 |0 0 0

0 0 0 10 |0 0 0
--- page 5 ---
CO-2; b Explain image smoothing using frequency domain filters [06]
SO-1
BL-2

CO-1; c . Let x(n) = {1,2, 3 , 4,5,6}. Sketch the following signals derived from x(n) | [04]
SO-1 F
BL-3 i. y,(m) = x(-n- 2)

ii, y(n) = x(2n)
````

## 2021-22 · Re-Exam · Sem 4 · paper 301d9c0b8c29

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/ARTIFICIAL INTELLIGENCE/SEM-IV/SIGNAL AND IMAGE PROCESSING/Signal and Image Processing, Sem-IV, Re-Exam, Year 2021-22.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 June 2022
- Text: ocr (5 pages), mean OCR confidence 84.2

````text
/ bd
* SVKM’s NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT &
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINE!

Academic Year: 2021-22

Programme: B. Tech Artificial Intelligence Year: II Semester: IV
Subject: Signal and Image Processing

Marks: 100
Date: 11 June 2022 Time: 10.00 am to 1.00 pm

Durations: 3 (Hrs)
No. of Pages: ©

Re-Examination (2021-22) _

Instructions: Candidates should read carefully the instructions printed on the ‘cguesticn paper oul on the cover
of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume suitable data if necessary.

Ql a. Sketch the following discrete time signals [04]
i. Unit step
CO-1 gs #3
SO-1 ii. Unit ramp
BL-1 iii. Unit impulse
n

iv. xm= () foralln
Co- 1 b Use the DFT property to obtain zero frequency term F(0,0) for me * given [04]
SO-1 image (Do not implement DFT). State the property used.
BL-3

22 2 2

1 fl it fl

1 jl jl jl

22 2 2

1
--- page 2 ---
Define Euclidean, city block and chess board distance measures. Find | [04]

CO-2 Cs
a De, D4 and Dg distanced between points p and q for the following image.

3 1 2 1(q)

2 2 0 2

1° 2 1 1

1(p) 0 3 2
CO-3 d. Write expressions for the following morphological operations on a binary | [04]
a image

i. Translation

ii. Reflection

iii. Dilation
iv. Erosion
CO-4 e Explain objective digital video quality measures [04]
SO-1
BL-2
Q2 a Compute 8 point DFT of the sequence x(n) = { 1,0, -1, 0,1,0, —1,0}, to [10]
CO-1 obtain X(k) using DIT FFT algorithm.
SO-1
BL-3
CO-2 b Perform histogram equalization on the image given below. Plot the [10]
an histograms of the image before and after equalization. Plot the

transformation function. Draw the new image. Comment on the results
obtained after equalization.

0 1 2. 2 6

2 1 1 2 1

1 3 4 3 3
--- page 3 ---
Q3 a Explain motion compensation and estimation with reference to video [10]

CO-4 compression algorithms. Assume that the 8x8 block being encoded in the
5 current frame is between pixel locations (21,37) and (28,44) best matches
with the block in the previous frame located between (21,43) and (28,50).
Obtain the motion vector.
CO-4 |b Explain intra frames, predictive frames and bidirectional frames and [06]
; =e discuss the significance of each type with reference to video processing.
sd CO-2 c Explain spatial resolution and grey level resolution with reference to a grey | [04]
a scale image.
Q4 a Given below is a 5x5 image, LPF mask and HPF mask. [10]
CO 2
oO : 6 i. Operate on central 3x3 pixels of the original image using the mask,

1 to obtain 3x3 image as output 1

ii. | Operate on central 3x3 pixels using mask 2 to obtain 3x3 image as
output 2

iii. | Using outputs, verify whether original image = output | image +
output 2 image

iv. Comment on the result obtained in (i), (ii) and (iii) above.

Original image Mask 1 Mask 2
6 |5 {12 | 12 3 1/9 | 1/9 | 1/9 1/9 | 1/9 | 1/9
14 | 12 |13 | 10 |9 1/9 | 1/9 | 1/9 1/9 | -8/9 | 1/9
10 |15 }4 |10)6 1/9 | 1/9 | 1/9 1/9 | 1/9 | 1/9

8 |3 |7 |4 |7
8 |}3 }10}8 45
--- page 4 ---
Explain linear-nonlinear, time variant-time invariant systems

[10]

So. Determine whether
BL-2,5 i. y(n) = x?(n) is linear or non linear
ii, y(n) = x(n) + x(n — 1) is time variant or time invariant
Q5 Perform operation (A © B)®B) on the following image with the given [10]
CO-3 structuring element. Draw the new image obtained. What is this operation
na 4 called? Comment on the results
Image A Structuring Element

0/0}0/0/0j/0|0|0 j0/0 B

0/0}0/0/0}0j,0|0]0|0

0/1{}141j)0/0j;1/1 4140

O/1/14)1j)0/0]1}1/1/0 1

Oj1 [1 j}1]/1/1 4141/1 /0 O}

0/1}1/1/0]0j,1{/1 4140

O/1/141j}0}/0}1 41 41)0

0/0};0;0/0/0j{0/0/0 10

0/0/0/}0/0j0j|0/0/0|0

0/0}0/0/0}0j,0{0]|0 40
Co-1 Perform 4-point circular convolution of the following two sequences using | [10]
SO-1 :
BL-3 graphical method.

x1(n) = {1,2,2}
X2(n) = {1,2,3,4}

Q6 Explain image segmentation based on discontinuities. Apply a suitable [10]
CO-3; mask to detect the horizontal line in the image given below. Draw the new
SO-1 oo
BL23 image.

0 0 0 10 |0 0 0
0 0 0 10 |0 0 0
0 10 10 10 10 10 | 90
0 0 0 10 | 0 0 0
0 0 0 10 |0 0 0

‘/s
--- page 5 ---
CO-2;
SO-1
BL-2

b

Explain image sharpening using frequency domain filters [06]

CO-1;
SO-1
BL-3

Cc

Let x(n) = {1,2,3, 4,5,6}. Sketch the following signals derived from x(n) | [04]
j

-i y(n) =x(n- 3)
ii, y(n) =x(-n+ 1)
````
