# Advanced Java: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 4423e1172437

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Advanced Java/ANS_Advanced Java(703CO0E019)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 14 May 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Advanced Java
Date: 14 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Question No. 1 is compulsory
4. Out of remaining questions, attempt any 4 questions
5. In all 5 questions to be attempted.
6. All questions carry equal marks
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary
Q1   Solve the following sub-questions.
CO   a. JSTL is a collection of standard tags used in JSP to perform common tasks like:   [5]
-1;   •   Conditional processing
SO-   • Looping
7;   • Formatting
BL-   • Database operations
3   It replaces Java code (<% %>) with clean, readable tags.
<c:set var="name" value="John"/>
<c:if test="${name == 'John'}">
Welcome John
</c:if>
<c:forEach var="i" begin="1" end="3">
${i}
</c:forEach>
EL is used to access data stored in different scopes (request, session, application)
without Java code.
${expression}
Feature   JSTL   EL
Type   Tag Library   Expression language
Purpose   Perform logic (loops, conditions) Access data
Syntax   <c:...>   ${...}
Complexity More powerful   Simple
Usage   Control flow   Data retrieval
Key point
JSTL + EL = Clean JSP
********** 1 **********
--- page 2 ---
EL is used inside JSTL
Avoid scriptlets in modern JSP
Helps maintain separation of concerns
CO b   [5]
-2;   .   Hibernate is a Java-based ORM (Object-Relational Mapping) framework that
SO-   simplifies database interactions by mapping Java objects to database tables.
7;   It eliminates the need for manual JDBC code and SQL queries, making database
BL-   operations more efficient and maintainable. Hibernate is widely used in enterprise
4   applications for data persistence.
Java Application
↓
Configuration (hibernate.cfg.xml)
↓
SessionFactory
↓
Session
↓
Transaction
↓
Query (HQL/Criteria)
↓
Database (RDBMS)
Step-by-Step Flow:
1. Load configuration file
2. Create SessionFactory
3. Open Session
4. Begin Transaction
5. Perform CRUD operations
6. Commit transaction
7. Close session
Ex:
Configuration cfg = new Configuration().configure();
SessionFactory factory = cfg.buildSessionFactory();
Session session = factory.openSession();
Transaction tx = session.beginTransaction();
Employee emp = new Employee();
emp.setName("John");
session.save(emp);
tx.commit();
session.close();
CO   c. What are the different modules in a Spring.   [5]
-1;
SO-   Spring Framework consists of the following core modules:
7;   Module   Purpose
BL-
Provides Dependency Injection (DI) and IoC
2   1️ Spring Core & Beans
(Inversion of Control).
********** 2 **********
--- page 3 ---
2️ Spring AOP (Aspect-   Used for cross-cutting concerns (e.g., logging,
Oriented Programming)   security, transactions).
Provides ApplicationContext for managing
3️ Spring Context
beans.
Simplifies database access and integrates with
4️ Spring JDBC & ORM
Hibernate, JPA, MyBatis.
5️ Spring MVC (Web Module) Used for web applications & REST APIs.
Provides authentication, authorization, and
6️ Spring Security
protection against threats.
Simplifies Spring configuration and provides
7️ Spring Boot
auto-configuration.
Simplifies database interactions with Spring Data
8️ Spring Data
JPA, MongoDB, Redis, etc.
Supports Microservices Architecture (Eureka,
9️ Spring Cloud
Feign, Zuul, etc.).
10 Spring Test   Supports unit & integration testing.
CO d What is Spring boot, solve challenges which exist with Spring MVC.   [5]
-1;   .
SO-
7;   Spring Boot is a framework built on top of Spring Framework that simplifies
BL-   application development by eliminating boilerplate configurations.
3   It provides:
Auto-configuration – No need for manual XML or Java-based configurations.
Embedded Servers – Comes with Tomcat, Jetty, and Undertow.
Microservices Support – Helps in building scalable applications.
Spring Boot Starters – Pre-configured dependencies for different features.
1️ Complex Configuration in Spring MVC
2️ Dependency Management Issues
3️ No Embedded Server in Spring MVC
4 REST API Development Requires Extra Configuration
Q2
CO   a. What is JDBCTemplate & advantage and key components with example.   [10
-2;   ]
SO-   Spring JDBC is part of the Spring Framework and provides a simple, consistent way
7;   to interact with relational databases using JDBC (Java Database Connectivity) while
BL-   removing much of the boilerplate code that developers typically need to write when
3   using JDBC directly. Spring JDBC provides both a low-level and high-level API,
simplifying the process of working with databases.
Here are some key notes on Spring JDBC:
1. Key Components
• JdbcTemplate: The core class in Spring JDBC that simplifies database
interactions. It provides methods to execute SQL queries, update statements,
and stored procedures. It automatically handles resource management (like
closing connections and handling exceptions).
********** 3 **********
--- page 4 ---
• NamedParameterJdbcTemplate: A subclass of JdbcTemplate that allows for
the use of named parameters in SQL queries instead of the traditional?
placeholders.
• SimpleJdbcCall: A helper class for calling stored procedures in a simpler
way.
• DataSource: Represents a connection pool or a factory for database
connections. Spring allows you to configure different types of data sources
like HikariCP, Apache DBCP, etc.
2. Common Operations
• Query Execution: Use JdbcTemplate.query() for queries that return a result
set and JdbcTemplate.update() for operations like INSERT, UPDATE, or
DELETE.
• Query for Objects: Use JdbcTemplate.queryForObject() when you expect a
single result and JdbcTemplate.queryForList() when you expect multiple
results.
• RowMapper: When using methods like query(), a RowMapper is used to map
rows of a result set to Java objects.
• PreparedStatementSetter: To set parameters on a prepared statement.
3. Spring JDBC Exceptions
• Spring provides a consistent exception hierarchy for handling database errors,
via the DataAccessException class. This eliminates the need for handling
different SQL exceptions (like SQLException) explicitly.
SQLErrorCodesTranslator: Helps map specific database error codes to exceptions
that can be more easily handled by the application.
CO b What is HQL, HCQL? Write the syntax to demonstrate the basic Crud   [10
-3;   .   operation using HQL.   ]
SO-
7;   HQL is designed to query the object model and not the relational model, making it
BL-   database-independent and more aligned with the application's object-oriented nature.
3
Key Features of HQL
• Object-Oriented: Queries are written in terms of the entity model, not the
database schema.
• Database Independent: Queries are independent of the underlying database.
• Powerful and Flexible: Supports CRUD operations, joins, aggregations, and
subqueries.
Basic HQL Syntax
********** 4 **********
--- page 5 ---
HCQL
The criteria query API lets us build nested, structured query expressions in Java,
providing a compile-time syntax checking that is not possible with a query language
like HQL or SQL.
********** 5 **********
--- page 6 ---
1. The simplest example of a criteria query is one with no optional parameters or
restrictions—the criteria query will simply return every object that corresponds to the
class.
2. Using Restrictions
The Criteria API makes it easy to use restrictions in your queries to selectively
retrieve objects; for instance, your application could retrieve only products with a
price over $30. You may add these restrictions to a Criteria object with
the add() method.
Q3
CO   a.   [10
-3;   ]
SO-   <!DOCTYPE html>
6;   <html>
BL-   <head>
3   <title>Form Submission</title>
</head>
<body>
<h2>Simple Form</h2>
<form action="FormServlet" method="post">
<label>Name:</label>
<input type="text" name="name" required><br><br>
<label>Email:</label>
<input type="email" name="email" required><br><br>
<input type="submit" value="Submit">
</form>
</body>
</html>
<%@ page language="java" contentType="text/html; charset=UTF-8"
pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
<title>Form Submitted</title>
</head>
<body>
<h2>Form Submitted Successfully!</h2>
<p><strong>Name:</strong> ${requestScope.name}</p>
<p><strong>Email:</strong> ${requestScope.email}</p>
<a href="index.html">Go Back</a>
</body>
********** 6 **********
--- page 7 ---
</html>
CO b Write a Simple REST API coding with all needed file like controller, service,   [10
-3;   .   repo for insert & get all students. [annotation is mandatory]   ]
SO-
7;
BL-   @Entity
3   @Table(name = "students")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class Student {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
@Column(nullable = false)
private String name;
@Column(nullable = false, unique = true)
private String email;
}
@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {
}.
@Service
public class StudentService {
@Autowired
private StudentRepository studentRepository;
// Insert a new student
public Student saveStudent(Student student) {
return studentRepository.save(student);
}
// Retrieve all students
public List<Student> getAllStudents() {
return studentRepository.findAll();
}
}
@RestController
@RequestMapping("/students")
********** 7 **********
--- page 8 ---
public class StudentController {
@Autowired
private StudentService studentService;
// Insert a new student
@PostMapping
public Student createStudent(@RequestBody Student student) {
return studentService.saveStudent(student);
}
// Get all students
@GetMapping
public List<Student> getAllStudents() {
return studentService.getAllStudents();
}
}
Q4
CO   a. What is AOP. Explain the following what are the types of Advice?   [10
-2;   1.Advice   ]
SO-   2.Aspect
7;   3.JointPoint
BL-   4.PointCut
4   5.Proxy
6.TargetClass
AOP (Aspect-Oriented Programming) is a programming paradigm that allows us to
separate cross-cutting concerns (such as logging, security, and transaction
management) from business logic.
Spring AOP helps in applying additional behavior (advice) to certain parts of the
application without modifying the actual code.
1️ Advice
Advice is the action taken when a specific event occurs in the application.
It defines what should happen and runs at different points of method execution.
2️ Aspect
An Aspect is a class that contains multiple Advices to apply cross-cutting concerns
like logging, security, and transactions.
3️ JoinPoint
A JoinPoint is a point in the execution flow where an Advice can be applied.
Examples:
• Before a method runs
• After a method executes
4️ PointCut
A PointCut defines where an Advice should be applied.
It matches methods using expressions.
5️ Proxy
A Proxy is a class created dynamically by Spring AOP to apply Advice.
Spring uses dynamic proxies to apply aspects without modifying the original class.
Types of Proxies in Spring
********** 8 **********
--- page 9 ---
1. JDK Dynamic Proxy – Used when the target class implements an interface.
2. CGLIB Proxy – Used when the target class does not implement an
interface.
6️ Target Class
The Target Class is the actual class whose methods are advised (where AOP is
applied).
CO b Explain Spring MVC architecture & key annotations.   [10
-1;   .   ]
SO-
7;
Spring MVC is based on the Servlet API, but it offers several enhancements that
BL-
make it easier to work with, especially in large-scale web applications.
4
How Spring MVC Handles Requests
Spring MVC Workflow (Request Flow)
1. Client sends HTTP request: The request could be a GET, POST, or any
other type of HTTP request.
2. DispatcherServlet intercepts the request: The DispatcherServlet acts as
the front controller, receiving the request and forwarding it to the
appropriate handler.
3. HandlerMapping determines the appropriate controller: It matches the
incoming request to a specific controller method based on URL patterns,
annotations, or other configurations.
4. Controller processes the request: The controller performs the business
logic, updates the model, and returns a ModelAndView object (or just a
model).
********** 9 **********
--- page 10 ---
5. ViewResolver resolves the view: The logical view name returned by the
controller is resolved by the ViewResolver to an actual view (e.g., JSP or
Thymeleaf).
6. View renders the response: The view takes the model data and renders it
(e.g., as HTML) to be sent back to the client.
7. Response sent to the client: The rendered response is sent back to the
client (browser).
Key Annotations in Spring MVC
Spring MVC Annotations Overview
1. @Controller:
• Used to define a class as a controller. It is a specialization of
@Component, allowing Spring to automatically detect it via component
scanning.
2. @RequestMapping:
• Maps an HTTP request to a specific method in a controller.
•   It can be applied to methods or classes to map the URL pattern and
request type (GET, POST, etc.).
3. @GetMapping, @PostMapping, @PutMapping, @DeleteMapping:
• These are specialized versions of @RequestMapping used for specific
HTTP methods:
• @GetMapping: For GET requests
• @PostMapping: For POST requests
• @PutMapping: For PUT requests
• @DeleteMapping: For DELETE requests
4. @RequestParam:
Used to bind HTTP request parameters to method parameters.
Q5
CO   a. What is hibernate & key feature? what are the different types of association   [10
-2;   mapping supported by hibernate with example.   ]
SO-
7;   Hibernate is a Java-based ORM (Object-Relational Mapping) framework that
BL-   simplifies database interactions by mapping Java objects to database tables. It
3   eliminates the need for complex JDBC code and provides automatic SQL
generation.
Key Features of Hibernate
********** 10 **********
--- page 11 ---
ORM (Object-Relational Mapping) – Maps Java objects to database tables.
HQL (Hibernate Query Language) – Allows writing queries independent of the
database.
First & Second-Level Caching – Improves performance by reducing database calls.
Automatic Table Creation – Uses hbm2ddl.auto to create/update tables
automatically.
Lazy & Eager Loading – Controls data fetching strategy.
Transaction Management – Supports ACID transactions and integrates with
Spring.
Cross-Database Support – Works with MySQL, PostgreSQL, Oracle, etc.
Types of Association Mapping in Hibernate
Hibernate supports four types of associations:
1. One-to-One (@OneToOne)
2. One-to-Many (@OneToMany) & Many-to-One (@ManyToOne)
3. Many-to-Many (@ManyToMany)
CO b Inversion of Control (IoC) is a design principle where the control of object   [5]
-1;   .   creation and management is transferred from the programmer to the Spring
SO-   container.
7;   Instead of creating objects using new, Spring manages them.
BL-
3   class Car {
Engine engine = new PetrolEngine(); // tightly coupled
}
Problems:
• Tight coupling
• Hard to change implementation
•   Difficult to test
Dependency Injection (DI) is a technique to achieve IoC where dependencies are
provided (injected) from outside instead of creating them inside the class.
class Car {
Engine engine;
public Car(Engine engine) {
this.engine = engine;
}
}
Feature   Without IoC/DI   With IoC/DI
Object creation Manual (new)   Managed by Spring
Coupling   Tight   Loose
Flexibility   Low   High
Testing   Difficult   Easy
CO   c. JDBC (Java Database Connectivity) is a low-level API used to interact with   [5]
-2;   databases using SQL.
SO-   Hibernate is an ORM (Object Relational Mapping) framework that simplifies
7;   database operations by mapping Java objects to database tables.
BL-   Problem with JDBC
4   In JDBC, developers must:
********** 11 **********
--- page 12 ---
• Write SQL queries manually
• Handle connections, statements, result sets
• Convert table data into Java objects
Leads to more code, errors, and maintenance issues
Feature   JDBC   Hibernate
Level   Low-level API   High-level ORM
SQL Handling   Manual SQL   Automatic (HQL/ORM)
Boilerplate Code   High   Very less
Mapping   Manual   Automatic
Portability   Database dependent   Database independent
Caching   Not available   1st & 2nd level cache
Performance   Slower (more DB calls) Faster (caching)
Transaction Management Manual   Built-in
Maintainability   Difficult   Easy
Hibernate is better than JDBC because it:
•   Simplifies database operations
• Reduces code complexity
• Improves performance
• Provides better maintainability
Q6
CO   a. The DAO design pattern is used to separate data access logic from business   [10
-2;   logic.   ]
SO-   Why DAO is Needed
7;   Without DAO:
BL-   • Business logic directly interacts with DB
3   • Tight coupling
• Hard to maintain
With DAO:
• Clean separation
• Easy to modify DB logic
• Better maintainability
Controller → Service → DAO → Database
Components of DAO Pattern
1. DAO Interface
o Defines methods (CRUD)
2. DAO Implementation
o Contains actual DB logic
3. Entity / Model
o Java class mapped to table
4. Service Layer
o Uses DAO
public interface EmployeeDAO {
void save(Employee emp);
Employee getById(int id);
}
public class EmployeeDAOImpl implements EmployeeDAO {
public void save(Employee emp) {
// JDBC/Hibernate logic
}
********** 12 **********
--- page 13 ---
public Employee getById(int id) {
return null;
}
}
Advantages of DAO Pattern
• Separation of concerns
• Loose coupling
• Easy testing
• Reusability
• Maintainability
CO b Explain Spring Framework and modules.   [10
-4;   .   ]
SO-   Spring is a powerful, lightweight, and modular Java framework used for building
7;   enterprise applications. It simplifies Java development by providing:
BL-   Dependency Injection (DI) for better modularity.
3   Aspect-Oriented Programming (AOP) for handling cross-cutting concerns.
Transaction Management for database operations.
Integration with ORM frameworks like Hibernate.
Key Features of Spring Framework
1️ Dependency Injection (DI)
• Spring manages object dependencies automatically.
• Reduces tight coupling between components.
• Uses @Autowired annotation for injecting dependencies.
2️ Aspect-Oriented Programming (AOP)
• Helps separate business logic from cross-cutting concerns (logging, security,
etc.).
• Uses @Aspect and @Around annotations.
3️ Transaction Management
• Ensures data consistency in database operations.
• Uses @Transactional annotation.
4️ Spring MVC (Model-View-Controller)
• Helps build web applications in a structured way.
• Handles HTTP requests, responses, and views.
Spring Framework Modules
Spring is modular, meaning you can use only the parts you need.
Module   Purpose
Spring Core   Provides Dependency Injection (DI)
Spring AOP   Aspect-Oriented Programming (AOP)
Spring MVC   Web applications (REST APIs, JSP, Thymeleaf)
Spring Data JPA Database integration with Hibernate
********** 13 **********
--- page 14 ---
Spring Security Authentication & Authorization
Spring Boot   Simplifies Spring app development
Spring Cloud   Microservices support (Eureka, Feign, Zuul)
Q7
CO   a. What is session tracking. Explain the way of session tracking with syntax &   [10
-5;   example.   ]
SO-
6;   Http protocol is a stateless so we need to maintain state using session tracking
BL-   techniques. Each time user requests to the server, server treats the request as
2   the new request.
HTTP is stateless that means each request is considered as the new request.
Dynamic applications are built on the assumption that the same client accesses
the application multiple times.
Client data is lost with every request being considered as a new request.
Session Tracking Techniques
There are four techniques used in Session tracking:
• Cookies
• Hidden Form Field
• URL Rewriting
• HttpSession
• Cookie
A cookie is a small piece of textual information sent by the server to the client,
stored on the client, and returned by the client for all requests to the server.
• Stores data on the client-side (user's browser).
• Less secure than sessions for sensitive information (due to potential
theft).
• Cookie ck=new Cookie("user","kumar");//creating cookie object
• response.addCookie(ck);//adding cookie in the response
URL Rewriting
// (Pseudocode, not recommended for real applications)
String sessionId = request.getSession().getId();
String targetUrl = "welcome.jsp?sessionid=" + sessionId;
response.sendRedirect(targetUrl);
Advantage of URL Rewriting
1. It will always work whether cookie is disabled or not (browser
independent).
2. Extra form submission is not required on each pages.
Disadvantage of URL Rewriting
1. It will work only with links.
2. It can send Only textual information.
3. 1 Static page in the cycle cannot be the part of url rewriing
4. 2 User Book marks the Url
URL Rewriting
// (Pseudocode, not recommended for real applications)
String sessionId = request.getSession().getId();
String targetUrl = "welcome.jsp?sessionid=" + sessionId;
response.sendRedirect(targetUrl);
Advantage of URL Rewriting
1. It will always work whether cookie is disabled or not (browser
independent).
********** 14 **********
--- page 15 ---
2. Extra form submission is not required on each pages.
Disadvantage of URL Rewriting
1. It will work only with links.
2. It can send Only textual information.
3. 1 Static page in the cycle cannot be the part of url rewriing
4. 2 User Book marks the Url
CO b A Servlet is a Java class used to handle client requests and generate dynamic   [10
-2;   .   responses in web applications.   ]
SO-   Client (Browser)
5;   ↓
BL-   Web Server
3   ↓
Servlet Container (Tomcat)
↓
Servlet
↓
Database / Business Logic
↓
Response → Client
Key Points (Very Important for Exam)
•   Servlet is managed by container (Tomcat)
•   init() → called once
•   service() → called multiple times
•   destroy() → called once
• Supports multithreading (handles multiple requests)
Advantages of Servlet
• High performance
• Platform independent
• Handles multiple requests efficiently
• Secure and scalable
Servlet architecture defines how:
• Client request flows through container
•   Servlet processes request
• Response is sent back
Lifecycle ensures proper initialization, execution, and cleanup
Components of Servlet Architecture
1. Client (Browser)
• Sends HTTP request (GET/POST)
2. Web Server
• Receives request and forwards to servlet container
3. Servlet Container (e.g., Apache Tomcat)
• Manages servlet lifecycle
• Handles request/response
• Provides security & multithreading
4. Servlet
• Processes request
• Generates response
********** 15 **********
--- page 16 ---
5. Database / Business Logic
• Used for data processing
Initialization
• Method: init()
• Called only once
public void init() {
// initialization code
}
3. Request Processing
• Method: service()
• Calls doGet() / doPost()
protected void doGet(HttpServletRequest req, HttpServletResponse res) {
// handle request
}
Executed for each request
4. Destruction
• Method: destroy()
• Called once before servlet removal
public void destroy() {
// cleanup code
}
Servlet Life Cycle Flow (Write This)
Load → Init → Service → Destroy
********** 16 **********
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 57fa3c93d801

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_02/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Advanced Java/ANS_Advanced Java(703CO0E019)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 10 Jul 2026
- Text: text (16 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: Advanced Java
Date: 10 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 16 pages.
2. Answer to each new question to be started on a fresh page.
3. Question No. 1 is compulsory
4. Out of remaining questions, attempt any 4 questions
5. In all 5 questions to be attempted.
6. All questions carry equal marks
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary
Q1   Solve the following sub-questions.
CO-1;   a.   JSP   [5]
SO-7;   Feature   Servlet   (JavaServer   Spring MVC
BL-3   Pages)
Java class
Server-side
used to handle   Full MVC web
Definition   view
HTTP   framework
technology
requests
MVC
Controller   View
architecture
Type   (backend   (presentation
(Model + View
logic)   layer)
+ Controller)
Annotation-
Development   Pure Java
HTML + Java   based, clean
Style   code
separation
Complex
Easy &
Ease of Use   (manual   Easy for UI
structured
coding)
Code
Low   Medium   High
Maintainability
Separation of
Poor   Limited   Excellent
Concerns
High   Slightly slower
Optimized with
Performance   (compiled   (converted to
architecture
Java)   servlet)
Reusability   Low   Low   High
Rich features
Built-in
Minimal   Minimal   (validation, DI,
Features
AOP)
********** 1 **********
--- page 2 ---
Learning Curve Moderate   Easy   Moderate
CO-2;   b.   First-Level   [5]
SO-7;   Feature   Cache   Second-Level Cache
BL-4   Scope   Session level   SessionFactory level
Enabled by
Default   Needs configuration
default
Single session
Visibility   Across multiple sessions
only
Performance Fast   Faster (reduces DB hits globally)
Memory   External cache (Ehcache, Redis,
Storage
(Session)   etc.)
Lifetime   Till session ends   Till application runs / cache expiry
Sharing   Not shared   Shared
CO-1;   c.   What are the advantage of using Hibernate over JDBC.   [5]
SO-7;
BL-2   Simplified Code: Hibernate significantly reduces boilerplate
code required in JDBC, making the codebase cleaner and more
readable.
Advanced Mapping Features: Unlike JDBC, Hibernate fully
supports object-oriented features such as inheritance,
associations, and collections.
Transaction Management: Hibernate seamlessly handles
transaction management, requiring transactions for most
operations, which contrasts with JDBC's manual transaction
handling through commit and rollback.
Exception Handling: Hibernate abstracts boilerplate try-catch
blocks by converting JDBC's checked SQLExceptions into
unchecked JDBCException or HibernateException, simplifying
error handling.
Object-Oriented Query Language: HQL (Hibernate Query
Language) offers an object-oriented API, which aligns it more
with Java programming concepts than JDBC's need for native
SQL queries.
Caching for Performance: Hibernate's support for caching
enhances performance, a feature not available with JDBC, where
queries are directly executed without caching.
Database Synchronization: Hibernate can automatically
generate database tables, offering greater flexibility than JDBC,
which requires pre-existing tables.
Flexible Connection Management: Hibernate allows for both
JDBC-like connections and JNDI DataSource connections with
pooling, which is essential for enterprise applications and not
supported by JDBC.
********** 2 **********
--- page 3 ---
ORM Tool Independence: By supporting JPA annotations,
Hibernate-based applications are not tightly bound to Hibernate
and can switch ORM tools more easily than JDBC-based
applications, which are closely coupled with the database.
CO-1;   d.   Life Cycle of a Servlet (Servlet Life Cycle)   [5]
SO-7;   The web container maintains the life cycle of a servlet instance.
BL-3   Let's see the life cycle of the servlet:
1. Servlet class is loaded.
2. Servlet instance is created.
3. init method is invoked.
4. service method is invoked.
5. destroy method is invoked.
The ways to create a Servlet
There are three ways to create the servlet.
1.   By implementing the Servlet interface
2.   By inheriting the GenericServlet class
3.   By inheriting the HttpServlet class
Servlet Life
Feature   JSP Life Cycle
Cycle
Conversion   JSP → Servlet (extra step) No conversion
********** 3 **********
--- page 4 ---
Initialization
_jspInit()   init()
Method
Request Handling _jspService()   service()
Destruction
_jspDestroy()   destroy()
Method
Already
Compilation   Required (JSP compiled)
compiled
Slower (translation +
First Request   Faster
compile)
Complexity   More steps   Simpler
Usage   View (UI)   Controller (logic)
Q2
CO-2;   a.   What is JDBCTemplate ? what are the problems spring JDBC [10]
SO-7;   solves.
BL-3
Spring JDBC module, particularly through JdbcTemplate, solves
several common problems encountered in traditional JDBC
programming. Here are the primary issues it addresses:
1. Boilerplate Code for Resource Management
• Problem: Traditional JDBC requires a lot of boilerplate
code for managing resources such as Connection,
Statement, and ResultSet. You need to open connections,
handle exceptions, and close resources manually, which
increases the chance of errors (like resource leaks) and
makes the code harder to maintain.
•   Solution: Spring JDBC handles resource management for
you. It automatically manages the opening and closing of
database connections, statements, and result sets, and
ensures that these resources are cleaned up correctly even
in the case of errors.
Example of traditional JDBC:
Connection con = DriverManager.getConnection(...);
Statement stmt = con.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM users");
// Code to process the result set
con.close();
With Spring JDBC, this process is simplified and abstracted by
JdbcTemplate:
jdbcTemplate.query("SELECT * FROM users", new
UserRowMapper());
2. Exception Handling (SQLException)
********** 4 **********
--- page 5 ---
• Problem: JDBC uses SQLException, which is very
specific to SQL and database vendors. This means that
developers need to handle SQLException and map it to
more generic exceptions.
•   Solution: Spring wraps SQLException into a consistent
exception hierarchy using the DataAccessException class.
This allows you to handle database-related errors
uniformly, without worrying about the specifics of the
underlying database or SQL.
For example, JdbcTemplate throws a DataAccessException
instead of SQLException, which can be caught and handled in a
consistent manner:
try {
jdbcTemplate.query("SELECT * FROM users", new
UserRowMapper());
} catch (DataAccessException e) {
// Handle the error
}
3. Manual Mapping of Results
• Problem: When querying a database, developers need to
manually map the rows from the result set to Java objects.
This is often tedious and error-prone, especially if you're
working with large result sets or complex objects.
•   Solution: Spring JDBC provides the RowMapper interface
to map database rows to Java objects automatically. By
implementing RowMapper, you can simplify the process
of converting result sets into domain objects.
Example with RowMapper:
List<User> users = jdbcTemplate.query("SELECT * FROM
users", new UserRowMapper());
4. SQL Injection Protection
• Problem: Writing raw SQL queries with user input
directly can lead to SQL injection vulnerabilities, where
malicious users can manipulate SQL queries to gain
unauthorized access to the database.
•   Solution: Spring JDBC encourages the use of prepared
statements, which automatically handle user input as
parameters and prevent SQL injection. The use of
JdbcTemplate.update() and JdbcTemplate.query() with
parameterized queries ensures that user input is treated as
data, not executable code.
Example of preventing SQL injection:
String sql = "SELECT * FROM users WHERE id = ?";
********** 5 **********
--- page 6 ---
User user = jdbcTemplate.queryForObject(sql, new Object[]{id},
new UserRowMapper());
5. Transaction Management
• Problem: When executing multiple database operations
that need to be performed as a single transaction, it is easy
to make mistakes while managing transactions, especially
in complex scenarios.
•   Solution: Spring JDBC integrates with Spring's
transaction management system, allowing you to easily
handle both programmatic and declarative transactions.
You can define transactional boundaries using
@Transactional or via a programmatic approach, ensuring
that operations are either fully committed or rolled back in
case of errors.
Example with @Transactional:
@Transactional
public void transferMoney(int fromAccountId, int toAccountId,
double amount) {
// Perform money transfer operations, including database
updates
}
6. Batch Processing
• Problem: Executing multiple SQL operations (e.g.,
inserts, updates) individually can lead to performance
bottlenecks, especially for large datasets.
Solution: Spring JDBC provides support for batch processing
via JdbcTemplate.batchUpdate(), which allows you to execute a
batch of SQL statements in a single call, improving performance.
CO-3;   b.   Explain Spring Framework and Modules.   [10]
SO-7;
BL-3
Q3
CO-3;   a.   The ways to create a Servlet   [10]
SO-6;
********** 6 **********
--- page 7 ---
BL-3   There are three ways to create the servlet.
1.   By implementing the Servlet interface
2.   By inheriting the GenericServlet class
3.   By inheriting the HttpServlet class
<!DOCTYPE html>
<html>
<head>
<title>Form Submission</title>
</head>
<body>
<h2>Simple Form</h2>
<form action="FormServlet" method="post">
<label>Name:</label>
<input type="text" name="name" required><br><br>
<label>Email:</label>
<input type="email" name="email" required><br><br>
<input type="submit" value="Submit">
</form>
</body>
</html>
<%@ page language="java" contentType="text/html;
charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
<title>Form Submitted</title>
</head>
<body>
<h2>Form Submitted Successfully!</h2>
<p><strong>Name:</strong> ${requestScope.name}</p>
<p><strong>Email:</strong> ${requestScope.email}</p>
<a href="index.html">Go Back</a>
</body>
</html>
CO-3;   b.   Write a Hibernate Program to save Student having id, name   [10]
SO-7;   & address as property. write all files needed to run this
BL-3   program using MYSQL as DB.
HibernateStudentApp/
│── src/
│ ├── com/example/hibernate/
│ │ ├── Student.java
│ │ ├── HibernateUtil.java
│ │ ├── SaveStudent.java
│── resources/
│ ├── hibernate.cfg.xml
│── pom.xml (if using Maven)
********** 7 **********
--- page 8 ---
public class SaveStudent {
public static void main(String[] args) {
Session session =
HibernateUtil.getSessionFactory().openSession();
Transaction transaction = session.beginTransaction();
// Creating Student object
Student student = new Student("John Doe", "123 Main
Street");
// Saving Student
session.save(student);
transaction.commit();
session.close();
System.out.println("Student saved successfully!");
}
}
Q4
CO-2;   a.   Explain AOP flow & types of pointcut.   [10]
SO-7;
BL-4
Aspect-Oriented Programming (AOP) is a programming
paradigm that helps modularize cross-cutting concerns such
as logging, security, transactions, caching, and exception
handling. AOP allows separating these concerns from
business logic, improving code maintainability.
AOP Flow (Execution Flow in Spring AOP)
1. Join Point – A specific point in the execution flow of a
program (e.g., method execution, object creation).
2. Pointcut – A predicate (expression) that matches one
or more Join Points where advice should be applied.
3. Advice – The actual code that runs before, after, or
around a Join Point.
4. Aspect – A module that encapsulates Advice and
Pointcuts.
5. Weaving – The process of linking Aspects with the
target objects (Spring AOP supports runtime weaving).
Types of Pointcuts include execution, within, args, this,
target, and annotation-based pointcuts.
********** 8 **********
--- page 9 ---
@Aspect and @Pointcut help define AOP behavior in
Spring.
CO-1;   b.   Explain Spring MVC architecture & key annotations.   [10]
SO-7;
BL-4   Spring MVC is based on the Servlet API, but it offers several
enhancements that make it easier to work with, especially in
large-scale web applications.
How Spring MVC Handles Requests
Spring MVC Workflow (Request Flow)
1. Client sends HTTP request: The request could be a GET,
POST, or any other type of HTTP request.
2. DispatcherServlet intercepts the request: The
DispatcherServlet acts as the front controller, receiving the
request and forwarding it to the appropriate handler.
3. HandlerMapping determines the appropriate
controller: It matches the incoming request to a specific
controller method based on URL patterns, annotations, or
other configurations.
4. Controller processes the request: The controller
performs the business logic, updates the model, and
returns a ModelAndView object (or just a model).
5. ViewResolver resolves the view: The logical view name
returned by the controller is resolved by the ViewResolver
to an actual view (e.g., JSP or Thymeleaf).
6. View renders the response: The view takes the model
data and renders it (e.g., as HTML) to be sent back to the
client.
7. Response sent to the client: The rendered response is sent
back to the client (browser).
Key Annotations in Spring MVC
********** 9 **********
--- page 10 ---
Spring MVC Annotations Overview
1. @Controller:
• Used to define a class as a controller. It is a specialization
of @Component, allowing Spring to automatically detect
it via component scanning.
2. @RequestMapping:
• Maps an HTTP request to a specific method in a
controller.
•   It can be applied to methods or classes to map the URL
pattern and request type (GET, POST, etc.).
3. @GetMapping, @PostMapping, @PutMapping,
@DeleteMapping:
• These are specialized versions of @RequestMapping used
for specific HTTP methods:
o @GetMapping: For GET requests
o @PostMapping: For POST requests
o @PutMapping: For PUT requests
o @DeleteMapping: For DELETE requests
4. @RequestParam:
Used to bind HTTP request parameters to method parameters.
Q5
CO-2;   a.   Explain Bean & creation of bean & lifecycle.   [10]
SO-7;
BL-3   A Bean in Java (specifically in Spring and Java EE) is an
object that is managed by a container, such as the Spring
Framework. It is a reusable software component that follows
specific conventions:
1. It must have a public no-argument constructor.
2. It must have getter and setter methods for accessing
properties.
Instantiation: Spring container creates an instance of the
bean.
Property Population: Dependencies are injected (via
constructor, setter, or autowiring).
Initialization:
•   If the bean implements InitializingBean,
afterPropertiesSet() is called.
•   If an init-method is specified, it is executed.
•   If @PostConstruct is used, that method runs.
Ready to Use: The bean is now fully initialized and
available for use.
Destruction:
•   If DisposableBean is implemented, destroy() is called.
•   If a destroy-method is specified, it is executed.
********** 10 **********
--- page 11 ---
•   If @PreDestroy is used, that method runs before the
bean is destroyed.
CO-1;   b.   Tight coupling means classes are highly dependent on each   [5]
SO-7;   other, so a change in one class affects others.
BL-3   Spring reduces tight coupling using:
• Inversion of Control (IoC)
• Dependency Injection (DI)
class Car {
Engine engine = new PetrolEngine(); // tightly coupled
}
Issues:
• Cannot change engine type easily
• Hard to test
• Not flexible
Sol:
class Car {
Engine engine;
public Car(Engine engine) {
this.engine = engine;
}
}
How Spring Works
1. Objects are created by Spring Container
2. Dependencies are injected externally
3. Classes do not create their own dependencies
This is called Dependency Injection
Key Concepts Used
1. Inversion of Control (IoC)
• Control of object creation is transferred to Spring
• Developer does not use new keyword
2. Dependency Injection (DI)
• Dependencies are injected via:
o Constructor
o Setter
o Field
Feature   Tight Coupling Loose Coupling (Spring)
Dependency   Hard-coded   Injected
Flexibility   Low   High
Testing   Difficult   Easy
Maintainability Poor   Excellent
CO-2;   c.   JSTL is a collection of standard tags used in JSP to simplify   [5]
SO-7;   development by replacing Java code with custom tags.
BL-4
********** 11 **********
--- page 12 ---
-It helps in writing clean, readable, and maintainable JSP
pages without using scriptlets.
Advantages of JSTL
1. Eliminates Scriptlets
• No need for <% %> Java code
• Makes JSP clean
2. Improves Readability
• Easy to understand for developers and designers
3. Easy Maintenance
• Separation of business logic and presentation
4. Reduces Code Complexity
• Less boilerplate Java code
5. Supports MVC Architecture
• Keeps JSP as view only
6. Reusable & Standardized
• Provided by Java EE standard
• No need to create custom tags manually
7. Built-in Functions
• Looping, conditions, formatting, string operations
Q6
CO-2;   a.   Explain Spring Framework & features.   [10]
SO-7;
BL-3
Spring is a powerful, lightweight, and modular Java
framework used for building enterprise applications. It
simplifies Java development by providing:
Dependency Injection (DI) for better modularity.
Aspect-Oriented Programming (AOP) for handling cross-
cutting concerns.
Transaction Management for database operations.
Integration with ORM frameworks like Hibernate.
Key Features of Spring Framework
1️ Dependency Injection (DI)
• Spring manages object dependencies automatically.
• Reduces tight coupling between components.
• Uses @Autowired annotation for injecting
dependencies.
********** 12 **********
--- page 13 ---
2️ Aspect-Oriented Programming (AOP)
• Helps separate business logic from cross-cutting
concerns (logging, security, etc.).
• Uses @Aspect and @Around annotations.
3️ Transaction Management
• Ensures data consistency in database operations.
• Uses @Transactional annotation.
4️ Spring MVC (Model-View-Controller)
• Helps build web applications in a structured way.
• Handles HTTP requests, responses, and views.
Spring Framework Modules
Spring is modular, meaning you can use only the parts you
need.
Module   Purpose
Spring Core   Provides Dependency Injection (DI)
Spring AOP   Aspect-Oriented Programming (AOP)
Web applications (REST APIs, JSP,
Spring MVC
Thymeleaf)
Spring Data
Database integration with Hibernate
JPA
Spring Security Authentication & Authorization
Spring Boot   Simplifies Spring app development
Spring Cloud   Microservices support (Eureka, Feign, Zuul)
CO-4;   b. What is hibernate & key feature? what are the different types   [10]
SO-7;   of association mapping supported by hibernate with example.
BL-3
Hibernate is a Java-based ORM (Object-Relational Mapping)
framework that simplifies database interactions by mapping Java
objects to database tables. It eliminates the need for complex
JDBC code and provides automatic SQL generation.
Key Features of Hibernate
ORM (Object-Relational Mapping) – Maps Java objects to
database tables.
HQL (Hibernate Query Language) – Allows writing queries
independent of the database.
First & Second-Level Caching – Improves performance by
reducing database calls.
Automatic Table Creation – Uses hbm2ddl.auto to
create/update tables automatically.
Lazy & Eager Loading – Controls data fetching strategy.
Transaction Management – Supports ACID transactions and
integrates with Spring.
********** 13 **********
--- page 14 ---
Cross-Database Support – Works with MySQL, PostgreSQL,
Oracle, etc.
Types of Association Mapping in Hibernate
Hibernate supports four types of associations:
1. One-to-One (@OneToOne)
2. One-to-Many (@OneToMany) & Many-to-One
(@ManyToOne)
3. Many-to-Many (@ManyToMany)
Q7
CO-5;   a.   What is Caching in Hibernate? Explain the different level of   [10]
SO-6;   caching supported by Hibernate.
BL-2
Caching in Hibernate improves application performance by
reducing database queries. It stores frequently accessed data
in memory, minimizing unnecessary database interactions.
Hibernate supports two levels of caching:
1. First-Level Cache (Session-Level)
2. Second-Level Cache (SessionFactory-Level)
Additionally, Hibernate supports Query Cache for caching
query results.
1️ First-Level Cache (Session Cache)
• Enabled by default (No configuration needed).
• Works at the Session level.
• Data is stored in the Session object and remains cached
until the session is closed.
• Each Hibernate session has its own isolated cache.
•   If an entity is queried multiple times within the same
session, Hibernate does not hit the database again.
2️ Second-Level Cache (SessionFactory Cache)
• Works across multiple sessions (shared cache).
• Disabled by default (must be explicitly configured).
• Uses external cache providers such as:
o EHCache
o OSCache
o Infinispan
o Hazelcast
CO-2;   b. What is session tracking. Explain the way of session tracking   [10]
SO-5;   with syntax & example.
BL-3
Http protocol is a stateless so we need to maintain state using
session tracking techniques. Each time user requests to the server,
server treats the request as the new request.
HTTP is stateless that means each request is considered as the
new request.
Dynamic applications are built on the assumption that the same
client accesses the application multiple times.
********** 14 **********
--- page 15 ---
Client data is lost with every request being considered as a new
request.
Session Tracking Techniques
There are four techniques used in Session tracking:
1. Cookies
2. Hidden Form Field
3. URL Rewriting
4. HttpSession
1. Cookie
A cookie is a small piece of textual information sent by the server
to the client, stored on the client, and returned by the client for all
requests to the server.
•   Stores data on the client-side (user's browser).
• Less secure than sessions for sensitive information (due to
potential theft).
How to create Cookie?
Let's see the simple code to create cookie.
Cookie ck=new Cookie("user","kumar");//creating cookie object
response.addCookie(ck);//adding cookie in the response
URL Rewriting
// (Pseudocode, not recommended for real applications)
String sessionId = request.getSession().getId();
String targetUrl = "welcome.jsp?sessionid=" + sessionId;
response.sendRedirect(targetUrl);
Advantage of URL Rewriting
1. It will always work whether cookie is disabled or not
(browser independent).
2. Extra form submission is not required on each pages.
Disadvantage of URL Rewriting
1. It will work only with links.
2. It can send Only textual information.
Hidden Form Fields in HTML
********** 15 **********
--- page 16 ---
In this approach the unique token is embedded within each
HTML form. For example
<input type=”Hidden” name=”uid” value=”dac”>
********** 16 **********
````

## 2024-25 · Re-Exam · Sem 2 · Answer key · paper ba7944cf07d0

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_02/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Advanced Java/ANS_Advanced Java(703CO0E019)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Jul 2025
- Text: text (17 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 2 Re-exam(Exam Year: 2024-2025)
Subject: Advanced Java
Date: 02 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 17 pages.
2. Answer to each new question to be started on a fresh page.
3. Question No. 1 is compulsory
4. Out of remaining questions, attempt any 4 questions
5. In all 5 questions to be attempted.
6. All questions carry equal marks
7. Figure in right hand side indicates full marks
8. Assume Suitable data if necessary
Q1   Solve the following sub-questions.
CO   a. What is Servlet? Difference between GET & POST   [5]
-1;
SO-   A Servlet is a Server Side Java program which extends the functionality of web
7;   application.
BL-
3   It is used to create dynamics web pages.
Key Features of Java Servlets:
• Platform Independence: Written in Java, servlets are platform-independent,
ensuring compatibility across various operating systems.
•   Efficiency: Unlike CGI scripts, servlets run within the server's process,
eliminating the need to create a new process for each request, which enhances
performance.
Robustness: Leveraging Java's strong typing and exception handling, servlets
provide a robust environment for web applications.
GET   POST
1) In case of Get request, only limited   In case of post request, large
amount of data can be sent because data   amount of data can be sent
is sent in header.   because data is sent in body.
We can send text & binary
2)We can send only text data.
data.
3) It not secured because data is exposed   It is more secured because data is
in URL bar.   not exposed in URL bar.
********** 1 **********
--- page 2 ---
4) Get request can be bookmarked   Post request cannot be
bookmarked
5) Get request is idempotent. It means   Post request is non-idempotent
second request will be ignored until
response of first request is delivered.
6) Get request is more efficient and used   Post request is less efficient and
more than Post   used less than get.
CO b Explain Hibernate & what are the advantage of using Hibernate.   [5]
-2;   .
SO-   Hibernate is a Java-based ORM (Object-Relational Mapping) framework that
7;   simplifies database interactions by mapping Java objects to database tables.
BL-   It eliminates the need for manual JDBC code and SQL queries, making database
4   operations more efficient and maintainable. Hibernate is widely used in enterprise
applications for data persistence.
Advantages of Using Hibernate
1   . Simplifies Database Interaction
• Hibernate automatically translates Java objects to database tables.
• No need to write complex SQL queries or manage ResultSets manually.
2️ Database Independence
• Hibernate uses HQL (Hibernate Query Language), which is database-
independent.
• You can switch between databases without modifying your queries.
3️ Automatic Table Creation (DDL Operations)
• Hibernate can automatically create/update database tables.
• No need to manually write CREATE TABLE statements.
4️ Caching for Better Performance
CO   c. What are the different modules in a Spring.   [5]
-1;
SO-   Spring Framework consists of the following core modules:
7;   Module   Purpose
BL-
Provides Dependency Injection (DI) and IoC
2   1️ Spring Core & Beans
(Inversion of Control).
2️ Spring AOP (Aspect-   Used for cross-cutting concerns (e.g., logging,
Oriented Programming)   security, transactions).
Provides ApplicationContext for managing
3️ Spring Context
beans.
Simplifies database access and integrates with
4️ Spring JDBC & ORM
Hibernate, JPA, MyBatis.
5️ Spring MVC (Web Module) Used for web applications & REST APIs.
********** 2 **********
--- page 3 ---
Provides authentication, authorization, and
6️ Spring Security
protection against threats.
Simplifies Spring configuration and provides
7️ Spring Boot
auto-configuration.
Simplifies database interactions with Spring Data
8️ Spring Data
JPA, MongoDB, Redis, etc.
Supports Microservices Architecture (Eureka,
9️ Spring Cloud
Feign, Zuul, etc.).
10 Spring Test   Supports unit & integration testing.
CO d What is Spring boot, solve challenges which exist with Spring MVC.   [5]
-1;   .
SO-
7;   Spring Boot is a framework built on top of Spring Framework that simplifies
BL-   application development by eliminating boilerplate configurations.
3   It provides:
Auto-configuration – No need for manual XML or Java-based configurations.
Embedded Servers – Comes with Tomcat, Jetty, and Undertow.
Microservices Support – Helps in building scalable applications.
Spring Boot Starters – Pre-configured dependencies for different features.
1️ Complex Configuration in Spring MVC
2️ Dependency Management Issues
3️ No Embedded Server in Spring MVC
4 REST API Development Requires Extra Configuration
Q2
CO   a. What is JDBCTemplate & advantage and key components with example.   [10
-2;   ]
SO-   Spring JDBC is part of the Spring Framework and provides a simple, consistent way
7;   to interact with relational databases using JDBC (Java Database Connectivity) while
BL-   removing much of the boilerplate code that developers typically need to write when
3   using JDBC directly. Spring JDBC provides both a low-level and high-level API,
simplifying the process of working with databases.
Here are some key notes on Spring JDBC:
1. Key Components
• JdbcTemplate: The core class in Spring JDBC that simplifies database
interactions. It provides methods to execute SQL queries, update statements,
and stored procedures. It automatically handles resource management (like
closing connections and handling exceptions).
• NamedParameterJdbcTemplate: A subclass of JdbcTemplate that allows for
the use of named parameters in SQL queries instead of the traditional?
placeholders.
• SimpleJdbcCall: A helper class for calling stored procedures in a simpler
way.
• DataSource: Represents a connection pool or a factory for database
connections. Spring allows you to configure different types of data sources
like HikariCP, Apache DBCP, etc.
********** 3 **********
--- page 4 ---
2. Common Operations
• Query Execution: Use JdbcTemplate.query() for queries that return a result
set and JdbcTemplate.update() for operations like INSERT, UPDATE, or
DELETE.
• Query for Objects: Use JdbcTemplate.queryForObject() when you expect a
single result and JdbcTemplate.queryForList() when you expect multiple
results.
• RowMapper: When using methods like query(), a RowMapper is used to map
rows of a result set to Java objects.
• PreparedStatementSetter: To set parameters on a prepared statement.
3. Spring JDBC Exceptions
• Spring provides a consistent exception hierarchy for handling database errors,
via the DataAccessException class. This eliminates the need for handling
different SQL exceptions (like SQLException) explicitly.
SQLErrorCodesTranslator: Helps map specific database error codes to exceptions
that can be more easily handled by the application.
CO b What is HQL, HCQL? Write the syntax to demonstrate the basic Crud   [10
-3;   .   operation using HQL.   ]
SO-
7;   HQL is designed to query the object model and not the relational model, making it
BL-   database-independent and more aligned with the application's object-oriented nature.
3
Key Features of HQL
• Object-Oriented: Queries are written in terms of the entity model, not the
database schema.
• Database Independent: Queries are independent of the underlying database.
• Powerful and Flexible: Supports CRUD operations, joins, aggregations, and
subqueries.
Basic HQL Syntax
********** 4 **********
--- page 5 ---
HCQL
The criteria query API lets us build nested, structured query expressions in Java,
providing a compile-time syntax checking that is not possible with a query language
like HQL or SQL.
********** 5 **********
--- page 6 ---
1. The simplest example of a criteria query is one with no optional parameters or
restrictions—the criteria query will simply return every object that corresponds to the
class.
2. Using Restrictions
The Criteria API makes it easy to use restrictions in your queries to selectively
retrieve objects; for instance, your application could retrieve only products with a
price over $30. You may add these restrictions to a Criteria object with
the add() method.
Q3
CO   a. Explain the lifecycle of Servlet with diagram. Write a simple form submission   [10
-3;   using servlet.   ]
SO-
6;   Life Cycle of a Servlet (Servlet Life Cycle)
BL-   The web container maintains the life cycle of a servlet instance. Let's see the life
3   cycle of the servlet:
1. Servlet class is loaded.
2. Servlet instance is created.
3. init method is invoked.
4. service method is invoked.
5. destroy method is invoked.
********** 6 **********
--- page 7 ---
The ways to create a Servlet
There are three ways to create the servlet.
1.   By implementing the Servlet interface
2.   By inheriting the GenericServlet class
3.   By inheriting the HttpServlet class
<!DOCTYPE html>
<html>
<head>
<title>Form Submission</title>
</head>
<body>
<h2>Simple Form</h2>
<form action="FormServlet" method="post">
<label>Name:</label>
<input type="text" name="name" required><br><br>
<label>Email:</label>
<input type="email" name="email" required><br><br>
<input type="submit" value="Submit">
</form>
</body>
</html>
********** 7 **********
--- page 8 ---
<%@ page language="java" contentType="text/html; charset=UTF-8"
pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
<title>Form Submitted</title>
</head>
<body>
<h2>Form Submitted Successfully!</h2>
<p><strong>Name:</strong> ${requestScope.name}</p>
<p><strong>Email:</strong> ${requestScope.email}</p>
<a href="index.html">Go Back</a>
</body>
</html>
CO b Write a Simple REST API coding with all needed file like controller, service,   [10
-3;   .   repo for insert & get all students. [annotation is mandatory]   ]
SO-
7;
BL-   @Entity
3   @Table(name = "students")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class Student {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
@Column(nullable = false)
private String name;
@Column(nullable = false, unique = true)
private String email;
}
@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {
}.
@Service
public class StudentService {
@Autowired
private StudentRepository studentRepository;
********** 8 **********
--- page 9 ---
// Insert a new student
public Student saveStudent(Student student) {
return studentRepository.save(student);
}
// Retrieve all students
public List<Student> getAllStudents() {
return studentRepository.findAll();
}
}
@RestController
@RequestMapping("/students")
public class StudentController {
@Autowired
private StudentService studentService;
// Insert a new student
@PostMapping
public Student createStudent(@RequestBody Student student) {
return studentService.saveStudent(student);
}
// Get all students
@GetMapping
public List<Student> getAllStudents() {
return studentService.getAllStudents();
}
}
Q4
CO   a. What is AOP. Explain the following what are the types of Advice?   [10
-2;   1.Advice   ]
SO-   2.Aspect
7;   3.JointPoint
BL-   4.PointCut
4   5.Proxy
6.TargetClass
AOP (Aspect-Oriented Programming) is a programming paradigm that allows us to
separate cross-cutting concerns (such as logging, security, and transaction
management) from business logic.
Spring AOP helps in applying additional behavior (advice) to certain parts of the
application without modifying the actual code.
1️ Advice
Advice is the action taken when a specific event occurs in the application.
It defines what should happen and runs at different points of method execution.
2️ Aspect
An Aspect is a class that contains multiple Advices to apply cross-cutting concerns
like logging, security, and transactions.
********** 9 **********
--- page 10 ---
3️ JoinPoint
A JoinPoint is a point in the execution flow where an Advice can be applied.
Examples:
• Before a method runs
• After a method executes
4️ PointCut
A PointCut defines where an Advice should be applied.
It matches methods using expressions.
5️ Proxy
A Proxy is a class created dynamically by Spring AOP to apply Advice.
Spring uses dynamic proxies to apply aspects without modifying the original class.
Types of Proxies in Spring
1. JDK Dynamic Proxy – Used when the target class implements an interface.
2. CGLIB Proxy – Used when the target class does not implement an
interface.
6️ Target Class
The Target Class is the actual class whose methods are advised (where AOP is
applied).
CO b What is session tracking. Explain the way of session tracking with syntax &   [10
-1;   .   example.   ]
SO-
7;
BL-   Http protocol is a stateless so we need to maintain state using session tracking
4   techniques. Each time user requests to the server, server treats the request as the new
request.
HTTP is stateless that means each request is considered as the new request.
Dynamic applications are built on the assumption that the same client accesses the
application multiple times.
Client data is lost with every request being considered as a new request.
Session Tracking Techniques
There are four techniques used in Session tracking:
• Cookies
• Hidden Form Field
• URL Rewriting
• HttpSession
• Cookie
A cookie is a small piece of textual information sent by the server to the client, stored
on the client, and returned by the client for all requests to the server.
•   Stores data on the client-side (user's browser).
• Less secure than sessions for sensitive information (due to potential theft).
********** 10 **********
--- page 11 ---
• Cookie ck=new Cookie("user","kumar");//creating cookie object
•   response.addCookie(ck);//adding cookie in the response
URL Rewriting
// (Pseudocode, not recommended for real applications)
String sessionId = request.getSession().getId();
String targetUrl = "welcome.jsp?sessionid=" + sessionId;
response.sendRedirect(targetUrl);
Advantage of URL Rewriting
1. It will always work whether cookie is disabled or not (browser independent).
2. Extra form submission is not required on each pages.
Disadvantage of URL Rewriting
1. It will work only with links.
2. It can send Only textual information.
3. 1 Static page in the cycle cannot be the part of url rewriing
4. 2 User Book marks the Url
URL Rewriting
// (Pseudocode, not recommended for real applications)
String sessionId = request.getSession().getId();
String targetUrl = "welcome.jsp?sessionid=" + sessionId;
response.sendRedirect(targetUrl);
Advantage of URL Rewriting
1. It will always work whether cookie is disabled or not (browser independent).
2. Extra form submission is not required on each pages.
Disadvantage of URL Rewriting
1. It will work only with links.
2. It can send Only textual information.
3. 1 Static page in the cycle cannot be the part of url rewriing
4. 2 User Book marks the Url
Q5
CO   a. What is hibernate & key feature? what are the different types of association   [10
-2;   mapping supported by hibernate with example.   ]
SO-
7;   Hibernate is a Java-based ORM (Object-Relational Mapping) framework that
BL-   simplifies database interactions by mapping Java objects to database tables. It
3   eliminates the need for complex JDBC code and provides automatic SQL
generation.
********** 11 **********
--- page 12 ---
Key Features of Hibernate
ORM (Object-Relational Mapping) – Maps Java objects to database tables.
HQL (Hibernate Query Language) – Allows writing queries independent of the
database.
First & Second-Level Caching – Improves performance by reducing database calls.
Automatic Table Creation – Uses hbm2ddl.auto to create/update tables
automatically.
Lazy & Eager Loading – Controls data fetching strategy.
Transaction Management – Supports ACID transactions and integrates with
Spring.
Cross-Database Support – Works with MySQL, PostgreSQL, Oracle, etc.
Types of Association Mapping in Hibernate
Hibernate supports four types of associations:
1. One-to-One (@OneToOne)
2. One-to-Many (@OneToMany) & Many-to-One (@ManyToOne)
3. Many-to-Many (@ManyToMany)
CO b what are the challenges solved by Spring framework which exist with Servlet?   [5]
-1;   .
SO-   Challenges in Servlet-Based Development
7;   Challenge   Explanation   Spring Solution
BL-
Developers had to manually
3   Spring provides Spring MVC &
handle request/response,
Boilerplate Code   Spring Data JPA to reduce
session management, and
boilerplate code.
database connections.
Servlets, JSPs, and business   Dependency Injection (DI)
Tightly Coupled
logic were tightly coupled,   and Inversion of Control (IoC)
Components
making changes difficult.   enable loose coupling.
Developers had to manually
Difficult Object   Spring IoC Container manages
manage Java objects (service
Management   objects automatically.
classes, DAOs, etc.).
Servlets required manually   Spring @RequestMapping &
Manual Request
parsing GET/POST requests   @RestController handle
Processing
and setting response headers.   request mapping automatically.
Servlets required web.xml-   Spring uses Java-based
Hardcoded
based configurations, which   Configuration & Annotations
Configurations
were difficult to manage.   (@Configuration, @Bean).
In servlets, developers had to   Spring provides Declarative
Transaction
manually manage transactions Transaction Management
Management
with JDBC.   (@Transactional).
Difficult   Developers had to manually   Spring provides
Exception   handle exceptions and error   @ExceptionHandler & Global
Handling   pages.   Exception Handling.
********** 12 **********
--- page 13 ---
Implementing authentication & Spring Security provides built-
No Built-in
authorization required extra   in authentication &
Security
coding.   authorization.
Spring provides Unit Testing &
Limited Testing Servlets required full
Mocking via @WebMvcTest
Support   deployment for testing.
and Mockito.
CO   c. Write a note on ORM & Hibernate Caching.   [5]
-2;
SO-   Object-Relational Mapping (ORM) is a technique that allows developers to interact
7;   with a relational database using Java objects, without writing SQL queries manually.
BL-   Why ORM?
4
•   Eliminates manual SQL queries.
• Provides automatic mapping between Java objects and database tables.
• Ensures portability (works with different databases like MySQL,
PostgreSQL, etc.).
• Reduces boilerplate code for CRUD operations.
Popular ORM Tools:
• Hibernate (Most widely used in Java)
• JPA (Java Persistence API)
• MyBatis
• EclipseLink
Hibernate caching improves performance by reducing database queries. Instead of
hitting the database every time, Hibernate stores frequently accessed data in cache
memory.
Types of Caching in Hibernate
Hibernate supports two levels of caching:
Cache Level   Scope   Description
First-Level   Default cache, stores objects within a Hibernate
Per Session
Cache   Session.
Second-Level   Per   Stores objects across multiple sessions
Cache   SessionFactory   (Requires configuration).
Per   Caches query results to avoid repeated
Query Cache
SessionFactory   execution.
Q6
CO   a. Explain in detail IOC, DI & Autowiring.   [10
-2;   ]
SO-   Inversion of Control (IoC) is a design principle where the control of object
7;   creation and dependency management is transferred from the developer to the
BL-   Spring Container.
3   Without IoC:
• The developer manually creates and manages objects using the new
keyword.
• Leads to tight coupling between classes.
********** 13 **********
--- page 14 ---
• Hard to test and maintain.
With IoC (Spring):
• The Spring IoC Container creates and manages objects.
• Ensures loose coupling and better scalability.
• Uses Dependency Injection (DI) to provide objects.
2️⃣ Dependency Injection (DI)
📌 What is DI?
Dependency Injection (DI) is a technique where the Spring IoC Container injects
dependencies into a class at runtime instead of creating them manually.
Why Use DI?   Eliminates new keyword (manual object creation).
Promotes loose coupling between components.
Makes the application easier to test (can use mocks).
Supports modularity (easy to replace components).
Types of Dependency Injection in Spring
Spring supports three types of DI:
Type   Injection Method   Example
1. Constructor   Inject dependencies via
@Autowired on constructor
Injection   constructor
@Autowired on setter
2. Setter Injection   Inject dependencies via setters
method
Inject dependencies directly into @Autowired on instance
3. Field Injection
fields   variable
3️ Autowiring in Spring
📌 What is Autowiring?
Autowiring is a feature in Spring where the framework automatically injects
dependencies without manually creating objects using new.
Spring provides different types of autowiring to specify how dependencies should
be injected.
Types of Autowiring in Spring
Spring supports the following autowiring types:
Type   Description   Example Annotation
1.   Automatically injects a bean by
@Autowired
@Autowired type
Specifies which bean to inject if @Autowired
2. @Qualifier
multiple exist   @Qualifier("beanName")
Marks a bean as the default for
3. @Primary   @Primary
injection
CO b Explain Spring Framework and modules.   [10
-4;   .   ]
********** 14 **********
--- page 15 ---
SO-   Spring is a powerful, lightweight, and modular Java framework used for building
7;   enterprise applications. It simplifies Java development by providing:
BL-   Dependency Injection (DI) for better modularity.
3   Aspect-Oriented Programming (AOP) for handling cross-cutting concerns.
Transaction Management for database operations.
Integration with ORM frameworks like Hibernate.
Key Features of Spring Framework
1️ Dependency Injection (DI)
• Spring manages object dependencies automatically.
• Reduces tight coupling between components.
• Uses @Autowired annotation for injecting dependencies.
2️ Aspect-Oriented Programming (AOP)
• Helps separate business logic from cross-cutting concerns (logging, security,
etc.).
• Uses @Aspect and @Around annotations.
3️ Transaction Management
• Ensures data consistency in database operations.
• Uses @Transactional annotation.
4️ Spring MVC (Model-View-Controller)
• Helps build web applications in a structured way.
• Handles HTTP requests, responses, and views.
Spring Framework Modules
Spring is modular, meaning you can use only the parts you need.
Module   Purpose
Spring Core   Provides Dependency Injection (DI)
Spring AOP   Aspect-Oriented Programming (AOP)
Spring MVC   Web applications (REST APIs, JSP, Thymeleaf)
Spring Data JPA Database integration with Hibernate
Spring Security Authentication & Authorization
Spring Boot   Simplifies Spring app development
Spring Cloud   Microservices support (Eureka, Feign, Zuul)
Q7
CO   a. Explain Spring MVC architecture & key annotations.   [10
-5;   ]
SO-   Spring MVC is based on the Servlet API, but it offers several enhancements that
6;   make it easier to work with, especially in large-scale web applications.
BL-
2
********** 15 **********
--- page 16 ---
How Spring MVC Handles Requests
Spring MVC Workflow (Request Flow)
1. Client sends HTTP request: The request could be a GET, POST, or any
other type of HTTP request.
2. DispatcherServlet intercepts the request: The DispatcherServlet acts as the
front controller, receiving the request and forwarding it to the appropriate
handler.
3. HandlerMapping determines the appropriate controller: It matches the
incoming request to a specific controller method based on URL patterns,
annotations, or other configurations.
4. Controller processes the request: The controller performs the business logic,
updates the model, and returns a ModelAndView object (or just a model).
5. ViewResolver resolves the view: The logical view name returned by the
controller is resolved by the ViewResolver to an actual view (e.g., JSP or
Thymeleaf).
6. View renders the response: The view takes the model data and renders it
(e.g., as HTML) to be sent back to the client.
7. Response sent to the client: The rendered response is sent back to the client
(browser).
Key Annotations in Spring MVC
Spring MVC Annotations Overview
1. @Controller:
• Used to define a class as a controller. It is a specialization of @Component,
allowing Spring to automatically detect it via component scanning.
2. @RequestMapping:
• Maps an HTTP request to a specific method in a controller.
•   It can be applied to methods or classes to map the URL pattern and request
type (GET, POST, etc.).
********** 16 **********
--- page 17 ---
3. @GetMapping, @PostMapping, @PutMapping, @DeleteMapping:
• These are specialized versions of @RequestMapping used for specific HTTP
methods:
o @GetMapping: For GET requests
o @PostMapping: For POST requests
o @PutMapping: For PUT requests
o @DeleteMapping: For DELETE requests
4. @RequestParam:
Used to bind HTTP request parameters to method parameters.
CO b Explain Bean & creation of bean & lifecycle.   [10
-2;   .   ]
SO-   A Bean in Java (specifically in Spring and Java EE) is an object that is managed by a
5;   container, such as the Spring Framework. It is a reusable software component that
BL-   follows specific conventions:
3
1. It must have a public no-argument constructor.
2. It must have getter and setter methods for accessing properties.
Instantiation: Spring container creates an instance of the bean.
Property Population: Dependencies are injected (via constructor, setter, or
autowiring).
Initialization:
•   If the bean implements InitializingBean, afterPropertiesSet() is called.
•   If an init-method is specified, it is executed.
•   If @PostConstruct is used, that method runs.
Ready to Use: The bean is now fully initialized and available for use.
Destruction:
•   If DisposableBean is implemented, destroy() is called.
•   If a destroy-method is specified, it is executed.
•   If @PreDestroy is used, that method runs before the bean is destroyed.
********** 17 **********
````

## 2023-24 · Final-Exam · Sem 2 · Answer key · paper 9844944caebc

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2023/Sem_02/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Advanced Java/ANS_Advanced Java(703CO0E019)_2023-2024.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 19 Apr 2024
- Text: text (27 pages)

````text
Synoptic
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester II (Exam Year: 2023-2024)
Subject: Advanced Java
Date: 19 Apr 2024   Time: 10:00 am - 01:00 pm (03:00 Hrs.)
Max Marks:   100
FINAL EXAMINATION(2023-2024)
Instructions:
1. This Synoptic paper contains 27 pages
2. Answer to each new question to be started on a fresh page.
3. Question No. 1 is compulsory
4. Out of remaining questions, attempt any 4 questions
5. In all 5 questions to be attempted.
6. All questions carry equal marks
7. Figures in brackets on the right hand side indicate full marks
8. Assume Suitable data if necessary
1. 1 Answer briefly   20
A. Servlet life cycle:   5
1. Servlet class is loaded.
2. Servlet instance is created.
3. init method is invoked.
4. service method is invoked.
5. destroy method is invoked.
1) Servlet class is loaded
The classloader is responsible to load the servlet class. The servlet class is loaded when the first
request for the servlet is received by the web container.
2) Servlet instance is created
The web container creates the instance of a servlet after loading the servlet class. The servlet
instance is created only once in the servlet life cycle.
3) init method is invoked
The web container calls the init method only once after creating the servlet instance. The init
method is used to initialize the servlet. It is the life cycle method of the javax.servlet.Servlet
Page 1 of 27
--- page 2 ---
interface.
Syntax: public void init(ServletConfig config) throws ServletException
4) service method is invoked
The web container calls the service method each time when request for the servlet is received. If
servlet is not initialized, it follows the first three steps as described above then calls the service
method. If servlet is initialized, it calls the service method. Notice that servlet is initialized only
once. Syntax:public void service(ServletRequest request, ServletResponse response) throws
ServletException, IOException
5) destroy method is invoked
The web container calls the destroy method before removing the servlet instance from the
service. It gives the servlet an opportunity to clean up any resource for example memory, thread
etc.
syntax: public void destroy()
B. A Java Bean is a java class that should follow following conventions:   5
It should have a no-arg constructor.
It should be Serializable.
It should provide methods to set and get the values of the properties, known as getter and
setter methods.
A list of the 9 implicit objects is given below:
Object   Type
application   ServletContext
session   HttpSession
request   HttpServletRequest
response   HttpServletResponse
out   JspWriter
page   Object
pageContext   PageContext
config   ServletConfig
exception   Throwable
Page 2 of 27
--- page 3 ---
C.   5
Hibernate offers several advantages over JDBC:
1. Object-Relational Mapping (ORM): Hibernate provides a way to map Java objects to
database tables, reducing the need for manual mapping and making it easier to work
with object-oriented programming concepts.
2. Database Independence: Hibernate abstracts away the differences between various
databases, allowing developers to write code that is independent of the underlying
database system. This makes it easier to switch between different databases without
changing the application code.
3. Automatic Table Creation: Hibernate can automatically generate database tables based
on the entity classes, reducing the need for manual creation and maintenance of
database schemas.
4. Query Language: Hibernate Query Language (HQL) is an object-oriented query
language similar to SQL but operates on objects and their properties. HQL makes it
easier to write complex queries and perform operations on objects directly.
5. Caching: Hibernate provides a built-in caching mechanism that can improve
performance by reducing the number of database queries needed to fetch data. This can
lead to significant performance improvements, especially in applications with high
read-to-write ratios.
6. Transaction Management: Hibernate provides built-in support for transaction
management, making it easier to manage database transactions and ensuring data
integrity.
7. Lazy Loading: Hibernate supports lazy loading, which means that it loads data from
the database only when it is requested. This can improve performance by reducing the
amount of data loaded into memory at once.
Page 3 of 27
--- page 4 ---
8. Association Mapping: Hibernate provides a variety of ways to map associations
between entities, including one-to-one, one-to-many, and many-to-many relationships.
This makes it easier to represent complex relationships between objects in the database
D. The Spring Framework is a popular open-source framework for building enterprise-level Java   5
applications. It provides a comprehensive set of features designed to simplify development and
improve application maintainability.
Here's a breakdown of what Spring offers:
Dependency Injection: Spring promotes a dependency injection approach, where objects
don't create their own dependencies but are instead injected with them. This leads to loosely
coupled and more testable code.
Modular Design: Spring is a collection of modules that address various aspects of
application development, such as data access, web development, security, and more. You can
choose the modules you need for your project.
Configuration Management: Spring uses XML or Java annotations for configuration,
allowing you to define beans (managed objects) and their dependencies declaratively,
separating application logic from configuration details.
Aspect-Oriented Programming (AOP): Spring supports AOP, enabling you to implement
cross-cutting concerns like logging, security, and transaction management transparently
without modifying core application logic.
Transaction Management: Spring simplifies transaction management, allowing you to
define transactional boundaries and handle exceptions declaratively.
MVC (Model-View-Controller) Framework: Spring provides a robust MVC framework
(Spring MVC) for building web applications, separating business logic, data models, and
presentation layers.
2. 2 (Attempt Any 4 Questions)   80
1.   20
A. Index.html   10
<!DOCTYPE html>
<html>
Page 4 of 27
--- page 5 ---
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<form action="ArithmaticOperation" method="post">
First Number : <input type="text" name="num1"><br>
Second Number : <input type="text" name="num2"><br>
<input type="submit" name="submit" value="Submit">
</form>
</body>
</html>
ArithmaticOperation.java
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
public class ArithmaticOperation extends HttpServlet {
private static final long serialVersionUID = 1L;
protected void doPost(HttpServletRequest request, HttpServletResponse response) throws
ServletException, IOException {
int num1=Integer.parseInt(request.getParameter("num1"));
int num2=Integer.parseInt(request.getParameter("num2"));
int add=num1+num2;
int sub=num1-num2;
int div=num1/num2;
int mul=num1*num2;
PrintWriter out=response.getWriter();
out.println("Addition : " +add);
out.println("Subtraction : " +sub);
out.println("Division : " +div);
out.println("Multiplication : " +mul);
}
}
10
Page 5 of 27
--- page 6 ---
B. 1. Employee Class:
employee-form.html:
<!DOCTYPE html>
<html>
<head>
<title>Employee Information Form</title>
</head>
<body>
<h2>Employee Information Form</h2>
<form action="process.jsp" method="post">
ID: <input type="text" name="id"><br>
Name: <input type="text" name="name"><br>
Designation: <input type="text" name="designation"><br>
Salary: <input type="text" name="salary"><br>
<input type="submit" value="Submit">
</form>
</body>
</html>
process.jsp:
<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page language="java" %>
<%@ page import="java.util.*" %>
<%@ page import="java.io.*" %>
<!DOCTYPE html>
<html>
<head>
<title>Employee Details</title>
</head>
<body>
<h2>Employee Details</h2>
<%-- Retrieve form parameters --%>
<% String id = request.getParameter("id"); %>
<% String name = request.getParameter("name"); %>
<% String designation = request.getParameter("designation"); %>
<% String salary = request.getParameter("salary"); %>
Page 6 of 27
--- page 7 ---
<%-- Display employee details --%>
<p>ID: <%= id %></p>
<p>Name: <%= name %></p>
<p>Designation: <%= designation %></p>
<p>Salary: <%= salary %></p>
</body>
</html>
Advantages of JSP:
1. Simplicity: JSP allows developers to embed Java code directly into HTML pages, making
it easier to write dynamic web content.
2. Ease of Maintenance: JSP pages separate the presentation logic from the business logic,
making it easier to maintain and update the code.
3. Reusability: JSP pages can be reused across multiple web pages, reducing the need to
duplicate code.
4. Integration with Java: JSP pages can access Java objects and libraries, allowing
developers to leverage the power of Java in web applications.
5. Performance: JSP pages are compiled into Java servlets, which are then executed by the
servlet container. This compilation process can improve performance compared to other
scripting languages.
2.   20
A. Inheritance mapping in Hibernate is a technique used to map a class hierarchy to a relational   10
database schema. There are several strategies for inheritance mapping, such as:
1. Single Table Inheritance: All classes in the hierarchy are mapped to a single table. A
discriminator column is used to differentiate between different types of objects.
2. Joined Table Inheritance: Each class in the hierarchy is mapped to its own table. Columns
are shared between tables using foreign key relationships.
3. Table Per Class Inheritance: Each concrete class in the hierarchy is mapped to its own
table. Common fields are duplicated in each table.
Page 7 of 27
--- page 8 ---
Here's an example demonstrating the Single Table Inheritance mapping strategy using
annotations:
@Entity
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name = "employee_type", discriminatorType =
DiscriminatorType.STRING)
public abstract class Employee {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
private String name;
// getters and setters
}
@Entity
@DiscriminatorValue("full_time")
public class FullTimeEmployee extends Employee {
private double salary;
// additional fields and methods
}
@Entity
@DiscriminatorValue("part_time")
public class PartTimeEmployee extends Employee {
private double hourlyRate;
// additional fields and methods
}
import javax.persistence.*;
@Entity
@DiscriminatorValue("full_time")
public class FullTimeEmployee extends Employee {
private double salary;
public FullTimeEmployee() {
}
public FullTimeEmployee(String name, double salary) {
super(name);
this.salary = salary;
Page 8 of 27
--- page 9 ---
}
public double getSalary() {
return salary;
}
public void setSalary(double salary) {
this.salary = salary;
}
@Override
public String toString() {
return "FullTimeEmployee{" +
"id=" + getId() +
", name='" + getName() + '\'' +
", salary=" + salary +
'}';
}
}
PartTimeEmployee
import javax.persistence.*;
@Entity
@DiscriminatorValue("part_time")
public class PartTimeEmployee extends Employee {
private double hourlyRate;
public PartTimeEmployee() {
}
public PartTimeEmployee(String name, double hourlyRate) {
super(name);
this.hourlyRate = hourlyRate;
}
public double getHourlyRate() {
return hourlyRate;
}
public void setHourlyRate(double hourlyRate) {
Page 9 of 27
--- page 10 ---
this.hourlyRate = hourlyRate;
}
@Override
public String toString() {
return "PartTimeEmployee{" +
"id=" + getId() +
", name='" + getName() + '\'' +
", hourlyRate=" + hourlyRate +
'}';
}
}
10
B. 1. Employee Class:
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
@Entity
public class Employee {
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
private String name;
private double salary;
public Employee() {
}
public Employee(String name, double salary) {
this.name = name;
this.salary = salary;
}
// Getters and setters
// toString method
Page 10 of 27
--- page 11 ---
}
2.
HibernateUtil Class:
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
public class HibernateUtil {
private static final SessionFactory sessionFactory = buildSessionFactory();
private static SessionFactory buildSessionFactory() {
try {
// Create the SessionFactory from hibernate.cfg.xml
return new Configuration().configure().buildSessionFactory();
} catch (Throwable ex) {
// Make sure you log the exception, as it might be swallowed
System.err.println("Initial SessionFactory creation failed." + ex);
throw new ExceptionInInitializerError(ex);
}
}
public static SessionFactory getSessionFactory() {
return sessionFactory;
}
public static void shutdown() {
// Close caches and connection pools
getSessionFactory().close();
}
}
MainApp
public class MainApp {
public static void main(String[] args) {
Employee employee1 = new Employee("John Doe", 50000.0);
Employee employee2 = new Employee("Jane Smith", 65000.0);
try (Session session = HibernateUtil.getSessionFactory().openSession()) {
session.beginTransaction();
Page 11 of 27
--- page 12 ---
// Save employees
session.save(employee1);
session.save(employee2);
// HQL for select operation
String selectAllQuery = "FROM Employee";
Query query = session.createQuery(selectAllQuery);
List<Employee> employees = query.list();
System.out.println("Employees:");
for (Employee employee : employees) {
System.out.println(employee);
}
// HQL for delete operation
String deleteQuery = "DELETE FROM Employee WHERE id = 1";
query = session.createQuery(deleteQuery);
int rowsDeleted = query.executeUpdate();
System.out.println("Rows deleted: " + rowsDeleted);
session.getTransaction().commit();
System.out.println("Employees saved and HQL operations performed successfully");
}
}
}
3.   20
A. Employee.java   10
package demo;
public class Employee {
private int id;
private String name;
private String city;
public int getId() {
return id;
}
Page 12 of 27
--- page 13 ---
public void setId(int id) {
this.id = id;
}
public String getName() {
return name;
}
public void setName(String name) {
this.name = name;
}
public String getCity() {
return city;
}
public void setCity(String city) {
this.city = city;
}
void display(){
System.out.println(id+" "+name+" "+city);
}
}
Page 13 of 27
--- page 14 ---
applicationContext.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans
xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:p="http://www.springframework.org/schema/p"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">
<bean id="obj" class="demo.Employee">
<property name="id">
<value>20</value>
</property>
<property name="name">
<value>Arun</value>
</property>
<property name="city">
<value>ghaziabad</value>
</property>
</bean>
</beans>
Page 14 of 27
--- page 15 ---
Test.java
package demo;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.*;
public class Test {
public static void main(String[] args) {
Resource r=new ClassPathResource("applicationContext.xml");
BeanFactory factory=new XmlBeanFactory(r);
Employee e=(Employee)factory.getBean("obj");
s.display();
}
}
B. Spring is a lightweight open source framework based on   10
1. dependency injection (DI) and
2. aspect-oriented programming (AOP)
It is light-weighted and loosely coupled
Here's a breakdown of what Spring offers:
Dependency Injection: Spring promotes a dependency injection approach, where objects
don't create their own dependencies but are instead injected with them. This leads to loosely
coupled and more testable code.
Modular Design: Spring is a collection of modules that address various aspects of
application development, such as data access, web development, security, and more. You
can choose the modules you need for your project.
Configuration Management: Spring uses XML or Java annotations for configuration,
allowing you to define beans (managed objects) and their dependencies declaratively,
separating application logic from configuration details.
Page 15 of 27
--- page 16 ---
Aspect-Oriented Programming (AOP): Spring supports AOP, enabling you to implement
cross-cutting concerns like logging, security, and transaction management transparently
without modifying core application logic.
Transaction Management: Spring simplifies transaction management, allowing you to
define transactional boundaries and handle exceptions declaratively.
MVC (Model-View-Controller) Framework: Spring provides a robust MVC framework
(Spring MVC) for building web applications, separating business logic, data models, and
presentation layers.
Spring Framework modules
Some of the important Spring Framework modules are:
1. Spring Core Module
2. Spring Context [ JEE]
3. Spring DAO Module [ Spring JDBC]
4. Spring ORM module
5. Spring AOP [ Aspect Oriented Programming]
6. Spring WEB-MVC Module
7. Core – a key module that provides fundamental parts of the framework, such as IoC or DI
8. JDBC – enables a JDBC-abstraction layer that removes the need to do JDBC coding for
specific vendor databases
9. ORM integration – provides integration layers for popular object-relational mapping APIs,
such as JPA, JDO and Hibernate
10. Web – a web-oriented integration module that provides multipart file upload, Servlet
listeners and web-oriented application context functionalities
11. MVC framework – a web module implementing the Model View Controller design pattern
12. AOP module – aspect-oriented programming implementation allowing the definition of
clean method-interceptors and pointcuts
Difference between constructor andsetter injection
Page 16 of 27
--- page 17 ---
Constructor Injection   Setter Injection
There is no partial injection   There can be partial injection.
It doesn’t override the setter property.   It overrides the constructor property
It will create a new instance if any   It will not create new instance if any
modification is done   modification is done.
It works better for many properties   It works better for few properties.
}
4.   20
A. Spring AOP supports five primary types of advice that can be applied at different join points   10
(specific points in the program execution flow):
1. Before Advice: Executes before the target method is invoked. Useful for tasks like security
checks, logging, or initializing data.
2. After Advice (Returning Advice): Executes after the target method completes
successfully, having access to the return value. Often used for logging, auditing, or
cleaning up resources.
3. After Throwing Advice: Executes after the target method throws an exception, with access
to the exception object. Ideal for error handling, logging, or rolling back transactions.
4. Around Advice: The most powerful type, encompassing the entire execution of the target
method. It receives control before the method is called, can proceed with the invocation,
and perform additional logic after the method returns normally or throws an exception.
Useful for transaction management, performance monitoring, and implementing
custom security filters.
5. On Invocation Advice: Rarely used directly, it's invoked whenever a join point is reached,
regardless of success or failure. Used for specialized scenarios like monitoring or tracing
method calls throughout the application.
Pointcut Expression:
Purpose: Define which join points advice should be applied to.
It defines the criteria for selecting join points based on method signatures, class names,
annotations, and other attributes.
Page 17 of 27
--- page 18 ---
Pointcut expressions use a combination of pointcut designators and operators. Some common
pointcut designators include:
execution(…): Selects method execution join points.
within(…): Selects join points within a specific package or class.
args(…): Selects join points based on the arguments of the method.
annotation(…): Selects join points based on the presence of a specific annotation.
For example, the following pointcut expression selects all public methods in the
com.example.service package:
@Pointcut("execution(public * com.example.service.*.*(..))")
public void serviceMethods() {
public void beforeSaveCustomerAdvice   // Advice logic to execute before saving a customer
}
}
Pointcut expressions are used in conjunction with advice declarations to specify where the
advice should be applied in the application.
Top of Form
execution(...): Matches method execution (e.g., execution(* com.example.service.*.*
(..)) matches any method in the com.example.service package).
within(...): Matches methods within a specific type
(e.g., within(com.example.service.MyService)).
this(...): Matches based on the target object's type
(e.g., this(com.example.service.MyService)).
args(...): Matches methods based on their arguments (e.g., args(String, int)).
@annotation(...): Matches methods annotated with a specific annotation
(e.g., @annotation(org.springframework.transaction.Transactional)).
Logical operators (&&, ||, !): Combine conditions for more precise targeting.
Wildcards (*, ..): Match any number of characters (*) or any number of parameters (..).
Benefits of Pointcut Expressions:
Flexibility: Allow for fine-grained control over where advice is applied.
Page 18 of 27
--- page 19 ---
Reusability: Pointcut expressions can be reused for different types of advice, enhancing
maintainability.
Decoupling: Advice and join points are defined separately, promoting better code
organization.
Spring AOP uses AspectJ's pointcut expression language by default, offering a rich set of
features for defining join points.
B. Step 1: Open Spring Initializr http://start.spring.io.   10
Step 2: Provide the Group name. We have provided the Group name demo
Step 3: Provide the Artifact Id. We have provided the Artifact Id aop-before-advice-example.
Step 4: Add the Spring Web dependency.
Step 5: Click on the Generate button. When we click on the Generate button, it wraps all the
specifications in a jar file and downloads it to the local system.
Step 6: Extract the downloaded jar file.
Step 7: Import the folder by using the following steps:
File -> Import -> Existing Maven Projects -> Next -> Browse the Folder aop-before-advice-
example -> Finish.
Step 8: Open the pom.xml file and add the following AOP dependency. It is a starter for
aspect-oriented programming with Spring AOP and AspectJ.
Step 9: Open AopBeforeAdviceExampleApplication.java file and add an annotation
@EnableAspectJAutoProxy.
Step 10: Create a package with the name demo.model.
Step 11: Create a model class under the package demo.model. We have created a class with the
name Employee. In the class, define the following:
Define three variables empId, firstName, and secondName of type String.
Generate Getters and Setters.
Create a default
Step 12: Create a package with the name demo.controller.
Step 13: Create a controller class under the package demo.controller. We have created a class
with the name EmployeeController.
Step 14: Create a package with the name com.javatpoint.service.
Step 15: Create a Service class under the package demo.service. We have created a class with
the name EmployeeService.
In the Service class, we have defined two methods createEmployee and deleteEmployee.
Step 16: Create a package with the name demo.aspect.
Step 17: Create an aspect class under the package demo.aspect. We have created a class with
the name EmployeeServiceAspect.
Step 18: Open the eAopBeforeAdviceExampleApplication.java file and run it as Java
Application.
Page 19 of 27
--- page 20 ---
5.   20
A. Spring JDBC   10
Purpose: Provides a higher-level abstraction over the raw JDBC API, simplifying database
interactions in Java applications.
Key Features:
JdbcTemplate: A central class that offers convenient methods for executing SQL
statements (queries, updates, deletes) and working with results. It handles resource
management (opening/closing connections) and exception translation (JDBC exceptions
to Spring's DataAccessException hierarchy).
RowMapper: A callback interface used to map database rows to Java objects. This
reduces the boilerplate code involved in manually converting result sets.
NamedParameterJdbcTemplate: A variant of JdbcTemplate that allows parameter
binding using named placeholders (:paramName), enhancing readability and preventing
SQL injection vulnerabilities.
Spring DAO
Concept: A design pattern that encapsulates data access logic, providing a layer of
abstraction between the business logic and the underlying persistence mechanism (JDBC,
ORM like Hibernate, JPA, etc.).
Benefits:
Decoupling: Business logic doesn't depend on specific persistence technologies,
allowing for easier switching if needed.
Exception Handling: Spring DAO handles persistence-specific exceptions and
translates them into a consistent DataAccessException hierarchy, simplifying error
handling in the business layer.
Reusability: DAO methods can be reused across different parts of the application.
Implementation with Spring: Spring doesn't enforce a specific DAO implementation, but
it provides annotations and classes to streamline DAO development:
Page 20 of 27
--- page 21 ---
@Repository annotation: Marks a class as a DAO, enabling Spring to manage its
lifecycle and exception translation.
Abstract base classes like JdbcTemplateDaoSupport or JpaDaoSupport: These classes
provide common DAO functionality like datasource access, reducing boilerplate code
for specific technologies.
Example: Spring JDBC DAO for a User
Java
@Repository
public class UserDaoImpl implements UserDao {
private JdbcTemplate jdbcTemplate; // Injected by Spring
@Override
public User getUserById(long id) {
String sql = "SELECT name, email FROM users WHERE id = ?";
return jdbcTemplate.queryForObject(sql, new LongRowMapper(), id);
}
@Override
public void saveUser(User user) {
String sql = "INSERT INTO users (name, email) VALUES (?, ?)";
jdbcTemplate.update(sql, user.getName(), user.getEmail());
}
private static class LongRowMapper implements RowMapper<User> {
@Override
public User mapRow(ResultSet rs, int rowNum) throws SQLException {
String name = rs.getString("name");
String email = rs.getString("email");
return new User(name, email);
}
}
}
content_copy
In this example:
UserDaoImpl is a Spring DAO for User objects.
Page 21 of 27
--- page 22 ---
@Repository annotation marks it as a DAO.
It injects a JdbcTemplate instance for database interactions.
getUserById uses a query with a named parameter (?) and LongRowMapper to map results
to a User object.
saveUser uses an update statement with named parameters to insert a new user.
This is a basic example, and Spring JDBC offers more features like batch updates, prepared
statements, and transaction management.
B. import jakarta.servlet.ServletException;   10
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import java.io.IOException;
public class SessionServlet extends HttpServlet {
protected void doGet(HttpServletRequest request, HttpServletResponse response)
throws ServletException, IOException {
// Get the current session or create a new one if it doesn't exist
HttpSession session = request.getSession(true);
// Get the current session ID
String sessionId = session.getId();
// Check if the session is new or not
boolean isNewSession = session.isNew();
// Set some session attributes
session.setAttribute("username", "John");
session.setAttribute("language", "English");
// Get some session attributes
String username = (String) session.getAttribute("username");
String language = (String) session.getAttribute("language");
Page 22 of 27
--- page 23 ---
// Print the session information
response.setContentType("text/html");
response.getWriter().println("<h1>Session Tracking Example</h1>");
response.getWriter().println("<p>Session ID: " + sessionId + "</p>");
response.getWriter().println("<p>Is New Session: " + isNewSession + "</p>");
response.getWriter().println("<p>Username: " + username + "</p>");
response.getWriter().println("<p>Language: " + language + "</p>");
}
}
6.   20
A. The Spring MVC framework follows a request-response lifecycle that involves several   10
components working together. Here's a high-level overview of the workflow with a diagram:
1. Client sends a request: The client (browser) sends an HTTP request to the server.
2. DispatcherServlet receives the request: The DispatcherServlet is a front controller that
receives all incoming requests. It consults a HandlerMapping to determine the appropriate
Controller to handle the request.
3. Controller processes the request: The Controller contains the application logic to process
the request. It may interact with a service layer to perform business logic.
Page 23 of 27
--- page 24 ---
4. ModelAndView creation: The Controller returns a ModelAndView object, which
contains both the data (the model) and the view name.
5. ViewResolver resolves the view: The ViewResolver maps the logical view name to an
actual view (JSP or Thymeleaf template).
6. View rendering: The selected view is rendered, and the model data is passed to the view
for display.
7. Response sent to the client: The rendered view is sent back as the HTTP response to the
client.
Here's a basic example to illustrate this workflow:
@Controller
public class HomeController {
@RequestMapping("/")
public String home(Model model) {
model.addAttribute("message", "Hello, Spring MVC!");
return "home";
}
}
Views (home.jsp and result.jsp):
home.jsp:
<!DOCTYPE html>
<html>
<head>
<title>Home Page</title>
</head>
<body>
<h1>Welcome to Spring MVC</h1>
<p>${message}</p>
<form action="/result" method="post">
<input type="text" name="name" />
<input type="submit" value="Submit" />
</form>
</body>
</html>
Page 24 of 27
--- page 25 ---
result.jsp:
<!DOCTYPE html>
<html>
<head>
<title>Result Page</title>
</head>
<body>
<h1>Result Page</h1>
<p>Hello, ${name}!</p>
</body>
</html>
Configuration Files:
1. web.xml:
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
version="4.0">
<servlet>
<servlet-name>dispatcher</servlet-name>
<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
<init-param>
<param-name>contextConfigLocation</param-name>
<param-value>/WEB-INF/dispatcher-servlet.xml</param-value>
</init-param>
<load-on-startup>1</load-on-startup>
</servlet>
<servlet-mapping>
<servlet-name>dispatcher</servlet-name>
<url-pattern>/</url-pattern>
</servlet-mapping>
</web-app>
2. dispatcher-servlet.xml:
Page 25 of 27
--- page 26 ---
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:context="http://www.springframework.org/schema/context"
xmlns:mvc="http://www.springframework.org/schema/mvc"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd
http://www.springframework.org/schema/context
http://www.springframework.org/schema/context/spring-context.xsd
http://www.springframework.org/schema/mvc
http://www.springframework.org/schema/mvc/spring-mvc.xsd">
<context:component-scan base-package="com.example.controller" />
<mvc:annotation-driven />
<bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
<property name="prefix" value="/WEB-INF/views/" />
<property name="suffix" value=".jsp" />
</bean>
</beans>
In this example, the HomeController handles requests for the home page (/) and processes the
form submission to display the result (/result). The views are resolved using the
InternalResourceViewResolver, which maps logical view names to JSP files.
B. JavaBean Explanation - 4mks   10
A JavaBean is a reusable, platform-independent component that can be manipulated visually in
a builder tool.” A JavaBean is a reusable, platform-independent component that can be
manipulated visually in a builder tool.”
A JavaBean is a Java class that should follow the following conventions:
o It should have a no-arg constructor.
o It should be Serializable.
o It should provide methods to set and get the values of the properties, known as getter and
setter methods.
A JavaBean is a specially constructed Java class written in the Java and coded according to the
JavaBeans API specifications.
Advantages and disadvantages - 6mks
Advantages
Page 26 of 27
--- page 27 ---
1. Exposure to other applications
One of the most important advantages of a JavaBean is, the events properties and the methods
of a bean can be exposed directly to another application.
2. Registration to receive events
A JavaBean can be registered to receive events from other objects. However, we can also
generate events that can be sent to other objects.
3. Ease of configuration
We can easily use auxiliary software to configure the JavaBean. However, we can also save the
configuration setting of a JavaBean to persistent storage.
4. Portable
As JavaBeans are built in Java, we can easily port them to any other platform that contains
JRE.
5. Lightweight
JavaBeans are light weighted, I.e., we don't need to fulfill any special requirement to use it.
Also, it is very easy to create them. However, it doesn't need a complex system to register
components with JRE.
disadvantages
JavaBeans are mutable. So, it can't take advantages of immutable objects.
Creating the setter and getter method for each property separately may lead to the
boilerplate code.
Page 27 of 27
````
