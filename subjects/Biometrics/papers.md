# Biometrics: question papers in full

28 unique papers · 2010-11 to 2025-26 · Computer Engineering, AI and Data Science, Artificial Intelligence, Data Science, Information Technology

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 5 · paper 65cbb01ba30d

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_AIDS_7056/Biometrics/QP_Biometrics(702CO0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Dec 2025
- Text: text (4 pages)

````text
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
1. This question paper contains 4 pages.
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
CO–4, b   Illustrate a multimodal biometric system combining iris and face recognition for   5
SO-2,   secure building access.
BL-2
CO-3, c   Differentiate between genuine and imposter users and explain the role of ground   5
SO-6,   truth in system evaluation.
BL-2
CO-1,3, d   Compare iris and fingerprint recognition systems in terms of accuracy, speed, and   5
SO-4,   practical implementation.
BL-2,3
Section B (Attempt any four questions)
Q2.   a   A user enters a username into an online banking system, which then uses voice   5
CO-1,   recognition to confirm whether the speaker is the registered account holder.
SO-1,   Mention whether this is an identification or verification scenario with a brief
BL-4   explanation.
Q2.   b   What is the Daugman’s Rubber Sheet Model in iris recognition? Briefly explain its   5
CO-2,3,   purpose.
SO-6,
BL-2
Q2.   c   Biometric systems often encounter uncertainty during model development and   5
CO-3,   deployment. Discuss how epistemic and aleatoric uncertainty arise in such systems
SO-2,   and explain how each type influences model performance and decision-making.
BL-2   Support your answer with one example for each type.
Q2.   d   Analyze the advantages and disadvantages of using biometrics in surveillance systems   5
CO-3,   with respect to privacy concerns.
SO-4,
BL-3
Q3.   a   A leading multinational bank is implementing a multimodal biometric authentication   10
CO-4,   system at its ATM network. The system combines fingerprint and iris recognition to
SO-2,   ensure high security. During pilot testing, the bank observed that while iris recognition
BL-4
reduces false matches, fingerprint sensors fail occasionally due to wet or worn
fingerprints.
********** 1 **********
--- page 2 ---
Answer the following:
a) Construct a workflow diagram showing how feature-level and score-level fusion
will be applied in the system.
b) Recommend strategies to handle errors and inconsistencies between the two
modalities, considering practical deployment challenges.
b   The Metropolitan Security Department has introduced a facial-recognition–based   10
entry system for employees accessing a restricted data center. The system classifies
individuals as Authorized or Unauthorized based on facial matching probabilities.
The recorded data for 10 employees are given below:
Employee   Ground Truth   Probability
ID   of
Authorized
Access
1   Authorized   0.93
Q3.   2   Unauthorized   0.25
CO-3,   3   Authorized   0.87
SO-6,   4   Unauthorized   0.42
BL-4
5   Authorized   0.79
6   Unauthorized   0.33
7   Authorized   0.72
8   Unauthorized   0.15
9   Unauthorized   0.10
10   Authorized   0.90
Questions-
1. Compute the True Positives (TP), False Positives (FP), True Positive Rate (TPR),
and False Positive Rate (FPR).
2. Use the computed values to plot the ROC curve.
Q4.   a   A hospital wants to implement a biometric system to monitor staff attendance and   10
CO-2,3,   access to sensitive patient data. During trials, it was observed that some staff
SO-4,   members’ fingerprints are worn due to manual labor, and voice recognition struggles
BL-4   in noisy environments. Using this scenario, explain the limitations and advantages
of behavioral and physiological biometric traits. Recommend a possible multimodal
solution to overcome these challenges.
b   “A national bank introduces multimodal biometric authentication (fingerprint +   10
Q4.   voice) for mobile transactions. Some customers report inconsistent authentication
CO-1,3,   success rates during calls in noisy environments”. Analyze the possible technical
SO-5,
BL-3   and environmental causes of this issue and recommend strategies to enhance
reliability.
Q5.   a   The Smart University recently installed a multimodal biometric system to control   10
CO-4,   access to its research labs. The system uses fingerprint and iris recognition. During
SO-6,   testing, the following false match rates were recorded: Fingerprint FMR = 4%, Iris
BL-3   FMR = 3%.
Using OR fusion
a) Calculate the overall FMR.
b) If 500 impostor attempts are made, compute the expected number of false
acceptances.
********** 2 **********
--- page 3 ---
b   What is confidence interval?   10
Q5.   A university is using face recognition for student attendance. During exams, students
CO-3 ,   attempted to bypass the system by wearing masks, which resulted in higher false non-
SO-7 ,   match rates (FNMR). The university wants to improve system reliability and
BL-1,4
understand systematic and sampling errors in current performance evaluation. Suggest
improvements in system calibration to reduce FNMR, considering real-world
constraints like lighting and camera placement.
Q6.   a   Illustrate with examples how variations in user interaction with sensors, like   10
CO-1,   occluded iris or partial fingerprints, contribute to intra-class variations. Suggest
SO-1,   preprocessing techniques to reduce these effects.
BL-3
b   Explain the concept of fingerprint indexing and its role in accelerating fingerprint   10
identification. Discuss how minutiae points are used to generate feature vectors,
including the use of triplets (refer figure) and their geometric properties.
Q6.
CO-2,3,
SO-6,
BL-2
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
b   TechVille University has deployed a new fingerprint recognition system to automate   10
access to its laboratories. To test its accuracy, the IT team conducted a pilot study with
400 students, each providing a fingerprint sample. For each probe, the system returned
Q7.   a ranked list of candidate matches. The number of genuine matches observed at each
CO-3,   of the top 10 ranks is given below:
SO-7,
BL-4
********** 3 **********
--- page 4 ---
Rank of   Number of
Genuine   Students
Match   Matched
R1   220
R2   50
R3   40
R4   30
R5   20
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
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 20ef8574456f

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/Biometrics/QP_Biometrics(702CO0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Biometrics
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. 1.   Question No. _1_ is compulsory.
3. 2.   Out of remaining questions, attempt any 4 questions.
4. 3.   In all _5_ questions to be attempted.
5. 4.   All questions carry equal marks.
6. 5.   Answer to each new question to be started on a fresh page.
7. 6.   Figures in brackets on the right hand side indicate full marks.
8. 7.   Assume Suitable data if necessary.
Q1   Section A (Compulsory Question)   Marks
CO-2,3,   a   Identify and explain the functional components of a biometric system. Discuss   5
SO-1,   their role in ensuring reliable authentication.
BL-2
CO–4,   b   Define multimodal biometric systems. Explain how fusion of multiple modalities   5
SO-2,   improves system robustness.
BL-2
CO-3,   c   Explain the significance of performance parameters such as FAR, FRR, and   5
SO-6,   threshold in biometric systems.
BL-2
CO-1,3, d   Discuss applications of biometrics in large-scale surveillance systems. Highlight   5
SO-4,   associated benefits and concerns.
BL-2,3
Section B (Attempt any four questions)
Q2.   a A biometric system verifies a user by comparing a fingerprint with a stored   5
CO-1,   template. State whether this is identification or verification and justify your
SO-1,   answer.
BL-4
Q2.   b   Explain challenges in biometric data acquisition and how they affect system   5
CO-2,3,   performance. Give suitable examples.
SO-6,
BL-2
Q2.   c   Illustrate the biometric system design cycle and explain each stage briefly.   5
CO-3,
SO-2,
BL-2
Q2.   d Compare unimodal and multimodal biometric systems including accuracy,   5
CO-3,   flexibility, and security.
SO-4,
BL-3
Q3.   a A healthcare organization plans to deploy a multimodal biometric system using   10
CO-4,   face and iris recognition. Answer the following:
SO-2,
BL-4
1. Design a workflow illustrating feature-level and score-level fusion.
2. Suggest mechanisms to handle inconsistencies between modalities.
********** 1 **********
--- page 2 ---
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
Q4.   a   10
CO-2,3,
SO-4,
BL-4
Study the given iris processing images and answer the following:
a) Identify each stage shown in the images.
b) Explain iris segmentation and its challenges.
c) Explain how iris codes are generated and used for authentication.
b   A university plans to implement biometric attendance. Some students have worn 10
Q4.   fingerprints and inconsistent behaviour patterns. Analyze:
CO-1,3,
SO-5,   1. Limitations of physiological and behavioural biometrics
BL-3   2. Recommend a robust multimodal solution considering cost and usability
Q5.   a   Explain the concept of biometric identifiers and discuss their characteristics such   10
CO-4,   as universality, uniqueness, and permanence.
SO-6,
BL-3
Q5.   b   Explain the concept of multimodal biometric systems and discuss how fusion   10
CO-3 ,   techniques improve system reliability and security.
SO-7 ,
BL-1,4   A multimodal biometric system employs AND fusion by combining fingerprint
and iris recognition, where the fingerprint system has an accuracy of 90% and the
********** 2 **********
--- page 3 ---
iris system has an accuracy of 95%. The system processes 1000 authorized access
attempts and 1000 unauthorized access attempts. Based on this information,
calculate the combined system accuracy under AND fusion. Further, determine
the number of false rejections and false acceptances produced by the system.
Q6.   a A multimodal biometric system uses weighted fusion by combining face and   10
CO-1,   fingerprint recognition, where the face recognition system has an accuracy of 92%
SO-1,   (weight = 0.4) and the fingerprint recognition system has an accuracy of 97%
BL-3   (weight = 0.6). The system processes 1200 authorized access attempts and 800
unauthorized access attempts.
Based on the above information, answer the following:
a) Calculate the fused system accuracy.
b) Determine the number of correct matches and false rejections for authorized
users.
c) Compute the number of false acceptances for unauthorized users.
b   Describe the process of minutiae-based fingerprint matching by explaining the   10
key stages involved, namely alignment, correspondence, and match score
Q6.   generation. In your answer, discuss the role of the Hough Transform in
CO-2,3,   achieving alignment between two fingerprint images. Further, analyze how
SO-6,   spatial transformations (such as translation and rotation) and the selection of
BL-2   matching thresholds influence the accuracy and overall performance of the
fingerprint recognition system.
Q7.   a A biometric identification system is deployed in a secure facility to identify   10
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
********** 3 **********
--- page 4 ---
e) Analyze the system performance by interpreting Rank-1 accuracy and discuss
how improvements in feature extraction or matching algorithms could enhance
CMC performance.
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
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 9a6749b243d2

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/Biometrics/QP_Biometrics(702CO0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Biometrics
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. 1.   Question No. _1_ is compulsory.
3. 2.   Out of remaining questions, attempt any 4 questions.
4. 3.   In all _5_ questions to be attempted.
5. 4.   All questions carry equal marks.
6. 5.   Answer to each new question to be started on a fresh page.
7. 6.   Figures in brackets on the right hand side indicate full marks.
8. 7.   Assume Suitable data if necessary.
Q1   Section A (Compulsory Question)   Marks
CO-2,3,   a   Identify and explain the functional components of a biometric system. Discuss   5
SO-1,   their role in ensuring reliable authentication.
BL-2
CO–4,   b   Define multimodal biometric systems. Explain how fusion of multiple modalities   5
SO-2,   improves system robustness.
BL-2
CO-3,   c   Explain the significance of performance parameters such as FAR, FRR, and   5
SO-6,   threshold in biometric systems.
BL-2
CO-1,3, d   Discuss applications of biometrics in large-scale surveillance systems. Highlight   5
SO-4,   associated benefits and concerns.
BL-2,3
Section B (Attempt any four questions)
Q2.   a A biometric system verifies a user by comparing a fingerprint with a stored   5
CO-1,   template. State whether this is identification or verification and justify your
SO-1,   answer.
BL-4
Q2.   b   Explain challenges in biometric data acquisition and how they affect system   5
CO-2,3,   performance. Give suitable examples.
SO-6,
BL-2
Q2.   c   Illustrate the biometric system design cycle and explain each stage briefly.   5
CO-3,
SO-2,
BL-2
Q2.   d Compare unimodal and multimodal biometric systems including accuracy,   5
CO-3,   flexibility, and security.
SO-4,
BL-3
Q3.   a A healthcare organization plans to deploy a multimodal biometric system using   10
CO-4,   face and iris recognition. Answer the following:
SO-2,
BL-4
1. Design a workflow illustrating feature-level and score-level fusion.
2. Suggest mechanisms to handle inconsistencies between modalities.
********** 1 **********
--- page 2 ---
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
Q4.   a   10
CO-2,3,
SO-4,
BL-4
Study the given iris processing images and answer the following:
a) Identify each stage shown in the images.
b) Explain iris segmentation and its challenges.
c) Explain how iris codes are generated and used for authentication.
b   A university plans to implement biometric attendance. Some students have worn 10
Q4.   fingerprints and inconsistent behaviour patterns. Analyze:
CO-1,3,
SO-5,   1. Limitations of physiological and behavioural biometrics
BL-3   2. Recommend a robust multimodal solution considering cost and usability
Q5.   a   Explain the concept of biometric identifiers and discuss their characteristics such   10
CO-4,   as universality, uniqueness, and permanence.
SO-6,
BL-3
Q5.   b   Explain the concept of multimodal biometric systems and discuss how fusion   10
CO-3 ,   techniques improve system reliability and security.
SO-7 ,
BL-1,4   A multimodal biometric system employs AND fusion by combining fingerprint
and iris recognition, where the fingerprint system has an accuracy of 90% and the
********** 2 **********
--- page 3 ---
iris system has an accuracy of 95%. The system processes 1000 authorized access
attempts and 1000 unauthorized access attempts. Based on this information,
calculate the combined system accuracy under AND fusion. Further, determine
the number of false rejections and false acceptances produced by the system.
Q6.   a A multimodal biometric system uses weighted fusion by combining face and   10
CO-1,   fingerprint recognition, where the face recognition system has an accuracy of 92%
SO-1,   (weight = 0.4) and the fingerprint recognition system has an accuracy of 97%
BL-3   (weight = 0.6). The system processes 1200 authorized access attempts and 800
unauthorized access attempts.
Based on the above information, answer the following:
a) Calculate the fused system accuracy.
b) Determine the number of correct matches and false rejections for authorized
users.
c) Compute the number of false acceptances for unauthorized users.
b   Describe the process of minutiae-based fingerprint matching by explaining the   10
key stages involved, namely alignment, correspondence, and match score
Q6.   generation. In your answer, discuss the role of the Hough Transform in
CO-2,3,   achieving alignment between two fingerprint images. Further, analyze how
SO-6,   spatial transformations (such as translation and rotation) and the selection of
BL-2   matching thresholds influence the accuracy and overall performance of the
fingerprint recognition system.
Q7.   a A biometric identification system is deployed in a secure facility to identify   10
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
********** 3 **********
--- page 4 ---
e) Analyze the system performance by interpreting Rank-1 accuracy and discuss
how improvements in feature extraction or matching algorithms could enhance
CMC performance.
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
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 10 · paper 615d2aea9dbf

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_Computer_7032/Biometrics/QP_Biometrics(702CO0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (4 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Biometrics
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. 1.   Question No. _1_ is compulsory.
3. 2.   Out of remaining questions, attempt any 4 questions.
4. 3.   In all _5_ questions to be attempted.
5. 4.   All questions carry equal marks.
6. 5.   Answer to each new question to be started on a fresh page.
7. 6.   Figures in brackets on the right hand side indicate full marks.
8. 7.   Assume Suitable data if necessary.
Q1   Section A (Compulsory Question)   Marks
CO-2,3,   a   Identify and explain the functional components of a biometric system. Discuss   5
SO-1,   their role in ensuring reliable authentication.
BL-2
CO–4,   b   Define multimodal biometric systems. Explain how fusion of multiple modalities   5
SO-2,   improves system robustness.
BL-2
CO-3,   c   Explain the significance of performance parameters such as FAR, FRR, and   5
SO-6,   threshold in biometric systems.
BL-2
CO-1,3, d   Discuss applications of biometrics in large-scale surveillance systems. Highlight   5
SO-4,   associated benefits and concerns.
BL-2,3
Section B (Attempt any four questions)
Q2.   a A biometric system verifies a user by comparing a fingerprint with a stored   5
CO-1,   template. State whether this is identification or verification and justify your
SO-1,   answer.
BL-4
Q2.   b   Explain challenges in biometric data acquisition and how they affect system   5
CO-2,3,   performance. Give suitable examples.
SO-6,
BL-2
Q2.   c   Illustrate the biometric system design cycle and explain each stage briefly.   5
CO-3,
SO-2,
BL-2
Q2.   d Compare unimodal and multimodal biometric systems including accuracy,   5
CO-3,   flexibility, and security.
SO-4,
BL-3
Q3.   a A healthcare organization plans to deploy a multimodal biometric system using   10
CO-4,   face and iris recognition. Answer the following:
SO-2,
BL-4
1. Design a workflow illustrating feature-level and score-level fusion.
2. Suggest mechanisms to handle inconsistencies between modalities.
********** 1 **********
--- page 2 ---
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
Q4.   a   10
CO-2,3,
SO-4,
BL-4
Study the given iris processing images and answer the following:
a) Identify each stage shown in the images.
b) Explain iris segmentation and its challenges.
c) Explain how iris codes are generated and used for authentication.
b   A university plans to implement biometric attendance. Some students have worn 10
Q4.   fingerprints and inconsistent behaviour patterns. Analyze:
CO-1,3,
SO-5,   1. Limitations of physiological and behavioural biometrics
BL-3   2. Recommend a robust multimodal solution considering cost and usability
Q5.   a   Explain the concept of biometric identifiers and discuss their characteristics such   10
CO-4,   as universality, uniqueness, and permanence.
SO-6,
BL-3
Q5.   b   Explain the concept of multimodal biometric systems and discuss how fusion   10
CO-3 ,   techniques improve system reliability and security.
SO-7 ,
BL-1,4   A multimodal biometric system employs AND fusion by combining fingerprint
and iris recognition, where the fingerprint system has an accuracy of 90% and the
********** 2 **********
--- page 3 ---
iris system has an accuracy of 95%. The system processes 1000 authorized access
attempts and 1000 unauthorized access attempts. Based on this information,
calculate the combined system accuracy under AND fusion. Further, determine
the number of false rejections and false acceptances produced by the system.
Q6.   a A multimodal biometric system uses weighted fusion by combining face and   10
CO-1,   fingerprint recognition, where the face recognition system has an accuracy of 92%
SO-1,   (weight = 0.4) and the fingerprint recognition system has an accuracy of 97%
BL-3   (weight = 0.6). The system processes 1200 authorized access attempts and 800
unauthorized access attempts.
Based on the above information, answer the following:
a) Calculate the fused system accuracy.
b) Determine the number of correct matches and false rejections for authorized
users.
c) Compute the number of false acceptances for unauthorized users.
b   Describe the process of minutiae-based fingerprint matching by explaining the   10
key stages involved, namely alignment, correspondence, and match score
Q6.   generation. In your answer, discuss the role of the Hough Transform in
CO-2,3,   achieving alignment between two fingerprint images. Further, analyze how
SO-6,   spatial transformations (such as translation and rotation) and the selection of
BL-2   matching thresholds influence the accuracy and overall performance of the
fingerprint recognition system.
Q7.   a A biometric identification system is deployed in a secure facility to identify   10
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
********** 3 **********
--- page 4 ---
e) Analyze the system performance by interpreting Rank-1 accuracy and discuss
how improvements in feature extraction or matching algorithms could enhance
CMC performance.
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
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 5 · paper 399de69638f3

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_AIDS_7056/Biometrics/QP_Biometrics(702CO0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Feb 2026
- Text: text (3 pages)

````text
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
1. This question paper contains 3 pages.
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
CO–4, b   Define multimodal biometric systems and discuss their significance in high-security   5
SO-2,   areas.
BL-2
CO-3, c   Describe how biometric system performance is influenced by parameters such as FMR,   5
SO-6,   FNMR, and Threshold.
BL-2
CO-1,3, d   Explain the use of biometrics in surveillance systems for law enforcement.   5
SO-4,
BL-2,3
Section B (Attempt any four questions)
Q2.   a   A smartphone uses a stored fingerprint template to check if the person trying to unlock   5
CO-1,   the device is the authorized owner. State whether this scenario is an identification or
SO-1,   verification process. Give a brief justification.
BL-4
Q2.   b   Discuss any two challenges in iris segmentation and explain how segmentation   5
CO-2,3,   algorithms address them.
SO-6,
BL-2
Q2.   c   Illustrate the biometric system design cycle by organizing its major stages in logical   5
CO-3,   order. For each stage, briefly explain its role and importance in ensuring system
SO-2,   accuracy, usability, and security.
BL-2
Q2.   d   Compare the performance of face recognition and iris recognition systems in terms   5
CO-3,   of accuracy, cost, and deployability.
SO-4,
BL-3
Q3.   a   A hospital plans to implement a multimodal biometric system for patient identification,   10
CO-4,   combining face recognition and palm vein scanning. The hospital has experienced
SO-2,   misidentification of patients due to low-quality images from older cameras and
BL-4
variations in hand positioning. Management wants a reliable workflow that reduces
errors while maintaining patient privacy.
********** 1 **********
--- page 2 ---
Answer the following-
a) Design a detailed multimodal system workflow, showing how decision-level and
score-level fusion will handle mismatches between modalities.
b) Propose error handling techniques for situations where one modality fails or
produces low-confidence results.
b   The National Health Institute has implemented a fingerprint-based access control   10
system to ensure that only authorized doctors and nurses can enter critical care units.
The system predicts access validity based on fingerprint matching probabilities recorded
below:
Probability   of
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
Q4.   a   A school is planning to implement biometric attendance for students. Some students   10
CO-2,3,   have similar facial features, and some have difficulty maintaining a consistent typing
SO-4,   pattern on shared devices. Using this scenario, analyze the advantages and limitations
BL-4   of physiological (fingerprint, iris) and behavioral (keystroke, gait) biometric traits.
Recommend a practical and robust system design considering accuracy, cost, and user
convenience.
Q4.   b   “An organization uses face recognition for access control. During a system audit, false   10
CO-1,3,   acceptances are detected during low-light conditions”.
SO-5,   Analyze the environmental factors influencing biometric reliability and propose
BL-3   improvement strategies.
Q5.   a   City Hospital secures its high-risk wards with a multimodal biometric system using   10
CO-4,   fingerprint (FMR = 3%) and palm vein scanning (FMR = 1%).
SO-6,   Do the following based on the question given-
BL-3   a) Calculate the combined FMR using AND fusion.
b) Out of 600 unauthorized access attempts, how many are likely to be falsely
accepted?
b   What is uncertainty in the system?   10
Q5.
CO-3 ,   An airport security checkpoint uses iris recognition to verify travelers’ identities.
SO-7 ,   Recently, due to inconsistent lighting and camera alignment, the system has shown
BL-1,4
increased false non-match rates (FNMR). Security authorities need to assess the
system performance rigorously and propose improvements for operational reliability.
********** 2 **********
--- page 3 ---
Analyze systematic errors, sampling errors, and environmental factors that affect false
non match and false match rate in the airport scenario.
Q6.   a   Explain how changes in ambient conditions, such as inconsistent illumination or   10
CO-1,   background noise, influence the performance of biometric systems. Provide examples
SO-1,   for at least two modalities.
BL-3
Q6.   b   Mention at least two challenges that affect accurate face detection. Discuss the   10
CO-2,3,   following components of the Viola-Jones face detector-
SO-6,   a) Haar Features
BL-2   b) Integral Image
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
b   A corporate office implemented a facial recognition system for entry to secure areas. To   10
evaluate the system, 600 employees were tested. For each probe sample, the system
returned a ranked list of matches. The number of employees whose correct identity
appeared at each rank is as follows:
Rank   of Number of
Genuine   Employees
Match   Matched
R1   350
R2   100
R3   60
R4   40
Q7.
CO-3,   R5   25
SO-7,   R6   15
BL-4   R7   5
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
********** 3 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper 775194cf39ea

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_Computer_7002/Biometrics/QP_Biometrics(702CO0E009)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (5 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Biometrics
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 5 pages.
2. 1.   Question No. _1_ is compulsory.
3. 2.   Out of remaining questions, attempt any 4 questions.
4. 3.   In all _5_ questions to be attempted.
5. 4.   All questions carry equal marks.
6. 5.   Answer to each new question to be started on a fresh page.
7. 6.   Figures in brackets on the right hand side indicate full marks.
8. 7.   Assume Suitable data if necessary.
Q1   Section A (Compulsory Question)   Mark
s
CO-2,3,   a   Outline the techniques for IRIS Segmentation. Mention the advantages and   5
SO-1,   limitations of each. For the image given, suggest with reasons the best suited
BL-2   segmentation technique to be applied.
CO–4,   b   Explain the limitations of Unimodal Systems and suggest solutions to mitigate   5
SO-2,   them.
BL-2
CO-3,   c   Illustrate a block diagram to depict a multi biometric system which combines 5
SO-6,   fingerprint matcher score with iris matcher score. Under what circumstances are
BL-2   score level fusion optimum?
d A face recognition system processed 800 genuine attempts and 400 impostor   5
attempts. The system falsely rejected 150 genuine attempts and falsely accepted 50
impostor attempts.
CO-1,3,   Solve:
SO-4,
a) FNMR (%)
BL-2,3
b) FMR (%)
Discuss the robustness of such a biometric system.
********** 1 **********
--- page 2 ---
Section B (Attempt any four questions)
Q2.   a Make use of the graph given below which shows the verification performance of   5
CO-1,   a biometric system to discuss the outcome when the system must decide whether
SO-1,   to accept or reject the null hypothesis (H₀).
BL-3
Assume an appropriate decision threshold and explain your reasoning.
Q2.   b Apply the Viola jones algorithm to explain the detection of potential face locations   5
CO-2,3,   in an image.
SO-6,
BL-2
c A Biometric system has been designed considering face and fingerprint modalities.   5
The accuracies obtained for the two individual modalities are 98% and 95%
Q2.   respectively. Using the OR decision level fusion, solve
CO-3,   i) Find the combined accuracy?
SO-2,   ii) For 500 genuine attempts, calculate the expected number of correct genuine
BL-3   matches.
iii) Also list the various fusion techniques.
Q2.   d   If Gait biometric identification technique is applied in covert surveillance system,   5
CO-3,   explain its stages and examine the challenges caused by behavioral attributes of
SO-4,   individuals.
BL-3
Q3.   a   Develop a biometric system applying the multi-sensor and multi algorithmic   10
CO-4,   approach for person recognition using face as the modality. Discuss the stages
SO-2,   involved, the advantages and the challenges faced in designing the same.
BL-3
b A low-resolution image sensors capable of scanning 250 pixels per inch can be   10
Q3.   used to observe the Level 1 details of a fingerprint. Examine and justify the
CO-3,
statement.
SO-6,
BL-4   Explain the level 1 singularity feature extraction technique.
Q4.   a A financial institution has implemented a multifactor authentication system for   10
CO-2,3,   secure online transactions. The authentication process requires the customer to
SO-4,   enter a one-time password (OTP) sent to their registered mobile number, followed
BL-4
by verification using a biometric trait such as fingerprint or face recognition.
********** 2 **********
--- page 3 ---
The biometric system assigns a matching probability score to each transaction to
determine whether it is genuine or fraudulent. A dataset containing the biometric
scores and their corresponding ground truth labels (legitimate or fraudulent) is
provided in Table 1.
Using the data given in Table 1, infer the following tasks:
Construct the Receiver Operating Characteristic (ROC) curve for the biometric
system.
Calculate the True Positive Rate (TPR) and False Positive Rate (FPR) for different
threshold values.
Interpret the ROC curve and analyze the performance of the biometric
authentication system in detecting fraudulent transactions.
Table 1. Online Financial Transaction Data
Transaction   Ground Truth Probability
ID   Score
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
Q4.   b Apply the importance of ‘Uncertainty’ with respect to systematic errors and   10
CO-1,3,   sampling errors to explain designing test plans and reporting results for a biometric
SO-5,   system.
BL-3
Q5.   a Compare with necessary examples the physiological and behavioral biometrics 10
CO-1,   along with their applications. Discuss the requirements of an ideal biometric
SO-6,   system.
BL-2
b A university has implemented a biometric identification system to verify the   10
identity of students during examinations. The system compares a probe biometric
sample with the stored templates in the database and returns a ranked list of
possible matches.
Q5.   To evaluate the performance of the system, 900 probe samples are tested. For each
CO-3 ,
probe sample, the rank position at which the correct identity appears is recorded.
SO-7 ,
BL-1,4   The number of correct matches observed for the top 13 rank positions is
summarized in Table given.
Using the data provided in the table examine the following tasks:
a) Construct the Cumulative Match Characteristic (CMC) curve for the biometric
identification system.
********** 3 **********
--- page 4 ---
b) Compute the cumulative identification rate for each rank from Rank 1 to Rank
13.
c) Interpret the CMC curve and evaluate the identification performance of the
biometric system.
Rank of Matching   Count of Genuine
Score   Matches
1   0.95
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
Q6.   a A Multimodal biometric system uses feature level fusion to improve its   10
CO-4,   performance.
SO-1,   Examine the statement.
BL-4
Discuss the types of feature level fusion with suitable examples.
Compare the advantages and limitations of the types of feature level fusion.
Q6.   b   For a Biometric system based on Face as a biometric modality, identify and discuss   10
CO-2,3,   in brief the three main approaches to match the detected face images and the
SO-6,   suitable scenario where they can be applied.
BL-3
Q7.   a   Explain the role of ROC and DET curves for evaluating the performance of a   10
CO-1,3,   biometric system. For the images given below, compare the performance of the two
SO-2,   biometric systems. (you may label the curves as system as 1 and 2 for comparison)
BL-4
********** 4 **********
--- page 5 ---
b Compare the two Biometric system based on the Confidence intervals shown in the   10
image given below. Discuss in brief the techniques used for Computing the
confidence interval.
Q7.
CO-3,
SO-7,
BL-3
********** 5 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper 6ff66f0a544a

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, B.TECH INTEGRATED / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/VI SEMESTER/BIOMETRICS/Biometrics Batch 2025-26 Re Exam.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; exam date: 03 Jul 2026
- Text: ocr (5 pages), mean OCR confidence 86.7

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Subject: Biometrics :
Date: 03 Jul 2026 Titres 10: pieress 00; (03: 00 Hrs.)
Max. Marks: 100 &

RE EXAMINATION (Acad. Year:2%¥

Instructions:
1. This question paper contains 5 pages.
2. 1. Question No. _1_ is compulsory.
3. 2. Out of remaining questions, attempt any 4 questions.
4, 3. In all_S_ questions to be attempted.
5. 4. All questions carry equal marks.
6. 5. Answer to each new question to be started on a fresh page.
7, &. Figures in brackets on the right hand side indicate full marks.
8. 7. Assume Suitable data if necessary.
Ql Section A (Compulsory Question) Mark
s
CO-2,3, | a | Outline the techniques for IRIS Segmentation. Mention the advantages and | 5
SO-1, limitations of each. For the image given, suggest with reasons the best suited
BL-2

segmentation technique to be applied.

| CO-4, | b | Explain the limitations of Unimodal Systems and suggest solutions to mitigate | 5
SO-2, them. ,

BL-2 ”
CO-3, | ¢ | Illustrate a block diagram to depict a multi biometric system which combines} 5
SO-6, fingerprint matcher score with iris matcher score. Under what circumstances are
BL-2 score level fusion optimum?
d | A-face recognition system processed 800 genuine attempts and 400 impostor | 5
attempts. The system falsely rejected 150 genuine attempts and falsely accepted 50
impostor attempts.
a Solve: *
-4, 5
BL23 a) FNMR (%)

b) FMR (%)
“Discuss the robustness of such a biometric system.

FOR) OR RR ak
--- page 2 ---
Section B (Attempt any four questions)

Q2. a | Make use of the graph given below which shows, the verification performance of 5
CO-1, a biometric system to discuss the outcome when the system must decide whether J
SO- i, to accept or reject the null hypothesis (Ho). F
BLS Assume an appropriate decision threshold and explain your reasoning.
4 H, (Impostor)
1\
1 o\
14
I \ Match
Threshold
I \
I { H, (Genuine)
| \
! \ k
1a (FNMR) 8 (FMR) ~
a —
Test statistic (match score) |
Q2. b | Apply the Viola jones algorithm to explain’the detection of potential face locations | 5 |
ae in an image. ;
BL-2
¢ | A Biometric system has been designed considering face and fingerprint modalities. | 5
The accuracies obtained for the two individual modalities are 98% and 95%
Q2. respectively. Using the OR decision level fusion, solve
CO-3, i) Find the combined accuracy?
SO-2, li) For 500 genuine attempts, calculate the expected number of correct genuine
BL-3 matches.
iii) Also list the various fusion techniques.
Q2. d | If Gait biometric identification technique is applied in covert surveillance system, | 5
CO-3, explain its stages and examine the challenges caused by behavioral attributes of
SO-4, individuals. es
BL-3
Q3. a | Develop a biometric system applying the multi-sensor and multi algorithmic | 10
CO-4, approach for person recognition using face as the modality. Discuss the stages
a involved, the advantages and the challenges faced in designing the same.
b | A low-resolution image sensors capable of scanning 250 pixels per inch can be | 10
Q3. used to observe the Level | details of a fingerprint. Examine and justify the =
So : statement.
BL-4 Explain the level 1 singularity feature extraction technique.
Q4. a | A financial institution has implemented a multifactor authentication system for | 10
CO-2,3, secure online transactions. The authentication process requires the customer to
i ,, enter a one-time password (OTP) sent to their registered mobile number, followed

“by verification using a biometric trait such as fingerprint or face recognition.

FOI IGG 9 OR Gr
--- page 3 ---
The biometric system assigns a matching probability score to each transaction to
determine whether it is genuine or fraudulent. A dataset containing the biometric
scores and their corresponding ground truth labels (legitimate or fraudulent) iS
provided in Table 1.

_ Using the data given in Table 1, infer the following tasks:

Construct the Receiver Operating Characteristic (ROC) curve for the biometric
system.
Calculate the True Positive Rate (TPR) and False Positive Rate (FPR) for different
threshold values.
Interpret the ROC curve and analyze the performance of the biometric
authentication system in detecting fraudulent transactions.
Table 1. Online Financial Transaction Data
Transaction Ground Truth | Probability

ID Score
1 Legitimate 0.95
2 Fraudulent 0.45
3 Fraudulent 0.15
4 Legitimate 0.82
5 . Legitimate 0.74
6 Fraudulent 0.37
7 Legitimate 0.61 °
8 Fraudulent 0.52
9 Legitimate 0.38
10 Fraudulent 0.80
at Legitimate 0.20
12 Legitimate 0.05
13 Legitimate 0.85
Q4. Apply the importance of ‘Uncertainty’ with respect to systematic errors and | 10
CO-1,3, sampling errors to explain designing test plans and reporting results for a biometric
SO-5, system.
BL-3
Q5. Compare with necessary examples the physiological and behavioral biometrics | 10
CO-1, along with their applications. Discuss the requirements of an ideal biometric
SO-6, system.
BL-2
A university has implemented a biometric identification system to verify the | 10
identity of students during examinations. The system compares a probe biometric
sample with the stored templates in the database and returns a ranked list of
possible matches.
QS. To evaluate the performance of the system, 900 probe samples are tested. For each
CO-3 , is . . . .
50-7 probe sample, the rank position at which the correct identity appears is recorded.
BL-1,4 The number of correct matches observed for the top 13 rank positions is

summarized in Table given.

Using the data provided in the table examine the following tasks:

i) Construct the Cumulative Match Characteristic (CMC) curve for the biometric
identification system.

FG Gc ake
--- page 4 ---
b) Compute the cumulative identification rate for each rank from Rank | to: Rank <a
13.
c) Interpret the CMC curve and evaluate the identification performance of the

biometric system. ° e
Rank of Matching Count of Genuine
Score Matches
1 0.95
2 0.45
3 0.15
4 0.82
5 0.74
6 0.37 '
7 0.61
8 0.52 2)
9 0.38 i
10 é 0.80 :
11 0.20
12 0.05
13 : 0.85
Q6. a | A Multimodal biometric system uses feature level fusion to improve its | 10
CO-4, performance.
a Examine the statement.
Discuss the types of feature level fusion with suitable examples.
Compare the advantages and limitations of the types of feature level fusion.
Q6. b | Fora Biometric system based on Face as a biometric modality, identify and discuss | 10
CO-2,3, in brief the three main approaches to match the detected face images and the
a suitable scenario where they can be applied. ‘ a)
Q7. a | Explain the role of ROC and DET curves for evaluating the performance of a | 10
CO-1,3, biometric system. For the images given below, compare the performance of the two
an biometric.systems. (you may label the curves as system as | and 2 for comparison)

FOI ICR AOR AiG kok
--- page 5 ---
a

q

Detection Error Tradeoff (DET) curves

Receiver Operating Characteristic (ROC) curves
—— Linear SVM =

99% Random Forest

2 80%
é
=
& 50% 4
3
e
e
2
= 20%
&
2
& 5%
&
le | ——— Linear SVM (AUC = 0.96)
ood! - Random Forest (AUC = 0.99}
1% 5% 20% 50%   B0% 95% 99% 0.90 02 0.4 0.6 08 10

False Positive Rate (Positive label: 1) False Positive Rate (Positive label: 1)

Q7.

CO-3,
SO-7,
BL-3

b | Compare the two Biometric system based on the Confidence intervals shown in the

image given below. Discuss in brief the techniques used for Computing the
confidence interval.

ROC Curve

ROC Curve
eS: _. 100, T
I =
95
= 90
a5
; —— a
1.0 10.0 20 Lee Sytem
False match rate “0.10 1.00 10.00 100.00
. ' Fal rat
(a) Non-oveslapping confidence intervals. abemanchrats

{b) Overlapping confidence intervals.

10

FORO ack AR kk
````

## 2024-25 · Final + Re-Exam · Sem 6 · paper 489092d5fb38

- Departments: Artificial Intelligence, Computer Engineering, Data Science
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / COMPUTER, B TECH / CSE Data Science (311), MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-VI/BIOMETRICS/Biometrics, Sem VI, Final Year 2024-25 & Re Exam 2022-23.pdf` (+3 identical copies)
- Printed on paper: max marks: 100
- Text: ocr (6 pages), mean OCR confidence 71.3

````text
SVKM’S:NMIMS
MUKESH PATEL. SCHOOL. OF TECHNOLOGY. MANAGEMENTE& ENGINEERING
Academie Year:.2024-2025

Program/s: BTech /MBA Tech Year; 3rd Semester: VI
Stream/s ; Computers/¢ce= DS [AT .
Subject: Biometrics 5 Time; 3:hrs (2-00pmt0 5% 00 pro)
Date: _06'/.05 /2025 : No. of Pages:'5

Marks: 100 .

Final al aamuination/Re« -Eanmy 2022.+.23

Instructions: Candidates should:read carefully the instructions printed:on. the-question paper.and‘on-the.cover
of the:-Atiswer Book, which is provided for their use:

4) Question'No._1___is compulsory.

2) Out of remaining questions; aitempt'any’::, 4... questions;

3) In-all.:_$--questions to’be attempted.

4)All-questions:carry equal marks;

3) Answer to.each new. question: to: be started on.a.fresh'page.

6): Figures in: brackets .on'the right-hand side indicate full marks.
7) Assume Suitable-data:if necessary.

Qi ‘ :
Answer briefly: 20]

0-2; 4)
5 ea Compare‘and contrast the integro-differential operator and Geodesic: ‘Active 15]
BL2 Contours: for iris ségméntation.
CO-4: b):| List the-various fusion techniques and: discuss:Scenarios where cach will be
$06; suitable. 5]
BL-1
co}: ¢).) What'do-'you ‘meéan*by :nulland ‘alternate ‘hypothesis’ in’ a Verification
SO-1: problem? ‘Discuss with’ a:diagram:how ‘the null hypothesis: can be accepted {5
BL-1/4 ‘or rejected baséd ca the decision threshold for mateh' score:

d):| Identify’ the’-singularity points highlighted “by. the: rectangles. in_ the.
CO: fingerprint image given in the following figure: What level of featurés do
S021; these-singularity: points indicate? “List the. name -6f the primary” pattern.) [5]
BL-3 provided in the:image.
--- page 2 ---
Q2 Evaluate the effectiveness of biometric authentication versus traditional

CO-t: a) | password-based security systems. Which method is moré reliable in {10}
SO-1; cybersecurity? Justify your answer.

BL-5

Q2

CO-2: b) List and discuss the various approaches to face feature extraction and [10]
SO-1; matching techniques.

BL-1/6

Q3 Categorize the different types: of multi biometric. system: giving ‘suitable
CO-4; a) | examples for each type. List the advantages of a multi biometric:systems over | [19]
SO-1; unibiometric systems.

BL: 4

A hospital-has deployeda biometric-enabled mobile application for resident

b) medical officers to track patiénts' health records. The. resident medical
officer can access the mobile application after a presented biometrics sampie

4 is -suecessfully. validated. The deployed biometric system will heip doctors
classify the patients' health-records.as genuine or imposter. The biometric
system has assigned a probability score every time the application validates

the resident medica! operator's query, as given in Table 1. Evaluate the
system's performance by plotting the Receiver Operating Characteristics

Q3 (ROC). curve.
CO-3; [£0]
SLs. Table i Mobile Application Access Data
Resident Medical Ground Probability
Officcer's ID Trath Score
1 Genuine 0.99
2 Imposter 0.37

3 Genuine 0.91
--- page 3 ---
4 Genuine 0:87

5 Genuine 0.78
6 Imposter 0.61
7 Iniposter 0.78
8 Imposter ~ 0.55
9 Genuine 0:83
10 Genuine 0.60
isl ~ {~ Jmposter 0:21
12 Tinposter: 0.23
13 | -Genuine 0.95
14 Genuine 0.73
15 Genuine 0:39

Q4 . : ,

co.2: ; Explain the implementation. of Viola jones:algorithm fora Face recognition .
sous 4) | system. “410
BL-2

Q4 A biometric. system: niatches ‘fingerprints using: minutiae :points extracted |
CO-1.3- b) from: fingerprints. Explain. why: the alignment process.is required before:
$0-1 i performing matching. Discuss how the alignment can be done using minutiae: | [01
BL-2- descriptors.

Qs - Ilustrate.a neat diagram to:show score level fusion‘in a: multi biometric

CO-4; a) | system. Discuss thé challenges arising-in Score-level fusion when the match | [10]
SO-1; scores generated by the individual matchers arc not homogénedtis,

Q5 Examine the causes of sampling.and systematic errors in the biometric

CO-3; b) | recognition systems. Suggest ways to minimize such-errors. [10]
SO-1,6;

BL-2

Q6 Discuss: various stages:of identifying.a.person.based on face:biometri¢s in'a
C0-1,3: a). | covert. surveillance: system. Explain challenges related. to\'the -person!s [20]
80-1; behavioural attributes: for. such a:covert surveillance system,

BL-]
--- page 4 ---
The biometric system described in Q.3.(b) has also added the facility to enrol
b) | new resident medical officers during joining. The system was thus tested for

rank accuracies using 750 probe. samples owt of 1500 gallery samples to

determine the system's ability to identify enrolled resident medical officers.

The rank histogram is given in Table 2.

Construct.a Cumulative Match-Characteristics (CMC) curve to visualize the

rank accuracies of the biometric system.

Table 2'Rank Histogram
Rank of Matching Score | Count of Genuine Matches

R1 313

R2 102
06 R3 60
SOL. 6: R4 21 {10}
BL2 RS 28

R6 5

R7 2

R8 i

RO 4

R10 2

Ril 1

Ri2 1

R13 : 0

Ri4 0

Ris 0
Qi [5]
CO#1;, a) Compare. physiological and. behavioral biometrics with two examples of
SO-1: each,

BL-2
--- page 5 ---
Q7 How. does:gait-as:a biometric.trait.compare'to.other biometric. modalities in

CO-2; b) | terms of. accuracy, uniqueness, and'vulnerability to spoofing? What-are the 13]
SO-2). key features .extracted:from gait-analysis for: biometric identification?

BL-4.

Q7

Explain the concept of the Rank.X. identification graph. Describe the effect.| [5]

Soi €) | of increasing the number ofenrollments on Rank X-accursey.
BL-2
‘7
@ Discuss: the neéd to-normalize the non-uniform iris‘atea‘and explain [5]
ih 33 d) Daugman's rubber shect model.

BL-2
--- page 6 ---

````

## 2023-24 · Final-Exam · Sem 5 · paper d1db1962ea94

- Departments: Artificial Intelligence, Data Science
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / DATA SCIENCE
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-V/BIOMETRICS/Biometrics, Sem-V, A Y 2023-24, Final Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 25 / 14/2023
- Text: ocr (3 pages), mean OCR confidence 91.5

````text
_ SVKM'S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT&
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINE
Academic Year: 2023-2024
Program: B. Tech Year: 3" Semester:

Stream: Artificial Intelligence and Data Science

Subject: Biometrics Time: 3 hrs (2:00pmto 5% 00pw)
Date: 25 / 14/2023 . No. of Pages: 03
Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed o on the question paper and on the
cover of the Answer Book, which is provided for their use.

1) Question No. TI is compulsory.

2) Out of the remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.

7) Assume Suitable data if necessary.

8) Draw the ROC and CMC curves in the answer sheet in Questions 4 (b) and 6 (b).

Ql Answer briefly: [20]

CO-1; SO-1; | a. | Explain the weaknesses of the voice biometric that make it unsuitable for [5]
BL-1
network security applications.

CO-1,3;SO- | b. | What is meant by Gait recognition? Provide various challenges in | [5]
1,3; BL-2 a :
recognizing the gait of a person.

CO-4; SO-4; | c. | Illustrate with an example how a multimodal biometrics recognition system | [5]
rs

BL-2

improves identification significantly.
CO-2,3;SO- | d. | Define the following terms relating to the biometric recognition system. [5]
2,3; BL-1

i) Genuine and Imposter Matches ii) True Rejection Rate (TRR) iii) False
Acceptance Rate (FAR)

Q2| a. | Draw a generalized block diagram of the biometric system and briefly | [10]
CO-1; SO-1; discuss each block. Use the generalized block diagram of the biometric
BL-2 < F : .
system and explain the data flow for the verification and identification

problems.

Page 1 of 3
--- page 2 ---
Q2 | b. | What is meant by verification in a biometric recognition system? Using | [10]

CO-3; SO-3; suitable plots, explain Type J and Type 2 errors in null hypothésis testing

BL-1 ,
relating to verification tasks in a biometric system.

Q3 | a. | Explain various types of biometric data. [10]
CO-1; SO-1;
BL-1

Q3 | b. | Define eye biometrics. Compare and contrast between the retina and iris. | [10]
CO-3; SO-3; Discuss the challenges in acquiring the retina.
BL-3

Q4| a. | Classify techniques to fuse multiple biometric information and briefly | [10]

CO-4; SO-4; explain any two of them.
BL-1

Q4/| b. | The Institute of National Repute has developed a biometric system for | [10]
CO-1,3; SO-

scientists to enter the laboratory using a combination of fingerprint and iris.
1,3; BL-3

The biometric system will help the Institute to validate the legitimate user
for laboratory entry. The probability of correct prediction for each scientist
is provided in the following table. Draw a Receiver Operating

Characteristics (ROC) curve for the biometrics system thus defined.

Scientist's Class of the Scientist Probability of
Employment ID Correct Prediction
1 dummy 0.78
2 legitimate 0.95 *
3 legitimate 0.65
‘4 dummy 0.23
5 dummy 0.56
6 legitimate 0.99
7 dummy 0.33
8 legitimate 0.88
9 legitimate 0.43
10 dummy 0.10

Q5 | a. | What is meant by the minutiae points ofa fingerprint? Explain the technique | [10]
CO-2,3; SO- to recognize individuals based on their fingerprints’ minutiae patterns.
2,3; BL-2

_

Page 2 of 3
--- page 3 ---
QS | b. | Illustrate how errors in the test datasets can be minimized before and after | [10]

CO-4; SO-4; data collection. 7
BL-3 oe

Q6 | a. | Explain Daugman's Rubber Sheet model for normalizing iris images. [10]
CO-2,3; SO-
2,3; BL-1

Q6 | b. | The Institute of National Repute wishes to identify legitimate scientists for [10]
CO-1,3; SO- the biometric system explained in Q.4 (b). Thus, the biometric system is
1,3; BL-3

tested by presenting 700 probe samples. The number of genuine matches
out of 700 probe samples is noted for each of the top 10 rank metrics. The
resulting genuine rank histogram is given in Table 2 below. Plot the
Cumulative match Characteristics (CMC) curve for the biometric system.
Table 2 ;
Rank of the Rank Count of

Genuine Match | Genuine Matches

RI 423

R2 123

R3 51

R4 33

RS 20

R6 23

R7 11

R8 7 .
R9 5
R10 2

Q7| a. | Summarize any five characteristics of the iris biometrics that make it a [10]
CO-1; SO-1;

suitable choice for network security applications.
BL-1

Q7| b. | Explain template adaptation in the context of the biometric system's | [5]
CO-4; SO-4;

performance testing.
BL-2

Q7| c. | Explain what statistical uncertainty is in the biometric system. Discuss [5]
CO-1,3; SO- sampling errors that affect the statistical performance of the biometric
1,3; BL-1

systems,

Page 3 of 3
````

## 2023-24 · Re-Exam · Sem 6 · paper 600604d261b7

- Departments: Artificial Intelligence, Computer Engineering
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-VI/BIOMETRICS/Biometrics, Sem-VI, Fianal & Re Exam 2022-23.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 / 04/2024
- Text: ocr (4 pages), mean OCR confidence 93.1

````text
Comp )
SVKM'S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & EN it
SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERI
Academic Year: 2023-2024
Program: MBA Tech/ B. Tech Year: 3% Semester: 6m

Stream: Computer Engineering/ Artificial Intelligence | Computer

Subject: Biometrics Time: 3 hrs (2:00prn to 5:00pm )

Date: 24 / 04/2024 Ke ; No. of Pages: 04
Marks: 100
Final Examination / Re-Examination (2022-23)

Instructions: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use. .

1) Question No. 1 is compulsory.

2) Out of the remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right-hand side indicate full marks.
7) Assume Suitable data if necessary.

8) Use of a scientific calculator is allowed in the examination.

a.

Ql Answer briefly: [20]
CO-1,3; a. | Consider the person's fingerprint in Fig. 1 and [5]
SO-1,3; answer the following questions.

BL-2 1. Provide the type of fingerprint pattern.
2. Identify the singularity points highlighted

using rectangles. What is the level of features

> thus highlighted?
3. Discuss the information available in these
features.
CO-2,3; b. | Write the strengths and weaknesses of the retina recognition technique. [5]
SO-2,3;
BL-1
CO-3,4; c. | Define multimodal systems and explain their advantages over unimodal | [5]
SO-3,4; systems.
BL-1

Page 1 of 4
--- page 2 ---
CO-2; SO- d. | What do you mean by verification in a biometric recognition system? | [5]
2; BL-2 Formulate null and alternate hypothesis testing for verifying iris templates

based on the matching score between reference and query samples:*

Q2 | a. | The instructor wishes to develop an application for marking student's | [10]
CO-1;SO- ~ attendance using biometric features. Explain the general biometric

1; BL-1 attributes that you desire in the system. fe]

Q2| b. | The district cooperative bank wishes to provide a locker facility to the | [10]
CO-2;,SO- customers. The customers can operate the locker by giving voice commands
2; BL-3 and a fingerprint sample. The probability of correctly validating a genuine
query on a particular day by the biometric recognition algorithm employed
in the banking system is shown in the following Table 1. Plot the Receiver

Operating ‘Characteristics (ROC) curve using the given data to check the

algorithm performance.
Table 1
Customer ID Type of the Query Probability of
Correct Prediction
1 Genuine 0.73
2 Imposter . 0.95
3 Imposter 0.37
‘4 Genuine 0.97
5 Genuine 0.71
6 Imposter 0.41
7 Genuine 0.65
8 Imposter ; 0.29
9 Imposter 0.12
10 Genuine 0.84
Q3 | a. | Explain the process of fingerprint recognition using minutiae points. [10]
CO-1,3;
SO-1,3;
BL-2

Q3 | b. | A research institute is investigating the feasibility of using gait recognition | [10]

for human identification in video surveillance. Discuss the pros and cons of

Page 2 of 4
--- page 3 ---
CO-2,3; gait recognition compared to traditional biometric methods. How can the

SO-2,3; system overcome its limitations?
BL-2 z

Q4 | a. | Why is performance testing necessary forthe biometric recognition system? | [10]
CO-3,4; Illustrate the testing process with a block diagram and discuss each step
SO-3,4; briefly. :
BL-1

Q4| b. | Discuss systematic errors and sampling errors that affect the statistical | [10]
CO-2; SO- performance of the biometric systems.
2; BL-2

Q5 | a. | Analyze and describe the challenges associated with face recognition. [10]
CO-2,3;
SO-2,3;
BL-2

Q5 | b. | Compare and contrast feature, level fusion, score level fusion, and decision | [10]
CO-3,4; level fusion in multimodal biometric systems. Highlight the pros and cons
SO-3,4; of each technique.
BL-2

Q6 | a. | Explain Daugman's algorithm for recognizing the iris of a person. [10]
CO-2,3;
SO-2,3;
BL-1

Q6| b. | The district cooperative bank wishes to identify imposter customers while | [10]
CO-2; SO- operating the locker system, as explained in Q.2 (b). Thus, the biometric
2; BL-3 system is tested by presenting 1000 probe samples by registered customers.

The number of genuine matches out of 1000 probe samples is noted for each
of the top 10 rank metrics. The resulting genuine rank histogram is given in
Table 2. Plot the Cumulative match Characteristics (CMC) curve for the

biometric system.

Page 3 of 4
--- page 4 ---
Table 2 :
Rank of the Rank Count of j

Genuine Match | Genuine Matches ¥
Rl 489 7
R2 178
R3 ~ 134
R4 42
RS 9
R6 16
R7 3
R8 4
R9 19
R10 5
Q7 Suggest a technique to identify a suspect using biometric traits in | [10]
CO- surveillance video. Draw a block diagram of the proposed method and
1,3;SO-1,3; explain each block briefly. Discuss probable challenges in the proposed
BL-3 system.
Q7 Classify the types of biometric data and briefly explain them. [5]
CO-1;SO-
1; BL-1
Q7 Using an appropriate graph, explain the score histogram in the biometric | [5]
CO-2; SO- system verification problem. Illustrate how decision errors are determined
2; BL-2 using score histograms.

Page 4 of 4
````

## 2022-23 · Final-Exam · Sem 6 · paper d91ffab33443

- Departments: Artificial Intelligence, Computer Engineering
- Programmes: B TECH / ARTIFICAL INTELLIGENCE, B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/ARTIFICAL INTELLIGENCE/SEM-VI/BIOMETRICS/Biometrics, Sem-VI, Year 2022-23, Final Exam.pdf` (+2 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (5 pages), mean OCR confidence 85.8
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’S NMIMS

Academic Year: 2022-2023

Program/s: BTech /MBA Tech Year: 3rd Semester: VI
Stream/s ; Computers, AI

Subject: Biometrics Time: 3 hrs @:00 pm to 5:00 pm)
Date:_28 /04 / 2023 No. of Pages: 5

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

a> 3)Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql
Answer briefly: (20]

a)

CO-2; SO-1;
BL-2

[5]

Answer the following questions, considering the fingerprint of a person shown in
the figure.

1. Identify the type of singularity point highlighted by the rectangle.

2. Based on the other singularity points and their orientations observed on
the fingerprint, identify the fingerprint class into which the fingerprint can
be classified into.

3. Briefly outline the process of extracting these singularity points.
--- page 2 ---
b) | Justify why Feature-level fusion is challenging giving examples. Suggest
CO-2; SO-6;
BL techniques used to fuse features at feature level.

c) | The following graphs (a) and (b) contain ROC curves. Interpret the graphs with
respect to confidence intervals and justify which system is statistically more
significant than the other.

ROC Curve
Eee
—— System A
CO-1; $O-6; 1 ot come eae ame [5]
BL-5S
(a)
ROC Curve
an | io
80x To 1.00 10.00 100.60
False match rate
(b)

d) | Classify the different types of users of a biometric based system based on their
CO-3; SO-6; : ‘ . 5
BL-5 inherent differences as defined by Doddington. [5]
Q2 For a video surveillance system based on biometrics, choose the best combination

of traits which can be used. Justify your choice and depict a system diagram for | 519
co-3; so-1; | 2) [10]
; ; the same.

BL-2
Q2 The task is to build a biometric based application for employee attendance using | [10]
CO-3; $0-1; | 6) | a single trait. On checking the employee demographics, it is inferred that the age
--- page 3 ---
*

BL-2

group varies from 18 to 75, there are elder people in the organization and also
many twins. Considering this scenario, answer the following:

1. Suggest and justify a suitable biometric trait to be used for the
organization.

2. Choose a sensor for acquiring the data.

3. Identify the features which can be used to uniquely identify the
employees. .

4. Discuss briefly the steps used to extract the selected features.

5. List if there are any limitations of this trait or approach you have used.

Q3 There are various choices available for designing a multibiometric system based
CO-4; SO-1; a) | on type of information, acquisition and processing architecture. Categorize the [10]
BL- 6 different types giving suitable examples for each type.
Q3 . ae . . .
; |b) Explain Uncertainty in Biometric System. Discuss non-parametric method for | [10]
ae 80-1; estimating statistical uncertainty using necessary plots.
Consider that the face recognition algorithm uses SIFT for feature extraction. The
a) algorithm is being trained using sample images from the Flickr dataset where
images are of resolution 1024x1024.
Q4 A. Calculate the following based on the SIFT algorithm:
C62: $038 1. The dimension and the number of blur images for all the four | [10]
BL-3 ; octaves.
2. The number of DoG (difference of Gaussian) images created per
octave.
B. Illustrate the process of determining the local minima and maxima.
C. Show how low contrast key points can be removed.
Q4 A biometric attendance system based on iris recognition system is to be designed.
C0-3: $0.6: | 6) Develop a system and explain in brief the four typical modules that need to be [10]
BLS. ; implemented.
a) With reference to multibiometric systems, answer the following:
Q5
0-4. $0.4: 1. Types of Score level fusion techniques [10]
BL-6 ; 2. Compare unimodal and multibiometric systems.
The result of person verification system is given in the graph below. Interpret the
Q5 b) graph and discuss the result if the goal of the verification system to use the
CO1SO6: information available to either accept or reject HO. (make necessary assumption [10]
BL-5 , for threshold value).

Also
1. Ifthe threshold shifts to the right, explain its impact on FNMR and FMR
--- page 4 ---
2. Given a match score s and a match threshold t, give the verification
decision to accept and reject Ho.

4 H, (Impostor)
1\
YA
1 oN
1 1 Match
Threshold
! \
I \ H, (Genuine)
! \
! \
fa (FNMR)}I>

ll

Test statistic (match score) .

A finger print matching algorithm is implemented as given in the diagram below.
Discuss the need for alignment operation and explain the implementation of the
algorithm using minutiae descriptors.

Query minutiae

o ¥
e eh 8
ca a 2 g
P id F °
¢ « a
Q6 Se tg Sosy Ss tidy
Pe oe ats ag” ha 10
CO-2; SO-6; e © Se vegas ae [10]
e me ® te
BL-6 az & or
e > [+> score
2 e 6 we é
r 9 OF ae? 4
4 & a ad
E] - % af SbF
ba
@ do “og
? Alignment Pairing Scoring
a
ae
Template minutiae
Q6 Uncertainty has important implications for designing test plans and reporting

CO-1; SO-6; | b) | results’. Elaborate the statement with respect to systematic errors and sampling [10]
BL- 6 errors.

[5]
7 : 7 : - A
Q ) | Compare the categories of biometric systems based on ‘Identification’,
wuta ‘Authentication’ and ‘Verification’ of a person. Give examples of each category.
--- page 5 ---
b) Local binary pattern (LBP) algorithm is to be implemented for feature extraction
for face recognition on a given image matrix. Calculate the decimal value of the
central highlighted pixel. Consider that the neighboring pixels are considered in
the clockwise direction starting from the top left pixel.

pl [5]
CO-2; SO-2; 45 10 60
BL- 3

25 45 50

35 15 25
° istti icfmnettt [5]
CO-1: $0-6: Analyze how enrollment and acquisition errors impact biometric system
BL-4 *}°) performance. Discuss possible solutions to address them.
e7 [5]

CO-2; $O-1; | d) Discuss Daugman’s rubber sheet model for IRIS normalization.
BL-6
````

## 2022-23 · Re-Exam · Sem 6 · paper a2101d0a50a9

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/VI SEMESTER/BIOMETRICS/Biometrics, Sem-VI, Year 2022-23, Re Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (6 pages), mean OCR confidence 87.9

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& EN
Academic Year: 2022-2023
Program/s: B Tech / MBA Tech Year: III Semester: VI

Stream/s : Computers/ AI

Subject: Biometrics Time: 3 hrs (2.00 pmto 5:00 pm )

Date:__0) /duly/ 2023 No. of Pages: 6
Marks: 100

Re- Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. _1_ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

yo

1 20
e Answer briefly: 20]

[5]

CO-2; SO-1;
BL-2

The figure above shows the right image of a person captured through NIR
camera. Answer the following questions considering that you are using such
samples for iris based recognition.
1. Identify the feature of the iris that can be used to uniquely identify a
person.
2. Suppose you have to segment the iris from the image shown above,
identify the different challenges you will face in doing so.
Suggest any suitable algorithm for segmentation of the iris.
--- page 2 ---
b. | “Multimodal biometrics refers to the use of more than one source of | [5]
CO-4; SO-1; information for biometric recognition”, illustrate the statement with suitable
BL-2 examples.

CG; The following graphs (a) and (b) contain DET and ROC curves. Compare | [5]
them with respect to ease of assessing the overall performance of the system.

Detection Error Tradeoff (DET) curves

: —— Linear SVM
99% ; H |... Random Forest
3 95%
3
g 80%
g
& 50%
fd
$
= 20%
&
2
B 3%
1%
1% 5% 20% 30% 80% 95% 99%
False Positive Rate (Positive label: 1)
CO-1; SO-6; (a)
BL- 4
Receiver Operating Characteristic (ROC) curves
10 H
= 08 4
a
2
ra
g
= 064
é
g
= 04
2
3
~ &
2 0.2
— Linear SVM (AUC = 0.96)
0.0 —— Random Forest (AUC = 0.99)
0.0 02 04 0.6 08 Lo
False Positive Rate (Positive label: 1)
(b)
d. | If image ‘b’ is an enhanced image of image ‘a’ where the ridge width has | [5]
CO-2; SO-6; been reduced to one pixel, identify the technique used and state its
BL-3 significance.
2
--- page 3 ---
(a) (b)

an A Biometric system has to be designed for person Recognition. Discuss the [10]
or SO-2; | a) | challenges, privacy concerns and ideal biometric identifiers to be addressed.
The sensor installed for acquiring fingerprint scans of an individual for | [10]

b) authenticating the entry to a restricted area be used can provide a resolution
of only 250 pixels per inch (ppi). Considering this scenario, answer the

Q2 following:
CO-1: $0.2: 1. Identify the level of features which can be used to match the mate
BL-6 ; samples.
2. Discuss briefly the steps used to extract the selected features.
3. Justify the need of alignment of template and query fingerprint images
during matching phase.

a) | A biometric system for banking application is to be designed. The modalities | [10]
to be used have been finalized as finger print, signature and face. Multiple
samples of these modalities have been acquired. Answer the following
questions based on this scenario:

Q3 1. Identify the category/categories of multibiometrics this system will
~CO-3; $O2-; fall into.
BL-3 2. Choose a suitable fusion technique for this system and explain how
this fusion will be achieved.
3. Discuss the challenges which can be encountered if this system is used
over longer period of more than 10 years. Suggest a solution to rectify
this.
Q3 [10]
CO-1; $0-1; | p) Compare Parametric and Non parametric methods for computing biometric
— error confidence interval. Elaborate the Non Parametric technique.
Q4 a) | During the segmentation process of the iris, the integro-differential operator | [10]
assumes that the outer boundary of the iris can be approximated using a circle
CO-2; SO-1; - , 3 ?
BL-2 or an ellipse. Suggest and explain another method for segmentation stating

your reasons for its advantages.
--- page 4 ---
b)

Considering the Viola Jones algorithm for face detection and localization,
answer the following:
1. Justify the significance of the Haar features by giving suitable
examples.
2. Explain the significance of the integral image. Compute the integral
image for the image matrix shown below:

Q4 3.
CO-2; SO-1; 30 5 40
BL-3
25 | 45 50
5 5 5
4. State the need of the Adaboost process and explain the same.
Q5 a) | “Architecture of a multibiometric system refers to the sequence in which the
0-4: $0.2: multiple cues are acquired and processed”, in the same context discuss the
y ; types of multibiometric system with appropriate examples.
BL- 6 YP! yi! pprop p
b) | A biometric security solution has to be designed. [10]
1. Explain the significance of EER computed as given in the figure for
the system.
2. What will be the impact on FAR if FRR goes up.
3. For a very secure system suggest the changes required in FAR and
explain how it will impact user convenience.
e
Qs a a
8
CO-1; SO-6; P
BL-4 8 FAR FRR
S
‘oe
gt
Ex
Se
38 EER
of
Lo
2s
Sensitivity / level of security
Q6 a) | Fingerprint identification process is done by comparing the input probe image | [10]
CO-2; SO-; against a small subset of images in the database (gallery) having comparable
BL-4 index values which are computed as given in the diagram.
--- page 5 ---
Examine and justify how this technique allows for the successful indexing of
partial fingerprints.

b) | Interpret the figure given below and discuss performance measure of a system | [10]
with respect to FAR, FRR and Match scores.

0.1

0.09;

0.08+ <— Threshold {n} 4

Genuine distribution 4

0.07+
= p(sigenuine)

CJ
CO-1; SO-6; 2 0.067
BL-5 2

% 0.05+
Rel Impostor distribution,
& 0.04> p(s|impostor)

0
50 55 60 65 70 75 80 85
Match Score (s)

Q7 a) | You have to design a Fingerprint based biometric system for giving access to | [5]
1000 employees. Discuss the optimum steps you will undertake to design the

ey 80-6; same. Illustrate with a block diagram.
[5]
b) A biometric application for 750 employees of an organization using voice has
CO-1; SO-1: been designed. Five samples per person have been acquired The feature
BL-5S vectors generated are of dimension 13. If Euclidean distance is being used for

determining the identity of a person, determine the number of computations
to be performed for a rank 2 speaker identification system.

CO-1; SO-6; | c) . | Analyze the dependency of identification performance on the number of | [5]
Ble4 enrollments in a system. Discuss possible solutions to address them.
--- page 6 ---
CO-2; SO-6;
BL-4

d)

The diagram below explains the IRIDES matching process.

Infer the diagram
and state your conclusions. ~

ne

Subject 1, sample 1
Rr
PW es i

Subject 1, sample 2 :

ee AS

HD=0.2717 1

Pa se | ;

Subject 2, sample 1 i

HD = 0.4708

[5]
````

## 2018-19 · Final-Exam · Sem 8 · paper 1d91911acf2a

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/4th YEAR/COMPUTER/Sem_08/BIOMETRICS/Biometrics 2018-19 Final.pdf`
- Printed on paper: exam date: 13 April 2019
- Text: ocr (2 pages), mean OCR confidence 91.8

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHN! OLOGY MANAGEMENT & ENGINEERING

Program :B.Tech Integrated (COMPUTER) ~ : Year: IV Semester: VIII
Academic Y ear: 2018-2019 carson. “ “

Subject: Biometrics |“ z Mae. 70

Date: 13 April 2019 _,

MPSTME =
LIBRAE Dura oi

Final Examination

Instruction: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

NB:

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.

1. Justify the correctness of following statements with suitable example? [14]
a) Strength of feature components are independent of feature vector. [3]
b) “Wrong ROI selection will affect the overall performance of any Biometric System”. [3]
c) Robustness of any Biometric system is depend on richness of the Image Database. [3]
d) Multimodal Biometric system is always better compared to unimodal. [3]
e) Is PCA suitable for face recognition system? [2]
2. a) Find DCT of the following 4*4 facial image. [6]
2 4 4 2 Where C is 05 |. 0.5 05 0.5
4 6 8 3 0.653 | 0.2705 | -0.2705 | -0.653
2 8 10 4 0.5 -0.5 -0.5 0.5
3 8 6 2 ; 0.2705 | -0.653 | 0.653 | -0.2705
b) What are Minutiae? Explain limitations of Biometric systems based on Minutiae. [4]
c) Compare the two terms identification and verification in terms of Biometrics. [4]

3. Correct the sequence of the steps (to be followed to develop.a Biometric System) given below with your
justification. [14]
1)Feature Extraction 2) Preprocessing 3) Choosing Biometric Characteristics 4) Using the distance
measure to check the similarity of the query image 5) Feature Database Generation 6) Check the
performance 7) Finalizing the appropriate performance evaluation parameters 8) Designing the image
database.

4. a) Explain the sectorization of transforms for feature extraction in finger print recognition. [7]
b) Explain the various types of performance evaluation parameters and its significance in Biometric
System. [7]
Vee
--- page 2 ---
f

5, a) Explain palm print recognition system in detail. [7]

b) Explain the different characteristics of signature biometrics for network security. [7]

6. a) “Vector Quantization can be utilized only for obtaining the compactness of feature vector”. Do you

think this statement is complete”? Justify. [7]
b) Explain LBG algorithm. Implement LBG on the given iris biometric data set. [7]
Input Data Set Training Data Set
Length | Weight Length Weight
44 41 44 41
72 180 59 117
59 113 60 110
72 180
64 180
80 181
7. Write short notes on any two: [14]

a) Standard Test Best

b) Legal, Social and Ethical concerns of Biometric Systems.
c) Wavelet Transform

d) Limitations of Single Modal Biometric System.

242

}
````

## 2017-18 · Final-Exam · Sem 8 · paper 7d3803c108fe

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/4th YEAR/COMPUTER/Sem_08/BIOMETRICS/Biometrics 2017-18 Final.pdf`
- Printed on paper: max marks: 60; exam date: 07 May 2018
- Text: ocr (2 pages), mean OCR confidence 92.0

````text
“a

SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme:B.Tech Integrated (COMPUTER) «_ Year: IV Semester: vit

Academic Year: 2017-2018 ¢«

Lg

Marks:60 ©) %.%.

Date:07 May 2018 , Time: 2.00 pmeto 5.00 pm
Durations: 3, (lars) _ i

No. of Pages.t f
Be Se
* - sf

Final Examination (2017-18) ,

Subject:Biometrics “

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which'is provided for their use.

1) Question No. lis compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume suitable data if necessary.

Q1. Write a note on 3 Marks each
a. Similarity measures.
b. Performance evaluation parameters.
c. Biometric characteristics.
d. Min-Max Normalization.

Q2. 6 Marks each
a. “Morphological operations are suitable for signature feature extraction”, comment on this statement

with example.
b. “Multimodal biometrics system is always better compared to unimodal”.Comment on this statement

with example.

Q3. 6 Marks each
a. Is PCA suitable for face recognition system? Justify your answer with necessary details.
b. Vector quantization can be utilized only for obtaining compactness of feature vector. Do you think
statement is complete? Justify your answer.

Q4. 6 Marks each

a. Explain sectorization in transform domain in detail.
b. Give the mathematical expression of DCT. Generate 4 x 4 DCT Matrics.
--- page 2 ---
QS. 6 Marks each
a. What is a figure detection biometrics approach? Elaborate it with the help of GLCM.
b. Explain the creation of wavelet from transform.

Q6. 6 Marks each

a. Explain steps involved in Palm print recognition system.
b. Explain steps involved in Iris recognition system.

Q7. Comment on the correctness of the statements given below and justify your answer 3 Marks each

a. Feature components play important roles.

b. Dimensionality reduction is the key factor which affects the performance of any Biometrics based
solution. -

c. Specific feature extraction approaches are comparatively easier and better than generic.

d. Feature matching step does not:make much difference in the overall performance.
````

## 2016-17 · Final-Exam · Sem 2 · paper 9273819d800d

- Departments: Computer Engineering
- Programmes: M TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/COMPUTER/II SEMESTER/BIOMETRICS/Biometrics 2016-17 Final.pdf`
- Printed on paper: exam date: 6 May 2017
- Text: ocr (2 pages), mean OCR confidence 93.9

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: M. Tech (COMPUTER) A Year: I. Semester: II «

Academic Year: 2016-2017

Subject: Biometrics

‘Date: 6 May 2017 , wait
Dural
No. o

Final-Examination

ee

Instructions: Candidates should read carefully the instructions printed on the question paper and on the cover
of the Answer Book, which is provided for their use.

1) Question No. 01 is compulsory.

2) Out of remaining questions, attempt any 04 questions.

3) In all 05 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks. *
7) Assume Suitable data if necessary.

QI. Justify the correctness of following statements with suitable example. [14]
a. Biometrics trait selection need not consider the cultural psychology for developing the solution.
b. Dimensionality reduction is the key factor which affects the performance of any Biometrics based solution.
c. Feature selection need not be depended on the feature extraction algorithm.
d. Specific feature extraction approaches are comparatively easier and better than generic.
e. Feature matching step does not make much difference in the overall performance.
f. Signature recognition system is better suitable for verification.
g. Robustness of any biometrics system is depended on richness of the image database.

Q2. a. Suggest steps required to develop any biometrics system. Design specific algorithms w.r.t. each step. [14]
b. Compare and contrast between Generic and Specific feature extraction approaches.

Q3. a. Discuss the steps of PCA for developing the face recognition system. [14]

b. How the implementation of the face recognition system differs while considering its specific features and
generic features.

Q4. a. Explain the DCT sectorization technique of feature extraction. [14]

b. Explain clustering using LBG and K Means approach.

QS. a. Differentiate among ‘all steps of biometrics system development w.r.t. Finger print and Palm print. [14]
b. Explain the Text based and non-text based voice /speaker recognition.

Page 1 of 2
--- page 2 ---
“Ns

Q6. a. “Morphological operations are suitable for signature feature extraction” comment on this statement with [14]

example.
b. “Multomodal biometrics system is always better compared to unimodal” Comment on this statement with
example.
Q7. Write Note on [any two] [14]

a. Similarity measures

b. Performance evaluation parameters
c. Iris Recognition system

d. speaker recognition

Page 2 of 2
````

## 2015-16 · Final-Exam · Sem 2 · paper 3a39881a049c

- Departments: Computer Engineering
- Programmes: M TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/COMPUTER/II SEMESTER/BIOMETRICS/Biometrics 2015-16 Final.pdf`
- Printed on paper: max marks: 70; duration hours: 3; exam date: 07/05/2016
- Text: ocr (1 page), mean OCR confidence 91.9

````text
SVEM’sNMIMS SN) AGG
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT @ENGINEERING
Programme: M. Tech (COMPUTER) Year: I Semester: II

Academic Year: 2015-2016

Subject : Biometrics 5

Marks: 70

Time : 2.00 pm to 5.00 pm
Durations: 3 (hrs)

Date : 07/05/2016

Final-Examination

Instructions: Candidates Should read carefully the instructions printed on the question paper and on the
cover of the answer book, which is provided for their use. —
1. Question No.1 is compulsory .
2, Out of remaining questions, attempt any 4 questions
3. Inall 5 questions to be attempted
4. All questions carry equal marks.
5. Answer to each new question to be started ona fresh page.
6. Figures in brackets on the right hand side indicate full marks.
7. Assume Suitable data if necessary

Q1. Answer following Questions

a. Explain the prominent role of Biometric for today’s Network security. {06Marks]
b. Define FAR, FRR, FTR, ROI. ; [04 Marks]
c. Explain various Biometric characteristics. [04 Marks]
Q2. (a) Explain any 4 limitations to biometric system. [04 Marks]
(b) Explain how to use wavelet transform for feature extraction. [10 Marks]
Q3. (a) Differentiate between KFCG, LBG, KPE and K means techniques. [07 Marks]

(b) Explain sectorization technique in transform domain for feature extraction. {07 Marks]

Q4. (a) Explain all methods for feature extraction to develop finger print recognition system.
[10 Marks]
(b) Compare identification and verification with example. [04 Marks]
Qs. (a) Explain advantages and drawbacks of multimodal system and single modal recognition system.
{10 Marks]
(b) Explain any 2 image enhancement techniques for finger print recognition system.
[04 Marks]
Q6. (a) Explain Steps in Iris Recognition. [07Marks]

(b) Explain all methods for feature extraction to develop face recognition system. [07Marks]

Q7. (a) Explain all image enhancement techniques for finger print recognition system. {10 Marks]
(b) Speaker Recognition method and its variants [04 Marks]

4°

*
````

## 2015-16 · Re-Exam · Sem 2 · paper 414bfbf3df35

- Departments: Computer Engineering
- Programmes: M TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/COMPUTER/II SEMESTER/BIOMETRICS/Biometrics Batch 2015-16 Re Exam.pdf`
- Printed on paper: exam date: 01 July 2016
- Text: ocr (1 page), mean OCR confidence 91.9

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: M. Tech (Computer) . Year: I Semester: II
Academic Year: 2015-2016
Subject: Biometrics

Date: 01 July 2016
Re-Examination

Instructions: Candidates Should read carefully the instructions printed on the question paper aad on the
cover of the answer book, which is provided for their use.

1. Question No.1 is compulsory

2. Out of remaining questions, attempt any 4 questions

3. Inall 5 questions to be attempted

4. All questions carry equal marks.

5. Answer to each new question to be started ona fresh page.

6. Figures in brackets on the right hand side indicate full marks.

7. Assume Suitable data if necessary
Q1. Answer following Questions

a. Explain the prominent role of Biometric for today’s Network security. [06Marks]

b. Define FAR, FRR, FTR, ROI. [04 Marks]

c. What Behavioural Biometrics? Explain with Example. [04 Marks]
Q2. (a) Evaluate the benefits of Biometric system. [07 Marks]

(b) What is finger-scan biometric approach? Elaborate the finger-scan weaknesses. [07 Marks]
Q3. (a) Elaborate the Eigen-face facial scan technology. [07 Marks]

(b) How environment effects the facial-scan recognition approach? Discuss. [07 Marks]
Q4. (a) Explain Multimodal and Multi factor biometrics. [07 Marks]

(b) What is Feature Vector? Explain with One Example.
What is the role of it in Biometric Authentication? [07 Marks]

QS. (a) What is Vector Quantization ?
How Vector Quantization can be used to generate feature vector in Biometric Authentication ?

{07 Marks]

(b) Explain Colour Averaging Techniques and its application. [07 Marks]
Q6. (a) Explain Steps in Iris Recognition. [07 Marks]

(b) What are Minutiae ? Explain Limitation of Biometric Systems Based on Minutiae? [07Marks]
Q7. Write Short Notes on any two: {14 Marks]

(a) Face Recognition Methods.

(b) Speaker Recognition method and its variants.

(c) Legal, Social and Ethical Concerns of Biometric Recognition

(d) KPE and KEVR Vector Quantization Algorithms.

R= xX

V/,

jf
````

## 2014-15 · Final-Exam · Sem 2 · paper 86e2a7b05b6c

- Departments: Computer Engineering
- Programmes: M TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/COMPUTER/II SEMESTER/BIOMETRICS/Biometrics 2014-15 Final.pdf`
- Printed on paper: max marks: 60; duration hours: 3; exam date: 08/05/2015
- Text: ocr (2 pages), mean OCR confidence 92.1

````text
SVKM’s NMIMS ee pe
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & |

‘Sf we
Programme: M.Tech (COMP) Year: I Semester: II fl | f MPSTME )o i
St LIBRARY Js
. wes I$)
Academic Year: 2014-2015 iN Kaan wk =
Subject: Biometrics MS A A
Marks: 60 —
Date: 08/05/2015 Time : 10.00 am to 1.00 pm

Durations: 3 (hrs)

Final-Examination

Instruction: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.

NB:

1) Question No. 01 is compulsory.

2) Out of remaining questions, attempt any 04 questions.

3) In all 05 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q1. Comment on the correctness of the statements given below and justify your answer [12]
a. Feature components play important role.
b. Biometrics recognition system has no relation with CBIR system
c. Strength of Feature components are independent of Feature vector
d. EER can be plotted without considering FAR and FRR.

Q2. “Wrong ROI selection will affect the overall performance of any Biometrics system” comment
on this statement with justification y [12]

Q3. (a) “Speaker recognition system is different than speech recognition system” Whether this statement
is true or false justify your answer. [06]

(b) Discuss the “requirement study” phase of Biometrics designing system in detail. [06]

Q4. (a) Is PCA suitable for face recognition system? Justify your answer with necessary details

[06]

(b) Vector quantization can be utilized only for obtaining compactness of feature vector” do you
think this statement is complete? Justify your answer [06]
Q5. (a) Discuss various applications of any Biometrics system [06]
(b) Explain Limitation of Minutia based fingerprint recognition [06]
--- page 2 ---
Q6. (a) Take an example and suggest the feature vector generation for it using any transform method

w.r.t. reflection of its properties on it. [06]
(b) Explain Security aspects of Biometrics system w.r.t. any 6 real life applications [06]
Q7. Write note on any Three: [12]

a. Limitations of single modal Biometrics system
b. Gray averaging method

c. Need of Preprocessing

d. KFCG and LBG

——_——_--~
````

## 2013-14 · Final-Exam · Sem 2 · paper 52235cfeb60b

- Departments: Computer Engineering
- Programmes: M TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/COMPUTER/II SEMESTER/BIOMETRICS/Biometrics 2013-14 Final.pdf`
- Printed on paper: exam date: 08/05/2014
- Text: ocr (2 pages), mean OCR confidence 90.2
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
SVKM’s NMIMS .
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme: M. Tech (Computer) Year: I Semester: II
Academic Year: 2013-14 a
gat aid. Rit
Subject : Biometrics oy
Marké: 100. "a6 YZ y
Date : 08/05/2014 Time : 10.00 am:to 1} pm

D rations: 3 (hrs) Agr
Final Examination ‘ as oe oA

Instruction: Candidates should read carefully the instructions printed on the question paper and on the
cover of the Answer Book, which is provided for their use.

NB:

1) Question No. 01 is compulsory.

2) Out of remaining questions, attempt any 04 questions.

3) In all 05 questions to be attempted.

4) All questions carry equal marks. .

5) Answer to each new question to be started on a fresh page.
6) Figures in brackets on the right hand side indicate full marks.

QI. Comment on the correctness of the statements given below and justify your answer. [20]
a... Feature vector need not be compact and concise.
b. Image database needs to be rich enough w.r.t. its size only.
c. Biometrics system needs not be universal in nature.
d. FAR is the only parameter to comment on the performance of any Biometrics system.

Q2. Correct the sequence of the steps (to be followed to develop any Biometrics system) given below
with your justification and explain each step in detail. [20]
1.Feature extraction 2.preprocessing 3. Choosing biometrics characteristics 4. Using the distance
measure to check the similarity of the query image 5. Feature database generation. 6. Check the
performance 7. Finalizing the appropriate performance evaluation parameters 8. Designing the
Image database.

Q3. a.Draw the Basis image out of 4x4 Walsh transform matrix and explain how it can be used [20]
for generating feature vectors for the particular Biometrics system.
b. Differentiate among K-Means, LBG, KFCG, KPE.

Q4. a. Explain Iris recognition system w.r.t. following [20]
1. Designing of image database 2. Feature extraction 3. Simitarity measure 4. Performance
evaluation parameter.
b. Comment on following statement with justification : “feature extraction method may differ for
finger print recognition and signature recognition system”

W/o.
--- page 2 ---
QS. Write note on all possible features (and its extraction methods) that can extracted to develop

following systems. [20]
i. Face recognition system
ii. Finger print recognition system

Q6. Write note on any Four: [20]

a. Need of Multimodal biometrics system

b. Sectorization of transformed images for feature extraction.

c. speaker recognition system

d. Performance evaluation parameters for Biometrics system.

e. Color averaging methods for feature extraction with example

Q7. a. Explain palm print recognition system w.r.t. Designing the rich database, feature extraction [20]

similarity measure

b. Explain how wavelet transforms can be used for feature extraction ?
````

## 2013-14 · Re-Exam · Sem 2 · paper d4cdad6b67d7

- Departments: Computer Engineering
- Programmes: M TECH / COMPUTER
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/COMPUTER/II SEMESTER/BIOMETRICS/Biometrics Batch 2013-14 Re Exam.pdf`
- Printed on paper: exam date: 01/07/2014
- Text: ocr (2 pages), mean OCR confidence 90.8

````text
SVKM’s NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT & ENGINEERING

Programme:M. Tech (Computer) Year: I Semester: II

Academic Year: 2013-14

- aniTOTE OY may
Batch:2013-2014 on x »
cate stun ye

Subject : Biometrics

Le ™
Date :01/07/2014
Re-Examination

Instruction: Candidates should read carefully the instructions printed on the question paper and on the ~
cover of the Answer Book, which is provided for their use.

NB:

1) Question No.1 is compulsory.

2) Out of remaining questions, attempt any 4 questions.

3) In all 5 questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started ona fresh page.
6) Figures in brackets on the right hand side indicate full marks.

Q.1 Answer any four
a Compare identification and authentication 5
b Define (i)FAR (ii)GAR (iii) FRR 5
c Why to use biometrics? Explain. 5
d Explain characteristics of face features 5
.e What are the different similarity measures? 5
Q.2 a Explain the different characteristics of fingerprint biometrics for network 10
security.
b Explain all possible features and its extraction methods to develop face 10

recognition system..

Q3 a Explain PCA and its application in biometrics. 10
b Explain all possible image enhancement techniques for finger print image. 10
Q4 a Explain KFCG algorithm and give its advantages over LBG. 10
b Explain steps involved in Palm print recognition system. 10
Q5 a Write note on speaker recognition system. 10
b Discuss advantages and disadvantages of multimodal and uni modal 10

biometrics system.

\/2.
--- page 2 ---
Q.6

Q7

Discuss different signature verification scheme using feature extraction
method.

Explain sectorization in transform domain in detail.

Write short note on
Regional features

Use of wavelets in Biometrics

# ~~»

10

10

10
10
````

## 2011-12 · Exam not stated · Trim 3 · paper 443280015fb6

- Departments: Information Technology
- Programmes: M TECH / I T
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/I T/TRIM III/BIOMETRICAS/BIOMETRICS 2011-120001.pdf`
- Printed on paper: exam date: 09/05/2012
- Text: ocr (2 pages), mean OCR confidence 80.0
- 1 unreadable OCR line (stamps, scribbles, blank areas) left out; the raw OCR is in `question_bank/extracted_text/`.

````text
'\

SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Programme: M.Tech-I.T/Computer Year: I Trimester: II
Academic Year : 2011-2012 we
J aSXTUTE OF Mane.
mics: 100. Ka
Tarle:s1 ? > T2000 pho 5.00 pm

eee «this,
¥*y Mame ue oY
Instructions: 1. Attempt any five questions _

2. All questions carry equal marks (i.e. 20 Marks each)

Subject: Biometrics

Date: 09/05/2012
. Final - Examination

Q1) Justify the following statements
{a] Enlist the any five Physiological Biometric Characteristics.
[b] Differentiate between Verification and Identification.
[c] What are the Limitations of Multimodal Biometric systems?
[d] Define FAR and GAR .

Q2) [A] Give Steps of PCA for Face identification.
[B] Enlist all the color averaging methods. Explain any one method with example.

Q3) [A] Generate Hybrid Wavelet Transform from the given two orthogonal matrix.

1 1 1
1 1

A= B=|-2 1 1
1 -1

0 -1 1

[B] Apply the Hybrid transform generated in the Q3) [A] on the 1-D sequence
f(n)= {1, 2, 3, 1, 2, 3} and also prove the energy conservation principle.

Q4) [A] Give the Walsh 4x4 matrix and obtain the texture patterns for it.

[B] Give the 8-point haar wavelet transform matrix and apply it on the sequence
fin)= {1, 2, 3, 4, 1, 2, 3, 4}

} ;
Q5) [A] Explain Sectorization in 2-D transforms and obtain the 4-Sectors for Walsh 8x8
r } matrix.
[B] Extract the feature using method given in Q5 [A] for the image given below.

1 {1 [2 |2

3 |4 [5 |6

1 {3 |4 |2

2 |2 |2 |6
1
--- page 2 ---
Q6) Explain in brief KFCG algorithm for Face recognition. Take any 4x4 image and
Apply KFCG for the block size 1x2, compute the first codevector, split the
cluster into two and give two clusters along with their centriods.

Q7) What is Multimodal Biometrics, Explain any one Multimodal biometric method also
give the advantages and disadvantages of the Multimodal biometric identification.

````

## 2010-11 · Exam not stated · Trim 3 · ZIP of papers · paper 5a80dbc3531f · BIOMETRICS.pdf

- Departments: Information Technology
- Programmes: M TECH / I T
- Source: `02_Question_Papers/Legacy/M TECH/1ST YEAR/I T/TRIM III/BIOMETRICAS/M Tech I T TRIM III BIOMETRICS 2010-2011.zip`
- Text: text (2 pages)

````text
SVKM's NMIMS
Mukesh Patel School of Technolo   Mana erne
Programme:   M.Tech-I.TjComputer   Year:   I   Tri
Academic Year: 2010-2011
2.90 pm To 5.00 pm
3 hrs.
Instructions:   1. Attempt any five questions
2. All questions carry equal marks (i.e. 20 Marks each)
Ql) Justify the following statements
[a] Give any five Applications ofBi<.?!TI~tricIdentification.
[b] Differentiate between Verification and Identification.
[c] What are the Limitations ofBiometric systems?
[d] Define FAR, GAR and FRR.
Q2) [A] Give Steps of PC A for Face identification.
[B] Give the color averaging algorithms for iris recognition.
Q4) [A] Give the Walsh 4x4 matrix and obtain the texture patterns for it.
[B] Give the 8-point haar wavelet transform matrix and apply it on the sequence
f(n)= {O,1,2,3,0,   1,2, 3}
Q5) [A] Explain Sectorization in transforms and obtain the 4-Sectors for Walsh 8x8
matrix.
[B] Give anyone algorithm for Feature matching method.
Q6) [A] Explain in brief Linde Buzo Gray (LBG) algorithm for Face recognition.
[B] Apply LBG on the image given below, for the block size lx2 as shown below,
compute the first codevector,   split the cluster into two and give two clusters
along with their centriods and mean squared error.
--- page 2 ---
Q7) What is Multimodal Biometrics, Explain anyone Multimodal biometric method also
give the advantages and disadvantages of the Multimodal biometric identification.
````
