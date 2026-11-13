# Security Essentials in Applied AI: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 3e82d84ded7b

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Security Essentials in Applied AI/ANS_Security Essentials in Applied AI(703DB0C068)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (7 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Security Essentials in Applied AI
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 7 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions attempt any 4
6. In total 5 questions needs to be answered
7. All Questions carry equal marks
Q1 (Compulsory)
Q1 (i) Explain how bias in training data can influence the outcomes of an AI system with a suitable example.
(4)
Bias in training data occurs when the dataset used to train an AI model does not accurately represent the
diversity of the real-world population. Since machine learning models learn patterns directly from training data,
any imbalance or systematic error present in the dataset can significantly influence the predictions generated
by the AI system.
When biased data is used for training, the AI model may produce unfair, inaccurate, or discriminatory
outcomes. This problem arises because the model assumes that the patterns observed in the training data are
valid for all scenarios.
For example, consider an AI-based hiring system trained on historical employee data from a company where
most employees are male. If the dataset primarily contains successful profiles of male candidates, the model
may incorrectly learn that male applicants are more suitable for the job. As a result, the system might unfairly
rank male candidates higher than equally qualified female candidates.
Similarly, in facial recognition systems, if the training dataset contains more images of lighter-skinned
individuals than darker-skinned individuals, the model may achieve higher accuracy for one group and lower
accuracy for others.
Such biases can lead to ethical issues, loss of trust, and legal consequences. To reduce bias, organizations must
ensure diverse datasets, perform fairness testing, and apply bias mitigation techniques during model
development.
Q1 (ii) Explain the importance of encryption in protecting AI system data at rest and in transit with suitable
examples. (4)
Encryption is a critical security technique used to protect sensitive data by converting it into an unreadable
format that can only be accessed using a decryption key. In AI systems, encryption plays an essential role in
safeguarding data both at rest (stored data) and in transit (data being transmitted across networks).
Data at rest refers to information stored in databases, data lakes, or storage systems used for training machine
learning models. If attackers gain access to these storage systems, they could steal sensitive information such
**********   **********
--- page 2 ---
as medical records, financial transactions, or personal data. Encrypting stored datasets ensures that even if
unauthorized access occurs, the data remains unreadable without the proper encryption key.
Data in transit refers to information transferred between systems, such as when users send requests to AI APIs
or when data is transmitted between cloud servers. Encryption protocols such as TLS (Transport Layer Security)
ensure that attackers cannot intercept and read the transmitted data.
For example, in a healthcare AI system that analyzes patient records, encryption ensures that patient
information stored in hospital databases remains protected and that communication between the hospital
system and the AI model is secure.
Thus, encryption helps maintain confidentiality, integrity, and trustworthiness of AI systems.
Q1 (iii) Analyze how authentication and authorization mechanisms help secure API endpoints in AI
applications and prevent unauthorized access. (4)
AI applications often expose APIs that allow users or systems to interact with machine learning models. These
APIs may provide services such as predictions, analytics, or data processing. Without proper security
mechanisms, attackers could exploit these endpoints to access sensitive data or manipulate system behavior.
Authentication and authorization are two important mechanisms that secure API endpoints.
Authentication verifies the identity of a user or system attempting to access the API. Common authentication
methods include API keys, passwords, OAuth tokens, or JSON Web Tokens (JWT). For example, when a user
sends a request to an AI prediction API, the system first verifies the user’s credentials before processing the
request.
Authorization determines what actions an authenticated user is allowed to perform. This is often implemented
using Role-Based Access Control (RBAC). For example, administrators may have permission to deploy or retrain
models, while regular users may only be allowed to request predictions.
Together, authentication and authorization ensure that only legitimate users access AI services and that they
operate within permitted privileges. These mechanisms help prevent unauthorized access, data leaks, and
misuse of AI models.
Q1 (iv) Analyze the compliance requirements for deploying AI systems in industries such as healthcare or
finance. (4)
AI systems deployed in highly regulated industries such as healthcare and finance must comply with strict
regulatory and security requirements to protect sensitive information and ensure responsible decision-making.
In the healthcare sector, AI systems often process patient medical records and diagnostic data. Regulations
such as HIPAA require organizations to ensure the confidentiality, integrity, and availability of patient
information. Healthcare AI systems must implement strong encryption, secure access control mechanisms, and
maintain audit logs to track data access.
In the financial sector, AI systems may be used for fraud detection, credit scoring, or risk assessment. Financial
institutions must comply with strict regulatory standards that require transparency, fairness, and data
protection. Organizations must ensure that AI models do not introduce bias or discriminatory outcomes.
Compliance requirements also involve implementing data privacy protections, monitoring mechanisms, and
secure infrastructure. Organizations must document how data is collected, processed, and used within AI
systems.
Failure to comply with these regulations may lead to legal penalties, financial losses, and reputational damage.
Therefore, regulatory compliance is a crucial aspect of deploying trustworthy AI systems.
Q1 (v) Analyze adversarial attacks such as evasion, poisoning, and model inversion and their impact on AI
model reliability. (4)
2
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 3 ---
Adversarial attacks are deliberate attempts by attackers to manipulate AI systems in order to cause incorrect
predictions or extract sensitive information from models.
Evasion attacks occur during the model inference phase. In this type of attack, attackers modify input data
slightly to deceive the model into producing incorrect predictions. For example, small pixel changes in an image
may cause an object recognition model to misclassify a stop sign as another object.
Poisoning attacks occur during the training phase. Attackers insert malicious samples into the training dataset
to influence the model’s learning process. This can reduce model accuracy or introduce hidden vulnerabilities.
Model inversion attacks attempt to extract sensitive training data from the model by analyzing its outputs. For
example, attackers may reconstruct images or personal data used in training the model.
These attacks reduce the reliability and trustworthiness of AI systems. If not addressed, adversarial attacks can
lead to incorrect predictions, privacy violations, and system compromise. Implementing secure training
practices, adversarial defenses, and monitoring mechanisms is essential to protect AI models.
Q2
Q2 (i) AI bias in healthcare diagnostic system (10)
AI-based diagnostic systems are increasingly used in healthcare to predict diseases and assist doctors in clinical
decision-making. However, bias in training data can significantly affect the reliability and fairness of these
systems.
If the dataset used to train the diagnostic model is not representative of the entire population, the AI system
may produce inaccurate predictions for certain groups.
For example, suppose a disease prediction model is trained primarily using medical records from middle-aged
adults. When the same model is used to diagnose diseases in elderly patients or children, its predictions may be
less accurate because it has not learned patterns relevant to those age groups.
Similarly, if the dataset contains more data from patients belonging to one ethnic group, the model may
perform poorly for other ethnic groups. This can result in misdiagnosis or delayed treatment.
Bias Detection Techniques
Organizations can detect bias using various techniques such as:
•   Statistical fairness analysis
• Performance comparison across demographic groups
•   Fairness metrics such as equal opportunity or demographic parity
These techniques help identify whether the model behaves differently for different population groups.
Bias Mitigation Techniques
Several methods can reduce bias in AI systems:
• Data balancing: ensuring datasets contain diverse and representative samples.
• Data augmentation: increasing samples from underrepresented groups.
•   Fairness-aware algorithms: modifying training algorithms to reduce discrimination.
• Model auditing: regularly evaluating model performance and fairness.
Importance
Reducing bias improves:
• Model fairness
•   Patient safety
•   Trust in AI healthcare systems
Therefore, addressing bias is essential for building ethical and reliable healthcare AI systems.
Q2 (ii) DREAD threat modeling framework in healthcare AI system (10)
The DREAD framework is a risk assessment model used in threat modeling to prioritize security threats based
on their severity and impact.
3
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 4 ---
DREAD evaluates threats using five key factors:
1. Damage Potential
2. Reproducibility
3. Exploitability
4. Affected Users
5. Discoverability
Each factor is assigned a score, which helps determine the overall risk level of a threat.
Damage Potential
This measures the potential harm caused by an attack. In a healthcare diagnostic system, an attack that
manipulates medical predictions could lead to incorrect treatment decisions and severe patient harm.
Reproducibility
This factor evaluates how easily an attack can be repeated. If attackers can repeatedly exploit a vulnerability in
the diagnostic system, the risk level becomes higher.
Exploitability
Exploitability measures how easy it is for attackers to perform the attack. Vulnerabilities that require minimal
technical expertise or tools pose higher risks.
Affected Users
This factor estimates the number of users affected by the attack. In healthcare systems, an attack could impact
thousands of patients relying on AI-based diagnoses.
Discoverability
Discoverability assesses how easily attackers can identify system vulnerabilities.
Importance in Threat Prioritization
By calculating scores for each factor, organizations can rank threats according to severity and allocate resources
accordingly.
For example:
• Data breach → High priority
• Minor logging error → Low priority
Thus, the DREAD framework helps healthcare organizations implement risk-based security management for AI
systems.
Q3
Q3 (i) Importance of integrating security throughout the AI lifecycle (10)
Security must be integrated throughout the AI development lifecycle to ensure that AI systems remain safe,
reliable, and resilient against cyber threats.
The AI lifecycle typically includes stages such as data collection, model training, testing, deployment, and
monitoring. If security considerations are ignored during early stages, vulnerabilities may emerge later during
deployment.
During data collection, organizations must ensure that training datasets are secure and free from malicious
manipulation. Failure to verify data sources may result in data poisoning attacks.
During model development, developers should implement secure coding practices and protect model
parameters from unauthorized access.
During deployment, AI systems must use secure APIs, authentication mechanisms, and encryption to protect
data transmission.
Neglecting security in early stages can create serious vulnerabilities. For example, if training data is
compromised, the resulting AI model may produce incorrect predictions even after deployment. Similarly,
poorly secured APIs can allow attackers to access or manipulate AI services.
4
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 5 ---
Integrating security practices such as threat modeling, vulnerability testing, and continuous monitoring
ensures that potential risks are identified and mitigated early.
Thus, adopting a secure AI development lifecycle helps organizations build trustworthy and resilient AI
systems.
Q3 (ii) Ethical guidelines for AI fraud detection system (10)
A financial institution deploying an AI-based fraud detection system must ensure that the system operates
ethically and responsibly while processing large volumes of customer transaction data.
AI Governance
AI governance refers to policies and frameworks that guide responsible AI development. Organizations must
define clear policies regarding how the AI system collects, processes, and analyzes financial data.
Governance mechanisms should ensure transparency, accountability, and fairness in automated decision-
making.
User Privacy
Financial transactions contain sensitive personal and financial information. The system must implement strong
privacy protections such as encryption, access control, and anonymization techniques.
Organizations should also follow privacy regulations that limit unnecessary data collection.
Informed Consent
Customers should be informed about how their data is used in fraud detection systems. Financial institutions
must clearly communicate data usage policies and obtain user consent where required.
Responsible Deployment Guidelines
To ensure ethical deployment, organizations should:
• Conduct bias and fairness assessments
• Implement strong security measures
•   Maintain transparency in automated decisions
•   Establish oversight mechanisms
By following these guidelines, financial institutions can deploy AI fraud detection systems that are secure,
ethical, and compliant with regulatory standards.
Q4
Q4 (i) RBAC in AI healthcare management system (10)
Role-Based Access Control (RBAC) is a security mechanism that restricts system access based on user roles
rather than assigning permissions individually to users.
In an AI-powered healthcare management system, RBAC ensures that medical professionals and staff can only
access information relevant to their responsibilities.
Role Definition
The system may include several roles such as:
•   Doctors
•   Nurses
•   Administrators
•   Patients
Each role has different responsibilities and requires access to different system resources.
Permission Assignment
Permissions are assigned based on roles:
Doctors may access patient records, diagnostic reports, and treatment recommendations generated by AI
models.
Nurses may access patient records and update patient care information but may not modify AI model settings.
5
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 6 ---
Administrators may manage user accounts, system configuration, and infrastructure.
Patients may view their own medical records but cannot access data belonging to other patients.
Implementation
When a user logs into the system, authentication verifies their identity. The system then checks their assigned
role and grants access only to permitted resources.
RBAC helps prevent unauthorized access, reduces data breaches, and ensures that sensitive healthcare data
remains protected.
Q5
Q5 (i) Role of encryption and hashing in AI data storage (10)
Encryption and hashing are essential cryptographic techniques used to secure data stored in AI systems.
Encryption converts readable data into an unreadable format using cryptographic algorithms. Only authorized
users with the correct decryption key can restore the original data.
There are two main types of encryption used in AI data storage:
Symmetric Encryption uses a single key for both encryption and decryption. Algorithms such as AES are widely
used for encrypting large datasets stored in AI systems.
Asymmetric Encryption uses two keys: a public key and a private key. This method is often used in secure
communications.
Hashing is another cryptographic technique used to ensure data integrity. Hash functions convert data into
fixed-length values called hash codes. Even a small change in the input data produces a completely different
hash value.
In AI systems, hashing is commonly used for securing passwords and verifying file integrity.
Together, encryption and hashing ensure data confidentiality, integrity, and protection against unauthorized
access.
Q6
Q6 (i) Importance of DPIAs in AI systems (10)
Data Protection Impact Assessments (DPIAs) are systematic evaluations used to identify privacy risks associated
with processing personal data.
AI systems often process large datasets containing sensitive information such as medical records, financial
transactions, and personal identifiers.
DPIAs help organizations evaluate how data processing activities may affect individuals’ privacy and define
mitigation measures.
The DPIA process involves describing the data processing activity, identifying potential risks, evaluating impacts,
and implementing safeguards.
Benefits include improved regulatory compliance, early risk identification, and stronger data protection
mechanisms.
DPIAs therefore help organizations build privacy-preserving AI systems.
Q6 (ii) OAuth-based authentication for AI recommendation API (10)
OAuth is a widely used authorization framework that allows users to grant limited access to their resources
without sharing credentials.
In an AI-powered recommendation system, OAuth can secure API endpoints by validating user identity and
controlling access permissions.
The process begins when a user attempts to access the recommendation API. The system redirects the user to
an authorization server where authentication occurs.
6
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 7 ---
After successful authentication, the server generates an access token. The client application includes this token
in subsequent API requests.
The API server verifies the token before processing requests.
OAuth improves security by preventing credential exposure and enabling controlled access to AI services.
Q7
Q7 (i) GDPR-compliant data management strategy for AI analytics platform (10)
A GDPR-compliant data management strategy ensures that AI systems process personal data responsibly.
Key practices include obtaining user consent, collecting only necessary data, anonymizing personal identifiers,
and implementing secure storage mechanisms.
Organizations must also provide users with rights such as data access, correction, and deletion.
Regular audits and monitoring ensure compliance with regulatory requirements.
Q7 (ii) Adversarial robustness techniques for AI models (10)
Adversarial robustness techniques help protect AI models from malicious inputs designed to manipulate
predictions.
Common defense methods include:
•   Adversarial training, where models are trained using adversarial examples.
•   Input preprocessing, which removes adversarial perturbations.
•   Defensive distillation, which improves model stability.
• Robust model architectures, designed to resist adversarial attacks.
While these techniques improve security, they may increase computational complexity and may not fully
eliminate vulnerabilities.
Therefore, organizations must combine multiple defense strategies to ensure robust AI systems.
7
**********   **********
Sensitivity: LNT Construction Internal Use
````

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper 9a4b0bcf9f57

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Security Essentials in Applied AI/ANS_Security Essentials in Applied AI(703DB0C068)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Apr 2025
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Security Essentials in Applied AI
Date: 28 Apr 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions attempt any 4
6. In total 5 questions needs to be answered
7. All Questions carry equal marks
Q1 (Compulsory - 5 x 4 Marks = 20 Marks)
1. Explain the concept of AI transparency and its role in ethical AI.
AI transparency refers to making AI decision-making processes understandable, explainable, and
interpretable to stakeholders. It ensures users can trust AI systems and understand how decisions are
made.
Role in Ethical AI:
• Fairness & Bias Detection: Transparent AI helps identify and mitigate biases in models.
• Accountability: Allows stakeholders to audit AI decisions and hold organizations responsible
for outcomes.
• User Trust: Increases confidence in AI-driven decisions, especially in sensitive domains like
healthcare and finance.
• Regulatory Compliance: Regulations like GDPR require transparency in AI models to protect
user rights.
2. Describe the layered security approach and its relevance in AI applications.
A layered security approach (also known as defense-in-depth) involves implementing multiple
security measures across different layers to protect AI applications.
Layers of Security in AI:
1. Data Security: Encrypting and anonymizing AI training data to prevent leaks.
2. Model Security: Preventing adversarial attacks and model extraction threats.
1
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 2 ---
3. Application Security: Protecting APIs, authentication, and authorization mechanisms.
4. Network Security: Implementing firewalls and intrusion detection systems.
5. User Access Control: Using Role-Based Access Control (RBAC) to restrict access based on
user privileges.
Relevance in AI:
•   Protects against adversarial attacks.
• Ensures compliance with security regulations.
• Reduces risks associated with unauthorized data access.
3. Key differences between symmetric encryption and hashing in securing AI data
stores.
Feature   Symmetric Encryption   Hashing
Purpose   Protects data confidentiality   Ensures data integrity
Uses a shared secret key for encryption and No keys are used, converts data to a fixed-
Key Usage
decryption   length hash
Reversibility Reversible (decryptable)   Irreversible (one-way function)
Examples   AES, DES   SHA-256, MD5
Use Case in   Ensuring data integrity and preventing
Encrypting sensitive AI models and datasets
AI   tampering
4. Explain Data Protection Impact Assessments (DPIAs) for AI projects.
A DPIA is a systematic process used to identify and minimize risks related to personal data processing
in AI projects.
Steps in a DPIA:
1. Identify the data processing activity (e.g., AI model training on personal data).
2. Assess the necessity and proportionality of data collection.
3. Analyze risks to individuals' privacy and data security.
4. Implement measures to mitigate these risks.
5. Monitor and review DPIA outcomes periodically.
Importance in AI:
• Ensures compliance with GDPR and other privacy laws.
• Helps organizations minimize potential privacy risks in AI applications.
5. Differentiate between evasion attacks, poisoning attacks, and model inversion in
adversarial machine learning.
2
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 3 ---
Attack Type   Description   Example
Evasion   Slightly modifies input data to deceive Changing pixel values in an image to fool a
Attack   the model.   facial recognition AI.
Poisoning   Injects malicious data into training   Introducing biased data in a spam detection
Attack   datasets to corrupt AI models.   model to misclassify spam emails.
Model   Reverse-engineers the training data   Extracting patient details from an AI-driven
Inversion   from an AI model’s outputs.   healthcare model.
Q2
a) Explain SHAP technique used for improving AI model explainability.
SHAP (SHapley Additive exPlanations) is a game-theoretic approach to explain the predictions of
machine learning models.
Key Features:
• Assigns a Shapley value to each feature, quantifying its impact on a prediction.
• Works with both black-box and interpretable models.
• Used in high-stakes AI applications like healthcare and finance to enhance trust and
compliance.
Example: In a loan approval AI, SHAP can show that a high credit score had the most positive impact
on approval.
b) Explain the DREAD threat modeling methodology and its relevance in identifying AI
security threats.
DREAD is a risk assessment framework used to evaluate potential AI security threats.
Factor   Description   Example in AI Security
Data leakage from an AI-powered
Damage   Impact of the attack
chatbot
Adversarial attacks on image
Reproducibility How easy is the attack to replicate?
classifiers
How easily can the vulnerability be
Exploitability   Model stealing via API queries
exploited?
Affected Users Number of users impacted   Unauthorized facial recognition use
How easily can an attacker find the   Public AI models with exposed
Discoverability
vulnerability?   endpoints
Q3
a) Symmetric encryption and hashing techniques used for securing AI data stores.
3
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 4 ---
• Symmetric Encryption: AES, DES for encrypting AI training data.
• Hashing: SHA-256, bcrypt for data integrity verification.
Example: Encrypting AI model weights before storing in cloud environments.
b) Ethical challenges in AI healthcare applications & mitigation strategies.
Challenge   Mitigation Strategy
Bias in AI decisions Use diverse datasets and fairness constraints.
Privacy concerns   Anonymize and encrypt patient data.
Explainability   Use SHAP, LIME for interpretable AI.
Q4
a) Role-Based Access Control (RBAC) and its implementation in AI security.
RBAC ensures only authorized users access specific AI resources.
Implementation in AI:
1. Data Access Control: Restrict access to training data based on user roles.
2. Model Access Control: Limit who can modify or retrain AI models.
3. API Security: Implement role-based authentication for AI endpoints.
b) GDPR compliance principles in AI applications.
Principle   AI Implementation
Data Minimization Collect only necessary user data.
Transparency   Explain AI decisions to users.
User Consent   Allow users to opt in/out of AI data processing.
Q5
a) Steps for integrating Keycloak for authentication.
1. Install Keycloak & set up a realm.
2. Create clients and configure authentication.
3. Implement OAuth2/JWT for secure authentication.
b) Compliance requirements for AI in healthcare.
4
**********   **********
Sensitivity: LNT Construction Internal Use
--- page 5 ---
• HIPAA: Protects patient data in the U.S.
• GDPR: Ensures patient data privacy in Europe.
• FDA regulations: Governs AI use in medical diagnostics.
Q6
a) Machine Learning in incident response & security monitoring.
• Threat Detection: AI analyzes network anomalies to detect cyberattacks.
• Automated Response: AI systems mitigate threats by blocking malicious activities.
b) Importance of OAuth and JWT in AI API security.
• OAuth 2.0: Provides secure authorization for AI APIs.
• JWT (JSON Web Token): Ensures secure data exchange between clients and servers.
Q7
a) FGSM Adversarial Attack and defenses.
• FGSM: Generates adversarial examples by adding small perturbations to input data.
•   Effect: Causes deep learning models to misclassify images.
• Defense: Adversarial training, model regularization, and defensive distillation.
5
**********   **********
Sensitivity: LNT Construction Internal Use
````
