# Agile Product Development with DevOps: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 64d0e094ab9f

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIDS_7056/Agile Product Development with DevOps/ANS_Agile Product Development with DevOps(702AI0C022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Agile Product Development with DevOps
Date: 04 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. Answer to each new question to be started on a fresh page.
5. Figure in right hand side indicates full marks.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Elaborate the need of Agile Software Development.
Agile Software Development (2 Marks )and Its Need –(3 Marks)
Agile Software Development is a software development methodology that focuses on:
Flexibility
Collaboration
Customer satisfaction
It is based on the Agile Manifesto, which emphasizes:
•   Individuals and interactions over processes and tools
CO-1 ;   •   Working software over comprehensive documentation
SO-6 ;   •   Customer collaboration over contract negotiation   5
•   Responding to change over following a plan
BL-1
Need for Agile
Agile is needed because:
•   Requirements change frequently in real-world projects
•   Faster delivery is required
•   Customer feedback is essential
•   Traditional models are rigid and slow
•   It improves product quality through continuous testing and feedback
•   Agile Development Models
b.   Explain the recursive merge of git branching.
1) Definition (2 Marks)
Recursive merge is the default merge strategy used by Git when merging two
CO-1,2 ;   branches. It is mainly used when branches have diverged and may have multiple
SO- 6;   5
common ancestors. Git recursively finds a common base (merge base) and merges
BL-2,3
changes accordingly.
2) Working of Recursive Merge (2 Marks)
Git identifies the common ancestor commit of both branches.
********** 1 **********
--- page 2 ---
Compares changes from both branches with the base.
Automatically merges non-conflicting changes.
•   If conflicts occur, Git marks them for manual resolution.
• Can handle complex histories by performing repeated (recursive) merges.
3) Key Feature (1 Mark)
Produces a three-way merge (base + two branches), ensuring accurate integration of
changes
c.   Explain authentication and authorization in Jenkins security.
Marking Scheme (Step-wise)
o   Authentication explanation – 2M
o   Authorization explanation – 2M
o   Difference between both – 1M
Model Answer
Jenkins security is based on two key concepts: authentication and authorization.
Authentication
Authentication is the process of verifying the identity of a user.
•   Ensures that only valid users can access Jenkins
•   Methods include:
•   Jenkins internal database
CO- 1,2;   • LDAP integration
SO- 6;   5
•   Single Sign-On (SSO)
BL-3,4
Authorization
Authorization determines what actions a user is allowed to perform after
authentication.
Defines permissions such as read, write, or admin access
Implemented using strategies like:
•   Role-based access
•   Matrix-based security
Difference
•   Authentication: Verifies identity
•   Authorization: Grants permissions
d.   Differentiate between Docker Create , Docker Start and Docker Run
commands.
CO-2,3 ;
Feature   docker create   docker start   docker run   5
SO- 6;
BL-2,3
Primary   Creates a new   Restarts an existing   Creates a new
Action   container from an   container that is   container
********** 2 **********
--- page 3 ---
image without   currently in a stopped   and starts it
starting it.   state.   immediately.
Containe   Generates a new   Uses a previously   Generates a new
r ID   container ID and   assigned container ID   container ID upon
prints it to the   or name.   creation.
terminal.
State   Image → Created   Stopped → Running.   Image → Running.
Change   (Stopped).
Resource   Prepares the   Allocates CPU and   Allocates all
s   filesystem and   RAM to the existing   necessary
configuration but   container process.   resources and
consumes no   executes the
CPU/RAM.   startup command.
Configur   Allows full   Reuses the   Allows full
ation   configuration   configuration defined   configuration
(ports, volumes,   when the container   (ports, volumes,
env) during   was first created.   env) during the
creation.   run command.
Typical   Setting up a   Resuming work in a   The "go-to"
Use Case   complex   container where you   command for
configuration   want to keep previous   launching fresh
ahead of time to   file changes.   instances of an
start later.   application.
A   An online fashion retailer wants to frequently update its mobile app with
new features such as discount coupons, live tracking and personalized
recommendations. Explain why Agile is suitable for this project and how
Q.2   Iterative Development benefits the organization.
CO-1 ;   10
SO-6 ;
An online fashion retailer has a big scope in business as it is the sector which will
BL-1   always be in demand. It operates in a highly dynamic and competitive environment
where customer preferences, trends, and technologies change rapidly. In such a
scenario, adopting the Agile methodology is highly suitable for developing and
updating the mobile app.
Why Agile Process is Suitable :
********** 3 **********
--- page 4 ---
Agile Process is a flexible and adaptive software development approach that
emphasizes proper planning, continuous improvement, customer feedback, and rapid
delivery. It is well-suited for this project due to the following reasons:
1. Frequent Requirement Changes
Features like discount coupons, live tracking, and personalized
recommendations may evolve based on customer behavior , feedback and
market trends. Agile allows easy incorporation of changing requirements
even at later stages of development as per the requirements.
2. Faster Time-to-Market
Agile delivers the application in small increments (sprints), enabling the
retailer to release new features quickly. This helps the company stay
competitive by continuously enhancing user experience as well as keep them
informed and notified.
3. Customer-Centric Approach
Agile promotes regular feedback from users. The retailer can analyze user
reviews and app usage data to refine features like recommendations and
offers.
4. Improved Collaboration
Agile encourages close collaboration between developers, designers,
marketing teams, and stakeholders. This ensures that business goals like
increasing sales through discounts align with technical development.
5. Risk Reduction
Since development happens in small cycles, issues are identified and
resolved early. This minimizes the risk of major failures in the app.
How Iterative Development Benefits the Organization
Iterative Development is a core principle of Agile where the product is developed and
refined through repeated cycles (iterations). Its benefits include:
1. Continuous Improvement
Each iteration builds upon the previous version, allowing gradual
enhancement of features such as recommendation algorithms and tracking
systems.
2. Early Delivery of Value
The retailer can release basic features (e.g., simple discount coupons) early
and then enhance them (e.g., AI-based personalized coupons) in future
iterations.
3. Better Quality Assurance
Testing is performed in every iteration, ensuring bugs are detected early and
the app remains stable and reliable.
4. Adaptability to User Feedback
User feedback from one iteration can be incorporated into the next, ensuring
the app evolves according to customer needs.
5. Efficient Resource Utilization
The development team can prioritize high-value features first, ensuring
optimal use of time and resources.
B   Explain in details about the different phases in DevOps methodology
and how it is related with continuous integration?
DevOps is a combination of practices that help teams deliver software faster and more
reliably. It has several phases that work together like a loop, not a straight line. There
CO-1;
SO-6;   are 6 phases of DevOps methodology:   10
BL-1,2   Planning: The first step where everyone comes together to understand the project
requirements and goals. The aim is to set a clear direction for development. This phase
ensures that the team knows what needs to be done and how to manage the entire
process. Tools like Google Apps or Asana help in organizing tasks and keeping the
team aligned.
********** 4 **********
--- page 5 ---
Development: This is when the actual coding happens. Developers write the code,
create features, and define tests. The code is stored in a shared place called a
&quot;repository&quot; where the team can work together, make changes, and track
different versions of the code. Think of it as building the product step-by-step. Tools
like Git, Eclipse, or IntelliJ help developers collaborate efficiently.
Continuous Integration (CI): After developers write the code, this phase helps
automate checking, testing, and building the software. It ensures that changes don’t
break anything and that the system is working smoothly from the start. It’s like a quality
check to catch issues early. Jenkins or CircleCI are used for this automated process.
Deployment: Once the code is ready, it&#39;s time to release it. This phase
automates the process of making the code live, which means the product gets updated
automatically without needing manual intervention. Cloud services, like AWS or
Azure, help in managing these deployments and scaling the product as needed.
Operations: This phase happens continuously throughout the product’s life. The team
keeps an eye on the software, making sure it’s running smoothly. Operations include
maintaining the infrastructure, handling issues, and ensuring the software is available
and scalable. Tools like Loggly or AppDynamics are used to monitor the performance
of the product.
Monitoring: The final phase is all about keeping track of the software’s performance
and health. It’s an ongoing process where the team watches for any problems, collects
data, and analyses how the software is performing. This helps identify areas for
improvement. Tools like Nagios or Splunk are used for monitoring the system’s status
and fixing any issues that arise.
A
A startup is using GitHub for managing a machine learning project.
They face the following issues:
• Sensitive files are accidentally committed.
• Developers want to ignore certain files permanently.
• The team wants to review code before merging.
• A developer wants to undo a commit but keep the changes.
Q.3
• They need to maintain a clean and understandable commit
CO-1,2;   10
SO-5;   history.
BL-3   a) What is .gitignore and why is it important?
b) What is a pull request and its benefits?
c) Which command is used to undo the last commit but keep changes?
d) Why are meaningful commit messages important?
e) How can sensitive files be removed from tracking?
a) .gitignore (3 Marks):
File used to ignore unwanted files (e.g., logs, temp files). Prevents unnecessary or
sensitive files from being tracked.
********** 5 **********
--- page 6 ---
b) Pull request (2 Marks):
A request to merge changes into main branch after review; improves code quality and
collaboration.
c) Undo last commit (2 Marks):
git reset --soft HEAD~1 – removes commit but keeps changes.
d) Commit messages importance (2 Marks):
Helps understand changes and maintain clear project history.
e) Remove sensitive files (1 Mark):
Use git rm --cached <file>.
B   A project requires automation of build, test, and deployment across multiple
environments. Explain how Jenkins Pipeline concepts (Pipeline, Stage, Node, Step) can
be used to design this workflow.
Marking Scheme (Refined)
•   Introduction to pipeline concept – 2M
•   Explanation of components (Pipeline, Stage, Node, Step) – 4M
•   Workflow explanation across environments – 2M
•   Advantages – 2M
Detailed Model Answer
Jenkins Pipeline is a framework that allows defining and automating the CI/CD
workflow as code. It organizes the process into logical components that enable efficient
execution across multiple environments.
Pipeline Concept
A pipeline represents the entire workflow of building, testing, and deploying an
application. It defines the sequence of operations required for software delivery.
Key Components
1. Pipeline
CO-1,2;   •   Represents the complete CI/CD process
SO-6;   •   Defines the overall workflow   10
BL-2,3   2. Stage
•   Divides the pipeline into logical phases
•   Examples: Build, Test, Deploy
3. Node
•   Represents the execution environment (agent)
•   Executes tasks on specific machines or environments
4. Step
•   Individual tasks performed within a stage
•   Example: running tests, compiling code
Workflow Across Environments
1. The pipeline is triggered when code is committed
2. The Build stage compiles the application
3. The Test stage validates functionality
4. The Deploy stage deploys to different environments (e.g., staging, production)
5. Each stage runs on appropriate nodes based on environment requirements
Advantages
•   Automates entire workflow
•   Ensures consistency across environments
A   Explain in detail every step in Container Lifecycle and support your
Q.4
answer with a diagram. Also explain any 3 commands for Container   10
CO-2,3;
SO-6;   Management.
********** 6 **********
--- page 7 ---
BL-1,2   Marking Scheme (Step-wise)
•   Steps – 6M
•   Diagram – 2.5M
• command – 1.5 M
Container Lifecycle Stages
Image Build/Pull: The process starts by obtaining a container image from a registry
(like Docker Hub) or building one using a Dockerfile.
Created (Created State): The docker create command creates a thin writable container
layer over the image, preparing the file system, but the application does not start.
Running (Running State): The docker start command launches the container's main
process. The docker run command combines creation and starting into a single step.
Paused (Paused State): The docker pause command freezes all processes within the
container using cgroups.
Stopped (Stopped State): The docker stop command (graceful shutdown) or docker kill
command (abrupt shutdown) shuts down the primary process, halting execution. The
container remains as a resource.
Deleted (Deleted State): The docker rm command removes the container, freeing its
resources and deleting the writable layer.
Container Management Commands
docker run -d --name my-app nginx
docker ps / docker ps -a
docker stop <container_id>
docker rm <container_id>
B   What is a Pod in Kubernetes? Describe the various phases of the Pod
CO-3;   lifecycle in detail and explain the significance of each phase.
SO-6;   What is pod – 2 Marks   10
BL-2,3
Explain & significance - 8 Marks
Pods are the smallest deployable units in Kubernetes.
********** 7 **********
--- page 8 ---
A pod is just a wrapper around the container.
A Pod is a group of one or more containers, with shared storage and network
resources and a unique IP address.
It contains one or more application containers that are relatively tightly coupled and
use the shared volume.
A pod contains just a single container in a more common use case.
A Pod is not a process, but an environment for the running container(s).
A Kubernetes Pod follows a defined lifecycle, moving through a sequence of five
main phases: Pending, Running, Succeeded, Failed, and Unknown. These phases offer
a high-level summary of the Pod's status within the cluster.
Phases of a Pod Lifecycle
Pending: The Pod is accepted by Kubernetes but waiting for containers to be created or
pulled. This indicates it is waiting for scheduling, image pulling, or volume mounting.
Running: The Pod is bound to a node, with all containers created and at least one
running, starting, or restarting. This is the normal operational state for services.
Succeeded: All containers terminated successfully (exit code 0) and will not restart,
typical for completed jobs.
Failed: All containers terminated, with at least one failing (non-zero exit code),
signaling an application error. Depending on restartPolicy,   it may enter
CrashLoopBackOff.
Unknown: The control plane cannot determine the Pod's status, usually due to node
communication issues.
A   Explain Nagios Plugins (NRPE) and Objects, Nagios Commands and
Notification.
Nagios Plugins and objects – 5 Marks
Nagios Commands and Notification - 5 Marks
Nagios Plugins (NRPE)
Small executable programs/scripts used to check services, hosts, and resources.
Q.5   Plugins return data to Nagios in the form of:
OK
CO-4;   10
WARNING
SO-6;
BL-2,3,4   CRITICAL
UNKNOWN
Can check both local and remote resources.
Examples: check_disk, check_ping, check_http, etc
Nagios Objects
Objects are the fundamental building blocks of the Nagios configuration, defined in
text-based configuration files. Key object types include:
Hosts: Physical devices on your network (servers, routers, switches).
********** 8 **********
--- page 9 ---
Services: Specific aspects or characteristics of a host being monitored (e.g., memory
usage, number of logged-in users, or network services like SMTP or HTTP).
Contacts: The people or entities that receive notifications.
Host Groups/Service Groups: Logical groupings of hosts or services to simplify
configuration and management.
Timeperiods: Define specific time ranges during which monitoring checks or
notifications are active (e.g., 24x7, business hours)
Nagios Commands
Commands are definitions that tell Nagios exactly which programs or scripts to run for
various tasks. Defined in commands.cfg
Check Commands: Used to determine the status of hosts and services.
Notification Commands: Executed to send alerts (e.g., a command to send an email via
mailx).
Event Handlers: Scripts triggered automatically when a host or service changes state
(e.g., restarting a failed service).
Nagios Notifications
Notifications are alerts sent when a host or service enters a "hard" problem state or
recovers.
Filters: Before sending a notification, Nagios passes it through filters like scheduled
downtime, flap detection, and notification periods.
Methods: Alerts can be sent via email, SMS, pager, or integrated with third-party tools
like PagerDuty or xMatters.
Escalations: If an issue remains unresolved, notifications can be "escalated" to different
contacts or groups
B   Explain the key features of Kubernetes. Also, differentiate between a
Pod and a container.
Key Features of Kubernetes – 7 Marks
Difference – 3 Marks
Kubernetes is a powerful container orchestration platform with the following key
features:
Container Orchestration
CO-3;   Automates deployment, scaling, and management of containerized applications.
SO-6;   10
Auto Scaling
BL-2,3
Automatically scales applications up or down based on CPU usage or custom
metrics.
Self-Healing
Detects and replaces failed containers, restarts crashed containers, and reschedules
t
them on healthy nodes.
Service Discovery & Load Balancing
Provides built-in DNS and load balancing to distribute traffic among containers.
********** 9 **********
--- page 10 ---
Rolling Updates & Rollbacks
Enables seamless updates of applications without downtime and allows rollback to
previous versions if needed.
Storage Orchestration
Automatically mounts storage systems like local storage, NFS, or cloud storage.
Configuration Management
Manages configuration using ConfigMaps and sensitive data using Secrets.
Batch Execution
Handles batch jobs and scheduled tasks using Jobs and CronJobs.
Multi-Cloud & Hybrid Support
Can run across on-premises, public cloud, or hybrid environments.
Aspect   Pod   Container
Smallest deployable unit in   Lightweight, standalone
Definition
Kubernetes   executable package
Composition Can contain one or more containers Single application instance
Purpose   Manages and groups containers   Runs application code
Shares same IP address and network Has its own isolated
Networking
namespace   environment
Shares volumes among containers   Has isolated filesystem (unless
Storage
in the same pod   shared)
Managed by container runtime
Lifecycle   Managed by Kubernetes
(e.g., Docker)
Used for deploying applications in Used to package and run
Usage
Kubernetes   applications
A   Describe the components of Prometheus architecture and explain their
roles in monitoring systems.
Components – 6Marks
Role in Monitoring – 4Marks
Prometheus is a popular open-source monitoring and alerting system written in
Golang, capable of collecting and processing metrics from various targets.
Prometheus primarily consists of the following.
Q.6   •   Prometheus Server
•   Service Discovery
CO-3,4;   •   Time-Series Database (TSDB)   10
SO-6;   •   Targets
•   Exporters
BL-2,3
•   Push Gateway
•   Alert Manager
•   Client Libraries
• PromQL
Roles in Monitoring
•   Data Collection (Pull Model): Unlike push-based systems, Prometheus
actively scrapes targets, making it easy to detect when a target goes down.
•   Metric Storage: The TSDB allows fast, time-series-focused storage of numeric
metrics, supporting multi-dimensional data.
•   Alerting and Notification: Prometheus periodically evaluates configured rules,
triggering alerts sent to the Alert manager for notification processing.
********** 10 **********
--- page 11 ---
•   Visualization: Through   the HTTP API, data   is exposed   to   tools
like Grafana for dashboards.
B   Differentiate between Scrum, Extreme Programming and Lean Agile
Development Models. Also mention examples for each model.
•   Comparison/Differences: 7 marks
•   Examples:3 marks
Extreme
Aspect   Scrum   Lean Development
Programming (XP)
Project   Process
Focus   management   Engineering practices   optimization &
framework   waste reduction
Iterative with strong
Approach   Iterative (Sprints)   Continuous flow
coding practices
Product Owner,
Key Roles   Scrum Master,   No strict roles   No strict roles
CO-1 ;   Team
SO-6 ;   Daily stand-up,   Pair programming,   10
Eliminate waste,
BL-1   Practices   sprint planning,   TDD, continuous
fast delivery
review   integration
Documentat
Minimal   Minimal   Minimal
ion
Flexibility   Moderate   High   Very high
Delivery   Fixed sprint (2–4
Frequent releases   Continuous delivery
Cycle   weeks)
• Scrum Example:
A software company developing a mobile app uses 2-week sprints with daily
stand-ups and sprint reviews.
•   Extreme Programming (XP) Example:
A development team uses pair programming and Test-Driven Development
(TDD) to build a banking system.
•   Lean Development Example:
A startup focuses on eliminating unnecessary features and delivering only
value-added functionalities quickly.
A   Write a short note on Jenkinsfile and explain its benefits.
Marking Scheme (Step-wise)
•   Definition – 2M
• Key features – 2M
•   Benefits – 1M
Model Answer
Q.7   A Jenkinsfile is a text file that defines the CI/CD pipeline as code.
It is stored in the version control repository along with the application code and
CO-1,2;   contains instructions for building, testing, and deploying the application.   5
SO-6;   Key features:
BL-2,3,4   •   Defines pipeline stages and workflow
•   Uses a structured syntax (Declarative or Scripted)
•   Supports automation and version control
Benefits:
•   Ensures consistency across builds
•   Enables versioning and tracking of pipeline changes
•   Improves collaboration among team members
Thus, Jenkinsfile is a key component of the Pipeline-as-Code concept.
********** 11 **********
--- page 12 ---
B   With proper block diagram explain about Continuous Integration (CI).
For proper explanation and block diagram (2.5+2.5) total 5 Marks
Continuous Integration (CI) is a software development practice that makes sure
developers integrate their code into a shared repository as and when they are done
working on the feature. Each integration is verified by means of an automated build
process that allows teams to detect problems in their code at a very early stage rather
than finding them after the deployment.
CO-1;
SO-6;   5
BL-1,2
Based on the above flow, we can have a brief overview of the CI process.
•   Developers regularly check out code into their local workspaces and work on
the features assigned to them.
• Once they are done working on it, the code is committed and pushed to the
remote shared repository which is handled by making use of effective version
control tools like git.
•   The CI server keeps track of the changes done to the shared repository and it
pulls the changes as soon as it detects them.
•   The CI server then triggers the build of the code and runs unit and integration
test cases if set up.
• The team is informed of the build results. In case of the build failure, the team
has to work on fixing the issue as early as possible, and then the process
repeats.
C   Explain three main components of Docker architecture.
1) Docker Client (1.5 Marks)
• The Docker Client is the interface through which users interact
with Docker.
• It uses commands like docker build, docker run, docker pull.
CO-2,3;   • Sends requests to the Docker Daemon to perform operations.
2) Docker Daemon (Docker Engine) (2 Marks)
SO-6;   5
BL-2,3   • The Docker Daemon is the core component that runs in the background.
• It is responsible for building images, running containers, and managing
Docker objects.
•Listens to API requests from the Docker Client and executes them.
3) Docker Registry (1.5 Marks)
• A Docker Registry is a storage system for Docker images.
• Images can be pushed (uploaded) and pulled (downloaded) from the registry.
• Example: Docker Hub
********** 12 **********

[Text in pictures on this page, read by OCR]
Build and test results are fed back to the developers

¥

Jenkins check the Jenkins deploy the
shatec repository at build application the build application is
periocic intervals and onthe test server then deployed to the
every check inis production server
pullec and then build
--- page 13 ---
D   Describe the Git workflow. Explain the stages from working directory
to repository with suitable commands.
Workflow Explanation (3 Marks):
CO-1,2;
Working Directory → Staging Area → Repository.
SO-5;   Changes are made, staged using git add, and committed using git commit.   5
BL-2,3   Commands (2 Marks):
git add, git commit, git status.
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper cc32263ff9d2

- Departments: AI and Machine Learning
- Programmes: BTech AIML 7053
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AIML_7053/Agile Product Development with DevOps/ANS_Agile Product Development with DevOps(702AI0C022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Agile Product Development with DevOps
Date: 04 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. Answer to each new question to be started on a fresh page.
5. Figure in right hand side indicates full marks.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Elaborate the need of Agile Software Development.
Agile Software Development (2 Marks )and Its Need –(3 Marks)
Agile Software Development is a software development methodology that focuses on:
Flexibility
Collaboration
Customer satisfaction
It is based on the Agile Manifesto, which emphasizes:
•   Individuals and interactions over processes and tools
CO-1 ;   •   Working software over comprehensive documentation
SO-6 ;   •   Customer collaboration over contract negotiation   5
•   Responding to change over following a plan
BL-1
Need for Agile
Agile is needed because:
•   Requirements change frequently in real-world projects
•   Faster delivery is required
•   Customer feedback is essential
•   Traditional models are rigid and slow
•   It improves product quality through continuous testing and feedback
•   Agile Development Models
b.   Explain the recursive merge of git branching.
1) Definition (2 Marks)
Recursive merge is the default merge strategy used by Git when merging two
CO-1,2 ;   branches. It is mainly used when branches have diverged and may have multiple
SO- 6;   5
common ancestors. Git recursively finds a common base (merge base) and merges
BL-2,3
changes accordingly.
2) Working of Recursive Merge (2 Marks)
Git identifies the common ancestor commit of both branches.
********** 1 **********
--- page 2 ---
Compares changes from both branches with the base.
Automatically merges non-conflicting changes.
•   If conflicts occur, Git marks them for manual resolution.
• Can handle complex histories by performing repeated (recursive) merges.
3) Key Feature (1 Mark)
Produces a three-way merge (base + two branches), ensuring accurate integration of
changes
c.   Explain authentication and authorization in Jenkins security.
Marking Scheme (Step-wise)
o   Authentication explanation – 2M
o   Authorization explanation – 2M
o   Difference between both – 1M
Model Answer
Jenkins security is based on two key concepts: authentication and authorization.
Authentication
Authentication is the process of verifying the identity of a user.
•   Ensures that only valid users can access Jenkins
•   Methods include:
•   Jenkins internal database
CO- 1,2;   • LDAP integration
SO- 6;   5
•   Single Sign-On (SSO)
BL-3,4
Authorization
Authorization determines what actions a user is allowed to perform after
authentication.
Defines permissions such as read, write, or admin access
Implemented using strategies like:
•   Role-based access
•   Matrix-based security
Difference
•   Authentication: Verifies identity
•   Authorization: Grants permissions
d.   Differentiate between Docker Create , Docker Start and Docker Run
commands.
CO-2,3 ;
Feature   docker create   docker start   docker run   5
SO- 6;
BL-2,3
Primary   Creates a new   Restarts an existing   Creates a new
Action   container from an   container that is   container
********** 2 **********
--- page 3 ---
image without   currently in a stopped   and starts it
starting it.   state.   immediately.
Containe   Generates a new   Uses a previously   Generates a new
r ID   container ID and   assigned container ID   container ID upon
prints it to the   or name.   creation.
terminal.
State   Image → Created   Stopped → Running.   Image → Running.
Change   (Stopped).
Resource   Prepares the   Allocates CPU and   Allocates all
s   filesystem and   RAM to the existing   necessary
configuration but   container process.   resources and
consumes no   executes the
CPU/RAM.   startup command.
Configur   Allows full   Reuses the   Allows full
ation   configuration   configuration defined   configuration
(ports, volumes,   when the container   (ports, volumes,
env) during   was first created.   env) during the
creation.   run command.
Typical   Setting up a   Resuming work in a   The "go-to"
Use Case   complex   container where you   command for
configuration   want to keep previous   launching fresh
ahead of time to   file changes.   instances of an
start later.   application.
A   An online fashion retailer wants to frequently update its mobile app with
new features such as discount coupons, live tracking and personalized
recommendations. Explain why Agile is suitable for this project and how
Q.2   Iterative Development benefits the organization.
CO-1 ;   10
SO-6 ;
An online fashion retailer has a big scope in business as it is the sector which will
BL-1   always be in demand. It operates in a highly dynamic and competitive environment
where customer preferences, trends, and technologies change rapidly. In such a
scenario, adopting the Agile methodology is highly suitable for developing and
updating the mobile app.
Why Agile Process is Suitable :
********** 3 **********
--- page 4 ---
Agile Process is a flexible and adaptive software development approach that
emphasizes proper planning, continuous improvement, customer feedback, and rapid
delivery. It is well-suited for this project due to the following reasons:
1. Frequent Requirement Changes
Features like discount coupons, live tracking, and personalized
recommendations may evolve based on customer behavior , feedback and
market trends. Agile allows easy incorporation of changing requirements
even at later stages of development as per the requirements.
2. Faster Time-to-Market
Agile delivers the application in small increments (sprints), enabling the
retailer to release new features quickly. This helps the company stay
competitive by continuously enhancing user experience as well as keep them
informed and notified.
3. Customer-Centric Approach
Agile promotes regular feedback from users. The retailer can analyze user
reviews and app usage data to refine features like recommendations and
offers.
4. Improved Collaboration
Agile encourages close collaboration between developers, designers,
marketing teams, and stakeholders. This ensures that business goals like
increasing sales through discounts align with technical development.
5. Risk Reduction
Since development happens in small cycles, issues are identified and
resolved early. This minimizes the risk of major failures in the app.
How Iterative Development Benefits the Organization
Iterative Development is a core principle of Agile where the product is developed and
refined through repeated cycles (iterations). Its benefits include:
1. Continuous Improvement
Each iteration builds upon the previous version, allowing gradual
enhancement of features such as recommendation algorithms and tracking
systems.
2. Early Delivery of Value
The retailer can release basic features (e.g., simple discount coupons) early
and then enhance them (e.g., AI-based personalized coupons) in future
iterations.
3. Better Quality Assurance
Testing is performed in every iteration, ensuring bugs are detected early and
the app remains stable and reliable.
4. Adaptability to User Feedback
User feedback from one iteration can be incorporated into the next, ensuring
the app evolves according to customer needs.
5. Efficient Resource Utilization
The development team can prioritize high-value features first, ensuring
optimal use of time and resources.
B   Explain in details about the different phases in DevOps methodology
and how it is related with continuous integration?
DevOps is a combination of practices that help teams deliver software faster and more
reliably. It has several phases that work together like a loop, not a straight line. There
CO-1;
SO-6;   are 6 phases of DevOps methodology:   10
BL-1,2   Planning: The first step where everyone comes together to understand the project
requirements and goals. The aim is to set a clear direction for development. This phase
ensures that the team knows what needs to be done and how to manage the entire
process. Tools like Google Apps or Asana help in organizing tasks and keeping the
team aligned.
********** 4 **********
--- page 5 ---
Development: This is when the actual coding happens. Developers write the code,
create features, and define tests. The code is stored in a shared place called a
&quot;repository&quot; where the team can work together, make changes, and track
different versions of the code. Think of it as building the product step-by-step. Tools
like Git, Eclipse, or IntelliJ help developers collaborate efficiently.
Continuous Integration (CI): After developers write the code, this phase helps
automate checking, testing, and building the software. It ensures that changes don’t
break anything and that the system is working smoothly from the start. It’s like a quality
check to catch issues early. Jenkins or CircleCI are used for this automated process.
Deployment: Once the code is ready, it&#39;s time to release it. This phase
automates the process of making the code live, which means the product gets updated
automatically without needing manual intervention. Cloud services, like AWS or
Azure, help in managing these deployments and scaling the product as needed.
Operations: This phase happens continuously throughout the product’s life. The team
keeps an eye on the software, making sure it’s running smoothly. Operations include
maintaining the infrastructure, handling issues, and ensuring the software is available
and scalable. Tools like Loggly or AppDynamics are used to monitor the performance
of the product.
Monitoring: The final phase is all about keeping track of the software’s performance
and health. It’s an ongoing process where the team watches for any problems, collects
data, and analyses how the software is performing. This helps identify areas for
improvement. Tools like Nagios or Splunk are used for monitoring the system’s status
and fixing any issues that arise.
A
A startup is using GitHub for managing a machine learning project.
They face the following issues:
• Sensitive files are accidentally committed.
• Developers want to ignore certain files permanently.
• The team wants to review code before merging.
• A developer wants to undo a commit but keep the changes.
Q.3
• They need to maintain a clean and understandable commit
CO-1,2;   10
SO-5;   history.
BL-3   a) What is .gitignore and why is it important?
b) What is a pull request and its benefits?
c) Which command is used to undo the last commit but keep changes?
d) Why are meaningful commit messages important?
e) How can sensitive files be removed from tracking?
a) .gitignore (3 Marks):
File used to ignore unwanted files (e.g., logs, temp files). Prevents unnecessary or
sensitive files from being tracked.
********** 5 **********
--- page 6 ---
b) Pull request (2 Marks):
A request to merge changes into main branch after review; improves code quality and
collaboration.
c) Undo last commit (2 Marks):
git reset --soft HEAD~1 – removes commit but keeps changes.
d) Commit messages importance (2 Marks):
Helps understand changes and maintain clear project history.
e) Remove sensitive files (1 Mark):
Use git rm --cached <file>.
B   A project requires automation of build, test, and deployment across multiple
environments. Explain how Jenkins Pipeline concepts (Pipeline, Stage, Node, Step) can
be used to design this workflow.
Marking Scheme (Refined)
•   Introduction to pipeline concept – 2M
•   Explanation of components (Pipeline, Stage, Node, Step) – 4M
•   Workflow explanation across environments – 2M
•   Advantages – 2M
Detailed Model Answer
Jenkins Pipeline is a framework that allows defining and automating the CI/CD
workflow as code. It organizes the process into logical components that enable efficient
execution across multiple environments.
Pipeline Concept
A pipeline represents the entire workflow of building, testing, and deploying an
application. It defines the sequence of operations required for software delivery.
Key Components
1. Pipeline
CO-1,2;   •   Represents the complete CI/CD process
SO-6;   •   Defines the overall workflow   10
BL-2,3   2. Stage
•   Divides the pipeline into logical phases
•   Examples: Build, Test, Deploy
3. Node
•   Represents the execution environment (agent)
•   Executes tasks on specific machines or environments
4. Step
•   Individual tasks performed within a stage
•   Example: running tests, compiling code
Workflow Across Environments
1. The pipeline is triggered when code is committed
2. The Build stage compiles the application
3. The Test stage validates functionality
4. The Deploy stage deploys to different environments (e.g., staging, production)
5. Each stage runs on appropriate nodes based on environment requirements
Advantages
•   Automates entire workflow
•   Ensures consistency across environments
A   Explain in detail every step in Container Lifecycle and support your
Q.4
answer with a diagram. Also explain any 3 commands for Container   10
CO-2,3;
SO-6;   Management.
********** 6 **********
--- page 7 ---
BL-1,2   Marking Scheme (Step-wise)
•   Steps – 6M
•   Diagram – 2.5M
• command – 1.5 M
Container Lifecycle Stages
Image Build/Pull: The process starts by obtaining a container image from a registry
(like Docker Hub) or building one using a Dockerfile.
Created (Created State): The docker create command creates a thin writable container
layer over the image, preparing the file system, but the application does not start.
Running (Running State): The docker start command launches the container's main
process. The docker run command combines creation and starting into a single step.
Paused (Paused State): The docker pause command freezes all processes within the
container using cgroups.
Stopped (Stopped State): The docker stop command (graceful shutdown) or docker kill
command (abrupt shutdown) shuts down the primary process, halting execution. The
container remains as a resource.
Deleted (Deleted State): The docker rm command removes the container, freeing its
resources and deleting the writable layer.
Container Management Commands
docker run -d --name my-app nginx
docker ps / docker ps -a
docker stop <container_id>
docker rm <container_id>
B   What is a Pod in Kubernetes? Describe the various phases of the Pod
CO-3;   lifecycle in detail and explain the significance of each phase.
SO-6;   What is pod – 2 Marks   10
BL-2,3
Explain & significance - 8 Marks
Pods are the smallest deployable units in Kubernetes.
********** 7 **********
--- page 8 ---
A pod is just a wrapper around the container.
A Pod is a group of one or more containers, with shared storage and network
resources and a unique IP address.
It contains one or more application containers that are relatively tightly coupled and
use the shared volume.
A pod contains just a single container in a more common use case.
A Pod is not a process, but an environment for the running container(s).
A Kubernetes Pod follows a defined lifecycle, moving through a sequence of five
main phases: Pending, Running, Succeeded, Failed, and Unknown. These phases offer
a high-level summary of the Pod's status within the cluster.
Phases of a Pod Lifecycle
Pending: The Pod is accepted by Kubernetes but waiting for containers to be created or
pulled. This indicates it is waiting for scheduling, image pulling, or volume mounting.
Running: The Pod is bound to a node, with all containers created and at least one
running, starting, or restarting. This is the normal operational state for services.
Succeeded: All containers terminated successfully (exit code 0) and will not restart,
typical for completed jobs.
Failed: All containers terminated, with at least one failing (non-zero exit code),
signaling an application error. Depending on restartPolicy,   it may enter
CrashLoopBackOff.
Unknown: The control plane cannot determine the Pod's status, usually due to node
communication issues.
A   Explain Nagios Plugins (NRPE) and Objects, Nagios Commands and
Notification.
Nagios Plugins and objects – 5 Marks
Nagios Commands and Notification - 5 Marks
Nagios Plugins (NRPE)
Small executable programs/scripts used to check services, hosts, and resources.
Q.5   Plugins return data to Nagios in the form of:
OK
CO-4;   10
WARNING
SO-6;
BL-2,3,4   CRITICAL
UNKNOWN
Can check both local and remote resources.
Examples: check_disk, check_ping, check_http, etc
Nagios Objects
Objects are the fundamental building blocks of the Nagios configuration, defined in
text-based configuration files. Key object types include:
Hosts: Physical devices on your network (servers, routers, switches).
********** 8 **********
--- page 9 ---
Services: Specific aspects or characteristics of a host being monitored (e.g., memory
usage, number of logged-in users, or network services like SMTP or HTTP).
Contacts: The people or entities that receive notifications.
Host Groups/Service Groups: Logical groupings of hosts or services to simplify
configuration and management.
Timeperiods: Define specific time ranges during which monitoring checks or
notifications are active (e.g., 24x7, business hours)
Nagios Commands
Commands are definitions that tell Nagios exactly which programs or scripts to run for
various tasks. Defined in commands.cfg
Check Commands: Used to determine the status of hosts and services.
Notification Commands: Executed to send alerts (e.g., a command to send an email via
mailx).
Event Handlers: Scripts triggered automatically when a host or service changes state
(e.g., restarting a failed service).
Nagios Notifications
Notifications are alerts sent when a host or service enters a "hard" problem state or
recovers.
Filters: Before sending a notification, Nagios passes it through filters like scheduled
downtime, flap detection, and notification periods.
Methods: Alerts can be sent via email, SMS, pager, or integrated with third-party tools
like PagerDuty or xMatters.
Escalations: If an issue remains unresolved, notifications can be "escalated" to different
contacts or groups
B   Explain the key features of Kubernetes. Also, differentiate between a
Pod and a container.
Key Features of Kubernetes – 7 Marks
Difference – 3 Marks
Kubernetes is a powerful container orchestration platform with the following key
features:
Container Orchestration
CO-3;   Automates deployment, scaling, and management of containerized applications.
SO-6;   10
Auto Scaling
BL-2,3
Automatically scales applications up or down based on CPU usage or custom
metrics.
Self-Healing
Detects and replaces failed containers, restarts crashed containers, and reschedules
t
them on healthy nodes.
Service Discovery & Load Balancing
Provides built-in DNS and load balancing to distribute traffic among containers.
********** 9 **********
--- page 10 ---
Rolling Updates & Rollbacks
Enables seamless updates of applications without downtime and allows rollback to
previous versions if needed.
Storage Orchestration
Automatically mounts storage systems like local storage, NFS, or cloud storage.
Configuration Management
Manages configuration using ConfigMaps and sensitive data using Secrets.
Batch Execution
Handles batch jobs and scheduled tasks using Jobs and CronJobs.
Multi-Cloud & Hybrid Support
Can run across on-premises, public cloud, or hybrid environments.
Aspect   Pod   Container
Smallest deployable unit in   Lightweight, standalone
Definition
Kubernetes   executable package
Composition Can contain one or more containers Single application instance
Purpose   Manages and groups containers   Runs application code
Shares same IP address and network Has its own isolated
Networking
namespace   environment
Shares volumes among containers   Has isolated filesystem (unless
Storage
in the same pod   shared)
Managed by container runtime
Lifecycle   Managed by Kubernetes
(e.g., Docker)
Used for deploying applications in Used to package and run
Usage
Kubernetes   applications
A   Describe the components of Prometheus architecture and explain their
roles in monitoring systems.
Components – 6Marks
Role in Monitoring – 4Marks
Prometheus is a popular open-source monitoring and alerting system written in
Golang, capable of collecting and processing metrics from various targets.
Prometheus primarily consists of the following.
Q.6   •   Prometheus Server
•   Service Discovery
CO-3,4;   •   Time-Series Database (TSDB)   10
SO-6;   •   Targets
•   Exporters
BL-2,3
•   Push Gateway
•   Alert Manager
•   Client Libraries
• PromQL
Roles in Monitoring
•   Data Collection (Pull Model): Unlike push-based systems, Prometheus
actively scrapes targets, making it easy to detect when a target goes down.
•   Metric Storage: The TSDB allows fast, time-series-focused storage of numeric
metrics, supporting multi-dimensional data.
•   Alerting and Notification: Prometheus periodically evaluates configured rules,
triggering alerts sent to the Alert manager for notification processing.
********** 10 **********
--- page 11 ---
•   Visualization: Through   the HTTP API, data   is exposed   to   tools
like Grafana for dashboards.
B   Differentiate between Scrum, Extreme Programming and Lean Agile
Development Models. Also mention examples for each model.
•   Comparison/Differences: 7 marks
•   Examples:3 marks
Extreme
Aspect   Scrum   Lean Development
Programming (XP)
Project   Process
Focus   management   Engineering practices   optimization &
framework   waste reduction
Iterative with strong
Approach   Iterative (Sprints)   Continuous flow
coding practices
Product Owner,
Key Roles   Scrum Master,   No strict roles   No strict roles
CO-1 ;   Team
SO-6 ;   Daily stand-up,   Pair programming,   10
Eliminate waste,
BL-1   Practices   sprint planning,   TDD, continuous
fast delivery
review   integration
Documentat
Minimal   Minimal   Minimal
ion
Flexibility   Moderate   High   Very high
Delivery   Fixed sprint (2–4
Frequent releases   Continuous delivery
Cycle   weeks)
• Scrum Example:
A software company developing a mobile app uses 2-week sprints with daily
stand-ups and sprint reviews.
•   Extreme Programming (XP) Example:
A development team uses pair programming and Test-Driven Development
(TDD) to build a banking system.
•   Lean Development Example:
A startup focuses on eliminating unnecessary features and delivering only
value-added functionalities quickly.
A   Write a short note on Jenkinsfile and explain its benefits.
Marking Scheme (Step-wise)
•   Definition – 2M
• Key features – 2M
•   Benefits – 1M
Model Answer
Q.7   A Jenkinsfile is a text file that defines the CI/CD pipeline as code.
It is stored in the version control repository along with the application code and
CO-1,2;   contains instructions for building, testing, and deploying the application.   5
SO-6;   Key features:
BL-2,3,4   •   Defines pipeline stages and workflow
•   Uses a structured syntax (Declarative or Scripted)
•   Supports automation and version control
Benefits:
•   Ensures consistency across builds
•   Enables versioning and tracking of pipeline changes
•   Improves collaboration among team members
Thus, Jenkinsfile is a key component of the Pipeline-as-Code concept.
********** 11 **********
--- page 12 ---
B   With proper block diagram explain about Continuous Integration (CI).
For proper explanation and block diagram (2.5+2.5) total 5 Marks
Continuous Integration (CI) is a software development practice that makes sure
developers integrate their code into a shared repository as and when they are done
working on the feature. Each integration is verified by means of an automated build
process that allows teams to detect problems in their code at a very early stage rather
than finding them after the deployment.
CO-1;
SO-6;   5
BL-1,2
Based on the above flow, we can have a brief overview of the CI process.
•   Developers regularly check out code into their local workspaces and work on
the features assigned to them.
• Once they are done working on it, the code is committed and pushed to the
remote shared repository which is handled by making use of effective version
control tools like git.
•   The CI server keeps track of the changes done to the shared repository and it
pulls the changes as soon as it detects them.
•   The CI server then triggers the build of the code and runs unit and integration
test cases if set up.
• The team is informed of the build results. In case of the build failure, the team
has to work on fixing the issue as early as possible, and then the process
repeats.
C   Explain three main components of Docker architecture.
1) Docker Client (1.5 Marks)
• The Docker Client is the interface through which users interact
with Docker.
• It uses commands like docker build, docker run, docker pull.
CO-2,3;   • Sends requests to the Docker Daemon to perform operations.
2) Docker Daemon (Docker Engine) (2 Marks)
SO-6;   5
BL-2,3   • The Docker Daemon is the core component that runs in the background.
• It is responsible for building images, running containers, and managing
Docker objects.
•Listens to API requests from the Docker Client and executes them.
3) Docker Registry (1.5 Marks)
• A Docker Registry is a storage system for Docker images.
• Images can be pushed (uploaded) and pulled (downloaded) from the registry.
• Example: Docker Hub
********** 12 **********

[Text in pictures on this page, read by OCR]
Build and test results are fed back to the developers

¥

Jenkins check the Jenkins deploy the
shatec repository at build application the build application is
periocic intervals and onthe test server then deployed to the
every check inis production server
pullec and then build
--- page 13 ---
D   Describe the Git workflow. Explain the stages from working directory
to repository with suitable commands.
Workflow Explanation (3 Marks):
CO-1,2;
Working Directory → Staging Area → Repository.
SO-5;   Changes are made, staged using git add, and committed using git commit.   5
BL-2,3   Commands (2 Marks):
git add, git commit, git status.
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 71cbfb64a8fe

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_AI_7012/Agile Product Development with DevOps/ANS_Agile Product Development with DevOps(702AI0C022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Agile Product Development with DevOps
Date: 04 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. Answer to each new question to be started on a fresh page.
5. Figure in right hand side indicates full marks.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Elaborate the need of Agile Software Development.
Agile Software Development (2 Marks )and Its Need –(3 Marks)
Agile Software Development is a software development methodology that focuses on:
Flexibility
Collaboration
Customer satisfaction
It is based on the Agile Manifesto, which emphasizes:
•   Individuals and interactions over processes and tools
CO-1 ;   •   Working software over comprehensive documentation
SO-6 ;   •   Customer collaboration over contract negotiation   5
•   Responding to change over following a plan
BL-1
Need for Agile
Agile is needed because:
•   Requirements change frequently in real-world projects
•   Faster delivery is required
•   Customer feedback is essential
•   Traditional models are rigid and slow
•   It improves product quality through continuous testing and feedback
•   Agile Development Models
b.   Explain the recursive merge of git branching.
1) Definition (2 Marks)
Recursive merge is the default merge strategy used by Git when merging two
CO-1,2 ;   branches. It is mainly used when branches have diverged and may have multiple
SO- 6;   5
common ancestors. Git recursively finds a common base (merge base) and merges
BL-2,3
changes accordingly.
2) Working of Recursive Merge (2 Marks)
Git identifies the common ancestor commit of both branches.
********** 1 **********
--- page 2 ---
Compares changes from both branches with the base.
Automatically merges non-conflicting changes.
•   If conflicts occur, Git marks them for manual resolution.
• Can handle complex histories by performing repeated (recursive) merges.
3) Key Feature (1 Mark)
Produces a three-way merge (base + two branches), ensuring accurate integration of
changes
c.   Explain authentication and authorization in Jenkins security.
Marking Scheme (Step-wise)
o   Authentication explanation – 2M
o   Authorization explanation – 2M
o   Difference between both – 1M
Model Answer
Jenkins security is based on two key concepts: authentication and authorization.
Authentication
Authentication is the process of verifying the identity of a user.
•   Ensures that only valid users can access Jenkins
•   Methods include:
•   Jenkins internal database
CO- 1,2;   • LDAP integration
SO- 6;   5
•   Single Sign-On (SSO)
BL-3,4
Authorization
Authorization determines what actions a user is allowed to perform after
authentication.
Defines permissions such as read, write, or admin access
Implemented using strategies like:
•   Role-based access
•   Matrix-based security
Difference
•   Authentication: Verifies identity
•   Authorization: Grants permissions
d.   Differentiate between Docker Create , Docker Start and Docker Run
commands.
CO-2,3 ;
Feature   docker create   docker start   docker run   5
SO- 6;
BL-2,3
Primary   Creates a new   Restarts an existing   Creates a new
Action   container from an   container that is   container
********** 2 **********
--- page 3 ---
image without   currently in a stopped   and starts it
starting it.   state.   immediately.
Containe   Generates a new   Uses a previously   Generates a new
r ID   container ID and   assigned container ID   container ID upon
prints it to the   or name.   creation.
terminal.
State   Image → Created   Stopped → Running.   Image → Running.
Change   (Stopped).
Resource   Prepares the   Allocates CPU and   Allocates all
s   filesystem and   RAM to the existing   necessary
configuration but   container process.   resources and
consumes no   executes the
CPU/RAM.   startup command.
Configur   Allows full   Reuses the   Allows full
ation   configuration   configuration defined   configuration
(ports, volumes,   when the container   (ports, volumes,
env) during   was first created.   env) during the
creation.   run command.
Typical   Setting up a   Resuming work in a   The "go-to"
Use Case   complex   container where you   command for
configuration   want to keep previous   launching fresh
ahead of time to   file changes.   instances of an
start later.   application.
A   An online fashion retailer wants to frequently update its mobile app with
new features such as discount coupons, live tracking and personalized
recommendations. Explain why Agile is suitable for this project and how
Q.2   Iterative Development benefits the organization.
CO-1 ;   10
SO-6 ;
An online fashion retailer has a big scope in business as it is the sector which will
BL-1   always be in demand. It operates in a highly dynamic and competitive environment
where customer preferences, trends, and technologies change rapidly. In such a
scenario, adopting the Agile methodology is highly suitable for developing and
updating the mobile app.
Why Agile Process is Suitable :
********** 3 **********
--- page 4 ---
Agile Process is a flexible and adaptive software development approach that
emphasizes proper planning, continuous improvement, customer feedback, and rapid
delivery. It is well-suited for this project due to the following reasons:
1. Frequent Requirement Changes
Features like discount coupons, live tracking, and personalized
recommendations may evolve based on customer behavior , feedback and
market trends. Agile allows easy incorporation of changing requirements
even at later stages of development as per the requirements.
2. Faster Time-to-Market
Agile delivers the application in small increments (sprints), enabling the
retailer to release new features quickly. This helps the company stay
competitive by continuously enhancing user experience as well as keep them
informed and notified.
3. Customer-Centric Approach
Agile promotes regular feedback from users. The retailer can analyze user
reviews and app usage data to refine features like recommendations and
offers.
4. Improved Collaboration
Agile encourages close collaboration between developers, designers,
marketing teams, and stakeholders. This ensures that business goals like
increasing sales through discounts align with technical development.
5. Risk Reduction
Since development happens in small cycles, issues are identified and
resolved early. This minimizes the risk of major failures in the app.
How Iterative Development Benefits the Organization
Iterative Development is a core principle of Agile where the product is developed and
refined through repeated cycles (iterations). Its benefits include:
1. Continuous Improvement
Each iteration builds upon the previous version, allowing gradual
enhancement of features such as recommendation algorithms and tracking
systems.
2. Early Delivery of Value
The retailer can release basic features (e.g., simple discount coupons) early
and then enhance them (e.g., AI-based personalized coupons) in future
iterations.
3. Better Quality Assurance
Testing is performed in every iteration, ensuring bugs are detected early and
the app remains stable and reliable.
4. Adaptability to User Feedback
User feedback from one iteration can be incorporated into the next, ensuring
the app evolves according to customer needs.
5. Efficient Resource Utilization
The development team can prioritize high-value features first, ensuring
optimal use of time and resources.
B   Explain in details about the different phases in DevOps methodology
and how it is related with continuous integration?
DevOps is a combination of practices that help teams deliver software faster and more
reliably. It has several phases that work together like a loop, not a straight line. There
CO-1;
SO-6;   are 6 phases of DevOps methodology:   10
BL-1,2   Planning: The first step where everyone comes together to understand the project
requirements and goals. The aim is to set a clear direction for development. This phase
ensures that the team knows what needs to be done and how to manage the entire
process. Tools like Google Apps or Asana help in organizing tasks and keeping the
team aligned.
********** 4 **********
--- page 5 ---
Development: This is when the actual coding happens. Developers write the code,
create features, and define tests. The code is stored in a shared place called a
&quot;repository&quot; where the team can work together, make changes, and track
different versions of the code. Think of it as building the product step-by-step. Tools
like Git, Eclipse, or IntelliJ help developers collaborate efficiently.
Continuous Integration (CI): After developers write the code, this phase helps
automate checking, testing, and building the software. It ensures that changes don’t
break anything and that the system is working smoothly from the start. It’s like a quality
check to catch issues early. Jenkins or CircleCI are used for this automated process.
Deployment: Once the code is ready, it&#39;s time to release it. This phase
automates the process of making the code live, which means the product gets updated
automatically without needing manual intervention. Cloud services, like AWS or
Azure, help in managing these deployments and scaling the product as needed.
Operations: This phase happens continuously throughout the product’s life. The team
keeps an eye on the software, making sure it’s running smoothly. Operations include
maintaining the infrastructure, handling issues, and ensuring the software is available
and scalable. Tools like Loggly or AppDynamics are used to monitor the performance
of the product.
Monitoring: The final phase is all about keeping track of the software’s performance
and health. It’s an ongoing process where the team watches for any problems, collects
data, and analyses how the software is performing. This helps identify areas for
improvement. Tools like Nagios or Splunk are used for monitoring the system’s status
and fixing any issues that arise.
A
A startup is using GitHub for managing a machine learning project.
They face the following issues:
• Sensitive files are accidentally committed.
• Developers want to ignore certain files permanently.
• The team wants to review code before merging.
• A developer wants to undo a commit but keep the changes.
Q.3
• They need to maintain a clean and understandable commit
CO-1,2;   10
SO-5;   history.
BL-3   a) What is .gitignore and why is it important?
b) What is a pull request and its benefits?
c) Which command is used to undo the last commit but keep changes?
d) Why are meaningful commit messages important?
e) How can sensitive files be removed from tracking?
a) .gitignore (3 Marks):
File used to ignore unwanted files (e.g., logs, temp files). Prevents unnecessary or
sensitive files from being tracked.
********** 5 **********
--- page 6 ---
b) Pull request (2 Marks):
A request to merge changes into main branch after review; improves code quality and
collaboration.
c) Undo last commit (2 Marks):
git reset --soft HEAD~1 – removes commit but keeps changes.
d) Commit messages importance (2 Marks):
Helps understand changes and maintain clear project history.
e) Remove sensitive files (1 Mark):
Use git rm --cached <file>.
B   A project requires automation of build, test, and deployment across multiple
environments. Explain how Jenkins Pipeline concepts (Pipeline, Stage, Node, Step) can
be used to design this workflow.
Marking Scheme (Refined)
•   Introduction to pipeline concept – 2M
•   Explanation of components (Pipeline, Stage, Node, Step) – 4M
•   Workflow explanation across environments – 2M
•   Advantages – 2M
Detailed Model Answer
Jenkins Pipeline is a framework that allows defining and automating the CI/CD
workflow as code. It organizes the process into logical components that enable efficient
execution across multiple environments.
Pipeline Concept
A pipeline represents the entire workflow of building, testing, and deploying an
application. It defines the sequence of operations required for software delivery.
Key Components
1. Pipeline
CO-1,2;   •   Represents the complete CI/CD process
SO-6;   •   Defines the overall workflow   10
BL-2,3   2. Stage
•   Divides the pipeline into logical phases
•   Examples: Build, Test, Deploy
3. Node
•   Represents the execution environment (agent)
•   Executes tasks on specific machines or environments
4. Step
•   Individual tasks performed within a stage
•   Example: running tests, compiling code
Workflow Across Environments
1. The pipeline is triggered when code is committed
2. The Build stage compiles the application
3. The Test stage validates functionality
4. The Deploy stage deploys to different environments (e.g., staging, production)
5. Each stage runs on appropriate nodes based on environment requirements
Advantages
•   Automates entire workflow
•   Ensures consistency across environments
A   Explain in detail every step in Container Lifecycle and support your
Q.4
answer with a diagram. Also explain any 3 commands for Container   10
CO-2,3;
SO-6;   Management.
********** 6 **********
--- page 7 ---
BL-1,2   Marking Scheme (Step-wise)
•   Steps – 6M
•   Diagram – 2.5M
• command – 1.5 M
Container Lifecycle Stages
Image Build/Pull: The process starts by obtaining a container image from a registry
(like Docker Hub) or building one using a Dockerfile.
Created (Created State): The docker create command creates a thin writable container
layer over the image, preparing the file system, but the application does not start.
Running (Running State): The docker start command launches the container's main
process. The docker run command combines creation and starting into a single step.
Paused (Paused State): The docker pause command freezes all processes within the
container using cgroups.
Stopped (Stopped State): The docker stop command (graceful shutdown) or docker kill
command (abrupt shutdown) shuts down the primary process, halting execution. The
container remains as a resource.
Deleted (Deleted State): The docker rm command removes the container, freeing its
resources and deleting the writable layer.
Container Management Commands
docker run -d --name my-app nginx
docker ps / docker ps -a
docker stop <container_id>
docker rm <container_id>
B   What is a Pod in Kubernetes? Describe the various phases of the Pod
CO-3;   lifecycle in detail and explain the significance of each phase.
SO-6;   What is pod – 2 Marks   10
BL-2,3
Explain & significance - 8 Marks
Pods are the smallest deployable units in Kubernetes.
********** 7 **********
--- page 8 ---
A pod is just a wrapper around the container.
A Pod is a group of one or more containers, with shared storage and network
resources and a unique IP address.
It contains one or more application containers that are relatively tightly coupled and
use the shared volume.
A pod contains just a single container in a more common use case.
A Pod is not a process, but an environment for the running container(s).
A Kubernetes Pod follows a defined lifecycle, moving through a sequence of five
main phases: Pending, Running, Succeeded, Failed, and Unknown. These phases offer
a high-level summary of the Pod's status within the cluster.
Phases of a Pod Lifecycle
Pending: The Pod is accepted by Kubernetes but waiting for containers to be created or
pulled. This indicates it is waiting for scheduling, image pulling, or volume mounting.
Running: The Pod is bound to a node, with all containers created and at least one
running, starting, or restarting. This is the normal operational state for services.
Succeeded: All containers terminated successfully (exit code 0) and will not restart,
typical for completed jobs.
Failed: All containers terminated, with at least one failing (non-zero exit code),
signaling an application error. Depending on restartPolicy,   it may enter
CrashLoopBackOff.
Unknown: The control plane cannot determine the Pod's status, usually due to node
communication issues.
A   Explain Nagios Plugins (NRPE) and Objects, Nagios Commands and
Notification.
Nagios Plugins and objects – 5 Marks
Nagios Commands and Notification - 5 Marks
Nagios Plugins (NRPE)
Small executable programs/scripts used to check services, hosts, and resources.
Q.5   Plugins return data to Nagios in the form of:
OK
CO-4;   10
WARNING
SO-6;
BL-2,3,4   CRITICAL
UNKNOWN
Can check both local and remote resources.
Examples: check_disk, check_ping, check_http, etc
Nagios Objects
Objects are the fundamental building blocks of the Nagios configuration, defined in
text-based configuration files. Key object types include:
Hosts: Physical devices on your network (servers, routers, switches).
********** 8 **********
--- page 9 ---
Services: Specific aspects or characteristics of a host being monitored (e.g., memory
usage, number of logged-in users, or network services like SMTP or HTTP).
Contacts: The people or entities that receive notifications.
Host Groups/Service Groups: Logical groupings of hosts or services to simplify
configuration and management.
Timeperiods: Define specific time ranges during which monitoring checks or
notifications are active (e.g., 24x7, business hours)
Nagios Commands
Commands are definitions that tell Nagios exactly which programs or scripts to run for
various tasks. Defined in commands.cfg
Check Commands: Used to determine the status of hosts and services.
Notification Commands: Executed to send alerts (e.g., a command to send an email via
mailx).
Event Handlers: Scripts triggered automatically when a host or service changes state
(e.g., restarting a failed service).
Nagios Notifications
Notifications are alerts sent when a host or service enters a "hard" problem state or
recovers.
Filters: Before sending a notification, Nagios passes it through filters like scheduled
downtime, flap detection, and notification periods.
Methods: Alerts can be sent via email, SMS, pager, or integrated with third-party tools
like PagerDuty or xMatters.
Escalations: If an issue remains unresolved, notifications can be "escalated" to different
contacts or groups
B   Explain the key features of Kubernetes. Also, differentiate between a
Pod and a container.
Key Features of Kubernetes – 7 Marks
Difference – 3 Marks
Kubernetes is a powerful container orchestration platform with the following key
features:
Container Orchestration
CO-3;   Automates deployment, scaling, and management of containerized applications.
SO-6;   10
Auto Scaling
BL-2,3
Automatically scales applications up or down based on CPU usage or custom
metrics.
Self-Healing
Detects and replaces failed containers, restarts crashed containers, and reschedules
t
them on healthy nodes.
Service Discovery & Load Balancing
Provides built-in DNS and load balancing to distribute traffic among containers.
********** 9 **********
--- page 10 ---
Rolling Updates & Rollbacks
Enables seamless updates of applications without downtime and allows rollback to
previous versions if needed.
Storage Orchestration
Automatically mounts storage systems like local storage, NFS, or cloud storage.
Configuration Management
Manages configuration using ConfigMaps and sensitive data using Secrets.
Batch Execution
Handles batch jobs and scheduled tasks using Jobs and CronJobs.
Multi-Cloud & Hybrid Support
Can run across on-premises, public cloud, or hybrid environments.
Aspect   Pod   Container
Smallest deployable unit in   Lightweight, standalone
Definition
Kubernetes   executable package
Composition Can contain one or more containers Single application instance
Purpose   Manages and groups containers   Runs application code
Shares same IP address and network Has its own isolated
Networking
namespace   environment
Shares volumes among containers   Has isolated filesystem (unless
Storage
in the same pod   shared)
Managed by container runtime
Lifecycle   Managed by Kubernetes
(e.g., Docker)
Used for deploying applications in Used to package and run
Usage
Kubernetes   applications
A   Describe the components of Prometheus architecture and explain their
roles in monitoring systems.
Components – 6Marks
Role in Monitoring – 4Marks
Prometheus is a popular open-source monitoring and alerting system written in
Golang, capable of collecting and processing metrics from various targets.
Prometheus primarily consists of the following.
Q.6   •   Prometheus Server
•   Service Discovery
CO-3,4;   •   Time-Series Database (TSDB)   10
SO-6;   •   Targets
•   Exporters
BL-2,3
•   Push Gateway
•   Alert Manager
•   Client Libraries
• PromQL
Roles in Monitoring
•   Data Collection (Pull Model): Unlike push-based systems, Prometheus
actively scrapes targets, making it easy to detect when a target goes down.
•   Metric Storage: The TSDB allows fast, time-series-focused storage of numeric
metrics, supporting multi-dimensional data.
•   Alerting and Notification: Prometheus periodically evaluates configured rules,
triggering alerts sent to the Alert manager for notification processing.
********** 10 **********
--- page 11 ---
•   Visualization: Through   the HTTP API, data   is exposed   to   tools
like Grafana for dashboards.
B   Differentiate between Scrum, Extreme Programming and Lean Agile
Development Models. Also mention examples for each model.
•   Comparison/Differences: 7 marks
•   Examples:3 marks
Extreme
Aspect   Scrum   Lean Development
Programming (XP)
Project   Process
Focus   management   Engineering practices   optimization &
framework   waste reduction
Iterative with strong
Approach   Iterative (Sprints)   Continuous flow
coding practices
Product Owner,
Key Roles   Scrum Master,   No strict roles   No strict roles
CO-1 ;   Team
SO-6 ;   Daily stand-up,   Pair programming,   10
Eliminate waste,
BL-1   Practices   sprint planning,   TDD, continuous
fast delivery
review   integration
Documentat
Minimal   Minimal   Minimal
ion
Flexibility   Moderate   High   Very high
Delivery   Fixed sprint (2–4
Frequent releases   Continuous delivery
Cycle   weeks)
• Scrum Example:
A software company developing a mobile app uses 2-week sprints with daily
stand-ups and sprint reviews.
•   Extreme Programming (XP) Example:
A development team uses pair programming and Test-Driven Development
(TDD) to build a banking system.
•   Lean Development Example:
A startup focuses on eliminating unnecessary features and delivering only
value-added functionalities quickly.
A   Write a short note on Jenkinsfile and explain its benefits.
Marking Scheme (Step-wise)
•   Definition – 2M
• Key features – 2M
•   Benefits – 1M
Model Answer
Q.7   A Jenkinsfile is a text file that defines the CI/CD pipeline as code.
It is stored in the version control repository along with the application code and
CO-1,2;   contains instructions for building, testing, and deploying the application.   5
SO-6;   Key features:
BL-2,3,4   •   Defines pipeline stages and workflow
•   Uses a structured syntax (Declarative or Scripted)
•   Supports automation and version control
Benefits:
•   Ensures consistency across builds
•   Enables versioning and tracking of pipeline changes
•   Improves collaboration among team members
Thus, Jenkinsfile is a key component of the Pipeline-as-Code concept.
********** 11 **********
--- page 12 ---
B   With proper block diagram explain about Continuous Integration (CI).
For proper explanation and block diagram (2.5+2.5) total 5 Marks
Continuous Integration (CI) is a software development practice that makes sure
developers integrate their code into a shared repository as and when they are done
working on the feature. Each integration is verified by means of an automated build
process that allows teams to detect problems in their code at a very early stage rather
than finding them after the deployment.
CO-1;
SO-6;   5
BL-1,2
Based on the above flow, we can have a brief overview of the CI process.
•   Developers regularly check out code into their local workspaces and work on
the features assigned to them.
• Once they are done working on it, the code is committed and pushed to the
remote shared repository which is handled by making use of effective version
control tools like git.
•   The CI server keeps track of the changes done to the shared repository and it
pulls the changes as soon as it detects them.
•   The CI server then triggers the build of the code and runs unit and integration
test cases if set up.
• The team is informed of the build results. In case of the build failure, the team
has to work on fixing the issue as early as possible, and then the process
repeats.
C   Explain three main components of Docker architecture.
1) Docker Client (1.5 Marks)
• The Docker Client is the interface through which users interact
with Docker.
• It uses commands like docker build, docker run, docker pull.
CO-2,3;   • Sends requests to the Docker Daemon to perform operations.
2) Docker Daemon (Docker Engine) (2 Marks)
SO-6;   5
BL-2,3   • The Docker Daemon is the core component that runs in the background.
• It is responsible for building images, running containers, and managing
Docker objects.
•Listens to API requests from the Docker Client and executes them.
3) Docker Registry (1.5 Marks)
• A Docker Registry is a storage system for Docker images.
• Images can be pushed (uploaded) and pulled (downloaded) from the registry.
• Example: Docker Hub
********** 12 **********

[Text in pictures on this page, read by OCR]
Build and test results are fed back to the developers

¥

Jenkins check the Jenkins deploy the
shatec repository at build application the build application is
periocic intervals and onthe test server then deployed to the
every check inis production server
pullec and then build
--- page 13 ---
D   Describe the Git workflow. Explain the stages from working directory
to repository with suitable commands.
Workflow Explanation (3 Marks):
CO-1,2;
Working Directory → Staging Area → Repository.
SO-5;   Changes are made, staged using git add, and committed using git commit.   5
BL-2,3   Commands (2 Marks):
git add, git commit, git status.
********** 13 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 9b220d12d399

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_AI_7051/Agile Product Development with DevOps/ANS_Agile Product Development with DevOps(702AI0C022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (13 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Agile Product Development with DevOps
Date: 04 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 13 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. Answer to each new question to be started on a fresh page.
5. Figure in right hand side indicates full marks.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
a.   Elaborate the need of Agile Software Development.
Agile Software Development (2 Marks )and Its Need –(3 Marks)
Agile Software Development is a software development methodology that focuses on:
Flexibility
Collaboration
Customer satisfaction
It is based on the Agile Manifesto, which emphasizes:
•   Individuals and interactions over processes and tools
CO-1 ;   •   Working software over comprehensive documentation
SO-6 ;   •   Customer collaboration over contract negotiation   5
•   Responding to change over following a plan
BL-1
Need for Agile
Agile is needed because:
•   Requirements change frequently in real-world projects
•   Faster delivery is required
•   Customer feedback is essential
•   Traditional models are rigid and slow
•   It improves product quality through continuous testing and feedback
•   Agile Development Models
b.   Explain the recursive merge of git branching.
1) Definition (2 Marks)
Recursive merge is the default merge strategy used by Git when merging two
CO-1,2 ;   branches. It is mainly used when branches have diverged and may have multiple
SO- 6;   5
common ancestors. Git recursively finds a common base (merge base) and merges
BL-2,3
changes accordingly.
2) Working of Recursive Merge (2 Marks)
Git identifies the common ancestor commit of both branches.
********** 1 **********
--- page 2 ---
Compares changes from both branches with the base.
Automatically merges non-conflicting changes.
•   If conflicts occur, Git marks them for manual resolution.
• Can handle complex histories by performing repeated (recursive) merges.
3) Key Feature (1 Mark)
Produces a three-way merge (base + two branches), ensuring accurate integration of
changes
c.   Explain authentication and authorization in Jenkins security.
Marking Scheme (Step-wise)
o   Authentication explanation – 2M
o   Authorization explanation – 2M
o   Difference between both – 1M
Model Answer
Jenkins security is based on two key concepts: authentication and authorization.
Authentication
Authentication is the process of verifying the identity of a user.
•   Ensures that only valid users can access Jenkins
•   Methods include:
•   Jenkins internal database
CO- 1,2;   • LDAP integration
SO- 6;   5
•   Single Sign-On (SSO)
BL-3,4
Authorization
Authorization determines what actions a user is allowed to perform after
authentication.
Defines permissions such as read, write, or admin access
Implemented using strategies like:
•   Role-based access
•   Matrix-based security
Difference
•   Authentication: Verifies identity
•   Authorization: Grants permissions
d.   Differentiate between Docker Create , Docker Start and Docker Run
commands.
CO-2,3 ;
Feature   docker create   docker start   docker run   5
SO- 6;
BL-2,3
Primary   Creates a new   Restarts an existing   Creates a new
Action   container from an   container that is   container
********** 2 **********
--- page 3 ---
image without   currently in a stopped   and starts it
starting it.   state.   immediately.
Containe   Generates a new   Uses a previously   Generates a new
r ID   container ID and   assigned container ID   container ID upon
prints it to the   or name.   creation.
terminal.
State   Image → Created   Stopped → Running.   Image → Running.
Change   (Stopped).
Resource   Prepares the   Allocates CPU and   Allocates all
s   filesystem and   RAM to the existing   necessary
configuration but   container process.   resources and
consumes no   executes the
CPU/RAM.   startup command.
Configur   Allows full   Reuses the   Allows full
ation   configuration   configuration defined   configuration
(ports, volumes,   when the container   (ports, volumes,
env) during   was first created.   env) during the
creation.   run command.
Typical   Setting up a   Resuming work in a   The "go-to"
Use Case   complex   container where you   command for
configuration   want to keep previous   launching fresh
ahead of time to   file changes.   instances of an
start later.   application.
A   An online fashion retailer wants to frequently update its mobile app with
new features such as discount coupons, live tracking and personalized
recommendations. Explain why Agile is suitable for this project and how
Q.2   Iterative Development benefits the organization.
CO-1 ;   10
SO-6 ;
An online fashion retailer has a big scope in business as it is the sector which will
BL-1   always be in demand. It operates in a highly dynamic and competitive environment
where customer preferences, trends, and technologies change rapidly. In such a
scenario, adopting the Agile methodology is highly suitable for developing and
updating the mobile app.
Why Agile Process is Suitable :
********** 3 **********
--- page 4 ---
Agile Process is a flexible and adaptive software development approach that
emphasizes proper planning, continuous improvement, customer feedback, and rapid
delivery. It is well-suited for this project due to the following reasons:
1. Frequent Requirement Changes
Features like discount coupons, live tracking, and personalized
recommendations may evolve based on customer behavior , feedback and
market trends. Agile allows easy incorporation of changing requirements
even at later stages of development as per the requirements.
2. Faster Time-to-Market
Agile delivers the application in small increments (sprints), enabling the
retailer to release new features quickly. This helps the company stay
competitive by continuously enhancing user experience as well as keep them
informed and notified.
3. Customer-Centric Approach
Agile promotes regular feedback from users. The retailer can analyze user
reviews and app usage data to refine features like recommendations and
offers.
4. Improved Collaboration
Agile encourages close collaboration between developers, designers,
marketing teams, and stakeholders. This ensures that business goals like
increasing sales through discounts align with technical development.
5. Risk Reduction
Since development happens in small cycles, issues are identified and
resolved early. This minimizes the risk of major failures in the app.
How Iterative Development Benefits the Organization
Iterative Development is a core principle of Agile where the product is developed and
refined through repeated cycles (iterations). Its benefits include:
1. Continuous Improvement
Each iteration builds upon the previous version, allowing gradual
enhancement of features such as recommendation algorithms and tracking
systems.
2. Early Delivery of Value
The retailer can release basic features (e.g., simple discount coupons) early
and then enhance them (e.g., AI-based personalized coupons) in future
iterations.
3. Better Quality Assurance
Testing is performed in every iteration, ensuring bugs are detected early and
the app remains stable and reliable.
4. Adaptability to User Feedback
User feedback from one iteration can be incorporated into the next, ensuring
the app evolves according to customer needs.
5. Efficient Resource Utilization
The development team can prioritize high-value features first, ensuring
optimal use of time and resources.
B   Explain in details about the different phases in DevOps methodology
and how it is related with continuous integration?
DevOps is a combination of practices that help teams deliver software faster and more
reliably. It has several phases that work together like a loop, not a straight line. There
CO-1;
SO-6;   are 6 phases of DevOps methodology:   10
BL-1,2   Planning: The first step where everyone comes together to understand the project
requirements and goals. The aim is to set a clear direction for development. This phase
ensures that the team knows what needs to be done and how to manage the entire
process. Tools like Google Apps or Asana help in organizing tasks and keeping the
team aligned.
********** 4 **********
--- page 5 ---
Development: This is when the actual coding happens. Developers write the code,
create features, and define tests. The code is stored in a shared place called a
&quot;repository&quot; where the team can work together, make changes, and track
different versions of the code. Think of it as building the product step-by-step. Tools
like Git, Eclipse, or IntelliJ help developers collaborate efficiently.
Continuous Integration (CI): After developers write the code, this phase helps
automate checking, testing, and building the software. It ensures that changes don’t
break anything and that the system is working smoothly from the start. It’s like a quality
check to catch issues early. Jenkins or CircleCI are used for this automated process.
Deployment: Once the code is ready, it&#39;s time to release it. This phase
automates the process of making the code live, which means the product gets updated
automatically without needing manual intervention. Cloud services, like AWS or
Azure, help in managing these deployments and scaling the product as needed.
Operations: This phase happens continuously throughout the product’s life. The team
keeps an eye on the software, making sure it’s running smoothly. Operations include
maintaining the infrastructure, handling issues, and ensuring the software is available
and scalable. Tools like Loggly or AppDynamics are used to monitor the performance
of the product.
Monitoring: The final phase is all about keeping track of the software’s performance
and health. It’s an ongoing process where the team watches for any problems, collects
data, and analyses how the software is performing. This helps identify areas for
improvement. Tools like Nagios or Splunk are used for monitoring the system’s status
and fixing any issues that arise.
A
A startup is using GitHub for managing a machine learning project.
They face the following issues:
• Sensitive files are accidentally committed.
• Developers want to ignore certain files permanently.
• The team wants to review code before merging.
• A developer wants to undo a commit but keep the changes.
Q.3
• They need to maintain a clean and understandable commit
CO-1,2;   10
SO-5;   history.
BL-3   a) What is .gitignore and why is it important?
b) What is a pull request and its benefits?
c) Which command is used to undo the last commit but keep changes?
d) Why are meaningful commit messages important?
e) How can sensitive files be removed from tracking?
a) .gitignore (3 Marks):
File used to ignore unwanted files (e.g., logs, temp files). Prevents unnecessary or
sensitive files from being tracked.
********** 5 **********
--- page 6 ---
b) Pull request (2 Marks):
A request to merge changes into main branch after review; improves code quality and
collaboration.
c) Undo last commit (2 Marks):
git reset --soft HEAD~1 – removes commit but keeps changes.
d) Commit messages importance (2 Marks):
Helps understand changes and maintain clear project history.
e) Remove sensitive files (1 Mark):
Use git rm --cached <file>.
B   A project requires automation of build, test, and deployment across multiple
environments. Explain how Jenkins Pipeline concepts (Pipeline, Stage, Node, Step) can
be used to design this workflow.
Marking Scheme (Refined)
•   Introduction to pipeline concept – 2M
•   Explanation of components (Pipeline, Stage, Node, Step) – 4M
•   Workflow explanation across environments – 2M
•   Advantages – 2M
Detailed Model Answer
Jenkins Pipeline is a framework that allows defining and automating the CI/CD
workflow as code. It organizes the process into logical components that enable efficient
execution across multiple environments.
Pipeline Concept
A pipeline represents the entire workflow of building, testing, and deploying an
application. It defines the sequence of operations required for software delivery.
Key Components
1. Pipeline
CO-1,2;   •   Represents the complete CI/CD process
SO-6;   •   Defines the overall workflow   10
BL-2,3   2. Stage
•   Divides the pipeline into logical phases
•   Examples: Build, Test, Deploy
3. Node
•   Represents the execution environment (agent)
•   Executes tasks on specific machines or environments
4. Step
•   Individual tasks performed within a stage
•   Example: running tests, compiling code
Workflow Across Environments
1. The pipeline is triggered when code is committed
2. The Build stage compiles the application
3. The Test stage validates functionality
4. The Deploy stage deploys to different environments (e.g., staging, production)
5. Each stage runs on appropriate nodes based on environment requirements
Advantages
•   Automates entire workflow
•   Ensures consistency across environments
A   Explain in detail every step in Container Lifecycle and support your
Q.4
answer with a diagram. Also explain any 3 commands for Container   10
CO-2,3;
SO-6;   Management.
********** 6 **********
--- page 7 ---
BL-1,2   Marking Scheme (Step-wise)
•   Steps – 6M
•   Diagram – 2.5M
• command – 1.5 M
Container Lifecycle Stages
Image Build/Pull: The process starts by obtaining a container image from a registry
(like Docker Hub) or building one using a Dockerfile.
Created (Created State): The docker create command creates a thin writable container
layer over the image, preparing the file system, but the application does not start.
Running (Running State): The docker start command launches the container's main
process. The docker run command combines creation and starting into a single step.
Paused (Paused State): The docker pause command freezes all processes within the
container using cgroups.
Stopped (Stopped State): The docker stop command (graceful shutdown) or docker kill
command (abrupt shutdown) shuts down the primary process, halting execution. The
container remains as a resource.
Deleted (Deleted State): The docker rm command removes the container, freeing its
resources and deleting the writable layer.
Container Management Commands
docker run -d --name my-app nginx
docker ps / docker ps -a
docker stop <container_id>
docker rm <container_id>
B   What is a Pod in Kubernetes? Describe the various phases of the Pod
CO-3;   lifecycle in detail and explain the significance of each phase.
SO-6;   What is pod – 2 Marks   10
BL-2,3
Explain & significance - 8 Marks
Pods are the smallest deployable units in Kubernetes.
********** 7 **********
--- page 8 ---
A pod is just a wrapper around the container.
A Pod is a group of one or more containers, with shared storage and network
resources and a unique IP address.
It contains one or more application containers that are relatively tightly coupled and
use the shared volume.
A pod contains just a single container in a more common use case.
A Pod is not a process, but an environment for the running container(s).
A Kubernetes Pod follows a defined lifecycle, moving through a sequence of five
main phases: Pending, Running, Succeeded, Failed, and Unknown. These phases offer
a high-level summary of the Pod's status within the cluster.
Phases of a Pod Lifecycle
Pending: The Pod is accepted by Kubernetes but waiting for containers to be created or
pulled. This indicates it is waiting for scheduling, image pulling, or volume mounting.
Running: The Pod is bound to a node, with all containers created and at least one
running, starting, or restarting. This is the normal operational state for services.
Succeeded: All containers terminated successfully (exit code 0) and will not restart,
typical for completed jobs.
Failed: All containers terminated, with at least one failing (non-zero exit code),
signaling an application error. Depending on restartPolicy,   it may enter
CrashLoopBackOff.
Unknown: The control plane cannot determine the Pod's status, usually due to node
communication issues.
A   Explain Nagios Plugins (NRPE) and Objects, Nagios Commands and
Notification.
Nagios Plugins and objects – 5 Marks
Nagios Commands and Notification - 5 Marks
Nagios Plugins (NRPE)
Small executable programs/scripts used to check services, hosts, and resources.
Q.5   Plugins return data to Nagios in the form of:
OK
CO-4;   10
WARNING
SO-6;
BL-2,3,4   CRITICAL
UNKNOWN
Can check both local and remote resources.
Examples: check_disk, check_ping, check_http, etc
Nagios Objects
Objects are the fundamental building blocks of the Nagios configuration, defined in
text-based configuration files. Key object types include:
Hosts: Physical devices on your network (servers, routers, switches).
********** 8 **********
--- page 9 ---
Services: Specific aspects or characteristics of a host being monitored (e.g., memory
usage, number of logged-in users, or network services like SMTP or HTTP).
Contacts: The people or entities that receive notifications.
Host Groups/Service Groups: Logical groupings of hosts or services to simplify
configuration and management.
Timeperiods: Define specific time ranges during which monitoring checks or
notifications are active (e.g., 24x7, business hours)
Nagios Commands
Commands are definitions that tell Nagios exactly which programs or scripts to run for
various tasks. Defined in commands.cfg
Check Commands: Used to determine the status of hosts and services.
Notification Commands: Executed to send alerts (e.g., a command to send an email via
mailx).
Event Handlers: Scripts triggered automatically when a host or service changes state
(e.g., restarting a failed service).
Nagios Notifications
Notifications are alerts sent when a host or service enters a "hard" problem state or
recovers.
Filters: Before sending a notification, Nagios passes it through filters like scheduled
downtime, flap detection, and notification periods.
Methods: Alerts can be sent via email, SMS, pager, or integrated with third-party tools
like PagerDuty or xMatters.
Escalations: If an issue remains unresolved, notifications can be "escalated" to different
contacts or groups
B   Explain the key features of Kubernetes. Also, differentiate between a
Pod and a container.
Key Features of Kubernetes – 7 Marks
Difference – 3 Marks
Kubernetes is a powerful container orchestration platform with the following key
features:
Container Orchestration
CO-3;   Automates deployment, scaling, and management of containerized applications.
SO-6;   10
Auto Scaling
BL-2,3
Automatically scales applications up or down based on CPU usage or custom
metrics.
Self-Healing
Detects and replaces failed containers, restarts crashed containers, and reschedules
t
them on healthy nodes.
Service Discovery & Load Balancing
Provides built-in DNS and load balancing to distribute traffic among containers.
********** 9 **********
--- page 10 ---
Rolling Updates & Rollbacks
Enables seamless updates of applications without downtime and allows rollback to
previous versions if needed.
Storage Orchestration
Automatically mounts storage systems like local storage, NFS, or cloud storage.
Configuration Management
Manages configuration using ConfigMaps and sensitive data using Secrets.
Batch Execution
Handles batch jobs and scheduled tasks using Jobs and CronJobs.
Multi-Cloud & Hybrid Support
Can run across on-premises, public cloud, or hybrid environments.
Aspect   Pod   Container
Smallest deployable unit in   Lightweight, standalone
Definition
Kubernetes   executable package
Composition Can contain one or more containers Single application instance
Purpose   Manages and groups containers   Runs application code
Shares same IP address and network Has its own isolated
Networking
namespace   environment
Shares volumes among containers   Has isolated filesystem (unless
Storage
in the same pod   shared)
Managed by container runtime
Lifecycle   Managed by Kubernetes
(e.g., Docker)
Used for deploying applications in Used to package and run
Usage
Kubernetes   applications
A   Describe the components of Prometheus architecture and explain their
roles in monitoring systems.
Components – 6Marks
Role in Monitoring – 4Marks
Prometheus is a popular open-source monitoring and alerting system written in
Golang, capable of collecting and processing metrics from various targets.
Prometheus primarily consists of the following.
Q.6   •   Prometheus Server
•   Service Discovery
CO-3,4;   •   Time-Series Database (TSDB)   10
SO-6;   •   Targets
•   Exporters
BL-2,3
•   Push Gateway
•   Alert Manager
•   Client Libraries
• PromQL
Roles in Monitoring
•   Data Collection (Pull Model): Unlike push-based systems, Prometheus
actively scrapes targets, making it easy to detect when a target goes down.
•   Metric Storage: The TSDB allows fast, time-series-focused storage of numeric
metrics, supporting multi-dimensional data.
•   Alerting and Notification: Prometheus periodically evaluates configured rules,
triggering alerts sent to the Alert manager for notification processing.
********** 10 **********
--- page 11 ---
•   Visualization: Through   the HTTP API, data   is exposed   to   tools
like Grafana for dashboards.
B   Differentiate between Scrum, Extreme Programming and Lean Agile
Development Models. Also mention examples for each model.
•   Comparison/Differences: 7 marks
•   Examples:3 marks
Extreme
Aspect   Scrum   Lean Development
Programming (XP)
Project   Process
Focus   management   Engineering practices   optimization &
framework   waste reduction
Iterative with strong
Approach   Iterative (Sprints)   Continuous flow
coding practices
Product Owner,
Key Roles   Scrum Master,   No strict roles   No strict roles
CO-1 ;   Team
SO-6 ;   Daily stand-up,   Pair programming,   10
Eliminate waste,
BL-1   Practices   sprint planning,   TDD, continuous
fast delivery
review   integration
Documentat
Minimal   Minimal   Minimal
ion
Flexibility   Moderate   High   Very high
Delivery   Fixed sprint (2–4
Frequent releases   Continuous delivery
Cycle   weeks)
• Scrum Example:
A software company developing a mobile app uses 2-week sprints with daily
stand-ups and sprint reviews.
•   Extreme Programming (XP) Example:
A development team uses pair programming and Test-Driven Development
(TDD) to build a banking system.
•   Lean Development Example:
A startup focuses on eliminating unnecessary features and delivering only
value-added functionalities quickly.
A   Write a short note on Jenkinsfile and explain its benefits.
Marking Scheme (Step-wise)
•   Definition – 2M
• Key features – 2M
•   Benefits – 1M
Model Answer
Q.7   A Jenkinsfile is a text file that defines the CI/CD pipeline as code.
It is stored in the version control repository along with the application code and
CO-1,2;   contains instructions for building, testing, and deploying the application.   5
SO-6;   Key features:
BL-2,3,4   •   Defines pipeline stages and workflow
•   Uses a structured syntax (Declarative or Scripted)
•   Supports automation and version control
Benefits:
•   Ensures consistency across builds
•   Enables versioning and tracking of pipeline changes
•   Improves collaboration among team members
Thus, Jenkinsfile is a key component of the Pipeline-as-Code concept.
********** 11 **********
--- page 12 ---
B   With proper block diagram explain about Continuous Integration (CI).
For proper explanation and block diagram (2.5+2.5) total 5 Marks
Continuous Integration (CI) is a software development practice that makes sure
developers integrate their code into a shared repository as and when they are done
working on the feature. Each integration is verified by means of an automated build
process that allows teams to detect problems in their code at a very early stage rather
than finding them after the deployment.
CO-1;
SO-6;   5
BL-1,2
Based on the above flow, we can have a brief overview of the CI process.
•   Developers regularly check out code into their local workspaces and work on
the features assigned to them.
• Once they are done working on it, the code is committed and pushed to the
remote shared repository which is handled by making use of effective version
control tools like git.
•   The CI server keeps track of the changes done to the shared repository and it
pulls the changes as soon as it detects them.
•   The CI server then triggers the build of the code and runs unit and integration
test cases if set up.
• The team is informed of the build results. In case of the build failure, the team
has to work on fixing the issue as early as possible, and then the process
repeats.
C   Explain three main components of Docker architecture.
1) Docker Client (1.5 Marks)
• The Docker Client is the interface through which users interact
with Docker.
• It uses commands like docker build, docker run, docker pull.
CO-2,3;   • Sends requests to the Docker Daemon to perform operations.
2) Docker Daemon (Docker Engine) (2 Marks)
SO-6;   5
BL-2,3   • The Docker Daemon is the core component that runs in the background.
• It is responsible for building images, running containers, and managing
Docker objects.
•Listens to API requests from the Docker Client and executes them.
3) Docker Registry (1.5 Marks)
• A Docker Registry is a storage system for Docker images.
• Images can be pushed (uploaded) and pulled (downloaded) from the registry.
• Example: Docker Hub
********** 12 **********

[Text in pictures on this page, read by OCR]
Build and test results are fed back to the developers

¥

Jenkins check the Jenkins deploy the
shatec repository at build application the build application is
periocic intervals and onthe test server then deployed to the
every check inis production server
pullec and then build
--- page 13 ---
D   Describe the Git workflow. Explain the stages from working directory
to repository with suitable commands.
Workflow Explanation (3 Marks):
CO-1,2;
Working Directory → Staging Area → Repository.
SO-5;   Changes are made, staged using git add, and committed using git commit.   5
BL-2,3   Commands (2 Marks):
git add, git commit, git status.
********** 13 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 145c761313a4

- Departments: AI and Data Science
- Programmes: BTech AIDS 7056
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_AIDS_7056/Agile Product Development with DevOps/ANS_Agile Product Development with DevOps(702AI0C022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Agile Product Development with DevOps
Date: 30 Jun 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. Answer to each new question to be started on a fresh page.
5. Figure in right hand side indicates full marks.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
CO- 1;   a Explain Prototyping Model in detail. Support your answer with diagram.
SO-6;   5
BL-1   Phases – 4 Marks
Diagram -1 Mark
In the Prototyping Model, an initial prototype (a working version) of the
software is built and refined through multiple iterations based on user
feedback.
Phases of Prototyping Model:
1. Requirement Gathering – Collect initial requirements.
2. Quick Design – Create a basic system structure.
3. Prototyping – Develop a working prototype.
4. User Evaluation – Get feedback from users.
5. Refinement – Improve the prototype based on feedback.
6. Final Development – Convert the refined prototype into a full
system.
********** 1 **********

[Text in pictures on this page, read by OCR]
Build Prototype

va Ne customer

Requirements
. . Cust satisfied .
Gathering —> Quick Design Evaluation of Design
Prototype J
x / Implement
Refine a5
Requirements

Test

Maintenance
--- page 2 ---
CO-1,2;   b
SO- 5;   Explain the purpose and usage of the following Git commands with   5
BL-2,3   examples: git init, git add, git commit, and git status.
Commands Explanation (4 Marks):
• git init – Initializes a repository (1 Mark)
• git add – Stages changes (1 Mark)
• git commit – Saves changes with message (1 Mark)
• git status – Shows file status (1 Mark)
Example (1 Mark):
git init → git add file.txt → git commit -m "Initial commit"
CO-1,2;   c
Explain the process of plugin installation and upgrade in Jenkins.   5
SO-6;
BL-3,4   Marking Scheme (Step-wise)
• Definition/role of plugins – 1Mark
•   Installation process – 2Marks
• Upgrade process – 1.5Marks
• Importance/benefits – 0.5Marks
Model Answer
Jenkins plugins are extensions that enhance the functionality of Jenkins by
enabling integration with various tools and adding new features.
Plugin Installation Process
Plugins can be installed using the Jenkins Plugin Manager:
• Navigate to “Manage Jenkins”
•   Select “Manage Plugins”
• Search for the required plugin
•   Select and install the plugin
•   Restart Jenkins (if required)
This allows Jenkins to support additional tools like version control systems,
cloud services, and build tools.
Plugin Upgrade Process
Jenkins periodically checks for plugin updates.
• Go to Plugin Manager
• View available updates
•   Select plugins to upgrade
•   Install updates and restart Jenkins
Importance
• Enhances Jenkins capabilities
• Keeps system updated and secure
• Enables integration with modern tools
********** 2 **********
--- page 3 ---
Thus, plugin management is essential for maintaining an efficient CI/CD
environment.
CO-2,3;   d
SO-6 ;   How Docker images and containers are created and managed in Docker   5
BL-2,3   Environment?
How – 2.5 Marks
Managed – 2.5 Marks
Creating and Managing Docker Images
Docker images are read-only, immutable templates that serve as blueprints
for containers.
Creation (Build):
Dockerfile: Developers write a Dockerfile containing sequential instructions
(e.g., FROM, RUN, COPY, CMD) to assemble the image.
Layered Architecture: Each instruction in a Dockerfile creates a new layer.
This makes images lightweight as layers can be cached and reused across
different images.
Build Command: Running docker build -t image_name:tag . compiles the
Dockerfile into a usable image.
Management:
Storage (Registries): Images are stored and shared in Docker Registries, with
Docker Hub being the default public option.
Listing & Removal: Users view local images with docker images and can
remove unused ones with docker rmi image_name to save space.
Versioning: Images are managed using tags (e.g., ubuntu:22.04) to
distinguish between different versions.
2. Creating and Managing Docker Containers
A container is a live, runnable instance of an image that includes an additional
writable layer for temporary data.
Creation and Execution:
Run Command: The command docker run <image_name> pulls the image if
it's missing, creates the container, and starts it immediately.
Create Command: Alternatively, docker create <image_name> prepares a
********** 3 **********
--- page 4 ---
container in a "Created" state without starting it.
Lifecycle Management:
States: Containers transition through several states: Created (ready), Running
(active), Paused (processes frozen), Stopped (shutdown gracefully), and
Deleted (removed).
Control Commands:
docker start/stop: Initiates or halts a container.
docker pause/unpause: Suspends or resumes container processes without a
full shutdown.
docker rm: Permanently removes a stopped container.
Q2   a   10
CO-1;   A large enterprise with 40+ teams is transitioning from Waterfall to
SO-6;   Agile. Some teams follow Agile strictly, while others resist change.
BL-1   Integration issues and inconsistent practices are causing project delays.
Analyze the challenges of scaling Agile. How can an Agile mindset,
principles, and   coordination mechanisms improve   large-scale
development?
Analyze the challenges – 5Marks
How – 5 Marks
Transitioning a large enterprise with 40+ teams from Waterfall to Agile
is a complex, high-stakes endeavor that involves navigating deep-seated
cultural resistance and technical hurdles. The scenario described—some
teams practicing Agile strictly while others resist—indicates a lack of
consistent, organizational-level adoption (or "agile theater").
Challenges of Scaling Agile (40+ Teams)
Scaling Agile goes beyond just applying Scrum; it requires addressing
structural, cultural, and technical bottlenecks.
• Deep Cultural Resistance & "Agile Theater": Resistance often
stems from fear of job insecurity, loss of control by managers, and
comfort with old processes. When change is forced rather than
adopted, organizations may exhibit "agile theater," where teams go
through the motions (e.g., daily stand-ups) without actually
following agile principles.
********** 4 **********

[Text in pictures on this page, read by OCR]
AGILE MANIFESTO

FOUR CORE VALUES & TWELVE PRINCIPLES

Deliver Early & Often
Embrace Change 4 1.

Release Frequently
Collaborate Daily ¢ > 02. hoch
Empower Teams Working software

Talk Face-to-Face over comprehensive documentation
Measure by Working Software 03. Castomer:
Maintain Sustainable Pace Fone a fern
Focus on Quality 04.
Keep It Simple Poi ron beri

Trust Self-Organizing Teams
Reflect & Improve
--- page 5 ---
Integration Issues & Hidden Dependencies: As described, multiple
teams working on a single project create significant dependencies,
causing "module integration issues" and code quality problems. A lack
of unified, automated testing (CI/CD) makes integrating 40+ teams' work
extremely challenging
•   Inconsistent Practices & Low Maturity: When some teams are
"strict" and others are not, it leads to communication failures and
misalignment in delivery, resulting in inconsistent practices.
•   "Wagile" or "Scrumfall" Behaviour: Many teams end up in a
hybrid state where they use short-term Sprints but keep long-term, fixed,
rigid Waterfall planning.
•   Lack of Leadership Support: A common failure factor is when
senior management advocates Agile but does not change the traditional
"command-and-control" management style.
Improving Large-Scale Development
To overcome these challenges, a shift in mindset, reinforced by proper
structure, is required.
1. Fostering an Agile Mindset and Principles
•   Leadership Alignment and Servant Leadership: Leaders must stop
managing tasks and start enabling teams. This involves transitioning
from "command-and-control" to "servant leadership," where managers
remove impediments for teams.
•   Create a Culture of Psychological Safety: A blameless
environment is needed to encourage learning from mistakes, rather than
punishing teams for delays that are often the result of complex, systemic
issues.
•   Focus on Value, Not Velocity: Teams should be trained to focus
on delivering valuable, working software to customers, rather than just
maximizing "story points".
2. Coordination Mechanisms for Scale
•   Scaled Agile Frameworks (e.g., SAFe, LeSS): For 40+ teams, a
structured framework   is   essential to coordinate dependencies.
Techniques like a "Master Product Backlog" or "Scrum of Scrums"
provide an overview of all products and align team goals.
• Communities of Practice (CoPs): To harmonize inconsistent
practices, create CoPs where developers, Scrum Masters, and
Product Owners from different teams meet voluntarily to share
best practices, tools, and lessons learned.
•   Cross-functional and Self-organizing Teams: Break down silos by
ensuring teams are truly cross-functional (including testers,
developers, and designers) so they can complete a user story
without depending on external teams.
********** 5 **********
--- page 6 ---
• Automated Continuous Integration (CI/CD): To solve integration
issues, automated integration testing must be implemented to
ensure that code from different teams can be tested immediately,
reducing "late-discovery" defects.
• Agile Training and Dedicated Coaching: Invest in professional
training for all levels—not just developers—to ensure a common
understanding of Agile values, mitigating resistance caused by a
lack of knowledge.
CO-1;   b
What is the essential preparation requiring before starting a new project on 10
SO-6;   DevOps platform, and how can each step be detailed?
BL-1,2
For each point of explanation require 2 marks total 5X2=10 marks
Preparing for a new project on a DevOps platform requires a holistic
approach that aligns culture, processes, and tools before code is written.
Essential preparations include creating a strategy, building a cross-functional
team, automating infrastructure, setting up CI/CD pipelines, and establishing
monitoring.
1. Define Strategy and Goals (Planning Phase)
Before selecting tools, define what success looks like to ensure the project
aligns with business objectives.
•   Create a DevOps Roadmap: Develop a step-by-step transformation
plan. Document this roadmap in a central, accessible location (like
Confluence or Jira) to keep all stakeholders aligned.
•   Establish Key Performance Indicators (KPIs): Define metrics like
Deployment Frequency, Lead Time for Changes, Mean Time to Recovery
(MTTR), and Change Failure Rate.
•   Adopt Agile Project Management: Structure the work using Agile
methodologies (Scrum/Kanban) to break the project into small, manageable
sprints.
2. Build and Train the Team (Cultural Preparation)
DevOps is a cultural shift, not just a technical one.
•   Assemble Cross-Functional Teams: Combine developers, operations
engineers, QA, and security specialists into a single team with shared
responsibility.
•   Foster Collaboration: Set up communication channels (e.g., Slack,
Teams) to break down silos. Implement "You build it, you run it"
ownership.
•   Conduct Training Workshops: Ensure the team is proficient in new
tools, Git branching models, and security practices.
3. Select and Setup the Toolchain
Choose a set of integrated tools rather than attempting to buy one single
"DevOps product".
•   Version Control Setup (Git): Create a source code repository
(GitHub, Bitbucket) and define a branching strategy (e.g., GitHub Flow or
Trunk-Based Development).
********** 6 **********
--- page 7 ---
•   Infrastructure as Code (IaC): Prepare to use tools like Terraform or
Ansible to define infrastructure in text-based configuration files, allowing
repeatable and auditable deployments.
•   Tool Integration: Integrate work tracking (Jira) with source control
(Bitbucket/GitLab) to provide full visibility from planning to deployment.
4. Implement CI/CD and Testing Frameworks
Automating the building, testing, and deployment of code is essential.
•   Continuous Integration (CI): Establish automated pipelines (Jenkins,
GitHub Actions) that pull code, run tests, and build artifacts immediately
after a commit.
•   Automated Testing Setup: Create a repository of unit, integration,
and security tests that run automatically on every pull request.
•   Continuous Delivery (CD): Ensure the code is always in a deployable
state by automating the promotion of code to staging and production
environments.
5. Establish Operational Readiness (Monitoring & Security)
The project should be observable and secure from the start.
•   Set Up Continuous Monitoring: Implement logging and monitoring
tools (Prometheus, Grafana, ELK Stack) to monitor application
performance and system health.
•   Create Runbooks: Document operational procedures to guide the
team in resolving common issues.
•   Embed Security (DevSecOps): Integrate security scanning
(SAST/DAST) directly into the CI/CD pipeline. Use a secrets management
system rather than storing keys in code.
Q3   a A DevOps team is managing a project using Git and remote repositories.   10
CO-1,2;   They encounter:
SO-5;   • Difficulty syncing local and remote repositories.
BL-3   • Confusion between git fetch and git pull.
• The need to revert to a previous stable version.
• Multiple versions of code needing proper tracking.
• The requirement to collaborate efficiently across teams.
a) Differentiate between git fetch and git pull.
b) How can the project be reverted to a previous version safely?
c) Which commands are used to sync local and remote repositories?
d) How does Git help in version tracking?
e) Why is Git suitable for collaborative development?
a) Fetch vs Pull (3 Marks):
git fetch downloads changes without merging;
git pull downloads and merges changes.
b) Revert to previous version (2 Marks):
Use git revert or git checkout <commit_id>.
c) Sync commands (2 Marks):
git push and git pull.
d) Version tracking (2 Marks):
Git tracks all changes with commits, allowing history and rollback.
********** 7 **********
--- page 8 ---
e) Collaboration (1 Mark):
Enables multiple developers to work simultaneously efficiently.
CO-1,2;   b A team wants to monitor and visualize their CI/CD workflow clearly.   10
SO-6;   Explain how Jenkins Delivery Pipeline helps in visualization and
BL-2,3   management of different stages.
Marking Scheme (Refined)
•   Introduction to Delivery Pipeline – 2M
•   Explanation of stages (commit, test, deploy) – 3M
•   Visualization and working mechanism – 3M
•   Benefits and practical importance – 2M
Model Answer
Jenkins Delivery Pipeline is a visualization tool that provides a clear
graphical representation of the Continuous Delivery process. It helps teams
monitor and manage different stages of the CI/CD workflow.
Concept of Delivery Pipeline
A delivery pipeline represents the flow of software from code commit to
deployment. It organizes the workflow into multiple stages such as build,
test, and deployment. Each stage contains one or more tasks (jobs), and the
pipeline shows how these stages are connected.
Stages in Delivery Pipeline
1. Commit Stage
• Code is integrated into the repository
•   Initial build and basic tests are performed
2. Test Stage
• Advanced testing such as integration and system testing
• Ensures application quality
3. Deployment Stage
•   Application is deployed to staging or production environment
•   Final validation before release
Visualization and Working
• The Delivery Pipeline plugin displays all stages in a pipeline view
• Each stage is represented visually with status indicators
(success/failure)
•   It shows the flow from one stage to another
•   Provides real-time updates of pipeline progress
This helps teams easily track:
•   Current stage of execution
•   Failed stages
•   Latest successful builds
Benefits
• Improves visibility of CI/CD process
• Helps identify bottlenecks quickly
• Enhances team collaboration
•   Provides better monitoring and control
********** 8 **********
--- page 9 ---
Q4   a
What is a Dockerfile? Explain its structure and commonly used instructions   10
(FROM, RUN, CMD, COPY, etc.) with an example.
What – 1 Mark
Structure – 3 Marks
Instructions & example - 6
A Dockerfile is a script containing instructions to build a Docker image.
Sample Dockerfile:
FROM node:14
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "app.js"]
Explanation:
• FROM → base image
• WORKDIR → working directory
• COPY → copy files
• RUN → install dependencies
CO-2,3;   • CMD → run application
SO-6;
BL-1,2   Dockerfile automates image creation.
Command   Purpose
docker   Starts all services in detached (background) mode.
compose up -d
docker   Stops and removes all containers and networks.
compose down
docker   Lists the status of running services.
compose ps
docker   Follows the live log output from all services.
compose logs
-f
docker   Rebuilds images if the Dockerfile has changed.
compose build
docker   Runs a command inside a running service container.
compose exec
[service]
[cmd]
********** 9 **********
--- page 10 ---
CO-3;   b   Explain Replication Controller and ReplicaSet with suitable diagram. Give   10
SO-6;   the ReplicaSet YAML Walkthrough example.
BL-2,3   Explain & diagram -8 Marks
Example – 2 Marks
Replica Set
ReplicaSet is a process that runs multiple instances of a Pod and keeps the
specified number of Pods constant. let’s take an example where we have a
set of two worker nodes in a cluster as in the above diagram.
we have the front end, running on worker1 and the backend is on the
worker2 node.
The application is working great as long as the pods and nodes are healthy
and running.
Please note, these two pods are running without any controllers backing
these parts as of now.
Replication Controller (RC)
A Replication Controller manages multiple instances of a pod. It uses
equality-based selectors (e.g., app = frontend) to ensure the correct number
of pods are running.
Key Characteristics:
Legacy: Deprecated in favor of ReplicaSets.
Selector Type: Supports only equality-based selectors (key=value).
Behavior: If a node fails, it replaces the pods.
apiVersion: apps/v1   # 1. API Version (apps/v1 for RS)
kind: ReplicaSet   # 2. Resource Type
metadata:
name: frontend-rs   # 3. Name of the ReplicaSet
labels:
app: web
tier: frontend
spec:
replicas: 3   # 4. Desired Number of Pods
selector:
matchLabels:   # 5. Selector to identify pods
tier: frontend   # Must match template labels
template:   # 6. Pod Template
metadata:
labels:   # 7. Labels applied to pods
********** 10 **********
--- page 11 ---
tier: frontend
spec:
containers:
- name: nginx
image: nginx:1.16.1   # 8. Container Image
ports:
- containerPort: 80
Q5   a   Explain the Nagios Remote Plugin Executor with diagram and analyze the   10
CO-4;   role of NRPE in distributed monitoring environments.
SO-6;   Explain & diagram -7 Marks
BL-2,3,4   Analyze – 3 Marks
NRPE (Nagios Remote Plugin Executor) is an agent that allows Nagios to
execute plugins on remote Linux/Unix machines. This is useful for
monitoring system metrics and services that are not externally visible (e.g.,
CPU load, disk usage, memory usage).
1. Monitoring Host
Runs the Nagios Core.
Uses the check_nrpe plugin to communicate with remote systems.
Sends encrypted requests (via SSL) to remote hosts using NRPE.
2. Remote Linux/Unix Host
Runs the NRPE daemon.
Accepts requests from the monitoring host and executes specific monitoring
plugins locally.
Returns the result of these plugins back to Nagios.
3. Communication Flow
Nagios initiates a connection using check_nrpe.
A secure (SSL) connection is established with the NRPE daemon on the
remote host.
NRPE executes local Nagios plugins (like check_disk, check_load, etc.).
These plugins collect data from local resources/services or query other
remote services.
The results are sent back to Nagios for analysis and alerting.
Core Role in Distributed Environments:
********** 11 **********
--- page 12 ---
Secure Remote Execution: NRPE allows execution of Nagios plugins on
remote hosts, returning results via an encrypted (SSL) connection, which is
more secure and efficient than using SSH for every check.
Segmented Network Monitoring: It enables monitoring of servers behind
firewalls or in DMZs. The NRPE daemon on the remote machine (port
5666) only needs to accept connections from the central monitoring server,
simplifying firewall configuration.
Reduced Monitoring Overhead: By running checks locally on the target
machine and only sending the result back, NRPE reduces the load on the
central monitoring server compared to active, network-intensive polling.
Indirect Proxy Monitoring: NRPE can be configured to act as a proxy,
allowing the monitoring server to check resources on remote networks that
are not directly reachable, provided the NRPE host has access.
Scalability: NRPE is essential for scaling Nagios to monitor hundreds or
thousands of nodes, commonly used in distributed, redundant, or failover
configurations
CO-3;   b   Explain the architecture of Kubernetes. Describe the role of master and   10
SO-6;   worker node components in detail.
BL-2,3   Explain – 5 Marks
Describe – 5 Marks
Kubernetes follows a client-server architecture designed as a distributed
control system. The architecture is divided into two primary layers: the
Control Plane (Master Node), which serves as the "brain" for making global
decisions, and the Worker Nodes, which act as the "hands" to execute
application workloads.
1. Control Plane (Master Node) Components
The Control Plane manages the cluster's global state and orchestrates tasks
such as scheduling and scaling.
kube-apiserver: The central management point and "front door" of the
cluster. It exposes the Kubernetes API, handles authentication and
authorization, and is the only component that communicates directly with the
cluster's database.
etcd: A distributed, highly available key-value store that serves as the
cluster's "memory" and single source of truth. It stores all cluster data,
including configuration, state, and secrets.
kube-scheduler: The "decision maker" that assigns newly created Pods to
specific worker nodes. It evaluates resource requirements (CPU, memory),
hardware/software constraints, and affinity rules to select the most suitable
node for a
kube-controller-manager: An automation engine that runs multiple controller
********** 12 **********
--- page 13 ---
processes to maintain the "desired state" of the cluster. Key controllers
include:
Node Controller: Monitors node health and responds if a node goes down.
Replication Controller: Ensures the correct number of Pod replicas are
running at all times.
cloud-controller-manager (CCM): Handles cloud-provider-specific logic,
such as managing cloud load balancers or storage volumes.
2. Worker Node Components
Worker Nodes are the machines (physical or virtual) where application
containers actually run.
kubelet: A local agent that runs on every node. It receives Pod specifications
(PodSpecs) from the API server and ensures the containers described in those
specs are running and healthy.
kube-proxy: A network proxy that manages network rules on the node. It
enables communication between Pods and handles request routing for
Kubernetes Services, providing load balancing across Pods.
Container Runtime: The software responsible for actually running the
containers. While Docker was historically common, Kubernetes now
primarily uses runtimes that adhere to the Container Runtime Interface (CRI),
such as containerd or CRI-O.
Q6   a   Explain the architecture of Prometheus and discuss how its pull-based   10
CO-2,3;   model differs from push-based monitoring systems.
SO-6;   Explain – 5 Marks
BL-2,3
Discuss pull base & push based – 5 Marks
Prometheus is a popular open-source monitoring and alerting system
written in Golang, capable of collecting and processing metrics from
various targets.
You can also query, view, analyze the metrics and get alerted based on the
thresholds.
Prometheus collects and stores its metrics as time series data, i.e. metrics
information is stored with the timestamp at which it was recorded, alongside
optional key-value pairs called labels.
********** 13 **********
--- page 14 ---
Feature   Pull-Based (Prometheus)   Push-Based (Traditional)
Data Flow   Server actively requests data   Targets actively send data to the
from targets.   server.
Health   Inherently knows if a target   Harder to distinguish between a
Check   is down if the pull fails.   "quiet" system and a system that is
down.
Control   Server controls the load and   Server can be overwhelmed if many
frequency of data collection.   targets push data simultaneously.
Configurati   Centralized in the monitoring   Decentralized; every target must
on   server.   know the server's address.
Security   Pulling often requires open   More secure for targets as they only
ports on targets (potential   need outbound connections.
risk).
Best Use   Long-running services and   Short-lived jobs or systems behind
Case   dynamic cloud environments.   strict firewalls.
CO-1;   b   Compare Agile Methodologies with Traditional Approaches of Project   10
SO-6;   Management. Also write about the limitations of Agile Methodology.
BL-1
Compare - 6 Marks
Limitations -4 Marks
Feature   Agile Methodology   Traditional (Waterfall
Workflow   Iterative & Incremental: Projects are   Linear & Sequential: F
broken into short cycles called "sprints"   path: Initiation → Plann
(2-4 weeks).   → Monitoring → Closu
Flexibility   High: Welcomes late-stage changes and Low: Changes often req
evolving requirements.   approvals and can disru
timelines.
Documentation   Minimal: Prioritizes working software   Comprehensive: Heavi
over extensive records.   detailed upfront plannin
********** 14 **********
--- page 15 ---
Customer Role   Continuous Involvement: Customers   Upfront Involvement: Customers are
provide feedback after every iteration.   typically involved only during initial
planning and final delivery.
Team Structure   Self-Organizing: Cross-functional   Hierarchical: Defined roles with a project
teams with shared ownership and flat   manager holding primary accountability.
hierarchy.
Risk   Reactive: Identified and mitigated   Proactive: Risks are identified and
Management   throughout the project via frequent   planned for extensively before execution
reviews.   begins.
Limitations of Agile Methodology
Despite its flexibility, Agile has several drawbacks that can hinder specific
project types:
Lack of Predictability: Because requirements evolve, it is difficult to
estimate final costs, total resources, or a definitive completion date at the
start.
Documentation Deficiency: Agile's focus on "just-in-time" documentation
can lead to insufficient records for long-term maintenance, legal
compliance, or onboarding new members.
High Time Demands: The method requires constant, high-level interaction
through daily stand-ups and sprint reviews, which can strain team members'
schedules and reduce focus.
Dependency on Customer Availability: If stakeholders are disengaged or
unavailable to provide feedback, the iterative process can stall or result in a
product that misses user needs.
Scope Creep: The inherent flexibility can lead to continuous feature
additions without a clear "end goal," causing the project to run beyond its
original intent.
Challenges in Scaling: While effective for small teams, scaling Agile to
large corporations often introduces bureaucratic barriers that erode the
benefits of speed and adaptability.
Incompatibility with Fixed Projects: It is unsuitable for projects where the
final outcome must be fixed from the start, such as construction or heavily
regulated manufacturing.
Q7   a
Explain authentication and authorization in Jenkins’s security.   5
CO-1,2;
SO-6;   Marking Scheme (Step-wise)
BL-2,3   • Authentication explanation – 2M
• Authorization explanation – 2M
•   Difference between both – 1M
Model Answer
Jenkins security is based on two key concepts: authentication and
authorization.
Authentication
Authentication is the process of verifying the identity of a user.
• Ensures that only valid users can access Jenkins
********** 15 **********
--- page 16 ---
• Methods include:
•   Jenkins internal database
• LDAP integration
•   Single Sign-On (SSO)
Authorization
Authorization determines what actions a user is allowed to perform after
authentication.
•   Defines permissions such as read, write, or admin access
Implemented using strategies like:
o Role-based access
o Matrix-based security
Difference
•   Authentication: Verifies identity
•   Authorization: Grants permissions
Together, they ensure secure access control in Jenkins.
CO-1;   b   Give proper explanation for problems on overall delivery process in   5
SO-6;   DevOps process model.
BL-1,2
for each point of explanation 1 marks total 5X1=5 marks
• Waste in having too many handover and decision points in the
process
• Waste due to unnecessary wait time between steps
• Many software changes are packaged up into large, big bang releases
• Large/infrequent releases breed an environment for escaped defects,
bugs
• Releases: seen as something to dread instead a +ve opportunity for
change
• People are disengaged or there is low morale (or both)
• Software changes are not trusted until they have been tested many
times
• Over complex dependencies within the software design
• Value occurs only when the end users are successfully leveraging the
SW
• DevOps aims at providing tighter integration of development and
deployment operations
CO-2,3;   c
Describe the role of Git in version control. How does it help in tracking and   5
SO-6;   managing changes in a project?
BL-2,3
Role of Git (3 Marks):
Git is a version control system that tracks changes, maintains history, and allows
rollback.
Benefits (2 Marks):
Improves collaboration, prevents data loss, and manages versions efficiently.
CO-1,2;   d   Write five differences between traditional software development and   5
SO-5;   software development with Docker.
********** 16 **********
--- page 17 ---
BL-2,3   Use of Docker in   Traditional   Docker Deployment
DevOpsFeature   Deployment
Environment   Different   Same environment
Consistency   environments on   across all machines
different machines   using Docker images.
cause issues.
Setup Complexity   Manual setup of   Pre-configured
software, libraries,   Docker images
and configurations.   eliminate manual
setup.
Error Probability   High chance of errors Reduced errors as
due to manual   everything is bundled
configuration.   in the image.
Deployment Speed   Time-consuming due   Faster as the same
to separate setups for   Docker image runs
each machine.   everywhere.
Dependency   Dependencies must be All dependencies are
Management   manually installed on   packaged inside the
each system.   Docker image.
Portability   Code may work   Works the same on
differently on   any system that
different systems.   supports Docker.
Collaboration   Difficult to share the   Easy sharing via
exact working   Docker images.
environment.
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper f23044fefbb4

- Departments: Artificial Intelligence
- Programmes: BTech AI 7012
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_AI_7012/Agile Product Development with DevOps/ANS_Agile Product Development with DevOps(702AI0C022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Agile Product Development with DevOps
Date: 30 Jun 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. Answer to each new question to be started on a fresh page.
5. Figure in right hand side indicates full marks.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
CO- 1;   a Explain Prototyping Model in detail. Support your answer with diagram.
SO-6;   5
BL-1   Phases – 4 Marks
Diagram -1 Mark
In the Prototyping Model, an initial prototype (a working version) of the
software is built and refined through multiple iterations based on user
feedback.
Phases of Prototyping Model:
1. Requirement Gathering – Collect initial requirements.
2. Quick Design – Create a basic system structure.
3. Prototyping – Develop a working prototype.
4. User Evaluation – Get feedback from users.
5. Refinement – Improve the prototype based on feedback.
6. Final Development – Convert the refined prototype into a full
system.
********** 1 **********

[Text in pictures on this page, read by OCR]
Build Prototype

va Ne customer

Requirements
. . Cust satisfied .
Gathering —> Quick Design Evaluation of Design
Prototype J
x / Implement
Refine a5
Requirements

Test

Maintenance
--- page 2 ---
CO-1,2;   b
SO- 5;   Explain the purpose and usage of the following Git commands with   5
BL-2,3   examples: git init, git add, git commit, and git status.
Commands Explanation (4 Marks):
• git init – Initializes a repository (1 Mark)
• git add – Stages changes (1 Mark)
• git commit – Saves changes with message (1 Mark)
• git status – Shows file status (1 Mark)
Example (1 Mark):
git init → git add file.txt → git commit -m "Initial commit"
CO-1,2;   c
Explain the process of plugin installation and upgrade in Jenkins.   5
SO-6;
BL-3,4   Marking Scheme (Step-wise)
• Definition/role of plugins – 1Mark
•   Installation process – 2Marks
• Upgrade process – 1.5Marks
• Importance/benefits – 0.5Marks
Model Answer
Jenkins plugins are extensions that enhance the functionality of Jenkins by
enabling integration with various tools and adding new features.
Plugin Installation Process
Plugins can be installed using the Jenkins Plugin Manager:
• Navigate to “Manage Jenkins”
•   Select “Manage Plugins”
• Search for the required plugin
•   Select and install the plugin
•   Restart Jenkins (if required)
This allows Jenkins to support additional tools like version control systems,
cloud services, and build tools.
Plugin Upgrade Process
Jenkins periodically checks for plugin updates.
• Go to Plugin Manager
• View available updates
•   Select plugins to upgrade
•   Install updates and restart Jenkins
Importance
• Enhances Jenkins capabilities
• Keeps system updated and secure
• Enables integration with modern tools
********** 2 **********
--- page 3 ---
Thus, plugin management is essential for maintaining an efficient CI/CD
environment.
CO-2,3;   d
SO-6 ;   How Docker images and containers are created and managed in Docker   5
BL-2,3   Environment?
How – 2.5 Marks
Managed – 2.5 Marks
Creating and Managing Docker Images
Docker images are read-only, immutable templates that serve as blueprints
for containers.
Creation (Build):
Dockerfile: Developers write a Dockerfile containing sequential instructions
(e.g., FROM, RUN, COPY, CMD) to assemble the image.
Layered Architecture: Each instruction in a Dockerfile creates a new layer.
This makes images lightweight as layers can be cached and reused across
different images.
Build Command: Running docker build -t image_name:tag . compiles the
Dockerfile into a usable image.
Management:
Storage (Registries): Images are stored and shared in Docker Registries, with
Docker Hub being the default public option.
Listing & Removal: Users view local images with docker images and can
remove unused ones with docker rmi image_name to save space.
Versioning: Images are managed using tags (e.g., ubuntu:22.04) to
distinguish between different versions.
2. Creating and Managing Docker Containers
A container is a live, runnable instance of an image that includes an additional
writable layer for temporary data.
Creation and Execution:
Run Command: The command docker run <image_name> pulls the image if
it's missing, creates the container, and starts it immediately.
Create Command: Alternatively, docker create <image_name> prepares a
********** 3 **********
--- page 4 ---
container in a "Created" state without starting it.
Lifecycle Management:
States: Containers transition through several states: Created (ready), Running
(active), Paused (processes frozen), Stopped (shutdown gracefully), and
Deleted (removed).
Control Commands:
docker start/stop: Initiates or halts a container.
docker pause/unpause: Suspends or resumes container processes without a
full shutdown.
docker rm: Permanently removes a stopped container.
Q2   a   10
CO-1;   A large enterprise with 40+ teams is transitioning from Waterfall to
SO-6;   Agile. Some teams follow Agile strictly, while others resist change.
BL-1   Integration issues and inconsistent practices are causing project delays.
Analyze the challenges of scaling Agile. How can an Agile mindset,
principles, and   coordination mechanisms improve   large-scale
development?
Analyze the challenges – 5Marks
How – 5 Marks
Transitioning a large enterprise with 40+ teams from Waterfall to Agile
is a complex, high-stakes endeavor that involves navigating deep-seated
cultural resistance and technical hurdles. The scenario described—some
teams practicing Agile strictly while others resist—indicates a lack of
consistent, organizational-level adoption (or "agile theater").
Challenges of Scaling Agile (40+ Teams)
Scaling Agile goes beyond just applying Scrum; it requires addressing
structural, cultural, and technical bottlenecks.
• Deep Cultural Resistance & "Agile Theater": Resistance often
stems from fear of job insecurity, loss of control by managers, and
comfort with old processes. When change is forced rather than
adopted, organizations may exhibit "agile theater," where teams go
through the motions (e.g., daily stand-ups) without actually
following agile principles.
********** 4 **********

[Text in pictures on this page, read by OCR]
AGILE MANIFESTO

FOUR CORE VALUES & TWELVE PRINCIPLES

Deliver Early & Often
Embrace Change 4 1.

Release Frequently
Collaborate Daily ¢ > 02. hoch
Empower Teams Working software

Talk Face-to-Face over comprehensive documentation
Measure by Working Software 03. Castomer:
Maintain Sustainable Pace Fone a fern
Focus on Quality 04.
Keep It Simple Poi ron beri

Trust Self-Organizing Teams
Reflect & Improve
--- page 5 ---
Integration Issues & Hidden Dependencies: As described, multiple
teams working on a single project create significant dependencies,
causing "module integration issues" and code quality problems. A lack
of unified, automated testing (CI/CD) makes integrating 40+ teams' work
extremely challenging
•   Inconsistent Practices & Low Maturity: When some teams are
"strict" and others are not, it leads to communication failures and
misalignment in delivery, resulting in inconsistent practices.
•   "Wagile" or "Scrumfall" Behaviour: Many teams end up in a
hybrid state where they use short-term Sprints but keep long-term, fixed,
rigid Waterfall planning.
•   Lack of Leadership Support: A common failure factor is when
senior management advocates Agile but does not change the traditional
"command-and-control" management style.
Improving Large-Scale Development
To overcome these challenges, a shift in mindset, reinforced by proper
structure, is required.
1. Fostering an Agile Mindset and Principles
•   Leadership Alignment and Servant Leadership: Leaders must stop
managing tasks and start enabling teams. This involves transitioning
from "command-and-control" to "servant leadership," where managers
remove impediments for teams.
•   Create a Culture of Psychological Safety: A blameless
environment is needed to encourage learning from mistakes, rather than
punishing teams for delays that are often the result of complex, systemic
issues.
•   Focus on Value, Not Velocity: Teams should be trained to focus
on delivering valuable, working software to customers, rather than just
maximizing "story points".
2. Coordination Mechanisms for Scale
•   Scaled Agile Frameworks (e.g., SAFe, LeSS): For 40+ teams, a
structured framework   is   essential to coordinate dependencies.
Techniques like a "Master Product Backlog" or "Scrum of Scrums"
provide an overview of all products and align team goals.
• Communities of Practice (CoPs): To harmonize inconsistent
practices, create CoPs where developers, Scrum Masters, and
Product Owners from different teams meet voluntarily to share
best practices, tools, and lessons learned.
•   Cross-functional and Self-organizing Teams: Break down silos by
ensuring teams are truly cross-functional (including testers,
developers, and designers) so they can complete a user story
without depending on external teams.
********** 5 **********
--- page 6 ---
• Automated Continuous Integration (CI/CD): To solve integration
issues, automated integration testing must be implemented to
ensure that code from different teams can be tested immediately,
reducing "late-discovery" defects.
• Agile Training and Dedicated Coaching: Invest in professional
training for all levels—not just developers—to ensure a common
understanding of Agile values, mitigating resistance caused by a
lack of knowledge.
CO-1;   b
What is the essential preparation requiring before starting a new project on 10
SO-6;   DevOps platform, and how can each step be detailed?
BL-1,2
For each point of explanation require 2 marks total 5X2=10 marks
Preparing for a new project on a DevOps platform requires a holistic
approach that aligns culture, processes, and tools before code is written.
Essential preparations include creating a strategy, building a cross-functional
team, automating infrastructure, setting up CI/CD pipelines, and establishing
monitoring.
1. Define Strategy and Goals (Planning Phase)
Before selecting tools, define what success looks like to ensure the project
aligns with business objectives.
•   Create a DevOps Roadmap: Develop a step-by-step transformation
plan. Document this roadmap in a central, accessible location (like
Confluence or Jira) to keep all stakeholders aligned.
•   Establish Key Performance Indicators (KPIs): Define metrics like
Deployment Frequency, Lead Time for Changes, Mean Time to Recovery
(MTTR), and Change Failure Rate.
•   Adopt Agile Project Management: Structure the work using Agile
methodologies (Scrum/Kanban) to break the project into small, manageable
sprints.
2. Build and Train the Team (Cultural Preparation)
DevOps is a cultural shift, not just a technical one.
•   Assemble Cross-Functional Teams: Combine developers, operations
engineers, QA, and security specialists into a single team with shared
responsibility.
•   Foster Collaboration: Set up communication channels (e.g., Slack,
Teams) to break down silos. Implement "You build it, you run it"
ownership.
•   Conduct Training Workshops: Ensure the team is proficient in new
tools, Git branching models, and security practices.
3. Select and Setup the Toolchain
Choose a set of integrated tools rather than attempting to buy one single
"DevOps product".
•   Version Control Setup (Git): Create a source code repository
(GitHub, Bitbucket) and define a branching strategy (e.g., GitHub Flow or
Trunk-Based Development).
********** 6 **********
--- page 7 ---
•   Infrastructure as Code (IaC): Prepare to use tools like Terraform or
Ansible to define infrastructure in text-based configuration files, allowing
repeatable and auditable deployments.
•   Tool Integration: Integrate work tracking (Jira) with source control
(Bitbucket/GitLab) to provide full visibility from planning to deployment.
4. Implement CI/CD and Testing Frameworks
Automating the building, testing, and deployment of code is essential.
•   Continuous Integration (CI): Establish automated pipelines (Jenkins,
GitHub Actions) that pull code, run tests, and build artifacts immediately
after a commit.
•   Automated Testing Setup: Create a repository of unit, integration,
and security tests that run automatically on every pull request.
•   Continuous Delivery (CD): Ensure the code is always in a deployable
state by automating the promotion of code to staging and production
environments.
5. Establish Operational Readiness (Monitoring & Security)
The project should be observable and secure from the start.
•   Set Up Continuous Monitoring: Implement logging and monitoring
tools (Prometheus, Grafana, ELK Stack) to monitor application
performance and system health.
•   Create Runbooks: Document operational procedures to guide the
team in resolving common issues.
•   Embed Security (DevSecOps): Integrate security scanning
(SAST/DAST) directly into the CI/CD pipeline. Use a secrets management
system rather than storing keys in code.
Q3   a A DevOps team is managing a project using Git and remote repositories.   10
CO-1,2;   They encounter:
SO-5;   • Difficulty syncing local and remote repositories.
BL-3   • Confusion between git fetch and git pull.
• The need to revert to a previous stable version.
• Multiple versions of code needing proper tracking.
• The requirement to collaborate efficiently across teams.
a) Differentiate between git fetch and git pull.
b) How can the project be reverted to a previous version safely?
c) Which commands are used to sync local and remote repositories?
d) How does Git help in version tracking?
e) Why is Git suitable for collaborative development?
a) Fetch vs Pull (3 Marks):
git fetch downloads changes without merging;
git pull downloads and merges changes.
b) Revert to previous version (2 Marks):
Use git revert or git checkout <commit_id>.
c) Sync commands (2 Marks):
git push and git pull.
d) Version tracking (2 Marks):
Git tracks all changes with commits, allowing history and rollback.
********** 7 **********
--- page 8 ---
e) Collaboration (1 Mark):
Enables multiple developers to work simultaneously efficiently.
CO-1,2;   b A team wants to monitor and visualize their CI/CD workflow clearly.   10
SO-6;   Explain how Jenkins Delivery Pipeline helps in visualization and
BL-2,3   management of different stages.
Marking Scheme (Refined)
•   Introduction to Delivery Pipeline – 2M
•   Explanation of stages (commit, test, deploy) – 3M
•   Visualization and working mechanism – 3M
•   Benefits and practical importance – 2M
Model Answer
Jenkins Delivery Pipeline is a visualization tool that provides a clear
graphical representation of the Continuous Delivery process. It helps teams
monitor and manage different stages of the CI/CD workflow.
Concept of Delivery Pipeline
A delivery pipeline represents the flow of software from code commit to
deployment. It organizes the workflow into multiple stages such as build,
test, and deployment. Each stage contains one or more tasks (jobs), and the
pipeline shows how these stages are connected.
Stages in Delivery Pipeline
1. Commit Stage
• Code is integrated into the repository
•   Initial build and basic tests are performed
2. Test Stage
• Advanced testing such as integration and system testing
• Ensures application quality
3. Deployment Stage
•   Application is deployed to staging or production environment
•   Final validation before release
Visualization and Working
• The Delivery Pipeline plugin displays all stages in a pipeline view
• Each stage is represented visually with status indicators
(success/failure)
•   It shows the flow from one stage to another
•   Provides real-time updates of pipeline progress
This helps teams easily track:
•   Current stage of execution
•   Failed stages
•   Latest successful builds
Benefits
• Improves visibility of CI/CD process
• Helps identify bottlenecks quickly
• Enhances team collaboration
•   Provides better monitoring and control
********** 8 **********
--- page 9 ---
Q4   a
What is a Dockerfile? Explain its structure and commonly used instructions   10
(FROM, RUN, CMD, COPY, etc.) with an example.
What – 1 Mark
Structure – 3 Marks
Instructions & example - 6
A Dockerfile is a script containing instructions to build a Docker image.
Sample Dockerfile:
FROM node:14
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "app.js"]
Explanation:
• FROM → base image
• WORKDIR → working directory
• COPY → copy files
• RUN → install dependencies
CO-2,3;   • CMD → run application
SO-6;
BL-1,2   Dockerfile automates image creation.
Command   Purpose
docker   Starts all services in detached (background) mode.
compose up -d
docker   Stops and removes all containers and networks.
compose down
docker   Lists the status of running services.
compose ps
docker   Follows the live log output from all services.
compose logs
-f
docker   Rebuilds images if the Dockerfile has changed.
compose build
docker   Runs a command inside a running service container.
compose exec
[service]
[cmd]
********** 9 **********
--- page 10 ---
CO-3;   b   Explain Replication Controller and ReplicaSet with suitable diagram. Give   10
SO-6;   the ReplicaSet YAML Walkthrough example.
BL-2,3   Explain & diagram -8 Marks
Example – 2 Marks
Replica Set
ReplicaSet is a process that runs multiple instances of a Pod and keeps the
specified number of Pods constant. let’s take an example where we have a
set of two worker nodes in a cluster as in the above diagram.
we have the front end, running on worker1 and the backend is on the
worker2 node.
The application is working great as long as the pods and nodes are healthy
and running.
Please note, these two pods are running without any controllers backing
these parts as of now.
Replication Controller (RC)
A Replication Controller manages multiple instances of a pod. It uses
equality-based selectors (e.g., app = frontend) to ensure the correct number
of pods are running.
Key Characteristics:
Legacy: Deprecated in favor of ReplicaSets.
Selector Type: Supports only equality-based selectors (key=value).
Behavior: If a node fails, it replaces the pods.
apiVersion: apps/v1   # 1. API Version (apps/v1 for RS)
kind: ReplicaSet   # 2. Resource Type
metadata:
name: frontend-rs   # 3. Name of the ReplicaSet
labels:
app: web
tier: frontend
spec:
replicas: 3   # 4. Desired Number of Pods
selector:
matchLabels:   # 5. Selector to identify pods
tier: frontend   # Must match template labels
template:   # 6. Pod Template
metadata:
labels:   # 7. Labels applied to pods
********** 10 **********
--- page 11 ---
tier: frontend
spec:
containers:
- name: nginx
image: nginx:1.16.1   # 8. Container Image
ports:
- containerPort: 80
Q5   a   Explain the Nagios Remote Plugin Executor with diagram and analyze the   10
CO-4;   role of NRPE in distributed monitoring environments.
SO-6;   Explain & diagram -7 Marks
BL-2,3,4   Analyze – 3 Marks
NRPE (Nagios Remote Plugin Executor) is an agent that allows Nagios to
execute plugins on remote Linux/Unix machines. This is useful for
monitoring system metrics and services that are not externally visible (e.g.,
CPU load, disk usage, memory usage).
1. Monitoring Host
Runs the Nagios Core.
Uses the check_nrpe plugin to communicate with remote systems.
Sends encrypted requests (via SSL) to remote hosts using NRPE.
2. Remote Linux/Unix Host
Runs the NRPE daemon.
Accepts requests from the monitoring host and executes specific monitoring
plugins locally.
Returns the result of these plugins back to Nagios.
3. Communication Flow
Nagios initiates a connection using check_nrpe.
A secure (SSL) connection is established with the NRPE daemon on the
remote host.
NRPE executes local Nagios plugins (like check_disk, check_load, etc.).
These plugins collect data from local resources/services or query other
remote services.
The results are sent back to Nagios for analysis and alerting.
Core Role in Distributed Environments:
********** 11 **********
--- page 12 ---
Secure Remote Execution: NRPE allows execution of Nagios plugins on
remote hosts, returning results via an encrypted (SSL) connection, which is
more secure and efficient than using SSH for every check.
Segmented Network Monitoring: It enables monitoring of servers behind
firewalls or in DMZs. The NRPE daemon on the remote machine (port
5666) only needs to accept connections from the central monitoring server,
simplifying firewall configuration.
Reduced Monitoring Overhead: By running checks locally on the target
machine and only sending the result back, NRPE reduces the load on the
central monitoring server compared to active, network-intensive polling.
Indirect Proxy Monitoring: NRPE can be configured to act as a proxy,
allowing the monitoring server to check resources on remote networks that
are not directly reachable, provided the NRPE host has access.
Scalability: NRPE is essential for scaling Nagios to monitor hundreds or
thousands of nodes, commonly used in distributed, redundant, or failover
configurations
CO-3;   b   Explain the architecture of Kubernetes. Describe the role of master and   10
SO-6;   worker node components in detail.
BL-2,3   Explain – 5 Marks
Describe – 5 Marks
Kubernetes follows a client-server architecture designed as a distributed
control system. The architecture is divided into two primary layers: the
Control Plane (Master Node), which serves as the "brain" for making global
decisions, and the Worker Nodes, which act as the "hands" to execute
application workloads.
1. Control Plane (Master Node) Components
The Control Plane manages the cluster's global state and orchestrates tasks
such as scheduling and scaling.
kube-apiserver: The central management point and "front door" of the
cluster. It exposes the Kubernetes API, handles authentication and
authorization, and is the only component that communicates directly with the
cluster's database.
etcd: A distributed, highly available key-value store that serves as the
cluster's "memory" and single source of truth. It stores all cluster data,
including configuration, state, and secrets.
kube-scheduler: The "decision maker" that assigns newly created Pods to
specific worker nodes. It evaluates resource requirements (CPU, memory),
hardware/software constraints, and affinity rules to select the most suitable
node for a
kube-controller-manager: An automation engine that runs multiple controller
********** 12 **********
--- page 13 ---
processes to maintain the "desired state" of the cluster. Key controllers
include:
Node Controller: Monitors node health and responds if a node goes down.
Replication Controller: Ensures the correct number of Pod replicas are
running at all times.
cloud-controller-manager (CCM): Handles cloud-provider-specific logic,
such as managing cloud load balancers or storage volumes.
2. Worker Node Components
Worker Nodes are the machines (physical or virtual) where application
containers actually run.
kubelet: A local agent that runs on every node. It receives Pod specifications
(PodSpecs) from the API server and ensures the containers described in those
specs are running and healthy.
kube-proxy: A network proxy that manages network rules on the node. It
enables communication between Pods and handles request routing for
Kubernetes Services, providing load balancing across Pods.
Container Runtime: The software responsible for actually running the
containers. While Docker was historically common, Kubernetes now
primarily uses runtimes that adhere to the Container Runtime Interface (CRI),
such as containerd or CRI-O.
Q6   a   Explain the architecture of Prometheus and discuss how its pull-based   10
CO-2,3;   model differs from push-based monitoring systems.
SO-6;   Explain – 5 Marks
BL-2,3
Discuss pull base & push based – 5 Marks
Prometheus is a popular open-source monitoring and alerting system
written in Golang, capable of collecting and processing metrics from
various targets.
You can also query, view, analyze the metrics and get alerted based on the
thresholds.
Prometheus collects and stores its metrics as time series data, i.e. metrics
information is stored with the timestamp at which it was recorded, alongside
optional key-value pairs called labels.
********** 13 **********
--- page 14 ---
Feature   Pull-Based (Prometheus)   Push-Based (Traditional)
Data Flow   Server actively requests data   Targets actively send data to the
from targets.   server.
Health   Inherently knows if a target   Harder to distinguish between a
Check   is down if the pull fails.   "quiet" system and a system that is
down.
Control   Server controls the load and   Server can be overwhelmed if many
frequency of data collection.   targets push data simultaneously.
Configurati   Centralized in the monitoring   Decentralized; every target must
on   server.   know the server's address.
Security   Pulling often requires open   More secure for targets as they only
ports on targets (potential   need outbound connections.
risk).
Best Use   Long-running services and   Short-lived jobs or systems behind
Case   dynamic cloud environments.   strict firewalls.
CO-1;   b   Compare Agile Methodologies with Traditional Approaches of Project   10
SO-6;   Management. Also write about the limitations of Agile Methodology.
BL-1
Compare - 6 Marks
Limitations -4 Marks
Feature   Agile Methodology   Traditional (Waterfall
Workflow   Iterative & Incremental: Projects are   Linear & Sequential: F
broken into short cycles called "sprints"   path: Initiation → Plann
(2-4 weeks).   → Monitoring → Closu
Flexibility   High: Welcomes late-stage changes and Low: Changes often req
evolving requirements.   approvals and can disru
timelines.
Documentation   Minimal: Prioritizes working software   Comprehensive: Heavi
over extensive records.   detailed upfront plannin
********** 14 **********
--- page 15 ---
Customer Role   Continuous Involvement: Customers   Upfront Involvement: Customers are
provide feedback after every iteration.   typically involved only during initial
planning and final delivery.
Team Structure   Self-Organizing: Cross-functional   Hierarchical: Defined roles with a project
teams with shared ownership and flat   manager holding primary accountability.
hierarchy.
Risk   Reactive: Identified and mitigated   Proactive: Risks are identified and
Management   throughout the project via frequent   planned for extensively before execution
reviews.   begins.
Limitations of Agile Methodology
Despite its flexibility, Agile has several drawbacks that can hinder specific
project types:
Lack of Predictability: Because requirements evolve, it is difficult to
estimate final costs, total resources, or a definitive completion date at the
start.
Documentation Deficiency: Agile's focus on "just-in-time" documentation
can lead to insufficient records for long-term maintenance, legal
compliance, or onboarding new members.
High Time Demands: The method requires constant, high-level interaction
through daily stand-ups and sprint reviews, which can strain team members'
schedules and reduce focus.
Dependency on Customer Availability: If stakeholders are disengaged or
unavailable to provide feedback, the iterative process can stall or result in a
product that misses user needs.
Scope Creep: The inherent flexibility can lead to continuous feature
additions without a clear "end goal," causing the project to run beyond its
original intent.
Challenges in Scaling: While effective for small teams, scaling Agile to
large corporations often introduces bureaucratic barriers that erode the
benefits of speed and adaptability.
Incompatibility with Fixed Projects: It is unsuitable for projects where the
final outcome must be fixed from the start, such as construction or heavily
regulated manufacturing.
Q7   a
Explain authentication and authorization in Jenkins’s security.   5
CO-1,2;
SO-6;   Marking Scheme (Step-wise)
BL-2,3   • Authentication explanation – 2M
• Authorization explanation – 2M
•   Difference between both – 1M
Model Answer
Jenkins security is based on two key concepts: authentication and
authorization.
Authentication
Authentication is the process of verifying the identity of a user.
• Ensures that only valid users can access Jenkins
********** 15 **********
--- page 16 ---
• Methods include:
•   Jenkins internal database
• LDAP integration
•   Single Sign-On (SSO)
Authorization
Authorization determines what actions a user is allowed to perform after
authentication.
•   Defines permissions such as read, write, or admin access
Implemented using strategies like:
o Role-based access
o Matrix-based security
Difference
•   Authentication: Verifies identity
•   Authorization: Grants permissions
Together, they ensure secure access control in Jenkins.
CO-1;   b   Give proper explanation for problems on overall delivery process in   5
SO-6;   DevOps process model.
BL-1,2
for each point of explanation 1 marks total 5X1=5 marks
• Waste in having too many handover and decision points in the
process
• Waste due to unnecessary wait time between steps
• Many software changes are packaged up into large, big bang releases
• Large/infrequent releases breed an environment for escaped defects,
bugs
• Releases: seen as something to dread instead a +ve opportunity for
change
• People are disengaged or there is low morale (or both)
• Software changes are not trusted until they have been tested many
times
• Over complex dependencies within the software design
• Value occurs only when the end users are successfully leveraging the
SW
• DevOps aims at providing tighter integration of development and
deployment operations
CO-2,3;   c
Describe the role of Git in version control. How does it help in tracking and   5
SO-6;   managing changes in a project?
BL-2,3
Role of Git (3 Marks):
Git is a version control system that tracks changes, maintains history, and allows
rollback.
Benefits (2 Marks):
Improves collaboration, prevents data loss, and manages versions efficiently.
CO-1,2;   d   Write five differences between traditional software development and   5
SO-5;   software development with Docker.
********** 16 **********
--- page 17 ---
BL-2,3   Use of Docker in   Traditional   Docker Deployment
DevOpsFeature   Deployment
Environment   Different   Same environment
Consistency   environments on   across all machines
different machines   using Docker images.
cause issues.
Setup Complexity   Manual setup of   Pre-configured
software, libraries,   Docker images
and configurations.   eliminate manual
setup.
Error Probability   High chance of errors Reduced errors as
due to manual   everything is bundled
configuration.   in the image.
Deployment Speed   Time-consuming due   Faster as the same
to separate setups for   Docker image runs
each machine.   everywhere.
Dependency   Dependencies must be All dependencies are
Management   manually installed on   packaged inside the
each system.   Docker image.
Portability   Code may work   Works the same on
differently on   any system that
different systems.   supports Docker.
Collaboration   Difficult to share the   Easy sharing via
exact working   Docker images.
environment.
********** 17 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper a0f63e0daf6d

- Departments: Artificial Intelligence
- Programmes: MBATech AI 7051
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_AI_7051/Agile Product Development with DevOps/ANS_Agile Product Development with DevOps(702AI0C022)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 30 Jun 2026
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (AI)/B. Tech (AI & DS)/B. Tech (AI & ML)/MBA Tech (AI)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Agile Product Development with DevOps
Date: 30 Jun 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 17 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions.
4. Answer to each new question to be started on a fresh page.
5. Figure in right hand side indicates full marks.
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume suitable data if necessary.
Q1
Answer briefly:   [20]
CO- 1;   a Explain Prototyping Model in detail. Support your answer with diagram.
SO-6;   5
BL-1   Phases – 4 Marks
Diagram -1 Mark
In the Prototyping Model, an initial prototype (a working version) of the
software is built and refined through multiple iterations based on user
feedback.
Phases of Prototyping Model:
1. Requirement Gathering – Collect initial requirements.
2. Quick Design – Create a basic system structure.
3. Prototyping – Develop a working prototype.
4. User Evaluation – Get feedback from users.
5. Refinement – Improve the prototype based on feedback.
6. Final Development – Convert the refined prototype into a full
system.
********** 1 **********

[Text in pictures on this page, read by OCR]
Build Prototype

va Ne customer

Requirements
. . Cust satisfied .
Gathering —> Quick Design Evaluation of Design
Prototype J
x / Implement
Refine a5
Requirements

Test

Maintenance
--- page 2 ---
CO-1,2;   b
SO- 5;   Explain the purpose and usage of the following Git commands with   5
BL-2,3   examples: git init, git add, git commit, and git status.
Commands Explanation (4 Marks):
• git init – Initializes a repository (1 Mark)
• git add – Stages changes (1 Mark)
• git commit – Saves changes with message (1 Mark)
• git status – Shows file status (1 Mark)
Example (1 Mark):
git init → git add file.txt → git commit -m "Initial commit"
CO-1,2;   c
Explain the process of plugin installation and upgrade in Jenkins.   5
SO-6;
BL-3,4   Marking Scheme (Step-wise)
• Definition/role of plugins – 1Mark
•   Installation process – 2Marks
• Upgrade process – 1.5Marks
• Importance/benefits – 0.5Marks
Model Answer
Jenkins plugins are extensions that enhance the functionality of Jenkins by
enabling integration with various tools and adding new features.
Plugin Installation Process
Plugins can be installed using the Jenkins Plugin Manager:
• Navigate to “Manage Jenkins”
•   Select “Manage Plugins”
• Search for the required plugin
•   Select and install the plugin
•   Restart Jenkins (if required)
This allows Jenkins to support additional tools like version control systems,
cloud services, and build tools.
Plugin Upgrade Process
Jenkins periodically checks for plugin updates.
• Go to Plugin Manager
• View available updates
•   Select plugins to upgrade
•   Install updates and restart Jenkins
Importance
• Enhances Jenkins capabilities
• Keeps system updated and secure
• Enables integration with modern tools
********** 2 **********
--- page 3 ---
Thus, plugin management is essential for maintaining an efficient CI/CD
environment.
CO-2,3;   d
SO-6 ;   How Docker images and containers are created and managed in Docker   5
BL-2,3   Environment?
How – 2.5 Marks
Managed – 2.5 Marks
Creating and Managing Docker Images
Docker images are read-only, immutable templates that serve as blueprints
for containers.
Creation (Build):
Dockerfile: Developers write a Dockerfile containing sequential instructions
(e.g., FROM, RUN, COPY, CMD) to assemble the image.
Layered Architecture: Each instruction in a Dockerfile creates a new layer.
This makes images lightweight as layers can be cached and reused across
different images.
Build Command: Running docker build -t image_name:tag . compiles the
Dockerfile into a usable image.
Management:
Storage (Registries): Images are stored and shared in Docker Registries, with
Docker Hub being the default public option.
Listing & Removal: Users view local images with docker images and can
remove unused ones with docker rmi image_name to save space.
Versioning: Images are managed using tags (e.g., ubuntu:22.04) to
distinguish between different versions.
2. Creating and Managing Docker Containers
A container is a live, runnable instance of an image that includes an additional
writable layer for temporary data.
Creation and Execution:
Run Command: The command docker run <image_name> pulls the image if
it's missing, creates the container, and starts it immediately.
Create Command: Alternatively, docker create <image_name> prepares a
********** 3 **********
--- page 4 ---
container in a "Created" state without starting it.
Lifecycle Management:
States: Containers transition through several states: Created (ready), Running
(active), Paused (processes frozen), Stopped (shutdown gracefully), and
Deleted (removed).
Control Commands:
docker start/stop: Initiates or halts a container.
docker pause/unpause: Suspends or resumes container processes without a
full shutdown.
docker rm: Permanently removes a stopped container.
Q2   a   10
CO-1;   A large enterprise with 40+ teams is transitioning from Waterfall to
SO-6;   Agile. Some teams follow Agile strictly, while others resist change.
BL-1   Integration issues and inconsistent practices are causing project delays.
Analyze the challenges of scaling Agile. How can an Agile mindset,
principles, and   coordination mechanisms improve   large-scale
development?
Analyze the challenges – 5Marks
How – 5 Marks
Transitioning a large enterprise with 40+ teams from Waterfall to Agile
is a complex, high-stakes endeavor that involves navigating deep-seated
cultural resistance and technical hurdles. The scenario described—some
teams practicing Agile strictly while others resist—indicates a lack of
consistent, organizational-level adoption (or "agile theater").
Challenges of Scaling Agile (40+ Teams)
Scaling Agile goes beyond just applying Scrum; it requires addressing
structural, cultural, and technical bottlenecks.
• Deep Cultural Resistance & "Agile Theater": Resistance often
stems from fear of job insecurity, loss of control by managers, and
comfort with old processes. When change is forced rather than
adopted, organizations may exhibit "agile theater," where teams go
through the motions (e.g., daily stand-ups) without actually
following agile principles.
********** 4 **********

[Text in pictures on this page, read by OCR]
AGILE MANIFESTO

FOUR CORE VALUES & TWELVE PRINCIPLES

Deliver Early & Often
Embrace Change 4 1.

Release Frequently
Collaborate Daily ¢ > 02. hoch
Empower Teams Working software

Talk Face-to-Face over comprehensive documentation
Measure by Working Software 03. Castomer:
Maintain Sustainable Pace Fone a fern
Focus on Quality 04.
Keep It Simple Poi ron beri

Trust Self-Organizing Teams
Reflect & Improve
--- page 5 ---
Integration Issues & Hidden Dependencies: As described, multiple
teams working on a single project create significant dependencies,
causing "module integration issues" and code quality problems. A lack
of unified, automated testing (CI/CD) makes integrating 40+ teams' work
extremely challenging
•   Inconsistent Practices & Low Maturity: When some teams are
"strict" and others are not, it leads to communication failures and
misalignment in delivery, resulting in inconsistent practices.
•   "Wagile" or "Scrumfall" Behaviour: Many teams end up in a
hybrid state where they use short-term Sprints but keep long-term, fixed,
rigid Waterfall planning.
•   Lack of Leadership Support: A common failure factor is when
senior management advocates Agile but does not change the traditional
"command-and-control" management style.
Improving Large-Scale Development
To overcome these challenges, a shift in mindset, reinforced by proper
structure, is required.
1. Fostering an Agile Mindset and Principles
•   Leadership Alignment and Servant Leadership: Leaders must stop
managing tasks and start enabling teams. This involves transitioning
from "command-and-control" to "servant leadership," where managers
remove impediments for teams.
•   Create a Culture of Psychological Safety: A blameless
environment is needed to encourage learning from mistakes, rather than
punishing teams for delays that are often the result of complex, systemic
issues.
•   Focus on Value, Not Velocity: Teams should be trained to focus
on delivering valuable, working software to customers, rather than just
maximizing "story points".
2. Coordination Mechanisms for Scale
•   Scaled Agile Frameworks (e.g., SAFe, LeSS): For 40+ teams, a
structured framework   is   essential to coordinate dependencies.
Techniques like a "Master Product Backlog" or "Scrum of Scrums"
provide an overview of all products and align team goals.
• Communities of Practice (CoPs): To harmonize inconsistent
practices, create CoPs where developers, Scrum Masters, and
Product Owners from different teams meet voluntarily to share
best practices, tools, and lessons learned.
•   Cross-functional and Self-organizing Teams: Break down silos by
ensuring teams are truly cross-functional (including testers,
developers, and designers) so they can complete a user story
without depending on external teams.
********** 5 **********
--- page 6 ---
• Automated Continuous Integration (CI/CD): To solve integration
issues, automated integration testing must be implemented to
ensure that code from different teams can be tested immediately,
reducing "late-discovery" defects.
• Agile Training and Dedicated Coaching: Invest in professional
training for all levels—not just developers—to ensure a common
understanding of Agile values, mitigating resistance caused by a
lack of knowledge.
CO-1;   b
What is the essential preparation requiring before starting a new project on 10
SO-6;   DevOps platform, and how can each step be detailed?
BL-1,2
For each point of explanation require 2 marks total 5X2=10 marks
Preparing for a new project on a DevOps platform requires a holistic
approach that aligns culture, processes, and tools before code is written.
Essential preparations include creating a strategy, building a cross-functional
team, automating infrastructure, setting up CI/CD pipelines, and establishing
monitoring.
1. Define Strategy and Goals (Planning Phase)
Before selecting tools, define what success looks like to ensure the project
aligns with business objectives.
•   Create a DevOps Roadmap: Develop a step-by-step transformation
plan. Document this roadmap in a central, accessible location (like
Confluence or Jira) to keep all stakeholders aligned.
•   Establish Key Performance Indicators (KPIs): Define metrics like
Deployment Frequency, Lead Time for Changes, Mean Time to Recovery
(MTTR), and Change Failure Rate.
•   Adopt Agile Project Management: Structure the work using Agile
methodologies (Scrum/Kanban) to break the project into small, manageable
sprints.
2. Build and Train the Team (Cultural Preparation)
DevOps is a cultural shift, not just a technical one.
•   Assemble Cross-Functional Teams: Combine developers, operations
engineers, QA, and security specialists into a single team with shared
responsibility.
•   Foster Collaboration: Set up communication channels (e.g., Slack,
Teams) to break down silos. Implement "You build it, you run it"
ownership.
•   Conduct Training Workshops: Ensure the team is proficient in new
tools, Git branching models, and security practices.
3. Select and Setup the Toolchain
Choose a set of integrated tools rather than attempting to buy one single
"DevOps product".
•   Version Control Setup (Git): Create a source code repository
(GitHub, Bitbucket) and define a branching strategy (e.g., GitHub Flow or
Trunk-Based Development).
********** 6 **********
--- page 7 ---
•   Infrastructure as Code (IaC): Prepare to use tools like Terraform or
Ansible to define infrastructure in text-based configuration files, allowing
repeatable and auditable deployments.
•   Tool Integration: Integrate work tracking (Jira) with source control
(Bitbucket/GitLab) to provide full visibility from planning to deployment.
4. Implement CI/CD and Testing Frameworks
Automating the building, testing, and deployment of code is essential.
•   Continuous Integration (CI): Establish automated pipelines (Jenkins,
GitHub Actions) that pull code, run tests, and build artifacts immediately
after a commit.
•   Automated Testing Setup: Create a repository of unit, integration,
and security tests that run automatically on every pull request.
•   Continuous Delivery (CD): Ensure the code is always in a deployable
state by automating the promotion of code to staging and production
environments.
5. Establish Operational Readiness (Monitoring & Security)
The project should be observable and secure from the start.
•   Set Up Continuous Monitoring: Implement logging and monitoring
tools (Prometheus, Grafana, ELK Stack) to monitor application
performance and system health.
•   Create Runbooks: Document operational procedures to guide the
team in resolving common issues.
•   Embed Security (DevSecOps): Integrate security scanning
(SAST/DAST) directly into the CI/CD pipeline. Use a secrets management
system rather than storing keys in code.
Q3   a A DevOps team is managing a project using Git and remote repositories.   10
CO-1,2;   They encounter:
SO-5;   • Difficulty syncing local and remote repositories.
BL-3   • Confusion between git fetch and git pull.
• The need to revert to a previous stable version.
• Multiple versions of code needing proper tracking.
• The requirement to collaborate efficiently across teams.
a) Differentiate between git fetch and git pull.
b) How can the project be reverted to a previous version safely?
c) Which commands are used to sync local and remote repositories?
d) How does Git help in version tracking?
e) Why is Git suitable for collaborative development?
a) Fetch vs Pull (3 Marks):
git fetch downloads changes without merging;
git pull downloads and merges changes.
b) Revert to previous version (2 Marks):
Use git revert or git checkout <commit_id>.
c) Sync commands (2 Marks):
git push and git pull.
d) Version tracking (2 Marks):
Git tracks all changes with commits, allowing history and rollback.
********** 7 **********
--- page 8 ---
e) Collaboration (1 Mark):
Enables multiple developers to work simultaneously efficiently.
CO-1,2;   b A team wants to monitor and visualize their CI/CD workflow clearly.   10
SO-6;   Explain how Jenkins Delivery Pipeline helps in visualization and
BL-2,3   management of different stages.
Marking Scheme (Refined)
•   Introduction to Delivery Pipeline – 2M
•   Explanation of stages (commit, test, deploy) – 3M
•   Visualization and working mechanism – 3M
•   Benefits and practical importance – 2M
Model Answer
Jenkins Delivery Pipeline is a visualization tool that provides a clear
graphical representation of the Continuous Delivery process. It helps teams
monitor and manage different stages of the CI/CD workflow.
Concept of Delivery Pipeline
A delivery pipeline represents the flow of software from code commit to
deployment. It organizes the workflow into multiple stages such as build,
test, and deployment. Each stage contains one or more tasks (jobs), and the
pipeline shows how these stages are connected.
Stages in Delivery Pipeline
1. Commit Stage
• Code is integrated into the repository
•   Initial build and basic tests are performed
2. Test Stage
• Advanced testing such as integration and system testing
• Ensures application quality
3. Deployment Stage
•   Application is deployed to staging or production environment
•   Final validation before release
Visualization and Working
• The Delivery Pipeline plugin displays all stages in a pipeline view
• Each stage is represented visually with status indicators
(success/failure)
•   It shows the flow from one stage to another
•   Provides real-time updates of pipeline progress
This helps teams easily track:
•   Current stage of execution
•   Failed stages
•   Latest successful builds
Benefits
• Improves visibility of CI/CD process
• Helps identify bottlenecks quickly
• Enhances team collaboration
•   Provides better monitoring and control
********** 8 **********
--- page 9 ---
Q4   a
What is a Dockerfile? Explain its structure and commonly used instructions   10
(FROM, RUN, CMD, COPY, etc.) with an example.
What – 1 Mark
Structure – 3 Marks
Instructions & example - 6
A Dockerfile is a script containing instructions to build a Docker image.
Sample Dockerfile:
FROM node:14
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "app.js"]
Explanation:
• FROM → base image
• WORKDIR → working directory
• COPY → copy files
• RUN → install dependencies
CO-2,3;   • CMD → run application
SO-6;
BL-1,2   Dockerfile automates image creation.
Command   Purpose
docker   Starts all services in detached (background) mode.
compose up -d
docker   Stops and removes all containers and networks.
compose down
docker   Lists the status of running services.
compose ps
docker   Follows the live log output from all services.
compose logs
-f
docker   Rebuilds images if the Dockerfile has changed.
compose build
docker   Runs a command inside a running service container.
compose exec
[service]
[cmd]
********** 9 **********
--- page 10 ---
CO-3;   b   Explain Replication Controller and ReplicaSet with suitable diagram. Give   10
SO-6;   the ReplicaSet YAML Walkthrough example.
BL-2,3   Explain & diagram -8 Marks
Example – 2 Marks
Replica Set
ReplicaSet is a process that runs multiple instances of a Pod and keeps the
specified number of Pods constant. let’s take an example where we have a
set of two worker nodes in a cluster as in the above diagram.
we have the front end, running on worker1 and the backend is on the
worker2 node.
The application is working great as long as the pods and nodes are healthy
and running.
Please note, these two pods are running without any controllers backing
these parts as of now.
Replication Controller (RC)
A Replication Controller manages multiple instances of a pod. It uses
equality-based selectors (e.g., app = frontend) to ensure the correct number
of pods are running.
Key Characteristics:
Legacy: Deprecated in favor of ReplicaSets.
Selector Type: Supports only equality-based selectors (key=value).
Behavior: If a node fails, it replaces the pods.
apiVersion: apps/v1   # 1. API Version (apps/v1 for RS)
kind: ReplicaSet   # 2. Resource Type
metadata:
name: frontend-rs   # 3. Name of the ReplicaSet
labels:
app: web
tier: frontend
spec:
replicas: 3   # 4. Desired Number of Pods
selector:
matchLabels:   # 5. Selector to identify pods
tier: frontend   # Must match template labels
template:   # 6. Pod Template
metadata:
labels:   # 7. Labels applied to pods
********** 10 **********
--- page 11 ---
tier: frontend
spec:
containers:
- name: nginx
image: nginx:1.16.1   # 8. Container Image
ports:
- containerPort: 80
Q5   a   Explain the Nagios Remote Plugin Executor with diagram and analyze the   10
CO-4;   role of NRPE in distributed monitoring environments.
SO-6;   Explain & diagram -7 Marks
BL-2,3,4   Analyze – 3 Marks
NRPE (Nagios Remote Plugin Executor) is an agent that allows Nagios to
execute plugins on remote Linux/Unix machines. This is useful for
monitoring system metrics and services that are not externally visible (e.g.,
CPU load, disk usage, memory usage).
1. Monitoring Host
Runs the Nagios Core.
Uses the check_nrpe plugin to communicate with remote systems.
Sends encrypted requests (via SSL) to remote hosts using NRPE.
2. Remote Linux/Unix Host
Runs the NRPE daemon.
Accepts requests from the monitoring host and executes specific monitoring
plugins locally.
Returns the result of these plugins back to Nagios.
3. Communication Flow
Nagios initiates a connection using check_nrpe.
A secure (SSL) connection is established with the NRPE daemon on the
remote host.
NRPE executes local Nagios plugins (like check_disk, check_load, etc.).
These plugins collect data from local resources/services or query other
remote services.
The results are sent back to Nagios for analysis and alerting.
Core Role in Distributed Environments:
********** 11 **********
--- page 12 ---
Secure Remote Execution: NRPE allows execution of Nagios plugins on
remote hosts, returning results via an encrypted (SSL) connection, which is
more secure and efficient than using SSH for every check.
Segmented Network Monitoring: It enables monitoring of servers behind
firewalls or in DMZs. The NRPE daemon on the remote machine (port
5666) only needs to accept connections from the central monitoring server,
simplifying firewall configuration.
Reduced Monitoring Overhead: By running checks locally on the target
machine and only sending the result back, NRPE reduces the load on the
central monitoring server compared to active, network-intensive polling.
Indirect Proxy Monitoring: NRPE can be configured to act as a proxy,
allowing the monitoring server to check resources on remote networks that
are not directly reachable, provided the NRPE host has access.
Scalability: NRPE is essential for scaling Nagios to monitor hundreds or
thousands of nodes, commonly used in distributed, redundant, or failover
configurations
CO-3;   b   Explain the architecture of Kubernetes. Describe the role of master and   10
SO-6;   worker node components in detail.
BL-2,3   Explain – 5 Marks
Describe – 5 Marks
Kubernetes follows a client-server architecture designed as a distributed
control system. The architecture is divided into two primary layers: the
Control Plane (Master Node), which serves as the "brain" for making global
decisions, and the Worker Nodes, which act as the "hands" to execute
application workloads.
1. Control Plane (Master Node) Components
The Control Plane manages the cluster's global state and orchestrates tasks
such as scheduling and scaling.
kube-apiserver: The central management point and "front door" of the
cluster. It exposes the Kubernetes API, handles authentication and
authorization, and is the only component that communicates directly with the
cluster's database.
etcd: A distributed, highly available key-value store that serves as the
cluster's "memory" and single source of truth. It stores all cluster data,
including configuration, state, and secrets.
kube-scheduler: The "decision maker" that assigns newly created Pods to
specific worker nodes. It evaluates resource requirements (CPU, memory),
hardware/software constraints, and affinity rules to select the most suitable
node for a
kube-controller-manager: An automation engine that runs multiple controller
********** 12 **********
--- page 13 ---
processes to maintain the "desired state" of the cluster. Key controllers
include:
Node Controller: Monitors node health and responds if a node goes down.
Replication Controller: Ensures the correct number of Pod replicas are
running at all times.
cloud-controller-manager (CCM): Handles cloud-provider-specific logic,
such as managing cloud load balancers or storage volumes.
2. Worker Node Components
Worker Nodes are the machines (physical or virtual) where application
containers actually run.
kubelet: A local agent that runs on every node. It receives Pod specifications
(PodSpecs) from the API server and ensures the containers described in those
specs are running and healthy.
kube-proxy: A network proxy that manages network rules on the node. It
enables communication between Pods and handles request routing for
Kubernetes Services, providing load balancing across Pods.
Container Runtime: The software responsible for actually running the
containers. While Docker was historically common, Kubernetes now
primarily uses runtimes that adhere to the Container Runtime Interface (CRI),
such as containerd or CRI-O.
Q6   a   Explain the architecture of Prometheus and discuss how its pull-based   10
CO-2,3;   model differs from push-based monitoring systems.
SO-6;   Explain – 5 Marks
BL-2,3
Discuss pull base & push based – 5 Marks
Prometheus is a popular open-source monitoring and alerting system
written in Golang, capable of collecting and processing metrics from
various targets.
You can also query, view, analyze the metrics and get alerted based on the
thresholds.
Prometheus collects and stores its metrics as time series data, i.e. metrics
information is stored with the timestamp at which it was recorded, alongside
optional key-value pairs called labels.
********** 13 **********
--- page 14 ---
Feature   Pull-Based (Prometheus)   Push-Based (Traditional)
Data Flow   Server actively requests data   Targets actively send data to the
from targets.   server.
Health   Inherently knows if a target   Harder to distinguish between a
Check   is down if the pull fails.   "quiet" system and a system that is
down.
Control   Server controls the load and   Server can be overwhelmed if many
frequency of data collection.   targets push data simultaneously.
Configurati   Centralized in the monitoring   Decentralized; every target must
on   server.   know the server's address.
Security   Pulling often requires open   More secure for targets as they only
ports on targets (potential   need outbound connections.
risk).
Best Use   Long-running services and   Short-lived jobs or systems behind
Case   dynamic cloud environments.   strict firewalls.
CO-1;   b   Compare Agile Methodologies with Traditional Approaches of Project   10
SO-6;   Management. Also write about the limitations of Agile Methodology.
BL-1
Compare - 6 Marks
Limitations -4 Marks
Feature   Agile Methodology   Traditional (Waterfall
Workflow   Iterative & Incremental: Projects are   Linear & Sequential: F
broken into short cycles called "sprints"   path: Initiation → Plann
(2-4 weeks).   → Monitoring → Closu
Flexibility   High: Welcomes late-stage changes and Low: Changes often req
evolving requirements.   approvals and can disru
timelines.
Documentation   Minimal: Prioritizes working software   Comprehensive: Heavi
over extensive records.   detailed upfront plannin
********** 14 **********
--- page 15 ---
Customer Role   Continuous Involvement: Customers   Upfront Involvement: Customers are
provide feedback after every iteration.   typically involved only during initial
planning and final delivery.
Team Structure   Self-Organizing: Cross-functional   Hierarchical: Defined roles with a project
teams with shared ownership and flat   manager holding primary accountability.
hierarchy.
Risk   Reactive: Identified and mitigated   Proactive: Risks are identified and
Management   throughout the project via frequent   planned for extensively before execution
reviews.   begins.
Limitations of Agile Methodology
Despite its flexibility, Agile has several drawbacks that can hinder specific
project types:
Lack of Predictability: Because requirements evolve, it is difficult to
estimate final costs, total resources, or a definitive completion date at the
start.
Documentation Deficiency: Agile's focus on "just-in-time" documentation
can lead to insufficient records for long-term maintenance, legal
compliance, or onboarding new members.
High Time Demands: The method requires constant, high-level interaction
through daily stand-ups and sprint reviews, which can strain team members'
schedules and reduce focus.
Dependency on Customer Availability: If stakeholders are disengaged or
unavailable to provide feedback, the iterative process can stall or result in a
product that misses user needs.
Scope Creep: The inherent flexibility can lead to continuous feature
additions without a clear "end goal," causing the project to run beyond its
original intent.
Challenges in Scaling: While effective for small teams, scaling Agile to
large corporations often introduces bureaucratic barriers that erode the
benefits of speed and adaptability.
Incompatibility with Fixed Projects: It is unsuitable for projects where the
final outcome must be fixed from the start, such as construction or heavily
regulated manufacturing.
Q7   a
Explain authentication and authorization in Jenkins’s security.   5
CO-1,2;
SO-6;   Marking Scheme (Step-wise)
BL-2,3   • Authentication explanation – 2M
• Authorization explanation – 2M
•   Difference between both – 1M
Model Answer
Jenkins security is based on two key concepts: authentication and
authorization.
Authentication
Authentication is the process of verifying the identity of a user.
• Ensures that only valid users can access Jenkins
********** 15 **********
--- page 16 ---
• Methods include:
•   Jenkins internal database
• LDAP integration
•   Single Sign-On (SSO)
Authorization
Authorization determines what actions a user is allowed to perform after
authentication.
•   Defines permissions such as read, write, or admin access
Implemented using strategies like:
o Role-based access
o Matrix-based security
Difference
•   Authentication: Verifies identity
•   Authorization: Grants permissions
Together, they ensure secure access control in Jenkins.
CO-1;   b   Give proper explanation for problems on overall delivery process in   5
SO-6;   DevOps process model.
BL-1,2
for each point of explanation 1 marks total 5X1=5 marks
• Waste in having too many handover and decision points in the
process
• Waste due to unnecessary wait time between steps
• Many software changes are packaged up into large, big bang releases
• Large/infrequent releases breed an environment for escaped defects,
bugs
• Releases: seen as something to dread instead a +ve opportunity for
change
• People are disengaged or there is low morale (or both)
• Software changes are not trusted until they have been tested many
times
• Over complex dependencies within the software design
• Value occurs only when the end users are successfully leveraging the
SW
• DevOps aims at providing tighter integration of development and
deployment operations
CO-2,3;   c
Describe the role of Git in version control. How does it help in tracking and   5
SO-6;   managing changes in a project?
BL-2,3
Role of Git (3 Marks):
Git is a version control system that tracks changes, maintains history, and allows
rollback.
Benefits (2 Marks):
Improves collaboration, prevents data loss, and manages versions efficiently.
CO-1,2;   d   Write five differences between traditional software development and   5
SO-5;   software development with Docker.
********** 16 **********
--- page 17 ---
BL-2,3   Use of Docker in   Traditional   Docker Deployment
DevOpsFeature   Deployment
Environment   Different   Same environment
Consistency   environments on   across all machines
different machines   using Docker images.
cause issues.
Setup Complexity   Manual setup of   Pre-configured
software, libraries,   Docker images
and configurations.   eliminate manual
setup.
Error Probability   High chance of errors Reduced errors as
due to manual   everything is bundled
configuration.   in the image.
Deployment Speed   Time-consuming due   Faster as the same
to separate setups for   Docker image runs
each machine.   everywhere.
Dependency   Dependencies must be All dependencies are
Management   manually installed on   packaged inside the
each system.   Docker image.
Portability   Code may work   Works the same on
differently on   any system that
different systems.   supports Docker.
Collaboration   Difficult to share the   Easy sharing via
exact working   Docker images.
environment.
********** 17 **********
````
