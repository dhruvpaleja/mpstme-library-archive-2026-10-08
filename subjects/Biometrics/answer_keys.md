# Biometrics: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 4e3887856929

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_AIDS_7056/Biometrics/ANS_Biometrics(702CO0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: text (14 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: III/Semester V(Exam Year: 2025-2026)
Subject: Biometrics
Date: 03 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 14 pages.
2. Question No. _1_ is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all _5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Section A (Compulsory Question)   Marks
CO-2,3, a   Identify key features in fingerprint recognition and explain their significance in   5
SO-1,   reducing false matches.
BL-2
Mark Bifurcation
1. Listing key features – 2 marks
2. Explaining their significance – 3 marks
Answer (Brief)
Key Features (2 marks):
1. Minutiae points – ridge endings and bifurcations
2. Ridge patterns – loops, whorls, and arches
3. Ridge count and orientation – number and direction of ridges between
minutiae
4. Pore structure (in high-resolution scans)
Significance (3 marks):
• These unique and stable features enable precise matching between enrolled
and probe fingerprints.
• Minutiae-based comparison reduces false matches by focusing on geometric
relations rather than whole-image similarity.
• Ridge and pore analysis further distinguishes similar patterns, enhancing
accuracy and reliability of identification.
********** 1 **********
--- page 2 ---
CO–4, b   Illustrate a multimodal biometric system combining iris and face recognition for   5
SO-2,   secure building access.
BL-2
Mark Bifurcation
1. System components and workflow – 3 marks
2. Security and accuracy benefits – 2 marks
Answer (Brief)
System Workflow (3 marks):
1. Data Acquisition: Cameras capture face and iris images at the entry point.
2. Feature Extraction: Distinctive facial geometry and iris texture patterns are
extracted.
3. Fusion Module:
o Score-level fusion combines match scores from both modalities.
o Access is granted only if the combined score exceeds the security
threshold.
4. Decision & Access Control: Integrated system unlocks the door if identity is
verified.
Benefits (2 marks):
• Higher accuracy: Reduces false acceptance/rejection by using two independent
traits.
• Spoof resistance: Difficult to forge both modalities simultaneously, enhancing
security.
CO-3, c   Differentiate between genuine and imposter users and explain the role of ground   5
SO-6,   truth in system evaluation.
BL-2
Mark Bifurcation
1. Difference between genuine and imposter users – 2 marks
2. Role of ground truth in evaluation – 3 marks
Answer (Brief)
Difference (2 marks):
• Genuine User: The person whose biometric data matches their enrolled
template.
• Imposter User: A person attempting authentication using another individual’s
biometric data.
Role of Ground Truth (3 marks):
• Ground truth is the verified identity label used to determine whether a match
is correct or incorrect.
•   It enables accurate calculation of performance metrics such as False Accept
Rate (FAR) and False Reject Rate (FRR).
• Ensures the biometric system is objectively evaluated by comparing system
output with true identity data.
CO-1,3, d   Compare iris and fingerprint recognition systems in terms of accuracy, speed, and   5
SO-4,   practical implementation.
BL-2,3
********** 2 **********
--- page 3 ---
Mark Bifurcation
Comparison points (accuracy, speed, implementation) – 5 marks
Parameter   Iris Recognition   Fingerprint Recognition
Very high – unique iris   Moderate to high – affected by
patterns give low false match   skin conditions and sensor
Accuracy   rate   quality
Slower – requires precise eye
alignment and high-resolution   Faster – quick image capture
Speed   capture   and matching
Practical
Implement   Costlier and less user-friendly;   Economical, widely deployed
ation   used in high-security areas   in mobiles, ATMs, and offices
Section B (Attempt any four questions)
Q2.   a   A user enters a username into an online banking system, which then uses voice   5
CO-1,   recognition to confirm whether the speaker is the registered account holder.
SO-1,   Mention whether this is an identification or verification scenario with a brief
BL-4   explanation.
Mark Bifurcation
1. Correct classification (identification/verification) – 2 marks
2. Explanation and reasoning – 3 marks
Answer (Brief)
•   Verification Scenario (2 marks)
Explanation (3 marks):
• The system already knows the claimed identity (through username).
•   It performs one-to-one matching between the user’s live voice sample and
the stored voice template of that specific account.
• Purpose: to verify if the speaker truly matches the enrolled user, ensuring
secure authentication.
Q2.   b   What is the Daugman’s Rubber Sheet Model in iris recognition? Briefly explain its   5
CO-2,3,   purpose
SO-6,
BL-2
Mark Bifurcation
1. Definition of Daugman’s Rubber Sheet Model – 2 marks
2. Explanation of purpose and significance – 3 marks
Answer (Brief)
Definition (2 marks):
• Daugman’s Rubber Sheet Model is a mathematical model that normalizes the
iris region by mapping it from a circular shape to a fixed rectangular coordinate
system.
•   It represents each point in the iris as a pair of polar coordinates (r, θ).
Purpose (3 marks):
• Compensates for variations in pupil dilation, head tilt, and distance.
• Ensures that features are compared under a consistent scale and orientation.
• Enhances matching accuracy and robustness in iris recognition systems.
Q2.   c   Biometric systems often encounter uncertainty during model development and   5
CO-3,   deployment. Discuss how epistemic and aleatoric uncertainty arise in such systems
********** 3 **********
--- page 4 ---
SO-2,   and explain how each type influences model performance and decision-making.
BL-2   Support your answer with one example for each type.
Mark Bifurcation
1. Definition of both uncertainty types – 2 marks
2. Impact on model performance and decision-making – 2 marks
3. Example for each type – 1 mark
Answer (Brief)
1. Epistemic Uncertainty (Model Uncertainty) – 2 marks
•   Arises due to limited knowledge or incomplete training data.
• Can be reduced by collecting more diverse and representative data.
•   Influence: Causes the model to make incorrect predictions for unseen or rare
biometric patterns.
• Example: A face recognition system misclassifies users from underrepresented
ethnic groups due to biased training data.
2. Aleatoric Uncertainty (Data Uncertainty) – 2 marks
•   Results from inherent randomness or noise in sensor data.
• Cannot be eliminated but can be modelled or mitigated.
•   Influence: Leads to fluctuating confidence in recognition under changing
environmental conditions.
• Example: Fingerprint recognition errors due to moisture or dirt on the sensor
surface.
Q2.   d   Analyze the advantages and disadvantages of using biometrics in surveillance systems   5
CO-3,   with respect to privacy concerns.
SO-4,
BL-3
Mark Bifurcation
1. Advantages – 2.5 marks
2. Disadvantages (Privacy concerns) – 2.5 marks
Answer (Brief)
Advantages (2.5 marks):
• Provides accurate and automated identification in real-time surveillance.
• Enhances public safety and supports crime prevention.
• Reduces human error and improves operational efficiency in monitoring.
Disadvantages / Privacy Concerns (2.5 marks):
• Raises privacy violations due to tracking without consent.
•   Potential data breaches or misuse of biometric databases.
• Can lead to mass surveillance, profiling, and loss of individual anonymity.
Q3.   a   A leading multinational bank is implementing a multimodal biometric authentication   10
CO-4,   system at its ATM network. The system combines fingerprint and iris recognition to
SO-2,   ensure high security. During pilot testing, the bank observed that while iris recognition
BL-4
reduces false matches, fingerprint sensors fail occasionally due to wet or worn
fingerprints.
Answer the following:
a) Construct a workflow diagram showing how feature-level and score-level fusion
will be applied in the system.
b) Recommend strategies to handle errors and inconsistencies between the two
modalities, considering practical deployment challenges.
Mark Bifurcation
a) Workflow diagram with explanation – 5 marks
b) Error handling and deployment strategies – 5 marks
********** 4 **********
--- page 5 ---
Answer (Brief)
a) Workflow Diagram (5 marks)
Multimodal Authentication Workflow:
1. Data Acquisition:
o Capture fingerprint and iris images simultaneously.
2. Preprocessing:
o Noise removal, segmentation, and normalization of both modalities.
3. Feature Extraction:
o Extract minutiae points from fingerprints and texture patterns from the
iris.
4. Fusion Approaches:
o Feature-level fusion: Combine extracted features into a joint vector for
matching.
o Score-level fusion: Independently match each modality → generate
matching scores → apply weighted combination (e.g., 70% iris + 30%
fingerprint).
5. Decision Module:
o   If fused score ≥ threshold → Access Granted, else Access Denied.
b) Error Handling and Deployment Strategies (5 marks)
• Sensor Quality Control: Use moisture-resistant fingerprint sensors and guide
users to wipe fingers before scanning.
• Adaptive Fusion: Increase weight of iris score when fingerprint data quality is
poor.
•   Fallback Mechanism: Allow single-modality verification (iris only) during
fingerprint sensor failure.
• Template Update: Periodically update fingerprint templates to account for skin
changes.
• User Feedback Interface: Provide clear prompts for re-scans and quality issues.
•   Security Measures: Encrypt multimodal templates and use liveness detection to
prevent spoofing.
b   The Metropolitan Security Department has introduced a facial-recognition–based   10
entry system for employees accessing a restricted data center. The system classifies
individuals as Authorized or Unauthorized based on facial matching probabilities.
The recorded data for 10 employees are given below:
Employee   Ground Truth   Probability
ID   of
Authorized
Access
Q3.
CO-3,   1   Authorized   0.93
SO-6,   2   Unauthorized   0.25
BL-4   3   Authorized   0.87
4   Unauthorized   0.42
5   Authorized   0.79
6   Unauthorized   0.33
7   Authorized   0.72
8   Unauthorized   0.15
9   Unauthorized   0.10
10   Authorized   0.90
********** 5 **********
--- page 6 ---
Questions-
1. Compute the True Positives (TP), False Positives (FP), True Positive Rate (TPR),
and False Positive Rate (FPR).
2. Use the computed values to plot the ROC curve.
Mark Bifurcation
a) Computation of TP, FP, TPR, FPR – 8 marks
b)ROC plot– 2 marks
Employ   Probability of
ee ID   Ground Truth   Authorized Access   TP   FP   TPR   FPR
1   Authorized   0.93   1   0   0.2   0
10   Authorized   0.9   2   0   0.4   0
3   Authorized   0.87   3   0   0.6   0
5   Authorized   0.79   4   0   0.8   0
7   Authorized   0.72   5   0   1   0
4   Unauthorized   0.42   5   1   1   0.2
6   Unauthorized   0.33   5   2   1   0.4
2   Unauthorized   0.25   5   3   1   0.6
8   Unauthorized   0.15   5   4   1   0.8
9   Unauthorized   0.1   5   5   1   1
Q4.   a   A hospital wants to implement a biometric system to monitor staff attendance and   10
CO-2,3,   access to sensitive patient data. During trials, it was observed that some staff
SO-4,   members’ fingerprints are worn due to manual labor, and voice recognition struggles
BL-4   in noisy environments. Using this scenario, explain the limitations and advantages
of behavioral and physiological biometric traits. Recommend a possible multimodal
solution to overcome these challenges.
Mark Bifurcation
Advantages – 3 Marks
Limitations – 3 Marks
Multimodal Recommendation – 4 Marks
Answer (10 Marks)
1. Advantages of Biometric Traits (3 marks)
•   Physiological traits (e.g., fingerprint, iris, face):
o Unique and difficult to forge.
o Relatively stable over time.
o Easy to use for fast identification.
********** 6 **********
--- page 7 ---
•   Behavioural traits (e.g., voice, gait, signature):
o Can be captured without physical contact.
o Useful where physiological traits are worn or damaged.
o Reflects user behavior, adding an extra layer of security.
2. Limitations of Biometric Traits (3 marks)
•   Physiological traits:
o Fingerprints may be worn in manual laborers → reduced recognition
accuracy.
o Illumination or camera quality can affect facial recognition.
•   Behavioral traits:
o Voice recognition affected by background noise or illness.
o Signature or gait may vary with stress or injury, reducing reliability.
3. Recommended Multimodal Solution (4 marks)
• Combine physiological and behavioral traits to improve accuracy and reliability:
o Use fingerprint or iris scanning for staff with intact fingerprints.
o Use voice or facial recognition as a secondary factor, especially in noisy
environments or for worn fingerprints.
o Implement score-level or decision-level fusion to confirm identity if one
modality fails.
o Optional: Include access logs or ID cards as a fallback for extreme cases.
b   “A national bank introduces multimodal biometric authentication (fingerprint +   10
Q4.   voice) for mobile transactions. Some customers report inconsistent authentication
CO-1,3,   success rates during calls in noisy environments”. Analyze the possible technical
SO-5,
BL-3   and environmental causes of this issue and recommend strategies to enhance
reliability.
Marks Allocation:
•   Technical Causes: 3
• Environmental Causes: 2
• Recommendations: 5
Answer (10 Marks)
1. Possible Technical Causes (3 marks)
• Poor microphone quality or mobile device limitations affecting voice capture.
•   Fingerprint sensor issues (dirty, wet, or worn fingers).
•   Inadequate signal processing or feature extraction algorithms.
•   Incompatibility of voice recognition system with background noise.
2. Possible Environmental Causes (2 marks)
• High ambient noise during calls (crowded areas, traffic, and machinery).
• Users speaking softly or under stress.
•   Finger conditions (wet, oily, or dry skin) reducing sensor accuracy.
3. Recommended Strategies to Enhance Reliability (5 marks)
• Noise reduction techniques: Use advanced signal processing to filter background
noise for voice.
• Adaptive algorithms: Employ robust voice recognition models that handle varying
environments.
•   Fallback mechanisms: Allow alternative authentication (OTP, PIN, fingerprint
only) if one modality fails.
• Multimodal fusion: Use score-level or decision-level fusion to combine
fingerprint and voice scores for higher accuracy.
• User guidance: Provide instructions for proper finger placement and clear speech
during authentication.
********** 7 **********
--- page 8 ---
Q5.   a   The Smart University recently installed a multimodal biometric system to control   10
CO-4,   access to its research labs. The system uses fingerprint and iris recognition. During
SO-6,   testing, the following false match rates were recorded: Fingerprint FMR = 4%, Iris
BL-3   FMR = 3%.
Using OR fusion
a) Calculate the overall FMR.
b) If 500 impostor attempts are made, compute the expected number of false
acceptances.
Mark Bifurcation
(a) Calculate overall FMR (5 marks)
(b) Expected false acceptances (5 marks)
********** 8 **********
--- page 9 ---
b   What is confidence interval?   10
Q5.   A university is using face recognition for student attendance. During exams, students
CO-3 ,   attempted to bypass the system by wearing masks, which resulted in higher false non-
SO-7 ,   match rates (FNMR). The university wants to improve system reliability and
BL-1,4
understand systematic and sampling errors in current performance evaluation. Suggest
improvements in system calibration to reduce FNMR, considering real-world
constraints like lighting and camera placement.
Marks Bifurcation
Definition CI – 2 Marks
Improving system calibration – 8 Marks
Confidence Interval (2 Marks):
A confidence interval (CI) is a statistical range, derived from sample data, that estimates
where the true population parameter (e.g., mean accuracy or FNMR) is likely to fall, with
a specified confidence level (e.g., 95%). It reflects the precision and reliability of
performance estimates in biometric evaluations.
Improving System Calibration to Reduce FNMR (8 Marks):
1. Dataset Recalibration:
o Collect new samples including masked and partially occluded faces to
represent real-world exam conditions.
o Use stratified sampling to avoid bias toward easy (unmasked) cases.
2. Algorithm Enhancement:
o   Integrate mask-aware or multimodal recognition (e.g., combine facial and
iris features).
o Retrain the model with data augmentation for varied lighting, angles, and
occlusions.
3. System Calibration:
o Adjust decision thresholds using ROC/DET analysis to balance False
Match and False Non-Match rates.
o Regularly validate thresholds under realistic scenarios to maintain optimal
sensitivity.
4. Environmental Adjustments:
o Improve lighting uniformity and reduce glare/shadows.
o Ensure camera placement at consistent angles and heights for uniform
capture.
5. Continuous Monitoring:
o Implement periodic re-evaluation and feedback-based recalibration.
o Use confidence intervals to monitor statistical variation and ensure stable
performance over time.
Q6.   a   Illustrate with examples how variations in user interaction with sensors, like   10
CO-1,   occluded iris or partial fingerprints, contribute to intra-class variations. Suggest
SO-1,   preprocessing techniques to reduce these effects.
BL-3
Marks Bifurcation
• Concept and Examples of Intra-Class Variation – 5 Marks
• Preprocessing Techniques to Reduce Effects – 5 Marks
1. Concept and Examples of Intra-Class Variation (5 Marks):
********** 9 **********
--- page 10 ---
•   Intra-class variation refers to differences in biometric data from the same user
due to inconsistent sensor interaction or environmental factors.
• Examples:
o Occluded Iris: Eyelids, eyelashes, or glasses partially covering the iris
lead to incomplete feature capture.
o Partial Fingerprints: Incomplete finger placement or dry skin reduces
ridge details.
o Face Recognition: Variations in pose, expression, or illumination alter
captured features.
2. Preprocessing Techniques to Reduce Effects (5 Marks):
• Normalization: Adjust brightness, contrast, and scale for consistent image
quality.
• Segmentation: Isolate clear regions (e.g., unoccluded iris portion, central
fingerprint area).
• Image Enhancement: Apply filters (e.g., Gabor, histogram equalization) to
improve feature clarity.
• Alignment: Rotate/translate images to correct misplacement before feature
extraction.
•   Quality Assessment: Reject or re-acquire low-quality samples automatically.
b   Explain the concept of fingerprint indexing and its role in accelerating fingerprint   10
identification. Discuss how minutiae points are used to generate feature vectors,
including the use of triplets (refer figure) and their geometric properties.
Q6.
CO-2,3,
SO-6,
BL-2
Marks Bifurcation
• Concept and Role of Fingerprint Indexing – 5 Marks
• Use of Minutiae Triplets and Feature Vector Generation – 5 Marks
1. Concept and Role of Fingerprint Indexing (5 Marks):
•   Fingerprint indexing is a technique used to speed up the identification process in
large fingerprint databases by organizing and searching data efficiently before
detailed matching.
•   Instead of comparing a query fingerprint with every stored template, indexing
narrows down candidate lists based on shared structural or statistical features.
•   Role:
o Reduces computational cost and search time.
o Enables real-time identification in large-scale systems (e.g., border
control, law enforcement).
o Acts as a pre-filtering stage before fine-grained minutiae matching.
2. Use of Minutiae Triplets and Feature Vector Generation (5 Marks):
********** 10 **********
--- page 11 ---
• Minutiae points (ridge endings and bifurcations) represent the core fingerprint
features.
• To create robust and rotation-invariant feature vectors:
o Select triplets of minutiae forming a triangle.
o Extract geometric properties such as:
▪   Side lengths between minutiae.
▪   Internal angles of the triangle.
▪   Orientation of ridges relative to a reference minutia.
• These triplet features are encoded into a feature vector representing spatial
relationships uniquely for indexing and matching.
Q7.   a   A banking security system integrates fingerprint and iris recognition modules to ensure   10
CO-1,3,   secure and reliable customer authentication. Unlike a simple logical rule-based
SO-2,   approach, the system employs a score-level weighted fusion strategy, where each
BL-4   biometric modality contributes to the final decision based on its reliability. The
fingerprint recognition subsystem, known for its high consistency, is assigned a weight
of 0.6, while the iris recognition subsystem, though slightly less consistent, is given a
weight of 0.4. The performance accuracies of the individual systems are 95% for
fingerprint recognition and 90% for iris recognition. During evaluation, the system
processed 1000 genuine user attempts and 600 impostor attempts, using a fusion
threshold of 0.8 (on a normalized 0–1 scale) for final acceptance.
Based on above statements do the following-
(a) Calculate the expected fused accuracy of the multimodal system using the
weighted average model.
(b) Determine the expected number of correct genuine matches and false rejections
resulting from this fusion scheme.
(c) Compute the expected number of correct impostor rejections and false
acceptances, and interpret how the weighting strategy influences the trade-off between
system security and user convenience.
Marks Bifurcation (10 Marks):
•   Calculation of Fused Accuracy – 3 Marks
• Genuine Matches and False Rejections – 2 Marks
• Impostor Rejections and False Acceptances, Interpretation – 5 Marks
Given Data:
•   Fingerprint accuracy = 95% → 0.95
•   Iris accuracy = 90% → 0.90
• Weights: Fingerprint = 0.6, Iris = 0.4
• Fusion threshold = 0.8
• Genuine attempts = 1000
• Impostor attempts = 600
********** 11 **********
--- page 12 ---
b   TechVille University has deployed a new fingerprint recognition system to automate   10
access to its laboratories. To test its accuracy, the IT team conducted a pilot study with
400 students, each providing a fingerprint sample. For each probe, the system returned
a ranked list of candidate matches. The number of genuine matches observed at each
of the top 10 ranks is given below:
Rank of   Number of
Genuine   Students
Match   Matched
R1   220
R2   50
Q7.   R3   40
CO-3,
SO-7,   R4   30
BL-4   R5   20
R6   15
R7   10
R8   10
R9   5
R10   0
Tasks:
1.   Compute the cumulative number of genuine matches at each rank.
2.   Calculate the cumulative recognition percentage for ranks R1 to R10.
3.   Plot the Cumulative Match Characteristics (CMC) curve.
4.   Identify the rank at which 85% of students are correctly identified.
5.   Analyze the system’s performance, focusing on the rank-1 recognition and
suggesting possible improvements.
********** 12 **********
--- page 13 ---
Marks Bifurcation (10 Marks):
• Cumulative Matches and Recognition Percentage – 4 Marks
• CMC Curve Plot – 2 Marks
• Rank for 85% Identification & Performance Analysis – 4 Marks
1. Cumulative Number of Genuine Matches (4 Marks)
Rank Cumulative Matches
R1   220
R2   220 + 50 = 270
R3   270 + 40 = 310
R4   310 + 30 = 340
R5   340 + 20 = 360
R6   360 + 15 = 375
R7   375 + 10 = 385
R8   385 + 10 = 395
R9   395 + 5 = 400
R10 400 + 0 = 400
2. Cumulative Recognition Percentage (%)
Rank Recognition %
R1   220/400 × 100 = 55%
R2   270/400 × 100 = 67.5%
R3   310/400 × 100 = 77.5%
R4   340/400 × 100 = 85%
R5   360/400 × 100 = 90%
R6   375/400 × 100 = 93.75%
R7   385/400 × 100 = 96.25%
R8   395/400 × 100 = 98.75%
R9   400/400 × 100 = 100%
R10 400/400 × 100 = 100%
3. CMC Curve (2 Marks)
X-axis: Rank (R1 to R10)
Y-axis: Cumulative Recognition Percentage (%)
********** 13 **********
--- page 14 ---
5. Performance Analysis and Suggestions (2 Marks)
Rank-1 Recognition: 55% → Only 220 out of 400 students correctly matched at top
rank.
Implications: Moderate system reliability for single-attempt access.
Suggestions to Improve Performance:
Enhance fingerprint image quality (better sensors, cleaning).
Use advanced matching algorithms with better tolerance for rotation and partial prints.
Implement multi-sample averaging (capture multiple samples per student).
Apply preprocessing like noise reduction, ridge enhancement.
********** 14 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 91d1c414ab75

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/Biometrics/ANS_Biometrics(702CO0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Biometrics
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. 1.   Question No. _1_ is compulsory.
3. 2.   Out of remaining questions, attempt any 4 questions.
4. 3.   In all _5_ questions to be attempted.
5. 4.   All questions carry equal marks.
6. 5.   Answer to each new question to be started on a fresh page.
7. 6.   Figures in brackets on the right hand side indicate full marks.
8. 7.   Assume Suitable data if necessary.
Q1   Section A (Compulsory Question)   Marks
CO-2,3, a   Identify and explain the functional components of a biometric system. Discuss   5
SO-1,   their role in ensuring reliable authentication.
BL-2
Marks Bifurcation (5 Marks)
. Functional components identification – 2 Marks
Explanation of components and their role in authentication – 3 Marks
Answer-
Functional Components of a Biometric System
A biometric system is used to identify or authenticate an individual based on
physiological or behavioral characteristics. The main functional components of a
biometric system are as follows:
1. Sensor Module
The sensor module captures the biometric data of the user such as fingerprint,
face image, iris image, or voice sample. The quality of captured data directly
affects the accuracy of the system.
2. Pre-processing Module
This module improves the quality of the captured biometric data by removing
noise, enhancing image quality, and normalizing the data so that it can be
processed properly.
3. Feature Extraction Module
In this stage, unique features are extracted from the biometric data. For example,
minutiae points in fingerprint, iris texture patterns, or facial feature points are
extracted and converted into a feature vector.
4. Template Database
The extracted features are stored in the database as biometric templates. These
templates are used later for comparison during authentication.
5. Matching Module
The matching module compares the extracted features with stored templates in
the database and calculates a matching score to determine similarity.
6. Decision Module
The decision module accepts or rejects the user based on the matching score and
a predefined threshold value.
********** 1 **********
--- page 2 ---
Role in Reliable Authentication
These components work together to ensure reliable authentication. Proper data
acquisition, accurate feature extraction, and efficient matching reduce false
acceptance and false rejection rates, thereby improving the accuracy, security,
and reliability of the biometric system.
CO–4, b   Define multimodal biometric systems. Explain how fusion of multiple modalities   5
SO-2,   improves system robustness.
BL-2
Marks Bifurcation (5 Marks)
1. Definition of Multimodal Biometric System – 2 Marks
2. Explanation of fusion and improvement in robustness – 3 Marks
Answer-
Multimodal Biometric System
A multimodal biometric system is a biometric system that uses more than one
biometric trait for identification or authentication. Instead of relying on a single
biometric trait such as fingerprint or face, the system combines multiple traits like
fingerprint, face, iris, or voice to improve accuracy and reliability.
Examples include:
• Face + Fingerprint
•   Iris + Fingerprint
• Voice + Face Recognition
Fusion and System Robustness
In multimodal biometric systems, fusion refers to the process of combining
information from multiple biometric sources. Fusion can be performed at different
levels such as sensor level, feature level, score level, or decision level.
Fusion improves system robustness in the following ways:
• Improves accuracy by combining multiple biometric traits
• Reduces false acceptance rate (FAR) and false rejection rate (FRR)
•   Provides better security because multiple traits must match
• Works even if one biometric trait fails due to noise or poor quality
• Reduces spoofing attacks since it is difficult to fake multiple biometric traits
CO-3, c   Explain the significance of performance parameters such as FAR, FRR, and   5
SO-6,   threshold in biometric systems.
BL-2
Marks Bifurcation (5 Marks)
1. Definition of FAR, FRR, and Threshold – 2 Marks
2. Significance of these performance parameters in biometric systems – 3
Marks
Answer-
Performance Parameters in Biometric Systems
Biometric systems are evaluated using performance parameters such as False
Acceptance Rate (FAR), False Rejection Rate (FRR), and Threshold. These
parameters help measure the accuracy and reliability of the biometric system.
1. False Acceptance Rate (FAR)
FAR is the probability that the biometric system incorrectly accepts an
unauthorized   person   as   an   authorized   user.
A high FAR means the system is less secure because impostors may gain access.
2. False Rejection Rate (FRR)
FRR is the probability that the biometric system incorrectly rejects an authorized
user.
A high FRR means the system is less user-friendly because genuine users are
denied access.
********** 2 **********
--- page 3 ---
3. Threshold
Threshold is the decision value used to accept or reject a user based on the
matching score.
•   If the matching score is above the threshold, the user is accepted.
•   If the matching score is below the threshold, the user is rejected.
Changing the threshold affects FAR and FRR:
•   Increasing threshold → decreases FAR but increases FRR
• Decreasing threshold → decreases FRR but increases FAR
Significance
These parameters are important because they help balance security and usability
of biometric systems. A good biometric system maintains low FAR and low FRR
by selecting an optimal threshold value.
CO-1,3, d   Discuss applications of biometrics in large-scale surveillance systems. Highlight   5
SO-4,   associated benefits and concerns.
BL-2,3
Marks Bifurcation (5 Marks)
1. Applications of biometrics in large-scale surveillance systems – 2 Marks
2. Benefits and concerns associated with biometric surveillance – 3 Marks
Answer
Applications of Biometrics in Large-Scale Surveillance Systems
Biometrics is widely used in large-scale surveillance systems for identification
and monitoring of individuals in public and secure areas. Some major applications
include:
1. Airport and Border Security – Face recognition and iris recognition are used
to identify passengers and detect criminals or unauthorized persons.
2. Law Enforcement and Criminal Identification – Police use fingerprint and
face recognition databases to identify suspects and missing persons.
3. Public Surveillance Systems – Face recognition cameras are used in public
places such as railway stations, malls, and smart cities for monitoring
activities.
4. Access Control in Government and Military Areas – Biometric
authentication is used to allow access only to authorized personnel.
5. National ID Systems – Large-scale biometric databases are used for
identification systems such as Aadhaar.
Benefits of Biometric Surveillance
• Improves security and crime prevention
• Helps in fast identification of criminals and suspects
• Reduces identity fraud
• Enables automated monitoring systems
•   Useful in large population management
Concerns and Issues
•   Privacy concerns and misuse of personal data
• Risk of data breaches and identity theft
•   Ethical issues related to continuous surveillance
•   Possibility of false identification
• High implementation cost
Section B (Attempt any four questions)
********** 3 **********
--- page 4 ---
Q2.   a   A biometric system verifies a user by comparing a fingerprint with a stored   5
CO-1,   template. State whether this is identification or verification and justify your
SO-1,   answer.
BL-4
Marks Bifurcation (5 Marks)
1. Identification vs Verification statement – 2 Marks
2. Justification with explanation of biometric process – 3 Marks
Answer
Identification or Verification
The given biometric system represents Verification, not Identification.
Justification
In biometric systems, there are two modes of operation:
1. Identification (1:N Matching)
In identification mode, the biometric sample is compared with all templates stored
in the database to determine the identity of the person. The system asks “Who are
you?”
2. Verification (1:1 Matching)
In verification mode, the biometric sample is compared with one stored template
associated with a claimed identity. The system asks “Are you who you claim to
be?”
In the given scenario, the system verifies a user by comparing a fingerprint with a
stored template. This indicates one-to-one comparison, which is verification.
Q2. b   Explain challenges in biometric data acquisition and how they affect system   5
CO-2,3,   performance. Give suitable examples.
SO-6,
BL-2
Marks Bifurcation (5 Marks)
1. Challenges in biometric data acquisition – 2 Marks
2. Effect on system performance with examples – 3 Marks
Answer
Challenges in Biometric Data Acquisition
Biometric data acquisition is the process of capturing biometric traits such as
fingerprint, face, iris, or voice using sensors. Several challenges occur during data
acquisition which affect system accuracy and performance.
Some common challenges include:
1. Poor Quality Sensors – Low-resolution sensors capture unclear biometric
images.
2. Environmental Conditions – Lighting, noise, temperature, and humidity
affect data capture.
3. User Cooperation – Improper finger placement, face angle, or movement
affects data quality.
4. Physical Changes – Injuries, aging, scars, or illness may change biometric
traits.
5. Noise and Distortion – Background noise in voice recognition or blur in face
images.
6. Occlusion – Face covered by mask, glasses, hair, etc.
Effect on System Performance
These challenges affect biometric system performance in the following ways:
•   Increase False Rejection Rate (FRR) when genuine users are rejected due to
poor data quality.
********** 4 **********
--- page 5 ---
•   Increase False Acceptance Rate (FAR) when unclear data matches
incorrectly.
• Reduce accuracy and reliability of the biometric system.
•   Increase processing time due to repeated data capture.
• Example:
o Wet or dirty fingers in fingerprint recognition may cause rejection.
o Low lighting in face recognition may cause incorrect identification.
o Background noise affects voice recognition accuracy.
Q2.   c   Illustrate the biometric system design cycle and explain each stage briefly.   5
CO-3,
SO-2,
BL-2
Marks Bifurcation (5 Marks)
1. Biometric system design cycle diagram / stages identification – 2 Marks
2. Explanation of each stage briefly – 3 Marks
Answer-
Biometric System Design Cycle
The biometric system design cycle consists of several stages involved in
developing and deploying a biometric authentication system. The cycle ensures
that the system is accurate, reliable, and secure.
Stages in Biometric System Design Cycle
1. Data Acquisition
In this stage, biometric data such as fingerprint, face, iris, or voice is collected
using sensors or cameras. The quality of captured data is important for system
performance.
2. Pre-processing
The captured biometric data is processed to remove noise, enhance image quality,
normalize the data, and prepare it for feature extraction.
3. Feature Extraction
Unique features are extracted from biometric data such as fingerprint minutiae
points, iris patterns, or facial features. These features represent the biometric trait.
4. Template Creation and Storage
The extracted features are stored in the database as biometric templates for future
comparison.
5. Matching
The extracted features from the input biometric sample are compared with stored
templates, and a matching score is generated.
6. Decision Making
Based on the matching score and threshold value, the system decides whether to
accept or reject the user.
7. Performance Evaluation
The system performance is evaluated using parameters such as FAR, FRR, and
accuracy,   and   the   system   may   be   improved   if   needed.
Data Acquisition → Pre-processing → Feature Extraction → Template Storage
→ Matching → Decision → Performance Evaluation
Q2. d   Compare unimodal and multimodal biometric systems including accuracy,   5
CO-3,   flexibility, and security.
SO-4,
BL-3
Marks Bifurcation (5 Marks)
1. Explanation of Unimodal and Multimodal biometric systems – 2 Marks
********** 5 **********
--- page 6 ---
2. Comparison based on accuracy, flexibility, and security – 3 Marks
Answer
Unimodal Biometric System
A unimodal biometric system uses only one biometric trait for authentication,
such as fingerprint, face, iris, or voice recognition. The system captures a single
biometric feature and compares it with the stored template for identification or
verification.
Examples: Fingerprint recognition system, Face recognition system.
Multimodal Biometric System
A multimodal biometric system uses more than one biometric trait for
authentication. It combines multiple biometric sources such as fingerprint and
face, iris and fingerprint, or voice and face recognition to improve system
performance.
Examples: Face + Fingerprint authentication, Iris + Fingerprint systems.
Comparison Between Unimodal and Multimodal Biometric Systems
Unimodal   Multimodal
Feature
Biometric   Biometric
Accuracy   Lower accuracy   Higher accuracy
Flexibility   Less flexible   More flexible
Security   Less secure   More secure
Higher FAR and   Lower FAR and
Error Rates
FRR   FRR
Cost   Low cost   High cost
System Complexity   Simple   Complex
Q3.   a   A healthcare organization plans to deploy a multimodal biometric system using   10
CO-4,   face and iris recognition. Answer the following:
SO-2,
BL-4
1.   Design a workflow illustrating feature-level and score-level fusion.
2.   Suggest mechanisms to handle inconsistencies between modalities.
Marks Bifurcation (10 Marks)
1.   Workflow for feature-level and score-level fusion (diagram/steps) – 5 Marks
2.   Mechanisms to handle inconsistencies between modalities – 5 Marks
Answer
Multimodal Biometric System (Face + Iris)
A multimodal biometric system combines multiple biometric traits to improve
accuracy, reliability, and security. In this system, face recognition and iris
recognition are used together.
1. Workflow for Feature-Level and Score-Level Fusion
(a) Feature-Level Fusion Workflow
********** 6 **********
--- page 7 ---
In feature-level fusion, features from face and iris are combined before matching.
Workflow Steps:
1.   Capture face image and iris image using sensors.
2.   Preprocess both images (noise removal, normalization).
3.   Extract features from face and iris separately.
4.   Combine feature vectors into a single feature vector.
5.   Store combined template in database.
6.   During authentication, extract features again and compare with stored
template.
7.   Matching score generated and decision taken.
Flow (Text Diagram)
Face Image → Feature Extraction →
→ Feature Fusion → Matching → Decision
Iris Image → Feature Extraction →
(b) Score-Level Fusion Workflow
In score-level fusion, matching scores from both modalities are combined.
Workflow Steps:
1.   Capture face and iris images.
2.   Extract features separately.
3.   Match face features with face template → Score 1.
4.   Match iris features with iris template → Score 2.
5.   Combine scores using sum rule, weighted sum, or average.
6.   Final score compared with threshold.
7.   Accept or Reject decision.
Flow (Text Diagram)
Face → Matching → Score 1
Iris → Matching → Score 2
Score Fusion → Final Score → Decision
2. Mechanisms to Handle Inconsistencies Between Modalities
In multimodal systems, sometimes one biometric modality may fail due to poor
quality data. The system should handle inconsistencies using the following
methods:
Mechanisms:
1.   Weighted Score Fusion
o   Assign higher weight to more reliable modality (e.g., iris more
reliable than face).
2.   Quality-Based Fusion
o   If face image quality is poor, give more importance to iris
recognition.
********** 7 **********
--- page 8 ---
3.   Fallback Mechanism
o   If one modality fails, system authenticates using the other modality.
4.   Adaptive Threshold
o   Threshold changes based on available modalities.
5.   Decision-Level Fusion
o   Final decision taken using AND/OR rules.
Example:
o   AND Rule → Both face and iris must match (high security)
o   OR Rule → Either face or iris match (high usability)
b A network security organization deploys a machine learning–based intrusion   10
detection system to monitor incoming traffic and classify activities as Normal or
Attack. The system generates probability scores indicating the likelihood of
normal behavior. During evaluation, it is observed that the dataset is highly
imbalanced, with significantly more normal traffic than attack instances.
Given the following classification results:
ID   Actual Class   Probability (Normal)
1   Normal   0.93
Q3.   2   Normal   0.88
CO-3,   3   Normal   0.82
SO-6,   4   Normal   0.79
BL-4
5   Normal   0.75
6   Normal   0.71
7   Attack   0.42
8   Normal   0.85
9   Normal   0.78
10   Attack   0.30
Compute TP, FP, TPR, and FPR. Plot ROC curve. Comment on performance
under severe class imbalance.
Marks Bifurcation (10 Marks)
1. TP, FP, TPR, FPR – 6 marks
2. ROC points / ROC curve – 3 Marks
3. Comment on class imbalance – 1 Mark
Answer
********** 8 **********
--- page 9 ---
FPR =
Step Actual   TP   FP   TPR = TP/8
FP/2
Start —   0   0   0   0
1   Normal 1   0   0.125   0
2   Normal 2   0   0.25   0
3   Normal 3   0   0.375   0
4   Normal 4   0   0.50   0
5   Normal 5   0   0.625   0
6   Normal 6   0   0.75   0
7   Normal 7   0   0.875   0
8   Normal 8   0   1   0
9   Attack   8   1   1   0.5
10   Attack   8   2   1   1
Comment on class imbalance – 1 Mark
Since the dataset contains more Normal samples than Attack samples, accuracy
alone may be misleading. ROC curve is a better performance measure for
imbalanced datasets. The ROC curve is close to the top-left corner, indicating
good classifier performance. However, class imbalance may cause the model to
favor the majority class (Normal), so evaluation should focus on TPR, FPR, and
ROC rather than accuracy.
Q4.   a   10
CO-2,3,
SO-4,
BL-4
Study the given iris processing images and answer the following:
a) Identify each stage shown in the images.
********** 9 **********
--- page 10 ---
b) Explain iris segmentation and its challenges.
c) Explain how iris codes are generated and used for authentication.
Ans   Marks Bifurcation (10 Marks)
a) Identify each stage shown in images – 3 Marks
b) Iris segmentation and its challenges – 4 Marks
c) Iris code generation and authentication – 3 Marks
Answer
(a) Identify Each Stage Shown in Iris Processing Images
The iris recognition process consists of the following stages typically shown in iris
processing images:
1. Iris Image Acquisition – Capturing the eye image using a camera.
2. Iris Segmentation – Detecting the iris region by locating the pupil and iris
boundaries.
3. Normalization – Converting the circular iris region into a rectangular form
using polar coordinates.
4. Feature Extraction / Iris Code Generation – Extracting texture features and
generating binary iris code.
5. Matching – Comparing iris code with stored template for authentication.
(b) Iris Segmentation and Its Challenges
Iris Segmentation
Iris segmentation is the process of isolating the iris region from the eye image by
detecting:
•   Pupil boundary
•   Iris outer boundary
•   Eyelids and eyelashes
Techniques used include:
•   Intergro Differential
•   Geodesic
The segmented iris region is then used for further processing.
Challenges in Iris Segmentation
1. Eyelid occlusion – Eyelids may cover part of iris.
2. Eyelashes interference – Eyelashes create noise.
3. Reflections – Light reflections on eye surface.
4. Poor image quality – Low resolution or blur.
5. Off-angle images – Eye not aligned properly.
6. Pupil dilation – Changes iris size.
These challenges may reduce recognition accuracy.
(c) Iris Code Generation and Authentication
After segmentation and normalization, features are extracted from iris texture.
Iris Code Generation
•   Filters such as Gabor filters or wavelets are used.
•   Iris texture is converted into a binary code (iris code).
• Each iris code is unique for each individual.
Authentication Process
1. Capture iris image.
2. Segment and normalize iris.
3. Generate iris code.
4. Compare iris code with stored template.
5. Matching is performed using Hamming Distance.
6.   If matching score is above threshold → Accept.
7. Otherwise → Reject.
Q4.   b   A university plans to implement biometric attendance. Some students have   10
CO-1,3,   worn
********** 10 **********
--- page 11 ---
SO-5,   fingerprints and inconsistent behaviour patterns. Analyze:
BL-3
1. Limitations of physiological and behavioural biometrics
2. Recommend a robust multimodal solution considering cost and usability
Marks Bifurcation (10 Marks)
1. Limitations of physiological biometrics – 3 Marks
2. Limitations of behavioural biometrics – 3 Marks
3. Recommendation of robust multimodal solution (cost & usability) – 4
Marks
Answer
1. Limitations of Physiological Biometrics
Physiological biometrics are based on physical characteristics such as
fingerprint, face, iris, and palmprint. These systems have some limitations:
• Worn fingerprints due to manual work, injuries, or aging may reduce
fingerprint recognition accuracy.
• Face recognition affected by lighting, pose, masks, or facial expressions.
• Iris recognition requires high-quality cameras and controlled environment.
• Sensor hygiene issues in fingerprint scanners.
• Hardware cost may be high for iris scanners.
• Failure to enroll may occur if biometric trait cannot be captured properly.
Thus, physiological biometrics may suffer from noise, environmental effects,
and physical changes.
2. Limitations of Behavioural Biometrics
Behavioural biometrics include signature, keystroke dynamics, voice
recognition, and gait recognition.
Limitations include:
• Behaviour changes over time.
• Voice affected by illness or noise.
• Signature may vary each time.
• Keystroke patterns change with mood, stress, or device.
• Less accurate compared to physiological biometrics.
• Higher False Rejection Rate (FRR).
Thus, behavioural biometrics are not always consistent and may reduce system
reliability.
3. Recommended Robust Multimodal Solution (Cost & Usability)
To handle worn fingerprints and inconsistent behaviour, a multimodal biometric
system should be implemented.
Recommended System:
Face Recognition + Fingerprint + RFID/ID Card
Reasons:
• Face recognition is contactless and fast.
• Fingerprint provides high accuracy.
• RFID/ID card acts as backup authentication.
• Multimodal system reduces FAR and FRR.
• Works even if one biometric fails.
• Cost is moderate compared to iris recognition systems.
• Usability is high for student attendance systems.
Fusion Method:
• Use Score-level fusion or Decision-level fusion.
********** 11 **********
--- page 12 ---
• Example:
o Face OR Fingerprint → Attendance marked
o Both match → High security mode
Q5.   a   Explain the concept of biometric identifiers and discuss their characteristics   10
CO-4,   such as universality, uniqueness, Collectability, Acceptability, Resistance to
SO-6,   Circumvention and permanence.
BL-3
Marks Bifurcation (10 Marks)
1. Concept of biometric identifiers – 5 Marks
2. Characteristics: Universality, Uniqueness, Permanence – 5 Marks
Answer
Concept of Biometric Identifiers
Biometric identifiers are measurable physiological or behavioral characteristics
that can be used to identify or verify the identity of an individual. These
identifiers are unique to each person and are used in biometric authentication
systems such as fingerprint recognition, face recognition, iris recognition,
voice recognition, and signature verification.
Biometric identifiers are used in security systems, attendance systems, banking
authentication, border control, and surveillance systems because they provide
reliable and secure identification.
Examples of biometric identifiers:
• Fingerprint
• Face
• Iris
• Retina
• Voice
• Signature
• Keystroke dynamics
• Gait
Characteristics of Biometric Identifiers
1. Universality
Universality means that every person should possess the biometric trait.
For example, every individual has a face and fingerprints, so these traits satisfy
universality. A biometric system cannot be effective if some people do not
have that trait.
Example: Fingerprint and face recognition satisfy universality.
2. Uniqueness
Uniqueness means that the biometric trait should be different for each
individual.
Even identical twins have different fingerprints and iris patterns. This property
helps in distinguishing one person from another.
Example: Iris patterns and fingerprints are highly unique.
3. Permanence
Permanence means that the biometric trait should remain stable over time and
should not change significantly with age or environment.
Example: Iris and fingerprint patterns remain stable for many years, while voice
and signature may change over time.
Q5.   b   Explain the concept of multimodal biometric systems and discuss how fusion   10
CO-3 ,   techniques improve system reliability and security.
********** 12 **********
--- page 13 ---
SO-7 ,
BL-1,4   A multimodal biometric system employs AND fusion by combining fingerprint
and iris recognition, where the fingerprint system has an accuracy of 90% and the
iris system has an accuracy of 95%. The system processes 1000 authorized access
attempts and 1000 unauthorized access attempts. Based on this information,
calculate the combined system accuracy under AND fusion. Further, determine
the number of false rejections and false acceptances produced by the system.
Marks Bifurcation (10 Marks)
1. Concept of multimodal biometric systems and fusion techniques – 5 Marks
2. AND fusion accuracy, false rejections, and false acceptances calculation –
5 Marks
Answer
Multimodal Biometric Systems and Fusion Techniques
A multimodal biometric system uses more than one biometric trait such as
fingerprint, face, iris, or voice for authentication. These systems improve
accuracy, reliability, and security compared to unimodal biometric systems
because multiple biometric traits are used for identification.
Fusion techniques are used to combine information from multiple biometric
systems. Fusion can be performed at different levels such as feature level, score
level, and decision level. Fusion improves system reliability by reducing False
Acceptance Rate (FAR) and False Rejection Rate (FRR). It also improves
security because it is difficult to spoof multiple biometric traits. Multimodal
systems also work even if one biometric trait fails due to noise or poor quality
data.
AND Fusion Calculation
Given:
•   Fingerprint accuracy = 90% = 0.9
•   Iris accuracy = 95% = 0.95
• Authorized attempts = 1000
• Unauthorized attempts = 1000
• Fusion type = AND fusion
********** 13 **********
--- page 14 ---
Q6.   a   A multimodal biometric system uses weighted fusion by combining face and   10
CO-1,   fingerprint recognition, where the face recognition system has an accuracy of 92%
SO-1,   (weight = 0.4) and the fingerprint recognition system has an accuracy of 97%
BL-3   (weight = 0.6). The system processes 1200 authorized access attempts and 800
unauthorized access attempts.
Based on the above information, answer the following:
a) Calculate the fused system accuracy.
b) Determine the number of correct matches and false rejections for authorized
users.
c) Compute the number of false acceptances for unauthorized users.
Marks Bifurcation (10 Marks)
1. Fused accuracy calculation using weighted fusion – 5 Marks
2. Correct matches, false rejections, and false acceptances calculation – 5
Marks
Answer
Given Data
• Face accuracy = 92% = 0.92, weight = 0.4
•   Fingerprint accuracy = 97% = 0.97, weight = 0.6
• Authorized attempts = 1200
• Unauthorized attempts = 800
b   Describe the process of minutiae-based fingerprint matching by explaining the   10
Q6.   key stages involved, namely alignment, correspondence, and match score
CO-2,3,   generation. Discuss the role of the Hough Transform in achieving alignment
SO-6,
BL-2   between two fingerprint images. Further, analyze how spatial transformations
(such as translation and rotation) and the selection of matching thresholds
********** 14 **********
--- page 15 ---
influence the accuracy and overall performance of the fingerprint recognition
system.
Marks Bifurcation (10 Marks)
1. Minutiae-based fingerprint matching stages (alignment, correspondence,
match score) – 5 Marks
2. Role of Hough Transform, spatial transformations, and matching
threshold on system performance – 5 Marks
Answer
Minutiae-Based Fingerprint Matching
Minutiae-based fingerprint matching is a widely used method in fingerprint
recognition systems. It compares fingerprint images based on minutiae points,
which are ridge endings and bifurcations.
The fingerprint matching process consists of three main stages: alignment,
correspondence, and match score generation.
1. Alignment Stage
In the alignment stage, two fingerprint images (input fingerprint and stored
template) are aligned so that their minutiae points overlap as closely as possible.
Since fingerprint images may be captured at different positions or orientations,
alignment is necessary before matching.
Alignment compensates for:
•   Translation (shift in x and y direction)
•   Rotation (angle change)
• Small scaling differences
Role of Hough Transform
The Hough Transform is used to estimate the best alignment parameters
between two fingerprint images. It finds the transformation parameters such as
rotation angle and translation values that maximize the number of matching
minutiae points between two fingerprints. This helps in aligning the fingerprints
correctly before matching.
2. Correspondence Stage
In this stage, minutiae points from the input fingerprint are compared with
minutiae points in the stored template.
Two minutiae points are considered matched if:
•   Their spatial distance is within a tolerance limit.
•   Their orientation difference is within an allowed range.
•   Their minutiae type (ridge ending or bifurcation) is the same.
This stage determines how many minutiae points correspond between two
fingerprints.
3. Match Score Generation
After finding corresponding minutiae points, a match score is calculated.
If the match score is greater than a predefined threshold, the fingerprints are
considered matched; otherwise, they are rejected.
Influence of Spatial Transformations and Threshold
Spatial Transformations
Fingerprint images may differ due to translation and rotation. Proper alignment
using spatial transformations improves matching accuracy. Poor alignment may
lead to incorrect matching and increase False Rejection Rate (FRR).
********** 15 **********
--- page 16 ---
Matching Threshold
The threshold determines whether a fingerprint is accepted or rejected.
• High threshold → increases security but increases False Rejection Rate.
• Low threshold → decreases False Rejection Rate but increases False
Acceptance Rate.
• Optimal threshold balances FAR and FRR.
Q7.   a   A biometric identification system is deployed in a secure facility to identify   10
CO-1,3,   individuals from a large database. During evaluation, each probe image
SO-2,   generates a ranked list of candidate identities. Total number of probe samples are
BL-4   715. The distribution of correct matches at different ranks is recorded as follows:
Number of Correct
Rank
Identifications
R1   280
R2   120
R3   90
R4   70
R5   60
R6   40
R7   25
R8   15
R9   10
R10   5
Based on the above data, answer the following:
a) Compute the cumulative number of correct identifications up to each rank.
b) Calculate the cumulative match accuracy (%) for each rank from R1 to R10.
c) Plot the Cumulative Match Characteristic (CMC) curve.
d) Determine the minimum rank at which at least 95% identification accuracy is
achieved.
e) Analyze the system performance by interpreting Rank-1 accuracy and discuss
how improvements in feature extraction or matching algorithms could enhance
CMC performance.
Marks Bifurcation (10 Marks)
1. Cumulative correct identifications – 2 Marks
2. Cumulative match accuracy (%) – 2 Marks
3. CMC curve plotting – 2 Marks
4. Rank for 95% accuracy – 2 Marks
5. Performance analysis & Rank-1 discussion – 2 Marks
(a) Cumulative Correct Identifications
Rank   Correct   Cumulative Correct
R1   280   280
R2   120   400
R3   90   490
R4   70   560
********** 16 **********
--- page 17 ---
R5   60   620
R6   40   660
R7   25   685
R8   15   700
R9   10   710
R10   5   715
(b) Cumulative Match Accuracy (%)
Rank   Cumulative Correct   Accuracy (%)
R1   280   39.16
R2   400   55.94
R3   490   68.53
R4   560   78.32
R5   620   86.71
R6   660   92.31
R7   685   95.80
R8   700   97.90
R9   710   99.30
R10   715   100
(c) CMC Curve
Plot Rank vs Cumulative Match Accuracy.
The CMC curve increases with rank and approaches 100% at Rank 10.
CMC Points:
(1,39.16), (2,55.94), (3,68.53), (4,78.32), (5,86.71), (6,92.31), (7,95.80), (8,97.90),
(9,99.30), (10,100)
********** 17 **********
--- page 18 ---
(d) Rank for ≥ 95% Identification Accuracy
From the table, accuracy ≥ 95% occurs at Rank 7.
Minimum Rank = R7
(e) System Performance Analysis
• Rank-1 accuracy:
• Rank-1 accuracy is moderate, indicating correct identity appears at first
position for 39% of probes.
• System performance can be improved by:
o Better feature extraction
o Improved matching algorithms
o Deep learning-based recognition
o Better preprocessing and alignment
o Multimodal biometric systems
Improving feature extraction increases Rank-1 accuracy and improves the CMC
curve.
b A hospital deploys a biometric system using iris recognition to identify patients   10
and access medical records. While the system provides high accuracy, issues arise
when patients have difficulty positioning themselves correctly or when the system
fails due to reflections or lighting variations. This results in delays in patient
Q7.   processing.
CO-3,
SO-7,   Answer the following based on above scenario-
BL-4   a) Identify operational challenges in iris-based systems.
b) Discuss how environmental and user-related factors affect system performance.
c) Evaluate the advantages of iris recognition over other modalities.
d) Propose system improvements to enhance usability and efficiency.
Marks Bifurcation (10 Marks)
a)   Operational   challenges   in   iris-based   systems   –   2   Marks
b) Environmental and user-related factors affecting performance – 3 Marks
c) Advantages of   iris recognition over other modalities – 2 Marks
d) Proposed system improvements for usability and efficiency – 3 Marks
Answer
(a) Operational Challenges in Iris-Based Systems (2 Marks)
Operational challenges in iris recognition systems include:
•   Difficulty in correct eye positioning
•   Reflections from glasses or eye surface
•   Lighting variations affecting iris image capture
• Motion blur due to user movement
********** 18 **********
--- page 19 ---
•   Failure to capture iris for elderly or sick patients
• System delays due to repeated capture attempts
These challenges reduce system efficiency and increase authentication time.
(b) Environmental and User-Related Factors Affecting System Performance
(3 Marks)
Environmental Factors:
• Poor illumination
•   Light reflections
• Camera distance and focus
• Shadows and lighting variations
User-Related Factors:
• Improper eye alignment
• Eye movement during capture
• Wearing glasses or contact lenses
• Medical eye conditions
• Lack of user cooperation
These factors lead to poor image quality, segmentation errors, increased False
Rejection Rate (FRR), and slower system performance.
(c) Advantages of Iris Recognition Over Other Modalities (2 Marks)
• Very high accuracy
• Highly unique iris patterns
•   Stable over lifetime (high permanence)
•   Contactless biometric system
•   Difficult to spoof
• Low False Acceptance Rate (FAR)
•   Suitable for high-security applications
Iris recognition is more accurate and secure than fingerprint and face recognition
systems.
(d) Proposed System Improvements to Enhance Usability and Efficiency (3
Marks)
• Automatic eye detection and alignment system
•   Proper lighting and anti-reflection cameras
• User guidance interface for positioning
• Multimodal biometrics (Face + Iris)
•   Quality assessment before image capture
•   Faster processing algorithms
•   Multiple automatic capture attempts
•   High-resolution cameras
These improvements increase usability, reduce delays, and improve system
efficiency.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 98cacb01fbe7

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/Biometrics/ANS_Biometrics(702CO0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Biometrics
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. 1.   Question No. _1_ is compulsory.
3. 2.   Out of remaining questions, attempt any 4 questions.
4. 3.   In all _5_ questions to be attempted.
5. 4.   All questions carry equal marks.
6. 5.   Answer to each new question to be started on a fresh page.
7. 6.   Figures in brackets on the right hand side indicate full marks.
8. 7.   Assume Suitable data if necessary.
Q1   Section A (Compulsory Question)   Marks
CO-2,3, a   Identify and explain the functional components of a biometric system. Discuss   5
SO-1,   their role in ensuring reliable authentication.
BL-2
Marks Bifurcation (5 Marks)
. Functional components identification – 2 Marks
Explanation of components and their role in authentication – 3 Marks
Answer-
Functional Components of a Biometric System
A biometric system is used to identify or authenticate an individual based on
physiological or behavioral characteristics. The main functional components of a
biometric system are as follows:
1. Sensor Module
The sensor module captures the biometric data of the user such as fingerprint,
face image, iris image, or voice sample. The quality of captured data directly
affects the accuracy of the system.
2. Pre-processing Module
This module improves the quality of the captured biometric data by removing
noise, enhancing image quality, and normalizing the data so that it can be
processed properly.
3. Feature Extraction Module
In this stage, unique features are extracted from the biometric data. For example,
minutiae points in fingerprint, iris texture patterns, or facial feature points are
extracted and converted into a feature vector.
4. Template Database
The extracted features are stored in the database as biometric templates. These
templates are used later for comparison during authentication.
5. Matching Module
The matching module compares the extracted features with stored templates in
the database and calculates a matching score to determine similarity.
6. Decision Module
The decision module accepts or rejects the user based on the matching score and
a predefined threshold value.
********** 1 **********
--- page 2 ---
Role in Reliable Authentication
These components work together to ensure reliable authentication. Proper data
acquisition, accurate feature extraction, and efficient matching reduce false
acceptance and false rejection rates, thereby improving the accuracy, security,
and reliability of the biometric system.
CO–4, b   Define multimodal biometric systems. Explain how fusion of multiple modalities   5
SO-2,   improves system robustness.
BL-2
Marks Bifurcation (5 Marks)
1. Definition of Multimodal Biometric System – 2 Marks
2. Explanation of fusion and improvement in robustness – 3 Marks
Answer-
Multimodal Biometric System
A multimodal biometric system is a biometric system that uses more than one
biometric trait for identification or authentication. Instead of relying on a single
biometric trait such as fingerprint or face, the system combines multiple traits like
fingerprint, face, iris, or voice to improve accuracy and reliability.
Examples include:
• Face + Fingerprint
•   Iris + Fingerprint
• Voice + Face Recognition
Fusion and System Robustness
In multimodal biometric systems, fusion refers to the process of combining
information from multiple biometric sources. Fusion can be performed at different
levels such as sensor level, feature level, score level, or decision level.
Fusion improves system robustness in the following ways:
• Improves accuracy by combining multiple biometric traits
• Reduces false acceptance rate (FAR) and false rejection rate (FRR)
•   Provides better security because multiple traits must match
• Works even if one biometric trait fails due to noise or poor quality
• Reduces spoofing attacks since it is difficult to fake multiple biometric traits
CO-3, c   Explain the significance of performance parameters such as FAR, FRR, and   5
SO-6,   threshold in biometric systems.
BL-2
Marks Bifurcation (5 Marks)
1. Definition of FAR, FRR, and Threshold – 2 Marks
2. Significance of these performance parameters in biometric systems – 3
Marks
Answer-
Performance Parameters in Biometric Systems
Biometric systems are evaluated using performance parameters such as False
Acceptance Rate (FAR), False Rejection Rate (FRR), and Threshold. These
parameters help measure the accuracy and reliability of the biometric system.
1. False Acceptance Rate (FAR)
FAR is the probability that the biometric system incorrectly accepts an
unauthorized   person   as   an   authorized   user.
A high FAR means the system is less secure because impostors may gain access.
2. False Rejection Rate (FRR)
FRR is the probability that the biometric system incorrectly rejects an authorized
user.
A high FRR means the system is less user-friendly because genuine users are
denied access.
********** 2 **********
--- page 3 ---
3. Threshold
Threshold is the decision value used to accept or reject a user based on the
matching score.
•   If the matching score is above the threshold, the user is accepted.
•   If the matching score is below the threshold, the user is rejected.
Changing the threshold affects FAR and FRR:
•   Increasing threshold → decreases FAR but increases FRR
• Decreasing threshold → decreases FRR but increases FAR
Significance
These parameters are important because they help balance security and usability
of biometric systems. A good biometric system maintains low FAR and low FRR
by selecting an optimal threshold value.
CO-1,3, d   Discuss applications of biometrics in large-scale surveillance systems. Highlight   5
SO-4,   associated benefits and concerns.
BL-2,3
Marks Bifurcation (5 Marks)
1. Applications of biometrics in large-scale surveillance systems – 2 Marks
2. Benefits and concerns associated with biometric surveillance – 3 Marks
Answer
Applications of Biometrics in Large-Scale Surveillance Systems
Biometrics is widely used in large-scale surveillance systems for identification
and monitoring of individuals in public and secure areas. Some major applications
include:
1. Airport and Border Security – Face recognition and iris recognition are used
to identify passengers and detect criminals or unauthorized persons.
2. Law Enforcement and Criminal Identification – Police use fingerprint and
face recognition databases to identify suspects and missing persons.
3. Public Surveillance Systems – Face recognition cameras are used in public
places such as railway stations, malls, and smart cities for monitoring
activities.
4. Access Control in Government and Military Areas – Biometric
authentication is used to allow access only to authorized personnel.
5. National ID Systems – Large-scale biometric databases are used for
identification systems such as Aadhaar.
Benefits of Biometric Surveillance
• Improves security and crime prevention
• Helps in fast identification of criminals and suspects
• Reduces identity fraud
• Enables automated monitoring systems
•   Useful in large population management
Concerns and Issues
•   Privacy concerns and misuse of personal data
• Risk of data breaches and identity theft
•   Ethical issues related to continuous surveillance
•   Possibility of false identification
• High implementation cost
Section B (Attempt any four questions)
********** 3 **********
--- page 4 ---
Q2.   a   A biometric system verifies a user by comparing a fingerprint with a stored   5
CO-1,   template. State whether this is identification or verification and justify your
SO-1,   answer.
BL-4
Marks Bifurcation (5 Marks)
1. Identification vs Verification statement – 2 Marks
2. Justification with explanation of biometric process – 3 Marks
Answer
Identification or Verification
The given biometric system represents Verification, not Identification.
Justification
In biometric systems, there are two modes of operation:
1. Identification (1:N Matching)
In identification mode, the biometric sample is compared with all templates stored
in the database to determine the identity of the person. The system asks “Who are
you?”
2. Verification (1:1 Matching)
In verification mode, the biometric sample is compared with one stored template
associated with a claimed identity. The system asks “Are you who you claim to
be?”
In the given scenario, the system verifies a user by comparing a fingerprint with a
stored template. This indicates one-to-one comparison, which is verification.
Q2. b   Explain challenges in biometric data acquisition and how they affect system   5
CO-2,3,   performance. Give suitable examples.
SO-6,
BL-2
Marks Bifurcation (5 Marks)
1. Challenges in biometric data acquisition – 2 Marks
2. Effect on system performance with examples – 3 Marks
Answer
Challenges in Biometric Data Acquisition
Biometric data acquisition is the process of capturing biometric traits such as
fingerprint, face, iris, or voice using sensors. Several challenges occur during data
acquisition which affect system accuracy and performance.
Some common challenges include:
1. Poor Quality Sensors – Low-resolution sensors capture unclear biometric
images.
2. Environmental Conditions – Lighting, noise, temperature, and humidity
affect data capture.
3. User Cooperation – Improper finger placement, face angle, or movement
affects data quality.
4. Physical Changes – Injuries, aging, scars, or illness may change biometric
traits.
5. Noise and Distortion – Background noise in voice recognition or blur in face
images.
6. Occlusion – Face covered by mask, glasses, hair, etc.
Effect on System Performance
These challenges affect biometric system performance in the following ways:
•   Increase False Rejection Rate (FRR) when genuine users are rejected due to
poor data quality.
********** 4 **********
--- page 5 ---
•   Increase False Acceptance Rate (FAR) when unclear data matches
incorrectly.
• Reduce accuracy and reliability of the biometric system.
•   Increase processing time due to repeated data capture.
• Example:
o Wet or dirty fingers in fingerprint recognition may cause rejection.
o Low lighting in face recognition may cause incorrect identification.
o Background noise affects voice recognition accuracy.
Q2.   c   Illustrate the biometric system design cycle and explain each stage briefly.   5
CO-3,
SO-2,
BL-2
Marks Bifurcation (5 Marks)
1. Biometric system design cycle diagram / stages identification – 2 Marks
2. Explanation of each stage briefly – 3 Marks
Answer-
Biometric System Design Cycle
The biometric system design cycle consists of several stages involved in
developing and deploying a biometric authentication system. The cycle ensures
that the system is accurate, reliable, and secure.
Stages in Biometric System Design Cycle
1. Data Acquisition
In this stage, biometric data such as fingerprint, face, iris, or voice is collected
using sensors or cameras. The quality of captured data is important for system
performance.
2. Pre-processing
The captured biometric data is processed to remove noise, enhance image quality,
normalize the data, and prepare it for feature extraction.
3. Feature Extraction
Unique features are extracted from biometric data such as fingerprint minutiae
points, iris patterns, or facial features. These features represent the biometric trait.
4. Template Creation and Storage
The extracted features are stored in the database as biometric templates for future
comparison.
5. Matching
The extracted features from the input biometric sample are compared with stored
templates, and a matching score is generated.
6. Decision Making
Based on the matching score and threshold value, the system decides whether to
accept or reject the user.
7. Performance Evaluation
The system performance is evaluated using parameters such as FAR, FRR, and
accuracy,   and   the   system   may   be   improved   if   needed.
Data Acquisition → Pre-processing → Feature Extraction → Template Storage
→ Matching → Decision → Performance Evaluation
Q2. d   Compare unimodal and multimodal biometric systems including accuracy,   5
CO-3,   flexibility, and security.
SO-4,
BL-3
Marks Bifurcation (5 Marks)
1. Explanation of Unimodal and Multimodal biometric systems – 2 Marks
********** 5 **********
--- page 6 ---
2. Comparison based on accuracy, flexibility, and security – 3 Marks
Answer
Unimodal Biometric System
A unimodal biometric system uses only one biometric trait for authentication,
such as fingerprint, face, iris, or voice recognition. The system captures a single
biometric feature and compares it with the stored template for identification or
verification.
Examples: Fingerprint recognition system, Face recognition system.
Multimodal Biometric System
A multimodal biometric system uses more than one biometric trait for
authentication. It combines multiple biometric sources such as fingerprint and
face, iris and fingerprint, or voice and face recognition to improve system
performance.
Examples: Face + Fingerprint authentication, Iris + Fingerprint systems.
Comparison Between Unimodal and Multimodal Biometric Systems
Unimodal   Multimodal
Feature
Biometric   Biometric
Accuracy   Lower accuracy   Higher accuracy
Flexibility   Less flexible   More flexible
Security   Less secure   More secure
Higher FAR and   Lower FAR and
Error Rates
FRR   FRR
Cost   Low cost   High cost
System Complexity   Simple   Complex
Q3.   a   A healthcare organization plans to deploy a multimodal biometric system using   10
CO-4,   face and iris recognition. Answer the following:
SO-2,
BL-4
1.   Design a workflow illustrating feature-level and score-level fusion.
2.   Suggest mechanisms to handle inconsistencies between modalities.
Marks Bifurcation (10 Marks)
1.   Workflow for feature-level and score-level fusion (diagram/steps) – 5 Marks
2.   Mechanisms to handle inconsistencies between modalities – 5 Marks
Answer
Multimodal Biometric System (Face + Iris)
A multimodal biometric system combines multiple biometric traits to improve
accuracy, reliability, and security. In this system, face recognition and iris
recognition are used together.
1. Workflow for Feature-Level and Score-Level Fusion
(a) Feature-Level Fusion Workflow
********** 6 **********
--- page 7 ---
In feature-level fusion, features from face and iris are combined before matching.
Workflow Steps:
1.   Capture face image and iris image using sensors.
2.   Preprocess both images (noise removal, normalization).
3.   Extract features from face and iris separately.
4.   Combine feature vectors into a single feature vector.
5.   Store combined template in database.
6.   During authentication, extract features again and compare with stored
template.
7.   Matching score generated and decision taken.
Flow (Text Diagram)
Face Image → Feature Extraction →
→ Feature Fusion → Matching → Decision
Iris Image → Feature Extraction →
(b) Score-Level Fusion Workflow
In score-level fusion, matching scores from both modalities are combined.
Workflow Steps:
1.   Capture face and iris images.
2.   Extract features separately.
3.   Match face features with face template → Score 1.
4.   Match iris features with iris template → Score 2.
5.   Combine scores using sum rule, weighted sum, or average.
6.   Final score compared with threshold.
7.   Accept or Reject decision.
Flow (Text Diagram)
Face → Matching → Score 1
Iris → Matching → Score 2
Score Fusion → Final Score → Decision
2. Mechanisms to Handle Inconsistencies Between Modalities
In multimodal systems, sometimes one biometric modality may fail due to poor
quality data. The system should handle inconsistencies using the following
methods:
Mechanisms:
1.   Weighted Score Fusion
o   Assign higher weight to more reliable modality (e.g., iris more
reliable than face).
2.   Quality-Based Fusion
o   If face image quality is poor, give more importance to iris
recognition.
********** 7 **********
--- page 8 ---
3.   Fallback Mechanism
o   If one modality fails, system authenticates using the other modality.
4.   Adaptive Threshold
o   Threshold changes based on available modalities.
5.   Decision-Level Fusion
o   Final decision taken using AND/OR rules.
Example:
o   AND Rule → Both face and iris must match (high security)
o   OR Rule → Either face or iris match (high usability)
b A network security organization deploys a machine learning–based intrusion   10
detection system to monitor incoming traffic and classify activities as Normal or
Attack. The system generates probability scores indicating the likelihood of
normal behavior. During evaluation, it is observed that the dataset is highly
imbalanced, with significantly more normal traffic than attack instances.
Given the following classification results:
ID   Actual Class   Probability (Normal)
1   Normal   0.93
Q3.   2   Normal   0.88
CO-3,   3   Normal   0.82
SO-6,   4   Normal   0.79
BL-4
5   Normal   0.75
6   Normal   0.71
7   Attack   0.42
8   Normal   0.85
9   Normal   0.78
10   Attack   0.30
Compute TP, FP, TPR, and FPR. Plot ROC curve. Comment on performance
under severe class imbalance.
Marks Bifurcation (10 Marks)
1. TP, FP, TPR, FPR – 6 marks
2. ROC points / ROC curve – 3 Marks
3. Comment on class imbalance – 1 Mark
Answer
********** 8 **********
--- page 9 ---
FPR =
Step Actual   TP   FP   TPR = TP/8
FP/2
Start —   0   0   0   0
1   Normal 1   0   0.125   0
2   Normal 2   0   0.25   0
3   Normal 3   0   0.375   0
4   Normal 4   0   0.50   0
5   Normal 5   0   0.625   0
6   Normal 6   0   0.75   0
7   Normal 7   0   0.875   0
8   Normal 8   0   1   0
9   Attack   8   1   1   0.5
10   Attack   8   2   1   1
Comment on class imbalance – 1 Mark
Since the dataset contains more Normal samples than Attack samples, accuracy
alone may be misleading. ROC curve is a better performance measure for
imbalanced datasets. The ROC curve is close to the top-left corner, indicating
good classifier performance. However, class imbalance may cause the model to
favor the majority class (Normal), so evaluation should focus on TPR, FPR, and
ROC rather than accuracy.
Q4.   a   10
CO-2,3,
SO-4,
BL-4
Study the given iris processing images and answer the following:
a) Identify each stage shown in the images.
********** 9 **********
--- page 10 ---
b) Explain iris segmentation and its challenges.
c) Explain how iris codes are generated and used for authentication.
Ans   Marks Bifurcation (10 Marks)
a) Identify each stage shown in images – 3 Marks
b) Iris segmentation and its challenges – 4 Marks
c) Iris code generation and authentication – 3 Marks
Answer
(a) Identify Each Stage Shown in Iris Processing Images
The iris recognition process consists of the following stages typically shown in iris
processing images:
1. Iris Image Acquisition – Capturing the eye image using a camera.
2. Iris Segmentation – Detecting the iris region by locating the pupil and iris
boundaries.
3. Normalization – Converting the circular iris region into a rectangular form
using polar coordinates.
4. Feature Extraction / Iris Code Generation – Extracting texture features and
generating binary iris code.
5. Matching – Comparing iris code with stored template for authentication.
(b) Iris Segmentation and Its Challenges
Iris Segmentation
Iris segmentation is the process of isolating the iris region from the eye image by
detecting:
•   Pupil boundary
•   Iris outer boundary
•   Eyelids and eyelashes
Techniques used include:
•   Intergro Differential
•   Geodesic
The segmented iris region is then used for further processing.
Challenges in Iris Segmentation
1. Eyelid occlusion – Eyelids may cover part of iris.
2. Eyelashes interference – Eyelashes create noise.
3. Reflections – Light reflections on eye surface.
4. Poor image quality – Low resolution or blur.
5. Off-angle images – Eye not aligned properly.
6. Pupil dilation – Changes iris size.
These challenges may reduce recognition accuracy.
(c) Iris Code Generation and Authentication
After segmentation and normalization, features are extracted from iris texture.
Iris Code Generation
•   Filters such as Gabor filters or wavelets are used.
•   Iris texture is converted into a binary code (iris code).
• Each iris code is unique for each individual.
Authentication Process
1. Capture iris image.
2. Segment and normalize iris.
3. Generate iris code.
4. Compare iris code with stored template.
5. Matching is performed using Hamming Distance.
6.   If matching score is above threshold → Accept.
7. Otherwise → Reject.
Q4.   b   A university plans to implement biometric attendance. Some students have   10
CO-1,3,   worn
********** 10 **********
--- page 11 ---
SO-5,   fingerprints and inconsistent behaviour patterns. Analyze:
BL-3
1. Limitations of physiological and behavioural biometrics
2. Recommend a robust multimodal solution considering cost and usability
Marks Bifurcation (10 Marks)
1. Limitations of physiological biometrics – 3 Marks
2. Limitations of behavioural biometrics – 3 Marks
3. Recommendation of robust multimodal solution (cost & usability) – 4
Marks
Answer
1. Limitations of Physiological Biometrics
Physiological biometrics are based on physical characteristics such as
fingerprint, face, iris, and palmprint. These systems have some limitations:
• Worn fingerprints due to manual work, injuries, or aging may reduce
fingerprint recognition accuracy.
• Face recognition affected by lighting, pose, masks, or facial expressions.
• Iris recognition requires high-quality cameras and controlled environment.
• Sensor hygiene issues in fingerprint scanners.
• Hardware cost may be high for iris scanners.
• Failure to enroll may occur if biometric trait cannot be captured properly.
Thus, physiological biometrics may suffer from noise, environmental effects,
and physical changes.
2. Limitations of Behavioural Biometrics
Behavioural biometrics include signature, keystroke dynamics, voice
recognition, and gait recognition.
Limitations include:
• Behaviour changes over time.
• Voice affected by illness or noise.
• Signature may vary each time.
• Keystroke patterns change with mood, stress, or device.
• Less accurate compared to physiological biometrics.
• Higher False Rejection Rate (FRR).
Thus, behavioural biometrics are not always consistent and may reduce system
reliability.
3. Recommended Robust Multimodal Solution (Cost & Usability)
To handle worn fingerprints and inconsistent behaviour, a multimodal biometric
system should be implemented.
Recommended System:
Face Recognition + Fingerprint + RFID/ID Card
Reasons:
• Face recognition is contactless and fast.
• Fingerprint provides high accuracy.
• RFID/ID card acts as backup authentication.
• Multimodal system reduces FAR and FRR.
• Works even if one biometric fails.
• Cost is moderate compared to iris recognition systems.
• Usability is high for student attendance systems.
Fusion Method:
• Use Score-level fusion or Decision-level fusion.
********** 11 **********
--- page 12 ---
• Example:
o Face OR Fingerprint → Attendance marked
o Both match → High security mode
Q5.   a   Explain the concept of biometric identifiers and discuss their characteristics   10
CO-4,   such as universality, uniqueness, Collectability, Acceptability, Resistance to
SO-6,   Circumvention and permanence.
BL-3
Marks Bifurcation (10 Marks)
1. Concept of biometric identifiers – 5 Marks
2. Characteristics: Universality, Uniqueness, Permanence – 5 Marks
Answer
Concept of Biometric Identifiers
Biometric identifiers are measurable physiological or behavioral characteristics
that can be used to identify or verify the identity of an individual. These
identifiers are unique to each person and are used in biometric authentication
systems such as fingerprint recognition, face recognition, iris recognition,
voice recognition, and signature verification.
Biometric identifiers are used in security systems, attendance systems, banking
authentication, border control, and surveillance systems because they provide
reliable and secure identification.
Examples of biometric identifiers:
• Fingerprint
• Face
• Iris
• Retina
• Voice
• Signature
• Keystroke dynamics
• Gait
Characteristics of Biometric Identifiers
1. Universality
Universality means that every person should possess the biometric trait.
For example, every individual has a face and fingerprints, so these traits satisfy
universality. A biometric system cannot be effective if some people do not
have that trait.
Example: Fingerprint and face recognition satisfy universality.
2. Uniqueness
Uniqueness means that the biometric trait should be different for each
individual.
Even identical twins have different fingerprints and iris patterns. This property
helps in distinguishing one person from another.
Example: Iris patterns and fingerprints are highly unique.
3. Permanence
Permanence means that the biometric trait should remain stable over time and
should not change significantly with age or environment.
Example: Iris and fingerprint patterns remain stable for many years, while voice
and signature may change over time.
Q5.   b   Explain the concept of multimodal biometric systems and discuss how fusion   10
CO-3 ,   techniques improve system reliability and security.
********** 12 **********
--- page 13 ---
SO-7 ,
BL-1,4   A multimodal biometric system employs AND fusion by combining fingerprint
and iris recognition, where the fingerprint system has an accuracy of 90% and the
iris system has an accuracy of 95%. The system processes 1000 authorized access
attempts and 1000 unauthorized access attempts. Based on this information,
calculate the combined system accuracy under AND fusion. Further, determine
the number of false rejections and false acceptances produced by the system.
Marks Bifurcation (10 Marks)
1. Concept of multimodal biometric systems and fusion techniques – 5 Marks
2. AND fusion accuracy, false rejections, and false acceptances calculation –
5 Marks
Answer
Multimodal Biometric Systems and Fusion Techniques
A multimodal biometric system uses more than one biometric trait such as
fingerprint, face, iris, or voice for authentication. These systems improve
accuracy, reliability, and security compared to unimodal biometric systems
because multiple biometric traits are used for identification.
Fusion techniques are used to combine information from multiple biometric
systems. Fusion can be performed at different levels such as feature level, score
level, and decision level. Fusion improves system reliability by reducing False
Acceptance Rate (FAR) and False Rejection Rate (FRR). It also improves
security because it is difficult to spoof multiple biometric traits. Multimodal
systems also work even if one biometric trait fails due to noise or poor quality
data.
AND Fusion Calculation
Given:
•   Fingerprint accuracy = 90% = 0.9
•   Iris accuracy = 95% = 0.95
• Authorized attempts = 1000
• Unauthorized attempts = 1000
• Fusion type = AND fusion
********** 13 **********
--- page 14 ---
Q6.   a   A multimodal biometric system uses weighted fusion by combining face and   10
CO-1,   fingerprint recognition, where the face recognition system has an accuracy of 92%
SO-1,   (weight = 0.4) and the fingerprint recognition system has an accuracy of 97%
BL-3   (weight = 0.6). The system processes 1200 authorized access attempts and 800
unauthorized access attempts.
Based on the above information, answer the following:
a) Calculate the fused system accuracy.
b) Determine the number of correct matches and false rejections for authorized
users.
c) Compute the number of false acceptances for unauthorized users.
Marks Bifurcation (10 Marks)
1. Fused accuracy calculation using weighted fusion – 5 Marks
2. Correct matches, false rejections, and false acceptances calculation – 5
Marks
Answer
Given Data
• Face accuracy = 92% = 0.92, weight = 0.4
•   Fingerprint accuracy = 97% = 0.97, weight = 0.6
• Authorized attempts = 1200
• Unauthorized attempts = 800
b   Describe the process of minutiae-based fingerprint matching by explaining the   10
Q6.   key stages involved, namely alignment, correspondence, and match score
CO-2,3,   generation. Discuss the role of the Hough Transform in achieving alignment
SO-6,
BL-2   between two fingerprint images. Further, analyze how spatial transformations
(such as translation and rotation) and the selection of matching thresholds
********** 14 **********
--- page 15 ---
influence the accuracy and overall performance of the fingerprint recognition
system.
Marks Bifurcation (10 Marks)
1. Minutiae-based fingerprint matching stages (alignment, correspondence,
match score) – 5 Marks
2. Role of Hough Transform, spatial transformations, and matching
threshold on system performance – 5 Marks
Answer
Minutiae-Based Fingerprint Matching
Minutiae-based fingerprint matching is a widely used method in fingerprint
recognition systems. It compares fingerprint images based on minutiae points,
which are ridge endings and bifurcations.
The fingerprint matching process consists of three main stages: alignment,
correspondence, and match score generation.
1. Alignment Stage
In the alignment stage, two fingerprint images (input fingerprint and stored
template) are aligned so that their minutiae points overlap as closely as possible.
Since fingerprint images may be captured at different positions or orientations,
alignment is necessary before matching.
Alignment compensates for:
•   Translation (shift in x and y direction)
•   Rotation (angle change)
• Small scaling differences
Role of Hough Transform
The Hough Transform is used to estimate the best alignment parameters
between two fingerprint images. It finds the transformation parameters such as
rotation angle and translation values that maximize the number of matching
minutiae points between two fingerprints. This helps in aligning the fingerprints
correctly before matching.
2. Correspondence Stage
In this stage, minutiae points from the input fingerprint are compared with
minutiae points in the stored template.
Two minutiae points are considered matched if:
•   Their spatial distance is within a tolerance limit.
•   Their orientation difference is within an allowed range.
•   Their minutiae type (ridge ending or bifurcation) is the same.
This stage determines how many minutiae points correspond between two
fingerprints.
3. Match Score Generation
After finding corresponding minutiae points, a match score is calculated.
If the match score is greater than a predefined threshold, the fingerprints are
considered matched; otherwise, they are rejected.
Influence of Spatial Transformations and Threshold
Spatial Transformations
Fingerprint images may differ due to translation and rotation. Proper alignment
using spatial transformations improves matching accuracy. Poor alignment may
lead to incorrect matching and increase False Rejection Rate (FRR).
********** 15 **********
--- page 16 ---
Matching Threshold
The threshold determines whether a fingerprint is accepted or rejected.
• High threshold → increases security but increases False Rejection Rate.
• Low threshold → decreases False Rejection Rate but increases False
Acceptance Rate.
• Optimal threshold balances FAR and FRR.
Q7.   a   A biometric identification system is deployed in a secure facility to identify   10
CO-1,3,   individuals from a large database. During evaluation, each probe image
SO-2,   generates a ranked list of candidate identities. Total number of probe samples are
BL-4   715. The distribution of correct matches at different ranks is recorded as follows:
Number of Correct
Rank
Identifications
R1   280
R2   120
R3   90
R4   70
R5   60
R6   40
R7   25
R8   15
R9   10
R10   5
Based on the above data, answer the following:
a) Compute the cumulative number of correct identifications up to each rank.
b) Calculate the cumulative match accuracy (%) for each rank from R1 to R10.
c) Plot the Cumulative Match Characteristic (CMC) curve.
d) Determine the minimum rank at which at least 95% identification accuracy is
achieved.
e) Analyze the system performance by interpreting Rank-1 accuracy and discuss
how improvements in feature extraction or matching algorithms could enhance
CMC performance.
Marks Bifurcation (10 Marks)
1. Cumulative correct identifications – 2 Marks
2. Cumulative match accuracy (%) – 2 Marks
3. CMC curve plotting – 2 Marks
4. Rank for 95% accuracy – 2 Marks
5. Performance analysis & Rank-1 discussion – 2 Marks
(a) Cumulative Correct Identifications
Rank   Correct   Cumulative Correct
R1   280   280
R2   120   400
R3   90   490
R4   70   560
********** 16 **********
--- page 17 ---
R5   60   620
R6   40   660
R7   25   685
R8   15   700
R9   10   710
R10   5   715
(b) Cumulative Match Accuracy (%)
Rank   Cumulative Correct   Accuracy (%)
R1   280   39.16
R2   400   55.94
R3   490   68.53
R4   560   78.32
R5   620   86.71
R6   660   92.31
R7   685   95.80
R8   700   97.90
R9   710   99.30
R10   715   100
(c) CMC Curve
Plot Rank vs Cumulative Match Accuracy.
The CMC curve increases with rank and approaches 100% at Rank 10.
CMC Points:
(1,39.16), (2,55.94), (3,68.53), (4,78.32), (5,86.71), (6,92.31), (7,95.80), (8,97.90),
(9,99.30), (10,100)
********** 17 **********
--- page 18 ---
(d) Rank for ≥ 95% Identification Accuracy
From the table, accuracy ≥ 95% occurs at Rank 7.
Minimum Rank = R7
(e) System Performance Analysis
• Rank-1 accuracy:
• Rank-1 accuracy is moderate, indicating correct identity appears at first
position for 39% of probes.
• System performance can be improved by:
o Better feature extraction
o Improved matching algorithms
o Deep learning-based recognition
o Better preprocessing and alignment
o Multimodal biometric systems
Improving feature extraction increases Rank-1 accuracy and improves the CMC
curve.
b A hospital deploys a biometric system using iris recognition to identify patients   10
and access medical records. While the system provides high accuracy, issues arise
when patients have difficulty positioning themselves correctly or when the system
fails due to reflections or lighting variations. This results in delays in patient
Q7.   processing.
CO-3,
SO-7,   Answer the following based on above scenario-
BL-4   a) Identify operational challenges in iris-based systems.
b) Discuss how environmental and user-related factors affect system performance.
c) Evaluate the advantages of iris recognition over other modalities.
d) Propose system improvements to enhance usability and efficiency.
Marks Bifurcation (10 Marks)
a)   Operational   challenges   in   iris-based   systems   –   2   Marks
b) Environmental and user-related factors affecting performance – 3 Marks
c) Advantages of   iris recognition over other modalities – 2 Marks
d) Proposed system improvements for usability and efficiency – 3 Marks
Answer
(a) Operational Challenges in Iris-Based Systems (2 Marks)
Operational challenges in iris recognition systems include:
•   Difficulty in correct eye positioning
•   Reflections from glasses or eye surface
•   Lighting variations affecting iris image capture
• Motion blur due to user movement
********** 18 **********
--- page 19 ---
•   Failure to capture iris for elderly or sick patients
• System delays due to repeated capture attempts
These challenges reduce system efficiency and increase authentication time.
(b) Environmental and User-Related Factors Affecting System Performance
(3 Marks)
Environmental Factors:
• Poor illumination
•   Light reflections
• Camera distance and focus
• Shadows and lighting variations
User-Related Factors:
• Improper eye alignment
• Eye movement during capture
• Wearing glasses or contact lenses
• Medical eye conditions
• Lack of user cooperation
These factors lead to poor image quality, segmentation errors, increased False
Rejection Rate (FRR), and slower system performance.
(c) Advantages of Iris Recognition Over Other Modalities (2 Marks)
• Very high accuracy
• Highly unique iris patterns
•   Stable over lifetime (high permanence)
•   Contactless biometric system
•   Difficult to spoof
• Low False Acceptance Rate (FAR)
•   Suitable for high-security applications
Iris recognition is more accurate and secure than fingerprint and face recognition
systems.
(d) Proposed System Improvements to Enhance Usability and Efficiency (3
Marks)
• Automatic eye detection and alignment system
•   Proper lighting and anti-reflection cameras
• User guidance interface for positioning
• Multimodal biometrics (Face + Iris)
•   Quality assessment before image capture
•   Faster processing algorithms
•   Multiple automatic capture attempts
•   High-resolution cameras
These improvements increase usability, reduce delays, and improve system
efficiency.
********** 19 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper acbc617483ef

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_Computer_7032/Biometrics/ANS_Biometrics(702CO0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Biometrics
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. 1.   Question No. _1_ is compulsory.
3. 2.   Out of remaining questions, attempt any 4 questions.
4. 3.   In all _5_ questions to be attempted.
5. 4.   All questions carry equal marks.
6. 5.   Answer to each new question to be started on a fresh page.
7. 6.   Figures in brackets on the right hand side indicate full marks.
8. 7.   Assume Suitable data if necessary.
Q1   Section A (Compulsory Question)   Marks
CO-2,3, a   Identify and explain the functional components of a biometric system. Discuss   5
SO-1,   their role in ensuring reliable authentication.
BL-2
Marks Bifurcation (5 Marks)
. Functional components identification – 2 Marks
Explanation of components and their role in authentication – 3 Marks
Answer-
Functional Components of a Biometric System
A biometric system is used to identify or authenticate an individual based on
physiological or behavioral characteristics. The main functional components of a
biometric system are as follows:
1. Sensor Module
The sensor module captures the biometric data of the user such as fingerprint,
face image, iris image, or voice sample. The quality of captured data directly
affects the accuracy of the system.
2. Pre-processing Module
This module improves the quality of the captured biometric data by removing
noise, enhancing image quality, and normalizing the data so that it can be
processed properly.
3. Feature Extraction Module
In this stage, unique features are extracted from the biometric data. For example,
minutiae points in fingerprint, iris texture patterns, or facial feature points are
extracted and converted into a feature vector.
4. Template Database
The extracted features are stored in the database as biometric templates. These
templates are used later for comparison during authentication.
5. Matching Module
The matching module compares the extracted features with stored templates in
the database and calculates a matching score to determine similarity.
6. Decision Module
The decision module accepts or rejects the user based on the matching score and
a predefined threshold value.
********** 1 **********
--- page 2 ---
Role in Reliable Authentication
These components work together to ensure reliable authentication. Proper data
acquisition, accurate feature extraction, and efficient matching reduce false
acceptance and false rejection rates, thereby improving the accuracy, security,
and reliability of the biometric system.
CO–4, b   Define multimodal biometric systems. Explain how fusion of multiple modalities   5
SO-2,   improves system robustness.
BL-2
Marks Bifurcation (5 Marks)
1. Definition of Multimodal Biometric System – 2 Marks
2. Explanation of fusion and improvement in robustness – 3 Marks
Answer-
Multimodal Biometric System
A multimodal biometric system is a biometric system that uses more than one
biometric trait for identification or authentication. Instead of relying on a single
biometric trait such as fingerprint or face, the system combines multiple traits like
fingerprint, face, iris, or voice to improve accuracy and reliability.
Examples include:
• Face + Fingerprint
•   Iris + Fingerprint
• Voice + Face Recognition
Fusion and System Robustness
In multimodal biometric systems, fusion refers to the process of combining
information from multiple biometric sources. Fusion can be performed at different
levels such as sensor level, feature level, score level, or decision level.
Fusion improves system robustness in the following ways:
• Improves accuracy by combining multiple biometric traits
• Reduces false acceptance rate (FAR) and false rejection rate (FRR)
•   Provides better security because multiple traits must match
• Works even if one biometric trait fails due to noise or poor quality
• Reduces spoofing attacks since it is difficult to fake multiple biometric traits
CO-3, c   Explain the significance of performance parameters such as FAR, FRR, and   5
SO-6,   threshold in biometric systems.
BL-2
Marks Bifurcation (5 Marks)
1. Definition of FAR, FRR, and Threshold – 2 Marks
2. Significance of these performance parameters in biometric systems – 3
Marks
Answer-
Performance Parameters in Biometric Systems
Biometric systems are evaluated using performance parameters such as False
Acceptance Rate (FAR), False Rejection Rate (FRR), and Threshold. These
parameters help measure the accuracy and reliability of the biometric system.
1. False Acceptance Rate (FAR)
FAR is the probability that the biometric system incorrectly accepts an
unauthorized   person   as   an   authorized   user.
A high FAR means the system is less secure because impostors may gain access.
2. False Rejection Rate (FRR)
FRR is the probability that the biometric system incorrectly rejects an authorized
user.
A high FRR means the system is less user-friendly because genuine users are
denied access.
********** 2 **********
--- page 3 ---
3. Threshold
Threshold is the decision value used to accept or reject a user based on the
matching score.
•   If the matching score is above the threshold, the user is accepted.
•   If the matching score is below the threshold, the user is rejected.
Changing the threshold affects FAR and FRR:
•   Increasing threshold → decreases FAR but increases FRR
• Decreasing threshold → decreases FRR but increases FAR
Significance
These parameters are important because they help balance security and usability
of biometric systems. A good biometric system maintains low FAR and low FRR
by selecting an optimal threshold value.
CO-1,3, d   Discuss applications of biometrics in large-scale surveillance systems. Highlight   5
SO-4,   associated benefits and concerns.
BL-2,3
Marks Bifurcation (5 Marks)
1. Applications of biometrics in large-scale surveillance systems – 2 Marks
2. Benefits and concerns associated with biometric surveillance – 3 Marks
Answer
Applications of Biometrics in Large-Scale Surveillance Systems
Biometrics is widely used in large-scale surveillance systems for identification
and monitoring of individuals in public and secure areas. Some major applications
include:
1. Airport and Border Security – Face recognition and iris recognition are used
to identify passengers and detect criminals or unauthorized persons.
2. Law Enforcement and Criminal Identification – Police use fingerprint and
face recognition databases to identify suspects and missing persons.
3. Public Surveillance Systems – Face recognition cameras are used in public
places such as railway stations, malls, and smart cities for monitoring
activities.
4. Access Control in Government and Military Areas – Biometric
authentication is used to allow access only to authorized personnel.
5. National ID Systems – Large-scale biometric databases are used for
identification systems such as Aadhaar.
Benefits of Biometric Surveillance
• Improves security and crime prevention
• Helps in fast identification of criminals and suspects
• Reduces identity fraud
• Enables automated monitoring systems
•   Useful in large population management
Concerns and Issues
•   Privacy concerns and misuse of personal data
• Risk of data breaches and identity theft
•   Ethical issues related to continuous surveillance
•   Possibility of false identification
• High implementation cost
Section B (Attempt any four questions)
********** 3 **********
--- page 4 ---
Q2.   a   A biometric system verifies a user by comparing a fingerprint with a stored   5
CO-1,   template. State whether this is identification or verification and justify your
SO-1,   answer.
BL-4
Marks Bifurcation (5 Marks)
1. Identification vs Verification statement – 2 Marks
2. Justification with explanation of biometric process – 3 Marks
Answer
Identification or Verification
The given biometric system represents Verification, not Identification.
Justification
In biometric systems, there are two modes of operation:
1. Identification (1:N Matching)
In identification mode, the biometric sample is compared with all templates stored
in the database to determine the identity of the person. The system asks “Who are
you?”
2. Verification (1:1 Matching)
In verification mode, the biometric sample is compared with one stored template
associated with a claimed identity. The system asks “Are you who you claim to
be?”
In the given scenario, the system verifies a user by comparing a fingerprint with a
stored template. This indicates one-to-one comparison, which is verification.
Q2. b   Explain challenges in biometric data acquisition and how they affect system   5
CO-2,3,   performance. Give suitable examples.
SO-6,
BL-2
Marks Bifurcation (5 Marks)
1. Challenges in biometric data acquisition – 2 Marks
2. Effect on system performance with examples – 3 Marks
Answer
Challenges in Biometric Data Acquisition
Biometric data acquisition is the process of capturing biometric traits such as
fingerprint, face, iris, or voice using sensors. Several challenges occur during data
acquisition which affect system accuracy and performance.
Some common challenges include:
1. Poor Quality Sensors – Low-resolution sensors capture unclear biometric
images.
2. Environmental Conditions – Lighting, noise, temperature, and humidity
affect data capture.
3. User Cooperation – Improper finger placement, face angle, or movement
affects data quality.
4. Physical Changes – Injuries, aging, scars, or illness may change biometric
traits.
5. Noise and Distortion – Background noise in voice recognition or blur in face
images.
6. Occlusion – Face covered by mask, glasses, hair, etc.
Effect on System Performance
These challenges affect biometric system performance in the following ways:
•   Increase False Rejection Rate (FRR) when genuine users are rejected due to
poor data quality.
********** 4 **********
--- page 5 ---
•   Increase False Acceptance Rate (FAR) when unclear data matches
incorrectly.
• Reduce accuracy and reliability of the biometric system.
•   Increase processing time due to repeated data capture.
• Example:
o Wet or dirty fingers in fingerprint recognition may cause rejection.
o Low lighting in face recognition may cause incorrect identification.
o Background noise affects voice recognition accuracy.
Q2.   c   Illustrate the biometric system design cycle and explain each stage briefly.   5
CO-3,
SO-2,
BL-2
Marks Bifurcation (5 Marks)
1. Biometric system design cycle diagram / stages identification – 2 Marks
2. Explanation of each stage briefly – 3 Marks
Answer-
Biometric System Design Cycle
The biometric system design cycle consists of several stages involved in
developing and deploying a biometric authentication system. The cycle ensures
that the system is accurate, reliable, and secure.
Stages in Biometric System Design Cycle
1. Data Acquisition
In this stage, biometric data such as fingerprint, face, iris, or voice is collected
using sensors or cameras. The quality of captured data is important for system
performance.
2. Pre-processing
The captured biometric data is processed to remove noise, enhance image quality,
normalize the data, and prepare it for feature extraction.
3. Feature Extraction
Unique features are extracted from biometric data such as fingerprint minutiae
points, iris patterns, or facial features. These features represent the biometric trait.
4. Template Creation and Storage
The extracted features are stored in the database as biometric templates for future
comparison.
5. Matching
The extracted features from the input biometric sample are compared with stored
templates, and a matching score is generated.
6. Decision Making
Based on the matching score and threshold value, the system decides whether to
accept or reject the user.
7. Performance Evaluation
The system performance is evaluated using parameters such as FAR, FRR, and
accuracy,   and   the   system   may   be   improved   if   needed.
Data Acquisition → Pre-processing → Feature Extraction → Template Storage
→ Matching → Decision → Performance Evaluation
Q2. d   Compare unimodal and multimodal biometric systems including accuracy,   5
CO-3,   flexibility, and security.
SO-4,
BL-3
Marks Bifurcation (5 Marks)
1. Explanation of Unimodal and Multimodal biometric systems – 2 Marks
********** 5 **********
--- page 6 ---
2. Comparison based on accuracy, flexibility, and security – 3 Marks
Answer
Unimodal Biometric System
A unimodal biometric system uses only one biometric trait for authentication,
such as fingerprint, face, iris, or voice recognition. The system captures a single
biometric feature and compares it with the stored template for identification or
verification.
Examples: Fingerprint recognition system, Face recognition system.
Multimodal Biometric System
A multimodal biometric system uses more than one biometric trait for
authentication. It combines multiple biometric sources such as fingerprint and
face, iris and fingerprint, or voice and face recognition to improve system
performance.
Examples: Face + Fingerprint authentication, Iris + Fingerprint systems.
Comparison Between Unimodal and Multimodal Biometric Systems
Unimodal   Multimodal
Feature
Biometric   Biometric
Accuracy   Lower accuracy   Higher accuracy
Flexibility   Less flexible   More flexible
Security   Less secure   More secure
Higher FAR and   Lower FAR and
Error Rates
FRR   FRR
Cost   Low cost   High cost
System Complexity   Simple   Complex
Q3.   a   A healthcare organization plans to deploy a multimodal biometric system using   10
CO-4,   face and iris recognition. Answer the following:
SO-2,
BL-4
1.   Design a workflow illustrating feature-level and score-level fusion.
2.   Suggest mechanisms to handle inconsistencies between modalities.
Marks Bifurcation (10 Marks)
1.   Workflow for feature-level and score-level fusion (diagram/steps) – 5 Marks
2.   Mechanisms to handle inconsistencies between modalities – 5 Marks
Answer
Multimodal Biometric System (Face + Iris)
A multimodal biometric system combines multiple biometric traits to improve
accuracy, reliability, and security. In this system, face recognition and iris
recognition are used together.
1. Workflow for Feature-Level and Score-Level Fusion
(a) Feature-Level Fusion Workflow
********** 6 **********
--- page 7 ---
In feature-level fusion, features from face and iris are combined before matching.
Workflow Steps:
1.   Capture face image and iris image using sensors.
2.   Preprocess both images (noise removal, normalization).
3.   Extract features from face and iris separately.
4.   Combine feature vectors into a single feature vector.
5.   Store combined template in database.
6.   During authentication, extract features again and compare with stored
template.
7.   Matching score generated and decision taken.
Flow (Text Diagram)
Face Image → Feature Extraction →
→ Feature Fusion → Matching → Decision
Iris Image → Feature Extraction →
(b) Score-Level Fusion Workflow
In score-level fusion, matching scores from both modalities are combined.
Workflow Steps:
1.   Capture face and iris images.
2.   Extract features separately.
3.   Match face features with face template → Score 1.
4.   Match iris features with iris template → Score 2.
5.   Combine scores using sum rule, weighted sum, or average.
6.   Final score compared with threshold.
7.   Accept or Reject decision.
Flow (Text Diagram)
Face → Matching → Score 1
Iris → Matching → Score 2
Score Fusion → Final Score → Decision
2. Mechanisms to Handle Inconsistencies Between Modalities
In multimodal systems, sometimes one biometric modality may fail due to poor
quality data. The system should handle inconsistencies using the following
methods:
Mechanisms:
1.   Weighted Score Fusion
o   Assign higher weight to more reliable modality (e.g., iris more
reliable than face).
2.   Quality-Based Fusion
o   If face image quality is poor, give more importance to iris
recognition.
********** 7 **********
--- page 8 ---
3.   Fallback Mechanism
o   If one modality fails, system authenticates using the other modality.
4.   Adaptive Threshold
o   Threshold changes based on available modalities.
5.   Decision-Level Fusion
o   Final decision taken using AND/OR rules.
Example:
o   AND Rule → Both face and iris must match (high security)
o   OR Rule → Either face or iris match (high usability)
b A network security organization deploys a machine learning–based intrusion   10
detection system to monitor incoming traffic and classify activities as Normal or
Attack. The system generates probability scores indicating the likelihood of
normal behavior. During evaluation, it is observed that the dataset is highly
imbalanced, with significantly more normal traffic than attack instances.
Given the following classification results:
ID   Actual Class   Probability (Normal)
1   Normal   0.93
Q3.   2   Normal   0.88
CO-3,   3   Normal   0.82
SO-6,   4   Normal   0.79
BL-4
5   Normal   0.75
6   Normal   0.71
7   Attack   0.42
8   Normal   0.85
9   Normal   0.78
10   Attack   0.30
Compute TP, FP, TPR, and FPR. Plot ROC curve. Comment on performance
under severe class imbalance.
Marks Bifurcation (10 Marks)
1. TP, FP, TPR, FPR – 6 marks
2. ROC points / ROC curve – 3 Marks
3. Comment on class imbalance – 1 Mark
Answer
********** 8 **********
--- page 9 ---
FPR =
Step Actual   TP   FP   TPR = TP/8
FP/2
Start —   0   0   0   0
1   Normal 1   0   0.125   0
2   Normal 2   0   0.25   0
3   Normal 3   0   0.375   0
4   Normal 4   0   0.50   0
5   Normal 5   0   0.625   0
6   Normal 6   0   0.75   0
7   Normal 7   0   0.875   0
8   Normal 8   0   1   0
9   Attack   8   1   1   0.5
10   Attack   8   2   1   1
Comment on class imbalance – 1 Mark
Since the dataset contains more Normal samples than Attack samples, accuracy
alone may be misleading. ROC curve is a better performance measure for
imbalanced datasets. The ROC curve is close to the top-left corner, indicating
good classifier performance. However, class imbalance may cause the model to
favor the majority class (Normal), so evaluation should focus on TPR, FPR, and
ROC rather than accuracy.
Q4.   a   10
CO-2,3,
SO-4,
BL-4
Study the given iris processing images and answer the following:
a) Identify each stage shown in the images.
********** 9 **********
--- page 10 ---
b) Explain iris segmentation and its challenges.
c) Explain how iris codes are generated and used for authentication.
Ans   Marks Bifurcation (10 Marks)
a) Identify each stage shown in images – 3 Marks
b) Iris segmentation and its challenges – 4 Marks
c) Iris code generation and authentication – 3 Marks
Answer
(a) Identify Each Stage Shown in Iris Processing Images
The iris recognition process consists of the following stages typically shown in iris
processing images:
1. Iris Image Acquisition – Capturing the eye image using a camera.
2. Iris Segmentation – Detecting the iris region by locating the pupil and iris
boundaries.
3. Normalization – Converting the circular iris region into a rectangular form
using polar coordinates.
4. Feature Extraction / Iris Code Generation – Extracting texture features and
generating binary iris code.
5. Matching – Comparing iris code with stored template for authentication.
(b) Iris Segmentation and Its Challenges
Iris Segmentation
Iris segmentation is the process of isolating the iris region from the eye image by
detecting:
•   Pupil boundary
•   Iris outer boundary
•   Eyelids and eyelashes
Techniques used include:
•   Intergro Differential
•   Geodesic
The segmented iris region is then used for further processing.
Challenges in Iris Segmentation
1. Eyelid occlusion – Eyelids may cover part of iris.
2. Eyelashes interference – Eyelashes create noise.
3. Reflections – Light reflections on eye surface.
4. Poor image quality – Low resolution or blur.
5. Off-angle images – Eye not aligned properly.
6. Pupil dilation – Changes iris size.
These challenges may reduce recognition accuracy.
(c) Iris Code Generation and Authentication
After segmentation and normalization, features are extracted from iris texture.
Iris Code Generation
•   Filters such as Gabor filters or wavelets are used.
•   Iris texture is converted into a binary code (iris code).
• Each iris code is unique for each individual.
Authentication Process
1. Capture iris image.
2. Segment and normalize iris.
3. Generate iris code.
4. Compare iris code with stored template.
5. Matching is performed using Hamming Distance.
6.   If matching score is above threshold → Accept.
7. Otherwise → Reject.
Q4.   b   A university plans to implement biometric attendance. Some students have   10
CO-1,3,   worn
********** 10 **********
--- page 11 ---
SO-5,   fingerprints and inconsistent behaviour patterns. Analyze:
BL-3
1. Limitations of physiological and behavioural biometrics
2. Recommend a robust multimodal solution considering cost and usability
Marks Bifurcation (10 Marks)
1. Limitations of physiological biometrics – 3 Marks
2. Limitations of behavioural biometrics – 3 Marks
3. Recommendation of robust multimodal solution (cost & usability) – 4
Marks
Answer
1. Limitations of Physiological Biometrics
Physiological biometrics are based on physical characteristics such as
fingerprint, face, iris, and palmprint. These systems have some limitations:
• Worn fingerprints due to manual work, injuries, or aging may reduce
fingerprint recognition accuracy.
• Face recognition affected by lighting, pose, masks, or facial expressions.
• Iris recognition requires high-quality cameras and controlled environment.
• Sensor hygiene issues in fingerprint scanners.
• Hardware cost may be high for iris scanners.
• Failure to enroll may occur if biometric trait cannot be captured properly.
Thus, physiological biometrics may suffer from noise, environmental effects,
and physical changes.
2. Limitations of Behavioural Biometrics
Behavioural biometrics include signature, keystroke dynamics, voice
recognition, and gait recognition.
Limitations include:
• Behaviour changes over time.
• Voice affected by illness or noise.
• Signature may vary each time.
• Keystroke patterns change with mood, stress, or device.
• Less accurate compared to physiological biometrics.
• Higher False Rejection Rate (FRR).
Thus, behavioural biometrics are not always consistent and may reduce system
reliability.
3. Recommended Robust Multimodal Solution (Cost & Usability)
To handle worn fingerprints and inconsistent behaviour, a multimodal biometric
system should be implemented.
Recommended System:
Face Recognition + Fingerprint + RFID/ID Card
Reasons:
• Face recognition is contactless and fast.
• Fingerprint provides high accuracy.
• RFID/ID card acts as backup authentication.
• Multimodal system reduces FAR and FRR.
• Works even if one biometric fails.
• Cost is moderate compared to iris recognition systems.
• Usability is high for student attendance systems.
Fusion Method:
• Use Score-level fusion or Decision-level fusion.
********** 11 **********
--- page 12 ---
• Example:
o Face OR Fingerprint → Attendance marked
o Both match → High security mode
Q5.   a   Explain the concept of biometric identifiers and discuss their characteristics   10
CO-4,   such as universality, uniqueness, Collectability, Acceptability, Resistance to
SO-6,   Circumvention and permanence.
BL-3
Marks Bifurcation (10 Marks)
1. Concept of biometric identifiers – 5 Marks
2. Characteristics: Universality, Uniqueness, Permanence – 5 Marks
Answer
Concept of Biometric Identifiers
Biometric identifiers are measurable physiological or behavioral characteristics
that can be used to identify or verify the identity of an individual. These
identifiers are unique to each person and are used in biometric authentication
systems such as fingerprint recognition, face recognition, iris recognition,
voice recognition, and signature verification.
Biometric identifiers are used in security systems, attendance systems, banking
authentication, border control, and surveillance systems because they provide
reliable and secure identification.
Examples of biometric identifiers:
• Fingerprint
• Face
• Iris
• Retina
• Voice
• Signature
• Keystroke dynamics
• Gait
Characteristics of Biometric Identifiers
1. Universality
Universality means that every person should possess the biometric trait.
For example, every individual has a face and fingerprints, so these traits satisfy
universality. A biometric system cannot be effective if some people do not
have that trait.
Example: Fingerprint and face recognition satisfy universality.
2. Uniqueness
Uniqueness means that the biometric trait should be different for each
individual.
Even identical twins have different fingerprints and iris patterns. This property
helps in distinguishing one person from another.
Example: Iris patterns and fingerprints are highly unique.
3. Permanence
Permanence means that the biometric trait should remain stable over time and
should not change significantly with age or environment.
Example: Iris and fingerprint patterns remain stable for many years, while voice
and signature may change over time.
Q5.   b   Explain the concept of multimodal biometric systems and discuss how fusion   10
CO-3 ,   techniques improve system reliability and security.
********** 12 **********
--- page 13 ---
SO-7 ,
BL-1,4   A multimodal biometric system employs AND fusion by combining fingerprint
and iris recognition, where the fingerprint system has an accuracy of 90% and the
iris system has an accuracy of 95%. The system processes 1000 authorized access
attempts and 1000 unauthorized access attempts. Based on this information,
calculate the combined system accuracy under AND fusion. Further, determine
the number of false rejections and false acceptances produced by the system.
Marks Bifurcation (10 Marks)
1. Concept of multimodal biometric systems and fusion techniques – 5 Marks
2. AND fusion accuracy, false rejections, and false acceptances calculation –
5 Marks
Answer
Multimodal Biometric Systems and Fusion Techniques
A multimodal biometric system uses more than one biometric trait such as
fingerprint, face, iris, or voice for authentication. These systems improve
accuracy, reliability, and security compared to unimodal biometric systems
because multiple biometric traits are used for identification.
Fusion techniques are used to combine information from multiple biometric
systems. Fusion can be performed at different levels such as feature level, score
level, and decision level. Fusion improves system reliability by reducing False
Acceptance Rate (FAR) and False Rejection Rate (FRR). It also improves
security because it is difficult to spoof multiple biometric traits. Multimodal
systems also work even if one biometric trait fails due to noise or poor quality
data.
AND Fusion Calculation
Given:
•   Fingerprint accuracy = 90% = 0.9
•   Iris accuracy = 95% = 0.95
• Authorized attempts = 1000
• Unauthorized attempts = 1000
• Fusion type = AND fusion
********** 13 **********
--- page 14 ---
Q6.   a   A multimodal biometric system uses weighted fusion by combining face and   10
CO-1,   fingerprint recognition, where the face recognition system has an accuracy of 92%
SO-1,   (weight = 0.4) and the fingerprint recognition system has an accuracy of 97%
BL-3   (weight = 0.6). The system processes 1200 authorized access attempts and 800
unauthorized access attempts.
Based on the above information, answer the following:
a) Calculate the fused system accuracy.
b) Determine the number of correct matches and false rejections for authorized
users.
c) Compute the number of false acceptances for unauthorized users.
Marks Bifurcation (10 Marks)
1. Fused accuracy calculation using weighted fusion – 5 Marks
2. Correct matches, false rejections, and false acceptances calculation – 5
Marks
Answer
Given Data
• Face accuracy = 92% = 0.92, weight = 0.4
•   Fingerprint accuracy = 97% = 0.97, weight = 0.6
• Authorized attempts = 1200
• Unauthorized attempts = 800
b   Describe the process of minutiae-based fingerprint matching by explaining the   10
Q6.   key stages involved, namely alignment, correspondence, and match score
CO-2,3,   generation. Discuss the role of the Hough Transform in achieving alignment
SO-6,
BL-2   between two fingerprint images. Further, analyze how spatial transformations
(such as translation and rotation) and the selection of matching thresholds
********** 14 **********
--- page 15 ---
influence the accuracy and overall performance of the fingerprint recognition
system.
Marks Bifurcation (10 Marks)
1. Minutiae-based fingerprint matching stages (alignment, correspondence,
match score) – 5 Marks
2. Role of Hough Transform, spatial transformations, and matching
threshold on system performance – 5 Marks
Answer
Minutiae-Based Fingerprint Matching
Minutiae-based fingerprint matching is a widely used method in fingerprint
recognition systems. It compares fingerprint images based on minutiae points,
which are ridge endings and bifurcations.
The fingerprint matching process consists of three main stages: alignment,
correspondence, and match score generation.
1. Alignment Stage
In the alignment stage, two fingerprint images (input fingerprint and stored
template) are aligned so that their minutiae points overlap as closely as possible.
Since fingerprint images may be captured at different positions or orientations,
alignment is necessary before matching.
Alignment compensates for:
•   Translation (shift in x and y direction)
•   Rotation (angle change)
• Small scaling differences
Role of Hough Transform
The Hough Transform is used to estimate the best alignment parameters
between two fingerprint images. It finds the transformation parameters such as
rotation angle and translation values that maximize the number of matching
minutiae points between two fingerprints. This helps in aligning the fingerprints
correctly before matching.
2. Correspondence Stage
In this stage, minutiae points from the input fingerprint are compared with
minutiae points in the stored template.
Two minutiae points are considered matched if:
•   Their spatial distance is within a tolerance limit.
•   Their orientation difference is within an allowed range.
•   Their minutiae type (ridge ending or bifurcation) is the same.
This stage determines how many minutiae points correspond between two
fingerprints.
3. Match Score Generation
After finding corresponding minutiae points, a match score is calculated.
If the match score is greater than a predefined threshold, the fingerprints are
considered matched; otherwise, they are rejected.
Influence of Spatial Transformations and Threshold
Spatial Transformations
Fingerprint images may differ due to translation and rotation. Proper alignment
using spatial transformations improves matching accuracy. Poor alignment may
lead to incorrect matching and increase False Rejection Rate (FRR).
********** 15 **********
--- page 16 ---
Matching Threshold
The threshold determines whether a fingerprint is accepted or rejected.
• High threshold → increases security but increases False Rejection Rate.
• Low threshold → decreases False Rejection Rate but increases False
Acceptance Rate.
• Optimal threshold balances FAR and FRR.
Q7.   a   A biometric identification system is deployed in a secure facility to identify   10
CO-1,3,   individuals from a large database. During evaluation, each probe image
SO-2,   generates a ranked list of candidate identities. Total number of probe samples are
BL-4   715. The distribution of correct matches at different ranks is recorded as follows:
Number of Correct
Rank
Identifications
R1   280
R2   120
R3   90
R4   70
R5   60
R6   40
R7   25
R8   15
R9   10
R10   5
Based on the above data, answer the following:
a) Compute the cumulative number of correct identifications up to each rank.
b) Calculate the cumulative match accuracy (%) for each rank from R1 to R10.
c) Plot the Cumulative Match Characteristic (CMC) curve.
d) Determine the minimum rank at which at least 95% identification accuracy is
achieved.
e) Analyze the system performance by interpreting Rank-1 accuracy and discuss
how improvements in feature extraction or matching algorithms could enhance
CMC performance.
Marks Bifurcation (10 Marks)
1. Cumulative correct identifications – 2 Marks
2. Cumulative match accuracy (%) – 2 Marks
3. CMC curve plotting – 2 Marks
4. Rank for 95% accuracy – 2 Marks
5. Performance analysis & Rank-1 discussion – 2 Marks
(a) Cumulative Correct Identifications
Rank   Correct   Cumulative Correct
R1   280   280
R2   120   400
R3   90   490
R4   70   560
********** 16 **********
--- page 17 ---
R5   60   620
R6   40   660
R7   25   685
R8   15   700
R9   10   710
R10   5   715
(b) Cumulative Match Accuracy (%)
Rank   Cumulative Correct   Accuracy (%)
R1   280   39.16
R2   400   55.94
R3   490   68.53
R4   560   78.32
R5   620   86.71
R6   660   92.31
R7   685   95.80
R8   700   97.90
R9   710   99.30
R10   715   100
(c) CMC Curve
Plot Rank vs Cumulative Match Accuracy.
The CMC curve increases with rank and approaches 100% at Rank 10.
CMC Points:
(1,39.16), (2,55.94), (3,68.53), (4,78.32), (5,86.71), (6,92.31), (7,95.80), (8,97.90),
(9,99.30), (10,100)
********** 17 **********
--- page 18 ---
(d) Rank for ≥ 95% Identification Accuracy
From the table, accuracy ≥ 95% occurs at Rank 7.
Minimum Rank = R7
(e) System Performance Analysis
• Rank-1 accuracy:
• Rank-1 accuracy is moderate, indicating correct identity appears at first
position for 39% of probes.
• System performance can be improved by:
o Better feature extraction
o Improved matching algorithms
o Deep learning-based recognition
o Better preprocessing and alignment
o Multimodal biometric systems
Improving feature extraction increases Rank-1 accuracy and improves the CMC
curve.
b A hospital deploys a biometric system using iris recognition to identify patients   10
and access medical records. While the system provides high accuracy, issues arise
when patients have difficulty positioning themselves correctly or when the system
fails due to reflections or lighting variations. This results in delays in patient
Q7.   processing.
CO-3,
SO-7,   Answer the following based on above scenario-
BL-4   a) Identify operational challenges in iris-based systems.
b) Discuss how environmental and user-related factors affect system performance.
c) Evaluate the advantages of iris recognition over other modalities.
d) Propose system improvements to enhance usability and efficiency.
Marks Bifurcation (10 Marks)
a)   Operational   challenges   in   iris-based   systems   –   2   Marks
b) Environmental and user-related factors affecting performance – 3 Marks
c) Advantages of   iris recognition over other modalities – 2 Marks
d) Proposed system improvements for usability and efficiency – 3 Marks
Answer
(a) Operational Challenges in Iris-Based Systems (2 Marks)
Operational challenges in iris recognition systems include:
•   Difficulty in correct eye positioning
•   Reflections from glasses or eye surface
•   Lighting variations affecting iris image capture
• Motion blur due to user movement
********** 18 **********
--- page 19 ---
•   Failure to capture iris for elderly or sick patients
• System delays due to repeated capture attempts
These challenges reduce system efficiency and increase authentication time.
(b) Environmental and User-Related Factors Affecting System Performance
(3 Marks)
Environmental Factors:
• Poor illumination
•   Light reflections
• Camera distance and focus
• Shadows and lighting variations
User-Related Factors:
• Improper eye alignment
• Eye movement during capture
• Wearing glasses or contact lenses
• Medical eye conditions
• Lack of user cooperation
These factors lead to poor image quality, segmentation errors, increased False
Rejection Rate (FRR), and slower system performance.
(c) Advantages of Iris Recognition Over Other Modalities (2 Marks)
• Very high accuracy
• Highly unique iris patterns
•   Stable over lifetime (high permanence)
•   Contactless biometric system
•   Difficult to spoof
• Low False Acceptance Rate (FAR)
•   Suitable for high-security applications
Iris recognition is more accurate and secure than fingerprint and face recognition
systems.
(d) Proposed System Improvements to Enhance Usability and Efficiency (3
Marks)
• Automatic eye detection and alignment system
•   Proper lighting and anti-reflection cameras
• User guidance interface for positioning
• Multimodal biometrics (Face + Iris)
•   Quality assessment before image capture
•   Faster processing algorithms
•   Multiple automatic capture attempts
•   High-resolution cameras
These improvements increase usability, reduce delays, and improve system
efficiency.
********** 19 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 710e5b319ece

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_AIDS_7056/Biometrics/ANS_Biometrics(702CO0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE AND DATA
SCIENCE)
Year: III/Sem 5 Re-exam(Exam Year: 2025-2026)
Subject: Biometrics
Date: 10 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Question No. _1_ is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. In all _5_ questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1   Section A (Compulsory Question)   Marks
CO-2,3, a   Identify the main components of a biometric system and their functions.   5
SO-1,
BL-2
1 mark for each.
1.   Sensor / Data Capture: Captures the biometric trait (e.g., fingerprint, face, iris).
2.   Feature Extraction: Processes the captured data to extract unique features.
3.   Database / Template Storage: Stores the extracted features (templates) for
comparison.
4.   Matching / Decision Module: Compares input features with stored templates and
computes similarity.
5.   System Output / Decision: Provides the final result (accept or reject the identity).
CO–4, b   Define multimodal biometric systems and discuss their significance in high-security   5
SO-2,   areas.
BL-2
Marks Distribution:
1. Definition of multimodal biometric system: 2 marks
2. Significance / advantages in high-security areas: 3 marks
Answer (Brief):
1. Definition (2 marks):
A multimodal biometric system uses two or more biometric traits (e.g., fingerprint
+ iris, face + palm vein) for verifying an individual's identity.
2. Significance in High-Security Areas (3 marks):
i.   Higher Accuracy: Reduces false acceptance and false rejection rates.
ii.   Improved Security: Difficult for imposters to spoof multiple traits simultaneously.
iii.   Robustness: Works even if one modality fails or is unavailable.
********** 1 **********
--- page 2 ---
iv.   Flexibility: Can handle variations in environment or sensor quality.
CO-3, c   Describe how biometric system performance is influenced by parameters such as FMR,   5
SO-6,   FNMR, and Threshold.
BL-2
Marks Distribution:
•   Definition of FMR, FNMR, Threshold: 2 marks
•   Effect on system performance: 3 marks
Answer (Brief):
1. Definitions (2 marks):
o FMR (False Match Rate): Probability that an imposter is incorrectly
accepted.
o FNMR (False Non-Match Rate): Probability that a genuine user is
incorrectly rejected.
o Threshold: Predefined similarity score above which a match is accepted.
2. Effect on Performance (3 marks):
o Higher Threshold: Reduces FMR (more secure) but increases FNMR (less
user-friendly).
o Lower Threshold: Reduces FNMR (more user-friendly) but increases
FMR (less secure).
o Balanced Threshold: Optimizes trade-off between security and usability.
CO-1,3, d   Explain the use of biometrics in surveillance systems for law enforcement.   5
SO-4,
BL-2,3
Marks Distribution:
•   Definition / role of biometrics in surveillance: 2 marks
• Key applications / significance for law enforcement: 3 marks
Answer (Brief):
1. Role of Biometrics (2 marks):
Biometric systems capture and analyze unique traits (e.g., face, iris, fingerprints)
from individuals to identify or verify them automatically in public or restricted
areas.
2. Significance for Law Enforcement (3 marks):
o Criminal Identification: Detects known offenders in real-time.
o Tracking Suspects: Monitors movements in public spaces using facial
recognition or gait analysis.
o Access Control & Security: Prevents unauthorized entry in sensitive
zones.
o Evidence Collection: Stores biometric data for investigations and legal
proceedings.
Section B (Attempt any four questions)
********** 2 **********
--- page 3 ---
Q2.   a   A smartphone uses a stored fingerprint template to check if the person trying to unlock   5
CO-1,   the device is the authorized owner. State whether this scenario is an identification or
SO-1,   verification process. Give a brief justification.
BL-4
Marks Distribution:
•   State the process correctly: 2 marks
•   Justification: 3 marks
Answer (Brief):
1. Process Type: Verification
2. Justification (3 marks):
o The system checks if the claimed identity (authorized owner) matches the
stored fingerprint template.
o   It performs a one-to-one comparison, unlike identification, which
compares the input against all templates in a database.
o Ensures that only the authorized user can unlock the device.
Q2.   b   Discuss any two challenges in iris segmentation and explain how segmentation   5
CO-2,3,   algorithms address them.
SO-6,
BL-2
Marks Distribution:
• Mention two challenges: 2 marks (1 mark each)
•   Explanation of how algorithms address them: 3 marks (1.5 marks each)
Answer (Brief):
1. Challenge 1 – Eyelid / Eyelash Occlusion:
o Problem: Upper/lower eyelids or eyelashes may cover parts of the iris,
causing incomplete or noisy data.
o Solution: Segmentation algorithms use edge detection and masking
techniques to isolate the iris region and ignore occluded areas.
2. Challenge 2 – Pupil Dilation / Variable Illumination:
o Problem: Changes in pupil size or lighting can distort iris patterns.
o Solution: Algorithms apply normalization techniques (e.g., Daugman’s
rubber sheet model) to map the iris into a fixed-size pattern for consistent
feature extraction.
Q2.   c   Illustrate the biometric system design cycle by organizing its major stages in logical   5
CO-3,   order. For each stage, briefly explain its role and importance in ensuring system
SO-2,   accuracy, usability, and security.
BL-2
Marks Distribution:
•   Correct identification of major stages in logical order: 2 marks
•   Brief explanation of role and importance for each stage: 3 marks
Answer (Brief):
********** 3 **********
--- page 4 ---
Major Stages of Biometric System Design Cycle:
1. Data Capture / Sensor Acquisition (Role: Accuracy & Usability)
o Captures biometric traits (fingerprint, face, iris) from users.
o High-quality capture ensures accurate matching and smooth user
experience.
2. Preprocessing (Role: Accuracy & Security)
o Removes noise, enhances images, and normalizes data.
o Improves system reliability and prevents errors due to poor-quality input.
3. Feature Extraction (Role: Accuracy & Security)
o Extracts unique patterns from the captured data.
o   Critical for accurate identification/verification and resistance to spoofing.
4. Template Storage (Role: Security & Usability)
o Stores extracted features securely in a database.
o Ensures data privacy while allowing fast retrieval for comparisons.
5. Matching / Decision (Role: Accuracy & Usability)
o Compares input features with stored templates and computes similarity.
o Determines identity reliably, balancing false acceptance/rejection rates.
6. System Feedback / Output (Role: Usability & Security)
o Provides acceptance/rejection results or alerts.
o Ensures user awareness and triggers security measures if needed.
Q2.   d   Compare the performance of face recognition and iris recognition systems in terms   5
CO-3,   of accuracy, cost, and deployability.
SO-4,
BL-3
Marks Distribution:
• Comparison for accuracy: 2 marks
• Comparison for cost: 1 mark
• Comparison for deployability: 2 marks
Answer
(Brief):
Parameter   Face Recognition   Iris Recognition
Moderate; affected   Very high; unique iris
by lighting, pose,   patterns lead to low
Accuracy   and expression   FMR/FNMR
Low to moderate;
uses standard   High; requires
Cost   cameras   specialized iris scanners
Easy; can be
integrated into   Moderate; needs
smartphones, CCTV, controlled environment
Deployability and laptops   and user cooperation
Q3.   a   A hospital plans to implement a multimodal biometric system for patient identification,   10
CO-4,   combining face recognition and palm vein scanning. The hospital has experienced
SO-2,   misidentification of patients due to low-quality images from older cameras and
BL-4
variations in hand positioning. Management wants a reliable workflow that reduces
errors while maintaining patient privacy.
********** 4 **********
--- page 5 ---
Answer the following-
a) Design a detailed multimodal system workflow, showing how decision-level and
score-level fusion will handle mismatches between modalities.
b) Propose error handling techniques for situations where one modality fails or
produces low-confidence results.
Marks Distribution:
• Workflow design with fusion explanation: 6 marks
•   Error handling techniques: 4 marks
Answer (Brief but Complete):
a) Multimodal System Workflow (6 marks)
1. Data Capture / Acquisition:
o Capture face image using camera and palm vein image using NIR sensor.
o Preprocessing applied to enhance image quality (illumination correction,
hand alignment).
2. Feature Extraction:
o Extract unique facial features (e.g., eigenfaces, deep learning
embeddings).
o Extract palm vein patterns (vein bifurcations, texture features).
3. Matching:
o Compare each modality’s input features with stored templates.
o Compute similarity scores for face and palm vein separately.
4. Score-Level Fusion:
o Combine similarity scores from both modalities using weighted sum or
logistic regression.
o Ensures partial mismatches are handled by giving appropriate weight to
the more reliable modality.
5. Decision-Level Fusion:
o Make final accept/reject decision based on majority voting or threshold
rules if one modality strongly disagrees.
o Enhances reliability when modalities conflict.
6. System Output:
o Display patient ID or trigger security alert in case of low-confidence
matching.
b) Error Handling Techniques (4 marks)
1. Fallback Mechanism:
o   If one modality fails (e.g., poor face image), rely on the other modality
with higher confidence score.
2. Re-Capture Prompt:
o Prompt patient to re-capture face or palm image in case of low-quality
input.
3. Threshold Adjustment:
o Dynamically adjust matching thresholds based on sensor quality and
environmental conditions.
4. Audit Logging & Manual Verification:
o Log failed attempts and allow human verification for critical cases to
maintain accuracy and privacy.
********** 5 **********
--- page 6 ---
b   The National Health Institute has implemented a fingerprint-based access control   10
system to ensure that only authorized doctors and nurses can enter critical care units.
The system predicts access validity based on fingerprint matching probabilities recorded
below:
Probability of
Staff ID   Ground Truth
Authorized Access
1   Authorized   0.94
2   Unauthorized   0.15
3   Authorized   0.88
Q3.
CO-3,   4   Unauthorized   0.31
SO-6,   5   Authorized   0.74
BL-4   6   Unauthorized   0.44
7   Authorized   0.68
8   Unauthorized   0.22
9   Unauthorized   0.18
10   Authorized   0.91
Do the following:
1.   Compute the True Positives (TP), False Positives (FP), True Positive Rate (TPR),
and False Positive Rate (FPR).
2.   Use the computed values to plot the ROC curve.
Marks Distribution:
•   Correct computation of TP, FP: 4 marks
•   Correct calculation of TPR and FPR: 4 marks
• ROC curve plotted correctly: 2 marks
Roll   Probab
No   Status   ility   TP   FP   TPR   FPR
Regula
4   r   0.92   1   0   0.2   0
Regula
10   r   0.88   2   0   0.4   0
Regula
1   r   0.85   3   0   0.6   0
Regula
5   r   0.78   4   0   0.8   0
Regula
7   r   0.67   5   0   1   0
Irregul
6 ar   0.45   5   1   1   0.2
Irregul
3 ar   0.34   5   2   1   0.4
Irregul
8 ar   0.28   5   3   1   0.6
Irregul
9 ar   0.19   5   4   1   0.8
********** 6 **********
--- page 7 ---
Irregul
2 ar   0.12   5   5   1   1
Q4.   a   A school is planning to implement biometric attendance for students. Some students   10
CO-2,3,   have similar facial features, and some have difficulty maintaining a consistent typing
SO-4,   pattern on shared devices. Using this scenario, analyze the advantages and limitations
BL-4   of physiological (fingerprint, iris) and behavioral (keystroke, gait) biometric traits.
Recommend a practical and robust system design considering accuracy, cost, and user
convenience.
Marks Distribution (10 Marks Total)
•   Explanation of traits (physiological & behavioral) – 3 marks
• Advantages and limitations – 4 marks
• System design recommendation – 3 marks
Answer (Brief)
Physiological traits:
• Advantages: Stable, unique, and accurate (fingerprint, iris).
•   Limitations: Require sensors; affected by dirt, lighting, or eye obstruction.
Behavioral traits:
• Advantages: Non-intrusive and easy to collect.
•   Limitations: Inconsistent due to stress, fatigue, or shared devices.
Recommended System:
Adopt a multimodal system using fingerprint + face recognition.
********** 7 **********
--- page 8 ---
It offers high accuracy, moderate cost, and easy usability, making it ideal for school
attendance with minimal errors.
Q4.   b   “An organization uses face recognition for access control. During a system audit, false   10
CO-1,3,   acceptances are detected during low-light conditions”.
SO-5,   Analyze the environmental factors influencing biometric reliability and propose
BL-3   improvement strategies.
Marks Distribution
• Environmental factors affecting reliability – 5 marks
• Improvement strategies – 5 marks
Answer (Brief)
Environmental Factors:
•   Lighting conditions: Poor or uneven illumination affects facial feature detection.
• Camera quality: Low-resolution sensors reduce image clarity.
• Background and pose variations: Shadows or user movement cause feature
mismatch.
• Temperature and humidity: Can impact infrared sensors or camera performance.
Improvement Strategies:
• Use infrared or 3D face recognition for better performance in low light.
• Implement adaptive illumination and image preprocessing (contrast
enhancement).
• Conduct regular calibration and retraining with diverse lighting data.
• Combine with a secondary biometric (e.g., fingerprint) for higher accuracy and
security.
Q5.   a   City Hospital secures its high-risk wards with a multimodal biometric system using   10
CO-4,   fingerprint (FMR = 3%) and palm vein scanning (FMR = 1%).
SO-6,   Do the following based on the question given-
BL-3   a) Calculate the combined FMR using AND fusion.
b) Out of 600 unauthorized access attempts, how many are likely to be falsely
accepted?
Marks Distribution
•   Combined FMR using AND fusion – 6 marks
•   Number of false acceptances (calculation and interpretation) – 4 marks
********** 8 **********
--- page 9 ---
b   What is uncertainty in the system?   10
Q5.   An airport security checkpoint uses iris recognition to verify travelers’ identities.
CO-3 ,   Recently, due to inconsistent lighting and camera alignment, the system has shown
SO-7 ,   increased false non-match rates (FNMR). Security authorities need to assess the
BL-1,4
system performance rigorously and propose improvements for operational reliability.
Analyze systematic errors, sampling errors, and environmental factors that affect false
non match and false match rate in the airport scenario.
Marks Distribution (10 Marks Total)
•   Analysis of errors & factors (systematic, sampling, environmental) – 4 marks
• Assessment steps & improvement strategies (operational recommendations) – 6
marks
Definition of Uncertainty
Uncertainty = the lack of perfect knowledge about whether a biometric decision (match /
non-match) is correct. It arises from measurement noise, model/algorithm limitations,
variability in users or sensors, and sampling variability — and it directly causes FNMR
and FMR to deviate from ideal values.
Systematic Errors (bias in system design):
• Camera misalignment or poor calibration leads to incomplete iris capture,
increasing FNMR.
********** 9 **********
--- page 10 ---
•   Incorrect threshold settings or algorithmic bias may raise FMR or FNMR for
certain users.
• Outdated templates or inconsistent enrollment procedures reduce matching
accuracy.
Sampling Errors (data-related issues):
• Limited or non-representative training data fails to capture variations in lighting
and demographics.
• Few enrollment samples increase intra-user variability, causing higher FNMR.
• Small or skewed evaluation sets give unreliable estimates of FMR/FNMR.
Environmental Factors:
•   Inconsistent lighting, reflections, or shadows distort iris texture.
• Changes in user distance, angle, or movement reduce capture quality.
•   Dust, humidity, or glare on camera lenses impact recognition.
Q6.   a   Explain how changes in ambient conditions, such as inconsistent illumination or   10
CO-1,   background noise, influence the performance of biometric systems. Provide examples
SO-1,   for at least two modalities.
BL-3
Marks Distribution Explanation of ambient conditions and their impact – 4
marks
•   Effect on two biometric modalities (with examples) – 4 marks
• Mitigation or improvement strategies / clarity – 2 marks
Ambient conditions directly affect the quality of biometric data capture. Variations in
lighting, temperature, noise, or background can distort the input signal, leading to false
matches or false rejections.
Examples:
1. Face Recognition:
o Inconsistent illumination (e.g., shadows, glare, low light) alters facial
contrast and feature visibility.
o Results in higher False Non-Match Rate (FNMR) since stored templates
differ from real-time captures.
o Mitigation: Use infrared or 3D cameras, and apply image normalization or
illumination correction.
2. Voice Recognition:
o Background noise from crowds or announcements masks speech patterns.
o Causes false matches (system misidentifies another speaker) or false
rejections (fails to recognize genuine user).
o Mitigation: Employ noise-cancellation microphones and adaptive signal
filtering.
********** 10 **********
--- page 11 ---
Q6.   b   Mention at least two challenges that affect accurate face detection. Discuss the   10
CO-2,3,   following components of the Viola-Jones face detector-
SO-6,   a) Haar Features
BL-2   b) Integral Image
Marks Distribution (10 Marks Total)
•   Challenges in accurate face detection – 5 marks
•   Explanation of Haar Features & Integral Image – 5 marks
Challenges in Accurate Face Detection (5 Marks):
1. Illumination Variation: Changes in lighting cause shadows or bright spots,
altering facial feature contrast.
2. Pose Variation: Faces tilted, rotated, or partially occluded reduce detection
accuracy.
3. Facial Expressions: Smiling or frowning changes local feature geometry.
4. Background Clutter: Complex scenes may confuse detectors with similar patterns.
5. Low Image Quality: Blurriness or low resolution affects feature extraction.
Viola–Jones Components (5 Marks):
a) Haar Features:
• Simple rectangular features representing edge, line, and texture differences (e.g.,
eyes vs. cheeks).
• Used to distinguish facial regions efficiently.
• Example: A two-rectangle Haar feature detects the eye region as darker than the
upper cheeks.
b) Integral Image:
• A precomputed image where each pixel stores the sum of all pixel intensities
above and to the left.
• Allows rapid calculation of Haar feature values in constant time.
•   Significantly speeds up detection, enabling real-time face detection performance.
Q7.   a   A secure access control system integrates face recognition and voice recognition   10
CO-1,3,   modules using a decision-level “AND” fusion rule to improve authentication reliability.
SO-2,   The performance metrics for each modality are as follows: the face recognition system
BL-4   has an accuracy of 92%, while the voice recognition system achieves 88% accuracy.
During a performance evaluation, the system processed 1200 genuine access attempts
(from authorized users) and 800 impostor attempts (from unauthorized users).
Based on above statements do the following:
(a) Calculate the overall system accuracy when the “AND” fusion rule is applied.
(b) Determine the expected number of correct genuine matches and false rejections
under this fusion condition.
(c) Compute the expected number of correct impostor rejections and false acceptances,
assuming independence between the two modalities.
Q7.   b   A corporate office implemented a facial recognition system for entry to secure areas. To   10
CO-3,   evaluate the system, 600 employees were tested. For each probe sample, the system
********** 11 **********
--- page 12 ---
SO-7,   returned a ranked list of matches. The number of employees whose correct identity
BL-4   appeared at each rank is as follows:
Rank   of Number of
Genuine   Employees
Match   Matched
R1   350
R2   100
R3   60
R4   40
R5   25
R6   15
R7   5
R8   5
R9   0
R10   0
Tasks:
1.   Compute the cumulative genuine matches for each rank.
2.   Calculate the cumulative recognition percentage for R1 to R10.
3.   Plot the CMC curve.
4.   Determine the minimum rank needed to achieve 95% correct identification.
5.   Discuss the system’s effectiveness, emphasizing rank-1 performance, and propose
enhancements to reduce false negatives.
Marks distribution (suggested — total 10)
1. Compute cumulative genuine matches for each rank — 2 marks
2. Calculate cumulative recognition percentage R1–R10 — 2 marks
3. Plot the CMC curve (labelled, readable) — 2 marks
4. Determine minimum rank to reach ≥95% identification — 1.5 marks
5. Discussion of effectiveness and recommended enhancements — 2.5 marks
Given data (summary)
•   Total employees tested = 600
• Matches at ranks R1..R10 = [350, 100, 60, 40, 25, 15, 5, 5, 0, 0]
1) Cumulative genuine matches (step-by-step, brief) — 2 marks
Compute cumulative sum of matches by rank:
• R1: 350
• R2: 350 + 100 = 450
• R3: 450 + 60 = 510
• R4: 510 + 40 = 550
• R5: 550 + 25 = 575
• R6: 575 + 15 = 590
• R7: 590 + 5 = 595
********** 12 **********
--- page 13 ---
• R8: 595 + 5 = 600
• R9: 600 + 0 = 600
• R10: 600 + 0 = 600
(These are the cumulative genuine matches at each rank.)
2) Cumulative recognition percentage R1–R10 — 2 marks
Percentage = (Cumulative matches / 600) × 100:
• R1: 350 / 600 = 58.33%
• R2: 450 / 600 = 75.00%
• R3: 510 / 600 = 85.00%
• R4: 550 / 600 = 91.67%
• R5: 575 / 600 = 95.83%
• R6: 590 / 600 = 98.33%
• R7: 595 / 600 = 99.17%
• R8: 600 / 600 = 100.00%
• R9: 600 / 600 = 100.00%
• R10: 600 / 600 = 100.00%
Cumulati
Cumulat
ve
Rank   ive
Recogniti
Matches
on
0.583333
R1   350
33
R2   450   0.75
R3   510   0.85
0.916666
R4   550
67
0.958333
R5   575
33
0.983333
R6   590
33
0.991666
R7   595
67
R8   600   1
R9   600   1
R10   600   1
•
********** 13 **********
--- page 14 ---
3) CMC curve — 2 marks
4) Minimum rank to achieve 95% correct identification — 1.5 marks
• Minimum rank = Rank 5, because cumulative recognition at R5 = 95.83%
which is the first rank ≥ 95%.
5) Discussion (effectiveness, emphasis on rank-1) and proposed enhancements — 2.5
marks
Key observations (brief, pointwise):
• Rank-1 = 58.33%: This is modest — only ~58% of employees are identified
correctly at the top match. For secure-entry use, a higher rank-1 rate (typically
>90% for frictionless entry) is desirable.
• Rank-5 = 95.83%: The system finds the correct identity within top-5 for most
users (good for retrieval/forensic scenarios), but not for automatic one-to-one
authentication at the door.
• False negatives (genuine users not matched top-1) are common here and may
cause user friction or fallback to manual checks.
Practical recommendations to reduce false negatives / improve rank-1 (forward-
thinking, prioritized):
1. Improve enrollment quality: re-capture multiple high-quality images per
employee with variation in pose, expression, illumination; keep templates
updated (periodic re-enrollment).
2. Preprocessing pipeline: better face alignment, normalization, and
illumination correction to make probe vs template more consistent.
3. Algorithm upgrade / fine-tuning: use state-of-the-art deep face embeddings
and fine-tune on a representative dataset from the office (domain adaptation).
4. Score/threshold tuning: if operating as 1:1 verification, tune decision
threshold to trade FMR/FNMR appropriately for security vs convenience. For
identification (1:N), consider using a stricter secondary check for near-ties.
********** 14 **********
--- page 15 ---
5. Multi-stage matcher (cascaded): fast lightweight matcher to shortlist +
stronger matcher for top candidates — can improve top-1 by reducing
confusion.
6. Multi-modal fusion: add another biometric (e.g., access card, fingerprint) or
contextual signals (time/location) for fusion to increase reliability.
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 8b910e1f4b29

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_Computer_7002/Biometrics/ANS_Biometrics(702CO0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (23 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Biometrics
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 23 pages.
2. 1.   Question No. _1_ is compulsory.
3. 2.   Out of remaining questions, attempt any 4 questions.
4. 3.   In all _5_ questions to be attempted.
5. 4.   All questions carry equal marks.
6. 5.   Answer to each new question to be started on a fresh page.
7. 6.   Figures in brackets on the right hand side indicate full marks.
8. 7.   Assume Suitable data if necessary.
Q1 Section A (Compulsory Question)   Marks
CO-2,3, a   Outline the techniques for IRIS Segmentation. Mention the advantages and   5
SO-1,   limitations of each. For the image given, suggest with reasons the best suited
BL-2   segmentation technique to be applied.
Marks:
3 Marks- List with Advantages and limitation
2 marks: Geodesic Active Contour technique
Technique   Main Idea   Advantage   Limitation
Integro-   Detect circular
Highly   Computational
Differential   boundaries using
accurate   cost
Operator   gradient
Circular Hough Detect circles in
Robust   Slow
Transform   edge images
********** 1 **********
--- page 2 ---
Detect boundaries   Sensitive to
Edge Detection   Simple
using gradients   noise
Active Contour Curve evolves to   Needs
Flexible
(Snake)   fit boundary   initialization
Geodesic   Level-set based   Handles
Complex
Active Contour contour evolution occlusion
Intensity-based
Thresholding   Fast   Less accurate
segmentation
Region   Expand from seed Good for   Sensitive to
Growing   region   clear regions seed
CNN-based   Very   Requires
Deep Learning
segmentation   accurate   training data
Advantages of GAC:
• Handles complex and irregular boundaries.
• Robust to noise and occlusion.
• Automatically evolves contour toward object edges.
• Allows contour splitting and merging.
• Provides accurate segmentation results.
b   Explain the limitations of Unimodal Systems and suggest solutions to mitigate   5
them.
Marks:
2 Marks- List of limitations
3 marks: Advantages of Multimodal Systems
Unimodal systems face issues such as inter class similarity, intra-class
variation, spoofing and non-universality.
Some other limitations of a unimodal system are listed below.
CO–4,   i. No Flexibility as only one feature has been enrolled.
SO-2,   ii.   Noisy Biometric Data.
BL-2   iii.   Failure to enrol rate with increased population.
iv.   Unacceptable error rates using a single biometric feature.
v.   Easy to employ fake biometric.
Solutions to mitigate the limitations
i.   Cancelable biometrics (apply transformations to biometric data)
ii.   Multi-factor authentication (biometric + PIN/password)
iii.   Template protection & encryption
iv.   Dynamic / behavioral biometrics (gait, keystroke dynamics)
v.   Multimodal
********** 2 **********
--- page 3 ---
c   Illustrate a block diagram to depict a multi biometric system which combines   5
fingerprint matcher score with iris matcher score. Under what circumstances
are score level fusion optimum?
Marks:
2 Marks- Block diagram
3 marks: Reasons to consider score level fusion.
CO-3,
SO-6,
BL-2
Score level fusion is optimum when:
• Multiple biometric systems output matching scores.
• Feature vectors are not accessible or incompatible.
• A balance between performance and complexity is required.
• Scores can be normalized to a common range.
• Multiple algorithms analyze the same or different biometric traits.
d A face recognition system processed 800 genuine attempts and 400 impostor   5
attempts. The system falsely rejected 150 genuine attempts and falsely
accepted 50 impostor attempts.
Solve:
a) FNMR (%)
b) FMR (%)
Discuss the robustness of such a biometric system.
CO-1,3,   Marks:
SO-4,   3 marks for calculations
BL-3   2 mark for discussion
FMR= 50/400 = 0.125
FNMR= 150/800 = 0.185
********** 3 **********
--- page 4 ---
Interpretation:
1. False Match Rate (FMR = 12.5%)
• This means 12.5% of unauthorized users are incorrectly accepted.
• This is quite high, indicating poor security.
• A robust system should ideally have very low FMR (close to 0%).
2. False Non-Match Rate (FNMR ≈ 18.75%)
• This means 18.75% of genuine users are incorrectly rejected.
• This is also high, indicating poor usability/user convenience.
System Robustness:
• A robust biometric system should have:
o Low FMR → High security
o Low FNMR → High usability
As Both FMR and FNMR are high
• The system is:
o Not secure (high false acceptance)
o Not user-friendly (high false rejection)
Conclusion:
The biometric system is not robust.
It suffers from both high security risk and poor user convenience, making it
unreliable for real-world deployment.
Section B (Attempt any four questions)
Q2. a   5
CO-1,   Make use of the graph given below which shows the verification performance
SO-1,   of a biometric system to discuss the outcome when the system must decide
BL-3   whether to accept or reject the null hypothesis (H₀).
Assume an appropriate decision threshold and explain your reasoning.
********** 4 **********
--- page 5 ---
Marks:
2 marks Interpretation of the graph
3 marks explanation and reasoning
Answer should discuss the following points.
• H₀ represents genuine user scores, H₁ represents impostor scores.
• A match threshold determines whether the claim is accepted or rejected.
• FNMR (α): Genuine users rejected.
• FMR (β): Impostors accepted.
• Changing the threshold affects the trade-off between security and
usability.
b Apply the Viola jones algorithm to explain the detection of potential face   5
locations in an image.
Marks:
List the steps: 1 marks
Discussion of each steps in in brief: 4
Viola Jones Face detection
Q2.   • Haar Features
CO-2,3,   •   Integral Image
SO-6,   • Adaboost
BL-2   • Cascading
Haar features
• Haar features are similar to the convolutional kernels which are used to detect
the presence of that feature in the given image.
• By using these kernels the black region is replaced by +1 and the white region
is replaced by -1.
• Each feature results in a single value which is calculated by subtracting the
sum of pixels under white rectangle from the sum of pixels under black
rectangle.
• No single Haar-like filter can perform the face detection task with high
accuracy.
********** 5 **********
--- page 6 ---
•   Therefore, a set of Haar-like filters of different sizes need to be applied to
each window.
• The filter responses must be combined in an appropriate way in order to detect
a face. As a result, the number of features in each detection window could be
very large.
Integral Image
In an integral image the value at the pixel (x,y) is the sum of pixels above and to the
left of (x,y)
•   Integral image allows for the calculation of sum of all pixels inside any given
rectangle using only four values at the corner of the rectangle
Adaboost
• Adaboost is a machine learning algorithm which helps in finding only the best
features among all these 160000+ features.
•   After these features are found a weighted combination of all these features is
used in evaluating and deciding any given window has a face or not.
• Each of the selected features are considered okay to be included if they can
atleast perform better than random guessing (detects more than half the cases)
• These features are also called as weak classifiers.
Adaboost constructs a strong classifier as a linear combination of these weak
classifiers.
Cascading
• The basic principle of Viola Jones is to scan the detector many times through
the same image – each time with a new size.
• Even if the image should contain one or more faces it is obvious that an
excessive large amount of the evaluated sub-windows would still be negative.
(without faces)
• So the algorithm should concentrate on discarding non-faces quickly and
concentrate more on probable face regions.
• Hence a single strong classifier formed out of linear combination of best
features is not good to evaluate on each window because of computation cost.
c   A Biometric system has been designed considering face and fingerprint   5
modalities. The accuracies obtained for the two individual modalities are
98% and 95% respectively. Using the OR decision level fusion, solve
i)   Find the combined accuracy
ii)   For 500 genuine attempts, calculate the expected number of correct
genuine matches.
iii)   Also list the various fusion techniques.
Q2.
CO-3,   Marks:
SO-2,   1.5 Marks for combined accuracy
BL-3   1.5 Mark for correct genuine matches
2 Marks List the various multi biometric system
1. Combined Accuracy
= 1- { (1-Acc 1)*(1- Acc2)}
= 1- { (1-0.95)*(1-0.98)}
= 0.999 = 99.9%
********** 6 **********
--- page 7 ---
2. Correct genuine matches
500*0.999
499.5
List of the various multi biometric system
d   If Gait biometric identification technique is applied in covert surveillance   5
system, explain its stages and examine the challenges caused by behavioral
attributes of individuals.
Marks:
3 marks: Stages in Gait Biometric Identification
2 marks : Examine the challenges
Stages in Gait Biometric Identification
1. Data Acquisition:
Capture of walking sequences using surveillance cameras from a distance.
Q2.   2. Silhouette Extraction:
CO-3,   Separation of the human body from the background to obtain the gait
pattern.
SO-4,
3. Feature Extraction:
BL-3   Extraction of gait features such as stride length, joint movement, and body
dynamics (e.g., Gait Energy Image).
4. Feature Representation:
Converting features into a structured template for comparison.
5. Matching and Recognition:
Comparing the extracted gait pattern with stored templates to identify the
individual.
Challenges due to the behavioral attributes
• Walking Speed Variation: Changes in speed alter gait patterns.
• Carrying Conditions: Bags, backpacks, or objects affect walking style.
• Clothing Variations: Loose or bulky clothes distort body shape.
********** 7 **********
--- page 8 ---
• Emotional State: Stress or fatigue changes natural gait.
• Surface and Footwear: Different terrains or shoes impact walking patterns.
Gait biometrics is suitable for covert surveillance due to its non-intrusive nature,
but its effectiveness is reduced by behavioral variations, making it less reliable
compared to physiological biometrics.
Q3.   a   Develop a biometric system applying the multi-sensor and multi algorithmic   10
CO-4,   approach for person recognition using face as the modality. Discuss the stages
SO-2,   involved, the advantages and the challenges faced in designing the same.
BL-3
Marks:
5 marks: Multi sensor approach
5 marks: Multi algorithmic approach
•   In these systems, a single biometric trait is imaged or captured using
multiple sensors in order to extract diverse information.
• For example, a system may record the two-dimensional texture content
of a person’s face using a CCD camera and the three-dimensional
surface shape (also called the depth or range image) of the face using a
range sensor in order to perform authentication (Figure).
• The introduction of a new sensor (in this case, the range sensor) to measure
the facial surface variation increases the cost of the multibiometric system.
•   However, the availability of multi-sensor data pertaining to a single trait
can not only improve the matching accuracy of the overall recognition
system, but also assist in the intermediate processing stages of the
individual component systems like image segmentation and registration.
• Another example of multi-sensor fusion is the use of both a thermal
infrared camera and a visible light camera for face recognition.
•   Spatial registration between the data obtained from the multiple
sensors is usually one of the fundamental issues in designing a multi-
sensor system.
(Spatial – image domain. Spatial registration- describes spatial relationship
between images in one or more frames. Image registration is the process that
overlays two or more images from various imaging sensors taken at different
times and angles- or to geometrically align images for analysis)
• However, this may not be always the case and there are multi-sensor
systems in which registration is either “built in” to the sensor or
registration may not be needed.
• The range sensor that acquires the 2D texture and 3D range images in
Figure is an example of the first category.
• The two captured images can be processed independently without spatially
registering them.
• However, in this scenario, the user is required to interact with the sensors
one at a time, leading to larger enrollment and verification times.
********** 8 **********
--- page 9 ---
Similarly list and discuss the use of multi algorithm for face detection.
b A low-resolution image sensors capable of scanning 250 pixels per inch can   10
be used to observe the Level 1 details of a fingerprint. Examine and justify
the statement.
Explain the level 1 singularity feature extraction technique
Marks:
4 Marks: Justification of using low resolution scanners
6 Marks: Steps in Feature extraction technique with explanation
Level 1 (Low Res) features are : Ridge flow, pattern type (Arch, Loop, Whorl),
Core, Delta
Low-resolution sensors are effective for Level 1 features:
Macro Structure Focus: Level 1 features are global patterns, not tiny details.
They are defined by the general flow of ridges across the entire finger, which acts
Q3.   as a "fingerprint map" rather than a high-detail map of specific ridge bifurcations or
CO-3,   endings.
SO-6,
BL-4   Classification & Filtering: These features are primarily used to categorize
fingerprints (e.g., whorl vs. loop) to filter databases or to align fingerprints during
identification. A low-resolution image provides enough context to rule out non-
matching patterns.
Reduced Noise Impact: High-resolution sensors often capture too much noise,
which can obscure small, fine features. Low-resolution sensors act as a natural, pre-
processing, low-pass filter that smoothing out imperfections while keeping the
prominent, overarching ridge patterns.
Contextual Feature Extraction: Algorithms often extract local orientation and
frequency as an intermediate step to enhance the fingerprint, which works
effectively even at lower resolutions
Step 1:
********** 9 **********
--- page 10 ---
Step 2: Orientation field estimation and smoothing
Step 3 Singularity extraction using Poincare’ Index method.
•   Fingerprint singularity can be extracted from the orientation field using the
well known Poincare’ index method.
•   Poincare’ index refers to the cumulative change of orientations along a
closed path in an orientation field.
• To accurately detect the location and type of singularity, Poincare’ index is
generally evaluated using the eight neighbors of a pixel.
•   Let O[i] ∈ [0,π ), i = 0, . . . , 7, denote the orientations at eight neighbors,
counterclockwise sorted starting from any neighbor, of a pixel.
Step 4: Direction of singularity
• A singular point can also be assigned a direction.
• One approach is to define the reference orientation field for a loop and a
delta, respectively.
• The orientation field around a true singular point can be approximated by a
rotated version of the reference orientation field.
• The rotation angle is defined as the direction of the singular point.
• The reference orientation fields of loop and delta, respectively, are given
by
Q4.   a A financial institution has implemented a multifactor authentication system   10
CO-   for secure online transactions. The authentication process requires the
2,3,   customer to enter a one-time password (OTP) sent to their registered mobile
SO-4,   number, followed by verification using a biometric trait such as fingerprint or
BL-4   face recognition.
The biometric system assigns a matching probability score to each transaction
to determine whether it is genuine or fraudulent. A dataset containing the
biometric scores and their corresponding ground truth labels (legitimate or
fraudulent) is provided in Table 1.
********** 10 **********
--- page 11 ---
Using the data given in Table 1, infer the following tasks:
1. Construct the Receiver Operating Characteristic (ROC) curve for the
biometric system.
2. Calculate the True Positive Rate (TPR) and False Positive Rate (FPR)
for different threshold values.
3. Interpret the ROC curve and analyze the performance of the
biometric authentication system in detecting fraudulent transactions.
Table 1. Online Financial Transaction Data
Transaction   Ground   Probability
ID   Truth   Score
1   Legitimate   0.95
2   Fraudulent   0.45
3   Fraudulent   0.15
4   Legitimate   0.82
5   Legitimate   0.74
6   Fraudulent   0.37
7   Legitimate   0.61
8   Fraudulent   0.52
9   Legitimate   0.38
10   Fraudulent   0.80
11   Legitimate   0.20
12   Legitimate   0.05
13   Legitimate   0.85
Marks:
4 Marks: Table calculations of TPR, FPR
2 Marks: ROC Graph
4 marks: Interpretation and analysis of the curve.
Trans   Proba
Ground
action   bility   TP   FP   TPR   FPR
Truth
ID   Score
1 Legitimate   0.95   1   0   0.125   0
2 Legitimate   0.85   2   0   0.25   0
3 Legitimate   0.82   3   0   0.375   0
4 Fraudulent   0.8   3   1   0.375   0.2
5 Legitimate   0.74   4   1   0.5   0.2
6 Legitimate   0.61   5   1   0.625   0.2
********** 11 **********
--- page 12 ---
7 Fraudulent   0.52   5   2   0.625   0.4
8 Fraudulent   0.45   5   3   0.625   0.6
9 Legitimate   0.38   6   3   0.75   0.6
10 Fraudulent   0.37   6   4   0.75   0.8
11 Legitimate   0.2   7   4   0.85   0.8
12 Fraudulent   0.15   7   5   0.85   1
13 Legitimate   0.05   8   5   1   1
TPR
Chart Title
1.2
1
0.8
0.6
0.4
0.2
0
0   0.2   0.4   0.6   0.8   1   1.2
FPR
The Receiver Operating Characteristic (ROC) curve represents the
performance of a classification or biometric verification system by plotting:
• X-axis: False Positive Rate (FPR)
• Y-axis: True Positive Rate (TPR)
1. System Performance
o The points on the curve move towards the top-right region,
indicating that the True Positive Rate increases as False Positive
Rate increases.
o The classifier shows moderate to good discrimination capability.
2. Comparison with Ideal System
o An ideal ROC curve would reach the top-left corner (TPR = 1,
FPR = 0).
********** 12 **********
--- page 13 ---
o The plotted points are not very close to this ideal point,
suggesting the system is not perfect but performs reasonably
well.
3. Trade-off Between Errors
o As the threshold decreases, more genuine cases are correctly
accepted (higher TPR) but more impostors may also be accepted
(higher FPR).
4. Overall Conclusion
o The ROC curve suggests the system performs better than random
classification but still has some overlap between genuine and
impostor scores.
o The optimal operating point would be the point closest to the
top-left region, balancing high TPR and low FPR
b   Apply the importance of ‘Uncertainty’ with respect to systematic errors and   10
sampling errors to explain designing test plans and reporting results for a
biometric system.
Marks:
2 Marks: Definition of Uncertainty
2 Marks: Meaning of Sampling and Systematic Errors
6 Marks: Discussion of Sampling and Systematic Errors for designing and
reporting
•   Uncertainty”, is a broader concept than “error”.
•   It is the doubt about how well a test result represents the quantity it is said
to measure. Uncertainty can exist even in the absence of error in the sense
Q4.   of “mistake”.
CO-1,3,   • A central source of uncertainty is definitional incompleteness in specifying
all of the factors influencing the measurement.
SO-5,
• What we actually measure is usually only a proxy for what we want to
BL-3   measure.
• How we control, measure and report the values in a test must reflect how we
expect those values to be used by others.
•   In other words, our testing and reporting must take into account, and state,
how we expect the results to be used.
• No matter how carefully one conducts an analysis, the error rates established
through testing will always differ from the observed error rates for the same
system in operation.
•   Uncertainty has important implications for designing test plans and
reporting results.
• The ultimate goal is for all results to be “statistically significant”,
meaning they are unlikely to be due to chance.
• There are two primary sources of errors that prevent one from knowing
“true” performance statistics:
•   systematic errors and sampling errors.
********** 13 **********
--- page 14 ---
There is little that can be done to quantify systematic errors, but the magnitude of
the sampling error can often be estimated.
• Systematic errors result from environmental factors or test procedures
that bias the result in any direction.
• An example of a systematic error for a biometric system is when the
demographics of the test subject population does not match that of the target
population (e.g. young males were over-represented because they were more
likely to respond to the advertisement for participants).
•   Ideally, test subjects should be randomly selected from the target population.
However, this is not always possible.
•   Behavioral aspects can also introduce systematic errors.
• For example, if a test subject for a covert surveillance system knows the
nature of the trial, he or she may alter their behavior (e.g. by looking for the
hidden cameras).
• In theory, systematic errors can be identified and controlled; in practice
they are inevitable.
• The difficulty lies in the fact that they are always present and bias the result
in the same direction, so they cannot be uncovered or removed by simply
running the experiment multiple times.
•   Therefore, more often that not, they remain unknown and unobserved. The
best approach for dealing with systematic errors is through careful
experiment design, and strict adherence to best practice standards.
•
• Sampling errors are a consequence of using a finite set of subjects to
represent a larger target population.
• Sampling errors are always present, even when the subjects are selected
randomly.
• unique individuals tend to perform differently within a biometric system.
• For example, some people may have trouble authenticating, while others
may be prone to being falsely accepted.
•   Therefore, the exact set of people selected to participate in a trial will have
some influence on the collective error rates.
• Unlike systematic errors, statistical theory can be used to estimate the
degree of sampling error.
However, this assumes that the trial participants have been selected randomly, and
are representative of the target population
Q5.   a Compare with necessary examples the physiological and behavioral biometrics   10
CO-1,   along with their applications. Discuss the requirements of an ideal biometric
SO-6,   system
BL-2
Marks:
5 marks: comparison with applications
5 marks: Ideal biometric system
Biometric systems can be categorized into physiological and behavioral biometrics,
depending on whether they rely on physical traits or learned behaviors for
identification.
********** 14 **********
--- page 15 ---
1. Universality
– Every person should have the biometric characteristic
2. Uniqueness
– No two persons should be the same in terms of the biometric
characteristic
3. Performance
– The biometric characteristic should be invariant over time
4. Collectability
– The biometric characteristic should be measurable with some
(practical) sensing device
5. Acceptability
– One would want to minimize the objections of the users to the
measuring/collection of the biometric
********** 15 **********
--- page 16 ---
b A university has implemented a biometric identification system to verify the   10
identity of students during examinations. The system compares a probe
biometric sample with the stored templates in the database and returns a
ranked list of possible matches.
To evaluate the performance of the system, 900 probe samples are tested. For
each probe sample, the rank position at which the correct identity appears is
recorded. The number of correct matches observed for the top 13 rank
positions is summarized in Table given.
Using the data provided in the table examine the following tasks:
1. Construct the Cumulative Match Characteristic (CMC) curve for the
biometric identification system.
2. Compute the cumulative identification rate for each rank from Rank 1
to Rank 13.
3. Interpret the CMC curve and evaluate the identification performance of
the biometric system.
Rank of Matching   Count of Genuine
Q5.   Score   Matches
CO-3,
SO-7,
1   0.95
BL-4
2   0.45
3   0.15
4   0.82
5   0.74
6   0.37
7   0.61
8   0.52
9   0.38
10   0.80
11   0.20
12   0.05
13   0.85
Marks:
4 Marks: Table calculations of Identification Rate
********** 16 **********
--- page 17 ---
2 Marks: CMC Graph
4 Marks: Analysis of the curve
Rank of Count of
Identificati
Matchin Genuine
on Rate
g Score   Matches
R1   550   0.61111
R2   174   0.804
R3   30   0.83778
R4   21   0.86111
R5   36   0.90111
R6   7   0.90889
R7   15   0.92556
R8   8   0.93444
R9   11   0.94667
R10   4   0.95111
R11   2   0.95333
R12   2   0.95556
R13   15   0.97222
The Cumulative Match Characteristic (CMC) curve represents the
performance of a biometric identification system by plotting:
• X-axis: Rank (R1, R2, R3, …)
• Y-axis: Identification Rate (probability that the correct identity appears
within the top ranks).
1. Rank-1 Performance
o At Rank 1 (R1) the identification rate is approximately 0.6
(60%).
********** 17 **********
--- page 18 ---
o This means 60% of probe samples are correctly identified as the
top match.
2. Improvement with Higher Ranks
o As the rank increases, the identification rate steadily increases.
o By Rank 2, the identification rate rises to about 80%, indicating
that the correct identity appears within the top two matches for
most samples.
3. Performance Saturation
o From Rank 5 onwards, the curve increases slowly and
approaches 0.95–0.98.
o This indicates that almost all genuine identities are found within
the top few ranks.
4. Overall System Performance
o The rapid rise at lower ranks suggests that the biometric system
performs reasonably well.
o The curve approaching 1.0 indicates high identification accuracy
when multiple ranks are considered.
Conclusion
The CMC curve shows that the biometric system has moderate Rank-1
accuracy but strong overall identification performance, since the correct
identity is found within the top few ranks for most probe samples.
Q6.   a   A Multimodal biometric system uses feature level fusion to improve its   10
CO-4,   performance.
SO-1,   a) Examine the statement.
BL-4   b) Discuss the types of feature level fusion with suitable examples.
c) Compare the advantages and limitations of the types of feature
level fusion
Marks:
2 Marks: Justification
6 Marks: Types of feature level fusion and discussion
2 Marks: Compare the advantages and limitations of both approaches
•   Feature-level fusion schemes can be categorized into two broad classes,
namely, homogeneous and heterogeneous.
• A homogeneous feature fusion scheme is used when the feature sets to be
combined are obtained by applying the same feature extraction algorithm to
multiple samples of the same biometric trait (e.g., minutia sets from two
impressions of the same finger).
• This approach is applicable to multi-sample and multi-sensor systems.
• Heterogeneous feature fusion techniques are required if the component
feature sets originate from different feature extraction algorithms or from
samples of different biometric traits (or different instances of the same trait).
e.g. As per the given image
Template update:
********** 18 **********
--- page 19 ---
• A template in the database can be updated based on the evidence presented
by the current feature set in order to reflect (possibly) permanent changes in
a person’s biometric.
• Hand geometry systems use this process to update the geometric
measurements stored in the database in order to account for changes in an
individual’s hand over a period of time.
Usually, the template is updated after every successful authentication
Template Improvement
• While template update is used to accommodate temporal changes in a
person’s biometric, the purpose of template improvement is to increase the
number of features (and decrease the number of spurious features) whilst
retaining its integrity
Heterogeneous feature fusion:
How does one consolidate feature sets originating from different algorithms and
different biometric modalities?
Feature level fusion is difficult to achieve in such cases:
1.The relationship between the feature spaces of different biometric systems may
not be known.
2. The feature sets of multiple modalities may be incompatible.
3. If the two feature sets are fixed length feature vectors, then one could consider
augmenting them to generate a new larger feature set. However, concatenating
two feature vectors might lead to the curse-of-dimensionality problem, where
increasing the number of features might actually degrade the system performance
especially in the presence of small number of training samples.
********** 19 **********
--- page 20 ---
4. Most commercial biometric systems do not provide access to the feature sets
used in their products due to proprietary reasons.
b   For a Biometric system based on Face as a biometric modality, identify and   10
discuss in brief the three main approaches to match the detected face images
and the suitable scenario where they can be applied.
Marks:
3 marks : List the approaches
6 marks : Discuss in brief (Appearance 2, Model based 2, Texture based 3)
1 mark: Scenario
Q6.
CO-2,3,
SO-6,
BL-3
Discuss in brief the basic algorithms
Appearance based approach:
Application: Passport photo verification at immigration counters
• Works well when faces are captured in controlled environments (frontal
face, good lighting).
• Compares overall facial appearance with stored images.
Model based approach:
Application: Driver monitoring systems in cars
•   Suitable for varying head poses and angles.
• Uses 3D structure of the face to track and identify the driver even when they
turn their head.
Texture based approach : in forensics for finer skin details.
Q7.   a   Explain the role of ROC and DET curves for evaluating the performance of a   10
CO-1,3,   biometric system. For the images given below, compare the performance of
********** 20 **********
--- page 21 ---
SO-2,   the two biometric systems. (you may label the curves as system as 1 and 2 for
BL-4   comparison)
Marks:
5 marks: Concept of ROC and DET curves in performance evaluation of
biometric system
5 marks: Comparison
Solution
1. Receiver Operating Characteristic (ROC) Curve
The ROC curve is used to evaluate the verification performance of a biometric
system by showing the trade-off between:
• True Positive Rate (TPR) / Genuine Acceptance Rate (GAR)
•   False Positive Rate (FPR) / False Acceptance Rate (FAR)
Role of ROC Curve:
1. Performance Visualization
o Displays how well the biometric system can distinguish between
genuine users and impostors.
2. Threshold Analysis
o Shows how changing the decision threshold affects TPR and FPR.
3. System Comparison
o Multiple biometric systems can be compared using their ROC
curves.
o A curve closer to the top-left corner indicates better performance.
4. Accuracy Evaluation
o Helps determine the optimal operating point where the system
balances security and convenience.
2. Detection Error Trade-off (DET) Curve
The DET curve is another graphical representation used to analyze biometric
system errors. It plots:
•   False Match Rate (FMR / FAR)
•   False Non-Match Rate (FNMR / FRR)
********** 21 **********
--- page 22 ---
Both axes are usually shown in logarithmic scale, making the error trade-offs easier
to observe.
Role of DET Curve:
1. Error Analysis
o Clearly shows the relationship between false acceptances and false
rejections.
2. Comparison of Biometric Systems
o Makes it easier to compare systems because curves appear
approximately linear.
3. Identification of Equal Error Rate (EER)
o The point where FAR = FRR is called the Equal Error Rate, which is
an important measure of system performance.
4. Fine-Grained Evaluation
o Particularly useful when error rates are very small.
Comparison:
Take ROC curves and compare the 2 systems, Similarly take DET curves and
compare the 2 systems.
b   Compare the two Biometric system based on the Confidence intervals shown   10
in the image given below. Discuss in brief the techniques used for Computing
the confidence interval.
Q7.
CO-3,
SO-7,
BL-3
Marks:
6 marks ; statistical inference of the two system
4 marks : list the techniques used to estimate Confidence Interval
•   Figure given contains two graphs, each containing two ROC curves with
85% confidence intervals indicated.
•   In the case of Fig.(a), the confidence intervals are narrow, implying that the
ROC curves are very reliable.
********** 22 **********
--- page 23 ---
• The intervals between the two curves do not overlap, so the claim that
“System A has higher verification rates than System B” is statistically
significant and thus unlikely be to an artifact of sampling error.
•   In contrast, in Fig.(b), the confidence intervals are relatively wide, and there
is overlap between the two curves.
• The verification rates for System A are higher than System B.
•   However, since the confidence intervals overlap, the result may be a result
of sampling error, and another test may have had a different outcome.
•   Therefore, one cannot make a statistically significant claim that System A is
better than System B without further testing.
•
Techniques to Estimate CI
•   Bootstrap Method: Resampling the biometric data to estimate the variance
of the error rate.
• Binomial Model: Assuming errors follow a binomial distribution to
calculate confidence intervals.
• Expected Performance Curve (EPC): Evaluates performance based on
thresholds determined by training sets, offering a realistic estimation
********** 23 **********
````
