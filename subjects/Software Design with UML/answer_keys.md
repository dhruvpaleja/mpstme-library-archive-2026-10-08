# Software Design with UML: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 6 · Answer key · paper f9b418cd8935

- Departments: Computer Science and Business Systems
- Programmes: BTech CSBS 7036
- Source: `02_Question_Papers/2025/Sem_06/Final-Exam/BTech_CSBS_7036/Software Design with UML/ANS_Software Design with UML(702CO0C018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 04 May 2026
- Text: text (4 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY (COMPUTER SCIENCE AND BUSINESS
SYSTEMS)
Year: III/Semester VI(Exam Year: 2025-2026)
Subject: Software Design with UML
Date: 04 May 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 4 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question No.1 is compulsory
5. Out of remaining questions, attempt any 4 questions
6. In all 5 questions to be attempted
7. Assume suitable data if necessary
Q1   Answer briefly:   [20]
a)   Differentiate between process and thread. What is thread lifecycle?
A process is an independent program in execution with its own memory
space, whereas a thread is a lightweight unit of execution within a process
that shares memory and resources with other threads. Processes are heavier,
slower to create, and communicate using complex mechanisms, while
Chap 9,   threads are faster and enable efficient multitasking within the same   [5]
CO4,SO2,BL2
application. The thread lifecycle consists of stages: New (created), Runnable
(ready to run), Running (executing), Blocked/Waiting (paused for resources
or events), and Terminated (execution finished), transitioning between these
states until completion.
b)   What is design pattern. What problem does the Singleton pattern solve?
A design pattern is a reusable, proven solution to common software design
problems that helps developers write efficient, maintainable, and scalable
Chap2,CO2,SO2,BL3   code. The Singleton pattern solves the problem of ensuring that a class has   [5]
only one instance throughout the application while providing a global access
point to it. This is useful in situations like configuration settings, logging, or
database connections, where multiple instances could lead to inconsistency
or resource conflicts.
c)   What is the key difference between Aggregation and Composition? Explain
with real time example.
The key difference between aggregation and composition lies in ownership
and lifecycle dependency. In aggregation, objects have a “has-a” relationship
Chap5,   but can exist independently—for example, a Department and Professors:   [5]
CO3,SO2,BL2   professors can exist even if the department is removed. In composition, there
is a strong ownership where the child object cannot exist without the
parent—for example, a House and its Rooms: if the house is destroyed, the
rooms cease to exist. Thus, aggregation represents a weak relationship, while
composition represents a strong, dependent relationship.
d)   Explain the Software Crisis in detail and how modern methodologies solve   [5]
Chap1,CO1,SO2,BL2
it.
********** 1 **********
--- page 2 ---
The software crisis refers to the difficulties faced in the early days of
software development, especially during the 1960s–70s, when projects
frequently exceeded budgets, missed deadlines, and produced unreliable or
hard-to-maintain systems due to increasing complexity and lack of structured
practices. Problems included poor quality, unclear requirements, and
inefficient development processes. Modern methodologies like Agile,
Scrum, and DevOps address these issues by promoting iterative
development, continuous feedback, better project management, automated
testing, and collaboration, ensuring faster delivery, improved quality, and
adaptability to changing requirements.
Q2   [20]
a)   What are the key features of the Spiral Model? For railway reservation
system which process model is suitable and why?
Chap1,CO1;SO2,BL3   The Spiral Model combines iterative development with systematic risk   [10]
analysis. Its key features include risk assessment at every phase, iterative
cycles (spirals), customer feedback at each stage, and progressive
refinement of the system. It is especially suitable for large, complex, and
high-risk projects where requirements may evolve.
b)   Explain the Characteristics of Object-Oriented Systems. Also discuss the
advantage of OOSAD.
Chap2,CO1;SO2,BL2   Object-Oriented Systems are characterized by encapsulation (data hiding),   [10]
inheritance (code reuse), polymorphism (multiple behaviors), and
abstraction (hiding complexity). They model real-world entities as objects,
making systems more modular and easier to manage.
Q3   [20]
a).   Explain how use case diagrams capture functional requirements with an
Chap3,   example of hospital management system.   [10]
CO2;SO2,BL3
Neat diagram is required.
b)   In an embedded system like a washing machine, a state diagram shows
different operational states and transitions based on events. Students are
Chap7,   expected to clearly identify and label these states and show transitions [10]
CO3;SO2,BL3   triggered by events such as button press, water level detection, and timer
completion.
Neat state diagram is required.
Q4   [20]
a)   What are combined fragments in sequence diagram. Explain loop, alt and
opt type of fragments.
Combined fragments in a UML sequence diagram are used to represent
control logic such as conditions, loops, and alternatives within interactions
Chap4,CO3;SO6,   between objects. They help model complex behaviors like decision-making   [10]
BL3   and repetition in a clear and structured way.
• Loop fragment: Represents repetition of a sequence of messages as
long as a condition is true (e.g., retrying payment until success).
•   Alt (Alternative) fragment: Represents conditional branching (like
if-else), where only one path is executed based on a condition (e.g.,
payment success vs failure).
********** 2 **********
--- page 3 ---
• Opt (Optional) fragment: Represents a single optional path that
executes only if a condition is true (like an if statement without
else, e.g., applying a discount if eligible).
b)   Design swimlane diagram for the case study on “ hospital management
Chap7,CO3;SO2,BL4   system”   [10]
Neat Diagram is required.
Q5   [20]
a)   Explain the transition from analysis to design with suitable diagram.
Chap4, CO3, SO2,   [10]
BL3
b)   Explain aggregation, composition, realization and inheritance with an
example of hospital management system.
In a Hospital Management System, different object-oriented relationships
help model real-world interactions clearly:
•   Aggregation (weak “has-a” relationship): A Hospital has Doctors,
but doctors can exist independently and may work in multiple
hospitals. So, if the hospital is removed, doctors still exist.
•   Composition (strong “has-a” relationship): A Patient has a Medical
Record, which cannot exist without the patient. If the patient is
Chap 5,   deleted, the medical record is also removed, showing strong   [10]
CO3,SO2,BL3   dependency.
•   Inheritance (is-a relationship): Doctor and Nurse can inherit from a
common superclass like Staff, sharing common attributes (name,
ID, salary) while having their own specific features.
•   Realization (implements relationship): An interface like Payment
can be realized by classes such as CreditCardPayment or
UPIPayment, where each class provides its own implementation of
the payment method.
These relationships improve modularity, reusability, and clarity in
designing the hospital system.
Q6   [20]
a)   Explain the 3 layers in package diagram, with neat diagram
6,CO4,SO2,BL2   [10]
1. Presentation Layer (UI Layer)
********** 3 **********
--- page 4 ---
This layer handles user interaction. It includes interfaces like web pages,
mobile apps, or GUIs where users input data and view results. It does not
contain business logic but communicates user requests to the next layer.
2. Business Logic Layer (Application Layer)
This is the core layer where all processing happens. It contains business
rules, validations, and decision-making logic (e.g., booking rules in a
railway or hospital system). It acts as a bridge between presentation and
data layers.
3. Data Access Layer (Database Layer)
This layer manages data storage and retrieval. It interacts with databases,
performs CRUD operations, and ensures data persistence. It isolates
database logic from the rest of the system.
b)   Explain initial db design in a UML environment with an example of
hospital management system
Ans:
8,CO4,SO2,BL4   Initial database design in a UML environment involves identifying entities   [10]
(classes), attributes, and relationships from system requirements and
representing them using UML class diagrams, which are later mapped to
database tables.
Q7   [20]
a)   Discuss how high cohesion and low coupling improve system design with
an example.
High cohesion means a module focuses on a single, well-defined
responsibility, while low coupling means modules have minimal
dependencies on each other. Together, they improve system design by
making it easier to understand, maintain, test, and modify code without
affecting other parts of the system.
8, CO4,SO2,BL3   [10]
Example: In a Hospital Management System, a Billing module should only
handle payment-related tasks (high cohesion), and it should interact with
modules like Patient or Appointment through well-defined interfaces rather
than direct dependencies (low coupling). This way, if billing logic changes
(e.g., new payment method), it can be updated without impacting other
modules, resulting in a more flexible and scalable system.
b) Design the deployment diagram for online food ordering system.
9,CO4,SO2,BL4   Ans: Design a diagram, considering the processor, connection , node and   [10]
device.
********** 4 **********
````
