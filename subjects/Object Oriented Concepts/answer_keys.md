# Object Oriented Concepts: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 2 · Answer key · paper d297136716e7

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/76902__Semester II.zip :: Final-Exam/Bachelor of Science (Information Technology) - 45618/Object Oriented Concepts/ANS_Final-Exam_Object Oriented Concepts(NHOOC151)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 60; duration hours: 2; exam date: 25 Mar 2026
- Text: text (12 pages)

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: Bachelor of Science (Information Technology)/B.Sc. (IT)
Year: I/Semester II (Exam Year: 2025-2026)
Subject: Object Oriented Concepts
Date: 25 Mar 2026   Time: 08:00 am - 10:00 am (02:00 Hrs.)
Max Marks: 60
FINAL EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 12 pages
2. Questions Q1 to Q3 are compulsory
3. In total 12 Questions must be attempted
4. Each question carries equal marks. The marks for each question are indicated on the right-hand side
5. Start each new question on a fresh page in the answer booklet
6. Draw diagrams wherever required to support your answers
7. Students may add pseudocode or code sippet to the answer where relevant
8. For any psuedocode based question, ensure to describe clearly
9. Clearly mention the question number while answering to avoid confusion
Q1. Answer the following questions(Attempt Any 4 Questions)   20
a. Characteristics of Imperative Programming   5
1. The program specifies how a task should be performed through a sequence of
commands
2. Data is stored in variables whose values change during program execution
3. Uses loops (for, while), conditionals (if-else), and statements to control program flow
4. Program execution is based on modifying program state over time
Differences between Programming and Object Oriented Programming
Imperative Programming   Object-Oriented Programming
Page 1 of 12
--- page 2 ---
Focuses on procedures and step-by-
Focuses on objects and data modeling
step instructions
Emphasizes functions and control flow   Emphasizes classes and objects
Data and methods are bundled
Data and functions are separate
together
Less focus on real-world modeling   Models real-world entities
b. Objects are considered as instances of class because   5
1. A class acts as a blueprint or template that defines the structure (attributes) and behavior
(methods)
2. An object is a specific realization of that blueprint
3. Therefore, an object is called an instance of a class because it is a concrete example created
from the class definition
Effects of creating multiple objects
1. Each object has its own copy of data (attributes). Changes made to one object’s data do not
affect others
2. Objects share the same methods. All objects use the same behavior defined in the class
3. While the structure and behavior remain the same, each object maintains its own
independent state
c. Modular design is an approach where a system is divided into smaller, independent modules,   5
each responsible for a specific task. It contributes to improving modifiability in the following
ways:
1. If a change is required, it can be made in one module without affecting the entire system
2. If a change is required, it can be made in one module without affecting the entire system
3. Only the modified module needs thorough retesting, saving time and effort
4. Updates, bug fixes, or feature additions can be handled more efficiently
Page 2 of 12
--- page 3 ---
Consider an Online Shopping System divided into modules such as:
User Management
Payment Processing
Order Management
If the payment method needs to be updated (e.g., adding UPI support), only the Payment
Processing module needs modification. The other modules remain unaffected.
d. A Ride-Sharing System involves multiple entities such as drivers, passengers, rides, and   5
payments. Object-Oriented concepts can be applied to organize the system effectively.
Using OOP, the following main classes can be identified:
Driver – stores driver details, availability status
Passenger – stores passenger details and ride history
Ride – manages ride details such as pickup, drop, fare
Payment – handles payment method and transaction details
Each class contains related data and methods, ensuring proper structure.
Suggested modifications for future updates:
1. Create a common superclass such as User for Driver and Passenger to avoid code
duplication
2. Design the Payment class so new payment methods (e.g., wallet, UPI) can be added
without affecting other classes
3. Design the Payment class so new payment methods (e.g., wallet, UPI) can be added
without affecting other classes
4. Keep data private and allow controlled updates to ensure safe feature additions
e.   5
Page 3 of 12
--- page 4 ---
f. In the Cohesion–Coupling Matrix, if we move sequentially from one quadrant to the next   5
(in a logical progression from worst to best), we can observe how design quality improves
step by step. The usual sequence of improvement is:
1. Low Cohesion – High Coupling (Worst)
2. Low Cohesion – Low Coupling
3. High Cohesion – High Coupling
4. High Cohesion – Low Coupling (Best)
From Low Cohesion – High Coupling to Low Cohesion – Low Coupling
1. Coupling is reduced, modules become more independent. However, internal structure
is still weak. This is a partial improvement
From Low Cohesion – Low Coupling to High Cohesion – High Coupling -
1. Internal organization improves, modules now have clear responsibilities but
dependencies between modules increases. This improves internal clarity but reduces
flexibility due to high coupling
From High Cohesion – High Coupling to High Cohesion – Low Coupling -
1. Coupling is reduced while maintaining strong internal focus. Modules are both well-
structured and independent. This represents the highest design improvement.
Page 4 of 12
--- page 5 ---
Sequential movement shows gradual design refinement. The final quadrant (High
Cohesion – Low Coupling) represents the most desirable system design because it
combines clarity with independence.
Q2. Answer the following questions(Attempt Any 4 Questions)   20
a. If a programmer does not specify any access modifier, the compiler automatically assigns a   5
default access level.
Default Accessibility (C++)
·   In a class → Private by default
·   In a structure (struct) → Public by default
-Meaning
Members declared without modifier in a class cannot be accessed directly outside the class.
-Importance
This prevents accidental exposure of data and enforces encapsulation even if programmer
forgets to specify access level.
Conceptually:
Class = Secure by default
Struct = Open by default
b. An abstract class cannot be instantiated because it may contain abstract methods that do not   5
have implementations. Creating an object of such a class would result in incomplete behavior,
since the required methods are meant to be defined in derived classes.
Abstract classes are designed to act as base templates, ensuring that subclasses provide specific
implementations while sharing common structure.
Example:
If Shape is abstract and declares an abstract method area(), then instantiating Shape is
meaningless because the actual area calculation depends on whether the shape is a Circle,
Rectangle, etc. Therefore, only concrete subclasses can be instantiated.
c. A class can have different types of constructors based on how objects are initialized.   5
Default Constructor
A default constructor is called when an object is created without passing any arguments. It
initializes the object with default values set by the programmer.
Example use: Creating a new object with initial values like ID = 0 and salary = 0.
Copy Constructor
Page 5 of 12
--- page 6 ---
A copy constructor is called when a new object is created using an existing object. It copies all
the values of the existing object into the new one.
Example use: Creating a duplicate Employee object with the same ID and salary.
Thus, the default constructor initializes a fresh object, while the copy constructor initializes an
object by copying another object’s data.
Example:
#include <iostream>
using namespace std;
class Employee {
int empID;
double salary;
public:
// Default constructor
Employee() {
empID = 0;
salary = 0.0;
}
// Copy constructor
Employee(Employee &e) {
empID = e.empID;
salary = e.salary;
}
void setData(int id, double sal) {
empID = id;
salary = sal;
}
void display() {
cout << "ID: " << empID << " Salary: " << salary << endl;
}
};
int main() {
Employee e1;
e1.setData(101, 50000);
Employee e2 = e1; // Copy constructor invoked
Page 6 of 12
--- page 7 ---
e1.display();
e2.display();
return 0;
}
d. The inheritance pattern used here is Hybrid Inheritance (combination of hierarchical and   5
multiple inheritance).
Device is the base class.
Printer and Scanner inherit from Device → Hierarchical Inheritance.
AllInOne inherits from both Printer and Scanner → Multiple Inheritance.
Device
/ \
Printer Scanner
\ /
AllInOne
Advantage:
Code Reusability –
The AllInOne class can reuse features of Device (basic features), Printer (printing functions),
and Scanner (scanning functions). This reduces duplication of code and improves modularity.
Issue:
Diamond Problem (Ambiguity Issue) –
Since both Printer and Scanner inherit from Device, the AllInOne class may receive two copies
of Device’s members. This can create ambiguity when accessing Device’s methods or variables
and may require special handling (e.g., virtual inheritance in C++).
e. Method overloading and method overriding are two important ways to achieve   5
polymorphism.
Method overloading occurs when multiple methods in the same class have the same name
but different parameter lists. It is resolved at compile time and is mainly used for
convenience and readability.
Method overriding occurs when a derived class provides its own implementation of a
method already defined in the base class. It is resolved at runtime and forms the
foundation of dynamic polymorphism.
Page 7 of 12
--- page 8 ---
Method overriding is considered more powerful because it allows true run-time
polymorphism. It enables a base class reference to call derived class methods
dynamically, supporting extensibility, dynamic binding, and flexible design in real-world
applications.
f. Composition: Building and Room   5
A Building is made up of multiple Room objects, and a room cannot exist without a
building. This is Composition.
Multiplicity:
Building → Room : 1 to 1..*
Association: Room and Sensor
Each Room is associated with multiple Sensors, but sensors may be reassigned or reused.
Therefore, this is a normal Association (or aggregation-like sharing).
Multiplicity:
Room → Sensor : 1 to 0..*
Sensor → Room : 0..1 to 1 (if assigned to one room at a time)
Dependency: MaintenanceService and Sensor
A MaintenanceService depends on Sensor data temporarily for diagnostics, so the
relationship is Dependency.
Q3. Answer the following questions(Attempt Any 4 Questions)   20
a. The Singleton design pattern is a creational design pattern that ensures a class has only   5
one instance and provides a global point of access to that instance.
Primary Objective of Singleton
1. To prevent multiple instances of a class from being created
2. To allow all parts of the system to access the same shared instance
3. To ensure consistent behavior when managing shared resources such as configuration
settings, logging, or database connections
4. Prevents unnecessary creation of multiple objects, saving memory and system
resources
Page 8 of 12
--- page 9 ---
5. Provides a single control point for managing shared services like logging,
configuration, or caching
6. Ensures all components use the same data or configuration, avoiding conflicts
7. Makes it easier to manage access permissions and security since only one instance
handles operations
b. Answer:   5
The Iterator pattern is a behavioral design pattern that allows sequential access to elements of a
collection without exposing its internal structure. It separates the traversal logic from the
collection itself.
Example
Suppose we have a collection of student names: [Anita, Rahul, Meera]
Pseudocode / Simple Steps
1. Create an iterator for the student list
2. While the iterator has more elements:
1. Retrieve the next student name
2. Display the name
Working Explanation
1. The iterator moves one element at a time
2. It checks whether another element exists before accessing it
3. The internal storage (array, list, etc.) is not exposed to the user
c. Must Have (First Version Core Features)   5
1. The system shall allow registered voters to log in securely.
2. The system shall verify voter identity before allowing voting.
3. The system shall display the list of candidates/options clearly.
Page 9 of 12
--- page 10 ---
4. The system shall allow the voter to cast exactly one vote.
5. The system shall confirm submission before final vote recording.
6. The system shall store the vote securely and prevent duplicate voting.
Should Have (Important Enhancements)
7. The system shall generate a voting receipt after successful submission.
8. The system shall provide session timeout for inactive users.
Could Have (Optional Features)
9. The system shall support multilingual interface for accessibility.
10. The system shall provide accessibility support for disabled voters.
Won’t Have (Not in First Release)
11. The system shall provide remote internet voting in future versions.
12. The system shall include blockchain-based voting verification later.
5
d. 1. Accuracy
Step counts, heart rate, and sleep monitoring must be correct. Inaccurate data can
mislead users about health progress.
2. Performance
The app should run smoothly without draining the battery. Good performance ensures
continuous tracking.
3. Usability
The interface must be simple and user-friendly. Better usability increases engagement
and motivation.
4. Reliability
The app must record daily activity consistently without crashes. Reliability builds
trust in reports.
5. Security and Privacy
Health data must be protected from unauthorized access. Privacy ensures user
confidence.
Page 10 of 12
--- page 11 ---
6. Scalability
The app should support millions of users and large data storage. Scalability ensures
uninterrupted service.
e. Domain expertise refers to in-depth knowledge of the specific field or industry for which   5
a system is being developed (e.g., banking, healthcare, education). It plays a critical role
in ensuring requirements are complete and correct.
Role in Completeness and Correctness
1. Domain experts understand real-world processes and can identify requirements that
users may overlook
2. They help recognize special conditions, rules, and constraints specific to the domain
3. Prevents missing functionalities by aligning requirements with actual workflows
4. Ensures that system rules match real-world regulations and policies
5. Prevents incorrect assumptions by clarifying terminology and processes
6. Confirms that requirements reflect actual user needs
f. Weakness in the current requirements   5
1. Incomplete requirements like delivery tracking, restaurant management, and order history
are missing
2. Delivery partners and restaurants were not consulted
3. The system may work technically but fail to support real-world operations effectively
4. Customers may demand features like order tracking, estimated delivery time, and
notifications
Additional Requirements to be gathered
1. Order tracking
2. Delivery notifications
3. Ratings or feedbacks
Page 11 of 12
--- page 12 ---
4. Order history
5. Multiple payment options
6. Order and menu management
7. Delivery assignment
8. Route optimization
Page 12 of 12
````

## 2025-26 · Re-Exam · Sem 2 · Answer key · paper c7ee2ac6ba87

- Departments: B.Sc Information Technology
- Programmes: Bachelor of Science (Information Technology) - 45618
- Source: `00_Original_Downloads/2023/76902__Semester II.zip :: Re-Exam/Bachelor of Science (Information Technology) - 45618/Object Oriented Concepts/ANS_Re-Exam_Object Oriented Concepts(NHOOC151)_Semester II_2025-2026.pdf`
- Printed on paper: max marks: 60; duration hours: 2; exam date: 17 Jun 2026
- Text: text (13 pages)

````text
Synoptic
SVKM
Narsee Monjee College of Com. & Eco.
Programme: B.Sc. (IT)
Year: I/Semester II (Exam Year: 2025-2026)
Subject: Object Oriented Concepts
Date: 17 Jun 2026   Time: 10:30 am - 12:30 pm (02:00 Hrs.)
Max Marks: 60
RE EXAMINATION(2025-2026)
Instructions:
1. This Synoptic paper contains 13 pages
2. Questions Q1 to Q3 are compulsory
3. In total 12 Questions must be attempted
4. Each question carries equal marks. The marks for each question are indicated on the right-hand side
5. Start each new question on a fresh page in the answer booklet
6. Draw diagrams wherever required to support your answers
7. Students may add pseudocode or code sippet to the answer where relevant
8. For any psuedocode based question, ensure to describe clearly
9. Clearly mention the question number while answering to avoid confusion
Q1. Answer the following questions(Attempt Any 4 Questions)   20
a. Object-Oriented Programming (OOP) is a programming paradigm based on the concept   5
of objects, where data and the methods that operate on that data are bundled together
into a single unit called a class. It focuses on modeling real-world entities using objects to
improve modularity, reusability, and maintainability.
Four Fundamental Principles of OOP:
1. Encapsulation
Bundling data (variables) and methods (functions) within a class and restricting direct
access to some components to protect data integrity.
Page 1 of 13
--- page 2 ---
2. Abstraction
Hiding complex implementation details and exposing only the essential features of an
object to the user.
3. Inheritance
Allowing one class (child class) to acquire properties and behaviors of another class
(parent class), promoting code reusability.
4. Polymorphism
The ability of objects to take multiple forms, enabling methods to perform
differently based on the object calling them   (e.g., method overloading or
overriding)
b. A class is considered the fundamental building block of an object-oriented system   5
because it forms the basic structure from which objects are created and organized and it
is considered so for the following reasons:
1. A class defines the attributes and methods that objects will have. Without classes,
objects cannot be created
2. Classes combine data and functions into a single unit, promoting modular design
3. Through inheritance, classes allow reuse and extension of existing functionality
4. Large systems are structured into multiple interacting classes, making them
manageable
5. Concepts like encapsulation, abstraction, inheritance, and polymorphism are
implemented through classes
c. Encapsulation means keeping data and the methods that operate on that data together inside a   5
class, while restricting direct access to the data. Since data and related methods are grouped in
one class, the student registration module can be tested independently without affecting other
parts of the system. Encapsulation provides specific methods (e.g., registerStudent(),
updateDetails()) to interact with the module, making it easier to test defined functionalities.
Because internal data cannot be modified directly, unexpected changes are minimized, making
test results more reliable
It controls data access and modificaton in the following ways:
Page 2 of 13
--- page 3 ---
1. Data members (like student ID, name, course details) are kept private, preventing
unauthorized access
2. Data members (like student ID, name, course details) are kept private, preventing
unauthorized access
3. Ensures that incorrect or invalid data cannot be directly entered into the system
d. In a University Course Registration System, the main classes can be:   5
Student – stores student details and enrolled courses
Course – contains course information such as course code, title, and credits
Enrollment – represents the registration of a student in a course
Grade – stores marks or final grade for a course
The relationships among these classes help structure the system logically. Following are
the relationships:
1. Association
A student can enroll in multiple courses, and a course can have multiple students.
This represents a many-to-many association.
2. Aggregation
The Enrollment class can act as a link between Student and Course.
If a student record is removed, enrollment details may also be affected, but courses can
still exist independently
3. Composition
A Grade is strongly related to Enrollment.
If an enrollment is deleted, the corresponding grade is also removed. This shows a strong
“part-of” relationship
4. Dependency
The Course Registration system may depend on validation rules (e.g., prerequisites),
showing functional dependency between Course and Enrollment.
Page 3 of 13
--- page 4 ---
e.   5
f. Cohesion refers to how closely related the tasks within a module are. It is mainly classified as:   5
High Cohesion - A module performs a single, well-defined task. All elements of the module
are strongly related to each other.
Low Cohesion - A module performs multiple unrelated tasks. The elements inside the module
are weakly related.
High Cohesion leads to better modular design because - 3 Marks
1. The module has a clear purpose, making it easier to understand
2. Changes can be made within one module without affecting others
3. Testing and debugging become simpler
4. It improves maintainability and system organization
In contrast, low cohesion increases complexity and makes maintenance difficult.
Q2. Answer the following questions(Attempt Any 4 Questions)   20
a. Access specifiers (access modifiers) are keywords used inside a class to control the   5
accessibility (visibility) of data members and member functions to other parts of the program.
Page 4 of 13
--- page 5 ---
They help implement the OOP principle of Encapsulation, where the internal details of an
object are hidden and only required information is exposed.
Purpose of Access Specifiers
Protect sensitive data from unauthorized access
Restrict direct modification of variables
Provide controlled access through member functions
Maintain data integrity
Reduce dependency between classes
Improve modularity and maintainability
b. An interface defines a contract that specifies what methods a class must implement. It focuses   5
only on method declarations and ensures that different unrelated classes follow the same set of
behaviors. A class can implement multiple interfaces.
An abstract class is a partially implemented class that provides a common base for related
classes. It can contain both abstract methods (without implementation) and concrete methods
(with implementation). A class can extend only one abstract class.
Differences:
Interface provides only method rules, abstract class provides rules plus shared
implementation.
Interface does not contain constructors, abstract class can have constructors.
Interface supports multiple inheritance through implementation, abstract class does not.
Interface is used for defining capabilities, abstract class is used for defining a base category.
Page 5 of 13
--- page 6 ---
Example:
Payable can be an interface implemented by Teacher and Consultant, while Employee can be
an abstract class providing common details like name and requiring subclasses to define salary
calculation.
c. A constructor is a special member function of a class that is automatically executed when   5
an object is created. Its main purpose is to initialize the data members of the object at the
time of creation itself.
In a class like Employee, the data members such as employee ID and salary must have
meaningful values before the object is used. If constructors are not used, the variables
may contain garbage values, leading to incorrect results.
By using a constructor, the Employee object can be created with proper initial values,
either through default initialization or by passing parameters. This ensures that every
Employee object starts in a valid and consistent state.
Thus, constructors help in automatic and correct initialization of employee details
immediately during object creation.
C++ Example:
#include <iostream>
using namespace std;
class Employee {
int empID;
double salary;
public:
Employee(int id, double sal) {
empID = id;
salary = sal;
}
void display() {
cout << "Employee ID: " << empID << endl;
cout << "Salary: " << salary << endl;
}
};
int main() {
Employee e1(101, 45000);
e1.display();
return 0;
}
Page 6 of 13
--- page 7 ---
d. A class hierarchy that combines more than one form of inheritance is called Hybrid   5
Inheritance. It is a mixture of two or more inheritance types such as hierarchical, multilevel,
and multiple inheritance.
Example:
1. Device (Base Class)
Attributes: deviceID, brand
Methods: powerOn(), powerOff()
2. InputDevice inherits from Device
3. OutputDevice inherits from Device
4. SmartPhone inherits from both InputDevice and OutputDevice
Device
/   \
InputDevice OutputDevice
\ /
SmartPhone
Here,
Device → InputDevice and OutputDevice (Hierarchical Inheritance)
SmartPhone → InputDevice + OutputDevice (Multiple Inheritance)
This forms a hybrid inheritance structure because it includes hierarchical inheritance
(Device → Printer, Scanner) and multiple inheritance (AllInOne inherits from both).
Complications of Hybrid Inheritance
Hybrid inheritance can become complicated because:
It creates complex relationships between classes.
Conflicts may arise due to multiple parent classes having the same members.
The flow of inherited properties becomes difficult to trace.
Debugging and maintenance become harder in large systems.
Therefore, hybrid inheritance provides flexibility but increases complexity and must be
used carefully in object-oriented design.
Page 7 of 13
--- page 8 ---
e. Polymorphism is a key feature of object-oriented programming that allows one interface   5
or method name to represent multiple forms. It is mainly classified into compile-time
polymorphism and run-time polymorphism.
Compile-time polymorphism is also called static binding. In this type, the method to be
executed is decided by the compiler during compilation. It is achieved through method
overloading and operator overloading. Since the decision is made early, it is faster but
less flexible because the exact method call is fixed before execution.
Run-time polymorphism is also called dynamic binding. In this type, the method to be
executed is decided at runtime based on the actual object type. It is achieved through
method overriding using inheritance and virtual functions. This provides greater
flexibility because the same base class reference can work with different derived class
objects and execute the correct method dynamically.
Run-time polymorphism provides greater flexibility in object-oriented systems because it
supports dynamic behavior, extensibility, and allows programs to adapt to new derived
classes without modifying existing code.
f. Aggregation: Film and Scene   5
A Film aggregates multiple Scene objects because scenes can exist independently during
editing and may be reused or moved. This is Aggregation.
Multiplicity:
Film → Scene : 1 to 0..*
Association: Scene and Actor
Each Scene involves multiple Actors, and an Actor can appear in many scenes. This is a
many-to-many Association.
Multiplicity:
Scene → Actor : 0.. to 0..**
Dependency: ProductionReport and Film
A ProductionReport depends on Film data for generating reports, so it is a Dependency
relationship.
Aggregation vs Composition in this design
Aggregation means Film does not fully control the lifetime of Scenes.
Composition would mean Scenes cannot exist without Film, which is not true here.
Thus, aggregation is more appropriate because scenes remain independent during
production workflows.
Page 8 of 13
--- page 9 ---
Q3. Answer the following questions(Attempt Any 4 Questions)   20
5
a. 1. Ensures that only one object of the class exists throughout the application
2. Provides a single, easy-to-access instance that can be used anywhere in the system
3. Prevents unnecessary duplication of objects, saving memory and system resources
4. Since all components use the same instance, data remains consistent across the
application
5. Useful for managing shared services like configuration settings, logging, or session
handling
6. The instance can be created only when it is first required, improving performance
7. Instead of using global variables, a Singleton provides a structured and secure global
access point
8. Since the constructor is private, object creation is strictly controlled
9. Having a single instance makes it easier to track issues related to shared resources
10. Useful when different modules need to coordinate through one common object
b. An iterator is an object that allows sequential access to elements of a collection (such as a   5
list, array, or set) without exposing its internal structure
Purpose in OOP
1. Allows elements of a collection to be accessed one by one in a structured manner
2. Users do not need to know how the collection is implemented internally
3. Separates collection storage logic from traversal logic
4. Different types of collections can be traversed using a common interface
c. Must Have   5
Page 9 of 13
--- page 10 ---
1. The system shall allow student registration and login.
2. The system shall allow administrators to create and schedule exams.
3. The system shall display questions and accept answers during the exam.
4. The system shall enforce exam timing and auto-submit after time ends.
5. The system shall calculate results for objective-type exams.
Should Have (Important but not critical)
6. The system shall allow question bank management for reuse.
7. The system shall provide exam performance reports for students.
8. The system shall support multiple question types (MCQ, descriptive).
Could Have (Optional enhancements)
9. The system shall provide proctoring features like webcam monitoring.
10. The system shall allow students to review answers before final submission.
Won’t Have (Later versions)
11. The system shall support AI-based cheating detection in future releases.
The system shall provide offline exam mode in later versions.
5
d. 1. Real-time Responsiveness
Live bus location must update quickly. This is an NFR because it defines system speed,
not functionality.
2. Availability
The app must remain accessible throughout the day. High uptime ensures commuters
can rely on it.
3. Accuracy
Arrival time predictions must be correct. Accuracy ensures dependable planning.
Page 10 of 13
--- page 11 ---
4. Scalability
The system must support many users during rush hours. Scalability ensures
performance under load.
5. Security
Online ticket payments and user accounts must be protected. Security ensures safe
transactions.
6. Reliability
The system should provide consistent tracking without errors. Reliability prevents
commuter confusion.
7. Usability
The interface must be easy for all users, including elderly passengers. Usability
improves adoption.
e. Domain knowledge refers to deep understanding of the specific field in which a system   5
operates (such as healthcare, aviation, banking, etc.). It is especially critical in safety-
critical and large-scale systems.
Importance in Safety Critical Systems
In systems where human life or major assets are involved (e.g., medical or aviation
systems):
Incorrect requirements can lead to dangerous consequences
Domain experts understand legal standards and safety protocols
Critical edge cases must be identified and properly managed
Without domain knowledge, even technically correct systems may become unsafe.
Importance in Large-Scale Systems
In systems with many users and complex processes:
Large systems involve multiple interconnected processes
Domain experts help identify real-world constraints
Mistakes in large systems are expensive to fix
f. System Requirements -(Any 3)   5
Page 11 of 13
--- page 12 ---
System Needs /
Category   Description
Requirements
Student   Students can upload files in multiple
Assignment Upload
Features   formats (PDF, DOCX, etc.).
Submission   System should enforce deadlines and
Deadlines   allow late submissions with restrictions.
View Grades /   Students can view graded assignments
Feedback   and teacher comments.
Alerts for new assignments, deadlines,
Notifications
and grades.
Teacher   Teachers can create assignments, set
Assignment Creation
Features   deadlines, and specify instructions.
Teachers can grade submissions and
Grading & Feedback
provide detailed comments.
Ability to download all student
Bulk Download
submissions at once.
Administrator   Admins can add/remove students,
User Management
Features   teachers, and assign classes.
Track system usage, performance, and
System Monitoring
errors.
Non-
Protect user data and prevent
Functional   Security
unauthorized access.
Requirements
System should be available during
Reliability
school hours and prevent data loss.
Interface should be simple and intuitive
Usability
for all users.
Support growing number of users and
Scalability
assignments.
Page 12 of 13
--- page 13 ---
User Requirements -
User Type   Expectation
Easy and quick assignment upload, clear deadlines, timely
Students
feedback.
Simplified grading process, ability to provide constructive
Teachers
feedback, efficient class management.
Smooth user management, ability to monitor system usage, and
Administrators
ensure security and compliance.
Page 13 of 13
````
