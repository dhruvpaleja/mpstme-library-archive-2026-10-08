# Object Oriented Programming Lab — syllabus

8 syllabus section(s) for this course in the archive, newest batch first. Text comes from the PDF (OCR for scanned pages; check figures against the source). All programmes' syllabi: [`syllabi/`](../README.md).

## B TECH · Cyber Security · AY 2026-27 · Sem 1

- Course as printed: Object Oriented Programming Lab (code 702CO0C064)
- Source: `04_Syllabi_Archive/B TECH/2ND YEAR/CYBERSECURITY/SEM III/B Tech Cybersecurity, 2nd Year, Sem-III, A Y 2026-27.pdf`, page 16-22

````text
Program: B Tech (CE, DS, AI, AIML, AIDS, IT, CSECS, CSEDS, CSBS, Semester: I/II/III/IV
CS)
MBA Tech (CE, IT, DS, AI)
Course: Object Oriented Programming Lab   Course Code: 702CO0C064
Teaching Scheme   Evaluation Scheme
Lecture   Tutorial
Practical   Internal Continuous   Term End Examinations
(Hours per   (Hours per
(Hours per   Credit   Assessment (ICA) (Marks -   (TEE)
week)   week)
week)   50)   (Marks- 50 )
0   2   0   1   Marks Scaled to 50   (Practical Examination)
Marks Scaled to 50
Prerequisite: Computational Thinking for Problem Solving
Course Objective
This course aims to help students understand the object-oriented paradigm and its application in designing and
developing solutions to engineering/industry problems.
Course Outcomes- After completion of the course, students will be able to -
1.   Implement basic programs using classes, objects (K3),
2.   Design solutions with class diagrams and implementing polymorphism, and inheritance (K3),
3.   Implement programs using exception handling and files (K3),
4.   Implement programs using abstract classes, and interfaces (K3),
5.   Design solutions using generics programming and design patterns for real-world problems (K3).
List of Experiments
Exp.   Programming Topic
No.
1.   Concept: Implement a program using classes, objects, data members and member functions.
Problem Statement: Create a class “Employee” to read and print information about an employee with
the following data members:
Name of the employee,
ID of the employee,
Department of the employee,
Basic salary.
Task: Perform the following functions to complete the operations:
1.   Write a member function read_Employee() to initialize the object.
2.   Write a member function to Calculate Gross salary and its components (declare them as data
members) based on the following conditions:
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Dearness allowance (DA) = 50 % of basic salary
HRA = 30 % basic salary
TA = 10 % basic salary
Gross Salary = basic salary + DA + HRA + TA.
3.   Write a member function to display employee details with Gross Salary and all other
components.
2.   Concepts: Implement a program using Encapsulation, Abstractions and Array of Objects.
Problem Statement: A school is developing Library Management system to maintain the records of the
books. Where it performs basic operations such as making entry of the book, searching the book by book
name and author name. It also shows availability of the books.
Task:
Create class to manage the books in “Library” with following data members and functions.
Name of the book
Author of the book
Price of the book
No. of copies
Implement member functions to perform the following operations:
Read the data of 5 books – include books in the library.
Display the data of books – print the list of all the books in the library.
Search the specified book in the Library by name, if it is available or not, if available then display no of
copies of the book.
Search the specified book in the Library by Author Name, display all the books of the same author.
3   Concept: Implement a program using the concepts of constructor to initialize the object.
Problem Statement: A customer can open account in the bank with following attributes. A customer can
performs basic operations with the account created using class called “Bank Account”.
Customer Name
Address
Account Number
Age
Balance Amount
Task: Implement following functions to perform operations with an account:
1.   Use the parameterized constructor to initialize the array of objects.
2.   Write a function to withdraw amount after checking account no.
3.   Write a function to deposit amount after checking account no.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
4.   Write a function to display balance amount after checking account no.
5.   Write a function to display the Customer Profile.
4.   Concept: Implement a program using Inheritance, Runtime polymorphism and Modelling classes.
Problem Statement: A bank want to extend two more insurance services to their customers along with
basic bank operations performed using “Saving Bank Account”. These two additional services will be
implemented without changing existing bank account class. So, two additional classes are created by
deriving features from the “Bank Account”. These classes are name as “Life Insurance” and “Car
Insurance”. Premium of both the insurance policies are linked to bank account of the customer so that it
can be directly deducted from their saving account and current balance will be displayed after every
deduction. Features derived from the base classes are shown in the following diagram. The “Claim” class
is used to settle the claim amount and deposited in the respective saving bank account.
Note: Use Bank Account class created in the experiment 3 as base class in the hierarchy.
Data Members:   Members Functions:
Name of the   Open account
customer   Bank Account   Withdraw
Address Age   (Base Class)   Display Customer Deposit Details
Saving Account No   Display Balance
Balance
Data Members:   Data Members:
Policy No   Policy No
Sum Assured   Car Details
Premium   Premium
Term (No of Years)   Car   Duration
Life Insurance   Insurance
Members Functions:   (Derived Class)   (Derived Class)   Members Read Functions: data
Read data   Calculate premium
Calculate premium   Deduct premium
Deduct premium   (from saving)
(from saving annually   Display Information
and Term by 1).   Derived Data
Display Information   Members:
Policy No   Members Functions:
Sum Assured   Claim   Settlement Amount.
Premium   (Term or Car)
Term (No of Years)   Deposit amount in
Car details   (Derived   saving acc.
Premium   Class)   Display Information
Duration
Inheritance
Task:
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Implement member functions to perform the task: calculation of premium and deduction from the bank
account.
Life Insurance Class: Derived from Bank Account class
A.   Calculate Premium for Life insurance: use following conditions
1.   If age of a person is below 25 years - 3 K / Year / Lakh. (Sum Assured)
2.   If age of a person is in between 26 to 45 years – 4 K /year/ Lakh
3.   If age of a person is in between 46 to 60 years – 5 K /year/ Lakh
4.   If age > 60 – no insurance.
Car Insurance Class: Derived from Bank Account class
B.   Calculate Premium for car insurance: Use following conditions
1.   If Car is new then – 5 K / Year / Lakh (8 L)
2.   If Car is between 2 – 4 Year old – 3 K/ Year / Lakh
3.   If Car is between 5 – 7 Year old – 2 K/ Year / Lakh
Claim class: Derived from Life Insurance and Car Insurance
Function: Settlement () - will calculate the amount depending on the status of the policy
1.   Life insurance:
a.   If policy closed within first 5 years – Zero amount
b.   If policy closed between 6 – 12 years – 25 % of sum assured
c.   If policy closed between 13-20 years – 50 % of sum assured + 20 % of sum assured as bonus
d.   If policy closed after 20 years – sum assured + 100 % of sum assured as bonus
Deposit this amount to saving account
2.   Car Insurance:
a.   Amount spent by customer on repairing of Car.
Deposit this amount to saving account
Concept: Implement programs using exception handling
5
Problem Statements 1:
Write a program that takes two integers as input from the user and performs division. Handle the
division_by_zero error if the denominator is zero and display an appropriate message.
Problem Statements 2:
Create a method check_Eligibility(int age) that checks if a person is eligible to vote (age >= 18). If the age
is less than 18, the method should throw an Exception. Use the throws keyword to indicate that this
method can throw an exception.
Problem Statements 3:
Create a user-defined exception InsufficientBalanceException. Write a program where a user enters the
withdrawal amount. If the balance is less than the withdrawal amount, throw the custom exception.
Note: Consider the class “Bank_Account” created in the assignment 3 to demonstrate the withdrawal.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
6   Concept: Implement programs to handle data with external files.
Task1:
1.   Write a program to copy an image file from one location to another using byte-oriented streams.
Task2:
2.   Write a program to read a text file, and write a function to count the number of words in it.
3.   Write a function to search for the specific word. Use Buffer for efficient reading.
Concept: Implement programs to demonstrate the use of inner classes
7   Problem Statement: A smart home system has multiple devices, such as lights and fans, controlled by a
remote. Each remote has a power button to toggle the device on or off.
Task:
Create a class SmartHome that contains an inner class RemoteControl.
RemoteControl should have a method toggleDevice() that switches the device state (ON/OFF).
Simulate controlling a device using the inner class.
Expected outcome:
Device is currently OFF
Turning ON the device...
Device is now ON
Concept: Implement programs using abstract class and Interfaces
8   Problem Statement: An airline reservation system allows users to book economy and business class
tickets. The fare calculation and seat allocation process differs based on the ticket type.
Task:
Create an abstract class Flight with an abstract method calculateFare().
Implement subclasses EconomyClass and BusinessClass that override calculateFare().
Create an interface SeatAllocation with a method assignSeat().
Implement SeatAllocation in both subclasses to assign seat numbers.
Expected Outcome:
Enter ticket type (Economy/Business):
Business Fare: $1000
Seat assigned: 12A
Concept: Implement programs using template class and functions.
9
Problem Statement: Implement a generic library for fundamental data structures such as Stack, Queue,
and Linked List using templates (C++) or generics (Java).We write a generic function that can be used
for different data types. Examples of function templates are sort(), max(), min(), printArray().
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Task:
i.   Implement a generic stack with push, pop, and peek operations.
ii.   Implement a generic queue with enqueue and dequeue operations.
iii.   Implement a generic linked list with insertion, deletion, and search functionality.
iv.   Demonstrate with different data types (integers, floating-point numbers, and user-defined types
like complex numbers).
Concept: Implement program suing generics programming
10
Problem Statement:
Implement a generic sorting utility that allows users to sort data using custom comparator functions
provided as lambda expressions.
Task:
1.   Create a Generic Sorting Class:
a.   Implement a generic function that takes an array or list and a comparator function as input.
b.   Use lambda expressions to define different sorting criteria dynamically.
2.   Implement Sorting Strategies:
a.   Allow sorting based on natural ordering (ascending/descending).
b.   Allow user-defined sorting strategies (e.g., sorting based on absolute value, even-odd priority).
3.   Demonstrate with Different Data Types:
a.   Sort integers (normal order, absolute value, even-odd priority).
b.   Sort strings (alphabetically, by length).
c.   Sort user-defined objects (e.g., Employee class based on salary, age).
Text Books:
1. Y. Daniel Liang, “Introduction to Java Programming and Data Structures, Comprehensive Version”, 12th
Edition, Pearson paperback, 2024.
2. E. Balagurusamy, “Object Oriented Programming with C++”, 8th Edition, McGraw Hill, 2020.
Reference Books:
1. Dimitri Nesteruk, “Design Patterns in Modern C++20: Reusable Approaches for Object-Oriented Software
Design” 2nd Edition, Apress, 2022.
2. Maurice Naftalin, Philip Wadler, “Java Generics and Collections: Fundamentals and Recommended
Practices”, O'Reilly Media, Inc., 2nd Edition, 2025.
3. Bjarne Stroustrup, “The C++ Programming Language”, 4th Edition, Addison Wesley, Pearson Education,
2022.
4. Herbert Schildt, “Java 2: The Complete Reference”, 5th Edition, McGraw-Hill Education, 2017.
The list which is provided in the syllabus is guideline to conduct the practical sessions. The faculty can create
more practical examples suitable to given concepts in each experiment.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS
Mukesh Patel School of Technology Management & Engineering
Program: B Tech & MBA Tech (Artificial Intelligence), B Tech   Semester: III / IV
Cyber Security
````

## B TECH · Data Science · AY 2026-27 · Sem 1

- Course as printed: Object Oriented Programming Lab (code 702CO0C064)
- Source: `04_Syllabi_Archive/B TECH/2ND YEAR/DATA SCIENCE/Sem_03/B Tech 2nd Year, (Data Science), Sem III, Year 2026-2027.pdf`, page 19-25

````text
Program: B Tech (CE, DS, AI, AIML, AIDS, IT, CSECS, CSEDS, CSBS, Semester: I/II/III/IV
CS)
MBA Tech (CE, IT, DS, AI)
Course: Object Oriented Programming Lab   Course Code: 702CO0C064
Teaching Scheme   Evaluation Scheme
Lecture   Tutorial
Practical   Internal Continuous   Term End Examinations
(Hours per   (Hours per
(Hours per   Credit   Assessment (ICA) (Marks -   (TEE)
week)   week)
week)   50)   (Marks- 50 )
0   2   0   1   Marks Scaled to 50   (Practical Examination)
Marks Scaled to 50
Prerequisite: Computational Thinking for Problem Solving
Course Objective
This course aims to help students understand the object-oriented paradigm and its application in designing and
developing solutions to engineering/industry problems.
Course Outcomes- After completion of the course, students will be able to -
1.   Implement basic programs using classes, objects (K3),
2.   Design solutions with class diagrams and implementing polymorphism, and inheritance (K3),
3.   Implement programs using exception handling and files (K3),
4.   Implement programs using abstract classes, and interfaces (K3),
5.   Design solutions using generics programming and design patterns for real-world problems (K3).
List of Experiments
Exp.   Programming Topic
No.
1.   Concept: Implement a program using classes, objects, data members and member functions.
Problem Statement: Create a class “Employee” to read and print information about an employee with
the following data members:
Name of the employee,
ID of the employee,
Department of the employee,
Basic salary.
Task: Perform the following functions to complete the operations:
1.   Write a member function read_Employee() to initialize the object.
2.   Write a member function to Calculate Gross salary and its components (declare them as data
members) based on the following conditions:
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Dearness allowance (DA) = 50 % of basic salary
HRA = 30 % basic salary
TA = 10 % basic salary
Gross Salary = basic salary + DA + HRA + TA.
3.   Write a member function to display employee details with Gross Salary and all other
components.
2.   Concepts: Implement a program using Encapsulation, Abstractions and Array of Objects.
Problem Statement: A school is developing Library Management system to maintain the records of the
books. Where it performs basic operations such as making entry of the book, searching the book by book
name and author name. It also shows availability of the books.
Task:
Create class to manage the books in “Library” with following data members and functions.
Name of the book
Author of the book
Price of the book
No. of copies
Implement member functions to perform the following operations:
Read the data of 5 books – include books in the library.
Display the data of books – print the list of all the books in the library.
Search the specified book in the Library by name, if it is available or not, if available then display no of
copies of the book.
Search the specified book in the Library by Author Name, display all the books of the same author.
3   Concept: Implement a program using the concepts of constructor to initialize the object.
Problem Statement: A customer can open account in the bank with following attributes. A customer can
performs basic operations with the account created using class called “Bank Account”.
Customer Name
Address
Account Number
Age
Balance Amount
Task: Implement following functions to perform operations with an account:
1.   Use the parameterized constructor to initialize the array of objects.
2.   Write a function to withdraw amount after checking account no.
3.   Write a function to deposit amount after checking account no.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
4.   Write a function to display balance amount after checking account no.
5.   Write a function to display the Customer Profile.
4.   Concept: Implement a program using Inheritance, Runtime polymorphism and Modelling classes.
Problem Statement: A bank want to extend two more insurance services to their customers along with
basic bank operations performed using “Saving Bank Account”. These two additional services will be
implemented without changing existing bank account class. So, two additional classes are created by
deriving features from the “Bank Account”. These classes are name as “Life Insurance” and “Car
Insurance”. Premium of both the insurance policies are linked to bank account of the customer so that it
can be directly deducted from their saving account and current balance will be displayed after every
deduction. Features derived from the base classes are shown in the following diagram. The “Claim” class
is used to settle the claim amount and deposited in the respective saving bank account.
Note: Use Bank Account class created in the experiment 3 as base class in the hierarchy.
Data Members:   Members Functions:
Name of the   Open account
customer   Bank Account   Withdraw
Address Age   (Base Class)   Display Customer Deposit Details
Saving Account No   Display Balance
Balance
Data Members:   Data Members:
Policy No   Policy No
Sum Assured   Car Details
Premium   Premium
Term (No of Years)   Car   Duration
Life Insurance   Insurance
Members Functions:   (Derived Class)   (Derived Class)   Members Read Functions: data
Read data   Calculate premium
Calculate premium   Deduct premium
Deduct premium   (from saving)
(from saving annually   Display Information
and Term by 1).   Derived Data
Display Information   Members:
Policy No   Members Functions:
Sum Assured   Claim   Settlement Amount.
Premium   (Term or Car)
Term (No of Years)   Deposit amount in
Car details   (Derived   saving acc.
Premium   Class)   Display Information
Duration
Inheritance
Task:
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Implement member functions to perform the task: calculation of premium and deduction from the bank
account.
Life Insurance Class: Derived from Bank Account class
A.   Calculate Premium for Life insurance: use following conditions
1.   If age of a person is below 25 years - 3 K / Year / Lakh. (Sum Assured)
2.   If age of a person is in between 26 to 45 years – 4 K /year/ Lakh
3.   If age of a person is in between 46 to 60 years – 5 K /year/ Lakh
4.   If age > 60 – no insurance.
Car Insurance Class: Derived from Bank Account class
B.   Calculate Premium for car insurance: Use following conditions
1.   If Car is new then – 5 K / Year / Lakh (8 L)
2.   If Car is between 2 – 4 Year old – 3 K/ Year / Lakh
3.   If Car is between 5 – 7 Year old – 2 K/ Year / Lakh
Claim class: Derived from Life Insurance and Car Insurance
Function: Settlement () - will calculate the amount depending on the status of the policy
1.   Life insurance:
a.   If policy closed within first 5 years – Zero amount
b.   If policy closed between 6 – 12 years – 25 % of sum assured
c.   If policy closed between 13-20 years – 50 % of sum assured + 20 % of sum assured as bonus
d.   If policy closed after 20 years – sum assured + 100 % of sum assured as bonus
Deposit this amount to saving account
2.   Car Insurance:
a.   Amount spent by customer on repairing of Car.
Deposit this amount to saving account
Concept: Implement programs using exception handling
5
Problem Statements 1:
Write a program that takes two integers as input from the user and performs division. Handle the
division_by_zero error if the denominator is zero and display an appropriate message.
Problem Statements 2:
Create a method check_Eligibility(int age) that checks if a person is eligible to vote (age >= 18). If the age
is less than 18, the method should throw an Exception. Use the throws keyword to indicate that this
method can throw an exception.
Problem Statements 3:
Create a user-defined exception InsufficientBalanceException. Write a program where a user enters the
withdrawal amount. If the balance is less than the withdrawal amount, throw the custom exception.
Note: Consider the class “Bank_Account” created in the assignment 3 to demonstrate the withdrawal.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
6   Concept: Implement programs to handle data with external files.
Task1:
1.   Write a program to copy an image file from one location to another using byte-oriented streams.
Task2:
2.   Write a program to read a text file, and write a function to count the number of words in it.
3.   Write a function to search for the specific word. Use Buffer for efficient reading.
Concept: Implement programs to demonstrate the use of inner classes
7   Problem Statement: A smart home system has multiple devices, such as lights and fans, controlled by a
remote. Each remote has a power button to toggle the device on or off.
Task:
Create a class SmartHome that contains an inner class RemoteControl.
RemoteControl should have a method toggleDevice() that switches the device state (ON/OFF).
Simulate controlling a device using the inner class.
Expected outcome:
Device is currently OFF
Turning ON the device...
Device is now ON
Concept: Implement programs using abstract class and Interfaces
8   Problem Statement: An airline reservation system allows users to book economy and business class
tickets. The fare calculation and seat allocation process differs based on the ticket type.
Task:
Create an abstract class Flight with an abstract method calculateFare().
Implement subclasses EconomyClass and BusinessClass that override calculateFare().
Create an interface SeatAllocation with a method assignSeat().
Implement SeatAllocation in both subclasses to assign seat numbers.
Expected Outcome:
Enter ticket type (Economy/Business):
Business Fare: $1000
Seat assigned: 12A
Concept: Implement programs using template class and functions.
9
Problem Statement: Implement a generic library for fundamental data structures such as Stack, Queue,
and Linked List using templates (C++) or generics (Java).We write a generic function that can be used
for different data types. Examples of function templates are sort(), max(), min(), printArray().
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Task:
i.   Implement a generic stack with push, pop, and peek operations.
ii.   Implement a generic queue with enqueue and dequeue operations.
iii.   Implement a generic linked list with insertion, deletion, and search functionality.
iv.   Demonstrate with different data types (integers, floating-point numbers, and user-defined types
like complex numbers).
Concept: Implement program suing generics programming
10
Problem Statement:
Implement a generic sorting utility that allows users to sort data using custom comparator functions
provided as lambda expressions.
Task:
1.   Create a Generic Sorting Class:
a.   Implement a generic function that takes an array or list and a comparator function as input.
b.   Use lambda expressions to define different sorting criteria dynamically.
2.   Implement Sorting Strategies:
a.   Allow sorting based on natural ordering (ascending/descending).
b.   Allow user-defined sorting strategies (e.g., sorting based on absolute value, even-odd priority).
3.   Demonstrate with Different Data Types:
a.   Sort integers (normal order, absolute value, even-odd priority).
b.   Sort strings (alphabetically, by length).
c.   Sort user-defined objects (e.g., Employee class based on salary, age).
Text Books:
1. Y. Daniel Liang, “Introduction to Java Programming and Data Structures, Comprehensive Version”, 12th
Edition, Pearson paperback, 2024.
2. E. Balagurusamy, “Object Oriented Programming with C++”, 8th Edition, McGraw Hill, 2020.
Reference Books:
1. Dimitri Nesteruk, “Design Patterns in Modern C++20: Reusable Approaches for Object-Oriented Software
Design” 2nd Edition, Apress, 2022.
2. Maurice Naftalin, Philip Wadler, “Java Generics and Collections: Fundamentals and Recommended
Practices”, O'Reilly Media, Inc., 2nd Edition, 2025.
3. Bjarne Stroustrup, “The C++ Programming Language”, 4th Edition, Addison Wesley, Pearson Education,
2022.
4. Herbert Schildt, “Java 2: The Complete Reference”, 5th Edition, McGraw-Hill Education, 2017.
The list which is provided in the syllabus is guideline to conduct the practical sessions. The faculty can create
more practical examples suitable to given concepts in each experiment.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Program: B Tech (CE, DS, AI, AIML, AIDS, IT, CSECS, CSEDS, CSBS, Semester: III
CS)
MBA Tech (CE, IT, DS, AI)
````

## B TECH · Information Technology · AY 2026-27 · Sem 1

- Course as printed: Object Oriented Programming Lab (code 702CO0C064)
- Source: `04_Syllabi_Archive/B TECH/2ND YEAR/I T/Sem_03/B Tech, 2nd Year, (IT), Sem-III, Year 2026-2027.pdf`, page 16-22

````text
Program: B Tech (CE, DS, AI, AIML, AIDS, IT, CSECS, CSEDS, CSBS, Semester: I/II/III/IV
CS)
MBA Tech (CE, IT, DS, AI)
Course: Object Oriented Programming Lab   Course Code: 702CO0C064
Teaching Scheme   Evaluation Scheme
Lecture   Tutorial
Practical   Internal Continuous   Term End Examinations
(Hours per   (Hours per
(Hours per   Credit   Assessment (ICA) (Marks -   (TEE)
week)   week)
week)   50)   (Marks- 50 )
0   2   0   1   Marks Scaled to 50   (Practical Examination)
Marks Scaled to 50
Prerequisite: Computational Thinking for Problem Solving
Course Objective
This course aims to help students understand the object-oriented paradigm and its application in designing and
developing solutions to engineering/industry problems.
Course Outcomes- After completion of the course, students will be able to -
1.   Implement basic programs using classes, objects (K3),
2.   Design solutions with class diagrams and implementing polymorphism, and inheritance (K3),
3.   Implement programs using exception handling and files (K3),
4.   Implement programs using abstract classes, and interfaces (K3),
5.   Design solutions using generics programming and design patterns for real-world problems (K3).
List of Experiments
Exp.   Programming Topic
No.
1.   Concept: Implement a program using classes, objects, data members and member functions.
Problem Statement: Create a class “Employee” to read and print information about an employee with
the following data members:
Name of the employee,
ID of the employee,
Department of the employee,
Basic salary.
Task: Perform the following functions to complete the operations:
1.   Write a member function read_Employee() to initialize the object.
2.   Write a member function to Calculate Gross salary and its components (declare them as data
members) based on the following conditions:
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Dearness allowance (DA) = 50 % of basic salary
HRA = 30 % basic salary
TA = 10 % basic salary
Gross Salary = basic salary + DA + HRA + TA.
3.   Write a member function to display employee details with Gross Salary and all other
components.
2.   Concepts: Implement a program using Encapsulation, Abstractions and Array of Objects.
Problem Statement: A school is developing Library Management system to maintain the records of the
books. Where it performs basic operations such as making entry of the book, searching the book by book
name and author name. It also shows availability of the books.
Task:
Create class to manage the books in “Library” with following data members and functions.
Name of the book
Author of the book
Price of the book
No. of copies
Implement member functions to perform the following operations:
Read the data of 5 books – include books in the library.
Display the data of books – print the list of all the books in the library.
Search the specified book in the Library by name, if it is available or not, if available then display no of
copies of the book.
Search the specified book in the Library by Author Name, display all the books of the same author.
3   Concept: Implement a program using the concepts of constructor to initialize the object.
Problem Statement: A customer can open account in the bank with following attributes. A customer can
performs basic operations with the account created using class called “Bank Account”.
Customer Name
Address
Account Number
Age
Balance Amount
Task: Implement following functions to perform operations with an account:
1.   Use the parameterized constructor to initialize the array of objects.
2.   Write a function to withdraw amount after checking account no.
3.   Write a function to deposit amount after checking account no.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
4.   Write a function to display balance amount after checking account no.
5.   Write a function to display the Customer Profile.
4.   Concept: Implement a program using Inheritance, Runtime polymorphism and Modelling classes.
Problem Statement: A bank want to extend two more insurance services to their customers along with
basic bank operations performed using “Saving Bank Account”. These two additional services will be
implemented without changing existing bank account class. So, two additional classes are created by
deriving features from the “Bank Account”. These classes are name as “Life Insurance” and “Car
Insurance”. Premium of both the insurance policies are linked to bank account of the customer so that it
can be directly deducted from their saving account and current balance will be displayed after every
deduction. Features derived from the base classes are shown in the following diagram. The “Claim” class
is used to settle the claim amount and deposited in the respective saving bank account.
Note: Use Bank Account class created in the experiment 3 as base class in the hierarchy.
Data Members:   Members Functions:
Name of the   Open account
customer   Bank Account   Withdraw
Address Age   (Base Class)   Display Customer Deposit Details
Saving Account No   Display Balance
Balance
Data Members:   Data Members:
Policy No   Policy No
Sum Assured   Car Details
Premium   Premium
Term (No of Years)   Car   Duration
Life Insurance   Insurance
Members Functions:   (Derived Class)   (Derived Class)   Members Read Functions: data
Read data   Calculate premium
Calculate premium   Deduct premium
Deduct premium   (from saving)
(from saving annually   Display Information
and Term by 1).   Derived Data
Display Information   Members:
Policy No   Members Functions:
Sum Assured   Claim   Settlement Amount.
Premium   (Term or Car)
Term (No of Years)   Deposit amount in
Car details   (Derived   saving acc.
Premium   Class)   Display Information
Duration
Inheritance
Task:
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Implement member functions to perform the task: calculation of premium and deduction from the bank
account.
Life Insurance Class: Derived from Bank Account class
A.   Calculate Premium for Life insurance: use following conditions
1.   If age of a person is below 25 years - 3 K / Year / Lakh. (Sum Assured)
2.   If age of a person is in between 26 to 45 years – 4 K /year/ Lakh
3.   If age of a person is in between 46 to 60 years – 5 K /year/ Lakh
4.   If age > 60 – no insurance.
Car Insurance Class: Derived from Bank Account class
B.   Calculate Premium for car insurance: Use following conditions
1.   If Car is new then – 5 K / Year / Lakh (8 L)
2.   If Car is between 2 – 4 Year old – 3 K/ Year / Lakh
3.   If Car is between 5 – 7 Year old – 2 K/ Year / Lakh
Claim class: Derived from Life Insurance and Car Insurance
Function: Settlement () - will calculate the amount depending on the status of the policy
1.   Life insurance:
a.   If policy closed within first 5 years – Zero amount
b.   If policy closed between 6 – 12 years – 25 % of sum assured
c.   If policy closed between 13-20 years – 50 % of sum assured + 20 % of sum assured as bonus
d.   If policy closed after 20 years – sum assured + 100 % of sum assured as bonus
Deposit this amount to saving account
2.   Car Insurance:
a.   Amount spent by customer on repairing of Car.
Deposit this amount to saving account
Concept: Implement programs using exception handling
5
Problem Statements 1:
Write a program that takes two integers as input from the user and performs division. Handle the
division_by_zero error if the denominator is zero and display an appropriate message.
Problem Statements 2:
Create a method check_Eligibility(int age) that checks if a person is eligible to vote (age >= 18). If the age
is less than 18, the method should throw an Exception. Use the throws keyword to indicate that this
method can throw an exception.
Problem Statements 3:
Create a user-defined exception InsufficientBalanceException. Write a program where a user enters the
withdrawal amount. If the balance is less than the withdrawal amount, throw the custom exception.
Note: Consider the class “Bank_Account” created in the assignment 3 to demonstrate the withdrawal.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
6   Concept: Implement programs to handle data with external files.
Task1:
1.   Write a program to copy an image file from one location to another using byte-oriented streams.
Task2:
2.   Write a program to read a text file, and write a function to count the number of words in it.
3.   Write a function to search for the specific word. Use Buffer for efficient reading.
Concept: Implement programs to demonstrate the use of inner classes
7   Problem Statement: A smart home system has multiple devices, such as lights and fans, controlled by a
remote. Each remote has a power button to toggle the device on or off.
Task:
Create a class SmartHome that contains an inner class RemoteControl.
RemoteControl should have a method toggleDevice() that switches the device state (ON/OFF).
Simulate controlling a device using the inner class.
Expected outcome:
Device is currently OFF
Turning ON the device...
Device is now ON
Concept: Implement programs using abstract class and Interfaces
8   Problem Statement: An airline reservation system allows users to book economy and business class
tickets. The fare calculation and seat allocation process differs based on the ticket type.
Task:
Create an abstract class Flight with an abstract method calculateFare().
Implement subclasses EconomyClass and BusinessClass that override calculateFare().
Create an interface SeatAllocation with a method assignSeat().
Implement SeatAllocation in both subclasses to assign seat numbers.
Expected Outcome:
Enter ticket type (Economy/Business):
Business Fare: $1000
Seat assigned: 12A
Concept: Implement programs using template class and functions.
9
Problem Statement: Implement a generic library for fundamental data structures such as Stack, Queue,
and Linked List using templates (C++) or generics (Java).We write a generic function that can be used
for different data types. Examples of function templates are sort(), max(), min(), printArray().
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Task:
i.   Implement a generic stack with push, pop, and peek operations.
ii.   Implement a generic queue with enqueue and dequeue operations.
iii.   Implement a generic linked list with insertion, deletion, and search functionality.
iv.   Demonstrate with different data types (integers, floating-point numbers, and user-defined types
like complex numbers).
Concept: Implement program suing generics programming
10
Problem Statement:
Implement a generic sorting utility that allows users to sort data using custom comparator functions
provided as lambda expressions.
Task:
1.   Create a Generic Sorting Class:
a.   Implement a generic function that takes an array or list and a comparator function as input.
b.   Use lambda expressions to define different sorting criteria dynamically.
2.   Implement Sorting Strategies:
a.   Allow sorting based on natural ordering (ascending/descending).
b.   Allow user-defined sorting strategies (e.g., sorting based on absolute value, even-odd priority).
3.   Demonstrate with Different Data Types:
a.   Sort integers (normal order, absolute value, even-odd priority).
b.   Sort strings (alphabetically, by length).
c.   Sort user-defined objects (e.g., Employee class based on salary, age).
Text Books:
1. Y. Daniel Liang, “Introduction to Java Programming and Data Structures, Comprehensive Version”, 12th
Edition, Pearson paperback, 2024.
2. E. Balagurusamy, “Object Oriented Programming with C++”, 8th Edition, McGraw Hill, 2020.
Reference Books:
1. Dimitri Nesteruk, “Design Patterns in Modern C++20: Reusable Approaches for Object-Oriented Software
Design” 2nd Edition, Apress, 2022.
2. Maurice Naftalin, Philip Wadler, “Java Generics and Collections: Fundamentals and Recommended
Practices”, O'Reilly Media, Inc., 2nd Edition, 2025.
3. Bjarne Stroustrup, “The C++ Programming Language”, 4th Edition, Addison Wesley, Pearson Education,
2022.
4. Herbert Schildt, “Java 2: The Complete Reference”, 5th Edition, McGraw-Hill Education, 2017.
The list which is provided in the syllabus is guideline to conduct the practical sessions. The faculty can create
more practical examples suitable to given concepts in each experiment.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Program: B Tech (CE, IT, CSBS)   Semester: III
MBA Tech (CE, IT)
````

## B TECH · Data Science · AY 2025-26 · Sem 1

- Course as printed: Object Oriented Programming Lab
- Source: `00_Original_Downloads/SYLLABUS/B TECH/11716__1ST YEAR.zip :: DATA SCIENCE/SEM II/B_Tech_(All_Program_Except_CSBS__CSDS_311__1st_Year__Sem_II__A_Y_2025-26_nTLGYhtNZd.pdf`, page 28-34

````text
Program: B Tech and MBA Tech All Programs   Semester: I/II
Course: Object Oriented Programming Lab   Code:
Teaching Scheme   Evaluation Scheme
Lecture   Tutorial
Practical   Internal Continuous   Term End Examinations
(Hours per   (Hours per
(Hours per   Credit   Assessment (ICA) (Marks -   (TEE)
week)   week)
week)   50)   (Marks- 50 )
0   2   0   1   Marks Scaled to 50   (Practical Examination)
Marks Scaled to 50
Prerequisite: Computational Thinking for Problem Solving
Course Objective
This course aims to help students understand the object-oriented paradigm and its application in designing and
developing solutions to engineering/industry problems.
Course Outcomes- After completion of the course, students will be able to -
1.   Implement basic programs using classes, objects (K3),
2.   Design solutions with class diagrams and implementing polymorphism, and inheritance (K3),
3.   Implement programs using exception handling and files (K3),
4.   Implement programs using abstract classes, and interfaces (K3),
5.   Design solutions using generics programming and design patterns for real-world problems (K3).
List of Experiments
Exp.   Programming Topic
No.
1.   Concept: Implement a program using classes, objects, data members and member functions.
Problem Statement: Create a class “Employee” to read and print information about an employee with
the following data members:
Name of the employee,
ID of the employee,
Department of the employee,
Basic salary.
Task: Perform the following functions to complete the operations:
1.   Write a member function read_Employee() to initialize the object.
2.   Write a member function to Calculate Gross salary and its components (declare them as data
members) based on the following conditions:
Signature
(Head of the Department )   AY 2025-26
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Dearness allowance (DA) = 50 % of basic salary
HRA = 30 % basic salary
TA = 10 % basic salary
Gross Salary = basic salary + DA + HRA + TA.
3.   Write a member function to display employee details with Gross Salary and all other
components.
2.   Concepts: Implement a program using Encapsulation, Abstractions and Array of Objects.
Problem Statement: A school is developing Library Management system to maintain the records of the
books. Where it performs basic operations such as making entry of the book, searching the book by book
name and author name. It also shows availability of the books.
Task:
Create class to manage the books in “Library” with following data members and functions.
Name of the book
Author of the book
Price of the book
No. of copies
Implement member functions to perform the following operations:
Read the data of 5 books – include books in the library.
Display the data of books – print the list of all the books in the library.
Search the specified book in the Library by name, if it is available or not, if available then display no of
copies of the book.
Search the specified book in the Library by Author Name, display all the books of the same author.
3   Concept: Implement a program using the concepts of constructor to initialize the object.
Problem Statement: A customer can open account in the bank with following attributes. A customer can
performs basic operations with the account created using class called “Bank Account”.
Customer Name
Address
Account Number
Age
Balance Amount
Task: Implement following functions to perform operations with an account:
1.   Use the parameterized constructor to initialize the array of objects.
2.   Write a function to withdraw amount after checking account no.
3.   Write a function to deposit amount after checking account no.
Signature
(Head of the Department )   AY 2025-26
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
4.   Write a function to display balance amount after checking account no.
5.   Write a function to display the Customer Profile.
4.   Concept: Implement a program using Inheritance, Runtime polymorphism and Modelling classes.
Problem Statement: A bank want to extend two more insurance services to their customers along with
basic bank operations performed using “Saving Bank Account”. These two additional services will be
implemented without changing existing bank account class. So, two additional classes are created by
deriving features from the “Bank Account”. These classes are name as “Life Insurance” and “Car
Insurance”. Premium of both the insurance policies are linked to bank account of the customer so that it
can be directly deducted from their saving account and current balance will be displayed after every
deduction. Features derived from the base classes are shown in the following diagram. The “Claim” class
is used to settle the claim amount and deposited in the respective saving bank account.
Note: Use Bank Account class created in the experiment 3 as base class in the hierarchy.
Data Members:   Members Functions:
Name of the   Open account
customer   Bank Account   Withdraw
Address Age   (Base Class)   Display Customer Deposit Details
Saving Account No   Display Balance
Balance
Data Members:   Data Members:
Policy No   Policy No
Sum Assured   Car Details
Premium   Premium
Term (No of Years)   Car   Duration
Life Insurance   Insurance
Members Functions:   (Derived Class)   (Derived Class)   Members Read Functions: data
Read data   Calculate premium
Calculate premium   Deduct premium
Deduct premium   (from saving)
(from saving annually   Display Information
and Term by 1).   Derived Data
Display Information   Members:
Policy No   Members Functions:
Sum Assured   Claim   Settlement Amount.
Premium   (Term or Car)
Term (No of Years)   Deposit amount in
Car details   (Derived   saving acc.
Premium   Class)   Display Information
Duration
Inheritance
Task:
Signature
(Head of the Department )   AY 2025-26
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Implement member functions to perform the task: calculation of premium and deduction from the bank
account.
Life Insurance Class: Derived from Bank Account class
A.   Calculate Premium for Life insurance: use following conditions
1.   If age of a person is below 25 years - 3 K / Year / Lakh. (Sum Assured)
2.   If age of a person is in between 26 to 45 years – 4 K /year/ Lakh
3.   If age of a person is in between 46 to 60 years – 5 K /year/ Lakh
4.   If age > 60 – no insurance.
Car Insurance Class: Derived from Bank Account class
B.   Calculate Premium for car insurance: Use following conditions
1.   If Car is new then – 5 K / Year / Lakh (8 L)
2.   If Car is between 2 – 4 Year old – 3 K/ Year / Lakh
3.   If Car is between 5 – 7 Year old – 2 K/ Year / Lakh
Claim class: Derived from Life Insurance and Car Insurance
Function: Settlement () - will calculate the amount depending on the status of the policy
1.   Life insurance:
a.   If policy closed within first 5 years – Zero amount
b.   If policy closed between 6 – 12 years – 25 % of sum assured
c.   If policy closed between 13-20 years – 50 % of sum assured + 20 % of sum assured as bonus
d.   If policy closed after 20 years – sum assured + 100 % of sum assured as bonus
Deposit this amount to saving account
2.   Car Insurance:
a.   Amount spent by customer on repairing of Car.
Deposit this amount to saving account
Concept: Implement programs using exception handling
5
Problem Statements 1:
Write a program that takes two integers as input from the user and performs division. Handle the
division_by_zero error if the denominator is zero and display an appropriate message.
Problem Statements 2:
Create a method check_Eligibility(int age) that checks if a person is eligible to vote (age >= 18). If the age
is less than 18, the method should throw an Exception. Use the throws keyword to indicate that this
method can throw an exception.
Problem Statements 3:
Create a user-defined exception InsufficientBalanceException. Write a program where a user enters the
withdrawal amount. If the balance is less than the withdrawal amount, throw the custom exception.
Note: Consider the class “Bank_Account” created in the assignment 3 to demonstrate the withdrawal.
Signature
(Head of the Department )   AY 2025-26
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
6   Concept: Implement programs to handle data with external files.
Task1:
1.   Write a program to copy an image file from one location to another using byte-oriented streams.
Task2:
2.   Write a program to read a text file, and write a function to count the number of words in it.
3.   Write a function to search for the specific word. Use Buffer for efficient reading.
Concept: Implement programs to demonstrate the use of inner classes
7   Problem Statement: A smart home system has multiple devices, such as lights and fans, controlled by a
remote. Each remote has a power button to toggle the device on or off.
Task:
Create a class SmartHome that contains an inner class RemoteControl.
RemoteControl should have a method toggleDevice() that switches the device state (ON/OFF).
Simulate controlling a device using the inner class.
Expected outcome:
Device is currently OFF
Turning ON the device...
Device is now ON
Concept: Implement programs using abstract class and Interfaces
8   Problem Statement: An airline reservation system allows users to book economy and business class
tickets. The fare calculation and seat allocation process differs based on the ticket type.
Task:
Create an abstract class Flight with an abstract method calculateFare().
Implement subclasses EconomyClass and BusinessClass that override calculateFare().
Create an interface SeatAllocation with a method assignSeat().
Implement SeatAllocation in both subclasses to assign seat numbers.
Expected Outcome:
Enter ticket type (Economy/Business):
Business Fare: $1000
Seat assigned: 12A
Concept: Implement programs using template class and functions.
9
Problem Statement: Implement a generic library for fundamental data structures such as Stack, Queue,
and Linked List using templates (C++) or generics (Java).We write a generic function that can be used
for different data types. Examples of function templates are sort(), max(), min(), printArray().
Signature
(Head of the Department )   AY 2025-26
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Task:
i.   Implement a generic stack with push, pop, and peek operations.
ii.   Implement a generic queue with enqueue and dequeue operations.
iii.   Implement a generic linked list with insertion, deletion, and search functionality.
iv.   Demonstrate with different data types (integers, floating-point numbers, and user-defined types
like complex numbers).
Concept: Implement program suing generics programming
10
Problem Statement:
Implement a generic sorting utility that allows users to sort data using custom comparator functions
provided as lambda expressions.
Task:
1.   Create a Generic Sorting Class:
a.   Implement a generic function that takes an array or list and a comparator function as input.
b.   Use lambda expressions to define different sorting criteria dynamically.
2.   Implement Sorting Strategies:
a.   Allow sorting based on natural ordering (ascending/descending).
b.   Allow user-defined sorting strategies (e.g., sorting based on absolute value, even-odd priority).
3.   Demonstrate with Different Data Types:
a.   Sort integers (normal order, absolute value, even-odd priority).
b.   Sort strings (alphabetically, by length).
c.   Sort user-defined objects (e.g., Employee class based on salary, age).
Text Books:
1. Y. Daniel Liang, “Introduction to Java Programming and Data Structures, Comprehensive Version”, 12th
Edition, Pearson paperback, 2024.
2. E. Balagurusamy, “Object Oriented Programming with C++”, 8th Edition, McGraw Hill, 2020.
Reference Books:
1. Dimitri Nesteruk, “Design Patterns in Modern C++20: Reusable Approaches for Object-Oriented Software
Design” 2nd Edition, Apress, 2022.
2. Maurice Naftalin, Philip Wadler, “Java Generics and Collections: Fundamentals and Recommended
Practices”, O'Reilly Media, Inc., 2nd Edition, 2025.
3. Bjarne Stroustrup, “The C++ Programming Language”, 4th Edition, Addison Wesley, Pearson Education,
2022.
4. Herbert Schildt, “Java 2: The Complete Reference”, 5th Edition, McGraw-Hill Education, 2017.
The list which is provided in the syllabus is guideline to conduct the practical sessions. The faculty can create
more practical examples suitable to given concepts in each experiment.
Signature
(Head of the Department )   AY 2025-26
SVKM’s Narsee Monjee Institute of Management Studies
Mukesh Patel School of Technology Management & Engineering
Program: B Tech / MBA Tech (All Program)   Semester: I /II
````

## MBA Tech · Artificial Intelligence · batch 2025-2030 · Sem 1

- Course as printed: Object Oriented Programming Lab (code 702CO0C064)
- Source: `04_Syllabi_Archive/MBA Tech/ARTIFICIAL INTELLIGENCE/BATCH (2025-2030)/Syllabus/Semester 3.pdf`, page 18-24

````text
Program: B Tech (CE, DS, AI, AIML, AIDS, IT, CSECS, CSEDS, CSBS, Semester: I/II/III/IV
CS)
MBA Tech (CE, IT, DS, AI)
Course: Object Oriented Programming Lab   Course Code: 702CO0C064
Teaching Scheme   Evaluation Scheme
Lecture   Tutorial
Practical   Internal Continuous   Term End Examinations
(Hours per   (Hours per
(Hours per   Credit   Assessment (ICA) (Marks -   (TEE)
week)   week)
week)   50)   (Marks- 50 )
0   2   0   1   Marks Scaled to 50   (Practical Examination)
Marks Scaled to 50
Prerequisite: Computational Thinking for Problem Solving
Course Objective
This course aims to help students understand the object-oriented paradigm and its application in designing and
developing solutions to engineering/industry problems.
Course Outcomes- After completion of the course, students will be able to -
1.   Implement basic programs using classes, objects (K3),
2.   Design solutions with class diagrams and implementing polymorphism, and inheritance (K3),
3.   Implement programs using exception handling and files (K3),
4.   Implement programs using abstract classes, and interfaces (K3),
5.   Design solutions using generics programming and design patterns for real-world problems (K3).
List of Experiments
Exp.   Programming Topic
No.
1.   Concept: Implement a program using classes, objects, data members and member functions.
Problem Statement: Create a class “Employee” to read and print information about an employee with
the following data members:
Name of the employee,
ID of the employee,
Department of the employee,
Basic salary.
Task: Perform the following functions to complete the operations:
1.   Write a member function read_Employee() to initialize the object.
2.   Write a member function to Calculate Gross salary and its components (declare them as data
members) based on the following conditions:
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Dearness allowance (DA) = 50 % of basic salary
HRA = 30 % basic salary
TA = 10 % basic salary
Gross Salary = basic salary + DA + HRA + TA.
3.   Write a member function to display employee details with Gross Salary and all other
components.
2.   Concepts: Implement a program using Encapsulation, Abstractions and Array of Objects.
Problem Statement: A school is developing Library Management system to maintain the records of the
books. Where it performs basic operations such as making entry of the book, searching the book by book
name and author name. It also shows availability of the books.
Task:
Create class to manage the books in “Library” with following data members and functions.
Name of the book
Author of the book
Price of the book
No. of copies
Implement member functions to perform the following operations:
Read the data of 5 books – include books in the library.
Display the data of books – print the list of all the books in the library.
Search the specified book in the Library by name, if it is available or not, if available then display no of
copies of the book.
Search the specified book in the Library by Author Name, display all the books of the same author.
3   Concept: Implement a program using the concepts of constructor to initialize the object.
Problem Statement: A customer can open account in the bank with following attributes. A customer can
performs basic operations with the account created using class called “Bank Account”.
Customer Name
Address
Account Number
Age
Balance Amount
Task: Implement following functions to perform operations with an account:
1.   Use the parameterized constructor to initialize the array of objects.
2.   Write a function to withdraw amount after checking account no.
3.   Write a function to deposit amount after checking account no.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
4.   Write a function to display balance amount after checking account no.
5.   Write a function to display the Customer Profile.
4.   Concept: Implement a program using Inheritance, Runtime polymorphism and Modelling classes.
Problem Statement: A bank want to extend two more insurance services to their customers along with
basic bank operations performed using “Saving Bank Account”. These two additional services will be
implemented without changing existing bank account class. So, two additional classes are created by
deriving features from the “Bank Account”. These classes are name as “Life Insurance” and “Car
Insurance”. Premium of both the insurance policies are linked to bank account of the customer so that it
can be directly deducted from their saving account and current balance will be displayed after every
deduction. Features derived from the base classes are shown in the following diagram. The “Claim” class
is used to settle the claim amount and deposited in the respective saving bank account.
Note: Use Bank Account class created in the experiment 3 as base class in the hierarchy.
Data Members:   Members Functions:
Name of the   Open account
customer   Bank Account   Withdraw
Address Age   (Base Class)   Display Customer Deposit Details
Saving Account No   Display Balance
Balance
Data Members:   Data Members:
Policy No   Policy No
Sum Assured   Car Details
Premium   Premium
Term (No of Years)   Car   Duration
Life Insurance   Insurance
Members Functions:   (Derived Class)   (Derived Class)   Members Read Functions: data
Read data   Calculate premium
Calculate premium   Deduct premium
Deduct premium   (from saving)
(from saving annually   Display Information
and Term by 1).   Derived Data
Display Information   Members:
Policy No   Members Functions:
Sum Assured   Claim   Settlement Amount.
Premium   (Term or Car)
Term (No of Years)   Deposit amount in
Car details   (Derived   saving acc.
Premium   Class)   Display Information
Duration
Inheritance
Task:
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Implement member functions to perform the task: calculation of premium and deduction from the bank
account.
Life Insurance Class: Derived from Bank Account class
A.   Calculate Premium for Life insurance: use following conditions
1.   If age of a person is below 25 years - 3 K / Year / Lakh. (Sum Assured)
2.   If age of a person is in between 26 to 45 years – 4 K /year/ Lakh
3.   If age of a person is in between 46 to 60 years – 5 K /year/ Lakh
4.   If age > 60 – no insurance.
Car Insurance Class: Derived from Bank Account class
B.   Calculate Premium for car insurance: Use following conditions
1.   If Car is new then – 5 K / Year / Lakh (8 L)
2.   If Car is between 2 – 4 Year old – 3 K/ Year / Lakh
3.   If Car is between 5 – 7 Year old – 2 K/ Year / Lakh
Claim class: Derived from Life Insurance and Car Insurance
Function: Settlement () - will calculate the amount depending on the status of the policy
1.   Life insurance:
a.   If policy closed within first 5 years – Zero amount
b.   If policy closed between 6 – 12 years – 25 % of sum assured
c.   If policy closed between 13-20 years – 50 % of sum assured + 20 % of sum assured as bonus
d.   If policy closed after 20 years – sum assured + 100 % of sum assured as bonus
Deposit this amount to saving account
2.   Car Insurance:
a.   Amount spent by customer on repairing of Car.
Deposit this amount to saving account
Concept: Implement programs using exception handling
5
Problem Statements 1:
Write a program that takes two integers as input from the user and performs division. Handle the
division_by_zero error if the denominator is zero and display an appropriate message.
Problem Statements 2:
Create a method check_Eligibility(int age) that checks if a person is eligible to vote (age >= 18). If the age
is less than 18, the method should throw an Exception. Use the throws keyword to indicate that this
method can throw an exception.
Problem Statements 3:
Create a user-defined exception InsufficientBalanceException. Write a program where a user enters the
withdrawal amount. If the balance is less than the withdrawal amount, throw the custom exception.
Note: Consider the class “Bank_Account” created in the assignment 3 to demonstrate the withdrawal.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
6   Concept: Implement programs to handle data with external files.
Task1:
1.   Write a program to copy an image file from one location to another using byte-oriented streams.
Task2:
2.   Write a program to read a text file, and write a function to count the number of words in it.
3.   Write a function to search for the specific word. Use Buffer for efficient reading.
Concept: Implement programs to demonstrate the use of inner classes
7   Problem Statement: A smart home system has multiple devices, such as lights and fans, controlled by a
remote. Each remote has a power button to toggle the device on or off.
Task:
Create a class SmartHome that contains an inner class RemoteControl.
RemoteControl should have a method toggleDevice() that switches the device state (ON/OFF).
Simulate controlling a device using the inner class.
Expected outcome:
Device is currently OFF
Turning ON the device...
Device is now ON
Concept: Implement programs using abstract class and Interfaces
8   Problem Statement: An airline reservation system allows users to book economy and business class
tickets. The fare calculation and seat allocation process differs based on the ticket type.
Task:
Create an abstract class Flight with an abstract method calculateFare().
Implement subclasses EconomyClass and BusinessClass that override calculateFare().
Create an interface SeatAllocation with a method assignSeat().
Implement SeatAllocation in both subclasses to assign seat numbers.
Expected Outcome:
Enter ticket type (Economy/Business):
Business Fare: $1000
Seat assigned: 12A
Concept: Implement programs using template class and functions.
9
Problem Statement: Implement a generic library for fundamental data structures such as Stack, Queue,
and Linked List using templates (C++) or generics (Java).We write a generic function that can be used
for different data types. Examples of function templates are sort(), max(), min(), printArray().
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Task:
i.   Implement a generic stack with push, pop, and peek operations.
ii.   Implement a generic queue with enqueue and dequeue operations.
iii.   Implement a generic linked list with insertion, deletion, and search functionality.
iv.   Demonstrate with different data types (integers, floating-point numbers, and user-defined types
like complex numbers).
Concept: Implement program suing generics programming
10
Problem Statement:
Implement a generic sorting utility that allows users to sort data using custom comparator functions
provided as lambda expressions.
Task:
1.   Create a Generic Sorting Class:
a.   Implement a generic function that takes an array or list and a comparator function as input.
b.   Use lambda expressions to define different sorting criteria dynamically.
2.   Implement Sorting Strategies:
a.   Allow sorting based on natural ordering (ascending/descending).
b.   Allow user-defined sorting strategies (e.g., sorting based on absolute value, even-odd priority).
3.   Demonstrate with Different Data Types:
a.   Sort integers (normal order, absolute value, even-odd priority).
b.   Sort strings (alphabetically, by length).
c.   Sort user-defined objects (e.g., Employee class based on salary, age).
Text Books:
1. Y. Daniel Liang, “Introduction to Java Programming and Data Structures, Comprehensive Version”, 12th
Edition, Pearson paperback, 2024.
2. E. Balagurusamy, “Object Oriented Programming with C++”, 8th Edition, McGraw Hill, 2020.
Reference Books:
1. Dimitri Nesteruk, “Design Patterns in Modern C++20: Reusable Approaches for Object-Oriented Software
Design” 2nd Edition, Apress, 2022.
2. Maurice Naftalin, Philip Wadler, “Java Generics and Collections: Fundamentals and Recommended
Practices”, O'Reilly Media, Inc., 2nd Edition, 2025.
3. Bjarne Stroustrup, “The C++ Programming Language”, 4th Edition, Addison Wesley, Pearson Education,
2022.
4. Herbert Schildt, “Java 2: The Complete Reference”, 5th Edition, McGraw-Hill Education, 2017.
The list which is provided in the syllabus is guideline to conduct the practical sessions. The faculty can create
more practical examples suitable to given concepts in each experiment.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Program: B Tech (CE, DS, AI, AIML, AIDS, IT, CSECS, CSEDS, CSBS, Semester: III
CS)
MBA Tech (CE, IT, DS, AI)
````

## MBA Tech · Data Science · batch 2025-2030 · Sem 1

- Course as printed: Object Oriented Programming Lab (code 702CO0C064)
- Source: `04_Syllabi_Archive/MBA Tech/DATA SCIENCE/BATCH (2025-2030)/Syllabus/Semester 3.pdf`, page 26-32

````text
Program: B Tech (CE, DS, AI, AIML, AIDS, IT, CSECS, CSEDS, CSBS, Semester: I/II/III/IV
CS)
MBA Tech (CE, IT, DS, AI)
Course: Object Oriented Programming Lab   Course Code: 702CO0C064
Teaching Scheme   Evaluation Scheme
Lecture   Tutorial
Practical   Internal Continuous   Term End Examinations
(Hours per   (Hours per
(Hours per   Credit   Assessment (ICA) (Marks -   (TEE)
week)   week)
week)   50)   (Marks- 50 )
0   2   0   1   Marks Scaled to 50   (Practical Examination)
Marks Scaled to 50
Prerequisite: Computational Thinking for Problem Solving
Course Objective
This course aims to help students understand the object-oriented paradigm and its application in designing and
developing solutions to engineering/industry problems.
Course Outcomes- After completion of the course, students will be able to -
1.   Implement basic programs using classes, objects (K3),
2.   Design solutions with class diagrams and implementing polymorphism, and inheritance (K3),
3.   Implement programs using exception handling and files (K3),
4.   Implement programs using abstract classes, and interfaces (K3),
5.   Design solutions using generics programming and design patterns for real-world problems (K3).
List of Experiments
Exp.   Programming Topic
No.
1.   Concept: Implement a program using classes, objects, data members and member functions.
Problem Statement: Create a class “Employee” to read and print information about an employee with
the following data members:
Name of the employee,
ID of the employee,
Department of the employee,
Basic salary.
Task: Perform the following functions to complete the operations:
1.   Write a member function read_Employee() to initialize the object.
2.   Write a member function to Calculate Gross salary and its components (declare them as data
members) based on the following conditions:
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Dearness allowance (DA) = 50 % of basic salary
HRA = 30 % basic salary
TA = 10 % basic salary
Gross Salary = basic salary + DA + HRA + TA.
3.   Write a member function to display employee details with Gross Salary and all other
components.
2.   Concepts: Implement a program using Encapsulation, Abstractions and Array of Objects.
Problem Statement: A school is developing Library Management system to maintain the records of the
books. Where it performs basic operations such as making entry of the book, searching the book by book
name and author name. It also shows availability of the books.
Task:
Create class to manage the books in “Library” with following data members and functions.
Name of the book
Author of the book
Price of the book
No. of copies
Implement member functions to perform the following operations:
Read the data of 5 books – include books in the library.
Display the data of books – print the list of all the books in the library.
Search the specified book in the Library by name, if it is available or not, if available then display no of
copies of the book.
Search the specified book in the Library by Author Name, display all the books of the same author.
3   Concept: Implement a program using the concepts of constructor to initialize the object.
Problem Statement: A customer can open account in the bank with following attributes. A customer can
performs basic operations with the account created using class called “Bank Account”.
Customer Name
Address
Account Number
Age
Balance Amount
Task: Implement following functions to perform operations with an account:
1.   Use the parameterized constructor to initialize the array of objects.
2.   Write a function to withdraw amount after checking account no.
3.   Write a function to deposit amount after checking account no.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
4.   Write a function to display balance amount after checking account no.
5.   Write a function to display the Customer Profile.
4.   Concept: Implement a program using Inheritance, Runtime polymorphism and Modelling classes.
Problem Statement: A bank want to extend two more insurance services to their customers along with
basic bank operations performed using “Saving Bank Account”. These two additional services will be
implemented without changing existing bank account class. So, two additional classes are created by
deriving features from the “Bank Account”. These classes are name as “Life Insurance” and “Car
Insurance”. Premium of both the insurance policies are linked to bank account of the customer so that it
can be directly deducted from their saving account and current balance will be displayed after every
deduction. Features derived from the base classes are shown in the following diagram. The “Claim” class
is used to settle the claim amount and deposited in the respective saving bank account.
Note: Use Bank Account class created in the experiment 3 as base class in the hierarchy.
Data Members:   Members Functions:
Name of the   Open account
customer   Bank Account   Withdraw
Address Age   (Base Class)   Display Customer Deposit Details
Saving Account No   Display Balance
Balance
Data Members:   Data Members:
Policy No   Policy No
Sum Assured   Car Details
Premium   Premium
Term (No of Years)   Car   Duration
Life Insurance   Insurance
Members Functions:   (Derived Class)   (Derived Class)   Members Read Functions: data
Read data   Calculate premium
Calculate premium   Deduct premium
Deduct premium   (from saving)
(from saving annually   Display Information
and Term by 1).   Derived Data
Display Information   Members:
Policy No   Members Functions:
Sum Assured   Claim   Settlement Amount.
Premium   (Term or Car)
Term (No of Years)   Deposit amount in
Car details   (Derived   saving acc.
Premium   Class)   Display Information
Duration
Inheritance
Task:
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Implement member functions to perform the task: calculation of premium and deduction from the bank
account.
Life Insurance Class: Derived from Bank Account class
A.   Calculate Premium for Life insurance: use following conditions
1.   If age of a person is below 25 years - 3 K / Year / Lakh. (Sum Assured)
2.   If age of a person is in between 26 to 45 years – 4 K /year/ Lakh
3.   If age of a person is in between 46 to 60 years – 5 K /year/ Lakh
4.   If age > 60 – no insurance.
Car Insurance Class: Derived from Bank Account class
B.   Calculate Premium for car insurance: Use following conditions
1.   If Car is new then – 5 K / Year / Lakh (8 L)
2.   If Car is between 2 – 4 Year old – 3 K/ Year / Lakh
3.   If Car is between 5 – 7 Year old – 2 K/ Year / Lakh
Claim class: Derived from Life Insurance and Car Insurance
Function: Settlement () - will calculate the amount depending on the status of the policy
1.   Life insurance:
a.   If policy closed within first 5 years – Zero amount
b.   If policy closed between 6 – 12 years – 25 % of sum assured
c.   If policy closed between 13-20 years – 50 % of sum assured + 20 % of sum assured as bonus
d.   If policy closed after 20 years – sum assured + 100 % of sum assured as bonus
Deposit this amount to saving account
2.   Car Insurance:
a.   Amount spent by customer on repairing of Car.
Deposit this amount to saving account
Concept: Implement programs using exception handling
5
Problem Statements 1:
Write a program that takes two integers as input from the user and performs division. Handle the
division_by_zero error if the denominator is zero and display an appropriate message.
Problem Statements 2:
Create a method check_Eligibility(int age) that checks if a person is eligible to vote (age >= 18). If the age
is less than 18, the method should throw an Exception. Use the throws keyword to indicate that this
method can throw an exception.
Problem Statements 3:
Create a user-defined exception InsufficientBalanceException. Write a program where a user enters the
withdrawal amount. If the balance is less than the withdrawal amount, throw the custom exception.
Note: Consider the class “Bank_Account” created in the assignment 3 to demonstrate the withdrawal.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
6   Concept: Implement programs to handle data with external files.
Task1:
1.   Write a program to copy an image file from one location to another using byte-oriented streams.
Task2:
2.   Write a program to read a text file, and write a function to count the number of words in it.
3.   Write a function to search for the specific word. Use Buffer for efficient reading.
Concept: Implement programs to demonstrate the use of inner classes
7   Problem Statement: A smart home system has multiple devices, such as lights and fans, controlled by a
remote. Each remote has a power button to toggle the device on or off.
Task:
Create a class SmartHome that contains an inner class RemoteControl.
RemoteControl should have a method toggleDevice() that switches the device state (ON/OFF).
Simulate controlling a device using the inner class.
Expected outcome:
Device is currently OFF
Turning ON the device...
Device is now ON
Concept: Implement programs using abstract class and Interfaces
8   Problem Statement: An airline reservation system allows users to book economy and business class
tickets. The fare calculation and seat allocation process differs based on the ticket type.
Task:
Create an abstract class Flight with an abstract method calculateFare().
Implement subclasses EconomyClass and BusinessClass that override calculateFare().
Create an interface SeatAllocation with a method assignSeat().
Implement SeatAllocation in both subclasses to assign seat numbers.
Expected Outcome:
Enter ticket type (Economy/Business):
Business Fare: $1000
Seat assigned: 12A
Concept: Implement programs using template class and functions.
9
Problem Statement: Implement a generic library for fundamental data structures such as Stack, Queue,
and Linked List using templates (C++) or generics (Java).We write a generic function that can be used
for different data types. Examples of function templates are sort(), max(), min(), printArray().
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Task:
i.   Implement a generic stack with push, pop, and peek operations.
ii.   Implement a generic queue with enqueue and dequeue operations.
iii.   Implement a generic linked list with insertion, deletion, and search functionality.
iv.   Demonstrate with different data types (integers, floating-point numbers, and user-defined types
like complex numbers).
Concept: Implement program suing generics programming
10
Problem Statement:
Implement a generic sorting utility that allows users to sort data using custom comparator functions
provided as lambda expressions.
Task:
1.   Create a Generic Sorting Class:
a.   Implement a generic function that takes an array or list and a comparator function as input.
b.   Use lambda expressions to define different sorting criteria dynamically.
2.   Implement Sorting Strategies:
a.   Allow sorting based on natural ordering (ascending/descending).
b.   Allow user-defined sorting strategies (e.g., sorting based on absolute value, even-odd priority).
3.   Demonstrate with Different Data Types:
a.   Sort integers (normal order, absolute value, even-odd priority).
b.   Sort strings (alphabetically, by length).
c.   Sort user-defined objects (e.g., Employee class based on salary, age).
Text Books:
1. Y. Daniel Liang, “Introduction to Java Programming and Data Structures, Comprehensive Version”, 12th
Edition, Pearson paperback, 2024.
2. E. Balagurusamy, “Object Oriented Programming with C++”, 8th Edition, McGraw Hill, 2020.
Reference Books:
1. Dimitri Nesteruk, “Design Patterns in Modern C++20: Reusable Approaches for Object-Oriented Software
Design” 2nd Edition, Apress, 2022.
2. Maurice Naftalin, Philip Wadler, “Java Generics and Collections: Fundamentals and Recommended
Practices”, O'Reilly Media, Inc., 2nd Edition, 2025.
3. Bjarne Stroustrup, “The C++ Programming Language”, 4th Edition, Addison Wesley, Pearson Education,
2022.
4. Herbert Schildt, “Java 2: The Complete Reference”, 5th Edition, McGraw-Hill Education, 2017.
The list which is provided in the syllabus is guideline to conduct the practical sessions. The faculty can create
more practical examples suitable to given concepts in each experiment.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS
Mukesh Patel School of Technology Management and Engineering
Technology Management Department
Program: MBA Tech / B Tech (All Programs)   Semester: III / IV
````

## B TECH INTEGRATED · Data Science · batch 2023-2029 · Sem 7

- Course as printed: Object Oriented Programming Lab (code 701CO0C026)
- Source: `04_Syllabi_Archive/B TECH INTEGRATED/Data Science/Batch ( 2023 To 2029 )/Semester - 7.pdf`, page 27-33

````text
Program: B Tech Integrated (IT, DS)   Semester: VII
Course: Object Oriented Programming Lab   Course Code: 701CO0C026
Teaching Scheme   Evaluation Scheme
Lecture   Tutorial
Practical   Internal Continuous   Term End Examinations
(Hours per   (Hours per
(Hours per   Credit   Assessment (ICA) (Marks -   (TEE)
week)   week)
week)   50)   (Marks- 50 )
0   2   0   1   Marks Scaled to 50   (Practical Examination)
Marks Scaled to 50
Prerequisite: Computational Thinking for Problem Solving
Course Objective
This course aims to help students understand the object-oriented paradigm and its application in designing and
developing solutions to engineering/industry problems.
Course Outcomes- After completion of the course, students will be able to -
1.   Implement basic programs using classes, objects (K3),
2.   Design solutions with class diagrams and implementing polymorphism, and inheritance (K3),
3.   Implement programs using exception handling and files (K3),
4.   Implement programs using abstract classes, and interfaces (K3),
5.   Design solutions using generics programming and design patterns for real-world problems (K3).
List of Experiments
Exp.   Programming Topic
No.
1.   Concept: Implement a program using classes, objects, data members and member functions.
Problem Statement: Create a class “Employee” to read and print information about an employee with
the following data members:
Name of the employee,
ID of the employee,
Department of the employee,
Basic salary.
Task: Perform the following functions to complete the operations:
1.   Write a member function read_Employee() to initialize the object.
2.   Write a member function to Calculate Gross salary and its components (declare them as data
members) based on the following conditions:
Dearness allowance (DA) = 50 % of basic salary
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
HRA = 30 % basic salary
TA = 10 % basic salary
Gross Salary = basic salary + DA + HRA + TA.
3.   Write a member function to display employee details with Gross Salary and all other
components.
2.   Concepts: Implement a program using Encapsulation, Abstractions and Array of Objects.
Problem Statement: A school is developing Library Management system to maintain the records of the
books. Where it performs basic operations such as making entry of the book, searching the book by book
name and author name. It also shows availability of the books.
Task:
Create class to manage the books in “Library” with following data members and functions.
Name of the book
Author of the book
Price of the book
No. of copies
Implement member functions to perform the following operations:
Read the data of 5 books – include books in the library.
Display the data of books – print the list of all the books in the library.
Search the specified book in the Library by name, if it is available or not, if available then display no of
copies of the book.
Search the specified book in the Library by Author Name, display all the books of the same author.
3   Concept: Implement a program using the concepts of constructor to initialize the object.
Problem Statement: A customer can open account in the bank with following attributes. A customer can
performs basic operations with the account created using class called “Bank Account”.
Customer Name
Address
Account Number
Age
Balance Amount
Task: Implement following functions to perform operations with an account:
1.   Use the parameterized constructor to initialize the array of objects.
2.   Write a function to withdraw amount after checking account no.
3.   Write a function to deposit amount after checking account no.
4.   Write a function to display balance amount after checking account no.
5.   Write a function to display the Customer Profile.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
4.   Concept: Implement a program using Inheritance, Runtime polymorphism and Modelling classes.
Problem Statement: A bank want to extend two more insurance services to their customers along with
basic bank operations performed using “Saving Bank Account”. These two additional services will be
implemented without changing existing bank account class. So, two additional classes are created by
deriving features from the “Bank Account”. These classes are name as “Life Insurance” and “Car
Insurance”. Premium of both the insurance policies are linked to bank account of the customer so that it
can be directly deducted from their saving account and current balance will be displayed after every
deduction. Features derived from the base classes are shown in the following diagram. The “Claim” class
is used to settle the claim amount and deposited in the respective saving bank account.
Note: Use Bank Account class created in the experiment 3 as base class in the hierarchy.
Data Members:   Members Functions:
Name of the   Open account
customer   Bank Account   Withdraw
Address   (Base Class)   Deposit
Age   Display Customer Details
Saving Account No   Display Balance
Balance
Data Members:   Data Members:
Policy No   Policy No
Sum Assured   Car Details
Premium   Premium
Term (No of Years)   Car   Duration
Life Insurance   Insurance
Members Functions:   (Derived Class)   (Derived Class)   Members Read Functions: data
Read data   Calculate premium
Calculate premium   Deduct premium
Deduct premium   (from saving)
(from saving annually   Display Information
and Term by 1).   Derived Data
Display Information   Members:
Policy No   Members Functions:
Sum Assured   Claim   Settlement Amount.
Premium   (Term or Car)
Term (No of Years)   Deposit amount in
Car details   (Derived   saving acc.
Premium   Class)   Display Information
Duration
Inheritance
Task:
Implement member functions to perform the task: calculation of premium and deduction from the bank
account.
Life Insurance Class: Derived from Bank Account class
A.   Calculate Premium for Life insurance: use following conditions
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
1.   If age of a person is below 25 years - 3 K / Year / Lakh. (Sum Assured)
2.   If age of a person is in between 26 to 45 years – 4 K /year/ Lakh
3.   If age of a person is in between 46 to 60 years – 5 K /year/ Lakh
4.   If age > 60 – no insurance.
Car Insurance Class: Derived from Bank Account class
B.   Calculate Premium for car insurance: Use following conditions
1.   If Car is new then – 5 K / Year / Lakh (8 L)
2.   If Car is between 2 – 4 Year old – 3 K/ Year / Lakh
3.   If Car is between 5 – 7 Year old – 2 K/ Year / Lakh
Claim class: Derived from Life Insurance and Car Insurance
Function: Settlement () - will calculate the amount depending on the status of the policy
1.   Life insurance:
a.   If policy closed within first 5 years – Zero amount
b.   If policy closed between 6 – 12 years – 25 % of sum assured
c.   If policy closed between 13-20 years – 50 % of sum assured + 20 % of sum assured as bonus
d.   If policy closed after 20 years – sum assured + 100 % of sum assured as bonus
Deposit this amount to saving account
2.   Car Insurance:
a.   Amount spent by customer on repairing of Car.
Deposit this amount to saving account
Concept: Implement programs using exception handling
5
Problem Statements 1:
Write a program that takes two integers as input from the user and performs division. Handle the
division_by_zero error if the denominator is zero and display an appropriate message.
Problem Statements 2:
Create a method check_Eligibility(int age) that checks if a person is eligible to vote (age >= 18). If the age
is less than 18, the method should throw an Exception. Use the throws keyword to indicate that this
method can throw an exception.
Problem Statements 3:
Create a user-defined exception InsufficientBalanceException. Write a program where a user enters the
withdrawal amount. If the balance is less than the withdrawal amount, throw the custom exception.
Note: Consider the class “Bank_Account” created in the assignment 3 to demonstrate the withdrawal.
6   Concept: Implement programs to handle data with external files.
Task1:
1.   Write a program to copy an image file from one location to another using byte-oriented streams.
Task2:
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
2.   Write a program to read a text file, and write a function to count the number of words in it.
3.   Write a function to search for the specific word. Use Buffer for efficient reading.
Concept: Implement programs to demonstrate the use of inner classes
7   Problem Statement: A smart home system has multiple devices, such as lights and fans, controlled by a
remote. Each remote has a power button to toggle the device on or off.
Task:
Create a class SmartHome that contains an inner class RemoteControl.
RemoteControl should have a method toggleDevice() that switches the device state (ON/OFF).
Simulate controlling a device using the inner class.
Expected outcome:
Device is currently OFF
Turning ON the device...
Device is now ON
Concept: Implement programs using abstract class and Interfaces
8   Problem Statement: An airline reservation system allows users to book economy and business class
tickets. The fare calculation and seat allocation process differs based on the ticket type.
Task:
Create an abstract class Flight with an abstract method calculateFare().
Implement subclasses EconomyClass and BusinessClass that override calculateFare().
Create an interface SeatAllocation with a method assignSeat().
Implement SeatAllocation in both subclasses to assign seat numbers.
Expected Outcome:
Enter ticket type (Economy/Business):
Business Fare: $1000
Seat assigned: 12A
Concept: Implement programs using template class and functions.
9
Problem Statement: Implement a generic library for fundamental data structures such as Stack, Queue,
and Linked List using templates (C++) or generics (Java).We write a generic function that can be used
for different data types. Examples of function templates are sort(), max(), min(), printArray().
Task:
i.   Implement a generic stack with push, pop, and peek operations.
ii.   Implement a generic queue with enqueue and dequeue operations.
iii.   Implement a generic linked list with insertion, deletion, and search functionality.
iv.   Demonstrate with different data types (integers, floating-point numbers, and user-defined types
like complex numbers).
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Concept: Implement program suing generics programming
10
Problem Statement:
Implement a generic sorting utility that allows users to sort data using custom comparator functions
provided as lambda expressions.
Task:
1.   Create a Generic Sorting Class:
a.   Implement a generic function that takes an array or list and a comparator function as input.
b.   Use lambda expressions to define different sorting criteria dynamically.
2.   Implement Sorting Strategies:
a.   Allow sorting based on natural ordering (ascending/descending).
b.   Allow user-defined sorting strategies (e.g., sorting based on absolute value, even-odd priority).
3.   Demonstrate with Different Data Types:
a.   Sort integers (normal order, absolute value, even-odd priority).
b.   Sort strings (alphabetically, by length).
c.   Sort user-defined objects (e.g., Employee class based on salary, age).
Text Books:
1. Y. Daniel Liang, “Introduction to Java Programming and Data Structures, Comprehensive Version”, 12th
Edition, Pearson paperback, 2024.
2. E. Balagurusamy, “Object Oriented Programming with C++”, 8th Edition, McGraw Hill, 2020.
Reference Books:
1. Dimitri Nesteruk, “Design Patterns in Modern C++20: Reusable Approaches for Object-Oriented Software
Design” 2nd Edition, Apress, 2022.
2. Maurice Naftalin, Philip Wadler, “Java Generics and Collections: Fundamentals and Recommended
Practices”, O'Reilly Media, Inc., 2nd Edition, 2025.
3. Bjarne Stroustrup, “The C++ Programming Language”, 4th Edition, Addison Wesley, Pearson Education,
2022.
4. Herbert Schildt, “Java 2: The Complete Reference”, 5th Edition, McGraw-Hill Education, 2017.
The list which is provided in the syllabus is guideline to conduct the practical sessions. The faculty can create
more practical examples suitable to given concepts in each experiment.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management & Engineering
Program: B Tech Integrated All Programs   Semester: VII /VIII
````

## B TECH INTEGRATED · Information Technology · batch 2023-2029 · Sem 7

- Course as printed: Object Oriented Programming Lab (code 701CO0C026)
- Source: `04_Syllabi_Archive/B TECH INTEGRATED/IT/Batch ( 2023 To 2029 )/Semester - 7.pdf`, page 10-16

````text
Program: B Tech Integrated (IT, DS)   Semester: VII
Course: Object Oriented Programming Lab   Course Code: 701CO0C026
Teaching Scheme   Evaluation Scheme
Lecture   Tutorial
Practical   Internal Continuous   Term End Examinations
(Hours per   (Hours per
(Hours per   Credit   Assessment (ICA) (Marks -   (TEE)
week)   week)
week)   50)   (Marks- 50 )
0   2   0   1   Marks Scaled to 50   (Practical Examination)
Marks Scaled to 50
Prerequisite: Computational Thinking for Problem Solving
Course Objective
This course aims to help students understand the object-oriented paradigm and its application in designing and
developing solutions to engineering/industry problems.
Course Outcomes- After completion of the course, students will be able to -
1.   Implement basic programs using classes, objects (K3),
2.   Design solutions with class diagrams and implementing polymorphism, and inheritance (K3),
3.   Implement programs using exception handling and files (K3),
4.   Implement programs using abstract classes, and interfaces (K3),
5.   Design solutions using generics programming and design patterns for real-world problems (K3).
List of Experiments
Exp.   Programming Topic
No.
1.   Concept: Implement a program using classes, objects, data members and member functions.
Problem Statement: Create a class “Employee” to read and print information about an employee with
the following data members:
Name of the employee,
ID of the employee,
Department of the employee,
Basic salary.
Task: Perform the following functions to complete the operations:
1.   Write a member function read_Employee() to initialize the object.
2.   Write a member function to Calculate Gross salary and its components (declare them as data
members) based on the following conditions:
Dearness allowance (DA) = 50 % of basic salary
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
HRA = 30 % basic salary
TA = 10 % basic salary
Gross Salary = basic salary + DA + HRA + TA.
3.   Write a member function to display employee details with Gross Salary and all other
components.
2.   Concepts: Implement a program using Encapsulation, Abstractions and Array of Objects.
Problem Statement: A school is developing Library Management system to maintain the records of the
books. Where it performs basic operations such as making entry of the book, searching the book by book
name and author name. It also shows availability of the books.
Task:
Create class to manage the books in “Library” with following data members and functions.
Name of the book
Author of the book
Price of the book
No. of copies
Implement member functions to perform the following operations:
Read the data of 5 books – include books in the library.
Display the data of books – print the list of all the books in the library.
Search the specified book in the Library by name, if it is available or not, if available then display no of
copies of the book.
Search the specified book in the Library by Author Name, display all the books of the same author.
3   Concept: Implement a program using the concepts of constructor to initialize the object.
Problem Statement: A customer can open account in the bank with following attributes. A customer can
performs basic operations with the account created using class called “Bank Account”.
Customer Name
Address
Account Number
Age
Balance Amount
Task: Implement following functions to perform operations with an account:
1.   Use the parameterized constructor to initialize the array of objects.
2.   Write a function to withdraw amount after checking account no.
3.   Write a function to deposit amount after checking account no.
4.   Write a function to display balance amount after checking account no.
5.   Write a function to display the Customer Profile.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
4.   Concept: Implement a program using Inheritance, Runtime polymorphism and Modelling classes.
Problem Statement: A bank want to extend two more insurance services to their customers along with
basic bank operations performed using “Saving Bank Account”. These two additional services will be
implemented without changing existing bank account class. So, two additional classes are created by
deriving features from the “Bank Account”. These classes are name as “Life Insurance” and “Car
Insurance”. Premium of both the insurance policies are linked to bank account of the customer so that it
can be directly deducted from their saving account and current balance will be displayed after every
deduction. Features derived from the base classes are shown in the following diagram. The “Claim” class
is used to settle the claim amount and deposited in the respective saving bank account.
Note: Use Bank Account class created in the experiment 3 as base class in the hierarchy.
Data Members:   Members Functions:
Name of the   Open account
customer   Bank Account   Withdraw
Address   (Base Class)   Deposit
Age   Display Customer Details
Saving Account No   Display Balance
Balance
Data Members:   Data Members:
Policy No   Policy No
Sum Assured   Car Details
Premium   Premium
Term (No of Years)   Car   Duration
Life Insurance   Insurance
Members Functions:   (Derived Class)   (Derived Class)   Members Read Functions: data
Read data   Calculate premium
Calculate premium   Deduct premium
Deduct premium   (from saving)
(from saving annually   Display Information
and Term by 1).   Derived Data
Display Information   Members:
Policy No   Members Functions:
Sum Assured   Claim   Settlement Amount.
Premium   (Term or Car)
Term (No of Years)   Deposit amount in
Car details   (Derived   saving acc.
Premium   Class)   Display Information
Duration
Inheritance
Task:
Implement member functions to perform the task: calculation of premium and deduction from the bank
account.
Life Insurance Class: Derived from Bank Account class
A.   Calculate Premium for Life insurance: use following conditions
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
1.   If age of a person is below 25 years - 3 K / Year / Lakh. (Sum Assured)
2.   If age of a person is in between 26 to 45 years – 4 K /year/ Lakh
3.   If age of a person is in between 46 to 60 years – 5 K /year/ Lakh
4.   If age > 60 – no insurance.
Car Insurance Class: Derived from Bank Account class
B.   Calculate Premium for car insurance: Use following conditions
1.   If Car is new then – 5 K / Year / Lakh (8 L)
2.   If Car is between 2 – 4 Year old – 3 K/ Year / Lakh
3.   If Car is between 5 – 7 Year old – 2 K/ Year / Lakh
Claim class: Derived from Life Insurance and Car Insurance
Function: Settlement () - will calculate the amount depending on the status of the policy
1.   Life insurance:
a.   If policy closed within first 5 years – Zero amount
b.   If policy closed between 6 – 12 years – 25 % of sum assured
c.   If policy closed between 13-20 years – 50 % of sum assured + 20 % of sum assured as bonus
d.   If policy closed after 20 years – sum assured + 100 % of sum assured as bonus
Deposit this amount to saving account
2.   Car Insurance:
a.   Amount spent by customer on repairing of Car.
Deposit this amount to saving account
Concept: Implement programs using exception handling
5
Problem Statements 1:
Write a program that takes two integers as input from the user and performs division. Handle the
division_by_zero error if the denominator is zero and display an appropriate message.
Problem Statements 2:
Create a method check_Eligibility(int age) that checks if a person is eligible to vote (age >= 18). If the age
is less than 18, the method should throw an Exception. Use the throws keyword to indicate that this
method can throw an exception.
Problem Statements 3:
Create a user-defined exception InsufficientBalanceException. Write a program where a user enters the
withdrawal amount. If the balance is less than the withdrawal amount, throw the custom exception.
Note: Consider the class “Bank_Account” created in the assignment 3 to demonstrate the withdrawal.
6   Concept: Implement programs to handle data with external files.
Task1:
1.   Write a program to copy an image file from one location to another using byte-oriented streams.
Task2:
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
2.   Write a program to read a text file, and write a function to count the number of words in it.
3.   Write a function to search for the specific word. Use Buffer for efficient reading.
Concept: Implement programs to demonstrate the use of inner classes
7   Problem Statement: A smart home system has multiple devices, such as lights and fans, controlled by a
remote. Each remote has a power button to toggle the device on or off.
Task:
Create a class SmartHome that contains an inner class RemoteControl.
RemoteControl should have a method toggleDevice() that switches the device state (ON/OFF).
Simulate controlling a device using the inner class.
Expected outcome:
Device is currently OFF
Turning ON the device...
Device is now ON
Concept: Implement programs using abstract class and Interfaces
8   Problem Statement: An airline reservation system allows users to book economy and business class
tickets. The fare calculation and seat allocation process differs based on the ticket type.
Task:
Create an abstract class Flight with an abstract method calculateFare().
Implement subclasses EconomyClass and BusinessClass that override calculateFare().
Create an interface SeatAllocation with a method assignSeat().
Implement SeatAllocation in both subclasses to assign seat numbers.
Expected Outcome:
Enter ticket type (Economy/Business):
Business Fare: $1000
Seat assigned: 12A
Concept: Implement programs using template class and functions.
9
Problem Statement: Implement a generic library for fundamental data structures such as Stack, Queue,
and Linked List using templates (C++) or generics (Java).We write a generic function that can be used
for different data types. Examples of function templates are sort(), max(), min(), printArray().
Task:
i.   Implement a generic stack with push, pop, and peek operations.
ii.   Implement a generic queue with enqueue and dequeue operations.
iii.   Implement a generic linked list with insertion, deletion, and search functionality.
iv.   Demonstrate with different data types (integers, floating-point numbers, and user-defined types
like complex numbers).
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Concept: Implement program suing generics programming
10
Problem Statement:
Implement a generic sorting utility that allows users to sort data using custom comparator functions
provided as lambda expressions.
Task:
1.   Create a Generic Sorting Class:
a.   Implement a generic function that takes an array or list and a comparator function as input.
b.   Use lambda expressions to define different sorting criteria dynamically.
2.   Implement Sorting Strategies:
a.   Allow sorting based on natural ordering (ascending/descending).
b.   Allow user-defined sorting strategies (e.g., sorting based on absolute value, even-odd priority).
3.   Demonstrate with Different Data Types:
a.   Sort integers (normal order, absolute value, even-odd priority).
b.   Sort strings (alphabetically, by length).
c.   Sort user-defined objects (e.g., Employee class based on salary, age).
Text Books:
1. Y. Daniel Liang, “Introduction to Java Programming and Data Structures, Comprehensive Version”, 12th
Edition, Pearson paperback, 2024.
2. E. Balagurusamy, “Object Oriented Programming with C++”, 8th Edition, McGraw Hill, 2020.
Reference Books:
1. Dimitri Nesteruk, “Design Patterns in Modern C++20: Reusable Approaches for Object-Oriented Software
Design” 2nd Edition, Apress, 2022.
2. Maurice Naftalin, Philip Wadler, “Java Generics and Collections: Fundamentals and Recommended
Practices”, O'Reilly Media, Inc., 2nd Edition, 2025.
3. Bjarne Stroustrup, “The C++ Programming Language”, 4th Edition, Addison Wesley, Pearson Education,
2022.
4. Herbert Schildt, “Java 2: The Complete Reference”, 5th Edition, McGraw-Hill Education, 2017.
The list which is provided in the syllabus is guideline to conduct the practical sessions. The faculty can create
more practical examples suitable to given concepts in each experiment.
Signature
(Head of the Department )   AY 2026-27
SVKM’s NMIMS Deemed-to-be University
Mukesh Patel School of Technology Management and Engineering
Program: B Tech Integrated (IT, DS)   Semester: VII
````
