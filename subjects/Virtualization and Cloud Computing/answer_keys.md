# Virtualization and Cloud Computing: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper f7adb45af807

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7057/Virtualization and Cloud Computing/ANS_Virtualization and Cloud Computing(702DB0E008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 08 May 2026
- Text: mixed (7 pages), mean OCR confidence 71.7

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Virtualization and Cloud Computing
Date: 08 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 7 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Section-A
Q1
CO-1   A.   Explain full   virtualization,   para-virtualization,   and   OS-level   [05]
BL-2   virtualization and identify which is most suitable for scalable cloud environments.
Answer:
• FullVirtualization:
Complete simulation of hardware allowing multiple OS to run
independently using hypervisor (1M)
• Para-Virtualization:
Guest OS is aware of virtualization and interacts efficiently with
hypervisor (1M)
• OS-LevelVirtualization:
Multiple isolated containers share same OS kernel (1M)
• Comparison:
Full = flexible, Para = efficient, OS-level = lightweight (1M)
• Conclusion:
OS-level virtualization is most suitable for scalable cloud due to efficiency
(1M)
********** 1 **********
--- page 2 ---
CO-3   B.   Explain IAM Users, Groups, and Roles and how they help in managing   [05]
BL-2   permissions efficiently.
Answer:
• Users: Individual identities for authentication (1M)
• Groups: Collection of users with common permissions (1M)
• Roles: Temporary access without credentials (1M)
• Working: Users assigned to groups, roles assumed when needed (1M)
• Benefit: Simplifies permission management and enhances security (1M)
CO-3   C.   Explain how Elastic Load Balancing (ELB) distributes traffic and ensures high   [05]
BL-2   availability.
Answer:
• ELB distributes incoming requests across multiple servers (1M)
• Uses health checks to monitor instance status (1M)
• Automatically redirects traffic from failed instances (1M)
• Improves availability and load distribution (1M)
• Example: Handling traffic spikes in web apps (1M)
CO-2   D.   Explain different S3 storage classes and recommend the most suitable option.   [05]
BL-2   Answer:
• Standard: High availability, frequent access (1M)
• Standard-IA: Lower cost for infrequent access (1M)
• Glacier: Low-cost archival storage (1M)
• Comparison: Cost vs access speed trade-off (1M)
• Recommendation: Glacier for rarely accessed data (1M)
Section- B
Q2
CO-1 A   A networking team is designing a communication system. Explain the OSI model   [10]
BL-2   layers and compare them with   the TCP/IP model,   highlighting   their
functionalities.
Answer:
• OSI Model: 7 layers including physical to application (3M)
• TCP/IP Model: 4 layers (Network Interface, Internet, Transport,
Application) (3M)
• Mapping: OSI layers combined into TCP/IP layers (2M)
•   Difference: OSI theoretical, TCP/IP practical (1M)
********** 2 **********
--- page 3 ---
• Example: HTTP in application layer (1M)
CO-1 B   A company is planning cloud adoption. Explain different cloud deployment   [10]
BL-2   models (Public, Private, Hybrid) and justify their use with examples.
Answer:
•   Public Cloud: Shared infrastructure, scalable (2M)
•   Private Cloud: Dedicated, secure environment (2M)
• Hybrid Cloud: Combination of both (2M)
• Comparison: Cost, control, flexibility (2M)
• Use Case: Hybrid for sensitive + scalable workloads (2M)
Q3
CO-2 A   A financial organization needs strict access control. Explain IAM policies   [10]
BL-3   (Managed and Inline) and how they are used to secure AWS resources.
Answer:
•   Policies define permissions using JSON (2M)
• Managed Policies: Reusable and centralized (2M)
•   Inline Policies: Attached to specific entity (2M)
•   Structure: Effect, Action, Resource (2M)
•   Benefit: Fine-grained access control (2M)
CO-3 B   A startup wants to deploy applications with varying workloads. Explain   [10]
BL-3   the working of EC2 instances and how security groups and key pairs ensure secure
access.
Answer:
• EC2 provides virtual servers (2M)
•   Instance lifecycle management (2M)
•   Security groups control inbound/outbound traffic (2M)
• Key pairs used for secure SSH access (2M)
• Example: Web server deployment (2M)
Q4
CO-2 A   An   e-commerce   platform   must   handle   unpredictable   traffic   [10]
BL-2   efficiently. Explain different types of Elastic Load Balancers (ALB, NLB,
CLB) and their use cases.
Answer:
• ALB: Layer 7 routing (HTTP/HTTPS) (2M)
********** 3 **********
--- page 4 ---
• NLB: High performance Layer 4 (2M)
• CLB: Basic load balancing (2M)
• Comparison: performance and use case (2M)
• Example: Microservices using ALB (2M)
CO-2 B   A   company   is   selecting   a   database   solution   for   different   [10]
BL-2   applications. Compare Amazon RDS and DynamoDB based on   structure,
scalability, and use cases.
Answer:
• RDS: Relational DB, structured schema (3M)
• DynamoDB: NoSQL, flexible schema (3M)
• Comparison: SQL vs NoSQL, vertical vs horizontal scaling (2M)
• Use case: RDS for transactions, DynamoDB for high throughput (2M)
Q5
CO-2 A   A startup wants to develop an event-driven application without managing   [10]
BL-2   servers. Explain the working of AWS Lambda and discuss its advantages.
Answer:
•   Serverless compute service (2M)
•   Executes code on events (2M)
• No infrastructure management (2M)
•   Benefits: scalability and cost efficiency (2M)
• Example: Trigger on S3 upload (2M)
CO-3 B   A cloud application needs to automatically adjust resources based on   [10]
BL-3   demand. Explain   how Auto   Scaling   Groups   (ASG)   and   scaling
policies maintain performance and availability.
Answer:
• ASG maintains required number of instances (2M)
• Dynamic scaling based on metrics (2M)
•   Scheduled scaling based on time (2M)
• Improves availability and performance (2M)
• Example: Traffic-based scaling (2M)
Q6
********** 4 **********
--- page 5 ---
CO-3 A   A global application requires monitoring and performance optimization. Explain   [10]
BL-3   the role of CloudWatch and CloudTrail in monitoring and auditing AWS
resources.
Answer:
• CloudWatch monitors metrics and logs (3M)
•   CloudTrail records API activity (3M)
•   Difference: monitoring vs auditing (2M)
•   Integration for complete visibility (1M)
• Use case: security tracking (1M)
CO-3 B   A system administrator needs to control traffic flow in a VPC. Explain how   [10]
BL-3   security groups and route tables are configured to achieve this.
Answer:
To control traffic flow in a VPC, a system administrator uses Security Groups and
Route Tables, which manage access and routing of network traffic. (1M)
Security Groups act as virtual firewalls attached to instances. They control inbound
and outbound traffic based on rules such as protocol, port number, and
source/destination IP. For example, allowing HTTP (port 80) and SSH (port 22)
ensures only required traffic is permitted. Security groups are stateful, meaning
return traffic is automatically allowed. (4M)
Route Tables define how traffic is directed within the VPC. Each subnet is
associated with a route table that contains rules specifying where traffic should go.
For example, a route like 0.0.0.0/0 → Internet Gateway allows internet access for
public subnets, while private subnets may route traffic through a NAT Gateway.
(3M)
By combining both, route tables ensure traffic reaches the correct destination,
while security groups ensure only authorized traffic is allowed. This provides
secure and controlled communication within the VPC. (2M)
Q7
CO-3 A   EC2 Web Server Deployment   [10]
A startup plans to host a dynamic web application using a virtual server on Amazon
BL-3   Web Services EC2.
Answer:
********** 5 **********
--- page 6 ---
EC2 Instance Setup & Configuration
Tasks to Performed:
• Launch an EC2 instance using a suitable AMI (e.g., Amazon Linux).
•   Select an appropriate instance type (e.g., free-tier eligible).
•   Configure instance in default VPC with public subnet.
•   Create/use a key pair for secure access.
•   Configure security group to allow required inbound traffic (e.g., SSH,
HTTP).
•   Connect to the instance using SSH.
•   Install and start a web server.
•   Configure the web server to run at system boot.
Verify in Answer Sheet:
•   Step-by-step procedure for launching and configuring the EC2 instance.
• Key pair usage and SSH connection process.
•   Security group rules configured with purpose.
• Commands used for web server installation and setup.
EC2 instance launch and configuration and Proper SSH connection and key pair
management.
CO-3 B   Answer:   [05]
Webpage Deployment & Testing
BL-3   Tasks to Performed:
•   Create and deploy a sample webpage (index.html).
•   Ensure correct file permissions.
•   Webpagemustdisplay:
“Mukesh Patel School of Technology Management and Engineering”
•   Access the application using the EC2 public IP.
Verify in Answer Sheet:
•   Steps to deploy the webpage.
•   File location and permission details.
•   Public IP address used for access.
•   Steps followed to test and verify webpage accessibility.
Web server installation, configuration, and webpage deployment.
CO-3 C   Answer:   [05]
Security Configuration & Explanation
BL-3   Tasks to Performed:
•   Ensure proper security group configuration for controlled access.
Verify in Answer Sheet:
•   Explanation of configured security group rules.
•   Purpose and importance of key pairs.
• Overview of web server setup and its role in hosting applications.
********** 6 **********
--- page 7 ---
Security group configuration and documentation quality.

FIC 7 IC OHH
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 0367a0b00c83

- Departments: Data Science
- Programmes: BTech CSE DS 7057
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CSE_DS_7057/Virtualization and Cloud Computing/ANS_Virtualization and Cloud Computing(702DB0E008)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 Jul 2026
- Text: text (7 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Virtualization and Cloud Computing
Date: 04 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 7 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory. Out of remaining questions, attempt any 4 questions.
5. In all 5 questions to be attempted
6. All questions carry equal marks.
7. Assume Suitable data if necessary.
Section-A
Q1
CO-1   A.   [05]
BL-2   Explain IaaS, PaaS, and SaaS with suitable examples and suggest which
model is best for application development and deployment.
Answer:
• IaaS (Infrastructure as a Service):
Provides virtualized computing resources such as servers, storage,
and networking. User controls OS and applications.
Example: AWS EC2 (1.5M)
• PaaS (Platform as a Service):
Provides platform with OS, runtime, and development tools.
Developers focus only on application development.
Example: Google App Engine (1.5M)
• SaaS (Software as a Service):
Fully managed software delivered over internet. No control over
infrastructure.
Example: Gmail (1M)
• Conclusion:
PaaS is best for application development and deployment due to
ease of development and reduced management (1M)
********** 1 **********
--- page 2 ---
CO-3   B.   [05]
BL-2   Explain IAM Roles and temporary credentials and how they improve
security.
Answer:
• IAM Roles:
Roles define a set of permissions that can be assumed by users or
services without permanent credentials (1.5M)
• Temporary Credentials:
Generated using AWS STS, valid for limited time (1M)
• Working:
External user assumes role → gets temporary access → expires
automatically (1M)
•   Security Benefit:
No long-term credentials, reduces risk of misuse (1M)
• Use Case:
Third-party application access (0.5M)
CO-3   C.   [05]
BL-2   Explain how an Application Load Balancer (ALB) works and how it
improves application performance.
Answer:
• Works at Layer 7 (Application layer) (1M)
• Routes traffic based on URL path, host, headers (1M)
• Supports microservices architecture (0.5M)
• Improves performance by intelligent routing (1M)
• Example: /api → server1, /images → server2 (1.5M)
CO-2   D.   [05]
BL-2   Explain S3 lifecycle policies and how they help in cost optimization.
Answer:
•   Lifecycle policies automatically move data between storage
classes (1.5M)
• Example transitions: Standard → IA → Glacier (1M)
•   Deletes old data automatically (1M)
• Reduces storage cost significantly (1M)
•   Suitable for backup/archival (0.5M)
Section- B
Q2
CO-1 A   [10]
A networking company is designing a communication system for a large
BL-2
enterprise. Explain the OSI model layers and map them with the TCP/IP
model, highlighting key differences.
Answer:
• OSI Model (7 Layers):
Physical, Data Link, Network, Transport, Session, Presentation,
Application (4M)
********** 2 **********
--- page 3 ---
• TCP/IP Model (4 Layers):
Network Interface, Internet, Transport, Application (3M)
• Mapping:
OSI Application + Presentation + Session → TCP/IP Application
OSI Network → Internet layer (2M)
•   Differences:
OSI is conceptual; TCP/IP is practical and widely used (1M)
CO-1 B   [10]
A multinational company is planning to adopt cloud infrastructure.
BL-2
Compare Public, Private, and Hybrid cloud models and recommend the
most suitable model with justification.
Answer:
•   Public Cloud: Shared resources, scalable (2.5M)
•   Private Cloud: Dedicated, secure (2.5M)
• Hybrid Cloud: Combination, flexible (2.5M)
• Recommendation: Hybrid cloud for balance of cost and
control (2.5M)
Q3
CO-2 A   [10]
A financial organization needs strict access control for different
BL-3
departments. Explain different IAM policies (Managed and Inline) and
how they are used to control access.
Answer:
•   Policies define permissions in JSON (2M)
• Managed Policies: Reusable, AWS-managed or custom (3M)
•   Inline Policies: Attached to specific user/group (2M)
•   Structure: Effect, Action, Resource (2M)
• Use: Fine-grained access control (1M)
CO-3 B   [10]
A startup wants to deploy applications with different performance needs.
BL-3
Explain different EC2 instance types and suggest suitable instances for
compute-intensive and memory-intensive applications.
Answer:
• General purpose (balanced) (2M)
• Compute optimized (high CPU) (2M)
• Memory optimized (high RAM) (2M)
•   Storage optimized (I/O intensive) (2M)
• Recommendation:
Compute apps → compute optimized, DB →
memory optimized (2M)
Q4
CO-2 A   [10]
An e-commerce platform faces unpredictable traffic loads. Explain how
BL-2
Auto Scaling Groups work with Elastic Load Balancing to maintain high
availability and scalability.
********** 3 **********
--- page 4 ---
Answer:
• ELB distributes traffic (2M)
• ASG automatically adds/removes instances (3M)
• Works together for scalability (2M)
• Maintains availability during peak load (2M)
• Example scenario (1M)
CO-2 B   [10]
BL-2   A company needs both transactional and analytical database solutions.
Compare Amazon RDS and Amazon Redshift and justify their use in
different scenarios.
Answer:
• RDS: OLTP, relational DB (3M)
•   Redshift: OLAP, data warehouse (3M)
•   Difference: transactional vs analytical (2M)
• Use case: RDS for apps, Redshift for analytics (2M)
Q5
CO-2 A   [10]
A startup wants to build a serverless application. Explain the working of
BL-2
AWS Lambda and discuss its advantages.
Answer:
•   Serverless service (2M)
•   Event-driven execution (2M)
• No server management (2M)
•   Benefits: scalability, cost efficiency (2M)
• Example: file upload triggers processing (2M)
CO-3 B   [10]
A cloud application needs to automatically scale resources based on
BL-3
demand. Explain different Auto Scaling policies (dynamic and scheduled)
with an example.
Answer:
• Dynamic scaling: based on metrics (CPU) (3M)
• Scheduled scaling: time-based (3M)
• Improves performance and cost (2M)
• Example scenario (2M)
Q6
CO-3 A   [10]
A company wants to monitor system performance and track user
BL-3
activities. Explain the role of Amazon CloudWatch and CloudTrail in
monitoring and logging.
Answer:
• CloudWatch: monitors metrics, alarms (4M)
•   CloudTrail: logs API activity (4M)
•   Difference: monitoring vs auditing (2M)
********** 4 **********
--- page 5 ---
CO-3 B   [10]
A DevOps engineer needs to design a secure network in AWS. Explain the
BL-3   step-by-step process to create and configure a VPC.
Answer: (10M for all steps)
Step 1: Create VPC
Go to AWS VPC dashboard and create a new VPC by specifying a CIDR
block (e.g., 10.0.0.0/16), which defines the IP range.
Step 2: Create Subnets
Create public and private subnets within the VPC. Public subnets allow
internet access, while private subnets are used for secure internal
resources.
Step 3: Create Internet Gateway (IGW)
Create an Internet Gateway and attach it to the VPC to enable internet
connectivity.
Step 4: Configure Route Tables
Create route tables and add routes. For public subnet, add a route
(0.0.0.0/0) pointing to the Internet Gateway.
Step 5: Configure Security Groups
Set up security groups to control inbound and outbound traffic (e.g., allow
SSH, HTTP).
Step 6: Configure Network ACLs (Optional)
Add an extra layer of security using Network Access Control Lists
Q7
CO-3 A   [10]
BL-3   Question: AWS IAM Configuration
An organization wants to securely manage access to cloud resources
using Amazon Web Services IAM.
IAM User Creation & Policy Assignment
Tasks to Perform:
• Create a new IAM user.
• Assign appropriate access type (programmatic or console access).
• Attach suitable policies (e.g., S3 read-only access).
Write in Answer Sheet:
• Step-by-step procedure for IAM user creation.
• Access type selected with justification.
********** 5 **********
--- page 6 ---
•   Policies attached and permissions granted.
• Explanation of the principle of least privilege.
Answer:
Secure Access Management in AWS using IAM (Least Privilege Principle)
An organization can securely manage access to AWS resources using IAM
(Identity and Access Management) by creating users, roles, and policies
with minimal required permissions.
a) IAM User Creation (10 Marks)
An IAM user represents an individual or application that needs access to
AWS.
Steps (AWS Management Console):
1. Go to IAM Dashboard → Users → Create User
2. Enter username (e.g., TestUser)
3. Select access type:
a. Programmatic access (for CLI/API using access keys)
b. Console access (for AWS login via browser)
4. Set password (for console access)
5. Click Next → Permissions
Policy Assignment
Policies define what actions a user can perform.
Attach Policy:
• Choose Attach existing policies directly
•   Select AmazonS3ReadOnlyAccess
Permissions Granted:
• Allows user to:
o View S3 buckets
o   List objects
o Download objects
• Does NOT allow:
o Upload, delete, or modify objects
This follows the least privilege principle by granting only read access
instead of full control.
CO-3 B   [05]
BL-3   IAM Role Creation
Tasks to Perform:
• Create an IAM role for EC2 to access S3.
• Attach appropriate policy to the role.
Write in Answer Sheet:
• Steps to create IAM role.
• Role configuration details and attached policies.
• Explanation of how roles differ from users.
• Use case of IAM role in EC2 access.
********** 6 **********
--- page 7 ---
Answer:
b) IAM Role Creation (5 Marks)
An IAM role is used to grant permissions to AWS services (like EC2)
without using credentials.
Steps:
1. Go to IAM → Roles → Create Role
2. Select Trusted Entity: AWS Service
3. Choose EC2
4. Attach policy:
a. AmazonS3ReadOnlyAccess
5. Name role (e.g., EC2-S3-Access-Role)
6. Create role
Usage:
• Attach this role to an EC2 instance
• EC2 can now securely access S3 without storing access keys
CO-3 C   [05]
BL-3   Testing & Explanation
Tasks to Perform:
•   Verify access permissions using the created user/role.
Write in Answer Sheet:
• Steps followed to verify permissions.
• Explanation of IAM user, IAM role, and policies.
• Observations on access control and security implementation.
Answer:
c) Testing and Deliverables (5 Marks)
Verify Access:
For IAM User:
• Login using IAM credentials
• Open S3:
o Can view and download files
o Cannot upload/delete files
For IAM Role:
• Launch EC2 instance with attached role
• Use AWS CLI:
aws s3 ls
o Should list buckets (read access confirmed
X----------------------------------------------------------------------------------------------------------------- X
********** 7 **********
````
