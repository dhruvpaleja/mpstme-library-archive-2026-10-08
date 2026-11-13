# Computer Vision: question papers in full

57 unique papers · 2011-12 to 2025-26 · Artificial Intelligence, Data Science, Computer Engineering, AI and Data Science, AI and Machine Learning, Electronics and Telecommunication, Common (all branches), Information Technology

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Exam not stated · Sem 7 · paper 25e34ee908f9

- Departments: Artificial Intelligence, Data Science
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE, B TECH / CSE DATA SCIENCE (311)
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/ARTIFICIAL INTELLIGENCE/SEM-VII/COMPUTER VISION/B Tech, MBA Tech, (CSE-DS(311),AI), Computer Vision, Sem-VII, Batch 2023-2024 & 2_3d965e05.pdf` (+1 identical copies)
- Printed on paper: max marks: 100
- Text: ocr (4 pages), mean OCR confidence 87.0

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS ENGINEERING
Academic Year: 2025-2026

Program: B. Tech./ MBA Tech Stream: CSE(DS)/AI Year: TV Semester: VII

Subject: Computer Vision Time: 3 _ hrs (\ozonanto 4.00pm)
Date: _24 / \ /2025 No. of Pages: 4

Marks: 100

_ Re] Examination (23-24/24-25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume suitable data if necessary.

Ql Answer briefly:
CO-1; | a | What are the three key limitations of human vision, and how does computer vision | [05]
SO-1; help to overcome these limitations?
BL-4
CO-2; | b | In SIFT algorithm, if the number of octaves is changed from 4 to 6, what effect will it | [05]
SO-1; have on the length of the feature vector for orientation assignment of key points?
BL-4

COo- c | Apply the mean-shift algorithm to the following image, using the given parameters: | [05]

3,4; e Color bandwidth = 18, Threshold for convergence: distance between old and
SO-1; new means = 30
BL-3 _ —50 55 60 190 200

Image = [ex 4s 202 196 2051

CO-1; | d_ | Briefly explain the concept of invariants, their types, and applications in 3D computer | [05]

SO-1; vision.
BL-2
Answer any four from Q2 to Q7
Q2 a | Elaborate on the typical steps involved in the process of recognition in computer | [10]
CO-4: vision.
SO-1;
BL-2

Page 1 of 4
--- page 2 ---
CO-2; [| b_ | Apply the following two Gaussian filters to update the pixels in the highlighted 3x3 [10]

SO-1; region of the given image. Do not update the non-highlighted boundary pixels.
BL-5 Evaluate and compare the results obtained from both filters.
12 1 ,fi 1 1
Gaussian filters, fi=xl2 4 2,fh=a]1 2 1
lr 24 Mir 44
Image:
1} 1 1 1] 1
1);,5]5 15] 1
1 5 5 5 1
1 5 5 5 1
1 1 1 1 1
Q3 a | Perform the Harris Corner Detection on the following 5x5 grayscale image using the | [10]
CO-2: filter below to determine whether a corner is present at the center pixel.
SO-1; Given parameters: Harris constant k = 0.06, Threshold for corner response R > 20000
BL-3 Vertical filter: Horizontal filter:
1 0 -1 1 1 1
1 0 -l 0 0 0
1 0 -1 -l -1 -1

0 0 12 0 0

0 0 12 0 0

o | o | 2] 0 4] 0
o | o | 12 | 0 | Oo

0 0 12 0 0

CO-3;| b | Perform K-means clustering with K = 2 on the following 3x3 grayscale image. [10]

SO-1; Use absolute distance on intensity values (1-D) and start with initial centroids C1=20

BL-3 and C2=200. Perform iterations until convergence, showing the assignment step and
centroid updates. Finally give the final cluster centers and the clustered image with

labels for each pixel.

Page 2 of 4
--- page 3 ---
Image:
18 22 20

200 | 210 | 205

19 21 18
Q4 a_ | Apply the Speeded-Up Robust Features (SURF) method to perform keypoint [10]
Son. detection by constructing a Hessian matrix for the highlighted region of the image.
BL-3 (Given: The constant, W = 0.9, and the threshold = 15)

Image =

1 2 2 2 1

1 1 1 1 1
00 0 0 0 0 0 0 0 0
01-2 1,0 0 1 1 1 £40

G,=|0 1 -2 1 O}|, G,=j]0 -—2 -2 —2 OF,

01-210 0 1 1 1 £=+0
00 0 0 0 0 0 0 0 0

0 0 0 0 0
0 1 0-10
Gy=|0 0 0 0 0
0-10 1 0
0 0 0 0 0

CO-2;| b | Find the mean and standard deviation for the following pixel intensity values Xi(t), X2 | [10]
SO-1; (t), Xa(t), X(t), Xs(t) in an image observed for K=5 in a Gaussian Mixture Model
BL-5 (GMM) and interpret the results. ;

Page 3 of 4
--- page 4 ---
Xi (t) = [5,6,5]
X(t) = [251, 252, 254]
X4(t) = [250,.249, 250)
X4(t) = [250, 250, 248)

X3(t) = (0, 0, 0]

Q5 a_ | Write a note on essential matrix. Let the point in the first image be x and the | [10]
CO-1: corresponding point in the second image be x’. Use the following essential matrix E to
S0-1: determine if the epipolar constraint is perfectly satisfied:

BL-3

0 -1 2 1 2
e-([1 0 “1 ; =[P ; x'=]1
—2 #1 0 1 1

co-4; | b | Discuss the crucial blocks including Perception, Analysis, and Response in | [10]

SO-1; surveillance systems.
BL-2

Q6 a | Compute epipolar line on the right image given the coordinates of point X and the | [10]
CO-1: fundamental matrix F.

SO-1; 343.5300 —0.00310695 —0.0025646 2.96584

BL-3 y= 221.7005} F=| —0.028094 —0.00771621 56.3813

1 13.1905 —29.2007 —9999.79

CO-4; | b | Brief on various types of image acquisition systems available for vehicle vision | [10]
SO-1; system.

BL-2

Q7 a | Explain the Correspondence problem in 3-dimensional vision. [10]
CO-1;
SO-1;

BL-2
CO-4; | b | Enlist and explain the major challenges encountered in dry cereal grain quality | [10]
SO-1; inspection from the perspective of computer vision.

BL-2

Page 4 of 4
````

## 2025-26 · Final-Exam · Sem 2 · paper a30fce4374a9

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS) - 7027
- Source: `00_Original_Downloads/2025/Semester II/76514__Final-Exam.zip :: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS) - 7027/Computer Vision/QP_Final-Exam_Computer Vision(703DB0E027)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: M. Tech (AI)/M. Tech - DS (BA)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Computer Vision
Date: 05 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q No.   Part   Question   Marks
Q1   a   What is image processing? List its common objectives and explain any two   4
CO1   types of image processing with examples.
BL-
1,2,3
b   What is the Harris Corner Detector? Explain its basic principle and state three   4
CO3   real-world use cases.
BL-
2,3,4
c   Define a Convolutional Neural Network (CNN). Name its key layers and   4
CO2   explain the role of Max Pooling.
BL-
2,3,4,5
d   What is YOLO? State how it differs from traditional two-stage object detectors   4
CO4   like R-CNN.
BL-
2,3,4
Q2   a   Explain histogram equalization as an image enhancement technique. Describe   10
CO3   how it works, state its formula, and discuss its advantages and limitations with
BL-3,4   a real-world example.
b   Compare Discrete Fourier Transform (DFT) and Fast Fourier Transform (FFT)   10
CO3   in image processing. Explain low-pass, high-pass, and band-pass frequency
BL-   filters with use cases for each.
3,5,6
Q3   a   A manufacturing company wants to automate quality inspection of products on   10
CO3   an assembly line using computer vision.
BL-3,5   1. Which image segmentation techniques would you recommend for separating
defective regions from the background? Explain Thresholding and Watershed
Segmentation in detail.
2. How would you apply the Canny Edge Detector to identify defect
boundaries? Describe its five steps.
3. What challenges might arise and how would you address them?
********** 1 **********
--- page 2 ---
Q No.   Part   Question   Marks
b   Explain SIFT (Scale-Invariant Feature Transform) as a feature extraction   10
CO4   method. Describe why it is scale-invariant and rotation-invariant, and compare
BL-   it with SURF (Speeded-Up Robust Features) in terms of speed, accuracy, and
2,3,4   use cases.
Q4   a   Explain Generative Adversarial Networks (GANs) in detail. Describe the GAN   10
CO4   training process, the loss functions used, and explain two practical applications
BL-   of GANs in computer vision.
2,3,4
b   A healthcare startup wants to improve the quality of low-resolution chest X-ray   10
CO5   images before feeding them into a diagnostic model.
BL-   1. Which image enhancement and restoration techniques would you apply
3,4,5,6   (histogram equalization, denoising, deblurring)? Explain each.
2. Explain how Linear Filtering (Convolution and Gaussian Filtering) helps in
pre-processing these medical images.
3. How would GANs help in generating high-quality synthetic X-ray data to
augment the training dataset?
Q5   a   A smart city surveillance system needs to detect pedestrians and vehicles in   10
CO5   real time.
BL-   1. Compare YOLO and SSD object detection architectures — explain how each
3,4,5,6   works, their speed vs accuracy tradeoffs.
2. Which architecture would you choose for real-time camera feeds and why?
3. How would you handle class imbalance in the training dataset for rare
vehicle types (e.g., ambulances)?
b   A hospital wants to classify skin lesion images (benign/malignant) but has only   10
CO4   800 labeled images.
BL-   1. Explain Transfer Learning and why it is the most appropriate approach here.
2,3,4   2. Describe the fine-tuning strategy using ResNet-50: which layers to freeze,
which to retrain, and why.
3. What data augmentation techniques would you apply to expand the dataset
and improve generalization?
Q6   a   A robotics company is developing a system to track moving objects on a   10
CO3   factory floor using cameras.
BL-   1. Explain Optical Flow for moving object description — what it measures and
2,3,4,5   two algorithms (Lucas-Kanade, Horn-Schunck).
2. Explain Background Subtraction for detecting moving objects — describe
the MOG2 method.
3. How would you combine both approaches for robust object tracking?
b   A mobile app startup wants to create an image matching feature (like Google   10
CO5   Lens) that can identify products from a photo.
BL-   1. Explain the role of keypoint detection using Harris Corner Detector and
3,4,5,6   SIFT in building a product recognition pipeline.
2. Explain camera calibration and pose estimation — why are they important
when the photo angle varies?
3. How would feature descriptors enable robust matching across different
lighting and viewpoints?
Q7   a   A satellite imagery company wants to detect deforestation by comparing forest   10
CO1   images taken at different times.
********** 2 **********
--- page 3 ---
Q No.   Part   Question   Marks
BL-   1. Which image processing techniques would you use for pre-processing (noise
3,4,6   removal, enhancement)?
2. How would change detection using image segmentation and feature
extraction identify deforested areas?
3. What CNN-based approach would you use to classify and localize
deforestation at scale?
b   Explain the complete ML pipeline for a Computer Vision task: image   10
CO3   collection, preprocessing, model selection, training, evaluation, and
BL-2,3   deployment.
A self-driving car company needs to deploy a real-time pedestrian detection
system.
1. Describe the pipeline from data collection (dashcam footage) to model
deployment on an edge device.
2. What evaluation metrics (precision, recall, mAP) would you use and why?
3. How would you handle model drift after deployment?
********** 3 **********
````

## 2025-26 · Final-Exam · Sem 2 · paper 9fa4ef7b9928

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Computer Vision/QP_Computer Vision(703DB0E027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: M. Tech (AI)/M. Tech - DS (BA)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Computer Vision
Date: 05 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q No.   Part   Question   Marks
Q1   a   What is image processing? List its common objectives and explain any two   4
CO1   types of image processing with examples.
BL-
1,2,3
b   What is the Harris Corner Detector? Explain its basic principle and state three   4
CO3   real-world use cases.
BL-
2,3,4
c   Define a Convolutional Neural Network (CNN). Name its key layers and   4
CO2   explain the role of Max Pooling.
BL-
2,3,4,5
d   What is YOLO? State how it differs from traditional two-stage object detectors   4
CO4   like R-CNN.
BL-
2,3,4
Q2   a   Explain histogram equalization as an image enhancement technique. Describe   10
CO3   how it works, state its formula, and discuss its advantages and limitations with
BL-3,4   a real-world example.
b   Compare Discrete Fourier Transform (DFT) and Fast Fourier Transform (FFT)   10
CO3   in image processing. Explain low-pass, high-pass, and band-pass frequency
BL-   filters with use cases for each.
3,5,6
Q3   a   A manufacturing company wants to automate quality inspection of products on   10
CO3   an assembly line using computer vision.
BL-3,5   1. Which image segmentation techniques would you recommend for separating
defective regions from the background? Explain Thresholding and Watershed
Segmentation in detail.
2. How would you apply the Canny Edge Detector to identify defect
boundaries? Describe its five steps.
3. What challenges might arise and how would you address them?
********** 1 **********
--- page 2 ---
Q No.   Part   Question   Marks
b   Explain SIFT (Scale-Invariant Feature Transform) as a feature extraction   10
CO4   method. Describe why it is scale-invariant and rotation-invariant, and compare
BL-   it with SURF (Speeded-Up Robust Features) in terms of speed, accuracy, and
2,3,4   use cases.
Q4   a   Explain Generative Adversarial Networks (GANs) in detail. Describe the GAN   10
CO4   training process, the loss functions used, and explain two practical applications
BL-   of GANs in computer vision.
2,3,4
b   A healthcare startup wants to improve the quality of low-resolution chest X-ray   10
CO5   images before feeding them into a diagnostic model.
BL-   1. Which image enhancement and restoration techniques would you apply
3,4,5,6   (histogram equalization, denoising, deblurring)? Explain each.
2. Explain how Linear Filtering (Convolution and Gaussian Filtering) helps in
pre-processing these medical images.
3. How would GANs help in generating high-quality synthetic X-ray data to
augment the training dataset?
Q5   a   A smart city surveillance system needs to detect pedestrians and vehicles in   10
CO5   real time.
BL-   1. Compare YOLO and SSD object detection architectures — explain how each
3,4,5,6   works, their speed vs accuracy tradeoffs.
2. Which architecture would you choose for real-time camera feeds and why?
3. How would you handle class imbalance in the training dataset for rare
vehicle types (e.g., ambulances)?
b   A hospital wants to classify skin lesion images (benign/malignant) but has only   10
CO4   800 labeled images.
BL-   1. Explain Transfer Learning and why it is the most appropriate approach here.
2,3,4   2. Describe the fine-tuning strategy using ResNet-50: which layers to freeze,
which to retrain, and why.
3. What data augmentation techniques would you apply to expand the dataset
and improve generalization?
Q6   a   A robotics company is developing a system to track moving objects on a   10
CO3   factory floor using cameras.
BL-   1. Explain Optical Flow for moving object description — what it measures and
2,3,4,5   two algorithms (Lucas-Kanade, Horn-Schunck).
2. Explain Background Subtraction for detecting moving objects — describe
the MOG2 method.
3. How would you combine both approaches for robust object tracking?
b   A mobile app startup wants to create an image matching feature (like Google   10
CO5   Lens) that can identify products from a photo.
BL-   1. Explain the role of keypoint detection using Harris Corner Detector and
3,4,5,6   SIFT in building a product recognition pipeline.
2. Explain camera calibration and pose estimation — why are they important
when the photo angle varies?
3. How would feature descriptors enable robust matching across different
lighting and viewpoints?
Q7   a   A satellite imagery company wants to detect deforestation by comparing forest   10
CO1   images taken at different times.
********** 2 **********
--- page 3 ---
Q No.   Part   Question   Marks
BL-   1. Which image processing techniques would you use for pre-processing (noise
3,4,6   removal, enhancement)?
2. How would change detection using image segmentation and feature
extraction identify deforested areas?
3. What CNN-based approach would you use to classify and localize
deforestation at scale?
b   Explain the complete ML pipeline for a Computer Vision task: image   10
CO3   collection, preprocessing, model selection, training, evaluation, and
BL-2,3   deployment.
A self-driving car company needs to deploy a real-time pedestrian detection
system.
1. Describe the pipeline from data collection (dashcam footage) to model
deployment on an edge device.
2. What evaluation metrics (precision, recall, mAP) would you use and why?
3. How would you handle model drift after deployment?
********** 3 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 9cd3c99143f9

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIDS_7056/COMPUTER VISION FOR AI/QP_COMPUTER VISION FOR AI(702AI0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI
Date: 05 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Use of Scientific calculator is allowed.
Q1   Answer briefly:   [20]
CO- 2   a. For a localized window in an image, the gradient sums are calculated as   [05]
SO- 1
BL- 2,3   ∑𝐼𝑥 2 = 40,   ∑𝐼𝑦 2 = 45   , ∑𝐼𝑥𝐼𝑦= 5.
Compute   the   Harris   Response 𝑅   (Consider 𝑘= 0.04   )   and
classify the feature at this location.
CO- 3   b. Two images have histogram intersection scores 0.95 (Level 0) and 1.0 (Level 1).   [05]
SO-1   Weights are 1 and 0.5 respectively. Evaluate their feature similarity using image
BL-3   pyramids techniques.
CO- 4   c.   In the context of Mean Shift image segmentation, consider a 1D feature space   [05]
SO- 1   with the following pixel intensity values: X = {10, 12, 15, 16, 17, 25, 30}. If the
BL-2,3   algorithm starts at an initial estimate y1 = 15 with a bandwidth h = 3.
i.   Define the set of points that fall within the kernel window.
ii.   Calculate the mean shift vector and the resulting new center y2.
CO- 5   d.   List the primary functions of a Pooling Layer in a Convolutional Neural   [05]
SO- 1,6   Network (CNN) architecture and name three common types of pooling.
BL- 1,3
Q2   a   Classify each of the following scenarios as a Low-Level, Mid-Level, or High-
CO- 1   Level feature extraction process. Provide a brief explanation for each   [10]
SO- 1   classification.
BL-2,3
i.   Satellite imaging system enhances contrast and detects terrain edges
ii.   Security system identifies a person’s category
iii.   Agricultural drone segments crop regions based on color/texture
iv. A hand-gesture recognition system extracts contours of fingers before
classification.
v. A smart classroom attendance system detects students’ faces and
identifies each individual.
Q2   b   Given a 1D signal I = [10, 10, 10, 80, 80, 80] and two Gaussian kernels:   [10]
********** 1 **********
--- page 2 ---
CO- 1   G1 = [0.2, 0.6, 0.2]
SO- 1   G2 = [0.3, 0.4, 0.3]
BL- 3   Calculate the Difference of Gaussian values identify the exact location of the
Zero Crossing. Justify your answer by explaining the sign change.
Q3   a   Given the following 4 × 4 grayscale image patch   [10]
CO- 2   1 5 2 4
SO- 1   𝐼= [ 3 6 1 2 ]
BL- 2,3   2 4 5 1
1 2 3 4
i.   Compute the complete 4 × 4 Integral Image corresponding to the given
image patch.
ii.   Compute the sum of pixel intensities in the bottom-right region of the
original image, and apply the SURF (Speeded Up Robust Features)
keypoint detection method to the bottom-left 2x2 matrix.
Q3   b   Given an image of size 128 x128 pixels, calculate the total length of the   [10]
CO- 2   Histogram of Oriented Gradients (HOG) feature vector using the following
SO- 1   configuration:
BL-2,3   •   Cell Size: 8 x 8 pixels
• Block Size: 2 x 2 cells (16 x 16 pixels)
• Block Overlap: 50% (Stride = 8 pixels
i.   Calculate the total number of blocks across the width and height.
ii.   Compute the final length of the resulting feature vector.
iii. A pixel within a HoG cell has a calculated gradient magnitude of 25 and
an orientation angle of 55°. The histogram is constructed using 9 bins over
an unsigned 180° range, meaning each bin has a width of 20°. Assuming
the bin intervals start from 0°, calculate how the gradient magnitude of
this pixel is distributed among the appropriate adjacent histogram bins.
Assuming the interpolation points are anchored strictly at 40° and 60°
rather than the standard bin centers.
Q4   a   I. A feature matching algorithm extracts 3D descriptors from an image. You are   [10]
CO- 3   given the following set of reference descriptors to organize into a KD-Tree:
SO- 2   A = (5, 4, 9) ,B=(2,8,3),C=(8,1,7),D=(7,5,2),E=(1,6,4)
i.   Construct the KD-Tree for the descriptors.
BL-
ii. A descriptor from the query image is: Q=(3,7,4)
3,4,5   Using the constructed KD-Tree, determine the nearest matching
descriptor.
II. Explain the working principle of the Brute-Force feature matching technique.
How does it determine the matching key points between two images? What are
the primary disadvantages of the Brute-Force feature matching approach?
Explain how the "Ratio Test" is used to overcome one of these specific
limitations.
Q4   b An image retrieval system uses a small vocabulary of 3 visual words. You have   [10]
CO- 3   a database of 10 reference images (N=10). The raw visual word occurrence
SO- 2   histograms for two reference images (H1, H2) and a new query image (Q) are
provided below:
BL-3,4,5
• H1: [4, 2, 4]
• H2: [5, 0, 5]
********** 2 **********
--- page 3 ---
• Q: [3, 4, 3]
You are also given the Document Frequency (DF) for each visual word across
the entire 10-image database:
• DF1 = 10 (Word 1 appears in all 10 images)
• DF2 = 1 (Word 2 appears in only 1 image)
• DF3 = 10 (Word 3 appears in all 10 images)
Based on this data, Solve the following questions:
i) Determine the Term Frequency (TF) for all 3 visual words across H1, H2, and
Q.
ii) Compute the Inverse Document Frequency (IDF) for each visual word using
base-10 logarithms (IDF = Log10(N/DFi)).
iii) Calculate the final TF-IDF weighted feature vectors for H1, H2, and Q.
iv) Using Cosine Similarity on the resulting TF-IDF vectors, evaluate the
similarity between the query Q and the reference images. Identify which
reference image is the better match.
Q5   a   In Optical Flow, the motion of a pixel is described by the equation:   [10]
CO- 4   𝐼𝑥𝑢+ 𝐼𝑦𝑣+ 𝐼𝑡= 0
SO- 1   where:
BL-   𝑢= horizontal optical flow 𝑣= vertical optical flow
3,4,5   𝐼𝑥, 𝐼𝑦= spatial image gradients 𝐼𝑡= temporal gradient
A single pixel gives one equation with two unknowns, which is unsolvable.
The Lucas–Kanade method addresses this by assuming that all pixels inside a
small neighborhood (such as a 2 × 2 or 3 × 3 window) share the same motion.
Consider a 2 × 2 neighborhood having the following gradients:
Pixel   𝐼𝑥   𝐼𝑦   𝐼𝑡
1   2   1   –5
2   1   3   –7
3   3   2   –8
4   2   2   –6
Using the Lucas–Kanade method:
i.   Construct the matrices 𝐴= [𝐼𝑥   𝐼𝑦], 𝑏= [−𝐼𝑡]
ii.   Compute the optical flow vector u and v.
Q5   b   I. Given a 1D dataset X = {5, 12, 18, 25, 30, 45, 50}. You are asked to perform   [10]
CO- 4   K-means clustering (K=2) with initial centroids C1 = 15 and C2 = 40. Perform 1
SO- 1   iteration and determine the new cluster assignments and updated centroids.
II. Compare the Mean Shift algorithm with K-means clustering for image
BL-3,4,5
segmentation. Which is more suitable when the number of objects in an image is
unknown.
Q6   a   I. Differentiate between SIFT, SURF, and HoG based on the following four   [10]
CO- 2,3   technical criteria:
SO- 1
BL-3,4,5   • Invariance to scale and rotation.
• Computational efficiency/speed.
• Typical descriptor dimensionality.
• Primary application domain (e.g., global object detection vs. local point
matching).
********** 3 **********
--- page 4 ---
II. Given a simplified visual codebook with K = 2 cluster centers and an image
with 3 local feature descriptors (all in 2-dimensional space), Compute the final
L2-normalized Vector of Locally Aggregated Descriptors (VLAD) vector for the
image. Consider the following cluster center and Image descriptor:
• Cluster Centers (Codebook): C1 = (1, 1) and C2 = (5, 5)
• Image Descriptors: X1 = (2, 1), X2 = (1, 2), and X3 = (6, 4)
Q6   b   Convolutional Neural Network (CNN) designed for grayscale image processing.   [10]
CO- 5   The architecture is defined as follows:
SO- 2   Input Image: 64 × 64 × 1
BL-3,4   Layer 1: Conv1
• Kernel size: 5 × 5
• Number of filters: 16
•   Stride: 1
• Padding: 0 (Valid convolution)
Layer 2: MaxPool1
•   Kernel: 2 × 2
•   Stride: 2
Layer 3: Conv2
• Kernel size: 3 × 3
• Number of filters: 32
•   Stride: 2
• Padding: 1 (Same convolution)
Layer 4: FC1 (Fully Connected Layer)
•   Input: Flattened output of Conv2
• Output nodes: 128
Output Layer
• Softmax layer
•   Input: 128 units
• Output: 5 classes
i.   Compute the Output Shape (Height × Width × Depth) for every
layer.
ii.   Calculate the number of Trainable Parameters for every layer.
Q7   a   Explain the limitations of Selective Search used in R-CNN and Fast R-CNN. How   [10]
CO- 5   does Faster R-CNN overcome these using Region Proposal Networks?
SO- 2
BL-4,5
Q7   b An AgTech startup is building a robot to autonomously harvest strawberries. The   [10]
CO- 5   robot must find each berry and outline its exact shape so the robotic gripper can
SO- 2,6   pick it without crushing the delicate fruit.
BL-3,4,5
i.   In harvesting, a 5-pixel misalignment can cause the gripper to crush the
fruit. Explain how RoIAlign avoids the "quantization" errors found in
RoIPool
ii.   If the startup wants the robot to operate at very high speeds, they might
consider using YOLO instead of Mask R-CNN. However, standard YOLO
outputs "bounding boxes" (rectangles) rather than pixel-perfect masks.
Explain why using a bounding box instead of a precise mask might result
in the robot damaging the fruit.
********** 4 **********
--- page 5 ---
iii.   SegNet is an "encoder-decoder" architecture. Briefly explain what the
encoder does to the input image, and what the decoder does to reconstruct
the shape of the strawberry.
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 6a7242489e13

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/COMPUTER VISION/QP_COMPUTER VISION(702EX0E015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/MBA Tech (Comp)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: COMPUTER VISION
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Use of Scientific calculator is allowed.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 2   a. Consider a pixel neighbourhood where the elements of the second-moment   [05]
SO- 1   (structure)   matrix   are   given   as   follows:
BL-   𝑆𝑥𝑥= 18   ,   𝑆𝑦𝑦= 14   ,   and   𝑆𝑥𝑦= 6   .
2,3,4   Assume the Harris detector sensitivity parameter 𝑘= 0.04.
i. Calculate the Harris corner response 𝑅using
𝑅= det⁡(𝑀) −𝑘 (trace(𝑀))2
ii. Based on the computed values of the determinant and trace of the matrix,
interpret the nature of the image feature at this point. Indicate whether it
corresponds to a flat region, an edge, or a corner, and justify your answer.
CO- 3   b. Suppose two local image feature vectors extracted from different images are   [05]
SO- 1   represented as
BL-2,3   P = (1,4,2)⁡⁡⁡and⁡⁡⁡Q = (3,6,4)
i.   Calculate the cosine similarity between feature vectors P and Q.
ii.   Based on the computed similarity value, assess whether these two features
are likely to be a reliable match. Briefly justify your conclusion.
CO- 4   c.   i. Explain the importance of homogeneous coordinates in performing image   [05]
SO- 1   transformations in computer vision.
BL-3   ii. An image point 𝑄(4,5)is subjected to a scaling transformation with scaling
factors
𝑆𝑥= 3⁡along the x-axis and 𝑆𝑦= 2⁡along the y-axis.
Represent the point using homogeneous coordinates and determine the final
coordinates of the point after applying the scaling operation.
CO- 5   d. Define a feature map in the context of CNNs. How does the number of filters in   [05]
SO- 1   a convolutional layer affect the depth of the resulting feature maps?
BL- 2
********** 1 **********
--- page 2 ---
Q2   a A smart video surveillance system deployed in public spaces relies on a
CO- 1   multi-level vision architecture to monitor activities and detect security threats.   [10]
SO- 1   i. Explain the responsibilities of low-level, mid-level, and high-level vision
BL-1,2   processing stages in the design of an intelligent surveillance system.
ii. Using the example of an automated CCTV surveillance system in a shopping
mall, describe how visual data is processed at each level:
• How raw video frames are enhanced and prepared at the low-level stage
• How objects, motion, or human activities are identified at the mid-level
stage
• How suspicious behaviour or security alerts are inferred at the high-level
stage.
iii. Illustrate how malfunction or inaccuracies at any one of these stages can
negatively impact the effectiveness of the entire surveillance system. Provide
suitable examples relevant to the shopping mall scenario.
Q2   b A 3 × 3grayscale image patch is given as:   [10]
CO- 1   12 18 12
SO- 2   𝐼= [ 18 36 18 ]
12 18 12
BL- 1,2
i.   Using the Laplacian kernel
0 1 0
[ 1 −4 1 ]
0 1 0
compute the Laplacian response at the center pixel.
Gaussian blurred responses of the same pixel at two scales are:
𝐺𝜎1 = 30, 𝐺𝜎2 = 24
ii.   Compute the Difference of Gaussian (DoG) and comment on whether it
indicates a significant feature.
iii.   If Sobel gradients are:
𝐺𝑥= 10, 𝐺𝑦= 5
Calculate Gradient magnitude Gradient direction
iv.   Assign the gradient direction to the closest HOG orientation bin:
0∘,  45∘,  90∘,  135∘
Q3   a   Consider a grayscale image represented by the following pixel intensity matrix:   [10]
CO- 2   2 1 3 4
SO- 1   [ 0 𝟏 𝟐 1 ]
BL-3,4,5   3 𝟐 𝟏 0
1 𝟏 𝟐 3
i.   Construct the integral image for the given matrix.
ii.   Using the integral image, compute the sum of pixel values in the 3 × 2
rectangular regions starting at position (2,2).
iii.   Explain how integral images allow constant-time computation of box
filter responses regardless of filter size.
********** 2 **********
--- page 3 ---
Q3   b The Scale-Invariant Feature Transform (SIFT) is a widely used algorithm for   [10]
CO- 2   detecting and describing distinctive local features that are robust to changes in
SO- 1   imaging conditions.
i.Explain how scale-space construction using Gaussian filtering enables the
BL-2,3,4
detection of keypoints that are invariant to scale variations in the image.
i.Discuss the role of accurate keypoint localization in SIFT and analyze how it
improves the stability and reliability of extracted features.
i.Describe the process of orientation assignment in the SIFT algorithm and explain
how this step ensures rotation invariance.
v.With suitable justification, explain why SIFT features outperform traditional
edge and corner detectors when matching images captured under real-world
variations such as changes in illumination, scale, and viewpoint.
Q4   a   Consider a set of 2-D feature points extracted from an image:   [10]
CO- 3   (1,1),  (3,3),  (9,9),  (11,11)
SO- 2
BL- 3,4   Assume the number of clusters 𝐾= 2and the initial cluster centers are given as:
𝜇1 = (1,1), 𝜇2 = (9,9)
Answer the following:
i.   Assign each data point to its nearest cluster centre using Euclidean
distance.
ii.   Calculate the updated cluster centroids after completing one iteration of
the K-means algorithm.
II. In a multi-resolution image matching approach, feature similarity is computed
at different levels of an image pyramid and combined using weighted scores.
Suppose two images produce the following histogram similarity values:
• Pyramid Level 0 (original resolution): similarity score = 0.88
• Pyramid Level 1 (reduced resolution): similarity score = 0.96
The corresponding weights assigned to these levels are:
• Level 0 → weight = 1.0
• Level 1 → weight = 0.6
Calculate the overall weighted feature similarity score between the two images.
Briefly explain how using multiple pyramid levels improves the robustness of
image similarity measurement.
Q4   b   In an image retrieval system based on the Bag of Visual Words (BoVW) model,   [10]
CO- 3   three database images are represented by the following visual word histograms:
SO- 2   𝐼1 = [3,1,2,0],𝐼2 = [1,2,0,2], 𝐼3 = [2,0,1,3]
BL-3,4,5
A query image has the histogram:
𝑄= [2,1,1,1]
i. Calculate the Term Frequency (TF) vectors for all images.
ii. Compute the Document Frequency (DF) and Inverse Document Frequency
(IDF) for each visual word.
iii. Determine the TF-IDF representation for the query image.
iv. Using Euclidean distance, identify which image in the database best matches
the query.
Q5   a   I. Consider the following one-dimensional data points:   [10]
CO-4   1,  3,  6,  11,  13
********** 3 **********
--- page 4 ---
SO- 1   A Mean Shift algorithm is applied with a kernel window (bandwidth) of 4.
BL- 3   Starting from the initial point 𝑥= 3:
i.   Perform the first iteration of the Mean Shift procedure by identifying all
data points within the window and computing the new mean.
ii.   Use the updated mean as the starting point and perform the second
iteration.
II. Compare and contrast the K-means clustering algorithm with the Mean Shift
clustering method, highlighting   their working principles, assumptions,
advantages, and limitations.
Q5   b   i. Why is it necessary to use multiple frames instead of a single frame for   [10]
CO- 2   background modelling in background subtraction techniques?
SO- 2   ii.   Explain the role of N consecutive images in constructing a reliable
background model for motion detection.
BL-3,4
iii.   In background subtraction methods, what problems arise   if the
background reference is built using only one image? How does using N
images overcome these problems?
Q6   a A drone-based mapping system detects a triangular Region of Interest (ROI)   [10]
CO- 5   corresponding to a rooftop segment. The vertices of the triangle in the image
SO- 2   coordinate system are:
BL-3   A (2, 3), B (6, 3), and C (4, 7)
To register this ROI with a reference map, the following 2D affine
transformations are applied sequentially:
• Scale the triangle by a factor of 𝑆𝑥= 2along the x-axis and 𝑆𝑦= 4along
the y-axis.
•   Translate the scaled triangle by 5 units rightward and 3 units downward.
Answer the following:
i. Write the scaling matrix and translation matrix using 3 × 3 homogeneous
coordinates.
ii. Determine the composite transformation matrix assuming scaling is followed
by translation.
iii. Compute the transformed coordinates of the triangle vertices 𝐴′, 𝐵′, 𝐶′.
Q6   b   I) Discuss the limitations of using an brute-force feature matching strategy when   [10]
CO- 3,5   comparing descriptors from two images. Consider aspects such as accuracy,
SO- 2   ambiguity, and computational cost.
BL-2,3,4
II) An image of size 8 × 8 is processed through a convolutional layer in a
Convolutional Neural Network with the following configuration:
• Kernel (filter) size: 5 × 5
•   Stride: 2
• Zero padding: 1
• Number of convolution filters: 3
Answer the following:
i. Determine the spatial dimensions of the output feature map produced by each
filter.
ii. If each filter includes one bias parameter, compute the total number of
trainable parameters in this convolutional layer.
********** 4 **********
--- page 5 ---
Q7   a   i.   What were the main efficiency limitations in the original R-CNN   [10]
CO- 5   framework?
SO- 1   ii.   Describe how Fast R-CNN redesigned the detection pipeline to overcome
these inefficiencies.
BL-2
iii.   What was the major speed bottleneck that still remained in Fast R-CNN,
and how was it addressed in Faster R-CNN?
Q7   b   I) A convolutional neural network processes a grayscale image, producing the   [10]
CO- 5   following 4 × 4 feature map after the first convolution layer:
SO- 2   5 8 12 6
7 9 15 10
BL-3,4   𝐺= [   ]
4 6 20 18
3 5 16 14
i.   State the purpose of the pooling layer in CNNs.
ii.   Apply 2 × 2 pooling with stride 2 and compute the resulting feature
maps using:
a) Max Pooling
b) Average Pooling
c) Min Pooling
Show intermediate calculations clearly.
II.) The Faster R-CNN framework originally used RoIPool for extracting
fixed-size feature maps from proposal regions.
i.   Explain how quantization in the RoIPool layer introduces localization
inaccuracies during region pooling.
ii.   Discuss the impact of this quantization error on object detection accuracy,
particularly for small objects.
iii.   Describe how RoIAlign eliminates this issue and improves spatial
precision.
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper b591f67acdbf

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/COMPUTER VISION/QP_COMPUTER VISION(702EX0E015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/MBA Tech (Comp)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: COMPUTER VISION
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Use of Scientific calculator is allowed.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 2   a. Consider a pixel neighbourhood where the elements of the second-moment   [05]
SO- 1   (structure)   matrix   are   given   as   follows:
BL-   𝑆𝑥𝑥= 18   ,   𝑆𝑦𝑦= 14   ,   and   𝑆𝑥𝑦= 6   .
2,3,4   Assume the Harris detector sensitivity parameter 𝑘= 0.04.
i. Calculate the Harris corner response 𝑅using
𝑅= det⁡(𝑀) −𝑘 (trace(𝑀))2
ii. Based on the computed values of the determinant and trace of the matrix,
interpret the nature of the image feature at this point. Indicate whether it
corresponds to a flat region, an edge, or a corner, and justify your answer.
CO- 3   b. Suppose two local image feature vectors extracted from different images are   [05]
SO- 1   represented as
BL-2,3   P = (1,4,2)⁡⁡⁡and⁡⁡⁡Q = (3,6,4)
i.   Calculate the cosine similarity between feature vectors P and Q.
ii.   Based on the computed similarity value, assess whether these two features
are likely to be a reliable match. Briefly justify your conclusion.
CO- 4   c.   i. Explain the importance of homogeneous coordinates in performing image   [05]
SO- 1   transformations in computer vision.
BL-3   ii. An image point 𝑄(4,5)is subjected to a scaling transformation with scaling
factors
𝑆𝑥= 3⁡along the x-axis and 𝑆𝑦= 2⁡along the y-axis.
Represent the point using homogeneous coordinates and determine the final
coordinates of the point after applying the scaling operation.
CO- 5   d. Define a feature map in the context of CNNs. How does the number of filters in   [05]
SO- 1   a convolutional layer affect the depth of the resulting feature maps?
BL- 2
********** 1 **********
--- page 2 ---
Q2   a A smart video surveillance system deployed in public spaces relies on a
CO- 1   multi-level vision architecture to monitor activities and detect security threats.   [10]
SO- 1   i. Explain the responsibilities of low-level, mid-level, and high-level vision
BL-1,2   processing stages in the design of an intelligent surveillance system.
ii. Using the example of an automated CCTV surveillance system in a shopping
mall, describe how visual data is processed at each level:
• How raw video frames are enhanced and prepared at the low-level stage
• How objects, motion, or human activities are identified at the mid-level
stage
• How suspicious behaviour or security alerts are inferred at the high-level
stage.
iii. Illustrate how malfunction or inaccuracies at any one of these stages can
negatively impact the effectiveness of the entire surveillance system. Provide
suitable examples relevant to the shopping mall scenario.
Q2   b A 3 × 3grayscale image patch is given as:   [10]
CO- 1   12 18 12
SO- 2   𝐼= [ 18 36 18 ]
12 18 12
BL- 1,2
i.   Using the Laplacian kernel
0 1 0
[ 1 −4 1 ]
0 1 0
compute the Laplacian response at the center pixel.
Gaussian blurred responses of the same pixel at two scales are:
𝐺𝜎1 = 30, 𝐺𝜎2 = 24
ii.   Compute the Difference of Gaussian (DoG) and comment on whether it
indicates a significant feature.
iii.   If Sobel gradients are:
𝐺𝑥= 10, 𝐺𝑦= 5
Calculate Gradient magnitude Gradient direction
iv.   Assign the gradient direction to the closest HOG orientation bin:
0∘,  45∘,  90∘,  135∘
Q3   a   Consider a grayscale image represented by the following pixel intensity matrix:   [10]
CO- 2   2 1 3 4
SO- 1   [ 0 𝟏 𝟐 1 ]
BL-3,4,5   3 𝟐 𝟏 0
1 𝟏 𝟐 3
i.   Construct the integral image for the given matrix.
ii.   Using the integral image, compute the sum of pixel values in the 3 × 2
rectangular regions starting at position (2,2).
iii.   Explain how integral images allow constant-time computation of box
filter responses regardless of filter size.
********** 2 **********
--- page 3 ---
Q3   b The Scale-Invariant Feature Transform (SIFT) is a widely used algorithm for   [10]
CO- 2   detecting and describing distinctive local features that are robust to changes in
SO- 1   imaging conditions.
i.Explain how scale-space construction using Gaussian filtering enables the
BL-2,3,4
detection of keypoints that are invariant to scale variations in the image.
i.Discuss the role of accurate keypoint localization in SIFT and analyze how it
improves the stability and reliability of extracted features.
i.Describe the process of orientation assignment in the SIFT algorithm and explain
how this step ensures rotation invariance.
v.With suitable justification, explain why SIFT features outperform traditional
edge and corner detectors when matching images captured under real-world
variations such as changes in illumination, scale, and viewpoint.
Q4   a   Consider a set of 2-D feature points extracted from an image:   [10]
CO- 3   (1,1),  (3,3),  (9,9),  (11,11)
SO- 2
BL- 3,4   Assume the number of clusters 𝐾= 2and the initial cluster centers are given as:
𝜇1 = (1,1), 𝜇2 = (9,9)
Answer the following:
i.   Assign each data point to its nearest cluster centre using Euclidean
distance.
ii.   Calculate the updated cluster centroids after completing one iteration of
the K-means algorithm.
II. In a multi-resolution image matching approach, feature similarity is computed
at different levels of an image pyramid and combined using weighted scores.
Suppose two images produce the following histogram similarity values:
• Pyramid Level 0 (original resolution): similarity score = 0.88
• Pyramid Level 1 (reduced resolution): similarity score = 0.96
The corresponding weights assigned to these levels are:
• Level 0 → weight = 1.0
• Level 1 → weight = 0.6
Calculate the overall weighted feature similarity score between the two images.
Briefly explain how using multiple pyramid levels improves the robustness of
image similarity measurement.
Q4   b   In an image retrieval system based on the Bag of Visual Words (BoVW) model,   [10]
CO- 3   three database images are represented by the following visual word histograms:
SO- 2   𝐼1 = [3,1,2,0],𝐼2 = [1,2,0,2], 𝐼3 = [2,0,1,3]
BL-3,4,5
A query image has the histogram:
𝑄= [2,1,1,1]
i. Calculate the Term Frequency (TF) vectors for all images.
ii. Compute the Document Frequency (DF) and Inverse Document Frequency
(IDF) for each visual word.
iii. Determine the TF-IDF representation for the query image.
iv. Using Euclidean distance, identify which image in the database best matches
the query.
Q5   a   I. Consider the following one-dimensional data points:   [10]
CO-4   1,  3,  6,  11,  13
********** 3 **********
--- page 4 ---
SO- 1   A Mean Shift algorithm is applied with a kernel window (bandwidth) of 4.
BL- 3   Starting from the initial point 𝑥= 3:
i.   Perform the first iteration of the Mean Shift procedure by identifying all
data points within the window and computing the new mean.
ii.   Use the updated mean as the starting point and perform the second
iteration.
II. Compare and contrast the K-means clustering algorithm with the Mean Shift
clustering method, highlighting   their working principles, assumptions,
advantages, and limitations.
Q5   b   i. Why is it necessary to use multiple frames instead of a single frame for   [10]
CO- 2   background modelling in background subtraction techniques?
SO- 2   ii.   Explain the role of N consecutive images in constructing a reliable
background model for motion detection.
BL-3,4
iii.   In background subtraction methods, what problems arise   if the
background reference is built using only one image? How does using N
images overcome these problems?
Q6   a A drone-based mapping system detects a triangular Region of Interest (ROI)   [10]
CO- 5   corresponding to a rooftop segment. The vertices of the triangle in the image
SO- 2   coordinate system are:
BL-3   A (2, 3), B (6, 3), and C (4, 7)
To register this ROI with a reference map, the following 2D affine
transformations are applied sequentially:
• Scale the triangle by a factor of 𝑆𝑥= 2along the x-axis and 𝑆𝑦= 4along
the y-axis.
•   Translate the scaled triangle by 5 units rightward and 3 units downward.
Answer the following:
i. Write the scaling matrix and translation matrix using 3 × 3 homogeneous
coordinates.
ii. Determine the composite transformation matrix assuming scaling is followed
by translation.
iii. Compute the transformed coordinates of the triangle vertices 𝐴′, 𝐵′, 𝐶′.
Q6   b   I) Discuss the limitations of using an brute-force feature matching strategy when   [10]
CO- 3,5   comparing descriptors from two images. Consider aspects such as accuracy,
SO- 2   ambiguity, and computational cost.
BL-2,3,4
II) An image of size 8 × 8 is processed through a convolutional layer in a
Convolutional Neural Network with the following configuration:
• Kernel (filter) size: 5 × 5
•   Stride: 2
• Zero padding: 1
• Number of convolution filters: 3
Answer the following:
i. Determine the spatial dimensions of the output feature map produced by each
filter.
ii. If each filter includes one bias parameter, compute the total number of
trainable parameters in this convolutional layer.
********** 4 **********
--- page 5 ---
Q7   a   i.   What were the main efficiency limitations in the original R-CNN   [10]
CO- 5   framework?
SO- 1   ii.   Describe how Fast R-CNN redesigned the detection pipeline to overcome
these inefficiencies.
BL-2
iii.   What was the major speed bottleneck that still remained in Fast R-CNN,
and how was it addressed in Faster R-CNN?
Q7   b   I) A convolutional neural network processes a grayscale image, producing the   [10]
CO- 5   following 4 × 4 feature map after the first convolution layer:
SO- 2   5 8 12 6
7 9 15 10
BL-3,4   𝐺= [   ]
4 6 20 18
3 5 16 14
i.   State the purpose of the pooling layer in CNNs.
ii.   Apply 2 × 2 pooling with stride 2 and compute the resulting feature
maps using:
a) Max Pooling
b) Average Pooling
c) Min Pooling
Show intermediate calculations clearly.
II.) The Faster R-CNN framework originally used RoIPool for extracting
fixed-size feature maps from proposal regions.
i.   Explain how quantization in the RoIPool layer introduces localization
inaccuracies during region pooling.
ii.   Discuss the impact of this quantization error on object detection accuracy,
particularly for small objects.
iii.   Describe how RoIAlign eliminates this issue and improves spatial
precision.
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 7 · paper e2dffb309cbf

- Departments: AI and Machine Learning, Artificial Intelligence
- Programmes: BTech AI 7012, BTech AIML 7053, MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AIML_7053/COMPUTER VISION FOR AI/QP_COMPUTER VISION FOR AI(702AI0C029)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: ocr (6 pages), mean OCR confidence 83.9
- 2 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: B. Tech (AD/B. Tech (AI & ML)/MBA Tech (AD)

Year: IV/Semester VIl(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI

Date: 01 Dec 2025 Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100

FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:

1. This question Paper contains 5 pages.

2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks

4. Question Number | is compulsory.

Out of remaining questions, attempt any 4 questions

6. In all, 5 questions to be attempted

7. All questions carry equal marks

8. Assume suitable data if necessary

Q1 Answer briefly: —s)

CO-1; | a. | For each of the following applications, argue which feature | [04]
SO-1;

level (Low-level, Mid-level, or High-level) is most
BL-5 appropriate. Justify the answer.
(i) Barcode scanner on a retail point-of-sale (POS):
Recognition of edges and parallel lines
(ii) Detection of suspicious activities like theft:

understanding the context, semantics, and temporal
sequence of events.

CO-2; | b. | Why is Rotated BRIEF used instead of BRIEF? For Rotated [04]
Boa BRIEF, rotate a pixel P1 around the key point by 45°, where

coordinates. of P1= (3,5) and calculate new coordinates.
CO-3; | c. | Consider that Imagel has

one keypoint descriptor, Di= |- [04]
SO-1; [0.3, 0.4, 0.6].
BL-2 Image2 has the three keypoints. Corresponding descriptors
are

Dar = [0.2, 0.5, 0.6], Daa = [0.9, 0.1, 0.4], Dz =[0.4, 0.4, 0.5]

(i) Use Brute Force matching to find the best match for D4.
(ii) How many Euclidean distances are to be calculated if
imagel has 2 key points and image2 has 5 key points.
Discuss the stopping conditions in K-means clustering. [04]

CO-4; | d.
S0-4;
BL-2

CO-5; | e. | State and explain two reasons to justify that ‘Faster RCNN’ [04]
SO-5; ;

BL-6 is faster than ‘Fast RCNN’.

Q.2 | a} For Histogram of Gradient (HoG) descriptor, [10]
CO-1;

SO-1;

HRRERERKEE 7 RERERK RHEE
--- page 2 ---
i) Write the steps in brief to determine HoG of an image | i]

and to classify the objects
ii) Consider the following image and gradient filters, Gx
and Gy. Determine Gradient magnitudes and angles

for the highlighted pixels.
iii) Plot 9-bin histogram of gradients.
10 10 10 10 —1 01 ee ool
10 50 50 10 —-2 0 2 0 0 0
10 50 50 10 —1 0 1 1 2 1
101 OPO 10

Image Gx Gy
Q2 b | For Difference of Gaussian (DoG),
ee i) Describe key features of DoG as edge enhancement
BL-3, technique.
. ii) Justify that DoG enhances edges even if image has
noisy pixels. Show with example images. \ AN re”
iii) Consider that an image is filtered by Gaussian \
filters. Filtered images are given below. Calculate
Difference of Gaussian. Locate edge pixels for
threshold = 10.
lol Io2
20 28 32 28 20 24 34 40 34 24
28 48 60 48 28 34 56 72 56 34
=|32 60 80 60 32} | =|40 72 96 72 40
28 48 60 48 28 34 56 72 56 34
20 28 32 28 20 24 34 40 34 24
Image filtered by Gaussian Image filtered by Gaussian
filter with ol = 1 filter with o2 = 2
Q.3 a | Apply Harris corner detection to test whether bold and | [10]
sole underlined pixel is a corner/ edge/flat point. Use window of
BL-3 size 3x3. Given: k = 0.04 and threshold = 10°. If threshold is

increased to 10°, whether the point will be corner/ edge/flat

point?

1 1] 6 | 6 | 6
1 Tradl dG ba aN Oes|bO
Required gradient filters are given below.

HRARERAREEK 2 FREEREE ERE

.
--- page 3 ---
=i OFF =e
G,={-1 0 1], =[0 0 |

aoly =O! OU eee Coa? Me

Q3 b | For the following image
CO-2; (i) Compute the integral image
a (ii) Apply the given filters on the highlighted region of
the integral image to construct its Hessian matrix.
(iii) Using this Hessian matrix, calculate whether the
highlighted point is a key point. (For Hessian matrix,
constant, W = 0.9, and threshold = 10)
1 1 1 1 1 pO Ok 10) 0) 0
1 1 1 1 1 Ig 7) bet aL ©
1 ] 2 2 2 TE es 7) eri =u
fen |e | oe |e 0 0 0 00
image
Gy ro One 0) 05.40
Ohne ties} 1-210)
ee ee eee A 0)..0,,,
er i ale Sea eer
=10 -—2 -2 -2 0 10 0 00 0
(Ng 1 I
(O)pemal 1 a Ls (0)
Q4 a | For Scale-Invariant Feature Transform (SIFT), [10]
CO-2; i) List and explain the steps to determine the SIFT
Fi a descriptor in brief. Write the role of each step.
ii) Illustrate key point orientation assignment in details.
Q4 b | For Fast Library for Approximate Nearest Neighbors
CO-3; (leq ABex
SO-1: (FLANN),
BL-3,5

(i) Construct a K-D tree for the following 3-dimensional

descriptors of Image 1.

FRKEEHKEERE QOFKEEEKE EEE
--- page 4 ---
i Descriptors: (3, 1, 4), (@, 2, 5). 2; 3, 7), (2, 1, 3), (2, 4;
5), (1, 4, 4), G, 2, 1), (0, 5, 7), (4, 3, 4), (6, 1,4). G, 2,
5), (5, 3, 6), (4, 0, 6), (4, 1, 2), (7: 1, 6), (7, 0, 5).

(ii) Choose a match for the descriptor (7, 1, 7) of Image 2

Q5 a | Describe steps for descriptor matching using Bag of Visual | [10]
oe Words. Explain it with example images.
| BL-5 Explain why Bag of Visual words method is preferred over
pair wise feature matching?
Q5 b | For segmentation of images, [10]

CO-4; (i) List the limitations of K-Means algorithm and Mean shift

SO-2; algorithm.

BL-6 (ii) The following dataset contains pixels of color image.
Apply K-means clustering with K=3 clusters for one
iteration. Points are
e Pl=[255,0,0]

e P2=(0, 255, 50]
e p3=(0, 0, 255]
e P4=(250, 10, 10]
Initial centroids are - C1=P1=[255,0,0], C2=P3=
{0,0,255]

(iii) Calculate updated values of centroids

Q6 a | Using the Lucas-Kanade optical flow method, 10

CO-5; (i) Derive the mathematical relationship used to determine

SO-4; the velocity vector of a moving object in an image

BL-3 sequence.

(ii) State and explain the assumptions made in this
derivation. discuss why these assumptions are
necessary, and how they can be addressed or relaxed
when they are not satisfied.

Q6 b | Design an appropriate Convolutional Neural Network >

ete : (CNN) model with the following architecture specifications Yes ~~

BL-6 for an input RGB image of size 32 x 32 for 10 classes

« One convolutional layer with 32 filters, each of size
3x3

* One max pooling layer with pool size (2x2)
* One dropout layer with probability 0.2

. One flatten layer

« Two dense (fully connected) layers

« No padding (i-e., "valid" convolution)

e Stride = 1 for convolution

HRKKKAKEEK A ERKEKEKEEKE
--- page 5 ---
i) Draw architecture and show the shape of output after
each layer. Do not consider bias terms at any layer.

li) Specify activation functions for the layers

Q7 a |For Region based Convolutional Network (RCNN),

CO-5; i) Draw architecture and write the role of each step ok ah
SO-4; ii) Explain selective search algorithm in details

BL-3

Q7 b | For Single Shot Detector, justify the use of multiple boxes

CO-5; to detect object of different scale. Explain with suitable Ned ger
SO-4; diagrams.

BL-3

--- page 6 ---

````

## 2025-26 · Final-Exam · Sem 7 · paper 3c880f9c355a

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AIML_7053/COMPUTER VISION FOR AI/QP_COMPUTER VISION FOR AI(702AI0C029)_2025-2026_3c880f9c35.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all, 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q1   Answer briefly:
CO-1;   a. For each of the following applications, argue which feature   [04]
SO-1;   level (Low-level, Mid-level, or High-level)   is most
BL-5   appropriate. Justify the answer.
(i) Barcode scanner on a retail point-of-sale (POS):
Recognition of edges and parallel lines
(ii) Detection   of   suspicious   activities   like   theft:
understanding the context, semantics, and temporal
sequence of events.
CO-2;   b. Why is Rotated BRIEF used instead of BRIEF? For Rotated [04]
SO-1;
BRIEF, rotate a pixel P1 around the key point by 45°, where
BL-3
coordinates of P1= (3,5) and calculate new coordinates.
CO-3;   c. Consider that Image1 has one keypoint descriptor, D1=   [04]
SO-1;   [0.3, 0.4, 0.6].
BL-2   Image2 has the three keypoints. Corresponding descriptors
are
D21 = [0.2, 0.5, 0.6], D22 = [0.9, 0.1, 0.4], D23 = [0.4, 0.4, 0.5]
(i) Use Brute Force matching to find the best match for D1.
(ii) How many Euclidean distances are to be calculated if
image1 has 2 key points and image2 has 5 key points.
CO-4;   d. Discuss the stopping conditions in K-means clustering.   [04]
SO-4;
BL-2
CO-5;   e.   State and explain two reasons to justify that ‘Faster RCNN’   [04]
SO-5;
is faster than ‘Fast RCNN’.
BL-6
Q. 2   a   For Histogram of Gradient (HoG) descriptor,   [10]
CO-1;
SO-1;
********** 1 **********
--- page 2 ---
BL-3   i) Write the steps in brief to determine HoG of an image
and to classify the objects
ii) Consider the following image and gradient filters, Gx
and Gy. Determine Gradient magnitudes and angles
for the highlighted pixels.
iii) Plot 9-bin histogram of gradients.
10 10 10 10   −1 0 1   −1 −2 −1
10 𝟓𝟎 𝟓𝟎 10   [ −2 0 2 ]   [ 0   0   0 ]
[
10 𝟓𝟎 𝟓𝟎 10   −1 0 1   1   2   1
10 10 10 10
Image   Gx   Gy
Q2   b For Difference of Gaussian (DoG),
CO-1;
i) Describe key features of DoG as edge enhancement
SO-1;
BL-3,   technique.
5
ii) Justify that DoG enhances edges even if image has
noisy pixels. Show with example images.
iii) Consider that an image is filtered by Gaussian
filters. Filtered images are given below. Calculate
Difference of Gaussian. Locate edge pixels for
threshold = 10.
Iσ1   Iσ2
20 28 32 28 20   24 34 40 34 24
28 48 60 48 28   34 56 72 56 34
= 32 60 80 60 32 = 40 72 96 72 40
28 48 60 48 28   34 56 72 56 34
[ 20 28 32 28 20]   [ 24 34 40 34 24]
Image filtered by Gaussian   Image filtered by Gaussian
filter with σ1 = 1   filter with σ2 = 2
Q. 3   a Apply Harris corner detection to test whether bold and   [10]
CO-2;
underlined pixel is a corner/ edge/flat point. Use window of
SO-1;
BL-3   size 3×3. Given: k = 0.04 and threshold = 105. If threshold is
increased to 106, whether the point will be corner/ edge/flat
point?
1   1   1   1   1
1   1   1   1   1
1   1   6   6   6
1   1   6   6   6
1   1   6   6   6
Required gradient filters are given below.
********** 2 **********
--- page 3 ---
−1 0 1   −1 −1 −1
𝐺𝑥= [ −1 0 1 ] ,   𝐺𝑦= [ 0   0   0 ]
−1 0 1   1   1   1
Q3   b For the following image
CO-2;   (i)   Compute the integral image
SO-1;
(ii)   Apply the given filters on the highlighted region of
BL-4
the integral image to construct its Hessian matrix.
(iii)   Using this Hessian matrix, calculate whether the
highlighted point is a key point. (For Hessian matrix,
constant, W = 0.9, and threshold = 10)
1   1   1   1   1   0 0 0 0 0
1   1   1   1   1   1 1 −2 1 1
1   1   2   2   2   𝐺𝑥= 1 1 −2 1 1
1   1   2   2   2   1 1 −2 1 1
1   1   2   2   2   [ 0 0 0 0 0]
image
𝐺𝑦   0 0 0   0 0
0 1 0 −1 0
0   1   1   1 0   𝐺𝑥𝑦= 0 0 0   0 0
0   1   1   1 0   0 −1 0   1 0
= 0 −2 −2 −2 0   [ 0 0 0   0   0]
0   1   1   1 0
[ 0   1   1   1   0]
Q4   a For Scale-Invariant Feature Transform (SIFT),   [10]
CO-2;   i) List and explain the steps to determine the SIFT
SO-5;
descriptor in brief. Write the role of each step.
BL-3,4
ii) Illustrate key point orientation assignment in details.
Q4   b   For Fast Library for Approximate Nearest Neighbors
CO-3;
(FLANN),
SO-1;
BL-3,5   (i) Construct a K-D tree for the following 3-dimensional
descriptors of Image 1.
********** 3 **********
--- page 4 ---
Descriptors: (3, 1, 4), (3, 2, 5), (2, 3, 7), (2, 1, 3), (2, 4,
5), (1, 4, 4), (1, 2, 1), (0, 5, 7), (4, 3, 4), (6, 1, 4), (5, 2,
5), (5, 3, 6), (4, 0, 6), (4, 1, 2), (7, 1, 6), (7, 0, 5).
(ii) Choose a match for the descriptor (7, 1, 7) of Image 2
Q5   a Describe steps for descriptor matching using Bag of Visual   [10]
CO-3;
Words. Explain it with example images.
SO-1;
BL-5   Explain why Bag of Visual words method is preferred over
pair wise feature matching?
Q5   b For segmentation of images,   [10]
CO-4;   (i) List the limitations of K-Means algorithm and Mean shift
SO-2;   algorithm.
BL-6
(ii) The following dataset contains pixels of color image.
Apply K-means clustering with K=3 clusters for one
iteration. Points are
• P1=[255,0,0]
• P2=[0,  255,  50]
• P3=[0,  0,  255]
• P4=[250,  10,  10]
Initial centroids are   - C1=P1=[255,0,0], C2=P3=
[0,0,255]
(iii) Calculate updated values of centroids
Q 6   a   Using the Lucas–Kanade optical flow method,   10
CO-5;   (i) Derive the mathematical relationship used to determine
SO-4;   the velocity vector of a moving object in an image
BL-3   sequence.
(ii) State and explain the assumptions made in this
derivation.   discuss why these assumptions are
necessary, and how they can be addressed or relaxed
when they are not satisfied.
Q 6   b   Design an appropriate Convolutional Neural Network
CO-5;
(CNN) model with the following architecture specifications
SO-1;
BL-6   for an input RGB image of size 32 × 32 for 10 classes
• One convolutional layer with 32 filters, each of size
3×3
• One max pooling layer with pool size (2×2)
• One dropout layer with probability 0.2
• One flatten layer
• Two dense (fully connected) layers
• No padding (i.e., "valid" convolution)
•   Stride = 1 for convolution
********** 4 **********
--- page 5 ---
i) Draw architecture and show the shape of output after
each layer. Do not consider bias terms at any layer.
ii) Specify activation functions for the layers
Q 7   a   For Region based Convolutional Network (RCNN),
CO-5;   i) Draw architecture and write the role of each step
SO-4;   ii) Explain selective search algorithm in details
BL-3
Q 7   b   For Single Shot Detector, justify the use of multiple boxes
CO-5;   to detect object of different scale. Explain with suitable
SO-4;   diagrams.
BL-3
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 7 · paper 8080bf82f97f

- Departments: Data Science
- Programmes: BTech CSE DS 7011, BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSE_DS_7011/COMPUTER VISION/QP_COMPUTER VISION(702EX0E015)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Nov 2025
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: COMPUTER VISION
Date: 29 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions,attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1   Answer briefly   [20]
a. A computer vision system for a warehouse robot that navigates to reads
labels on packages is to be developed. Which type of technique (low-
level, mid-level, high-level) would be most appropriate to identify the
labels for the following
CO-1
SO-2   [04]
i) Determine the features of labels and match it with the product label.
BL-2
ii) To interpret the text on a package label (e.g., destination or product
ID) and understand the type of product using deep learning.
Justify answer using the steps involved
b. For Scale-Invariant Feature Transform (SIFT) algorithm, a point has
Ixx=6, Iyy = 4, Ixy = 1, where, Ixx and Iyy are second order derivatives in
x and y directions respectively and Ixy is first order derivative in x
CO-2
direction of derivative in y direction.   [04]
SO-1
BL-3,6
Construct Hessian matrix and test whether the given the given point is
a keypoint or not. For SIFT, r = 10
c. How does FLANN use KD-Trees to accelerate nearest neighbor
CO-2   searches in high-dimensional feature matching?
SO-1   Construct a KD-Tree for the following 2D points (split alternately on   [04]
BL-3   x and y):
𝑃1 = (3,6), 𝑃2 = (17,15), 𝑃3 = (13,15),𝑃4 = (6,12),𝑃5 = (9,1)
d.   i) Write purpose of the Fully Connected (FC) layer in a Convolutional
CO-2
SO-5   Neural Network (CNN)?   [04]
ii) Explain with the help of a simple diagram showing how the feature
BL-3
map is flattened and connected to the output neurons.
CO- 4   e.   List and justify any two limitations of Region based Convolutional
SO- 5   [04]
Neural Network.
BL- 5
Q2   a   For SIFT (Scale-Invariant Feature Transform) algorithm,
********** 1 **********
--- page 2 ---
CO-3   i) Briefly describe the role of each step in 2-3 sentences.   [10]
SO-2
ii) Explain scale space generation in details using an example image
BL-3
of size M×N. Assume initial value of standard deviation =1.6.
Sketch images and standard deviations at each stage.
b   For Histogram of gradients,
i) Gradient magnitude and angles of a cell are given below. Plot
histogram of gradient for 9-bin histogram.
40   100   20   80   0   10   30   55
40   100   20   80   0   10   30   55
Q2
40   100   20   80   0   10   30   55
CO-1   [10]
SO-1   40   100   20   80   0   10   30   55
BL-3
Magnitude   Angle
ii) Show how length of HoG vector for an image of size 64×128 is
determined if 8 pixels per cell and number of 4 cells per block
are given.
a   Consider the following 9×9 integral image.
i) Filter the image at the center with the given 9×9 filter. Use
integral image.
ii) How many additions, subtractions and multiplications are used
for this computation?
Q3   iii) Compare SIFT and SURF descriptors
CO-2   0   0   0   0   0   1   2   3   4   [10]
SO-4   0   0   0   0   0   2   4   6   8
BL-4, 5   0   0   0   0   0   3   6   9   12
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
Integral image
********** 2 **********
--- page 3 ---
Filter
Q3   b   Describe Binary Robust Independent Elementary Features (BRIEF)
CO- 2   descriptor in details. Use examples to explain GII and GIII approaches   [10]
SO- 4
BL- 3   to choose pair of pixels.
a An image retrieval system for a fashion e-commerce website is to be
developed. Each image is represented by a feature vector extracted
using SIFT.
Q4   (i) Explain how cosine similarity is used to compare two image feature
vectors. Explain with examples.
CO-2   (ii) Feature vectors extracted from images:   [10]
SO-4
BL-3   𝐹1 = [1,2,3],𝐹2 = [2,1,3],𝐹3 = [0,1,1]
Feature vector to be matched is Q = [1,1,2]. Compute the cosine
similarity between Q and each feature vector to identify the best
match.
b
For Bag of Visual Words (BoVW) model
(i)   Write the steps for matching SIFT or ORB descriptors.
(ii)   Consider 6 images and 5 visual words. Calculate TF-IDF (Term
Q4   Frequency Inverse Document Frequency) on histogram of image
A and image B and plot it.
CO-2   Image A: [2, 1, 0, 1, 1]   [10]
SO-1
Image B: [0, 2, 1, 1, 0]
BL-4
Image C: [1, 0, 1, 0, 2]
Image D: [0, 1, 0, 2, 1]
Image E: [1, 1, 0, 0, 0]
Image F: [0, 0, 1, 1, 0]
a   For a pedestrian tracking system for autonomous vehicles, the system
captures consecutive video frames.
Q5   (i)   Describe how the Lucas–Kanade method estimates optical flow
for a small window of pixels.
CO-2   (ii)   Write a real-world scenario where sparse optical flow is   [10]
SO- 4
preferred over dense optical flow.
BL- 3
(iii)   For a 2×2 window, the image derivatives are:
𝐼𝑥= [3,1],𝐼𝑦= [1,2],𝐼𝑡= [−2, −1]
********** 3 **********
--- page 4 ---
Calculate optical flow vectors for the window.
b   For the given color image,
(i)   Apply K-Means clustering for K=2 using Euclidean
distance. Initialize centroids as C1 = (12,20,30), C2 =
Q5   (200,210,220)
CO-2   (ii)   Assign clusters to each pixel and updated centroid for one
[10]
SO-4   iteration.
BL-1,4
(iii)   Comment on how K-Means reduces the color palette
(labels) in images
(10, 20, 30)   (12,18, 28)   (200, 210, 220)
(11, 21, 29)   (15, 22, 32)   (198, 208, 218)
(14, 19, 31)   (13, 31, 30)   (201, 212, 221)
a   In relation to 3D model, write in brief about
Q6
(i)   camera model
CO-3   [10]
SO-1   (ii)   Intrinsic matrix
BL-3
(iii)   Extrinsic matrix
Q6   b
In relation to stereo vision, explain Epipolar constraints to determine
CO-3   [10]
SO-2   essential matrix.
BL-3
Q7   a
Draw architecture of Fast RCNN and explain each layer/block in 2-3
CO-4   [10]
SO-5   sentences in brief.
BL-4
b   In relation to RCNN, justify that
Q7
i) RCNN is slow
CO-4   [10]
SO- 5   ii) Fast RCNN is faster than RCNN
BL-6
iii) Faster RCNN is faster than Fast RCNN
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 7 · paper 49edd36dc938

- Departments: Artificial Intelligence
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE, MBA TECH / Artificial Intelligence
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/ARTIFICIAL INTELLIGENCE/SEM-VII/COMPUTER VISION FOR AI/Computer Vision for AI, Sem-VII, Year 2025-26, Final Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: ocr (5 pages), mean OCR confidence 86.6

````text
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI .
Date: 01 Dec 2025 Time: 10:00 am to 01:00.pm (03:00 Hrs.)
Max. Marks: 100

FINAL EXAMINATION (Acad. Year:2025-2026)

Instructions:

1. This question paper contains 5 pages.

2. Answer to each new question td be started on a fresh page.

3. Figure in right hand side indicates full marks

4. Question Number | is compulsory.

5. Out of remaining questions, attempt any 4 questions

6. In all, 5 questions to be attempted

7. All- questions carry equal marks

8. Assume suitable data if necessary

Ql Answer briefly:

CO-1; | a. | For each of the following applications, argue which feature | [04]
SO-1; level (Low-level, Mid-level, or- High-level) is most
BL-5 appropriate. Justify the answer.
(i) Barcode scanner on a retail point-of-sale (POS):
Recognition of edges and parallel lines
(ii) Detection of suspicious activities like theft:
understanding the context, semantics, and temporal
sequence of events.

CO-2; | b. | Why is Rotated BRIEF used instead of BRIEF? For Rotated | [04]
BRIEF, rotate a pixel P1 around the key point by 45°, where | ~

coordinates of P1= (3,5) and calculate new coordinates.

CO-3; | c. | Consider that Imagel has one keypoint descriptor, Di= |. [04]

SO-1; [0.3, 0.4, 0.6].
BL-2 Image2 has the three keypoints. Corresponding descriptors
are

Dai = [0.2, 0.5, 0.6], Do2 = [0.9, 0.1, 0.4], D23 = [0.4, 0.4, 0.5]

(i) Use Brute Force matching to find the best match for D1.
(ii) How many Euclidean distances are to be calculated if
imagel has 2 key points and image2 has 5 key points.

CO-4; | d. | Discuss the stopping conditions in K-means clustering. [04]
SO-4;
BL-2

CO-S5; | e. | State and explain two reasons to justify that ‘Faster RCNN’ | [04]

te ‘| is faster than ‘Fast RCNN’. ‘ ©

Q.2 a | For Histogram of Gradient (HoG) descriptor, [10]
CO-1;
SO-1;

FR 7 Gok
--- page 2 ---
BL-3 i) Write the steps in brief to determine HoG of an image
and to classify the objects
ii) Consider the following image and gradient filters, Gx
and Gy. Determine Gradient magnitudes and angles J
for the highlighted pixels.
ili) Plot 9-bin histogram of gradients.

10 10 10 10 -2 0 4 fo —2 °|

10 50 50 10. |-2 0 2 0 0 0
10 50 50 10 -1 0 1 1 2 1
10 10 10 10

Image Gx Gy

Q2 b | For Difference of Gaussian (DoG),
CO-1;

>

SO-1: i) Describe key features of DoG as edge enhancement
BL-3, technique.

a
° ii) Justify that DoG enhances edges even if image has

noisy pixels. Show with example images. ; oy we
iii) Consider that an image is filtered by Gaussian |
filters. Filtered images are given below. Calculate

Difference of Gaussian. Locate edge pixels for
threshold = 10.

Io1 Io2

20 28 32 28 20 24 34 40 34 24

28 48 60 48 28 34 56 72 56 34
=|/32 60 80 60 32]|=/40 72 96 72 40

28 48 60 48 28 34 56 72 56 34
20 28 32 28 20 24 34 40 34 24

Image filtered by Gaussian | Image filtered by Gaussian
filter with ol = 1 filter with 62 = 2

Q.3 a | Apply Harris corner detection to test whether bold and [10]

roe underlined pixel is a corner/ edge/flat point. Use window of

BL-3 size 3x3. Given: k = 0.04 and threshold = 10°. If threshold is
increased to 10°, whether the point will be corner/ edge/flat

point?

1 I 1 1 1

1 alta ae | 1

|e aa a Ps er 6

1 6 tle 6 6

. 1 1 6 6 6
Required gradient filters are given below.

FRR DKK

4 .
--- page 3 ---
—-1 0 1 -1 -1i -1
G,=j-1 0 1), G=|0 0 0
“1 0 FT 1 i 1
sd it
Q3 b | For the following image
CO-2; (i) Compute the integral image
ae (ii) | Apply the given filters on the highlighted region of
a= the integral image to construct its Hessian matrix.
(iii) | Using this Hessian matrix, calculate whether the
highlighted point is a key point. (For Hessian matrix,
constant, W = 0.9, and threshold = 10)
1 1 1 1 1 00 0 0 0
1 1] 1 1 1 11-2 1 1 ©
1 1 2 | 2 3 G,=]1 1 -2 1 1 (PS HB
1 1 2 2 2 11-2 1 «421
1 1 2 2 2 00 0 0 0
image
Gy 0 0 0 0 0
0 1 0 -1 0
or 1 1% @=l0 0 0 oO O
0 1 1 1 0
0 -1 0 1 =+0
=|0 -2 -2 -2 0 00 0 0 0
> o t 1 1 20
Oo 1 1 1 «0 .
Q4 a | For Scale-Invariant Feature Transform (SIFT), [10]
CO-2; i) List and explain the steps to determine the SIFT
SO-5; . . . .
BL-3,4 descriptor in brief. Write the role of each step.
ii) Illustrate key point orientation assignment in details.
i Q4 b | For Fast Library for Approximate Nearest Neighbors
CO-3; Cie] AB e—
= SO-1: (FLANN),
BL-3,5 | . | (i) Construct a K-D tree for the following 3-dimensional
, 4 descriptors of Image 1. ,

ARR A ARK SE
--- page 4 ---
Descriptors: (3, 1, 4), (3, 2, 5), (2, 3, 7), (2, 1, 3), (2, 4,
5), 1, 4,4), (1, 2, D, 0, 5; 7), (4, 3, 4), (6, 1, 4), GS, 2,
5), G, 3, 6), (4, 0, 6), (4, 1, 2), (7, 1, 6), (7, 0, 5).

(ii) Choose a match for the descriptor (7, 1, 7) of Image 2 a: 2
Q5 a | Describe steps for descriptor matching using Bag of Visual [10]
co Words. Explain it with example images.
BL-5 Explain why Bag of Visual words method is preferred over
pair wise feature matching? ~
Q5 b | For segmentation of images, [10]
CO-4; (i) List the limitations of K-Means algorithm and Mean shift
SO-2; algorithm.
BL-6 (ii) The following dataset contains pixels of color image.
Apply K-means clustering with K=3 clusters for one
iteration. Points are
e P1=[255,0,0]
e P2=[0, 255, 50]
e P3=[0, 0, 255] 7
e P4=[250, 10, 10]
Initial centroids are - Cl=P1=[255,0,0], C2=P3=
[0,0,255]
(aii) Calculate updated values of centroids
Q6 a ‘| Using the Lucas—Kanade optical flow method, 10
CO-5; (i) Derive the mathematical relationship used to determine
SO-4; the velocity vector of a moving object in an image
BL-3 sequence.
(ii) State and explain the assumptions made in this
derivation. discuss why these assumptions are
necessary, and how they can be addressed or relaxed
when they are not satisfied.
Q6 b | Design an appropriate Convolutional Neural Network
Sot 2 (CNN) model with the following architecture specifications \e \o\ ae
BL-6 for an input RGB image of size 32 x 32 for 10 classes

e¢ One convolutional layer with 32 filters, each of size
3x3

¢ One max pooling layer with pool size (2x2)

e One dropout layer with probability 0.2

e One flatten layer

¢ Two dense (fully connected) layers

e No padding (i.e., "valid" coavolution)

e Stride = 1 for convolution

FO GR oR
--- page 5 ---
i) Draw architecture and show the shape of output after
each layer. Do not consider bias terms at any layer.

ii) Specify activation functions for the layers

Q7 a | For Region based Convolutional Network (RCNN), _ a7
CO-5; i) Draw architecture and write the role of each step ek yw

SO-4; ii) Explain selective search algorithm in details

BL-3

Q7 b | For Single Shot Detector, justify the use of multiple boxes .
CO-5; to detect object of different scale. Explain with suitable Degen
SO-4; diagrams. .
BL-3

FOCI OR a
````

## 2025-26 · Re-Exam · Sem 12 · paper b65e6b1fd15a

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2024/Sem_12/Re-Exam/Integrated_Computer_7032/Computer Vision/QP_Computer Vision(702AI0C017)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech Intg. (CE)
Year: III / VI/Semester VI/Semester XII(Exam Year: 2025-2026)
Subject: Computer Vision
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 2 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 4   a   In relation to epipolar geometry, explain epipolar constraint. Show how it
SO- 1,6   [05]
BL- 2   useful in matching key points.
CO- 3   b.   Explain in brief any two advantages and two limitations of the K-Means
SO- 1,6   [05]
algorithm.
BL- 5
c.   Determine the integral image for the following image.
CO- 2
SO- 1,6   [05]
BL- 4
CO- 4   d.
SO- 1,6   Explain two examples of mid-level processing.   [05]
BL- 3
a   Given the following gradient magnitude and orientation matrices, compute
the histogram of oriented gradients using 9 bins (0–180°). Determine the
HOG feature vector for the 4×4 image.
Q2
CO- 1
SO- 1, 6   [10]
BL- 5
Gradient Magnitude   Gradient orientation (Ɵ)
b   For Harris corner detector,
Q2   i) Show with example images that Harris corner detector is invariant
CO- 1   to rotation and variant to scaling   [10]
SO- 1, 6   ii) Explain the steps involved in constructing Harris matrix and using
BL- 5   corner response to determine whether the pixel is corner, edge or
flat region.
********** 1 **********
--- page 2 ---
a
Q3
CO- 2   List the steps for extracting Scale-Invariant Feature Transform (SIFT)   [10]
SO- 1, 6   features from an image, and describe key point localization in detail.
BL- 5
Q3   b
For Speeded-Up Robust Features (SURF), explain the scale space
CO- 2   generation for feature detection and justify in brief that it is computationally   [10]
SO- 1, 6
BL- 1,5   efficient.
a   Explain the Mean Shift clustering algorithm with reference to the
Q4   following aspects:
i) The working procedure of the algorithm and criteria for convergence
CO- 3   ii) Effect of large and small bandwidth   [10]
SO- 1, 6
iii) The advantages and limitations of Mean Shift
BL- 2
Support your explanation with a suitable example plots of data points
Q4   b
CO- 3   Describe how Gaussian Mixture model is used to generate background   [10]
SO- 1,6   model.
BL- 5
Q5   a
Show the concept of optical flow. Compare dense and sparse optical flow
CO- 3   [10]
SO- 1,6   with suitable example images.
BL- 4
Q5   b
CO- 3   Describe how background frame is generated using temporal average. Also   [10]
SO- 1,6   show how background subtraction is used generate foreground of the image.
BL- 5
Q6   a
Explain any five challenges of implementing a cereal grain inspection
CO- 4   [10]
SO- 1,6   system using computer vision.
BL- 2
Q6   b   Show how 2D Cartesian coordinates are converted to 3D homogeneous
CO- 4   coordinates and vice versa. Convert the point (3,4) from Cartesian to   [10]
SO- 1,6   homogeneous form. Also, determine the corresponding 2D Cartesian
BL- 5   coordinates for the homogeneous point (9,12,3).
a   Explain in brief the following:
Q7   • World coordinate system
CO- 4   • Camera coordinate system   [10]
SO- 1, 6
BL- 3   • Image coordinate system
•   Pixel coordinate system
Q7   b
Draw a labeled sketch of epipolar geometry and explain it with reference to
CO- 4   [10]
SO- 1,6   points, epipolar lines, and the essential and fundamental matrices.
BL- 3
********** 2 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper 96ca07e11459

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_AIDS_7056/COMPUTER VISION FOR AI/QP_COMPUTER VISION FOR AI(702AI0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI
Date: 01 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Use of Scientific calculator is allowed.
Q1   Answer briefly:   [20]
CO- 2   a. Given:   [05]
SO- 1   Sxx=12, Syy=9, Sxy=5, k=0.05
BL- 2,3
Compute Harris response (R). Classify the feature type (e.g., flat region, edge,
or corner) by analyzing the relationship between the determinant and the trace
of the second-moment matrix.
CO- 3   b. Two feature descriptors are given: A= (2,3,1), B= (4,6,2)   [05]
SO-1   i.   Compute cosine similarity between A and B.
BL-3   ii.   Comment whether they are good matching key points or not.
CO- 4   c.   In the context of Mean Shift image segmentation, consider a 1D feature space   [05]
SO- 1   with the following pixel intensity values: X = {5, 15, 18, 24, 27, 30, 35}. If the
BL-2,3   algorithm starts at an initial estimate y1 = 20 with a bandwidth = 6.
i. Define the set of points that fall within the kernel window.
ii. Calculate the mean shift vector and the resulting new center y2
CO- 5   d. Explain the primary purpose of the Convolutional Layer in a CNN. Describe the   [05]
SO- 1,6   role of "filters" (or kernels) and how they produce a feature map.
BL- 1,3
Q2   a   Computer Vision systems are often designed in hierarchical stages: low-level,
CO- 1   mid-level, and high-level processing.   [10]
SO- 1
BL-2,3   i.   Explain the roles of low-level, mid-level, and high-level vision tasks in a
Computer Vision pipeline.
ii.   Consider an application of autonomous driving. Demonstrate how each
level of vision (low, mid, high) is applied to process visual data and make
decisions.
iii.   Illustrate how improper functioning of any one level can affect the overall
performance of the system.
Q2   b A grayscale image patch (3×3) is given:   [10]
CO- 1   10 20 10
SO- 1   𝐼= [ 20 40 20 ]
10 20 10
********** 1 **********
--- page 2 ---
BL- 3   0 1   0
i.   Using Laplacian kernel: [ 1 −4 1 ] Compute the LoG response at
0 1   0
the center pixel.
ii.   Given Gaussian responses at two scales: Gσ1=35, Gσ2=25. Compute
DoG and interpret whether it indicates a strong feature or not.
−1 0 1   −1 −2 −1
iii.   Using Sobel operators: 𝐺𝑥= [ −2 0 2 ] 𝐺𝑦= [ 0   0   0 ]
−1 0 1   1   2   1
Compute gradient magnitude and gradient direction
iv.   Assign the gradient to one of the Histogram of Gradient (HoG) bins:
Bins: 00, 450, 900, 1350
Q3   a   Consider the below image.   [10]
CO- 2
SO- 1
BL- 2,3
i.   Compute integral image
ii.   Justify that an integral image enables fast computation of filtered image
in algorithms like SURF. Explain with an example.
Q3   b The Scale Invariant Feature Transform (SIFT) is widely used for detecting and   [10]
CO- 2   describing local features in images.
SO- 1   i.   Analyze the role of scale-space representation using Difference of
BL-2,3   Gaussian (DoG) in detecting stable keypoints across different image
scales.
ii.   Examine how keypoint localization improves the stability and accuracy
of detected features.
iii.   Analyze how orientation assignment ensures rotation invariance in SIFT.
iv.   Evaluate why SIFT descriptors are more robust compared to simple edge
or corner-based features in real-world image matching applications.
Q4   a   Given 3 images with histogram of visual words:   [10]
CO- 3   H1 = [4,2,0,1],   H2 = [2,1,3,0],   H3 = [1,2,1,2]
SO- 2   Query image: Q = [3,1,1,1]
i.   Compute TF for each histogram
BL-
ii.   Compute DF and IDF
3,4,5   iii.   Compute TF-IDF for query
iv.   Compute the Euclidean distance between the TF-IDF vector of the query
image and TF vector of each image. Identify the best match.
Q4   b   In an image matching system, a set of keypoint descriptors from two images are   [10]
CO- 3   compared using nearest neighbor matching followed by a ratio test. A descriptor
SO- 2   in Image A has the following Euclidean distances to its nearest neighbors in
Image B:
BL-3,4,5
• Best match distance = 0.42
• Second-best match distance = 0.50
Threshold T=0.75
********** 2 **********
--- page 3 ---
i.   Compute the ratio value and determine whether the match should be
accepted or rejected.
ii.   Explain how the ratio test helps in improving the reliability of feature
matching in real-world applications.
Q5   a   I. You have deployed a background subtraction system on a static traffic camera   [10]
CO- 4   to count cars passing through an intersection. On a calm, overcast day, it works
SO- 1   with 99% accuracy. However, on a sunny, windy day with fast-moving clouds,
the system starts generating hundreds of false positives, flagging empty stretches
BL-
of road and the sides of the street as "moving vehicles."
3,4,5
What two specific environmental factors are breaking your basic background
subtraction model, and what advanced background modeling technique should
you implement to fix this?
II. Explain two fundamental limitations of standard optical flow methods.
Q5   b   Consider a 5 × 5grayscale image whose pixel intensity values are given by   [10]
CO- 4   10 12 15 14 10
SO- 1   11 25 26 24 12
𝐼= 14 28 30 29 15
BL-3,4,5
12 27 26 25 13
[ 10 11 14 12 10]
Assume that pixel coordinates are indexed using 0-based indexing in the form
(row, column).
The pixel located at position (2,2), which is the center of the image and has an
intensity value of 30, is selected as the initial point for the mean shift algorithm.
Let the spatial bandwidth be 𝑆= 1, where distance is measured using the
Chebyshev (chessboard) distance, resulting in a 3 × 3 spatial neighborhood. The
color (intensity) bandwidth is given as ℎ𝑐= 5.
Perform one iteration of the mean shift algorithm and determine:
i.   The spatial neighbourhood of the pixel (2,2).
ii.   The pixels within this neighbourhood that satisfy the color (intensity)
bandwidth condition.
iii.   The mean intensity of the selected pixels.
iv.   The new spatial location of the pixel after the mean shift update.
Q6   a   I. An image retrieval system uses Pyramid Feature Matching to rank results. For   [10]
CO- 2,3   a specific query, the system returns the following intersection scores:
SO- 1   Level 0 = 0.90 and Level 1 = 0.98. Calculate the similarity score using
Weight Set : {w0 = 1, w1 = 0.5}.
BL-3,4,5
II. A pixel inside a Histogram of Oriented Gradients (HoG) cell has a gradient
magnitude of 32 and a gradient orientation of 73°. The HoG descriptor uses 9
orientation bins spanning an unsigned range of 0° to 180°, resulting in a bin width
of 20°. The bin boundaries start at 0°. Assuming that the orientation interpolation
is performed strictly between the bin boundary angles of 60° and 80° (not the bin
centres):
i.   Identify the two adjacent histogram bins to which this pixel contributes.
ii.   Calculate the interpolation weights for each bin.
iii.   Determine how the gradient magnitude is distributed between these two
bins.
********** 3 **********
--- page 4 ---
Q6   b A CNN architecture is defined as follows:   [10]
CO- 5   •   Input Image: 64 x 64 x 3 (RGB image)
SO- 2   • Layer 1: Conv1
o Kernel size: 5 x 5
BL-3,4
o Number of filters: 16
o   Stride: 1
o Padding: 2 (Same convolution)
• Layer 2: MaxPool1
o Kernel size: 2 x 2
o   Stride: 2
• Layer 3: Conv2
o Kernel size: 3 x 3
o Number of filters: 32
o   Stride: 1
o Padding: 0 (Valid convolution)
• Layer 4: FC1 (Fully Connected Layer)
o Input: Flattened output of Conv2
o Output nodes: 128
• Output Layer
o Softmax layer
o Input: 128 units
o Output: 5 classes
Tasks:
i. Compute the output feature map size after each layer.
ii. Compute the number of parameters after each layer.
Q7   a   i.   Identify the two major computational bottlenecks of the original R-CNN   [10]
CO- 5   architecture.
SO- 2   ii.   Explain how Fast R-CNN specifically solved these bottlenecks to achieve
faster training and inference.
BL-4,5
iii.   Identify the remaining bottleneck in Fast R-CNN and explain how Faster
R-CNN eliminated it to achieve true "real-time" or near-real-time object
detection.
Q7   b A MedTech company is developing an autonomous microsurgical robot designed   [10]
CO- 5   to assist in the removal of brain tumors (glioblastomas) using a laser scalpel. The
SO- 2,6   robot's vision system must identify the tumor in real-time MRI feeds and outline
its exact boundaries to ensure the laser vaporizes the cancer cells without
BL-3,4,5
destroying the adjacent healthy brain tissue.
i. In neurosurgery, a sub-millimeter spatial misalignment (translating to just a
few pixels) can cause the laser to damage critical healthy neurons. Explain how
RoIAlign prevents the "quantization" (rounding) errors inherent in standard
RoIPool, preserving the sub-pixel accuracy required for this delicate procedure.
ii. To achieve ultra-fast, real-time tracking of the brain during surgery, the
engineering team suggests using a standard YOLO model instead of Mask R-
CNN. However, YOLO outputs object "bounding boxes" (rectangles) rather than
pixel-perfect masks. Explain why feeding a bounding box to the laser scalpel
instead of a precise segmentation mask would result in severe damage to the
patient.
iii. The final medical imaging system utilizes an "encoder-decoder" architecture
(like U-Net or SegNet). Briefly explain what the encoder does to the input MRI
image, and what the decoder does to reconstruct the precise spatial shape of the
tumor.
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper 0f8e8432ce28

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_AIML_7053/COMPUTER VISION FOR AI/QP_COMPUTER VISION FOR AI(702AI0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all, 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q1   Answer briefly:
CO-1;   a.   For each of the following applications, identify which feature level   [04]
SO-1;
(Low-level, Mid-level, or High-level) is most appropriate, and
BL-5
explain your reasoning.
i) Detecting car wheels based on feature descriptors and
matching
ii) Detecting a person with a hat using semantic relation of
objects
CO-2;   b.   Justify that Speeded Up Robust Features (SURF) is fast. Given the   [04]
SO-1;
following Hessian matrices for three key points at intermediate of
BL-5
SURF. Test whether SURF stops comparison or continues with the
calculation of Euclidean distance for comparison?
H1 =[10 −1   H2 =[10 −2   H3 =[10 −1
−1 15],   −2 −15],   −1 −5]
CO-3;   c.   Use Earth Mover Distance test whether the given two images   [04]
SO-1;
match.
BL-5
1   1   0   0   1   2   1   1
1   2   0   0   2   2   1   1
2   2   3   3   3   3   0   0
1   2   3   2   3   3   0   0
Image 1 (2-bit)   Image 2 (2-bit)
CO-4;   d.   In the context of optical flow, what does the velocity vector represent?   [04]
SO-1;
Compare sparse and dense optical flow.
BL-2
********** 1 **********
--- page 2 ---
CO-5;   e.   For Region based Convolutional Network, explain the role of   [04]
SO-1;
‘Bounding Box Regressor’ algorithm.
BL-3
Q2   a   For Histogram of Gradient,   [10]
CO-1;   i) Describe the steps for determining HoG descriptor in brief
SO-1;
ii) For image size of 64×128, calculate the length of HoG vector
BL-3
for 8×8 pixels/cell and 4×4 cells/ block.
CO-2;   b   For the given image, apply Harris corner detector to test whether   [10]
SO-1;
pixel at the center is corner pixel or not. Sobel operators Gx and
BL-3
Gy. Size of window is 3×3. (Given: k = 0.04 and threshold for
corner response = 1000).
0   0   0   0   0
0   0   0   0   0
1   1   1   0   0
1   1   1   0   0
1   1   2   0   0
Image
−1 0 1   −1 −2 −1
𝐺𝑥= [ −2 0 2 ] ,   𝐺𝑦= [ 0   0   0 ]
−1 0 1   1   2   1
Q3   a   For Oriented FAST and Rotated BRIEF (ORB),   [10]
CO-2;   i) Write the roles of FAST and rBrief.
SO-1;
ii) Find the orientation of the highlighted key point
BL-5
1   1   1   1   1
1   10   10   10   1
Image =   1   10   40   10   1
1   10   10   10   1
1   1   1   1   1
i)   List advantages
Q3   b   For the generation of feature descriptors using Speeded Up Robust   [10]
CO-3;   Features (SURF), list the steps and explain it in brief.
SO-1;
Justify that SURF is faster than SIFT.
BL-3,5
Q4   a   Explain the steps involved in the Bag of Visual Words for feature   [10]
CO-3;
matching. Use example images and histograms for the explanation.
SO-1;
BL-5   K-means clustering uses K = 6
********** 2 **********
--- page 3 ---
CO-5;   b   Design an appropriate Convolutional Neural Network (CNN)   [10]
SO-1;
model with the following architecture specifications for an input
BL-6
gray image of size 64 × 64.
• One convolutional layer with 12 filters, each of size 3×3
• One max pooling layer with pool size (3×3)
• One dropout layer with probability 0.1
• One flatten layer
• Three dense (fully connected) layers
• No padding (i.e., "valid" convolution)
•   Stride = 1 for convolution
Tasks:
1. Provide the output shape after each layer.
2. Do not consider bias terms at any layer.
3. Clearly specify activation functions.
Q5   a   For Gaussian Mixture Model, explain   [10]
CO-4;   i)   Key feature
SO-1;
ii)   Initialization phase
BL-2
iii)   Matching of pixels with Gaussian curve
CO-5;   b   In a Single-Shot Detector (SSD), feature maps of sizes 38×38,   [10]
SO-1;
19×19, 10×10, and 5×5 are used for multi-scale detection. Each
BL-3
location predicts 4 bounding boxes with 21 class scores.
• Calculate the total number of bounding boxes generated.
• How many total output values (bounding box coordinates +
class scores) are produced for one image?
Q6   a   Give an overview of the U-Net architecture for image   [10]
CO-5;   segmentation and explain the working of its encoder–decoder
SO-1;
structure with a neat schematic diagram.
BL-2
CO-4;   b   Draw architecture of Mask RCNN and explain it in brief. Justify   [10]
SO-1;
the use of RoI align in Mask RCNN
BL-3
Q7   a   Explain the steps of Scale-Invariant Feature Transform in brief.   [10]
CO-1;   Describe the generation descriptor after key point localization of
SO-1;
SIFT algorithm.
BL-3
********** 3 **********
--- page 4 ---
CO-3;   b   Explain Region Proposal Network of Faster RCNN and justify that   [10]
SO-1;
it makes Faster RCNN is faster than Fast RCNN. Illustrate with
BL-3
example images.
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper 63994ecb3234

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_AI_7012/COMPUTER VISION FOR AI/QP_COMPUTER VISION FOR AI(702AI0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all, 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q1   Answer briefly:
CO-1;   a.   For each of the following applications, identify which feature level   [04]
SO-1;
(Low-level, Mid-level, or High-level) is most appropriate, and
BL-5
explain your reasoning.
i) Detecting car wheels based on feature descriptors and
matching
ii) Detecting a person with a hat using semantic relation of
objects
CO-2;   b.   Justify that Speeded Up Robust Features (SURF) is fast. Given the   [04]
SO-1;
following Hessian matrices for three key points at intermediate of
BL-5
SURF. Test whether SURF stops comparison or continues with the
calculation of Euclidean distance for comparison?
H1 =[10 −1   H2 =[10 −2   H3 =[10 −1
−1 15],   −2 −15],   −1 −5]
CO-3;   c.   Use Earth Mover Distance test whether the given two images   [04]
SO-1;
match.
BL-5
1   1   0   0   1   2   1   1
1   2   0   0   2   2   1   1
2   2   3   3   3   3   0   0
1   2   3   2   3   3   0   0
Image 1 (2-bit)   Image 2 (2-bit)
CO-4;   d.   In the context of optical flow, what does the velocity vector represent?   [04]
SO-1;
Compare sparse and dense optical flow.
BL-2
********** 1 **********
--- page 2 ---
CO-5;   e.   For Region based Convolutional Network, explain the role of   [04]
SO-1;
‘Bounding Box Regressor’ algorithm.
BL-3
Q2   a   For Histogram of Gradient,   [10]
CO-1;   i) Describe the steps for determining HoG descriptor in brief
SO-1;
ii) For image size of 64×128, calculate the length of HoG vector
BL-3
for 8×8 pixels/cell and 4×4 cells/ block.
CO-2;   b   For the given image, apply Harris corner detector to test whether   [10]
SO-1;
pixel at the center is corner pixel or not. Sobel operators Gx and
BL-3
Gy. Size of window is 3×3. (Given: k = 0.04 and threshold for
corner response = 1000).
0   0   0   0   0
0   0   0   0   0
1   1   1   0   0
1   1   1   0   0
1   1   2   0   0
Image
−1 0 1   −1 −2 −1
𝐺𝑥= [ −2 0 2 ] ,   𝐺𝑦= [ 0   0   0 ]
−1 0 1   1   2   1
Q3   a   For Oriented FAST and Rotated BRIEF (ORB),   [10]
CO-2;   i) Write the roles of FAST and rBrief.
SO-1;
ii) Find the orientation of the highlighted key point
BL-5
1   1   1   1   1
1   10   10   10   1
Image =   1   10   40   10   1
1   10   10   10   1
1   1   1   1   1
i)   List advantages
Q3   b   For the generation of feature descriptors using Speeded Up Robust   [10]
CO-3;   Features (SURF), list the steps and explain it in brief.
SO-1;
Justify that SURF is faster than SIFT.
BL-3,5
Q4   a   Explain the steps involved in the Bag of Visual Words for feature   [10]
CO-3;
matching. Use example images and histograms for the explanation.
SO-1;
BL-5   K-means clustering uses K = 6
********** 2 **********
--- page 3 ---
CO-5;   b   Design an appropriate Convolutional Neural Network (CNN)   [10]
SO-1;
model with the following architecture specifications for an input
BL-6
gray image of size 64 × 64.
• One convolutional layer with 12 filters, each of size 3×3
• One max pooling layer with pool size (3×3)
• One dropout layer with probability 0.1
• One flatten layer
• Three dense (fully connected) layers
• No padding (i.e., "valid" convolution)
•   Stride = 1 for convolution
Tasks:
1. Provide the output shape after each layer.
2. Do not consider bias terms at any layer.
3. Clearly specify activation functions.
Q5   a   For Gaussian Mixture Model, explain   [10]
CO-4;   i)   Key feature
SO-1;
ii)   Initialization phase
BL-2
iii)   Matching of pixels with Gaussian curve
CO-5;   b   In a Single-Shot Detector (SSD), feature maps of sizes 38×38,   [10]
SO-1;
19×19, 10×10, and 5×5 are used for multi-scale detection. Each
BL-3
location predicts 4 bounding boxes with 21 class scores.
• Calculate the total number of bounding boxes generated.
• How many total output values (bounding box coordinates +
class scores) are produced for one image?
Q6   a   Give an overview of the U-Net architecture for image   [10]
CO-5;   segmentation and explain the working of its encoder–decoder
SO-1;
structure with a neat schematic diagram.
BL-2
CO-4;   b   Draw architecture of Mask RCNN and explain it in brief. Justify   [10]
SO-1;
the use of RoI align in Mask RCNN
BL-3
Q7   a   Explain the steps of Scale-Invariant Feature Transform in brief.   [10]
CO-1;   Describe the generation descriptor after key point localization of
SO-1;
SIFT algorithm.
BL-3
********** 3 **********
--- page 4 ---
CO-3;   b   Explain Region Proposal Network of Faster RCNN and justify that   [10]
SO-1;
it makes Faster RCNN is faster than Fast RCNN. Illustrate with
BL-3
example images.
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper 75c78e37fcae

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSE_DS_7011/COMPUTER VISION/QP_COMPUTER VISION(702EX0E015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER VISION
Date: 05 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions,attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1   Answer briefly   [20]
CO-1   a. A computer vision system for an autonomous vehicle is to be developed.   [04]
BL-2   Which technique (low-level/mid-level/high-level) is preferable for the
process. Justify each answer.
i.   Detect of the edges of road signs. Justify your answer.
ii.   Understand the meaning of road signs, such as "Stop" or "Left"
or “Right”.
CO-2   b. Explain the roles of FAST and rBRIEF in the ORB (Oriented FAST and   [04]
BL-3
Rotated BRIEF) feature descriptor.
CO-2   c.   For Brute Force Matcher   [04]
BL-3   (i)   Given the following feature descriptors:
𝐷1 = [1,2,3],𝐷2 = [2,2,3], 𝐷3 = [0,1,1]
Query descriptor, 𝑄= [1,2,2]
Use Brute Force Matcher to identify the descriptor which is the
best match for query descriptor. Use Euclidean distance.
(ii)   What is the main limitation Brute Force Matcher? Prove it with
an example.
CO-2   d.   For K-means clustering,   [04]
BL-3   i)   Explain two limitations with examples
ii) Perform one iteration of K-Means clustering for the pixel intensity
for the set, X = [10,12,15,70,75,80],  k=2
Assume initial means μ₁ = 12, μ₂ = 75
CO-4   e. An input image of size 33×33 is passed through a convolutional layer   [04]
BL-4   followed by a Max pooling layer.
Convolution Layer
filter size = 5×5, stride = 1, padding = 2, number of filters = 10,
ReLU activation
Max-pooling layer
Filter size = 2 × 2, Stride = 2
Calculate
i) Output dimensions after the convolution layer
********** 1 **********
--- page 2 ---
ii) Output dimensions after the pooling layer
Q2   a   For Histogram of Gradients descriptor, describe each step in brief.
CO-2   [10]
BL-2
Q2   b   Determine corner response for the following image using Harris Corner   [10]
CO-2   response. Use window of size 3×3. Filters for the determining gradients
BL-3
are given below. Test whether pixel at the center is a corner or not.
Threshold for corner response, Th = 300,000
20   20   20   20   20
20   20   20   20   20
10   10   10   10   10
10   10   10   10   10
10   10   10   10   10
Image
1   0   -1   1   2   1
2   0   -2   0   0   0
1   0   -1   -1   -2   -1
Sobel mask for x-gradient   Sobel mask for y-gradient
Q3   a   For SIFT (Scale-Invariant Feature Transform) algorithm and briefly   [10]
CO-2   describe the role of each step in 2-3 sentences. Explain key point
BL-3
localization in details.
********** 2 **********
--- page 3 ---
Q3   b   Consider the following image.   [10]
CO-2   i) Construct integral image.
BL-3, 4
ii) Apply the given filter and calculate the output at the center of
image. Use integral image to filter the image.
iii) Why is SURF descriptor faster than SIFT descriptor?
0   0   0   0   0   1   1   1   1
0   0   0   0   0   1   1   1   1
0   0   0   0   0   1   1   1   1
0   0   0   0   0   1   1   1   1
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
Image
Filter
Q4   a   Develop an image retrieval system for a large dataset of natural images   [10]
(forests, mountains, rivers).
CO-2
(i) Explain how Bag of Visual Words (BoVW) represents each image
BL-3
and discuss how clustering of descriptors helps in constructing the
visual vocabulary
(ii) Describe one limitation of BoVW in object recognition.
(iii) SIFT descriptors from three images (each descriptor is 2D for
simplicity) are given below. Construct BoVW histogram for each
image. Consider cluster centres as μ₁ = (2,2), μ₂ = (8,8).
Image   Descriptor1, D1 Descriptor2, D2 Descriptor3, D3
I1   (1,2)   (2,1)   (3,2)
I2   (8,8)   (9,9)   (8,9)
I3   (1,1)   (2,2)   (2,1)
Q4   b   For image matching using Image Pyramid,   [10]
(i) Explain the technique for image matching using Earth Mover’s
CO-2
Distance (EMD).
BL-3,4
(ii) Write one practical application of pyramids in image processing
or object detection.
********** 3 **********
--- page 4 ---
(iii) Given   normalized   histograms   representing   intensity
distributions of two images, Compute the distance between H₁
and H₂ using EMD
𝐻1 = [0.0, 0.2,0.5,0.3], 𝐻2 = [0.0, 0.0,0.1,0.9]
(iv) Repeat the same for two other images with the following
histograms and interpret the similarity between them.
𝐻1 = [0.0, 0.2,0.5,0.3], 𝐻2 = [0.0, 0.4,0.4,0.2]
v) Which pair of the histograms is more similar than other
Q5   a   Describe how Gaussian Mixture Model (GMM) is generated to [10]
construct background frame. A pixel intensity is modeled with a 3-
CO-2
component (K=3)
BL-3
Gaussian Curve Μ   σ   w
1   100   5   0.5
2   120   7   0.3
3   150   10   0.2
A new pixel intensity is x = 118. Test whether it belongs to
background or foreground.
Q5   b   For Mean Shift algorithm,   [10]
CO-2   (i) Explain advantages and limitations of Mean Shift algorithm with
BL-3   suitable examples.
(ii) Predict the effect of increasing the space bandwidth, hs on
clustering the samples. Explain with examples
Q6   a   For 2D images,   [10]
(i) Explain image transformations using scaling, rotation, flipping,
CO-3
and shearing, with their effects on images and general
BL-3,4
mathematical forms.
(ii) A point P(3, 2) is transformed using the following 2×2
transformation matrix:
𝑇= [2 1
0 1]
Calculate the new coordinates of the point after transformation
(iii)   If P(3,2) is transformed with scaling in x direction by 2 and in Y
direction by 1, followed by horizontal shear factor of 1.
Determine the new coordinates of the point after transformation.
Comment on the transformations in (ii) and (iii).
Q6   b   In relation to stereo vision, explain in brief   [10]
CO-3   (i)   Determination of depth
BL-3
(ii)   Epipolar geometry
Q7   a   Draw architecture of RCNN and explain each layer/block in 2-3 [10]
CO- 4   sentences in brief.
BL-3
Q7   b   Illustrate ‘Divide and Conquer’ approach for YOLO. Justify that YOLO   [10]
CO-4   speeds up the process of object detection
BL-4
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper ff4115bf3ccb

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSE_DS_7057/COMPUTER VISION/QP_COMPUTER VISION(702EX0E015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER VISION
Date: 05 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions,attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1   Answer briefly   [20]
CO-1   a. A computer vision system for an autonomous vehicle is to be developed.   [04]
BL-2   Which technique (low-level/mid-level/high-level) is preferable for the
process. Justify each answer.
i.   Detect of the edges of road signs. Justify your answer.
ii.   Understand the meaning of road signs, such as "Stop" or "Left"
or “Right”.
CO-2   b. Explain the roles of FAST and rBRIEF in the ORB (Oriented FAST and   [04]
BL-3
Rotated BRIEF) feature descriptor.
CO-2   c.   For Brute Force Matcher   [04]
BL-3   (i)   Given the following feature descriptors:
𝐷1 = [1,2,3],𝐷2 = [2,2,3], 𝐷3 = [0,1,1]
Query descriptor, 𝑄= [1,2,2]
Use Brute Force Matcher to identify the descriptor which is the
best match for query descriptor. Use Euclidean distance.
(ii)   What is the main limitation Brute Force Matcher? Prove it with
an example.
CO-2   d.   For K-means clustering,   [04]
BL-3   i)   Explain two limitations with examples
ii) Perform one iteration of K-Means clustering for the pixel intensity
for the set, X = [10,12,15,70,75,80],  k=2
Assume initial means μ₁ = 12, μ₂ = 75
CO-4   e. An input image of size 33×33 is passed through a convolutional layer   [04]
BL-4   followed by a Max pooling layer.
Convolution Layer
filter size = 5×5, stride = 1, padding = 2, number of filters = 10,
ReLU activation
Max-pooling layer
Filter size = 2 × 2, Stride = 2
Calculate
i) Output dimensions after the convolution layer
********** 1 **********
--- page 2 ---
ii) Output dimensions after the pooling layer
Q2   a   For Histogram of Gradients descriptor, describe each step in brief.
CO-2   [10]
BL-2
Q2   b   Determine corner response for the following image using Harris Corner   [10]
CO-2   response. Use window of size 3×3. Filters for the determining gradients
BL-3
are given below. Test whether pixel at the center is a corner or not.
Threshold for corner response, Th = 300,000
20   20   20   20   20
20   20   20   20   20
10   10   10   10   10
10   10   10   10   10
10   10   10   10   10
Image
1   0   -1   1   2   1
2   0   -2   0   0   0
1   0   -1   -1   -2   -1
Sobel mask for x-gradient   Sobel mask for y-gradient
Q3   a   For SIFT (Scale-Invariant Feature Transform) algorithm and briefly   [10]
CO-2   describe the role of each step in 2-3 sentences. Explain key point
BL-3
localization in details.
********** 2 **********
--- page 3 ---
Q3   b   Consider the following image.   [10]
CO-2   i) Construct integral image.
BL-3, 4
ii) Apply the given filter and calculate the output at the center of
image. Use integral image to filter the image.
iii) Why is SURF descriptor faster than SIFT descriptor?
0   0   0   0   0   1   1   1   1
0   0   0   0   0   1   1   1   1
0   0   0   0   0   1   1   1   1
0   0   0   0   0   1   1   1   1
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0
Image
Filter
Q4   a   Develop an image retrieval system for a large dataset of natural images   [10]
(forests, mountains, rivers).
CO-2
(i) Explain how Bag of Visual Words (BoVW) represents each image
BL-3
and discuss how clustering of descriptors helps in constructing the
visual vocabulary
(ii) Describe one limitation of BoVW in object recognition.
(iii) SIFT descriptors from three images (each descriptor is 2D for
simplicity) are given below. Construct BoVW histogram for each
image. Consider cluster centres as μ₁ = (2,2), μ₂ = (8,8).
Image   Descriptor1, D1 Descriptor2, D2 Descriptor3, D3
I1   (1,2)   (2,1)   (3,2)
I2   (8,8)   (9,9)   (8,9)
I3   (1,1)   (2,2)   (2,1)
Q4   b   For image matching using Image Pyramid,   [10]
(i) Explain the technique for image matching using Earth Mover’s
CO-2
Distance (EMD).
BL-3,4
(ii) Write one practical application of pyramids in image processing
or object detection.
********** 3 **********
--- page 4 ---
(iii) Given   normalized   histograms   representing   intensity
distributions of two images, Compute the distance between H₁
and H₂ using EMD
𝐻1 = [0.0, 0.2,0.5,0.3], 𝐻2 = [0.0, 0.0,0.1,0.9]
(iv) Repeat the same for two other images with the following
histograms and interpret the similarity between them.
𝐻1 = [0.0, 0.2,0.5,0.3], 𝐻2 = [0.0, 0.4,0.4,0.2]
v) Which pair of the histograms is more similar than other
Q5   a   Describe how Gaussian Mixture Model (GMM) is generated to [10]
construct background frame. A pixel intensity is modeled with a 3-
CO-2
component (K=3)
BL-3
Gaussian Curve Μ   σ   w
1   100   5   0.5
2   120   7   0.3
3   150   10   0.2
A new pixel intensity is x = 118. Test whether it belongs to
background or foreground.
Q5   b   For Mean Shift algorithm,   [10]
CO-2   (i) Explain advantages and limitations of Mean Shift algorithm with
BL-3   suitable examples.
(ii) Predict the effect of increasing the space bandwidth, hs on
clustering the samples. Explain with examples
Q6   a   For 2D images,   [10]
(i) Explain image transformations using scaling, rotation, flipping,
CO-3
and shearing, with their effects on images and general
BL-3,4
mathematical forms.
(ii) A point P(3, 2) is transformed using the following 2×2
transformation matrix:
𝑇= [2 1
0 1]
Calculate the new coordinates of the point after transformation
(iii)   If P(3,2) is transformed with scaling in x direction by 2 and in Y
direction by 1, followed by horizontal shear factor of 1.
Determine the new coordinates of the point after transformation.
Comment on the transformations in (ii) and (iii).
Q6   b   In relation to stereo vision, explain in brief   [10]
CO-3   (i)   Determination of depth
BL-3
(ii)   Epipolar geometry
Q7   a   Draw architecture of RCNN and explain each layer/block in 2-3 [10]
CO- 4   sentences in brief.
BL-3
Q7   b   Illustrate ‘Divide and Conquer’ approach for YOLO. Justify that YOLO   [10]
CO-4   speeds up the process of object detection
BL-4
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 7 · paper 256f09376f7e

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/MBATech_AI_7051/COMPUTER VISION FOR AI/QP_COMPUTER VISION FOR AI(702AI0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all, 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q1   Answer briefly:
CO-1;   a.   For each of the following applications, identify which feature level   [04]
SO-1;
(Low-level, Mid-level, or High-level) is most appropriate, and
BL-5
explain your reasoning.
i) Detecting car wheels based on feature descriptors and
matching
ii) Detecting a person with a hat using semantic relation of
objects
CO-2;   b.   Justify that Speeded Up Robust Features (SURF) is fast. Given the   [04]
SO-1;
following Hessian matrices for three key points at intermediate of
BL-5
SURF. Test whether SURF stops comparison or continues with the
calculation of Euclidean distance for comparison?
H1 =[10 −1   H2 =[10 −2   H3 =[10 −1
−1 15],   −2 −15],   −1 −5]
CO-3;   c.   Use Earth Mover Distance test whether the given two images   [04]
SO-1;
match.
BL-5
1   1   0   0   1   2   1   1
1   2   0   0   2   2   1   1
2   2   3   3   3   3   0   0
1   2   3   2   3   3   0   0
Image 1 (2-bit)   Image 2 (2-bit)
CO-4;   d.   In the context of optical flow, what does the velocity vector represent?   [04]
SO-1;
Compare sparse and dense optical flow.
BL-2
********** 1 **********
--- page 2 ---
CO-5;   e.   For Region based Convolutional Network, explain the role of   [04]
SO-1;
‘Bounding Box Regressor’ algorithm.
BL-3
Q2   a   For Histogram of Gradient,   [10]
CO-1;   i) Describe the steps for determining HoG descriptor in brief
SO-1;
ii) For image size of 64×128, calculate the length of HoG vector
BL-3
for 8×8 pixels/cell and 4×4 cells/ block.
CO-2;   b   For the given image, apply Harris corner detector to test whether   [10]
SO-1;
pixel at the center is corner pixel or not. Sobel operators Gx and
BL-3
Gy. Size of window is 3×3. (Given: k = 0.04 and threshold for
corner response = 1000).
0   0   0   0   0
0   0   0   0   0
1   1   1   0   0
1   1   1   0   0
1   1   2   0   0
Image
−1 0 1   −1 −2 −1
𝐺𝑥= [ −2 0 2 ] ,   𝐺𝑦= [ 0   0   0 ]
−1 0 1   1   2   1
Q3   a   For Oriented FAST and Rotated BRIEF (ORB),   [10]
CO-2;   i) Write the roles of FAST and rBrief.
SO-1;
ii) Find the orientation of the highlighted key point
BL-5
1   1   1   1   1
1   10   10   10   1
Image =   1   10   40   10   1
1   10   10   10   1
1   1   1   1   1
i)   List advantages
Q3   b   For the generation of feature descriptors using Speeded Up Robust   [10]
CO-3;   Features (SURF), list the steps and explain it in brief.
SO-1;
Justify that SURF is faster than SIFT.
BL-3,5
Q4   a   Explain the steps involved in the Bag of Visual Words for feature   [10]
CO-3;
matching. Use example images and histograms for the explanation.
SO-1;
BL-5   K-means clustering uses K = 6
********** 2 **********
--- page 3 ---
CO-5;   b   Design an appropriate Convolutional Neural Network (CNN)   [10]
SO-1;
model with the following architecture specifications for an input
BL-6
gray image of size 64 × 64.
• One convolutional layer with 12 filters, each of size 3×3
• One max pooling layer with pool size (3×3)
• One dropout layer with probability 0.1
• One flatten layer
• Three dense (fully connected) layers
• No padding (i.e., "valid" convolution)
•   Stride = 1 for convolution
Tasks:
1. Provide the output shape after each layer.
2. Do not consider bias terms at any layer.
3. Clearly specify activation functions.
Q5   a   For Gaussian Mixture Model, explain   [10]
CO-4;   i)   Key feature
SO-1;
ii)   Initialization phase
BL-2
iii)   Matching of pixels with Gaussian curve
CO-5;   b   In a Single-Shot Detector (SSD), feature maps of sizes 38×38,   [10]
SO-1;
19×19, 10×10, and 5×5 are used for multi-scale detection. Each
BL-3
location predicts 4 bounding boxes with 21 class scores.
• Calculate the total number of bounding boxes generated.
• How many total output values (bounding box coordinates +
class scores) are produced for one image?
Q6   a   Give an overview of the U-Net architecture for image   [10]
CO-5;   segmentation and explain the working of its encoder–decoder
SO-1;
structure with a neat schematic diagram.
BL-2
CO-4;   b   Draw architecture of Mask RCNN and explain it in brief. Justify   [10]
SO-1;
the use of RoI align in Mask RCNN
BL-3
Q7   a   Explain the steps of Scale-Invariant Feature Transform in brief.   [10]
CO-1;   Describe the generation descriptor after key point localization of
SO-1;
SIFT algorithm.
BL-3
********** 3 **********
--- page 4 ---
CO-3;   b   Explain Region Proposal Network of Faster RCNN and justify that   [10]
SO-1;
it makes Faster RCNN is faster than Fast RCNN. Illustrate with
BL-3
example images.
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper 870798f8af40

- Departments: Artificial Intelligence, Computer Engineering, Data Science
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / ARTIFICIAL INTELLIGENCE, B TECH / COMPUTER, B TECH / DATA SCIENCE, B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-VI/COMPUTER VISION/Computer Vision Batch 2023-24,2024-25 Re Exam.pdf` (+6 identical copies)
- Printed on paper: max marks: 100; exam date: 06 July 2026
- Text: ocr (3 pages), mean OCR confidence 78.9

````text
SVKM’S NMIMS rs
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT ENGINEERING

Academic Year: 2025-26
Program: B.Tech/ B Tech Intg.(COMP/AI&DS)

Subject: COMPUTER VISION °
Date : 06 July 2026
Marks: 100
Re-Exam (2023-24/2024-25)
Instructions:

1. This question paper contains 3 pages.

2. Question No. | is compulsory.

3. Out of remaining questions, attempt any 4 questions.

4. In all 5 questions to be attempted.

5. All questions carry equal marks.

6. Answer to each new question to be started on a fresh page.

7. Figures in brackets on the right-hand side indicate full marks.

8. Assume Suitable data if necessary. t
Ql Answer briefly (20] ‘
CO- 4 a. ° i
SO- 1,6 Describe the limitations of human vision using examples. {05S]

BL- 2
COz3 b. . . : .
S0- 1.6 For mean shift algorithm, show the effect of large and small bandwidth of [05]
BL-5 , window (kernel function). Explain it with suitable plots
CO- 2 c. ar : |
SO- 1,6 Compare Scale Invariant Feature Transform (SIFT) and Speeded-Up Robust }- [05]
BL-4 Features (SURF)
CO- 4 d.
SO- 1,6 Explain in brief Image Rectification. [05]
BL- 3
Q2 a
CO- | List the steps to determine Histogram of Gradients (HoG) as a feature for
SO- 1,6 the image. Explain each step in brief. {10]
BL- 5
b Given the following image gradients for a 3x3 window centered at a pixel: |
_ |2 2 2 121i.
2 2 2 15 1
29 3 Lil
Q2
CO- | Gradient in x direction, Ix Gradient in x direction, ly [10] —
SO- 1,6 “ i) Construct Harris corner matrix and determine corner response.
BL-5 Assume constant, k = 0.04 and threshold = 100. =
ii) Determine whether the given pixel corresponds to a corner, edge,
or flat region. Also, spectfy the conditions based on the corner =
response function that are used to classify a pixel into these
categories.
oc ee
CO-2 For the Scale Invariant Feature Transform (SIFT) algorithm, explain the 10]
so- 1,6 | process of scale-space generation followed by the Difference of Gaussian

RRR RRR RAE | RR RRR KEK
--- page 2 ---
(DoG) method. Illustrate it with a neat block diagram and suitable example

BL- 5

images.
b Given the following grayscale image: *

22 2 2 2 i
222 2 2
22 2 2 2

Q3 22 2 2 2

CO-2 22 2 2 2 ,

i) Construct the integral image for the given input. [10]
SO- 1,6 Pe . . ‘ . .
BL-1.5 i) Using the integral image, compute the sum of pixels which are bold.

How many additions and subtractions are required for summation.
ul) Verify your answer using direct summation. How many additions are
required?

iv) State the advantage of using an integral image for such computations.

a Describe the advantages and limitations of the K-Nearest Neighbor (KNN)
algorithm. A dataset contains the following labeled points.
Point (x, y) Class |
Q4 Pl (1,2) Class 1
CO-3 B2 (2,1) Class |
SO- 1,6 P3 (2,4) Class 2 [10]
BL-2 P4 (3,3) Class 2 .
PS (6,5) Class 2
| P6 (7,7) Class |

A new point, P= (3,2) is to be classified using K-Nearest Neighbor (KNN)
with Euclidean distance. Perform classification for K=1 and K = 3.

os 3 ° Explain the process of background subtraction for motion tracking in a ;
S0- 1.6 video using frame differencing. Also, illustrate how varying threshold {10]
BL-5 > values affects the segmentation of foreground objects.
Q5 a
CO- 3 Derive optical flow equation for determining velocity vector, [Vx,Vy], £10]
SO- 1,6 where Vx and Vy are velocities in X and Y direction respectively.
BL- 4
Q5 b *
CO- 3 Explain the basic concept of Gaussian Mixture Modeling (GMM) for the: [10]
SO- 1,6 generation of background.
BL- 5 .
Q6 a
CO- 4 oo, . . ‘
Describe in brief the any five challenges of Automated Visual Inspection (10]
a a (AVI) systems using computer vision.
Q6 b
CO- 4 v For 2x2 transformation of image, explain flipping and mirroring 10]
SO- 1,6 matrices and their effects.
BL- 5
Q7 a ’
CO- 4 Show camera model and clearly showing extrinsic and intrinsic matrix and [10]
SO- 1,6 world coordinates. Explain the role of extrinsic and intrinsic matrix.
BL-3 |v
Q7 b “Explain how epipolar geometry is used for matching key points in stereo | [10]
CO- 4 | images, and illustrate the concept with suitable example images. Also,

RRR RRR REE K DORR RRR KKK
--- page 3 ---
. .

SO- 1,6 describe the epipolar constraint with reference to a point and _ its
BL- 3 corresponding epipolar line. .

RRR RRR RRR Qk RRR RHE
````

## 2025-26 · Re-Exam · Sem 7 · paper b3cd0d2b1551

- Departments: Artificial Intelligence, Common (all branches), Data Science
- Programmes: B TECH, B TECH / CSE DATA SCIENCE (311), MBA TECH / Artificial Intelligence
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/CSE DATA SCIENCE (311)/SEM-VII/COMPUTER VISION/Computer Vision, Sem-VII, Batch 2023-24 & 2024-25 Re Exam.pdf` (+2 identical copies)
- Printed on paper: max marks: 100
- Text: ocr (4 pages), mean OCR confidence 86.7

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2025-2026 ;

Program: B. Tech./ MBA Tech Stream: CSE(DS)/AI Year: TV Semester: VII

Subject: Computer Vision Time: 3 _ hrs (jozeoamto 4:00pm)
Date: 24 / ti _/2025 . No. of Pages: 4 -

Marks: 100

__ Re) Examination (23-24/24-25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

(Question No. 1 is compulsory.
2) Out of remaining questions, attempt any 4 questions. ( y

3) In all 5 questions to be attempted.
4) All questions carry equal marks. . S
5) Answer to each new question to be started on a fresh page. S

“%, *
6) Figures in brackets on the right hand side indicate full marks. EET

7) Assume suitable data if necessary.

Ql Answer briefly:
CO-1; | a | What are the three key limitations of human vision, and how does computer vision | [05]
SO-1; help to overcome these limitations?
BL-4
CO-2; | b_ | In SIFT algorithm, if the number of octaves is changed from 4 to 6, what effect will it | [05]
SO-1; have on the length of the feature vector for orientation assignment of key points?
BL-4
|_ CO- c | Apply the mean-shift algorithm to the following image, using the given parameters: | [05]
03.4; e Color bandwidth = 18, Threshold for convergence: distance between old and
SO-1; ‘

new means = 30

BL-3 image = (5° 55 60 190 200 |
g 53 45 202 196 205

CO-1; | d_ | Briefly explain the concept of invariants, their types, and applications in 3D computer | [05]

SO-1; vision.

BL-2

Answer any four from Q2 to Q7
Q2 a_ | Elaborate on the typical steps involved in the process of recognition in computer | [10]
. CO-4; vision. :

SO-1; 4

BL-2

Page 1 of 4
--- page 2 ---
4 x

CO-2; | b | Apply the following two Gaussian filters to update the pixels in the highlighted 3x3 | [10]
SO-1; region of the given image. Do not update the non-highlighted boundary pixels.

BL-5 Evaluate and compare the results obtained from both filters.
. 1 2 2 111
Gaussian filters, fi=wzl2 4 2) fh=—a]1 2 1
ma 12 1 10 111
Image:
1] 1 1 1 1
1] 5 5 5 | 1
1 | 5 5 5] 1
|
1] 5 5 5 | 1
1 1 1 1 1 .
Q3 a_ | Perform the Harris Corner Detection on the following 5x5 grayscale image using the | [10]
CO-2: filter below to determine whether a corner is present at the center pixel.
SO-1; Given parameters: Harris constant k = 0.06, Threshold for corner response R > 20000
BL-3 Vertical filter: Horizontal filter:
1 0 -1 1 1 1
1 0 -1 0 0 0
1 0 -1 -1 -1 -1
=
Image:

0 0 12 0 0

0 0 12 0 0

o | of}2]o0] 0

0 0 12 0 0

0 0 12 0 0

t

CO#3; | b | Perform K-means clustering with K = 2 on the following 3x3 grayscale image. | [10]

SO-1; Use absolute distance on intensity values (1-D) and start with initial centroids C)=20

BL-3 and C2=200. Perform iterations until convergence, showing the assignment step and
centroid updates. Finally give the final cluster centers and the clustered image with
labels for each pixel.

;
Page 2 of 4
--- page 3 ---
Image: a
is | 22 | 20

200 | 210 | 205

19 21 18
Q4 a | Apply the Speeded-Up Robust Features (SURF) method to perform keypoint [10]
Sou detection by constructing a Hessian matrix for the highlighted region of the image.
BL-3 (Given: The constant, W = 0.9, and the threshold = 15)

rm

I =
mace 1 2 2 2 1
1 1 1 1 1
00 0 0 0 0 0 0 0 0
0 1-2 1~°0 0 1 1 1 0
G,=|0 1 -2 1 O|, G,=j]0 -—2 -2 —2 OF
0 1-2 1 °0 0 1 1 1 O
00 0 0 0 0 0 0 0 0

oO 0 1 0-10
Gy=|0 0 0 0 0

CO-2; |b | Find the mean and standard deviation for the following pixel intensity values Xi(t), X2 | [10]
SO-1; (t), X3(t), Xa(t), Xs(t) in an image observed for K=5 in a Gaussian Mixture Model
BL-5 (GMM) and interpret the results.

Page 3 of 4
--- page 4 ---
X,(t) = [5, 6,5]
X(t) = [251, 252, 254)
. X3(t) = (250, 249, 250)
X(t) = (250, 250, 248)

X5(t) = (0,0, 0]

Q5 Write a note on essential matrix. Let the point in the first image be x and the [101)
CO-1: corresponding point in the second image be x’. Use the following essential matrix E to
SO-1; determine if the epipolar constraint is perfectly satisfied:

BL-3 ,
o -l1 Z 1 2
E=]1 0 - 3 (7 ; v=[]
—2 1 0 1 y
CO-4; Discuss the crucial blocks including Perception, Analysis, and Response in |} [10]
SO-1; surveillance systems.
BL-2

Q6 Compute epipolar line on the right image given the coordinates of point X and the | [10]

CO-1: fundamental matrix F.

Ts _ 321069: _f 95646 9 9658

SO-1; 343.5300 0.00310695 came 2.96584

BL-3 x = |221.7005 = | —0.028094 —0.00771621 56.3813 >)
1 13.1905 —29.2007 —9999.79

CO-4; Brief on various types of image acquisition systems available for vehicle vision | [10]

SO-1; system.

BL-2

Q7 Explain the Correspondence problem in 3-dimensional vision. [10]

CO-1;

SO-1;

BL-2

CO-43 Enlist and explain the major challenges encountered in dry cereal grain quality | [10]
SO-1; inspection from the perspective of computer vision.

BL-2

Page 4 of 4
````

## 2024-25 · Final + Re-Exam · Sem 6 · paper f4eea022b2a9

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/VI SEMESTER/COMPUTER VISION/Computer Vision, Sem VI, Final Exam 2024-25 & Re Exam 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 89.8

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025

Program/s: B.Tech / MBA Tech /B¥I Year: ITI/V/VI Semester: VI/X/XII
Stream/s : (CE/ AIDS/ CE-intg) / MBA Tech

Subject: Computer Vision "Time: 03 hrs (2.00 pm to 5.00 pm)
Date:_03_/ 05 / 2025 No. of Pages: 04
Marks: 100

Final Examination (2024-25)/Re-Examination (2023-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

8) Use of Scientific calculator is allowed.

Ql Answer briefly: ; [20]
Co- 1 a. | Given. the below Image patch (I) and sobel mask along x and y direction as G, ,G,. | [05]
SO- 1 10 20 30 -1 01 —1 -2 -1
BL- 3 T= 0 50 | Gy = | 0 | Gy = 0 oO oO

70 80 90 -1 0 1 1 2 1

i. Compute gradient along x-direction with J at the center pixel =50
ii. Compute gradient along y-direction with J at the center pixel =50
ili. Compute gradient magnitude

iv. Compute gradient direction

CO-2 b. | How does the Difference of Gaussian (DoG) help in detecting key points in an} [C5]
SO- 1 image, and why is it preferred over a single Gaussian filter for feature extraction?

BL-2 ‘

Co- 3 c. | Describe the k-means segmentation algorithm and its applications. [05]
SO- 1

BL-1

Page| 1
--- page 2 ---
CO- 4 d. | Cartesian coordinates of a point are (2, 4). [05]

SO- 1,6 i) Convert it to homogeneous coordinates.
BL-3 ii) Apply scaling with S, =3 and Sy = 2, followed by translation of tx = 5 and ty
= |. Determine the Cartesian coordinates of the point after transformation.
22
iii) Is transformed point equivalent to 39] ? Justify

2

Q2a i | A self-driving car uses computer vision to detect and identify objects on the road,

Co- 1,3 such as pedestrians, other vehicles, and traffic signs. Explain how different stages of [05]

SO- 1 computer vision (low-level, mid-level, and high-level processing) contribute to

BL-3- object recognition in this scenario.

ii_| Apply averaging filter of 3 x 3 on image of size 5 x 5 given below. [05]

a) find the filtered image.
b) If edge detection filter is used on the image what would be the effect if
edge is detected with and without average filter? Describe.
[ 20 20 20 20 207

20 20 20 20 204
[= |160 160 160 160 160

160 160 160 160 160;
L160 160 160 160 1601

Q2b i | Compute Integral image from the image given in Q2 (a-ii). Justify that an integral | [05]
COo-2 image enable fast computation of filtered image in algorithms like SURF.

SO- 2

BL-3

ii | A 1024 = 1024 image is processed using the SIFT algorithm. The Difference of | [05]
Gaussian (DoG) pyramid is constructed with 4 octaves, where each octave has 5
scale levels (including the base level).
a. How many total images are generated in the DoG pyramid?
b. Ifthe determinant of the Hessian matrix at a detected keypoint is 500 and the
trace is 40, calculate the edge response ratio R. Comment whether this

keypoint will be accepted?

Q3a Consider a given 5 x 5 grayscale image. [10]
CO- 2 fo 112 2
SO- 1,6 |? 1 2 3|
T= 3 3
BL- 4
2123 4
2.2 3 4 4

Page | 2
--- page 3 ---
i. Compute the Gray-Level Co-occurrence Matrix (GLCM) by considering (1,0)
adjacency (Spatial Relationship)

ii. Compute Contrast and write its interpretation:

iii. Compute Homogeneity

iv. Compute Energy

Q3b i | The Gabor filter is widely used for texture analysis in image processing. [05]
CO-2 .

So- 1 a) Explain how the Gabor filter captures texture information in an image.

BL-2 b) Describe the effect of changing the Wavelength, Aspect ratio and orientation of

a Gabor filter on the extracted features.

CO- 2 ii_| Consider the image [05]

SO- 2 10 20 30 10 -1 “Tt 2 1
BL3 1 | 50 | n= fe 0 =2| =| 0 |
70 80 90 10 -1)° -1 -2 -1

0 0 0 0 1 0

bef 2 i} b= [ —~2 |

0 0 0 0 1 0

By using Hessian corner detection method and for a threshold 15000, determine
whether center point = 50 is a corner point?

Q4a i | Explain the difference between Gaussian Mixture Model (GMM) based background | [05]
COo- 3 subtraction and Running Average based background modeling. ;
SO- 2

BL-2

ii | A 10x10 image consists of pixels, where each pixel has 3 parameters. If 20 such | [05]
frames are processed using a Gaussian Mixture Model (GMM) for background
subtraction, and each pixel is modeled with 2 Gaussian components, how many total
parameters are required for all pixels across all frames?

Q4b Describe Meanshift algorithm and its uses. Consider the following RGB pixel vaiues | [10]
CO- 3 in a neighborhood:
SO- 2 Pixels | (R,G,B)
BL-2,4 1 120, 130, 140
2 - 125,135,145
3 110,120,130
4 100,110,120
5 200,210,220

Page |3
--- page 4 ---
Perform one iteration of mean shift and determine the updated color cluster from the
initial pixel 1 and color bandwidth (hc)=30 using Euclidian distance.

Q5a Illustrate the steps to estimate the depth of objects using stereo images. Use [10]
COo- 4 example images to explain.

SO- 1,6

BL- 4

Q5b For stereo images, [10]
Co- 1 i. Construct a diagram to show epipolar geometry and show key points and

SO- 1,6 .corresponding epipolar lines.

BL-5 ii. Consider the following fundamental matrix.

—-3 -2 20
F= 2 —7 50
10 -30 -—100
Consider that Cartesian coordinates of points on left and right images are (3, 2)
and (1,4) respectively. Evaluate epipolar lines on left and right images.

Q6a What are the essential elements required for computing the velocity vector in the [10]

CO- 3 Lucas-Kanade method? How does the method account for local variations in an

SO- 2 image? —

BL-2

Q6b For 3D world coordinates, [10]

Co- 4 i. List and explain the steps of converting world coordinate to pixel coordinate

SO- 1,6 system and function of each step in brief.

BL-1,3 ii. Illustrate the conversion of world coordinates to camera coordinates in
details.

Q7a What is an Automated Visual Inspection (AVI) system, and what are the key [10]

CO- 4 challenges associated with its implementation in industrial applications? Explain

SO- 2 with examples.

BL-2

Q7b How does object detection work in a cereal grain inspection system? What [10]

CO- 4 challenges are faced in ensuring accurate grain quality assessment? Explain. with

SO- 2 examples.

BL-2

Page | 4
````

## 2024-25 · Final + Re-Exam · Sem 7 · paper c46898c4436b

- Departments: Artificial Intelligence, Common (all branches), Data Science, Electronics and Telecommunication
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE, B TECH / CSE DATA SCIENCE (311), B TECH / EXTC, MBA TECH, MBA TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/ARTIFICIAL INTELLIGENCE/SEM-VII/COMPUTER VISION/Computer Vision, Sem-VII, Final Exam 2024-25 & Re Exam 2023-24.pdf` (+4 identical copies)
- Printed on paper: max marks: 100; exam date: 7 / 12/2024
- Text: ocr (4 pages), mean OCR confidence 87.7

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2024-2025
Program: B. Tech./ MBA Tech Stream: EXTC/CSE(DS)/AV/AIML Year: TV Semester: VII

Subject: Computer Vision Time: 3 _ hrs (lozcoanto 4 +00pm)
Date: 7 / 12/2024 No. of Pages: 04
Marks: 100

Final Examination (2024-25)/ Re-Examination (2023-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use,

a
1) Question No. 1 is compulsory. .
2) Out of remaining questions, attempt any 4 questions. ~
3) In all 5 questions to be attempted. "ey
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume suitable data if necessary.
Ql Answer briefly:
CO-5;| a | Decide the level of features (low, medium, or high) required for the following | [05]
SO-1, tasks on an image? Justify your answer. ~
BL-2 - Detection of Textures in Natural Scenes :
- Detecting Shape of Animals in an Image °
- Identifying Cup, Spoon, and Table in an Image
CO-2;| b_ | List the steps in Scale-Invariant Feature Transform (SIFT) algorithm. [05]
Ce SO-1;
BL-1
CO-2;| c | Identify the most suitable and simplest image segmentation method out of the | [05]
SO-1; following for the given scenario:
BL-5

Scenario:
You want to monitor a river to identify the number of boats and ships passing
under a bridge each day. The goal is to segment the images or video frames to
detect and count the moving objects (boats and ships) while ignoring the static
background (river and bridge).
Segmentation methods:

- K-means clustering

- Background subtraction

Write down potential benefits of the identified method.

Page 1 of 4
--- page 2 ---
[ CO-2; d_ | Investigate if the highlighted region in the image contains an edge or flat region | [05]
SO-1; or filtered region? Apply the given filter on the image and interprét the result.
BL-5 .
Filter: Image:
1 9 l 200 | 100 0 0 0
(1/16)} 2 4 2 200 | 100 0 0 0
l 2 1 200 | 100 0 0 0
200 | 100 0 0 0
200 | 100 0 0 0
Answer any four from Q2 to Q7
Q2 a | Explain scale space generation used in Scale-Invariant Feature Transform (SIFT) | [10]
CO-2: algorithm. Show how SIFT detects objects of different sizes.
SO-1; a
BL-2 =
CO-2; Identify the filters g, and Jy from the following, process the given image with | [10]
ice IJx and gy and provide the output matrices. Also, compute the magnitude and
° angle of gradients at each pixel.
Filters:
-5 0 5 -5
0 .
5
Image:
10 10 10 10 &
10 10 10 10
100 | 100 | 100 | 100
10 10 10 10
10 10 10 10
Q3 a | Use the following matrices of I, and I, to construct a Hessian matrix for the | [10]
_— CO-2; underlined center point and conclude whether the image contained edge or flat
SO-1; region or corner. (K=0.06, window size = 5 x 5, threshold = 35000)
BL-3
errs —!
Page 2. of 4

=
--- page 3 ---
7

ly:

0; 0 0 |0] 0 0} 0 0 0 | 0

0} -80 | 40 | 0] 0 0} -80 | -40 | 0 | 0

0} -40 | 120] 0] 0 0} 40 | 120°} 160 | 0

0} 0 | 160; 0] 0 0} 0 0 0 10

0}; 0 0 |0] 0 0} 0 0 0 | 0
CO-2;| b | Explain sparse and dense optical flow and list one advantage and disadvantage | [10]
SO-1; of each. Derive equation of optical flow using Lukas — Kanade method.
BL-3

Q4 a | Compare Scale-Invariant FeatureTransform (SIFT) and Speeded-Up Robust | [10]
CO-2; Features (SURF). a
SO-1; Determine an integral image of the following image. Find sum of the elements in
BL-3 _ : . .
the highlighted region using integral image.

10°} 10 | 10 | 10 | 10 | 10 | 10

20 | 20 | 20 | 20 | 20 | 20 | 20

30 | 30 30 | 30 | 30

20 | 20 -| 20 | 20 :

30 | 30 30 | 30

20 | 20 | 20 | 20 | 20 | 20 | 20

10 | 10 | 10 | 10 | 10 | 10 | 10
CO-2;| b i. Explain the computation flow (block diagram) of background subtraction [10]
SO-1; method.
BL-l ii. Explain the significance of mean, variance ,and weight of each Gaussian

curve of GMM model.
Q5 a | Brief on epipolar geometry. Let the point in the first image be x and the [10]

CO-1: corresponding point in the second image be x'. Use the following essential matrix
SO-1; F to determine if the epipolar constraint x""Ex = 0 is perfectly satisfied:
BL-3

vA 0 -1 1 4
E=|-1 3 2 ; x=|3 ; x'=12
0 -2 #1 1 1

Page 3 of 4
--- page 4 ---
»

CO-2;|} b | Normalize the following GLCM matrix and calculate its energy and dissimilarity. | [05]
SO-1;

ala 2}2]/1]}0
0}2]}/0]0
o}o]3]1
o}o]fo]i

CO-2;| c | Explain the significance of the following parameters in the designing of a 2D | [05]
SO-1; Gabor filter. Show pictorial representation to illustrate the effect increasing and

BL-2 reducing the values of these parameters on a 2D Gabor filter?
- Lambda (A) a
- Gamma (y) e
Q6 a_ | Recite the following terms with tht help of an epipolar geometry (diagram). [10]
CO-1; - Epipoles :
SO-1; - Epipolar Plane
BL-1 - Epipolar Lines
- Essential matrix
CO-1;| b | Perform the following tasks through matrix multiplication operation. [10]
SO-1; - Scale the point P = (1,2) by a factor of 3 along the x-axis and 2 along
BL-3 the y-axis using inhomogeneous (i.e*Cartesian) coordinate system.

- Rotate the point P = (2,3) by 180 degrees counterclockwise and
translate it by tx = 4 and ty = —2 using homogeneous coordinate
system.

Q7 a | Describe the role of intrinsic parameters in camera calibration. Illustrate the | [10]
CO-; process of converting camera coordinates to image coordinates using the
SO-1; computation with similar triangle.
BL-4 Compute the image coordinates for the camera coordinates (Xc, Yc, Zc) = (5, 6,

7) with the focal length f= 5.

CO- b | Provide a comprehensive overview of the critical factors in designing a quality | [10]
sui inspection system for cereal seeds/ grains.
BL-2

Page 4 of 4
````

## 2024-25 · Final + Re-Exam · Sem 12 · paper 821c6f5b8af7

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/6th YEAR/COMPUTER/Sem_12/Computer Vision/Computer Vision Batch 2024-25 Final Batch 2023-24 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 89.9

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT&
SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2024-2025
Program/s: B.Tech / MBA Tech /@TI Year: III/V/VI Semester: VI/X/XII
Stream/s : (CE/ AIDS/ CE-intg) / MBA Tech

Subject: Computer Vision Time: 03 hrs (2.00 pm to 5.00 pm)
Date:_03 / 05 / 2025 No. of Pages: 04
Marks: 100

Final Examination (2024-25)/Re-Examination (2023-24)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.
ai.
1) Question No. | is compulsory.
2) Out of remaining questions, attempt any 4 questions.
3) In all S questions to be attempted. o
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.
8) Use of Scientific calculator is allowed.

Ql Answer briefly: ; . [20]
Co- | a. | Given the below Image patch (I) and sobel mask along x and y direction as G, , Gy. | [05]
SO- 1 10 20 30 -1 0 1 —-1 -2.-1
BL- 3 T= io 50 | Gy = E 0 | ,Gy = | 0 0 0

70 80 90 -1 0 1 1 2 1

i. Compute gradient along x-direction with / at the center pixel =50
ii. Compute gradient along y-direction with / at the center pixel =50
iii. Compute gradient magnitude

iv. Compute gradient direction

¢

CO-2 b. | How does the Difference of Gaussian (DoG) help in detecting key points in an! [051
SO- 1 image, and why is it preferred over a single Gaussian filter for feature extraction?

BL-2

CO- 3 c. | Describe the k-means segmentation algorithm and its applications. [05]
SO- 1

BL-1

Page | 1
--- page 2 ---
CO- 4 d. | Cartesian coordinates of a point are (2, 4). 9 [05]
SO- 1,6 i) Convert it to homogeneous coordinates. ;
BL-3 ii) Apply scaling with Sx =3 and S, = 2, followed by translation of tx = 5 and ty
= |. Determine the Cartesian coordinates of the point after transformation.
22
iii) Is transformed point equivalent to [35] ? Justify
2
Q2a i | A self-driving car uses computer vision to detect and identify objects on the road,
Co- 1,3 such as pedestrians, other vehicles, and traffic signs. Explain how different stages of | [05]
SO- 1 computer vision (low-level, mid-level, and high-level processing) contribute to
BL-3 ° object recognition in this scenario.
ii | Apply averaging filter of 3 x 3 on image of size 5 x 5 given below. [05]
a) find the filtered image.
b) Ifedge detection filter is used on the i image what would be the effect if
edge is detected with and without average filter? Describe.
20 20 20 20 20
| 20 20 20 20 20 |
I= {160 160 160 160 160
160 160 160 160 160
L160 160 160 160 1601
Q2b i | Compute Integral image from the image given in Q2 (a-ii). Justify that an integral | [05]
CO- 2 image enable fast computation of filtered image in algorithms like SURF.
SO- 2
BL- 3

ii | A 1024 x 1024 image is processed using the SIFT algorithm. The Difference of | [05] 1,
Gaussian (DoG) pyramid is constructed with 4 octaves, where each octave has 5
scale levels (including the base level).
a. How many total images are generated in the DoG pyramid?
b. Ifthe determinant of the Hessian matrix at a detected keypoint is 500 and the
trace is 40, calculate the edge response ratio R. Comment whether this
keypoint will be accepted?

Q3a Consider a given 5 x 5 grayscale image. [10] a
CO-2 iF 1 12 2),

SO- 1,6 012 3

BL-4 i= F 0 2 3 3

boa a

Page | 2
--- page 3 ---
i. Compute the Gray-Level Co-occurrence Matrix (GLCM) by considera a, 0)
adjacency (Spatial Relationship) :

ii. Compute Contrast and write its interpretation

iii. Compute Homogeneity

iv. Compute Energy

Q3b i | The Gabor filter is widely used for texture analysis in image processing. [05]
CO- 2

SO- 1 a) Explain how the Gabor filter captures texture information in an image.

BL-2 b) Describe the effect of changing the Wavelength, Aspect ratio and orientation of

a Gabor filter on the extracted features.

COo-2 ii | Consider the image [05]
SO- 2 10 20 30 10 -1 “yt o2 1
BL3 1=|Ac 50 | n= fe 0 =| 4={0 0 |
70 80 90 1 O- -1 -1 -—-2 -1
0 0 O 0 1 0
Ixx = ; -2 i, lyy = 0 —2 |
0 O O 0 1 0

By using Hessian corner detection method and for a threshold 15000, determine
whether center point = 50 is a corner point?

Q4a i | Explain the difference between Gaussian Mixture Model (GMM) based background | [05]
Co- 3 subtraction and Running Average based background modeling.

SO- 2

BL-2

ii | A 10x10 image consists of pixels, where each pixel has 3 parameters. If 20 such | [05]
frames are processed using a Gaussian Mixture Model (GMM) for background
subtraction, and each pixel is modeled with 2 Gaussian components, how many total
parameters are required for all pixels across all frames?

Q4b Describe Meanshift algorithm and its uses. Consider the following RGB pixel vaiues | [10]
CO- 3 in a neighborhood:
SO- 2 Pixels | (R,G,B)
BL-2,4 1 120, 130, 140
2 125,135,145
3 110,120,130
4 100,110,120
5 200,210,220

Page |3
--- page 4 ---
Perform one iteration of mean shift and determine the updated color cluster fem the
initial pixel 1 and color bandwidth (hc)=30 using Euclidian distance.

Q5a Illustrate the steps to estimate the depth of objects using stereo images. Use [10]
CO- 4 example images to explain.

SO- 1,6

BL- 4

Qs5b For stereo images, [10]
Co- | i. Construct. a diagram to show epipolar geometry and show key points and

SO- 1,6 .corresponding epipolar lines.

BL-5 . | ii. Consider the following fundamental matrix.

F=|-2 -—-7 50
10 -30 -—100
Consider that Cartesian coordinates of points on left and right images are (3, 2)
and (1,4) respectively. Evaluate epipolar lines on left and right images.

[-3) -2 20 |

Q6a What are the essential elements required for computing the velocity vector in the [10]

CO- 3 Lucas-Kanade method? How does the method account for local variations in an

SO- 2 image?

BL-2

Q6b For 3D world coordinates, [10]

CO- 4 i. List and explain the steps of converting world coordinate to pixel coordinate

SO- 1,6 system and function of each step in brief.

BL-1,3 ii. Illustrate the conversion of world coordinates to camera coordinates in
details.

Q7a What is an Automated Visual Inspection (AVI) system, and what are the key [10]

CO- 4 challenges associated with its implementation in industrial applications? Explain

SO- 2 with examples.

BL-2

Q7b How does object detection work in a cereal grain inspection system? What | [10]

CO- 4 challenges are faced in ensuring accurate grain quality assessment? Explain with

SO- 2 examples.

BL-2

Page | 4
````

## 2024-25 · Final-Exam · Sem 2 · paper ea1ebce43096

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Computer Vision/QP_Computer Vision(703DB0E027)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2025
- Text: mixed (2 pages), mean OCR confidence 78.2

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Computer Vision
Date: 09 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 2 pages.
2. Question No.1 is compulsory
3. Out of the remaining questions attempt any 4 Questions.
4. In all questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
CO-   Q1
4;   a. What is Transfer Learning?   [05]
BL- 1
CO-   Q1
What are Harrcascades and What are the types of Harrcascedes used in
3;   b.   [05]
Smile Detection
BL- 3
CO-   Q1
2;   c.
What are the types of Blurring used in OpenCV   [05]
BL-
2,3
Q1
CO-   d.
1;
What is the basis of EAST text Detector?   [05]
BL-
3,6
CO-1,2,3 Q2
Explain how Object detection works
;
BL-2
CO- 2,3; Q3 How are useful and un-useful features distinguished in computer vision?
BL-2   Explain in detail
CO-   Q4
2,3,4;   How does region based CNN used in object detection
BL-1
CO- 2;   Q5 Distinguish between Instance Segmentation and Semantic Segmentation
********** 1 **********
--- page 2 ---
BL-2

CO- 2; Q6

BL-2 What is difference between Edge Detection and Contour Detection

FIC 2 I HH ar
````

## 2024-25 · Final-Exam · paper 2337591b0d1c

- Departments: Data Science
- Programmes: M TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/DATA SCIENCE/SEM II FALL SEMESTER/Computer Vision/Computer Vision Batch 2024-25 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2025
- Text: ocr (2 pages), mean OCR confidence 84.2

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANAL}
Year: I/Semester I[(Exam Year: 2024-2025) .
Subject: Computer Vision

‘Date: 09 May 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100

FINAL EXAMINATION (Acad. Year:2024-2025)

Instructions:

1. This question paper contains 2 pages.

2. Question No.1 is compulsory :

3. Out of the remaining questions attempt any 4 Questions.

4. In all questions to be attempted

5. All questions carry equal marks.

6. Answer to each new question to be started on a fresh page.

7. Figures in brackets on the right hand side indicate full marks.

8. Assume Suitable data if necessary.

CO- Q1
4; a. | What is Transfer Learning? [05]
BL- 1
CO- Q1 .
3: b What are Harrcascades and What are the types of Harrcascedes used in [05]
, “| Smile Detection
BL- 3
CO- Q1
aL © | what are the types of Blurring used in OpenCV [05]
2,3
Qi
Co- d.
cn What is the basis of EAST text Detector? [05]
3,6
OL aoe a2 Explain how Object detection works
BL-2

CO- 2,3; | Q3 {How are useful and un-useful features distinguished.in computer vision?
BL-2 Explain in detail

CO- Q4

2,3,4; How does region based CNN used in object detection

BL-1

CO- 2; Q5 | Distinguish between Instance Segmentation and Semantic Segmentation

Seg 7 dao ok aback
--- page 2 ---
BL-2

CO- 2;
BL-2

Q6

What is difference between Edge Detection and Contour Detection

SR aR 2 Rk
````

## 2024-25 · Re-Exam · Sem 6 · paper 7eb7ede8690b

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/BTech_AIDS_7056/Computer Vision/QP_Computer Vision(702AI0C017)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech Intg. (CE)
Year: III / VI/Semester VI/Semester XII(Exam Year: 2024-2025)
Subject: Computer Vision
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 2 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 4   a   In relation to epipolar geometry, explain epipolar constraint. Show how it
SO- 1,6   [05]
BL- 2   useful in matching key points.
CO- 3   b.   Explain in brief any two advantages and two limitations of the K-Means
SO- 1,6   [05]
algorithm.
BL- 5
c.   Determine the integral image for the following image.
CO- 2
SO- 1,6   [05]
BL- 4
CO- 4   d.
SO- 1,6   Explain two examples of mid-level processing.   [05]
BL- 3
a   Given the following gradient magnitude and orientation matrices, compute
the histogram of oriented gradients using 9 bins (0–180°). Determine the
HOG feature vector for the 4×4 image.
Q2
CO- 1
SO- 1, 6   [10]
BL- 5
Gradient Magnitude   Gradient orientation (Ɵ)
b   For Harris corner detector,
Q2   i) Show with example images that Harris corner detector is invariant
CO- 1   to rotation and variant to scaling   [10]
SO- 1, 6   ii) Explain the steps involved in constructing Harris matrix and using
BL- 5   corner response to determine whether the pixel is corner, edge or
flat region.
********** 1 **********
--- page 2 ---
a
Q3
CO- 2   List the steps for extracting Scale-Invariant Feature Transform (SIFT)   [10]
SO- 1, 6   features from an image, and describe key point localization in detail.
BL- 5
Q3   b
For Speeded-Up Robust Features (SURF), explain the scale space
CO- 2   generation for feature detection and justify in brief that it is computationally   [10]
SO- 1, 6
BL- 1,5   efficient.
a   Explain the Mean Shift clustering algorithm with reference to the
Q4   following aspects:
i) The working procedure of the algorithm and criteria for convergence
CO- 3   ii) Effect of large and small bandwidth   [10]
SO- 1, 6
iii) The advantages and limitations of Mean Shift
BL- 2
Support your explanation with a suitable example plots of data points
Q4   b
CO- 3   Describe how Gaussian Mixture model is used to generate background   [10]
SO- 1,6   model.
BL- 5
Q5   a
Show the concept of optical flow. Compare dense and sparse optical flow
CO- 3   [10]
SO- 1,6   with suitable example images.
BL- 4
Q5   b
CO- 3   Describe how background frame is generated using temporal average. Also   [10]
SO- 1,6   show how background subtraction is used generate foreground of the image.
BL- 5
Q6   a
Explain any five challenges of implementing a cereal grain inspection
CO- 4   [10]
SO- 1,6   system using computer vision.
BL- 2
Q6   b   Show how 2D Cartesian coordinates are converted to 3D homogeneous
CO- 4   coordinates and vice versa. Convert the point (3,4) from Cartesian to   [10]
SO- 1,6   homogeneous form. Also, determine the corresponding 2D Cartesian
BL- 5   coordinates for the homogeneous point (9,12,3).
a   Explain in brief the following:
Q7   • World coordinate system
CO- 4   • Camera coordinate system   [10]
SO- 1, 6
BL- 3   • Image coordinate system
•   Pixel coordinate system
Q7   b
Draw a labeled sketch of epipolar geometry and explain it with reference to
CO- 4   [10]
SO- 1,6   points, epipolar lines, and the essential and fundamental matrices.
BL- 3
********** 2 **********
````

## 2024-25 · Re-Exam · Sem 7 · paper be9f3bdaa146

- Departments: Data Science, Electronics and Telecommunication
- Programmes: B TECH / CSE DATA SCIENCE (311), B TECH / EXTC, MBA TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/CSE DATA SCIENCE (311)/SEM-VII/COMPUTER VISION/Computer Vision, Sem-VII, Batch 2023-24, 2024-25, Re Exam.pdf` (+2 identical copies)
- Printed on paper: max marks: 100
- Text: ocr (6 pages), mean OCR confidence 86.4

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2024-2025
Program: B. Tech./ MBA Tech Stream: EXTC/CSE(DS)/AI/AIML Year: 1V_— Semester: VII
Subject: Computer Vision
Date: _J5_/ 02 / 2025
Marks: 100

Time: 0% hrs (2pm to 5 pr )
No. of Pages: 05 ae es

Re-Examination (2023-24)/(2024-25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume suitable data if necessary.

Ql Answer briefly:

CO-1; a | Discuss four key differences in human vision and computer vision and describe | [05]
SO-1; BL-2 each in short.

CO-2; b | What are the properties of good key points (good features)? Specify any three [05]
SO-1; BL-2 with justification. :

CO-2; ¢ | Identify the most suitable image segmentation method out of the following for | [05]
SO-1; BL-S the given scenario:

Scenario:

You want to analyze satellite images of a city to monitor land use patterns. The
goal is to segment the images into different land use categories, such as
residential areas, commercial zones, parks, and water bodies.

Segmentation methods:
- K-means clustering
- Background subtraction

List potential benefits of the identified method.

Page 1of 5
--- page 2 ---
CO-2; d i. Does the highlighted region of the image below contain edge or flat |[05]

SO-1; BL-3 region or comer?
ii. Apply the given Gaussian filter on the image and interpret the result.

Filter: Image:

|e 1 1 ] 100 | 100 | 100 | 100 | 100 | 100 }100

Pye 2 ee il 100 | 100 | 100 | 100 | 100 | 100 100
(1/34) VP Bal ae al 100 | 100 | 100 | 100 | 100 | 100|100

Hele?) alee | el 0 0 0 0 0 0 | 0

yal ] 1 1 0 0 0 0 0 OF TEO

100 | 100 | 100 | 100 | 100 | 100 }100
100 | 100 | 100 } 100 | 100 | 100)100

Answer any.four from Q2 to Q7

Q2 a | Decide the level of features (low, medium, or high) required for the following [10]
CO-1: tasks on an image? Justify your answer.
SO-1; BL-5 i. Detection of mosaic patterns

ii. ~ Classification of five objects
iii, | Detection of homogeneous regions with boundaries
iv. Recognizing Facial Expressions
vy. Edge Detection
CO-2; b | Identify the filters g,, and g, from the following, process the given image with | [10]

SO-1; BL-3 gx and gy and provide the filtered image. Also, compute the magnitude of the
gradients of the image.
Filters:
-1 0 ll -i -2 -|
-2 0 2 0 0 0
-1 0 1 1 2 1
Image:

10 10 100 10 10

10 10 100 10 10

10 10 100 10 10

10 10 100 10 10

Page 2 of 5
--- page 3 ---
Q3 | a | Identify the filters g, and Jy from the following, construct Hessian matrix that [10]

CO-2; is useful in Harris corner detection at the underlined center point (window size =
SO-1; BL-3 3x3).

Filters:
1 0 -1 1 2 1
2 0 -2 0 0 0
1 0 -1 -1 -2 -1
Image

0 0 0 0 0

0 30 30 30 30

0 30 0 0 0

0 30 0 0 0

0 30 0 0 0

CO-2; b | For optical flow, answer the following: [10]
SO-1; BL-5 i. Evaluate the optical flow velocities Vx and Vy for two key points of an

object using Lukas — Kanade method. Required gradients are given in the
table below. :

Point | Gradient along x | Gradient along y | Gradient of intensity with

direction direction respect to time (di/dt)
1 1 2 -3
2 2 1 -1

ii, Also, comment on the motion of the object.

iii. State the assumptions in Lukas-Kanade method. How do image pyramids
address the assumptions?

Page 3 of 5
--- page 4 ---
Determine an integral image for the following image. Use the following box filter-| [10]

Q4 a
CO-2; to filter the image at two points that are bold and underlined.
SO-1; BL-3
Box filter: Image:
EB | ope ee ae tet ier
Bb Del Deo P|) 22
Fis les aa ee Se] 2
414i4|/4]4]4]414
51-3 Sel Baeare Boh 3- |S
D0) SF veo ieee
0 4 1 1 1 1 Lo ] 1 1 1 1 1 1 1
CO-2; b | Describe the limitations of the background subtraction method. Explain it with a [10]
SO-1; BL-2 real-world example. Justify that the Gaussian Mixture Model (GMM) address the
limitations. Explain how a fix number of Gaussian curves can be generated using
a given number of video frames.
Q5 a | Illustrate 3D to 2D perspective projection using a pinhole camera model. List the | [10]
CO-1: steps to convert 3D world coordinate system to 2D pixel coordinate system, and
SO-1; BL-1 explain conversion of a point from 3D camera coordinate system to 2D image
coordinate system in detail.
CO-3,4; |b | Discuss five key challenges faced in Automated Visual Inspection (AVI) |[10]
SO-1; BL-2 systems.
Q6 Describe the role of the fundamental matrix in it. Let the point in the first image | [10]
CO-1: be x and the corresponding point in the second image be x’. Use the following |
SO-1; BL-3 fundamental matrix to determine if the epipolar constraint x''Fx = 0 is perfectly
satisfied:
O10) 1 3)
r=[1 0 =| = [| v=}
OF 2 AI td al
CO-1; Perform the following tasks through matrix multiplication operation. [10]
SO-1; BL-3 i. Translate the point P = (2,3) by t = 4 and ty = 5 using homogeneous

coordinate system.
ii. Rotate the point P = (3,4) by 90 degrees counterclockwise using

homogeneous coordinate system.

‘ Page 4 of 5
--- page 5 ---
Q7 a | Describe the role of extrinsic parameters in camera calibration. Also, compute | [10]

CO-1; the camera coordinates for the world point (Xw, Yw, Zw) = (7, 8, 9) using He
SO-1; BL-3 following rotation (R) and translation (t) matrices. j
Oil) 5
Re— F 0 | ; t= -3|
QO Z

CO-2; b | Explain the significance of the parameters Theta (@) and Sigma (6) in the [05];

SO-1; BL-2 designing of a 2D Gabor filter. Show pictorial representation to illustrate the
effect increasing and reducing the values of these parameters on a 2D Gabor |)
filter?

CO-2; c | Construct a Gray-Level Co-occurrence matrix for the following 2-bit image and | [05]

SO-1; BL-3

calculate its contrast. Use spatial relationship as (1 30)

0 mt) 0 1

l 0 3 1

2 2 0 1

Page 5 of 5
--- page 6 ---

````

## 2023-24 · Exam not stated · Sem 6 · paper 8760b2fcb84f

- Departments: Computer Engineering, Electronics and Telecommunication
- Programmes: B TECH / COMPUTER, B TECH / EXTC, B.TECH INTEGRATED / COMPUTER, B.TECH INTEGRATED / EXTC, MBA TECH / Computer, MBA TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/VI SEMESTER/COMPUTER VISION/Computer Vision, Sem-VI, Fianal 2023-24.pdf` (+5 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27/04 /2024
- Text: ocr (4 pages), mean OCR confidence 82.3
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
_ SVKM’S NMIMS _
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS ENGINEERING/

SCHOOL OF TECHNOLOGY MANAGEMENT -
Academic Year: 2023-2024 :
Program/s: BTech Integrated/MBATech/BTech ; Year: Six/Three/Four
Stream/s: Computer Engineering/ EXTC , Semester: XII/VI/VIII
Subject: Computer Vision Time: 3 hrs (2 pm to Spm)
Date: 27/04 /2024 ; No. of Page:

Marks: 100

Final Examination

}
Instructions: Candidates should read carefully the instructions printed on the question paper aid on the we)

a of the Answer Book, which is provided for their use. ra
1) Question No. 1 is compulsory. 7
2) Out of remaining questions, attempt any 4 questions.
3) In all 5 questions to be attempted. :
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
’ 6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.
Qi Answer briefly:

a. State whether computer vision or human vision is preferable for each of the following
scenarios. If computer vision is preferable, write whether low, medium or high level
processing is used in that scenario. Justify answer.

CO-1; (i) Two images ofa person at different ages are given. Test whether same person is | [5]
nae 6 there in both the images or not.
=> (ii) An image of hundreds of red and blue balls is shown to a person fora short time.
‘He is asked to tell the number of red and blue balls.
(iii) Identify an object in an image which is pixelated.

b. Describe the role of Difference of Gaussians (DoG). Consider that an image consists of
a few cars on a road and noisy pixels. Image is blurred by Gaussian filters of standard
deviations o1, 62 and 63.

ae © Filtered image with Gaussian filters of o1 show blurred edges of cars, road and
50-6: noisy pixels. _ : [5]
BL-6

e Filtered image with Gaussian filters of 02 show blurred edges of cars and road.
Noisy pixel disappear.
e Filtered image with Gaussian filters of 03 show blurred edges of only cars.

Comment on all the combinations for DoGs for the images. Justify.
--- page 2 ---
c. | Consider the following frames of a video. Temporal median filter is used on Framed,
Frame 1 and Frame 2 to generate background frame. Calculate foreground for Frame 3.
Assume threshold = 3

1 2 3 1 2 3
1)2P3 Tepe Ta
CO-2; : :
SO-1; # 4 6 4 4 6 4 ~ | [5]
BL-4 Frame 0 Frame 1
1]/2]3°]. 373 ]3
1 2 3 10 | 10 | 10
6 6 6 5 5 5
Frame 2 Frame 3
Consider two points, (2, 3, 4) and (4, 6, 8) in homogeneous coordinate system. Projective
transformation matrix, H is given below.
a 203
CO-4; - . H=|0 4 3
SO-1; f 0 | [5]
BL3 “(i) Calculate coordinates of this point after projective transformation and its
coordinates in Cartesian coordinate system.
(ii) Compare coordinates of two points in Cartesian coordinate system
a Consider that mean shift algorithm is used for segmentation of color image.
ae (i) Demonstrate the steps of algorithm
co-; (ii) Consider an image with RGB pixel values, (10,200,5), (10,205,5), (7,196,14), [10]
SO-1; (14,206,9),. (50,100,40), (46,100,40), (50,105,40), (50,95,44) and (10, 205, 5).
BL-3 Apply mean shift algorithm for clustering. Initial point is (46, 100, 40) and use
maximum Manhatten distance between point and corresponding centroid as 20.
@ b ws
CO-1; Explain three limitations for each of computer vision and human vision. Justify each 110]
SO-1; limitation with an example
BL-1,6 ;
a List and explain the steps to determine Histogram of Gradient (HoG) feature descriptor
Q3 . for an image patch of size 128x128. ;
ae Consider an 8x8 cell in which 40 elements have gradiént magnitude, 10 and angle,.50 | [10]
BL-6 degrees. Gradient magnitude is 2 and angle is 40 degrees for remaining elements.

Construct 9-bin histogram and identify the dominant-angle for this cell.
--- page 3 ---
Consider an image given below.
(i) Construct Harris Matrix for the point highlighted with bold and underline. Use

Window size of 3x3. Required filters are given below.

Q@3 (ii) Determine corner response at this point. Assume constant, k=0.04
CO-2; : ‘ :
Si, 0 {0 |O0 |0 |0 1 10 |-1 1 J2° pa [10]
> 20 | 20 | 20.) 20 | 0 2 10 |-2 0 |0 |0
BL-6
0 {0 Jo |20|0 tbo 1a a [2 |-1
0 {0 {0 | 20/0 Filters
0 |0 {0 |20;0 .
Image
Q4 a For Scale-Invariant Feature Transform (SIFT) algorithm,
Or e List the steps and explain each step in brief [10]
BL-1 3 e Explain key point localization in details
b Consider the following image and filter.
(i) Calculate pixel value which is bold and underlined for the filtered image. Use
integral image.
(ii) How many additions and subtractions are used for the above computation?
Q4 oJololofofo fofo fo] fo jojo.
CO-2; 0;o0}0/0}/0)01010)0 0.) 0
50-1: olololojoflojojo jo} ji fi ji 141 ]1 [10]
= olololojolojoj}ojoj} ji fi fd 1j1 jl
BL-3 ojofoljolafijifiji] ji ji |i iP 1fi |i
oJ/o;/oO;oO};L}1 {iyi fi 1 ]1
ofo;o};o};i ji yl ]t yl 1 |1
@ olo;O;O}1-;1)1 4141 0. }'0
ofolo}lo fi {1 }1}i ft | } Oy} O°} 02) 0.) Oe
Image Filter
a Describe the use of Gabor filters to detect edges of an image.
Also, show the effect of change in standard deviation on filter.
Assume that a bank of 4 Gabor filters with orientations of 0°, 45°, 90° and 135° are .
Qs used to filter the following irhage. Draw the shape of Gabor filters, filtered image for
Seat each filter and addition of all the filtered ‘images: [10]

BL-3
--- page 4 ---
b | For each of the two 3-bit images given below- ee

(i) Determine Gray Level Occurrence Matrix (GLCM) with spatial relationship, (0,1)
(ii). Compute contrast and homogeneity of each image

Q5 (iti) Compare contrast of images for the given relationship and justify your answer

CO-2; 3 4 5 6 |7 3. 13 3 [3 43
SO-1,6; « 3 4 5 6 7. 4 4 rr 4 7 [10] .
BL-3,6. 3 {4 [5 |6 17 Ts (5 5 [5 [5

13 4 5 6 7 6 6 6 6 6

3 4 5 6 7 17 7 7 7 7
Image 1 . ; Image 2

Q6 a
CO-3: Explain Lucas Kanade method to determine optical flow of an object in a video. Justify [10]
oe ‘ - | the reason for not using large displacements (more than 2 pixels).

b For 3D vision,

(i) Describe 3D world point and demonstrate mapping of a point in 3D world

Q6 .
eri coordinate with image coordinate.
—— , (ii) Assume that the coordinates of a 3D camera point are (5,10,20). Compute | [10]
a, 3 P corresponding point in image coordinate system in terms of row and column
: ~ numbers. Focal length of camera =6, width and height of each pixel = 0.1 cm, size
of image is 100100
a Describe Essential and Fundamental matrices. Show the use of these matrices for
Q7 mapping points using epipolar geometry of stereo images. Consider that a point on left
CO-4; ~ | image is (200, 100,1). Compute corresponding epipolar line. Fundamental matrix is [10]
SO-1,6;
of .83 0.0 0.0 3.
: ; F=1]0.0 0.0 56
15 -30 -—10000

Q7 b . . . P ser
aca Justify the use of image rectification for searching corresponding points. Show the

; ‘steps of generating rectified images : [10]
BL-2, 6
````

## 2023-24 · Final-Exam · Sem 7 · paper 6d4cc77993a2

- Departments: Artificial Intelligence, Electronics and Telecommunication
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE, B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/ARTIFICIAL INTELLIGENCE/SEM-VII/COMPUTER VISION/Computer Vision, Sem-VII, Final Exam, A Y 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 87.2

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINE
Academic Year: 2023-2024 :

Program: B Tech Stream: Artificial Intelligence/ EXTC Year: Four Semester: VII

Subject: Computer Vision Time: 3 hrs JO AWA — | Pw)
Date: 22] \\ [re 23 No. of Pages: 5

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.
2) Out of remaining questions, attempt any 4 questions.
>) 3) In all 5 questions to be attempted.
4) All questions carry equal marks.
5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
a. Justify the following statements using examples
so (i) Human vision can perceive depth and computer vision can not (5]
BL-5 (ii) Computer vision predicts correct sizes of different objects unlike
human vision
b. | Describe Laplacian of Gaussian (LoG) in brief. Consider the following image
matrix, Gaussian filter and Laplacian filter. Determine LoG for only ong pixel of
image which is bold and underlined
5 5 5 5 5 riaidadada -1 ]-1]-1
5 5 s 5 5 rlo2to2}el1 -1/8 |-1
so? 5 [5 [5 [5 [5 ilatlalala = [-1 [-1 [5]
BL-3 5 5 5 5 5 tlololola Laplacian Filter

5 5 $ 5 5
1] r}id] 141

Gaussian Filter

Image Matrix
--- page 2 ---
ed

c. Consider that the following three frames of a video are used for generation of
background model using temporal average filter. Determine background image.
Extract foreground in the 4" frame. Use threshold = 2
2 13 13 41 2 |3 |3 13 2 1/3 |3 |2
2/2 2 2 f2 13 73 J2 2/1 |i /2
2 72 |2 12 2 13 13 |2 2 }1 1 /2
Cco-3
So-2 2/2 [2 {2 2 (2 |2 |2 2/2 12 |2 [5]
BL-2 Framel Frame2 . Frame3
2 13 13 13
2 |6 |2 |2
2 1/6 |2 /2
212 72 12
Frame 4
d. Consider a point P; = (8, 10, 2). Apply Homogeneous transformation using the
following matrix and determine projection of this point in Cartesian
coordinates. Also, determine projection of P2 = (16, 20,4) in Cartesian
Cco-4 coordinates. Compare Cartesian coordinates of these points and justify the
S02 answer. 5}
BL-2, 5
4 0 3
0 4 6
0 0 1
*
a. For a video of cricket match,
i) Interest points are identified in two consecutive frames
o ii) Edges of frames are enhanced
604 iii) Track movements of ball using background subtraction [10]
So-2 iv) Classify activities players to identify whether a player is batting or not
BL-2, 5 v) Apply K-means algorithm to segment objects on playground
For each of these tasks, identify whether it is a low level, medium level or high
"A level processing. Justify each answer in 1-2 sentences
= Q . ee
co Describe two features of Histogram of Gradients (HoG). List and explain steps in [10]
SO-1 brief for determining HoG.
BL- 1,3
--- page 3 ---
Q3 ¥
co Show that Harris corner detector identifies corners using gradients of image in X 10
SOo-1 and Y directions & lambda values. [10]
BL-2

b [10]

For Scale Invariant Feature Transform (SIFT),
(i) List the steps for key point localization.
(ii) Hessian matrix for a point at intermediate stage of key point

localization is given below.

Q3
Cco-2 10 5
SO-1 5 20
BL-5
Determine whether the given point is a corner allen or not. Assume
that value of constant, r = 10.
a [10]
Justify that Speeded up Robust Features (SURF) is faster than Scale Invariant
Feature Transform (SIFT) corner detector.
Determine second order derivative at a point (highlighted in bold and underline)
along X direction for the given image and discrete Gaussian filter. Use Integral
image for the computation.
%
a 0]0]0|0]0]0]0]0]0][0|0 |i ]1 |i |1]1]0]0
ey d/o lololololjolojojjo jo |i {1 {i [1 {1 [o Jo
BL-6 ofololololololefo}o!o ji Ji ttyl fr joe (0

010/11 |1]1 {1111010 oo Tay atatatazto fo

0 [0 | -2 | -2 | -2|-2|-2/0 |0
0 {0 |-2|-2 | -2|-2|-2}0 |0
--- page 4 ---
H

Consider that Gray Level Co-occurrence Matrix (GLCM) is used to determine [10]
texture of a 2-bit image. Assume that relationship of pixel is (0,1). J
(i) Construct GLCM and determine contrast and homogeneity of the
following image
d 1 2 3° 1/3
1 1 Z, 3 3
Q4 1 1 2 3 3
is 2 2 3 3 3
BL-6 2 2 3 3 3
0 0 0 1 2
(ii) Assume that GLCM of an image (image 1) has non zero values along the
diagonal only. GLCM of another image (image 2) has non zero values at
almost all locations. Compare contrast of these images and justify.
[10]
Q5 Explain Mean Shift algorithm with and without weighted mean to segment an
soe image. If very large and very small window sizes are used, comment on the effect
BL-2 on segmentation for each of these cases.
What is optical flow? Describe Lucas Kanade (LK) method for determining [10]
Q5 velocity vector of an object in a video. Consider that two pixels in first frame of
ee video have moved by 6 and 10 locations in the next frame. State whether LK
BL-3 method can determine velocity of these pixels. If no, suggest the solution.
[10]
Q6 Write a short note on each of the following
ie 3 (i) Difference of Gaussian (DoG)
BL-1 (ii) Image pyramid for optical flow
4
--- page 5 ---
06 b Justify the reason of using corner points as interest points. If image is rotated or [10]
co scaled to large size, what would be the effect on detection of corner poift in each
So-1 of these cases?
BL-5
a For epipolar geometry, ; [10]
Qi (i) Draw a neat and labeled diagram for the setup
Co-4 (ii) Show the use of Essential matrix for mapping points, epipoles and
tS epipolar lines
b Describe 3D world points, Camera points, image points and digital image points. [10]
Show how calibration is used for mapping 3D world points to the points in digital
Qi image.
CO-4 Assume that orientation and location of camera is not changed. If any other world
an point is to be mapped to an image point, can the same camera calibration be

used? Justify your answer.
````

## 2023-24 · Final-Exam · Sem 2 · paper afa43122a238

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM II/COMPUTER VISION/Computer Vision Batch 2023-24 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 2/5/24
- Text: ocr (2 pages), mean OCR confidence 84.3

````text
SVKMW’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & EN! GINEERING

SCHOOL OF TECHNOLOGY MANAGEMENT
Academic Year: 2023-2024

’ Program/s: M.Tech Year: I Semester: II
Stream/s ; Artificial Intelligence

Subject: Computer Vision Time: 3 hrs 2. tospa)

Date: 2/5/24 No. of Pages: 2/”

Marks: 100 . (2/

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and o
of the Answer Book, which is provided for their use.

1) All Question are compulsory .

2) Answer to each new question to be started on a fresh page.

3) Figures in brackets on the right hand side indicate full marks.
4) Assume Suitable data if necessary.

5) Open Internet Exam

6) .ipynb Notebook to be submitted

n the co’

——
ver

Qi

Answer briefly:

[20]

: a. Describe Layers of Computer Vision
CO-;SO-;|— i.’ Kernel
BL- ii. Stride
iii. | Pooling +.PTO

Pare |
--- page 2 ---
Load the data from kaggle computer vision (20)
!kaggle datasets download -d jonathanoheix/face-expression-

Q2 recognition-dataset ais 140]
CO-; SO-; a. LOAD
BL- b. CLEANING
c. VISUALISE
d.MODELING
a. Load the data from kaggle computer vision (20)
https: //www.kaggle.com/datasets/mbkinaci/fruit-
images-for-object detection
Q3 a. LOAD
CO-; SO-; b. CLEANING [40]
BL- c. VISUALISE
d. MODELING

fage2—
````

## 2023-24 · Re-Exam · Sem 7 · paper e41368eb883f

- Departments: Artificial Intelligence, Electronics and Telecommunication
- Programmes: B TECH / ARTIFICIAL INTELLIGENCE, B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/ARTIFICIAL INTELLIGENCE/SEM-VII/COMPUTER VISION/Computer Vision, Sem-VII, Year 2023-24, Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 86.1
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
[PSTME

FBR ARY
SVKM’S NMIMS F

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING

Academic Year: 2023-2024

¥

Program: B Tech Stream: Artificial Intelligence/ EXTC Year: Four Semester: VII
Subject: Computer Vision Time: 3 hrs YOAW, — (Pry
Date: OS /Feb/2024 No. of Pages: 4

Marks: 100

Re- Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

(™ 3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started ona fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
a. Consider an image showing students sitting in a class room. For each of the
following tasks, identify whether it is a low level, medium level or high level
Co processing. Justify each answer in 2-3 sentences
SO-2 (i) Identify whether it is a class room or not [5]
BL-1, 6 (ii) Classify activity of students, writing on paper or listening to teacher
(iii) Two images of the same class room are given. Identify interest points
in each image and match them.
b. | Describe Laplacian of Gaussian (LoG) in brief. Assume that LoG of an image and
LoG after applying threshold are given below. Justify why threshold has identified
dots and only one vertical line.
Cco-2
SO-2 [5]
BL-2, 6
LoG of Image LoG after applying threshold
--- page 2 ---
ae c. Explain Background Subtraction using temporal median filter considering a video

»
SO-1 which consists of 200 frames, each of size 50x50 pixels. a [5]
BL-2
d. | Assume that coordinate of a point is (3,4) in an image. Apply the given
transformation matrix] followed by transformation matrix2 on this point.
Determine transformed point in Cartesian coordinates, Identify the type of
transformation provided by each matrix.
Co-4
SO-1 2 0 0 1 Jo J5 [5]
BL-3 0 0.5 0 0 |i, | 10
0 0 1 0 10 1
Transformation matrix | Transformation matrix 2
a. List limitations of computer vision. Also, consider that an image -
o i) has noisy points which are to be reduced
ii) has horizontal lines which are to be eliminated
Co-1 . ; . {10]
SO-1 iii) get depth of object from 2D images
BL-2 Suggest filter/ algorithm/ process and explain it in brief
Q b. Consider that Histogram of Gradient (HoG) is computed for an object of an image.
8
sor List and justify each step used for computation of feature vector of HoG. Show [10]
BL-3 how HoG determines the shape of an object.
a. For given image matrix,
(i) Use Hessian detector to determine Corner Response at a pixel (béld and
underlined). Required filters are given below
(ii) List two differences between Harris and Hessian corner detectors
o—}o—fo—fo—fo—] [2 12 Jo
Q3
40 40 40 40 40 1 -2 1
co-2 0 fo |o Jo fo [10]
SO-1 0 {o [0 |o |o oj? |?
BL-3, 1 Image Matrix Filter for Lx
1 0 1
-2 0 -2
1 0 1

Filter for Ix
--- page 3 ---
b

Consider that Scale Invariant Feature Transform (SIFT) is used to identify
interest points. -
* Explain the role of orientation assignment.

* — List the steps for orientation assignment. Justify each step.

(ii) If both horizontal and vertical edges are to be removed, choose filter

parameters.

Q3 * Magnitude and orientation of points in a cell are given below. Determine [10]
CO-2 orientation of the cell. ,
SO-1
BL- 1,5 10 10 5 5 60 100 | 60 60
10 | 10 | 5 5 60 | 100 |.60 | 60
10 10 5 5 60 100 | 60 60
10 10 5 5 t 60 100 | 60 60
Magnitude Orientation in degrees
a For Speeded up Robust Features (SURF) corner detector,
(i) scale space generation uses increase in the size of filters instead of
down sampling the image. Justify.
(ii) Determine second order derivative at a point (highlighted in bold and
underline) along Y direction for the given image and discrete Gaussian
filter. Use Integral image for the computation. [10]
4: 0/0/0/0/;/0/0/0}0;0}}0 |0 }0 }0 |0 |0 |0 Jo Jo
01;0 {0 }0 }0 {0 |0 |0 /0
Cco-2 0;0/0/0/0/0;0);0)}0
1 }1 J. |-2]-2]-2}1 |1 J 1
SO-1 0/0 Jo ;2/2]2 1/0 Ifo fo
BL-6 1] 1 Ji [-2]-2]-2}1 71 J 1
0/0;0;/2;/2/2/o0};o]}o]}i fl fl | -24-2]-2]}2 f1
Ololol2t2iztiolololli {i fi [-24)-2}2]1 [1 ]1
0 {0/0 }0 }0 |0 }0 |}0 |0
07;0;/0/2/2/2/0/01/0
0/0 1/0 {0 |0 J}0 |0 |0 |0
0;0/0/0;0/;/0};0;0);0
0;0;/0/0/0/0}0;0/0 Filter
Image
b For 2D Gabor filter, list and explain various parameters. For 2D Gabor filter,
Q4 (i) Assume that an image consists of edges in vertical, horizontal, forward and
co-3 backward diagonal directions. Choose filter parameters to highlight these [10]
SO-6 stripes.
BL-1, 3, 1
--- page 4 ---
a ¥ [10]

Q5 Explain K-means algorithm for segmentation of a color image. Show how elbow
Soe method is used to determine the optimum value of K. Justify that it is not
BL-1,5 preferable to use the value of K, which is smaller/larger than the optimum value.

b Consider that Gaussian Mixture Model (GMM) using three Gaussians is used for [10]
Qs generation of background model. Assume that GMM is applied on a video of 50
Co-3 frames with each frame of size 50x50 pixels.
SO-6 (i) Explain each step in brief
= (ii) How many pixels are considered for generation of Gaussian Mixture

Model and how many models are generated for this video?

Q6 a Write short notes on the following ; [10]
C0-3,4 (i) Watershed Transform for segmentation
SO-2 (ii) Selection of corresponding points in stereo vision
BL-
Q6 ° [10]
CO-1 Explain Local and global feature descriptors. List various local descriptors and
SO-2 show the comparison of these local descriptors.
BL-3
Q7 4 Explain the steps of converting 3D world point to 2D coordinates of digital [10]
CO-4 image.
SO-6 If there is a change in location of world point, describe the effect on extrinsic and
Bide intrinsic matrices of camera and justify your answer. :
Q7 b . [10]
co-4 Describe image rectification and justify that Rectification reduces complexity of
SO-6 search for corresponding points
BL-3
````

## 2023-24 · Re-Exam · Sem 7 · paper 532e2713de64

- Departments: Electronics and Telecommunication
- Programmes: B TECH / EXTC
- Source: `02_Question_Papers/Legacy/B TECH/4TH YEAR/EXTC/Sem_07/COMPUTER VISION/Computer Networks, Sem-V, Batch 2022-23, 2023-24, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 06/02/2024
- Text: ocr (7 pages), mean OCR confidence 89.1
- 8 unreadable OCR lines (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
L

SVKM’S NMIMS ‘

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING/
SCHOOL OF TECHNOLOGY MANAGEMENT :

Academic Year: 2023-2024

Program: B Tech Year: Ill Semester: V

Stream: Artificial Intelligence

Subject: Computer Networks ; Time: 3 Hrs. (10:00am to 1:00 pm)
Date: 06/02/2024 . No. of Pages: 07
Marks: 100

ReExamination( 2023-2024)/Re-Examination ( 2022-2023)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
(of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) In all___5_ questions to be attempted. ,

4) All questions carry equal marks. :

5) Answer to each new question to be started ona fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: [20]
CO-3 ; SO- | a. Explain the need of subnet mask in subnetting. [05]
1;BL-2
b. Consider the scenario below where 4 TCP senders are connected to 4
la receivers. Senders transmit to the receiving hosts at the fastest rate possible (i.e.,
CO-4:s0 at the rate at which the bottleneck link between a server and its destination is
aor : ; . ___ | [05]
1;BL-1 operating at 100% utilization and is fairly shared among the connections passing

through that link). R = 1 Gbps and again Re is 300 Mbps and Rs is 400 Mbps and

that all four senders have data to send,
--- page 2 ---
Server-3

Server-2

Server-i Server-4

Host-2

What is the minimum value of Re that will ensure that the connections to Host-1

and Host-2 are not bottlenecked at links with capacity Rc or Re?

CO-4 ; SO-
1;BL-3

Suppose an HTTP client makes a request to the gaia.cs.umass.edu web server. The
client has never before requested a given base object, nor has it communicated
recently with the gaia.cs.umass.edu server. You can assume, however, that the
client host knows the IP address of gaia.cs.umass.edu.

Suppose also that after downloading the base file, the browser encounters a jpeg
object in the base htm! file that is stored on gaia.cs.umass.edu, and therefore makes
another GET request to gaia.cs.umass.edu for that referenced jpeg object.

How many round trip times (RTTs) are needed from when the client first makes
the request to when the base page and the jpeg file are completely downloaded,
assuming the time needed by the server to transmit the base file, or the jpeg file
into the server's link is (each) equal to 1/2 RTT and that the time needed to transmit
the HTTP GET into the client's link is zero? You should assume that persistent

HTTP 1.1 is being used. (You should take into account any TCP setup time

[05]
--- page 3 ---
required before an HTTP GET is actually sent by the client, the time needed for
9
the server to transmit the requested object, and any propagation ‘délays not

accounted for in these amounts of time.)

What are the differences between message confidentiality and message integrity?

CO-1 ; SO- Can you have confidentiality without integrity? Can you have integrity without | [05]
glee confidentiality? Justify your answer.
=
2
Q2
CO-3; SO- [10]
1;BL-3
Using Djikstra’s algorithm, calculate the shortest path from ‘w’ to all the nodes.
Show the steps used in Djikstra’s algorithm.
Suppose Client A initiates a Telnet session with Server S. At about the same time,
Client B also initiates a Telnet session with Server S. Provide possible source and
destination port numbers for
CO-3 ; SO- a. The segments sent from A to S. [5]
oes b. The segments sent from S to A.
c. If A and B are different hosts, is it possible that the source port number in the
segments from A to S is the same as that from B to S?
CO-4 ; SO- Suppose you wanted to implement a new routing protocol in the SDN contol plane. [5]
1 ;BL-2 At which layer would you implement that protocol? Explain.
The rdt3.0 protocol (also known as the alternating bit protocol) reliably transfers
data from sender to receiver over a channel that can corrupt, lose and delay (but
not reorder) packets. The rdt 3.0 sender is shown below, with the new timer
operations (the only addition beyond rdt 2.2) highlighted. If you think about it,
Q3 you’ll hopefully realize that the rdt2.2 receiver works also in the rdt 3.0 setting
nna (since it can already handle bit error and duplicates); so we don’t need a new rdt [5]

3.0 receiver. The rdt 2.2 receiver (also now the rdt 3.0 receiver) is also shown

below.

List the sequences of transitions could possibly occur as a result of an initial
--- page 4 ---
rdt_send() call at the sender (with no messages initially in the channel) , and
re
possible later message corruption and subsequent error recovery?

sndpkt = make_pkt(0, data, checksum) _( corrupt(rcvpkt) |]

Gay ‘dt_rev(revpkt)
A meen
udt_send(sndpkt)

tdt_rev(rcvpkt) start_timer
&& notcorrupt(rcvpkt)
&8& isACK(revpkt, 1)

stop_timer

5 timeout _
Shee ee send(sndpkt)
start_timer
( corrupt(revpkt) || ndpkt = make_pkt(1, data, checksum)

start_timer

&& has_seq0(revpkt)

extract (revpkt ,data)

deliver_data(data)

sndpkt=make_pkt(ACK,0,checksum) rdt_rev(revpkt) 6%
udt_send(sndpkt) (corrupt (revpkt) | |

@) see! __ (kd) 5 seq0(revpkt))
_a.™~ sndpkt=make_pkt (ACK, 0,checksum)

udt_send( sndpkt)
wt.zoimms >a, RDT 3.0 2g

(corrupt (revpkt) | | n
O fr ir
see Nes T checksum) receiver

sasgpecciterspys) NE” ‘

&& has_seql(revpkt)

rdt_rev(revpkt)
&& notcorrupt(rcvpkt)

&& en 53)
stop_timer
rdt_rcv(revpk'
ee eEtSA)

extract (revpkt data)
deliver_data(data)
sndpkt»make_pkt(ACK,1,checksum)
udt_send(sndpkt)

CO-4 ; SO-
1 ;BL-2

b. | Suppose you can access the caches in the local DNS servers of your department.
Can you propose a way to roughly determine the Web servers (outside your

department) that are most popular among the users in your department? Explain.

[5]

CO-4 ; SO-
1 ;BL-1

c. | Suppose Bob initiates a TCP connection to Trudy who is pretending to be Alice.

During the handshake, Trudy sends Bob Alice’s certificate. In what step of the TLS

handshake algorithm will Bob discover that he is not communicating with Alice?

[5]
--- page 5 ---
aa What is the purpose of the random nonces in the TLS handshake? [5]
Consider the network shown below, and assume that each node initially eae the
costs to each of its neighbors. Consider the distance-vector algorithm and show the
distance table entries at node z.
Q4
CO-1; SO- [10]
1;BL-2
° GS—_,—_-@5
Z 3 xX.
Suppose that an intruder has an encrypted message as well as the decrypted version
CO-2 ; SO- of that message. Can the intruder mount a ciphertext-only attack, a known-plaintext | [5]
1;BL-2 attack, or a chosen-plaintext attack?
1.CDNs typically adopt one of two different server placement philosophies. Name
and briefly describe them.
CO- 1; SO- 2.Besides network-related considerations such as delay, loss, and bandwidth | [5]
pie performance, there are other important factors that go into designing a CDN server
selection strategy. What are they?
Q5 If the seven-bit Hamming codeword received by a receiver is 1011001. Assuming
CO-2; $O- the even parity state, find whether the received codeword is correct or wrong. If | [10]
™ | 1;BL-3 wrong locate the bit in the error.
Given a message M = 11010110101 and a generator polynomial G(x) = x%4 + x2
CO-2 ; SO- + 1, calculate the CRC code and transmission message. If one bit of the [05]
1;BL-2 transmission message is flipped during transmission (e.g., 11010110101 changes
to 11010111101), can the receiver detect the error?
CO- 2; SO- If the data unit to be transmitted is 10101001 00111001, write the steps used at [05]
— 1;BL-3 Sender site and Receiver site for 8-bit checksum calculation.
Q6 Consider the figure below, which shows the arrival of 6 messages for transmission
a CO-4; SO- at different multiple access wireless nodes at times t = 0.3, 1.7, 1.8, 2.5, 4.2, 4.6. | [05]
1;BL-2 Each transmission requires exactly one time unit.
--- page 6 ---
i. 23 4 > 6 ¥

=0.0 1.0 2.0 13.0

t=4.0 15.0
For the pure ALOHA protocol, indicate which packets are successfully transmitted

with explanations. You can, assume that if a packet experiences a collision, a node

will not attempt a retransmission of that packet until sometime after t=5.

b. Consider the network fragment shown below. x has only two attached neighbors,
wand y. w has a minimum-cost path to destination u (not shown) of 5, and y has a
minimum-cost path to u of 6. The complete paths from w and y to u (and between

w and y) are not shown. All link costs in the network have strictly positive integer

_~
values.

ou es
ee
5 = Ya
Give x’s distance vector for destinations w, y, and u.
Give a link-cost change for either c(x, w) or c(x, y) such that x will not inform its
neighbors of a new minimum-cost path to u as a result of executing the distance-
vector algorithm. ;
co-4;s0- | & Describe polling and token-passing protocols and what are the differences between [05]
1 sBL-2 the two. .
d. I. Find the class of each address
CO-1:S0- i. 11000011 00111011 00001011 11101111 [05]
1;BL-2 ii, = 129,5.25.111
I]. Distinguish between IPv4 and IPv6 addresses.
Q7 a. Consider sending a packet from a source host to a destination host over a fixed
CO-1; S0- route. List the delay components in the end-to-end delay. Which of these delays | [5]
1;BL-1 are constant and which are variable?
CO- 4; so- b. Suppose Alice, with a Web-based e-mail account (such as Hotmail or Gmail), [5]
E ;BL-2 sends a message to Bob, who accesses his mail from his mail server using IMAP.
--- page 7 ---
é
24
Discuss how the message gets from Alice’s host to Bob’s host. Be sure to list the
roe
series of application-layer protocols that are used to move the message between the

two hosts.

CO- 4; SO- | c.

What is Selective Repeat protocol and explain its implementation? [10]
1; BL-1 : :
````

## 2023-24 · Re-Exam · Sem 12 · paper 65dbb89bd14c

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/6th YEAR/COMPUTER/Sem_12/Computer Vision/Computer Vision Batch 2023-24 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 85.9

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINE
SCHOOL OF TECHNOLOGY MANAGEMENT .
Academic Year: 2023-2024

¥

Program/s: BTech Integrated/MBA Tech/BTech/MBA Tech Year: Six/Three/Four
Stream/s: Computer Engineering/ EXTC Semester: XII/VI/VUI
Subject: Computer Vision : Time: 3 hrs (2 pm to Spm)
Date: 29. 62024 No. of Pages: 4

Marks: 100

‘Re Examination

instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi - | Answer briefly:

a. | Consider the following scenarios. Identify any of Low, Medium and High devel processing

in each of the scenarios. Justify each answer.

Cco-1 i) Video of a class room is given. Apply optical flow algorithm and track an object
g Pply op
ao (ii) Videos of a speaker and persons sitting in a room are given. Determine whether it

is a class room or not

CO : (iii) Identify interest points in an image and match these points in another image

b. | Assume that an object exists in two images and second image is rotated.

CO-2; (i) Justify with example that instead of smooth patch and edge, corner point should be
Dai 6 considered as an interest/key point for detecting the object.

(ii) List any two features of good interest points.

c. | Consider frames of a video. Temporal average filter is used on Frame0 and Framel to

generate background frame. Calculate foreground for Frame 2. Assume threshold = 2 -
CO-3; i 2 3 1 4 3 1 3 8 [5]
SO-1;
BL-4 i 2 3 3 2 3 2 3 8
4 6 4 6 6 6 6 7 10
| Frame 0 Frame 1 Frame 2
--- page 2 ---
i

Test whether points (6,4,1) and (12,8,2) lie on a line represented by (-1,.d; 2) or not.

CO-4; “ya
SO-1; Compare coordinates of these points in Cartesian coordinate system and justify your | [5]
BL-5,6 answer.
a Consider the given image, Gaussian filter and Laplacian filter.
(i) Apply filters to determine Laplacian of Gaussian (LoG) of the image for the pixels
which are bold and underlined.
(ii) Test whether these pixels are edge point are not. Assume threshold = 12
Q2 (iii) Justify the use of Gaussian filter for detection of edge points using Laplacian filter
CO-2; 10 10 10 10 1]f2]1 0 |-1 Jo [10]
SO-1;
BL-3,6 40 40 40 40 (1/16)}2 |4 | 2 -l |4 |-l
40 40 60 40 iizil 0 j|-1 |0
Gaussian Filter Laplacian Filter
10 10 10 10
Image
Q2 b ;
CO-1: List three differences for comparing Low and high level processing of computer vision. [10]
SO-1; Justify each comparison with an example.
BL-1,6
a u
Consider an image given below. Construct Hessian Matrix for the point highlighted with
bold and underline. Use Window size of 3x3. Required filters are given below.
Image
0 ;0 {0 |0 |0
20 | 20 | 20 | 20/0
G6 |0 |0 | 20/0
0 ;0 {0 |20/0
Q3 0 |0 |0 |; 20/0
CO-2; ‘ [10]
SO-1; 0 0 0 0 1 0
Bix6 I 2 1 0 5) 0
0 0 0 0 1 0
Filter for Ixx in x direction Filter for lyy in y direction
1 0 -1 1 2 i
2 0 -2 0 0 0
1 0 -1 -l -2 -1
Filter for Ix in x direction __ Filter for ly of Ix
--- page 3 ---
Q3 -
ane For Scale-Invariant Feature Transform (SIFT) algorithm, ? es
Su , * — List the steps and explain in brief the role of each step [10]
_ - + Explain the construction of scale space generation in details
Consider the following image and filter. :
(i) For the filtered image, compute the value of pixel which is bold and underlined.
Use integral image.
(ii) Evaluate the number of additions and subtractions for the above computation.
2/2}212/0/0;0);0]0
4
Q 2/2)2/2/0;0j;0]0)0
tn 2[2|2[2 [0/0 [0/0 fo {10}
BL-3 2/2)/2/2/0j)0]/0/0)0
0/0;0/0/0j)0;0}0]0
0;/0/0/0/0j)0;/0};0];0
0;0;/0/0;/0/0;0};0)]0
0/0/0/0/0j/0;0]/0]0
0/0/0/0/0j;0}0]0]0 |
Image . Filter
Q4
CO-2; Describe how Gabor filters are generated using Sinusoidal wave and Gaussian function. [10]
SO-1; Show the effect of any two parameters on the shape of Gabor filter and filtered image.
BL-2
For the given 2-bit image,
(i) Construct Gray Level Occurrence Matrix and compute contrast and homogeneity
of image. Use spatial relationship of (1,0)
Q5 (ii) Repeat the above for spatial relationship of (0,1)
co-2: (iii) Compare contrasts and homogeneity of images for the above relationships. Justify
in, your answer [10]
SO-1;
BL-36 0|0/0j/0)0
> 010 {0/040
1 {141i ]1 fi
2.12 | 2 12 42
313 [3 13 [3
Q5 For segmentation of images,
CO-3; (i) Explain the effect of windows with small and large bandwidth with examples of 110]
SO-1,6; window and images if Mean shift algorithm is used
BL-2,6 (ii) Compare K-means and mean shift algorithms. Justify with examples.
--- page 4 ---
i

Q6 a

mo
CO-3: In relation to Gaussian Mixture model, explain generation of background for a video. Use [10]
SO-1; 20 frames and three Gaussian curves.
BL-3

b For 3D vision,

(i) Demonstrate mapping of a point in 3D world coordinate with points in camera

Q6 coordinates and image coordinates. Image coordinates should be in terms of rows
CO-4; ° and columns.
SO-6; (ii) Consider that coordinates of a 3D world point are (2,4,8). Compute corresponding [10]
BL- point in camera coordinate system. Rotation and translation matrices are given
2,3,5 below.
1 01 1 mY
R=!}0 1 0 T={43
—L 0 2 6
a For stereo images,
Q7 (i) Describe epipolar geometry to map points using epipolar lines of stereo images.
CO-4: (ii) Justify the reason of utilizing epipolar constraint for mapping of interest points.
SO-1: ; (iii) Consider a point, (205, 80) on right image. Determine corresponding epipolar line | [10]
BL- in left image. Fundamental matrix is
1,5,6 . [0.0 00 2 :
F=]00 0.0 10
10 -10 -100.
Q7 b
Write short notes on
CO-4; .
5.3 (i) Depth estimation using rectified images in 3D vision [10]
“a 3 (ii) 8-point algorithm to estimate fundamental matrix ~
````

## 2022-23 · Exam not stated · Sem 6 · paper 8111c8988456

- Departments: Computer Engineering
- Programmes: MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/MBA TECH/3RD YEAR/Computer/SEM VI/COMPUETR VISION/Computer Vision_8111c89884.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 /05 / 23
- Text: ocr (2 pages), mean OCR confidence 90.4

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2022-2023

Program/s: MBA Tech. Year: III Semester: VI

Stream/s: CE

Subject: Computer Vision Time: 3 hrs. (2.00 pm. To 5.00pm.)
Date:02 /05 / 23 No. of Pages:2

Marks:100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: [20]
CO-3; SO- | (a) / [
en What is classification error and how is it calculated? Provide an example. [5]
CO-2; SO- | (b) .

What is a texel and how are they used? [5]
1,2;BL-1,2
CO-2; SO- | (c)
eae What are the advantages and disadvantages of using HOG as a feature descriptor? | [5]
CO- 3; SO- | (d) . : = ' ;
Laer Describe the concept of optical flow and how it is used for motion segmentation. | [5]
Q2 Answer below questions: [20]
a (a) What is overfitting in the context of classification? How does it impact | [10]
4 a (b) classification error and how can it be addressed?
a, i What is the Scale-Invariant Feature Transform (SIFT) algorithm and how is it used

in object recognition? [10]

Q3 Answer below questions: [20]
--- page 2 ---
(a) Explain how the choice of parameters, such as the window size and the | [10]

Soin regularization parameter, can impact the performance of the optical flow algorithm.
BL23 (b) Explain how machine learning-based methods, such as support vector machines or
deep learning, can be used for brain tumor detection. [10]
Q4 Answer below questions: [20]
C0-2,4; (a) Explain how the choice of parameters, such as the cell size and block size, can | [10]
$0-1,2; impact the performance of the HOG descriptor.
BL23 (b) How can deformable object detection be used for applications such as facial
expression recognition or object tracking? [10]
Q5 Answer below questions: [20]
(a) -| Consider the below matrix and calculate magnitude and Orientation for the point
underlined and bold. [10]
120 |20 | 89 | 96 | 122
58 | 160 | 69 | 120 | 110
cal 145 |78 | 85 | 80 | 70
BL-2,3 190 | 215 | 56 | 200 | 66
214 |97 | 45 | 102 | 45
(b) What is a gray-level co-occurrence matrix? How can they be used for texture [10]
discrimination?
Q6 Answer below questions: [20]
C0-2,3: What are the advantages and disadvantages of using an overlapping versus a non- | [10]
$0-1,2; (a) overlapping sliding window approach?
BL-1,2,3
(b) Explain the concept of feature extraction and how it is used in object recognition. | [10]
Q7 Answer below questions: [20]
C0-23; (a) How can texture features be used for tasks such as texture classification and | [10]
50-1,2; segmentation? Provide an example.
BL-1,2,3

(b) Describe the steps involved in computing the SURF descriptor for an image patch. | [10]
````

## 2022-23 · Final-Exam · Sem 2 · paper 94fbb9f28f21

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM II/COMPUTER VISION/Computer Vision Batch 2022-23 Final0001.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29/04 / 2023
- Text: ocr (1 page), mean OCR confidence 93.8

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING

Academic Year: 2022-2023 STITUTE So
Program/s: M.Tech Year‘1 Semester II aN a
Stream/s: Artificial Intelligence \
Subject: Computer Vision Time: 3 hrs @pmto 5 pm)
Date:29/04 / 2023 No. of Pages: 1

Marks: 100
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

* 1) All Questions are compulsory and All questions carry equal marks.
2) Answer to each new question to be started on a Jupyter Notebook.
3) Figures in brackets on the right hand side indicate full marks.
4) Use of Internet is not allowed. However Class Notes and PPTs are allowed.
5) Soft copy of Python Codes and Output Images needs to be submitted.
6) Input Images and Output Sample Images are provided separately in two different folders for your reference.

Question Marks

Write a program to draw an image to achieve an output as shown in

Qi 20
Question 1 Output.png (Draw any 5 shapes)

Write a program to achieve 4 different images as output that are named
Q2 as Question 2 Output 1, Output 2, Output 3, Output 4 using the 2 20

images Question 2 Horizontal Rect.png and Question 2 Vertical Rect.png

Write a program to open webcam of laptop/ desktop and use haar
cascade to detect face and eyes. (If camera doesn’t work then please use 5
Q3 0
t the image provided by the name of Question 3 Input Image.jpg and haar

cascade files are also provided in the inputs folder)

Write a Program to read the input image as Question 4 Input Image.png

and output an image where only the central corner points are detected
Q4 20

with a corner point in it as red color. The output image should be same

as Question 4 Output.png

Write a Program to read the input image Question 5 Input Image.jpg
a) Detect and Draw all Contours around all the objects in the image

b) Identify the Contour Number against every Shapes and give 1-2 lines

20

Qs explanation against every detected contour array.
c) Calculate Extend, Solidity, Equivalent Diameter contour properties for
all the shapes in the image.

d) Draw Extreme Points of all the Objects.

pe!
````

## 2022-23 · Re-Exam · Sem 6 · paper 6de6509f2975

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM VI/COMPUTER VISION/Computer Vision, Sem-VI, Year 2022-23, Batch 2021-22 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 94.6

````text
.

SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEME & ENGINEERING ° Ve
Academic Year: 2022-2023 Siig ;
Program: B. Tech Data Science Year: III Semester: VI
Subject: Computer Vision Time: 3 hrs (Ziepmto StuDpm)
Date:_20_/ 04 / 23 No. of Pages: 2
Marks: 100

Re-Examination (Batch - 2021-22)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. | is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 a. What is convolution and filtering in image processing? Explain with an example of how 5
convolution and filtering can be used to detect edges in an image.

b. What is Epipolar geometry and how is it used in multi-camera views for object tracking and 5
surveillance?

c. What is the concept of "shape from X" in computer vision, and how does it relate to estimating the 5
3D structure of a scene or object from 2D images?

d. What are the challenges and opportunities in the field of pattern analysis for computer vision, and 5
how are researchers working to overcome these challenges.

Q.2 a. Explain the concept of dimensionality reduction, and how techniques such as principal component 10
analysis (PCA) and linear discriminant analysis (LDA) are used to reduce the dimensionality of
image feature vectors?

b. How do machine learning-based algorithms such as YOLO, Faster R-CNN, and SSD improve 10
object detection accuracy in computer vision applications?

Q.3 a. How does the discrete wavelet transform (DWT) help in feature extraction for image compression 10
and denoising, and what are the applications of DWT in video processing?

b. List and explain any five challenges of multi-camera systems? 10
A multi-camera system is used to track the movement of a ball in a sports game. If the system
consists of six cameras and the ball is in the field of view of at least three cameras at any given

time, what is the minimum number of cameras required to triangulate the position of the ball in
3D space?

Page | of 2
--- page 2 ---
Q.4

Q.5

Q. 6

Q.7

Explain the Hough transform and its application in detecting straight lines in an image, and how it
is used in autonomous vehicles for lane detection?

How deep learning-based methods such as convolutional neural networks (CNNs) improve the
accuracy of motion analysis in computer vision applications? Explain with the block diagram.

Describe how does the Phong model help to estimate surface shape from reflected light, and what
are the limitations of this approach?

Explain the difference between supervised and unsupervised classification, and provide examples
of how each approach is used in image classification tasks?

How does the mean-shift algorithm work for image segmentation, and what are its key strengths
and weaknesses?

How the use of orthogonal transformations beneficial in the processing of medical images, such
as X-rays or MRIs?

Explain the role of Markov random fields (MRFs) in image segmentation.

What are artificial neural networks (ANNs), and how are they used for image classification tasks
in computer vision?

Write a short note on albedo estimation.
What is the difference between digital and analog image formation?

Explain Kanade-Lucas-Tomasi (KLT) algorithm.

Page 2 of 2

10

10

10

10

10

10
````

## 2021-22 · Final-Exam · Sem 2 · paper f2e9a75869b5

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM II/COMPUTER VISION/Computer Vision 2021-22 Final0001.pdf`
- Printed on paper: duration hours: 3; exam date: 11 April 2022
- Text: ocr (2 pages), mean OCR confidence 86.2

````text
*

SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGH

Academic Year: 2021-22

Programme: M.Tech (Artificial Intelligence) - Year: 1 ~° Semester: I
ject: ter Vision -

Subject: Compu tds ©

Date: 11 April 2022 ~ Time: 2.00 pm to 5.00 pm

Durations: 3 (hrs)
No. of Pages: _O2 _
Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.

2) Out of remaining questions, attempt any__4 _ questions.
3)Inall__5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi Answer briefly: [20]

a. If we initialize k-means clustering algorithm with same number of clusters but different starting
GO: SOs; Ble positions for centers, will algorithm always converge to same solution? QI
CO-; SO-; BL- | >: What is affine transformation? 2]
CO-;S0-; BL- | & In YOLOv3 is softmax used for class prediction? 22]
CO-; SO-; BL- d. What is Rol pooling? [2]
CO-;S0-;BL- | & Is SSD better than Faster R-CNN? [2]
co-;S0-;BL- | f What is softmax classifier in image classification? [2]
CO-; SO-; BL- | & What is basic idea of reflectance map? [2]
CO-;S0-; BL- | 5. What is spatio-temporal analysis? [2]
CO-; SO-; BL- |. bs What is difference between convolution and correlation? [2]
CO-; SO-; BL- | }: What is difference between max pooling and mean pooling? [2]
Q2 [20]

a. A SIFT descriptor for a 16 x 16 image window W is a vector of 128 numbers which can be thought
CO-; SO-; BL- of as being grouped in 16 consecutive groups of 8 numbers each. What does each group of 8 | [5]

numbers represent?

co-;S0-;Bl- | What is visual texture? ; [5]

Ve
--- page 2 ---
CO-;SO-; BL- © What is basic idea of multi object detection? [5]
CO-; SO-; BL- d. What is region merging in image segmentation? [5]
Q3 [20]
CO-; SO-; BL- | 4 What is gradient of following function at x = y = 0? (5]
2 : f(xy) = (x — 2)8 siny
CO-; SO-; BL- | b. What is meant by 2D motion field? [5]
CO-; SO-; BL- | c. How does loss function work in SSD? [5]
CO-; SO-; BL- | d. ts YOLOVS superior than YOLOv4? . [5]
Q4 (20]
cen. a.
CO-; SO-; BL- Briefly highlight differences between YOLO9000 and YOLOv4? [6]
b. coe . . sacs sata
CO-; SO-; BL- . Briefly highlight generic nature of object detection pipeline? (7]
c.
CO-; SO-; BL- Briefly highlight mean-shift segmentation? [7]
Qs [20]
CO-; SO-; BL- | a. What is meant by optical flow and how it is related to motion field? [6]
CO-; SO-; BL- | b. How deep neural networks can be used for image classification? (7)
CO-; SO-; BL- | c. What is camera calibration problem? . (7)
Q6 [20]
CO-; SO-; BL- | a. Briefly highlight hough transform in circles [6]
CO-; SO-; BL- | b. Describe briefly how conditional statistics can be used for region segmentation 17]
CO-; SO-; BL- | c. Describe how principal component analysis can be used to recognize and distinguish faces 17]
````

## 2021-22 · Re-Exam · Sem 6 · paper 464f8a388e44

- Departments: Data Science
- Programmes: B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/DATA SCIENCE/SEM VI/COMPUTER VISION/Computer Version, Sem-VI, Re-Exam, Year 2021-22.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 June 2022
- Text: ocr (2 pages), mean OCR confidence 86.7

````text
SVKM’s NMIMS 5psTM
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & EN! eens ya AR
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERI Gn

Academic Year: 2021-22

Programme: B.Tech (Data Science) Year: III Semester: VI
Subject: Computer Vision .
¢ Marks: 100 ~«
Date: 09 June 2022 Time: 2.00 pm to 5.00 pm
= Durations: 3 (Hrs)

No. of Pages: 2 _
Re-Examination (2021-22)

Po ee eee
. Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
e of the Answer Book, which is provided for their use.

1) Question No. _1 is compulsory.

2) Out of remaining questions, attempt any __4 __ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Assume Suitable data if necessary.
Ql Answer briefly: [20]
CO-; SO-; BL- * What is image classification? [2]
CO-;S0-; BL- | > What is difference between mAP and AP? [2]
CO-;S0-; BL- | ¢ Is SSD better than YOLOv1? [2]
CO-; SO-; BL: d. What is boundary detection? 2]
CO-;S0-; BL- | & Is it better to have higher FPS in object detection systems? 2]
CO-; SO-; BL- fs Can corner detection be used for image segmentation? [2]
CO-;S0-;BL- | & What is binary entropy loss? = [2]
CO-; $O-; BL- h. What is difference between erosion and dilation? 22]
CO-;SO-; BL- | i What is idea of blurring in images? [2]
CO-;S0-;BL- | J Are logistic classifier used in YOLOv3? [2]
Q2 [20]
CO-; SO-; BL- o Briefly discuss whether feature extraction is supervised or unsupervised learning (5]

ae. CO-; SO-; BL- b. In object detection what is batch normalization? [5]

CO-; SO-; BL- What are differences between classification and clustering in images? [5]

A/a
--- page 2 ---
CO-; $O-; BL- a. What are differences between affine and projective transformations? [5]
Q3 [20]
CO-; SO-; BL- | a. In SSD how are scales and aspect ratios of default boxes represented? [5]
CO-; SO-; BL- | b. Briefly discuss about texture segmentation [5]
CO-; SO-; BL- | c. Briefly discuss about line detectors in images [5]
CO-; SO-; BL- | d. Briefly discuss about linear discriminant analysis in images [5]
Qa [20]
a.
CO-; SO-; BL- What are differences between coarse grained and fine grained features in object detection? [6]
b. ' ’
CO-; SO-; BL- What are differences between LoG and DoG filters? [7]
é.
CO-; SO-; BL- What are differences between texture and region growing segmentation methods? [7]
Qs [20]
CO-; SO-; BL- | a. What are differences between graph cut and mean shift image segmentation methods? [6]
CO-; SO-; BL- | b. How can shape be identified from color, motion and edges? [7]
CO-; SO-; BL- | c. Briefly discuss about dynamic stereo motion 17]
Q6 [20]
CO-; SO-; BL- | a. What are differences between k-means and k-medoids clustering algorithms? [6]
CO-; SO-; BL- | b. Briefly discuss idea of HoG in computer {7]
CO-; SO-; BL- | c. Briefly discuss differences between YOLOv4 and YOLOv5 [7]

Ur
````

## 2019-20 · Exam not stated · Sem 1 · paper 50e160faaf26

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM I/COMPUTER VISION/Computer Vision 2019-20.pdf`
- Printed on paper: max marks: 50; exam date: 18 November 2019
- Text: ocr (1 page), mean OCR confidence 92.3

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: M.Tech (Artificial Intelligence) Year: I Semester: |

Academic Year: 2019-20
Subject: Computer Vision

Date: 18 November 2019

/

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.

2) Out of remaining questions, attempt any __1__ question.

3) In all ___2_ questions to be attempted.

4) All questions carry equal marks.

5) Figures in brackets on the right hand side indicate full marks.
6) Assume suitable data if necessary.

Ql1) Implement a car logo detector using HOG + KNN. Training and test images are provided in the folder ‘train’ and
‘test’. (Marks 50)

Q2) In the image given to you - ‘image_q2.jpg’, calculate and label all the shapes in the image. Output should be as
shown in ‘image_q2_ans.jpg’. (Marks 50)

Q3) In the image given to you - ‘passport.jpg’, detect and extract the MRZ region. Run OCR on the extracted image.
Output should be as shown in ‘passport_output.jpg’. (Marks 50)
````

## 2018-19 · Exam not stated · Sem 1 · paper e2bbf83b1124

- Departments: Artificial Intelligence
- Programmes: M TECH / ARTIFICIAL INTELLIGENT
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/ARTIFICIAL INTELLIGENT/SEM I/COMPUTER VISION/Computer Vision 2018-19.pdf`
- Printed on paper: exam date: 28 November 2018
- Text: ocr (2 pages), mean OCR confidence 95.0

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: M.Tech (Artificial Intelligence) ~~ Year: I Semester: I

Academic Year: 2018-2019 —

Subject: Computer Vision “

Date: 28 November 2018

Final-Examination _

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Attempt any 05 questions.

2) All questions carry equal marks.

3) It is open book, open notes and open google examination.

4) Some problems are subjective/theoretical and some are coding problems.
5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

7) Assume suitable data if necessary.

Q. 1) Code: Mix up the feature matching and find Homography from calib3d module to find known objects
in a complex image. (20 Marks)

(Object marked in white border — cluttered image)
--- page 2 ---
Q. 2) Subjective: The architecture and sketch for a 2-hidden layer neural network. In total it will
have 4 layers, one-input, two-hidden and one-output. Describe all the terms such as a, z,
theta/weights, activation function and delta. Include forward propagation and backward propagation
equations. (20 Marks)

Q. 3) Code: Use numpy to code the 2-hidden layer network. Solve the XOR problem using the
network. (20 Marks)

Q. 4) Code: Use feature extraction and edge detection methods to extract the outline of cars from an
input image. Input: - an image of a car, Output: - binarized image with the outline of the car.
‘ (20 Marks)

Q. 5) Code: Perform morphological transformations to morph an input image. Use transformations
such as erosion, dilation, gradients, top hat, black hat etc... (20 Marks)

(Color Image) ansfc rmed Ima e)

Q. 6) Code: Histogram backpropagation. Explain and demonstrate what Histogram backpropagation
is. Use existing code to generate images and outputs. (20 Marks)

ae
````

## 2011-12 · Exam not stated · Trim 2 · ZIP of papers · paper 206e14150bbb · COMPUTER VISION.pdf

- Departments: Information Technology
- Programmes: M TECH / I T
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/I T/TRIM II/COMPUTER VISION/M Tech I T TRIM II COMPUTER VISION.zip`
- Printed on paper: exam date: 06/02/2012
- Text: ocr (2 pages), mean OCR confidence 87.6

````text
i
‘
4

Serre ee ee _ ~~
SVBRM's Nea
Mukesh Patel School Of Technology Management & Engings#tegq <,
_ Programme: MM. Tech- 1.7. / COMPUTER Year: [ Trimester:
Academic Year : 2011-2012
Subject: COMPUTER VISION Marks: oo = 6, 32
Time \ 22.00 Bey 5.09 city
Date: 06/02/2012 Duration: W
Final - Examination

Instruction : Candidates should read carefully the instructions pririted on the question paper and
on the Answer Book, Which is provided for their use.

NB:
1. Attempt Ay Five Out of following
2. All question carry equal marks (i.¢.20)
3. Answer to each question to be started on fresh page
4, Figures to the right indicate full marks.
Q1.

a) What is gray-tone spatial dependence matrix? Explain. 20

The above image has five gray levels from 0 to 4.
1. Calculate the co-occurrence matrices for 0°, 45°, 90° and 135° with distance 1.
2. Extract the following features from the co-occurrence matrices
a. Homogeneity in image (Angular Second Moment (ASM)).
b. Contrast
c. Correlation (Presence of organize structure within the image)
J 3, Compare ile values of the above features and give conclusion about image.

Q.2.What is Image morphology? With help of appropriate examples explain Erosion, Dialation,
Opening and Closing operations in Morphological image processing? Enlist morphological

operations and Explain Hit and Miss Transform? 20
Q.3.
a. What is multiresolution processing? Explain Laplacian pyramid and Guassian pyramids
with example. 10

b. Make the Clusters for following dataset using k-mean and average linkage algorithms.
Give graphical representation and dendrogram of the clusters obtained.
Data set: <4,10> <30,20> <15,8> <24,6> <24,16> <8,4> 10

Rage i\o
--- page 2 ---
Q4.
a. Differentiate between High Boost and High Pass Filtering. 05
b. On the following image operate by following gradient masks (centre 3x3 pixels) 15
i Horizontal Sobel Operator
ii Vertical Prewitt Operator
iii Robert Operator

10/09/40 [04] 01
09/10/90 | 04! 04
40 | 90 | 100 | 09 | 04
0404/90 | 10/09
01/04/40 | 091 10

Q.5.
a. Explain the concept of morphological Watershed algorithm for segmentation with
example, Give its advantages and disadvantages 10
b. Explain all steps required to generate the walshlets Pyramid with example. 10
Q.6 20

What is panoramic view construction? what are it’s applications? List the problems in image
fusion for panoramic view construction? Enlist and elaborate similarity measures used to find
extent of overlap in image mosaicing? Write short note on column matching and block matching
techniques used in image mosaicing?

Q.7 Give the following algorithms with all steps

a. Colorization of Grayscale image using source color image 10
b. Missing Object (View) Reconstruction 10
i i 4 ane >| >.

“!
````
