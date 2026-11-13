# Essentials of Computer Science: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 6ca6ce1e6ccf

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/BTech_CS_7055/Essentials of Computer Science/ANS_Essentials of Computer Science(702CS0C005)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 25 Nov 2025
- Text: text (8 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE)
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Essentials of Computer Science
Date: 25 Nov 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 8 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Ans 1. a (5 marks, 1x5)
The von Neumann architecture is a computer design model proposed by John von Neumann in 1945. It
describes a system where the CPU, memory, and input/output devices are interconnected and share a common
bus system.
Key components: Explain all the key components in details (1 marks each)
1. Central Processing Unit (CPU) – Executes instructions.
2. Memory Unit – Stores both data and instructions.
3. Control Unit – Directs operations of the processor.
4. Arithmetic Logic Unit (ALU) – Performs calculations and logical operations.
5. Input/Output Devices – Facilitate communication with the external environment.
Ans 1. b (any 5) 1 marks each
Procedural Oriented Programming   Object-Oriented Programming
In procedural programming, the program is divided   In object-oriented programming, the program is
into small parts called functions.   divided into small parts called objects.
Procedural programming follows a top-down   Object-oriented programming follows a bottom-up
approach.   approach.
There is no access specifier in procedural   Object-oriented programming has access specifiers
programming.   like private, public, protected, etc.
********** 1 **********
--- page 2 ---
Procedural Oriented Programming   Object-Oriented Programming
Adding new data and functions is not easy.   Adding new data and function is easy.
Procedural programming does not have any proper   Object-oriented programming provides data hiding
way of hiding data so it is less secure.   so it is more secure.
In procedural programming, overloading is not   Overloading is possible in object-oriented
possible.   programming.
In procedural programming, there is no concept of   In object-oriented programming, the concept of
data hiding and inheritance.   data hiding and inheritance is used.
Ans 1. c (5 marks, each is 1 marks)
An operating system is a system software that manages computer hardware, software resources, and provides
services for computer programs. The image outlines five key components: Explain all this 5 components
• Memory Manager
•   Processor Manager
•   Device Manager
•   File Manager
• User Command Interface
Ans 1.d (5 marks, each 1 marks)
Benefits of Cloud Computing
Explain any 5 from following:
•   Highly Scalable
• More Flexible
• Reduced Infrastructure
•   Higher Security
• Back-up & Disaster Recovery
• No Location Constraints
Ans 2. a (10 marks, 2+2+2+2+2)
ROM (Read-Only Memory) is a type of non-volatile memory used in computers and electronic devices. It stores
permanent data and instructions that are essential for system operation, such as firmware or the BIOS in a
computer.
•   Non-volatile: Retains data even when power is turned off.
•   Pre-set memory: Data is written during manufacturing or programming and cannot be easily modified.
•   Fast access time: ROM provides quick read access to stored data.
• Permanent storage: Ideal for storing system-level instructions.
•   Expensive to manufacture: Especially for types that are hard-coded during production.
********** 2 **********
--- page 3 ---
Types of ROM:
1. PROM (Programmable ROM)
2. EPROM (Erasable Programmable ROM)
3. EEPROM (Electrically Erasable Programmable ROM)
4. EAROM (Electrically Alterable ROM)
Ans 2. b (10 marks, 2+2+3+3)
Convert (11101101)₂ to Base 10   2 marks
This is a binary number. To convert to decimal:
(11101101)2 = 1×2^7 + 1×2^6 + 1×2^5 + 0×2^4 + 1×2^3 + 1×2^2 + 0×2^1 + 1×2^0=128+64+32+0+8+4+0+1=237
Convert (170)₁₀ to Base 2   2 marks
Divide 170 by 2 repeatedly:
• 170 ÷ 2 = 85 → remainder 0
• 85 ÷ 2 = 42 → remainder 1
• 42 ÷ 2 = 21 → remainder 0
• 21 ÷ 2 = 10 → remainder 1
• 10 ÷ 2 = 5 → remainder 0
• 5 ÷ 2 = 2 → remainder 1
• 2 ÷ 2 = 1 → remainder 0
• 1 ÷ 2 = 0 → remainder 1
Reading remainders bottom-up:
(170)10 =(10101010)2
Convert (101011)₂ to Gray Code   3 marks
Gray code: first bit remains the same, each next bit is XOR of previous and current bit.
Binary: 1 0 1 0 1 1
Gray:
•   First bit = 1
• 1⊕0 = 1
• 0⊕1 = 1
• 1⊕0 = 1
• 0⊕1 = 1
• 1⊕1 = 0
********** 3 **********
--- page 4 ---
So:
(101011)2→111110 (Gray Code)
Convert (2E7)₁₆ to Base 8   3 marks
Hex to Binary:
• 2 → 0010
• E → 1110
• 7 → 0111
→ Binary: 001011100111
Group into 3-bit chunks:
001 011 100 111 → Octal:
• 001 → 1
• 011 → 3
• 100 → 4
• 111 → 7
So:
(2E7)16 = (1347)8
Ans 3.a (10 marks, 2x5) Explain any 5
Programming Concepts – An Overview
Few important concepts:
•   Eager Evaluation
•   Lazy Evaluation
•   Procedures
•   Functions
•   External State
•   Internal State
•   Concurrency
•   Static vs Dynamic Typing
Ans 3.b (10 marks)
function findSecondLargest(arr):
if length of arr < 2:
return "Array must have at least two elements"
first = -∞
********** 4 **********
--- page 5 ---
second = -∞
for each element x in arr:
if x > first:
second = first
first = x
else if x > second and x != first:
second = x
if second == -∞:
return "No second largest element found"
else:
return second
Ans 4.a (10 marks, 2x5)
An explanation of the different states of a process as shown in a typical Job and Process Status Diagram in
operating systems:
• New
• Ready
• Running
•   Waiting (Blocked)
• Terminated (Exit)
• Suspended (Optional)
Ans 4.b (10 marks, 2.5x4)
Explain each in details definition, works, examples
• Time Sharing
•   Buffering
•   Spooling (Simultaneous Peripheral Operations On-Line)
• Caching
Ans 5.a (10 marks, 2x5)
Certain common characteristics can be used to assess distributed systems:
Explain in detailed any five
********** 5 **********
--- page 6 ---
•   Heterogeneity
• Openness
•   Security
•   Scalability
•   Failure Handling
•   Concurrency
•   Transparency
Ans 5.b (10 marks, 2x5)
Challenges of Secure Programming explain all in details.
•   Vigilance
o Continuous monitoring and proactive measures to ensure security.
•   Malicious Influence
o Refers to the intentional manipulation or exploitation of software vulnerabilities by attackers.
•   Vulnerabilities as Bugs
o Bugs are coding mistakes, often leading to security vulnerabilities.
•   Vulnerability Chains
o A sequence of interconnected vulnerabilities exploited together by attackers.
• Bugs and Entropy
o Refers to the unpredictability and disorder in the system due to bugs and poor design.
Ans 6.a (10 marks, 2+2x4)
Explain Cloud Interoperability in details then its categories.
Cloud Interoperability Categories
•   Platform
•   Application
• Management
•   Publication and Acquisition
Ans 6.b (10 marks, 2+2+2x3)
A Cloud Service Provider (CSP) is a company that offers cloud computing services such as storage, networking,
databases, software, analytics, and more over the internet. These services are typically offered on a pay-as-you-
go basis.
Why Are CSPs Important in Cloud Computing? CSPs play a crucial role in enabling:
•   Scalability: Easily scale resources up or down.
•   Cost Efficiency: Pay only for what you use.
•   Accessibility: Access services from anywhere.
•   Security: Advanced security features and compliance.
•   Innovation: Rapid deployment of new technologies.
********** 6 **********
--- page 7 ---
Features and Services of 3 Major CSPs explain in terms features and services
Amazon Web Services (AWS)
Microsoft Azure
Google Cloud Platform (GCP)
Ans 7.a (10 marks, 2+2x4)
Explain Role of Cloud Computing in Machine Learning
Cloud computing provides the computational power, storage, and scalability needed for machine
learning tasks. It enables researchers, developers, and businesses to build, train, and deploy ML models
without investing in expensive hardware.
How Cloud Infrastructure Supports ML (any 4)
o Scalable Compute Resources
o Storage for Large Datasets
o Pre-built ML Services
o Collaboration and Accessibility
o Model Deployment and Monitoring
o Cost Efficiency
Ans 7.b (10 marks, 5+5)
Applications of Supervised Learning
• Email Spam Detection
o   Classifies emails as "spam" or "not spam" based on labeled examples.
• Medical Diagnosis
o Predicts diseases based on patient data (e.g., symptoms, test results).
•   Credit Scoring
o Assesses loan risk by analyzing historical financial data.
• Image Classification
o   Identifies objects in images (e.g., cats vs. dogs).
• Speech Recognition
o Converts spoken language into text using labeled audio data.
• Sentiment Analysis
o Determines the sentiment (positive/negative) of text reviews or social media posts.
Applications of Unsupervised Learning
• Customer Segmentation
o Groups customers based on purchasing behavior for targeted marketing.
• Anomaly Detection
o   Identifies unusual patterns in data (e.g., fraud detection in banking).
• Market Basket Analysis
o Finds associations between products bought together (used in recommendation systems).
• Document Clustering
********** 7 **********
--- page 8 ---
o Organizes large sets of documents into topics or categories.
•   Dimensionality Reduction
o Reduces the number of features in data while preserving structure (e.g., PCA for visualization).
• Genetic Data Analysis
o Clusters genetic sequences to identify similarities and evolutionary relationships.
********** 8 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper 7e2b5070faee

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/BTech_CS_7055/Essentials of Computer Science/ANS_Essentials of Computer Science(702CS0C005)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (10 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE)
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Essentials of Computer Science
Date: 02 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 10 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Ans 1.a (5 marks, 1x5)
The von Neumann architecture is a computer design model proposed by John von Neumann in 1945. It
describes a system where the CPU, memory, and input/output devices are interconnected and share a
common bus system.
Key components: Explain all the key components in details (1 marks each)
1. Central Processing Unit (CPU) – Executes instructions.
2. Memory Unit – Stores both data and instructions.
3. Control Unit – Directs operations of the processor.
4. Arithmetic Logic Unit (ALU) – Performs calculations and logical operations.
5. Input/Output Devices – Facilitate communication with the external environment.
Ans 1.b (5 marks, 2+3)
The Object-Oriented Data Model is based on a collection of objects, similar to the Entity-Relationship
(E-R) model, but with deeper structure and behavior. Each object contains:
• Instance variables (data)
• Methods (code that operates on the data)
Objects can be nested to any depth and are grouped into classes that define their structure and behavior.
Communication between objects occurs through method invocation, known as sending messages. Each
object has a unique identity, even if it contains the same values as another object.
Advantages of Object-Oriented Data Model (any 3x0.5)
1. Handles a wide variety of complex data types
********** 1 **********
--- page 2 ---
2. Integrates object-oriented programming with database technology
3. Enhances productivity and modularity
4. Improves data access and abstraction
Disadvantages of Object-Oriented Data Model (any 3x0.5)
1. Lacks a precise formal definition
2. Can be difficult to maintain
3. Not suitable for all types of applications
Ans 1.c (5 marks, 1x5, any 5)
Operating System (OS) Services explain in detailed any 5
1. Program Execution
o Loads and executes programs
o Allows debugging
2. I/O Operation
o Handles all read and write operations
o May involve files or I/O devices like printers
3. File System Manipulation
o Allows reading/writing of files
o Supports file creation and deletion
4. Communication
o Enables processes to communicate with each other
5. Error Detection
o Detects errors in CPU, hardware, instructions, and devices
6. Resource Allocation
o Manages system resources for optimal utilization
7. Security/Protection
o Prevents unauthorized access
o Protects the system from imposters
8. Accounting
o Tracks user activity and system usage
o Generates statistics and billing information
Ans 1.d (5 marks, 1x5, any 5)
Explain any 5 out of it. Advantages of Cloud Computing
o Lower computer costs
o Improved performance
********** 2 **********
--- page 3 ---
o Reduced software costs
o Instant software updates
o Improved document format compatibility
o Unlimited storage capacity
o Increased data reliability
o Universal document access
o Latest version availability
o Easier group collaboration
o Device independence
Disadvantages of Cloud Computing
o Requires a constant Internet connection
o Does not work well with low-speed connections
o Features might be limited
o Can be slow
o Stored data can be lost
o Stored data might not be secure
Ans 2.a (10 marks, 2x5)
Define SECONDARY STORAGE DEVICE then explain any 4 from following
o Hard Disk
o Floppy Disk
o Compact Disk
o Tape Drives
o DLT (Digital Linear Tapes)
o DAT (Digital Audio Tape)
o Micro Vault USB Storage Media
Ans 2.b (10 marks, 2+2+3+3)
(10101111)₂ to Base 10
Binary to Decimal:
(10101111) = 1×2^7 + 0×2^6 + 1×2^5 + 0×2^4 + 1×2^3 + 1×2^2 + 1×2^1 +1×2^0
=128+0+32+0+8+4+2+1=175
(178)₁₀ to Base 2
Decimal to Binary:
Divide 178 by 2 repeatedly → remainders (bottom-up):
178 =10110010
(110101)₂ to Gray Code
Binary: 1 1 0 1 0 1
Gray Code:
********** 3 **********
--- page 4 ---
•   First bit = 1
• 1⊕1 = 0
• 1⊕0 = 1
• 0⊕1 = 1
• 1⊕0 = 1
• 0⊕1 = 1
So:
(110101)2→101111 (Gray Code)
(2C9)₁₆ to Base 8
Step 1: Hex to Binary
• 2 → 0010
• C → 1100
• 9 → 1001
→ Binary: 001011001001
Step 2: Group into 3-bit chunks
→ 001 011 001 001 → Octal:
• 001 → 1
• 011 → 3
• 001 → 1
• 001 → 1
So:
(2C9)16 = 13118
Ans 3.a (10 marks, 2x2.5)
Database Language
• A DBMS has appropriate languages and interfaces to express database queries and updates.
• Database languages can be used to read, store, and update the data in the database.
Explain Types of DBMS Languages in details:
1. DDL – Data Definition Language
2. DCL – Data Control Language
3. DML – Data Manipulation Language
4. TCL – Transaction Control Language
Ans 3.b (10 marks, )
********** 4 **********
--- page 5 ---
Step 1: Take two input strings str1 and str2.
Step 2: If the lengths of str1 and str2 are not equal, return False (not anagrams).
Step 3: Create two frequency maps (or character count dictionaries) for both strings.
Step 4: Compare the two frequency maps:
•   If they are equal, return True (strings are anagrams).
•   Otherwise, return False.
function areAnagrams(str1, str2):
if length(str1) ≠ length(str2):
return False
count1 = frequencyMap(str1)
count2 = frequencyMap(str2)
if count1 == count2:
return True
else:
return False
function frequencyMap(s):
map = empty dictionary
for each character c in s:
if c in map:
map[c] += 1
else:
map[c] = 1
return map
Ans 4.a (10 marks, 2x5)
Scenario: Multiple Processes in Different States.
An explanation of the different states of a process as shown in a typical Job and Process Status Diagram in
operating systems:
********** 5 **********
--- page 6 ---
• New
• Ready
• Running
• Waiting (Blocked)
• Terminated (Exit)
• Suspended (Optional)
Ans 4.b (10 marks, any 5x2)
Multiprogramming   Multi-tasking
It uses multiple tasks for the task allocation within the
It includes the single CPU to execute the
same CPU, allowing it to manage and execute several
program.
operations concurrently.
Concept of Context Switching and Time Sharing is
Concept of Context Switching is used.
used.
In multiprogrammed system, the   The processor is typically used in time sharing mode.
operating system simply switches to, and   Switching happens when either allowed time expires
executes, another job when current job   or where there other reason for current process needs
needs to wait.   to wait (example process needs to do IO).
Multi-programming increases CPU   In multi-tasking also increases CPU utilization, it also
utilization by organizing jobs .   increases responsiveness.
The idea is to reduce the CPU idle time   The idea is to further extend the CPU Utilization
for as long as possible.   concept by increasing responsiveness Time Sharing.
It uses job scheduling algorithms so that
Time sharing mechanism is used so that multiple tasks
more than one program can run at the
can run at the same time.
same time.
In community edition, personalized   Promotions, personalized shopping experiences can be
shopping experiences is not created.   displayed in enterprise edition products.
Ans 5.a (10 marks, )
Header fields explain all
a. Source Port Address
b. Destination Port Address
c. Sequence Number
********** 6 **********
--- page 7 ---
d. Acknowledgement Number
e. Header Length (HLEN)
f. Control flags
o URG: Urgent pointer is valid
o ACK: Acknowledgement number is valid( used in case of cumulative acknowledgement)
o PSH: Request for push
o RST: Reset the connection
o SYN: Synchronize sequence numbers
o FIN: Terminate the connection
g. Window size
h. Checksum
i. Urgent pointer
Ans 5.b (10 marks, 2+3+5)
Introduction to Data-in-Motion
• Data in motion is data that is being transmitted over a network.
•   It refers to data in transit, such as:
o Data exiting the network via email, web, or other Internet protocols.
o Data being manipulated by an application.
• The collection process for data in motion is similar to that of data at rest, but the key difference is:
o Analytics occur in real-time as the event happens.
Attacks on Data-in-Motion
• Major threats:
o Interception – unauthorized access during transmission.
o Alteration – tampering with data in transit.
•   Attackers don’t need physical access to the device; they only need to be along the transmission
path.
Explain Preventive Measures
• Encrypt network sessions for secure transmission.
• Use encryption tunnels to protect data paths.
• Recommended technologies:
• VPN (Virtual Private Network)
• SSH (Secure Shell)
• AES (Advanced Encryption Standard)
• SSL (Secure Socket Layer)
• GnuPG (Gnu Privacy Guard)
Ans 6.a (10 marks, 2.5x4)
Definition of Portability
•   Portability is the ability to run components or systems written for one environment in other software
and hardware environments.
********** 7 **********
--- page 8 ---
•   Illustrated using Rackspace and Amazon Web Services (AWS) with binary code representing data
transfer.
• Purpose: To mitigate risk and increase flexibility.
Categories of Cloud Portability
1. Data Portability
o Movement of data components across different applications.
2. Application Portability
o Transfer of application components across:
▪ Cloud PaaS services
▪   Traditional computing platforms
3. Platform Portability
o Movement of platform components across:
▪ Cloud IaaS services
▪ Non-cloud infrastructure (platform source portability)
▪ Bundles with applications and data (machine image portability)
Ans 6.b (10 marks, any 5x2)
Category   AWS   Microsoft Azure   Google Cloud
Platform
Compute   EC2, Lambda   Virtual Machines,   Compute Engine,
Azure Functions   Cloud Functions
Storage   S3, EBS   Blob Storage, Disk   Cloud Storage,
Storage   Persistent Disks
Database   RDS, DynamoDB   Azure SQL   Cloud SQL,
Database, Cosmos   Firestore, Bigtable
DB
AI/ML   SageMaker   Azure Machine   Vertex AI,
Learning   TensorFlow
Networking   VPC, CloudFront   Virtual Network,   VPC, Cloud CDN
Azure CDN
DevOps Tools   CodePipeline,   Azure DevOps,   Cloud Build,
CloudFormation   ARM Templates   Deployment
Manager
Security   IAM, KMS, Shield   Azure Active   IAM, Cloud
Directory, Security   Identity, Security
Center   Command Center
Strengths   Broadest service   Microsoft   ML & analytics,
range, global reach   integration, hybrid   competitive pricing
cloud
Ans 7.a (10 marks, 2+4+4)
********** 8 **********
--- page 9 ---
Reinforcement Learning is a type of machine learning where an agent learns to make decisions by
interacting with an environment. It receives rewards or penalties based on its actions and aims to
maximize cumulative rewards over time.
Working Principles of RL
1. Agent: The learner or decision-maker.
2. Environment: Where the agent operates.
3. State: Current situation of the agent.
4. Action: Choices the agent can make.
5. Reward: Feedback from the environment after an action.
The agent uses a trial-and-error approach and learns a policy (strategy) to choose actions that yield the
highest rewards.
Applications of Reinforcement Learning
•   Robotics: Training robots to walk, grasp, or navigate.
• Game Playing: AI agents mastering games like chess, Go, or video games.
• Autonomous Vehicles: Learning to drive safely in dynamic environments.
• Finance: Portfolio management and trading strategies.
• Healthcare: Personalized treatment planning and drug discovery.
• Recommendation Systems: Adapting suggestions based on user behavior.
Ans 7.b (10 marks, 2.5x4)
Cloud computing significantly enhances the development and deployment of machine learning (ML) models
by providing scalable infrastructure, vast storage, and specialized ML services. It enables faster
experimentation, collaboration, and deployment without the need for expensive hardware.
1. Scalability (3 Marks)
• Cloud platforms offer on-demand access to high-performance computing resources (CPUs, GPUs,
TPUs).
•   Automatically scale up or down based on workload.
• Supports training of large models and parallel processing efficiently.
2. Storage (2 Marks)
• ML projects require handling large datasets (images, logs, text).
• Cloud services like Amazon S3, Azure Blob Storage, and Google Cloud Storage provide secure,
scalable, and cost-effective storage.
• Enables data sharing, versioning, and remote access across teams.
3. Machine Learning Services (3 Marks)
********** 9 **********
--- page 10 ---
• Cloud providers offer end-to-end ML platforms:
o AWS SageMaker
o Azure Machine Learning
o Google Vertex AI
• These platforms support:
o Data preprocessing
o Model training and hyperparameter tuning
o Deployment as APIs
o Monitoring and retraining
4. Real-World Impact (2 Mark)
• Enables startups and enterprises to build and deploy ML models without physical infrastructure.
•   Facilitates collaboration, continuous integration, and real-time inference.
•   Accelerates innovation in sectors like healthcare, finance, retail, and autonomous systems.
********** 10 **********
````
