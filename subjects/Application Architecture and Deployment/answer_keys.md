# Application Architecture and Deployment: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper fa0c77263aa1

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS) - 7027
- Source: `00_Original_Downloads/2025/Semester II/76514__Final-Exam.zip :: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS) - 7027/Application Architecture & Deployment/ANS_Final-Exam_Application Architecture & Deployment(703DB0E024)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 May 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Application Architecture & Deployment
Date: 09 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. In all ___5_ questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q No.   Part   Question   Model Answer / Key Points   Marks
Q1   a   A healthcare company is building a patient   Start with Monolithic (simpler, faster   5
CO1   management system that needs to handle   to build). Plan Microservices
BL-1,2   appointment booking, medical record   migration for scale.
management, and billing. Initially, they plan to   Monolith: Easier dev/debug initially.
start small but expect exponential user   Microservices: Independent scaling,
growth. Would you recommend a monolithic   fault isolation, separate
or microservices architecture? Justify your   deployability.
answer. How would factors like scalability,   Recommendation: Monolith-first
fault isolation, and independent deployability   with clear migration path.
influence your choice?
b   A university is developing a Student   GET: Retrieve data. POST: Create   5
CO3   Information System using REST APIs. The   resource. PUT: Full update. PATCH:
BL-1,2,3   system should allow students and admins to   Partial update. DELETE: Remove
create, retrieve, update, and delete student   resource.
records. Explain the different REST API   Example: GET /records → fetch all;
methods (GET, POST, PUT, PATCH, DELETE)   POST /records → add new; DELETE
with examples related to managing student   /records/{id} → remove.
records.
c   Explain the concept of Virtualization. How   Virtualization: Full OS per VM via   5
CO2   does it differ from Containerization? State key   Hypervisor (VMware, KVM). Heavy,
BL-   advantages of containerization.   slow.
1,2,3,4   Containerization: Shares host OS
kernel. Lightweight, fast (Docker).
Key: Dockerfile → Image →
Container.
Advantages: Portability, consistency,
fast startup, resource efficiency.
d   What is a Kubernetes Service? Explain the   Kubernetes concepts: Pods (smallest   5
CO4   types of Kubernetes Services (ClusterIP,   deployable unit), Services (stable
BL-   NodePort, LoadBalancer).   networking), ConfigMaps (non-
2,3,4,5,6
********** 1 **********
--- page 2 ---
Q No.   Part   Question   Model Answer / Key Points   Marks
sensitive config), Secrets (sensitive
data, base64 encoded).
Namespace: Logical cluster isolation
for multi-team environments.
Q2   a   Explain the essential qualities of a well-   API Threats: Injection, Broken Auth,   10
CO1   designed software architecture. Cover aspects   Excessive Data Exposure, IDOR, Rate
BL-1,2,3   such as scalability, maintainability, availability,   Limit Bypass.
and security. Why are these characteristics   Mitigation: JWT/OAuth2 for auth,
critical for enterprise applications?   HTTPS always, input validation, rate
limiting, RBAC.
API Keys: Simple but not scalable.
JWT: Stateless, preferred. OAuth2:
Delegated authorization.
b   Compare REST, SOAP, GraphQL and gRPC APIs.   Refer to lecture notes and   10
CO3   Highlight their advantages, disadvantages, and   prescribed textbooks for detailed
BL-2,4   best use-case scenarios for each.   answer.
Key concepts: Compare REST, SOAP,
GraphQL and gRPC APIs. Highlight
their advantages, disadvantages,
and best use-c...
Apply relevant diagrams, code
examples, and real-world scenarios
in exam.
Q3   a   TechStart, an EdTech company, has multiple   Refer to lecture notes and   10
CO5   developers building different modules of their   prescribed textbooks for detailed
BL-1,3,4   online learning platform — courses, users,   answer.
payments, and video streaming.   Key concepts: TechStart, an EdTech
Challenges:   company, has multiple developers
1. Each developer uses a different OS and   building different modules of their
Python version causing 'it works on my   online lea...
machine' issues.   Apply relevant diagrams, code
2. Deploying updates requires manual   examples, and real-world scenarios
configuration across servers.   in exam.
3. New developers take days to set up their
local environment.
Explain how Docker resolves these challenges.
Describe the role of a Dockerfile and write one
for a simple Flask application that returns
'Welcome to TechStart!' on port 8080.
Explain how to build and run this container.
b   Explain the Kubernetes architecture. Describe   Kubernetes concepts: Pods (smallest   10
CO3   the roles of the Master Node components (API   deployable unit), Services (stable
BL-1,3   Server, etcd, Scheduler, Controller Manager)   networking), ConfigMaps (non-
and Worker Node components (kubelet, kube-   sensitive config), Secrets (sensitive
proxy, container runtime).   data, base64 encoded).
Namespace: Logical cluster isolation
for multi-team environments.
Q4   a   Explain the common security threats faced by   API Threats: Injection, Broken Auth,   10
CO5   REST APIs (such as injection attacks, broken   Excessive Data Exposure, IDOR, Rate
BL-1,3,4   authentication, excessive data exposure).   Limit Bypass.
Additionally, describe the steps and tools to
********** 2 **********
--- page 3 ---
Q No.   Part   Question   Model Answer / Key Points   Marks
secure APIs effectively, including use of JWT,   Mitigation: JWT/OAuth2 for auth,
OAuth2, and HTTPS.   HTTPS always, input validation, rate
limiting, RBAC.
API Keys: Simple but not scalable.
JWT: Stateless, preferred. OAuth2:
Delegated authorization.
b   Explain the role of Docker in modern DevOps   Refer to lecture notes and   10
CO4   workflows. Describe Docker Engine, Docker   prescribed textbooks for detailed
BL-1,4   Hub, Docker Images, Docker Containers, and   answer.
Docker Volumes. Compare Docker-based   Key concepts: Explain the role of
deployment to traditional VM-based   Docker in modern DevOps
deployment.   workflows. Describe Docker Engine,
Docker Hub, Docker Im...
Apply relevant diagrams, code
examples, and real-world scenarios
in exam.
Q5   a   A fintech company is deploying a real-time   Kubernetes concepts: Pods (smallest   10
CO3   fraud detection API on Kubernetes. The API   deployable unit), Services (stable
BL-1,2   handles unpredictable traffic spikes during   networking), ConfigMaps (non-
shopping festivals.   sensitive config), Secrets (sensitive
1. Which Kubernetes features would you use   data, base64 encoded).
for automatic scaling? Explain HPA (Horizontal   Namespace: Logical cluster isolation
Pod Autoscaler) and how it works.   for multi-team environments.
2. How would you configure liveness and
readiness probes to handle container health?
3. Suggest a deployment strategy (Rolling
Update / Blue-Green) to deploy updates with
zero downtime.
b   A retail company's e-commerce application is   HPA: Scales pod replicas based on   10
CO4   currently monolithic. As the business grows, it   CPU/memory metrics. Requires
BL-1,2,3   faces issues with slow deployments, scaling   Metrics Server.
bottlenecks, and difficulty adding new   VPA: Adjusts CPU/memory requests
features.   per pod.
1. What specific scaling and maintenance   Liveness Probe: Restarts unhealthy
challenges are they likely facing?   container. Readiness Probe:
2. Outline a step-by-step strategy to migrate   Removes from LB until ready.
from the monolithic system to a microservices   Strategy: Rolling Update (zero
architecture while ensuring business   downtime) vs Blue-Green (instant
continuity.   switch).
Q6   a   Your team is deploying a sentiment analysis   CI: Automated build + test on each   10
CO2   ML model as a REST API. You want to use CI/CD   commit. CD: Automated deployment
BL-   for automated testing and deployment.   to production.
1,3,4,6   1. Explain Continuous Integration (CI) and   MLOps adds: data versioning, model
Continuous Deployment (CD) and their   evaluation gates, drift monitoring,
significance in MLOps.   retraining pipelines.
2. Describe the key steps in setting up a CI/CD   Tools: GitHub Actions, Jenkins,
pipeline for this ML API using GitHub Actions.   MLflow, DVC, Prometheus/Grafana
3. What challenges are specific to CI/CD for ML   for monitoring.
models and how would you address them?
b   A healthcare SaaS platform is built using   Kubernetes concepts: Pods (smallest   10
CO4   microservices: Auth Service, Patient Service,   deployable unit), Services (stable
BL-1,2,3   and Appointment Service.   networking), ConfigMaps (non-
********** 3 **********
--- page 4 ---
Q No.   Part   Question   Model Answer / Key Points   Marks
1. What is Docker Compose and how does it   sensitive config), Secrets (sensitive
help manage this multi-container setup?   data, base64 encoded).
2. Write a docker-compose.yml to define and   Namespace: Logical cluster isolation
run these three services, each as a Python   for multi-team environments.
Flask app.
3. Explain how inter-service communication
and networking works in Docker Compose.
Q7   a   You are deploying a trained churn prediction   Kubernetes concepts: Pods (smallest   10
CO4   ML model as a Flask REST API using Docker,   deployable unit), Services (stable
BL-1,2   Kubernetes, and CI/CD pipelines.   networking), ConfigMaps (non-
Explain the process of containerizing the Flask   sensitive config), Secrets (sensitive
ML model and advantages over bare-metal   data, base64 encoded).
deployment.   Namespace: Logical cluster isolation
How can Kubernetes manage, scale, and   for multi-team environments.
monitor this containerized ML model? Mention
Deployments, Services, and HPA.
Outline a CI/CD pipeline from code commit to
Kubernetes deployment, including testing,
image build, and rollout stages.
b   A food delivery startup is designing a new   HLD: System-level view —   10
CO5   mobile application similar to Zomato. The   architecture, components, APIs, data
BL-2,3,5   team must prepare HLD and LLD before coding   flow, tech stack.
begins.   LLD: Code-level view — class
Explain the differences between High-Level   diagrams, DB schema, method
Design (HLD) and Low-Level Design (LLD) in   signatures, algorithms.
software architecture.   Both required: HLD aligns
For the food delivery app, describe what   stakeholders; LLD guides developers.
aspects would be covered under HLD (system   Skipping HLD causes rework;
components, APIs, databases) and what under   skipping LLD causes inconsistent
LLD (class design, method signatures, database   implementations.
schema).
Why is it essential to complete both HLD and
LLD before starting development?
********** 4 **********
````

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper d011a7c948a4

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Application Architecture & Deployment/ANS_Application Architecture & Deployment(703DB0E024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Dec 2025
- Text: mixed (3 pages), mean OCR confidence 21.9
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY (ARTIFICIAL INTELLIGENCE)
Year: I/Semester I(Exam Year: 2025-2026)
Subject: Application Architecture & Deployment
Date: 05 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question 1 is compulsory
5. Attempt any four from remaining
Q1
Answer briefly:   Marks
a. Common types include Monolithic Architecture, where all components are tightly
CO-1 ;   coupled in one application, and Microservices, a collection of small, independent
SO-2 ;   services. Other essential types are Layered (N-Tier), separating presentation, logic, [5]
BL-3   and data; Service-Oriented Architecture (SOA), and Event-Driven Architecture
(EDA), based on state changes.
b   APIs promote interoperability by allowing disparate systems to communicate using [5]
CO-2 ;   standardized contracts. They ensure modularity and decoupling by hiding
SO-2 ;   implementation details (abstraction). APIs enhance security by enforcing strict
BL-2   access control and accelerate development by reusing existing functionality (e.g.,
payment gateways).
c   Virtualization (VMs) isolates systems at the hardware layer, requiring a full guest OS   [5]
CO-3 ;
for high security, but resulting in large footprints and slow boot times.
SO-2 ;
Containerization isolates at the OS level, sharing the host kernel. Containers are
BL-1
significantly lighter, faster to boot, and highly resource-efficient, ideal for density.
d Docker is used for building, packaging, and running containerized applications, ideal [5]
CO-4 ;   for local development or simple, single-instance deployments. Kubernetes is used
SO- 2;   for orchestration, managing large clusters of containers, handling automated
BL-3   scaling, load balancing, and ensuring high availability for complex production
microservices
a. Microservices structure an application as a collection of small, autonomous, and
Q2
independently deployable services, usually communicating via APIs. Advantages
CO-1;
include improved scalability, technological flexibility, and fault isolation.   [10]
SO-2;
Disadvantages involve significant operational complexity, challenging distributed
BL-2   transactions, and overhead in monitoring and networking.
b. A Monolith is a single, tightly coupled application sharing one database, requiring   [10]
Q2
redeployment for any change. Microservices are loosely coupled, deployed
CO-2;
independently, and often use decentralized databases. Monoliths are simpler
SO-2;
initially but hard to scale and update; Microservices are complex but offer superior
BL-2   component scalability and resilience.
********** 1 **********
--- page 2 ---
Q3   a. Key API design principles include using resources (nouns), correctly mapping   [10]
HTTP methods (verbs) to actions, ensuring statelessness, and using standard HTTP
CO-3;
status codes and versioning. Testing approaches include Functional Testing
SO-2;
(verifying business logic), Performance Testing (load and stress), and Security
BL-2   Testing (vulnerability assessment).
b. Flask is a Python microframework used to define APIs by mapping URLs to   [10]
Q3
Python functions using @app.route decorators. It leverages jsonify to return
CO-3;
standard JSON responses. Key testing types are Functional Testing (tools: Postman,
SO-2;
Insomnia), Performance Testing (tools: JMeter, k6), and API Automation (tools:
BL-2   Pytest, RestAssured).
a. VMs provide maximum hardware-level isolation and are ideal for running diverse   [10]
Q4
operating systems or legacy applications. Containers offer rapid startup times,
CO3-;
extreme resource efficiency, and high density by sharing the host OS kernel.
SO-2;
Containers are the standard for microservices and CI/CD, while VMs are used for
BL-2
infrastructure consolidation (IaaS).
b. Containerization bundles an application and its dependencies into a portable,   [10]
Q4
executable image, isolated via kernel namespaces and cgroups. This guarantees
CO3-;
consistency across environments, drastically accelerating CI/CD pipelines. Its
SO-2;
advantages over virtualization include a lower resource footprint, near-instant
BL-2
startup, and far higher deployment density.
a. A Kubernetes Deployment is a declarative object managing the update lifecycle of   [10]
Q5
Pods and ReplicaSets, ensuring the desired state is maintained. Benefits include
CO3-;
self-healing, reliable rollouts, and easy rollbacks. Common strategies include
SO-2;
Rolling Updates (gradually replacing old pods) and Blue/Green Deployment
BL-2
(running two full versions simultaneously and switching traffic).
Q5   b. Kubernetes follows a Master-Worker architecture. The Control Plane (Master)   [10]
CO3-;   manages the cluster state using the API Server and stores configuration in etcd.
SO-2;   The Worker Nodes run the application containers via the Kubelet agent and
BL-2   handle network routing with Kube-proxy.
a. SDLC is a framework defining tasks performed at each stage of software   [10]
Q6
development, ensuring quality and efficient progress. Key stages are Planning,
CO4-;
Design, Implementation, Testing, Deployment, and Maintenance. SDLC is essential
SO-2;
because it provides structure, reduces risk, ensures clear requirements, and
BL-6
improves quality assurance through defined milestones.
b. Agile is an iterative SDLC approach emphasizing customer collaboration, rapid   [10]
Q6
delivery of working software, and flexibility over rigid planning. It breaks work into
CO4-;
small sprints, adapting to change quickly. This contrasts sharply with traditional
SO-2;
Waterfall, which is strictly sequential and requires comprehensive planning before
BL-2
any development begins.
a. Docker Swarm is Docker’s native, simpler orchestration tool, focused on ease of   [10]
Q7
setup and use for basic container clustering. Kubernetes is a much more feature-
CO-4;
rich, complex, and standardized system offering advanced networking, auto-
SO-2;
scaling, and security policies. Swarm is suited for quick deployments; Kubernetes
BL-6
handles enterprise-level, complex microservice management.
b. HTTP methods define the action to be performed on a resource in a RESTful API,   [10]
Q7
adhering to the standard CRUD model. GET retrieves resources (Read). POST
CO4-;
creates new resources. PUT fully updates or replaces an existing resource. DELETE
SO-2;
removes a resource. This mapping ensures the API interface is clear, predictable,
BL-2
and stateless.
********** 2 **********
--- page 3 ---
FC QI a iar
````

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper 8ad15695768c

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Application Architecture & Deployment/ANS_Application Architecture & Deployment(703DB0E024)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Apr 2025
- Text: text (3 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Application Architecture & Deployment
Date: 28 Apr 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No 1 is Compulsory .
5. Out of remaining question, attempt any 4.
6. In total 5 questions needs to be answered.
7. All Questions carry equal marks.
Q1
(i) Monolithic vs Microservices Architecture
Microservices architecture is recommended for scalability, maintainability, and deployment flexibility. Initially,
a monolithic approach may be easier, but as the user base grows, microservices allow independent scaling of
different modules like authentication, order processing, and payments. It enables faster deployments and fault
isolation.
(ii) REST API Methods
REST API follows HTTP methods:
- **GET**: Retrieve employee records (`/employees`)
- **POST**: Create a new employee (`/employees` with request body)
- **PUT**: Update the entire employee record (`/employees/{id}`)
- **PATCH**: Modify specific fields (`/employees/{id}` with JSON body)
- **DELETE**: Remove an employee (`/employees/{id}`)
(iii) Containerization & Docker Architecture
Containerization packages applications and dependencies, ensuring consistency across environments. Docker
has components like:
- **Docker Engine**: Core runtime for running containers.
- **Images**: Pre-configured environment snapshots.
- **Containers**: Running instances of Docker images.
- **Docker Hub**: Centralized repository for sharing images.
(iv) Kubernetes: Pod & Deployment
- **Pod**: The smallest deployable unit in Kubernetes, consisting of one or more containers.
- **Deployment**: Manages replica sets and updates, ensuring desired state management.
(v) SDLC and Its Importance
Software Development Life Cycle (SDLC) includes planning, design, coding, testing, deployment, and
maintenance. It ensures systematic development, reducing errors and improving efficiency.
********** 1 **********
--- page 2 ---
Q2
(i) Essential Characteristics of Software Architecture
A well-structured architecture has:
- **Scalability**: Supports growth without performance degradation.
- **Maintainability**: Allows easy modifications.
- **Security**: Protects data and access.
- **Performance**: Ensures responsiveness under load.
- **Modularity**: Breaks the system into manageable components.
(ii) Types of APIs
- **REST**: Stateless, lightweight, widely used.
- **GraphQL**: Allows flexible querying but requires a learning curve.
- **SOAP**: Secure but verbose.
- **gRPC**: High-performance binary communication, ideal for microservices.
Q3
(i) Docker Benefits & Dockerfile Example
Docker ensures uniform environments and simplifies deployment. A **Dockerfile** defines the image,
specifying dependencies and configurations.
Example Dockerfile for Flask:
```
FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install flask
CMD ["python", "app.py"]
```
(ii) Kubernetes Architecture
Key components:
- **Master Node**: API Server, Controller Manager, Scheduler.
- **Worker Nodes**: Kubelet, Kube Proxy, Pods.
- **etcd**: Cluster state storage.
Q4
(i) API Security Threats & Protection
Common threats include SQL Injection, Cross-Site Scripting (XSS), and Man-in-the-Middle attacks.
Protection methods: Authentication (OAuth, JWT), Rate limiting, API gateways.
(ii) Docker in Modern Deployment
Docker enables consistent environments, isolates dependencies, and reduces overhead compared to virtual
machines. Key components: Docker Engine, Images, Containers, Registry.
Q5
(i) Kubernetes for Auto-Scaling & Load Balancing
- **Horizontal Pod Autoscaler (HPA)** scales based on CPU/Memory usage.
- **ReplicaSets** maintain redundancy.
- **Load Balancer** distributes traffic among pods.
- **Liveness & Readiness Probes** ensure uptime.
********** 2 **********
--- page 3 ---
(ii) Monolithic to Microservices Transition
Challenges: Scalability issues, slow deployments, difficult maintenance.
Transition strategy: Identify services, create APIs, use containerization, and migrate incrementally.
Q6
(i) CI/CD for Machine Learning
Continuous Integration (CI) automates testing, while Continuous Deployment (CD) automates releases.
Steps: Code commit -> Testing -> Build -> Deployment using GitHub Actions & AWS EC2.
(ii) Docker Compose for Microservices
Docker Compose simplifies managing multiple services:
```
version: '3'
services:
user:
image: user-service
item:
image: item-service
order:
image: order-service
```
Q7
(i) Deploying ML Model with Docker & Kubernetes
Docker ensures containerization, and Kubernetes automates scaling and load balancing.
CI/CD enables automated testing and deployment to cloud-based Kubernetes clusters.
(ii) High-Level vs Low-Level Design in Ride-Sharing Apps
HLD covers overall system architecture, components, and data flow.
LLD details class structures, database schemas, and API contracts.
Both are crucial for structured development.
********** 3 **********
````

## 2024-25 · Re-Exam · Sem 2 · Answer key · paper 191fb011825e

- Departments: Data Science
- Programmes: MASTER OF TECHNOLOGY - DATA SCIENCE (BU
- Source: `02_Question_Papers/2024/Sem_02/Re-Exam/MASTER OF TECHNOLOGY - DATA SCIENCE (BU_db368963/Application Architecture & Deployment/ANS_Application Architecture & Deployment(703DB0E024)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2025
- Text: text (3 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF TECHNOLOGY - DATA SCIENCE (BUSINESS ANALYTICS)
Year: I/Sem 2 Re-exam(Exam Year: 2024-2025)
Subject: Application Architecture & Deployment
Date: 01 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No 1 is Compulsory .
5. Out of remaining question, attempt any 4.
6. In total 5 questions needs to be answered.
7. All Questions carry equal marks.
Q1
(i) Monolithic vs Microservices for Real-time Chat Application
Microservices architecture is recommended due to its ability to scale individual components like messaging,
user authentication, and notifications separately. It ensures low-latency communication and better
maintainability by allowing independent updates and deployments.
(ii) ReplicaSets & Services in Kubernetes
- **ReplicaSets** ensure the desired number of pod replicas are running.
- **Services** expose pods to other components or the internet and enable load balancing.
(iii) SDLC Phases & Their Importance
1. **Planning** - Requirement gathering.
2. **Design** - System architecture definition.
3. **Development** - Coding and implementation.
4. **Testing** - Identifying bugs and ensuring quality.
5. **Deployment** - Releasing software to users.
6. **Maintenance** - Updating and fixing issues.
(iv) REST API Methods for Flight Bookings
- **GET**: Retrieve flight details (`/flights/{id}`).
- **POST**: Book a flight (`/flights/book`).
- **PUT**: Update booking details (`/flights/{id}`).
- **PATCH**: Modify passenger name (`/flights/{id}`).
- **DELETE**: Cancel booking (`/flights/{id}`).
(v) Advantages of Containerization & Docker Architecture
Containerization provides isolation, portability, and consistency across environments.
Docker components: Docker Engine, Images, Containers, Docker Hub.
Q2
(i) Principles of Software Architecture
Scalability, modularity, security, performance, and maintainability ensure a robust design.
********** 1 **********
--- page 2 ---
(ii) SOAP vs REST vs GraphQL
- **SOAP**: Secure but heavy.
- **REST**: Simple, widely used.
- **GraphQL**: Flexible data retrieval but complex.
Q3
(i) Docker Benefits for IoT & Dockerfile Example
Docker ensures consistency across IoT environments. Example Dockerfile:
```
FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install flask
CMD ["python", "app.py"]
```
(ii) Kubernetes Architecture
Master Node: API Server, Controller Manager, Scheduler.
Worker Nodes: Kubelet, Kube Proxy, Pods.
etcd: Cluster state storage.
Q4
(i) API Security Best Practices
Common vulnerabilities: SQL Injection, XSS, Man-in-the-Middle attacks.
Protection: OAuth, JWT, API gateways.
(ii) Docker in Software Development
Docker ensures consistency, isolates dependencies, and reduces overhead. Components: Docker Engine,
Images, Containers.
Q5
(i) Kubernetes for Video Streaming Scalability
- **HPA** scales pods automatically.
- **Liveness Probes** restart failed containers.
- **Load Balancers** distribute traffic efficiently.
(ii) Monolithic to Microservices Migration
Challenges: Performance bottlenecks, difficult scaling.
Migration strategy: Identify services, use APIs, containerize components.
Q6
(i) CI/CD for Fraud Detection API
CI automates testing; CD ensures continuous deployment.
Steps: Code commit -> Testing -> Deployment with GitHub Actions & AWS EC2.
(ii) Docker Compose for Microservices
Example `docker-compose.yml` for Students, Courses, and Payments:
```
version: '3'
services:
student:
image: student-service
course:
image: course-service
********** 2 **********
--- page 3 ---
payment:
image: payment-service
```
Q7
(i) Deploying AI Chatbot with Docker & Kubernetes
Docker ensures containerization; Kubernetes automates scaling.
CI/CD automates deployment.
(ii) High-Level vs Low-Level Design for Ride-Hailing App
HLD: Architecture, components, data flow.
LLD: Class structures, database schemas, API contracts.
********** 3 **********
````
