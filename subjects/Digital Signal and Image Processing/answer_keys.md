# Digital Signal and Image Processing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 338f7e5f67e6

- Departments: Mechatronics
- Programmes: BTech Mechatronics 7004
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Mechatronics_7004/Digital Signal and Image Processing/ANS_Digital Signal and Image Processing(702MH0E008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 11 May 2026
- Text: mixed (10 pages), mean OCR confidence 47.4
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (MECHATRONICS ENGINEERING)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Digital Signal and Image Processing
Date: 11 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. Assume Suitable data if necessary.
Q1   Attempt the following   [20]
a   Identify whether the following system is of Minimum Phase, Maximum Phase or
Mixed Phase type.
H ( z ) = 3 z 2 + 1 z − 1
2   2
Ans :   [05]
CO-1 ; SO-1 ;   H ( z ) = 3 z 2 + 1 z − 1 = ( 3 z − )1   z + 1  
BL-4   2   2      2 
1   1
Hence the zeros are at z =   and z = −   .
3   2
Both the zeros are inside the unit circle, hence it is Minimum Phase System.
b   1
One of the zeros of a causal linear phase FIR filter lies at 𝑧=   . Predict the
2
location of the other zero and hence compute the transfer function and impulse
CO-1 ; SO- 1;   response of the filter.   [05]
BL-6
Ans :
********** 1 **********
--- page 2 ---
1   1
Zero of a linear phase filter occur at reciprocal location z0 =   . =   = 2 .
2   z 0
−  z 1   ( z − 2 )
   2 
H (z) =   2
z
5
z2 − z + 1
2
=
2
= 1 − 5 z −+ 1 z − 2
2
− 5
h(n) =    ,1   , 1 
2
CO- 2; SO- 1;   c   Explanation of Connectivity in details.   [05]
BL-2
d   For the DFT pair of real point sequence, compute boxed quantities.
Ans :
x(n)   X(K)
4   20
𝟐   𝟓+ 𝟑𝒋
CO-1; SO-1;   5   −5 + 2𝑗   [05]
BL-3
6   −𝟓 − 𝟐𝒋
[ 3 ]   [ 5 − 3𝑗]
Q2   [20]
a   Given x[n] = { 4+ 4j, 3+3j, 2+2j, 1+j }.
CO-1; SO-1;   [10]
BL-3   i)   Compute X[K]
********** 2 **********
--- page 3 ---
ii)   Let p[n] = {4,3,2,1} and q[n] = {4,3,2,1}
Compute P[K] and Q[K] using result of X[K].
Ans :
X[K] = {10 + 10j, 4 , 2+2j, 4j}   2 Marks
X*[K] = {10 - 10j, 4, 2-2j, - 4j}   2 Marks
X*[-K] = {10 - 10j, -4j, 2-2j, 4}   2 Marks
P[K] = {10, 2 - 2j , 2 , 2+2j}   2 Marks
Q[K] = {10, 2 - 2j , 2 , 2+2j}   2 Marks
b   If x(n) = {1,1,2,1} and h(n) = {1,2,3,4}, find circular convolution using DIF FFT &
IFFT.   [10]
Ans :
CO-1; SO-1;   X(K) = {5,-1,1,-1}
BL-3
H(K)={10 , -2+2j , -2 , -2-2j}
Y(K) = { 50 , 2-2j , -2 , 2+2j}
y(n) = { 13,14,11,12}
Q3   [20]
a   Compute the order of a Digital Butterworth filter for following specifications:
Ap = 1.93 dB
As = 13.97 dB
Wp = 0.6π rad
Ws = 0.2π rad
CO-4; SO-1; BL-
Ans :
3
The Given Filter is HPF. 1 Mark   [08]
Ωp = 2.752 rad / sec   2 Marks
Ωs = 0.649 rad / sec   2 Marks
N = 1.3   2 Marks
Let Order = 2   1 Mark
b   𝜋
Design 6th order Linear Phase High Pass FIR filter with 𝑤𝑐 =   using
CO-4; SO-1;   2
[12]
BL-6   Blackman window function.
Ans : h[n] = { 0 , 0, - 0.2 , -0.5, - 0.2, 0, 0 }
Q4   [20]
********** 3 **********
--- page 4 ---
a   Perform Histogram Equalization for the given image. Also sketch the equalized
histogram.
1   3   4   1   3
4   2   7   7   7
1   7   0   2   1
0   3   1   7   6
2   1   2   5   6
Ans :
CO-2; SO-1; BL-   [10]
5   Histogram Equalized Image:
2   4   5   2   4
5   3   7   7   7
2   7   1   3   2
1   4   2   7   6
3   2   3   5   6
Sketch the equalized histogram [ 02 Marks]
Stepwise Solution : 08 Marks
b   Apply Contrast Stretching Function for given 8-bit image and compute the output
the image.
0   100   200
F =
50   220   240
80   255   200
3
α = 0.4 , β = 2 , γ =
11
CO-2; SO-1; BL-   a = 100, b = 200, s1 = 40, s2 = 240   [10]
3
Also sketch contrast stretching graph.
Ans :
0   40   240
A =
20   246   251
32   255   240
Sketch the contrast stretching graph [ 02 Marks]
Stepwise Solution : 08 Marks
********** 4 **********
--- page 5 ---
Q5   [20]
Explanation of Morphological operations in Image Processing.
CO-3; SO-1; BL-   [06]
2   a   Minimum Four Morphological operations
b   Apply gray level slicing with Background and Without Background on the 3 bit
image shown below and compute the output of the image.
(Assume r1 = 3 and r2= 5 )
2 1 2 2 1
2 3 4 5 2
F = 6 2 7 6 0
2 6 6 5 1
[ 0 3 2 2 1]
Ans :
With Background :
CO-2; SO-1; BL-   2 1 2 2 1   [08]
3
2 7 7 7 2
6 2 7 6 0
2 6 6 7 1
[ 0 7 2 2 1]
Without Background :
0 0 0 0 0
0 7 7 7 0
0 0 0 0 0
0 0 0 7 0
[ 0 7 0 0 0]
CO-3; SO-1;   c   Explanation of Thresholding in Image Processing.   [06]
BL-2
Q6   [20]
a   Compute the DFT of x(n) = {1, 3, 6, 9} using MATLAB Script.   [05]
Also plot magnitude and phase response of X(K).
Print the script code, results and plot of X(K), magnitude of X(K), phase of X(K).
Ans. :
CO-1; SO-1; BL-
4   Script Code :
clc;
clear all;
close all;
x=input('Enter the sequence : ')
N=length(x)
xK=fft(x,N)
********** 5 **********
--- page 6 ---
n=0:N-1;
subplot (3,1,1);
stem(n,x);
xlabel('n---->');
ylabel('amplitude');
title('input sequence');
subplot (3,1,2);
stem(n,abs(xK));
xlabel('n---->');
ylabel('magnitude');
title('magnitude response');
subplot (3,1,3);
stem(n,angle(xK));
xlabel('n---->');
ylabel('phase');
title('Phase responce');
Results :
Enter the sequence : [1 3 6 9]
x =
1   3   6   9   [02]
N =
4
xK =
Columns 1 through 2
19.0000 + 0.0000i -5.0000 + 6.0000i
Columns 3 through 4
-5.0000 + 0.0000i -5.0000 - 6.0000i
Plot:
[03]
********** 6 **********
--- page 7 ---
CO-5; SO-1; BL- b   Implement image smoothing and sharpening using MATLAB.
3
Apply predefined 2-D prewitt filter for smoothing and unsharp masking for
sharpening to file ‘flower.jpg’ which is saved on desktop using MATLAB.
Print the script code, original image, smoothened image and sharpened image.
Ans. :
Script Code :
clc;
close all;   [06]
clear all;
a = imread('flower.jpg');
subplot(1,3,1);
imshow(a);
title('original image');
h = fspecial("prewitt");
b = imfilter(a,h);
subplot(1,3,2);
imshow(b);
title('smoothened image');
c = imsharpen(a);
subplot(1,3,3);
imshow(c);
title('sharpened image');
Plot :
[04]
Q7   [20]
a   Implement Band Pass FIR Filter for given design specifications using MATLAB:
Length of the filter = 20
Passband frequency:200 Hz
CO-4; SO-1; BL-
4   Stopband frequency:300 Hz
Sampling frequency:1000 Hz
window = hanning
********** 7 **********
--- page 8 ---
Print the script code, results and plot of magnitude response and phase response of
FIR Filter.
Ans :
Script Code:
clc;
close all;
clear all;
n = 20;
fp = 200;
fq = 300;
fs = 1000;
fn = [fp fq] / (fs/2);
window = hann(n+1);   [06]
b = fir1(n,fn,"bandpass",window);
[H W] = freqz(b,1,128);
subplot(2,1,1);
plot(W/pi,abs(H));
title('Magnitude Response of Band Pass FIR filter');
ylabel('Gain in dB');
xlabel('Normalised Frequency');
subplot(2,1,2);
plot(W/pi,angle(H));
title('Phase Response of Band Pass FIR filter');
ylabel('Angle');
xlabel('Normalised Frequency');
Plot:
[04]
********** 8 **********
--- page 9 ---
Implement relationships between pixels using neighbours of pixel for input 7 X 7
random matrix.
b
Print the script code, results for 4 point neighbour and 8 point neighbour of pixel
element at P(5,6).
Ans:
Script Code:
% To find Neighbour of a given Pixel
a=magic(7);
disp('a='); disp(a);
b=input('Enter the row < size of the Matrix');
c=input(' Enter the Column < size of matrix');
disp('Element'); disp(a(b,c));
% 4 Point Neighbour
N4=[a(b+1,c), a(b-1,c), a(b,c+1), a(b,c-1)];
disp('N4='); disp(N4);
%8 Point Neighbour
N8=[a(b+1,c), a(b-1,c), a(b,c+1), a(b,c-1), a(b+1,c+1), a(b+1,c-1), a(b-1,c-1), a(b-
1,c+1)];
disp('N8='); disp(N8);
Results :
CO-2; SO-1; BL-
3
Please note that following 7 X 7 matrix randomly generated so with respect to that
result will vary and kindly evaluate accordingly.
[06]
a=
30 39 48 1 10 19 28
38 47 7   9 18 27 29
46 6   8 17 26 35 37
5 14 16 25 34 36 45
13 15 24 33 42 44 4
21 23 32 41 43 3 12
22 31 40 49 2 11 20
Enter the row < size of the Matrix 5
Enter the Column < size of matrix 6
Element   [04]
44
N4=
3 36   4 42
N8=
Columns 1 through 7
3 36   4 42 12 43 34
Column 8
********** 9 **********
--- page 10 ---
45

FRR ICR 7 OI HOH
````
