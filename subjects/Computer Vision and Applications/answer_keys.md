# Computer Vision and Applications: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper a0509a860d8c

- Departments: Data Science
- Programmes: BTech DS 7009
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_DS_7009/Computer Vision and Applications/ANS_Computer Vision and Applications(702DB0C024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (6 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Computer Vision and Applications
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Qestion No 1 is compullsory
5. Out if the remaining questions, attempt any 4
6. In all 5 questions to be attempted
Q1. All Questions are Compulsory   [20]
a. An image processing pipeline needs to scale a 2D point by a factor of 2, rotate it by 90 degrees, and
translate it by t(x) = 10, t(y) = 5$. Express a sample point (x,y) in
homogeneous coordinates, and construct the single composite affine matrix required to perform all
three operations simultaneously.   [4]
Affine Transform:
(i) Must show homogeneous coordinates P = [x, y, 1]^T.
(ii) Must correctly set up Scale, Rotation, and Translation matrices.
(iii) Must state that the final single matrix is a product of all three: M = T * R *
b. What is the difference between the derivative of a Gaussian filter and the Difference of Gaussians
filter? Provide an example of where each of these is practically used in image processing / computer
vision.
[4]
Gaussian Filters:
(i) Derivative of Gaussian is for exact edge detection (e.g., Canny).
(ii) Difference of Gaussians (DoG) is a faster mathematical approximation used for scale-space extrema
detection (e.g., SIFT).
c. While configuring a Canny edge detector for a robotic assembly line, you notice the
output contains many fragmented, broken edges along the conveyor belt. Describe the Canny pipeline
and which specific step is responsible for fixing this? Explain how modifying the upper and lower values
in the double thresholding step will help link these broken edge pixels.
[4]
Canny Edges:
(i) The "Hysteresis Thresholding" (Double Thresholding) step is responsible.
(ii) Lowering the lower threshold or tightening the gap allows weak pixels to be connected to strong edge pixels,
closing the fragmented gaps.
********** 1 **********
--- page 2 ---
d. In the context of Image Processing using Convolution Networks, explain the following components of
the network, and their function, in a maximum of 2-3 sentences each:
(i) Convolution layer
(ii) Pooling layer
(iii) Activation function
(iv) Fully-connected layer   [4]
CNN Components:
(i) Convolution extracts spatial features.
(ii) Pooling reduces dimensionality and provides spatial invariance.
(iii) Activation introduces non-linearity (e.g., ReLU).
(iv) Fully-Connected Layer maps features to final classification labels.
e. Describe motion detection and object tracking techniques in video analysis. [4]
Motion Tracking:
(i) Must mention background subtraction for initial motion detection.
(ii) Must mention either Optical Flow (Lucas-Kanade), Kalman Filters, or Mean Shift for tracking the detected
object across frames.
Optional Group (Attempt Any 4)   [80]
Q2.
[20]
a. Obtain the output image when the following filters are applied on the following image:
(i) Box filter of size (3x3)
(ii) Sobel filter (vertical edge)
(iii) Gaussian filter (size 5x5)   [10]
Filters:
(i) Box filter output: uniformly blurred/smoothed image.
(ii) Sobel filter output: highlights vertical edges, darkens flat regions.
(iii) Gaussian filter output: natural smoothing that preserves structural edges better than the Box filter.
b. Suppose you are given two consecutive frames of a traffic camera capturing a fast moving car where the
car moved by 20 pixels to the right and 15 pixels down and you apply the standard Lucas-Kanade optical
flow algorithm with a small window (5x5).
********** 2 **********
--- page 3 ---
(a) Explain why the algorithm is likely to fail in estimating the correct motion.
(b) Identify which assumptions of optical flow are violated.
(c) Describe the result of the above algorithm qualitatively.
(d) Describe how pyramidal Lucas-Kanade algorithm helps in this case.
(e) If the image is down sampled by a factor of 2 at each level: What will be the apparent motion at level 1? At
level 2?   [10]
Lucas-Kanade:
(i) Fails because the large pixel shift violates the "small motion" (Spatial Coherence) assumption.
(ii) Pyramidal LK solves this by downsampling the image so large pixel shifts become small sub-pixel shifts at
higher pyramid levels.
(iii) Level 1 apparent motion calculation: 10px right, 7.5px down.
(iv) Level 2 apparent motion calculation: 5px right, 3.75px down.
Q3.
[20]
a. Suppose you are asked to run the inference of the images for classification that are captured on a slow-
moving conveyer belt in a corn-flakes factory. Each image can capture hundreds of corn flakes. Your
classification results will be used to take actions - whether to discard the flakes in the image or not. You
have the option of using YOLO and Faster-RCNN models.
(a) Which of the two models is appropriate for the above use case?
(b) Explain why the selected model gives faster response based on the model architectures.
(c) Will your answer change if the application is changed where the images now contain bigger and
fewer objects - for example in case of self-driving vehicles?
(d) Provide justification for your answer.   [10]
YOLO vs R-CNN:
(i) Must select YOLO for the fast-moving belt due to its single-stage, real-time processing speed.
(ii) Faster R-CNN is too slow because the Region Proposal Network (RPN) creates a computational bottleneck.
(iii) For self-driving, both are viable, but YOLO is still preferred for real-time safety, while Faster R-CNN is better
for detecting tiny distant objects.
b. Consider the case of running Harris Corner Detection on a patch in the following chessboard image. The
white squares have value 2 and the black squares have value 0. Assume a square window function
(w(x,y) = 1), and the patch is exactly 2x2 pixels:
P = [0 2
2 0]
For image derivatives, use: Dx = [1 0 -1], Dy = [1 0 -1]^T
(a) Compute image gradients Ix and Iy.
********** 3 **********
--- page 4 ---
(b) Compute Ix^2, Iy^2, IxIy.
(c) Compute the second moment matrix M.
(d) Compute Harris Corner Response using the following equation assuming   k = 0.04.
(e) Compute the eigenvalues of the second moment matrix.
(f) Is the patch a corner or an edge?
(g) Would the classification change if we increased the patch size? Why or why not?   [10]
Harris Corner:
(i) Check for calculation of Ix, Iy image gradients.
(ii) Check calculation of the Second Moment Matrix using Ix^2, Iy^2, and IxIy.
(iii) Must calculate the final Harris response R.
(iv) Student should note that a larger patch size makes the detection more robust to noise but less localized.
Q4.
[20]
a. You are building the preprocessing module for the "Eyeglass Classifier" virtual try-on kiosk. Before
passing the facial image to the machine learning model, you must segment the dark eyeglass frames
from the user's face. Construct a pipeline that reads an input image, applies binary thresholding to
segment the dark pixels, extracts the contours of the segmented regions, and draws a bounding
rectangle around the largest contour (representing the glasses). Mention the key OpenCV functions to
be used.   [10]
Eyeglass Pipeline:
(i) Read image and convert to Grayscale.
(ii) Apply binary inverse thresholding to segment dark glasses from light skin.
(iii) Use contour finding functions to locate shapes.
(iv) Extract the largest area and draw a bounding rectangle around it.
b. In the figure below, we applied a Gaussian filter to an image of a zebra’s nose and computed the
derivative. To obtain each of the images, we varied the standard deviation σ of the Gaussian filter.
Given a fixed kernel size, should the standard deviation σ of the Gaussian filter increase or decrease
from the leftmost to the rightmost image?
Provide justification to your answer.
[10]
Gaussian Sigma:
(i) The student must state that the standard deviation (sigma) increases from the leftmost to the rightmost
image.
(ii) Justification: A higher sigma flattens the Gaussian bell curve, pulling in pixel weights from further away,
which causes heavier blurring and loss of high-frequency detail.
********** 4 **********
--- page 5 ---
Q5.
[20]
a. SIFT is considered one of the most robust feature extractors in classical computer vision.
i) Outline the four primary stages of the SIFT calculation pipeline.
ii) Explain the concept of the Difference of Gaussians (DoG) pyramid in the first stage. Why is it used instead of
a standard Laplacian?
iii) What does each entry in the final 128-dimensional vector represent, and why does SIFT cap gradient
magnitudes during this final step? (Explain how this helps with illumination invariance).   [10]
SIFT:
(i) List the 4 stages: Scale-space extrema, keypoint localization, orientation assignment, descriptor generation.
(ii) DoG is used because it is an efficient mathematical approximation of the Laplacian of Gaussian.
(iii) The 128-D vector contains gradient histograms; capping the gradients prevents extreme illumination
changes from ruining the feature match.
b. Face recognition systems are widely used today. Explain the complete pipeline of a face recognition
system and mention two practical challenges it may face regarding deployment. Mention the key
OpenCV functions to be used. [10]
Face Recog Pipeline:
(i) Steps: Face Detection -> Alignment -> Feature Extraction -> Matching.
(ii) Common challenges include illumination shifts, pose variations, and occlusion.
(iii) Mention of relevant OpenCV functions (e.g., CascadeClassifier, FaceRecognizer).
Q6.
[20]
a. An animal shelter wants to build a mobile app to classify intake photos as 'Cat' or 'Dog'. Design and
implement an image classification pipeline for the same. Describe what would be the model you
would buil from scratch for   the same.. Which loss function would you
use and why?
You find out that they only have a small dataset of 500 images, which is not enough to train a deep neural
network from scratch without severe overfitting.
Explain the concept of Transfer Learning and detail the exact architectural changes you must make to the final
layers of the   pre-trained ImageNet model to adapt it for this
binary 'Cats vs. Dogs' task.   [10]
Cats vs Dogs:
(i) Pipeline architecture: Convolutional blocks -> Max Pooling -> Flatten -> Dense layer.
(ii) Must use Binary Cross-Entropy loss for a two-class problem.
(iii) Transfer Learning implementation: Freeze early ImageNet layers to prevent overfitting, and replace the
1000-class head with a new binary dense layer.
b. Design a License Plate Detection system for a parking mall. Explain how your system will handle
different lighting conditions, vehicle orientations, and moving backgrounds. Mention the key OpenCV
functions to be used.   [10]
License Plate:
(i) Pipeline: Grayscale -> Adaptive Thresholding or Bilateral Filter (to handle lighting) -> Canny Edge Detection.
********** 5 **********
--- page 6 ---
(ii) Contour selection by specific rectangular aspect ratios.
(iii) Mention of relevant OpenCV functions.
Q7 .
a. a. Deep Learning has revolutionized how we process both static images and dynamic video feeds.
b. Detail the complete architecture of a standard Convolutional Neural Network (CNN), explaining the
specific mathematical and functional roles of Convolution, Max Pooling, and Fully Connected layers. (4
marks)
c. Contrast the fundamental architectural memory of a CNN with that of a Recurrent Neural Network
(RNN). Provide one specific computer vision application where an RNN is strictly required. (3 marks)
d. Explain the concept of "Region Proposals" in the R-CNN framework. How does R-CNN differ from
standard, whole-image classification?
[10]
Deep Learning Architectures:
(i) CNN extracts spatial hierarchies; RNN maintains a hidden state (memory) for sequential temporal data.
(ii) Application for RNN: Video action recognition or video captioning.
(iii) R-CNN extracts thousands of sub-regions before classification, unlike a standard CNN which classifies the
whole image grid at once.
b. Explain modern object detection techniques with reference to Advanced Driver Assistance Systems (ADAS).
Specifically, describe how object detection frameworks are tuned and applied for pedestrian detection and lane
detection in self-driving cars. [10]
ADAS Object Detection:
(i) Must explain bounding box regression techniques for identifying pedestrians and vehicles.
(ii) Must explain segmentation or Hough Transforms for detecting lane markings.
********** 6 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 53ab59d80531

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_DS_7052/Computer Vision and Applications/ANS_Computer Vision and Applications(702DB0C024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (6 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Computer Vision and Applications
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Qestion No 1 is compullsory
5. Out if the remaining questions, attempt any 4
6. In all 5 questions to be attempted
Q1. All Questions are Compulsory   [20]
a. An image processing pipeline needs to scale a 2D point by a factor of 2, rotate it by 90 degrees, and
translate it by t(x) = 10, t(y) = 5$. Express a sample point (x,y) in
homogeneous coordinates, and construct the single composite affine matrix required to perform all
three operations simultaneously.   [4]
Affine Transform:
(i) Must show homogeneous coordinates P = [x, y, 1]^T.
(ii) Must correctly set up Scale, Rotation, and Translation matrices.
(iii) Must state that the final single matrix is a product of all three: M = T * R *
b. What is the difference between the derivative of a Gaussian filter and the Difference of Gaussians
filter? Provide an example of where each of these is practically used in image processing / computer
vision.
[4]
Gaussian Filters:
(i) Derivative of Gaussian is for exact edge detection (e.g., Canny).
(ii) Difference of Gaussians (DoG) is a faster mathematical approximation used for scale-space extrema
detection (e.g., SIFT).
c. While configuring a Canny edge detector for a robotic assembly line, you notice the
output contains many fragmented, broken edges along the conveyor belt. Describe the Canny pipeline
and which specific step is responsible for fixing this? Explain how modifying the upper and lower values
in the double thresholding step will help link these broken edge pixels.
[4]
Canny Edges:
(i) The "Hysteresis Thresholding" (Double Thresholding) step is responsible.
(ii) Lowering the lower threshold or tightening the gap allows weak pixels to be connected to strong edge pixels,
closing the fragmented gaps.
********** 1 **********
--- page 2 ---
d. In the context of Image Processing using Convolution Networks, explain the following components of
the network, and their function, in a maximum of 2-3 sentences each:
(i) Convolution layer
(ii) Pooling layer
(iii) Activation function
(iv) Fully-connected layer   [4]
CNN Components:
(i) Convolution extracts spatial features.
(ii) Pooling reduces dimensionality and provides spatial invariance.
(iii) Activation introduces non-linearity (e.g., ReLU).
(iv) Fully-Connected Layer maps features to final classification labels.
e. Describe motion detection and object tracking techniques in video analysis. [4]
Motion Tracking:
(i) Must mention background subtraction for initial motion detection.
(ii) Must mention either Optical Flow (Lucas-Kanade), Kalman Filters, or Mean Shift for tracking the detected
object across frames.
Optional Group (Attempt Any 4)   [80]
Q2.
[20]
a. Obtain the output image when the following filters are applied on the following image:
(i) Box filter of size (3x3)
(ii) Sobel filter (vertical edge)
(iii) Gaussian filter (size 5x5)   [10]
Filters:
(i) Box filter output: uniformly blurred/smoothed image.
(ii) Sobel filter output: highlights vertical edges, darkens flat regions.
(iii) Gaussian filter output: natural smoothing that preserves structural edges better than the Box filter.
b. Suppose you are given two consecutive frames of a traffic camera capturing a fast moving car where the
car moved by 20 pixels to the right and 15 pixels down and you apply the standard Lucas-Kanade optical
flow algorithm with a small window (5x5).
********** 2 **********
--- page 3 ---
(a) Explain why the algorithm is likely to fail in estimating the correct motion.
(b) Identify which assumptions of optical flow are violated.
(c) Describe the result of the above algorithm qualitatively.
(d) Describe how pyramidal Lucas-Kanade algorithm helps in this case.
(e) If the image is down sampled by a factor of 2 at each level: What will be the apparent motion at level 1? At
level 2?   [10]
Lucas-Kanade:
(i) Fails because the large pixel shift violates the "small motion" (Spatial Coherence) assumption.
(ii) Pyramidal LK solves this by downsampling the image so large pixel shifts become small sub-pixel shifts at
higher pyramid levels.
(iii) Level 1 apparent motion calculation: 10px right, 7.5px down.
(iv) Level 2 apparent motion calculation: 5px right, 3.75px down.
Q3.
[20]
a. Suppose you are asked to run the inference of the images for classification that are captured on a slow-
moving conveyer belt in a corn-flakes factory. Each image can capture hundreds of corn flakes. Your
classification results will be used to take actions - whether to discard the flakes in the image or not. You
have the option of using YOLO and Faster-RCNN models.
(a) Which of the two models is appropriate for the above use case?
(b) Explain why the selected model gives faster response based on the model architectures.
(c) Will your answer change if the application is changed where the images now contain bigger and
fewer objects - for example in case of self-driving vehicles?
(d) Provide justification for your answer.   [10]
YOLO vs R-CNN:
(i) Must select YOLO for the fast-moving belt due to its single-stage, real-time processing speed.
(ii) Faster R-CNN is too slow because the Region Proposal Network (RPN) creates a computational bottleneck.
(iii) For self-driving, both are viable, but YOLO is still preferred for real-time safety, while Faster R-CNN is better
for detecting tiny distant objects.
b. Consider the case of running Harris Corner Detection on a patch in the following chessboard image. The
white squares have value 2 and the black squares have value 0. Assume a square window function
(w(x,y) = 1), and the patch is exactly 2x2 pixels:
P = [0 2
2 0]
For image derivatives, use: Dx = [1 0 -1], Dy = [1 0 -1]^T
(a) Compute image gradients Ix and Iy.
********** 3 **********
--- page 4 ---
(b) Compute Ix^2, Iy^2, IxIy.
(c) Compute the second moment matrix M.
(d) Compute Harris Corner Response using the following equation assuming   k = 0.04.
(e) Compute the eigenvalues of the second moment matrix.
(f) Is the patch a corner or an edge?
(g) Would the classification change if we increased the patch size? Why or why not?   [10]
Harris Corner:
(i) Check for calculation of Ix, Iy image gradients.
(ii) Check calculation of the Second Moment Matrix using Ix^2, Iy^2, and IxIy.
(iii) Must calculate the final Harris response R.
(iv) Student should note that a larger patch size makes the detection more robust to noise but less localized.
Q4.
[20]
a. You are building the preprocessing module for the "Eyeglass Classifier" virtual try-on kiosk. Before
passing the facial image to the machine learning model, you must segment the dark eyeglass frames
from the user's face. Construct a pipeline that reads an input image, applies binary thresholding to
segment the dark pixels, extracts the contours of the segmented regions, and draws a bounding
rectangle around the largest contour (representing the glasses). Mention the key OpenCV functions to
be used.   [10]
Eyeglass Pipeline:
(i) Read image and convert to Grayscale.
(ii) Apply binary inverse thresholding to segment dark glasses from light skin.
(iii) Use contour finding functions to locate shapes.
(iv) Extract the largest area and draw a bounding rectangle around it.
b. In the figure below, we applied a Gaussian filter to an image of a zebra’s nose and computed the
derivative. To obtain each of the images, we varied the standard deviation σ of the Gaussian filter.
Given a fixed kernel size, should the standard deviation σ of the Gaussian filter increase or decrease
from the leftmost to the rightmost image?
Provide justification to your answer.
[10]
Gaussian Sigma:
(i) The student must state that the standard deviation (sigma) increases from the leftmost to the rightmost
image.
(ii) Justification: A higher sigma flattens the Gaussian bell curve, pulling in pixel weights from further away,
which causes heavier blurring and loss of high-frequency detail.
********** 4 **********
--- page 5 ---
Q5.
[20]
a. SIFT is considered one of the most robust feature extractors in classical computer vision.
i) Outline the four primary stages of the SIFT calculation pipeline.
ii) Explain the concept of the Difference of Gaussians (DoG) pyramid in the first stage. Why is it used instead of
a standard Laplacian?
iii) What does each entry in the final 128-dimensional vector represent, and why does SIFT cap gradient
magnitudes during this final step? (Explain how this helps with illumination invariance).   [10]
SIFT:
(i) List the 4 stages: Scale-space extrema, keypoint localization, orientation assignment, descriptor generation.
(ii) DoG is used because it is an efficient mathematical approximation of the Laplacian of Gaussian.
(iii) The 128-D vector contains gradient histograms; capping the gradients prevents extreme illumination
changes from ruining the feature match.
b. Face recognition systems are widely used today. Explain the complete pipeline of a face recognition
system and mention two practical challenges it may face regarding deployment. Mention the key
OpenCV functions to be used. [10]
Face Recog Pipeline:
(i) Steps: Face Detection -> Alignment -> Feature Extraction -> Matching.
(ii) Common challenges include illumination shifts, pose variations, and occlusion.
(iii) Mention of relevant OpenCV functions (e.g., CascadeClassifier, FaceRecognizer).
Q6.
[20]
a. An animal shelter wants to build a mobile app to classify intake photos as 'Cat' or 'Dog'. Design and
implement an image classification pipeline for the same. Describe what would be the model you
would buil from scratch for   the same.. Which loss function would you
use and why?
You find out that they only have a small dataset of 500 images, which is not enough to train a deep neural
network from scratch without severe overfitting.
Explain the concept of Transfer Learning and detail the exact architectural changes you must make to the final
layers of the   pre-trained ImageNet model to adapt it for this
binary 'Cats vs. Dogs' task.   [10]
Cats vs Dogs:
(i) Pipeline architecture: Convolutional blocks -> Max Pooling -> Flatten -> Dense layer.
(ii) Must use Binary Cross-Entropy loss for a two-class problem.
(iii) Transfer Learning implementation: Freeze early ImageNet layers to prevent overfitting, and replace the
1000-class head with a new binary dense layer.
b. Design a License Plate Detection system for a parking mall. Explain how your system will handle
different lighting conditions, vehicle orientations, and moving backgrounds. Mention the key OpenCV
functions to be used.   [10]
License Plate:
(i) Pipeline: Grayscale -> Adaptive Thresholding or Bilateral Filter (to handle lighting) -> Canny Edge Detection.
********** 5 **********
--- page 6 ---
(ii) Contour selection by specific rectangular aspect ratios.
(iii) Mention of relevant OpenCV functions.
Q7 .
a. a. Deep Learning has revolutionized how we process both static images and dynamic video feeds.
b. Detail the complete architecture of a standard Convolutional Neural Network (CNN), explaining the
specific mathematical and functional roles of Convolution, Max Pooling, and Fully Connected layers. (4
marks)
c. Contrast the fundamental architectural memory of a CNN with that of a Recurrent Neural Network
(RNN). Provide one specific computer vision application where an RNN is strictly required. (3 marks)
d. Explain the concept of "Region Proposals" in the R-CNN framework. How does R-CNN differ from
standard, whole-image classification?
[10]
Deep Learning Architectures:
(i) CNN extracts spatial hierarchies; RNN maintains a hidden state (memory) for sequential temporal data.
(ii) Application for RNN: Video action recognition or video captioning.
(iii) R-CNN extracts thousands of sub-regions before classification, unlike a standard CNN which classifies the
whole image grid at once.
b. Explain modern object detection techniques with reference to Advanced Driver Assistance Systems (ADAS).
Specifically, describe how object detection frameworks are tuned and applied for pedestrian detection and lane
detection in self-driving cars. [10]
ADAS Object Detection:
(i) Must explain bounding box regression techniques for identifying pedestrians and vehicles.
(ii) Must explain segmentation or Hough Transforms for detecting lane markings.
********** 6 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper aabd2b8a76ac

- Departments: Data Science
- Programmes: Integrated DS 7038
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_DS_7038/Computer Vision and Applications/ANS_Computer Vision and Applications(702DB0C024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (6 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (DS)/B. Tech Intg. (DS)/MBA Tech (DS)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Computer Vision and Applications
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Qestion No 1 is compullsory
5. Out if the remaining questions, attempt any 4
6. In all 5 questions to be attempted
Q1. All Questions are Compulsory   [20]
a. An image processing pipeline needs to scale a 2D point by a factor of 2, rotate it by 90 degrees, and
translate it by t(x) = 10, t(y) = 5$. Express a sample point (x,y) in
homogeneous coordinates, and construct the single composite affine matrix required to perform all
three operations simultaneously.   [4]
Affine Transform:
(i) Must show homogeneous coordinates P = [x, y, 1]^T.
(ii) Must correctly set up Scale, Rotation, and Translation matrices.
(iii) Must state that the final single matrix is a product of all three: M = T * R *
b. What is the difference between the derivative of a Gaussian filter and the Difference of Gaussians
filter? Provide an example of where each of these is practically used in image processing / computer
vision.
[4]
Gaussian Filters:
(i) Derivative of Gaussian is for exact edge detection (e.g., Canny).
(ii) Difference of Gaussians (DoG) is a faster mathematical approximation used for scale-space extrema
detection (e.g., SIFT).
c. While configuring a Canny edge detector for a robotic assembly line, you notice the
output contains many fragmented, broken edges along the conveyor belt. Describe the Canny pipeline
and which specific step is responsible for fixing this? Explain how modifying the upper and lower values
in the double thresholding step will help link these broken edge pixels.
[4]
Canny Edges:
(i) The "Hysteresis Thresholding" (Double Thresholding) step is responsible.
(ii) Lowering the lower threshold or tightening the gap allows weak pixels to be connected to strong edge pixels,
closing the fragmented gaps.
********** 1 **********
--- page 2 ---
d. In the context of Image Processing using Convolution Networks, explain the following components of
the network, and their function, in a maximum of 2-3 sentences each:
(i) Convolution layer
(ii) Pooling layer
(iii) Activation function
(iv) Fully-connected layer   [4]
CNN Components:
(i) Convolution extracts spatial features.
(ii) Pooling reduces dimensionality and provides spatial invariance.
(iii) Activation introduces non-linearity (e.g., ReLU).
(iv) Fully-Connected Layer maps features to final classification labels.
e. Describe motion detection and object tracking techniques in video analysis. [4]
Motion Tracking:
(i) Must mention background subtraction for initial motion detection.
(ii) Must mention either Optical Flow (Lucas-Kanade), Kalman Filters, or Mean Shift for tracking the detected
object across frames.
Optional Group (Attempt Any 4)   [80]
Q2.
[20]
a. Obtain the output image when the following filters are applied on the following image:
(i) Box filter of size (3x3)
(ii) Sobel filter (vertical edge)
(iii) Gaussian filter (size 5x5)   [10]
Filters:
(i) Box filter output: uniformly blurred/smoothed image.
(ii) Sobel filter output: highlights vertical edges, darkens flat regions.
(iii) Gaussian filter output: natural smoothing that preserves structural edges better than the Box filter.
b. Suppose you are given two consecutive frames of a traffic camera capturing a fast moving car where the
car moved by 20 pixels to the right and 15 pixels down and you apply the standard Lucas-Kanade optical
flow algorithm with a small window (5x5).
********** 2 **********
--- page 3 ---
(a) Explain why the algorithm is likely to fail in estimating the correct motion.
(b) Identify which assumptions of optical flow are violated.
(c) Describe the result of the above algorithm qualitatively.
(d) Describe how pyramidal Lucas-Kanade algorithm helps in this case.
(e) If the image is down sampled by a factor of 2 at each level: What will be the apparent motion at level 1? At
level 2?   [10]
Lucas-Kanade:
(i) Fails because the large pixel shift violates the "small motion" (Spatial Coherence) assumption.
(ii) Pyramidal LK solves this by downsampling the image so large pixel shifts become small sub-pixel shifts at
higher pyramid levels.
(iii) Level 1 apparent motion calculation: 10px right, 7.5px down.
(iv) Level 2 apparent motion calculation: 5px right, 3.75px down.
Q3.
[20]
a. Suppose you are asked to run the inference of the images for classification that are captured on a slow-
moving conveyer belt in a corn-flakes factory. Each image can capture hundreds of corn flakes. Your
classification results will be used to take actions - whether to discard the flakes in the image or not. You
have the option of using YOLO and Faster-RCNN models.
(a) Which of the two models is appropriate for the above use case?
(b) Explain why the selected model gives faster response based on the model architectures.
(c) Will your answer change if the application is changed where the images now contain bigger and
fewer objects - for example in case of self-driving vehicles?
(d) Provide justification for your answer.   [10]
YOLO vs R-CNN:
(i) Must select YOLO for the fast-moving belt due to its single-stage, real-time processing speed.
(ii) Faster R-CNN is too slow because the Region Proposal Network (RPN) creates a computational bottleneck.
(iii) For self-driving, both are viable, but YOLO is still preferred for real-time safety, while Faster R-CNN is better
for detecting tiny distant objects.
b. Consider the case of running Harris Corner Detection on a patch in the following chessboard image. The
white squares have value 2 and the black squares have value 0. Assume a square window function
(w(x,y) = 1), and the patch is exactly 2x2 pixels:
P = [0 2
2 0]
For image derivatives, use: Dx = [1 0 -1], Dy = [1 0 -1]^T
(a) Compute image gradients Ix and Iy.
********** 3 **********
--- page 4 ---
(b) Compute Ix^2, Iy^2, IxIy.
(c) Compute the second moment matrix M.
(d) Compute Harris Corner Response using the following equation assuming   k = 0.04.
(e) Compute the eigenvalues of the second moment matrix.
(f) Is the patch a corner or an edge?
(g) Would the classification change if we increased the patch size? Why or why not?   [10]
Harris Corner:
(i) Check for calculation of Ix, Iy image gradients.
(ii) Check calculation of the Second Moment Matrix using Ix^2, Iy^2, and IxIy.
(iii) Must calculate the final Harris response R.
(iv) Student should note that a larger patch size makes the detection more robust to noise but less localized.
Q4.
[20]
a. You are building the preprocessing module for the "Eyeglass Classifier" virtual try-on kiosk. Before
passing the facial image to the machine learning model, you must segment the dark eyeglass frames
from the user's face. Construct a pipeline that reads an input image, applies binary thresholding to
segment the dark pixels, extracts the contours of the segmented regions, and draws a bounding
rectangle around the largest contour (representing the glasses). Mention the key OpenCV functions to
be used.   [10]
Eyeglass Pipeline:
(i) Read image and convert to Grayscale.
(ii) Apply binary inverse thresholding to segment dark glasses from light skin.
(iii) Use contour finding functions to locate shapes.
(iv) Extract the largest area and draw a bounding rectangle around it.
b. In the figure below, we applied a Gaussian filter to an image of a zebra’s nose and computed the
derivative. To obtain each of the images, we varied the standard deviation σ of the Gaussian filter.
Given a fixed kernel size, should the standard deviation σ of the Gaussian filter increase or decrease
from the leftmost to the rightmost image?
Provide justification to your answer.
[10]
Gaussian Sigma:
(i) The student must state that the standard deviation (sigma) increases from the leftmost to the rightmost
image.
(ii) Justification: A higher sigma flattens the Gaussian bell curve, pulling in pixel weights from further away,
which causes heavier blurring and loss of high-frequency detail.
********** 4 **********
--- page 5 ---
Q5.
[20]
a. SIFT is considered one of the most robust feature extractors in classical computer vision.
i) Outline the four primary stages of the SIFT calculation pipeline.
ii) Explain the concept of the Difference of Gaussians (DoG) pyramid in the first stage. Why is it used instead of
a standard Laplacian?
iii) What does each entry in the final 128-dimensional vector represent, and why does SIFT cap gradient
magnitudes during this final step? (Explain how this helps with illumination invariance).   [10]
SIFT:
(i) List the 4 stages: Scale-space extrema, keypoint localization, orientation assignment, descriptor generation.
(ii) DoG is used because it is an efficient mathematical approximation of the Laplacian of Gaussian.
(iii) The 128-D vector contains gradient histograms; capping the gradients prevents extreme illumination
changes from ruining the feature match.
b. Face recognition systems are widely used today. Explain the complete pipeline of a face recognition
system and mention two practical challenges it may face regarding deployment. Mention the key
OpenCV functions to be used. [10]
Face Recog Pipeline:
(i) Steps: Face Detection -> Alignment -> Feature Extraction -> Matching.
(ii) Common challenges include illumination shifts, pose variations, and occlusion.
(iii) Mention of relevant OpenCV functions (e.g., CascadeClassifier, FaceRecognizer).
Q6.
[20]
a. An animal shelter wants to build a mobile app to classify intake photos as 'Cat' or 'Dog'. Design and
implement an image classification pipeline for the same. Describe what would be the model you
would buil from scratch for   the same.. Which loss function would you
use and why?
You find out that they only have a small dataset of 500 images, which is not enough to train a deep neural
network from scratch without severe overfitting.
Explain the concept of Transfer Learning and detail the exact architectural changes you must make to the final
layers of the   pre-trained ImageNet model to adapt it for this
binary 'Cats vs. Dogs' task.   [10]
Cats vs Dogs:
(i) Pipeline architecture: Convolutional blocks -> Max Pooling -> Flatten -> Dense layer.
(ii) Must use Binary Cross-Entropy loss for a two-class problem.
(iii) Transfer Learning implementation: Freeze early ImageNet layers to prevent overfitting, and replace the
1000-class head with a new binary dense layer.
b. Design a License Plate Detection system for a parking mall. Explain how your system will handle
different lighting conditions, vehicle orientations, and moving backgrounds. Mention the key OpenCV
functions to be used.   [10]
License Plate:
(i) Pipeline: Grayscale -> Adaptive Thresholding or Bilateral Filter (to handle lighting) -> Canny Edge Detection.
********** 5 **********
--- page 6 ---
(ii) Contour selection by specific rectangular aspect ratios.
(iii) Mention of relevant OpenCV functions.
Q7 .
a. a. Deep Learning has revolutionized how we process both static images and dynamic video feeds.
b. Detail the complete architecture of a standard Convolutional Neural Network (CNN), explaining the
specific mathematical and functional roles of Convolution, Max Pooling, and Fully Connected layers. (4
marks)
c. Contrast the fundamental architectural memory of a CNN with that of a Recurrent Neural Network
(RNN). Provide one specific computer vision application where an RNN is strictly required. (3 marks)
d. Explain the concept of "Region Proposals" in the R-CNN framework. How does R-CNN differ from
standard, whole-image classification?
[10]
Deep Learning Architectures:
(i) CNN extracts spatial hierarchies; RNN maintains a hidden state (memory) for sequential temporal data.
(ii) Application for RNN: Video action recognition or video captioning.
(iii) R-CNN extracts thousands of sub-regions before classification, unlike a standard CNN which classifies the
whole image grid at once.
b. Explain modern object detection techniques with reference to Advanced Driver Assistance Systems (ADAS).
Specifically, describe how object detection frameworks are tuned and applied for pedestrian detection and lane
detection in self-driving cars. [10]
ADAS Object Detection:
(i) Must explain bounding box regression techniques for identifying pedestrians and vehicles.
(ii) Must explain segmentation or Hough Transforms for detecting lane markings.
********** 6 **********
````
