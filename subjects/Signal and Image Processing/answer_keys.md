# Signal and Image Processing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 7f10b8f97751

- Departments: AI and Data Science, Artificial Intelligence
- Programmes: BTech AIDS 7056, MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AIDS_7056/Signal and Image Processing/ANS_Signal and Image Processing(702AI0C033)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Signal and Image Processing
Date: 11 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
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
Ans. x(n)={2, 0, 1, 2, 1}
↑
a) {2, 0, 1, 2, 1}
↑   [02]
b) {1, 2, 1, 0, 2}
[01]
↑
c) {4, 0, 2, 4, 2}   [01]
↑
CO-2;   b   Briefly discuss the following two properties of Discrete Fourier Transform   [04]
SO-1;
(DFT): linearity and periodicity.
BL-2
Ans.
[02]
[02]
CO-3;   c   Explain the effect of digital negative transformation on histogram   [04]
SO-1;
redistribution using the image below.
BL-3
3   2   4   5   1
4   5   6   7   1
3   4   2   1   0
4   5   1   2   3
7   6   5   4   1
********** 1 **********
--- page 2 ---
Ans.   S = 7 − r
4   5   3   2   6
3   2   1   0   6
4   3   5   6   7
3   2   6   5   4
0   1   2   3   6   [2.5]
Digital negative reverses intensity levels.
Dark pixels → bright, and Bright pixels → dark
[1.5]
Histogram is reflected about the center.
CO-4;   d   Illustrate the concept of morphological opening operations on binary images.   [04]
SO-1;
Explain the process step-by-step, including intermediate steps.
BL-3
Ans. Opening Operation:
• Defined as erosion followed by dilation using the same structuring
element.
• It removes small objects, noise, and thin protrusions while preserving   [02]
the shape of larger objects.
• Example: A binary image containing a large object with small isolated
white noise pixels. After Opening Small noise pixels are removed. The   [02]
main object remains unchanged in shape and size.
CO-6;   e   Briefly explain the significance of motion vectors and residuals in motion   [04]
SO-1;
estimation.
BL-2
Ans. Ate least two key points are expected on motion vectors and residuals. Each
for 1 mark.
Motion Vectors (MV):
• Represent the displacement of a block from one frame to another
• Capture the temporal redundancy in video sequences
• Used to predict the current frame from a reference frame
• Reduce the amount of data needed → improves compression
efficiency   [02]
•   Essential in video coding standards like MPEG and H.26x
Residuals (Prediction Error):
•   Difference between the actual block and the predicted block using
motion vectors
• Represent the remaining information not captured by motion
estimation   [02]
• Usually contains fine details and texture information
• Encoded and transmitted to reconstruct the original frame accurately
********** 2 **********
--- page 3 ---
Answer any four from Q2 to Q7
Q2   a   Consider the following grayscale image.   [10]
CO-5;   For homogeneity, (max intensity − min intensity) ≤ T.
SO-1;
BL-3
i.   Use region splitting (quadtree approach) with threshold T = 5. Show
image matrix with regions.
ii.   If the threshold is increased to T = 10, show how this change affects
the number of final regions.
iii.   If entire image is homogeneous, determine the threshold and justify
your answer.
Ans.   i)   For entire 4×4 image, (max intensity − min intensity) = 63-11 = 52.
Image is not homogeneous. Splitting into four 2×2 blocks results in
regions corresponding to:
• Top-left cluster (low intensities ~11–14)
• Top-right cluster (low intensities ~11–13)
• Bottom-left cluster (high intensities ~60–63)
• Bottom-right cluster (high intensities ~58–63)
• Each 2×2 block has (max − min) ≤ 5 → homogeneous → no further
splitting.
• Final number of regions = 4.   [06]
ii)   Increasing threshold to T = 10 would keep all four regions unchanged
[02]
but reinforces homogeneity and avoids unnecessary splits.
iii)   Threshold >52. Difference of pixels is <= 52. All pixels will be   [02]
homogeneous.
CO-3;   b   Compute shape and size for a 3-channel image consisting of 232 rows, 425   [10]
SO-1;
columns, and 8 bits per pixel. Also, find the number of possible colors for
BL-3
this image.
Write the key advantages of binary, grayscale, and color images, and their
applications.
Ans. Shape = 232 × 425 × 3 = 2,95,800 pixels   [1.5]
Size = 232 × 425 × 3 × 8 = 23,66,400 bits   [1.5]
No. of possible colors = 28×3 = 224 = 16,777,216 = 16.7 million   [01]
********** 3 **********
--- page 4 ---
Binary Images (1-bit): Very small storage requirement, Fast processing,
Useful for document scanning, OCR, segmentation tasks.   [02]
Grayscale Images (8-bit): Simpler than color images, Lower computational
cost, Retains intensity information,
Useful for: medical imaging, edge detection, pattern recognition   [02]
Color Images (like RGB): Rich visual information, better human perception
Useful for: object detection, classification, real-world scene understanding   [02]
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
Ans   i.   𝑥𝑒[𝑛] = {−2, 1, 0, 1, −2}   and   𝑥𝑜[𝑛] = {0, 0, 0, 0, 0}   [3.5]
↑   ↑
[03]
ii.   𝑥𝑒[𝑛] = {2, 2, 1, 2, 2}   and   𝑥𝑜[𝑛] = {0, 0, 0, 0, 0}
↑   ↑
[3.5]
iii.   𝑥𝑒[𝑛] = {0, 0, −4, 0, 0}   and   𝑥𝑜[𝑛] = {−1, −3, 0, 3, 1}
↑   ↑
CO-2;   b   Find the circular convolution of the following two sequences using DFT-   [10]
SO-1;
IDFT method.
BL-3
𝑥1(𝑛) = {0, 2, 1, 0}   and   𝑥2(𝑛) = {2, 1, 0, 0}
Ans   𝑥(𝑘) = (𝑊𝑁 𝑘𝑛) . 𝑥(𝑛)   [01]
1 1   1   1   0   3
1 −𝑗 −1   𝑗   2   −1 −𝑗2
𝑥1(𝑘) = [   ]   . [ ] = [   ]
1 −1 1 −1   1   −1
1   𝑗 −1 −𝑗 4×4 0 4×1   −1 + 𝑗2 4×1   [02]
1 1   1   1   2   3
1 −𝑗 −1   𝑗   1   2 −𝑗
𝑥2(𝑘) = [   ]   . [ ] = [   ]
1 −1 1 −1   0   1
1   𝑗 −1 −𝑗 4×4 0 4×1   2 + 𝑗 4×1   [02]
𝑌(𝑘) = 𝑥1(𝑘) . 𝑥2(𝑘)
********** 4 **********
--- page 5 ---
𝑌(𝑘) = [3, (−1 −𝑗2), −1, (−1 + 𝑗2)] . [3, (2 −𝑗), 1, (2 + 𝑗)]
𝑌(𝑘) = {9, (−4 −𝑗3), −1, (−4 + 𝑗3)}
[02]
1   ∗
𝑦(𝑛) =   . (𝑊𝑁 𝑘𝑛)   . 𝑌(𝑘)
4
1 1   1   1   9   0
1 1   𝑗 −1 −𝑗   −4 −𝑗3   4
𝑦(𝑛) =   . [   ]   . [   ] = [ ]
4 1 −1 1 −1   −1   4
1 −𝑗 −1   𝑗 4×4 −4 + 𝑗3 4×1   1 4×1   [03]
Q4   a   Identify whether the following systems are static or dynamic and causal or   [10]
CO-1;
non-causal. Justify your answer.
SO-1;
BL-3   i.   𝑦[𝑛] = 𝑥[5𝑛]
ii.   𝑦[𝑛−9] + 𝑢[𝑛+ 1] = 𝑥[2𝑛]
iii.   ℎ[𝑛] = 𝑢[𝑛−1] + 6
Ans.   i.   𝑦[𝑛] = 𝑥[0.5𝑛]
Dynamic (has memory)
Non-causal, uses future values for some n.   [03]
ii.   𝑦[𝑛−9] + 𝑢[𝑛+ 1] = 𝑥[2𝑛]
Dynamic (has memory)
Non-causal, uses future values for some n.   [3.5]
iii.   ℎ[𝑛] = 𝑢[𝑛−1] + 6
Dynamic (has memory)
Non-causal, 6 is present for all n.   [3.5]
CO-2;   b   Given x(n) = {1, 0, 0, 1, -1, 0, 0, -1}, compute the 8-point discrete Fourier   [10]
SO-1;
BL-3   transform (DFT) using fast Fourier transform (FFT) with Radix-2.
Ans.   Initial arrangement of sequence elements into even and odd groups is for 1
mark. Output of each pass is of for 3 marks.
********** 5 **********
--- page 6 ---
Q5   a   i.   Perform contrast stretching on the following grayscale image using   [10]
CO-3;   𝑠1 = 3 = 1.5   ,   𝑠2 − 𝑠1 = 4−3 = 1   , and   (𝐿−1) − 𝑠2 = 7−4 = 0.75
SO-1;   𝑟1   2   𝑟2 − 𝑟1   3−2   (𝐿−1) − 𝑟2   7−3
BL-3   ii.   Apply log transformation on the following image with C = 1.5 (and
logarithm of base 10). Normalize the log transformed image using the
formula 𝑠𝑛𝑜𝑟𝑚𝑎𝑙𝑖𝑧𝑒𝑑= 𝑠 × (𝐿−1)
𝑠𝑚𝑎𝑥.
5   4   2   3
7   6   0   1
1   1   7   6
2   2   4   5
Ans.
Contrast stretching:
𝑎𝑙𝑝ℎ𝑎∗𝑟   0 ≤𝑟≤𝑟1
𝑠= {   𝑏𝑒𝑡𝑎∗ (𝑟−𝑟1) + 𝑠1   𝑟1 < 𝑟≤𝑟2
𝑔𝑎𝑚𝑚𝑎∗(𝑟−𝑟2) + 𝑠2   𝑟2 < 𝑟≤𝐿−1
1.5 ∗𝑟   0 ≤𝑟≤2
𝑠= { 1 ∗ (𝑟−2) + 3   2 < 𝑟≤3
[01]
0.75 ∗(𝑟−3) + 4   3 < 𝑟≤7
r   s
0   0
1   1.5 ≈ 2
2   3
3   4
4   4.75 ≈ 5
5   5.5 ≈ 6
6   6.25 ≈ 6
7   7
********** 6 **********
--- page 7 ---
[05]
Log transformation:
1.17   1.05   0.72   0.90
1.35   1.27   0   0.45
0.45   0.45   1.35   1.27
[02]
0.72   0.72   1.05   1.17
Normalization of log-transformed image (rounded-off output):
6   5   4   5
7   7   0   2
2   2   7   7
[02]
4   4   5   6
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
Ans.   i.
********** 7 **********
--- page 8 ---
0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0   [04]
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0   [02]
[ 0 0 0 0 0 0 0 0]
ii.   During dilation, neighboring 1s spread into the hole. The hole
completely disappears (gets filled).
iii.
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1   [04]
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
[ 1 1 1 1 1 1 1 1]
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
Ans.   i.
×   ×   ×   ×
×   24   -29   ×
×   -26   30   ×
×   ×   ×   ×
ii.   [3.5]
********** 8 **********
--- page 9 ---
×   ×   ×   ×
×   24   -24   ×
×   -20   22   ×
×   ×   ×   ×
[3.5]
iii.   Median filter of size 3×3.
×   ×   ×   ×
×   2   2   ×
×   4   5   ×
×   ×   ×   ×
In the above answers ‘×’ indicates don’t care condition.   [03]
CO-1;   b   Perform convolution sum of the following two sequences by tabulation   [05]
SO-1;
method.
BL-3
Index (n)   -3   -2   1   0   1
x(n)   5   4   3   2   1
h(n)   1   2   2   2   2
Ans. Tabulation multiplications:
For n = −4,   y[−4] = x[−2]h[−2] = 5⋅1 = 5
For n = −3, y[−3] = x[−2]h[−1]+x[−1]h[−2] = 5⋅2+4⋅1 = 10+4 = 14
For n = −2, y[−2] = 5⋅2+4⋅2+3⋅1 = 10+8+3 = 21
For n = −1, y[−1] = 5⋅2+4⋅2+3⋅2+2⋅1 = 10+8+6+2 = 26
For n = 0,   y[0] = 5⋅2+4⋅2+3⋅2+2⋅2+1⋅1 = 10+8+6+4+1 = 29   [2.5]
For n = 1,   y[1] = 4⋅2+3⋅2+2⋅2+1⋅2 = 8+6+4+2 = 20
For n = 2,   y[2] = 3⋅2+2⋅2+1⋅2 = 6+4+2 = 12
For n = 3,   y[3] = 2⋅2+1⋅2 = 4+2 = 6
For n = 4,   y[4] = 1⋅2 = 2
y[n] = {5, 14, 21, 26, 29, 20, 12, 6, 2},   n = −4 to 4   [2.5]
********** 9 **********
--- page 10 ---
CO-2;   c   Find the Discrete Fourier transform (DFT) of the 1-D signal, 𝑥(𝑛) =   [05]
SO-1;
BL-3   {4,2,1,2}
Ans.   𝑥(𝑘) = (𝑊𝑁 𝑘𝑛) . 𝑥(𝑛)   [01]
1 1   1   1
1 −𝑗 −1   𝑗   [01]
𝑊𝑁 𝑘𝑛= [   ]
1 −1 1 −1
1   𝑗 −1 −𝑗 4×4
1   1   1   1   4   9
1 −𝑗 −1   𝑗   2   3   [03]
𝑥(𝑘) = [   ]   . [ ] = [ ]
1 −1 1 −1   1   1
1   𝑗 −1 −𝑗 4×4 2 4×1   3 4×1
Q7   a   Normalize the following grayscale image matrix to the range [0, 1] using the   [05]
CO-3;   formula [ 𝑥 − 𝑥𝑚𝑖𝑛   ]. Then apply the power-law (gamma) transformation
SO-1;   𝑥𝑚𝑎𝑥 − 𝑥𝑚𝑖𝑛
BL-3   with c=1 and γ=0.5. Show the final output image matrix.
2   3   4   5
2   2   2   2
1   1   1   1
4   6   7   0
Ans.
[2.5]
[2.5]
CO-5;   b   Explain why image smoothing is applied before thresholding when   [05]
SO-1;
converting a grayscale image to a binary image. Illustrate your answer with
BL-3
an example by comparing the image and its corresponding histogram before
and after smoothing.
********** 10 **********
--- page 11 ---
Ans. Image smoothing reduces noise and small intensity variations, making the
histogram more uniform and clearly separated.
This improves the effectiveness of Otsu’s method for better threshold
selection.
(2M) for without averaging
(3M) for averaging
CO-6;   c   Briefly explain any two measures of digital video quality.   [05]
SO-1;
BL-2
Ans. Each one if for 2.5 marks. Students may also include formulae in
explanation.
Reference:
Mean Squared Error (MSE): Measures the average squared difference
between original and reconstructed frames. Lower MSE indicates better
quality.
Peak Signal-to-Noise Ratio (PSNR): Expresses quality in decibels based on
MSE. Higher PSNR indicates better visual quality.
Structural Similarity Index (SSIM): Measures similarity based on
luminance, contrast, and structure. Values range from 0 to 1; higher values
mean better quality.
Video Quality Metric (VQM): Evaluates perceived video quality based on
human visual perception. Lower VQM indicates better quality.
Mean Absolute Error (MAE): Measures the average absolute difference
between original and reconstructed frames. Lower MAE means better
quality.
Bit Error Rate (BER): Measures the number of erroneous bits in
transmission. Lower BER indicates better video quality.
********** 11 **********
--- page 12 ---
Visual Information Fidelity (VIF): Measures how much visual information
is preserved in the processed video. Higher values indicate better quality.
CO-6;   d   State the advantages and limitations of the Exhaustive Search Block   [05]
SO-1;
Matching method in video processing.
BL-2
Ans. Advantages: optimal accuracy (global best match), simple implementation,
robust to complex motion and noise, consistent results.   [2.5]
Limitations: very high computational cost, slow/not suitable for real-time,
high-power consumption, redundant computations, high memory access
overhead.   [2.5]
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper e2907039e2ca

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AIML_7053/Signal and Image Processing/ANS_Signal and Image Processing(702AI0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Signal and Image Processing
Date: 11 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
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
Ans. x(n)={2, 0, 1, 2, 1}
↑
a) {2, 0, 1, 2, 1}
↑   [02]
b) {1, 2, 1, 0, 2}
[01]
↑
c) {4, 0, 2, 4, 2}   [01]
↑
CO-2;   b   Briefly discuss the following two properties of Discrete Fourier Transform   [04]
SO-1;
(DFT): linearity and periodicity.
BL-2
Ans.
[02]
[02]
CO-3;   c   Explain the effect of digital negative transformation on histogram   [04]
SO-1;
redistribution using the image below.
BL-3
3   2   4   5   1
4   5   6   7   1
3   4   2   1   0
4   5   1   2   3
7   6   5   4   1
********** 1 **********
--- page 2 ---
Ans.   S = 7 − r
4   5   3   2   6
3   2   1   0   6
4   3   5   6   7
3   2   6   5   4
0   1   2   3   6   [2.5]
Digital negative reverses intensity levels.
Dark pixels → bright, and Bright pixels → dark
[1.5]
Histogram is reflected about the center.
CO-4;   d   Illustrate the concept of morphological opening operations on binary images.   [04]
SO-1;
Explain the process step-by-step, including intermediate steps.
BL-3
Ans. Opening Operation:
• Defined as erosion followed by dilation using the same structuring
element.
• It removes small objects, noise, and thin protrusions while preserving   [02]
the shape of larger objects.
• Example: A binary image containing a large object with small isolated
white noise pixels. After Opening Small noise pixels are removed. The   [02]
main object remains unchanged in shape and size.
CO-6;   e   Briefly explain the significance of motion vectors and residuals in motion   [04]
SO-1;
estimation.
BL-2
Ans. Ate least two key points are expected on motion vectors and residuals. Each
for 1 mark.
Motion Vectors (MV):
• Represent the displacement of a block from one frame to another
• Capture the temporal redundancy in video sequences
• Used to predict the current frame from a reference frame
• Reduce the amount of data needed → improves compression
efficiency   [02]
•   Essential in video coding standards like MPEG and H.26x
Residuals (Prediction Error):
•   Difference between the actual block and the predicted block using
motion vectors
• Represent the remaining information not captured by motion
estimation   [02]
• Usually contains fine details and texture information
• Encoded and transmitted to reconstruct the original frame accurately
********** 2 **********
--- page 3 ---
Answer any four from Q2 to Q7
Q2   a   Consider the following grayscale image.   [10]
CO-5;   For homogeneity, (max intensity − min intensity) ≤ T.
SO-1;
BL-3
i.   Use region splitting (quadtree approach) with threshold T = 5. Show
image matrix with regions.
ii.   If the threshold is increased to T = 10, show how this change affects
the number of final regions.
iii.   If entire image is homogeneous, determine the threshold and justify
your answer.
Ans.   i)   For entire 4×4 image, (max intensity − min intensity) = 63-11 = 52.
Image is not homogeneous. Splitting into four 2×2 blocks results in
regions corresponding to:
• Top-left cluster (low intensities ~11–14)
• Top-right cluster (low intensities ~11–13)
• Bottom-left cluster (high intensities ~60–63)
• Bottom-right cluster (high intensities ~58–63)
• Each 2×2 block has (max − min) ≤ 5 → homogeneous → no further
splitting.
• Final number of regions = 4.   [06]
ii)   Increasing threshold to T = 10 would keep all four regions unchanged
[02]
but reinforces homogeneity and avoids unnecessary splits.
iii)   Threshold >52. Difference of pixels is <= 52. All pixels will be   [02]
homogeneous.
CO-3;   b   Compute shape and size for a 3-channel image consisting of 232 rows, 425   [10]
SO-1;
columns, and 8 bits per pixel. Also, find the number of possible colors for
BL-3
this image.
Write the key advantages of binary, grayscale, and color images, and their
applications.
Ans. Shape = 232 × 425 × 3 = 2,95,800 pixels   [1.5]
Size = 232 × 425 × 3 × 8 = 23,66,400 bits   [1.5]
No. of possible colors = 28×3 = 224 = 16,777,216 = 16.7 million   [01]
********** 3 **********
--- page 4 ---
Binary Images (1-bit): Very small storage requirement, Fast processing,
Useful for document scanning, OCR, segmentation tasks.   [02]
Grayscale Images (8-bit): Simpler than color images, Lower computational
cost, Retains intensity information,
Useful for: medical imaging, edge detection, pattern recognition   [02]
Color Images (like RGB): Rich visual information, better human perception
Useful for: object detection, classification, real-world scene understanding   [02]
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
Ans   i.   𝑥𝑒[𝑛] = {−2, 1, 0, 1, −2}   and   𝑥𝑜[𝑛] = {0, 0, 0, 0, 0}   [3.5]
↑   ↑
[03]
ii.   𝑥𝑒[𝑛] = {2, 2, 1, 2, 2}   and   𝑥𝑜[𝑛] = {0, 0, 0, 0, 0}
↑   ↑
[3.5]
iii.   𝑥𝑒[𝑛] = {0, 0, −4, 0, 0}   and   𝑥𝑜[𝑛] = {−1, −3, 0, 3, 1}
↑   ↑
CO-2;   b   Find the circular convolution of the following two sequences using DFT-   [10]
SO-1;
IDFT method.
BL-3
𝑥1(𝑛) = {0, 2, 1, 0}   and   𝑥2(𝑛) = {2, 1, 0, 0}
Ans   𝑥(𝑘) = (𝑊𝑁 𝑘𝑛) . 𝑥(𝑛)   [01]
1 1   1   1   0   3
1 −𝑗 −1   𝑗   2   −1 −𝑗2
𝑥1(𝑘) = [   ]   . [ ] = [   ]
1 −1 1 −1   1   −1
1   𝑗 −1 −𝑗 4×4 0 4×1   −1 + 𝑗2 4×1   [02]
1 1   1   1   2   3
1 −𝑗 −1   𝑗   1   2 −𝑗
𝑥2(𝑘) = [   ]   . [ ] = [   ]
1 −1 1 −1   0   1
1   𝑗 −1 −𝑗 4×4 0 4×1   2 + 𝑗 4×1   [02]
𝑌(𝑘) = 𝑥1(𝑘) . 𝑥2(𝑘)
********** 4 **********
--- page 5 ---
𝑌(𝑘) = [3, (−1 −𝑗2), −1, (−1 + 𝑗2)] . [3, (2 −𝑗), 1, (2 + 𝑗)]
𝑌(𝑘) = {9, (−4 −𝑗3), −1, (−4 + 𝑗3)}
[02]
1   ∗
𝑦(𝑛) =   . (𝑊𝑁 𝑘𝑛)   . 𝑌(𝑘)
4
1 1   1   1   9   0
1 1   𝑗 −1 −𝑗   −4 −𝑗3   4
𝑦(𝑛) =   . [   ]   . [   ] = [ ]
4 1 −1 1 −1   −1   4
1 −𝑗 −1   𝑗 4×4 −4 + 𝑗3 4×1   1 4×1   [03]
Q4   a   Identify whether the following systems are static or dynamic and causal or   [10]
CO-1;
non-causal. Justify your answer.
SO-1;
BL-3   i.   𝑦[𝑛] = 𝑥[5𝑛]
ii.   𝑦[𝑛−9] + 𝑢[𝑛+ 1] = 𝑥[2𝑛]
iii.   ℎ[𝑛] = 𝑢[𝑛−1] + 6
Ans.   i.   𝑦[𝑛] = 𝑥[0.5𝑛]
Dynamic (has memory)
Non-causal, uses future values for some n.   [03]
ii.   𝑦[𝑛−9] + 𝑢[𝑛+ 1] = 𝑥[2𝑛]
Dynamic (has memory)
Non-causal, uses future values for some n.   [3.5]
iii.   ℎ[𝑛] = 𝑢[𝑛−1] + 6
Dynamic (has memory)
Non-causal, 6 is present for all n.   [3.5]
CO-2;   b   Given x(n) = {1, 0, 0, 1, -1, 0, 0, -1}, compute the 8-point discrete Fourier   [10]
SO-1;
BL-3   transform (DFT) using fast Fourier transform (FFT) with Radix-2.
Ans.   Initial arrangement of sequence elements into even and odd groups is for 1
mark. Output of each pass is of for 3 marks.
********** 5 **********
--- page 6 ---
Q5   a   i.   Perform contrast stretching on the following grayscale image using   [10]
CO-3;   𝑠1 = 3 = 1.5   ,   𝑠2 − 𝑠1 = 4−3 = 1   , and   (𝐿−1) − 𝑠2 = 7−4 = 0.75
SO-1;   𝑟1   2   𝑟2 − 𝑟1   3−2   (𝐿−1) − 𝑟2   7−3
BL-3   ii.   Apply log transformation on the following image with C = 1.5 (and
logarithm of base 10). Normalize the log transformed image using the
formula 𝑠𝑛𝑜𝑟𝑚𝑎𝑙𝑖𝑧𝑒𝑑= 𝑠 × (𝐿−1)
𝑠𝑚𝑎𝑥.
5   4   2   3
7   6   0   1
1   1   7   6
2   2   4   5
Ans.
Contrast stretching:
𝑎𝑙𝑝ℎ𝑎∗𝑟   0 ≤𝑟≤𝑟1
𝑠= {   𝑏𝑒𝑡𝑎∗ (𝑟−𝑟1) + 𝑠1   𝑟1 < 𝑟≤𝑟2
𝑔𝑎𝑚𝑚𝑎∗(𝑟−𝑟2) + 𝑠2   𝑟2 < 𝑟≤𝐿−1
1.5 ∗𝑟   0 ≤𝑟≤2
𝑠= { 1 ∗ (𝑟−2) + 3   2 < 𝑟≤3
[01]
0.75 ∗(𝑟−3) + 4   3 < 𝑟≤7
r   s
0   0
1   1.5 ≈ 2
2   3
3   4
4   4.75 ≈ 5
5   5.5 ≈ 6
6   6.25 ≈ 6
7   7
********** 6 **********
--- page 7 ---
[05]
Log transformation:
1.17   1.05   0.72   0.90
1.35   1.27   0   0.45
0.45   0.45   1.35   1.27
[02]
0.72   0.72   1.05   1.17
Normalization of log-transformed image (rounded-off output):
6   5   4   5
7   7   0   2
2   2   7   7
[02]
4   4   5   6
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
Ans.   i.
********** 7 **********
--- page 8 ---
0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0   [04]
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0   [02]
[ 0 0 0 0 0 0 0 0]
ii.   During dilation, neighboring 1s spread into the hole. The hole
completely disappears (gets filled).
iii.
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1   [04]
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
[ 1 1 1 1 1 1 1 1]
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
Ans.   i.
×   ×   ×   ×
×   24   -29   ×
×   -26   30   ×
×   ×   ×   ×
ii.   [3.5]
********** 8 **********
--- page 9 ---
×   ×   ×   ×
×   24   -24   ×
×   -20   22   ×
×   ×   ×   ×
[3.5]
iii.   Median filter of size 3×3.
×   ×   ×   ×
×   2   2   ×
×   4   5   ×
×   ×   ×   ×
In the above answers ‘×’ indicates don’t care condition.   [03]
CO-1;   b   Perform convolution sum of the following two sequences by tabulation   [05]
SO-1;
method.
BL-3
Index (n)   -3   -2   1   0   1
x(n)   5   4   3   2   1
h(n)   1   2   2   2   2
Ans. Tabulation multiplications:
For n = −4,   y[−4] = x[−2]h[−2] = 5⋅1 = 5
For n = −3, y[−3] = x[−2]h[−1]+x[−1]h[−2] = 5⋅2+4⋅1 = 10+4 = 14
For n = −2, y[−2] = 5⋅2+4⋅2+3⋅1 = 10+8+3 = 21
For n = −1, y[−1] = 5⋅2+4⋅2+3⋅2+2⋅1 = 10+8+6+2 = 26
For n = 0,   y[0] = 5⋅2+4⋅2+3⋅2+2⋅2+1⋅1 = 10+8+6+4+1 = 29   [2.5]
For n = 1,   y[1] = 4⋅2+3⋅2+2⋅2+1⋅2 = 8+6+4+2 = 20
For n = 2,   y[2] = 3⋅2+2⋅2+1⋅2 = 6+4+2 = 12
For n = 3,   y[3] = 2⋅2+1⋅2 = 4+2 = 6
For n = 4,   y[4] = 1⋅2 = 2
y[n] = {5, 14, 21, 26, 29, 20, 12, 6, 2},   n = −4 to 4   [2.5]
********** 9 **********
--- page 10 ---
CO-2;   c   Find the Discrete Fourier transform (DFT) of the 1-D signal, 𝑥(𝑛) =   [05]
SO-1;
BL-3   {4,2,1,2}
Ans.   𝑥(𝑘) = (𝑊𝑁 𝑘𝑛) . 𝑥(𝑛)   [01]
1 1   1   1
1 −𝑗 −1   𝑗   [01]
𝑊𝑁 𝑘𝑛= [   ]
1 −1 1 −1
1   𝑗 −1 −𝑗 4×4
1   1   1   1   4   9
1 −𝑗 −1   𝑗   2   3   [03]
𝑥(𝑘) = [   ]   . [ ] = [ ]
1 −1 1 −1   1   1
1   𝑗 −1 −𝑗 4×4 2 4×1   3 4×1
Q7   a   Normalize the following grayscale image matrix to the range [0, 1] using the   [05]
CO-3;   formula [ 𝑥 − 𝑥𝑚𝑖𝑛   ]. Then apply the power-law (gamma) transformation
SO-1;   𝑥𝑚𝑎𝑥 − 𝑥𝑚𝑖𝑛
BL-3   with c=1 and γ=0.5. Show the final output image matrix.
2   3   4   5
2   2   2   2
1   1   1   1
4   6   7   0
Ans.
[2.5]
[2.5]
CO-5;   b   Explain why image smoothing is applied before thresholding when   [05]
SO-1;
converting a grayscale image to a binary image. Illustrate your answer with
BL-3
an example by comparing the image and its corresponding histogram before
and after smoothing.
********** 10 **********
--- page 11 ---
Ans. Image smoothing reduces noise and small intensity variations, making the
histogram more uniform and clearly separated.
This improves the effectiveness of Otsu’s method for better threshold
selection.
(2M) for without averaging
(3M) for averaging
CO-6;   c   Briefly explain any two measures of digital video quality.   [05]
SO-1;
BL-2
Ans. Each one if for 2.5 marks. Students may also include formulae in
explanation.
Reference:
Mean Squared Error (MSE): Measures the average squared difference
between original and reconstructed frames. Lower MSE indicates better
quality.
Peak Signal-to-Noise Ratio (PSNR): Expresses quality in decibels based on
MSE. Higher PSNR indicates better visual quality.
Structural Similarity Index (SSIM): Measures similarity based on
luminance, contrast, and structure. Values range from 0 to 1; higher values
mean better quality.
Video Quality Metric (VQM): Evaluates perceived video quality based on
human visual perception. Lower VQM indicates better quality.
Mean Absolute Error (MAE): Measures the average absolute difference
between original and reconstructed frames. Lower MAE means better
quality.
Bit Error Rate (BER): Measures the number of erroneous bits in
transmission. Lower BER indicates better video quality.
********** 11 **********
--- page 12 ---
Visual Information Fidelity (VIF): Measures how much visual information
is preserved in the processed video. Higher values indicate better quality.
CO-6;   d   State the advantages and limitations of the Exhaustive Search Block   [05]
SO-1;
Matching method in video processing.
BL-2
Ans. Advantages: optimal accuracy (global best match), simple implementation,
robust to complex motion and noise, consistent results.   [2.5]
Limitations: very high computational cost, slow/not suitable for real-time,
high-power consumption, redundant computations, high memory access
overhead.   [2.5]
********** 12 **********
````

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper af8060d4c289

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_AI_7012/Signal and Image Processing/ANS_Signal and Image Processing(702AI0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: text (12 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Signal and Image Processing
Date: 11 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 12 pages.
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
Ans. x(n)={2, 0, 1, 2, 1}
↑
a) {2, 0, 1, 2, 1}
↑   [02]
b) {1, 2, 1, 0, 2}
[01]
↑
c) {4, 0, 2, 4, 2}   [01]
↑
CO-2;   b   Briefly discuss the following two properties of Discrete Fourier Transform   [04]
SO-1;
(DFT): linearity and periodicity.
BL-2
Ans.
[02]
[02]
CO-3;   c   Explain the effect of digital negative transformation on histogram   [04]
SO-1;
redistribution using the image below.
BL-3
3   2   4   5   1
4   5   6   7   1
3   4   2   1   0
4   5   1   2   3
7   6   5   4   1
********** 1 **********
--- page 2 ---
Ans.   S = 7 − r
4   5   3   2   6
3   2   1   0   6
4   3   5   6   7
3   2   6   5   4
0   1   2   3   6   [2.5]
Digital negative reverses intensity levels.
Dark pixels → bright, and Bright pixels → dark
[1.5]
Histogram is reflected about the center.
CO-4;   d   Illustrate the concept of morphological opening operations on binary images.   [04]
SO-1;
Explain the process step-by-step, including intermediate steps.
BL-3
Ans. Opening Operation:
• Defined as erosion followed by dilation using the same structuring
element.
• It removes small objects, noise, and thin protrusions while preserving   [02]
the shape of larger objects.
• Example: A binary image containing a large object with small isolated
white noise pixels. After Opening Small noise pixels are removed. The   [02]
main object remains unchanged in shape and size.
CO-6;   e   Briefly explain the significance of motion vectors and residuals in motion   [04]
SO-1;
estimation.
BL-2
Ans. Ate least two key points are expected on motion vectors and residuals. Each
for 1 mark.
Motion Vectors (MV):
• Represent the displacement of a block from one frame to another
• Capture the temporal redundancy in video sequences
• Used to predict the current frame from a reference frame
• Reduce the amount of data needed → improves compression
efficiency   [02]
•   Essential in video coding standards like MPEG and H.26x
Residuals (Prediction Error):
•   Difference between the actual block and the predicted block using
motion vectors
• Represent the remaining information not captured by motion
estimation   [02]
• Usually contains fine details and texture information
• Encoded and transmitted to reconstruct the original frame accurately
********** 2 **********
--- page 3 ---
Answer any four from Q2 to Q7
Q2   a   Consider the following grayscale image.   [10]
CO-5;   For homogeneity, (max intensity − min intensity) ≤ T.
SO-1;
BL-3
i.   Use region splitting (quadtree approach) with threshold T = 5. Show
image matrix with regions.
ii.   If the threshold is increased to T = 10, show how this change affects
the number of final regions.
iii.   If entire image is homogeneous, determine the threshold and justify
your answer.
Ans.   i)   For entire 4×4 image, (max intensity − min intensity) = 63-11 = 52.
Image is not homogeneous. Splitting into four 2×2 blocks results in
regions corresponding to:
• Top-left cluster (low intensities ~11–14)
• Top-right cluster (low intensities ~11–13)
• Bottom-left cluster (high intensities ~60–63)
• Bottom-right cluster (high intensities ~58–63)
• Each 2×2 block has (max − min) ≤ 5 → homogeneous → no further
splitting.
• Final number of regions = 4.   [06]
ii)   Increasing threshold to T = 10 would keep all four regions unchanged
[02]
but reinforces homogeneity and avoids unnecessary splits.
iii)   Threshold >52. Difference of pixels is <= 52. All pixels will be   [02]
homogeneous.
CO-3;   b   Compute shape and size for a 3-channel image consisting of 232 rows, 425   [10]
SO-1;
columns, and 8 bits per pixel. Also, find the number of possible colors for
BL-3
this image.
Write the key advantages of binary, grayscale, and color images, and their
applications.
Ans. Shape = 232 × 425 × 3 = 2,95,800 pixels   [1.5]
Size = 232 × 425 × 3 × 8 = 23,66,400 bits   [1.5]
No. of possible colors = 28×3 = 224 = 16,777,216 = 16.7 million   [01]
********** 3 **********
--- page 4 ---
Binary Images (1-bit): Very small storage requirement, Fast processing,
Useful for document scanning, OCR, segmentation tasks.   [02]
Grayscale Images (8-bit): Simpler than color images, Lower computational
cost, Retains intensity information,
Useful for: medical imaging, edge detection, pattern recognition   [02]
Color Images (like RGB): Rich visual information, better human perception
Useful for: object detection, classification, real-world scene understanding   [02]
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
Ans   i.   𝑥𝑒[𝑛] = {−2, 1, 0, 1, −2}   and   𝑥𝑜[𝑛] = {0, 0, 0, 0, 0}   [3.5]
↑   ↑
[03]
ii.   𝑥𝑒[𝑛] = {2, 2, 1, 2, 2}   and   𝑥𝑜[𝑛] = {0, 0, 0, 0, 0}
↑   ↑
[3.5]
iii.   𝑥𝑒[𝑛] = {0, 0, −4, 0, 0}   and   𝑥𝑜[𝑛] = {−1, −3, 0, 3, 1}
↑   ↑
CO-2;   b   Find the circular convolution of the following two sequences using DFT-   [10]
SO-1;
IDFT method.
BL-3
𝑥1(𝑛) = {0, 2, 1, 0}   and   𝑥2(𝑛) = {2, 1, 0, 0}
Ans   𝑥(𝑘) = (𝑊𝑁 𝑘𝑛) . 𝑥(𝑛)   [01]
1 1   1   1   0   3
1 −𝑗 −1   𝑗   2   −1 −𝑗2
𝑥1(𝑘) = [   ]   . [ ] = [   ]
1 −1 1 −1   1   −1
1   𝑗 −1 −𝑗 4×4 0 4×1   −1 + 𝑗2 4×1   [02]
1 1   1   1   2   3
1 −𝑗 −1   𝑗   1   2 −𝑗
𝑥2(𝑘) = [   ]   . [ ] = [   ]
1 −1 1 −1   0   1
1   𝑗 −1 −𝑗 4×4 0 4×1   2 + 𝑗 4×1   [02]
𝑌(𝑘) = 𝑥1(𝑘) . 𝑥2(𝑘)
********** 4 **********
--- page 5 ---
𝑌(𝑘) = [3, (−1 −𝑗2), −1, (−1 + 𝑗2)] . [3, (2 −𝑗), 1, (2 + 𝑗)]
𝑌(𝑘) = {9, (−4 −𝑗3), −1, (−4 + 𝑗3)}
[02]
1   ∗
𝑦(𝑛) =   . (𝑊𝑁 𝑘𝑛)   . 𝑌(𝑘)
4
1 1   1   1   9   0
1 1   𝑗 −1 −𝑗   −4 −𝑗3   4
𝑦(𝑛) =   . [   ]   . [   ] = [ ]
4 1 −1 1 −1   −1   4
1 −𝑗 −1   𝑗 4×4 −4 + 𝑗3 4×1   1 4×1   [03]
Q4   a   Identify whether the following systems are static or dynamic and causal or   [10]
CO-1;
non-causal. Justify your answer.
SO-1;
BL-3   i.   𝑦[𝑛] = 𝑥[5𝑛]
ii.   𝑦[𝑛−9] + 𝑢[𝑛+ 1] = 𝑥[2𝑛]
iii.   ℎ[𝑛] = 𝑢[𝑛−1] + 6
Ans.   i.   𝑦[𝑛] = 𝑥[0.5𝑛]
Dynamic (has memory)
Non-causal, uses future values for some n.   [03]
ii.   𝑦[𝑛−9] + 𝑢[𝑛+ 1] = 𝑥[2𝑛]
Dynamic (has memory)
Non-causal, uses future values for some n.   [3.5]
iii.   ℎ[𝑛] = 𝑢[𝑛−1] + 6
Dynamic (has memory)
Non-causal, 6 is present for all n.   [3.5]
CO-2;   b   Given x(n) = {1, 0, 0, 1, -1, 0, 0, -1}, compute the 8-point discrete Fourier   [10]
SO-1;
BL-3   transform (DFT) using fast Fourier transform (FFT) with Radix-2.
Ans.   Initial arrangement of sequence elements into even and odd groups is for 1
mark. Output of each pass is of for 3 marks.
********** 5 **********
--- page 6 ---
Q5   a   i.   Perform contrast stretching on the following grayscale image using   [10]
CO-3;   𝑠1 = 3 = 1.5   ,   𝑠2 − 𝑠1 = 4−3 = 1   , and   (𝐿−1) − 𝑠2 = 7−4 = 0.75
SO-1;   𝑟1   2   𝑟2 − 𝑟1   3−2   (𝐿−1) − 𝑟2   7−3
BL-3   ii.   Apply log transformation on the following image with C = 1.5 (and
logarithm of base 10). Normalize the log transformed image using the
formula 𝑠𝑛𝑜𝑟𝑚𝑎𝑙𝑖𝑧𝑒𝑑= 𝑠 × (𝐿−1)
𝑠𝑚𝑎𝑥.
5   4   2   3
7   6   0   1
1   1   7   6
2   2   4   5
Ans.
Contrast stretching:
𝑎𝑙𝑝ℎ𝑎∗𝑟   0 ≤𝑟≤𝑟1
𝑠= {   𝑏𝑒𝑡𝑎∗ (𝑟−𝑟1) + 𝑠1   𝑟1 < 𝑟≤𝑟2
𝑔𝑎𝑚𝑚𝑎∗(𝑟−𝑟2) + 𝑠2   𝑟2 < 𝑟≤𝐿−1
1.5 ∗𝑟   0 ≤𝑟≤2
𝑠= { 1 ∗ (𝑟−2) + 3   2 < 𝑟≤3
[01]
0.75 ∗(𝑟−3) + 4   3 < 𝑟≤7
r   s
0   0
1   1.5 ≈ 2
2   3
3   4
4   4.75 ≈ 5
5   5.5 ≈ 6
6   6.25 ≈ 6
7   7
********** 6 **********
--- page 7 ---
[05]
Log transformation:
1.17   1.05   0.72   0.90
1.35   1.27   0   0.45
0.45   0.45   1.35   1.27
[02]
0.72   0.72   1.05   1.17
Normalization of log-transformed image (rounded-off output):
6   5   4   5
7   7   0   2
2   2   7   7
[02]
4   4   5   6
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
Ans.   i.
********** 7 **********
--- page 8 ---
0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0   [04]
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0   [02]
[ 0 0 0 0 0 0 0 0]
ii.   During dilation, neighboring 1s spread into the hole. The hole
completely disappears (gets filled).
iii.
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1   [04]
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
[ 1 1 1 1 1 1 1 1]
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
Ans.   i.
×   ×   ×   ×
×   24   -29   ×
×   -26   30   ×
×   ×   ×   ×
ii.   [3.5]
********** 8 **********
--- page 9 ---
×   ×   ×   ×
×   24   -24   ×
×   -20   22   ×
×   ×   ×   ×
[3.5]
iii.   Median filter of size 3×3.
×   ×   ×   ×
×   2   2   ×
×   4   5   ×
×   ×   ×   ×
In the above answers ‘×’ indicates don’t care condition.   [03]
CO-1;   b   Perform convolution sum of the following two sequences by tabulation   [05]
SO-1;
method.
BL-3
Index (n)   -3   -2   1   0   1
x(n)   5   4   3   2   1
h(n)   1   2   2   2   2
Ans. Tabulation multiplications:
For n = −4,   y[−4] = x[−2]h[−2] = 5⋅1 = 5
For n = −3, y[−3] = x[−2]h[−1]+x[−1]h[−2] = 5⋅2+4⋅1 = 10+4 = 14
For n = −2, y[−2] = 5⋅2+4⋅2+3⋅1 = 10+8+3 = 21
For n = −1, y[−1] = 5⋅2+4⋅2+3⋅2+2⋅1 = 10+8+6+2 = 26
For n = 0,   y[0] = 5⋅2+4⋅2+3⋅2+2⋅2+1⋅1 = 10+8+6+4+1 = 29   [2.5]
For n = 1,   y[1] = 4⋅2+3⋅2+2⋅2+1⋅2 = 8+6+4+2 = 20
For n = 2,   y[2] = 3⋅2+2⋅2+1⋅2 = 6+4+2 = 12
For n = 3,   y[3] = 2⋅2+1⋅2 = 4+2 = 6
For n = 4,   y[4] = 1⋅2 = 2
y[n] = {5, 14, 21, 26, 29, 20, 12, 6, 2},   n = −4 to 4   [2.5]
********** 9 **********
--- page 10 ---
CO-2;   c   Find the Discrete Fourier transform (DFT) of the 1-D signal, 𝑥(𝑛) =   [05]
SO-1;
BL-3   {4,2,1,2}
Ans.   𝑥(𝑘) = (𝑊𝑁 𝑘𝑛) . 𝑥(𝑛)   [01]
1 1   1   1
1 −𝑗 −1   𝑗   [01]
𝑊𝑁 𝑘𝑛= [   ]
1 −1 1 −1
1   𝑗 −1 −𝑗 4×4
1   1   1   1   4   9
1 −𝑗 −1   𝑗   2   3   [03]
𝑥(𝑘) = [   ]   . [ ] = [ ]
1 −1 1 −1   1   1
1   𝑗 −1 −𝑗 4×4 2 4×1   3 4×1
Q7   a   Normalize the following grayscale image matrix to the range [0, 1] using the   [05]
CO-3;   formula [ 𝑥 − 𝑥𝑚𝑖𝑛   ]. Then apply the power-law (gamma) transformation
SO-1;   𝑥𝑚𝑎𝑥 − 𝑥𝑚𝑖𝑛
BL-3   with c=1 and γ=0.5. Show the final output image matrix.
2   3   4   5
2   2   2   2
1   1   1   1
4   6   7   0
Ans.
[2.5]
[2.5]
CO-5;   b   Explain why image smoothing is applied before thresholding when   [05]
SO-1;
converting a grayscale image to a binary image. Illustrate your answer with
BL-3
an example by comparing the image and its corresponding histogram before
and after smoothing.
********** 10 **********
--- page 11 ---
Ans. Image smoothing reduces noise and small intensity variations, making the
histogram more uniform and clearly separated.
This improves the effectiveness of Otsu’s method for better threshold
selection.
(2M) for without averaging
(3M) for averaging
CO-6;   c   Briefly explain any two measures of digital video quality.   [05]
SO-1;
BL-2
Ans. Each one if for 2.5 marks. Students may also include formulae in
explanation.
Reference:
Mean Squared Error (MSE): Measures the average squared difference
between original and reconstructed frames. Lower MSE indicates better
quality.
Peak Signal-to-Noise Ratio (PSNR): Expresses quality in decibels based on
MSE. Higher PSNR indicates better visual quality.
Structural Similarity Index (SSIM): Measures similarity based on
luminance, contrast, and structure. Values range from 0 to 1; higher values
mean better quality.
Video Quality Metric (VQM): Evaluates perceived video quality based on
human visual perception. Lower VQM indicates better quality.
Mean Absolute Error (MAE): Measures the average absolute difference
between original and reconstructed frames. Lower MAE means better
quality.
Bit Error Rate (BER): Measures the number of erroneous bits in
transmission. Lower BER indicates better video quality.
********** 11 **********
--- page 12 ---
Visual Information Fidelity (VIF): Measures how much visual information
is preserved in the processed video. Higher values indicate better quality.
CO-6;   d   State the advantages and limitations of the Exhaustive Search Block   [05]
SO-1;
Matching method in video processing.
BL-2
Ans. Advantages: optimal accuracy (global best match), simple implementation,
robust to complex motion and noise, consistent results.   [2.5]
Limitations: very high computational cost, slow/not suitable for real-time,
high-power consumption, redundant computations, high memory access
overhead.   [2.5]
********** 12 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper f068394ad60c

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AIDS_7056/Signal and Image Processing/ANS_Signal and Image Processing(702AI0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 Jul 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Signal and Image Processing
Date: 14 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data if necessary.
Q1   Answer briefly:
CO-1;   a   Perform time shifting on the following discrete time signal to determine 𝑥(𝑛−   [04]
SO-1;
2) and 𝑥(−𝑛).
BL-3
Ans. Each one is for 2 marks.
CO-2;   b   Perform circular convolution of the sequences x1(n) = {2, 1, 2, 1} and   [04]
SO-1;
x2(n) = {1, 2, 1, 2} using the matrix multiplication method.
BL-3
Ans. Circulant matrix formation is for 1.5 marks, calculations for 1.5 marks, and
final answer is for 1 mark.
2 1 2 1   1   8
1 2 1 2   2   10
[   ]   . [ ] = [   ]
2 1 2 1   1   8
1 2 1 2 4×4 2 4×1   10 4×1
CO-3;   c   Explain the concept of gray level slicing. For the given 4-bit grayscale image,   [04]
SO-1;
perform gray level slicing without preserving the background using thresholds
BL-3
********** 1 **********
--- page 2 ---
T1 = 6 and T2 = 11. Show all the steps and discuss how different threshold
ranges affect image enhancement and background information loss.
15   11   6   7   8
10   12   15   3   1
8   9   5   11   12
7   5   6   8   0
12   3   4   10   13
Ans. The formula for grey level slicing without preserving background is
S = L-1;   if A ≤ r ≤ B
S = 0;   Otherwise
The formula for grey level slicing with preserving background is
S = L-1 ;   if A ≤ r ≤ B
S = r;   Otherwise (as it is)
[1.5]
Gray-level Slicing without Preserving
0   15   15   15   15
15   0   0   0   0
15   15   0   15   0
15   0   15   15   0
0   0   0   15   0
[1.5]
Discussion:
Narrow range -High contrast (specific features)
[01]
Wide range- Low contrast (more spread)
CO-5;   d   Discuss the concept of region merging in image segmentation and illustrate it   [04]
SO-1;
with an example.
BL-3
Ans.   • Region merging is a bottom-up segmentation approach
• Each pixel starts as a separate region.
• The merging criterion is based on intensity similarity. Adjacent regions
are merged only if the absolute difference between their pixel values is
less than or equal to the threshold.
• This ensures homogeneous regions while preserving boundaries   [02]
between distinct intensity groups
Any suitable example.   [02]
********** 2 **********
--- page 3 ---
CO-6;   e   Explain motion estimation in video processing. Mention any three motion   [04]
SO-1;
estimation algorithms used in video processing?
BL-2
Ans. Motion estimation is the process of determining the motion of objects between
consecutive video frames by finding matching blocks or pixels between
frames.   [02]
Any three of the following algorithms.
Algorithm   Speed   Accuracy
Full Search (Exhaustive Search)   Slow   Very High
Three-Step Search (TSS)   Medium Good
Two-Dimensional Logarithmic   Medium Good
Search   [02]
Diamond Search   Fast   Good
Hexagon Search   Fast   Good
Answer any four from Q2 to Q7
Q2   a   [10]
Explain the steps involved in finding the optimal threshold using Otsu’s
CO-5;
SO-1;   thresholding method for image segmentation.
BL-2
Ans.   •   Let {0,1, 2,…, L-1} be L intensity levels and size of image is M×N
• For histogram, ni is number of pixels with intensity, i
• Normalized histogram has pi=ni/MN
•   Select threshold, T(k)=k, 0 < k < L-1 to generate classes C1 and C2
•   Probability that a pixel is assigned to C1 and C2 are,
𝑘
𝑃1(𝑘) = ∑𝑝𝑖
𝑖=0
𝐿−1
𝑃2(𝑘) = ∑𝑝𝑖 = 1 −𝑃1(𝑘)
𝑖=𝑘+1
𝑘
1
𝑚1(𝑘) =   ∑𝑖𝑝𝑖
𝑃1(𝑘)
𝑖=0
𝐿−1
1
𝑚2(𝑘) =   ∑𝑖𝑝𝑖
𝑃2(𝑘)
𝑖=𝑘+1
[05]
Average intensity up to k =
𝑘
𝑚(𝑘) = ∑𝑖𝑝𝑖
𝑖=0
Global mean of entire image
𝐿−1
𝑚𝐺= ∑𝑖𝑝𝑖
𝑖=0
𝐿−1
𝜎𝐺 2 = ∑(𝑖−𝑚𝐺)2𝑝𝑖
𝑖=0
********** 3 **********
--- page 4 ---
𝜎𝐵 2(𝑘) = 𝑃1(𝑘)𝑃2(𝑘)(𝑚1 −𝑚2)2
Metric for separability
𝜎𝐵 2
𝜂= 2
𝜎𝐺   [05]
Choose k which provides maximum separability.
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
Ans Any three-color models:
• RGB
• CMY / CMYK
• HSI
• HSV
• YCbCr   [01]
[04]
4-adjacency:
********** 4 **********
--- page 5 ---
[02]
8-adjacency:
[03]
Q3   a   State the commutative and distributive properties of convolution. Perform   [10]
CO-1;   convolution sum of the following two sequences by tabulation method and
SO-1;
matrix methods.
BL-3
Index (n)   -2   -1   0   1
x(n)   2   2   1   2
h(n)   1   1   1   -2
Ans
[02]
Tabulation multiplications:
n   y(n)
-4   (2×1 = 2)
-3   (2×1 + 2×1 = 4)
-2   (2×1 + 2×1 + 1×1 = 5)
-1   (2×(-2) + 2×1 + 1×1 + 2×1 = 1)
0   (2×(-2) + 1×1 + 2×1 = -1)
1   (1×(-2) + 2×1 = 0)
2   (2×(-2) = -4)
[04]
Matrix method:
********** 5 **********
--- page 6 ---
[04]
CO-2;   b   Given x(n) = {1, 1, 1, 1, 0, 0, 0, 0}, compute the 8-point discrete Fourier   [10]
SO-1;
transform (DFT) using fast Fourier transform (FFT) with Radix-2.
BL-3
Ans   Initial arrangement of sequence elements into even and odd groups is for 1
mark. Output of each pass is of for 3 marks.
Q4   a   Find the even and odd components of the following signal and sketch the same.   [10]
CO-1;
Index (n)   -3   -2   -1   0   1   2   3   4
SO-1;
x(n)   1   2   3   4   5   6   7   8
BL-3
Ans.
[01]
n   -4   -3   -2   -1   0   1   2   3   4
x[n]   0   1   2   3   4   5   6   7   8
x[-n]   8   7   6   5   4   3   2   1   0
x[n] + x[-n]   8   8   8   8   8   8   8   8   8
Even, xe[n]   4   4   4   4   4   4   4   4   4
x[n] - x[-n]   -8   -6   -4   -2   0   2   4   6   8
Odd, xo[n]   -4   -3   -2   -1   0   1   2   3   4
[06]
[1.5
]
********** 6 **********
--- page 7 ---
[1.5
]
CO-2;   b   Find the response of Linear Time Invariant (LTI) system with input, x(n) =   [10]
SO-1;
{2,2,2}, and impulse function, h(n) = {1, 1} using decimation in time (DIT)
BL-3
with radix-2 Fast Fourier Transform (FFT).
Ans.
[2.5
]
[2.5
]
𝑌(𝐾) = [6,−𝑗2, 2, 𝑗2]. [2, (1 −𝑗), 0, (1 + 𝑗)]   [02]
𝑌(𝐾) = {12, (−2 −𝑗2), 0, (−2 + 𝑗2)}
𝑌∗(𝐾) = {12, (−2 + 𝑗2), 0, (−2 −𝑗2)}
********** 7 **********
--- page 8 ---
[2.5
]
[0.5
𝑦(𝑛) = {2, 4, 4, 2}   ]
Q5   a   Consider the following images:   [10]
CO-3;   10   10   10   10   10   30   30   30
SO-1;   30   30   30   30   10   30   30   30
BL-3   30   30   30   30   10   30   30   30
30   30   30   30   10   30   30   30
Image 1   Image 2
i.   Apply the horizontal and vertical Sobel operators (without zero
padding) to Image 1 and Image 2 and compute the gradient magnitude
for both images.
ii.   Write your observations based on the results obtained in part (i).
Ans.
[01]
80   80   0   0
0   0   0   0
Gx   Gy   [04]
0   0   80   0
0   0   80   0
Gx   Gy   [04]
Observations (2 marks)
Intensity changes vertically → horizontal edge.
********** 8 **********
--- page 9 ---
Intensity changes horizontally → vertical edge.   [01]
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
Ans.   i.   Threshold is ±2, Region 1 (Seed = 10, range [8,12]) and Region 2 (Seed
= 50, range [48,52])
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
𝟏𝟏 𝟏𝟎 𝟏𝟏 80 81
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
50 51 50 55 55   [03]
[ 50 50 51 55 55]
ii.
Threshold is ±1, Region 1 (Seed = 10, range [9,11]), Region 2 (Seed =
50, range [49,51])
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
𝟏𝟏 𝟏𝟎 𝟏𝟏 80 81
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
50 51 50 55 55
[ 50 50 51 55 55]
Threshold is ±10, Region 1 (Seed = 10, range [0,20]), Region 2 (Seed
= 50, range [40,60])
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
[04]
𝟏𝟏 𝟏𝟎 𝟏𝟏 80 81
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
50 51 50 55 55
[ 50 50 51 55 55]
[03]
iii.   Small threshold may lead to under segmentation. Large threshold can
combine two different segments. Therefore, optimum threshold should
be chosen. Examples
********** 9 **********
--- page 10 ---
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
Ans. Histogram of input image (1 Mark), Histogram equalization steps (5 Marks)
Histogram equalized image (1 Mark) and observations (2 marks)
Resultant image (1 mark)
Gray   PDF   s_k = (L-1) *   New
Frequency
Level   (p(r_k) = CDF   CDF =   Gray
(n_k)
(r_k)   n_k/36)   7*CDF   Level
0   2   0.056   0.056   0.392   0
1   4   0.111   0.167   1.169   1
2   4   0.111   0.278   1.946   2
3   8   0.222   0.500   3.500   4
4   4   0.111   0.611   4.277   4
5   4   0.111   0.722   5.054   5
6   8   0.222   0.944   6.608   7
7   2   0.056   1.000   7.000   7
Resultant image:
CO-1;   b   Determine whether the following signals are energy signal or power signal.   [05]
SO-1;   i.   x[n] = u[n]
BL-3   ii.   x[n] = 5
Ans.   i.
********** 10 **********
--- page 11 ---
[2.5
]
ii. Assuming, A=5
[2.5
]
CO-2;   c   Calculate the discrete Fourier transform (DFT) for the signal, x(n) = {1, 1, 1,   [05]
SO-1;
1}, using the twiddle matrix method.
BL-3
Ans.   𝑥(𝑘) = (𝑊𝑁 𝑘𝑛) . 𝑥(𝑛)   [01]
1 1   1   1
1 −𝑗 −1   𝑗   [01]
𝑊𝑁 𝑘𝑛= [   ]
1 −1 1 −1
1   𝑗 −1 −𝑗 4×4
1   1   1   1   1   4
1 −𝑗 −1   𝑗   1   0   [03]
𝑥(𝑘) = [   ]   . [ ] = [ ]
1 −1 1 −1   1   0
1   𝑗 −1 −𝑗 4×4 1 4×1   0 4×1
Q7   a   Define the Ideal Low-Pass Filter (ILPF) in the frequency domain. Explain its   [05]
CO-3;   effect on an image and discuss the occurrence of ringing artifacts. Also explain
SO-1;
BL-2   the role of cutoff frequency.
Ans. Definition (1 mark)
********** 11 **********
--- page 12 ---
ILPF passes low frequencies and blocks high frequencies.
D ( u , v ) = [( u − M / 2 ) 2 + ( v − N / 2 ) 2 ] 1 / 2
Effect on Image (1 marks): Smooths image, removes noise and blurs edges
Ringing (1 marks): Due to sharp cutoff frequency. It causes oscillations near
edges.
Decision of cut-off frequency (2 marks)
• Compute circles that enclose specified amounts of total image power
PT
• PT is obtained by summation of components of power spectrum at each
M − 1 N − 1
P T =  P ( u , v )
point as   u = 0 v = 0
Small D0: more blur and large D0: less blur
CO-4;   b A binary image is shown below. The diameters of the circular objects are 3, 5,   [05]
SO-1;
and 7 pixels. The sizes of the square objects are 9×9, 11×11, and 15×15 pixels.
BL-3
i.   Apply erosion to eliminate all the objects except the largest square.
Justify your answer.
ii.   Determine the size, shape, and intensity (value) of the structuring
element required.
Ans.
********** 12 **********
--- page 13 ---
Structuring Element size>11x11 Image size
and <=15x15   [(SE-1)/2] x [(SE-1)/2]
Intensity Black   (3M)   (2M)
CO-6;   c   Compare I-frames, P-frames, and B-frames in video compression. Write at   [05]
SO-1;
least five differences between them.
BL-2
Ans. Each difference is for 1 mark.
Feature   I-Frame   P-Frame   B-Frame
(Intra)   (Predicted)   (Bidirectional)
Full form   Intra-coded   Predictive   Bidirectional frame
frame   frame
Reference   Not required   Uses previous   Uses previous and
frame   frame   next frames
Compression   Lowest   Medium   Highest compression
compression   compression
Quality   Highest   Medium   Lowest
Data size   Largest   Smaller than I   Smallest
Encoding type   Intra-frame   Forward   Forward + backward
coding   prediction   prediction
Error   No   Yes   Yes
propagation
Use   Reference   Motion   Improve compression
frame   prediction
CO-6;   d   [05]
SO-1;   Explain the Three-Step Search (TSS) method used in video processing.
BL-2
Ans. Any of these two.
Three Step Search
It is one of the earliest fast block matching algorithms. It runs as follows:
1. Start with search location at center
2. Set step size S = 4 and search parameter p = 7
3. Search 8 locations +/- S pixels around location (0,0) and the location
(0,0)   [02]
4. Pick among the 9 locations searched, the one with minimum cost
function
5. Set the new search origin to the above picked location
6. Set the new step size as S = S/2
7. Repeat the search procedure until S = 1
The resulting location for S=1 is the one with minimum cost function and the
macro block at this location is the best match.   [03]
********** 13 **********
--- page 14 ---
There is a reduction in computation by a factor of 9 in this algorithm. For p=7,
while ES evaluates cost for 225 macro-blocks, TSS evaluates only for 25
macro blocks.
OR
New Three Step Search
TSS uses a uniformly allocated checking pattern and is prone to miss small
motions. NTSS is an improvement over TSS as it provides a center biased
search scheme and has provisions to stop halfway to reduce the computational
cost. It was one of the first widely accepted fast algorithms and frequently
used for implementing earlier standards like MPEG 1 and H.261.
The algorithm runs as follows:
1. Start with search location at center
2. Search 8 locations +/- S pixels with S = 4 and 8 locations +/- S pixels
with S = 1 around location (0,0)
3. Pick among the 16 locations searched, the one with minimum cost
function
4. If the minimum cost function occurs at origin, stop the search and set
motion vector to (0,0)
5. If the minimum cost function occurs at one of the 8 locations at S = 1,
set the new search origin to this location
1. Check adjacent weights for this location, depending on location
it may check either 3 or 5 points
6. The one that gives lowest weight is the closest match, set the motion
vector to that location
7. If the lowest weight after the first step was one of the 8 locations at S
= 4, the normal TSS procedure follows
1. Pick among the 9 locations searched, the one with minimum
cost function
2. Set the new search origin to the above picked location
3. Set the new step size as S = S/2
4. Repeat the search procedure until S = 1
Thus this algorithm checks 17 points for each macro-block and the worst-case
scenario involves checking 33 locations, which is still much faster than TSS.
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 424b948f5d8e

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_AI_7012/Signal and Image Processing/ANS_Signal and Image Processing(702AI0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 Jul 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Signal and Image Processing
Date: 14 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data if necessary.
Q1   Answer briefly:
CO-1;   a   Perform time shifting on the following discrete time signal to determine 𝑥(𝑛−   [04]
SO-1;
2) and 𝑥(−𝑛).
BL-3
Ans. Each one is for 2 marks.
CO-2;   b   Perform circular convolution of the sequences x1(n) = {2, 1, 2, 1} and   [04]
SO-1;
x2(n) = {1, 2, 1, 2} using the matrix multiplication method.
BL-3
Ans. Circulant matrix formation is for 1.5 marks, calculations for 1.5 marks, and
final answer is for 1 mark.
2 1 2 1   1   8
1 2 1 2   2   10
[   ]   . [ ] = [   ]
2 1 2 1   1   8
1 2 1 2 4×4 2 4×1   10 4×1
CO-3;   c   Explain the concept of gray level slicing. For the given 4-bit grayscale image,   [04]
SO-1;
perform gray level slicing without preserving the background using thresholds
BL-3
********** 1 **********
--- page 2 ---
T1 = 6 and T2 = 11. Show all the steps and discuss how different threshold
ranges affect image enhancement and background information loss.
15   11   6   7   8
10   12   15   3   1
8   9   5   11   12
7   5   6   8   0
12   3   4   10   13
Ans. The formula for grey level slicing without preserving background is
S = L-1;   if A ≤ r ≤ B
S = 0;   Otherwise
The formula for grey level slicing with preserving background is
S = L-1 ;   if A ≤ r ≤ B
S = r;   Otherwise (as it is)
[1.5]
Gray-level Slicing without Preserving
0   15   15   15   15
15   0   0   0   0
15   15   0   15   0
15   0   15   15   0
0   0   0   15   0
[1.5]
Discussion:
Narrow range -High contrast (specific features)
[01]
Wide range- Low contrast (more spread)
CO-5;   d   Discuss the concept of region merging in image segmentation and illustrate it   [04]
SO-1;
with an example.
BL-3
Ans.   • Region merging is a bottom-up segmentation approach
• Each pixel starts as a separate region.
• The merging criterion is based on intensity similarity. Adjacent regions
are merged only if the absolute difference between their pixel values is
less than or equal to the threshold.
• This ensures homogeneous regions while preserving boundaries   [02]
between distinct intensity groups
Any suitable example.   [02]
********** 2 **********
--- page 3 ---
CO-6;   e   Explain motion estimation in video processing. Mention any three motion   [04]
SO-1;
estimation algorithms used in video processing?
BL-2
Ans. Motion estimation is the process of determining the motion of objects between
consecutive video frames by finding matching blocks or pixels between
frames.   [02]
Any three of the following algorithms.
Algorithm   Speed   Accuracy
Full Search (Exhaustive Search)   Slow   Very High
Three-Step Search (TSS)   Medium Good
Two-Dimensional Logarithmic   Medium Good
Search   [02]
Diamond Search   Fast   Good
Hexagon Search   Fast   Good
Answer any four from Q2 to Q7
Q2   a   [10]
Explain the steps involved in finding the optimal threshold using Otsu’s
CO-5;
SO-1;   thresholding method for image segmentation.
BL-2
Ans.   •   Let {0,1, 2,…, L-1} be L intensity levels and size of image is M×N
• For histogram, ni is number of pixels with intensity, i
• Normalized histogram has pi=ni/MN
•   Select threshold, T(k)=k, 0 < k < L-1 to generate classes C1 and C2
•   Probability that a pixel is assigned to C1 and C2 are,
𝑘
𝑃1(𝑘) = ∑𝑝𝑖
𝑖=0
𝐿−1
𝑃2(𝑘) = ∑𝑝𝑖 = 1 −𝑃1(𝑘)
𝑖=𝑘+1
𝑘
1
𝑚1(𝑘) =   ∑𝑖𝑝𝑖
𝑃1(𝑘)
𝑖=0
𝐿−1
1
𝑚2(𝑘) =   ∑𝑖𝑝𝑖
𝑃2(𝑘)
𝑖=𝑘+1
[05]
Average intensity up to k =
𝑘
𝑚(𝑘) = ∑𝑖𝑝𝑖
𝑖=0
Global mean of entire image
𝐿−1
𝑚𝐺= ∑𝑖𝑝𝑖
𝑖=0
𝐿−1
𝜎𝐺 2 = ∑(𝑖−𝑚𝐺)2𝑝𝑖
𝑖=0
********** 3 **********
--- page 4 ---
𝜎𝐵 2(𝑘) = 𝑃1(𝑘)𝑃2(𝑘)(𝑚1 −𝑚2)2
Metric for separability
𝜎𝐵 2
𝜂= 2
𝜎𝐺   [05]
Choose k which provides maximum separability.
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
Ans Any three-color models:
• RGB
• CMY / CMYK
• HSI
• HSV
• YCbCr   [01]
[04]
4-adjacency:
********** 4 **********
--- page 5 ---
[02]
8-adjacency:
[03]
Q3   a   State the commutative and distributive properties of convolution. Perform   [10]
CO-1;   convolution sum of the following two sequences by tabulation method and
SO-1;
matrix methods.
BL-3
Index (n)   -2   -1   0   1
x(n)   2   2   1   2
h(n)   1   1   1   -2
Ans
[02]
Tabulation multiplications:
n   y(n)
-4   (2×1 = 2)
-3   (2×1 + 2×1 = 4)
-2   (2×1 + 2×1 + 1×1 = 5)
-1   (2×(-2) + 2×1 + 1×1 + 2×1 = 1)
0   (2×(-2) + 1×1 + 2×1 = -1)
1   (1×(-2) + 2×1 = 0)
2   (2×(-2) = -4)
[04]
Matrix method:
********** 5 **********
--- page 6 ---
[04]
CO-2;   b   Given x(n) = {1, 1, 1, 1, 0, 0, 0, 0}, compute the 8-point discrete Fourier   [10]
SO-1;
transform (DFT) using fast Fourier transform (FFT) with Radix-2.
BL-3
Ans   Initial arrangement of sequence elements into even and odd groups is for 1
mark. Output of each pass is of for 3 marks.
Q4   a   Find the even and odd components of the following signal and sketch the same.   [10]
CO-1;
Index (n)   -3   -2   -1   0   1   2   3   4
SO-1;
x(n)   1   2   3   4   5   6   7   8
BL-3
Ans.
[01]
n   -4   -3   -2   -1   0   1   2   3   4
x[n]   0   1   2   3   4   5   6   7   8
x[-n]   8   7   6   5   4   3   2   1   0
x[n] + x[-n]   8   8   8   8   8   8   8   8   8
Even, xe[n]   4   4   4   4   4   4   4   4   4
x[n] - x[-n]   -8   -6   -4   -2   0   2   4   6   8
Odd, xo[n]   -4   -3   -2   -1   0   1   2   3   4
[06]
[1.5
]
********** 6 **********
--- page 7 ---
[1.5
]
CO-2;   b   Find the response of Linear Time Invariant (LTI) system with input, x(n) =   [10]
SO-1;
{2,2,2}, and impulse function, h(n) = {1, 1} using decimation in time (DIT)
BL-3
with radix-2 Fast Fourier Transform (FFT).
Ans.
[2.5
]
[2.5
]
𝑌(𝐾) = [6,−𝑗2, 2, 𝑗2]. [2, (1 −𝑗), 0, (1 + 𝑗)]   [02]
𝑌(𝐾) = {12, (−2 −𝑗2), 0, (−2 + 𝑗2)}
𝑌∗(𝐾) = {12, (−2 + 𝑗2), 0, (−2 −𝑗2)}
********** 7 **********
--- page 8 ---
[2.5
]
[0.5
𝑦(𝑛) = {2, 4, 4, 2}   ]
Q5   a   Consider the following images:   [10]
CO-3;   10   10   10   10   10   30   30   30
SO-1;   30   30   30   30   10   30   30   30
BL-3   30   30   30   30   10   30   30   30
30   30   30   30   10   30   30   30
Image 1   Image 2
i.   Apply the horizontal and vertical Sobel operators (without zero
padding) to Image 1 and Image 2 and compute the gradient magnitude
for both images.
ii.   Write your observations based on the results obtained in part (i).
Ans.
[01]
80   80   0   0
0   0   0   0
Gx   Gy   [04]
0   0   80   0
0   0   80   0
Gx   Gy   [04]
Observations (2 marks)
Intensity changes vertically → horizontal edge.
********** 8 **********
--- page 9 ---
Intensity changes horizontally → vertical edge.   [01]
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
Ans.   i.   Threshold is ±2, Region 1 (Seed = 10, range [8,12]) and Region 2 (Seed
= 50, range [48,52])
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
𝟏𝟏 𝟏𝟎 𝟏𝟏 80 81
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
50 51 50 55 55   [03]
[ 50 50 51 55 55]
ii.
Threshold is ±1, Region 1 (Seed = 10, range [9,11]), Region 2 (Seed =
50, range [49,51])
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
𝟏𝟏 𝟏𝟎 𝟏𝟏 80 81
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
50 51 50 55 55
[ 50 50 51 55 55]
Threshold is ±10, Region 1 (Seed = 10, range [0,20]), Region 2 (Seed
= 50, range [40,60])
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
[04]
𝟏𝟏 𝟏𝟎 𝟏𝟏 80 81
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
50 51 50 55 55
[ 50 50 51 55 55]
[03]
iii.   Small threshold may lead to under segmentation. Large threshold can
combine two different segments. Therefore, optimum threshold should
be chosen. Examples
********** 9 **********
--- page 10 ---
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
Ans. Histogram of input image (1 Mark), Histogram equalization steps (5 Marks)
Histogram equalized image (1 Mark) and observations (2 marks)
Resultant image (1 mark)
Gray   PDF   s_k = (L-1) *   New
Frequency
Level   (p(r_k) = CDF   CDF =   Gray
(n_k)
(r_k)   n_k/36)   7*CDF   Level
0   2   0.056   0.056   0.392   0
1   4   0.111   0.167   1.169   1
2   4   0.111   0.278   1.946   2
3   8   0.222   0.500   3.500   4
4   4   0.111   0.611   4.277   4
5   4   0.111   0.722   5.054   5
6   8   0.222   0.944   6.608   7
7   2   0.056   1.000   7.000   7
Resultant image:
CO-1;   b   Determine whether the following signals are energy signal or power signal.   [05]
SO-1;   i.   x[n] = u[n]
BL-3   ii.   x[n] = 5
Ans.   i.
********** 10 **********
--- page 11 ---
[2.5
]
ii. Assuming, A=5
[2.5
]
CO-2;   c   Calculate the discrete Fourier transform (DFT) for the signal, x(n) = {1, 1, 1,   [05]
SO-1;
1}, using the twiddle matrix method.
BL-3
Ans.   𝑥(𝑘) = (𝑊𝑁 𝑘𝑛) . 𝑥(𝑛)   [01]
1 1   1   1
1 −𝑗 −1   𝑗   [01]
𝑊𝑁 𝑘𝑛= [   ]
1 −1 1 −1
1   𝑗 −1 −𝑗 4×4
1   1   1   1   1   4
1 −𝑗 −1   𝑗   1   0   [03]
𝑥(𝑘) = [   ]   . [ ] = [ ]
1 −1 1 −1   1   0
1   𝑗 −1 −𝑗 4×4 1 4×1   0 4×1
Q7   a   Define the Ideal Low-Pass Filter (ILPF) in the frequency domain. Explain its   [05]
CO-3;   effect on an image and discuss the occurrence of ringing artifacts. Also explain
SO-1;
BL-2   the role of cutoff frequency.
Ans. Definition (1 mark)
********** 11 **********
--- page 12 ---
ILPF passes low frequencies and blocks high frequencies.
D ( u , v ) = [( u − M / 2 ) 2 + ( v − N / 2 ) 2 ] 1 / 2
Effect on Image (1 marks): Smooths image, removes noise and blurs edges
Ringing (1 marks): Due to sharp cutoff frequency. It causes oscillations near
edges.
Decision of cut-off frequency (2 marks)
• Compute circles that enclose specified amounts of total image power
PT
• PT is obtained by summation of components of power spectrum at each
M − 1 N − 1
P T =  P ( u , v )
point as   u = 0 v = 0
Small D0: more blur and large D0: less blur
CO-4;   b A binary image is shown below. The diameters of the circular objects are 3, 5,   [05]
SO-1;
and 7 pixels. The sizes of the square objects are 9×9, 11×11, and 15×15 pixels.
BL-3
i.   Apply erosion to eliminate all the objects except the largest square.
Justify your answer.
ii.   Determine the size, shape, and intensity (value) of the structuring
element required.
Ans.
********** 12 **********
--- page 13 ---
Structuring Element size>11x11 Image size
and <=15x15   [(SE-1)/2] x [(SE-1)/2]
Intensity Black   (3M)   (2M)
CO-6;   c   Compare I-frames, P-frames, and B-frames in video compression. Write at   [05]
SO-1;
least five differences between them.
BL-2
Ans. Each difference is for 1 mark.
Feature   I-Frame   P-Frame   B-Frame
(Intra)   (Predicted)   (Bidirectional)
Full form   Intra-coded   Predictive   Bidirectional frame
frame   frame
Reference   Not required   Uses previous   Uses previous and
frame   frame   next frames
Compression   Lowest   Medium   Highest compression
compression   compression
Quality   Highest   Medium   Lowest
Data size   Largest   Smaller than I   Smallest
Encoding type   Intra-frame   Forward   Forward + backward
coding   prediction   prediction
Error   No   Yes   Yes
propagation
Use   Reference   Motion   Improve compression
frame   prediction
CO-6;   d   [05]
SO-1;   Explain the Three-Step Search (TSS) method used in video processing.
BL-2
Ans. Any of these two.
Three Step Search
It is one of the earliest fast block matching algorithms. It runs as follows:
1. Start with search location at center
2. Set step size S = 4 and search parameter p = 7
3. Search 8 locations +/- S pixels around location (0,0) and the location
(0,0)   [02]
4. Pick among the 9 locations searched, the one with minimum cost
function
5. Set the new search origin to the above picked location
6. Set the new step size as S = S/2
7. Repeat the search procedure until S = 1
The resulting location for S=1 is the one with minimum cost function and the
macro block at this location is the best match.   [03]
********** 13 **********
--- page 14 ---
There is a reduction in computation by a factor of 9 in this algorithm. For p=7,
while ES evaluates cost for 225 macro-blocks, TSS evaluates only for 25
macro blocks.
OR
New Three Step Search
TSS uses a uniformly allocated checking pattern and is prone to miss small
motions. NTSS is an improvement over TSS as it provides a center biased
search scheme and has provisions to stop halfway to reduce the computational
cost. It was one of the first widely accepted fast algorithms and frequently
used for implementing earlier standards like MPEG 1 and H.261.
The algorithm runs as follows:
1. Start with search location at center
2. Search 8 locations +/- S pixels with S = 4 and 8 locations +/- S pixels
with S = 1 around location (0,0)
3. Pick among the 16 locations searched, the one with minimum cost
function
4. If the minimum cost function occurs at origin, stop the search and set
motion vector to (0,0)
5. If the minimum cost function occurs at one of the 8 locations at S = 1,
set the new search origin to this location
1. Check adjacent weights for this location, depending on location
it may check either 3 or 5 points
6. The one that gives lowest weight is the closest match, set the motion
vector to that location
7. If the lowest weight after the first step was one of the 8 locations at S
= 4, the normal TSS procedure follows
1. Pick among the 9 locations searched, the one with minimum
cost function
2. Set the new search origin to the above picked location
3. Set the new step size as S = S/2
4. Repeat the search procedure until S = 1
Thus this algorithm checks 17 points for each macro-block and the worst-case
scenario involves checking 33 locations, which is still much faster than TSS.
********** 14 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 67a36f848adc

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/MBATech_AI_7051/Signal and Image Processing/ANS_Signal and Image Processing(702AI0C033)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 Jul 2026
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Signal and Image Processing
Date: 14 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Assume suitable data if necessary.
Q1   Answer briefly:
CO-1;   a   Perform time shifting on the following discrete time signal to determine 𝑥(𝑛−   [04]
SO-1;
2) and 𝑥(−𝑛).
BL-3
Ans. Each one is for 2 marks.
CO-2;   b   Perform circular convolution of the sequences x1(n) = {2, 1, 2, 1} and   [04]
SO-1;
x2(n) = {1, 2, 1, 2} using the matrix multiplication method.
BL-3
Ans. Circulant matrix formation is for 1.5 marks, calculations for 1.5 marks, and
final answer is for 1 mark.
2 1 2 1   1   8
1 2 1 2   2   10
[   ]   . [ ] = [   ]
2 1 2 1   1   8
1 2 1 2 4×4 2 4×1   10 4×1
CO-3;   c   Explain the concept of gray level slicing. For the given 4-bit grayscale image,   [04]
SO-1;
perform gray level slicing without preserving the background using thresholds
BL-3
********** 1 **********
--- page 2 ---
T1 = 6 and T2 = 11. Show all the steps and discuss how different threshold
ranges affect image enhancement and background information loss.
15   11   6   7   8
10   12   15   3   1
8   9   5   11   12
7   5   6   8   0
12   3   4   10   13
Ans. The formula for grey level slicing without preserving background is
S = L-1;   if A ≤ r ≤ B
S = 0;   Otherwise
The formula for grey level slicing with preserving background is
S = L-1 ;   if A ≤ r ≤ B
S = r;   Otherwise (as it is)
[1.5]
Gray-level Slicing without Preserving
0   15   15   15   15
15   0   0   0   0
15   15   0   15   0
15   0   15   15   0
0   0   0   15   0
[1.5]
Discussion:
Narrow range -High contrast (specific features)
[01]
Wide range- Low contrast (more spread)
CO-5;   d   Discuss the concept of region merging in image segmentation and illustrate it   [04]
SO-1;
with an example.
BL-3
Ans.   • Region merging is a bottom-up segmentation approach
• Each pixel starts as a separate region.
• The merging criterion is based on intensity similarity. Adjacent regions
are merged only if the absolute difference between their pixel values is
less than or equal to the threshold.
• This ensures homogeneous regions while preserving boundaries   [02]
between distinct intensity groups
Any suitable example.   [02]
********** 2 **********
--- page 3 ---
CO-6;   e   Explain motion estimation in video processing. Mention any three motion   [04]
SO-1;
estimation algorithms used in video processing?
BL-2
Ans. Motion estimation is the process of determining the motion of objects between
consecutive video frames by finding matching blocks or pixels between
frames.   [02]
Any three of the following algorithms.
Algorithm   Speed   Accuracy
Full Search (Exhaustive Search)   Slow   Very High
Three-Step Search (TSS)   Medium Good
Two-Dimensional Logarithmic   Medium Good
Search   [02]
Diamond Search   Fast   Good
Hexagon Search   Fast   Good
Answer any four from Q2 to Q7
Q2   a   [10]
Explain the steps involved in finding the optimal threshold using Otsu’s
CO-5;
SO-1;   thresholding method for image segmentation.
BL-2
Ans.   •   Let {0,1, 2,…, L-1} be L intensity levels and size of image is M×N
• For histogram, ni is number of pixels with intensity, i
• Normalized histogram has pi=ni/MN
•   Select threshold, T(k)=k, 0 < k < L-1 to generate classes C1 and C2
•   Probability that a pixel is assigned to C1 and C2 are,
𝑘
𝑃1(𝑘) = ∑𝑝𝑖
𝑖=0
𝐿−1
𝑃2(𝑘) = ∑𝑝𝑖 = 1 −𝑃1(𝑘)
𝑖=𝑘+1
𝑘
1
𝑚1(𝑘) =   ∑𝑖𝑝𝑖
𝑃1(𝑘)
𝑖=0
𝐿−1
1
𝑚2(𝑘) =   ∑𝑖𝑝𝑖
𝑃2(𝑘)
𝑖=𝑘+1
[05]
Average intensity up to k =
𝑘
𝑚(𝑘) = ∑𝑖𝑝𝑖
𝑖=0
Global mean of entire image
𝐿−1
𝑚𝐺= ∑𝑖𝑝𝑖
𝑖=0
𝐿−1
𝜎𝐺 2 = ∑(𝑖−𝑚𝐺)2𝑝𝑖
𝑖=0
********** 3 **********
--- page 4 ---
𝜎𝐵 2(𝑘) = 𝑃1(𝑘)𝑃2(𝑘)(𝑚1 −𝑚2)2
Metric for separability
𝜎𝐵 2
𝜂= 2
𝜎𝐺   [05]
Choose k which provides maximum separability.
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
Ans Any three-color models:
• RGB
• CMY / CMYK
• HSI
• HSV
• YCbCr   [01]
[04]
4-adjacency:
********** 4 **********
--- page 5 ---
[02]
8-adjacency:
[03]
Q3   a   State the commutative and distributive properties of convolution. Perform   [10]
CO-1;   convolution sum of the following two sequences by tabulation method and
SO-1;
matrix methods.
BL-3
Index (n)   -2   -1   0   1
x(n)   2   2   1   2
h(n)   1   1   1   -2
Ans
[02]
Tabulation multiplications:
n   y(n)
-4   (2×1 = 2)
-3   (2×1 + 2×1 = 4)
-2   (2×1 + 2×1 + 1×1 = 5)
-1   (2×(-2) + 2×1 + 1×1 + 2×1 = 1)
0   (2×(-2) + 1×1 + 2×1 = -1)
1   (1×(-2) + 2×1 = 0)
2   (2×(-2) = -4)
[04]
Matrix method:
********** 5 **********
--- page 6 ---
[04]
CO-2;   b   Given x(n) = {1, 1, 1, 1, 0, 0, 0, 0}, compute the 8-point discrete Fourier   [10]
SO-1;
transform (DFT) using fast Fourier transform (FFT) with Radix-2.
BL-3
Ans   Initial arrangement of sequence elements into even and odd groups is for 1
mark. Output of each pass is of for 3 marks.
Q4   a   Find the even and odd components of the following signal and sketch the same.   [10]
CO-1;
Index (n)   -3   -2   -1   0   1   2   3   4
SO-1;
x(n)   1   2   3   4   5   6   7   8
BL-3
Ans.
[01]
n   -4   -3   -2   -1   0   1   2   3   4
x[n]   0   1   2   3   4   5   6   7   8
x[-n]   8   7   6   5   4   3   2   1   0
x[n] + x[-n]   8   8   8   8   8   8   8   8   8
Even, xe[n]   4   4   4   4   4   4   4   4   4
x[n] - x[-n]   -8   -6   -4   -2   0   2   4   6   8
Odd, xo[n]   -4   -3   -2   -1   0   1   2   3   4
[06]
[1.5
]
********** 6 **********
--- page 7 ---
[1.5
]
CO-2;   b   Find the response of Linear Time Invariant (LTI) system with input, x(n) =   [10]
SO-1;
{2,2,2}, and impulse function, h(n) = {1, 1} using decimation in time (DIT)
BL-3
with radix-2 Fast Fourier Transform (FFT).
Ans.
[2.5
]
[2.5
]
𝑌(𝐾) = [6,−𝑗2, 2, 𝑗2]. [2, (1 −𝑗), 0, (1 + 𝑗)]   [02]
𝑌(𝐾) = {12, (−2 −𝑗2), 0, (−2 + 𝑗2)}
𝑌∗(𝐾) = {12, (−2 + 𝑗2), 0, (−2 −𝑗2)}
********** 7 **********
--- page 8 ---
[2.5
]
[0.5
𝑦(𝑛) = {2, 4, 4, 2}   ]
Q5   a   Consider the following images:   [10]
CO-3;   10   10   10   10   10   30   30   30
SO-1;   30   30   30   30   10   30   30   30
BL-3   30   30   30   30   10   30   30   30
30   30   30   30   10   30   30   30
Image 1   Image 2
i.   Apply the horizontal and vertical Sobel operators (without zero
padding) to Image 1 and Image 2 and compute the gradient magnitude
for both images.
ii.   Write your observations based on the results obtained in part (i).
Ans.
[01]
80   80   0   0
0   0   0   0
Gx   Gy   [04]
0   0   80   0
0   0   80   0
Gx   Gy   [04]
Observations (2 marks)
Intensity changes vertically → horizontal edge.
********** 8 **********
--- page 9 ---
Intensity changes horizontally → vertical edge.   [01]
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
Ans.   i.   Threshold is ±2, Region 1 (Seed = 10, range [8,12]) and Region 2 (Seed
= 50, range [48,52])
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
𝟏𝟏 𝟏𝟎 𝟏𝟏 80 81
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
50 51 50 55 55   [03]
[ 50 50 51 55 55]
ii.
Threshold is ±1, Region 1 (Seed = 10, range [9,11]), Region 2 (Seed =
50, range [49,51])
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
𝟏𝟏 𝟏𝟎 𝟏𝟏 80 81
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
50 51 50 55 55
[ 50 50 51 55 55]
Threshold is ±10, Region 1 (Seed = 10, range [0,20]), Region 2 (Seed
= 50, range [40,60])
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
[04]
𝟏𝟏 𝟏𝟎 𝟏𝟏 80 81
𝟏𝟎 𝟏𝟏 𝟏𝟎 80 80
50 51 50 55 55
[ 50 50 51 55 55]
[03]
iii.   Small threshold may lead to under segmentation. Large threshold can
combine two different segments. Therefore, optimum threshold should
be chosen. Examples
********** 9 **********
--- page 10 ---
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
Ans. Histogram of input image (1 Mark), Histogram equalization steps (5 Marks)
Histogram equalized image (1 Mark) and observations (2 marks)
Resultant image (1 mark)
Gray   PDF   s_k = (L-1) *   New
Frequency
Level   (p(r_k) = CDF   CDF =   Gray
(n_k)
(r_k)   n_k/36)   7*CDF   Level
0   2   0.056   0.056   0.392   0
1   4   0.111   0.167   1.169   1
2   4   0.111   0.278   1.946   2
3   8   0.222   0.500   3.500   4
4   4   0.111   0.611   4.277   4
5   4   0.111   0.722   5.054   5
6   8   0.222   0.944   6.608   7
7   2   0.056   1.000   7.000   7
Resultant image:
CO-1;   b   Determine whether the following signals are energy signal or power signal.   [05]
SO-1;   i.   x[n] = u[n]
BL-3   ii.   x[n] = 5
Ans.   i.
********** 10 **********
--- page 11 ---
[2.5
]
ii. Assuming, A=5
[2.5
]
CO-2;   c   Calculate the discrete Fourier transform (DFT) for the signal, x(n) = {1, 1, 1,   [05]
SO-1;
1}, using the twiddle matrix method.
BL-3
Ans.   𝑥(𝑘) = (𝑊𝑁 𝑘𝑛) . 𝑥(𝑛)   [01]
1 1   1   1
1 −𝑗 −1   𝑗   [01]
𝑊𝑁 𝑘𝑛= [   ]
1 −1 1 −1
1   𝑗 −1 −𝑗 4×4
1   1   1   1   1   4
1 −𝑗 −1   𝑗   1   0   [03]
𝑥(𝑘) = [   ]   . [ ] = [ ]
1 −1 1 −1   1   0
1   𝑗 −1 −𝑗 4×4 1 4×1   0 4×1
Q7   a   Define the Ideal Low-Pass Filter (ILPF) in the frequency domain. Explain its   [05]
CO-3;   effect on an image and discuss the occurrence of ringing artifacts. Also explain
SO-1;
BL-2   the role of cutoff frequency.
Ans. Definition (1 mark)
********** 11 **********
--- page 12 ---
ILPF passes low frequencies and blocks high frequencies.
D ( u , v ) = [( u − M / 2 ) 2 + ( v − N / 2 ) 2 ] 1 / 2
Effect on Image (1 marks): Smooths image, removes noise and blurs edges
Ringing (1 marks): Due to sharp cutoff frequency. It causes oscillations near
edges.
Decision of cut-off frequency (2 marks)
• Compute circles that enclose specified amounts of total image power
PT
• PT is obtained by summation of components of power spectrum at each
M − 1 N − 1
P T =  P ( u , v )
point as   u = 0 v = 0
Small D0: more blur and large D0: less blur
CO-4;   b A binary image is shown below. The diameters of the circular objects are 3, 5,   [05]
SO-1;
and 7 pixels. The sizes of the square objects are 9×9, 11×11, and 15×15 pixels.
BL-3
i.   Apply erosion to eliminate all the objects except the largest square.
Justify your answer.
ii.   Determine the size, shape, and intensity (value) of the structuring
element required.
Ans.
********** 12 **********
--- page 13 ---
Structuring Element size>11x11 Image size
and <=15x15   [(SE-1)/2] x [(SE-1)/2]
Intensity Black   (3M)   (2M)
CO-6;   c   Compare I-frames, P-frames, and B-frames in video compression. Write at   [05]
SO-1;
least five differences between them.
BL-2
Ans. Each difference is for 1 mark.
Feature   I-Frame   P-Frame   B-Frame
(Intra)   (Predicted)   (Bidirectional)
Full form   Intra-coded   Predictive   Bidirectional frame
frame   frame
Reference   Not required   Uses previous   Uses previous and
frame   frame   next frames
Compression   Lowest   Medium   Highest compression
compression   compression
Quality   Highest   Medium   Lowest
Data size   Largest   Smaller than I   Smallest
Encoding type   Intra-frame   Forward   Forward + backward
coding   prediction   prediction
Error   No   Yes   Yes
propagation
Use   Reference   Motion   Improve compression
frame   prediction
CO-6;   d   [05]
SO-1;   Explain the Three-Step Search (TSS) method used in video processing.
BL-2
Ans. Any of these two.
Three Step Search
It is one of the earliest fast block matching algorithms. It runs as follows:
1. Start with search location at center
2. Set step size S = 4 and search parameter p = 7
3. Search 8 locations +/- S pixels around location (0,0) and the location
(0,0)   [02]
4. Pick among the 9 locations searched, the one with minimum cost
function
5. Set the new search origin to the above picked location
6. Set the new step size as S = S/2
7. Repeat the search procedure until S = 1
The resulting location for S=1 is the one with minimum cost function and the
macro block at this location is the best match.   [03]
********** 13 **********
--- page 14 ---
There is a reduction in computation by a factor of 9 in this algorithm. For p=7,
while ES evaluates cost for 225 macro-blocks, TSS evaluates only for 25
macro blocks.
OR
New Three Step Search
TSS uses a uniformly allocated checking pattern and is prone to miss small
motions. NTSS is an improvement over TSS as it provides a center biased
search scheme and has provisions to stop halfway to reduce the computational
cost. It was one of the first widely accepted fast algorithms and frequently
used for implementing earlier standards like MPEG 1 and H.261.
The algorithm runs as follows:
1. Start with search location at center
2. Search 8 locations +/- S pixels with S = 4 and 8 locations +/- S pixels
with S = 1 around location (0,0)
3. Pick among the 16 locations searched, the one with minimum cost
function
4. If the minimum cost function occurs at origin, stop the search and set
motion vector to (0,0)
5. If the minimum cost function occurs at one of the 8 locations at S = 1,
set the new search origin to this location
1. Check adjacent weights for this location, depending on location
it may check either 3 or 5 points
6. The one that gives lowest weight is the closest match, set the motion
vector to that location
7. If the lowest weight after the first step was one of the 8 locations at S
= 4, the normal TSS procedure follows
1. Pick among the 9 locations searched, the one with minimum
cost function
2. Set the new search origin to the above picked location
3. Set the new step size as S = S/2
4. Repeat the search procedure until S = 1
Thus this algorithm checks 17 points for each macro-block and the worst-case
scenario involves checking 33 locations, which is still much faster than TSS.
********** 14 **********
````
