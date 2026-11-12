# Modern Digital Signal Processing: question papers in full

4 unique papers · 2006-07 to 2009-10 · Electronics and Telecommunication

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2009-10 · Exam not stated · Trim 3 · ZIP of papers · paper 53823d66a8a4 · 2009-2010.pdf

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/TRIM III/Modern Digital Signal Processing/M Tech EXTC TRIM III Modern Digital Signal Processing 2009-2010.zip`
- Printed on paper: exam date: 10 May 2010
- Text: ocr (2 pages), mean OCR confidence 91.2

````text
SVKM’S N.M.I.MLS.
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT AND
ENGINEERING

M.Tech First Year (EXTC)
Trimester III, 2009-10

Subject : Modern Digital Signal Processing

Date 10 May 2010 Hal io com

Instructions : Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

NB: 1.Attempt any five questions.
2. All questions carry equal marks.
3. Answers to each new question to be started on a fresh page.

4. Figures in brackets indicate full marks.

Q1) Derive the Periodogram from the power-spectrum density estimate in non-parametric

analysis of random signals. What is the necessity of averaging periodograms ? (7)
(b) Describe the ARMA model for parametric spectral analysis. What is the power spectrum
for the auto-regressive model, and for the moving-average model? 6)

(c) What are the characteristics of an all-pass system? Show that H(z) = (¢'-a' \i(-a.z" ) is
an all-pass filter, where a is a complex number, and hence derive the frequency response. (7)

Q2) (a) Using the concept of Bilinear Transformation in IIR filters, derive the relationship
between discrete domain frequency @ and the continuous domain frequency {2 . Map the
frequency response in the discrete domain for an arbitrary response, and compare with
the frequency response in the continuous domain. (10)

(b) For the 3-point Moving-average digital filter given by the sequence :
y(nT) = [x(nT) + x(mT-T) + x(T-2T)] /3,
obtain the z-transform, the block diagram, the poles, and the frequency response. (10)

Q3) (a) For a sequence x(n), define Autocorrelation Pxx (k) , and hence derive the expression for
Power Spectral Density ®,,(@) from the Fourier Transform. Obtain the relationship
between the output P.S.D. ®,,(@) and the input P.S.D. ®,,(@), when a sequence x(n) is
filtered by a linear system mieie Transfer Function is given by He”). (12)

(b) For a uniformly distributed random signal {X{n]} with a probability density function
Pxjnj » the mean and variance are given by m,=2 and o,” = 1/3. When this sequence is
filtered by a } MOVER, average filter h{n] = {1/3 , 1/3 , 1/3}, find the mean my and standard
deviation 6, of the output sequence {Y[n]}. (8)

—_—i =
--- page 2 ---
ye
Q4) (a) Define a Hilbert Transform H(jo) and find the corresponding sequence h(n) from th.
Inverse Fourier Transform. (7)
(b) Write short notes on Matched filters and Inverse filters. (6)

(c) Show that the Fourier Transform of a sequence x(nT) obtained by sampling an analog
signal x,(t) is given by : X,(jQ) = (1/T). © (X(jQ —kQ;) where Q, = 27/T is the angular
sampling frequency. k (7)

Q5) (a) Describe in detail up-sampling and down-sampling, along with the consequent
alterations in the frequency spectrum. Under what conditions can aliasing be avoided in

down-sampling ? (8)
(b) Convert a system transfer function H(s) = (s+0.1)/ {(s+0.1)” +16} to an equivalent digital
filter using Bilinear transformation with a resonant peak at @, = 7/2, and verify. (12)

Q6) (a) Show that a low-pass filter can be transformed to a high-pass one by changing the
Laplace transform variable from s to s’ = Q2/ s where Q, is the -3dB corner frequency. (5)
(b) Show that a low-pass digital filter can be transformed to a high-pass one by replacing
H(@) by H(@-z) in the frequency domain. Hence find the corresponding transformation in
the impulse response h(n). (7)
(c) The difference equation corresponding to a low-pass filter is given by : y(n) = 0.9y(n-1) +
0.1x(n). What is the corresponding equation for a high-pass filter, and its frequency
response? (8)
````

## 2008-09 · Exam not stated · Trim 3 · ZIP of papers · paper b781fbb87d2f · 2008-2009.pdf

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/TRIM III/Modern Digital Signal Processing/M Tech EXTC TRIM III Modern Digital Signal Processing 2008-2009.zip`
- Text: ocr (2 pages), mean OCR confidence 84.0

````text
SUKM's Noaim§ Unw ERS ITY.
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENA ND ENGINEERING

A Dale :0Y-OS OF . \Q\
J SUBJECT:- Modern Digital Signal Processing MAX. MARKS:- ino
fo COURSE:- M. Tech TRIM IIT (2008-09)

DURA’ na 3 Hag urs
% A CO- 5-Ony Ws
N.B.: (1) Question No.1 is compulsory. \ eo
(2) Answer any four out of remaining six questions.
(3) Assume suitable data whenever required but justify the same.

1.Explain in brief (any four) : (20)

a) Let h(n) be the unit sample response of a low pass filter with a cutoff frequency , what type of filter
has a unit sample response g(n) = (-1)n h(n)?

b) Suppose that a discrete time sequence x(n) is bandlimited so that
X(e”)=0 0.32 <|ol<z
This sequence is then sampled to form the sequence y(7) = x(nN)
Where JN is an integer. Find the largest value for N for which x(m) may be uniquely
recovered from y(n)

c) Explain interpolation process with an example.
d) Compare bilinear and impulse invariant transformation.
e) Obtain the expression for the output y(n) in terms of x(n) for the multirate system given as follows

aN

x) ——* J 5 | 20 > | 4 > y(n)

2. a) Cosider the following specifications for a low pass filter

0.99 <|H(e”*)| <1.01 0<|o|<0.32 and

|H(e!*)|< 0.01 0.357 <|o| <7

Design a linear phase FIR filter to meet these specifications using the window design
method. (10)

b) Use the bilinear transformation to design a discrete time Chebychev high pass filter an
equiripple passband with

0<|H(e”))<0.1 O<|o\<0.17 and
‘
0.9<|H(e!”)| <i.0 0.32 <|o|<a (10)
3. (a) Consider the system shown in the figure below. (' °)
Ty Tr
Xa(t) x(n) re) Ya(t)
coment cf fo | M > D/C pon

Assume that the input is bandlimited, XY, (jQ) = 0 for Ql > 271000

PTO
--- page 2 ---
i. What constraints must be placed on M, 7, and T, in order for ¥,(f) to be equal to x,(t)?
ii, Tf f, = f, =20kHz and M = 4, find an expression for y, (0) in terms of x, (0)

4. (a)What is the need for short time

spectral analysis? Explain the technique for short time spectral
analysis for speech. (10)
(b) Explain the pole zero locations for Type I, Type II, Type III and Type IV linear phase FIR filters, (10)
5. (a) Consider the system y(n) = 0.5y(n-1) + x(n) (10)

i. Compute its response to the input x(n) = ( u(”) assuming infinite precision-arithmetic.

ii. Compute the response of the system

precision sign-and-ma
fractional bits). The q

Yn), OS n¥<5 to the same input, assuming finite-

gnitude fractional arithmatic with five bits (i.e. the sign bit plus four
uantization is performed by truncation.

(b) Explain applications of DSP in RADAR systems

(10)
6. (a) Explain polyphase decomposition process. (10)
(b) Explain Rounding and Truncation errors in FIR filters. 3 (10)

7. Write short notes on (Any two)

(20)
a. What is meant by limit cycles in recursive structures,

b. Power spectral estimation using Bartlett window.

cc.

Frequency domain characteristics of different window functions.

> x
````

## 2007-08 · Exam not stated · Trim 3 · ZIP of papers · paper d64870e01fd2 · 2007-2008.pdf

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/TRIM III/Modern Digital Signal Processing/M Tech EXTC TRIM III Modern Digital Signal Processing 2007-2008.zip`
- Printed on paper: duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 86.3

````text
y “a
Y
ON
SVKM’S N.M.LMLS. UNIVERSITY 3 a ~\
MUKESH PATEL SCHOOL OF TECHNOLOGY MAN. EMEN,AND \.
ENGINEERING =( NMIMS Un versity i
# ( ee oF 3|
_ Crelewen )- _
M.Tech {First Year
Trimester III, 2007-08
Subject : Modern Digital Signal Processing
Qole: 30-vy,-08 - caine oid

Time : 3 hours 2: 00-5: 0pm

Instructions : Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

NB : 1.Attempt any five questions.
Vv 2. All questions carry equal marks. :
3. Answers to each new question to be started on a fresh page.

4. Figures in brackets indicate full marks.

~~“ QT) (ay Show that afow-pass filter: carr be transformed to airigh-pass one by-cinmging the Laplace
transform variable from s to s‘ = Q,”/ s where Q, is the -3dB corner frequency. ~ (5)
(b) Show that a low-pass digital filter can be transformed to a high-pass one by replacing H(@)
by H(-z) in the frequency domain. Hence find the corresponding transformation in the impulse
response h(n). (7)
(c) The difference equation corresponding to a low-pass filter is given by : y(n) = 0.9y(n-1) +
0.1x(n). What is the corresponding equation for a high-pass filter, and its frequency response?(8)

Q2) Derive the periodogram from the power-spectrum density estimate in non-parametric analysis of
Ly random signals. What is the necessity of averaging periodograms ? (7)
(b) Describe the ARMA model for parametric spectral analysis. What is the power spectrum for
the auto-regressive model, and for the moving-average model? (6)
(c) What are the characteristics of an all-pass system? Show that H(z) = @i-a y(1- az") is an
all-pass filter, where a is a complex number, and hence derive the frequency response. (7)

Q4) (a) Using the concept of Bilinear Transformation in IIR filters, derive the relationship between
‘discrete domain frequency @ and the continuous domain frequency Q . Map the frequency
response in the discrete domain for an arbitrary response, and compare with the frequency
response in the continuous domain. (10)
(b) For the 3-point Moving-average digital filter given led the sequence : =
y(nT) = [x(nT) + x(nT-T) + x(nT-2T)] /3°, = ee a
obtain the z-transform, the block diagram, the poles, and the frequency response. ~~ (0)>>

PTO
--- page 2 ---
2.

Q4) (a) For a sequence x(n), define Autocorrelation g,,(k) , and hence derive the expression,
Power Spectral Density ®,, (@) from the Fourier Transform. Obtain the relationship betwe
output P.S.D. ®,, (@) and the input P.S.D. ®,,(@), when a sequence x(n) is filtered by a i
system whose Transfer Function is given by H(e"). (12)
(by For a uniformly distributed random signal { X{n}} with a probability density function pxjn) , ~~
the mean and variance are given bym,=2 and 6, = 1/3. When this sequence is filtered bya
moving average filter h[n] = {1/3 , 1/3 , 1/3}, find the mean my, and standard deviation oy of the

output sequence {Y[n]}: (8)
Q5) (a) Define a Hilbert Transform H(jo) and find the corresponding sequence h(n) from the

Inverse Fourier Transform. (7)

(b) Write short notes on Matched filters and Inverse filters. ; (6)

(c) Show that the Fourier Transform of a sequence x(nT) obtained by sampling an analog signal
x,(t) is given by : XQ) = (1/T). x (X,(jQ—kQ;) where Q, = 2z/T is the angular sampling
frequency. (7)

Q6) (a) Describe in detail up-sampling and down-sampling, along with the consequent alterations in
the frequency spectrum. Under what conditions can aliasing be avoided in down-sampling ?
(8) —
(b) Convert a system transfer function H(s) = (s+0.1)/{(s+0.1)° +16} to an equivalent digital
filter using Bilinear transformation with a resonant peak at @,= 7/2, and verify. (12)
````

## 2006-07 · Exam not stated · Trim 3 · ZIP of papers · paper 9a7ed8f5a6bc · 2006-2007.pdf

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/TRIM III/Modern Digital Signal Processing/M Tech EXTC TRIM III Modern Digital Signal Processing 2006-2007.zip`
- Printed on paper: duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 89.9

````text
Sv Pi
NMI moss UNIVERS IT y

AUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT AND ENGINEERING

_ SSUBJECT:- Modern Digital Signal Processing MAX. MARKS:-100
& COURSE:- M. Tech TRIM III (2006-07) DURATION:- 3 Hours
Dotc.- S[s] ot
N.B.: (1) Question No.1 is compulsory.
(2) Answer any four out of remaining six questions. /
(3) Assume suitable data whenever required but justify the same. }
1.Explain in brief (any four) : \ (20)
(a) Justify the statement ‘The frequency sampling realization of FIR filter needs fewer computations
especially for narrowband filers’.
(b) Show that the zeros of a linear phase FIR filter occur at reciprocal locations, also show that FIR filter
with antisymmetric impulse response and odd length will compulsory have zeroatz=land z=-l.
(c) Compare bilinear and impulse invariant transformation.
(d) Applications of multirate signal processing.
(e) Errors which arise due to quantization process while realization of filters.

2. Consider the analog lowpass filter specification given by
Passband: = -1<|H(jQ), $0, for 0<Q<10 _ rad/sec
Stopband: |H (ja) ap < 70% for Q>50 rad/sec

Sampling period T, = 10” sec.
(a) Determine the order of the Butterworth filter that satisfies the specification and draw the s-plane

pole/zero pattern. Transfer the poles to the z-plane using impulse invariant method. (9)
(b) Determine the order of the Chebyshev filter that satisfies the specification and draw the s-plane
pole/zero pattern. Transfer the poles to the z-plane using impulse invariant method. (9)
(c) Compare the order of the two filters. (2)

3. (a) Digital audio tape (DAT) drives have a sampling frequency of 48 kHz, whereas a compact disk (CD)
player operates at a rate of 44.1 kHz. In order to record directly from a CD onto a DAT, it is necessary
to convert the sampling rate from 44.1 to 48 kHz. Determine the specifications of the sampling rate
converter and associated filter. (10)

(b) Find the number of multiplications needed for computation of output for a filter used in a decimator of
5. Filter is, (10)
(i) FIR filter of length 16
(ii) IIR filter of length 6

4.(a) Explain polyphase decomposition process. (10)
(b) A two stage decimator has input sampling rate of 12 KHz and an output sampling rate of 400Hz.
f, = 180 Hz, f; = 200 Hz. Decimation factors are 15 and 2. Find the lengths of the two FIR filters

used and the number of multiplications per second of the two filters. Overall 5, = 0.002 and

6, =0.001 (10)

5.(a) What are the limitations of non-parametric methods in spectral estimation? How the parametric
methods overcome the limitations of the non-parametric methods? (10)
(b) Explain the applications of DSP in RADAR systems (10)

6.(a) What is the need for short time spectral analysis? Explain the technique for short time spectral analysis
for speech. (10)
(b) Design an low pass FIR filter which the following frequency response

PT

0
--- page 2 ---
H(e!”) =e a emt
4 4
ie 3x
H(e’’)=0 “/- <@<az
Use Hamming window. (10)

7.(a) Consider the system y(n) = 0.875 y(n -1) — 0.125 y(n -2) + x(n)
(i) Compute its poles and design the cascade realization of the system.
(ii) Quantize the coefficients of the system using truncation, maintaining a sign bit plus three other bits.
Determine the poles of the resulting system.
(iii) Repeat part (ii) for the same precision using rounding
(iv) Compare the poles obtained in parts (ii) and (iii) with those in part (i) (10)

(b) What is meant by limit cycles in recursive structures. (10)

— xX —
````
