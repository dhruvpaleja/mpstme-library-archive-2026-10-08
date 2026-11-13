# Computer Vision: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 8720c2b551c8

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS) - 7027
- Source: `00_Original_Downloads/2025/Semester II/76514__Final-Exam.zip :: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS) - 7027/Computer Vision/ANS_Final-Exam_Computer Vision(703DB0E027)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: M. Tech (AI)/M. Tech - DS (BA)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Computer Vision
Date: 05 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q No.   Part   Question   Model Answer / Key Points   Marks
Q1   a   What is image processing? List its common   Image processing: manipulating digital   4
CO1   objectives and explain any two types of   images using computers to improve
BL-   image processing with examples.   quality or extract info.
1,2,3   Objectives: Enhancement, Restoration,
Segmentation, Feature Extraction,
Analysis.
Enhancement: Improve
brightness/contrast (e.g., histogram
equalization).
Restoration: Recover blurred/noisy
images (e.g., Wiener filter, inpainting).
b   What is the Harris Corner Detector? Explain   Harris Corner Detector: detects corners   4
CO3   its basic principle and state three real-world   by analyzing intensity variation in all
BL-   use cases.   directions.
2,3,4   Flat region: no change in any direction.
Edge: change in one direction. Corner:
change in all directions.
Uses: Object tracking, image stitching,
3D reconstruction.
c   Define a Convolutional Neural Network   CNN: deep neural network that processes   4
CO2   (CNN). Name its key layers and explain the   images by learning spatial hierarchies of
BL-   role of Max Pooling.   features.
2,3,4,5   Key layers: Convolutional, Activation
(ReLU), Pooling, Fully Connected,
Softmax.
Max Pooling: reduces spatial dimensions
by retaining the maximum value in each
region — reduces parameters and
provides translation invariance.
********** 1 **********
--- page 2 ---
Q No.   Part   Question   Model Answer / Key Points   Marks
d   What is YOLO? State how it differs from   YOLO (You Only Look Once): single-   4
CO4   traditional two-stage object detectors like R-   stage detector treating detection as one
BL-   CNN.   regression problem.
2,3,4   R-CNN: region proposals → feature
extraction → classification (slow, ~0.02
fps).
YOLO: entire image processed in one
forward pass → grid predictions → 45
fps (real-time). Key difference: speed and
unified architecture.
Q2   a   Explain histogram equalization as an image   Histogram equalization redistributes pixel   10
CO3   enhancement technique. Describe how it   intensities to achieve uniform
BL-3,4   works, state its formula, and discuss its   distribution, improving contrast.
advantages and limitations with a real-world   Steps: compute histogram → compute
example.   CDF → map original intensities using:
s_k = (L-1) × CDF(r_k).
Advantages: automatic, no parameters,
improves low-contrast images (e.g.,
medical X-rays).
Limitations: may over-enhance noise;
does not work well when histogram is
already spread (CLAHE used instead).
b   Compare Discrete Fourier Transform (DFT)   DFT: converts spatial → frequency   10
CO3   and Fast Fourier Transform (FFT) in image   domain; O(N²) complexity. FFT: efficient
BL-   processing. Explain low-pass, high-pass, and DFT computation; O(N log N).
3,5,6   band-pass frequency filters with use cases   Low-Pass Filter: keeps low frequencies
for each.   → smoothing, noise removal (e.g.,
blurring).
High-Pass Filter: keeps high frequencies
→ sharpening, edge detection.
Band-Pass Filter: keeps specific
frequency range → pattern recognition,
texture analysis.
FFT is ~100× faster for 1024×1024
images.
Q3   a   A manufacturing company wants to   Thresholding: T=128 → pixel > T =   10
CO3   automate quality inspection of products on   white (foreground), else black. Simple,
BL-3,5   an assembly line using computer vision.   fast, effective for high contrast.
1. Which image segmentation techniques   Watershed: treats image as topographic
would you recommend for separating   surface; finds boundaries between
defective regions from the background?   catchment basins.
Explain Thresholding and Watershed   Canny Steps: (1) Gaussian smoothing (2)
Segmentation in detail.   Gradient calculation-Sobel (3) Non-
2. How would you apply the Canny Edge   maximum suppression (4) Double
Detector to identify defect boundaries?   thresholding (5) Edge tracking by
Describe its five steps.   hysteresis.
3. What challenges might arise and how   Challenges: varying lighting → use
would you address them?   adaptive thresholding; texture noise →
apply Gaussian pre-filter.
b   Explain SIFT (Scale-Invariant Feature   SIFT: detects keypoints and creates 128-   10
CO4   Transform) as a feature extraction method.   dimensional descriptor invariant to scale,
BL-   Describe why it is scale-invariant and   rotation, and illumination.
2,3,4   rotation-invariant, and compare it with   Scale-invariant: uses Gaussian scale
SURF (Speeded-Up Robust Features) in   space / DoG pyramid to detect keypoints
terms of speed, accuracy, and use cases.   at multiple scales.
********** 2 **********
--- page 3 ---
Q No.   Part   Question   Model Answer / Key Points   Marks
Rotation-invariant: assigns dominant
orientation to each keypoint.
SURF: faster using integral images; 64-
dim descriptor. Comparable accuracy.
SIFT: preferred for high-accuracy
matching. SURF: preferred for real-time
applications.
Q4   a   Explain Generative Adversarial Networks   GAN: Generator G creates fake images   10
CO4   (GANs) in detail. Describe the GAN training   from noise z; Discriminator D classifies
BL-   process, the loss functions used, and explain   real/fake.
2,3,4   two practical applications of GANs in   Training: D maximizes log(D(x)) + log(1-
computer vision.   D(G(z))); G minimizes log(1-D(G(z))).
Nash equilibrium: G produces
indistinguishable images; D outputs 0.5.
Applications: Image-to-image translation
(pix2pix — sketches to photos), Super-
resolution (SRGAN), Data augmentation
for rare classes.
b   A healthcare startup wants to improve the   Histogram Equalization: redistributes   10
CO5   quality of low-resolution chest X-ray images   intensities to improve contrast of dark X-
BL-   before feeding them into a diagnostic model.   ray regions.
3,4,5,6   1. Which image enhancement and restoration   Denoising: remove Gaussian/salt-and-
techniques would you apply (histogram   pepper noise using median filter or
equalization, denoising, deblurring)?   Gaussian blur.
Explain each.   Deblurring: Wiener filter or deep learning
2. Explain how Linear Filtering   deconvolution to restore sharpness.
(Convolution and Gaussian Filtering) helps   Gaussian Filtering: convolves image with
in pre-processing these medical images.   Gaussian kernel σ to suppress high-
3. How would GANs help in generating   frequency noise.
high-quality synthetic X-ray data to augment   GANs: conditional GAN (cGAN) can
the training dataset?   synthesize realistic X-ray images with
specific pathologies for augmentation.
Q5   a   A smart city surveillance system needs to   YOLO: single-stage, grid-based   10
CO5   detect pedestrians and vehicles in real time.   predictions; 45+ fps; slightly lower
BL-   1. Compare YOLO and SSD object detection   accuracy on small objects.
3,4,5,6   architectures — explain how each works,   SSD: multi-scale anchor boxes across
their speed vs accuracy tradeoffs.   multiple feature maps; 59 fps; better
2. Which architecture would you choose for   small object detection.
real-time camera feeds and why?   Choice: YOLO v8 for real-time (160+
3. How would you handle class imbalance in   fps), especially with GPU; SSD if better
the training dataset for rare vehicle types   accuracy on small objects needed.
(e.g., ambulances)?   Class imbalance: oversampling rare
classes, data augmentation (flip, crop,
color jitter), weighted loss function (focal
loss).
b   A hospital wants to classify skin lesion   Transfer Learning: reuses ResNet-50   10
CO4   images (benign/malignant) but has only 800   weights (trained on 1.2M ImageNet
BL-   labeled images.   images) to avoid training from scratch.
2,3,4   1. Explain Transfer Learning and why it is   Strategy: freeze Conv1–Conv4 (low-level
the most appropriate approach here.   features — edges, textures); retrain
2. Describe the fine-tuning strategy using   Conv5 + new FC layers (domain-specific
ResNet-50: which layers to freeze, which to   patterns).
retrain, and why.   Phase 2: unfreeze last blocks with very
low lr (1e-5) for end-to-end fine-tuning.
********** 3 **********
--- page 4 ---
Q No.   Part   Question   Model Answer / Key Points   Marks
3. What data augmentation techniques would   Augmentation: horizontal flip, random
you apply to expand the dataset and improve   rotation (±15°), color jitter, zoom, cutout
generalization?   — prevent overfitting on 800 samples.
Q6   a   A robotics company is developing a system   Optical Flow: measures apparent motion   10
CO3   to track moving objects on a factory floor   of pixels between frames. Assumes
BL-   using cameras.   brightness constancy.
2,3,4,5   1. Explain Optical Flow for moving object   Lucas-Kanade: sparse flow, local
description — what it measures and two   polynomial expansion around keypoints;
algorithms (Lucas-Kanade, Horn-Schunck).   fast, noisy regions problematic.
2. Explain Background Subtraction for   Horn-Schunck: dense flow, global
detecting moving objects — describe the   smoothness constraint; slower but dense
MOG2 method.   field.
3. How would you combine both approaches   Background Subtraction: MOG2 (Mixture
for robust object tracking?   of Gaussians) models background with
multiple Gaussians per pixel; foreground
= moving objects.
Combined: use MOG2 to detect regions
of interest → apply Lucas-Kanade for
tracking within detected regions.
b   A mobile app startup wants to create an   Harris: detects corners as initial interest   10
CO5   image matching feature (like Google Lens)   points (scale-insensitive). SIFT:
BL-   that can identify products from a photo.   computes 128-d descriptor at Harris
3,4,5,6   1. Explain the role of keypoint detection   keypoints — scale and rotation invariant.
using Harris Corner Detector and SIFT in   Camera Calibration: estimates intrinsic
building a product recognition pipeline.   (focal length, principal point) and
2. Explain camera calibration and pose   extrinsic (rotation, translation)
estimation — why are they important when   parameters — corrects lens distortion.
the photo angle varies?   Pose Estimation: finds camera position
3. How would feature descriptors enable   relative to scene using PnP algorithm
robust matching across different lighting and   with matched keypoints.
viewpoints?   Descriptor matching: Lowe's ratio test
filters false matches; RANSAC removes
outliers → robust to lighting/viewpoint
changes.
Q7   a   A satellite imagery company wants to detect   Pre-processing: Gaussian smoothing for   10
CO1   deforestation by comparing forest images   noise, histogram equalization for contrast
BL-   taken at different times.   normalization, radiometric correction for
3,4,6   1. Which image processing techniques   satellite sensors.
would you use for pre-processing (noise   Change detection: segment both images
removal, enhancement)?   using Watershed/K-means → extract
2. How would change detection using image   SIFT features → compare descriptors or
segmentation and feature extraction identify   difference maps to identify changed
deforested areas?   regions.
3. What CNN-based approach would you use CNN approach: Use semantic
to classify and localize deforestation at   segmentation (U-Net) to classify every
scale?   pixel as forest/non-forest; compare
segmentation masks across time periods.
Or use Siamese CNN for direct change
detection.
Scale: apply sliding window or tile-based
inference on large satellite tiles.
b   Explain the complete ML pipeline for a   Pipeline: Collect dashcam data →   10
CO3   Computer Vision task: image collection,   annotate bounding boxes (CVAT tool,
BL-2,3   preprocessing, model selection, training,   COCO format) → preprocess (resize
evaluation, and deployment.   640×640, normalize 0-1, augment) →
train YOLOv8 → evaluate → export
********** 4 **********
--- page 5 ---
Q No.   Part   Question   Model Answer / Key Points   Marks
A self-driving car company needs to deploy   ONNX → deploy on NVIDIA Jetson
a real-time pedestrian detection system.   edge device.
1. Describe the pipeline from data collection   Metrics: Precision (reduce false positives
(dashcam footage) to model deployment on — important for braking), Recall (detect
an edge device.   all pedestrians — critical for safety),
2. What evaluation metrics (precision, recall,   mAP@0.5:0.95 for overall benchmark.
mAP) would you use and why?   Model drift: monitor confidence score
3. How would you handle model drift after   distribution in production; trigger
deployment?   retraining when accuracy drops;
implement active learning pipeline.
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 618db90dcd5b

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Computer Vision/ANS_Computer Vision(703DB0E027)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: M. Tech (AI)/M. Tech - DS (BA)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Computer Vision
Date: 05 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q No.   Part   Question   Model Answer / Key Points   Marks
Q1   a   What is image processing? List its common   Image processing: manipulating digital   4
CO1   objectives and explain any two types of   images using computers to improve
BL-   image processing with examples.   quality or extract info.
1,2,3   Objectives: Enhancement, Restoration,
Segmentation, Feature Extraction,
Analysis.
Enhancement: Improve
brightness/contrast (e.g., histogram
equalization).
Restoration: Recover blurred/noisy
images (e.g., Wiener filter, inpainting).
b   What is the Harris Corner Detector? Explain   Harris Corner Detector: detects corners   4
CO3   its basic principle and state three real-world   by analyzing intensity variation in all
BL-   use cases.   directions.
2,3,4   Flat region: no change in any direction.
Edge: change in one direction. Corner:
change in all directions.
Uses: Object tracking, image stitching,
3D reconstruction.
c   Define a Convolutional Neural Network   CNN: deep neural network that processes   4
CO2   (CNN). Name its key layers and explain the   images by learning spatial hierarchies of
BL-   role of Max Pooling.   features.
2,3,4,5   Key layers: Convolutional, Activation
(ReLU), Pooling, Fully Connected,
Softmax.
Max Pooling: reduces spatial dimensions
by retaining the maximum value in each
region — reduces parameters and
provides translation invariance.
********** 1 **********
--- page 2 ---
Q No.   Part   Question   Model Answer / Key Points   Marks
d   What is YOLO? State how it differs from   YOLO (You Only Look Once): single-   4
CO4   traditional two-stage object detectors like R-   stage detector treating detection as one
BL-   CNN.   regression problem.
2,3,4   R-CNN: region proposals → feature
extraction → classification (slow, ~0.02
fps).
YOLO: entire image processed in one
forward pass → grid predictions → 45
fps (real-time). Key difference: speed and
unified architecture.
Q2   a   Explain histogram equalization as an image   Histogram equalization redistributes pixel   10
CO3   enhancement technique. Describe how it   intensities to achieve uniform
BL-3,4   works, state its formula, and discuss its   distribution, improving contrast.
advantages and limitations with a real-world   Steps: compute histogram → compute
example.   CDF → map original intensities using:
s_k = (L-1) × CDF(r_k).
Advantages: automatic, no parameters,
improves low-contrast images (e.g.,
medical X-rays).
Limitations: may over-enhance noise;
does not work well when histogram is
already spread (CLAHE used instead).
b   Compare Discrete Fourier Transform (DFT)   DFT: converts spatial → frequency   10
CO3   and Fast Fourier Transform (FFT) in image   domain; O(N²) complexity. FFT: efficient
BL-   processing. Explain low-pass, high-pass, and DFT computation; O(N log N).
3,5,6   band-pass frequency filters with use cases   Low-Pass Filter: keeps low frequencies
for each.   → smoothing, noise removal (e.g.,
blurring).
High-Pass Filter: keeps high frequencies
→ sharpening, edge detection.
Band-Pass Filter: keeps specific
frequency range → pattern recognition,
texture analysis.
FFT is ~100× faster for 1024×1024
images.
Q3   a   A manufacturing company wants to   Thresholding: T=128 → pixel > T =   10
CO3   automate quality inspection of products on   white (foreground), else black. Simple,
BL-3,5   an assembly line using computer vision.   fast, effective for high contrast.
1. Which image segmentation techniques   Watershed: treats image as topographic
would you recommend for separating   surface; finds boundaries between
defective regions from the background?   catchment basins.
Explain Thresholding and Watershed   Canny Steps: (1) Gaussian smoothing (2)
Segmentation in detail.   Gradient calculation-Sobel (3) Non-
2. How would you apply the Canny Edge   maximum suppression (4) Double
Detector to identify defect boundaries?   thresholding (5) Edge tracking by
Describe its five steps.   hysteresis.
3. What challenges might arise and how   Challenges: varying lighting → use
would you address them?   adaptive thresholding; texture noise →
apply Gaussian pre-filter.
b   Explain SIFT (Scale-Invariant Feature   SIFT: detects keypoints and creates 128-   10
CO4   Transform) as a feature extraction method.   dimensional descriptor invariant to scale,
BL-   Describe why it is scale-invariant and   rotation, and illumination.
2,3,4   rotation-invariant, and compare it with   Scale-invariant: uses Gaussian scale
SURF (Speeded-Up Robust Features) in   space / DoG pyramid to detect keypoints
terms of speed, accuracy, and use cases.   at multiple scales.
********** 2 **********
--- page 3 ---
Q No.   Part   Question   Model Answer / Key Points   Marks
Rotation-invariant: assigns dominant
orientation to each keypoint.
SURF: faster using integral images; 64-
dim descriptor. Comparable accuracy.
SIFT: preferred for high-accuracy
matching. SURF: preferred for real-time
applications.
Q4   a   Explain Generative Adversarial Networks   GAN: Generator G creates fake images   10
CO4   (GANs) in detail. Describe the GAN training   from noise z; Discriminator D classifies
BL-   process, the loss functions used, and explain   real/fake.
2,3,4   two practical applications of GANs in   Training: D maximizes log(D(x)) + log(1-
computer vision.   D(G(z))); G minimizes log(1-D(G(z))).
Nash equilibrium: G produces
indistinguishable images; D outputs 0.5.
Applications: Image-to-image translation
(pix2pix — sketches to photos), Super-
resolution (SRGAN), Data augmentation
for rare classes.
b   A healthcare startup wants to improve the   Histogram Equalization: redistributes   10
CO5   quality of low-resolution chest X-ray images   intensities to improve contrast of dark X-
BL-   before feeding them into a diagnostic model.   ray regions.
3,4,5,6   1. Which image enhancement and restoration   Denoising: remove Gaussian/salt-and-
techniques would you apply (histogram   pepper noise using median filter or
equalization, denoising, deblurring)?   Gaussian blur.
Explain each.   Deblurring: Wiener filter or deep learning
2. Explain how Linear Filtering   deconvolution to restore sharpness.
(Convolution and Gaussian Filtering) helps   Gaussian Filtering: convolves image with
in pre-processing these medical images.   Gaussian kernel σ to suppress high-
3. How would GANs help in generating   frequency noise.
high-quality synthetic X-ray data to augment   GANs: conditional GAN (cGAN) can
the training dataset?   synthesize realistic X-ray images with
specific pathologies for augmentation.
Q5   a   A smart city surveillance system needs to   YOLO: single-stage, grid-based   10
CO5   detect pedestrians and vehicles in real time.   predictions; 45+ fps; slightly lower
BL-   1. Compare YOLO and SSD object detection   accuracy on small objects.
3,4,5,6   architectures — explain how each works,   SSD: multi-scale anchor boxes across
their speed vs accuracy tradeoffs.   multiple feature maps; 59 fps; better
2. Which architecture would you choose for   small object detection.
real-time camera feeds and why?   Choice: YOLO v8 for real-time (160+
3. How would you handle class imbalance in   fps), especially with GPU; SSD if better
the training dataset for rare vehicle types   accuracy on small objects needed.
(e.g., ambulances)?   Class imbalance: oversampling rare
classes, data augmentation (flip, crop,
color jitter), weighted loss function (focal
loss).
b   A hospital wants to classify skin lesion   Transfer Learning: reuses ResNet-50   10
CO4   images (benign/malignant) but has only 800   weights (trained on 1.2M ImageNet
BL-   labeled images.   images) to avoid training from scratch.
2,3,4   1. Explain Transfer Learning and why it is   Strategy: freeze Conv1–Conv4 (low-level
the most appropriate approach here.   features — edges, textures); retrain
2. Describe the fine-tuning strategy using   Conv5 + new FC layers (domain-specific
ResNet-50: which layers to freeze, which to   patterns).
retrain, and why.   Phase 2: unfreeze last blocks with very
low lr (1e-5) for end-to-end fine-tuning.
********** 3 **********
--- page 4 ---
Q No.   Part   Question   Model Answer / Key Points   Marks
3. What data augmentation techniques would   Augmentation: horizontal flip, random
you apply to expand the dataset and improve   rotation (±15°), color jitter, zoom, cutout
generalization?   — prevent overfitting on 800 samples.
Q6   a   A robotics company is developing a system   Optical Flow: measures apparent motion   10
CO3   to track moving objects on a factory floor   of pixels between frames. Assumes
BL-   using cameras.   brightness constancy.
2,3,4,5   1. Explain Optical Flow for moving object   Lucas-Kanade: sparse flow, local
description — what it measures and two   polynomial expansion around keypoints;
algorithms (Lucas-Kanade, Horn-Schunck).   fast, noisy regions problematic.
2. Explain Background Subtraction for   Horn-Schunck: dense flow, global
detecting moving objects — describe the   smoothness constraint; slower but dense
MOG2 method.   field.
3. How would you combine both approaches   Background Subtraction: MOG2 (Mixture
for robust object tracking?   of Gaussians) models background with
multiple Gaussians per pixel; foreground
= moving objects.
Combined: use MOG2 to detect regions
of interest → apply Lucas-Kanade for
tracking within detected regions.
b   A mobile app startup wants to create an   Harris: detects corners as initial interest   10
CO5   image matching feature (like Google Lens)   points (scale-insensitive). SIFT:
BL-   that can identify products from a photo.   computes 128-d descriptor at Harris
3,4,5,6   1. Explain the role of keypoint detection   keypoints — scale and rotation invariant.
using Harris Corner Detector and SIFT in   Camera Calibration: estimates intrinsic
building a product recognition pipeline.   (focal length, principal point) and
2. Explain camera calibration and pose   extrinsic (rotation, translation)
estimation — why are they important when   parameters — corrects lens distortion.
the photo angle varies?   Pose Estimation: finds camera position
3. How would feature descriptors enable   relative to scene using PnP algorithm
robust matching across different lighting and   with matched keypoints.
viewpoints?   Descriptor matching: Lowe's ratio test
filters false matches; RANSAC removes
outliers → robust to lighting/viewpoint
changes.
Q7   a   A satellite imagery company wants to detect   Pre-processing: Gaussian smoothing for   10
CO1   deforestation by comparing forest images   noise, histogram equalization for contrast
BL-   taken at different times.   normalization, radiometric correction for
3,4,6   1. Which image processing techniques   satellite sensors.
would you use for pre-processing (noise   Change detection: segment both images
removal, enhancement)?   using Watershed/K-means → extract
2. How would change detection using image   SIFT features → compare descriptors or
segmentation and feature extraction identify   difference maps to identify changed
deforested areas?   regions.
3. What CNN-based approach would you use CNN approach: Use semantic
to classify and localize deforestation at   segmentation (U-Net) to classify every
scale?   pixel as forest/non-forest; compare
segmentation masks across time periods.
Or use Siamese CNN for direct change
detection.
Scale: apply sliding window or tile-based
inference on large satellite tiles.
b   Explain the complete ML pipeline for a   Pipeline: Collect dashcam data →   10
CO3   Computer Vision task: image collection,   annotate bounding boxes (CVAT tool,
BL-2,3   preprocessing, model selection, training,   COCO format) → preprocess (resize
evaluation, and deployment.   640×640, normalize 0-1, augment) →
train YOLOv8 → evaluate → export
********** 4 **********
--- page 5 ---
Q No.   Part   Question   Model Answer / Key Points   Marks
A self-driving car company needs to deploy   ONNX → deploy on NVIDIA Jetson
a real-time pedestrian detection system.   edge device.
1. Describe the pipeline from data collection   Metrics: Precision (reduce false positives
(dashcam footage) to model deployment on — important for braking), Recall (detect
an edge device.   all pedestrians — critical for safety),
2. What evaluation metrics (precision, recall,   mAP@0.5:0.95 for overall benchmark.
mAP) would you use and why?   Model drift: monitor confidence score
3. How would you handle model drift after   distribution in production; trigger
deployment?   retraining when accuracy drops;
implement active learning pipeline.
********** 5 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper f3064bfc5f1e

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIDS_7056/COMPUTER VISION FOR AI/ANS_COMPUTER VISION FOR AI(702AI0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (21 pages)

````text
SYNOPTICS
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
1. This question paper contains 21 pages.
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
Solution   • Harris Matrix – (1 Marks)
• Compute the Determinant of M and Trace (M)— (2 Marks)
• Compute R and Classify the feature (2 Marks)
Solution:
For a localized window:
•   ∑𝐼𝑥2 = 40
•   ∑𝐼𝑦2 = 45
• ∑𝐼𝑥𝐼𝑦= 5
•   Harris constant 𝑘= 0.04
STEP 1: Form the Harris Matrix (Structure Tensor)
∑𝐼𝑥 2   ∑𝐼𝑥𝐼𝑦   [40 5
𝑀= [   2 ] =   45]
∑𝐼𝑥𝐼𝑦   ∑𝐼𝑦   5
STEP 2: Compute the Determinant of M and Trace (M)
det (𝑀) = (40)(45) −(5)(5)
det (𝑀) = 1800 −25 = 1775
STEP 3: Compute the Trace of M
********** 1 **********
--- page 2 ---
trace(𝑀) = 40 + 45 = 85
STEP 4: Apply the Harris Response Formula
𝑅= det (𝑀) −𝑘(trace(𝑀))2
Substitute values:
𝑅= 1775 −0.04(852)
Compute 852:
852 = 7225
Now compute 0.04 × 7225:
0.04 × 7225 = 289
Final value of 𝑅:
𝑅= 1775 −289 = 1486
It is Strong Corner feature.
CO- 3   b. Two images have histogram intersection scores 0.95 (Level 0) and 1.0 (Level 1).   [05]
SO-1   Weights are 1 and 0.5 respectively. Evaluate their feature similarity using image
BL-3   pyramids techniques.
Solution   • Pyramid-based similarity formula (2 Marks)
• Multiply histogram scores with their weights ( 2 Marks)
• Compute the overall similarity (1 Marks)
Solution:
Step:1
In pyramid-based similarity:
∑𝑤𝑖⋅𝐻𝑖
𝑆=
∑𝑤𝑖
Where:
• 𝐻𝑖= Histogram intersection score at level 𝑖
• 𝑤𝑖= weight at level 𝑖
• 𝑆= overall similarity score
Step 2: Multiply histogram scores with their weights
Level 0
𝑤0 ⋅𝐻0 = 1.0 ⋅0.95 = 0.95
Level 1
𝑤1 ⋅𝐻1 = 0.5 ⋅1.0 = 0.5
Step 3: Sum weighted scores
∑𝑤𝑖𝐻𝑖= 0.95 + 0.5 = 1.45
Step 4: Sum the weights
∑𝑤𝑖= 1.0 + 0.5 = 1.5
********** 2 **********
--- page 3 ---
Step 5: Compute the overall similarity
1.45
𝑆=
1.5
𝑆= 0.9667
CO- 4   c.   In the context of Mean Shift image segmentation, consider a 1D feature space   [05]
SO- 1   with the following pixel intensity values: X = {10, 12, 15, 16, 17, 25, 30}. If the
BL-2,3   algorithm starts at an initial estimate y1 = 15 with a bandwidth h = 3.
i.   Define the set of points that fall within the kernel window.
ii.   Calculate the mean shift vector and the resulting new centre y2.
Solution   • Set of points that fall within the kernel window (2 Marks)
• Calculate the mean shift vector (3 Marks)
Solution:
•   Pixel intensity values:
𝑋= {10,12,15,16,17,25,30}
•   Initial estimate:
𝑦1 = 15
• Bandwidth:
ℎ= 3
Mean Shift uses a kernel window of radius h to find points near the current
estimate.
(i) Points within the kernel window
A point 𝑥𝑖is included if:
∣𝑥𝑖−𝑦1 ∣≤ℎ
Substitute values:
∣𝑥𝑖−15 ∣≤3
Check each point in 𝑋:
Points inside kernel window:
12,15,16,17
ii) Mean shift vector and new center 𝑦2
Step 1: Compute the mean of points in the window:
12 + 15 + 16 + 17
Mean =
4
60
Mean = = 15
4
Step 2: Compute Mean Shift Vector:
𝑚(𝑦1) = Mean −𝑦1 = 15 −15 = 0
Step 3: New center:
********** 3 **********
--- page 4 ---
𝑦2 = 𝑦1 + 𝑚(𝑦1) = 15 + 0 = 15
CO- 5   d.   List the primary functions of a Pooling Layer in a Convolutional Neural   [05]
SO- 1,6   Network (CNN) architecture and name three common types of pooling.
BL- 1,3
Solution   • Primary functions of a Pooling Layer (2 Marks)
• Three common types of pooling   (3 Marks)
Solution: The Pooling Layer (also known as a sub-sampling or down-sampling
layer) plays a critical role in reducing the spatial size of the representation to
decrease the number of parameters and computation in the network.
Primary Functions of a Pooling Layer
1. Spatial Dimensionality Reduction: By reducing the height and width of
the input volume, pooling decreases the computational load and memory
footprint for subsequent layers.
2. Invariance to Small Transformations: It helps the network become
invariant to small translations, distortions, and shifts in the input. If an
object moves by a few pixels, the pooled feature map remains relatively
similar.
3. Prevention of Overfitting: By abstracting the features and reducing the
number of parameters, it acts as a form of regularization, helping the
model generalize better to unseen data.
Feature Compression: It extracts the most dominant features (like edges or
textures) while discarding less relevant noise or background information
Three Common Types of Pooling
• Max Pooling: The most popular type. it selects the maximum value from
the region of the feature map covered by the filter. It is highly effective at
capturing prominent features like bright edges.
• Average Pooling: It calculates the average value of all pixels in the region.
This provides a smoother down-sampling but can sometimes "wash out"
fine details compared to Max Pooling.
• Minimum Pooling:
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
Solution   Each Question carry ( 2 Marks)
i.   Satellite imaging system enhances contrast and detects terrain edges
********** 4 **********
--- page 5 ---
•   Classification: Low-Level Feature Extraction
•   Explanation: This process involves pixel-level manipulations. Enhancing
contrast and detecting edges (discontinuities in intensity) are fundamental
operations that do not require any knowledge of the objects within the
scene.
ii. Security system identifies a person’s category
•   Classification: High-Level Feature Extraction
•   Explanation: Identifying a "category" (e.g., employee, intruder, or visitor)
requires semantic understanding. The system must move beyond shapes
to interpret the identity or role of the subject, which is a complex cognitive
task.
iii. Agricultural drone segments crop regions based on color/texture
•   Classification: Mid-Level Feature Extraction
•   Explanation: Segmentation based on texture or color patterns involves
grouping pixels into meaningful regions or "blobs." It is more advanced
than simple edge detection but lacks the full semantic identification of
high-level processing.
iv. A hand-gesture recognition system extracts contours of fingers before
classification .
•   Classification: Mid-Level Feature Extraction.
•   Explanation: While edges are low-level, a "contour" represents the
organized shape and boundary of a specific object part (the finger). This
structural representation acts as a bridge between raw pixels and the final
high-level gesture classification.
v. A smart classroom attendance system detects students’ faces and identifies
each individual.
•   Classification: High-Level Feature Extraction
•   Explanation: Face recognition is a classic high-level task. It involves
recognizing specific individuals by comparing complex spatial features
against a database, requiring a high degree of abstraction and semantic
labeling.
Q2   b   Given a 1D signal I = [10, 10, 10, 80, 80, 80] and two Gaussian kernels:   [10]
CO- 1   G1 = [0.2, 0.6, 0.2]
SO- 1   G2 = [0.3, 0.4, 0.3]
Calculate the Difference of Gaussian values identify the exact location of the
BL- 2,3
Zero Crossing. Justify your answer by explaining the sign change.
Solution   • Calculate the Difference of Gaussian values (2 Marks)
• identify the exact location of the Zero Crossing (2 Marks)
********** 5 **********
--- page 6 ---
• Justify your answer by explaining the sign change. (1 Marks)
.
Calculation of Convolutions (S1 and S2)
We apply the kernels to the signal where they fully overlap (from index 1 to
index 4).
Inde   Signal
S1=I∗G1   S2=I∗G2
x   Window
[10, 10,   0.2(10) + 0.6(10) +   0.3(10) + 0.4(10) +
1
10]   0.2(10) = {10}   0.3(10) = {10}
[10, 10,   0.2(10) + 0.6(10) +   0.3(10) + 0.4(10) +
2
80]   0.2(80) = {24}   0.3(80) = {31}
[10, 80,   0.2(10) + 0.6(80) +   0.3(10) + 0.4(80) +
3
80]   0.2(80) = {66}   0.3(80) = {59}
[80, 80,   0.2(80) + 0.6(80) +   0.3(80) + 0.4(80) +
4
80]   0.2(80) = {80}   0.3(80) = {80}
2. Difference of Gaussian (DoG) Calculation
The DoG is computed as S1 - S2:
• At Index 1: 10 - 10 = {0}
• At Index 2: 24 - 31 = {-7}
• At Index 3: 66 - 59 = {+7}
• At Index 4: 80 - 80 = {0}
3. Identify the Zero Crossing
• Exact Location: Between Index 2 and Index 3.
Since the values are symmetric (-7 and +7), the Zero Crossing is exactly at
Index 2.5.
Justification and Sign Change Explanation
Reason for Sign Change: The signal undergoes a sharp transition from 10 to
80.
o At Index 2: The "blurrier" kernel (G2) captures the upcoming
edge (the 80) more heavily than the sharper kernel (G1), resulting
in a negative DoG (24 - 31 = -7).
o At Index 3: The "sharper" kernel (G1) is now centered on the
high value (80) while still seeing the low value (10), whereas _2
spreads the influence of the low value more widely, making S1 >
S2. This results in a positive DoG (66 - 59 = +7).
In edge detection, a zero crossing in the DoG (or Laplacian of Gaussian)
represents the inflection point of the intensity gradient, which identifies the
precise spatial location of an edge. The transition from Negative to Positive
indicates a step-up edge (dark to bright).
********** 6 **********
--- page 7 ---
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
Solution   • Integral Image Computation and Region Summation ( 5 Marks)
• Compute the sum of pixel intensities in the bottom-right region (5
Marks)
Solution:
Resulting Integral Image S:
[1, 6, 8, 12,
4, 15, 18, 24,
6, 21, 29, 36,
7, 24, 35, 46]
2. Compute Sum of Bottom-Right 2 × 2 Region   ( 5 Marks)
The selected region consists of:
[5, 1,
3, 4]
Using the rectangular region sum formula:
Sum = S(D) + S(A) − S(B) − S(C)
Where:
D = S(4,4) = 46
A = S(2,2) = 15
B = S(2,4) = 24
C = S(4,2) = 24
Sum = 46 + 15 - 24 - 24 = 13
Verification: 5 + 1 + 3 + 4 = 13. Correct.
Q3   b   Given an image of size 128 x128 pixels, calculate the total length of the   [10]
CO- 2   Histogram of Oriented Gradients (HOG) feature vector using the following
SO- 1   configuration:
BL-2,3   •   Cell Size: 8 x 8 pixels
• Block Size: 2 x 2 cells (16 x 16 pixels)
• Block Overlap: 50% (Stride = 8 pixels)
i.   Calculate the total number of blocks across the width and height.
ii.   Compute the final length of the resulting feature vector.
iii. A pixel within a HoG cell has a calculated gradient magnitude of 25 and
an orientation angle of 55°. The histogram is constructed using 9 bins
over an unsigned 180° range, meaning each bin has a width of 20°.
********** 7 **********
--- page 8 ---
Assuming the bin intervals start from 0°, calculate how the gradient
magnitude of this pixel is distributed among the appropriate adjacent
histogram bins.
Solution
• Calculate the total number of blocks ( 2 Marks)
• Compute the final length of the resulting feature vector (4 Marks)
• calculate the gradient magnitude of this pixel (4 Marks)
i)Image Size: 128 × 128 pixels
Cell Size: 8 × 8 pixels
Block Size: 2 × 2 cells = 16 × 16 pixels
Block Overlap: 50% → Stride = 8 pixels
Formula:
Blocks = ( (Image Dimension − Block Size) / Stride ) + 1
Width:
= (128 − 16) / 8 + 1
= 112 / 8 + 1
= 14 + 1
= 15 blocks
Height:
= 15 blocks
Total blocks = 15 × 15 = 225 blocks
--------------------------------------------------
ii) Final Length of the HOG Feature Vector
--------------------------------------------------
Cells per Block = 2 × 2 = 4 cells
Bins per Cell = 9
Features per Block = 4 × 9 = 36
Total Vector Length = 225 × 36 = 8100
--------------------------------------------------
iii) Soft Voting for Orientation 55° (Magnitude = 25)
--------------------------------------------------
Orientation range = 0° to 180°
Number of bins = 9
Bin width = 20°
Bin = 0°, 20°, 40°, 60°, 80° ...
********** 8 **********
--- page 9 ---
Angle = 55° lies between centers 40° (lower) and 60° (upper).
Distances:
Soft Voting (linear interpolation):
Vote600= 25 × ( (55 − 40) / 20 ) = 25 × (15 / 20) = 18.75
Since 550is closer to 600 than 400, the share for the upper boundary is higher.
Vote400, = 25 × ( (60 − 55) / 20 ) = 25 × (5 / 20) = 6.25
Verification:
18.75 + 6.25 = 25 (correct distribution)
--------------------------------------------------
FINAL ANSWERS
--------------------------------------------------
• Total Blocks: 225
• HOG Feature Vector Length: 8100
• Soft Voting: 18.75 to 50° bin, 6.25 to 70° bin
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
Solution   I.
• Construct the KD-Tree for the descriptors (3 Marks)
• Determine the nearest matching descriptor. (2 Marks)
II.
• Working principle of the Brute-Force feature matching (2 Marks)
• Disadvantages of the Brute-Force feature matching approach
(1 Marks)
• Explain the Ratio Test   (2 Marks)
The Data Points:
• A=(5, 4, 9)
• B=(2, 8, 3)
• C=(8, 1, 7)
• D=(7, 5, 2)
• E=(1, 6, 4)
Level 0: Split by X-coordinate
********** 9 **********
--- page 10 ---
1. Sort by X: E(1), B(2), A(5), D(7), C(8).
2. Median: A(5, 4, 9).
3. Root: A.
o Left Branch (X < 5): \{E, B\}
o Right Branch (X > 5): \{D, C\}
Level 1: Split by Y-coordinate
•   Left (E, B):
1. Sort by Y: E(6), B(8).
2. Median (upper): B(2, 8, 3).
3. E(1, 6, 4) goes to the left of B (since 6 < 8).
• Right (D, C):
1. Sort by Y: C(1), D(5).
2. Median (upper): D(7, 5, 2).
3. C(8, 1, 7) goes to the left of D (since 1 < 5).
The Final Tree Structure:
• Level 0 (Root): A(5, 4, 9)
o Level 1 (Left): B(2, 8, 3)
▪ Level 2 (Left): E(1, 6, 4)
o Level 1 (Right): D(7, 5, 2)
▪ Level 2 (Left): C(8, 1, 7)
ii. Nearest Neighbor Search for Q = (3, 7, 4)   (2 Marks)
We use the tree to find the "closest" point by traversing down and then
"backtracking" if a closer point could exist on the other side of a splitting plane.
Step 1: Traversal to Leaf
1. At Root A(5, 4, 9): Q_x(3) < A_x(5). Go Left.
2. At Node B(2, 8, 3): Q_y(7) < B_y(8). Go Left.
3. At Leaf E(1, 6, 4): This is our first "Current Best."
Step 2: Calculate Distance to E
Using Euclidean distance squared (d^2):
d^2(Q, E) = (3-1)^2 + (7-6)^2 + (4-4)^2 = 2^2 + 1^2 + 0^2 = {5}
Step 3: Backtrack to B
Is B closer than E?
d^2(Q, B) = (3-2)^2 + (7-8)^2 + (4-3)^2 = 1^2 + (-1)^2 + 1^2 = {3}
New Current Best: B (Distance = sqrt{3}=1.73).
Check if we need to search the other side of B: The distance from Q to the splitting
plane Y=8 is |7-8| = 1. Since 1^2 < 3, we technically should check B's right child,
but B has no right child.
Step 4: Backtrack to Root A
Is A closer than B?
d^2(Q, A) = (3-5)^2 + (7-4)^2 + (4-9)^2 = (-2)^2 + 3^2 + (-5)^2 = 4 + 9 + 25 =
38
********** 10 **********
--- page 11 ---
Result: A is much further.
Check if we need to search the Right side of A: The distance from Q to the
splitting plane X=5 is |3-5| = 2. Since 2^2 > 3 (our current best distance squared),
we do not need to search the right branch (D, C).
Conclusion:
The nearest matchng descriptor to Q(3, 7, 4) is B(2, 8, 3).
II.Solution:
The Brute-Force (BF) Matcher takes the descriptor of one feature from the first
set (Image A) and compares it with every feature descriptor in the second set
(Image B) using a distance calculation.
1. Descriptor Comparison: It calculates the "distance" between two feature
vectors.
o For binary descriptors (like ORB or BRIEF), it typically uses
Hamming Distance.
o For gradient-based descriptors (like SIFT or SURF), it typically
uses Euclidean Distance (L_2 norm).
2. Selection: After comparing one feature from Image A against all features
in Image B, the matcher returns the one with the smallest distance as the
"best match."
Primary Disadvantages
While reliable, the Brute-Force approach has two major bottlenecks: (1 Marks)
• Computational Complexity: Because it performs an exhaustive search, the
complexity is O(N. M), where N and M are the number of features in each
image. As the number of keypoints grows, the matching time increases
exponentially.
• High False Positive Rate: The matcher is "forced" to find a match. Even
if a feature in Image A doesn't actually exist in Image B (due to occlusion
or noise), the algorithm will still pick the "least different" descriptor, often
resulting in incorrect matches.
The "Ratio Test" (Lowe's Test)   (2 Marks)
To address the issue of ambiguous or false matches, David Lowe proposed the
Ratio Test. Instead of simply taking the closest match, the algorithm looks at the
two best matches for a specific keypoint.
How it works:
1. For a descriptor in Image A, find the two closest neighbors in Image B
(m1 and m2).
2. Calculate the ratio of their distances: Ratio = distance(m1)}/distance(m2).
3. The Threshold: A match is only kept if the ratio is below a certain
threshold (commonly 0.7 or 0.8).
Why it works:
•   Distinctive Matches: If a feature is a good match, m_1 will be
significantly closer than m_2, resulting in a small ratio.
• Ambiguous Matches: If the feature is part of a repetitive pattern (like
blades of grass or windows on a building), m1 and m2 will have very
********** 11 **********
--- page 12 ---
similar distances. The ratio will be close to 1.0, and the match will be
discarded as unreliable.
Q4   b An image retrieval system uses a small vocabulary of 3 visual words. You have   [10]
CO- 3   a database of 10 reference images (N=10). The raw visual word occurrence
SO- 2   histograms for two reference images (H1, H2) and a new query image (Q) are
provided below:
BL-3,4,5
• H1: [4, 2, 4]
• H2: [5, 0, 5]
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
Solution   Determine the Term Frequency (TF) ( 1 Marks)
Calculate the final TF-IDF weighted feature vectors ( 2 Marks)
Compute the Inverse Document Frequency (IDF) (3 Marks)
Cosine Similarity on the resulting TF-IDF vectors (4 Marks)
An image retrieval system uses a vocabulary of 3 visual words. The database
contains N = 10 images.
Histograms:
- H1: [4, 2, 4]
- H2: [5, 0, 5]
- Q: [3, 4, 3]
Document frequencies (DF):
- DF1 = 10
- DF2 = 1
- DF3 = 10
i) Normalized Term Frequency (TF)
TF = count / total counts
H1 sum = 10 → TF(H1) = [0.4, 0.2, 0.4]
H2 sum = 10 → TF(H2) = [0.5, 0.0, 0.5]
Q sum = 10 → TF(Q) = [0.3, 0.4, 0.3]
********** 12 **********
--- page 13 ---
-------------------------------------------------------------
ii) Inverse Document Frequency (IDF)   (2 Marks)
-------------------------------------------------------------
IDF_i = log10(N / DF_i)
IDF1 = log10(10/10) = 0
IDF2 = log10(10/1) = 1
IDF3 = log10(10/10) = 0
IDF = [0, 1, 0]
-------------------------------------------------------------
iii) TF-IDF Feature Vectors   (3 Marks)
-------------------------------------------------------------
TF-IDF = TF × IDF
H1: [0.4, 0.2, 0.4] × [0,1,0] = [0, 0.2, 0]
H2: [0.5, 0.0, 0.5] × [0,1,0] = [0, 0.0, 0]
Q : [0.3, 0.4, 0.3] × [0,1,0] = [0, 0.4, 0]
-------------------------------------------------------------
iv) Cosine Similarity   (3 Marks)
-------------------------------------------------------------
Similarity(A,B) = (A·B) / (||A|| ||B||)
- Similarity(Q, H1)
Dot = 0.4 × 0.2 = 0.08
||Q|| = 0.4
||H1|| = 0.2
Similarity = 0.08 / (0.4 × 0.2) = 1.0
- Similarity(Q, H2)
H2 = [0,0,0] → zero vector → similarity = 0
-------------------------------------------------------------
Conclusion
-------------------------------------------------------------
H1 is the best match because both Q and H1 contain the only discriminative
word (Word 2), while H2 does not.
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
********** 13 **********
--- page 14 ---
Using the Lucas–Kanade method:
i.   Construct the matrices 𝐴= [𝐼𝑥   𝐼𝑦], 𝑏= [−𝐼𝑡]
ii.   Compute the optical flow vector u and v.
Solution   • Construct the matrices (4 Marks)
• Compute the optical flow vector u and v (6 Marks)
STEP 1: Given Gradients for 2×2 Neighborhood
-------------------------------------------------------------
Pixel | Ix | Iy | It
1   | 2   | 1   | -5
2   | 1   | 3   | -7
3   | 3   | 2   | -8
4   | 2   | 2   | -6
-------------------------------------------------------------
STEP 2: Construct Matrices A and b
-------------------------------------------------------------
A = [ 2,1,
1,3,
3,2,
2,2 ]
b = [5,
7,
8,
6]
(Note: b = -It)
-------------------------------------------------------------
STEP 3: Compute Normal Equations )
-------------------------------------------------------------
A^T A = [ [sum(Ix^2), sum(Ix Iy)],
[sum(Ix Iy), sum(Iy^2)] ]
Compute components:
- sum(Ix^2) = 2^2 + 1^2 + 3^2 + 2^2 = 18
- sum(Iy^2) = 1^2 + 3^2 + 2^2 + 2^2 = 18
- sum(Ix Iy) = 2*1 + 1*3 + 3*2 + 2*2 = 15
Thus:
A^T A = [ 18, 15,
15, 18]
Next compute A^T b:
- sum(Ix * b) = 2*5 + 1*7 + 3*8 + 2*6 = 53
- sum(Iy * b) = 1*5 + 3*7 + 2*8 + 2*6 = 54
Thus:
A^T b = [53, 54]
********** 14 **********
--- page 15 ---
STEP 4: Solve for Optical Flow (u, v)
-------------------------------------------------------------
Solve:
[18 15] [u] = [53]
[15 18] [v] [54]
Determinant:
Det = 18*18 - 15*15 = 99
Compute u:
u = (1/99)(53*18 - 15*54)
= (1/99)(954 - 810)
= 144/99 ≈ 1.4545
Compute v:
v = (1/99)(18*54 - 15*53)
= (1/99)(972 - 795)
= 177/99 ≈ 1.7879
-------------------------------------------------------------
FINAL RESULT: Optical Flow Vector
-------------------------------------------------------------
u ≈ 1.45
v ≈ 1.79
This represents the horizontal (u) and vertical (v) motion shared by pixels in the
2×2 neighborhood..
Q5   b   I. Given a 1D dataset X = {5, 12, 18, 25, 30, 45, 50}. You are asked to perform   [10]
CO- 4   K-means clustering (K=2) with initial centroids C1 = 15 and C2 = 40. Perform 1
SO- 1   iteration and determine the new cluster assignments and updated centroids.
II. Compare the Mean Shift algorithm with K-means clustering for image
BL-3,4,5
segmentation. Which is more suitable when the number of objects in an image is
unknown.
Soluitio   I.
n   Determine the new cluster assignments (3 Marks)
Updated centroids   (2 Marks)
II.
Compare the Mean Shift algorithm with K-means clustering (5 Marks)
Solution:
i) K-means Clustering (K = 2)
Dataset: X = {5, 12, 18, 25, 30, 45, 50}
Initial centroids: C1 = 15, C2 = 40
Step 1: Assign each point to the nearest centroid
Distance from C1=15 and C2=40:
5 → C1
12 → C1
18 → C1
25 → C1
30 → C2
45 → C2
50 → C2
********** 15 **********
--- page 16 ---
Clusters:
Cluster 1: {5,12,18,25}
Cluster 2: {30,45,50}
Step 2: Update Centroids
C1_new = (5+12+18+25)/4 = 15
C2_new = (30+45+50)/3 = 41.67
Updated centroids:
C1 = 15, C2 ≈ 41.67
--------------------------------------------------
ii) K-means vs Mean Shift for Image Segmentation
K-means:
- Requires number of clusters (K) to be known.
- Uses fixed centroids, iterative optimization.
- Not suitable when number of objects is unknown.
Mean Shift:
- Does NOT require specifying number of clusters.
- Automatically finds number of modes in data.
- Better for images with unknown number of segments.
Conclusion:
Mean Shift is more suitable when the number of objects in an image is
unknown.
Q6   a   I. Differentiate between SIFT, SURF, and HoG based on the following four   [10]
CO- 2,3   technical criteria:
SO- 1
BL-3,4,5   • Invariance to scale and rotation.
• Computational efficiency/speed.
• Typical descriptor dimensionality.
• Primary application domain (e.g., global object detection vs. local point
matching).
II. Given a simplified visual codebook with K = 2 cluster centers and an image
with 3 local feature descriptors (all in 2-dimensional space), Compute the final
L2-normalized Vector of Locally Aggregated Descriptors (VLAD) vector for the
image. Consider the following cluster center and Image descriptor:
• Cluster Centers (Codebook): C1 = (1, 1) and C2 = (5, 5)
• Image Descriptors: X1 = (2, 1), X2 = (1, 2), and X3 = (6, 4)
Solution   Differentiate between SIFT, SURF, and HoG (4 Marks)
Vector of Locally Aggregated Descriptors (VLAD) (6 Marks)
Solution :
1. Invariance to Scale and Rotation   (4 Marks)
- SIFT: Fully invariant to scale and rotation due to Difference of Gaussian
pyramid and orientation assignment.
- SURF: Approximate scale and rotation invariance using Hessian-based
detectors and Haar-wavelet responses.
- HoG: Not scale-invariant unless multi-scale processing is applied; not rotation
********** 16 **********
--- page 17 ---
invariant.
2. Computational Efficiency / Speed
- SIFT: Slowest; uses floating‑point operations.
- SURF: Faster than SIFT due to integral images and box filters.
- HoG: Fast and efficient; simple gradient operations.
3. Typical Descriptor Dimensionality
- SIFT: 128‑dimensional.
- SURF: 64‑dimensional.
- HoG: Variable; typically between 36–81 per block.
4. Application Domain
- SIFT: Local feature matching, image stitching.
- SURF: Real-time matching, tracking.
- HoG: Global object detection (e.g., pedestrian detection).
ii) VLAD Computation (K = 2)   (6 Marks)
Cluster Centres:
C1 = (1,1)
C2 = (5,5)
Descriptors:
X1 = (2,1)
X2 = (1,2)
X3 = (6,4)
Step 1: Assign descriptors to nearest centre
Distance(X1,C1)=1 → C1
Distance(X2,C1)=1 → C1
Distance(X3,C2)=√2 → C2
Step 2: Compute Residuals
Cluster 1 residuals:
(X1 - C1) = (1,0)
(X2 - C1) = (0,1)
Sum = (1,1)
Cluster 2 residuals:
(X3 - C2) = (1,-1)
Step 3: Concatenate VLAD vector
VLAD = [1,1, 1,-1]
Step 4: L2 Normalize
||VLAD|| = sqrt(1^2 + 1^2 + 1^2 + (-1)^2) = 2
Normalized VLAD = [0.5, 0.5, 0.5, -0.5]
Q6   b   Convolutional Neural Network (CNN) designed for grayscale image processing.   [10]
CO- 5   The architecture is defined as follows:
SO- 2   Input Image: 64 × 64 × 1
BL-3   Layer 1: Conv1
• Kernel size: 5 × 5
• Number of filters: 16
********** 17 **********
--- page 18 ---
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
Solution   Solution:
i.   Determine the output shapes (5 Marks)
ii.   number of Trainable Parameters (5 Marks)
Output Size = (W - K + 2P)/S + 1
Where W is Input Size, K is Kernel Size, P is Padding, and S is Stride.
Output Shape (Height × Width × Depth)
1. Input Image: 64 x 64 x 1
2. Layer 1 (Conv1): * H_{out} = {64 - 5 + 0}/{1} + 1 = 60
o Shape: {60 x 60 x 16}
3. Layer 2 (MaxPool1): * H_{out} = {60/2) = 30
o Shape: {30 x 30 x 16}
4. Layer 3 (Conv2): * H_{out} = {30 - 3 + 2(1)}/{2} + 1 = 29/2 + 1 = 15
o Shape: {15 x 15 x 32}
5. Layer 4 (FC1): * Flattened Input: 15 x 15 x 32 = 7,200
o Shape: {1 x 1 x 128} (or simply 128 nodes)
6. Output Layer: * Shape: {1 x 1 x 5} (or 5 nodes)
ii. Trainable Parameters
The number of parameters in a Conv layer is calculated as: Params = {Kernel
Height} x {Kernel Width} x {Input Depth}) + 1] x {Number of Filters}
(The +1 represents the bias term for each filter)
• Layer 1 (Conv1): * [(5 x 5 x 1) + 1] x 16 = 26 x 16 = {416}
• Layer 2 (MaxPool1): * Pooling layers have no trainable parameters.
Total: 0
• Layer 3 (Conv2): * [(3 x 3 x 16) + 1] x 32 = (144 + 1) x 32 = {4,640}
• Layer 4 (FC1): * Each of the 128 nodes connects to all 7,200 inputs,
plus 128 biases.
o (7,200 x 128) + 128 = {921,728}
********** 18 **********
--- page 19 ---
• Output Layer: * (128 x 5) + 5 = {645}
Layer   Output Shape   Trainable Parameters
Input   64 x 64 x 1   0
Conv1   60 x 60 x 16   416
MaxPool1   30 x 30 x 16   0
Conv2   15 x 15 x 32   4,640
FC1   128   921,728
Softmax   5   645
Total   -   927,429
Q7   a   Explain the limitations of Selective Search used in R-CNN and Fast R-CNN. How   [10]
CO- 5   does Faster R-CNN overcome these using Region Proposal Networks?
SO- 2
BL-2,4
Soution   Limitations of Selective Search   (5 Marks)   [10]
How Faster R-CNN Overcomes Limitations of Selective Search (5 Marks)
Solution:
Limitations of Selective Search   (5 Marks)
Selective Search is a "traditional" computer vision algorithm that groups pixels
based on color, texture, size, and shape compatibility to identify potential object
locations (Region Proposals).
1. Computational Inefficiency: Selective Search is a CPU-based algorithm.
While the rest of the CNN (convolutional layers) runs on the GPU,
Selective Search creates a massive lag because the GPU must wait for the
CPU to finish generating proposals.
2. Fixed Heuristics: It relies on hand-crafted features (like color histograms).
These rules are static and do not "learn" from the data, meaning it might
suggest thousands of irrelevant boxes that the network then has to process.
********** 19 **********
--- page 20 ---
3. High Latency: In a standard R-CNN, Selective Search takes
approximately 2 seconds per image to generate ~2,000 proposals. This
makes real-time object detection impossible.
How Faster R-CNN Overcomes Limitations of Selective Search
Faster R-CNN introduced the Region Proposal Network (RPN), which
completely replaces Selective Search. The key innovation is that the RPN is a
fully convolutional network that shares the same feature map as the detection
network.
1. Shared Convolutional Features
Instead of running a separate algorithm on the raw image, the RPN takes the
feature map produced by the last shared convolutional layer. This means proposal
generation happens at "near-zero" extra cost because the heavy lifting (feature
extraction) is already done for the detector.
2. Anchor Boxes
To handle objects of different scales and aspect ratios without sliding windows
of every possible size, RPN uses Anchor Boxes.
• At each pixel location in the feature map, the RPN evaluates a set of
predefined boxes (e.g., 3 scales × 3 aspect ratios = 9 anchors).
• The network predicts two things for each anchor:
o Objectness Score: Is there an object here or just background?
o Boundary Box Regressor: Fine-tuning the anchor coordinates to fit
the object better.
3. End-to-End Trainability
Because the RPN is a neural network, it is trainable. While Selective Search
proposes boxes blindly, the RPN learns over time which areas of an image are
likely to contain objects based on the specific dataset. This results in far fewer,
but much higher-quality, proposals (usually ~300 instead of 2,000).
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
iii.   SegNet is an "encoder-decoder" architecture. Briefly explain what the
encoder does to the input image, and what the decoder does to reconstruct
the shape of the strawberry. (3 Marks)
Solution   RoIAlign vs. RoIPool: Avoiding Quantization Errors (4 Marks)
YOLO bounding box (4 Marks)
SegNet: Encoder-Decoder Architecture (3 Marks)
In the original RoIPool (used in Fast/Faster R-CNN), the system performs
"quantization," which means it rounds fractional coordinates to the nearest whole
pixel.
********** 20 **********
--- page 21 ---
• The Problem (RoIPool): If a strawberry's region of interest (RoI) is at
coordinate 10., RoIPool rounds it to 1. When dividing the RoI into a grid
(e.g., 7 x7), further rounding occurs. These small errors accumulate,
leading to a "misalignment" between the feature map and the actual object
in the image. For a delicate strawberry, a 5-pixel shift means the gripper
hits the fruit instead of the stem.
• The Solution (RoIAlign): Introduced in Mask R-CNN, RoIAlign removes
quantization entirely. It uses Bilinear Interpolation to calculate the exact
values of the input features at floating-point coordinates. Instead of
rounding 10.7 to 11, it calculates what the pixel value would be at exactly
10.7 by looking at its four nearest neighbors.
ii. Bounding Boxes (YOLO) vs. Precise Masks
Using a standard YOLO bounding box (a rectangle) is risky for delicate
harvesting for the following reasons:
• Background Inclusion: A rectangle always includes the corners of the
background (leaves, stems, or other berries) that are not part of the target
strawberry. The robot might try to "grip" the width of the box, mistakenly
crushing the edges of the berry or snagging a nearby branch.
•   Irregular Shapes: Strawberries are rarely perfect rectangles. They can be
tilted, heart-shaped, or elongated. A bounding box provides the "limit" of
the object but zero information about its orientation or curvature.
iii. SegNet: Encoder-Decoder Architecture
SegNet is designed specifically for semantic segmentation (pixel-wise
labeling).
• The Encoder: Its job is Feature Extraction. It uses a series of convolutional
and pooling layers to "compress" the input image. It identifies high-level
features (the color and texture of a strawberry) while reducing the spatial
resolution. Crucially, SegNet's encoder stores the max-pooling indices
(the locations of the strongest pixels) to help the decoder later.
• The Decoder: Its job is Upsampling and Reconstruction. It takes the low-
resolution "summary" from the encoder and maps it back to the original
image size. It uses those stored pooling indices to place pixels back in
their precise original locations. This allows the robot to see the exact,
sharp boundary of the strawberry rather than a blurry blob.
********** 21 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper d1fc1f43ee9b

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/COMPUTER VISION/ANS_COMPUTER VISION(702EX0E015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/MBA Tech (Comp)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: COMPUTER VISION
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Use of Scientific calculator is allowed.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 2   a. Consider a pixel neighborhood where the elements of the second-moment   [05]
SO- 1   (structure)   matrix   are   given   as   follows:
BL-   𝑆𝑥𝑥= 18   ,   𝑆𝑦𝑦= 14   ,   and   𝑆𝑥𝑦= 6   .
2,3,4   Assume the Harris detector sensitivity parameter 𝑘= 0.04.
i. Calculate the Harris corner response 𝑅 using
𝑅= det (𝑀) −𝑘 (trace(𝑀))2
ii. Based on the computed values of the determinant and trace of the matrix,
interpret the nature of the image feature at this point. Indicate whether it
corresponds to a flat region, an edge, or a corner, and justify your answer.
Solution   Calculate the Harris corner response 𝑹 - 4 marks
Indicate whether it corresponds to a flat region, an edge, or a corner -1
Marks
Harris Corner Detection – Solution
Given:
S_xx = 18, S_yy = 14, S_xy = 6
Harris parameter k = 0.04
Structure Matrix
The second moment (structure) matrix M is given by:
M = [[18, 6], [6, 14]]
i. Harris Corner Response Calculation
Determinant of M:
det(M) = (18 × 14) − (6)² = 252 − 36 = 216
Trace of M:
trace(M) = 18 + 14 = 32
Harris corner response R:
R = det(M) − k(trace(M))²
********** 1 **********
--- page 2 ---
R = 216 − 0.04 × (32)²
R = 216 − 40.96 = 175.04
ii. Interpretation of Image Feature
Since the determinant and trace of the matrix are both large and the Harris
response R is strongly positive, the point corresponds to a corner.
This indicates significant intensity variation in both horizontal and vertical
directions, which is the defining characteristic of a corner in Harris corner
detection.
CO- 3   b. Suppose two local image feature vectors extracted from different images are   [05]
SO- 1   represented as
BL-2,3   P = (1,4,2) and Q = (3,6,4)
i.   Calculate the cosine similarity between feature vectors P and Q.
ii.   Based on the computed similarity value, assess whether these two features
are likely to be a reliable match. Briefly justify your conclusion.
Solution   Calculate the cosine similarity - 04 Marks
Reliable Match---   01 Marks
Cosine Similarity Between Image Feature Vectors
Given Feature Vectors:
P = (1, 4, 2)
Q = (3, 6, 4)
i. Cosine Similarity Calculation
The cosine similarity between two vectors P and Q is defined as:
cos(θ) = (P · Q) / (||P|| ||Q||)
Dot product P · Q = (1×3) + (4×6) + (2×4) = 35
Magnitude of P, ||P|| = √(1² + 4² + 2²) = 4.5826
Magnitude of Q, ||Q|| = √(3² + 6² + 4²) = 7.8102
Cosine Similarity = 35 / (4.5826 × 7.8102)
Cosine Similarity = 0.9779
ii. Feature Matching Interpretation
The cosine similarity value is close to 1, indicating strong similarity between
the two feature vectors.
Hence, the two features are likely to be a reliable match.
In practice, higher cosine similarity values indicate better feature
correspondence.
CO- 4   c.   i. Explain the importance of homogeneous coordinates in performing image   [05]
SO- 1   transformations in computer vision.
BL-3   ii. An image point 𝑄(4,5)is subjected to a scaling transformation with scaling
factors
𝑆𝑥= 3 along the x-axis and 𝑆𝑦= 2 along the y-axis.
Represent the point using homogeneous coordinates and determine the final
coordinates of the point after applying the scaling operation.
Solution   Explain Homogeneous Coordinates –02 Marks
Scaling Transformation Using Homogeneous Coordinates -03 Marks
i. Importance of Homogeneous Coordinates in Image Transformations
Homogeneous coordinates play a crucial role in computer vision and image
processing because they allow different types of geometric transformations to be
represented and performed using matrix multiplication. In homogeneous
coordinates, a 2D image point (x, y) is represented as a 3D vector (x, y, 1). This
********** 2 **********
--- page 3 ---
representation makes it possible to combine translation, scaling, rotation, and
shearing transformations into a single matrix form. Homogeneous coordinates
also simplify the mathematical formulation of transformations and enable easy
concatenation of multiple transformations using matrix multiplication. As a
result, they are widely used in image registration, object detection, and camera
geometry in computer vision.
ii. Scaling Transformation Using Homogeneous Coordinates
Given image point: Q(4, 5)
Scaling factors: Sx = 3 (x-direction), Sy = 2 (y-direction)
Step 1: Representation in homogeneous coordinates:
Q = [4 5 1]^T
Step 2: Scaling transformation matrix:
S = [[3, 0, 0], [0, 2, 0], [0, 0, 1]]
Step 3: Apply scaling transformation:
[x' y' 1]^T = S × Q
Result:
x' = 3 × 4 = 12
y' = 2 × 5 = 10
Final coordinates after scaling: Q' (12, 10)
CO- 5   d. Define a feature map in the context of CNNs. How does the number of filters in   [05]
SO- 1   a convolutional layer affect the depth of the resulting feature maps?
BL- 2
Solution   Feature Map in Convolutional Neural Networks (CNNs) (3 Makrs)
Impact of Filter (2 Marks)
Definition of Feature Map
In the context of Convolutional Neural Networks (CNNs), a feature map is the
output produced by applying a convolutional filter (kernel) to an input image or
to the output of a previous layer. Each feature map highlights specific patterns
such as edges, corners, textures, or more complex features, depending on the
depth of the network.
Kernel (Convolutional Filter)
A kernel (also called a filter) is a small matrix of trainable weights, for example
3×3 or 5×5, that slides over the input image. At each spatial location, element-
wise multiplication is performed between the kernel and the corresponding local
region of the input, and the results are summed to produce one value in the feature
map.
Example of a 3×3 kernel:
[ 1 0 -1 ]
[ 1 0 -1 ]
[ 1 0 -1 ]
Feature Map Generation
When a kernel is convolved with the input, the resulting output is a 2D feature
map. Each feature map corresponds to one kernel and represents the presence and
strength of a particular feature across the spatial dimensions of the input.
Example of a resulting feature map (conceptual):
[ 0.2 1.3 0.8 ]
[ 1.1 2.5 1.6 ]
[ 0.4 1.7 0.9 ]
Effect of Number of Filters on Feature Map Depth
The number of filters in a convolutional layer directly determines the depth
(number of channels) of the output feature maps. If a convolutional layer uses N
********** 3 **********
--- page 4 ---
different filters, it will produce N different feature maps stacked along the depth
dimension.
For example, if an input image is convolved using 32 filters, the output of that
convolutional layer will consist of 32 feature maps. Each feature map captures
different visual characteristics from the input.
In summary, a feature map is the spatial output obtained after applying a
convolutional kernel to an input. Kernels act as feature detectors, while the
number of filters controls how many distinct features are learned and therefore
defines the depth of the resulting feature maps.
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
Solution   responsibilities of low-level, mid-level, and high-level -2 Marks
visual data is processed at each level – 2 Marks
Example –01 Marks
Multi-Level Vision Architecture in Smart Video Surveillance Systems
Smart video surveillance systems deployed in public spaces use a multi-level
vision architecture to efficiently process visual data, monitor activities, and
detect potential security threats. This architecture divides visual processing into
low-level, mid-level, and high-level stages, each with distinct responsibilities.
i. Responsibilities of Vision Processing Levels
Low-Level Vision Processing:
Low-level vision deals with raw pixel data and focuses on improving image
quality and extracting basic visual information. Its responsibilities include noise
reduction, contrast enhancement, illumination correction, edge detection, and
frame normalization. This stage prepares clean and reliable visual data for later
analysis.
Mid-Level Vision Processing:
Mid-level vision interprets the enhanced data to recognize meaningful structures
and patterns. It is responsible for object detection, motion estimation, tracking,
segmentation, and basic activity recognition, such as identifying pedestrians or
groups.
High-Level Vision Processing:
High-level vision performs semantic interpretation and decision-making. It
analyzes outputs from the mid-level stage to understand behaviors, detect
********** 4 **********
--- page 5 ---
anomalies, and generate security alerts by applying rules, contextual reasoning,
or machine learning models.
ii. Automated CCTV Surveillance System in a Shopping Mall
Low-Level Stage: Video Enhancement and Preparation
In a shopping mall, raw CCTV video frames may suffer from poor lighting,
shadows, or camera noise. At the low-level stage, techniques such as noise
filtering, brightness and contrast adjustment, background normalization, and
frame stabilization are applied to enhance video quality.
Mid-Level   Stage:   Detection   of   Objects   and   Activities
At the mid-level stage, the system detects and tracks objects such as shoppers,
staff, or unattended bags. Motion analysis identifies walking patterns, crowd
formation, loitering, and abnormal movement.
High-Level Stage: Inference of Suspicious Behaviour
The high-level stage evaluates detected activities in context. Examples include
detecting abandoned objects, prolonged loitering near restricted areas, or panic
situations, leading to alarms or security notifications.
iii. Impact of Malfunction or Inaccuracies in Vision Stages
Low-Level Errors:
Poor noise removal or illumination handling can result in unclear video frames,
which may cause later detection stages to fail.
Mid-Level Errors:
Incorrect object detection or tracking may generate false alarms or miss genuine
threats, such as failing to detect unattended bags.
High-Level Errors:
Faulty reasoning or improper rules may either overestimate normal behavior as
suspicious or fail to identify real security risks.
Conclusion
An intelligent surveillance system relies on accurate processing at all vision
levels. Errors at any stage can propagate through the system, reducing overall
effectiveness and reliability.
Q2   b A 3 × 3grayscale image patch is given as:   [10]
CO- 1   12 18 12
SO- 2   𝐼= [ 18 36 18 ]
12 18 12
BL- 1,2
(a)Using the Laplacian kernel
0 1 0
[ 1 −4 1 ]
0 1 0
compute the Laplacian response at the center pixel.
(b)Gaussian blurred responses of the same pixel at two scales are:
𝐺𝜎1 = 30, 𝐺𝜎2 = 24
Compute the Difference of Gaussian (DoG) and comment on whether it indicates
a significant feature.
(c) If Sobel gradients are:
********** 5 **********
--- page 6 ---
𝐺𝑥= 10, 𝐺𝑦= 5
Calculate Gradient magnitude and Gradient direction
(d)Assign the gradient direction to the closest HOG orientation bin:
0∘,  45∘,  90∘,  135∘
Solution   • Laplacian Response   (3 Marks)
• Difference of Gaussian (DoG) (2 Marks)
• Gradient Magnitude and Direction (3 Marks)
• HOG Orientation Bin Assignment (2 Marks)
Image Processing Operations – Solution
Given a 3×3 grayscale image patch:
I = [[12, 18, 12], [18, 36, 18], [12, 18, 12]]
(a) Laplacian Response
Laplacian kernel used:
[[0, 1, 0], [1, -4, 1], [0, 1, 0]]
Laplacian response at the center pixel is computed as:
(0×12 + 1×18 + 0×12) + (1×18 − 4×36 + 1×18) + (0×12 + 1×18 + 0×12)
= 18 + (18 − 144 + 18) + 18
= −54
(b) Difference of Gaussian (DoG)
Given Gaussian blurred responses: G(σ1) = 30, G(σ2) = 24
DoG = G(σ1) − G(σ2) = 30 − 24 = 6
A non-zero DoG value indicates the presence of a significant feature such as an
edge or blob.
(c) Gradient Magnitude and Direction
Given Sobel gradients: Gx = 10, Gy = 5
Gradient magnitude: |G| = √(Gx² + Gy²) = √(125) ≈ 11.18
Gradient direction: θ = tan⁻¹(Gy / Gx) = tan⁻¹(0.5) ≈ 26.6°
(d) HOG Orientation Bin Assignment
Given bins: 0°, 45°, 90°, 135°
Computed angle ≈ 26.6°
Closest HOG orientation bin: 45°
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
Solution   • Integral Image – 4 Marks
• compute the sum of pixel values—3 Marks
• integral images allow constant-time computation of box filter -3
Marks
********** 6 **********
--- page 7 ---
Integral Image Computation – Solution
Given grayscale image matrix (4 × 4):
I = [[2, 1, 3, 4], [0, 1, 2, 1], [3, 2, 1, 0], [1, 1, 2, 3]]
1. Construction of Integral Image
An integral image (summed-area table) at location (x, y) contains the sum of all
pixel values above and to the left of that position, inclusive.
The integral image is calculated cumulatively row-wise and column-wise.
Integral Image:
II = [[2, 3, 6, 10], [2, 4, 9, 14], [5, 9, 15, 20], [6, 11, 19, 27]]
2. Sum of Pixel Values Using Integral Image
A 3 × 2 rectangular region starting at position (2,2) covers rows 2–3 and
columns 2–4.
Using the integral image, the sum is computed as:
Sum = II(3,4) − II(1,4) − II(3,1) + II(1,1)
Sum = 20 − 10 − 5 + 2 = 7
Final sum of pixel values = 7
3. Importance of Integral Images
Integral images enable constant-time computation of rectangular (box) filter
responses. Regardless of the filter size, only four memory accesses and a few
arithmetic operations are required. This makes integral images extremely
efficient for real-time applications such as object detection, feature extraction,
and image filtering.
Q3   b The Scale-Invariant Feature Transform (SIFT) is a widely used algorithm for   [10]
CO- 2   detecting and describing distinctive local features that are robust to changes in
SO- 1   imaging conditions.
i.   Explain how scale-space construction using Gaussian filtering enables
BL-2,3,4
the detection of keypoints that are invariant to scale variations in the
image.
ii.   Discuss the role of accurate keypoint localization in SIFT and analyze
how it improves the stability and reliability of extracted features.
iii.   Describe the process of orientation assignment in the SIFT algorithm
and explain how this step ensures rotation invariance.
iv.   With suitable justification, explain why SIFT features outperform
traditional edge and corner detectors when matching images captured
under real-world variations such as changes in illumination, scale, and
viewpoint.
Solution   • Scale-Space Construction and Scale Invariance (3 Marks)
• Keypoint Localization and Its Importance (2 Marks)
• Orientation Assignment and Rotation Invariance (3 Marks)
• Superiority of SIFT over Traditional Edge and Corner Detectors (2
Marks)
The Scale-Invariant Feature Transform (SIFT) is a robust algorithm for
detecting and describing local features in images. It is designed to be invariant
to scale, rotation, and partially invariant to illumination and viewpoint changes.
(a) Scale-Space Construction and Scale Invariance
SIFT achieves scale invariance by constructing a scale space of the image using
Gaussian filtering. The input image is convolved with Gaussian kernels at
different scales (standard deviations). Adjacent Gaussian-blurred images are
********** 7 **********
--- page 8 ---
subtracted to form Difference of Gaussian (DoG) images. Local extrema
(maxima and minima) in the DoG scale space across both spatial location and
scale are selected as keypoints. Since keypoints are detected at characteristic
scales, the same physical feature can be identified even when the image is
resized, making the detection scale invariant.
(b) Keypoint Localization and Its Importance
After detecting potential keypoints, SIFT performs accurate keypoint
localization by fitting a 3D quadratic function to the local sample points. This
step refines the keypoint location and scale, and discards unstable keypoints
with low contrast or those poorly localized along edges. Accurate localization
improves the stability and repeatability of features, reduces sensitivity to noise,
and ensures that only distinctive and reliable keypoints are retained for further
processing.
(c) Orientation Assignment and Rotation Invariance
For each keypoint, SIFT assigns one or more dominant orientations based on
local image gradient directions around the keypoint at the selected scale. A
histogram of gradient orientations is formed, and the peak(s) of this histogram
determine the orientation(s). All subsequent feature descriptors are computed
relative to this orientation, ensuring that the descriptor remains unchanged even
if the image is rotated. This step provides rotation invariance.
(d) Superiority of SIFT over Traditional Edge and Corner Detectors
SIFT features outperform traditional edge and corner detectors because they are
highly distinctive and robust to real-world variations. Unlike simple edge or
corner detectors, SIFT incorporates scale-space analysis, orientation
normalization, and rich local descriptors based on gradient distributions. This
makes SIFT features resilient to changes in illumination, scale, rotation, and
moderate viewpoint differences. As a result, SIFT produces reliable feature
matches across varied imaging conditions, which is essential for tasks such as
object recognition, image matching, and 3D reconstruction.
Q4   a   Consider a set of 2-D feature points extracted from an image:   [10]
CO- 3   (1,1),  (3,3),  (9,9),  (11,11)
SO- 2
BL- 3,4   Assume the number of clusters 𝐾= 2 and the initial cluster centers are given as:
𝜇1 = (1,1), 𝜇2 = (9,9)
Answer the following:
1. Assign each data point to its nearest cluster centre using Euclidean
distance.
2. Calculate the updated cluster centroids after completing one iteration of
the K-means algorithm.
II. In a multi-resolution image matching approach, feature similarity is computed
at different levels of an image pyramid and combined using weighted scores.
Suppose two images produce the following histogram similarity values:
• Pyramid Level 0 (original resolution): similarity score = 0.88
********** 8 **********
--- page 9 ---
• Pyramid Level 1 (reduced resolution): similarity score = 0.96
The corresponding weights assigned to these levels are:
• Level 0 → weight = 1.0
• Level 1 → weight = 0.6
•
Calculate the overall weighted feature similarity score between the two images.
Briefly explain how using multiple pyramid levels improves the robustness of
image similarity measurement.
Solution   • K-Means Clustering (5 Marks)
• Multi-Resolution Image Matching (5 Marks)
I. K-Means Clustering
Given 2D feature points: (1,1), (3,3), (9,9), (11,11)
Number of clusters: K = 2
Initial cluster centers: μ₁ = (1,1), μ₂ = (9,9)
Assignment of Points to Nearest Cluster
Euclidean distance is used as the distance metric.
(1,1): Distance to μ₁ = 0, Distance to μ₂ = √((8)²+(8)²) = 11.31 → Assigned to
Cluster 1
(3,3): Distance to μ₁ = √((2)²+(2)²) = 2.83, Distance to μ₂ = √((6)²+(6)²) = 8.49
→ Assigned to Cluster 1
(9,9): Distance to μ₁ = 11.31, Distance to μ₂ = 0 → Assigned to Cluster 2
(11,11): Distance to μ₁ = 14.14, Distance to μ₂ = 2.83 → Assigned to Cluster 2
Updated Cluster Centroids After One Iteration
Cluster 1 points: (1,1), (3,3)
Updated μ₁ = ((1+3)/2 , (1+3)/2) = (2,2)
Cluster 2 points: (9,9), (11,11)
Updated μ₂ = ((9+11)/2 , (9+11)/2) = (10,10)
II. Multi-Resolution Image Matching
Given similarity scores at different pyramid levels:
Level 0 (original resolution): Similarity = 0.88, Weight = 1.0
Level 1 (reduced resolution): Similarity = 0.96, Weight = 0.6
Overall Weighted Similarity Score
Weighted similarity = (1.0 × 0.88) + (0.6 × 0.96)
= 0.88 + 0.576 = 1.456
Overall weighted feature similarity score = 1.456
Score = 1.456/1.6
Similarity score=0.91
Importance of Using Multiple Pyramid Levels
Using multiple pyramid levels improves robustness by capturing image features
at different spatial resolutions. Higher-resolution levels preserve fine details,
while lower-resolution levels capture global structure and are less sensitive to
noise, illumination changes, and small misalignments. Combining similarity
scores across levels therefore results in a more reliable and stable image matching
process.
Q4   b   In an image retrieval system based on the Bag of Visual Words (BoVW) model,   [10]
CO- 3   three database images are represented by the following visual word histograms:
SO- 2   𝐼1 = [3,1,2,0],𝐼2 = [1,2,0,2], 𝐼3 = [2,0,1,3]
********** 9 **********
--- page 10 ---
BL-3,4,5   A query image has the histogram:
𝑄= [2,1,1,1]
i.   Calculate   the Term   Frequency   (TF)   vectors   for   all   images.
ii. Compute the Document Frequency (DF) and Inverse Document Frequency
(IDF)   for   each   visual   word.
iii.   Determine   the TF-IDF   representation   for   the   query   image.
iv. Using Euclidean distance, identify which image in the database best matches
the query.
Solution   • Calculate the Term Frequency (TF) (2 Marks)
• Compute the Document Frequency (DF) and Inverse Document
Frequency (IDF) (3 Marks)
• TF-IDF representation for the query image (2 Makrs)
• image in the database best matches the query (3 Marks)
Bag of Visual Words (BoVW) with TF–IDF – Solution
Database image histograms:
I₁ = [3, 1, 2, 0]
I₂ = [1, 2, 0, 2]
I₃ = [2, 0, 1, 3]
Query image histogram: Q = [2, 1, 1, 1]
i. Term Frequency (TF) Calculation
Term Frequency (TF) is computed by normalizing each histogram by the total
number of visual words in that image.
TF(I₁) = [3/6, 1/6, 2/6, 0/6] = [0.50, 0.17, 0.33, 0.00]
TF(I₂) = [1/5, 2/5, 0/5, 2/5] = [0.20, 0.40, 0.00, 0.40]
TF(I₃) = [2/6, 0/6, 1/6, 3/6] = [0.33, 0.00, 0.17, 0.50]
TF(Q) = [2/5, 1/5, 1/5, 1/5] = [0.40, 0.20, 0.20, 0.20]
ii. Document Frequency (DF) and Inverse Document Frequency (IDF)
Document Frequency (DF) is the number of images in which a visual word
appears at least once.
DF values:
Word 1: appears in I₁, I₂, I₃ → DF = 3
Word 2: appears in I₁, I₂ → DF = 2
Word 3: appears in I₁, I₃ → DF = 2
Word 4: appears in I₂, I₃ → DF = 2
IDF values (IDF = ln(N / DF)):
IDF₁ = ln(3/3) = 0.00
IDF₂ = ln(3/2) = 0.41
IDF₃ = ln(3/2) = 0.41
IDF₄ = ln(3/2) = 0.41
iii. TF–IDF Representation of Query Image
TF–IDF(Q):
[0.00, 0.08, 0.08, 0.08]
iv. Image Matching Using Euclidean Distance
Euclidean distance is used to compare the TF–IDF query vector with database
image vectors. The image with the minimum distance is considered the best
match.
Computed distances (using TF–IDF vectors):
Distance(Q, I₁) ≈ 0.29
Distance(Q, I₂) ≈ 0.36
Distance(Q, I₃) ≈ 0.33
Best matching image for the query: I₁ (minimum distance)
********** 10 **********
--- page 11 ---
Q5   a   I. Consider the following one-dimensional data points:   [10]
CO-4   1,  3,  6,  11,  13
SO- 1
A Mean Shift algorithm is applied with a kernel window (bandwidth) of 4.
BL- 3
Starting from the initial point 𝑥= 3:
i.   Perform the first iteration of the Mean Shift procedure by identifying all
data points within the window and computing the new mean.
ii.   Use the updated mean as the starting point and perform the second
iteration.
II. Compare and contrast the K-means clustering algorithm with the Mean Shift
clustering method, highlighting   their working principles, assumptions,
advantages, and limitations.
Solution   • Mean Shift Algorithm Numerical– 5 Marks (3+2)
• K-mean and Mean shift difference – 5 Marks
Mean Shift Algorithm – Worked Example
Given 1D data points: 1, 3, 6, 11, 13
Kernel window (bandwidth) = 4
Initial point x = 3
--- First Iteration ---
Points within window [x - 4, x + 4] = [-1, 7]
Included points: 1, 3, 6
Mean = (1 + 3 + 6) / 3 = 10 / 3 ≈ 3.33
--- Second Iteration ---
New window centered at x = 3.33 ⇒ [−0.67, 7.33]
Included points: 1, 3, 6
Mean = (1 + 3 + 6) / 3 = 3.33
II. K-mean and Mean Shift method
Clustering is an unsupervised learning technique used to group similar data
points. K-means and Mean Shift are two widely used clustering algorithms,
each based on different principles and assumptions.
1. Working Principles
K-means clustering partitions the dataset into a predefined number of clusters
(K). It works by initializing K centroids, assigning each data point to the nearest
centroid based on a distance measure (usually Euclidean distance), and then
updating the centroids as the mean of all points assigned to each cluster. This
process is repeated iteratively until convergence.
Mean Shift clustering is a density-based method that does not assume a fixed
number of clusters. It works by placing a window (kernel) around each data
point and iteratively shifting the window toward regions of higher data density
(the mean of points within the window). Points that converge to the same mode
are grouped into the same cluster.
2. Assumptions
********** 11 **********
--- page 12 ---
K-means assumes that clusters are spherical, equally sized, and well separated,
and that the number of clusters K is known in advance.
Mean Shift assumes that clusters correspond to modes (peaks) in the underlying
data density distribution and relies on an appropriate bandwidth parameter to
estimate density.
3. Advantages
K-means is simple to understand, easy to implement, computationally efficient,
and works well for large datasets when clusters are compact and distinct.
Mean Shift does not require prior knowledge of the number of clusters, can
discover arbitrarily shaped clusters, and is well-suited for applications such as
image segmentation.
4. Limitations
K-means is sensitive to the initial placement of centroids, choice of K, and
outliers. It also performs poorly when clusters are non-spherical or have varying
densities.
Mean Shift is computationally expensive, especially for large datasets, and its
performance heavily depends on the choice of bandwidth. An incorrect
bandwidth can lead to over-segmentation or under-segmentation of data.
In summary, K-means is a fast, parametric clustering technique suitable for
large-scale problems with simple cluster structures, while Mean Shift is a non-
parametric, flexible clustering method that can automatically detect the number
of clusters but at a higher computational cost.
Q5   b   i. Why is it necessary to use multiple frames instead of a single frame for   [10]
CO- 2   background modeling in background subtraction techniques?
SO- 2   ii.   Explain the role of N consecutive images in constructing a reliable
background model for motion detection.
BL-3,4
iii.   In background subtraction methods, what problems arise   if the
background reference is built using only one image? How does using N
images overcome these problems?
Solution   Background substraction – 10 Marks (4+4+2)
i. Why is it necessary to use multiple frames instead of a single frame?
Using multiple frames is necessary because a single image cannot accurately
represent the background in real-world video scenes. A single frame may contain
temporary objects, moving entities, noise, illumination variations, or shadows.
These factors can cause incorrect classification of background and foreground.
Multiple frames help capture stable background characteristics over time,
reducing the influence of noise and transient objects.
ii. Role of N consecutive images in constructing a reliable background model
N consecutive images are used to observe pixel behavior over time. By analyzing
intensity values across N frames, the system can estimate statistical properties
such as mean, median, or variance for each pixel. This temporal analysis helps
********** 12 **********
--- page 13 ---
distinguish between background pixels (which remain consistent) and foreground
pixels (which change frequently). As a result, the background model becomes
more robust and reliable for motion detection.
iii. Problems with single-image background reference and how N images
overcome them
If the background reference is built using only one image, several problems arise:
noise is mistaken as motion, shadows or illumination changes cause false
detections, and stationary foreground objects may become part of the
background. Using N images overcomes these issues by averaging or statistically
modeling pixel behavior over time. This approach filters out noise, adapts to
gradual illumination changes, and correctly identifies persistent background
elements, leading to more accurate motion detection.
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
Solution   Affine Transformation of a Triangular ROI (10 Marks)
Given triangle vertices:
A(2, 3), B(6, 3), C(4, 7)
Scaling factors:
Sx = 2 (x-axis), Sy = 4 (y-axis)
Translation: 5 units right, 3 units downward
(i) Homogeneous Transformation Matrices
Scaling matrix:
[ 2 0 0 ]
[ 0 4 0 ]
[ 0 0 1 ]
Translation matrix:
[ 1 0 5 ]
[ 0 1 -3 ]
[ 0 0 1 ]
(ii) Composite Transformation Matrix (T × S):
********** 13 **********
--- page 14 ---
[ 2 0 5 ]
[ 0 4 -3 ]
[ 0 0 1 ]
(iii) Transformed Coordinates:
A'(9, 9)
B'(17, 9)
C'(13, 25)
Summary: The triangle is first scaled about the origin and then translated,
resulting in the above transformed vertices.
Q6   b   I) Discuss the limitations of using an exhaustive (brute-force) feature matching   [10]
CO- 3,5   strategy when comparing descriptors from two images. Consider aspects such as
SO- 2   accuracy, ambiguity, and computational cost.
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
Solution   • Feature Matching Limitations (5 Marks)
• CNN Convolution Layer Analysis (5 Marks)
I) Limitations of Exhaustive (Brute Force) Feature Matching
An exhaustive or brute-force feature matching strategy compares every
descriptor from the first image with every descriptor from the second image
using a distance metric such as Euclidean distance.
1. Computational Cost:
Brute-force matching is computationally expensive, especially for images
having a large number of features. The time complexity grows quadratically,
making it unsuitable for real-time or large-scale applications.
2. Ambiguity in Matching:
Descriptors may look similar across different regions, leading to multiple
potential matches. This ambiguity can cause incorrect correspondences,
particularly in repetitive textures.
3. Reduced Accuracy in Noisy Conditions:
Noise, illumination changes, or viewpoint variations can distort descriptors,
causing brute-force matching to produce false matches. Without additional
constraints, the accuracy may degrade significantly.
II) Convolutional Neural Network Layer Analysis
Given:
Input image size: 8 × 8
Kernel size: 5 × 5
Stride: 2
********** 14 **********
--- page 15 ---
Zero padding: 1
Number of filters: 3
(i) Output Feature Map Size:
Output dimension formula:
(N − F + 2P)/S + 1
Where N = 8, F = 5, P = 1, S = 2
(8 − 5 + 2×1)/2 + 1 = (5)/2 + 1 = 2.5 + 1 ≈ 3.5
Taking floor value: 3
Therefore, output size per filter = 3 × 3
(ii) Number of Trainable Parameters:
Weights per filter = 5 × 5 = 25
Bias per filter = 1
Total parameters per filter = 26
Total trainable parameters = 26 × 3 = 78
Q7   a   i.   What were the main efficiency limitations in the original R-CNN   [10]
CO- 5   framework?
SO- 1   ii.   Describe how Fast R-CNN redesigned the detection pipeline to overcome
these inefficiencies.
BL-2
iii.   What was the major speed bottleneck that still remained in Fast R-CNN,
and how was it addressed in Faster R-CNN?
Solution   •   i) Efficiency Limitations of Original R-CNN (4 Marks)
•   ii) Improvements Introduced by Fast R-CNN (3 Marks)
•   iii) Remaining Bottleneck in Fast R-CNN and Faster R-CNN
Solution (3 Marks)
Evolution of the R-CNN Object Detection Frameworks
i) Efficiency Limitations of Original R-CNN
The original R-CNN (Region-based Convolutional Neural Network) framework
suffered from several efficiency limitations:
1. Redundant Computation:
Each region proposal (around 2000 per image) was independently passed
through a CNN, leading to repeated and expensive convolution operations.
2. Multi-stage Training Pipeline:
R-CNN required separate stages for CNN fine-tuning, SVM training, and
bounding box regression, increasing complexity and training time.
3. Large Storage Requirements:
Extracted region features were stored on disk, consuming hundreds of gigabytes
and slowing down training and experimentation.
ii) Improvements Introduced by Fast R-CNN
Fast R-CNN redesigned the detection pipeline to improve efficiency in the
following ways:
1. Single Forward Pass:
********** 15 **********
--- page 16 ---
The entire image is passed once through the convolutional layers to generate a
shared feature map.
2. ROI Pooling Layer:
Region of Interest (ROI) Pooling extracts fixed-size feature vectors from the
shared feature map, eliminating redundant CNN computations.
3. End-to-End Training:
Classification and bounding box regression are combined into a single network
trained using a multi-task loss, simplifying training and improving speed.
iii) Remaining Bottleneck in Fast R-CNN and Faster R-CNN Solution
Despite improvements, Fast R-CNN still faced a major speed bottleneck:
1. Selective Search:
Fast R-CNN relied on selective search for region proposals, which is
computationally expensive and operates outside the neural network.
Faster R-CNN addressed this limitation by introducing the Region Proposal
Network (RPN), which shares convolutional features with the detection network
and generates region proposals efficiently within the CNN, enabling near real-
time object detection.
Q7   b   I.) A convolutional neural network processes a grayscale image, producing the   [10]
CO- 5   following 4 × 4 feature map after the first convolution layer:
SO- 2   5 8 12 6
7 9 15 10
BL-3,4   𝐺= [   ]
4 6 20 18
3 5 16 14
a) State the purpose of the pooling layer in CNNs.
b) Apply 2 × 2 pooling with stride 2 and compute the resulting feature maps
using:
a)Max Pooling
b) Average Pooling
c)Min Pooling
Show intermediate calculations clearly.
II.) The Faster R-CNN framework originally used RoIPool for extracting
fixed-size feature maps from proposal regions.
i.   Explain how quantization in the RoIPool layer introduces localization
inaccuracies during region pooling.
ii.   Discuss the impact of this quantization error on object detection accuracy,
particularly for small objects.
iii.   Describe how RoIAlign eliminates this issue and improves spatial
precision.
Solution   • Pooling Numerical (5 Marks)
• Faster R-CNN   (5 Marks)
Solution
I. Pooling in Convolutional Neural Networks
********** 16 **********
--- page 17 ---
Given 4×4 feature map G:
5 8 12 6
7 9 15 10
4 6 20 18
3 5 16 14
a) Purpose of pooling layer
The pooling layer reduces the spatial dimensions of feature maps while
retaining important information. It decreases computational cost, controls
overfitting, and introduces translation invariance by summarizing local
neighborhoods.
b) 2×2 Pooling with stride 2
Pooling regions:
Region 1: [[5, 8], [7, 9]]
Region 2: [[12, 6], [15, 10]]
Region 3: [[4, 6], [3, 5]]
Region 4: [[20, 18], [16, 14]]
i) Max Pooling
Region 1: max(5,8,7,9) = 9
Region 2: max(12,6,15,10) = 15
Region 3: max(4,6,3,5) = 6
Region 4: max(20,18,16,14) = 20
Resulting feature map:
[9 15
6 20]
ii) Average Pooling
Region 1: (5+8+7+9)/4 = 7.25
Region 2: (12+6+15+10)/4 = 10.75
Region 3: (4+6+3+5)/4 = 4.5
Region 4: (20+18+16+14)/4 = 17
Resulting feature map:
[7.25 10.75
4.5   17]
iii) Min Pooling
Region 1: min(5,8,7,9) = 5
Region 2: min(12,6,15,10) = 6
Region 3: min(4,6,3,5) = 3
Region 4: min(20,18,16,14) = 14
Resulting feature map:
[5 6
3 14]
II. RoIPool vs RoIAlign in Faster R-CNN
RoIPool introduces localization inaccuracies because it quantizes floating-point
proposal coordinates to integer values. This rounding causes misalignment
between the original image and feature maps, leading to loss of spatial precision
during pooling.
This quantization error significantly affects object detection accuracy, especially
for small objects, where even minor spatial shifts can cause incorrect feature
extraction, resulting in missed detections or poor bounding box localization.
RoIAlign eliminates quantization by avoiding coordinate rounding and instead
uses bilinear interpolation to compute exact feature values at precise locations.
********** 17 **********
--- page 18 ---
This preserves spatial correspondence, improving localization accuracy and
overall object detection performance.
********** 18 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 3d3dd8c8f9a5

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/COMPUTER VISION/ANS_COMPUTER VISION(702EX0E015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/MBA Tech (Comp)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: COMPUTER VISION
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Use of Scientific calculator is allowed.
9. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 2   a. Consider a pixel neighborhood where the elements of the second-moment   [05]
SO- 1   (structure)   matrix   are   given   as   follows:
BL-   𝑆𝑥𝑥= 18   ,   𝑆𝑦𝑦= 14   ,   and   𝑆𝑥𝑦= 6   .
2,3,4   Assume the Harris detector sensitivity parameter 𝑘= 0.04.
i. Calculate the Harris corner response 𝑅 using
𝑅= det (𝑀) −𝑘 (trace(𝑀))2
ii. Based on the computed values of the determinant and trace of the matrix,
interpret the nature of the image feature at this point. Indicate whether it
corresponds to a flat region, an edge, or a corner, and justify your answer.
Solution   Calculate the Harris corner response 𝑹 - 4 marks
Indicate whether it corresponds to a flat region, an edge, or a corner -1
Marks
Harris Corner Detection – Solution
Given:
S_xx = 18, S_yy = 14, S_xy = 6
Harris parameter k = 0.04
Structure Matrix
The second moment (structure) matrix M is given by:
M = [[18, 6], [6, 14]]
i. Harris Corner Response Calculation
Determinant of M:
det(M) = (18 × 14) − (6)² = 252 − 36 = 216
Trace of M:
trace(M) = 18 + 14 = 32
Harris corner response R:
R = det(M) − k(trace(M))²
********** 1 **********
--- page 2 ---
R = 216 − 0.04 × (32)²
R = 216 − 40.96 = 175.04
ii. Interpretation of Image Feature
Since the determinant and trace of the matrix are both large and the Harris
response R is strongly positive, the point corresponds to a corner.
This indicates significant intensity variation in both horizontal and vertical
directions, which is the defining characteristic of a corner in Harris corner
detection.
CO- 3   b. Suppose two local image feature vectors extracted from different images are   [05]
SO- 1   represented as
BL-2,3   P = (1,4,2) and Q = (3,6,4)
i.   Calculate the cosine similarity between feature vectors P and Q.
ii.   Based on the computed similarity value, assess whether these two features
are likely to be a reliable match. Briefly justify your conclusion.
Solution   Calculate the cosine similarity - 04 Marks
Reliable Match---   01 Marks
Cosine Similarity Between Image Feature Vectors
Given Feature Vectors:
P = (1, 4, 2)
Q = (3, 6, 4)
i. Cosine Similarity Calculation
The cosine similarity between two vectors P and Q is defined as:
cos(θ) = (P · Q) / (||P|| ||Q||)
Dot product P · Q = (1×3) + (4×6) + (2×4) = 35
Magnitude of P, ||P|| = √(1² + 4² + 2²) = 4.5826
Magnitude of Q, ||Q|| = √(3² + 6² + 4²) = 7.8102
Cosine Similarity = 35 / (4.5826 × 7.8102)
Cosine Similarity = 0.9779
ii. Feature Matching Interpretation
The cosine similarity value is close to 1, indicating strong similarity between
the two feature vectors.
Hence, the two features are likely to be a reliable match.
In practice, higher cosine similarity values indicate better feature
correspondence.
CO- 4   c.   i. Explain the importance of homogeneous coordinates in performing image   [05]
SO- 1   transformations in computer vision.
BL-3   ii. An image point 𝑄(4,5)is subjected to a scaling transformation with scaling
factors
𝑆𝑥= 3 along the x-axis and 𝑆𝑦= 2 along the y-axis.
Represent the point using homogeneous coordinates and determine the final
coordinates of the point after applying the scaling operation.
Solution   Explain Homogeneous Coordinates –02 Marks
Scaling Transformation Using Homogeneous Coordinates -03 Marks
i. Importance of Homogeneous Coordinates in Image Transformations
Homogeneous coordinates play a crucial role in computer vision and image
processing because they allow different types of geometric transformations to be
represented and performed using matrix multiplication. In homogeneous
coordinates, a 2D image point (x, y) is represented as a 3D vector (x, y, 1). This
********** 2 **********
--- page 3 ---
representation makes it possible to combine translation, scaling, rotation, and
shearing transformations into a single matrix form. Homogeneous coordinates
also simplify the mathematical formulation of transformations and enable easy
concatenation of multiple transformations using matrix multiplication. As a
result, they are widely used in image registration, object detection, and camera
geometry in computer vision.
ii. Scaling Transformation Using Homogeneous Coordinates
Given image point: Q(4, 5)
Scaling factors: Sx = 3 (x-direction), Sy = 2 (y-direction)
Step 1: Representation in homogeneous coordinates:
Q = [4 5 1]^T
Step 2: Scaling transformation matrix:
S = [[3, 0, 0], [0, 2, 0], [0, 0, 1]]
Step 3: Apply scaling transformation:
[x' y' 1]^T = S × Q
Result:
x' = 3 × 4 = 12
y' = 2 × 5 = 10
Final coordinates after scaling: Q' (12, 10)
CO- 5   d. Define a feature map in the context of CNNs. How does the number of filters in   [05]
SO- 1   a convolutional layer affect the depth of the resulting feature maps?
BL- 2
Solution   Feature Map in Convolutional Neural Networks (CNNs) (3 Makrs)
Impact of Filter (2 Marks)
Definition of Feature Map
In the context of Convolutional Neural Networks (CNNs), a feature map is the
output produced by applying a convolutional filter (kernel) to an input image or
to the output of a previous layer. Each feature map highlights specific patterns
such as edges, corners, textures, or more complex features, depending on the
depth of the network.
Kernel (Convolutional Filter)
A kernel (also called a filter) is a small matrix of trainable weights, for example
3×3 or 5×5, that slides over the input image. At each spatial location, element-
wise multiplication is performed between the kernel and the corresponding local
region of the input, and the results are summed to produce one value in the feature
map.
Example of a 3×3 kernel:
[ 1 0 -1 ]
[ 1 0 -1 ]
[ 1 0 -1 ]
Feature Map Generation
When a kernel is convolved with the input, the resulting output is a 2D feature
map. Each feature map corresponds to one kernel and represents the presence and
strength of a particular feature across the spatial dimensions of the input.
Example of a resulting feature map (conceptual):
[ 0.2 1.3 0.8 ]
[ 1.1 2.5 1.6 ]
[ 0.4 1.7 0.9 ]
Effect of Number of Filters on Feature Map Depth
The number of filters in a convolutional layer directly determines the depth
(number of channels) of the output feature maps. If a convolutional layer uses N
********** 3 **********
--- page 4 ---
different filters, it will produce N different feature maps stacked along the depth
dimension.
For example, if an input image is convolved using 32 filters, the output of that
convolutional layer will consist of 32 feature maps. Each feature map captures
different visual characteristics from the input.
In summary, a feature map is the spatial output obtained after applying a
convolutional kernel to an input. Kernels act as feature detectors, while the
number of filters controls how many distinct features are learned and therefore
defines the depth of the resulting feature maps.
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
Solution   responsibilities of low-level, mid-level, and high-level -2 Marks
visual data is processed at each level – 2 Marks
Example –01 Marks
Multi-Level Vision Architecture in Smart Video Surveillance Systems
Smart video surveillance systems deployed in public spaces use a multi-level
vision architecture to efficiently process visual data, monitor activities, and
detect potential security threats. This architecture divides visual processing into
low-level, mid-level, and high-level stages, each with distinct responsibilities.
i. Responsibilities of Vision Processing Levels
Low-Level Vision Processing:
Low-level vision deals with raw pixel data and focuses on improving image
quality and extracting basic visual information. Its responsibilities include noise
reduction, contrast enhancement, illumination correction, edge detection, and
frame normalization. This stage prepares clean and reliable visual data for later
analysis.
Mid-Level Vision Processing:
Mid-level vision interprets the enhanced data to recognize meaningful structures
and patterns. It is responsible for object detection, motion estimation, tracking,
segmentation, and basic activity recognition, such as identifying pedestrians or
groups.
High-Level Vision Processing:
High-level vision performs semantic interpretation and decision-making. It
analyzes outputs from the mid-level stage to understand behaviors, detect
********** 4 **********
--- page 5 ---
anomalies, and generate security alerts by applying rules, contextual reasoning,
or machine learning models.
ii. Automated CCTV Surveillance System in a Shopping Mall
Low-Level Stage: Video Enhancement and Preparation
In a shopping mall, raw CCTV video frames may suffer from poor lighting,
shadows, or camera noise. At the low-level stage, techniques such as noise
filtering, brightness and contrast adjustment, background normalization, and
frame stabilization are applied to enhance video quality.
Mid-Level   Stage:   Detection   of   Objects   and   Activities
At the mid-level stage, the system detects and tracks objects such as shoppers,
staff, or unattended bags. Motion analysis identifies walking patterns, crowd
formation, loitering, and abnormal movement.
High-Level Stage: Inference of Suspicious Behaviour
The high-level stage evaluates detected activities in context. Examples include
detecting abandoned objects, prolonged loitering near restricted areas, or panic
situations, leading to alarms or security notifications.
iii. Impact of Malfunction or Inaccuracies in Vision Stages
Low-Level Errors:
Poor noise removal or illumination handling can result in unclear video frames,
which may cause later detection stages to fail.
Mid-Level Errors:
Incorrect object detection or tracking may generate false alarms or miss genuine
threats, such as failing to detect unattended bags.
High-Level Errors:
Faulty reasoning or improper rules may either overestimate normal behavior as
suspicious or fail to identify real security risks.
Conclusion
An intelligent surveillance system relies on accurate processing at all vision
levels. Errors at any stage can propagate through the system, reducing overall
effectiveness and reliability.
Q2   b A 3 × 3grayscale image patch is given as:   [10]
CO- 1   12 18 12
SO- 2   𝐼= [ 18 36 18 ]
12 18 12
BL- 1,2
(a)Using the Laplacian kernel
0 1 0
[ 1 −4 1 ]
0 1 0
compute the Laplacian response at the center pixel.
(b)Gaussian blurred responses of the same pixel at two scales are:
𝐺𝜎1 = 30, 𝐺𝜎2 = 24
Compute the Difference of Gaussian (DoG) and comment on whether it indicates
a significant feature.
(c) If Sobel gradients are:
********** 5 **********
--- page 6 ---
𝐺𝑥= 10, 𝐺𝑦= 5
Calculate Gradient magnitude and Gradient direction
(d)Assign the gradient direction to the closest HOG orientation bin:
0∘,  45∘,  90∘,  135∘
Solution   • Laplacian Response   (3 Marks)
• Difference of Gaussian (DoG) (2 Marks)
• Gradient Magnitude and Direction (3 Marks)
• HOG Orientation Bin Assignment (2 Marks)
Image Processing Operations – Solution
Given a 3×3 grayscale image patch:
I = [[12, 18, 12], [18, 36, 18], [12, 18, 12]]
(a) Laplacian Response
Laplacian kernel used:
[[0, 1, 0], [1, -4, 1], [0, 1, 0]]
Laplacian response at the center pixel is computed as:
(0×12 + 1×18 + 0×12) + (1×18 − 4×36 + 1×18) + (0×12 + 1×18 + 0×12)
= 18 + (18 − 144 + 18) + 18
= −54
(b) Difference of Gaussian (DoG)
Given Gaussian blurred responses: G(σ1) = 30, G(σ2) = 24
DoG = G(σ1) − G(σ2) = 30 − 24 = 6
A non-zero DoG value indicates the presence of a significant feature such as an
edge or blob.
(c) Gradient Magnitude and Direction
Given Sobel gradients: Gx = 10, Gy = 5
Gradient magnitude: |G| = √(Gx² + Gy²) = √(125) ≈ 11.18
Gradient direction: θ = tan⁻¹(Gy / Gx) = tan⁻¹(0.5) ≈ 26.6°
(d) HOG Orientation Bin Assignment
Given bins: 0°, 45°, 90°, 135°
Computed angle ≈ 26.6°
Closest HOG orientation bin: 45°
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
Solution   • Integral Image – 4 Marks
• compute the sum of pixel values—3 Marks
• integral images allow constant-time computation of box filter -3
Marks
********** 6 **********
--- page 7 ---
Integral Image Computation – Solution
Given grayscale image matrix (4 × 4):
I = [[2, 1, 3, 4], [0, 1, 2, 1], [3, 2, 1, 0], [1, 1, 2, 3]]
1. Construction of Integral Image
An integral image (summed-area table) at location (x, y) contains the sum of all
pixel values above and to the left of that position, inclusive.
The integral image is calculated cumulatively row-wise and column-wise.
Integral Image:
II = [[2, 3, 6, 10], [2, 4, 9, 14], [5, 9, 15, 20], [6, 11, 19, 27]]
2. Sum of Pixel Values Using Integral Image
A 3 × 2 rectangular region starting at position (2,2) covers rows 2–3 and
columns 2–4.
Using the integral image, the sum is computed as:
Sum = II(3,4) − II(1,4) − II(3,1) + II(1,1)
Sum = 20 − 10 − 5 + 2 = 7
Final sum of pixel values = 7
3. Importance of Integral Images
Integral images enable constant-time computation of rectangular (box) filter
responses. Regardless of the filter size, only four memory accesses and a few
arithmetic operations are required. This makes integral images extremely
efficient for real-time applications such as object detection, feature extraction,
and image filtering.
Q3   b The Scale-Invariant Feature Transform (SIFT) is a widely used algorithm for   [10]
CO- 2   detecting and describing distinctive local features that are robust to changes in
SO- 1   imaging conditions.
i.   Explain how scale-space construction using Gaussian filtering enables
BL-2,3,4
the detection of keypoints that are invariant to scale variations in the
image.
ii.   Discuss the role of accurate keypoint localization in SIFT and analyze
how it improves the stability and reliability of extracted features.
iii.   Describe the process of orientation assignment in the SIFT algorithm
and explain how this step ensures rotation invariance.
iv.   With suitable justification, explain why SIFT features outperform
traditional edge and corner detectors when matching images captured
under real-world variations such as changes in illumination, scale, and
viewpoint.
Solution   • Scale-Space Construction and Scale Invariance (3 Marks)
• Keypoint Localization and Its Importance (2 Marks)
• Orientation Assignment and Rotation Invariance (3 Marks)
• Superiority of SIFT over Traditional Edge and Corner Detectors (2
Marks)
The Scale-Invariant Feature Transform (SIFT) is a robust algorithm for
detecting and describing local features in images. It is designed to be invariant
to scale, rotation, and partially invariant to illumination and viewpoint changes.
(a) Scale-Space Construction and Scale Invariance
SIFT achieves scale invariance by constructing a scale space of the image using
Gaussian filtering. The input image is convolved with Gaussian kernels at
different scales (standard deviations). Adjacent Gaussian-blurred images are
********** 7 **********
--- page 8 ---
subtracted to form Difference of Gaussian (DoG) images. Local extrema
(maxima and minima) in the DoG scale space across both spatial location and
scale are selected as keypoints. Since keypoints are detected at characteristic
scales, the same physical feature can be identified even when the image is
resized, making the detection scale invariant.
(b) Keypoint Localization and Its Importance
After detecting potential keypoints, SIFT performs accurate keypoint
localization by fitting a 3D quadratic function to the local sample points. This
step refines the keypoint location and scale, and discards unstable keypoints
with low contrast or those poorly localized along edges. Accurate localization
improves the stability and repeatability of features, reduces sensitivity to noise,
and ensures that only distinctive and reliable keypoints are retained for further
processing.
(c) Orientation Assignment and Rotation Invariance
For each keypoint, SIFT assigns one or more dominant orientations based on
local image gradient directions around the keypoint at the selected scale. A
histogram of gradient orientations is formed, and the peak(s) of this histogram
determine the orientation(s). All subsequent feature descriptors are computed
relative to this orientation, ensuring that the descriptor remains unchanged even
if the image is rotated. This step provides rotation invariance.
(d) Superiority of SIFT over Traditional Edge and Corner Detectors
SIFT features outperform traditional edge and corner detectors because they are
highly distinctive and robust to real-world variations. Unlike simple edge or
corner detectors, SIFT incorporates scale-space analysis, orientation
normalization, and rich local descriptors based on gradient distributions. This
makes SIFT features resilient to changes in illumination, scale, rotation, and
moderate viewpoint differences. As a result, SIFT produces reliable feature
matches across varied imaging conditions, which is essential for tasks such as
object recognition, image matching, and 3D reconstruction.
Q4   a   Consider a set of 2-D feature points extracted from an image:   [10]
CO- 3   (1,1),  (3,3),  (9,9),  (11,11)
SO- 2
BL- 3,4   Assume the number of clusters 𝐾= 2 and the initial cluster centers are given as:
𝜇1 = (1,1), 𝜇2 = (9,9)
Answer the following:
1. Assign each data point to its nearest cluster centre using Euclidean
distance.
2. Calculate the updated cluster centroids after completing one iteration of
the K-means algorithm.
II. In a multi-resolution image matching approach, feature similarity is computed
at different levels of an image pyramid and combined using weighted scores.
Suppose two images produce the following histogram similarity values:
• Pyramid Level 0 (original resolution): similarity score = 0.88
********** 8 **********
--- page 9 ---
• Pyramid Level 1 (reduced resolution): similarity score = 0.96
The corresponding weights assigned to these levels are:
• Level 0 → weight = 1.0
• Level 1 → weight = 0.6
•
Calculate the overall weighted feature similarity score between the two images.
Briefly explain how using multiple pyramid levels improves the robustness of
image similarity measurement.
Solution   • K-Means Clustering (5 Marks)
• Multi-Resolution Image Matching (5 Marks)
I. K-Means Clustering
Given 2D feature points: (1,1), (3,3), (9,9), (11,11)
Number of clusters: K = 2
Initial cluster centers: μ₁ = (1,1), μ₂ = (9,9)
Assignment of Points to Nearest Cluster
Euclidean distance is used as the distance metric.
(1,1): Distance to μ₁ = 0, Distance to μ₂ = √((8)²+(8)²) = 11.31 → Assigned to
Cluster 1
(3,3): Distance to μ₁ = √((2)²+(2)²) = 2.83, Distance to μ₂ = √((6)²+(6)²) = 8.49
→ Assigned to Cluster 1
(9,9): Distance to μ₁ = 11.31, Distance to μ₂ = 0 → Assigned to Cluster 2
(11,11): Distance to μ₁ = 14.14, Distance to μ₂ = 2.83 → Assigned to Cluster 2
Updated Cluster Centroids After One Iteration
Cluster 1 points: (1,1), (3,3)
Updated μ₁ = ((1+3)/2 , (1+3)/2) = (2,2)
Cluster 2 points: (9,9), (11,11)
Updated μ₂ = ((9+11)/2 , (9+11)/2) = (10,10)
II. Multi-Resolution Image Matching
Given similarity scores at different pyramid levels:
Level 0 (original resolution): Similarity = 0.88, Weight = 1.0
Level 1 (reduced resolution): Similarity = 0.96, Weight = 0.6
Overall Weighted Similarity Score
Weighted similarity = (1.0 × 0.88) + (0.6 × 0.96)
= 0.88 + 0.576 = 1.456
Overall weighted feature similarity score = 1.456
Score = 1.456/1.6
Similarity score=0.91
Importance of Using Multiple Pyramid Levels
Using multiple pyramid levels improves robustness by capturing image features
at different spatial resolutions. Higher-resolution levels preserve fine details,
while lower-resolution levels capture global structure and are less sensitive to
noise, illumination changes, and small misalignments. Combining similarity
scores across levels therefore results in a more reliable and stable image matching
process.
Q4   b   In an image retrieval system based on the Bag of Visual Words (BoVW) model,   [10]
CO- 3   three database images are represented by the following visual word histograms:
SO- 2   𝐼1 = [3,1,2,0],𝐼2 = [1,2,0,2], 𝐼3 = [2,0,1,3]
********** 9 **********
--- page 10 ---
BL-3,4,5   A query image has the histogram:
𝑄= [2,1,1,1]
i.   Calculate   the Term   Frequency   (TF)   vectors   for   all   images.
ii. Compute the Document Frequency (DF) and Inverse Document Frequency
(IDF)   for   each   visual   word.
iii.   Determine   the TF-IDF   representation   for   the   query   image.
iv. Using Euclidean distance, identify which image in the database best matches
the query.
Solution   • Calculate the Term Frequency (TF) (2 Marks)
• Compute the Document Frequency (DF) and Inverse Document
Frequency (IDF) (3 Marks)
• TF-IDF representation for the query image (2 Makrs)
• image in the database best matches the query (3 Marks)
Bag of Visual Words (BoVW) with TF–IDF – Solution
Database image histograms:
I₁ = [3, 1, 2, 0]
I₂ = [1, 2, 0, 2]
I₃ = [2, 0, 1, 3]
Query image histogram: Q = [2, 1, 1, 1]
i. Term Frequency (TF) Calculation
Term Frequency (TF) is computed by normalizing each histogram by the total
number of visual words in that image.
TF(I₁) = [3/6, 1/6, 2/6, 0/6] = [0.50, 0.17, 0.33, 0.00]
TF(I₂) = [1/5, 2/5, 0/5, 2/5] = [0.20, 0.40, 0.00, 0.40]
TF(I₃) = [2/6, 0/6, 1/6, 3/6] = [0.33, 0.00, 0.17, 0.50]
TF(Q) = [2/5, 1/5, 1/5, 1/5] = [0.40, 0.20, 0.20, 0.20]
ii. Document Frequency (DF) and Inverse Document Frequency (IDF)
Document Frequency (DF) is the number of images in which a visual word
appears at least once.
DF values:
Word 1: appears in I₁, I₂, I₃ → DF = 3
Word 2: appears in I₁, I₂ → DF = 2
Word 3: appears in I₁, I₃ → DF = 2
Word 4: appears in I₂, I₃ → DF = 2
IDF values (IDF = ln(N / DF)):
IDF₁ = ln(3/3) = 0.00
IDF₂ = ln(3/2) = 0.41
IDF₃ = ln(3/2) = 0.41
IDF₄ = ln(3/2) = 0.41
iii. TF–IDF Representation of Query Image
TF–IDF(Q):
[0.00, 0.08, 0.08, 0.08]
iv. Image Matching Using Euclidean Distance
Euclidean distance is used to compare the TF–IDF query vector with database
image vectors. The image with the minimum distance is considered the best
match.
Computed distances (using TF–IDF vectors):
Distance(Q, I₁) ≈ 0.29
Distance(Q, I₂) ≈ 0.36
Distance(Q, I₃) ≈ 0.33
Best matching image for the query: I₁ (minimum distance)
********** 10 **********
--- page 11 ---
Q5   a   I. Consider the following one-dimensional data points:   [10]
CO-4   1,  3,  6,  11,  13
SO- 1
A Mean Shift algorithm is applied with a kernel window (bandwidth) of 4.
BL- 3
Starting from the initial point 𝑥= 3:
i.   Perform the first iteration of the Mean Shift procedure by identifying all
data points within the window and computing the new mean.
ii.   Use the updated mean as the starting point and perform the second
iteration.
II. Compare and contrast the K-means clustering algorithm with the Mean Shift
clustering method, highlighting   their working principles, assumptions,
advantages, and limitations.
Solution   • Mean Shift Algorithm Numerical– 5 Marks (3+2)
• K-mean and Mean shift difference – 5 Marks
Mean Shift Algorithm – Worked Example
Given 1D data points: 1, 3, 6, 11, 13
Kernel window (bandwidth) = 4
Initial point x = 3
--- First Iteration ---
Points within window [x - 4, x + 4] = [-1, 7]
Included points: 1, 3, 6
Mean = (1 + 3 + 6) / 3 = 10 / 3 ≈ 3.33
--- Second Iteration ---
New window centered at x = 3.33 ⇒ [−0.67, 7.33]
Included points: 1, 3, 6
Mean = (1 + 3 + 6) / 3 = 3.33
II. K-mean and Mean Shift method
Clustering is an unsupervised learning technique used to group similar data
points. K-means and Mean Shift are two widely used clustering algorithms,
each based on different principles and assumptions.
1. Working Principles
K-means clustering partitions the dataset into a predefined number of clusters
(K). It works by initializing K centroids, assigning each data point to the nearest
centroid based on a distance measure (usually Euclidean distance), and then
updating the centroids as the mean of all points assigned to each cluster. This
process is repeated iteratively until convergence.
Mean Shift clustering is a density-based method that does not assume a fixed
number of clusters. It works by placing a window (kernel) around each data
point and iteratively shifting the window toward regions of higher data density
(the mean of points within the window). Points that converge to the same mode
are grouped into the same cluster.
2. Assumptions
********** 11 **********
--- page 12 ---
K-means assumes that clusters are spherical, equally sized, and well separated,
and that the number of clusters K is known in advance.
Mean Shift assumes that clusters correspond to modes (peaks) in the underlying
data density distribution and relies on an appropriate bandwidth parameter to
estimate density.
3. Advantages
K-means is simple to understand, easy to implement, computationally efficient,
and works well for large datasets when clusters are compact and distinct.
Mean Shift does not require prior knowledge of the number of clusters, can
discover arbitrarily shaped clusters, and is well-suited for applications such as
image segmentation.
4. Limitations
K-means is sensitive to the initial placement of centroids, choice of K, and
outliers. It also performs poorly when clusters are non-spherical or have varying
densities.
Mean Shift is computationally expensive, especially for large datasets, and its
performance heavily depends on the choice of bandwidth. An incorrect
bandwidth can lead to over-segmentation or under-segmentation of data.
In summary, K-means is a fast, parametric clustering technique suitable for
large-scale problems with simple cluster structures, while Mean Shift is a non-
parametric, flexible clustering method that can automatically detect the number
of clusters but at a higher computational cost.
Q5   b   i. Why is it necessary to use multiple frames instead of a single frame for   [10]
CO- 2   background modeling in background subtraction techniques?
SO- 2   ii.   Explain the role of N consecutive images in constructing a reliable
background model for motion detection.
BL-3,4
iii.   In background subtraction methods, what problems arise   if the
background reference is built using only one image? How does using N
images overcome these problems?
Solution   Background substraction – 10 Marks (4+4+2)
i. Why is it necessary to use multiple frames instead of a single frame?
Using multiple frames is necessary because a single image cannot accurately
represent the background in real-world video scenes. A single frame may contain
temporary objects, moving entities, noise, illumination variations, or shadows.
These factors can cause incorrect classification of background and foreground.
Multiple frames help capture stable background characteristics over time,
reducing the influence of noise and transient objects.
ii. Role of N consecutive images in constructing a reliable background model
N consecutive images are used to observe pixel behavior over time. By analyzing
intensity values across N frames, the system can estimate statistical properties
such as mean, median, or variance for each pixel. This temporal analysis helps
********** 12 **********
--- page 13 ---
distinguish between background pixels (which remain consistent) and foreground
pixels (which change frequently). As a result, the background model becomes
more robust and reliable for motion detection.
iii. Problems with single-image background reference and how N images
overcome them
If the background reference is built using only one image, several problems arise:
noise is mistaken as motion, shadows or illumination changes cause false
detections, and stationary foreground objects may become part of the
background. Using N images overcomes these issues by averaging or statistically
modeling pixel behavior over time. This approach filters out noise, adapts to
gradual illumination changes, and correctly identifies persistent background
elements, leading to more accurate motion detection.
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
Solution   Affine Transformation of a Triangular ROI (10 Marks)
Given triangle vertices:
A(2, 3), B(6, 3), C(4, 7)
Scaling factors:
Sx = 2 (x-axis), Sy = 4 (y-axis)
Translation: 5 units right, 3 units downward
(i) Homogeneous Transformation Matrices
Scaling matrix:
[ 2 0 0 ]
[ 0 4 0 ]
[ 0 0 1 ]
Translation matrix:
[ 1 0 5 ]
[ 0 1 -3 ]
[ 0 0 1 ]
(ii) Composite Transformation Matrix (T × S):
********** 13 **********
--- page 14 ---
[ 2 0 5 ]
[ 0 4 -3 ]
[ 0 0 1 ]
(iii) Transformed Coordinates:
A'(9, 9)
B'(17, 9)
C'(13, 25)
Summary: The triangle is first scaled about the origin and then translated,
resulting in the above transformed vertices.
Q6   b   I) Discuss the limitations of using an exhaustive (brute-force) feature matching   [10]
CO- 3,5   strategy when comparing descriptors from two images. Consider aspects such as
SO- 2   accuracy, ambiguity, and computational cost.
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
Solution   • Feature Matching Limitations (5 Marks)
• CNN Convolution Layer Analysis (5 Marks)
I) Limitations of Exhaustive (Brute Force) Feature Matching
An exhaustive or brute-force feature matching strategy compares every
descriptor from the first image with every descriptor from the second image
using a distance metric such as Euclidean distance.
1. Computational Cost:
Brute-force matching is computationally expensive, especially for images
having a large number of features. The time complexity grows quadratically,
making it unsuitable for real-time or large-scale applications.
2. Ambiguity in Matching:
Descriptors may look similar across different regions, leading to multiple
potential matches. This ambiguity can cause incorrect correspondences,
particularly in repetitive textures.
3. Reduced Accuracy in Noisy Conditions:
Noise, illumination changes, or viewpoint variations can distort descriptors,
causing brute-force matching to produce false matches. Without additional
constraints, the accuracy may degrade significantly.
II) Convolutional Neural Network Layer Analysis
Given:
Input image size: 8 × 8
Kernel size: 5 × 5
Stride: 2
********** 14 **********
--- page 15 ---
Zero padding: 1
Number of filters: 3
(i) Output Feature Map Size:
Output dimension formula:
(N − F + 2P)/S + 1
Where N = 8, F = 5, P = 1, S = 2
(8 − 5 + 2×1)/2 + 1 = (5)/2 + 1 = 2.5 + 1 ≈ 3.5
Taking floor value: 3
Therefore, output size per filter = 3 × 3
(ii) Number of Trainable Parameters:
Weights per filter = 5 × 5 = 25
Bias per filter = 1
Total parameters per filter = 26
Total trainable parameters = 26 × 3 = 78
Q7   a   i.   What were the main efficiency limitations in the original R-CNN   [10]
CO- 5   framework?
SO- 1   ii.   Describe how Fast R-CNN redesigned the detection pipeline to overcome
these inefficiencies.
BL-2
iii.   What was the major speed bottleneck that still remained in Fast R-CNN,
and how was it addressed in Faster R-CNN?
Solution   •   i) Efficiency Limitations of Original R-CNN (4 Marks)
•   ii) Improvements Introduced by Fast R-CNN (3 Marks)
•   iii) Remaining Bottleneck in Fast R-CNN and Faster R-CNN
Solution (3 Marks)
Evolution of the R-CNN Object Detection Frameworks
i) Efficiency Limitations of Original R-CNN
The original R-CNN (Region-based Convolutional Neural Network) framework
suffered from several efficiency limitations:
1. Redundant Computation:
Each region proposal (around 2000 per image) was independently passed
through a CNN, leading to repeated and expensive convolution operations.
2. Multi-stage Training Pipeline:
R-CNN required separate stages for CNN fine-tuning, SVM training, and
bounding box regression, increasing complexity and training time.
3. Large Storage Requirements:
Extracted region features were stored on disk, consuming hundreds of gigabytes
and slowing down training and experimentation.
ii) Improvements Introduced by Fast R-CNN
Fast R-CNN redesigned the detection pipeline to improve efficiency in the
following ways:
1. Single Forward Pass:
********** 15 **********
--- page 16 ---
The entire image is passed once through the convolutional layers to generate a
shared feature map.
2. ROI Pooling Layer:
Region of Interest (ROI) Pooling extracts fixed-size feature vectors from the
shared feature map, eliminating redundant CNN computations.
3. End-to-End Training:
Classification and bounding box regression are combined into a single network
trained using a multi-task loss, simplifying training and improving speed.
iii) Remaining Bottleneck in Fast R-CNN and Faster R-CNN Solution
Despite improvements, Fast R-CNN still faced a major speed bottleneck:
1. Selective Search:
Fast R-CNN relied on selective search for region proposals, which is
computationally expensive and operates outside the neural network.
Faster R-CNN addressed this limitation by introducing the Region Proposal
Network (RPN), which shares convolutional features with the detection network
and generates region proposals efficiently within the CNN, enabling near real-
time object detection.
Q7   b   I.) A convolutional neural network processes a grayscale image, producing the   [10]
CO- 5   following 4 × 4 feature map after the first convolution layer:
SO- 2   5 8 12 6
7 9 15 10
BL-3,4   𝐺= [   ]
4 6 20 18
3 5 16 14
a) State the purpose of the pooling layer in CNNs.
b) Apply 2 × 2 pooling with stride 2 and compute the resulting feature maps
using:
a)Max Pooling
b) Average Pooling
c)Min Pooling
Show intermediate calculations clearly.
II.) The Faster R-CNN framework originally used RoIPool for extracting
fixed-size feature maps from proposal regions.
i.   Explain how quantization in the RoIPool layer introduces localization
inaccuracies during region pooling.
ii.   Discuss the impact of this quantization error on object detection accuracy,
particularly for small objects.
iii.   Describe how RoIAlign eliminates this issue and improves spatial
precision.
Solution   • Pooling Numerical (5 Marks)
• Faster R-CNN   (5 Marks)
Solution
I. Pooling in Convolutional Neural Networks
********** 16 **********
--- page 17 ---
Given 4×4 feature map G:
5 8 12 6
7 9 15 10
4 6 20 18
3 5 16 14
a) Purpose of pooling layer
The pooling layer reduces the spatial dimensions of feature maps while
retaining important information. It decreases computational cost, controls
overfitting, and introduces translation invariance by summarizing local
neighborhoods.
b) 2×2 Pooling with stride 2
Pooling regions:
Region 1: [[5, 8], [7, 9]]
Region 2: [[12, 6], [15, 10]]
Region 3: [[4, 6], [3, 5]]
Region 4: [[20, 18], [16, 14]]
i) Max Pooling
Region 1: max(5,8,7,9) = 9
Region 2: max(12,6,15,10) = 15
Region 3: max(4,6,3,5) = 6
Region 4: max(20,18,16,14) = 20
Resulting feature map:
[9 15
6 20]
ii) Average Pooling
Region 1: (5+8+7+9)/4 = 7.25
Region 2: (12+6+15+10)/4 = 10.75
Region 3: (4+6+3+5)/4 = 4.5
Region 4: (20+18+16+14)/4 = 17
Resulting feature map:
[7.25 10.75
4.5   17]
iii) Min Pooling
Region 1: min(5,8,7,9) = 5
Region 2: min(12,6,15,10) = 6
Region 3: min(4,6,3,5) = 3
Region 4: min(20,18,16,14) = 14
Resulting feature map:
[5 6
3 14]
II. RoIPool vs RoIAlign in Faster R-CNN
RoIPool introduces localization inaccuracies because it quantizes floating-point
proposal coordinates to integer values. This rounding causes misalignment
between the original image and feature maps, leading to loss of spatial precision
during pooling.
This quantization error significantly affects object detection accuracy, especially
for small objects, where even minor spatial shifts can cause incorrect feature
extraction, resulting in missed detections or poor bounding box localization.
RoIAlign eliminates quantization by avoiding coordinate rounding and instead
uses bilinear interpolation to compute exact feature values at precise locations.
********** 17 **********
--- page 18 ---
This preserves spatial correspondence, improving localization accuracy and
overall object detection performance.
********** 18 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 49ce603ecacd

- Departments: AI and Machine Learning, Artificial Intelligence
- Programmes: BTech AI 7012, BTech AIML 7053, MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AIML_7053/COMPUTER VISION FOR AI/ANS_COMPUTER VISION FOR AI(702AI0C029)_2025-2026.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This synoptic contains 18 pages.
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
(i) Barcode scanner on a   retail point-of-sale (POS):
Recognition of edges and parallel lines
(ii) Detection   of   suspicious   activities   like   theft:
understanding the context, semantics, and temporal
sequence of events.
Solutio   (i)   Barcode scanner on a retail point-of-sale (POS): Low-
n   level features. Applies edge detection algorithms and
locates the edges and lines. (2M)
(ii)   Detection of suspicious activities like theft: High-level
features.   Detecting   an   "activity"   requires
understanding the context, semantics, and temporal
sequence of events, which involves complex reasoning
about objects and their interactions over time. (2M)
CO-2;   b. Why is Rotated BRIEF used instead of BRIEF? For Rotated   [04]
SO-1;
BRIEF, rotate a pixel P1 around the key point by 45°, where
BL-3
coordinates of P1= (3,5) and calculate new coordinates.
Solutio   • BRIEF is Sensitive to rotation of image
n
• rBRIEF improves BRIEF by aligning the image patch
to the orientation of the key point. (2M)
********** 1 **********
--- page 2 ---
• Rotate the set, S according to the orientation of key
points
x’ = x cos(θ) – y sin(θ)   y’ = x sin(θ) + y cos(θ)
x' = -1.4142 ≈ -1   y' = 5.6568 ≈ 6
P1(3,5)  P1’(-1,6) (2M)
CO-3;   c. Consider that Image1 has one keypoint descriptor, D1=   [04]
SO-1;   [0.3, 0.4, 0.6].
BL-2   Image2 has the three keypoints. Corresponding descriptors
are
D21 = [0.2, 0.5, 0.6], D22 = [0.9, 0.1, 0.4], D23 = [0.4, 0.4, 0.5]
(i) Use Brute Force matching to find the best match for D1.
(ii) How many Euclidean distances are to be calculated if
image1 has 2 key points and image2 has 5 key points.
Solutio   Euclidean distance between
n   D1 and D21: 0.173
D1 and D22: 0.678
D1 and D23: 0.1
Best match for D1 is D23 and D21(3M)
10 Euclidean distance (1M)
CO-4;   d. Discuss the stopping conditions in K-means clustering.   [04]
SO-4;
BL-2
Solutio   1. Centroids Do Not Change (Convergence)
n
2. Maximum Number of Iterations Reached
3. Minimal Change in Total Within-Cluster Sum of
Squares (WCSS)
4. No Change in Cluster Assignments
2M for each (any two of the above)
CO-5;   e.   State and explain two reasons to justify that ‘Faster RCNN’   [04]
SO-5;
is faster than ‘Fast RCNN’.
BL-6
Solutio   1. Faster RCNN uses Region Proposal Network (RPN)
n
instead of selective search method, which takes long.
Selective search is handcrafted method. RPN is based on
the network. (2M)
2. Fast RCNN have several stages in sequence. Stages are
Selective Search, CNN, feature map, ROI pooling, FC
layers, Softmax, BB regressor. Faster R-CNN builds a
network that has only a single stage, CNN, RPN, FC
layers, Softmax, BB regressor. (2M)
********** 2 **********
--- page 3 ---
Q. 2   a   For Histogram of Gradient (HoG) descriptor,   [10]
CO-1;
i)   Write the steps in brief to determine HoG of an image
SO-1;
BL-3   and to classify the objects
ii) Consider the following image and gradient filters, Gx
and Gy. Determine Gradient magnitudes and angles
for the highlighted pixels.
iii) Plot 9-bin histogram of gradients.
Solutio   i)   Steps   [10]
n
 Crop image to obtain image patch and Divide patch
by cells of 8 ⨯ 8 pixels
 Compute the gradients for pixels in the patch
(localized portion)
 Make histograms using the computed gradients
(magnitude and orientation) for each cell
 Apply normalization with neighboring histograms
 Concatenate all histograms to form a vector
 Vector represents feature descriptor of the image
patch
 Use features to compare objects Or use features to
train classifier
(4M)
ii)
(4M)
********** 3 **********

[Text in pictures on this page, read by OCR]
10 10 10 10 10 10 10 10

10 120 -120 10 10 120 120 1

10 120 -120 10 10 -120 -120 |]

10 10 10 10 10 10 10 10
Gx Gy

10 169.7 169.7 10 10 45 135 10
10 169.7 169.7 10 10 135 45 10

10 10 10 “J E 10 10 10
10 10 10 10 10 10 10 10

Magnitude Angle
--- page 4 ---
0 0   2×127.   2×42.   0   0   2×42.   2×127   0
3   4   4   .3
=254.6   =84.8   =84.8   =254.
6
0 2   40   60   80   10   120   140   16
0   0   0
Histogram
(2M)
Q2   b For Difference of Gaussian (DoG),   [10]
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
********** 4 **********

[Text in pictures on this page, read by OCR]
Io1 Io2

20 28 32 28 20 24 34 40 34 2
28 48 60 48 28 34 56 72 56 3
=|/32 60 80 60 32} =|40 72 96 72 4
28 48 60 48 28 34 56 72 56 3
20 28 32 28 20 24 34 40 34 2

Image filtered by Gaussian Image filtered by Gaussia
filter with ol =1 filter with o2 =2
--- page 5 ---
Solutio   i) DoG   [10]
n
• Edge enhancement algorithm
• Use two Gaussian filters to blur the image
•   Find difference of blurred and less blurred image
• Where I is grey image, Gσ1 and Gσ2 are Gaussian
filters with sigma, σ1 and σ2 respectively
•   Gaussian kernel suppresses high-frequency
spatial information
•   Subtraction preserves spatial information that has
frequency which is not common to filtered images
•   Thus, DoG is a spatial band-pass filter
(4M)
ii) Increase low and high sigma value to smoothen the
image before determining DoG (3M)
iii)
 Highlighted pixels are edge pixels. (3M)
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
Required gradient filter
********** 5 **********
--- page 6 ---
Solution
(3M)
𝑅 = 𝑑𝑒𝑡(𝐻) − 𝑘. {𝑡𝑟𝑎𝑐𝑒(𝐻)}2
𝑅 = {(700 × 700) − (225 × 225)} − 0.04 × {700 + 700}2
𝑅 = 360975 (2M)
R> 100000, it is a corner point, (2M)
If threshold is changed to 1000000, point will be a flat
point.
Q3   b For the following image   [10]
CO-2;   (i)   Compute the integral image
SO-1;
(ii)   Apply the given filters on the highlighted region of
BL-4
the integral image to construct its Hessian matrix.
(iii)   Using this Hessian matrix, calculate whether the
highlighted point is a key point. (For Hessian matrix,
constant, W = 0.9, and threshold = 10)
********** 6 **********

[Text in pictures on this page, read by OCR]
1111 11111
15 5 0 15 10 15 1
I,=]1 10 10 0 l,=|1 5 10 15 6
1 15 15 0 100 06
11 6 6 116 6 6
(3M)
a TE
1 25 25 1
=]1 100 100 6 111 11
1 225 225 0 6 1 25 100 225 1
lo. el =|1 25 100 225 6
10 0 p 6
11 6 6 6
1 11
25 50 0
Iy.ly=]1 50 100 0
0 0 0
--- page 7 ---
Solutio   Integral Image
n   1   2   3   4   5
2   4   6   8   10
3   6   10   14   18
4   8   14   20   26
5   10   18   26   34
(4M)
𝐿𝑥𝑥 = −2(14 − 3 − 8 + 2) + (8 − 2) + (26 − 5 − 14 + 3)
= 6
𝐿𝑦𝑦 = −2(14 − 8 − 3 + 2) + (8 − 2) + (26 − 14 − 5 + 3)
= 6
𝐿𝑥𝑦 = (4 − 2 − 2 + 1) + (20 − 14 − 14 + 10)
− (8 − 4 − 6 + 3) − (8 − 6 − 4 + 3) = 1
(3M)
𝐿𝑥𝑥(𝑝, 𝜎)   𝐿𝑥𝑦(𝑝, 𝜎)   6 1
𝐻(𝑝, 𝜎) = [   ] = [   ]
𝐿𝑥𝑦(𝑝, 𝜎)   𝐿𝑦𝑦(𝑝, 𝜎)   1 6
2
𝐷𝑒𝑡(𝐻) = 𝐿𝑥𝑥. 𝐿𝑦𝑦 − (𝑊. 𝐿𝑥𝑦) = 36 − (0.9 × 1)2 = 35.19
(2M)
𝐷𝑒𝑡(𝐻) (>10) indicates that the highlighted point is a key
point. (1M)
Q4   a For Scale-Invariant Feature Transform (SIFT),   [10]
CO-2;   i) List and explain the steps to determine the SIFT
SO-5;
descriptor in brief. Write the role of each step.
BL-3,4
ii) Illustrate key point orientation assignment in details.
********** 7 **********

[Text in pictures on this page, read by OCR]
1 1
1 1
1 2
1 2
1 2
image
1 1
1 1
—2 -2
1 1

1 1

1
1

xy
--- page 8 ---
Solutio   Steps
n   1. Construct a Scale Space:
• Generate images over multiple scales
• Ensures that features are scale-independent
2. Key point Localisation:
• Select key points based on measure of stability
• Ignore other key points to avoid false keypoints
3. Orientation Assignment:
• Compute best orientations for each key point region
• To ensure that keypoints are rotation invariant
4. Keypoint Descriptor:
• Use local image gradients at selected scale and
rotation
(6M)
Orientation Assignment
• Each keypoint is identified by
•   location in image
•   Scale at which key point was selected
• Use a 16x16 pixels (window) around each key point
in the original image
• Window is divided into 16 cells of 4x4 pixels
********** 8 **********
--- page 9 ---
• Determine gradients of each pixel in X and Y
direction
• Determine magnitudes and orientations of gradients
for each pixel of each cell
•   Divide orientation (0 to 360o) into 8 bins
• Draw Histogram on circular scale
(4M)
Q4   b   For Fast Library for Approximate Nearest Neighbors   [10]
CO-3;
(FLANN),
SO-1;
BL-3,5   (i) Construct a K-D tree for the following 3-dimensional
descriptors of Image 1.
Descriptors: (3, 1, 4), (3, 2, 5), (2, 3, 7), (2, 1, 3), (2, 4,
5), (1, 4, 4), (1, 2, 1), (0, 5, 7), (4, 3, 4), (6, 1, 4), (5, 2,
5), (5, 3, 6), (4, 0, 6), (4, 1, 2), (7, 1, 6), (7, 0, 5).
(ii) Choose a match for the descriptor (7, 1, 7) of Image 2
Solutio   Level 0 (root): split by x,
n
Level 1: split by y,
********** 9 **********

[Text in pictures on this page, read by OCR]
Z

/

7 <

The orientations all

. . . ended up in two bins:
Orientations in each of 41 in one bin, 5 in the

the 16 pixels of the cell other. (rough count)

511000000
--- page 10 ---
Level 2: split by z,
… then repeat.
Split into two groups: Root = (4, 3, 4)
Left subtree (x < 4): (0,5,7), (1,4,4), (1,2,1), (2,3,7), (2,1,3),
(2,4,5), (3,1,4), (3,2,5)
Right subtree (x >= 4): (4,0,6), (4,1,2), (5,2,5), (5,3,6),
(6,1,4), (7,1,6), (7,0,5)
(2M)
Build left subtree (split by y), Node: (2,3,7)
Left-left (y < 3): (3,1,4), (2,1,3), (1,2,1), (3,2,5)
Left-right (y > =3): (2,4,5), (1,4,4), (0,5,7)
Build right subtree (split by y), node = (6,1,4)
Right-left (y < 1): (4,0,6), (7,0,5)
Right-right (y > =1): (4,1,2), (5,2,5), (5,3,6), (7,1,6)
(2M)
Level 2 (split by z)
Left-left group (y < 3): node = (3,1,4)
Left (z < 4): (1,2,1), (2,1,3)
Right (z > =4): (3,2,5)
Left-right group (y > 3): node = (2,4,5)
Left (z < 5): (1,4,4)
Right (z >= 5): (0,5,7)
(2M)
Right-left group (y < 1): node = (4,0,6)
Left (z < 6): (7,0,5)
Right (z > =6): none
Right-right group (y > 1): node = (5,2,5)
Left (z < 5): (4,1,2)
Right (z > =5): (5,3,6), (7,1,6)
(2M)
Query descriptor (Image 2): (7, 1, 7)
Nearest match (Image 1): (7, 1, 6)
Euclidean distance: 1.00
(2M)
There are several variants of the tree
********** 10 **********
--- page 11 ---
Q5   a Describe steps for descriptor matching using Bag of Visual   [10]
CO-3;
Words. Explain it with example images.
SO-1;
BL-5   Explain why Bag of Visual words method is preferred over
pair wise feature matching?
Solutio
Explanation
n
•   Pairwise descriptor matching is computationally
expensive.
•   Instead of comparing pairwise descriptors, group
descriptors with similar values to form clusters
• Use K-means clustering to generate ‘K’ clusters
• Each cluster has a centroid
•   Centroid represents all the descriptors within the
cluster
•   Centroid or cluster center is visual word the cluster
•   Computational complexity is low because, K
centroids are compared not N descriptors
(3M)
First image
1. Extract descriptors of first image
• Choose strong key points
• Determine corresponding descriptors
2. Apply K-means clustering on descriptors
• Groups similar descriptors
•   Generate K groups or clusters
• Determine Cluster mean, also called cluster centres
•   Set of K clusters is a visual vocabulary
• Length of each cluster center is length of feature
descriptor
• For SIFT, it is 128
Second image
1. Extract feature of key points of second image
2. For each key point, find the nearest cluster from K
clusters of first image
3. Assign the nearest cluster of first image to descriptor
of the second image
********** 11 **********
--- page 12 ---
4. There can be several descriptors of second image
which are assigned a particular cluster of first image
5. Generate Histogram of K visual words for the image
Match histograms of two images.
(7M) for description and at least one example image
Q5   b For segmentation of images,   [10]
CO-4;   (i) List the limitations of K-Means algorithm and Mean shift
SO-2;   algorithm.
BL-6
(ii) The following dataset contains pixels of color image.
Apply K-means clustering with K=3 clusters for one
iteration. Points are
 P1=[255,0,0]
 P2=[0, 255, 50]
 P3=[0, 0, 255]
 P4=[250, 10, 10]
Initial   centroids   are   - C1=P1=[255,0,0], C2=P3=
[0,0,255]
(iii) Calculate updated values of centroids
Solutio   (i) Limitations of K-means
n   • Need to choose the value of K
• Converges to a local minimum of WCSS
•   Sensitive to initialization of centroid
•   It is sensitive to rescaling
•   Sensitive to outliers
• Segments “spherical” clusters, does not work if
clusters have a complex geometric shape
Limitations of Mean Shift Algorithm
 Clustering depends on the choice of window size
(bandwidth) which can lead to under or over
segmentation
 Computationally more expensive than K-means
 Slow, especially for high-resolution images
 Can identify noisy pixel as clusters
 Finds arbitrary number of clusters
(4 M)
(ii) Distance of points to C1 = [255,0,0]
P1: 0
P2: 130050
P3: 130050
P4: 225
Distance of points to C2 = [0,0,255]
P1: 130050
P2: 130050
P3: 0
P4: 122625
Choose nearest centroid
 P1 → assign C1
 P2 → tie; but both equal  assign C2
********** 12 **********
--- page 13 ---
 P3 assign C2
 P4 → assign C1
   Cluster 1 members: P1, P4
   Cluster 2 members: P2, P3
Updated centroids-
Cluster 1: P1=(255,0,0), P4=(250,10,10)
 RC1=(255+250)/2=252.5
 GC1=(0+10)/2=5.0
 BC1=(0+10)/2=5.0
Update centroid, C1= (252.5, 5.0, 5.0)
Cluster 2: P2=(0,255,0), P3=(0,0,255),
 RC2=(0+0)/2=0
 GC2=127.5
 BC2=127.5
Update centroid, C2= (0,127.5,127.5)
C3 can be P2 or P4. Depending on the choice update centroids
(6M)
Q 6   a   Using the Lucas–Kanade optical flow method,   10
CO-5;   (i) Derive the mathematical relationship used to determine
SO-4;   the velocity vector of a moving object in an image
BL-3   sequence.
(ii) State and explain the assumptions made in this
derivation.   discuss why   these assumptions   are
necessary, and how they can be addressed or relaxed
when they are not satisfied.
Solutio   •   If a point, x in the image at time t moves to other
n   location at time (t+dt), its intensity does not change
• Therefore dt is assumed to be small
I(x+dx, y+dy, t+dt) = I(x,y,t)
• Taylor series expansion
I(x+dx, y+dy, t+dt) = I(x,y,t) + (dI/dx)δx +(dI/dy)δy +
(dI/dt)δt +[(d2I/dx2)δx +(d2I/dy2)δy + (d2I/dt2)δt]/2 + ...
Where, dI/dx, dI/dy and dI/dt are image gradients along
horizontal axis, vertical axis and time
•   If higher order derivatives are neglected,
(dI/dx)δx + (dI/dy)δy + (dI/dt)δt = 0
(dI/dx)δx/δt + (dI/dy)δy/δt + (dI/dt)δt/δt = 0
(dI/dx)Vx + (dI/dy)Vy + (dI/dt) = 0,
Where, Vx = δx/δt and Vy = δy/δt
• Determine Vx and Vy to find movement over time
(dI/dx)Vx + (dI/dy)Vy + (dI/dt) = 0
• Use interest points in the optical flow function
•   Select a set of interest points in a frame of video
********** 13 **********
--- page 14 ---
• Determine the locations of same interest points in the
next frame
• Determine velocity vector
• Use velocity vector to track the motion of interest
points between two frames
• Method work best with slow-moving objects
• Assume that 2 consecutive frames are separated by a
small time increment (dt) such that objects are not
displaced significantly
(dI/dx)Vx + (dI/dy)Vy + (dI/dt) = 0
Or
Ix (q)Vx + Iy (q)Vy = - It (q)
Where,
•   Ix and Iy are pixel intensity gradients along x and y
direction at interest point, q
• Vx and Vy are velocities along x and y direction
•   It is change in pixel intensity of q between two
consecutive frames
• Use 3x3 window around the interest point, q
• Assume that all nine points have the same motion
between two consecutive frames
• Where q1,q2,…,qn denote pixels inside the window
(ex: n = 9)
•   All pixels satisfy optical equation
Av=b
[Vx , Vy]T = (ATA)-1(AT)(-b)
********** 14 **********
--- page 15 ---
• Determine velocity vector for every pixel in the
image to estimate the optical flow
• Few pixels (e.g., feature points like corners or edges)
are tracked to reduce computational cost
• Method to find Vx and Vy is valid for small
displacements (low velocity)
• For large displacements (more then 2 pixels) the
method cannot be used
• Because second order derivative of Taylor Series
expansion dominates
•   Therefore construct image pyramid such that large
velocities   reduce   to   small   displacements   in
subsampled images
(6M) for description
(2M) for assumptions
(2M) for solution
Q 6   b   Design an appropriate Convolutional Neural Network   [10]
CO-5;
(CNN) model with the following architecture specifications
SO-1;
BL-6   for an input RGB image of size 32 × 32 for 10 classes
 One convolutional layer with 32 filters, each of size
3×3
 One max pooling layer with pool size (2×2)
 One dropout layer with probability 0.2
 One flatten layer
 Two dense (fully connected) layers
 No padding (i.e., "valid" convolution)
   Stride = 1 for convolution
i) Draw architecture and show the shape of output after
each layer. Do not consider bias terms at any layer.
ii) Specify activation functions for the layers
********** 15 **********
--- page 16 ---
Solutio   Layer   Description   Parameters /   Activati   Outp
n   Details   on   ut
Functio   Shape
n
Input   Input image   Size = 32×32×3 —   (32,
32, 3 )
Conv2D   Convolution   Filter size = 3×3,   ReLU   (30,
with 32   stride = 1, no   30,
filters of   padding → output   32)
size 3×3   size =
(32−3+1)×(32−3+
1) = 30×30
MaxPooling   Pooling   Pool size = (2×2), —   (15,
2D   layer   stride = 2 →   15,
output size = 30/2   32)
= 15
Dropout   Regularizati   Dropout rate = 0.2 —   (15,
on   15,
32)
Flatten   Converts   15×15×32 = 7200 —   (7200
3D tensor to   )
1D vector
Dense (Fully   Fully   Units = 128   ReLU   (128, )
Connected   connected   (assumed
1)   layer   reasonable for
intermediate
layer)
Dense (Fully   Output   Units = 10 (for   Softmax   (10,)
Connected   layer   example, 10
2)   classes)
(4M) Architecture
(6M) shape at each layer
Q 7   a   For Region based Convolutional Network (RCNN),   [10]
CO-5;   i) Draw architecture and write the role of each step
SO-4;   ii) Explain selective search algorithm in details
BL-3
********** 16 **********
--- page 17 ---
Solutio
n
(5M)
ii) Selective search algorithm
 Generate 2,000 region proposals using the Selective
Search algorithm. Input each region proposal into CNN
   Extract a feature vector of length, 4096 from each region
proposal from CNN
 Use a pre-trained SVM algorithm to classify the region
proposal to either the background or one of the object
classes.   Refine bounding box   predictions   using
bounding box regression
 Segment the image into regions. Regions have similarity
in color, texture or any other parameter
 Use graph segmentation to capture the regions. Merge
regions into larger regions iteratively. Merged regions
are called region proposals
 Assume that the image is a graph of vertices (nodes)
 Edges connect the nodes. Assign weight to each edge.
Weight is dependent on the distance between the nodes
 Distance can be color difference, texture difference or
any
 Nodes having low distance have low weight
 Connect nodes with low weight using edges
 Merge edges with weight less than a threshold
(5M)
********** 17 **********

[Text in pictures on this page, read by OCR]
Input Image

Selective Search
2000 region Proposals

Warp and resize to
224x224

CNN (Ex: Alexnet)

Feature Vector

Pa
SVM Classifier BB regressor
I |

Predict Class Refined Box
--- page 18 ---
 Merged edges are called components. Nodes which are
not merged are the ones which have large distance
Q 7   b   For Single Shot Detector, justify the use of multiple boxes [10]
CO-5;   to detect object of different scale. Explain with suitable
SO-4;   diagrams.
BL-3
Solutio   The SSD is based on the use of convolutional networks
n   that produce multiple bounding boxes of various fixed
sizes and scores the presence of the object class instance
in those boxes, followed by a non-maximum suppression
step to produce the final detections.
Each input image is divided into grids of various sizes
and at each grid, the detection is performed for different
classes and different aspect ratios.
A score is assigned to each of these grids that indicates
how well an object matches in that grid.
Non maximum supression is applied to get the final
detection from the set of overlapping detections.
It uses different grid sizes to detect objects of different
sizes.
The multi-scale feature maps are added to the end of the
truncated backbone model.
These multi-scale feature maps reduce in size progressively,
which allows the detections at various scales of the image.
The convolutional layers vary for each feature layer.
The addition of each extra layer produces a fixed number of
predictions using the convolutional filters in them.
For example, a feature layer of size m x n with p channels,
the minimal prediction parameter that gives a decent
detection is a 3 x 3 x p small kernel. Such kernel gives us the
score for a category, or a shape offset relative to the default
box coordinates.
Justification (5M)
Explanation (5M)
********** 18 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper faa162b56430

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_AIML_7053/COMPUTER VISION FOR AI/ANS_COMPUTER VISION FOR AI(702AI0C029)_2025-2026_faa162b564.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
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
Solutio   (i) Barcode scanner on a retail point-of-sale (POS): Low-
n   level features. Applies edge detection algorithms and
locates the edges and lines. (2M)
(ii)   Detection of suspicious activities like theft: High-level
features.   Detecting   an   "activity"   requires
understanding the context, semantics, and temporal
sequence of events, which involves complex reasoning
about objects and their interactions over time. (2M)
CO-2;   b. Why is Rotated BRIEF used instead of BRIEF? For Rotated [04]
SO-1;
BRIEF, rotate a pixel P1 around the key point by 45°, where
BL-3
coordinates of P1= (3,5) and calculate new coordinates.
Solutio   • BRIEF is Sensitive to rotation of image
n
• rBRIEF improves BRIEF by aligning the image patch
to the orientation of the key point. (2M)
********** 1 **********
--- page 2 ---
• Rotate the set, S according to the orientation of key
points
x’ = x cos(θ) – y sin(θ)   y’ = x sin(θ) + y cos(θ)
x' = -1.4142 ≈ -1   y' = 5.6568 ≈ 6
P1(3,5) → P1’(-1,6) (2M)
CO-3;   c. Consider that Image1 has one keypoint descriptor, D1=   [04]
SO-1;   [0.3, 0.4, 0.6].
BL-2   Image2 has the three keypoints. Corresponding descriptors
are
D21 = [0.2, 0.5, 0.6], D22 = [0.9, 0.1, 0.4], D23 = [0.4, 0.4, 0.5]
(i) Use Brute Force matching to find the best match for D1.
(ii) How many Euclidean distances are to be calculated if
image1 has 2 key points and image2 has 5 key points.
Solutio   Euclidean distance between
n   D1 and D21: 0.173
D1 and D22: 0.678
D1 and D23: 0.1
Best match for D1 is D23 (3M)
10 Euclidean distance (1M)
CO-4;   d. Discuss the stopping conditions in K-means clustering.   [04]
SO-4;
BL-2
Solutio   1. Centroids Do Not Change (Convergence)
n
2. Maximum Number of Iterations Reached
3. Minimal Change in Total Within-Cluster Sum of
Squares (WCSS)
4. No Change in Cluster Assignments
1M for each
CO-5;   e.   State and explain two reasons to justify that ‘Faster RCNN’   [04]
SO-5;
is faster than ‘Fast RCNN’.
BL-6
Solutio   1. Faster RCNN uses Region Proposal Network (RPN)
n
instead of selective search method, which takes long.
Selective search is handcrafted method. RPN is based on
the network. (2M)
2. Fast RCNN have several stages in sequence. Stages are
Selective Search, CNN, feature map, ROI pooling, FC
layers, Softmax, BB regressor. Faster R-CNN builds a
network that has only a single stage, CNN, RPN, FC
layers, Softmax, BB regressor. (2M)
********** 2 **********
--- page 3 ---
Q. 2   a   For Histogram of Gradient (HoG) descriptor,   [10]
CO-1;
i) Write the steps in brief to determine HoG of an image
SO-1;
BL-3   and to classify the objects
ii) Consider the following image and gradient filters, Gx
and Gy. Determine Gradient magnitudes and angles
for the highlighted pixels.
iii) Plot 9-bin histogram of gradients.
10 10 10 10   −1 0 1   −1 −2 −1
10 𝟓𝟎 𝟓𝟎 10   [ −2 0 2 ]   [ 0   0   0 ]
[   ]
10 𝟓𝟎 𝟓𝟎 10   −1 0 1   1   2   1
10 10 10 10
Image   Gx   Gy
Solutio   i) Steps   [10]
n
• Crop image to obtain image patch and Divide patch
by cells of 8 ⨯ 8 pixels
• Compute the gradients for pixels in the patch
(localized portion)
• Make histograms using the computed gradients
(magnitude and orientation) for each cell
• Apply normalization with neighboring histograms
• Concatenate all histograms to form a vector
• Vector represents feature descriptor of the image
patch
• Use features to compare objects Or use features to
train classifier
(5M)
ii)
10 10   10 10   10   10   10 10
10 𝟏𝟐𝟎 −𝟏𝟐𝟎 10   10 𝟏𝟐𝟎   𝟏𝟐𝟎 10
[   ]   [
10 𝟏𝟐𝟎 −𝟏𝟐𝟎 10   10 −𝟏𝟐𝟎 −𝟏𝟐𝟎 10
10 10   10 10   10   10   10 10
Gx   Gy
10   10   10 10   10 10   10 10
10 𝟏𝟔𝟗. 𝟕 𝟏𝟔𝟗. 𝟕 10   10 𝟒𝟓 𝟏𝟑𝟓 10
[   ]   [   ]
10 𝟏𝟔𝟗. 𝟕 𝟏𝟔𝟗. 𝟕 10   10 𝟏𝟑𝟓 𝟒𝟓 10
10   10   10 10   10 10   10 10
Magnitude   Angle
iii) (4M)
********** 3 **********
--- page 4 ---
0 0   2×127. 2×42. 0   0   2×42. 2×127 0
3   4   4   .3
=254.6 =84.8   =84.8 =254.
6
0 2   40   60   80 10 120   140   16
0   0   0
Histogram
(1M)
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
Solutio   i) DoG
n
• Edge enhancement algorithm
• Use two Gaussian filters to blur the image
• Find difference of blurred and less blurred image
• Where I is grey image, Gσ1 and Gσ2 are Gaussian
filters with sigma, σ1 and σ2 respectively
• Gaussian kernel suppresses high-frequency
spatial information
•   Subtraction preserves spatial information that has
frequency which is not common to filtered images
• Thus, DoG is a spatial band-pass filter
(4M)
********** 4 **********
--- page 5 ---
ii) Increase low and high sigma value to smoothen the
image before determining DoG (4M)
iii)
4 6   8 6 4
6 8   𝟏𝟐 8 6
DoG = 8 𝟏𝟐 𝟏𝟔 𝟏𝟐 𝟖𝟎
6 8 𝟏𝟐 8   6
[ 4 6   8   6   4 ]
• Highlighted pixels are edge pixels.
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
−1 0 1   −1 −1 −1
𝐺𝑥= [ −1 0 1 ] ,   𝐺𝑦= [ 0   0   0 ]
−1 0 1   1   1   1
Solutio
n
1 1   1 1 1   1 1 1   1 1
1 5   5 0 1   1 5 10 15 1
𝐼𝑥= 1 10 10 0 6 ,   𝐼𝑦= 1 5 10 15 6
1 15 15 0 6   1 0 0   0 6
[ 1 1   6 6 6]   [ 1 1 6   6   6]
(3 M)
1   1   1   1 1   𝐼𝑦2
1 25   25 0 1
𝐼𝑥2 = 1 100 100 0 6   1 1   1   1   1
1 225 225 0 6   1 25 100 225 1
[ 1   1   6   6 6] = 1 25 100 225 6
1 0   0   0   6
[ 1 1   6   6   6]
1 1   1   1 1
1 25 50 0 1
𝐼𝑥. 𝐼𝑦= 1 50 100 0 6
1 0   0   0 6
[ 1 1   6   6 6]
(2M)
********** 5 **********
--- page 6 ---
𝐼𝑥 2   𝐼𝑥𝐼𝑦   [700 225
𝐻= ∑𝑤(𝑥, 𝑦) [   2 ] =   700]
𝐼𝑥𝐼𝑦   𝐼𝑦   225
𝑥,𝑦
𝑅= 𝑑𝑒𝑡(𝐻) −𝑘. {𝑡𝑟𝑎𝑐𝑒(𝐻)}2
𝑅= {(700 × 700) −(225 × 225)} −0.04 × {700 + 700}2
𝑅= 360975 (2M)
R> 100000, it is a corner point, (2M)
If threshold is changed to 1000000, point will be a flat
point.
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
Solutio   Integral Image
n   1   2   3   4   5
2   4   6   8   10
3   6   10   14   18
4   8   14   20   26
5   10   18   26   34
(2M)
𝐿𝑥𝑥= −2(14 −3 −8 + 2) + (8 −2) + (26 −5 −14 + 3)
= 6
𝐿𝑦𝑦= −2(14 −8 −3 + 2) + (8 −2) + (26 −14 −5 + 3)
= 6
********** 6 **********
--- page 7 ---
𝐿𝑥𝑦= (4 −2 −2 + 1) + (20 −14 −14 + 10)
−(8 −4 −6 + 3) −(8 −6 −4 + 3) = 1
(4M)
[𝐿𝑥𝑥(𝑝, 𝜎) 𝐿𝑥𝑦(𝑝, 𝜎)   [6 1
𝐻(𝑝, 𝜎) =   𝜎)] =   6]
𝐿𝑥𝑦(𝑝, 𝜎) 𝐿𝑦𝑦(𝑝,   1
2
𝐷𝑒𝑡(𝐻) = 𝐿𝑥𝑥. 𝐿𝑦𝑦−(𝑊. 𝐿𝑥𝑦) = 36 −(0.9 × 1)2 = 35.19
(3M)
𝐷𝑒𝑡(𝐻) (>10) indicates that the highlighted point is a key
point. (1M)
Q4   a For Scale-Invariant Feature Transform (SIFT),   [10]
CO-2;   i) List and explain the steps to determine the SIFT
SO-5;
descriptor in brief. Write the role of each step.
BL-3,4
ii) Illustrate key point orientation assignment in details.
Solutio   Steps
n   1. Construct a Scale Space:
• Generate images over multiple scales
• Ensures that features are scale-independent
2. Key point Localisation:
• Select key points based on measure of stability
• Ignore other key points to avoid false keypoints
3. Orientation Assignment:
• Compute best orientations for each key point region
• To ensure that keypoints are rotation invariant
4. Keypoint Descriptor:
• Use local image gradients at selected scale and
rotation
(5M)
Orientation Assignment
• Each keypoint is identified by
•   location in image
•   Scale at which key point was selected
• Use a 16x16 pixels (window) around each key point
in the original image
• Window is divided into 16 cells of 4x4 pixels
********** 7 **********
--- page 8 ---
• Determine gradients of each pixel in X and Y
direction
• Determine magnitudes and orientations of gradients
for each pixel of each cell
• Divide orientation (0 to 360o) into 8 bins
• Draw Histogram on circular scale
(5M)
Q4   b   For Fast Library for Approximate Nearest Neighbors
CO-3;
(FLANN),
SO-1;
BL-3,5   (i) Construct a K-D tree for the following 3-dimensional
descriptors of Image 1.
Descriptors: (3, 1, 4), (3, 2, 5), (2, 3, 7), (2, 1, 3), (2, 4,
5), (1, 4, 4), (1, 2, 1), (0, 5, 7), (4, 3, 4), (6, 1, 4), (5, 2,
5), (5, 3, 6), (4, 0, 6), (4, 1, 2), (7, 1, 6), (7, 0, 5).
(ii) Choose a match for the descriptor (7, 1, 7) of Image 2
Solutio   Level 0 (root): split by x,
n
Level 1: split by y,
********** 8 **********

[Text in pictures on this page, read by OCR]
— +

7 ‘

The orientations all
ended up in two bins:
11 in one bin, 5 in the
other. (rough count)

511000000

Orientations in each of
the 16 pixels of the cell
--- page 9 ---
Level 2: split by z,
… then repeat.
Split into two groups: Root = (4, 3, 4)
Left subtree (x < 4): (0,5,7), (1,4,4), (1,2,1), (2,3,7), (2,1,3),
(2,4,5), (3,1,4), (3,2,5)
Right subtree (x >= 4): (4,0,6), (4,1,2), (5,2,5), (5,3,6),
(6,1,4), (7,1,6), (7,0,5)
(2M)
Build left subtree (split by y), Node: (2,3,7)
Left-left (y < 3): (3,1,4), (2,1,3), (1,2,1), (3,2,5)
Left-right (y > =3): (2,4,5), (1,4,4), (0,5,7)
Build right subtree (split by y), node = (6,1,4)
Right-left (y < 1): (4,0,6), (7,0,5)
Right-right (y > =1): (4,1,2), (5,2,5), (5,3,6), (7,1,6)
(2M)
Level 2 (split by z)
Left-left group (y < 3): node = (3,1,4)
Left (z < 4): (1,2,1), (2,1,3)
Right (z > =4): (3,2,5)
Left-right group (y > 3): node = (2,4,5)
Left (z < 5): (1,4,4)
Right (z >= 5): (0,5,7)
(2M)
Right-left group (y < 1): node = (4,0,6)
Left (z < 6): (7,0,5)
Right (z > =6): none
Right-right group (y > 1): node = (5,2,5)
Left (z < 5): (4,1,2)
Right (z > =5): (5,3,6), (7,1,6)
(2M)
Query descriptor (Image 2): (7, 1, 7)
Nearest match (Image 1): (7, 1, 6)
Euclidean distance: 1.00
(2M)
********** 9 **********
--- page 10 ---
Q5   a Describe steps for descriptor matching using Bag of Visual   [10]
CO-3;
Words. Explain it with example images.
SO-1;
BL-5   Explain why Bag of Visual words method is preferred over
pair wise feature matching?
Solutio
n
•   Pairwise descriptor matching is computationally
expensive.
•   Instead of comparing pairwise descriptors, group
descriptors with similar values to form clusters
• Use K-means clustering to generate ‘K’ clusters
• Each cluster has a centroid
•   Centroid represents all the descriptors within the
cluster
•   Centroid or cluster center is visual word the cluster
• Computational complexity is because, K centroids
are compared not N descriptors
(3M)
First image
1. Extract descriptors of first image
• Choose strong key points
• Determine corresponding descriptors
2. Apply K-means clustering on descriptors
• Groups similar descriptors
• Generate K groups or clusters
• Determine Cluster mean, also called cluster centres
•   Set of K clusters is a visual vocabulary
• Length of each cluster center is length of feature
descriptor
• For SIFT, it is 128
Second image
1. Extract feature of key points of second image
2. For each key point, find the nearest cluster from K
clusters of first image
3. Assign the nearest cluster of first image to descriptor
of the second image
********** 10 **********
--- page 11 ---
4. There can be several descriptors of second image
which are assigned a particular cluster of first image
5. Generate Histogram of K visual words for the image
Match histograms of two images.
(7M) for description and at least one example image
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
Solutio   (i) Limitations of K-means
n   • Need to choose the value of K
• Converges to a local minimum of WCSS
•   Sensitive to initialization of centroid
•   It is sensitive to rescaling
•   Sensitive to outliers
• Segments “spherical” clusters, does not work if
clusters have a complex geometric shape
Limitations of Mean Shift Algorithm
• Clustering depends on the choice of window size
(bandwidth) which can lead to under or over
segmentation
• Computationally more expensive than K-means
• Slow, especially for high-resolution images
• Can identify noisy pixel as clusters
• Finds arbitrary number of clusters
(4 M)
(ii) Distance of points to C1 = [255,0,0]
P1: 0
P2: 130050
P3: 130050
P4: 225
Distance of points to C2 = [0,0,255]
P1: 130050
P2: 130050
P3: 0
P4: 122625
Choose nearest centroid
• P1 → assign C1
• P2 → tie; but both equal → assign C2
********** 11 **********
--- page 12 ---
• P3→ assign C2
• P4 → assign C1
•   Cluster 1 members: P1, P4
•   Cluster 2 members: P2, P3
Updated centroids-
Cluster 1: P1=(255,0,0),  P4=(250,10,10)
• RC1=(255+250)/2=252.5
• GC1=(0+10)/2=5.0
• BC1=(0+10)/2=5.0
Update centroid, C1= (252.5,  5.0,  5.0)
Cluster 2: P2=(0,255,0),  P3=(0,0,255)P2=(0,255,0),
• RC2=(0+0)/2=0
• GC2=127.5
• BC2=127.5
Update centroid, C2= (0,127.5,127.5)
(6M)
Q 6   a   Using the Lucas–Kanade optical flow method,   10
CO-5;   (i) Derive the mathematical relationship used to determine
SO-4;   the velocity vector of a moving object in an image
BL-3   sequence.
(ii) State and explain the assumptions made in this
derivation.   discuss why these assumptions are
necessary, and how they can be addressed or relaxed
when they are not satisfied.
Solutio   • If a point, x in the image at time t moves to other
n   location at time (t+dt), its intensity does not change
• Therefore dt is assumed to be small
I(x+dx, y+dy, t+dt) = I(x,y,t)
• Taylor series expansion
I(x+dx, y+dy, t+dt) = I(x,y,t) + (dI/dx)δx +(dI/dy)δy +
(dI/dt)δt +[(d2I/dx2)δx +(d2I/dy2)δy + (d2I/dt2)δt]/2 + ...
Where, dI/dx, dI/dy and dI/dt are image gradients along
horizontal axis, vertical axis and time
•   If higher order derivatives are neglected,
(dI/dx)δx + (dI/dy)δy + (dI/dt)δt = 0
(dI/dx)δx/δt + (dI/dy)δy/δt + (dI/dt)δt/δt = 0
(dI/dx)Vx + (dI/dy)Vy + (dI/dt) = 0,
Where, Vx = δx/δt and Vy = δy/δt
• Determine Vx and Vy to find movement over time
(dI/dx)Vx + (dI/dy)Vy + (dI/dt) = 0
• Use interest points in the optical flow function
•   Select a set of interest points in a frame of video
********** 12 **********
--- page 13 ---
• Determine the locations of same interest points in the
next frame
• Determine velocity vector
• Use velocity vector to track the motion of interest
points between two frames
• Method work best with slow-moving objects
• Assume that 2 consecutive frames are separated by a
small time increment (dt) such that objects are not
displaced significantly
(dI/dx)Vx + (dI/dy)Vy + (dI/dt) = 0
Or
Ix (q)Vx + Iy (q)Vy = - It (q)
Where,
•   Ix and Iy are pixel intensity gradients along x and y
direction at interest point, q
• Vx and Vy are velocities along x and y direction
•   It is change in pixel intensity of q between two
consecutive frames
• Use 3x3 window around the interest point, q
• Assume that all nine points have the same motion
between two consecutive frames
• Where q1,q2,…,qn denote pixels inside the window
(ex: n = 9)
•   All pixels satisfy optical equation
Av=b
[Vx , Vy]T = (ATA)-1(AT)(-b)
********** 13 **********
--- page 14 ---
• Determine velocity vector for every pixel in the
image to estimate the optical flow
• Few pixels (e.g., feature points like corners or edges)
are tracked to reduce computational cost
• Method to find Vx and Vy   is valid for small
displacements (low velocity)
• For large displacements (more then 2 pixels) the
method cannot be used
• Because second order derivative of Taylor Series
expansion dominates
•   Therefore construct image pyramid such that large
velocities reduce   to   small   displacements   in
subsampled images
(6M) for description
(2M) for assumptions
(2M) for solution
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
i) Draw architecture and show the shape of output after
each layer. Do not consider bias terms at any layer.
ii) Specify activation functions for the layers
********** 14 **********
--- page 15 ---
Solutio   Layer   Description   Parameters /   Activati Outp
n   Details   on   ut
Functio Shape
n
Input   Input image   Size = 32×32×3 —   (32,
32, 3)
Conv2D   Convolution Filter size = 3×3, ReLU   (30,
with 32   stride = 1, no   30,
filters of   padding → output   32)
size 3×3   size =
(32−3+1)×(32−3+
1) = 30×30
MaxPooling   Pooling   Pool size = (2×2), —   (15,
2D   layer   stride = 2 →   15,
output size = 30/2   32)
= 15
Dropout   Regularizati Dropout rate = 0.2 —   (15,
on   15,
32)
Flatten   Converts   15×15×32 = 7200 —   (7200,
3D tensor to   )
1D vector
Dense (Fully Fully   Units = 128   ReLU   (128,)
Connected   connected   (assumed
1)   layer   reasonable for
intermediate
layer)
Dense (Fully Output   Units = 10 (for   Softmax   (10,)
Connected   layer   example, 10
2)   classes)
(4M) Architecture
(6M) shape at each layer
Q 7   a   For Region based Convolutional Network (RCNN),
CO-5;   i) Draw architecture and write the role of each step
SO-4;   ii) Explain selective search algorithm in details
BL-3
********** 15 **********
--- page 16 ---
Solutio
n
(5M)
ii) Selective search algorithm
• Generate 2,000 region proposals using the Selective
Search algorithm. Input each region proposal into CNN
• Extract a feature vector of length, 4096 from each region
proposal from CNN
• Use a pre-trained SVM algorithm to classify the region
proposal to either the background or one of the object
classes. Refine bounding box predictions using
bounding box regression
• Segment the image into regions. Regions have similarity
in color, texture or any other parameter
• Use graph segmentation to capture the regions. Merge
regions into larger regions iteratively. Merged regions
are called region proposals
• Assume that the image is a graph of vertices (nodes)
• Edges connect the nodes. Assign weight to each edge.
Weight is dependent on the distance between the nodes
• Distance can be color difference, texture difference or
any
• Nodes having low distance have low weight
• Connect nodes with low weight using edges
• Merge edges with weight less than a threshold
********** 16 **********

[Text in pictures on this page, read by OCR]
Input Image

Selective Search
2000 region Proposals

Warp and resize to
224x224

CNN (Ex: Alexnet)

Feature Vector

SS

SVM Classifier BB regressor

Predict Class Refined Box
--- page 17 ---
• Merged edges are called components. Nodes which are
not merged are the ones which have large distance
Q 7   b   For Single Shot Detector, justify the use of multiple boxes
CO-5;   to detect object of different scale. Explain with suitable
SO-4;   diagrams.
BL-3
Solutio   The SSD is based on the use of convolutional networks
n   that produce multiple bounding boxes of various fixed
sizes and scores the presence of the object class instance
in those boxes, followed by a non-maximum suppression
step to produce the final detections.
Each input image is divided into grids of various sizes
and at each grid, the detection is performed for different
classes and different aspect ratios.
A score is assigned to each of these grids that indicates
how well an object matches in that grid.
Non maximum supression is applied to get the final
detection from the set of overlapping detections.
It uses different grid sizes to detect objects of different
sizes.
The multi-scale feature maps are added to the end of the
truncated backbone model.
These multi-scale feature maps reduce in size progressively,
which allows the detections at various scales of the image.
The convolutional layers vary for each feature layer.
The addition of each extra layer produces a fixed number of
predictions using the convolutional filters in them.
For example, a feature layer of size m x n with p channels,
the minimal prediction parameter that gives a decent
detection is a 3 x 3 x p small kernel. Such kernel gives us the
score for a category, or a shape offset relative to the default
box coordinates.
********** 17 **********
````

## 2025-26 · Final-Exam · Sem 7 · Answer key · paper 77086fd15208

- Departments: Data Science
- Programmes: BTech CSE DS 7011, BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_07/Final-Exam/BTech_CSE_DS_7011/COMPUTER VISION/ANS_COMPUTER VISION(702EX0E015)_2025-2026.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Nov 2025
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)
Year: IV/Semester VII(Exam Year: 2025-2026)
Subject: COMPUTER VISION
Date: 29 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
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
i) Mid level: use feature descriptors like SIFT/ SURF etc and match
the features with the labels on product
Solution   ii)   High-level: Train CNN model for product labels or apply
segmentation using RCNN etc
2 Marks each for correct techniques and justification
b. For Scale-Invariant Feature Transform (SIFT) algorithm, a point has
Ixx=6, Iyy = 4, Ixy = 1, where, Ixx and Iyy are second order derivatives in
x and y directions respectively and Ixy is first order derivative in x
CO-2
direction of derivative in y direction.   [04]
SO-1
BL-3,6
Construct Hessian matrix and test whether the given the given point is
a keypoint or not. For SIFT, r = 10
𝐻 = [Ixx   Ixy] = [6   1]
Ixy Iyy   1 4
Solution   Determinant = 6x4 – 1 =23
Trace = 6+4 =10
********** 1 **********
--- page 2 ---
𝑡𝑟𝑎𝑐𝑒2(𝐻)   (𝑟 + 1)2
<
𝑑𝑒𝑡𝑒𝑟𝑚𝑖𝑛𝑎𝑛𝑡(𝐻)   𝑟
Trace2/Determinant < 12.1
Trace2/Determinant = 100/23 = 4.35
Since 4.35< 12.1, the given point is key point
2 Marks for H matrix, trace and determinant
2 Marks for test for key point
c. How does FLANN use KD-Trees to accelerate nearest neighbor
CO-2   searches in high-dimensional feature matching?
SO-1   Construct a KD-Tree for the following 2D points (split alternately on   [04]
BL-3   x and y):
𝑃1 = (3,6), 𝑃2 = (17,15), 𝑃3 = (13,15), 𝑃4 = (6,12), 𝑃5 = (9,1)
 FLANN builds a set of KD-Trees to partition the feature space.
 During search, it traverses the KD-Tree(s) instead of comparing
with all database descriptors → faster retrieval.
(9, 1) <-- Root (x split)
/   \
Solution
(6,12)   (13,15)
/   \   /   \
(3,6)   -   -   (17,15)
Location of (3,6) and (6,12) can be exchanged
Location of (13,15) and (17,15) can be exchanged
2 Marks: advantage of FLANN
2 Marks: KD tree
d.   i) Write purpose of the Fully Connected (FC) layer in a Convolutional
CO-2
SO-5   Neural Network (CNN)?   [04]
ii) Explain with the help of a simple diagram showing how the feature
BL-3
map is flattened and connected to the output neurons.
 The FC layer combines the features learned by convolution and
pooling layers to perform final classification or prediction.
   It converts the 2D/3D feature maps into a 1D vector and
connects every input value to every output neuron.
Solution
 Each connection learns a weight, helping the network associate
feature patterns with specific output classes.
2 Marks: Justification
2 Marks: Diagram
CO- 4   e.   List and justify any two limitations of Region based Convolutional
SO- 5   [04]
Neural Network.
BL- 5
********** 2 **********
--- page 3 ---
1. Selective Search algorithm for generating region proposals, takes a
lot of time
2. Each region proposal requires multiple stages
• Region   proposal   generation,   feature   extraction,   and
Solution
classification using SVM
• Ex: 100 images each with 2000 region proposals requires
200,000 sets of steps
•   It is impossible to implement in real time
3. Extracted features from the pre-trained CNN are saved to train the
SVMs
• Requires hundreds of gigabytes of storage
4. Require ‘N’ SVMs for ‘N’ classes, which is huge
4 Marks: 2 Marks each for a limitation with justification
a   For SIFT (Scale-Invariant Feature Transform) algorithm,
Q2   i) Briefly describe the role of each step in 2-3 sentences.
CO-3   ii) Explain scale space generation in details using an example image
SO-2   [10]
BL-3   of size M×N. Assume initial value of standard deviation =1.6.
Sketch images and standard deviations at each stage.
********** 3 **********
--- page 4 ---
1. Construct a Scale Space:
• Generate images over multiple scales
• To ensures that features are scale-independent
2. Key point Localisation:
• Select key points based on measure of stability
• Ignore other key points to avoid false keypoints
3. Orientation Assignment:
• Compute best orientations for each key point region
• To ensure that keypoints are rotation invariant
4. Keypoint Descriptor:
• Use local image gradients at selected scale and rotation
Solution
Scale space Generation:
•   Scale space is a collection of images having different resolutions
and blurring generated from a single image
•   Ideal number of low resolution versions (octaves) is four
• Octave is different levels of image resolutions
• Each octave is down sampled by 2 to generate next octave to
reduce image size by 1/4
• Each octave has five blurred images, std1= 1.6, std2=1.6 k,
std3=1.6k2, std4= 1.6k3, k = 21/2
•   Gaussian filter of different scales (variance) blur the images
********** 4 **********
--- page 5 ---
Determine Difference of Gaussian (DoG) of two consecutive blurred
images in each octave
4 Marks for the list of key steps
4 Marks for the description
2 Marks for image
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
•   9-bin Histogram
(40x   (50x   (10x   60x4 0   0   0   0   0
4)+(   4)+(   4)+(   =240
50x4   10x4   20x4
Solution
)=   )=24   )=12
360   0   0
0   20   40   60   80   100   120   140   160
4 Marks: Histogram
********** 5 **********
--- page 6 ---
•
• Each block contains 4 cells ( 1 histogram/ cell)
• Each block has 4 histograms (9 values/ histogram)
•   Concatenate 4 histograms to form a 36 x 1 element vector for a
block
• Normalize the vector
• 𝑎 =   𝑎1
𝑛1   √𝑎12+𝑎22+⋯+𝑎362
Where values of a represent elements of histogram
• Normalized vector, an has 36 element /block
• 16×16 block is moved in steps of 8 pixels ( i.e. 50% overlap with
the previous block )
• 16×16 block is moved in steps of 8 ( i.e. 50% overlap with the
previous block )
• Number of blocks = 7 x 15 = 105
•   For each block, there are 36 values
• Length of the final vector 105 x 36 = 3780
6 Marks: for determining length of descriptor
********** 6 **********
--- page 7 ---
a   Consider the following 9×9 integral image.
i)   Filter the image at the center with the given 9×9 filter. Use
integral image.
ii) How many additions, subtractions and multiplications are used
for this computation?
iii) Compare SIFT and SURF descriptors
0   0   0   0   0   1   2   3   4
0   0   0   0   0   2   4   6   8
0   0   0   0   0   3   6   9   12
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
Q3   0   0   0   0   0   4   8   12   16
CO-2   0   0   0   0   0   4   8   12   16   [10]
SO-4   0   0   0   0   0   4   8   12   16
BL-4, 5   Integral image
Filter
i) Integral image
0   0   0   0   0   1   2   3   4
0   0   0   0   0   2   4   6   8
0   0   0   0   0   3   6   9   12
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
Output = -2(4-2-0+0) + (16-8-4+2) = -4+6=2
For each filter 3 additions and subtractions. One filter requires
multiplication. Final output requires 2 additions/subtractions
********** 7 **********
--- page 8 ---
SIFT
• High dimensionality
• Leads to good accuracy
• Approximates Laplacian of Gaussian with DoG
• Uses determinant and trace of Hessian matrix
SURF
•   It is a speeded-up version of SIFT (Fast and robust algorithm)
• Approximates LoG with Box Filter
•   Convolution with box filter using integral images speeds up the
process
•   Convolution can be done in parallel for different scales
• Thus enabling real-time applications such as tracking and
object recognition
• Uses determinant of Hessian matrix for both scale and location
not trace
4 marks: Output
2 marks: number of computations
4 marks: Comparison
Q3   b   Describe Binary Robust Independent Elementary Features (BRIEF)
CO- 2   descriptor in details. Use examples to explain GII and GIII approaches   [10]
SO- 4
BL- 3   to choose pair of pixels.
• Each key point is described by a feature vector which is 128–
512 bits string
•   It is noise sensitive therefore uses Gaussian filter to smoothen
the image
• Use Gaussian kernel with variance in the range 0 - 3 (Usually,
2)
•   Steps
Solution
• Choose two pixels at two locations, x and y
{1, 𝑝(𝑥) < 𝑝(𝑦)
𝜋(𝑝; 𝑥, 𝑦) =
0, 𝑝(𝑥) ≥𝑝(𝑦)
Where, p(x) is intensity value at x and p(y) is intensity value at y
Choose ‘n’ pairs of ‘x’ and ‘y’ locations, where, n = 128, 256 or 512
Binary descriptor is ‘n’ values of π(p;x,y)
Descriptor is ‘n’ number of ones and zeroes
********** 8 **********
--- page 9 ---
Feature descriptors two interest points are matched using Hamming
distance
• Gaussian(G II):
• Both x and y pixels are drawn from a Gaussian distribution
with standard deviation of 0.04×S² around key point
• Gaussian(G III):
• The first pixel(x) is drawn from a Gaussian distribution
centered around the key point with a standard deviation
of 0.04×S²
• The second pixel(y) is drawn from a Gaussian distribution
centered around the first pixel(x) with a standard deviation
of 0.01×S².
• The pair of pixels is more local
4 marks: BRIEF descriptor
6 marks: 3 marks each for GII and GIII approaches
Q4   a An image retrieval system for a fashion e-commerce website is to be
CO-2   developed. Each image is represented by a feature vector extracted   [10]
SO-4   using SIFT.
********** 9 **********
--- page 10 ---
BL-3   (i) Explain how cosine similarity is used to compare two image feature
vectors. Explain with examples.
(ii) Feature vectors extracted from images:
𝐹1 = [1,2,3], 𝐹2 = [2,1,3], 𝐹3 = [0,1,1]
Feature vector to be matched is Q = [1,1,2]. Compute the cosine
similarity between Q and each feature vector to identify the best
match.
 Cosine Similarity: Measures the angle between two vectors,
independent of their magnitude. Values range from −1 to 1.
 Advantage over Euclidean: Magnitude differences do not
dominate; only direction of features matters, which is useful
for high-dimensional descriptors.
   Applications:
o Image retrieval / nearest neighbor search
o Face recognition (feature embedding comparison)
o Document/image clustering
Step 1 – Compute norms:
∣∣ 𝑄 ∣∣= √12 + 12 + 22 = √1 + 1 + 4 = √6 ≈ 2.449
∣∣ 𝐹1 ∣∣= √12 + 22 + 32 = √1 + 4 + 9 = √14 ≈ 3.742
Solution   ∣∣ 𝐹2 ∣∣= √22 + 12 + 32 = √4 + 1 + 9 = √14 ≈ 3.742
∣∣ 𝐹3 ∣∣= √02 + 12 + 12 = √0 + 1 + 1 = √2 ≈ 1.414
Step 2 – Compute dot products:
𝑄 ⋅ 𝐹1 = 1 ∗ 1 + 1 ∗ 2 + 2 ∗ 3 = 1 + 2 + 6 = 9
𝑄 ⋅ 𝐹2 = 1 ∗ 2 + 1 ∗ 1 + 2 ∗ 3 = 2 + 1 + 6 = 9
𝑄 ⋅ 𝐹3 = 1 ∗ 0 + 1 ∗ 1 + 2 ∗ 1 = 0 + 1 + 2 = 3
Step 3 – Compute cosine similarities:
cos(𝑄, 𝐹1) = 9/(2.449 ∗ 3.742) ≈ 9/9.164 ≈ 0.982
cos(𝑄, 𝐹2) = 9/(2.449 ∗ 3.742) ≈ 0.982
cos(𝑄, 𝐹3) = 3/(2.449 ∗ 1.414) ≈ 3/3.464 ≈ 0.866
Most similar feature vectors: F₁ and F₂ (cos ≈ 0.982)
4 Marks: cosine similarity
6 Marks: calculation
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
********** 10 **********
--- page 11 ---
Steps for Image matching using Bag of Words
1. Extract feature of key points of second image
2. For each key point, find the nearest cluster from K clusters
of first image
3. Assign the nearest cluster of first image to descriptor of the
second image
4. There can be several descriptors of second image which are
assigned a particular cluster of first image
5. Generate Histogram of K visual words for the image
Document frequency (DF)
Count of images (of the 6) where each word appears at least once:
 DF(W1) = 3 (A, C, E)
 DF(W2) = 4 (A, B, D, E)
Solution    DF(W3) = 3 (B, C, F)
 DF(W4) = 4 (A, B, D, F)
 DF(W5) = 3 (A, C, D)
IDF = log(N/ni)
 IDF(W1)=log10(6/3) =0.30103
 IDF(W2)= log10(6/4)=log10(1.5)=0.17609
 IDF(W3)= log10(6/3)=0.30103
 IDF(W4)= log10(6/4)=0.17609
 IDF(W5)= log10(6/3)=0.30103
Image A: TF_A = [2, 1, 0, 1, 1]
TF_A × IDF
= [2×0.30103, 1×0.17609, 0×0.30103, 1×0.17609, 1×0.30103]/5
TF_B × IDF
= [0×0.30103, 2 ×0.17609, 1 ×0.30103, 1×0.17609, 0×0.30103]/4
4 Marks: steps
6 marks: calculations
a   For a pedestrian tracking system for autonomous vehicles, the system
captures consecutive video frames.
(i)   Describe how the Lucas–Kanade method estimates optical flow
Q5
for a small window of pixels.
CO-2   (ii)   Write a real-world scenario where sparse optical flow is   [10]
SO- 4   preferred over dense optical flow.
BL- 3   (iii)   For a 2×2 window, the image derivatives are:
𝐼𝑥 = [3,1], 𝐼𝑦 = [1,2], 𝐼𝑡 = [−2, −1]
Calculate optical flow vectors for the window.
Assumes brightness constancy: a pixel’s intensity stays
constant between frames, so 𝐼(𝑥 + 𝑢, 𝑦 + 𝑣, 𝑡 + 1) ≈ 𝐼(𝑥, 𝑦, 𝑡).
 For small motion, linearize to get the optical flow constraint:
𝐼𝑥𝑢 + 𝐼𝑦𝑣 + 𝐼𝑡 = 0.
Solution    Lucas–Kanade assumes constant (u,v) inside a small window
and builds an overdetermined linear system from all pixels in
that window:
𝐴 = [𝐼𝑥   𝐼𝑦], 𝑏 = 𝐼𝑡
Solve in least-squares sense:
********** 11 **********
--- page 12 ---
(𝐴𝑇𝐴) [𝑢 𝑣] = −𝐴𝑇𝑏
   This uses image gradients 𝐼𝑥, 𝐼𝑦and temporal derivative 𝐼𝑡; it is
robust to noise by aggregating information over the window.
Given
𝐼𝑥 = [3, 1], 𝐼𝑦 = [1, 2], 𝐼𝑡 = [−2, − 1].
Form 𝐴and 𝑏:
Form 𝐴and 𝑏:
𝐴= [3 1 2], 𝑏= [−2 −1].
1
Compute
𝐴𝑇𝐴= [10 5 −𝐴𝑇𝑏= [7
5   5],   4].
Solve
[10 5 5][𝑢 𝑣] = [7 4].
5
From second row: 5𝑢 + 5𝑣 = 4 ⇒ 𝑢 + 𝑣 = 0.8. Substitute into first
row:
10(0.8 − 𝑣) + 5𝑣 = 7 ⇒ −5𝑣 = −1 ⇒ 𝑣 = 0.2.
Hence 𝑢 = 0.8 − 0.2 = 0.6.
(𝑢, 𝑣) = (0.6, 0.2)— motion to the right and slightly down.
5 Marks: description
5 Marks: computation
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
********** 12 **********
--- page 13 ---
Compute Euclidean distance to centroids
   Pixels with RGB ~10–15 → close to C1→ Cluster 1
Solution      Pixels with RGB ~198–201 → close to C2 → Cluster 2
After 1st iteration:
 Cluster 1: (10, 20, 30), (12,18, 28), (11, 21, 29), (15, 22, 32),
(14, 19, 31), (13, 31, 30)
 Cluster 2: (200, 210, 220), (198, 208, 218), (201, 212, 221)
C1new=
 Sum R: 10+12+11+15+14+13 = 75 → 75/6 = 12.5
 Sum G: 20+18+21+22+19+21 = 121 → 121/6 ≈ 20.17 ≈ 20
 Sum B: 30+28+29+32+31+30 = 180 → 180/6 = 30
C1new=(12.5,20,30)
C1new=
 Sum R: 200+198+201 = 599 → 599/3 ≈ 199.67 ≈ 200
 Sum G: 210+208+212 = 630 → 630/3 = 210
 Sum B: 220+218+221 = 659 → 659/3 ≈ 219.67 ≈ 220
C2new=(200,210,220)
(10, 20, 30)   (12,18, 28)   (200, 210, 220)
(11, 21, 29)   (15, 22, 32)   (198, 208, 218)
(14, 19, 31)   (13, 31, 30)   (201, 212, 221)
6 Marks: centroids
2 Marks: clustering
2 Marks: comments
a   In relation to 3D model, write in brief about
Q6
(i)   camera model
CO-3   [10]
SO-1   (ii)   Intrinsic matrix
BL-3
(iii)   Extrinsic matrix
********** 13 **********
--- page 14 ---
Given
•   Location and orientation of a camera with respect to axes of
world point
• And property of the camera like focal length and resolution
•   Find where a point in the world (called the world point)
appears on the image plane
Solution   • Camera model
********** 14 **********
--- page 15 ---
• And (iii) Determination of extrinsic and intrinsic matrix is
called camera calibration.
Extract 3-D information from 2-D photographs using extrinsic
and intrinsic matrices.
• Used to map 3D world scene into 2D image plane
•   Extrinsic parameters represent the camera’s position in the 3-D
scene
•   Intrinsic characteristics represent the camera’s optical center
and focal length
•   Coordinates of world points are transformed to camera
coordinates using the extrinsic parameters
•   Intrinsic parameters are used to map the camera coordinates
into the image plane
•   Intrinsic or Internal Parameters
• Depend on how camera captures the images
• Map image plane coordinates to image coordinates in terms
of row and column numbers
• Uses optical center, focal length and skew coefficient
********** 15 **********
--- page 16 ---
• Extrinsic or External Parameters
• Depends on orientation and location of the camera
•   Requires rotation and translation of the camera with respect
to world coordinate system (3D coordinates)
• Do not consider internal parameters (focal length, the field
of view, etc.)
4 Marks: Camera model
3 Marks: Extrinsic
3 Marks: Intrinsic
Q6   b
In relation to stereo vision, explain Epipolar constraints to determine
CO-3   [10]
SO-2   essential matrix.
BL-3
Epipolar Constraint
•   corresponding point of x in left image lies on the epipolar line,
l’ in right image
•   corresponding point for x’ in right image lies on the epipolar
line, l in left image
Solution
********** 16 **********
--- page 17 ---
•   Point x’ lie on line, l’
•   x’Tl’ = 0
•   Also, Ex=l’
•   Therefore, x’TEx = 0
•   Similarly, ETx’ = l
• And Ee=0
5 Marks: Image of epipolar geometry and description
5 marks: relations for essential matrix
Q7   a
Draw architecture of Fast RCNN and explain each layer/block in 2-3
CO-4   [10]
SO-5   sentences in brief.
BL-4
********** 17 **********

[Text in pictures on this page, read by OCR]
line in the second image using E matrix

Ex = I

Conditions:

1. Vectors, x, t, x’ are coplanar, therefore, | and I’ lie on this plane
2. Camera at O’ is rotated and translated version of O

3 There is no other transformation for O
--- page 18 ---
Solution
•   Selective search determines region proposals
• Each region proposal is not passed to CNN
•   Entire image is fed to CNN which saves time
• Uses feature map which is a tensor
•   Feature maps are higher dimensional features of image
•   Parts of feature map corresponds to a region proposals
•   Instead of SVM, softmax classifier is used
• Ground truth for Softmax is known, [0,0,1,0,…]
• Match coordinates of region proposal with feature map
• Matched part is called ROI of feature map
• ROI pooling layer converts varying sizes of features to fixed
sizes of features
5 Marks: architecture, 5 Marks: description
b   In relation to RCNN, justify that
Q7
i) RCNN is slow
CO-4   [10]
SO- 5   ii) Fast RCNN is faster than RCNN
BL-6
iii) Faster RCNN is faster than Fast RCNN
i) RCNN is slow
Solution      Selective Search algorithm for generating region proposals,
takes a lot of time
********** 18 **********

[Text in pictures on this page, read by OCR]
Fast RONN

Input Image

———

CNN (Ex: VGG16)
) Selective Search

A

Feature Map 2000 region Proposals
ROI Pooling
3
Feature Vector
Z
Softmax Classifier BB regressor
AN I

Predicted Class Refined Box
--- page 19 ---
 Each region proposal requires multiple stages
 Region proposal generation, feature extraction, and
classification using SVM
 Ex: 100 images each with 2000 region proposals requires
200,000 sets of steps
   It is impossible to implement in real time
 Extracted features from the pre-trained CNN are saved to train
the SVMs
 Requires hundreds of gigabytes of storage
 Require ‘N’ SVMs for ‘N’ classes, which is huge
ii) Fast RCNN is faster than RCNN
   Fast R-CNN uses ROIs for identification of region
proposals
 ROI Pooling layer makes Fast R-CNN faster than R-CNN
 Does not save extracted features
 Therefore, does not need large memory compared to R-
CNN
iii) Faster RCNN is faster than Fast RCNN
   Faster RCNN uses Region Proposal Network (RPN) instead of
selective search method
 RPN generates regions which may contain objects
 RCNN and Fast RCNN have several stages in sequence
   Faster R-CNN builds a network that has only a single stage
 Stages are input CNN  RPN  Region Proposal 
RoI Pooling  FC layers  Classifier and BB regressor
3 Marks: slow RCNN, 3 Marks: Fast RCNN is faster
4 Marks: Faster RCNN is faster
********** 19 **********
````

## 2025-26 · Re-Exam · Sem 12 · Answer key · paper 10b79e3d8a03

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2024/Sem_12/Re-Exam/Integrated_Computer_7032/Computer Vision/ANS_Computer Vision(702AI0C017)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech Intg. (CE)
Year: III / VI/Semester VI/Semester XII(Exam Year: 2025-2026)
Subject: Computer Vision
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 11 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 4   a.   In relation to epipolar geometry, explain epipolar constraint. Show
SO- 1,6   [05]
BL- 2   how it useful in matching key points.
Solution
Description (3M)
Use of epipolar constraint (2M)
CO- 3   b.   Explain in brief any two advantages and two limitations of the K-
SO- 1,6   [05]
BL- 5   Means algorithm.
Advantages:
Solution
1. Simple and Easy to Implement
********** 1 **********

[Text in pictures on this page, read by OCR]
* For stereo images,
* Akey point in left image has corresponding point in a line in right image
* This is epipolar constraint
* Epipolar constraint reduces matching problem from 2D image search to 1D line search
* Therefore search for correspondences is quicker
* Corresponding point is searched on epipolar line

* Determine a epipolar line for matching each corresponding point

Epipolar line

Key point

Left image Right image
--- page 2 ---
2. Computationally Efficient
Initial random centroids → quickly move to stable
positions after few iterations.
Limitations:
1. Requires Predefined K
2. Sensitive to Initial Centroids
(2M) for points
(2M) for explanation
c.   Determine the integral image for the following image.
CO- 2
SO- 1,6   [05]
BL- 4
Integral image
Solution
(5M)
CO- 1   d.
SO- 1,6   Explain two examples of mid-level processing.   [05]
BL- 5
1. Use low level features for image matching
2. Keep track of moving objects in a video
3. Determine optical flow to predict speed and direction of
Solution   movement of object
4. Image Clustering
Any two examples (2M)
Explanation (3M)
Given the following gradient magnitude and orientation matrices,
compute the histogram of oriented gradients using 9 bins (0–180°).
What is the final HOG feature vector for the 4×4 image?
Which bin does a pixel with:
(a) 35° belong to?
Q2a   (b) 95° belong to?
CO- 1
SO- 1, 6   [10]
BL- 5
Gradient Magnitude   Gradient orientation (Ɵ)
Bin Range   Bin
Solution   (°)   Center
0–20   10
20–40   30
********** 2 **********
--- page 3 ---
40–60   50
60–80   70
80–100   90
100–120   110
120–140   130
140–160   150
160–180   170
(10°, M=2): +2, (20°, M=3): +3, (30°, M=1): +1, (40°, M=2):+2
(50°, 4): +4, (60°, 2): +2, (70°, 1): +1, (80°, 3): +3
(90°, 2): +2, (100°, 1): +1, (110°, 3): +3, (120°, 2): +2
(130°, 1): +1, (140°, 2): +2, (150°, 2): +2, (160°, 4): +4
HoG vector is [2, 4, 6, 3, 5, 4, 3, 4, 4]
Bin range (5M)
Determination of HoG vector (5M)
For Harris corner detector,
Q2b   i) Show with example images that Harris corner detector is
CO- 1   invariant to rotation and variant to scaling   [10]
SO- 1, 6   ii) Explain the steps involved in constructing Harris matrix and
BL- 5   using corner response to determine whether the pixel is corner,
edge or flat region.
i) Assume a window of size 3×3 centered at a location,
(x,y)
Harris matrix is
𝐼𝑥 2   𝐼𝑥𝐼𝑦
𝑀= ∑𝑤(𝑥, 𝑦) [   2 ]
𝐼𝑥𝐼𝑦   𝐼𝑦
𝑥,𝑦
Ix and Iy are derivatives in x and y directions in window
R = det{M} – k (trace {M})2
Det{M} = Ix2 Iy2 - Ixy2
Trace{M}=Ix2 +Iy2
Empirically determined value of k is 0.04 – 0.06
R is +ve and large for corner points
R is –ve and large magnitude for edge
Solution   |R| is small for flat region
ii)   Harris and Hessian detectors are rotation invariant
• Corner gets magnified and becomes bigger than the size of the
window by zooming. After scaling, corner points are classified
as edges
********** 3 **********
--- page 4 ---
Q3a
List the steps for extracting Scale-Invariant Feature Transform
CO- 2   (SIFT) features from an image, and describe keypoint localization in   [10]
SO- 1, 6
BL- 5   detail.
1. Construct a Scale Space:
• Generate images over multiple scales
• Ensures that features are scale-independent
2. Key point Localisation:
• Select key points based on measure of stability
• Ignore other key points to avoid false keypoints
3. Orientation Assignment:
• Compute best orientations for each key point region
• To ensure that keypoints are rotation invariant
4. Keypoint Descriptor:
• Use local image gradients at selected scale and rotation
(5M)
• Each pixel is compared with 26 other pixel values
•   Pixel marked x is compared with 26 other pixel values
•   If it is the highest positive or lowest negative among 26
neighbors (maxima or minima)
Solution   •   It is selected as a potential keypoint
•   Discard weak key points
• Normalize DoGs to get values in 0 -1 range
•   Set threshold to 0.03
• For DOG(x), x is coordinates of extrema (minima/maxima)
•   If DOG(x) < Threshold, discard it
•   Else retain it
•   Construct Hessian matrix at each potential keypoint to check
whether these points are good corner points not edge points
********** 4 **********
--- page 5 ---
Q3b
For Speeded-Up Robust Features (SURF), explain the scale space
CO- 2   generation for feature detection and justify in brief why it is   [10]
SO- 1, 6
BL- 1, 5   computationally efficient.
• For SURF, instead of reducing the size of image, filter size is
increased
• Computational complexity does not increase with the size of filter
• Because integral images and box filters are used
Solution
• Uses a number of octaves
• Each octave has a number of layers
For each octave and layer, image is filtered with second order
Gaussian Filter with higher and higher standard deviation
SURF achieves high speed due to:
• Use of integral images → fast computation
• Box filter approximation instead of Gaussian filters
• Scale-space via filter scaling, not image scaling
• Efficient Haar wavelet computations
Explain the Mean Shift clustering algorithm with reference to the
following aspects:
Q4a
i) The working procedure of the algorithm and criteria for
CO- 3   convergence   [10]
SO- 1, 6
ii) Effect of large and small bandwidth
BL- 2
iii) The advantages and limitations of Mean Shift
Support your explanation with a suitable example plots of data
points
Working of Mean Shift Algorithm
1. Choose a window (bandwidth) around a data point
2. Compute the mean of all points inside the window
3. Shift the window center to this mean
4. Repeat until the shift is very small
Solution   5. Points converging to the same location form a cluster
The algorithm stops when:
Shift in position is very small, or
The point reaches a stable mode (peak)
(4M)
********** 5 **********
--- page 6 ---
Bandwidth (window size) controls the radius of the neighborhood
• Large bandwidth → fewer clusters (smoother result)
• Small bandwidth → more clusters (detailed structure)
(2M)
Advantages
• No need to specify number of clusters
• Can detect arbitrarily shaped clusters
• Robust to noise
• Works well for density estimation
Limitations
•   Computationally expensive
•   Choice of bandwidth is critical
•   Not suitable for very high-dimensional data
• May merge nearby clusters if bandwidth is large
(4M)
Q4b
CO- 3   Describe how Gaussian Mixture model is used to generate   [10]
SO- 1,6   background model.
BL- 5
• Generate mixture of ‘k’ Gaussians distribution models for
each pixel of background frame
•   Values for ‘k’ is in the range 3 to 5
• Weight of each distribution is proportional to the amount of
time each color/intensity stays on that pixel
•   If a pixel has almost the same intensity for few consecutive
frames
• Weight of the Gaussian distribution of the pixel is more
• This pixel is a background pixel
Solution   •   If weight of Gaussian distribution of a pixel is low, that pixel
classified as a foreground pixel
Video frames   Background model
Q5a
Show the concept of optical flow. Compare dense and sparse optical
CO- 3   [10]
SO- 1,6   flow with suitable example images.
BL- 4
********** 6 **********
--- page 7 ---
•   If there is a relative motion between the camera and the
objects in the scene
•   Points of objects move in consecutive frames of video
•   Velocity vectors for these points in consecutive frames
is optic flow
•   It describes movement of objects
•   Optical flow is used for a series of frames of a video that
have a small time step between them
•   Calculates velocity of points between consecutive frames
• And provides an estimation of location of points in the next
image sequence
Solution
(4M)
Sparse optical flow
•   Is flow vectors of interest points of frames
•   Interest points could be edges or corners of object in a frame
Dense optical flow
•   Provides flow vectors of all pixels
• Has one flow vector per pixel
• Has higher accuracy
•   Is slow and computationally expensive
(4M)
(2M) for images
Q5b
Describe how background frame is generated using temporal average.
CO- 3   Also show how background subtraction is used generate foreground   [10]
SO- 1,6
BL- 5   of the image.
Solution
********** 7 **********

[Text in pictures on this page, read by OCR]
Compute running average over the previous frames
1 n-1
Bayt) ==) IGy.t i) [B(xy.t)I(xy.t)| > th
i=0

If difference at a location less than threshold, then pixel at that location is
background pixel
Else it is mapped as a foreground pixel
New object introduced in the current frame becomes a part of foreground
Current frame holds the newly introduced object and background
Background can also be generated by assigning weights

B(x,y)=(1-a)B(x,y) + a I(x,y)
--- page 8 ---
Q6a
Explain any five challenges of implementing a cereal grain inspection
CO- 4   [10]
SO- 1,6   system using computer vision.
BL- 2
Grain Variability
Shape and Size Variation: Cereal grains often come in varying sizes,
shapes, and orientations. This variation complicates consistent feature
extraction and classification.
Color Variability: Different grains have varying colors, and even within
the same type of grain, ripeness or moisture content can lead to color
changes. Lighting conditions further exacerbate this issue.
Texture Differences: Grain surfaces may differ in texture due to natural
variations or handling. Identifying features based on texture requires
advanced techniques like Local Binary Patterns (LBP) or more complex
CNN models.
2. Imaging Conditions
Lighting Conditions: Changes in lighting, shadows, and reflections during
image capture can significantly affect the quality and consistency of
images. Ensuring uniform lighting in an industrial setting is difficult,
leading to potential inaccuracies.
Background Noise: Separating grain from the background, particularly in
bulk storage or conveyor systems, is challenging. This requires robust
segmentation algorithms to isolate grains accurately.
Solution   Motion Blur: In real-time inspection systems, grains may be moving on
conveyors, leading to motion blur, which can affect image clarity and
reduce the system’s accuracy.
3. Object Detection and Classification
Identifying Defects and Foreign Objects: Detecting small defects or
foreign objects like stones, chaff, or weed seeds requires high-resolution
imaging and fine-tuned detection algorithms, often necessitating complex
deep learning models.
Data Annotation: Training a machine learning model to detect grain
defects or classify different grains requires a large labeled dataset.
Labeling this data can be time-consuming and error-prone.
Grain Overlapping and Occlusion: In bulk inspection scenarios, grains
may overlap, which hinders accurate detection and feature extraction.
4. High Throughput Requirements
Real-time Processing: In industrial applications, grains often move at high
speeds on conveyor belts. Implementing a system that can process
images in real-time, while maintaining high accuracy, is a major
computational challenge.
********** 8 **********
--- page 9 ---
Efficient Algorithms: The system needs to balance accuracy and speed,
especially when dealing with large datasets or high-resolution images.
Lightweight yet accurate models like MobileNet or EfficientNet are
essential for industrial scalability.
5. Data and Model Generalization
Domain Adaptation: A model trained in a controlled lab environment
might not generalize well to field or real-world scenarios due to changes
in lighting, grain quality, or background noise.
Handling Different Grain Types: Cereal grain systems must handle
various grains like wheat, rice, corn, and barley. Training a model to
generalize across different grain types while retaining accuracy can be
difficult.
6. Moisture and Damage Detection
Detecting Internal Defects: Image processing systems typically analyze
external features, making it hard to detect internal defects like moisture
content or fungal infections, which might require more advanced imaging
techniques like X-ray or NIR (Near-Infrared).
Subtle Differences in Damaged Grains: Differentiating between slightly
damaged grains and healthy grains may be challenging, especially when
damage does not significantly alter visible features.
7. Cost and Scalability
Hardware Costs: High-resolution cameras, lighting setups, and
computing power for real-time image processing add significant costs to
implementing a system. Industrial scalability, in terms of processing large
volumes of grains, can further increase costs.
Maintaining System Accuracy Over Time: The system’s performance
might degrade over time due to hardware wear, lighting changes, or grain
quality variations, requiring continuous calibration and maintenance.
(5M) for key points
(5M) for description
Show how 2D Cartesian coordinates are converted to 3D
Q6b
homogeneous coordinates and vice versa. Convert the point (3,4)
CO- 4   from Cartesian to homogeneous form. Also, determine the   [10]
SO- 1,6
BL- 5   corresponding 2D Cartesian coordinates for the homogeneous point
(9,12,3).
********** 9 **********
--- page 10 ---
Solution
(4M)
(4M)
2D point, (3,4) to Homogeneous point is (3,4,1)
3D point (9,12,3) 2D point is (3,4)
(2M)
Q7a   Explain in brief the following:
CO- 4   • World coordinate system   [10]
SO- 1, 6
BL- 3   • Camera coordinate system
********** 10 **********

[Text in pictures on this page, read by OCR]
¢ All the points from origin to ‘p’ along line are equivalent to one another
* Each point on line except origin is homogeneous coordinate of p = (x,y)
* Cartesian to homogeneous, p > p

BLS »=(5
a

By
--- page 11 ---
• Image coordinate system
•   Pixel coordinate system
Solution
(3M) each for the description of World and camera coordinate
system (2M) each image and pixel coordinate systems
Q7b   Draw a labeled sketch of epipolar geometry and explain it with
CO- 4   reference to points, epipolar lines, and the essential and fundamental   [10]
SO- 1,6
BL- 3   matrices.
(5M)
Solution
(5M)
********** 11 **********

[Text in pictures on this page, read by OCR]
* Standard epipolar geometry setup involves two cameras observing the same 3D
point P

* Cameras are located at O, and O,

* Projection of point, P, on the image planes is located at p and p’ respectively

epipolar plane Image planes

oO, \ 2

epipolar line for p’ baseline
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 25d2a4853ff6

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_AIDS_7056/COMPUTER VISION FOR AI/ANS_COMPUTER VISION FOR AI(702AI0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2026
- Text: text (20 pages)

````text
SYNOPTICS
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
1. This question paper contains 20 pages.
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
Solution   • Compute Harris response (R). (3 Marks)
• Classify the feature type (e.g., flat region, edge, or corner) (2 Marks)
Given
𝑆𝑥𝑥= 12, 𝑆𝑦𝑦= 9, 𝑆𝑥𝑦= 5, 𝑘= 0.05
The second moment (structure) matrix is:
𝑀= [𝑆𝑥𝑥 𝑆𝑥𝑦 = [12 5
𝑆𝑥𝑦 𝑆𝑦𝑦]   5   9]
Step 1: Compute Determinant of 𝑀
det⁡(𝑀) = 𝑆𝑥𝑥𝑆𝑦𝑦−𝑆𝑥𝑦 2
det⁡(𝑀) = (12)(9) −(5)2 = 108 −25 = 83
Step 2: Compute Trace of 𝑀
********** 1 **********
--- page 2 ---
trace(𝑀) = 𝑆𝑥𝑥+ 𝑆𝑦𝑦
trace(𝑀) = 12 + 9 = 21
Article I.   Step 3: Harris Corner Response Formula
𝑅= det⁡(𝑀) −𝑘⋅(trace(𝑀))2
Substitute values:
𝑅= 83 −0.05 × (21)2
𝑅= 83 −0.05 × 441
𝑅= 83 −22.05
𝑅= 60.95
Step 4: Feature Classification
General Harris Interpretation
Condition   Interpretation
Small determinant, small
Flat region
trace
Small determinant, large
Edge
trace
Large determinant, large
Corner
trace
In this case
• Determinant = 83 (large )
• Trace = 21 (large )
•   Harris response R = 60.95 > 0 (large positive)
Final Answer
Harris response:
𝑅= 60.95
•   Feature type:
********** 2 **********
--- page 3 ---
Corner
CO- 3   b. Two feature descriptors are given: A=(2,3,1), B=(4,6,2)   [05]
SO-1   i.   Compute cosine similarity between A and B
BL-3   ii.   Comment whether they are good matching keypoints or not.
Solution   i.   Compute cosine similarity between A and B (3 Marks)
ii. Comment whether they are good matching keypoints (2 Marks)
Cosine Similarity Calculation
Given Feature Descriptors:
A = [2, 3, 1]
B = [4, 6, 2]
Step-by-Step Solution:
1. Compute the dot product:
A · B = (2×4) + (3×6) + (1×2) = 28
2. Compute magnitudes:
|A| = √(2² + 3² + 1²) = 3.7417
|B| = √(4² + 6² + 2²) = 7.4833
3. Cosine similarity formula:
cosθ = (A · B) / (|A| × |B|)
cosθ = 28 / (3.7417 × 7.4833) = 1.0000
Conclusion:
Cosine Similarity = 1.0000
Yes, these are good matching keypoints because cosine similarity is very high.
CO- 4   c.   In the context of Mean Shift image segmentation, consider a 1D feature space   [05]
SO- 1   with the following pixel intensity values: X = {5, 15, 18, 24, 27, 30, 35}. If the
BL-2,3   algorithm starts at an initial estimate y1 = 20 with a bandwidthh = 6.
i.   Define the set of points that fall within the kernel window.
ii.   Calculate the mean shift vector and the resulting new center y2
i.   Define the set of points that fall within the kernel window. (3 Marks)
ii.   Calculate the mean shift vector and the resulting new center y2 (2
Marks)
Given:
Feature space X = [5, 15, 18, 24, 27, 30, 35]
Initial estimate y1 = 20
Bandwidth h = 6
Solution:
1. Determine points within the kernel window:
Condition: |xi - y1| ≤ h → |xi - 20| ≤ 6
Points within window: [15, 18, 24]
2. Compute the new center (mean) and mean shift vector:
New center y2 = mean([15, 18, 24]) = 19.0
Mean shift vector = y2 − y1 = 19.0 − 20 = -1.0
Final Answer:
y2 = 19.0
Mean Shift Vector = -1.0
CO- 5   d. Explain the primary purpose of the Convolutional Layer in a CNN. Describe the   [05]
role of "filters" (or kernels) and how they produce a feature map.
********** 3 **********
--- page 4 ---
SO- 1,6
BL- 1,3
Solution   • primary purpose of the Convolutional Layer in a CNN (3 Marks)
• Role of "filters" (or kernels) (2 Marks)
Convolutional Layer in CNN
Primary Purpose of the Convolutional Layer:
The primary purpose of the convolutional layer in a Convolutional Neural
Network (CNN) is to automatically extract meaningful features from input data
such as images. It captures local patterns like edges, corners, and textures while
preserving spatial relationships between pixels. This enables the network to build
hierarchical feature representations and reduces the number of parameters
compared to fully connected layers.
Role of Filters (Kernels):
Filters, also known as kernels, are small matrices of learnable weights (e.g., 3×3
or 5×5). Each filter is designed to detect a specific pattern in the input image,
such as horizontal edges or textures. During training, the CNN learns the optimal
weights of these filters.
Feature Map Generation:
A filter slides over the input image and performs element-wise multiplication
followed by summation at each location. The result of this operation at every
position forms a feature map. Each filter produces one feature map, and multiple
filters generate multiple feature maps representing different features in the input.
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
Solution   i. Roles of low-level, mid-level, and high-level vision. (3 Marks)
ii. Application of autonomous driving   (3 Marks)
iii. Improper functioning of any one level (4 Marks)
Computer Vision (CV) systems are commonly designed as a hierarchical pipeline
consisting of low-level, mid-level, and high-level vision tasks. Each level
processes visual data with increasing abstraction   to enable accurate
understanding and decision-making.
(i) Roles of Low-Level, Mid-Level, and High-Level Vision Tasks:
Low-Level Vision:
Low-level vision operates directly on raw pixel data. Its role is to enhance image
quality and extract basic visual primitives such as edges, corners, and textures.
********** 4 **********
--- page 5 ---
Typical tasks include noise reduction, smoothing, edge detection, and intensity
or color processing. The output is an improved image or basic features.
Mid-Level Vision:
Mid-level vision organizes low-level features into meaningful structures. It
focuses on region formation, segmentation, and shape detection. Common tasks
include image segmentation, contour detection, feature grouping, and object
proposal generation. The output is a structured representation of objects and
regions.
High-Level Vision:
High-level vision performs semantic interpretation of the scene. It involves
recognizing objects, understanding scenes, and making decisions. Tasks include
object recognition, scene understanding, activity recognition, and planning. The
output is semantic labels and decisions.
(ii) Application of Hierarchical Vision in Autonomous Driving:
Low-Level Vision in Autonomous Driving:
In autonomous vehicles, low-level vision processes camera images by removing
noise, enhancing contrast, and detecting edges. For example, lane markings are
detected using edge detection techniques.
Mid-Level Vision in Autonomous Driving:
Mid-level vision segments the scene into different components such as roads,
pedestrians, vehicles, and traffic signs. It also tracks moving objects across
frames.
High-Level Vision in Autonomous Driving:
High-level vision recognizes traffic signs, predicts pedestrian movement, and
makes driving decisions such as stopping or slowing down when obstacles are
detected.
(iii) Effect of Improper Functioning of Any Vision Level:
If Low-Level Vision fails, noise or poor edge detection can lead to incorrect
feature extraction, affecting all higher stages. If Mid-Level Vision fails, improper
segmentation may cause objects to be missed or misidentified. If High-Level
Vision fails, incorrect interpretation can result in wrong decisions, leading to
safety risks in applications like autonomous driving.
Conclusion:
Computer Vision systems rely on a hierarchical design where each level plays a
critical role. Proper functioning of all levels is essential for accurate perception
and reliable decision-making.
Q2   b A grayscale image patch (3×3) is given:   [10]
CO- 1   10 20 10
SO- 1   𝐼= [ 20 40 20 ]
10 20 10
BL- 3
********** 5 **********
--- page 6 ---
0 1   0
i.   Using Laplacian kernel: [ 1 −4 1 ] Compute the LoG response at
0 1   0
the center pixel.
ii.   Given Gaussian responses at two scales: Gσ1=35, Gσ2=25.
Compute DoG and interpret whether it indicates a strong feature or
not.
−1 0 1   −1 −2 −1
iii.   Using Sobel operators: 𝐺𝑥= ⁡[ −2 0 2 ] 𝐺𝑦= ⁡[ 0   0   0 ]
−1 0 1   1   2   1
Compute gradient magnitude and gradient direction
iv.   Assign the gradient to one of the HoG bins: Bins: 00 , 450, 900, 1350
• Laplacian kernel (3 Marks)
• Compute DoG (2 Marks)
• Sobel operators (3 Marks)
• HoG bins   (2 Marks)
Numerical Solution: LoG, DoG, Sobel and HOG
Given Image Patch (3×3):
I = [[10, 20, 10], [20, 40, 20], [10, 20, 10]]
1. LoG Response at Center Pixel
Using Laplacian Kernel [[0,1,0],[1,-4,1],[0,1,0]]
LoG = (1×20 + 1×20 + 1×20 + 1×20) − 4×40 = -100
LoG Response = -100
2. Difference of Gaussian (DoG)
Given: Gσ1 = 35, Gσ2 = 25
DoG = 35 − 25 = 10
Since magnitude is high, it indicates a strong feature.
3. Gradient using Sobel Operators
Computed Gx = 0 and Gy = 0
Gradient Magnitude and Direction
Gradient Magnitude = √(0² + 0²) = 0
Gradient Direction = Undefined (flat region)
4. HOG Bin Assignment
No HOG bin assigned due to zero gradient magnitude.
Q3   a   Consider the below image.   [10]
CO- 2
SO- 1
BL- 2,3
i.   Compute integral image
ii.   Justify that an integral image enables fast computation of filtered image
in algorithms like SURF. Explain with an example
Solution   • Integral Image (5 Marks)
• Fast Computation in SURF (5 Marks)
********** 6 **********
--- page 7 ---
i. Computation of Integral Image
Applying this to your image 𝐼, the integral image is:
For SURF, the integral image at position (𝑥, 𝑦)is defined as:
𝐼𝐼(𝑥, 𝑦) = ∑   𝐼(𝑖, 𝑗)
𝑖≤𝑥, 𝑗≤𝑦
ii. Integral Image for Fast Computation in SURF
The integral image enables fast computation of rectangular sums in constant time,
regardless of the size of the region. This property is heavily used in algorithms
such as SURF for fast box filter evaluation.
For example, to compute the sum of pixel values in a rectangular region using an
integral image, only four array references are required.
If a rectangle is defined by its top-left (x1, y1) and bottom-right (x2, y2) corners,
the sum is computed as:
Sum = II(x2, y2) − II(x1−1, y2) − II(x2, y1−1) + II(x1−1, y1−1)
In SURF, large box filters approximate Gaussian derivatives. Using the integral
image, these filters are applied very efficiently without increasing computational
cost as the filter size grows. This significantly speeds up feature detection and
description.
Thus, the integral image allows rapid computation of filtered responses and is a
key factor behind the real-time performance of SURF and similar Computer
Vision algorithms.
Q3   b The Scale Invariant Feature Transform (SIFT) is widely used for detecting and   [10]
CO- 2   describing local features in images.
SO- 1   i.   Analyze the role of scale-space representation using Difference of
BL-2,3   Gaussian (DoG) in detecting stable keypoints across different image
scales.
ii.   Examine how keypoint localization improves the stability and accuracy
of detected features.
iii.   Analyze how orientation assignment ensures rotation invariance in SIFT.
iv.   Evaluate why SIFT descriptors are more robust compared to simple edge
or corner-based features in real-world image matching applications
Solution   • Role of Scale-Space Representation Using Difference of Gaussian
(DoG)
• Scale-Space Representation (3 Marks)
********** 7 **********
--- page 8 ---
• Keypoint Localization and Its Effect on Stability and Accuracy (3
Marks)
• Orientation Assignment for Rotation Invariance (2 Marks)
• Why SIFT Descriptors Are More Robust Than Simple Edge or
Corner Features (2 Marks)
Scale Invariant Feature Transform (SIFT)
The Scale Invariant Feature Transform (SIFT) is a robust technique used to detect
and describe local features in images. It is designed to be invariant to scale,
rotation, and partially invariant to illumination and viewpoint changes, making it
highly effective for real-world image matching.
i. Role of Scale-Space Representation Using Difference of Gaussian (DoG)
Scale-Space Representation
Objects in images can appear at different sizes due to changes in distance or
resolution. To reliably detect features regardless of scale, SIFT constructs a scale
space by progressively blurring the image with Gaussian filters of increasing
standard deviation (σ).
𝑳(𝒙, 𝒚, 𝝈) = 𝑮(𝒙, 𝒚, 𝝈) ∗𝑰(𝒙, 𝒚)
where 𝑮is a Gaussian kernel and 𝑰is the input image.
Difference of Gaussian (DoG)
Instead of directly using the Laplacian of Gaussian (LoG), SIFT approximates it
efficiently using Difference of Gaussian (DoG):
DoG(𝒙, 𝒚, 𝝈) = 𝑳(𝒙, 𝒚, 𝒌𝝈) −𝑳(𝒙, 𝒚, 𝝈)
Importance of DoG for Keypoint Detection
Detects scale-invariant extrema (maxima/minima) across space and scale
Efficient approximation to LoG
Highlights blob-like structures, which are stable image features
Enables detection of the same physical feature regardless of image scale
Thus, DoG ensures stable keypoints across different image scales.
ii. Keypoint Localization and Its Effect on Stability and Accuracy
After detecting candidate extrema in the DoG scale space, SIFT refines their
locations using keypoint localization.
Keypoint Localization Process
Fits a 3D quadratic function (using Taylor series expansion) around each
candidate keypoint
Accurately determines:
Spatial location (x, y)
Scale (σ)
Rejection of Unstable Keypoints
Keypoints are discarded if they:
Have low contrast (sensitive to noise)
Lie along edges (poorly localized, using Hessian matrix ratio)
Benefits
Improves   repeatability
Eliminates   noise-sensitive   points
********** 8 **********
--- page 9 ---
Ensures   precise   localization
Increases matching accuracy
Result: Only highly stable and distinctive features are retained.
iii. Orientation Assignment for Rotation Invariance
To achieve rotation invariance, SIFT assigns a consistent orientation to each
keypoint.
Orientation Assignment Steps
Compute gradient magnitude and orientation around the keypoint:
𝒎(𝒙, 𝒚) = √(𝑳𝒙)𝟐+ (𝑳𝒚)𝟐
𝜽(𝒙, 𝒚) = 𝐭𝐚𝐧⁡−𝟏(𝑳𝒚/𝑳𝒙)
Create an orientation histogram (usually 36 bins spanning 0°–360°)
Select the dominant orientation(s) based on peak values
Why Orientation Assignment Works
Descriptor is computed relative to the keypoint’s orientation
Any image rotation produces the same relative gradient pattern
Hence, SIFT features remain rotation invariant.
iv. Why SIFT Descriptors Are More Robust Than Simple Edge or Corner
Features
Limitations of Simple Features
Edges: Sensitive to noise and illumination
Corners: Limited distinctiveness
Poor invariance to scale and rotation
Strengths of SIFT Descriptors
SIFT represents each keypoint using a 128-dimensional descriptor based on local
gradient distributions.
Key advantages:
Highly distinctive and descriptive
Invariant to scale and rotation
Robust to illumination changes
Partially invariant to viewpoint changes
Performs well under clutter and occlusion
Q4   a   Given 3 images with histogram of visual words:   [10]
CO- 3   H1 = [4,2,0,1],   H2 = [2,1,3,0],   H3 = [1,2,1,2]
SO- 2   Query image: Q = [3,1,1,1]
i.   Compute TF for each histogram
BL-
ii.   Compute DF and IDF
3,4,5   iii.   Compute TF-IDF for query
iv.   Compute the Euclidean distance between the TF-IDF vector of the query
image and TF vector of each image. Identify the best match.
Solution   i.   Compute TF for each histogram (3 Marks)
ii.   Compute DF and IDF   (3 Marks)
iii.   Compute TF-IDF for query (2 Marks)
********** 9 **********
--- page 10 ---
iv.   Compute the Euclidean distance between the TF-IDF vector of the
query image and TF vector of each image. Identify the best match.
(2 Marks)
TF-IDF and Image Matching using Bag of Visual Words
Given histograms:
H1 = [4, 2, 0, 1]
H2 = [2, 1, 3, 0]
H3 = [1, 2, 1, 2]
Query Q = [3, 1, 1, 1]
i. Term Frequency (TF)
TF(H1) = [0.5714285714285714, 0.2857142857142857, 0.0,
0.14285714285714285]
TF(H2) = [0.3333333333333333, 0.16666666666666666, 0.5, 0.0]
TF(H3) = [0.16666666666666666, 0.3333333333333333,
0.16666666666666666, 0.3333333333333333]
TF(Query) = [0.5, 0.16666666666666666, 0.16666666666666666,
0.16666666666666666]
ii. Document Frequency (DF) and Inverse Document Frequency (IDF)
DF = [3, 3, 2, 2]
IDF = [0.0, 0.0, 0.4054651081081644, 0.4054651081081644]
iii. TF-IDF of Query
TF-IDF(Query) = [0.0, 0.0, 0.06757751801802739, 0.06757751801802739]
iv. Euclidean Distance and Best Match
Distance(Query, H1) = 0.6468
Distance(Query, H2) = 0.5748
Distance(Query, H3) = 0.4683
Best match is Image H3 (minimum distance).
Q4   b   In an image matching system, a set of keypoint descriptors from two images are   [10]
CO- 3   compared using nearest neighbor matching followed by a ratio test. A descriptor
SO- 2   in Image A has the following Euclidean distances to its nearest neighbors in
Image B:
BL-3,4,5
• Best match distance = 0.42
• Second-best match distance = 0.50
Threshold T=0.75
i.   Compute the ratio value and determine whether the match should be
accepted or rejected.
ii.   Explain how the ratio test helps in improving the reliability of feature
matching in real-world applications.
Solution   • Compute the ratio value (5 Marks)
• Ratio test helps in improving the reliability of feature matching (5
Marks)
i. Ratio computation and decision
Given:
Best (nearest) match distance, 𝑑1 = 0.42
Second-best match distance, 𝑑2 = 0.50
Ratio test threshold, 𝑇= 0.75
Ratio value
The ratio test (proposed by Lowe for SIFT) is computed as:
********** 10 **********
--- page 11 ---
𝑑1
Ratio =
𝑑2
0.42
Ratio =   = 0.84
0.50
Decision
Acceptance condition:
𝑑1
< 𝑇
𝑑2
Here:
0.84 > 0.75
Decision: Reject the match
Reason:
Although the best match has a relatively low distance, it is not sufficiently
better than the second-best match. This indicates ambiguity.
ii. How the ratio test improves reliability of feature matching
The ratio test improves matching reliability by eliminating ambiguous
correspondences that frequently arise in real-world images.
Key reasons:
1. Suppresses ambiguous matches
In textured or repetitive regions (e.g., windows, bricks, foliage), a keypoint may
have multiple similar matches. If the best and second-best distances are close, the
match is unreliable.The ratio test rejects such cases automatically.
2. Focuses on match distinctiveness
A good match should be significantly closer than all alternatives. The ratio test
captures this idea numerically by comparing distances rather than using an
absolute threshold.
3. Reduces false positives
Matches caused by noise, illumination changes, or viewpoint variation often
produce similar distances to multiple candidates. Rejecting these reduces
incorrect correspondences.
Q5   a You have deployed a background subtraction system on a static traffic camera to   [10]
CO- 4   count cars passing through an intersection. On a calm, overcast day, it works with
SO- 1   99% accuracy. However, on a sunny, windy day with fast-moving clouds, the
system starts generating hundreds of false positives, flagging empty stretches of
BL-
road and the sides of the street as "moving vehicles."
3,4,5
i. What two specific environmental factors are breaking your basic background
subtraction model, and what advanced background modeling technique should
you implement to fix this?
ii. Explain two fundamental limitations of standard optical flow methods.
Solution   • Background Subtraction (5 Marks)
• and Optical Flow – (5 Marks)
********** 11 **********
--- page 12 ---
i. Environmental Factors and Advanced Background Modeling
Two environmental factors are responsible for breaking the basic background
subtraction model:
1. Illumination changes due to fast-moving clouds:
Rapid changes in sunlight intensity cause sudden brightness variations across
the scene. Basic background subtraction assumes a relatively constant
background, so these illumination shifts are incorrectly detected as moving
objects.
2. Motion of background elements due to wind:
Wind causes trees, shadows, and roadside objects to move. Since traditional
background subtraction treats any pixel change as foreground, these dynamic
background regions produce many false positives.
Advanced Technique to Fix the Problem:
To address these issues, a Mixture of Gaussians (MoG / GMM) background
model should be used. This approach models each pixel as a mixture of multiple
distributions over time, allowing it to adapt to repetitive background motion and
gradual illumination changes while still detecting true moving vehicles.
ii. Fundamental Limitations of Standard Optical Flow Methods
1. Sensitivity to illumination changes:
Optical flow algorithms assume brightness consistency of pixels between
frames. Sudden changes in lighting, shadows, or reflections violate this
assumption, leading to incorrect motion estimates.
2. Difficulty with large or fast motions:
Many optical flow methods rely on small motion assumptions and local
linearization. When objects move quickly or over large distances between
frames, the motion cannot be accurately captured, resulting in errors or missing
flow vectors.
Q5   b   Consider a 5 × 5grayscale image whose pixel intensity values are given by   [10]
CO- 4   10 12 15 14 10
SO- 1   11 25 26 24 12
BL-3,4,5   𝐼= 14 28 30 29 15
12 27 26 25 13
[ 10 11 14 12 10]
Assume that pixel coordinates are indexed using 0-based indexing in the form
(row, column).
The pixel located at position (2,2), which is the center of the image and has an
intensity value of 30, is selected as the initial point for the mean shift algorithm.
Let the spatial bandwidth be 𝑆= 1, where distance is measured using the
Chebyshev (chessboard) distance, resulting in a 3 × 3⁡spatial neighborhood. The
color (intensity) bandwidth is given as ℎ𝑐= 5.
Perform one iteration of the mean shift algorithm and determine:
1. The spatial neighbourhood of the pixel at (2,2).
********** 12 **********
--- page 13 ---
2. The pixels within this neighbourhood that satisfy the color (intensity)
bandwidth condition.
3. The mean intensity of the selected pixels.
4. The new spatial location of the pixel after the mean shift update.
Solution   • Spatial Neighborhood: (3 Marks)
• Pixels satisfying color bandwidth: (3 Marks)
Mean Intensity: (2 Marks)
• new spatial location (2 Marks)
Given Image (5×5):
10 12 15 14 10
11 25 26 24 12
14 28 30 29 15
12 27 26 25 13
10 11 14 12 10
Initial pixel location: (2,2)
Initial intensity: 30
Spatial bandwidth S = 1 (Chebyshev distance)
Color bandwidth h_c = 5
1. Spatial Neighborhood:
Using Chebyshev distance ≤ 1, the 3×3 neighborhood centered at (2,2) is:
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
Corresponding intensities:
25, 26, 24
28, 30, 29
27, 26, 25
2. Pixels satisfying color bandwidth:
|Intensity − 30| ≤ 5
Selected pixels:
28, 30, 29, 27, 26, 25, 26, 25
3. Mean Intensity:
Mean = (28 + 30 + 29 + 27 + 26 + 25 + 26 + 25) / 8
Mean Intensity = 27
4. New Spatial Location:
Coordinates of selected pixels:
(2,1), (2,2), (2,3), (1,2), (3,2), (1,1), (1,3), (3,1)
Mean row = (2+2+2+1+3+1+1+3)/8 = 1.875
Mean column = (1+2+3+2+2+1+3+1)/8 = 1.875
Updated location ≈ (2,2)
Conclusion:
After one mean shift iteration, the pixel remains at (2,2) with updated mean
********** 13 **********
--- page 14 ---
intensity 27.
Q6   a   I. An image retrieval system uses Pyramid Feature Matching to rank results. For   [10]
CO- 2,3   a specific query, the system returns the following intersection scores: Level 0 =
SO- 1   0.90 and Level 1 = 0.98. Calculate the similarity score using
Weight Set A: {w0 = 1, w1 = 0.5}.
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
Solution   • Pyramid Feature Matching (5 Marks)
• HoG Descriptor (5 Marks)
PART I: PYRAMID FEATURE MATCHING (PFM)
Given:
Intersection Scores:
Level 0 = 0.90
Level 1 = 0.98
Weights (Set A):
w0 = 1
w1 = 0.5
Similarity Score Formula:
Similarity = w0 × Score(Level 0) + w1 × Score(Level 1)
Calculation:
Similarity = (1 × 0.90) + (0.5 × 0.98)
Similarity = 0.90 + 0.49
Similarity = 1.39
Final Similarity Score = 1.39/ 1.5=0.926
--------------------------------------------------
PART II: HISTOGRAM OF ORIENTED GRADIENTS (HoG)
Given:
Gradient magnitude = 32
Gradient orientation = 73°
Total bins = 9
Unsigned range = 0° to 180°
Bin width = 20°
Bin boundaries start at 0°
********** 14 **********
--- page 15 ---
Bin boundaries:
0°, 20°, 40°, 60°, 80°, ...
(i) Adjacent Histogram Bins:
Since 73° lies between 60° and 80°, the pixel contributes to:
• 60° bin
• 80° bin
(ii) Interpolation Weights:
Total interval = 80° − 60° = 20°
Distance from 60° = 73° − 60° = 13°
Distance from 80° = 80° − 73° = 7°
Weight for 60° bin = (80 − 73) / 20 = 7 / 20 = 0.35
Weight for 80° bin = (73 − 60) / 20 = 13 / 20 = 0.65
(iii) Distribution of Gradient Magnitude:
Contribution to 60° bin = 32 × 0.35 = 11.2
Contribution to 80° bin = 32 × 0.65 = 20.8
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
Solution   i. Compute the output feature map size (5 Marks)
ii. Compute the number of parameters (5 Marks)
Given CNN Architecture:
Input Image: 64 × 64 × 3
********** 15 **********
--- page 16 ---
-----------------------------------
TASK i: Output Feature Map Size After Each Layer
-----------------------------------
1. Input Layer:
Size = 64 × 64 × 3
2. Layer 1: Conv1
Kernel size = 5 × 5
Stride = 1
Padding = 2 (Same Convolution)
Number of filters = 16
Output size formula:
Output = (W − F + 2P)/S + 1
Height = (64 − 5 + 2×2)/1 + 1 = 64
Width = (64 − 5 + 2×2)/1 + 1 = 64
Depth = 16
Output Size after Conv1 = 64 × 64 × 16
3. Layer 2: MaxPool1
Kernel size = 2 × 2
Stride = 2
Height = (64 − 2)/2 + 1 = 32
Width = (64 − 2)/2 + 1 = 32
Depth remains unchanged
Output Size after MaxPool1 = 32 × 32 × 16
4. Layer 3: Conv2
Kernel size = 3 × 3
Stride = 1
Padding = 0 (Valid Convolution)
Number of filters = 32
Height = (32 − 3 + 0)/1 + 1 = 30
Width = (32 − 3 + 0)/1 + 1 = 30
Depth = 32
Output Size after Conv2 = 30 × 30 × 32
5. Layer 4: FC1
Flattened input = 30 × 30 × 32 = 28800
Output nodes = 128
Output Size after FC1 = 128
6. Output Layer:
Softmax with 5 classes
********** 16 **********
--- page 17 ---
Output Size = 5
-----------------------------------
TASK ii: Number of Parameters in Each Layer
-----------------------------------
1. Conv1 Layer:
Parameters per filter = 5 × 5 × 3 = 75
Total parameters = (75 × 16) + 16 (biases)
Total = 1216
2. MaxPool Layer:
No trainable parameters
Total = 0
3. Conv2 Layer:
Parameters per filter = 3 × 3 × 16 = 144
Total parameters = (144 × 32) + 32 (biases)
Total = 4640
4. Fully Connected Layer (FC1):
Total parameters = (28800 × 128) + 128 (biases)
Total = 3686528
5. Output Layer (Softmax):
Total parameters = (128 × 5) + 5 (biases)
Total = 645
-----------------------------------
FINAL SUMMARY
-----------------------------------
Conv1 Output: 64 × 64 × 16 | Parameters: 1,216
MaxPool Output: 32 × 32 × 16 | Parameters: 0
Conv2 Output: 30 × 30 × 32 | Parameters: 4,640
FC1 Output: 128 | Parameters: 3,686,528
Softmax Output: 5 | Parameters: 645
Q7   a   i.   Identify the two major computational bottlenecks of the original R-CNN   [10]
CO- 5   architecture.
SO- 2   ii.   Explain how Fast R-CNN specifically solved these bottlenecks to achieve
faster training and inference.
BL-4,5
iii.   Identify the remaining bottleneck in Fast R-CNN and explain how Faster
R-CNN eliminated it to achieve true "real-time" or near-real-time object
detection.
Solution   Major Computational Bottlenecks of the Original R-CNN (4 Marks)
How Fast R-CNN Solved These Bottlenecks (3 Marks)
Remaining Bottleneck in Fast R-CNN and How Faster R-CNN Eliminated
It (3 Marks)
i. Major Computational Bottlenecks of the Original R-CNN
********** 17 **********
--- page 18 ---
The original R-CNN (Regions with Convolutional Neural Networks)
architecture suffered from two major computational bottlenecks:
1. Repeated CNN computation for each region proposal:
R-CNN uses an external region proposal method (Selective Search) to
generate around 2000 region proposals per image. Each proposal is
independently cropped, resized, and processed through a full convolutional
neural network. This leads to massive redundant computation and very slow
inference.
2. Multi-stage training pipeline:
R-CNN requires a complex, multi-step training process involving CNN fine-
tuning, SVM training for classification, and separate bounding box regression
training. This fragmented pipeline increases training time, storage requirements,
and implementation complexity.
ii. How Fast R-CNN Solved These Bottlenecks
Fast R-CNN introduced key architectural improvements to efficiently address
the limitations of R-CNN:
1. Single shared convolutional feature map:
Instead of running the CNN separately on each region proposal, Fast R-CNN
processes the entire image once through the convolutional layers to generate a
shared feature map. Region proposals are then projected onto this feature map,
eliminating redundant CNN computations.
2. ROI Pooling layer:
Fast R-CNN introduces the Region of Interest (ROI) Pooling layer, which
extracts fixed-size feature vectors from the shared feature map for each
proposal. This enables batch processing of proposals and efficient GPU
utilization.
3. End-to-end multi-task training:
Fast R-CNN replaces the multi-stage training of R-CNN with a single end-to-
end training process using a multi-task loss that jointly optimizes classification
and bounding box regression.
These improvements significantly reduce both training and inference time while
improving detection accuracy.
iii. Remaining Bottleneck in Fast R-CNN and How Faster R-CNN Eliminated It
Remaining Bottleneck in Fast R-CNN:
The primary bottleneck in Fast R-CNN is the use of an external region proposal
algorithm (Selective Search). This method runs on the CPU and is
computationally expensive, taking significant time per image and preventing
real-time performance.
How Faster R-CNN Eliminated This Bottleneck:
Faster R-CNN introduces the Region Proposal Network (RPN), a fully
********** 18 **********
--- page 19 ---
convolutional network that shares the same convolutional features as the
detection network. The RPN generates high-quality region proposals directly on
the GPU, eliminating the need for Selective Search.
By integrating region proposal generation into the neural network and sharing
features, Faster R-CNN achieves near real-time object detection while
maintaining high accuracy.
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
Solution   • Role of RoIAlign in Preventing Quantization Errors (4 Marks)
• Why Bounding Boxes from YOLO Are Unsafe for Laser Surgery (3
Marks)
• Encoder–Decoder Architecture in Medical Image Segmentation (3
Marks)
A MedTech company is designing an autonomous microsurgical robot for
glioblastoma removal using a laser scalpel. Extreme spatial accuracy is required
to avoid damaging healthy brain tissue.
------------------------------------------------------------
i. Role of RoIAlign in Preventing Quantization Errors
------------------------------------------------------------
Standard RoIPool converts floating-point region proposals into discrete grid
locations by rounding coordinates to integer values. This rounding
(quantization) causes spatial misalignment between the proposed region and the
extracted features, leading to loss of fine spatial details.
RoIAlign eliminates this issue by avoiding any coordinate rounding. Instead, it
preserves the exact floating-point coordinates and uses bilinear interpolation to
compute the feature values at precise sub-pixel locations. This maintains spatial
correspondence between MRI pixels and feature maps.
********** 19 **********
--- page 20 ---
In neurosurgery, even a few-pixel error can translate to sub-millimeter
inaccuracies, potentially damaging critical neurons. RoIAlign ensures sub-pixel
accuracy, allowing the laser scalpel to follow the exact tumor boundary.
------------------------------------------------------------
ii. Why Bounding Boxes from YOLO Are Unsafe for Laser Surgery
------------------------------------------------------------
YOLO models detect objects using rectangular bounding boxes, which only
provide coarse localization. A bounding box encloses both tumor tissue and
surrounding healthy brain matter.
If a laser scalpel used a bounding box for guidance, it would indiscriminately
vaporize all tissue inside the rectangle, including vital healthy neurons. This
lack of pixel-level precision makes bounding boxes unsuitable for surgical
applications.
In contrast, segmentation masks (as produced by Mask R-CNN or U-Net)
provide pixel-perfect delineation of tumor boundaries, enabling selective laser
ablation and patient safety.
------------------------------------------------------------
iii. Encoder–Decoder Architecture in Medical Image Segmentation
------------------------------------------------------------
The encoder takes the input MRI image and progressively applies convolution
and pooling operations to extract high-level semantic features. During this
process, spatial resolution is reduced while contextual understanding ("what is
present") is increased.
The decoder performs the reverse operation. It upsamples the encoded features
back to the original image resolution using techniques like transposed
convolution or interpolation. By combining high-level semantic information
with low-level spatial details (often via skip connections), the decoder
reconstructs an accurate, pixel-wise segmentation of the tumor.
This encoder–decoder structure allows precise localization of tumor boundaries
while leveraging deep contextual understanding.
********** 20 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 05f45a5bd61b

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_AIML_7053/COMPUTER VISION FOR AI/ANS_COMPUTER VISION FOR AI(702AI0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all, 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q1   Answer briefly:
CO-1;   a.   For each of the following applications, identify which feature level (Low-   [04]
SO-1;
level, Mid-level, or High-level) is most appropriate, and explain your
BL-5
reasoning.
i) Detecting car wheels based on feature descriptors and matching
ii) Detecting a person with a hat using semantic relation of objects
Solutio   i) Detecting car wheels: Mid-level features   [02]
n
a. Detecting a car wheel primarily relies on geometric structure and
grouping, making it a quintessential Mid-level feature task.
ii) Detecting a person with a hat: High-level features
This task requires two distinct object recognition steps and a   [02]
semantic relationship between them, making it a High-level feature
task.
CO-2;   b.   Justify that Speeded Up Robust Features (SURF) is fast. Given the [04]
SO-1;
following Hessian matrices for three key points at intermediate of SURF.
BL-5
Test whether SURF stops comparison or continues with the calculation of
Euclidean distance for comparison?
H1 =[10 −1   H2 =[10 −2   H3 =[10 −1
−1 15],   −2 −15],   −1 −5]
Solution   •   It is a speeded-up version of SIFT (Fast and robust algorithm)   [03]
.   • Approximates LoG with Box Filter
********** 1 **********
--- page 2 ---
• Convolution with box filter using integral images speeds up the
process
• Convolution can be done in parallel for different scales
• Thus enabling real-time applications such as tracking and object
recognition
• Uses determinant of Hessian matrix for both scale and location not
trace
Trace1 = 25,   Trace2 = -5,   Trace3 = 5
It will check the Euclidean distance between key point 1 and key point 3
as sign of trace is same.   [01]
CO-3;   c.   Use Earth Mover Distance test whether the given two images match.   [04]
SO-1;
BL-5   1   1   0   0   1   2   1   1
1   2   0   0   2   2   1   1
2   2   3   3   3   3   0   0
1   2   3   2   3   3   0   0
Image 1 (2-bit)   Image 2 (2-bit)
Ans.   Level 0
• Normalized histogram of image1,
p10 = [4/16, 4/16, 5/16, 3/16]   [03]
c10 = [4/16, 8/16, 13/16, 16/16]
• Normalized histogram of image2,   [01]
p20 = [4/16, 5/16, 3/16, 4/16]
c20 = [4/16, 9/16, 12/16, 16/16]
4
𝐸𝑀𝐷𝐿0 = ∑|𝑐10(𝑖) −𝑐20(𝑖)|
𝑖=0
1   1
𝐸𝑀𝐷𝐿0 = 0 + + + 0
16 16
𝐸𝑀𝐷𝐿0 = 0.25
Level 1
Down sample image by averaging:
1   0
2   3
Image 1 (2-bit)
Image 2 (2-bit)
********** 2 **********
--- page 3 ---
• Normalized histogram of image1, p11 = [1/4,   2   1   1/4, 1/4, 1/4]
3   0
c11 = [1/4, 2/4, 3/4, 4/4]
• Normalized histogram of image2, p21 = [1/4, 1/4, 1/4, 1/4]
c21 = [1/4, 2/4, 3/4, 4/4]
𝐸𝑀𝐷𝐿0 = 0
• Weights of levels, wL0 = 1.0, wL1 = 0.5
• Pyramid with EMD Score
= [(wL0 × EMDL0 )+(wL1 × EMDL1)]/(wL0 + wL1)
= [(1×0.25)+(0.5x0)]/1.5 = 0.167
Small EMD indicates a close similarity between the two histograms
CO-4;   d.   In the context of optical flow, what does the velocity vector represent?   [04]
SO-1;
Compare sparse and dense optical flow.
BL-2
Ans.   • Calculates velocity of points between consecutive frames of video   [01]
• Thus, describes speed and direction of the movement of objects for a
sequence of frames
• And provides an estimation of location of points in the next frame
Sparse optical flow
•   Is flow vectors of interest points of frames
• K interest points have K number of velocity vectors   [03]
•   Interest points could be edges or corners of object in a frame
Dense optical flow
• Provides flow vectors of all pixels
• Has one flow vector per pixel
• Has higher accuracy
•   Is slow and computationally expensive
CO-5;   e.   For Region based Convolutional Network, explain the role of ‘Bounding   [04]
SO-1;
Box Regressor’ algorithm.
BL-3
Ans.   • Bounding box are provided for training CNN
• Bounding box generated is for region proposal which may contain a part [02]
of the object
• While Ground truth box is for the entire object
• Intersection over union (IOU) of the boxes measures the closeness of   [02]
bounding with Ground Truth box
• Select region proposals with IOU > 0.5 with any of ground truth boxes
• Other proposals are background proposals
********** 3 **********
--- page 4 ---
Q2   a   For Histogram of Gradient,   [10]
CO-1;   i) Describe the steps for determining HoG descriptor in brief
SO-1;
ii) For image size of 64×128, calculate the length of HoG vector for 8×8
BL-3
pixels/cell and 4×4 cells/ block.
Ans.   i) Steps
• Crop image to obtain image patch
• Divide patch by cells of 8 ⨯ 8 pixels
• Compute the gradients for pixels in the patch (localized portion)
• Make histograms using the computed gradients (magnitude and   [05
orientation) for each cell   ]
• Apply normalization with neighboring histograms
• Concatenate all histograms to form a vector
• Vector represents feature descriptor of the image patch
• Use features to compare objects
• Or use features to train classifier
ii) Length of descriptor
• Each block contains 4 cells ( 1 histogram/ cell)
• Each block has 4 histograms (9 values/ histogram)
• Concatenate 4 histograms to form a 36 x 1 element vector for a
[05
block
]
• 16×16 block is moved in steps of 8 ( i.e. 50% overlap with the
previous block )
• Number of blocks = 7 x 15 = 105
• For each block, there are 36 values
• Length of the final vector 105×36 = 3780
CO-2;   b   For the given image, apply Harris corner detector to test whether pixel at   [10]
SO-1;
the center is corner pixel or not. Sobel operators Gx and Gy. Size of
BL-3
window is 3×3. (Given: k = 0.04 and threshold for corner response =
1000).
0   0   0   0   0
0   0   0   0   0
1   1   1   0   0
1   1   1   0   0
1   1   2   0   0
********** 4 **********
--- page 5 ---
Image
−1 0 1   −1 −2 −1
𝐺𝑥= [ −2 0 2 ] ,   𝐺𝑦= [ 0   0   0 ]
−1 0 1   1   2   1
Ans.
0 0   0   0 0   0 0 0 0 0
0 0 −1 −1 0   0 4 3 1 0
𝐼𝑥= 1 0 −3 −3 0 ,   𝐼𝑦= 1 4 3 1 0
1 1 −4 −5 0   1 1 2 1 0
[ 1 1   2   0   0]   [ 1 1 2 0 0]
[04
]
0 0 0   0 0   0 0 0 0 0
0 0 1   1 0   0 16 9 0 0
𝐼𝑥2 = 1 0 9   9 0 ,   𝐼𝑦2 = 1 16 9 0 0
1 1 16 25 0   1 1 4 0 0
[ 1 1 2   0   0]   [ 1 1 2 0 0]
[01
0 0 0   0   0   ]
0 0 −3 −1 0
𝐼𝑥. 𝐼𝑦= 1 0 −9 −3 0
1 1 −8 −5 0
[ 1 1 2   0   0]
𝐼𝑥 2   𝐼𝑥𝐼𝑦   62 −28
𝐻= ∑𝑤(𝑥, 𝑦) [   2 ] = [   ]   [01
𝐼𝑥𝐼𝑦   𝐼𝑦   −28 55
𝑥,𝑦   ]
𝑅= 𝑑𝑒𝑡(𝐻) −𝑘. {𝑡𝑟𝑎𝑐𝑒(𝐻)}2
𝑅= {(62 × 55) −(−28 × −28)} −0.04 × {62 + 55}2 = 2078.44   [01
R > 1000, it is a corner.   ]
[02
]
[01
]
Q3   a   For Oriented FAST and Rotated BRIEF (ORB),   [10]
CO-2;   i) Write the roles of FAST and rBrief.
SO-1;
ii) Find the orientation of the highlighted key point
BL-5
1   1   1   1   1
********** 5 **********
--- page 6 ---
1   10   10   10   1
Image =   1   10   40   10   1
1   10   10   10   1
1   1   1   1   1
iii) List advantages
Ans   i) Fusion of FAST key point detector and rBRIEF descriptor at each   [02
scale   ]
• FAST is used to detect key points of the image pyramid
• Uses rotated BRIEF based on the orientation of each key point
ii) Orientation
x=0 x=1 x=2 x=3 x=4
y=0   1   1   1   1   1
y=1   1   10   10   10   1
y=2   1   10   40   10   1
y=3   1   10   10   10   1
[05
y=4   1   1   1   1   1
]
𝑚00 = ∑𝐼(𝑥, 𝑦) = (16 ∗1) + (8 ∗10) + 40 = 136
𝑥,𝑦
𝑚10 = ∑𝑥 . 𝐼(𝑥, 𝑦)
𝑥,𝑦
𝑚10 = (0 ∗5) + (1 ∗32) + (2 ∗62) + (3 ∗32) + (4 ∗5) = 272
𝑚01 = ∑𝑦 . 𝐼(𝑥, 𝑦)
𝑥,𝑦
𝑚01 = (0 ∗5) + (1 ∗32) + (2 ∗62) + (3 ∗32) + (4 ∗5) = 272
(𝑚01
𝜃= 𝑡𝑎𝑛−1 ( 𝑚00) ) = 𝑡𝑎𝑛−1 (𝑚01 ) = 𝑡𝑎𝑛−1 (272 272) = 45
(𝑚10   𝑚10
𝑚00)
Orientation of key point is 45°
iii) Advantages
•   Fast, therefore suitable for real time applications
• Scale invariant, enabling it to detect features at different scales
within an image
•   Rotation-invariant, can match object even if the object is oriented
• Not patented like SIFT or SURF   [3]
********** 6 **********
--- page 7 ---
Q3   b   For the generation of feature descriptors using Speeded Up Robust   [10]
CO-3;   Features (SURF), list the steps and explain it in brief.
SO-1;
Justify that SURF is faster than SIFT.
BL-3,5
Ans
Detector   [03
1. Construct Hessian matrix using box filters at each pixel and   ]
identify key points
2. Increase the size of box filters and repeat step 1
3. For each key point, select points within radius of 6s, where s is
standard deviation of filter for key point
4. Apply Gaussian filter of 2.5s on key point
5. Use Haar wavelet of size 4s to determine magnitude and direction
of points
6. Draw histogram of orientation for 6 bins to identify orientation of
key point
Descriptor
1. Around each key point, choose points within region of square with   [04
size (20s, 20s)   ]
2. Divide region into 16 sub-regions
3. For each sub-region, determine vector of length 4
4. Length of descriptor vector for region is 64
SIFT
• High dimensionality
• Leads to good accuracy   [03
• Approximates Laplacian of Gaussian with DoG   ]
• Uses determinant and trace of Hessian matrix
SURF
•   It is a speeded-up version of SIFT (Fast and robust algorithm)
• Approximates LoG with Box Filter
• Convolution with box filter using integral images speeds up the
process
• Convolution can be done in parallel for different scales
• Thus enabling real-time applications such as tracking and object
recognition
********** 7 **********
--- page 8 ---
• Uses determinant of Hessian matrix for both scale and location not
trace
Q4   a   Explain the steps involved in the Bag of Visual Words for feature matching.   [10]
CO-3;
Use example images and histograms for the explanation. K-means
SO-1;
BL-5   clustering uses K = 6
Ans.   First image
1. Extract descriptors of first image   [05
• Choose strong key points, N=10   ]
• Determine corresponding descriptors of length 128
2. Apply K-means clustering on descriptors
• Groups similar descriptors
• Generate K groups or clusters, K=5
• Determine Cluster mean, also called cluster centres
•   Set of K clusters is a visual vocabulary
• Length of each cluster center is length of feature descriptor
Second image
1. Extract feature of key points of second image
2. For each key point, find the nearest cluster from K clusters of first
image
3. Assign the nearest cluster of first image to descriptor of the second
image
4. There can be several descriptors of second image which are
assigned a particular cluster of first image
5. Generate Histogram of K visual words for the image
[05] marks for images and histograms
CO-5;   b   Design an appropriate Convolutional Neural Network (CNN) model with   [10]
SO-1;
the following architecture specifications for an input gray image of size
BL-6
64 × 64.
• One convolutional layer with 12 filters, each of size 3×3
• One max pooling layer with pool size (3×3)
• One dropout layer with probability 0.1
• One flatten layer
********** 8 **********
--- page 9 ---
• Three dense (fully connected) layers
• No padding (i.e., "valid" convolution)
•   Stride = 1 for convolution
Tasks:
1. Provide the output shape after each layer.
2. Do not consider bias terms at any layer.
3. Clearly specify activation functions.
Ans.   Possible solution:
Layer   Description   Formula /   Activation Output
Reasoning   Shape
Input   Gray image   64×64×1   —   (64,
64, 1)
Conv2D   12 filters, 3×3, (64 − 3 + 1) = ReLU   (62,
stride 1, valid   62 → 62×62   62, 12)
padding   spatial size
MaxPooling2D pool size =   floor(62 / 3) —   (20,   [05
(3×3), stride = = 20   20, 12)
3   ]
Dropout   rate = 0.1   (no change in —   (20,
shape)   20, 12)
Flatten   Flatten 3D →   20×20×12 = —   (4800,)
1D   4800
Dense 1   128 units   —   ReLU   (128,)
Dense 2   64 units   —   ReLU   (64,)
Dense 3   10 units (e.g., —   Softmax   (10,)   [05
10-class
output)   ]
Q5   a   For Gaussian Mixture Model, explain   [10]
CO-4;   i)   Key feature
SO-1;
ii)   Initialization phase
BL-2
iii)   Matching of pixels with Gaussian curve
Ans.   • Generate mixture of ‘k’ Gaussians distribution models for each
pixel of background frame.
•   Values for ‘k’ is in the range 3 to 5
• Weight of each distribution is proportional to the amount of time
each color/intensity stays on that pixel   [02
•   If a pixel has almost the same intensity for few consecutive   ]
frames. Weight of the Gaussian distribution of the pixel is more.
This pixel is a background pixel
********** 9 **********
--- page 10 ---
•   If weight of Gaussian distribution of a pixel is low, that pixel
classified as a foreground pixel
• Each pixel value of reference/ background frame corresponds to 3
Gaussian mixtures
• Each Gaussian Distribution has different parameters
• Model parameters are updated with each new frame
Initialization
•   Create a Gaussian model for a pixel value at a location in the first
frame, x1   [02
• Use w=1 and μ = x1 and large σ for Gaussian model   ]
Match pixel in the next frame
• Check if Gaussian includes pixel at the same location in the next
frame
•   Pixel value is xt, at = 2 (for the second frame)
• Matching conditions for xt
• Case 1 (matches with at least of one of K Gaussians): update all   [06
matched Gaussian curves   ]
• Case 2 (no match in any Gaussian): create a Gaussian to model xt
{1 𝑖𝑓 ( 𝑥𝑡−𝜇𝑘 𝑡−1) ≤2.5 𝜎𝑘 𝑡−1
𝑀𝑘(𝑥𝑡) =
0   𝑂𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒
•   If xt is satisfying matching condition, Update parameters of all
matched Gaussians to include xt in the matched Gaussian curve
CO-5;   b   In a Single-Shot Detector (SSD), feature maps of sizes 38×38, 19×19,   [10]
SO-1;
10×10, and 5×5 are used for multi-scale detection. Each location predicts
BL-3
4 bounding boxes with 21 class scores.
• Calculate the total number of bounding boxes generated.
• How many total output values (bounding box coordinates + class
scores) are produced for one image?
Ans.   Feature Map 1: 38×38
• Number of locations = 38 × 38 = 1,444
********** 10 **********
--- page 11 ---
• Bounding boxes = 1,444 × 4 = 5,776
Feature Map 2: 19×19
• Number of locations = 19 × 19 = 361
• Bounding boxes = 361 × 4 = 1,444
Feature Map 3: 10×10
• Number of locations = 10 × 10 = 100
• Bounding boxes = 100 × 4 = 400
Feature Map 4: 5×5
• Number of locations = 5 × 5 = 25
• Bounding boxes = 25 × 4 = 100
Total = 5,776 + 1,444 + 400 + 100 = 7,720 bounding boxes   [06
]
Total Output Values (Bounding Box Coordinates + Class Scores)
For each bounding box, the SSD outputs:
• 4 coordinates (x_center, y_center, width, height) or (x_min,
y_min, x_max, y_max)
• 21 class scores (confidences for each of the 21 classes)
Output values per bounding box = 4 + 21 = 25 values
Method 1: Using total bounding boxes
Total output values = Total bounding boxes × (coordinates + class scores)
Total output values = 7,720 × 25 = 193,000 values
[04
]
Q6   a   Give an overview of the U-Net architecture for image segmentation and   [10]
CO-5;   explain the working of its encoder–decoder structure with a neat
SO-1;
schematic diagram.
BL-2
Ans.   Reference:
********** 11 **********
--- page 12 ---
[03
]
• Input image: U-Net starts with a 2D image, such as a medical
scan or a satellite photo. The goal is to assign a class label to every
pixel in the image.   [03
• Downsampling: The image passes through convolutional layers   ]
that learn important visual features. As the image moves through
different layers, its resolution decreases, and the model identifies
broader patterns.
• Bottleneck layer: At the center of the network, the feature maps
reach their smallest spatial resolution while capturing high-level
semantic features. Simply put, this compressed representation of
the feature maps is the overall context of the input.
• Upsampling: The network then reconstructs the image by
gradually increasing the resolution. Transposed convolutions help
expand the feature maps back toward the original size.
• Skip connections: The feature maps from the downsampling path   [04
are concatenated with those in the upsampling path. This helps   ]
preserve fine-grained spatial details while integrating high-level
contextual information.
• The output is a segmentation map: The final output is a pixel-
wise segmentation mask matching the input size. Each pixel is
classified into a category like object, background, or region of
interest.
CO-4;   b   Draw architecture of Mask RCNN and explain it in brief. Justify the use   [10]
SO-1;
of RoI align in Mask RCNN
BL-3
********** 12 **********

[Text in pictures on this page, read by OCR]
128 64 642

Contraction network Expansion network

Output imag

Input image Eases

572x572 x3

256 128
Li
lglg

a 512 256
3x3, ReLU
SS Zz (ts => conv 3x3, Rel

3 Bx
S# 512 512 1024 sin tS &   —coPyand crop

= # max pool 2x2
*
88 SF: 1024 4A & # up-conv 2x2
_aemes—
a = conv 1x1

o

°
--- page 13 ---
Ans.
• A region proposal on image, width = 200 and height = 145
•   Scale factor = 512/16 = 32
• On feature map, width = 200/32= 6.25 and height = 145/32 = 4.53
•   Coordinates of centre on feature map, x = 9.25, y = 6
•   If size and coordinates of the box are quantized
• Some part of ROI is not processed
• Looses data if coordinates are quantized
•   Therefore ROI align is used
RoI align
• For 3×3 pooling, divide ROI into 9 cells
•   Size of each cell (4.53/3 = 1.51) × (6.53/3 = 2.08)
[04
]
********** 13 **********

[Text in pictures on this page, read by OCR]
Mask RCNN

Input Image

CNN (Ex: Resnet)
Shared Feature Map

Region Proposal Network

Region Proposals

ROI Align

FC Layers
Soft =
2 BB regressor Mask head
Classifier - .

Predicted Class Refined Box Mask Coord
--- page 14 ---
[02
]
• Determine equidistant 4 points in each cell
• Apply bilinear interpolation for intensity at each point of the cell
• Apply max pooling in each cell
Q7   a   Explain the steps of Scale-Invariant Feature Transform in brief. Describe   [10]
CO-1;   the generation descriptor after key point localization of SIFT algorithm.
SO-1;
BL-3
Ans.   • Determine histogram for each cell around key point   [05]
• 16 cells and 8 orientations = 16x8 = 128 bins with magnitude of
gradients as bin value
•   Feature vector of each key point contains 128 elements
• Use Gaussian-weighted circular window with σ equals to 1.5 times
the scale of the image at which key point is selected
• Gaussian window is used to give less emphasis to gradients that
are far from the key point
[05]
• 16 cells and 8 orientations 128 values
• SIFT feature vector of each key point contains 128 elements
********** 14 **********
--- page 15 ---
CO-3;   b   Explain Region Proposal Network of Faster RCNN and justify that it   [10]
SO-1;
makes Faster RCNN is faster than Fast RCNN. Illustrate with example
BL-3
images.
Ans.   • Uses Region Proposal Network (RPN) instead of selective search
method   [5]
• RPN generates regions which possibly contain objects
• These proposals are given to ROI pooling
• Use CNN to generate feature map with ‘C’ channels
• Use a window of size n×n (ex: 3×3)
• Output at each location shows whether the region contains an
object or not
• Move the window to capture all parts of image
•
[05
]
•   Usually, scale of 1:1, 1:2, 1:3, 2:1, etc are used for anchor boxes
• Apply 1×1 convolution on window (red region) to generate
features of size 1×1×C
********** 15 **********
--- page 16 ---
•   Feature corresponding to window which covers a part of the object
is useful to guess whether reference boxes contain an object or not
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 4c67c8cc2b7b

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_AI_7012/COMPUTER VISION FOR AI/ANS_COMPUTER VISION FOR AI(702AI0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all, 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q1   Answer briefly:
CO-1;   a.   For each of the following applications, identify which feature level (Low-   [04]
SO-1;
level, Mid-level, or High-level) is most appropriate, and explain your
BL-5
reasoning.
i) Detecting car wheels based on feature descriptors and matching
ii) Detecting a person with a hat using semantic relation of objects
Solutio   i) Detecting car wheels: Mid-level features   [02]
n
a. Detecting a car wheel primarily relies on geometric structure and
grouping, making it a quintessential Mid-level feature task.
ii) Detecting a person with a hat: High-level features
This task requires two distinct object recognition steps and a   [02]
semantic relationship between them, making it a High-level feature
task.
CO-2;   b.   Justify that Speeded Up Robust Features (SURF) is fast. Given the [04]
SO-1;
following Hessian matrices for three key points at intermediate of SURF.
BL-5
Test whether SURF stops comparison or continues with the calculation of
Euclidean distance for comparison?
H1 =[10 −1   H2 =[10 −2   H3 =[10 −1
−1 15],   −2 −15],   −1 −5]
Solution   •   It is a speeded-up version of SIFT (Fast and robust algorithm)   [03]
.   • Approximates LoG with Box Filter
********** 1 **********
--- page 2 ---
• Convolution with box filter using integral images speeds up the
process
• Convolution can be done in parallel for different scales
• Thus enabling real-time applications such as tracking and object
recognition
• Uses determinant of Hessian matrix for both scale and location not
trace
Trace1 = 25,   Trace2 = -5,   Trace3 = 5
It will check the Euclidean distance between key point 1 and key point 3
as sign of trace is same.   [01]
CO-3;   c.   Use Earth Mover Distance test whether the given two images match.   [04]
SO-1;
BL-5   1   1   0   0   1   2   1   1
1   2   0   0   2   2   1   1
2   2   3   3   3   3   0   0
1   2   3   2   3   3   0   0
Image 1 (2-bit)   Image 2 (2-bit)
Ans.   Level 0
• Normalized histogram of image1,
p10 = [4/16, 4/16, 5/16, 3/16]   [03]
c10 = [4/16, 8/16, 13/16, 16/16]
• Normalized histogram of image2,   [01]
p20 = [4/16, 5/16, 3/16, 4/16]
c20 = [4/16, 9/16, 12/16, 16/16]
4
𝐸𝑀𝐷𝐿0 = ∑|𝑐10(𝑖) −𝑐20(𝑖)|
𝑖=0
1   1
𝐸𝑀𝐷𝐿0 = 0 + + + 0
16 16
𝐸𝑀𝐷𝐿0 = 0.25
Level 1
Down sample image by averaging:
1   0
2   3
Image 1 (2-bit)
Image 2 (2-bit)
********** 2 **********
--- page 3 ---
• Normalized histogram of image1, p11 = [1/4,   2   1   1/4, 1/4, 1/4]
3   0
c11 = [1/4, 2/4, 3/4, 4/4]
• Normalized histogram of image2, p21 = [1/4, 1/4, 1/4, 1/4]
c21 = [1/4, 2/4, 3/4, 4/4]
𝐸𝑀𝐷𝐿0 = 0
• Weights of levels, wL0 = 1.0, wL1 = 0.5
• Pyramid with EMD Score
= [(wL0 × EMDL0 )+(wL1 × EMDL1)]/(wL0 + wL1)
= [(1×0.25)+(0.5x0)]/1.5 = 0.167
Small EMD indicates a close similarity between the two histograms
CO-4;   d.   In the context of optical flow, what does the velocity vector represent?   [04]
SO-1;
Compare sparse and dense optical flow.
BL-2
Ans.   • Calculates velocity of points between consecutive frames of video   [01]
• Thus, describes speed and direction of the movement of objects for a
sequence of frames
• And provides an estimation of location of points in the next frame
Sparse optical flow
•   Is flow vectors of interest points of frames
• K interest points have K number of velocity vectors   [03]
•   Interest points could be edges or corners of object in a frame
Dense optical flow
• Provides flow vectors of all pixels
• Has one flow vector per pixel
• Has higher accuracy
•   Is slow and computationally expensive
CO-5;   e.   For Region based Convolutional Network, explain the role of ‘Bounding   [04]
SO-1;
Box Regressor’ algorithm.
BL-3
Ans.   • Bounding box are provided for training CNN
• Bounding box generated is for region proposal which may contain a part [02]
of the object
• While Ground truth box is for the entire object
• Intersection over union (IOU) of the boxes measures the closeness of   [02]
bounding with Ground Truth box
• Select region proposals with IOU > 0.5 with any of ground truth boxes
• Other proposals are background proposals
********** 3 **********
--- page 4 ---
Q2   a   For Histogram of Gradient,   [10]
CO-1;   i) Describe the steps for determining HoG descriptor in brief
SO-1;
ii) For image size of 64×128, calculate the length of HoG vector for 8×8
BL-3
pixels/cell and 4×4 cells/ block.
Ans.   i) Steps
• Crop image to obtain image patch
• Divide patch by cells of 8 ⨯ 8 pixels
• Compute the gradients for pixels in the patch (localized portion)
• Make histograms using the computed gradients (magnitude and   [05
orientation) for each cell   ]
• Apply normalization with neighboring histograms
• Concatenate all histograms to form a vector
• Vector represents feature descriptor of the image patch
• Use features to compare objects
• Or use features to train classifier
ii) Length of descriptor
• Each block contains 4 cells ( 1 histogram/ cell)
• Each block has 4 histograms (9 values/ histogram)
• Concatenate 4 histograms to form a 36 x 1 element vector for a
[05
block
]
• 16×16 block is moved in steps of 8 ( i.e. 50% overlap with the
previous block )
• Number of blocks = 7 x 15 = 105
• For each block, there are 36 values
• Length of the final vector 105×36 = 3780
CO-2;   b   For the given image, apply Harris corner detector to test whether pixel at   [10]
SO-1;
the center is corner pixel or not. Sobel operators Gx and Gy. Size of
BL-3
window is 3×3. (Given: k = 0.04 and threshold for corner response =
1000).
0   0   0   0   0
0   0   0   0   0
1   1   1   0   0
1   1   1   0   0
1   1   2   0   0
********** 4 **********
--- page 5 ---
Image
−1 0 1   −1 −2 −1
𝐺𝑥= [ −2 0 2 ] ,   𝐺𝑦= [ 0   0   0 ]
−1 0 1   1   2   1
Ans.
0 0   0   0 0   0 0 0 0 0
0 0 −1 −1 0   0 4 3 1 0
𝐼𝑥= 1 0 −3 −3 0 ,   𝐼𝑦= 1 4 3 1 0
1 1 −4 −5 0   1 1 2 1 0
[ 1 1   2   0   0]   [ 1 1 2 0 0]
[04
]
0 0 0   0 0   0 0 0 0 0
0 0 1   1 0   0 16 9 0 0
𝐼𝑥2 = 1 0 9   9 0 ,   𝐼𝑦2 = 1 16 9 0 0
1 1 16 25 0   1 1 4 0 0
[ 1 1 2   0   0]   [ 1 1 2 0 0]
[01
0 0 0   0   0   ]
0 0 −3 −1 0
𝐼𝑥. 𝐼𝑦= 1 0 −9 −3 0
1 1 −8 −5 0
[ 1 1 2   0   0]
𝐼𝑥 2   𝐼𝑥𝐼𝑦   62 −28
𝐻= ∑𝑤(𝑥, 𝑦) [   2 ] = [   ]   [01
𝐼𝑥𝐼𝑦   𝐼𝑦   −28 55
𝑥,𝑦   ]
𝑅= 𝑑𝑒𝑡(𝐻) −𝑘. {𝑡𝑟𝑎𝑐𝑒(𝐻)}2
𝑅= {(62 × 55) −(−28 × −28)} −0.04 × {62 + 55}2 = 2078.44   [01
R > 1000, it is a corner.   ]
[02
]
[01
]
Q3   a   For Oriented FAST and Rotated BRIEF (ORB),   [10]
CO-2;   i) Write the roles of FAST and rBrief.
SO-1;
ii) Find the orientation of the highlighted key point
BL-5
1   1   1   1   1
********** 5 **********
--- page 6 ---
1   10   10   10   1
Image =   1   10   40   10   1
1   10   10   10   1
1   1   1   1   1
iii) List advantages
Ans   i) Fusion of FAST key point detector and rBRIEF descriptor at each   [02
scale   ]
• FAST is used to detect key points of the image pyramid
• Uses rotated BRIEF based on the orientation of each key point
ii) Orientation
x=0 x=1 x=2 x=3 x=4
y=0   1   1   1   1   1
y=1   1   10   10   10   1
y=2   1   10   40   10   1
y=3   1   10   10   10   1
[05
y=4   1   1   1   1   1
]
𝑚00 = ∑𝐼(𝑥, 𝑦) = (16 ∗1) + (8 ∗10) + 40 = 136
𝑥,𝑦
𝑚10 = ∑𝑥 . 𝐼(𝑥, 𝑦)
𝑥,𝑦
𝑚10 = (0 ∗5) + (1 ∗32) + (2 ∗62) + (3 ∗32) + (4 ∗5) = 272
𝑚01 = ∑𝑦 . 𝐼(𝑥, 𝑦)
𝑥,𝑦
𝑚01 = (0 ∗5) + (1 ∗32) + (2 ∗62) + (3 ∗32) + (4 ∗5) = 272
(𝑚01
𝜃= 𝑡𝑎𝑛−1 ( 𝑚00) ) = 𝑡𝑎𝑛−1 (𝑚01 ) = 𝑡𝑎𝑛−1 (272 272) = 45
(𝑚10   𝑚10
𝑚00)
Orientation of key point is 45°
iii) Advantages
•   Fast, therefore suitable for real time applications
• Scale invariant, enabling it to detect features at different scales
within an image
•   Rotation-invariant, can match object even if the object is oriented
• Not patented like SIFT or SURF   [3]
********** 6 **********
--- page 7 ---
Q3   b   For the generation of feature descriptors using Speeded Up Robust   [10]
CO-3;   Features (SURF), list the steps and explain it in brief.
SO-1;
Justify that SURF is faster than SIFT.
BL-3,5
Ans
Detector   [03
1. Construct Hessian matrix using box filters at each pixel and   ]
identify key points
2. Increase the size of box filters and repeat step 1
3. For each key point, select points within radius of 6s, where s is
standard deviation of filter for key point
4. Apply Gaussian filter of 2.5s on key point
5. Use Haar wavelet of size 4s to determine magnitude and direction
of points
6. Draw histogram of orientation for 6 bins to identify orientation of
key point
Descriptor
1. Around each key point, choose points within region of square with   [04
size (20s, 20s)   ]
2. Divide region into 16 sub-regions
3. For each sub-region, determine vector of length 4
4. Length of descriptor vector for region is 64
SIFT
• High dimensionality
• Leads to good accuracy   [03
• Approximates Laplacian of Gaussian with DoG   ]
• Uses determinant and trace of Hessian matrix
SURF
•   It is a speeded-up version of SIFT (Fast and robust algorithm)
• Approximates LoG with Box Filter
• Convolution with box filter using integral images speeds up the
process
• Convolution can be done in parallel for different scales
• Thus enabling real-time applications such as tracking and object
recognition
********** 7 **********
--- page 8 ---
• Uses determinant of Hessian matrix for both scale and location not
trace
Q4   a   Explain the steps involved in the Bag of Visual Words for feature matching.   [10]
CO-3;
Use example images and histograms for the explanation. K-means
SO-1;
BL-5   clustering uses K = 6
Ans.   First image
1. Extract descriptors of first image   [05
• Choose strong key points, N=10   ]
• Determine corresponding descriptors of length 128
2. Apply K-means clustering on descriptors
• Groups similar descriptors
• Generate K groups or clusters, K=5
• Determine Cluster mean, also called cluster centres
•   Set of K clusters is a visual vocabulary
• Length of each cluster center is length of feature descriptor
Second image
1. Extract feature of key points of second image
2. For each key point, find the nearest cluster from K clusters of first
image
3. Assign the nearest cluster of first image to descriptor of the second
image
4. There can be several descriptors of second image which are
assigned a particular cluster of first image
5. Generate Histogram of K visual words for the image
[05] marks for images and histograms
CO-5;   b   Design an appropriate Convolutional Neural Network (CNN) model with   [10]
SO-1;
the following architecture specifications for an input gray image of size
BL-6
64 × 64.
• One convolutional layer with 12 filters, each of size 3×3
• One max pooling layer with pool size (3×3)
• One dropout layer with probability 0.1
• One flatten layer
********** 8 **********
--- page 9 ---
• Three dense (fully connected) layers
• No padding (i.e., "valid" convolution)
•   Stride = 1 for convolution
Tasks:
1. Provide the output shape after each layer.
2. Do not consider bias terms at any layer.
3. Clearly specify activation functions.
Ans.   Possible solution:
Layer   Description   Formula /   Activation Output
Reasoning   Shape
Input   Gray image   64×64×1   —   (64,
64, 1)
Conv2D   12 filters, 3×3, (64 − 3 + 1) = ReLU   (62,
stride 1, valid   62 → 62×62   62, 12)
padding   spatial size
MaxPooling2D pool size =   floor(62 / 3) —   (20,   [05
(3×3), stride = = 20   20, 12)
3   ]
Dropout   rate = 0.1   (no change in —   (20,
shape)   20, 12)
Flatten   Flatten 3D →   20×20×12 = —   (4800,)
1D   4800
Dense 1   128 units   —   ReLU   (128,)
Dense 2   64 units   —   ReLU   (64,)
Dense 3   10 units (e.g., —   Softmax   (10,)   [05
10-class
output)   ]
Q5   a   For Gaussian Mixture Model, explain   [10]
CO-4;   i)   Key feature
SO-1;
ii)   Initialization phase
BL-2
iii)   Matching of pixels with Gaussian curve
Ans.   • Generate mixture of ‘k’ Gaussians distribution models for each
pixel of background frame.
•   Values for ‘k’ is in the range 3 to 5
• Weight of each distribution is proportional to the amount of time
each color/intensity stays on that pixel   [02
•   If a pixel has almost the same intensity for few consecutive   ]
frames. Weight of the Gaussian distribution of the pixel is more.
This pixel is a background pixel
********** 9 **********
--- page 10 ---
•   If weight of Gaussian distribution of a pixel is low, that pixel
classified as a foreground pixel
• Each pixel value of reference/ background frame corresponds to 3
Gaussian mixtures
• Each Gaussian Distribution has different parameters
• Model parameters are updated with each new frame
Initialization
•   Create a Gaussian model for a pixel value at a location in the first
frame, x1   [02
• Use w=1 and μ = x1 and large σ for Gaussian model   ]
Match pixel in the next frame
• Check if Gaussian includes pixel at the same location in the next
frame
•   Pixel value is xt, at = 2 (for the second frame)
• Matching conditions for xt
• Case 1 (matches with at least of one of K Gaussians): update all   [06
matched Gaussian curves   ]
• Case 2 (no match in any Gaussian): create a Gaussian to model xt
{1 𝑖𝑓 ( 𝑥𝑡−𝜇𝑘 𝑡−1) ≤2.5 𝜎𝑘 𝑡−1
𝑀𝑘(𝑥𝑡) =
0   𝑂𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒
•   If xt is satisfying matching condition, Update parameters of all
matched Gaussians to include xt in the matched Gaussian curve
CO-5;   b   In a Single-Shot Detector (SSD), feature maps of sizes 38×38, 19×19,   [10]
SO-1;
10×10, and 5×5 are used for multi-scale detection. Each location predicts
BL-3
4 bounding boxes with 21 class scores.
• Calculate the total number of bounding boxes generated.
• How many total output values (bounding box coordinates + class
scores) are produced for one image?
Ans.   Feature Map 1: 38×38
• Number of locations = 38 × 38 = 1,444
********** 10 **********
--- page 11 ---
• Bounding boxes = 1,444 × 4 = 5,776
Feature Map 2: 19×19
• Number of locations = 19 × 19 = 361
• Bounding boxes = 361 × 4 = 1,444
Feature Map 3: 10×10
• Number of locations = 10 × 10 = 100
• Bounding boxes = 100 × 4 = 400
Feature Map 4: 5×5
• Number of locations = 5 × 5 = 25
• Bounding boxes = 25 × 4 = 100
Total = 5,776 + 1,444 + 400 + 100 = 7,720 bounding boxes   [06
]
Total Output Values (Bounding Box Coordinates + Class Scores)
For each bounding box, the SSD outputs:
• 4 coordinates (x_center, y_center, width, height) or (x_min,
y_min, x_max, y_max)
• 21 class scores (confidences for each of the 21 classes)
Output values per bounding box = 4 + 21 = 25 values
Method 1: Using total bounding boxes
Total output values = Total bounding boxes × (coordinates + class scores)
Total output values = 7,720 × 25 = 193,000 values
[04
]
Q6   a   Give an overview of the U-Net architecture for image segmentation and   [10]
CO-5;   explain the working of its encoder–decoder structure with a neat
SO-1;
schematic diagram.
BL-2
Ans.   Reference:
********** 11 **********
--- page 12 ---
[03
]
• Input image: U-Net starts with a 2D image, such as a medical
scan or a satellite photo. The goal is to assign a class label to every
pixel in the image.   [03
• Downsampling: The image passes through convolutional layers   ]
that learn important visual features. As the image moves through
different layers, its resolution decreases, and the model identifies
broader patterns.
• Bottleneck layer: At the center of the network, the feature maps
reach their smallest spatial resolution while capturing high-level
semantic features. Simply put, this compressed representation of
the feature maps is the overall context of the input.
• Upsampling: The network then reconstructs the image by
gradually increasing the resolution. Transposed convolutions help
expand the feature maps back toward the original size.
• Skip connections: The feature maps from the downsampling path   [04
are concatenated with those in the upsampling path. This helps   ]
preserve fine-grained spatial details while integrating high-level
contextual information.
• The output is a segmentation map: The final output is a pixel-
wise segmentation mask matching the input size. Each pixel is
classified into a category like object, background, or region of
interest.
CO-4;   b   Draw architecture of Mask RCNN and explain it in brief. Justify the use   [10]
SO-1;
of RoI align in Mask RCNN
BL-3
********** 12 **********

[Text in pictures on this page, read by OCR]
128 64 642

Contraction network Expansion network

Output imag

Input image Eases

572x572 x3

256 128
Li
lglg

a 512 256
3x3, ReLU
SS Zz (ts => conv 3x3, Rel

3 Bx
S# 512 512 1024 sin tS &   —coPyand crop

= # max pool 2x2
*
88 SF: 1024 4A & # up-conv 2x2
_aemes—
a = conv 1x1

o

°
--- page 13 ---
Ans.
• A region proposal on image, width = 200 and height = 145
•   Scale factor = 512/16 = 32
• On feature map, width = 200/32= 6.25 and height = 145/32 = 4.53
•   Coordinates of centre on feature map, x = 9.25, y = 6
•   If size and coordinates of the box are quantized
• Some part of ROI is not processed
• Looses data if coordinates are quantized
•   Therefore ROI align is used
RoI align
• For 3×3 pooling, divide ROI into 9 cells
•   Size of each cell (4.53/3 = 1.51) × (6.53/3 = 2.08)
[04
]
********** 13 **********

[Text in pictures on this page, read by OCR]
Mask RCNN

Input Image

CNN (Ex: Resnet)
Shared Feature Map

Region Proposal Network

Region Proposals

ROI Align

FC Layers
Soft =
2 BB regressor Mask head
Classifier - .

Predicted Class Refined Box Mask Coord
--- page 14 ---
[02
]
• Determine equidistant 4 points in each cell
• Apply bilinear interpolation for intensity at each point of the cell
• Apply max pooling in each cell
Q7   a   Explain the steps of Scale-Invariant Feature Transform in brief. Describe   [10]
CO-1;   the generation descriptor after key point localization of SIFT algorithm.
SO-1;
BL-3
Ans.   • Determine histogram for each cell around key point   [05]
• 16 cells and 8 orientations = 16x8 = 128 bins with magnitude of
gradients as bin value
•   Feature vector of each key point contains 128 elements
• Use Gaussian-weighted circular window with σ equals to 1.5 times
the scale of the image at which key point is selected
• Gaussian window is used to give less emphasis to gradients that
are far from the key point
[05]
• 16 cells and 8 orientations 128 values
• SIFT feature vector of each key point contains 128 elements
********** 14 **********
--- page 15 ---
CO-3;   b   Explain Region Proposal Network of Faster RCNN and justify that it   [10]
SO-1;
makes Faster RCNN is faster than Fast RCNN. Illustrate with example
BL-3
images.
Ans.   • Uses Region Proposal Network (RPN) instead of selective search
method   [5]
• RPN generates regions which possibly contain objects
• These proposals are given to ROI pooling
• Use CNN to generate feature map with ‘C’ channels
• Use a window of size n×n (ex: 3×3)
• Output at each location shows whether the region contains an
object or not
• Move the window to capture all parts of image
•
[05
]
•   Usually, scale of 1:1, 1:2, 1:3, 2:1, etc are used for anchor boxes
• Apply 1×1 convolution on window (red region) to generate
features of size 1×1×C
********** 15 **********
--- page 16 ---
•   Feature corresponding to window which covers a part of the object
is useful to guess whether reference boxes contain an object or not
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 7a8b113a3f12

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSE_DS_7011/COMPUTER VISION/ANS_COMPUTER VISION(702EX0E015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER VISION
Date: 05 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions,attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1   Answer briefly   [20]
CO-1   a. A computer vision system for an autonomous vehicle is to be developed.   [04]
SO-2   Which technique (low-level/mid-level/high-level) is preferable for the
BL-2   process:
i.   Detect of the edges of road signs. Justify your answer.
ii.   Understand the meaning of road signs, such as "Stop" or "Left"
or “Right”.
Justify each answer.
Solutio   i. Low-level technique:
n
Use edge detection for identifying the boundaries of the sign. It
works at the pixel level to detect features that help identify basic
structures such as the edges of signs, which can then be used for
higher-level processing. For edge detection, algorithms like Canny
Edge Detection or Sobel Operator are typically used to identify
regions of high intensity changes that represent boundaries or
contours of objects like road signs.
ii. high-level technique:
Involves interpreting more complex structures and semantic
meaning, typically using machine learning or deep learning models
like Convolutional Neural Networks (CNNs). The task of
understanding and classifying road signs is a pattern recognition
problem or train the network
2 Marks each for correct techniques and justification
CO-2   b. Explain the roles of FAST and rBRIEF in the ORB (Oriented FAST and   [04]
SO-3
Rotated BRIEF) feature descriptor.
BL-3
Solutio   FAST is used to detect keypoints (interest points) in an image quickly.
n
********** 1 **********
--- page 2 ---
•   It examines a circle of 16 pixels around a candidate pixel.
•   If a certain number of contiguous pixels in that circle are either
brighter or darker than the central pixel by a threshold, it is
marked as a keypoint.
rBRIEF (Rotated Binary Robust Independent Elementary Features)
• BRIEF creates a descriptor by performing intensity comparisons
between pairs of pixels in a patch around the keypoint.
• The result is a binary string (e.g., 256 bits long).
• ORB rotates the BRIEF descriptor according to the keypoint
orientation computed from FAST.
• This makes rBRIEF rotation-invariant.
2 Marks: At least 2 key points of FAST
2 Marks: At least 2 key points of rBrief
CO-2   c.   For Brute Force Matcher   [04]
SO-2   (i)   Given the following feature descriptors:
BL-3   𝐷1 = [1,2,3], 𝐷2 = [2,2,3],𝐷3 = [0,1,1]
Query descriptor, 𝑄= [1,2,2]
Use Brute Force Matcher to identify the descriptor which is the
best match for query descriptor. Use Euclidean distance.
(ii)   What is the main limitation Brute Force Matcher? Prove it with
an example.
Solutio   i) Euclidean distances:
n   𝑑(𝑄, 𝐷1) = √(1 −1)2 + (2 −2)2 + (2 −3)2 = √1 = 1
𝑑(𝑄, 𝐷2) = √(1 −2)2 + (2 −2)2 + (2 −3)2 = √1 + 0 + 1 = √2
≈1.414
𝑑(𝑄, 𝐷3) = √(1 −0)2 + (2 −1)2 + (2 −1)2 = √1 + 1 + 1 = √3
≈1.732
Best match: 𝐷1(minimum distance = 1)
ii) Limitation: Computationally expensive for large datasets; slow for
high-dimensional descriptors. Requires computations of 100
Euclidean distances. Each distance requires 128 subtractions, 128
multiplications and one square root.
2 Marks: Calculation of best match
2 Marks: limitations
CO-2   d.   For K-means clustering,   [04]
SO-1   i)   Explain two limitations with examples
BL-3   ii) Perform one iteration of K-Means clustering for the pixel intensity
for the set, X = [10,12,15,70,75,80],  k=2
Assume initial means μ₁ = 12, μ₂ = 75
Solution   i) Limitations
• Need to choose the value of K
• Converges to a local minimum of WCSS
•   Sensitive to initialization of centroid
********** 2 **********
--- page 3 ---
•   It is sensitive to rescaling
•   Sensitive to outliers
• Segments “spherical” clusters, does not work if clusters have a
complex geometric shape
ii) Clusters
Cluster1 → [10, 12, 15], mean = 12.33
Cluster2 → [70, 75, 80], mean = 75.0
New means: μ₁ = 12.33, μ₂ = 75.0
2 Marks: limitations
2 Marks: computation
CO-4   e. An input image of size 33×33 is passed through a convolutional layer   [04]
SO-5   followed by a Max pooling layer.
BL-4
Convolution Layer
•   filter size = 5×5,
•   stride = 1,
• padding = 2,
• number of filters = 10
• ReLU activation
Max-pooling layer
• Filter size = 2 × 2
• Stride = 2
Calculate
i) Output dimensions after the convolution layer
ii) Output dimensions after the pooling layer
Solutio   i) Output width and height is [(33-5+ 2(1))/2]+1 = 16
n
Output of convolution layer: 16×15×10
ii) Output of max pooling layer: [(16-2)/2]+1 = 8
Output of max pooling layer: 8×8×10
2 Marks: Convolution layer
2 Marks: Max pooling layer
Q2   a   For Histogram of Gradients descriptor, describe each step in brief.
CO-2   [10]
SO-1
BL-2
Solutio   1. Divide patch by cells of 8 ⨯ 8 pixels
n   2. Compute the gradients for pixels in the patch (localized
portion)
3. Construct histograms using the computed gradients (magnitude
and orientation) for each cell. Consider 9-bin histogram. For
image size of 64x128,
• 128 cells are available (8x16 = 128 cells)
• For each cell, there are 64 pixels
********** 3 **********
--- page 4 ---
• 64 pixels have 64 magnitudes and 64 directions
(64+64=128 values)
• Map 128 values into a 9-bin histogram
• Histogram provides a useful and compact representation of
gradients
4. Apply normalization with neighboring histograms. Normalize
histogram over a 16×16 pixels/block.
• Each block contains 4 cells ( 1 histogram/ cell)
• Each block has 4 histograms (9 values/ histogram)
• Concatenate 4 histograms to form a 36 x 1 element vector
for a block
• Normalize the vector
5. Concatenate all histograms to form a vector
10 Marks: 2 Marks each for detailed description
Q2   b   Determine corner response for the following image using Harris Corner   [10]
CO-2   response. Use window of size 3×3. Filters for the determining gradients
SO-2
are given below. Test whether pixel at the center is a corner or not.
BL-3
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
Solutio
n   0   0   0   40   40   40
0   0   0   40   40   40
0   0   0   0   0   0
Ix   Iy
********** 4 **********
--- page 5 ---
0   0   0   160 160 160
0   0   0   0   0   0
0   0   0   160 160 160
0   0   0
0   0   0
I2x   I2y
0   0   0
0   0   0
0   0   0
IxIy
𝐼𝑥 2   𝐼𝑥𝐼𝑦
𝑀= ∑𝑤(𝑥, 𝑦) [   2 ]
𝐼𝑥𝐼𝑦   𝐼𝑦
𝑥,𝑦
𝑀= [0   0
0 9600]
Determinant of M
= 9600
Trace of M
= 9600
R = det{M} – k (trace {M})2
• R =9600-0.04(9600)(9600) = 3676800
• For threshold = 3000000
• R is negative. Therefore, point at the center of window is not a
corner point.
5 Marks: Construction of matrices
4 Marks: Computation of corner response
1 Mark: point is not a corner point
Q3   a   For SIFT (Scale-Invariant Feature Transform) algorithm and briefly   [10]
CO-2   describe the role of each step in 2-3 sentences. Explain key point
SO-4
localization in details.
BL-3
********** 5 **********
--- page 6 ---
Solutio
n
• Each pixel is compared with 26 other pixel values
•   Pixel marked x is compared with 26 other pixel values
•   If it is the highest positive or lowest negative among 26
neighbors (maxima or minima)
•   It is selected as a potential keypoint
•   Discard weak key points
• Normalize DoGs to get values in 0 -1 range
•   Set threshold to 0.03
• For DOG(x), x is coordinates of extrema (minima/maxima)
•   If DOG(x) < Threshold, discard it
********** 6 **********
--- page 7 ---
•   Else retain it
Construct Hessian matrix at each potential keypoint to check whether
these points are good corner points not edge points.
∑[𝐼𝑥𝑥   𝐼𝑥𝑦
𝐻=   𝐼𝑥𝑦   𝐼𝑦𝑦]
Ixx and Iyy are second order derivative in x and y directions
Ixy is first order derivative in x direction and then in y direction
•   Select key point if
𝑡𝑟𝑎𝑐𝑒2(𝐻)   (𝑟+ 1)2
<
𝑑𝑒𝑡𝑒𝑟𝑚𝑖𝑛𝑎𝑛𝑡(𝐻)   𝑟
• For SIFT, r = 10
•   Trace2(H)/Determinant(H) < 12.1
4 Marks: steps and description
6 Marks: Description of key point localization with images
Q3   b   Consider the following image.   [10]
CO-2   i) Construct integral image.
SO-4
ii) Apply the given filter and calculate the output at the center of
BL-3, 4
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
********** 7 **********
--- page 8 ---
Solutio   Integral image
n   0   0   0   0   0   1   2   3   4
0   0   0   0   0   2   4   6   8
0   0   0   0   0   3   6   9   12
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
Output = -2(8-6-0+0)+(6-0-0+0)+(8-8-0+0)
= -4 + 6 = 2
SURF
• Approximates LoG with Box Filter
• Convolution with box filter using integral images speeds up the
process
• Convolution can be done in parallel for different scales
• Thus enabling real-time applications such as tracking and
object recognition
• Uses determinant of Hessian matrix for both scale and location
not trace
4 Marks: Integral image
3 marks: Filtered outputs
3 marks: points to justify that SURF is fast
Q4   a   Develop an image retrieval system for a large dataset of natural images   [10]
(forests, mountains, rivers).
CO-2
(i) Explain how Bag of Visual Words (BoVW) represents each image
SO-2
and discuss how clustering of descriptors helps in constructing the
BL-3
visual vocabulary
(ii) Describe one limitation of BoVW in object recognition.
(iii) SIFT descriptors from three images (each descriptor is 2D for
simplicity) are given below. Construct BoVW histogram for each
image. Consider cluster centres as μ₁ = (2,2), μ₂ = (8,8).
Image   Descriptor1,   Descriptor2,   Descriptor3, D3
D1   D2
I1   (1,2)   (2,1)   (3,2)
I2   (8,8)   (9,9)   (8,9)
I3   (1,1)   (2,2)   (2,1)
Solutio   BoVW treats an image as a “bag” of local features, ignoring spatial
arrangement.
n
•   Steps:
1. Extract local descriptors (SIFT, ORB) from keypoints.
********** 8 **********
--- page 9 ---
2. Cluster all descriptors from dataset using k-means →
visual vocabulary.
3. Represent each image as a histogram of visual words
(count of descriptors assigned to each cluster).
•   Limitation: Spatial information is lost → may fail for objects
where shape matters.
Step 1 – Assign descriptors to clusters using Euclidean distance
•   μ₁ = (2,2), μ₂ = (8,8)
Image I1 descriptors: (1,2),(2,1),(3,2)
•   d((1,2), μ₁) = √((1−2)² + (2−2)²)=1 → cluster 1
•   d((1,2), μ₂) = √((1−8)² + (2−8)²)=√(49+36)=√85≈9.22 →
cluster 2
→ Assigned to μ₁
•   d((2,1), μ₁) = √((2−2)²+(1−2)²)=1 → cluster 1
•   d((3,2), μ₁) = √((3−2)²+(2−2)²)=1 → cluster 1
I1 histogram: [3,0]
Image I2 descriptors: (8,8),(9,9),(8,9)
•   All distances closer to μ₂ → cluster 2
I2 histogram: [0,3]
Image I3 descriptors: (1,1),(2,2),(2,1)
•   d((1,1), μ₁)=√2≈1.41 → cluster 1
•   d((2,2), μ₁)=0 → cluster 1
•   d((2,1), μ₁)=1 → cluster 1
I3 histogram: [3,0]
Step 2 – Final BoVW Histograms:
Image   Cluster 1   Cluster 2
I1   3   0
I2   0   3
I3   3   0
4 Marks: Description
6 marks: computation of histogram, 2 marks for each image
Q4b   For image matching using Image Pyramid,   [10]
(i) Explain the technique for image matching using Earth Mover’s
CO-2
Distance (EMD).
SO-1
(ii) Write one practical application of pyramids in image processing
BL-3,4
or object detection.
(iii) Given   normalized   histograms   representing   intensity
distributions of two images, Compute the distance between H₁
and H₂ using EMD
𝐻1 = [0.0, 0.2,0.5,0.3],𝐻2 = [0.0,0.0,0.1,0.9]
(iv) Repeat the same for two other images with the following
histograms and interpret the similarity between them.
𝐻1 = [0.0, 0.2,0.5,0.3],𝐻2 = [0.0,0.4,0.4,0.2]
v) Which pair of the histograms is more similar than other
Solutio   i) Image Pyramid: Multi-scale representation of an image
n
********** 9 **********
--- page 10 ---
•   consists of a sequence of images at progressively lower
resolutions. Is a way to measure difference between two
histograms
•   Based on the minimum cost required to turn one histogram into
the other
•   Consider that each histogram bin as a pile of earth (mass)
located at a certain position
•   To transform one histogram (earth) into another, move the
earth so that the two histograms match
•   The cost of moving earth depends on
• How much mass is moved
• How far it is moved
(ii)   Applications:
o Object detection at multiple scales (e.g., face detection).
o Image blending and compression.
o Multi-scale feature extraction.
(iii)   Compute cumulative sums (CDFs)
Bin Cum(H₁) Cum(H₂) Difference
0   0.0   0.0   0.0
1   0.2   0.0   0.2
2   0.7   0.1   0.6
3   1.0   1.0   0.0
EMD = Average cumulative difference
𝐸𝑀𝐷= (0.0 + 0.2 + 0.6 + 0)/4 = 0.2
EMD is small. Histograms are similar.
vi) Compute cumulative sums (CDFs)
Bin Cum(H₁) Cum(H₂) Difference
0   0.0   0.0   0.0
1   0.2   0.4   0.2
2   0.7   0.8   0.1
3   1.0   1.0   0.0
𝐸𝑀𝐷= (0.0 + 0.2 + 0.1 + 0.0)/4 = 0.075
v) Most similar pair
𝐻1 = [0.0, 0.2,0.5,0.3], 𝐻2 = [0.0, 0.4,0.4,0.2]
3 Marks: description
2 Marks: application
4 Marks: Computation
1 Mark: similar pair
********** 10 **********
--- page 11 ---
Q5   a   Describe how Gaussian Mixture Model (GMM) is generated to   [10]
construct background frame. A pixel intensity is modeled with a 3-
CO-2
component (K=3)
SO-4
BL-3
Gaussian   Μ   σ   w
Curve
1   100   5   0.5
2   120   7   0.3
3   150   10   0.2
A new pixel intensity is x = 118. Test whether it belongs to
background or foreground.
Solutio   • Generate mixture of ‘k’ Gaussians distribution models for each
n   pixel of background frame
•   Values for ‘k’ is in the range 3 to 5
• Weight of each distribution is proportional to the amount of
time each color/intensity stays on that pixel
•   If a pixel has almost the same intensity for few consecutive
frames
• Weight of the Gaussian distribution of the pixel is more
• This pixel is a background pixel
•   If weight of Gaussian distribution of a pixel is low, that pixel
classified as a foreground pixel
• Each pixel value of reference/ background frame corresponds
to 3 Gaussian mixtures
• Each Gaussian Distribution has different parameters
• Model parameters are updated with each new frame
( 𝑥𝑡−𝜇𝑘 𝑡−1) ≤2.5 𝜎𝑘 𝑡−1
Distance from curve 1= 180-100 =80 and 2.5×5 =12.5, 80>12.5
Distance from curve 2= 180-120 =60 and 2.5×7 =17.5, 60>17.5
Distance from curve 3= 180-150 =30 and 2.5×10 =25, 30>25
Pixel at 180 does not belong to any curve. Therefore, it is a foreground
pixel.
6 Marks: description
3 Marks: computation for each curve
1Mark: Pixel is foreground
Q5   b   For Mean Shift algorithm,   [10]
CO-2   (i) Explain advantages and limitations of Mean Shift algorithm with
SO-1   suitable examples.
BL-3
********** 11 **********
--- page 12 ---
(ii) Predict the effect of increasing the space bandwidth, hs on
clustering the samples. Explain with examples
Solutio   Bandwidth (Radius) Parameter:
n   • Bandwidth is a crucial parameter that controls the radius of the
window
•   It affects the scale of the clusters
• Small bandwidth: More clusters, finer segmentation
• Large bandwidth: Fewer clusters, coarser segmentation
•   Selecting the optimal bandwidth is important for the quality of
segmentation
•   Larger the widow size is, the closer the local mean point is to
the global mean
• Large region can ignore the local structure of the dataset
• Mean value is calculated for a small local area
•   If small bandwidth is used, several noisy clusters can appear
Advantages
• Finds number of modes (clusters) depending on the data values
• Robust to noise or outliers
• Mean is dependent on the regions of high density
• Avoid the influence of noise in the image
• Does not assume any prior shape (like spherical, elliptical, etc.)
of data clusters
Limitations:
• Clustering depends on the choice of window size (bandwidth)
which can lead to under or over segmentation
• Computationally more expensive than K-means
• Slow, especially for high-resolution images
• Can identify noisy pixel as clusters
• Finds arbitrary number of clusters
5 Marks: Effect of bandwidth
5 Marks: advantages and limitations
Q6   a   For 2D images,   [10]
CO-3
(i) Explain image transformations using scaling, rotation, flipping,
SO-4
and shearing, with their effects on images and general
BL-3,4
mathematical forms.
********** 12 **********
--- page 13 ---
(ii) A point P(3, 2) is transformed using the following 2×2
transformation matrix:
𝑇= [2 1
0 1]
Calculate the new coordinates of the point after transformation
(iii)   If P(3,2) is transformed with scaling in x direction by 2 and in Y
direction by 1, followed by horizontal shear factor of 1.
Determine the new coordinates of the point after transformation.
Comment on the transformations in (ii) and (iii).
Solutio   Image Transformations
n   Scaling - resize image
[𝑥2 = [𝑎 0 [𝑥1
𝑦2]   0 𝑏] 𝑦1]
𝑆 = [𝑎 0
0 𝑏]
Rotation
[𝑥2 𝑦2] = 𝑅[𝑥1 𝑦1]   [𝑥2 = [cos⁡(𝜃) −sin⁡(𝜃) ] [𝑥1
𝑦2]   sin⁡(𝜃)   cos⁡(𝜃)   𝑦1]
Flipping -
About Y-axis
[𝑥2 = [−1 0 [𝑥1
𝑦2]   0   1] 𝑦1]
About X-axis
[𝑥2 = [1 0 [𝑥1
𝑦2]   0 −1] 𝑦1]
Image Transformations
Scaling - resize image
[𝑥2 = [𝑎 0 [𝑥1
𝑦2]   0 𝑏] 𝑦1]
𝑆 = [𝑎 0
0 𝑏]
Rotation
[𝑥2 𝑦2] ********** = [cos⁡(𝜃) 13 ********** −sin⁡(𝜃) ] [𝑥1 𝑦1]
sin⁡(𝜃)   cos⁡(𝜃)
--- page 14 ---
[𝑥2 = 𝑅[𝑥1
𝑦2]   𝑦1]
Flipping -
About Y-axis
[𝑥2 = [−1 0 [𝑥1
𝑦2]   0   1] 𝑦1]
About X-axis
[𝑥2 = [1 0 [𝑥1
𝑦2]   0 −1] 𝑦1]
Shearing –
Vertical Shear
[𝑥2   1   0 [𝑥1
𝑦2] = [ 𝑚𝑦 1] 𝑦1]
Horizontal Shear
[𝑥2 = [1 𝑚𝑥 ] [𝑥1
𝑦2]   0   1   𝑦1]
(ii)
[𝑥2 = [2 1 [3 = [8
𝑦2]   0 1] 2]   2]
1 Marks for calculation
(iii)   [𝑥2 𝑦2] = [2 0 1] [3 2] = [6 2] after scaling
0
[𝑥2 = [1 1 [6 = [8
𝑦2]   0 1] 2]   2]
********** 14 **********
--- page 15 ---
Transformations in (ii) and (iii) are same.
6 Marks (1.5 M for each transformation)
2 Marks for calculation and 1M for comment
Q6   b   In relation to stereo vision, explain in brief   [10]
CO-3   (i)   Determination of depth
SO-1
Epipolar geometry
BL-3
Solutio   (i)   For each interest point, (ex: point x) in the first image
n   • Determine corresponding epipolar line in the right image
• Search probable corresponding interest points on epipolar line
• Pick the best match at x’ (use Euclidian distance)
• Disparity = x-x’
• Depth(x) = K/(x-x’), K is dependent on camera matrix
(ii)
•   First camera is mapped with the second camera by a rotation R
• And then by a translation T
•   Location of corresponding points (x and x’) can be found using
Essential Matrix (E) and Fundamental Matrix (F)
• Goal is to determine E and F matrices
********** 15 **********

[Text in pictures on this page, read by OCR]
* Standard epipolar geometry setup involves two cameras observing the same 3D
point P

* Cameras are located at O, and O,

* Projection of point, P, on the image planes is located at p and p’ respectively

epipolar plane Image planes

epipolar line for p

epipolar line for p’

baseline
--- page 16 ---
5 Marks: Depth calculation
5 Marks: Epipolar geometry
Q7   a   Draw architecture of RCNN and explain each layer/block in 2-3 [10]
CO- 4   sentences in brief.
SO-5
BL-3
Solutio
n
1. Generate 2,000 region proposals using the Selective
Search algorithm
2. Input each region proposal into CNN
3. Extract a feature vector of length, 4096 from each region
proposal from CNN
4. Use a pre-trained SVM algorithm to classify the region
proposal to either the background or one of the object classes
5. Refine bounding box predictions using bounding box
regression
Selective search:
• Segment the image into regions
• Regions have similarity in color, texture or any other parameter
********** 16 **********

[Text in pictures on this page, read by OCR]
Input Image

Selective Search
2000 region Proposals

Warp and resize to
224x224

CNN (Ex: Alexnet)

Feature Vector

SS

SVM Classifier BB regressor

Predict Class Refined Box
--- page 17 ---
• Use graph segmentation to capture the regions
• Merge regions into larger regions iteratively
• Merged regions are called region proposals
Warp
• Each region proposal is given as input to CNN
• CNN is used to extract features of region proposal
•   If Alexnet is used, image size should be 227×227
CNN
•   Train Alexnet using a large data set for image classification
• Or use any trained CNN for classification
• Replace last layer which is classification layer (soft max)
SVM
• Binary SVM classifier uses 4096 features to classify each
object
• For ‘n’ number of classes, ‘n’ binary SVMs are used
Bounding box regressor
•   Select region proposals with IOU > 0.5 with any of ground
truth boxes
• Other proposals are background proposals
4 Marks: block diagram
6 Marks: description
Q7b   b   Illustrate ‘Divide and Conquer’ approach for YOLO. Justify that YOLO   [10]
CO-4   speeds up the process of object detection
SO-5
BL-4
Solutio   YOLO is fast
n   • YOLO implements one-stage object detection, making object
detection a single regression task.
• A single neural network of YOLO predicts bounding boxes and
class probabilities from the complete image in one forward
pass (single-step).
•   It significantly increases the speed of operation in YOLO.
YOLO works on the principle of divide and conquer.
YOLO divides the input image into an S × S grid.
Each grid cell is responsible for detecting objects whose center falls
within it.
********** 17 **********
--- page 18 ---
Each cell predicts B bounding boxes and C conditional class
probabilities.
Pr⁡(𝐶𝑙𝑎𝑠𝑠𝑖 | 𝑂𝑏𝑗𝑒𝑐𝑡)
Each bounding box consists of 5 predictions: x, y, w, h, confidence.
x, y → center of box relative to bounds of grid cell
w, h → relative to whole image
Confidence → Pr⁡(𝑂𝑏𝑗𝑒𝑐𝑡) × 𝐼𝑜𝑈 between the predicted box and the
ground truth
These predictions are encoded as S × S × (𝐵× 5 + 𝐶) tensor.
• In the original YOLO paper, the authors used the PASCAL VOC
dataset, which contains 20 classes (C = 20), a grid of 7 × 7 (S =
7), and at most 2 classes per grid element (B = 2), giving a 7 ×
7 × 30 output prediction.
• Figure shows a simplified output vector considering a three-by-
three grid, three classes, and a single class per grid for eight
values. In this simplified case, the output of YOLO would be 3
× 3 × 8.
• YOLOv1 achieved an average precision (AP) of 63.4 on the
PASCAL VOC2007 dataset. These predictions are encoded as
S × S × (𝐵× 5 + 𝐶) tensor.
3 Marks: Justification for speed
7 Marks: divide and conquer approach
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 08aca7563ef5

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/BTech_CSE_DS_7057/COMPUTER VISION/ANS_COMPUTER VISION(702EX0E015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Feb 2026
- Text: text (18 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. TECH (CSE - DS)/B. Tech (CSE - DS) (311)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER VISION
Date: 05 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 18 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions,attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1   Answer briefly   [20]
CO-1   a. A computer vision system for an autonomous vehicle is to be developed.   [04]
SO-2   Which technique (low-level/mid-level/high-level) is preferable for the
BL-2   process:
i.   Detect of the edges of road signs. Justify your answer.
ii.   Understand the meaning of road signs, such as "Stop" or "Left"
or “Right”.
Justify each answer.
Solutio   i. Low-level technique:
n
Use edge detection for identifying the boundaries of the sign. It
works at the pixel level to detect features that help identify basic
structures such as the edges of signs, which can then be used for
higher-level processing. For edge detection, algorithms like Canny
Edge Detection or Sobel Operator are typically used to identify
regions of high intensity changes that represent boundaries or
contours of objects like road signs.
ii. high-level technique:
Involves interpreting more complex structures and semantic
meaning, typically using machine learning or deep learning models
like Convolutional Neural Networks (CNNs). The task of
understanding and classifying road signs is a pattern recognition
problem or train the network
2 Marks each for correct techniques and justification
CO-2   b. Explain the roles of FAST and rBRIEF in the ORB (Oriented FAST and   [04]
SO-3
Rotated BRIEF) feature descriptor.
BL-3
Solutio   FAST is used to detect keypoints (interest points) in an image quickly.
n
********** 1 **********
--- page 2 ---
•   It examines a circle of 16 pixels around a candidate pixel.
•   If a certain number of contiguous pixels in that circle are either
brighter or darker than the central pixel by a threshold, it is
marked as a keypoint.
rBRIEF (Rotated Binary Robust Independent Elementary Features)
• BRIEF creates a descriptor by performing intensity comparisons
between pairs of pixels in a patch around the keypoint.
• The result is a binary string (e.g., 256 bits long).
• ORB rotates the BRIEF descriptor according to the keypoint
orientation computed from FAST.
• This makes rBRIEF rotation-invariant.
2 Marks: At least 2 key points of FAST
2 Marks: At least 2 key points of rBrief
CO-2   c.   For Brute Force Matcher   [04]
SO-2   (i)   Given the following feature descriptors:
BL-3   𝐷1 = [1,2,3], 𝐷2 = [2,2,3],𝐷3 = [0,1,1]
Query descriptor, 𝑄= [1,2,2]
Use Brute Force Matcher to identify the descriptor which is the
best match for query descriptor. Use Euclidean distance.
(ii)   What is the main limitation Brute Force Matcher? Prove it with
an example.
Solutio   i) Euclidean distances:
n   𝑑(𝑄, 𝐷1) = √(1 −1)2 + (2 −2)2 + (2 −3)2 = √1 = 1
𝑑(𝑄, 𝐷2) = √(1 −2)2 + (2 −2)2 + (2 −3)2 = √1 + 0 + 1 = √2
≈1.414
𝑑(𝑄, 𝐷3) = √(1 −0)2 + (2 −1)2 + (2 −1)2 = √1 + 1 + 1 = √3
≈1.732
Best match: 𝐷1(minimum distance = 1)
ii) Limitation: Computationally expensive for large datasets; slow for
high-dimensional descriptors. Requires computations of 100
Euclidean distances. Each distance requires 128 subtractions, 128
multiplications and one square root.
2 Marks: Calculation of best match
2 Marks: limitations
CO-2   d.   For K-means clustering,   [04]
SO-1   i)   Explain two limitations with examples
BL-3   ii) Perform one iteration of K-Means clustering for the pixel intensity
for the set, X = [10,12,15,70,75,80],  k=2
Assume initial means μ₁ = 12, μ₂ = 75
Solution   i) Limitations
• Need to choose the value of K
• Converges to a local minimum of WCSS
•   Sensitive to initialization of centroid
********** 2 **********
--- page 3 ---
•   It is sensitive to rescaling
•   Sensitive to outliers
• Segments “spherical” clusters, does not work if clusters have a
complex geometric shape
ii) Clusters
Cluster1 → [10, 12, 15], mean = 12.33
Cluster2 → [70, 75, 80], mean = 75.0
New means: μ₁ = 12.33, μ₂ = 75.0
2 Marks: limitations
2 Marks: computation
CO-4   e. An input image of size 33×33 is passed through a convolutional layer   [04]
SO-5   followed by a Max pooling layer.
BL-4
Convolution Layer
•   filter size = 5×5,
•   stride = 1,
• padding = 2,
• number of filters = 10
• ReLU activation
Max-pooling layer
• Filter size = 2 × 2
• Stride = 2
Calculate
i) Output dimensions after the convolution layer
ii) Output dimensions after the pooling layer
Solutio   i) Output width and height is [(33-5+ 2(1))/2]+1 = 16
n
Output of convolution layer: 16×15×10
ii) Output of max pooling layer: [(16-2)/2]+1 = 8
Output of max pooling layer: 8×8×10
2 Marks: Convolution layer
2 Marks: Max pooling layer
Q2   a   For Histogram of Gradients descriptor, describe each step in brief.
CO-2   [10]
SO-1
BL-2
Solutio   1. Divide patch by cells of 8 ⨯ 8 pixels
n   2. Compute the gradients for pixels in the patch (localized
portion)
3. Construct histograms using the computed gradients (magnitude
and orientation) for each cell. Consider 9-bin histogram. For
image size of 64x128,
• 128 cells are available (8x16 = 128 cells)
• For each cell, there are 64 pixels
********** 3 **********
--- page 4 ---
• 64 pixels have 64 magnitudes and 64 directions
(64+64=128 values)
• Map 128 values into a 9-bin histogram
• Histogram provides a useful and compact representation of
gradients
4. Apply normalization with neighboring histograms. Normalize
histogram over a 16×16 pixels/block.
• Each block contains 4 cells ( 1 histogram/ cell)
• Each block has 4 histograms (9 values/ histogram)
• Concatenate 4 histograms to form a 36 x 1 element vector
for a block
• Normalize the vector
5. Concatenate all histograms to form a vector
10 Marks: 2 Marks each for detailed description
Q2   b   Determine corner response for the following image using Harris Corner   [10]
CO-2   response. Use window of size 3×3. Filters for the determining gradients
SO-2
are given below. Test whether pixel at the center is a corner or not.
BL-3
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
Solutio
n   0   0   0   40   40   40
0   0   0   40   40   40
0   0   0   0   0   0
Ix   Iy
********** 4 **********
--- page 5 ---
0   0   0   160 160 160
0   0   0   0   0   0
0   0   0   160 160 160
0   0   0
0   0   0
I2x   I2y
0   0   0
0   0   0
0   0   0
IxIy
𝐼𝑥 2   𝐼𝑥𝐼𝑦
𝑀= ∑𝑤(𝑥, 𝑦) [   2 ]
𝐼𝑥𝐼𝑦   𝐼𝑦
𝑥,𝑦
𝑀= [0   0
0 9600]
Determinant of M
= 9600
Trace of M
= 9600
R = det{M} – k (trace {M})2
• R =9600-0.04(9600)(9600) = 3676800
• For threshold = 3000000
• R is negative. Therefore, point at the center of window is not a
corner point.
5 Marks: Construction of matrices
4 Marks: Computation of corner response
1 Mark: point is not a corner point
Q3   a   For SIFT (Scale-Invariant Feature Transform) algorithm and briefly   [10]
CO-2   describe the role of each step in 2-3 sentences. Explain key point
SO-4
localization in details.
BL-3
********** 5 **********
--- page 6 ---
Solutio
n
• Each pixel is compared with 26 other pixel values
•   Pixel marked x is compared with 26 other pixel values
•   If it is the highest positive or lowest negative among 26
neighbors (maxima or minima)
•   It is selected as a potential keypoint
•   Discard weak key points
• Normalize DoGs to get values in 0 -1 range
•   Set threshold to 0.03
• For DOG(x), x is coordinates of extrema (minima/maxima)
•   If DOG(x) < Threshold, discard it
********** 6 **********
--- page 7 ---
•   Else retain it
Construct Hessian matrix at each potential keypoint to check whether
these points are good corner points not edge points.
∑[𝐼𝑥𝑥   𝐼𝑥𝑦
𝐻=   𝐼𝑥𝑦   𝐼𝑦𝑦]
Ixx and Iyy are second order derivative in x and y directions
Ixy is first order derivative in x direction and then in y direction
•   Select key point if
𝑡𝑟𝑎𝑐𝑒2(𝐻)   (𝑟+ 1)2
<
𝑑𝑒𝑡𝑒𝑟𝑚𝑖𝑛𝑎𝑛𝑡(𝐻)   𝑟
• For SIFT, r = 10
•   Trace2(H)/Determinant(H) < 12.1
4 Marks: steps and description
6 Marks: Description of key point localization with images
Q3   b   Consider the following image.   [10]
CO-2   i) Construct integral image.
SO-4
ii) Apply the given filter and calculate the output at the center of
BL-3, 4
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
********** 7 **********
--- page 8 ---
Solutio   Integral image
n   0   0   0   0   0   1   2   3   4
0   0   0   0   0   2   4   6   8
0   0   0   0   0   3   6   9   12
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
0   0   0   0   0   4   8   12   16
Output = -2(8-6-0+0)+(6-0-0+0)+(8-8-0+0)
= -4 + 6 = 2
SURF
• Approximates LoG with Box Filter
• Convolution with box filter using integral images speeds up the
process
• Convolution can be done in parallel for different scales
• Thus enabling real-time applications such as tracking and
object recognition
• Uses determinant of Hessian matrix for both scale and location
not trace
4 Marks: Integral image
3 marks: Filtered outputs
3 marks: points to justify that SURF is fast
Q4   a   Develop an image retrieval system for a large dataset of natural images   [10]
(forests, mountains, rivers).
CO-2
(i) Explain how Bag of Visual Words (BoVW) represents each image
SO-2
and discuss how clustering of descriptors helps in constructing the
BL-3
visual vocabulary
(ii) Describe one limitation of BoVW in object recognition.
(iii) SIFT descriptors from three images (each descriptor is 2D for
simplicity) are given below. Construct BoVW histogram for each
image. Consider cluster centres as μ₁ = (2,2), μ₂ = (8,8).
Image   Descriptor1,   Descriptor2,   Descriptor3, D3
D1   D2
I1   (1,2)   (2,1)   (3,2)
I2   (8,8)   (9,9)   (8,9)
I3   (1,1)   (2,2)   (2,1)
Solutio   BoVW treats an image as a “bag” of local features, ignoring spatial
arrangement.
n
•   Steps:
1. Extract local descriptors (SIFT, ORB) from keypoints.
********** 8 **********
--- page 9 ---
2. Cluster all descriptors from dataset using k-means →
visual vocabulary.
3. Represent each image as a histogram of visual words
(count of descriptors assigned to each cluster).
•   Limitation: Spatial information is lost → may fail for objects
where shape matters.
Step 1 – Assign descriptors to clusters using Euclidean distance
•   μ₁ = (2,2), μ₂ = (8,8)
Image I1 descriptors: (1,2),(2,1),(3,2)
•   d((1,2), μ₁) = √((1−2)² + (2−2)²)=1 → cluster 1
•   d((1,2), μ₂) = √((1−8)² + (2−8)²)=√(49+36)=√85≈9.22 →
cluster 2
→ Assigned to μ₁
•   d((2,1), μ₁) = √((2−2)²+(1−2)²)=1 → cluster 1
•   d((3,2), μ₁) = √((3−2)²+(2−2)²)=1 → cluster 1
I1 histogram: [3,0]
Image I2 descriptors: (8,8),(9,9),(8,9)
•   All distances closer to μ₂ → cluster 2
I2 histogram: [0,3]
Image I3 descriptors: (1,1),(2,2),(2,1)
•   d((1,1), μ₁)=√2≈1.41 → cluster 1
•   d((2,2), μ₁)=0 → cluster 1
•   d((2,1), μ₁)=1 → cluster 1
I3 histogram: [3,0]
Step 2 – Final BoVW Histograms:
Image   Cluster 1   Cluster 2
I1   3   0
I2   0   3
I3   3   0
4 Marks: Description
6 marks: computation of histogram, 2 marks for each image
Q4b   For image matching using Image Pyramid,   [10]
(i) Explain the technique for image matching using Earth Mover’s
CO-2
Distance (EMD).
SO-1
(ii) Write one practical application of pyramids in image processing
BL-3,4
or object detection.
(iii) Given   normalized   histograms   representing   intensity
distributions of two images, Compute the distance between H₁
and H₂ using EMD
𝐻1 = [0.0, 0.2,0.5,0.3],𝐻2 = [0.0,0.0,0.1,0.9]
(iv) Repeat the same for two other images with the following
histograms and interpret the similarity between them.
𝐻1 = [0.0, 0.2,0.5,0.3],𝐻2 = [0.0,0.4,0.4,0.2]
v) Which pair of the histograms is more similar than other
Solutio   i) Image Pyramid: Multi-scale representation of an image
n
********** 9 **********
--- page 10 ---
•   consists of a sequence of images at progressively lower
resolutions. Is a way to measure difference between two
histograms
•   Based on the minimum cost required to turn one histogram into
the other
•   Consider that each histogram bin as a pile of earth (mass)
located at a certain position
•   To transform one histogram (earth) into another, move the
earth so that the two histograms match
•   The cost of moving earth depends on
• How much mass is moved
• How far it is moved
(ii)   Applications:
o Object detection at multiple scales (e.g., face detection).
o Image blending and compression.
o Multi-scale feature extraction.
(iii)   Compute cumulative sums (CDFs)
Bin Cum(H₁) Cum(H₂) Difference
0   0.0   0.0   0.0
1   0.2   0.0   0.2
2   0.7   0.1   0.6
3   1.0   1.0   0.0
EMD = Average cumulative difference
𝐸𝑀𝐷= (0.0 + 0.2 + 0.6 + 0)/4 = 0.2
EMD is small. Histograms are similar.
vi) Compute cumulative sums (CDFs)
Bin Cum(H₁) Cum(H₂) Difference
0   0.0   0.0   0.0
1   0.2   0.4   0.2
2   0.7   0.8   0.1
3   1.0   1.0   0.0
𝐸𝑀𝐷= (0.0 + 0.2 + 0.1 + 0.0)/4 = 0.075
v) Most similar pair
𝐻1 = [0.0, 0.2,0.5,0.3], 𝐻2 = [0.0, 0.4,0.4,0.2]
3 Marks: description
2 Marks: application
4 Marks: Computation
1 Mark: similar pair
********** 10 **********
--- page 11 ---
Q5   a   Describe how Gaussian Mixture Model (GMM) is generated to   [10]
construct background frame. A pixel intensity is modeled with a 3-
CO-2
component (K=3)
SO-4
BL-3
Gaussian   Μ   σ   w
Curve
1   100   5   0.5
2   120   7   0.3
3   150   10   0.2
A new pixel intensity is x = 118. Test whether it belongs to
background or foreground.
Solutio   • Generate mixture of ‘k’ Gaussians distribution models for each
n   pixel of background frame
•   Values for ‘k’ is in the range 3 to 5
• Weight of each distribution is proportional to the amount of
time each color/intensity stays on that pixel
•   If a pixel has almost the same intensity for few consecutive
frames
• Weight of the Gaussian distribution of the pixel is more
• This pixel is a background pixel
•   If weight of Gaussian distribution of a pixel is low, that pixel
classified as a foreground pixel
• Each pixel value of reference/ background frame corresponds
to 3 Gaussian mixtures
• Each Gaussian Distribution has different parameters
• Model parameters are updated with each new frame
( 𝑥𝑡−𝜇𝑘 𝑡−1) ≤2.5 𝜎𝑘 𝑡−1
Distance from curve 1= 180-100 =80 and 2.5×5 =12.5, 80>12.5
Distance from curve 2= 180-120 =60 and 2.5×7 =17.5, 60>17.5
Distance from curve 3= 180-150 =30 and 2.5×10 =25, 30>25
Pixel at 180 does not belong to any curve. Therefore, it is a foreground
pixel.
6 Marks: description
3 Marks: computation for each curve
1Mark: Pixel is foreground
Q5   b   For Mean Shift algorithm,   [10]
CO-2   (i) Explain advantages and limitations of Mean Shift algorithm with
SO-1   suitable examples.
BL-3
********** 11 **********
--- page 12 ---
(ii) Predict the effect of increasing the space bandwidth, hs on
clustering the samples. Explain with examples
Solutio   Bandwidth (Radius) Parameter:
n   • Bandwidth is a crucial parameter that controls the radius of the
window
•   It affects the scale of the clusters
• Small bandwidth: More clusters, finer segmentation
• Large bandwidth: Fewer clusters, coarser segmentation
•   Selecting the optimal bandwidth is important for the quality of
segmentation
•   Larger the widow size is, the closer the local mean point is to
the global mean
• Large region can ignore the local structure of the dataset
• Mean value is calculated for a small local area
•   If small bandwidth is used, several noisy clusters can appear
Advantages
• Finds number of modes (clusters) depending on the data values
• Robust to noise or outliers
• Mean is dependent on the regions of high density
• Avoid the influence of noise in the image
• Does not assume any prior shape (like spherical, elliptical, etc.)
of data clusters
Limitations:
• Clustering depends on the choice of window size (bandwidth)
which can lead to under or over segmentation
• Computationally more expensive than K-means
• Slow, especially for high-resolution images
• Can identify noisy pixel as clusters
• Finds arbitrary number of clusters
5 Marks: Effect of bandwidth
5 Marks: advantages and limitations
Q6   a   For 2D images,   [10]
CO-3
(i) Explain image transformations using scaling, rotation, flipping,
SO-4
and shearing, with their effects on images and general
BL-3,4
mathematical forms.
********** 12 **********
--- page 13 ---
(ii) A point P(3, 2) is transformed using the following 2×2
transformation matrix:
𝑇= [2 1
0 1]
Calculate the new coordinates of the point after transformation
(iii)   If P(3,2) is transformed with scaling in x direction by 2 and in Y
direction by 1, followed by horizontal shear factor of 1.
Determine the new coordinates of the point after transformation.
Comment on the transformations in (ii) and (iii).
Solutio   Image Transformations
n   Scaling - resize image
[𝑥2 = [𝑎 0 [𝑥1
𝑦2]   0 𝑏] 𝑦1]
𝑆 = [𝑎 0
0 𝑏]
Rotation
[𝑥2 𝑦2] = 𝑅[𝑥1 𝑦1]   [𝑥2 = [cos⁡(𝜃) −sin⁡(𝜃) ] [𝑥1
𝑦2]   sin⁡(𝜃)   cos⁡(𝜃)   𝑦1]
Flipping -
About Y-axis
[𝑥2 = [−1 0 [𝑥1
𝑦2]   0   1] 𝑦1]
About X-axis
[𝑥2 = [1 0 [𝑥1
𝑦2]   0 −1] 𝑦1]
Image Transformations
Scaling - resize image
[𝑥2 = [𝑎 0 [𝑥1
𝑦2]   0 𝑏] 𝑦1]
𝑆 = [𝑎 0
0 𝑏]
Rotation
[𝑥2 𝑦2] ********** = [cos⁡(𝜃) 13 ********** −sin⁡(𝜃) ] [𝑥1 𝑦1]
sin⁡(𝜃)   cos⁡(𝜃)
--- page 14 ---
[𝑥2 = 𝑅[𝑥1
𝑦2]   𝑦1]
Flipping -
About Y-axis
[𝑥2 = [−1 0 [𝑥1
𝑦2]   0   1] 𝑦1]
About X-axis
[𝑥2 = [1 0 [𝑥1
𝑦2]   0 −1] 𝑦1]
Shearing –
Vertical Shear
[𝑥2   1   0 [𝑥1
𝑦2] = [ 𝑚𝑦 1] 𝑦1]
Horizontal Shear
[𝑥2 = [1 𝑚𝑥 ] [𝑥1
𝑦2]   0   1   𝑦1]
(ii)
[𝑥2 = [2 1 [3 = [8
𝑦2]   0 1] 2]   2]
1 Marks for calculation
(iii)   [𝑥2 𝑦2] = [2 0 1] [3 2] = [6 2] after scaling
0
[𝑥2 = [1 1 [6 = [8
𝑦2]   0 1] 2]   2]
********** 14 **********
--- page 15 ---
Transformations in (ii) and (iii) are same.
6 Marks (1.5 M for each transformation)
2 Marks for calculation and 1M for comment
Q6   b   In relation to stereo vision, explain in brief   [10]
CO-3   (i)   Determination of depth
SO-1
Epipolar geometry
BL-3
Solutio   (i)   For each interest point, (ex: point x) in the first image
n   • Determine corresponding epipolar line in the right image
• Search probable corresponding interest points on epipolar line
• Pick the best match at x’ (use Euclidian distance)
• Disparity = x-x’
• Depth(x) = K/(x-x’), K is dependent on camera matrix
(ii)
•   First camera is mapped with the second camera by a rotation R
• And then by a translation T
•   Location of corresponding points (x and x’) can be found using
Essential Matrix (E) and Fundamental Matrix (F)
• Goal is to determine E and F matrices
********** 15 **********

[Text in pictures on this page, read by OCR]
* Standard epipolar geometry setup involves two cameras observing the same 3D
point P

* Cameras are located at O, and O,

* Projection of point, P, on the image planes is located at p and p’ respectively

epipolar plane Image planes

epipolar line for p

epipolar line for p’

baseline
--- page 16 ---
5 Marks: Depth calculation
5 Marks: Epipolar geometry
Q7   a   Draw architecture of RCNN and explain each layer/block in 2-3 [10]
CO- 4   sentences in brief.
SO-5
BL-3
Solutio
n
1. Generate 2,000 region proposals using the Selective
Search algorithm
2. Input each region proposal into CNN
3. Extract a feature vector of length, 4096 from each region
proposal from CNN
4. Use a pre-trained SVM algorithm to classify the region
proposal to either the background or one of the object classes
5. Refine bounding box predictions using bounding box
regression
Selective search:
• Segment the image into regions
• Regions have similarity in color, texture or any other parameter
********** 16 **********

[Text in pictures on this page, read by OCR]
Input Image

Selective Search
2000 region Proposals

Warp and resize to
224x224

CNN (Ex: Alexnet)

Feature Vector

SS

SVM Classifier BB regressor

Predict Class Refined Box
--- page 17 ---
• Use graph segmentation to capture the regions
• Merge regions into larger regions iteratively
• Merged regions are called region proposals
Warp
• Each region proposal is given as input to CNN
• CNN is used to extract features of region proposal
•   If Alexnet is used, image size should be 227×227
CNN
•   Train Alexnet using a large data set for image classification
• Or use any trained CNN for classification
• Replace last layer which is classification layer (soft max)
SVM
• Binary SVM classifier uses 4096 features to classify each
object
• For ‘n’ number of classes, ‘n’ binary SVMs are used
Bounding box regressor
•   Select region proposals with IOU > 0.5 with any of ground
truth boxes
• Other proposals are background proposals
4 Marks: block diagram
6 Marks: description
Q7b   b   Illustrate ‘Divide and Conquer’ approach for YOLO. Justify that YOLO   [10]
CO-4   speeds up the process of object detection
SO-5
BL-4
Solutio   YOLO is fast
n   • YOLO implements one-stage object detection, making object
detection a single regression task.
• A single neural network of YOLO predicts bounding boxes and
class probabilities from the complete image in one forward
pass (single-step).
•   It significantly increases the speed of operation in YOLO.
YOLO works on the principle of divide and conquer.
YOLO divides the input image into an S × S grid.
Each grid cell is responsible for detecting objects whose center falls
within it.
********** 17 **********
--- page 18 ---
Each cell predicts B bounding boxes and C conditional class
probabilities.
Pr⁡(𝐶𝑙𝑎𝑠𝑠𝑖 | 𝑂𝑏𝑗𝑒𝑐𝑡)
Each bounding box consists of 5 predictions: x, y, w, h, confidence.
x, y → center of box relative to bounds of grid cell
w, h → relative to whole image
Confidence → Pr⁡(𝑂𝑏𝑗𝑒𝑐𝑡) × 𝐼𝑜𝑈 between the predicted box and the
ground truth
These predictions are encoded as S × S × (𝐵× 5 + 𝐶) tensor.
• In the original YOLO paper, the authors used the PASCAL VOC
dataset, which contains 20 classes (C = 20), a grid of 7 × 7 (S =
7), and at most 2 classes per grid element (B = 2), giving a 7 ×
7 × 30 output prediction.
• Figure shows a simplified output vector considering a three-by-
three grid, three classes, and a single class per grid for eight
values. In this simplified case, the output of YOLO would be 3
× 3 × 8.
• YOLOv1 achieved an average precision (AP) of 63.4 on the
PASCAL VOC2007 dataset. These predictions are encoded as
S × S × (𝐵× 5 + 𝐶) tensor.
3 Marks: Justification for speed
7 Marks: divide and conquer approach
********** 18 **********
````

## 2025-26 · Re-Exam · Sem 7 · Answer key · paper 5f028d50d757

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_07/Re-Exam/MBATech_AI_7051/COMPUTER VISION FOR AI/ANS_COMPUTER VISION FOR AI(702AI0C029)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & ML)/MBA Tech (AI)
Year: IV/Sem 7 Re-exam(Exam Year: 2025-2026)
Subject: COMPUTER VISION FOR AI
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question Number 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions
6. In all, 5 questions to be attempted
7. All questions carry equal marks
8. Assume suitable data if necessary
Q1   Answer briefly:
CO-1;   a.   For each of the following applications, identify which feature level (Low-   [04]
SO-1;
level, Mid-level, or High-level) is most appropriate, and explain your
BL-5
reasoning.
i) Detecting car wheels based on feature descriptors and matching
ii) Detecting a person with a hat using semantic relation of objects
Solutio   i) Detecting car wheels: Mid-level features   [02]
n
a. Detecting a car wheel primarily relies on geometric structure and
grouping, making it a quintessential Mid-level feature task.
ii) Detecting a person with a hat: High-level features
This task requires two distinct object recognition steps and a   [02]
semantic relationship between them, making it a High-level feature
task.
CO-2;   b.   Justify that Speeded Up Robust Features (SURF) is fast. Given the [04]
SO-1;
following Hessian matrices for three key points at intermediate of SURF.
BL-5
Test whether SURF stops comparison or continues with the calculation of
Euclidean distance for comparison?
H1 =[10 −1   H2 =[10 −2   H3 =[10 −1
−1 15],   −2 −15],   −1 −5]
Solution   •   It is a speeded-up version of SIFT (Fast and robust algorithm)   [03]
.   • Approximates LoG with Box Filter
********** 1 **********
--- page 2 ---
• Convolution with box filter using integral images speeds up the
process
• Convolution can be done in parallel for different scales
• Thus enabling real-time applications such as tracking and object
recognition
• Uses determinant of Hessian matrix for both scale and location not
trace
Trace1 = 25,   Trace2 = -5,   Trace3 = 5
It will check the Euclidean distance between key point 1 and key point 3
as sign of trace is same.   [01]
CO-3;   c.   Use Earth Mover Distance test whether the given two images match.   [04]
SO-1;
BL-5   1   1   0   0   1   2   1   1
1   2   0   0   2   2   1   1
2   2   3   3   3   3   0   0
1   2   3   2   3   3   0   0
Image 1 (2-bit)   Image 2 (2-bit)
Ans.   Level 0
• Normalized histogram of image1,
p10 = [4/16, 4/16, 5/16, 3/16]   [03]
c10 = [4/16, 8/16, 13/16, 16/16]
• Normalized histogram of image2,   [01]
p20 = [4/16, 5/16, 3/16, 4/16]
c20 = [4/16, 9/16, 12/16, 16/16]
4
𝐸𝑀𝐷𝐿0 = ∑|𝑐10(𝑖) −𝑐20(𝑖)|
𝑖=0
1   1
𝐸𝑀𝐷𝐿0 = 0 + + + 0
16 16
𝐸𝑀𝐷𝐿0 = 0.25
Level 1
Down sample image by averaging:
1   0
2   3
Image 1 (2-bit)
Image 2 (2-bit)
********** 2 **********
--- page 3 ---
• Normalized histogram of image1, p11 = [1/4,   2   1   1/4, 1/4, 1/4]
3   0
c11 = [1/4, 2/4, 3/4, 4/4]
• Normalized histogram of image2, p21 = [1/4, 1/4, 1/4, 1/4]
c21 = [1/4, 2/4, 3/4, 4/4]
𝐸𝑀𝐷𝐿0 = 0
• Weights of levels, wL0 = 1.0, wL1 = 0.5
• Pyramid with EMD Score
= [(wL0 × EMDL0 )+(wL1 × EMDL1)]/(wL0 + wL1)
= [(1×0.25)+(0.5x0)]/1.5 = 0.167
Small EMD indicates a close similarity between the two histograms
CO-4;   d.   In the context of optical flow, what does the velocity vector represent?   [04]
SO-1;
Compare sparse and dense optical flow.
BL-2
Ans.   • Calculates velocity of points between consecutive frames of video   [01]
• Thus, describes speed and direction of the movement of objects for a
sequence of frames
• And provides an estimation of location of points in the next frame
Sparse optical flow
•   Is flow vectors of interest points of frames
• K interest points have K number of velocity vectors   [03]
•   Interest points could be edges or corners of object in a frame
Dense optical flow
• Provides flow vectors of all pixels
• Has one flow vector per pixel
• Has higher accuracy
•   Is slow and computationally expensive
CO-5;   e.   For Region based Convolutional Network, explain the role of ‘Bounding   [04]
SO-1;
Box Regressor’ algorithm.
BL-3
Ans.   • Bounding box are provided for training CNN
• Bounding box generated is for region proposal which may contain a part [02]
of the object
• While Ground truth box is for the entire object
• Intersection over union (IOU) of the boxes measures the closeness of   [02]
bounding with Ground Truth box
• Select region proposals with IOU > 0.5 with any of ground truth boxes
• Other proposals are background proposals
********** 3 **********
--- page 4 ---
Q2   a   For Histogram of Gradient,   [10]
CO-1;   i) Describe the steps for determining HoG descriptor in brief
SO-1;
ii) For image size of 64×128, calculate the length of HoG vector for 8×8
BL-3
pixels/cell and 4×4 cells/ block.
Ans.   i) Steps
• Crop image to obtain image patch
• Divide patch by cells of 8 ⨯ 8 pixels
• Compute the gradients for pixels in the patch (localized portion)
• Make histograms using the computed gradients (magnitude and   [05
orientation) for each cell   ]
• Apply normalization with neighboring histograms
• Concatenate all histograms to form a vector
• Vector represents feature descriptor of the image patch
• Use features to compare objects
• Or use features to train classifier
ii) Length of descriptor
• Each block contains 4 cells ( 1 histogram/ cell)
• Each block has 4 histograms (9 values/ histogram)
• Concatenate 4 histograms to form a 36 x 1 element vector for a
[05
block
]
• 16×16 block is moved in steps of 8 ( i.e. 50% overlap with the
previous block )
• Number of blocks = 7 x 15 = 105
• For each block, there are 36 values
• Length of the final vector 105×36 = 3780
CO-2;   b   For the given image, apply Harris corner detector to test whether pixel at   [10]
SO-1;
the center is corner pixel or not. Sobel operators Gx and Gy. Size of
BL-3
window is 3×3. (Given: k = 0.04 and threshold for corner response =
1000).
0   0   0   0   0
0   0   0   0   0
1   1   1   0   0
1   1   1   0   0
1   1   2   0   0
********** 4 **********
--- page 5 ---
Image
−1 0 1   −1 −2 −1
𝐺𝑥= [ −2 0 2 ] ,   𝐺𝑦= [ 0   0   0 ]
−1 0 1   1   2   1
Ans.
0 0   0   0 0   0 0 0 0 0
0 0 −1 −1 0   0 4 3 1 0
𝐼𝑥= 1 0 −3 −3 0 ,   𝐼𝑦= 1 4 3 1 0
1 1 −4 −5 0   1 1 2 1 0
[ 1 1   2   0   0]   [ 1 1 2 0 0]
[04
]
0 0 0   0 0   0 0 0 0 0
0 0 1   1 0   0 16 9 0 0
𝐼𝑥2 = 1 0 9   9 0 ,   𝐼𝑦2 = 1 16 9 0 0
1 1 16 25 0   1 1 4 0 0
[ 1 1 2   0   0]   [ 1 1 2 0 0]
[01
0 0 0   0   0   ]
0 0 −3 −1 0
𝐼𝑥. 𝐼𝑦= 1 0 −9 −3 0
1 1 −8 −5 0
[ 1 1 2   0   0]
𝐼𝑥 2   𝐼𝑥𝐼𝑦   62 −28
𝐻= ∑𝑤(𝑥, 𝑦) [   2 ] = [   ]   [01
𝐼𝑥𝐼𝑦   𝐼𝑦   −28 55
𝑥,𝑦   ]
𝑅= 𝑑𝑒𝑡(𝐻) −𝑘. {𝑡𝑟𝑎𝑐𝑒(𝐻)}2
𝑅= {(62 × 55) −(−28 × −28)} −0.04 × {62 + 55}2 = 2078.44   [01
R > 1000, it is a corner.   ]
[02
]
[01
]
Q3   a   For Oriented FAST and Rotated BRIEF (ORB),   [10]
CO-2;   i) Write the roles of FAST and rBrief.
SO-1;
ii) Find the orientation of the highlighted key point
BL-5
1   1   1   1   1
********** 5 **********
--- page 6 ---
1   10   10   10   1
Image =   1   10   40   10   1
1   10   10   10   1
1   1   1   1   1
iii) List advantages
Ans   i) Fusion of FAST key point detector and rBRIEF descriptor at each   [02
scale   ]
• FAST is used to detect key points of the image pyramid
• Uses rotated BRIEF based on the orientation of each key point
ii) Orientation
x=0 x=1 x=2 x=3 x=4
y=0   1   1   1   1   1
y=1   1   10   10   10   1
y=2   1   10   40   10   1
y=3   1   10   10   10   1
[05
y=4   1   1   1   1   1
]
𝑚00 = ∑𝐼(𝑥, 𝑦) = (16 ∗1) + (8 ∗10) + 40 = 136
𝑥,𝑦
𝑚10 = ∑𝑥 . 𝐼(𝑥, 𝑦)
𝑥,𝑦
𝑚10 = (0 ∗5) + (1 ∗32) + (2 ∗62) + (3 ∗32) + (4 ∗5) = 272
𝑚01 = ∑𝑦 . 𝐼(𝑥, 𝑦)
𝑥,𝑦
𝑚01 = (0 ∗5) + (1 ∗32) + (2 ∗62) + (3 ∗32) + (4 ∗5) = 272
(𝑚01
𝜃= 𝑡𝑎𝑛−1 ( 𝑚00) ) = 𝑡𝑎𝑛−1 (𝑚01 ) = 𝑡𝑎𝑛−1 (272 272) = 45
(𝑚10   𝑚10
𝑚00)
Orientation of key point is 45°
iii) Advantages
•   Fast, therefore suitable for real time applications
• Scale invariant, enabling it to detect features at different scales
within an image
•   Rotation-invariant, can match object even if the object is oriented
• Not patented like SIFT or SURF   [3]
********** 6 **********
--- page 7 ---
Q3   b   For the generation of feature descriptors using Speeded Up Robust   [10]
CO-3;   Features (SURF), list the steps and explain it in brief.
SO-1;
Justify that SURF is faster than SIFT.
BL-3,5
Ans
Detector   [03
1. Construct Hessian matrix using box filters at each pixel and   ]
identify key points
2. Increase the size of box filters and repeat step 1
3. For each key point, select points within radius of 6s, where s is
standard deviation of filter for key point
4. Apply Gaussian filter of 2.5s on key point
5. Use Haar wavelet of size 4s to determine magnitude and direction
of points
6. Draw histogram of orientation for 6 bins to identify orientation of
key point
Descriptor
1. Around each key point, choose points within region of square with   [04
size (20s, 20s)   ]
2. Divide region into 16 sub-regions
3. For each sub-region, determine vector of length 4
4. Length of descriptor vector for region is 64
SIFT
• High dimensionality
• Leads to good accuracy   [03
• Approximates Laplacian of Gaussian with DoG   ]
• Uses determinant and trace of Hessian matrix
SURF
•   It is a speeded-up version of SIFT (Fast and robust algorithm)
• Approximates LoG with Box Filter
• Convolution with box filter using integral images speeds up the
process
• Convolution can be done in parallel for different scales
• Thus enabling real-time applications such as tracking and object
recognition
********** 7 **********
--- page 8 ---
• Uses determinant of Hessian matrix for both scale and location not
trace
Q4   a   Explain the steps involved in the Bag of Visual Words for feature matching.   [10]
CO-3;
Use example images and histograms for the explanation. K-means
SO-1;
BL-5   clustering uses K = 6
Ans.   First image
1. Extract descriptors of first image   [05
• Choose strong key points, N=10   ]
• Determine corresponding descriptors of length 128
2. Apply K-means clustering on descriptors
• Groups similar descriptors
• Generate K groups or clusters, K=5
• Determine Cluster mean, also called cluster centres
•   Set of K clusters is a visual vocabulary
• Length of each cluster center is length of feature descriptor
Second image
1. Extract feature of key points of second image
2. For each key point, find the nearest cluster from K clusters of first
image
3. Assign the nearest cluster of first image to descriptor of the second
image
4. There can be several descriptors of second image which are
assigned a particular cluster of first image
5. Generate Histogram of K visual words for the image
[05] marks for images and histograms
CO-5;   b   Design an appropriate Convolutional Neural Network (CNN) model with   [10]
SO-1;
the following architecture specifications for an input gray image of size
BL-6
64 × 64.
• One convolutional layer with 12 filters, each of size 3×3
• One max pooling layer with pool size (3×3)
• One dropout layer with probability 0.1
• One flatten layer
********** 8 **********
--- page 9 ---
• Three dense (fully connected) layers
• No padding (i.e., "valid" convolution)
•   Stride = 1 for convolution
Tasks:
1. Provide the output shape after each layer.
2. Do not consider bias terms at any layer.
3. Clearly specify activation functions.
Ans.   Possible solution:
Layer   Description   Formula /   Activation Output
Reasoning   Shape
Input   Gray image   64×64×1   —   (64,
64, 1)
Conv2D   12 filters, 3×3, (64 − 3 + 1) = ReLU   (62,
stride 1, valid   62 → 62×62   62, 12)
padding   spatial size
MaxPooling2D pool size =   floor(62 / 3) —   (20,   [05
(3×3), stride = = 20   20, 12)
3   ]
Dropout   rate = 0.1   (no change in —   (20,
shape)   20, 12)
Flatten   Flatten 3D →   20×20×12 = —   (4800,)
1D   4800
Dense 1   128 units   —   ReLU   (128,)
Dense 2   64 units   —   ReLU   (64,)
Dense 3   10 units (e.g., —   Softmax   (10,)   [05
10-class
output)   ]
Q5   a   For Gaussian Mixture Model, explain   [10]
CO-4;   i)   Key feature
SO-1;
ii)   Initialization phase
BL-2
iii)   Matching of pixels with Gaussian curve
Ans.   • Generate mixture of ‘k’ Gaussians distribution models for each
pixel of background frame.
•   Values for ‘k’ is in the range 3 to 5
• Weight of each distribution is proportional to the amount of time
each color/intensity stays on that pixel   [02
•   If a pixel has almost the same intensity for few consecutive   ]
frames. Weight of the Gaussian distribution of the pixel is more.
This pixel is a background pixel
********** 9 **********
--- page 10 ---
•   If weight of Gaussian distribution of a pixel is low, that pixel
classified as a foreground pixel
• Each pixel value of reference/ background frame corresponds to 3
Gaussian mixtures
• Each Gaussian Distribution has different parameters
• Model parameters are updated with each new frame
Initialization
•   Create a Gaussian model for a pixel value at a location in the first
frame, x1   [02
• Use w=1 and μ = x1 and large σ for Gaussian model   ]
Match pixel in the next frame
• Check if Gaussian includes pixel at the same location in the next
frame
•   Pixel value is xt, at = 2 (for the second frame)
• Matching conditions for xt
• Case 1 (matches with at least of one of K Gaussians): update all   [06
matched Gaussian curves   ]
• Case 2 (no match in any Gaussian): create a Gaussian to model xt
{1 𝑖𝑓 ( 𝑥𝑡−𝜇𝑘 𝑡−1) ≤2.5 𝜎𝑘 𝑡−1
𝑀𝑘(𝑥𝑡) =
0   𝑂𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒
•   If xt is satisfying matching condition, Update parameters of all
matched Gaussians to include xt in the matched Gaussian curve
CO-5;   b   In a Single-Shot Detector (SSD), feature maps of sizes 38×38, 19×19,   [10]
SO-1;
10×10, and 5×5 are used for multi-scale detection. Each location predicts
BL-3
4 bounding boxes with 21 class scores.
• Calculate the total number of bounding boxes generated.
• How many total output values (bounding box coordinates + class
scores) are produced for one image?
Ans.   Feature Map 1: 38×38
• Number of locations = 38 × 38 = 1,444
********** 10 **********
--- page 11 ---
• Bounding boxes = 1,444 × 4 = 5,776
Feature Map 2: 19×19
• Number of locations = 19 × 19 = 361
• Bounding boxes = 361 × 4 = 1,444
Feature Map 3: 10×10
• Number of locations = 10 × 10 = 100
• Bounding boxes = 100 × 4 = 400
Feature Map 4: 5×5
• Number of locations = 5 × 5 = 25
• Bounding boxes = 25 × 4 = 100
Total = 5,776 + 1,444 + 400 + 100 = 7,720 bounding boxes   [06
]
Total Output Values (Bounding Box Coordinates + Class Scores)
For each bounding box, the SSD outputs:
• 4 coordinates (x_center, y_center, width, height) or (x_min,
y_min, x_max, y_max)
• 21 class scores (confidences for each of the 21 classes)
Output values per bounding box = 4 + 21 = 25 values
Method 1: Using total bounding boxes
Total output values = Total bounding boxes × (coordinates + class scores)
Total output values = 7,720 × 25 = 193,000 values
[04
]
Q6   a   Give an overview of the U-Net architecture for image segmentation and   [10]
CO-5;   explain the working of its encoder–decoder structure with a neat
SO-1;
schematic diagram.
BL-2
Ans.   Reference:
********** 11 **********
--- page 12 ---
[03
]
• Input image: U-Net starts with a 2D image, such as a medical
scan or a satellite photo. The goal is to assign a class label to every
pixel in the image.   [03
• Downsampling: The image passes through convolutional layers   ]
that learn important visual features. As the image moves through
different layers, its resolution decreases, and the model identifies
broader patterns.
• Bottleneck layer: At the center of the network, the feature maps
reach their smallest spatial resolution while capturing high-level
semantic features. Simply put, this compressed representation of
the feature maps is the overall context of the input.
• Upsampling: The network then reconstructs the image by
gradually increasing the resolution. Transposed convolutions help
expand the feature maps back toward the original size.
• Skip connections: The feature maps from the downsampling path   [04
are concatenated with those in the upsampling path. This helps   ]
preserve fine-grained spatial details while integrating high-level
contextual information.
• The output is a segmentation map: The final output is a pixel-
wise segmentation mask matching the input size. Each pixel is
classified into a category like object, background, or region of
interest.
CO-4;   b   Draw architecture of Mask RCNN and explain it in brief. Justify the use   [10]
SO-1;
of RoI align in Mask RCNN
BL-3
********** 12 **********

[Text in pictures on this page, read by OCR]
128 64 642

Contraction network Expansion network

Output imag

Input image Eases

572x572 x3

256 128
Li
lglg

a 512 256
3x3, ReLU
SS Zz (ts => conv 3x3, Rel

3 Bx
S# 512 512 1024 sin tS &   —coPyand crop

= # max pool 2x2
*
88 SF: 1024 4A & # up-conv 2x2
_aemes—
a = conv 1x1

o

°
--- page 13 ---
Ans.
• A region proposal on image, width = 200 and height = 145
•   Scale factor = 512/16 = 32
• On feature map, width = 200/32= 6.25 and height = 145/32 = 4.53
•   Coordinates of centre on feature map, x = 9.25, y = 6
•   If size and coordinates of the box are quantized
• Some part of ROI is not processed
• Looses data if coordinates are quantized
•   Therefore ROI align is used
RoI align
• For 3×3 pooling, divide ROI into 9 cells
•   Size of each cell (4.53/3 = 1.51) × (6.53/3 = 2.08)
[04
]
********** 13 **********

[Text in pictures on this page, read by OCR]
Mask RCNN

Input Image

CNN (Ex: Resnet)
Shared Feature Map

Region Proposal Network

Region Proposals

ROI Align

FC Layers
Soft =
2 BB regressor Mask head
Classifier - .

Predicted Class Refined Box Mask Coord
--- page 14 ---
[02
]
• Determine equidistant 4 points in each cell
• Apply bilinear interpolation for intensity at each point of the cell
• Apply max pooling in each cell
Q7   a   Explain the steps of Scale-Invariant Feature Transform in brief. Describe   [10]
CO-1;   the generation descriptor after key point localization of SIFT algorithm.
SO-1;
BL-3
Ans.   • Determine histogram for each cell around key point   [05]
• 16 cells and 8 orientations = 16x8 = 128 bins with magnitude of
gradients as bin value
•   Feature vector of each key point contains 128 elements
• Use Gaussian-weighted circular window with σ equals to 1.5 times
the scale of the image at which key point is selected
• Gaussian window is used to give less emphasis to gradients that
are far from the key point
[05]
• 16 cells and 8 orientations 128 values
• SIFT feature vector of each key point contains 128 elements
********** 14 **********
--- page 15 ---
CO-3;   b   Explain Region Proposal Network of Faster RCNN and justify that it   [10]
SO-1;
makes Faster RCNN is faster than Fast RCNN. Illustrate with example
BL-3
images.
Ans.   • Uses Region Proposal Network (RPN) instead of selective search
method   [5]
• RPN generates regions which possibly contain objects
• These proposals are given to ROI pooling
• Use CNN to generate feature map with ‘C’ channels
• Use a window of size n×n (ex: 3×3)
• Output at each location shows whether the region contains an
object or not
• Move the window to capture all parts of image
•
[05
]
•   Usually, scale of 1:1, 1:2, 1:3, 2:1, etc are used for anchor boxes
• Apply 1×1 convolution on window (red region) to generate
features of size 1×1×C
********** 15 **********
--- page 16 ---
•   Feature corresponding to window which covers a part of the object
is useful to guess whether reference boxes contain an object or not
********** 16 **********
````

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper 2bdd2bed0cb7

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Computer Vision/ANS_Computer Vision(703DB0E027)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2025
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Computer Vision
Date: 09 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 16 pages.
2. Question No.1 is compulsory
3. Out of the remaining questions attempt any 4 Questions.
4. In all questions to be attempted
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1a.
The basis of YOLO (You Only Look Once) is a real-time object detection system that frames the task
of object detection as a single regression problem. Unlike traditional object detection methods that
first generate region proposals and then classify them (like in R-CNN), YOLO looks at the entire image
once and predicts both the bounding boxes and the class probabilities for those boxes simultaneously.
Here’s a breakdown of the key concepts that form the basis of YOLO:
1. Unified Architecture: YOLO uses a single neural network to directly predict bounding boxes
and class probabilities from full images in one evaluation. The network divides the image into a grid
(e.g., 13x13 grid) and for each grid cell, it predicts a certain number of bounding boxes and the
probability of those boxes containing certain classes of objects.
2. Grid-based Detection: The input image is divided into a grid, and each grid cell is responsible
for detecting an object if the object’s center falls into that grid cell. For each cell, YOLO predicts:
• Bounding box coordinates (x, y, width, height),
• Objectness score (confidence that an object is in the bounding box),
• Class probabilities.
3. Single Forward Pass: Instead of running a separate classifier for each possible region of
interest, YOLO performs detection in a single forward pass of the network, making it much faster
than traditional methods.
4. Loss Function: YOLO optimizes a loss function that penalizes errors in bounding box
coordinates, objectness scores, and class probabilities. The loss function ensures the model learns to
predict accurate locations and correct classifications for objects.
5. Speed: YOLO’s key advantage is its speed. By looking at the whole image at once, it is able to
process images quickly, which makes it suitable for real-time applications.
********** 1 **********
--- page 2 ---
6. Localization and Classification: YOLO jointly solves object localization and classification,
which leads to more global context when making predictions.
Despite its speed, earlier versions of YOLO struggled with small objects and objects that were close to
each other. However, newer versions (YOLOv2, YOLOv3, and beyond) improved accuracy and
addressed many of these challenges while maintaining real-time processing capabilities.
Q1b.
Contrastive Loss is a loss function used primarily in metric learning tasks, where the goal is to learn a
distance metric that ensures similar data points are close to each other in the embedding space, while
dissimilar points are pushed farther apart. It is commonly used in applications like face verification,
Siamese networks, and self-supervised learning.
Purpose:
The main objective of contrastive loss is to train a model to create meaningful embeddings of data
points, such that:
•   Positive pairs (data points that belong to the same class) are pulled closer together in the
embedding space.
•   Negative pairs (data points that belong to different classes) are pushed farther apart in the
embedding space.
Key Concepts:
•   Anchor: The reference data point.
•   Positive Sample: A sample that is similar (or belongs to the same class) as the anchor.
•   Negative Sample: A sample that is dissimilar (or belongs to a different class) than the anchor.
Contrastive Loss Formula:
The contrastive loss function is defined as follows:
L(W) = \frac{1}{2N} \sum_{i=1}^{N} \left[ y \cdot D^2 + (1 - y) \cdot \max(0, m - D)^2 \right]
Where:
• W are the model parameters (weights).
•   N is the total number of pairs.
•   y is a binary label that indicates whether the pair is a positive pair (1 if the points are similar, 0
if dissimilar).
•   D is the Euclidean distance between the embeddings of the two data points.
•   m is the margin (a hyperparameter) that defines how far apart dissimilar pairs should be.
•   L(W) is the contrastive loss that we aim to minimize during training.
How the Loss Works:
1. For Positive Pairs (y = 1):
• The goal is to minimize the distance D between the anchor and the positive sample.
• If the two samples are similar (i.e., belong to the same class), the loss encourages the network to
reduce the Euclidean distance between their embeddings.
• The term for positive pairs is: D^2 , which tries to pull the similar points together.
2. For Negative Pairs (y = 0):
• The goal is to increase the distance between the anchor and the negative sample.
********** 2 **********
--- page 3 ---
• If the two samples are dissimilar (i.e., belong to different classes), the loss tries to push the
distance between their embeddings to be greater than a predefined margin m .
• The term for negative pairs is: \max(0, m - D)^2 , which penalizes the model if the
distance D is less than the margin m , meaning the dissimilar points are too close.
Q1c.
1. Blurring Filters
Blurring is used to reduce noise and detail in an image by averaging neighboring pixel values.
•   Average Blurring (Box Filter):
• Function: cv2.blur()
• Purpose: Each pixel value is replaced by the average of the pixel values in a square
neighborhood around the pixel.
• Kernel Example: A 3x3 kernel would result in averaging the values of the surrounding pixels.
Gaussian Blurring:
• Function: cv2.GaussianBlur()
• Purpose: Similar to average blurring, but the weights of the pixels decrease with distance from
the central pixel, following a Gaussian distribution.
Median Blurring:
• Function: cv2.medianBlur()
• Purpose: Instead of averaging, the median of the pixel values in the neighborhood is computed.
This is particularly useful for reducing salt-and-pepper noise.
2. Sharpening Filters
Sharpening enhances the edges in an image by highlighting areas of high contrast.
•   Laplacian Filter:
• Function: cv2.Laplacian()
• Purpose: A second-order derivative filter that enhances the edges by computing the Laplacian of
the image, emphasizing regions where there is a rapid change in intensity.
3. Edge Detection Filters
Edge detection filters highlight areas of the image where there are sharp intensity changes, such as
object boundaries.
•   Sobel Filter:
• Function: cv2.Sobel()
• Purpose: Computes the first-order derivative (gradient) in the x or y direction. The Sobel
operator can highlight edges in a specific direction.
Canny Edge Detector:
• Function: cv2.Canny()
• Purpose: A multi-step algorithm that performs edge detection using gradient magnitude and
non-maximum suppression. It detects edges efficiently by considering both gradient strength and
edge continuity.
4. Noise Reduction Filters
These filters help in reducing noise in an image, especially useful for images with imperfections or
random variations.
********** 3 **********
--- page 4 ---
•   Non-Local Means Denoising:
• Function: cv2.fastNlMeansDenoising()
• Purpose: Reduces noise while preserving sharp details in the image, useful for denoising color
images or video frames.
5. Morphological Filters
Morphological operations are used to process binary or grayscale images, typically for tasks like noise
removal, object extraction, and shape analysis.
•   Erosion:
• Function: cv2.erode()
• Purpose: Shrinks the white regions in a binary image by eroding boundaries, often used to
remove noise.
Q1d.
OpenCV uses the luminosity method for converting color images (RGB) to grayscale. This method
takes into account the human eye’s sensitivity to different colors, assigning higher weights to the green
channel, as the human eye is more sensitive to green light than to red or blue light. The formula
OpenCV employs for the conversion is based on the ITU-R BT.601 standard for luminance calculation.
Formula for Conversion:
The grayscale value for each pixel is computed using the following formula:
\text{Gray} = 0.299 \times R + 0.587 \times G + 0.114 \times B
Where:
•   R is the red channel value of the pixel.
•   G is the green channel value of the pixel.
•   B is the blue channel value of the pixel.
Logic Behind the Formula:
The formula assigns different weights to the RGB channels because the human eye perceives colors
with varying sensitivity:
•   Green (G) contributes the most (58.7%) to the perceived brightness because the human eye is
most sensitive to green.
•   Red (R) contributes significantly (29.9%) but less than green.
•   Blue (B) contributes the least (11.4%), as the human eye is less sensitive to blue light.
This weighted sum is more accurate than a simple average of the RGB values because it reflects how
humans perceive brightness. By emphasizing the green channel and de-emphasizing the blue channel,
the grayscale image better represents the intensity of the scene as perceived by the human visual
system.
Why Not Simple Averaging?
A simple averaging method would take equal weights for all three color channels:
\text{Gray} = \frac{R + G + B}{3}
However, this approach does not account for the human eye’s varying sensitivity to different colors,
which could result in a less perceptually accurate grayscale image. The luminosity method used by
OpenCV provides a more realistic conversion by considering how colors contribute differently to
perceived brightness.
Q2.
********** 4 **********
--- page 5 ---
Instance Segmentation is a computer vision task that combines object detection and semantic
segmentation. Its purpose is to detect objects in an image, classify them, and generate precise pixel-wise
masks for each object instance. This means that it not only identifies the objects but also separates each
instance of the same class. It provides a more fine-grained analysis than either object detection or
semantic segmentation alone.
Key Characteristics of Instance Segmentation:
1. Object Detection:
• Identifies and classifies objects in an image.
• Produces bounding boxes that localize objects.
2. Semantic Segmentation:
• Assigns a label to each pixel in the image, indicating which object class the pixel belongs to.
• It does not differentiate between different instances of the same class.
3. Instance Segmentation:
• Combines both tasks: It detects objects (like object detection) but also provides pixel-level
masks (like semantic segmentation), while distinguishing between different instances of the same
object class.
• For example, in a picture with multiple people, instance segmentation would classify and
separate each person individually by assigning each a unique mask.
Example:
In a street scene with two cars and three pedestrians:
•   Object Detection: Draws bounding boxes around each car and pedestrian and labels them as
“car” and “person.”
•   Semantic Segmentation: Assigns a “car” label to every pixel belonging to a car and a “person”
label to every pixel belonging to a pedestrian.
•   Instance Segmentation: Labels each car and pedestrian with a separate mask, distinguishing
between the two cars and three pedestrians individually.
How Instance Segmentation Works:
Instance segmentation typically involves several steps that extend object detection and semantic
segmentation tasks.
1. Feature Extraction (Backbone Network):
•   A Convolutional Neural Network (CNN), such as ResNet, is used to extract features from the
input image. The network transforms the image into feature maps that capture important visual
patterns like edges, textures, and object parts.
2. Region Proposal:
•   A Region Proposal Network (RPN), such as the one used in Faster R-CNN, generates candidate
regions of interest (ROIs) where objects might be located. This step proposes areas of the image that
are likely to contain objects.
3. Bounding Box Prediction:
•   The network predicts the bounding boxes for each proposed region, localizing objects by
generating coordinates that define the region around each object.
4. Object Classification:
•   Each detected object is classified into one of the predefined categories (e.g., “person,” “dog,”
“car”) using the features extracted from the region proposals.
********** 5 **********
--- page 6 ---
5. Mask Generation:
•   After detecting and classifying objects, a separate mask head is used to predict a pixel-level
mask for each object. The mask provides a fine-grained segmentation of the object’s shape.
•   The mask is applied within the predicted bounding box, ensuring that only the object is
segmented while ignoring the background or other objects.
6. Non-Maximum Suppression (NMS):
•   Multiple bounding boxes for the same object are often predicted. NMS is used to filter
overlapping boxes by keeping the one with the highest confidence score, thus removing duplicates.
Popular Architectures for Instance Segmentation:
1. Mask R-CNN:
• Mask R-CNN is the most popular architecture for instance segmentation. It extends Faster R-
CNN by adding a third branch for predicting masks.
• It has three main components:
1.   Region Proposal Network (RPN): Proposes regions of interest where objects might be
located.
2.   Bounding Box and Classification Head: Detects and classifies objects within each
region.
3. Mask Head: Generates pixel-level masks for each detected object, giving the shape and
boundaries of the object.
2. YOLACT (You Only Look At Coefficients):
• YOLACT is designed for real-time instance segmentation. It decouples mask prediction from
bounding box prediction, making the process faster.
• It generates a set of prototype masks and learns coefficients to combine them into final instance
masks.
3. SOLO (Segmenting Objects by Locations):
• SOLO segments objects directly by learning the spatial location of objects in the image grid,
instead of relying on bounding box proposals. This eliminates the need for region proposals and
makes the process faster while still achieving accurate segmentation.
4. TensorMask:
• TensorMask uses a dense sliding window approach to predict masks for objects at every location
in the image. It applies a tensor decomposition technique to efficiently handle mask generation for
high-resolution images.
Challenges in Instance Segmentation:
1. Overlapping Objects:
• One of the main challenges is distinguishing between overlapping objects, especially when
multiple instances of the same object class are closely packed together.
2. Fine Object Boundaries:
• Accurately segmenting the boundaries of objects is often difficult, particularly for objects with
complex shapes or fine details.
3. Computational Complexity:
********** 6 **********
--- page 7 ---
• Instance segmentation models, such as Mask R-CNN, are computationally intensive due to the
need for pixel-wise predictions and multi-stage processing. This makes them slower than simpler
tasks like object detection.
Applications of Instance Segmentation:
1. Autonomous Driving:
• In self-driving cars, instance segmentation is used to detect and differentiate between objects like
pedestrians, vehicles, road signs, and other important elements in the scene, enabling the car to
make safe navigation decisions.
2. Medical Imaging:
• Instance segmentation is widely used in medical imaging for tasks like detecting and segmenting
tumors, cells, or organs from images like CT scans or MRIs. It helps doctors make precise
diagnoses and treatment plans.
3. Robotics:
• Robots use instance segmentation to identify and manipulate objects in their environment. This
allows them to understand which objects are present and how to interact with them in tasks like
picking and placing.
4. Image Editing and Augmented Reality (AR):
• Instance segmentation can be used to separate objects from the background for tasks like object
removal or enhancement in image editing. In AR, it enables virtual objects to interact accurately
with real-world objects.
5. Panoptic Segmentation:
• Instance segmentation is also used as a part of panoptic segmentation, which unifies both
instance segmentation (for objects) and semantic segmentation (for background elements) into a
single framework.
Instance Segmentation vs. Related Tasks:
1. Object Detection:
• Object detection only identifies objects and draws bounding boxes around them without
segmenting the object at the pixel level.
2. Semantic Segmentation:
• Semantic segmentation assigns a class label to each pixel in the image but does not differentiate
between individual object instances of the same class.
3. Instance Segmentation:
• Instance segmentation goes beyond both object detection and semantic segmentation by
identifying individual objects, classifying them, and generating pixel-level masks that separate
each object instance.
Summary:
•   Instance segmentation is a complex task that combines object detection and semantic
segmentation, providing pixel-level masks for each object instance in an image.
•   Popular architectures like Mask R-CNN, YOLACT, and SOLO are designed to perform
instance segmentation with high accuracy and, in some cases, real-time performance.
********** 7 **********
--- page 8 ---
•   Applications of instance segmentation include autonomous driving, medical imaging, robotics,
and AR, where precise object identification and segmentation are crucial.
•   It is more challenging than either object detection or semantic segmentation due to the need for
pixel-level precision and instance-level separation, especially in cluttered scenes with overlapping
objects.
Q3.
Semantic Segmentation is a computer vision task that involves classifying each pixel in an image into
a predefined category. The goal of semantic segmentation is to provide a dense prediction, where each
pixel is labeled with a specific class (e.g., road, car, sky, person, etc.). Unlike object detection, which
outputs bounding boxes around objects, semantic segmentation provides a more fine-grained
understanding of the image by labeling every pixel.
Key Characteristics of Semantic Segmentation:
1. Pixel-Level Classification:
• In semantic segmentation, each pixel in the image is assigned to a specific category. For
example, in a road scene, every pixel will be classified as “road,” “car,” “sky,” “pedestrian,” etc.
2. Class-Level Grouping:
• Pixels are grouped by their class, meaning all instances of the same class are treated as part of
one category. This means that semantic segmentation does not distinguish between different
instances of the same object. For example, if there are two people in an image, both will be labeled
as “person” without separating them as individual instances.
Example:
Consider an image of a street with cars, pedestrians, and buildings. Semantic segmentation would:
•   Label all pixels that belong to a “car” as one category.
•   Label all pixels that belong to a “person” as another category.
•   Label pixels belonging to “buildings” as yet another category.
It does not distinguish between two different cars or two different people—both cars will have the same
label “car,” and both people will have the same label “person.”
How Semantic Segmentation Works:
The task of semantic segmentation is usually carried out by Convolutional Neural Networks (CNNs).
Below are the typical steps involved in the process:
1. Feature Extraction (Convolutional Layers):
•   Similar to other computer vision tasks like image classification or object detection, semantic
segmentation begins with extracting features from the image using convolutional layers. These layers
capture hierarchical features, starting with low-level features like edges and moving to more abstract
features such as object parts.
2. Fully Convolutional Networks (FCNs):
•   One of the first architectures specifically designed for semantic segmentation is the Fully
Convolutional Network (FCN). In an FCN, all fully connected layers are replaced by convolutional
layers, allowing the network to output a dense, pixel-wise classification map.
•   This way, the output has the same spatial dimensions as the input image, with each pixel
classified into one of the predefined classes.
3. Encoder-Decoder Architectures:
•   Encoder-Decoder networks are common in semantic segmentation. The encoder
(downsampling) part of the network captures features at multiple scales by progressively reducing the
********** 8 **********
--- page 9 ---
image size. The decoder (upsampling) part reconstructs the original spatial resolution by upsampling
the feature maps.
•   Skip connections between corresponding encoder and decoder layers (as seen in U-Net) help
preserve low-level details, ensuring accurate segmentation at pixel-level boundaries.
4. Dilated (Atrous) Convolutions:
•   Dilated convolutions are often used to increase the receptive field without losing spatial
resolution. This allows the network to capture more context from the image while maintaining fine
details, which is important for accurate segmentation.
5. Conditional Random Fields (CRFs):
•   In some models (e.g., DeepLab), Conditional Random Fields (CRFs) are applied after the CNN
to refine the pixel-level predictions. CRFs help sharpen the boundaries of segmented objects,
improving accuracy at the edges, which can sometimes be blurry in CNN predictions.
Popular Architectures for Semantic Segmentation:
1. FCN (Fully Convolutional Network):
• FCN replaces the fully connected layers in a traditional CNN with convolutional layers, allowing
for dense pixel-wise predictions. FCN was one of the earliest successful models for semantic
segmentation.
2. U-Net:
• Originally developed for medical image segmentation, U-Net is a popular encoder-decoder
architecture with skip connections between encoder and decoder layers, allowing the network to
recover fine-grained details during upsampling. It is particularly useful in scenarios where precise
segmentation is required.
3. DeepLab (DeepLabV3, DeepLabV3+):
• DeepLab uses dilated convolutions and incorporates Conditional Random Fields (CRFs) to
refine the boundaries of segmented objects. DeepLab is widely used in state-of-the-art semantic
segmentation tasks due to its ability to capture multi-scale context and improve boundary accuracy.
4. SegNet:
• SegNet is another encoder-decoder architecture similar to U-Net. It uses the indices from max-
pooling layers during the upsampling phase to help improve the precision of the segmentation map.
5. PSPNet (Pyramid Scene Parsing Network):
• PSPNet introduces a pyramid pooling module to capture global context by pooling features at
multiple scales. This allows the network to make better predictions by understanding the larger
context of objects in the scene.
Challenges in Semantic Segmentation:
1. Boundary Precision:
• Accurate segmentation at object boundaries can be challenging, especially when the object has a
complex shape or when there is ambiguity in the boundary regions. Models must learn to
differentiate between small, fine-grained details and background clutter.
2. Class Imbalance:
• In many images, certain classes (like background or sky) may dominate, leading to an imbalance.
This can cause the model to underperform in detecting smaller objects or minority classes, which
may be of particular importance in some applications.
********** 9 **********
--- page 10 ---
3. Computational Cost:
• Semantic segmentation models need to produce dense, pixel-level predictions, which can be
computationally expensive, especially for high-resolution images. Efficient architectures and
optimization techniques are often required to achieve real-time performance.
4. Occlusions:
• When objects overlap or occlude one another, the model may struggle to segment each object
correctly, especially if they belong to the same class.
Applications of Semantic Segmentation:
1. Autonomous Vehicles:
• Semantic segmentation is crucial for autonomous driving, as it helps the vehicle understand the
environment by labeling roads, pedestrians, other vehicles, and obstacles, allowing the system to
make safe navigation decisions.
2. Medical Imaging:
• In medical applications, semantic segmentation is used to label and identify organs, tumors, or
other structures in medical images (e.g., MRI or CT scans). Precise segmentation is critical for
diagnosis and treatment planning.
3. Satellite and Aerial Imagery:
• In remote sensing and satellite imagery, semantic segmentation is used to analyze land use, crop
health, deforestation, and urban development by classifying different land regions.
4. Robotics:
• Robots use semantic segmentation to understand their environment and identify objects for
manipulation or navigation. This helps robots perform tasks such as picking objects or moving
through obstacles.
5. Augmented Reality (AR):
• In AR applications, semantic segmentation helps in overlaying digital elements onto real-world
objects by understanding the boundaries and categories of objects in the scene.
Difference from Related Tasks:
1. Object Detection:
• Object detection identifies and localizes objects by drawing bounding boxes around them, but it
does not provide pixel-level precision. In contrast, semantic segmentation provides a pixel-wise
classification of the image.
2. Instance Segmentation:
• Instance segmentation is a more advanced task than semantic segmentation, as it not only
classifies each pixel but also distinguishes between different instances of the same object class. In
semantic segmentation, all objects of the same class are grouped together, while instance
segmentation assigns unique labels to each object instance.
Summary:
•   Semantic segmentation involves classifying each pixel in an image into a predefined class,
allowing for dense, pixel-wise understanding of the scene.
•   It is commonly used in autonomous driving, medical imaging, remote sensing, and robotics,
where a detailed understanding of the scene is required.
********** 10 **********
--- page 11 ---
•   Architectures such as FCN, U-Net, DeepLab, and PSPNet are popular for performing semantic
segmentation.
•   The key challenge lies in achieving accurate boundary detection, managing class imbalances, and
handling computational complexity, especially in real-time applications.
Q4.
Contour Detection is a computer vision technique used to identify and extract the boundaries of objects
within an image. Contours are simply curves joining all the continuous points along a boundary that
have the same color or intensity. In the context of image processing, contours are useful for object
detection, shape analysis, and recognition.
Key Concepts in Contour Detection:
1. Contours:
• A contour is the boundary or outline of an object, represented as a curve or a list of points.
• Contours are typically found by detecting edges and then tracing the boundary of objects in the
image.
2. Contour Representation:
• Contours can be represented as a list of points, where each point corresponds to a pixel along the
boundary of the object.
• Contours can be either open (a line or curve) or closed (forming a loop around an object).
How OpenCV Performs Contour Detection:
In OpenCV, contour detection is performed using the cv2.findContours() function, which finds contours
in a binary image. The general process involves the following steps:
Step-by-Step Process:
1. Convert the Image to Grayscale:
•   Since contour detection is based on intensity differences, the first step is to convert the image to
grayscale using cv2.cvtColor().
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
2. Apply Binary Thresholding:
•   Contours are detected in a binary image (black and white). Hence, after converting to grayscale,
you apply a thresholding operation to obtain a binary image. In a binary image, pixels that are above a
threshold are set to white (255), and those below are set to black (0).
ret, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
Alternatively, you can use Canny Edge Detection to create a binary image that highlights the edges,
which often provides better results for contour detection:
edges = cv2.Canny(gray_image, 100, 200)
3. Find Contours:
•   Once you have a binary image, you can find the contours using cv2.findContours(). This function
takes a binary image as input and returns a list of detected contours and the contour hierarchy.
•   Syntax:
contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE,
cv2.CHAIN_APPROX_SIMPLE)
•   Parameters:
• binary_image: The input binary image where contours will be detected.
• cv2.RETR_TREE: The contour retrieval mode. It defines how the contours should be retrieved.
********** 11 **********
--- page 12 ---
•   cv2.RETR_EXTERNAL: Retrieves only the outermost contours.
•   cv2.RETR_LIST: Retrieves all contours without establishing any hierarchical
relationships.
•   cv2.RETR_CCOMP: Retrieves all contours and organizes them into a two-level
hierarchy.
•   cv2.RETR_TREE: Retrieves all contours and reconstructs a full hierarchy of nested
contours.
• cv2.CHAIN_APPROX_SIMPLE: The contour approximation method. This compresses
horizontal, vertical, and diagonal segments and leaves only their end points.
•   cv2.CHAIN_APPROX_NONE: Stores all the points on the contour boundary.
•   cv2.CHAIN_APPROX_SIMPLE: Compresses segments to reduce memory usage and
processing time by only keeping essential points.
•   Return Values:
• contours: A list of contour points, where each contour is represented as a NumPy array of
coordinates.
• hierarchy: Contains information about the image topology. It describes the parent-child
relationships between contours, useful in detecting nested contours.
4. Draw Contours:
•   After detecting contours, you can visualize them on the original image using
cv2.drawContours().
•   Syntax:
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
•   Parameters:
• image: The image on which to draw the contours.
• contours: The list of contours obtained from cv2.findContours().
• -1: Specifies that all contours should be drawn. If a specific contour is to be drawn, you can pass
its index.
• (0, 255, 0): The color of the contour (in this case, green).
• 2: The thickness of the contour lines.
•   Example:
image = cv2.imread('input_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE,
cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow('Contours', image)
cv2.waitKey(0)
Types of Contour Retrieval Modes:
1. cv2.RETR_EXTERNAL:
********** 12 **********
--- page 13 ---
• Retrieves only the outer contours and ignores any contours that are inside or nested within other
objects.
2. cv2.RETR_LIST:
• Retrieves all contours without any hierarchical information. All contours are treated as separate,
independent objects.
3. cv2.RETR_CCOMP:
• Retrieves all contours and arranges them in a two-level hierarchy. Outer contours of the object
are stored on one level, and the contours of holes inside the object are stored on the second level.
4. cv2.RETR_TREE:
• Retrieves all contours and reconstructs a full hierarchical structure of nested contours. This is
useful for detecting objects within objects (e.g., detecting nested shapes).
Types of Contour Approximation Methods:
1. cv2.CHAIN_APPROX_NONE:
• Stores all the contour points without any approximation. This leads to more detailed contours but
uses more memory and computation.
2. cv2.CHAIN_APPROX_SIMPLE:
• Compresses segments by only keeping their endpoints. This reduces the number of points
representing the contour, thus improving efficiency.
Applications of Contour Detection:
1. Object Detection and Recognition:
• Contours can be used to detect and recognize objects based on their shapes. By analyzing the
contours, one can classify objects or track them in videos.
2. Shape Analysis:
• Contours allow the extraction of shape-related features, such as perimeter, area, convexity, and
aspect ratio, enabling applications such as shape matching and object recognition.
3. Object Tracking:
• Contours can be used to detect moving objects in video sequences by tracking the changes in the
shape and boundary of objects over time.
4. Image Segmentation:
• Contours help in segmenting objects from the background in an image. By detecting object
boundaries, contours enable efficient segmentation for further analysis.
Summary:
•   Contour Detection is used to find the boundaries of objects in images.
•   OpenCV performs contour detection using the cv2.findContours() function, which finds and
retrieves contours from binary images.
•   Before detecting contours, the image is typically converted to grayscale and thresholded to create
a binary image.
•   The contours can then be drawn using cv2.drawContours() and used for tasks such as object
detection, shape analysis, and image segmentation.
********** 13 **********
--- page 14 ---
This powerful tool can be used in a variety of applications, from identifying shapes to tracking objects
in videos, making it an essential technique in computer vision.
Q5.
Edge Detection is a fundamental technique in computer vision and image processing that aims to
identify the boundaries or significant changes in intensity in an image, typically where the color or
brightness changes abruptly. Edges are useful for identifying objects, their shapes, and structures
within an image. Various techniques can be used for edge detection, each with its own strengths
and methods.
Key Methods for Edge Detection:
1. Gradient-Based Edge Detection:
Gradient-based methods detect edges by calculating the rate of change in pixel intensity across an
image. The magnitude of this change is used to detect sharp transitions, which correspond to
edges.
a. Sobel Operator:
• Description: The Sobel operator uses convolution to compute the first-order derivatives
(gradients) of the image in both the horizontal (x) and vertical (y) directions. It highlights
regions where the intensity changes significantly, thus detecting edges.
• Kernels:
•   The Sobel operator uses two 3x3 kernels, one for detecting changes in the horizontal
direction (Gx) and one for the vertical direction (Gy):
2. Second-Order Derivative Methods:
These methods focus on detecting edges based on the second-order derivative of the image
intensity. The second derivative identifies points where the intensity changes sharply.
a. Laplacian of Gaussian (LoG):
•   Description: The Laplacian of Gaussian (LoG) method combines Gaussian smoothing with
the Laplacian operator. First, the image is smoothed to reduce noise, and then the Laplacian is
applied to detect regions of rapid intensity change.
•   Laplacian Operator:
The Laplacian operator computes the second derivative of the image, detecting edges by looking
for zero-crossings in the derivative.
3. Canny Edge Detection:
•   Description: The Canny Edge Detector is one of the most widely used edge detection
methods due to its accuracy and robustness. It is a multi-step process that includes noise
reduction, gradient calculation, non-maximum suppression, and edge tracking by hysteresis.
•   Steps:
1.   Noise Reduction: Apply a Gaussian filter to the image to smooth it and reduce noise.
2.   Gradient Calculation: Compute gradients in the x and y directions (using Sobel
filters) to find areas with sharp intensity changes.
3.   Non-Maximum Suppression: Thin the edges by keeping only the local maxima in the
gradient direction.
4.   Hysteresis Thresholding: Use two thresholds (a high threshold and a low threshold)
to detect strong edges and weak edges. Weak edges connected to strong edges are kept, while
other weak edges are discarded.
********** 14 **********
--- page 15 ---
Q6.
Image registration is the process of aligning two or more images of the same scene or object, taken
from different times, perspectives, or sensors, so that the corresponding points in the images
overlap. The goal of image registration is to geometrically align multiple images for comparison,
fusion, or other purposes. This is essential in various fields such as medical imaging, satellite
imagery, computer vision, and augmented reality.
General Steps in Image Registration:
1. Preprocessing:
• This step involves preparing the images for registration. It may include:
•   Noise reduction: Removing noise that could interfere with feature detection.
•   Image enhancement: Improving the contrast or clarity of the images for better
feature extraction.
2. Feature Detection:
• Key points (or features) are detected in both images. These features are distinctive points in
the image, such as corners, edges, or blobs, that can be easily matched between the images.
• Common methods for detecting keypoints include:
•   SIFT (Scale-Invariant Feature Transform): Detects scale and rotation-invariant
features.
•   SURF (Speeded-Up Robust Features): Similar to SIFT but faster.
•   ORB (Oriented FAST and Rotated BRIEF): A fast and efficient alternative to SIFT
and SURF.
• Feature detectors locate important points or regions in the images that can serve as anchors
for alignment.
3. Feature Matching:
• After detecting the keypoints, the next step is to match corresponding features between the
images. This is done by comparing the feature descriptors (a mathematical representation of
the features) of both images and finding the best matches.
• Techniques for feature matching include:
•   Brute-Force Matching: Compares each descriptor in one image with all descriptors
in the other image.
•   FLANN (Fast Library for Approximate Nearest Neighbors): A more efficient
method for high-dimensional feature matching.
•   KNN (k-Nearest Neighbors): Finds the closest matches between descriptors based on
distance metrics.
4. Transformation Model Estimation:
• Once corresponding points (features) have been matched between the images, the next step
is to estimate the geometric transformation that aligns one image with the other.
• Common transformation models include:
•   Translation: Shifting the image by a certain amount in the x and y directions.
********** 15 **********
--- page 16 ---
•   Rotation: Rotating the image around a point.
•   Scaling: Resizing the image.
•   Affine Transformation: A linear transformation that includes translation, scaling,
rotation, and shearing. It preserves parallel lines but not angles or lengths.
•   Homography (Perspective Transformation): Used for more complex
transformations, where perspective changes. It can map points from one image plane to
another, accounting for both translation and rotation.
• RANSAC (Random Sample Consensus) is often used to robustly estimate the
transformation while rejecting outliers (mismatched points). It works by iteratively selecting
random sets of correspondences and finding the best transformation that fits the majority of
matches.
********** 16 **********
````

## 2024-25 · Re-Exam · Sem 6 · Answer key · paper 4539fccdc63e

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/BTech_AIDS_7056/Computer Vision/ANS_Computer Vision(702AI0C017)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (11 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI & DS)/B. Tech Intg. (CE)
Year: III / VI/Semester VI/Semester XII(Exam Year: 2024-2025)
Subject: Computer Vision
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 11 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right-hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Answer briefly:   [20]
CO- 4   a.   In relation to epipolar geometry, explain epipolar constraint. Show
SO- 1,6   [05]
BL- 2   how it useful in matching key points.
Solution
Description (3M)
Use of epipolar constraint (2M)
CO- 3   b.   Explain in brief any two advantages and two limitations of the K-
SO- 1,6   [05]
BL- 5   Means algorithm.
Advantages:
Solution
1. Simple and Easy to Implement
********** 1 **********

[Text in pictures on this page, read by OCR]
* For stereo images,
* Akey point in left image has corresponding point in a line in right image
* This is epipolar constraint
* Epipolar constraint reduces matching problem from 2D image search to 1D line search
* Therefore search for correspondences is quicker
* Corresponding point is searched on epipolar line

* Determine a epipolar line for matching each corresponding point

Epipolar line

Key point

Left image Right image
--- page 2 ---
2. Computationally Efficient
Initial random centroids → quickly move to stable
positions after few iterations.
Limitations:
1. Requires Predefined K
2. Sensitive to Initial Centroids
(2M) for points
(2M) for explanation
c.   Determine the integral image for the following image.
CO- 2
SO- 1,6   [05]
BL- 4
Integral image
Solution
(5M)
CO- 1   d.
SO- 1,6   Explain two examples of mid-level processing.   [05]
BL- 5
1. Use low level features for image matching
2. Keep track of moving objects in a video
3. Determine optical flow to predict speed and direction of
Solution   movement of object
4. Image Clustering
Any two examples (2M)
Explanation (3M)
Given the following gradient magnitude and orientation matrices,
compute the histogram of oriented gradients using 9 bins (0–180°).
What is the final HOG feature vector for the 4×4 image?
Which bin does a pixel with:
(a) 35° belong to?
Q2a   (b) 95° belong to?
CO- 1
SO- 1, 6   [10]
BL- 5
Gradient Magnitude   Gradient orientation (Ɵ)
Bin Range   Bin
Solution   (°)   Center
0–20   10
20–40   30
********** 2 **********
--- page 3 ---
40–60   50
60–80   70
80–100   90
100–120   110
120–140   130
140–160   150
160–180   170
(10°, M=2): +2, (20°, M=3): +3, (30°, M=1): +1, (40°, M=2):+2
(50°, 4): +4, (60°, 2): +2, (70°, 1): +1, (80°, 3): +3
(90°, 2): +2, (100°, 1): +1, (110°, 3): +3, (120°, 2): +2
(130°, 1): +1, (140°, 2): +2, (150°, 2): +2, (160°, 4): +4
HoG vector is [2, 4, 6, 3, 5, 4, 3, 4, 4]
Bin range (5M)
Determination of HoG vector (5M)
For Harris corner detector,
Q2b   i) Show with example images that Harris corner detector is
CO- 1   invariant to rotation and variant to scaling   [10]
SO- 1, 6   ii) Explain the steps involved in constructing Harris matrix and
BL- 5   using corner response to determine whether the pixel is corner,
edge or flat region.
i) Assume a window of size 3×3 centered at a location,
(x,y)
Harris matrix is
𝐼𝑥 2   𝐼𝑥𝐼𝑦
𝑀= ∑𝑤(𝑥, 𝑦) [   2 ]
𝐼𝑥𝐼𝑦   𝐼𝑦
𝑥,𝑦
Ix and Iy are derivatives in x and y directions in window
R = det{M} – k (trace {M})2
Det{M} = Ix2 Iy2 - Ixy2
Trace{M}=Ix2 +Iy2
Empirically determined value of k is 0.04 – 0.06
R is +ve and large for corner points
R is –ve and large magnitude for edge
Solution   |R| is small for flat region
ii)   Harris and Hessian detectors are rotation invariant
• Corner gets magnified and becomes bigger than the size of the
window by zooming. After scaling, corner points are classified
as edges
********** 3 **********
--- page 4 ---
Q3a
List the steps for extracting Scale-Invariant Feature Transform
CO- 2   (SIFT) features from an image, and describe keypoint localization in   [10]
SO- 1, 6
BL- 5   detail.
1. Construct a Scale Space:
• Generate images over multiple scales
• Ensures that features are scale-independent
2. Key point Localisation:
• Select key points based on measure of stability
• Ignore other key points to avoid false keypoints
3. Orientation Assignment:
• Compute best orientations for each key point region
• To ensure that keypoints are rotation invariant
4. Keypoint Descriptor:
• Use local image gradients at selected scale and rotation
(5M)
• Each pixel is compared with 26 other pixel values
•   Pixel marked x is compared with 26 other pixel values
•   If it is the highest positive or lowest negative among 26
neighbors (maxima or minima)
Solution   •   It is selected as a potential keypoint
•   Discard weak key points
• Normalize DoGs to get values in 0 -1 range
•   Set threshold to 0.03
• For DOG(x), x is coordinates of extrema (minima/maxima)
•   If DOG(x) < Threshold, discard it
•   Else retain it
•   Construct Hessian matrix at each potential keypoint to check
whether these points are good corner points not edge points
********** 4 **********
--- page 5 ---
Q3b
For Speeded-Up Robust Features (SURF), explain the scale space
CO- 2   generation for feature detection and justify in brief why it is   [10]
SO- 1, 6
BL- 1, 5   computationally efficient.
• For SURF, instead of reducing the size of image, filter size is
increased
• Computational complexity does not increase with the size of filter
• Because integral images and box filters are used
Solution
• Uses a number of octaves
• Each octave has a number of layers
For each octave and layer, image is filtered with second order
Gaussian Filter with higher and higher standard deviation
SURF achieves high speed due to:
• Use of integral images → fast computation
• Box filter approximation instead of Gaussian filters
• Scale-space via filter scaling, not image scaling
• Efficient Haar wavelet computations
Explain the Mean Shift clustering algorithm with reference to the
following aspects:
Q4a
i) The working procedure of the algorithm and criteria for
CO- 3   convergence   [10]
SO- 1, 6
ii) Effect of large and small bandwidth
BL- 2
iii) The advantages and limitations of Mean Shift
Support your explanation with a suitable example plots of data
points
Working of Mean Shift Algorithm
1. Choose a window (bandwidth) around a data point
2. Compute the mean of all points inside the window
3. Shift the window center to this mean
4. Repeat until the shift is very small
Solution   5. Points converging to the same location form a cluster
The algorithm stops when:
Shift in position is very small, or
The point reaches a stable mode (peak)
(4M)
********** 5 **********
--- page 6 ---
Bandwidth (window size) controls the radius of the neighborhood
• Large bandwidth → fewer clusters (smoother result)
• Small bandwidth → more clusters (detailed structure)
(2M)
Advantages
• No need to specify number of clusters
• Can detect arbitrarily shaped clusters
• Robust to noise
• Works well for density estimation
Limitations
•   Computationally expensive
•   Choice of bandwidth is critical
•   Not suitable for very high-dimensional data
• May merge nearby clusters if bandwidth is large
(4M)
Q4b
CO- 3   Describe how Gaussian Mixture model is used to generate   [10]
SO- 1,6   background model.
BL- 5
• Generate mixture of ‘k’ Gaussians distribution models for
each pixel of background frame
•   Values for ‘k’ is in the range 3 to 5
• Weight of each distribution is proportional to the amount of
time each color/intensity stays on that pixel
•   If a pixel has almost the same intensity for few consecutive
frames
• Weight of the Gaussian distribution of the pixel is more
• This pixel is a background pixel
Solution   •   If weight of Gaussian distribution of a pixel is low, that pixel
classified as a foreground pixel
Video frames   Background model
Q5a
Show the concept of optical flow. Compare dense and sparse optical
CO- 3   [10]
SO- 1,6   flow with suitable example images.
BL- 4
********** 6 **********
--- page 7 ---
•   If there is a relative motion between the camera and the
objects in the scene
•   Points of objects move in consecutive frames of video
•   Velocity vectors for these points in consecutive frames
is optic flow
•   It describes movement of objects
•   Optical flow is used for a series of frames of a video that
have a small time step between them
•   Calculates velocity of points between consecutive frames
• And provides an estimation of location of points in the next
image sequence
Solution
(4M)
Sparse optical flow
•   Is flow vectors of interest points of frames
•   Interest points could be edges or corners of object in a frame
Dense optical flow
•   Provides flow vectors of all pixels
• Has one flow vector per pixel
• Has higher accuracy
•   Is slow and computationally expensive
(4M)
(2M) for images
Q5b
Describe how background frame is generated using temporal average.
CO- 3   Also show how background subtraction is used generate foreground   [10]
SO- 1,6
BL- 5   of the image.
Solution
********** 7 **********

[Text in pictures on this page, read by OCR]
Compute running average over the previous frames
1 n-1
Bayt) ==) IGy.t i) [B(xy.t)I(xy.t)| > th
i=0

If difference at a location less than threshold, then pixel at that location is
background pixel
Else it is mapped as a foreground pixel
New object introduced in the current frame becomes a part of foreground
Current frame holds the newly introduced object and background
Background can also be generated by assigning weights

B(x,y)=(1-a)B(x,y) + a I(x,y)
--- page 8 ---
Q6a
Explain any five challenges of implementing a cereal grain inspection
CO- 4   [10]
SO- 1,6   system using computer vision.
BL- 2
Grain Variability
Shape and Size Variation: Cereal grains often come in varying sizes,
shapes, and orientations. This variation complicates consistent feature
extraction and classification.
Color Variability: Different grains have varying colors, and even within
the same type of grain, ripeness or moisture content can lead to color
changes. Lighting conditions further exacerbate this issue.
Texture Differences: Grain surfaces may differ in texture due to natural
variations or handling. Identifying features based on texture requires
advanced techniques like Local Binary Patterns (LBP) or more complex
CNN models.
2. Imaging Conditions
Lighting Conditions: Changes in lighting, shadows, and reflections during
image capture can significantly affect the quality and consistency of
images. Ensuring uniform lighting in an industrial setting is difficult,
leading to potential inaccuracies.
Background Noise: Separating grain from the background, particularly in
bulk storage or conveyor systems, is challenging. This requires robust
segmentation algorithms to isolate grains accurately.
Solution   Motion Blur: In real-time inspection systems, grains may be moving on
conveyors, leading to motion blur, which can affect image clarity and
reduce the system’s accuracy.
3. Object Detection and Classification
Identifying Defects and Foreign Objects: Detecting small defects or
foreign objects like stones, chaff, or weed seeds requires high-resolution
imaging and fine-tuned detection algorithms, often necessitating complex
deep learning models.
Data Annotation: Training a machine learning model to detect grain
defects or classify different grains requires a large labeled dataset.
Labeling this data can be time-consuming and error-prone.
Grain Overlapping and Occlusion: In bulk inspection scenarios, grains
may overlap, which hinders accurate detection and feature extraction.
4. High Throughput Requirements
Real-time Processing: In industrial applications, grains often move at high
speeds on conveyor belts. Implementing a system that can process
images in real-time, while maintaining high accuracy, is a major
computational challenge.
********** 8 **********
--- page 9 ---
Efficient Algorithms: The system needs to balance accuracy and speed,
especially when dealing with large datasets or high-resolution images.
Lightweight yet accurate models like MobileNet or EfficientNet are
essential for industrial scalability.
5. Data and Model Generalization
Domain Adaptation: A model trained in a controlled lab environment
might not generalize well to field or real-world scenarios due to changes
in lighting, grain quality, or background noise.
Handling Different Grain Types: Cereal grain systems must handle
various grains like wheat, rice, corn, and barley. Training a model to
generalize across different grain types while retaining accuracy can be
difficult.
6. Moisture and Damage Detection
Detecting Internal Defects: Image processing systems typically analyze
external features, making it hard to detect internal defects like moisture
content or fungal infections, which might require more advanced imaging
techniques like X-ray or NIR (Near-Infrared).
Subtle Differences in Damaged Grains: Differentiating between slightly
damaged grains and healthy grains may be challenging, especially when
damage does not significantly alter visible features.
7. Cost and Scalability
Hardware Costs: High-resolution cameras, lighting setups, and
computing power for real-time image processing add significant costs to
implementing a system. Industrial scalability, in terms of processing large
volumes of grains, can further increase costs.
Maintaining System Accuracy Over Time: The system’s performance
might degrade over time due to hardware wear, lighting changes, or grain
quality variations, requiring continuous calibration and maintenance.
(5M) for key points
(5M) for description
Show how 2D Cartesian coordinates are converted to 3D
Q6b
homogeneous coordinates and vice versa. Convert the point (3,4)
CO- 4   from Cartesian to homogeneous form. Also, determine the   [10]
SO- 1,6
BL- 5   corresponding 2D Cartesian coordinates for the homogeneous point
(9,12,3).
********** 9 **********
--- page 10 ---
Solution
(4M)
(4M)
2D point, (3,4) to Homogeneous point is (3,4,1)
3D point (9,12,3) 2D point is (3,4)
(2M)
Q7a   Explain in brief the following:
CO- 4   • World coordinate system   [10]
SO- 1, 6
BL- 3   • Camera coordinate system
********** 10 **********

[Text in pictures on this page, read by OCR]
¢ All the points from origin to ‘p’ along line are equivalent to one another
* Each point on line except origin is homogeneous coordinate of p = (x,y)
* Cartesian to homogeneous, p > p

BLS »=(5
a

By
--- page 11 ---
• Image coordinate system
•   Pixel coordinate system
Solution
(3M) each for the description of World and camera coordinate
system (2M) each image and pixel coordinate systems
Q7b   Draw a labeled sketch of epipolar geometry and explain it with
CO- 4   reference to points, epipolar lines, and the essential and fundamental   [10]
SO- 1,6
BL- 3   matrices.
(5M)
Solution
(5M)
********** 11 **********

[Text in pictures on this page, read by OCR]
* Standard epipolar geometry setup involves two cameras observing the same 3D
point P

* Cameras are located at O, and O,

* Projection of point, P, on the image planes is located at p and p’ respectively

epipolar plane Image planes

oO, \ 2

epipolar line for p’ baseline
````
