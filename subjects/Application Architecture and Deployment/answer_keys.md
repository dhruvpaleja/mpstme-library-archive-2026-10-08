# Application Architecture and Deployment: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper d011a7c948a4

- Departments: Artificial Intelligence
- Programmes: MASTER OF TECHNOLOGY (ARTIFICIAL INTELL
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF TECHNOLOGY (ARTIFICIAL INTELL_fdd2a5aa/Application Architecture & Deployment/ANS_Application Architecture & Deployment(703DB0E024)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 Dec 2025
- Text: mixed (3 pages), mean OCR confidence 21.9

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
