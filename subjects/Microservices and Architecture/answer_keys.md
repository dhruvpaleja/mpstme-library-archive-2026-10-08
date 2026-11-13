# Microservices and Architecture: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 3 · Answer key · paper 930aa72e5747

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_03/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Microservices and Architecture/ANS_Microservices and Architecture(703CO0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 24 Nov 2025
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: II/Semester III(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 24 Nov 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted.
5. All questions carry equal marks
6. Figures in brackets on the right hand side indicate full marks
7. Answer to each new question to be started on a fresh page.
Q.1   Answer briefly:   20
a) Explain API Gateway architecture   5
• An API Gateway is a server that acts as a single entry point for all client
requests to microservices.
• Architecture Components:
1. Client Request → hits API Gateway.
2. Routing → Gateway routes request to appropriate microservice.
3. Security → Authentication, Authorization, Rate Limiting.
4. Response Aggregation → Combines responses from multiple
services if needed.
5. Monitoring & Logging → Tracks requests and metrics.
•   Benefits: Centralized security, reduced client complexity, caching,
request aggregation, throttling.
b) Write an explanatory note on the Architecture of Apache Kafka.   5
Kafka is a distributed streaming platform for building real-time data
pipelines.
Components:
1. Producer → Sends messages to Kafka topics.
2. Broker → Kafka server storing messages. Multiple brokers form a
cluster.
3. Consumer → Reads messages from Kafka topics.
4. Topic → Logical channel for messages; can be partitioned for
parallelism.
5. Partition → Subdivision of topic for scalability.
6. Zookeeper → Manages cluster metadata and leader election (Kafka 2.x,
newer versions may not require Zookeeper).
********** 1 **********
--- page 2 ---
7. Working: Producers send messages → Broker stores in partitions →
Consumers subscribe to topics.
c) Explain IOC in brief   5
OC (Inversion of Control) is a principle where the control of object creation
and dependency management is given to a framework/container instead of
manual instantiation.
Benefits: Loose coupling, better testability, modular design.
Example: Spring IoC Container injects dependencies via Constructor
Injection or Setter Injection.
d) Compare Virtual Machine and Docker   5
Feature   Virtual Machine (VM)   Docker Container
Shared OS kernel, isolated
Architecture   Full OS + hypervisor
processes
Resource
Heavy   Lightweight
Usage
Startup Time Minutes   Seconds
Portability   Less portable   Highly portable
Isolation   Stronger (full OS)   Process-level isolation
Running multiple OS on same   Microservices deployment,
Use Case
hardware   CI/CD
Q. 2(a)   Explain Monolithic Application. What are the advantages and Limitations of   10
Monolithic Application?
Definition:
A monolithic application is a single-tiered software application where
all modules (UI, business logic, and database access) are packaged
together.
Advantages:
1. Simple to develop and test initially.
2. Easy deployment (single artifact).
3. Low latency for internal function calls.
Limitations:
1. Difficult to scale; entire app scales as one.
2. Hard to maintain and understand as codebase grows.
3. Technology stack lock-in.
4. Any change requires redeployment of the entire applicatio
********** 2 **********
--- page 3 ---
Q. 2(b)   You are building a Spring Boot application for an online store to manage   10
Product inventory using MySQL with a layered architecture.
Answer the following:
1. Create a Product entity class with suitable annotations and fields (id,
name, price).
2. Define a JPA Repository interface for database operations.
3. Implement a Service Layer to handle business logic for CRUD
operations.
4. Develop a REST Controller exposing endpoints to Create, Retrieve,
Update, Delete, and List all products.
5. Configure MySQL connection settings in application.properties.
1. Product Entity Class
import jakarta.persistence.*;
@Entity
public class Product {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
private String name;
private double price;
// getters and setters
}
2. JPA Repository
import org.springframework.data.jpa.repository.JpaRepository;
public interface ProductRepository extends JpaRepository<Product, Long> {}
3. Service Layer
import org.springframework.stereotype.Service;
import java.util.List;
@Service
public class ProductService {
private final ProductRepository repo;
public ProductService(ProductRepository repo) { this.repo = repo; }
public Product save(Product product) { return repo.save(product); }
public List<Product> getAll() { return repo.findAll(); }
public Product getById(Long id) { return repo.findById(id).orElse(null); }
public void delete(Long id) { repo.deleteById(id); }
}
4. REST Controller
import org.springframework.web.bind.annotation.*;
import java.util.List;
@RestController
@RequestMapping("/products")
public class ProductController {
private final ProductService service;
public ProductController(ProductService service) { this.service = service; }
@PostMapping public Product create(@RequestBody Product p) { return
service.save(p); }
@GetMapping public List<Product> getAll() { return service.getAll(); }
@GetMapping("/{id}") public Product getById(@PathVariable Long id) { return
service.getById(id); }
********** 3 **********
--- page 4 ---
@PutMapping("/{id}") public Product update(@PathVariable Long id,
@RequestBody Product p) {
p.setId(id); return service.save(p);
}
@DeleteMapping("/{id}") public void delete(@PathVariable Long id)
{ service.delete(id); }
}
5. MySQL Connection in application.properties
spring.datasource.url=jdbc:mysql://localhost:3306/shopdb
spring.datasource.username=root
spring.datasource.password=root
spring.jpa.hibernate.ddl-auto=update
Q. 3(a)   Explain the purpose of Spring Boot Actuator. How can you implement a custom   10
Health Indicator in a Spring Boot application? Write the necessary steps and
code.
Purpose:
• Provides production-ready endpoints to monitor and manage Spring Boot
applications (health, metrics, environment, etc.).
Custom Health Indicator Steps:
1. Add dependency in pom.xml:
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
2. Create a custom health indicator:
import org.springframework.boot.actuate.health.Health;
import org.springframework.boot.actuate.health.HealthIndicator;
import org.springframework.stereotype.Component;
@Component
public class CustomHealthIndicator implements HealthIndicator {
@Override
public Health health() {
boolean serviceUp = checkService(); // custom logic
if(serviceUp) {
return Health.up().withDetail("Service Status", "Running").build();
}
return Health.down().withDetail("Service Status", "Down").build();
}
private boolean checkService() {
// perform check logic
return true;
}
}
3. Access endpoint: http://localhost:8080/actuator/health
********** 4 **********
--- page 5 ---
Q. 3(b)   Write a Spring Boot application demonstrating inter-service communication.   10
Implement two approaches: one using OpenFeign and another using WebClient
1. Using OpenFeign
@FeignClient(name="product-service", url="http://localhost:8081")
public interface ProductClient {
@GetMapping("/products")
List<Product> getProducts();
}
2. Using WebClient
import org.springframework.web.reactive.function.client.WebClient;
WebClient webClient = WebClient.create("http://localhost:8081");
List<Product> products = webClient.get().uri("/products")
.retrieve()
.bodyToMono(new ParameterizedTypeReference<List<Product>>() {})
.block();
Q. 4(a)   Explain Design Pattern and write a note on   10
• CQRS (Command Query Responsibility Segregation)
• Event Sourcing Design Pattern
Design Pattern: Reusable solution to recurring problems in software design.
CQRS (Command Query Responsibility Segregation):
•   Separates read and write operations into different models to optimize
performance, scalability, and security.
Event Sourcing:
•   Stores state changes as a sequence of events instead of only storing the
current state.
• Helps in audit trails, replaying events, and eventual consistency.
Q. 4(b)   How can you implement a Spring Cloud Config Server and Client with a Refresh 10
Feature?In your answer, include:
1. Configuring application.properties for the Config Client
2. Configuring application.properties for the Config Server
3. Creating a REST Controller to fetch configuration values
Adding required dependencies in pom.xml for both Config Server and
ClientConfig Server application.properties
server.port=8888
spring.cloud.config.server.git.uri=https://github.com/user/config-repo
spring.cloud.config.server.git.clone-on-start=true
Config Client application.properties
spring.application.name=config-client
spring.cloud.config.uri=http://localhost:8888
management.endpoints.web.exposure.include=*
********** 5 **********
--- page 6 ---
REST Controller
@RestController
public class ConfigController {
@Value("${some.config}")
private String configValue;
@GetMapping("/config")
public String getConfig() { return configValue; }
}
Dependencies (pom.xml)
• Server: spring-cloud-config-server
•   Client: spring-cloud-starter-config, spring-boot-starter-actuator
Refresh Feature: Annotate controller or bean with @RefreshScope to refresh
configuration at runtime.
Q. 5(a)   Suppose you are developing multiple microservices that need to discover each   10
other dynamically.
Explain how to set up a Discovery Server using Eureka, and how to configure
two microservices as Eureka Clients with proper settings in
application.properties.
1. Setup Eureka Server
server.port=8761
eureka.client.register-with-eureka=false
eureka.client.fetch-registry=false
@SpringBootApplication
@EnableEurekaServer
public class EurekaServerApp {}
2. Eureka Clients Configuration
spring.application.name=service1
eureka.client.service-url.defaultZone=http://localhost:8761/eureka/
• Add @EnableEurekaClient in Spring Boot main class.
• Repeat for second microservice.
Q. 5(b)   Explain the ideal CI/CD pipeline for Spring Boot microservices. Describe each   10
stage from code commit to monitoring and rollback, including the tools
commonly used and key actions performed at each stage. Additionally, explain
the benefits of implementing such a pipeline in a microservices architecture.
Stages:
1. Code Commit → GitHub/GitLab
2. Build → Maven/Gradle build & unit tests
3. Continuous Integration → Jenkins/CI server triggers build
********** 6 **********
--- page 7 ---
4. Artifact Repository → Nexus/Artifactory stores binaries
5. Deploy to Dev/Test → Docker/K8s for deployment
6. Automated Testing → Integration & E2E tests
7. Deploy to Production → Canary/Rolling updates
8. Monitoring → Prometheus/Grafana
9. Rollback → If failures, revert to previous stable deployment
Benefits: Faster release cycles, automated quality checks, minimal downtime,
early detection of errors.
Q. 6(a)   You are deploying a web application on a Kubernetes cluster that must be highly   10
available, scalable, and accessible to users through a domain name.
Explain how the following Kubernetes objects would be used:
1. Deployment
2. Service
3. ReplicaSet
4. Ingress
Object Purpose
Manages replica sets and rolling updates; ensures desired state of
Deployment
pods.
Service Provides stable IP/DNS to access pods; load balances traffic.
ReplicaSet Ensures specified number of pod replicas are running.
Manages external access to services; can provide SSL, routing, and
Ingress
host/path-based rules.
Q. 6(b)   What is Docker?   10
Explain the process of Dockerizing a Spring Boot Application with MySQL
using a Docker Network.
Include:
1. Creation of a Dockerfile and building a custom image
2. Setting up a MySQL container with environment variables in a shared
Docker network
1. Dockerfile for Spring Boot App
FROM openjdk:17-jdk-alpine
VOLUME /tmp
COPY target/app.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
•   Build: docker build -t springboot-app .
2. MySQL Container & Docker Network
docker network create mynetwork
docker run -d --name mysql-db --network mynetwork -e MYSQL_ROOT_PASSWORD=root -e
MYSQL_DATABASE=shopdb mysql:8
docker run -d --name springboot-app --network mynetwork -p 8080:8080 springboot-app
********** 7 **********
--- page 8 ---
Q. 7(a)   Explain the process of converting a monolithic application into microservices.   10
Also, describe the key steps involved in migrating existing monolithic
applications to a microservices architecture.
Process:
1. Identify business domains.
2. Split monolithic modules into independent services.
3. Design APIs for communication between services.
4. Implement Database per service if possible.
5. Use Service Discovery (Eureka), API Gateway, and Centralized
Logging.
Steps for Migrating Existing Monolith:
1. Analyze existing codebase and module boundaries.
2. Gradually extract modules as microservices (strangler pattern).
3. Implement inter-service communication via REST or messaging.
4. Ensure CI/CD and automated testing for each microservice.
5. Deploy microservices incrementally with monitoring.
Q. 7(b)   Write short notes on:   10
1. OAuth 2.0
2. JSON Web Token (JWT
. OAuth 2.0
•   Definition: OAuth 2.0 is an authorization framework that allows
applications to obtain limited access to user resources on another service
without sharing credentials.
• Roles:
1. Resource Owner – User who owns the data.
2. Client – Application requesting access.
3. Authorization Server – Issues access tokens after authentication.
4. Resource Server – Hosts protected resources, validates tokens.
• Flow:
1. Client requests authorization.
2. Authorization server authenticates user.
3. Server issues an access token.
4. Client uses token to access resources on the resource server.
• Grant Types: Authorization Code, Implicit, Password Credentials, Client
Credentials.
• Key Features:
1. Token-based access, scope-limited permissions, stateless and
secure.
2. JSON Web Token (JWT)
•   Definition: JWT is a compact, URL-safe token format for securely
transmitting claims between parties.
• Structure: 3 parts separated by dots (.):
********** 8 **********
--- page 9 ---
1. Header – Algorithm & token type.
2. Payload – Claims (e.g., user info, roles, expiry).
3. Signature – Ensures token integrity using secret or public/private
key.
• Usage:
1. Authentication: User logs in, server issues JWT, client sends it in
Authorization header for API access.
2. Stateless sessions – no server-side session storage needed.
• Advantages:
1. Lightweight, secure, easy to verify, cross-domain compatibility.
********** 9 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 671a187e72f5

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_Computer_7002/Microservices and Architecture/ANS_Microservices and Architecture(702CO0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (21 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   A banking application has a single codebase where UI, business logic,
and database access are tightly coupled. Any minor change requires full
redeployment. Identify the limitations of monolithic architecture in this
scenario and explain how they impact scalability and maintenance.
Ans.1.a.
In this scenario, the banking application follows a monolithic
architecture, where UI, business logic, and database layers are tightly
coupled within a single codebase. This design leads to several
CO- ;   limitations that directly affect scalability and maintenance.
SO- ;   [5]
BL-
Poor Scalability
• The application must be scaled as a whole, not component-wise.
Impact:
•   If only one module (e.g., login system) needs scaling, the entire
system must scale
• Leads to higher infrastructure cost
Difficult Maintenance
• Large codebase becomes complex over time.
********** 1 **********
--- page 2 ---
Impact:
• Hard for new developers to understand
• Debugging becomes time-consuming
•   Increased chances of introducing new errors
b.   When to use what:
i)   RestTemplate:
ii)   WebClient:
iii)   OpenFeign:
Ans.b.
CO- ;   •   RestTemplate: For simple, blocking HTTP calls in non-reactive
SO- ;   [5]
applications (legacy code, small projects). Generally avoid for new
BL-
development.
• WebClient: For modern, high-performance, reactive applications and
microservices.
• OpenFeign: For simplifying communication between microservices by
abstracting away HTTP details. Recommended for most microservice-to-
microservice communication.
c.
Why is testing more complex in microservices compared to monolithic
systems? Explain the role of test automation, service virtualization, and
contract testing in ensuring reliability of microservices.
Testing is More Complex in Microservices because:
1. Distributed Architecture
• Multiple services communicate over networks, so hrd to test
CO- ;   complete workflows end-to-end and Network failures and
SO- ;   latency issues arise.   [5]
BL-
2. Independent Deployments
• Each service can be updated independently so Version
compatibility issues and One service update may break others.
3. Multiple Technologies
•   Different services may use different languages/frameworks so
•   Difficult to maintain consistent testing strategy
4. Data Consistency Issues
********** 2 **********
--- page 3 ---
• Each service has its own database so it is hard to validate
transactions across services.
5. Increased Failure Points
• More services = more chances of failure so Debugging becomes
complex.
Role of Testing Techniques in Ensuring Reliability
1. Test Automation
What it is:
• Runs tests frequently (CI/CD pipelines)
•   Detects bugs early
• Supports regression testing
Benefit:
•   Faster and reliable testing
•   Essential for continuous delivery
2. Service Virtualization
What it is:
Simulating dependent services that are:
• Not available
• Costly
•   Still under development
Role:
• Allows testing of a service in isolation
• Mimics real service behavior
Benefit:
• Reduces dependency on external services
• Enables parallel development and testing
3. Contract Testing
What it is:
Testing the agreement (contract) between services:
• Request format
• Response format
Role:
• Ensures services interact correctly
•   Detects breaking changes early
********** 3 **********
--- page 4 ---
Benefit:
• Prevents integration failures
• Maintains compatibility between services
d.   What are the benefits of implementing a CI/CD pipeline in modern software
development?
Ans.1.d   CI/CD   (Continuous   Integration   and   Continuous
Delivery/Deployment) is a set of practices that automate the process of
building, testing, and deploying software frequently and reliably.
Continuous Integration (CI)
• Developers frequently merge code changes into a shared
repository
• Each change is automatically:
o Built
o Tested
Goal: Detect errors early
Continuous Delivery (CD)
• Code changes are automatically prepared for release
• Deployment is ready but may need manual approval
CO- ;   Continuous Deployment (CD)
SO- ;   • Every validated change is automatically deployed to production [5]
BL-
• No manual intervention required
2. Importance of CI/CD in Microservices
• Supports Independent Deployment Each microservice can be
built and deployed separately.
•   Faster Development and Release Cycle Automation reduces
manual effort. Frequent and quick releases.
3. Improved Code Quality
• Automated testing ensures bugs are caught early .More reliable
and stable services.
4. Scalability of Development Teams
• Multiple teams can work on different services simultaneously
5. Reduced Risk in Deployment
•   Small, incremental changes are easier to test and rollback
********** 4 **********
--- page 5 ---
o
Q.2.a.
a.   Why do we use Configuration Server in microservices architecture.
How does it help in managing dependencies? Explain in detail.
Ans 2.a
A Configuration Server is a centralized service that stores and
provides configuration properties (like database URLs, API keys, ports)
to all microservices.
Key Purposes
1. Centralized Configuration Management
•   All configurations are stored in one place (e.g., Git repository)
Benefit:
• Avoids duplication across services
• Easy to manage and update
2. Externalized Configuration
• Configuration is kept outside the application code
Benefit:
Q2   • No need to rebuild/redeploy services for config changes
[10]
CO-;
SO-;   [10]
3. Environment-Specific Configurations
BL-
• Supports different environments:
o Dev
o Test
o Production
Benefit:
• Same code works in multiple environments with different
configs
4. Dynamic Updates
•   Services can refresh configuration at runtime
Benefit:
• Changes applied without restarting services
2. How it Helps in Managing Dependencies
1. Central Control of Service Dependencies
• Configuration Server stores:
o Database connections
o External service URLs
********** 5 **********
--- page 6 ---
o API endpoints
•   Services don’t hardcode dependencies
• Easy to update when dependencies change
2. Loose Coupling
•   Services depend on configuration, not on fixed values
• Reduces tight coupling between services
• Improves flexibility
3. Easy Version Control
•   Configurations are stored in version control (e.g., Git)
• Track changes in dependencies
• Rollback if needed
4. Consistency Across Services
• Same configuration can be shared by multiple services
• Ensures uniform dependency settings
• Avoids mismatch errors
5. Simplifies Scaling and Deployment
• New services can fetch configuration dynamically
•   Faster onboarding of services
• No manual setup required
Example
Instead of hardcoding:
db.url=localhost:3306
Service fetches from Configuration Server:
db.url=prod-db-server:3306
Q 2.b Write steps to develop and run a “Hello World” application using
b.   Spring Boot.
Ans.2.b.
1. Create a Spring Boot Project
You can use:
• Spring Initializr (web tool)
• IDE like IntelliJ IDEA or Eclipse IDE
Steps:
•   Select:
********** 6 **********
--- page 7 ---
o   Project: Maven / Gradle
o Language: Java
o Dependencies: Spring Web
•   Generate and download project
2. Import Project into IDE
• Open IDE
•   Import the downloaded project as a Maven/Gradle project
3. Create Main Application Class
Spring Boot provides a main class like:
@SpringBootApplication
public class DemoApplication {
public static void main(String[] args) {
SpringApplication.run(DemoApplication.class, args);
}
}
4. Create Controller Class
Create a REST controller:
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
public class HelloController {
@GetMapping("/hello")
public String sayHello() {
return "Hello World";
}
}
5. Run the Application
• Run the main class (DemoApplication)
• Embedded server (Tomcat) starts automatically
6. Test the Application
Open browser or use Postman:
http://localhost:8080/hello
Output:
Hello World
Summary Flow
1. Create project
2. Import into IDE
********** 7 **********
--- page 8 ---
3. Write main class
4. Create controller
5. Run application
6. Test in browser
Q.3.b. Write a note on following?
a.   (i) Ribbon
(ii)Zuul
[10]
Ans Q3.b
b.   (ii)Ribbon:
Ribbon is an Inter-Process Communication (remote procedure calls) library
with a built-in software load balancer (which is mostly used for client-side
load balancing). Primarily it is used for REST calls with various serialization
scheme support.
How Ribbon Works (Step-by-Step)
1. Client makes a service call
The client (e.g., Order Service) wants to call another microservice.
2. Ribbon intercepts the request
Instead of directly calling the service, the request goes to Ribbon.
3. Service instance list is fetched
Ribbon gets available service instances from a service registry (like
Eureka).
4. Load-balancing decision
Ribbon applies a load-balancing algorithm such as:
o Round Robin
Q3   o Random
CO1-;   o Weighted response time
SO2-;   5. Request is sent to one instance
Ribbon forwards the request to the selected service instance.
BLU-
Advantages
• Reduces dependency on external load balancers
•   Faster decision-making (no extra network hop)
•   Better fault tolerance
(i)Zuul is an API Gateway developed by Netflix used in microservices
architecture to handle all incoming requests and route them to appropriate
services.
Key Functions
•   Routing: Directs client requests to specific microservices
•   Filtering: Performs pre and post processing (authentication, logging)
• Load Balancing: Distributes requests across instances
[10]
•   Security: Acts as a single entry point for enforcing security policies
Types of Filters
•   Pre-filters: Before request reaches service
•   Post-filters: After response is generated
********** 8 **********
--- page 9 ---
•   Route-filters: Handle routing
•   Error-filters: Handle failures
Advantages
•   Centralized control
• Improved security
•   Simplifies client interaction
• Reduces complexity of microservices communication
Q.3.a Why do we need the service discovering and registering process?
Explain with neat architecture diagram.
Ans 3.a. In a microservices architecture, services are:
• Deployed independently
• Scaled up/down dynamically
• Running on dynamic IP addresses and ports
Because of this, hardcoding service URLs is not feasible.
Service discovery and registration solve this problem by enabling
services to find and communicate with each other dynamically.
Eureka Architecture:
1.Service Registry (The Eureka Server):
The Eureka Server acts as a centralized "phonebook" for
microservices. It runs as a standalone application (typically on a
default port like 8761).
Microservices (called "clients") register themselves with the Eureka
Server when they start up, providing details like their hostname, IP
address, port, and a unique service ID.
2. Client Registration:
********** 9 **********

[Text in pictures on this page, read by OCR]
111.22.33.44:9090

| Request
111.22.33.44,8098 .
ENON Service B
Load 100.2.3.4:8090
Balancer :
Service B
[Resisters
333,111.33.1:8081
ee Instance List Query Service B
magaesaae° Disco
Service-B iscovery |.—_
ti22ssexs080)*#——F Service 111.22.33:8080

Service -A | 111:22:33:44:8098 Service B
--- page 10 ---
Each microservice includes a Eureka Client library (e.g., in Spring
Boot, via the spring-cloud-starter-netflix-eureka-client dependency).
When a service boots up, it sends a registration request to the
Eureka Server with its metadata. For example: "I’m Service A,
running at IP 192.168.1.10, port 8080."
The server stores this info in a registry—a dynamic list of all active
services.
3.Heartbeat and Health Checks:
Registered services send periodic "heartbeats" (typically every 30
seconds) to the Eureka Server to say, "I’m still alive!"
If a service stops sending heartbeats (e.g., it crashes), the Eureka
Server removes it from the registry after a timeout period. This
keeps the registry up-to-date.
4.Service Discovery:
When a microservice (e.g., Service B) needs to talk to another
service (e.g., Service A), it doesn’t hardcode the target’s address.
Instead, it asks the Eureka Server: "Where’s Service A?"
The Eureka Client in Service B fetches the current list of Service A
instances from the server (this list is cached locally and refreshed
periodically). Service B then picks an instance (often using a load
balancer like Netflix Ribbon).
[10]
a.   Q.4.a What challenges arise in ensuring security and service communication
throughout the microservices lifecycle?.
Ans.4.a.
Increased Attack Surface
Q4
Challenge:
CO-;
SO-;   • Each microservice exposes APIs, increasing the number of
BL-   attack entry points.
• Network-based communication makes services vulnerable to
external threats.
Solution:
• Use an API Gateway to act as a single entry point.
********** 10 **********
--- page 11 ---
• Apply centralized security controls such as authentication,
authorization, and rate limiting.
2️. Service-to-Service Authentication
Challenge:
• Ensuring that only authorized services communicate is difficult.
• Manual management of credentials does not scale in large
systems.
Solution:
• Implement OAuth 2.0, JWT, or mutual TLS (mTLS) for secure
service identity.
• Use role-based or policy-based access control for authorization.
3️ Secure Data Transmission
Challenge:
• Data exchanged between services may be intercepted.
• Lack of encryption can lead to data breaches.
Solution:
• Encrypt all inter-service communication using HTTPS/TLS.
• Use service mesh technologies to automatically enforce
encryption policies.
4️ API Versioning and Compatibility
Challenge:
• Multiple service versions may exist during upgrades.
• Breaking changes can disrupt dependent services.
Solution:
• Use proper API versioning strategies (URI-based, header-based).
• Ensure backward compatibility and gradual version deprecation.
5️. Policy Enforcement Across the Microservices Lifecycle
Challenge:
• Maintaining consistent security policies across development,
testing, and production is complex.
Solution:
•   Integrate automated security checks into the CI/CD pipeline.
********** 11 **********
--- page 12 ---
• Use static code analysis, dependency scanning, and security
testing tools.
4.b. Design and explain REST APIs for a student management system using
operations:
•   Create Employee
• Get Employee
[10]
•   Delete Employee
Specify endpoints, HTTP methods, and sample request/response structures.
Ans.4.b.
Base URL
https://api.university.com/employee
1. Create Employee
Endpoint
POST /employee
Creates a new employee record in the system.
Sample Request (JSON)
{
"employeeId": "S101",
"name": "Amit Sharma",
"age": 20,
"department": "Computer Science",
"email": "amit.sharma@univ.edu"
}
Sample Response (201 Created)
{
"message": "Employee created successfully",
"studentId": "S101"
}
2. Get Employee
Endpoint
GET /employees/{employeeId}
********** 12 **********
--- page 13 ---
Retrieves details of a specific student using the student ID.
Sample Request
GET /employees/S101
Sample Response (200 OK)
{
"employeeId": "S101",
"name": "Amit Sharma",
"age": 20,
"department": "Computer Science",
"email": "amit.sharma@univ.edu"
}
3. Delete Employee
Endpoint
DELETE /employees/{employeeId}
Deletes an employee record from the system.
Sample Request
DELETE /employees/S101
Sample Response (200 OK)
{
"message": "Employee deleted successfully"
}
[10]
What is topic in Kafka. Explain Kafka architecture with a suitable use case.
a.
b.
Kafka Topic
Q5
CO-;
SO-;
BL-
• A logical channel for messages.
• Comparable to a table in a database or a folder in a file system.
•   Identified by a unique name.
• You can have any number of topics.
•   Producers send data to topics; consumers subscribe to topics.
•   Internally, topics are divided into partitions.
•   Topics help in organizing data streams.
********** 13 **********
--- page 14 ---
• Data can be retained even after consumption depending on the
retention policy.
Kafka Workflow (Basic Flow)
1. Producer sends messages to a topic.
2. Kafka stores messages in partitions.
3. Consumer reads messages using offsets.
4. Kafka retains messages for a configured time (default 7 days).
Kafka Use Cases
•   Real-time analytics
• Logging and monitoring
•   Event sourcing
• Messaging system
• Stream processing
Features of Kafka
1. Publish-Subscribe System
o Producers send messages.
o Consumers receive messages from topics.
Apache Kafka Architecture :
1. Kafka Producer
• Sends messages to Kafka topics.
• Can choose the partition or let Kafka decide.
• Sends key-value pairs.
•   Writes are asynchronous and allow high throughput.
********** 14 **********

[Text in pictures on this page, read by OCR]
Kafka Cluster with group of brokers

Broker 1

Topics

& Partitions Pull messagt
=f a a
altri ts]

Messages get stored in partitions using offset ids

Push messages

4
papxa}

Broker 2 Pull message

Broker 3
--- page 15 ---
• Does not directly communicate with the consumer.
•   Acts as the entry point for data into the Kafka system.
2. Kafka Cluster
• A Kafka cluster consists of multiple brokers (minimum 3
recommended).
•   Enables scalability, fault tolerance, and replication.
• Can handle failover and load balancing.
•   Partitions are spread across the brokers in the cluster.
3. Kafka Broker
• A Kafka cluster is made of multiple brokers.
• A Kafka broker is a Kafka server.
•   It stores data (partitions) and handles client requests
(producers/consumers).
• Each broker has a unique ID.
• Kafka topics are divided into partitions, stored across brokers.
•   Brokers are distributed and horizontally scalable (just add more to
scale ie increase load handling).
•   Brokers do not share partitions – each partition belongs to one
leader broker at a time.
Kafka brokers store data durably on disk and support replication.
4. Kafka Partitions
• A single topic can have multiple partitions.
•   Partitions allow parallelism and scalability.
• Each partition is ordered, and messages are stored sequentially.
• A partition belongs to only one broker (leader) at a time.
More partitions = More parallelism, but also more complexity
[Use case can be to explain with e-commerce site example]
Q.5.b. Why the distributed transactions should be avoided with the use of two-
phase commit protocol? How the identified issues can be solved?
Ans.5.b. Distributed transactions using the Two-Phase Commit (2PC)
protocol are generally avoided in microservices and distributed systems
because they introduce several serious drawbacks related to
performance, scalability, and availability. Although 2PC guarantees
********** 15 **********
--- page 16 ---
atomicity across multiple services, it contradicts the core principles of
microservices such as loose coupling and independent service
operation.
One major reason for avoiding 2PC is its blocking nature. In the 2PC
protocol, if the coordinator fails after participants have agreed to
commit but before the final decision is communicated, all participating
services remain blocked while holding locks on resources. This can lead
to resource starvation and system unavailability. Additionally, 2PC
significantly reduces scalability because each service must lock its
resources until the global transaction completes, limiting throughput as
the number of services grows.
Another critical issue is reduced availability. The failure of even a
single participant or the coordinator can cause the entire transaction to
fail or hang indefinitely. This tightly couples the availability of all
participating services, which is undesirable in distributed environments.
Furthermore, 2PC incurs high performance overhead due to multiple
network round trips and coordination messages, increasing latency and
reducing system responsiveness.
To solve these issues, modern distributed systems prefer eventual
consistency–based approaches. The most widely adopted solution is
the Saga pattern, where a distributed transaction is broken into a
sequence of local transactions managed by individual services. Each
service completes its transaction independently and publishes an event.
If a failure occurs, compensating transactions are executed to undo
previous actions, eliminating the need for global locks and blocking.
Sagas can be implemented using choreography (event-driven) or
orchestration (central controller).
Another solution is adopting eventual consistency, where temporary
inconsistencies are allowed but the system eventually reaches a
consistent state. This approach improves availability and fault tolerance.
[10]
“Service-to-service communication is managed through an intermediate
a.
infrastructure layer.” What is this layer? Explain with architecture diagram.
Ans.6.a
Q6   A Service Mesh is an architectural layer used in microservices
architecture to manage service-to-service communication in a
CO-;
reliable, secure, and observable manner. Instead of embedding
SO-;
communication logic inside application code, a service mesh offloads
BL-
these concerns to a dedicated infrastructure layer, allowing developers
to focus only on business logic.
In a service mesh, every microservice instance is paired with a
lightweight network proxy, and all service-to-service communication
passes through these proxies. This approach provides consistent
********** 16 **********
--- page 17 ---
handling of cross-cutting concerns such as traffic management, security,
observability, and resilience.
Service Mesh :
At a high level, a service mesh consists of two planes:
• Data Plane
• Control Plane
The application services do not communicate directly with each other.
Instead, communication flows through sidecar proxies that form the
data plane, while the control plane manages and configures these
proxies.
Key Components of Service Mesh
1. Data Plane (Sidecar Proxies)
The data plane consists of lightweight proxies (often deployed as
sidecars) that run alongside each microservice. These proxies intercept
all inbound and outbound traffic between services. They handle tasks
such as load balancing, service discovery, retries, timeouts, circuit
breaking, encryption, and telemetry collection. Since the proxy is
independent of application code, communication policies can be
changed without redeploying services.
2. Control Plane
The control plane manages and configures the data plane proxies. It
defines traffic policies, security rules, and routing behavior and then
pushes these configurations dynamically to the proxies. The control
plane does not handle application traffic directly; instead, it acts as the
brain of the service mesh.
3. Traffic Management Component
This component controls how requests are routed between services. It
supports features such as intelligent load balancing, canary
deployments, blue-green deployments, traffic splitting, retries, and fault
injection. Traffic management helps improve reliability and enables
safe deployment strategies.
4. Security Component
The security layer of a service mesh provides mutual TLS (mTLS) for
service-to-service authentication and encryption. It also supports
authorization policies, certificate management, and identity verification.
This ensures zero-trust communication within the microservices
environment.
5. Observability Component
Service mesh provides deep observability into service interactions. It
collects metrics, logs, and distributed traces automatically without
requiring changes in application code. This helps in monitoring latency,
error rates, service dependencies, and overall system health.
********** 17 **********
--- page 18 ---
6. Policy and Configuration Management
This component allows administrators to define and enforce policies
such as rate limiting, access control, quotas, and retry rules centrally.
Policies are consistently applied across all services through the data
plane proxies.
[10]
b.
Q.6.b. A food delivery platform integrates restaurant, delivery, and payment
services. Real-time updates are required. Identify suitable integration patterns
and justify their use.
Ans.6.b.
The Event-Driven Architecture (EDA) pattern is highly suitable for
this scenario. In this pattern, services communicate by producing and
consuming events rather than direct synchronous calls. For example,
when an order is placed, the restaurant service publishes an
OrderPlaced event, which is consumed by the delivery and payment
services. This enables real-time updates such as order confirmation,
preparation status, and delivery tracking. Event-driven integration
ensures low latency, high scalability, and loose coupling between
services.
The Publish–Subscribe (Pub/Sub) pattern is another appropriate
integration pattern. In this pattern, the restaurant service publishes
events (e.g., FoodPrepared), and multiple subscribers such as the
delivery service, notification service, and user interface can receive
these updates simultaneously. This is ideal for real-time notifications
like “order accepted,” “out for delivery,” and “delivered,” without the
publisher needing to know who the consumers are.
********** 18 **********

[Text in pictures on this page, read by OCR]
Peta... nonnnne ny nnn
Microservice - P
Business
awe Service Mesh
Network
Functions Ieee. h

Application Network

Functions Data Plane
--- page 19 ---
For managing transactions across payment, restaurant, and delivery
services, the Saga pattern is recommended. Instead of using distributed
transactions, a saga coordinates a sequence of local transactions. For
example, after payment confirmation, the restaurant accepts the order; if
the restaurant rejects it, a compensating action such as payment refund
is triggered. This pattern ensures data consistency while maintaining
system availability and avoiding blocking issues.
The Asynchronous Messaging pattern using message brokers (such as
queues or streams) is essential for real-time systems. It allows services
to communicate without waiting for immediate responses, improving
responsiveness and fault tolerance. If one service is temporarily
unavailable, messages are queued and processed later, ensuring reliable
communication.
The API Gateway pattern is useful for external communication with
client applications. The gateway provides a single entry point for
mobile or web apps, routes requests to appropriate services, and
aggregates responses. It can also push real-time updates to clients using
WebSockets or server-sent events.
Q.7.a. What is OAuth2.0. When should we choose this protocol?
Ans.7.a.
[10]
Q7
CO-;
SO-;
BL-
[10]
The flow shown in above Figure includes the following steps: 1. The
resource owner (user) provides the client application with it's username
and password. 2. The Client Application requests an access token from
the Authorization Server (Facebook) by passing credentials received
from the resource owner. 3. The Authorization Server(Facebook)
authenticates the client by validating the resource owner credentials.
********** 19 **********
--- page 20 ---
Once Validation is successful and if request is valid, it sends an access
token. 4. Client sends the received access token to Resource Server
(Facebook where) to access the resource end point. 5. Resource Server
validates the access token by calling Authorization Server. 6. If the
token is valid, resource server return the requested resource (e.g.,
profile data) to Client and You see your data in the Client app.
Note: - 1. Authorization Server (e.g., Facebook): Handles user login and
issues access tokens to apps after authentication and authorization. 2.
Resource Server (e.g., Facebook): Stores and provides user data (e.g.,
profile) to apps once a valid token is presented. In short: Authorization
Server grants access; Resource Server delivers the data. 3.
Authorization Code: A temporary code issued by the Authorization
Server after user approval, exchanged by the client for an Access
Token. 4. Access Token: A credential sent to the Resource Server to
access user data, valid for a set time.
Q.7.b. Write steps to migrate Existing monolithic Applications to
Microservices.
(1 step = 1 mark)
Ans.7.b.
1. Assessment and Planning: Evaluate the monolithic application to
understand its architecture, dependencies, and functionalities. Identify the
parts of the application that can be modularized and migrated to
microservices.
2. Define Microservices Boundaries: (Decomposition) Break down the
monolithic application into smaller, loosely coupled services. Define the
boundaries (bounded contexts) of microservices based on business
functionalities. Each microservice should have a well-defined scope and
responsibility. Consider factors such as domain-driven design (DDD)
principles and the single responsibility principle (SRP).
3. Database Decoupling: If the monolithic application shares a database,
consider decoupling the database to enable each microservice to have its own
database or a subset of the original database.
********** 20 **********
--- page 21 ---
4. Identify and Extract Services: Identify modules or functionalities in the
monolithic application that can be extracted into microservices. Start with less
critical or isolated parts of the application to minimize risk. Determine the
dependencies between services and define communication mechanisms (e.g.,
REST, messaging).
5. Refactor and Rewrite: Refactor the extracted modules into microservices,
using modern frameworks and technologies. Rewrite any parts of the
application that are tightly coupled or rely heavily on the monolithic
architecture.
6. Implement API Gateway: Implement an API gateway to manage and route
requests to the appropriate microservices. The API gateway can also handle
authentication, rate limiting, and other cross-cutting concerns.
7. Implement Service Discovery: Use a service discovery mechanism to
enable microservices to locate and communicate with each other dynamically.
8. Containerization: Containerize each microservice using Docker or similar
tools to ensure consistency and portability across different environments.
9. Orchestration: Use a container orchestration tool like Kubernetes to manage
and scale the microservices in a distributed environment.
10. Testing and Deployment: Test each microservice individually to ensure
functionality and compatibility. At a minimum each micorservice should be
independently deployable therefore Implement a continuous integration and
deployment (CI/CD) pipeline to automate the deployment process.
11. Monitoring and Logging: Implement monitoring and logging mechanisms
to track the performance and behavior of microservices in real-time. For
example, you might use Docker and Kubernetes for deployment and Use tools
like Prometheus and Grafana for monitoring.
12. Iterative Approach: Migrate the monolithic application to microservices in
an iterative manner, starting with smaller, less critical parts of the application
and gradually expanding to other areas.
13. Incremental Improvement: Continuously monitor and improve the
performance, scalability, and reliability of the microservices architecture
based on feedback and insights gathered during the migration process.
Migrating from a monolithic architecture to microservices is a complex
process that requires careful planning, execution, and continuous
improvement. It's essential to involve all stakeholders, including developers,
architects, and operations teams, to ensure a smooth and successful transition
********** 21 **********
````

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 2bcaf4a16a34

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/MBATech_Computer_7047/Microservices and Architecture/ANS_Microservices and Architecture(702CO0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (21 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   A banking application has a single codebase where UI, business logic,
and database access are tightly coupled. Any minor change requires full
redeployment. Identify the limitations of monolithic architecture in this
scenario and explain how they impact scalability and maintenance.
Ans.1.a.
In this scenario, the banking application follows a monolithic
architecture, where UI, business logic, and database layers are tightly
coupled within a single codebase. This design leads to several
CO- ;   limitations that directly affect scalability and maintenance.
SO- ;   [5]
BL-
Poor Scalability
• The application must be scaled as a whole, not component-wise.
Impact:
•   If only one module (e.g., login system) needs scaling, the entire
system must scale
• Leads to higher infrastructure cost
Difficult Maintenance
• Large codebase becomes complex over time.
********** 1 **********
--- page 2 ---
Impact:
• Hard for new developers to understand
• Debugging becomes time-consuming
•   Increased chances of introducing new errors
b.   When to use what:
i)   RestTemplate:
ii)   WebClient:
iii)   OpenFeign:
Ans.b.
CO- ;   •   RestTemplate: For simple, blocking HTTP calls in non-reactive
SO- ;   [5]
applications (legacy code, small projects). Generally avoid for new
BL-
development.
• WebClient: For modern, high-performance, reactive applications and
microservices.
• OpenFeign: For simplifying communication between microservices by
abstracting away HTTP details. Recommended for most microservice-to-
microservice communication.
c.
Why is testing more complex in microservices compared to monolithic
systems? Explain the role of test automation, service virtualization, and
contract testing in ensuring reliability of microservices.
Testing is More Complex in Microservices because:
1. Distributed Architecture
• Multiple services communicate over networks, so hrd to test
CO- ;   complete workflows end-to-end and Network failures and
SO- ;   latency issues arise.   [5]
BL-
2. Independent Deployments
• Each service can be updated independently so Version
compatibility issues and One service update may break others.
3. Multiple Technologies
•   Different services may use different languages/frameworks so
•   Difficult to maintain consistent testing strategy
4. Data Consistency Issues
********** 2 **********
--- page 3 ---
• Each service has its own database so it is hard to validate
transactions across services.
5. Increased Failure Points
• More services = more chances of failure so Debugging becomes
complex.
Role of Testing Techniques in Ensuring Reliability
1. Test Automation
What it is:
• Runs tests frequently (CI/CD pipelines)
•   Detects bugs early
• Supports regression testing
Benefit:
•   Faster and reliable testing
•   Essential for continuous delivery
2. Service Virtualization
What it is:
Simulating dependent services that are:
• Not available
• Costly
•   Still under development
Role:
• Allows testing of a service in isolation
• Mimics real service behavior
Benefit:
• Reduces dependency on external services
• Enables parallel development and testing
3. Contract Testing
What it is:
Testing the agreement (contract) between services:
• Request format
• Response format
Role:
• Ensures services interact correctly
•   Detects breaking changes early
********** 3 **********
--- page 4 ---
Benefit:
• Prevents integration failures
• Maintains compatibility between services
d.   What are the benefits of implementing a CI/CD pipeline in modern software
development?
Ans.1.d   CI/CD   (Continuous   Integration   and   Continuous
Delivery/Deployment) is a set of practices that automate the process of
building, testing, and deploying software frequently and reliably.
Continuous Integration (CI)
• Developers frequently merge code changes into a shared
repository
• Each change is automatically:
o Built
o Tested
Goal: Detect errors early
Continuous Delivery (CD)
• Code changes are automatically prepared for release
• Deployment is ready but may need manual approval
CO- ;   Continuous Deployment (CD)
SO- ;   • Every validated change is automatically deployed to production [5]
BL-
• No manual intervention required
2. Importance of CI/CD in Microservices
• Supports Independent Deployment Each microservice can be
built and deployed separately.
•   Faster Development and Release Cycle Automation reduces
manual effort. Frequent and quick releases.
3. Improved Code Quality
• Automated testing ensures bugs are caught early .More reliable
and stable services.
4. Scalability of Development Teams
• Multiple teams can work on different services simultaneously
5. Reduced Risk in Deployment
•   Small, incremental changes are easier to test and rollback
********** 4 **********
--- page 5 ---
o
Q.2.a.
a.   Why do we use Configuration Server in microservices architecture.
How does it help in managing dependencies? Explain in detail.
Ans 2.a
A Configuration Server is a centralized service that stores and
provides configuration properties (like database URLs, API keys, ports)
to all microservices.
Key Purposes
1. Centralized Configuration Management
•   All configurations are stored in one place (e.g., Git repository)
Benefit:
• Avoids duplication across services
• Easy to manage and update
2. Externalized Configuration
• Configuration is kept outside the application code
Benefit:
Q2   • No need to rebuild/redeploy services for config changes
[10]
CO-;
SO-;   [10]
3. Environment-Specific Configurations
BL-
• Supports different environments:
o Dev
o Test
o Production
Benefit:
• Same code works in multiple environments with different
configs
4. Dynamic Updates
•   Services can refresh configuration at runtime
Benefit:
• Changes applied without restarting services
2. How it Helps in Managing Dependencies
1. Central Control of Service Dependencies
• Configuration Server stores:
o Database connections
o External service URLs
********** 5 **********
--- page 6 ---
o API endpoints
•   Services don’t hardcode dependencies
• Easy to update when dependencies change
2. Loose Coupling
•   Services depend on configuration, not on fixed values
• Reduces tight coupling between services
• Improves flexibility
3. Easy Version Control
•   Configurations are stored in version control (e.g., Git)
• Track changes in dependencies
• Rollback if needed
4. Consistency Across Services
• Same configuration can be shared by multiple services
• Ensures uniform dependency settings
• Avoids mismatch errors
5. Simplifies Scaling and Deployment
• New services can fetch configuration dynamically
•   Faster onboarding of services
• No manual setup required
Example
Instead of hardcoding:
db.url=localhost:3306
Service fetches from Configuration Server:
db.url=prod-db-server:3306
Q 2.b Write steps to develop and run a “Hello World” application using
b.   Spring Boot.
Ans.2.b.
1. Create a Spring Boot Project
You can use:
• Spring Initializr (web tool)
• IDE like IntelliJ IDEA or Eclipse IDE
Steps:
•   Select:
********** 6 **********
--- page 7 ---
o   Project: Maven / Gradle
o Language: Java
o Dependencies: Spring Web
•   Generate and download project
2. Import Project into IDE
• Open IDE
•   Import the downloaded project as a Maven/Gradle project
3. Create Main Application Class
Spring Boot provides a main class like:
@SpringBootApplication
public class DemoApplication {
public static void main(String[] args) {
SpringApplication.run(DemoApplication.class, args);
}
}
4. Create Controller Class
Create a REST controller:
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
public class HelloController {
@GetMapping("/hello")
public String sayHello() {
return "Hello World";
}
}
5. Run the Application
• Run the main class (DemoApplication)
• Embedded server (Tomcat) starts automatically
6. Test the Application
Open browser or use Postman:
http://localhost:8080/hello
Output:
Hello World
Summary Flow
1. Create project
2. Import into IDE
********** 7 **********
--- page 8 ---
3. Write main class
4. Create controller
5. Run application
6. Test in browser
Q.3.b. Write a note on following?
a.   (i) Ribbon
(ii)Zuul
[10]
Ans Q3.b
b.   (ii)Ribbon:
Ribbon is an Inter-Process Communication (remote procedure calls) library
with a built-in software load balancer (which is mostly used for client-side
load balancing). Primarily it is used for REST calls with various serialization
scheme support.
How Ribbon Works (Step-by-Step)
1. Client makes a service call
The client (e.g., Order Service) wants to call another microservice.
2. Ribbon intercepts the request
Instead of directly calling the service, the request goes to Ribbon.
3. Service instance list is fetched
Ribbon gets available service instances from a service registry (like
Eureka).
4. Load-balancing decision
Ribbon applies a load-balancing algorithm such as:
o Round Robin
Q3   o Random
CO1-;   o Weighted response time
SO2-;   5. Request is sent to one instance
Ribbon forwards the request to the selected service instance.
BLU-
Advantages
• Reduces dependency on external load balancers
•   Faster decision-making (no extra network hop)
•   Better fault tolerance
(i)Zuul is an API Gateway developed by Netflix used in microservices
architecture to handle all incoming requests and route them to appropriate
services.
Key Functions
•   Routing: Directs client requests to specific microservices
•   Filtering: Performs pre and post processing (authentication, logging)
• Load Balancing: Distributes requests across instances
[10]
•   Security: Acts as a single entry point for enforcing security policies
Types of Filters
•   Pre-filters: Before request reaches service
•   Post-filters: After response is generated
********** 8 **********
--- page 9 ---
•   Route-filters: Handle routing
•   Error-filters: Handle failures
Advantages
•   Centralized control
• Improved security
•   Simplifies client interaction
• Reduces complexity of microservices communication
Q.3.a Why do we need the service discovering and registering process?
Explain with neat architecture diagram.
Ans 3.a. In a microservices architecture, services are:
• Deployed independently
• Scaled up/down dynamically
• Running on dynamic IP addresses and ports
Because of this, hardcoding service URLs is not feasible.
Service discovery and registration solve this problem by enabling
services to find and communicate with each other dynamically.
Eureka Architecture:
1.Service Registry (The Eureka Server):
The Eureka Server acts as a centralized "phonebook" for
microservices. It runs as a standalone application (typically on a
default port like 8761).
Microservices (called "clients") register themselves with the Eureka
Server when they start up, providing details like their hostname, IP
address, port, and a unique service ID.
2. Client Registration:
********** 9 **********

[Text in pictures on this page, read by OCR]
111.22.33.44:9090

| Request
111.22.33.44,8098 .
ENON Service B
Load 100.2.3.4:8090
Balancer :
Service B
[Resisters
333,111.33.1:8081
ee Instance List Query Service B
magaesaae° Disco
Service-B iscovery |.—_
ti22ssexs080)*#——F Service 111.22.33:8080

Service -A | 111:22:33:44:8098 Service B
--- page 10 ---
Each microservice includes a Eureka Client library (e.g., in Spring
Boot, via the spring-cloud-starter-netflix-eureka-client dependency).
When a service boots up, it sends a registration request to the
Eureka Server with its metadata. For example: "I’m Service A,
running at IP 192.168.1.10, port 8080."
The server stores this info in a registry—a dynamic list of all active
services.
3.Heartbeat and Health Checks:
Registered services send periodic "heartbeats" (typically every 30
seconds) to the Eureka Server to say, "I’m still alive!"
If a service stops sending heartbeats (e.g., it crashes), the Eureka
Server removes it from the registry after a timeout period. This
keeps the registry up-to-date.
4.Service Discovery:
When a microservice (e.g., Service B) needs to talk to another
service (e.g., Service A), it doesn’t hardcode the target’s address.
Instead, it asks the Eureka Server: "Where’s Service A?"
The Eureka Client in Service B fetches the current list of Service A
instances from the server (this list is cached locally and refreshed
periodically). Service B then picks an instance (often using a load
balancer like Netflix Ribbon).
[10]
a.   Q.4.a What challenges arise in ensuring security and service communication
throughout the microservices lifecycle?.
Ans.4.a.
Increased Attack Surface
Q4
Challenge:
CO-;
SO-;   • Each microservice exposes APIs, increasing the number of
BL-   attack entry points.
• Network-based communication makes services vulnerable to
external threats.
Solution:
• Use an API Gateway to act as a single entry point.
********** 10 **********
--- page 11 ---
• Apply centralized security controls such as authentication,
authorization, and rate limiting.
2️. Service-to-Service Authentication
Challenge:
• Ensuring that only authorized services communicate is difficult.
• Manual management of credentials does not scale in large
systems.
Solution:
• Implement OAuth 2.0, JWT, or mutual TLS (mTLS) for secure
service identity.
• Use role-based or policy-based access control for authorization.
3️ Secure Data Transmission
Challenge:
• Data exchanged between services may be intercepted.
• Lack of encryption can lead to data breaches.
Solution:
• Encrypt all inter-service communication using HTTPS/TLS.
• Use service mesh technologies to automatically enforce
encryption policies.
4️ API Versioning and Compatibility
Challenge:
• Multiple service versions may exist during upgrades.
• Breaking changes can disrupt dependent services.
Solution:
• Use proper API versioning strategies (URI-based, header-based).
• Ensure backward compatibility and gradual version deprecation.
5️. Policy Enforcement Across the Microservices Lifecycle
Challenge:
• Maintaining consistent security policies across development,
testing, and production is complex.
Solution:
•   Integrate automated security checks into the CI/CD pipeline.
********** 11 **********
--- page 12 ---
• Use static code analysis, dependency scanning, and security
testing tools.
4.b. Design and explain REST APIs for a student management system using
operations:
•   Create Employee
• Get Employee
[10]
•   Delete Employee
Specify endpoints, HTTP methods, and sample request/response structures.
Ans.4.b.
Base URL
https://api.university.com/employee
1. Create Employee
Endpoint
POST /employee
Creates a new employee record in the system.
Sample Request (JSON)
{
"employeeId": "S101",
"name": "Amit Sharma",
"age": 20,
"department": "Computer Science",
"email": "amit.sharma@univ.edu"
}
Sample Response (201 Created)
{
"message": "Employee created successfully",
"studentId": "S101"
}
2. Get Employee
Endpoint
GET /employees/{employeeId}
********** 12 **********
--- page 13 ---
Retrieves details of a specific student using the student ID.
Sample Request
GET /employees/S101
Sample Response (200 OK)
{
"employeeId": "S101",
"name": "Amit Sharma",
"age": 20,
"department": "Computer Science",
"email": "amit.sharma@univ.edu"
}
3. Delete Employee
Endpoint
DELETE /employees/{employeeId}
Deletes an employee record from the system.
Sample Request
DELETE /employees/S101
Sample Response (200 OK)
{
"message": "Employee deleted successfully"
}
[10]
What is topic in Kafka. Explain Kafka architecture with a suitable use case.
a.
b.
Kafka Topic
Q5
CO-;
SO-;
BL-
• A logical channel for messages.
• Comparable to a table in a database or a folder in a file system.
•   Identified by a unique name.
• You can have any number of topics.
•   Producers send data to topics; consumers subscribe to topics.
•   Internally, topics are divided into partitions.
•   Topics help in organizing data streams.
********** 13 **********
--- page 14 ---
• Data can be retained even after consumption depending on the
retention policy.
Kafka Workflow (Basic Flow)
1. Producer sends messages to a topic.
2. Kafka stores messages in partitions.
3. Consumer reads messages using offsets.
4. Kafka retains messages for a configured time (default 7 days).
Kafka Use Cases
•   Real-time analytics
• Logging and monitoring
•   Event sourcing
• Messaging system
• Stream processing
Features of Kafka
1. Publish-Subscribe System
o Producers send messages.
o Consumers receive messages from topics.
Apache Kafka Architecture :
1. Kafka Producer
• Sends messages to Kafka topics.
• Can choose the partition or let Kafka decide.
• Sends key-value pairs.
•   Writes are asynchronous and allow high throughput.
********** 14 **********

[Text in pictures on this page, read by OCR]
Kafka Cluster with group of brokers

Broker 1

Topics

& Partitions Pull messagt
=f a a
altri ts]

Messages get stored in partitions using offset ids

Push messages

4
papxa}

Broker 2 Pull message

Broker 3
--- page 15 ---
• Does not directly communicate with the consumer.
•   Acts as the entry point for data into the Kafka system.
2. Kafka Cluster
• A Kafka cluster consists of multiple brokers (minimum 3
recommended).
•   Enables scalability, fault tolerance, and replication.
• Can handle failover and load balancing.
•   Partitions are spread across the brokers in the cluster.
3. Kafka Broker
• A Kafka cluster is made of multiple brokers.
• A Kafka broker is a Kafka server.
•   It stores data (partitions) and handles client requests
(producers/consumers).
• Each broker has a unique ID.
• Kafka topics are divided into partitions, stored across brokers.
•   Brokers are distributed and horizontally scalable (just add more to
scale ie increase load handling).
•   Brokers do not share partitions – each partition belongs to one
leader broker at a time.
Kafka brokers store data durably on disk and support replication.
4. Kafka Partitions
• A single topic can have multiple partitions.
•   Partitions allow parallelism and scalability.
• Each partition is ordered, and messages are stored sequentially.
• A partition belongs to only one broker (leader) at a time.
More partitions = More parallelism, but also more complexity
[Use case can be to explain with e-commerce site example]
Q.5.b. Why the distributed transactions should be avoided with the use of two-
phase commit protocol? How the identified issues can be solved?
Ans.5.b. Distributed transactions using the Two-Phase Commit (2PC)
protocol are generally avoided in microservices and distributed systems
because they introduce several serious drawbacks related to
performance, scalability, and availability. Although 2PC guarantees
********** 15 **********
--- page 16 ---
atomicity across multiple services, it contradicts the core principles of
microservices such as loose coupling and independent service
operation.
One major reason for avoiding 2PC is its blocking nature. In the 2PC
protocol, if the coordinator fails after participants have agreed to
commit but before the final decision is communicated, all participating
services remain blocked while holding locks on resources. This can lead
to resource starvation and system unavailability. Additionally, 2PC
significantly reduces scalability because each service must lock its
resources until the global transaction completes, limiting throughput as
the number of services grows.
Another critical issue is reduced availability. The failure of even a
single participant or the coordinator can cause the entire transaction to
fail or hang indefinitely. This tightly couples the availability of all
participating services, which is undesirable in distributed environments.
Furthermore, 2PC incurs high performance overhead due to multiple
network round trips and coordination messages, increasing latency and
reducing system responsiveness.
To solve these issues, modern distributed systems prefer eventual
consistency–based approaches. The most widely adopted solution is
the Saga pattern, where a distributed transaction is broken into a
sequence of local transactions managed by individual services. Each
service completes its transaction independently and publishes an event.
If a failure occurs, compensating transactions are executed to undo
previous actions, eliminating the need for global locks and blocking.
Sagas can be implemented using choreography (event-driven) or
orchestration (central controller).
Another solution is adopting eventual consistency, where temporary
inconsistencies are allowed but the system eventually reaches a
consistent state. This approach improves availability and fault tolerance.
[10]
“Service-to-service communication is managed through an intermediate
a.
infrastructure layer.” What is this layer? Explain with architecture diagram.
Ans.6.a
Q6   A Service Mesh is an architectural layer used in microservices
architecture to manage service-to-service communication in a
CO-;
reliable, secure, and observable manner. Instead of embedding
SO-;
communication logic inside application code, a service mesh offloads
BL-
these concerns to a dedicated infrastructure layer, allowing developers
to focus only on business logic.
In a service mesh, every microservice instance is paired with a
lightweight network proxy, and all service-to-service communication
passes through these proxies. This approach provides consistent
********** 16 **********
--- page 17 ---
handling of cross-cutting concerns such as traffic management, security,
observability, and resilience.
Service Mesh :
At a high level, a service mesh consists of two planes:
• Data Plane
• Control Plane
The application services do not communicate directly with each other.
Instead, communication flows through sidecar proxies that form the
data plane, while the control plane manages and configures these
proxies.
Key Components of Service Mesh
1. Data Plane (Sidecar Proxies)
The data plane consists of lightweight proxies (often deployed as
sidecars) that run alongside each microservice. These proxies intercept
all inbound and outbound traffic between services. They handle tasks
such as load balancing, service discovery, retries, timeouts, circuit
breaking, encryption, and telemetry collection. Since the proxy is
independent of application code, communication policies can be
changed without redeploying services.
2. Control Plane
The control plane manages and configures the data plane proxies. It
defines traffic policies, security rules, and routing behavior and then
pushes these configurations dynamically to the proxies. The control
plane does not handle application traffic directly; instead, it acts as the
brain of the service mesh.
3. Traffic Management Component
This component controls how requests are routed between services. It
supports features such as intelligent load balancing, canary
deployments, blue-green deployments, traffic splitting, retries, and fault
injection. Traffic management helps improve reliability and enables
safe deployment strategies.
4. Security Component
The security layer of a service mesh provides mutual TLS (mTLS) for
service-to-service authentication and encryption. It also supports
authorization policies, certificate management, and identity verification.
This ensures zero-trust communication within the microservices
environment.
5. Observability Component
Service mesh provides deep observability into service interactions. It
collects metrics, logs, and distributed traces automatically without
requiring changes in application code. This helps in monitoring latency,
error rates, service dependencies, and overall system health.
********** 17 **********
--- page 18 ---
6. Policy and Configuration Management
This component allows administrators to define and enforce policies
such as rate limiting, access control, quotas, and retry rules centrally.
Policies are consistently applied across all services through the data
plane proxies.
[10]
b.
Q.6.b. A food delivery platform integrates restaurant, delivery, and payment
services. Real-time updates are required. Identify suitable integration patterns
and justify their use.
Ans.6.b.
The Event-Driven Architecture (EDA) pattern is highly suitable for
this scenario. In this pattern, services communicate by producing and
consuming events rather than direct synchronous calls. For example,
when an order is placed, the restaurant service publishes an
OrderPlaced event, which is consumed by the delivery and payment
services. This enables real-time updates such as order confirmation,
preparation status, and delivery tracking. Event-driven integration
ensures low latency, high scalability, and loose coupling between
services.
The Publish–Subscribe (Pub/Sub) pattern is another appropriate
integration pattern. In this pattern, the restaurant service publishes
events (e.g., FoodPrepared), and multiple subscribers such as the
delivery service, notification service, and user interface can receive
these updates simultaneously. This is ideal for real-time notifications
like “order accepted,” “out for delivery,” and “delivered,” without the
publisher needing to know who the consumers are.
********** 18 **********

[Text in pictures on this page, read by OCR]
Peta... nonnnne ny nnn
Microservice - P
Business
awe Service Mesh
Network
Functions Ieee. h

Application Network

Functions Data Plane
--- page 19 ---
For managing transactions across payment, restaurant, and delivery
services, the Saga pattern is recommended. Instead of using distributed
transactions, a saga coordinates a sequence of local transactions. For
example, after payment confirmation, the restaurant accepts the order; if
the restaurant rejects it, a compensating action such as payment refund
is triggered. This pattern ensures data consistency while maintaining
system availability and avoiding blocking issues.
The Asynchronous Messaging pattern using message brokers (such as
queues or streams) is essential for real-time systems. It allows services
to communicate without waiting for immediate responses, improving
responsiveness and fault tolerance. If one service is temporarily
unavailable, messages are queued and processed later, ensuring reliable
communication.
The API Gateway pattern is useful for external communication with
client applications. The gateway provides a single entry point for
mobile or web apps, routes requests to appropriate services, and
aggregates responses. It can also push real-time updates to clients using
WebSockets or server-sent events.
Q.7.a. What is OAuth2.0. When should we choose this protocol?
Ans.7.a.
[10]
Q7
CO-;
SO-;
BL-
[10]
The flow shown in above Figure includes the following steps: 1. The
resource owner (user) provides the client application with it's username
and password. 2. The Client Application requests an access token from
the Authorization Server (Facebook) by passing credentials received
from the resource owner. 3. The Authorization Server(Facebook)
authenticates the client by validating the resource owner credentials.
********** 19 **********
--- page 20 ---
Once Validation is successful and if request is valid, it sends an access
token. 4. Client sends the received access token to Resource Server
(Facebook where) to access the resource end point. 5. Resource Server
validates the access token by calling Authorization Server. 6. If the
token is valid, resource server return the requested resource (e.g.,
profile data) to Client and You see your data in the Client app.
Note: - 1. Authorization Server (e.g., Facebook): Handles user login and
issues access tokens to apps after authentication and authorization. 2.
Resource Server (e.g., Facebook): Stores and provides user data (e.g.,
profile) to apps once a valid token is presented. In short: Authorization
Server grants access; Resource Server delivers the data. 3.
Authorization Code: A temporary code issued by the Authorization
Server after user approval, exchanged by the client for an Access
Token. 4. Access Token: A credential sent to the Resource Server to
access user data, valid for a set time.
Q.7.b. Write steps to migrate Existing monolithic Applications to
Microservices.
(1 step = 1 mark)
Ans.7.b.
1. Assessment and Planning: Evaluate the monolithic application to
understand its architecture, dependencies, and functionalities. Identify the
parts of the application that can be modularized and migrated to
microservices.
2. Define Microservices Boundaries: (Decomposition) Break down the
monolithic application into smaller, loosely coupled services. Define the
boundaries (bounded contexts) of microservices based on business
functionalities. Each microservice should have a well-defined scope and
responsibility. Consider factors such as domain-driven design (DDD)
principles and the single responsibility principle (SRP).
3. Database Decoupling: If the monolithic application shares a database,
consider decoupling the database to enable each microservice to have its own
database or a subset of the original database.
********** 20 **********
--- page 21 ---
4. Identify and Extract Services: Identify modules or functionalities in the
monolithic application that can be extracted into microservices. Start with less
critical or isolated parts of the application to minimize risk. Determine the
dependencies between services and define communication mechanisms (e.g.,
REST, messaging).
5. Refactor and Rewrite: Refactor the extracted modules into microservices,
using modern frameworks and technologies. Rewrite any parts of the
application that are tightly coupled or rely heavily on the monolithic
architecture.
6. Implement API Gateway: Implement an API gateway to manage and route
requests to the appropriate microservices. The API gateway can also handle
authentication, rate limiting, and other cross-cutting concerns.
7. Implement Service Discovery: Use a service discovery mechanism to
enable microservices to locate and communicate with each other dynamically.
8. Containerization: Containerize each microservice using Docker or similar
tools to ensure consistency and portability across different environments.
9. Orchestration: Use a container orchestration tool like Kubernetes to manage
and scale the microservices in a distributed environment.
10. Testing and Deployment: Test each microservice individually to ensure
functionality and compatibility. At a minimum each micorservice should be
independently deployable therefore Implement a continuous integration and
deployment (CI/CD) pipeline to automate the deployment process.
11. Monitoring and Logging: Implement monitoring and logging mechanisms
to track the performance and behavior of microservices in real-time. For
example, you might use Docker and Kubernetes for deployment and Use tools
like Prometheus and Grafana for monitoring.
12. Iterative Approach: Migrate the monolithic application to microservices in
an iterative manner, starting with smaller, less critical parts of the application
and gradually expanding to other areas.
13. Incremental Improvement: Continuously monitor and improve the
performance, scalability, and reliability of the microservices architecture
based on feedback and insights gathered during the migration process.
Migrating from a monolithic architecture to microservices is a complex
process that requires careful planning, execution, and continuous
improvement. It's essential to involve all stakeholders, including developers,
architects, and operations teams, to ensure a smooth and successful transition
********** 21 **********
````

## 2025-26 · Final-Exam · Sem 10 · Answer key · paper b4fab9a64cc6

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_10/Final-Exam/Integrated_Computer_7032/Microservices and Architecture/ANS_Microservices and Architecture(702CO0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 May 2026
- Text: text (21 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III / V/Semester VI/Semester X(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 07 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 21 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   A banking application has a single codebase where UI, business logic,
and database access are tightly coupled. Any minor change requires full
redeployment. Identify the limitations of monolithic architecture in this
scenario and explain how they impact scalability and maintenance.
Ans.1.a.
In this scenario, the banking application follows a monolithic
architecture, where UI, business logic, and database layers are tightly
coupled within a single codebase. This design leads to several
CO- ;   limitations that directly affect scalability and maintenance.
SO- ;   [5]
BL-
Poor Scalability
• The application must be scaled as a whole, not component-wise.
Impact:
•   If only one module (e.g., login system) needs scaling, the entire
system must scale
• Leads to higher infrastructure cost
Difficult Maintenance
• Large codebase becomes complex over time.
********** 1 **********
--- page 2 ---
Impact:
• Hard for new developers to understand
• Debugging becomes time-consuming
•   Increased chances of introducing new errors
b.   When to use what:
i)   RestTemplate:
ii)   WebClient:
iii)   OpenFeign:
Ans.b.
CO- ;   •   RestTemplate: For simple, blocking HTTP calls in non-reactive
SO- ;   [5]
applications (legacy code, small projects). Generally avoid for new
BL-
development.
• WebClient: For modern, high-performance, reactive applications and
microservices.
• OpenFeign: For simplifying communication between microservices by
abstracting away HTTP details. Recommended for most microservice-to-
microservice communication.
c.
Why is testing more complex in microservices compared to monolithic
systems? Explain the role of test automation, service virtualization, and
contract testing in ensuring reliability of microservices.
Testing is More Complex in Microservices because:
1. Distributed Architecture
• Multiple services communicate over networks, so hrd to test
CO- ;   complete workflows end-to-end and Network failures and
SO- ;   latency issues arise.   [5]
BL-
2. Independent Deployments
• Each service can be updated independently so Version
compatibility issues and One service update may break others.
3. Multiple Technologies
•   Different services may use different languages/frameworks so
•   Difficult to maintain consistent testing strategy
4. Data Consistency Issues
********** 2 **********
--- page 3 ---
• Each service has its own database so it is hard to validate
transactions across services.
5. Increased Failure Points
• More services = more chances of failure so Debugging becomes
complex.
Role of Testing Techniques in Ensuring Reliability
1. Test Automation
What it is:
• Runs tests frequently (CI/CD pipelines)
•   Detects bugs early
• Supports regression testing
Benefit:
•   Faster and reliable testing
•   Essential for continuous delivery
2. Service Virtualization
What it is:
Simulating dependent services that are:
• Not available
• Costly
•   Still under development
Role:
• Allows testing of a service in isolation
• Mimics real service behavior
Benefit:
• Reduces dependency on external services
• Enables parallel development and testing
3. Contract Testing
What it is:
Testing the agreement (contract) between services:
• Request format
• Response format
Role:
• Ensures services interact correctly
•   Detects breaking changes early
********** 3 **********
--- page 4 ---
Benefit:
• Prevents integration failures
• Maintains compatibility between services
d.   What are the benefits of implementing a CI/CD pipeline in modern software
development?
Ans.1.d   CI/CD   (Continuous   Integration   and   Continuous
Delivery/Deployment) is a set of practices that automate the process of
building, testing, and deploying software frequently and reliably.
Continuous Integration (CI)
• Developers frequently merge code changes into a shared
repository
• Each change is automatically:
o Built
o Tested
Goal: Detect errors early
Continuous Delivery (CD)
• Code changes are automatically prepared for release
• Deployment is ready but may need manual approval
CO- ;   Continuous Deployment (CD)
SO- ;   • Every validated change is automatically deployed to production [5]
BL-
• No manual intervention required
2. Importance of CI/CD in Microservices
• Supports Independent Deployment Each microservice can be
built and deployed separately.
•   Faster Development and Release Cycle Automation reduces
manual effort. Frequent and quick releases.
3. Improved Code Quality
• Automated testing ensures bugs are caught early .More reliable
and stable services.
4. Scalability of Development Teams
• Multiple teams can work on different services simultaneously
5. Reduced Risk in Deployment
•   Small, incremental changes are easier to test and rollback
********** 4 **********
--- page 5 ---
o
Q.2.a.
a.   Why do we use Configuration Server in microservices architecture.
How does it help in managing dependencies? Explain in detail.
Ans 2.a
A Configuration Server is a centralized service that stores and
provides configuration properties (like database URLs, API keys, ports)
to all microservices.
Key Purposes
1. Centralized Configuration Management
•   All configurations are stored in one place (e.g., Git repository)
Benefit:
• Avoids duplication across services
• Easy to manage and update
2. Externalized Configuration
• Configuration is kept outside the application code
Benefit:
Q2   • No need to rebuild/redeploy services for config changes
[10]
CO-;
SO-;   [10]
3. Environment-Specific Configurations
BL-
• Supports different environments:
o Dev
o Test
o Production
Benefit:
• Same code works in multiple environments with different
configs
4. Dynamic Updates
•   Services can refresh configuration at runtime
Benefit:
• Changes applied without restarting services
2. How it Helps in Managing Dependencies
1. Central Control of Service Dependencies
• Configuration Server stores:
o Database connections
o External service URLs
********** 5 **********
--- page 6 ---
o API endpoints
•   Services don’t hardcode dependencies
• Easy to update when dependencies change
2. Loose Coupling
•   Services depend on configuration, not on fixed values
• Reduces tight coupling between services
• Improves flexibility
3. Easy Version Control
•   Configurations are stored in version control (e.g., Git)
• Track changes in dependencies
• Rollback if needed
4. Consistency Across Services
• Same configuration can be shared by multiple services
• Ensures uniform dependency settings
• Avoids mismatch errors
5. Simplifies Scaling and Deployment
• New services can fetch configuration dynamically
•   Faster onboarding of services
• No manual setup required
Example
Instead of hardcoding:
db.url=localhost:3306
Service fetches from Configuration Server:
db.url=prod-db-server:3306
Q 2.b Write steps to develop and run a “Hello World” application using
b.   Spring Boot.
Ans.2.b.
1. Create a Spring Boot Project
You can use:
• Spring Initializr (web tool)
• IDE like IntelliJ IDEA or Eclipse IDE
Steps:
•   Select:
********** 6 **********
--- page 7 ---
o   Project: Maven / Gradle
o Language: Java
o Dependencies: Spring Web
•   Generate and download project
2. Import Project into IDE
• Open IDE
•   Import the downloaded project as a Maven/Gradle project
3. Create Main Application Class
Spring Boot provides a main class like:
@SpringBootApplication
public class DemoApplication {
public static void main(String[] args) {
SpringApplication.run(DemoApplication.class, args);
}
}
4. Create Controller Class
Create a REST controller:
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
public class HelloController {
@GetMapping("/hello")
public String sayHello() {
return "Hello World";
}
}
5. Run the Application
• Run the main class (DemoApplication)
• Embedded server (Tomcat) starts automatically
6. Test the Application
Open browser or use Postman:
http://localhost:8080/hello
Output:
Hello World
Summary Flow
1. Create project
2. Import into IDE
********** 7 **********
--- page 8 ---
3. Write main class
4. Create controller
5. Run application
6. Test in browser
Q.3.b. Write a note on following?
a.   (i) Ribbon
(ii)Zuul
[10]
Ans Q3.b
b.   (ii)Ribbon:
Ribbon is an Inter-Process Communication (remote procedure calls) library
with a built-in software load balancer (which is mostly used for client-side
load balancing). Primarily it is used for REST calls with various serialization
scheme support.
How Ribbon Works (Step-by-Step)
1. Client makes a service call
The client (e.g., Order Service) wants to call another microservice.
2. Ribbon intercepts the request
Instead of directly calling the service, the request goes to Ribbon.
3. Service instance list is fetched
Ribbon gets available service instances from a service registry (like
Eureka).
4. Load-balancing decision
Ribbon applies a load-balancing algorithm such as:
o Round Robin
Q3   o Random
CO1-;   o Weighted response time
SO2-;   5. Request is sent to one instance
Ribbon forwards the request to the selected service instance.
BLU-
Advantages
• Reduces dependency on external load balancers
•   Faster decision-making (no extra network hop)
•   Better fault tolerance
(i)Zuul is an API Gateway developed by Netflix used in microservices
architecture to handle all incoming requests and route them to appropriate
services.
Key Functions
•   Routing: Directs client requests to specific microservices
•   Filtering: Performs pre and post processing (authentication, logging)
• Load Balancing: Distributes requests across instances
[10]
•   Security: Acts as a single entry point for enforcing security policies
Types of Filters
•   Pre-filters: Before request reaches service
•   Post-filters: After response is generated
********** 8 **********
--- page 9 ---
•   Route-filters: Handle routing
•   Error-filters: Handle failures
Advantages
•   Centralized control
• Improved security
•   Simplifies client interaction
• Reduces complexity of microservices communication
Q.3.a Why do we need the service discovering and registering process?
Explain with neat architecture diagram.
Ans 3.a. In a microservices architecture, services are:
• Deployed independently
• Scaled up/down dynamically
• Running on dynamic IP addresses and ports
Because of this, hardcoding service URLs is not feasible.
Service discovery and registration solve this problem by enabling
services to find and communicate with each other dynamically.
Eureka Architecture:
1.Service Registry (The Eureka Server):
The Eureka Server acts as a centralized "phonebook" for
microservices. It runs as a standalone application (typically on a
default port like 8761).
Microservices (called "clients") register themselves with the Eureka
Server when they start up, providing details like their hostname, IP
address, port, and a unique service ID.
2. Client Registration:
********** 9 **********

[Text in pictures on this page, read by OCR]
111.22.33.44:9090

| Request
111.22.33.44,8098 .
ENON Service B
Load 100.2.3.4:8090
Balancer :
Service B
[Resisters
333,111.33.1:8081
ee Instance List Query Service B
magaesaae° Disco
Service-B iscovery |.—_
ti22ssexs080)*#——F Service 111.22.33:8080

Service -A | 111:22:33:44:8098 Service B
--- page 10 ---
Each microservice includes a Eureka Client library (e.g., in Spring
Boot, via the spring-cloud-starter-netflix-eureka-client dependency).
When a service boots up, it sends a registration request to the
Eureka Server with its metadata. For example: "I’m Service A,
running at IP 192.168.1.10, port 8080."
The server stores this info in a registry—a dynamic list of all active
services.
3.Heartbeat and Health Checks:
Registered services send periodic "heartbeats" (typically every 30
seconds) to the Eureka Server to say, "I’m still alive!"
If a service stops sending heartbeats (e.g., it crashes), the Eureka
Server removes it from the registry after a timeout period. This
keeps the registry up-to-date.
4.Service Discovery:
When a microservice (e.g., Service B) needs to talk to another
service (e.g., Service A), it doesn’t hardcode the target’s address.
Instead, it asks the Eureka Server: "Where’s Service A?"
The Eureka Client in Service B fetches the current list of Service A
instances from the server (this list is cached locally and refreshed
periodically). Service B then picks an instance (often using a load
balancer like Netflix Ribbon).
[10]
a.   Q.4.a What challenges arise in ensuring security and service communication
throughout the microservices lifecycle?.
Ans.4.a.
Increased Attack Surface
Q4
Challenge:
CO-;
SO-;   • Each microservice exposes APIs, increasing the number of
BL-   attack entry points.
• Network-based communication makes services vulnerable to
external threats.
Solution:
• Use an API Gateway to act as a single entry point.
********** 10 **********
--- page 11 ---
• Apply centralized security controls such as authentication,
authorization, and rate limiting.
2️. Service-to-Service Authentication
Challenge:
• Ensuring that only authorized services communicate is difficult.
• Manual management of credentials does not scale in large
systems.
Solution:
• Implement OAuth 2.0, JWT, or mutual TLS (mTLS) for secure
service identity.
• Use role-based or policy-based access control for authorization.
3️ Secure Data Transmission
Challenge:
• Data exchanged between services may be intercepted.
• Lack of encryption can lead to data breaches.
Solution:
• Encrypt all inter-service communication using HTTPS/TLS.
• Use service mesh technologies to automatically enforce
encryption policies.
4️ API Versioning and Compatibility
Challenge:
• Multiple service versions may exist during upgrades.
• Breaking changes can disrupt dependent services.
Solution:
• Use proper API versioning strategies (URI-based, header-based).
• Ensure backward compatibility and gradual version deprecation.
5️. Policy Enforcement Across the Microservices Lifecycle
Challenge:
• Maintaining consistent security policies across development,
testing, and production is complex.
Solution:
•   Integrate automated security checks into the CI/CD pipeline.
********** 11 **********
--- page 12 ---
• Use static code analysis, dependency scanning, and security
testing tools.
4.b. Design and explain REST APIs for a student management system using
operations:
•   Create Employee
• Get Employee
[10]
•   Delete Employee
Specify endpoints, HTTP methods, and sample request/response structures.
Ans.4.b.
Base URL
https://api.university.com/employee
1. Create Employee
Endpoint
POST /employee
Creates a new employee record in the system.
Sample Request (JSON)
{
"employeeId": "S101",
"name": "Amit Sharma",
"age": 20,
"department": "Computer Science",
"email": "amit.sharma@univ.edu"
}
Sample Response (201 Created)
{
"message": "Employee created successfully",
"studentId": "S101"
}
2. Get Employee
Endpoint
GET /employees/{employeeId}
********** 12 **********
--- page 13 ---
Retrieves details of a specific student using the student ID.
Sample Request
GET /employees/S101
Sample Response (200 OK)
{
"employeeId": "S101",
"name": "Amit Sharma",
"age": 20,
"department": "Computer Science",
"email": "amit.sharma@univ.edu"
}
3. Delete Employee
Endpoint
DELETE /employees/{employeeId}
Deletes an employee record from the system.
Sample Request
DELETE /employees/S101
Sample Response (200 OK)
{
"message": "Employee deleted successfully"
}
[10]
What is topic in Kafka. Explain Kafka architecture with a suitable use case.
a.
b.
Kafka Topic
Q5
CO-;
SO-;
BL-
• A logical channel for messages.
• Comparable to a table in a database or a folder in a file system.
•   Identified by a unique name.
• You can have any number of topics.
•   Producers send data to topics; consumers subscribe to topics.
•   Internally, topics are divided into partitions.
•   Topics help in organizing data streams.
********** 13 **********
--- page 14 ---
• Data can be retained even after consumption depending on the
retention policy.
Kafka Workflow (Basic Flow)
1. Producer sends messages to a topic.
2. Kafka stores messages in partitions.
3. Consumer reads messages using offsets.
4. Kafka retains messages for a configured time (default 7 days).
Kafka Use Cases
•   Real-time analytics
• Logging and monitoring
•   Event sourcing
• Messaging system
• Stream processing
Features of Kafka
1. Publish-Subscribe System
o Producers send messages.
o Consumers receive messages from topics.
Apache Kafka Architecture :
1. Kafka Producer
• Sends messages to Kafka topics.
• Can choose the partition or let Kafka decide.
• Sends key-value pairs.
•   Writes are asynchronous and allow high throughput.
********** 14 **********

[Text in pictures on this page, read by OCR]
Kafka Cluster with group of brokers

Broker 1

Topics

& Partitions Pull messagt
=f a a
altri ts]

Messages get stored in partitions using offset ids

Push messages

4
papxa}

Broker 2 Pull message

Broker 3
--- page 15 ---
• Does not directly communicate with the consumer.
•   Acts as the entry point for data into the Kafka system.
2. Kafka Cluster
• A Kafka cluster consists of multiple brokers (minimum 3
recommended).
•   Enables scalability, fault tolerance, and replication.
• Can handle failover and load balancing.
•   Partitions are spread across the brokers in the cluster.
3. Kafka Broker
• A Kafka cluster is made of multiple brokers.
• A Kafka broker is a Kafka server.
•   It stores data (partitions) and handles client requests
(producers/consumers).
• Each broker has a unique ID.
• Kafka topics are divided into partitions, stored across brokers.
•   Brokers are distributed and horizontally scalable (just add more to
scale ie increase load handling).
•   Brokers do not share partitions – each partition belongs to one
leader broker at a time.
Kafka brokers store data durably on disk and support replication.
4. Kafka Partitions
• A single topic can have multiple partitions.
•   Partitions allow parallelism and scalability.
• Each partition is ordered, and messages are stored sequentially.
• A partition belongs to only one broker (leader) at a time.
More partitions = More parallelism, but also more complexity
[Use case can be to explain with e-commerce site example]
Q.5.b. Why the distributed transactions should be avoided with the use of two-
phase commit protocol? How the identified issues can be solved?
Ans.5.b. Distributed transactions using the Two-Phase Commit (2PC)
protocol are generally avoided in microservices and distributed systems
because they introduce several serious drawbacks related to
performance, scalability, and availability. Although 2PC guarantees
********** 15 **********
--- page 16 ---
atomicity across multiple services, it contradicts the core principles of
microservices such as loose coupling and independent service
operation.
One major reason for avoiding 2PC is its blocking nature. In the 2PC
protocol, if the coordinator fails after participants have agreed to
commit but before the final decision is communicated, all participating
services remain blocked while holding locks on resources. This can lead
to resource starvation and system unavailability. Additionally, 2PC
significantly reduces scalability because each service must lock its
resources until the global transaction completes, limiting throughput as
the number of services grows.
Another critical issue is reduced availability. The failure of even a
single participant or the coordinator can cause the entire transaction to
fail or hang indefinitely. This tightly couples the availability of all
participating services, which is undesirable in distributed environments.
Furthermore, 2PC incurs high performance overhead due to multiple
network round trips and coordination messages, increasing latency and
reducing system responsiveness.
To solve these issues, modern distributed systems prefer eventual
consistency–based approaches. The most widely adopted solution is
the Saga pattern, where a distributed transaction is broken into a
sequence of local transactions managed by individual services. Each
service completes its transaction independently and publishes an event.
If a failure occurs, compensating transactions are executed to undo
previous actions, eliminating the need for global locks and blocking.
Sagas can be implemented using choreography (event-driven) or
orchestration (central controller).
Another solution is adopting eventual consistency, where temporary
inconsistencies are allowed but the system eventually reaches a
consistent state. This approach improves availability and fault tolerance.
[10]
“Service-to-service communication is managed through an intermediate
a.
infrastructure layer.” What is this layer? Explain with architecture diagram.
Ans.6.a
Q6   A Service Mesh is an architectural layer used in microservices
architecture to manage service-to-service communication in a
CO-;
reliable, secure, and observable manner. Instead of embedding
SO-;
communication logic inside application code, a service mesh offloads
BL-
these concerns to a dedicated infrastructure layer, allowing developers
to focus only on business logic.
In a service mesh, every microservice instance is paired with a
lightweight network proxy, and all service-to-service communication
passes through these proxies. This approach provides consistent
********** 16 **********
--- page 17 ---
handling of cross-cutting concerns such as traffic management, security,
observability, and resilience.
Service Mesh :
At a high level, a service mesh consists of two planes:
• Data Plane
• Control Plane
The application services do not communicate directly with each other.
Instead, communication flows through sidecar proxies that form the
data plane, while the control plane manages and configures these
proxies.
Key Components of Service Mesh
1. Data Plane (Sidecar Proxies)
The data plane consists of lightweight proxies (often deployed as
sidecars) that run alongside each microservice. These proxies intercept
all inbound and outbound traffic between services. They handle tasks
such as load balancing, service discovery, retries, timeouts, circuit
breaking, encryption, and telemetry collection. Since the proxy is
independent of application code, communication policies can be
changed without redeploying services.
2. Control Plane
The control plane manages and configures the data plane proxies. It
defines traffic policies, security rules, and routing behavior and then
pushes these configurations dynamically to the proxies. The control
plane does not handle application traffic directly; instead, it acts as the
brain of the service mesh.
3. Traffic Management Component
This component controls how requests are routed between services. It
supports features such as intelligent load balancing, canary
deployments, blue-green deployments, traffic splitting, retries, and fault
injection. Traffic management helps improve reliability and enables
safe deployment strategies.
4. Security Component
The security layer of a service mesh provides mutual TLS (mTLS) for
service-to-service authentication and encryption. It also supports
authorization policies, certificate management, and identity verification.
This ensures zero-trust communication within the microservices
environment.
5. Observability Component
Service mesh provides deep observability into service interactions. It
collects metrics, logs, and distributed traces automatically without
requiring changes in application code. This helps in monitoring latency,
error rates, service dependencies, and overall system health.
********** 17 **********
--- page 18 ---
6. Policy and Configuration Management
This component allows administrators to define and enforce policies
such as rate limiting, access control, quotas, and retry rules centrally.
Policies are consistently applied across all services through the data
plane proxies.
[10]
b.
Q.6.b. A food delivery platform integrates restaurant, delivery, and payment
services. Real-time updates are required. Identify suitable integration patterns
and justify their use.
Ans.6.b.
The Event-Driven Architecture (EDA) pattern is highly suitable for
this scenario. In this pattern, services communicate by producing and
consuming events rather than direct synchronous calls. For example,
when an order is placed, the restaurant service publishes an
OrderPlaced event, which is consumed by the delivery and payment
services. This enables real-time updates such as order confirmation,
preparation status, and delivery tracking. Event-driven integration
ensures low latency, high scalability, and loose coupling between
services.
The Publish–Subscribe (Pub/Sub) pattern is another appropriate
integration pattern. In this pattern, the restaurant service publishes
events (e.g., FoodPrepared), and multiple subscribers such as the
delivery service, notification service, and user interface can receive
these updates simultaneously. This is ideal for real-time notifications
like “order accepted,” “out for delivery,” and “delivered,” without the
publisher needing to know who the consumers are.
********** 18 **********

[Text in pictures on this page, read by OCR]
Peta... nonnnne ny nnn
Microservice - P
Business
awe Service Mesh
Network
Functions Ieee. h

Application Network

Functions Data Plane
--- page 19 ---
For managing transactions across payment, restaurant, and delivery
services, the Saga pattern is recommended. Instead of using distributed
transactions, a saga coordinates a sequence of local transactions. For
example, after payment confirmation, the restaurant accepts the order; if
the restaurant rejects it, a compensating action such as payment refund
is triggered. This pattern ensures data consistency while maintaining
system availability and avoiding blocking issues.
The Asynchronous Messaging pattern using message brokers (such as
queues or streams) is essential for real-time systems. It allows services
to communicate without waiting for immediate responses, improving
responsiveness and fault tolerance. If one service is temporarily
unavailable, messages are queued and processed later, ensuring reliable
communication.
The API Gateway pattern is useful for external communication with
client applications. The gateway provides a single entry point for
mobile or web apps, routes requests to appropriate services, and
aggregates responses. It can also push real-time updates to clients using
WebSockets or server-sent events.
Q.7.a. What is OAuth2.0. When should we choose this protocol?
Ans.7.a.
[10]
Q7
CO-;
SO-;
BL-
[10]
The flow shown in above Figure includes the following steps: 1. The
resource owner (user) provides the client application with it's username
and password. 2. The Client Application requests an access token from
the Authorization Server (Facebook) by passing credentials received
from the resource owner. 3. The Authorization Server(Facebook)
authenticates the client by validating the resource owner credentials.
********** 19 **********
--- page 20 ---
Once Validation is successful and if request is valid, it sends an access
token. 4. Client sends the received access token to Resource Server
(Facebook where) to access the resource end point. 5. Resource Server
validates the access token by calling Authorization Server. 6. If the
token is valid, resource server return the requested resource (e.g.,
profile data) to Client and You see your data in the Client app.
Note: - 1. Authorization Server (e.g., Facebook): Handles user login and
issues access tokens to apps after authentication and authorization. 2.
Resource Server (e.g., Facebook): Stores and provides user data (e.g.,
profile) to apps once a valid token is presented. In short: Authorization
Server grants access; Resource Server delivers the data. 3.
Authorization Code: A temporary code issued by the Authorization
Server after user approval, exchanged by the client for an Access
Token. 4. Access Token: A credential sent to the Resource Server to
access user data, valid for a set time.
Q.7.b. Write steps to migrate Existing monolithic Applications to
Microservices.
(1 step = 1 mark)
Ans.7.b.
1. Assessment and Planning: Evaluate the monolithic application to
understand its architecture, dependencies, and functionalities. Identify the
parts of the application that can be modularized and migrated to
microservices.
2. Define Microservices Boundaries: (Decomposition) Break down the
monolithic application into smaller, loosely coupled services. Define the
boundaries (bounded contexts) of microservices based on business
functionalities. Each microservice should have a well-defined scope and
responsibility. Consider factors such as domain-driven design (DDD)
principles and the single responsibility principle (SRP).
3. Database Decoupling: If the monolithic application shares a database,
consider decoupling the database to enable each microservice to have its own
database or a subset of the original database.
********** 20 **********
--- page 21 ---
4. Identify and Extract Services: Identify modules or functionalities in the
monolithic application that can be extracted into microservices. Start with less
critical or isolated parts of the application to minimize risk. Determine the
dependencies between services and define communication mechanisms (e.g.,
REST, messaging).
5. Refactor and Rewrite: Refactor the extracted modules into microservices,
using modern frameworks and technologies. Rewrite any parts of the
application that are tightly coupled or rely heavily on the monolithic
architecture.
6. Implement API Gateway: Implement an API gateway to manage and route
requests to the appropriate microservices. The API gateway can also handle
authentication, rate limiting, and other cross-cutting concerns.
7. Implement Service Discovery: Use a service discovery mechanism to
enable microservices to locate and communicate with each other dynamically.
8. Containerization: Containerize each microservice using Docker or similar
tools to ensure consistency and portability across different environments.
9. Orchestration: Use a container orchestration tool like Kubernetes to manage
and scale the microservices in a distributed environment.
10. Testing and Deployment: Test each microservice individually to ensure
functionality and compatibility. At a minimum each micorservice should be
independently deployable therefore Implement a continuous integration and
deployment (CI/CD) pipeline to automate the deployment process.
11. Monitoring and Logging: Implement monitoring and logging mechanisms
to track the performance and behavior of microservices in real-time. For
example, you might use Docker and Kubernetes for deployment and Use tools
like Prometheus and Grafana for monitoring.
12. Iterative Approach: Migrate the monolithic application to microservices in
an iterative manner, starting with smaller, less critical parts of the application
and gradually expanding to other areas.
13. Incremental Improvement: Continuously monitor and improve the
performance, scalability, and reliability of the microservices architecture
based on feedback and insights gathered during the migration process.
Migrating from a monolithic architecture to microservices is a complex
process that requires careful planning, execution, and continuous
improvement. It's essential to involve all stakeholders, including developers,
architects, and operations teams, to ensure a smooth and successful transition
********** 21 **********
````

## 2025-26 · Re-Exam · Sem 3 · Answer key · paper bb9918c33298

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_03/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Microservices and Architecture/ANS_Microservices and Architecture(703CO0C026)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 31 Jan 2026
- Text: mixed (9 pages), mean OCR confidence 34.6
- **Low OCR quality**: most likely handwritten or a poor scan, so the text below is only partly readable. Restore the original file to read it.

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: II/Sem 3 Re-exam(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 31 Jan 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Question No. 1 is compulsory.
3. Out of remaining questions, attempt any 4 questions
4. In all 5 questions to be attempted.
5. All questions carry equal marks
6. Figures in brackets on the right hand side indicate full marks
7. Answer to each new question to be started on a fresh page.
Q.1 Answer briefly:   2
0
a) What is the role of Eureka Server and Eureka Client in a Microservice architecture   5
• Eureka Server: Service registry that tracks available microservices for discovery.
• Eureka Client: Registers with the Eureka Server and discovers other services
dynamically.
• Example:
• Eureka Server runs at http://localhost:8761.
• Microservice 1 & 2 register as clients:
spring.application.name=ms1
eureka.client.service-url.defaultZone=http://localhost:8761/eureka/
•   Clients use Eureka to locate other services without hardcoding URLs.
b) Compare between Monolithic and Microservice architecture   5
Feature   Monolithic   Microservices
Structure   Single application   Independent services per module
Deployment   Single unit   Multiple deployable units
Scalability   Entire app scales   Service-level scaling
Technology Stack One tech stack   Polyglot possible
Fault Isolation   Failure affects entire app Failure isolated to one service
Development   Easier initially   Complex but modular
c)   5
Explain Saga Pattern in detail.
********** 1 **********
--- page 2 ---
• Definition: Saga is a pattern for managing distributed transactions in microservices
without locking resources.
• Two types:
1. Choreography → Each service triggers the next; compensating actions for failures.
2. Orchestration → Central orchestrator coordinates transaction steps and handles
failures.
• Benefits:
• Avoids 2PC complexity, better availability.
• Example: Ordering system:
•   Service A (Order) → Service B (Payment) → Service C (Inventory).
•   If Payment fails, compensating action: cancel order.
d) Write a note on CI/CD pipeline   5
• CI (Continuous Integration): Automates code integration into a shared repository.
Each commit triggers build & automated tests.
• CD (Continuous Delivery/Deployment): Automatically deploys code to
testing/staging (Delivery) or directly to production (Deployment).
•   Stages:
o Code Commit → Git/GitHub.
o Build → Maven/Gradle.
o Automated Testing → Unit & Integration tests.
o Deploy → Dev/Staging/Production via Jenkins/GitLab CI.
o Monitoring & Rollback → Prometheus/Grafana, ability to revert.
Q.   You are developing a Spring Boot application for a company to manage Employee records 1
2(a   using MySQL in a structured, layered architecture.   0
)   Answer the following:
1. Create an Employee entity class with fields — id, name, and salary.
2. Define a JPA Repository interface for performing database operations.
3. Implement a Service Layer to handle business logic for CRUD operations.
4. Develop a REST Controller exposing endpoints to Create, Retrieve, Update,
Delete, and List all employees.
5. Configure MySQL connection settings in the application.properties file.
1. Employee Entity
import jakarta.persistence.*;
@Entity
public class Employee {
@Id @GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
private String name;
private double salary;
// getters & setters
********** 2 **********
--- page 3 ---
}
2. JPA Repository
import org.springframework.data.jpa.repository.JpaRepository;
public interface EmployeeRepository extends JpaRepository<Employee, Long>
{}
3. Service Layer
import org.springframework.stereotype.Service;
import java.util.List;
@Service
public class EmployeeService {
private final EmployeeRepository repo;
public EmployeeService(EmployeeRepository repo){ this.repo = repo; }
public Employee save(Employee e){ return repo.save(e); }
public List<Employee> getAll(){ return repo.findAll(); }
public Employee getById(Long id){ return
repo.findById(id).orElse(null); }
public void delete(Long id){ repo.deleteById(id); }
}
4. REST Controller
import org.springframework.web.bind.annotation.*;
import java.util.List;
@RestController
@RequestMapping("/employees")
public class EmployeeController {
private final EmployeeService service;
public EmployeeController(EmployeeService service){ this.service =
service; }
@PostMapping public Employee create(@RequestBody Employee e){ return
service.save(e); }
@GetMapping public List<Employee> getAll(){ return service.getAll();
}
@GetMapping("/{id}") public Employee getById(@PathVariable Long id){
return service.getById(id); }
@PutMapping("/{id}") public Employee update(@PathVariable Long id,
@RequestBody Employee e){
e.setId(id); return service.save(e); }
@DeleteMapping("/{id}") public void delete(@PathVariable Long id){
service.delete(id); }
}
5. MySQL Configuration
spring.datasource.url=jdbc:mysql://localhost:3306/companydb
spring.datasource.username=root
spring.datasource.password=root
spring.jpa.hibernate.ddl-auto=update
Q. How can you implement In-Memory Basic Authentication in Spring Boot?In your answer,   1
2(b   include:   0
)
1. Writing a Security Configuration Class for In-Memory Authentication
********** 3 **********
--- page 4 ---
2. Creating a Controller to Test Authentication
3. Defining User Roles and Authorities in the Security Configuration
4. Adding Required Dependencies in pom.xml (if using Spring Security Starter)
. Security Configuration
import org.springframework.context.annotation.*;
import
org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.core.userdetails.User;
import
org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;
@Configuration
public class SecurityConfig {
@Bean
public InMemoryUserDetailsManager userDetailsService() {
var user1 =
User.withUsername("admin").password("{noop}admin123").roles("ADMIN").buil
d();
var user2 =
User.withUsername("user").password("{noop}user123").roles("USER").build()
;
return new InMemoryUserDetailsManager(user1, user2);
}
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws
Exception {
http.authorizeHttpRequests().anyRequest().authenticated()
.and().httpBasic();
return http.build();
}
}
2. Test Controller
@RestController
public class TestController {
@GetMapping("/welcome")
public String welcome(){ return "Welcome!"; }
}
3. Dependencies (pom.xml)
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-security</artifactId>
</dependency>
Q.   What is the role of an API Gateway in microservices?   1
3(a   Explain with example how two microservices (ms1 and ms2) can be registered with Eureka   0
)   Server and accessed via API Gateway, including configuration details from
application.properties.
Steps:
********** 4 **********
--- page 5 ---
1. Register microservices (ms1 and ms2) with Eureka:
spring.application.name=ms1
eureka.client.service-url.defaultZone=http://localhost:8761/eureka/
2. API Gateway routes requests:
spring.application.name=api-gateway
server.port=8080
eureka.client.service-url.defaultZone=http://localhost:8761/eureka/
• Example: /ms1/** → forwarded to ms1, /ms2/** → forwarded to ms2.
Benefits: Centralized routing, security, monitoring, throttling.
Q.   Write down the step to implement a Spring Cloud Config Server and Client with a Refresh   1
3(b   Feature?   0
)
Config Server application.properties
server.port=8888
spring.cloud.config.server.git.uri=https://github.com/user/config-repo
Config Client application.properties
spring.application.name=config-client
spring.cloud.config.uri=http://localhost:8888
management.endpoints.web.exposure.include=*
Controller with Refresh
@RestController
@RefreshScope
public class ConfigController {
@Value("${some.config}") private String configValue;
@GetMapping("/config") public String getConfig(){ return configValue;
}
}
Q.   Describe and draw the core components and working of Kubernetes Architecture.   1
4(a Core Components:   0
)
• Master Node: API Server, Scheduler, Controller Manager, etcd
• Worker Node: Kubelet, Kube-proxy, Container Runtime (Docker)
• Pods: Smallest deployable units containing containers
•   Service: Exposes pods internally or externally
Working:
1. User submits deployment via kubectl.
2. Master schedules pods to nodes.
********** 5 **********
--- page 6 ---
3. Kubelet ensures pods are running.
4. Service provides network access.
(Diagram: Master Node → Worker Node → Pods → Containers)
Q.   Design pattern in Spring Microservices with diagram.   1
4(b   0
)
Example: Circuit Breaker Pattern
• Purpose: Prevent cascading failures between services.
• Components:
1. Client calls Service A.
2. Circuit Breaker monitors responses.
3. On repeated failure, trips and returns fallback response.
(Diagram: Client → Circuit Breaker → Service → Fallback)
Q.   Explain the Docker Architecture? Create a docker-compose.yml file to run a Spring Boot   1
5(a   application with a MySQL database   0
)   Docker Architecture:
• Docker Client → CLI/GUI to interact with Docker Engine
• Docker Engine → Builds & runs containers
• Images → Read-only templates
• Containers → Running instances
docker-compose.yml
version: '3.8'
services:
app:
image: springboot-app
build: .
ports: ["8080:8080"]
environment:
- SPRING_DATASOURCE_URL=jdbc:mysql://db:3306/companydb
- SPRING_DATASOURCE_USERNAME=root
********** 6 **********

[Text in pictures on this page, read by OCR]
Integration Database
Patterns Patterns Patterns

Decompose by
Business
Capability

API Gateway Database per Extemal
Pattern Service Configuration

Decompose by Aggregator Shared Database Performance IMM Service Discovery
Subdomain Pattern per Service Metrics Pattern

Distributed Circuit Breaker
Tracing Pattern

Decompose by

BS proxy Pattern
Transactions J

Blue-Green
Event Sourcing Health Check Deployment
Pattern

Gateway Routing

trangler Pattern nasil

Chained
fee Bulkhead Pattern Microservice Saga Pattern
Pattern

ISS Sidecar Pattern JN Branch Pattern

Client-Side UI
Composition

Pattern
--- page 7 ---
- SPRING_DATASOURCE_PASSWORD=root
depends_on:
- db
db:
image: mysql:8
environment:
MYSQL_ROOT_PASSWORD: root
MYSQL_DATABASE: companydb
ports: ["3306:3306"]
Q.   What are the two ways of Microservice communication?Provide the complete code to   1
5(b   0
implement the communication using Open Feign and RestClient
)
1. OpenFeign Example
@FeignClient(name="ms2", url="http://localhost:8082")
public interface MS2Client {
@GetMapping("/data")
String getData();
}
2. RestTemplate Example
@Autowired private RestTemplate restTemplate;
String data = restTemplate.getForObject("http://localhost:8082/data",
String.class);
Q.   Draw and Explain the architecture of Apache Kafka with the help of a simple diagram, describing 1
6(a   the roles of Producer, Topic, Partition, Broker, and Consumer.   0
)
Components:
• Producer → Sends messages
• Topic → Logical channel for messages
•   Partition → Divides topic for parallelism
• Broker → Kafka server storing messages
• Consumer → Reads messages
********** 7 **********
--- page 8 ---
(Diagram: Producer → Topic → Partition → Broker → Consumer)
Q.   Explain Mike Cohn's original test pyramid with diagram? Types of Testing in Spring boot   1
6(b   Microservices   0
)   Layers:
1. Unit Tests (base, most tests)
2. Service/Integration Tests (middle)
3. UI/End-to-End Tests (top, fewer tests)
Types of Testing in Spring Boot Microservices:
• Unit Tests → Mockito, JUnit
• Integration Tests → SpringBootTest
• Contract Tests → Pact/REST Assured
• E2E Tests → Selenium, Postman
(Diagram: Pyramid with Unit at bottom → Integration → E2E at top)
Q.   Write a Spring Boot program using Actuator to display application health. Extend it by   1
7(a   adding a custom Health Indicator that checks a custom service or condition.   0
)   @SpringBootApplication
public class ActuatorApp {}
java
Copy code
@Component
public class CustomHealthIndicator implements HealthIndicator {
@Override
public Health health() {
boolean serviceUp = checkService();
return serviceUp ? Health.up().withDetail("Service", "Running").build()
: Health.down().withDetail("Service", "Down").build();
}
private boolean checkService(){ return true; }
}
Access: http://localhost:8080/actuator/health
Q.   What is a distributed transaction? Explain Two-phase commit (2pc) pattern. what are the   1
7(b   benefits disadvantages of using 2pc?   0
)
Distributed Transaction: Transaction spanning multiple databases/microservices.
2PC Steps:
1. Prepare Phase → Coordinator asks all participants to prepare and vote.
2. Commit Phase → If all agree, commit; else rollback.
Benefits:Ensures ACID consistency across services.
Disadvantages:
• Blocking protocol → can lock resources.
•   Single point of failure (coordinator).
• Slower compared to Saga or eventual consistency.
********** 8 **********
--- page 9 ---
FIC QF OH ar
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 6920bcf389ee

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_Computer_7002/Microservices and Architecture/ANS_Microservices and Architecture(702CO0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   A startup initially developed its e-commerce application as a monolithic
system. As the number of users increased from 10,000 to 1 million,
deployment failures and downtime became frequent. Analyze the situation
and justify whether migrating to Microservices would solve these issues.
Explain with architectural reasoning.
Ans.1.a. As the startup’s user base grew from 10,000 to 1 million, the
limitations of its monolithic architecture became more visible, leading to
frequent deployment failures and downtime. In a monolithic system, all
CO- ;
SO- ;   application modules such as user management, product catalog, orders,   [5]
BL-   payments, and notifications are tightly coupled and deployed as a single unit.
Any small change, bug fix, or enhancement in one module requires
rebuilding, testing, and redeploying the entire application. With a large user
base and increasing traffic, this results in long deployment times, higher risk
of failure, and complete application downtime even for minor issues.
Scalability is also limited because the entire application must be scaled
together, even if only one component (for example, payment or search)
experiences high load, leading to inefficient resource utilization and
performance bottlenecks.
********** 1 **********
--- page 2 ---
Migrating to a microservices architecture can significantly reduce
these issues if designed and implemented correctly. In microservices,
the application is decomposed into smaller, independent services, each
responsible for a specific business capability and typically owning its
own database. From an architectural perspective, this enables
independent deployment, meaning a failure or update in one service
does not bring down the entire system. For example, updating the
recommendation service will not affect order processing or user
authentication. This directly addresses the deployment failures and
downtime experienced in the monolithic setup. Microservices also
support horizontal scalability, allowing only the heavily used services,
such as product search or checkout, to be scaled independently, which
is critical when handling millions of users.
Additionally, microservices improve system resilience through fault
isolation. If one service fails, circuit breakers and retries can prevent
cascading failures, ensuring partial functionality rather than total
downtime. Continuous deployment pipelines become safer and faster
because services are smaller and easier to test. Architecturally,
microservices align well with cloud-native practices, containerization,
and orchestration platforms, enabling rolling updates and zero-
downtime deployments.
b.   Write a note on the following design principles for developing the micro-
services?
(i) Loose Coupling
(ii) Resiliency
Ans.1.b.
CO- ;
SO- ;   (i)   Loose Coupling: -
Coupling is a measure of the interdependence between micro [5]
BL-
services. When there is a high interdependency between micro
services, this will result in a tightly coupled system, while a low
interdependency will produce a loosely coupled system. Tightly
coupled systems build a brittle system architecture. A change done
in one system will affect all the related systems. If one system goes
down, all the related systems will be dysfunctional. A micro
services architecture must be highly cohesive and loosely coupled.
********** 2 **********
--- page 3 ---
(ii)   Resiliency: - Resilience is a measure of the capacity of a system or
individual components in a system to recover quickly from a failure.
In other words, it is an attribute of a system that enables it to deal
with failure in a way that doesn’t cause the entire system to fail.
There are various ways to achieve resilience - time out, circuit
breaker, fail fast etc.
c.   Explain the Component and integration testing?
: Component Testing: It focuses on testing the interaction and integration
between multiple micro services or components within a system. Component
testing assesses the behaviour of a set of interconnected services or components
that work together to accomplish a specific task or functionality.
• These components may include micro services, modules, or other units of
the application architecture.
•   Unlike unit testing, component testing may involve real-world interactions
with external dependencies, such as databases, APIs, or other services.
Benefits of Component Testing
• Component testing validates the integration and communication between
micro services, uncovering issues related to service dependencies and data
flow.
Challenges of Component Testing
•   Coordinating and orchestrating component tests across multiple services
CO- ;   can be challenging. Ensuring consistent test environments and managing
test data can also be complex.   [5]
SO- ;
BL-   Integration testing- It verifies the interaction between different services or
components to ensure they work together correctly. Unlike unit testing,
which focuses on testing individual units in isolation, integration testing
evaluates how these units interact and communicate with each other.
•   Integration testing validates the interaction and communication between
different services or components to ensure they exchange data and
collaborate effectively.
•   Integration testing often involves end-to-end testing scenarios that span
multiple services or components, simulating real-world user interactions
and workflows.
Benefits of Integration Testing
•   Integration testing helps ensure data consistency across multiple services or
components.
Challenges of Integration Testing
•   Setting up and maintaining integration test environments that accurately
reflect the production environment can be difficult.
CO- ;   d.
1. What is Docker? Explain Docker image and container.
SO- ;
[5]
BL-
What is inter-service communication? Mention synchronous and   [10]
Q2   a.   asynchronous methods.
CO-; SO-;
BL-
Ans.2.a.   [10]
********** 3 **********
--- page 4 ---
Inter-service communication is the mechanism by which independent
services in a distributed or microservices-based architecture exchange
b.   data and coordinate actions to fulfill business functionality. Since each
service runs in its own process and often on different machines,
communication over a network is required to share requests, responses,
or events.
Synchronous communication is request–response based, where the
calling service waits for an immediate reply from the called service.
Common synchronous methods include RESTful APIs over
HTTP/HTTPS, gRPC (remote procedure calls using HTTP/2 and
Protocol Buffers), and GraphQL. While synchronous communication is
simple to implement and suitable for real-time operations, it increases
coupling between services and can lead to higher latency and cascading
failures if a dependent service is slow or unavailable.
Asynchronous communication is event-driven or message-based,
where the calling service sends a message and continues processing
without waiting for an immediate response. Common asynchronous
methods include message queues and event streaming platforms such as
Apache Kafka, RabbitMQ, and cloud-based messaging services, as well
as publish–subscribe patterns. Asynchronous communication improves
scalability, fault tolerance, and loose coupling, making it well-suited for
high-traffic and resilient microservices systems.
Q.2.b A team wants to quickly create a REST microservice without manual
configuration. Explain how Spring Boot dependencies and auto-configuration
help achieve this. Illustrate using a simple Hello World service flow.
Spring Boot allows a team to quickly create a REST microservice
without manual configuration by using starter dependencies and auto-
configuration, and this process can be clearly understood through the
programming steps of a simple Hello World service. First, the developer
creates a Spring Boot project using Spring Initializr or an IDE and
selects the dependency spring-boot-starter-web. This single starter
internally brings in all required libraries such as Spring MVC, an
embedded Tomcat server, Jackson for JSON processing, and validation
support, so no explicit dependency management or server setup is
required.
The next programming step is to define the main application class. This
class is annotated with @SpringBootApplication, which is a
combination of @Configuration, @EnableAutoConfiguration, and
@ComponentScan. When the application starts, Spring Boot
automatically scans the classpath, detects the web dependency, and
configures the DispatcherServlet, request handling infrastructure, and
the embedded web server based on sensible defaults.
********** 4 **********
--- page 5 ---
After this, the developer creates a REST controller class. The class is
annotated with @RestController, and a method inside it is mapped to
a URL using @GetMapping("/hello"). The method simply returns a
string such as “Hello World.” There is no need to write XML
configuration or manually register the controller, because component
scanning automatically detects it and registers it as a Spring bean.
The next step is to run the application using the main() method or the
Spring Boot Maven/Gradle plugin. During startup, Spring Boot’s auto-
configuration mechanism checks the available dependencies and
configures beans such as the embedded Tomcat server, HTTP message
converters, and request mappings. Once the application is running, an
HTTP GET request to http://localhost:8080/hello is handled by
the embedded server, routed through the DispatcherServlet to the
controller method, and the response “Hello World” is sent back to the
client.
A company deploys microservices manually, causing frequent production
a.   failures. Design a CI/CD pipeline and explain how it improves reliability and
deployment speed.
When a company deploys microservices manually, errors such as wrong
configurations, inconsistent environments, missed steps, and untested
code frequently cause production failures. Designing a CI/CD
b.   (Continuous Integration / Continuous Deployment) pipeline
automates the entire build, test, and deployment process, which
significantly improves both reliability and deployment speed.
In a well-designed CI/CD pipeline, the process starts when a developer
commits code to a version control system such as Git. This commit
[10]
automatically triggers the Continuous Integration (CI) stage. In the CI
Q3   stage, the source code is checked out and a build is executed using tools
CO-; SO-;   like Maven or Gradle. Automated unit tests and static code analysis are
BL-   run immediately to detect defects early. If any test fails, the pipeline
stops, preventing faulty code from moving further. This early feedback   [10]
loop ensures that only verified code proceeds, reducing production
failures.
********** 5 **********
--- page 6 ---
Once the CI stage is successful, the pipeline moves to the artifact and
containerization stage. Each microservice is packaged as an
independent artifact and commonly built into a Docker image. The
image is versioned and pushed to a container registry. This ensures
consistency across development, testing, and production environments,
eliminating the “works on my machine” problem that is common with
manual deployments.
Next is the Continuous Deployment (CD) stage. The Docker images
are automatically deployed to staging or test environments using
container orchestration platforms such as Kubernetes. Automated
integration tests, contract tests, and smoke tests are executed to validate
inter-service communication and overall system behavior. Advanced
deployment strategies such as rolling deployments or blue-green
deployments are used to update services without downtime. Only after
these checks pass does the pipeline promote the release to production,
often with approval gates for sensitive systems.
The CI/CD pipeline improves reliability by removing manual steps,
enforcing automated testing at every stage, and ensuring consistent,
repeatable deployments. Faulty code is detected early, and deployment
failures are minimized through controlled rollout strategies and quick
rollback mechanisms. It improves deployment speed by automating
repetitive tasks, enabling frequent small releases instead of risky large
deployments, and allowing independent deployment of microservices.
Overall, a CI/CD pipeline transforms deployments from an error-prone
manual activity into a fast, predictable, and reliable process suitable for
large-scale microservices systems.
Q.3.b. Why are traditional ACID transactions difficult to implement in
microservices architecture?
Ans.3.b. Traditional ACID transactions are difficult to implement in a
microservices architecture because microservices are designed to be
distributed, loosely coupled, independently deployable, and highly
scalable, whereas ACID transactions assume a single, tightly
controlled transactional boundary. In microservices, each service
typically owns its own database (database-per-service pattern), so a
single business operation often spans multiple services and multiple
databases. Implementing ACID across these boundaries requires
distributed transactions using protocols like two-phase commit, which
introduce blocking behavior, high latency, and complex failure
handling. This directly conflicts with the scalability and availability
goals of microservices.
From an architectural perspective, ACID transactions require strong
consistency and locking of resources until a transaction completes. In a
distributed microservices environment, network delays, partial failures,
and service crashes are common, making it difficult to guarantee
atomicity and isolation without sacrificing availability. If one service
********** 6 **********
--- page 7 ---
becomes slow or unavailable, other services involved in the transaction
may be forced to wait, leading to cascading failures and reduced system
resilience. This violates the principle of fault isolation, which is a key
benefit of microservices.
Additionally, ACID transactions create tight coupling between services
because all participating services must coordinate transaction states and
support compatible transaction managers. This reduces independent
deployment and makes versioning and scaling of services more
complex. According to the CAP theorem, in the presence of network
partitions, a distributed system must choose between consistency and
availability. ACID transactions favor strong consistency, which reduces
availability—an unacceptable trade-off for most large-scale, cloud-
native microservices systems.
Therefore, traditional ACID transactions are difficult and undesirable in
microservices due to distribution, independent data ownership, failure
tolerance requirements, and scalability needs. As a result, microservices
architectures typically replace distributed ACID transactions with
eventual consistency models, Saga patterns, and compensating
transactions, which better align with the architectural principles of
microservices.
Explain the complete lifecycle of a microservice.
a.   Ans 5.a.
b.
[10]
Q4
CO-; SO-;
BL-
[10]
The lifecycle of a microservice describes all stages from its conception
to retirement, covering how it is designed, built, deployed, operated,
scaled, and finally decommissioned in a production environment. This
lifecycle ensures that microservices remain reliable, scalable, and
independently manageable.
The lifecycle begins with service identification and design, where
business requirements are analyzed and decomposed into small,
********** 7 **********

[Text in pictures on this page, read by OCR]
Update 07

01 Design 7S «®) Decommission 08
02 Develop C4 \S

a Microservices
mies

03 Build (a Monitor 06

04 Deploy (e Operate 05
--- page 8 ---
independently deployable services based on business capabilities and
bounded contexts. During this stage, clear API contracts, data
ownership (database per service), communication style (synchronous or
asynchronous), and non-functional requirements such as scalability,
security, and fault tolerance are defined.
Next is development and local testing, where the microservice is
implemented using a chosen technology stack. Developers write
business logic, REST or messaging interfaces, and configuration. Unit
tests and component tests are created to validate functionality in
isolation. Local environments or lightweight containers are often used
to simulate dependencies.
The microservice then enters the build and continuous integration
phase, where source code changes are committed to version control and
automatically built by a CI pipeline. Dependencies are resolved, the
application is compiled, and automated unit tests, static code analysis,
and security checks are executed. A successful build produces a
versioned artifact or container image.
This is followed by packaging and containerization, where the
microservice is packaged—commonly as a Docker container. The
container image includes the application and its runtime dependencies,
ensuring consistency across environments. The image is tagged and
stored in a container registry for reuse.
The next stage is deployment and release, where the microservice is
deployed to test, staging, and production environments using
orchestration platforms such as Kubernetes. Deployment strategies like
rolling updates, blue-green deployments, or canary releases are used to
minimize downtime and risk. Configuration is externalized using
environment variables or configuration servers.
Once deployed, the microservice moves into the runtime and
operation phase. Here, it handles live traffic, communicates with other
services, and interacts with its own data store. Monitoring, logging, and
distributed tracing are enabled to observe health, performance, and
failures. Alerts are configured to notify teams of abnormal behavior.
As usage patterns change, the microservice undergoes scaling and
optimization. Horizontal or vertical scaling is applied based on load,
often automatically through auto-scaling policies. Performance tuning,
caching, and resource optimization are carried out to meet service-level
objectives.
The lifecycle also includes maintenance and evolution, where the
microservice is enhanced with new features, security patches, and bug
fixes. New versions are continuously delivered through the CI/CD
pipeline, while backward compatibility of APIs is maintained through
versioning.
********** 8 **********
--- page 9 ---
Q.4.b. Design REST APIs for a Library Management System with operations:
• Add book
•   Issue book
•   Return book
Specify endpoints, HTTP methods, and sample request/response structures.
Ans.4.b. RESTful API design for a Library Management System
covering Add Book, Issue Book, and Return Book, including endpoints,
HTTP methods, and sample request/response structures.
1. Add Book
This operation allows a librarian to add a new book to the library
catalog.
• Endpoint: /api/books
• HTTP Method: POST
Sample Request (JSON):
{
"isbn": "978-0134685991",
"title": "Effective Java",
"author": "Joshua Bloch",
"category": "Programming",
"totalCopies": 5
}
Sample Response (JSON):
{
"bookId": "B101",
"message": "Book added successfully",
"availableCopies": 5
}
2. Issue Book
This operation issues a book to a library member if copies are available.
• Endpoint: /api/books/{bookId}/issue
• HTTP Method: POST
Sample Request (JSON):
{
"memberId": "M202",
"issueDate": "2026-04-01"
}
Sample Response (JSON):
{
"transactionId": "T501",
"bookId": "B101",
"memberId": "M202",
"status": "ISSUED",
********** 9 **********
--- page 10 ---
"dueDate": "2026-04-15"
}
3. Return Book
This operation records the return of an issued book and updates
availability.
• Endpoint: /api/books/{bookId}/return
• HTTP Method: POST
Sample Request (JSON):
{
"memberId": "M202",
"returnDate": "2026-04-10"
}
Sample Response (JSON):
{
"transactionId": "T501",
"bookId": "B101",
"status": "RETURNED",
"fineAmount": 0
}
What is Kubernetes? List its core components.
Kubernetes is an open-source container orchestration platform used to
automate the deployment, scaling, load balancing, and management of
containerized applications. It abstracts the underlying infrastructure and
provides a resilient, self-healing environment for running microservices
and cloud-native applications.
Core components of Kubernetes are:
Control Plane Components
Q5
1. API Server (kube-apiserver): The central management
CO-; SO-;   component that exposes the Kubernetes REST API and acts as   [10]
BL-   the entry point for all administrative and operational commands.   [10]
2. etcd: A distributed key–value store that holds the entire cluster
state, configuration data, and metadata reliably.
3. Scheduler (kube-scheduler): Assigns pods to suitable worker
nodes based on resource availability, policies, and constraints.
4. Controller Manager (kube-controller-manager): Runs
controllers that continuously monitor cluster state and take
corrective actions, such as restarting failed pods or maintaining
desired replica counts.
Worker Node Components
5. kubelet: An agent running on each worker node that ensures
containers are running in a pod as defined by the control plane.
********** 10 **********
--- page 11 ---
6. Container Runtime: Software such as Docker or containerd
responsible for running containers on the node.
7. kube-proxy: Manages network rules and enables service discovery
and load balancing across pods.
Together, these components enable Kubernetes to provide automated
deployment, scaling, fault tolerance, and efficient management of
containerized applications.
Q.5.b. How the CQRS manages the query traffic arrived at the micro-service?
Q.5.b. CQRS (Command Query Responsibility Segregation)
manages query traffic in a microservices architecture by separating
read (query) operations from write (command) operations, allowing
each side to be optimized independently. Instead of a single service and
data model handling both reads and writes, CQRS introduces distinct
paths, models, and sometimes even services for queries and commands.
In CQRS, query traffic is routed only to the query side of the
microservice, which is designed specifically for high-volume, read-
heavy workloads. The query model is typically denormalized and
optimized for fast reads, often using read-optimized databases such as
replicas, caches, or NoSQL stores. This prevents heavy read traffic from
impacting write performance and transactional consistency on the
command side.
When a command modifies data, the command side processes it and
updates the write database. These changes are then propagated to the
query side using events or asynchronous messaging. The query side
consumes these events and updates its read models accordingly.
Because this synchronization is asynchronous, the query model may be
eventually consistent, but it remains highly available and scalable.
From a traffic management perspective, CQRS enables horizontal
scaling of the query side independently. If query traffic increases,
additional read-service instances or read replicas can be added without
affecting the command side. Load balancers and API gateways can
route all GET requests to the query service, while POST, PUT, and
DELETE requests go to the command service. Caching layers can also
be placed in front of the query side to further absorb read traffic.
Thus, CQRS manages query traffic by isolating it from writes, using
read-optimized data models, enabling independent scaling, and
supporting eventual consistency, which together improve performance,
scalability, and stability of microservices under heavy read loads.
Q6   A large microservices system struggles with service-to-service security, traffic
[10]
CO-; SO-;   a.   control, and observability. Explain how a Service Mesh can address these
BL-   challenges.
********** 11 **********
--- page 12 ---
Ans 6.a
In a large microservices system, managing service-to-service security,
traffic control, and observability becomes difficult when these   [10]
concerns are implemented individually inside each service. A Service
b.
Mesh addresses these challenges by introducing a dedicated
infrastructure layer that handles all inter-service communication in a
consistent, transparent, and centralized manner without changing
application code.
A service mesh works by deploying a sidecar proxy alongside each
microservice instance. All inbound and outbound traffic flows through
this proxy, allowing the mesh to control, secure, and observe
communication uniformly across the system.
For service-to-service security, a service mesh provides built-in
mechanisms such as mutual TLS (mTLS) for encrypting traffic and
authenticating services automatically. Each service gets a verifiable
identity, and secure communication is enforced by default without
developers having to implement certificates, encryption logic, or
authentication libraries in application code. Fine-grained authorization
policies can also be applied centrally to control which services are
allowed to communicate with each other, improving zero-trust security.
For traffic control, a service mesh enables intelligent traffic
management at the infrastructure level. It supports features such as load
balancing, retries, timeouts, circuit breakers, rate limiting, and fault
injection. Advanced deployment strategies like canary releases, blue-
green deployments, and traffic splitting can be implemented by
routing a percentage of traffic to different service versions. This allows
safer releases and better resilience without modifying service logic.
For observability, a service mesh automatically captures detailed
telemetry data from all service interactions. This includes metrics
(latency, request rates, error rates), distributed traces across multiple
services, and structured logs. Because proxies observe all traffic, the
observability data is consistent and complete, even when services are
written in different languages. Central dashboards and alerts can be
built using this data, making it easier to detect failures, performance
bottlenecks, and dependency issues in complex microservices
environments.
In summary, a service mesh addresses these challenges by offloading
cross-cutting concerns from application code to the platform layer. It
standardizes security through mTLS and policy enforcement, improves
reliability and deployment safety through advanced traffic control, and
enhances visibility through uniform observability. Popular service mesh
implementations such as Istio and Linkerd are widely used to provide
these capabilities in large-scale, production-grade microservices
systems
********** 12 **********
--- page 13 ---
Q.6.b. Explain any two microservices integration patterns.
Ans .6.b.
Active Composition or Orchestration Microservice integration can be
implemented in such a way that a given (integration) microservice actively
calls several other services (can be core or composite service). The business
logic and the network communication are built as part of the integration
service. The integration microservice should formulate business functionality
out of the composition that it does.
For example, as illustrated in Figure, microservice-1 calls microservice-4 and
microservice-5 synchronously. The business capability that microservice-1
offers is a composition of the capabilities of microservice-4 and microservice-
5. Also, the integration service that we develop can be exposed as an API via
the API gateway layer. Figure 7-5 Active composition of microservices : a
given integration microservice calls multiple microservices and formulates a
business capability The key concept here is that, with an active composition ,
we create an integration service that’s dependent on some other set of
microservices. If you consider the theoretical aspects that we discussed in the
********** 13 **********
--- page 14 ---
irst few chapters, this seems like a violation of the microservices principles.
But it’s virtually impossible to build anything useful without depending on the
other services and systems. What really important here is to understand the
boundaries between these services and clearly define the capabilities.
Reactive Composition or Choreography With the reactive communication
style, we don’t have a service that synchronously calls other services. Instead,
all the interactions between services are implemented using the asynchronous
event-driven communication style. For example, as shown in Figure 7-6, the
communication between the microservices and the consumer application is
done via event-driven asynchronous messaging. Therefore, we need to use an
event bus as the messaging backbone. The event bus is a dumb messaging
infrastructure and all the logic resides at the service level
Explain the key difference between JWT and OAuth 2.0?
a.   Ans.7.a.   [10]
JWT (JSON Web Token)   OAuth 2.0
Q7   An authorization
A token format (standard for structuring   framework/protocol that
CO-; SO-;
and signing tokens).   defines flows for obtaining
BL-   and using access tokens.
Delegate and manage
Securely transmit claims/information   [10]
authorization (granting
(authentication + authorization data) in a
controlled access to
self-contained way.
resources).
********** 14 **********
--- page 15 ---
Services obtain an access
Services exchange a signed JWT directly.   token from an Authorization
The receiving service validates the   Server (using a grant type),
signature and claims locally (stateless).   then present it to the
resource service.
Can use any token format
— commonly JWT (as
Always a structured, self-contained JWT
bearer token) or opaque
(with header, payload, signature).
tokens (random strings
requiring introspection).
Can be stateful (especially
Fully stateless. No need to call back to a
with opaque tokens that need
central server for validation (just verify
introspection) or stateless
signature + claims).
(when using JWTs).
More complex (requires
Authorization Server,
Simpler to implement for internal trusted
client registration, secure
services.
secret handling in Client
Credentials flow).
Q.7.b. Discuss the challenges of securing communication between
microservices. Explain how mTLS and service mesh (sidecar pattern) help in
achieving authentication and encryption between services.
Ans.7.b.
Securing communication between microservices is challenging because
microservices are distributed, independently deployable, and often
communicate over untrusted networks. Unlike monolithic
applications, where internal calls occur within a single process or
trusted network, microservices interact over HTTP/gRPC or messaging
systems, exposing them to risks such as eavesdropping, tampering,
impersonation, and replay attacks. Key challenges include
authentication, authorization, encryption, certificate management,
and key rotation for thousands of service-to-service connections.
Manually implementing these in every service increases complexity,
introduces inconsistency, and is error-prone.
Mutual TLS (mTLS) helps solve these challenges by providing both
encryption and strong authentication at the transport layer. In mTLS,
each service presents a certificate to prove its identity to the other
service, and all traffic is encrypted. This ensures that only authorized
services can communicate and that data in transit cannot be intercepted
or modified. mTLS also allows automatic certificate rotation and
centralized management when combined with a certificate authority,
reducing operational overhead.
********** 15 **********
--- page 16 ---
A service mesh, implemented via the sidecar pattern, further
simplifies secure communication. In this model, a sidecar proxy is
deployed alongside each microservice instance, intercepting all inbound
and outbound traffic. The proxies handle mTLS automatically,
encrypting traffic and verifying service identities without requiring
changes to application code. Policies for authentication, authorization,
and traffic rules are centrally configured in the mesh, ensuring
consistent enforcement across all services. This approach offloads
security responsibilities from individual services, provides uniform
encryption and identity verification, and integrates seamlessly with
observability and traffic management features.
In summary, the distributed nature of microservices makes secure
service-to-service communication complex. mTLS ensures encryption
and mutual authentication, while a service mesh with sidecar
proxies automates these mechanisms across the system, providing
consistent, scalable, and reliable security without adding significant
complexity to individual microservices.
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper d4f4107f0f73

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/MBATech_Computer_7047/Microservices and Architecture/ANS_Microservices and Architecture(702CO0E010)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 03 Jul 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech Intg. (CE)/MBA Tech (Comp)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Microservices and Architecture
Date: 03 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. _1___ is compulsory.
5. Out of remaining questions, attempt any __4___ questions.
6. Assume Suitable data if necessary.
Q1
Answer briefly:   [20]
a.   A startup initially developed its e-commerce application as a monolithic
system. As the number of users increased from 10,000 to 1 million,
deployment failures and downtime became frequent. Analyze the situation
and justify whether migrating to Microservices would solve these issues.
Explain with architectural reasoning.
Ans.1.a. As the startup’s user base grew from 10,000 to 1 million, the
limitations of its monolithic architecture became more visible, leading to
frequent deployment failures and downtime. In a monolithic system, all
CO- ;
SO- ;   application modules such as user management, product catalog, orders,   [5]
BL-   payments, and notifications are tightly coupled and deployed as a single unit.
Any small change, bug fix, or enhancement in one module requires
rebuilding, testing, and redeploying the entire application. With a large user
base and increasing traffic, this results in long deployment times, higher risk
of failure, and complete application downtime even for minor issues.
Scalability is also limited because the entire application must be scaled
together, even if only one component (for example, payment or search)
experiences high load, leading to inefficient resource utilization and
performance bottlenecks.
********** 1 **********
--- page 2 ---
Migrating to a microservices architecture can significantly reduce
these issues if designed and implemented correctly. In microservices,
the application is decomposed into smaller, independent services, each
responsible for a specific business capability and typically owning its
own database. From an architectural perspective, this enables
independent deployment, meaning a failure or update in one service
does not bring down the entire system. For example, updating the
recommendation service will not affect order processing or user
authentication. This directly addresses the deployment failures and
downtime experienced in the monolithic setup. Microservices also
support horizontal scalability, allowing only the heavily used services,
such as product search or checkout, to be scaled independently, which
is critical when handling millions of users.
Additionally, microservices improve system resilience through fault
isolation. If one service fails, circuit breakers and retries can prevent
cascading failures, ensuring partial functionality rather than total
downtime. Continuous deployment pipelines become safer and faster
because services are smaller and easier to test. Architecturally,
microservices align well with cloud-native practices, containerization,
and orchestration platforms, enabling rolling updates and zero-
downtime deployments.
b.   Write a note on the following design principles for developing the micro-
services?
(i) Loose Coupling
(ii) Resiliency
Ans.1.b.
CO- ;
SO- ;   (i)   Loose Coupling: -
Coupling is a measure of the interdependence between micro [5]
BL-
services. When there is a high interdependency between micro
services, this will result in a tightly coupled system, while a low
interdependency will produce a loosely coupled system. Tightly
coupled systems build a brittle system architecture. A change done
in one system will affect all the related systems. If one system goes
down, all the related systems will be dysfunctional. A micro
services architecture must be highly cohesive and loosely coupled.
********** 2 **********
--- page 3 ---
(ii)   Resiliency: - Resilience is a measure of the capacity of a system or
individual components in a system to recover quickly from a failure.
In other words, it is an attribute of a system that enables it to deal
with failure in a way that doesn’t cause the entire system to fail.
There are various ways to achieve resilience - time out, circuit
breaker, fail fast etc.
c.   Explain the Component and integration testing?
: Component Testing: It focuses on testing the interaction and integration
between multiple micro services or components within a system. Component
testing assesses the behaviour of a set of interconnected services or components
that work together to accomplish a specific task or functionality.
• These components may include micro services, modules, or other units of
the application architecture.
•   Unlike unit testing, component testing may involve real-world interactions
with external dependencies, such as databases, APIs, or other services.
Benefits of Component Testing
• Component testing validates the integration and communication between
micro services, uncovering issues related to service dependencies and data
flow.
Challenges of Component Testing
•   Coordinating and orchestrating component tests across multiple services
CO- ;   can be challenging. Ensuring consistent test environments and managing
test data can also be complex.   [5]
SO- ;
BL-   Integration testing- It verifies the interaction between different services or
components to ensure they work together correctly. Unlike unit testing,
which focuses on testing individual units in isolation, integration testing
evaluates how these units interact and communicate with each other.
•   Integration testing validates the interaction and communication between
different services or components to ensure they exchange data and
collaborate effectively.
•   Integration testing often involves end-to-end testing scenarios that span
multiple services or components, simulating real-world user interactions
and workflows.
Benefits of Integration Testing
•   Integration testing helps ensure data consistency across multiple services or
components.
Challenges of Integration Testing
•   Setting up and maintaining integration test environments that accurately
reflect the production environment can be difficult.
CO- ;   d.
1. What is Docker? Explain Docker image and container.
SO- ;
[5]
BL-
What is inter-service communication? Mention synchronous and   [10]
Q2   a.   asynchronous methods.
CO-; SO-;
BL-
Ans.2.a.   [10]
********** 3 **********
--- page 4 ---
Inter-service communication is the mechanism by which independent
services in a distributed or microservices-based architecture exchange
b.   data and coordinate actions to fulfill business functionality. Since each
service runs in its own process and often on different machines,
communication over a network is required to share requests, responses,
or events.
Synchronous communication is request–response based, where the
calling service waits for an immediate reply from the called service.
Common synchronous methods include RESTful APIs over
HTTP/HTTPS, gRPC (remote procedure calls using HTTP/2 and
Protocol Buffers), and GraphQL. While synchronous communication is
simple to implement and suitable for real-time operations, it increases
coupling between services and can lead to higher latency and cascading
failures if a dependent service is slow or unavailable.
Asynchronous communication is event-driven or message-based,
where the calling service sends a message and continues processing
without waiting for an immediate response. Common asynchronous
methods include message queues and event streaming platforms such as
Apache Kafka, RabbitMQ, and cloud-based messaging services, as well
as publish–subscribe patterns. Asynchronous communication improves
scalability, fault tolerance, and loose coupling, making it well-suited for
high-traffic and resilient microservices systems.
Q.2.b A team wants to quickly create a REST microservice without manual
configuration. Explain how Spring Boot dependencies and auto-configuration
help achieve this. Illustrate using a simple Hello World service flow.
Spring Boot allows a team to quickly create a REST microservice
without manual configuration by using starter dependencies and auto-
configuration, and this process can be clearly understood through the
programming steps of a simple Hello World service. First, the developer
creates a Spring Boot project using Spring Initializr or an IDE and
selects the dependency spring-boot-starter-web. This single starter
internally brings in all required libraries such as Spring MVC, an
embedded Tomcat server, Jackson for JSON processing, and validation
support, so no explicit dependency management or server setup is
required.
The next programming step is to define the main application class. This
class is annotated with @SpringBootApplication, which is a
combination of @Configuration, @EnableAutoConfiguration, and
@ComponentScan. When the application starts, Spring Boot
automatically scans the classpath, detects the web dependency, and
configures the DispatcherServlet, request handling infrastructure, and
the embedded web server based on sensible defaults.
********** 4 **********
--- page 5 ---
After this, the developer creates a REST controller class. The class is
annotated with @RestController, and a method inside it is mapped to
a URL using @GetMapping("/hello"). The method simply returns a
string such as “Hello World.” There is no need to write XML
configuration or manually register the controller, because component
scanning automatically detects it and registers it as a Spring bean.
The next step is to run the application using the main() method or the
Spring Boot Maven/Gradle plugin. During startup, Spring Boot’s auto-
configuration mechanism checks the available dependencies and
configures beans such as the embedded Tomcat server, HTTP message
converters, and request mappings. Once the application is running, an
HTTP GET request to http://localhost:8080/hello is handled by
the embedded server, routed through the DispatcherServlet to the
controller method, and the response “Hello World” is sent back to the
client.
A company deploys microservices manually, causing frequent production
a.   failures. Design a CI/CD pipeline and explain how it improves reliability and
deployment speed.
When a company deploys microservices manually, errors such as wrong
configurations, inconsistent environments, missed steps, and untested
code frequently cause production failures. Designing a CI/CD
b.   (Continuous Integration / Continuous Deployment) pipeline
automates the entire build, test, and deployment process, which
significantly improves both reliability and deployment speed.
In a well-designed CI/CD pipeline, the process starts when a developer
commits code to a version control system such as Git. This commit
[10]
automatically triggers the Continuous Integration (CI) stage. In the CI
Q3   stage, the source code is checked out and a build is executed using tools
CO-; SO-;   like Maven or Gradle. Automated unit tests and static code analysis are
BL-   run immediately to detect defects early. If any test fails, the pipeline
stops, preventing faulty code from moving further. This early feedback   [10]
loop ensures that only verified code proceeds, reducing production
failures.
********** 5 **********
--- page 6 ---
Once the CI stage is successful, the pipeline moves to the artifact and
containerization stage. Each microservice is packaged as an
independent artifact and commonly built into a Docker image. The
image is versioned and pushed to a container registry. This ensures
consistency across development, testing, and production environments,
eliminating the “works on my machine” problem that is common with
manual deployments.
Next is the Continuous Deployment (CD) stage. The Docker images
are automatically deployed to staging or test environments using
container orchestration platforms such as Kubernetes. Automated
integration tests, contract tests, and smoke tests are executed to validate
inter-service communication and overall system behavior. Advanced
deployment strategies such as rolling deployments or blue-green
deployments are used to update services without downtime. Only after
these checks pass does the pipeline promote the release to production,
often with approval gates for sensitive systems.
The CI/CD pipeline improves reliability by removing manual steps,
enforcing automated testing at every stage, and ensuring consistent,
repeatable deployments. Faulty code is detected early, and deployment
failures are minimized through controlled rollout strategies and quick
rollback mechanisms. It improves deployment speed by automating
repetitive tasks, enabling frequent small releases instead of risky large
deployments, and allowing independent deployment of microservices.
Overall, a CI/CD pipeline transforms deployments from an error-prone
manual activity into a fast, predictable, and reliable process suitable for
large-scale microservices systems.
Q.3.b. Why are traditional ACID transactions difficult to implement in
microservices architecture?
Ans.3.b. Traditional ACID transactions are difficult to implement in a
microservices architecture because microservices are designed to be
distributed, loosely coupled, independently deployable, and highly
scalable, whereas ACID transactions assume a single, tightly
controlled transactional boundary. In microservices, each service
typically owns its own database (database-per-service pattern), so a
single business operation often spans multiple services and multiple
databases. Implementing ACID across these boundaries requires
distributed transactions using protocols like two-phase commit, which
introduce blocking behavior, high latency, and complex failure
handling. This directly conflicts with the scalability and availability
goals of microservices.
From an architectural perspective, ACID transactions require strong
consistency and locking of resources until a transaction completes. In a
distributed microservices environment, network delays, partial failures,
and service crashes are common, making it difficult to guarantee
atomicity and isolation without sacrificing availability. If one service
********** 6 **********
--- page 7 ---
becomes slow or unavailable, other services involved in the transaction
may be forced to wait, leading to cascading failures and reduced system
resilience. This violates the principle of fault isolation, which is a key
benefit of microservices.
Additionally, ACID transactions create tight coupling between services
because all participating services must coordinate transaction states and
support compatible transaction managers. This reduces independent
deployment and makes versioning and scaling of services more
complex. According to the CAP theorem, in the presence of network
partitions, a distributed system must choose between consistency and
availability. ACID transactions favor strong consistency, which reduces
availability—an unacceptable trade-off for most large-scale, cloud-
native microservices systems.
Therefore, traditional ACID transactions are difficult and undesirable in
microservices due to distribution, independent data ownership, failure
tolerance requirements, and scalability needs. As a result, microservices
architectures typically replace distributed ACID transactions with
eventual consistency models, Saga patterns, and compensating
transactions, which better align with the architectural principles of
microservices.
Explain the complete lifecycle of a microservice.
a.   Ans 5.a.
b.
[10]
Q4
CO-; SO-;
BL-
[10]
The lifecycle of a microservice describes all stages from its conception
to retirement, covering how it is designed, built, deployed, operated,
scaled, and finally decommissioned in a production environment. This
lifecycle ensures that microservices remain reliable, scalable, and
independently manageable.
The lifecycle begins with service identification and design, where
business requirements are analyzed and decomposed into small,
********** 7 **********

[Text in pictures on this page, read by OCR]
Update 07

01 Design 7S «®) Decommission 08
02 Develop C4 \S

a Microservices
mies

03 Build (a Monitor 06

04 Deploy (e Operate 05
--- page 8 ---
independently deployable services based on business capabilities and
bounded contexts. During this stage, clear API contracts, data
ownership (database per service), communication style (synchronous or
asynchronous), and non-functional requirements such as scalability,
security, and fault tolerance are defined.
Next is development and local testing, where the microservice is
implemented using a chosen technology stack. Developers write
business logic, REST or messaging interfaces, and configuration. Unit
tests and component tests are created to validate functionality in
isolation. Local environments or lightweight containers are often used
to simulate dependencies.
The microservice then enters the build and continuous integration
phase, where source code changes are committed to version control and
automatically built by a CI pipeline. Dependencies are resolved, the
application is compiled, and automated unit tests, static code analysis,
and security checks are executed. A successful build produces a
versioned artifact or container image.
This is followed by packaging and containerization, where the
microservice is packaged—commonly as a Docker container. The
container image includes the application and its runtime dependencies,
ensuring consistency across environments. The image is tagged and
stored in a container registry for reuse.
The next stage is deployment and release, where the microservice is
deployed to test, staging, and production environments using
orchestration platforms such as Kubernetes. Deployment strategies like
rolling updates, blue-green deployments, or canary releases are used to
minimize downtime and risk. Configuration is externalized using
environment variables or configuration servers.
Once deployed, the microservice moves into the runtime and
operation phase. Here, it handles live traffic, communicates with other
services, and interacts with its own data store. Monitoring, logging, and
distributed tracing are enabled to observe health, performance, and
failures. Alerts are configured to notify teams of abnormal behavior.
As usage patterns change, the microservice undergoes scaling and
optimization. Horizontal or vertical scaling is applied based on load,
often automatically through auto-scaling policies. Performance tuning,
caching, and resource optimization are carried out to meet service-level
objectives.
The lifecycle also includes maintenance and evolution, where the
microservice is enhanced with new features, security patches, and bug
fixes. New versions are continuously delivered through the CI/CD
pipeline, while backward compatibility of APIs is maintained through
versioning.
********** 8 **********
--- page 9 ---
Q.4.b. Design REST APIs for a Library Management System with operations:
• Add book
•   Issue book
•   Return book
Specify endpoints, HTTP methods, and sample request/response structures.
Ans.4.b. RESTful API design for a Library Management System
covering Add Book, Issue Book, and Return Book, including endpoints,
HTTP methods, and sample request/response structures.
1. Add Book
This operation allows a librarian to add a new book to the library
catalog.
• Endpoint: /api/books
• HTTP Method: POST
Sample Request (JSON):
{
"isbn": "978-0134685991",
"title": "Effective Java",
"author": "Joshua Bloch",
"category": "Programming",
"totalCopies": 5
}
Sample Response (JSON):
{
"bookId": "B101",
"message": "Book added successfully",
"availableCopies": 5
}
2. Issue Book
This operation issues a book to a library member if copies are available.
• Endpoint: /api/books/{bookId}/issue
• HTTP Method: POST
Sample Request (JSON):
{
"memberId": "M202",
"issueDate": "2026-04-01"
}
Sample Response (JSON):
{
"transactionId": "T501",
"bookId": "B101",
"memberId": "M202",
"status": "ISSUED",
********** 9 **********
--- page 10 ---
"dueDate": "2026-04-15"
}
3. Return Book
This operation records the return of an issued book and updates
availability.
• Endpoint: /api/books/{bookId}/return
• HTTP Method: POST
Sample Request (JSON):
{
"memberId": "M202",
"returnDate": "2026-04-10"
}
Sample Response (JSON):
{
"transactionId": "T501",
"bookId": "B101",
"status": "RETURNED",
"fineAmount": 0
}
What is Kubernetes? List its core components.
Kubernetes is an open-source container orchestration platform used to
automate the deployment, scaling, load balancing, and management of
containerized applications. It abstracts the underlying infrastructure and
provides a resilient, self-healing environment for running microservices
and cloud-native applications.
Core components of Kubernetes are:
Control Plane Components
Q5
1. API Server (kube-apiserver): The central management
CO-; SO-;   component that exposes the Kubernetes REST API and acts as   [10]
BL-   the entry point for all administrative and operational commands.   [10]
2. etcd: A distributed key–value store that holds the entire cluster
state, configuration data, and metadata reliably.
3. Scheduler (kube-scheduler): Assigns pods to suitable worker
nodes based on resource availability, policies, and constraints.
4. Controller Manager (kube-controller-manager): Runs
controllers that continuously monitor cluster state and take
corrective actions, such as restarting failed pods or maintaining
desired replica counts.
Worker Node Components
5. kubelet: An agent running on each worker node that ensures
containers are running in a pod as defined by the control plane.
********** 10 **********
--- page 11 ---
6. Container Runtime: Software such as Docker or containerd
responsible for running containers on the node.
7. kube-proxy: Manages network rules and enables service discovery
and load balancing across pods.
Together, these components enable Kubernetes to provide automated
deployment, scaling, fault tolerance, and efficient management of
containerized applications.
Q.5.b. How the CQRS manages the query traffic arrived at the micro-service?
Q.5.b. CQRS (Command Query Responsibility Segregation)
manages query traffic in a microservices architecture by separating
read (query) operations from write (command) operations, allowing
each side to be optimized independently. Instead of a single service and
data model handling both reads and writes, CQRS introduces distinct
paths, models, and sometimes even services for queries and commands.
In CQRS, query traffic is routed only to the query side of the
microservice, which is designed specifically for high-volume, read-
heavy workloads. The query model is typically denormalized and
optimized for fast reads, often using read-optimized databases such as
replicas, caches, or NoSQL stores. This prevents heavy read traffic from
impacting write performance and transactional consistency on the
command side.
When a command modifies data, the command side processes it and
updates the write database. These changes are then propagated to the
query side using events or asynchronous messaging. The query side
consumes these events and updates its read models accordingly.
Because this synchronization is asynchronous, the query model may be
eventually consistent, but it remains highly available and scalable.
From a traffic management perspective, CQRS enables horizontal
scaling of the query side independently. If query traffic increases,
additional read-service instances or read replicas can be added without
affecting the command side. Load balancers and API gateways can
route all GET requests to the query service, while POST, PUT, and
DELETE requests go to the command service. Caching layers can also
be placed in front of the query side to further absorb read traffic.
Thus, CQRS manages query traffic by isolating it from writes, using
read-optimized data models, enabling independent scaling, and
supporting eventual consistency, which together improve performance,
scalability, and stability of microservices under heavy read loads.
Q6   A large microservices system struggles with service-to-service security, traffic
[10]
CO-; SO-;   a.   control, and observability. Explain how a Service Mesh can address these
BL-   challenges.
********** 11 **********
--- page 12 ---
Ans 6.a
In a large microservices system, managing service-to-service security,
traffic control, and observability becomes difficult when these   [10]
concerns are implemented individually inside each service. A Service
b.
Mesh addresses these challenges by introducing a dedicated
infrastructure layer that handles all inter-service communication in a
consistent, transparent, and centralized manner without changing
application code.
A service mesh works by deploying a sidecar proxy alongside each
microservice instance. All inbound and outbound traffic flows through
this proxy, allowing the mesh to control, secure, and observe
communication uniformly across the system.
For service-to-service security, a service mesh provides built-in
mechanisms such as mutual TLS (mTLS) for encrypting traffic and
authenticating services automatically. Each service gets a verifiable
identity, and secure communication is enforced by default without
developers having to implement certificates, encryption logic, or
authentication libraries in application code. Fine-grained authorization
policies can also be applied centrally to control which services are
allowed to communicate with each other, improving zero-trust security.
For traffic control, a service mesh enables intelligent traffic
management at the infrastructure level. It supports features such as load
balancing, retries, timeouts, circuit breakers, rate limiting, and fault
injection. Advanced deployment strategies like canary releases, blue-
green deployments, and traffic splitting can be implemented by
routing a percentage of traffic to different service versions. This allows
safer releases and better resilience without modifying service logic.
For observability, a service mesh automatically captures detailed
telemetry data from all service interactions. This includes metrics
(latency, request rates, error rates), distributed traces across multiple
services, and structured logs. Because proxies observe all traffic, the
observability data is consistent and complete, even when services are
written in different languages. Central dashboards and alerts can be
built using this data, making it easier to detect failures, performance
bottlenecks, and dependency issues in complex microservices
environments.
In summary, a service mesh addresses these challenges by offloading
cross-cutting concerns from application code to the platform layer. It
standardizes security through mTLS and policy enforcement, improves
reliability and deployment safety through advanced traffic control, and
enhances visibility through uniform observability. Popular service mesh
implementations such as Istio and Linkerd are widely used to provide
these capabilities in large-scale, production-grade microservices
systems
********** 12 **********
--- page 13 ---
Q.6.b. Explain any two microservices integration patterns.
Ans .6.b.
Active Composition or Orchestration Microservice integration can be
implemented in such a way that a given (integration) microservice actively
calls several other services (can be core or composite service). The business
logic and the network communication are built as part of the integration
service. The integration microservice should formulate business functionality
out of the composition that it does.
For example, as illustrated in Figure, microservice-1 calls microservice-4 and
microservice-5 synchronously. The business capability that microservice-1
offers is a composition of the capabilities of microservice-4 and microservice-
5. Also, the integration service that we develop can be exposed as an API via
the API gateway layer. Figure 7-5 Active composition of microservices : a
given integration microservice calls multiple microservices and formulates a
business capability The key concept here is that, with an active composition ,
we create an integration service that’s dependent on some other set of
microservices. If you consider the theoretical aspects that we discussed in the
********** 13 **********
--- page 14 ---
irst few chapters, this seems like a violation of the microservices principles.
But it’s virtually impossible to build anything useful without depending on the
other services and systems. What really important here is to understand the
boundaries between these services and clearly define the capabilities.
Reactive Composition or Choreography With the reactive communication
style, we don’t have a service that synchronously calls other services. Instead,
all the interactions between services are implemented using the asynchronous
event-driven communication style. For example, as shown in Figure 7-6, the
communication between the microservices and the consumer application is
done via event-driven asynchronous messaging. Therefore, we need to use an
event bus as the messaging backbone. The event bus is a dumb messaging
infrastructure and all the logic resides at the service level
Explain the key difference between JWT and OAuth 2.0?
a.   Ans.7.a.   [10]
JWT (JSON Web Token)   OAuth 2.0
Q7   An authorization
A token format (standard for structuring   framework/protocol that
CO-; SO-;
and signing tokens).   defines flows for obtaining
BL-   and using access tokens.
Delegate and manage
Securely transmit claims/information   [10]
authorization (granting
(authentication + authorization data) in a
controlled access to
self-contained way.
resources).
********** 14 **********
--- page 15 ---
Services obtain an access
Services exchange a signed JWT directly.   token from an Authorization
The receiving service validates the   Server (using a grant type),
signature and claims locally (stateless).   then present it to the
resource service.
Can use any token format
— commonly JWT (as
Always a structured, self-contained JWT
bearer token) or opaque
(with header, payload, signature).
tokens (random strings
requiring introspection).
Can be stateful (especially
Fully stateless. No need to call back to a
with opaque tokens that need
central server for validation (just verify
introspection) or stateless
signature + claims).
(when using JWTs).
More complex (requires
Authorization Server,
Simpler to implement for internal trusted
client registration, secure
services.
secret handling in Client
Credentials flow).
Q.7.b. Discuss the challenges of securing communication between
microservices. Explain how mTLS and service mesh (sidecar pattern) help in
achieving authentication and encryption between services.
Ans.7.b.
Securing communication between microservices is challenging because
microservices are distributed, independently deployable, and often
communicate over untrusted networks. Unlike monolithic
applications, where internal calls occur within a single process or
trusted network, microservices interact over HTTP/gRPC or messaging
systems, exposing them to risks such as eavesdropping, tampering,
impersonation, and replay attacks. Key challenges include
authentication, authorization, encryption, certificate management,
and key rotation for thousands of service-to-service connections.
Manually implementing these in every service increases complexity,
introduces inconsistency, and is error-prone.
Mutual TLS (mTLS) helps solve these challenges by providing both
encryption and strong authentication at the transport layer. In mTLS,
each service presents a certificate to prove its identity to the other
service, and all traffic is encrypted. This ensures that only authorized
services can communicate and that data in transit cannot be intercepted
or modified. mTLS also allows automatic certificate rotation and
centralized management when combined with a certificate authority,
reducing operational overhead.
********** 15 **********
--- page 16 ---
A service mesh, implemented via the sidecar pattern, further
simplifies secure communication. In this model, a sidecar proxy is
deployed alongside each microservice instance, intercepting all inbound
and outbound traffic. The proxies handle mTLS automatically,
encrypting traffic and verifying service identities without requiring
changes to application code. Policies for authentication, authorization,
and traffic rules are centrally configured in the mesh, ensuring
consistent enforcement across all services. This approach offloads
security responsibilities from individual services, provides uniform
encryption and identity verification, and integrates seamlessly with
observability and traffic management features.
In summary, the distributed nature of microservices makes secure
service-to-service communication complex. mTLS ensures encryption
and mutual authentication, while a service mesh with sidecar
proxies automates these mechanisms across the system, providing
consistent, scalable, and reliable security without adding significant
complexity to individual microservices.
********** 16 **********
````

## 2024-25 · Final-Exam · Sem 3 · Answer key · paper cb637816f511

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_03/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Microservices and Architecture/ANS_Microservices and Architecture(703CO0C022)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 27 Nov 2024
- Text: mixed (5 pages), mean OCR confidence 66.9

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: II/Semester III(Exam Year: 2024-2025)
Subject: Microservices and Architecture
Date: 27 Nov 2024   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 5 pages.
2. Question No. 1 is compulsory
3. Out of the remaining questions, answer any 4
4. In all, 5 questions to be attempted
5. Assume suitable data if necessary. Specify what you have assumed in the answer.
6. Figures on the right hand side indicate full marks
1a. Microservices Design Principles
•   Resilience: Refers to the system's ability to handle failures gracefully. Techniques include
retries, circuit breakers, and fallbacks, ensuring service availability despite component failures.
• Config Storage Only in the Environment: Emphasizes externalizing configuration, allowing
different environments (development, staging, production) to have specific settings without
changing the codebase, enhancing flexibility and security.
1b. Saga Orchestration Pattern
The Saga Orchestration pattern manages distributed transactions by breaking them into smaller,
independent transactions. An orchestrator coordinates these transactions, ensuring that each one
completes successfully or triggers compensating transactions in case of failure, maintaining overall
data consistency.
1c. Spring Boot Controller Class
@RestController
@RequestMapping("/api")
public class MathController {
@PostMapping("/sum")
public ResponseEntity<Integer> sum(@RequestBody SumRequest request) {
int result = request.getNum1() + request.getNum2();
return ResponseEntity.ok(result);
}
}
class SumRequest {
private int num1;
private int num2;
// Getters and Setters
********** 1 **********
--- page 2 ---
}
1d. Deployment YAML in Kubernetes
A Deployment YAML file defines the desired state for a Kubernetes application. It specifies the
container image, replicas, and other configurations. Kubernetes uses this file to manage the lifecycle of
the application, ensuring the specified number of replicas is running and healthy.
2a. Actuator and /health Endpoint
• Actuator: A Spring Boot feature providing endpoints to monitor and manage applications. The
/health endpoint returns the application's health status, indicating whether the application is up
and running.
Custom Health Check Example:
@Component
@ConditionalOnEnabledHealthIndicator("external_service_health")
public class CustomHealthCheck implements HealthIndicator {
private final Random randomizer = new Random();
private final List<Integer> statusCodes = List.of(200, 204, 401, 404, 503);
@Override
public Health health() {
int randomStatusCode =
statusCodes.get(randomizer.nextInt(statusCodes.size()));
Health.Builder healthBuilder = new Health.Builder();
return (switch(randomStatusCode) {
case 200, 204 -> healthBuilder.up()
.withDetail("External_Service", "Service is Up and Running ✅")
.withDetail("url", "https://example.com");
case 503 -> healthBuilder.down()
.withDetail("External_Service", "Service is Down 🔻")
.withDetail("alternative_url", "https://alt-example.com");
default -> healthBuilder.unknown().withException(new
RuntimeException("Received status: " + randomStatusCode));
}).build();
}
}
2b. Kubernetes vs. Docker
Kubernetes addresses orchestration, scaling, and management of containerized applications, while
Docker focuses on containerization. Kubernetes solves challenges like load balancing, service
discovery, and automated rollouts/rollback.
Diagram: Show Docker containers as components within Kubernetes Pods.
3a. API Gateway Concepts
1. Header-based Routing: Routes requests based on HTTP headers.
2. Method-based Routing: Directs requests based on HTTP methods (GET, POST).
3. Aggregation: Combines responses from multiple microservices into a single response.
4. Rate Limiting: Controls the number of requests a client can make to prevent abuse.
********** 2 **********
--- page 3 ---
5. Transformation: Modifies request/response formats for compatibility.
3b. OAuth 2.0 with Identity Providers
Using OAuth 2.0, users can authenticate with an external Identity Provider (like Google). The
application requests an access token from the Identity Provider, allowing secure access to protected
resources.
•   Authentication and Permission: You log in to your Google account (if not already logged in) and grant
permission for the site to access certain information from your Google account (like your email address
or profile info).
• Authorization Code Exchange: After you give permission, Google sends back an authorization
code to the site.
•   Access Token: The site exchanges that authorization code for an access token, which allows it to access
your information from Google
•   Access Your Info: The site can then retrieve your basic profile information (like your name and email)
using the access token.
4a. Docker & Kubernetes Commands
1. Build Docker Image: docker build -t image-name .
2. Get Status of Kubernetes Services: kubectl get services
3. Check if Container is Running: docker ps
4. Stop the Container: docker stop container-id
5. Get Inside the Running Container: docker exec -it container-id /bin/bash
4b. Deploying Spring Boot to Kubernetes
1. Build a Docker image for the Spring Boot application.
2. Publish the docker to a registry
3. Create a Deployment YAML specifying the image path on the registry and desired replicas.
4. Apply the YAML with kubectl apply -f deployment.yaml.
5. Expose the service using a Service YAML to manage access.
5a. Request DTO vs. JPA Class
• Request DTO: Data Transfer Object for receiving input.
• JPA Class: Represents the database entity.
JPA Class Example:
@Entity
@Table(name=”Person”)
public class User {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
@Column(name=”AGE”)
********** 3 **********
--- page 4 ---
private Integer age;
@Column(name=”NAME”)
private String name;
// Getters and Setters
}
Request DTO Example:
public class UserRequestDTO {
private Integer age;
private String name;
// Getters and Setters
}
5b. Spring Cloud Config
Spring Cloud Config provides server and client-side support for externalized configuration in a
distributed system. To implement:
1. Set up a Spring Cloud Config server.
2. Store configuration properties in a Git repository.
3. Configure client applications to fetch configurations from the server.
6a. Kafka Architecture
Kafka is a distributed messaging system with producers (which send messages), consumers (which read
messages), topics (categories for messages), and brokers (servers managing topics). It supports high-
throughput, fault-tolerant message processing.
6b. ACID Properties
ACID properties ensure reliable processing of database transactions:
• Atomicity: All operations in a transaction complete successfully or none do.
• Consistency: Transactions bring the database from one valid state to another.
•   Isolation: Transactions are isolated from one another until completed.
•   Durability: Once a transaction is committed, it remains so, even in case of a failure.
7a. Questions
1. Default Tomcat Port: 8080
2. Change Port Number: Set in application.properties (e.g., server.port=8081).
3. Controller Annotations:
o   @RestController: Marks the class as a REST controller.
o @GetMapping: Maps HTTP GET requests to specific handler methods.
o @PostMapping: Maps HTTP POST requests to specific handler methods.
7b. True or False Statements
1. False
2. True
********** 4 **********
--- page 5 ---
3. False
4. True
5. True

FIC DI EH ar
````
