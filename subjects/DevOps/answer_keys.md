# DevOps: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 8 · Answer key · paper b358a546a7e8

- Departments: Data Science
- Programmes: MBATech DS 7052
- Source: `02_Question_Papers/2025/Sem_08/Final-Exam/MBATech_DS_7052/DevOps/ANS_DevOps(702DB0E015)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 12 May 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF BUSINESS ADMINISTRATION IN TECHNOLOGY
MANAGEMENT (DATA SCIENCE)
Year: IV/Semester VIII(Exam Year: 2025-2026)
Subject: DevOps
Date: 12 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of the remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. All questions carry equal marks.
Q1
Answer briefly:   [20]
a.
List the different possible cases for Bottlenecks in CI/CD
CO-3
SO-1   [5]
BL- 1
.
b.   What are the principles of agile methods in software development?
CO-1
SO-2   Agile methods in software development are guided by several   [5]
BL- 2   key principles that prioritize flexibility, collaboration, and
********** 1 **********

[Text in pictures on this page, read by OCR]
Possible Bottlenecks in CI/CD Pipeline

Bottleneck Description Possible Solution

Slow Builds Long build times delay Optimize build tools, use caching, and
deployments. parallelize builds.

Flaky Tests Unstable tests cause false failures. Improve test reliability and use test retries.

Manual Approvals Delays due to human intervention. Automate approvals where possible.

Limited Infrastructure Inadequate resources slow down Use cloud-based scalable infrastructure.
pipelines.

Inefficient Code Merges —_ Frequent merge conflicts slow Use feature flags and small, frequent merges.
integration.

Security Scans Delays Security checks slow down Integrate lightweight, automated security
deployment. scans.

Logging & Monitoring Lack of insights makes debugging —_ Implement centralized logging and proactive
Gaps slow. monitoring.
--- page 2 ---
customer value. The Agile Manifesto outlines the core
principles of Agile development, which include:
1. Customer Satisfaction Through Continuous Delivery:
• Agile values delivering working software
frequently to provide value to customers sooner
and gather feedback.
2. Accommodate Changing Requirements:
• Agile embraces changing customer needs and
requirements, allowing for flexibility in project
scope and priorities.
3. Frequent Delivery of Working Software:
• Agile promotes delivering small, incremental
releases of software to ensure regular progress
and immediate value to the customer.
4. Collaboration Between Developers and Business
Stakeholders:
• Agile encourages close collaboration between
development teams and business stakeholders to
ensure alignment with customer needs.
5. Build Projects Around Motivated Individuals:
• Agile emphasizes building teams of motivated,
self-organizing individuals and trusting them to
make decisions.
6. Face-to-Face Communication:
• Agile values face-to-face communication as the
most effective means of conveying information
within the team.
7. Working Software as the Primary Measure of
Progress:
• Agile relies on the delivery of functioning software
as the primary indicator of project progress.
8. Sustainable Development:
• Agile promotes a sustainable pace of work,
preventing team burnout and ensuring long-term
productivity.
9. Technical Excellence and Good Design:
• Agile emphasizes the importance of high-quality
code and continuous improvement of
development practices.
********** 2 **********
--- page 3 ---
10.   Simplicity:
• Agile values simplicity in both software design and
development processes.
11.   Self-Organizing Teams:
• Agile encourages self-organizing teams that make
decisions about how they work and organize their
tasks.
12.   Reflection and Adaptation:
• Agile teams regularly reflect on their work and
adapt their processes to improve continuously.
These Agile principles foster a dynamic, customer-centric, and
iterative approach to software development, enabling teams
to respond effectively to changing requirements and deliver
valuable software.
c.   Discuss the Pull Request Model in source code management
CO-2
SO-2   [5]
BL-1
d
CO-3
SO-2   [5]
BL-1
********** 3 **********

[Text in pictures on this page, read by OCR]
Pull Request (PR) Model in Source Code Management

A Pull Request (PR) is a process in Git-based workflows where developers propose changes to a

repository. It enables code review, collaboration, and version control before merging changes.

Step Description

1. Fork & Clone Developer creates a copy of the repository and clones it locally.

2. Create a Branch Anew feature branch is created for changes ( git checkout -b feature-branch ).
3. Make Changes & Code is modified and committed with meaningful messages ( git commit -m
Commit “Feature update" ).

4. Push to Remote Changes are pushed to the remote repo ( git push origin feature-branch ).

5. Open a Pull Request Developer submits a PR for review in platforms like GitHub, GitLab, or Bitbucket.
6. Code Review & Reviewers provide feedback, request changes, or approve the PR.

Discussion

7. Merge the PR Once approved, the branch is merged into the main branch ( git merge ).

8. Delete the Branch The feature branch is deleted to keep the repo clean ( git branch -d feature-

branch ).

Short Notes on Ansible

Aspect Description

What is Ansible? An open-source automation tool used for configuration management, application

deployment, and orchestration.

Key Features Agentless, uses YAML-based Playbooks, idempotent (ensures consistency), and supports

multi-tier deployments.
How it Works? Uses SSH for remote execution and inventory files to define managed hosts.

Core Components _Playbooks (automation scripts), Modules (pre-built tasks), Roles (structured Playbooks).

Common Use Server provisioning, Cl/CD automation, cloud configuration, security hardening.
Cases
Basic Command ansible all -m ping (tests connectivity), ansible-playbook playbook.yml (runs a

ee
--- page 4 ---
a   Describe various components that constitute the DevOps architecture with
a neat diagram
1. Source Code Repository:
• Central repository (e.g., Git) for storing application
code and configurations.
2. Build Automation:
• Continuous Integration (CI) tools (e.g., Jenkins,
Travis CI) for automating code compilation,
testing, and artifact generation.
3. Containerization:
• Docker for packaging applications and their
dependencies into containers for consistency and
portability.
4. Artifact Repository:
• Repository (e.g., Nexus, JFrog Artifactory) to store
and manage artifacts, including container images
and software packages.
5. Configuration Management:
Q2   • Tools (e.g., Ansible, Puppet, Chef) for automating
server configuration and ensuring consistency.
CO-1   [10]
SO-1   6. Continuous Deployment:
BL-2   • Continuous Deployment (CD) tools (e.g., Jenkins,
Spinnaker) for automating application deployment
to various environments.
7. Infrastructure as Code:
• Tools like Terraform and CloudFormation for
defining infrastructure in code, making it
reproducible.
8. Monitoring and Logging:
• Monitoring and logging tools (e.g., Prometheus,
ELK stack) to track application performance, detect
issues, and provide insights.
9. Orchestration:
• Container orchestration platforms (e.g.,
Kubernetes) for managing containerized
applications at scale.
10.   Collaboration and Communication:
• Collaboration tools (e.g., Slack, Microsoft Teams)
and issue tracking (e.g., Jira) for team
communication and task management.
********** 4 **********
--- page 5 ---
11.   Security and Compliance:
• Security scanning tools (e.g., SonarQube) and
compliance checks to ensure code quality and
security.
12.   Feedback and Continuous Improvement:
• Continuous feedback loops and retrospectives for
ongoing process improvement.
These components work together to streamline the software
development and delivery process in a DevOps architecture,
emphasizing automation, collaboration, and a culture of
continuous improvement.
b
Describe various components of Kubernetes architecture with a neat
diagram.
1. Master Node:
• API Server: Exposes the Kubernetes API.
• Controller Manager: Ensures the desired state of the
cluster.
• Scheduler: Assigns workloads to worker nodes.
• etcd: Consistent and distributed key-value store for
cluster data.
Q2   2. Worker Nodes:
CO-3   • Kubelet: Ensures containers are running.   [10]
SO-3   • Kube Proxy: Maintains network rules.
BL-3   • Container Runtime: Manages containerization (e.g.,
Docker).
3. Add-Ons:
• DNS: Provides DNS-based service discovery.
• Dashboard: Web-based UI for cluster management.
• Ingress Controller: Manages external access to services.
• CNI: Plugin for networking within the cluster.
• Storage Plugin: Enables dynamic storage provisioning.
These components collectively enable the deployment, scaling, and
management of containerized applications in a Kubernetes cluster
Q3   a   [10]
********** 5 **********
--- page 6 ---
CO-2   What is a DevOps CICD pipeline? Explain various stages involved in the
SO-2   DevOps pipeline.
BL-3
A DevOps CI/CD (Continuous Integration/Continuous
Deployment) pipeline is an automated workflow that helps
organizations streamline the software development and
delivery process. It consists of several stages, each serving a
specific purpose:
1. Code Integration:
• Developers regularly integrate their code into a
shared repository.
• Automated tests are run to identify issues early.
2. Build and Compile:
• The code is compiled and built into executable
artifacts.
• Dependency management is handled, and the
build process is automated.
3. Automated Testing:
• Comprehensive testing, including unit tests,
integration tests, and end-to-end tests, is
performed automatically.
• Testing ensures the code's correctness and
identifies bugs.
4. Artifact Generation:
• Build artifacts, such as executable files and
libraries, are generated and stored.
• These artifacts are used for deployment.
5. Deployment to Staging:
• The application is deployed to a staging
environment that closely resembles the
production environment.
• Testing is conducted in a real-world environment
to ensure compatibility.
6. User Acceptance Testing (UAT):
• Stakeholders or users test the application in the
staging environment.
• Feedback is collected and issues are addressed.
7. Deployment to Production:
• Once testing is successful, the application is
deployed to the production environment.
********** 6 **********
--- page 7 ---
• Rollout strategies, such as blue-green or canary
deployments, may be used to minimize downtime.
8. Monitoring and Feedback:
• Continuous monitoring and feedback collection
are critical.
• Performance, errors, and user feedback are
monitored in the production environment.
9. Continuous Improvement:
• Feedback and monitoring data drive ongoing
improvements.
• The pipeline is iteratively enhanced to optimize
the development and delivery process.
A well-structured DevOps CI/CD pipeline automates the
software development lifecycle, accelerates delivery, reduces
errors, and supports a culture of continuous improvement.
b
Write short notes on the following terminology related to
i. Docker Image
ii. Docker Container
iii. Dockerfile
iv. Docker Hub
Docker Image:
Q3
CO-3   • A lightweight, standalone, executable package that includes
SO-1   application code, runtime, libraries, and system tools.
• Used as a blueprint to create Docker containers.
BL-2
ii. Docker Container:
• An instance of a Docker image that runs as a standalone,
isolated environment.
• Provides consistent and reproducible application execution.
iii. Dockerfile:
• A text file that contains instructions for building a Docker
image.
********** 7 **********
--- page 8 ---
• Defines the application's environment, dependencies, and
setup.
iv. Docker Hub:
• A cloud-based registry service provided by Docker for storing,
sharing, and distributing Docker images.
• Offers a vast repository of public and private Docker images for
various applications and services.
a
Write short notes on the following terminology related to
i. Infrastructure as a code
ii. Kubernetes POD
iii. Microservices
V. Orchestration
i. Infrastructure as Code (IaC):
•   Practice of managing and provisioning infrastructure using
code and automation.
• Enables consistent and reproducible infrastructure
Q4   deployments.
CO-3   ii. Kubernetes POD:   [10]
SO-2
BL-1
• The smallest deployable unit in Kubernetes.
• Contains one or more containers that share network and
storage resources.
iii. Microservices:
•   Architectural approach where a large application is broken
down into small, independent services.
• Each service focuses on a specific function and communicates
through APIs.
iv. Orchestration:
• The automated coordination and management of various
components or services in a system.
********** 8 **********
--- page 9 ---
• Commonly used in cloud computing and container
orchestration platforms like Kubernetes.
• Ensures optimal resource utilization and scalability.
b   What are the parameters to be measured at every stage of DevOps
Maturity Model? Explain.
1. Stage 0 - Chaos:
• Culture: Lack of collaboration and
communication.
• Manual Processes: No automation in place.
• Infrastructure: Manual, untracked changes.
2. Stage 1 - Reactive:
• Culture: Acknowledgment of collaboration's
importance.
• Some Automation: Basic CI/CD tools.
• Infrastructure: Limited automation.
3. Stage 2 - Repeatable:
• Culture: Defined roles and collaboration.
• Continuous Integration: Automated testing.
Q4   • Configuration Management: Some automation.
4. Stage 3 - Defined:
CO-2; SO-3;   • Culture: Collaboration embedded.   [10]
BL-3   • Full CI/CD: Automated deployment and
monitoring.
• Infrastructure: Infrastructure as Code (IaC)
adoption.
5. Stage 4 - Managed:
• Culture: Collaboration as a norm.
• Data-Driven Decisions: Extensive metrics and
analytics.
• Full IaC: Automated, versioned infrastructure.
6. Stage 5 - Optimizing:
• Culture: Continuous improvement mindset.
• Advanced CI/CD: Experimentation and canary
deployments.
• Immutable Infrastructure: Dynamic, self-healing.
Measuring these parameters at each stage helps assess an
organization's progress in adopting DevOps principles, from
********** 9 **********
--- page 10 ---
initial chaos to a highly optimized, efficient, and collaborative
environment.
a   Write short notes on Jenkins. What are the useful plugins in Jenkin?
Explain?
Jenkins:
• Jenkins is an open-source automation server that
supports building, deploying, and automating projects.
•   It offers an extensible plugin architecture and a wide
range of plugins to support various development,
deployment, and automation tasks.
• Jenkins provides continuous integration (CI) and
continuous delivery (CD) capabilities, allowing for
automated testing and deployment of applications.
Useful Jenkins Plugins:
1. Pipeline:
Q5   • Allows defining build and deployment pipelines as
CO-2;   code using the Jenkinsfile.
• Provides flexibility and reusability in defining   [10]
SO-2;   complex build processes.
BL-2   2. GitHub Integration:
• Integrates Jenkins with GitHub for automatic
builds and notifications.
• Supports GitHub webhooks and pull request
builds.
3. Docker:
• Facilitates building and managing Docker
containers within Jenkins.
• Useful for containerized application deployment.
4. AWS Elastic Beanstalk:
• Streamlines the deployment of applications to
AWS Elastic Beanstalk.
• Enables CI/CD for AWS cloud deployments.
5. Blue Ocean:
• Offers a modern, user-friendly UI for Jenkins,
enhancing the visualization of pipelines and
builds.
********** 10 **********
--- page 11 ---
6. Slack Notification:
• Sends build notifications and reports to Slack
channels.
• Enhances team communication and collaboration.
7. JUnit:
• Parses JUnit test results for reporting and trend
analysis.
• Essential for tracking test results and identifying
regressions.
8. SonarQube:
• Integrates Jenkins with SonarQube for code
quality analysis and reporting.
• Aids in maintaining code quality standards.
9. Artifactory:
• Enables artifact management, distribution, and
resolution.
• Supports integration with JFrog Artifactory for
artifact storage.
These plugins extend Jenkins' capabilities, making it a versatile
and powerful tool for automating and streamlining various
aspects of the software development and deployment
process.
b   What is cloud computing? Explain the role of cloud computing in
implementing the DevOps Process.
Cloud Computing:
• Cloud computing is the delivery of computing services (e.g., servers,
storage, databases, networking, software, analytics, and intelligence)
Q5   over the internet, often referred to as "the cloud."
• Cloud providers, such as AWS, Azure, and Google Cloud, offer on-
CO-3;   demand resources and services, eliminating the need for   [10]
SO-2;   organizations to own and maintain physical hardware.
BL-2
Role of Cloud Computing in Implementing DevOps:
1. Scalability:
• Cloud platforms provide elastic resources, enabling DevOps
teams to scale infrastructure up or down based on workload
requirements.
• This supports the dynamic nature of DevOps practices, where
applications can experience varying workloads and demand.
********** 11 **********
--- page 12 ---
2. Automation:
• Cloud services offer tools for automating infrastructure
provisioning and management. DevOps heavily relies on
automation for deployment, configuration, and scaling.
•   Infrastructure as Code (IaC) is a key DevOps practice, and
cloud services support the IaC approach.
3. Resource Flexibility:
• Cloud platforms offer a diverse range of services and
resources, such as virtual machines, containers, serverless
computing, and databases.
• DevOps teams can choose the right resources for specific
application needs and employ various services for different
stages of the DevOps pipeline.
4. Collaboration and Remote Access:
• Cloud platforms facilitate remote access and collaboration,
allowing DevOps teams to work from anywhere, enhancing
team collaboration, and ensuring accessibility to resources.
5. DevOps Tooling:
• Cloud providers offer various DevOps-specific tools,
including CI/CD platforms, container orchestration,
monitoring, and management services.
• These tools streamline the DevOps process and enhance
application lifecycle management.
6. Security and Compliance:
• Cloud providers invest in security and compliance measures,
and they often provide features like identity and access
management (IAM), encryption, and compliance
certifications.
• DevOps teams can leverage these features to ensure the
security and compliance of their applications.
Cloud computing plays a crucial role in DevOps by providing the
infrastructure and services needed to implement DevOps practices
effectively. It enables scalability, automation, flexibility, and collaboration,
while also enhancing security and compliance in the software development
and deployment process.
a   Explain the significance of source code control in project management, its
history, and its role in version control and collaboration
Significance of Source Code Control in Project Management:
Q6   • History: Source code control, or version control, has
been used in software development for decades. Early
CO-1   [10]
SO-1   systems like SCCS and RCS evolved into modern
BL-2   distributed version control systems like Git and SVN.
• Role in Version Control: Source code control tracks
changes to code, ensuring versioning, traceability, and
the ability to roll back to previous states. This is crucial
for reproducibility, debugging, and compliance.
********** 12 **********
--- page 13 ---
• Role in Collaboration: Source code control enables
collaboration among developers. Multiple team
members can work on code simultaneously, merge
changes, and resolve conflicts, ensuring efficient
teamwork and code quality.
• Branching and Forking: It allows for branching, which is
essential for concurrent development, experimentation,
and isolation of features. Forking enables community-
driven open-source development.
• Conflict Resolution: Provides tools for conflict resolution,
ensuring smooth integration of changes made by
different developers.
• Continuous Integration: Integrates with CI/CD pipelines,
automating the testing and deployment of code
changes.
• History and Annotations: It maintains a detailed history
of code changes and annotates code with contributors,
making it easy to trace who made which changes and
why.
• Rollback and Recovery: Offers the ability to roll back to
previous code states, facilitating recovery from errors or
unwanted changes.
Source code control is an integral part of project
management, supporting the software development lifecycle,
improving collaboration, and ensuring the integrity of code
throughout its evolution.
b
What is the DevOps maturity model? Explain various phases of DevOps
maturity model with a neat sketch.
The DevOps Maturity Model assesses an organization's maturity in adopting
Q6   DevOps practices, with stages ranging from low maturity to high maturity.
Here are the various phases of the DevOps maturity model:
CO-2   [10]
SO-2   1. Stage 0 - Chaos:
BL-2   • Culture: Minimal collaboration and communication.
• Automation: Lack of automation in development and
deployment.
•   Infrastructure: Manual, untracked changes.
2. Stage 1 - Reactive:
• Culture: Acknowledgment of the need for collaboration.
• Automation: Basic Continuous Integration (CI) tools.
********** 13 **********
--- page 14 ---
•   Infrastructure: Limited automation; manual changes.
3. Stage 2 - Repeatable:
• Culture: Roles and responsibilities defined, limited
collaboration.
• Automation: Adoption of CI/CD tools; automated testing.
•   Infrastructure: Some automation, limited version control.
4. Stage 3 - Defined:
• Culture: Collaboration integrated into processes.
• Automation: Full CI/CD adoption, automated deployment
and monitoring.
•   Infrastructure: Automation through Infrastructure as Code
(IaC) is a norm.
5. Stage 4 - Managed:
• Culture: Collaboration as a standard practice.
• Automation: Extensive metrics and analytics; data-driven
decisions.
•   Infrastructure: Infrastructure is managed with full IaC;
dynamic and scalable.
6. Stage 5 - Optimizing:
• Culture: Continuous improvement mindset is prevalent.
• Automation: Advanced CI/CD practices, experimentation,
and canary deployments.
•   Infrastructure: Immutable infrastructure, self-healing,
dynamic scaling.
Each stage represents the organization's level of maturity in areas like
culture, automation, and infrastructure. As organizations progress through
these stages, they become more efficient, collaborative, and capable of
delivering software with higher quality and agility.
a
Describe a Docker container’s lifecycle with commands.
The lifecycle of a Docker container involves creating, starting,
stopping, and managing containers. Here are some essential
Q7   commands for each stage:
CO-3   1. Create a Container:   [10]
SO-2
BL-4   •   docker run -d --name my-container my-image: Creates and runs
a container from an image with the name "my-
container."
2. Start a Container:
•   docker start my-container: Starts a previously created
container.
3. Stop a Container:
********** 14 **********
--- page 15 ---
•   docker stop my-container: Gracefully stops a running
container.
•   docker kill my-container: Forces a container to stop
immediately.
4. List Containers:
•   docker ps: Lists running containers.
•   docker ps -a: Lists all containers (including stopped
ones).
5. Remove a Container:
•   docker rm my-container: Removes a stopped container.
•   docker rm -f my-container: Removes a running container
forcibly.
6. Inspect a Container:
•   docker inspect my-container: Provides detailed
information about a container's configuration and
status.
7. Pause and Unpause a Container:
•   docker pause my-container: Pauses a running container.
•   docker unpause my-container: Unpauses a paused
container.
Managing the lifecycle of Docker containers using these
commands allows for efficient container orchestration and
resource management.
b   Execute the below scenario with the git command:
There are 3 files created in the root project directory – {your_name}.txt
and {your sur_name}.txt & {your_sap_id}.txt. Write git command to
Q7   execute the below steps.
CO-1   1: Configure your user in Git Client.   [10]
SO-2   2: Get the latest pull from Remote.
BL-3   3: Commit {your_name}.txt with message “{your name} committing this
change for term test 1”
4: Discard {your sir_name}.txt from working directory.
5: Push {your_sap_id}.txt to your remote repo.
********** 15 **********
````
