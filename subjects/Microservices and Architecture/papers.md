# Microservices and Architecture: question papers in full

28 unique papers · 2023-24 to 2025-26 · Computer Engineering, Computer Applications (MCA), Computer Science and Business Systems

Each paper: year, exam, semester, departments and programmes, then its full text as extracted. Scanned papers were read by OCR, so equations and symbols may contain recognition errors. Structured data: [`questions.jsonl`](questions.jsonl) (one record per question) and [`papers.jsonl`](papers.jsonl) (one record per paper). Index of files: [`README.md`](README.md).

## 2025-26 · Final-Exam · Sem 3 · paper 47124f7b2207

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Microservices and Architecture/QP_Microservices and Architecture(703CO0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 Nov 2025
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 24 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted.
5. All questions carry equal marks
6. Figures in brackets on the right hand side indicate full marks
7. Answer to each new question to be started on a fresh page.
Q.1   Answer briefly:   20
a)   Explain API Gateway architecture   5
b)   Write an explanatory note on the Architecture of Apache Kafka.   5
c)   Explain IOC in brief   5
d)   Compare Virtual Machine and Docker   5
Q. 2(a)   Explain Monolithic Application. What are the advantages and Limitations of   10
Monolithic Application?
You are building a Spring Boot application for an online store to manage Product   10
Q. 2(b)   inventory using MySQL with a layered architecture.
Answer the following:
1. Create a Product entity class with suitable annotations and fields (id, name,
price).
2. Define a JPA Repository interface for database operations.
3. Implement a Service Layer to handle business logic for CRUD operations.
4. Develop a REST Controller exposing endpoints to Create, Retrieve,
Update, Delete, and List all products.
5. Configure MySQL connection settings in application.properties.
Q. 3(a)   Explain the purpose of Spring Boot Actuator. How can you implement a custom   10
Health Indicator in a Spring Boot application? Write the necessary steps and code.
Q. 3(b)   Write a Spring Boot application demonstrating inter-service communication.   10
Implement two approaches: one using OpenFeign and another using WebClient
Q. 4(a)   Explain Design Pattern and write a note on   10
• CQRS
• Event Sourcing Design Pattern
********** 1 **********
--- page 2 ---
Q. 4(b) How can you implement a Spring Cloud Config Server and Client with a Refresh   10
Feature?In your answer, include:
1. Configuring application.properties for the Config Client
2. Configuring application.properties for the Config Server
3. Creating a REST Controller to fetch configuration values
4. Adding required dependencies in pom.xml for both Config Server and Client
Q. 5(a)   Suppose you are developing multiple microservices that need to discover each other   10
dynamically.Explain how to set up a Discovery Server using Eureka, and how to
configure two microservices as Eureka Clients with proper settings in
application.properties.
Q. 5(b   Explain the ideal CI/CD pipeline for Spring Boot microservices. Describe each   10
stage from code commit to monitoring and rollback, including the tools commonly
used and key actions performed at each stage. Additionally, explain the benefits of
implementing such a pipeline in a microservices architecture.
Q. 6(a) You are deploying a web application on a Kubernetes cluster that must be highly   10
available, scalable, and accessible to users through a domain name.
Explain how the following Kubernetes objects would be used:
1. Deployment
2. Service
3. ReplicaSet
4. Ingress
Q. 6(b) What is Docker?Explain the process of Dockerizing a Spring Boot Application with   10
MySQL using a Docker Network.
Include:
1. Creation of a Dockerfile and building a custom image
2. Setting up a MySQL container with environment variables in a shared
Docker network
Q. 7(a   Explain the process of converting a monolithic application into microservices.Also,   10
describe the key steps involved in migrating existing monolithic applications to a
microservices architecture.
Q. 7(b)   Write short notes on:   10
1. OAuth 2.0
2. JSON Web Token (JWT
********** 2 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper 750d07e702d0

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/Microservices and Architecture/QP_Microservices and Architecture(702CO0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   A Financial application has a single codebase where UI, business logic,
CO- ;   and database access are tightly coupled. Any minor change requires full
SO- ;   [5]
redeployment. Identify the limitations of monolithic architecture in this
BL-
scenario and explain how they impact scalability and maintenance.
b.   When should the following be used?
CO- ;   i)   RestTemplate:
SO- ;   [5]
ii)   WebClient:
BL-
iii)   OpenFeign:
CO- ;   c.   Why in Microservices, testing becomes more complex compared to legacy
SO- ;   [5]
systems? Explain the role of contract testing, test automation and service
BL-
virtualization in ensuring reliability of Microservices.
d.
CO- ;
SO- ;   What are the benefits of implementing a CI/CD pipeline in modern software [5]
BL-   development?
********** 1 **********
--- page 2 ---
a.   Why do we use Configuration Server in Microservices architecture.
How does it help in managing dependencies? Explain in detail.   [10]
Q2
CO-;
SO-;   Provide steps to develop and run a “Hello World” application using Spring
b.
BL-   Boot.   [10]
a.   Write a note on following?   [10]
(i)   Ribbon
Q3   (ii)   Zuul
CO1-;
SO2-;
b.
BLU-   Why do we need the service discovering and registering process? Explain with
[10]
neat architecture diagram.
a.   What challenges arise in ensuring security and service communication
throughout the Microservices lifecycle?   [10]
Q4   Design and explain REST APIs for an employee management system using
b.
CO-;   operations:
SO-;
BL-   •   Create Employee   [10]
• Get Employee
•   Delete Employee
Specify endpoints, HTTP methods, and sample request/response structures.
a.   What is topic in Kafka. Explain Kafka architecture with a suitable use case.
[10]
Q5
CO-;
SO-;
Why the distributed transactions should be avoided with the use of two-phase
BL-   b.
[10]
commit protocol? How the identified issues can be solved?
********** 2 **********
--- page 3 ---
a.   “Service-to-service communication is managed through an intermediate   [10]
Q6   infrastructure layer.” What is this layer? Explain with architecture diagram.
CO-;
SO-;
BL-
Which integration pattern would be suitable for a food delivery platform
b.
integrates restaurant, delivery, and payment services? Real-time updates are
[10]
required. Justify their use.
Q7   a.   What is OAuth2.0. Explain with Architecture/Sequence diagram. When   [10]
CO-;   should we choose this protocol?
SO-;
BL-   b.
Write steps to migrate Existing Monolithic Applications to Microservices.   [10]
(1 step = 1 mark)
********** 3 **********
````

## 2025-26 · Final-Exam · Sem 6 · paper a1c2421f3e1c

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/Microservices and Architecture/QP_Microservices and Architecture(702CO0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   A Financial application has a single codebase where UI, business logic,
CO- ;   and database access are tightly coupled. Any minor change requires full
SO- ;   [5]
redeployment. Identify the limitations of monolithic architecture in this
BL-
scenario and explain how they impact scalability and maintenance.
b.   When should the following be used?
CO- ;   i)   RestTemplate:
SO- ;   [5]
ii)   WebClient:
BL-
iii)   OpenFeign:
CO- ;   c.   Why in Microservices, testing becomes more complex compared to legacy
SO- ;   [5]
systems? Explain the role of contract testing, test automation and service
BL-
virtualization in ensuring reliability of Microservices.
d.
CO- ;
SO- ;   What are the benefits of implementing a CI/CD pipeline in modern software [5]
BL-   development?
********** 1 **********
--- page 2 ---
a.   Why do we use Configuration Server in Microservices architecture.
How does it help in managing dependencies? Explain in detail.   [10]
Q2
CO-;
SO-;   Provide steps to develop and run a “Hello World” application using Spring
b.
BL-   Boot.   [10]
a.   Write a note on following?   [10]
(i)   Ribbon
Q3   (ii)   Zuul
CO1-;
SO2-;
b.
BLU-   Why do we need the service discovering and registering process? Explain with
[10]
neat architecture diagram.
a.   What challenges arise in ensuring security and service communication
throughout the Microservices lifecycle?   [10]
Q4   Design and explain REST APIs for an employee management system using
b.
CO-;   operations:
SO-;
BL-   •   Create Employee   [10]
• Get Employee
•   Delete Employee
Specify endpoints, HTTP methods, and sample request/response structures.
a.   What is topic in Kafka. Explain Kafka architecture with a suitable use case.
[10]
Q5
CO-;
SO-;
Why the distributed transactions should be avoided with the use of two-phase
BL-   b.
[10]
commit protocol? How the identified issues can be solved?
********** 2 **********
--- page 3 ---
a.   “Service-to-service communication is managed through an intermediate   [10]
Q6   infrastructure layer.” What is this layer? Explain with architecture diagram.
CO-;
SO-;
BL-
Which integration pattern would be suitable for a food delivery platform
b.
integrates restaurant, delivery, and payment services? Real-time updates are
[10]
required. Justify their use.
Q7   a.   What is OAuth2.0. Explain with Architecture/Sequence diagram. When   [10]
CO-;   should we choose this protocol?
SO-;
BL-   b.
Write steps to migrate Existing Monolithic Applications to Microservices.   [10]
(1 step = 1 mark)
********** 3 **********
````

## 2025-26 · Final-Exam · Sem 10 · paper 4f056a07c26c

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_Computer_7032/Microservices and Architecture/QP_Microservices and Architecture(702CO0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 3 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   A Financial application has a single codebase where UI, business logic,
CO- ;   and database access are tightly coupled. Any minor change requires full
SO- ;   [5]
redeployment. Identify the limitations of monolithic architecture in this
BL-
scenario and explain how they impact scalability and maintenance.
b.   When should the following be used?
CO- ;   i)   RestTemplate:
SO- ;   [5]
ii)   WebClient:
BL-
iii)   OpenFeign:
CO- ;   c.   Why in Microservices, testing becomes more complex compared to legacy
SO- ;   [5]
systems? Explain the role of contract testing, test automation and service
BL-
virtualization in ensuring reliability of Microservices.
d.
CO- ;
SO- ;   What are the benefits of implementing a CI/CD pipeline in modern software [5]
BL-   development?
********** 1 **********
--- page 2 ---
a.   Why do we use Configuration Server in Microservices architecture.
How does it help in managing dependencies? Explain in detail.   [10]
Q2
CO-;
SO-;   Provide steps to develop and run a “Hello World” application using Spring
b.
BL-   Boot.   [10]
a.   Write a note on following?   [10]
(i)   Ribbon
Q3   (ii)   Zuul
CO1-;
SO2-;
b.
BLU-   Why do we need the service discovering and registering process? Explain with
[10]
neat architecture diagram.
a.   What challenges arise in ensuring security and service communication
throughout the Microservices lifecycle?   [10]
Q4   Design and explain REST APIs for an employee management system using
b.
CO-;   operations:
SO-;
BL-   •   Create Employee   [10]
• Get Employee
•   Delete Employee
Specify endpoints, HTTP methods, and sample request/response structures.
a.   What is topic in Kafka. Explain Kafka architecture with a suitable use case.
[10]
Q5
CO-;
SO-;
Why the distributed transactions should be avoided with the use of two-phase
BL-   b.
[10]
commit protocol? How the identified issues can be solved?
********** 2 **********
--- page 3 ---
a.   “Service-to-service communication is managed through an intermediate   [10]
Q6   infrastructure layer.” What is this layer? Explain with architecture diagram.
CO-;
SO-;
BL-
Which integration pattern would be suitable for a food delivery platform
b.
integrates restaurant, delivery, and payment services? Real-time updates are
[10]
required. Justify their use.
Q7   a.   What is OAuth2.0. Explain with Architecture/Sequence diagram. When   [10]
CO-;   should we choose this protocol?
SO-;
BL-   b.
Write steps to migrate Existing Monolithic Applications to Microservices.   [10]
(1 step = 1 mark)
********** 3 **********
````

## 2025-26 · Final-Exam · Sem 3 · paper 8c8af7e82be6

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/2ND YEAR/III SEMESTER/Microservice and Architecture/Microservices and Architecture 2025-26 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 Nov 2025
- Text: ocr (2 pages), mean OCR confidence 90.6

````text
SVKMs NMIMS ‘
MUKESH PATEL SCH.OF TECH.MGMT ENGG-

Programme: MASTER OF COMPUTER APPLICATIO
Year: II/Semester WI(Exam Year: 2025-2026)
Subject: Microservices and Architecture

Date: 24 Nov 2025 Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100 .

FINAL EXAMINATION (Acad. Year:2025-2026)

Instructions: s

1. This question paper contains 2 pages.

2. Question No. 1 is compulsory.

3. Out of remaining questions, attempt any 4 questions

4. In all 5 questions to be attempted.

5. All questions carry equal marks

6. Figures in brackets on the right hand side indicate full marks

7. Answer to each new question to be started on a fresh page.

Q.1 Answer briefly: ; 20
a) Explain API Gateway architecture _ 5
b) Write an explanatory note on the Architecture of Apache Kafka. 5
c) Explain IOC in brief 5
d) Compare Virtual Machine and Docker 5

Q. 2(a) | Explain Monolithic Application. What are the advantages and Limitations of - 10
Monolithic Application?
You are building a Spring Boot application for an online store to manage Product 10

Q. 2(b) | inventory using MySQL with a layered architecture.

Answer the following:

1. Create a Product entity class with suitable annotations and fields (id, name,
‘ price). .
2. Define a JPA Repository interface for database operations.
3, Implement a Service Layer to handle business logic for CRUD operations.
4. Develop a REST Controller exposing endpoints to Create, Retrieve,
Update, Delete, and List all products.
5: Configure MySQL connection settings in application.properties.

Q. 3(a) | Explain the purpose of Spring Boot Actuator. How can you implement a custom 10
Health Indicator in a Spring Boot application? Write the necessary steps and code.
Q. 3(b) | Write a Spring Boot application demonstrating inter-service communication. 10

Impjement two approaches: one using OpenFeign and another using WebClient
r

Q. 4(a) | Explain Design Pattern and write a note on 10
* CQRS
e Event Sourcing Design Pattern

FR 7 RRR ®
--- page 2 ---
Q. 4(b) | How can you implement a Spring Cloud Config Server and Client with a Refresh 10
Feature?In your answer, include: H
1. Configuring application.properties for the Config Client ‘
2. Configuring application.properties for the Config Server ~
3. Creating a REST Controller to fetch configuration values “”
4, Adding required dependencies in pom.xml for both Config Server and Client
Q. 5(a)_ | Suppose you are developing multiple microservices that need to discover each-other | 10
dynamically.Explain how to, set up-a Discovery Server using Eureka, and how to
configure two microservices as Eureka Clients with proper settings in ~
application.properties.
Q. 5(b__ | Explain the ideal CI/CD pipeline for Spring Boot microservices. Describe each 10
stage from code commit to monitoring and rollback, including the tools commonly
used and key actions performed at each stage. Additionally, explain the benefits of
implementing such a pipeline in a microservices architecture.
Q. 6(a) | You are deploying a web application on a Kubernetes cluster that must be highly 10
available, scalable, and accessible to users through a domain name.
Explain how the following Kubernetes objects. would be used:
1. Deployment :
2. Service a
3. ReplicaSet
4._ Ingress
Q. 6(b) | What is Docker?Explain the process of Dockerizing a Spring Boot Application with | 10
MySQL using a Docker Network.
Include:
1. Creation of a Dockerfile and building a custom image
2. Setting up a MySQL container with environment variables in a shared
Docker network
Q. 7(a_| Explain the process of converting a monolithic application into microservices.Also, 10
describe the key steps involved in migrating existing monolithic applications to a
microservices architecture.
Q. 7(b) | Write short notes on: 10

1. OAuth 2.0
2. JSON Web Token (JWT

FIG 2 Hk Go ik

4 .
````

## 2025-26 · Re-Exam · Sem 3 · paper 5115784a6c85

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Microservices and Architecture/QP_Microservices and Architecture(703CO0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted.
5. All questions carry equal marks
6. Figures in brackets on the right hand side indicate full marks
7. Answer to each new question to be started on a fresh page.
Q.1   Answer briefly:   20
a)   What is the role of Eureka Server and Eureka Client in a Microservice architecture   5
b)   Compare between Monolithic and Microservice architecture   5
c)   Explain Saga Pattern in detail.   5
d)   Write a note on CI/CD pipeline   5
Q. 2(a) You are developing a Spring Boot application for a company to manage Employee   10
records using MySQL in a structured, layered architecture.
Answer the following:
1. Create an Employee entity class with fields — id, name, and salary.
2. Define a JPA Repository interface for performing database operations.
3. Implement a Service Layer to handle business logic for CRUD operations.
4. Develop a REST Controller exposing endpoints to Create, Retrieve, Update,
Delete, and List all employees.
5. Configure MySQL connection settings in the application.properties file.
Q. 2(b) How can you implement In-Memory Basic Authentication in Spring Boot?In your   10
answer, include:
1. Writing a Security Configuration Class for In-Memory Authentication
2. Creating a Controller to Test Authentication
3. Defining User Roles and Authorities in the Security Configuration
4. Adding Required Dependencies in pom.xml (if using Spring Security Starter)
Q. 3(a) What is the role of an API Gateway in microservices?   10
Explain with example how two microservices (ms1 and ms2) can be registered with
Eureka Server and accessed via API Gateway, including configuration details from
application.properties.
********** 1 **********
--- page 2 ---
Q. 3(b) Write down the step to implement a Spring Cloud Config Server and Client with a   10
Refresh Feature?
Q. 4(a) Describe and draw the core components and working of Kubernetes Architecture.   10
Q. 4(b) Design pattern in Spring Microservices with diagram.   10
Q. 5(a) Explain the Docker Architecture? Create a docker-compose.yml file to run a Spring   10
Boot application with a MySQL database.
Q. 5(b) What are the two ways of Microservice communication?Provide the complete code to   10
implement the communication using Open Feign and RestClient
Q. 6(a) Draw and Explain the architecture of Apache Kafka with the help of a simple diagram,   10
describing the roles of Producer, Topic, Partition, Broker, and Consumer.
Q. 6(b) Explain Mike Cohn's original test pyramid with diagram? Types of Testing in Spring   10
boot Microservices
Q. 7(a) Write a Spring Boot program using Actuator to display application health. Extend it by   10
adding a custom Health Indicator that checks a custom service or condition.
Q. 7(b) What is a Distributed transaction? Explain Two-phase commit (2pc) pattern. what are   10
the benefits disadvantages of using 2pc?
********** 2 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper 2f35f08f9ba4

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_Computer_7002/Microservices and Architecture/QP_Microservices and Architecture(702CO0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   A banking application has a single codebase where UI, business logic,
CO-1 ;
SO- ;   and database access are tightly coupled. Any minor change requires full [5]
BL-4   redeployment. Identify the limitations of monolithic architecture in this
scenario and explain how they impact scalability and maintenance.
CO-2 ;   b.
SO- ;   Explain the challenges of transaction management in microservices.   [5]
BL-2
c.
CO- 3;   Why is testing more complex in microservices compared to monolithic
SO- ;   [5]
systems? Explain the role of test automation, service virtualization, and
BL-2
contract testing in ensuring reliability of microservices.
CO-4 ;   d.
SO- ;   What is CI/CD? Explain its importance in Microservices.   [5]
BL-2
a.   Write steps to develop and run a “Hello World” application using Spring
Q2   [10]
Boot.
CO-3;
SO-;
[10]
BL-3   Explain the purpose of a Configuration Server in microservices architecture.
b.
How does it help in managing dependencies?
Q3   [10]
a.   Explain the architecture of Eureka for the service discovering and registering
CO1-3;
process?
SO2-;
BLU-2
********** 1 **********
--- page 2 ---
b.   Write a note on following?
(i) Zuul   [10]
(ii) Hystrix
a.   Discuss challenges in managing microservices lifecycle and their solutions.   [10]
Design and explain REST APIs for a student management system using
Q4   b.
operations:
CO-4;
SO-;   •   Create Student
BL-3   [10]
• Get Student
•   Delete student
Specify endpoints, HTTP methods, and sample request/response structures.
Q5   a.   Explain Docker architecture and components with a diagram.   [10]
CO-2;
SO-;
BL-2   b.   Why the distributed transactions should be avoided with the use of two-phase   [10]
commit protocol? How the identified issues can be solved?
[10]
Q6   a.   Explain Service Mesh architecture and its components.
CO-3;
SO-;   b.   A food delivery platform integrates restaurant, delivery, and payment services.
BL-2   Real-time updates are required. Identify suitable integration patterns and   [10]
justify their use.
Q7   a.   Explain the architecture of OAuth2.0 to authenticate the user.   [10]
CO-2;
SO-;   Write the key difference between service-to-service communication using
BL-3   b.   [10]
JWT and mutual TLS?
********** 2 **********
````

## 2025-26 · Re-Exam · Sem 6 · paper 5a1f0c98ceb5

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_Computer_7047/Microservices and Architecture/QP_Microservices and Architecture(702CO0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (2 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 2 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   A banking application has a single codebase where UI, business logic,
CO-1 ;
SO- ;   and database access are tightly coupled. Any minor change requires full [5]
BL-4   redeployment. Identify the limitations of monolithic architecture in this
scenario and explain how they impact scalability and maintenance.
CO-2 ;   b.
SO- ;   Explain the challenges of transaction management in microservices.   [5]
BL-2
c.
CO- 3;   Why is testing more complex in microservices compared to monolithic
SO- ;   [5]
systems? Explain the role of test automation, service virtualization, and
BL-2
contract testing in ensuring reliability of microservices.
CO-4 ;   d.
SO- ;   What is CI/CD? Explain its importance in Microservices.   [5]
BL-2
a.   Write steps to develop and run a “Hello World” application using Spring
Q2   [10]
Boot.
CO-3;
SO-;
[10]
BL-3   Explain the purpose of a Configuration Server in microservices architecture.
b.
How does it help in managing dependencies?
Q3   [10]
a.   Explain the architecture of Eureka for the service discovering and registering
CO1-3;
process?
SO2-;
BLU-2
********** 1 **********
--- page 2 ---
b.   Write a note on following?
(i) Zuul   [10]
(ii) Hystrix
a.   Discuss challenges in managing microservices lifecycle and their solutions.   [10]
Design and explain REST APIs for a student management system using
Q4   b.
operations:
CO-4;
SO-;   •   Create Student
BL-3   [10]
• Get Student
•   Delete student
Specify endpoints, HTTP methods, and sample request/response structures.
Q5   a.   Explain Docker architecture and components with a diagram.   [10]
CO-2;
SO-;
BL-2   b.   Why the distributed transactions should be avoided with the use of two-phase   [10]
commit protocol? How the identified issues can be solved?
[10]
Q6   a.   Explain Service Mesh architecture and its components.
CO-3;
SO-;   b.   A food delivery platform integrates restaurant, delivery, and payment services.
BL-2   Real-time updates are required. Identify suitable integration patterns and   [10]
justify their use.
Q7   a.   Explain the architecture of OAuth2.0 to authenticate the user.   [10]
CO-2;
SO-;   Write the key difference between service-to-service communication using
BL-3   b.   [10]
JWT and mutual TLS?
********** 2 **********
````

## 2025-26 · Re-Exam · Sem 4 · paper 9cd663402ff2

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, B.TECH INTEGRATED / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/2ND YEAR/COMPUTER/SEM IV/MICROPROCESSOR AND MICROCONTOLLER/Microservices and Architecture Batch 2025-26 Re Exam.pdf` (+3 identical copies)
- Printed on paper: max marks: 100; exam date: 03 Jul 2026
- Text: ocr (2 pages), mean OCR confidence 84.5

````text
Programme: B. Tech (COMP)/B. Tech Intg. (C

Subject: Microservices and Architecture

Date: 03 Jul 2026
Max. Marks: 100

Instructions:

SVKMs NMIMS°
MUKESH PATEL SCH.OF TECH.MGMT ENGG;

Year: IlJ/Sem 6 Re-exam(Exam Year;

am to 01:00

bay = EY
SMHS NNER
RE EXAMINATION (Acad. Year:2025-2026)—=—

1. This question paper contains 2 pages.

2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks

4. Question No._1___ is compulsory.

5. Out of remaining questions, attempt any 4 _ questions.
6. Assume Suitable data if necessary.

Ql ;
Answer briefly: [20]
Gti a. A banking application has a single codebase where UI, business logic,
SO-; , and database access are tightly coupled. Any minor change requires full | [5]
BL-4 redeployment. Identify the limitations of monolithic architecture in this
scenario and explain how they impact scalability and maintenance.
C02; |b.
SO-; Explain the challenges of transaction management in microservices. [5]
BL-2
G
CO- 3; Why is testing more complex in microservices compared to monolithic [5]
_ 5 systems? Explain the role of test automation, service virtualization, and
contract testing in ensuring reliability of microservices.
CO-4 ; d.
SO-; What is CI/CD? Explain its importance in Microservices. [5]
BL-2
Q2 a Write steps to develop and run a “Hello World” application using Spring [10]
Boot. ,
CO-3;
SO-;
BL-3 Explai ‘ oo. . . [10]
b xplain the purpose of a Configuration Server in microservices architecture.
How does it help in managing dependencies?
Q3 . . 4. . a. [10]
a. Explain the architecture of Eureka for the service discovering and registering
COL; | process?
SOQ2-; ,
BLU-2

FOI CIO AGI ik ak ak ok
--- page 2 ---
Write a note on following?

(i) Zuul [10]
(ii) Hystrix io
Discuss challenges in managing microservices lifecycle and their solutions. [10]
Q4 Design and explain REST APIs for a student management system using
CO-4: operations:
SO-; e =Create Student
10
BL-3 e Get Student [10]
e Delete student
Specify endpoints, HTTP methods, and sample request/response structures.
Q5 Explain Docker architecture and components with a diagram. [10]
CO-2; :
SO-; a ; . ; ;
BL-2 Why the distributed transactions should be avoided with the use of two-phase [10]
commit protocol? How the identified issues can be solved?
[10]
Q6 : Explain Service Mesh architecture and its components.
CO-3;
SO-; A food delivery platform integrates restaurant, delivery, and payment services.
BL-2 Real-time updates are required. Identify suitable integration patterns and [10]
justify their use.
Q7 Explain the architecture of OAuth2.0 to authenticate the user. [10]
CO-2;
aie Write the key difference between service-to-service communication using [10]

JWT and mutual TLS?

FRI OK Ok a
.

-~\
````

## 2024-25 · Final-Exam · Sem 3 · paper ce6881c7420b

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_03/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Microservices and Architecture/QP_Microservices and Architecture(703CO0C022)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 Nov 2024
- Text: text (3 pages)

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: II/Semester III(Exam Year: 2024-2025)
Subject: Microservices and Architecture
Date: 27 Nov 2024   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, answer any 4
4. In all, 5 questions to be attempted
5. Assume suitable data if necessary. Specify what you have assumed in the answer.
6. Figures on the right hand side indicate full marks
Q1   20
Explain in short, the following 2 design principles of Micro   5
1A   Services Architecture:
1. Resilience
2. Config Storage only in the environment
1B   Explain Saga Orchestration pattern of Transaction   5
Management
1C   Write a Spring Boot Controller Class with a POST endpoint   5
that takes in 2 integers as input, and returns their sum as
output
1D   In the context of Kubernetes, what is a Deployment YAML?   5
Explain in detail
Q2   20
2A   What is Actuator? Explain function of the /health endpoint.   10
Write code to demonstrate understanding of custom health
check implementation
2B   Explain what problems Kubernetes solves that Docker does   10
not solve. Draw a diagram that shows the relation between
Docker containers and Kubernetes pods
Q3   20
3A   Explain the following API Gateway concepts   10
********** 1 **********
--- page 2 ---
1. Header-based Routing
2. Method-based Routing
3. Aggregation
4. Rate Limiting
5. Transformation
3B   With respect to Micro Services security, explain the   10
following flavor of OAuth 2.0 implementation:
Login to a site using your credentials of an Identity Provider
such as Google
Q4   20
4A   Provide commands for the following:   10
1. Build docker image
2. Get status of Kubernetes Services
3. Check if the container is running
4. Stop the container
5. Get inside the running container
4B   Explain in detail how you will deploy a Spring Boot Service   10
to Kubernetes
Q5   20
5A   What is the difference between a Request DTO and a JPA   10
class? Write code to show a JPA class that has 1 integer
attribute and 1 String attribute. Write code to show the
corresponding possible Request DTO class
5B   Which Spring Cloud Service helps developers achieve the   10
Design Principle
“Config storage only in the environment”? Explain how you
will implement that Service
Q6   20
6A   Explain Kafka architecture   10
6B   Explain ACID properties in DBMS Transaction Management   10
Q7   20
7A   Answer the following:   10
1. What is the default port number on which Tomcat
runs?
********** 2 **********
--- page 3 ---
2. In a Spring Boot application, how can you change
this port number?
3. Provide any 3 Annotations found in a Controller
Class in Spring Boot and explain the usage of each
one
7B   State true or false:   10
1. One can pass data parameters in the URL when using
HTTP POST
2. Monolith applications can use 2 Phase Commit for
Transaction Management
3. Service YAML must contain the registry location of
the docker image of the service to be deployed
4. @RequestBody is a valid Spring Boot annotation
5. A Spring Boot service docker image requires Java
installed in it
********** 3 **********
````

## 2024-25 · Final-Exam · Sem 6 · paper 215fffa163d3

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/VI SEMESTER/MICROSERVICES AND ARCHITECTURE/Microservices and Architecture, Sem VI, Year 2024-25, Final Exam.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 6/5/2025
- Text: ocr (2 pages), mean OCR confidence 91.5

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2024-2025

Program: B.Tech/MBA Tech/B. tech(INTGS) Stream: COMP Year: [II/V Semester VI/X
Subject: Microservices and Architecture Time: 3 hrs (2:00pm to Btoopm)
Date: 6/5/2025 No. of Pages 2

Marks: 100

Final Examination(24- 25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No._1___ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) In all__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Qi Answer briefly: r 20
a) | Write a note on CI/CD pipeline 5
b) | A note on 5
« IOC
e REST
c) | Compare between Microservices and SOA Architecture? 5
d) | Compare Virtual Machine and Docker 5
Q. 2(a) | How can you implement basic CRUD operations using Spring Boot, JPA, and 1

MySQL with a structured:service layer? In your answer, include:

1. Creating an Entity class

2. Defining a JPA Repository for database operations

3. Implementing a Service Layer for business logic

4. Creating a REST Controller with CRUD methods (Create, Retrieve, Update,
Delete, and List All)

s Configuring MySQL in application.properties

Q. 2(b) | How can you implement In-Memory Basic Authentication in Spring Boot?In your 10
answer, include:

L. Sane a Security Configuration Class for In-Memory Authentication
--- page 2 ---
2. Creating a Controller to Test Authentication
3. Defining User Roles and Authorities in the Security Configuration
4. Adding Required Dependencies in pom.xml (if using Spring Security Starter)

Q. 3(a) | Explain API Gateway Architecture? 10

If two Microservices (ms! and ms2) communicate using Eureka Server and also use
API Gateway. Write down the steps and configuration needed?

e Registering Microservices with Eureka: How do you configure ms! and ms2
as Eureka clients in application.properties

« Configuring API Gateway for Routing: How do you define routes in
application.properties for ms] and ms2?

Q. 3(b) | Write down the step to implement a Spring Cloud Config Server and Client with a 10
Refresh Feature?

Q. 4(a)__| Explain Kubernetes Architecture? Write the configuration and commands for 10
Dockerizing a Spring Boot Application on

1. How do you create a Dockerfile for a Spring Boot application?

2. What command is used to build a Docker image and verify its creation?
3. How do you run the Spring Boot container and expose it on port 8080?
4, What are the steps to push and pull a Docker image to Docker Hub?

Q. 4(b) | Design pattern in Spring Microservices with diagram. 10

Q. 5(a)__| Explain the Docker Architecture? Explain docker-compose. Create a docker- 10
compose.yml file to run a Spring Boot application with a MySQL database

Q. 5(b) What are the two ways of Microservice communication? 10

Provide the complete code to implement the communication using Open Feign and
RestClient

Q. 6(a) | What is Kafka? Explain its architecture with the steps to run producer and consumer? | 10

Q. 6(b) | Mike Cohn's original test pyramid? Explain with diagram? Types of Testing in Spring | 10
boot Microservices

Q. 7(a)__| What is a distributed transaction? ExplainTwo-phase commit (2pc) pattern .what are | 10
the benefits disadvantages of using 2pc?

Q.7(b) | What is Actuator? Write down all the steps and code for Creating a Custom Health 10
Indicator
````

## 2024-25 · Final-Exam · Sem 10 · paper 74efdbd73c51

- Departments: Computer Engineering
- Programmes: B.TECH INTEGRATED / COMPUTER
- Source: `02_Question_Papers/Legacy/B.TECH INTEGRATED/5th YEAR/COMPUTER/SEM X/Microservices and Architecture/Microservices and Architecture Batch 2024-25 Final.pdf`
- Printed on paper: duration hours: 3; exam date: 6/5/2025
- Text: ocr (2 pages), mean OCR confidence 89.8

````text
2( MPSTME A\
oN LIBRARY /¢|

>.
FNEERING <=

.
NS UN

SVKM’S NMIMS

MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENTS& E
Academic Year: 2024-2025

%

Year: IlI/V Semester VIX
Time: 3 hrs (2:00pm to Sz00pm)
No. of Pages 2

Program: B.Tech/MBA Tech/B. tech(INTGS) Stream: COMP
Subject: Microservices and Architecture
Date: 6/5/2025

Marks; 100
Final Examination(24- 25)

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 questions.
3) Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate fuJl marks..

7) Assume Suitable data if necessary.

Ql Answer briefly: 20

a) | Write a note on CI/CD pipeline

b) | A note on

e 10C

e REST
c) | Compare between Microservices and SOA Architecture?
d) | Compare Virtual Machine and Docker

y
Q.2(a) | How can you implement basic CRUD operations using Spring Boot, JPA, and 10
MySQL with a structured service layer? In your answer, include:

1. Creating an Entity class

2. Defining a JPA Repository for database operations

3. Implementing a Service Layer for business logic

4. Creating a REST Controller with CRUD methods (Create, Retrieve, Update,
Delete, and List All)

§- Configuring MySQL in application.properties

Q.2(b) | How can you implement In-Memory Basic Authentication in Spring Boot?In your 10

answer, include:

1. Writing a Security Configuration Class for In-Memory Authentication
--- page 2 ---
2. Creating a Controller to Test Authentication a
3. Defining User Roles and Authorities in the Security Configuration :
4. Adding Required Dependencies in pom.xml (if using Spring Security Starter)

Q. 3(a)

Explain API Gateway Architecture?

If two Microservices (ms1 and ms2) communicate using Eureka Server and also use
API Gateway. Write down the steps and configuration needed?

e Registering Microservices with Eureka: How do you configure ms! and ms2
as Eureka clients in application.properties

¢ Configuring API Gateway for Routing: How do you define routes in
application.properties for ms! and ms2?

10

Q 3(6)

Write down the step to implement a Spring Cloud Config Server and Client with a
Refresh Feature?

10

Q. 4(a)

Explain Kubernetes Architecture? Write the configuration and commands for
Dockerizing.a Spring Boot Application on

1. How do you create a Dockerfile for a Spring Boot application?

2. What command is used to build a Docker image and verify its creation?
3. How do you run the Spring Boot container and expose it on port 8080?
4. What are the steps to push and pull a Docker image to Docker Hub?

10

Q. 4(b)

Design pattern in Spring Microservices with diagram.

10

Q. 5(a)

Explain the Docker Architecture? Explain docker-compose. Create a docker-
compose.yml file to run a Spring Boot application with a MySQL database

10

Q. 5(b)

What are the two ways of Microservice communication?

Provide the complete code to implement the communication using Open Feign and
RestClient

10

Q. 6(a)

What is Kafka? Explain its architecture with the steps to run producer and consumer?

10

Q. 6(b)

Mike Cohn's original test pyramid? Explain with diagram? Types of Testing in Spring
boot Microservices

10

Q. 7a)

What is a distributed transaction? ExplainTwo-phase commit (2pc) pattern .what are
the benefits disadvantages of using 2pc?

10

Q. 7(b)

What is Actuator? Write down all the steps and code for Creating a Custom Health
Indicator

10
````

## 2024-25 · Final-Exam · Sem 3 · paper ed09e2a7e0c2

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/2ND YEAR/III SEMESTER/Microservice and Architecture/Microservices and Architecture Batch 2024-25 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 Nov 2024
- Text: ocr (3 pages), mean OCR confidence 89.5

````text
Year: I1/Semester II[(Exam Year: 2024-2025) SE Na S
F , ; * MS UNIVERSE
Subject: Microservices and Architecture SS
Date: 27 Nov 2024 Time: 10:00 am to 01:00 pm, (03:00 Hrs.)
Max. Marks: 100 ‘ne

SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: MASTER OF COMPUTER APPLICATIONS

FINAL EXAMINATION (Acad. Year:2024-2025)

Instructions:

This question paper contains 3 pages.

MPSTME
LIBRARY

2. Question No. | is compulsory
3. Out of the remaining questions, answer any 4
4. In all, 5 questions to be attempted
5. Assume suitable data if necessary. Specify what you have assumed in the answer.
6. Figures on the right hand side indicate full marks
[a1 | | 20 _]
Explain in short, the following 2 design principles of Micro 3
1A Services Architecture: “ey
1. Resilience “
2. Config Storage only in the environment
1B Explain Saga Orchestration pattern of Transaction 5
Management
1c Write a Spring Boot Controller Class with a POST endpoint 5
that takes in 2 integers as input, and returns their sum as :
output .
1D In the context of Kubernetes, what is a Deployment YAML? | 5
Explain in detail
[a2] | [ 20
2A What is Actuator? Explain function of the /health endpoint. | 10
Write code to demonstrate understanding of custom health
check implementation
2B Explain what problems Kubernetes solves that Docker does | 10

not solve. Draw a diagram that shows the relation between
Docker containers and Kubernetes pods

[aT ED =

[

3A ‘| Explain the following API Gateway concepts 10

HRAARAAARK RRR ERK EEK
--- page 2 ---
1. Header-based Routing
2. Method-based Routing .
3. Aggregation

4. Rate Limiting

5. Transformation

3B

With respect to Micro Services security, explain the 10
following flavor of OAuth 2.0 implementation:

Login to a site using your creden tials of an Identity Provider
such as Google

[a4 |

4A

Provide commands for the following: 10
1. Build docker image
2. Get status of Kubernetes Services
3. Check if the container is running
4. Stop the container _
5. Getinside the running container ~

4B

Explain in detail how you will déploy a Spring Boot Service 10
to Kubernetes

[as _|

| 20

SA

What is the difference between a Request DTO and a JPA ‘10
class? Write code to show a JPA class that has 1 integer
attribute and 1 String attribute. Write code to show the
corresponding possible Request DTO class

5B

Which Spring Cloud Service helps developers achieve the 10
Design Principle

“Config storage only in the environment”? Explain how you

will implement that Service

[as_|

| | 20
[ 6A Explain Kafka architecture 10
| 6B Explain ACID properties in DBMS Transaction Management 10
[7 [20
7A Answer the following: “] 10
1. What is the default port number on which Tomcat
runs?

FRR DR ROK
--- page 3 ---
2. Ina Spring Boot application, how can you change
this port number?

3. Provide any 3 Annotations found in a Controller
Class in Spring Boot and explain the usage of each

one
7B State true or false: 10
1. One can pass data parameters in the URL when using
HTTP POST

2. Monolith applications can use 2 Phase Commit for
Transaction Management

3. Service YAML must contain the registry location of
the docker image of the service to be deployed

4. @RequestBody is a valid Spring Boot annotation

5. A Spring Boot service docker image requires Java
installed in it

ail

o

oy

FOR RR RRR ARR
````

## 2024-25 · Re-Exam · Sem 3 · paper e1283a914628

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/2ND YEAR/III SEMESTER/Microservice and Architecture/Microservices and Architecture Batch 2024-25 Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (4 pages), mean OCR confidence 91.3

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M

Programme: MASTER OF COMPUTER TUL Des
Year: II/Semester III

Subject: Microservices and Architecture
Date: /3 /o2.]2025 Time: (03:00 Hrs.)

Max. Marks: 100 (loam te \pm)

Re-EXAMINATION (Acad. Year: 2024-2025)

Instructions:
1. This question paper contains 3 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, answer any 4
4. In all, 5 questions to be attempted
5. Assume suitable data if necessary. Specify what you have assumed in the answer.
6. Figures on the right hand side indicate full marks

Qi 20
Explain in short, the following 2 design principles of Micro Services Architecture: 5
1A 1. High Cohesion/Loose Coupling
2. Writing to STDOUT
1B | Explain differences between Saga Choreography and Saga Orchestration 5
1C | Write a Spring Boot Controller Class with a GET endpoint that takes in 2 integers as 5
input, multiplies them and returns the output
1D _| Explain the difference between Virtual Machines and Docker Container 5
Q2
2A | What is Service Discovery? Why is it needed? Explain how Eureka works in detail. 10
The important code snippets involved in Eureka Client and Server are expected.
2B | Explain what is a Docker Image and Docker Containers. What are the advantages of 10
using Docker?
Q3
3A | Explain the following Kubernetes concepts: 10
1. Pod
2. ReplicaSet
3. Service

4. Deployments
5. StatefulSet

FIR FR RE
--- page 2 ---
3B | Explain the following concepts in API Security 10
1. Authentication
2. Identity Provider
3. How passwords are stored
4. What is “Salt” in passwords
5. What is “Pepper” in passwords
a4
4A | Provide commands for the following: 10
1. Apply deployment yaml
2. Get status of pods after applying deployment yaml
3. Runa docker container with port mapping
4. Tag adocker image
5. Apply service yaml after changing the service name inside the yaml
4B | Explain in detail the significance of following packages in Domain Driven Design: 10
1. Endpoints
2. DTOs
3. Services
4. Repository
Q5
5A | Explain Dependency Injection with the help of a code example that uses a constructor | 10
and a relevant annotation. Also explain what is gradle and the basic gradle
dependency required for writing REST APIs in Spring Boot
5B | What is meant by a Docker Registry? Give 1 example of a docker registry. Give 1 10
major difference between Docker and Docker-Compose.
Q6
6A | Explain the following API Gateway concepts 10
1. Authorization
2. Logging
3. Load Balancing
4. Path-based Routing
5. Parameter-based Routing
6B | Write Code to implement a Custom Shutdown Listener. 10

If you configure the timeout in application.properties as 20 seconds but your custom
shutdown listener takes 30 seconds to complete, will the shutdown occur after 20
seconds or after 30 seconds? In either case, explain why

If you configure the timeout in application.properties as 30 seconds but your custom
shutdown listener takes 20 seconds to complete, will the shutdown occur after 20
seconds or after 30 seconds? In either case, explain why

FOO IIICICC (2 lok «
--- page 3 ---
Q7
7A 1. What Spring Class will you use in 1 Service to call another Service? 10
2. Inside what folder is application.properties file?
VY 4 src
Vo‘ main
> java
> “ resources
3. Ina deployment yaml file, what does “replicas: 1” property imply?
4. Inthe labs, what was the website which you used to download a basic skeletal
spring project, with gradle dependencies?
5. Name 2 HTTP methods other than GET and POST
7B | State true or false: 10

1. Microservices Architecture states that you should have 1 DB (Data Model) per
service

2. Kubernetes helps automate creation of multiple instances of a service

3. @ControllerRest is a valid Spring Boot annotation

4. The following is valid code in a Controller
@GetMapping("/hello")
public String sayHello() {
return "Hello, World!";

}

5. HTTP 100 is a valid HTTP response code

FOC 2 ko a #
--- page 4 ---

````

## 2023-24 · Final-Exam · Sem 6 · paper 35ae843581a7

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/VI SEMESTER/MICROSERVICES AND ARCHITECTURE/Microservices and Architecture, Sem-VI, Final 2023-24.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3
- Text: ocr (2 pages), mean OCR confidence 90.8

````text
SVKM’S NMIMS '
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMEN .:
Academic Year: 2023-2024

Program: Bech /MBA Tech Stream: Computer Engg- Year: III Semester:VI

Subject: Microservices and Architecture Time: 3 hrs (2-00 pm to 5.00pm)
Date: 24 Jo4] 2024 No. of Pages: 2

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is-compulsory.

2) Out of remaining questions, attempt any 4 _ questions.
3)Inall___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Ql Answer briefly: ao
a) | Explain DTO in Spring Boot Framework? >
b) | A note on Kafka Architecture?
c)| Compare Micoservice and SOA Architecture. State the disadvantages of | °
microservices
d) | Write note on Synchronous and Asynchronous communication in Microservices 5
Q. 2(a) What is Design Pattern? Explain with diagram. -

1. Circuit Breaker Design Pattern
2. Command Query Responsibility Segregator (CQRS)

Q. 2(b) Explain Monolithic Application. What are the advantages and Limitations of 10
Monolithic Application?

Q. 3(a) What is Spring Data JPA. write a 10
e Entity name Employee with id and name as property
e Controller which performs any four crud operation using

Response Entity

L e Dependency needed in pom.xml
--- page 2 ---
¥

Q. 3(b)

What are the different ways in which microservice1 can call micorservice 2.Write a
program of where microservicel calling microservice2 using restTemplate

10

Explain API Gateway. Explain its architecture with program sample code?

Q. 4(a) 7

Q. 4(b) How does Domain-Driven Design (DDD) guide the design of microservices? 10

Q. S(a) What is Discovery Server. How to Implement Microservice Registry using Eureka i
Client and Server. Write the steps and configuration needed?

Q. 5(b) What is Saga pattern? State the advantages and disadvantages of the Saga pattern 10

Q. 6(a) Describe Kafa? Write down all the steps for running kafa producer and consumer | !°
program? ;

Q. 6(b) Explain the Working of Docker? Write frequently used Docker commands. 10
Compare Docker and Kubernetes

Q. 7(a) Write short note on: OAuth 2.0 and JSON Web Token? 10

Q. 7(b) Describe the key components of a Kubernetes cluster, such as Master Node, Worker | !°

Node, and etcd.
````

## 2023-24 · Final-Exam · Sem 5 · paper 43f3e29ee98a

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSBS/SEM-V/MICROSERVICES AND ARCHITECTURE/Microservices and Architecture, Sem-V, Final Exam, A Y 2023-24.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 2/12/23
- Text: ocr (2 pages), mean OCR confidence 91.4

````text
SVKM’S NMIMS Rh
, Ss
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING=
Academic Year: 2023-2024

a”

¥

Program: B.Tech Stream: CSBS omen Year: II Semester: V
Subject: Microservices and Architecture ~ Time: 3 hrs (2 pm to 5 pm)
Date: 2/12/23 ; No. of Pages 2

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. 1 is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.
3)Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 Answer briefly: 20
a) | Write anote on Spring Boot Actuator 5
b) | A note on Synchronous and Asynchronous communication in 5
Microservices
c) | What are Microservices ? What are the main differences between 5

Microservices and SOA Architecture?

d) | Difference between Spring and Spring Boot? 5

Q. 2(a) | Using Product as a class with attribute id and name .write a code 10
demonstrating CRUD operation in Microservices.

Q. 2(b) | What is kafka? explain its architecture, along with steps for running a 10
producer and consumer .
--- page 2 ---
10

Q. 3(a) | Explain API Gateway Architecture? What are the advantages and
drawbacks?---. »
Q. 3(b) | How to Implement Microservice Registry using Eureka Client and , 10
Server. Write the steps and configuration needed?
Q. 4(a) 10
In Springdata JPA write a
e Entity name Employee with id and name as property
e Controller which performs crud operation
Q. 4(b) | Why use Docker? Explain the Docker Architecture? Write 5 Docker 10
commands.
Q. 5(a) | Design pattern in Spring Microservices with diagram. 10
Q. 5(b) | Explain the fundamental Microservices design principles 10
Q. 6(a) | What is a distributed transaction? Two-phase commit (2pc) pattern 10
what are the benefits disadvantages of using 2pc?
Q. 6(b) | Mike Cohn's original test pyramid? Explain with diagram? Types of 10
Testing in Spring Spring Microservices ’
Q. 7(a) | Explain Microservices Deployment Patterns with Diagram 10
Q. 7(b) | Explain InMemory Basic Authentication with the program in SpringBoot | 10
````

## 2023-24 · Final-Exam · Sem 3 · paper ce8bdb06e8b5

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/2ND YEAR/III SEMESTER/Microservice and Architecture/Microservice and Architecture Batch 2023-24 Final.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01/12/23
- Text: ocr (2 pages), mean OCR confidence 92.5

````text
MPSTME

LIBRARY

SVKM’S NMIMS

Academic Year: 2023-2024

Program: MCA : | ; Year: IJ Semester III
Subject: Microservices and Architecture Time: 3 hrs (10 am to 1 pm)
Date: 01/12/23 No. of Pages 2

Marks: 100

Final Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1___ is compulsory.

2) Out of remaining questions, attempt any __4 _ questions.

3) Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 Answer briefly: ; 20
a) | Write anote on Spring Boot Actuator 5
b) | A note on Synchronous and Asynchronous communication in 5
Microservices ;
c) | What are Microservices ? What are the main differences between 5

Microservices and SOA Architecture?

d) | Difference between Spring and Spring Boot? 2)

Q. 2(a) | Write a code demonstrating CRUD operation in Microservices. 10

Q. 2(b) | Explain in Memory Basic Authentication with the program in spring boot | 10

Q. 3(a) | Explain API Gateway Architecture? What are the advantages and 10
drawbacks?
--- page 2 ---
Q. 3(b)

How to Implement Microservice Registry using Eureka Client and

vw | 10
Server. Write the steps and configuration needed? ial

Q. 4(a)

10

In Springdata JPA write a
e Entity name Employee with id and name as property
e Controller which performs crud operation

Q. 4(b) | Design pattern in Spring Microservices with diagram. 10

Q. 5(a) | Why use Docker? Explain the Docker Architecture? Write 5 Docker 10
commands.

Q. 5(b) | Explain the fundamental Microservices design principles 10

Q. 6(a) | What is a distributed transaction? Two-phase commit (2pc) pattern 10
what are the benefits disadvantages of using 2pc?

Q. 6(b) | Mike Cohn's original test pyramid? Explain with diagram? Types of 10

Testing in Spring Spring Microservices

Q. 7(a)

Explain Microservices Deployment Patterns with Diagram 10

Q. 7(b)

What is kafka? Explain its architecture with the steps to run producer and | 10
consumer?
````

## 2023-24 · Re-Exam · Sem 6 · paper 056a0dd115fb

- Departments: Computer Engineering
- Programmes: B TECH / COMPUTER, MBA TECH / Computer
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/COMPUTER/VI SEMESTER/MICROSERVICES AND ARCHITECTURE/Microservices and Architecture Re-exam 2023-2024.pdf` (+1 identical copies)
- Printed on paper: max marks: 100; duration hours: 3; exam date: 4/7/24
- Text: ocr (2 pages), mean OCR confidence 90.0

````text
SVKM’S NMIMS .
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINE
Academic Year: 2023-2024

¥

Program: BTech /MBA Tech Stream: Computer Engg Year: III Semester VI
Subject: Microservices and Architecture Time: 3 hrs (2:00pm to $2 00pm)
Date: 4/7/24 No. of Pages 2
Marks: 100 :
Re Examination

Instructions: Candidates shouid read carefuiiy the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1____ is compulsory.

2) Out of remaining questions, attempt any __4 questions.

3) In all___5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 Answer briefly: 20
a) | Write a note on Spring Boot Actuator 5
b) | Compare DTO and JPA Entity 5

c) | What are Microservices ? What are the main differences between Microservices and | 5
SOA Architecture?

d) | Difference between Spring and Spring Boot? 5

Q. 2(a) 10

Explain the essential step to Migrate Monolithic Applications into Microservices

Q. 2(b) | Explain in Memory Basic Authentication with the program in spring boot 10

Q. 3(a) | Explain API Gateway Architecture? What are the advantages and drawbacks? 10

Q. 3(b) | How to Implement Microservice Registry using Eureka Client and Server. Write the 10
steps and configuration needed?
--- page 2 ---
Q. 4(a) 10
In Springdata JPA write a
¢ Entity name Product with id and name as property
¢ Controller which performs any four crud operation using
Response Entity
Q. 4(b) | Explain Design pattern in Spring Microservices with diagram. 10
1. Event Sourcing Design Pattern
2. Database or Shared Database Design Pattern
Q. 5(a) Why use Docker? Write 5 Docker commands.how does it differ from traditional 10
virtualization?
Q. 5(b) | Explain the architecture of Kubernetes in Detail with diagram 10
Q. 6(a) What is a distributed transaction? Two-phase commit (2pc) pattern what are the 10
benefits disadvantages of using 2pc?
Q. 6(b) | Mike Cohn's original test pyramid? Explain with diagram? Types of Testing in Spring | '°
Spring Microservices
Q.7(a) | How does Domain-Driven Design (DDD) influence the design of microservices? 10

Q 7(b)

What is kafka? Explain its architecture with the steps to run producer and consumer?

10
````

## 2023-24 · Re-Exam · Sem 5 · paper f95486f3a500

- Departments: Computer Science and Business Systems
- Programmes: B TECH / CSBS
- Source: `02_Question_Papers/Legacy/B TECH/3RD YEAR/CSBS/SEM-V/MICROSERVICES AND ARCHITECTURE/Microservices & Architecture, Sem-V, Year 2023-24, Re Exam.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 4/02/24
- Text: ocr (2 pages), mean OCR confidence 89.3

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2023-2024

¥

Program: B.Tech Stream: CSBS Year: III Semester: V
Subject: Microservices and Architecture Time: 3 hrs (2 pm to 5 pm)
Date: 4/02/24 No. of Pages 2
Marks: 100 .

Re Examination

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1_-_ is compulsory. :

2) Out of remaining questions, attempt any __4 _ questions.
3)Inall__5_ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 Answer briefly: 20
a) | A note on Kafka Architecture? 5
b) | Explain Spring Boot Framework? 5
c) | Describe different ways Microservices can communicate? 5
d)| A note on Communication models for Microservices ‘ 5

=

Q.2(a) | What is a Monolithic Application? What are its strengths and | 10
weaknesses?

Q.2(b) | What are Design Patterns, and can you explain two of them in Spring | 10
Microservices with diagrams?

Q. 3(a) | Explain Spring Data JPA. Create an "Employee" entity with id and | 10
wea name properties
a) Controller for CRUD operations, and mention the required

dependencies in the pom.xml.
b) Provide a program for a Controller, Service, and Spring Repository

for CRUD operations.
--- page 2 ---
+

What is an API Gateway, and how does it work? Can you provide a

10

Q. 3(b)
sample program to illustrate its architecture?

Q. 4(a) | Write a program for Controller, Service and Spring Repository for crud | 10
operation ;

Q. 4(b)__| Explain the 10 fundamental Microservices design principles 10

Q.5(a) | How can I set up a Microservice Registry using Eureka Client and | 10
Server? What steps and configurations are needed?

Q. 5(b) | What is the Saga pattern? Can you highlight its advantages and | 10
disadvantages?

Q. 6(a) | Write down all the steps for running kafa producer and consumer | 10
program?

Q. 6(b) | Explain Docker and its functionality. Mention some commonly used | 10
Docker commands.

Q. 7(a) | Write short note on: OAuth 2.0 and JSON Web Token? 10

Q. 7(b) . | Discuss testing in Spring Boot Microservices and identify the types of | 10

testing used in Spring Microservices. ‘
````

## 2023-24 · Re-Exam · Sem 3 · paper 3882649de34f

- Departments: Computer Applications (MCA)
- Programmes: MCA
- Source: `02_Question_Papers/Legacy/MCA/2ND YEAR/III SEMESTER/Microservice and Architecture/Microservices and Architecture Batch 2023-24 Re Exam0001.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09/02/2024
- Text: ocr (2 pages), mean OCR confidence 89.4

````text
SVKM’S NMIMS
MUKESH PATEL SCHOOL OF TECHNOLOGY MANAGEMENT& ENGINEERING
Academic Year: 2023-2024 ;

rv

Program: MCA Year: Il Semester’ Ill
Subject: Microservices and Architecture Time: 3 hrs (2: pm to5-pm)
‘Date: 09/02/2024 No. of Pages 2 }
Marks: 100 eA
Re-Examination . ——

Instructions: Candidates should read carefully the instructions printed on the question paper and on
the cover of the Answer Book, which is provided for their use.

1) Question No. _1__ is compulsory.

2) Out of remaining questions, attempt any 4 _ questions.

3) Inall___5__ questions to be attempted.

4) All questions carry equal marks.

5) Answer to each new question to be started on a fresh page.

6) Figures in brackets on the right hand side indicate full marks.
7) Assume Suitable data if necessary.

Q.1 Answer briefly: 20
a) | Explain Spring Boot Framework? 5
b) | A note on Kafka Architecture? 5
c)| Define Microservices and highlight the key distinctions from SOA | 5
Architecture.
d) | A note on Communication models for Microservices ‘ 5
Q. 2(a) | What is Design Pattern? Explain any two design pattern in Spring 10

Microservices with diagram.

Q. 2(b) | Explain Monolithic Application. What are the advantages and 10
Limitations of Monolithic Application?

Q. 3(a) | What is Spring DataJPA. write a 10
e Entity name Employee with id and name as property
e Controller which performs crud operation
e Dependency needed in Pom.xml
--- page 2 ---
Q. 3(b) | What are the different ways in which microservicel can call ; 10
micorservice 2. Write a program of where microservicel calling
microservice2 using restTemplate

Q. 4(a) | Explain API Gateway. Explain its architecture with program sample 10
code?

Q. 4(b) | Explain the 10 fundamental Microservices design principles 10
Q. S5(a)_ | What is Discovery Server. How to Implement Microservice Registry 10
using Eureka Client and Server. Write the steps and configuration

needed?
Q. 5(b) | What is Saga pattern? State the advantages and disadvantages of the 10
Saga pattern

'Q. 6(a) | Write down all the steps for running kafa producer and consumer | 10

program?

Q. 6(b) | What is Docker? Explain the Working of Docker? Write frequently used | 10

Docker commands.
a

Q. 7(a) | Write short note on: OAuth 2.0 and JSON Web Token? - - 10

Q. 7(b) | Explain is testing in spring boot Microsevices. What are the types of 10
Testing in Spring Microservices?
````
