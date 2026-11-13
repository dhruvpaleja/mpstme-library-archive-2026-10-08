# Advance DSP: question papers in full

12 unique papers · 2010-11 to 2016-17 · Electronics and Telecommunication, Electronics

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2016-17 · Final-Exam · Sem 2 · paper 503b08ebd676

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/II SEMESTER/ADVANCES DSP/Advanced DSP 2016-17 Final.pdf`
- Printed on paper: exam date: 4 May 2017
- Text: ocr (2 pages), mean OCR confidence 91.1

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: M. Tech (EXTC) _ Year:1 | Semester: II °
Academic Year: 2016-2017
Subject: Advanced DSP -

Date: 4 May 2017 Time: 2

No. of Pag

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 04 questions.

3) In all 05 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks. .

7) Assume Suitable data if necessary,

QI. (a) State True / False with proper justifications. (02 MARKS each)

(i) In Welch method the power spectrum estimation is obtained by periodogram averaging using non-

overlapping segments.

(ii) Anti-imaging filter is used in an interpolator.

(iii) In sampling rate conversion by rational factor, decimation is performed after interpolation to preserve
spectral characteristics.

(iv) In case of FIR filter design using windows, a shorter window is better than a longer one.

(b) (i) Determine the output y[n] in terms of input x[n] for the given multirate system. (03 MARKS)

x[n] —> T4 > 112 T3 --—> yln|

(ii) Determine the order of a Chebyshev filter for the following specifications. Passband ripple is 3 dB for
0<|w|<0.2z. At least 25 dB attenuation for 0.451 <|w|<x. (03 MARKS)

Q2. (a) Determine coefficients of Discrete Wavelet Transform for the signal, x(n)={1, 2, 0, -2}using Haar wavelet.
(07 MARKS)

Page 10f2
--- page 2 ---
(b) The transfer function of an FIR filter is H(z) = 0.2 + 0.7271 + 0.827? + 0.15273 + 0.6274 + 0.32275 +
0.52-© + 0.4z~7 + 0.9278. Perform polyphase decomposition of H(z) to decompose into (i) 2 sections (ii)
3 sections. (07 MARKS)
Q3. (a) Find the impulse response h[n] of a filter having desired frequency response which is given by
Inve for0<|al < 1
; or0< |o| <=
Hg (ei) = 1 2
0 for z <lo|<z

It is given that N = 7. Use:frequency sampling approach. (08 MARKS)

‘ jes
(b) Consider the spectrum of the signal x[n] shown in the figure. Ix(e”*)|
Determine the spectrum of downsampled version of the signal —1 rt
for sampling rate reduction factor (i) 2 (ii) 3. (06 MARKS) 2 2 <2)

Q4. (a) Design a second order bandpass digital Butterworth filter with passband of 200Hz to 300Hz and sampling
frequency of 2000Hz using bilinear transformation. (08 MARKS)

(b) Compare parametric and non-parametric techniques of spectral estimation. Explain in detail any one
technique for parametric method of spectral estimation. (06 MARKS)

QS. (a) Design a normalized linear phase FIR lowpass filter using windowing technique having the phase delay of
t = 4 and at least 40 dB attenuation in the stopband. Also obtain the expression for the magnitude response of
the filter. (07 MARKS)

(b) Given a two channel Quadrature Mirror Filter Bank, derive the conditions for perfect reconstruction, aliasing
cancellation and no amplitude and phase distortion. State the relation between the analysis and synthesis
filters. Also state why this filter is known as Quadrature Mirror Filter Bank. (07 MARKS)

Q6. (a) Describe Chebyshev polynomial and extermal frequencies in relation to the optimum FIR filters.

(07 MARKS)

(b) What is linear prediction modelling? Explain the Levinson—Durbin algorithm for calculation of linear
predictor coefficients (07 MARKS) ,

Q7. (a) Compare Short Time Fourier Transform and Continuous Wavelet Transform with respect to their
mathematical representation, advantages, disadvantages, time frequency plane and applications.

(08 MARKS)

(b) What are the advantages of using lattice predictors? Using suitable diagram explain the configuration of a
lattice predictor and its inverse. (06 MARKS)

Page 2 of 2
````

## 2015-16 · Final-Exam · Sem 2 · paper 0d19540cbd21

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/II SEMESTER/ADVANCES DSP/Advanced DSP 2015-16 Final.pdf`
- Printed on paper: max marks: 70; duration hours: 3; exam date: 05/05/2016
- Text: ocr (2 pages), mean OCR confidence 94.2

````text
SVKM’s NM
MUKESH PATEL SCHOOL OF TECHNOLOG

Programme: M. Tech (EXTC) Year: I

Academic Year: 2015-2016

Subject : Advanced DSP
Marks: 70

Date : 05/05/2016 . Time : 2.00 pm to 5.00 pm
Durations: 3 (hrs)

Final-Examination

Instruction: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.

NB:

1) Question No. | is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary

Q. 1 State whether the following statements are true or false. Justify the answer in brief. (14)
(a) An FIR filter is designed using windowing technique. If required length is N then Rectangular
window provides less transition bandwidth than Hamming window.
(b) Butterworth filter has a maximally flat response in pass band and ripple in stop band.
(c) The selected frequency points in frequency sampling technique are the samples of DFT.
(d) Toeplitz matrix is symmetric about the diagonal and diagonal elements are zero.
(e) TheWelch method allows the signal segments to overlap.

(f) An interpolator requires a filter to avoid aliasing.
(g) Wavelet transform uses high pass filter to extract the detail function.

Q. 2 (a) Desired frequency response of a DT filter is shown below. Use windowing technique to design
the filter of length 7. Use Hamming window. Draw the structure for the designed filter. If an input
signal of the frequency range, 300 Hz to 2500 Hz is sampled with 8000 Hz then determine the
frequencies which fall within the pass band of the filter.

jw
[H(e )|
1,
3n/4 3n/4 w (10)
(b) Describe dilation and translation in relation to mother wavelet. (4)

Page 1 of 2
--- page 2 ---
Q.3 (a) Design a linear phase High Pass FIR filter of length 13 using type I frequency sampling
technique for the cut off frequency of 0.77. (7)

(b) Use efficient polyphase structure realization to implement a decimator for M = 2. Impulse
response of the filter used in decimator is
h(n) = {0.05, -0.06, -0.09, 0.15, 0.15, -0.09, -0.06, 0.05}
Justify that the above structure is more efficient than the other polyphase structure. (7)

Q. 4 (a) List limitations of non parametric methods for power spectrum estimation. Explain in brief how
Pi Pp P P
parametric method avoids these limitations. (4)

(b) Justify that the sample rate conversion of 2/5, uses upsampler followed by the downsampler.
If input sequence, x(n) ={ 2,3,5,1,2,6} then the determine the time domain output of the sample
rate convertor. Plot the frequency response at the output of convertor.

jw
xX(e )
1
(10)
| |
-2n T/4 (6) n/4 2n w
Q5. (a) Describe least square method for the design of IIR filters. (7)
(b) Draw a block schematic of a forward prediction error filter and derive expression for the

prediction error normal equations. (7)

Q6. (a) Determine the order of a digital Butterworth low pass filter for passband and stop band edge
frequency of 1000 Hz and 3000 Hz respectively. Pass band and Stop band attenuations are 3dB
and 40 dB respectively. Sampling frequency is 8000Hz. Determine the transfer function of the
designed filter. Transform the filter to high pass filter. (10)

(b) List features of Chebyshev filter. (4)

Q. 7 (a) Draw a block schematic for Barlett and Welch method for power spectrum estimation and
explain algorithm. (7)

(b) Describe multi resolution analysis using wavelet transform show its application for image
compression. (7)

Page 2 of 2
````

## 2014-15 · Final-Exam · Sem 2 · paper 0c6c82727cd7

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/II SEMESTER/ADVANCES DSP/Advanced DSP 2014-15 Final.pdf`
- Printed on paper: max marks: 60; duration hours: 3; exam date: 06/05/2015
- Text: ocr (3 pages), mean OCR confidence 87.5
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’s NMIMS PA ew
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT aseuyeenin »
ST MPSTME Yo t
Programme: M.Tech (EXTC) Year: I Semester: II AC LIVPRARY pe
; Ses wg %
Academic Year: 2014-2015 SS neg RS e
Subject: Advanced DSP een
Marks: 60
Date: 06/05/2015 Time : 10.00 am to 1.00 pm

Durations: 3 (hrs)

Final-Examination

Instruction: Candidates should read carefully the instructions printed on the question paper and
on the cover of the Answer Book, which is provided for their use.

NB:

1) Question No. | is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all five questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary

Q1.Answer any three out of four. (3 x 4=12)
(a) Find all the zeros location and the transfer function of a causal Type-1 linear phase FIR
filter of minimum length if it has a zero at z=0.5ei"3 and a zero at z=1.

(b) An IIR digital LPF has a pass band edge frequency wp=0.32. What is the pass band edge
frequency in Hz of the prototype analog LPF if the digital fi

(i) the impulse invariant method and (ii) the bilinear transfo
T=0.1ms?

Iter has been designed using
rmation method with

(c) In the system of figure given below, fi
terms of x (n).

wan) >{r3 {dy iS Lf = a = = > y (hn)
J {eae | Li >

nd Y (z) in terms of X (z).In addition find y (n) in

(d) What do you mean by Short time Fourier Transform?

Q2. (a) Determine the anti-aliasing FIR filter lengths and cutoff frequencies for the two-stage
decimator with the following specifications and block diagram.

(6M)
--- page 2 ---
abe

Original sampling rate: fs = 240 kHz

Audio frequency range: 0-3,400 Hz
Passband ripple: 5p = 0:05 (absolute)
Stopband attenuation: 5s = 0:005 (absolute)
FIR filter design using the window method
New sampling rate: fav = 8 kHz

XA) Stage Mice, ee ee ee
Anti-aliasing _ | : : [Anti-aliasing ; ; » y¥(m)
: filter H1(z) [im | ‘ filter H2(z) iM :
A
(b) Sketch the lattice structure for the (6M)

1-0.8271+4 0.15272
1+0.1z71- 0.72 2-2

H(@)=

Q3.(a) Explain the effect of dilation and translation of a function g(t) in frequency domain.
(6M)
(b) Consider a length 8 FIR system function shown given by
H(z) =1+0.5z! + 0.42? - 0.623 + 24 +1.225 + 0.22% + 0.127
Develop a four branch polyphase realization of H (z) and determine the expressions for the
polyphase transfer functions Eo (z), Ei(z), E2(z) and Es(z) . From this realization, develop a
canonic four-branch polyphase realization of H (z). (6M)

Q4.(a) Design a linear phase FIR digital LPF of unity gain using Hamming window whose cut —
off frequency is 1.2 rad/sample and length of window M=9.Assume the necessary data. (6M)

(b) What is multiresolution analysis? How it is performed using filter banks? (6M)

Q5. Derive the expression for Levinson Durbin recursion to find the predictor coefficients.
(12M)

Q6(a) Find Y1 to Y9 in the Two Channel Filter Bank after interchanging down sampler and up
sampler as shown in fig.

— Yue

TON Vat TIN Vel

“(12)

+| HyZ) | a

(6M)
--- page 3 ---
(b) Explain Hilbert transformers. (6M)

Q7.(a) Explain the performance characteristics of Welch power spectrum estimate and Blackman

Tukey power spectrum estimate. (6M)
(b) Determine the poles of Butterworth Low Pass Filter for N=3. Sketch the poles of
Ha(s)Ha(-s) and hence determine the system function Ha(s). (6M)
````

## 2014-15 · Re-Exam · Sem 2 · paper 0d69a3cb178e

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/II SEMESTER/ADVANCES DSP/Advanced DSP Batch 2014-15 Re Exam.pdf`
- Printed on paper: exam date: 29/06/2015
- Text: ocr (2 pages), mean OCR confidence 88.7

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: M. Tech (EXTC) Year: I Semester: II

Batch: 2014-15
Academic Year: 2014-2015

Subject: Advanced DSP ne

J, ge Ray 60
Date: 29/06/2015 a 10.00 am to 1.00 pm
. s: 3 (hrs)

R 2Bxamination /

NP =
; — Ges

. SU A

eal

Instruction: Candidates should read carefully the instructions printed on the question paper and
on the cover of the Answer Book, which is provided for their use.

NB:

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) Inall_5 questions to be attempted,

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary

Q1.Answer any three out of five. (3 x 4=12)

(a) Why filter is required for interpolator. Draw spectrum and the output of interpolator after
filter.

(b) Discuss FIR diffrentiator giving impulse response and transfer function.
(c) Give the various steps in parametric estimation process.

(d) Discuss autoregressive model and filter.

(e) Explain STFT.

Q2.(a) A three stage decimator is used to reduce the sampling rate from 3072KHz to 48 KHz.

Xn)
—>—\h ve phecky Wa H face
3072 tye | (CK) thacie)|~ AQEH2
Steg | Steger Stege3

Indicate sampling rate at output of each of three stages. Write Overail decimation factor.

(6 M)
(b) Sketch the lattice structure for (6M)

H(z) = 1-0.8z74+ 0.1527
~ 140.1272— 0.72 272

ae
--- page 2 ---
Q3.(a) The desired unit sample response is ha(n) =2(0.5)"u(n).Determine the parameters of filter
with system function

H(2) = bo + byz7}

ne a,z~+

using Pade’s approximation technique. (6M)
(b) Explain relation of DWT with filter banks. (6M)

Q4. (a) Discuss the use of DFT in power spectrum estimation. (6M)

(b)Design a first order digital LPF with 3-dB cut off frequency of 0.252 by applying bilinear
transformation for Butterworth approximation. (6M)

QS. Derive the expression for Levinson Durbin recursion to find the predictor coefficients.

‘ (12M)
Q6 (a) A FIR digital filter is characterized by transfer function
H(z) = Dot h(n)z™
where M=11.Determine and sketch the frequency response of the filter. (6M)

(b) The analysis side low pass filter of a two-band, perfect reconstruction, orthogonal (CQF)
filter bank has an impulse response h{n] supported on the interval n = 0 to n = 5.Obtain the
impulse response of the other three filters. (6M)

Q7 (a) Write short notes on any two (6x2=12)
(i) Frequency sampling method of filter design
(ii) | Application of wavelet in image processing
(iii) Quadrature mirror filter

2 A
````

## 2013-14 · Final-Exam · Sem 2 · paper c10e90f33f24

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/II SEMESTER/ADVANCES DSP/Advanced DSP 2013-14 Final.pdf`
- Printed on paper: exam date: 06/05/2014
- Text: ocr (2 pages), mean OCR confidence 86.2
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme:M. Tech (Electronics & Telecommunication) Year:1 Semester: II

Academic Year: 2013-14

capone at a,

Subject : Advanced DSP aS
Marks; A> .

Date : 06/05/2014 Time { £00 Oat té Ka te
Dura' Be s 3 irs) s

Final Examination te ax

* ~ —Z
rar aa

Instructions: Candidates should read carefully the instructions printed on the question paper
and on the cover of the Answer Book, which is provided for their use.

1. Question No. | is compulsory.

2. Out of remaining questions, attempt any 4 questions.

3. Inall 5 questions to be attempted.

4. All questions carry equal marks.

5. Answer to each new question to be started on a fresh page.

6. Figures in brackets on the right hand side indicate full marks.

Ql Attempt any four (S marks each) 20
(a) Obtain the expression for output y(n) in terms of x(n) for the multirate system shown Pi]
below.
actn) ;
—af5 y20 bolt 4 Fe gm
(b) Determine the lattice Coefficients corresponding to the FIR filter with system function 5

H(z)=1+2z"'+1/3z?

(c) Explain gibb’s phenomenon. How it can be eliminated? 5
(d) Explain periodogram for power spectrum estimation. 5
(e) system is given by 5

Where a and b are real with a#b. Show that |H(e)} is constant if ab=1 and determine its
value. Find the phase response?

2 (a) What is multiresolution analysis? How is it performed using filter banks? 10

(b) Find the squared magnitude response of a filter, which has two pole P,. = 0.8e**” and two 10

zeros at origin. Plot it w.r.t. frequency and identify the filter type based on passband.
3 (a) FIR LTI system has an impulse response h(n) which is real valued, even and has finite 10

duration of (2N +1). Show that if Z,;=r ¢"° is a zero of system, then z=(//r)e"” is also a zero
of the system.

(b) Consider a signal x(n)= s(n)+w(n),where s(n) is an AR(1) process that satisfies the difference 10
equation

S(n)= 0.8s(n-1)+v(n)

V/2.
--- page 2 ---
Q4

Q5

Q6.

Q7

(a)

(b)

(a)

(b)

(a)
(b)

Where {v(n)} is a white noise sequence with variance o”,= 0.49 and {w(n)} is a white noise
sequence with white noise sequence with variance one.The processes {v(n)} and {w(n)} are
uncorrelated.

(a) Determine the autocorrelation sequences {Yxx(m)} and {Yss(m)}.
(b) Design a wiener filter of length M=2 to estimate {s(n)}.

Design a butterworth digital LPF using bilinear transformation ny taking T=0.1 to satisfy 10
following specifications.


The transfer function of IIR filter is H(z)= 1+0.7z-1/1-0.9z-1. 10

Perform polyphase decomposition into 4 sections.

Derive the expression to find minimum mean square prediction error for a forward prediction fil 10

filter.

The desired response of low pass filter is 160
—sSw —aT]4 Gv < 3074

‘ e
Ra Ces) = ie) Onewiee .

Determine H(ejw) for M=7 using hamming window.

Discuss application of DSP in denoising ECG signal. 10
Explain use of DFT in power spectrum estimation. 10
Explain the role of wavelets in satellite Image denoising and Image compression. 20

xX:

2a
````

## 2013-14 · Re-Exam · Sem 2 · paper 0df0c907be47

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/II SEMESTER/ADVANCES DSP/Advanced DSP Batch 2013-14 Re Exam.pdf`
- Printed on paper: exam date: 30/06/2014
- Text: ocr (2 pages), mean OCR confidence 88.1

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme:M. Tech (Electronics & Telecommunication) Year: I Semester: II
Academic Year: 2013-14 Pines
RN
Batch:2013-2014 / i Ne
} MPSTME ye
Subject : Advanced DSP - Marks:1 on 6 LIBRARY dé
Time : 1 m to 1.00 pgs
Date :30/06/2014 Durations» re J

Re-Examination

Instructions: Candidates should read carefully the instructions printed on the question paper
and on-the cover of the Answer Book, which is provided for their use.

1. Question No. | is compulsory.

2. . Out of remaining questions, attempt any 4 questions.

3. Inall 5 questions to be attempted.

4. All questions carry equal marks.

5. Answer to each new question to be started on a fresh page.

6. Figures in brackets on the right hand side indicate full marks.

Ql Attempt any four (S marks each) 20

(a) The signal x(n) is defined by 5

iain, [es we
0, otherwise

Obtain:
(i) Decimated signal with a factor of three.
(ii) Interpolated signal with a factor of three.
(b) Show POLE ZERO locations of normalized fourth order Butterworth IIR filter 5
(c) Explain time frequency analysis. . 5
(d) Explain periodogram for power spectrum estimation. 5
(e) A stable filter is always causal. True or False? Justify your answer. 5
2 (a) What is STFT.Explain with mathematical analysis. 10
(b) Compare parametric and non parametric methods for power spectrum estimation. 10
3 (a) Determine the system function of the all pole filter described by the lattice coefficients 10
K1=0.6,K2=0.3,K3=0.5, and K4=0.9.
(b) Consider a signal x(n)= s(n)+w(n),where s(n) is an AR(1) process that satisfies the difference 10
equation

S(n)= 0.8s(n-1)+v(n)
Where {v(n)} is a white noise sequence with variance o*, = 0.49 and {w(n)} is a white noise
sequence with white noise sequence with variance one.The processes {v(n)} and {w(n)} are
uncorrelated.
(a) Determine the autocorrelation sequences {Yxx(m)} and {Yss(m)}.
(b) Design a wiener filter of length M=2 to estimate {s(n)}.

Q4 (a) Design a butterworth digital LPF by impulse invariance method for the following 10

/2.
--- page 2 ---
Qs

Q6.

7

(b)

(a)

(b)

(a)
(b)

(a)
(b)

specifications:-

(i) Passband gain required=0.9

(ii) Frequency up to which passband gain must remain more or less steady= 100
rad/sec

(iii) Gain in attenuation band = 0.4

(iv) Frequency from which attenuation must start=200 rad/sec.

The transfer function of IIR filter is H(z)= 1+0.7z-1/1-0.9z-1.

Perform polyphase decomposition into 2 sections.

Derive the expression to find minimum mean square prediction error for a backward prediction

filter.
The desired response of low pass filter is
-- ess = 3/4 gw ge 3%
ig (e2”) =
oO Other tae

Determine H(ejw) for M=7 using hanning window.

Discuss application of DSP in digital voice recording.

How can energy density spectrum can be determined for a discrete time system.

Give mathematical conditions for CTWT and DWT.

Discuss four applications of Wavelet Transform.

—————?

2/2

10

10

10

10
10

10
ite)
````

## 2012-13 · Final-Exam · Trim 2 · paper 423f6f45b27e

- Departments: Electronics, Electronics and Telecommunication
- Programmes: M TECH / ELECTRONIC, M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ELECTRONIC/TRIM II/ADVANCE DSP/Advanced DSP 2012-13 Final.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07/02/2013
- Text: ocr (2 pages), mean OCR confidence 83.0
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
u
7

a ym
¢ Harerne®

Bl LIBRARY ds

Xon UZ A$ /
SVKM’s NMIMS Minis *
Mukesh Patel School Of Péchnology Management & Engineering ~~~
Programme: M Tech - ELEX / EXIC Year: [| Trimester: II
Academic Year : 2012-2013

Subject: ADVANCED DSP Marks: 100
Time: 2.00pm To 5.00pm
Date: 07/02/2013 Duration: 3 hrs.

Final - Examination

Instructions: Candidates should read carefully the instructions printed on the question
paper and on the cover of the Answer Book, which is provided for their use.

NB:
1. Answer to each new question to be started on a fresh page.
2. Question no. 1 is compulsory.
3. From the remaining questions, attempt any four questions.
4. In all five questions to be attempted.
5. Figures in brackets on the right hand side indicate full marks.

Q: 1) Write notes on any two of the following: (20 Marks)
a) Applications of DSP in Video Processing.

b) Explain the principle and procedure for designing FIR filter using rectangular
window.

c) Weiner Filters.

Q: 2) (20 Marks)
(a) find the order an¢ cuLoff frequency of a digital fitter with following specifications
BgsjHCe sist, Ocos04an
tHe )[ s 0.48, O6nSuwen

Use impulse invatiance method
(b} Draw its poles.

Q: 3) (20 Marks)

Sesign the digital high pass filter for cut-off frequency of 30 Hz and sampling frequency
of 150 Hz using BLT.

My
--- page 2 ---
Q:4) a) (10 Marks)
A linear phase FIR filter has response given by e~)”°. What is the order of filter
Justify your answer.

b) (10 Marks)
Obtain the polyphase structure of the filter with the transfer function
1-32"
H(z) = =
) 1+4z"
Q: 5) (20 Marks)
An WR iow pass filter is required tc meet the following specfications
Passband peak fa peak rippe > s1dB
Passband edge > 4.2 kHz
Stopband attenuation ' 2 40 6B
Stopband edge 2.5 kz
Sample rate € kHz
The fiter is to be designed by performing BLT on ean anelog system function of

tecuired order butterwvorth fitter so as to meet the specifications in the implementation.

Q: 6) Write short note on any two: (20 Marks)
a) Discuss the relative merits and de-merits of Windowing method.
b) Write short note on Forward Linear Prediction.
c) Compare IR and FIR filters. List the steps required to design IIR filters.

Q:7) (20 Marks)

The power density spectrum of an AR process [xin)] is given as

C,

Pes = Foes
al aie

25


where o is the vatiance of the input sequence.

(a) Determine the difference equavon for generating the AR process when the ex-
citation is white noise.

(b) Determine the system function for the whitening filter.

X

“fo
````

## 2012-13 · Re-Exam · Trim 2 · paper 0bede0e20618

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/TRIM II/ADVANCE DSP/ADAVANCED DSP II M TECH (EXTC) 2012-13 RE EXAM.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 13/6/2013
- Text: text (2 pages)

````text
SVKM's NMIMS
Patel School
Programme:   . EXTC   Year:   I   Trimester:   I1
Academic Year :2012-2013
Bat&:   2012-2013
Subject:   Adavanced DSP   Marks:   100
Time:   10.00 am 'I'o 1.00pm
Date:   13/6/2013   Duration: 3hrs.
Re - Examination
.-
Instructions: Candidates should read carefully the instructions on the questlon paper and on the cover of
the Answer Book, which is provided for then use.
NB:
I. Question No. 1is cdmpulsory
2. Out of remaining questions, attempt any 4 questions
3. In all 5 questions to be answered
4. Answer to each new question to be started ona fresh page
~~   .~   5.Figures in brackets on the right hand side indicate full marks
1.   Attempt any four questions
(a) List the various methods for non-parametric power spectnun estimation. What quality metric:
is used to evaluate the performance of these methods?   ,   [51
(b) What is Hilbert Transformer? Derive the impulse response of Hilbert Transformer.   I   151
(c) What are the drawbacks of Fourier Transform analysis and how can Wavelet Transform
overcome them?   q   l5i
(d) Obtain the ply-phase decomposition of the W system with transfer function_'
H(z)= - 1-22-'   [51
1+ 32-'
(e) What is the purpose of FIR differentiator? Derive the impulse response of FlR differentiator. :   [5]
s+o.1
1   I Convert the analog filter with tnlnsfer function H(s)=   into a digital IIR flter'
(s+o.1)1+9
using impulse invariance method.
(b) What are the advantages of multi-rate signal processing?   -   151
(c) Define periodogtain and explain its purpose.   151
3.
(a) A one-stage decimator is characterized by the following: Decimation Factor = 3, ~nti-'
aliasing filter coeE1cients: h(0) = h(4) = -0.06, h(1) = h(3) = 0.30, h(2) = 0.62. Given the
input datax(n) with values [6, -2, -3, 8, 6, 4, -21, calculate and list the filtered output w(n);   I101
and the output of the decimator y(m).
11 2
--- page 2 ---
. .
>.   (b) I Describe any two applications of Wavelet Transforms in detail.   - ,   I [lo1
. ..   I   I
4.
(a) What type of problems can be solved using Wiener Filter?   151
(b) Consider an AR process of order 1, described by x(n) = mi$-1) + w(n) where a is a constant
and (wfn)) is a white noise process of zero mean and variance 2. Find the mean and   1101
autocorrelation function of the process {x(n)}.
(c) Transform the   single-pole   low-pass   Butterworth   filter with system   ftu~ction
into a band-pass filter with upper and lower band edge frequencies dl. and
5.   1
(a) I What properties and conditions should be satisfied by a mother wavelet fiction?   [   [5]
@) Design an FIR digital filter to approximate an ideal low-pass filter with passband gain of
unity, cut-off frequency of 850 Hz and working at a sampling ftequency off, = 1500 Hz. The   [lo]
length of the impulse response should be 5. Use arectangnlar window.
(c)   Consider a system with transfer function H(z) = z - ~-a ,la1 < 1. Show that this is an all-
I-U-~   151
pass filter.
Develop an expression for the output y[n] as a function of the input x[n] for the multi-rate
structure as shown:
151
with suitable diagrams how to achieve sampling rate conversion by a rational factor
(c) Determine the frequency resolution of the Welch and Blackman-Tukey methods of power
spectrum estimates for a quality Eactor Q = 10. Assume that overlap in Welch's method is   [5]
50% and the length of the sample sequence is 1000.
rk
7,
(a) Explain how DSP can be applied in Image Processing.   1101
(b) Derive the Wiener-HopfOequation for FIRWiener filter.   1101
````

## 2011-12 · Exam not stated · Trim 2 · paper ce3b6c37d883

- Departments: Electronics, Electronics and Telecommunication
- Programmes: M TECH / ELECTRONIC, M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ELECTRONIC/TRIM II/ADVANCE DSP/ADVANCED DSP.pdf` (+1 identical copies)
- Printed on paper: duration hours: 3; exam date: 03/02/2012
- Text: ocr (2 pages), mean OCR confidence 88.7

````text
a SVKM’s NMIMS
Mukesh Patel School Of Technology Management & Engin

_Programme: M. Tech- ELEX / EXTC Year: I Trimester;
Academic Year : 2011-2012

| * svKe's \*
Subject: ADVANCED DSP Marks{>( oo 2) Ve
Time: , «C 20s prmyTo stp m
Date: 03/02/2012 Duration, 3 hrs. oe3
Final - Examination Ne ae
SY MANAGENS

Instructions: Candidates should read carefully the instructions printed on the question paper and
on the cover of the Answer Book, which is provided for their use

NB:
1. Question No. 1 is compulsory
2. Out of remaining questions, attempt any 4 questions.
3. Inall 5 questions to be attempted
4. Answer to each new question to be stared on a fresh page
5. Figure in brackets indicate full marks
1. Attempt following questions (any 4) [20]

(a) | Obtain the mapping formula for bilinear transformation method.

(b) | Obtain the polyphase decomposition of the I[R system with transfer function.
1-42"!

1+5z7

H(Z)=

(c) | What are the limitations of non-parametric methods in spectral estimation?

(d) | What are the various applications of Wavelet Transform?

2.(a) | Design a digital Butterworth low pass filter satisfying the following specifications | [10]
using bilinear transformation (Assume T = 1 Sec)

09<|H(e™) <1,   Oswsn
|H(e™)| < 0.2, 3n/4<w<n

(b) | Implement a two stage decimator for the following specifications. [10]
; | Sampling rate of the input signal = 20,000 Hz
* |M=100

q }| Pass band = 0 to 40 Hz
Transition band = 40 to 50 Hz
Pass band ripple = 0.01
Stop band ripple = 0.002

3.(a) | What is a linear phase filter? What conditions are iu be satisfied by the impulse | [16]
response of an FIR system in order to have a linear phase? Plot and justify
compulsory zero locations for symmetric and antisymmetric even and
antisymmetric odd FIR filters.

(b) | Explain how AR parameters are obtained by using linear prediction. [10]

h
--- page 2 ---
——

—
| 4.(a) | Define parametric and non-parametric methods of power spectrum estimation. | [12]
| Explain the non-parametric methods of power spectrum estimation.

(b) | Explain the interpolation and decimation process with an example. [8]
| 5.(a) | Explain the forward —backward lattice algorithm. [10]
| (b) | State and explain the important properties of CWT [10]
| 6.(a) | Discuss application of DSP in Image Processing. [8]
|

| (b) | What is the need for short time spectral analysis? {5]

(c) | Determine the frequency resolution of the Bartlett, Welch methods of power } [7]
| spectrum estimates for a quality factor Q = 10. Assume the overlap in Welch’s
| method is 50% and the length of the sample sequence is 1000.

| 7.(a) | Write a short note on Wiener Filter. [10]

1 0) Explain with block diagram signal processing in radar system. [10]

sak

x

v7

fa
````

## 2011-12 · Exam not stated · Trim 2 · ZIP of papers · paper e4c679642dd8 · ADVANCED DSP.pdf

- Departments: Electronics
- Programmes: M TECH / ELECTRONIC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ELECTRONIC/TRIM II/ADVANCE DSP/M Tech ELECTRONIC TRIM II ADVANCED DSP.zip`
- Printed on paper: duration hours: 3; exam date: 03/02/2012
- Text: ocr (2 pages), mean OCR confidence 88.7

````text
a SVKM’s NMIMS
Mukesh Patel School Of Technology Management & Engin

_Programme: M. Tech- ELEX / EXTC Year: I Trimester;
Academic Year : 2011-2012

| * svKe's \*
Subject: ADVANCED DSP Marks{>( oo 2) Ve
Time: , «C 20s prmyTo stp m
Date: 03/02/2012 Duration, 3 hrs. oe3
Final - Examination Ne ae
SY MANAGENS

Instructions: Candidates should read carefully the instructions printed on the question paper and
on the cover of the Answer Book, which is provided for their use

NB:
1. Question No. 1 is compulsory
2. Out of remaining questions, attempt any 4 questions.
3. Inall 5 questions to be attempted
4. Answer to each new question to be stared on a fresh page
5. Figure in brackets indicate full marks
1. Attempt following questions (any 4) [20]

(a) | Obtain the mapping formula for bilinear transformation method.

(b) | Obtain the polyphase decomposition of the I[R system with transfer function.
1-42"!

1+5z7

H(Z)=

(c) | What are the limitations of non-parametric methods in spectral estimation?

(d) | What are the various applications of Wavelet Transform?

2.(a) | Design a digital Butterworth low pass filter satisfying the following specifications | [10]
using bilinear transformation (Assume T = 1 Sec)

09<|H(e™) <1,   Oswsn
|H(e™)| < 0.2, 3n/4<w<n

(b) | Implement a two stage decimator for the following specifications. [10]
; | Sampling rate of the input signal = 20,000 Hz
* |M=100

q }| Pass band = 0 to 40 Hz
Transition band = 40 to 50 Hz
Pass band ripple = 0.01
Stop band ripple = 0.002

3.(a) | What is a linear phase filter? What conditions are iu be satisfied by the impulse | [16]
response of an FIR system in order to have a linear phase? Plot and justify
compulsory zero locations for symmetric and antisymmetric even and
antisymmetric odd FIR filters.

(b) | Explain how AR parameters are obtained by using linear prediction. [10]

h
--- page 2 ---
——

—
| 4.(a) | Define parametric and non-parametric methods of power spectrum estimation. | [12]
| Explain the non-parametric methods of power spectrum estimation.

(b) | Explain the interpolation and decimation process with an example. [8]
| 5.(a) | Explain the forward —backward lattice algorithm. [10]
| (b) | State and explain the important properties of CWT [10]
| 6.(a) | Discuss application of DSP in Image Processing. [8]
|

| (b) | What is the need for short time spectral analysis? {5]

(c) | Determine the frequency resolution of the Bartlett, Welch methods of power } [7]
| spectrum estimates for a quality factor Q = 10. Assume the overlap in Welch’s
| method is 50% and the length of the sample sequence is 1000.

| 7.(a) | Write a short note on Wiener Filter. [10]

1 0) Explain with block diagram signal processing in radar system. [10]

sak

x

v7

fa
````

## 2011-12 · Exam not stated · Trim 2 · ZIP of papers · paper 0ec41aaf73e8 · ADVANCED DSP.pdf

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/TRIM II/ADVANCE DSP/M Tech EXTC TRIM II advanced DSP ADVANCED DSP.zip`
- Printed on paper: duration hours: 3; exam date: 03/02/2012
- Text: ocr (2 pages), mean OCR confidence 88.7

````text
a SVKM’s NMIMS
Mukesh Patel School Of Technology Management & Engin

_Programme: M. Tech- ELEX / EXTC Year: I Trimester;
Academic Year : 2011-2012

| * svKe's \*
Subject: ADVANCED DSP Marks{>( oo 2) Ve
Time: , «C 20s prmyTo stp m
Date: 03/02/2012 Duration, 3 hrs. oe3
Final - Examination Ne ae
SY MANAGENS

Instructions: Candidates should read carefully the instructions printed on the question paper and
on the cover of the Answer Book, which is provided for their use

NB:
1. Question No. 1 is compulsory
2. Out of remaining questions, attempt any 4 questions.
3. Inall 5 questions to be attempted
4. Answer to each new question to be stared on a fresh page
5. Figure in brackets indicate full marks
1. Attempt following questions (any 4) [20]

(a) | Obtain the mapping formula for bilinear transformation method.

(b) | Obtain the polyphase decomposition of the I[R system with transfer function.
1-42"!

1+5z7

H(Z)=

(c) | What are the limitations of non-parametric methods in spectral estimation?

(d) | What are the various applications of Wavelet Transform?

2.(a) | Design a digital Butterworth low pass filter satisfying the following specifications | [10]
using bilinear transformation (Assume T = 1 Sec)

09<|H(e™) <1,   Oswsn
|H(e™)| < 0.2, 3n/4<w<n

(b) | Implement a two stage decimator for the following specifications. [10]
; | Sampling rate of the input signal = 20,000 Hz
* |M=100

q }| Pass band = 0 to 40 Hz
Transition band = 40 to 50 Hz
Pass band ripple = 0.01
Stop band ripple = 0.002

3.(a) | What is a linear phase filter? What conditions are iu be satisfied by the impulse | [16]
response of an FIR system in order to have a linear phase? Plot and justify
compulsory zero locations for symmetric and antisymmetric even and
antisymmetric odd FIR filters.

(b) | Explain how AR parameters are obtained by using linear prediction. [10]

h
--- page 2 ---
——

—
| 4.(a) | Define parametric and non-parametric methods of power spectrum estimation. | [12]
| Explain the non-parametric methods of power spectrum estimation.

(b) | Explain the interpolation and decimation process with an example. [8]
| 5.(a) | Explain the forward —backward lattice algorithm. [10]
| (b) | State and explain the important properties of CWT [10]
| 6.(a) | Discuss application of DSP in Image Processing. [8]
|

| (b) | What is the need for short time spectral analysis? {5]

(c) | Determine the frequency resolution of the Bartlett, Welch methods of power } [7]
| spectrum estimates for a quality factor Q = 10. Assume the overlap in Welch’s
| method is 50% and the length of the sample sequence is 1000.

| 7.(a) | Write a short note on Wiener Filter. [10]

1 0) Explain with block diagram signal processing in radar system. [10]

sak

x

v7

fa
````

## 2010-11 · Re-Exam · Trim 2 · ZIP of papers · paper 6f5110251584 · Advanced DSP 2010-11 Re-Exam.pdf.pdf

- Departments: Electronics and Telecommunication
- Programmes: M TECH / EXTC
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/EXTC/TRIM II/ADVANCE DSP/M Tech EXTC TRIM II advanced DSP 2010-2011 Re exam.zip`
- Text: ocr (2 pages), mean OCR confidence 77.3

````text
SVKM’s NMIMS

\ Mukesh Patel School of Technology Management & Engineerin;
Programme: M.TECH - EXTC Year: I Trimester: a
Academic Year : 2010-2011
Batch: 2010-2011
Subject: Advanced DSP Marks:
Time:
Dae: 18/06/2011 Duration:

NLRB Y
3)
i.   G) How do you compute the energy of a discrete signal in time and frequency domains? {12]
(A)
Gi) Define sample autocorrelation function. Give the é of this estimate.

(Hi) Whai is the basic principle < ie power spectrum?
(iv) Why are FIR filters widel
(v) Definer Power spectrum
ivi) Define Hilbert transform

(B) (@) Explain Physical significance of spectral factorization. {8}
Gi) Wiener — Khintchine theorem.

2.(A) Consider the two systems shown in figure [10]

erms of x[nj, M, aad L

(i) Describe y,[n] and yz in} :
you derived im part (@) to show that, if M and L are relatively

(ii) Use the relationships th
prime, then y,{n} = yo[n)

(B) Explain the pole zero locations tor Type 1, Type if Type Il and Type fV linear phase FIR [10]
filters.
3.(A) Consider the two-channel QMF bank in figure with analysis and synthesis filters given by [10]
Holz) =34427°-3827%42%42°%.   ilz) = Ho(--)
Find a set of causal and stabie synthesis filters that result in perfect reconstruction.
(B) Explain power spectrum estimation using Bartlet method. {10]

Sampling rate of the input [10]

as.

4.(A) Implement a two stage decimator for ihe following specificati
signal = 20000 Hz

M=100

Passband = 0 to 40 Hz
Transition band 40 to 50 Hz
Passband ripple = 0.01
Stopband ripple = 0.002

Vy
--- page 2 ---
dogram, and {10}

fidh

{ iwY
lHle" |< 0.1, 05<SaSm

Use bilinear transformation and assuming T = sec

(B) Explain LMS algorithm for direct FIR filters. {10]

Perform the Haar decomposition, using (1/2, 1/2) and [10]

6(A) Letx=[9501-6-5140-5750
(1/2, -1/2) as Gecomposition {analys

(B) Application of DSP in radar signa’ processing {10}

Ts Write short notes on the following

(A) Forware linear prediction 10]
{10]

(Bs FIR wiener filter

IN

i

a
````
