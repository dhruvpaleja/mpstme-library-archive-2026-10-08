# Systems Analysis and Design: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper 49a380c1c311

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSE_DS_7011/Systems Analysis and Design/ANS_Systems Analysis and Design(702CO0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 May 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Systems Analysis and Design
Date: 02 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted
7. Assume suitable data if necessary
Q1   Answer briefly:   [20]
a)   List guidelines for component-level design. Why should components be loosely
coupled?
Component-level design should ensure high cohesion, low coupling, clear
Unit-6, CO-   interfaces, reusability, and simplicity. Components should perform a single well-
3; SO-1 ;   defined task and interact through well-specified interfaces. They should also be   [5]
BL-2   modular and easy to test and maintain. Components should be loosely coupled so
that changes in one component do not affect others, improving flexibility,
scalability, and ease of maintenance.
b) Define Agile Model and list its key principles.
The Agile Model is an iterative and incremental software development
Unit-1, CO-1   approach that focuses on flexibility, customer collaboration, and rapid delivery
; SO-1 ; BL-   of working software. Its key principles include customer satisfaction, frequent   [5]
2   delivery, adaptability to changes, continuous feedback, teamwork, and
simplicity. Agile promotes close interaction between developers and
stakeholders throughout the development process.
c)   Differentiate between functional and non-functional requirements.
Functional requirements define what the system should do, such as features and
functionalities (e.g., login, payment processing). Non-functional requirements
Unit No: 8;   (NFRs) define how the system should perform, such as performance, reliability,
CO-3 ; SO-2 ;   security, and usability. While functional requirements focus on system   [5]
BL-2   behavior, NFRs focus on system quality and constraints.
d)   List and design the notations used in sequence diagram.
Unit-4, CO-2
; SO-2;   A sequence diagram includes actors and objects as participants, each represented   [5]
BL-3   with a lifeline showing its existence over time. Communication is shown using
messages (arrows) such as synchronous, asynchronous, and return messages.
********** 1 **********
--- page 2 ---
Activation bars indicate when an object is executing a task. It may also include
combined fragments like loop or condition (alt, opt) to represent control flow,
along with object creation and destruction when required.
Q2   [20]
a) Design a Activity Diagram for an Online Banking System showing the workflow
from user login to transaction completion. Include steps such as selecting a
banking service, entering and confirming transaction details, and initiating
Unit-2;CO-1;
payment.   [10]
SO-2; BL-3
Ans: all notations of activity diagram is required.
b) Define association, aggregation, composition, interface realisation, dependency
and association class. Show these relationships for online banking system using
the class diagram.
Ans:
Association is a relationship showing how two classes are connected and interact
Unit-3; CO-   with each other. Aggregation is a “has-a” relationship where one class contains
3; SO-2; BL-   [10]
another but both can exist independently (weak relationship). Composition is a
3
strong “part-of” relationship where the contained object cannot exist without the
parent. Interface realization occurs when a class implements the methods
defined in an interface. Dependency represents a temporary relationship where
one class depends on another for some functionality. Association class is a class
attached to an association that contains attributes of the relationship itself.
Q3   [20]
a). Compare Prescriptive, Evolutionary, and Agile Models with suitable examples.
Prescriptive, Evolutionary, and Agile models differ mainly in flexibility and
how software is developed over time. Prescriptive models (e.g., Waterfall
Model) follow a structured, sequential approach with well-defined phases,
suitable for stable and well-understood requirements, such as government or
banking systems. Evolutionary models (e.g., Spiral Model or Prototyping)
Unit-1; CO-1;   develop software in iterations, allowing gradual refinement and user feedback,
[10]
SO-2; BL-2   making them suitable for complex systems like simulation software. Agile
models (e.g., Scrum) emphasize rapid, incremental delivery, continuous
feedback, and adaptability to change, ideal for dynamic projects like mobile app
development. Thus, prescriptive models focus on planning, evolutionary models
focus on gradual refinement, and agile models focus on flexibility and
collaboration.
b) Design Usecase diagram, An e-commerce platform allows users to browse products, add
items to a cart, and place orders online. The process begins when a user logs in and
searches for products. After selecting items, the user adds them to the cart and proceeds
to checkout. The system then verifies payment details and processes the transaction. If
Unit-2;CO-2;   the payment is successful, the order is confirmed and sent for delivery; otherwise, the
[10]
SO-2; BL-2   user is prompted to retry. Finally, the system updates the order status and notifies the
user.
Actors:customer
Usecase:place order, add to the cart
Q4   [20]
Unit-4; CO-2   a) Design collaboration diagram for the case study. A customer uses an ATM to
SO-6; BL-4   [10]
withdraw cash by inserting the card and entering a PIN. The ATM sends the PIN
********** 2 **********
--- page 3 ---
to the bank server for verification. After successful authentication, the customer
selects the withdrawal option and enters the amount. The ATM requests the bank
server to check the account balance. If sufficient funds are available, the amount
is debited from the account. Finally, the ATM dispenses cash and prints a receipt,
with all objects collaborating through message exchanges.
Customer (Actor) , ATM Machine (Boundary Object) , Card Reader
(Device/Interface Object) ,Bank Server (Control Object) ,Account Database
(Entity Object) , Cash Dispenser (Device Object) , Receipt Printer (Device
Object)
How they collaborate:Customer interacts with ATM Machine , ATM uses
Card Reader to read card , ATM sends PIN to Bank Server , Bank Server
verifies using Account Database , ATM requests balance check from Bank
Server , If valid to Cash Dispenser gives cash , Receipt Printer prints receipt
How do functional requirements get transformed into design elements? Explain
b) with neat diagram.
Unit-5; CO-3;   [10]
SO-2; BL-3
Q5   [20]
Unit-7; CO-4;   a)   Discuss the role of drivers and stubs in unit testing. Design the framework for the same. [10]
SO-2; BL-4
b) Direct communication between boundary and entity objects should be avoided.
Discuss the reason with an example.
Direct communication between boundary and entity objects should be avoided
to maintain proper separation of concerns and system structure. Boundary
Unit - 3; CO-   objects handle user interaction, while entity objects represent core data, so
[10]
2; SO-2; BL-2   allowing them to communicate directly can lead to tight coupling and poor
design. Instead, control objects act as intermediaries to manage logic and
coordinate interactions. This improves maintainability, flexibility, and
scalability, as changes in the user interface or data layer will not directly affect
each other.
Q6   [20]
a) Explain how black-box testing techniques can be used to generate test cases for
a Paytm system. Illustrate with test cases.
Black-box testing techniques can be used in a Paytm-like system by focusing on
Unit-7, CO-4;   inputs, outputs, and user-visible behavior without considering internal code.   [10]
SO-2; BL-4
Techniques such as equivalence partitioning, boundary value analysis, and
decision table testing help generate effective test cases for features like login,
money transfer, and recharge.
********** 3 **********

[Text in pictures on this page, read by OCR]
Component-
Tow oriented Level Design
elements

Interface Desig
Analysis Model

Donaviorat Architectural Design
‘clement s

Data/ Class Design

Pel

Design Model
--- page 4 ---
b) Design package diagram for the case study ATM system in Q4(a)
A Package Diagram for an ATM system organizes the system into logical groups
Unit-6, CO-2;   of related classes. The main packages include the User Interface package, which
SO-2;   handles interaction through the ATM screen and keypad, and the ATM [10]
BL-3   Operations package, which manages functions like cash withdrawal, deposit, and
balance inquiry. The Authentication package is responsible for card validation
and PIN verification, while the Bank Services package handles communication
with the bank server for transaction processing and account management.
Q7   [20]
a) Explain how deployment diagrams help in system scalability and performance
analysis.
Deployment diagrams help in system scalability and performance analysis by
providing a clear view of how software components are physically distributed
Unit-8, CO-3;   across hardware nodes such as servers, databases, and networks. By visualizing
SO-2;   [10]
BL-3   this mapping, developers can identify bottlenecks, such as overloaded servers or
slow communication paths, and make decisions like adding more servers, load
balancing, or optimizing network connections. They also help in analyzing how
the system will behave under increased load, enabling better planning for
scalability and improved performance through efficient resource allocation.
Unit-4, CO-4;
SO-2;   b) Design the state diagram for the case study in Q3(b).
[10]
BL-4   All the state diagram notation should be denoted.
********** 4 **********
````

## 2025-26 · Re-Exam · Sem 6 · Answer key · paper 0f3d3e7161d6

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_06/Re-Exam/BTech_CSE_DS_7011/Systems Analysis and Design/ANS_Systems Analysis and Design(702CO0C020)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 29 Jun 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2025-2026)
Subject: Systems Analysis and Design
Date: 29 Jun 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted
7. Assume suitable data if necessary
Q1   Answer briefly:   [20]
a) What is cohesion and coupling in component design. Explain the concept by
considering online banking system.
Cohesion and coupling are key principles in component design. Cohesion refers to how
Unit-6, CO-   closely related the functions within a component are, and high cohesion is desirable—
3; SO-2 ;   for example, in an online banking system, an AccountService handling only account-   [5]
BL-3   related tasks like balance checking and transactions. Coupling refers to the dependency
between components, and low coupling is preferred, such as keeping the user interface
independent from database logic.
b) What is Prototype Model? State its advantages and disadvantages.
The Prototype Model is a development approach where an initial working model is
Unit-1, CO-1   built to understand user requirements, especially when they are unclear. It allows early
; SO-1 ; BL-   feedback and improves user satisfaction, but it can be time-consuming and may lead to   [5]
2   confusion if users mistake the prototype for the final system.
c)   Discuss the non functional requirements (i) Scalability (iii) Performance (iii)Usability
(iv)Reliability
Unit No: 8;
Non-functional requirements like scalability, performance, usability, and reliability
CO-3; SO-2;   [5]
define the quality of a system. In an online banking system, scalability ensures it can
BL-2
handle many users, performance ensures fast transactions, usability ensures ease of use,
and reliability ensures accurate and consistent operations without failures.
d) Explain fork- join and decision node in activity diagram, with an example.
Unit-4, CO-2
; SO-6;   [5]
In activity diagrams, a decision node is used to represent conditional branching (e.g.,
BL-4
checking if sufficient balance exists before a transaction), while fork and join nodes are
********** 1 **********
--- page 2 ---
used for parallel processing, such as loading account details and transaction history
simultaneously and then combining them before displaying the dashboard.
Q2   [20]
a)   Identify business processes for a Library Management System using use cases. Design
Unit-2;CO-1;   the neat Usecase diagram with required notation.
[10]
SO-2; BL-3
Identification of actors, usecases and relation for LMS.
b)   Identify objects and design a class diagram for a Banking System. The class diagram
Unit-3; CO-
must show six valid relationships between the classes.
3; SO-6; BL-   [10]
4
Six valid relationships required.
Q3   [20]
a)   Describe Agile Process Models and explain Scrum in details with its key
.   characteristics.
Agile Process Models are iterative and flexible approaches to software development
that focus on delivering small increments of working software, continuous customer
Unit-1; CO-   feedback, and adapting to changing requirements. Models like Scrum, XP, and Kanban
1; SO-2; BL-   emphasize collaboration, quick delivery, and improvement through iterations. Scrum, a   [10]
2   popular Agile framework, organizes work into time-boxed sprints (2–4 weeks) and
involves roles such as Product Owner, Scrum Master, and Development Team. It
includes key activities like sprint planning, daily meetings, reviews, and retrospectives.
Its main characteristics are iterative development, continuous feedback, adaptability,
team collaboration, and frequent delivery of usable software.
b) Design Swimlane diagram for the case study. The Fixed Deposit System in an
international bank allows customers to deposit a fixed amount for a specific period at a
fixed interest rate. Customers choose the deposit amount and tenure, and the system
processes the request after verification. Interest is calculated and added either
Unit-2;CO-1;
periodically or at maturity. On completion, the maturity amount is credited to the [10]
SO-2; BL-4
customer’s account. The system also supports premature withdrawal with penalties.
Notifications are sent to keep customers updated about their deposit status.
Ans:all the swimlane notations required.
Q4   [20]
a)   Difference between Sequence Diagram and Collaboration Diagram. Also explain the
role of combined fragment in sequence diagram.
A Sequence Diagram focuses on the time-ordered flow of messages between objects,
showing how interactions occur step-by-step along a timeline, whereas a Collaboration
Unit-4; CO-2
Diagram (also called Communication Diagram) emphasizes the structural organization
SO-2; BL-4   [10]
of objects and their relationships, with message flow shown using numbering instead
of a strict time axis. In a Sequence Diagram, a combined fragment is used to represent
control logic such as conditions, loops, or parallel execution (e.g., alt for if-else, loop
for repetition, par for parallel actions), helping to model complex interaction scenarios
clearly within the sequence of messages.
Which are the 4 types of design considered, while transforming design from analysis to
b) design model
Data/Class design :
Unit-5; CO-   Transforms analysis models into design class realizations, data structures required to
3; SO-6; BL-   implement software, classes, relationships defined by CRC index cards.   [10]
4   Architectural design :
It defines relationship between structural elements of a software, architectural style and
design patterns, constraints that affect the architecture.
Interface design:
It defines how software communicates with systems that interoperate with it, humans
********** 2 **********
--- page 3 ---
who use it.
Component level design:
It transforms structural elements of software architecture into a procedural description
of software components.
Q5   [20]
a)   Differentiate between alpha, beta and gamma testing. Also identify these tests as alpha,
beta and gamma testing.
Alpha, Beta, and Gamma Testing are stages of software testing that differ based
on who performs them and where they are conducted. Alpha testing is done
Unit-7;CO-4;   internally by developers or testers at the developer’s site to identify bugs before
[10]
SO-2; BL-4   release. Beta testing is performed by a limited number of real users in a real
environment to gather feedback and uncover issues not found during alpha
testing. Gamma testing is the final testing phase where the product is released to
a wider audience with minimal changes expected, mainly to ensure stability and
readiness for full deployment.
b) Explain the 3 layers in package diagram, with neat diagram
Three-layer architecture is commonly used to organize the system into logical groups for
better modularity and maintainability. The Presentation Layer (top layer) handles user
Unit-5;CO-2;   interaction, such as UI screens in an online banking system (e.g., login page, dashboard).
[10]
SO-2; BL-2   The Business Logic Layer (middle layer) contains the core functionality and rules, such
as processing transactions, validating accounts, and applying business rules. The Data
Access Layer (bottom layer) is responsible for interacting with the database, including
storing and retrieving account and transaction data. This layered structure improves
separation of concerns, making the system easier to design, test, and maintain.
Q6   [20]
a) A bank wants to test its ATM system before deployment. Explain the statement
coverage for the ATM system, considering the “if condition” for withdrawal function.
Statement coverage ensures that every statement in the program is executed at
least once during testing. In an ATM withdrawal function, consider an if
Unit-7, CO-   condition like: if (balance ≥ withdrawal amount). To achieve statement
4; SO-2; BL-   [10]
coverage, test cases must be designed so that both the true branch (sufficient
4
balance → withdrawal successful) and the false branch (insufficient balance →
display error message) are executed at least once. This ensures all statements in
the withdrawal logic are tested, but it does not guarantee that all logical
conditions are fully verified.
b) What are the main elements of component diagram? Explain with their notation
diagram
The main elements of a Component Diagram in UML represent the structure of a
system in terms of its modular parts:
Unit-6, CO-   Component: A modular unit (e.g., ATM module, Account Service), shown as a
2; SO-2;   rectangle with a small component icon (two rectangles on the side).   [10]
BL-3   Interface: Defines services provided or required by a component, represented by a
lollipop (○) for provided interface and a socket for required interface.
Dependency: Shows how one component depends on another, drawn as a dashed
arrow.
Port: A small square on the component boundary indicating interaction points.
Connector: Links components or interfaces, showing communication between them.
********** 3 **********
--- page 4 ---
Q7   [20]
a) Draw a Deployment Diagram for a Mobile Banking Application showing interaction
between mobile device, API server, and database.
The Mobile Device hosts the mobile banking app used by customers.
Unit-8, CO-
The API Server processes requests (login, transfer, balance check).
3; SO-2;   [10]
The Database stores user accounts and transaction data.
BL-3
Mobile → API Server via HTTPS
API Server → Database via SQL queries
Unit-4, CO-   Design the state diagram for the case study in Q3(b).
4; SO-6;   b)
[10]
BL-4   Discuss all the state diagram notations required for the Fixed Deposit System in an
international bank.
********** 4 **********
````

## 2024-25 · Final-Exam · Sem 6 · Answer key · paper 9b2d76d19267

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_06/Final-Exam/BTech_CSE_DS_7011/Systems Analysis and Design/ANS_Systems Analysis and Design(702CO0C020)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2025
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Semester VI(Exam Year: 2024-2025)
Subject: Systems Analysis and Design
Date: 05 May 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
Q1   Answer briefly:   [20]
a) A company wants to develop a payment gateway integration for multiple third-
Unit-no:3,   party services (PayPal., etc). Design interface for the same.
CO- 3; SO-2 ;
[5]
BL-3,
Moderate   Ans: Show any two components, also mention the provided and required
interface.
b)   Describe Unified development Process (UDP) with its phases and neat diagram.
Ans:
Inception, Elaboration , Construction and Transition
Unit No: 1;
CO-3 ; SO-2 ;   [5]
BL-2;Low
Unit No: 8;   c) What are non-functional requirements (NFRs), and Why are NFRs important in
CO-3 ; SO-2 ;   system design and development?
[5]
BL-2;   Non-Functional Requirements (NFRs) define the quality attributes, constraints,
Moderate   and performance standards of a system rather than its specific functionalities.
********** 1 **********

[Text in pictures on this page, read by OCR]
Phases Inception

Business Modeling H :

Analysis

Design “a ee

Implementation

Test

Deployment

Phases

Configuration and
Change Management

Project Management
--- page 2 ---
Unlike functional requirements (which describe what a system should do), NFRs
describe how a system should behave.
NFRs include:
1. Performance – System response time, latency, throughput, scalability.
2. Security – Authentication, authorization, data encryption, access control.
3. Reliability – System uptime, fault tolerance, recovery mechanisms.
4. Usability – User experience, UI/UX standards, accessibility.
5. Scalability – Ability to handle increasing load efficiently.
6. Maintainability – Ease of debugging, code modularity, versioning.
7. Interoperability – Ability to work with other systems (APIs, third-party
integrations).
d) Why is high cohesion and low coupling is preferred in software design?
Unit No: 6,   Ans:
CO-3 ; SO-2;
BL-3,   In software design, the principles of high cohesion and low coupling improve   [5]
Moderate   maintainability, scalability, and reliability of a system. These concepts are
fundamental to writing modular, reusable, and robust code.
Q2   [20]
a) A bank wants to develop a secured online banking system with features such as
account management, money transfers, bill payments, and fraud detection. Which
Unit No: 1,
process model will be suitable? Also justify why other models are not suitable
CO-21 SO-1;
(Select any two models).   [10]
BL-3
moderate
Ans: Any model is suitable. Proper justification as per the model is required.
b) A hospital wants to develop a Hospital Management System to manage patients,
doctors, appointments, billing, and medical records. The system should allow
patients to book appointments, doctors to view and update medical records, and
the admin to manage hospital operations. Design the class diagram for the above
case study.
Ans: Class diagram must have any five relations, class names and operations must
be named properly.
Notations   Naming conventions
3 partition, name-noun,
attribute-varible, methods-
Unit No: 3,
CO-2; SO-6;   Class   verbs   [10]
BL-4 high   Cardinality will be used
Association   alongwith all the relations
Dependency
Aggregation
Composition
Interface-realisation
Association class
Generalisation-specialisation
Q3   [20]
********** 2 **********
--- page 3 ---
a) A healthcare organization is implementing a Vaccine Management System to
.   streamline the process of vaccine distribution, scheduling, and administration. The
system connects citizens, healthcare workers, hospital administrators, and
inventory managers to ensure an efficient vaccination process. Design Usecase
diagram mentioning all the required relations, use cases and actors.
Ans: Actors and use cases are named properly.
Notations   Naming conventions
Unit No: 2,
CO-1; SO-6;   Primary Actor/Secondary   [10]
BL-3   Actor   Noun
Usecases   Verb
Association   Verb
Directed Association   Verb
usescases must be
Generalisation and   verbs   Actors:
specialisation   Nouns
b) How does Extreme programming (XP) helps in handling changing requirements
during development? Explain each stage of XP programming.
Frequent Releases – Delivers working software in small iterations, allowing quick
Unit No: 1,
adaptation to changes. Continuous Customer Involvement – Keeps the customer
CO-1; SO-6;   [10]
BL-2   engaged to refine requirements dynamically. Test-Driven Development (TDD) –
Ensures changes do not break existing functionality.
Pair Programming – Improves code quality and knowledge sharing to handle
evolving requirements. Refactoring – Allows for continuous improvement of the
codebase to accommodate new changes.
Q4   [20]
a)   Design Activity diagram for the case mentioned in Q.2(b).
Activity Diagram
Naming
Unit No: 4,   Notations   conventions
CO-2; SO-6;
BL-3   Start/End   [10]
Activity   Verbs
Transistion   Verbs
Fork/Join
Choice Point
Design component diagram for Library management system, A system for
b) managing book inventory and student borrow/return operations.
Components:
Book Catalog Component (Manages books, authors, genres)
•   User Management Component (Handles student/staff logins)
Unit No: 6,   •   Issue & Return Component (Manages book borrowing and returning)
[10
CO-3; S-6; BL-   •   Fine Calculation Component (Handles overdue charges)
]
4   •   Notification Component (Sends due date reminders)
• Database Component (Stores book and user data)
• Payment Gateway
Ans: Interface(Provided and required), components( above mentioned 6
components), association, dependency..etc, must be shown in the design.
********** 3 **********
--- page 4 ---
Q5   [20]
a)   Design Test Case Template for a module login System, consider at least four cases
(Eg: username and password).
Ans:
Unit No: 7,
CO-4; SO-6;   [10]
BL-3
b)   Explain at what circumstances integration, unit and system testing is done?
Explain with an example.
Ans:
When is Unit Testing Done?
•   During the development phase, before integrating with other modules.
•   Developers perform unit testing immediately after writing a function or
method.
Unit No: 7,   •   It is done in isolation to verify that each component behaves as expected.
CO-4; SO-1;   [10]
When is Integration Testing Done?
BL-3
•   After unit testing, when individual modules are combined.
•   Ensures that different components work together correctly.
• Performed after multiple unit-tested components are integrated.
When is System Testing Done?
•   After integration testing, when the entire system is ready.
• Performed in a realistic environment to test overall functionality.
•   Validates that the software meets business requirements.
Q6
[20]
a) What are stubs and drivers. Explain top down and bottom up integration approach
and the usage of stubs and drivers.
Ans:
Unit No: 7,
A stub is a dummy module that simulates the behavior of a lower-level component
CO-4; SO-6;   [10]
that is not yet developed.
BL-4
A dummy module that mimics the behavior of a higher-level module in bottom-up
integration testing. It sends test inputs and invokes the lower-level module.
b)   Explain SCRUM agile model with its key features backlog, sprint scrum master,
scrum meeting, retrospective team.
Unit No: 6,
SCRUM is an Agile framework that facilitates iterative and incremental software
CO-3; SO-6;   [10]
BL-4   development. It is widely used for managing complex projects, enabling flexibility,
collaboration, and continuous improvement.
Q7   [20]
Unit No: 8,   a)
What kind of considerations are taken into account when creating deployment
CO-4; SO-2;   [10]
BL-2   diagram for real world system.
********** 4 **********
--- page 5 ---
Deployment Diagram in UML represents the physical architecture of a system,
showing how software components are distributed across hardware nodes
(servers, databases, client devices, etc.).
Discuss the importance of Package diagram. How it helps in real world system
b) development. Explain with an example.
A Package Diagram is crucial for organizing large systems into manageable
modules, ensuring clarity in system design and dependencies. Below are key
reasons why package diagrams are important:
1. Organizes Complex Systems
•   Helps break down a large system into logical groups.
• Improves maintainability and readability.
2. Shows Dependencies Between Modules
Unit No:5,   •   Clearly represents which package depends on another.
CO-4; SO-6;
•   Helps in understanding module interactions and avoiding unnecessary   [10]
BL-4
dependencies.
3. Facilitates Modular Development
•   Supports modular programming by grouping related components.
•   Enables reusability of packages across different projects.
4. Aids in Team Collaboration
•   Helps different teams work on different packages without conflicts.
•   Ensures structured software architecture for easier communication.
5. Supports Better Code Management
•   Helps in structuring the codebase into different layers.
•   Prevents tight coupling by enforcing dependency rules.
********** 5 **********
````

## 2024-25 · Re-Exam · Sem 6 · Answer key · paper 290653293b43

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_06/Re-Exam/BTech_CSE_DS_7011/Systems Analysis and Design/ANS_Systems Analysis and Design(702CO0C020)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Jul 2025
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: III/Sem 6 Re-exam(Exam Year: 2024-2025)
Subject: Systems Analysis and Design
Date: 07 Jul 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 5 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. All questions carry equal marks
7. Assume suitable data if necessary
Q1   Answer briefly:   [20]
a)   Differentiate between a provided and required interface in a component diagram.
Explain with an example
Provided   Required
Definition   Describes   Describes
services/functions a   services/functions a
component offers to   component depends on
Unit-6, CO-
others.   from others.
3; SO-1 ;   [5]
BL-2, Low   Lolipop symbol, A   Socket symbol, A
Payment Gateway   Shopping Cart
Component provides a   Component requires a
PaymentProcessing   PaymentProcessing
interface.   interface.
Unit-1, CO-   b)
1 ; SO-6 ;   A company is developing a new e-commerce platform. With the neat diagram
[5]
BL-3,   explain , how the UDP phases would be applied to this project.
Moderate
********** 1 **********
--- page 2 ---
c) What are non-functional requirements (NFRs), and Why are NFRs important in
system design and development?
Non-Functional Requirements (NFRs) define the quality attributes, constraints,
and performance standards of a system rather than its specific functionalities.
Unlike functional requirements (which describe what a system should do), NFRs
describe how a system should behave.
NFRs include:
Unit 8; CO-
3; SO-2 ;   1. Performance – System response time, latency, throughput, scalability.   [5]
BL-2, Low   2. Security – Authentication, authorization, data encryption, access control.
3. Reliability – System uptime, fault tolerance, recovery mechanisms.
4. Usability – User experience, UI/UX standards, accessibility.
5. Scalability – Ability to handle increasing load efficiently.
6. Maintainability – Ease of debugging, code modularity, versioning.
Interoperability – Ability to work with other systems (APIs, third-party
integrations).
d) Design the composite state for the Banking system, Consider ‘Account creation’
Unit-4, CO-
as the state.
2 ; SO-6;   [5]
Consider the composite state. States can be start, registering, loging in, account
BL-4, High
created, ending.
Q2   [20]
a) A healthcare organization is developing a Blood Bank Management System to
streamline blood donation and distribution. The system enables donors, patients,
hospital administrators, and inventory managers to interact efficiently, ensuring
the availability of blood when needed. Design Usecase diagram mentioning all the
required relations, use cases and actors.
CO-2; SO-2;   Ans: Actors and use cases are named properly.   [10
BL-2   ]
Notations   Naming conventions
Primary Actor/Secondary Actor Noun
Usecases   Verb
Association   Verb
Directed Association   Verb
********** 2 **********

[Text in pictures on this page, read by OCR]
Phases Inception

Business Modeling H :

Analysis

Design “a ee

Implementation

Test

Deployment

Phases

Configuration and
Change Management

Project Management
--- page 3 ---
usescases must be
Generalisation and   verbs   Actors:
specialisation   Nouns
b) Design Class diagram for an e-commerce company wants to develop an Online
Shopping System to allow customers to browse products, place orders, and
make payments online. The system should also enable administrators to manage
inventory and process orders efficiently.
Ans: Class diagram must have any five relations, class names and operations must
be named properly.
Notations   Naming conventions
3 partition, name-noun,
attribute-varible, methods-
CO-4; SO-6;   Class   verbs   [10
BL-4   ]
Cardinality will be used
Association   alongwith all the relations
Dependency
Aggregation
Composition
Interface-realisation
Association class
Generalisation-specialisation
Q3   [20]
a)   Differentiate between Prototype model and Spiral Model with their Advantages,
.   Disadvantages, SDLC, risk management.
CO-2; SO-1;
[10]
BL-2
b)   Explain the process of design, Coding and testing in Extreme programming with its
key features.
Design Process in XP
Key Characteristics of XP Design:
CO-4; SO-6;   •   Simple Design: Only design what is needed at the moment. Avoid complex   [10
BL-4   architectures.   ]
•   Refactoring: Continuously improve code structure without changing
functionality.
• CRC (Class-Responsibility-Collaboration) Cards: Used for brainstorming
object-oriented design.
********** 3 **********

[Text in pictures on this page, read by OCR]
Prototype Model Spiral Model

A working prototype (simplified version) of A risk-driven iterative model that follows a

the system is built first to understand user cyclic process of planning, risk assessment,
requirements better. development, and review.

Rapid prototyping followed by iterative Repeated phases in a spiral structure with
refinement. continuous risk analysis.

Low-risk management as the focus is on High-risk management due to continuous risk
gathering requirements. analysis in each phase.

High involvement; users test the prototype Moderate involvement; users provide feedback

and provide feedback. after each iteration.
--- page 4 ---
•   Spike Solutions: Quick experiments to explore solutions for complex
problems.
Key Characteristics of XP Coding:
•   Pair Programming: Two developers work together at one workstation.
•   Test-Driven Development (TDD): Write test cases before writing code.
•   Collective Code Ownership: Every developer can modify any part of the
code.
•   Continuous Integration: Merge and test code frequently.
Key Characteristics of XP Testing:
• Automated Unit Testing: Every feature must have test cases.
•   Frequent Customer Feedback: Customers validate features after each
iteration.
•   Continuous Integration Testing: Merge code daily to detect issues early.
• Acceptance Testing: Customers write tests to validate requirements.
Q4   [20]
CO-1; SO-2;   a)
BL-3   Design sequence diagram for the case mentioned in Q.2(b).   [10]
Airline Reservation System
b)   Description: A system for booking and managing airline tickets.
Components:
•   Flight Search Component (Handles flight availability search)
•   Booking Component (Manages ticket reservations)
•   Payment Component (Processes transactions)
CO-4; SO-6;   •   Passenger Management Component (Handles customer details)   [10]
BL-4   •   Notification Component (Sends booking confirmations)
•   Database Component (Stores passenger and flight details)
Ans: Interface(Provided and required), components( above mentioned 6
components), association, dependency..etc, must be shown in the design.
Q5   [20]
a)   Design Test Case Template for an Authentication System, consider at least four cases (Eg:
username and password).
CO-2; SO-6;
[10]
BL-3
b) What are boundary, control, and entity objects, and how do they relate to a sequence
diagram? Explain with an example.
CO-4; SO-6;
[10]
BL-4   Boundary Objects → Manage user interaction, Control Objects → Handle
application logic, Entity Objects → Represent data and business rules.
Q6   [20]
CO-4; SO-6;   a)   Differentiate between alpha, beta and gamma testing. Also identify these tests as alpha,
[10]
BL-4   beta and gamma testing.
********** 4 **********
--- page 5 ---
1   A mobile payment application is released to the public, and users report issues
like failed transactions or app crashes in real-world usage, in the customers
environment. Beta testing
2   A social media app releases a version to a select group of users to collect
feedback on usability, bugs, and performance before the official launch. Beta
testing
3   A new AI-based voice assistant is launched worldwide without prior controlled
testing, relying on post-launch feedback for improvements. Gamma Testing
4   A hospital management system is tested by internal developers to validate the
integration of patient records before deploying to hospitals. Alpha Testing
5   A new e-commerce website invites registered customers to test the site and
report issues before making it public. Beta Testing
b)   Explain Encapsulation, Abstraction, and Inheritance with suitable examples. How do these
concepts contribute to Object-Oriented Programming?
CO-3; SO-6;
[10]
BL-4
Q7   [20]
a) Why is high cohesion and low coupling is preferred in software design? Explain
with an example.
Cohesion refers to how closely related and focused the responsibilities of a
CO-3; SO-2;   module/class are.   [10
BL-3   High Cohesion: A module performs a single, well-defined task.   ]
Low Cohesion: A module handles multiple unrelated tasks, making it harder to
maintain.
Design Activity Diagram for an Online Food Ordering System, covering key steps like
b)   selecting food, ordering, making payment, and handling success or failure.
Activity Diagram
CO-4; SO-6;   Naming
BL-4   Notations   conventions   [10]
Start/End
Activity   Verbs
Transistion   Verbs
Fork/Join
Choice Point
********** 5 **********

[Text in pictures on this page, read by OCR]
Concept Definition Example

Encapsulation —_ Hides data and provides Private attributes in
controlled access via methods. BankAccount with getter/

setter.

Abstraction Hides implementation details Abstract class shape with
and provides only essential area() and perimeter() .
features.

Inheritance Allows one class to inherit Manager Class inheriting
attributes and methods from from employee .

another.
````
