# Java Programming: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 1 · Answer key · paper d64729a23488

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_01/Final-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Java Programming/ANS_Java Programming(703CO0C018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Dec 2025
- Text: mixed (15 pages), mean OCR confidence 87.9

````text
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Semester I(Exam Year: 2025-2026)
Subject: Java Programming
Date: 01 Dec 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions
1. This question paper contains 15 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Answer to each new question to be started on a fresh page
5. Question No. 1 is compulsory. Out of remaining questions, attempt any 4 questions. In all 5 questions to
be attempted
6. Assume Suitable data if necessary.
7. Output for all programming questions is mandatory.
Q1   Answer briefly:   [20]
CO-1 ;
SO-1,6;   a.   [5]
BL-2
Java does not support multiple inheritance using classes to avoid ambiguity and
complexity that occurs when two parent classes have methods with the same
name and a child class inherits from both   leading to confusion about which
method to execute.By restricting multiple inheritance, Java ensures simplicity,
clarity, and reliability in its object model. Instead, Java allows a class to
implement multiple interfaces, which provide method declarations without
implementation, thereby avoiding conflicts.
CO-3 ;
SO-1,6;   b.   Explain the steps to connect a Java application to a database using JDBC.   [5]
BL-2
Java applications need to be programmed for interacting with data sources. JDBC
Drivers for specific databases are to be loaded in a java application for JDBC
support which can be done dynamically at run time. These JDBC drivers
communicate with the respective data source.
Steps to connect a Java program using JDBC API.
1. Import JDBC Packages: Import the necessary JDBC packages at the
beginning of your Java program. You'll typically need to import classes from the
java.sql package.
2. Load Driver: Load JDBC Driver for specific databases using forName()
method of class Class. Syntax: Class.forName("com.mysql.jdbc.Driver")
--- page 2 ---
3. Create Connection: Create a connection with a database using DriverManager
class. Database credentials are to be passed while establishing the connection.
Syntax: DriverManager.getConnection()
4. Create SQL Query: To manipulate the database we need to create a query
using commands like INSERT, UPDATE, DELETE, etc. These queries are
created and stored in string format. Syntax: String sql_query = "INSERT INTO
Student(name, roll_no) values('ABC','XYZ')"
5. Create SQL Statement: The query we have created is in form of a string. To
perform the operations in the string on a database we need to fire that query on
the database. To achieve this we need to convert a string object into SQL
statements. This can be done using createStatement() and prepareStatement()
interfaces.
Syntax: Statement St = con.createStatement();
6. Execute Statement: To execute SQL statements on the database we can use
two methods depending on which type of query we are executing.
Execute Update: Execute update method is used to execute queries like insert,
update, delete, etc. Return type of executeUpdate() method is int. Syntax: int
check = st.executeUpdate(sql);
Execute Query: Execute query method is used to execute queries used to display
data from the database, such as select. Return type of executeQuery() method is
result set. Syntax: Resultset = st.executeUpdate(sql);
7. Closing Statement: After performing operations on the database, it is better to
close every interface object to avoid further conflicts. Synatx: con.close();
CO-1
What is the difference between == operator and .equals() method when
SO-1,6;   c.   [5]
comparing strings in Java? Explain with an example.
BL-4
In Java, the == operator and the .equals() method are used to compare strings, but
they work differently:
== Operator (2.5 M):
Compares references (memory addresses) of two string objects. Returns true only
if both references point to the same object in memory.
.equals() Method (2.5 M):
Compares the actual content (value) of two strings. Returns true if the text inside
both strings is the same, regardless of whether they are different objects.
Example:
String s1 = new String("Hello");
String s2 = new String("Hello");
System.out.prin
CO-2 ;
d.   Explain the Collection Framework in brief with a neat diagram.   [5]
SO-1,6;
--- page 3 ---
BL-4

Collection Framework explanation (2M)
Diagram (3M)
The Collection framework represents a unified architecture for storing and
manipulating a group of objects. It has:
e Interfaces and its implementations
e Classes
e =6Algorithm
The Collections framework is defined in the java.util package

(interface
Iterable (class
* implements
Collection t extends

‘

4

a
el LinkedHashSet

LinkedList

Write a Java program to create a class Student with overloaded

Q2 constructors. A default constructor that only initializes Name. A constructor
CO-1; to initialize Name and Roll Number and another constructor to initialize [10]
SO-1,6; “| Name, Roll Number, and Marks. Display the details of students using a

BL-6 display() method. Demonstrate constructor overloading in the main method

by creating objects using each constructor and displaying the details.

// Program to demonstrate constructor overloading in Java

class Student {
String name;
int rollNo;
double marks;

// Default constructor (only initializes name)

Student() {
name = "Unknown";
rollINo = 0;
marks = 0.0;

}

// Constructor to initialize Name and Roll Number

FSI A I dk ck ak i ak kk
--- page 4 ---
Student(String n, int r) {
name = n;
rollNo = r;
marks = 0.0;
}
// Constructor to initialize Name, Roll Number, and Marks
Student(String n, int r, double m) {
name = n;
rollNo = r;
marks = m;
}
// Method to display student details
void display() {
System.out.println("Name: " + name);
System.out.println("Roll No: " + rollNo);
System.out.println("Marks: " + marks);
}
// Main method to test constructor overloading
public static void main(String[] args) {
// Using default constructor
Student s1 = new Student();
// Using constructor with Name and Roll Number
Student s2 = new Student("Ravi", 101);
// Using constructor with Name, Roll Number, and Marks
Student s3 = new Student("Priya", 102, 89.5);
// Display details of each student
s1.display();
s2.display();
s3.display();
}
}
CO-3;   Write a program to establish a connection with MySQL database for storing
SO-1,6;   b.   Student Details. Create a table and insert student details (Roll No, Name,   [10]
BL-6   Address) for 3 students in it and display it.
import java.sql.*;
public class StudentDatabase {
public static void main(String[] args) {
// Database URL, username, and password
String url = "jdbc:mysql://localhost:3306/StudentDetails";
String user = "root";
String password = "root";
Connection conn = null;
Statement stmt = null;
--- page 5 ---
try {
// 1. Load JDBC Driver
Class.forName("com.mysql.cj.jdbc.Driver");
// 2. Establish Connection
conn = DriverManager.getConnection(url, user, password);
System.out.println("Connected to the database successfully.");
stmt = conn.createStatement();
// 3. Create Student table
String createTable = "CREATE TABLE IF NOT EXISTS Student (" +
"RollNo INT PRIMARY KEY," +
"Name VARCHAR(50)," +
"Address VARCHAR(100))";
stmt.executeUpdate(createTable);
System.out.println("Student table created successfully.");
// 4. Insert student details
String insert1 = "INSERT INTO Student VALUES (1, 'Ravi', 'Delhi')";
String insert2 = "INSERT INTO Student VALUES (2, 'Priya',
'Mumbai')";
String insert3 = "INSERT INTO Student VALUES (3, 'Amit',
'Bangalore')";
stmt.executeUpdate(insert1);
stmt.executeUpdate(insert2);
stmt.executeUpdate(insert3);
System.out.println("Inserted student details successfully.");
// 5. Display student details
String selectQuery = "SELECT * FROM Student";
ResultSet rs = stmt.executeQuery(selectQuery);
System.out.println("\n--- Student Details ---");
while (rs.next()) {
int roll = rs.getInt("RollNo");
String name = rs.getString("Name");
String address = rs.getString("Address");
System.out.println("Roll No: " + roll + ", Name: " + name + ", Address:
" + address);
}
rs.close();
stmt.close();
conn.close();
} catch (Exception e) {
e.printStackTrace();
}
}
}
--- page 6 ---
Write a program to display the following pattern by asking the user for
number of lines using command line arguments.
Q3   *
CO-1;   * *
a.   [10]
SO-1,6;   * * *
BL-6   * * * *
* * *
* *
*
// Program to display a star pattern using command line argument
class StarPattern {
public static void main(String[] args) {
// Convert the argument to integer
int n = Integer.parseInt(args[0]);
// Upper half of the pattern
for (int i = 1; i <= n; i++) {
for (int j = 1; j <= i; j++) {
System.out.print("* ");
}
System.out.println();
}
// Lower half of the pattern
for (int i = n - 1; i >= 1; i--) {
for (int j = 1; j <= i; j++) {
System.out.print("* ");
}
System.out.println();
} } }
Output :
javac StarPattern.java
java StarPattern 4
*
* *
* * *
* * * *
* * *
* *
*
Design an abstract class Transport that defines an abstract method
calculateFare(int distance). Create two subclasses Bus and Train that
inherits Transport class and overrides calculateFare( int distance) method
CO-1;
to calculate and display the fare based on following criteria -
SO-1,6;   b.   [10]
Bus   fare is calculated as distance × 10
BL-6
Train   fare is calculated as distance × 5
Write a main method to create objects and to display appropriate details of
Bus and Train fares.
// Abstract class Transport
abstract class Transport {
--- page 7 ---
// Abstract method to calculate fare
abstract void calculateFare(int distance);
}
// Subclass Bus inheriting Transport
class Bus extends Transport {
@Override
void calculateFare(int distance) {
int fare = distance * 10;
System.out.println("Bus Fare for " + distance + " km = Rs. " + fare);
}
}
// Subclass Train inheriting Transport
class Train extends Transport {
@Override
void calculateFare(int distance) {
int fare = distance * 5;
System.out.println("Train Fare for " + distance + " km = Rs. " + fare);
}
}
// Main class
public class FareCalculator {
public static void main(String[] args) {
// Create objects of Bus and Train
Bus bus = new Bus();
Train train = new Train();
// Example distances
int busDistance = 15;
int trainDistance = 30;
// Display fares
System.out.println("=== Fare Calculation ===");
bus.calculateFare(busDistance);
train.calculateFare(trainDistance);
}
}
Output :
=== Fare Calculation ===
Bus Fare for 15 km = Rs. 150
Train Fare for 30 km = Rs. 150
Q4
a. Get the characters from index 3 to index 11 of the string.
CO-1;
a.   b. Return the string without any whitespace at the beginning or the end   [10]
SO-1,6;
c. Convert the string to upper case.
BL-6
e. Split the string
public class StringFunctions {
public static void main(String[] args) {
--- page 8 ---
// Original string
String str = "This is Java Programming ";
// a. Get characters from index 3 to 11
String substring = str.substring(3, 12); // end index is exclusive
System.out.println("a) Characters from index 3 to 11: " + substring);
// b. Remove whitespace at the beginning or end
String trimmed = str.trim();
System.out.println("b) String after trimming: '" + trimmed + "'");
// c. Convert the string to upper case
String upper = str.toUpperCase();
System.out.println("c) String in upper case: " + upper);
String replaced = str.replace("Java", "PHP");
System.out.println("d) String after replacement: " + replaced);
// e. Split the string
String[] words = str.split(" ");
System.out.println("e) Words in the string:");
for (String word : words) {
if (!word.isEmpty()) // Skip extra spaces
System.out.println(word);
}
}
}
Output :
a) Characters from index 3 to 11: s is Jav
b) String after trimming: 'This is Java Programming'
c) String in upper case: THIS IS JAVA PROGRAMMING
d) String after replacement: This is PHP Programming
e) Words in the string:
This
is
Java
Programming
CO-3;
SO-1,6;   b.   Discuss the Lifecycle of JavaFX Application in detail.   [10]
BL-2
--- page 9 ---
We need to import javafx.application.Application class in every JavaFX
application.
This provides the following life cycle methods for JavaFX application.
public void init()
public abstract void start(Stage primaryStage)
public void stop()
init() The init() method is an empty method that can be overridden. In
this method, the user cannot create a stage or a scene.
start()   The start() method is the entry point method of the JavaFX
application where all the graphics code of JavaFX is to be written.
stop()   The stop() method is an empty method that can also be
overridden, just like the init() method. In this method, the user can write
the code to halt the application.
Other than these methods, the JavaFX application also implements a static
method known as launch(). This launch() method is used to launch the
JavaFX application. As stated earlier, the launch() method is static, the
user should call it from a static method only. Generally, that static method,
which calls the launch() method, is the main() method only.
Whenever a user launches a JavaFX application, there are few actions that
are carried out in a particular manner only.
The following is the order given in which a JavaFX application is
launched.
Firstly, an instance of the application class is created.
After that, the init() method is called.
After the init() method, the start() method is called.
After calling the start() method, the launcher waits for the JavaFX
application to end and then calls the stop() method.
in order to create a basic JavaFX application, we need to:
Import javafx.application.Application into our code.
Inherit Application into our class.
Override start() method of Application class.
Q5
Explain the concept of Exception Handling in Java along with types of
CO-1;
a.   exceptions. Write a single code to demonstrate the use of five keywords used   [10]
SO-1,6;
for Exception Handling in Java.
BL-6
Exception Handling (2M)
Exception Handling in Java is a powerful mechanism that allows a programmer
to detect and manage runtime errors gracefully, so that the normal flow of the
program continues without abrupt termination.
An exception is an event that disrupts the normal execution of a program, such as
dividing by zero, accessing an invalid array index, or opening a missing file.
Without exception handling, such errors would cause the program to crash.
With exception handling, Java provides a structured way to detect, handle, and
recover from these situations.
Types of Exceptions (3M):
Checked Exceptions   Checked at compile time (e.g., IOException,
SQLException).
--- page 10 ---
Unchecked Exceptions   Occur at runtime (e.g., ArithmeticException,
NullPointerException).
Errors   Serious issues that cannot usually be handled   (e.g.,
OutOfMemoryError).
Code (5M) :
class ExceptionDemo {
// Method that declares an exception using 'throws'
static void divide(int a, int b) throws ArithmeticException {
if (b == 0)
throw new ArithmeticException("Division by zero not allowed!"); //
'throw'
else
System.out.println("Result: " + (a / b));
}
public static void main(String[] args) {
try {
divide(10, 0); // This will cause an exception
}
catch (ArithmeticException e) { // 'catch'
System.out.println("Exception Caught: " + e.getMessage());
}
finally { // 'finally'
System.out.println("Program execution completed.");
}
}
}
CO-2;
Enlist all the Generic Restrictions and justify any two of them with the help
SO-1,6;   b.   [10]
of the code.
BL-4
Generic Restrictions (3M)
You cannot use generics in certain ways and in certain scenarios as listed
You cannot use primitive datatypes with generics.
You cannot instantiate the generic parameters.
The generic type parameter cannot be static.
You cannot cast parameterized type of one datatype to other.
You cannot create an array of generic type objects.
A generic type class cannot extend the throwable class therefore, you
cannot catch or throw these objects.
Code for any two (3.5M each)
Q6   Create a package named geometry that contains classes for the shapes Circle
CO-1;   and Rectangle. Each class should have a method to calculate area. Import
a.   [10]
SO-1,6;   this package into a main class outside the geometry package and compute
BL-6   the area for all the shapes.
Circle.java (2.5M)
package geometry;
--- page 11 ---
public class Circle {
private double radius;
public Circle(double radius) {
this.radius = radius;
}
public double area() {
return Math.PI * radius * radius;
}
}
Rectangle.java (2.5M)
package geometry;
public class Rectangle {
private double length, width;
public Rectangle(double length, double width) {
this.length = length;
this.width = width;
}
public double area() {
return length * width;
}
}
Main.java (3M)
import geometry.Circle;
import geometry.Rectangle;
public class MainShape {
public static void main(String[] args) {
// Create objects of shapes
Circle circle = new Circle(5);   // radius = 5
Rectangle rectangle = new Rectangle(4, 6); // length=4, width=6
// Compute and display area
System.out.println("Circle Area: " + circle.area());
System.out.println("Rectangle Area: " + rectangle.area());
}
}
Output : (2M)
javac geometry/*.java
javac MainShape.java
java MainShape
Circle Area: 78.53981633974483
Rectangle Area: 24.0
CO-3;   Write a JavaFX Code to generate a calculator page that consists of one
b.   [10]
SO-1,6;   textfield (Enter Number) and two buttons (Square and Cube). The user
--- page 12 ---
BL-6   enters a number in textfield and when clicks on the Square or Cube button,
the square or cube of the number entered is calculated and displayed.
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
public class CalculatorFX extends Application {
@Override
public void start(Stage primaryStage) {
primaryStage.setTitle("Square & Cube Calculator");
// Create UI elements
Label lblNumber = new Label("Enter Number:");
TextField txtNumber = new TextField();
Button btnSquare = new Button("Square");
Button btnCube = new Button("Cube");
Label lblResult = new Label("Result: ");
// Layout using GridPane
GridPane grid = new GridPane();
grid.setVgap(10);
grid.setHgap(10);
grid.add(lblNumber, 0, 0);
grid.add(txtNumber, 1, 0);
grid.add(btnSquare, 0, 1);
grid.add(btnCube, 1, 1);
grid.add(lblResult, 0, 2, 2, 1); // span 2 columns
// Button Actions
btnSquare.setOnAction(e -> {
try {
double num = Double.parseDouble(txtNumber.getText());
double square = num * num;
lblResult.setText("Result: " + square);
} catch (NumberFormatException ex) {
lblResult.setText("Please enter a valid number!");
}
});
btnCube.setOnAction(e -> {
try {
double num = Double.parseDouble(txtNumber.getText());
double cube = num * num * num;
lblResult.setText("Result: " + cube);
} catch (NumberFormatException ex) {
lblResult.setText("Please enter a valid number!");
}
--- page 13 ---
});
// Scene and Stage
Scene scene = new Scene(grid, 300, 150);
primaryStage.setScene(scene);
primaryStage.show();
}
public static void main(String[] args) {
launch(args);
}
}
Q7
CO-1;   Demonstrate the use of super keyword to call a constructor and method of
a.   [10]
SO-1,6;   the parent class.
BL-3
// Parent class
class Parent {
String message;
// Parent class constructor
Parent(String msg) {
this.message = msg;
System.out.println("Parent Constructor called: " + message);
}
// Parent class method
void displayMessage() {
System.out.println("Message from Parent: " + message);
}
}
// Child class
class Child extends Parent {
String childMessage;
// Child class constructor
Child(String msgParent, String msgChild) {
super(msgParent); // Call parent class constructor
this.childMessage = msgChild;
System.out.println("Child Constructor called: " + childMessage);
}
// Child class method
void showMessages() {
super.displayMessage(); // Call parent class method
System.out.println("Message from Child: " + childMessage);
}
}
// Main class
public class SuperDemo {
public static void main(String[] args) {
--- page 14 ---
// Create Child object
Child c = new Child("Hello from Parent", "Hello from Child");
// Display messages
c.showMessages();
}
}
Write a Java Program to create an Array List for storing CGPA of students.
CO-2;
The program must allow to add CGPA to array list, display the entire list,
SO-1,6;   b.   [10]
display CGPA at a particular index, delete CGPA at particular index and
BL-6
clear entire list. Use switch case to select the desired option.
import java.util.ArrayList;
import java.util.Scanner;
public class CGPAListManager {
public static void main(String[] args) {
ArrayList<Double> cgpaList = new ArrayList<>();
Scanner sc = new Scanner(System.in);
int choice;
do {
System.out.println("\n--- CGPA ArrayList Operations ---");
System.out.println("1. Add CGPA");
System.out.println("2. Display entire list");
System.out.println("3. Display CGPA at particular index");
System.out.println("4. Delete CGPA at particular index");
System.out.println("5. Clear entire list");
System.out.println("6. Exit");
System.out.print("Enter your choice: ");
choice = sc.nextInt();
switch (choice) {
case 1:
System.out.print("Enter CGPA to add: ");
double cgpa = sc.nextDouble();
cgpaList.add(cgpa);
System.out.println("CGPA added successfully!");
break;
case 2:
System.out.println("CGPA List: " + cgpaList);
break;
case 3:
System.out.print("Enter index to display CGPA: ");
int index = sc.nextInt();
if (index >= 0 && index < cgpaList.size()) {
System.out.println("CGPA at index " + index + ": " +
cgpaList.get(index));
} else {
System.out.println("Invalid index!");
}
break;
--- page 15 ---
case 4:
System.out.print("Enter index to delete CGPA: ");
int delIndex = sc.nextInt();
if (delIndex >= 0 && delIndex < cgpaList.size()) {
cgpaList.remove(delIndex);
System.out.println("CGPA at index " + delIndex + " deleted.");
} else {
System.out.println("Invalid index!");
}
break;
case 5:
cgpaList.clear();
System.out.println("All CGPAs cleared from the list.");
break;
case 6:
System.out.println("Exiting program.");
break;
default:
System.out.println("Invalid choice! Please try again.");
}
} while (choice != 6);
sc.close();
}
}
````

## 2025-26 · Re-Exam · Sem 1 · Answer key · paper 3035a37a2594

- Departments: Computer Applications (MCA)
- Programmes: MASTER OF COMPUTER APPLICATIONS - 7061
- Source: `02_Question_Papers/2025/Sem_01/Re-Exam/MASTER OF COMPUTER APPLICATIONS - 7061/Java Programming/ANS_Java Programming(703CO0C018)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 07 Feb 2026
- Text: text (19 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: MASTER OF COMPUTER APPLICATIONS
Year: I/Sem 1 Re-exam(Exam Year: 2025-2026)
Subject: Java Programming
Date: 07 Feb 2026   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 19 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Answer to each new question to be started on a fresh page
5. Question No. 1 is compulsory. Out of remaining questions, attempt any 4 questions. In all 5 questions to
be attempted
6. Assume Suitable data if necessary.
7. Output for all programming questions is mandatory.
Q1   Answer briefly:   [20]
CO-1 ;
What is Java Virtual Machine (JVM)? Explain its role in Java's platform
SO-1,6;   a.   [5]
independence.
BL-2
JVM (2M) :
 JVM (Java Virtual Machine) is an abstract machine. It is a specification that
provides runtime environment in which java bytecode can be executed.
 JVM is an interpreter. It is the main component of Java that makes java
platform independent.
 It is because the bytecode file can be taken onto any system and the JVM
residing in that system will interpret and translate the byte code into machine
readable code.
 The JVM performs following operation:
 Loads code
 Verifies code
 Executes code
 Provides runtime environment
Role of JVM in Java’s Platform Independence (3M)
Java is famous for its motto: “Write Once, Run Anywhere (WORA)”. JVM plays
a central role in achieving this.
Step-by-step process:
Write Java Code: A developer writes code in Java (.java file).
Compile Java Code: The Java compiler (javac) converts .java files into bytecode
(.class files). Bytecode is platform-independent and cannot run directly on the
OS.
********** 1 **********
--- page 2 ---
Run Bytecode on JVM: Each platform (Windows, Linux, macOS) has its own
JVM. The JVM interprets or just-in-time (JIT) compiles bytecode into native
machine code specific to that platform.
This means the same .class file can run on any platform with a compatible JVM.
CO-3 ;
SO-1,6;   b.   Elaborate on different types of JDBC Drivers.   [5]
BL-2
JDBC (Java Database Connectivity) drivers are platform-specific or database-
specific implementations that allow Java applications to connect to and interact
with relational databases. There are four main types of JDBC drivers, known as
JDBC driver types 1, 2, 3, and 4. Each type has its own characteristics and is
suited for different scenarios:
Type-1 JDBC Driver (JDBC-ODBC Bridge Driver):
Type-1 drivers are also known as JDBC-ODBC Bridge drivers.
They use the JDBC-ODBC bridge to connect to the database.
The bridge relies on the ODBC (Open Database Connectivity) driver installed on
the system to communicate with the database.
Type-1 drivers are considered legacy and have been deprecated in favor of other
driver types. They are not recommended for new development.
Type-2 JDBC Driver (Native-API Driver):
Type-2 drivers are known as Native-API drivers.
They are platform-specific drivers that use a database-specific native API to
communicate with the database.
These drivers provide better performance than Type-1 drivers because they
communicate directly with the database without the ODBC layer.
However, they are still somewhat dependent on the platform and database, which
can limit portability.
Type-3 JDBC Driver (Network Protocol Driver):
Type-3 drivers are also called Network Protocol drivers.
They use a middleware or network protocol to connect to the database server.
The client-side of the driver translates JDBC calls into a database-independent
protocol, which is then transmitted over the network to a server-side component
that interacts with the database.
Type-3 drivers are generally platform-independent and can work with different
databases as long as there is a compatible server-side component.
Type-4 JDBC Driver (Thin Driver or Direct-to-Database Pure Java Driver):
Type-4 drivers are known as Thin drivers.
They are pure Java drivers that communicate directly with the database using a
database-specific protocol.
Type-4 drivers are highly portable because they don't rely on platform-specific
libraries or middleware.
They are typically the preferred choice for modern Java applications as they offer
good performance and platform independence.
Examples of Type-4 drivers include Oracle Thin Driver, PostgreSQL JDBC
Driver, and MySQL Connector/J.
********** 2 **********
--- page 3 ---
The choice of JDBC driver type depends on various factors, including the specific
database being used, the application's portability requirements, and performance
considerations. In general, Type-4 drivers are recommended for new Java
applications because they offer good performance and are platform-independent.
However, in some legacy or specialized scenarios, other driver types may still be
used.
CO-1
Explain the concept of immutability in Java String class. Write a code
SO-1,6;   c.   [5]
snippet to support your answer.
BL-4
In Java, the String class is immutable, which means once a String object is
created, its value cannot be changed. Any modification on a string (like
concatenation or replacement) creates a new String object rather than changing
the original object.
Let's try to understand the concept of immutability by the example given below:
String s="Java";
s.concat(" Programming");   //concat() method appends the string at the end
System.out.println(s);   //will print Java because strings are immutable objects
Now it can be understood that Java is not changed but a new object is created
with Java Programming and s reference variable still refers to “Java" and not to
“Java Programming". That is why String is known as immutable.
But if we explicitly assign it to the reference variable, it will refer to “Java
Programming" object. Please notice that still “Java” object is not modified, only
that the reference variable refers to the new object.
String s="Java";
s=s.concat(" Programming");
System.out.println(s); //prints Java Programming
CO-2 ;
Justify the statement “The generic type parameter cannot be static” with a
SO-1,6;   d.   [5]
code.
BL-4
The generic type parameter cannot be static.
class Student<T>{
static T age;
Student(T age){
this.age = age;
}
public void display() {
System.out.println("Value of age: "+this.age);
}
}
public class Main {
public static void main(String args[]) {
Student<Float> std1 = new Student<Float>(25.5f);
std1.display();
}
}
********** 3 **********
--- page 4 ---
Implement a base class Vehicle with properties modelName and basePrice
(take values from user). Derive classes Car and Truck from it. The Car class
Q2   should calculate the on-road price by adding 10% tax to the base price. The
CO-1;   Truck class should calculate the on-road price by adding 15% tax to the base
a.   [10]
SO-1,6;   price. Implement a method calculateOnRoadPrice() in each class to display
BL-6   the total cost. Write a main method to create objects of both classes and
display vehicle details and final on road price of Car and Truck. Use
appropriate constructors to initialize values.
import java.util.Scanner;
// Base class
class Vehicle {
protected String modelName;
protected double basePrice;
// Constructor to initialize values
public Vehicle(String modelName, double basePrice) {
this.modelName = modelName;
this.basePrice = basePrice;
}
// Method to calculate on-road price (to be overridden)
public void calculateOnRoadPrice() {
System.out.println("Base Vehicle Price: " + basePrice);
}
}
// Derived class Car
class Car extends Vehicle {
public Car(String modelName, double basePrice) {
super(modelName, basePrice);
}
// Override method to calculate on-road price with 10% tax
@Override
public void calculateOnRoadPrice() {
double onRoadPrice = basePrice + (0.10 * basePrice);
System.out.println("Car Model: " + modelName);
System.out.println("Base Price: " + basePrice);
System.out.println("On-Road Price (with 10% tax): " + onRoadPrice);
}
}
// Derived class Truck
class Truck extends Vehicle {
public Truck(String modelName, double basePrice) {
super(modelName, basePrice);
}
// Override method to calculate on-road price with 15% tax
@Override
public void calculateOnRoadPrice() {
********** 4 **********
--- page 5 ---
double onRoadPrice = basePrice + (0.15 * basePrice);
System.out.println("Truck Model: " + modelName);
System.out.println("Base Price: " + basePrice);
System.out.println("On-Road Price (with 15% tax): " + onRoadPrice);
}
}
// Main class
public class VehicleTest {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
// Input for Car
System.out.print("Enter Car model name: ");
String carModel = sc.nextLine();
System.out.print("Enter Car base price: ");
double carPrice = sc.nextDouble();
sc.nextLine(); // Consume leftover newline
Car car = new Car(carModel, carPrice);
// Input for Truck
System.out.print("Enter Truck model name: ");
String truckModel = sc.nextLine();
System.out.print("Enter Truck base price: ");
double truckPrice = sc.nextDouble();
Truck truck = new Truck(truckModel, truckPrice);
System.out.println("\n--- Vehicle Details and On-Road Price ---");
car.calculateOnRoadPrice();
System.out.println();
truck.calculateOnRoadPrice();
sc.close();
}
}
CO-3;   Write a program to connect to MySQL and create a database for storing
SO-1,6;   b. Employee details. Create a table for storing employee details (E_id, Name,   [10]
BL-6   Address), insert details of 3 employees into it and display it.
import java.sql.*;
public class EmployeeDatabaseDemo {
public static void main(String[] args) {
// Database credentials
String url = "jdbc:mysql://localhost:3306/";
String user = "root";
String password = "root";
Connection con = null;
Statement stmt = null;
try {
********** 5 **********
--- page 6 ---
// 1. Load MySQL JDBC driver
Class.forName("com.mysql.cj.jdbc.Driver");
// 2. Connect to MySQL server
con = DriverManager.getConnection(url, user, password);
stmt = con.createStatement();
// 3. Create database
String createDatabase = "CREATE DATABASE IF NOT EXISTS
EmployeeDB";
stmt.executeUpdate(createDatabase);
System.out.println("Database created successfully.");
// 4. Connect to the newly created database
con.setCatalog("EmployeeDB");
// 5. Create Employee table
String createTable = "CREATE TABLE IF NOT EXISTS Employee (" +
"E_id INT PRIMARY KEY, " +
"Name VARCHAR(50), " +
"Address VARCHAR(100))";
stmt.executeUpdate(createTable);
System.out.println("Table created successfully.");
// 6. Insert 3 employee records
String insert1 = "INSERT INTO Employee VALUES (101, 'Alice', 'New
York')";
String insert2 = "INSERT INTO Employee VALUES (102, 'Bob', 'Los
Angeles')";
String insert3 = "INSERT INTO Employee VALUES (103, 'Charlie',
'Chicago')";
stmt.executeUpdate(insert1);
stmt.executeUpdate(insert2);
stmt.executeUpdate(insert3);
System.out.println("Inserted 3 employee records successfully.");
// 7. Retrieve and display employee details
String selectQuery = "SELECT * FROM Employee";
ResultSet rs = stmt.executeQuery(selectQuery);
System.out.println("\nEmployee Details:");
System.out.println("E_id\tName\tAddress");
System.out.println("-----------------------------");
while (rs.next()) {
int id = rs.getInt("E_id");
String name = rs.getString("Name");
String address = rs.getString("Address");
System.out.println(id + "\t" + name + "\t" + address);
}
********** 6 **********
--- page 7 ---
} catch (ClassNotFoundException e) {
System.out.println("MySQL JDBC Driver not found.");
e.printStackTrace();
} catch (SQLException e) {
e.printStackTrace();
} finally {
try {
if (stmt != null) stmt.close();
if (con != null) con.close();
} catch (SQLException e) {
e.printStackTrace();
}
}
}
}
Write a program to display the following pattern by asking the user for
number of lines using BufferedReader method.
Q3
CO-1;
a.   [10]
SO-1,6;
BL-6
import java.io.*
public class LetterPattern {
public static void main(String[] args) {
// The letter 'A' corresponds to ASCII 65.
char startChar = 'A';
BufferedReader br=new BufferedReader(new InputStreamReader(System.in);
String str=br.readLine();
int maxRows=Integer.parseInt(str); // The longest row contains 5 letters (A
to E)
// 1. Increasing part of the pattern (Rows 1 to 5: A, AB, ABC, ABCD,
ABCDE)
for (int i = 1; i <= maxRows; i++) {
// Loop to print the characters for the current row
for (int j = 0; j < i; j++) {
System.out.print((char) (startChar + j) + " ");
}
// Move to the next line after the row is complete
System.out.println();
}
// 2. Decreasing part of the pattern (Rows 6 to 9: ABCD, ABC, AB, A)
// We start from maxRows - 1 (4) because the row with 5 letters (maxRows)
is already printed.
********** 7 **********
--- page 8 ---
for (int i = maxRows - 1; i >= 1; i--) {
// Loop to print the characters for the current row
for (int j = 0; j < i; j++) {
System.out.print((char) (startChar + j) + " ");
}
// Move to the next line
System.out.println();
}
}
}
Create a class Book with a method getDetails() that displays the book title
and author. Derive the subclasses TextBook and Novel that override
CO-1;
getDetails() to include additional information like subject (for TextBook)
SO-1,6;   b.   [10]
and genre (for Novel). Demonstrate method overriding by calling
BL-6
getDetails() on different subclass objects. Use appropriate constructors for
taking input.
// Base class
class Book {
protected String title;
protected String author;
// Constructor
public Book(String title, String author) {
this.title = title;
this.author = author;
}
// Method to display book details
public void getDetails() {
System.out.println("Book Title: " + title);
System.out.println("Author: " + author);
}
}
// Subclass for TextBook
class TextBook extends Book {
private String subject;
// Constructor
public TextBook(String title, String author, String subject) {
super(title, author); // Call superclass constructor
this.subject = subject;
}
// Overridden method
@Override
public void getDetails() {
super.getDetails(); // Call base class method
System.out.println("Subject: " + subject);
}
}
// Subclass for Novel
********** 8 **********
--- page 9 ---
class Novel extends Book {
private String genre;
// Constructor
public Novel(String title, String author, String genre) {
super(title, author);
this.genre = genre;
}
// Overridden method
@Override
public void getDetails() {
super.getDetails();
System.out.println("Genre: " + genre);
}
}
// Main class to demonstrate
public class Main {
public static void main(String[] args) {
// Create objects of subclasses
TextBook tb = new TextBook("Mathematics 101", "John Smith",
"Mathematics");
Novel nv = new Novel("The Great Adventure", "Emily Bronte",
"Adventure");
// Demonstrate method overriding
System.out.println("TextBook Details:");
tb.getDetails();
System.out.println("\nNovel Details:");
nv.getDetails();
}
}
Q4
CO-1;   Discuss string comparison techniques in Java. Explain with example how
a.   [10]
SO-1,6;   are ==, equals(), equalsIgnoreCase(), and compareTo() methods different?
BL-5
Each technique explanation (1M)
== Operator
The == operator compares references, not the content of the string. It checks
whether two string variables point to the same memory location (object
reference).
equals() Method
Compares the content of strings. Returns true if the strings have the same
sequence of characters.
equalsIgnoreCase() Method
********** 9 **********
--- page 10 ---
Compares string content ignoring case differences. Useful when you want "Hello"
and "hello" to be considered equal.
compareTo() Method
Used for lexicographical comparison (dictionary order).
Returns an integer. 0 → strings are equal, <0 → calling string is less than
argument, >0 → calling string is greater than argument
Code (6M) :
public class StringComparisonDemo {
public static void main(String[] args) {
// Strings for comparison
String s1 = "Hello";
String s2 = "Hello";
String s3 = new String("Hello");
String s4 = "hello";
String s5 = "World";
// 1. Using '=='
System.out.println("Using '==':");
System.out.println("s1 == s2: " + (s1 == s2)); // true, same reference in
string pool
System.out.println("s1 == s3: " + (s1 == s3)); // false, different objects
System.out.println();
// 2. Using equals()
System.out.println("Using equals():");
System.out.println("s1.equals(s2): " + s1.equals(s2)); // true
System.out.println("s1.equals(s3): " + s1.equals(s3)); // true, content same
System.out.println("s1.equals(s4): " + s1.equals(s4)); // false, case-sensitive
System.out.println();
// 3. Using equalsIgnoreCase()
System.out.println("Using equalsIgnoreCase():");
System.out.println("s1.equalsIgnoreCase(s4): " +
s1.equalsIgnoreCase(s4)); // true, ignores case
System.out.println();
// 4. Using compareTo()
System.out.println("Using compareTo():");
System.out.println("s1.compareTo(s2): " + s1.compareTo(s2)); // 0, strings
equal
System.out.println("s1.compareTo(s5): " + s1.compareTo(s5)); // negative,
"Hello" < "World"
System.out.println("s5.compareTo(s1): " + s5.compareTo(s1)); // positive,
"World" > "Hello"
}
}
CO-3;
SO-1,6;   b.   Discuss the Application structure of JavaFX in detail.   [10]
BL-2
********** 10 **********
--- page 11 ---
 JavaFX application is divided hierarchically into three main components
known as Stage, Scene and nodes.
Stage
 Stage in a JavaFX application is similar to the Frame in a Swing
Application.
 It acts like a container for all the JavaFX objects.
 Primary Stage is created internally by the platform.
 Other stages can further be created by the application.
 The object of primary stage is passed to start method.
 We need to call show method on the primary stage object in order to show
our primary stage.
 Initially, the primary Stage looks like following.
 However, we can add various objects to this primary stage.
 The objects can only be added in a hierarchical way i.e. first, scene graph
will be added to this primaryStage and then that scene graph may contain
the nodes.
 A node may be any object of the user's interface like text area, buttons,
shapes, media, etc.
 It is represented by Stage class of the package javafx.stage.
 A stage has two parameters determining its position namely Width and
Height. It is divided as Content Area and Decorations (Title Bar and
Borders).
 You have to call the show() method to display the contents of a stage.
Scene
 A scene represents the physical contents of a JavaFX application.
 It contains all the contents of a scene graph.
 The class Scene of the package javafx.scene represents the scene object.
Javafx.scene.Scene class provides all the methods to deal with a scene
object.
 At an instance, the scene object is added to only one stage.
 You can create a scene by instantiating the Scene Class.
 You can opt for the size of the scene by passing its dimensions (height and
width) along with the root node to its constructor.
 Creating scene is necessary in order to visualize the contents on the stage.
 In order to implement Scene in our JavaFX application, we must import
javafx.scene package in our code.
Scene Graph
 A scene graph is a tree-like data structure (hierarchical) representing the
contents of a scene.
 In contrast, a node is a visual/graphical object of a scene graph. A node is
the element which is visualized on the stage. It can be any button, text box,
layout, image, radio button, check box, etc.
********** 11 **********
--- page 12 ---
 A node may include −
 Geometrical (Graphical) objects (2D and 3D) such as − Circle,
Rectangle, Polygon, etc.
 UI Controls such as − Button, Checkbox, Choice Box, Text Area,
etc.
 Containers (Layout Panes) such as Border Pane, Grid Pane, Flow
Pane, etc.
 Media elements such as Audio, Video and Image Objects.It can be
seen as the collection of various nodes.
 The nodes are implemented in a tree kind of structure.
 There is always one root in the scene graph. This will act as a parent node
for all the other nodes present in the scene graph. However, this node may
be any of the layouts available in the JavaFX system.
 The leaf nodes exist at the lowest level in the tree hierarchy.
 Each of the node present in the scene graphs represents classes of
javafx.scene package therefore we need to import the package into our
application in order to create a full featured javafx application.
 As discussed earlier a node is of three types −
 Root Node − The first Scene Graph is known as the Root node.
 Branch Node/Parent Node − The node with child nodes are known as
branch/parent nodes. The abstract class named Parent of the package
javafx.scene is the base class of all the parent nodes, and those parent nodes
will be of the following types −
 Group − A group node is a collective node that contains a list of
children nodes. Whenever the group node is rendered, all its child
nodes are rendered in order. Any transformation, effect state applied
on the group will be applied to all the child nodes.
 Region − It is the base class of all the JavaFX Node based UI
Controls, such as Chart, Pane and Control.
 WebView − This node manages the web engine and displays its
contents.
 Leaf Node − The node without child nodes is known as the leaf node. For
example, Rectangle, Ellipse, Box, ImageView, MediaView are examples of
leaf nodes.
It is mandatory to pass the root node to the scene graph.
Create a custom checked exception TransactionLimitExceededException to
Q5
be thrown when a user tries to make a transaction that exceeds a predefined
CO-1;
a.   limit.   Implement   a   Transaction   class   with   a   method   [10]
SO-1,6;
processTransaction(double amount) that checks if the transaction amount
BL-6
exceeds the limit. If it does, throw TransactionLimitExceededException.
// Custom checked exception
class TransactionLimitExceededException extends Exception {
public TransactionLimitExceededException(String message) {
super(message);
}
}
// Transaction class
class Transaction {
private double transactionLimit;
// Constructor to set transaction limit
public Transaction(double transactionLimit) {
********** 12 **********
--- page 13 ---
this.transactionLimit = transactionLimit;
}
// Method to process transaction
public   void   processTransaction(double   amount)   throws
TransactionLimitExceededException {
if (amount > transactionLimit) {
throw new TransactionLimitExceededException(
"Transaction amount $" + amount + " exceeds the limit of $" +
transactionLimit
);
} else {
System.out.println("Transaction of $" + amount + " processed
successfully.");
}
}
}
// Main class to test
public class TransactionTest {
public static void main(String[] args) {
Transaction t = new Transaction(5000); // Set transaction limit to $5000
double amount = 6000; // Sample transaction input
try {
t.processTransaction(amount);
} catch (TransactionLimitExceededException e) {
System.out.println("Error: " + e.getMessage());
}
}
}
output:
Error: Transaction amount $6000.0 exceeds the limit of $5000.0
CO-2;
Explain Generic Methods and their rules. Also explain Bounded Types with
SO-1,6;   b.   [10]
a code.
BL-4
Generic Methods and Rules (4M)
 You can write a single generic method declaration that can be called with
arguments of different types.
 Based on the types of the arguments passed to the generic method, the
compiler handles each method call appropriately.
 Generic Java method takes a parameter and returns some value after
performing a task.
 It is exactly like a normal function, however, a generic method has type
parameters that are cited by actual type.
 This allows the generic method to be used in a more general way.
 The compiler takes care of the type of safety which enables programmers to
code easily since they do not have to perform long, individual type castings.
 Following are the rules to define Generic Methods −
 All generic method declarations have a type parameter section
delimited by angle brackets (< and >) that precedes the method's return
type.
********** 13 **********
--- page 14 ---
 Each type parameter section contains one or more type parameters
separated by commas. A type parameter, also known as a type
variable, is an identifier that specifies a generic type name.
 The type parameters can be used to declare the return type and act as
placeholders for the types of the arguments passed to the generic
method, which are known as actual type arguments.
 A generic method's body is declared like that of any other method.
Note that type parameters can represent only reference types, not
primitive types (like int, double and char).
Bounded type explanation (2M)
 In general, the type parameter can accept any data types.
 However, if we want to use generics for some specific types (such as accept
data of number types) only, then we can use bounded types.
 In the case of bound types, we use the extends keyword.
 Syntax : <T extends A>
This means T can only accept data that are subtypes of A.
 Eg : class GenericsClass <T extends Number>
Here, GenericsClass is   created   with   bounded   type.   This
means GenericsClass can only work with data types that are subtypes
of Number (Integer, Double, and so on).
Bounded Type Code (4M)
class GenericsClass <T extends Number> {
public void display() {
System.out.println("This is a bounded type generics class.");
} }
class Main {
public static void main(String[] args) {
// create an object of GenericsClass
GenericsClass<Integer/Float/Double/Long/Short>   obj   =   new
GenericsClass<>();
obj.display();
} }
Q6
CO-1;   Explain how multiple inheritance is supported in Java. Develop a code to
a.   [10]
SO-1,6;   demonstrate the same.
BL-6
Explanation (4M)
Multiple inheritance is when a class inherits from more than one parent class.
Java does not support multiple inheritance with classes because it can lead to the
Diamond Problem (ambiguity if two parent classes have the same method).
Multiple inheritance is supported using interfaces. A class can implement
multiple interfaces, allowing it to inherit behavior from multiple sources.
Code (6M)
// First interface
interface Printer {
void print(String message); // abstract method
}
// Second interface
interface Scanner {
********** 14 **********
--- page 15 ---
void scan(String document); // abstract method
}
// Class implementing both interfaces (multiple inheritance)
class MultiFunctionMachine implements Printer, Scanner {
// Implement print method
@Override
public void print(String message) {
System.out.println("Printing: " + message);
}
// Implement scan method
@Override
public void scan(String document) {
System.out.println("Scanning: " + document);
}
}
// Main class to demonstrate
public class MultipleInheritanceDemo {
public static void main(String[] args) {
MultiFunctionMachine mfm = new MultiFunctionMachine();
// Call methods from both interfaces
mfm.print("Hello, world!");
mfm.scan("Document1.pdf");
}
}
Write a JavaFX Code to generate a course enrollment page wherein the
student enters Name, Roll no, gender, department and selects three courses
CO-3;   out of five courses offered. On clicking the Enroll button the student
SO-1,6;   b.   completes the enrollment process and the message “Hello abc, Your course   [10]
BL-6   enrollment in xyz department is completed” is displayed where abc is the
student name and xyz is the department entered by the user. Use appropriate
JavaFX fields.
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;
public class CourseEnrollment extends Application {
@Override
public void start(Stage primaryStage) {
primaryStage.setTitle("Course Enrollment Form");
// Grid layout
GridPane grid = new GridPane();
grid.setVgap(10);
grid.setHgap(10);
********** 15 **********
--- page 16 ---
// Name
Label nameLabel = new Label("Name:");
TextField nameField = new TextField();
grid.add(nameLabel, 0, 0);
grid.add(nameField, 1, 0);
// Roll No
Label rollLabel = new Label("Roll No:");
TextField rollField = new TextField();
grid.add(rollLabel, 0, 1);
grid.add(rollField, 1, 1);
// Gender (Radio Buttons)
Label genderLabel = new Label("Gender:");
ToggleGroup genderGroup = new ToggleGroup();
RadioButton maleRB = new RadioButton("Male");
RadioButton femaleRB = new RadioButton("Female");
maleRB.setToggleGroup(genderGroup);
femaleRB.setToggleGroup(genderGroup);
HBox genderBox = new HBox(10, maleRB, femaleRB);
grid.add(genderLabel, 0, 2);
grid.add(genderBox, 1, 2);
// Department (ChoiceBox)
Label deptLabel = new Label("Department:");
TextField deptChoice = new TextField();
grid.add(deptLabel, 0, 3);
grid.add(deptChoice, 1, 3);
// Courses (CheckBoxes)
Label courseLabel = new Label("Select 3 Courses:");
CheckBox course1 = new CheckBox("Java");
CheckBox course2 = new CheckBox("Python");
CheckBox course3 = new CheckBox("Data Structures");
CheckBox course4 = new CheckBox("Algorithms");
CheckBox course5 = new CheckBox("Databases");
VBox courseBox = new VBox(5, course1, course2, course3, course4,
course5);
grid.add(courseLabel, 0, 4);
grid.add(courseBox, 1, 4);
// Enroll Button
Button enrollBtn = new Button("Enroll");
grid.add(enrollBtn, 1, 5);
// Message Label
Label messageLabel = new Label();
grid.add(messageLabel, 1, 6);
// Button action
enrollBtn.setOnAction(e -> {
String name = nameField.getText();
String dept = deptChoice.getText();
********** 16 **********
--- page 17 ---
messageLabel.setText("Hello " + name + ", Your course enrollment in " +
dept + " department is completed");
});
// Scene setup
Scene scene = new Scene(grid, 450, 400);
primaryStage.setScene(scene);
primaryStage.show();
}
public static void main(String[] args) {
launch(args);
}
}
Q7
CO-1;   Demonstrate the effect of using final keyword with a method and a variable
a.   [10]
SO-1,6;   with the help of appropriate codes.
BL-3
Final Variable (5M)
 Final variable : If you make any variable as final, you cannot change the value
of final variable(It will be constant).
 Example of final variable : There is a final variable speedlimit, we are going
to change the value of this variable, but it can't be changed because final
variable once assigned a value can never be changed.
 Code :
class Bike{
final int speedlimit=90; //final variable
void run(){
speedlimit=400;   // changing value of speedlimit
}
}
class Main{
public static void main(String args[]){
Bike b=new Bike();
b.run();
}
}
Final Method (5M) :
 Final method : If you make any method as final, you cannot override it.
 Code :
class Bike{
final void run()
{
System.out.println("running");
}
}
class Honda extends Bike{
void run()   // overriding final method run()
********** 17 **********
--- page 18 ---
{
System.out.println("running safely with 100kmph");
}
}
class Main{
public static void main(String args[]){
Honda h= new Honda();
h.run();
}
}
CO-2;
Explain TreeSet Collection and any five of its methods in detail with the help
SO-1,6;   b.   [10]
of a code.
BL-6
 Java TreeSet class implements the Set interface that uses a tree for storage.
The objects of the TreeSet class are stored in ascending order.
 The important points about the Java TreeSet class are:
 Java TreeSet class contains unique elements only like HashSet.
 Java TreeSet class access and retrieval times are quite fast.
 Java TreeSet class doesn't allow null element.
 Java TreeSet class is non synchronized.
 Java TreeSet class maintains ascending order.
 The TreeSet can only allow those generic types that are comparable.
 Syntax : TreeSet<Integer> abc=new TreeSet<>();
 TreeSet is being implemented using a binary search tree
 Methods of TreeSet : Apart from the methods of SortedSet, Set and
Collections interface, the TreeSet interface also includes these methods:
 higher(element) - Returns the lowest element among those elements
that are strictly greater than the specified element or else returns
NULL
 lower(element) - Returns the greatest element among those elements
that are strictly less than the specified element or else returns NULL
 ceiling(element) - Returns the lowest element among those elements
that are greater than or equal to the specified element.   If
the element passed exists in a tree set, it returns the element passed as
an argument or else returns NULL.
 floor(element) - Returns the greatest element among those elements
that are   less than or equal   to the specified element.   If
the element passed exists in a tree set, it returns the element passed as
an argument or else returns NULL.
 pollFirst() - returns and removes the first element from the set
 pollLast() - returns and removes the last element from the set
 headSet(element, booleanValue) - The headSet() method returns all
the elements of a tree set before the specified element (which is passed
as an argument). The booleanValue parameter is optional. Its default
value is false. If true is passed as a booleanValue, the method returns
all the elements before the specified element including the specified
element.
 tailSet(element, booleanValue) - The tailSet() method returns all the
elements of a tree set after the specified element (which is passed as a
parameter)   including   the   specified element.
The booleanValue parameter is optional. Its default value is true.
If false is passed as a booleanValue, the method returns all the
********** 18 **********
--- page 19 ---
elements   after   the   specified element without including the
specified element.
 subSet(e1, bv1, e2, bv2) - The subSet() method returns all the
elements   between e1 and e2 including e1.   The bv1 and bv2 are
optional parameters. The default value of bv1 is true, and the default
value of bv2 is false. If false is passed as bv1, the method returns all
the elements between e1 and e2 without including e1. If true is passed
as bv2, the method returns all the elements between e1 and e2,
including e1.
********** 19 **********
````
