# Computer Vision and Applications: question papers in full

10 unique papers · 2022-23 to 2025-26 · Data Science

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 6 · paper f86112b42a3d

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_DS_7009/Computer Vision and Applications/QP_Computer Vision and Applications(702DB0C024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Computer Vision and Applications
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Qestion No 1 is compullsory
5. Out if the remaining questions, attempt any 4
6. In all 5 questions to be attempted
Q1.   [20]
a. An image processing pipeline needs to scale a 2D point by a factor of 2, rotate it by 90 degrees, and
translate it by tx = 10, ty = 5. Express a sample point (x,y) in homogeneous coordinates, and construct
the   single   composite   affine   matrix required to   perform   all   three   operations
simultaneously.   [4]
b. What is the difference between the derivative of a Gaussian filter and the Difference of Gaussians
filter? Provide an example of where each of these is practically used in image processing / computer
vision.   [4]
c. While configuring a Canny edge detector for a robotic assembly line, you notice the
output contains many fragmented, broken edges along the conveyor belt. Describe the Canny pipeline
and which specific step is responsible for fixing this? Explain how modifying the upper and lower
values in the double thresholding step will help link these broken edge pixels.   [4]
d. In the context of Image Processing using Convolution Networks, explain the following components of
the network, and their function, in a maximum of 2-3 sentences each:
(i) Convolution layer
(ii) Pooling layer
(iii) Activation function
(iv) Fully-connected layer   [4]
e. Describe motion detection and object tracking techniques in video analysis.   [4]
********** 1 **********
--- page 2 ---
Q2.   [20]
a. Obtain the output image when the following filters are applied on the following image:
i.   Box filter of size (3x3)
ii.   Sobel filter (vertical edge)
iii.   Gaussian filter (size5x5)   [10]
b. Suppose you are given two consecutive frames of a traffic camera capturing a fast-moving car where
the car moved by 20 pixels to the right and 15 pixels down and you apply the standard Lucas-Kanade optical
flow algorithm with a small window (5x5).
i.   Explain why the algorithm is likely to fail in estimating the correct motion.
ii.   Identify which assumptions of optical flow are violated.
iii.   Describe the result of the above algorithm qualitatively.
iv.   Describe how pyramidal Lucas-Kanade algorithm helps in this case.
v.   If the image is down sampled by a factor of 2 at each level: What will be the apparent motion
at level 1? At level 2?   [10]
Q3.   [20]
a. Suppose you are asked to run the inference of the images for classification that are captured on a slow-
moving conveyer belt in a corn-flakes factory. Each image can capture hundreds of corn flakes. Your
classification results will be used to take actions - whether to discard the flakes in the image or not. You
have the option of using YOLO and Faster-RCNN models.
i.   Which of the two models is appropriate for the above use case?
ii.   Explain why the selected model gives faster response based on the model architectures.
iii.   Will your answer change if the application is changed where the images now contain bigger
and fewer objects - for example in case of self-driving vehicles?
iv.   Provide justification for your answer.   [10]
b. Consider the case of running Harris Corner Detection on a patch in the following chessboard image.
The white squares have value 2 and the black squares have value 0. Assume a square window function
(w(x,y) = 1), and the patch is exactly 2x2 pixels:
********** 2 **********
--- page 3 ---
P = [0 2
2 0]
For image derivatives, use: Dx = [1 0 -1], Dy = [1 0 -1]T
i.   Compute image gradients Ix and Iy.
ii.   Compute Ix2, , Iy2 , IxIy.
iii.   Compute the second moment matrix M.
iv.   Compute Harris Corner Response using the following equation assuming k = 0.04.
v.   Compute the eigenvalues of the second moment matrix.
vi.   Is the patch a corner or an edge? \
vii.   Would the classification change if we increased the patch size? Why or why
not?   [10]
Q4.   [20]
a. You are building the preprocessing module for the "Eyeglass Classifier" virtual try-on kiosk. Before
passing the facial image to the machine learning model, you must segment the dark eyeglass frames
from the user's face. Construct a pipeline that reads an input image, applies binary thresholding to
segment the dark pixels, extracts the contours of the segmented regions, and draws a bounding rectangle
around the largest contour (representing the glasses). Mention the key OpenCV functions to be
used.   [10]
b. In the figure below, we applied a Gaussian filter to an image of a zebra’s nose and computed the
derivative. To obtain each of the images, we varied the standard deviation σ of the Gaussian filter.
Given a fixed kernel size, should the standard deviation σ of the Gaussian filter increase or decrease
from the leftmost to the rightmost image?
********** 3 **********
--- page 4 ---
Provide justification for your answer.   [10]
Q5.   [20]
a. Face recognition systems are widely used today. Explain the complete pipeline of a face recognition
system and mention two practical challenges it may face regarding deployment. Mention the key OpenCV
functions to be used.   [10]
b. SIFT is considered one of the most robust feature extractors in classical computer vision.
i) Outline the four primary stages of the SIFT calculation pipeline.
ii) Explain the concept of the Difference of Gaussians (DoG) pyramid in the first stage. Why is it used
instead of a standard Laplacian?
iii) What does each entry in the final 128-dimensional vector represent, and why does SIFT cap gradient
magnitudes   during   this final   step?   (Explain how   this   helps   with   illumination
invariance).   [10]
Q6.   [20]
a. An animal shelter wants to build a mobile app to classify intake photos as 'Cat' or 'Dog'. Design and implement
an image classification pipeline for the same.
i.   Describe the architecture of the CNN model you would build for the same. Which loss
function would you use and why?
ii.   You find out that they only have a small dataset of 500 images, which is not enough to train a deep
neural network from scratch without severe overfitting.
iii.   Explain the concept of Transfer Learning and detail the exact architectural changes you must make
to the final layers of the pre-trained ImageNet model to adapt it for this binary 'Cats vs. Dogs'
task.   [10]
b. Design a License Plate Detection system for a parking mall. Explain how your system will handle different
lighting conditions, vehicle orientations, and moving backgrounds. Mention the key OpenCV functions to be
used.   [10]
Q7 .
a. Deep Learning has revolutionized how we process both static images and dynamic video feeds.
i.Detail the complete architecture of a standard Convolutional Neural Network (CNN), explaining
the specific mathematical and functional roles of Convolution, Max Pooling, and Fully Connected
layers. (4 marks)
ii.Contrast the fundamental architectural memory of a CNN with that of a Recurrent Neural Network
(RNN). Provide one specific computer vision application where an RNN is strictly required. (3
marks)
iii.Explain the concept of "Region Proposals" in the R-CNN framework. How does R-CNN differ
from standard image classification   [10]
********** 4 **********
--- page 5 ---
b. Explain modern object detection techniques with reference to Advanced Driver Assistance Systems
(ADAS). Specifically, describe how object detection frameworks are tuned and applied for pedestrian
detection and lane detection in self-driving cars.   [10]
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 8275dc39df54

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_DS_7052/Computer Vision and Applications/QP_Computer Vision and Applications(702DB0C024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Computer Vision and Applications
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Qestion No 1 is compullsory
5. Out if the remaining questions, attempt any 4
6. In all 5 questions to be attempted
Q1.   [20]
a. An image processing pipeline needs to scale a 2D point by a factor of 2, rotate it by 90 degrees, and
translate it by tx = 10, ty = 5. Express a sample point (x,y) in homogeneous coordinates, and construct
the   single   composite   affine   matrix required to   perform   all   three   operations
simultaneously.   [4]
b. What is the difference between the derivative of a Gaussian filter and the Difference of Gaussians
filter? Provide an example of where each of these is practically used in image processing / computer
vision.   [4]
c. While configuring a Canny edge detector for a robotic assembly line, you notice the
output contains many fragmented, broken edges along the conveyor belt. Describe the Canny pipeline
and which specific step is responsible for fixing this? Explain how modifying the upper and lower
values in the double thresholding step will help link these broken edge pixels.   [4]
d. In the context of Image Processing using Convolution Networks, explain the following components of
the network, and their function, in a maximum of 2-3 sentences each:
(i) Convolution layer
(ii) Pooling layer
(iii) Activation function
(iv) Fully-connected layer   [4]
e. Describe motion detection and object tracking techniques in video analysis.   [4]
********** 1 **********
--- page 2 ---
Q2.   [20]
a. Obtain the output image when the following filters are applied on the following image:
i.   Box filter of size (3x3)
ii.   Sobel filter (vertical edge)
iii.   Gaussian filter (size5x5)   [10]
b. Suppose you are given two consecutive frames of a traffic camera capturing a fast-moving car where
the car moved by 20 pixels to the right and 15 pixels down and you apply the standard Lucas-Kanade optical
flow algorithm with a small window (5x5).
i.   Explain why the algorithm is likely to fail in estimating the correct motion.
ii.   Identify which assumptions of optical flow are violated.
iii.   Describe the result of the above algorithm qualitatively.
iv.   Describe how pyramidal Lucas-Kanade algorithm helps in this case.
v.   If the image is down sampled by a factor of 2 at each level: What will be the apparent motion
at level 1? At level 2?   [10]
Q3.   [20]
a. Suppose you are asked to run the inference of the images for classification that are captured on a slow-
moving conveyer belt in a corn-flakes factory. Each image can capture hundreds of corn flakes. Your
classification results will be used to take actions - whether to discard the flakes in the image or not. You
have the option of using YOLO and Faster-RCNN models.
i.   Which of the two models is appropriate for the above use case?
ii.   Explain why the selected model gives faster response based on the model architectures.
iii.   Will your answer change if the application is changed where the images now contain bigger
and fewer objects - for example in case of self-driving vehicles?
iv.   Provide justification for your answer.   [10]
b. Consider the case of running Harris Corner Detection on a patch in the following chessboard image.
The white squares have value 2 and the black squares have value 0. Assume a square window function
(w(x,y) = 1), and the patch is exactly 2x2 pixels:
********** 2 **********
--- page 3 ---
P = [0 2
2 0]
For image derivatives, use: Dx = [1 0 -1], Dy = [1 0 -1]T
i.   Compute image gradients Ix and Iy.
ii.   Compute Ix2, , Iy2 , IxIy.
iii.   Compute the second moment matrix M.
iv.   Compute Harris Corner Response using the following equation assuming k = 0.04.
v.   Compute the eigenvalues of the second moment matrix.
vi.   Is the patch a corner or an edge? \
vii.   Would the classification change if we increased the patch size? Why or why
not?   [10]
Q4.   [20]
a. You are building the preprocessing module for the "Eyeglass Classifier" virtual try-on kiosk. Before
passing the facial image to the machine learning model, you must segment the dark eyeglass frames
from the user's face. Construct a pipeline that reads an input image, applies binary thresholding to
segment the dark pixels, extracts the contours of the segmented regions, and draws a bounding rectangle
around the largest contour (representing the glasses). Mention the key OpenCV functions to be
used.   [10]
b. In the figure below, we applied a Gaussian filter to an image of a zebra’s nose and computed the
derivative. To obtain each of the images, we varied the standard deviation σ of the Gaussian filter.
Given a fixed kernel size, should the standard deviation σ of the Gaussian filter increase or decrease
from the leftmost to the rightmost image?
********** 3 **********
--- page 4 ---
Provide justification for your answer.   [10]
Q5.   [20]
a. Face recognition systems are widely used today. Explain the complete pipeline of a face recognition
system and mention two practical challenges it may face regarding deployment. Mention the key OpenCV
functions to be used.   [10]
b. SIFT is considered one of the most robust feature extractors in classical computer vision.
i) Outline the four primary stages of the SIFT calculation pipeline.
ii) Explain the concept of the Difference of Gaussians (DoG) pyramid in the first stage. Why is it used
instead of a standard Laplacian?
iii) What does each entry in the final 128-dimensional vector represent, and why does SIFT cap gradient
magnitudes   during   this final   step?   (Explain how   this   helps   with   illumination
invariance).   [10]
Q6.   [20]
a. An animal shelter wants to build a mobile app to classify intake photos as 'Cat' or 'Dog'. Design and implement
an image classification pipeline for the same.
i.   Describe the architecture of the CNN model you would build for the same. Which loss
function would you use and why?
ii.   You find out that they only have a small dataset of 500 images, which is not enough to train a deep
neural network from scratch without severe overfitting.
iii.   Explain the concept of Transfer Learning and detail the exact architectural changes you must make
to the final layers of the pre-trained ImageNet model to adapt it for this binary 'Cats vs. Dogs'
task.   [10]
b. Design a License Plate Detection system for a parking mall. Explain how your system will handle different
lighting conditions, vehicle orientations, and moving backgrounds. Mention the key OpenCV functions to be
used.   [10]
Q7 .
a. Deep Learning has revolutionized how we process both static images and dynamic video feeds.
i.Detail the complete architecture of a standard Convolutional Neural Network (CNN), explaining
the specific mathematical and functional roles of Convolution, Max Pooling, and Fully Connected
layers. (4 marks)
ii.Contrast the fundamental architectural memory of a CNN with that of a Recurrent Neural Network
(RNN). Provide one specific computer vision application where an RNN is strictly required. (3
marks)
iii.Explain the concept of "Region Proposals" in the R-CNN framework. How does R-CNN differ
from standard image classification   [10]
********** 4 **********
--- page 5 ---
b. Explain modern object detection techniques with reference to Advanced Driver Assistance Systems
(ADAS). Specifically, describe how object detection frameworks are tuned and applied for pedestrian
detection and lane detection in self-driving cars.   [10]
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 10 · paper a4253c6095bd

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_DS_7038/Computer Vision and Applications/QP_Computer Vision and Applications(702DB0C024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Computer Vision and Applications
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Qestion No 1 is compullsory
5. Out if the remaining questions, attempt any 4
6. In all 5 questions to be attempted
Q1.   [20]
a. An image processing pipeline needs to scale a 2D point by a factor of 2, rotate it by 90 degrees, and
translate it by tx = 10, ty = 5. Express a sample point (x,y) in homogeneous coordinates, and construct
the   single   composite   affine   matrix required to   perform   all   three   operations
simultaneously.   [4]
b. What is the difference between the derivative of a Gaussian filter and the Difference of Gaussians
filter? Provide an example of where each of these is practically used in image processing / computer
vision.   [4]
c. While configuring a Canny edge detector for a robotic assembly line, you notice the
output contains many fragmented, broken edges along the conveyor belt. Describe the Canny pipeline
and which specific step is responsible for fixing this? Explain how modifying the upper and lower
values in the double thresholding step will help link these broken edge pixels.   [4]
d. In the context of Image Processing using Convolution Networks, explain the following components of
the network, and their function, in a maximum of 2-3 sentences each:
(i) Convolution layer
(ii) Pooling layer
(iii) Activation function
(iv) Fully-connected layer   [4]
e. Describe motion detection and object tracking techniques in video analysis.   [4]
********** 1 **********
--- page 2 ---
Q2.   [20]
a. Obtain the output image when the following filters are applied on the following image:
i.   Box filter of size (3x3)
ii.   Sobel filter (vertical edge)
iii.   Gaussian filter (size5x5)   [10]
b. Suppose you are given two consecutive frames of a traffic camera capturing a fast-moving car where
the car moved by 20 pixels to the right and 15 pixels down and you apply the standard Lucas-Kanade optical
flow algorithm with a small window (5x5).
i.   Explain why the algorithm is likely to fail in estimating the correct motion.
ii.   Identify which assumptions of optical flow are violated.
iii.   Describe the result of the above algorithm qualitatively.
iv.   Describe how pyramidal Lucas-Kanade algorithm helps in this case.
v.   If the image is down sampled by a factor of 2 at each level: What will be the apparent motion
at level 1? At level 2?   [10]
Q3.   [20]
a. Suppose you are asked to run the inference of the images for classification that are captured on a slow-
moving conveyer belt in a corn-flakes factory. Each image can capture hundreds of corn flakes. Your
classification results will be used to take actions - whether to discard the flakes in the image or not. You
have the option of using YOLO and Faster-RCNN models.
i.   Which of the two models is appropriate for the above use case?
ii.   Explain why the selected model gives faster response based on the model architectures.
iii.   Will your answer change if the application is changed where the images now contain bigger
and fewer objects - for example in case of self-driving vehicles?
iv.   Provide justification for your answer.   [10]
b. Consider the case of running Harris Corner Detection on a patch in the following chessboard image.
The white squares have value 2 and the black squares have value 0. Assume a square window function
(w(x,y) = 1), and the patch is exactly 2x2 pixels:
********** 2 **********
--- page 3 ---
P = [0 2
2 0]
For image derivatives, use: Dx = [1 0 -1], Dy = [1 0 -1]T
i.   Compute image gradients Ix and Iy.
ii.   Compute Ix2, , Iy2 , IxIy.
iii.   Compute the second moment matrix M.
iv.   Compute Harris Corner Response using the following equation assuming k = 0.04.
v.   Compute the eigenvalues of the second moment matrix.
vi.   Is the patch a corner or an edge? \
vii.   Would the classification change if we increased the patch size? Why or why
not?   [10]
Q4.   [20]
a. You are building the preprocessing module for the "Eyeglass Classifier" virtual try-on kiosk. Before
passing the facial image to the machine learning model, you must segment the dark eyeglass frames
from the user's face. Construct a pipeline that reads an input image, applies binary thresholding to
segment the dark pixels, extracts the contours of the segmented regions, and draws a bounding rectangle
around the largest contour (representing the glasses). Mention the key OpenCV functions to be
used.   [10]
b. In the figure below, we applied a Gaussian filter to an image of a zebra’s nose and computed the
derivative. To obtain each of the images, we varied the standard deviation σ of the Gaussian filter.
Given a fixed kernel size, should the standard deviation σ of the Gaussian filter increase or decrease
from the leftmost to the rightmost image?
********** 3 **********
--- page 4 ---
Provide justification for your answer.   [10]
Q5.   [20]
a. Face recognition systems are widely used today. Explain the complete pipeline of a face recognition
system and mention two practical challenges it may face regarding deployment. Mention the key OpenCV
functions to be used.   [10]
b. SIFT is considered one of the most robust feature extractors in classical computer vision.
i) Outline the four primary stages of the SIFT calculation pipeline.
ii) Explain the concept of the Difference of Gaussians (DoG) pyramid in the first stage. Why is it used
instead of a standard Laplacian?
iii) What does each entry in the final 128-dimensional vector represent, and why does SIFT cap gradient
magnitudes   during   this final   step?   (Explain how   this   helps   with   illumination
invariance).   [10]
Q6.   [20]
a. An animal shelter wants to build a mobile app to classify intake photos as 'Cat' or 'Dog'. Design and implement
an image classification pipeline for the same.
i.   Describe the architecture of the CNN model you would build for the same. Which loss
function would you use and why?
ii.   You find out that they only have a small dataset of 500 images, which is not enough to train a deep
neural network from scratch without severe overfitting.
iii.   Explain the concept of Transfer Learning and detail the exact architectural changes you must make
to the final layers of the pre-trained ImageNet model to adapt it for this binary 'Cats vs. Dogs'
task.   [10]
b. Design a License Plate Detection system for a parking mall. Explain how your system will handle different
lighting conditions, vehicle orientations, and moving backgrounds. Mention the key OpenCV functions to be
used.   [10]
Q7 .
a. Deep Learning has revolutionized how we process both static images and dynamic video feeds.
i.Detail the complete architecture of a standard Convolutional Neural Network (CNN), explaining
the specific mathematical and functional roles of Convolution, Max Pooling, and Fully Connected
layers. (4 marks)
ii.Contrast the fundamental architectural memory of a CNN with that of a Recurrent Neural Network
(RNN). Provide one specific computer vision application where an RNN is strictly required. (3
marks)
iii.Explain the concept of "Region Proposals" in the R-CNN framework. How does R-CNN differ
from standard image classification   [10]
********** 4 **********
--- page 5 ---
b. Explain modern object detection techniques with reference to Advanced Driver Assistance Systems
(ADAS). Specifically, describe how object detection frameworks are tuned and applied for pedestrian
detection and lane detection in self-driving cars.   [10]
********** 5 **********
````

## 2025-26 · Re-Exam · Sem 10 · paper 03fb12693d0e

- Departments: Data Science
- Programmes: B.TECH INTEGRATED / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/5th YEAR/DATA SCIENCE/Sem_10/Computer Vision and Applications/Computer Vision and Applications Batch 2025-26 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06 Jul 2026
- Text: ocr (5 pages), mean OCR confidence 91.5
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: B. Tech (DS)/B. Tech Intg.
Year: IIL / V/Sem 10 Re-exam/Sem 6 Re-e ke
Subject: Computer Vision and Applications
Date: 06 Jul 2026 (03:00 Hrs.)
Max. Marks: 100
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Qestion No 1 is compullsory

5. Out if the remaining questions, attempt any 4
6. In all 5 questions to be attempted

Ql. [20]

a. With an example, show how the processes of resizing, skewing; rotation and translation of an image, are

supported by expressing an image in homogeneous coordinates and applying a single affine transformation
matrix. [4]

b. While configuring a Canny edge detector for a robotic assembly line, you notice the output contains many
fragmented, broken edges along the conveyor belt. Describe the Canny pipeline and which specific step is

responsible for fixing this? Explain how modifying the upper and lower values in the double thresholding
step will help link these broken edge pixels. [4]

c. An office building recently upgraded its face recognition attendance system from an Eigenfaces algorithm
to Local Binary Patterns Histograms (LBPH). The old system failed completely in the late afternoon when
harsh sunlight hit the users' faces from the side, but the new LBPH system handles this illumination shift
effortlessly. Describe the core mathematical process by which LBPH extracts local features,

and explain exactly why this specific pixel-comparison approach makes it inherently robust to such
lighting variations. ~*~ . [4]

*d. Contrast the fundamental architectural memory of a CNN with that of a Recurrent Neural Network (RNN).
Provide one specific computer vision application where an RNN is strictly required. [4]

e. Explain briefly the differences in the workings of YOLO and SSD models’ in object detection. Which of
the above two are appropriate for real time applications and provide justification? [4]

/

FRR 7 aR RR RE

tae
--- page 2 ---
Q2. 2 [20]

Q3. . [20]
You are building a real-time vehicle classification system for a smart highway toll booth. You have
successfully extracted a set of 128-dimensi

onal HOG (Histogram of Oriented Gradients) features from a
dataset of 10,000 vehicle and non-vehicle images.
i.

Detail the complete supervised trainin,
Support Vector Machine (SVM
handled.

Explain exactly what the SVM mathematically constructs in this 12
distinguish between "vehicle" and "
and Support Vectors in your answer.
During inference, a camera captures a new

Mathematically, how does the trained SVM dec

§ pipeline required to use these HOG features to train a
). Explicitly mention how positive and negative samples are
li. 8-dimensional feature space to
non-vehicle" vectors. Define the terms Hyperplane, Margin,
ili. image, and its 128-D HOG vector is extracted.
ide which class this new vector belongs to? [10]

b A manufacturing plant uses a vision system to align microchips on a fast

uses Template Matching to find a specific fiducial marker on the chip.
i. Given a 100x100 pixel input image and a 10x10 pixel template, calculate the exact dimensions of
the resulting response map if standard template matching is applied without any padding.
ii. Explain why this standard Template Matchin,
arrives on the conveyor belt rotated by 45 d
height.

-moving belt. The legacy system

egrees or scaled down due to a change in camera
iii. To solve this, you upgrade the system to use the

SIFT algorithm. Explain how SIFT's "Orientation
Assignment"

step mathematically achieves rotation invariance for its feature descriptors. [10]


>
approach will completely fail if the microchip
--- page 3 ---
Q4.

Q5.

[20]

1. Suppose you are designing an automated fruit sorting system. The camera captures images of apples (red)
and leaves (green) on a conveyor belt. You have extracted a 6-pixel sample table to calibrate your machine

learning model: [10]

Pixel R (Red) G (Green) B (Biue)

al 240 20 20

P2 230 3% 10

P3 10 200 30

P4 20 220 40

PS 5 § 5

Pe 10 10 10

i. | Formulate this as an image classification problem. If using a Support Vector Machine (SVM), what
does it mathematically construct in the 3D (R,G,B) feature space to separate the Apples from the
Leaves? :

ii. If we use the k-Nearest Neighbors (KNN) algorithm for this problem, what is the role of the 'k'
parameter? State one advantage and one disadvantage of using.KNN over SVM for a real-time
hardware sorting system. [10]

a. In computer vision, geometric transformations are essential for image alignment.

i. Write the generic 3x3 homogeneous matrices for Translation, Rotation, and Scaling.

ii. Let a pixel coordinate be P = [x, y, 1]. Show mathematically the combined affine transformation
matrix if you first scale the image by a factor of 2, and then translate it by Tx=5, Ty=10. Does the
order of matrix multiplication matter? Justify your answer.

iii. Explain the fundamental difference between an Affine Transformation and a Perspective
Transformation, specifically mentioning their respective Degrees of Freedom (DoF) . [10]

[20]
a. You are given two consecutive frames from a drone tracking a boat on a fast-moving river.
i. The water ripples create dynamic, non-rigid motion. Identify which core assumption of the standard
Lucas-Kanade optical flow algorithm is violated by these moving ripples.

ii. | Suppose the boat is moving very fast, causing it to shift by 30 pixels between consecutive frames.
Explain why the standard Lucas-Kanade algorithm fails here, and describe how the Pyramidal
Lucas-Kanade approach solves this large-motion issue.

iii. Differentiate between Sparse and Dense Optical Flow. Which method is computationally
more appropriate fortracking just the specific corners of the boat, and
why? [10]

.

b. You are given a set of random images of persons—images of persons with glasses and without glasses.
You ag tasked with creating a pipeline that takes a random image of a person and classifies whether the
person has eye-glasses or not, using a linear SVM classifier. Your pipeline should have the following

RR di a a a

e
--- page 4 ---
stages: Pre-processing, HOG feature extraction, Dimensionality Reduction and Classification. Describe the
tasks that you need to perform under each of the four stages. [10]

e : [20] ry

a. Image thresholding is a crucial pre-processing step, but it often fails in real-world environments.

Q6.

i. Consider the scenario in the image above. Explain why standard global binary thresholding will fail
to cleanly segment the text from the background in this image:

ii. Detail how Adaptive Thresholding solves this uneven illumination issue. How does it
mathematically differ from applying a single global
threshold? [10]

b. Modern object detection frameworks rely heavily on the concept of "Anchor Boxes" (or prior boxes).
i. Explain what an Anchor Box is and why it is used in models like YOLO or SSD instead of having
the network predict bounding box coordinates entirely from scratch. (5 marks)
ii. Ifa single grid cell contains both a tall, narrow pedestrian and a wide, squat car, explain how having
multiple anchor boxes of different aspect ratios allows a Single-Shot Detector to predict both

objects simultaneously. [10]

Q7.

a. Consider a 5x5 input image matrix. A convolution operation is performed using a 3x3 kernel with a stride

of 1 and no padding.

i. / Calculate the final numerical value of the top-left pixel of the resulting feature map. Detail

” your calculation steps.
il. Explain the purpose of applying a Max Pooling layer (2x2) on a resulting feature map in a

Convolutional Neural Network (CNN). How does it provide spatial invariance?
iii, | Discuss the "Vanishing Gradient" problem that often occurs during the backpropagation phase of
training deep networks, and explain how the ReLU activation function mathematically helps

mitigate it. [10]

FRR 2 RRR RE

ey -
--- page 5 ---
b.

ii.

In object detection Ps

Explain the differrence between one shot and two shot detection. Compare the architectural approach
of Single-Shot Detectors (like YOLO or SSD) against Two-Stage Detectors (like Faster R-CNN).
Which is more appropriate for a high-speed conveyor belt?

During object detection, the model often generates multiple overlapping bounding boxes around a
single microchip. Detail the algorithmic steps of Non-Maximum Suppression (NMS) and explain how
it uses the Intersection over Union (IoU) metric to clean up the
output. [10]

FRR RR aK

ay
````

## 2024-25 · Final + Re-Exam · Sem 6 · paper d3e3096594cf

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM VI/COMPUTER VISION AND APPLICATIONS/Computer Vision and Applications, Sem-VI, Final Exam 2024-25 & Re Exam 2023-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02/ 05/2025
- Text: ocr (2 pages), mean OCR confidence 92.1

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: BTech Year: III Semester: VI

Stream/s : BTech (DS)/MBA Tech (DS)

Subject: Computer Vision and Applications Time: 3 hrs (2 to S)prn
Date: 02/ 05/2025 No. of Pages: 2
Marks: 100
ema eee
Final Examination/Re-Examination (Re-cxam y' ar)
(24-25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. lis compulsory.

2) Out of remaining questions, attempt any 3 questions.

3) In all 4 questions to be attempted.

4) Internet access is allowed

5) You can use Google Colab/Kaggle to solve the problem. Please login with Gmail ID wherever needed
6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.

8) Please share all notebooks in a folder with your name

9) Make sure all outputs are present

Build an image classification model to distinguish classes.
https://www.kaggle.com/datasets/muratkokludataset/grapevine-

Qi leaves-image-dataset [40]

Train your own custom CNN and benchmark it against 3 pre trained

models

Define a detection framework for the following problem

~ https://www.kaggle.com/datasets/sebastianpalaciob/plantvillage-for- [30]

object-detection-yolo
--- page 2 ---
Develop a Neural Style Transfer module for any content and style image

3
: \ [30]
of your choice
Q4
Build a GAN to generate new images on a dataset of your choice [30]
Develop an image classification model to categorizing the classes in the
Qs following data
[30]
nttps://www.kaggle.com/datasets/muratkokludataset/rice-image-
dataset
Q6 Define an object detection framework for the following dataset
https://www.kaggle.com/datasets/andy8744/playing-cards-object- [30]

detection-dataset/data
````

## 2023-24 · Re-Exam · Sem 6 · paper 1590d6ca72a0

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE, MBA TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM VI/COMPUTER VISION AND APPLICATIONS/Computer Vision and Application , Re-exam 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100
- Text: ocr (2 pages), mean OCR confidence 90.5

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2023-2024

Program: B. Tech./ MBA Tech. Stream: Data Science Year: II] Semester: VI
Subject: Computer Vision and Applications Time: 3 _ hrs (Ztoopmio Stedpmy
Date: _24/ 6 / 2024 No. of Pages: 02
Marks: 100
Re Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4__ questions.

3) In all_5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer the following.

CO-1; SO-1; BL-2 | a. | Write about the OpenCV library in Python, highlighting its key aspects. | [04]

CO-3; SO-1; BL-2 | b. | Discuss template matching. [04]
CO-1; SO-1; BL-2 | c. | Explain briefly about backpropagation. [04]
: CO-4; SO-1; BL-2 | d. | Explain the Sobel operator and its use in image processing. [04]
CO-2; SO-1; BL-2 | e. | Brief on point operators. [04]
Q2 A | Import necessary libraries and write down a program in Python for [10]
CO-2; SO-2; BL-3 the following tasks.

- Read given image, convert it to a grayscale image
- Change brightness and contrast of the original color image
independently

ent - Plot brightness and contrast changed images one below the other in
a column using subplots function.

- Apply gamma correction to the original input image

Page 1 of 2
--- page 2 ---
- Apply Gaussian bur to the original input image.

CO-2;SO-1; BL-2 | B_ | Explain the following 2D transformations using mathematical [10]
equations or matrix multiplications with homogeneous coordinates.
Also, specify their degrees of freedom.
(i) Scale

(ii) Rigid/ Euclidean (Rotation + Translation)

Q3 A_ | Explain median smoothing and bilateral smoothing in detail referring [10]
CO-2; SO-1; BL-2 to their mathematical equations or sample calculations. State the
major advantages of using median smoothing and bilateral

smoothing?

CO-2; SO-1; BL-2 | B_ | Justify the need of pyramid in computer vision. Also, explain the {10]

Gaussian pyramid and it’s any two applications.

Q4 A_ | Discuss Harris corner detection and the conditions for determining [10]
CO-3; SO-1; BL-1 whether the detected object is a corner, edge, or flat region.
CO-3; SO-2; BL-3 | B_ | Using the given image, implement Harris corner detection and print [10]

the impact of using various window sizes in detecting corners (Use

OpenCv).
Qs A_ | What are the challenges in pedestrian detection for self-driving cars, [10]
CO-3; SO-1; BL-2 and how can they be addressed?
CO-3; SO-1; BL-2 | B | Discuss the role of Histograms of Gradients (HOG) in object [10]
detection.
a6 A [10]

Explain the key components of a Recurrent Neural Network (RNN).
CO-1; SO-1; BL-2

CO-3; SO-1; BL-1 | B | Explain the implementation of Lucas-Kanade method in OpenCv. [10]
Q? A_ | &xplain the concept of image segmentation and two of its [10]

CO-3; SO-1; BL-2 applications.

CO-1; SO-1; BL-1 | B_ | Discuss the functioning of Convolutional and Dropout layers, as well [10]

as activation functions, in convolutional neural networks (CNN).

Page 2 of 2
````

## 2022-23 · Final-Exam · Sem 6 · paper 6e532c7a29f1

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM VI/COMPUTER VISION AND APPLICATIONS/Computer Vision & Applications, Sem-VI, Year 2022-23, Final Exam.pdf`
- Printed on paper: max marks: 100
- Text: ocr (4 pages), mean OCR confidence 92.2

````text
| a MPSTME
SVKM’S NMIMS LIBRARY

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS
Academic Year: 2022-2023

Program/s: B.Tech Year: II] Semester: VI

Stream/s : Data Science
Subject: Computer Vision and Applications Time: 04 _ hrs (2 pm to 5 pm_)
Date:_20 / 0H / 2023 No. of Pages: 4

Marks: 100
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. | is compulsory.
> 2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Relevant Datasets have been provided for data driven questions
7) Figures in brackets on the right hand side indicate full marks.
8) Assume Suitable data if necessary.

qi Answer briefly: [20]
CO-1; SO-1; a. Explain the steps present in the Canny Edge Detection algorithm. 5
BL-Il
CO-1 ; SO-2; b. Define Projective Transformation and give its application. 5
BL-I
CO-1; SO-2; G Explain how fine-tuning is performed in Transfer Learning. S
BL-II
CO-2; SO-2; d. Interpret the ground truth and predicted values given for a covid-19 classification problem in | 5
BL-Ili
> i covid19.csv file and determine the ideal threshold for classification using the ROC curve.
Q2 a. Calculate the number of parameters manually for the Alex-Net architecture given below. [10]
CO-4; SO-2; Sr. Layers/Input
BL-Ill
1 Input Image (e.g. 224 x 224 x 3)
2 Convolutional Layer (11 x 11 x 96), stride=4
3 Max Pooling Layer (3 x 3), stride=2
4 Convolutional Layer (5 x 5 x 256), pad=2
5 Max Pooling Layer (3 x 3), stride=2
6 Convolutional Layer (3 x 3 x 384), pad=1
mice 7 Convolutional Layer (3 x 3 x 384), pad=1
8 Convolutional Layer (3 x 3 x 256), pad=1
| 2 Max Pooling Layer (3 x 3), stride=2
L |
--- page 2 ---
10 Fully Connected 4096

11 Fully Connected 4096

12 Output Layer 1000

b. Explain Convolutional Neural Networks and its various components in detail. Compare the {10]

characteristics of a CNN with ANN and state its advantages.

Q3 a. Analyze the CNN architecture given below and ca!culate the number of trainable and non- [10]
CO-4; SO-3; trainable parameters using Tensorflow.
BL-IV
Sr Layer/Block Repeat
1 Input Layer: 224x224x3
2 Conv Layer: 1
32 Kernels

11x11 Kernel size
Strides 2
Padding same

Activation Relu

3 Maxpooling: 1
Size 3x3
Strides 2

Padding same

4 Conv Layer: 1
64 Kernels
1x1 Kernel size
Padding Same

Activation Relu

S Conv Layer 1
196 Kernels
3x3 Kernel size
Padding same

Activation Relu

6 Maxpooling 1
Size 3x3
Padding same

Activation Relu

7 Inception Module 1
1x1 Filters: 64
3x3 Reduce Filters: 96
3x3 Filters: 128
--- page 3 ---
5x5 Reduce Filters: 16
SxS Filters: 32

Pooling Projection Filters: 32

8 Residual Block 3
Kernel Size: 3x3
Filters: (64,64,128]

Strides: 1

9 Inception Module i,
1x1 Filters: 364
3x3 Reduce Filters: 192
3x3 Filters: 364
5x5 Reduce Filters: 48
5x5 Filters: 128

Pooling Projection Filters: 128

10 Mobilenet Block 1
64 Kernels
3x3 Kernel Size

Strides 1

11 Mobilenet Block a
128 Kernels

3x3 Kernel Size

Strides 2
12 Global Average Pooling 1
13 Output Layer 1

39 Neurons Softmax

b. Illustrate the block diagram of the above architecture. Explain the Inception module, Residual (10)
block and MobileNet module used in the above architecture.
Q4a a. Examine the binary image classification problem on classifying waste as Organic or Recylable in the | [10]
CO-3; SO-3; dataset given in the link below:

BL-IIl
https://www.kaggle.com/datasets/techsash/waste-classification-data

i: Use transfer learning to train a pretrained model for 3-5 epochs and illustrate the loss
curves. Explain the fitting of your model in terms of the loss curve.
ii. Evaluate the performance of the model and explain the results of the classification
metrics
iii. IIlustrate the confusion matrix and analyze the results
iv. Would False Positive be a bigger problem or False Negative be a bigger problem if this

model were to be used in the waste management sector ? Justify your answer.
--- page 4 ---
b. Explain the Siamese network architecture. Explain how triplet loss can be used in Siamese network | [10]

architecture.

Qs a. Compare RCNN, Fast RCNN and Faster RCNN algorithms for object detection. [10]
CO-2; SO-2;
BL-IV,V fs, 5 x

b. Distinguish how Faster RCNN algorithm can be used for detecting faces in images compared to [10]

Haar Cascades. Briefly describe the training process for the two methods.

Q6 a. Explain the following metrics used in Object Detection: Intersection over Union (loU), Mean [10]
CO-1,3; SO-3; Average Precision (mAP).
BL-ILIV

b. Analyze the images 000300.jpg and 001504. jpg in the train folder in the dataset given below:- [10]

https://www.kaggle.com/datasets/quadeer15sh/amur-tiger-reidentification
Apply the four different affine transformations on image 001504.jpg and perform SIFT matches
between each transformed version of image 001504.jpg and 000300.jpg.

i. Rotation (about the origin): angle 15 degrees

ii. Shearing (x direction): 0.3

iii. Translation (y direction): 30

iv. Sheared_Translation (performs shearing in x direction and translation in y direction): 0.3

Shearing and 30 Translation

Give the total number of feature matches between the transformed image 001504.jpg and
000300.jpg for each of the four transformations. Write your observations about the feature matches

in brief.
Q7 a. Determine the better performing model based on the data given in the table below. Show the [10]
CO-3; SO-3; necessary working.
BL-III,VI
Model
1 P(A) P(B) P(C) GT(A) GT(B) GT(C)
1 0.55 0.35 0.1 1 0 0
2 0.3 0.5 0.2 0 1 0
3 0.6 |* 0.35 0.05 1 0 0
4 0.3 0.3 0.4 ie} 0 dL.
5: 0.3 0.5 0.2 ie) 1 ie)
6 0.01 0.45 0.54 ie} EY 0
Model
2 P(A) P(B) P(C) GT(A) GT(B) GT(C)
1 0.8 0.1 0.1 1 0 0
2 0.5 0.4 0.1 0 1 0
3) 0.75 0.2 0.05 1. 0 0
4 0.05 0.2 0.75 0 i?) 1
5 0.2 0.7 0.1 0 1 0
6 0.05 0.9 0.05 (°) 1 ie}
b. Formulate the loss function of YOLO object detection algorithm. Briefly explain non max {10]

suppression and output unit of YOLO.
````
