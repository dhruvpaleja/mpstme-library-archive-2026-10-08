# Software Engineering: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper 0df84e66dc65

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_02/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Software Engineering/ANS_Software Engineering(703IT0C001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (24 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester II(Exam Year: 2025-2026)
Subject: Software Engineering
Date: 05 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 24 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
Q1   Answer briefly:   [20]
CO-1;   a.   Examine the differences between traditional process models and agile [5]
BL-4
processes.
Ans: Any 5 correct points 5 marks
Traditional Process
Aspect   Agile Processes
Models
Follows a sequential and
Development   Follows an iterative and
structured approach (e.g.,
Approach   incremental approach.
Waterfall model).
Requirements are fixed at Requirements can change
Requirement
the beginning and changes frequently during
Changes
are difficult.   development.
Limited customer
Continuous customer
Customer   involvement after
involvement throughout the
Involvement requirements are
project.
collected.
Development is slower
Development is faster with
Development because phases are
small iterations and quick
Speed   completed one after
releases.
another.
Testing is usually done   Testing is done
Testing   after development is   continuously during
completed.   development.
Focuses more on working
Documentatio Requires extensive
software than
n   documentation.
documentation.
********** 1 **********
--- page 2 ---
Teams often work   Teams work collaboratively
Team
individually with defined with frequent
Collaboration
roles.   communication.
Scrum, Extreme
Waterfall Model, Spiral   Programming (XP),
Examples
Model, V-Model.   Adaptive Software
Development (ASD).
CO-2;   b.   Explain the following requirement engineering task   [5]
BL-2
i.   Inception
ii.   Elicitation
iii.   Elaboration
iv.   Negotiation
v.   Validation
Correct answer 1 marks each
Task   Purpose   Example
Understand scope &   Identify features of online
Inception
feasibility   banking
Gather requirements from Ask users about bill
Elicitation
stakeholders   payments
Refine & analyze   Define transfer limits and
Elaboration
requirements   notifications
Resolve conflicts &   Agree on daily fund
Negotiation
prioritize   transfer limits
Ensure requirements are   Verify app meets all user
Validation
correct & complete   needs
CO-3;   c.   A company plans to develop an Online Food Ordering System where [5]
BL-3
customers can browse the menu, place orders, and make payments
through the application. The system allows customers to register and log
in before placing an order. While placing an order, the customer may
apply a discount coupon, which is optional. The system also provides a
payment process that always includes order confirmation. Based on this
scenario, identify the actors and use cases and determine the relationships
such as «include», «extend», and association in the Use Case Diagram
Correct identification of usecase, actor, relationship and diagram (5
marks)
1. Actors
• Customer – Primary user who browses the menu, places orders,
applies coupons, and makes payments.
• System – Implicit actor that handles order processing and payment
confirmation.
********** 2 **********
--- page 3 ---
2. Use Cases
1. Register
2. Login
3. Browse Menu
4. Place Order
5. Apply Discount Coupon (optional)
6. Make Payment
7. Order Confirmation
3. Relationships in Use Case Diagram
a) Association
Shows which actor interacts with which use case.
• Customer → Register
• Customer → Login
• Customer → Browse Menu
• Customer → Place Order
• Customer → Apply Discount Coupon
• Customer → Make Payment
b) «include» Relationships
Used for mandatory steps that always happen.
• Login «include» Register (if a new customer needs to register
first)
• Make Payment «include» Order Confirmation (system always
confirms the order after payment)
• Place Order «include» Login (customer must log in before placing
an order)
c) «extend» Relationships
Used for optional behavior.
• Apply Discount Coupon «extend» Place Order (optional; not
every order will have a coupon)
********** 3 **********
--- page 4 ---
CO-4;   d.   Justify the importance of software testing in the software development [5]
BL-3
life cycle.
Ans: Correct 5 points than 5 marks
Software testing is a critical activity in the SDLC that ensures the
software meets its requirements, works correctly, and is of high quality.
Here’s why it is important:
1. Detects Defects Early
Testing identifies bugs and errors in the software at an early stage, which
reduces costs and effort for fixing them later in the development process.
Example:
Finding a calculation error in a billing system during unit testing is easier
and cheaper to fix than after deployment.
2. Ensures Quality and Reliability
Testing ensures the software performs as expected under various
conditions, increasing user confidence and reliability.
Example:
Testing a banking application for multiple simultaneous transactions
ensures it works correctly without data loss.
********** 4 **********
--- page 5 ---
3. Validates Requirements
Through testing, developers verify that the software meets all functional
and non-functional requirements.
Example:
A food ordering system must correctly apply discount coupons and
confirm orders; testing validates this functionality.
4. Reduces Maintenance Cost
Identifying and fixing defects during development reduces the need for
expensive post-release maintenance.
Example:
Fixing a login bug before deployment prevents repeated user complaints
and emergency patches.
5. Improves User Experience
Testing helps ensure the software is user-friendly, responsive, and free
from critical failures, enhancing user satisfaction.
Example:
Testing a mobile app for smooth navigation and crash-free operation
improves overall user experience.
Q2   a   Describe the RAD (Rapid Application Development) model with the   [10]
CO-1;   help of neat diagram. Also state its advantages and disadvantages.
BL-2
Diagram (4 marks)
Explain with advantage and disadvantage (6 marks)
********** 5 **********
--- page 6 ---
RAD (Rapid Application Development) Model
Rapid Application Development (RAD) is a software development
model that emphasizes quick development and iteration of prototypes
with continuous user feedback. It focuses on speed, flexibility, and user
involvement rather than following a strict sequential process.
Phases of RAD Model
1. Requirement Planning
o Gather basic requirements quickly.
o Define system objectives, scope, and constraints.
2. User Design
o Develop prototypes and mock-ups.
o Users provide feedback and suggest improvements.
3. Construction
o Convert prototypes into functional components.
o Use iterative development for fast coding and testing.
4. Cutover
o Final system deployment.
o Conduct final testing, user training, and documentation.
Advantages of RAD Model
1. Fast Development
o Reduces overall development time with iterative
prototyping.
2. User Involvement
o Users provide feedback at each stage, improving
requirement accuracy.
3. Flexibility
o Easy to accommodate changes during development.
4. Early Detection of Issues
o Problems are identified during prototyping rather than
after full implementation.
Disadvantages of RAD Model
1. Requires Skilled Developers
********** 6 **********
--- page 7 ---
o Needs experienced developers who can work quickly and
iteratively.
2. Not Suitable for Large Projects
o Difficult to manage complex systems with many
interdependent modules.
3. Dependence on User Feedback
o Success relies heavily on active user participation.
4. High Cost
o Prototyping and iterative development can increase
development cost.
CO-3;   b   A school plans to develop a School Management System to manage its   [10]
BL-6
academic activities. The system contains School, Teachers, Students,
Classes, and ID Cards. A School has several Classes, and each class
contains many Students. Teachers teach different classes and subjects.
Every Student is issued a Student ID Card, and the ID card cannot exist
without the student. There are two types of students: Undergraduate
Student and Postgraduate Student, both derived from the Student class.
Based on this scenario, identify the classes and determine the
relationships and draw the UML Class Diagram.
Correct identification of class and relationship 5 marks
Class diagram 5 marks
Identified Classes
1. School
2. Class
3. Teacher
4. Student
o UndergraduateStudent (inherits from Student)
o PostgraduateStudent (inherits from Student)
5. IDCard
Relationships
1. Association
o Teachers teach different classes and subjects → Teacher
↔ Class (many-to-many)
********** 7 **********
--- page 8 ---
2. Aggregation
o School has several Classes → School ◇→ Class (whole-
part, Classes can exist independently)
3. Composition
o Student is issued an IDCard → Student ◆→ IDCard
(IDCard cannot exist without Student)
4. Generalization
o UndergraduateStudent and PostgraduateStudent inherit
from Student → Student → UndergraduateStudent /
PostgraduateStudent
UML Class Diagram Structure
Q3   a   A supermarket wants to implement an Online Grocery Ordering System. [10]
CO-2;   Customers can browse grocery items, place orders, and make online
BL-6
payments. The system records order details and customer information in
the database. After receiving the order, the store prepares the items and
sends them for delivery to the customer. Based on this scenario, draw
DFD Level 0, Level 1, and Level 2.
DFD level 0 3 marks
DFD level 1 4 marks
DFD level 2 3 marks
********** 8 **********
--- page 9 ---
CO-3;   b   A bank develops an Online Banking System that allows customers to   [10]
BL-6
transfer money between accounts. A customer first logs into the system
using a username and password. After successful authentication, the
customer selects the money transfer option and enters the receiver’s
account details and transfer amount. The system then verifies the
account details and checks the account balance in the bank database. If
the balance is sufficient, the system transfers the money and sends a
transaction confirmation message to the customer. Based on this
scenario, identify the objects involved and draw the Sequence Diagram
and Collaboration diagram.
Sequence diagram (5 marks)
Identified Objects
1. Customer – Initiates the money transfer.
2. OnlineBankingSystem – Handles the user interface and money
transfer process.
3. AuthenticationModule – Verifies username and password.
4. AccountDatabase – Stores account details and balance.
5. TransactionProcessor – Performs the money transfer.
********** 9 **********
--- page 10 ---
6. NotificationService – Sends confirmation message to the
customer.
Collaboration (5 marks)
Q4   a   Explain the Scrum framework used in Agile development with a neat   [10]
CO-1;   diagram. Describe the roles of Product Owner, Scrum Master, and
BL-2
Development Team.
Diagram 4marks
********** 10 **********
--- page 11 ---
Scrum Framework in Agile Development (6 marks)
Scrum is an Agile framework used for managing and completing
complex software projects. It emphasizes iterative development,
collaboration, and adaptability to changing requirements. Scrum divides
work into small, manageable units called sprints (usually 2–4 weeks),
allowing teams to deliver incremental value frequently.
Scrum Framework Components
1. Product Backlog – A prioritized list of features, enhancements,
and fixes that the product should have.
2. Sprint Backlog – A set of tasks selected from the product
backlog to be completed in a single sprint.
3. Sprints – Time-boxed iterations where the team works on the
selected backlog items.
4. Daily Scrum – Short daily meetings to discuss progress, plans,
and blockers.
5. Sprint Review – Meeting at the end of a sprint to demonstrate
completed work to stakeholders.
6. Sprint Retrospective – Meeting to reflect on the process and
improve team performance.
Roles in Scrum
1. Product Owner
• Represents stakeholders and customers.
********** 11 **********
--- page 12 ---
• Responsible for defining, prioritizing, and maintaining the
product backlog.
• Ensures the team works on the most valuable features.
Example: Prioritizing a “payment gateway integration” feature over
minor UI tweaks.
2. Scrum Master
•   Facilitates the Scrum process and removes obstacles for the
development team.
• Ensures the team follows Scrum principles and practices.
• Acts as a coach and mentor for the team.
Example: Helping the team resolve environment setup issues or
clarifying Scrum roles.
3. Development Team
•   Cross-functional team responsible for delivering potentially
shippable product increments in each sprint.
•   Self-organizing and decides how to accomplish sprint goals.
•   Includes developers, testers, designers, and other roles as
needed.
CO-2;   b   Discuss the steps in Transform mapping with an example.   [10]
BL-1
Ans: Transform Mapping in Software Engineering (2 marks)
Transform mapping is a technique used in structured analysis and
software design to derive a software architecture or data flow design
from a structured specification of the problem. It focuses on
transforming inputs into outputs and helps in identifying processes in a
data flow diagram (DFD).
Concept(2 marks)
• Transform mapping is applied when the output can be described
as a transformation of inputs.
•   It is particularly used when the system specification is functional
and deterministic (i.e., each input leads to a specific output).
********** 12 **********
--- page 13 ---
• Helps in creating modular, efficient, and maintainable process
structures.
Steps in Transform Mapping (6 marks)
1. Identify the Input and Output
o Determine all inputs and desired outputs of the system
from the specification.
o Example: Input: student marks; Output: student grades.
2. Identify the Differences
o Analyze how inputs must be transformed to achieve
outputs.
o Example: Calculating total marks, then mapping to
grades.
3. Determine Sub-transformations
o Divide the overall transformation into smaller,
manageable sub-transformations.
o Helps in designing modular processes in DFD.
o Example: Total marks calculation, Grade assignment,
Merit ranking.
4. Draw the Transform Structure
o Represent the main transformation as a parent process
and sub-transformations as child processes.
o Helps in creating process decomposition in DFD or
hierarchy diagrams.
5. Verify with the Specification
o Ensure that the transform structure correctly produces all
outputs from inputs.
o Adjust sub-transformations if necessary.
Q5   a   Explain the concept and purpose of System Testing in the Software   [10]
CO-4;   Development Life Cycle.
BL-2
Ans: System Testing in the Software Development Life Cycle (SDLC)
(2 marks)
System Testing is a level of software testing where the complete and
integrated software system is tested to verify that it meets its specified
********** 13 **********
--- page 14 ---
requirements. It is performed after integration testing and before
acceptance testing.
Concept of System Testing (4 marks)
• Focuses on validating the software as a whole rather than
individual components.
•   Tests the interactions between modules, the overall functionality,
performance, security, and reliability.
• Conducted in an environment that closely resembles the
production environment.
Key Features:
• Performed by independent testers (not the developers).
• Covers functional and non-functional testing.
• Uses test cases derived from system requirements.
Purpose of System Testing (4 marks)
1. Verification of Complete System
o Ensures that the entire system works according to
requirements.
o Confirms that all integrated components interact
correctly.
2. Validation Against Requirements
o Ensures the system meets functional, performance,
security, and usability requirements.
3. Detect Defects Before Release
o   Identifies defects that may arise due to module
interactions or system-level issues.
o Reduces the risk of failures in the production
environment.
4. Ensures Quality and Reliability
o Validates that the system is stable, reliable, and performs
as expected under different conditions.
5. Facilitates User Confidence
o A successfully tested system ensures that users can trust
the software, increasing acceptance.
********** 14 **********
--- page 15 ---
Types of System Testing
•   Functional Testing: Verifies system functions.
• Performance Testing: Evaluates speed, responsiveness, and
stability.
•   Security Testing: Checks for vulnerabilities and unauthorized
access.
•   Compatibility Testing: Ensures the system works across
different platforms.
•   Usability Testing: Assesses user interface and experience.
CO-3;   b   An insurance company uses a Claim Processing System to handle   [10]
BL-6
customer claims. A customer first submits a claim request with
supporting documents. The insurance officer verifies the documents and
assesses the claim details. If the claim is valid, the system approves the
claim and processes the payment. If the claim is invalid, the system
rejects the claim and informs the customer. Based on this scenario, draw
an Activity Diagram showing the claim processing workflow.
Correct flow and activities than 10 marks
Q6   a   Define Architecture. Discuss any four Architectural Styles.   [10]
CO-2;   Define Architecture 1 marks and any four architectural styles 2 marks
BL-2
each
Data centered architectures:
********** 15 **********
--- page 16 ---
• A data store will reside at the center of this architecture and is
accessed frequently by the other components that update, add,
delete, or modify the data present within the store.
• The figure illustrates a typical data-centered style. The client
software accesses a central repository. Variations of this
approach are used to transform the repository into a blackboard
when data related to the client or data of interest for the client
change the notifications to client software.
• This data-centered architecture will promote integrability. This
means that the existing components can be changed and new
client components can be added to the architecture without the
permission or concern of other clients.
• Data can be passed among clients using the blackboard
mechanism.
Advantages of Data centered architecture:
• Repository of data is independent of clients
•   Client work independent of each other
•   It may be simple to add additional clients.
• Modification can be very easy
Data centered architecture
2] Data flow architectures:
• This kind of architecture is used when input data is transformed
into output data through a series of computational manipulative
components.
• The figure represents pipe-and-filter architecture since it uses
both pipe and filter and it has a set of components called filters
connected by lines.
• Pipes are used to transmitting data from one component to the
next.
********** 16 **********
--- page 17 ---
• Each filter will work independently and is designed to take data
input of a certain form and produces data output to the next filter
of a specified form. The filters don't require any knowledge of
the working of neighboring filters.
•   If the data flow degenerates into a single line of transforms, then
it is termed as batch sequential. This structure accepts the batch
of data and then applies a series of sequential components to
transform it.
Advantages of Data Flow architecture:
•   It encourages upkeep, repurposing, and modification.
• With this design, concurrent execution is supported.
Disadvantage of Data Flow architecture:
•   It frequently degenerates to batch sequential system
• Data flow architecture does not allow applications that require
greater user engagement.
•   It is not easy to coordinate two different but related streams
Data Flow architecture
3] Call and Return architectures
It is used to create a program that is easy to scale and modify. Many
sub-styles exist within this category. Two of them are explained below.
• Remote procedure call architecture: This components is used to
present in a main program or sub program architecture
distributed among multiple computers on a network.
• Main program or Subprogram architectures: The main program
structure decomposes into number of subprograms or function
into a control hierarchy. Main program contains number of
subprograms that can invoke other components.
********** 17 **********
--- page 18 ---
4] Object Oriented architecture
The components of a system encapsulate data and the operations that
must be applied to manipulate the data. The coordination and
communication between the components are established via the
message passing.
Characteristics of Object Oriented architecture:
• Object protect the system's integrity.
• An object is unaware of the depiction of other items.
Advantage of Object Oriented architecture:
•   It enables the designer to separate a challenge into a collection
of autonomous objects.
• Other objects are aware of the implementation details of the
object, allowing changes to be made without having an impact
on other objects.
5] Layered architecture
• A number of different layers are defined with each layer
performing a well-defined set of operations. Each layer will do
some operations that becomes closer to machine instruction set
progressively.
• At the outer layer, components will receive the user interface
operations and at the inner layers, components will perform the
operating system interfacing(communication and coordination
with OS)
•   Intermediate layers to utility services and application software
functions.
• One common example of this architectural style is OSI-ISO
(Open Systems Interconnection-International Organisation for
Standardisation) communication system.
********** 18 **********
--- page 19 ---
Layered architecture
CO-4;   b   Explain the concept of software quality activities in software   [10]
BL-2
development.
Ans: Correct SQA activities than 10 marks
Software Quality Activities in Software Development
Software quality activities are systematic actions performed during the
software development life cycle (SDLC) to ensure that the software
product meets its requirements, is reliable, efficient, maintainable, and
satisfies user expectations. These activities aim to prevent defects,
detect errors early, and improve the overall quality of the software.
1. Quality Planning
•   Definition: Establishing quality objectives and defining how
they will be achieved.
•   Activities:
o Define quality standards (e.g., ISO, CMMI).
o Identify critical success factors.
o Plan for reviews, testing, and audits.
• Purpose: Ensures the development team knows what quality is
expected and how to achieve it.
2. Quality Assurance (QA)
•   Definition: Process-oriented activities to ensure the software
development process is being followed correctly.
•   Activities:
********** 19 **********
--- page 20 ---
o Process audits and inspections.
o Verification of adherence to coding standards.
o Training developers in best practices.
• Purpose: Prevents defects by improving the software
development process.
3. Quality Control (QC)
•   Definition: Product-oriented activities to identify defects in the
software product.
•   Activities:
o Testing (unit, integration, system, acceptance).
o Code reviews and inspections.
o Performance, security, and usability testing.
• Purpose: Detects and corrects defects in the software before
release.
4. Software Reviews and Audits
•   Definition: Formal examination of software work products.
• Types:
o Peer reviews: Developers check each other’s code.
o Walkthroughs: Step-by-step review of design or code.
o Audits: Formal evaluation against standards.
• Purpose: Identifies errors early, improves design and
documentation quality.
5. Testing
•   Definition: Execution of software to validate it meets
requirements.
• Types:
o Unit Testing
o Integration Testing
o System Testing
o Acceptance Testing
• Purpose: Ensures software is functional, reliable, and meets user
expectations.
********** 20 **********
--- page 21 ---
6. Continuous Improvement
•   Definition: Using feedback from QA, QC, and user experience to
improve processes and products.
•   Activities:
o Root cause analysis of defects.
o Updating processes based on lessons learned.
• Purpose: Achieves higher quality in future releases.
Summary
Software quality activities are a combination of planning, assurance,
control, reviews, testing, and continuous improvement. They help:
• Prevent defects through good processes.
• Detect errors in the product before release.
• Ensure the final software meets quality standards and user
expectations.
Q7   a   Explain how software myths affect software development projects.   [10]
CO-1;   Ans: Correct justification than 10 marks
BL-2
Software myths are common misconceptions or false beliefs about
software development. Believing in these myths can lead to poor
planning, wasted resources, delays, and project failures. Let’s explore
their impact:
1. Myth: Software development is easy and can be done quickly
•   Effect: Leads management to underestimate time, cost, and
effort, resulting in unrealistic schedules and overworked
developers.
• Example: Assuming a complex banking system can be
developed in a few weeks causes rushed coding and low-quality
software.
2. Myth: Adding more programmers speeds up the project
•   Effect: Can delay progress due to increased communication
overhead and onboarding time.
********** 21 **********
--- page 22 ---
• Example: Adding new developers to a half-finished project may
require experienced team members to train them, slowing down
the overall progress.
3. Myth: Software will never have bugs
•   Effect: Teams may skip proper testing, leading to software
failures, defects, and user dissatisfaction.
• Example: Releasing a mobile app without testing causes crashes
and poor user experience.
4. Myth: Once software is written, it doesn’t need maintenance
•   Effect: Ignoring maintenance planning can result in high costs,
outdated systems, and security issues over time.
• Example: Not updating an e-commerce website regularly may
expose it to security vulnerabilities.
5. Myth: Documentation is not important
•   Effect: Poor documentation leads to miscommunication,
difficulty in maintenance, and knowledge loss when team
members leave.
• Example: Future developers cannot understand the code
structure or system logic, increasing maintenance time.
CO-4;   b   Discuss with a neat diagram User Interface Design Process.   [10]
BL-2
Diagram (4 marks)
********** 22 **********
--- page 23 ---
User Interface (UI) Design Process (6 marks)
The User Interface Design Process is a systematic approach to
designing user interfaces that are easy to use, efficient, and visually
appealing. It ensures that users can interact with the system effectively
while achieving their goals.
Main Steps of the UI Design Process
1. Requirement Analysis
o Understand user needs, tasks, and goals.
o Gather functional and non-functional requirements.
2. Conceptual Design
o Create a high-level design of the interface.
o Identify information flow, navigation structure, and main
elements.
3. Prototyping
o Develop mock-ups or wireframes.
o Focus on layout, controls, and user interactions.
4. Evaluation & User Testing
o Test the prototype with real users.
o Collect feedback to identify usability issues.
5. Implementation
o Convert prototypes into working interfaces with code.
o Ensure consistency with design guidelines.
6. Deployment & Maintenance
********** 23 **********
--- page 24 ---
o Release the interface to users.
o Continuously update and improve based on feedback and
new requirements.
********** 24 **********
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper e18a2c3c87ff

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CSBS_7036/Software Engineering/ANS_Software Engineering(702IT0C016)_2025-2026.pdf`
- Text: mixed (17 pages), mean OCR confidence 80.7

````text
Note: The provided synoptic answer attempts to cover content from standard textbooks and
reference materials that closely align with the context of the question.
--- page 2 ---
Q1
[20]
a   Explain challenges in maintaining Legacy software.
Maintaining legacy software poses several significant challenges:
Outdated Technology: Old programming languages, tools, and platforms
make upgrades and integration with modern systems difficult.
Lack of Documentation: Incomplete or missing documentation hampers
[5 M]
understanding of system logic and dependencies.
CO-1;   1
Scarcity of Skilled Personnel: Few developers are familiar with obsolete
BL-L   marks
technologies, increasing maintenance cost and effort.
each
High Technical Debt: Frequent patches and quick fixes over time make the
codebase complex and error-prone.
Integration and Security Issues: Legacy systems often struggle to interface
with modern applications and lack up-to-date security mechanisms.
b Compare the Incremental and RAD models in terms of development speed,
modularity, and project size suitability.
5 clear points needs to be addressed
Development Speed: RAD (Rapid Application Development) is faster due to
prototyping and parallel component development, while Incremental
Model progresses in fixed sequential increments.
Modularity: Both are modular, but RAD emphasizes reusable components
and visual tools for rapid assembly, whereas Incremental focuses on   [5 M]
CO-
functional modules built in planned stages.   1
2,BL-
User Involvement: RAD involves high user interaction and feedback at   marks
L
every iteration, while Incremental has limited user involvement after   each
requirement finalization.
Project Size Suitability: RAD suits small to medium projects requiring
quick delivery; Incremental suits medium to large projects with well-defined
requirements.
Flexibility and Risk: RAD offers high flexibility but may lack control in large
systems; Incremental provides better risk management and stable progress
through phased delivery.
c What are the different types of relationships used in class diagrams? Explain
with suitable examples.
[5 M]
CO-3;   types of relationships in UML class diagrams are fundamental elements   1
BL-L   that define how classes and objects interact with one another within an   marks
object-oriented system. The main relationship types are:   each
Association:
Represents a structural connection between two classes showing how
instances of one class are linked to instances of another.
--- page 3 ---
Example:
teachers teach students.
Aggregation:
A special type of a   -
where the contained object can exist independently of the container.
Example:
teachers can still exist even if the department is removed.
Composition:
A stronger form of aggregation where the lifetime of the contained object
depends on the container.
Example:   if the house is
destroyed, its rooms cease to exist.
Inheritance (Generalization):
-
behavior from a superclass.
Example:
Dependency:
Indicates that one class depends on another for its behavior or data;
typically short-lived or temporary.
Example:
class to retrieve data.
These relationships together define the structural and behavioural
connections between components in an object-oriented system, ensuring
clear modularity and interaction mapping during system design.
d   Explain Unit testing with suitable example.
Unit Testing is the process of testing individual components or modules of a
software system in isolation to ensure that each unit performs as designed.
unit testing focuses on verifying module interfaces, local data structures,
boundary conditions, independent paths, and error-handling mechanisms.
It is usually performed by the developer during the coding phase. Stubs and
drivers are used to simulate interactions between modules, creating a
controlled test environment.
CO-4;   [5 M]
Example:- 2 marks
BL-L   3+2
Consider a function calculateTotal() in a billing application that sums item
prices and applies tax. A unit test for this function would input a known set
of prices and tax rate, then verify that the output matches the expected
total.
In summary, unit testing ensures the correctness of each individual
software component before integration, preventing error propagation and
reducing debugging effort later in development.
Q2   [20]
a   Describe the main phases of the Waterfall Model and explain why it is
considered a prescriptive process model.
ANS- as per standard text book,
CO-1;   Main Phases of the Waterfall Model: (6 marks)   [10 M]
BL-L   Communication   6+4
(Project initiation and requirements gathering)
The development process begins with interaction between the customer
and the development team.
--- page 4 ---
All functional and non-functional requirements are identified and
documented before moving forward.
Planning
(Estimating, scheduling, and tracking)
Project plans are created, including cost estimation, resource allocation,
and timelines.
Risks are identified and managed at this stage.
Modeling
(Analysis and design)
Requirements are analyzed and transformed into system and software
design models.
This includes architectural design and detailed component design.
Construction
(Coding and testing)
The actual software is developed based on the design models.
Unit testing and integration testing are performed to verify correctness.
Deployment
(Delivery, support, and feedback)
The completed software is delivered to the customer.
User feedback is collected, and maintenance or support activities are
carried out.
The Waterfall Model is one of the earliest and most structured software
development models. It follows a linear and sequential approach, where
progress flows steadily through a series of well-defined phases.
OR as per reference material
Main Phases of the Waterfall Model:
Requirements Analysis:
All system requirements are gathered and documented in detail. The focus
is on understanding what the system must do.
System Design:
Converts requirements into a blueprint for system architecture, data
structures, interfaces, and algorithms.
Implementation (Coding):
Developers translate the design into executable code using appropriate
programming languages and tools.
Testing:
The developed system is thoroughly tested for errors, performance, and
compliance with the requirements.
Deployment:
The tested software is delivered to the client or deployed into the
production environment.
Maintenance:
Post-deployment, the software undergoes maintenance activities like bug
fixes, updates, and performance improvements.
4 marks
Why It Is Considered a Prescriptive Process Model:
It prescribes a fixed set of process elements, including:
Framework activities
Tasks and actions
--- page 5 ---
Work products
Quality assurance checkpoints
Change control mechanisms
It enforces a predictable and well-defined process flow, where activities
must be completed in a specific order.
Each phase has clearly defined deliverables and documentation, leaving
little flexibility for revisiting earlier stages once a phase is completed.
Pressman states that prescriptive models are intended to bring order and
structure to software development by defining what must be done and
when during the project lifecycle.
The Waterfall Model is called prescriptive because it strictly defines and
enforces each phase, requiring that one phase be completed before the
next begins. It prescribes how the development process should proceed
in a controlled, document-driven, and phase-wise manner.
This rigidity provides predictability, clarity, and traceability, which are
valuable in projects with stable, well-understood requirements but limits
flexibility for iterative or changing needs.
b Design a labelled sequence diagram for following problem statement.
tests for students. When a student logs in through the Exam Portal UI, the
request is sent to the Exam Controller, which authenticates the student
using the student entity. Once authenticated, the Exam Controller retrieves
the exam details from the Exam entity and displays them to the student.
When the student starts the exam, the Exam Controller delivers one
question at a time by fetching it from the Question Bank entity. The student
submits answers through the Exam Portal UI, which are then passed to the
Exam Controller for storage in the Answer Sheet entity. After the student
Answer Sheet and initiates the e
CO-3;
[10 M]
BL-M
5 marks for class and 5 marks for labelled transition.
--- page 6 ---
Q3   [20]
a
Define the three key roles in the Scrum framework and mention their core
responsibilities
Ans- as per standard text book-
1. Product Owner 3 MARK
Definition:
The Product Owner represents the customer and stakeholders and is
responsible for maximizing the value of the product.
Core Responsibilities:
Defines and clearly communicates product requirements
Creates, maintains, and prioritizes the Product Backlog
Ensures backlog items are well understood by the team
Accepts or rejects completed work based on business value
2. Scrum Master- 3 MARK
Definition:
The Scrum Master is a facilitator and coach who ensures that Scrum
principles and practices are properly followed.
Core Responsibilities:
Facilitates Scrum events (Sprint Planning, Daily Scrum, Sprint Review,
Retrospective)
Removes impediments
Coaches the team in Agile and Scrum practices
Protects the team from external interruptions
CO2   Ensures continuous improvement of the Scrum process   [10 M]
,BL-H   3. Development Team 4 MARK   3+3+4
Definition:
The Development Team consists of professionals who build and deliver the
product increment.
Core Responsibilities:
Designs, develops, tests, and integrates product features
Delivers a potentially shippable increment at the end of each sprint
Self-organizes to decide how work is done
Estimates tasks and commits to sprint goals
Ensures product quality through continuous testing and integration
OR as per reference material
Definition & Responsibilities:
Represents the customer and business interests
Creates and maintains the Product Backlog, which is a prioritized list of
features that deliver business value
Assesses the backlog and updates priorities as required
Ensures that requirements reflect customer needs and business value
In the Scrum framework, three key roles form the foundation of an agile
development team. Each has distinct responsibilities that ensure smooth
project execution and product delivery.
1. Product Owner (PO):
--- page 7 ---
Core Responsibility: Represents the voice of the customer and defines the
product vision.
Key Duties:
Create and maintain the Product Backlog with prioritized user stories.
Ensure that the team works on features that deliver the highest business
value.
Clarify requirements and accept completed work that meets the Definition
of Done (DoD).
2. Scrum Master (SM):
Core Responsibility: Acts as a facilitator and coach for the Scrum team.
Key Duties:
Ensure Scrum principles and practices are properly followed.
Remove impediments or blockers affecting team progress.
Foster communication, collaboration, and continuous improvement within
the team.
Shield the team from external distractions and scope creep.
3. Development Team (Dev Team):
Core Responsibility: Responsible for delivering potentially shippable
product increments at the end of each sprint.
Key Duties:
Self-organize to plan and execute sprint work.
Collaborate daily to design, develop, test, and integrate features.
Maintain product quality through coding standards and testing.
Participate actively in sprint planning, reviews, and retrospectives.
b   Critically evaluate the importance of UML in bridging the gap between
Object-Oriented Analysis (OOA) and Object-Oriented Design (OOD).
Provide an example showing how a conceptual model transition into
specific UML diagrams.
Bridging Conceptual and Design Phases: UML provides a standard visual
language that connects Object-Oriented Analysis (understanding
requirements) with Object-Oriented Design (defining structure and
behavior).
Unified Representation: It translates conceptual models (like classes,
[10 M]
relationships, and interactions) into concrete design elements, ensuring
CO-3;   2
clarity between analysts and developers.
BL-H   marks
Improved Traceability: UML maintains consistency from high-level
each
requirements to low-level implementation by mapping use cases to class
and sequence diagrams.
Facilitates Design Validation: UML diagrams help verify that design
elements faithfully represent the analyzed business logic and system
behavior before coding.
Example: In a Library Management System, the OOA identifies entities like
Book, Member, and Librarian; these transition into UML Class Diagrams
showing relationships (association, inheritance) and Sequence Diagrams
depicting interactions like issueBook() or returnBook() during OOD.
--- page 8 ---
Q4   [20]
a   "Requirements Engineering is not just about documenting what users want,
but about balancing conflicting needs, resolving ambiguities, and ensuring
feasibility."
In light of this statement, critically discuss the role of Requirements
Engineering in the success of a software project.
Answer:
Requirements Engineering (RE) plays a critical role in determining the
success or failure of a software project. It goes far beyond simple
documentation   it ensures that the developed system truly meets business
objectives, user expectations, and technical feasibility.
Elicitation and Understanding of Needs:
RE involves gathering diverse stakeholder needs through interviews,
workshops, and observations. This helps uncover explicit and implicit
requirements, ensuring that no essential functionality is overlooked.
Conflict Resolution and Prioritization:   [10 M]
CO-2;   Stakeholders often have conflicting goals for example, marketing   2
BL-M   demands more features while developers prefer simplicity. RE balances   marks
these competing interests through negotiation and prioritization to achieve   each
realistic, value-driven outcomes.
Clarifying Ambiguities:
Ambiguous requirements lead to misinterpretation and costly rework.
Through techniques like prototyping and use-case modeling, RE ensures
that requirements are clear, consistent, and testable.
Feasibility and Risk Management:
RE assesses technical, financial, and operational feasibility before design
begins. Early validation of requirements prevents resource wastage on
impractical solutions.
Foundation for Design, Development, and Testing:
Well-engineered requirements form the baseline for all subsequent SDLC
phases they guide design decisions, implementation priorities, and test
case development, ensuring traceability and alignment with user goals.
b   Explain how a Level-0, Level-1, and Level-2 Data Flow Diagram (DFD) can be
applied in the design of a Student Enrollment System. How do successive
[10 M]
levels increase the detail and functional decomposition of the process?
CO-3;   2
BL-L   marks
each
Answer:
--- page 9 ---
LEVEL 0: CONTEXT DIAGRAM

Student —~ f Admin
Application Details
—* Enrollment Reports
Application

Submssion Enrollment

Confirmation «~
Message

™\ Invoices
“

Payment Details “™ ——__
Finance
Student Department
--- page 10 ---
LEVEL 1: SYSTEM OVERVIEW

Student Admin

mH,

Raw Application —»{ Application
Submission

2.0
Application
Submission

Application Details
/ iin Reports
3.0

D1 Student 0.0
Database Student
———, Enrollment Eligibility

Verification

D2
Fee Payment |< Invoices

y

Eligibility Check System

Request
x
4.0 /) =

Enrolloment
Confirmation

Finance

Student Department
--- page 11 ---
Level-0 DFD (Context Diagram): 2 MARKS
Represents the entire Student Enrollment System as a single process
interacting with external entities like Student, Admin, and Finance
Department.
Data flows include application submission, payment details, and
confirmation messages.
Level-1 DFD: 2 MARKS
Decomposes the main system into major sub-processes, such as Application
Submission, Eligibility Verification, Fee Payment, and Enrollment
Confirmation.
Introduces data stores like Student Database and Course Catalog to show
internal data flow.
Level-2 DFD: 2 MARKS
Provides detailed decomposition of Level-1 processes.
For example, Eligibility Verification can be split into Document Check,
Prerequisite Validation, and Seat Availability Check.
Similarly, Fee Payment can include Invoice Generation, Payment
Verification, and Receipt Issuance.
Successive Level Detailing: 2 MARKS
Each level adds more functional detail and data flow clarity, breaking down
complex processes into smaller, manageable tasks.
Functional Decomposition Benefit: 2 MARKS
--- page 12 ---
This hierarchical refinement ensures better understanding, simplifies
design, and helps developers and analysts verify that all system functions
are captured and logically connected before implementation.
Q5   [20]
a   Analyze the influence of data mining and data warehousing on architectural
decisions in large-scale information systems. How do these concepts guide
database design at both the architectural and component levels?
Answer:
1. Role of Data Mining and Data Warehousing in System Architecture:
Data warehousing and data mining profoundly shape the architectural
decisions of large-scale information systems.
Data Warehousing focuses on the collection, integration, and storage of
large volumes of historical and transactional data for analysis and decision-
making.
Data Mining applies analytical techniques on this data to discover hidden
patterns, trends, and correlations, supporting strategic business
intelligence.------------- 2 MARKS
2. Influence on Architectural Decisions: 4 MARKS
Separation of Operational and Analytical Workloads:
Architectural design must distinguish between OLTP (Online Transaction
Processing) systems handling daily transactions and OLAP (Online
Analytical Processing) systems for analysis.
analytical queries from burdening live systems.
CO-3;   [10 M]
Layered and Modular Architecture:
BL-M   2+4+4
Large-scale systems adopt multi-layered architectures data acquisition,
ETL (Extract-Transform-Load), storage, and presentation layers to support
data warehousing and mining effectively.
tools.
Data Integration and Consistency:
Architectural choices emphasize data normalization, cleansing, and
transformation to ensure consistent, high-quality data across distributed
sources before storage in the warehouse.
3. : 4 MARKS
Influence on Database Design (Architectural LevelSchema Design (Star and
Snowflake Models):
Data warehouses use dimensional modeling to structure data into fact and
dimension tables for efficient querying and reporting.
Fact table stores sales data; dimension tables store customer,
product, and time details.
Data Storage Optimization:
Large-scale systems use denormalization, indexing, and partitioning to
speed up analytical queries on massive datasets.
--- page 13 ---
Metadata Management:
Metadata repositories become a crucial architectural element for managing
data lineage, transformations, and schema evolution.
Influence on Database Design (Component Level):
ETL Components:
Design includes robust ETL pipelines that extract raw data, clean it, and load
it into the warehouse supporting accurate data mining.
Data Staging and Aggregation:
Intermediate staging areas and data marts are introduced to handle pre-
processing, aggregation, and summary generation efficiently.
Data Mining Integration:
Embedding mining algorithms (e.g., clustering, classification, association
rules) within the architecture guides the choice of indexing methods, data
partitioning, and computational resources.
Overall Impact:
Data warehousing ensures data availability, reliability, and performance
for analytics.
Data mining drives intelligent architectural designs that support predictive
modeling and decision support systems.
Together, they transform traditional databases into knowledge-driven,
scalable architectures capable of supporting real-time analytics and
business intelligence.
b Compare Agile and plan-driven approaches in terms of specification
and delivery, and justify situations where Agile is more effective.
Specification Approach:
Plan-driven: Requirements are fully defined upfront before development
begins.
Agile: Requirements evolve through continuous user feedback and iterative
refinement.
Delivery Cycle:
Plan-driven: Delivers the complete system at the end of the project.
Agile: Delivers working software in short, incremental iterations.
[10 M]
Flexibility to Change:
CO-2;   2
Plan-driven: Limited flexibility changes are costly once development
BL-H   marks
starts.
each
Agile: Highly adaptable welcomes changing requirements even late in
development.
Customer Involvement:
Plan-driven: Involvement mainly during requirement and acceptance
stages.
Agile: Continuous customer collaboration throughout the project.
When Agile is More Effective:
Agile is ideal for dynamic environments with evolving requirements, rapid
market changes, or innovative projects where frequent feedback,
flexibility, and early delivery are critical to success.
Q6   [20]
--- page 14 ---
a   Describe the major features of the Scrum methodology and analyze the role
of backlog and sprint cycles in managing change
FROM TEXT BOOK-
Major Features of Scrum Methodology 5 Marks
Scrum emphasizes the use of software process patterns that enable a team to
manage complex projects through an iterative approach. Its major features
include:
Small, Self-Organizing Teams: Scrum relies on small, highly motivated
project teams that are in control of their own work and foster heavy
collaboration.
Iterative Development: Work is partitioned into "packets" that are tackled
in short, fixed-duration cycles.
Minimal Work Products: The process focuses on delivering operational
software increments rather than comprehensive documentation.
Process Patterns: Scrum uses specific activities and roles to ensure
progress, such as:
Backlog: A prioritized list of project requirements or features that provide
business value for the customer.
Sprints: Work units consisting of a specific set of backlog items that must
be completed within a pre-defined time-box (typically 30 days).
Scrum Meetings: Short daily meetings (often 15 minutes) where the team
coordinates activities, assesses progress, and identifies obstacles.
Demos: Delivering the software increment to the customer so that
functionality can be demonstrated and evaluated.
CO-2;   [10 M]
Role of Backlog and Sprint Cycles in Managing Change 5 marks
BL-M   5+5
and manage change effectively during a project:
Dynamic Requirement Management (Backlog): The backlog is not a static
document; it is a prioritized list that can be updated as new requirements
emerge or business priorities shift. This allows the team to respond to change
rather than strictly following a rigid, initial plan.
Controlled Work Environments (Sprints): While the backlog is dynamic, the
sprint provides stability. Once a sprint begins, the items being worked on are
frozen; no changes are introduced until the next sprint cycle. This ensures
that the team can complete a functional increment without being disrupted by
constant mid-cycle "feature creep".
Continuous Feedback Loops: Because each sprint cycle ends with a demo
to the stakeholders, the team receives immediate feedback. This feedback
can then be used to update the backlog, ensuring that the next sprint cycle
incorporates any necessary changes or refinements requested by the
customer.
FROM Reference material -
1. Major Features of the Scrum Methodology: 5m
Iterative and Incremental Development:
Work is divided into short, time-boxed iterations called sprints (usually 2 4
weeks) to deliver working product increments frequently.
Defined Roles:
Scrum defines three primary roles   Product Owner (manages
--- page 15 ---
requirements), Scrum Master (facilitates the process), and Development
Team (builds the product).
Empirical Process Control:
Scrum relies on transparency, inspection, and adaptation to manage
progress and handle uncertainty effectively.
Regular Ceremonies:
Core events include Sprint Planning, Daily Scrum, Sprint Review, and
Retrospective to ensure communication, accountability, and continuous
improvement.
Working Software as Progress Measure:
Success is judged by the delivery of functional product increments, not by
documentation or percentage completion.
2. Role of Backlog and Sprint Cycles in Managing Change: 5m
Product Backlog Dynamic Requirement Management:
The Product Backlog contains prioritized user stories and features. It
evolves continuously based on stakeholder feedback and changing business
needs. This flexibility ensures Scrum can quickly respond to changes.
Sprint Backlog Short-Term Focus:
At the start of each sprint, the team selects items from the Product Backlog
to form a Sprint Backlog, focusing only on achievable goals for that sprint,
thus limiting change within the sprint duration.
Sprint Cycles Iterative Adaptation:
After each sprint, reviews and retrospectives provide opportunities to
incorporate feedback and reprioritize work, adapting to new
requirements or market shifts.
Change Control through Timeboxing:
Changes are deferred to the next sprint, ensuring stability within the
current iteration while allowing adaptability between sprints.
Continuous Value Delivery:
By combining backlog refinement and iterative sprint cycles, Scrum allows
teams to deliver incremental value, adapt to evolving requirements, and
continuously align with customer expectations.
b   Discuss which ISO 9126 characteristic efficiency, maintainability, or
portability should be prioritized for government-grade cybersecurity
systems and justify your reasoning.
Answer
Prioritize: Maintainability   for government-grade cybersecurity systems,
the ability to rapidly patch, harden, and adapt to emerging threats
CO-4;   [10 M]
outweighs raw efficiency or broad portability.
BL-L   3+3+4
Why maintainability first
Rapid vulnerability response: High maintainability (clean modular design,
clear interfaces, strong CI/CD, IaC) enables fast patching and hotfix
rollout, shrinking exposure windows during zero-days and APT incidents.
Secure configuration at scale: Maintainable systems support policy-as-
code, repeatable hardening baselines, and auditable change control core
to compliance (e.g., STIGs, CIS benchmarks).
--- page 16 ---
Lower defect density over time: Refactorable codebases and strong test
coverage reduce regression risk when introducing new crypto suites, auth
flows, or telemetry. -----3m
Where efficiency fits
Second priority: Crypto, packet processing, and analytics need predictable
latency and throughput (e.g., for real-time detection, deep packet
inspection). Optimize critical paths while preserving testability avoid
larity and security.
Where portability fits
Third priority (contextual): Useful for multi-domain deployments (on-
prem, air-gapped, sovereign clouds) and hardware refresh cycles. But
excessive abstraction for portability can increase attack surface and
operational complexity; keep it intentional (e.g., portable cryptographic
backends, OS-agnostic agents) without compromising maintainability.----3m
Practical rubric (prioritized controls)
Maintainability: MTTR for security patches, % code with unit/integration
tests, change-failure rate, config drift metrics.
Efficiency: P95 latency under load, CPU/memory per secured connection,
throughput with modern ciphers.
Portability: # of certified target platforms, build reproducibility,
dependency isolation (SBOM, container provenance). --- 4m
Q7   [20]
a   Design a labeled state transition diagram for following problem statement.
a Library Management System. The system should manage the complete
life cycle of a BookCopy object (an individual copy of a book), tracking how
its state changes as it is issued, returned, or reserved by users. Initially,
every BookCopy in the library flagged as Available, meaning it can be
borrowed by any registered member. When a Member places a hold
request for a BookCopy, its marked as Reserved. While in this state, the
book cannot be borrowed by anyone else. If the member fails to collect the
book within the allowed reservation period(15 days), the system
automatically changes its state back to Available. When a reserved book is
collected or directly borrowed (without reservation), its flagged as Issued.
CO-3;   During this state, the system tracks the issue date and due date. If the
BL-H   member returns the book on or before the due date, the state moves back   [10 M]
to Available. However, if the member fails to return the book by the due
date, the system marks it as Overdue. Once an overdue book is returned,
the system calculates a fine, records payment, and changes its flag back to
--- page 17 ---
5 marks for state, 5 marks for labelled message
b Judge whether adopting CMMI processes necessarily guarantees higher
software quality or whether contextual organizational factors play a greater
role support your argument.
-based answer:
Answer:
Adopting CMMI (Capability Maturity Model Integration) processes does
not automatically guarantee higher software quality. While CMMI
provides a structured framework for process improvement, the
organizational context, culture, and leadership commitment largely
determine its effectiveness.
Framework vs. Implementation Reality:
CMMI defines what to improve (process maturity) but not how to
implement it effectively. Without genuine adoption, it can become a   [10 M]
checklist exercise that adds bureaucracy rather than value.   2
CO-4;
Cultural and Human Factors:   marks
BL-H
Organizational culture communication, collaboration, and learning plays   each
a greater role. Teams that embrace continuous improvement and open   point
feedback achieve better quality, even with minimal formal structure.
Domain and Size Dependency:
In dynamic domains like startups or agile environments, rigid CMMI
processes may reduce responsiveness, while in large, regulated projects
(e.g., defense, aerospace), CMMI ensures consistency and compliance.
Leadership and Quality Mindset:
Success depends on management commitment to quality as a philosophy,
not just certification. Quality arises from empowering teams, not merely
following documented procedures.
Balanced Integration:
The best outcomes occur when CMMI is blended with adaptive practices
(like Agile) and tailored to organizational maturity ensuring processes
remain flexible, efficient, and people-focused.
````

## 2025-26 · Final-Exam · Sem 5 · Answer key · paper 0203493ad1ae

- Departments: Computer Science
- Programmes: BTech CS 7055
- Source: `02_Question_Papers/2025/Sem_05/Final-Exam/BTech_CS_7055/Software Engineering/ANS_Software Engineering(702IT0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Dec 2025
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / V/Semester IX/Semester V(Exam Year: 2025-2026)
Subject: Software Engineering
Date: 09 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 Questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   [20]
CO-1;   a Explain challenges in maintaining Legacy software.   [5 M]
BL-L   Maintaining legacy software poses several significant challenges:
1. Outdated Technology: Old programming languages, tools, and
platforms make upgrades and integration with modern systems
difficult.
2. Lack of Documentation: Incomplete or missing documentation
hampers understanding of system logic and dependencies.
3. Scarcity of Skilled Personnel: Few developers are familiar with
obsolete technologies, increasing maintenance cost and effort.
4. High Technical Debt: Frequent patches and quick fixes over time
make the codebase complex and error-prone.
5. Integration and Security Issues: Legacy systems often struggle to
interface with modern applications and lack up-to-date security
mechanisms.
CO-   b Compare the Incremental and RAD models in terms of development speed,   [5 M]
2,BL-L   modularity, and project size suitability.
1. Development Speed: RAD (Rapid Application Development) is faster
due to prototyping and parallel component development, while
Incremental Model progresses in fixed sequential increments.
********** 1 **********
--- page 2 ---
2. Modularity: Both are modular, but RAD emphasizes reusable
components and visual tools for rapid assembly, whereas Incremental
focuses on functional modules built in planned stages.
3. User Involvement: RAD involves high user interaction and feedback
at every iteration, while Incremental has limited user involvement
after requirement finalization.
4. Project Size Suitability: RAD suits small to medium projects requiring
quick delivery; Incremental suits medium to large projects with well-
defined requirements.
5. Flexibility and Risk: RAD offers high flexibility but may lack control
in large systems; Incremental provides better risk management and
stable progress through phased delivery.
CO-3;   c What are the different types of relationships used in class diagrams? Explain [5 M]
BL-L   with suitable examples.
According to the document “UML.pdf”, the types of relationships in UML
class diagrams are fundamental elements that define how classes and objects
interact with one another within an object-oriented system. The main
relationship types are:
1. Association:
Represents a structural connection between two classes showing how
instances of one class are linked to instances of another.
Example: A “Teacher” class associated with a “Student” class
indicates that teachers teach students.
2. Aggregation:
A special type of association representing a “whole-part” relationship
where the contained object can exist independently of the container.
Example: A “Department” class aggregates multiple “Teacher”
objects—teachers can still exist even if the department is removed.
3. Composition:
A stronger form of aggregation where the lifetime of the contained
object depends on the container.
Example: A “House” class composed of “Room” objects—if the
house is destroyed, its rooms cease to exist.
4. Inheritance (Generalization):
Defines an “is-a” relationship where a subclass inherits properties and
behavior from a superclass.
Example: A “Car” class inheriting from a general “Vehicle” class.
5. Dependency:
Indicates that one class depends on another for its behavior or data;
typically short-lived or temporary.
Example: A “ReportGenerator” class depends on a
“DatabaseConnection” class to retrieve data.
These relationships together define the structural and behavioral connections
between components in an object-oriented system, ensuring clear modularity
and interaction mapping during system design.
********** 2 **********
--- page 3 ---
CO-4;   d   Explain Unit testing with suitable example.   [5 M]
BL-L
Unit Testing is the process of testing individual components or modules of a
software system in isolation to ensure that each unit performs as designed.
According to testing.pdf, unit testing focuses on verifying module interfaces,
local data structures, boundary conditions, independent paths, and error-
handling mechanisms.
It is usually performed by the developer during the coding phase. Stubs and
drivers are used to simulate interactions between modules, creating a
controlled test environment.
Example:
Consider a function calculateTotal() in a billing application that sums
item prices and applies tax. A unit test for this function would input a known
set of prices and tax rate, then verify that the output matches the expected
total.
In summary, unit testing ensures the correctness of each individual software
component before integration, preventing error propagation and reducing
debugging effort later in development.
Q2   [20]
CO-1;   a Describe the main phases of the Waterfall Model and explain why it is   [10
BL-L   considered a prescriptive process model.   M]
The Waterfall Model is one of the earliest and most structured software
development models. It follows a linear and sequential approach, where
progress flows steadily through a series of well-defined phases.
Main Phases of the Waterfall Model:
1. Requirements Analysis:
All system requirements are gathered and documented in detail. The
focus is on understanding what the system must do.
2. System Design:
Converts requirements into a blueprint for system architecture, data
structures, interfaces, and algorithms.
3. Implementation (Coding):
Developers translate the design into executable code using appropriate
programming languages and tools.
4. Testing:
The developed system is thoroughly tested for errors, performance,
and compliance with the requirements.
5. Deployment:
The tested software is delivered to the client or deployed into the
production environment.
********** 3 **********
--- page 4 ---
6. Maintenance:
Post-deployment, the software undergoes maintenance activities like
bug fixes, updates, and performance improvements.
Why It Is Considered a Prescriptive Process Model:
The Waterfall Model is called prescriptive because it strictly defines and
enforces each phase, requiring that one phase be completed before the next
begins. It prescribes how the development process should proceed — in a
controlled, document-driven, and phase-wise manner.
This rigidity provides predictability, clarity, and traceability, which are
valuable in projects with stable, well-understood requirements but limits
flexibility for iterative or changing needs.
✅ In summary:
The Waterfall Model is a phase-driven, prescriptive process model that
enforces a disciplined, sequential flow — from requirements to maintenance
— ensuring structured development but offering limited adaptability to
change.
CO-3;   b Design a labelled sequence diagram for following problem statement.   [10
BL-M   M]
“A university is developing an Online Examination System to conduct digital
tests for students. When a student logs in through the Exam Portal UI, the
request is sent to the Exam Controller, which authenticates the student using
the student entity. Once authenticated, the Exam Controller retrieves the exam
details from the Exam entity and displays them to the student. When the
student starts the exam, the Exam Controller delivers one question at a time by
fetching it from the Question Bank entity. The student submits answers
through the Exam Portal UI, which are then passed to the Exam Controller for
storage in the Answer Sheet entity. After the student completes the test and
clicks “Submit,” the Exam Controller finalizes the Answer Sheet and initiates
the evaluation process.”
********** 4 **********
--- page 5 ---
5 marks for state and 5 marks for labelled transition.
Q3   [20]
CO2 ,BL- a   [10
H   M]
Define the three key roles in the Scrum framework and mention their core
responsibilities
In the Scrum framework, three key roles form the foundation of an agile
development team. Each has distinct responsibilities that ensure smooth
project execution and product delivery.
1. Product Owner (PO):
• Core Responsibility: Represents the voice of the customer and defines
the product vision.
• Key Duties:
o Create and maintain the Product Backlog with prioritized user
stories.
o Ensure that the team works on features that deliver the highest
business value.
o Clarify requirements and accept completed work that meets the
Definition of Done (DoD).
2. Scrum Master (SM):
• Core Responsibility: Acts as a facilitator and coach for the Scrum
team.
• Key Duties:
o Ensure Scrum principles and practices are properly followed.
o Remove impediments or blockers affecting team progress.
********** 5 **********
--- page 6 ---
o Foster communication, collaboration, and continuous
improvement within the team.
o Shield the team from external distractions and scope creep.
3. Development Team (Dev Team):
• Core Responsibility: Responsible for delivering potentially shippable
product increments at the end of each sprint.
• Key Duties:
o Self-organize to plan and execute sprint work.
o Collaborate daily to design, develop, test, and integrate
features.
o Maintain product quality through coding standards and testing.
o Participate actively in sprint planning, reviews, and
retrospectives.
✅ In summary:
The Product Owner manages the what (requirements), the Scrum Master
manages the how (process), and the Development Team delivers the actual
product increment, working together to achieve agile project success.
CO-3;   b Critically evaluate the importance of UML in bridging the gap between   [10
Object-Oriented Analysis (OOA) and Object-Oriented Design (OOD).
BL-H   M]
Provide an example showing how a conceptual model transition into
specific UML diagrams.
1. Bridging Conceptual and Design Phases: UML provides a standard
visual language that connects Object-Oriented Analysis
(understanding requirements) with Object-Oriented Design (defining
structure and behavior).
2. Unified Representation: It translates conceptual models (like classes,
relationships, and interactions) into concrete design elements,
ensuring clarity between analysts and developers.
3. Improved Traceability: UML maintains consistency from high-level
requirements to low-level implementation by mapping use cases to
class and sequence diagrams.
4. Facilitates Design Validation: UML diagrams help verify that design
elements faithfully represent the analyzed business logic and system
behavior before coding.
5. Example: In a Library Management System, the OOA identifies
entities like Book, Member, and Librarian; these transition into UML
Class Diagrams showing relationships (association, inheritance) and
Sequence Diagrams depicting interactions like issueBook() or
returnBook() during OOD.
********** 6 **********
--- page 7 ---
Q4   [20]
CO-2;   a "Requirements Engineering is not just about documenting what users want, but [10
BL-M   about balancing conflicting needs, resolving ambiguities, and ensuring M]
feasibility."
In light of this statement, critically discuss the role of Requirements
Engineering in the success of a software project.
Answer:
Requirements Engineering (RE) plays a critical role in determining the
success or failure of a software project. It goes far beyond simple
documentation—it ensures that the developed system truly meets business
objectives, user expectations, and technical feasibility.
1. Elicitation and Understanding of Needs:
RE involves gathering diverse stakeholder needs through interviews,
workshops, and observations. This helps uncover explicit and implicit
requirements, ensuring that no essential functionality is overlooked.
2. Conflict Resolution and Prioritization:
Stakeholders often have conflicting goals—for example, marketing
demands more features while developers prefer simplicity. RE
balances these competing interests through negotiation and
prioritization to achieve realistic, value-driven outcomes.
3. Clarifying Ambiguities:
Ambiguous requirements lead to misinterpretation and costly rework.
Through techniques like prototyping and use-case modeling, RE
ensures that requirements are clear, consistent, and testable.
4. Feasibility and Risk Management:
RE assesses technical, financial, and operational feasibility before
design begins. Early validation of requirements prevents resource
wastage on impractical solutions.
5. Foundation for Design, Development, and Testing:
Well-engineered requirements form the baseline for all subsequent
SDLC phases—they guide design decisions, implementation
priorities, and test case development, ensuring traceability and
alignment with user goals.
✅ In summary:
Requirements Engineering is the cornerstone of software success,
transforming vague ideas into actionable, conflict-free, and feasible
specifications. Effective RE minimizes misunderstandings, manages risks,
********** 7 **********
--- page 8 ---
and ensures that the final product is both technically sound and user-centric,
directly contributing to project success.
CO-3;   b Explain how a Level-0, Level-1, and Level-2 Data Flow Diagram (DFD) can   [10
be applied in the design of a Student Enrollment System. How do successive
BL-L   M]
levels increase the detail and functional decomposition of the process?
Here’s a concise, clear answer:
Answer:
1. Level-0 DFD (Context Diagram):
Represents the entire Student Enrollment System as a single process
interacting with external entities like Student, Admin, and Finance
Department.
Data flows include application submission, payment details, and
confirmation messages.
2. Level-1 DFD:
Decomposes the main system into major sub-processes, such as
Application Submission, Eligibility Verification, Fee Payment, and
Enrollment Confirmation.
Introduces data stores like Student Database and Course Catalog to
show internal data flow.
3. Level-2 DFD:
Provides detailed decomposition of Level-1 processes.
For example, Eligibility Verification can be split into Document
Check, Prerequisite Validation, and Seat Availability Check.
Similarly, Fee Payment can include Invoice Generation, Payment
Verification, and Receipt Issuance.
4. Successive Level Detailing:
Each level adds more functional detail and data flow clarity, breaking
down complex processes into smaller, manageable tasks.
5. Functional Decomposition Benefit:
This hierarchical refinement ensures better understanding, simplifies
design, and helps developers and analysts verify that all system
functions are captured and logically connected before implementation.
✅ In summary:
Level-0 shows the system’s boundaries, Level-1 defines its major functions,
and Level-2 elaborates internal process logic—together ensuring clarity,
completeness, and accurate system design.
********** 8 **********
--- page 9 ---
Q5   [20]
CO-3;   a Analyze the influence of data mining and data warehousing on architectural   [10
decisions in large-scale information systems. How do these concepts guide
BL-M   M]
database design at both the architectural and component levels?
Here’s a comprehensive and analytical answer:
Answer:
1. Role of Data Mining and Data Warehousing in System Architecture:
Data warehousing and data mining profoundly shape the architectural
decisions of large-scale information systems.
• Data Warehousing focuses on the collection, integration, and storage
of large volumes of historical and transactional data for analysis and
decision-making.
• Data Mining applies analytical techniques on this data to discover
hidden patterns, trends, and correlations, supporting strategic business
intelligence.
2. Influence on Architectural Decisions:
1. Separation of Operational and Analytical Workloads:
Architectural design must distinguish between OLTP (Online
Transaction Processing) systems handling daily transactions and
OLAP (Online Analytical Processing) systems for analysis.
→ This separation ensures performance optimization and prevents
analytical queries from burdening live systems.
2. Layered and Modular Architecture:
Large-scale systems adopt multi-layered architectures—data
acquisition, ETL (Extract-Transform-Load), storage, and presentation
layers—to support data warehousing and mining effectively.
→ Enables scalability, maintainability, and easy integration of
analytical tools.
3. Data Integration and Consistency:
Architectural choices emphasize data normalization, cleansing, and
transformation to ensure consistent, high-quality data across
distributed sources before storage in the warehouse.
3. Influence on Database Design (Architectural Level):
1. Schema Design (Star and Snowflake Models):
Data warehouses use dimensional modeling to structure data into fact
and dimension tables for efficient querying and reporting.
→ Example: Fact table stores sales data; dimension tables store
customer, product, and time details.
********** 9 **********
--- page 10 ---
2. Data Storage Optimization:
Large-scale systems use denormalization, indexing, and partitioning
to speed up analytical queries on massive datasets.
→ Improves performance for data mining operations.
3. Metadata Management:
Metadata repositories become a crucial architectural element for
managing data lineage, transformations, and schema evolution.
4. Influence on Database Design (Component Level):
1. ETL Components:
Design includes robust ETL pipelines that extract raw data, clean it,
and load it into the warehouse—supporting accurate data mining.
2. Data Staging and Aggregation:
Intermediate staging areas and data marts are introduced to handle
pre-processing, aggregation, and summary generation efficiently.
3. Data Mining Integration:
Embedding mining algorithms (e.g., clustering, classification,
association rules) within the architecture guides the choice of
indexing methods, data partitioning, and computational resources.
5. Overall Impact:
• Data warehousing ensures data availability, reliability, and
performance for analytics.
• Data mining drives intelligent architectural designs that support
predictive modeling and decision support systems.
Together, they transform traditional databases into knowledge-driven,
scalable architectures capable of supporting real-time analytics and
business intelligence.
✅ In Summary:
Data mining and data warehousing guide both architectural and component-
level database design by defining how data is structured, processed, and
analyzed. They promote modular, scalable architectures with optimized
schemas, ETL pipelines, and analytical layers—enabling large-scale
information systems to evolve into intelligent, decision-oriented platforms.
CO-2;   b Compare Agile and plan-driven approaches in terms of specification   [10
and delivery, and justify situations where Agile is more effective.
BL-H   M]
1. Specification Approach:
********** 10 **********
--- page 11 ---
o Plan-driven: Requirements are fully defined upfront before
development begins.
o Agile: Requirements evolve through continuous user feedback
and iterative refinement.
2. Delivery Cycle:
o Plan-driven: Delivers the complete system at the end of the
project.
o Agile: Delivers working software in short, incremental
iterations.
3. Flexibility to Change:
o Plan-driven: Limited flexibility—changes are costly once
development starts.
o Agile: Highly adaptable—welcomes changing requirements
even late in development.
4. Customer Involvement:
o Plan-driven: Involvement mainly during requirement and
acceptance stages.
o Agile: Continuous customer collaboration throughout the
project.
5. When Agile is More Effective:
Agile is ideal for dynamic environments with evolving requirements,
rapid market changes, or innovative projects where frequent feedback,
flexibility, and early delivery are critical to success.
Q6   [20]
CO-2;   a Describe the major features of the Scrum methodology and analyze the role of [10
BL-M   backlog and sprint cycles in managing change   M]
Here’s a clear, structured answer:
Answer:
1. Major Features of the Scrum Methodology:
1. Iterative and Incremental Development:
Work is divided into short, time-boxed iterations called sprints
(usually 2–4 weeks) to deliver working product increments frequently.
2. Defined Roles:
Scrum defines three primary roles — Product Owner (manages
requirements), Scrum Master (facilitates the process), and
Development Team (builds the product).
3. Empirical Process Control:
Scrum relies on transparency, inspection, and adaptation to manage
progress and handle uncertainty effectively.
4. Regular Ceremonies:
Core events include Sprint Planning, Daily Scrum, Sprint Review, and
Retrospective to ensure communication, accountability, and
continuous improvement.
********** 11 **********
--- page 12 ---
5. Working Software as Progress Measure:
Success is judged by the delivery of functional product increments,
not by documentation or percentage completion.
2. Role of Backlog and Sprint Cycles in Managing Change:
1. Product Backlog – Dynamic Requirement Management:
The Product Backlog contains prioritized user stories and features. It
evolves continuously based on stakeholder feedback and changing
business needs. This flexibility ensures Scrum can quickly respond to
changes.
2. Sprint Backlog – Short-Term Focus:
At the start of each sprint, the team selects items from the Product
Backlog to form a Sprint Backlog, focusing only on achievable goals
for that sprint, thus limiting change within the sprint duration.
3. Sprint Cycles – Iterative Adaptation:
After each sprint, reviews and retrospectives provide opportunities to
incorporate feedback and reprioritize work, adapting to new
requirements or market shifts.
4. Change Control through Timeboxing:
Changes are deferred to the next sprint, ensuring stability within the
current iteration while allowing adaptability between sprints.
5. Continuous Value Delivery:
By combining backlog refinement and iterative sprint cycles, Scrum
allows teams to deliver incremental value, adapt to evolving
requirements, and continuously align with customer expectations.
✅ In summary:
Scrum’s structured yet flexible framework—centered on backlog
management and sprint iterations—enables teams to manage change
dynamically, ensuring continuous delivery of value while maintaining
process stability.
CO-4;   b Discuss which ISO 9126 characteristic—efficiency, maintainability, or   [10
portability—should be prioritized for government-grade cybersecurity
BL-L   M]
systems and justify your reasoning.
Answer
Prioritize: Maintainability — for government-grade cybersecurity systems,
the ability to rapidly patch, harden, and adapt to emerging threats outweighs
raw efficiency or broad portability.
Why maintainability first
1. Rapid vulnerability response: High maintainability (clean modular
design, clear interfaces, strong CI/CD, IaC) enables fast patching and
hotfix rollout, shrinking exposure windows during zero-days and APT
incidents.
2. Secure configuration at scale: Maintainable systems support policy-
as-code, repeatable hardening baselines, and auditable change
control—core to compliance (e.g., STIGs, CIS benchmarks).
********** 12 **********
--- page 13 ---
3. Lower defect density over time: Refactorable codebases and strong
test coverage reduce regression risk when introducing new crypto
suites, auth flows, or telemetry.
Where efficiency fits
• Second priority: Crypto, packet processing, and analytics need
predictable latency and throughput (e.g., for real-time detection, deep
packet inspection). Optimize critical paths while preserving
testability—avoid “performance hacks” that erode clarity and security.
Where portability fits
• Third priority (contextual): Useful for multi-domain deployments (on-
prem, air-gapped, sovereign clouds) and hardware refresh cycles. But
excessive abstraction for portability can increase attack surface and
operational complexity; keep it intentional (e.g., portable
cryptographic backends, OS-agnostic agents) without compromising
maintainability.
Practical rubric (prioritized controls)
•   Maintainability: MTTR for security patches, % code with
unit/integration tests, change-failure rate, config drift metrics.
•   Efficiency: P95 latency under load, CPU/memory per secured
connection, throughput with modern ciphers.
•   Portability: # of certified target platforms, build reproducibility,
dependency isolation (SBOM, container provenance).
Conclusion
Choose maintainability as the primary lever to sustain security posture over
the system’s life; optimize efficiency on security-critical paths; adopt
targeted portability to meet deployment mandates—without inflating
complexity. This ordering best protects mission outcomes under evolving
threat landscapes.
Q7   [20]
CO-3;   a Design a labeled state transition diagram for following problem statement.   [10
BL-H   M]
“A university library wants to automate the process of book lending through a
Library Management System. The system should manage the complete life
cycle of a BookCopy object (an individual copy of a book), tracking how its
state changes as it is issued, returned, or reserved by users. Initially, every
BookCopy in the library flagged as Available, meaning it can be borrowed by
any registered member. When a Member places a hold request for a BookCopy,
its marked as Reserved. While in this state, the book cannot be borrowed by
anyone else. If the member fails to collect the book within the allowed
reservation period(15 days), the system automatically changes its state back to
Available. When a reserved book is collected or directly borrowed (without
reservation), its flagged as Issued. During this state, the system tracks the issue
date and due date. If the member returns the book on or before the due date,
the state moves back to Available. However, if the member fails to return the
book by the due date, the system marks it as Overdue. Once an overdue book
********** 13 **********
--- page 14 ---
is returned, the system calculates a fine, records payment, and changes its flag
back to Available.”
5 marks for classes, 5 marks for labelled message
CO-4;   b Judge whether adopting CMMI processes necessarily guarantees higher   [10
BL-H   software quality or whether contextual organizational factors play a greater   M]
role—support your argument.
Here’s a critical evaluation-based answer:
Answer:
Adopting CMMI (Capability Maturity Model Integration) processes does not
automatically guarantee higher software quality. While CMMI provides a
structured framework for process improvement, the organizational context,
culture, and leadership commitment largely determine its effectiveness.
1. Framework vs. Implementation Reality:
CMMI defines what to improve (process maturity) but not how to
implement it effectively. Without genuine adoption, it can become a
checklist exercise that adds bureaucracy rather than value.
2. Cultural and Human Factors:
Organizational culture—communication, collaboration, and
learning—plays a greater role. Teams that embrace continuous
improvement and open feedback achieve better quality, even with
minimal formal structure.
3. Domain and Size Dependency:
In dynamic domains like startups or agile environments, rigid CMMI
processes may reduce responsiveness, while in large, regulated
projects (e.g., defense, aerospace), CMMI ensures consistency and
compliance.
4. Leadership and Quality Mindset:
Success depends on management commitment to quality as a
philosophy, not just certification. Quality arises from empowering
teams, not merely following documented procedures.
5. Balanced Integration:
The best outcomes occur when CMMI is blended with adaptive
********** 14 **********
--- page 15 ---
practices (like Agile) and tailored to organizational maturity—
ensuring processes remain flexible, efficient, and people-focused.
✅ In summary:
CMMI provides the foundation for disciplined process improvement, but true
software quality depends on contextual organizational factors—culture,
leadership, and adaptability—rather than process compliance alone.
********** 15 **********
````

## 2025-26 · Final-Exam · Sem 9 · Answer key · paper 7ccb9200736c

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_09/Final-Exam/Integrated_Computer_7032/Software Engineering/ANS_Software Engineering(702IT0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 09 Dec 2025
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / V/Semester IX/Semester V(Exam Year: 2025-2026)
Subject: Software Engineering
Date: 09 Dec 2025   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 Questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   [20]
CO-1;   a Explain challenges in maintaining Legacy software.   [5 M]
BL-L   Maintaining legacy software poses several significant challenges:
1. Outdated Technology: Old programming languages, tools, and
platforms make upgrades and integration with modern systems
difficult.
2. Lack of Documentation: Incomplete or missing documentation
hampers understanding of system logic and dependencies.
3. Scarcity of Skilled Personnel: Few developers are familiar with
obsolete technologies, increasing maintenance cost and effort.
4. High Technical Debt: Frequent patches and quick fixes over time
make the codebase complex and error-prone.
5. Integration and Security Issues: Legacy systems often struggle to
interface with modern applications and lack up-to-date security
mechanisms.
CO-   b Compare the Incremental and RAD models in terms of development speed,   [5 M]
2,BL-L   modularity, and project size suitability.
1. Development Speed: RAD (Rapid Application Development) is faster
due to prototyping and parallel component development, while
Incremental Model progresses in fixed sequential increments.
********** 1 **********
--- page 2 ---
2. Modularity: Both are modular, but RAD emphasizes reusable
components and visual tools for rapid assembly, whereas Incremental
focuses on functional modules built in planned stages.
3. User Involvement: RAD involves high user interaction and feedback
at every iteration, while Incremental has limited user involvement
after requirement finalization.
4. Project Size Suitability: RAD suits small to medium projects requiring
quick delivery; Incremental suits medium to large projects with well-
defined requirements.
5. Flexibility and Risk: RAD offers high flexibility but may lack control
in large systems; Incremental provides better risk management and
stable progress through phased delivery.
CO-3;   c What are the different types of relationships used in class diagrams? Explain [5 M]
BL-L   with suitable examples.
According to the document “UML.pdf”, the types of relationships in UML
class diagrams are fundamental elements that define how classes and objects
interact with one another within an object-oriented system. The main
relationship types are:
1. Association:
Represents a structural connection between two classes showing how
instances of one class are linked to instances of another.
Example: A “Teacher” class associated with a “Student” class
indicates that teachers teach students.
2. Aggregation:
A special type of association representing a “whole-part” relationship
where the contained object can exist independently of the container.
Example: A “Department” class aggregates multiple “Teacher”
objects—teachers can still exist even if the department is removed.
3. Composition:
A stronger form of aggregation where the lifetime of the contained
object depends on the container.
Example: A “House” class composed of “Room” objects—if the
house is destroyed, its rooms cease to exist.
4. Inheritance (Generalization):
Defines an “is-a” relationship where a subclass inherits properties and
behavior from a superclass.
Example: A “Car” class inheriting from a general “Vehicle” class.
5. Dependency:
Indicates that one class depends on another for its behavior or data;
typically short-lived or temporary.
Example: A “ReportGenerator” class depends on a
“DatabaseConnection” class to retrieve data.
These relationships together define the structural and behavioral connections
between components in an object-oriented system, ensuring clear modularity
and interaction mapping during system design.
********** 2 **********
--- page 3 ---
CO-4;   d   Explain Unit testing with suitable example.   [5 M]
BL-L
Unit Testing is the process of testing individual components or modules of a
software system in isolation to ensure that each unit performs as designed.
According to testing.pdf, unit testing focuses on verifying module interfaces,
local data structures, boundary conditions, independent paths, and error-
handling mechanisms.
It is usually performed by the developer during the coding phase. Stubs and
drivers are used to simulate interactions between modules, creating a
controlled test environment.
Example:
Consider a function calculateTotal() in a billing application that sums
item prices and applies tax. A unit test for this function would input a known
set of prices and tax rate, then verify that the output matches the expected
total.
In summary, unit testing ensures the correctness of each individual software
component before integration, preventing error propagation and reducing
debugging effort later in development.
Q2   [20]
CO-1;   a Describe the main phases of the Waterfall Model and explain why it is   [10
BL-L   considered a prescriptive process model.   M]
The Waterfall Model is one of the earliest and most structured software
development models. It follows a linear and sequential approach, where
progress flows steadily through a series of well-defined phases.
Main Phases of the Waterfall Model:
1. Requirements Analysis:
All system requirements are gathered and documented in detail. The
focus is on understanding what the system must do.
2. System Design:
Converts requirements into a blueprint for system architecture, data
structures, interfaces, and algorithms.
3. Implementation (Coding):
Developers translate the design into executable code using appropriate
programming languages and tools.
4. Testing:
The developed system is thoroughly tested for errors, performance,
and compliance with the requirements.
5. Deployment:
The tested software is delivered to the client or deployed into the
production environment.
********** 3 **********
--- page 4 ---
6. Maintenance:
Post-deployment, the software undergoes maintenance activities like
bug fixes, updates, and performance improvements.
Why It Is Considered a Prescriptive Process Model:
The Waterfall Model is called prescriptive because it strictly defines and
enforces each phase, requiring that one phase be completed before the next
begins. It prescribes how the development process should proceed — in a
controlled, document-driven, and phase-wise manner.
This rigidity provides predictability, clarity, and traceability, which are
valuable in projects with stable, well-understood requirements but limits
flexibility for iterative or changing needs.
✅ In summary:
The Waterfall Model is a phase-driven, prescriptive process model that
enforces a disciplined, sequential flow — from requirements to maintenance
— ensuring structured development but offering limited adaptability to
change.
CO-3;   b Design a labelled sequence diagram for following problem statement.   [10
BL-M   M]
“A university is developing an Online Examination System to conduct digital
tests for students. When a student logs in through the Exam Portal UI, the
request is sent to the Exam Controller, which authenticates the student using
the student entity. Once authenticated, the Exam Controller retrieves the exam
details from the Exam entity and displays them to the student. When the
student starts the exam, the Exam Controller delivers one question at a time by
fetching it from the Question Bank entity. The student submits answers
through the Exam Portal UI, which are then passed to the Exam Controller for
storage in the Answer Sheet entity. After the student completes the test and
clicks “Submit,” the Exam Controller finalizes the Answer Sheet and initiates
the evaluation process.”
********** 4 **********
--- page 5 ---
5 marks for state and 5 marks for labelled transition.
Q3   [20]
CO2 ,BL- a   [10
H   M]
Define the three key roles in the Scrum framework and mention their core
responsibilities
In the Scrum framework, three key roles form the foundation of an agile
development team. Each has distinct responsibilities that ensure smooth
project execution and product delivery.
1. Product Owner (PO):
• Core Responsibility: Represents the voice of the customer and defines
the product vision.
• Key Duties:
o Create and maintain the Product Backlog with prioritized user
stories.
o Ensure that the team works on features that deliver the highest
business value.
o Clarify requirements and accept completed work that meets the
Definition of Done (DoD).
2. Scrum Master (SM):
• Core Responsibility: Acts as a facilitator and coach for the Scrum
team.
• Key Duties:
o Ensure Scrum principles and practices are properly followed.
o Remove impediments or blockers affecting team progress.
********** 5 **********
--- page 6 ---
o Foster communication, collaboration, and continuous
improvement within the team.
o Shield the team from external distractions and scope creep.
3. Development Team (Dev Team):
• Core Responsibility: Responsible for delivering potentially shippable
product increments at the end of each sprint.
• Key Duties:
o Self-organize to plan and execute sprint work.
o Collaborate daily to design, develop, test, and integrate
features.
o Maintain product quality through coding standards and testing.
o Participate actively in sprint planning, reviews, and
retrospectives.
✅ In summary:
The Product Owner manages the what (requirements), the Scrum Master
manages the how (process), and the Development Team delivers the actual
product increment, working together to achieve agile project success.
CO-3;   b Critically evaluate the importance of UML in bridging the gap between   [10
Object-Oriented Analysis (OOA) and Object-Oriented Design (OOD).
BL-H   M]
Provide an example showing how a conceptual model transition into
specific UML diagrams.
1. Bridging Conceptual and Design Phases: UML provides a standard
visual language that connects Object-Oriented Analysis
(understanding requirements) with Object-Oriented Design (defining
structure and behavior).
2. Unified Representation: It translates conceptual models (like classes,
relationships, and interactions) into concrete design elements,
ensuring clarity between analysts and developers.
3. Improved Traceability: UML maintains consistency from high-level
requirements to low-level implementation by mapping use cases to
class and sequence diagrams.
4. Facilitates Design Validation: UML diagrams help verify that design
elements faithfully represent the analyzed business logic and system
behavior before coding.
5. Example: In a Library Management System, the OOA identifies
entities like Book, Member, and Librarian; these transition into UML
Class Diagrams showing relationships (association, inheritance) and
Sequence Diagrams depicting interactions like issueBook() or
returnBook() during OOD.
********** 6 **********
--- page 7 ---
Q4   [20]
CO-2;   a "Requirements Engineering is not just about documenting what users want, but [10
BL-M   about balancing conflicting needs, resolving ambiguities, and ensuring M]
feasibility."
In light of this statement, critically discuss the role of Requirements
Engineering in the success of a software project.
Answer:
Requirements Engineering (RE) plays a critical role in determining the
success or failure of a software project. It goes far beyond simple
documentation—it ensures that the developed system truly meets business
objectives, user expectations, and technical feasibility.
1. Elicitation and Understanding of Needs:
RE involves gathering diverse stakeholder needs through interviews,
workshops, and observations. This helps uncover explicit and implicit
requirements, ensuring that no essential functionality is overlooked.
2. Conflict Resolution and Prioritization:
Stakeholders often have conflicting goals—for example, marketing
demands more features while developers prefer simplicity. RE
balances these competing interests through negotiation and
prioritization to achieve realistic, value-driven outcomes.
3. Clarifying Ambiguities:
Ambiguous requirements lead to misinterpretation and costly rework.
Through techniques like prototyping and use-case modeling, RE
ensures that requirements are clear, consistent, and testable.
4. Feasibility and Risk Management:
RE assesses technical, financial, and operational feasibility before
design begins. Early validation of requirements prevents resource
wastage on impractical solutions.
5. Foundation for Design, Development, and Testing:
Well-engineered requirements form the baseline for all subsequent
SDLC phases—they guide design decisions, implementation
priorities, and test case development, ensuring traceability and
alignment with user goals.
✅ In summary:
Requirements Engineering is the cornerstone of software success,
transforming vague ideas into actionable, conflict-free, and feasible
specifications. Effective RE minimizes misunderstandings, manages risks,
********** 7 **********
--- page 8 ---
and ensures that the final product is both technically sound and user-centric,
directly contributing to project success.
CO-3;   b Explain how a Level-0, Level-1, and Level-2 Data Flow Diagram (DFD) can   [10
be applied in the design of a Student Enrollment System. How do successive
BL-L   M]
levels increase the detail and functional decomposition of the process?
Here’s a concise, clear answer:
Answer:
1. Level-0 DFD (Context Diagram):
Represents the entire Student Enrollment System as a single process
interacting with external entities like Student, Admin, and Finance
Department.
Data flows include application submission, payment details, and
confirmation messages.
2. Level-1 DFD:
Decomposes the main system into major sub-processes, such as
Application Submission, Eligibility Verification, Fee Payment, and
Enrollment Confirmation.
Introduces data stores like Student Database and Course Catalog to
show internal data flow.
3. Level-2 DFD:
Provides detailed decomposition of Level-1 processes.
For example, Eligibility Verification can be split into Document
Check, Prerequisite Validation, and Seat Availability Check.
Similarly, Fee Payment can include Invoice Generation, Payment
Verification, and Receipt Issuance.
4. Successive Level Detailing:
Each level adds more functional detail and data flow clarity, breaking
down complex processes into smaller, manageable tasks.
5. Functional Decomposition Benefit:
This hierarchical refinement ensures better understanding, simplifies
design, and helps developers and analysts verify that all system
functions are captured and logically connected before implementation.
✅ In summary:
Level-0 shows the system’s boundaries, Level-1 defines its major functions,
and Level-2 elaborates internal process logic—together ensuring clarity,
completeness, and accurate system design.
********** 8 **********
--- page 9 ---
Q5   [20]
CO-3;   a Analyze the influence of data mining and data warehousing on architectural   [10
decisions in large-scale information systems. How do these concepts guide
BL-M   M]
database design at both the architectural and component levels?
Here’s a comprehensive and analytical answer:
Answer:
1. Role of Data Mining and Data Warehousing in System Architecture:
Data warehousing and data mining profoundly shape the architectural
decisions of large-scale information systems.
• Data Warehousing focuses on the collection, integration, and storage
of large volumes of historical and transactional data for analysis and
decision-making.
• Data Mining applies analytical techniques on this data to discover
hidden patterns, trends, and correlations, supporting strategic business
intelligence.
2. Influence on Architectural Decisions:
1. Separation of Operational and Analytical Workloads:
Architectural design must distinguish between OLTP (Online
Transaction Processing) systems handling daily transactions and
OLAP (Online Analytical Processing) systems for analysis.
→ This separation ensures performance optimization and prevents
analytical queries from burdening live systems.
2. Layered and Modular Architecture:
Large-scale systems adopt multi-layered architectures—data
acquisition, ETL (Extract-Transform-Load), storage, and presentation
layers—to support data warehousing and mining effectively.
→ Enables scalability, maintainability, and easy integration of
analytical tools.
3. Data Integration and Consistency:
Architectural choices emphasize data normalization, cleansing, and
transformation to ensure consistent, high-quality data across
distributed sources before storage in the warehouse.
3. Influence on Database Design (Architectural Level):
1. Schema Design (Star and Snowflake Models):
Data warehouses use dimensional modeling to structure data into fact
and dimension tables for efficient querying and reporting.
→ Example: Fact table stores sales data; dimension tables store
customer, product, and time details.
********** 9 **********
--- page 10 ---
2. Data Storage Optimization:
Large-scale systems use denormalization, indexing, and partitioning
to speed up analytical queries on massive datasets.
→ Improves performance for data mining operations.
3. Metadata Management:
Metadata repositories become a crucial architectural element for
managing data lineage, transformations, and schema evolution.
4. Influence on Database Design (Component Level):
1. ETL Components:
Design includes robust ETL pipelines that extract raw data, clean it,
and load it into the warehouse—supporting accurate data mining.
2. Data Staging and Aggregation:
Intermediate staging areas and data marts are introduced to handle
pre-processing, aggregation, and summary generation efficiently.
3. Data Mining Integration:
Embedding mining algorithms (e.g., clustering, classification,
association rules) within the architecture guides the choice of
indexing methods, data partitioning, and computational resources.
5. Overall Impact:
• Data warehousing ensures data availability, reliability, and
performance for analytics.
• Data mining drives intelligent architectural designs that support
predictive modeling and decision support systems.
Together, they transform traditional databases into knowledge-driven,
scalable architectures capable of supporting real-time analytics and
business intelligence.
✅ In Summary:
Data mining and data warehousing guide both architectural and component-
level database design by defining how data is structured, processed, and
analyzed. They promote modular, scalable architectures with optimized
schemas, ETL pipelines, and analytical layers—enabling large-scale
information systems to evolve into intelligent, decision-oriented platforms.
CO-2;   b Compare Agile and plan-driven approaches in terms of specification   [10
and delivery, and justify situations where Agile is more effective.
BL-H   M]
1. Specification Approach:
********** 10 **********
--- page 11 ---
o Plan-driven: Requirements are fully defined upfront before
development begins.
o Agile: Requirements evolve through continuous user feedback
and iterative refinement.
2. Delivery Cycle:
o Plan-driven: Delivers the complete system at the end of the
project.
o Agile: Delivers working software in short, incremental
iterations.
3. Flexibility to Change:
o Plan-driven: Limited flexibility—changes are costly once
development starts.
o Agile: Highly adaptable—welcomes changing requirements
even late in development.
4. Customer Involvement:
o Plan-driven: Involvement mainly during requirement and
acceptance stages.
o Agile: Continuous customer collaboration throughout the
project.
5. When Agile is More Effective:
Agile is ideal for dynamic environments with evolving requirements,
rapid market changes, or innovative projects where frequent feedback,
flexibility, and early delivery are critical to success.
Q6   [20]
CO-2;   a Describe the major features of the Scrum methodology and analyze the role of [10
BL-M   backlog and sprint cycles in managing change   M]
Here’s a clear, structured answer:
Answer:
1. Major Features of the Scrum Methodology:
1. Iterative and Incremental Development:
Work is divided into short, time-boxed iterations called sprints
(usually 2–4 weeks) to deliver working product increments frequently.
2. Defined Roles:
Scrum defines three primary roles — Product Owner (manages
requirements), Scrum Master (facilitates the process), and
Development Team (builds the product).
3. Empirical Process Control:
Scrum relies on transparency, inspection, and adaptation to manage
progress and handle uncertainty effectively.
4. Regular Ceremonies:
Core events include Sprint Planning, Daily Scrum, Sprint Review, and
Retrospective to ensure communication, accountability, and
continuous improvement.
********** 11 **********
--- page 12 ---
5. Working Software as Progress Measure:
Success is judged by the delivery of functional product increments,
not by documentation or percentage completion.
2. Role of Backlog and Sprint Cycles in Managing Change:
1. Product Backlog – Dynamic Requirement Management:
The Product Backlog contains prioritized user stories and features. It
evolves continuously based on stakeholder feedback and changing
business needs. This flexibility ensures Scrum can quickly respond to
changes.
2. Sprint Backlog – Short-Term Focus:
At the start of each sprint, the team selects items from the Product
Backlog to form a Sprint Backlog, focusing only on achievable goals
for that sprint, thus limiting change within the sprint duration.
3. Sprint Cycles – Iterative Adaptation:
After each sprint, reviews and retrospectives provide opportunities to
incorporate feedback and reprioritize work, adapting to new
requirements or market shifts.
4. Change Control through Timeboxing:
Changes are deferred to the next sprint, ensuring stability within the
current iteration while allowing adaptability between sprints.
5. Continuous Value Delivery:
By combining backlog refinement and iterative sprint cycles, Scrum
allows teams to deliver incremental value, adapt to evolving
requirements, and continuously align with customer expectations.
✅ In summary:
Scrum’s structured yet flexible framework—centered on backlog
management and sprint iterations—enables teams to manage change
dynamically, ensuring continuous delivery of value while maintaining
process stability.
CO-4;   b Discuss which ISO 9126 characteristic—efficiency, maintainability, or   [10
portability—should be prioritized for government-grade cybersecurity
BL-L   M]
systems and justify your reasoning.
Answer
Prioritize: Maintainability — for government-grade cybersecurity systems,
the ability to rapidly patch, harden, and adapt to emerging threats outweighs
raw efficiency or broad portability.
Why maintainability first
1. Rapid vulnerability response: High maintainability (clean modular
design, clear interfaces, strong CI/CD, IaC) enables fast patching and
hotfix rollout, shrinking exposure windows during zero-days and APT
incidents.
2. Secure configuration at scale: Maintainable systems support policy-
as-code, repeatable hardening baselines, and auditable change
control—core to compliance (e.g., STIGs, CIS benchmarks).
********** 12 **********
--- page 13 ---
3. Lower defect density over time: Refactorable codebases and strong
test coverage reduce regression risk when introducing new crypto
suites, auth flows, or telemetry.
Where efficiency fits
• Second priority: Crypto, packet processing, and analytics need
predictable latency and throughput (e.g., for real-time detection, deep
packet inspection). Optimize critical paths while preserving
testability—avoid “performance hacks” that erode clarity and security.
Where portability fits
• Third priority (contextual): Useful for multi-domain deployments (on-
prem, air-gapped, sovereign clouds) and hardware refresh cycles. But
excessive abstraction for portability can increase attack surface and
operational complexity; keep it intentional (e.g., portable
cryptographic backends, OS-agnostic agents) without compromising
maintainability.
Practical rubric (prioritized controls)
•   Maintainability: MTTR for security patches, % code with
unit/integration tests, change-failure rate, config drift metrics.
•   Efficiency: P95 latency under load, CPU/memory per secured
connection, throughput with modern ciphers.
•   Portability: # of certified target platforms, build reproducibility,
dependency isolation (SBOM, container provenance).
Conclusion
Choose maintainability as the primary lever to sustain security posture over
the system’s life; optimize efficiency on security-critical paths; adopt
targeted portability to meet deployment mandates—without inflating
complexity. This ordering best protects mission outcomes under evolving
threat landscapes.
Q7   [20]
CO-3;   a Design a labeled state transition diagram for following problem statement.   [10
BL-H   M]
“A university library wants to automate the process of book lending through a
Library Management System. The system should manage the complete life
cycle of a BookCopy object (an individual copy of a book), tracking how its
state changes as it is issued, returned, or reserved by users. Initially, every
BookCopy in the library flagged as Available, meaning it can be borrowed by
any registered member. When a Member places a hold request for a BookCopy,
its marked as Reserved. While in this state, the book cannot be borrowed by
anyone else. If the member fails to collect the book within the allowed
reservation period(15 days), the system automatically changes its state back to
Available. When a reserved book is collected or directly borrowed (without
reservation), its flagged as Issued. During this state, the system tracks the issue
date and due date. If the member returns the book on or before the due date,
the state moves back to Available. However, if the member fails to return the
book by the due date, the system marks it as Overdue. Once an overdue book
********** 13 **********
--- page 14 ---
is returned, the system calculates a fine, records payment, and changes its flag
back to Available.”
5 marks for classes, 5 marks for labelled message
CO-4;   b Judge whether adopting CMMI processes necessarily guarantees higher   [10
BL-H   software quality or whether contextual organizational factors play a greater   M]
role—support your argument.
Here’s a critical evaluation-based answer:
Answer:
Adopting CMMI (Capability Maturity Model Integration) processes does not
automatically guarantee higher software quality. While CMMI provides a
structured framework for process improvement, the organizational context,
culture, and leadership commitment largely determine its effectiveness.
1. Framework vs. Implementation Reality:
CMMI defines what to improve (process maturity) but not how to
implement it effectively. Without genuine adoption, it can become a
checklist exercise that adds bureaucracy rather than value.
2. Cultural and Human Factors:
Organizational culture—communication, collaboration, and
learning—plays a greater role. Teams that embrace continuous
improvement and open feedback achieve better quality, even with
minimal formal structure.
3. Domain and Size Dependency:
In dynamic domains like startups or agile environments, rigid CMMI
processes may reduce responsiveness, while in large, regulated
projects (e.g., defense, aerospace), CMMI ensures consistency and
compliance.
4. Leadership and Quality Mindset:
Success depends on management commitment to quality as a
philosophy, not just certification. Quality arises from empowering
teams, not merely following documented procedures.
5. Balanced Integration:
The best outcomes occur when CMMI is blended with adaptive
********** 14 **********
--- page 15 ---
practices (like Agile) and tailored to organizational maturity—
ensuring processes remain flexible, efficient, and people-focused.
✅ In summary:
CMMI provides the foundation for disciplined process improvement, but true
software quality depends on contextual organizational factors—culture,
leadership, and adaptability—rather than process compliance alone.
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper 61357df1aaee

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_02/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Software Engineering/ANS_Software Engineering(703IT0C001)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2026
- Text: text (20 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 2 Re-exam(Exam Year: 2025-2026)
Subject: Software Engineering
Date: 01 Jul 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 20 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks.
4. Question No.1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all 5 questions to be attempted.
Q1
Answer briefly   [20]
CO-1;   a.   Compare Waterfall model and Spiral model.
BL-4
(Correct 5 points 5 marks)
Parameter   Waterfall Model   Spiral Model
Linear and sequential   Iterative model with risk
Definition
development model   analysis
Step-by-step (one phase after Cyclical (repeated
Approach
another)   iterations)
Flexibility   Very less flexible   Highly flexible
User   Limited (mostly at beginning Continuous user
Involvement and end)   involvement
Risk   Strong focus on risk
No explicit risk analysis   [5]
Handling   analysis
Difficult to implement   Changes can be easily
Changes
changes   incorporated
Simple and easy to
Complexity   Complex to manage
understand
Small and well-defined   Large and complex
Suitable For
projects   projects
Testing   Done at the end   Done in every iteration
Higher cost due to
Cost   Lower cost
iterations
CO-2;   b.   Discuss any five-requirement engineering task.   [5]
BL-2
********** 1 **********
--- page 2 ---
(Any five-requirement engineering task each 1 marks)
Inception
Inception is the initial phase of requirement engineering where the basic
idea of the project is defined. It involves identifying stakeholders,
understanding the problem, and determining the scope of the system.
Elicitation
Elicitation is the process of gathering requirements from users and
stakeholders. It uses techniques such as interviews, questionnaires, and
observations to understand user needs.
Elaboration
Elaboration involves analyzing and refining the gathered requirements. It
helps in understanding the details, relationships, and constraints of the
system.
Negotiation
Negotiation is the process of resolving conflicts among different
requirements. It ensures that all stakeholders agree on the final set of
prioritized requirements.
Specification
Specification involves documenting the requirements in a clear and
structured format, usually in an SRS document, which serves as a
guideline for development.
CO-3;   c.   Enlist the steps to draw Use case diagram. Explain types of actors with
BL-3
suitable example.
(Steps 2 marks, types of actor 2 marks (1 marks each), example 1 marks)
Steps to Draw Use Case Diagram
1. Identify the System
Define the system boundary and what the system will do.
[5]
2. Identify Actors
Determine all users or external entities interacting with the system.
3. Identify Use Cases
List all the functions/services the system provides.
4. Establish Relationships
Connect actors to use cases using associations.
********** 2 **********
--- page 3 ---
5. Draw System Boundary
Represent the system with a rectangle and place use cases inside it.
6. Refine the Diagram
Add relationships like include, extend, and generalization if needed.
Types of Actors with Example
1. Primary Actor
The main user who directly interacts with the system.
Example: Customer in an online shopping system.
2. Secondary Actor
Supports the system but does not directly use it.
Example: Payment Gateway in online shopping.
CO-4;   d.   Which type of testing is conducted at end user sites and developers is not
BL-3
present. Justify your answer for the same.
(Correct identification and justification 5 marks)
Beta testing is performed by actual users in a real-world environment
after the software has been developed and internally tested (alpha
testing). In this phase, the software is released to a limited group of users
[5]
outside the organization. Since developers are not present, users interact
with the system independently and provide feedback based on real usage.
This helps in identifying defects, usability issues, and performance
problems that may not be detected during internal testing. Therefore, beta
testing ensures that the software meets user expectations before final
release.
Q2   a   Describe Prototyping model with the help of neat diagram. Also state its
CO-1;   advantages and disadvantages.
BL-2
(Explain 3 marks, diagram 3 marks, advantages and disadvantages 4
marks)
Prototyping Model   [10]
The Prototyping Model is a software development approach in which a
working model (prototype) of the system is built before developing the
final product. This prototype helps users understand the system and
provide feedback. Based on the feedback, the prototype is refined until
the final system is developed.
********** 3 **********
--- page 4 ---
Advantages
• Helps in better understanding of requirements
• Early detection of errors
• Improves user involvement and satisfaction
• Reduces risk of system failure
Disadvantages
• Can increase development cost and time
• Frequent changes may cause confusion
• Prototype may not be efficient for large systems
• Users may expect final system too early
CO-3;   b   In a food delivery system, a user places an order through a mobile
BL-6
application. The process begins when the user selects food items and
places an order. The application sends the order details to the restaurant
for confirmation. Once the restaurant accepts the order, the system
processes the payment through a payment gateway. After successful [10]
payment, a delivery partner is assigned to deliver the order. The user is
notified about the order status until it is delivered. Based on this scenario,
draw sequence diagram.
(Correct identification of object and correct diagram 10 marks)
********** 4 **********
--- page 5 ---
Q3   a   An online shopping system allows users to browse and purchase
CO-2;   products. The process begins when the user logs into the system and
BL-6
searches for products. The system retrieves product information from the
database and displays it. The user selects items and places an order. The
order details are processed by the system and sent to the payment module
for transaction processing. Once payment is successful, the order is [10]
confirmed and stored in the database. The system then updates inventory
and generates an invoice. Based on this scenario, draw DFD Level 0,
Level 1, and Level 2.
(DFD Level 0- 3marks, DFD Level 1- 4marks, DFD Level 2- 3 marks)
********** 5 **********
--- page 6 ---
CO-3;   b   In an ATM system, a customer performs a sequence of actions to
BL-6
withdraw cash. The process begins when the customer inserts the card
and enters the PIN. The system verifies the PIN, and if it is valid, the
customer selects the withdrawal option and enters the amount. The
system checks the account balance. If sufficient funds are available, cash
[10]
is dispensed; otherwise, an error message is displayed. The transaction is
recorded, and the card is ejected, ending the process. Based on this
scenario, draw activity diagram.
Correct identification of activity and notation 10 marks
********** 6 **********
--- page 7 ---
Q4   a   Describe the different principles to achieve agility. Explain Capability
CO-1;   Maturity Model Integration with neat diagram.
BL-2
Agile Principle (3 marks)
[10]
CMMI explain 4 marks
1. Maturity level 1 : Initial
********** 7 **********
--- page 8 ---
•   processes are poorly managed or controlled.
•   unpredictable outcomes of processes involved.
• ad hoc and chaotic approach used.
• No KPAs (Key Process Areas) defined.
• Lowest quality and highest risk.
2. Maturity level 2 : Managed
• requirements are managed.
•   processes are planned and controlled.
•   projects are managed and implemented according to their
documented plans.
• This risk involved is lower than Initial level, but still
exists.
•   Quality is better than Initial level.
3. Maturity level 3 : Defined
•   processes are well characterized and described using
standards, proper procedures, and methods, tools, etc.
• Medium quality and medium risk involved.
• Focus is process standardization.
4. Maturity level 4 : Quantitatively managed
•   quantitative objectives for process performance and
quality are set.
•   quantitative   objectives   are   based   on   customer
requirements, organization needs, etc.
•   process performance measures are analyzed quantitatively.
•   higher quality of processes is achieved.
• lower risk
5. Maturity level 5 : Optimizing
• continuous improvement   in   processes and   their
performance.
• improvement has to be both incremental and innovative.
•   highest quality of processes.
• lowest risk in processes and their performance.
Diagram 3 marks
********** 8 **********
--- page 9 ---
CO-2;   b   Define Architecture Design. Explain with an example architectural
BL-1
context diagram.
Architecture Design (2 marks)
The software needs an architectural design to represent the design of the
software. IEEE defines architectural design as "the process of defining a
collection of hardware and software components and their interfaces to
establish the framework for the development of a computer system." The
software that is built for computer-based systems can exhibit one of these
many architectural styles.
Architectural context diagram. (diagram 4 marks, Theory 4 marks)   [10]
Q5   a
CO-4;   Explain Integration testing and describe its different approaches.
[10]
BL-2   Integration Testing (4 marks)
********** 9 **********
--- page 10 ---
Integration Testing is a Software Testing Technique that focuses on
verifying the interactions and data exchange between different
components or modules of a Software Application. The goal of
Integration Testing is to identify any problems or bugs that arise when
different components are combined and interact with each other.
It mainly tests interface between two software units or modules. It
focuses on determining the correctness of the interface. Once all the
modules have been unit-tested, integration testing is performed.
Integration testing can be done by picking module by module. This can
be done so that there is a proper sequence to be followed.
Exposing the defects is the major focus of the integration testing and the
time of interaction between the integrated units.
Bottom-Up Integration Testing (3 marks)
In bottom-up testing, each module at lower levels are tested with higher
modules until all modules are tested. The primary purpose of this
integration testing is that each subsystem tests the interfaces among
various modules making up the subsystem. This integration testing uses
test drivers to drive and pass appropriate data to the lower-level modules.
Advantages of Bottom-Up Integration Testing
•   In bottom-up testing, no stubs are required.
• A principal advantage of this integration testing is that several
disjoint subsystems can be tested simultaneously.
•   It is easy to create the test conditions.
• Best for applications that uses bottom up design approach.
•   It is Easy to observe the test results.
Disadvantages of Bottom-Up Integration Testing
• Driver modules must be produced.
•   In this testing, the complexity that occurs when the system is made
up of a large number of small subsystems.
• As Far modules have been created, there is no working model can
be represented.
Top-Down Integration Testing (3 marks)
Top-down integration testing technique is used in order to simulate the
behaviour of the lower-level modules that are not yet integrated. In this
********** 10 **********
--- page 11 ---
integration testing, testing takes place from top to bottom. First, high-
level modules are tested and then low-level modules and finally
integrating the low-level modules to a high level to ensure the system is
working as intended.
Advantages of Top-Down Integration Testing
•   Separately debugged module.
• Few or no drivers needed.
•   It is more stable and accurate at the aggregate level.
•   Easier isolation of interface errors.
•   In this, design defects can be found in the early stages.
Disadvantages of Top-Down Integration Testing
• Needs many Stubs.
• Modules at lower level are tested inadequately.
•   It is difficult to observe the test output.
•   It is difficult to stub design.
CO-3;   b   A student goes through different states in an exam process. Initially, the
BL-6
student is in the Registered state. After appearing for the exam, the state
changes to Exam Given. Once results are declared, the student moves to
[10]
either Pass or Fail state. Based on this scenario, draw State transition
diagram.
(Identification of correct states and notation 10 marks)
********** 11 **********
--- page 12 ---
Q6   a   Explain Architectural styles with suitable examples.
CO-2;   (5 architectural style each for 2 marks)
BL-2
1] Data centered architectures:
• A data store will reside at the center of this architecture and is
accessed frequently by the other components that update, add,
delete, or modify the data present within the store.
• The figure illustrates a typical data-centered style. The client
software accesses a central repository. Variations of this approach
are used to transform the repository into a blackboard when data
related to the client or data of interest for the client change the
notifications to client software.
[10]
• This data-centered architecture will promote integrability. This
means that the existing components can be changed and new client
components can be added to the architecture without the
permission or concern of other clients.
• Data can be passed among clients using the blackboard
mechanism.
Advantages of Data centered architecture:
• Repository of data is independent of clients
•   Client work independent of each other
•   It may be simple to add additional clients.
• Modification can be very easy
********** 12 **********
--- page 13 ---
Data centered architecture
2] Data flow architectures:
• This kind of architecture is used when input data is transformed
into output data through a series of computational manipulative
components.
• The figure represents pipe-and-filter architecture since it uses
both pipe and filter and it has a set of components called filters
connected by lines.
• Pipes are used to transmitting data from one component to the
next.
• Each filter will work independently and is designed to take data
input of a certain form and produces data output to the next filter
of a specified form. The filters don't require any knowledge of the
working of neighboring filters.
•   If the data flow degenerates into a single line of transforms, then
it is termed as batch sequential. This structure accepts the batch
of data and then applies a series of sequential components to
transform it.
Advantages of Data Flow architecture:
•   It encourages upkeep, repurposing, and modification.
• With this design, concurrent execution is supported.
Disadvantage of Data Flow architecture:
•   It frequently degenerates to batch sequential system
• Data flow architecture does not allow applications that require
greater user engagement.
•   It is not easy to coordinate two different but related streams
********** 13 **********
--- page 14 ---
Data Flow architecture
3] Call and Return architectures
It is used to create a program that is easy to scale and modify. Many sub-
styles exist within this category. Two of them are explained below.
• Remote procedure call architecture: This components is used to
present in a main program or sub program architecture distributed
among multiple computers on a network.
• Main program or Subprogram architectures: The main program
structure decomposes into number of subprograms or function
into a control hierarchy. Main program contains number of
subprograms   that   can   invoke   other   components.
4] Object Oriented architecture
The components of a system encapsulate data and the operations that
must be applied to manipulate the data. The coordination and
communication between the components are established via the message
passing.
Characteristics of Object Oriented architecture:
• Object protect the system's integrity.
• An object is unaware of the depiction of other items.
Advantage of Object Oriented architecture:
•   It enables the designer to separate a challenge into a collection of
autonomous objects.
********** 14 **********
--- page 15 ---
• Other objects are aware of the implementation details of the
object, allowing changes to be made without having an impact on
other objects.
5] Layered architecture
• A number of different layers are defined with each layer
performing a well-defined set of operations. Each layer will do
some operations that becomes closer to machine instruction set
progressively.
• At the outer layer, components will receive the user interface
operations and at the inner layers, components will perform the
operating system interfacing(communication and coordination
with OS)
•   Intermediate layers to utility services and application software
functions.
• One common example of this architectural style is OSI-ISO (Open
Systems   Interconnection-International   Organisation   for
Standardisation) communication system.
Layered architecture
CO-4;   b   Explain the quality factors defined in ISO 9126.
BL-2
(Classification of Quality Model 1 marks)
[10]
Furthermore, the first part i.e. the Quality model is concerned classified
into two categories as depicted in the following figure:
********** 15 **********
--- page 16 ---
Functionality
The functions are those that will satisfy implied needs.
Suitability
Accuracy
Interoperability
Security
Functionality Compliance
Reliability (1marks)
A set of attributes that will bear on the capability of software to maintain
the level of performance.
Maturity
Fault Tolerance
Recoverability
Reliability Compliance
Usability (1marks)
A set of attributes that bear on the effort needed for use by an implied set
of users.
Understandability
Learnability
Operability
Attractiveness
Usability Compliance
Efficiency (1marks)
********** 16 **********
--- page 17 ---
A set of attributes that bear on the relationship between the level of
performance of the software under stated conditions.
Time Behavior
Resource Utilization
Efficiency Compliance
Maintainability(1marks)
A set of attributes that bear on the effort needed to make specified
modifications.
Analyzability
Changeability
Stability
Testability
Maintainability Compliance
Portability (1marks)
A set of attributes that bear on the ability of software to be transferred
from one environment to another.
Adaptability
Installability
Co-existence
Replaceability
Portability Compliance
Quality in Use Model (2 marks)
It identifies the four quality characteristics.
Effectiveness
Productivity
Safety
Satisfaction
External Metrics (1 marks)
External Metrices is used to describe external metrics that are used to
measure characteristics and sub-characteristics which are identified in
quality model.
********** 17 **********
--- page 18 ---
Internal Metrics (1 marks)
Internal Metrices is used to describe internal metrics that are used to
measure characteristics and sub-characteristics which are identified in
quality model.
Quality in use metrics
Quality in use metrices is used to identify metrics that are used to measure
the effects of combined quality characteristics for users.
Q7   a   Define software engineering and discuss various characteristics of
CO-1;   software engineering in detail.
BL-2
Software Engineering (4 marks)
• Software Engineering is the systematic process of designing,
developing, testing, and maintaining software using techniques
like requirements analysis, design, testing, and maintenance.
•   It ensures software is high-quality, reliable, and maintainable,
especially for large software systems.
• Software Engineering improves efficiency, quality, and budget
management, helping deliver software on time, within budget, and
meeting all requirements
•   It continuously adopting new tools and methodologies to handle
complexity and evolving technologies.   [10]
1. Software is Developed, Not Manufactured (2 marks)
• Hardware is manufactured in factories, but software is developed
(designed and coded)
• Cost is mainly in development, not in production
• Once developed, copies can be made at almost zero cost
Example:
Creating software like an app takes effort, but copying it is easy.
2. Software Does Not Wear Out (2 marks)
• Hardware components wear out over time due to physical usage
• Software does not degrade physically
********** 18 **********
--- page 19 ---
However:
• Software may deteriorate due to changes, updates, and bugs
• This is called software deterioration
Example:
Frequent updates may introduce errors, making software less efficient.
3. Software is Custom-Built (2 marks)
• Most software is developed for specific requirements
• Unlike hardware, it is not mass-produced in the same way
But modern trend:
• Use of reusable components, libraries, and frameworks
CO-4;   b   Discuss the following:
BL-2
i.   Place the user in control
ii.   Make the interface consistent
i. Place the User in Control (5 marks)
This principle means the system should be designed in such a way that
the user feels in charge of the interaction, not the system.
Key Points:
Flexible interaction
Users should be able to choose how they perform tasks (e.g., shortcuts,
menus)
[10]
Undo/Redo options
Users should be able to easily correct mistakes
Interruptible processes
Users should be able to cancel or pause operations
User-friendly navigation
Easy movement between screens/pages
Avoid forcing actions
System should not impose unnecessary steps
Provide feedback
Inform users about system status (loading, success, error)
Example:
********** 19 **********
--- page 20 ---
“Cancel” button during file upload
“Undo delete” option in apps
This increases user satisfaction and confidence
✅ ii. Make the Interface Consistent (5 marks)
This principle ensures that the interface behaves uniformly throughout
the system.
Key Points:
Consistent layout
Same design structure across all screens
Uniform terminology
Same words used for same actions (e.g., “Save” everywhere)
Standard icons and colors
Same symbols represent same actions
Consistent navigation
Menus and buttons behave similarly
Follow platform standards
Align with OS/app guidelines (e.g., mobile UI patterns)
Example:
Same “Submit” button style on all pages
Same color for error messages (e.g., red)
This reduces learning effort and confusion
********** 20 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 7cb7a1e98100

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CSBS_7036/Software Engineering/ANS_Software Engineering(702IT0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Software Engineering
Date: 02 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 Questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   [20]
CO-1;   a Differentiate between generic software products and customized software   [5 M]
BL-L   solutions. Which type is likely to yield higher revenue for a company, and
what factors contribute to this difference?
1. Generic Software Products:
• Generic software products are developed to serve the needs of a wide
range of users or organizations.
• They are commercially packaged and sold in the market to multiple
customers (e.g., Microsoft Office, Adobe Photoshop).
• Development cost is high initially, but it is recovered through mass
sales, licensing, or subscriptions.
•   Support, updates, and new versions are released periodically to
maintain competitiveness.
2. Customized Software Solutions:
• Customized software is developed specifically for a single client or
organization according to unique business needs.
•   It is tailor-made, often involving client collaboration during the
development process.
• Maintenance and updates are client-specific, and reuse across other
clients is minimal.
********** 1 **********
--- page 2 ---
• Cost and development time are higher per project due to detailed
requirement analysis and integration efforts.
Aspect   Generic Software   Customized Software
Target Market   Mass market   Specific client
Volume sales &   One-time project
Revenue Type
licensing   payments
Development Cost
Through multiple users Through single client
Recovery
Revenue Potential   High (long-term)   Moderate (short-term)
CO-   b Why is the Spiral Model regarded as a meta-model in software development?   [5 M]
2,BL-L
Explanation:
1. Combination of Multiple Models:
Each phase (or “loop”) of the spiral can adopt a different process
model depending on project needs.
o For example, one iteration may follow a Waterfall approach
for documentation, while another may use Prototyping for user
interface design.
2. Risk-Driven Framework:
The Spiral Model’s main focus is risk analysis and risk reduction at
every iteration, which guides the selection of an appropriate process
for the next phase.
This adaptability allows it to encompass and manage other models
under its structure.
3. Iterative and Evolutionary Nature:
Like the Iterative model, the Spiral Model continuously refines
requirements and design through repeated cycles, each adding more
detail and functionality.
4. Meta-Model Concept:
Because the Spiral Model can include, control, or guide other models
within its framework, it acts as a “model of models”—that is, a meta-
model in software engineering.
CO-3;   c   Define UML and describe its purpose in object-oriented software   [5 M]
BL-L   development.
Definition of UML:
UML stands for Unified Modeling Language.
It is a standardized visual modeling language used to specify, visualize,
construct, and document the components of a software system, particularly
those developed using object-oriented (OO) principles.
********** 2 **********
--- page 3 ---
Purpose of UML in Object-Oriented Software Development:
1. Visual Representation of System Design:
UML provides diagrams (like class, use-case, sequence, and activity
diagrams) that help in visualizing the system’s architecture, behavior,
and interactions.
2. Enhances Communication:
It serves as a common language among developers, designers,
analysts, and stakeholders, improving understanding and reducing
ambiguity.
3. Supports OO Concepts:
UML directly represents object-oriented features such as classes,
inheritance, polymorphism, and associations.
4. Facilitates Analysis and Design:
It helps in analyzing system requirements and designing software
architecture before actual coding begins, leading to fewer design
flaws.
5. Provides Documentation and Maintainability:
UML diagrams act as comprehensive documentation, aiding future
maintenance, system upgrades, and team transitions.
CO-4;   d Compare and Contrast Unit Testing with Integration Testing.   [5 M]
BL-L   Aspect   Unit Testing   Integration Testing
Individual module
Focus   Interaction between modules
correctness
Coarser-grained (module
Granularity   Fine-grained (small units)
combinations)
Responsibility Developer   Tester/QA
Early in SDLC (after
Timing   After successful unit testing
coding)
Goal   Validate internal logic   Validate combined functionality
Q2   [20]
CO-1;   a Explain how Extreme Programming (XP) incorporates the concepts of pair   [10
BL-L   programming and continuous testing to improve software quality.   M]
Here’s a complete and structured answer to your question:
Answer:
Extreme Programming (XP) is an agile software development methodology
that emphasizes customer satisfaction, teamwork, and adaptability. Two of its
core practices—pair programming and continuous testing—play a key role in
improving software quality.
********** 3 **********
--- page 4 ---
1. Pair Programming:
•   Definition:
Pair programming means two programmers work together on the same
workstation.
One acts as the driver (writes the code), and the other acts as the
observer or navigator (reviews each line of code in real time).
• How it improves quality:
1. Real-time code review: Continuous peer checking detects logic
and syntax errors early.
2. Knowledge sharing: Enhances team understanding and avoids
dependency on a single developer.
3. Improved design decisions: Two minds working together
produce cleaner, well-structured code.
4. Better adherence to coding standards: Promotes consistent
style and structure across the project.
5. Reduced defects: Early detection leads to fewer bugs in later
stages of testing.
2. Continuous Testing:
•   Definition:
In XP, tests are written before or alongside the code (Test-Driven
Development, or TDD), and executed continuously throughout the
development process.
• How it improves quality:
1. Immediate feedback: Developers know instantly if new code
breaks existing functionality.
2. Regression prevention: Continuous test execution ensures
stability after every code change.
3. Higher confidence in changes: Automated tests allow frequent
integration and refactoring.
4. Customer satisfaction: Frequent testing ensures software
continuously meets customer requirements.
5. Documentation through tests: Test cases serve as living
documentation for expected behavior.
3. Combined Impact on Quality:
•   Pair programming ensures better design and fewer coding errors,
while continuous testing ensures ongoing verification of system
behavior.
•   Together, they create a feedback-rich, defect-prevention environment,
resulting in robust, maintainable, and high-quality software.
********** 4 **********
--- page 5 ---
✅ In summary:
Extreme Programming integrates pair programming (collaborative
development) and continuous testing (early and repeated validation) to ensure
that software is reliable, flexible, and aligned with customer needs at every
stage of development.
CO-3;   b Evaluate the role of UML modeling in reducing development risk and   [10
propose how it can be integrated with agile methodologies for iterative
BL-M   M]
design validation.
Here’s a complete, detailed answer to your question:
Answer:
1. Role of UML Modeling in Reducing Development Risk:
1. Early Visualization of the System:
UML provides graphical models—like use case, class, and sequence
diagrams—that help teams visualize system architecture before
coding.
→ This reduces the risk of misunderstanding requirements and design
flaws.
2. Improved Communication:
UML serves as a common visual language among developers,
designers, and stakeholders.
→ It ensures clarity in understanding functionality and interactions,
reducing risks of misinterpretation.
3. Validation and Traceability:
Each UML diagram corresponds to a specific phase of SDLC
(requirements, design, testing).
→ This ensures traceability of requirements and early validation,
lowering the risk of rework.
4. Early Error Detection:
Visual modeling highlights inconsistencies, missing functionality, and
design bottlenecks before implementation, saving cost and time.
5. Facilitates Risk Management:
UML supports scenario modeling and “what-if” analysis, helping
identify critical components and potential failure points.
2. Integration of UML with Agile Methodologies for Iterative Design Validation:
1. Lightweight Modeling Approach:
Use UML diagrams selectively (e.g., use-case and class diagrams) in
agile sprints to represent evolving requirements without over-
documentation.
2. Continuous Design Refinement:
Update UML models incrementally as part of each sprint review to
reflect new or modified features.
→ Ensures design always aligns with current implementation.
********** 5 **********
--- page 6 ---
3. Model-Based Collaboration:
Integrate UML into Agile tools (like Jira, Enterprise Architect, or
Visual Paradigm) for real-time collaboration and visibility.
4. Executable Models and Test Alignment:
Combine UML behavioral diagrams (e.g., sequence/activity) with
automated test cases to validate system behavior iteratively.
5. Feedback Loop with Stakeholders:
Use UML visualizations during sprint demos to collect stakeholder
feedback quickly and reduce misunderstanding risk.
✅ In Summary:
UML modeling reduces development risk by improving clarity,
communication, and early validation of requirements and design.
When integrated into agile workflows through lightweight, iterative updates
and stakeholder feedback, it becomes a powerful tool for continuous design
validation and risk mitigation throughout the project lifecycle.
Q3   [20]
CO2 ,BL- a   [10
Analyze how human factors influence the success of agile projects and
H   M]
design a strategy to strengthen collaboration and trust within an agile team.
Here’s a detailed and well-structured answer to your question:
Answer:
1. Influence of Human Factors on Agile Project Success:
Agile methodologies—like Scrum or XP—depend heavily on people and
interactions rather than processes or tools. Therefore, human factors such as
motivation, trust, communication, and leadership play a crucial role in
determining the success of agile projects.
a) Communication and Collaboration:
•   Effective, open communication ensures that requirements, progress,
and challenges are clearly shared within the team.
• Miscommunication leads to misunderstanding of user stories, poor
sprint outcomes, and reduced team efficiency.
b) Trust and Psychological Safety:
• Team members must feel safe to express opinions, admit mistakes,
and share new ideas.
• Lack of trust discourages feedback, innovation, and ownership of
work.
c) Motivation and Empowerment:
• Agile emphasizes self-organizing teams where members take
ownership of tasks.
• Motivation drives creativity and continuous improvement; low morale
leads to missed deadlines and poor product quality.
********** 6 **********
--- page 7 ---
d) Leadership and Support:
• Servant leadership in agile helps facilitate the team rather than control
it.
•   Effective leaders remove impediments, encourage participation, and
recognize individual contributions.
e) Cultural and Emotional Intelligence:
• Understanding cultural differences and emotional cues ensures better
team cohesion, especially in distributed teams.
• Emotional intelligence fosters empathy and smoother conflict
resolution.
2. Strategy to Strengthen Collaboration and Trust in Agile Teams:
A structured approach to enhancing teamwork, trust, and shared ownership
can significantly improve agile outcomes.
a) Establish Clear Communication Channels:
• Use daily stand-ups, retrospectives, and sprint reviews to maintain
transparency.
• Encourage face-to-face or video interactions to build personal
connection and clarity.
b) Foster Psychological Safety:
• Create an environment where mistakes are viewed as learning
opportunities.
• Encourage open dialogue and constructive criticism during
retrospectives.
c) Build Shared Ownership and Accountability:
• Define clear sprint goals and assign responsibilities collectively.
•   Celebrate collective success rather than individual achievements to
reinforce teamwork.
d) Encourage Pair Programming and Peer Reviews:
•   Collaborative coding improves code quality, enhances learning, and
increases trust between developers.
e) Continuous Feedback and Recognition:
• Provide timely feedback during sprint reviews.
• Recognize contributions publicly to boost morale and reinforce
positive behavior.
f) Invest in Team Building and Empathy Training:
********** 7 **********
--- page 8 ---
• Conduct workshops or informal activities to strengthen interpersonal
relationships.
• Train team members in emotional intelligence to improve cooperation
and conflict management.
✅ In Summary:
Human factors like trust, motivation, and communication directly influence
agile project success.
By promoting psychological safety, open communication, shared
accountability, and continuous feedback, organizations can cultivate an agile
culture built on collaboration, respect, and trust, ultimately leading to higher
productivity and team satisfaction.
CO-3;   b Design an activity diagram for booking an appointment at the   [10
dispensary, which includes the sequential steps of requesting an
BL-H   M]
appointment, checking availability, confirming a slot, generating a
token, and finally confirming the appointment, while also representing
the decision flow when a slot is unavailable and looping back to check
for another available slot before completion?
2 MARKS FOR EACH STEP
Q4   [20]
CO-2;   a   Illustrate how Sprint Planning and Daily Scrum meetings contribute to   [10
BL-M   incremental delivery and team synchronization.   M]
Here’s a clear and detailed explanation for your question:
Answer:
********** 8 **********
--- page 9 ---
In Agile Scrum, both Sprint Planning and Daily Scrum meetings are essential
ceremonies that ensure incremental delivery of the product and maintain team
synchronization throughout the development cycle.
1. Sprint Planning – Foundation for Incremental Delivery
Definition:
Sprint Planning is a meeting held at the beginning of each sprint to define
what work will be done and how it will be accomplished during that sprint.
Contribution to Incremental Delivery:
1. Defines Clear Sprint Goals:
The team collaborates with the Product Owner to set achievable sprint
objectives that represent a potentially shippable product increment.
2. Prioritization of Work:
User stories are selected from the Product Backlog based on business
value and team capacity, ensuring that high-value features are
delivered first.
3. Task Breakdown:
Each selected story is decomposed into smaller, manageable tasks.
This structure enables the team to complete and deliver working
software iteratively.
4. Commitment and Estimation:
The team estimates effort and commits to deliver a small, functional
increment within the sprint timebox (usually 2–4 weeks).
5. Transparency and Predictability:
The planning process aligns the entire team around what will be
delivered, enhancing visibility and accountability.
2. Daily Scrum – Engine for Team Synchronization
Definition:
The Daily Scrum (Stand-up) is a short, time-boxed (15-minute) meeting held
every day of the sprint where each team member discusses progress, plans,
and blockers.
Contribution to Team Synchronization:
1. Continuous Alignment:
Keeps all members informed about who is doing what, ensuring
coordinated progress toward the sprint goal.
2. Early Problem Detection:
Team members identify impediments or dependencies early so the
Scrum Master can resolve them promptly.
3. Adaptive Planning:
Daily updates allow the team to adjust priorities or reallocate tasks
based on current progress or new challenges.
********** 9 **********
--- page 10 ---
4. Accountability and Focus:
By sharing daily updates, members stay focused and accountable,
reducing duplication of work and improving productivity.
5. Enhanced Communication:
Promotes open collaboration and strengthens trust among team
members, particularly in cross-functional teams.
3. Combined Impact:
•   Sprint Planning sets the direction for incremental delivery.
• Daily Scrum maintains momentum and synchronization through
continuous feedback and alignment.
Together, they ensure that:
• Work remains on track.
• Increments are delivered regularly.
• The team remains cohesive, self-organized, and responsive to change.
✅ In Summary:
Sprint Planning defines the roadmap for each iteration, ensuring a focused
and achievable increment, while the Daily Scrum maintains alignment,
transparency, and adaptability among team members.
Together, they form the backbone of incremental delivery and continuous
team synchronization in Agile Scrum.
CO-3;   b Design the class diagram for Placement activity process. XYZ Institute of   [10
Technology conducts annual campus placements for final-year students across
BL-L   M]
Engineering and Management disciplines. The Placement Cell, in coordination
with faculty and student representatives, manages end-to-end activities from
company outreach to offer letter distribution.
Q5   [20]
CO-3;   a Design a labeled state transition model for following problem statement.   [10
“A food delivery company is developing an Online Food Delivery System to
BL-M   M]
manage the complete life cycle of a Food Order object. Each Food Order
********** 10 **********
--- page 11 ---
represents a customer’s request to purchase items from a restaurant. The
order passes through a sequence of states from creation until completion or
cancellation. When a customer requests an order, a new Food Order is
created. Once payment is made successfully, the order Confirmed. If the
payment fails, the order moves to the “Payment Failed” state, from which it
can either be retried or cancelled permanently. After confirmation, the order
is sent to the Restaurant, to Being Prepared. When preparation is completed,
the order moves to “Ready for Pickup.” At this stage, a Delivery Person is
assigned, and the order transitions to the “Out for Delivery”. If the delivery is
successful, the order marked as “Delivered”. However, if the customer rejects
the order or the delivery fails, it marks as “Returned” or “Cancelled”
respectively.
: 5 marks for state and 5 marks for labelled transition.
CO-2;   b Compare the effectiveness of continuing maintenance, re-engineering, and   [10
replacement strategies for legacy systems in terms of business risk, cost, and
BL-H   M]
long-term sustainability.
Here’s a comprehensive and structured answer to your question:
Answer:
Legacy systems are older software systems that remain in use because they
perform critical business functions. Organizations often face a strategic
decision between continuing maintenance, re-engineering, or replacing these
systems. Each strategy differs in its impact on business risk, cost, and long-
term sustainability.
1. Continuing Maintenance
********** 11 **********
--- page 12 ---
Definition:
Continuing maintenance means keeping the legacy system operational with
minimal updates or bug fixes, without major architectural changes.
Evaluation:
Aspect   Analysis
Moderate to High — Risk of system failure increases
Business Risk   over time due to obsolete technology and lack of vendor
support.
Low short-term cost (since changes are minimal), but
Cost   high long-term maintenance costs as patching becomes
complex.
Poor — Difficult to adapt to new technologies, security
Long-term
risks increase, and skilled manpower for old platforms
Sustainability
becomes scarce.
Conclusion:
Suitable when the system is stable, low-change, and still meets essential
business needs with minimal enhancement requirements.
2. Re-engineering
Definition:
Re-engineering involves analyzing, restructuring, and optimizing the existing
legacy system to improve maintainability, performance, and compatibility
without complete replacement.
Evaluation:
Aspect   Analysis
Medium — Controlled risk since business logic is
Business Risk   preserved; risk occurs mainly during migration or code
transformation.
Moderate — Requires investment in analysis, redesign,
Cost   and partial redevelopment. Cost is balanced by improved
efficiency.
Long-term   Good — Extends system life, reduces technical debt, and
Sustainability   allows integration with modern platforms.
Conclusion:
Effective when the legacy system has high business value but suffers from
technical inefficiencies or outdated architecture.
3. Replacement
********** 12 **********
--- page 13 ---
Definition:
Replacement involves developing or acquiring a completely new system to
substitute the legacy system and migrate essential data and processes.
Evaluation:
Aspect   Analysis
High — Risk of data loss, user resistance, and functional
Business Risk
gaps during transition to the new system.
Very High — Involves full system development,
Cost
training, data migration, and infrastructure setup.
Excellent — New technologies provide better scalability,
Long-term
integration, and security; supports future business
Sustainability
growth.
Conclusion:
Ideal when the legacy system’s maintenance cost exceeds its value or when
modernization is crucial for business competitiveness.
4. Comparative Summary
Business   Long-Term
Strategy   Cost   Suitability
Risk   Sustainability
Low
Continuing   Short-term
High   initially,   Poor
Maintenance   survival
high later
Balanced
Re-engineering Medium Moderate   Good
approach
Long-term
Replacement   High   Very High   Excellent
transformation
✅ In Summary:
• Continuing maintenance offers short-term cost savings but
grows risky and unsustainable.
• Re-engineering balances cost and risk, extending system life
while improving maintainability.
• Replacement demands high upfront investment but ensures
long-term sustainability and alignment with modern business
needs.
Hence, re-engineering is often the most practical and cost-effective strategy
for organizations that want modernization without the extreme risk or cost of
full system replacement.
Q6   [20]
********** 13 **********
--- page 14 ---
CO-2;   a Explain how a Level-0, Level-1, and Level-2 Data Flow Diagram (DFD) can   [10
be applied in the design of a Student Enrollment System. How do successive
BL-M   M]
levels increase the detail and functional decomposition of the process?
Level   Description   Detail Provided
Shows the system as a single
Level-0
process interacting with external Very high-level overview
(Context)
entities.
Breaks the system into core sub- Shows major functions and
Level-1
processes and data stores.   data relationships
Expands each sub-process into   Provides implementation-
Level-2
smaller, logical steps.   ready detail for design
CO-4;   b Evaluate how Efficiency, Maintainability, and Portability interrelate to   [10
determine overall software quality, and design a metric-based
BL-L   M]
evaluation framework to measure their combined impact
Efficiency, maintainability, and portability are interdependent attributes that
collectively determine software quality.
High efficiency ensures optimal performance, while maintainability allows
easy updates without degrading that performance.
Portability enhances system adaptability across platforms, influencing both
maintenance effort and efficiency.
Balancing these factors ensures sustainable performance and lower lifecycle
cost.
A metric-based framework can include CPU utilization, mean time to modify
(MTTM), and successful build rate across platforms to quantify overall
quality.
Q7   [20]
CO-3;   a Evaluate how adherence to Golden Rules and Interface Design Principles   [10
BL-H   (e.g., consistency, anticipation, focus) enhances usability and user   M]
satisfaction in modern web or mobile interfaces
Adherence to Golden Rules and Interface Design Principles ensures a
seamless, intuitive, and satisfying user experience.
Consistency in layout, icons, and navigation reduces cognitive load and helps
users predict behavior easily.
Anticipation enables systems to foresee user needs—like auto-suggestions or
shortcuts—reducing effort and frustration.
Focus and feedback guide user attention and confirm actions, improving
confidence and task completion speed.
Together, these principles enhance usability, minimize errors, and
significantly boost user satisfaction in modern interfaces.
********** 14 **********
--- page 15 ---
CO-4;   b Critically analyze how verification and validation complement each other in   [10
ensuring software reliability and propose an improved framework combining
BL-H   M]
both stages effectively
Verification and validation are complementary processes that together ensure
software reliability and quality assurance.
Verification checks whether the product is built correctly—through reviews,
inspections, and testing against specifications.
Validation ensures the right product is built—confirming it meets user needs
and real-world requirements.
Their integration minimizes defects, ensuring correctness and fitness for
purpose.
An improved framework combines early verification (static analysis, peer
reviews) with continuous validation (user testing, feedback loops) across all
SDLC phases, ensuring reliable, user-centered software delivery.
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 7295bc5fdb66

- Departments: Computer Engineering
- Programmes: BTech Computer 7002
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_Computer_7002/Software Engineering/ANS_Software Engineering(702IT0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Software Engineering
Date: 02 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 Questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   [20]
CO-1;   a Differentiate between generic software products and customized software   [5 M]
BL-L   solutions. Which type is likely to yield higher revenue for a company, and
what factors contribute to this difference?
1. Generic Software Products:
• Generic software products are developed to serve the needs of a wide
range of users or organizations.
• They are commercially packaged and sold in the market to multiple
customers (e.g., Microsoft Office, Adobe Photoshop).
• Development cost is high initially, but it is recovered through mass
sales, licensing, or subscriptions.
•   Support, updates, and new versions are released periodically to
maintain competitiveness.
2. Customized Software Solutions:
• Customized software is developed specifically for a single client or
organization according to unique business needs.
•   It is tailor-made, often involving client collaboration during the
development process.
• Maintenance and updates are client-specific, and reuse across other
clients is minimal.
********** 1 **********
--- page 2 ---
• Cost and development time are higher per project due to detailed
requirement analysis and integration efforts.
Aspect   Generic Software   Customized Software
Target Market   Mass market   Specific client
Volume sales &   One-time project
Revenue Type
licensing   payments
Development Cost
Through multiple users Through single client
Recovery
Revenue Potential   High (long-term)   Moderate (short-term)
CO-   b Why is the Spiral Model regarded as a meta-model in software development?   [5 M]
2,BL-L
Explanation:
1. Combination of Multiple Models:
Each phase (or “loop”) of the spiral can adopt a different process
model depending on project needs.
o For example, one iteration may follow a Waterfall approach
for documentation, while another may use Prototyping for user
interface design.
2. Risk-Driven Framework:
The Spiral Model’s main focus is risk analysis and risk reduction at
every iteration, which guides the selection of an appropriate process
for the next phase.
This adaptability allows it to encompass and manage other models
under its structure.
3. Iterative and Evolutionary Nature:
Like the Iterative model, the Spiral Model continuously refines
requirements and design through repeated cycles, each adding more
detail and functionality.
4. Meta-Model Concept:
Because the Spiral Model can include, control, or guide other models
within its framework, it acts as a “model of models”—that is, a meta-
model in software engineering.
CO-3;   c   Define UML and describe its purpose in object-oriented software   [5 M]
BL-L   development.
Definition of UML:
UML stands for Unified Modeling Language.
It is a standardized visual modeling language used to specify, visualize,
construct, and document the components of a software system, particularly
those developed using object-oriented (OO) principles.
********** 2 **********
--- page 3 ---
Purpose of UML in Object-Oriented Software Development:
1. Visual Representation of System Design:
UML provides diagrams (like class, use-case, sequence, and activity
diagrams) that help in visualizing the system’s architecture, behavior,
and interactions.
2. Enhances Communication:
It serves as a common language among developers, designers,
analysts, and stakeholders, improving understanding and reducing
ambiguity.
3. Supports OO Concepts:
UML directly represents object-oriented features such as classes,
inheritance, polymorphism, and associations.
4. Facilitates Analysis and Design:
It helps in analyzing system requirements and designing software
architecture before actual coding begins, leading to fewer design
flaws.
5. Provides Documentation and Maintainability:
UML diagrams act as comprehensive documentation, aiding future
maintenance, system upgrades, and team transitions.
CO-4;   d Compare and Contrast Unit Testing with Integration Testing.   [5 M]
BL-L   Aspect   Unit Testing   Integration Testing
Individual module
Focus   Interaction between modules
correctness
Coarser-grained (module
Granularity   Fine-grained (small units)
combinations)
Responsibility Developer   Tester/QA
Early in SDLC (after
Timing   After successful unit testing
coding)
Goal   Validate internal logic   Validate combined functionality
Q2   [20]
CO-1;   a Explain how Extreme Programming (XP) incorporates the concepts of pair   [10
BL-L   programming and continuous testing to improve software quality.   M]
Here’s a complete and structured answer to your question:
Answer:
Extreme Programming (XP) is an agile software development methodology
that emphasizes customer satisfaction, teamwork, and adaptability. Two of its
core practices—pair programming and continuous testing—play a key role in
improving software quality.
********** 3 **********
--- page 4 ---
1. Pair Programming:
•   Definition:
Pair programming means two programmers work together on the same
workstation.
One acts as the driver (writes the code), and the other acts as the
observer or navigator (reviews each line of code in real time).
• How it improves quality:
1. Real-time code review: Continuous peer checking detects logic
and syntax errors early.
2. Knowledge sharing: Enhances team understanding and avoids
dependency on a single developer.
3. Improved design decisions: Two minds working together
produce cleaner, well-structured code.
4. Better adherence to coding standards: Promotes consistent
style and structure across the project.
5. Reduced defects: Early detection leads to fewer bugs in later
stages of testing.
2. Continuous Testing:
•   Definition:
In XP, tests are written before or alongside the code (Test-Driven
Development, or TDD), and executed continuously throughout the
development process.
• How it improves quality:
1. Immediate feedback: Developers know instantly if new code
breaks existing functionality.
2. Regression prevention: Continuous test execution ensures
stability after every code change.
3. Higher confidence in changes: Automated tests allow frequent
integration and refactoring.
4. Customer satisfaction: Frequent testing ensures software
continuously meets customer requirements.
5. Documentation through tests: Test cases serve as living
documentation for expected behavior.
3. Combined Impact on Quality:
•   Pair programming ensures better design and fewer coding errors,
while continuous testing ensures ongoing verification of system
behavior.
•   Together, they create a feedback-rich, defect-prevention environment,
resulting in robust, maintainable, and high-quality software.
********** 4 **********
--- page 5 ---
✅ In summary:
Extreme Programming integrates pair programming (collaborative
development) and continuous testing (early and repeated validation) to ensure
that software is reliable, flexible, and aligned with customer needs at every
stage of development.
CO-3;   b Evaluate the role of UML modeling in reducing development risk and   [10
propose how it can be integrated with agile methodologies for iterative
BL-M   M]
design validation.
Here’s a complete, detailed answer to your question:
Answer:
1. Role of UML Modeling in Reducing Development Risk:
1. Early Visualization of the System:
UML provides graphical models—like use case, class, and sequence
diagrams—that help teams visualize system architecture before
coding.
→ This reduces the risk of misunderstanding requirements and design
flaws.
2. Improved Communication:
UML serves as a common visual language among developers,
designers, and stakeholders.
→ It ensures clarity in understanding functionality and interactions,
reducing risks of misinterpretation.
3. Validation and Traceability:
Each UML diagram corresponds to a specific phase of SDLC
(requirements, design, testing).
→ This ensures traceability of requirements and early validation,
lowering the risk of rework.
4. Early Error Detection:
Visual modeling highlights inconsistencies, missing functionality, and
design bottlenecks before implementation, saving cost and time.
5. Facilitates Risk Management:
UML supports scenario modeling and “what-if” analysis, helping
identify critical components and potential failure points.
2. Integration of UML with Agile Methodologies for Iterative Design Validation:
1. Lightweight Modeling Approach:
Use UML diagrams selectively (e.g., use-case and class diagrams) in
agile sprints to represent evolving requirements without over-
documentation.
2. Continuous Design Refinement:
Update UML models incrementally as part of each sprint review to
reflect new or modified features.
→ Ensures design always aligns with current implementation.
********** 5 **********
--- page 6 ---
3. Model-Based Collaboration:
Integrate UML into Agile tools (like Jira, Enterprise Architect, or
Visual Paradigm) for real-time collaboration and visibility.
4. Executable Models and Test Alignment:
Combine UML behavioral diagrams (e.g., sequence/activity) with
automated test cases to validate system behavior iteratively.
5. Feedback Loop with Stakeholders:
Use UML visualizations during sprint demos to collect stakeholder
feedback quickly and reduce misunderstanding risk.
✅ In Summary:
UML modeling reduces development risk by improving clarity,
communication, and early validation of requirements and design.
When integrated into agile workflows through lightweight, iterative updates
and stakeholder feedback, it becomes a powerful tool for continuous design
validation and risk mitigation throughout the project lifecycle.
Q3   [20]
CO2 ,BL- a   [10
Analyze how human factors influence the success of agile projects and
H   M]
design a strategy to strengthen collaboration and trust within an agile team.
Here’s a detailed and well-structured answer to your question:
Answer:
1. Influence of Human Factors on Agile Project Success:
Agile methodologies—like Scrum or XP—depend heavily on people and
interactions rather than processes or tools. Therefore, human factors such as
motivation, trust, communication, and leadership play a crucial role in
determining the success of agile projects.
a) Communication and Collaboration:
•   Effective, open communication ensures that requirements, progress,
and challenges are clearly shared within the team.
• Miscommunication leads to misunderstanding of user stories, poor
sprint outcomes, and reduced team efficiency.
b) Trust and Psychological Safety:
• Team members must feel safe to express opinions, admit mistakes,
and share new ideas.
• Lack of trust discourages feedback, innovation, and ownership of
work.
c) Motivation and Empowerment:
• Agile emphasizes self-organizing teams where members take
ownership of tasks.
• Motivation drives creativity and continuous improvement; low morale
leads to missed deadlines and poor product quality.
********** 6 **********
--- page 7 ---
d) Leadership and Support:
• Servant leadership in agile helps facilitate the team rather than control
it.
•   Effective leaders remove impediments, encourage participation, and
recognize individual contributions.
e) Cultural and Emotional Intelligence:
• Understanding cultural differences and emotional cues ensures better
team cohesion, especially in distributed teams.
• Emotional intelligence fosters empathy and smoother conflict
resolution.
2. Strategy to Strengthen Collaboration and Trust in Agile Teams:
A structured approach to enhancing teamwork, trust, and shared ownership
can significantly improve agile outcomes.
a) Establish Clear Communication Channels:
• Use daily stand-ups, retrospectives, and sprint reviews to maintain
transparency.
• Encourage face-to-face or video interactions to build personal
connection and clarity.
b) Foster Psychological Safety:
• Create an environment where mistakes are viewed as learning
opportunities.
• Encourage open dialogue and constructive criticism during
retrospectives.
c) Build Shared Ownership and Accountability:
• Define clear sprint goals and assign responsibilities collectively.
•   Celebrate collective success rather than individual achievements to
reinforce teamwork.
d) Encourage Pair Programming and Peer Reviews:
•   Collaborative coding improves code quality, enhances learning, and
increases trust between developers.
e) Continuous Feedback and Recognition:
• Provide timely feedback during sprint reviews.
• Recognize contributions publicly to boost morale and reinforce
positive behavior.
f) Invest in Team Building and Empathy Training:
********** 7 **********
--- page 8 ---
• Conduct workshops or informal activities to strengthen interpersonal
relationships.
• Train team members in emotional intelligence to improve cooperation
and conflict management.
✅ In Summary:
Human factors like trust, motivation, and communication directly influence
agile project success.
By promoting psychological safety, open communication, shared
accountability, and continuous feedback, organizations can cultivate an agile
culture built on collaboration, respect, and trust, ultimately leading to higher
productivity and team satisfaction.
CO-3;   b Design an activity diagram for booking an appointment at the   [10
dispensary, which includes the sequential steps of requesting an
BL-H   M]
appointment, checking availability, confirming a slot, generating a
token, and finally confirming the appointment, while also representing
the decision flow when a slot is unavailable and looping back to check
for another available slot before completion?
2 MARKS FOR EACH STEP
Q4   [20]
CO-2;   a   Illustrate how Sprint Planning and Daily Scrum meetings contribute to   [10
BL-M   incremental delivery and team synchronization.   M]
Here’s a clear and detailed explanation for your question:
Answer:
********** 8 **********
--- page 9 ---
In Agile Scrum, both Sprint Planning and Daily Scrum meetings are essential
ceremonies that ensure incremental delivery of the product and maintain team
synchronization throughout the development cycle.
1. Sprint Planning – Foundation for Incremental Delivery
Definition:
Sprint Planning is a meeting held at the beginning of each sprint to define
what work will be done and how it will be accomplished during that sprint.
Contribution to Incremental Delivery:
1. Defines Clear Sprint Goals:
The team collaborates with the Product Owner to set achievable sprint
objectives that represent a potentially shippable product increment.
2. Prioritization of Work:
User stories are selected from the Product Backlog based on business
value and team capacity, ensuring that high-value features are
delivered first.
3. Task Breakdown:
Each selected story is decomposed into smaller, manageable tasks.
This structure enables the team to complete and deliver working
software iteratively.
4. Commitment and Estimation:
The team estimates effort and commits to deliver a small, functional
increment within the sprint timebox (usually 2–4 weeks).
5. Transparency and Predictability:
The planning process aligns the entire team around what will be
delivered, enhancing visibility and accountability.
2. Daily Scrum – Engine for Team Synchronization
Definition:
The Daily Scrum (Stand-up) is a short, time-boxed (15-minute) meeting held
every day of the sprint where each team member discusses progress, plans,
and blockers.
Contribution to Team Synchronization:
1. Continuous Alignment:
Keeps all members informed about who is doing what, ensuring
coordinated progress toward the sprint goal.
2. Early Problem Detection:
Team members identify impediments or dependencies early so the
Scrum Master can resolve them promptly.
3. Adaptive Planning:
Daily updates allow the team to adjust priorities or reallocate tasks
based on current progress or new challenges.
********** 9 **********
--- page 10 ---
4. Accountability and Focus:
By sharing daily updates, members stay focused and accountable,
reducing duplication of work and improving productivity.
5. Enhanced Communication:
Promotes open collaboration and strengthens trust among team
members, particularly in cross-functional teams.
3. Combined Impact:
•   Sprint Planning sets the direction for incremental delivery.
• Daily Scrum maintains momentum and synchronization through
continuous feedback and alignment.
Together, they ensure that:
• Work remains on track.
• Increments are delivered regularly.
• The team remains cohesive, self-organized, and responsive to change.
✅ In Summary:
Sprint Planning defines the roadmap for each iteration, ensuring a focused
and achievable increment, while the Daily Scrum maintains alignment,
transparency, and adaptability among team members.
Together, they form the backbone of incremental delivery and continuous
team synchronization in Agile Scrum.
CO-3;   b Design the class diagram for Placement activity process. XYZ Institute of   [10
Technology conducts annual campus placements for final-year students across
BL-L   M]
Engineering and Management disciplines. The Placement Cell, in coordination
with faculty and student representatives, manages end-to-end activities from
company outreach to offer letter distribution.
Q5   [20]
CO-3;   a Design a labeled state transition model for following problem statement.   [10
“A food delivery company is developing an Online Food Delivery System to
BL-M   M]
manage the complete life cycle of a Food Order object. Each Food Order
********** 10 **********
--- page 11 ---
represents a customer’s request to purchase items from a restaurant. The
order passes through a sequence of states from creation until completion or
cancellation. When a customer requests an order, a new Food Order is
created. Once payment is made successfully, the order Confirmed. If the
payment fails, the order moves to the “Payment Failed” state, from which it
can either be retried or cancelled permanently. After confirmation, the order
is sent to the Restaurant, to Being Prepared. When preparation is completed,
the order moves to “Ready for Pickup.” At this stage, a Delivery Person is
assigned, and the order transitions to the “Out for Delivery”. If the delivery is
successful, the order marked as “Delivered”. However, if the customer rejects
the order or the delivery fails, it marks as “Returned” or “Cancelled”
respectively.
: 5 marks for state and 5 marks for labelled transition.
CO-2;   b Compare the effectiveness of continuing maintenance, re-engineering, and   [10
replacement strategies for legacy systems in terms of business risk, cost, and
BL-H   M]
long-term sustainability.
Here’s a comprehensive and structured answer to your question:
Answer:
Legacy systems are older software systems that remain in use because they
perform critical business functions. Organizations often face a strategic
decision between continuing maintenance, re-engineering, or replacing these
systems. Each strategy differs in its impact on business risk, cost, and long-
term sustainability.
1. Continuing Maintenance
********** 11 **********
--- page 12 ---
Definition:
Continuing maintenance means keeping the legacy system operational with
minimal updates or bug fixes, without major architectural changes.
Evaluation:
Aspect   Analysis
Moderate to High — Risk of system failure increases
Business Risk   over time due to obsolete technology and lack of vendor
support.
Low short-term cost (since changes are minimal), but
Cost   high long-term maintenance costs as patching becomes
complex.
Poor — Difficult to adapt to new technologies, security
Long-term
risks increase, and skilled manpower for old platforms
Sustainability
becomes scarce.
Conclusion:
Suitable when the system is stable, low-change, and still meets essential
business needs with minimal enhancement requirements.
2. Re-engineering
Definition:
Re-engineering involves analyzing, restructuring, and optimizing the existing
legacy system to improve maintainability, performance, and compatibility
without complete replacement.
Evaluation:
Aspect   Analysis
Medium — Controlled risk since business logic is
Business Risk   preserved; risk occurs mainly during migration or code
transformation.
Moderate — Requires investment in analysis, redesign,
Cost   and partial redevelopment. Cost is balanced by improved
efficiency.
Long-term   Good — Extends system life, reduces technical debt, and
Sustainability   allows integration with modern platforms.
Conclusion:
Effective when the legacy system has high business value but suffers from
technical inefficiencies or outdated architecture.
3. Replacement
********** 12 **********
--- page 13 ---
Definition:
Replacement involves developing or acquiring a completely new system to
substitute the legacy system and migrate essential data and processes.
Evaluation:
Aspect   Analysis
High — Risk of data loss, user resistance, and functional
Business Risk
gaps during transition to the new system.
Very High — Involves full system development,
Cost
training, data migration, and infrastructure setup.
Excellent — New technologies provide better scalability,
Long-term
integration, and security; supports future business
Sustainability
growth.
Conclusion:
Ideal when the legacy system’s maintenance cost exceeds its value or when
modernization is crucial for business competitiveness.
4. Comparative Summary
Business   Long-Term
Strategy   Cost   Suitability
Risk   Sustainability
Low
Continuing   Short-term
High   initially,   Poor
Maintenance   survival
high later
Balanced
Re-engineering Medium Moderate   Good
approach
Long-term
Replacement   High   Very High   Excellent
transformation
✅ In Summary:
• Continuing maintenance offers short-term cost savings but
grows risky and unsustainable.
• Re-engineering balances cost and risk, extending system life
while improving maintainability.
• Replacement demands high upfront investment but ensures
long-term sustainability and alignment with modern business
needs.
Hence, re-engineering is often the most practical and cost-effective strategy
for organizations that want modernization without the extreme risk or cost of
full system replacement.
Q6   [20]
********** 13 **********
--- page 14 ---
CO-2;   a Explain how a Level-0, Level-1, and Level-2 Data Flow Diagram (DFD) can   [10
be applied in the design of a Student Enrollment System. How do successive
BL-M   M]
levels increase the detail and functional decomposition of the process?
Level   Description   Detail Provided
Shows the system as a single
Level-0
process interacting with external Very high-level overview
(Context)
entities.
Breaks the system into core sub- Shows major functions and
Level-1
processes and data stores.   data relationships
Expands each sub-process into   Provides implementation-
Level-2
smaller, logical steps.   ready detail for design
CO-4;   b Evaluate how Efficiency, Maintainability, and Portability interrelate to   [10
determine overall software quality, and design a metric-based
BL-L   M]
evaluation framework to measure their combined impact
Efficiency, maintainability, and portability are interdependent attributes that
collectively determine software quality.
High efficiency ensures optimal performance, while maintainability allows
easy updates without degrading that performance.
Portability enhances system adaptability across platforms, influencing both
maintenance effort and efficiency.
Balancing these factors ensures sustainable performance and lower lifecycle
cost.
A metric-based framework can include CPU utilization, mean time to modify
(MTTM), and successful build rate across platforms to quantify overall
quality.
Q7   [20]
CO-3;   a Evaluate how adherence to Golden Rules and Interface Design Principles   [10
BL-H   (e.g., consistency, anticipation, focus) enhances usability and user   M]
satisfaction in modern web or mobile interfaces
Adherence to Golden Rules and Interface Design Principles ensures a
seamless, intuitive, and satisfying user experience.
Consistency in layout, icons, and navigation reduces cognitive load and helps
users predict behavior easily.
Anticipation enables systems to foresee user needs—like auto-suggestions or
shortcuts—reducing effort and frustration.
Focus and feedback guide user attention and confirm actions, improving
confidence and task completion speed.
Together, these principles enhance usability, minimize errors, and
significantly boost user satisfaction in modern interfaces.
********** 14 **********
--- page 15 ---
CO-4;   b Critically analyze how verification and validation complement each other in   [10
ensuring software reliability and propose an improved framework combining
BL-H   M]
both stages effectively
Verification and validation are complementary processes that together ensure
software reliability and quality assurance.
Verification checks whether the product is built correctly—through reviews,
inspections, and testing against specifications.
Validation ensures the right product is built—confirming it meets user needs
and real-world requirements.
Their integration minimizes defects, ensuring correctness and fitness for
purpose.
An improved framework combines early verification (static analysis, peer
reviews) with continuous validation (user testing, feedback loops) across all
SDLC phases, ensuring reliable, user-centered software delivery.
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper ddd93e8389c5

- Departments: Cyber Security, Information Technology
- Programmes: BTech CyberSecurity 7010, Integrated IT 7037
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_CyberSecurity_7010/Software Engineering/ANS_Software Engineering(702IT0C016)_2025-2026.pdf` (+1 identical copies)
- Text: text (18 pages)

````text
Q1
[20]
a Differentiate between generic software products and customized
software solutions. Which type is likely to yield higher revenue for a
company, and what factors contribute to this difference?
1. Generic Software Products: 2mark
• Generic software products are developed to serve the needs of a
wide range of users or organizations.
• They are commercially packaged and sold in the market to
multiple customers (e.g., Microsoft Office, Adobe Photoshop).
• Development cost is high initially, but it is recovered through
mass sales, licensing, or subscriptions.
•   Support, updates, and new versions are released periodically to
maintain competitiveness.
CO-   2. Customized Software Solutions: 2mark   [5
1;
M]
BL-L   • Customized software is developed specifically for a single
client or organization according to unique business needs.
•   It is tailor-made, often involving client collaboration during the
development process.
• Maintenance and updates are client-specific, and reuse across
other clients is minimal.
• Cost and development time are higher per project due to detailed
requirement analysis and integration efforts.
1 mark
Aspect   Generic Software Customized Software
Target Market   Mass market   Specific client
Volume sales &   One-time project
Revenue Type
licensing   payments
Development Cost   Through multiple
Through single client
Recovery   users
Revenue Potential   High (long-term)   Moderate (short-term)
b Why is the Spiral Model regarded as a meta-model in software
development?
CO-   [5
2,BL
M]
-L
Explanation:
--- page 2 ---
1. Combination of Multiple Models: 2M
Each phase (or “loop”) of the spiral can adopt a different process
model depending on project needs.
o For example, one iteration may follow a Waterfall
approach for documentation, while another may use
Prototyping for user interface design.
2. Risk-Driven Framework: 1M
The Spiral Model’s main focus is risk analysis and risk
reduction at every iteration, which guides the selection of an
appropriate process for the next phase.
This adaptability allows it to encompass and manage other
models under its structure.
3. Iterative and Evolutionary Nature:1M
Like the Iterative model, the Spiral Model continuously refines
requirements and design through repeated cycles, each adding
more detail and functionality.
4. Meta-Model Concept:1M
Because the Spiral Model can include, control, or guide other
models within its framework, it acts as a “model of models”—
that is, a meta-model in software engineering.
c   Define UML and describe its purpose in object-oriented software
development.
Definition of UML:
UML stands for Unified Modeling Language.
It is a standardized visual modeling language used to specify,
visualize, construct, and document the components of a software
system, particularly those developed using object-oriented (OO)
principles.
CO-   [5
Purpose of UML in Object-Oriented Software Development:
3;
M]
BL-L
1. Visual Representation of System Design:
UML provides diagrams (like class, use-case, sequence, and
activity diagrams) that help in visualizing the system’s
architecture, behavior, and interactions.
2. Enhances Communication:
It serves as a common language among developers, designers,
analysts, and stakeholders, improving understanding and
reducing ambiguity.
3. Supports OO Concepts:
UML directly represents object-oriented features such as
classes, inheritance, polymorphism, and associations.
4. Facilitates Analysis and Design:
It helps in analyzing system requirements and designing
--- page 3 ---
software architecture before actual coding begins, leading to
fewer design flaws.
5. Provides Documentation and Maintainability:
UML diagrams act as comprehensive documentation, aiding
future maintenance, system upgrades, and team transitions.
ONE MARK EACH POINT
d Compare and Contrast Unit Testing with Integration Testing.-- 01 M-
EACH POINT
Aspect   Unit Testing   Integration Testing
Individual module
Focus   Interaction between modules
CO-   correctness   [5
4;   Fine-grained (small   Coarser-grained (module
Granularity   M]
BL-L   units)   combinations)
Responsibility Developer   Tester/QA
Early in SDLC (after
Timing   After successful unit testing
coding)
Validate combined
Goal   Validate internal logic
functionality
[20
Q2
]
a Explain how Extreme Programming (XP) incorporates the concepts of
pair programming and continuous testing to improve software quality.
Answer:
Extreme Programming (XP) is an agile software development
methodology that emphasizes customer satisfaction, teamwork, and
adaptability. Two of its core practices—pair programming and
CO-   continuous testing—play a key role in improving software quality.
[10
1;
M]
BL-L
1. Pair Programming: 3M
•   Definition:
Pair programming means two programmers work together on
the same workstation.
One acts as the driver (writes the code), and the other acts as the
observer or navigator (reviews each line of code in real time).
• How it improves quality:
1. Real-time code review: Continuous peer checking
detects logic and syntax errors early.
--- page 4 ---
2. Knowledge sharing: Enhances team understanding and
avoids dependency on a single developer.
3. Improved design decisions: Two minds working
together produce cleaner, well-structured code.
4. Better adherence to coding standards: Promotes
consistent style and structure across the project.
5. Reduced defects: Early detection leads to fewer bugs in
later stages of testing.
2. Continuous Testing: 3M
•   Definition:
In XP, tests are written before or alongside the code (Test-
Driven Development, or TDD), and executed continuously
throughout the development process.
• How it improves quality:
1. Immediate feedback: Developers know instantly if new
code breaks existing functionality.
2. Regression prevention: Continuous test execution
ensures stability after every code change.
3. Higher confidence in changes: Automated tests allow
frequent integration and refactoring.
4. Customer satisfaction: Frequent testing ensures
software continuously meets customer requirements.
5. Documentation through tests: Test cases serve as
living documentation for expected behavior.
3. Combined Impact on Quality:3M
•   Pair programming ensures better design and fewer coding
errors, while continuous testing ensures ongoing verification of
system behavior.
•   Together, they create a feedback-rich, defect-prevention
environment, resulting in robust, maintainable, and high-
quality software.
Extreme Programming integrates pair programming (collaborative
development) and continuous testing (early and repeated validation) to
ensure that software is reliable, flexible, and aligned with customer
needs at every stage of development.—01M
--- page 5 ---
b Evaluate the role of UML modeling in reducing development risk and
propose how it can be integrated with agile methodologies for iterative
design validation.
Answer:
1. Role of UML Modeling in Reducing Development Risk: 5M
1. Early Visualization of the System:
UML provides graphical models—like use case, class, and
sequence diagrams—that help teams visualize system
architecture before coding.
→ This reduces the risk of misunderstanding requirements
and design flaws.
2. Improved Communication:
UML serves as a common visual language among developers,
designers, and stakeholders.
→ It ensures clarity in understanding functionality and
CO-   interactions, reducing risks of misinterpretation.
3;   3. Validation and Traceability:   [10
Each UML diagram corresponds to a specific phase of SDLC
BL-   (requirements, design, testing).   M]
M   → This ensures traceability of requirements and early
validation, lowering the risk of rework.
4. Early Error Detection:
Visual modeling highlights inconsistencies, missing
functionality, and design bottlenecks before implementation,
saving cost and time.
5. Facilitates Risk Management:
UML supports scenario modeling and “what-if” analysis,
helping identify critical components and potential failure
points.
2. Integration of UML with Agile Methodologies for Iterative Design Validation:
5M
1. Lightweight Modeling Approach:
Use UML diagrams selectively (e.g., use-case and class
diagrams) in agile sprints to represent evolving requirements
without over-documentation.
2. Continuous Design Refinement:
Update UML models incrementally as part of each sprint
review to reflect new or modified features.
→ Ensures design always aligns with current implementation.
--- page 6 ---
3. Model-Based Collaboration:
Integrate UML into Agile tools (like Jira, Enterprise Architect,
or Visual Paradigm) for real-time collaboration and visibility.
4. Executable Models and Test Alignment:
Combine UML behavioral diagrams (e.g., sequence/activity)
with automated test cases to validate system behavior
iteratively.
5. Feedback Loop with Stakeholders:
Use UML visualizations during sprint demos to collect
stakeholder feedback quickly and reduce misunderstanding risk.
UML modelling reduces development risk by improving clarity,
communication, and early validation of requirements and design.
When integrated into agile workflows through lightweight, iterative
updates and stakeholder feedback, it becomes a powerful tool for
continuous design validation and risk mitigation throughout the
project lifecycle.
[20
Q3
]
a
Analyze how human factors influence the success of agile projects and
design a strategy to strengthen collaboration and trust within an agile
team.
Answer:
1. Influence of Human Factors on Agile Project Success: 5 marks
CO2
Agile methodologies—like Scrum or XP—depend heavily on people   [10
,BL-   and interactions rather than processes or tools. Therefore, human
M]
H   factors such as motivation, trust, communication, and leadership play a
crucial role in determining the success of agile projects.
a) Communication and Collaboration:
•   Effective, open communication ensures that requirements,
progress, and challenges are clearly shared within the team.
• Miscommunication leads to misunderstanding of user stories,
poor sprint outcomes, and reduced team efficiency.
--- page 7 ---
b) Trust and Psychological Safety:
• Team members must feel safe to express opinions, admit
mistakes, and share new ideas.
• Lack of trust discourages feedback, innovation, and ownership
of work.
c) Motivation and Empowerment:
•   Agile emphasizes self-organizing teams where members take
ownership of tasks.
•   Motivation drives creativity and continuous improvement; low
morale leads to missed deadlines and poor product quality.
d) Leadership and Support:
•   Servant leadership in agile helps facilitate the team rather than
control it.
•   Effective leaders remove impediments, encourage participation,
and recognize individual contributions.
e) Cultural and Emotional Intelligence:
• Understanding cultural differences and emotional cues ensures
better team cohesion, especially in distributed teams.
• Emotional intelligence fosters empathy and smoother conflict
resolution.
2. Strategy to Strengthen Collaboration and Trust in Agile Teams: 5 marks
A structured approach to enhancing teamwork, trust, and shared
ownership can significantly improve agile outcomes.
a) Establish Clear Communication Channels:
• Use daily stand-ups, retrospectives, and sprint reviews to
maintain transparency.
• Encourage face-to-face or video interactions to build personal
connection and clarity.
b) Foster Psychological Safety:
•   Create an environment where mistakes are viewed as learning
opportunities.
• Encourage open dialogue and constructive criticism during
retrospectives.
c) Build Shared Ownership and Accountability:
--- page 8 ---
• Define clear sprint goals and assign responsibilities collectively.
•   Celebrate collective success rather than individual achievements
to reinforce teamwork.
d) Encourage Pair Programming and Peer Reviews:
•   Collaborative coding improves code quality, enhances learning,
and increases trust between developers.
e) Continuous Feedback and Recognition:
•   Provide timely feedback during sprint reviews.
• Recognize contributions publicly to boost morale and reinforce
positive behavior.
f) Invest in Team Building and Empathy Training:
• Conduct workshops or informal activities to strengthen
interpersonal relationships.
•   Train team members in emotional intelligence to improve
cooperation and conflict management.
Human factors like trust, motivation, and communication directly
influence agile project success.
By promoting psychological safety, open communication, shared
accountability, and continuous feedback, organizations can cultivate
an agile culture built on collaboration, respect, and trust, ultimately
leading to higher productivity and team satisfaction.
b Design an activity diagram for booking an appointment at the
dispensary, which includes the sequential steps of requesting an
CO-
appointment, checking availability, confirming a slot, generating a   [10
3;   token, and finally confirming the appointment, while also representing
M]
BL-H   the decision flow when a slot is unavailable and looping back to check
for another available slot before completion?
--- page 9 ---
2 MARKS FOR EACH STEP
[20
Q4
]
a   Illustrate how Sprint Planning and Daily Scrum meetings contribute to
incremental delivery and team synchronization.
CO-
2;   [10
Answer: -
BL-   M]
In Agile Scrum, both Sprint Planning and Daily Scrum meetings are
M
essential ceremonies that ensure incremental delivery of the product
and maintain team synchronization throughout the development cycle.
--- page 10 ---
1. Sprint Planning – Foundation for Incremental Delivery-
03 marks
Definition:
Sprint Planning is a meeting held at the beginning of each sprint to
define what work will be done and how it will be accomplished
during that sprint.
Contribution to Incremental Delivery:
1. Defines Clear Sprint Goals:
The team collaborates with the Product Owner to set achievable
sprint objectives that represent a potentially shippable product
increment.
2. Prioritization of Work:
User stories are selected from the Product Backlog based on
business value and team capacity, ensuring that high-value
features are delivered first.
3. Task Breakdown:
Each selected story is decomposed into smaller, manageable
tasks. This structure enables the team to complete and deliver
working software iteratively.
4. Commitment and Estimation:
The team estimates effort and commits to deliver a small,
functional increment within the sprint timebox (usually 2–4
weeks).
5. Transparency and Predictability:
The planning process aligns the entire team around what will be
delivered, enhancing visibility and accountability.
2. Daily Scrum – Engine for Team Synchronization – 3
marks
Definition:
The Daily Scrum (Stand-up) is a short, time-boxed (15-minute)
meeting held every day of the sprint where each team member discusses
progress, plans, and blockers.
Contribution to Team Synchronization:
1. Continuous Alignment:
Keeps all members informed about who is doing what, ensuring
coordinated progress toward the sprint goal.
2. Early Problem Detection:
Team members identify impediments or dependencies early so
the Scrum Master can resolve them promptly.
--- page 11 ---
3. Adaptive Planning:
Daily updates allow the team to adjust priorities or reallocate
tasks based on current progress or new challenges.
4. Accountability and Focus:
By sharing daily updates, members stay focused and
accountable, reducing duplication of work and improving
productivity.
5. Enhanced Communication:
Promotes open collaboration and strengthens trust among team
members, particularly in cross-functional teams.
3. Combined Impact: - 3 marks
• Sprint Planning sets the direction for incremental delivery.
• Daily Scrum maintains momentum and synchronization
through continuous feedback and alignment.
Together, they ensure that:
• Work remains on track.
•   Increments are delivered regularly.
• The team remains cohesive, self-organized, and responsive to
change.
01 marks
Sprint Planning defines the roadmap for each iteration, ensuring a
focused and achievable increment, while the Daily Scrum maintains
alignment, transparency, and adaptability among team members.
Together, they form the backbone of incremental delivery and
continuous team synchronization in Agile Scrum.
b Design the class diagram for Placement activity process. XYZ Institute
CO-   of Technology conducts annual campus placements for final-year
students across Engineering and Management disciplines. The   [10
3;   Placement Cell, in coordination with faculty and student representatives,
BL-L   manages end-to-end activities from company outreach to offer letter   M]
distribution.
--- page 12 ---
[20
Q5
]
a Design a labeled state transition model for following problem statement.
“A food delivery company is developing an Online Food Delivery
System to manage the complete life cycle of a Food Order object. Each
Food Order represents a customer’s request to purchase items from a
restaurant. The order passes through a sequence of states from creation
until completion or cancellation. When a customer requests an order, a
new Food Order is created. Once payment is made successfully, the
CO-   order Confirmed. If the payment fails, the order moves to the “Payment
Failed” state, from which it can either be retried or cancelled
3;   [10
permanently. After confirmation, the order is sent to the Restaurant, to
BL-   Being Prepared. When preparation is completed, the order moves to   M]
“Ready for Pickup.” At this stage, a Delivery Person is assigned, and
M
the order transitions to the “Out for Delivery”. If the delivery is
successful, the order marked as “Delivered”. However, if the customer
rejects the order or the delivery fails, it marks as “Returned” or
“Cancelled” respectively.
: 5 marks for state and 5 marks for labelled transition.
--- page 13 ---
b Compare the effectiveness of continuing maintenance, re-engineering,
and replacement strategies for legacy systems in terms of business risk,
cost, and long-term sustainability.
2 marks each points
Answer:
Legacy systems are older software systems that remain in use because
they perform critical business functions. Organizations often face a
strategic decision between continuing maintenance, re-engineering,
or replacing these systems. Each strategy differs in its impact on
business risk, cost, and long-term sustainability.
CO-
[10
2;
1. Continuing Maintenance   M]
BL-H
Definition:
Continuing maintenance means keeping the legacy system operational
with minimal updates or bug fixes, without major architectural
changes.
Evaluation:
Aspect   Analysis
Moderate to High — Risk of system failure
Business Risk   increases over time due to obsolete technology and
lack of vendor support.
Low short-term cost (since changes are minimal),
Cost   but high long-term maintenance costs as patching
becomes complex.
--- page 14 ---
Poor — Difficult to adapt to new technologies,
Long-term
security risks increase, and skilled manpower for
Sustainability
old platforms becomes scarce.
Conclusion:
Suitable when the system is stable, low-change, and still meets
essential business needs with minimal enhancement requirements.
2. Re-engineering
Definition:
Re-engineering involves analyzing, restructuring, and optimizing the
existing legacy system to improve maintainability, performance, and
compatibility without complete replacement.
Evaluation:
Aspect   Analysis
Medium — Controlled risk since business logic is
Business Risk   preserved; risk occurs mainly during migration or
code transformation.
Moderate — Requires investment in analysis,
Cost   redesign, and partial redevelopment. Cost is
balanced by improved efficiency.
Long-term   Good — Extends system life, reduces technical
Sustainability   debt, and allows integration with modern platforms.
Conclusion:
Effective when the legacy system has high business value but suffers
from technical inefficiencies or outdated architecture.
3. Replacement
Definition:
Replacement involves developing or acquiring a completely new
system to substitute the legacy system and migrate essential data and
processes.
Evaluation:
Aspect   Analysis
High — Risk of data loss, user resistance, and
Business Risk
functional gaps during transition to the new system.
--- page 15 ---
Very High — Involves full system development,
Cost
training, data migration, and infrastructure setup.
Excellent — New technologies provide better
Long-term
scalability, integration, and security; supports
Sustainability
future business growth.
Conclusion:
Ideal when the legacy system’s maintenance cost exceeds its value or
when modernization is crucial for business competitiveness.
4. Comparative Summary
Business   Long-Term
Strategy   Cost   Suitability
Risk   Sustainability
Low
Continuing   Short-term
High   initially,   Poor
Maintenance   survival
high later
Re-   Balanced
Medium Moderate Good
engineering   approach
Long-term
Replacement High   Very High Excellent
transformation
• Continuing maintenance offers short-term cost savings
but grows risky and unsustainable.
• Re-engineering balances cost and risk, extending system
life while improving maintainability.
• Replacement demands high upfront investment but
ensures long-term sustainability and alignment with
modern business needs.
Hence, re-engineering is often the most practical and cost-effective
strategy for organizations that want modernization without the extreme
risk or cost of full system replacement.
[20
Q6
]
CO-   a Explain how a Level-0, Level-1, and Level-2 Data Flow Diagram
(DFD) can be applied in the design of a Student Enrollment System. ( 5
2;   marks)   [10
BL-   How do successive levels increase the detail and functional   M]
decomposition of the process? ( 5 marks)
M
--- page 16 ---
Level   Description   Detail Provided
Shows the system as a single
Level-0
process interacting with   Very high-level overview
(Context)
external entities.
Breaks the system into core   Shows major functions
Level-1
sub-processes and data stores. and data relationships
Expands each sub-process into Provides implementation-
Level-2
smaller, logical steps.   ready detail for design
b Evaluate how Efficiency, Maintainability, and Portability interrelate to
determine overall software quality, and design a metric-based
evaluation framework to measure their combined impact
- 2 marks each point
Efficiency, maintainability, and portability are interdependent attributes
that collectively determine software quality.
High efficiency ensures optimal performance, while maintainability
allows easy updates without degrading that performance.
Portability enhances system adaptability across platforms, influencing
both maintenance effort and efficiency.
CO-
[10
4;
Balancing these factors ensures sustainable performance and lower   M]
BL-L
lifecycle cost.
A metric-based framework can include CPU utilization, mean time to
modify (MTTM), and successful build rate across platforms to quantify
overall quality.
Interrelation:
Efficiency affects Maintainability: If code is efficient but hard to
maintain, it's like having a sports car that's a pain to repair ,Balance
is key.
Maintainability impacts Portability: If code is easy to maintain but
not portable, it's like having a phone that's easy to fix but only works
on one network.
Portability influences Efficiency: If code is portable but inefficient,
it's like having a universal charger that's super slow.
[20
Q7
]
--- page 17 ---
a Evaluate how adherence to Golden Rules and Interface Design
Principles (e.g., consistency, anticipation, focus) enhances usability and
user satisfaction in modern web or mobile interfaces
(5marks +5 marks)
Adherence to Golden Rules and Interface Design Principles ensures a
seamless, intuitive, and satisfying user experience.
Consistency in layout, icons, and navigation reduces cognitive load and
helps users predict behavior easily.
Anticipation enables systems to foresee user needs—like auto-
suggestions or shortcuts—reducing effort and frustration.
Focus and feedback guide user attention and confirm actions,
CO-   improving confidence and task completion speed.
Together, these principles enhance usability, minimize errors, and   [10
3;   significantly boost user satisfaction in modern interfaces.
M]
BL-H
In conclusion discuss,
1. Golden Rule: Place the User in Control
2. Golden Rule: Reduce the User’s Memory Load
3. Golden Rule: Make the Interface Consistent
4. Interface Design Principle: Anticipation
5. Interface Design Principle: Focus
b Critically analyze how verification and validation complement each
other in ensuring software reliability and propose an improved
framework combining both stages effectively
2 marks each point
Verification and validation are complementary processes that together
CO-   ensure software reliability and quality assurance.
[10
4;
M]
BL-H   Verification checks whether the product is built correctly—through
reviews, inspections, and testing against specifications.
Validation ensures the right product is built—confirming it meets user
needs and real-world requirements.
--- page 18 ---
Their integration minimizes defects, ensuring correctness and fitness for
purpose.
An improved framework combines early verification (static analysis,
peer reviews) with continuous validation (user testing, feedback
loops) across all SDLC phases, ensuring reliable, user-centered software
delivery.
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper aba0e68edf67

- Departments: Information Technology
- Programmes: BTech IT 7001
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/BTech_IT_7001/Software Engineering/ANS_Software Engineering(702IT0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Software Engineering
Date: 02 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 Questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   [20]
CO-1;   a Differentiate between generic software products and customized software   [5 M]
BL-L   solutions. Which type is likely to yield higher revenue for a company, and
what factors contribute to this difference?
1. Generic Software Products:
• Generic software products are developed to serve the needs of a wide
range of users or organizations.
• They are commercially packaged and sold in the market to multiple
customers (e.g., Microsoft Office, Adobe Photoshop).
• Development cost is high initially, but it is recovered through mass
sales, licensing, or subscriptions.
•   Support, updates, and new versions are released periodically to
maintain competitiveness.
2. Customized Software Solutions:
• Customized software is developed specifically for a single client or
organization according to unique business needs.
•   It is tailor-made, often involving client collaboration during the
development process.
• Maintenance and updates are client-specific, and reuse across other
clients is minimal.
********** 1 **********
--- page 2 ---
• Cost and development time are higher per project due to detailed
requirement analysis and integration efforts.
Aspect   Generic Software   Customized Software
Target Market   Mass market   Specific client
Volume sales &   One-time project
Revenue Type
licensing   payments
Development Cost
Through multiple users Through single client
Recovery
Revenue Potential   High (long-term)   Moderate (short-term)
CO-   b Why is the Spiral Model regarded as a meta-model in software development?   [5 M]
2,BL-L
Explanation:
1. Combination of Multiple Models:
Each phase (or “loop”) of the spiral can adopt a different process
model depending on project needs.
o For example, one iteration may follow a Waterfall approach
for documentation, while another may use Prototyping for user
interface design.
2. Risk-Driven Framework:
The Spiral Model’s main focus is risk analysis and risk reduction at
every iteration, which guides the selection of an appropriate process
for the next phase.
This adaptability allows it to encompass and manage other models
under its structure.
3. Iterative and Evolutionary Nature:
Like the Iterative model, the Spiral Model continuously refines
requirements and design through repeated cycles, each adding more
detail and functionality.
4. Meta-Model Concept:
Because the Spiral Model can include, control, or guide other models
within its framework, it acts as a “model of models”—that is, a meta-
model in software engineering.
CO-3;   c   Define UML and describe its purpose in object-oriented software   [5 M]
BL-L   development.
Definition of UML:
UML stands for Unified Modeling Language.
It is a standardized visual modeling language used to specify, visualize,
construct, and document the components of a software system, particularly
those developed using object-oriented (OO) principles.
********** 2 **********
--- page 3 ---
Purpose of UML in Object-Oriented Software Development:
1. Visual Representation of System Design:
UML provides diagrams (like class, use-case, sequence, and activity
diagrams) that help in visualizing the system’s architecture, behavior,
and interactions.
2. Enhances Communication:
It serves as a common language among developers, designers,
analysts, and stakeholders, improving understanding and reducing
ambiguity.
3. Supports OO Concepts:
UML directly represents object-oriented features such as classes,
inheritance, polymorphism, and associations.
4. Facilitates Analysis and Design:
It helps in analyzing system requirements and designing software
architecture before actual coding begins, leading to fewer design
flaws.
5. Provides Documentation and Maintainability:
UML diagrams act as comprehensive documentation, aiding future
maintenance, system upgrades, and team transitions.
CO-4;   d Compare and Contrast Unit Testing with Integration Testing.   [5 M]
BL-L   Aspect   Unit Testing   Integration Testing
Individual module
Focus   Interaction between modules
correctness
Coarser-grained (module
Granularity   Fine-grained (small units)
combinations)
Responsibility Developer   Tester/QA
Early in SDLC (after
Timing   After successful unit testing
coding)
Goal   Validate internal logic   Validate combined functionality
Q2   [20]
CO-1;   a Explain how Extreme Programming (XP) incorporates the concepts of pair   [10
BL-L   programming and continuous testing to improve software quality.   M]
Here’s a complete and structured answer to your question:
Answer:
Extreme Programming (XP) is an agile software development methodology
that emphasizes customer satisfaction, teamwork, and adaptability. Two of its
core practices—pair programming and continuous testing—play a key role in
improving software quality.
********** 3 **********
--- page 4 ---
1. Pair Programming:
•   Definition:
Pair programming means two programmers work together on the same
workstation.
One acts as the driver (writes the code), and the other acts as the
observer or navigator (reviews each line of code in real time).
• How it improves quality:
1. Real-time code review: Continuous peer checking detects logic
and syntax errors early.
2. Knowledge sharing: Enhances team understanding and avoids
dependency on a single developer.
3. Improved design decisions: Two minds working together
produce cleaner, well-structured code.
4. Better adherence to coding standards: Promotes consistent
style and structure across the project.
5. Reduced defects: Early detection leads to fewer bugs in later
stages of testing.
2. Continuous Testing:
•   Definition:
In XP, tests are written before or alongside the code (Test-Driven
Development, or TDD), and executed continuously throughout the
development process.
• How it improves quality:
1. Immediate feedback: Developers know instantly if new code
breaks existing functionality.
2. Regression prevention: Continuous test execution ensures
stability after every code change.
3. Higher confidence in changes: Automated tests allow frequent
integration and refactoring.
4. Customer satisfaction: Frequent testing ensures software
continuously meets customer requirements.
5. Documentation through tests: Test cases serve as living
documentation for expected behavior.
3. Combined Impact on Quality:
•   Pair programming ensures better design and fewer coding errors,
while continuous testing ensures ongoing verification of system
behavior.
•   Together, they create a feedback-rich, defect-prevention environment,
resulting in robust, maintainable, and high-quality software.
********** 4 **********
--- page 5 ---
✅ In summary:
Extreme Programming integrates pair programming (collaborative
development) and continuous testing (early and repeated validation) to ensure
that software is reliable, flexible, and aligned with customer needs at every
stage of development.
CO-3;   b Evaluate the role of UML modeling in reducing development risk and   [10
propose how it can be integrated with agile methodologies for iterative
BL-M   M]
design validation.
Here’s a complete, detailed answer to your question:
Answer:
1. Role of UML Modeling in Reducing Development Risk:
1. Early Visualization of the System:
UML provides graphical models—like use case, class, and sequence
diagrams—that help teams visualize system architecture before
coding.
→ This reduces the risk of misunderstanding requirements and design
flaws.
2. Improved Communication:
UML serves as a common visual language among developers,
designers, and stakeholders.
→ It ensures clarity in understanding functionality and interactions,
reducing risks of misinterpretation.
3. Validation and Traceability:
Each UML diagram corresponds to a specific phase of SDLC
(requirements, design, testing).
→ This ensures traceability of requirements and early validation,
lowering the risk of rework.
4. Early Error Detection:
Visual modeling highlights inconsistencies, missing functionality, and
design bottlenecks before implementation, saving cost and time.
5. Facilitates Risk Management:
UML supports scenario modeling and “what-if” analysis, helping
identify critical components and potential failure points.
2. Integration of UML with Agile Methodologies for Iterative Design Validation:
1. Lightweight Modeling Approach:
Use UML diagrams selectively (e.g., use-case and class diagrams) in
agile sprints to represent evolving requirements without over-
documentation.
2. Continuous Design Refinement:
Update UML models incrementally as part of each sprint review to
reflect new or modified features.
→ Ensures design always aligns with current implementation.
********** 5 **********
--- page 6 ---
3. Model-Based Collaboration:
Integrate UML into Agile tools (like Jira, Enterprise Architect, or
Visual Paradigm) for real-time collaboration and visibility.
4. Executable Models and Test Alignment:
Combine UML behavioral diagrams (e.g., sequence/activity) with
automated test cases to validate system behavior iteratively.
5. Feedback Loop with Stakeholders:
Use UML visualizations during sprint demos to collect stakeholder
feedback quickly and reduce misunderstanding risk.
✅ In Summary:
UML modeling reduces development risk by improving clarity,
communication, and early validation of requirements and design.
When integrated into agile workflows through lightweight, iterative updates
and stakeholder feedback, it becomes a powerful tool for continuous design
validation and risk mitigation throughout the project lifecycle.
Q3   [20]
CO2 ,BL- a   [10
Analyze how human factors influence the success of agile projects and
H   M]
design a strategy to strengthen collaboration and trust within an agile team.
Here’s a detailed and well-structured answer to your question:
Answer:
1. Influence of Human Factors on Agile Project Success:
Agile methodologies—like Scrum or XP—depend heavily on people and
interactions rather than processes or tools. Therefore, human factors such as
motivation, trust, communication, and leadership play a crucial role in
determining the success of agile projects.
a) Communication and Collaboration:
•   Effective, open communication ensures that requirements, progress,
and challenges are clearly shared within the team.
• Miscommunication leads to misunderstanding of user stories, poor
sprint outcomes, and reduced team efficiency.
b) Trust and Psychological Safety:
• Team members must feel safe to express opinions, admit mistakes,
and share new ideas.
• Lack of trust discourages feedback, innovation, and ownership of
work.
c) Motivation and Empowerment:
• Agile emphasizes self-organizing teams where members take
ownership of tasks.
• Motivation drives creativity and continuous improvement; low morale
leads to missed deadlines and poor product quality.
********** 6 **********
--- page 7 ---
d) Leadership and Support:
• Servant leadership in agile helps facilitate the team rather than control
it.
•   Effective leaders remove impediments, encourage participation, and
recognize individual contributions.
e) Cultural and Emotional Intelligence:
• Understanding cultural differences and emotional cues ensures better
team cohesion, especially in distributed teams.
• Emotional intelligence fosters empathy and smoother conflict
resolution.
2. Strategy to Strengthen Collaboration and Trust in Agile Teams:
A structured approach to enhancing teamwork, trust, and shared ownership
can significantly improve agile outcomes.
a) Establish Clear Communication Channels:
• Use daily stand-ups, retrospectives, and sprint reviews to maintain
transparency.
• Encourage face-to-face or video interactions to build personal
connection and clarity.
b) Foster Psychological Safety:
• Create an environment where mistakes are viewed as learning
opportunities.
• Encourage open dialogue and constructive criticism during
retrospectives.
c) Build Shared Ownership and Accountability:
• Define clear sprint goals and assign responsibilities collectively.
•   Celebrate collective success rather than individual achievements to
reinforce teamwork.
d) Encourage Pair Programming and Peer Reviews:
•   Collaborative coding improves code quality, enhances learning, and
increases trust between developers.
e) Continuous Feedback and Recognition:
• Provide timely feedback during sprint reviews.
• Recognize contributions publicly to boost morale and reinforce
positive behavior.
f) Invest in Team Building and Empathy Training:
********** 7 **********
--- page 8 ---
• Conduct workshops or informal activities to strengthen interpersonal
relationships.
• Train team members in emotional intelligence to improve cooperation
and conflict management.
✅ In Summary:
Human factors like trust, motivation, and communication directly influence
agile project success.
By promoting psychological safety, open communication, shared
accountability, and continuous feedback, organizations can cultivate an agile
culture built on collaboration, respect, and trust, ultimately leading to higher
productivity and team satisfaction.
CO-3;   b Design an activity diagram for booking an appointment at the   [10
dispensary, which includes the sequential steps of requesting an
BL-H   M]
appointment, checking availability, confirming a slot, generating a
token, and finally confirming the appointment, while also representing
the decision flow when a slot is unavailable and looping back to check
for another available slot before completion?
2 MARKS FOR EACH STEP
Q4   [20]
CO-2;   a   Illustrate how Sprint Planning and Daily Scrum meetings contribute to   [10
BL-M   incremental delivery and team synchronization.   M]
Here’s a clear and detailed explanation for your question:
Answer:
********** 8 **********
--- page 9 ---
In Agile Scrum, both Sprint Planning and Daily Scrum meetings are essential
ceremonies that ensure incremental delivery of the product and maintain team
synchronization throughout the development cycle.
1. Sprint Planning – Foundation for Incremental Delivery
Definition:
Sprint Planning is a meeting held at the beginning of each sprint to define
what work will be done and how it will be accomplished during that sprint.
Contribution to Incremental Delivery:
1. Defines Clear Sprint Goals:
The team collaborates with the Product Owner to set achievable sprint
objectives that represent a potentially shippable product increment.
2. Prioritization of Work:
User stories are selected from the Product Backlog based on business
value and team capacity, ensuring that high-value features are
delivered first.
3. Task Breakdown:
Each selected story is decomposed into smaller, manageable tasks.
This structure enables the team to complete and deliver working
software iteratively.
4. Commitment and Estimation:
The team estimates effort and commits to deliver a small, functional
increment within the sprint timebox (usually 2–4 weeks).
5. Transparency and Predictability:
The planning process aligns the entire team around what will be
delivered, enhancing visibility and accountability.
2. Daily Scrum – Engine for Team Synchronization
Definition:
The Daily Scrum (Stand-up) is a short, time-boxed (15-minute) meeting held
every day of the sprint where each team member discusses progress, plans,
and blockers.
Contribution to Team Synchronization:
1. Continuous Alignment:
Keeps all members informed about who is doing what, ensuring
coordinated progress toward the sprint goal.
2. Early Problem Detection:
Team members identify impediments or dependencies early so the
Scrum Master can resolve them promptly.
3. Adaptive Planning:
Daily updates allow the team to adjust priorities or reallocate tasks
based on current progress or new challenges.
********** 9 **********
--- page 10 ---
4. Accountability and Focus:
By sharing daily updates, members stay focused and accountable,
reducing duplication of work and improving productivity.
5. Enhanced Communication:
Promotes open collaboration and strengthens trust among team
members, particularly in cross-functional teams.
3. Combined Impact:
•   Sprint Planning sets the direction for incremental delivery.
• Daily Scrum maintains momentum and synchronization through
continuous feedback and alignment.
Together, they ensure that:
• Work remains on track.
• Increments are delivered regularly.
• The team remains cohesive, self-organized, and responsive to change.
✅ In Summary:
Sprint Planning defines the roadmap for each iteration, ensuring a focused
and achievable increment, while the Daily Scrum maintains alignment,
transparency, and adaptability among team members.
Together, they form the backbone of incremental delivery and continuous
team synchronization in Agile Scrum.
CO-3;   b Design the class diagram for Placement activity process. XYZ Institute of   [10
Technology conducts annual campus placements for final-year students across
BL-L   M]
Engineering and Management disciplines. The Placement Cell, in coordination
with faculty and student representatives, manages end-to-end activities from
company outreach to offer letter distribution.
Q5   [20]
CO-3;   a Design a labeled state transition model for following problem statement.   [10
“A food delivery company is developing an Online Food Delivery System to
BL-M   M]
manage the complete life cycle of a Food Order object. Each Food Order
********** 10 **********
--- page 11 ---
represents a customer’s request to purchase items from a restaurant. The
order passes through a sequence of states from creation until completion or
cancellation. When a customer requests an order, a new Food Order is
created. Once payment is made successfully, the order Confirmed. If the
payment fails, the order moves to the “Payment Failed” state, from which it
can either be retried or cancelled permanently. After confirmation, the order
is sent to the Restaurant, to Being Prepared. When preparation is completed,
the order moves to “Ready for Pickup.” At this stage, a Delivery Person is
assigned, and the order transitions to the “Out for Delivery”. If the delivery is
successful, the order marked as “Delivered”. However, if the customer rejects
the order or the delivery fails, it marks as “Returned” or “Cancelled”
respectively.
: 5 marks for state and 5 marks for labelled transition.
CO-2;   b Compare the effectiveness of continuing maintenance, re-engineering, and   [10
replacement strategies for legacy systems in terms of business risk, cost, and
BL-H   M]
long-term sustainability.
Here’s a comprehensive and structured answer to your question:
Answer:
Legacy systems are older software systems that remain in use because they
perform critical business functions. Organizations often face a strategic
decision between continuing maintenance, re-engineering, or replacing these
systems. Each strategy differs in its impact on business risk, cost, and long-
term sustainability.
1. Continuing Maintenance
********** 11 **********
--- page 12 ---
Definition:
Continuing maintenance means keeping the legacy system operational with
minimal updates or bug fixes, without major architectural changes.
Evaluation:
Aspect   Analysis
Moderate to High — Risk of system failure increases
Business Risk   over time due to obsolete technology and lack of vendor
support.
Low short-term cost (since changes are minimal), but
Cost   high long-term maintenance costs as patching becomes
complex.
Poor — Difficult to adapt to new technologies, security
Long-term
risks increase, and skilled manpower for old platforms
Sustainability
becomes scarce.
Conclusion:
Suitable when the system is stable, low-change, and still meets essential
business needs with minimal enhancement requirements.
2. Re-engineering
Definition:
Re-engineering involves analyzing, restructuring, and optimizing the existing
legacy system to improve maintainability, performance, and compatibility
without complete replacement.
Evaluation:
Aspect   Analysis
Medium — Controlled risk since business logic is
Business Risk   preserved; risk occurs mainly during migration or code
transformation.
Moderate — Requires investment in analysis, redesign,
Cost   and partial redevelopment. Cost is balanced by improved
efficiency.
Long-term   Good — Extends system life, reduces technical debt, and
Sustainability   allows integration with modern platforms.
Conclusion:
Effective when the legacy system has high business value but suffers from
technical inefficiencies or outdated architecture.
3. Replacement
********** 12 **********
--- page 13 ---
Definition:
Replacement involves developing or acquiring a completely new system to
substitute the legacy system and migrate essential data and processes.
Evaluation:
Aspect   Analysis
High — Risk of data loss, user resistance, and functional
Business Risk
gaps during transition to the new system.
Very High — Involves full system development,
Cost
training, data migration, and infrastructure setup.
Excellent — New technologies provide better scalability,
Long-term
integration, and security; supports future business
Sustainability
growth.
Conclusion:
Ideal when the legacy system’s maintenance cost exceeds its value or when
modernization is crucial for business competitiveness.
4. Comparative Summary
Business   Long-Term
Strategy   Cost   Suitability
Risk   Sustainability
Low
Continuing   Short-term
High   initially,   Poor
Maintenance   survival
high later
Balanced
Re-engineering Medium Moderate   Good
approach
Long-term
Replacement   High   Very High   Excellent
transformation
✅ In Summary:
• Continuing maintenance offers short-term cost savings but
grows risky and unsustainable.
• Re-engineering balances cost and risk, extending system life
while improving maintainability.
• Replacement demands high upfront investment but ensures
long-term sustainability and alignment with modern business
needs.
Hence, re-engineering is often the most practical and cost-effective strategy
for organizations that want modernization without the extreme risk or cost of
full system replacement.
Q6   [20]
********** 13 **********
--- page 14 ---
CO-2;   a Explain how a Level-0, Level-1, and Level-2 Data Flow Diagram (DFD) can   [10
be applied in the design of a Student Enrollment System. How do successive
BL-M   M]
levels increase the detail and functional decomposition of the process?
Level   Description   Detail Provided
Shows the system as a single
Level-0
process interacting with external Very high-level overview
(Context)
entities.
Breaks the system into core sub- Shows major functions and
Level-1
processes and data stores.   data relationships
Expands each sub-process into   Provides implementation-
Level-2
smaller, logical steps.   ready detail for design
CO-4;   b Evaluate how Efficiency, Maintainability, and Portability interrelate to   [10
determine overall software quality, and design a metric-based
BL-L   M]
evaluation framework to measure their combined impact
Efficiency, maintainability, and portability are interdependent attributes that
collectively determine software quality.
High efficiency ensures optimal performance, while maintainability allows
easy updates without degrading that performance.
Portability enhances system adaptability across platforms, influencing both
maintenance effort and efficiency.
Balancing these factors ensures sustainable performance and lower lifecycle
cost.
A metric-based framework can include CPU utilization, mean time to modify
(MTTM), and successful build rate across platforms to quantify overall
quality.
Q7   [20]
CO-3;   a Evaluate how adherence to Golden Rules and Interface Design Principles   [10
BL-H   (e.g., consistency, anticipation, focus) enhances usability and user   M]
satisfaction in modern web or mobile interfaces
Adherence to Golden Rules and Interface Design Principles ensures a
seamless, intuitive, and satisfying user experience.
Consistency in layout, icons, and navigation reduces cognitive load and helps
users predict behavior easily.
Anticipation enables systems to foresee user needs—like auto-suggestions or
shortcuts—reducing effort and frustration.
Focus and feedback guide user attention and confirm actions, improving
confidence and task completion speed.
Together, these principles enhance usability, minimize errors, and
significantly boost user satisfaction in modern interfaces.
********** 14 **********
--- page 15 ---
CO-4;   b Critically analyze how verification and validation complement each other in   [10
ensuring software reliability and propose an improved framework combining
BL-H   M]
both stages effectively
Verification and validation are complementary processes that together ensure
software reliability and quality assurance.
Verification checks whether the product is built correctly—through reviews,
inspections, and testing against specifications.
Validation ensures the right product is built—confirming it meets user needs
and real-world requirements.
Their integration minimizes defects, ensuring correctness and fitness for
purpose.
An improved framework combines early verification (static analysis, peer
reviews) with continuous validation (user testing, feedback loops) across all
SDLC phases, ensuring reliable, user-centered software delivery.
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 10310154840d

- Departments: Computer Engineering
- Programmes: MBATech Computer 7047
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_Computer_7047/Software Engineering/ANS_Software Engineering(702IT0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Software Engineering
Date: 02 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 Questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   [20]
CO-1;   a Differentiate between generic software products and customized software   [5 M]
BL-L   solutions. Which type is likely to yield higher revenue for a company, and
what factors contribute to this difference?
1. Generic Software Products:
• Generic software products are developed to serve the needs of a wide
range of users or organizations.
• They are commercially packaged and sold in the market to multiple
customers (e.g., Microsoft Office, Adobe Photoshop).
• Development cost is high initially, but it is recovered through mass
sales, licensing, or subscriptions.
•   Support, updates, and new versions are released periodically to
maintain competitiveness.
2. Customized Software Solutions:
• Customized software is developed specifically for a single client or
organization according to unique business needs.
•   It is tailor-made, often involving client collaboration during the
development process.
• Maintenance and updates are client-specific, and reuse across other
clients is minimal.
********** 1 **********
--- page 2 ---
• Cost and development time are higher per project due to detailed
requirement analysis and integration efforts.
Aspect   Generic Software   Customized Software
Target Market   Mass market   Specific client
Volume sales &   One-time project
Revenue Type
licensing   payments
Development Cost
Through multiple users Through single client
Recovery
Revenue Potential   High (long-term)   Moderate (short-term)
CO-   b Why is the Spiral Model regarded as a meta-model in software development?   [5 M]
2,BL-L
Explanation:
1. Combination of Multiple Models:
Each phase (or “loop”) of the spiral can adopt a different process
model depending on project needs.
o For example, one iteration may follow a Waterfall approach
for documentation, while another may use Prototyping for user
interface design.
2. Risk-Driven Framework:
The Spiral Model’s main focus is risk analysis and risk reduction at
every iteration, which guides the selection of an appropriate process
for the next phase.
This adaptability allows it to encompass and manage other models
under its structure.
3. Iterative and Evolutionary Nature:
Like the Iterative model, the Spiral Model continuously refines
requirements and design through repeated cycles, each adding more
detail and functionality.
4. Meta-Model Concept:
Because the Spiral Model can include, control, or guide other models
within its framework, it acts as a “model of models”—that is, a meta-
model in software engineering.
CO-3;   c   Define UML and describe its purpose in object-oriented software   [5 M]
BL-L   development.
Definition of UML:
UML stands for Unified Modeling Language.
It is a standardized visual modeling language used to specify, visualize,
construct, and document the components of a software system, particularly
those developed using object-oriented (OO) principles.
********** 2 **********
--- page 3 ---
Purpose of UML in Object-Oriented Software Development:
1. Visual Representation of System Design:
UML provides diagrams (like class, use-case, sequence, and activity
diagrams) that help in visualizing the system’s architecture, behavior,
and interactions.
2. Enhances Communication:
It serves as a common language among developers, designers,
analysts, and stakeholders, improving understanding and reducing
ambiguity.
3. Supports OO Concepts:
UML directly represents object-oriented features such as classes,
inheritance, polymorphism, and associations.
4. Facilitates Analysis and Design:
It helps in analyzing system requirements and designing software
architecture before actual coding begins, leading to fewer design
flaws.
5. Provides Documentation and Maintainability:
UML diagrams act as comprehensive documentation, aiding future
maintenance, system upgrades, and team transitions.
CO-4;   d Compare and Contrast Unit Testing with Integration Testing.   [5 M]
BL-L   Aspect   Unit Testing   Integration Testing
Individual module
Focus   Interaction between modules
correctness
Coarser-grained (module
Granularity   Fine-grained (small units)
combinations)
Responsibility Developer   Tester/QA
Early in SDLC (after
Timing   After successful unit testing
coding)
Goal   Validate internal logic   Validate combined functionality
Q2   [20]
CO-1;   a Explain how Extreme Programming (XP) incorporates the concepts of pair   [10
BL-L   programming and continuous testing to improve software quality.   M]
Here’s a complete and structured answer to your question:
Answer:
Extreme Programming (XP) is an agile software development methodology
that emphasizes customer satisfaction, teamwork, and adaptability. Two of its
core practices—pair programming and continuous testing—play a key role in
improving software quality.
********** 3 **********
--- page 4 ---
1. Pair Programming:
•   Definition:
Pair programming means two programmers work together on the same
workstation.
One acts as the driver (writes the code), and the other acts as the
observer or navigator (reviews each line of code in real time).
• How it improves quality:
1. Real-time code review: Continuous peer checking detects logic
and syntax errors early.
2. Knowledge sharing: Enhances team understanding and avoids
dependency on a single developer.
3. Improved design decisions: Two minds working together
produce cleaner, well-structured code.
4. Better adherence to coding standards: Promotes consistent
style and structure across the project.
5. Reduced defects: Early detection leads to fewer bugs in later
stages of testing.
2. Continuous Testing:
•   Definition:
In XP, tests are written before or alongside the code (Test-Driven
Development, or TDD), and executed continuously throughout the
development process.
• How it improves quality:
1. Immediate feedback: Developers know instantly if new code
breaks existing functionality.
2. Regression prevention: Continuous test execution ensures
stability after every code change.
3. Higher confidence in changes: Automated tests allow frequent
integration and refactoring.
4. Customer satisfaction: Frequent testing ensures software
continuously meets customer requirements.
5. Documentation through tests: Test cases serve as living
documentation for expected behavior.
3. Combined Impact on Quality:
•   Pair programming ensures better design and fewer coding errors,
while continuous testing ensures ongoing verification of system
behavior.
•   Together, they create a feedback-rich, defect-prevention environment,
resulting in robust, maintainable, and high-quality software.
********** 4 **********
--- page 5 ---
✅ In summary:
Extreme Programming integrates pair programming (collaborative
development) and continuous testing (early and repeated validation) to ensure
that software is reliable, flexible, and aligned with customer needs at every
stage of development.
CO-3;   b Evaluate the role of UML modeling in reducing development risk and   [10
propose how it can be integrated with agile methodologies for iterative
BL-M   M]
design validation.
Here’s a complete, detailed answer to your question:
Answer:
1. Role of UML Modeling in Reducing Development Risk:
1. Early Visualization of the System:
UML provides graphical models—like use case, class, and sequence
diagrams—that help teams visualize system architecture before
coding.
→ This reduces the risk of misunderstanding requirements and design
flaws.
2. Improved Communication:
UML serves as a common visual language among developers,
designers, and stakeholders.
→ It ensures clarity in understanding functionality and interactions,
reducing risks of misinterpretation.
3. Validation and Traceability:
Each UML diagram corresponds to a specific phase of SDLC
(requirements, design, testing).
→ This ensures traceability of requirements and early validation,
lowering the risk of rework.
4. Early Error Detection:
Visual modeling highlights inconsistencies, missing functionality, and
design bottlenecks before implementation, saving cost and time.
5. Facilitates Risk Management:
UML supports scenario modeling and “what-if” analysis, helping
identify critical components and potential failure points.
2. Integration of UML with Agile Methodologies for Iterative Design Validation:
1. Lightweight Modeling Approach:
Use UML diagrams selectively (e.g., use-case and class diagrams) in
agile sprints to represent evolving requirements without over-
documentation.
2. Continuous Design Refinement:
Update UML models incrementally as part of each sprint review to
reflect new or modified features.
→ Ensures design always aligns with current implementation.
********** 5 **********
--- page 6 ---
3. Model-Based Collaboration:
Integrate UML into Agile tools (like Jira, Enterprise Architect, or
Visual Paradigm) for real-time collaboration and visibility.
4. Executable Models and Test Alignment:
Combine UML behavioral diagrams (e.g., sequence/activity) with
automated test cases to validate system behavior iteratively.
5. Feedback Loop with Stakeholders:
Use UML visualizations during sprint demos to collect stakeholder
feedback quickly and reduce misunderstanding risk.
✅ In Summary:
UML modeling reduces development risk by improving clarity,
communication, and early validation of requirements and design.
When integrated into agile workflows through lightweight, iterative updates
and stakeholder feedback, it becomes a powerful tool for continuous design
validation and risk mitigation throughout the project lifecycle.
Q3   [20]
CO2 ,BL- a   [10
Analyze how human factors influence the success of agile projects and
H   M]
design a strategy to strengthen collaboration and trust within an agile team.
Here’s a detailed and well-structured answer to your question:
Answer:
1. Influence of Human Factors on Agile Project Success:
Agile methodologies—like Scrum or XP—depend heavily on people and
interactions rather than processes or tools. Therefore, human factors such as
motivation, trust, communication, and leadership play a crucial role in
determining the success of agile projects.
a) Communication and Collaboration:
•   Effective, open communication ensures that requirements, progress,
and challenges are clearly shared within the team.
• Miscommunication leads to misunderstanding of user stories, poor
sprint outcomes, and reduced team efficiency.
b) Trust and Psychological Safety:
• Team members must feel safe to express opinions, admit mistakes,
and share new ideas.
• Lack of trust discourages feedback, innovation, and ownership of
work.
c) Motivation and Empowerment:
• Agile emphasizes self-organizing teams where members take
ownership of tasks.
• Motivation drives creativity and continuous improvement; low morale
leads to missed deadlines and poor product quality.
********** 6 **********
--- page 7 ---
d) Leadership and Support:
• Servant leadership in agile helps facilitate the team rather than control
it.
•   Effective leaders remove impediments, encourage participation, and
recognize individual contributions.
e) Cultural and Emotional Intelligence:
• Understanding cultural differences and emotional cues ensures better
team cohesion, especially in distributed teams.
• Emotional intelligence fosters empathy and smoother conflict
resolution.
2. Strategy to Strengthen Collaboration and Trust in Agile Teams:
A structured approach to enhancing teamwork, trust, and shared ownership
can significantly improve agile outcomes.
a) Establish Clear Communication Channels:
• Use daily stand-ups, retrospectives, and sprint reviews to maintain
transparency.
• Encourage face-to-face or video interactions to build personal
connection and clarity.
b) Foster Psychological Safety:
• Create an environment where mistakes are viewed as learning
opportunities.
• Encourage open dialogue and constructive criticism during
retrospectives.
c) Build Shared Ownership and Accountability:
• Define clear sprint goals and assign responsibilities collectively.
•   Celebrate collective success rather than individual achievements to
reinforce teamwork.
d) Encourage Pair Programming and Peer Reviews:
•   Collaborative coding improves code quality, enhances learning, and
increases trust between developers.
e) Continuous Feedback and Recognition:
• Provide timely feedback during sprint reviews.
• Recognize contributions publicly to boost morale and reinforce
positive behavior.
f) Invest in Team Building and Empathy Training:
********** 7 **********
--- page 8 ---
• Conduct workshops or informal activities to strengthen interpersonal
relationships.
• Train team members in emotional intelligence to improve cooperation
and conflict management.
✅ In Summary:
Human factors like trust, motivation, and communication directly influence
agile project success.
By promoting psychological safety, open communication, shared
accountability, and continuous feedback, organizations can cultivate an agile
culture built on collaboration, respect, and trust, ultimately leading to higher
productivity and team satisfaction.
CO-3;   b Design an activity diagram for booking an appointment at the   [10
dispensary, which includes the sequential steps of requesting an
BL-H   M]
appointment, checking availability, confirming a slot, generating a
token, and finally confirming the appointment, while also representing
the decision flow when a slot is unavailable and looping back to check
for another available slot before completion?
2 MARKS FOR EACH STEP
Q4   [20]
CO-2;   a   Illustrate how Sprint Planning and Daily Scrum meetings contribute to   [10
BL-M   incremental delivery and team synchronization.   M]
Here’s a clear and detailed explanation for your question:
Answer:
********** 8 **********
--- page 9 ---
In Agile Scrum, both Sprint Planning and Daily Scrum meetings are essential
ceremonies that ensure incremental delivery of the product and maintain team
synchronization throughout the development cycle.
1. Sprint Planning – Foundation for Incremental Delivery
Definition:
Sprint Planning is a meeting held at the beginning of each sprint to define
what work will be done and how it will be accomplished during that sprint.
Contribution to Incremental Delivery:
1. Defines Clear Sprint Goals:
The team collaborates with the Product Owner to set achievable sprint
objectives that represent a potentially shippable product increment.
2. Prioritization of Work:
User stories are selected from the Product Backlog based on business
value and team capacity, ensuring that high-value features are
delivered first.
3. Task Breakdown:
Each selected story is decomposed into smaller, manageable tasks.
This structure enables the team to complete and deliver working
software iteratively.
4. Commitment and Estimation:
The team estimates effort and commits to deliver a small, functional
increment within the sprint timebox (usually 2–4 weeks).
5. Transparency and Predictability:
The planning process aligns the entire team around what will be
delivered, enhancing visibility and accountability.
2. Daily Scrum – Engine for Team Synchronization
Definition:
The Daily Scrum (Stand-up) is a short, time-boxed (15-minute) meeting held
every day of the sprint where each team member discusses progress, plans,
and blockers.
Contribution to Team Synchronization:
1. Continuous Alignment:
Keeps all members informed about who is doing what, ensuring
coordinated progress toward the sprint goal.
2. Early Problem Detection:
Team members identify impediments or dependencies early so the
Scrum Master can resolve them promptly.
3. Adaptive Planning:
Daily updates allow the team to adjust priorities or reallocate tasks
based on current progress or new challenges.
********** 9 **********
--- page 10 ---
4. Accountability and Focus:
By sharing daily updates, members stay focused and accountable,
reducing duplication of work and improving productivity.
5. Enhanced Communication:
Promotes open collaboration and strengthens trust among team
members, particularly in cross-functional teams.
3. Combined Impact:
•   Sprint Planning sets the direction for incremental delivery.
• Daily Scrum maintains momentum and synchronization through
continuous feedback and alignment.
Together, they ensure that:
• Work remains on track.
• Increments are delivered regularly.
• The team remains cohesive, self-organized, and responsive to change.
✅ In Summary:
Sprint Planning defines the roadmap for each iteration, ensuring a focused
and achievable increment, while the Daily Scrum maintains alignment,
transparency, and adaptability among team members.
Together, they form the backbone of incremental delivery and continuous
team synchronization in Agile Scrum.
CO-3;   b Design the class diagram for Placement activity process. XYZ Institute of   [10
Technology conducts annual campus placements for final-year students across
BL-L   M]
Engineering and Management disciplines. The Placement Cell, in coordination
with faculty and student representatives, manages end-to-end activities from
company outreach to offer letter distribution.
Q5   [20]
CO-3;   a Design a labeled state transition model for following problem statement.   [10
“A food delivery company is developing an Online Food Delivery System to
BL-M   M]
manage the complete life cycle of a Food Order object. Each Food Order
********** 10 **********
--- page 11 ---
represents a customer’s request to purchase items from a restaurant. The
order passes through a sequence of states from creation until completion or
cancellation. When a customer requests an order, a new Food Order is
created. Once payment is made successfully, the order Confirmed. If the
payment fails, the order moves to the “Payment Failed” state, from which it
can either be retried or cancelled permanently. After confirmation, the order
is sent to the Restaurant, to Being Prepared. When preparation is completed,
the order moves to “Ready for Pickup.” At this stage, a Delivery Person is
assigned, and the order transitions to the “Out for Delivery”. If the delivery is
successful, the order marked as “Delivered”. However, if the customer rejects
the order or the delivery fails, it marks as “Returned” or “Cancelled”
respectively.
: 5 marks for state and 5 marks for labelled transition.
CO-2;   b Compare the effectiveness of continuing maintenance, re-engineering, and   [10
replacement strategies for legacy systems in terms of business risk, cost, and
BL-H   M]
long-term sustainability.
Here’s a comprehensive and structured answer to your question:
Answer:
Legacy systems are older software systems that remain in use because they
perform critical business functions. Organizations often face a strategic
decision between continuing maintenance, re-engineering, or replacing these
systems. Each strategy differs in its impact on business risk, cost, and long-
term sustainability.
1. Continuing Maintenance
********** 11 **********
--- page 12 ---
Definition:
Continuing maintenance means keeping the legacy system operational with
minimal updates or bug fixes, without major architectural changes.
Evaluation:
Aspect   Analysis
Moderate to High — Risk of system failure increases
Business Risk   over time due to obsolete technology and lack of vendor
support.
Low short-term cost (since changes are minimal), but
Cost   high long-term maintenance costs as patching becomes
complex.
Poor — Difficult to adapt to new technologies, security
Long-term
risks increase, and skilled manpower for old platforms
Sustainability
becomes scarce.
Conclusion:
Suitable when the system is stable, low-change, and still meets essential
business needs with minimal enhancement requirements.
2. Re-engineering
Definition:
Re-engineering involves analyzing, restructuring, and optimizing the existing
legacy system to improve maintainability, performance, and compatibility
without complete replacement.
Evaluation:
Aspect   Analysis
Medium — Controlled risk since business logic is
Business Risk   preserved; risk occurs mainly during migration or code
transformation.
Moderate — Requires investment in analysis, redesign,
Cost   and partial redevelopment. Cost is balanced by improved
efficiency.
Long-term   Good — Extends system life, reduces technical debt, and
Sustainability   allows integration with modern platforms.
Conclusion:
Effective when the legacy system has high business value but suffers from
technical inefficiencies or outdated architecture.
3. Replacement
********** 12 **********
--- page 13 ---
Definition:
Replacement involves developing or acquiring a completely new system to
substitute the legacy system and migrate essential data and processes.
Evaluation:
Aspect   Analysis
High — Risk of data loss, user resistance, and functional
Business Risk
gaps during transition to the new system.
Very High — Involves full system development,
Cost
training, data migration, and infrastructure setup.
Excellent — New technologies provide better scalability,
Long-term
integration, and security; supports future business
Sustainability
growth.
Conclusion:
Ideal when the legacy system’s maintenance cost exceeds its value or when
modernization is crucial for business competitiveness.
4. Comparative Summary
Business   Long-Term
Strategy   Cost   Suitability
Risk   Sustainability
Low
Continuing   Short-term
High   initially,   Poor
Maintenance   survival
high later
Balanced
Re-engineering Medium Moderate   Good
approach
Long-term
Replacement   High   Very High   Excellent
transformation
✅ In Summary:
• Continuing maintenance offers short-term cost savings but
grows risky and unsustainable.
• Re-engineering balances cost and risk, extending system life
while improving maintainability.
• Replacement demands high upfront investment but ensures
long-term sustainability and alignment with modern business
needs.
Hence, re-engineering is often the most practical and cost-effective strategy
for organizations that want modernization without the extreme risk or cost of
full system replacement.
Q6   [20]
********** 13 **********
--- page 14 ---
CO-2;   a Explain how a Level-0, Level-1, and Level-2 Data Flow Diagram (DFD) can   [10
be applied in the design of a Student Enrollment System. How do successive
BL-M   M]
levels increase the detail and functional decomposition of the process?
Level   Description   Detail Provided
Shows the system as a single
Level-0
process interacting with external Very high-level overview
(Context)
entities.
Breaks the system into core sub- Shows major functions and
Level-1
processes and data stores.   data relationships
Expands each sub-process into   Provides implementation-
Level-2
smaller, logical steps.   ready detail for design
CO-4;   b Evaluate how Efficiency, Maintainability, and Portability interrelate to   [10
determine overall software quality, and design a metric-based
BL-L   M]
evaluation framework to measure their combined impact
Efficiency, maintainability, and portability are interdependent attributes that
collectively determine software quality.
High efficiency ensures optimal performance, while maintainability allows
easy updates without degrading that performance.
Portability enhances system adaptability across platforms, influencing both
maintenance effort and efficiency.
Balancing these factors ensures sustainable performance and lower lifecycle
cost.
A metric-based framework can include CPU utilization, mean time to modify
(MTTM), and successful build rate across platforms to quantify overall
quality.
Q7   [20]
CO-3;   a Evaluate how adherence to Golden Rules and Interface Design Principles   [10
BL-H   (e.g., consistency, anticipation, focus) enhances usability and user   M]
satisfaction in modern web or mobile interfaces
Adherence to Golden Rules and Interface Design Principles ensures a
seamless, intuitive, and satisfying user experience.
Consistency in layout, icons, and navigation reduces cognitive load and helps
users predict behavior easily.
Anticipation enables systems to foresee user needs—like auto-suggestions or
shortcuts—reducing effort and frustration.
Focus and feedback guide user attention and confirm actions, improving
confidence and task completion speed.
Together, these principles enhance usability, minimize errors, and
significantly boost user satisfaction in modern interfaces.
********** 14 **********
--- page 15 ---
CO-4;   b Critically analyze how verification and validation complement each other in   [10
ensuring software reliability and propose an improved framework combining
BL-H   M]
both stages effectively
Verification and validation are complementary processes that together ensure
software reliability and quality assurance.
Verification checks whether the product is built correctly—through reviews,
inspections, and testing against specifications.
Validation ensures the right product is built—confirming it meets user needs
and real-world requirements.
Their integration minimizes defects, ensuring correctness and fitness for
purpose.
An improved framework combines early verification (static analysis, peer
reviews) with continuous validation (user testing, feedback loops) across all
SDLC phases, ensuring reliable, user-centered software delivery.
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 5 · Answer key · paper 887ca75f7b64

- Departments: Information Technology
- Programmes: MBATech IT 7041
- Source: `02_Question_Papers/2025/Sem_05/Re-Exam/MBATech_IT_7041/Software Engineering/ANS_Software Engineering(702IT0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Software Engineering
Date: 02 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 Questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   [20]
CO-1;   a Differentiate between generic software products and customized software   [5 M]
BL-L   solutions. Which type is likely to yield higher revenue for a company, and
what factors contribute to this difference?
1. Generic Software Products:
• Generic software products are developed to serve the needs of a wide
range of users or organizations.
• They are commercially packaged and sold in the market to multiple
customers (e.g., Microsoft Office, Adobe Photoshop).
• Development cost is high initially, but it is recovered through mass
sales, licensing, or subscriptions.
•   Support, updates, and new versions are released periodically to
maintain competitiveness.
2. Customized Software Solutions:
• Customized software is developed specifically for a single client or
organization according to unique business needs.
•   It is tailor-made, often involving client collaboration during the
development process.
• Maintenance and updates are client-specific, and reuse across other
clients is minimal.
********** 1 **********
--- page 2 ---
• Cost and development time are higher per project due to detailed
requirement analysis and integration efforts.
Aspect   Generic Software   Customized Software
Target Market   Mass market   Specific client
Volume sales &   One-time project
Revenue Type
licensing   payments
Development Cost
Through multiple users Through single client
Recovery
Revenue Potential   High (long-term)   Moderate (short-term)
CO-   b Why is the Spiral Model regarded as a meta-model in software development?   [5 M]
2,BL-L
Explanation:
1. Combination of Multiple Models:
Each phase (or “loop”) of the spiral can adopt a different process
model depending on project needs.
o For example, one iteration may follow a Waterfall approach
for documentation, while another may use Prototyping for user
interface design.
2. Risk-Driven Framework:
The Spiral Model’s main focus is risk analysis and risk reduction at
every iteration, which guides the selection of an appropriate process
for the next phase.
This adaptability allows it to encompass and manage other models
under its structure.
3. Iterative and Evolutionary Nature:
Like the Iterative model, the Spiral Model continuously refines
requirements and design through repeated cycles, each adding more
detail and functionality.
4. Meta-Model Concept:
Because the Spiral Model can include, control, or guide other models
within its framework, it acts as a “model of models”—that is, a meta-
model in software engineering.
CO-3;   c   Define UML and describe its purpose in object-oriented software   [5 M]
BL-L   development.
Definition of UML:
UML stands for Unified Modeling Language.
It is a standardized visual modeling language used to specify, visualize,
construct, and document the components of a software system, particularly
those developed using object-oriented (OO) principles.
********** 2 **********
--- page 3 ---
Purpose of UML in Object-Oriented Software Development:
1. Visual Representation of System Design:
UML provides diagrams (like class, use-case, sequence, and activity
diagrams) that help in visualizing the system’s architecture, behavior,
and interactions.
2. Enhances Communication:
It serves as a common language among developers, designers,
analysts, and stakeholders, improving understanding and reducing
ambiguity.
3. Supports OO Concepts:
UML directly represents object-oriented features such as classes,
inheritance, polymorphism, and associations.
4. Facilitates Analysis and Design:
It helps in analyzing system requirements and designing software
architecture before actual coding begins, leading to fewer design
flaws.
5. Provides Documentation and Maintainability:
UML diagrams act as comprehensive documentation, aiding future
maintenance, system upgrades, and team transitions.
CO-4;   d Compare and Contrast Unit Testing with Integration Testing.   [5 M]
BL-L   Aspect   Unit Testing   Integration Testing
Individual module
Focus   Interaction between modules
correctness
Coarser-grained (module
Granularity   Fine-grained (small units)
combinations)
Responsibility Developer   Tester/QA
Early in SDLC (after
Timing   After successful unit testing
coding)
Goal   Validate internal logic   Validate combined functionality
Q2   [20]
CO-1;   a Explain how Extreme Programming (XP) incorporates the concepts of pair   [10
BL-L   programming and continuous testing to improve software quality.   M]
Here’s a complete and structured answer to your question:
Answer:
Extreme Programming (XP) is an agile software development methodology
that emphasizes customer satisfaction, teamwork, and adaptability. Two of its
core practices—pair programming and continuous testing—play a key role in
improving software quality.
********** 3 **********
--- page 4 ---
1. Pair Programming:
•   Definition:
Pair programming means two programmers work together on the same
workstation.
One acts as the driver (writes the code), and the other acts as the
observer or navigator (reviews each line of code in real time).
• How it improves quality:
1. Real-time code review: Continuous peer checking detects logic
and syntax errors early.
2. Knowledge sharing: Enhances team understanding and avoids
dependency on a single developer.
3. Improved design decisions: Two minds working together
produce cleaner, well-structured code.
4. Better adherence to coding standards: Promotes consistent
style and structure across the project.
5. Reduced defects: Early detection leads to fewer bugs in later
stages of testing.
2. Continuous Testing:
•   Definition:
In XP, tests are written before or alongside the code (Test-Driven
Development, or TDD), and executed continuously throughout the
development process.
• How it improves quality:
1. Immediate feedback: Developers know instantly if new code
breaks existing functionality.
2. Regression prevention: Continuous test execution ensures
stability after every code change.
3. Higher confidence in changes: Automated tests allow frequent
integration and refactoring.
4. Customer satisfaction: Frequent testing ensures software
continuously meets customer requirements.
5. Documentation through tests: Test cases serve as living
documentation for expected behavior.
3. Combined Impact on Quality:
•   Pair programming ensures better design and fewer coding errors,
while continuous testing ensures ongoing verification of system
behavior.
•   Together, they create a feedback-rich, defect-prevention environment,
resulting in robust, maintainable, and high-quality software.
********** 4 **********
--- page 5 ---
✅ In summary:
Extreme Programming integrates pair programming (collaborative
development) and continuous testing (early and repeated validation) to ensure
that software is reliable, flexible, and aligned with customer needs at every
stage of development.
CO-3;   b Evaluate the role of UML modeling in reducing development risk and   [10
propose how it can be integrated with agile methodologies for iterative
BL-M   M]
design validation.
Here’s a complete, detailed answer to your question:
Answer:
1. Role of UML Modeling in Reducing Development Risk:
1. Early Visualization of the System:
UML provides graphical models—like use case, class, and sequence
diagrams—that help teams visualize system architecture before
coding.
→ This reduces the risk of misunderstanding requirements and design
flaws.
2. Improved Communication:
UML serves as a common visual language among developers,
designers, and stakeholders.
→ It ensures clarity in understanding functionality and interactions,
reducing risks of misinterpretation.
3. Validation and Traceability:
Each UML diagram corresponds to a specific phase of SDLC
(requirements, design, testing).
→ This ensures traceability of requirements and early validation,
lowering the risk of rework.
4. Early Error Detection:
Visual modeling highlights inconsistencies, missing functionality, and
design bottlenecks before implementation, saving cost and time.
5. Facilitates Risk Management:
UML supports scenario modeling and “what-if” analysis, helping
identify critical components and potential failure points.
2. Integration of UML with Agile Methodologies for Iterative Design Validation:
1. Lightweight Modeling Approach:
Use UML diagrams selectively (e.g., use-case and class diagrams) in
agile sprints to represent evolving requirements without over-
documentation.
2. Continuous Design Refinement:
Update UML models incrementally as part of each sprint review to
reflect new or modified features.
→ Ensures design always aligns with current implementation.
********** 5 **********
--- page 6 ---
3. Model-Based Collaboration:
Integrate UML into Agile tools (like Jira, Enterprise Architect, or
Visual Paradigm) for real-time collaboration and visibility.
4. Executable Models and Test Alignment:
Combine UML behavioral diagrams (e.g., sequence/activity) with
automated test cases to validate system behavior iteratively.
5. Feedback Loop with Stakeholders:
Use UML visualizations during sprint demos to collect stakeholder
feedback quickly and reduce misunderstanding risk.
✅ In Summary:
UML modeling reduces development risk by improving clarity,
communication, and early validation of requirements and design.
When integrated into agile workflows through lightweight, iterative updates
and stakeholder feedback, it becomes a powerful tool for continuous design
validation and risk mitigation throughout the project lifecycle.
Q3   [20]
CO2 ,BL- a   [10
Analyze how human factors influence the success of agile projects and
H   M]
design a strategy to strengthen collaboration and trust within an agile team.
Here’s a detailed and well-structured answer to your question:
Answer:
1. Influence of Human Factors on Agile Project Success:
Agile methodologies—like Scrum or XP—depend heavily on people and
interactions rather than processes or tools. Therefore, human factors such as
motivation, trust, communication, and leadership play a crucial role in
determining the success of agile projects.
a) Communication and Collaboration:
•   Effective, open communication ensures that requirements, progress,
and challenges are clearly shared within the team.
• Miscommunication leads to misunderstanding of user stories, poor
sprint outcomes, and reduced team efficiency.
b) Trust and Psychological Safety:
• Team members must feel safe to express opinions, admit mistakes,
and share new ideas.
• Lack of trust discourages feedback, innovation, and ownership of
work.
c) Motivation and Empowerment:
• Agile emphasizes self-organizing teams where members take
ownership of tasks.
• Motivation drives creativity and continuous improvement; low morale
leads to missed deadlines and poor product quality.
********** 6 **********
--- page 7 ---
d) Leadership and Support:
• Servant leadership in agile helps facilitate the team rather than control
it.
•   Effective leaders remove impediments, encourage participation, and
recognize individual contributions.
e) Cultural and Emotional Intelligence:
• Understanding cultural differences and emotional cues ensures better
team cohesion, especially in distributed teams.
• Emotional intelligence fosters empathy and smoother conflict
resolution.
2. Strategy to Strengthen Collaboration and Trust in Agile Teams:
A structured approach to enhancing teamwork, trust, and shared ownership
can significantly improve agile outcomes.
a) Establish Clear Communication Channels:
• Use daily stand-ups, retrospectives, and sprint reviews to maintain
transparency.
• Encourage face-to-face or video interactions to build personal
connection and clarity.
b) Foster Psychological Safety:
• Create an environment where mistakes are viewed as learning
opportunities.
• Encourage open dialogue and constructive criticism during
retrospectives.
c) Build Shared Ownership and Accountability:
• Define clear sprint goals and assign responsibilities collectively.
•   Celebrate collective success rather than individual achievements to
reinforce teamwork.
d) Encourage Pair Programming and Peer Reviews:
•   Collaborative coding improves code quality, enhances learning, and
increases trust between developers.
e) Continuous Feedback and Recognition:
• Provide timely feedback during sprint reviews.
• Recognize contributions publicly to boost morale and reinforce
positive behavior.
f) Invest in Team Building and Empathy Training:
********** 7 **********
--- page 8 ---
• Conduct workshops or informal activities to strengthen interpersonal
relationships.
• Train team members in emotional intelligence to improve cooperation
and conflict management.
✅ In Summary:
Human factors like trust, motivation, and communication directly influence
agile project success.
By promoting psychological safety, open communication, shared
accountability, and continuous feedback, organizations can cultivate an agile
culture built on collaboration, respect, and trust, ultimately leading to higher
productivity and team satisfaction.
CO-3;   b Design an activity diagram for booking an appointment at the   [10
dispensary, which includes the sequential steps of requesting an
BL-H   M]
appointment, checking availability, confirming a slot, generating a
token, and finally confirming the appointment, while also representing
the decision flow when a slot is unavailable and looping back to check
for another available slot before completion?
2 MARKS FOR EACH STEP
Q4   [20]
CO-2;   a   Illustrate how Sprint Planning and Daily Scrum meetings contribute to   [10
BL-M   incremental delivery and team synchronization.   M]
Here’s a clear and detailed explanation for your question:
Answer:
********** 8 **********
--- page 9 ---
In Agile Scrum, both Sprint Planning and Daily Scrum meetings are essential
ceremonies that ensure incremental delivery of the product and maintain team
synchronization throughout the development cycle.
1. Sprint Planning – Foundation for Incremental Delivery
Definition:
Sprint Planning is a meeting held at the beginning of each sprint to define
what work will be done and how it will be accomplished during that sprint.
Contribution to Incremental Delivery:
1. Defines Clear Sprint Goals:
The team collaborates with the Product Owner to set achievable sprint
objectives that represent a potentially shippable product increment.
2. Prioritization of Work:
User stories are selected from the Product Backlog based on business
value and team capacity, ensuring that high-value features are
delivered first.
3. Task Breakdown:
Each selected story is decomposed into smaller, manageable tasks.
This structure enables the team to complete and deliver working
software iteratively.
4. Commitment and Estimation:
The team estimates effort and commits to deliver a small, functional
increment within the sprint timebox (usually 2–4 weeks).
5. Transparency and Predictability:
The planning process aligns the entire team around what will be
delivered, enhancing visibility and accountability.
2. Daily Scrum – Engine for Team Synchronization
Definition:
The Daily Scrum (Stand-up) is a short, time-boxed (15-minute) meeting held
every day of the sprint where each team member discusses progress, plans,
and blockers.
Contribution to Team Synchronization:
1. Continuous Alignment:
Keeps all members informed about who is doing what, ensuring
coordinated progress toward the sprint goal.
2. Early Problem Detection:
Team members identify impediments or dependencies early so the
Scrum Master can resolve them promptly.
3. Adaptive Planning:
Daily updates allow the team to adjust priorities or reallocate tasks
based on current progress or new challenges.
********** 9 **********
--- page 10 ---
4. Accountability and Focus:
By sharing daily updates, members stay focused and accountable,
reducing duplication of work and improving productivity.
5. Enhanced Communication:
Promotes open collaboration and strengthens trust among team
members, particularly in cross-functional teams.
3. Combined Impact:
•   Sprint Planning sets the direction for incremental delivery.
• Daily Scrum maintains momentum and synchronization through
continuous feedback and alignment.
Together, they ensure that:
• Work remains on track.
• Increments are delivered regularly.
• The team remains cohesive, self-organized, and responsive to change.
✅ In Summary:
Sprint Planning defines the roadmap for each iteration, ensuring a focused
and achievable increment, while the Daily Scrum maintains alignment,
transparency, and adaptability among team members.
Together, they form the backbone of incremental delivery and continuous
team synchronization in Agile Scrum.
CO-3;   b Design the class diagram for Placement activity process. XYZ Institute of   [10
Technology conducts annual campus placements for final-year students across
BL-L   M]
Engineering and Management disciplines. The Placement Cell, in coordination
with faculty and student representatives, manages end-to-end activities from
company outreach to offer letter distribution.
Q5   [20]
CO-3;   a Design a labeled state transition model for following problem statement.   [10
“A food delivery company is developing an Online Food Delivery System to
BL-M   M]
manage the complete life cycle of a Food Order object. Each Food Order
********** 10 **********
--- page 11 ---
represents a customer’s request to purchase items from a restaurant. The
order passes through a sequence of states from creation until completion or
cancellation. When a customer requests an order, a new Food Order is
created. Once payment is made successfully, the order Confirmed. If the
payment fails, the order moves to the “Payment Failed” state, from which it
can either be retried or cancelled permanently. After confirmation, the order
is sent to the Restaurant, to Being Prepared. When preparation is completed,
the order moves to “Ready for Pickup.” At this stage, a Delivery Person is
assigned, and the order transitions to the “Out for Delivery”. If the delivery is
successful, the order marked as “Delivered”. However, if the customer rejects
the order or the delivery fails, it marks as “Returned” or “Cancelled”
respectively.
: 5 marks for state and 5 marks for labelled transition.
CO-2;   b Compare the effectiveness of continuing maintenance, re-engineering, and   [10
replacement strategies for legacy systems in terms of business risk, cost, and
BL-H   M]
long-term sustainability.
Here’s a comprehensive and structured answer to your question:
Answer:
Legacy systems are older software systems that remain in use because they
perform critical business functions. Organizations often face a strategic
decision between continuing maintenance, re-engineering, or replacing these
systems. Each strategy differs in its impact on business risk, cost, and long-
term sustainability.
1. Continuing Maintenance
********** 11 **********
--- page 12 ---
Definition:
Continuing maintenance means keeping the legacy system operational with
minimal updates or bug fixes, without major architectural changes.
Evaluation:
Aspect   Analysis
Moderate to High — Risk of system failure increases
Business Risk   over time due to obsolete technology and lack of vendor
support.
Low short-term cost (since changes are minimal), but
Cost   high long-term maintenance costs as patching becomes
complex.
Poor — Difficult to adapt to new technologies, security
Long-term
risks increase, and skilled manpower for old platforms
Sustainability
becomes scarce.
Conclusion:
Suitable when the system is stable, low-change, and still meets essential
business needs with minimal enhancement requirements.
2. Re-engineering
Definition:
Re-engineering involves analyzing, restructuring, and optimizing the existing
legacy system to improve maintainability, performance, and compatibility
without complete replacement.
Evaluation:
Aspect   Analysis
Medium — Controlled risk since business logic is
Business Risk   preserved; risk occurs mainly during migration or code
transformation.
Moderate — Requires investment in analysis, redesign,
Cost   and partial redevelopment. Cost is balanced by improved
efficiency.
Long-term   Good — Extends system life, reduces technical debt, and
Sustainability   allows integration with modern platforms.
Conclusion:
Effective when the legacy system has high business value but suffers from
technical inefficiencies or outdated architecture.
3. Replacement
********** 12 **********
--- page 13 ---
Definition:
Replacement involves developing or acquiring a completely new system to
substitute the legacy system and migrate essential data and processes.
Evaluation:
Aspect   Analysis
High — Risk of data loss, user resistance, and functional
Business Risk
gaps during transition to the new system.
Very High — Involves full system development,
Cost
training, data migration, and infrastructure setup.
Excellent — New technologies provide better scalability,
Long-term
integration, and security; supports future business
Sustainability
growth.
Conclusion:
Ideal when the legacy system’s maintenance cost exceeds its value or when
modernization is crucial for business competitiveness.
4. Comparative Summary
Business   Long-Term
Strategy   Cost   Suitability
Risk   Sustainability
Low
Continuing   Short-term
High   initially,   Poor
Maintenance   survival
high later
Balanced
Re-engineering Medium Moderate   Good
approach
Long-term
Replacement   High   Very High   Excellent
transformation
✅ In Summary:
• Continuing maintenance offers short-term cost savings but
grows risky and unsustainable.
• Re-engineering balances cost and risk, extending system life
while improving maintainability.
• Replacement demands high upfront investment but ensures
long-term sustainability and alignment with modern business
needs.
Hence, re-engineering is often the most practical and cost-effective strategy
for organizations that want modernization without the extreme risk or cost of
full system replacement.
Q6   [20]
********** 13 **********
--- page 14 ---
CO-2;   a Explain how a Level-0, Level-1, and Level-2 Data Flow Diagram (DFD) can   [10
be applied in the design of a Student Enrollment System. How do successive
BL-M   M]
levels increase the detail and functional decomposition of the process?
Level   Description   Detail Provided
Shows the system as a single
Level-0
process interacting with external Very high-level overview
(Context)
entities.
Breaks the system into core sub- Shows major functions and
Level-1
processes and data stores.   data relationships
Expands each sub-process into   Provides implementation-
Level-2
smaller, logical steps.   ready detail for design
CO-4;   b Evaluate how Efficiency, Maintainability, and Portability interrelate to   [10
determine overall software quality, and design a metric-based
BL-L   M]
evaluation framework to measure their combined impact
Efficiency, maintainability, and portability are interdependent attributes that
collectively determine software quality.
High efficiency ensures optimal performance, while maintainability allows
easy updates without degrading that performance.
Portability enhances system adaptability across platforms, influencing both
maintenance effort and efficiency.
Balancing these factors ensures sustainable performance and lower lifecycle
cost.
A metric-based framework can include CPU utilization, mean time to modify
(MTTM), and successful build rate across platforms to quantify overall
quality.
Q7   [20]
CO-3;   a Evaluate how adherence to Golden Rules and Interface Design Principles   [10
BL-H   (e.g., consistency, anticipation, focus) enhances usability and user   M]
satisfaction in modern web or mobile interfaces
Adherence to Golden Rules and Interface Design Principles ensures a
seamless, intuitive, and satisfying user experience.
Consistency in layout, icons, and navigation reduces cognitive load and helps
users predict behavior easily.
Anticipation enables systems to foresee user needs—like auto-suggestions or
shortcuts—reducing effort and frustration.
Focus and feedback guide user attention and confirm actions, improving
confidence and task completion speed.
Together, these principles enhance usability, minimize errors, and
significantly boost user satisfaction in modern interfaces.
********** 14 **********
--- page 15 ---
CO-4;   b Critically analyze how verification and validation complement each other in   [10
ensuring software reliability and propose an improved framework combining
BL-H   M]
both stages effectively
Verification and validation are complementary processes that together ensure
software reliability and quality assurance.
Verification checks whether the product is built correctly—through reviews,
inspections, and testing against specifications.
Validation ensures the right product is built—confirming it meets user needs
and real-world requirements.
Their integration minimizes defects, ensuring correctness and fitness for
purpose.
An improved framework combines early verification (static analysis, peer
reviews) with continuous validation (user testing, feedback loops) across all
SDLC phases, ensuring reliable, user-centered software delivery.
********** 15 **********
````

## 2025-26 · Re-Exam · Sem 9 · Answer key · paper 07d41717e999

- Departments: Computer Engineering
- Programmes: Integrated Computer 7032
- Source: `02_Question_Papers/2025/Sem_09/Re-Exam/Integrated_Computer_7032/Software Engineering/ANS_Software Engineering(702IT0C016)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 02 Feb 2026
- Text: text (15 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: B. Tech (COMP)/B. Tech (CS)/B. Tech (CSBS)/B. Tech (CSE - CS)/B. TECH
(CSE - DS)/B. Tech Intg. (CE)/B. Tech Intg. (IT)/B. Tech (IT)/MBA Tech (Comp)/MBA Tech
(IT)
Year: III / V/Sem 5 Re-exam/Sem 9 Re-exam(Exam Year: 2025-2026)
Subject: Software Engineering
Date: 02 Feb 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory
5. Out of remaining questions, attempt any 4 Questions
6. In all 5 questions to be attempted.
7. All questions carry equal marks.
8. Assume Suitable data if necessary.
Q1   [20]
CO-1;   a Differentiate between generic software products and customized software   [5 M]
BL-L   solutions. Which type is likely to yield higher revenue for a company, and
what factors contribute to this difference?
1. Generic Software Products:
• Generic software products are developed to serve the needs of a wide
range of users or organizations.
• They are commercially packaged and sold in the market to multiple
customers (e.g., Microsoft Office, Adobe Photoshop).
• Development cost is high initially, but it is recovered through mass
sales, licensing, or subscriptions.
•   Support, updates, and new versions are released periodically to
maintain competitiveness.
2. Customized Software Solutions:
• Customized software is developed specifically for a single client or
organization according to unique business needs.
•   It is tailor-made, often involving client collaboration during the
development process.
• Maintenance and updates are client-specific, and reuse across other
clients is minimal.
********** 1 **********
--- page 2 ---
• Cost and development time are higher per project due to detailed
requirement analysis and integration efforts.
Aspect   Generic Software   Customized Software
Target Market   Mass market   Specific client
Volume sales &   One-time project
Revenue Type
licensing   payments
Development Cost
Through multiple users Through single client
Recovery
Revenue Potential   High (long-term)   Moderate (short-term)
CO-   b Why is the Spiral Model regarded as a meta-model in software development?   [5 M]
2,BL-L
Explanation:
1. Combination of Multiple Models:
Each phase (or “loop”) of the spiral can adopt a different process
model depending on project needs.
o For example, one iteration may follow a Waterfall approach
for documentation, while another may use Prototyping for user
interface design.
2. Risk-Driven Framework:
The Spiral Model’s main focus is risk analysis and risk reduction at
every iteration, which guides the selection of an appropriate process
for the next phase.
This adaptability allows it to encompass and manage other models
under its structure.
3. Iterative and Evolutionary Nature:
Like the Iterative model, the Spiral Model continuously refines
requirements and design through repeated cycles, each adding more
detail and functionality.
4. Meta-Model Concept:
Because the Spiral Model can include, control, or guide other models
within its framework, it acts as a “model of models”—that is, a meta-
model in software engineering.
CO-3;   c   Define UML and describe its purpose in object-oriented software   [5 M]
BL-L   development.
Definition of UML:
UML stands for Unified Modeling Language.
It is a standardized visual modeling language used to specify, visualize,
construct, and document the components of a software system, particularly
those developed using object-oriented (OO) principles.
********** 2 **********
--- page 3 ---
Purpose of UML in Object-Oriented Software Development:
1. Visual Representation of System Design:
UML provides diagrams (like class, use-case, sequence, and activity
diagrams) that help in visualizing the system’s architecture, behavior,
and interactions.
2. Enhances Communication:
It serves as a common language among developers, designers,
analysts, and stakeholders, improving understanding and reducing
ambiguity.
3. Supports OO Concepts:
UML directly represents object-oriented features such as classes,
inheritance, polymorphism, and associations.
4. Facilitates Analysis and Design:
It helps in analyzing system requirements and designing software
architecture before actual coding begins, leading to fewer design
flaws.
5. Provides Documentation and Maintainability:
UML diagrams act as comprehensive documentation, aiding future
maintenance, system upgrades, and team transitions.
CO-4;   d Compare and Contrast Unit Testing with Integration Testing.   [5 M]
BL-L   Aspect   Unit Testing   Integration Testing
Individual module
Focus   Interaction between modules
correctness
Coarser-grained (module
Granularity   Fine-grained (small units)
combinations)
Responsibility Developer   Tester/QA
Early in SDLC (after
Timing   After successful unit testing
coding)
Goal   Validate internal logic   Validate combined functionality
Q2   [20]
CO-1;   a Explain how Extreme Programming (XP) incorporates the concepts of pair   [10
BL-L   programming and continuous testing to improve software quality.   M]
Here’s a complete and structured answer to your question:
Answer:
Extreme Programming (XP) is an agile software development methodology
that emphasizes customer satisfaction, teamwork, and adaptability. Two of its
core practices—pair programming and continuous testing—play a key role in
improving software quality.
********** 3 **********
--- page 4 ---
1. Pair Programming:
•   Definition:
Pair programming means two programmers work together on the same
workstation.
One acts as the driver (writes the code), and the other acts as the
observer or navigator (reviews each line of code in real time).
• How it improves quality:
1. Real-time code review: Continuous peer checking detects logic
and syntax errors early.
2. Knowledge sharing: Enhances team understanding and avoids
dependency on a single developer.
3. Improved design decisions: Two minds working together
produce cleaner, well-structured code.
4. Better adherence to coding standards: Promotes consistent
style and structure across the project.
5. Reduced defects: Early detection leads to fewer bugs in later
stages of testing.
2. Continuous Testing:
•   Definition:
In XP, tests are written before or alongside the code (Test-Driven
Development, or TDD), and executed continuously throughout the
development process.
• How it improves quality:
1. Immediate feedback: Developers know instantly if new code
breaks existing functionality.
2. Regression prevention: Continuous test execution ensures
stability after every code change.
3. Higher confidence in changes: Automated tests allow frequent
integration and refactoring.
4. Customer satisfaction: Frequent testing ensures software
continuously meets customer requirements.
5. Documentation through tests: Test cases serve as living
documentation for expected behavior.
3. Combined Impact on Quality:
•   Pair programming ensures better design and fewer coding errors,
while continuous testing ensures ongoing verification of system
behavior.
•   Together, they create a feedback-rich, defect-prevention environment,
resulting in robust, maintainable, and high-quality software.
********** 4 **********
--- page 5 ---
✅ In summary:
Extreme Programming integrates pair programming (collaborative
development) and continuous testing (early and repeated validation) to ensure
that software is reliable, flexible, and aligned with customer needs at every
stage of development.
CO-3;   b Evaluate the role of UML modeling in reducing development risk and   [10
propose how it can be integrated with agile methodologies for iterative
BL-M   M]
design validation.
Here’s a complete, detailed answer to your question:
Answer:
1. Role of UML Modeling in Reducing Development Risk:
1. Early Visualization of the System:
UML provides graphical models—like use case, class, and sequence
diagrams—that help teams visualize system architecture before
coding.
→ This reduces the risk of misunderstanding requirements and design
flaws.
2. Improved Communication:
UML serves as a common visual language among developers,
designers, and stakeholders.
→ It ensures clarity in understanding functionality and interactions,
reducing risks of misinterpretation.
3. Validation and Traceability:
Each UML diagram corresponds to a specific phase of SDLC
(requirements, design, testing).
→ This ensures traceability of requirements and early validation,
lowering the risk of rework.
4. Early Error Detection:
Visual modeling highlights inconsistencies, missing functionality, and
design bottlenecks before implementation, saving cost and time.
5. Facilitates Risk Management:
UML supports scenario modeling and “what-if” analysis, helping
identify critical components and potential failure points.
2. Integration of UML with Agile Methodologies for Iterative Design Validation:
1. Lightweight Modeling Approach:
Use UML diagrams selectively (e.g., use-case and class diagrams) in
agile sprints to represent evolving requirements without over-
documentation.
2. Continuous Design Refinement:
Update UML models incrementally as part of each sprint review to
reflect new or modified features.
→ Ensures design always aligns with current implementation.
********** 5 **********
--- page 6 ---
3. Model-Based Collaboration:
Integrate UML into Agile tools (like Jira, Enterprise Architect, or
Visual Paradigm) for real-time collaboration and visibility.
4. Executable Models and Test Alignment:
Combine UML behavioral diagrams (e.g., sequence/activity) with
automated test cases to validate system behavior iteratively.
5. Feedback Loop with Stakeholders:
Use UML visualizations during sprint demos to collect stakeholder
feedback quickly and reduce misunderstanding risk.
✅ In Summary:
UML modeling reduces development risk by improving clarity,
communication, and early validation of requirements and design.
When integrated into agile workflows through lightweight, iterative updates
and stakeholder feedback, it becomes a powerful tool for continuous design
validation and risk mitigation throughout the project lifecycle.
Q3   [20]
CO2 ,BL- a   [10
Analyze how human factors influence the success of agile projects and
H   M]
design a strategy to strengthen collaboration and trust within an agile team.
Here’s a detailed and well-structured answer to your question:
Answer:
1. Influence of Human Factors on Agile Project Success:
Agile methodologies—like Scrum or XP—depend heavily on people and
interactions rather than processes or tools. Therefore, human factors such as
motivation, trust, communication, and leadership play a crucial role in
determining the success of agile projects.
a) Communication and Collaboration:
•   Effective, open communication ensures that requirements, progress,
and challenges are clearly shared within the team.
• Miscommunication leads to misunderstanding of user stories, poor
sprint outcomes, and reduced team efficiency.
b) Trust and Psychological Safety:
• Team members must feel safe to express opinions, admit mistakes,
and share new ideas.
• Lack of trust discourages feedback, innovation, and ownership of
work.
c) Motivation and Empowerment:
• Agile emphasizes self-organizing teams where members take
ownership of tasks.
• Motivation drives creativity and continuous improvement; low morale
leads to missed deadlines and poor product quality.
********** 6 **********
--- page 7 ---
d) Leadership and Support:
• Servant leadership in agile helps facilitate the team rather than control
it.
•   Effective leaders remove impediments, encourage participation, and
recognize individual contributions.
e) Cultural and Emotional Intelligence:
• Understanding cultural differences and emotional cues ensures better
team cohesion, especially in distributed teams.
• Emotional intelligence fosters empathy and smoother conflict
resolution.
2. Strategy to Strengthen Collaboration and Trust in Agile Teams:
A structured approach to enhancing teamwork, trust, and shared ownership
can significantly improve agile outcomes.
a) Establish Clear Communication Channels:
• Use daily stand-ups, retrospectives, and sprint reviews to maintain
transparency.
• Encourage face-to-face or video interactions to build personal
connection and clarity.
b) Foster Psychological Safety:
• Create an environment where mistakes are viewed as learning
opportunities.
• Encourage open dialogue and constructive criticism during
retrospectives.
c) Build Shared Ownership and Accountability:
• Define clear sprint goals and assign responsibilities collectively.
•   Celebrate collective success rather than individual achievements to
reinforce teamwork.
d) Encourage Pair Programming and Peer Reviews:
•   Collaborative coding improves code quality, enhances learning, and
increases trust between developers.
e) Continuous Feedback and Recognition:
• Provide timely feedback during sprint reviews.
• Recognize contributions publicly to boost morale and reinforce
positive behavior.
f) Invest in Team Building and Empathy Training:
********** 7 **********
--- page 8 ---
• Conduct workshops or informal activities to strengthen interpersonal
relationships.
• Train team members in emotional intelligence to improve cooperation
and conflict management.
✅ In Summary:
Human factors like trust, motivation, and communication directly influence
agile project success.
By promoting psychological safety, open communication, shared
accountability, and continuous feedback, organizations can cultivate an agile
culture built on collaboration, respect, and trust, ultimately leading to higher
productivity and team satisfaction.
CO-3;   b Design an activity diagram for booking an appointment at the   [10
dispensary, which includes the sequential steps of requesting an
BL-H   M]
appointment, checking availability, confirming a slot, generating a
token, and finally confirming the appointment, while also representing
the decision flow when a slot is unavailable and looping back to check
for another available slot before completion?
2 MARKS FOR EACH STEP
Q4   [20]
CO-2;   a   Illustrate how Sprint Planning and Daily Scrum meetings contribute to   [10
BL-M   incremental delivery and team synchronization.   M]
Here’s a clear and detailed explanation for your question:
Answer:
********** 8 **********
--- page 9 ---
In Agile Scrum, both Sprint Planning and Daily Scrum meetings are essential
ceremonies that ensure incremental delivery of the product and maintain team
synchronization throughout the development cycle.
1. Sprint Planning – Foundation for Incremental Delivery
Definition:
Sprint Planning is a meeting held at the beginning of each sprint to define
what work will be done and how it will be accomplished during that sprint.
Contribution to Incremental Delivery:
1. Defines Clear Sprint Goals:
The team collaborates with the Product Owner to set achievable sprint
objectives that represent a potentially shippable product increment.
2. Prioritization of Work:
User stories are selected from the Product Backlog based on business
value and team capacity, ensuring that high-value features are
delivered first.
3. Task Breakdown:
Each selected story is decomposed into smaller, manageable tasks.
This structure enables the team to complete and deliver working
software iteratively.
4. Commitment and Estimation:
The team estimates effort and commits to deliver a small, functional
increment within the sprint timebox (usually 2–4 weeks).
5. Transparency and Predictability:
The planning process aligns the entire team around what will be
delivered, enhancing visibility and accountability.
2. Daily Scrum – Engine for Team Synchronization
Definition:
The Daily Scrum (Stand-up) is a short, time-boxed (15-minute) meeting held
every day of the sprint where each team member discusses progress, plans,
and blockers.
Contribution to Team Synchronization:
1. Continuous Alignment:
Keeps all members informed about who is doing what, ensuring
coordinated progress toward the sprint goal.
2. Early Problem Detection:
Team members identify impediments or dependencies early so the
Scrum Master can resolve them promptly.
3. Adaptive Planning:
Daily updates allow the team to adjust priorities or reallocate tasks
based on current progress or new challenges.
********** 9 **********
--- page 10 ---
4. Accountability and Focus:
By sharing daily updates, members stay focused and accountable,
reducing duplication of work and improving productivity.
5. Enhanced Communication:
Promotes open collaboration and strengthens trust among team
members, particularly in cross-functional teams.
3. Combined Impact:
•   Sprint Planning sets the direction for incremental delivery.
• Daily Scrum maintains momentum and synchronization through
continuous feedback and alignment.
Together, they ensure that:
• Work remains on track.
• Increments are delivered regularly.
• The team remains cohesive, self-organized, and responsive to change.
✅ In Summary:
Sprint Planning defines the roadmap for each iteration, ensuring a focused
and achievable increment, while the Daily Scrum maintains alignment,
transparency, and adaptability among team members.
Together, they form the backbone of incremental delivery and continuous
team synchronization in Agile Scrum.
CO-3;   b Design the class diagram for Placement activity process. XYZ Institute of   [10
Technology conducts annual campus placements for final-year students across
BL-L   M]
Engineering and Management disciplines. The Placement Cell, in coordination
with faculty and student representatives, manages end-to-end activities from
company outreach to offer letter distribution.
Q5   [20]
CO-3;   a Design a labeled state transition model for following problem statement.   [10
“A food delivery company is developing an Online Food Delivery System to
BL-M   M]
manage the complete life cycle of a Food Order object. Each Food Order
********** 10 **********
--- page 11 ---
represents a customer’s request to purchase items from a restaurant. The
order passes through a sequence of states from creation until completion or
cancellation. When a customer requests an order, a new Food Order is
created. Once payment is made successfully, the order Confirmed. If the
payment fails, the order moves to the “Payment Failed” state, from which it
can either be retried or cancelled permanently. After confirmation, the order
is sent to the Restaurant, to Being Prepared. When preparation is completed,
the order moves to “Ready for Pickup.” At this stage, a Delivery Person is
assigned, and the order transitions to the “Out for Delivery”. If the delivery is
successful, the order marked as “Delivered”. However, if the customer rejects
the order or the delivery fails, it marks as “Returned” or “Cancelled”
respectively.
: 5 marks for state and 5 marks for labelled transition.
CO-2;   b Compare the effectiveness of continuing maintenance, re-engineering, and   [10
replacement strategies for legacy systems in terms of business risk, cost, and
BL-H   M]
long-term sustainability.
Here’s a comprehensive and structured answer to your question:
Answer:
Legacy systems are older software systems that remain in use because they
perform critical business functions. Organizations often face a strategic
decision between continuing maintenance, re-engineering, or replacing these
systems. Each strategy differs in its impact on business risk, cost, and long-
term sustainability.
1. Continuing Maintenance
********** 11 **********
--- page 12 ---
Definition:
Continuing maintenance means keeping the legacy system operational with
minimal updates or bug fixes, without major architectural changes.
Evaluation:
Aspect   Analysis
Moderate to High — Risk of system failure increases
Business Risk   over time due to obsolete technology and lack of vendor
support.
Low short-term cost (since changes are minimal), but
Cost   high long-term maintenance costs as patching becomes
complex.
Poor — Difficult to adapt to new technologies, security
Long-term
risks increase, and skilled manpower for old platforms
Sustainability
becomes scarce.
Conclusion:
Suitable when the system is stable, low-change, and still meets essential
business needs with minimal enhancement requirements.
2. Re-engineering
Definition:
Re-engineering involves analyzing, restructuring, and optimizing the existing
legacy system to improve maintainability, performance, and compatibility
without complete replacement.
Evaluation:
Aspect   Analysis
Medium — Controlled risk since business logic is
Business Risk   preserved; risk occurs mainly during migration or code
transformation.
Moderate — Requires investment in analysis, redesign,
Cost   and partial redevelopment. Cost is balanced by improved
efficiency.
Long-term   Good — Extends system life, reduces technical debt, and
Sustainability   allows integration with modern platforms.
Conclusion:
Effective when the legacy system has high business value but suffers from
technical inefficiencies or outdated architecture.
3. Replacement
********** 12 **********
--- page 13 ---
Definition:
Replacement involves developing or acquiring a completely new system to
substitute the legacy system and migrate essential data and processes.
Evaluation:
Aspect   Analysis
High — Risk of data loss, user resistance, and functional
Business Risk
gaps during transition to the new system.
Very High — Involves full system development,
Cost
training, data migration, and infrastructure setup.
Excellent — New technologies provide better scalability,
Long-term
integration, and security; supports future business
Sustainability
growth.
Conclusion:
Ideal when the legacy system’s maintenance cost exceeds its value or when
modernization is crucial for business competitiveness.
4. Comparative Summary
Business   Long-Term
Strategy   Cost   Suitability
Risk   Sustainability
Low
Continuing   Short-term
High   initially,   Poor
Maintenance   survival
high later
Balanced
Re-engineering Medium Moderate   Good
approach
Long-term
Replacement   High   Very High   Excellent
transformation
✅ In Summary:
• Continuing maintenance offers short-term cost savings but
grows risky and unsustainable.
• Re-engineering balances cost and risk, extending system life
while improving maintainability.
• Replacement demands high upfront investment but ensures
long-term sustainability and alignment with modern business
needs.
Hence, re-engineering is often the most practical and cost-effective strategy
for organizations that want modernization without the extreme risk or cost of
full system replacement.
Q6   [20]
********** 13 **********
--- page 14 ---
CO-2;   a Explain how a Level-0, Level-1, and Level-2 Data Flow Diagram (DFD) can   [10
be applied in the design of a Student Enrollment System. How do successive
BL-M   M]
levels increase the detail and functional decomposition of the process?
Level   Description   Detail Provided
Shows the system as a single
Level-0
process interacting with external Very high-level overview
(Context)
entities.
Breaks the system into core sub- Shows major functions and
Level-1
processes and data stores.   data relationships
Expands each sub-process into   Provides implementation-
Level-2
smaller, logical steps.   ready detail for design
CO-4;   b Evaluate how Efficiency, Maintainability, and Portability interrelate to   [10
determine overall software quality, and design a metric-based
BL-L   M]
evaluation framework to measure their combined impact
Efficiency, maintainability, and portability are interdependent attributes that
collectively determine software quality.
High efficiency ensures optimal performance, while maintainability allows
easy updates without degrading that performance.
Portability enhances system adaptability across platforms, influencing both
maintenance effort and efficiency.
Balancing these factors ensures sustainable performance and lower lifecycle
cost.
A metric-based framework can include CPU utilization, mean time to modify
(MTTM), and successful build rate across platforms to quantify overall
quality.
Q7   [20]
CO-3;   a Evaluate how adherence to Golden Rules and Interface Design Principles   [10
BL-H   (e.g., consistency, anticipation, focus) enhances usability and user   M]
satisfaction in modern web or mobile interfaces
Adherence to Golden Rules and Interface Design Principles ensures a
seamless, intuitive, and satisfying user experience.
Consistency in layout, icons, and navigation reduces cognitive load and helps
users predict behavior easily.
Anticipation enables systems to foresee user needs—like auto-suggestions or
shortcuts—reducing effort and frustration.
Focus and feedback guide user attention and confirm actions, improving
confidence and task completion speed.
Together, these principles enhance usability, minimize errors, and
significantly boost user satisfaction in modern interfaces.
********** 14 **********
--- page 15 ---
CO-4;   b Critically analyze how verification and validation complement each other in   [10
ensuring software reliability and propose an improved framework combining
BL-H   M]
both stages effectively
Verification and validation are complementary processes that together ensure
software reliability and quality assurance.
Verification checks whether the product is built correctly—through reviews,
inspections, and testing against specifications.
Validation ensures the right product is built—confirming it meets user needs
and real-world requirements.
Their integration minimizes defects, ensuring correctness and fitness for
purpose.
An improved framework combines early verification (static analysis, peer
reviews) with continuous validation (user testing, feedback loops) across all
SDLC phases, ensuring reliable, user-centered software delivery.
********** 15 **********
````

## 2024-25 · Final-Exam · Sem 2 · Answer key · paper 1a36b35e008c

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_02/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Software Engineering/ANS_Software Engineering(703IT0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Apr 2025
- Text: text (7 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester II(Exam Year: 2024-2025)
Subject: Software Engineering
Date: 28 Apr 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 7 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all, 5 questions to be attempted.
7. All questions carry equal marks.
Q1.   Answer briefly:   [20]
CO1 ; SO1;   a.   Explain the concept of Layered Technology in Software Engineering
BL2
• Software engineering is a fully layered technology.
• To develop a software, we need to go from one layer to another.
• All these layers are related to each other and each layer demands the
fulfillment of the previous layer.
The layered technology consists of:
1. Quality focus
2. Process
3. Methods
4. Tools
CO2 ; SO1;   b.   Discuss Process flow in Scrum with the help of neat diagram.
BL1
CO3 ;   c.   Discuss the elements of Analysis model in brief.
SO1 ;
********** 1 **********
--- page 2 ---
BL1
CO4 ; SO1;   d. How to draw Class Diagrams in UML? Give steps.
BL1
Q2.
CO1 ; SO1;   a.   What are Legacy Systems? Discuss typical components of Legacy Systems. [10]
BL2
• Legacy systems: old computer-based systems still in use by
organizations
•   Typical logical parts of a legacy system are:
• System hardware
• Support software
•   Application software (legacy software systems)
•   Application data
•   Business processes
•   Business policies and rules
Embeds
knowledge of
Uses
Support   Application   Business policies
software   software   and rules
Runs-on   Runs-on   Uses   Uses   Constrains
System   Application   Business
hardware   data   processes
CO2 ; SO2;   b.   What is Capability Maturity Model Integration? Discuss it’s different   [10]
BL3   Levels with neat diagram.
• CMMI (Capability Maturity Model Integration) is a proven
industry framework to improve product quality and development
efficiency for both hardware and software
• Many companies have been involved in CMMI definition
such as Motorola and Ericsson
• CMMI has been established as a model to improve business
results
• CMMI, staged, uses 5 levels to describe the maturity of the
organization, same as predecessor CMM
•   Vastly improved version of the CMM
********** 2 **********
--- page 3 ---
• Emphasis on business needs, integration and
institutionalization
Q3.
CO2 ; SO2;   a.   Explain Incremental process model with following details:   [10]
BL1   • Process Model with diagram
• When do we use it?
• Advantages
• Disadvantages
When we use the Incremental Model?
When the requirements are superior.
A project has a lengthy development schedule.
When Software team are not very well skilled or trained.
When the customer demands a quick release of the product.
You can develop prioritized requirements first.
Advantage of Incremental Model
-Errors are easy to be recognized.
-Easier to test and debug
-More flexible.
-Simple to manage risk because it handled during its iteration.
-The Client gets important functionality early.
Disadvantage of Incremental Model
-Need for good planning
********** 3 **********
--- page 4 ---
-Total Cost is high.
-Well defined module interfaces are needed
CO1 ; SO1;   b.   State the importance of architecture. Discuss any two architectural styles   [10]
BL2   with advantages and limitations.
Representations of software architecture are an enabler for communication
between all parties (stakeholders) interested in the development of a
computer-based system.
The architecture highlights early design decisions that will have a
profound impact on all software engineering work that follows and, as
important, on the ultimate success of the system as an operational entity.
Architecture “constitutes a relatively small, intellectually graspable model
of how the system is structured and how its components work together”
[BAS03].
Q4.
CO2 ; SO1;   a.   What is the criterion for selection of a software process model? As the   [10]
BL1   project manager, which software development lifecycle model would you
choose for the given scenario? Justify your choice.
********** 4 **********
--- page 5 ---
XYZ is a multinational tech firm currently developing a groundbreaking
product for a client. The product is unlike anything the development team
has worked on before, and the client is unclear about the exact
requirements, leading to communication issues. As a result, the company
is facing challenges in fully understanding the user's needs. To resolve
this, the team has decided to create a sample application of the product to
present to the client for feedback.
Selection Criteria:
-The nature of the project and application.
-The methods and tools to be used.
-The controls (rules)and deliverables(documents, features) that are
required.
CO1 ; SO2;   b.   State the importance of User Interface Design. Explain UI design   [10]
BL2   principles and design issues.
User interface design creates an effective communication medium
between a human and a computer.
User interface design begins with the identification of user, task,
and environmental requirements. Once user tasks have been
identified, user scenarios are created and analyzed to define a set of
interface objects and actions.
These form the basis for the creation of screen layouts that depict
graphical design and placement of icons, definition of descriptive
screen text and specification of major and minor menu items.
Tools are used to prototype and ultimately implement the design
model, and the result is evaluated for quality.
design principles to help the designers.
◼ Place the user in control
◼ Reduce the user’s memory load
◼ Make the interface consistent
Issues
◼ Response time( length, variability)
◼ Help facilities
◼ Error handling
◼ Menu and command labeling
◼ Application accessibility
◼ Internationalization
Q5.
CO4 ; SO2;   a.   Explain the role of Validation testing. Discuss its types in detail.   [10]
BL4
(Testing 4m+ types 6m)
“ Validation testing focuses on user-visible actions and
user-recognizable output from the system.”
CO1 ; SO1;   b. Why to use Sequence Diagrams? Draw a sequence diagram for the   [10]
BL2   following flow of events in a use case:
1. A manager plans a team meeting and notifies the team members of
the meeting time and agenda.
2. The manager prepares the presentation materials and prints them
using the office printer (OfficeP) to provide copies for all
attendees.
********** 5 **********
--- page 6 ---
3. The manager distributes the presentation materials to the team
members at the meeting location.
4. During the meeting, the team members ask questions and discuss
the presentation.
5. After the meeting, the team members submit their feedback to the
manager.
6. The manager reviews the feedback and shares a summary with the
team.
(Why use Sequence Diagrams 4m+ diagram 6m)
Q6.
CO3 ;   a.   Explain Flow oriented Modeling in detail with suitable examples.   [10]
SO2 ;
BL4
CO2 ; SO1;   b. Why are Activity diagrams important? Design an activity diagram for a   [10]
BL1   library book borrowing system, showing activities such as searching for a
book, checking availability, issuing the book, and returning it.
(Importance 4m + diagram 6m)
Activity diagram helps to describe the flow of control of the target system,
such as the exploring complex business rules and operations, describing
the use case also the business process. It is object-oriented equivalent of
flow charts and data-flow diagrams (DFDs).
Useful to specify software or hardware system behaviour
Based on data flow models – a graphical representation (with a Directed
Graph) of how data move around an information system
Q7.
CO2 ; SO2;   a.   Summarize the steps in drawing Class Diagrams. Create a class diagram   [10]
BL2   for an Online Shopping System with classes like Customer, Product,
Order, and Payment. Include attributes, methods, and the relationships
between the classes.
(Steps 4m+ diagram 6m)
CO4 ;   b.   Describe Process and Project Metrics for Software Quality.   [10]
SO2 ;   Process
BL4   Quality-related
focus on quality of work products and deliverables
Productivity-related
Production of work-products related to effort expended
Statistical SQA data
error categorization & analysis
Defect removal efficiency
propagation of errors from process activity to activity
Reuse data
The number of components produced and their degree of reusability
Project
◼ used to minimize the development schedule by making the
adjustments necessary to avoid delays and mitigate potential
problems and risks
◼ used to assess product quality on an ongoing basis and, when
necessary, modify the technical approach to improve quality.
◼ every project should measure:
◼ inputs—measures of the resources (e.g., people, tools)
required to do the work.
********** 6 **********
--- page 7 ---
◼ outputs—measures of the deliverables or work products
created during the software engineering process and their
effectiveness.
********** 7 **********
````

## 2024-25 · Final-Exam · Sem 5 · Answer key · paper ccbb2e9c0dd7

- Departments: Computer Engineering, Cyber Security, Data Science, Information Technology
- Programmes: BTech Computer 7002, BTech CSE DS 7057, BTech CyberSecurity 7010, MBATech Computer 7047, MBATech IT 7041
- Source: `02_Question_Papers/2024/Sem_05/Final-Exam/BTech_Computer_7002/Software Engineering/ANS_Software Engineering(702IT0C016)_2024-2025.pdf` (+5 identical copies)
- Text: mixed (17 pages), mean OCR confidence 84.0

````text
Note: The provided synoptic answer attempts to cover content from standard textbooks and
reference materials that closely align with the context of the question.
--- page 2 ---
Q1
[20]
a   Explain challenges in maintaining Legacy software.
Maintaining legacy software poses several significant challenges:
Outdated Technology: Old programming languages, tools, and platforms
make upgrades and integration with modern systems difficult.
Lack of Documentation: Incomplete or missing documentation hampers
[5 M]
understanding of system logic and dependencies.
CO-1;   1
Scarcity of Skilled Personnel: Few developers are familiar with obsolete
BL-L   marks
technologies, increasing maintenance cost and effort.
each
High Technical Debt: Frequent patches and quick fixes over time make the
codebase complex and error-prone.
Integration and Security Issues: Legacy systems often struggle to interface
with modern applications and lack up-to-date security mechanisms.
b Compare the Incremental and RAD models in terms of development speed,
modularity, and project size suitability.
5 clear points needs to be addressed
Development Speed: RAD (Rapid Application Development) is faster due to
prototyping and parallel component development, while Incremental
Model progresses in fixed sequential increments.
Modularity: Both are modular, but RAD emphasizes reusable components
and visual tools for rapid assembly, whereas Incremental focuses on   [5 M]
CO-
functional modules built in planned stages.   1
2,BL-
User Involvement: RAD involves high user interaction and feedback at   marks
L
every iteration, while Incremental has limited user involvement after   each
requirement finalization.
Project Size Suitability: RAD suits small to medium projects requiring
quick delivery; Incremental suits medium to large projects with well-defined
requirements.
Flexibility and Risk: RAD offers high flexibility but may lack control in large
systems; Incremental provides better risk management and stable progress
through phased delivery.
c What are the different types of relationships used in class diagrams? Explain
with suitable examples.
[5 M]
CO-3;   types of relationships in UML class diagrams are fundamental elements   1
BL-L   that define how classes and objects interact with one another within an   marks
object-oriented system. The main relationship types are:   each
Association:
Represents a structural connection between two classes showing how
instances of one class are linked to instances of another.
--- page 3 ---
Example: A “Teacher” class associated with a “Student” class indicates that
teachers teach students.
Aggregation:
A special type of association representing a “whole-part” relationship
where the contained object can exist independently of the container.
Example: A “Department” class aggregates multiple “Teacher” objects—
teachers can still exist even if the department is removed.
Composition:
A stronger form of aggregation where the lifetime of the contained object
depends on the container.
Example: A “House” class composed of “Room” objects—if the house is
destroyed, its rooms cease to exist.
Inheritance (Generalization):
Defines an “is-a” relationship where a subclass inherits properties and
behavior from a superclass.
Example: A “Car” class inheriting from a general “Vehicle” class.
Dependency:
Indicates that one class depends on another for its behavior or data;
typically short-lived or temporary.
Example: A “ReportGenerator” class depends on a “DatabaseConnection”
class to retrieve data.
These relationships together define the structural and behavioural
connections between components in an object-oriented system, ensuring
clear modularity and interaction mapping during system design.
d   Explain Unit testing with suitable example.
Unit Testing is the process of testing individual components or modules of a
software system in isolation to ensure that each unit performs as designed.
unit testing focuses on verifying module interfaces, local data structures,
boundary conditions, independent paths, and error-handling mechanisms.
It is usually performed by the developer during the coding phase. Stubs and
drivers are used to simulate interactions between modules, creating a
controlled test environment.
CO-4;   [5 M]
Example:- 2 marks
BL-L   3+2
Consider a function calculateTotal() in a billing application that sums item
prices and applies tax. A unit test for this function would input a known set
of prices and tax rate, then verify that the output matches the expected
total.
In summary, unit testing ensures the correctness of each individual
software component before integration, preventing error propagation and
reducing debugging effort later in development.
Q2   [20]
a   Describe the main phases of the Waterfall Model and explain why it is
considered a prescriptive process model.
ANS- as per standard text book,
CO-1;   Main Phases of the Waterfall Model: (6 marks)   [10 M]
BL-L   Communication   6+4
(Project initiation and requirements gathering)
The development process begins with interaction between the customer
and the development team.
--- page 4 ---
All functional and non-functional requirements are identified and
documented before moving forward.
Planning
(Estimating, scheduling, and tracking)
Project plans are created, including cost estimation, resource allocation,
and timelines.
Risks are identified and managed at this stage.
Modeling
(Analysis and design)
Requirements are analyzed and transformed into system and software
design models.
This includes architectural design and detailed component design.
Construction
(Coding and testing)
The actual software is developed based on the design models.
Unit testing and integration testing are performed to verify correctness.
Deployment
(Delivery, support, and feedback)
The completed software is delivered to the customer.
User feedback is collected, and maintenance or support activities are
carried out.
The Waterfall Model is one of the earliest and most structured software
development models. It follows a linear and sequential approach, where
progress flows steadily through a series of well-defined phases.
OR as per reference material –
Main Phases of the Waterfall Model:
Requirements Analysis:
All system requirements are gathered and documented in detail. The focus
is on understanding what the system must do.
System Design:
Converts requirements into a blueprint for system architecture, data
structures, interfaces, and algorithms.
Implementation (Coding):
Developers translate the design into executable code using appropriate
programming languages and tools.
Testing:
The developed system is thoroughly tested for errors, performance, and
compliance with the requirements.
Deployment:
The tested software is delivered to the client or deployed into the
production environment.
Maintenance:
Post-deployment, the software undergoes maintenance activities like bug
fixes, updates, and performance improvements.
4 marks
Why It Is Considered a Prescriptive Process Model:
It prescribes a fixed set of process elements, including:
Framework activities
Tasks and actions
--- page 5 ---
Work products
Quality assurance checkpoints
Change control mechanisms
It enforces a predictable and well-defined process flow, where activities
must be completed in a specific order.
Each phase has clearly defined deliverables and documentation, leaving
little flexibility for revisiting earlier stages once a phase is completed.
Pressman states that prescriptive models are intended to bring order and
structure to software development by defining what must be done and
when during the project lifecycle.
The Waterfall Model is called prescriptive because it strictly defines and
enforces each phase, requiring that one phase be completed before the
next begins. It prescribes how the development process should proceed —
in a controlled, document-driven, and phase-wise manner.
This rigidity provides predictability, clarity, and traceability, which are
valuable in projects with stable, well-understood requirements but limits
flexibility for iterative or changing needs.
b   Design a labelled sequence diagram for following problem statement.
“A university is developing an Online Examination System to conduct digital
tests for students. When a student logs in through the Exam Portal UI, the
request is sent to the Exam Controller, which authenticates the student
using the student entity. Once authenticated, the Exam Controller retrieves
the exam details from the Exam entity and displays them to the student.
When the student starts the exam, the Exam Controller delivers one
question at a time by fetching it from the Question Bank entity. The student
submits answers through the Exam Portal UI, which are then passed to the
Exam Controller for storage in the Answer Sheet entity. After the student
completes the test and clicks “Submit,” the Exam Controller finalizes the
Answer Sheet and initiates the evaluation process.”
CO-3;
[10 M]
BL-M
5 marks for class and 5 marks for labelled transition.
--- page 6 ---
Q3   [20]
a
Define the three key roles in the Scrum framework and mention their core
responsibilities
Ans- as per standard text book-
1. Product Owner—3 MARK
Definition:
The Product Owner represents the customer and stakeholders and is
responsible for maximizing the value of the product.
Core Responsibilities:
Defines and clearly communicates product requirements
Creates, maintains, and prioritizes the Product Backlog
Ensures backlog items are well understood by the team
Accepts or rejects completed work based on business value
2. Scrum Master- 3 MARK
Definition:
The Scrum Master is a facilitator and coach who ensures that Scrum
principles and practices are properly followed.
Core Responsibilities:
Facilitates Scrum events (Sprint Planning, Daily Scrum, Sprint Review,
Retrospective)
Removes impediments that block the team’s progress
Coaches the team in Agile and Scrum practices
Protects the team from external interruptions
CO2   [10 M]
Ensures continuous improvement of the Scrum process
,BL-H   3. Development Team – 4 MARK   3+3+4
Definition:
The Development Team consists of professionals who build and deliver the
product increment.
Core Responsibilities:
Designs, develops, tests, and integrates product features
Delivers a potentially shippable increment at the end of each sprint
Self-organizes to decide how work is done
Estimates tasks and commits to sprint goals
Ensures product quality through continuous testing and integration
OR as per reference material
Definition & Responsibilities:
Represents the customer and business interests
Creates and maintains the Product Backlog, which is a prioritized list of
features that deliver business value
Assesses the backlog and updates priorities as required
Ensures that requirements reflect customer needs and business value
In the Scrum framework, three key roles form the foundation of an agile
development team. Each has distinct responsibilities that ensure smooth
project execution and product delivery.
1. Product Owner (PO):
--- page 7 ---
Core Responsibility: Represents the voice of the customer and defines the
product vision.
Key Duties:
Create and maintain the Product Backlog with prioritized user stories.
Ensure that the team works on features that deliver the highest business
value.
Clarify requirements and accept completed work that meets the Definition
of Done (DoD).
2. Scrum Master (SM):
Core Responsibility: Acts as a facilitator and coach for the Scrum team.
Key Duties:
Ensure Scrum principles and practices are properly followed.
Remove impediments or blockers affecting team progress.
Foster communication, collaboration, and continuous improvement within
the team.
Shield the team from external distractions and scope creep.
3. Development Team (Dev Team):
Core Responsibility: Responsible for delivering potentially shippable
product increments at the end of each sprint.
Key Duties:
Self-organize to plan and execute sprint work.
Collaborate daily to design, develop, test, and integrate features.
Maintain product quality through coding standards and testing.
Participate actively in sprint planning, reviews, and retrospectives.
b   Critically evaluate the importance of UML in bridging the gap between
Object-Oriented Analysis (OOA) and Object-Oriented Design (OOD).
Provide an example showing how a conceptual model transition into
specific UML diagrams.
Bridging Conceptual and Design Phases: UML provides a standard visual
language that connects Object-Oriented Analysis (understanding
requirements) with Object-Oriented Design (defining structure and
behavior).
Unified Representation: It translates conceptual models (like classes,
[10 M]
relationships, and interactions) into concrete design elements, ensuring
CO-3;   2
clarity between analysts and developers.
BL-H   marks
Improved Traceability: UML maintains consistency from high-level
each
requirements to low-level implementation by mapping use cases to class
and sequence diagrams.
Facilitates Design Validation: UML diagrams help verify that design
elements faithfully represent the analyzed business logic and system
behavior before coding.
Example: In a Library Management System, the OOA identifies entities like
Book, Member, and Librarian; these transition into UML Class Diagrams
showing relationships (association, inheritance) and Sequence Diagrams
depicting interactions like issueBook() or returnBook() during OOD.
--- page 8 ---
Q4   [20]
a   "Requirements Engineering is not just about documenting what users want,
but about balancing conflicting needs, resolving ambiguities, and ensuring
feasibility."
In light of this statement, critically discuss the role of Requirements
Engineering in the success of a software project.
Answer:
Requirements Engineering (RE) plays a critical role in determining the
success or failure of a software project. It goes far beyond simple
documentation—it ensures that the developed system truly meets business
objectives, user expectations, and technical feasibility.
Elicitation and Understanding of Needs:
RE involves gathering diverse stakeholder needs through interviews,
workshops, and observations. This helps uncover explicit and implicit
requirements, ensuring that no essential functionality is overlooked.
Conflict Resolution and Prioritization:   [10 M]
CO-2;   Stakeholders often have conflicting goals—for example, marketing   2
BL-M   demands more features while developers prefer simplicity. RE balances   marks
these competing interests through negotiation and prioritization to achieve   each
realistic, value-driven outcomes.
Clarifying Ambiguities:
Ambiguous requirements lead to misinterpretation and costly rework.
Through techniques like prototyping and use-case modeling, RE ensures
that requirements are clear, consistent, and testable.
Feasibility and Risk Management:
RE assesses technical, financial, and operational feasibility before design
begins. Early validation of requirements prevents resource wastage on
impractical solutions.
Foundation for Design, Development, and Testing:
Well-engineered requirements form the baseline for all subsequent SDLC
phases—they guide design decisions, implementation priorities, and test
case development, ensuring traceability and alignment with user goals.
b   Explain how a Level-0, Level-1, and Level-2 Data Flow Diagram (DFD) can be
applied in the design of a Student Enrollment System. How do successive
[10 M]
levels increase the detail and functional decomposition of the process?
CO-3;   2
BL-L   marks
each
Answer:
--- page 9 ---
LEVEL 0: CONTEXT DIAGRAM

Student | —~\ i Admin |

0.0

Student

Enrollment
System

Application Details
ad Enrollment Reports

Application
Submssion

Confirmation «~ nx Invoices

Message
Payment Details
Finance
Student Department |
--- page 10 ---
LEVEL 1: SYSTEM OVERVIEW

Student ay Vd Admin

1.0
Raw Application —>| Application

Submission

2.0
Application
Submission

Application Details
Enrollment Reports

0.0

Student
Enrollment
System

D1 Student

Database eat —~__,.

Eligibility Check
Request

40 <7 \ |
Enrolloment Lee <= Invoices

3.0
Eligibility
Verification

Confirmation

y

Finance

Student Department
--- page 11 ---
Level-0 DFD (Context Diagram): 2 MARKS
Represents the entire Student Enrollment System as a single process
interacting with external entities like Student, Admin, and Finance
Department.
Data flows include application submission, payment details, and
confirmation messages.
Level-1 DFD: 2 MARKS
Decomposes the main system into major sub-processes, such as Application
Submission, Eligibility Verification, Fee Payment, and Enrollment
Confirmation.
Introduces data stores like Student Database and Course Catalog to show
internal data flow.
Level-2 DFD: 2 MARKS
Provides detailed decomposition of Level-1 processes.
For example, Eligibility Verification can be split into Document Check,
Prerequisite Validation, and Seat Availability Check.
Similarly, Fee Payment can include Invoice Generation, Payment
Verification, and Receipt Issuance.
Successive Level Detailing: 2 MARKS
Each level adds more functional detail and data flow clarity, breaking down
complex processes into smaller, manageable tasks.
Functional Decomposition Benefit: 2 MARKS
--- page 12 ---
This hierarchical refinement ensures better understanding, simplifies
design, and helps developers and analysts verify that all system functions
are captured and logically connected before implementation.
Q5   [20]
a   Analyze the influence of data mining and data warehousing on architectural
decisions in large-scale information systems. How do these concepts guide
database design at both the architectural and component levels?
Answer:
1. Role of Data Mining and Data Warehousing in System Architecture:
Data warehousing and data mining profoundly shape the architectural
decisions of large-scale information systems.
Data Warehousing focuses on the collection, integration, and storage of
large volumes of historical and transactional data for analysis and decision-
making.
Data Mining applies analytical techniques on this data to discover hidden
patterns, trends, and correlations, supporting strategic business
intelligence.------------- 2 MARKS
2. Influence on Architectural Decisions: 4 MARKS
Separation of Operational and Analytical Workloads:
Architectural design must distinguish between OLTP (Online Transaction
Processing) systems handling daily transactions and OLAP (Online
Analytical Processing) systems for analysis.
→ This separation ensures performance optimization and prevents
analytical queries from burdening live systems.
CO-3;   [10 M]
Layered and Modular Architecture:
BL-M   2+4+4
Large-scale systems adopt multi-layered architectures—data acquisition,
ETL (Extract-Transform-Load), storage, and presentation layers—to support
data warehousing and mining effectively.
→ Enables scalability, maintainability, and easy integration of analytical
tools.
Data Integration and Consistency:
Architectural choices emphasize data normalization, cleansing, and
transformation to ensure consistent, high-quality data across distributed
sources before storage in the warehouse.
3. : 4 MARKS
Influence on Database Design (Architectural LevelSchema Design (Star and
Snowflake Models):
Data warehouses use dimensional modeling to structure data into fact and
dimension tables for efficient querying and reporting.
→ Example: Fact table stores sales data; dimension tables store customer,
product, and time details.
Data Storage Optimization:
Large-scale systems use denormalization, indexing, and partitioning to
speed up analytical queries on massive datasets.
→ Improves performance for data mining operations.
--- page 13 ---
Metadata Management:
Metadata repositories become a crucial architectural element for managing
data lineage, transformations, and schema evolution.
Influence on Database Design (Component Level):
ETL Components:
Design includes robust ETL pipelines that extract raw data, clean it, and load
it into the warehouse—supporting accurate data mining.
Data Staging and Aggregation:
Intermediate staging areas and data marts are introduced to handle pre-
processing, aggregation, and summary generation efficiently.
Data Mining Integration:
Embedding mining algorithms (e.g., clustering, classification, association
rules) within the architecture guides the choice of indexing methods, data
partitioning, and computational resources.
Overall Impact:
Data warehousing ensures data availability, reliability, and performance
for analytics.
Data mining drives intelligent architectural designs that support predictive
modeling and decision support systems.
Together, they transform traditional databases into knowledge-driven,
scalable architectures capable of supporting real-time analytics and
business intelligence.
b Compare Agile and plan-driven approaches in terms of specification
and delivery, and justify situations where Agile is more effective.
Specification Approach:
Plan-driven: Requirements are fully defined upfront before development
begins.
Agile: Requirements evolve through continuous user feedback and iterative
refinement.
Delivery Cycle:
Plan-driven: Delivers the complete system at the end of the project.
Agile: Delivers working software in short, incremental iterations.
[10 M]
Flexibility to Change:
CO-2;   2
Plan-driven: Limited flexibility—changes are costly once development
BL-H   marks
starts.
each
Agile: Highly adaptable—welcomes changing requirements even late in
development.
Customer Involvement:
Plan-driven: Involvement mainly during requirement and acceptance
stages.
Agile: Continuous customer collaboration throughout the project.
When Agile is More Effective:
Agile is ideal for dynamic environments with evolving requirements, rapid
market changes, or innovative projects where frequent feedback,
flexibility, and early delivery are critical to success.
Q6   [20]
--- page 14 ---
a   Describe the major features of the Scrum methodology and analyze the role
of backlog and sprint cycles in managing change
FROM TEXT BOOK-
Major Features of Scrum Methodology – 5 Marks
Scrum emphasizes the use of software process patterns that enable a team to
manage complex projects through an iterative approach. Its major features
include:
Small, Self-Organizing Teams: Scrum relies on small, highly motivated
project teams that are in control of their own work and foster heavy
collaboration.
Iterative Development: Work is partitioned into "packets" that are tackled
in short, fixed-duration cycles.
Minimal Work Products: The process focuses on delivering operational
software increments rather than comprehensive documentation.
Process Patterns: Scrum uses specific activities and roles to ensure
progress, such as:
Backlog: A prioritized list of project requirements or features that provide
business value for the customer.
Sprints: Work units consisting of a specific set of backlog items that must
be completed within a pre-defined time-box (typically 30 days).
Scrum Meetings: Short daily meetings (often 15 minutes) where the team
coordinates activities, assesses progress, and identifies obstacles.
Demos: Delivering the software increment to the customer so that
functionality can be demonstrated and evaluated.
CO-2;   [10 M]
Role of Backlog and Sprint Cycles in Managing Change – 5 marks
BL-M   5+5
Backlogs and sprint cycles are fundamental to Scrum’s ability to "embrace"
and manage change effectively during a project:
Dynamic Requirement Management (Backlog): The backlog is not a static
document; it is a prioritized list that can be updated as new requirements
emerge or business priorities shift. This allows the team to respond to change
rather than strictly following a rigid, initial plan.
Controlled Work Environments (Sprints): While the backlog is dynamic, the
sprint provides stability. Once a sprint begins, the items being worked on are
frozen; no changes are introduced until the next sprint cycle. This ensures
that the team can complete a functional increment without being disrupted by
constant mid-cycle "feature creep".
Continuous Feedback Loops: Because each sprint cycle ends with a demo
to the stakeholders, the team receives immediate feedback. This feedback
can then be used to update the backlog, ensuring that the next sprint cycle
incorporates any necessary changes or refinements requested by the
customer.
FROM Reference material -
1. Major Features of the Scrum Methodology: 5m
Iterative and Incremental Development:
Work is divided into short, time-boxed iterations called sprints (usually 2–4
weeks) to deliver working product increments frequently.
Defined Roles:
Scrum defines three primary roles — Product Owner (manages
--- page 15 ---
requirements), Scrum Master (facilitates the process), and Development
Team (builds the product).
Empirical Process Control:
Scrum relies on transparency, inspection, and adaptation to manage
progress and handle uncertainty effectively.
Regular Ceremonies:
Core events include Sprint Planning, Daily Scrum, Sprint Review, and
Retrospective to ensure communication, accountability, and continuous
improvement.
Working Software as Progress Measure:
Success is judged by the delivery of functional product increments, not by
documentation or percentage completion.
2. Role of Backlog and Sprint Cycles in Managing Change: 5m
Product Backlog – Dynamic Requirement Management:
The Product Backlog contains prioritized user stories and features. It
evolves continuously based on stakeholder feedback and changing business
needs. This flexibility ensures Scrum can quickly respond to changes.
Sprint Backlog – Short-Term Focus:
At the start of each sprint, the team selects items from the Product Backlog
to form a Sprint Backlog, focusing only on achievable goals for that sprint,
thus limiting change within the sprint duration.
Sprint Cycles – Iterative Adaptation:
After each sprint, reviews and retrospectives provide opportunities to
incorporate feedback and reprioritize work, adapting to new
requirements or market shifts.
Change Control through Timeboxing:
Changes are deferred to the next sprint, ensuring stability within the
current iteration while allowing adaptability between sprints.
Continuous Value Delivery:
By combining backlog refinement and iterative sprint cycles, Scrum allows
teams to deliver incremental value, adapt to evolving requirements, and
continuously align with customer expectations.
b   Discuss which ISO 9126 characteristic—efficiency, maintainability, or
portability—should be prioritized for government-grade cybersecurity
systems and justify your reasoning.
Answer
Prioritize: Maintainability — for government-grade cybersecurity systems,
the ability to rapidly patch, harden, and adapt to emerging threats
CO-4;   [10 M]
outweighs raw efficiency or broad portability.
BL-L   3+3+4
Why maintainability first
Rapid vulnerability response: High maintainability (clean modular design,
clear interfaces, strong CI/CD, IaC) enables fast patching and hotfix
rollout, shrinking exposure windows during zero-days and APT incidents.
Secure configuration at scale: Maintainable systems support policy-as-
code, repeatable hardening baselines, and auditable change control—core
to compliance (e.g., STIGs, CIS benchmarks).
--- page 16 ---
Lower defect density over time: Refactorable codebases and strong test
coverage reduce regression risk when introducing new crypto suites, auth
flows, or telemetry. -----3m
Where efficiency fits
Second priority: Crypto, packet processing, and analytics need predictable
latency and throughput (e.g., for real-time detection, deep packet
inspection). Optimize critical paths while preserving testability—avoid
“performance hacks” that erode clarity and security.
Where portability fits
Third priority (contextual): Useful for multi-domain deployments (on-
prem, air-gapped, sovereign clouds) and hardware refresh cycles. But
excessive abstraction for portability can increase attack surface and
operational complexity; keep it intentional (e.g., portable cryptographic
backends, OS-agnostic agents) without compromising maintainability.----3m
Practical rubric (prioritized controls)
Maintainability: MTTR for security patches, % code with unit/integration
tests, change-failure rate, config drift metrics.
Efficiency: P95 latency under load, CPU/memory per secured connection,
throughput with modern ciphers.
Portability: # of certified target platforms, build reproducibility,
dependency isolation (SBOM, container provenance). --- 4m
Q7   [20]
a   Design a labeled state transition diagram for following problem statement.
“A university library wants to automate the process of book lending through
a Library Management System. The system should manage the complete
life cycle of a BookCopy object (an individual copy of a book), tracking how
its state changes as it is issued, returned, or reserved by users. Initially,
every BookCopy in the library flagged as Available, meaning it can be
borrowed by any registered member. When a Member places a hold
request for a BookCopy, its marked as Reserved. While in this state, the
book cannot be borrowed by anyone else. If the member fails to collect the
book within the allowed reservation period(15 days), the system
automatically changes its state back to Available. When a reserved book is
collected or directly borrowed (without reservation), its flagged as Issued.
During this state, the system tracks the issue date and due date. If the
CO-3;
member returns the book on or before the due date, the state moves back   [10 M]
BL-H
to Available. However, if the member fails to return the book by the due
date, the system marks it as Overdue. Once an overdue book is returned,
the system calculates a fine, records payment, and changes its flag back to
Available.”
--- page 17 ---
5 marks for state, 5 marks for labelled message
b Judge whether adopting CMMI processes necessarily guarantees higher
software quality or whether contextual organizational factors play a greater
role—support your argument.
Here’s a critical evaluation-based answer:
Answer:
Adopting CMMI (Capability Maturity Model Integration) processes does
not automatically guarantee higher software quality. While CMMI
provides a structured framework for process improvement, the
organizational context, culture, and leadership commitment largely
determine its effectiveness.
Framework vs. Implementation Reality:
CMMI defines what to improve (process maturity) but not how to
implement it effectively. Without genuine adoption, it can become a   [10 M]
checklist exercise that adds bureaucracy rather than value.   2
CO-4;
Cultural and Human Factors:   marks
BL-H
Organizational culture—communication, collaboration, and learning—plays   each
a greater role. Teams that embrace continuous improvement and open   point
feedback achieve better quality, even with minimal formal structure.
Domain and Size Dependency:
In dynamic domains like startups or agile environments, rigid CMMI
processes may reduce responsiveness, while in large, regulated projects
(e.g., defense, aerospace), CMMI ensures consistency and compliance.
Leadership and Quality Mindset:
Success depends on management commitment to quality as a philosophy,
not just certification. Quality arises from empowering teams, not merely
following documented procedures.
Balanced Integration:
The best outcomes occur when CMMI is blended with adaptive practices
(like Agile) and tailored to organizational maturity—ensuring processes
remain flexible, efficient, and people-focused.
````

## 2024-25 · Re-Exam · Sem 2 · Answer key · paper e8c5b25a4f43

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2024/Sem_02/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Software Engineering/ANS_Software Engineering(703IT0C001)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2025
- Text: text (6 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 2 Re-exam(Exam Year: 2024-2025)
Subject: Software Engineering
Date: 01 Jul 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 6 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No. 1 is compulsory.
5. Out of remaining questions, attempt any 4 questions.
6. In all, 5 questions to be attempted.
7. All questions carry equal marks.
Q1.   Answer briefly:   [20]
a. Which are the five activities in a generic process framework for software
engineering? Discuss in brief.
Communication
• Planning
• Modeling
• Construction
• Deployment
b. Discuss the important features of Agile Tool Jira.
•   - It is used for bug tracking, issue tracking, and project management.
•   - JIRA is an incident managementtool.
•   - JIRA is a platform independent tool; it can be used with any OS.
•   - JIRA is multi-lingual tool −
English,French,German,Japanese,Spanish,etc.
•   - JIRA supports MySQL,Oracle, PostgreSQL and SQL server in the
backend.
•   - JIRA can be integrated with many other tools − Subversion,GIT,Clear
case, and many more
c.   Discuss the elements of Analysis model in brief.
********** 1 **********
--- page 2 ---
d. How to draw Use Case Diagrams in UML? Give steps.
Q2.
a. What are Legacy Systems? Discuss different approaches for assessment of Legacy [10]
Systems.
• Legacy systems: old computer-based systems still in use by organizations
• Assessment of legacy systems includes:
•   Business value assessment (subjective). Viewpoints:
•   End-users: look at system’s functionality and performance
• Customers: look at the quality of services provided
•   Business managers: assess the usefulness of the system in
terms of business support
• IT managers: are concerned with the availability of technical
support for the system
•   Senior managers: interested in system’s contribution to the
business goals
• System quality assessment
b. What is Agile model? When to use it? Discuss Advantages and Disadvantages of   [10]
Agile model.
Mostly used model in todays digital era.
• Agile means” The ability to respond to(continue) changes from
requirements, technology and people”
• It is an incremental and iterative process of software development.
When Project size is large
• When frequent changes are required.
• When a highly qualified and experienced team is available.
• When a customer is ready to have a meeting with a software team all
the time.(every iteration)
• Projects with flexible timeline and budget.
Advantages of Agile model
• Support customer involvement and customer satisfaction
• Strong communication of the software team with the customer’
• Little planning require(more focus on design and development)
********** 2 **********
--- page 3 ---
• Efficient design and fulfils the business requirement.
• Anytime changes are acceptable.
• Provides a very realistic(accurate) approach to software development
• Updated version of functioning software are released every week.
• it reduces total development time.
Disadvantages of Agile model
• Due to the lack of proper documentation (cant waste time on doc), once the
project completes and the developers allotted to another project , maintenance of
the finished project can become difficult.
• Depends heavily on customer interaction, so if customer is not clear, team can
be driven in the wrong direction.
Q3.
a.   Explain Spiral model with following details:   [10]
• Process Model with diagram
• When do we use it?
• Advantages
• Disadvantages
When to use Spiral model?
When the project is large and high budget.
When requirement are unclear and complex.
When changes may require at any time
When the software needs continuous risk evaluation
Advantages of Spiral Model
High amount of risk analysis.
Risky part can be developed earlier which help in better rik
management.
Useful for large and mission-critical project.
Allows extensive use of prototype(solve all error in prototype).
There is always a space for customer feedback.
Changing the requirement can be accommodated.
Development is fast
Disadvantages of Spiral Model
Risk analysis needed highly particular expertise.
Can be a costly model to use.
Doesn t work for smaller projects.
Spiral process is complex sometimes because spiral may be infinitely.
Large number of spiral stages required excessive documentation.
b. Discuss data centered and layered architectures with their advantages and   [10]
limitations.
********** 3 **********
--- page 4 ---
Q4.
a. What is the criterion for selection of a software process model? As the project   [10]
manager, which software development lifecycle model would you choose for the
given scenario? Justify your choice.
PQR is a global software development company working on a highly innovative
product for a client. This product is entirely new to both the development team
and the client, resulting in significant ambiguity about the project requirements.
The development team is struggling to accurately capture the client's needs. To
overcome this, the team plans to develop a preliminary version of the product and
seek feedback from the client.
Selection Criteria:
-The nature of the project and application.
-The methods and tools to be used.
-The controls (rules)and deliverables(documents, features) that are
required.
b.   State the importance of User Interface Design. Explain User Interface Design   [10]
Process with all necessary steps.
User interface design creates an effective communication medium
between a human and a computer.
User interface design begins with the identification of user, task,
and environmental requirements. Once user tasks have been
identified, user scenarios are created and analyzed to define a set of
********** 4 **********
--- page 5 ---
interface objects and actions.
These form the basis for the creation of screen layouts that depict
graphical design and placement of icons, definition of descriptive
screen text and specification of major and minor menu items.
Tools are used to prototype and ultimately implement the design
model, and the result is evaluated for quality.
User Interface Design Process
◼ Using information developed during interface analysis, define interface
objects and actions (operations).
◼ Define events (user actions) that will cause the state of the user interface
to change. Model this behavior.
◼ Depict each interface state as it will actually look to the end-user.
◼ Indicate how the user interprets the state of the system from information
provided through the interface.
◼ Use-case can be used to define interface objects and the actions that are
applied to them.
Q5.
a.   Explain the role of System testing. Discuss its types in detail.   [10]
(Testing 4m+ types 6m)
“ System testing is a series of different tests whose primary
purpose is to fully exercise the computer-based system and to
verify that system elements( hardware, people, information)
have been properly integrated and perform allocated
functions.”
b. Why to use Sequence Diagrams? Draw a sequence diagram for the following flow [10]
of events in a use case:
1. A library administrator announces the availability of new books and the
due date for book returns.
2. The administrator then prepares the list of new books and gets it printed
using the library printer (LibraryP) for distribution.
3. The administrator hands out the new books list to the library members at
the library desk.
4. The library members select and borrow the books.
5. The library members return the borrowed books before the due date.
6. The administrator checks the returned books and updates the library
records.
(Why use Sequence Diagrams 4m+ diagram 6m)
Q6.
********** 5 **********
--- page 6 ---
a.   Explain Requirement Engineering tasks in detail.   [10]
b. Why are Activity diagrams important? Design an activity diagram to represent   [10]
the process of booking a ticket on an airline reservation system.
(Importance 4m + diagram 6m)
Activity diagram helps to describe the flow of control of the target system, such
as the exploring complex business rules and operations, describing the use case
also the business process. It is object-oriented equivalent of flow charts and data-
flow diagrams (DFDs).
Useful to specify software or hardware system behaviour
Based on data flow models – a graphical representation (with a Directed Graph)
of how data move around an information system
Q7.
a. Summarize the steps in drawing Class Diagrams. Create a class diagram for a   [10]
Hotel Reservation System with classes like Guest, Room, Reservation, and
Payment. Include attributes, methods, and the relationships between the classes.
(Steps 4m+ diagram 6m)
b. Discuss Function-based metrics for Software Quality. How to compute Function   [10]
points?
◼ Function-based metrics:- use the function point as a normalizing factor or
as a measure of the functionality delivered, cost incurred, errors and
number of components in the resultant system
◼ Function points are derived using an empirical relationship based on
countable (direct) measures of software's information domain and
assessments of software complexity
◼ Information domain values are defined in the following manner:
◼ Number of external inputs (EIs)- originates from user or another
application
◼ Number of external outputs (EOs)- derived within the
application
◼ Number of external inquiries (EQs)- input that generate
immediate software response
◼ Number of internal logical files (ILFs)- logical grouping of data,
residing within application boundary and maintained by external
inputs.
◼ Number of external interface files (EIFs)-resides external but
provides data that maybe of use to the application
◼ FP = count total * [ 0.65 + 0.01 *∑( F( i))]
◼ F( i) with i=1 to 14 are value adjustment factors for a given set of
questions. The answers can range from
◼   0( not important ) to 5( absolutely essential)
◼ Based on the FP value, managers can estimate the overall size and can
do effective planning.
********** 6 **********
````
